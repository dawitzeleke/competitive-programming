class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = [0] * (len(recipes))
        deque = collections.deque()
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient] += [recipes[i]]
                
        answer = []
        for i, ingredient in enumerate(ingredients):
            indegree[i] += len(ingredient)
        queue = collections.deque()
        for supply in supplies:
            queue.append(supply)
        while queue:
            current = queue.popleft()
            if current not in supplies:
                answer.append(current)
            for neighbor in graph[current]:
                indegree[recipes.index(neighbor)] -= 1
                if indegree[recipes.index(neighbor)] == 0:
                    queue.append(neighbor)
        return answer