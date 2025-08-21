from ctypes import HRESULT

fac=int(input("Enter a number: "))
def factorial(n):
    if n<2:
        return  1
    else:
        return n*(factorial(n-1))
result=factorial(fac)
print(f"factorial of {fac} is:" ,result)

