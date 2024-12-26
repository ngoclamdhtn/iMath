import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module

# Helper function to calculate quantile
def calculate_quantile(L, F, f, h, target_position):
    return L + ((target_position - F) / f) * h

def tao_ten_mau_ghep_nhom():
    list_nhom=[["Khoảng tuổi","Số người"], ["Cân nặng (đơn vị:kg)","Số người"], 
    ["Điểm số","Số học sinh"], ["Lương (đơn vị: triệu đồng)","Số nhân viên"],
    ["Điểm thi","Số người dự thi"],
    ["Quãng đường chạy bộ mỗi ngày (đơn vị: km)","Số ngày chạy bộ"]
    ]
    so_nhom=len(list_nhom)
    #Chọn ngẫu nhiên một nhóm
    i =random.randint(0,so_nhom-1)
    nhom=list_nhom[i]
    ten_nhom=nhom[0]
    ten_tan_so=nhom[1]
    #
    if "Khoảng tuổi" in ten_nhom:
        u1 = random.randint(15,25)
        d = random.randint(5,10)
        tan_so_min =1
        tan_so_max =35

    if "Cân nặng" in ten_nhom:
        u1 = random.randint(35,45)
        d = random.randint(5,10)
        tan_so_min =1
        tan_so_max =35

    if "Điểm số" in ten_nhom:
        u1 = random.choice([0,1,2])
        d = random.choice([2, 2.5])
        tan_so_min =1
        tan_so_max =10

    if "Điểm thi" in ten_nhom:
        u1 = random.choice([0,1,2])
        d = random.choice([2, 2.5, 3, 3.5])
        tan_so_min =1
        tan_so_max =20

    if "Lương" in ten_nhom:
        u1 = random.randint(5,10)
        d = random.randint(3,6)
        tan_so_min =1
        tan_so_max =15

    if "Quãng đường chạy bộ" in ten_nhom:
        u1 = random.choice([1,1.5,1.2])
        d = random.choice([0.5,1])
        tan_so_min =1
        tan_so_max =8
    return ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max

def tao_mau_ghep_nhom(so_nhom,so_bat_dau,khoang_cach,tan_so_min,tan_so_max):
    #Tạo số nhóm, số bắt đầu, khoảng cách
    u1= so_bat_dau
    d = khoang_cach

    #Tạo list các cặp giá trị và tần số
    gia_tri= [u1+i*d for i in range(so_nhom)]

    dau_noi=" & "
    khoang_gt=dau_noi.join(f"[{gia_tri[i-1]} ; {gia_tri[i]})" for i in range(1,so_nhom))
    khoang_gt=khoang_gt.replace(".",",")
    khoang_gt=khoang_gt.replace(",0","")

    tan_so=[random.randint(tan_so_min,tan_so_max) for i in range(so_nhom-1)]
    list_tan_so = dau_noi.join(f"{str(tan_so[i])}" for i in range(so_nhom-1))
    return gia_tri,khoang_gt,list_tan_so, tan_so

def codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so):
    code=f"\\begin{{tabular}}{{|c|c|c|c|c|c|c|}}\n\
        \\hline\n\
        {ten_nhom}   & {list_khoang_gia_tri}\\\\  \n\
        \\hline \n\
        {ten_tan_so} & {list_tan_so} \\\\ \n\
        \\hline \n\
    \\end{{tabular}}\n"
    return code

#### Bài 1:SỐ TRUNG BÌNH VÀ MỐT CỦA MẪU SỐ LIỆU GHÉP NHÓM #######

