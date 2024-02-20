"""
                        Toán	Văn	    Anh	    Sử	    Địa    Lý	Hoá	    Sinh
Trần Tuấn Thông           5	     7	     9	     3	     7	    4	  8	      2                  
Nguyễn Hữu Nhân           3	     6	     8	     4	     9	    6	  8	      3                  
Nguyễn Hồng Thái          6	     3	     6	     3	     9	    0	  5	      2                      
Lê Ngọc Nhật Minh         4	     9	     3	     6	     5	    5	  4	      0                      
Hồ Anh Thư                7	     0	     0	     6	     5	    3	  4	      4              
Huỳnh Trọng Minh          4	     6	     6	     1	     9	    1	  5	      5                      
Hà Nhật Khôi              5	     6	     1	     4	     5	    7	  4	      9                  
Phùng Khánh Linh          9	     4	     2	     1	     7	    4	  0	      6                      
Quốc Toản                 8	     6	     1	     5	     3	    2	  9	      2              
Dương Sắc Minh            6	     5	     0	     2	     2	    4	  9	      6                  
Trí Trần                  1	     9	     5	     2	     3	    4	  7	      4              
Hà Tài Nam                1	     6	     1	     1	     3	    8	  1	      7              
Đỗ Quốc Hùng              5	     7	     6	     5	     9	    7	  1	      9                  
Nguyễn Vương Hiếu         3	     6	     4	     3	     9	    8	  7	      4                      
Nguyễn Thị Quốc Nguyên    6	     5	     7	     9	     2	    7	  5	      7                          
"""


"""
chuyển đổi thành list
sample = [
    ["Trần Tuấn Thông",5, 7, 9, 3, 7, 4, 8, 2],
    ["Nguyễn Hữu Nhân",3, 6, 8, 4, 9, 6, 8, 3],
    ["Nguyễn Hồng Thái",6, 3, 6, 3, 9, 0, 5, 2],
    ["Lê Ngọc Nhật Minh",4, 9, 3, 6, 5, 5, 4, 0],
    ["Hồ Anh Thư",7, 0, 0, 6, 5, 3, 4, 4],
    ["Huỳnh Trọng Minh",4, 6, 6, 1, 9, 1, 5, 5],
    ["Hà Nhật Khôi",5, 6, 1, 4, 5, 7, 4, 9],
    ["Phùng Khánh Linh",9, 4, 2, 1, 7, 4, 0, 6],
    ["Quốc Toản",8, 6, 1, 5, 3, 2, 9, 2],
    ["Dương Sắc Minh",6, 5, 0, 2, 2, 4, 9, 6],
    ["Trí Trần",1, 9, 5, 2, 3, 4, 7, 4],
    ["Hà Tài Nam",1, 6, 1, 1, 3, 8, 1, 7],
    ["Đỗ Quốc Hùng",5, 7, 6, 5, 9, 7, 1, 9],
    ["Nguyễn Vương Hiếu",3, 6, 4, 3, 9, 8, 7, 4],
    ["Nguyễn Thị Quốc Nguyên",6, 5, 7, 9, 2, 7, 5, 7]
]
Chuyển đổi thành dictionary (cho anh chị nào biết dùng. nếu ko biết dùng thì anh chị dùng List cũng được nha)

sample = {
    "Trần Tuấn Thông": {
        "Toán": 5,
        "Văn": 7,
        "Anh": 9,
        "Sử": 3,
        "Địa": 7,
        "Lý": 4,
        "Hoá": 8,
        "Sinh": 2,
    },
    "Nguyễn Hữu Nhân": {
        "Toán": 3,
        "Văn": 6,
        "Anh": 8,
        "Sử": 4,
        "Địa": 9,
        "Lý": 6,
        "Hoá": 8,
        "Sinh": 3,
    },
    "Nguyễn Hồng Thái": {
        "Toán": 6,
        "Văn": 3,
        "Anh": 6,
        "Sử": 3,
        "Địa": 9,
        "Lý": 0,
        "Hoá": 5,
        "Sinh": 2,
    },
    "Lê Ngọc Nhật Minh": {
        "Toán": 4,
        "Văn": 9,
        "Anh": 3,
        "Sử": 6,
        "Địa": 5,
        "Lý": 5,
        "Hoá": 4,
        "Sinh": 0,
    },
    "Hồ Anh Thư": {
        "Toán": 7,
        "Văn": 0,
        "Anh": 0,
        "Sử": 6,
        "Địa": 5,
        "Lý": 3,
        "Hoá": 4,
        "Sinh": 4,
    },
    "Huỳnh Trọng Minh": {
        "Toán": 4,
        "Văn": 6,
        "Anh": 6,
        "Sử": 1,
        "Địa": 9,
        "Lý": 1,
        "Hoá": 5,
        "Sinh": 5,
    },
    "Hà Nhật Khôi": {
        "Toán": 5,
        "Văn": 6,
        "Anh": 1,
        "Sử": 4,
        "Địa": 5,
        "Lý": 7,
        "Hoá": 4,
        "Sinh": 9,
    },
    "Phùng Khánh Linh": {
        "Toán": 9,
        "Văn": 4,
        "Anh": 2,
        "Sử": 1,
        "Địa": 7,
        "Lý": 4,
        "Hoá": 0,
        "Sinh": 6,
    },
    "Quốc Toản": {
        "Toán": 8,
        "Văn": 6,
        "Anh": 1,
        "Sử": 5,
        "Địa": 3,
        "Lý": 2,
        "Hoá": 9,
        "Sinh": 2,
    },
    "Dương Sắc Minh": {
        "Toán": 6,
        "Văn": 5,
        "Anh": 0,
        "Sử": 2,
        "Địa": 2,
        "Lý": 4,
        "Hoá": 9,
        "Sinh": 6,
    },
    "Trí Trần": {
        "Toán": 1,
        "Văn": 9,
        "Anh": 5,
        "Sử": 2,
        "Địa": 3,
        "Lý": 4,
        "Hoá": 7,
        "Sinh": 4,
    },
    "Hà Tài Nam": {
        "Toán": 1,
        "Văn": 6,
        "Anh": 1,
        "Sử": 1,
        "Địa": 3,
        "Lý": 8,
        "Hoá": 1,
        "Sinh": 7,
    },
    "Đỗ Quốc Hùng": {
        "Toán": 5,
        "Văn": 7,
        "Anh": 6,
        "Sử": 5,
        "Địa": 9,
        "Lý": 7,
        "Hoá": 1,
        "Sinh": 9,
    },
    "Nguyễn Vương Hiếu": {
        "Toán": 3,
        "Văn": 6,
        "Anh": 4,
        "Sử": 3,
        "Địa": 9,
        "Lý": 8,
        "Hoá": 7,
        "Sinh": 4,
    },
    "Nguyễn Thị Quốc Nguyên": {
        "Toán": 6,
        "Văn": 5,
        "Anh": 7,
        "Sử": 9,
        "Địa": 2,
        "Lý": 7,
        "Hoá": 5,
        "Sinh": 7,
    },
}
"""


