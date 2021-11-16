

def isPalindrome(x: int) -> bool:
    if (x < 0):
        return False
    else:
        new_x=[]
        for i in reversed(str(x)):
            new_x.append(i)
        if (int("".join(new_x)) == x):
            return True
        else:
            return False
            
        
               
        
        
print(isPalindrome(121))