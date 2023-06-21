# try:
#     file = open("Day-30(Errors,Exceptions & JSON Data)/a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open("Day-30(Errors,Exceptions & JSON Data)/a_file.txt","w")
#     file.write("Divyanshi💜")
# except KeyError as error_message:
#     print(f"The key {error_message} doesnot exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")


height = float(input("Height:"))
weight = float(input("Weight:"))

if height>2.5:
    raise ValueError("Human Heights can't be over 2.5m")

bmi = height/weight**2
print(bmi)