def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1 = []
    a = 0
    b = 0
    c = 0
    while c < len(data):
        if data[c].isdigit():
            a +=1
        else:
            b +=1
        c += 1
    list1.append(a)
    list1.append(b)
    return list1

    
# Read data from file
f = open('txt_file/data05.txt')
data= f.read()
print(main(data))
