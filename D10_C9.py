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

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(10000000000000))
    return m


#Tạo dấu cho một số

#[D10_C9_B1_01]-M1. Chọn ngẫu nhiên 1 vật từ 2 nhóm đồ vật. Tìm số phần tử không gian mẫu.
def mjulk_L10_C9_B1_01():   
	#Tạo bậc ngẫu nhiên
	do_vat_1=["chiếc kem que", "cái bút bi", "cuốn vở ô li" , "cuốn truyện cổ tích"]
	do_vat_2=["chiếc kem ốc quế", "cái bút mực","cuốn vở kẻ ngang" , "cuốn tiểu thuyết trinh thám"]
	ten_chung=["chiếc kem","cái bút","cuốn vở", "cuốn truyện"]
	i= random.randint(0,3)
	vat_1=do_vat_1[i]
	vat_2=do_vat_2[i]
	ten_chung=ten_chung[i]
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

	noi_dung=f"Chọn ngẫu nhiên một {ten_chung} từ {m} {vat_1} khác nhau và {n} {vat_2} khác nhau." \
	f" Số phần tử của không gian mẫu là"\

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)={m}+{n}={m+n}$.\n"\

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


#[D10_C9_B1_02]-M1. Cho ngẫu nhiên 2 vật từ 2 nhóm đồ vật. Tìm số phần tử của không gian mẫu.
def mjulk_L10_C9_B1_02():   
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

	noi_dung=f"Một cửa hàng có {m} {vat_1} khác nhau và {n} {vat_2} khác nhau. Chọn ngẫu nhiên một {vat_1} và một {vat_2}. Số phần tử của không gian mẫu là"\

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)={m}.{n}={kq}$.\n"\

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

#[D10_C9_B1_03]-M2. Chọn k quả cầu khác màu. Tìm số phần tử của không gian mẫu.
def mjulk_L10_C9_B1_03():  	
	m=random.randint(10,20)
	n=random.randint(12,20)
	if n==m:
		n=m+random.randint(2,4)
	k=min(m,n)-random.randint(3,8)
	mau_sac=["màu đỏ", "màu xanh", "màu vàng", "màu trắng", "màu tím", "màu đen"]
	random.shuffle(mau_sac)
	noi_dung=f"Một hộp chứa ${{{m}}}$ quả cầu {mau_sac[0]} được đánh số từ ${{1}}$ đến ${{{m}}}$ và ${{{n}}}$ quả cầu {mau_sac[1]} được đánh số từ ${{1}}$ đến ${{{n}}}$." \
			f" Chọn ngẫu nhiên ${{{k}}}$ quả cầu. Số phần tử của không gian mẫu là"

	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)=C^{{{k}}}_{{{m+n}}}={binomial(m+n,k)}$.\n"

	kq=binomial(m+n,k)
	kq2=chinh_hop(k, m+n)
	kq3=m+n+k
	kq4=m*n*k

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

#[D10_C9_B1_04]-M2. Gieo ngẫu nhiên k con xúc xắc. Tìm số phần tử của không gian mẫu.
def mjulk_L10_C9_B1_04():  	

	k=random.randint(1,7)
	noi_dung=f"Gieo ngẫu nhiên 1 con xúc xắc cân đối, đồng chất {k} lần." \
			f" Số phần tử của không gian mẫu là"

	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)=6^{{{k}}}={6**k}$.\n"

	kq=6**k
	kq2=6*k
	kq3=k**6
	kq4=6+k

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


#[D10_C9_B1_05]-M2. Gieo ngẫu nhiên k đồng xu. Tìm số phần tử của không gian mẫu.
def mjulk_L10_C9_B1_05():  	

	k=random.randint(2,15)
	noi_dung=f"Gieo ngẫu nhiên {k} đồng xu." \
			f" Số phần tử của không gian mẫu là"

	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)=2^{{{k}}}={2**k}$.\n"

	kq=2**k
	kq2=2*k
	kq3=k**2
	kq4=2+k

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

#[D10_C9_B1_06]-M2. Chọn k vật từ n vật. Tính số phần tử của không gian mẫu
def mjulk_L10_C9_B1_06():  	
	k=random.randint(3,10)
	n=k+random.randint(1,5)

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


	noi_dung=f"Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} từ ${{{n}}}$ {ten_chung}. Số phần tử của không gian mẫu là"

	kq=binomial(n,k)
	kq2=chinh_hop(k,n)
	kq3=n*k
	kq4=random.choice([binomial(n,k)+random.randint(10,30), abs(binomial(n,k)-random.randint(10,30))])

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={kq}$.\n"	
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

#[D10_C9_B1_07]-M2. Chọn k đối tượng từ 2 nhóm đối tượng. Tính số phần tử của không gian mẫu.
def mjulk_L10_C9_B1_07():  	

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
	so_vat_1=random.randint(6,12)
	so_vat_2=random.randint(6,12)
	n=so_vat_1 + so_vat_2

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} từ {address}."\
	f" Số phần tử của không gian mẫu là"

	kq=binomial(n,k)
	kq2=chinh_hop(k,n)
	kq3=n*k
	kq4=random.choice([binomial(n,k)+random.randint(20,30), abs(binomial(n,k)-random.randint(10,20))])

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={kq}$.\n"	
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

