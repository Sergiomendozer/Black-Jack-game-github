def return_5(x):
    str = "5"
    return (str)

def caller(t):
    z = int(return_5(t))
    w = t + z
    print (w)

caller(int(input("number to add 5:")))
