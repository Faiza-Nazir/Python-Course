  #Error and exception Handling
  #Problem 1    Write funtion divide two numbers....
def safe_divide(a,b):
  try:
    divide = a/b
    return divide
  except:
    print("Error: Cannot divide by zero")
print(safe_divide(10,0))
print(safe_divide(20,2))

  #Problem 2   Enter a valid number print thank you.... 
while True:
  try:
     num = int(input("Enter a number: "))  
     print("Thank you")
     break
  except ValueError:
    print("Invalid input.")
    
  #Problem 3    Read file named data.txt....
try:
  with open("data.txt", "r") as f:
    file = f.read() 
    print(file)
    print("File exist")
except FileNotFoundError:
  print("File not found!")
finally:
  print("Operation complete")
  
 # Problem 4    Raise a ValueError if the number is negative....
def check_positive(num):
    if num > 0:
      x = "Positive number"
      return x
    else:
      return "Number must be positive"
print(check_positive(10))
print(check_positive(-5))

    #Problem 5    Write users input to output.txt...
try:
    text = input("Enter a text: ")
    with open("data.txt", "w") as file:
        file.write(text)
    print("Text successfully written to data.txt")
except IOError:
    print("Could not write to file!")
finally:
    print("Writing complete")
    
   #Problem 6   To read log.txt.and append a new line....
try:
    txt = input("Enter some text: ")
    with open("data.txt", "w")as f:
       f.write(txt)
    txt1 = input("Enter some text: ")
    with open("data.txt" , "a")as f:
      f.write(txt1)
    with open("data.txt" , "r")as f:
      f = f.read()
    print(f)
except FileNotFoundError:
  print("file not exist create new file!")
finally:
  print("operation done")

    #Problem 7   find bug in this function. Use print statements.....
def multiply_list(lst):
  result = 0
  print(result)
  for num in lst:
   print(num)
  result *= num
  print(result)
  return result
 
print(multiply_list([1, 2, 3, 4]))

    #Problem 8   Converts a user input to an integer....
try:
    num = int(input("Enter a number: "))
    divide = num/100
    print(divide)
except ValueError:
  print("Not a number!")
except ZeroDivisionError:
  print("Cannot divide by zero!")

   #Find second largest number
num = [35,80,34,67,98,100,90,102]
max= 0
sec = 0
for i in num:
    if i > max:
      sec= max
      max= i
print(max)
print(sec)   

    #sorting a number in the list 
lst = [6,8,3,9,10]
list = []
while lst:                    
  smaller = lst[0]           
  for i in lst:            
        if i < smaller:      
            smaller = i
  list.append(smaller)  
  lst.remove(smaller)
print(list)

     #Swapping a number
num = [2,3,4,5,6,7]
num[0],num[-1] = num[-1],num[0]
num[1],num[-2] = num[-2],num[1]
num[2],num[-3] = num[-3],num[2]
print(num)
   




