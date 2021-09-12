SELECT DISTINCT Title FROM App_ID_Info
LEFT JOIN Games_1
WHERE Games_1.appid = App_ID_Info.appid;