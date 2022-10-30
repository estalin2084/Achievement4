#Name: Unit Converter.py
# Author: Estalin Peña
# Date Created: october 24, 2022
# Date Last Modified: october 24, 2022
# Purpose: Print the cube of a number




square_dictionary = dict()#Dictionary for square numbers

for x in range(1,11):#iterates between the numbers 1 to 10 and adds the cube of the ten numbers
    square_dictionary[x] = x ** 3

print(square_dictionary)#Displays the numbers with the cube of each.