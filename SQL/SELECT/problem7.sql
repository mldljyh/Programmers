-- Programmmers SQL SELECT Problem 7
-- https://programmers.co.kr/learn/courses/30/lessons/59405
SELECT NAME 
FROM(
    SELECT NAME
    FROM ANIMAL_INS
    ORDER BY DATETIME
)
WHERE ROWNUM <= 1;
