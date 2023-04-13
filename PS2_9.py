words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# a. Convert words array into uppercase
print([x.upper() for x in words])
# b. Convert words array into lowercase
print([x.lower() for x in words])
# c. Display length of word array
print([len(x) for x in words])
# d. Display Upppercase, lowercase and length of words in array
print([[x.upper(), x.lower(), len(x)] for x in words])
# e. display 4 or more characters words into array
print([x for x in words if len(x)>3])