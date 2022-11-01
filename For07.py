def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    a = 0
    for i in range(N):
        a+=i%2!=0
    return a

print(main(10))