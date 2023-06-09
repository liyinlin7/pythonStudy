

def rate_math_2(a, b):
    g = 1 / (1/a + 1/b)
    print(g)
    g_ = g - 0.0125
    print(g_)
    a1 = a / g
    b1 = b / g
    a_ = a1 * g_
    b_ = b1 * g_
    print("选项a的值：", a_)
    print("选项b的值：", b_)

def rate_math_3(a, b, c):
    g = 1 / (1/a + 1/b + 1/c)
    print(g)
    g_ = g - 0.0125
    print(g_)
    a1 = a / g
    b1 = b / g
    c1 = c / g
    a_ = a1 * g_
    b_ = b1 * g_
    c_ = c1 * g_
    print("选项a的值：", a_)
    print("选项b的值：", b_)
    print("选项c的值：", c_)


if __name__ == '__main__':
    rate_math_2(7.06, 1.05)
    # rate_math_3(4.30, 1.65, 3.50)
