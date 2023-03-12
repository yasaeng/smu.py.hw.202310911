def get_radius(prompt='넓이를 구하고자 하는 원의 반지름은?'):
    r = int(input(prompt))
    return r

def get_circle_area(r):
    a = (3.14) * r * r
    print('반지름', r,"인 원의 넓이 = 3.14 x", r,'x', r, '=', end='') 
    return a

print('strat')
input_r = get_radius()
result = get_circle_area(input_r)
print(result)
print('finish')
