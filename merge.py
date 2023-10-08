def merge_list(list1, list2):
    mergeList = list1 + list2
    
    for i in range(len(mergeList) - 1):    
        for j in range(0, len(mergeList) - i - 1):  
            if mergeList[j] > mergeList[j+1]:   
                mergeList[j], mergeList[j+1] = mergeList[j+1], mergeList[j]

    return mergeList