#ĐÚNG -SAI
#[D10_C9_B1_08]-TF-M2. Tạo câu đúng-sai: Chọn 2 nhóm đồ vật.	
def mjulk_L10_C9_B1_08(): 
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


	so_vat_1=random.randint(13,20)
	so_vat_2=random.randint(13,20)
	tong_so=so_vat_1+so_vat_2
	k=random.randint(3,9)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Số phần tử của không gian mẫu là $C^{{{k}}}_{{{tong_so}}}$"
	kq1_F=f"Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Số phần tử của không gian mẫu là $A^{{{k}}}_{{{tong_so}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
			f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{tong_so}}}$."
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{tong_so}}}$."

	k=random.randint(4,9)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1

	kq2_T=f"*Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Số phần tử của biến cố chọn được đúng ${{{k_1}}}$ {vat_1} là " \
		f"${{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k-k_1)}}}$"
	kq2_F=f"Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Số phần tử của biến cố chọn được đúng {k_1} {vat_1} là "\
			 f"${{{binomial(so_vat_1,k_1)}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
	f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n"\
	f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là "\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$."

	k=random.randint(4,9)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)
	kq_false=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq3_T=f"*Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Biến cố chọn có cả {vat_1} và {vat_2} có số phần tử là ${{{kq_true}}}$"
	kq3_F=f"Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Biến cố chọn có cả {vat_1} và {vat_2} có số phần tử là ${{{kq_false}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
			f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là:\n\n "\
			f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n"\
			f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là:\n\n "\
			f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,9)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_2,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Biến cố chọn có ít nhất ${{1}}$ {vat_1} là: ${{{kq_true}}}$"
	kq4_F=f"Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Biến cố chọn có ít nhất có ít nhất ${{1}}$ {vat_1} là: ${{{kq_false}}}$"
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
			f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:\n\n"\
			f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n"\
			f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:\n\n"\
			f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_2}}}={kq_true}$."

	k=random.randint(4,9)
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=binomial(tong_so,k)-binomial(so_vat_1,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq5_T=f"*Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Biến cố chọn có ít nhất ${{1}}$ {vat_2} là: ${{{kq_true}}}$"
	kq5_F=f"Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Biến cố chọn có ít nhất ${{1}}$ {vat_2} là: ${{{kq_false}}}$"
	loigiai_5=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
			f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là:\n\n"\
				f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."
	kq5=random.choice([kq5_T, kq5_F])
	if kq5==kq5_F:
		loigiai_5=f"Khẳng định đã cho là khẳng định sai.\n\n"\
			f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là:\n\n "\
			f"$C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}={kq_true}$."

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
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C9_B1_09]-TF-M2. Gieo một con xúc sắc k lần. Đúng-Sai:
def mjulk_L10_C9_B1_09():
	
	noi_dung=f"Gieo một con xúc sắc cân đối đồng chất ${{2}}$ lần. Xét tính đúng-sai của các khẳng định sau"
	kq1_T=f"*Số phần tử của không gian mẫu là ${{36}}$"
	kq1_F=f"Số phần tử của không gian mẫu là ${{{random.choice([12,24,6])}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
	f"$n(\\Omega)=6.6=36$."
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f"$n(\\Omega)=6.6=36$."

	k=random.choice(["nhất","hai"])
	mat=random.randint(1,6)
	kq2_T=f'*Số phần tử của biến cố "Lần thứ {k} xuất hiện mặt {mat} chấm bằng ${{6}}$"'
	kq2_F=f'Số phần tử của biến cố "Lần thứ {k} xuất hiện mặt {mat} chấm bằng ${{{random.choice([1, random.randint(2,5), 12])}}}$"'
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
		f"Số phần tử của biến cố lần thứ {k} xuất hiện mặt {mat} chấm bằng ${{6}}$."
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f"Số phần tử của biến cố lần thứ {k} xuất hiện mặt {mat} chấm bằng ${{6}}$."

	k=random.randint(5,10)
	m=random.randint(9,11)

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):	 
			if i+j>k:
				t=t+1
				list_kq.append(f"({i};{j})")
			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")
	
	kq3_T=f'*Số phần tử của biến cố "Tổng số chấm của hai lần gieo lớn ${{{k}}}$ bằng ${{{t}}}$"'
	kq3_F=f'Số phần tử của biến cố "Tổng số chấm của hai lần gieo lớn ${{{k}}}$ bằng ${{{t_kq2}}}$"'
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
		f'Biến cố "Tổng số chấm của hai lần gieo lớn ${{{k}}}$" là:\n\n'\
		f'$\\{{{list_kq}\\}}$.\n\n'\
		f'Số phần tử bằng ${{{t}}}$.'
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f'Biến cố "Tổng số chấm của hai lần gieo lớn ${{{k}}}$" là:\n\n'\
		f'$\\{{{list_kq} \\}}$.\n\n'\
		f'Số phần tử bằng ${{{t}}}$.'

	k=random.randint(10,30)
	t=0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):
			if i*j>=k:
				t=t+1
				list_kq.append(f"({i};{j})")
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")

	kq4_T=f'*Số phần tử của biến cố "Tích số chấm của hai lần gieo không nhỏ hơn ${{{k}}}$ bằng ${{{t}}}$"'
	kq4_F=f'Số phần tử của biến cố "Tích số chấm của hai lần gieo không nhỏ hơn ${{{k}}}$ bằng ${{{t+random.randint(1,5)}}}$"'
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
		f'Biến cố "tích số chấm của hai lần gieo không nhỏ hơn ${{{k}}}$ là:\n\n'\
		f'$\\{{{list_kq}\\}}$\n\n'\
		f'Số phần tử là ${{{t}}}$.'
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f'Biến cố "Tích số chấm của hai lần gieo không nhỏ hơn ${{{k}}}$ là:\n\n'\
		f'$\\{{{list_kq}\\}}$\n\n'\
		f'Số phần tử là ${{{t}}}$.'

	k=random.randint(2,5)
	t=0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):
			if i+j%k==0:
				t=t+1
				list_kq.append(f"({i};{j})")
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")

	kq5_T=f'* Số phần tử của biến cố "Tổng số chấm của hai lần gieo chia hết cho ${{{k}}}$ bằng ${{{t}}}$"' 
	kq5_F=f' Số phần tử của biến cố "Tổng số chấm của hai lần gieo chia hết cho ${{{k}}}$ bằng ${{{t+random.randint(1,5)}}}$"'
	kq5=random.choice([kq5_T, kq5_F])
	loigiai_5=f'Khẳng định đã cho là khẳng định đúng.\n\n'\
		f'Biến cố "Tổng số chấm của hai lần gieo chia hết cho ${{{k}}}$" là \n\n'\
		f'$\\{{{list_kq}\\}}$\n\n'\
		f'Số phần tử là ${{{t}}}$.'
	if kq5==kq5_F:
		loigiai_5=f'Khẳng định đã cho là khẳng định sai.\n\n'\
		f'Biến cố "Tổng số chấm của hai lần gieo chia hết cho ${{{k}}}$" là \n\n'\
		f'$\\{{{list_kq}\\}}$\n\n'\
		f'Số phần tử là ${{{t}}}$.'

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
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C9_B1_10]-TF-M2. Có 3 loại đồ vật. Đúng-Sai
def mjulk_L10_C9_B1_10():
	
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2, sach_3 =do_vat_1[0], do_vat_1[1], do_vat_1[2]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2, truyen_3=do_vat_2[0], do_vat_2[1], do_vat_2[2]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2, buctranh_3=do_vat_3[0], do_vat_3[1], do_vat_3[2]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2, vienbi_3=do_vat_4[0], do_vat_4[1], do_vat_4[2]

	vat_1=[f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=[ f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	vat_3=[ f"{vienbi_3}", f"{truyen_3}", f"{buctranh_3}", f"{sach_3}"]
	address=[ "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=[ "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["trong hộp", "để đọc","để mua", "để mua"]

	i=random.randint(0,len(vat_1)-1)
	vat_1, vat_2, vat_3, address,in_where, ten_chung =vat_1[i], vat_2[i],vat_3[i], address[i], in_where[i], ten_chung[i]

	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"
	#Khai báo số lượng ban đầu
	so_vat_1=random.randint(9,13)
	so_vat_2=random.randint(7,12)
	so_vat_3=random.randint(8,14)
	so_vat_min=min(so_vat_1,so_vat_2,so_vat_3)
	n= so_vat_1 + so_vat_2+so_vat_3

	
	#Tạo số lượng cần lấy
	k=random.randint(4, so_vat_min)
	t=binomial(n,k)

	noi_dung=f'Một {address} có ${{{so_vat_1}}}$ {vat_1}, ${{{so_vat_2}}}$ {vat_2} và  ${{{so_vat_3}}}$ {vat_3}.' \
	f' Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Xét tính đúng-sai của các khẳng định sau'
	kq1_T=f'*Số phần tử của không gian mẫu là ${{{t}}}$' 
	kq1_F=f'Số phần tử của không gian mẫu là ${{{t+random.randint(1,10)}}}$'
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f'Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={{{t}}}$.'
	loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'	
	if kq1==kq1_F:
		loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	m=random.randint(1,k)
	t_kq=binomial(so_vat_1,m)*binomial(so_vat_2+so_vat_3,k-m)
	t_kq_false=binomial(so_vat_1,m)

	kq2_T=f'*Biến cố "Có đúng ${{{m}}}$ {vat_1} được chọn" có số phần tử là ${{{t_kq}}}$'
	kq2_F=f'Biến cố "Có đúng ${{{m}}}$ {vat_1} được chọn" có số phần tử là ${{{t_kq_false}}}$'
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f'Số cách chọn có đúng ${{{m}}}$ {vat_1} được chọn là: $C^{{{m}}}_{{{so_vat_1}}}.C^{{{k-m}}}_{{{so_vat_2+so_vat_3}}}={t_kq}.$'
	loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	
	if kq2==kq2_F:
		loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	t_kq=binomial(n,k)-binomial(so_vat_1+so_vat_3,k)
	
	kq3_T=f'*Biến cố "Có ít nhất một {vat_2} được chọn" có số phần tử là ${{{t_kq}}}$' 
	kq3_F=f'Biến cố "Có ít nhất một {vat_2} được chọn" có số phần tử là ${{{t_kq+random.randint(1,4)}}}$ '
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f'Số cách chọn có ít nhất một {vat_2} được chọn là: $C^{{{k}}}_{{{n}}}-C^{{{k}}}_{{{so_vat_1+so_vat_3}}}={t_kq}$'
	loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n{HDG}'
	if kq3==kq3_F:
		loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	t_2mau=binomial(so_vat_1+so_vat_2,k)+binomial(so_vat_2+so_vat_3,k)+binomial(so_vat_3+so_vat_1,k)
	t_1mau=binomial(so_vat_1,k)+binomial(so_vat_2,k)+binomial(so_vat_3,k)
	t_kq=t_2mau-2*t_1mau
	list_PA =[kq1, kq2, kq3]

	kq4_T=f'*Biến cố "Có đúng hai loại {ten_chung} được chọn" có số phần tử là ${{{t_kq}}}$'
	kq4_F=f'Biến cố "Có đúng hai loại {ten_chung} được chọn" có số phần tử là ${{{t_2mau}}}$ ' 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f'Số cách chọn chỉ có một loại {ten_chung} là: $C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}}$\n\n'\
	f'Số cách chọn có đúng hai loại {ten_chung} là:\n\n $C^{{{k}}}_{{{so_vat_1+so_vat_2}}}+C^{{{k}}}_{{{so_vat_2+so_vat_3}}}+C^{{{k}}}_{{{so_vat_1+so_vat_3}}}'\
	f"-2(C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}})={t_2mau}-{2*t_1mau}={t_kq}$."
	loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'	
	if kq4==kq4_F:
		loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	t_2mau=binomial(so_vat_1+so_vat_2,k)+binomial(so_vat_2+so_vat_3,k)+binomial(so_vat_3+so_vat_1,k)
	t_1mau=binomial(so_vat_1,k)+binomial(so_vat_2,k)+binomial(so_vat_3,k)
	t_kq=binomial(n,k)-t_2mau-3*t_1mau
	t_3mau=so_vat_1*so_vat_2*so_vat_3

	kq5_T=f'*Biến cố "Cả 3 loại {ten_chung} đều được chọn" có số phần tử là ${{{t_kq}}}$' 
	kq5_F=f'Biến cố "Cả 3 loại {ten_chung} đều được chọn" có số phần tử là ${{{t_3mau}}}$ '
	kq5=random.choice([kq5_T, kq5_F])
	HDG=f'Số cách chọn chỉ có một loại {ten_chung} là: $C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}}={t_1mau}$\n\n'\
	f'Số cách chọn có cả 3 loại {ten_chung} là:\n\n '\
	f'$C^{{{k}}}_{{{n}}}-(C^{{{k}}}_{{{so_vat_1+so_vat_2}}}+C^{{{k}}}_{{{so_vat_2+so_vat_3}}}+C^{{{k}}}_{{{so_vat_1+so_vat_3}}})'\
	f"-3(C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}})={binomial(n,k)}-{t_2mau}-{3*t_1mau}={t_kq}$."
	loigiai_5=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	if kq5==kq5_F:
		loigiai_5=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'	
	#Trộn các phương án
	list_PA.append(kq4)
	list_PA.append(kq5)
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
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C9_B1_11]-TF-M2. Có n tấm thẻ, lấy ngẫu nhiên k thẻ. Đúng-Sai: không gian mẫu, các thẻ đều chẵn (lẻ), ít nhất một thẻ chia hết cho m, m thẻ chẵn (lẻ) được chọn
def mjulk_L10_C9_B1_11():
	n=random.randint(15,50)
	k=random.randint(3,7)

	noi_dung=f'Có ${{{n}}}$ tấm thẻ được đánh số từ ${{1}}$ đến ${{{n}}}$. Lấy ngẫu nhiên ${{{k}}}$ thẻ.\n\n'\
	f'Xét tính đúng-sai của các khẳng định sau'

	t_kq=binomial(n,k)
	kq1_T=f'*$n(\\Omega)={t_kq}$' 
	kq1_F=f'$n(\\Omega)={chinh_hop(k,n)}$'
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f'Số phần tử của không gian mẫu là $n(\\Omega)=C^{{{k}}}_{{{n}}}={t_kq}$.'
	loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	if kq1==kq1_F:
	    loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	chon=random.choice(['chẵn', 'lẻ'])
	dem_chan, dem_le= 0, 0	
	for i in range(1,n+1):
		if i%2==0:
			dem_chan+=1
		if i%2!=0:
			dem_le+=1
	if chon=="chẵn": 
		dem=dem_chan
	else:
		dem=dem_le
	t_kq=binomial(dem,k)

	ten_bienco=["A","B","C","D","E"]
	random.shuffle(ten_bienco)
	kq2_T=f'*Gọi ${{{ten_bienco[0]}}}$ là biến cố "Số ghi trên các tấm thẻ đều là số {chon}". Khi đó $n({ten_bienco[0]})={t_kq}$'
	kq2_F=f'Gọi ${{{ten_bienco[0]}}}$ là biến cố "Số ghi trên các tấm thẻ đều là số {chon}". Khi đó $n({ten_bienco[0]})={t_kq+random.randint(1,3)}$'
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f'Từ ${{1}}$ đến ${{{n}}}$ có ${{{dem}}}$ số {chon}. Do đó $n(A)=C^{{{k}}}_{{{dem}}}={t_kq}$.'
	loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	if kq2==kq2_F:
	    loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'
	
	m=random.randint(2,6)
	dem= 0
	for i in range(1,n+1):
		if i%m==0:
			dem+=1
	t_kq=binomial(n,k)-binomial(n-dem,k)

	kq3_T=f'*Gọi ${{{ten_bienco[1]}}}$ là biến cố "Có ít nhất một thẻ ghi số chia hết cho ${{{m}}}$". Khi đó $n({ten_bienco[1]})={t_kq}$' 
	kq3_F=f'Gọi ${{{ten_bienco[1]}}}$ là biến cố "Có ít nhất một thẻ ghi số chia hết cho ${{{m}}}$". Khi đó $n({ten_bienco[1]})={t_kq+random.randint(1,3)}$'
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f'Từ ${{1}}$ đến ${{{n}}}$ có ${{{dem}}}$ số chia hết cho ${{{m}}}$.\n\n'\
	f'Số cách chọn ${{{k}}}$ thẻ có ít nhất một thẻ ghi số chia hết cho ${{{m}}}$ là: '\
	f'$C^{{{k}}}_{{{n}}}-C^{{{k}}}_{{{n-dem}}}={t_kq}$.'
	loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	if kq3==kq3_F:
	    loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	m=random.randint(2,k)
	chon=random.choice(['chẵn', 'lẻ'])
	dem_chan, dem_le= 0, 0	
	for i in range(1,n+1):
		if i%2==0:
			dem_chan+=1
		if i%2!=0:
			dem_le+=1
	if chon=="chẵn": 
		dem=dem_chan
		
	else:
		dem=dem_le

	if chon=="chẵn":
		t_kq=binomial(dem_chan,m)*binomial(dem_le,k-m)
		t_kq_false=t_kq=binomial(dem_chan,m)
		HDG=f'Từ ${{1}}$ đến ${{{n}}}$ có ${{{dem}}}$ số {chon}.\n\n'\
		f'Số cách chọn "Có đúng ${{{m}}}$ thẻ {chon} được chọn" là $C^{{{m}}}_{{{dem_chan}}}.C^{{{k-m}}}_{{{dem_le}}}={t_kq}$.'
	else:
		t_kq=binomial(dem_le,m)*binomial(dem_chan,k-m)
		t_kq_false=binomial(dem_le,m)
		HDG=f'Từ ${{1}}$ đến ${{{n}}}$ có ${{{dem}}}$ số {chon}.\n\n'\
		f'Số cách chọn "Có đúng ${{{m}}}$ thẻ {chon} được chọn" là $C^{{{m}}}_{{{dem_le}}}.C^{{{k-m}}}_{{{dem_chan}}}={t_kq}$.'

	kq4_T=f'*Gọi ${{{ten_bienco[2]}}}$ là biến cố "Có đúng ${{{m}}}$ thẻ {chon} được chọn". Khi đó $n({ten_bienco[1]})={t_kq}$'
	kq4_F=f'Gọi ${{{ten_bienco[2]}}}$ là biến cố "Có đúng ${{{m}}}$ thẻ {chon} được chọn". Khi đó $n({ten_bienco[1]})={t_kq_false}$' 
	kq4=random.choice([kq4_T, kq4_F])

	loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	if kq4==kq4_F:
	    loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
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

	noi_dung_loigiai=f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"\
	f"\n\n a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n \n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTF\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"        

	return debai,debai_latex,loigiai_word,dap_an

#Bài 2- Xác suất

#[D10_C9_B2_01]-M2. Chọn n đối tượng tự từ 2 nhóm đối tượng. Tính xác suất k vật được chọn.
def mjulk_L10_C9_B2_01():  	

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
	so_vat_2=random.randint(10,15)
	tong_so= so_vat_1 + so_vat_2

	
	#Tạo số lượng cần lấy
	k=random.randint(5,10)
	k_1=random.randint(2,k-1)
	k_2=k-k_1

	chon=random.randint(1,2)
	
	if chon==1:
		noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}." \
		f" Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Xác suất để có đúng ${{{k_1}}}$ {vat_1} được chọn là"
		kq=phan_so((binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2))/binomial(tong_so,k))
		kq2=phan_so((binomial(so_vat_1,k_1)+binomial(so_vat_2,k_2))/binomial(tong_so,k))
		kq3=phan_so(binomial(so_vat_1,k_1)/binomial(tong_so,k))
		kq4=phan_so(random.choice([binomial(tong_so,k_1)/binomial(tong_so,k), (binomial(tong_so,k)+random.randint(100,200))/binomial(tong_so,k), (abs(binomial(tong_so,k)-random.randint(50,100)))/binomial(tong_so,k)]))

		noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$.\n\n"\
		f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_1}}}$ {vat_1} là: $C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$.\n\n"\
		f"Xác suất để có đúng ${{{k_1}}}$ {vat_1} được chọn là: $P=\\dfrac{{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}}}{{{binomial(tong_so,k)}}}={(phan_so((binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2))/binomial(tong_so,k)))}$"
	
	if chon==2:

		noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}." \
			f"  Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Xác suất để có đúng ${{{k_2}}}$ {vat_2} là"		

		kq=phan_so((binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2))/binomial(tong_so,k))
		kq2=phan_so((binomial(so_vat_1,k_1)+binomial(so_vat_2,k_2))/binomial(tong_so,k))
		kq3=phan_so(binomial(so_vat_1,k_1)/binomial(tong_so,k))
		kq4=phan_so(random.choice([binomial(tong_so,k_1)/binomial(tong_so,k), (binomial(tong_so,k)+random.randint(100,200))/binomial(tong_so,k)]))

		noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$.\n\n"\
		f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} trong đó có đúng ${{{k_2}}}$ {vat_2} là: $C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$.\n\n"\
		f"Xác suất để có đúng ${{{k_2}}}$ {vat_2} được chọn là: $P=\\dfrac{{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}}}{{{binomial(tong_so,k)}}}={(phan_so((binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2))/binomial(tong_so,k)))}$"

	
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

