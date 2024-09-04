t = int(input())
strToNum = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
numToStr = {0: "ZRO",1: "ONE",2: "TWO",3: "THR",4: "FOR",5: "FIV",6: "SIX",7: "SVN",8: "EGT",9: "NIN"}

for test_case in range(1, t+1):
    test = list(input().split())
    number = list(input().split())

    for i in range(len(number)):
        number[i] = strToNum[number[i]]

    number.sort()

    for i in range(len(number)):
        number[i] = numToStr[number[i]]

    print(f'#{test_case}')
    print(*number)