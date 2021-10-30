
# i didn't understand the question well 

a = 12
s = "hello"

try :
    print(a + s) # will raise TypeError
except TypeError: # will handle only TypeError
	print(str(a) + s)
	print("Printed using type-casted data types")
except Exception:
    print("Error")
else : 
    print("Printed using original data types")
