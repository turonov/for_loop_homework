def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """ 
    a=[]
    for s in list1:
        a.append(s.title())
    return a

print(main('rustam'))