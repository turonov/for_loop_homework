def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """ 
    a = []
    for i in list1:
        a.append(i.title())
    return a

print(main('rustam', 'diyor', 'alisher', 'bektosh'))