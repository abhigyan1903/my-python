#cube
def c(h):
    return h*h*h
#duvisble by three
def div(h):
    if h%3==0:
        return c(h)
             
        
    else:
        return False
num1=int(input("please enter your number"))
print("the cube of your number is",div(num1))