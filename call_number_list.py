def solution(phone_book):
    '''
    phone_book.sort(key=len)
    bef = 0
    teleport = [len(phone_book)] * len(phone_book)
    for i in range(1, len(phone_book)):
        if len(phone_book[i - 1]) < len(phone_book[i]):
            for j in range(bef, i): teleport[j] = i
            bef = j
    for i in range(len(phone_book) - 1):
        for j in range(teleport[i], len(phone_book)):
            if phone_book[j].startswith(phone_book[i]): return False
        '''
    phone_book.sort()
    i = 0
    while i < len(phone_book):
        j = i
        while j < len(phone_book):
            if not phone_book[j].startswith(phone_book[i]): i = j
            elif phone_book[j].startswith(phone_book[i]) and i != j: return False
            j += 1
        i += 1
    return True
