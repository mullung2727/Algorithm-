# 사용횟수 i -> j+k = i가 되도록 조합한 것(j, k >= 1)에 사칙연산한 값 + N*i*11
def combi(n, i_th, prev_combi, target):
    if i_th == 1:
        if target == n:
            return True
        return [set([n])]
    add_set = set()
    add_set.add(n * int('1'*i_th))
    for j in range(1, i_th//2+1):
        k = i_th-j
        part1 = prev_combi[j-1]
        part2 = prev_combi[k-1]
        for jj in part1:
            for kk in part2:
                add_set.add(jj+kk)
                add_set.add(jj-kk)
                add_set.add(kk-jj)
                add_set.add(jj*kk)
                if jj: add_set.add(kk//jj)
                if kk: add_set.add(jj//kk)
        for ll in add_set:
            if ll == target:
                return True
    print(add_set)
    prev_combi.append(add_set)
    return prev_combi

def solution(n, number):
    combi_ls = []
    for i in range(1, 9):
        combi_ls = combi(n, i, combi_ls, number)
        if combi_ls == True:
            return i
    return -1

print(solution(5, 31168))

