def solution(phone_book):
    phone_book.sort(key= lambda x: len(x))
    prev = len(phone_book[0])
    len_ls = [0]
    for i in range(len(phone_book)-1):
        now = len(phone_book[i])
        if now > prev:
            len_ls.append(i)
            prev = now
    for idx1, idx2 in zip(len_ls[:-1], len_ls[1:]):
        for i in range(idx1, idx2):
            pn = phone_book[i]
            for j in range(idx2, len(phone_book)):
                if phone_book[j].startswith(pn):
                    return False

    return True