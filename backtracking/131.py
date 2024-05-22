"""
131. Palindrome Partitioning
Type - Medium

Topics - String, Dynamic Programming, Backtracking

Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

 
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 
Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def calculate(s, i, prev):
            nonlocal out
            if i == len(s):
                out.append(prev)
                return None
            temp = ''
            for start in range(i, len(s)):
                temp += s[start]
                if palindrome(temp):
                    tempList = list(prev)
                    tempList.append(temp)
                    calculate(s, start+1, tempList)
            return None
        
        def palindrome(s):
            i = 0
            j = len(s)-1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True

        out = []
        calculate(s, 0, [])
        return out
        