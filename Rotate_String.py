'''

We need to determine if the string goal can be obtained from the string s by performing any number of shifts.

A shift involves moving the leftmost character of s to the rightmost position. For example, if s = "abcde", after one shift it becomes "bcdea". 
This process can be repeated multiple times.

We can observe that if s can be shifted to become goal, then goal must be a substring of the string s + s (the concatenation of s with itself). 
This is because concatenating s with itself covers all possible rotations of s.

'''
def rotateString(s, goal):
        if len(s) == len(goal):     #Obviously if the lengths of both the strings aren't equal then the problem statement is impossible.
                
                return goal in s+s  #Checking if goal in a substring of the string s+s which covers all possible rotations of s

        return False                #If lengths of the strings aren't equal or goal cannot be formed by rotating s.
