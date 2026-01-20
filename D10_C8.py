import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module

from itertools import permutations
def xu_li_dau_cham(a):
	str_a=str(a)
	str_a=str_a.replace(".",",")
	return str_a

#Tạo tập hợp khác 0
def tao_taphop_khac_0(n):
	# Tạo một tập hợp rỗng
	unique_digits_set = set()

	while len(unique_digits_set) < n:
	    digit = random.randint(1, 9)  # Tạo một chữ số ngẫu nhiên từ 1 đến 9
	    unique_digits_set.add(digit)
	return unique_digits_set

def tao_taphop_chua_0(n):
	# Tạo một tập hợp rỗng
	unique_digits_set = set()

	# Thêm chữ số 0 vào tập hợp
	unique_digits_set.add(0)

	# Thêm 4 chữ số khác nhau vào tập hợp
	while len(unique_digits_set) < n:
	    digit = random.randint(1, 9)  # Tạo một chữ số ngẫu nhiên từ 1 đến 9
	    unique_digits_set.add(digit)
	return unique_digits_set

#Tính số chỉnh hợp chập k của n
def chinh_hop(k,n):
	t=factorial(n) / factorial(n - k)
	return t

def dem_so_le_den_m(m):
    dem = 0
    for so in range(1, m + 1, 2):
        dem += 1
    return dem

def dem_so_chan_den_m(m):
    dem = 0
    for so in range(2, m + 1, 2):
        dem += 1
    return dem


def tinh_tong_chu_so(so):
    # Lấy giá trị tuyệt đối để đảm bảo không bị lỗi với số âm
    so = abs(so)
    tong = 0
    while so > 0:
        tong += so % 10  # Lấy chữ số cuối cùng
        so //= 10        # Bỏ chữ số cuối cùng
    return tong


################ Bài 1: QUY TẮC CỘNG VÀ QUY TẮC NHÂN ########################
#[D10_C8_B1_01]-M1. Cho 2 nhóm đồ vật. Tìm số cách chọn 1 vật
def mcn__L10_C8_B1_01():   
	#Tạo bậc ngẫu nhiên
	do_vat_1=["chiếc kem que", "cái bút bi", "cuốn vở ô li" , "cuốn truyện cổ tích"]
	do_vat_2=["chiếc kem ốc quế", "cái bút mực","cuốn vở kẻ ngang" , "cuốn tiểu thuyết trinh thám"]
	i= random.randint(0,3)
	vat_1=do_vat_1[i]
	vat_2=do_vat_2[i]
	n=random.randint(5,20)
	m=random.randint(6,30)
	if m==n:
		m=n+random.randint(2,6)
	kq=m+n
	kq2=m*n
	kq3=abs(m-n)
	kq4=m+n+random.randint(2,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Trong một cửa hàng có {m} {vat_1} và {n} {vat_2}." \
	f" Hỏi có bao nhiêu cách chọn mua một {vat_1} hoặc một {vat_2} từ cửa hàng này?"\

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Theo quy tắc cộng ta có số cách chọn là: ${m}+{n}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_02]-M1. Cho số lượng học sinh. Chọn 1 bạn để giữ chức vụ.
def mcn__L10_C8_B1_02():   

	chuc_vu=random.choice(["lớp trưởng", "lớp phó học tập", "lớp phó lao động" , "bí thư chi đoàn", "lớp phó văn nghệ", "cờ đỏ"])
	
	n=random.randint(15,20)
	m=random.randint(15,25)
	if m==n:
		m=n+random.randint(2,6)
	kq=m+n
	kq2=m*n
	kq3=abs(m-n)
	kq4=m+n+random.randint(2,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một lớp có {m} học sinh nam, {n} học sinh nữ." \
	f" Hỏi giáo viên có bao nhiêu cách chọn ra 1 bạn trong lớp để làm {chuc_vu}?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Theo quy tắc cộng ta có số cách chọn là: ${m}+{n}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_03]-M1. Chọn một thức uống từ các loại nước.
def mcn__L10_C8_B1_03():   

	nuoc=["nước ép", "trà sữa" , "nước ngọt có ga", "chè", "sữa chua"]
	random.shuffle(nuoc)
	n=random.randint(3,6)
	m=random.randint(3,6)
	p=random.randint(3,6)
	if m==n==p:
		n=m+random.randint(1,3)
	kq=m+n+p
	kq2=m*n*p
	kq3=m+n*p
	kq4=m*p+n*p

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một quán nước có {m} loại {nuoc[0]}, {n} loại {nuoc[1]} và {p} loại {nuoc[2]}." \
	f" Một khách hàng muốn lựa chọn một loại đồ uống thì có bao nhiêu cách chọn?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Theo quy tắc cộng ta có số cách chọn là: ${m}+{n}+{p}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_04]-M1. Chọn một địa điểm đi du lịch.
def mcn__L10_C8_B1_04():   
	ten_nguoi=random.choice(["Nam", "An", "Minh", "Phương", "Thảo","Mai", "Hoa"])

	khu_vuc=["Thủ đô Hà Nội", "Đà Nẵng" , "Thành phố Hồ Chí Minh", "Thừa Thiên Huế", "Đà Lạt", "Lào Cai", "Phú Quốc", "Hà Giang", "Đắk Lắk"]
	random.shuffle(khu_vuc)

	n=random.randint(3,10)
	m=random.randint(3,10)
	p=random.randint(3,10)
	if m==n==p:
		n=m+random.randint(1,3)
	kq=m+n+p
	kq2=m*n*p
	kq3=m+n*p
	kq4=m*p+n*p

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Gia đình bạn {ten_nguoi} muốn đi du lịch." \
	f" {khu_vuc[0]} có {m} địa điểm, {khu_vuc[1]} có {n} địa điểm, {khu_vuc[2]} có {p} địa điểm."\
	f" Hỏi gia đình bạn {ten_nguoi} có bao nhiêu cách chọn một địa điểm du lịch cho gia đình từ các địa điểm trên?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Theo quy tắc cộng ta có số cách chọn là: ${m}+{n}+{p}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#9.1.2 Quy tắc nhân
#[D10_C8_B1_05]-M1. Cho 2 nhóm đồ vật. Tìm số cách chọn 2 vật.
def mcn__L10_C8_B1_05():   
	#Tạo bậc ngẫu nhiên
	do_vat_1=["chiếc kem que", "cái bút bi", "cuốn vở ô li" , "cuốn truyện cổ tích"]
	do_vat_2=["chiếc kem ốc quế", "cái bút mực","cuốn vở kẻ ngang" , "cuốn tiểu thuyết trinh thám"]
	i= random.randint(0,3)
	vat_1=do_vat_1[i]
	vat_2=do_vat_2[i]
	n=random.randint(5,20)
	m=random.randint(6,30)
	if m==n:
		m=n+random.randint(2,6)
	kq=m*n
	kq2=m+n
	kq3=binomial(m+n, 2)
	kq4=m+n+random.randint(2,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Trong một cửa hàng có {m} {vat_1} và {n} {vat_2}." \
	f" Hỏi có bao nhiêu cách chọn mua một {vat_1} và một {vat_2} từ cửa hàng này?"\

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Theo quy tắc nhân ta có số cách chọn là: ${m}.{n}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_06]-M1. Cho số lượng học sinh. Chọn 2 bạn để giữ chức vụ.
def mcn__L10_C8_B1_06():   

	chuc_vu=["lớp trưởng", "lớp phó học tập", "lớp phó lao động" , "bí thư chi đoàn", "lớp phó văn nghệ", "cờ đỏ", "tổ trưởng"]
	random.shuffle(chuc_vu)
	
	n=random.randint(15,20)
	m=random.randint(15,25)
	if m==n:
		m=n+random.randint(2,6)
	kq=chinh_hop(2,m+n)
	kq2=m+n
	kq3=binomial(m+n, 2)
	kq4=m*n+random.randint(2,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một lớp có ${{{m}}}$ học sinh nam, ${{{n}}}$ học sinh nữ." \
	f" Hỏi giáo viên có bao nhiêu cách chọn ra 2 bạn trong lớp để một bạn làm {chuc_vu[0]} và một bạn làm {chuc_vu[1]}?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Theo quy tắc nhân ta có số cách chọn là: ${{{m+n}.{m+n-1}={kq}}}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_07]-M1. Tìm số đường đi từ A đến B và từ B đến C.
def mcn__L10_C8_B1_07():   

	n=random.randint(3,8)
	m=random.randint(5,9)
	if m==n:
		m=n+random.randint(2,6)
	kq=m*n
	kq2=m+n
	kq3=binomial(m+n, 2)
	kq4=m*n+random.randint(2,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Từ thành phố ${{A}}$ đến thành phố ${{B}}$ có {m} con đường đi, từ thành phố ${{B}}$ đến thành phố ${{C}}$ có {n} con đường đi." \
	f" Hỏi từ thành phố ${{A}}$ có bao nhiêu cách chọn đường đi đến thành phố ${{C}}$ (bắt buộc qua thành phố ${{B}}$)?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Theo quy tắc nhân ta có số cách chọn là: ${m}.{n}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_08]-M2. Từ n chữ số lập được bao nhiêu số có k chữ số.
def mcn__L10_C8_B1_08():  	
	n=random.randint(4,8)
	set_A =my_module.tao_taphop(n,1,9)
	k=random.randint(2,n-1)

	kq=n**k
	kq2=n*k
	kq3=binomial(n, k)
	kq4=factorial(n) / factorial(n - k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Từ các chữ  số $\\{{ {set_A} \\}}$ có thể lập được bao nhiêu số tự nhiên gồm {k} chữ số?" \


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	t=f"{n}"
	a_i=""
	for i in range(1,k+1):
		a_i=a_i +f"a_{i}"
		t=t + f".{n}"
	t=t[:-2]

	noi_dung_loigiai=f"Gọi $\\overline{{{a_i}}}$ là số cần lập.\n"\
		f"Mỗi chữ số ${{a_i}},i=\\overline{{1, {k}}}$ có số cách chọn là: {n}.\n"\
		f"Theo quy tắc nhân ta có số cách lập là: ${t}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_09]-M2. Từ n chữ số lập được bao nhiêu số có k chữ số khác nhau.
def mcn__L10_C8_B1_09():  	
	n=random.randint(4,8)
	set_A =my_module.tao_taphop(n,1,9)
	k=random.randint(2,n-1)

	kq=factorial(n) / factorial(n - k)
	kq2=n*k
	kq3=binomial(n, k)
	kq4=n+k

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Từ các chữ  số $\\{{ {set_A} \\}}$ có thể lập được bao nhiêu số tự nhiên gồm {k} chữ số khác nhau?" \


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	t=f"{n}"
	so_cach=f"{n}"
	a_i=""
	a_i_chu=""
	for i in range(1,k+1):
		a_i=a_i +f"a_{i}"
		a_i_chu=a_i_chu +f"a_{i},"

		t=t + f".{n-i}"
		so_cach=so_cach + f",{n-i}"
	t=t[:-2]
	so_cach=so_cach[:-2]

	a_i_chu=a_i_chu[:-1]

	noi_dung_loigiai=f"Gọi $\\overline{{{a_i}}}$ là số cần lập.\n"\
		f"Mỗi chữ số ${{{a_i_chu}}}$ có số cách chọn lần lượt là: {so_cach}.\n"\
		f"Theo quy tắc nhân ta có số cách lập là: ${t}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_10]-M2. Từ n chữ số có chứa số 0 lập được bao nhiêu số có k chữ số khác nhau.
def mcn__L10_C8_B1_10():  	
	n=random.randint(4,8)
	set_A =tao_taphop_chua_0(n)
	k=random.randint(2,n-1)
	t=chinh_hop(k-1,n-1)

	kq=(n-1)*t
	kq2=n*k
	kq3=binomial(n, k)
	kq4=chinh_hop(k,n)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Từ các chữ  số $\\{{ {set_A} \\}}$ có thể lập được bao nhiêu số tự nhiên gồm ${{{k}}}$ chữ số khác nhau?" \


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	t=f"{n-1}"
	so_cach=f"{n-1}"
	a_i=""
	a_i_chu=""
	for i in range(1,k+1):
		a_i=a_i +f"a_{i}"
		a_i_chu=a_i_chu +f"a_{i},"

		t=t + f".{n-i}"
		so_cach=so_cach + f",{n-i}"
	t=t[:-2]
	so_cach=so_cach[:-2]

	a_i_chu=a_i_chu[:-1]

	noi_dung_loigiai=f"Gọi $\\overline{{{a_i}}}$ là số cần lập.\n"\
		f"Mỗi chữ số ${{{a_i_chu}}}$ có số cách chọn lần lượt là: {so_cach}.\n"\
		f"Theo quy tắc nhân ta có số cách lập là: ${t}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B1_11]-M3. Chọn 2 quả cầu khác màu và tổng là chẵn hoặc lẻ.
def mcn__L10_C8_B1_11():  	
	m=random.randint(10,20)
	n=random.randint(12,25)
	if n==m:
		n=m+random.randint(2,4)
	mau_sac=["màu đỏ", "màu xanh", "màu vàng", "màu trắng", "màu tím", "màu đen"]
	random.shuffle(mau_sac)

	chon=random.choice(["chẵn", "lẻ"])
	sl_m_chan=dem_so_chan_den_m(m)
	sl_m_le=dem_so_le_den_m(m)

	sl_n_chan=dem_so_chan_den_m(n)
	sl_n_le=dem_so_le_den_m(n)
	if chon=="lẻ":
		t1=sl_m_chan*sl_n_le
		t2=sl_m_le*sl_n_chan

		noi_dung_loigiai=f"Để tổng của hai số là một số lẻ thì một số là số lẻ và số còn lại là số chẵn.\n"\
		f"Trường hợp 1: Chọn quả {mau_sac[0]} số chẵn và quả {mau_sac[1]} số lẻ có số cách là: ${sl_m_chan}.{sl_n_le}={t1}$\n"\
		f"Trường hợp 2: Chọn quả {mau_sac[0]} số lẻ và quả {mau_sac[1]} số chẵn có số cách là: ${sl_m_le}.{sl_n_chan}={t2}$\n"\
		f"Tổng số cách chọn là: ${t1} + {t2}={t1+t2}$.\n"
	else:
		t1=sl_m_chan*sl_n_chan
		t2=sl_m_le*sl_n_le
		kq=t1+t2

		noi_dung_loigiai=f"Để tổng của hai số là một số chẵn thì hai số phải cùng là số lẻ hoặc cùng là số chẵn.\n"\
		f"Trường hợp 1: Chọn quả {mau_sac[0]} số chẵn và quả {mau_sac[1]} số chẵn có số cách là: ${sl_m_chan}.{sl_n_chan}={t1}$\n"\
		f"Trường hợp 2: Chọn quả {mau_sac[0]} số lẻ và quả {mau_sac[1]} số chẵn có số cách là: ${sl_m_le}.{sl_n_le}={t2}$\n"\
		f"Tổng số cách chọn là: ${t1} + {t2}={t1+t2}$.\n"

	kq=t1+t2
	kq2=t1*t2
	kq3=(sl_m_chan+sl_n_le+sl_m_le+sl_n_chan)
	kq4=sl_m_chan*sl_n_le*sl_m_le*sl_n_chan

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một hộp chứa ${{{m}}}$ quả cầu {mau_sac[0]} được đánh số từ ${{1}}$ đến ${{{m}}}$ và ${{{n}}}$ quả cầu {mau_sac[1]} được đánh số từ ${{1}}$ đến ${{{n}}}$." \
			f"Chọn ngẫu nhiên ${{2}}$ quả cầu. Hỏi có bao nhiêu cách để chọn được hai quả cầu khác màu và tổng của các số trên hai quả cầu là một số {chon}?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an






#[D10_C8_B1_12]-TL-M2. Tính số ước nguyên của một số
def mcn__L10_C8_B1_12(): 
    a= random.choice([n for n in range(40, 1000) if len([i for i in range(2, n//2 + 1) if n % i == 0]) >= 2])
    b= sum(1 for i in range(1, abs(a) + 1) if a % i == 0)
    c= b*2
    noi_dung=f"Số ước của ${{{a}}}$ là "
    noi_dung_loigiai=f"Số ước của ${{{a}}}$ là ${{{c}}}$ "
    pa_A= f"*${{{c}}}$"

    dss=[ f"${{{c-1}}}$",
    f"${{{c+1}}}$",
    f"${{{c+5}}}$",
f"${{{c+3}}}$",
    f"${{{c+2}}}$",
f"${{{c-2}}}$",
    f"${{{c+4}}}$",
    ]
    pa_B, pa_C, pa_D= random.sample(dss, 3)  
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an






#[D10_C8_B1_13]-SA-M2. Tính số ước nguyên của một số
def mcn__L10_C8_B1_13(): 
	a= random.choice([n for n in range(40, 1000) if len([i for i in range(2, n//2 + 1) if n % i == 0]) >= 2])
	b= sum(1 for i in range(1, abs(a) + 1) if a % i == 0)
	c= b*2
	kq=str(c)
	noi_dung=f"Số ước của ${{{a}}}$ là"
	noi_dung_loigiai=f"Số ước của ${{{a}}}$ là ${{{c}}}$ "

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an







#[D10_C8_B1_14]-TF-M2. Chọn đề tài thi cử. Xét ĐS
def mcn__L10_C8_B1_14(): 
	detai=["con người", "thiên nhiên", "lịch sử", "địa lí", "văn hoá xã hội", "ẩm thực", "khoa bảng"]
	A,B,C,D =random.sample(detai,4)
	a,b,c,d=random.sample(range(3,10),4)


	noi_dung = f"Trong một cuộc thi tìm hiểu về đất nước Việt Nam, ban tổ chức công bố danh sách các đề tài bao gồm: ${{{a}}}$ đề tài về {A}, ${{{b}}}$ đề tài về {B}, ${{{c}}}$ đề tài về {C} và ${{{d}}}$ đề tài về {D}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a}}}$ cách để chọn được một câu hỏi thuộc đề tài về {A}" 
	kq1_F=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{b}}}$ cách để chọn được một câu hỏi thuộc đề tài về {A} "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a}}}$ cách để chon được một câu hỏi thuộc đề tài về {A} "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Nếu mỗi thí sinh phải chọn ${{2}}$ câu hỏi thuộc các đề tài trên thì có ${{{a*b}}}$ cách để chọn được 1 đề tài về {A} và 1 đề tài về {B} "
	kq2_F=f"Nếu mỗi thí sinh phải chọn ${{2}}$ câu hỏi thuộc các đề tài trên thì có ${{{a*b+1}}}$ cách để chọn được 1 đề tài về {A} và 1 đề tài về {B} "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Nếu mỗi thứ sinh phải chọn ${{2}}$ câu hỏi thuộc các đề tài trên thì có ${{{a} \\cdot {b} = {a*b}}}$ cách để chọn được 1 đề tài về {A} và 1 đề tài về {B}"
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"*Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b+c+d}}}$ cách chọn" 
	kq3_F=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b+c+d+1}}}$ cách chọn "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b+c+d}}}$ cách chọn"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"*Nếu mỗi thí sinh phải chọn 4 câu hỏi thuộc đủ các đề tài thì có ${{{a*b*c*d}}}$ cách chọn "
	kq4_F=f"Nếu mỗi thí sinh phải chọn 4 câu hỏi thuộc đủ các đề tài thì có ${{{a*b*c*d+1}}}$ cách chọn " 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Nếu mỗi thí sinh phải chọn 4 câu hỏi thuộc đủ các đề tài thì có ${{{a}\\cdot {b} \\cdot {c} \\cdot {d} ={a*b*c*d}}}$ cách chọn "
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an










#[D10_C8_B1_15]-TF-M3. Chọn đề tài thi cử. Xét ĐS
def mcn__L10_C8_B1_15(): 
	detai=["con người", "thiên nhiên", "lịch sử", "địa lí", "văn hoá xã hội", "ẩm thực", "khoa bảng"]
	A,B,C,D =random.sample(detai,4)
	a,b,c,d=random.sample(range(3,10),4)


	noi_dung = f"Trong một cuộc thi tìm hiểu về đất nước Việt Nam, ban tổ chức công bố danh sách các đề tài bao gồm: ${{{a}}}$ đề tài về {A}, ${{{b}}}$ đề tài về {B}, ${{{c}}}$ đề tài về {C} và ${{{d}}}$ đề tài về {D}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b+c+d}}}$ cách chọn" 
	kq1_F=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b+c+d+1}}}$ cách chọn "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a}+{b}+{c}+{d}={a+b+c+d}}}$ cách chọn "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"*Nếu mỗi thí sinh phải chọn ${{3}}$ câu hỏi thuộc ba đề tài khác nhau thì có ${{{a*b*c+a*b*d+b*d*c+a*c*d}}}$ cách chọn "
	kq4_F=f"Nếu mỗi thí sinh phải chọn ${{3}}$ câu hỏi thuộc ba đề tài khác nhau thì có ${{{a*b*c+a*b*d+b*d*c+a*c*d+1}}}$ cách chọn  "
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"TH1: chọn được ${{1}}$ đề tài về {A} và ${{1}}$ đề tài về {B} và ${{1}}$ đề tài {C} có ${{{a} \\cdot {b} \\cdot{c} ={a*b*c}}}$ cách chọn \n\n"
f"TH2: chọn được ${{1}}$ đề tài về {A} và ${{1}}$ đề tài về {B} và ${{1}}$ đề tài {D} có ${{{a} \\cdot {b} \\cdot{d} ={a*b*d}}}$ cách chọn \n\n"
f"TH3: chọn được ${{1}}$ đề tài về {B} và ${{1}}$ đề tài về {D} và ${{1}}$ đề tài {C} có ${{{b} \\cdot {d} \\cdot{c} ={b*d*c}}}$ cách chọn \n\n"
f"TH4: chọn được ${{1}}$ đề tài về {A} và ${{1}}$ đề tài về {C} và ${{1}}$ đề tài {D} có ${{{a} \\cdot {c} \\cdot{d} ={a*c*d}}}$ cách chọn \n\n"
f"Vậy chọn ${{3}}$ câu hỏi thuộc ba đề tài khác nhau thì có ${{{a*b*c+a*b*d+b*d*c+a*c*d}}}$ cách chọn "
)
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"*Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b}}}$ cách chọn đề tài về {A} hoặc đề tài về {B}" 
	kq3_F=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b+1}}}$ cách chọn đề tài về {A} hoặc đề tài về {B} "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Nếu mỗi thí sinh chọn ${{1}}$ câu hỏi thuộc các đề tài trên thì có ${{{a+b+c+d}}}$ cách chọn đề tài về {A} hoặc đề tài về {B}"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Nếu mỗi thí sinh phải chọn ${{4}}$ câu hỏi thuộc đủ các đề tài thì có ${{{a*b*c*d}}}$ cách chọn "
	kq2_F=f"Nếu mỗi thí sinh phải chọn ${{4}}$ câu hỏi thuộc đủ các đề tài thì có ${{{a*b*c*d+1}}}$ cách chọn " 
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Nếu mỗi thí sinh phải chọn ${{4}}$ câu hỏi thuộc đủ các đề tài thì có ${{{a}\\cdot {b} \\cdot {c} \\cdot {d} ={a*b*c*d}}}$ cách chọn "
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an