#[D10_C9_B2_02]-M3. Chọn n vật từ 2 nhóm. Tính xác suất cả 2 nhóm đều được chọn.
def mjulk_L10_C9_B2_02():  	

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
	so_vat_2=random.randint(10,15)
	tong_so= so_vat_1 + so_vat_2

	
	#Tạo số lượng cần lấy
	k=random.randint(5,10)
	k_1=random.randint(2,k-1)
	k_2=k-k_1

		
	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}." \
		f" Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Xác suất để cả {vat_1} và {vat_2} được chọn là"		

	kq=phan_so((binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k))/binomial(tong_so,k))
	kq2=phan_so((binomial(so_vat_1,k)*binomial(so_vat_2,k))/binomial(tong_so,k))
	kq3=phan_so(binomial(tong_so,k_1)/binomial(tong_so,k))
	kq4=phan_so(random.choice([(binomial(tong_so,k_1)+binomial(tong_so,k_2))/binomial(tong_so,k), (abs(binomial(tong_so,k)-random.randint(50,100)))/binomial(tong_so,k)]))

	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{tong_so}}}={binomial(tong_so,k)}$.\n\n"\
	f"Số cách chọn có cả {vat_1} và {vat_2} là:"\
					f" $C^{{{k}}}_{{{tong_so}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={kq}$.\n\n"\
	f"Xác suất để cả {vat_1} và {vat_2} được chọn là: $P=\\dfrac{{{binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)}}}{{{binomial(tong_so,k)}}}={(phan_so((binomial(tong_so,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k))/binomial(tong_so,k)))}$"

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

#[D10_C9_B2_03]-M2. Cho một quả cầu từ n quả cầu được đánh số. Tính xác suất quả cầu ghi số là chẵn (lẻ).
def mjulk_L10_C9_B2_03():   
    #Tạo bậc ngẫu nhiên
	n =random.randint(15,40)
	chan_le=random.choice(["chẵn", "lẻ"])

	t=0
	list_kq=[]
	if chan_le=="chẵn":
		for i in range(1,n+1):    	
			if i%2==0:
				t=t+1
				list_kq.append(i)
	else:
		for i in range(1,n+1):
			if i%2!=0:
				t=t+1
				list_kq.append(i)
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")

    
	kq=f"{phan_so(t/n)}"
	kq2=f"{phan_so((t+1)/n)}"
	kq3=f"{phan_so((t+random.randint(2,4))/n)}"
	kq4=f"{phan_so((t+random.randint(5,7))/n)}"

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một hộp chứa {n} quả cầu cùng kích thước được đánh số từ 1 đến {n}. Chọn ngẫu nhiên 1 quả cầu từ hộp." \
	f" Tính xác suất của biến cố “Số ghi trên quả cầu được chọn là một số {chan_le}”."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)={n}$.\n\n"\
	f"Gọi ${{A}}$ là biến cố số ghi trên quả cầu được là một số {chan_le}.\n\n"\
	f"${{A}}=\\{{{list_kq}\\}}\\Rightarrow n(A)={t}$.\n\n"\
	f"Xác suất của biến cố ${{A}}$ là: $P=\\dfrac{{{t}}}{{{n}}}={phan_so(t/n)}$.\n"
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D10_C9_B2_04]-M3. Cho một quả cầu từ n quả cầu được đánh số. Tính xác suất quả là số chẵn (lẻ) và chia hết cho k.
def mjulk_L10_C9_B2_04():   
    #Tạo bậc ngẫu nhiên
	n =random.randint(15,40)	
	chan_le=random.choice(["chẵn", "lẻ"])
	if chan_le=="chẵn":
		k=random.choice([4,6,8,10,12])
	if chan_le=="lẻ":
		k=random.choice([3,5,7,9])
	#if k in [2,4,6]: chan_le="chẵn"
	t=0
	list_kq=[]
	if chan_le=="chẵn":
		for i in range(1,n+1):    	
			if i%k==0 and i%2==0:
				t=t+1
				list_kq.append(i)
	else:
		for i in range(1,n+1):
			if i%k==0 and i%2!=0:
				t=t+1
				list_kq.append(i)
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")

    
	kq=f"{phan_so(t/n)}"
	kq2=f"{phan_so((t+1)/n)}"
	kq3=f"{phan_so((t+random.randint(2,4))/n)}"
	kq4=f"{phan_so((t+random.randint(5,7))/n)}"

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một hộp chứa {n} quả cầu cùng kích thước được đánh số từ 1 đến {n}. Chọn ngẫu nhiên 1 quả cầu từ hộp." \
	f" Xác suất của biến cố “Số ghi trên quả cầu được chọn là một số {chan_le} và chia hết cho {k}” bằng"

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)={n}$.\n\n"\
	f"Gọi ${{A}}$ là biến cố số ghi trên quả cầu được chọn vừa là một số {chan_le} và chia hết cho {k}.\n\n"\
	f"${{A}}=\\{{{list_kq}\\}}\\Rightarrow n(A)={t}$.\n\n"\
	f"Xác suất của biến cố ${{A}}$ là: $P=\\dfrac{{{t}}}{{{n}}}={phan_so(t/n)}$.\n"
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D10_C9_B2_05]-M2. Cho một hộp chứa n tấm thẻ đánh số. Tính xác suất thẻ được chọn ghi số thuộc [a;b].
def mjulk_L10_C9_B2_05():   
    #Tạo bậc ngẫu nhiên
	n =random.randint(15,40)
	k=random.choice([3,4,5,6])	
	a=random.randint(1,6)
	b=n-random.randint(1,4)	
	t=b-a+1
	
    
	kq=f"{phan_so(t/n)}"
	kq2=f"{phan_so((t+1)/n)}"
	kq3=f"{phan_so((t+random.randint(2,4))/n)}"
	kq4=f"{phan_so((t+random.randint(5,7))/n)}"

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một hộp chứa {n} thẻ được đánh số từ 1 đến {n}. Chọn ngẫu nhiên 1 quả thẻ từ hộp." \
	f" Gọi ${{A}}$ là biến cố “Số ghi trên thẻ được chọn là một số thuộc đoạn ${{[{a};{b}]}}$”."\
	f" Xác suất của biến cố ${{A}}$ là"
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)={n}$.\n\n"\
	f"$n(A)={b}-{a}+1={b-a+1}$.\n\n"\
	f" Xác suất của biến cố ${{A}}$ là $P=\\dfrac{{{t}}}{{{n}}}={phan_so(t/n)}$.\n"  
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D10_C9_B2_06]-M2. Gieo 2 con xúc xắc. Tính xác suất để  i + j>k.
def mjulk_L10_C9_B2_06():   
    #Tạo bậc ngẫu nhiên
	
	k=random.randint(5,10)
	m=random.randint(9,11)

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):	 
			if i+j>k:
				t=t+1
				list_kq.append(f"({i};{j})")
			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")
	
    
	kq=t
	kq2=t_kq2
	kq3=abs(t-2)
	kq4=t+3

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]


	#Tạo các phương án
	pa_A= f"*${{{phan_so(kq/36)}}}$"
	pa_B= f"${{{phan_so(kq2/36)}}}$"
	pa_C= f"${{{phan_so(kq3/36)}}}$"
	pa_D= f"${{{phan_so(kq4/36)}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Gieo một con xúc xắc cân đối và đồng chất hai lần." \
	f" Gọi ${{A}}$ là biến cố “Tổng số chấm của hai lần gieo lớn hơn {k}”."\
	f" Xác suất của biến cố ${{A}}$ bằng"
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu: $n(\\Omega)=36$.\n\n"\
	f"${{A}}=\\{{{list_kq}\\}}$. \n\n Vậy số phần tử của biến cố ${{A}}$ là ${{{t}}}$.\n\n"\
	f" Xác suất của biến cố ${{A}}$ là: $P=\\dfrac{{{t}}}{{{36}}}={phan_so(t/36)}$.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D10_C9_B2_07]-M2. Gieo 2 con xúc xắc. Tính xác suất để  i + j<k.
