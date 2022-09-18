# Author: jakub-kuba

# not in use

import pickle
import sys

def open_file(file_name, mode):
    """Check if the correct file exists"""
    try:
        f = open(file_name, mode)
        f.close()
    except FileNotFoundError:
        print("\nThe file not found. Ending the program.\n")
        sys.exit()

def ask_yes_no(myfile, question):
    """Add a country & address to the dictionary"""
    f = open(myfile, "rb")
    mydict = pickle.load(f)
    keys_sorted = sorted(mydict.keys())
    dict_sorted = {key:mydict[key] for key in keys_sorted}
    print("Countries available:\n", dict_sorted)
    f.close()
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        while response == "y":
            f = open(myfile, "rb")
            mydict = pickle.load(f)
            f.close()
            country = input("Add a country: ")
            add = input("Address: ")
            mydict[country] = add
            f = open(myfile, "wb")
            pickle.dump(mydict, f)
            keys = sorted(list(mydict.keys()))
            print("Countries available:", keys)
            f.close()
            response = input(question).lower()

def delete_country(myfile, question):
    """Delete a country from the dictionary"""
    f = open(myfile, "rb")
    mydict = pickle.load(f)
    keys_sorted = sorted(mydict.keys())
    dict_sorted = {key:mydict[key] for key in keys_sorted}
    print("Countries available:\n", dict_sorted)
    f.close()
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        while response == "y":
            f = open(myfile, "rb")
            mydict = pickle.load(f)
            f.close()
            country = input("Delete a country: ")
            while country in mydict:
                del mydict[country]
                f = open(myfile, "wb")
                pickle.dump(mydict, f)
                keys = sorted(list(mydict.keys()))
                print("Countries available:", keys)
                f.close()
                response = input(question).lower()

def main():
    myfile = "countries.dat"
    open_file(myfile, "rb")
    ask_yes_no(myfile, "Do you want to add a country? (y/n): ")
    delete_country(myfile, "Do you want to delete a country? (y/n): ")
  
if __name__== "__main__":
      main()