# Problem 10
'''
Modified Person Class

Create a class named Person with the following 4 private attributes.

__first_name
__last_name
__age
__email

Include a constructor :
__init__(self,first_name, last_name,age)
 email is formed by concatenating the first name, last name and gmail.com in the format specified in the output.

Include the methods:
        __str__(self)
This method returns a string corresponding to person details in the format specified in the sample output.
       fullname(self)
This method returns the full name of the person as a concatenation of first name and last name separated by a space.

Create an object of class Person to test the above class.


Input and Output Format:
Refer Sample Input and Output for formatting specifications.

Sample Input and Output:
[All text in bold corresponds to input and the rest corresponds to output]

Enter first name
Mahirl
Enter last name
Malar
Enter age
10
Full name of the person is  Mahirl Malar
Person Details
Mahirl Malar is 10 years old and her email id is Mahirl.Malar@gmail.com
'''	
class Person:
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__email = f"{first_name}.{last_name}@gmail.com".lower()

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} is {self.__age} years old and her email id is {self.__email}"

    def fullname(self):
        return f"{self.__first_name} {self.__last_name}"

# from Person import Person

person_first_name = input("Enter first name\n")
person_last_name = input("Enter last name\n")
person_age = input("Enter age\n")
person = Person(person_first_name, person_last_name, person_age)
print("Full name of the person is ",person.fullname())
print("Person Details")
print(person)