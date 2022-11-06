def div(a,b):           # Decorder is improve the fuunction withot touch the fuunction
    # if a<b:
    #     a,b = b,a
    print(a/b)

def smart_div(func):
    def inner(a,b):            #function inside the function,  name can be different    
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner
   
div(4,2)    

div1 = smart_div(div)
div1(2,4)
div(2,4)
