# The Python command to write something when the code is run is print()
# print("Hello, World!") 

# In computer programming, there are different ways that data are stored and interpreted
# by the language you are using, which are called "data types"
#
# In Python, the four biggest data types are strings, integers, floats, and booleans

# here, I'm defining variables with four different data types
a = "1" # string -- collection of letters, words, numbers, etc. surrounded by either " " or ' '
b = 1 # integer -- whole numbers (ex. 1, 68, 5349, 908742598, etc.)
c = 1.0 # float -- numbers with a decimal place (ex. 1.0, 3.23, 9.0000000002, 10000.3333, etc.)
d = True # boolean -- True or False, where the T or F have to be capitalized

# print(a)
# print(b)
# print(c)
# print(d)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# print(a + str(b))




# When defining variables (in Python, we use a variable name followed by an equal sign, as we did above),
# it is helpful to use names that are descriptive so you can easily remember what it is later.
# Ex. If you want to define a variable for the number of apples, you might want to define your 
# variable as int_apples = 5, where the int_ means you are using an integer

print(a)
print(b)
print(c)
print(d)

# use the type() command to determine which data type your variable is

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Not all data types are compatible. For example, if you uncomment the following line of 
# code, you will get an error because Python does not know that the "1" is referring 
# to a number

print(a + b)

# You can convert the string "1" to an integer 1 using int(), which will allow you to
# then add a and b

ab = int(a) + b
print(ab)

# Now we are going to start putting together sentences. 
# Here, we define two variables that we can change later, called adjective and verb

adjective = 'fun' # Quick note: In Python, it does not matter whether you use " " or ' '
verb = 'build'

# One way to create a sentence is to add strings together. Python takes everything
# very literally, though, so you have to make sure you include spaces and the 
# correct punctuation in your strings

output1 = "Programming is so " + adjective + ". What should we " + verb + "?"
print(output1)

# Another way to put a sentence together is by using what's called an f-string. This is
# a bit more straightforward because you don't have to worry about adding anything together,
# anything in the curly brackets {} specifies that you're calling a variable.
# The f-string format is the following:

output2 = f"Programming is so {adjective}. What should we {verb}?"
print(output2)

# output1 and output2 will produce the same sentence.

# We can also use the console to define variables, which is what we call user-input. Instead of 
# defining a variable in our Python script, we can use input() and a phrase, such as 
# "What adjective would you like?", and whatever you type in the console will define the 
# variable. Here are two examples below:

userAdjective = input("Provide an adjective: ")

userVerb = input("Provide a verb: ")

print(f"Programming is so {userAdjective}. What should we {userVerb}?")


# Finally, we can write what are called functions. A function is a block of 
# code that only runs when you call the name of the function. This is really 
# useful when you want to run the same code lots of times, but just change
# one or two parameters (such as adjective and verb!). The function we define
# below will produce the same output as the three lines of code above, but unless
# you type MadLibs() after the function, it will not run the code

def MadLibs():
    userAdjective = input("Provide an adjective: ")
    userVerb = input("Provide a verb: ")
    print(f"Programming is so {userAdjective}. What should we {userVerb}?")

MadLibs() 
