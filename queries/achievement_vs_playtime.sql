SELECT Games_1.appid, SUM(Games_1.playtime_forever), Achievement_Percentages.Name, Achievement_Percentages.Percentage
FROM   Games_1
LEFT JOIN Achievement_Percentages ON Games_1.appid = Achievement_Percentages.appid
GROUP BY Games_1.appid;