# Write a function to count integers, strings, and floats in a mixed list and return the result as a dictionary.
def countDataType(data):
    data_type_count = {}    
    for i in data:
        data_type = type(i).__name__
        data_type_count[data_type] = data_type_count.get(data_type, 0) + 1
    return(data_type_count)

lists=['abc',1,2,3.4,5.5,'def']
print(countDataType(lists))
