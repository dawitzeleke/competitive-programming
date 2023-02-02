class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = [0] * 26
        for task in tasks:
            task_freq[ord(task) - ord('A')] += 1
        task_freq.sort(reverse=True)
        time = 0
        while task_freq[0] > 0:
            i = 0
            while i <= n:
                if task_freq[0] == 0:
                    break
                if i < 26 and task_freq[i] > 0:
                    task_freq[i] -= 1
                time += 1
                i += 1
            task_freq.sort(reverse=True)
        return time
