# my_string = '''This is a multi-line
# string in Python. It can span
# across multiple lines without the
# need for escape characters.'''

# my_string = "Hello " + "World!"

# print(my_string)

# if "fun" in "this is fun":
#     print("this is fun contains the word fun.")
    
# print("this is fun".index("fun"))

print(",".join(["foo", "bar"]))
# print("," + ["foo", "bar"])
# print(["foo", "bar"].join(","))
print(",".join(["foo", "bar"]))
print("foo,bar".split(","))

print(" ".join([x.capitalize() for x in "yo yo yo".split()]))

number = 123
print(f"{number}")

number = 123
print("{number}".format(number=number))

print("this is fun".index("fun"))