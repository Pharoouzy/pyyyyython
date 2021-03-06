import numpy as np # Make numpy available using np

# Create a numpy array, and append an element
a = np.array(["Hello", "World"])
a = np.append(a, "!")
print("Current array: {}".format(a))
print("Printing each element")
for i in a:
	print(i)

print("\nPrinting each element and their index")
for i,e in enumerate(a):
	print("Index: {}, was: {}".format(i, e))