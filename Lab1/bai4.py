
import math

def tu_giac_deu(chieu_dai_day, chieu_cao):
    # Tính diện tích xung quanh
    dien_tich_xung_quanh = (chieu_dai_day * math.sqrt(3) / 4) * chieu_dai_day * 4
    
    # Tính diện tích toàn phần
    dien_tich_toan_phan = dien_tich_xung_quanh + (chieu_dai_day ** 2)
    
    # Tính thể tích
    the_tich = (chieu_dai_day ** 2 * chieu_cao * math.sqrt(3)) / 4
    
    return dien_tich_xung_quanh, dien_tich_toan_phan, the_tich

# Nhập độ dài cạnh đáy và chiều cao từ người dùng
chieu_dai_day = float(input("Nhập độ dài cạnh đáy của hình chóp tứ giác đều: "))
chieu_cao = float(input("Nhập chiều cao của hình chóp tứ giác đều: "))

# Tính toán các giá trị
dien_tich_xung_quanh, dien_tich_toan_phan, the_tich = tu_giac_deu(chieu_dai_day,chieu_cao)

# In kết quả
print("Diện tích xung quanh của hình chóp tứ giác đều là: {:.2f}".format(dien_tich_xung_quanh))
print("Diện tích toàn phần của hình chóp tứ giác đều là: {:.2f}".format(dien_tich_toan_phan))
print("Thể tích của hình chóp tứ giác đều là: {:.2f}".format(the_tich))
