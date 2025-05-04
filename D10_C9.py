import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
from itertools import permutations
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
    m=latex(Rational(t).limit_denominator(1000000000))
    return m

def la_so_chinh_phuong(n):
    can_bac_hai = int(math.sqrt(n))
    return can_bac_hai * can_bac_hai == n
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def la_hop_so(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def dem_uoc(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
#Tạo dấu cho một số


def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

def tinh_tong_chu_so(so):
    # Lấy giá trị tuyệt đối để đảm bảo không bị lỗi với số âm
    so = abs(so)
    tong = 0
    while so > 0:
        tong += so % 10  # Lấy chữ số cuối cùng
        so //= 10        # Bỏ chữ số cuối cùng
    return tong
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

#[D10_C9_B2_32]-TF-M2. Tạo câu đúng-sai: Chọn 2 nhóm đồ vật. Đúng-sai: không gian mẫu, xác suất
def mjulk_L10_C9_B2_32(): 
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

#[D10_C9_B2_33]-TF-M2. Gieo một con xúc sắc 2 lần. Đúng-Sai: không gian mẫu, xác suất.
def mjulk_L10_C9_B2_33():
	
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

	

#[D10_C9_B2_34]-TF-M3. Chọn k vật từ 3 nhóm. Xét Đ-S: không gian mẫu, xác suất.
def mjulk_L10_C9_B2_34():
	
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


#[D10_C9_B2_35]-TF-M3. XS các btoán về rút thẻ số 2lần không hoàn lại 
def mjulk_L10_C9_B2_35(): 
    a2=random.randint(1,4)
    a1=a2+random.randint(23,45)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)
    b=random.choice([i for i in nhom2])
    danh_sach = [x + y for x in nhom1 for y in nhom2 if x!=y] 
    ds=[x*y for x in nhom1 for y in nhom2 if x!=y] 
    a=len(danh_sach)
    thutu=random.choice(["hai", "nhất"])
    chon =random.randint(1,2)
    if chon ==1:
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Xét phép thử: Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa. Xét tính đúng-sai của các khẳng định sau. "     
        debai_word= f"{noi_dung}\n"
        c=a3-1
        kq1_T=f"*Xác suất để lần thứ {thutu} rút được thẻ ghi số ${{{b}}}$ là ${{{phan_so(c/a)}}}$ " 
        kq1_F=f"Xác suất để lần thứ {thutu} rút được thẻ ghi số ${{{b}}}$ là "
        kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])

        kq1=random.choice([kq1_T, kq1_F])
        HDG=(f" $\\Omega= \\left\\{{  \\left(  i;j       \\right) , {a2} \\le i,j \\le {a1}, i \\ne j  \\right\\}}$ \n\n"
            f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
            f" Gọi A là biến cố lần thứ {thutu} rút được thẻ ghi số ${{{b}}}$ \n\n"
        f" Số kết quả thuận lợi của biến cố A là ${{{c}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        c=(a3-1)*(a3-1)
        kq2_T=f"*Xác suất để lần thứ {thutu} không rút được thẻ ghi số ${{{b}}}$ là "
        kq2_F=f"Xác suất để lần thứ {thutu} không rút được thẻ ghi số ${{{b}}}$ là "

        kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq2=random.choice([kq2_T, kq2_F])
        HDG=(f" Gọi B là biến cố lần thứ {thutu} không rút được thẻ ghi số ${{{b}}}$ \n\n "
         f" Số kết quả thuận lợi của biến cố B là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        c= len([i for i in danh_sach if i % 2 != 0])
        kq3_T=f"*Xác suất để tổng số ghi trên hai thẻ là số lẻ là ${{{phan_so(c/a)}}}$ " 
        kq3_F=f"Xác suất để tổng số ghi trên hai thẻ là số lẻ là "
        kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" Gọi C là biến cố tổng số ghi trên hai thẻ là số lẻ \n\n "
         f" Số kết quả thuận lợi của biến cố C là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")    
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        
    if chon ==2:
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Xét phép thử: Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa. Xét tính đúng-sai của các khẳng định sau. "     
        debai_word= f"{noi_dung}\n"
        m=sum(1 for i in nhom2 if i%2==0)
        c=(a3-1)*m
        kq1_T=f"*Xác suất để lần thứ {thutu} rút được thẻ ghi số chẵn là ${{{phan_so(c/a)}}}$ " 
        kq1_F=f"Xác suất để lần thứ {thutu} rút được thẻ ghi số chẵn là "
        kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])

        kq1=random.choice([kq1_T, kq1_F])
        HDG=(f" $\\Omega= \\left\\{{  \\left(  i;j       \\right) , {a2} \\le i,j \\le {a1}  \\right\\}}$ \n\n"
            f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
            f" Gọi A là biến cố lần thứ {thutu} rút được thẻ ghi số chẵn \n\n"
        f" Số kết quả thuận lợi của biến cố A là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        c=(a3-1)*(a3-2)
        kq2_T=f"*Xác suất để cả hai lần đều không rút được thẻ ghi số ${{{b}}}$ là "
        kq2_F=f"Xác suất để cả hai lần đều không rút được thẻ ghi số ${{{b}}}$ là"

        kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq2=random.choice([kq2_T, kq2_F])
        HDG=(f" Gọi B là biến cố cả hai lần đều không rút được thẻ ghi số ${{{b}}}$ \n\n "
         f" Số kết quả thuận lợi của biến cố B là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


        c= len([i for i in danh_sach if i % 2 == 0])
        kq3_T=f"*Xác suất để tổng số ghi trên hai thẻ là số chẵn là ${{{phan_so(c/a)}}}$ " 
        kq3_F=f"Xác suất để tổng số ghi trên hai thẻ chẵn số chẵn là "
        kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" Gọi C là biến cố tổng số ghi trên hai thẻ là số chẵn \n\n "
         f" Số kết quả thuận lợi của biến cố C là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")    
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"




    danh_sach_moi = list(filter(lambda x: la_so_nguyen_to(x), nhom1))
    k = len(danh_sach_moi)

    c= k*(k-1)

    kq4_T=f"*Xác suất để hai số ghi trên hai thẻ đều là số nguyên tố là ${{{phan_so(c/a)}}}$ "
    kq4_F=f"Xác suất để hai số ghi trên hai thẻ đều là số nguyên tố là " 
    kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f" Gọi D là biến cố hai số ghi trên hai thẻ đều là số nguyên tố là \n\n "
    	f" Từ ${{{a2}}}$ đến ${{{a1}}}$ có ${{{k}}}$ số nguyên tố \n\n"
     f" Số kết quả thuận lợi của biến cố D là ${{{phan_so(c)}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")
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






#[D10_C9_B2_36]-TF-M3. XS các btoán về rút thẻ số 2lần có hoàn trả lại 
def mjulk_L10_C9_B2_36(): 
    a2=random.randint(1,5)
    a1=a2+random.randint(15,45)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)
    b=random.choice([i for i in nhom2])
    danh_sach = [x + y for x in nhom1 for y in nhom2] 
    ds=[x*y for x in nhom1 for y in nhom2 ] 
    a=len(danh_sach)
    thutu=random.choice(["hai", "nhất"])
    chon =random.randint(1,2)
    if chon ==1:
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Xét phép thử: Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa. Xét tính đúng-sai của các khẳng định sau. "     
        debai_word= f"{noi_dung}\n"
        c=a3
        kq1_T=f"*Xác suất để lần thứ {thutu} rút được thẻ ghi số ${{{b}}}$ là ${{{phan_so(c/a)}}}$ " 
        kq1_F=f"Xác suất để lần thứ {thutu} rút được thẻ ghi số ${{{b}}}$ là "
        kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])

        kq1=random.choice([kq1_T, kq1_F])
        HDG=(f" $\\Omega{{= \\left\\{{  \\left(  i;j       \\right) , {a2} \\le i,j \\le {a1}  \\right\\}} }}$ \n\n"
            f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
            f" Gọi A là biến cố lần thứ {thutu} rút được thẻ ghi số ${{{b}}}$ \n\n"
        f" Số kết quả thuận lợi của biến cố A là ${{{c}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        c=(a3-1)*a3
        kq2_T=f"*Xác suất để lần thứ {thutu} không rút được thẻ ghi số ${{{b}}}$ là "
        kq2_F=f"Xác suất để lần thứ {thutu} không rút được thẻ ghi số ${{{b}}}$ là "

        kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq2=random.choice([kq2_T, kq2_F])
        HDG=(f" Gọi B là biến cố lần thứ {thutu} không rút được thẻ ghi số ${{{b}}}$ \n\n "
         f" Số kết quả thuận lợi của biến cố B là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        c= len([i for i in danh_sach if i % 2 != 0])
        kq3_T=f"*Xác suất để tổng số ghi trên hai thẻ là số lẻ là ${{{phan_so(c/a)}}}$ " 
        kq3_F=f"Xác suất để tổng số ghi trên hai thẻ là số lẻ là "
        kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" Gọi C là biến cố tổng số ghi trên hai thẻ là số lẻ \n\n "
         f" Số kết quả thuận lợi của biến cố C là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")    
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"



    if chon ==2:
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Xét phép thử: Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa. Xét tính đúng-sai của các khẳng định sau. "     
        debai_word= f"{noi_dung}\n"
        m=sum(1 for i in nhom2 if i%2==0)
        c=a3*m
        kq1_T=f"*Xác suất để lần thứ {thutu} rút được thẻ ghi số chẵn là ${{{phan_so(c/a)}}}$ " 
        kq1_F=f"Xác suất để lần thứ {thutu} rút được thẻ ghi số chẵn là "
        kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])

        kq1=random.choice([kq1_T, kq1_F])
        HDG=(f" $\\Omega{{= \\left\\{{  \\left(  i;j       \\right) , {a2} \\le i,j \\le {a1}  \\right\\}} }}$ \n\n"
            f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
            f" Gọi A là biến cố lần thứ {thutu} rút được thẻ ghi số chẵn \n\n"
        f" Số kết quả thuận lợi của biến cố A là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        c=(a3-1)*(a3-1)
        kq2_T=f"*Xác suất để cả hai lần đều không rút được thẻ ghi số ${{{b}}}$ là "
        kq2_F=f"Xác suất để cả hai lần đều không rút được thẻ ghi số ${{{b}}}$ là "

        kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq2=random.choice([kq2_T, kq2_F])
        HDG=(f" Gọi B là biến cố cả hai lần đều không rút được thẻ ghi số ${{{b}}}$ \n\n "
         f" Số kết quả thuận lợi của biến cố B là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


        c= len([i for i in danh_sach if i % 2 == 0])
        kq3_T=f"*Xác suất để tổng số ghi trên hai thẻ là số chẵn là ${{{phan_so(c/a)}}}$ " 
        kq3_F=f"Xác suất để tổng số ghi trên hai thẻ chẵn số chẵn là "
        kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
            ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" Gọi C là biến cố tổng số ghi trên hai thẻ là số chẵn \n\n "
         f" Số kết quả thuận lợi của biến cố C là ${{{phan_so(c)}}}$ \n\n"
            f"Xác suất là ${{{phan_so(c/a)}}}$")    
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    danh_sach_moi = list(filter(lambda x: la_so_nguyen_to(x), nhom1))
    k = len(danh_sach_moi)

    c= k*k

    kq4_T=f"*Xác suất để hai số ghi trên hai thẻ là số nguyên tố là ${{{phan_so(c/a)}}}$ "
    kq4_F=f"Xác suất để hai số ghi trên hai thẻ là số nguyên tố là " 
    kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]) 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f" Gọi D là biến cố hai số ghi trên hai thẻ là số nguyên tố\n\n "
        f" Từ ${{{a2}}}$ đến ${{{a1}}}$ có ${{{k}}}$ số nguyên tố \n\n"
     f" Số kết quả thuận lợi của biến cố D là ${{{phan_so(c)}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")
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






#[D10_C9_B2_37]-TF-M3. XS các bài toán rút đồng thời 2 thẻ một lúc
def mjulk_L10_C9_B2_37():
	a2=random.randint(1,5)
	a1=a2+random.randint(15,45)
	a3= (a1-a2)+1
	nhom1 = range(a2, a1 + 1)
	nhom2 = range(a2, a1 + 1)
	b=random.choice([i for i in nhom2])


	sole=len([i for i in range(a2, a1 + 1) if i % 2 != 0])
	sochan=len([i for i in range(a2, a1 + 1) if i % 2 == 0])
	a=math.comb(a3, 2)

	noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Xét phép thử: Rút ngẫu nhiên đồng thời ${{2}}$ thẻ số. Xét tính đúng-sai của các khẳng định sau. "
	debai_word= f"{noi_dung}\n"
	chon =random.randint(1,2)

	if chon ==1: 
		c=sole*sochan

		kq1_T=f"*Xác suất để tổng hai số trên hai thẻ là một số lẻ là ${{{phan_so(c/a)}}}$" 
		kq1_F=f"Xác suất để tổng hai số trên hai thẻ là một số lẻ là "
		kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ",
		        f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
		        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
		kq1=random.choice([kq1_T, kq1_F])
		HDG=(f"${{ n(\\Omega)= {a} }}$ \n\n"
		f" Từ ${{{a2}}}$ đến ${{{a1}}}$ có ${{{sole}}}$ số lẻ và ${{{sochan}}}$ số chẵn. \n\n"
		f" Gọi ${{A}}$ là biến cố tổng hai số trên hai thẻ là một số lẻ \n\n "
		f" ${{n(A)= {c}}}$ \n\n"
		f" ${{ P(A)= {phan_so(c/a)} }}$")
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"




		c=math.comb(sole, 2)

		kq2_T=f"*Xác suất để tích hai số trên hai thẻ là số lẻ là ${{{phan_so(c/a)}}}$"
		kq2_F=f"Xác suất để tích hai số trên hai thẻ là số lẻ là  "
		kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ",
		     f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
		        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
		kq2=random.choice([kq2_T, kq2_F])
		HDG=	(f" Gọi ${{B}}$ là biến cố tích hai số trên hai thẻ là số lẻ.\n\n"
			f" ${{n(B)= {c}}}$ \n\n"
		f" ${{ P(B)= {phan_so(c/a)} }}$")
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon ==2: 
		c=math.comb(sole,2)+math.comb(sochan,2)

		kq1_T=f"*Xác suất để tổng hai số trên hai thẻ là một số chẵn là ${{{phan_so(c/a)}}}$" 
		kq1_F=f"Xác suất để tổng hai số trên hai thẻ là một số chẵn là "
		kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ",
		        f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
		        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
		kq1=random.choice([kq1_T, kq1_F])
		HDG=(f"${{ n(\\Omega)= {a} }}$ \n\n"
		f" Từ ${{{a2}}}$ đến ${{{a1}}}$ có ${{{sole}}}$ số lẻ và ${{{sochan}}}$ số chẵn. \n\n"
		f" Gọi ${{A}}$ là biến cố tổng hai số trên hai thẻ là một số chẵn \n\n "
		f" ${{n(A)= {c}}}$ \n\n"
		f" ${{ P(A)= {phan_so(c/a)} }}$")
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"




		c=sochan*(a3-1)

		kq2_T=f"*Xác suất để tích hai số trên hai thẻ là số chẵn là ${{{phan_so(c/a)}}}$"
		kq2_F=f"Xác suất để tích hai số trên hai thẻ là số chẵn là  "
		kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ",
		     f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
		        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
		kq2=random.choice([kq2_T, kq2_F])
		HDG=	(f" Gọi ${{B}}$ là biến cố tích hai số trên hai thẻ là số chẵn.\n\n"
			f" ${{n(B)= {c}}}$ \n\n"
		f" ${{ P(B)= {phan_so(c/a)} }}$")
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"



	c=math.comb(a3-1, 2)
	kq3_T=f"*Xác suất để trong hai thẻ rút ra không có thẻ nào ghi số ${{{b}}}$ là ${{{phan_so(c/a)}}}$" 
	kq3_F=f" Xác suất để trong hai thẻ rút ra không có thẻ nào ghi số ${{{b}}}$ là "
	kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ",
	        f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f" Gọi ${{C}}$ là biến cố trong hai thẻ rút ra không có thẻ nào ghi số ${{{b}}}$ \n\n"
		f" ${{n(C)= {c}}}$ \n\n"
	f" ${{ P(C)= {phan_so(c/a)} }}$")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	danh_sach_moi = list(filter(lambda x: la_so_nguyen_to(x), nhom1))
	k = len(danh_sach_moi)

	c= math.comb(k,2)


	kq4_T=f"*Xác suất để rút được hai thẻ đều là số nguyên tố là ${{{phan_so(c/a)}}}$ "
	kq4_F=f"Xác suất để rút được hai thẻ đều là số nguyên tố là  " 
	kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])

	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"Gọi D là biến cố rút được hai thẻ đều là số nguyên tố \n\n"
	f" ${{n(D)={c}}}$ \n\n"
	f" ${{P(D)= {phan_so(c/a)}}}$")
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



#[D10_C9_B2_38]-TF-M3. XS các bài toán chọn 2 người từ một nhóm
def mjulk_L10_C9_B2_38():
	a2=random.randint(10,20)
	a3=random.randint(10,25)
	a1=a2+a3
	a=math.comb(a1, 2)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])

	noi_dung = f"Một đội có ${{{a1}}}$ bạn  trong đó có bạn nữ tên {A} và bạn nam tên {B}. Giáo viên chọn ngẫu nhiên ra hai bạn tham gia hội khoẻ phù đổng của huyện. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	

	c=1
	kq1_T=f"*Xác suất để chọn được cả hai bạn {A} và {B} là ${{{phan_so(c/a)}}}$" 
	kq1_F=f"Xác suất để chọn được cả hai bạn {A} và {B} là "
	kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	kq1=random.choice([kq1_T, kq1_F])
	HDG=(f"${{ n(\\Omega)= {a} }}$ \n\n"
		f" Gọi ${{A}}$ là biến cố chọn được cả hai bạn {A} và {B} \n\n "
		f" ${{n(A)= {c}}}$ \n\n"
		f" ${{ P(A)= {phan_so(c/a)} }}$")	
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c=a1-2
	kq2_T=f"*Xác suất để chọn được {A} mà không chọn được {B} là ${{{phan_so(c/a)}}}$ "
	kq2_F=f"Xác suất để chọn được {A} mà không chọn được {B} là "
	kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	kq2=random.choice([kq2_T, kq2_F])
	HDG=(f" Gọi ${{B}}$ là biến cố chọn được {A} mà không chọn được {B} \n\n "
		f" ${{n(B)= {c}}}$ \n\n"
		f" ${{ P(B)= {phan_so(c/a)} }}$")	
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	c= math.comb(a1-2, 2)
	kq3_T=f"*Xác suất để cả hai bạn {A} và {B} đều không được chọn là ${{{phan_so(c/a)}}}$ " 
	kq3_F=f" Xác suất để cả hai bạn {A} và {B} đều không được chọn là "

	kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f" Gọi ${{C}}$ là biến cố cả hai bạn {A} và {B} đều không được chọn \n\n "
		f" ${{n(C)= {c}}}$ \n\n"
		f" ${{ P(C)= {phan_so(c/a)} }}$")	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	c= a3*(a2-1)
	kq4_T=f"*Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được một bạn nam và một bạn nữ trong đó không có {B} là ${{{phan_so(c/a)}}}$  "
	kq4_F=f"Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được một bạn nam và một bạn nữ trong đó không có {B} là " 
	kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f" Gọi ${{D}}$ là biến cố chọn được một bạn nam và một bạn nữ trong đó không có {B}\n\n "
		f" ${{n(D)= {c}}}$ \n\n"
		f" ${{ P(D)= {phan_so(c/a)} }}$")	
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



#[D10_C9_B2_39]-TF-M3. XS các bài toán chọn 3 người từ một nhóm kiểu 1
def mjulk_L10_C9_B2_39():
    a2=random.randint(10,20)
    a3=random.randint(10,25)
    a1=a2+a3
    a=math.comb(a1, 3)
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])

    noi_dung = f"Một đội có ${{{a1}}}$ bạn  trong đó có bạn nữ tên {A} và bạn nam tên {B}. Giáo viên chọn ngẫu nhiên ra ba bạn tham gia hội khoẻ phù đổng của huyện. Xét tính đúng-sai của các khẳng định sau. "       
    debai_word= f"{noi_dung}\n"
    

    c=a1-2
    kq1_T=f"*Xác suất để trong ba bạn được chọn có cả hai bạn {A} và {B} là ${{{phan_so(c/a)}}}$" 
    kq1_F=f"Xác suất để trong ba bạn được chọn có cả hai bạn {A} và {B} là "
    kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f"${{ n(\\Omega)= {a} }}$ \n\n"
        f" Gọi ${{A}}$ là biến cố trong ba bạn được chọn có cả hai bạn {A} và {B} \n\n "
        f" ${{n(A)= {c}}}$ \n\n"
        f" ${{ P(A)= {phan_so(c/a)} }}$")   
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    c=math.comb(a1-2,2)
    kq2_T=f"*Xác suất để trong ba bạn được chọn có {A} mà không có {B} là ${{{phan_so(c/a)}}}$ "
    kq2_F=f"Xác suất để trong ba bạn được chọn có {A} mà không có {B} là "
    kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
    kq2=random.choice([kq2_T, kq2_F])
    HDG=(f" Gọi ${{B}}$ là biến cố trong ba bạn được chọn có {A} mà không có {B} \n\n "
        f" ${{n(B)= {c}}}$ \n\n"
        f" ${{ P(B)= {phan_so(c/a)} }}$")   
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"



    c= math.comb(a1-2, 3)
    kq3_T=f"*Xác suất để cả hai bạn {A} và {B} đều không được chọn là ${{{phan_so(c/a)}}}$ " 
    kq3_F=f" Xác suất để cả hai bạn {A} và {B} đều không được chọn là "

    kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
    kq3=random.choice([kq3_T, kq3_F])
    HDG=(f" Gọi ${{C}}$ là biến cố cả hai bạn {A} và {B} đều không được chọn \n\n "
        f" ${{n(C)= {c}}}$ \n\n"
        f" ${{ P(C)= {phan_so(c/a)} }}$")   
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    chon =random.randint(1,6)
    if chon ==1:
        c= math.comb(a2-1,2)*a3
        kq4_T=f"*Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nam và một bạn nữ trong đó không có {B} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nam và một bạn nữ trong đó không có {B} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nam và một bạn nữ trong đó không có {B}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   

    if chon ==2:
        c= math.comb(a3,2)*(a2-1)
        kq4_T=f"*Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nữ và một bạn nam trong đó không có {B} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nữ và một bạn nam trong đó không có {B} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nữ và một bạn nam trong đó không có {B}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   

    if chon ==3:
        c= math.comb(a3-1,2)*a2
        kq4_T=f"*Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nữ và một bạn nam trong đó không có {A} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nữ và một bạn nam trong đó không có {A} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nữ và một bạn nam trong đó không có {A}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


    if chon ==4:
        c= math.comb(a3-1,1)*a2
        kq4_T=f"*Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nữ và một bạn nam trong đó có {A} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nữ và một bạn nam trong đó có {A} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nữ và một bạn nam trong đó có {A}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


    if chon ==5:
        c= math.comb(a2-1,1)*a3
        kq4_T=f"*Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nam và một bạn nữ trong đó có {B} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nam và một bạn nữ trong đó có {B} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nam và một bạn nữ trong đó có {B}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


    if chon ==6:
        c= math.comb(a2-1,2)*(a3-1)
        kq4_T=f"*Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nam và một bạn nữ trong đó không có {B} và {A} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Biết trong đội có ${{{a2}}}$ bạn nam, xác suất để chọn được hai bạn nam và một bạn nữ trong đó không có {B} và {A} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nam và một bạn nữ trong đó không có {B} và {A}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


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





