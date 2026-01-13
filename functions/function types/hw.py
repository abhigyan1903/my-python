try:
    age=int(input("please ,enter your age:"))
    print(age)
    
except age<0:
       raise ValueError
       
except age==0:
       raise ZeroDivisionError
       
except age>0:
      print("corect age")
else:
      print("wrong input")