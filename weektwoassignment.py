my_list=[]
print(my_list)
#Append 10,20,30,40 to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#Insert value 15 in index 1
my_list.insert(1,15)
print(my_list)
#adding values of another list to my_list
my_list2=[50,60,70]
my_list.extend(my_list2)
print(my_list)
#Removing the last element in the list
my_list.remove(70)
print(my_list)
#Sorting the values in ascending order but since its already in order, no change will be seen
my_list.sort()
print(my_list)
#Getting the index of the value 30 in the list
print(my_list.index(30))
