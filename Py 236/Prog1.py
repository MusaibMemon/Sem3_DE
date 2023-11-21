# write a prog to get integer solution of x^2 - 2y^2 =1 for range 1 to 100

def equ(x,y):
    for x in range(1,101):
        for x in range(1,101):
            if x ** 2 - 2 * y ** 2 == 1:
                print(x,y)
equ(1,2)