#[D11_C5_B1_01]. Tìm giá trị đại diện của mẫu số liệu ghép nhóm.
def treqw_L11_C5_B1_01():
	
	#Tạo số nhóm, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	u1= random.randint(15,25)
	d = random.randint(5,10)
	
	#Tạo list các cặp khoảng tuổi và số khách
	#Cú pháp: tao_mau_ghep_nhom(so_nhom,so_batdau,khoang_cach,tan_so_min,tan_so_max)

	do_tuoi,khoang_tuoi,so_nguoi=tao_mau_ghep_nhom(so_nhom,u1,d,1,15)[0:3]

	#Chọn khoảng tuổi ngẫu nhiên
	k = random.randint(1,so_nhom-1)
	nhom_k=f"[{do_tuoi[k-1]};{do_tuoi[k]})"
	nhom_k=nhom_k.replace(".",",")

	kq=str((do_tuoi[k-1] + do_tuoi[k])/2).replace(".",",")
	kq=kq.replace(",0","")
	kq2=str((do_tuoi[k-1] + do_tuoi[k])/4).replace(".",",")
	kq2=kq2.replace(",0","")
	kq3=do_tuoi[k]
	kq4=do_tuoi[k-1]

	ten_nhom="Khoảng tuổi"
	ten_tan_so="Số người"

	code_latex=codelatex_bang_ghep_nhom(ten_nhom,khoang_tuoi,ten_tan_so,so_nguoi)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	
	 
	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"$ {{{kq2}}}$"
	pa_C= f"$ {{{kq3}}}$"
	pa_D= f"$ {{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	noi_dung= f"Cho bảng số liệu ghép nhóm về độ tuổi và số lượng khách hàng của một cửa hàng như sau:"

	dap_an=my_module.tra_ve_dap_an(list_PA) 
	debai= f"{noi_dung}\n"\
	f"{file_name}\n" \
	f" Tính giá trị đại diện của nhóm ${{{nhom_k}}}$.\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Giá trị đại diện của nhóm là ${{{kq}}}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính giá trị đại diện của nhóm ${nhom_k}$.\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính giá trị đại diện của nhóm ${nhom_k}$.\n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C5_B1_02]. Tìm giá trị đại diện của mẫu số liệu ghép nhóm ngẫu nhiên.
def treqw_L11_C5_B1_02():
	
	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:3]

	#Chọn khoảng ngẫu nhiên
	k = random.randint(1,so_nhom-1)
	nhom_k=f"[{gia_tri[k-1]};{gia_tri[k]})"
	nhom_k=nhom_k.replace(".",",")

	kq=str((gia_tri[k-1] + gia_tri[k])/2).replace(".",",")
	kq=kq.replace(",0","")
	kq2=str((gia_tri[k-1] + gia_tri[k])/4).replace(".",",")
	kq2=kq2.replace(",0","")
	kq3=gia_tri[k]
	kq4=gia_tri[k-1]

	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"$ {{{kq2}}}$"
	pa_C= f"$ {{{kq3}}}$"
	pa_D= f"$ {{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như sau:"

	dap_an=my_module.tra_ve_dap_an(list_PA) 
	debai= f"{noi_dung}\n"\
	f"{file_name}\n" \
	f" Tính giá trị đại diện của nhóm ${{{nhom_k}}}$.\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Giá trị đại diện của nhóm là ${{{kq}}}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính giá trị đại diện của nhóm {nhom_k}.\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính giá trị đại diện của nhóm {nhom_k}.\n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an
	

