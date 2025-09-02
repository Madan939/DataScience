#Write a program to convert a list of strings into a list of integers
string_list=["1","2","3","4","5"]
lists=[]
for x in string_list:
    lists.append(int(x))
print(lists)