#[D10_C8_B1_16]-TF-M3. Các bài toán về tạo số.(nhiều kiểu)
def mcn__L10_C8_B1_16(): 
	m=random.choice([i for i in range(-20,20) if i!=0])
	q=random.randint(1,2)
	if q==1:

		noi_dung = f"Cho các chữ số ${{0;1;2;3;4;5;6;7;8;9}}$ . Xét tính đúng-sai của các khẳng định sau. "		
		debai_word= f"{noi_dung}\n"
		chon =random.randint(1,3)
		if chon ==1:
			kq1_T=f"*Có ${{{phan_so(9*10*10*10)}}}$ số tự nhiên có ${{4}}$ chữ số được tạo thành từ các chữ số trên" 
			kq1_F=f" Có ${{{phan_so(9*10*10*10+m)}}}$ số tự nhiên có ${{4}}$ chữ số được tạo thành từ các chữ số trên"
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f"Có ${{{phan_so(9*10*10*10)}}}$ số tự nhiên có ${{4}}$ chữ số được tạo thành từ các chữ số trên "
			loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq1==kq1_F:
				loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		if chon ==2: 
			kq1_T=f"*Có ${{{phan_so(9*10*10)}}}$ số tự nhiên có ${{3}}$ chữ số được tạo thành từ các chữ số trên" 
			kq1_F=f" Có ${{{phan_so(9*10*10+m)}}}$ số tự nhiên có ${{3}}$ chữ số được tạo thành từ các chữ số trên"
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f"Có ${{{phan_so(9*10*10)}}}$ số tự nhiên có ${{3}}$ chữ số được tạo thành từ các chữ số trên "
			loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq1==kq1_F:
				loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==3: 
			kq1_T=f"*Có ${{{phan_so(9*10*10*10*10)}}}$ số tự nhiên có ${{5}}$ chữ số được tạo thành từ các chữ số trên" 
			kq1_F=f" Có ${{{phan_so(9*10*10*10*10+m)}}}$ số tự nhiên có ${{5}}$ chữ số được tạo thành từ các chữ số trên"
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f"Có ${{{phan_so(9*10*10*10*10)}}}$ số tự nhiên có ${{5}}$ chữ số được tạo thành từ các chữ số trên "
			loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq1==kq1_F:
				loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		chon =random.randint(1,3)
		if chon ==1:

			kq2_T=f"*Có ${{{phan_so(9*9*8*7)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			kq2_F=f"Có ${{{phan_so(9*9*8*7+m)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau được tạo thành từ các chữ số trên  "
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f"Có ${{{phan_so(9*9*8*7)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq2==kq2_F:
				loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==2: 
			kq2_T=f"*Có ${{{phan_so(9*9*8)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			kq2_F=f"Có ${{{phan_so(9*9*8+m)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau được tạo thành từ các chữ số trên  "
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f"Có ${{{phan_so(9*9*8)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq2==kq2_F:
				loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon ==3:

			kq2_T=f"*Có ${{{phan_so(9*9*8*7*6)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			kq2_F=f"Có ${{{phan_so(9*9*8*7*6+m)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau được tạo thành từ các chữ số trên  "
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f"Có ${{{phan_so(9*9*8*7*6)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq2==kq2_F:
				loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		chon =random.randint(1,3)
		if chon ==1:


			kq3_T=f"*Có ${{{phan_so(9*10*10*5)}}}$ số tự nhiên có ${{4}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên  " 
			kq3_F=f"Có ${{{phan_so(9*10*10*5+m)}}}$ số tự nhiên có ${{4}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"Có ${{{phan_so(9*10*10*5)}}}$ số tự nhiên có ${{4}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		if chon ==2:
			kq3_T=f"*Có ${{{phan_so(9*10*5)}}}$ số tự nhiên có ${{3}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên  " 
			kq3_F=f"Có ${{{phan_so(9*10*5+m)}}}$ số tự nhiên có ${{3}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"Có ${{{phan_so(9*10*5)}}}$ số tự nhiên có ${{3}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		if chon ==3:


			kq3_T=f"*Có ${{{phan_so(9*10*10*10*5)}}}$ số tự nhiên có ${{5}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên  " 
			kq3_F=f"Có ${{{phan_so(9*10*10*10*5+m)}}}$ số tự nhiên có ${{5}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"Có ${{{phan_so(9*10*10*10*5)}}}$ số tự nhiên có ${{5}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		chon =random.randint(1,3)
		if chon ==1:
			kq4_T=f"*Có ${{{phan_so(9*8*7+4*8*8*7)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  "
			kq4_F=f"Có ${{{phan_so(9*8*7+4*8*8*7+m)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Có ${{{phan_so(9*8*7+4*8*8*7)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==2:


			kq4_T=f"*Có ${{{phan_so(9*8+4*8*8)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  "
			kq4_F=f"Có ${{{phan_so(9*8+4*8*8+m)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Có ${{{phan_so(9*8+4*8*8)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==3:
			kq4_T=f"*Có ${{{phan_so(9*8*7*6+4*8*8*7*6)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  "
			kq4_F=f"Có ${{{phan_so(9*8*7*6+4*8*8*7*6+m)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Có ${{{phan_so(9*8*7*6+4*8*8*7*6)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	if q==2:
		m=random.randint(1,8)
		if m==1:
			noi_dung = f"Cho các chữ số ${{0;1;2;3;4;5;6;7}}$. Xét tính đúng-sai của các khẳng định sau. "	

		if m==2:
			noi_dung = f"Cho các chữ số ${{0;1;2;3;4;5;6;9}}$. Xét tính đúng-sai của các khẳng định sau. "		


		if m==3:
			noi_dung = f"Cho các chữ số ${{0;1;2;3;4;7;6;9}}$. Xét tính đúng-sai của các khẳng định sau. "	

		if m==4:
			noi_dung = f"Cho các chữ số ${{0;3;2;5;4;7;6;9}}$. Xét tính đúng-sai của các khẳng định sau. "	

		if m==5:
			noi_dung = f"Cho các chữ số ${{0;1;2;3;4;5;8;9}}$. Xét tính đúng-sai của các khẳng định sau. "	

		if m==6:
			noi_dung = f"Cho các chữ số ${{0;1;2;3;6;5;8;9}}$. Xét tính đúng-sai của các khẳng định sau. "	


		if m==7:
			noi_dung = f"Cho các chữ số ${{0;1;4;3;8;5;6;7}}$. Xét tính đúng-sai của các khẳng định sau. "	

		if m==8:
			noi_dung = f"Cho các chữ số ${{0;1;2;3;4;7;8;9}}$. Xét tính đúng-sai của các khẳng định sau. "	

		debai_word= f"{noi_dung}\n"
		chon =random.randint(1,3)
		if chon ==1:
			kq1_T=f"*Có ${{{phan_so(7*8*8*8)}}}$ số tự nhiên có ${{4}}$ chữ số được tạo thành từ các chữ số trên" 
			kq1_F=f" Có ${{{phan_so(7*8*8*8+m)}}}$ số tự nhiên có ${{4}}$ chữ số được tạo thành từ các chữ số trên"
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f"Có ${{{phan_so(7*8*8*8)}}}$ số tự nhiên có ${{4}}$ chữ số được tạo thành từ các chữ số trên "
			loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq1==kq1_F:
				loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		if chon ==2: 
			kq1_T=f"*Có ${{{phan_so(7*8*8)}}}$ số tự nhiên có ${{3}}$ chữ số được tạo thành từ các chữ số trên" 
			kq1_F=f" Có ${{{phan_so(7*8*8+m)}}}$ số tự nhiên có ${{3}}$ chữ số được tạo thành từ các chữ số trên"
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f"Có ${{{phan_so(7*8*8)}}}$ số tự nhiên có ${{3}}$ chữ số được tạo thành từ các chữ số trên "
			loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq1==kq1_F:
				loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==3: 
			kq1_T=f"*Có ${{{phan_so(7*8*8*8*8)}}}$ số tự nhiên có ${{5}}$ chữ số được tạo thành từ các chữ số trên" 
			kq1_F=f" Có ${{{phan_so(7*8*8*8*8+m)}}}$ số tự nhiên có ${{5}}$ chữ số được tạo thành từ các chữ số trên"
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f"Có ${{{phan_so(7*8*8*8*8)}}}$ số tự nhiên có ${{5}}$ chữ số được tạo thành từ các chữ số trên "
			loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq1==kq1_F:
				loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		chon =random.randint(1,3)
		if chon ==1:

			kq2_T=f"*Có ${{{phan_so(7*7*6*5)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			kq2_F=f"Có ${{{phan_so(7*7*6*5+m)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau được tạo thành từ các chữ số trên  "
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f"Có ${{{phan_so(7*7*6*5)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq2==kq2_F:
				loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==2: 
			kq2_T=f"*Có ${{{phan_so(7*7*6)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			kq2_F=f"Có ${{{phan_so(7*7*6+m)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau được tạo thành từ các chữ số trên  "
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f"Có ${{{phan_so(7*7*6)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq2==kq2_F:
				loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon ==3:

			kq2_T=f"*Có ${{{phan_so(7*7*6*5)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			kq2_F=f"Có ${{{phan_so(7*7*6*5+m)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau được tạo thành từ các chữ số trên  "
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f"Có ${{{phan_so(7*7*6*5)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau được tạo thành từ các chữ số trên "
			loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq2==kq2_F:
				loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		chon =random.randint(1,3)
		if chon ==1:

			kq3_T=f"*Có ${{{phan_so(7*8*8*4)}}}$ số tự nhiên có ${{4}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên  " 
			kq3_F=f"Có ${{{phan_so(7*8*8*4+m)}}}$ số tự nhiên có ${{4}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"Có ${{{phan_so(7*8*8*4)}}}$ số tự nhiên có ${{4}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		if chon ==2:
			kq3_T=f"*Có ${{{phan_so(7*8*4)}}}$ số tự nhiên có ${{3}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên  " 
			kq3_F=f"Có ${{{phan_so(7*8*4+m)}}}$ số tự nhiên có ${{3}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"Có ${{{phan_so(7*8*4)}}}$ số tự nhiên có ${{3}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


		if chon ==3:


			kq3_T=f"*Có ${{{phan_so(7*8*8*8*4)}}}$ số tự nhiên có ${{5}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên  " 
			kq3_F=f"Có ${{{phan_so(7*8*8*8*4+m)}}}$ số tự nhiên có ${{5}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"Có ${{{phan_so(7*8*8*8*5)}}}$ số tự nhiên có ${{5}}$ chữ số và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		chon =random.randint(1,3)
		if chon ==1:
			kq4_T=f"*Có ${{{phan_so(7*7*6+3*6*6*5)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  "
			kq4_F=f"Có ${{{phan_so(7*7*6+3*6*6*5+m)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Có ${{{phan_so(7*7*6+3*6*6*5)}}}$ số tự nhiên có ${{4}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==2:


			kq4_T=f"*Có ${{{phan_so(7*6+3*6*6)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  "
			kq4_F=f"Có ${{{phan_so(7*6+3*6*6+m)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Có ${{{phan_so(7*6+3*6*6)}}}$ số tự nhiên có ${{3}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon ==3:
			kq4_T=f"*Có ${{{phan_so(7*6*5*4+3*6*6*5*4)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  "
			kq4_F=f"Có ${{{phan_so(7*6*5*4+3*6*6*5*4+m)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên  " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Có ${{{phan_so(7*6*5*4+3*6*6*5*4)}}}$ số tự nhiên có ${{5}}$ chữ số khác nhau và là số chẵn được tạo thành từ các chữ số trên "
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an




#[D10_C8_B1_17]-TF-M3. Các bài toán về xếp người thành hàng(nhiều kiểu)
def mcn__L10_C8_B1_17(): 
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	m=random.randint(4,6)
	n=m
	a=random.choice([i for i in range(-10,10) if i!=0])
	vt=random.choice(["cuối", "đầu", "vị trí thứ hai", "vị trí thứ ba", "vị trí thứ tư", "vị trí thứ năm"])
	noi_dung = f"Có ${{{m}}}$ bạn nam và ${{{n}}}$ nữ trong đó có bạn nam tên {B} và bạn nữ tên {A}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"

	kq1_T=f"*Có ${{{factorial(m+n)}}}$ cách xếp các bạn thành một hàng dọc" 
	kq1_F=f"Có ${{{factorial(m+n)+a}}}$ cách xếp các bạn thành một hàng dọc "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Có ${{{factorial(m+n)}}}$ cách xếp các bạn thành một hàng dọc "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon =random.randint(1,2)
	if chon ==1:

		kq2_T=f"*Có ${{{2*factorial(m)*factorial(m)}}}$ cách xếp các bạn nam nữ xen kẽ thành một hàng dọc "
		kq2_F=f"Có ${{{2*factorial(m)*factorial(m)+a}}}$ cách xếp các bạn nam nữ xen kẽ thành một hàng dọc "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Có ${{{2*factorial(m)*factorial(m)}}}$ cách xếp các bạn nam nữ xen kẽ thành một hàng dọc"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon ==2:
		gt=random.choice(["nam", "nữ"])

		kq2_T=f"*Có ${{{m*factorial(m+n-1)}}}$ cách xếp để một bạn {gt} luôn đứng đầu hàng "
		kq2_F=f"Có ${{{m*factorial(m+n-1)+a}}}$ cách xếp để một bạn {gt} luôn đứng đầu hàng "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Có ${{{m*factorial(m+n-1)}}}$ cách xếp để một bạn {gt} luôn đứng đầu hàng"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	chon =random.randint(1,2)
	if chon ==1:
		vt=["cuối", "đầu", "vị trí thứ hai", "vị trí thứ ba", "vị trí thứ tư", "vị trí thứ năm"]
		đầu, cuối =random.sample(vt,2)

		kq3_T=f"* Có ${{{factorial(m+n-2)}}}$ cách xếp các bạn thành một hàng dọc sao cho {A} đứng {đầu} hàng còn {B} đứng {cuối} hàng" 
		kq3_F=f"Có ${{{factorial(m+n-2)}}}$ cách xếp các bạn thành một hàng dọc sao cho {A} đứng {đầu} hàng còn {B} đứng {cuối} hàng "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Có ${{{factorial(m+n-2)}}}$ cách xếp các bạn thành một hàng dọc sao cho {A} đứng đầu hàng còn {B} đứng cuối hàng"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon ==2:
		

		kq3_T=f"* Có ${{{factorial(m+n-2)}}}$ cách xếp các bạn thành một hàng dọc sao cho {A} hoặc {B} đứng {vt} của hàng" 
		kq3_F=f"Có ${{{factorial(m+n-2)}}}$ cách xếp các bạn thành một hàng dọc sao cho {A} hoặc {B} đứng {vt} của hàng "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Có ${{{factorial(m+n-2)}}}$ cách xếp các bạn thành một hàng dọc sao cho {A} hoặc {B} đứng {vt} của hàng"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	chon=random.randint(1,2)
	if chon ==1:

		kq4_T=f"*Có ${{{factorial(m+1)*factorial(m)}}}$ cách xếp các bạn nam luôn đứng cạnh nhau "
		kq4_F=f"Có ${{{factorial(m+1)*factorial(m)+a}}}$ cách xếp các bạn nam luôn đứng cạnh nhau " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Coi các bạn nam là 1 cùng với ${{{m}}}$ bạn nữ thì có ${{{factorial(m+1)}}}$ cách xếp \n\n"
		f" Trong nhóm các bạn nam thì có ${{{factorial(m)}}}$ cách xếp \n\n"
		f" Theo quy tắc nhân có ${{{factorial(m+1)*factorial(m)}}}$ cách xếp các bạn nam luôn đứng cạnh nhau ")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon ==2:

		kq4_T=f"*Có ${{{factorial(m+m-1)*factorial(2)}}}$ cách xếp hai bạn {B} và {A} luôn đứng cạnh nhau "
		kq4_F=f"Có ${{{factorial(m+m-1)*factorial(2)+a}}}$ cách xếp hai bạn {B} và {A} luôn đứng cạnh nhau " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Coi hai bạn {B} và {A} là 1 cùng với ${{{m+m-2}}}$ bạn còn lại thì có ${{{factorial(m+m-1)}}}$ cách xếp \n\n"
		f" Trong nhóm hai bạn {B} và {A} thì có ${{{factorial(2)}}}$ cách xếp \n\n"
		f" Theo quy tắc nhân có ${{{factorial(m+m-1)*factorial(2)}}}$ cách xếp chai bạn {B} và {A} luôn đứng cạnh nhau ")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an





#[D10_C8_B1_18]-TF-M3. Các bài toán về xếp 3 nhóm đồ vật
def mcn__L10_C8_B1_18(): 
	a=random.choice([i for i in range(-10,10) if i!=0])
	m=random.randint(2,3)
	n=random.randint(1,3)
	p=random.randint(2,4)
	ds=["Toán học", "Văn học", "Hoá học", "Ngoại ngữ", "Địa lí", "Lịch sử", "Tin học", "Âm nhạc", "Mĩ thuật", "Sinh học", "Giáo dục công dân"]
	A,B,C=random.sample(ds, 3)
	noi_dung = f"Một giá có ${{{m}}}$ quyển sách {A} khác nhau có ${{{n}}}$ quyển sách {B} khác nhau và ${{{p}}}$ quyển sách {C} khác nhau. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Có ${{{factorial(m+n+p)}}}$ cách sắp xếp các quyển sách thành một chồng" 
	kq1_F=f"Có ${{{factorial(m+n+p)+a}}}$ cách sắp xếp các quyển sách thành một chồng"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Có ${{{factorial(m+n+p)}}}$ cách sắp xếp các quyển sách thành một chồng"
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	kq2_T=f"* Có ${{{factorial(m)*factorial(n+p)}}}$ cách sắp xếp các quyển sách {A} luôn trên cùng"
	kq2_F=f"Có ${{{factorial(m)*factorial(n+p)+a}}}$ cách sắp xếp các quyển sách {A} luôn trên cùng "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Xếp các quyển sách {A} thì có ${{{factorial(m)}}}$ cách \n\n"
	f" Xếp các quyển còn lại có ${{{factorial(n+p)}}}$ cách \n\n"
	f" Theo quy tắc nhân có ${{{factorial(m)*factorial(n+p)}}}$ cách sắp xếp các quyển sách {A} luôn trên cùng "
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	kq3_T=f"*Có ${{{(m+n)*(m+n-1)*factorial(m+n+p-2)}}}$ cách xếp để quyển trên cùng và dưới cùng không phải sách {C} " 
	kq3_F=f"Có ${{{(m+n)*(m+n-1)*factorial(m+n+p-2)+a}}}$ cách xếp để quyển trên cùng và dưới cùng không phải sách {C} "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Có ${{{(m+n)*(m+n-1)*factorial(m+n+p-2)}}}$ cách xếp để quyển trên cùng và dưới cùng không phải sách {C}"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	kq4_T=f"*Có ${{{n*(n-1)*factorial(m+n+p-2)}}}$ cách xếp để quyển trên cùng và dưới cùng là sách {C}  "
	kq4_T=f"*Có ${{{n*(n-1)*factorial(m+n+p-2)+a}}}$ cách xếp để quyển trên cùng và dưới cùng là sách {C} "
	kq4_F=f"Có ${{{n*(n-1)*factorial(m+n+p-2)}}}$ cách xếp để quyển trên cùng và dưới cùng là sách {C} " 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Có ${{{n*(n-1)*factorial(m+n+p-2)}}}$ cách xếp để quyển trên cùng và dưới cùng là sách {C}"
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an





#[D10_C8_B1_19]-TF-M3. Các bài toán về chọn vật từ ba nhóm đối tượng
def mcn__L10_C8_B1_19(): 
	m=random.randint(6,20)
	n=random.randint(5,30)
	p=random.randint(5,20)
	A=random.choice(["viên bi", "quả cầu"])
	a=random.choice([i for i in range(-3,3) if i!=0])
	mau=["xanh", "đỏ", "tím", "vàng", "trắng", "đen"]
	e,u,k=random.sample(mau,3)

	noi_dung = f"Một hộp có ${{{m}}}$ {A} {e}, ${{{n}}}$ {A} {u} và ${{{p}}}$ {A} {k}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Có ${{{m+n+p}}}$ cách để chọn ra một {A}" 
	kq1_F=f"Có ${{{m+n+p+a}}}$ cách để chọn ra một {A} "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Có ${{{m}+{n}+{p}={m+n+p}}}$ cách để chọn ra một {A} "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Có ${{{m*n}}}$ cách để chọn ra hai {A} trong đó có một quả màu {e} và một quả màu {u} "
	kq2_F=f"Có ${{{m*n+a}}}$ cách để chọn ra hai {A} trong đó có một quả màu {e} và một quả màu {u} "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Có ${{{m} \\cdot {n}={m*n}}}$ cách để chọn ra hai {A} trong đó có một quả màu {e} và một quả màu {u}"
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* Có ${{{m*n*p}}}$ cách để chọn ra ba {A} đủ các màu" 
	kq3_F=f"Có ${{{m*n*p+a}}}$ cách để chọn ra ba {A} đủ các màu "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Có ${{{m} \\cdot {n} \\cdot {p} = {m*n*p}}}$ cách để chọn ra ba {A} đủ các màu"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"*Có ${{{m*n+n*p+p*m}}}$ cách để chọn ra hai {A} khác màu "
	kq4_F=f"Có ${{{m*n+n*p+p*m+a}}}$ cách để chọn ra hai {A} khác màu  " 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Có ${{{m} \\cdot {n} + {m} \\cdot {p}+{p} \\cdot {n}=   {m*n+n*p+p*m}}}$ cách để chọn ra hai {A} khác màu "
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an







#[D10_C8_B1_20]-SA-M2. Tính số cái bắt tay
def mcn__L10_C8_B1_20(): 
	a= random.randint(8,110)
	kq=str(phan_so(a*(a-1)))
	noi_dung=f"Tại một bữa tiệc có ${{{a}}}$ cặp vợ chồng, các ông chồng lần lượt đi bắt tay với các bà vợ, hỏi có bao nhiêu cái bắt tay biết rằng họ không bắt tay với vợ của mình."
	noi_dung_loigiai=f"Số cái bắt tay là ${{{a} \\cdot {a-1}}}$ là ${{{phan_so(a*(a-1))}}}$ "

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an






#[D10_C8_B1_21]-SA-M2. Tính số cách lấy ra 3 vật khác nhóm từ 3 nhóm
def mcn__L10_C8_B1_21(): 
	m=random.randint(6,20)
	n=random.randint(5,20)
	p=random.randint(5,20)
	A=random.choice(["viên bi", "quả cầu"])
	a=random.choice([i for i in range(-3,3) if i!=0])
	mau=["xanh", "đỏ", "tím", "vàng", "trắng", "đen"]
	e,u,k=random.sample(mau,3)
	kq=phan_so(m*n*p)

	noi_dung = f"Một hộp có ${{{m}}}$ {A} {e}, ${{{n}}}$ {A} {u} và ${{{p}}}$ {A} {k}. Có bao nhiêu cách lấy ra ba {A} khác màu.  "		

	noi_dung_loigiai=f"Số cách lấy ba {A} khác mầu là ${{{m} \\cdot {n} \\cdot {p }= {phan_so(m*n*p)}}}$ "

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an


#[D10_C8_B1_22]-SA-M3. Tính số cách lấy ra 2 vật khác nhóm từ 3 nhóm
def mcn__L10_C8_B1_22(): 
	m=random.randint(6,20)
	n=random.randint(5,20)
	p=random.randint(5,20)
	A=random.choice(["viên bi", "quả cầu"])
	a=random.choice([i for i in range(-3,3) if i!=0])
	mau=["xanh", "đỏ", "tím", "vàng", "trắng", "đen"]
	e,u,k=random.sample(mau,3)
	kq=m*n+n*p+m*p

	noi_dung = f"Một hộp có ${{{m}}}$ {A} {e}, ${{{n}}}$ {A} {u} và ${{{p}}}$ {A} {k}. Có bao nhiêu cách lấy ra hai {A} khác màu.  "		

	noi_dung_loigiai=f"Số cách lấy hai {A} khác màu là ${{{m} \\cdot {n}+ {n} \\cdot {p } +{m} \\cdot {p} = {m*n+n*p+m*p}}}$."

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C8_B1_23]-SA-M3. Tính số cách lấy ra 3 đ.tuong khác nhóm từ 4 nhóm
def mcn__L10_C8_B1_23(): 

	detai=["con người", "thiên nhiên", "lịch sử", "địa lí", "văn hoá xã hội", "ẩm thực", "khoa bảng"]
	A,B,C,D =random.sample(detai,4)
	a,b,c,d=random.sample(range(3,10),4)
	kq=phan_so(a*b*c+a*b*d+b*d*c+a*d*c)

	noi_dung = (f"Trong một cuộc thi tìm hiểu về đất nước Việt Nam, ban tổ chức công bố danh sách các đề tài bao gồm: ${{{a}}}$ đề tài về {A}, ${{{b}}}$ đề tài về {B}, ${{{c}}}$ đề tài về {C} và ${{{d}}}$ đề tài về {D}. "
	f" Mỗi thi sinh được lựa chọn ra ba đề tài thuộc ba mảng khác nhau. Hỏi mỗi thi sinh có bao nhiêu cách lựa chọn. "	)	
	noi_dung_loigiai=f"Số cách chọn đề tài là ${{{a} \\cdot {b} \\cdot {d}+ {a} \\cdot {b } \\cdot {d} +{b} \\cdot {c} \\cdot {d} +{a} \\cdot {d} \\cdot {c}= {phan_so(a*b*c+a*b*d+b*d*c+a*d*c)}}}$ "

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C8_B1_24]-SA-M3. B.toán tạo số chẵn có các chữ số khác nhau (ds có chứa cso 0)
def mcn__L10_C8_B1_24(): 
	le=[1,3,5,7,9]
	
	chan=[2,4,6,8]

	chon =random.randint(1,6)
	if chon ==1:
		a1,b1,c1=random.sample(chan,3)
		a,b,c,d=random.sample(le,4)
		kq=phan_so(7*6*5+3*6*6*5)
		noi_dung=f" Từ các chữ số ${{0;{a};{a1};{b};{b1};{c};{c1};{d}}}$ tạo được bao nhiêu số tự nhiên có bốn chữ số đôi một khác nhau và là số chẵn."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abcd}}$ $(a \\ne 0; a \\ne b \\ne c\\ne d)$ \n\n"
		f" TH1: ${{d=0}}$ \n\n a có ${{7}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n Theo quy tắc nhân có ${{7 \\cdot 6 \\cdot 5 ={phan_so(7*6*5)}}}$ số \n\n"
		f" TH2: ${{d \\ne 0}}$ \n\n d có ${{3}}$ cách chọn \n\n a có ${{6}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n Theo quy tắc nhân có ${{3 \\cdot 6 \\cdot 6 \\cdot 5 ={phan_so(3*6*6*5)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(7*6*5)} + {phan_so(3*6*6*5)}= {phan_so(7*6*5+3*6*6*5)} }}$ số ")
	if chon ==2:
		a1,b1,c1=random.sample(chan,3)
		a,b,c=random.sample(le,3)
		kq=phan_so(4*6*5+3*5*4*5)
		noi_dung=f" Từ các chữ số ${{0;{a};{a1};{b};{b1};{c};{c1}}}$ tạo được bao nhiêu số tự nhiên có bốn chữ số đôi một khác nhau và là số chẵn."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abcd}}$ $(a \\ne 0; a \\ne b \\ne c\\ne d)$ \n\n"
		f" TH1: ${{d=0}}$ \n\n a có ${{6}}$ cách chọn \n\n b có ${{5}}$ cách chọn \n\n c có ${{4}}$ cách chọn \n\n Theo quy tắc nhân có ${{6 \\cdot 5 \\cdot 4 ={phan_so(4*6*5)}}}$ số \n\n"
		f" TH2: ${{d \\ne 0}}$ \n\n d có ${{3}}$ cách chọn \n\n a có ${{5}}$ cách chọn \n\n b có ${{5}}$ cách chọn \n\n c có ${{4}}$ cách chọn \n\n Theo quy tắc nhân có ${{3 \\cdot 5 \\cdot 5 \\cdot 4 ={phan_so(3*5*5*4)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(4*6*5)} + {phan_so(3*5*5*4)}= {phan_so(4*6*5+3*5*4*5)} }}$ số ")


	if chon ==3:
		a1,b1,c1=random.sample(chan,3)
		a,b,c,d=random.sample(le,4)
		kq=phan_so(7*6+3*6*6)
		noi_dung=f" Từ các chữ số ${{0;{a};{a1};{b};{b1};{c};{c1};{d}}}$ tạo được bao nhiêu số tự nhiên có ba chữ số đôi một khác nhau và là số chẵn."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abc}}$ $(a \\ne 0; a \\ne b \\ne c)$ \n\n"
		f" TH1: ${{c=0}}$ \n\n a có ${{7}}$ cách chọn \n\n b có ${{6}}$ cách chọn  \n\n Theo quy tắc nhân có ${{7 \\cdot 6={phan_so(7*6)}}}$ số \n\n"
		f" TH2: ${{c \\ne 0}}$ \n\n c có ${{3}}$ cách chọn \n\n a có ${{6}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n Theo quy tắc nhân có ${{3 \\cdot 6 \\cdot 6 ={phan_so(3*6*6)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(7*6)} + {phan_so(3*6*6)}= {phan_so(7*6+3*6*6)} }}$ số ")
	if chon ==4:
		a1,b1,c1=random.sample(chan,3)
		a,b,c=random.sample(le,3)
		kq=phan_so(6*5+3*5*5)
		noi_dung=f" Từ các chữ số ${{0;{a};{a1};{b};{b1};{c};{c1}}}$ tạo được bao nhiêu số tự nhiên có ba chữ số đôi một khác nhau và là số chẵn."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abc}}$ $(a \\ne 0; a \\ne b \\ne c)$ \n\n"
		f" TH1: ${{c=0}}$ \n\n a có ${{6}}$ cách chọn \n\n b có ${{5}}$ cách chọn \n\n Theo quy tắc nhân có ${{6 \\cdot 5 ={phan_so(6*5)}}}$ số \n\n"
		f" TH2: ${{c \\ne 0}}$ \n\n c có ${{3}}$ cách chọn \n\n a có ${{5}}$ cách chọn \n\n b có ${{5}}$ cách chọn \n\n Theo quy tắc nhân có ${{3 \\cdot 5 \\cdot 5  ={phan_so(3*5*5)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(6*5)} + {phan_so(3*5*5)}= {phan_so(6*5+3*5*5)} }}$ số ")



	if chon ==5:
		a1,b1,c1, d1=random.sample(chan,4)
		a,b,c,d=random.sample(le,4)
		kq=phan_so(7*8+4*7*7)
		noi_dung=f" Từ các chữ số ${{0;{a};{a1};{b};{b1};{c};{c1};{d}; {d1}}}$ tạo được bao nhiêu số tự nhiên có ba chữ số đôi một khác nhau và là số chẵn."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abc}}$ $(a \\ne 0; a \\ne b \\ne c)$ \n\n"
		f" TH1: ${{c=0}}$ \n\n a có ${{8}}$ cách chọn \n\n b có ${{7}}$ cách chọn  \n\n Theo quy tắc nhân có ${{8 \\cdot 7={phan_so(7*8)}}}$ số \n\n"
		f" TH2: ${{c \\ne 0}}$ \n\n c có ${{4}}$ cách chọn \n\n a có ${{7}}$ cách chọn \n\n b có ${{7}}$ cách chọn \n\n Theo quy tắc nhân có ${{4 \\cdot 7 \\cdot 7 ={phan_so(4*7*7)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(7*8)} + {phan_so(4*7*7)}= {phan_so(7*8+4*7*7)} }}$ số ")
	if chon ==6:
		a1,b1,c1, d1=random.sample(chan,4)
		a,b,c,d=random.sample(le,4)
		kq=phan_so(6*5+3*5*5)
		noi_dung=f" Từ các chữ số ${{0;{a};{a1};{b};{b1};{c};{c1}; {d}}}$ tạo được bao nhiêu số tự nhiên có ba chữ số đôi một khác nhau và là số chẵn."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abc}}$ $(a \\ne 0; a \\ne b \\ne c)$ \n\n"
		f" TH1: ${{c=0}}$ \n\n a có ${{7}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n Theo quy tắc nhân có ${{7 \\cdot 6 ={phan_so(6*7)}}}$ số \n\n"
		f" TH2: ${{c \\ne 0}}$ \n\n c có ${{4}}$ cách chọn \n\n a có ${{6}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n Theo quy tắc nhân có ${{4 \\cdot 6 \\cdot 6  ={phan_so(4*6*6)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(6*7)} + {phan_so(4*6*6)}= {phan_so(6*7+4*6*6)} }}$ số ")


	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C8_B1_25]-SA-M3. B.toán tạo số chia hết cho 5 có các chữ số khác nhau (ds có chứa cso 0)
