def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    a=0
    for i in range(B,A,1):
        a+=i
    return a

print(main(6, 1))