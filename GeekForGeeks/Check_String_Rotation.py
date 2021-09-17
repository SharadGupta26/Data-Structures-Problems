
class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,a,b):
        x=len(a)
        y = len(b)
        #print(a[0:2], b[y-2:y] , a[2:x],b[0:y-2] )
        if x==y and a[0:2] == b[y-2:y] and a[2:x] == b[0:y-2] :
            return True
        elif x==y and a[x-2:x]==b[0:2] and a[0:x-2] == b[2:y] :
            return True
        else :
            return False
        #code here
