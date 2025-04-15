#Tasks:
#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
sum=0
my_int=list(input("Input values:").split())
print(my_int)
for values in my_int:
    sum += int(values)
print(f"The sum of all values in the list is {sum}")

#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
tuple=("Lost world","Solo leveling","O.R.V","Kaiju no.8","Vagabond","WindBreaker")
for books in tuple:
    print(books)

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
person_info={}
for i in range(3):
    key=input("Enter key value: ")
    value=input("Enter value:")
    person_info[key]=value
print(person_info)


#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
int1=set(input("Enter values: ").split())
int2=set(input("Input vlues: ").split())
int3= int1 & int2
print(int3)
#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
my_words=list(input("Input values: ").split())
print(my_words)
odd_characters=[odd_characters for odd_characters in my_words if len(odd_characters) %2 != 0]
print(odd_characters)