#[D10_C9_B2_10]-M1. Cho m nam ,n nữ, xs chọn k nữ(nam)
def mjulk_L10_C9_B2_10():
	k=random.randint(2,6)
	n=k+ random.randint(2,4)
	m=k+random.randint(2,6)
	a=math.comb(n+m,k)
	
	A= random.choice([" văn nghệ toàn trường", "hội khoẻ phù đồng của huyện", "thi đấu võ thuật của tỉnh", "thi đấu thể thao của trường"])
	chon=random.randint(1,2)
	if chon ==1: 
		c=math.comb(m,k)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất chọn được ${{{k}}}$ bạn nam là:"

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" ${{n(A)=C^{{{k}}}_{{{m}}}={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$")

	if chon ==2: 
		c=math.comb(n,k)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất chọn được ${{{k}}}$ bạn nữ là:"

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" ${{n(A)=C^{{{k}}}_{{{n}}}={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$")
	kq=f"${{{phan_so(c/a)} }}$"

	dss=[f"${{{phan_so(c/(a-10))}}}$ ",   f"${{{phan_so(c/(a-5))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

	kq2,kq3,kq4= random.sample(dss,3)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	 
	loigiai_word=my_module.frac_to_dfrac(f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n")
	loigiai_traloingan=my_module.frac_to_dfrac(f"Lời giải:\n {noi_dung_loigiai} \n")
	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex=my_module.frac_to_dfrac( f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n")

	latex_tuluan=my_module.frac_to_dfrac(f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C9_B2_11]-M2. Cho m nam ,n nữ chọn k bạn thoả dk nào đó
def mjulk_L10_C9_B2_11():
	k1=random.randint(1,3)
	k=k1+random.randint(1,3)
	n=k+ random.randint(2,4)
	m=k+random.randint(2,6)
	a=math.comb(n+m,k)
	c=math.comb(m,k)
	A= random.choice([" văn nghệ toàn trường", "hội khoẻ phù đồng của huyện", "thi đấu võ thuật của tỉnh", "thi đấu thể thao của trường"])
	chon=random.randint(1,2)
	if chon ==1: 
		c=math.comb(m,k1)*math.comb(n,k-k1)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất chọn được ${{{k1}}}$ bạn nam là:"

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" ${{n(A)=C^{{{k1}}}_{{{m}}} C^{{{k-k1}}}_{{{n}}}={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$")

	if chon ==2: 
		c=math.comb(n,k1)*math.comb(m,k-k1)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất chọn được ${{{k1}}}$ bạn nữ là:"

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" ${{n(A)=C^{{{k1}}}_{{{n}}} C^{{{k-k1}}}_{{{m}}}  ={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$")
	kq=f"${{{phan_so(c/a)} }}$"

	dss=[f"${{{phan_so(c/(a-6))}}}$ ",   f"${{{phan_so(c/(a-5))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

	kq2,kq3,kq4= random.sample(dss,3)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	 
	loigiai_word=my_module.frac_to_dfrac(f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n")
	loigiai_traloingan=my_module.frac_to_dfrac(f"Lời giải:\n {noi_dung_loigiai} \n")
	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex=my_module.frac_to_dfrac( f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n")

	latex_tuluan=my_module.frac_to_dfrac(f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C9_B2_12]-M1. Cho m nam ,n nữ, xs chọn được ít nhất 1 nữ (nam)
def mjulk_L10_C9_B2_12():
	k=random.randint(2,6)
	n=k+ random.randint(2,4)
	m=k+random.randint(2,6)
	a=math.comb(n+m,k)
	
	A= random.choice([" văn nghệ toàn trường", "hội khoẻ phù đồng của huyện", "thi đấu võ thuật của tỉnh", "thi đấu thể thao của trường"])
	chon=random.randint(1,2)
	if chon ==1: 
		c=math.comb(n,k)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất chọn được ít nhất một bạn nam là:"

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" Gọi ${{A}}$ là biến cố không chọn được bạn nam nào\n\n"
						f" ${{n(A)=C^{{{k}}}_{{{n}}}={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$ \n\n"
						f"  ${{P(\\overline{{A}})= 1- {phan_so(c/a)}= {phan_so(1-(c/a))} }}$ ")

	if chon ==2:
		
		c=math.comb(m,k)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất chọn được ít nhất một bạn nữ là:"

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" Gọi ${{A}}$ là biến cố không chọn được bạn nữ nào\n\n"
						f" ${{n(A)=C^{{{k}}}_{{{m}}}={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$ \n\n"
						f"  ${{P(\\overline{{A}})= 1- {phan_so(c/a)}= {phan_so(1-(c/a))} }}$ ")



	kq=f"${{{phan_so(1-(c/a))} }}$"

	dss=[f"${{{phan_so(c/(a-10))}}}$ ",   f"${{{phan_so(c/(a-5))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

	kq2,kq3,kq4= random.sample(dss,3)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	 
	loigiai_word=my_module.frac_to_dfrac(f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n")
	loigiai_traloingan=my_module.frac_to_dfrac(f"Lời giải:\n {noi_dung_loigiai} \n")
	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex=my_module.frac_to_dfrac( f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n")

	latex_tuluan=my_module.frac_to_dfrac(f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an




#[D10_C9_B2_13]-M2. Cho m nam ,n nữ, chọn k bạn trong đó có (không có) bạn A
def mjulk_L10_C9_B2_13():
	k=random.randint(2,6)
	n=k+ random.randint(2,4)
	m=k+random.randint(2,6)
	a=math.comb(n+m,k)
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])

	A= random.choice([" văn nghệ toàn trường", "hội khoẻ phù đồng của huyện", "thi đấu võ thuật của tỉnh", "thi đấu thể thao của trường"])
	chon=random.randint(1,2)
	if chon ==1: 
		c=math.comb(n+m-1,k-1)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ trong đó có bạn {B}, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất để {B} được chọn là:"

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" Gọi ${{A}}$ là biến cố để {B} được chọn\n\n"
						f" ${{n(A)=C^{{{k-1}}}_{{{n+m-1}}}={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$ \n\n"
					)

	if chon ==2: 
		c=math.comb(n+m-1,k)
		noi_dung=f" Một đội có ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ trong đó có bạn {B}, giáo viên chọn ngẫu nhiên ${{{k}}}$ bạn tham gia {A}. Xác suất để {B} không được chọn là:"

	

		noi_dung_loigiai=(f" ${{n(\\Omega)= C^{{{k}}}_{{{n+m}}} ={a}}}$ \n\n"
						f" Gọi ${{A}}$ là biến cố không chọn được {B}\n\n"
						f" ${{n(A)=C^{{{k}}}_{{{m+n-1}}}={c} }}$ \n\n"
						f" ${{P(A) = {phan_so(c/a)}}}$ \n\n"
					)

	kq=f"${{{phan_so(c/a)} }}$"

	dss=[f"${{{phan_so(c/(a-10))}}}$ ",   f"${{{phan_so(c/(a-5))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

	kq2,kq3,kq4= random.sample(dss,3)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	 
	loigiai_word=my_module.frac_to_dfrac(f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n")
	loigiai_traloingan=my_module.frac_to_dfrac(f"Lời giải:\n {noi_dung_loigiai} \n")
	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex=my_module.frac_to_dfrac( f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n")

	latex_tuluan=my_module.frac_to_dfrac(f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an





#[D10_C9_B2_14]-M1. Tính xs các bài toán về gieo 1 con xúc sắc (nhiều kiểu hỏi)
def mjulk_L10_C9_B2_14(): 
    chon =random.randint(1,2) 
    if chon ==1:
        a=random.randint(1,6)

        noi_dung=f" Gieo ngẫu nhiên một con xúc sắc cân đối và đồng chất. Xác suất để xuất hiện mặt ${{{a}}}$ chấm là"
        noi_dung_loigiai=f" Xác suất để xuất hiện mặt ${{{a}}}$ chấm là ${{{phan_so(1/6)}}}$."

        kq=f"${{{phan_so(1/6)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(6+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(6+random.randint(1,2)))}}}$ "
    if chon ==2:
        a=random.randint(1,6)

        noi_dung=f" Gieo ngẫu nhiên một con xúc sắc cân đối và đồng chất. Xác suất để xuất hiện mặt có số chấm chẵn là"
        noi_dung_loigiai=f" Xác suất để xuất hiện mặt mặt có số chấm chẵn là ${{{phan_so(1/2)}}}$."

        kq=f"${{{phan_so(1/2)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(6+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(6+random.randint(1,2)))}}}$ "

    if chon ==3:
        a=random.randint(1,6)

        noi_dung=f" Gieo ngẫu nhiên một con xúc sắc cân đối và đồng chất. Xác suất để xuất hiện mặt có số chấm lẻ là"
        noi_dung_loigiai=f" Xác suất để xuất hiện mặt mặt có số chấm lẻ là ${{{phan_so(1/2)}}}$."

        kq=f"${{{phan_so(1/2)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(6+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(6+random.randint(1,2)))}}}$ "
    if chon ==4:
        a=random.randint(1,6)

        noi_dung=f" Gieo ngẫu nhiên một con xúc sắc cân đối và đồng chất. Xác suất để xuất hiện mặt có số chấm chia hết cho 3 là"
        noi_dung_loigiai=f" Xác suất để xuất hiện mặt mặt có số chấm chia hết cho 3 là ${{{phan_so(1/3)}}}$."

        kq=f"${{{phan_so(1/3)}}}$ "
        kq2=f"${{{phan_so(1/(6-random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(6+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(6-random.randint(1,2)))}}}$ "
    if chon ==5:
        a=random.randint(1,6)

        noi_dung=f" Gieo ngẫu nhiên một con xúc sắc cân đối và đồng chất. Xác suất để xuất hiện mặt có số chấm chia hết cho 4 là"
        noi_dung_loigiai=f" Xác suất để xuất hiện mặt mặt có số chấm chia hết cho 4 là ${{{phan_so(1/6)}}}$."

        kq=f"${{{phan_so(1/6)}}}$ "
        kq2=f"${{{phan_so(1/(6-random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(6+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(6-random.randint(1,2)))}}}$ "
    if chon ==6:
        a=random.randint(1,6)

        noi_dung=f" Gieo ngẫu nhiên một con xúc sắc cân đối và đồng chất. Xác suất để xuất hiện mặt có số chấm chia hết cho 5 là"
        noi_dung_loigiai=f" Xác suất để xuất hiện mặt mặt có số chấm chia hết cho 5 là ${{{phan_so(1/6)}}}$."

        kq=f"${{{phan_so(1/6)}}}$ "
        kq2=f"${{{phan_so(1/(6-random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(6+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(6-random.randint(1,2)))}}}$ "
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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



#[D10_C9_B2_15]-M2. xs các btoán về gieo 2 con xúc sắc (rất nhiều kiểu hỏi)
def mjulk_L10_C9_B2_15(): 
    chon =random.randint(1,27) 
    if chon ==1:
        a=random.randint(1,6)

        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 2 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 2 là ${{{phan_so(1/36)}}}$."

        kq=f"${{{phan_so(1/36)}}}$ "
        kq2=f"${{{phan_so(1/(36-random.randint(10,20)))}}}$  "
        kq3=f"${{{phan_so(2/(36-random.randint(10,20)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(1,20)))}}}$ "
    if chon ==2:
        a=random.randint(1,6)

        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 3 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 3 là ${{{phan_so(1/18)}}}$."

        kq=f"${{{phan_so(1/18)}}}$ "
        kq2=f"${{{phan_so(1/(18+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(16+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(16+random.randint(1,2)))}}}$ "

    if chon ==3:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 4 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 4 là ${{{phan_so(3/36)}}}$."

        kq=f"${{{phan_so(1/12)}}}$ "
        kq2=f"${{{phan_so(1/(12+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(12+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(12+random.randint(1,2)))}}}$ "
    if chon ==4:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 5 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 5 là ${{{phan_so(4/36)}}}$."

        kq=f"${{{phan_so(1/9)}}}$ "
        kq2=f"${{{phan_so(1/(9+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(9+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(9-random.randint(1,3)))}}}$ "
    if chon ==5:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 6 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm trên hai con xúc sắc bằng 6 là ${{{phan_so(5/36)}}}$."

        kq=f"${{{phan_so(5/36)}}}$ "
        kq2=f"${{{phan_so(5/(12+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(1,2)))}}}$ "
    if chon ==6:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 7 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 7 là ${{{phan_so(6/36)}}}$."

        kq=f"${{{phan_so(1/6)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==7:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 8 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 8 là ${{{phan_so(5/36)}}}$."

        kq=f"${{{phan_so(5/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "


    if chon ==8:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 9 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 9 là ${{{phan_so(4/36)}}}$."

        kq=f"${{{phan_so(4/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==9:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 10 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 10 là ${{{phan_so(3/36)}}}$."

        kq=f"${{{phan_so(3/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==10:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 11 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm trên hai con xúc sắc bằng 11 là ${{{phan_so(2/36)}}}$."

        kq=f"${{{phan_so(2/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==11:
        noi_dung=f" Gieo hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm trên hai con xúc sắc bằng 12 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm trên hai con xúc sắc bằng 12 là ${{{phan_so(1/36)}}}$."

        kq=f"${{{phan_so(1/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==12:
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 5 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 5 là ${{{phan_so(11/36)}}}$."

        kq=f"${{{phan_so(11/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==13:
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 10 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 10 là ${{{phan_so(6/36)}}}$."

        kq=f"${{{phan_so(6/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==14:
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 6 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 6 là ${{{phan_so(15/36)}}}$."

        kq=f"${{{phan_so(15/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==15:
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 8 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 8 là ${{{phan_so(3/36)}}}$."

        kq=f"${{{phan_so(3/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==16:
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 4 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 4 là ${{{phan_so(15/36)}}}$."

        kq=f"${{{phan_so(15/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==17:
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 9 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm trên hai con xúc sắc chia hết cho 9 là ${{{phan_so(4/36)}}}$."

        kq=f"${{{phan_so(4/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==18:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là"
        noi_dung_loigiai=f" Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là ${{{phan_so(11/36)}}}$."

        kq=f"${{{phan_so(11/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==19:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là"
        noi_dung_loigiai=f" Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là ${{{phan_so(11/36)}}}$."

        kq=f"${{{phan_so(11/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==20:
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để cả hai con xúc sắc có số chấm xuất hiện giống nhau là"
        noi_dung_loigiai=f"Xác suất để cả hai con xúc sắc có số chấm xuất hiện giống nhau là ${{{phan_so(6/36)}}}$."

        kq=f"${{{phan_so(6/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==21:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để có mặt ${{{a}}}$ xuất hiện đúng một lần là"
        noi_dung_loigiai=f" Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là ${{{phan_so(10/36)}}}$."

        kq=f"${{{phan_so(10/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==22:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm xuất hiện trên hai con xúc sắc là một số lẻ là"
        noi_dung_loigiai=f"Xác suất để tích số chấm xuất hiện trên hai con xúc sắc là một số lẻ là ${{{phan_so(9/36)}}}$."

        kq=f"${{{phan_so(9/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==23:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tích số chấm xuất hiện trên hai con xúc sắc là một số chẵn là"
        noi_dung_loigiai=f"Xác suất để tích số chấm xuất hiện trên hai con xúc sắc là một số lẻ là ${{{phan_so(3/4)}}}$."

        kq=f"${{{phan_so(3/4)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==24:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 7 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 7 là ${{{phan_so(15/36)}}}$."

        kq=f"${{{phan_so(15/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==25:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 6 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 7 là ${{{phan_so(10/36)}}}$."

        kq=f"${{{phan_so(10/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$"
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$"
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==26:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 6 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 6 là ${{{phan_so(10/36)}}}$."

        kq=f"${{{phan_so(10/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$"
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$"
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==27:
        a=random.randint(1,6)
        noi_dung=f" Gieo đồng thời hai con xúc sắc cân đối và đồng chất. Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 5 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện trên hai con xúc sắc nhỏ hơn 5 là ${{{phan_so(7/36)}}}$."

        kq=f"${{{phan_so(7/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$"
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$"
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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



#[D10_C9_B2_16]-M1. xác suất các btoán về rút 1 thẻ số
def mjulk_L10_C9_B2_16(): 
    a=random.randint(20,50)
    b=a-random.randint(5,15)
    chon =random.randint(1,7)

    if chon ==1:
        c=len([i for i in range(1, a + 1) if i % b == 0])
        noi_dung=f"Một hộp chứa ${{{a}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{1}}$ đến ${{{a}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên một thẻ mà không nhìn vào hộp, xác suất để rút được thẻ ghi số chia hết cho ${{{b}}}$ là:  "
        


    if chon ==2:
        c=len([i for i in range(1, a + 1) if i < b])
        noi_dung=f"Một hộp chứa ${{{a}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{1}}$ đến ${{{a}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên một thẻ mà không nhìn vào hộp, xác suất để rút được thẻ ghi số nhỏ hơn ${{{b}}}$ là:  "
        


    if chon == 3:
        c = sum(1 for i in range(2, a+1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1)))
        noi_dung = f"Một hộp chứa ${{{a}}}$ thẻ được đánh số từ ${{1}}$ đến ${{{a}}}$. Rút ngẫu nhiên một thẻ mà không nhìn vào hộp, xác suất rút được thẻ ghi số nguyên tố là:  "
        

    if chon == 4:
        c = sum(1 for i in range(1, int(a**0.5) + 1) if i**2 <= a)
        noi_dung = f"Một hộp chứa ${{{a}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{1}}$ đến ${{{a}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên một thẻ mà không nhìn vào hộp, xác suất rút được thẻ ghi số chính phương là:  "
        


    if chon == 5:
        c = sum(1 for i in range(2, a+1) if any(i % j == 0 for j in range(2, int(i**0.5) + 1)))
        noi_dung = f"Một hộp chứa ${{{a}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{1}}$ đến ${{{a}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên một thẻ mà không nhìn vào hộp, xác suất rút được thẻ là hợp số là:  "
        

    if chon == 6:
        m = a - random.randint(10, 18)
        n = a - random.randint(1, 6)
        c = max(0, n - m - 1)
        noi_dung = f"Một hộp chứa ${{{a}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{1}}$ đến ${{{a}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên một thẻ mà không nhìn vào hộp, xác suất rút được thẻ ghi số lớn hơn ${{{m}}}$ và nhỏ hơn ${{{n}}}$ là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=a-random.randint(1,10)
        c = len([i for i in range(1, a + 1) if i % b != 0])
        noi_dung = f"Một hộp chứa ${{{a}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{1}}$ đến ${{{a}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên một thẻ mà không nhìn vào hộp, xác suất rút được thẻ ghi số không chia hết cho ${{{b}}}$ là:  "
        

    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "


    ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ",f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$ "]
    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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


#[D10_C9_B2_17]-M2. xs các btoán về xếp chỗ ngồi(4 kiểu)
def mjulk_L10_C9_B2_17(): 
    ds=["Lan", "Mai", "Hoa", "Sơn", "Hà", "Hồng", "Tâm", "Hiền", "Lam", "Thảo", "Tân","Tiến"]
    A, B, C =random.sample(ds, 3)

    D=random.choice(["đầu", "cuối", "giữa"])
    chon =random.randint(1,4)
    if chon ==1:
        a=random.randint(6,10)
        b=a-random.randint(3,4)
        c=a+random.randint(1,5)
        noi_dung=f" Xếp ngẫu nhiên chỗ ngồi cho ba bạn {A}, {B}, {C} vào một ghế dài. Xác suất để {A} ngồi {D} là "
        noi_dung_loigiai=f" Xác suất để {A} ngồi {D} là ${{{phan_so(1/3)}}}$"

        kq=f"${{{phan_so(1/3)}}}$ "
        kq2=f"${{{phan_so(1/a)}}}$ "
        kq3=f"${{{phan_so(1/b)}}}$ "
        kq4=f" ${{{phan_so(1/c)}}}$"
    if chon ==2:
        a=random.randint(2,4)
        b=random.randint(8,10)
        c=a+random.randint(1,3)
        noi_dung=f" Xếp ngẫu nhiên chỗ ngồi cho ba bạn {A}, {B}, {C} vào một ghế dài. Xác suất để {A} ngồi đầu và {B} ngồi cuối là "
        noi_dung_loigiai=f" Xác suất để {A} ngồi đầu và {B} ngồi cuối là ${{{phan_so(1/6)}}}$"

        kq=f"${{{phan_so(1/6)}}}$ "
        kq2=f"${{{phan_so(1/a)}}}$ "
        kq3=f"${{{phan_so(1/b)}}}$ "
        kq4=f" ${{{phan_so(1/c)}}}$"
    if chon ==3:
        a=random.randint(2,4)
        b=random.randint(7,10)
        c=random.randint(4, 5)
        noi_dung=f" Xếp ngẫu nhiên chỗ ngồi cho ba bạn {A}, {B}, {C} vào một ghế dài. Xác suất để {A} và {B} ngồi cạnh nhau là "
        noi_dung_loigiai=f" Xác suất để {A} và {B} ngồi cạnh nhau là ${{{phan_so(2/3)}}}$"

        kq=f"${{{phan_so(2/3)}}}$ "
        kq2=f"${{{phan_so(1/a)}}}$ "
        kq3=f"${{{phan_so(2/b)}}}$ "
        kq4=f" ${{{phan_so(2/c)}}}$"
    if chon ==4:
        a=random.randint(6,10)
        b=a-random.randint(3,4)
        c=a+random.randint(1,5)
        noi_dung=f" Xếp ngẫu nhiên chỗ ngồi cho ba bạn {A}, {B}, {C} vào một ghế dài. Xác suất để {A} và {B} không ngồi cạnh nhau là "
        noi_dung_loigiai=f" Xác suất để {A} và {B} không ngồi cạnh nhau là ${{{phan_so(1/3)}}}$"

        kq=f"${{{phan_so(1/3)}}}$ "
        kq2=f"${{{phan_so(1/a)}}}$ "
        kq3=f"${{{phan_so(1/b)}}}$ "
        kq4=f" ${{{phan_so(1/c)}}}$"
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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






#[D10_C9_B2_18]-M2. xác suất các bài toán về chọn người kiểu 1
def mjulk_L10_C9_B2_18(): 

    a=random.randint(2,3)
    b=random.randint(2,3)
    c=math.comb(a+b, 2)

    chon =random.randint(1,8)
    if chon ==1:
        d=a*b
        kq=phan_so(a*b/c)
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam và một bạn nữ là "
        noi_dung_loigiai=f" Xác suất để chọn được một bạn nam và một bạn nữ là ${{{phan_so(a*b/c)}}}$"

        kq=f"${{{phan_so(a*b/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d-2)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"                    ]

    if chon ==2:
    
        d=math.comb(a, 2)
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được hai bạn nữ là "
        noi_dung_loigiai=f" Xác suất để chọn được hai bạn nữ là ${{{phan_so(d/c)}}}$"
        kq=f"${{{phan_so(d/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d+4)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"                    ]

    if chon ==3:
        d=math.comb(b, 2)
 
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được hai bạn nam là "
        noi_dung_loigiai=f" Xác suất để chọn được hai bạn nam là ${{{phan_so(d/c)}}}$"

        kq=f"${{{phan_so(d/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d+4)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"           
         ]

    if chon ==4:
        d=a+b-1
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để bạn {A} được chọn là "
        noi_dung_loigiai=f" Xác suất để {A} được chọn là ${{{phan_so(d/c)}}}$"

        kq=f"${{{phan_so(d/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d-2)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"  ]         

    if chon ==5:
        d=b
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được một nam một nữ trong đó có bạn {A} là "
        noi_dung_loigiai=f" Xác suất để chọn được một nam một nữ trong đó có {A} được chọn là ${{{phan_so(d/c)}}}$"

        kq=f"${{{phan_so(d/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d+4)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"  ]  
    if chon ==6:
        d=1
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hưng", "Hoàng", "Công", "Thịnh", "Long", "Linh", "Trường"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam trong đó có một bạn tên {B}. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được {A} và {B} là "
        noi_dung_loigiai=f" Xác suất để chọn được {A} và {B} là ${{{phan_so(d/c)}}}$"
        kq=f"${{{phan_so(d/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d+4)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"  ]         

    if chon ==7:
        d=math.comb(a+b-1, 2)
        A=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hưng", "Hoàng", "Công", "Thịnh", "Long", "Linh", "Trường", "Hà", "Lan", "Mai"," Huệ"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam trong đó có một bạn tên {A} . Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để bạn {A} không được chọn là "
        noi_dung_loigiai=f" Xác suất để bạn {A} không được chọn là ${{{phan_so(d/c)}}}$"
        kq=f"${{{phan_so(d/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d-2)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"  ]         
    

    if chon ==8:
        d=a+b-2
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hưng", "Hoàng", "Công", "Thịnh", "Long", "Linh", "Trường"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam trong đó có một bạn tên {B}. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được {A} mà không chọn {B} là "
        noi_dung_loigiai=f" Xác suất để chọn được {A} mà không chọn {B} là ${{{phan_so(d/c)}}}$"
        kq=f"${{{phan_so(d/c)}}}$ "
        ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d+4)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"  ]         



    kq2, kq3, kq4 = random.sample(ds, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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


#[D10_C9_B2_19]-M2. Tính xác suất các bài toán về chọn người 
def mjulk_L10_C9_B2_19(): 

    a=random.randint(3,6)
    b=random.randint(3,6)
    c=math.comb(a+b, 2)

    chon =random.randint(1,7)
    if chon ==1:
        d=a*b
        kq=phan_so(a*b/c)
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam và một bạn nữ là "
        noi_dung_loigiai=f" Xác suất để chọn được một bạn nam và một bạn nữ là ${{{phan_so(a*b/c)}}}$"


    if chon ==2:
    
        d=math.comb(a, 2)
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được hai bạn nữ là "
        noi_dung_loigiai=f" Xác suất để chọn được hai bạn nữ là ${{{phan_so(d/c)}}}$"
        

    if chon ==3:
        d=math.comb(b, 2)
 
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được hai bạn nam là "
        noi_dung_loigiai=f" Xác suất để chọn được hai bạn nam là ${{{phan_so(d/c)}}}$"

        

    if chon ==4:
        d=a+b-1
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để bạn {A} được chọn là "
        noi_dung_loigiai=f" Xác suất để {A} được chọn là ${{{phan_so(d/c)}}}$"

 

    if chon ==5:
        d=b
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được một nam một nữ trong đó có bạn {A} là "
        noi_dung_loigiai=f" Xác suất để chọn được một nam một nữ trong đó có {A} được chọn là ${{{phan_so(d/c)}}}$"

    if chon ==6:
        d=a+b-2
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hưng", "Hoàng", "Công", "Thịnh", "Long", "Linh", "Trường"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam trong đó có một bạn tên {B}. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được {A} mà không chọn {B} là "
        noi_dung_loigiai=f" Xác suất để chọn được {A} mà không chọn {B} là ${{{phan_so(d/c)}}}$"


    if chon ==7:
        d=math.comb(a+b-1, 2)
        A=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hưng", "Hoàng", "Công", "Thịnh", "Long", "Linh", "Trường", "Hà", "Lan", "Mai"," Huệ"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ và ${{{b}}}$ bạn nam trong đó có một bạn tên {A} . Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để bạn {A} không được chọn là "
        noi_dung_loigiai=f" Xác suất để bạn {A} không được chọn là ${{{phan_so(d/c)}}}$"

    if chon ==8:
        d=a+b-2
        A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
        B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hưng", "Hoàng", "Công", "Thịnh", "Long", "Linh", "Trường"])
        noi_dung=f"Một nhóm gồm ${{{a}}}$ bạn nữ trong đó có một bạn tên {A} và ${{{b}}}$ bạn nam trong đó có một bạn tên {B}. Giáo viên chọn ngẫu nhiên hai bạn tham gia văn nghệ. Xác suất để chọn được {A} mà không chọn {B} là "
        noi_dung_loigiai=f" Xác suất để {A} và {B} không được chọn là ${{{phan_so(d/c)}}}$"


    kq=f"${{{phan_so(d/c)}}}$ "
    ds=[f"${{{phan_so((d+1)/c)}}}$ ",   f"${{{phan_so((d+2)/c)}}}$ ",f" ${{{phan_so((d-2)/c)}}}$",f" ${{{phan_so((d-1)/c)}}}$",f" ${{{phan_so((d+3)/c)}}}$"                    ]
    kq2, kq3, kq4 = random.sample(ds, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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





#[D10_C9_B2_20]-M2. xs các btoán về Rút quả cầu từ một hộp các quả vừa khác màu vừa khác số(18 kiểu)
def mjulk_L10_C9_B2_20(): 
    ds=[" đen", "đỏ", "xanh", "tím", "vàng", "trắng"]
    A,B=random.sample(ds,2)
    a=random.randint(10,25)
    m =random.randint(6, 15)
    n=m+random.randint(10,25)
    b=n-m+1
    u=a+b
    e=random.choice([3,4,5,6,7,8,10])
    chon=random.randint(1,17)
    if chon ==1:
        d=a
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {A} là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {A} là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {A} là ${{{x}}}$. ")

    if chon ==2:
        d=b
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {B} là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {B} là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {B} là ${{{x}}}$. ")

    if chon ==3:
        d=len([i for i in range(m, n + 1) if i %2 != 0])
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {B} ghi số lẻ là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {B} ghi số lẻ là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {B} ghi số lẻ là ${{{x}}}$. ")


    if chon ==4:
        d=len([i for i in range(1, a + 1) if i %2 != 0])
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {A} ghi số lẻ là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {A} ghi số lẻ là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {A} ghi số lẻ là ${{{x}}}$. ")


    if chon ==5:
        d=len([i for i in range(m, n + 1) if i %2 == 0])
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {B} ghi số chẵn là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {B} ghi số chẵn là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {B} ghi số chẵn là ${{{x}}}$. ")


    if chon ==6:
        d=len([i for i in range(1, a + 1) if i %2 == 0])
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {A} ghi số chẵn là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {A} ghi số chẵn là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {A} ghi số chẵn là ${{{x}}}$. ")



    if chon ==7:
        d1=len([i for i in range(1, a + 1) if i %2 != 0])
        d2=len([i for i in range(m, n + 1) if i %2 != 0])
        d=d1+d2
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu ghi số lẻ là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả cầu ghi số lẻ là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả cầu ghi số lẻ là ${{{x}}}$. ")


    if chon ==8:
        d1=len([i for i in range(m, n + 1) if i %2 == 0])
        d2=len([i for i in range(1, a + 1) if i %2 == 0])
        d=d1+d2
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu ghi số chẵn là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả cầu ghi số chẵn là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả cầu ghi số chẵn là ${{{x}}}$. ")



    if chon ==9:
        d=sum(1 for i in range(int(m**0.5), int(n**0.5) + 1) if m<=i**2 <= n)
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {B} ghi số chính phương là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {B} ghi số chính phương là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {B} ghi số chính phương là ${{{x}}}$. ")


    if chon ==10:
        d=sum(1 for i in range(1, int(a**0.5) + 1) if i**2 <= a)
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {A} ghi số chính phương là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {A} ghi số chính phương là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {A} ghi số chính phương là ${{{x}}}$. ")


    if chon ==11:
        d1=sum(1 for i in range(1, int(a**0.5) + 1) if i**2 <= a)
        d2=sum(1 for i in range(int(m**0.5), int(n**0.5) + 1) if m<=i**2 <= n)
        d=d1+d2
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu ghi số chính phương là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả cầu ghi số chính phương là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả cầu ghi số chính phương là ${{{x}}}$. ")



    if chon ==12:
        d=sum(1 for i in range(m, n+1) if all(i % d != 0 for d in range(2, int(i**0.5) + 1)) and i > 1)
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {B} ghi số nguyên tố là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {B} ghi số nguyên tố là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {B} ghi số nguyên tố là ${{{x}}}$. ")


    if chon ==13:
        d=sum(1 for i in range(2, a+1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1)))
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {A} ghi số nguyên tố là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {A} ghi số nguyên tố là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {A} ghi số nguyên tố là ${{{x}}}$. ")


    if chon ==14:
        d1=sum(1 for i in range(2, a+1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1)))
        d2=sum(1 for i in range(m, n+1) if all(i % d != 0 for d in range(2, int(i**0.5) + 1)) and i > 1)
        d=d1+d2
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu ghi số nguyên tố là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả ghi số nguyên tố là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả ghi số nguyên tố là ${{{x}}}$. ")


    if chon ==15:
        d=len([i for i in range(m, n + 1) if i % e == 0])
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {B} ghi số chia hết cho ${{{e}}}$ là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {B} ghi số chia hết cho ${{{e}}}$ là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {B} ghi số chia hết cho ${{{e}}}$ là ${{{x}}}$. ")


    if chon ==16:
        d=len([i for i in range(1, a + 1) if i % e == 0])
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu màu {A} ghi số chia hết cho ${{{e}}}$ là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả màu {A} ghi số chia hết cho ${{{e}}}$ là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả màu {A} ghi số chia hết cho ${{{e}}}$ là ${{{x}}}$. ")


    if chon ==17:
        d1=len([i for i in range(1, a + 1) if i % e == 0])
        d2=len([i for i in range(m, n + 1) if i % e == 0])
        d=d1+d2
        x=phan_so(d/u)
        noi_dung=f"Một hộp chứa ${{{a}}}$ quả cầu màu {A} được đánh số từ ${{1}}$ đến ${{{a}}}$ và ${{{b}}}$ quả cầu màu {B} được đánh số ${{{m}}}$ đến ${{{n}}}$. Lấy ngẫu nhiên một quả cầu trong hộp, xác suất để lấy được quả cầu ghi số chia hết cho ${{{e}}}$ là: "
        noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{u}}}$. \n\n"
                        f" Số các kết quả thuận lợi của biến cố lấy được quả ghi số chia hết cho ${{{e}}}$ là ${{{d}}}$\n\n"
                        f" Xác suất để lấy được quả ghi số chia hết cho ${{{e}}}$ là ${{{x}}}$. ")





    kq=f"${{{x}}}$ "
    ds1=[f"${{{phan_so(d/(u-1))}}}$ ",   f"${{{phan_so(d/(u-2))}}}$ ",f" ${{{phan_so(d/(u+4))}}}$",f" ${{{phan_so(d/(u+1))}}}$",f" ${{{phan_so(d/(u+2))}}}$" ,f" ${{{phan_so(d/(u+3))}}} $",f" ${{{phan_so(d/(u-3))}}}$ "]
    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_21]-M1. XS các bài toán quay số trúng thưởng
