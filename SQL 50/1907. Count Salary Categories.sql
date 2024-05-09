-- 1907. Count Salary Categories

-- Table: Accounts

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | account_id  | int  |
-- | income      | int  |
-- +-------------+------+
-- account_id is the primary key (column with unique values) for this table.
-- Each row contains information about the monthly income for one bank account.
 

-- Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

-- "Low Salary": All the salaries strictly less than $20000.
-- "Average Salary": All the salaries in the inclusive range [$20000, $50000].
-- "High Salary": All the salaries strictly greater than $50000.
-- The result table must contain all three categories. If there are no accounts in a category, return 0.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Accounts table:
-- +------------+--------+
-- | account_id | income |
-- +------------+--------+
-- | 3          | 108939 |
-- | 2          | 12747  |
-- | 8          | 87709  |
-- | 6          | 91796  |
-- +------------+--------+
-- Output: 
-- +----------------+----------------+
-- | category       | accounts_count |
-- +----------------+----------------+
-- | Low Salary     | 1              |
-- | Average Salary | 0              |
-- | High Salary    | 3              |
-- +----------------+----------------+
-- Explanation: 
-- Low Salary: Account 2.
-- Average Salary: No accounts.
-- High Salary: Accounts 3, 6, and 8.


# Write your MySQL query statement below
select "Low Salary" as category, (select count(income) from accounts where income < 20000) as accounts_count
union
select "Average Salary" as category, (select count(income) from accounts where income >= 20000 and income <= 50000) as accounts_count
union
select "High Salary" as category, (select count(income) from accounts where income > 50000) as accounts_count


-- Method 2

-- SELECT cty.category, COALESCE(COUNT(q.category), 0) accounts_count FROM (
--     SELECT 
--         CASE WHEN income < 20000 THEN 'Low Salary' 
--             WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
--             WHEN income > 50000 THEN 'High Salary' END category
--     FROM Accounts
-- ) AS q
-- RIGHT JOIN (SELECT 'Low Salary' AS category UNION ALL SELECT 'Average Salary' UNION ALL SELECT 'High Salary')
-- AS cty ON q.category = cty.category
-- GROUP BY category
