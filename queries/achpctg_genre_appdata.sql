SELECT App_ID_Info.appid, App_ID_Info.Title, App_ID_Info.Type, Games_Genres.Genre, Achievement_Percentages.Name, Achievement_Percentages.Percentage
FROM   App_ID_Info
LEFT JOIN Games_Genres
ON App_ID_Info.appid = Games_Genres.appid
INNER JOIN Achievement_Percentages
ON App_ID_Info.appid = Achievement_Percentages.appid;