# bye using loops
valid=True
while valid:
    try:
        num1=int(input("enter your first number:"))
        while num1%2==0:
            print("bye")
        valid=False
    except ValueError as ve:
        print("print odd number wrong input",ve)
    finally:
        print("done")
        
        