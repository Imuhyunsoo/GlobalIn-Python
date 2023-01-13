okane  = int(input("지폐로 교환할 돈은 얼마? "))

if(okane >= 50000):
    omanwon = okane // 50000
    okane %= 50000
    print("50000원짜리 ==> ", omanwon, "장")
if(okane >= 10000):
    manwon = okane // 10000
    okane %= 10000
    print("10000원짜리 ==> ", manwon, "장")
if(okane>=5000):
    osenwon = okane // 5000
    okane %= 5000
    print("5000원짜리 ==> ", osenwon, "장")
if(okane>=1000):
    senwon = okane // 1000
    okane %= 1000
    print("1000원짜리 ==> ", senwon, "장")
    print("지폐로 바꾸지 못한 돈 ==>", okane, "원")
