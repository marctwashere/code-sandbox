"""
This is a custom bruteforcing script that works for my friend's
specific password requirments. It attacks Microsoft's bitlocker.

Password stipulations:
- It is a combination of n words, n ranging from 3-5 (6?)
- Each word is all lowercase or possibly has the first letter capitalized
- The possible words are known beforehand
"""
import itertools

# USER PARAMS
words = ['apple', 'bunny', 'rabbit', 'sock', 'meep', 'nada']
min_words_in_pass = 3
max_words_in_pass = 6

def get_nth_bit(some_int, n):
    return (some_int >> n) & 1

# make sure there are enough words for all brute force sets
assert len(words) >= max_words_in_pass, 'You want to bruteforce words set size {} but only have {} words'.format(max_words_in_pass, len(words))

# look over all possible set SIZES
for set_size in range(min_words_in_pass, max_words_in_pass+1):

    # get list of all possible lower-case permutations
    perms = itertools.permutations(words, set_size)
    perms = list(perms)

    # loop over all uncapitalized word permutations
    for perm in perms:
        # listify it to make the elements assignable
        perm = list(perm)

        # loop over all possible capitalization patterns
        for capitalization_pattern in range(2**set_size):
            
            # loop over each word in the set
            for word_index in range(set_size):
                word = perm[word_index]

                # capitalize the word if there is a 1, don't if there is 0
                if get_nth_bit(capitalization_pattern, word_index) == 1:
                    word = word[0].upper() + word[1:]
                    perm[word_index] = word
                else:
                    word = word.lower()
                    perm[word_index] = word
            
            # join the perm for a possible password
            possible_pass = ''.join(list(perm))
            
            #TODO in addition to printing, have it type the text 
            print(possible_pass)