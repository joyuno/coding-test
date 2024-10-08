-- 코드를 입력하세요
SELECT YEAR(B.SALES_DATE) AS YEAR,MONTH(B.SALES_DATE) AS MONTH, A.GENDER, COUNT(DISTINCT B.USER_ID) AS USERS
FROM ONLINE_SALE B
JOIN (SELECT USER_ID,GENDER FROM USER_INFO WHERE GENDER IS NOT NULL) AS A
ON A.USER_ID = B.USER_ID
GROUP BY YEAR, MONTH, A.GENDER 
ORDER BY YEAR, MONTH, A.GENDER ASC