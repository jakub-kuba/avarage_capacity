# Author: jakub-kuba

# Select 5 countries and see the average stadium capacity
# in their top football league (source:stadiony.net)

import pandas as pd
import json
import sys
import requests
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def open_file(file_name, mode):
    """Check if the correct file exists"""
    try:
        with open(file_name, mode) as f:
            json.load(f)
    except FileNotFoundError:
        print("\nThe file not found. The program has quit.\n")
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
    with open(myfile, "r") as f:
        mydict = json.load(f)
    keys = sorted(list(mydict.keys()))
    print("Countries available:\n", keys)
    countries = mydict
    return countries


def select_country(countries, number):
    """Choose a country from the list."""
    choice = None
    numb = str(number)
    text = "What is country " + numb + "? "  
    while choice not in countries:
        choice = input(text)
    return choice


def get_address(countries, selected, address):
    """Return the address of the selected country."""
    
    code = countries.get(selected)
    cou = pd.read_html(address+code)
    return cou


def get_address(countries, selected, address):
    """Return the address of the selected country."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    code = countries.get(selected)
    response = requests.get(address+code, headers=headers)
    if response.status_code == 200:
        cou = pd.read_html(response.text)
        return cou
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")


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
    myfile = "countries_dict.json"
    address = 'http://stadiony.net/stadiony/'
    open_file(myfile, "r")
    new_df = create_df()
    df_list = []
    countries = get_countries(myfile)
    number = 1

    for n in range(5):
        selected = select_country(countries, number)
        myaddress = get_address(countries, selected, address)
        del countries[selected]
        division = league_level(myaddress)
        capacity = avg_capacity(division)   
        dic = {'League': selected, 'Capacity': capacity}
        df_list.append(dic)
        number += 1

    new_df = pd.DataFrame.from_records(df_list)
    new_df = new_df.sort_values(by=['Capacity'],
            ascending=False).reset_index(drop=True)

    now = datetime.now()
    date = now.strftime('%d-%b-%Y_%H-%M')
    new_df.to_excel("files/avarage capacity "+date+".xlsx", index=False)

    print("\nThis is a result:\n", new_df, '\n')

    fig,ax = plt.subplots(figsize=(9, 4.5))
    sns.set(style="whitegrid")
    ax.set_axisbelow(True)
    ax.grid(color='gray')
    ax.set_title("Average stadium capacity in the top football leagues")
    x = "Capacity"
    y = "League"
    colours = ["#07941c", "#8c8989", "#8c8989", "#8c8989", "#8c8989"]
    customPalette = sns.set_palette(sns.color_palette(colours))
    sns.barplot(x=x, y=y, data=new_df, orient='h', palette=customPalette)
    plt.show()

if __name__== "__main__":
      main()