def mcn__L10_C8_B1_25(): 
	le=[1,3,7,9]
	so=[1,2,3,4,6,7,8,9]
	
	chan=[2,4,6,8]
	a,b,c =random.sample(le, 3)
	a1,b1,c1=random.sample(chan,3)
	chon =random.randint(1,5)
	if chon ==1:
		kq=phan_so(6*7+6*6)

		noi_dung=f" Từ các chữ số ${{0; 5;{a};{a1};{b};{b1};{c};{c1}}}$ tạo được bao nhiêu số tự nhiên có ba chữ số đôi một khác nhau và là số chia hết cho ${{5}}$."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abc}}$ $(a \\ne 0; a \\ne b \\ne c)$ \n\n"
		f" TH1: ${{c=0}}$ \n\n a có ${{7}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n Theo quy tắc nhân có ${{7 \\cdot 6 ={phan_so(6*7)}}}$ số \n\n"
		f" TH2: ${{c=5}}$ \n\n a có ${{6}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n Theo quy tắc nhân có ${{ 6 \\cdot 6  ={phan_so(6*6)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(6*7)} + {phan_so(6*6)}= {phan_so(6*7+6*6)} }}$ số ")
	if chon ==2:
		kq=phan_so(6*7*5+6*6*5)

		noi_dung=f" Từ các chữ số ${{0; 5;{a};{a1};{b};{b1};{c};{c1}}}$ tạo được bao nhiêu số tự nhiên có bốn chữ số đôi một khác nhau và là số chia hết cho ${{5}}$."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abcd}}$ $(a \\ne 0; a \\ne b \\ne c \\ne d)$ \n\n"
		f" TH1: ${{d=0}}$ \n\n a có ${{7}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n Theo quy tắc nhân có ${{7 \\cdot 6 \\cdot 5={phan_so(6*7*5)}}}$ số \n\n"
		f" TH2: ${{d=5}}$ \n\n a có ${{6}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n Theo quy tắc nhân có ${{ 6 \\cdot 6 \\cdot 5  ={phan_so(6*6*5)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(6*7*5)} + {phan_so(6*6*5)}= {phan_so(6*7*5+6*6*5)} }}$ số ")

	if chon ==3:
		kq=phan_so(6*7*5*4+6*6*5*4)

		noi_dung=f" Từ các chữ số ${{0; 5;{a};{a1};{b};{b1};{c};{c1}}}$ tạo được bao nhiêu số tự nhiên có năm chữ số đôi một khác nhau và là số chia hết cho ${{5}}$."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abcde}}$ $(a \\ne 0; a \\ne b \\ne c \\ne d)$ \n\n"
		f" TH1: ${{e=0}}$ \n\n a có ${{7}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n d có ${{4}}$ cách chọn \n\n Theo quy tắc nhân có ${{7 \\cdot 6 \\cdot 5 \\cdot 4={phan_so(6*7*5*4)}}}$ số \n\n"
		f" TH2: ${{e=5}}$ \n\n a có ${{6}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n d có ${{4}}$ cách chọn \n\n Theo quy tắc nhân có ${{ 6 \\cdot 6 \\cdot 5 \\cdot 4  ={phan_so(6*6*5*4)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(6*7*5*4)} + {phan_so(6*6*5*4)}= {phan_so(6*7*5*4+6*6*5*4)} }}$ số ")


	if chon ==4:
		kq=phan_so(6*7*5*4+6*6*5*4)
		a,a1,b,b1,c,c1=random.sample(so,6)

		noi_dung=f" Từ các chữ số ${{0; 5;{a};{a1};{b};{b1};{c};{c1}}}$ tạo được bao nhiêu số tự nhiên có năm chữ số đôi một khác nhau và là số chia hết cho ${{5}}$."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abcde}}$ $(a \\ne 0; a \\ne b \\ne c \\ne d)$ \n\n"
		f" TH1: ${{e=0}}$ \n\n a có ${{7}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n d có ${{4}}$ cách chọn \n\n Theo quy tắc nhân có ${{7 \\cdot 6 \\cdot 5 \\cdot 4={phan_so(6*7*5*4)}}}$ số \n\n"
		f" TH2: ${{e=5}}$ \n\n a có ${{6}}$ cách chọn \n\n b có ${{6}}$ cách chọn \n\n c có ${{5}}$ cách chọn \n\n d có ${{4}}$ cách chọn \n\n Theo quy tắc nhân có ${{ 6 \\cdot 6 \\cdot 5 \\cdot 4  ={phan_so(6*6*5*4)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(6*7*5*4)} + {phan_so(6*6*5*4)}= {phan_so(6*7*5*4+6*6*5*4)} }}$ số ")

	if chon ==5:
		kq=phan_so(6*3*5*4+3*5*5*4)
		a,a1,b,b1,c=random.sample(so,5)

		noi_dung=f" Từ các chữ số ${{0; 5;{a};{a1};{b};{b1};{c}}}$ tạo được bao nhiêu số tự nhiên có năm chữ số đôi một khác nhau và là số chia hết cho ${{5}}$."
		noi_dung_loigiai=(f" Gọi số cần lập là $\\overline{{abcde}}$ $(a \\ne 0; a \\ne b \\ne c \\ne d)$ \n\n"
		f" TH1: ${{e=0}}$ \n\n a có ${{6}}$ cách chọn \n\n b có ${{5}}$ cách chọn \n\n c có ${{4}}$ cách chọn \n\n d có ${{3}}$ cách chọn \n\n Theo quy tắc nhân có ${{6 \\cdot 5 \\cdot 4 \\cdot 3={phan_so(6*3*5*4)}}}$ số \n\n"
		f" TH2: ${{e=5}}$ \n\n a có ${{5}}$ cách chọn \n\n b có ${{5}}$ cách chọn \n\n c có ${{4}}$ cách chọn \n\n d có ${{3}}$ cách chọn \n\n Theo quy tắc nhân có ${{ 5 \\cdot 5 \\cdot 4 \\cdot 3  ={phan_so(5*5*4*3)}}}$ số \n\n"
		f" Vậy có ${{{phan_so(6*3*5*4)} + {phan_so(3*5*5*4)}= {phan_so(6*3*5*4+3*5*5*4)} }}$ số ")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an








#[D10_C8_B1_26]-SA-M3. B.toán tạo số có các chữ số khác nhau lớn hơn số m cho trước
def mcn__L10_C8_B1_26(): 
	n=random.randint(6,9)
	nhom1=tao_taphop_khac_0(n)


	# Bước 2: Số m cho trước
	m = random.randint(1234,4567)
	# Bước 3: Tạo tất cả các số có 4 chữ số khác nhau
	so_hoan_vi = [
	    int(''.join(map(str, p)))  # Chuyển từng hoán vị thành số nguyên
	    for p in permutations(nhom1, 4)  # Tạo các hoán vị 4 chữ số từ tập hợp
	]

	# Bước 4: Lọc ra các số lớn hơn 2300
	so_ket_qua = [so for so in so_hoan_vi if so > m]

	# Bước 5: Đếm số lượng các số thỏa mãn
	kq = len(so_ket_qua)

	noi_dung=f" Từ các chữ số $\\{{ {nhom1} \\}}$ lập được bao nhiêu số tự nhiên có bốn chữ số đôi một khác nhau và lớn hơn ${{{m}}}$. "
	noi_dung_loigiai=f" Lập được ${{{kq}}}$ số thoả mãn yêu cầu."
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an


#[D10_C8_B1_27]-SA-M3. B.toán tạo số có các chữ số khác nhau nhỏ hơn số m cho trước
def mcn__L10_C8_B1_27(): 
	n=random.randint(6,9)
	nhom1=tao_taphop_khac_0(n)


	# Bước 2: Số m cho trước
	m = random.randint(1234,4567)
	# Bước 3: Tạo tất cả các số có 4 chữ số khác nhau
	so_hoan_vi = [
	    int(''.join(map(str, p)))  # Chuyển từng hoán vị thành số nguyên
	    for p in permutations(nhom1, 4)  # Tạo các hoán vị 4 chữ số từ tập hợp
	]

	# Bước 4: Lọc ra các số lớn hơn 2300
	so_ket_qua = [so for so in so_hoan_vi if so < m]

	# Bước 5: Đếm số lượng các số thỏa mãn
	kq = len(so_ket_qua)

	noi_dung=f" Từ các chữ số $\\{{ {nhom1} \\}}$ lập được bao nhiêu số tự nhiên có bốn chữ số đôi một khác nhau và nhỏ hơn ${{{m}}}$. "
	noi_dung_loigiai=f" Lập được ${{{kq}}}$ số thoả mãn yêu cầu."
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C8_B1_28]-SA-M4. B.toán tính tổng các số được tạo ra.
def mcn__L10_C8_B1_28(): 
	chon=random.randint(1,2)
	if chon ==1:
		n=random.randint(6,9)
		nhom1=tao_taphop_chua_0(n)
		a1=random.choice([i for i in nhom1 if i!=0])
		nhom2 = [x for x in nhom1 if x != 0] 
		nhom2=str(nhom2)
		nhom2=nhom2.replace("["," ").replace("]"," ").replace(",","+")

		sl=len(nhom1)
		s1=(sl-2)*(sl-2)*(sl-3)
		# Bước 3: Tạo tất cả các số có 4 chữ số khác nhau
		so_hoan_vi = [
		    int(''.join(map(str, p)))  
		    for p in permutations(nhom1, 4)  
		    if p[0] != 0  # Loại bỏ hoán vị có số 0 đứng đầu
	]
		# Bước 4: Lọc ra các số lớn hơn 2300
		m=sum(so_hoan_vi)

		# Bước 5: Đếm số lượng các số thỏa mãn
		
		kq=tinh_tong_chu_so(m)

		noi_dung=f" Từ các chữ số $ {nhom1} $ lập tất cả các số tự nhiên có bốn chữ số đôi một khác nhau. Tổng các số lập được là ${{m}}$. Tính tổng các chữ số của số ${{m}}$ "
		noi_dung_loigiai=(f"\n\n Xét chữ số ${{{a1}}}$ đứng ở hàng đơn vị ${{{s1}}}$ lần \n\n"
						f" Hoàn toàn tương tự chữ số ${{{a1}}}$ cũng đứng ở hàng chục ${{{s1}}}$ lần, hàng trăm ${{{s1}}}$ lần\n\n"
						f" Xét chữ số ${{{a1}}}$ đứng ở hàng nghìn ${{{chinh_hop(3,sl-1)}}}$ lần \n\n"
						f" Các chữ số khác cũng vậy (không tính chữ số 0 vì không có giá trị khi tính tổng)\n\n"
						f" Tổng các số sẽ là \n\n  $\\left( {nhom2} \\right) \\cdot (1+10+100) \\cdot {s1} + \\left( {nhom2} \\right) \\cdot 1000 \\cdot {chinh_hop(3,sl-1)} ={m}$ \n\n"
		f" Tổng các số tạo ra là ${{{m}}}$. \n\n Tổng các chữ số của nó là ${{{kq}}}$.")
	

	if chon ==2:
		n=random.randint(6,9)
		nhom1=tao_taphop_khac_0(n)
		a1=random.choice([i for i in nhom1 if i!=0])
		nhom2 = [x for x in nhom1 if x != 0] 
		nhom2=str(nhom2)
		nhom2=nhom2.replace("["," ").replace("]"," ").replace(",","+")

		sl=len(nhom1)
		s1=(sl-1)*(sl-2)*(sl-3)
		# Bước 3: Tạo tất cả các số có 4 chữ số khác nhau
		so_hoan_vi = [
		    int(''.join(map(str, p)))  
		    for p in permutations(nhom1, 4)  
		    if p[0] != 0  # Loại bỏ hoán vị có số 0 đứng đầu
	]
		# Bước 4: Lọc ra các số lớn hơn 2300
		m=sum(so_hoan_vi)

		# Bước 5: Đếm số lượng các số thỏa mãn
		
		kq=tinh_tong_chu_so(m)

		noi_dung=f" Từ các chữ số $ {nhom1} $ lập tất cả các số tự nhiên có bốn chữ số đôi một khác nhau. Tổng các số lập được là ${{m}}$. Tính tổng các chữ số của số ${{m}}$ "
		noi_dung_loigiai=(f"\n\n Xét chữ số ${{{a1}}}$ đứng ở hàng đơn vị ${{{s1}}}$ lần \n\n"
						f" Hoàn toàn tương tự chữ số ${{{a1}}}$ cũng đứng ở hàng chục ${{{s1}}}$ lần, hàng trăm ${{{s1}}}$ lần, hàng nghìn ${{{s1}}}$ lần\n\n"
						f" Tương tự các chữ số khác cũng vậy\n\n"
						f" Tổng các số sẽ là \n\n $\\left( {nhom2} \\right) \\cdot (1+10+100+1000) \\cdot {s1} ={m}$ \n\n"
		f" Tổng các số tạo ra là ${{{m}}}$. \n\n Tổng các chữ số của nó là ${{{kq}}}$.")




	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an














#[D10_C8_B1_29]-SA-M3. Cho 2 dt //, tính số vecto tạo ra có điểm đầu, điểm cuối k nằm trên 1 dt
def mcn__L10_C8_B1_29(): 
	a1=random.randint(10,50)
	a2=random.randint(10,50)
	kq=a1*a2*2

	noi_dung=f" Cho hai đường thẳng song song ${{(d)}}$ và ${{(d')}}$. Trên đường thẳng ${{(d)}}$ lấy ${{{a1}}}$ điểm khác nhau, trên đường thẳng ${{(d')}}$ lấy ${{{a2}}}$ điểm khác nhau. Hỏi có thể vẽ được bao nhiêu vectơ mà các điểm đầu và điểm cuối không cùng nằm trên một đường thẳng."
	noi_dung_loigiai=(f" TH1: điểm đầu thuộc ${{(d)}}$ và điểm cuối ${{(d')}}$ có ${{ {a1} \\cdot {a2}={a1*a2} }}$ vecto \n\n"
						f" TH2: điểm đầu thuộc ${{(d')}}$ và điểm cuối ${{(d)}}$ có ${{ {a1} \\cdot {a2}={a1*a2} }}$ vecto \n\n "
						f" Theo quy tắc cộng số vecto là ${{{a1*a2} +{a1*a2} ={a1*a2*2}}}$ vecto")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C8_B1_30]-SA-M4. Đếm các số chẵn(lẻ) có các chữ số khác nhau và nhỏ hơn(lớn hơn) m
def mcn__L10_C8_B1_30(): 
	n=random.randint(6,9)
	nhom1=tao_taphop_khac_0(n)


	# Bước 2: Số m cho trước
	
	# Bước 3: Tạo tất cả các số có 4 chữ số khác nhau
	so_hoan_vi = [
	    int(''.join(map(str, p)))  # Chuyển từng hoán vị thành số nguyên
	    for p in permutations(nhom1, 4)  # Tạo các hoán vị 4 chữ số từ tập hợp
	]

	chon=random.randint(1,4)
	if chon==1:
		m = random.randint(1234,4567)
	# Bước 4: Lọc ra các số lớn hơn 2300
		so_ket_qua = [so for so in so_hoan_vi if so > m and so%2==0 ]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)

		noi_dung=f" Từ các chữ số $\\{{ {nhom1} \\}}$ lập được tất cả bao nhiêu số tự nhiên chẵn có bốn chữ số đôi một khác nhau và lớn hơn ${{{m}}}$. "
		noi_dung_loigiai=f"Lập được ${{{kq}}}$ số (kết quả do lập trình tính) ."

	if chon==2:
		m = random.randint(1234,4567)
	# Bước 4: Lọc ra các số lớn hơn 2300
		so_ket_qua = [so for so in so_hoan_vi if so > m and so%2!=0 ]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)

		noi_dung=f" Từ các chữ số $\\{{ {nhom1} \\}}$ lập được tất cả bao nhiêu số tự nhiên lẻ có bốn chữ số đôi một khác nhau và lớn hơn ${{{m}}}$. "
		noi_dung_loigiai=f"Lập được ${{{kq}}}$ số (kết quả do lập trình tính) ."


	if chon==3:
		m = random.randint(6234,6567)
	# Bước 4: Lọc ra các số lớn hơn 2300
		so_ket_qua = [so for so in so_hoan_vi if so > m and so%2==0 ]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)

		noi_dung=f" Từ các chữ số $\\{{ {nhom1} \\}}$ lập được tất cả bao nhiêu số tự nhiên chẵn có bốn chữ số đôi một khác nhau và nhỏ hơn ${{{m}}}$. "
		noi_dung_loigiai=f"Lập được ${{{kq}}}$ số (kết quả do lập trình tính) ."

	if chon==4:
		m = random.randint(6234,6567)
	# Bước 4: Lọc ra các số lớn hơn 2300
		so_ket_qua = [so for so in so_hoan_vi if so > m and so%2!=0 ]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)

		noi_dung=f" Từ các chữ số $\\{{ {nhom1} \\}}$ lập được tất cả bao nhiêu số tự nhiên lẻ có bốn chữ số đôi một khác nhau và nhỏ hơn ${{{m}}}$. "
		noi_dung_loigiai=f"Lập được ${{{kq}}}$ số (kết quả do lập trình tính) ."


	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an




