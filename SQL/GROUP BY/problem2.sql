-- Programmers SQL GROUP BY problem 2
-- https://programmers.co.kr/learn/courses/30/lessons/59041
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
HAVING COUNT(NAME) >= 2
GROUP BY NAME
ORDER BY NAME;
