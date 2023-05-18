shopping_bag = {}
while True:
    print('\n[구입]')
    item = input('상품명? ')
    if item == '':
        break
    else:
        nums = int(input('수량은?'))
        shopping_bag[f'{item}'] = nums
        print(f'장바구니에 {item} {nums}개가 담겼습니다.')

print(f'>>>장바구니 보기: {shopping_bag}')

while True:
    print('\n[검색]')
    search = input('장바구니에서 확인하고자하는 상품은? ')
    ans = shopping_bag.get(search)
    if search == '':
        break
    else:
        if search in shopping_bag :
            print(f'{search}은(는) {ans}개 담겨있습니다.')
        else:
            print(f'{search}은(는) 없습니다.')
