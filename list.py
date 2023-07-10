# find the intersection of two lists.
def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


list1 = [1, 2, 3, 4, 5,9]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print(intersection)  
