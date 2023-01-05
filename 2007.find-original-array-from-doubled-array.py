#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original= []
        if len(changed)<2:
            return []
        else:
            j=0
            for i in range (len(changed)):
                while j < (len(changed)):
                    if 2*changed[i]==changed[j] :
                        if 2*changed[j] in changed:
                            original.append(changed[i])
                            changed.remove(changed[j])
                            

        return sorted(original)
# @lc code=end

