def fib(n):
    a = 0
    b = 1

    if n== 1:
        print(a)
    else:    
        print(a)
        print(a)

        for i in range(2,n):
            c = a + b
            a=b
            b=c
            print(c)

fib(5)    