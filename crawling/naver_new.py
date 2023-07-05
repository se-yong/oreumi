from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd



# beautifulSoup = 웹상의 정적인 페이지를 크롤링 하는데 주로 사용

# selenium = 웹 상에서 정적인 페이지를 탐색하는데 사용하던 beautifulsoup같은 패키지가 하지 못하는 동적인 크롤링을 지원한다. 
# 동적인 크롤링이란 url상에는 아무런 변화없이 동작하는 웹 페이지에 대한 크롤링을 의미한다.

# 정적인 페이지 vs 동적인 페이지
# 정적인 페이지는 현재 서버에 HTML 파일과 같은 형태로 직접 올려져 있어 서버에서 요청하지 않아도 이용 가능한 페이지를 말한다.
# 동적인 페이지는 반대로 사용을 위해서는 파일을 사용할때마다 서버에 요청해 받아 와야 하는 페이지.

# 간단히 설명하자면 옷가게에서 옷걸이에 걸린 옷들은 가져가서 바로 계산할 수 있지만
# 쇼케이스에 전시된 옷들은 점원에게 사이즈 요청해야만 구매 할수 있다.
# 서버가 옷가게라면 직접 전시되어 있는 옷걸이의 옷들은 '정적인 페이지', 
# 창고안에 있어서 존재하지만 유저가 함부로 건드리지 못하는 옷은 '동적인 페이지'

# selenium 의 By 는 이전 셀레니움이 업그레이드 되면서 생긴 모듈로 html에서 원하는 부분을 찾을 때
# find_element나 find_elements를 이용하는데, 이때 사용한다. by의 영어 뜻처럼 '~~을 이용하여' 찾는다.
# By.TAG_NAME, By.CSS_SELLECTOR, By.LINK_TAG, By.NAME, By.Id 등이 존재 한다.



# 입력된 수를 페이지 url 형식에 맞게 변경
# 1, 11, 21, 31, ---

def makePgNum(num):
	if num == 1:
		return num
	elif num == 0:
		return num + 1
	else:
		return num + 9 * (num - 1)


# 크롤링할 URL 을 생성하는 함수
# search = 검색할 단어
# start_pg = 검색을 시작할 페이지
# end_pg = 검색을 끝낼 페이지
def makeUrl(search, start_pg, end_pg):

	# 생성된 url을 저장할 리스트 초기화
	urls = []

	# start =end 이면 start 만으로 끝내기
	if start_pg == end_pg:
		# 이 때 url의 형식을 따라야 하기 때문에 makePgNum으로 page에 맞는 형식으로 변경
		start_page = makePgNum(start_pg)
		url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(
			start_page)
		urls.append(url)
		print("생성url: ", urls)
		return urls
	
	# start != end 이면 start부터 end가 될 때까지 URL을 생성해서 urls에 넣어주기
	else:
		for i in range(start_pg, end_pg + 1):
			page = makePgNum(i)
			url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(
			page)
		print("생성url: ", urls)
		return urls



