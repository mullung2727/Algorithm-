def solution(phone_book):
    phone_book.sort(key= lambda x: len(x))
    prev = len(phone_book[0])
    len_ls = [len(phone_book[0])]
    dic = {phone_book[0]:True}
    for i in range(1,len(phone_book)):
        now = len(phone_book[i])
        for j in len_ls:
            if dic.get(phone_book[i][:j]):
                return False
        dic[phone_book[i]] = True
        if now > prev:
            len_ls.append(now)
            prev = now

    return True

pb = ["12","11235","567","88","1212121212"]
print(sorted(pb))
print(solution(pb))

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solution(pb))