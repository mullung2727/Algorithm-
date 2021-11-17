def solution(rows, columns, queries):
    ls = [[0 for _ in range(columns)] for _ in range(rows)]
    i = 1
    answer = []
    for x in range(rows):
        for y in range(columns):
            ls[x][y] = i
            i += 1

    for x1, y1, x2, y2 in queries:
        min_n = 10001
        temp = ls[x1 - 1][y1 - 1]
        for y in range(y1, y2):
            temp2 = ls[x1 - 1][y]
            ls[x1 - 1][y] = temp
            temp = temp2
            min_n = min(min_n, temp)

        for x in range(x1, x2):
            temp2 = ls[x][y2 - 1]
            ls[x][y2 - 1] = temp
            temp = temp2
            min_n = min(min_n, temp)

        for y in range(y2 - 2, y1 - 2, -1):
            temp2 = ls[x2 - 1][y]
            ls[x2 - 1][y] = temp
            temp = temp2
            min_n = min(min_n, temp)

        for x in range(x2 - 2, x1 - 2, -1):
            temp2 = ls[x][y1 - 1]
            ls[x][y1 - 1] = temp
            temp = temp2
            min_n = min(min_n, temp)
        answer.append(min_n)
    return answer


rows, columns = 6, 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

ls = solution(rows, columns, queries)

print(ls)