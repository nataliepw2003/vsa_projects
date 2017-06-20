# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

x=0
z=1

y=int(raw_input("How many Fibonacci numbers would you like to generate? "))
print z
for number in range (1,y):
    a = x + z
    print a
    x=z
    z=a
