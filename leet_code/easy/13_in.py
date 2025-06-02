from collections import Counter
class Solution(object):
    def romanToInt(self, s):
        
        print(Counter(s))
        
test = Solution()
testcases = ["III","LVIII","MCMXCIV"]
for testcase in testcases:
    test.romanToInt(testcase)
    
'''
I = 1
II = 2
III = 3
IV = 4
V = 5
IX = 9
X = 10

'''