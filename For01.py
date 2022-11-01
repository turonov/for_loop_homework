import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    list=[]
    a=0
    while a<n:
        list=list+[a]
        a+=1
    return list
print(main(6))

