-- script that lists all Comedy shows in the database hbtn_0d_tvshows
-- joining the tv shows table to the tv genre table through the tv show
-- genres table which links shows with genres.
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;