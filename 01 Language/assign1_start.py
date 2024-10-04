# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

# TODO: the assignment operator is part of an expression
(x := 5)
print(x)

# TODO: The assignment expression is useful for writing concise code

while (thestr := input("Value? ")) != "exit":
    print(thestr)