#[D11_C5_B1_03]-M2. Tìm số trung bình của mẫu số liệu ghép nhóm ngẫu nhiên.
def treqw_L11_C5_B1_03():
	
	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:5]

	#Tìm list giá trị đại diện
	gia_tri_dai_dien=[]
	for i in range(1,len(gia_tri)):
		dai_dien = (gia_tri[i-1]+gia_tri[i])/2
		if int(dai_dien)==dai_dien:
			gia_tri_dai_dien.append(int(dai_dien))
		else:
			gia_tri_dai_dien.append(dai_dien)

	#Nhân giá trị đại diện và tần số rồi tính tổng
	tich, tich_dai_dien_square_x_tan_so = [],[]
	st_dai_dien_x_tan_so=""
	st_dai_dien_square_x_tan_so=""

	for a, b in zip(tan_so,gia_tri_dai_dien):
		tich.append(a*b)
		tich_dai_dien_square_x_tan_so.append(b**2*a)
		st_b=f"{b}".replace(".",",")
		st_dai_dien_x_tan_so+=f"{st_b}.{a}+"		

	st_dai_dien_x_tan_so=st_dai_dien_x_tan_so[0:len(st_dai_dien_x_tan_so)-1]
	
	tong_dai_dien_x_tan_so = sum(tich)

	#Tính tổng các tần số
	tong_tan_so=sum(tan_so)
	kq=	f"{tong_dai_dien_x_tan_so/tong_tan_so:.2f}"

	#Tạo kết quả ảo
	tich = []	
	for a, b in zip(tan_so,gia_tri):
		t = a*b
		tich.append(t)
	tong_giatri_x_tan_so = sum(tich)

	kq2=f"{(gia_tri[0]+gia_tri[so_nhom-1])/3:.2f}"	
	kq3=f"{sum(gia_tri)/so_nhom:.2f}"""
	kq4=f"{tong_giatri_x_tan_so/tong_tan_so:.2f}"

	kq=kq.replace(".",",")
	kq2=kq2.replace(".",",")
	kq3=kq3.replace(".",",")
	kq4=kq4.replace(".",",")

	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"$ {{{kq2}}}$"
	pa_C= f"$ {{{kq3}}}$"
	pa_D= f"$ {{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như sau:"		

	dap_an=my_module.tra_ve_dap_an(list_PA) 
	debai= f"{noi_dung}\n"\
	f"{file_name}\n"\
	f" Tính {ten_nhom.lower()} trung bình từ mẫu số liệu ghép nhóm trên.\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=(f"Các giá trị đại diện của mẫu số liệu là: {gia_tri_dai_dien}\n\n"
		f"Tổng tần số là: $n={tong_tan_so}$\n\n"
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("[","").replace("]","").replace(",",";")
	noi_dung_loigiai=noi_dung_loigiai.replace(".",",")

	noi_dung_loigiai+=(f"Số trung bình của mẫu số liệu ghép nhóm là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{{st_dai_dien_x_tan_so}}}{{ {tong_tan_so}}}={kq}$.\n\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính {ten_nhom.lower()} trung bình từ mẫu số liệu ghép nhóm trên.\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính {ten_nhom.lower()} trung bình từ mẫu số liệu ghép nhóm trên.\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D11_C5_B2_01]-M3. Tìm trung vị của mẫu số liệu ghép nhóm ngẫu nhiên.
def treqw_L11_C5_B2_01():
		
	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:5]

	#Code latex
	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	

	#Tìm list giá trị đại diện
	gia_tri_dai_dien=[]
	for i in range(1,len(gia_tri)):
		dai_dien = (gia_tri[i-1]+gia_tri[i])/2
		gia_tri_dai_dien.append(dai_dien)

	#Tính tổng các tần số	
	n=sum(tan_so)

	#Tìm list tần số tích lũy
	tan_so_tich_luy=[]
	t=0
	for i in range(1,len(gia_tri)):
		t=t+tan_so[i-1]
		tan_so_tich_luy.append(t)

	#Tìm vị trí của nhóm chứa trung vị
	i=0
	t=tan_so_tich_luy[0]
	while t<n/2:
		i=i+1
		t=tan_so_tich_luy[i]	
	k=i+1
	#r là đầu mút trái của nhóm thứ k
	r=gia_tri[k-1]

	#d là độ dài của nhóm k
	d=gia_tri[k]-gia_tri[k-1]

	#n_k là tần số tích lũy của nhóm k
	n_k=tan_so[k-1]

	#cf là tần số tích lũy của nhóm k-1
	cf=tan_so_tich_luy[k-2]

	#Tính trung vị
	Me= r+(n/2-cf)*d/n_k
	Me_2=r+(n/2+cf)*d/n_k

	
	Me_3=abs((n/2-cf)*d/n_k)

	r4=gia_tri[k]
	Me_4=r4+(n/2-cf)*d/n_k

	kq=	f"{Me:.2f}"
	kq2=f"{Me_2:.2f}"
	kq3=f"{Me_3:.2f}"
	kq4=f"{Me_4:.2f}"

	kq=kq.replace(".",",")
	kq2=kq2.replace(".",",")
	kq3=kq3.replace(".",",")
	kq4=kq4.replace(".",",")

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"$ {{{kq2}}}$"
	pa_C= f"$ {{{kq3}}}$"
	pa_D= f"$ {{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung=f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như bảng sau. Tính trung vị của mẫu số liệu ghép nhóm đã cho."
	debai= f"{noi_dung} \n\n"\
					f"{file_name} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f"Ta có: Tổng tần số là {n}\n"\
	f"Nhóm chứa trung vị là nhóm thứ $k={k}, r={r}, d={d}, n_k={n_k},cf={cf}$.\n"\
    					f"Áp dụng công thức tìm trung vị: $M_e=r+\\dfrac{{\\frac{{n}}{{2}}-cf}}{{n_k}}d={kq}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D11_C5_B2_02]-M3. Tìm mốt của mẫu số liệu ghép nhóm ngẫu nhiên.
