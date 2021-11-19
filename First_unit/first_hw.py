# Data structures homework

# 1.Create a list that contains all the even numbers between 1 and 299.
list = []

for i in range(1,300):
    if (i%2 == 0) :
        list.append(i)

#print("list =",list)

# 2. Iterate through the previously created list 
# and print first the length of the list then all the squared values of the list.

print("The length of the list =",len(list))
print("The squared values of the list are :")
for i in list :
    x = i**0.5  
    if (x%1==0) : 
        print(i)
    

#3.In one line check if 57 is in the list using one line of python.
print( "57 is in the list ? ==>", 57 in list)
        
    


