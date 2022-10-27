# Program to check if a number is prime or not

import string

print("\t", "\t","\t", "Welcome to the Prime number checker!")
print(" ")
print("Below please introduce a set of numbers separated with commas to check if they are primes. ")
print(" ")


number_list = input("Numbers: ")
print("")

prime_num = []
not_prime_num= []

for z in number_list.split(","):
    x = int(z)
    for i in range(2, int(x** 0.5) +1):
        if (x % i) != 0:
            prime_num.append(x)
            break
        else:
            not_prime_num.append(x)
        # break out of loop
            break

print("Prime numbers are: ")
print(" ".join(map(str,prime_num)))
print("-" *40)
print("Not prime numbers are: ")
print(" ".join(map(str,not_prime_num)))

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable


# prime numbers are greater than 1

    # check for factors



# check if flag is True

# print("Prime numbers are")
# print(", ".join(prime_num))