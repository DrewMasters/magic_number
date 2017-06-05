import pandas as pd

file_location = r'./test_files/'
c_standings = 'standings.csv'
c_week = 'c_week.csv'

standings = pd.read_csv(file_location+c_standings,names=['Team','Wins','Losses','Games_Remaining','Magic_Number'])
