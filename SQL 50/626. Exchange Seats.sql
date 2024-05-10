-- 626. Exchange Seats

-- Table: Seat

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | student     | varchar |
-- +-------------+---------+
-- id is the primary key (unique value) column for this table.
-- Each row of this table indicates the name and the ID of a student.
-- id is a continuous increment.
 

-- Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

-- Return the result table ordered by id in ascending order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Seat table:
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Abbot   |
-- | 2  | Doris   |
-- | 3  | Emerson |
-- | 4  | Green   |
-- | 5  | Jeames  |
-- +----+---------+
-- Output: 
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Doris   |
-- | 2  | Abbot   |
-- | 3  | Green   |
-- | 4  | Emerson |
-- | 5  | Jeames  |
-- +----+---------+
-- Explanation: 
-- Note that if the number of students is odd, there is no need to change the last one's seat.

-- Write your MySQL query statement below
SELECT 
CASE WHEN mod(id, 2) = 0 THEN id-1 
    -- For last line: id= 5 means, id+1 = 6 and check if 6 is in the id column, if not place the same student
    WHEN mod(id, 2) = 1 AND id+1 not in (SELECT id FROM seat) THEN id  
    ELSE id+1 END AS id, 

    student 
FROM seat
ORDER BY id

-- Method 2
SELECT 
    CASE WHEN id%2 <> 1 THEN id-1
        WHEN id = (SELECT MAX(id) FROM Seat) AND id%2 = 1 THEN id
        ELSE id+1
    END AS id
    , student
FROM Seat
ORDER BY 1