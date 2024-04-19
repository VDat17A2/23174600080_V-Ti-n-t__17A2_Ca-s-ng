def nhap_mang():
    n = int(input("Nhập số lượng phần tử trong mảng: "))
    mang = []
    for i in range(n):
        num = int(input(f"Nhập phần tử thứ {i+1}: "))
        mang.append(num)
    return mang

def tinh_tong_so_chan_le(mang):
    tong_chan = sum(num for num in mang if num % 2 == 0)
    tong_le = sum(num for num in mang if num % 2 != 0)
    return tong_chan, tong_le

mang = nhap_mang()
tong_chan, tong_le = tinh_tong_so_chan_le(mang)
print(f"Tổng các số chẵn trong mảng là: {tong_chan}")
print(f"Tổng các số lẻ trong mảng là: {tong_le}")
