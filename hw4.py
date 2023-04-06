def rep_char(c,n):
    print(str (c * n))

def draw_line_string(num):
    rep_char('-',num)

def make_welcome_sign(name):
    msg1 = f'Hello {name},'
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    draw_line_string(nstr)
    print(msg1)
    print(msg2)
    draw_line_string(nstr)
    
make_welcome_sign(input('input his/her name: '))
