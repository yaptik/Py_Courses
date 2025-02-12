# homework 1.0, print
print("Hello, Python!")
print("Hello, Artyom!")

#home work 1.1, sep+end
print("Programming", "Essentials", "in", sep="***", end="...") #printing string with parameters.
print("Python")

#home work 1.2, arrow sep+end
print("    ", "   * ", "  *   ", " *     ", "***   **", "  *   ", "  *   ", "  *****", sep="*\n", end="\n")

#home work 1.3
print("\n'I\"m'", "''learning''", "'''Python'''", sep="\n")

#home work 1.4
John = 1
Mary = 2
Adam = 3

print(f"John:{John}, Mary:{Mary}, Adam:{Adam}", sep=",")

total_apples = John + Mary + Adam #total apples count

print(f"Total apples count is:{total_apples}")

#home work 1.5
kilometers = 12.25
miles = 7.38

converting_kilometers = miles * 1.61
converting_miles = kilometers / 1.61
print(f"{miles} miles is {round(converting_kilometers, 2)} kilometers",
      f"{kilometers} kilometers is {round(converting_miles, 2)} miles", sep="\n")

#home work 1.6
#this program computes the number of seconds
# in a given number of hours.
# This program has been written two days ago.
a = 2 #number of hours
seconds = 3600 #seconds in hour
print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) #printing the number of seconds in a given number of hours
print("Goodbye", "but a programmer didn't have time to write any code")
#this is the end of the program that computes the number of seconds in 3 hours