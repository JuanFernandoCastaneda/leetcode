"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
"""

# Something naive. Look for pairs of suffixes+preffixes.
def shortestCommonSupersequence2(str1: str, str2: str) -> str:
    preffixes_str1 = [str1[:i] for i in range(len(str1))]
    preffixes_str2 = [str2[:i] for i in range(len(str2))]
    suffixes_str1 = [[str1[i:] for i in range(len(str1))]]
    suffixes_str2 = [[str2[i:] for i in range(len(str2))]]
    # We first look for the largest ones
    for prefix in reversed(preffixes_str1):
        pass 
    pass

# Still n^2 but more clear. Solves different problem still xdxdxd.
def shortestCommonSupersequence(str1: str, str2: str) -> str:
    sequence = ""
    max_fix_len = 0
    for preffix_len in range(len(str1), 0, -1):
        if str1[:preffix_len] == str2[-preffix_len:]:
            sequence = str2 + str1[preffix_len:]
            max_fix_len = preffix_len
            break
    for suffix_len in range(len(str1), 0, -1):
        if str1[-suffix_len:] == str2[:suffix_len]:
            if suffix_len > max_fix_len:
                sequence = str1 + str2[suffix_len:]
            break
    if sequence == "":
        sequence = str1 + str2
    return sequence

print(shortestCommonSupersequence("abac", "cab"))