"""
Cho data như trên, tương ứng với số điểm cuối năm của các bạn học sinh (data này là fake thôi, ko có ý gì đâu nhé)
dùng python để trả lời các câu hỏi:
    - tìm ra các học sinh bị điểm liệt. biết rằng 1 học sinh bị điểm liệt khi mà điểm thi của học sinh đó dưới 2.5.
    - cho biết có bao nhiêu môn bị liệt? và số điểm liệt của từng môn
    - Tính điểm trung bình cho cả năm học. công thức: tổng số điểm từng môn chia cho tổng số môn. làm tròn tới 2 chữ số sau dấu phẩy
    - phân loại học sinh thành: "Ở lại lớp", "Trung bình", "Khá", "Giỏi", biết:
        - học sinh "Giỏi"       : Nếu điểm trung bình >= 8.0, và không có môn nào dưới 6.5 điểm
        - học sinh "Khá"        : Nếu điểm trung bình >= 6.5, và không có môn nào dưới 5 điểm
        - học sinh "Trung bình" : Nếu điểm trung bình >= 5, và không có môn nào bị liệt
        - "Ở lại lớp"           : Nếu học sinh đó dính bất kì một điểm liệt nào

    # Từ đây trở xuống, coi như điểm của thí sinh là "Điểm thi tốt nghiệp"
    - Tính điểm tốt nghiệp của từng học sinh, biết: điểm tốt nghiệp = điểm toán nhân đôi + điểm văn nhân đôi + điểm Anh + điểm sử
    - Cho biết học sinh nào "Được tốt nghiệp" hoặc "Không đạt tốt nghiệp", biết để được công nhận xét tốt nghiệp, học sinh đó phải có điểm tốt nghiệp >= 30, và ko có môn nào bị điểm liệt
    - Nâng cao: Các thí sinh có quyền lựa chọn khối thi cho bản thân. cho biết các khối thi:
        - Khối A    : Toán - Lý - Hoá
        - Khối A1   : Toán - Lý - Anh
        - Khối B    : Toán - Hoá - Sinh
        - Khối C    : Văn - Sử - Địa
        - Khối D    : Văn - Toán - Anh

        ==> hãy cho biết: 2 nguyện vọng (2 khối thi) mà thí sinh đạt điểm cao nhất
        (Trường hợp 2 khối thi có số điểm bằng nhau thì lấy cả 2)
        Ví dụ: thi sinh Trần tuấn thông:
                - Khối A    : Toán - Lý - Hoá    = (5 + 4 + 8) = 17
                - Khối A1   : Toán - Lý - Anh    = (5 + 4 + 9) = 18
                - Khối B    : Toán - Hoá - Sinh  = (5 + 8 + 2) = 15
                - Khối C    : Văn - Sử - Địa     = (7 + 3 + 7) = 17
                - Khối D    : Văn - Toán - Anh   = (7 + 5 + 9) = 21

                ==> 2 nguyện vọng mà Trần Tuấn Thông đạt điểm cao nhất là khối D với 21 điểm và khối A1 với 18 điểm
"""

