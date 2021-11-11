def solution(dirs):
    visited_v = [[False for _ in range(10)] for _ in range(11)]
    visited_h = [[False for _ in range(11)] for _ in range(10)]

    position = [5, 5]

    answer = 0
    for i in dirs:
        if i == 'U':
            if position[1] < 10:
                if visited_h[position[1]][position[0]] == False:
                    answer += 1
                    visited_h[position[1]][position[0]] = True
                position[1] += 1
        if i == 'D':
            if position[1] > 0:
                if visited_h[position[1]-1][position[0]] == False:
                    answer += 1
                    visited_h[position[1]-1][position[0]] = True
                position[1] -= 1
        if i == 'L':
            if position[0] > 0:
                if visited_v[position[1]][position[0]-1] == False:
                    answer += 1
                    visited_v[position[1]][position[0]-1] = True
                position[0] -= 1
        if i == 'R':
            if position[0] < 10:
                if visited_v[position[1]][position[0]] == False:
                    answer += 1
                    visited_v[position[1]][position[0]] = True
                position[0] += 1

    return answer


a = "LULLLLLLU"
print(solution(a))