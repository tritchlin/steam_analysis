SELECT Games_1.steamid, Games_Genres.Genre
FROM   Games_1
INNER JOIN Games_Genres ON Games_1.appid = Games_Genres.appid;