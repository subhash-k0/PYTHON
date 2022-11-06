def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)


def main():
  result = fact(5)
  print(result)        
  print(__name__)