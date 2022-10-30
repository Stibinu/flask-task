from contextlib import nullcontext
from multiprocessing.sharedctypes import Value
from operator import truediv
import sqlite3
from flask import Flask
import xlrd
import sys
import requests
import json

url='http://192.168.1.8:8080'
data=[{"oil":381},{"gas":108074},{"brine":939}]
headers={"Content-Type":"application/json"}
response=requests.put(url,data=data,headers=headers)
res=response.json()


app = Flask(__name__)
@app.route('/', methods=['GET'])



def read_xls():
    return xlrd.open_workbook('./data/datasheet.xls')

#annual data calculation
# same well number can exist
# find same well numbers from rows and calculate annaul date for oil , gas , brine 
# oil quarter 1 row 20 , quarter 2 row 30 , so and so on , add the final data 
def calculate_annual():
    sheet = read_xls().sheet_by_index(0)


    well_data = []
    well_uniq = []
    wellvalue = 0

    all_sum = {}
    sum_oil = 0
    sum_gas = 0
    sum_brine = 0
    i = 1
    for row in range(i, sheet.nrows -1, i + 1):
        wellvalue = sheet.row_values(row)[0]
        if wellvalue not in well_uniq:
            well_uniq.append(wellvalue)
    for row in range(i, sheet.nrows -1, i + 1):
        wellvalue = sheet.row_values(row)[0]
        if wellvalue in well_uniq:
            sum_oil = sum_oil + sheet.row_values(row)[8]
            sum_gas = sum_gas + sheet.row_values(row)[9]
            sum_brine = sum_brine + sheet.row_values(row)[10]

            all_sum[wellvalue + ": oil ="] = sum_oil
            all_sum[wellvalue + ": gas ="] = sum_gas
            all_sum[wellvalue + ": brine ="] = sum_brine
            
    print(all_sum)

calculate_annual()  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

          


     #    rowval = sheet.row_values(wellnumberindex)[0]
    #    for column in range(0,sheet.ncols):
    #         sheet.row_values(column)
        

        







