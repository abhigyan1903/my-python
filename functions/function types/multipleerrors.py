#practising various errors
try:
    num1,num2=eval(input("enter two seperate numbers , each seperated by a comma:"))
    result=num1/num2
    print("your result is",result)
except SyntaxError as se:
    print("syntax error,perhaps you missed a coma",se)
except ZeroDivisionError as ze:
    print("division by zero is considered as an error",ze)
except:
    print("wrong input")
else:
    print("no errors are there")
finally:
    print("finaally we did it!")