#8.2.1 Hoán vị
#[D10_C8_B2_01]-M1. Xếp k bạn vào một hàng
def mcn__L10_C8_B2_01():  	
	k=random.randint(2,7)
	hang=random.choice(["ngang", "dọc"])
	kq=factorial(k)
	kq2=k**2
	kq3=k*(k-1)
	kq4=k

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Có bao nhiêu cách xếp ${{{k}}}$ bạn vào một hàng {hang}."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Mỗi cách chọn là một hoán vị của ${{{k}}}$ phần tử.\n "\
					f"Số cách chọn là: ${{{k}!={kq}}}$.\n"
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_02]-M1. Tìm số cách chọn k vật từ n nhóm đồ vật.
def mcn__L10_C8_B2_02():   
	#Tạo bậc ngẫu nhiên
	do_vat=random.choice(["bút chì màu", "cái bút bi", "điện thoại" ,"tai nghe", "cái bóng đèn","cuốn truyện tranh", "cuốn sách", "cuốn vở"])

	n=random.randint(8,15)
	k=random.randint(2,7)
	
	kq=chinh_hop(k,n)
	kq2=k*n
	kq3=binomial(n,k)
	kq4=n+k

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Có bao nhiêu cách chọn ${{{k}}}$ {do_vat} từ ${{{n}}}$ {do_vat} nhãn hiệu khác nhau và tặng cho ${{{k}}}$ bạn khác nhau?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Mỗi cách chọn là một chỉnh hợp chập ${{{k}}}$ của ${{{n}}}$.\n "\
					f"Số cách chọn là: $A^{{{k}}}_{{{n}}}={kq}$.\n"
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_03]-M1. Tìm số cách chọn k người từ n người và sắp xếp chức vụ trong lớp.
def mcn__L10_C8_B2_03():   
	#Tạo bậc ngẫu nhiên
	nguoi=random.choice(["học sinh"])
	chuc_vu_1=["lớp trưởng", "lớp phó học tập", "bí thư", "lớp phó lao động", "lớp phó văn nghệ", "thủ quỹ"]

	n=random.randint(25,35)
	k=random.randint(2,4)
	chuc_vu=""
	for i in range(k):
		chuc_vu+=f"{chuc_vu_1[i]}, "
	chuc_vu=chuc_vu[:-2]
	
	kq=chinh_hop(k,n)
	kq2=k*n
	kq3=binomial(n,k)
	kq4=n+k

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Có bao nhiêu cách chọn ${{{k}}}$ {nguoi} từ ${{{n}}}$ {nguoi} để giữ các chức vụ {chuc_vu} của lớp?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Mỗi cách chọn là một chỉnh hợp chập ${{{k}}}$ của ${{{n}}}$.\n "\
					f"Số cách chọn là: $A^{{{k}}}_{{{n}}}={kq}$.\n"
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C8_B2_04]-M1. Chọn k người từ n người phụ trách n công việc khác nhau.
def mcn__L10_C8_B2_04():   
	#Tạo bậc ngẫu nhiên
	nguoi=["học sinh","công an viên", "bác sĩ", "bông hoa", "học sinh", "đoàn viên"]
	cong_viec=["trực cờ đỏ", "quản lí", "trực", "cắm", "làm tổ trưởng", "trực cổng trường"]	
	tai=["tại","tại","tại","vào", "của", "vào"]
	noi_lam=["lớp","thôn","khoa", "lọ hoa","tổ", "ngày"]
	i=random.randint(0,len(nguoi)-1)
	n=random.randint(15,30)
	k=random.randint(2,5)	

	
	kq=chinh_hop(k,n)
	kq2=k*n*n
	kq3=binomial(n,k)
	kq4=n*k*k

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Có bao nhiêu cách chọn ${{{k}}}$ {nguoi[i]} từ ${{{n}}}$ {nguoi[i]} để {cong_viec[i]} {tai[i]} ${{{k}}}$ {noi_lam[i]} khác nhau?"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Mỗi cách chọn là một chỉnh hợp chập ${{{k}}}$ của ${{{n}}}$.\n "\
					f"Số cách chọn là: $A^{{{k}}}_{{{n}}}={kq}$.\n"
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_05]-M2. Từ n chữ số lập được bao nhiêu số có k chữ số khác nhau.
def mcn__L10_C8_B2_05():  	
	n=random.randint(6,9)
	set_A =tao_taphop_khac_0(n)
	k=random.randint(4,n-1)

	kq=chinh_hop(k,n)
	kq2=n*k
	kq3=binomial(n, k)
	kq4=n+k

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Từ các chữ  số $\\{{ {set_A} \\}}$ có thể lập được bao nhiêu số tự nhiên gồm {k} chữ số khác nhau?" \


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	a_i=""
	a_i_chu=""
	for i in range(1,k+1):
		a_i=a_i +f"a_{i}"
		a_i_chu=a_i_chu +f"a_{i},"
		
	a_i_chu=a_i_chu[:-1]

	noi_dung_loigiai=f"Gọi $\\overline{{{a_i}}}$ là số cần lập.\n"\
		f"Mỗi cách chọn một bộ ${{{a_i_chu}}}$ là một chỉnh hợp chập ${{{k}}}$ của ${{{n}}}$ phần tử.\n"\
		f"Số cách lập là: $A^{{{k}}}_{{{n}}} ={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_06]-M2. Lập số có k chữ số khác nhau từ n chữ số (chứa số 0).
def mcn__L10_C8_B2_06():  	
	n=random.randint(6,9)
	set_A =tao_taphop_chua_0(n)
	k=random.randint(4,n-1)

	kq=(n-1)*chinh_hop(k-1,n-1)
	kq2=n*chinh_hop(k-1,n-1)
	kq3=binomial(n, k)
	kq4=chinh_hop(k,n)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Từ các chữ  số $\\{{ {set_A} \\}}$ có thể lập được bao nhiêu số tự nhiên gồm {k} chữ số khác nhau?" \


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	a_i=""
	a_i_chu=""
	for i in range(1,k+1):
		a_i=a_i +f"a_{i}"
		a_i_chu=a_i_chu +f"a_{i},"
		
	a_i_chu=a_i_chu[4:-1]

	noi_dung_loigiai=f"Gọi $\\overline{{{a_i}}}$ là số cần lập.\n"\
		f"Chọn $a_1 \\ne 0$ có ${n-1}$ cách.\n"\
		f"Mỗi cách chọn một bộ ${{{a_i_chu}}}$ là một chỉnh hợp chập ${{{k-1}}}$ của ${{{n-1}}}$ phần tử.\n"\
		f"Số cách lập là: ${n-1}.A^{{{k-1}}}_{{{n-1}}} ={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C8_B2_07]-M2. Xếp k nhóm đồ vật vào một hàng.
def mcn__L10_C8_B2_07():  	
	m=random.randint(3,10)
	n=random.randint(3,10)
	p=random.randint(4,10)
	q=random.randint(4,10)
	if m==n==p:
		n=m-1
	if m==n==p==q:
		n=m-1
		p=q+1
	do_vat_1=["cuốn sách Toán", "cuốn sách Văn", "cuốn sách Tiếng Anh", "cuốn sách Vật Lí", "cuốn sách Hóa Học", "cuốn sách Sinh Học"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]

	do_vat=random.choice([do_vat_1,do_vat_2,do_vat_3])

	chon=random.randint(2,4)
	if chon==2:
		noi_dung=f"Có bao nhiêu cách xếp ${{{m}}}$ {do_vat[0]} khác nhau và ${{{n}}}$ {do_vat[1]} khác nhau"\
					f"vào một kệ ngang theo từng loại?"

		kq=f"2.{m}!.{n}!"
		kq2=f"2.({m}!+{n}!)"
		kq3=f"{m}!.{n}!"
		kq4=f"{m*n*p}!"

		noi_dung_loigiai=f"Số các chọn vị trí cho từng loại là: ${{2!=2}}$.\n"\
						f"Số xếp {do_vat[0]} là: ${{{m}!}}$.\n"\
						f"Số xếp {do_vat[1]} là: ${{{n}!}}$.\n"\
						f"Theo quy tắc nhân, tổng số xếp là: ${{{kq}}}$.\n"
	elif chon==3:
		noi_dung=f"Có bao nhiêu cách xếp ${{{m}}}$ {do_vat[0]} khác nhau, ${{{n}}}$ {do_vat[1]} khác nhau"\
					f"và ${{{p}}}$ {do_vat[2]} khác nhau vào một kệ ngang theo từng loại?"

		kq=f"3!.{m}!.{n}!.{p}!"
		kq2=f"{m}!.{n}!.{p}!"
		kq3=f"{m+n+p}!"
		kq4=f"3!.{m*n*p}!"

		noi_dung_loigiai=f"Số các chọn vị trí cho từng loại là: ${{3!}}$.\n"\
						f"Số xếp {do_vat[0]} là: ${{{m}!}}$.\n"\
						f"Số xếp {do_vat[1]} là: ${{{n}!}}$.\n"\
						f"Số xếp {do_vat[2]} là: ${{{p}!}}$.\n"\
						f"Theo quy tắc nhân, tổng số xếp là: ${{{kq}}}$.\n"
	else:

		noi_dung=f"Có bao nhiêu cách xếp ${{{m}}}$ {do_vat[0]} khác nhau, ${{{n}}}$ {do_vat[1]} khác nhau,"\
					f"${{{p}}}$ {do_vat[2]} và ${{{q}}}$ {do_vat[3]} khác nhau vào một kệ ngang theo từng loại?"

		kq=f"4!.{m}!.{n}!.{p}!.{q}!"
		kq2=f"{m}!.{n}!.{p}!.{q}!"
		kq3=f"{m+n+p+q}!"
		kq4=f"4!.{m*n*p*q}!"

		noi_dung_loigiai=f"Số các chọn vị trí cho từng loại là: ${{4!}}$.\n"\
						f"Số xếp {do_vat[0]} là: ${{{m}!}}$.\n"\
						f"Số xếp {do_vat[1]} là: ${{{n}!}}$.\n"\
						f"Số xếp {do_vat[2]} là: ${{{p}!}}$.\n"\
						f"Số xếp {do_vat[3]} là: ${{{q}!}}$.\n"\
						f"Theo quy tắc nhân, tổng số xếp là: ${{{kq}}}$.\n"


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA) 	


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_08]-TF-M2. Tạo câu đúng-sai: Chọn 2 nhóm đồ vật.	
def mcn__L10_C8_B2_08(): 
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]


	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	i=random.randint(0,len(vat_1)-1)
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"


	so_vat_1=random.randint(10,15)
	so_vat_2=random.randint(7,13)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,7)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq5_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_true}}}$"
	kq5_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_false}}}$"
	loigiai_5=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: "\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."
	

	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	
	kq5=random.choice([kq5_T, kq5_F])

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4, kq5]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
		if pa==kq1:
			loigiai.append(loigiai_1)
		if pa==kq2:
			loigiai.append(loigiai_2)
		if pa==kq3:
			loigiai.append(loigiai_3)
		if pa==kq4:
			loigiai.append(loigiai_4)
		if pa==kq5:
			loigiai.append(loigiai_5)

	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n \n"\
	f"b) {loigiai[1]}\n \n"\
	f"c) {loigiai[2]}\n \n"\
	f"d) {loigiai[3]}\n \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an


#[D10_C8_B2_09]-M1. Chọn k đối tượng từ n đối tượng.
def mcn__L10_C8_B2_09():  	
	k=random.randint(3,8)
	n=k+random.randint(6,12)

	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]

	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sác"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]

	i=random.randint(0,len(vat_1)-1)
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"


	noi_dung=f"Số cách chọn ${{{k}}}$ {ten_chung} từ ${{{n}}}$ {ten_chung} là"

	kq=binomial(n,k)
	kq2=chinh_hop(k,n)
	kq3=n*k
	kq4=random.choice([binomial(n,k)+random.randint(10,30), abs(binomial(n,k)-random.randint(10,30))])

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} từ ${{{n}}}$ {ten_chung} là: $C^{{{k}}}_{{{n}}}={kq}$.\n"	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA) 	


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C8_B2_10]-M2. Chọn k đối tượng từ 2 nhóm đối tượng.
def mcn__L10_C8_B2_10():  	

	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]

	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]

	i=random.randint(0,len(vat_1)-1)
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	k=random.randint(3,8)
	so_vat_1=random.randint(6,15)
	so_vat_2=random.randint(5,12)
	n=so_vat_1 + so_vat_2

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Số cách chọn ${{{k}}}$ {ten_chung} từ {address} là"

	kq=binomial(n,k)
	kq2=chinh_hop(k,n)
	kq3=n*k
	kq4=random.choice([binomial(n,k)+random.randint(20,30), abs(binomial(n,k)-random.randint(10,20))])

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} là: $C^{{{k}}}_{{{n}}}={kq}$.\n"	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA) 	


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_11]-M2. Chọn k đối tượng tự từ 2 nhóm đối tượng thỏa mãn điều kiện.
def mcn__L10_C8_B2_11():  	

	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]

	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]

	i=random.randint(0,len(vat_1)-1)
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"
	#Khai báo số lượng ban đầu
	so_vat_1=random.randint(10,15)
	so_vat_2=random.randint(7,13)
	tong_so= so_vat_1 + so_vat_2

	
	#Tạo số lượng cần lấy
	k=random.randint(3,7)
	k_1=random.randint(2,k-1)
	k_2=k-k_1

	chon=random.randint(1,3)
	if chon==1:
		noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}." \
			f" Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là"		

		kq=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
		kq2=binomial(so_vat_1,k_1)+binomial(so_vat_2,k_2)
		kq3=binomial(so_vat_1,k_1)
		kq4=random.choice([binomial(tong_so,k_1), binomial(tong_so,k)+random.randint(100,200), abs(binomial(tong_so,k)-random.randint(50,100))])

		noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là: $C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={kq}$.\n"	
	
	elif chon==2:

		noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}." \
			f" Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_2}}}$ {vat_2} là"		

		kq=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
		kq2=binomial(so_vat_1,k_1)+binomial(so_vat_2,k_2)
		kq3=binomial(so_vat_1,k_1)
		kq4=random.choice([binomial(tong_so,k_1), binomial(tong_so,k)+random.randint(100,200), abs(binomial(tong_so,k)-random.randint(50,100))])

		noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_2}}}$ {vat_2} là: $C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={kq}$.\n"	

	else:

		noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}." \
			f" Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là"		

		kq=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
		kq2=binomial(so_vat_1,k)*binomial(so_vat_2,k)
		kq3=binomial(tong_so,k)
		kq4=random.choice([binomial(tong_so,k_1)+binomial(tong_so,k_2), abs(binomial(tong_so,k)-random.randint(50,100))])

		noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là:"\
						f" $C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq}$.\n"	

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA) 	


	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_12]-M2. Xếp k học sinh vào 1 hàng, có 2 bạn đứng ở 2 đầu.
def mcn__L10_C8_B2_12():   
	#Tạo bậc ngẫu nhiên
	ten_vat="học sinh"
	ten_dau_hang=random.choice(["bạn Phương", "bạn Minh", "bạn Thảo", "bạn Thắng", "bạn Thùy"])
	ten_cuoi_hang=random.choice(["bạn Linh", "bạn Đức", "bạn Tuyết", "bạn Mai", "bạn Nhi"])
	hang=random.choice(["hàng dọc", "hàng ngang"])	

	k=random.randint(6,12)

	kq=2*factorial(k-2)
	kq2=factorial(k)
	kq3=binomial(k,2)
	kq4=factorial(k+2)

	noi_dung=f"Có bao nhiêu cách xếp ${{{k}}}$ {ten_vat} trong đó có bạn {ten_dau_hang} và {ten_cuoi_hang} vào một {hang} sao cho {ten_dau_hang} và {ten_cuoi_hang} đứng ở hai đầu?"
	noi_dung_loigiai=f"Xếp {ten_dau_hang} và {ten_cuoi_hang} vào hai đầu có: ${{2}}$ cách.\n "\
					f"Xếp ${{{k-2}}}$ bạn còn lại có: ${{{k-2}!={factorial(k-2)}}}$ cách.\n"\
					f"Số cách xếp thỏa mãn yêu cầu là: ${{2.{k-2}!={kq}}}$."		

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_13]-M3. Xếp k học sinh vào 1 hàng, có 2 bạn đứng cạnh nhau hoặc không cạnh nhau.
def mcn__L10_C8_B2_13():   
	#Tạo bậc ngẫu nhiên
	ten_vat="học sinh"
	ten_dau_hang=random.choice(["bạn Phương", "bạn Minh", "bạn Thảo", "bạn Thắng", "bạn Thùy"])
	ten_cuoi_hang=random.choice(["bạn Linh", "bạn Đức", "bạn Tuyết", "bạn Mai", "bạn Nhi"])
	hang=random.choice(["hàng dọc", "hàng ngang"])
	canh_nhau=random.choice(["đứng cạnh nhau", "không đứng cạnh nhau"])

	k=random.randint(5,12)

	canh_nhau=random.choice(["đứng cạnh nhau", "không đứng cạnh nhau"])
	
	if canh_nhau=="đứng cạnh nhau":	
		kq=2*(k-1)*factorial(k-2)
		kq2=random.choice([2*factorial(k),2*factorial(k-1)])
		kq3=(k-1)*factorial(k-2)
		kq4=random.choice([2*factorial(k-1),factorial(k)*2])

		noi_dung=f"Có bao nhiêu cách xếp ${{{k}}}$ {ten_vat} trong đó có bạn {ten_dau_hang} và {ten_cuoi_hang} vào một {hang} sao cho {ten_dau_hang} và {ten_cuoi_hang} {canh_nhau}?"
		noi_dung_loigiai=f"Xếp {ten_dau_hang} và {ten_cuoi_hang} {canh_nhau} có: ${{2.{k-1}={2*(k-1)}}}$ cách.\n"\
					f"Xếp ${{{k-2}}}$ bạn còn lại có: ${{{k-2}!={factorial(k-2)}}}$ cách.\n"\
					f"Số cách xếp thỏa mãn yêu cầu là: ${{2.{k-1}.{factorial(k-2)}={kq}}}$."	
	else:
		t_canhnhau=2*(k-1)*factorial(k-2)		
		kq=factorial(k)-t_canhnhau
		kq2=random.choice([2*factorial(k), (k-1)*factorial(k-2)])
		kq3=random.choice([(k-1)*factorial(k-2), 2*k*factorial(k-1)])
		kq4=random.choice([kq+random.randint(100,400)])

		noi_dung=f"Có bao nhiêu cách xếp ${{{k}}}$ {ten_vat} trong đó có bạn {ten_dau_hang} và {ten_cuoi_hang} vào một {hang} sao cho {ten_dau_hang} và {ten_cuoi_hang} {canh_nhau}?"
		noi_dung_loigiai=f"Xếp ${{{k}}}$ bạn tùy ý có ${{{k}!={factorial(k)}}}$ cách.\n"\
					f"Xếp {ten_dau_hang} và {ten_cuoi_hang} cạnh nhau có: ${{2.{k-1}={2*(k-1)}}}$ cách.\n"\
					f"Xếp ${{{k-2}}}$ bạn còn lại có: ${{{k-2}!={factorial(k-2)}}}$ cách.\n"\
					f"Số cách xếp ${{{k}}}$ {ten_vat} trong đó có bạn {ten_dau_hang} và {ten_cuoi_hang} cạnh nhau là: ${{{2*(k-1)}.{factorial(k-2)}={t_canhnhau}}}$.\n"\
					f"Số cách xếp {ten_dau_hang} và {ten_cuoi_hang} không đứng cạnh nhau là: ${{{factorial(k)}-{t_canhnhau}={kq}}}$."


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_14]-M2. Số đoạn thẳng tạo bởi 2 điểm
def mcn__L10_C8_B2_14():   
	
	n=random.randint(6,18)
	kq=binomial(n,2)
	kq2=chinh_hop(2,n)
	kq3=random.choice([kq2+random.randint(100,400)])
	kq4=random.choice([kq+random.randint(100,400)])

	noi_dung=f"Cho ${{{n}}}$ điểm phân biệt, lập được bao nhiêu đoạn thẳng nhận các điểm đã cho làm đầu mút?"
	noi_dung_loigiai=f"Mỗi đoạn thẳng là một tổ hợp chập ${{2}}$ của ${{{n}}}$ phần tử.\n"\
	f"Số đoạn thẳng là số tổ hợp chập ${{2}}$ của ${{{n}}}$ phần tử: $C^2_{{{n}}}={kq}$.\n"


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_15]-M2. Số tam giác tạo bởi 3 điểm
def mcn__L10_C8_B2_15():   
	
	n=random.randint(6,18)
	kq=binomial(n,3)
	kq2=chinh_hop(3,n)
	kq3=random.choice([kq2+random.randint(100,400)])
	kq4=random.choice([kq+random.randint(100,400)])

	noi_dung=f"Cho ${{{n}}}$ điểm phân biệt cho trước và không có ${{3}}$ điểm bất kì nào thẳng hàng, lập được bao nhiêu tam giác nhận các điểm đã cho làm đỉnh?"
	noi_dung_loigiai=f"Mỗi đoạn thẳng là một tổ hợp chập ${{3}}$ của ${{{n}}}$ phần tử.\n"\
	f"Số đoạn thẳng là số tổ hợp chập ${{3}}$ của ${{{n}}}$ phần tử: $C^3_{{{n}}}={kq}$.\n"


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_16]-M1. Số tập hợp con gồm k phần tử của n phần tử
def mcn__L10_C8_B2_16():   
	
	n=random.randint(6,18)
	k=random.randint(2,n-2)
	kq=binomial(n,k)
	kq2=chinh_hop(k,n)
	kq3=random.choice([k,n*k,kq2+random.randint(100,400)])
	kq4=random.choice([kq+random.randint(100,400)])

	noi_dung=f"Cho tập hợp ${{A}}$ có ${{{n}}}$ phần tử. Số tập hợp con gồm ${{{k}}}$ phần tử của tập hợp ${{A}}$ là"
	noi_dung_loigiai=f"Số tập hợp con gồm ${{{k}}}$ phần tử của tập hợp ${{A}}$ là: $C^3_{{{n}}}={kq}$.\n"	


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_17]-M3. Số tập hợp con có số phần tử < hơn k 
def mcn__L10_C8_B2_17():   
	
	n=random.randint(7,15)
	k=random.randint(2,6)
	t=0
	text=""
	for i in range(k):
		t+=binomial(n,i)
		text+=f"C^{{{i}}}_{{{n}}}+"
	text=text[0:-1]

	kq=t
	kq2=chinh_hop(k,n)
	kq3=random.choice([k,n*k,kq2+random.randint(100,400)])
	kq4=random.choice([binomial(n,k),kq+random.randint(100,400)])

	noi_dung=f"Cho tập hợp ${{A}}$ có ${{{n}}}$ phần tử. Số tập hợp con có số phần tử nhỏ hơn ${{{k}}}$ của tập hợp ${{A}}$ là"
	noi_dung_loigiai=f"Số tập hợp con có số phần tử nhỏ hơn ${{{k}}}$ của tập hợp ${{A}}$ là: ${text}={kq}$.\n"	


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_18]-M2. Số giao điểm tối đa của n đường thẳng phân biệt
def mcn__L10_C8_B2_18():   
	
	n=random.randint(6,15)
	kq=binomial(n,2)
	kq2=chinh_hop(2,n)
	kq3=random.choice([kq2+random.randint(100,400)])
	kq4=random.choice([kq+random.randint(100,400)])

	noi_dung=f"Tìm số giao điểm tối đa của ${{{n}}}$ đường thẳng phân biệt."
	noi_dung_loigiai=f"Mỗi giao điểm (nếu có) là một tổ hợp chập ${{2}}$ của ${{{n}}}$ phần tử.\n"\
	f"Số giao điểm tối đa là số tổ hợp chập ${{2}}$ của ${{{n}}}$ phần tử: $C^2_{{{n}}}={kq}$.\n"


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_19]-M3. Số hình chữ nhật tạo từ n đường song song và m đường vuông góc
def mcn__L10_C8_B2_19():   
	
	m=random.randint(6,12)
	n=random.randint(4,10)
	kq=binomial(m,2)*binomial(n,2)
	kq2=chinh_hop(4,m+n)
	kq3=binomial(m+n,4)
	kq4=kq+random.randint(100,400)

	noi_dung=f"Trong mặt phẳng có bao nhiêu hình chữ nhật được tạo thành từ ${{{m}}}$ đường thẳng đôi một song song và ${{{n}}}$ đường thẳng vuông góc với ${{{m}}}$ đường thẳng song song đó."
	noi_dung_loigiai=f"Mỗi hình chữ nhật là một cách chọn 2 đường từ ${{{m}}}$ đường song song và 2 đường từ ${{{n}}}$ đường vuông góc.\n"\
					f"Số cách chọn 2 đường từ ${{{m}}}$ đường: $C^2_{{{m}}}={binomial(m,2)}$.\n"\
					f"Số cách chọn 2 đường từ ${{{n}}}$ đường: $C^2_{{{n}}}={binomial(n,2)}$.\n"\
					f"Số hình chữ nhật là: ${binomial(m,2)}.{binomial(n,2)}={binomial(m,2)*binomial(n,2)}$.\n"


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_20]-M2. Số giao điểm tối đa của n đường tròn
def mcn__L10_C8_B2_20():   
	
	n=random.randint(5,15)
	kq=2*binomial(n,2)
	kq2=2*chinh_hop(2,n)
	kq3=random.choice([binomial(n,2), kq2+random.randint(100,400)])
	kq4=random.choice([binomial(n-2,2),kq+random.randint(100,400)])

	noi_dung=f"Tìm số giao điểm tối đa của ${{{n}}}$ đường tròn phân biệt."
	noi_dung_loigiai=f"Mỗi cách chọn 2 đường tròn từ  ${{{n}}}$ đường tròn là một tổ hợp chập ${{2}}$ của ${{{n}}}$ phần tử.\n"\
					f"Mỗi cặp đường tròn cho tối đa 2 giao điểm.\n"\
					f"Số giao điểm tối đa của ${{{n}}}$ đường tròn phân biệt là: $2*C^2_{{{n}}}={kq}$.\n"


	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B2_21]-M3. Số giao điểm tối đa của m đường thẳng và n đường tròn.
def mcn__L10_C8_B2_21():  
	m=random.randint(8,15) 	
	n=random.randint(5,10)
	kq=binomial(m,2)+2*binomial(n,2)+m*n*2
	kq2=binomial(m+n,2)
	kq3=random.choice([m*n*2, kq+random.randint(100,200)])
	kq4=random.choice([binomial(m,2)+2*binomial(n,2),kq+random.randint(200,400)])

	noi_dung=f"Cho ${{{m}}}$ đường thẳng phân biệt và ${{{n}}}$ đường tròn phân biệt. Tìm số giao điểm tối đa tạo bởi các đường thẳng và đường tròn đã cho."
	noi_dung_loigiai=f"Số giao điểm tối đa của ${{{m}}}$ đường thẳng phân biệt là: $C^2_{{{m}}}={binomial(m,2)}$.\n"\
					f"Số giao điểm tối đa của ${{{n}}}$ đường tròn phân biệt là: $2.C^2_{{{n}}}={2*binomial(n,2)}$.\n"\
					f"Số giao điểm tối đa của ${{{m}}}$ đường thẳng phân biệt và ${{{n}}}$ đường tròn phân biệt là: ${m}.{n}.2={m*n*2}$.\n"\
					f"Tổng số giao điểm tối đa được tạo ra là:${{{binomial(m,2)}+{2*binomial(n,2)}+{m*n*2}={kq}}}$."

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan,loigiai_traloingan,dap_an

