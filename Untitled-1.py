from datetime import datetime

class TramMua:
    def __init__(self, ten):
        self.ten = ten
        self.tong_luong_mua = 0
        self.tong_thoi_gian = 0

    def them_lan_do(self, start, end, luong):
        fmt = "%H:%M"
        thoi_gian = (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).seconds // 60
        self.tong_luong_mua += luong
        self.tong_thoi_gian += thoi_gian

    def luong_mua_trung_binh(self):
        if self.tong_thoi_gian == 0:
            return 0
        return self.tong_luong_mua * 60 / self.tong_thoi_gian

n = int(input())
ds = []
ma = {}
dem = 0

for _ in range(n):
    ten = input().strip()
    start = input().strip()
    end = input().strip()
    luong = int(input())

    if ten not in ma:
        dem += 1
        ma[ten] = f"T{dem:02d}"
        ds.append(TramMua(ten))

    idx = list(ma).index(ten)
    ds[idx].them_lan_do(start, end, luong)

for ten in ma:
    idx = list(ma).index(ten)
    print(ma[ten], ten, f"{ds[idx].luong_mua_trung_binh():.2f}")