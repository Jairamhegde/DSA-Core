select l.book_id,l.title,l.author,l.genre,l.publication_year,count(*) as current_borrowers
from library_books l

join borrowing_records b on l.book_id = b.book_id
where b.return_date is null
group by l.book_id,l.title,l.author,l.genre,l.publication_year,l.total_copies
having l.total_copies - current_borrowers= 0
order by current_borrowers desc, l.title asc;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna