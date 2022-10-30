#Name: EP Learning Institution Course Registry.py
# Author: Estalin Peña
# Date Created: october 27, 2022
# Date Last Modified: october 28, 2022
# Program to check if a number is prime or not

print("\t", "\t","\t", "Welcome to the Prime Number Checker!")#Welcome message for the user
print(" ")#space separating the texts printed
print("Below please introduce a set of numbers separated with commas to check if they are primes. ")#Message indicating the user what to do
print(" ")#space separating the texts printed


number_list = input("Numbers: ")#Takes the list of numbers to evaluate.
print("")#space separating the texts printed

prime_num = []#Empty list that will take the prime numbers
not_prime_num= []#Empty list that will take the not prime numbers

for z in number_list.split(","):#Irates the number list that the user enters and split the result with commas
    x = int(z)#variable transformed into int number
    for i in range(2, int(x** 0.5) +1):#This for loop evaluates if a number is prime and updated the prime_num list
        if (x % i) != 0:
            prime_num.append(x)
            break
        else:#this else updates the not_prime_num list 
            not_prime_num.append(x)
            break

print("Prime numbers are: ")#Displays the message of the prime numbers
print(" ".join(map(str,prime_num)))#Adds a space to the prime number list, converts the numbers into strings and print the prime number list.
print("-" *40)#Separates the results with dash signs 
print("Not prime numbers are: ")#Displays the Message for not prime numbers.
print(" ".join(map(str,not_prime_num)))#Adds a space to the not prime number list, converts the numbers into strings and print the not prime number list.