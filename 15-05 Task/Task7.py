# Reads two text files (file1.txt and file2.txt)
# Merges their content into a third file (merged.txt)
# Ensures that duplicate lines are not repeated.
try:
    file1=open("file1.txt","r")
    cnt1=file1.read()
    file1.close()
    file2=open("file2.txt","r")
    cnt2=file2.read()    
    file2.close()
except:
    data1=["hello","hi","what","when","how"]
    data2=["Hello","While","WHAT","by","why"]
    file1=open("file1.txt","w")
    file2=open("file2.txt","w")
    file1.write(" ".join(data1))
    file1.close()
    file2.write(" ".join(data2))
    file2.close()
    file1=open("file1.txt","r")
    cnt1=file1.read()
    file1.close()
    file2=open("file2.txt","r")
    cnt2=file2.read() 
    file2.close()
      
new_file_data=[]
for i in cnt1.split():
    new_file_data.append(i)
for i in cnt2.split():
    if i.lower() not in new_file_data:
        new_file_data.append(i)
file=open("merge.txt","w")
file.write(" ".join(new_file_data))
file.close()
print(new_file_data)