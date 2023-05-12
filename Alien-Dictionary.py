#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        answer = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(k):
            indegree[chr(97 + i)] = 0
            
        for r in range(N - 1):
            i = 0
            j = 0
            while i < len(alien_dict[r]) and j < len(alien_dict[r + 1]):

                if alien_dict[r][i] == alien_dict[r + 1][j]:
                    i += 1
                    j += 1
                    continue
                else:
                    graph[alien_dict[r][i]].append(alien_dict[r + 1][j])
                    indegree[alien_dict[r + 1][j]] +=1
                    break
             

        queue = deque()
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)

        while queue:
            current = queue.popleft()
            answer.append(current)
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
              
                    
        return answer
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
