"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""


def find_pairs(words):
    """
    The words parameter contains a list of two character 
    words (lower case, no duplicates). Using sets, find an O(n) 
    solution for displaying all symmetric pairs of words.  

    For example, if words was: [am, at, ma, if, fi], we would display:

    am & ma
    if & fi

    The order of the display above does not matter.  'at' would not 
    be displayed because 'ta' is not in the list of words.

    As a special case, if the letters are the same (example: 'aa') then
    it would not match anything else (remember no the assumption above
    that there were no duplicates) and therefore should not be displayed.
    """
    set1 = set()

    # loop through the list of items
    for item in words:
        # this will compare the inverse of the item to those in the set
        if item[::-1] in set1:
            print(item + " & " + item[::-1])
        # add the item that has been seen already to the set. This will prevent the duplicates from being added
        set1.add(item)


find_pairs(["am", "at", "ma", "if", "fi"])      # ma & am, fi & if
print("=============")
find_pairs(["ab", "bc", "cd", "de", "ba"])  # ba & ab
print("=============")
find_pairs(["ab", "ba", "ac", "ad", "da", "ca"])  # ba & ab, da & ad, ca & ac
print("=============")
find_pairs(["ab", "ac"])                    # None
print("=============")
find_pairs(["ab", "aa", "ba"])              # ba & ab
print("=============")
find_pairs(["23", "84", "49", "13", "32", "46",
           "91", "99", "94", "31", "57", "14"])
# 32 & 23, 94 & 49, 31 & 13

# result = ""

# for x in words:
#     if x[0] == x[1]:
#         continue
#     if x[::-1] in words:
#         result += x + " & " + x[::-1] + ", "
#         words.remove(x)
# print(result)
