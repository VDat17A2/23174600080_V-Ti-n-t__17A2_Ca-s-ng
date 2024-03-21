def doc_so_nguyen(so_nguyen):
    # Danh sách các từ đơn vị
    don_vi = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # Danh sách các từ đặc biệt cho các số từ 10 đến 19
    dac_biet = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    # Danh sách các từ chục
    chuc = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    # Tách chữ số hàng trăm, chục và đơn vị
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen % 100) // 10
    hang_don_vi = so_nguyen % 10

    # Tạo cách đọc của số nguyên
    doc = ''
    if hang_tram != 0:
        doc += don_vi[hang_tram] + ' hundred '

    if hang_chuc == 1:
        doc += dac_biet[hang_don_vi]
    elif hang_chuc > 1:
        doc += chuc[hang_chuc - 2] + ' '
        if hang_don_vi != 0:
            doc += don_vi[hang_don_vi]
    elif hang_don_vi != 0:
        doc += don_vi[hang_don_vi]

    return doc

# Nhập số nguyên có ba chữ số từ người dùng
so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))

# In cách đọc của số nguyên
print("Cách đọc của số là:", doc_so_nguyen(so_nguyen))