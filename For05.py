def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list = []
    for i in range(A, B+1):
       list = list + [i]
    return list(range(-1))

print(main(1, 8))