#  ========================================================================================

sample = {
    "Trần Tuấn Thông": {
        "Toán": 5,
        "Văn": 7,
        "Anh": 9,
        "Sử": 3,
        "Địa": 7,
        "Lý": 4,
        "Hoá": 8,
        "Sinh": 2,
    },
    "Nguyễn Hữu Nhân": {
        "Toán": 3,
        "Văn": 6,
        "Anh": 8,
        "Sử": 4,
        "Địa": 9,
        "Lý": 6,
        "Hoá": 8,
        "Sinh": 3,
    },
    "Nguyễn Hồng Thái": {
        "Toán": 6,
        "Văn": 3,
        "Anh": 6,
        "Sử": 3,
        "Địa": 9,
        "Lý": 0,
        "Hoá": 5,
        "Sinh": 2,
    },
    "Lê Ngọc Nhật Minh": {
        "Toán": 4,
        "Văn": 9,
        "Anh": 3,
        "Sử": 6,
        "Địa": 5,
        "Lý": 5,
        "Hoá": 4,
        "Sinh": 0,
    },
    "Hồ Anh Thư": {
        "Toán": 7,
        "Văn": 0,
        "Anh": 0,
        "Sử": 6,
        "Địa": 5,
        "Lý": 3,
        "Hoá": 4,
        "Sinh": 4,
    },
    "Huỳnh Trọng Minh": {
        "Toán": 4,
        "Văn": 6,
        "Anh": 6,
        "Sử": 1,
        "Địa": 9,
        "Lý": 1,
        "Hoá": 5,
        "Sinh": 5,
    },
    "Hà Nhật Khôi": {
        "Toán": 5,
        "Văn": 6,
        "Anh": 1,
        "Sử": 4,
        "Địa": 5,
        "Lý": 7,
        "Hoá": 4,
        "Sinh": 9,
    },
    "Phùng Khánh Linh": {
        "Toán": 9,
        "Văn": 4,
        "Anh": 2,
        "Sử": 1,
        "Địa": 7,
        "Lý": 4,
        "Hoá": 0,
        "Sinh": 6,
    },
    "Quốc Toản": {
        "Toán": 8,
        "Văn": 6,
        "Anh": 1,
        "Sử": 5,
        "Địa": 3,
        "Lý": 2,
        "Hoá": 9,
        "Sinh": 2,
    },
    "Dương Sắc Minh": {
        "Toán": 6,
        "Văn": 5,
        "Anh": 0,
        "Sử": 2,
        "Địa": 2,
        "Lý": 4,
        "Hoá": 9,
        "Sinh": 6,
    },
    "Trí Trần": {
        "Toán": 1,
        "Văn": 9,
        "Anh": 5,
        "Sử": 2,
        "Địa": 3,
        "Lý": 4,
        "Hoá": 7,
        "Sinh": 4,
    },
    "Hà Tài Nam": {
        "Toán": 1,
        "Văn": 6,
        "Anh": 1,
        "Sử": 1,
        "Địa": 3,
        "Lý": 8,
        "Hoá": 1,
        "Sinh": 7,
    },
    "Đỗ Quốc Hùng": {
        "Toán": 5,
        "Văn": 7,
        "Anh": 6,
        "Sử": 5,
        "Địa": 9,
        "Lý": 7,
        "Hoá": 1,
        "Sinh": 9,
    },
    "Nguyễn Vương Hiếu": {
        "Toán": 3,
        "Văn": 6,
        "Anh": 4,
        "Sử": 3,
        "Địa": 9,
        "Lý": 8,
        "Hoá": 7,
        "Sinh": 4,
    },
    "Nguyễn Thị Quốc Nguyên": {
        "Toán": 6,
        "Văn": 5,
        "Anh": 7,
        "Sử": 9,
        "Địa": 2,
        "Lý": 7,
        "Hoá": 5,
        "Sinh": 7,
    },
}

