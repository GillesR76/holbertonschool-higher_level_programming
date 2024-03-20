-- Script that lists all shows contained in the database without a
-- genre linked. Using a left join that returns all shows from the 
-- tv shows table and the matched records from the tv show genre.
-- Whith the left join, if there is no match the result is NULL on 
-- the tv show genre side. Using the where/is null condition to filter
-- only the results that return NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id