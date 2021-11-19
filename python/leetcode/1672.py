# https://leetcode.com/problems/richest-customer-wealth


def maximumWealth(accounts):
    return max(map(sum, accounts))
    

# def maximumWealth(accounts):
#     arr=[]
#     for i in accounts:
#         arr.append(sum(i))
#     return max(arr)
        
            



print(maximumWealth([[1,2,3],[3,2,1]]))