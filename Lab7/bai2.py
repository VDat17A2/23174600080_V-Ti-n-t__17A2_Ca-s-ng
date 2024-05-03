def xep_loai_diem(diem):
    if diem < 4.0:
        return 'F'
    elif diem <= 5.4:
        return 'D'
    elif diem <= 6.9:
        return 'C'
    elif diem <= 8.4:
        return 'B'
    else:
        return 'A'
thong_tin_sinh_vien = {}
for i in range(1, 11):
    ten = input(f"Nhập tên sinh viên {i}: ")
    diem = float(input(f"Nhập điểm thi của sinh viên {i}: "))
    thong_tin_sinh_vien[ten] = diem
xep_loai_sinh_vien = {}
for ten, diem in thong_tin_sinh_vien.items():
    xep_loai = xep_loai_diem(diem)
    xep_loai_sinh_vien[xep_loai] = xep_loai_sinh_vien.get(xep_loai, 0) + 1
print("\nXếp loại học lực và thống kê số lượng sinh viên:")
for xep_loai, so_luong in xep_loai_sinh_vien.items():
    print(f"{xep_loai}: {so_luong} sinh viên")