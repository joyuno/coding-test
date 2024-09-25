SELECT A.ID,
CASE 
    WHEN A.SIZE_OF_COLONY<=100 THEN 'LOW'
    WHEN A.SIZE_OF_COLONY<=1000 THEN 'MEDIUM'
    ELSE 'HIGH'
END AS SIZE
FROM ECOLI_DATA A
ORDER BY ID;