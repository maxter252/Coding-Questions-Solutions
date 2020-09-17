# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverse(input: int) -> int:
    input = str(input)
    if input[0] == '-':
        return '-' + input[:0:-1]
    else:
        return input[::-1]

# print(reverse(-12345))


# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def avg_len(input: str) -> float:

    words = input.replace('!','').replace('?','').replace(';','').replace(',','').replace('.','').split(" ")
    sum = 0 
    count = 0
    for i in words:
        count += 1
        sum += len(i)
    return (sum/count)

print(avg_len(sentence1))
print(avg_len(sentence2))