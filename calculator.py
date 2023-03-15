# Ask for the first number
print('what is the first number?')
num1 = input()
# Ask for the function to be performed
print('what is the sign?')
sign = input()
# Ask for the second number
print('what is the second number?')
num2 = input()


if sign == '+':
    answer = (str(int(num1) + int(num2)))
    print(answer)
if sign == '+':
    answer = (str(int(num1) + int(num2)))
    print(answer)
elif sign == '-':
    answer = (str(int(num1) - int(num2)))
    print(answer)
elif sign == '/':
    answer = (str(int(num1) / int(num2)))
    print(answer)
elif sign == '*':
    answer = (str(int(num1) * int(num2)))
    print(answer)
else:
    print("invalid sign. Please put valid sign")



