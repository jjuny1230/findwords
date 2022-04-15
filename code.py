# 파일 읽는 부분
with open("code.txt", "r") as f:
    data = f.read()

# 각 줄마다 자르기
a = data.split("\n")

for y in range(len(a)):
    for x in range(len(a[0])):
        # a 가 있는 위치 찾기
        if a[y][x] == 'a':
            print(x, y)
