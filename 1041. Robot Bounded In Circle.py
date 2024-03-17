# 1041. Robot Bounded In Circle

# Medium

# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
# The robot can receive one of three instructions:

# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

# Example 1:

# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
# "G": move one step. Position: (0, 1). Direction: South.
# "G": move one step. Position: (0, 0). Direction: South.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
# Based on that, we return true.
# Example 2:

# Input: instructions = "GG"
# Output: false
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
# Based on that, we return false.
# Example 3:

# Input: instructions = "GL"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
# "G": move one step. Position: (-1, 1). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
# "G": move one step. Position: (-1, 0). Direction: South.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
# "G": move one step. Position: (0, 0). Direction: East.
# "L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
# Based on that, we return true.
 

# Constraints:

# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1   # The robot starts facing north (upwards on a 2D grid).
        x, y = 0, 0     # The robot starts at the origin of the grid.

        for d in instructions:   # Iterate over each instruction.
            if d == "G":     # If the instruction is "G", the robot moves forward in its current direction.
                x, y = x + dirX, y + dirY

            elif d == "L":          # If the instruction is "L", the robot turns left.
                dirX, dirY = -1*dirY, dirX      # This is equivalent to a 90-degree counter-clockwise rotation in a 2D grid.
            else:
                dirX, dirY = dirY, -1*dirX       # This is equivalent to a 90-degree clockwise rotation in a 2D grid.
         # If the robot is not facing north or it has returned to the origin, it is bounded by a circle.
        return (dirX, dirY) != (0, 1) or (x, y) == (0, 0)

        # Time complexity: O(n)
        # Space complexity: O(1)


        # Method: 2
        
        # x, y = 0, 0
        # facing_deg = 0
        # for i in instructions:
        #     if i == 'L':
        #         facing_deg = (facing_deg - 90) % 360
        #     elif i == 'R':
        #         facing_deg = (facing_deg + 90) % 360
        #     elif i == 'G':
        #         if facing_deg == 0:
        #             y +=1
        #         elif facing_deg == 180:
        #             y -=1
        #         elif facing_deg == 90:
        #             x +=1
        #         elif facing_deg == 270:
        #             x -=1

        # return (x == 0 and y == 0) or facing_deg !=0
