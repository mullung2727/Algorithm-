import math
def gcd(w,h):
    return w if h%w == 0 else gcd(h%w, w)
def solution(w,h):
    cnt = 0
    if w > h:
        w,h = h,w
    div = gcd(w,h)
    origin_w = w
    origin_h = h
    w //= div
    h //= div
    prev = h
    loss = 0
    for x in range(1,w+1):
        now = -h/w*x+h
        if now == int(now):
            loss += prev - now
            prev = now
        else:
            loss += prev - int(now)
            prev = int(now+1)


    loss = loss * div
    answer = (origin_w*origin_h-loss)
    return int(answer)