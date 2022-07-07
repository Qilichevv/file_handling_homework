def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = 0
    b = 0
    while b<len(data):
        if data[b].isdigit():
            a +=int(data[b])
        b += 1
    return a    
# Read data from file
f = open('txt_file/data07.txt')
data = f.read()
print(main(data))