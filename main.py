print("Калькулятор")
print("Введите первое число:")num1 = float(input())
print("Введите второе число:")num2 = float(input())
print("Выберите операцию (+, -, *, /):")
operator = input()if operator == "+": result = num1 + num2
  elif operator == "-": result = num1 - num2
  elif operator == "*": result = num1 * num2
  elif operator == "/": result = num1 / num2
  else: print("Некорректная операция") 
result = None
if result is not None: 
  print("Результат:", result)
