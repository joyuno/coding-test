
SELECT A.book_id, B.author_name, DATE_FORMAT(A.published_date, '%Y-%m-%d')as published_date
from book AS A
join author B on A.author_id = B.author_id
where category in ('경제')
order by published_date asc