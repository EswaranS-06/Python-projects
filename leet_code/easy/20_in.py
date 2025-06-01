def isValid(s):
    po,pc,bo,bc,so,sc = 0,0,0,0,0,0
    #p, b, sq = 0, 0, 0
    is_valid = []
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == '(' :
                po += 1
                if s[j] == ')':
                    pc+=1
            elif s[i] == '{' :
                bo += 1
                if s[j] == '}':
                    bc+=1
            elif s[i] == '[' :
                so += 1
                if s[j] == ']':
                    sc += 1
                """so += 1
                sc += 1"""
                
testcase = ["([])","(]","()[]{}","()"]
for i in  testcase:
    isValid(i)