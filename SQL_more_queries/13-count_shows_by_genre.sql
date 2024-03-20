-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- using the AS keyword to rename the columns and counting the number of show_id
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.show_id) AS 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- GROUP BY clause to group the results by genre
GROUP BY tv_genres.name
-- filtering COUNT clause to not display a genre that doesn’t have any shows linked
HAVING COUNT(tv_show_genres.show_id) > 0
-- sorting the results by the number of shows linked to each genre
ORDER BY COUNT(tv_show_genres.show_id) DESC;
