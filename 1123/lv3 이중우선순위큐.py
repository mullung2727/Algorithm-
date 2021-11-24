def insert_val(n, ls):
    if not ls:
        ls.append(n)
        return ls
    start = 0
    end = len(ls) - 1
    mid = (start + end) // 2
    mid_val = ls[mid]
    pre_mid = mid
    cnt = 0
    while n <= ls[end] and n >= ls[start]:
        cnt += 1
        if n > mid_val:
            start = mid - 1
            mid = (start + end) // 2
            if mid == pre_mid:
                ls.insert(mid+1, n)
                break
            mid_val = ls[mid]
            pre_mid = mid
        elif n < mid_val:
            end = mid - 1
            mid = (start + end) // 2
            if mid == pre_mid:
                ls.insert(mid, n)
                break
            mid_val = ls[mid]
            pre_mid = mid
        else:
            ls.insert(mid, n)
            break
    if cnt == 0:
        if n < ls[0]:
            ls.insert(0, n)
        else:
            ls.append(n)
    return ls

def solution(operations):
    ls = []
    for o in operations:
        act, n = o.split()
        if act == "I":
            # print(n, ls)
            ls = insert_val(int(n), ls)
        else:
            if len(ls) > 0:
                if n == "-1":
                    ls.pop(0)
                else:
                    ls.pop()
        # print(111,ls)
    if ls:
        return [ls[-1], ls[0]]
    else:
        return [0,0]

operators = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operators))