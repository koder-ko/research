li = [20, 21, 22, 24]


def checking(d, li):
    for i in range(len(li)):
        for k in range(i, len(li)):
            for j in range(k, len(li)):
                if i + k == j + d or i + j == k + d or i + d == j + k:
                    print("성립X")
                    return False
    print("성립")
    return True

num = 0

a = 1
b = 2
c = 3

while num < 1000:
    checking(li[len(li) - 1] + c, li)
    a = b
    b = c
    c = a + b
    num += 1