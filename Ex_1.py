#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ვითვლით თითოეული გუნდის მოგებების პროცენტულ მაჩვენებელს
(რამდენი პროცენტია მოგებების საერთოდ ჩატარებული თამაშებიდან)
და ცალკე კონტეინერში ვინახავთ ყველაზე
მაღალი პროცენტული მაჩვენებლით 3 საფეხბურთო გუნდს
'''
import  numpy as np
import pandas as pd
data = pd.read_csv('football.csv')

# percentage გამოთვლა და ჩასმა 
data['Percent'] = (data.Wins / data.Games) * 100
print(data)

# გუნდების სორტირება პროცენტის მიხედვით და ტოპ 3 ის ამოღება
best_teams = (data.sort_values(by='Percent',ascending=[False])).head(3)
# print(best_teams)

# შენახვა
team_list = best_teams.values.tolist()
# print(team_list)

'''
ასევე ცალკე კონტეინერში ვინახავთ იმ გუნდების ჩანაწერებს,
რომელთა წაგებული მატჩების რაოდენობა აღემატება
როგორც მოგებულს ასევე ფრედ დასრულებულ თამაშს
'''
# წაგებული მატჩები მეტია  მოგებულს და ფრეს
bad_teams = data[(data.Losses > data.Wins ) & (data.Losses > data.Draws)]
# ექსელში გამოტანა (შესამოწმებლად)
bad_teams.to_excel(r'/home/davit/Desktop/py/შუალედური_2/davit datunashvili/Ex_1.xls', sheet_name='data', index = False)
# print(bad_teams)

'''
ორივე კონტეინერს, რიმელებიც მიიღეთ ანალიზის შედეგად უნდა ჩაწეროთ ახალ ფაილში სახელად proccesed (შეგიძლიათ შეინახოთ როგორც csv ფაილად ასევე txt ფაილად),
თითოეული კონტეინერის ჩაწერის შემდეგ ფაილში გამოყავით ადგილი მეორე კონტეინერის შიგთავსის ჩაწერამდე (შეგიძლიათ ცარიელი ხაზებით გამოყოთ ადგილი, შეგიძლიათ რაიმე სიმბოლოებით(მაგ: “**************”))
'''
# ადგილის ჩამატება
best_teams = best_teams.append(pd.Series(), ignore_index = True)
best_teams = best_teams.replace(np.nan, '#########', regex=True)
# print (best_teams)

# ინდექსების გასწორება
best_teams.sort_index()
bad_teams.sort_index()
# დაჯგუფება
proccesed = pd.concat([best_teams,bad_teams])
# print(proccesed)

# შენახვა proccesed.csv ფაილში
proccesed.to_csv('/home/davit/Desktop/py/შუალედური_2/davit datunashvili/proccesed.csv', index=True)
