# exercise A
age = int(input("How old are you? "))
print('your age is: ', age)

# exercise B
name_player_one = str(input("what's your name? "))
age_player_one = int(input("how old are you? "))

name_player_two = str(input("what's your name? "))
age_player_two = int(input("how old are you? "))

if(age_player_one > age_player_two): 
  print(name_player_one," is older!!")
else:
  print(name_player_two," is older!!")

# exercise C
name_user = str(input("What's your name? "))
age_user = int(input("How old are you? "))

if age_user >= 18: 
  print("Você é adulto”, quando a idade digitada for maior ou igual a 18")
if 13 < age_user < 18:
  print("Você é adolescente”, quando a idade digitada for menor do que 18 e maior do que 13")
if 0 <= age_user <= 13:
  print("Você é criança”, quando a idade digitada for maior ou igual a 0 e menor ou igual a 13")
if age_user < 0: 
  print("Idade inválida”, quando a idade digitada for menor do que 0")

# exercise D
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))
num4 = int(input("enter a number: "))

soma = (num1 + num2 + num3 +  num4) 
if soma % 2 == 0:
  print("pair")
else: 
  print("odd") 

# exercise E
numbers = []
for _ in range(5):
  nums = int(input("enter a number: "))
  numbers.append(nums)

for nums in numbers: 
  if nums > 0:
    print("positivo")
  elif(nums < 0):
    print("negativo")
  else:
    print("zero")