def mjulk_L10_C9_B2_07():   
    #Tạo bậc ngẫu nhiên
	
	k=random.randint(4,10)
	m=random.randint(9,11)

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):	 
			if i+j<k:
				t=t+1
				list_kq.append(f"({i};{j})")
			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")
	
    
	kq=t
	kq2=t_kq2
	kq3=abs(t-2)
	kq4=t+3

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]


	#Tạo các phương án
	pa_A= f"*${{{phan_so(kq/36)}}}$"
	pa_B= f"${{{phan_so(kq2/36)}}}$"
	pa_C= f"${{{phan_so(kq3/36)}}}$"
	pa_D= f"${{{phan_so(kq4/36)}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Gieo một con xúc xắc cân đối và đồng chất hai lần." \
	f" Gọi ${{A}}$ là biến cố “Tổng số chấm của hai lần gieo nhỏ hơn {k}”."\
	f" Xác suất của biến cố ${{A}}$ bằng"
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu: $n(\\Omega)=36$.\n\n"\
	f"${{A}}=\\{{{list_kq}\\}}$. \n\n Vậy số phần tử của biến cố ${{A}}$ là ${{{t}}}$.\n\n"\
	f" Xác suất của biến cố ${{A}}$ là: $P=\\dfrac{{{t}}}{{{36}}}={phan_so(t/36)}$.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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


