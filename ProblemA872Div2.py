def is_palindrome(s):
    return s == s[::-1]

def solve(s):
    n = len(s)
    
    for k in range(1, n//2 + 1):
        for i in range(n - k + 1):
            modified_s = s[:i] + s[i+k:]
            if not is_palindrome(modified_s):
                return n - k
    
    return -1  

t = int(input())

for i in range(t):
    string = input()
    print (solve(string))
