def maxSubsetSum(arr):
    n_1 = 0
    n = 0

    incl = 0
    excl = 0
     
    for i in arr: 
        new_excl = excl if excl>incl else incl 

        incl = excl + i 
        excl = new_excl 

    return (excl if excl>incl else incl)

print(maxSubsetSum([3, 7, 4, 6, 5]))