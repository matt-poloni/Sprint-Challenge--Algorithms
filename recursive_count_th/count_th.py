'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # If word length < 2...
    if len(word) < 2:
        # return 0 (base case)
        return 0
    # Else if the first two letters of word are 'th'...
    elif word[0:2] == 'th':
        # return 1 + the value of count_th w/ the remaining string after 'th'
        return 1 + count_th(word[2:])
    # Else if the second letter is 't'...
    elif word[1] == 't':
        # return the value of count_th w/ the remaining string after the first character
        return count_th(word[1:])
    # Otherwise...
    else:
        # return the value of count_th w/ the remaining string after the first two characters
        return count_th(word[2:])
