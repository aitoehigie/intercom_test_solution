#!/usr/bin/env python3

import click
import pprint
import ujson as json
from math import sin, cos, acos, radians
########################################
# Intercom Dublin latitude and longitude
########################################

INTERCOM_LATITUDE = 53.339428
INTERCOM_LONGITUDE = -6.257664

def distance_calculator(slat, slong, elat, elong):
    try:
        slat = radians(slat)
        slong = radians(slong)
        elat = radians(elat)
        elong = radians(elong)
        longitude_delta = slong - elong
        distance = 6371* acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(longitude_delta))
        return round(distance, 2)
    except:
        return 0


def app(file_name):
    customers = []
    try:
        with open(file_name, "r") as file:
            for line in file.readlines():        
                json_data = json.loads(line)
                elat = float(json_data.get("latitude"))
                elong = float(json_data.get("longitude"))
                distance = distance_calculator(slat=INTERCOM_LATITUDE, slong=INTERCOM_LONGITUDE, elat=elat, elong=elong)
                if distance <= 100:
                    customers.append(dict(name = json_data.get("name"), user_id = json_data.get("user_id")))                
                else:
                    continue
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        print ("Unexpeceted error:", sys.exc_info()[0])
    customers = sorted(customers, key=lambda customers: customers["user_id"])
    return customers

@click.command()
@click.argument("file_name")
def main(file_name):
    """
   This is little program that will read the full list of customers and output
   the names and user ids of matching customers (within 100km) of Intercom Dublin offices, sorted by User ID (ascending).
   Why? They are good guys and want to invite them for lunch. :)

   It is compulsory while calling the program that you pass in a json file containing the customer details.
   """
    pp = pprint.PrettyPrinter(indent=2)
    return pp.pprint(app(file_name))

if __name__ == "__main__":
    print (main())
