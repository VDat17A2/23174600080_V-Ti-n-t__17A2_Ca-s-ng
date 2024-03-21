def xep_loai_diem(diem):
    if 0 <= diem < 5:
        print("Điểm kém")
    elif 5 <= diem < 7:
        print("Điểm trung bình")
    elif 7 <= diem < 8.5:
        print("Điểm khá")
    elif 8.5 <= diem <= 10:
        print("Điểm tốt")
    else:
        print("Điểm không hợp lệ")

# Nhập điểm số từ người dùng
diem = float(input("Nhập điểm số của bài kiểm tra: "))
xep_loai_diem(diem)