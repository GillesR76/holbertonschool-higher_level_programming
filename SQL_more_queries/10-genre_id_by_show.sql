-- Script that lists the title of TV shows and their corresponding genre IDs.
-- It uses an inner join between the "tv_shows" and "tv_show_genres" tables using the 
-- "id" and "show_id" columns respectively.
-- The result is ordered by the title of the TV show and the genre ID.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id