#[D10_C9_B2_08]-M2. Gieo 2 con xúc xắc. Tính xác suất để  i + j=k.
def mjulk_L10_C9_B2_08():   
    #Tạo bậc ngẫu nhiên
	
	k=random.randint(4,10)
	m=random.randint(9,11)

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):	 
			if i+j==k:
				t=t+1
				list_kq.append(f"({i};{j})")
			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")
	
    
	kq=t
	kq2=t_kq2
	kq3=abs(t-2)
	kq4=t+3

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]


	#Tạo các phương án
	pa_A= f"*${{{phan_so(kq/36)}}}$"
	pa_B= f"${{{phan_so(kq2/36)}}}$"
	pa_C= f"${{{phan_so(kq3/36)}}}$"
	pa_D= f"${{{phan_so(kq4/36)}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Gieo một con xúc xắc cân đối và đồng chất hai lần." \
	f" Gọi ${{A}}$ là biến cố “Tổng số chấm của hai lần gieo bằng {k}”."\
	f" Xác suất của biến cố ${{A}}$ bằng"
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu: $n(\\Omega)=36$.\n\n"\
	f"${{A}}=\\{{{list_kq}\\}}$. \n\n Vậy số phần tử của biến cố ${{A}}$ là ${{{t}}}$.\n\n"\
	f" Xác suất của biến cố ${{A}}$ là: $P=\\dfrac{{{t}}}{{{36}}}={phan_so(t/36)}$.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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


