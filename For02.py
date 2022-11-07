def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a='0'
    for i in range(1,n):
        a+= ","+str (i)
    return a

print(main(5))
    
