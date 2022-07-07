def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = []
    b = 0
    while b < len(data):
        if data[b].isdigit():
            pass
        else:
            a.append(data[b])
        b +=1
    return a
    
# Read data from file
f = open('txt_file/data04.txt')
data= f.read()
print(main(data))
