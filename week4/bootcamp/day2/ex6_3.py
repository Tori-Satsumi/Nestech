#!/usr/bin/env python3

import csv
import os
import time
import gzip

# bài này khó. làm đc thì làm 


def find_max_price(datafile):
    # with open(datafile, "rb") as f:
    #     hld = {"time" : None, "Price": 0, "UNKNOWN" : None}
    #     for row in csv.DictReader(f, ["time", "price", "UNKNOWN"]): # NOQA
    #         if hld["Price"] < row["Price"]:
    #             hld = row

    #     try:
    #         # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    #         # raise NotImplementedError("Bạn chưa làm bài này")
    #         pass
    #     finally:
    #         ...
            
    with gzip.open('http://api.bitcoincharts.com/v1/csv/', 'rt', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

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