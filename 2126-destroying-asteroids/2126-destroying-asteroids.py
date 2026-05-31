class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        new_mass = mass

        for aster in asteroids:
            if new_mass >= aster:
                new_mass += aster
            else:
                return False

        return True