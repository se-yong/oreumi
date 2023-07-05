import os

foler_path = "C:\\Users\\Se-yong.park\\oreumi\\data-center"

if not os.path.exists(foler_path):
    os.makedirs(foler_path)
    print(f"폴더 '{foler_path}'를 생성했습니다.")
else:
    print(f"폴더 '{foler_path}'를 이미 존재합니다.")