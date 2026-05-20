import sys

i = 45667

tf1 = True
tf2 = False

x = 32.446
y = 3.1E31
z = 3.1E300
t = 3.1E400

myString1 = "A"
myString2 = "AB"
myString3 = "ABC"
myString4 = "The quick brown fox jumps over the lazy dog."

print("Integer:")
print(sys.getsizeof(i), "bytes.")
print(id(i))

print("Boolean:")
print(sys.getsizeof(tf1), "bytes.")
print(sys.getsizeof(tf2), "bytes.")

print("Float:")
print(sys.getsizeof(x), "bytes.")
print(sys.getsizeof(y), "bytes.")
print(sys.getsizeof(z), "bytes.")
print(sys.getsizeof(t), "bytes.")
print("y = ", y)
print("z = ", z)
print("t = ", t)

print("String:")
print(sys.getsizeof(myString1), "bytes.")
print(sys.getsizeof(myString2), "bytes.")
print(sys.getsizeof(myString3), "bytes.")
print(sys.getsizeof(myString4), "bytes.")