#[D10_C8_B2_22]-TF-M2. Tạo câu đúng-sai: Chọn 2 nhóm cuốn sách.	
def mcn__L10_C8_B2_22(): 
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]


	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	i=4
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	so_vat_1=random.randint(10,15)
	so_vat_2=random.randint(7,12)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,6)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq5_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_true}}}$"
	kq5_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_false}}}$"
	loigiai_5=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: "\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."
	

	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	
	kq5=random.choice([kq5_T, kq5_F])

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4, kq5]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
		if pa==kq1:
			loigiai.append(loigiai_1)
		if pa==kq2:
			loigiai.append(loigiai_2)
		if pa==kq3:
			loigiai.append(loigiai_3)
		if pa==kq4:
			loigiai.append(loigiai_4)
		if pa==kq5:
			loigiai.append(loigiai_5)

	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n \n"\
	f"b) {loigiai[1]}\n \n"\
	f"c) {loigiai[2]}\n \n"\
	f"d) {loigiai[3]}\n \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C8_B2_23]-TF-M2. Tạo câu đúng-sai: Chọn 2 cuốn truyện.	
def mcn__L10_C8_B2_23(): 
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]


	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	i=2
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	so_vat_1=random.randint(10,15)
	so_vat_2=random.randint(7,12)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,6)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq5_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_true}}}$"
	kq5_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_false}}}$"
	loigiai_5=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: "\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."
	

	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	
	kq5=random.choice([kq5_T, kq5_F])

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4, kq5]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
		if pa==kq1:
			loigiai.append(loigiai_1)
		if pa==kq2:
			loigiai.append(loigiai_2)
		if pa==kq3:
			loigiai.append(loigiai_3)
		if pa==kq4:
			loigiai.append(loigiai_4)
		if pa==kq5:
			loigiai.append(loigiai_5)

	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n \n"\
	f"b) {loigiai[1]}\n \n"\
	f"c) {loigiai[2]}\n \n"\
	f"d) {loigiai[3]}\n \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C8_B2_24]-TF-M2. Tạo câu đúng-sai: Chọn 2 bức tranh.	
def mcn__L10_C8_B2_24(): 
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]


	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	i=3
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	so_vat_1=random.randint(10,15)
	so_vat_2=random.randint(7,12)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,6)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq5_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_true}}}$"
	kq5_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_false}}}$"
	loigiai_5=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: "\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."
	

	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	
	kq5=random.choice([kq5_T, kq5_F])

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4, kq5]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
		if pa==kq1:
			loigiai.append(loigiai_1)
		if pa==kq2:
			loigiai.append(loigiai_2)
		if pa==kq3:
			loigiai.append(loigiai_3)
		if pa==kq4:
			loigiai.append(loigiai_4)
		if pa==kq5:
			loigiai.append(loigiai_5)

	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n \n"\
	f"b) {loigiai[1]}\n \n"\
	f"c) {loigiai[2]}\n \n"\
	f"d) {loigiai[3]}\n \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C8_B2_25]-TF-M2. Tạo câu đúng-sai: Chọn 2 viên bi.	
def mcn__L10_C8_B2_25(): 
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]


	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	i=1
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	so_vat_1=random.randint(10,15)
	so_vat_2=random.randint(7,12)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,6)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq5_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_true}}}$"
	kq5_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_false}}}$"
	loigiai_5=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: "\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."
	

	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	
	kq5=random.choice([kq5_T, kq5_F])

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4, kq5]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
		if pa==kq1:
			loigiai.append(loigiai_1)
		if pa==kq2:
			loigiai.append(loigiai_2)
		if pa==kq3:
			loigiai.append(loigiai_3)
		if pa==kq4:
			loigiai.append(loigiai_4)
		if pa==kq5:
			loigiai.append(loigiai_5)

	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n \n"\
	f"b) {loigiai[1]}\n \n"\
	f"c) {loigiai[2]}\n \n"\
	f"d) {loigiai[3]}\n \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C8_B2_26]-TF-M2. Tạo câu đúng-sai: Chọn 2 người.	
def mcn__L10_C8_B2_26(): 
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]


	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	i=0
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	so_vat_1=random.randint(10,15)
	so_vat_2=random.randint(7,12)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,6)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(3,8)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(3,7)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq5_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_true}}}$"
	kq5_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: ${{{kq_false}}}$"
	loigiai_5=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là: "\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."
	

	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	
	kq5=random.choice([kq5_T, kq5_F])

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4, kq5]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
		if pa==kq1:
			loigiai.append(loigiai_1)
		if pa==kq2:
			loigiai.append(loigiai_2)
		if pa==kq3:
			loigiai.append(loigiai_3)
		if pa==kq4:
			loigiai.append(loigiai_4)
		if pa==kq5:
			loigiai.append(loigiai_5)

	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n \n"\
	f"b) {loigiai[1]}\n \n"\
	f"c) {loigiai[2]}\n \n"\
	f"d) {loigiai[3]}\n \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"	
	return debai,debai_latex,loigiai_word,dap_an




#[D10_C8_B2_27]-M2. Xếp n người vào bàn tròn	
def mcn__L10_C8_B2_27(): 
	n=random.randint(8,30)
	noi_dung=f" Có bao nhiêu cách xếp ${{{n}}}$ người vào một bàn tròn."
	noi_dung_loigiai=f" Số cách xếp ${{{n}}}$ người vào bàn tròn là ${{{n-1}!}}$"

	kq=f"${{{n-1}!}}$"
	kqs=[f"${{{n}!}}$",
	f"${{{n-2}!}}$",
	f"${{{n+2}!}}$",
f"${{{n-3}!}}$",
f"${{{n+1}!}}$",
	f"${{{n+3}!}}$"]

	kq2,kq3,kq4=random.sample(kqs,3)

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an




#[D10_C8_B2_28]-M1. Có bn số có n chữ số khác nhau từ n chữ số (không có chữ số 0)	
def mcn__L10_C8_B2_28(): 
	n=random.randint(4,9)
	noi_dung=f" Có bao nhiêu số tự nhiên có ${{{n}}}$ chữ số khác nhau được lập từ ${{{n}}}$ chữ số ${{1;2;...;{n}}}$ ."
	noi_dung_loigiai=f" Có ${{{n}}}!$ số tự nhiên có ${{{n}}}$ chữ số khác nhau được lập từ ${{{n}}}$ chữ số ${{1;2;...;{n}}}$ "

	kq=f"${{{n}!}}$"
	kqs=[f"${{{n-1}!}}$",
	f"${{{n-2}!}}$",
	f"${{{n+2}!}}$",
f"${{{n-3}!}}$",
f"${{{n+1}!}}$",
	f"${{{n+3}!}}$"]

	kq2,kq3,kq4=random.sample(kqs,3)

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an





#[D10_C8_B2_29]-M2. Có bn số có n chữ số khác nhau tạo từ n chữ số (có chữ số 0)	
def mcn__L10_C8_B2_29(): 
	n=random.randint(4,9)
	noi_dung=f" Có bao nhiêu số tự nhiên có ${{{n}}}$ chữ số khác nhau được lập từ ${{{n}}}$ chữ số ${{0;1;...;{n-1}}}$ ."
	noi_dung_loigiai=(f" Có ${{{n}!}}$ số có ${{{n}}}$ chữ số khác nhau được lập từ ${{{n}}}$ chữ số trên tính cả chữ số ${{0}}$ đứng đầu \n\n"
					f" Xét các số có  ${{{n}}}$ chữ số khác nhau được lập từ ${{{n}}}$ chữ số trên với chữ số ${{0}}$ đứng đầu thì có ${{{n-1}}}!$ \n\n"
					f" Vậy có ${{{n}!-{n-1}!}}$  số tự nhiên có ${{{n}}}$ chữ số khác nhau được lập từ ${{{n}}}$ chữ số ${{0;1;...;{n-1}}}$")

	kq=f"${{{n}!-{n-1}!}}$"
	kqs=[f"${{{n}!}}$",
	f"${{{n-1}!}}$",
	f"${{{n}!-{n-2}!}}$",
f"${{{n-1}!-{n-2}!}}$",
f"${{{n+1}!-{n-1}!}}$",
	f"${{{n+1}!-{n}!}}$"]

	kq2,kq3,kq4=random.sample(kqs,3)

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an





#[D10_C8_B2_30]-M2. Tính số vecto tạo từ n điểm phân biệt
def mcn__L10_C8_B2_30(): 
	n=random.randint(20,100)
	noi_dung=f" Có bao nhiêu vectơ khác vectơ không được tạo từ ${{{n}}}$ điểm phân biệt trong mặt phẳng."
	noi_dung_loigiai=f" Có $A_{{{n}}}^{{2}}$ vectơ khác vectơ không được tạo từ ${{{n}}}$ điểm phân biệt trong mặt phẳng "
					

	kq=f"$A_{{{n}}}^{{2}}$"
	kqs=[f"${{{n}!}}$",
	f"$A_{{{n}}}^{{{n-1}}}$",
	f"$C_{{{n}}}^{{2}}$",
f"${{{n-1}!}}$",
f"${{{n+1}!}}$",
	f"${{{n+1}!-{n}!}}$"]

	kq2,kq3,kq4=random.sample(kqs,3)

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

def phan_so(t):
    m=latex(Rational(t).limit_denominator(1000000000))
    return m


#[D10_C8_B2_31]-M2. Số tam giác được tạo từ các điểm trên 2 đường thẳng song song
def mcn__L10_C8_B2_31(): 
	n=random.randint(10,20)
	m=random.choice([i for i in range(10,20) if i!=n])
	a= binomial(n,2)*m+ binomial(m,2)*n
	noi_dung=f"Cho hai đường thẳng ${{(d)}}$ và ${{(d')}}$ song song với nhau, trên đường thẳng ${{(d)}}$ có ${{{n}}}$ điểm phân biệt, trên đường thẳng ${{(d')}}$ có ${{{m}}}$ điểm phân biệt. Hỏi có thể tạo ra bao nhiêu tam giác có đỉnh là các điểm thuộc ${{(d)}}$ và ${{(d')}}$ ?"
	noi_dung_loigiai=(f" Lấy ${{2}}$ điểm thuộc ${{(d)}}$ và ${{1}}$ điểm thuộc ${{(d')}}$ taọ được $C_{{{n}}}^{{2}} C_{{{m}}}^{{1}}$ tam giác \n\n"
					f" Lấy ${{2}}$ điểm thuộc ${{(d')}}$ và ${{1}}$ điểm thuộc ${{(d)}}$ taọ được $C_{{{m}}}^{{2}} C_{{{n}}}^{{1}}$ tam giác \n\n"
						f" Vậy số tam giác được tạo ra là $C_{{{n}}}^{{2}} C_{{{m}}}^{{1}} +C_{{{m}}}^{{2}} C_{{{n}}}^{{1}}= {phan_so(a)} $ tam giác")
	kq=f"${{{phan_so(a)}}}$"
	kqs=[f"${{{phan_so(a+1)}}}$",
	f"${{{phan_so(a-1)}}}$",
	f"${{{phan_so(a+2)}}}$",
f"${{{phan_so(a-2)}}}$",
f"${{{phan_so(a+3)}}}$",
	f"${{{phan_so(a-3)}}}$"]

	kq2,kq3,kq4=random.sample(kqs,3)

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an









#[L10_C8_B2_32]-M2. Các btoán chọn k người thoả dk nào đó
def mcn__L10_C8_B2_32(): 
	k1=random.randint(1,3)
	k2=random.randint(1,4)
	k=k1+k2
	a1=k+random.randint(2,6)
	a2=k+random.randint(2,8)
	a= binomial(a1,k1)* binomial(a2,k2)
	noi_dung = f"Một đội có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ. Có bao nhiêu cách để chọn được ${{{k}}}$ bạn trong đó có ${{{k1}}}$ nam và ${{{k2}}}$ nữ."		

	noi_dung_loigiai=(f"Số cách chọn ${{{k1}}}$ nam là $C_{{{a1}}}^{{{k1}}}$\n\n"
					f"Số cách chọn ${{{k2}}}$ nữ là $C_{{{a2}}}^{{{k2}}}$ \n\n"
						f" Vậy số cách chọn ${{{k1}}}$ nam và ${{{k2}}}$ nữ là $C_{{{a1}}}^{{{k1}}} C_{{{a2}}}^{{{k2}}}= {phan_so(a)} $")

	kq=f"${{{phan_so(a)}}}$"
	kqs=[f"${{{phan_so(a+1)}}}$",
	f"${{{phan_so(a-1)}}}$",
	f"${{{phan_so(a+2)}}}$",
f"${{{phan_so(a-2)}}}$",
f"${{{phan_so(a+3)}}}$",
	f"${{{phan_so(a-3)}}}$"]

	kq2,kq3,kq4=random.sample(kqs,3)

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an









#[D10_C8_B2_33]-M2. Các btoán chọn k bi(cầu) đủ các màu
def mcn__L10_C8_B2_33(): 
	v=random.choice([" viên bi", "quả cầu"])
	mau=["xanh","đỏ", "tím ", "vàng", "trắng", "đen", "nâu", "xám"]
	x,d,t=random.sample(mau,3)
	chon =random.randint(1,2)
	if chon ==1:
		k=3
		a1=k+random.randint(2,6)
		a2=k+random.randint(2,8)
		a3=k+random.randint(2,8)
		a= a1*a2*a3
		noi_dung = f"Một hộp có ${{{a1}}}$ {v} {x}; ${{{a2}}}$ {v} {d} và ${{{a3}}}$ {v} {t}. Có bao nhiêu cách để chọn được ${{{k}}}$ {v} đủ ba màu."		

		noi_dung_loigiai=(f"Số cách chọn ${{1}}$ {v} {x} là $C_{{{a1}}}^{{1}}$\n\n"
						f"Số cách chọn ${{1}}$ {v} {d} là $C_{{{a2}}}^{{1}}$ \n\n"
						f"Số cách chọn ${{1}}$ {v} {t} là $C_{{{a3}}}^{{1}}$ \n\n"
							f" Vậy số cách chọn ${{{k}}}$ {v} đủ ba màu là $C_{{{a1}}}^{{1}} C_{{{a2}}}^{{2}} C_{{{a3}}}^{{1}}= {phan_so(a)} $")

	if chon ==2:
		k=4
		a1=k+random.randint(2,6)
		a2=k+random.randint(2,8)
		a3=k+random.randint(2,8)
		a= binomial(a1,1)* binomial(a2,1)*binomial(a3,2)+binomial(a1,2)* binomial(a2,1)*binomial(a3,1)+binomial(a1,1)* binomial(a2,2)*binomial(a3,1)
		noi_dung = f"Một hộp có ${{{a1}}}$ {v} {x}; ${{{a2}}}$ {v} {d} và ${{{a3}}}$ {v} {t}. Có bao nhiêu cách để chọn được ${{{k}}}$ {v} đủ ba màu."		

		noi_dung_loigiai=(f"Số cách chọn ${{1}}$ {v} {x}, ${{1}}$ {v} {d}, ${{2}}$ {v} {t}  là $C_{{{a1}}}^{{1}}C_{{{a2}}}^{{1}}C_{{{a3}}}^{{2}}$\n\n"
						f"Số cách chọn ${{1}}$ {v} {x}, ${{2}}$ {v} {d}, ${{1}}$ {v} {t} là $C_{{{a1}}}^{{1}}C_{{{a2}}}^{{2}}C_{{{a3}}}^{{1}}$ \n\n"
						f"Số cách chọn ${{2}}$ {v} {x}, ${{1}}$ {v} {d}, ${{1}}$ {v} {t} là $C_{{{a1}}}^{{2}}C_{{{a2}}}^{{1}}C_{{{a3}}}^{{1}}$ \n\n"
							f" Vậy số cách chọn ${{{k}}}$ {v} đủ ba màu là ${{ {phan_so(a)} }}$")


	kq=f"${{{phan_so(a)}}}$"
	kqs=[f"${{{phan_so(a+1)}}}$",
	f"${{{phan_so(a-1)}}}$",
	f"${{{phan_so(a+2)}}}$",
f"${{{phan_so(a-2)}}}$",
f"${{{phan_so(a+3)}}}$",
	f"${{{phan_so(a-3)}}}$"]

	kq2,kq3,kq4=random.sample(kqs,3)

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an











#[D10_C8_B2_34]-TF-M3. Cho m nam, n nữ trong đó có bạn A. Xét ĐS
def mcn__L10_C8_B2_34(): 
	k1=random.randint(1,3)
	k2=random.randint(1,4)
	k=k1+k2
	a1=k+random.randint(2,6)
	a2=k+random.randint(2,8)
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])	
	noi_dung = f"Một đội có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	c= binomial(a1+a2,k)
        
	kq1_T=f"*Số cách chọn ra ${{{k}}}$ bạn bất kì trong đội là ${{{phan_so(c)}}}$" 
	kq1_F=f"Số cách chọn ra ${{{k}}}$ bạn bất kì trong đội là  "
	kq1_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Số cách chọn ra ${{{k}}}$ bạn bất kì trong đội là ${{C^{{{k}}}_{{{a1+a2}}}={phan_so(c)}}}$ "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c= binomial(a1,k1)* binomial(a2,k2)
	kq2_T=f"*Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đội là ${{{phan_so(c)}}}$ "
	kq2_F=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đội là "

	kq2_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đội là ${{C^{{{k1}}}_{{{a1}}}\\cdot C^{{{k2}}}_{{{a2}}}={phan_so(c)}}}$"



	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c= binomial(a1+a2-1,k-1)
	kq3_T=f"* Số cách chọn ra ${{{k}}}$ bạn trong đó có bạn {B} là ${{{phan_so(c)}}}$ " 
	kq3_F=f"Số cách chọn ra ${{{k}}}$ bạn trong đó có bạn {B} là "
	kq3_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Số cách chọn ra ${{{k}}}$ bạn trong đó có bạn {B} là ${{C^{{{k-1}}}_{{{a1+a2-1}}}={phan_so(c)} }} $"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c= binomial(a1-1,k1-1)* binomial(a2,k2)
	kq4_T=f"*Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó có {B} là ${{{phan_so(c)}}}$  "
	kq4_F=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó có {B} là " 
	kq4_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó có {B} là ${{C^{{{k1-1}}}_{{{a1-1}}}\\cdot C^{{{k2}}}_{{{a2}}}={phan_so(c)}}}$"
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an








#[D10_C8_B2_35]-TF-M3. Cho m nam, n nữ trong đó có bạn nam A và nữ B. Xét ĐS
def mcn__L10_C8_B2_35(): 
	k1=random.randint(1,3)
	k2=random.randint(1,4)
	k=k1+k2
	a1=k+random.randint(2,6)
	a2=k+random.randint(2,8)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])	
	noi_dung = f"Một đội có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} và bạn nữ tên {A}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"

	c= binomial(a1+a2-2,k-2)
        
	kq1_T=f"*Số cách chọn ra ${{{k}}}$ bạn trong đội trong đó có cả {A} và {B} là ${{{phan_so(c)}}}$" 
	kq1_F=f"Số cách chọn ra ${{{k}}}$ bạn trong đội trong đó có cả {A} và {B} là  "
	kq1_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Số cách chọn ra ${{{k}}}$ bạn trong đó có cả {A} và {B} là ${{C^{{{k-2}}}_{{{a1+a2-2}}}={phan_so(c)}}}$ "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c= binomial(a1,k1)* binomial(a2-1,k2)
	kq2_T=f"*Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó không có {A} là ${{{phan_so(c)}}}$ "
	kq2_F=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó không có {A} là "

	kq2_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó không có {A} là ${{C^{{{k1}}}_{{{a1}}}\\cdot C^{{{k2-1}}}_{{{a2-1}}}={phan_so(c)}}}$"



	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c= binomial(a1+a2-2,k-1)
	kq3_T=f"* Số cách chọn ra ${{{k}}}$ bạn trong đó có bạn {B} mà không có bạn {A} là ${{{phan_so(c)}}}$ " 
	kq3_F=f"Số cách chọn ra ${{{k}}}$ bạn trong đó có bạn {B} mà không có bạn {A} là "
	kq3_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Số cách chọn ra ${{{k}}}$ bạn trong đó có bạn {B} mà không có bạn {A} là ${{C^{{{k-1}}}_{{{a1+a2-2}}}={phan_so(c)} }} $"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c= binomial(a1-1,k1-1)* binomial(a2-1,k2)+binomial(a1-1,k1)* binomial(a2-1,k2-1)+binomial(a1-1,k1)* binomial(a2-1,k2)
	kq4_T=f"*Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó {B} và {A} không đồng thời cùng có mặt là ${{{phan_so(c)}}}$  "
	kq4_F=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó {B} và {A} không đồng thời cùng có mặt là " 
	kq4_F +=random.choice([
                f"${{{c - 1}}}$", 
                f"${{{c + random.randint(6, 7)}}}$  ", 
                f"${{{c + random.randint(1, 3)}}}$ ", 
                f"${{{c + random.randint(4, 5)}}}$ "])
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó {B} và {A} không đồng thời cùng có mặt là \n\n ${{C^{{{k1-1}}}_{{{a1-1}}}\\cdot C^{{{k2}}}_{{{a2-1}}}+C^{{{k1}}}_{{{a1-1}}}\\cdot C^{{{k2-1}}}_{{{a2-1}}}+C^{{{k1}}}_{{{a1-1}}}\\cdot C^{{{k2}}}_{{{a2-1}}} ={phan_so(c)}}}$"
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an









#[D10_C8_B2_36]-SA-M3. Cho m nam, n nữ, chọn k bạn trong đó A, B không cùng có mặt.
def mcn__L10_C8_B2_36(): 
	k1=random.randint(2,4)
	k2=random.randint(2,4)
	k=k1+k2
	a1=k+random.randint(2,6)
	a2=k+random.randint(2,6)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	c= binomial(a1-1,k1-1)* binomial(a2-1,k2)+binomial(a1-1,k1)* binomial(a2-1,k2-1)+binomial(a1-1,k1)* binomial(a2-1,k2)
	kq=tinh_tong_chu_so(c)
	noi_dung = f"Một đội có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} và bạn nữ tên {A}. Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó {B} và {A} không đồng thời cùng có mặt là ${{m}}$. Tổng các chữ số của ${{m}}$ là "		
	noi_dung_loigiai=(f" TH1: Có {B} mà không có {A} thì có ${{C^{{{k1-1}}}_{{{a1-1}}}\\cdot C^{{{k2}}}_{{{a2-1}}} }}$ cách chọn \n\n"
					f" TH2: Có {A} mà không có {B} thì có ${{C^{{{k1}}}_{{{a1-1}}}\\cdot C^{{{k2-1}}}_{{{a2-1}}} }} $ cách chọn \n\n"
					f" TH3: Không có cả {A} và {B} là ${{C^{{{k1}}}_{{{a1-1}}}\\cdot C^{{{k2}}}_{{{a2-1}}} }}$ cách chọn \n\n"
	f"Số cách chọn ra ${{{k1}}}$ bạn nam và ${{{k2}}}$ bạn nữ trong đó {B} và {A} không đồng thời cùng có mặt là \n\n ${{m= C^{{{k1-1}}}_{{{a1-1}}}\\cdot C^{{{k2}}}_{{{a2-1}}}+C^{{{k1}}}_{{{a1-1}}}\\cdot C^{{{k2-1}}}_{{{a2-1}}}+C^{{{k1}}}_{{{a1-1}}}\\cdot C^{{{k2}}}_{{{a2-1}}} ={phan_so(c)}}}$ cách chọn\n\n"
	f"Tổng các chữ số của ${{m}}$ là ${{{kq}}}$ "
	)
	debai_word= f"{noi_dung}\n"


	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C8_B2_37]-SA-M3. Xếp m nam, n nữ sao cho bạn nam A luôn giữa 2 bạn nữ.
def mcn__L10_C8_B2_37(): 

	a1=random.randint(3,6)
	a2=random.randint(3,6)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	m= (a1+a2-2)*a2*(a2-1)*factorial(a1+a2-3)
	kq=tinh_tong_chu_so(m)
	noi_dung = f"Có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B}. Xếp các bạn thành một hàng ngang. Số cách xếp bạn {B} luôn đứng giữa hai bạn nữ là ${{m}}$. Tổng các chữ số của ${{m}}$ là "		
	noi_dung_loigiai=(f" Xếp bạn {B} có ${{{a1+a2-2}}}$ cách \n\n"
					f" Xếp bạn nữ đứng trước {B} có ${{{a2}}}$ cách \n\n"
					f" Xếp bạn nữ đứng sau {B} có ${{{a2-1}}}$ cách\n\n"
					f" Xếp các bạn còn lại có ${{{a1+a2-3}!}}$ cách \n\n"
					f" Theo quy tắc nhân có $  {{{a1+a2-2} \\cdot {a2} \\cdot {a2-1} \\cdot  {a1+a2-3}!= {(a1+a2-2)*a2*(a2-1)*factorial(a1+a2-3)} }}   $ cách xếp \n\n"
	f"Tổng các chữ số của ${{m}}$ là ${{{kq}}}$ "
	)
	debai_word= f"{noi_dung}\n"


	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C8_B2_38]-SA-M3. Xếp m nam, n nữ sao cho bạn nam (nữ) luôn cạnh nhau.
