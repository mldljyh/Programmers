-- Programmers SQL String, Date problem 3
-- https://programmers.co.kr/learn/courses/30/lessons/59409
SELECT a.ANIMAL_ID, a.NAME, NVL2(b.ANIMAL_ID,'O','X') AS  중성화
FROM ANIMAL_INS a
    LEFT OUTER JOIN 
    (SELECT ANIMAL_ID
      FROM ANIMAL_INS
      WHERE SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%'
    ) b
    ON a.ANIMAL_ID = b.ANIMAL_ID
--WHERE NOT NAME IS NULL
ORDER BY a.ANIMAL_ID;
