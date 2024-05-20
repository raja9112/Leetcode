# 649. Dota2 Senate

# Medium - Leetcode 75

# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

# Constraints:

# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        R, D = deque(), deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                R.append(i)
            else:
                D.append(i)

        while D and R:
            Dturn = D.popleft()
            Rturn = R.popleft()

            if Rturn < Dturn:
                R.append(Dturn + len(senate))
            else:
                D.append(Rturn + len(senate))


        return "Radiant" if R else "Dire"

# The two expressions `R, D = deque(), deque()` and `R = D = deque()` are not the same because they handle the assignment differently.

# 1. **`R, D = deque(), deque()`**:
#    - This line creates two separate `deque` objects and assigns them to `R` and `D` respectively.
#    - `R` and `D` are independent of each other, meaning that modifying one will not affect the other.
#    - Example:
#      ```python
#      from collections import deque
     
#      R, D = deque(), deque()
     
#      R.append(1)
#      D.append(2)
     
#      print(R)  # Output: deque([1])
#      print(D)  # Output: deque([2])
#      ```

# 2. **`R = D = deque()`**:
#    - This line creates a single `deque` object and assigns it to both `R` and `D`.
#    - `R` and `D` refer to the same object, meaning that modifying one will affect the other.
#    - Example:
#      ```python
#      from collections import deque
     
#      R = D = deque()
     
#      R.append(1)
#      D.append(2)
     
#      print(R)  # Output: deque([1, 2])
#      print(D)  # Output: deque([1, 2])
#      ```

# ### Explanation:
# - In `R, D = deque(), deque()`, the right-hand side creates two distinct `deque` instances, one for `R` and one for `D`.
# - In `R = D = deque()`, the right-hand side creates a single `deque` instance, and both `R` and `D` are references to this same instance.

# This distinction is crucial in scenarios where the objects are mutable (like `deque`). If you want `R` and `D` to operate on separate `deque` instances, 
# you should use `R, D = deque(), deque()`. If you want them to be references to the same instance, use `R = D = deque()`.