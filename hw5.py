def read_single_digit(n):
    if n == 1:
        print('일', end=' ')
    elif n == 2:
        print('이', end=' ')
    elif n == 3:
        print('삼', end=' ')
    elif n == 4:
        print('사', end=' ')
    elif n == 5:
        print('오', end=' ')
    elif n == 6:
        print('육', end=' ')
    elif n == 7:
        print('칠', end=' ')
    elif n == 8:
        print('팔', end=' ')
    elif n == 9:
        print('구', end=' ')
    elif n == 0:
        print('공', end=' ')
    else :
        '오류가 발생했습니다.'
def read_number(z):
    f = z // 100
    pf = z % 100
    s = pf //10
    t = pf % 10
    read_single_digit(f)
    read_single_digit(s)
    read_single_digit(t)

#주 프로그램부
integer = int(input('세 자리 정수 입력: '))
read_number(integer)