def mjulk_L10_C9_B2_21(): 
    a=random.randint(10,20)
    b=random.randint(1,a)
    chon =random.randint(1,9)
    C=random.choice([" con chuột máy tính"," chai dầu gội", " tuýt kem đánh răng", "hộp bánh", "túi nước giặt", "thú bông"])
    A=random.choice(["tivi", "tủ lạnh", "bàn là", "nồi cơm điện", "máy hút bụi", "mũ bảo hiểm", "điện thoại thông minh", "đèn học", "bộ nồi gia dụng", "ấm siêu tốc","máy sấy tóc"])
    B=random.choice(["siêu thị", "cửa hàng tiện lợi", "hội chợ", "cửa hàng bách hoá", " trung tâm thương mại", "công ty"," cửa hàng"])
    if chon ==1:
        c=1
        noi_dung=f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số ${{{b}}}$ thì người chơi nhận được một {A}. Xác suất để người chơi nhận được {A} là:"
        


    if chon ==2:
        c=len([i for i in range(1, a + 1) if i < b])
        noi_dung=f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số nhỏ hơn ${{{b}}}$ thì người chơi nhận được một {A}. Xác suất để người chơi nhận được {A} là:"

        


    if chon == 3:
        c = sum(1 for i in range(2, a+1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1)))
        noi_dung=f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số nguyên tố thì người chơi nhận được một {A}. Xác suất để người chơi nhận được {A} là:"
        

    if chon == 4:
        c = sum(1 for i in range(1, int(a**0.5) + 1) if i**2 <= a)
        noi_dung=f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số chính phương thì người chơi nhận được một {A}. Xác suất để người chơi nhận được {A} là:"
        


    if chon == 5:
        c = sum(1 for i in range(2, a+1) if any(i % j == 0 for j in range(2, int(i**0.5) + 1)))
        noi_dung=f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi hợp số thì người chơi nhận được một {A}. Xác suất để người chơi nhận được {A} là:"
        

    if chon == 6:
        n = random.randint(2, 5)
        m = random.choice([i for i in range(n+3,a-1) ])
        
        c = max(0, m - n - 1)
        noi_dung = f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số lớn hơn ${{{n}}}$ và nhỏ hơn ${{{m}}}$ thì người chơi nhận được một {A}. Xác suất để người chơi nhận được {A} là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=a-random.randint(1,10)
        c = len([i for i in range(1, a + 1) if i % b != 0])
        noi_dung = f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số chia hết cho ${{{b}}}$ thì người chơi nhận được một {A}. Xác suất để người chơi nhận được {A} là:  "
        
    if chon == 8:
        
        c = len([i for i in range(1, a + 1) if i % 2 != 0])
        noi_dung = f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số lẻ thì người chơi nhận được {C}. Xác suất để người chơi nhận được {C} là:  "
    
    if chon == 9:
        
        c = len([i for i in range(1, a + 1) if i % 2 == 0])
        noi_dung = f"Một {B} tổ chức quay số trúng thưởng nhân dịp khai trương, họ chuẩn bị một vòng tròn cố định tâm và có gắn kim quay tại tâm, vòng tròn được chia thành ${{{a}}}$ phần bằng nhau và đánh số liên tiếp từ ${{1}}$ đến ${{{a}}}$. Mỗi người chơi chỉ được quay một lần duy nhất, nếu quay vào ô ghi số chẵn thì người chơi nhận được {C}. Xác suất để người chơi nhận được {C} là:  "

    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "


    ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
    ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
    f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]
    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_22]-M2. XS các bài toán rút số từ 2 hộp và ghép lại với nhau
