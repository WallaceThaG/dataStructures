list1 = [2,5,12,36,47,56,59,78,156]
list2 = [16,39,42,43,66,69,100]
mergeList = []

flag = 0
for i in range(len(list2)):
    count = 0
    while (list2[i] > list1[count]):
        mergeList.append(list1[count])
        count += 1
    mergeList.append(list2[i])

print(mergeList)