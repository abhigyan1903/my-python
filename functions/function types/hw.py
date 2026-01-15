try:
    age=int(input("please ,enter your age:"))
    print(age)
    
except age<0:
       raise ValueError
       
except :
       raise ZeroDivisionError
       
except :
      print("corect age")
else:
      print("wrong input")