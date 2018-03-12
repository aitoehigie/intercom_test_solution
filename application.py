#!/usr/bin/env python3

##############################################
# application.py
# Author: Ehigie Pascal Aito
# Email: aitoehigie@gmail.com
# date: 11/03/2018
##############################################


import click
import ujson as json
from math import sin, cos, acos, radians
from tabulate import tabulate


################################################
# Intercom Dublin office: latitude and longitude
################################################

INTERCOM_LATITUDE = 53.339428
INTERCOM_LONGITUDE = -6.257664


def distance_calculator(slat, slong, elat, elong):
    try:
        slat = radians(slat)
        slong = radians(slong)
        elat = radians(elat)
        elong = radians(elong)
        longitude_delta = abs(slong - elong)
        distance = 6371 * acos(sin(slat) * sin(elat) +
                               cos(slat) * cos(elat) * cos(longitude_delta))
        return round(distance, 2)
    except ValueError:
        return 0


def file_reader(file_name):
    try:
        with open(file_name, "r") as file_object:
            file_object_data = file_object.readlines()
        return file_object_data
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        return None
    except:
        print ("Unexpeceted error:", sys.exc_info()[0])
        return None


def app_logic(file_name):
    customers = []
    if not isinstance(file_name, str):
        raise TypeError("Please provide a valid JSON file string argument")
    else:
        try:
            file_object_data = file_reader(file_name)
            if file_object_data:
                for line in file_object_data:
                    json_data = json.loads(line)
                    elat = float(json_data.get("latitude"))
                    elong = float(json_data.get("longitude"))
                    distance = distance_calculator(
                        slat=INTERCOM_LATITUDE, slong=INTERCOM_LONGITUDE, elat=elat, elong=elong)
                    if distance <= 100:
                        customers.append(dict(name=json_data.get("name"),
                                              user_id=json_data.get("user_id")))
                    else:
                        continue
            else:
                return None
            customers = sorted(
                customers, key=lambda customers: customers["user_id"])
        except RuntimeError:
            print ("An Error occured")
    return customers


@click.command()
@click.option("--file-name", "-f", help="Enter the name of the json file.",)
def main(file_name):
    """
   This is a little program that will read a JSON file that contains the full list of customers and output
   the names and user ids of matching customers (within 100km) of Intercom Dublin offices, sorted by User ID (ascending).
   Why? They are good guys and want to invite them for some food and drinks. :)

   It is compulsory while calling the program that you pass in a json file containing the customer details.
    """
    customers = app_logic(file_name)
    if customers:
        print(tabulate(customers, headers='keys',
                       tablefmt='psql', showindex=False))
    else:
        print ("The file name is not valid")


if __name__ == "__main__":
    main()
