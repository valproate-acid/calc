def main():
    a =  int(input())
    c = input()
    b = int(input())

    result =0

    
    if(c=="+"):
        result =add(a,b)
    elif(c=="-"):
        result = minus(a,b)
    elif(c=="*"):
        result = mul(a,b)
    elif(c=="/"):
        result = div(a,b)
    print(f"{a} {c} {b} = {result}")

def mul(a, b):
    return a*b

def div(a, b):
    if b == 0:
        return "error"
    return a/b

def add(num1,num2):
    return num1+num2
def minus(num1,num2):
    return num1-num2

if __name__ == "__main__":
    main()
