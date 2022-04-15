# 파일 읽는 부분
with open("code.txt", "r") as f:
    data = f.read()

# 각 줄마다 자르기
a = data.split("\n")

result = []

word = "improve"
for y in range(len(a)):
    for x in range(len(a[0])):
        # a 가 있는 위치 찾기
        if a[y][x] == word[0]:
            # 오른쪽 가로
            check = True
            if x + len(word) - 1 < len(a[0]):
                for b in range(len(word)):
                    if a[y][x + b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # 왼쪽 가로
            check = True
            if x - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y][x - b] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # 아래로 내려가는 세로
            check = True
            if y + len(word) - 1 < len(a):
                for b in range(len(word)):
                    if a[y + b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

            # 위로 올라가는 세로
            check = True
            if y - len(word) + 1 >= 0:
                for b in range(len(word)):
                    if a[y - b][x] != word[b]:
                        check = False
                        break
                if check:
                    result.append([x, y])

print(result)
