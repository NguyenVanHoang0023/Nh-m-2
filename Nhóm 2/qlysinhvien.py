''''''
#NHÓM : 02 DHKL 16A1
# 22174600023 Nguyễn Văn Hoàng
# 22174600020 Nguyễn Hoàng Anh
# 22174600016 Bùi Đặng Danh
# 22174600014 Bùi Ngọc Ánh
#22174600027 NGuyễn Hồng Nhung
''''''


# Quản lý sinh viên
import os,csv
import libs.xu_ly_sinh_vien

__path='files/ds_sinhvien.csv'
lstsinhvien=[]

#--------------------------------------------------------------------------------------------
def mo_file_ds_sv(__path,lstsinhvien):
      try:
            f=open(__path,'r', encoding = 'utf-8') 
            for dong in csv.reader(f):
                  if dong[0]=='ma_sv':
                        continue
                  lstsinhvien.append({'ma_sv':dong[0],'ten_sv':dong[1],'nam_sinh':dong[2],\
                        'gioi_tinh':dong[3],'tbcn':dong[4],'hoc_bong':dong[5]})
            f.close()
            return 1
      except Exception as ex1:
            print('Khong mở được file hop le ', ex1)
#----------------------------------------
def luu_ds_sv(__path,lstsinhvien):
      try:
            f=open(__path,'w',newline='', encoding = 'utf-8')
            csv.writer(f).writerow(['ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong'])
            for hd in lstsinhvien:
                  csv.writer(f).writerow([sv['ma_sv'],sv['ten_sv'], sv['nam_sinh'],sv['gioi_tinh'],sv['tbcn'],sv['hoc_bong']])
            f.close()
            return 1
      except Exception as ex1:
            return 0

#---------------------------------------------------------------------------------

def them_tt_sv(lstsinhvien):
      while True:
            ma_sv=input('Nhập mã sinh viên:')
            ten_sv=input('Nhập tên sinh viên:')
            nam_sinh=input('Nhập năm sinh:')
            gioi_tinh=input('Nhập giới tính:')
            tbcn=float(input('Nhập điểm:'))
            hoc_bong=float(input('Nhập tiền học bổng:'))
            lstsinhvien.append({'ma_sv':ma_sv,'ten_sv':ten_sv,'nam_sinh':nam_sinh,\
                  'gioi_tinh':gioi_tinh,'tbcn':tbcn,'hoc_bong':hoc_bong})
            # Heestr lệnh append
            tt=input('Bạn có muốn tiếp tục nhập thêm ? (1:TT)')
            if tt!= '1' :
                  break
      return

#-----------------------------------------------------------------------------------------
def in_ds_sv(lstsinhvien):
      print('{:20}{:20}{:20}{:20}{:>20}{:>20}'.format('ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong'))

      for sv in lstsinhvien:
            print('{:20}{:20}{:20}{:20}{:>20}{:>20}'.format(sv['ma_sv'],sv['ten_sv'],\
                  sv['nam_sinh'],sv['gioi_tinh'],sv['tbcn'],sv['hoc_bong']))
            
      return

#------------
def tra_cuu_sv(lstsinhvien,ma_sv):
      for sv in lstsinhvien:
            if sv['ma_sv'] == ma_sv:
                  return sv
      return

#-----------------------------------------------
def thong_ke(lstsinhvien):
      tong=0
      lstthongke=[]
      for sv in lstsinhvien:
            tong+=float(sv('hoc_bong'))
            print('Tổng tiền học bổng là: %f'%tong)
            return
#-------------------
def xoa_sv(lstsinhvien):
      for i in range(len(lstsinhvien)):
            sv=lstsinhvien[i]
            if sv['ma_sv']==ma_sv:
                  del(lstsinhvien[i])
                  return 1
      return 0

#--------------------
def loc_ds_sv(lstsinhvien):
      for sv in lstsinhvien:
            list_diem=list(filter(lambda i:'tbcn' in i,list_diem))
            print('list_diem:',list_diem)
            return
#-------------------
def sapxep(lstsinhvien):
      sorted_hoc_bong = sorted(lstsinhvien, key=lambda x: x['hoc_bong'])

      return sorted_hoc_bong
#-------------------
def hoc_bong(tbcn):
      tbcn=int(input('Nhập điểm trung bình cả năm:'))
      if tbcn>=9:
            print('Học bổng = 8000000')
      elif tbcn>=8 & tbcn<9:
            print('Học bổng = 5000000')
      elif tbcn>=7 & tbcn<8:
            print('Học bổng = 3000000')
      else:
            print('Học bỏng = 0')
      return 



#------------------Bắt đầu chương trình------------------------------------------------
#-----------viết bởi nhóm 2--------------------
print('CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN!!!!')
while True:
      print('1: Mở danh sách sinh viên ')
      print('2: Thêm sinh viên')
      print('3: In danh sách sinh viên ') 
      print('4: Lưu file danh sách sinh viên')
      print('5: Tra cứu sinh viên')
      print('6: Xóa sinh viên')
      print('7: Thống kê sinh viên theo hộc bổng')
      print('8: Lọc sinh viên theo điểm trung bình cả năm')
      print('9: Sinh viên có học bổng cao nhất')
      
      chon=int(input('Chọn chức năng thực hiện:'))
      if chon ==1:
            if mo_file_ds_sv(__path,lstsinhvien):
                  print('Bạn đã mở file!!')
            else:
                  break

      elif chon ==2:
            them_tt_sv(lstsinhvien)
      elif chon ==3:
            in_ds_sv(lstsinhvien)
      elif chon ==4:
            if luu_ds_sv(__path,luu_ds_sv)==1:
                  print('Lưu thành công!!')
            else:
                  print('Lưu không thành công!!')
            luu_ds_sv(__path,lstsinhvien)
      elif chon ==5:
            ma_sv=input('Nhập mã sinh viên tra cứu:')
            sv=tra_cuu_sv(lstsinhvien,ma_sv)
            if sv==None:
                  print('Không tra cứu được sinh viên %d'%ma_sv)
            else:
                  print(sv)
            tra_cuu_sv(lstsinhvien)
      elif chon ==6:
            ma_sv=input('Nhập mã sinh viên cần xóa:')
            k_tra=input('Bạn có chắc chắn muốn xóa không?( c/C hay k/K )')
            if k_tra=='c'or k_tra=='C':
                  kq=xoa_sv(lstsinhvien,ma_sv)
                  if kq==1:
                        print('Bạn đã xóa sinh viên ',ma_sv)
                  else: 
                        print('Không tồn tại mã sinh viên bạn muốn xóa!!!')
            xoa_sv(lstsinhvien)
      elif chon ==7:
            thong_ke(lstsinhvien)
      elif chon==8:
            loc_ds_sv(lstsinhvien)
      elif chon==9:
            sapxep(lstsinhvien)
      else:
            break
      tt=input('Bạn có muốn tiếp tục? (1:tt)')
      if tt!= '1':
            print
      else:
            os.system('cls')
            input('Gõ phím bất kì để tiếp tục chương trình!!')