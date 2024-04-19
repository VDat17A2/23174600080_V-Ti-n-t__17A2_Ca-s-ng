def nhap_day_so():
    """Nhập dãy số từ người dùng."""
    day_so = []
    try:
        while True:
            giatri = input("Nhập số (nhập 'x' để kết thúc): ")
            if giatri.lower() == 'x':
                break
            giatri = float(giatri)  
            day_so.append(giatri)
    except ValueError:
        print("Bạn đã nhập không phải là số. Hãy thử lại.")
        return nhap_day_so()
    return day_so

def tim_so_lon_nhat_nho_nhat(day_so):
    """Tìm số lớn nhất và số nhỏ nhất trong dãy số."""
    if len(day_so) == 0:
        print("Dãy số trống.")
        return
    so_lon_nhat = max(day_so)
    so_nho_nhat = min(day_so)
    print(f"Số lớn nhất trong dãy là: {so_lon_nhat}")
    print(f"Số nhỏ nhất trong dãy là: {so_nho_nhat}")

# Chỉ cần gọi hàm nhap_day_so và tim_so_lon_nhat_nho_nhat trong cùng một dòng
tim_so_lon_nhat_nho_nhat(nhap_day_so())