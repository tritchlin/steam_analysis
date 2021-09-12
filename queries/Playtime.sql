SELECT Games_1.appid, SUM(Games_1.playtime_forever)
FROM   Games_1
GROUP BY Games_1.appid;