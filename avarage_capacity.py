# Author: jakub-kuba

# Select 5 countries and see the average stadium capacity
# in their top football league (source:stadiony.net)

import pandas as pd
import pickle
import sys
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

def open_file(file_name, mode):
    """Check if the correct file exists."""
    try:
        f = open(file_name, mode)
        f.close()
    except FileNotFoundError:
        print("\nThe file not found. Ending the program.\n")
        sys.exit()

def create_df():
    """Create an empty DataFrame."""
    column_names = ["League", "Capacity"]
    new_df = pd.DataFrame(columns = column_names)
    new_df['Capacity'] = new_df['Capacity'].astype('int32')
    return new_df

def get_countries(myfile):
    """Load the file and show the names of the countries
    in alphabetical order.
    """
    f = open(myfile, "rb")
    mydict = pickle.load(f)
    keys = sorted(list(mydict.keys()))
    print("Countries available:\n", keys)
    countries = mydict
    f.close()
    return countries

def select_country(countries, number):
    """Choose a country from the list."""
    choice = None
    numb = str(number)
    text = "What is country " + numb + "? "  
    while choice not in countries:
        choice = input(text)
    return choice

def get_address(countries, selected):
    """Return the address of the selected country."""
    address = countries.get(selected)
    cou = pd.read_html(address)
    return cou

def league_level(country):
    """Determine which table relates to the best league"""
    if len(country[0]) < 3:
        std = country[1]
    else:
        std = country[0]
    return std

def avg_capacity(df):
    """Modify the selected DF and calculate the avarage for a given league"""
    df.columns=['Name', 'City', 'Club', 'Capacity']
    df['Capacity'] = df['Capacity'].str.replace(" ","")
    df['Capacity'] = df['Capacity'].astype('int64')
    cap = round(df['Capacity'].mean())
    return cap

def main():
    myfile = "countries.dat"
    open_file(myfile, "rb")
    new_df = create_df()
    countries = get_countries(myfile)
    number = 1

    for n in range(5):
        selected = select_country(countries, number)
        myaddress = get_address(countries, selected)
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

    fig,ax = plt.subplots(figsize=(9, 4.5))
    sns.set(style="whitegrid")
    ax.set_axisbelow(True)
    ax.grid(color='gray')
    ax.set_title("Average stadium capacity in the top football leagues")
    x = "Capacity"
    y = "League"
    colours = ["#07941c", "#8c8989", "#8c8989", "#8c8989", "#8c8989"]
    customPalette = sns.set_palette(sns.color_palette(colours))
    sns.barplot(x,y, data=new_df, orient='h', palette=customPalette)
    plt.show()

if __name__== "__main__":
      main()