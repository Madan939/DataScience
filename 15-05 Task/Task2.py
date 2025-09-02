# Use list comprehension to extract all prime numbers from a given list of numbers.
try:
    lists=[x for x in range(1,100)]
    print("List of prime numbers:")
    prime=[]
    for num in lists:
        if num>1:
            i=2
            while i<num:
                if num%i==0:
                    break
                i+=1
            else:
                prime.append(num)
    print(prime) 
except:
    print("An errror has occured.")

    