def treqw_L11_C5_B2_02():

	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:5]

	#Tính tổng các tần số	
	n=sum(tan_so)

	#Tìm vị trí chứa tần số lớn nhất
	tan_so_max=max(tan_so)
	i=0
	t=tan_so[i]
	while t!=tan_so_max:
		i=i+1
		t=tan_so[i]	
	k=i+1
	while k>len(tan_so)-1:
		#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
		so_nhom = random.randint(6,7)
		ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
		
		#Tạo code latex chứa các khoảng giá trị và các tần số
		gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:5]

		#Tính tổng các tần số	
		n=sum(tan_so)

		#Tìm vị trí chứa tần số lớn nhất
		tan_so_max=max(tan_so)
		i=0
		t=tan_so[i]
		while t!=tan_so_max:
			i=i+1
			t=tan_so[i]	
		k=i+1

	#u_k là đầu mút trái của nhóm thứ k
	u_k1=gia_tri[k-1]
	#u_k1 là đầu mút phải của nhóm thứ k
	u_k2=gia_tri[k]

	#Tần số của nhóm k
	n_k=tan_so[k-1]

	#Tần số của nhóm k-1
	if k==1:
		n_k1=0
	else:		
		n_k1=tan_so[k-2]

	#Tần số của nhóm k+1
	if k==so_nhom:
		n_k2=0
	else:
		n_k2=tan_so[k]

	#d là độ dài của nhóm k
	d=gia_tri[k]-gia_tri[k-1]

	#Tính mốt
	M_o= u_k1 + (n_k-n_k1)*(u_k2-u_k1)/(2*n_k-n_k1-n_k2)
	Mo_2=u_k1 + (n_k-n_k1)*(u_k2-u_k1)/(3*n_k-n_k1-n_k2)	
	Mo_3=u_k1 + (n_k-n_k1)*(u_k2-u_k1)/n	
	Mo_4=u_k1 + (n_k-n_k1)*(u_k2-u_k1)/(2*n_k+n_k1+n_k2)

	kq=	f"{M_o:.2f}"
	kq2=f"{Mo_2:.2f}"
	kq3=f"{Mo_3:.2f}"
	kq4=f"{Mo_4:.2f}"

	kq=kq.replace(".",",")
	kq2=kq2.replace(".",",")
	kq3=kq3.replace(".",",")
	kq4=kq4.replace(".",",")

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"$ {{{kq2}}}$"
	pa_C= f"$ {{{kq3}}}$"
	pa_D= f"$ {{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	#Code latex
	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code) 
	

	noi_dung=f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như bảng sau. Tìm mốt của mẫu số liệu ghép nhóm đã cho."
	debai= f"{noi_dung} \n\n"\
					f"{file_name} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f"Nhóm chứa mốt là nhóm thứ $k={k}, n_k={n_k},n_{{k-1}}={n_k1}, n_{{k+1}}={n_k2}, u_k={u_k1}, u_{{k+1}}={u_k2}$.\n"\
    					f"Áp dụng công thức tìm trung vị: $M_o=u_k+\\dfrac{{ (n_k - n_{{k-1}}) }}{{(n_k-n_{{k-1}})+(n_k-n_{{k+1}}) }}(u_{{k+1}}-u_k)={kq}$."
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D11_C5_B2_03]-M3. Tìm tứ phân vị Q1 của mẫu số liệu ghép nhóm.
def treqw_L11_C5_B2_03():

	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:5]

	# Given data from the table
	class_intervals, frequencies=[],[]
	for i in range(1,so_nhom):
		class_intervals.append((gia_tri[i-1],gia_tri[i]))
		frequencies.append(tan_so[i-1])
	# class_intervals=[(9.5,12.5), (12.5,15.5), (15.5,18.5), (18.5,21.5), (21.5,24.5)]
	# frequencies=[3,12,15,24,2]

	# Calculating total number of students
	N = sum(frequencies)

	# Setting the desired positions for Q1 and Q3
	Q1_position = N / 4
	Q2_position = N / 2
	Q3_position = 3 * N / 4

	# Initializing cumulative frequency
	cumulative_frequency = 0
	Q1_class =Q2_class= Q3_class = None

	for i, (interval, freq) in enumerate(zip(class_intervals, frequencies)):
	    cumulative_frequency += freq
	    # Determine Q1 class
	    if not Q1_class and cumulative_frequency >= Q1_position:
	        Q1_class = (interval, freq, cumulative_frequency - freq)

	    # Determine Q2 class
	    if not Q2_class and cumulative_frequency >= Q2_position:
	        Q2_class = (interval, freq, cumulative_frequency - freq)

	    # Determine Q3 class
	    if not Q3_class and cumulative_frequency >= Q3_position:
	        Q3_class = (interval, freq, cumulative_frequency - freq)

	# Calculating Q1
	L_Q1 = Q1_class[0][0]
	R_Q1 = Q1_class[0][1]
	F_Q1 = Q1_class[2]
	f_Q1 = Q1_class[1]
	h_Q1 = Q1_class[0][1] - Q1_class[0][0]
	Q1 = calculate_quantile(L_Q1, F_Q1, f_Q1, h_Q1, Q1_position)
	Q1_round=f"{round(Q1,2):.2f}".replace(".",",")
	

	# Calculating Q2
	L_Q2 = Q2_class[0][0]
	R_Q2 = Q2_class[0][1]
	F_Q2 = Q2_class[2]
	f_Q2 = Q2_class[1]
	h_Q2 = Q2_class[0][1] - Q2_class[0][0]
	Q2 = calculate_quantile(L_Q2, F_Q2, f_Q2, h_Q2, Q2_position)	

	# Calculating Q3
	L_Q3 = Q3_class[0][0]
	R_Q3 = Q3_class[0][1]
	F_Q3 = Q3_class[2]
	f_Q3 = Q3_class[1]
	h_Q3 = Q3_class[0][1] - Q3_class[0][0]
	Q3 = calculate_quantile(L_Q3, F_Q3, f_Q3, h_Q3, Q3_position)
	Q3_round=f"{round(Q3,2):.2f}".replace(".",",")

	kq=Q1
	kq_false=[
		Q2,Q3, 
		Q1+random.randint(1,2),Q1+random.randint(3,4),
		Q2+random.randint(1,2),
		Q3+random.randint(1,2)]
	kq2,kq3,kq4=kq_false[0:3]
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{round(kq,2):.2f}}}$".replace(".",",")
	pa_B= f"${{{round(kq2,2):.2f}}}$".replace(".",",")
	pa_C= f"${{{round(kq3,2):.2f}}}$".replace(".",",")
	pa_D= f"${{{round(kq4,2):.2f}}}$".replace(".",",")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	#Code latex
	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	

	noi_dung=f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như bảng sau. Tìm tứ phân vị thứ nhất ${{Q_1}}$ của mẫu số liệu ghép nhóm đã cho."
	debai= f"{noi_dung} \n\n"\
					f"{file_name} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=(f"Bước 1: Tổng tần số là: $N={N}$.\n\n"
	f"Bước 2: Xác định vị trí của $Q_1$: $Q_1$ nằm ở vị trí $\\dfrac{{{N}}}{{4}}={round(N/4,1)}$.\n\n"
	f"Bước 3: Xác định lớp chứa $Q_1$: tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_1$ ta được lớp $[{L_Q1};{R_Q1})$.\n\n"
	f"Bước 4: Xác định các thông số của công thức tính $Q_1$.\n\n"
	f" Cận dưới của lớp chứa $Q_1$: $L={L_Q1}$\n\n"
	f" Tổng tần số của các lớp trước lớp chứa $Q_1$: $F={F_Q1}$\n\n"
	f" Tần số của lớp chứa $Q_1$: $f={f_Q1}$.\n\n"
	f" Độ rộng lớp chứa $Q_1$: $h={Q1_class[0][1]} - {Q1_class[0][0]}={h_Q1}$.\n\n"
	f"Áp dụng công thức: $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
	f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={Q1_round}$."
		)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C5_B2_04]-M3. Tìm tứ phân vị Q2 của mẫu số liệu ghép nhóm.