def mcn__L10_C8_B2_38(): 
	gt=["nam", "nữ" ]
	nam, nữ=random.sample(gt, 2)
	a1=random.randint(3,7)
	a2=random.randint(3,7)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	m= factorial(a1)*factorial(a2+1)
	kq=tinh_tong_chu_so(m)
	noi_dung = f"Có ${{{a1}}}$ bạn {nam} và ${{{a2}}}$ bạn {nữ}. Số cách xếp các bạn thành một hàng ngang sao cho các bạn {nam} luôn đứng cạnh nhau là ${{m}}$. Tổng các chữ số của ${{m}}$ là "		
	noi_dung_loigiai=(f" Coi các bạn {nam} là 1 kết hợp với  ${{{a2}}}$ bạn {nữ} có ${{{a2+1}!}}$ cách xếp \n\n"
					f" Xếp riêng nhóm các bạn {nam} có ${{{a1}!}}$ cách \n\n"
					
					f" Theo quy tắc nhân có $  {{{a1}! \\cdot {a2+1}!= {factorial(a1)*factorial(a2+1)} }} $ cách xếp \n\n "
	f"Tổng các chữ số của ${{m}}$ là ${{{kq}}}$ "
	)
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an


#[D10_C8_B2_39]-SA-M2. Xếp m nam, n nữ sao cho bạn nam A không đứng đầu(cuối).
def mcn__L10_C8_B2_39(): 
	vt=random.choice(["đầu", "cuối"])
	ngang=random.choice(["ngang", "dọc"])
	a1=random.randint(3,5)
	a2=random.randint(3,5)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	m= (a1+a2-1)*factorial(a1+a2-1)
	kq=tinh_tong_chu_so(m)
	noi_dung = f"Có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B}. Xếp các bạn thành một hàng {ngang}. Số cách xếp bạn {B} không đứng {vt} hàng là ${{m}}$. Tổng các chữ số của ${{m}}$ là "		
	noi_dung_loigiai=(f" Xếp bạn {B} có ${{{a1+a2-1}}}$ cách \n\n"
					f" Xếp các bạn còn lại có ${{{a1+a2-1}!}}$ cách \n\n"
					f" Theo quy tắc nhân có $  {{{a1+a2-1} \\cdot {a1+a2-1}!= {(a1+a2-1)*factorial(a1+a2-1)} }}   $ cách xếp \n\n"
	f"Tổng các chữ số của ${{m}}$ là ${{{kq}}}$ "
	)
	debai_word= f"{noi_dung}\n"


	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C8_B2_40]-SA-M2. Xếp m nam, m nữ sao cho nam nữ xen kẽ.
def mcn__L10_C8_B2_40(): 
	vt=random.choice(["đầu", "cuối"])
	ngang=random.choice(["ngang", "dọc"])
	a1=random.randint(3,7)
	a2=random.randint(3,7)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	m= factorial(a1)*factorial(a1)*2
	kq=tinh_tong_chu_so(m)
	noi_dung = f"Có ${{{a1}}}$ bạn nam và ${{{a1}}}$ bạn nữ trong đó có bạn nam tên {B}. Xếp các bạn thành một hàng {ngang}. Số cách xếp sao cho nam nữ xen kẽ là ${{m}}$. Tổng các chữ số của ${{m}}$ là "		
	noi_dung_loigiai=(f" TH1: nam đứng đầu có ${{{a1}!{a1}! }}$ cách \n\n"
					f" TH2: nữ đứng đầu có ${{{a1}!{a1}! }}$ cách\n\n"
					f" Theo quy tắc cộng có $  {{{a1}!{a1}!+ {a1}!{a1}!= {factorial(a1)*factorial(a1)*2} }}   $ cách xếp \n\n"
	f"Tổng các chữ số của ${{m}}$ là ${{{kq}}}$ "
	)
	debai_word= f"{noi_dung}\n"


	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an







#[D10_C8_B2_41]-TF-M2. Xếp m nam, m nữ thoả các dk. Xét tính ĐS
def mcn__L10_C8_B2_41():
	a1=random.randint(5,10)
	a2=a1 
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	noi_dung = f"Có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} bạn nữ tên {A}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	doc=random.choice(["ngang", "dọc"])

	chon =random.randint(1,2)
	if chon==1:
		kq1_T=f"*Có ${{{a1+a2}!}}$ cách xếp các bạn trên thành một hàng {doc}" 
		kq1_F=f"Có ${{{a1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} "
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Có ${{{a1+a2}!}}$ cách xếp các bạn trên thành một hàng {doc} "
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon==2:
		vt=["đầu", "cuối"]
		dau, cuoi =random.sample(vt,2)
		kq1_T=f"*Có ${{{a1+a2-2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} đứng {dau} và {B} đứng {cuoi}" 
		kq1_F=f"Có ${{{a1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} đứng {dau} và {B} đứng {cuoi} "
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Có ${{{a1+a2-2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} đứng {dau} và {B} đứng {cuoi}"
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon =random.randint(1,2)
	if chon ==1:

		kq2_T=f"*Có ${{2 \\cdot {a1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho nam nữ xen kẽ "
		kq2_F=f"Có ${{{a1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho nam nữ xen kẽ  "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Có ${{2 \\cdot {a1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho nam nữ xen kẽ "
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon ==2:
		nữ=random.choice(["nữ", "nam"])

		kq2_T=f"*Có ${{ {a1+1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho các bạn {nữ} luôn đứng cạnh nhau "
		kq2_F=f"Có ${{{a1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho các bạn {nữ} luôn đứng cạnh nhau  "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Có ${{ {a1+1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho các bạn {nữ} luôn đứng cạnh nhau "
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon ==1:
		kq3_T=f"*Có ${{2\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} luôn đứng cạnh nhau " 
		kq3_F=f"Có ${{{a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} luôn đứng cạnh nhau  "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Có ${{2\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} luôn đứng cạnh nhau "
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	if chon ==2:
		kq3_T=f"*Có ${{{a1+a2}!-2\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} không đứng cạnh nhau " 
		kq3_F=f"Có ${{2\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} không đứng cạnh nhau  "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Có ${{{a1+a2}!-2\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} không đứng cạnh nhau"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	chon=random.randint(1,2)
	if chon ==1:

		kq4_T=f"*Có ${{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-3}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nam "
		kq4_F=f"Có ${{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nam " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Có ${{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-3}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nam"
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon ==2:

		kq4_T=f"*Có ${{{(a1+a2-2)*(a1-1)*(a1-2)}\\cdot {a1+a2-3}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nữ "
		kq4_F=f"Có ${{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-3}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nữ " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Có ${{{(a1+a2-2)*(a1-1)*(a1-2)}\\cdot {a1+a2-3}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nữ"
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an







#[D10_C8_B2_42]-TF-M3. Có m nam, n nữ, chọn k bạn thoả các dk. Xét tính ĐS
def mcn__L10_C8_B2_42():
	k=random.randint(2,5)
	i=random.randint(2,5)
	a1=i+random.randint(3,10)
	a2=k+random.randint(3,10)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	noi_dung = f"Một nhóm có ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} bạn nữ tên {A}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	doc=random.choice(["ngang", "dọc"])

	chon =random.randint(1,2)
	if chon==1:
		kq1_T=f"*Có ${{C^{{{k}}}_{{{a1+a2}}}}}$ cách chọn ra ${{{k}}}$ bạn từ nhóm bạn trên" 
		kq1_F=f"*Có ${{A^{{{k}}}_{{{a1+a2}}}}}$ cách chọn ra ${{{k}}}$ bạn từ nhóm bạn trên"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"*Có ${{C^{{{k}}}_{{{a1+a2}}} }}$ cách chọn ra ${{{k}}}$ bạn từ nhóm bạn trên"
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon==2:
		vt=["đầu", "cuối"]
		dau, cuoi =random.sample(vt,2)
		kq1_T=f"*Có ${{C^{{{k}}}_{{{a2}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ từ nhóm bạn trên" 
		kq1_F=f"Có ${{C^{{{k}}}_{{{a2+a1}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ từ nhóm bạn trên"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Có ${{C^{{{k}}}_{{{a2}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ từ nhóm bạn trên"
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon =random.randint(1,2)
	if chon ==1:

		kq2_T=f"*Có ${{C^{{{k}}}_{{{a2}}} \\cdot C^{{{i}}}_{{{a1}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ và ${{{i}}}$ bạn nam từ nhóm bạn trên"
		kq2_F=f"Có ${{C^{{{k}}}_{{{a2+a1}}} \\cdot C^{{{i}}}_{{{a1+a2}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ và ${{{i}}}$ bạn nam từ nhóm bạn trên"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Có ${{C^{{{k}}}_{{{a2}}} \\cdot C^{{{i}}}_{{{a1}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ và ${{{i}}}$ bạn nam từ nhóm bạn trên "
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon ==2:
		nữ=random.choice(["nữ", "nam"])

		kq2_T=f"*Có ${{C^{{{k}}}_{{{a2}}} \\cdot C^{{{i}}}_{{{a1}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ và ${{{i}}}$ bạn nam từ nhóm bạn trên "
		kq2_F=f"Có ${{A^{{{k}}}_{{{a2}}} \\cdot A^{{{i}}}_{{{a1}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ và ${{{i}}}$ bạn nam từ nhóm bạn trên "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Có ${{C^{{{k}}}_{{{a2}}} \\cdot C^{{{i}}}_{{{a1}}}}}$ cách chọn ra ${{{k}}}$ bạn nữ và ${{{i}}}$ bạn nam từ nhóm bạn trên "
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon ==1:
		kq3_T=f"*Có ${{A^{{2}}_{{{a2+a1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm  " 
		kq3_F=f"Có ${{C^{{2}}_{{{a2+a1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm  "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Có ${{A^{{2}}_{{{a2+a1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	if chon ==2:
		kq3_T=f"*Có ${{A^{{3}}_{{{a2+a1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên  " 
		kq3_F=f"Có ${{C^{{3}}_{{{a2+a1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên  "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Có ${{A^{{3}}_{{{a2+a1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên  "
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	chon=random.randint(1,2)
	if chon ==1:

		kq4_T=f"*Có ${{3 \\cdot A^{{2}}_{{{a2+a1-1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên trong đó {A} có giữ một chức vụ nào đó"
		kq4_F=f"Có ${{A^{{3}}_{{{a2+a1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên trong đó {A} có giữ một chức vụ nào đó" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Có ${{3 \\cdot A^{{2}}_{{{a2+a1-1}}} }}$ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên trong đó {A} có giữ một chức vụ nào đó"
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon ==2:

		kq4_T=f"*Có ${{{phan_so(6*(a2+a1-2))}}} $ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên trong đó {A} và {B} đều giữ các chức vụ "
		kq4_F=f"Có ${{{phan_so(6*(a2+a1-2)+random.randint(1,10))}}} $ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên trong đó {A} và {B} đều giữ các chức vụ  " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Có ${{{phan_so(6*(a2+a1-2))}}} $ cách chọn ra một bạn giữ vị trí trưởng nhóm, một bạn giữ vị trí phó nhóm, một bạn uỷ viên trong đó {A} và {B} đều giữ các chức vụ "
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an





#[D10_C8_B2_43]-SA-M3. Tạo các số có các chữ số tăng (giảm) dần
def mcn__L10_C8_B2_43(): 
	chon =random.randint(1,6)

	if chon ==1:
		l=random.randint(3,5)
		kq = binomial(6,l)
		a1,a2,a3,a4,a5,a6=random.sample(range(1,9),6)
		noi_dung=f" Từ các chữ số ${{0; {a1}; {a2}; {a3}; {a4}; {a5}; {a6} }}$ lập được bao nhiêu số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau mà các chữ số tăng dần. "

		noi_dung_loigiai=(f"Một tổ hợp gồm ${{{l}}}$ chữ số chỉ tạo ra được một số thoả mãn yêu cầu \n\n"
		f" Do đó lập được ${{C^{{{l}}}_{{6}}={kq}}}$ số thoả mãn yêu cầu.")



	if chon ==2:
		l=random.randint(3,6)
		kq = binomial(8,l)
		a1,a2,a3,a4,a5,a6,a7,a8=random.sample(range(1,9),8)
		noi_dung=f" Từ các chữ số ${{0; {a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7};{a8} }}$ lập được bao nhiêu số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau mà các chữ số tăng dần. "

		noi_dung_loigiai=(f"Một tổ hợp gồm ${{{l}}}$ chữ số chỉ tạo ra được một số thoả mãn yêu cầu \n\n"
		f" Do đó lập được ${{C^{{{l}}}_{{8}}={kq}}}$ số thoả mãn yêu cầu.")

	if chon ==3:
		l=random.randint(3,6)
		kq = binomial(7,l)
		a1,a2,a3,a4,a5,a6,a7=random.sample(range(1,9),7)
		noi_dung=f" Từ các chữ số ${{0; {a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7} }}$ lập được bao nhiêu số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau mà các chữ số tăng dần. "

		noi_dung_loigiai=(f"Một tổ hợp gồm ${{{l}}}$ chữ số chỉ tạo ra được một số thoả mãn yêu cầu \n\n"
		f" Do đó lập được ${{C^{{{l}}}_{{7}}={kq}}}$ số thoả mãn yêu cầu.")



	if chon ==6:
		l=random.randint(3,6)
		kq = binomial(7,l)
		a1,a2,a3,a4,a5,a6,a7=random.sample(range(0,9),7)
		noi_dung=f" Từ các chữ số ${{ {a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7} }}$ lập được bao nhiêu số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau mà các chữ số giảm dần. "
		noi_dung_loigiai=(f"Một tổ hợp gồm bốn chữ số chỉ tạo ra được một số thoả mãn yêu cầu \n\n"
		f" Do đó lập được ${{C^{{{l}}}_{{7}}={kq}}}$ số thoả mãn yêu cầu.")

	if chon ==4:
		l=random.randint(3,8)
		kq = binomial(9,l)
		a1,a2,a3,a4,a5,a6,a7,a8,a9=random.sample(range(0,9),9)
		noi_dung=f" Từ các chữ số ${{ {a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7}; {a8}; {a9} }}$ lập được bao nhiêu số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau mà các chữ số giảm dần. "
		noi_dung_loigiai=(f"Một tổ hợp gồm bốn chữ số chỉ tạo ra được một số thoả mãn yêu cầu \n\n"
		f" Do đó lập được ${{C^{{{l}}}_{{9}}={kq}}}$ số thoả mãn yêu cầu.")

	if chon ==5:
		l=random.randint(3,7)
		kq = binomial(8,l)
		a1,a2,a3,a4,a5,a6,a7,a8=random.sample(range(0,9),8)
		noi_dung=f" Từ các chữ số ${{ {a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7}; {a8}}}$ lập được bao nhiêu số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau mà các chữ số giảm dần. "
		noi_dung_loigiai=(f"Một tổ hợp gồm bốn chữ số chỉ tạo ra được một số thoả mãn yêu cầu \n\n"
		f" Do đó lập được ${{C^{{{l}}}_{{8}}={kq}}}$ số thoả mãn yêu cầu.")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an



#[D10_C8_B2_44]-SA-M4. Có bao nhiêu cách chia m kẹo cho n em.
def mcn__L10_C8_B2_44(): 
	n=random.randint(3,7)
	m=n+random.randint(2,8)

	kq=binomial(m-1,n-1)
	noi_dung=f" Có bao nhiêu cách chia ${{{m}}}$ chiếc kẹo cho ${{{n}}}$ em học sinh sao cho em nào cũng có ít nhất một kẹo?"
	noi_dung_loigiai=(f"Rải ${{{m}}}$ chiếc kẹo lên mặt bàn tạo ra ${{{m-1}}}$ vách ngăn, chọn ra ${{{n-1}}}$ vách ngăn để đặt cách thanh gỗ ngăn cách, giữ đúng thứ tự đó để chia kẹo cho các em cũng theo thứ tự.\n\n"
	f" Một cách làm như trên là một cách chia kẹo \n\n"
	f" Vậy có ${{C^{{{n-1}}}_{{{m-1}}}={kq}}}$ cách chia kẹo")


	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an



#[D10_C8_B2_45]-SA-M4. Số nghiệm nguyên dương của phương trình bậc nhất nhiều ẩn
def mcn__L10_C8_B2_45(): 
	chon =random.randint(1,2)
	if chon ==1:
		n=3
		m=random.randint(10,131)

		kq=binomial(m-1,n-1)

		noi_dung=f"Phương trình ${{x+y+z={m}}}$ có bao nhiêu nghiệm nguyên dương."
		noi_dung_loigiai=(f" Nghiệm của phương trình là một bộ ba số ${{(x;y;z)}}$ với $x;y;z \\ge 1; x;y;z \\in \\mathbb{{N}}$\n\n"
			f"Viết ${{{m}}}$ số ${{1}}$ lên giấy tạo ra ${{{m-1}}}$ vách ngăn giữa cách số ${{1}}$, chọn ra ${{{n-1}}}$ vách ngăn để đặt cách gạch sọc ngăn cách, giữ đúng thứ tự đó ta sẽ được một nghiệm của phương trình.\n\n"
		f" Vậy phương trình có ${{C^{{{n-1}}}_{{{m-1}}}={kq}}}$ nghiệm")
	if chon ==2:
		n=4
		m=random.randint(10,22)

		kq=binomial(m-1,n-1)

		noi_dung=f"Phương trình ${{x+y+z+t={m}}}$ có bao nhiêu nghiệm nguyên dương."
		noi_dung_loigiai=(f" Nghiệm của phương trình là một bộ ba số ${{(x;y;z;t)}}$ với $x;y;z;t \\ge 1; x;y;z;t \\in \\mathbb{{N}}$\n\n"
			f"Viết ${{{m}}}$ số ${{1}}$ lên giấy tạo ra ${{{m-1}}}$ vách ngăn giữa cách số ${{1}}$, chọn ra ${{{n-1}}}$ vách ngăn để đặt cách gạch sọc ngăn cách, giữ đúng thứ tự đó ta sẽ được một nghiệm của phương trình.\n\n"
		f" Vậy phương trình có ${{C^{{{n-1}}}_{{{m-1}}}={kq}}}$ nghiệm")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an








#[D10_C8_B2_46]-TF-M3. Cho k vật từ một nhóm thoả điều kiện nào đó. Xét ĐS
def mcn__L10_C8_B2_46():
	a=random.choice([i for i in range(-10,10) if i!=0])
	k=random.randint(2,5)
	m=k+ random.randint(2,5)
	n=k+random.randint(2,5)
	p=k+random.randint(2,5)
	A=random.choice(["viên bi", "quả cầu"])
	mau=["xanh", "đỏ", "tím", "vàng", "trắng", "đen", "xám", "nâu"]
	x,d,t=random.sample(mau,3)
	noi_dung = f"Một hộp chứa ${{{m}}}$ {A} {x} khác nhau, ${{{n}}}$ {A} {d} khác nhau và ${{{p}}}$ {A} {t} khác nhau. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Có ${{C^{{{k}}}_{{{m+n+p}}}}}$ cách chọn ra ${{{k}}}$ {A} từ hộp " 
	kq1_F=f"Có ${{C^{{{k}}}_{{{m*n*p}}}}}$ cách chọn ra ${{{k}}}$ {A} từ hộp "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f" Có ${{C^{{{k}}}_{{{m+n+p}}}}}$ cách chọn ra ${{{k}}}$ {A} từ hộp"
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq=binomial(m,k)+binomial(n,k)+binomial(p,k)

	kq2_T=f"*Có ${{{kq}}}$ cách chọn ra ${{{k}}}$ {A} cùng màu "
	kq2_F=f"Có ${{{kq+random.randint(1,10)}}}$ cách chọn ra ${{{k}}}$ {A} cùng màu "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Có ${{C^{{{k}}}_{{{m}}}+C^{{{k}}}_{{{n}}}+C^{{{k}}}_{{{p}}}={kq} }}$ cách chọn ra ${{{k}}}$ {A} cùng màu "
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq=binomial(m,2)*binomial(n,1)*binomial(p,1)+binomial(m,1)*binomial(n,1)*binomial(p,2)+binomial(m,1)*binomial(n,2)*binomial(p,1)

	kq3_T=f"*Có ${{{kq}}}$ cách lấy ra ${{4}}$ {A} đủ cả ba màu " 
	kq3_F=f"Có ${{{kq+a}}}$ cách lấy ra ${{4}}$ {A} đủ cả ba màu "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Có ${{{kq}}}$ cách lấy ra ${{4}}$ {A} đủ cả ba màu "
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	kq=binomial(m+n+p,3)-m*n*p

	kq4_T=f"* Có ${{{kq}}}$ cách lấy ra ${{3}}$ {A} không có đủ cả ba màu"
	kq4_F=f"Có ${{{kq+a}}}$ cách lấy ra ${{3}}$ {A} không có đủ cả ba màu " 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Có ${{C^{{{3}}}_{{{m+n+p}}}-{m} \\cdot {n} \\cdot {p}= {kq}}}$ cách lấy ra ${{3}}$ {A} không có đủ cả ba màu"
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an





#[D10_C8_B2_47]-SA-M3. Tạo số có chữ số x có mặt k lần, chữ số y có mặt q lần
def mcn__L10_C8_B2_47(): 
	m=random.randint(2,4)
	n=random.randint(2,4)
	l=m+n+random.randint(2,3)
	chon =random.randint(1,4)
	if chon ==1:
		a1,a2,a3,a4,a5,a6,a7=random.sample(range(1,9),7)

		m1=binomial(l,m)*binomial(l-m,n)*chinh_hop(l-m-n,5)
		kq=tinh_tong_chu_so(m1)
		noi_dung=f" Từ các chữ số ${{ {a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7} }}$ lập được ${{m}}$ số tự nhiên có ${{{l}}}$ chữ số sao cho chữ số ${{{a1}}}$ có mặt đúng ${{{m}}}$ lần, chữ số ${{{a6}}}$ có mặt đúng ${{{n}}}$ lần các chữ số khác có mặt không quá một lần. Tổng các chữ số của ${{m}}$ là "
		noi_dung_loigiai=(f"Có $C^{{{m}}}_{{{l}}} $ cách xếp số ${{{a1}}}$\n\n  "
			f"Có $C^{{{n}}}_{{{l-m}}} $ cách xếp số ${{{a2}}}$\n\n  "
			f" Có $A^{{{l-m-n}}}_{{{5}}}$ cách tạo số cho ${{{l-m-n}}}$ vị trí còn lại\n\n"
			f"Theo quy tắc nhân có $C^{{{m}}}_{{{l}}} \\cdot C^{{{n}}}_{{{l-m}}} \\cdot A^{{{l-m-n}}}_{{{5}}}= {m1}$ số\n\n"
			f" Tổng các chữ số của ${{{m}}}$ là ${{{kq}}}$"
	)


	if chon ==2:
		a1,a2,a3,a4,a5,a6=random.sample(range(1,9),6)
		m1=binomial(l,m)*binomial(l-m,n)*chinh_hop(l-m-n,4)
		kq=tinh_tong_chu_so(m1)
		noi_dung=f" Từ các chữ số ${{ {a1}; {a2}; {a3}; {a4}; {a5}; {a6} }}$ lập được ${{m}}$ số tự nhiên có ${{{l}}}$ chữ số sao cho chữ số ${{{a1}}}$ có mặt đúng ${{{m}}}$ lần, chữ số ${{{a6}}}$ có mặt đúng ${{{n}}}$ lần các chữ số khác có mặt không quá một lần. Tổng các chữ số của ${{m}}$ là "
		noi_dung_loigiai=(f"Có $C^{{{m}}}_{{{l}}} $ cách xếp số ${{{a1}}}$\n\n  "
			f"Có $C^{{{n}}}_{{{l-m}}} $ cách xếp số ${{{a2}}}$\n\n  "
			f" Có $A^{{{l-m-n}}}_{{{4}}}$ cách tạo số cho ${{{l-m-n}}}$ vị trí còn lại\n\n"
			f"Theo quy tắc nhân có $C^{{{m}}}_{{{l}}} \\cdot C^{{{n}}}_{{{l-m}}} \\cdot A^{{{l-m-n}}}_{{{4}}}= {m1}$ số\n\n"
			f" Tổng các chữ số của ${{{m}}}$ là ${{{kq}}}$"
		)
	if chon ==3:
		m1=binomial(l-1,m)*binomial(l-m,n)*chinh_hop(l-m-n,5)
		kq=tinh_tong_chu_so(m1)
		a1,a2,a3,a4,a5,a6=random.sample(range(1,9),6)
		noi_dung=f" Từ các chữ số ${{0; {a1}; {a2}; {a3}; {a4}; {a5}; {a6} }}$ lập được ${{m}}$ số tự nhiên có ${{{l}}}$ chữ số sao cho chữ số ${{0}}$ có mặt đúng ${{{m}}}$ lần, chữ số ${{{a6}}}$ có mặt đúng ${{{n}}}$ lần các chữ số khác có mặt không quá một lần. Tổng các chữ số của ${{m}}$ là "
		noi_dung_loigiai=(f"Có $C^{{{m}}}_{{{l-1}}} $ cách xếp số ${{0}}$\n\n  "
			f"Có $C^{{{n}}}_{{{l-m}}} $ cách xếp số ${{{a2}}}$\n\n  "
			f" Có $A^{{{l-m-n}}}_{{{5}}}$ cách tạo số cho ${{{l-m-n}}}$ vị trí còn lại\n\n"
			f"Theo quy tắc nhân có $C^{{{m}}}_{{{l-1}}} \\cdot C^{{{n}}}_{{{l-m}}} \\cdot A^{{{l-m-n}}}_{{{5}}}= {m1}$ số\n\n"
			f" Tổng các chữ số của ${{{m}}}$ là ${{{kq}}}$"
		)
	if chon ==4:
		a1,a2,a3,a4,a5,a6,a7=random.sample(range(1,9),7)
		m=random.randint(2,3)
		n=random.randint(2,3)
		l=m+n+random.randint(2,4)
		m1=binomial(l-1,m)*binomial(l-m,n)*chinh_hop(l-m-n,6)
		kq=tinh_tong_chu_so(m1)

		noi_dung=f" Từ các chữ số ${{0; {a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7} }}$ lập được ${{m}}$ số tự nhiên có ${{{l}}}$ chữ số sao cho chữ số ${{{0}}}$ có mặt đúng ${{{m}}}$ lần, chữ số ${{{a6}}}$ có mặt đúng ${{{n}}}$ lần các chữ số khác có mặt không quá một lần. Tổng các chữ số của ${{m}}$ là "
		noi_dung_loigiai=(f"Có $C^{{{m}}}_{{{l-1}}} $ cách xếp số ${{{0}}}$\n\n  "
			f"Có $C^{{{n}}}_{{{l-m}}} $ cách xếp số ${{{a2}}}$\n\n  "
			f" Có $A^{{{l-m-n}}}_{{{6}}}$ cách tạo số cho ${{{l-m-n}}}$ vị trí còn lại\n\n"
			f"Theo quy tắc nhân có $C^{{{m}}}_{{{l-1}}} \\cdot C^{{{n}}}_{{{l-m}}} \\cdot A^{{{l-m-n}}}_{{{6}}}= {m1}$ số\n\n"
			f" Tổng các chữ số của ${{{m}}}$ là ${{{kq}}}$"
	)
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C8_B2_48]-TF-M3. Các bài toán tạo số.
def mcn__L10_C8_B2_48(): 
	a1,a2,a3,a4,a5,a6,a7=random.sample(range(1,9),7)

	noi_dung = f"Từ các chữ số ${{{a1}; {a2}; {a3}; {a4}; {a5}; {a6}; {a7}}}$. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	l=random.randint(3,6)
	
	kq1_T=f"*Lập được ${{7^{{{l}}}}}$ số tự nhiên có ${{{l}}}$ chữ số " 
	kq1_F=f"Lập được ${{A^{{{l}}}_{{7}}}}$ số tự nhiên có ${{{l}}}$ chữ số "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Lập được ${{7^{{{l}}}}}$ số tự nhiên có ${{{l}}}$ chữ số "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	l=random.randint(3,6)
	kq2_T=f"*Lập được ${{A^{{{l}}}_{{7}}}}$ số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau "
	kq2_F=f" Lập được ${{C^{{{l}}}_{{7}}}}$ số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f" Lập được ${{A^{{{l}}}_{{7}}}}$ số tự nhiên có ${{{l}}}$ chữ số đôi một khác nhau "
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	l=random.randint(3,6)
	chu_so=[a1,a2,a3,a4,a5,a6,a7]

	# Bước 3: Tạo tất cả các số có 4 chữ số khác nhau
	so_hoan_vi = [
	    int(''.join(map(str, p)))  # Chuyển từng hoán vị thành số nguyên
	    for p in permutations(chu_so, l)  # Tạo các hoán vị 4 chữ số từ tập hợp
	]
	
	chon=random.randint(1,2)
	if chon ==1:
		so_ket_qua = [so for so in so_hoan_vi if so %2 ==0]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)
		a=random.choice([i for i in range(-10,10) if i!=0])

		kq3_T=f"* Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và là số chẵn" 
		kq3_F=f"Lập được ${{{kq+a}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và là số chẵn "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và là số chẵn"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon ==2:
		so_ket_qua = [so for so in so_hoan_vi if so %2 !=0]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)
		a=random.choice([i for i in range(-10,10) if i!=0])

		kq3_T=f"* Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và là số lẻ" 
		kq3_F=f"Lập được ${{{kq+a}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và là số lẻ "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và là số lẻ"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	l=4
	so_hoan_vi = [
	    int(''.join(map(str, p)))  # Chuyển từng hoán vị thành số nguyên
	    for p in permutations(chu_so, l)  # Tạo các hoán vị 4 chữ số từ tập hợp
	]

	chon=random.randint(1,2)
	if chon ==1:
		m=random.randint(1356,3456)
		so_ket_qua = [so for so in so_hoan_vi if so > m]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)
		kq4_T=f"*Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và lớn hơn ${{{m}}}$ "
		kq4_F=f"Lập được ${{{kq+a}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và lớn hơn ${{{m}}}$ " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và lớn hơn ${{{m}}}$"
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon ==2:
		m=random.randint(5134,7897)
		so_ket_qua = [so for so in so_hoan_vi if so < m]

		# Bước 5: Đếm số lượng các số thỏa mãn
		kq = len(so_ket_qua)
		kq4_T=f"*Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và nhỏ hơn ${{{m}}}$ "
		kq4_F=f"Lập được ${{{kq+a}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và nhỏ hơn ${{{m}}}$ " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Lập được ${{{kq}}}$ số tự nhiên có ${{{l}}}$ chữ số khác nhau và nhỏ hơn ${{{m}}}$"
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an



#[D10_C8_B2_49]-SA-M4. Đếm các số chia hết cho 6 được tạo thành từ các chữ số cho trước (các cs không nhất thiết khác nhau)
def mcn__L10_C8_B2_49(): 
	nhom1 = range(1, 10)
	chon =random.randint(1,5)
	if chon ==1:
		danh_sach = [ int(f"{x}{y}{z}{t}") for x in nhom1 for y in nhom1 for z in nhom1 for t in nhom1 ]
		dem=len([ i for i in danh_sach if i%6==0])
		noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số có ${{4}}$ chữ số chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
		noi_dung_loigiai=(f" Gọi số đó là $\\overline{{abcd}}$ \n\n"
				f" ${{d}}$ có 4 cách chọn \n\n"
				f" b có 9 cách chọn\n\n"
				f" c có 9 cách chọn \n\n"
				f" a có 3 cách chọn vì tổng b+d+c nếu chia hết cho 3, hoặc chia 3 dư 1, hoặc chia 3 dư 2.\n\n"
		f" Theo quy tắc nhân có ${{4\\cdot 9 \\cdot 9 \\cdot 3= {dem}}}$ số ")
		
	if chon ==2:
		danh_sach = [ int(f"{x}{y}{z}") for x in nhom1 for y in nhom1 for z in nhom1]
		dem=len([ i for i in danh_sach if i%6==0])
		noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số có ${{3}}$ chữ số chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
		noi_dung_loigiai=(f" Gọi số đó là $\\overline{{abc}}$ \n\n"
				f" ${{c}}$ có 4 cách chọn \n\n"
				f" b có 9 cách chọn\n\n"
				f" a có 3 cách chọn vì tổng b+c nếu chia hết cho 3, hoặc chia 3 dư 1, hoặc chia 3 dư 2.\n\n "
		f" Theo quy tắc nhân có ${{4\\cdot 9 \\cdot 3= {dem}}}$ số ")		

	if chon ==3:
		danh_sach = [ int(f"{x}{y}{z}{t}{a}") for x in nhom1 for y in nhom1 for z in nhom1 for t in nhom1 for a in nhom1]
		dem=len([ i for i in danh_sach if i%6==0])
		noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số có ${{5}}$ chữ số chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
		noi_dung_loigiai=(f" Gọi số đó là $\\overline{{abcde}}$ \n\n"
				f" ${{e}}$ có 4 cách chọn \n\n"
				f" d có 9 cách chọn \n\n"
				f" b có 9 cách chọn\n\n"
				f" c có 9 cách chọn \n\n"
				f" a có 3 cách chọn vì tổng b+d+c+e nếu chia hết cho 3, hoặc chia 3 dư 1, hoặc chia 3 dư 2.\n\n"
		f" Theo quy tắc nhân có ${{4\\cdot 9 \\cdot 9 \\cdot 9 \\cdot 3= {dem}}}$ số ")
	if chon ==4:
		danh_sach = [ int(f"{x}{y}{z}{t}{a}{b}") for x in nhom1 for y in nhom1 for z in nhom1 for t in nhom1 for a in nhom1 for b in nhom1]
		dem=len([ i for i in danh_sach if i%6==0])
		noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số có ${{6}}$ chữ số chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
		noi_dung_loigiai=(f" Gọi số đó là $\\overline{{abcdef}}$ \n\n"
				f" ${{f}}$ có 4 cách chọn \n\n"
				f" e có 9 cách chọn \n\n"
				f" d có 9 cách chọn \n\n"
				f" b có 9 cách chọn\n\n"
				f" c có 9 cách chọn \n\n"
				f" a có 3 cách chọn vì tổng b+d+c+e+f nếu chia hết cho 3, hoặc chia 3 dư 1, hoặc chia 3 dư 2.\n\n"
		f" Theo quy tắc nhân có ${{4\\cdot 9 \\cdot 9 \\cdot 9  \\cdot 9 \\cdot 3= {dem}}}$ số ")

	if chon ==5:
		danh_sach = [ int(f"{x}{y}{z}{t}{a}{b}") for x in nhom1 for y in nhom1 for z in nhom1 for t in nhom1 for a in nhom1 for b in nhom1]
		dem=len([ i for i in danh_sach if i%6==0])
		noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số có ${{6}}$ chữ số chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
		noi_dung_loigiai=(f" Gọi số đó là $\\overline{{abcdef}}$ \n\n"
				f" ${{f}}$ có 4 cách chọn \n\n"
				f" e có 9 cách chọn \n\n"
				f" d có 9 cách chọn \n\n"
				f" b có 9 cách chọn\n\n"
				f" c có 9 cách chọn \n\n"
				f" a có 3 cách chọn vì tổng b+d+c+e+f nếu chia hết cho 3, hoặc chia 3 dư 1, hoặc chia 3 dư 2.\n\n"
		f" Theo quy tắc nhân có ${{4\\cdot 9 \\cdot 9 \\cdot 9  \\cdot 9 \\cdot 3= {dem}}}$ số ")
	kq=tinh_tong_chu_so(dem)
	noi_dung_loigiai+=f" Tổng các chữ số của số ${{m}}$ là ${{{kq}}}$"
	


	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an






#[D10_C8_B2_50]-SA-M4. Đếm các số chia hết cho 6 được tạo thành từ các chữ số cho trước (các cs khác nhau)
def mcn__L10_C8_B2_50(): 

	w=random.randint(1,6)
	if w==1:

		nhom1 = range(1, 10)
		chon =random.randint(1,4)
		if chon ==1:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 4)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{4}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
			
		if chon ==2:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 3)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{3}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==3:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 5)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{5}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==4:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 6)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{6}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

	if w==2:


		nhom1 = range(1, 9)
		chon =random.randint(1,4)
		if chon ==1:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 4)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8}}$ lập được ${{m}}$ số tự nhiên có ${{4}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
			
		if chon ==2:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 3)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8}}$ lập được ${{m}}$ số tự nhiên có ${{3}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==3:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 5)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8}}$ lập được ${{m}}$ số tự nhiên có ${{5}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==4:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 6)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7;8}}$ lập được ${{m}}$ số tự nhiên có ${{6}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "


	if w==3:

		nhom1 = range(1, 8)
		chon =random.randint(1,4)
		if chon ==1:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 4)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7}}$ lập được ${{m}}$ số tự nhiên có ${{4}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
			
		if chon ==2:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 3)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7}}$ lập được ${{m}}$ số tự nhiên có ${{3}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==3:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 5)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7}}$ lập được ${{m}}$ số tự nhiên có ${{5}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==4:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 6)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6;7}}$ lập được ${{m}}$ số tự nhiên có ${{6}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

	if w==4:

		nhom1 = range(1, 7)
		chon =random.randint(1,3)
		if chon ==1:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 4)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6}}$ lập được ${{m}}$ số tự nhiên có ${{4}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
			
		if chon ==2:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 3)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6}}$ lập được ${{m}}$ số tự nhiên có ${{3}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==3:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 5)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{1;2;3;...;6}}$ lập được ${{m}}$ số tự nhiên có ${{5}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "


	if w==5:

		nhom1 = range(2, 10)
		chon =random.randint(1,4)
		if chon ==1:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 4)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{4}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
			
		if chon ==2:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 3)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{3}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==3:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 5)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{5}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==4:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 6)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số ${{2;3;...;6;7;8;9}}$ lập được ${{m}}$ số tự nhiên có ${{6}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

	if w==6:
		n=random.randint(6,9)
		nhom1 =tao_taphop_khac_0(n)
		# a1,a2,a3,a4,a5,a6,a7=random.sample(range(1,10),7)
		# nhom1 = [a1,a2,a3,a4,a5,a6,a7]
		chon =random.randint(1,4)
		if chon ==1:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 4)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số $\\{{{nhom1} \\}}$ lập được ${{m}}$ số tự nhiên có ${{4}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "
			
		if chon ==2:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 3)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số $\\{{{nhom1} \\}}$ lập được ${{m}}$ số tự nhiên có ${{3}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==3:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 5)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số $\\{{{nhom1} \\}}$ lập được ${{m}}$ số tự nhiên có ${{5}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

		if chon ==4:
			danh_sach=[int("".join(map(str, p))) for p in permutations(nhom1, 6)] 
			dem=len([ i for i in danh_sach if i%6==0])
			noi_dung=f"Từ các chữ số $\\{{{nhom1} \\}}$ lập được ${{m}}$ số tự nhiên có ${{6}}$ chữ số đôi một khác nhau và chia hết cho ${{6}}$. Tổng các chữ số của số ${{m}}$ là "

	noi_dung_loigiai=f" Có ${{{dem}}}$ số thoả mãn yêu cầu bài toán \n\n"

	kq=tinh_tong_chu_so(dem)
	noi_dung_loigiai+=f" Tổng các chữ số của số ${{m}}$ là ${{{kq}}}$"
	


	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an







#[D10_C8_B2_51]-SA-M3. Tạo số có các chữ số khác nhau trong đó phải có mặt của chữ số x,y...(ds không có 0) 
def mcn__L10_C8_B2_51(): 
	chon =random.randint(1,2)
	if chon ==1:
		n=random.randint(6,9)
		m=random.randint(4,5)
		nhom1 =tao_taphop_khac_0(n)
		a1, a2 = random.sample(list(nhom1), 2)
		noi_dung=f" Từ các chữ số $\\{{{nhom1}\\}}$ có thể lập được bao nhiên số tự nhiên có ${{{m}}}$ chữ số đôi một khác nhau trong đó luôn có mặt của chữ số ${{{a1}; {a2}}}$ "
		noi_dung_loigiai=(f" có $A^{{2}}_{{{m}}}$ cách xếp ${{{a1}; {a2}}}$ vào \n\n"
		f" Có  $A^{{{m-2}}}_{{{n-2}}}$ cách xếp số cho các chữ cái còn lại \n\n"
		f" Theo quy tắc nhân có $A^{{2}}_{{{m}}} \\cdot A^{{{m-2}}}_{{{n-2}}} = {chinh_hop(2,m)*chinh_hop(m-2,n-2)} $")
		kq= chinh_hop(2,m)*chinh_hop(m-2,n-2)

	if chon ==2:
		n=random.randint(7,9)
		m=random.randint(5,6)
		nhom1 =tao_taphop_khac_0(n)
		a1, a2, a3 = random.sample(list(nhom1), 3)
		noi_dung=f" Từ các chữ số $\\{{{nhom1}\\}}$ có thể lập được bao nhiên số tự nhiên có ${{{m}}}$ chữ số đôi một khác nhau trong đó luôn có mặt của chữ số ${{{a1}; {a2}; {a3}}}$ "
		noi_dung_loigiai=(f" có $A^{{3}}_{{{m}}}$ cách xếp ${{{a1}; {a2}; {a3}}}$ vào \n\n"
		f" Có  $A^{{{m-3}}}_{{{n-3}}}$ cách xếp số cho các chữ cái còn lại \n\n"
		f" Theo quy tắc nhân có $A^{{3}}_{{{m}}} \\cdot A^{{{m-3}}}_{{{n-3}}} = {chinh_hop(3,m)*chinh_hop(m-3,n-3)} $")
		kq= chinh_hop(3,m)*chinh_hop(m-3,n-3)
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an






#[D10_C8_B2_52]-SA-M3. Tạo số có các chữ số khác nhau trong đó phải có mặt của chữ số x,y...(ds có 0) 
def mcn__L10_C8_B2_52(): 
	n=random.randint(6,9)
	m=random.randint(4,5)
	nhom1 =tao_taphop_chua_0(n)
	nhom_khac_0 = [x for x in nhom1 if x != 0]
	a1, a2 = random.sample(nhom_khac_0, 2)
	kq= chinh_hop(2,m)*chinh_hop(m-2,n-2) - chinh_hop(2,m-1)*chinh_hop(m-3,n-3)
	noi_dung=f" Từ các chữ số $\\{{{nhom1}\\}}$ có thể lập được bao nhiên số tự nhiên có ${{{m}}}$ chữ số đôi một khác nhau trong đó luôn có mặt của chữ số ${{{a1}; {a2}}}$ "
	noi_dung_loigiai=(f" Xét các số có ${{{m}}}$ chữ số đôi một khác nhau trong đó luôn có mặt của chữ số ${{{a1}; {a2}}}$ tính cả chữ số 0 đứng đầu \n\n"
		f" có $A^{{2}}_{{{m}}}$ cách xếp ${{{a1}; {a2}}}$ \n\n"
	f" Có  $A^{{{m-2}}}_{{{n-2}}}$ cách xếp số cho các chữ cái còn lại \n\n"
	f" Theo quy tắc nhân có $A^{{2}}_{{{m}}} \\cdot A^{{{m-2}}}_{{{n-2}}} = {chinh_hop(2,m)*chinh_hop(m-2,n-2)} $\n\n"
	f" Xét các số có ${{{m}}}$ chữ số đôi một khác nhau trong đó luôn có mặt của chữ số ${{{a1}; {a2}}}$ và chữ số 0 đứng đầu  \n\n"

	f" có $A^{{2}}_{{{m-1}}}$ cách xếp ${{{a1}; {a2}}}$ \n\n"
	f" Có  $A^{{{m-3}}}_{{{n-3}}}$ cách xếp số cho các chữ cái còn lại \n\n"
	f" Theo quy tắc nhân có $A^{{2}}_{{{m-1}}} \\cdot A^{{{m-3}}}_{{{n-3}}} = {chinh_hop(2,m-1)*chinh_hop(m-3,n-3)} $\n\n"
	f" Vậy có $ {{ {chinh_hop(2,m)*chinh_hop(m-2,n-2)} -{chinh_hop(2,m-1)*chinh_hop(m-3,n-3)} = {kq} }}$ số "
	)


	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C8_B2_53]-SA-M3. Tìm số cách chọn có ít nhất một vật được chọn
