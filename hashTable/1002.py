""" 
1002. Find Common Characters
Type - Easy

Topics - Array, Hash Table, String

Given a string array words, return an array of all characters that show up in all strings 
within the words (including duplicates). You may return the answer in any order.

 
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

 

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashTable = dict()

        for w in words[0]:
            hashTable[w] = hashTable.get(w, 0)+1
        
        for i in range(1, len(words)):
            temp = dict()
            for w in words[i]:
                temp[w] = temp.get(w, 0)+1
                
            delKey = set()
            for k in hashTable.keys():
                if k in temp:
                    hashTable[k] = min(hashTable[k], temp[k])
                else:
                    delKey.add(k)

            for k in delKey:
                del hashTable[k]

        out = []
        for k, v in hashTable.items():
            for i in range(v):
                out.append(k)
        
        return out