# Author: jakub-kuba

# The program allows you to edit a json file containing countries
# and addresses (stadiony.net)

import sys
import json

def open_file(file_name, mode):
    """Check if the correct file exists"""
    try:
        with open(file_name, mode) as f:
            json.load(f)
    except FileNotFoundError:
        print("\nThe file not found. Ending the program.\n")
        sys.exit()


def ask_yes_no(myfile, question):
    """Add a country & address to the dictionary"""
    with open(myfile, "r") as f:
        mydict = json.load(f)
    keys_sorted = sorted(mydict.keys())
    dict_sorted = {key:mydict[key] for key in keys_sorted}
    print("Countries available:\n", dict_sorted)
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        while response == "y":
            with open(myfile, "r") as f:
                mydict = json.load(f)
            country = input("Add a country: ")
            add = input("Address: ")
            mydict[country] = add
            with open('countries_dict.json', 'w') as f:
                json.dump(mydict, f)
            keys = sorted(list(mydict.keys()))
            print("Countries available:", keys)
            response = input(question).lower()


def delete_country(myfile, question):
    """Delete a country from the dictionary"""
    with open(myfile, "r") as f:
        mydict = json.load(f)
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        while response == "y":
            with open(myfile, "r") as f:
                mydict = json.load(f)
            country = input("Delete a country: ")
            while country in mydict:
                del mydict[country]
                with open('countries_dict.json', 'w') as f:
                    json.dump(mydict, f)
                keys = sorted(list(mydict.keys()))
                print("Countries available:", keys)
                f.close()
                response = input(question).lower()


def main():
    myfile = "countries_dict.json"
    open_file(myfile, "r")
    ask_yes_no(myfile, "Do you want to add a country? (y/n): ")
    delete_country(myfile, "Do you want to delete a country? (y/n): ")
  
if __name__== "__main__":
      main()