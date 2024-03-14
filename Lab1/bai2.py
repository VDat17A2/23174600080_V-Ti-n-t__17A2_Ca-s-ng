class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
        self.so_luong = so_luong

    def __str__(self):
        return f"{self.ma_sach}: {self.ten_sach} - {self.tac_gia} ({self.nam_xuat_ban}) [{self.so_luong}]"


def main():
    # Nhập thông tin sinh viên
    so_luong_sach = int(input("Nhập số lượng sách: "))
    ma_sinh_vien = input("Nhập mã sinh viên: ")

    # Tạo danh sách sách
    danh_sach_sach = []

    for i in range(so_luong_sach):
        ten_sach = input("Nhập tên sách: ")
        tac_gia = input("Nhập tác giả: ")
        nam_xuat_ban = int(input("Nhập năm xuất bản: "))
        so_luong = int(input("Nhập số lượng sách: "))
        sach = Sach(ma_sinh_vien, ten_sach, tac_gia, nam_xuat_ban, so_luong)
        danh_sach_sach.append(sach)

    # In thông tin sách
    print(f"Thư viện ĐHKTKTCN có {so_luong_sach} sách:")
    for sach in danh_sach_sach:
        print(f"- {sach}")

if __name__ == "__main__":
    main()