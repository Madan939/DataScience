# Write a Python program to read a text file and count how many times each unique word appears.
# Ignore case (e.g., Python and python should be treated as the same word).
# Ignore punctuation (. , ! ?).
# Output the result as a dictionary.
unique_count=0
repeat_count=0
try:
    file=open("abc.txt","r")
    content=file.read()
    file.close()
except:
    lists=["hello","hi","how","Hello","WHY","what","HI","WHEN","While","DO"]
    file=open("abc.txt","w")
    file.write(" ".join(lists))
    file.close()
    file=open("abc.txt","r")
    content=file.read()
    file.close()
    
lower_data=content.lower()
data=content.split()
for i in data:
    if i not in lower_data:
        unique_count+=1
    if i in lower_data:
        repeat_count+=1
        
print({"Unique Words":unique_count})
print({"Repeated words":repeat_count})