#using pass statement
for j in range(50):
    if j%3==0:
        print("huff")
    elif j%2==0:
        print("buzz")
    elif j%5==0:
        pass
    else:
        print(j)