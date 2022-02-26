def case1(nums):
    h=nums//(3600)
    m=(nums - h*3600) // 60
    s=nums-(h*3600 + m*60)
    return result

def case2(s):
    h, s = divmod(s, 60 ** 2)
    m, s = divmod(s, 60)
    return '{:02}:{:02}:{:02}'.format(h, m, s)

def case3(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)

print(case2(400000000))