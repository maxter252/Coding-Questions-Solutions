def maxSubsetSum(arr):
    dp_n_1 = 0
    dp_n_2 = 0
    dp_n = 0

    for n in arr:
        dp_n = max([dp_n_1, dp_n_2, dp_n_2 + n ])
        dp_n_2 = dp_n_1
        dp_n_1 = dp_n

    return dp_n

def maxSubsetSum_2(arr):
    incl = 0
    excl = 0
     
    for i in arr: 
        new_excl = excl if excl>incl else incl 

        incl = excl + i 
        excl = new_excl 

    return (excl if excl>incl else incl)

print(maxSubsetSum([3, 7, 4, 6, 5]))