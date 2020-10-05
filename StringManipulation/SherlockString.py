from Collections import Counter


def isValid(s):
    """
    Sherlock considers a string to be valid if all characters of 
    the string appear the same number of times. It is also valid if 
    he can remove just one character from everywhere in the string, and the 
    remaining characters will occur the same number of times. Given 
    a string , determine if it is valid. If so, return YES, otherwise 
    return NO.
    """
    char_count = Counter(s)
    char_count_values = list(char_count.values())
    distinct_counts = Counter(char_count_values)


    if len(distinct_counts) == 1: return 'YES'
    if len(distinct_counts) > 2: return 'NO'

    min_count = min(char_count_values)
    max_count = max(char_count_values)
    if distinct_counts[1] == 1 : return "YES"
    if distinct_counts[max_count] == 1 and max_count == min_count + 1:
        return "YES"
    else:
        return "NO"