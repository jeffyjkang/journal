# Substring With Concatenation Of All Words
# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) that is a concatenation of each word in words exactly once and without any intervening characters.
# Example 1:
# Input:
# s = 'barfoothefoobarman',
# words = ['foo', 'bar']
# Output: [0, 9]
# Explanation: Substrings starting at index 0 and 9 are 'barfoo' and 'foobar' respectively.
# The output order does not matter, returning [9, 0] is fine too.
# Example 2:
# Input:
# s = 'wordgoodstudentgoodword',
# words = ['word', 'student']
# Output: []

def find_substring(s, w):
    # initialize word length to the length of w at index 0 (all words all same length)
    word_length = len(w[0])
    # initialize word count to the length of w
    word_count = len(w)
    # initialize list length as the product of word length and word count
    list_length = word_length * word_count
    # initialize results list as an empty list
    results = []
    # edge case, if the size of list length is greater than the length of string return empty list
    if list_length > len(s): return results
    # initialize empty hash map
    hash_map = {}
    # loop through word count's indices
    for i in range(word_count):
        # if word at index i is in the hashmap increment the value by 1
        if w[i] in hash_map:
            hash_map[w[i]] += 1
        # if word at index i is not in the hash map assign the key value pair to the value of words at index i and 1 respectively
        else:
            hash_map[w[i]] = 1
    # loop through the indices of string from 0 to list length + 1
    for i in range(len(s) - list_length + 1):
        # duplicate the hash map and store it in a temp variable, (*note pass by reference, do not assign temporary hash map to hash map)
        h_m = hash_map.copy()
        # assign index j to index i
        j = i
        # assign count to word count
        count = word_count
        # loop through while j is less than i + length of list
        while j < i + list_length:
            # assign word to string from index j to j + word length
            word = s[j : j + word_length]
            # if the word is not in the hash map, or the value of the temporary hash map at key word is equal to 0, break from the current iteration of the loop
            if (word not in hash_map or h_m[word] == 0):
                break
            # if the word is in the hash map and the value of temporary hash map at key word is not 0
            else:
                # decrement the value of temporary hash map at key word by 1
                h_m[word] -= 1
                # decrement the count by 1
                count -= 1
            # increment the j index by word length
            j += word_length
            # if the count is equal to zero, the temporary hash map's values are all 0, append the index of i to the results list
            if count == 0:
                results.append(i)
    # return the results list
    return results

string = 'barfoothefoobarman'
words = ['foo', 'bar']

print(find_substring(string, words))

TAGS = ['HASH_MAP', 'SEARCH']