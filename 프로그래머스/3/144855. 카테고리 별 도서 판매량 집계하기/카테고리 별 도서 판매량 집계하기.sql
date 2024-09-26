-- 코드를 입력하세요
SELECT a.CATEGORY, sum(b.sales) as TOTAL_SALES
from book a
join (select book_id, sales 
      from book_sales 
      where YEAR(sales_date) = 2022 AND MONTH(sales_date) = 1) as b
on a.book_id= b.book_id
group by category 
order by category asc