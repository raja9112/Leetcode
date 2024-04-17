# 17. Letter Combinations of a Phone Number

# Medium

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitsTochar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtracking(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitsTochar[digits[i]]:
                backtracking(i+1, curStr + c)

        if digits:
            backtracking(0, "")

        return res
    
#  Here’s how it works:

# Initialize a result list and a dictionary: The res list is used to store the final results. The digitsTochar dictionary maps each digit to its corresponding letters on a mobile phone keypad.
# Define a helper function backtracking: This function is used to generate the letter combinations. It takes two arguments: i (the current digit being processed) and curStr (the current combination of letters).
# Base case of backtracking: If the length of curStr is equal to the length of digits, it means we have formed a valid combination of letters. We append curStr to res and return.
# Recursive case of backtracking: If the length of curStr is less than the length of digits, we iterate over each letter c that the current digit can represent. For each letter, we recursively call backtracking with i+1 and curStr + c.
# Start the backtracking process: If digits is not an empty string, we call backtracking with 0 and an empty string to start the backtracking process.
# Return the result: Finally, we return res, which contains all possible letter combinations that the number could represent.

# Here’s how the program would work with this input:

# Initialize a result list and a dictionary: The res list is initialized as an empty list. The digitsTochar dictionary is initialized to map each digit to its corresponding letters on a mobile phone keypad.
# Start the backtracking process: Since digits is not an empty string, the backtracking function is called with 0 and an empty string.
# First recursive call to backtracking: In the first recursive call, i is 0 and curStr is an empty string. Since the length of curStr is less than the length of digits, it iterates over each letter that the first digit ("2") can represent. For each letter, it recursively calls backtracking with i+1 and curStr concatenated with the letter.
# Second recursive call to backtracking: In the second recursive call, i is 1 and curStr is "a". It iterates over each letter that the second digit ("3") can represent. For each letter, it recursively calls backtracking with i+1 and curStr concatenated with the letter.
# Third recursive call to backtracking: In the third recursive call, i is 2 and curStr is "ad". Since the length of curStr is equal to the length of digits, it appends curStr to res and returns.
# Repeat the process: The process is repeated for each possible combination of letters. After all recursive calls are finished, res contains all possible letter combinations that the number could represent.
# Return the result: Finally, it returns res, which is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# So, for this input, the letterCombinations method would return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], indicating all possible letter combinations that "23" could represent on a mobile phone keypad.

# Time complexity: O(4^n)
# Space complexity: O(n)