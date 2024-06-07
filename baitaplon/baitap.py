import random
import csv

# Hàm mô phỏng một lần chơi Monty Hall
def mo_phong_monty_hall():
    cua = ['dê', 'dê', 'xe hơi']
    random.shuffle(cua)
    
    lua_chon_nguoi_choi = random.randint(0, 2)
    cua_kha_dung = set([0, 1, 2])
    
    # Monty Hall tiết lộ một cánh cửa có dê
    cua_tiet_lo = random.choice([c for c in cua_kha_dung if c != lua_chon_nguoi_choi and cua[c] == 'dê'])
    
    # Người chơi quyết định đổi
    lua_chon_doi = list(cua_kha_dung - {lua_chon_nguoi_choi, cua_tiet_lo})[0]
    
    # Kết quả của mỗi lựa chọn
    ket_qua_giu = (cua[lua_chon_nguoi_choi] == 'xe hơi')
    ket_qua_doi = (cua[lua_chon_doi] == 'xe hơi')
    
    return lua_chon_nguoi_choi, cua_tiet_lo, lua_chon_doi, ket_qua_giu, ket_qua_doi

# Tính xác suất thắng khi giữ nguyên hoặc đổi lựa chọn
def tinh_xac_suat(so_lan_mo_phong):
    ket_qua = {
        'giu': 0,
        'doi': 0
    }
    
    tro_choi = []
    
    for _ in range(so_lan_mo_phong):
        lua_chon_nguoi_choi, cua_tiet_lo, lua_chon_doi, ket_qua_giu, ket_qua_doi = mo_phong_monty_hall()
        tro_choi.append({
            'lua_chon_ban_dau': lua_chon_nguoi_choi,
            'cua_tiet_lo': cua_tiet_lo,
            'lua_chon_doi': lua_chon_doi,
            'ket_qua_giu': ket_qua_giu,
            'ket_qua_doi': ket_qua_doi
        })
        
        if ket_qua_giu:
            ket_qua['giu'] += 1
        if ket_qua_doi:
            ket_qua['doi'] += 1
    
    xac_suat = {
        'giu': ket_qua['giu'] / so_lan_mo_phong,
        'doi': ket_qua['doi'] / so_lan_mo_phong
    }
    
    return xac_suat, tro_choi

# Lưu kết quả vào file CSV
def luu_ket_qua_csv(tro_choi, xac_suat, ten_file='ket_qua_monty_hall.csv'):
    with open(ten_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['lua_chon_ban_dau', 'cua_tiet_lo', 'lua_chon_doi', 'ket_qua_giu', 'ket_qua_doi'])
        
        for game in tro_choi:
            writer.writerow([game['lua_chon_ban_dau'], game['cua_tiet_lo'], game['lua_chon_doi'], game['ket_qua_giu'], game['ket_qua_doi']])
        
        writer.writerow([])
        writer.writerow(['xac_suat_giu', 'xac_suat_doi'])
        writer.writerow([xac_suat['giu'], xac_suat['doi']])

# Thực hiện mô phỏng và lưu kết quả
so_lan_mo_phong = 200
xac_suat, tro_choi = tinh_xac_suat(so_lan_mo_phong)
luu_ket_qua_csv(tro_choi, xac_suat)

print(f"Xác suất thắng khi giữ nguyên lựa chọn ban đầu: {xac_suat['giu']:.2f}")
print(f"Xác suất thắng khi đổi lựa chọn: {xac_suat['doi']:.2f}")