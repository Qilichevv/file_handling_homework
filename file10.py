def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=[]
    list1=data.split('\n')
    for i in list1:
        a.append(int(len(i)))

    
    return max(a)

f=open('txt_file/data10.txt')
data=f.read()
print(main(data))