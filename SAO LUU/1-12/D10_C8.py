import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
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
					f"Số cách chọn là: $A{{{k}!={kq}}}$.\n"
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

	n=random.randint(30,45)
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


	so_vat_1=random.randint(20,25)
	so_vat_2=random.randint(15,20)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,10)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(5,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
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
	k=random.randint(3,10)
	n=k+random.randint(6,20)

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

	k=random.randint(3,10)
	so_vat_1=random.randint(6,20)
	so_vat_2=random.randint(6,20)
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
	so_vat_1=random.randint(20,25)
	so_vat_2=random.randint(15,20)
	tong_so= so_vat_1 + so_vat_2

	
	#Tạo số lượng cần lấy
	k=random.randint(5,11)
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
	
	n=random.randint(6,30)
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
	
	n=random.randint(6,30)
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
	
	n=random.randint(6,30)
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
	
	n=random.randint(7,30)
	k=random.randint(4,8)
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
	
	n=random.randint(6,30)
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
	
	m=random.randint(6,20)
	n=random.randint(6,20)
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
	
	n=random.randint(10,25)
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
	m=random.randint(10,25) 	
	n=random.randint(10,25)
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

	so_vat_1=random.randint(20,25)
	so_vat_2=random.randint(15,20)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,10)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(5,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là "\
			 f" ${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
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

	so_vat_1=random.randint(20,25)
	so_vat_2=random.randint(15,20)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,10)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(5,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f" {binomial(so_vat_1,k_1)}"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
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

	so_vat_1=random.randint(20,25)
	so_vat_2=random.randint(15,20)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,10)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(5,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f" {binomial(so_vat_1,k_1)}"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
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

	so_vat_1=random.randint(20,25)
	so_vat_2=random.randint(15,20)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,10)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(5,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
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

	so_vat_1=random.randint(20,25)
	so_vat_2=random.randint(15,20)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,10)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} là ${{{binomial(tong_so,k)}}}$"
	kq1_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là ${{{chinh_hop(k, tong_so)}}}$"
	loigiai_1=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where}  là $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$."\

	k=random.randint(5,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	loigiai_2=f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_true}}}$"
	kq3_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là ${{{kq_false}}}$"
	loigiai_3=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là: "\
			 f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	loigiai_4=f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,11)
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

#Bài 3 - Nhị thức Niu-tơn
#[D10_C8_B3_01]-M1. Khai triển (x+a)^n
def mcn__L10_C8_B3_01():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -1), random.randint(1, 6)])	
	n=random.randint(4,6)
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
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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
	n=random.randint(4,6)
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
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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
	n=random.randint(4,6)
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
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

	noi_dung=f"Tìm hệ số của ${{ x^{{{k}}} }}$ trong khai triển biểu thức ${latex(f)}$."

	debai= f"{noi_dung}\n"
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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
			 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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