# you can assign multiple values to multiple vars
a, b = 5, 1

if a < b:
    # colon (:) denotes block in python
    # Blocks are called suites in Python doc
    # four space indent is considered standard in Python
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))

# tenary-like statement and it is called conditional expression
print("true" if a < b else "false")