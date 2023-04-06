class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2 != 0:
            return -1
        skill.sort()
        left = 1
        right = len(skill) - 2
        current = skill[len(skill) - 1] + skill[0]
        temp = skill[len(skill) - 1] * skill[0]
        while right > left:
            if skill[right] + skill[left] != current:
                return -1
            temp += skill[right] * skill[left]
            
            right -= 1
            left += 1
            
            
        return temp