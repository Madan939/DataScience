# File handling using exception handling
try:
    file=open("abc.txt","r")
    content=file.read()
    file.close()
    print(content)
except:
    file=open("abc.txt","w")
    file.write("hello")
    file.close()
    file=open("abc.txt","r")
    content=file.read()
    file.close()
    print(content)