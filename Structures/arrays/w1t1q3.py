outlet1Sales = [10, 12, 15, 10]
outlet2Sales = [5, 8, 3, 6]
outlet3Sales = [10, 12, 15, 23]

# easiest solution is to use a 2D array
salesList = [outlet1Sales, outlet2Sales, outlet3Sales]

# array totals[4]
totals = [0, 0, 0, 0]

# iterate through the 2D array and put in the sums of the quarters into the totals array 
for i in range(len(salesList)):
    for quarter in salesList[i]:
        totals[i] += quarter*1000
    print("Outlet" + str(i+1) + "Sales:", str(totals[i]))
