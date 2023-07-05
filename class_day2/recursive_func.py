# 재귀함수 : 자기 자신을 호출하는 함수
# 특정한 알고리즘, 문제를 풀기 위해서 주로 사용, 
# 어떤 문제를 시간문제적으로 해결하기위해서도 메모리를 이용하여 사용

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

def maze_solver(maze, start, end):
    if start == end:
        return [end]

    x, y = start
    if maze[x][y] == 0:
        return []

    path = []
    if x > 0:
        path = maze_solver(maze, (x-1, y), end)
    if not path and x < len(maze) - 1:
        path = maze_solver(maze, (x+1, y), end)
    if not path and y > 0:
        path = maze_solver(maze, (x, y-1), end)
    if not path and y < len(maze[0]) - 1:
        path = maze_solver(maze, (x, y+1), end)

    if path:
        return [start] + path
    else:
        return []