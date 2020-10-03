def isValid(s):
    alpha_dict = {}
    for i in s:
        alpha_dict[i] = (alpha_dict[i] if i in alpha_dict else 0) + 1
    
    count=0
    removals_available = 1
    reference = alpha_dict[min(alpha_dict, key=(lambda k: alpha_dict[k]))]
    print (reference)

    for key, val in alpha_dict.items():
        print (key, val)
        if not reference:
           reference = val 

        if removals_available <= 0 and val != reference:
            return 'NO'
        elif removals_available >= 1 and val-1 == reference:
            removals_available -= 1
        elif val < reference:
            return 'NO'

    return 'YES'


print(isValid('aaabbccddee'))