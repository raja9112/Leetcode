class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter
        # return Counter(s) == Counter(t)

        # return sorted(s) == sorted(t)

        # Hash method Time: 80ms
        # if len(s) != len(t):
        #     return False

        # countS = {}
        # countT = {}

        # for i in range(len(s)):
        #     # Adding countT.get(t[i], 0) -> key to occurence, if the key doesn't exists, the default value will return
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        #     countS[s[i]] = 1 + countS.get(s[i], 0)

        # for j in countS:
        #     if countS[j] != countT.get(j, 0):
        #         return False
        
        # return True
        
        # Hash mapping Time: 43ms
        table1 = {}
        table2 = {}

        for i in s:
            if i not in table1:
               table1[i] = 1
            else: 
                table1[i] += 1

        for j in t:
            if j not in table2:
                table2[j] = 1
            else: 
                table2[j] += 1

        if table1 != table2:
            return False
        return True