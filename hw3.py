def get_fixed_price(after) :
    before = after * (100/(100-dc))
    return before

dc = float(input('할인율은?'))
A = int(input('A 상품의 할인 된 가격은?'))
B = int(input('B 상품의 할인 된 가격은?'))
result_A = get_fixed_price(A)
result_B = get_fixed_price(B)
print("A", "상품의 정가는", result_A)
print("B", "상품의 정가는", result_B)
