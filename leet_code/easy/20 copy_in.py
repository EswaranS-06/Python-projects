class Solution():
    def isValid(self, s):
        lst = []
        clst =[]
        p,b,q = 0,0,0
        for i in s:
            lst.append(i)

        if len(lst) < 2:
            return False
            
        else:
            for i in range(len(lst)):
                for j in range(i+1,len(lst)):
                    if lst[i] == '(' :
                        clst.append(lst[i])
                        if lst[j] == ')':
                            clst.pop(lst[0])
                            break
                    elif lst[i] == '{' :
                        clst.append(lst[i])
                        if lst[j] == '}':
                            clst.pop(lst[0])
                            break
                    elif lst[i] == '[' :
                        clst.append(lst[i])
                        if lst[j] == ']':
                            clst.pop(lst[0])
                            break
                    else:
                        continue
                else:
                    if lst[i] == ')' or lst[i] == '}' or lst[i] == ']':
                        return False
        if p % 2 == 0 and b % 2 == 0 and q % 2 == 0:
            
            return True
        else:
        
            return False
     
        
                
testcase = ["([])","(]","()[]{}","()",'[','){']
test = Solution()
for i in  testcase:
    print(test.isValid(i))