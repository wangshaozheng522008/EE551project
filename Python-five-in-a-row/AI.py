def scan(cb):
    grade = [[0 for i in range(15)] for j in range(15)]
    for i in range(15):
        for j in range(15):
            if cb[i][j] == 0:
                x = i
                y = j
                t = 0
                while x - 1 >= 0 and cb[x-1][y] == -1:
                    grade[i][j] += 100
                    x -= 1
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500
                x = i
                y = j
                t = 0
                while x - 1 >= 0 and cb[x-1][y] == 1:
                    grade[i][j] += 95
                    x -= 1
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490
                x = i
                y = j
                t = 0
                while y - 1 >= 0 and cb[x][y - 1] == -1:
                    grade[i][j] += 100
                    y -= 1
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500
                x = i
                y = j
                t = 0
                while y - 1 >= 0 and cb[x][y - 1] == 1:
                    grade[i][j] += 95
                    y -= 1
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490

                x = i
                y = j
                t = 0
                while x + 1 <= 14 and cb[x + 1][y] == -1:
                    x += 1
                    grade[i][j] += 100
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500
                x = i
                y = j
                t = 0
                while x + 1 <= 14 and cb[x + 1][y] == 1:
                    x += 1
                    grade[i][j] += 95
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490
                x = i
                y = j
                t = 0
                while y + 1 <= 14 and cb[x][y + 1] == -1:
                    y += 1
                    grade[i][j] += 100
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500
                x = i
                y = j
                t = 0
                while y + 1 <= 14 and cb[x][y + 1] == 1:
                    y += 1
                    grade[i][j] += 95
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490

                x = i
                y = j
                t = 0
                while x - 1 >= 0 and y - 1 >= 0 and cb[x - 1][y - 1] == -1:
                    grade[i][j] += 100
                    x -= 1
                    y -= 1
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500
                x = i
                y = j
                t = 0
                while x - 1 >= 0 and y - 1 >= 0 and cb[x - 1][y - 1] == 1:
                    grade[i][j] += 90
                    x -= 1
                    y -= 1
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490
                x = i
                y = j
                t = 0
                while x + 1 <= 14 and y - 1 >= 0 and cb[x + 1][y - 1] == -1:
                    grade[i][j] += 100
                    x += 1
                    y -= 1
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500
                x = i
                y = j
                t = 0
                while x + 1 <= 14 and y - 1 >= 0 and cb[x + 1][y - 1] == 1:
                    grade[i][j] += 90
                    x += 1
                    y -= 1
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490
                x = i
                y = j
                t = 0
                while x + 1 <= 14 and y + 1 <= 14 and cb[x + 1][y + 1] == -1:
                    x += 1
                    y += 1
                    grade[i][j] += 100
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500

                x = i
                y = j
                t = 0
                while x + 1 <= 14 and y + 1 <= 14 and cb[x + 1][y + 1] == 1:
                    x += 1
                    y += 1
                    grade[i][j] += 90
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490
                x = i
                y = j
                t = 0
                while x - 1 >= 0 and y + 1 <= 14 and cb[x - 1][y + 1] == -1:
                    x -= 1
                    y += 1
                    grade[i][j] += 100
                    t += 1
                    if t == 3: grade[i][j] += 200
                    if t == 4: grade[i][j] += 500
                x = i
                y = j
                t = 0
                while x - 1 >= 0 and y + 1 <= 14 and cb[x - 1][y + 1] == 1:
                    x -= 1
                    y += 1
                    grade[i][j] += 90
                    t += 1
                    if t == 3: grade[i][j] += 190
                    if t == 4: grade[i][j] += 490

    return grade


def cmax(list):
    for i in range(15):
        if list[i] == max(list):
            return i


def sort(grade):
    L = []
    P = []
    for i in range(15):
        L.append(max(grade[i]))
        P.append(cmax(grade[i]))
    for j in range(15):
        if L[j] == max(L):
            return j, P[j]


def AIgo(cb):
    grade = scan(cb)
    x, y = sort(grade)
    print(grade[x][y])
    return x, y



