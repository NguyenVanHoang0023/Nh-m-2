import csv
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
            for sv in lstsinhvien:
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
      print('{:15}{:15}{:15}{:15}{:>20}{:>20}'.format('ma_sv','ten_sv','nam_sinh','gioi_tinh','tbcn','hoc_bong'))

      for sv in lstsinhvien:
            print('{:15}{:15}{:15}{:15}{:>20}{:>20}'.format(sv['ma_sv'],sv['ten_sv'],\
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
      tong+=float(('hoc_bong'))
      print('Tổng tiền học bổng là: %f'%tong)
      return
#-------------------
def xoa_sv(lstsinhvien,ma_sv):
      for i in range(len(lstsinhvien)):
            sv=lstsinhvien[i]
            if sv['ma_sv']==ma_sv:
                  del(lstsinhvien[i])
                  return 1
      return 0

#--------------------
def loc_ds_sv(lstsinhvien):
      list_diem=list(filter(lambda i:'tbcn' in i,list_diem))
      print('list_diem:',list_diem)
      return
#-------------------
def sapxep(lstsinhvien):
    sorted_hoc_bong = sorted(lstsinhvien, key=lambda x: x['hoc_bong'])

    return sorted_hoc_bong 

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
