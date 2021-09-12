SELECT App_ID_Info.appid, App_ID_Info.Title, App_ID_Info.Type, App_ID_Info.Price, App_ID_Info.Rating, App_ID_Info.Required_Age, App_ID_Info.Is_Multiplayer, Games_Genres.Genre
FROM   App_ID_Info
LEFT JOIN Games_Genres
ON App_ID_Info.appid = Games_Genres.appid
WHERE App_ID_Info.Type = "game" AND App_ID_Info.Rating >0
GROUP BY Games_Genres.Genre