def mjulk_L10_C9_B2_22(): 
    a=9
    b=random.randint(2,9)
    d=random.choice([i for i in range(2,9) if i!=b])
    m=random.choice([i for i in range(1,9) if i!=b and i!=d])    

    e=random.randint(0,9)
    f=random.choice([i for i in range(0,9) if i!=e])
    h=random.choice([i for i in range(0,9) if i!=e and i!=f])    
    b1=10*b+e 
    b2=10*b+f 
    b3=10*b+h 
    b4=10*d+e 
    b5=10*d+f 
    b6=10*d+h 
    b7=10*m+e 
    b8=10*m+f 
    b9=10*m+h 

    ds=[b1,b2,b3,b5,b4,b6,b7,b8,b9]

    chon =random.randint(1,7)
    if chon ==1:
        c1=sum(1 for x in (e, f, h) if x % 2 == 0)
        c=3*c1
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Từ mỗi túi I và II rút ngẫu nhiên một tấm thẻ và ghép thành số có hai chữ số với chữ số trên tấm thẻ rút từ túi I là chữ số hàng chục. Xác xuất để số tạo thành là số chẵn là: "

    if chon ==2:
        c1=sum(1 for x in (e, f, h) if x % 2 != 0)
        c=3*c1
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Từ mỗi túi I và II rút ngẫu nhiên một tấm thẻ và ghép thành số có hai chữ số với chữ số trên tấm thẻ rút từ túi I là chữ số hàng chục. Xác xuất để số tạo thành là số lẻ là: "

    if chon ==3:
        c=sum(all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Từ mỗi túi I và II rút ngẫu nhiên một tấm thẻ và ghép thành số có hai chữ số với chữ số trên tấm thẻ rút từ túi I là chữ số hàng chục. Xác xuất để số tạo thành là số nguyên tố là: "
    
    if chon ==4:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u == 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Từ mỗi túi I và II rút ngẫu nhiên một tấm thẻ và ghép thành số có hai chữ số với chữ số trên tấm thẻ rút từ túi I là chữ số hàng chục. Xác xuất để số tạo thành là số chia hết cho ${{{u}}}$ là: "

    if chon ==5:
        i=random.randint(10,20)
        j=i+random.randint(20,50)
        c=sum(i < x < j for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Từ mỗi túi I và II rút ngẫu nhiên một tấm thẻ và ghép thành số có hai chữ số với chữ số trên tấm thẻ rút từ túi I là chữ số hàng chục. Xác xuất để số tạo thành là số lớn hơn ${{{i}}}$ và nhỏ hơn ${{{j}}}$ là: "

    if chon ==6:

        c=sum(int(x**0.5)**2 == x for x in ds if x >= 0)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Từ mỗi túi I và II rút ngẫu nhiên một tấm thẻ và ghép thành số có hai chữ số với chữ số trên tấm thẻ rút từ túi I là chữ số hàng chục. Xác xuất để số tạo thành là số chính phương là: "

    if chon ==7:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u != 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Từ mỗi túi I và II rút ngẫu nhiên một tấm thẻ và ghép thành số có hai chữ số với chữ số trên tấm thẻ rút từ túi I là chữ số hàng chục. Xác xuất để số tạo thành là số không chia hết cho ${{{u}}}$ là: "

    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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

#[D10_C9_B2_23]-M2. XS các bài toán rút số từ 2 hộp và nhân lại với nhau
def mjulk_L10_C9_B2_23(): 
    a=9
    b=random.randint(1,9)
    d=random.choice([i for i in range(1,9) if i!=b])
    m=random.choice([i for i in range(1,9) if i!=b and i!=d])    

    e=random.randint(1,9)
    f=random.choice([i for i in range(1,9) if i!=e])
    h=random.choice([i for i in range(1,9) if i!=e and i!=f])    
    b1=b*e 
    b2=b*f 
    b3=b*h 
    b4=d*e 
    b5=d*f 
    b6=d*h 
    b7=m*e 
    b8=m*f 
    b9=m*h 
    ds=[b1,b2,b3,b5,b4,b6,b7,b8,b9]

    chon =random.randint(1,7)
    if chon ==1:
        c=sum(x % 2 == 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và nhân hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số chẵn là: "

    if chon ==2:
        c=sum(x % 2 != 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và nhân hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số lẻ là: "

    if chon ==3:
        c=sum(all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và nhân hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số nguyên tố là: "
    
    if chon ==4:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u == 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và nhân hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số chia hết cho ${{{u}}}$ là: "

    if chon ==5:
        i=random.randint(2,20)
        j=i+random.randint(20,50)
        c=sum(i < x < j for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và nhân hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số lớn hơn ${{{i}}}$ và nhỏ hơn ${{{j}}}$ là: "

    if chon ==6:

        c=sum(int(x**0.5)**2 == x for x in ds if x >= 0)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và nhân hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số chính phương là: "

    if chon ==7:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u != 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và nhân hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số không chia hết cho ${{{u}}}$ là: "


    


    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_24]-M2. XS các bài toán rút số từ 2 hộp và cộng lại với nhau
def mjulk_L10_C9_B2_24(): 
    a=9
    b=random.randint(2,9)
    d=random.choice([i for i in range(2,9) if i!=b])
    m=random.choice([i for i in range(2,9) if i!=b and i!=d])    

    e=random.randint(1,9)
    f=random.choice([i for i in range(1,9) if i!=e])
    h=random.choice([i for i in range(1,9) if i!=e and i!=f])    
    b1=b+e 
    b2=b+f 
    b3=b+h 
    b4=d+e 
    b5=d+f 
    b6=d+h 
    b7=m+e 
    b8=m+f 
    b9=m+h 
    ds=[b1,b2,b3,b5,b4,b6,b7,b8,b9]

    chon =random.randint(1,8)
    if chon ==1:
        c=sum(x % 2 == 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số chẵn là: "

    if chon ==2:
        c=sum(x % 2 != 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số lẻ là: "

    if chon ==3:
        c=sum(all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số nguyên tố là: "
    
    if chon ==4:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u == 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số chia hết cho ${{{u}}}$ là: "

    if chon ==5:
        i=min(ds)+1
        j=max(ds)-random.randint(1,3)
        c=sum(i < x < j for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số lớn hơn ${{{i}}}$ và nhỏ hơn ${{{j}}}$ là: "

    if chon ==6:

        c=sum(int(x**0.5)**2 == x for x in ds if x >= 0)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số chính phương là: "

    if chon ==7:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u != 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là số không chia hết cho ${{{u}}}$ là: "

    if chon == 8:
        e=random.choice([i for i in ds])
        u=e*random.randint(2,4)
        c=sum(u % x == 0 for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả là ước của ${{{u}}}$ là: "
    
    if chon == 9:
        e=random.choice([i for i in ds])
        u=e*random.randint(2,5) 
        v=e-1 
        c=sum(u % x == 0 and x>v for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả vừa là ước của ${{{u}}}$ và lớn hơn ${{{v}}}$ là: "

    if chon == 10:
        e=random.choice([i for i in ds if i!=1])
        u=e*random.randint(3,5) 
        v=e+random.randint(1,10)
        c=sum(u % x == 0 and x<v for x in ds)
        noi_dung=f"Cho hai túi I và II. Túi I chứa 3 tấm thẻ đánh số ${{{d}; {b}; {m}}}$. Túi II chứa 3 tấm thẻ, đánh số ${{{e}; {f}; {h}}}$. Rút ngẫu nhiên từ mỗi túi ra một tấm thẻ và cộng hai số ghi trên hai tấm thẻ với nhau. Xác xuất để kết quả vừa là ước của ${{{u}}}$ và nhỏ hơn ${{{v}}}$ là: "



    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_25]-M2. XS các bài toán quay số từ 2 vòng quay và nhân(cộng, ghép) lại với nhau(8 kiểu)
def mjulk_L10_C9_B2_25(): 
    ten=["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"]
    ten1, ten2=random.sample(ten,2)
    a=12
    b=random.randint(1,9)
    d=random.choice([i for i in range(1,9) if i!=b])
    m=random.choice([i for i in range(1,9) if i!=b and i!=d])    

    e=random.randint(1,9)
    f=random.choice([i for i in range(1,9) if i!=e])
    h=random.choice([i for i in range(1,9) if i!=e and i!=f])    
    g=random.choice([i for i in range(1,9) if i!=e and i!=f and i!=h])    
    b1=b*e 
    b2=b*f 
    b3=b*h 
    b4=d*e 
    b5=d*f 
    b6=d*h 
    b7=m*e 
    b8=m*f 
    b9=m*h 
    b10=b*g 
    b11=d*g 
    b12=m*g
    ds=[b1,b2,b3,b5,b4,b6,b7,b8,b9, b11, b12, b10]
    code_hinh=fr"""
\begin{{tikzpicture}}
    % Vẽ hình tròn thứ nhất (nhỏ lại)
    \draw[thick] (0,0) circle(2cm);
    
    % Vẽ các đường chia hình tròn thứ nhất thành 3 phần bằng nhau
    \foreach \angle in {{0,120,240}} {{
        \draw[thick] (0,0) -- (\angle:2cm);
    }}
    
    % Đánh số các phần của hình tròn thứ nhất
    \node at (60:1cm) {{${d}$}};
    \node at (180:1cm) {{${b}$}};
    \node at (-60:1cm){{${m}$}};
    
    % Vẽ hình tròn thứ hai (nhỏ lại, có khoảng cách)
    \draw[thick] (5,0) circle(2cm);
    
    % Vẽ các đường chia hình tròn thứ hai thành 4 phần bằng nhau
    \foreach \angle in {{0,90,180,270}} {{
        \draw[thick] (5,0) -- ++(\angle:2cm);
    }}
    
    % Đánh số các phần của hình tròn thứ hai
    \node at (6,1) {{${e}$}};
    \node at (6,-1) {{${f}$}};
    \node at (4,-1) {{${g}$}};
    \node at (4,1) {{${h}$}};
\end{{tikzpicture}}
    """
    chon =random.randint(1,7)
    if chon ==1:
        c=sum(x % 2 == 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là số chẵn là: "

    if chon ==2:
        c=sum(x % 2 != 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là số lẻ là: "

    if chon ==3:
        c=sum(all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là số nguyên tố là: "
    
    if chon ==4:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u == 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là số chia hết cho ${{{u}}}$ là: "

    if chon ==5:
        i=random.randint(2,20)
        j=i+random.randint(20,50)
        c=sum(i < x < j for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là số lớn hơn ${{{i}}}$ và nhỏ hơn ${{{j}}}$ là: "

    if chon ==6:

        c=sum(int(x**0.5)**2 == x for x in ds if x >= 0)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là số chính phương là: "

    if chon ==7:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u != 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là số không chia hết cho ${{{u}}}$ là: "

    # if chon ==8:
    #     u=random.randint(20,100)
    #     c=sum(u % x == 0 for x in ds)
    #     noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tích hai số ở hình quạt mà hai mũi tên chỉ vào là ước của ${{{u}}}$ là: "
    


    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai=(f"{noi_dung}\n"
        f"{file_name}\n")
    phuongan = f"A. {list_PA[0]}.\t   B. {list_PA[1]}.\t    C. {list_PA[2]}.\t     D. {list_PA[3]}.\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề latex
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
                   f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
                   f"\\end{{ex}}\n"
    
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C9_B2_26]-M3. XS các btoán quay số từ 2 vòng quay và cộng lại với nhau(10 kiểu)
def mjulk_L10_C9_B2_26(): 
    ten=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    ten1, ten2=random.sample(ten,2)
    a=12
    b=random.randint(1,9)
    d=random.choice([i for i in range(1,9) if i!=b])
    m=random.choice([i for i in range(1,9) if i!=b and i!=d])    

    e=random.randint(1,9)
    f=random.choice([i for i in range(1,9) if i!=e])
    h=random.choice([i for i in range(1,9) if i!=e and i!=f])    
    g=random.choice([i for i in range(1,9) if i!=e and i!=f and i!=h])    
    b1=b+e 
    b2=b+f 
    b3=b+h 
    b4=d+e 
    b5=d+f 
    b6=d+h 
    b7=m+e 
    b8=m+f 
    b9=m+h 
    b10=b+g 
    b11=d+g 
    b12=m+g
    ds=[b1,b2,b3,b5,b4,b6,b7,b8,b9, b11, b12, b10]
    code_hinh=fr"""
\begin{{tikzpicture}}
    % Vẽ hình tròn thứ nhất (nhỏ lại)
    \draw[thick] (0,0) circle(2cm);
    
    % Vẽ các đường chia hình tròn thứ nhất thành 3 phần bằng nhau
    \foreach \angle in {{0,120,240}} {{
        \draw[thick] (0,0) -- (\angle:2cm);
    }}
    
    % Đánh số các phần của hình tròn thứ nhất
    \node at (60:1cm) {{${d}$}};
    \node at (180:1cm) {{${b}$}};
    \node at (-60:1cm){{${m}$}};
    
    % Vẽ hình tròn thứ hai (nhỏ lại, có khoảng cách)
    \draw[thick] (5,0) circle(2cm);
    
    % Vẽ các đường chia hình tròn thứ hai thành 4 phần bằng nhau
    \foreach \angle in {{0,90,180,270}} {{
        \draw[thick] (5,0) -- ++(\angle:2cm);
    }}
    
    % Đánh số các phần của hình tròn thứ hai
    \node at (6,1) {{${e}$}};
    \node at (6,-1) {{${f}$}};
    \node at (4,-1) {{${g}$}};
    \node at (4,1) {{${h}$}};
\end{{tikzpicture}}
    """
    chon =random.randint(1,8)
    if chon ==1:
        c=sum(x % 2 == 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số chẵn là: "

    if chon ==2:
        c=sum(x % 2 != 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số lẻ là: "

    if chon ==3:
        c=sum(all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số nguyên tố là: "
    
    if chon ==4:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u == 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số chia hết cho ${{{u}}}$ là: "

    if chon ==5:
        i=min(ds) +2
        j=max(ds)-1
        c=sum(i < x < j for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số lớn hơn ${{{i}}}$ và nhỏ hơn ${{{j}}}$ là: "

    if chon ==6:

        c=sum(int(x**0.5)**2 == x for x in ds if x >= 0)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số chính phương là: "

    if chon ==7:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u != 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số không chia hết cho ${{{u}}}$ là: "

    if chon ==8:
        u=random.randint(20,100)
        c=sum(u % x == 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là ước của ${{{u}}}$ là: "
    
    if chon == 9:
        u=random.randint(20,100)
        v=random.randint(2,15)
        c=sum(u % x == 0 and x>v for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là ước của ${{{u}}}$ và lớn hơn ${{{v}}}$ là: "

    if chon == 10:
        u=random.randint(20,100)
        v=u-random.randint(25,)
        c=sum(u % x == 0 and x<v for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {ten1} quay tấm bìa ${{A}}$, bạn {ten2} quay tấm bìa ${{B}}$. Xác xuất để tổng hai số ở hình quạt mà hai mũi tên chỉ vào là ước của ${{{u}}}$ và nhỏ hơn ${{{v}}}$là: "



    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai=(f"{noi_dung}\n"
        f"{file_name}\n")
    phuongan = f"A. {list_PA[0]}.\t   B. {list_PA[1]}.\t    C. {list_PA[2]}.\t     D. {list_PA[3]}.\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề latex
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
                   f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
                   f"\\end{{ex}}\n"
    
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an




#[D10_C9_B2_27]-M2. XS các bài toán quay số từ 2 vòng quay và ghép lại với nhau(7 kiểu)
def mjulk_L10_C9_B2_27(): 
    X=random.choice(["An ", "Minh", "Phú", "Hà", "Lan", "Mai", "Hồng", "Huệ", "Bình"])
    Y=random.choice(["Công ", "Nga", "Quân", "Khôi", "Hải", "Hiền", "Kiên", "Duy","Bảo"])
    a=12
    b=random.randint(1,9)
    d=random.choice([i for i in range(1,9) if i!=b])
    m=random.choice([i for i in range(1,9) if i!=b and i!=d])    

    e=random.randint(1,9)
    f=random.choice([i for i in range(1,9) if i!=e])
    h=random.choice([i for i in range(1,9) if i!=e and i!=f])    
    g=random.choice([i for i in range(1,9) if i!=e and i!=f and i!=h])    
    b1=10*b+e 
    b2=10*b+f 
    b3=10*b+h 
    b4=10*d+e 
    b5=10*d+f 
    b6=10*d+h 
    b7=10*m+e 
    b8=10*m+f 
    b9=10*m+h 
    b10=10*b+g 
    b11=10*d+g 
    b12=10*m+g
    ds=[b1,b2,b3,b5,b4,b6,b7,b8,b9, b11, b12, b10]
    code_hinh=fr"""
\begin{{tikzpicture}}
    % Vẽ hình tròn thứ nhất (nhỏ lại)
    \draw[thick] (0,0) circle(2cm);
    
    % Vẽ các đường chia hình tròn thứ nhất thành 3 phần bằng nhau
    \foreach \angle in {{0,120,240}} {{
        \draw[thick] (0,0) -- (\angle:2cm);
    }}
    
    % Đánh số các phần của hình tròn thứ nhất
    \node at (60:1cm) {{${d}$}};
    \node at (180:1cm) {{${b}$}};
    \node at (-60:1cm){{${m}$}};
    
    % Vẽ hình tròn thứ hai (nhỏ lại, có khoảng cách)
    \draw[thick] (5,0) circle(2cm);
    
    % Vẽ các đường chia hình tròn thứ hai thành 4 phần bằng nhau
    \foreach \angle in {{0,90,180,270}} {{
        \draw[thick] (5,0) -- ++(\angle:2cm);
    }}
    
    % Đánh số các phần của hình tròn thứ hai
    \node at (6,1) {{${e}$}};
    \node at (6,-1) {{${f}$}};
    \node at (4,-1) {{${g}$}};
    \node at (4,1) {{${h}$}};
\end{{tikzpicture}}
    """
    chon =random.randint(1,7)
    if chon ==1:
        c=sum(x % 2 == 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là số chẵn là: "

    if chon ==2:
        c=sum(x % 2 != 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là số lẻ là: "

    if chon ==3:
        c=sum(all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là số nguyên tố là: "
    
    if chon ==4:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u == 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là số chia hết cho ${{{u}}}$ là: "

    if chon ==5:
        i=random.randint(2,20)
        j=i+random.randint(20,50)
        c=sum(i < x < j for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là số lớn hơn ${{{i}}}$ và nhỏ hơn ${{{j}}}$ là: "

    if chon ==6:

        c=sum(int(x**0.5)**2 == x for x in ds if x >= 0)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là số chính phương là: "

    if chon ==7:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u != 0 for x in ds)
        noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là số không chia hết cho ${{{u}}}$ là: "

    # if chon ==8:
    #     u=random.randint(20,100)
    #     c=sum(u % x == 0 for x in ds)
    #     noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là ước của ${{{u}}}$ là: "
    
    # if chon == 9:
    #     u=random.randint(20,100)
    #     v=random.randint(2,15)
    #     c=sum(u % x == 0 and x>v for x in ds)
    #     noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là ước của ${{{u}}}$ và lớn hơn ${{{v}}}$ là: "

    # if chon == 10:
    #     u=random.randint(20,100)
    #     v=u-random.randint(25,)
    #     c=sum(u % x == 0 and x<v for x in ds)
    #     noi_dung=f"Tấm bìa cứng ${{A}}$ hình tròn được chia thành ba hình quạt có diện tích bằng nhau, đánh số ${{{d}; {b}; {m}}}$ và tấm bìa cứng ${{B}}$ hình tròn được chia thành ${{4}}$ hình quạt có diện tích bằng nhau đánh số ${{{e}; {f}; {g}; {h}}}$. Trục quay của ${{A}}$ và ${{B}}$ được gắn mũi tên ở tâm. Bạn {X} quay tấm bìa ${{A}}$, bạn {Y} quay tấm bìa ${{B}}$ và ghép hai số quay được của 2 bạn thành số có hai chữ số với chữ số bạn {X} quay được là chữ số hàng chục. Xác suất để kết quả là ước của ${{{u}}}$ và nhỏ hơn ${{{v}}}$là: "

    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai=(f"{noi_dung}\n"
        f"{file_name}\n")
    phuongan = f"A. {list_PA[0]}.\t   B. {list_PA[1]}.\t    C. {list_PA[2]}.\t     D. {list_PA[3]}.\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề latex
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
                   f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
                   f"\\end{{ex}}\n"
    
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an





#[D10_C9_B2_28]-M2. Tính xác suất các bài toán về chọn 1 người từ 2 nhóm
def mjulk_L10_C9_B2_28(): 

    e=random.randint(1,12)
    
    ds2=["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"]
    ds3=["Hoà", "Minh", "Hiếu", "Hùng", "Hưng", "Hoàng", "Công", "Thịnh", "Long", "Linh", "Trường"]
    A,B,C,D =random.sample(ds2, 4)
    M,N,P,Q,Z=random.sample(ds3,5)
    w=random.randint(1,2)
    if w==1:
        a=7
        chon =random.randint(1,11)
        if chon ==1:
            c=3
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam là "

        if chon ==2:        
            c=4
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nữ là "               

        if chon ==3:
            c=2     
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn lớp ${{{e}}}$A là "


        if chon ==4:
            c=2
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn một bạn lớp ${{{e}}}$B là "

        if chon ==5:
            c=3
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn một bạn lớp ${{{e}}}$C là "

        if chon ==6:
            c=1

            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam lớp ${{{e}}}$A là "
        if chon ==7:
            c=2
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nữ lớp ${{{e}}}$C là "
   
        if chon ==8:
            c=4
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn bạn lớp ${{{e}}}$C là "
           
        if chon ==9:
            c=5
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn được bạn nữ lớp ${{{e}}}$C là "    
        if chon ==10:
            c=6
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn được bạn {A} là "
        if chon ==11:
            c=1
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{3}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất chọn được bạn {A} là "
    if w==2:
        a=8

        chon =random.randint(1,11)
        if chon ==1:
            c=4
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam là "

        if chon ==2:        
            c=4
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nữ là "               

        if chon ==3:
            c=2     
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn lớp ${{{e}}}$A là "


        if chon ==4:
            c=3
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn lớp ${{{e}}}$B là "

        if chon ==5:
            c=3
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn lớp ${{{e}}}$C là "

        if chon ==6:
            c=1

            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam lớp ${{{e}}}$A là "
        if chon ==7:
            c=2
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nữ lớp ${{{e}}}$C là "
   
        if chon ==8:
            c=5
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn bạn lớp ${{{e}}}$C là "
           
        if chon ==9:
            c=6
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn được bạn nữ lớp ${{{e}}}$C là "    
        if chon ==10:
            c=7
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn được bạn {Q} là "    
            chon =random.randint(1,9)
        if chon ==11:
            c=1
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{4}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất chọn được bạn {A} là "
    if w==3:
        a=9
        chon =random.randint(1,12)
        if chon ==1:
            c=5
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam là "

        if chon ==2:        
            c=4
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nữ là "               

        if chon ==3:
            c=2     
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn lớp ${{{e}}}$A là "


        if chon ==4:
            c=4
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn lớp ${{{e}}}$B là "

        if chon ==5:
            c=3
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn lớp ${{{e}}}$C là "

        if chon ==6:
            c=1
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nam lớp ${{{e}}}$A là "
        if chon ==7:
            c=2
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất để chọn được một bạn nữ lớp ${{{e}}}$C là "
   
        if chon ==8:
            c=6
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn bạn lớp ${{{e}}}$C là "
           
        if chon ==9:
            c=7
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn được bạn nữ lớp ${{{e}}}$C là "    
        if chon ==10:
            c=8
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất không chọn được bạn {Q} là "    
        if chon ==11:
            c=3
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn nam tên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất chọn được bạn nam lớp {B} là " 
        if chon ==12:
            c=1
            noi_dung=f"Một nhóm gồm ${{4}}$ bạn nữ tên {A} (lớp ${{{e}}}$A), {B} (lớp ${{{e}}}$B), {C} (lớp ${{{e}}}$C), {D} (lớp ${{{e}}}$C) và ${{5}}$ bạn namtên {M} (lớp ${{{e}}}$A), {N} (lớp ${{{e}}}$B), {P} (lớp ${{{e}}}$C), {Q} (lớp ${{{e}}}$B), {Z} (lớp ${{{e}}}$B). Giáo viên chọn ngẫu nhiên một bạn tham gia văn nghệ. Xác suất chọn được bạn {A} là "
    


    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    kq2, kq3, kq4 = random.sample(ds, 3)  
    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_29]-M3. XS các btoan tích số chấm, tổng số chấm khi gieo 1 con xúc xắc 2 lần 
def mjulk_L10_C9_B2_29(): 
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])

    chon =random.randint(1,27) 
    if chon ==1:
        a=random.randint(1,6)

        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 2 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 2 là ${{{phan_so(1/36)}}}$."

        kq=f"${{{phan_so(1/36)}}}$ "
        kq2=f"${{{phan_so(1/(36-random.randint(10,20)))}}}$  "
        kq3=f"${{{phan_so(2/(36-random.randint(10,20)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(1,20)))}}}$ "
    if chon ==2:
        a=random.randint(1,6)

        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 3 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 3 là ${{{phan_so(1/18)}}}$."

        kq=f"${{{phan_so(1/18)}}}$ "
        kq2=f"${{{phan_so(1/(18+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(16+random.randint(1,2)))}}}$  "
        kq4=f" ${{{phan_so(3/(16+random.randint(1,2)))}}}$ "

    if chon ==3:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 4 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 4 là ${{{phan_so(3/36)}}}$."

        kq=f"${{{phan_so(1/12)}}}$ "
        kq2=f"${{{phan_so(1/(12+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(12+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(12+random.randint(1,2)))}}}$ "
    if chon ==4:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 5 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 5 là ${{{phan_so(4/36)}}}$."

        kq=f"${{{phan_so(1/9)}}}$ "
        kq2=f"${{{phan_so(1/(9+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(9+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(9-random.randint(1,3)))}}}$ "
    if chon ==5:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 6 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm của hai lần gieo bằng 6 là ${{{phan_so(5/36)}}}$."

        kq=f"${{{phan_so(5/36)}}}$ "
        kq2=f"${{{phan_so(5/(12+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(1,2)))}}}$ "
    if chon ==6:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 7 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 7 là ${{{phan_so(6/36)}}}$."

        kq=f"${{{phan_so(1/6)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==7:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 8 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 8 là ${{{phan_so(5/36)}}}$."

        kq=f"${{{phan_so(5/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,2)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "


    if chon ==8:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 9 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 9 là ${{{phan_so(4/36)}}}$."

        kq=f"${{{phan_so(4/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(1,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==9:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 10 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 10 là ${{{phan_so(3/36)}}}$."

        kq=f"${{{phan_so(3/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==10:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 11 là"
        noi_dung_loigiai=f" Xác suất để tổng số chấm của hai lần gieo bằng 11 là ${{{phan_so(2/36)}}}$."

        kq=f"${{{phan_so(2/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==11:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm của hai lần gieo bằng 12 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm của hai lần gieo bằng 12 là ${{{phan_so(1/36)}}}$."

        kq=f"${{{phan_so(1/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==12:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm của hai lần gieo chia hết cho 5 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm của hai lần gieo chia hết cho 5 là ${{{phan_so(11/36)}}}$."

        kq=f"${{{phan_so(11/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==13:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm của hai lần gieo chia hết cho 10 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm của hai lần gieo chia hết cho 10 là ${{{phan_so(6/36)}}}$."

        kq=f"${{{phan_so(6/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==14:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm của hai lần gieo chia hết cho 6 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm của hai lần gieo chia hết cho 6 là ${{{phan_so(15/36)}}}$."

        kq=f"${{{phan_so(15/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,16)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==15:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm của hai lần gieo chia hết cho 8 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm của hai lần gieo chia hết cho 8 là ${{{phan_so(3/36)}}}$."

        kq=f"${{{phan_so(3/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==16:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm của hai lần gieo chia hết cho 4 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm của hai lần gieo chia hết cho 4 là ${{{phan_so(15/36)}}}$."

        kq=f"${{{phan_so(15/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==17:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm của hai lần gieo chia hết cho 9 là"
        noi_dung_loigiai=f" Xác suất để tích số chấm của hai lần gieo chia hết cho 9 là ${{{phan_so(4/36)}}}$."

        kq=f"${{{phan_so(4/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==18:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là"
        noi_dung_loigiai=f" Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là ${{{phan_so(11/36)}}}$."

        kq=f"${{{phan_so(11/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==19:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là"
        noi_dung_loigiai=f" Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là ${{{phan_so(11/36)}}}$."

        kq=f"${{{phan_so(11/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==20:
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để hai lần gieo có số chấm xuất hiện giống nhau là"
        noi_dung_loigiai=f"Xác suất để của hai lần gieo có số chấm xuất hiện giống nhau là ${{{phan_so(6/36)}}}$."

        kq=f"${{{phan_so(6/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==21:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để có mặt ${{{a}}}$ xuất hiện đúng một lần là"
        noi_dung_loigiai=f" Xác suất để có mặt ${{{a}}}$ chấm xuất hiện là ${{{phan_so(10/36)}}}$."

        kq=f"${{{phan_so(10/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==22:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm xuất hiện của hai lần gieo là một số lẻ là"
        noi_dung_loigiai=f"Xác suất để tích số chấm xuất hiện của hai lần gieo là một số lẻ là ${{{phan_so(9/36)}}}$."

        kq=f"${{{phan_so(9/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==23:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tích số chấm xuất hiện của hai lần gieo là một số chẵn là"
        noi_dung_loigiai=f"Xác suất để tích số chấm xuất hiện của hai lần gieo là một số lẻ là ${{{phan_so(3/4)}}}$."

        kq=f"${{{phan_so(3/4)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==24:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 7 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 7 là ${{{phan_so(15/36)}}}$."

        kq=f"${{{phan_so(15/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$  "
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$  "
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==25:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 6 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 7 là ${{{phan_so(10/36)}}}$."

        kq=f"${{{phan_so(10/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$"
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$"
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "

    if chon ==26:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 6 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 6 là ${{{phan_so(10/36)}}}$."

        kq=f"${{{phan_so(10/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$"
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$"
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    if chon ==27:
        a=random.randint(1,6)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần. Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 5 là"
        noi_dung_loigiai=f"Xác suất để tổng số chấm xuất hiện của hai lần gieo nhỏ hơn 5 là ${{{phan_so(7/36)}}}$."

        kq=f"${{{phan_so(7/36)}}}$ "
        kq2=f"${{{phan_so(1/(6+random.randint(7,20)))}}}$"
        kq3=f"${{{phan_so(2/(18+random.randint(1,6)))}}}$"
        kq4=f" ${{{phan_so(3/(36-random.randint(10,15)))}}}$ "
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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



#[D10_C9_B2_30]-M2. XS các btoán ghép số khi gieo 1 con xúc xắc 2 lần(7 kiểu)
def mjulk_L10_C9_B2_30(): 
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    a=36
    bo_1 = range(1, 7)
    bo_2 = range(1, 7)

    ds = [10 * x + y for x in bo_1 for y in bo_2]

    chon =random.randint(1,7)
    if chon ==1:
        
        c=sum(x % 2 == 0 for x in ds)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần, đem kết quả ghép thành số có hai chữ số với chữ số của lần gieo thứ nhất là chữ số hàng chục. Xác xuất để số tạo thành là số chẵn là: "

    if chon ==2:
        
        c=sum(x % 2 != 0 for x in ds)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần, đem kết quả ghép thành số có hai chữ số với chữ số của lần gieo thứ nhất là chữ số hàng chục. Xác xuất để số tạo thành là số lẻ là: "

    if chon ==3:
        c=sum(all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ds)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần, đem kết quả ghép thành số có hai chữ số với chữ số của lần gieo thứ nhất là chữ số hàng chục. Xác xuất để số tạo thành là số nguyên tố là: "
    
    if chon ==4:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u == 0 for x in ds)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần, đem kết quả ghép thành số có hai chữ số với chữ số của lần gieo thứ nhất là chữ số hàng chục. Xác xuất để số tạo thành là số chia hết cho ${{{u}}}$ là: "

    if chon ==5:
        i=random.randint(10,20)
        j=i+random.randint(20,50)
        c=sum(i < x < j for x in ds)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần, đem kết quả ghép thành số có hai chữ số với chữ số của lần gieo thứ nhất là chữ số hàng chục. Xác xuất để số tạo thành là số lớn hơn ${{{i}}}$ và nhỏ hơn ${{{j}}}$ là: "

    if chon ==6:

        c=sum(int(x**0.5)**2 == x for x in ds if x >= 0)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần, đem kết quả ghép thành số có hai chữ số với chữ số của lần gieo thứ nhất là chữ số hàng chục. Xác xuất để số tạo thành là số chính phương là: "

    if chon ==7:
        u=random.choice([3,4,5,6,10])
        c=sum(x % u != 0 for x in ds)
        noi_dung=f" Bạn {A} gieo ngẫu nhiên một con xúc xắc cân đối và đồng chất hai lần, đem kết quả ghép thành số có hai chữ số với chữ số của lần gieo thứ nhất là chữ số hàng chục. Xác xuất để số tạo thành là số không chia hết cho ${{{u}}}$ là: "

    noi_dung_loigiai=(f" Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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



#[D10_C9_B2_24]-M3. Tính xác suất các btoán về rút thẻ số 2 lần có hoàn trả lại và ghép lại với nhau(12 kiểu)
def mjulk_L10_C9_B2_24(): 
    a2=random.randint(1,3)
    a1=a2+random.randint(3,5)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)

    danh_sach = [10 * x + y for x in nhom1 for y in nhom2]
    a=len(danh_sach)
    chon =random.randint(1,11)

    if chon ==1:
        b=random.choice([3,4,5,6])
        danh_sach_moi = list(filter(lambda x: x % b==0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số chia hết cho ${{{b}}}$ là:  "
        
    if chon ==2:
        b=max(danh_sach)-random.randint(1,4)
        danh_sach_moi = list(filter(lambda x: x < b, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số nhỏ hơn ${{{b}}}$ là:  "
        

    if chon == 3:
        danh_sach_moi = list(filter(lambda x: la_so_nguyen_to(x), danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số nguyên tố là:  "
    if chon == 4:
        danh_sach_moi = list(filter(lambda x: la_so_chinh_phuong(x), danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số chính phương là:  "
        


    if chon == 5:

        danh_sach_moi = list(filter(lambda x: la_hop_so(x), danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là hợp số là:  "
        

    if chon == 6:
        m=min(danh_sach)+1
        n=max(danh_sach)-random.randint(1,3)
        danh_sach_moi = list(filter(lambda x: m <x <n, danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số lớn hơn ${{{m}}}$ và nhỏ hơn ${{{n}}}$ là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=random.choice([3,4,5,6])
        danh_sach_moi = list(filter(lambda x: x % b!=0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là ghi số không chia hết cho ${{{b}}}$ là:  "
        

    if chon == 9:
        b=random.choice([i for i in range(2,5)])
        e=random.choice([i for i in range(2,6) if i!=b and i%b!=0 and b%i !=0])
        danh_sach_moi = list(filter(lambda i: i % b == 0 and i%e==0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là bội của ${{{b}}}$ và ${{{e}}}$ là:  "
    if chon ==10:
        danh_sach_moi = list(filter(lambda x: x % 2 == 0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số chẵn là:  "
    

    if chon ==11:
        danh_sach_moi = list(filter(lambda x: x % 2 != 0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số lẻ là:  "

    if chon == 8:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)

        danh_sach_moi = list(filter(lambda x: x % b == j, danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép kết quả 2 lần rút thẻ thành số có hai chữ số với chữ số trên tấm thẻ rút lần đầu là chữ số hàng chục. Xác suất để kết quả là số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "

    danh_sach=str(danh_sach).replace("[","\\left\\{").replace("]","\\right\\} ").replace(",",";")
    danh_sach_moi=str(danh_sach_moi).replace("[","\\left\\{").replace("]","\\right\\} ").replace(",",";")
    noi_dung_loigiai=(f" $\\Omega = \\left\\{{ \\overline {{ij}}  ; {a2} \\le i;j \\le {a1} \\right\\}} $\n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
             f"$A={danh_sach_moi}$ \n\n Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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





#[D10_C9_B2_25]-M3. XS các btoán về rút thẻ số 2lần có hoàn trả lại và cộng kq lại với nhau(10kiểu)
def mjulk_L10_C9_B2_25(): 
    a2=random.randint(1,4)
    a1=a2+random.randint(3,5)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)

    danh_sach = [x + y for x in nhom1 for y in nhom2]
    a=len(danh_sach)
    chon =random.randint(1,10)

    if chon ==1:
        b=random.choice([i for i in range(3, int(a/2))])
        c=len([i for i in danh_sach if i % b == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia hết cho ${{{b}}}$ là:  "
        
    if chon ==2:
        b=random.randint(6,12)
        c=len([i for i in danh_sach if i < b])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số nhỏ hơn ${{{b}}}$ là:  "
        

    if chon == 3:
        c = sum(1 for i in danh_sach if la_so_nguyen_to(i))
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số nguyên tố là:  "
        

    if chon == 4:
        c = sum(1 for i in danh_sach if la_so_chinh_phuong(i))
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chính phương là:  "
        


    if chon == 5:
        c = sum(1 for i in danh_sach if la_hop_so(i) )
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là hợp số là:  "
        
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=random.choice([i for i in range(3,int(a/2))])
        c = len([i for i in danh_sach if i % b != 0])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là ghi số không chia hết cho ${{{b}}}$ là:  "
        

    if chon == 9:
        b=random.choice([i for i in range(2,5)])
        e=random.choice([i for i in range(2,6) if i!=b and i%b!=0 and b%i !=0])
        c = len([i for i in danh_sach if i % b == 0 and i%e==0 ])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là bội của ${{{b}}}$ và ${{{e}}}$ là:  "
    if chon ==10:
        c=len([i for i in danh_sach if i % 2 == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chẵn là:  "
    

    if chon ==6:
        c=len([i for i in danh_sach if i % 2 != 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số lẻ là:  "

    if chon == 8:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)
        c=sum(1 for so in danh_sach if so % b == j)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "

    noi_dung_loigiai=(f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_26]-M3. XS các btoán về rút thẻ số 2lần có hoàn trả lại và nhân kq lại với nhau(10kiểu)
def mjulk_L10_C9_B2_26(): 
    a2=random.randint(2,4)
    a1=a2+random.randint(3,5)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)

    danh_sach = [x * y for x in nhom1 for y in nhom2]
    a=len(danh_sach)
    chon =random.randint(1,8)

    if chon ==1:
        b=random.choice([3,4,5,6,12,20])
        c=len([i for i in danh_sach if i % b == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia hết cho ${{{b}}}$ là:  "
        
    if chon ==2:
        b=random.randint(20,35)
        c=len([i for i in danh_sach if i < b])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số nhỏ hơn ${{{b}}}$ là:  "
        
    if chon == 4:
        c = sum(1 for i in danh_sach if la_so_chinh_phuong(i))
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chính phương là:  "
        

    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=random.choice([i for i in range(3,int(a/2))])
        c = len([i for i in danh_sach if i % b != 0])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là ghi số không chia hết cho ${{{b}}}$ là:  "
        

    if chon == 5:
        b=random.choice([i for i in range(2,5)])
        e=random.choice([i for i in range(2,6) if i!=b and i%b!=0 and b%i !=0])
        c = len([i for i in danh_sach if i % b == 0 and i%e==0 ])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là bội của ${{{b}}}$ và ${{{e}}}$ là:  "
    if chon ==3:
        c=len([i for i in danh_sach if i % 2 == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chẵn là:  "
    

    if chon ==6:
        c=len([i for i in danh_sach if i % 2 != 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số lẻ là:  "

    if chon == 8:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)
        c=sum(1 for so in danh_sach if so % b == j)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "

    noi_dung_loigiai=(f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
    f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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






#[D10_C9_B2_27]-M4. XS các btoán về rút thẻ số 2lần không trả lại và nhân kq lại với nhau(7kiểu)
def mjulk_L10_C9_B2_27(): 
    a2=random.randint(2,4)
    a1=a2+random.randint(3,5)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)

    danh_sach = [x * y for x in nhom1 for y in nhom2 if y!=x]
    a=len(danh_sach)
    chon =random.randint(1,7)

    if chon ==1:
        b=random.choice([3,4,5,6,8,12])
        c=len([i for i in danh_sach if i % b == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia hết cho ${{{b}}}$ là:  "
        
    if chon ==2:
        b=random.randint(20,35)
        c=len([i for i in danh_sach if i < b])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số nhỏ hơn ${{{b}}}$ là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=random.choice([i for i in range(3,int(a/2))])
        c = len([i for i in danh_sach if i % b != 0])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là ghi số không chia hết cho ${{{b}}}$ là:  "
        

    if chon == 5:
        b=random.choice([i for i in range(2,5)])
        e=random.choice([i for i in range(2,6) if i!=b and i%b!=0 and b%i !=0])
        c = len([i for i in danh_sach if i % b == 0 and i%e==0 ])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là bội của ${{{b}}}$ và ${{{e}}}$ là:  "
    if chon ==3:
        c=len([i for i in danh_sach if i % 2 == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chẵn là:  "
    

    if chon ==6:
        c=len([i for i in danh_sach if i % 2 != 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số lẻ là:  "

    if chon == 4:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)
        c=sum(1 for so in danh_sach if so % b == j)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, nhân các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "

    noi_dung_loigiai=(f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
             f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_28]-M4. XS các btoán về rút thẻ số 2lần không trả lại và cộng kq lại với nhau(9kiểu)
def mjulk_L10_C9_B2_28(): 
    a2=random.randint(2,4)
    a1=a2+random.randint(3,5)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)

    danh_sach = [x + y for x in nhom1 for y in nhom2 if y!=x]
    a=len(danh_sach)
    chon =random.randint(1,9)

    if chon ==1:
        b=random.choice([3,4,5,6])
        c=len([i for i in danh_sach if i % b == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia hết cho ${{{b}}}$ là:  "
        
    if chon ==2:
        b=random.randint(7,12)
        c=len([i for i in danh_sach if i < b])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số nhỏ hơn ${{{b}}}$ là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=random.choice([i for i in range(3,int(a/2))])
        c = len([i for i in danh_sach if i % b != 0])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là ghi số không chia hết cho ${{{b}}}$ là:  "
        

    if chon == 5:
        b=random.choice([i for i in range(2,5)])
        e=random.choice([i for i in range(2,6) if i!=b and i%b!=0 and b%i !=0])
        c = len([i for i in danh_sach if i % b == 0 and i%e==0 ])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là bội của ${{{b}}}$ và ${{{e}}}$ là:  "
    if chon ==3:
        c=len([i for i in danh_sach if i % 2 == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chẵn là:  "
    

    if chon ==6:
        c=len([i for i in danh_sach if i % 2 != 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số lẻ là:  "

    if chon == 4:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)
        c=sum(1 for so in danh_sach if so % b == j)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "
    if chon ==8:
        c=len([i for i in danh_sach if la_so_nguyen_to(i)])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là số nguyên tố là:  "

    if chon ==9:
        c=len([i for i in danh_sach if la_hop_so(i)])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, cộng các số của 2 lần rút thẻ lại. Xác suất để kết quả là hợp tố là:  "

    noi_dung_loigiai=(f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
             f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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












#[D10_C9_B2_29]-M4. XS các btoán về rút thẻ số 2lần không trả lại và ghép kq lại với nhau(9kiểu)
def mjulk_L10_C9_B2_29(): 
    a2=random.randint(2,4)
    a1=a2+random.randint(3,5)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)

    danh_sach = [10*x + y for x in nhom1 for y in nhom2 if y!=x]
    a=len(danh_sach)
    chon =random.randint(1,9)

    if chon ==1:
        b=random.choice([3,4,5,6])
        c=len([i for i in danh_sach if i % b == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là số chia hết cho ${{{b}}}$ là:  "
        
    if chon ==2:
        b=random.randint(27,52)
        c=len([i for i in danh_sach if i < b])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là số nhỏ hơn ${{{b}}}$ là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=random.choice([i for i in range(3,int(a/2))])
        c = len([i for i in danh_sach if i % b != 0])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là ghi số không chia hết cho ${{{b}}}$ là:  "
        

    if chon == 5:
        b=random.choice([i for i in range(2,5)])
        e=random.choice([i for i in range(2,6) if i!=b and i%b!=0 and b%i !=0])
        c = len([i for i in danh_sach if i % b == 0 and i%e==0 ])
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là bội của ${{{b}}}$ và ${{{e}}}$ là:  "
    if chon ==3:
        c=len([i for i in danh_sach if i % 2 == 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là số chẵn là:  "
    

    if chon ==6:
        c=len([i for i in danh_sach if i % 2 != 0])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là số lẻ là:  "

    if chon == 4:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)
        c=sum(1 for so in danh_sach if so % b == j)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "
    if chon ==8:
        c=len([i for i in danh_sach if la_so_nguyen_to(i)])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là số nguyên tố là:  "

    if chon ==9:
        c=len([i for i in danh_sach if la_hop_so(i)])
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên 1 thẻ và không trả lại hộp, tiếp tục rút ngẫu nhiên 1 thẻ 1 lần nữa, ghép các số của 2 lần rút thẻ lại thành một số có hai chữ số với chữ số hàng chục là kết quả lần rút thứ nhất. Xác suất để kết quả là hợp tố là:  "

    noi_dung_loigiai=(f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
             f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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




#[D10_C9_B2_30]-M4. XS các btoán về rút thẻ số nhiều lần không trả lại và ghép kq lại với nhau(12kiểu)
def mjulk_L10_C9_B2_30(): 
    a1=random.choice([1,3,5,7,9] )
    a3=random.choice([2,4,6,8] )
    a4=random.choice([i for i in range(1,9) if i!=a1 and i!=a3])
    a2=random.choice([i for i in range(1,9) if i!=a1 and i!=a3 and i!=a4])

    chu_so=[a1, a2, a3, a4]
    b1, b2=random.sample(chu_so,2)


    danh_sach=[int("".join(map(str, p))) for p in permutations(chu_so, 4)] 
    e=min(danh_sach)

    a=len(danh_sach)
    chon =random.randint(1,12)


    if chon ==2:
        b=random.randint(e+1000,e+4000)
        c=len([i for i in danh_sach if i < b])
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số nhỏ hơn ${{{b}}}$ là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 7:
        b=random.choice([3,4,5,6,7,8])
        c = len([i for i in danh_sach if i % b != 0])
        noi_dung = f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là ghi số không chia hết cho ${{{b}}}$ là:  "
        


    if chon ==3:
        c=len([i for i in danh_sach if i % 2 == 0])
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số chẵn là:  "
    

    if chon ==6:
        c=len([i for i in danh_sach if i % 2 != 0])
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số lẻ là:  "

    if chon == 4:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)
        c=sum(1 for so in danh_sach if so % b == j)
        noi_dung = f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "
    if chon ==8:
        c=len([i for i in danh_sach if la_so_nguyen_to(i)])
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số nguyên tố là:  "

    if chon ==9:
        c=len([i for i in danh_sach if la_hop_so(i)])
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là hợp tố là:  "

    if chon ==10:
        c=2
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số có các chữ số tăng dần hoặc giảm dần là:  "
    hang=[" trăm", "nghìn", "chục", "đơn vị"]
    dv, dv1=random.sample(hang, 2)

    if chon ==11:

        c=6
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số có chữ số ${{{b1}}}$ xuất hiện ở hàng {dv} là:  "

    if chon ==1:

        c=2
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số có chữ số ${{{b1}}}$ xuất hiện ở hàng {dv} và chữ số ${{{b2}}}$ xuất hiện ở hàng {dv1} là:  "
    if chon ==5:

        c=18
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số có chữ số ${{{a1}}}$ không xuất hiện ở hàng {dv} là:  "
    
    if chon ==12:
        tang=random.choice([" tăng", "giảm"])
        c=1
        noi_dung=f"Một hộp chứa ${{4}}$ thẻ gồm các số ${a1}; {a2}; {a3}; {a4}$ (mỗi thẻ chỉ đánh một số). Rút ngẫu nhiên ${{4}}$ lần mỗi lần 1 thẻ và không lần nào hoàn trả lại hộp, ghép các số của 4 lần rút thẻ lại thành một số có 4 chữ số với chữ số hàng nghìn là kết quả lần rút thứ nhất, chữ số hàng trăm là kết quả của lần rút thứ hai, chữ số hàng chục là kết quả của lần rút thứ 3, chữ số hàng đơn vị là kết quả của lần rút cuối cùng. Xác suất để số tạo thành là số có các chữ số {tang} dần là:  "


    noi_dung_loigiai=(f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
             f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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






#[D10_C9_B2_31]-M3. XS các btoán rút vật từ hộp này bỏ sang hộp kia
def mjulk_L10_C9_B2_31():
    m=random.randint(3,5) 
    n=random.choice([i for i in range(4,6)])
    c=1 
    a=n+1 
    A=random.choice(["quả bóng", "quả cầu", "viên bi","quyển sách", "thanh kẹo"])

    noi_dung=f" Có hai hộp: hộp I chứa ${{{m}}}$ {A}, hộp II chứa ${{{n}}}$ {A} (các {A} đều có kích thước và khối lượng như nhau). Lấy ngẫu nhiên một {A} từ hộp I bỏ sang hộp II, rồi lại lấy ngẫu nhiên một {A} từ hộp II bỏ ra ngoài. Tính xác suất để {A} lấy ra chính là {A} của hộp I."
    noi_dung_loigiai=(f"\n\n  Đánh số các {A} của hộp I là $A_{{1}};A_{{2}};...;A_{{{m}}}$, đánh số các {A} của hộp II là $B_{{1}};B_{{2}};...;B_{{{n}}}$. \n\n"
                    f" Phép thử: Lấy ngẫu nhiên một {A} từ hộp I bỏ sang hộp II, rồi lại lấy ngẫu nhiên một \n\n {A} từ hộp II ra ngoài. \n\n"
                    f" Không gian mẫu là tập hợp gồm các phần tử có dạng $A_{{i}} B_{{j}} $ và $A_{{i}}A_{{i}}$ với $1\\le i \\le {m}, 1 \\le j \\le {n}, i, j \\in \\mathbb{{N}}$ \n\n"
                    f" $ n(\\Omega)= {phan_so(m*n+m)}$ \n\n"
                    f" Xét biến cố A: {A} lấy ra chính là {A} của hộp I \n\n "
                    f" Các kết quả thuận lợi của biến cố A là $A_{{i}}A_{{i}}$ với $1 \\le i \\le {m}$ \n\n "
                    f" $n(A)={m}$ \n\n"
                    f" Vậy $P(A)={phan_so(1/(n+1))}$")
    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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





#[D10_C9_B2_40]-TF-M3. XS các bài toán chọn 4 người từ một nhóm
def mjulk_L10_C9_B2_40():
    a2=random.randint(10,20)
    a3=random.randint(10,25)
    a1=a2+a3
    a=math.comb(a1, 4)
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])

    noi_dung = f"Một đội có ${{{a2}}}$ bạn nam trong đó có bạn nam tên {B} và ${{{a3}}}$ bạn nữ trong đó có bạn nữ tên {A}. Giáo viên chọn ngẫu nhiên ra bốn bạn tham gia hội khoẻ phù đổng của huyện. Xét tính đúng-sai của các khẳng định sau. "       
    debai_word= f"{noi_dung}\n"
    
    chon =random.randint(1,2)
    if chon ==1:
	    c=math.comb(a2,4)
	    kq1_T=f"*Xác suất để chọn được ${{4}}$ bạn nam là ${{{phan_so(c/a)}}}$" 
	    kq1_F=f"Xác suất để chọn được ${{4}}$ bạn nam là "
	    kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	    kq1=random.choice([kq1_T, kq1_F])
	    HDG=(f"${{ n(\\Omega)= {a} }}$ \n\n"
	        f" Gọi ${{A}}$ là biến cố chọn được ${{4}}$ bạn nam\n\n "
	        f" ${{n(A)= {c}}}$ \n\n"
	        f" ${{ P(A)= {phan_so(c/a)} }}$")   
    if chon ==2:
	    c=math.comb(a3,4)
	    kq1_T=f"*Xác suất để chọn được ${{4}}$ bạn nữ là ${{{phan_so(c/a)}}}$" 
	    kq1_F=f"Xác suất để chọn được ${{4}}$ bạn nữ là "
	    kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	    kq1=random.choice([kq1_T, kq1_F])
	    HDG=(f"${{ n(\\Omega)= {a} }}$ \n\n"
	        f" Gọi ${{A}}$ là biến cố chọn được ${{4}}$ bạn nữ\n\n "
	        f" ${{n(A)= {c}}}$ \n\n"
	        f" ${{ P(A)= {phan_so(c/a)} }}$")   
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    chon =random.randint(1,3)
    if chon ==1:

	    c=math.comb(a2,2)*math.comb(a3,2)
	    kq2_T=f"*Xác suất để chọn được ${{2}}$ bạn nam và ${{2}}$ bạn nữ là ${{{phan_so(c/a)}}}$ "
	    kq2_F=f"Xác suất để trong bốn bạn được chọn có ${{2}}$ bạn nam và ${{2}}$ bạn nữ là "
	    kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	    kq2=random.choice([kq2_T, kq2_F])
	    HDG=(f" Gọi ${{B}}$ là biến cố trong ba bạn được chọn ${{2}}$ bạn nam và ${{2}}$ bạn nữ \n\n "
	        f" ${{n(B)= {c}}}$ \n\n"
	        f" ${{ P(B)= {phan_so(c/a)} }}$")   

    if chon ==2:

	    c=math.comb(a3,3)*a2
	    kq2_T=f"*Xác suất để trong bốn bạn được chọn có ${{3}}$ bạn nữ và ${{1}}$ bạn nam là ${{{phan_so(c/a)}}}$ "
	    kq2_F=f"Xác suất để trong bốn bạn được chọn có ${{3}}$ bạn nữ và ${{1}}$ bạn nam là "
	    kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	    kq2=random.choice([kq2_T, kq2_F])
	    HDG=(f" Gọi ${{B}}$ là biến cố trong ba bạn được chọn có${{3}}$ bạn nữ và ${{1}}$ bạn nam \n\n "
	        f" ${{n(B)= {c}}}$ \n\n"
	        f" ${{ P(B)= {phan_so(c/a)} }}$")   

    if chon ==3:

	    c=math.comb(a2,3)*a3
	    kq2_T=f"*Xác suất để trong bốn bạn được chọn có ${{3}}$ bạn nam và ${{1}}$ bạn nữ là ${{{phan_so(c/a)}}}$ "
	    kq2_F=f"Xác suất để trong bốn bạn được chọn có ${{3}}$ bạn nam và ${{1}}$ bạn nữ là "
	    kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	    kq2=random.choice([kq2_T, kq2_F])
	    HDG=(f" Gọi ${{B}}$ là biến cố trong bốn bạn được chọn có${{3}}$ bạn nam và ${{1}}$ bạn nữ \n\n "
	        f" ${{n(B)= {c}}}$ \n\n"
	        f" ${{ P(B)= {phan_so(c/a)} }}$")   
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon =random.randint(1,4)
    if chon ==1:
	    c= math.comb(a3-1, 4)
	    kq3_T=f"*Xác suất để chọn được ${{4}}$ bạn nữ nhưng không có bạn {A} là ${{{phan_so(c/a)}}}$ " 
	    kq3_F=f" Xác suất để chọn được ${{4}}$ bạn nữ nhưng không có bạn {A} "

	    kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	    kq3=random.choice([kq3_T, kq3_F])
	    HDG=(f" Gọi ${{C}}$ là biến cố chọn được ${{3}}$ bạn nữ nhưng không có bạn {A} \n\n "
	        f" ${{n(C)= {c}}}$ \n\n"
	        f" ${{ P(C)= {phan_so(c/a)} }}$")   
	    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	    if kq3==kq3_F:
	        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon ==2:
	    c= math.comb(a3-1, 3)
	    kq3_T=f"*Xác suất để chọn được ${{4}}$ bạn nữ trong đó có bạn {A} là ${{{phan_so(c/a)}}}$ " 
	    kq3_F=f" Xác suất để chọn được ${{4}}$ bạn nữ trong đó có bạn {A} "

	    kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
	            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
	    kq3=random.choice([kq3_T, kq3_F])
	    HDG=(f" Gọi ${{C}}$ là biến cố chọn được ${{4}}$ bạn nữ trong đó có bạn {A} \n\n "
	        f" ${{n(C)= {c}}}$ \n\n"
	        f" ${{ P(C)= {phan_so(c/a)} }}$")   
	    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	    if kq3==kq3_F:
	        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon ==3:
        c= math.comb(a2-1, 4)
        kq3_T=f"*Xác suất để chọn được ${{4}}$ bạn nam nhưng không có bạn {B} là ${{{phan_so(c/a)}}}$ " 
        kq3_F=f" Xác suất để chọn được ${{4}}$ bạn nam nhưng không có bạn {B} "

        kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" Gọi ${{C}}$ là biến cố chọn được ${{4}}$ bạn nam nhưng không có bạn {B} \n\n "
            f" ${{n(C)= {c}}}$ \n\n"
            f" ${{ P(C)= {phan_so(c/a)} }}$")   
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon ==4:
        c= math.comb(a2-1, 3)
        kq3_T=f"*Xác suất để chọn được ${{4}}$ bạn nam trong đó có bạn {B} là ${{{phan_so(c/a)}}}$ " 
        kq3_F=f" Xác suất để chọn được ${{4}}$ bạn nam trong đó có bạn {B} "

        kq3_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" Gọi ${{C}}$ là biến cố chọn được ${{4}}$ bạn nam trong đó có bạn {B} \n\n "
            f" ${{n(C)= {c}}}$ \n\n"
            f" ${{ P(C)= {phan_so(c/a)} }}$")   
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    chon =random.randint(1,6)
    if chon ==1:
        c= math.comb(a2-1,2)*math.comb(a3,2)
        kq4_T=f"*Xác suất để chọn được hai bạn nam và hai bạn nữ trong đó không có {B} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Xác suất để chọn được hai bạn nam và một bạn nữ trong đó không có {B} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nam và một bạn nữ trong đó không có {B}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   

    if chon ==2:
        c=math.comb(a2,3)*math.comb(a3-1,1)
        kq4_T=f"*Xác suất để chọn được ba bạn nữ và một bạn nam trong đó không có {B} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Xác suất để chọn được ba bạn nữ và một bạn nam trong đó không có {B} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được ba bạn nữ và một bạn nam trong đó không có {B}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   

    if chon ==3:
        c= math.comb(a3-1,3)*a2
        kq4_T=f"*Xác suất để chọn được ba bạn nữ và một bạn nam trong đó không có {A} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Xác suất để chọn được ba bạn nữ và một bạn nam trong đó không có {A} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được ba bạn nữ và một bạn nam trong đó không có {A}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


    if chon ==4:
        c= math.comb(a3-1,1)*math.comb(a2,2)
        kq4_T=f"*Xác suất để chọn được hai bạn nữ và hai bạn nam trong đó có {A} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Xác suất để chọn được hai bạn nữ và hai bạn nam trong đó có {A} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nữ và hai bạn nam trong đó có {A}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


    if chon ==5:
        c=  math.comb(a2-1,1)*math.comb(a3,2)
        kq4_T=f"*Xác suất để chọn được hai bạn nam và hai bạn nữ trong đó có {B} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Xác suất để chọn được hai bạn nam và hai bạn nữ trong đó có {B} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nam và hai bạn nữ trong đó có {B}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


    if chon ==6:
        c= math.comb(a2-1,2)*math.comb(a3-1,2)
        kq4_T=f"*Xác suất để chọn được hai bạn nam và hai bạn nữ trong đó không có {B} và {A} là ${{{phan_so(c/a)}}}$  "
        kq4_F=f"Xác suất để chọn được hai bạn nam và hai bạn nữ trong đó không có {B} và {A} là " 
        kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" Gọi ${{D}}$ là biến cố chọn được hai bạn nam và hai bạn nữ trong đó không có {B} và {A}\n\n "
            f" ${{n(D)= {c}}}$ \n\n"
            f" ${{ P(D)= {phan_so(c/a)} }}$")   


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





#[D10_C9_B2_41]-TF-M3. XS các bài toán chọn vật(viên bi, quả cầu)
def mjulk_L10_C9_B2_41():
    D=random.choice(["viên bi", "quả cầu"])
    ds=["xanh","vàng", "đen", "tím", "trắng", "đỏ", "nâu", "xám"]
    A, B, C=random.sample(ds, 3)  
    k=random.randint(3,4)
    a1=k+random.randint(1,5)
    a2=k+random.randint(1,5)
    a3=a2+random.randint(1,3)
    a=a1+a2+a3
    a=math.comb(a,k)

    c=math.comb(a1,k)

    noi_dung = f"Một hộp chứa ${{{a1}}}$ {D} {A}, ${{{a2}}}$ {D} {B} và ${{{a3}}}$ {D} {C}. Chọn ngẫu nhiên không nhìn vào hộp ${{{k}}}$ {D}. Xét tính đúng-sai của các khẳng định sau. "     
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"*Xác suất để lấy được ${{{k}}}$ {D} {A} là ${{{phan_so(c/a)}}}$" 
    kq1_F=f"Xác suất để lấy được ${{{k}}}$ {D} {A} là  "
    kq1_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
            f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f"${{ n(\\Omega)= {a} }}$ \n\n"
        f" Gọi ${{A}}$ là biến cố lấy được ${{{k}}}$ {D} {A}\n\n "
        f" ${{n(A)=  C^{{{k}}}_{{{a1}}} = {c}}}$ \n\n"
        f" ${{ P(A)= {phan_so(c/a)} }}$")   


    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    c=math.comb(a1+a3,k)

    kq2_T=f"*Xác suất để ${{{k}}}$ {D} lấy ra không có {D} {B} là ${{{phan_so(c/a)}}}$ "
    kq2_F=f"Xác suất để ${{{k}}}$ {D} lấy ra không có {D} {B} là "
    kq2_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])

    kq2=random.choice([kq2_T, kq2_F])
    HDG=(f" Gọi ${{B}}$ là biến cố ${{{k}}}$ {D} lấy ra không có {D} {B} \n\n "
        f" ${{n(B)= C^{{{k}}}_{{{a1+a3}}}={c}}}$ \n\n"
        f" ${{ P(B)= {phan_so(c/a)} }}$")   

    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"



    c= math.comb(a1+a2,k)
    kq3_T=f"* Xác suất để ${{{k}}}$ {D} lấy ra có ít nhất một {D} {C} là ${{ {phan_so(1-(c/a))}}}$" 
    kq3_F=f"Xác suất để ${{{k}}}$ {D} lấy ra có ít nhất một {D} {C} là ${{ {phan_so(1-(c/(a+1)))}}}$ "
    kq3=random.choice([kq3_T, kq3_F])
    HDG=(f" Gọi ${{C}}$ là biến cố ${{{k}}}$ {D} lấy ra không có {D} {C} \n\n "
        f" ${{n(C)= C^{{{k}}}_{{{a1+a2}}}={c}}}$ \n\n"
        f" ${{ P(C)= {phan_so(c/a)} }}$ \n\n"
        f"Xác suất để ${{{k}}}$ {D} lấy ra có ít nhất một {D} {C} là ${{ 1-  {phan_so(c/a)}  = {phan_so(1-(c/a))} }}$")       


    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"



    if k==3: c=a1*a2*a3
    if k==4: c= math.comb(a1,1)*math.comb(a2,1)*math.comb(a3,2)+ math.comb(a1,2)*math.comb(a2,1)*math.comb(a3,1)+ math.comb(a1,1)*math.comb(a2,2)*math.comb(a3,1)

    kq4_T=f"*Xác suất để ${{{k}}}$ {D} lấy ra có đủ ba màu là ${{{phan_so(c/a)}}}$  "
    kq4_F=f"Xác suất để ${{{k}}}$ {D} lấy ra có đủ ba màu là " 
    kq4_F+=random.choice([f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ ", f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
                f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "])
    kq4=random.choice([kq4_T, kq4_F])

    HDG=(f"Gọi ${{C}}$ là biến cố ${{{k}}}$ {D} lấy ra có đủ ba màu \n\n "
      f" ${{n(C)= {c}}}$ \n\n"
        f" ${{ P(C)= {phan_so(c/a)} }}$")


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


#[D10_C9_B2_42]-M3. XS các btoan rút 2 thẻ số đồng thời(9 kiểu)
def mjulk_L10_C9_B2_42():

    danh_sach =random.sample(range(10, 100), random.randint(5, 9)) 
    a2=len(danh_sach) 
    a=math.comb(a2, 2)
    a1=random.choice([i for i in danh_sach])
    a3=random.choice([i for i in danh_sach if i!=a1])
    ds=str(danh_sach).replace("[","").replace("]","").replace(",",";") 
    DS=[x + y for i, x in enumerate(danh_sach) for j, y in enumerate(danh_sach) if i < j]
    DS1=[x * y for i, x in enumerate(danh_sach) for j, y in enumerate(danh_sach) if i < j]
    chon=random.randint(1,6)
    if chon ==1:
        c=a2-1
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp. Xác suất để rút được thẻ số ${{{a1}}}$ là:"
    if chon ==2: 
        c=math.comb(a2-1, 2)
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp. Xác suất để không rút được thẻ số ${{{a1}}}$ là:"
    if chon ==3: 
        c=math.comb(a2-2, 2)
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp. Xác suất để không rút được thẻ số ${{{a1}}}$ và thẻ số ${{{a2}}}$ là:"
    if chon ==4: 
        c=math.comb(a2-2, 2)
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp. Xác suất để rút được thẻ số ${{{a1}}}$ nhưng không rút được thẻ số ${{{a2}}}$ là:"
    if chon ==5: 
        c=len([i for i in DS if i % 2 == 0])
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp, rồi cộng hai số trên hai thẻ lại với nhau. Xác suất để kết quả là số chẵn là:"

    if chon ==6: 
        c=len([i for i in DS if i % 2 != 0])
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp, rồi cộng hai số trên hai thẻ lại với nhau. Xác suất để kết quả là số lẻ là:"
    if chon ==7: 
        c=len([i for i in DS1 if i % 2 == 0])
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp, rồi nhân hai số trên hai thẻ lại với nhau. Xác suất để kết quả là số chẵn là:"

    if chon ==8: 
        c=len([i for i in DS1 if i % 2 != 0])
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp, rồi nhân hai số trên hai thẻ lại với nhau. Xác suất để kết quả là số lẻ là:"

    if chon ==9: 
        b=random.choice([i for i in (3,6)])
        e=random.randint(1,b-1)
        c=len([i for i in DS if i % b != e])
        noi_dung=f" Một hộp chứa các thẻ số {ds}, rút ngẫu nhiên một lúc hai thẻ số mà không nhìn vào hộp, rồi cộng hai số trên hai thẻ lại với nhau. Xác suất để kết quả là số chia cho ${{{b}}}$ dư ${{{e}}}$ là:"
    

    noi_dung_loigiai=(f" \n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
             f" Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ ",f" ${{{phan_so(c/(a-5))}}} $",f" ${{{phan_so(c/(a-6))}}} $"]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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



#[D10_C9_B2_43]-M2. XS các btoán về rút đồng thời 2 thẻ và ghép kq lại với nhau(9kiểu)
def mjulk_L10_C9_B2_43(): 
    a2=random.randint(1,4)
    a1=a2+random.randint(3,5)
    a3= (a1-a2)+1
    nhom1 = range(a2, a1 + 1)
    nhom2 = range(a2, a1 + 1)

    danh_sach = [ int(f"{x}{y}") for x in nhom1 for y in nhom2 if x!=y]
    a=len(danh_sach) 
    chon =random.randint(1,9)

    if chon ==1:
        b=random.choice([3,4,5,6])
        danh_sach_moi = list(filter(lambda x: x % b==0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong danh sách số tạo thành. Xác suất để chọn được số là số chia hết cho ${{{b}}}$ là:  "
        
    if chon ==2:
        # i=min(ds)+1
        b=max(danh_sach)-random.randint(1,4)
        danh_sach_moi = list(filter(lambda x: x < b, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được số số nhỏ hơn ${{{b}}}$ là:  "
        
    
    # Tạo danh sách các phương án lựa chọn ngẫu nhiên

    if chon == 3:
        b=random.choice([i for i in range(3,int(a/2))])
        danh_sach_moi = list(filter(lambda x: x % b != 0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được số không chia hết cho ${{{b}}}$ là:  "
        

    if chon == 5:
        b=random.choice([i for i in range(2,5)])
        e=random.choice([i for i in range(2,6) if i!=b and i%b!=0 and b%i !=0])
        danh_sach_moi = list(filter(lambda i: i % b == 0 and i%e==0, danh_sach))
        c = len(danh_sach_moi)
        

        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được bội của ${{{b}}}$ và ${{{e}}}$ là:  "
    if chon ==7:

        danh_sach_moi = list(filter(lambda x: x % 2 == 0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được số chẵn là:  "
    

    if chon ==6:
        danh_sach_moi = list(filter(lambda x: x % 2 != 0, danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được số lẻ là:  "

    if chon == 4:
        b=random.choice([3,4,5,6])
        j=b-random.randint(1,b-1)

        danh_sach_moi = list(filter(lambda x: x % b == j, danh_sach))
        c = len(danh_sach_moi)
        noi_dung = f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được số chia cho ${{{b}}}$ dư ${{{j}}}$ là:  "
    if chon ==8:

        danh_sach_moi = list(filter(lambda x: la_so_nguyen_to(x), danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được số nguyên tố là:  "

    if chon ==9:
        c=len([i for i in danh_sach if la_hop_so(i)])
        danh_sach_moi = list(filter(lambda x: la_hop_so(x), danh_sach))
        c = len(danh_sach_moi)
        noi_dung=f"Một hộp chứa ${{{a3}}}$ thẻ được đánh số tự nhiên liên tiếp từ ${{{a2}}}$ đến ${{{a1}}}$ (mỗi thẻ chỉ đánh một số). Gọi ${{S}}$ là tập hợp các kết quả có thể của phép thử rút ngẫu nhiên cùng lúc 2 thẻ mà không nhìn vào hộp và ghép kết quả thành các số có hai chữ số. Chọn ngẫu nhiên một số trong tập ${{S}}$. Xác suất để chọn được hợp tố là:  "



    danh_sach=str(danh_sach).replace("[","\\left\\{").replace("]","\\right\\} ").replace(",",";")
    danh_sach_moi=str(danh_sach_moi).replace("[","\\left\\{").replace("]","\\right\\} ").replace(",",";")
    noi_dung_loigiai=(f" $\\Omega =  \\left\\{{ \\overline {{ij}}  ; {a2} \\le i;j \\le {a1} \\right\\}} $\n\n Số phần tử của không gian mẫu là ${{{a}}}$\n\n"
             f"$A={danh_sach_moi}$ \n\n Số kết quả thuận lợi của biến cố là ${{{c}}}$ \n\n"
        f"Xác suất là ${{{phan_so(c/a)}}}$")

    kq=f"${{{phan_so(c/a)}}}$ "
    if c!=0:

        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a-4))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]

    if c==0:
        c=c+random.randint(1,4)
        ds1=[f"${{{phan_so(c/(a-1))}}}$ ",   f"${{{phan_so(c/(a-2))}}}$ "
        ,f" ${{{phan_so(c/(a+4))}}}$",f" ${{{phan_so(c/(a+1))}}}$",f" ${{{phan_so(c/(a+2))}}}$" ,
        f" ${{{phan_so(c/(a+3))}}} $",f" ${{{phan_so(c/(a-3))}}}$",f" ${{{phan_so(c/(a+5))}}} $",f" ${{{phan_so(c/(a+7))}}}$",f" ${{{phan_so(c/(a+6))}}}$ "]


    kq2, kq3, kq4 = random.sample(ds1, 3)  


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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











#[D10_C9_B2_44]-SA-M3. cho a sách X, b sách Y, c sách Z, chọn m quyển, xs để số sách còn lại đủ 3 môn
def mjulk_L10_C9_B2_44(): 
	n1=random.randint(1,3)
	l1=random.randint(4,8)
	l=random.randint(4,8)
	l2=random.randint(4,9)
	m=max(l,l1,l2)+n1
	n=l+l1+l2
	a=binomial(n,m)
	b=binomial(l1+l2,m-l)+ binomial(l1+l,m-l1)+binomial(l+l2,m-l1)
	t=Fraction(a-b,a)
	tu=t.numerator
	kq=tinh_tong_chu_so(tu)
	dap_an= kq
	noi_dung=f"Thầy X có ${{{l+l1+l2}}}$ cuốn sách gồm ${{{l1}}}$ cuốn sách toán, ${{{l2}}}$ cuốn sách lí và ${{{l}}}$ cuốn sách hóa. Các cuốn sách đôi một khác nhau. Thầy X chọn ngẫu nhiên ${{{m}}}$ cuốn sách để làm phần thưởng cho một học sinh. Xác suất để số cuốn sách còn lại của thầy X có đủ 3 môn là $\\dfrac{{a}}{{b}}$, với $a,b \\in \\mathbb{{N}}$ và $(a;b)=1$. Tổng các chữ số của ${{a}}$ là "
	noi_dung_loigiai=(f'Gọi A là biến cố “Số cuốn sách còn lại của thầy X có đủ 3 môn”, suy ra $\\overline{{A}}$ là biến cố “Số cuốn sách còn lại của thầy X không có đủ 3 môn”= “Thầy X đã lấy hết số sách của một môn học”.\n\n'
		f"$n(\\Omega)= C_{{{n}}}^{{{m}}}= {{{a}}}$\n\n "
	f" $n(\\overline{{A}})=C_{{{l1}}}^{{{l1}}} C_{{{l+l2}}}^{{{m-l1}}}  + C_{{{l2}}}^{{{l2}}} C_{{{l1+l}}}^{{{m-l2}}} +  C_{{{l}}}^{{{l}}} C_{{{l1+l2}}}^{{{m-l}}} ={b}  $ \n\n"
	f" $P(\\overline{{A}})= \\dfrac{{n(\\overline{{A}})}}{{n(\\Omega)}}= {phan_so(b/a)} $\n\n"
	f" $P(A)=1-P(\\overline{{A}})= {phan_so(1-(b/a))} $\n\n"
	f" Tổng các chữ số của ${{a}}$ là ${{{dap_an}}}$")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C9_B2_45]-SA-M3. XS các bài toán chọn bi(4 kiểu)
def mjulk_L10_C9_B2_45():
	mau_sac=["màu đỏ", "màu xanh", "màu vàng", "màu trắng", "màu tím", "màu đen"]
	x,d,v=random.sample(mau_sac,3)
	chon =random.randint(1,4)
	if chon ==1:
		n=5
		
		l1=n+random.randint(1,8)
		l=n+random.randint(1,8)
		l2=n+random.randint(1,9)
		n1=l+l1+l2
		a=binomial(n1,5)
		b=binomial(l1,3)*binomial(l2,1)*binomial(l,1)+ binomial(l1,1)*binomial(l2,2)*binomial(l,2)
		t=b/a
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp có ${{{l+l1+l2}}}$ viên bi gồm ${{{l1}}}$ viên bi {x}, ${{{l2}}}$ viên bi {d} và ${{{l}}}$ viên bi {v}. Chọn ngẫu nhiên ${{{n}}}$ viên bi trong hộp. Tính xác suất để ${{{n}}}$ viên bi được chọn có đủ các màu và số bi {d} bằng số bi {v}.(Làm tròn kết quả đến hàng phần trăm)"
		noi_dung_loigiai=(f'Gọi A là biến cố “${{{n}}}$ viên bi được chọn có đủ 3 màu và số bi {d} bằng số bi {v}”.\n\n'
			f"$n(\\Omega)= C_{{{n1}}}^{{5}}= {{{a}}}$\n\n "
		f" TH1: Chọn 1 bi {d}, 1 bi {v}, 3 bi {x} có $C_{{{l1}}}^{{3}}C_{{{l2}}}^{{1}}C_{{{l}}}^{{1}} $ \n\n "
		f"TH2: Chọn 2 bi {d}, 2 bi {v}, 1 bi {x} có $C_{{{l1}}}^{{1}}C_{{{l2}}}^{{2}}C_{{{l}}}^{{2}} $ \n\n"
		f"$n(A)= C_{{{l1}}}^{{3}}C_{{{l2}}}^{{1}}C_{{{l}}}^{{1}}+ C_{{{l1}}}^{{1}}C_{{{l2}}}^{{2}}C_{{{l}}}^{{2}}= {b}$ \n\n"
		f" $P(A)= {phan_so(b/a)} \\approx {dap_an}$"
		)
	if chon ==2:
		n=4
		
		l1=n+random.randint(1,8)
		l=n+random.randint(1,8)
		l2=n+random.randint(1,9)
		n1=l+l1+l2
		a=binomial(n1,5)
		b=binomial(l1,2)*binomial(l2,1)*binomial(l,1)+ binomial(l1,1)*binomial(l2,1)*binomial(l,2)+ binomial(l1,1)*binomial(l2,2)*binomial(l,1)
		t=b/a
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp có ${{{l+l1+l2}}}$ viên bi gồm ${{{l1}}}$ viên bi {x}, ${{{l2}}}$ viên bi {d} và ${{{l}}}$ viên bi {v}. Chọn ngẫu nhiên ${{{n}}}$ viên bi trong hộp. Tính xác suất để ${{{n}}}$ viên bi được chọn có đủ các màu và số bi {d} bằng số bi {v}. (Làm tròn kết quả đến hàng phần trăm) "
		noi_dung_loigiai=(f'Gọi A là biến cố “${{{n}}}$ viên bi được chọn có đủ 3 màu”.\n\n'
			f"$n(\\Omega)= C_{{{n1}}}^{{5}}= {{{a}}}$\n\n "
		f" TH1: Chọn 1 bi {d}, 1 bi {v}, 2 bi {x} có $C_{{{l1}}}^{{2}}C_{{{l2}}}^{{1}}C_{{{l}}}^{{1}} $ \n\n "
		f"TH2: Chọn 2 bi {d}, 1 bi {v}, 1 bi {x} có $C_{{{l1}}}^{{1}}C_{{{l2}}}^{{2}}C_{{{l}}}^{{1}} $ \n\n"
		f"TH3: Chọn 1 bi {d}, 2 bi {v}, 1 bi {x} có $C_{{{l1}}}^{{1}}C_{{{l2}}}^{{1}}C_{{{l}}}^{{2}} $ \n\n"
		f"$n(A)= C_{{{l1}}}^{{2}}C_{{{l2}}}^{{1}}C_{{{l}}}^{{1}}+ C_{{{l1}}}^{{1}}C_{{{l2}}}^{{2}}C_{{{l}}}^{{1}}+C_{{{l1}}}^{{1}}C_{{{l2}}}^{{1}}C_{{{l}}}^{{2}} = {b}$ \n\n"
		f" $P(A)= {phan_so(b/a)} \\approx {dap_an}$"
		)
	if chon ==3:
		n=5

		l1=n+random.randint(1,8)
		l=n+random.randint(1,8)
		l2=n+random.randint(1,9)
		n1=l+l1+l2
		a=binomial(n1,5)
		b=binomial(l1,2)*binomial(l2,2)*binomial(l,1)+ binomial(l1,1)*binomial(l2,3)*binomial(l,1)
		t=b/a
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp có ${{{l+l1+l2}}}$ viên bi gồm ${{{l1}}}$ viên bi {x}, ${{{l2}}}$ viên bi {d} và ${{{l}}}$ viên bi {v}. Chọn ngẫu nhiên ${{{n}}}$ viên bi trong hộp. Tính xác suất để ${{{n}}}$ viên bi được chọn có đủ các màu và số bi {d} nhiều hơn số bi {v}. (Làm tròn kết quả đến hàng phần trăm) "
		noi_dung_loigiai=(f'Gọi A là biến cố “${{{n}}}$ viên bi được chọn có đủ 3 màu và số bi {d} nhiều hơn số bi {v}”.\n\n'
			f"$n(\\Omega)= C_{{{n1}}}^{{5}}= {{{a}}}$\n\n "
		f" TH1: Chọn 2 bi {d}, 1 bi {v}, 2 bi {x} có $C_{{{l1}}}^{{2}}C_{{{l2}}}^{{2}}C_{{{l}}}^{{1}} $ \n\n "
		f"TH2: Chọn 3 bi {d}, 1 bi {v}, 1 bi {x} có $C_{{{l1}}}^{{1}}C_{{{l2}}}^{{3}}C_{{{l}}}^{{1}} $ \n\n"
		f"$n(A)= C_{{{l1}}}^{{2}}C_{{{l2}}}^{{2}}C_{{{l}}}^{{1}}+ C_{{{l1}}}^{{1}}C_{{{l2}}}^{{3}}C_{{{l}}}^{{1}}= {b}$ \n\n"
		f" $P(A)= {phan_so(b/a)} \\approx {dap_an}$"
		)

	if chon ==4:
		n=random.randint(3,6)
		l1=n+random.randint(1,9)
		l=n+random.randint(1,8)
		l2=n+random.randint(1,9)
		n1=l+l1+l2
		a=binomial(n1,n)
		b=binomial(l1+l,n)
		t=1-(b/a)
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp có ${{{l+l1+l2}}}$ viên bi gồm ${{{l1}}}$ viên bi {x}, ${{{l2}}}$ viên bi {d} và ${{{l}}}$ viên bi {v}. Chọn ngẫu nhiên ${{{n}}}$ viên bi trong hộp. Tính xác suất để ${{{n}}}$ viên bi được chọn có ít nhất 1 viên bi {d}. (Làm tròn kết quả đến hàng phần trăm)"
		noi_dung_loigiai=(f'Gọi A là biến cố “${{{n}}}$ viên bi được chọn có ít nhất 1 bi {d}”.\n\n'
			f"$\\overline{{A}}$ không có bi đỏ được chọn\n\n"
			f"$n(\\Omega)= C_{{{n1}}}^{{{n}}}= {{{a}}}$\n\n "
		f"$n(\\overline A)= C_{{{l+l1}}}^{{{n}}}= {b}$ \n\n"
		f" $P(A)= 1- P(\\overline{{A}})= {phan_so(1-(b/a))} \\approx {dap_an}$"
		)
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C9_B2_46]-SA-M3. XS các bài toán chọn người
def mjulk_L10_C9_B2_46():
	a=random.randint(6,10)
	b=random.randint(6,15)
	n=a+b-random.randint(2,7)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	chon=random.randint(1,7)
	if chon ==1:
		a1=binomial(a+b,n)
		b1=binomial(a+b-2,n-2)
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một nhóm gồm ${{{a}}}$ nam và ${{{b}}}$ nữ, trong đó có bạn nam tên {B} và bạn nữ tên {A}. Giáo viên chọn ngẫu nhiên ra ${{{n}}}$ bạn tham gia văn nghệ. Tính xác suất để trong số các bạn được chọn có cả {A} và {B}. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b}}}^{{{n}}}={a1}$\n\n "
		f"$n(A)=C_{{{a+b-2}}}^{{{n-2}}}={b1} $ \n\n"
		f" $P(A)= {phan_so(b1/a1)} \\approx {dap_an}$")
	if chon ==2:
		a1=binomial(a+b,n)
		b1=binomial(a+b-2,n-1)
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một nhóm gồm ${{{a}}}$ nam và ${{{b}}}$ nữ, trong đó có bạn nam tên {B} và bạn nữ tên {A}. Giáo viên chọn ngẫu nhiên ra ${{{n}}}$ bạn tham gia văn nghệ. Tính xác suất để trong số các bạn được chọn có {A} nhưng không có {B}. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b}}}^{{{n}}}={a1}$\n\n "
		f"$n(A)=C_{{{a+b-2}}}^{{{n-1}}}={b1} $ \n\n"
		f" $P(A)= {phan_so(b1/a1)} \\approx {dap_an}$")
	if chon ==3:
		a1=binomial(a+b,n)
		b2=binomial(a+b-2,n-1)
		b3=binomial(a+b-2,n)
		b1=b2+b2+b3
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một nhóm gồm ${{{a}}}$ nam và ${{{b}}}$ nữ, trong đó có bạn nam tên {B} và bạn nữ tên {A}. Giáo viên chọn ngẫu nhiên ra ${{{n}}}$ bạn tham gia văn nghệ. Tính xác suất để trong số các bạn được chọn {A} và {B} không đồng thời cùng có mặt. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b}}}^{{{n}}}={a1}$\n\n "
			f" TH1: Chọn {A} nhưng không chọn {B} là $C_{{{a+b-2}}}^{{{n-1}}}={b2} $\n\n"
			f"TH2: Chọn {B} nhưng không chọn {A} là $C_{{{a+b-2}}}^{{{n-1}}}={b2} $\n\n"
			f"TH3: Không chọn cả {A} và {B} là $C_{{{a+b-2}}}^{{{n}}}={b3} $\n\n"
			f"$n(A)= {b2}+{b2}+{b3}={b1}$\n\n"
			f"$P(A)= {phan_so(b1/a1)} \\approx {dap_an}$"

)
	if chon ==4:
		m1=random.randint(3,5)
		b=m1+random.randint(2,6)
		n=m1+random.randint(2,4)
		a1=binomial(a+b,n)

		b1=binomial(b-1, m1-1)*binomial(a-1,n-m1)
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một nhóm gồm ${{{a}}}$ nam và ${{{b}}}$ nữ, trong đó có bạn nam tên {B} và bạn nữ tên {A}. Giáo viên chọn ngẫu nhiên ra ${{{n}}}$ bạn tham gia văn nghệ. Tính xác suất để chọn được ${{{m1}}}$ bạn nữ trong đó có {A} và {B} không được chọn. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b}}}^{{{n}}}={a1}$\n\n "
			f"$n(A)= C_{{{b-1}}}^{{{m1-1}}} C_{{{a-1}}}^{{{n-m1}}} = {b1}$\n\n"
			f"$P(A)= {phan_so(b1/a1)} \\approx {dap_an}$")
	if chon ==5:
		m1=random.randint(3,5)
		b=m1+random.randint(2,6)
		n=m1+random.randint(2,4)
		a1=binomial(a+b,n)

		b1=binomial(b-1, m1)*binomial(a-1,n-m1)
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một nhóm gồm ${{{a}}}$ nam và ${{{b}}}$ nữ, trong đó có bạn nam tên {B} và bạn nữ tên {A}. Giáo viên chọn ngẫu nhiên ra ${{{n}}}$ bạn tham gia văn nghệ. Tính xác suất để chọn được ${{{m1}}}$ bạn nữ trong đó {A} và {B} không được chọn. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b}}}^{{{n}}}={a1}$\n\n "
			f"$n(A)= C_{{{b-1}}}^{{{m1}}} C_{{{a-1}}}^{{{n-m1}}} = {b1}$\n\n"
			f"$P(A)= {phan_so(b1/a1)} \\approx {dap_an}$")
	if chon ==6:
		n=3
		a1=binomial(a+b,n)
		b1=binomial(a, 1)*binomial(b,2)+binomial(a,3)
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một nhóm gồm ${{{a}}}$ nam và ${{{b}}}$ nữ. Giáo viên chọn ngẫu nhiên ra ${{{n}}}$ bạn tham gia văn nghệ. Tính xác suất để chọn được nam nhiều hơn nữ. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b}}}^{{{n}}}={a1}$\n\n "
			f"$n(A)= C_{{{a}}}^{{1}} C_{{{b}}}^{{2}}+ C_{{{a}}}^{{3}}= {b1}$\n\n"
			f"$P(A)= {phan_so(b1/a1)} \\approx {dap_an}$")

	if chon ==7:
		n=4
		a1=binomial(a+b,n)
		b1=binomial(a, 1)*binomial(b,3)+binomial(b,4)
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một nhóm gồm ${{{a}}}$ nam và ${{{b}}}$ nữ. Giáo viên chọn ngẫu nhiên ra ${{{n}}}$ bạn tham gia văn nghệ. Tính xác suất để chọn được không quá một nam. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b}}}^{{{n}}}={a1}$\n\n "
			f"$n(A)= C_{{{a}}}^{{1}} C_{{{b}}}^{{3}}+ C_{{{b}}}^{{4}}= {b1}$\n\n"
			f"$P(A)= {phan_so(b1/a1)} \\approx {dap_an}$")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an







#[D10_C9_B2_47]-SA-M3. XS tổng các số trên các viên bi được chọn là số chia hết cho 3
def mjulk_L10_C9_B2_47(): 
	n=random.randint(20,50)
	l1=len([i for i in range(1, n + 1) if i % 3 == 1])
	l=len([i for i in range(1, n + 1) if i % 3== 0])
	l2=len([i for i in range(1, n + 1) if i % 3 == 2])
	
	chon=random.randint(1,2)
	if chon ==1:
		a=binomial(n,3)
		b=binomial(l1,3)+ binomial(l1,1)*binomial(l2,1)*binomial(l,1)+binomial(l2,3)+binomial(l,3)
		t=b/a
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp chứa ${{{n}}}$ viên bi được đánh số từ ${{1}}$ đến ${{{n}}}$. Chọn ngẫu nhiên ${{3}}$ viên bi từ hộp. Tính xác suất để tổng các số trên các viên bi được chọn là số chia hết cho ${{3}}$. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{n}}}^{{3}}= {{{a}}}$\n\n "
		f" TH1: Lấy được 3 bi ghi số chia 3 dư 1 là $ C_{{{l1}}}^{{3}}$ \n\n"
		f" TH2: Lấy được 3 bi ghi số chia hết cho 3 là $ C_{{{l}}}^{{3}}$ \n\n"
		f" TH3: Lấy được 1 bi ghi số chia hết cho 3, 1 bi ghi số chia 3 dư 1, 1 bi ghi số chia 3 dư 2 là $ C_{{{l1}}}^{{1}}  C_{{{l}}}^{{1}}  C_{{{l2}}}^{{1}}$ \n\n"
		f" TH4: Lấy được 3 bi ghi số chia 3 dư 2 là $ C_{{{l2}}}^{{3}}$"
		f" $n(A)=C_{{{l1}}}^{{3}}+ C_{{{l}}}^{{3}}+C_{{{l1}}}^{{1}}  C_{{{l}}}^{{1}}  C_{{{l2}}}^{{1}}+  C_{{{l2}}}^{{3}} ={b}  $ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}= {phan_so(b/a)} \\approx {dap_an} $")
	if chon ==2:
		a=binomial(n,2)
		b=binomial(l1,1)*binomial(l2,1)+binomial(l,2)
		t=b/a
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp chứa ${{{n}}}$ viên bi được đánh số từ ${{1}}$ đến ${{{n}}}$. Chọn ngẫu nhiên ${{2}}$ viên bi từ hộp. Tính xác suất để tổng các số trên các viên bi được chọn là số chia hết cho ${{3}}$. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{n}}}^{{2}}= {{{a}}}$\n\n "
		f" TH1: Lấy được 1 bi ghi số chia 3 dư 1 và 1 bi ghi số chia 3 dư 2 là $ C_{{{l1}}}^{{1}} C_{{{l2}}}^{{1}}$ \n\n"
		f" TH2: Lấy được 2 bi ghi số chia hết cho 3 là $ C_{{{l}}}^{{2}}$ \n\n"
		
		f" $n(A)=C_{{{l1}}}^{{1}} C_{{{l2}}}^{{1}}+ C_{{{l}}}^{{2}}={b}  $ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}= {phan_so(b/a)} \\approx {dap_an} $")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C9_B2_48]-SA-M3. XS các bài toán chọn sản phẩm tốt, xấu
def mjulk_L10_C9_B2_48():

	a=random.randint(50,80)
	n=random.randint(2,6)
	m=random.randint(10,20)

	a1=binomial(a,m)
	b1=binomial(a-n,m)+binomial(a-n,m-1)*binomial(n,1)+binomial(n,2)*binomial(a-n,m-2)
	t=b1/a1
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=f"Một lô hàng gồm ${{{a}}}$ sản phẩm trong đó có ${{{n}}}$ phế phẩm. Người ta kiểm tra ngẫu nhiên ${{{m}}}$ sản phẩm. Tính xác suất để trong số các sản phẩm được kiểm tra có không quá ${{2}}$ phế phẩm. (Kết quả làm tròn đến hàng phần trăm)"
	noi_dung_loigiai=(f"$n(\\Omega)=C_{{{a}}}^{{{m}}}$\n\n "
	f" $n(A)= C_{{{a-n}}}^{{{m}}} +C_{{{n}}}^{{{1}}}  C_{{{a-n}}}^{{{m-1}}} + C_{{{n}}}^{{{2}}}C_{{{a-n}}}^{{{m-2}}}$ \n\n"
	f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}} \\approx {dap_an} $")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C9_B2_49]-SA-M3. XS bài toán chọn cầu 2 lần
def mjulk_L10_C9_B2_49():
	chon=random.randint(1,2)
	a=random.randint(5,25)
	b=random.choice([i for i in range(5,20) if i!=a])
	mau_sac=["màu đỏ", "màu xanh", "màu vàng", "màu trắng", "màu tím", "màu đen"]
	x,d=random.sample(mau_sac,2)

	chon =random.randint(1,2)
	if chon ==1:
		a1=(a+b)*(a+b-1)
		b1=a*(a-1)+b*(b-1)
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp đựng ${{{a}}}$ quả cầu {x} và ${{{b}}}$ quả cầu {d}. Lấy ngẫu nhiên lần thứ nhất 1 quả cầu trong hộp không hoàn lại, tiếp tục lấy ngẫu nhiên 1 quả cầu lần thứ hai. Tính xác suất để lấy được 2 quả cầu cùng màu. (Kết quả làm tròn đến hàng phần trăm) "
		noi_dung_loigiai=(f"$n(\\Omega)=C_{{{a+b}}}^{{{1}}}C_{{{a+b-1}}}^{{{1}}} = {a1}$\n\n "
		f" $n(A)= C_{{{a}}}^{{{1}}} C_{{{a-1}}}^{{{1}}}+C_{{{b}}}^{{{1}}} C_{{{b-1}}}^{{{1}}} ={b1}$ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}= {phan_so(b1/a1)} \\approx {dap_an} $")
	if chon ==2:
		a1=(a+b)*(a+b-1)
		b1=a*b*2
		t=b1/a1
		kq="{:.2f}".format(t).replace(".", ",")
		dap_an= kq
		noi_dung=f"Một hộp đựng ${{{a}}}$ quả cầu {x} và ${{{b}}}$ quả cầu {d}. Lấy ngẫu nhiên lần thứ nhất 1 quả cầu trong hộp không hoàn lại, tiếp tục lấy ngẫu nhiên 1 quả cầu lần thứ hai. Tính xác suất để lấy được 2 quả cầu khác màu. (Kết quả làm tròn đến hàng phần trăm)"
		noi_dung_loigiai=(f"$n(\\Omega)=C_{{{a+b}}}^{{{1}}}C_{{{a+b-1}}}^{{{1}}} = {a1}$\n\n "
		f" $n(A)= C_{{{a}}}^{{{1}}} C_{{{b}}}^{{{1}}}+C_{{{b}}}^{{{1}}} C_{{{a}}}^{{{1}}} ={b1}$ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}= {phan_so(b1/a1)} \\approx {dap_an} $")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an










#[D10_C9_B2_50]-SA-M3. XS bài toán chọn ngẫu nhiên số nhỏ hơn số m
def mjulk_L10_C9_B2_50():
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
	b1 = [so for so in so_hoan_vi if so < m]
	b1=len(b1)
	a1=len(so_hoan_vi)
	t=b1/a1
	# Bước 5: Đếm số lượng các số thỏa mãn
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq

	noi_dung=f" Gọi S là tập hợp các số tự nhiên có bốn chữ số đôi một khác nhau được tạo thành từ các chữ số $\\{{ {nhom1} \\}}$. Lấy ngẫu nhiên một số từ tập S, tính xác suất để lấy được số nhỏ hơn ${{{m}}}$. (Kết quả làm tròn đến hàng phần trăm)  "
	noi_dung_loigiai=(f" $n(\\Omega)={{{a1}}}$ \n\n"
	f" $n(A)={{{b1}}}$ \n\n"
	f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}= {phan_so(b1/a1)} \\approx {dap_an} $")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an








#[D10_C9_B2_51]-TF-M3. XS các bài toán xếp m nam, m nữ hàng dọc. Xét tính ĐS
def mjulk_L10_C9_B2_51():
	a1=random.randint(5,10)
	a2=a1 
	kqm=factorial(a1+a2)
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	doc=random.choice(["ngang", "dọc"])

	noi_dung = f"Xếp ngẫu nhiên ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} bạn nữ tên {A} thành một hàng {doc}. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"

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
		kq1_T=f"*Xác suất {A} đứng {dau} và {B} đứng {cuoi} là $\\dfrac{{{a1+a2-2}!}}{{{a1+a2}!}}$" 
		kq1_F=f"Xác suất {A} đứng {dau} và {B} đứng {cuoi} là $\\dfrac{{{a1+a2-1}!}}{{{a1+a2}!}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=(f"Có $n(A)={{{a1+a2-2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} đứng {dau} và {B} đứng {cuoi}\n\n"
		f" $n(\\Omega)={{{a1+a2}!}} $ \n\n"
		f" $P(A)= \\dfrac{{{a1+a2-2}!}}{{{a1+a2}!}}$")
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon =random.randint(1,2)
	if chon ==1:

		kq2_T=f"*Xác suất xếp được nam nữ xen kẽ là $\\dfrac{{2 \\cdot {a1}!{a2}!}}{{{a1+a2}!}}$ "
		kq2_F=f"Xác suất xếp được nam nữ xen kẽ là $\\dfrac{{{a1}!{a2}!}}{{{a1+a2}!}}$  "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"Có ${{2 \\cdot {a1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho nam nữ xen kẽ \n\n"
		f"Xác suất xếp được nam nữ xen kẽ là $\\dfrac{{2 \\cdot {a1}!{a2}!}}{{{a1+a2}!}}$ ")
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon ==2:
		nữ=random.choice(["nữ", "nam"])

		kq2_T=f"*Xác suất xếp các bạn {nữ} luôn đứng cạnh nhau là $\\dfrac{{ {a1+1}!{a2}!}}{{{a1+a2}!}}$"
		kq2_F=f"Xác suất xếp các bạn {nữ} luôn đứng cạnh nhau là $\\dfrac{{ {a1}!{a2}!}}{{{a1+a2}!}}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"Có ${{ {a1+1}!{a2}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho các bạn {nữ} luôn đứng cạnh nhau \n\n"
		f"Xác suất xếp các bạn {nữ} luôn đứng cạnh nhau là $\\dfrac{{ {a1+1}!{a2}!}}{{{a1+a2}!}}$")
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon ==1:
		kq3_T=f"*Xác suất xếp {A} và {B} luôn đứng cạnh nhau là $\\dfrac{{2\\cdot {a1+a2-1}!}}{{{a1+a2}!}}$" 
		kq3_F=f"Xác suất xếp {A} và {B} luôn đứng cạnh nhau là $\\dfrac{{{a1+a2-1}!}}{{{a1+a2}!}}$ "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=(f"Có ${{2\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} luôn đứng cạnh nhau\n\n "
		f"Xác suất xếp {A} và {B} luôn đứng cạnh nhau là $\\dfrac{{2\\cdot {a1+a2-1}!}}{{{a1+a2}!}}$")

		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	if chon ==2:
		kq3_T=f"*Xác xuất để {A} và {B} không đứng cạnh nhau là $\\dfrac{{{a1+a2}!-2\\cdot {a1+a2-1}!}}{{{a1+a2}!}}$" 
		kq3_F=f"Xác xuất để {A} và {B} không đứng cạnh nhau là $\\dfrac{{2\\cdot {a1+a2-1}!}}{{{a1+a2}!}}$  "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=(f"Có ${{{a1+a2}!-2\\cdot {a1+a2-1}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} và {B} không đứng cạnh nhau \n\n"
		f"Xác xuất để {A} và {B} không đứng cạnh nhau là $\\dfrac{{{a1+a2}!-2\\cdot {a1+a2-1}!}}{{{a1+a2}!}}$")
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	chon=random.randint(1,2)
	if chon ==1:

		kq4_T=f"*Xác suất để {A} luôn đứng giữa hai bạn nam là $\\dfrac{{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-3}!}}{{{a1+a2}!}}$"
		kq4_F=f"Xác suất để {A} luôn đứng giữa hai bạn nam là $\\dfrac{{{(a1+a2-1)*(a1-1)*a1}\\cdot {a1+a2-3}!}}{{{a1+a2}!}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Có ${{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-3}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nam \n\n"
		f"Xác suất để {A} luôn đứng giữa hai bạn nam là $\\dfrac{{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-3}!}}{{{a1+a2}!}}$")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon ==2:

		kq4_T=f"*Xác suất xếp {A} luôn đứng giữa hai bạn nữ là $\\dfrac{{{(a1+a2-2)*(a1-1)*(a1-2)}\\cdot {a1+a2-3}!}}{{{a1+a2}!}}$"
		kq4_F=f"Xác suất xếp {A} luôn đứng giữa hai bạn nữ là $\\dfrac{{{(a1+a2-2)*(a1-1)*a1}\\cdot {a1+a2-3}!}}{{{a1+a2}!}}$ " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Có ${{{(a1+a2-2)*(a1-1)*(a1-2)}\\cdot {a1+a2-3}!}}$ cách xếp các bạn trên thành một hàng {doc} sao cho {A} luôn đứng giữa hai bạn nữ \n\n"
		f"Xác suất xếp {A} luôn đứng giữa hai bạn nữ là $\\dfrac{{{(a1+a2-2)*(a1-1)*(a1-2)}\\cdot {a1+a2-3}!}}{{{a1+a2}!}}$")
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




#[D10_C9_B2_52]-SA-M3. XS bài toán xếp m nam, m nữ hàng dọc(nhiều kiểu)
def mjulk_L10_C9_B2_52():
	a1=random.randint(5,10)
	a2=a1 

	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	doc=random.choice(["ngang", "dọc"])
	vt=["đầu", "cuối"]
	dau, cuoi =random.sample(vt,2)
	chon =random.randint(1,5)
	if chon ==1:
		a=factorial(a1+a2)
		b=factorial(a1+a2-2)	
		ucln=math.gcd(abs(a),abs(b))
		a,b=int(a/ucln),int(b/ucln)
		# Bước 5: Đếm số lượng các số thỏa mãn
		kq=a+b
		dap_an= kq

		noi_dung=f"Xếp ngẫu nhiên ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} bạn nữ tên {A} thành một hàng {doc}. Xác suất {A} đứng {dau} và {B} đứng {cuoi} là $\\dfrac{{a}}{{b}}$ với $(a; b)=1$ và $a;b \\in \\mathbb {{N}}$. Tính ${{a+b}}$"
		noi_dung_loigiai=(f" $n(\\Omega)={{{a1+a2}!}}$ \n\n"
		f" $n(A)={{{a1+a2-2}!}}$ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}=\\dfrac{{{a1+a2-2}!}}{{{a1+a2}!}}= {phan_so(b/a)}$ \n\n"
		f" Vậy ${{a+b}}={dap_an}$")


	if chon ==2:
		m=random.randint(4,8)
		a=factorial(2*m)
		b=factorial(m)*factorial(m)*2
		ucln=math.gcd(abs(a),abs(b))
		a,b=int(a/ucln),int(b/ucln)
		# Bước 5: Đếm số lượng các số thỏa mãn
		kq=a+b
		dap_an= kq
		noi_dung=f"Xếp ngẫu nhiên ${{{m}}}$ bạn nam và ${{{m}}}$ bạn nữ thành một hàng {doc}. Xác suất để nam nữ xếp xen kẽ là $\\dfrac{{a}}{{b}}$ với $(a; b)=1$ và $a;b \\in \\mathbb {{N}}$. Tính ${{a+b}}$"
		noi_dung_loigiai=(f" $n(\\Omega)={{{m+m}!}}$ \n\n"
		f" $n(A)={{2 \\cdot {m}!{m}!}}$ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}=\\dfrac{{2 \\cdot {m}!{m}!}}{{{m+m}!}}= {phan_so(b/a)}$ \n\n"
		f" Vậy ${{a+b}}={dap_an}$")


	if chon ==3:
		m=random.randint(5,8)
		n=random.choice([i for i in range(5,9)])
		a=factorial(2*m)
		b=factorial(m)*factorial(m)*2
		ucln=math.gcd(abs(a),abs(b))
		a,b=int(a/ucln),int(b/ucln)
		# Bước 5: Đếm số lượng các số thỏa mãn
		kq=a+b
		dap_an= kq
		noi_dung=f"Xếp ngẫu nhiên ${{{m}}}$ bạn nam và ${{{n}}}$ bạn nữ thành một hàng {doc}. Xác suất để các bạn nữ luôn đứng cạnh nhau là $\\dfrac{{a}}{{b}}$ với $(a; b)=1$ và $a;b \\in \\mathbb {{N}}$. Tính ${{a+b}}$"
		noi_dung_loigiai=(f" $n(\\Omega)={{{m+n}!}}$ \n\n"
		f" $n(A)={{ {n}!{m+1}!}}$ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}=\\dfrac{{{n}!{m+1}!}}{{{m+n}!}}= {phan_so(b/a)}$ \n\n"
		f" Vậy ${{a+b}}={dap_an}$")


	if chon ==4:
		a=factorial(a1+a2)
		b=factorial(a1+a2-1)*2
		
		ucln=math.gcd(abs(a),abs(b))
		a,b=int(a/ucln),int(b/ucln)
		# Bước 5: Đếm số lượng các số thỏa mãn
		kq=a+b
		dap_an= kq

		noi_dung=f"Xếp ngẫu nhiên ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} bạn nữ tên {A} thành một hàng {doc}. Xác suất để {A} và {B} luôn đứng cạnh nhau là $\\dfrac{{a}}{{b}}$ với $(a; b)=1$ và $a;b \\in \\mathbb {{N}}$. Tính ${{a+b}}$"
		noi_dung_loigiai=(f" $n(\\Omega)={{{a1+a2}!}}$ \n\n"
		f" $n(A)={{2 \\cdot {a1+a2-1}!}}$ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}=\\dfrac{{2 \\cdot {a1+a2-1}!}}{{{a1+a2}!}}= {phan_so(b/a)}$ \n\n"
		f" Vậy ${{a+b}}={dap_an}$")

	if chon ==5:
		a=factorial(a1+a2)
		b=factorial(a1+a2-1)*2
		
		ucln=math.gcd(abs(a-b),abs(a))
		a1,b1=int((a-b)/ucln),int(a/ucln)
		# Bước 5: Đếm số lượng các số thỏa mãn
		kq=a1+b1
		dap_an= kq

		noi_dung=f"Xếp ngẫu nhiên ${{{a1}}}$ bạn nam và ${{{a2}}}$ bạn nữ trong đó có bạn nam tên {B} bạn nữ tên {A} thành một hàng {doc}. Xác suất để {A} và {B} không đứng cạnh nhau là $\\dfrac{{a}}{{b}}$ với $(a; b)=1$ và $a;b \\in \\mathbb {{N}}$. Tính ${{a+b}}$"
		noi_dung_loigiai=(f" $n(\\Omega)={{{a1+a2}!}}$ \n\n"
			f" Gọi A là biến cố {A} và {B} đứng cạnh nhau \n\n"
		f" $n(A)={{2 \\cdot {a1+a2-1}!}}$ \n\n"
		f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}}=\\dfrac{{2 \\cdot {a1+a2-1}!}}{{{a1+a2}!}}= {phan_so(b/a)}$ \n\n"
		f"$P(\\overline A)= 1- P(A)= {phan_so(1-(b/a))}$ \n\n"
		f" Vậy ${{a+b}}={dap_an}$")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an


#[D10_C9_B2_53]-SA-M3. Có m khách bước vào cửa hàng n quầy. XS đễn a người cùng vào 1 quầy
def mjulk_L10_C9_B2_53():
	n=random.randint(2,5)
	m=n+random.randint(2,6)
	e=random.randint(3,5)
	thutu=random.choice([i for i in range(1,e)])
	a=binomial(m,n)*(e-1)**(m-n)
	b=e**m
	t=a/b
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=f" Có ${{{m}}}$ người khách bước ngẫu nhiên và một cửa hàng có ${{{e}}}$ quầy. Tính xác suất để ${{{n}}}$ người cùng chọn quầy thứ ${{{thutu}}}$. "
	noi_dung_loigiai=(f"$n(\\Omega)={e}^{{{m}}} $ \n\n"
	f"$n(A)= C_{{{m}}}^{{{n}}} {e-1}^{{{m-n}}} $ \n\n"
	f"$P(A)=\\dfrac{{n(A)}}{{n(\\Omega)}}= {phan_so(a/b)} \\approx {kq}$")
	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C9_B2_54]-SA-M3. Có m cặp nam nữ trong đó có n cặp vc. XS chọn 3 người k có cặp vc
def mjulk_L10_C9_B2_54():
	n=random.randint(2,5)
	m=n+random.randint(2,6)

	a=n*(2*m-2)
	b=binomial(2*m,3)
	t=1-(a/b)
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=f" Trong một buổi liên hoan có ${{{m}}}$ cặp nam nữ trong đó có ${{{n}}}$ cặp vợ chồng. Chọn ngẫu nhiên ${{3}}$ người biểu diễn một tiết mục văn nghệ. Tính xác suất để ${{3}}$ người được chọn không có cặp vợ chồng nào. (Kết quả làm tròn đến hàng phần trăm) "
	noi_dung_loigiai=(f"$n(\\Omega)=C_{{{2*m}}}^{{3}} $ \n\n"
		f" Gọi ${{A}}$ là biến cố không có cặp vợ chồng nào trong ${{3}}$ người được chọn \n\n"
		f"$\\overline{{A}}$ là biến cố trong ${{3}}$ người được chọn có một cặp vợ chồng \n\n"
		f" $n(\\overline{{A}})= C_{{{n}}}^{{1}} \\cdot C_{{{2*m-2}}}^{{1}} $\n\n"
	f"$P(A)=1-P(\\overline{{A}})=1- \\dfrac{{n(\\overline {{A}})}}{{n(\\Omega)}}= {phan_so(1-(a/b))} \\approx {kq}$")
	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an








#[D10_C9_B2_55]-SA-M3. Có m đôi giày. XS chọn 4 chiếc trong đó có ít nhất 1 đôi
def mjulk_L10_C9_B2_55():
	
	m=random.randint(7,16)
	a=m*binomial(2*m-2,2)- binomial(m,4)
	b=binomial(2*m,4)
	t=1-(a/b)
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=f"Một người có ${{{m}}}$ đôi giày khác nhau và trong lúc đi du lịch vội vã lấy ngẫu nhiên ${{4}}$ chiếc. Tính xác suất để trong ${{4}}$ chiếc giày lấy ra có ít nhất một đôi. (Kết quả làm tròn đến hàng phần trăm) "
	noi_dung_loigiai=(f"$n(\\Omega)=C_{{{2*m}}}^{{4}} $ \n\n"
		f" Gọi ${{A}}$ là biến cố trong ${{4}}$ chiếc giày lấy ra có ít nhất một đôi \n\n"
		f" $n({{A}})= C_{{{m}}}^{{1}} \\cdot  C_{{{2*m-2}}}^{{2}} -C_{{{m}}}^{{2}} $\n\n"
	f"$P(A)= \\dfrac{{n({{A}})}}{{n(\\Omega)}}= {phan_so(a/b)} \\approx {kq}$")
	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C9_B2_56]-SA-M3. Xs chọn 2 điểm tạo ra đt cắt 2 trục toạ độ
def mjulk_L10_C9_B2_56():
	a=random.randint(2,8)
	b= random.randint(2,10)
	c=random.randint(2,10)
	d=random.randint(2,8)
	a1=a*c+b*d
	b1=binomial(a+b+c+d,2)
	t=(a1/b1)
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=f"Trong mặt phẳng toạ độ Oxy, vẽ ${{{a}}}$ điểm ở trong góc phần thứ nhất, ${{{b}}}$ điểm ở trong góc phần thứ hai, ${{{c}}}$ điểm ở trong góc phần thứ ba, ${{{d}}}$ điểm ở trong góc phần thứ tư. Chọn hai điểm bất kì trong các điểm trên, tính xác suất để đoạn thẳng nối hai điểm đó cắt hai trục toạ độ. (Kết quả làm tròn đến hàng phần trăm)"
	noi_dung_loigiai=(f"$n(\\Omega)= C_{{{a+b+c+d}}}^{{2}}$ \n\n  "
	f"$n(A)= C_{{{a}}}^{{1}}  C_{{{c}}}^{{1}} +  C_{{{b}}}^{{1}}  C_{{{d}}}^{{1}}$ \n\n"
	f"$P(A)= \\dfrac{{n({{A}})}}{{n(\\Omega)}}= {phan_so(a1/b1)} \\approx {kq}$")


	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	



#[D10_C9_B2_57]-SA-M3. Có a phiếu trong đó có b phiếu trúng thưởng, m người rút. XS để A trúng thưởng
def mjulk_L10_C9_B2_57():
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	n=random.randint(2,5)
	b= random.randint(5,10)
	a=b+n+random.randint(10,20)
	d=random.randint(2,8)
	a1=n* chinh_hop(b-1,a-n)
	b1=chinh_hop(b,a)
	t=(a1/b1)
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=f"Một hộp có ${{{a}}}$ phiếu bốc thăm khác nhau trong đó có ${{{n}}}$ mã phiếu trúng thưởng. Có ${{{b}}}$ người tham gia bốc thăm trong đó có {A}, mỗi người chỉ được bốc một phiếu. Tính xác suất để chỉ có mỗi {A} rút được phiếu trúng thưởng. (Kết quả làm tròn đến hàng phần trăm)"
	noi_dung_loigiai=  (f"$ n(\\Omega)= A_{{{a}}}^{{{b}}}$ \n\n  "
	f"$n(A)=  {n} \\cdot A_{{{a-n}}}^{{{b-1}}} $ \n\n"
	f"$P(A)= \\dfrac{{n({{A}})}}{{n(\\Omega)}}= {phan_so(a1/b1)} \\approx {kq}$")

	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	


#[D10_C9_B2_58]-SA-M3. Tính xs chọn được k số có tổng bình phương chia hết cho 4
def mjulk_L10_C9_B2_58():
	a=random.randint(1,30)
	n=random.randint(20,30)
	k=random.choice([2,3])
	chan=len([i for i in range(a, a + n) if i %2==0])
	a1=binomial(chan,k)
	b1=binomial(n,k)
	t=(a1/b1)
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=f"Gọi S là tập hợp các số tự nhiên liên tiếp từ ${{{a}}}$ đến ${{{a+n-1}}}$. Chọn ngẫu nhiên ${{{k}}}$ số tự nhiên bất kì từ tập hợp S. Tính xác suất để tổng bình phương của ${{{k}}}$ số đó chia hết cho ${{4}}$. Kết quả làm tròn đến hàng phần trăm."
	noi_dung_loigiai=(f" $n(\\Omega)= C_{{{n}}}^{{{k}}}$ \n\n "
	f'A:" Tổng bình phương của ${{{k}}}$ số đó chia hết cho ${{4}}$ \n\n'
	f'A" Chọn được ${{{k}}}$ số chẵn" suy ra $n(A)= C_{{{chan}}}^{{{k}}}$ \n\n'
	f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}} \\approx {kq}$" )
	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	



#[D10_C9_B2_59]-SA-M4. Bài toán về chọn số của 2 bạn, ai chọn dc số lơn hơn thì thắng 
def mjulk_L10_C9_B2_59():
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	m=random.randint(5,7)
	n=0
	if m ==5 : n =m+random.randint(1,4)
	if m ==6 : n =m+random.randint(1,3)
	if m ==7 : n =m+random.randint(1,2)
	k=random.choice([2,3,4])
	kgm=binomial(n,k)*binomial(m,k)
	nA= binomial(m,k)*(binomial(n,k)- binomial(m,k))+binomial(m,k)*(binomial(m,k)-1)/2
	t=(nA/kgm)
	kq="{:.2f}".format(t).replace(".", ",")
	dap_an= kq
	noi_dung=(f"Bạn {A} có ${{{n}}}$ viên bi được đánh số từ ${{1}}$ đến ${{{n}}}$, bạn {B} có ${{{m}}}$ viên bi được đánh số từ ${{1}}$ đến ${{{m}}}$. Hai bạn cùng chơi một trò chơi bằng cách mỗi bạn rút ra ${{{k}}}$ viên bi và ghép lại theo thứ tự giảm dần để được số tự nhiên có ${{{k}}}$ chữ số. "
	f"Người thắng cuộc là người có số lớn hơn. Hỏi xác suất để bạn {A} thắng bạn {B} là bao nhiêu? (Làm tròn kết quả đến hàng phần trăm) ")
	noi_dung_loigiai=(f" $n(\\Omega)= C_{{{n}}}^{{{k}}}.C_{{{m}}}^{{{k}}} ={kgm} $ \n\n "
	f'A: "Bạn {A} thắng bạn {B} " \n\n'
	f" Trong tập hợp các số của {A} có $C_{{{n}}}^{{{k}}} - C_{{{m}}}^{{{k}}} ={binomial(n,k)-binomial(m,k)}$ số có chữ số đứng đầu lớn hơn ${{{m}}}$ và các số này đều lớn hơn bất cứ số nào mà {B} tạo ra \n\n"
	f"Tập các số của {B} có tất cả $C_{{{m}}}^{{{k}}}={binomial(m,k)}$ số và ta sẽ sắp xếp chúng theo thứ tự tăng dần như vậy nếu {B} tạo được số x nào đó mà số đó đứng ở vị trí thứ k khi sắp xếp thứ tự thì {A} có $C_{{{m}}}^{{{k}}}-k= {binomial(m,k)}-k$ số lớn hơn số x mà các chữ số được tạo từ ${{1}}$ đến ${{{m}}}$ \n\n   "
	f'Vậy $n(A)= C_{{{m}}}^{{{k}}} . ( C_{{{n}}}^{{{k}}} - C_{{{m}}}^{{{k}}}  ) +  (1+2+3+...+{binomial(m,k)-1}) ={nA} $    \n\n'
	f" $P(A)= \\dfrac{{n(A)}}{{n(\\Omega)}} \\approx {kq}$" )
	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	

#[D10_C9_B2_60]-SA-M4. Bài toán về chia phần thưởng. Xs 2 bạn nhận thưởng giống nhau
def mjulk_L10_C9_B2_60():
	A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
	B=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường"])
	x=random.randint(3,25)
	y=random.randint(3,20)
	z=random.randint(3,20)
	t=x+y+z
	kgm=binomial(t,x)*binomial(y+z,y)
	nA= binomial(t-2,y-2)*binomial(x+z,x)+ binomial(t-2,x-2)*binomial(y+z,y)+binomial(t-2,z-2)*binomial(y+x,y)
	t1=(nA/kgm)
	kq="{:.2f}".format(t1).replace(".", ",")
	dap_an= kq
	noi_dung=(f"Người ta dùng ${{{2*t}}}$ cuốn sách bao gồm ${{{x+y}}}$ cuốn Toán, ${{{x+z}}}$ cuốn Hoá, ${{{z+y}}}$ cuốn Lí( các cuốn sách cùng loại thì giống nhau) để làm phần thưởng cho ${{{phan_so(t)}}}$ học sinh. (Làm tròn kết quả đến hàng phần trăm) "
	f"(trong đó có hai học sinh {A} và {B}) mỗi học sinh nhận được hai cuốn sách khác thể loại (không tính thứ tự các cuốn sách ). Tính xác suất để hai học sinh {A} và {B } nhận thưởng giống nhau.")
	noi_dung_loigiai=(f"$n(\\Omega)= C_{{{t}}}^{{{x}}}.C_{{{y+z}}}^{{{y}}} .C_{{{z}}}^{{{z}}} $ \n\n "
	f"Gọi ${{x,y,z}}$ là số học sinh nhận được bộ Toán và Hoá, Toán và Lí, Hoá + Lí \n\n"
	f" Ta có $x+y={x+y}; x+z={x+z} ; z+y={z+y} $ suy ra $x={x}; y={y}; z={z}$ \n\n"
	f" TH1: {A} và {B} cùng nhận bộ Toán + lí là $C_{{{t-2}}}^{{{y-2}}}.C_{{{x+z}}}^{{{x}}}  $ \n\n "
	f" TH2: {A} và {B} cùng nhận bộ Toán +Hoá là $C_{{{t-2}}}^{{{x-2}}}.C_{{{y+z}}}^{{{y}}}  $ \n\n "
	f" TH3: {A} và {B} cùng nhận bộ Lí +Hoá là $C_{{{t-2}}}^{{{z-2}}}.C_{{{y+x}}}^{{{y}}}  $ \n\n "
	f" $n(A)= C_{{{t-2}}}^{{{y-2}}}.C_{{{x+z}}}^{{{x}}}  + C_{{{t-2}}}^{{{x-2}}}.C_{{{y+z}}}^{{{y}}}+ C_{{{t-2}}}^{{{z-2}}}.C_{{{y+x}}}^{{{y}}} $ \n\n"
	f" $P(A)= {kq}$")

	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	



#[D10_C9_B2_61]-SA-M4. XS chọn k người trong đó có đúng 1 cặp vợ chồng
def mjulk_L10_C9_B2_61():
	n=1
	k=n+1
	m=5
	x=random.randint(5,20)
	y=random.randint(10,25)

	kgm=binomial(x+y,5)
	nA= 2*binomial(y+x-4,3)+4*binomial(x+y-4,2)
	t1=(nA/kgm)
	kq="{:.2f}".format(t1).replace(".", ",")
	dap_an= kq
	noi_dung=f"Một công ty có ${{{x}}}$ nhân viên nam và ${{{y}}}$ nhân viên nữ trong đó có đúng ${{{k}}}$ cặp vợ chồng. Công ty chọn ngẫu nhiên ${{{m}}}$ người trong số ${{{x+y}}}$ nhân viên đi công tác. Tính xác suất sao cho trong ${{{m}}}$ người được chọn có đúng ${{{n}}}$ cặp vợ chồng. (Làm tròn kết quả đến hàng phần trăm)"
	noi_dung_loigiai=(f"$n(\\Omega)= C_{{{x+y}}}^{{{m}}} $ \n\n "
	
	f" TH1: Trong  ${{{m}}}$ người có ${{{n}}}$ cặp vợ chồng và ${{{m-2*n}}}$ người còn lại không có ai có vợ hoặc chồng trong công ty $C_{{{k}}}^{{{n}}}.C_{{{x+y-2*k}}}^{{{m-2*n}}}  $ \n\n "
	f" TH2: Trong  ${{{m}}}$ người có ${{{n}}}$ cặp vợ chồng, ${{{1}}}$ người có vợ hoặc chồng và ${{{m-2*n-1}}}$ người còn lại không phải vợ hoặc chồng với người đã chọn $C_{{{2}}}^{{{1}}}.C_{{{2}}}^{{{1}}}.C_{{{x+y-4}}}^{{{2}}}  $ \n\n "
	f" $n(A)= C_{{{k}}}^{{{n}}}.C_{{{x+y-2*k}}}^{{{m-2*n}}}+C_{{{2}}}^{{{1}}}.C_{{{2}}}^{{{1}}}.C_{{{x+y-4}}}^{{{2}}}  $ \n\n"
	f" $P(A)= {kq}$")

	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	



#[D10_C9_B2_62]-SA-M4. XS chọn số chia hết cho 11 có tận cùng là a
def mjulk_L10_C9_B2_62():
	n=random.choice([8,1,7,5,2,9,6,3,4])
	k=random.randint(4,7)
	m=11
	if k==4:
		dem=sum(1 for i in range(1000, 10000) if i % m == 0 and (i-n)%10==0) 
		kgm=9*10**3
		nA= dem
		t1=(nA/kgm)
	if k==5:
		dem=sum(1 for i in range(10000, 100000) if i % m == 0 and (i-n)%10==0) 
		kgm=9*10**4
		nA= dem
		t1=(nA/kgm)
	if k==6:
		dem=sum(1 for i in range(100000, 1000000) if i % m == 0 and (i-n)%10==0) 
		kgm=9*10**5
		nA= dem
		t1=(nA/kgm)
	if k==7:
		dem=sum(1 for i in range(1000000, 10000000) if i % m == 0 and (i-n)%10==0) 
		kgm=9*10**6
		nA= dem
		t1=(nA/kgm)
	kq="{:.2f}".format(t1).replace(".", ",")
	dap_an= kq
	noi_dung=f"Gọi A là tập hợp các số tự nhiên có ${{{k}}}$ chữ số. Chọn ngẫu nhiên một số trong A, tính xác suất để số được chọn chia hết cho ${{{m}}}$ và có chữ số tận cùng là ${{{n}}}$."
	noi_dung_loigiai=(f"$n(\\Omega)= 9.10^{{{k-1}}} $ \n\n "
		f"Xét ${10**(k-1)} \\le {m}q \\le {10**k-1}$ \n\n "
		f" ${int((10**(k-1))/m)+1} \\le q \\le {int((10**k-1)/m)}$ \n\n"
		f" Vì q có tận cùng là ${{{n}}}$ nên $q=10a+{n}$ \n\n"
		f" ${int((10**(k-1))/m)+1} \\le 10a+{n} \\le {int((10**k-1)/m)}$ \n\n"
		f" $ {phan_so((int((10**(k-1))/m)+1-n)/10)} \\le a \\le  {phan_so((int((10**k-1)/m)+1-n)/10)}$ \n\n"
	f" $n(A)= {dem}$ \n\n"
	f" $P(A)= {kq}$")

	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	






#[D10_C9_B2_63]-SA-M4. XS để tỏng k thẻ được chọn có 2 thẻ có tổng bằng a
def mjulk_L10_C9_B2_63():
	n=random.randint(8,20)
	m=random.choice([3,4,5,6])
	if m==4:
		kgm=binomial(2*n,m)
		nA= 2*n*(2*n-2)*(2*n-4)*(2*n-6)/factorial(4)
		t1=1-(nA/kgm)
		kq="{:.2f}".format(t1).replace(".", ",")
		dap_an= kq
		noi_dung=f"Có ${{{2*n}}}$ tấm thẻ được đánh số từ 1 đến ${{{2*n}}}$. Chọn ngẫu nhiên ra ${{{m}}}$ tấm thẻ. Tính xác suất để trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$. (Làm tròn kết quả đến hàng phần trăm)"
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{2*n}}}^{{{m}}} $ \n\n "
		f" Gọi A là biến cố trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$ \n\n "
		f" $\\overline{{A}} $: trong ${{{m}}}$ tấm thẻ chọn ra không có hai tấm thẻ nào mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$\n\n"
		f" $n(\\overline {{A}})= \\dfrac{{ C_{{{2*n}}}^{{{1}}}.C_{{{2*n-2}}}^{{{1}}}.C_{{{2*n-4}}}^{{{1}}}. C_{{{2*n-6}}}^{{{1}}} }}{{4!}}$ \n\n"
		f" $P(A)=1-P(\\overline{{A}})$\n\n"
		f" $P(A)= {kq}$")
	if m==3:
		kgm=binomial(2*n,m)
		nA= 2*n*(2*n-2)*(2*n-4)/factorial(3)
		t1=1-(nA/kgm)
		kq="{:.2f}".format(t1).replace(".", ",")
		dap_an= kq
		noi_dung=f"Có ${{{2*n}}}$ tấm thẻ được đánh số từ 1 đến ${{{2*n}}}$. Chọn ngẫu nhiên ra ${{{m}}}$ tấm thẻ. Tính xác suất để trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$.(Làm tròn kết quả đến hàng phần trăm)"
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{2*n}}}^{{{m}}} $ \n\n "
		f" Gọi A là biến cố trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$ \n\n "
		f" $\\overline{{A}} $: trong ${{{m}}}$ tấm thẻ chọn ra không có hai tấm thẻ nào mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$\n\n"
		f" $n(\\overline {{A}})= \\dfrac{{ C_{{{2*n}}}^{{{1}}}.C_{{{2*n-2}}}^{{{1}}}.C_{{{2*n-4}}}^{{{1}}}}}{{3!}}$ \n\n"
		f" $P(A)=1-P(\\overline{{A}})$\n\n"
		f" $P(A)= {kq}$")
	if m==5:
		kgm=binomial(2*n,m)
		nA= 2*n*(2*n-2)*(2*n-4)*(2*n-6)*(2*n-8)/factorial(5)
		t1=1-(nA/kgm)
		kq="{:.2f}".format(t1).replace(".", ",")
		dap_an= kq
		noi_dung=f"Có ${{{2*n}}}$ tấm thẻ được đánh số từ 1 đến ${{{2*n}}}$. Chọn ngẫu nhiên ra ${{{m}}}$ tấm thẻ. Tính xác suất để trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$. (Làm tròn kết quả đến hàng phần trăm)"
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{2*n}}}^{{{m}}} $ \n\n "
		f" Gọi A là biến cố trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$ \n\n "
		f" $\\overline{{A}} $: trong ${{{m}}}$ tấm thẻ chọn ra không có hai tấm thẻ nào mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$\n\n"
		f" $n(\\overline {{A}})= \\dfrac{{ C_{{{2*n}}}^{{{1}}}.C_{{{2*n-2}}}^{{{1}}}.C_{{{2*n-4}}}^{{{1}}}.C_{{{2*n-6}}}^{{{1}}}.C_{{{2*n-8}}}^{{{1}}}}}{{5!}}$ \n\n"
		f" $P(A)=1-P(\\overline{{A}})$\n\n"
		f" $P(A)= {kq}$")

	if m==6:
		kgm=binomial(2*n,m)
		nA= 2*n*(2*n-2)*(2*n-4)*(2*n-6)*(2*n-8)*(2*n-10)/factorial(6)
		t1=1-(nA/kgm)
		kq="{:.2f}".format(t1).replace(".", ",")
		dap_an= kq
		noi_dung=f"Có ${{{2*n}}}$ tấm thẻ được đánh số từ 1 đến ${{{2*n}}}$. Chọn ngẫu nhiên ra ${{{m}}}$ tấm thẻ. Tính xác suất để trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$. (Làm tròn kết quả đến hàng phần trăm)"
		noi_dung_loigiai=(f"$n(\\Omega)= C_{{{2*n}}}^{{{m}}} $ \n\n "
		f" Gọi A là biến cố trong ${{{m}}}$ tấm thẻ chọn ra có hai tấm thẻ mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$ \n\n "
		f" $\\overline{{A}} $: trong ${{{m}}}$ tấm thẻ chọn ra không có hai tấm thẻ nào mà tổng hai số trên hai tấm thẻ bằng ${{{2*n+1}}}$\n\n"
		f" $n(\\overline {{A}})= \\dfrac{{ C_{{{2*n}}}^{{{1}}}.C_{{{2*n-2}}}^{{{1}}}.C_{{{2*n-4}}}^{{{1}}}.C_{{{2*n-6}}}^{{{1}}} .C_{{{2*n-8}}}^{{{1}}}.C_{{{2*n-10}}}^{{{1}}} }}{{6!}}$ \n\n"
		f" $P(A)=1-P(\\overline{{A}})$\n\n"
		f" $P(A)= {kq}$")
	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an= kq

	return debai_word, loigiai_word, latex_tuluan, dap_an	