-- Script that selects the title of tv shows and their genre IDs. 
-- It uses a left join with the "tv_show_genres" table using 
-- the "id" column from "tv_shows" and the "show_id" column from "tv_show_genres":
-- it will return all records from the tv show table, and the matched records from the 
-- tv show genre table. 
-- If a TV show doesn't have a genre, it will display NULL for the genre_id
-- The result is ordered by the title of the TV shows and the genre IDs.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;