def mcn__L10_C8_B2_53():
	while True:
		n1=random.randint(4,8)
		n2=random.randint(4,8)
		n3=random.randint(4,8)

		k=random.randint(3,6)
		n=n1+n2+n3
		dap_an=binomial(n,k)-binomial(n2+n3,k)
		if all([n1!=n2,n2!=n3,n3!=n1,dap_an<9999]):
			break
	chon=random.randint(1,6)
		
	if chon==1:
		hoa=["hoa hồng", "hoa lan", "hoa mai", "hoa cúc", "hoa đào", "hoa ly", ]
		vat1, vat2, vat3=random.sample(hoa,3)
		
		noi_dung = (
		f"Cửa hàng bán hoa có ${{{n1}}}$ bó {vat1}, ${{{n2}}}$ bó {vat2} và ${{{n3}}}$ bó {vat3}."
		f" Chọn ngẫu nhiên ${{{k}}}$ bó hoa. Tính số cách chọn để có ít nhất một bó {vat1} được chọn."
		)	

		noi_dung_loigiai=(
		f"Số cách chọn ${{{k}}}$ bó hoa tùy ý: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"
		f"Số cách chọn không có bó {vat1} nào: $C^{{{k}}}_{{{n2+n3}}}={binomial(n2+n3,k)}$.\n\n"
		f"số cách chọn để có ít nhất một bó {vat1}: ${binomial(n,k)}-{binomial(n2+n3,k)}={dap_an}$.")
	
	if chon==2:
		sach=["sách Toán", "sách Vật Lí", "sách Văn", "sác Tiếng Anh", "sách Hóa Học", "sách Tin học", ]
		vat1, vat2, vat3=random.sample(sach,3)
		
		noi_dung = (
		f"Thư viện có ${{{n1}}}$ cuốn {vat1}, ${{{n2}}}$ cuốn {vat2} và ${{{n3}}}$ cuốn {vat3}, các cuốn sách là khác nhau."
		f" Chọn ngẫu nhiên ${{{k}}}$ cuốn sách. Tính số cách chọn để có ít nhất một cuốn {vat1} được chọn."
		)	

		noi_dung_loigiai=(
		f"Số cách chọn ${{{k}}}$ cuốn sách tùy ý: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"
		f"Số cách chọn không có cuốn {vat1} nào: $C^{{{k}}}_{{{n2+n3}}}={binomial(n2+n3,k)}$.\n\n"
		f"số cách chọn để có ít nhất một cuốn {vat1}: ${binomial(n,k)}-{binomial(n2+n3,k)}={dap_an}$.")

	if chon==3:
		qua=["cam", "táo", "ổi", "xoài", "lê", "mận", ]
		vat1, vat2, vat3=random.sample(qua,3)
		
		noi_dung = (
		f"Cửa hàng bán hoa quả có ${{{n1}}}$ quả {vat1}, ${{{n2}}}$ quả {vat2} và ${{{n3}}}$ quả {vat3}."
		f" Chọn ngẫu nhiên ${{{k}}}$ quả. Tính số cách chọn để có ít nhất một quả {vat1} được chọn."
		)	

		noi_dung_loigiai=(
		f"Số cách chọn ${{{k}}}$ quả tùy ý: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"
		f"Số cách chọn không có quả {vat1} nào: $C^{{{k}}}_{{{n2+n3}}}={binomial(n2+n3,k)}$.\n\n"
		f"số cách chọn để có ít nhất một quả {vat1}: ${binomial(n,k)}-{binomial(n2+n3,k)}={dap_an}$.")

	if chon==4:
		but=["bút bi", "bút chì", "bút màu", "bút mực" ]
		vat1, vat2, vat3=random.sample(but,3)
		
		noi_dung = (
		f"Một nhà sách có ${{{n1}}}$ cái {vat1}, ${{{n2}}}$ cái {vat2} và ${{{n3}}}$ cái {vat3}."
		f" Chọn ngẫu nhiên ${{{k}}}$ cái. Tính số cách chọn để có ít nhất một cái {vat1} được chọn."
		)	

		noi_dung_loigiai=(
		f"Số cách chọn ${{{k}}}$ bút tùy ý: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"
		f"Số cách chọn không có cái {vat1} nào: $C^{{{k}}}_{{{n2+n3}}}={binomial(n2+n3,k)}$.\n\n"
		f"số cách chọn để có ít nhất một cái {vat1}: ${binomial(n,k)}-{binomial(n2+n3,k)}={dap_an}$.")

	if chon==5:
		convat=["chó", "mèo", "thỏ", "gà", "dê", "vịt", "ngỗng" ]
		vat1, vat2, vat3=random.sample(convat,3)
		
		noi_dung = (
		f"Một trang trại có ${{{n1}}}$ con {vat1}, ${{{n2}}}$ con {vat2} và ${{{n3}}}$ con {vat3}."
		f" Chọn ngẫu nhiên ${{{k}}}$ con vật. Tính số cách chọn để có ít nhất một con {vat1} được chọn."
		)	

		noi_dung_loigiai=(
		f"Số cách chọn ${{{k}}}$ con vật tùy ý: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"
		f"Số cách chọn không có con {vat1} nào: $C^{{{k}}}_{{{n2+n3}}}={binomial(n2+n3,k)}$.\n\n"
		f"số cách chọn để có ít nhất một con {vat1}: ${binomial(n,k)}-{binomial(n2+n3,k)}={dap_an}$.")

	if chon==6:
		banh=["bánh mì", "bánh kem", "bánh quy", "bánh bao", "bánh bông lan", "bánh trứng",]
		vat1, vat2, vat3=random.sample(banh,3)
		
		noi_dung = (
		f"Một tiệm bánh có ${{{n1}}}$ cái {vat1}, ${{{n2}}}$ cái {vat2} và ${{{n3}}}$ cái {vat3}."
		f" Chọn ngẫu nhiên ${{{k}}}$ cái bánh. Tính số cách chọn để có ít nhất một cái {vat1} được chọn."
		)	

		noi_dung_loigiai=(
		f"Số cách chọn ${{{k}}}$ cái bánh tùy ý: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"
		f"Số cách chọn không có cái {vat1} nào: $C^{{{k}}}_{{{n2+n3}}}={binomial(n2+n3,k)}$.\n\n"
		f"số cách chọn để có ít nhất một cái {vat1}: ${binomial(n,k)}-{binomial(n2+n3,k)}={dap_an}$.")
	
		
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an


