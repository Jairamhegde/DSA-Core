# Last updated: 8/13/2026, 8:21:44 PM
class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []

        for i in s:
            if stack and stack[-1][0] == i:
                if stack[-1][1] == k-1:
                    stack.pop()
              
                else:
                    stack [-1][1] += 1
         
            else:
                stack.append([i,1])
             
        st = []
        for j in stack:
            
            if st and st[-1][0] == j[0]:
                if st[-1][1] == k-1:
                    stack.pop()
                else:
                    st [-1][1] += 1
            else:
                st.append(j)
    
        return "".join([ele[0]*ele[1] for ele in st])
        
        