def treqw_L11_C5_B2_04():

	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:5]

	# Given data from the table
	class_intervals, frequencies=[],[]
	for i in range(1,so_nhom):
		class_intervals.append((gia_tri[i-1],gia_tri[i]))
		frequencies.append(tan_so[i-1])
	# class_intervals=[(9.5,12.5), (12.5,15.5), (15.5,18.5), (18.5,21.5), (21.5,24.5)]
	# frequencies=[3,12,15,24,2]

	# Calculating total number of students
	N = sum(frequencies)

	# Setting the desired positions for Q1 and Q3
	Q1_position = N / 4
	Q2_position = N / 2
	Q3_position = 3 * N / 4

	# Initializing cumulative frequency
	cumulative_frequency = 0
	Q1_class =Q2_class= Q3_class = None

	for i, (interval, freq) in enumerate(zip(class_intervals, frequencies)):
	    cumulative_frequency += freq
	    # Determine Q1 class
	    if not Q1_class and cumulative_frequency >= Q1_position:
	        Q1_class = (interval, freq, cumulative_frequency - freq)

	    # Determine Q2 class
	    if not Q2_class and cumulative_frequency >= Q2_position:
	        Q2_class = (interval, freq, cumulative_frequency - freq)

	    # Determine Q3 class
	    if not Q3_class and cumulative_frequency >= Q3_position:
	        Q3_class = (interval, freq, cumulative_frequency - freq)

	# Calculating Q1
	L_Q1 = Q1_class[0][0]
	R_Q1 = Q1_class[0][1]
	F_Q1 = Q1_class[2]
	f_Q1 = Q1_class[1]
	h_Q1 = Q1_class[0][1] - Q1_class[0][0]
	Q1 = calculate_quantile(L_Q1, F_Q1, f_Q1, h_Q1, Q1_position)
	Q1_round=f"{round(Q1,2):.2f}".replace(".",",")
	

	# Calculating Q2
	L_Q2 = Q2_class[0][0]
	R_Q2 = Q2_class[0][1]
	F_Q2 = Q2_class[2]
	f_Q2 = Q2_class[1]
	h_Q2 = Q2_class[0][1] - Q2_class[0][0]
	Q2 = calculate_quantile(L_Q2, F_Q2, f_Q2, h_Q2, Q2_position)
	Q2_round=f"{round(Q2,2):.2f}".replace(".",",")

	# Calculating Q3
	L_Q3 = Q3_class[0][0]
	R_Q3 = Q3_class[0][1]
	F_Q3 = Q3_class[2]
	f_Q3 = Q3_class[1]
	h_Q3 = Q3_class[0][1] - Q3_class[0][0]
	Q3 = calculate_quantile(L_Q3, F_Q3, f_Q3, h_Q3, Q3_position)
	Q3_round=f"{round(Q3,2):.2f}".replace(".",",")

	kq=Q2
	kq_false=[
		Q1,Q3, 
		Q1+random.randint(1,2),Q1+random.randint(3,4),
		Q2+random.randint(1,2),
		Q3+random.randint(1,2)]
	kq2,kq3,kq4=kq_false[0:3]
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{round(kq,2):.2f}}}$".replace(".",",")
	pa_B= f"${{{round(kq2,2):.2f}}}$".replace(".",",")
	pa_C= f"${{{round(kq3,2):.2f}}}$".replace(".",",")
	pa_D= f"${{{round(kq4,2):.2f}}}$".replace(".",",")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	#Code latex
	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	

	noi_dung=f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như bảng sau. Tìm tứ phân vị thứ hai ${{Q_2}}$ của mẫu số liệu ghép nhóm đã cho."
	debai= f"{noi_dung} \n\n"\
					f"{file_name} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=(f"Bước 1: Tổng tần số là: $N={N}$.\n\n"
	f"Bước 2: Xác định vị trí của $Q_2$: $Q_2$ nằm ở vị trí $\\dfrac{{{N}}}{{2}}={round(N/2,1)}$.\n\n"
	f"Bước 3: Xác định lớp chứa $Q_2$: bằng cách tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_2$ ta được lớp $[{L_Q2};{R_Q2})$.\n\n"
	f"Bước 4: Xác định các thông số của công thức tính $Q_2$.\n\n"
	f" Cận dưới của lớp chứa $Q_2$: $L={L_Q2}$\n\n"
	f" Tổng tần số của các lớp trước lớp chứa $Q_2$: $F={F_Q2}$\n\n"
	f" Tần số của lớp chứa $Q_2$: $f={f_Q2}$.\n\n"
	f" Độ rộng lớp chứa $Q_2$: $h={Q2_class[0][1]} - {Q2_class[0][0]}={h_Q2}$.\n\n"
	f"Áp dụng công thức: $Q_2=L+\\left(\\dfrac{{ \\dfrac{{N}}{{2}}-F }}{{f}}\\right).h"
	f"={L_Q2}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{2}}-{F_Q2} }}{{{f_Q2}}}\\right).{h_Q2}={Q2_round}$."
		)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C5_B2_05]-M3. Tìm tứ phân vị Q3 của mẫu số liệu ghép nhóm.
