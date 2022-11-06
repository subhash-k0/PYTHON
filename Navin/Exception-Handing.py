a= 5
b= 3

try:
    print("Resource Open")
    print(a/b)
    k= int(input("Enter a number = "))
    print(k)

# except Exception as e:
#     print("Hey , You cannot divide a number by zero", e) 

except ZeroDivisionError as e:
    print("Hey , You cannot divide a number by zero", e) 

except ValueError as e:
    print("Invlid Input")

except Exception as e:
    print("something went Wrong")


finally:
    print("resorce Closed")   