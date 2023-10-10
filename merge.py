def merge_list(list1, list2):
    
    for item in list1 + list2:
        if not isinstance(item, int):
            raise TypeError("Both lists must contain only integers")
        
    mergeList = list1 + list2
    
    for i in range(len(mergeList) - 1):    
        for j in range(0, len(mergeList) - i - 1):  
            if mergeList[j] > mergeList[j+1]:   
                mergeList[j], mergeList[j+1] = mergeList[j+1], mergeList[j]

    return mergeList
