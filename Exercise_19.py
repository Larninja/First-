char = "radar"

def student_things(allstd): 
    lengths = []
    for student in allstd: 
        lengths.append(len(student))
        
    print(allstd[::-1])

    print(lengths)
    
#student_things(char)
    

        
def paridrome(name):
     if name[::1] == name[::-1]:
       return True
        
     else:
       return False
        
name = input("Input your name: ")
#print(paridrome(name))

num = []
def sums_nums(numbers):
   sums = 0
   for number in numbers: 
      sums += number
   print(numbers)
   print("the sums is: ",sums)
   
for i in range(9):
   n = float(input(f"Input a number ({i}): "))
   num.append(n)

sums_nums(num)
      
   