# 검색창을 띄워 주기 위한 함수
def input_start():

	# 사용자 입력
	# 검색어
	search = input("검색할 단어?\n")

	#시작 페이지
	page_start = int(input("시작페이지?"))
	print(f"시작할 페이지: {page_start}")

	# 끝 페이지
	page_end = int(input("종료페이지?"))
	print(f"종료할 페이지: {page_end}")


	# 네이버 url 생성
	search_urls = makeUrl(search, page_start, page_end)
	# 앞서 사용자가 입력한 값들을 이용하여 페이지에 삽입
	

	# selenium 을 이용하여 navernews 만 뽑아 오기 위한 작업 시작
	# OS를 안 따지는 크롬을 이용하여 진행
	# 크롬 열기
	driver = webdriver.Chrome()
	# implicitly_wait(n) = n초안에 페이지가 열리면 바로 넘어가고 아니면 n초까지 기다리기
	# time.sleep = n초동안 기다리기
	# 페이지가 열린 후에도 계속해서 기다리면 시간적 효율이 떨어지니 켜지면 끄기 위해 사용
	driver.implicitly_wait(3)


	# 크롤링할 네이버 뉴스 url 저장할 리스트 제작
	naver_urls = []


	# 본격적인 selenium으로 검색한 페이지 로드

	# 위에서 입력받은 검색할 naver 검색 url을 하나씩 실행 (한개든 여러개든 리스트 형식이니 요소를 받아와서 실행)
	for i in search_urls:

		# i = naver 검색 쿼리로 만들어진 url 하나
		# selenium 드라이버에 url 값 입력
		driver.get(i)
		time.sleep(3)		# 대기시간은 너무 빠르게 열렸다 닫혔다 하는걸 방지 - 즉 시간은 바꿔도 상관 없음

		# 네이버 기사 열어서 제목 및 본문 가져오기

		# 검색해서 떠있는 창에서 기사를 열수 있는 css selector 모아오기 - 즉 a링크(하이퍼 링크)
		a = driver.find_elements(By.CSS_SELECTOR, 'a.info')

		# 받아온 a 마다 실행 시키기
		for i in a:
			# a 값마다 클릭해서 실행
			i.click()

			# 드라이버를 이용해 윈도우, 즉 현재 열린 창을 1번으로 변경(handling) 
			# 시작은 0 이기에 검색창 은 0번 윈도우, 기사창은 검색 다음이기에 1번 윈도우
			driver.switch_to.window(driver.window_handles[1])
			time.sleep(3)		# 열고 나서 대기

			# 열린 페이지의 url을 url 변수에 저장
			url = driver.current_url
			print(url)			# 저장 확인
			
			# naver news만 받아오고 싶으니 확인
			# url 에 news.naver.com 이 존재하면 네이버 뉴스로 판단
			if "news.naver.com" in url:
				naver_urls.append(url)		#확인된 url naver_urls에 저장

			#현재 보고있는 페이지 종료
			driver.close()

			#다시 윈도우를 0번 - 검색창으로 변경
			driver.switch_to.window(driver.window_handles[0])
		


# 아래의 한줄은 임포트 된 명령이 아닌 직접 인터프리터로 실행 되야만 실행 하도록 하는 코드
# 즉 이 py 파일을 다른데서 참조한것이 아닌 직접 돌려야만 __name__ == __main__ 이 되어 아래의 코드가 실행
if __name__ == "__main__":
	
	# 검색어를 그냥 직접 집어넣었으니, 검색어를 직접 초기화
	search = "나비"

	# 위의 검색어로 검색했을 때 나오는 url들을 입력
	naver_urls = ['https://sports.news.naver.com/news.nhn?oid=442&aid=0000163350', 
	       		  'https://n.news.naver.com/mnews/article/001/0014045673?sid=103', 
		   		  'https://n.news.naver.com/mnews/article/366/0000913600?sid=101', 
		   		  'https://n.news.naver.com/mnews/article/025/0003290622?sid=102']

	# ConnectionError를 방지한다.
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102"}


	# 제목과 컨텐츠를 넣을 리스트 제작
	titles = []
	contents = []

	for url in naver_urls:
		# 현재 페이지를 request를 이용해 정적인 페이지로 전환
		orginial_html = requests.get(url, headers=headers)
		# 정적인 페이지의 내용을 받아온다.
		html = BeautifulSoup(orginial_html.text, "html.parser")

		# 네이버 뉴스의 기사 제목이 들어가 있는 부분을 이용해 제목만 가져오자
		title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
		# 가져온 html 의 기사제목은 리스트 타입으로, 이를 문자형으로 변환 시켜줘야함
		title = ''.join(str(title))

		# 정규 표현식을 이용하여 HTML 태그를 제거
		pattern1 = r'<[^>]*>'
		title = re.sub(pattern=pattern1, repl='', string=title)
		
		# 제목 저장
		titles.append(title)

		# 네이버의 컨텐츠가 들어있는 부분을 가져와서 넣자
		#기사의 텍스트만 가져와서 리스트를 합쳐 문자열 변환 해주기
		content = html.select("div#dic_area")
		content = ''.join(str(content))

		# 정규 표현식을 이용하여 HTML 태그를 제거
		content = re.sub(pattern=pattern1, repl='', string=content)
		
		# 정규 표현식을 이용하여 필요없는 부분 제거
		pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
		content = content.replace(pattern2,  '')
		
		#컨텐츠 저장
		contents.append(content)

print(titles)
print(contents)


# pandas를 이용해 데이터 정리
news_df = pd.DataFrame({'title':titles, 'link': naver_urls, 'content': contents})

# 정리된 데이터를 NaverNews_검색어 라는 이름의 csv 파일로 저장
news_df.to_csv(f'NaverNews_{search}.csv', index=False,  encoding='utf-8')