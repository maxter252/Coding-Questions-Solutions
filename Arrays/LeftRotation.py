def rotLeft(a, d):
    new_arr = []
    i = d 
    while i < len(a):
        new_arr.append(a[i])
        i+=1

    i = 0
    while i < d:
        new_arr.append(a[i])
        i+=1
    
    return new_arr

print(rotLeft([1,2,3,4,5],2))