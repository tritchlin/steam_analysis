from q_functions_split import db_interface, db_query

steamdb = db_interface('steamdata.db')
# input sql query file
# steamdb.set_query(path='player_loc_games.sql')
# use one of these if you want to return a csv, or json. Then run file as is.
# For memory issues, use parameter "chunk=number" example: steamdb.get_csv(chunk=1000)
# print(steamdb.get_df())
# steamdb.get_csv()
# steamdb.get_json()
steamdb.exec_script('create_indices.sql')
# steamdb.exec_script('drop_indices.sql')


# testing stuff.
# q = query('all_apps')
# df = steamdb.df_from_query(q)
# steamdb.df_from_query('good_games')S