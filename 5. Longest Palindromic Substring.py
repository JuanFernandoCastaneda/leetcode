def longestPalindrome(s: str) -> str:
    biggest_size = 0
    longest_word = ""
    for pos, letter in enumerate(s):
        size, word = add_neighbours(s, letter, pos, pos)
        if size > biggest_size: 
            biggest_size = size
            longest_word = word
    for pos, letter in enumerate(s[:-1]):
        if s[pos] == s[pos+1]:
            size, word = add_neighbours(s, s[pos]+s[pos+1], pos, pos+1)
            if size > biggest_size: 
                biggest_size = size
                longest_word = word
    return longest_word 
    
# Returns size of the (max) palindrome and the palindrome.
def add_neighbours(original_s, current_palindrome, lower_bound, upper_bound) -> str:
    if lower_bound-1 < 0 or upper_bound+1 >= len(original_s):
        return upper_bound-lower_bound+1, current_palindrome
    elif original_s[lower_bound-1] != original_s[upper_bound+1]:
        return upper_bound-lower_bound+1, current_palindrome
    else:
        new_palindrome = original_s[lower_bound-1] + current_palindrome + original_s[upper_bound+1]
        return add_neighbours(original_s, new_palindrome, lower_bound-1, upper_bound+1)

print(add_neighbours("detartrated", "t", 5, 5))
print(add_neighbours("detartrited", "t", 5, 5))

print(longestPalindrome("detartrated"))
print(longestPalindrome("detartrited"))
print(longestPalindrome("detartited"))
print(longestPalindrome("cbbd"))