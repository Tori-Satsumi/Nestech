#!/usr/bin/env python3

import csv
import os
import time

import urllib.request, json 


# bài này khó. làm đc thì làm 


def find_max_price(datafile):
    with urllib.request.urlopen("http://api.bitcoincharts.com/v1/csv/") as url:
        data = json.load(url)
        print(data)

            
        return None


def solve():
    """Tìm ngày giá BTC lên cao nhất. Trả về Tuple chứa ngày ở định dạng
    YYYY-mm-dd (VD: 2017-06-19) và giá VND của 1 BTC
    """
    # http://api.bitcoincharts.com/v1/csv/
    datafile = "localbtcVND.csv"
    exdir = os.path.dirname(__file__)
    datapath = os.path.join(exdir, datafile)

    result = find_max_price(datapath)
    return result


def main():
    now = time.gmtime(int(time.time()))
    print(now.tm_year, now.tm_mon, now.tm_mday)
    print(solve())


if __name__ == "__main__":
    main()