num1=int(input("enter anumber for search"))
print("entered  search no",(num1))
        
list=[]
for i in range(1,5):
    list.append(int(input("eneter no.")))
print(list)
print(num1 in list)
list.remove(num1)
print(list)

        

"""for element in list:
    if element==num1:
        print(element, end=' ')
    else:
        print("hekk")
print()"""
        
         
