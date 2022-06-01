def solution(numbers):
    answer = set()
    nlist = []
    for i in numbers: nlist.append(int(i))
    def maken(n, elsen):
        chk = True
        for i in range(2, n):
            if n > 2 and n % i == 0:
                chk = False
                break
        if chk and n > 1: 
            answer.add(n)
        for i in range(len(elsen)):
            tmp = n * 10 + elsen[i]
            maken(tmp, elsen[0:i] + elsen[i + 1:])
    for i in range(len(nlist)):
        maken(nlist[i], nlist[0:i] + nlist[i + 1:])
    return len(answer)
