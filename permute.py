def GetPermutations(listOFElements):
    # Create a empty list of lists
    listOfLists = []
    if len(listOFElements) <= 1:
        # If list has 0 or 1 element, then add in list of lists
        listOfLists.append(listOFElements)
    else:
        # If list has more than 1 elements
        # Iterate over all elements by index position
        for i in range(len(listOFElements)):
            # Select element at ith poistion
            elem = listOFElements[i]
            # Select remaining elements
            remainingList = listOFElements[:i] + listOFElements[i+1:]
            # get permutations of all remaining elements, and add ith element to it
            for perms in GetPermutations(remainingList):
                listOfLists.append([elem] + perms)

    # return permutations of given list
    return listOfLists