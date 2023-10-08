def merge_list(list1, list2):
    mergeList = list1 + list2
    swapped = False
    for i in range(len(mergeList) - 1, 0, -1):    
        for j in range(i):  
            if mergeList[j] > mergeList[j+1]:   
                mergeList[j], mergeList[j+1] = mergeList[j+1], mergeList[j]
                swapped = True  
        if swapped:
            swapped = False
        else:
            break
    return mergeList
