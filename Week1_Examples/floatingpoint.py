import math

a = 0.1
b = 0.1
c = 0.1

# Here is a dangerous algorithm

print("Algorithm 1:")
print("a+b+c = ", a+b+c)

if a+b+c == 0.3:
    print("Sanity")
else:
    print("Insanity")

# Here is a better algorithm!
print("Algorithm 2:")
epsilon = 1.0E-10
expectedValue = 0.3

difference = (a+b+c) - expectedValue

if math.fabs(difference) < epsilon:
    print("Sanity")
else:
    print("Insanity")

# Let's calculate the largest and smallest floating point numbers
# that one can store in Python

# IEEE standard for 64-bit
# the exponent is specified using 11 bits,
# and the mantissa is specified using 53 bits (1 sign bit + 52 value bits)
# The exponent is stored in a biased form,
# which means that the actual exponent is obtained by subtracting a
# bias value from the stored exponent. The bias value for double-precision
# floating-point numbers is 1023.
# 11111111110 = 2**11 - 2 = 2046 - 1023 = 1023
# 00000000001 = 1 - 1023 = -1022
# Thus, the largest exponent is 1023 and the smallest exponent is -1022
# For the mantissa, the largest is 1.1111111111... = 2 - 2^-52
# and the smallest is 1.00000000..... = 1
print("Algorithm 3:")
largest = (2-2**(-52))*(2**1023)
smallest = 2**(-1022)
print("largest:", largest)
print("smallest:", smallest)
