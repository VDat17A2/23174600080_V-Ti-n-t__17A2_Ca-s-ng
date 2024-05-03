def tao_vu_tien_dat(N):
    vu_tien_dat = {x: x**3 for x in range(1, N+1)}
    return vu_tien_dat

def in_vu_tien_dat(vu_tien_dat):
    for key, value in vu_tien_dat.items():
        print(f"{key}: {value}")
N = int(input("Nhập số nguyên N: "))
vu_tien_dat = tao_vu_tien_dat(N)
print("Từ điển dạng x: x^3:")
in_vu_tien_dat(vu_tien_dat)