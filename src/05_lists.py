# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("appended 4 to 'x'", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print("extend x into y", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x)
x.remove(8)
print("removed '8' from 'x'", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print("inserted '99' at fifth position in 'x'", x)

# Print the length of list x
# YOUR CODE HERE
print(" no. of items in 'x'", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for item in x:
    print("each item in 'x' multiply by 1000", item * 1000)
