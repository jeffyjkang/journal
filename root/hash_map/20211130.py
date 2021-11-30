# Group Anagrams
# Given an array of strings, group anagrams together.
# Example:
# Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Output:
# [
#     ['ate', 'eat', 'tea'],
#     ['nat', 'tan'],
#     ['bat']
# ]
# Note: All inputs will be in lowercase. The order of the outputs does not matter.

def group_anagrams(lst):
    # initialize empty hash map/ dict
    hash = {}
    # loop through the list
    for word in lst:
        # assign key variable to the sorted word
        key = ''.join(sorted(word))
        # if the key exists in the hash map, append the word to the value list
        if key in hash:
            hash[key].append(word)
        # else initialize the value at the key to a list that holds the word
        else:
            hash[key] = [word]
    # return the hash values
    return list(hash.values())

array = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

print(group_anagrams(array))

TAGS = ['HASH_MAP']
