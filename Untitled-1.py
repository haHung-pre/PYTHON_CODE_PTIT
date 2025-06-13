class ThiSinh:
    def __init__(self, ho_ten, ngay_sinh, diem_mon_1, diem_mon_2, diem_mon_3):
        self.ho_ten = ho_ten.strip()[:50]
        self.ngay_sinh = ngay_sinh
        self.diem_mon_1 = float(diem_mon_1)
        self.diem_mon_2 = float(diem_mon_2)
        self.diem_mon_3 = float(diem_mon_3)
        self.tong_diem = self.diem_mon_1 + self.diem_mon_2 + self.diem_mon_3

    def output(self):
        print(f"{self.ho_ten} {self.ngay_sinh} {self.tong_diem:.1f}")

ho_ten = input()
ngay_sinh = input()
diem_mon_1 = input()
diem_mon_2 = input()
diem_mon_3 = input()

thi_sinh = ThiSinh(ho_ten, ngay_sinh, diem_mon_1, diem_mon_2, diem_mon_3)
thi_sinh.output()