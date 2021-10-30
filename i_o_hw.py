
# 1/ Read all of the content of the file in one variable.

file = open("student_names.txt","r+")
students = file.read()
print(students)

# 2/ Write a list of random names to your file.

list = "Zack Peterson\nJarrett Bate\nJair Dudley\nLia Cuevas\n"
file.write(list)

# 3/ Read the first n lines of the file.
file = open("student_names.txt","r")
lignes = int(input("Enter the number of lignes you want to read from the begining of file :"))
for i in range(0,lignes):
    print(file.readline())
   
# 4/ Read the last n lines of the file.
file.seek(0,0)
n = int(input("Enter the number of lignes you want to read from the end of file :"))
for i in (file.readlines()[-n:]):
    print(i)
   

# 5/ Check if the name x is in the file.
file.seek(0,0)
name = input("Enter the name you are searching for : ")
names = file.read()
print(name + " is in the file ? ", name in names)
file.close()

# 6/ Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
bool = int(input("Enter 0 if you want to generate 26 text files : "))
if bool==0 : 
  list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for i in range(0,26) :
     f = list[i]+'.txt'
     file1 = open(f,"w")
  print("Program Ended!")
else : 
    print("Program Ended!")



