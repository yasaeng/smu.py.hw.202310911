def exchange(amount):
    a = amount
    n500 = a // 500
    a %= 500
    n100 = a // 100
    a %= 100
    n50 = a // 50
    a %= 50
    n10 = a // 10
    a %= 10
    print("500원 동전의 개수:" , n500)
    print("100원 동전의 개수:", n100)
    print("50원 동전의 개수:", n50)
    print("10원 동전의 개수:", n10)

def get_integer(prompt) :
    res = int(input(prompt))
    return res

m = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(m)

