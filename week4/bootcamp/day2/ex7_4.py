#!/usr/bin/env python3
import sqlite3
import csv

def solve() -> str:
    """
    Tải file sau về cùng thư mục với file code này
    https://github.com/NUKnightLab/sql-mysteries/raw/master/sql-murder-mystery.db
    Đây là 1 file database, 1 file dạng binary lưu trữ dữ liệu.
    File ở dạng binary (như file nhạc, film) nên không thể mở bằng text editor
    để đọc được. File này chứa dữ liệu của phần mềm sqlite, có thể dùng
    ngôn ngữ SQL để truy cập.
    Đọc file ex10/database.md để có hiểu biết tổng quát về database.
    https://sqlzoo.net/wiki/SQL_Tutorial

    Phần từ sau dòng này trở đi không bắt buộc, đây là 1 bài đọc.
    Làm theo hướng dẫn tại https://mystery.knightlab.com/
    Xem bài hướng dẫn tại đây https://mystery.knightlab.com/walkthrough.html

    Return tên kẻ đứng sau vụ giết người.

    Dùng thư viện có sẵn sqlite3 giải bài này.
    """
    db_file = "sql-murder-mystery.db"

    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """

        # connect to file
        conn = sqlite3.connect(db_file)
        # create cursor
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM crime_scene_report")

        rows = cur.fetchall()

        for row in rows:
            print(row)

        conn.close()
    
    create_connection(db_file)

    return None


def main():
    print("The real villain behind this crime is ", solve())


if __name__ == "__main__":
    main()