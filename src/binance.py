# coding: utf-8

import csv
from datetime import datetime

date_format = '%d.%m.%Y %H:%M'

with open('../resources/binance.csv') as file_obj:
    # Skips the heading
    # Using next() method
    heading = next(file_obj)

    rate = {2022:23.41, 2023:22.14}

    total_cost_USD = 0
    total_get_USD = 0
    total_cost_CZK = 0
    total_get_CZK = 0

    for line in file_obj.readlines():
        array = line.split(';')
        if (array[2] == "N/A"):
            print(array)

        if (array[8] != "Fee") & (array[2] != "N/A"):
            year_buy = datetime.strptime(array[2], date_format).year
            year_sell = datetime.strptime(array[3], date_format).year

            buy_usd = float(array[5].replace(",","."))
            buy = buy_usd * float(rate[year_buy])
            total_cost_USD = total_cost_USD + buy_usd
            total_cost_CZK = total_cost_CZK + buy

            sell_usd = float(array[4].replace(",", "."))
            sell = sell_usd * float(rate[year_sell])
            total_get_USD = total_get_USD + sell_usd
            total_get_CZK = total_get_CZK + sell

    print(str(total_cost_CZK) + " CZK " + "/" + str(total_cost_USD) + " USD")
    print(str(total_get_CZK) + " CZK " + "/" + str(total_get_USD) + " USD")

    print ("Profit v CZK: " + str(total_get_CZK - total_cost_CZK))