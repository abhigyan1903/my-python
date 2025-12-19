#finding the factorial of a number
def fact(d):
    ''' this function finds the factorial of a number'''
    if d==1 or d==1:
        return 1
    else:
        return d*fact(d-1)
num=int(input("please enter the number you want to factorise"))
print("the factorial of your number is",fact(num))
print(fact.__doc__)                 