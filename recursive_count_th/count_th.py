'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    pass
    # If word length < 2, return 0 (base case)
    # If the first two letters of word are 'th'...
        # return 1 + the value of count_th w/ the remaining string after 'th'
    # Else if the second letter is 't'...
        # return the value of count_th w/ the remaining string after the first character
    # Otherwise...
        # return the value of count_th w/ the remaining string after the first two characters