#[D10_C8_B2_54]-TF-M3. Phòng có m hàng ghế, mỗi hàng có n ghế. Xét Đ-S: Số cách xếp người vào các hàng
def mcn__L10_C8_B2_54():
	while True:
		s=random.randint(30,40)
		#Số hàng:
		h=random.randint(4,8)
		# Số ghế:
		m=random.randint(4,6)
		if h*m>=s:
			break

	noi_dung = (
	f"Một phòng họp {h} hàng ghế, mỗi hàng có {m} ghế."
	f" Có {s} người tham dự cuộc họp."
	" Xét tính đúng-sai của các khẳng định sau:")	

	kq1_T=f"* Có $A^{m}_{{{s}}}$ cách sắp xếp {m} người ngồi vào hàng ghế đầu tiên" 
	kq1_F=f"Có $C^{m}_{{{s}}}$ cách sắp xếp {m} người ngồi vào hàng ghế đầu tiên"

	HDG=(f"Mỗi cách chọn {m} người trong {s} người để ngồi vào hàng ghế đầu tiên là một chỉnh hợp chập {m} của {s}."
	f" Vậy có $A^{m}_{{{s}}}$ cách xếp 6 người ngồi vào hàng ghế đầu tiên. ")
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	s2=s-m

	kq2_T=f"* Sau khi sắp xếp xong hàng ghế đầu tiên, có $A^{m}_{{{s2}}}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ hai"
	kq2_F=random.choice([
	f"Sau khi sắp xếp xong hàng ghế đầu tiên, có $C^{m}_{{{s2}}}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ hai",
	f"Sau khi sắp xếp xong hàng ghế đầu tiên, có $P_{m}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ hai", ])

	HDG=f" Sau khi sắp xếp xong hàng ghế đầu tiên, có $A^{m}_{{{s2}}}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ hai."
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	s3=s-2*m

	kq3_T=f"* Sau khi sắp xếp xong hai hàng ghế đầu tiên, có $A^{m}_{{{s3}}}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ hai" 
	kq3_F=random.choice([
	f"Sau khi sắp xếp xong hai hàng ghế đầu tiên, có $C^{m}_{{{s3}}}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ ba",
	f"Sau khi sắp xếp xong hai hàng ghế đầu tiên, có $P_{m}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ ba",
	f"Sau khi sắp xếp xong hai hàng ghế đầu tiên, có $A^{m}_{{{s2}}}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ ba", ])

	HDG=f"Sau khi sắp xếp xong hai hàng ghế đầu tiên, có $A^{m}_{{{s3}}}$ cách sắp xếp {m} người ngồi vào hàng ghế thứ ba."
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	s4=s-3*m
	n=h*m-3*m

	kq4_T=f"* Sau khi sắp xếp xong ba hàng ghế đầu tiên, có $A^{{{s4}}}_{{{n}}}$ cách sắp xếp những người còn lại vào các ghế còn lại"
	kq4_F=random.choice([
		f"Sau khi sắp xếp xong ba hàng ghế đầu tiên, có $C^{{{s4}}}_{{{n}}}$ cách sắp xếp những người còn lại vào các ghế còn lại",
		f"Sau khi sắp xếp xong ba hàng ghế đầu tiên, có $P_{{{n}}}$ cách sắp xếp những người còn lại vào các ghế còn lại",
		f"Sau khi sắp xếp xong ba hàng ghế đầu tiên, có $A^{{{m}}}_{{{n}}}$ cách sắp xếp những người còn lại vào các ghế còn lại",  ])
	
	HDG=(f"Số ghế còn lại sau khi xếp ba hàng đầu tiên là {n}.\n\n"
		f"Số người còn lại sau khi xếp ba hàng đầu tiên là {s4}.\n\n"
		f"Có $A^{{{s4}}}_{{{n}}}$ cách sắp xếp những người còn lại vào các ghế còn lại.")
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"
	f"\n\n a) {loigiai[0]}\n"
	f"b) {loigiai[1]}\n"
	f"c) {loigiai[2]}\n"
	f"d) {loigiai[3]}\n")

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	loigiai_latex=(f"\n\n a) {loigiai[0]}\n\n"
	f"b) {loigiai[1]}\n\n"
	f"c) {loigiai[2]}\n\n"
	f"d) {loigiai[3]}\n\n")

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C8_B2_55]-TF-M3. Lớp có m nam, n nữ. Xét Đ-S: cách xếp vào 1 hàng, lập ban cán sự, chọn k người sửa bài tập
def mcn__L10_C8_B2_55():
	ten_lop=f"10A{random.randint(1,9)}"
	while True:
		m=random.randint(18,28)
		n=random.randint(14,22)
		if all([m>n]):
			break
	s=m+n
	noi_dung = (
	f"Lớp {ten_lop} có {m} học sinh nam và {n} học sinh nữ."
	f" Xét tính đúng-sai của các khẳng định sau:")

	chon=random.randint(1,2)
	if chon==1:
		kq1_T=f"* Số cách xếp các bạn nam thành một hàng dọc là ${{{m}!}}$" 
		kq1_F=random.choice([
			f"Số cách xếp các bạn nam thành một hàng dọc là $C^{{{m}}}_{{{s}}}$",
			f"Số cách xếp các bạn nam thành một hàng dọc là $A^{{{m}}}_{{{s}}}$",
		 ])
		
		HDG=f"Số cách xếp các bạn nam thành một hàng dọc là ${{{m}!}}$."
	
	if chon==2:
		kq1_T=f"* Số cách xếp các bạn nữ thành một hàng ngang là ${{{n}!}}$" 
		kq1_F=random.choice([
			f"Số cách xếp các bạn nữ thành một hàng ngang là $C^{{{n}}}_{{{s}}}$",
			f"Số cách xếp các bạn nữ thành một hàng ngang là $A^{{{n}}}_{{{s}}}$",
		 ])
		
		HDG=f"Số cách xếp các bạn nữ thành một hàng ngang là ${{{m}!}}$."		
	
	
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	k=random.randint(3,6)
	chon=random.randint(1,2)
	if chon==1:
		kq2_T=f"* Số cách xếp {k} bạn nam ngồi vào một bàn dài là $A^{k}_{{{m}}}$"
		kq2_F=f" Số cách xếp {k} bạn nam ngồi vào một bàn dài là $C^{k}_{{{m}}}$"
		
		HDG=f"Số cách xếp {k} bạn nam ngồi vào một bàn dài là $A^{k}_{{{m}}}$."
	
	if chon==2:
		kq2_T=f"* Số cách xếp {k} bạn nữ ngồi vào một bàn dài là $A^{k}_{{{n}}}$"
		kq2_F=f" Số cách xếp {k} bạn nữ ngồi vào một bàn dài là $C^{k}_{{{n}}}$"
		
		HDG=f"Số cách xếp {k} bạn nữ ngồi vào một bàn dài là $A^{k}_{{{n}}}$."	

	
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* Số cách lập một ban cán sự gồm 1 lớp trưởng, 1 lớp phó và 1 bí thư chi đoàn là $A^3_{{{s}}}$" 
	kq3_F=f"Số cách lập một ban cán sự gồm 1 lớp trưởng, 1 lớp phó và 1 bí thư chi đoàn là $C^3_{{{s}}}$"
	
	HDG=f"Số cách lập 1 ban cán sự gồm 1 lớp trưởng, 1 lớp phó và 1 bí thư chi đoàn là $A^3_{{{s}}}$."
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	k=random.randint(3,6)

	kq4_T=f"* Số cách chọn {k} bạn lên làm {k} bài tập khác nhau theo đúng thứ tự các bài tập là $A^{k}_{{{s}}}$"
	kq4_F=f"Số cách chọn {k} bạn lên làm {k} bài tập khác nhau theo đúng thứ tự các bài tập là $C^{k}_{{{s}}}$" 
	
	HDG=f"Số cách chọn {k} bạn lên làm {k} bài tập khác nhau theo đúng thứ tự các bài tập là $A^{k}_{{{s}}}$."
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"
	f"\n\n a) {loigiai[0]}\n"
	f"b) {loigiai[1]}\n"
	f"c) {loigiai[2]}\n"
	f"d) {loigiai[3]}\n")

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	loigiai_latex=(f"\n\n a) {loigiai[0]}\n\n"
	f"b) {loigiai[1]}\n\n"
	f"c) {loigiai[2]}\n\n"
	f"d) {loigiai[3]}\n\n")

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C8_B2_56]-TF-M3. Cửa hàng bán 3 loại. Xét Đ-S: cách xếp k sản phẩm, lập combo bán chạy, xếp theo nhóm
def mcn__L10_C8_B2_56():
	ten_lop=f"10A{random.randint(1,9)}"
	while True:
		m=random.randint(14,20)
		n=random.randint(14,22)
		p=random.randint(6,10)
		if all([m!=n]):
			break
	s=m+n+p
	k=random.randint(4,6)
	noi_dung = (
	f"Một cửa hàng tạp hóa bán có {m} chai nước giải khát khác nhau, {n} bịch bánh kẹo khác nhau và {p} hộp mỳ ăn liền khác nhau."
	f" Xét tính đúng-sai của các khẳng định sau:")	
	
	kq1_T=f"* Số cách bày {k} sản phẩm bất kỳ lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{s}}}$" 
	kq1_F=random.choice([
	f"Số cách bày {k} sản phẩm bất kỳ lên kệ trưng bày theo thứ tự từ trái sang phải là $C^{k}_{{{s}}}$",
	f"Số cách bày {k} sản phẩm bất kỳ lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{m}}}$",
	f"Số cách bày {k} sản phẩm bất kỳ lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{n}}}$", ])
	
	HDG=f"Số cách bày {k} sản phẩm bất kỳ lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{s}}}$."
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon==1:
		kq2_T=f"* Số cách bày {k} sản phẩm nước giải khát lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{m}}}$"
		kq2_F=f"Số cách bày {k} sản phẩm nước giải khát lên kệ trưng bày theo thứ tự từ trái sang phải là $C^{k}_{{{m}}}$"
		
		HDG=f"Số cách bày {k} sản phẩm nước giải khát lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{m}}}$."
	
	if chon==2:
		kq2_T=f"* Số cách bày {k} sản phẩm bánh kẹo lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{n}}}$"
		kq2_F=f"Số cách bày {k} sản phẩm bánh kẹo lên kệ trưng bày theo thứ tự từ trái sang phải là $C^{k}_{{{n}}}$"
		
		HDG=f"Số cách bày {k} sản phẩm bánh kẹo lên kệ trưng bày theo thứ tự từ trái sang phải là $A^{k}_{{{n}}}$."
	
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	k_1=random.randint(1,3)
	k_2=random.randint(1,3)
	k_3=random.randint(1,3)

	kq3_T=f"* Số cách tạo 1 combo gồm {k_1} chai nước giải khát, {k_2} bịch bánh kẹo và {k_3} mỳ ăn liền là $C^{k_1}_{{{m}}}.C^{k_2}_{{{n}}}.C^{k_3}_{{{p}}}$" 
	kq3_F=f"Số cách tạo 1 combo gồm {k_1} chai nước giải khát, {k_2} bịch bánh kẹo và {k_3} mỳ ăn liền là $A^{k_1}_{{{m}}}.A^{k_2}_{{{n}}}.A^{k_3}_{{{p}}}$"
	
	HDG=f"Số cách xếp là: $C^{k_1}_{{{m}}}.C^{k_2}_{{{n}}}.C^{k_3}_{{{p}}}$."
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	k_1=random.randint(3,6)
	k_2=random.randint(3,7)

	kq4_T=f"* Số cách xếp {k_1} chai nước giải khát và {k_2} bịch bánh kẹo lên kệ trưng bày theo 2 nhóm sản phẩm và theo thứ tự từ trái qua phải là $2.A^{k_1}_{{{m}}}.A^{k_2}_{{{n}}}$"
	kq4_F=f"Số cách xếp {k_1} chai nước giải khát và {k_2} bịch bánh kẹo lên kệ trưng bày theo 2 nhóm sản phẩm và theo thứ tự từ trái qua phải là $A^{k_1}_{{{m}}}.A^{k_2}_{{{n}}}$" 
	
	HDG=f"Số cách xếp là: $2.A^{k_1}_{{{m}}}.A^{k_2}_{{{n}}}$."
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.\n"\
	f"c) {list_PA[2]}.\n"\
	f"d) {list_PA[3]}.\n"
	loigiai=[]
	for pa in list_PA:
	    if pa==kq1:
	        loigiai.append(loigiai_1)
	    if pa==kq2:
	        loigiai.append(loigiai_2)
	    if pa==kq3:
	        loigiai.append(loigiai_3)
	    if pa==kq4:
	        loigiai.append(loigiai_4)


	noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"
	f"\n\n a) {loigiai[0]}\n"
	f"b) {loigiai[1]}\n"
	f"c) {loigiai[2]}\n"
	f"d) {loigiai[3]}\n")

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	loigiai_latex=(f"\n\n a) {loigiai[0]}\n\n"
	f"b) {loigiai[1]}\n\n"
	f"c) {loigiai[2]}\n\n"
	f"d) {loigiai[3]}\n\n")

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an



#Bài 3 - Nhị thức Niu-tơn
#[D10_C8_B3_01]-M1. Khai triển (x+a)^n
def mcn__L10_C8_B3_01():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -1), random.randint(1, 6)])	
	n=random.randint(4,5)
	f=(x+a)**n
	kq=latex(expand(f))
	kq2=latex(expand((x-a)**n))
	kq3=latex(expand((x+a)**(n-1)))
	kq4=latex(expand((x+a)**(n+1)))

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	noi_dung=f"Khai triển biểu thức ${latex(f)}$ ta được kết quả là"

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Áp dụng công thức khai triển Niu-tơn ta được: \n\n"\
					f"${latex(f)}={kq}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B3_02]-M1. Khai triển (a-x)^n
def mcn__L10_C8_B3_02():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -1), random.randint(1, 6)])	
	n=random.randint(4,5)
	f=(a-x)**n
	kq=latex(expand(f))
	kq2=latex(expand((x+a)**n))
	kq3=latex(expand((a-x)**(n-1)))
	kq4=latex(expand((a-x)**(n+1)))

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	noi_dung=f"Khai triển biểu thức ${latex(f)}$ ta được kết quả là"

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Áp dụng công thức khai triển Niu-tơn ta được: \n\n"\
					f"${latex(f)}={kq}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B3_03]-M2. Khai triển (ax+b)^n
def mcn__L10_C8_B3_03():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -2), random.randint(2, 6)])
	b = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	n=random.randint(4,5)
	f=(a*x+b)**n
	kq=latex(expand(f))
	kq2=latex(expand((a*x-b)**n))
	kq3=latex(expand((a*x+b)**(n-1)))
	kq4=latex(expand((a*x+b)**(n+1)))

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	noi_dung=f"Khai triển biểu thức ${latex(f)}$ ta được kết quả là"

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Áp dụng công thức khai triển Niu-tơn ta được: \n\n"\
					f"${latex(f)}={kq}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B3_04]-M2. Tìm hệ số của x^k trong khai triển của (ax+b)^n
def mcn__L10_C8_B3_04():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -2), random.randint(2, 6)])
	b = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	n=random.randint(4,5)
	k=random.randint(1,n)
	f=(a*x+b)**n
	kq=binomial(n,k)*a**k*b**(n-k)
	kq2=binomial(n,k)*a**k*b**k
	kq3=binomial(n,k)*a**(k+1)*b**k
	kq4=binomial(n,k)*a**(k-1)*b**(n-k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	noi_dung=f"Tìm hệ số của ${{ x^{{{k}}} }}$ trong khai triển biểu thức ${latex(f)}$."

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Số hạng chứa ${{ x^{{{k}}} }}$ là: $C^{{{k}}}_{{{n}}}.({a})^{{{k}}}.({b})^{{{n-k}}}.x^{{{k}}}={kq}{{ x^{{{k}}} }}$. \n"\
					f"Hệ số của ${{ x^{{{k}}} }}$ là ${{{kq}}}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B3_05]-M2. Tìm số hạng chứa x^k trong khai triển của (ax+b)^n
def mcn__L10_C8_B3_05():
	x=sp.symbols("x")
	a = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	n=random.randint(8,15)
	k=random.randint(1,n)
	f=(a*x+b)**n
	kq=binomial(n,k)*a**k*b**(n-k)
	kq2=binomial(n,k)*a**k*b**k
	kq3=binomial(n,k)*a**(k+1)*b**k
	kq4=binomial(n,k)*a**(k-1)*b**(n-k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq}x^{{{k}}}"
	kq2=f"{kq2}x^{{{k}}}"
	kq3=f"{kq3}x^{{{k}}}"
	kq4=f"{kq4}x^{{{k}}}"

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	noi_dung=f"Tìm số hạng chứa ${{ x^{{{k}}} }}$ trong khai triển biểu thức ${latex(f)}$."

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Số hạng chứa ${{ x^{{{k}}} }}$ là: $C^{{{k}}}_{{{n}}}.({a})^{{{k}}}.({b})^{{{n-k}}}.x^{{{k}}}={kq}{{ x^{{{k}}} }}$. \n"				
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B3_06]-M2. Tìm hệ số của x^k trong khai triển của (ax+b)^n, n=4,5
def mcn__L10_C8_B3_06():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -2), random.randint(2, 6)])
	b = random.choice([random.randint(-4, -2), random.randint(2,5)])
	n=random.randint(4,5)
	k=random.randint(1,n)
	f=(a*x+b)**n
	kq=binomial(n,k)*a**k*b**(n-k)
	kq2=binomial(n,k)*a**k*b**k
	kq3=binomial(n,k)*a**(k+1)*b**k
	kq4=binomial(n,k)*a**(k-1)*b**(n-k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

	if k!=1:
		noi_dung=f"Tìm hệ số của ${{ x^{{{k}}} }}$ trong khai triển biểu thức ${latex(f)}$."
		noi_dung_loigiai=f"Số hạng chứa ${{ x^{{{k}}} }}$ là: $C^{{{k}}}_{{{n}}}.({a})^{{{k}}}.({b})^{{{n-k}}}.x^{{{k}}}={kq}{{ x^{{{k}}} }}$. \n"\
						f"Hệ số của ${{ x^{{{k}}} }}$ là ${{{kq}}}$."
	else:
		noi_dung=f"Tìm hệ số của ${{x}}$ trong khai triển biểu thức ${latex(f)}$."
		noi_dung_loigiai=f"Số hạng chứa ${{x}}$ là: $C^{{{k}}}_{{{n}}}.({a}).({b})^{{{n-k}}}.x={kq}{{x}}$. \n"\
						f"Hệ số của ${{x}}$ là ${{{kq}}}$."


	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C8_B3_07]-M2. Tìm số hạng chứa x^k trong khai triển của (ax+b)^n, n=4,5
def mcn__L10_C8_B3_07():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	b = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	n=random.randint(4,5)
	k=random.randint(1,n)
	f=(a*x+b)**n
	kq=binomial(n,k)*a**k*b**(n-k)
	kq2=binomial(n,k)*a**k*b**k
	kq3=binomial(n,k)*a**(k+1)*b**k
	kq4=binomial(n,k)*a**(k-1)*b**(n-k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq}x^{{{k}}}".replace("x^{1}","x")
	kq2=f"{kq2}x^{{{k}}}".replace("x^{1}","x")
	kq3=f"{kq3}x^{{{k}}}".replace("x^{1}","x")
	kq4=f"{kq4}x^{{{k}}}".replace("x^{1}","x")

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	if k!=1:
		noi_dung=f"Tìm số hạng chứa ${{ x^{{{k}}} }}$ trong khai triển biểu thức ${latex(f)}$."
		noi_dung_loigiai=f"Số hạng chứa ${{ x^{{{k}}} }}$ là: $C^{{{k}}}_{{{n}}}.({a})^{{{k}}}.({b})^{{{n-k}}}.x^{{{k}}}={kq}{{ x^{{{k}}} }}$. \n"
	else:
		noi_dung=f"Tìm số hạng chứa ${{x}}$ trong khai triển biểu thức ${latex(f)}$."
		noi_dung_loigiai=f"Số hạng chứa ${{x}}$ là: $C^{{{k}}}_{{{n}}}.({a})^{{{k}}}.({b})^{{{n-k}}}.x={kq}{{x}}$. \n"

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
					
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C8_B3_08]-M2. Tìm số hạng thứ k+1 trong khai triển của (ax+b)^n giảm dần theo số mũ của x 
def mcn__L10_C8_B3_08():
	x=sp.symbols("x")
	a = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	n=random.randint(8,15)
	k=random.randint(3,n-2)
	f=(a*x+b)**n
	kq=binomial(n,k)*a**(n-k)*b**k
	kq2=binomial(n,k)*a**k*b**(n-k)
	kq3=binomial(n,k)*a**(k+1)*b**k
	kq4=binomial(n,k)*a**(k)*b**(k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq}x^{{{n-k}}}"
	kq2=f"{kq2}x^{{{n-k}}}"
	kq3=f"{binomial(n,k)*a**(n-k)*b**k}x^{{{k}}}"
	kq4=f"{kq4}x^{{{k+1}}}"

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	noi_dung=f"Tìm số hạng thứ ${{{k+1}}}$ trong khai triển biểu thức ${latex(f)}$ theo thứ tự giảm dần của số mũ của ${{x}}$."

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Số hạng thứ ${{{k+1}}}$ là: $C^{{{k}}}_{{{n}}}.({a})^{{{n-k}}}.({b})^{{{k}}}.x^{{{n-k}}}={binomial(n,k)*a**(n-k)*b**k}x^{{{n-k}}}$.\n"				
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C8_B3_09]-M2. Tìm hệ số của x^k trong khai triển của (ax+b)^n, n=4,5
def mcn__L10_C8_B3_09():
	x=sp.symbols("x")
	while True:
		a = random.choice([random.randint(-6, -2), random.randint(2, 6)])
		b = random.choice([random.randint(-4, -2), random.randint(2,5)])
		n=random.randint(4,5)
		k=random.randint(1,n)
		f=(a*x+b)**n
		kq=binomial(n,k)*a**k*b**(n-k)
		if all([kq<9999, kq>-999]):
			break

	if k!=1:
		noi_dung=f"Tìm hệ số của ${{ x^{{{k}}} }}$ trong khai triển biểu thức ${latex(f)}$."
		noi_dung_loigiai=f"Số hạng chứa ${{ x^{{{k}}} }}$ là: $C^{{{k}}}_{{{n}}}.({a})^{{{k}}}.({b})^{{{n-k}}}.x^{{{k}}}={kq}{{ x^{{{k}}} }}$. \n"\
						f"Hệ số của ${{ x^{{{k}}} }}$ là ${{{kq}}}$."
	else:
		noi_dung=f"Tìm hệ số của ${{x}}$ trong khai triển biểu thức ${latex(f)}$."
		noi_dung_loigiai=f"Số hạng chứa ${{x}}$ là: $C^{{{k}}}_{{{n}}}.({a}).({b})^{{{n-k}}}.x={kq}{{x}}$. \n"\
						f"Hệ số của ${{x}}$ là ${{{kq}}}$."

		
	debai_word= f"{noi_dung}"
	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n")
	dap_an=kq
	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung}\n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
	f"\\end{{ex}}\n")
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C8_B3_10]-SA-M2. Tìm số hạng không chứa x của (ax+b)^n, n=4,5
def mcn__L10_C8_B3_10():
	x=sp.symbols("x")
	while True:
		a = random.choice([random.randint(-6, -2), random.randint(2, 6)])
		b = random.choice([random.randint(-4, -2), random.randint(2,5)])
		n=random.randint(4,5)
		k=0
		f=(a*x+b)**n
		kq=b**n
		if all([kq<9999, kq>-999]):
			break


	noi_dung=f"Tìm số hạng không chứa ${{x}}$ trong khai triển biểu thức ${latex(f)}$."
	noi_dung_loigiai=f"Số hạng không chứa ${{x}}$ là: $C^{{{n}}}_{{{n}}}.({b})^{{{n}}}={kq}$. \n"		


		
	debai_word= f"{noi_dung}"
	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n")
	dap_an=kq
	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung}\n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
	f"\\end{{ex}}\n")
	return debai_word,loigiai_word,latex_tuluan,dap_an

