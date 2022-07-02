import pandas as pd
import pickle
import sys
from datetime import datetime
import seaborn as sns

##/home/j/Documents/Python/stadiums

#open the file
def open_file(file_name, mode):     
    try:
        f = open(file_name, mode)
        f.close()
    except:
        print("The file not found. Ending the program.\n")
        sys.exit()

#create a DataFrame
def create_df():
    column_names = ["League", "Capacity"]
    new_df = pd.DataFrame(columns = column_names)
    new_df['Capacity'] = new_df['Capacity'].astype('int32')
    return new_df

#load the file and show the names of the countries in alphabetical order
def get_countries():
    f = open(myfile, "rb")
    mydict = pickle.load(f)
    keys = sorted(list(mydict.keys()))
    print("Countries available:\n", keys)
    countries = mydict
    f.close()
    return countries

#choose a country from the list
def select_country(number):
    choice = None
    numb = str(number)
    text = "What is country " + numb + "? "  
    while choice not in countries:
        choice = input(text)
    return choice

#return the address of the selected country
def get_address():
    address = countries.get(selected)
    cou = pd.read_html(address)
    return cou

#determine which table relates to the best league
def league_level(country):
    if len(country[0]) < 3:
        std = country[1]
    else:
        std = country[0]
    return std

#
def avg_capacity(df):
    df.columns=['Name', 'City', 'Club', 'Capacity']
    df['Capacity'] = df['Capacity'].str.replace(" ","")
    df['Capacity'] = df['Capacity'].astype('int64')
    cap = round(division['Capacity'].mean())
    return cap


myfile = ("countries.dat")
start = open_file(myfile, "rb")
new_df = create_df()
countries = get_countries()
number = 1

for n in range(5):
    selected = select_country(number)
    myaddress = get_address()
    del countries[selected]
    division = league_level(myaddress)
    capacity = avg_capacity(division)   
    dic = {'League': selected, 'Capacity': capacity}
    new_df = new_df.append(dic, ignore_index = True)
    number += 1

new_df = new_df.sort_values(by=['Capacity'],
         ascending=False).reset_index(drop=True)

now = datetime.now()
date = now.strftime('%d-%b-%Y_%H-%M')
new_df.to_excel("files/avarage capacity "+date+".xlsx", index=False)

print("\nThis is a result:\n", new_df)









