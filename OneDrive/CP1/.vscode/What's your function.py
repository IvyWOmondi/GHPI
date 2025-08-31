import math
#Takes a number down to the nearest whole number
#floor function
arg1=float(input("Enter the first number (num1) here:" ))
arg2=float(input("Enter the second number (num2) here:" ))
result=(math.floor(arg1))
result2=(math.floor(arg2))
print(f"The two numbers {arg1}, and {arg2} rounded down are ({result},{result2})")
#main function from function video
def add(x, y):
    return x + y
def multiply(m,n):
    return m * n
def calculate(a,b):
    sum_value= add(a,b)
    product_value=multiply(a, b)
    return sum_value, product_value
def main():
    num1=5
    num2=3
    sum_result, product_result = calculate(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")
    print(f"The product of {num1} and {num2} is {product_result}")
if __name__ =="__main__":
    main()

