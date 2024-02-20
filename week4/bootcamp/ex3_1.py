#!/usr/bin/env python3
data = 1234


def solve(input_data):
    """Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    Hàm có sẵn tạo ra integer từ string: 69 == int('69')
    """
    # code here
    try:
        convert = bin(input_data)
        # print(convert)
        for i, _bin in enumerate(convert[::-1]):
            if _bin == "1":
                if i == 0:
                    return "1"
                else:
                    return convert[-i - 1:]            
    except:
        raise ValueError("Input can not invert to integer")



def main():
    print(solve(data))

if __name__ == "__main__":
    main()