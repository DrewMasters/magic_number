import pandas as pd

file_location = r'./test_files/'
c_standings = 'standings.csv'
c_week = 'c_week.csv'

tmp = file_location+c_standings
print tmp
standings = pd.read_csv(tmp,names=['Team','Wins','Losses','Games_Remaining','Magic_Number'])
print standings
