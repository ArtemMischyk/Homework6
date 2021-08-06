def listsum(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    return sum

print(listsum([1, 3, 5, 7, 9]))





















def func1(*args):
    print(args)
    print(type(args))


func1(1, 2, 3)
func1()
func1('a', 4, -3, 4, 'bb', 3.4)























print("Ноль в качестве знака операции"
      "\nзавершить работу программы")
while True:
    s = input("Знак (+, -, *, /): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")