def treqw_L11_C5_B2_05():

	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()[0:7]
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)[0:5]

	# Given data from the table
	class_intervals, frequencies=[],[]
	for i in range(1,so_nhom):
		class_intervals.append((gia_tri[i-1],gia_tri[i]))
		frequencies.append(tan_so[i-1])
	# class_intervals=[(9.5,12.5), (12.5,15.5), (15.5,18.5), (18.5,21.5), (21.5,24.5)]
	# frequencies=[3,12,15,24,2]

	# Calculating total number of students
	N = sum(frequencies)

	# Setting the desired positions for Q1 and Q3
	Q1_position = N / 4
	Q2_position = N / 2
	Q3_position = 3 * N / 4

	# Initializing cumulative frequency
	cumulative_frequency = 0
	Q1_class =Q2_class= Q3_class = None

	for i, (interval, freq) in enumerate(zip(class_intervals, frequencies)):
	    cumulative_frequency += freq
	    # Determine Q1 class
	    if not Q1_class and cumulative_frequency >= Q1_position:
	        Q1_class = (interval, freq, cumulative_frequency - freq)

	    # Determine Q2 class
	    if not Q2_class and cumulative_frequency >= Q2_position:
	        Q2_class = (interval, freq, cumulative_frequency - freq)

	    # Determine Q3 class
	    if not Q3_class and cumulative_frequency >= Q3_position:
	        Q3_class = (interval, freq, cumulative_frequency - freq)

	# Calculating Q1
	L_Q1 = Q1_class[0][0]
	R_Q1 = Q1_class[0][1]
	F_Q1 = Q1_class[2]
	f_Q1 = Q1_class[1]
	h_Q1 = Q1_class[0][1] - Q1_class[0][0]
	Q1 = calculate_quantile(L_Q1, F_Q1, f_Q1, h_Q1, Q1_position)
	Q1_round=f"{round(Q1,2):.2f}".replace(".",",")
	

	# Calculating Q2
	L_Q2 = Q2_class[0][0]
	R_Q2 = Q2_class[0][1]
	F_Q2 = Q2_class[2]
	f_Q2 = Q2_class[1]
	h_Q2 = Q2_class[0][1] - Q2_class[0][0]
	Q2 = calculate_quantile(L_Q2, F_Q2, f_Q2, h_Q2, Q2_position)	

	# Calculating Q3
	L_Q3 = Q3_class[0][0]
	R_Q3 = Q3_class[0][1]
	F_Q3 = Q3_class[2]
	f_Q3 = Q3_class[1]
	h_Q3 = Q3_class[0][1] - Q3_class[0][0]
	Q3 = calculate_quantile(L_Q3, F_Q3, f_Q3, h_Q3, Q3_position)
	Q3_round=f"{round(Q3,2):.2f}".replace(".",",")

	kq=Q3
	kq_false=[
		Q1,Q2, 
		Q1+random.randint(1,2),Q1+random.randint(3,4),
		Q2+random.randint(1,2),
		Q3+random.randint(1,2)]
	kq2,kq3,kq4=kq_false[0:3]
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{round(kq,2):.2f}}}$".replace(".",",")
	pa_B= f"${{{round(kq2,2):.2f}}}$".replace(".",",")
	pa_C= f"${{{round(kq3,2):.2f}}}$".replace(".",",")
	pa_D= f"${{{round(kq4,2):.2f}}}$".replace(".",",")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	#Code latex
	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	

	noi_dung=f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như bảng sau. Tìm tứ phân vị thứ ba ${{Q_3}}$ của mẫu số liệu ghép nhóm đã cho."
	debai= f"{noi_dung} \n\n"\
					f"{file_name} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=(f"Bước 1: Tổng tần số là: $N={N}$.\n\n"
	f"Bước 2: Xác định vị trí của $Q_3$: $Q_3$ nằm ở vị trí $\\dfrac{{3.{N}}}{{4}}={round(3*N/4,1)}$.\n\n"
	f"Bước 3: Xác định lớp chứa $Q_3$: tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_3$ ta được lớp $[{L_Q3};{R_Q3})$.\n\n"
	f"Bước 4: Xác định các thông số của công thức tính $Q_3$.\n\n"
	f" Cận dưới của lớp chứa $Q_3$: $L={L_Q3}$\n\n"
	f" Tổng tần số của các lớp trước lớp chứa $Q_3$: $F={F_Q3}$\n\n"
	f" Tần số của lớp chứa $Q_3$: $f={f_Q3}$.\n\n"
	f" Độ rộng lớp chứa $Q_3$: $h={Q3_class[0][1]} - {Q3_class[0][0]}={h_Q3}$.\n\n"
	f"Áp dụng công thức: $Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
	f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={Q3_round}$."
		)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an
