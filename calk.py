print('''
           ____________________
          |                    |
          |   Калькулятор v1   |
          |____________________|
                                  ''')   

what = input("Знак действия==>:")
a = float( input("Первое число==>:") )
b = float( input("Второе число==>:") )

if what == "+":
    c = a + b
    print("Результат===>:" + str(c))
elif what == "-":
    c = a - b
    print("Результат===>:" + str(c))
elif what == "*":
    c = a * b
    print("Результат===>:" + str(c))
elif what == "/":
    c = a / b
    print("Результат===>:" + str(c))
else:
    print("Неверная операция!! можно только + , - , * , /!! ")
