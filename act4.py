#Take two comma separated input from the user..
# Output 2 print lines
# 1 is user name length
# 2 is count the character thatuser inputed..
name,char= input("Enter Name and Char seperated with commas: ")

print("The Length of your name is ",len(name))
print("Charater count:",name.lower().count(char.lower()))  #case sensitive

