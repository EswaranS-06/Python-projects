mark = int(input("Enter the Marks"))
while mark != 0:
    if mark > 100:
        print("Invalid Mark")
    elif





"""nums = [2, 7, 12, 13]
target = 9

lst = [i for i in range(len(nums)) for j in range(len(nums)) if ( nums[i] + nums[j]) == target]

print(lst)
"""

'''
lst = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] + nums[j]) == target:
            lst.append(i)
            continue 
    continue

print(lst)
'''