#[D10_C9_B2_09]-M3. Gieo 2 con xúc xắc. Tìm biến cố giao: i + j = k và i.j <(>) m.
def mjulk_L10_C9_B2_09():      
	
	k=random.randint(6,8)
	m=random.randint(6,10)
	chon=random.choice(["nhỏ hơn", "lớn hơn"])

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):
			if chon=="nhỏ hơn":	 
				if i+j==k and i*j<m:
					t=t+1
					list_kq.append(f"({i};{j})")
			else:
				if i+j==k and i*j>m:
					t=t+1
					list_kq.append(f"({i};{j})")

			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")	
    
	kq=t
	kq2=t_kq2
	kq3=t_k
	kq4=t_m

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{phan_so(kq/36)}}}$"
	pa_B= f"${{{phan_so(kq2/36)}}}$"
	pa_C= f"${{{phan_so(kq3/36)}}}$"
	pa_D= f"${{{phan_so(kq4/36)}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Gieo một con xúc xắc cân đối và đồng chất hai lần." \
	f" Gọi ${{A}}$ là biến cố “Tổng số chấm của hai lần gieo bằng {k} và tích số chấm của hai lần gieo {chon} {m}”."\
	f" Xác suất của biến cố ${{A}}$ bằng"
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Số phần tử của không gian mẫu: $n(\\Omega)=36$.\n\n"\
					f"${{A}}=\\{{{list_kq}\\}}$. \n\n Số phần tử của biến cố ${{A}}$ là ${{{t}}}$."\
					f" Xác suất của biến cố ${{A}}$ là: $P=\\dfrac{{{t}}}{{{36}}}={phan_so(t/36)}$.\n"
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D10_C9_B1_12]-TF-M2. Tạo câu đúng-sai: Chọn 2 nhóm đồ vật. Đúng-sai: không gian mẫu, xác suất
def mjulk_L10_C9_B1_12(): 
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


	so_vat_1=random.randint(13,20)
	so_vat_2=random.randint(13,20)
	n=so_vat_1+so_vat_2
	k=random.randint(3,9)		

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}."\
	f" Lấy ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Xét tính đúng sai của các khẳng định sau:"

	kq1_T=f"*Số phần tử của không gian mẫu là $C^{{{k}}}_{{{n}}}$"
	kq1_F=f"Số phần tử của không gian mẫu là $A^{{{k}}}_{{{n}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
			f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{n}}}$."
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{n}}}$."

	
	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	t_kq=binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)/binomial(n,k)
	t_kq_false=binomial(so_vat_1,k_1)/binomial(n,k)

	kq2_T=f"*Xác suất của biến cố chọn được đúng ${{{k_1}}}$ {vat_1} là ${phan_so(t_kq)}$"
	kq2_F=f"Xác suất của biến cố chọn được đúng ${{{k_1}}}$ {vat_1} là ${phan_so(t_kq_false)}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{n}}}$.\n\n"\
	f"Số cách chọn {k} {ten_chung} {in_where} trong đó có đúng {k_1} {vat_1} là \n\n"\
				f"$C^{{{k_1}}}_{{{so_vat_1}}}.C^{{{k_2}}}_{{{so_vat_2}}}={binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}$.\n\n"\
	f'Xác suất cần tính là: $P=\\dfrac{{{binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2)}}}{{{binomial(n,k)}}}={phan_so(t_kq)}.$'
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}\n"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG} \n"

	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=(binomial(n,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k))/binomial(n,k)
	kq_false=(binomial(so_vat_1,k_1)*binomial(so_vat_2,k_2))/binomial(n,k)
	

	kq3_T=f"*Xác suất của biến cố chọn có cả {vat_1} và {vat_2} là ${{{phan_so(kq_true)}}}$"
	kq3_F=f"Xác suất của biến cố chọn có cả {vat_1} và {vat_2} là${{{phan_so(kq_false)}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{n}}}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có cả {vat_1} và {vat_2} là:\n\n"\
	f"$C^{{{k}}}_{{{n}}}-C^{{{k}}}_{{{so_vat_1}}}-C^{{{k}}}_{{{so_vat_2}}}={binomial(n,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)}$.\n\n"\
	f'Xác suất cần tính là: $P=\\dfrac{{{binomial(n,k)-binomial(so_vat_1,k)-binomial(so_vat_2,k)}}}{{{binomial(n,k)}}}={phan_so(kq_true)}$.'
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng. \n\n {HDG}"			
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=(binomial(n,k)-binomial(so_vat_2,k))/binomial(n,k)
	kq_false=random.choice([binomial(so_vat_1,k), so_vat_1])/binomial(n,k)
	if kq_false==kq_true: kq_false=kq_true+random.randint(1,10)

	kq4_T=f"*Xác suất của biến cố chọn có ít nhất ${{1}}$ {vat_1} là: ${{{phan_so(kq_true)}}}$"
	kq4_F=f"Xác suất của biến cố chọn có ít nhất ${{1}}$ {vat_1} là: ${{{phan_so(kq_false)}}}$"
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{n}}}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_1} là:\n\n"\
	f"$C^{{{k}}}_{{{n}}}-C^{{{k}}}_{{{so_vat_2}}}={binomial(n,k)-binomial(so_vat_2,k)}$.\n\n"\
	f'Xác suất cần tính là: $P=\\dfrac{{{binomial(n,k)-binomial(so_vat_2,k)}}}{{{binomial(n,k)}}}={phan_so(kq_true)}$.'
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"		
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n{HDG}"


	k_1 =random.randint(2,k-1)
	k_2=k-k_1
	kq_true=(binomial(n,k)-binomial(so_vat_1,k))/binomial(n,k)
	kq_false=random.choice([binomial(so_vat_2,k), so_vat_2])/binomial(n,k)

	kq5_T=f"*Xác suất của biến cố chọn có ít nhất ${{1}}$ {vat_2} là: ${{{phan_so(kq_true)}}}$"
	kq5_F=f"Xác suất của biến cố chọn có ít nhất ${{1}}$ {vat_2} là: ${{{phan_so(kq_false)}}}$"
	HDG=f"Số phần tử của không gian mẫu là số cách chọn ${{{k}}}$ {ten_chung} {in_where}. $n(\\Omega)= C^{{{k}}}_{{{n}}}$.\n\n"\
		f"Số cách chọn ${{{k}}}$ {ten_chung} {in_where} có ít nhất ${{1}}$ {vat_2} là:\n\n "\
		f"$C^{{{k}}}_{{{n}}}-C^{{{k}}}_{{{so_vat_1}}}={binomial(n,k)-binomial(so_vat_1,k)}$.\n\n"\
		f'Xác suất cần tính là: $P=\\dfrac{{{binomial(n,k)-binomial(so_vat_1,k)}}}{{{binomial(n,k)}}}={phan_so(kq_true)}$.'
	kq5=random.choice([kq5_T, kq5_F])
	loigiai_5=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"	
	if kq5==kq5_F:
		loigiai_5=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


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
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C9_B1_13]-TF-M2. Gieo một con xúc sắc 2 lần. Đúng-Sai: không gian mẫu, xác suất.
def mjulk_L10_C9_B1_13():
	
	noi_dung=f"Gieo một con xúc sắc cân đối đồng chất ${{2}}$ lần. Xét tính đúng-sai của các khẳng định sau"
	kq1_T=f"*Số phần tử của không gian mẫu là ${{36}}$"
	kq1_F=f"Số phần tử của không gian mẫu là ${{{random.choice([12,24,6])}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
	f"$n(\\Omega)=6.6=36$."
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f"$n(\\Omega)=6.6=36$."

	k=random.choice(["nhất","hai"])
	mat=random.randint(1,6)
	kq2_T=f'*Xác suất của biến cố "lần thứ {k} xuất hiện mặt {mat} chấm" bằng ${{{phan_so(1/6)}}}$'
	kq2_F=f'Xác suất của biến cố "lần thứ {k} xuất hiện mặt {mat} chấm" bằng ${{{phan_so(random.choice([1, random.randint(2,5), 12])/36)}}}$"'
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f'Số phần tử của không gian mẫu là ${{36}}$.\n\n'\
	f"Số phần tử của biến cố lần thứ {k} xuất hiện mặt {mat} chấm bằng ${{6}}$.\n\n"\
	f'Xác suất cần tính: $P=\\dfrac{{6}}{{36}}={phan_so(1/6)}.$'

	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"		
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	k=random.randint(5,10)
	m=random.randint(9,11)

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):	 
			if i+j>k:
				t=t+1
				list_kq.append(f"({i};{j})")
			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)
	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")
	
	kq3_T=f'*Xác suất của biến cố "Tổng số chấm của hai lần gieo lớn ${{{k}}}$" bằng ${{{phan_so(t/36)}}}$'
	kq3_F=f'Xác suất của biến cố "Tổng số chấm của hai lần gieo lớn ${{{k}}}$" bằng ${{{phan_so(t_kq2/36)}}}$'
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f'Số phần tử của không gian mẫu là ${{36}}$.\n\n'\
	f'Biến cố "tổng số chấm của hai lần gieo lớn ${{{k}}}$" là:\n\n'\
		f'$\\{{{list_kq}\\}}$.\n\n'\
		f'Số phần tử bằng ${{{t}}}$.\n\n'\
		f'Xác suất cần tính là: $P=\\dfrac{{{t}}}{{36}}={phan_so(t/36)}$.'
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"\
		
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	k=random.randint(10,30)
	t=0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):
			if i*j>=k:
				t=t+1
				list_kq.append(f"({i};{j})")
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")

	kq4_T=f'*Xác suất của biến cố "Tích số chấm của hai lần gieo không nhỏ hơn ${{{k}}}$" bằng ${{{phan_so(t/36)}}}$'
	kq4_F=f'Xác suất của biến cố "Tích số chấm của hai lần gieo không nhỏ hơn ${{{k}}}$" bằng ${{{phan_so((t+random.randint(1,3))/36)}}}$'
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f'Số phần tử của không gian mẫu là ${{36}}$.\n\n'\
		f'Biến cố "tích số chấm của hai lần gieo không nhỏ hơn ${{{k}}}$ là:\n\n'\
		f'$\\{{{list_kq}\\}}$\n\n'\
		f'Số phần tử là ${{{t}}}$.'\
		f'Xác suất cần tính là: $P=\\dfrac{{{t}}}{{36}}={phan_so(t/36)}$.'
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	k=random.randint(2,5)
	t=0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):
			if i+j%k==0:
				t=t+1
				list_kq.append(f"({i};{j})")
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")

	kq5_T=f'*Xác suất của biến cố "Tổng số chấm của hai lần gieo chia hết cho ${{{k}}}$" bằng ${{{phan_so(t/36)}}}$' 
	kq5_F=f'Xác suất của biến cố "Tổng số chấm của hai lần gieo chia hết cho ${{{k}}}$" bằng ${{{phan_so((t+random.randint(1,3))/36)}}}$'
	kq5=random.choice([kq5_T, kq5_F])
	HDG=f'Số phần tử của không gian mẫu là ${{36}}$.\n\n'\
			f'Biến cố "tổng số chấm của hai lần gieo chia hết cho ${{{k}}}$" là \n\n'\
		f'$\\{{{list_kq}\\}}$\n\n'\
		f'Số phần tử là ${{{t}}}$.\n\n'\
		f'Xác suất cần tính là: $P=\\dfrac{{{t}}}{{36}}={phan_so(t/36)}$.'
	loigiai_5=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	if kq5==kq5_F:
		loigiai_5=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

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
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C9_B1_14]-TF-M3. Chọn k vật từ 3 nhóm. Xét Đ-S: không gian mẫu, xác suất.
def mjulk_L10_C9_B1_14():
	
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2, sach_3 =do_vat_1[0], do_vat_1[1], do_vat_1[2]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2, truyen_3=do_vat_2[0], do_vat_2[1], do_vat_2[2]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2, buctranh_3=do_vat_3[0], do_vat_3[1], do_vat_3[2]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2, vienbi_3=do_vat_4[0], do_vat_4[1], do_vat_4[2]

	vat_1=[f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=[ f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	vat_3=[ f"{vienbi_3}", f"{truyen_3}", f"{buctranh_3}", f"{sach_3}"]
	address=[ "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=[ "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["trong hộp", "để đọc","để mua", "để mua"]

	i=random.randint(0,len(vat_1)-1)
	vat_1, vat_2, vat_3, address,in_where, ten_chung =vat_1[i], vat_2[i],vat_3[i], address[i], in_where[i], ten_chung[i]

	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"
	#Khai báo số lượng ban đầu
	so_vat_1=random.randint(8,13)
	so_vat_2=random.randint(7,12)
	so_vat_3=random.randint(6,11)
	so_vat_min=min(so_vat_1,so_vat_2,so_vat_3)
	n= so_vat_1 + so_vat_2+so_vat_3

	
	#Tạo số lượng cần lấy
	k=random.randint(4, so_vat_min)
	t=binomial(n,k)
	kg_mau=binomial(n,k)

	noi_dung=f'Một {address} có ${{{so_vat_1}}}$ {vat_1}, ${{{so_vat_2}}}$ {vat_2} và  ${{{so_vat_3}}}$ {vat_3}.' \
	f' Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} {in_where}. Xét tính đúng-sai của các khẳng định sau'
	kq1_T=f'*Số phần tử của không gian mẫu là ${{{t}}}$' 
	kq1_F=f'Số phần tử của không gian mẫu là ${{{t+random.randint(1,10)}}}$'
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f'Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={{{t}}}$.'
	loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'	
	if kq1==kq1_F:
		loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	m=random.randint(1,k)
	t_kq=binomial(so_vat_1,m)*binomial(so_vat_2+so_vat_3,k-m)
	t_kq_false=binomial(so_vat_1,m)

	kq2_T=f'*Xác suất của biến cố "Có đúng ${{{m}}}$ {vat_1} được chọn" là ${{{phan_so(t_kq/kg_mau)}}}$'
	kq2_F=f'Xác suất của biến cố "Có đúng ${{{m}}}$ {vat_1} được chọn" là ${{{phan_so(t_kq_false/kg_mau)}}}$'
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f'Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={{{t}}}$.\n\n'\
	f'Số cách chọn có đúng ${{{m}}}$ {vat_1} được chọn là:\n\n $C^{{{m}}}_{{{so_vat_1}}}.C^{{{k-m}}}_{{{so_vat_2+so_vat_3}}}={t_kq}.$\n\n'\
	f'Xác suất cần tính là: $P=\\dfrac{{{t_kq}}}{{{kg_mau}}}={phan_so(t_kq/kg_mau)}$.'
	loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	
	if kq2==kq2_F:
		loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	t_kq=binomial(n,k)-binomial(so_vat_1+so_vat_3,k)
	
	kq3_T=f'*Xác suất của biến cố "Có ít nhất một {vat_2} được chọn" là ${{{phan_so(t_kq/kg_mau)}}}$' 
	kq3_F=f'Xác suất của biến cố "Có ít nhất một {vat_2} được chọn" là ${{{phan_so(t_kq+random.randint(1,4)/kg_mau)}}}$ '
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f'Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={{{t}}}$.\n\n'\
	f'Số cách chọn có ít nhất một {vat_2} được chọn là:\n\n $C^{{{k}}}_{{{n}}}-C^{{{k}}}_{{{so_vat_1+so_vat_3}}}={t_kq}$.\n\n'\
	f'Xác suất cần tính là: $P=\\dfrac{{{t_kq}}}{{{kg_mau}}}={phan_so(t_kq/kg_mau)}$.'
	loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n{HDG}'
	if kq3==kq3_F:
		loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	t_2mau=binomial(so_vat_1+so_vat_2,k)+binomial(so_vat_2+so_vat_3,k)+binomial(so_vat_3+so_vat_1,k)
	t_1mau=binomial(so_vat_1,k)+binomial(so_vat_2,k)+binomial(so_vat_3,k)
	t_kq=t_2mau-2*t_1mau
	

	kq4_T=f'*Xác suất của biến cố "Có đúng hai loại {ten_chung} được chọn" là ${{{phan_so(t_kq/kg_mau)}}}$'
	kq4_F=f'Xác suất của biến cố "Có đúng hai loại {ten_chung} được chọn" là ${{{phan_so(t_2mau/kg_mau)}}}$ ' 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f'Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={{{t}}}$.\n\n'\
	f'Số cách chọn chỉ có một loại {ten_chung} là: $C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}}$\n\n'\
	f'Số cách chọn có đúng hai loại {ten_chung} là:\n\n $C^{{{k}}}_{{{so_vat_1+so_vat_2}}}+C^{{{k}}}_{{{so_vat_2+so_vat_3}}}+C^{{{k}}}_{{{so_vat_1+so_vat_3}}}'\
	f"-2(C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}})={t_2mau}-{2*t_1mau}={t_kq}$.\n\n"\
	f'Xác suất cần tính là: $P=\\dfrac{{{t_kq}}}{{{kg_mau}}}={phan_so(t_kq/kg_mau)}$.'
	loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'	
	if kq4==kq4_F:
		loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	t_2mau=binomial(so_vat_1+so_vat_2,k)+binomial(so_vat_2+so_vat_3,k)+binomial(so_vat_3+so_vat_1,k)
	t_1mau=binomial(so_vat_1,k)+binomial(so_vat_2,k)+binomial(so_vat_3,k)
	t_kq=binomial(n,k)-t_2mau-3*t_1mau
	t_3mau=so_vat_1*so_vat_2*so_vat_3

	kq5_T=f'*Xác suất của biến cố "Cả 3 loại {ten_chung} đều được chọn" là ${{{phan_so(t_kq/kg_mau)}}}$' 
	kq5_F=f'Xác suất của biến cố "Cả 3 loại {ten_chung} đều được chọn" là ${{{phan_so(t_3mau/kg_mau)}}}$ '
	kq5=random.choice([kq5_T, kq5_F])
	HDG=f'Số phần tử của không gian mẫu là: $C^{{{k}}}_{{{n}}}={{{t}}}$.\n\n'\
	f'Số cách chọn chỉ có một loại {ten_chung} là: $C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}}={t_1mau}$\n\n'\
	f'Số cách chọn có cả 3 loại {ten_chung} là:\n\n '\
	f'$C^{{{k}}}_{{{n}}}-(C^{{{k}}}_{{{so_vat_1+so_vat_2}}}+C^{{{k}}}_{{{so_vat_2+so_vat_3}}}+C^{{{k}}}_{{{so_vat_1+so_vat_3}}})'\
	f"-3(C^{{{k}}}_{{{so_vat_1}}}+C^{{{k}}}_{{{so_vat_2}}}+C^{{{k}}}_{{{so_vat_3}}})={binomial(n,k)}-{t_2mau}-{3*t_1mau}={t_kq}$.\n\n"\
	f'Xác suất cần tính là: $P=\\dfrac{{{t_kq}}}{{{kg_mau}}}={phan_so(t_kq/kg_mau)}$.'
	loigiai_5=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
	if kq5==kq5_F:
		loigiai_5=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'	
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
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"		

	return debai,debai_latex,loigiai_word,dap_an


