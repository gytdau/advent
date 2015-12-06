from inputData import *

# The first time I did it,
# I just replaced ( with + 1 and ( with - 1 and got the result.
# But that was a bit too cheaty in my eyes.

x = 0

for i in instructions:
    if i == "(":
        x += 1
    else:
        x -= 1

print(x)