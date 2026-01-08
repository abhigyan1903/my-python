#practising value error

try :
    a=int(input("please enter a number:"))
    print("you entered:",a)
except ValueError as va:
    print("oh no!the exception is:",va)
finally:
    print("yayy!")