#  ========================================================================================

ListOfUnderScoreStudentPerSubject = {}
ListOfAverageScorePerStudent = {}

for name in sample:
    TotalScore = 0.0
    AmountOfSubject = 0.0

    for subject in sample[name]:
        TotalScore += sample[name][subject]
        AmountOfSubject += 1

        if float(sample[name][subject]) <= 2.5:

            try:
                ListOfUnderScoreStudentPerSubject[name]
            except:
                ListOfUnderScoreStudentPerSubject[name] = [{
                    subject : sample[name][subject]
                }]
            else:
                ListOfUnderScoreStudentPerSubject[name].append({
                    subject : sample[name][subject]
                })
    
    ListOfAverageScorePerStudent[name] = round(float( TotalScore / AmountOfSubject), 2)

print()

#  ========================================================================================

def UnderScoreStudentList():
    print("Danh sách học sinh bị liệt:")
    for name in ListOfUnderScoreStudentPerSubject:
        print(f"\n{name} liệt {len(ListOfUnderScoreStudentPerSubject[name])} môn:")
        for lst in ListOfUnderScoreStudentPerSubject[name]:
            for subject in lst:
                print(f"{subject} : {lst[subject]}")

def StudentAverageScore():
    print("\n\nDanh sách điểm trung bình học sinh:\n")
    for name in ListOfAverageScorePerStudent:
        print(f"{name} : {ListOfAverageScorePerStudent[name]}")

#  ========================================================================================

def StudentRank():
    print("\nDanh sách loại học sinh:\n")
    for name1 in ListOfAverageScorePerStudent:
        for name2 in ListOfUnderScoreStudentPerSubject:
            print(f"{name1} ", end="")
            if name1 == name2:
                print("ở lại lớp")
                break
            else:
                AverageScore = ListOfAverageScorePerStudent[name1]
                ScoreChecking = 10

                for subject in sample[name1]:
                    if sample[name1][subject] < ScoreChecking:
                        ScoreChecking = sample[name1][subject]

                if AverageScore >= 8 and ScoreChecking >= 6.5:
                    print("học sinh Giỏi")
                    break
                elif AverageScore >= 6.5 and ScoreChecking >= 5:
                    print("học sinh Khá")
                    break
                elif AverageScore >= 5 and ScoreChecking >= 2.5:
                    print("học sinh Trung bình")
                    break
                else:
                    print("ở lại lớp")
                    break

#  ========================================================================================

def graduation():
    print("\n\nDanh sách học sinh tốt nghiệp:\n")

    LstOfSubjectForGraduation = [
        "Toán",
        "Văn",
        "Anh",
        "Sử",
    ]

    for name1 in ListOfAverageScorePerStudent:
        print(f"{name1} ", end = "")
        TotalScore = 0

        for subject in LstOfSubjectForGraduation:
            if subject == "Toán" or subject == "Văn":
                TotalScore += sample[name1][subject] * 2
            else:
                TotalScore += sample[name1][subject]
        
        if TotalScore >= 30:
            print("Được tốt nghiệp")              
        else:
            print("Không đạt tốt nghiệp")

#  ========================================================================================

def StudentBlockGrade():
    LstOfSubjectForValuation = {
        "A" : ["Toán", "Lý", "Hoá"],
        "A1": ["Toán", "Lý", "Anh"],
        "B" : ["Toán", "Hoá", "Sinh"],
        "C" : ["Văn", "Sử", "Địa"],
        "D" : ["Văn", "Toán", "Anh"],
    }

    Lst = {}

    for name in sample:
        Score1 = 0
        Score2 = 0
        Block1 = ""
        Block2 = ""

        for block in LstOfSubjectForValuation:
            hld = 0

            for subject in LstOfSubjectForValuation[block]:
                hld += sample[name][subject]

            if hld > Score2 or Score1 == 0:
                Score1 = Score2
                Score2 = hld
                
                Block1 = Block2
                Block2 = block

        Lst[name] = {
            Block2 : Score2,            
            Block1 : Score1,
        }

    for name in Lst:
        print(f"\n{name}: ")
        for item in Lst[name]:
            print(f"{item} : {Lst[name][item]}")

print()