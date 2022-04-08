-- Programmers SQL String, Date problem 4
-- https://programmers.co.kr/learn/courses/30/lessons/59411
SELECT ANIMAL_ID, NAME
FROM (SELECT a.ANIMAL_ID AS ANIMAL_ID , a.NAME AS NAME, a.DATETIME - b.DATETIME AS TIMES
      FROM ANIMAL_OUTS a
          INNER JOIN ANIMAL_INS b
          ON a.ANIMAL_ID = b.ANIMAL_ID
      ORDER BY TIMES DESC
      )
WHERE ROWNUM <= 2
