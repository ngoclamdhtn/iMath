import math
import sympy as sp
import numpy as np
from sympy import *
import random
from fractions import Fraction
import my_module
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

# Helper function to calculate quantile
def calculate_quantile(L, F, f, h, target_position):
    return L + ((target_position - F) / f) * h

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m
 
def tao_ten_mau_ghep_nhom():
    list_nhom=[["Khoảng tuổi","Số người"], ["Cân nặng(kg)","Số người"], 
    ["Điểm số","Số học sinh"], ["Lương(triệu đồng)","Số nhân viên"],
    ["Điểm thi","Số người dự thi"],
    ["Quãng đường chạy bộ (km)","Số ngày chạy bộ"]
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



#[D12_C3_B1_01]-M1. Tìm khoảng biến thiên của mẫu số liệu ghép nhóm.
def ytrzz_L12_C3_B1_01():
	
	#Tạo số nhóm, tên nhóm, tên tần số, số bắt đầu, khoảng cách
	so_nhom = random.randint(6,7)
	ten_nhom,ten_tan_so,u1,d,tan_so_min,tan_so_max = tao_ten_mau_ghep_nhom()
	
	#Tạo code latex chứa các khoảng giá trị và các tần số
	gia_tri,list_khoang_gia_tri,list_tan_so,tan_so=tao_mau_ghep_nhom(so_nhom,u1,d,tan_so_min,tan_so_max)


	kq=gia_tri[so_nhom-1] - gia_tri[0]

	k = random.randint(1,so_nhom-1)
	kq_fasle=[
		gia_tri[k] - gia_tri[1],
		gia_tri[k] + gia_tri[0],
		gia_tri[k] - gia_tri[0]+1,
		tan_so_max-tan_so_min,
		abs(tan_so[2]-tan_so[1]),
		abs(tan_so[3]-tan_so[2]),
		abs(tan_so[4]-tan_so[3]),
		
			]
	random.shuffle(kq_fasle)
	kq2,kq3,kq4=kq_fasle[0:3]

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	

	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)

	

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$".replace(".",",")
	pa_B= f"$ {{{kq2}}}$".replace(".",",")
	pa_C= f"$ {{{kq3}}}$".replace(".",",")
	pa_D= f"$ {{{kq4}}}$".replace(".",",")
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như sau:"

	dap_an=my_module.tra_ve_dap_an(list_PA) 
	debai= f"{noi_dung}\n"\
	f"{file_name}\n" \
	f" Khoảng biến thiên của mẫu số liệu ghép nhóm là\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=(f"Khoảng biến thiên của mẫu số liệu ghép nhóm là: "
	f"${gia_tri[so_nhom-1]} - {gia_tri[0]}={gia_tri[so_nhom-1] - gia_tri[0]}$")
	noi_dung_loigiai=noi_dung_loigiai.replace(".",",")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"
	

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_hinh}\\end{{center}}\n"\
	f" Khoảng biến thiên của mẫu số liệu ghép nhóm là.\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_hinh}\\end{{center}}\n"\
	f" Khoảng biến thiên của mẫu số liệu ghép nhóm là.\n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C3_B1_02]-M1. Tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm.
def ytrzz_L12_C3_B1_02():

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
	Q1_round=f"{round_half_up(Q1,2):.2f}".replace(".",",")
	

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
	Q3_round=f"{round_half_up(Q3,2):.2f}".replace(".",",")

	Delta_Q=Q3-Q1
	Delta_Q_round=f"{round_half_up(Delta_Q,2):.2f}".replace(".",",")

	kq=Delta_Q
	kq_false=[
		Q2-Q1,
		Q1+random.randint(1,2),
		Q3-Q2,
		Q3-Q2+random.randint(1,2),
		Q2-Q1+random.randint(1,2)]

	kq2,kq3,kq4=kq_false[0:3]
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{round_half_up(kq,2):.2f}}}$".replace(".",",")
	pa_B= f"${{{round_half_up(kq2,2):.2f}}}$".replace(".",",")
	pa_C= f"${{{round_half_up(kq3,2):.2f}}}$".replace(".",",")
	pa_D= f"${{{round_half_up(kq4,2):.2f}}}$".replace(".",",")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	#Code latex
	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	

	noi_dung=f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như bảng sau. Tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm đã cho."
	debai= f"{noi_dung} \n\n"\
					f"{file_name} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=(
		f"Tổng tần số là: $N={N}$.\n\n"
		f"Tìm tứ phân vị $Q_1$:\n\n"
	
		f"Bước 1: Xác định vị trí của $Q_1$: $Q_1$ nằm ở vị trí $\\dfrac{{{N}}}{{4}}={round_half_up(N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_1$: Tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_1$ ta được lớp $[{L_Q1};{R_Q1})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_1$.\n\n"
		f" Cận dưới của lớp $[{L_Q1};{R_Q1})$ chứa $Q_1$: $L={L_Q1}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_1$: $F={F_Q1}$\n\n"
		f" Tần số của lớp chứa $Q_1$: $f={f_Q1}$.\n\n"
		f" Độ rộng lớp chứa $Q_1$: $h={Q1_class[0][1]} - {Q1_class[0][0]}={h_Q1}$.\n\n"
		f"Áp dụng công thức: $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={phan_so(Q1)}$.\n\n"

		f"Tìm tứ phân vị $Q_3$:\n\n"
		f"Bước 1: Xác định vị trí của $Q_3$: $Q_3$ nằm ở vị trí $\\dfrac{{3.{N}}}{{4}}={round_half_up(3*N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_3$: tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_3$ ta được lớp $[{L_Q3};{R_Q3})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_3$.\n\n"
		f" Cận dưới của lớp $[{L_Q3};{R_Q3})$ chứa $Q_3$: $L={L_Q3}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_3$: $F={F_Q3}$\n\n"
		f" Tần số của lớp chứa $Q_3$: $f={f_Q3}$.\n\n"
		f" Độ rộng lớp chứa $Q_3$: $h={Q3_class[0][1]} - {Q3_class[0][0]}={h_Q3}$.\n\n"
		f"Áp dụng công thức: $Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={phan_so(Q3)}$.\n\n"
		f"Khoảng tứ phân vị là: $\\Delta_Q={phan_so(Q3)}-{phan_so(Q1)}={phan_so(Q3-Q1)}={Delta_Q_round}$."
		)
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_hinh}\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_hinh}\\end{{center}}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C3_B1_03]-TL-M3. Tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm.
def ytrzz_L12_C3_B1_03():

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
	Q1_round=f"{round_half_up(Q1,2):.2f}".replace(".",",")
	

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
	Q3_round=f"{round_half_up(Q3,2):.2f}".replace(".",",")

	Delta_Q=Q3-Q1
	Delta_Q_round=f"{round_half_up(Delta_Q,1):.1f}".replace(".",",")


	#Code latex
	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	

	noi_dung=(f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như bảng sau."
	f" Tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm đã cho (kết quả làm tròn đến hàng phần mười.")

	debai_word= f"{noi_dung} \n {file_name} \n"

	noi_dung_loigiai=(
		f"Tổng tần số là: $N={N}$.\n\n"

		f"Tìm tứ phân vị $Q_1$:\n\n"	
		f"Bước 1: Xác định vị trí của $Q_1$: $Q_1$ nằm ở vị trí $\\dfrac{{{N}}}{{4}}={round_half_up(N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_1$: Tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_1$ ta được lớp $[{L_Q1};{R_Q1})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_1$.\n\n"
		f" Cận dưới của lớp $[{L_Q1};{R_Q1})$ chứa $Q_1$: $L={L_Q1}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_1$: $F={F_Q1}$\n\n"
		f" Tần số của lớp chứa $Q_1$: $f={f_Q1}$.\n\n"
		f" Độ rộng lớp chứa $Q_1$: $h={Q1_class[0][1]} - {Q1_class[0][0]}={h_Q1}$.\n\n"
		f"Áp dụng công thức: $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={phan_so(Q1)}$.\n\n"

		f"Tìm tứ phân vị $Q_3$:\n\n"
		f"Bước 1: Xác định vị trí của $Q_3$: $Q_3$ nằm ở vị trí $\\dfrac{{3.{N}}}{{4}}={round_half_up(3*N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_3$: tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_3$ ta được lớp $[{L_Q3};{R_Q3})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_3$.\n\n"
		f" Cận dưới của lớp $[{L_Q3};{R_Q3})$ chứa $Q_3$: $L={L_Q3}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_3$: $F={F_Q3}$\n\n"
		f" Tần số của lớp chứa $Q_3$: $f={f_Q3}$.\n\n"
		f" Độ rộng lớp chứa $Q_3$: $h={Q3_class[0][1]} - {Q3_class[0][0]}={h_Q3}$.\n\n"
		f"Áp dụng công thức: $Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={phan_so(Q3)}$.\n\n"
		f"Khoảng tứ phân vị là: $\\Delta_Q={phan_so(Q3)}-{phan_so(Q1)}={phan_so(Q3-Q1)}={Delta_Q_round}$.\n\n"
		f"Đáp án: {Delta_Q_round}")
	dap_an=Delta_Q_round

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C3_B1_04]-TF-M3. Xét Đ-S: Khoảng biến thiên, Q1, Q3, khoảng tứ phân vị.
def ytrzz_L12_C3_B1_04():

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
	Q1_round=f"{round_half_up(Q1,2):.2f}".replace(".",",")
	Q1_false=Q1+random.randint(1,2)
	Q1_false_round=f"{round_half_up(Q1_false,2):.2f}".replace(".",",")
	

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
	Q3_round=f"{round_half_up(Q3,2):.2f}".replace(".",",")
	Q3_false=Q1+random.randint(1,2)
	Q3_false_round=f"{round_half_up(Q3_false,2):.2f}".replace(".",",")

	Delta_Q=Q3-Q1
	Delta_Q_round=f"{round_half_up(Delta_Q,2):.2f}".replace(".",",")

	Delta_Q_false=Delta_Q+random.randint(1,2)
	Delta_Q_false_round=f"{round_half_up(Delta_Q_false,2):.2f}".replace(".",",")

	#Code latex
	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)	

	noi_dung=( f"Cho bảng số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như hình dưới đây."
		f" Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm):")	

	kq=gia_tri[so_nhom-1] - gia_tri[0]
	
	kq1_T=f"* Khoảng biến thiên của mẫu số liệu là {kq}" 
	kq1_F=f"Khoảng biến thiên của mẫu số liệu là {kq+random.randint(1,2)}"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Khoảng biến thiên của mẫu số liệu là: ${gia_tri[so_nhom-1]} - {gia_tri[0]}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"* Tứ phân vị thứ nhất bằng ${{{Q1_round}}}$"
	kq2_F=f"Tứ phân vị thứ nhất bằng ${{{Q1_false_round}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=(
		f"Tìm tứ phân vị $Q_1$:\n\n"
		f"Tổng tần số là: $N={N}$.\n\n"
		f"Bước 1: Xác định vị trí của $Q_1$: $Q_1$ nằm ở vị trí $\\dfrac{{{N}}}{{4}}={round_half_up(N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_1$: Tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_1$ ta được lớp $[{L_Q1};{R_Q1})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_1$.\n\n"
		f" Cận dưới của lớp $[{L_Q1};{R_Q1})$ chứa $Q_1$: $L={L_Q1}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_1$: $F={F_Q1}$\n\n"
		f" Tần số của lớp chứa $Q_1$: $f={f_Q1}$.\n\n"
		f" Độ rộng lớp chứa $Q_1$: $h={Q1_class[0][1]} - {Q1_class[0][0]}={h_Q1}$.\n\n"
		f"Áp dụng công thức: $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={Q1_round}$.\n\n")
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* Tứ phân vị thứ ba bằng ${{{Q3_round}}}$" 
	kq3_F=f"Tứ phân vị thứ ba bằng ${{{Q3_false_round}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"Tìm tứ phân vị $Q_3$:\n\n"
		f"Tổng tần số là: $N={N}$.\n\n"
		f"Bước 1: Xác định vị trí của $Q_3$: $Q_3$ nằm ở vị trí $\\dfrac{{3.{N}}}{{4}}={round_half_up(3*N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_3$: tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_3$ ta được lớp $[{L_Q3};{R_Q3})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_3$.\n\n"
		f" Cận dưới của lớp $[{L_Q3};{R_Q3})$ chứa $Q_3$: $L={L_Q3}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_3$: $F={F_Q3}$\n\n"
		f" Tần số của lớp chứa $Q_3$: $f={f_Q3}$.\n\n"
		f" Độ rộng lớp chứa $Q_3$: $h={Q3_class[0][1]} - {Q3_class[0][0]}={h_Q3}$.\n\n"
		f"Áp dụng công thức: $Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={Q3_round}$.\n\n")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"* Khoảng tứ phân vị bằng ${{{Delta_Q_round}}}$"
	kq4_F=f"Khoảng tứ phân vị bằng ${{{Delta_Q_false_round}}}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f" $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={phan_so(Q1)}$.\n\n"
		f"$Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={phan_so(Q3)}$.\n\n"
		f"Khoảng tứ phân vị là: $\\Delta_Q={phan_so(Q3)}-{phan_so(Q1)}={phan_so(Q3-Q1)}={Delta_Q_round}$.\n\n"
		)
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"\
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
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f" Xét tính đúng sai của các khẳng định sau.\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C3_B1_05]-TF-M3. Xét Đ-S: Khoảng biến thiên, Q1, Q3, giá trị ngoại lệ.
def ytrzz_L12_C3_B1_05():

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
	Q1_round=f"{round_half_up(Q1,2):.2f}".replace(".",",")
	Q1_false=Q1+random.randint(1,2)
	Q1_false_round=f"{round_half_up(Q1_false,2):.2f}".replace(".",",")
	

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
	Q3_round=f"{round_half_up(Q3,2):.2f}".replace(".",",")
	Q3_false=Q1+random.randint(1,2)
	Q3_false_round=f"{round_half_up(Q3_false,2):.2f}".replace(".",",")

	Delta_Q=Q3-Q1
	Delta_Q_round=f"{round_half_up(Delta_Q,1):.2f}".replace(".",",")

	Delta_Q_false=Delta_Q+random.randint(1,2)
	Delta_Q_false_round=f"{round_half_up(Delta_Q_false,2):.2f}".replace(".",",")

	#Code latex
	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)	

	noi_dung=( f"Cho bảng số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như hình dưới đây."
		f" Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm):")	

	kq=gia_tri[so_nhom-1] - gia_tri[0]
	
	kq1_T=f"* Khoảng biến thiên của mẫu số liệu là {kq}" 
	kq1_F=f"Khoảng biến thiên của mẫu số liệu là {kq+random.randint(1,2)}"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Khoảng biến thiên của mẫu số liệu là: ${gia_tri[so_nhom-1]} - {gia_tri[0]}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"* Tứ phân vị thứ nhất bằng ${{{Q1_round}}}$"
	kq2_F=f"Tứ phân vị thứ nhất bằng ${{{Q1_false_round}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=(
		f"Tìm tứ phân vị $Q_1$:\n\n"
		f"Tổng tần số là: $N={N}$.\n\n"
		f"Bước 1: Xác định vị trí của $Q_1$: $Q_1$ nằm ở vị trí $\\dfrac{{{N}}}{{4}}={round_half_up(N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_1$: Tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_1$ ta được lớp $[{L_Q1};{R_Q1})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_1$.\n\n"
		f" Cận dưới của lớp $[{L_Q1};{R_Q1})$ chứa $Q_1$: $L={L_Q1}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_1$: $F={F_Q1}$\n\n"
		f" Tần số của lớp chứa $Q_1$: $f={f_Q1}$.\n\n"
		f" Độ rộng lớp chứa $Q_1$: $h={Q1_class[0][1]} - {Q1_class[0][0]}={h_Q1}$.\n\n"
		f"Áp dụng công thức: $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={Q1_round}$.\n\n")
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* Tứ phân vị thứ ba bằng ${{{Q3_round}}}$" 
	kq3_F=f"Tứ phân vị thứ ba bằng ${{{Q3_false_round}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"Tìm tứ phân vị $Q_3$:\n\n"
		f"Tổng tần số là: $N={N}$.\n\n"
		f"Bước 1: Xác định vị trí của $Q_3$: $Q_3$ nằm ở vị trí $\\dfrac{{3.{N}}}{{4}}={round_half_up(3*N/4,1)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_3$: tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_3$ ta được lớp $[{L_Q3};{R_Q3})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_3$.\n\n"
		f" Cận dưới của lớp $[{L_Q3};{R_Q3})$ chứa $Q_3$: $L={L_Q3}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_3$: $F={F_Q3}$\n\n"
		f" Tần số của lớp chứa $Q_3$: $f={f_Q3}$.\n\n"
		f" Độ rộng lớp chứa $Q_3$: $h={Q3_class[0][1]} - {Q3_class[0][0]}={h_Q3}$.\n\n"
		f"Áp dụng công thức: $Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={Q3_round}$.\n\n")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	a,b=Q1-1.5*Delta_Q, Q3+1.5*Delta_Q
	a_round=f"{round_half_up(a,2):.2f}".replace(".",",")
	b_round=f"{round_half_up(b,2):.2f}".replace(".",",")
	
	chon=random.randint(1,2)
	
	if chon==1:
		x=random.choice([Q1-random.randint(1,14)/10*Delta_Q, Q3+Delta_Q, Q3+random.randint(1,14)/10*Delta_Q])
		x_round=f"{round_half_up(x,2):.2f}".replace(".",",")		

		kq4_T=f"* ${{{x_round}}}$ không phải là giá trị ngoại lệ của mẫu số liệu"
		kq4_F=f"${{{x_round}}}$ là giá trị ngoại lệ của mẫu số liệu" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f" $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
			f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={phan_so(Q1)}$.\n\n"
			f"$Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
			f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={phan_so(Q3)}$.\n\n"
			f"Khoảng tứ phân vị là: $\\Delta_Q={phan_so(Q3)}-{phan_so(Q1)}={phan_so(Q3-Q1)}={Delta_Q_round}$.\n\n"
			f"Ta có: $Q_1-1,5.\\Delta_Q={a_round}, Q_3+1,5.\\Delta_Q={b_round}$.\n\n"
			f"Vì ${a_round}<{x_round}<{b_round}$ nên ${{{x_round}}}$ không phải là giá trị ngoại lệ của mẫu số liệu."
			)
	
	if chon==2:
		x=random.choice([Q3+random.randint(16,20)/10*Delta_Q])
		x_round=f"{round_half_up(x,2):.2f}".replace(".",",")		

		kq4_T=f"* ${{{x_round}}}$ là giá trị ngoại lệ của mẫu số liệu"
		kq4_F=f"${{{x_round}}}$ không phải là giá trị ngoại lệ của mẫu số liệu" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f" $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
			f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={phan_so(Q1)}$.\n\n"
			f"$Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
			f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={phan_so(Q3)}$.\n\n"
			f"Khoảng tứ phân vị là: $\\Delta_Q={phan_so(Q3)}-{phan_so(Q1)}={phan_so(Q3-Q1)}={Delta_Q_round}$.\n\n"
			f"Ta có: $Q_1-1,5.\\Delta_Q={a_round}, Q_3+1,5.\\Delta_Q={b_round}$.\n\n"
			f"Vì ${x_round}>{b_round}$ nên ${{{x_round}}}$ là giá trị ngoại lệ của mẫu số liệu."
			)
	
	
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"\
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
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f" Xét tính đúng sai của các khẳng định sau.\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C3_B1_06]-M3. Tìm giá trị ngoại lệ của bảng số liệu ghép nhóm.
def ytrzz_L12_C3_B1_06():
	while True:
		so_nhom = 6
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
		Q1_round=f"{round_half_up(Q1,2):.2f}".replace(".",",")

		

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
		Q3_round=f"{round_half_up(Q3,2):.2f}".replace(".",",")

		Delta_Q=Q3-Q1
		Delta_Q_round=f"{round_half_up(Delta_Q,2):.2f}".replace(".",",")
		a,b=Q1-1.5*Delta_Q, Q3+1.5*Delta_Q
		if a>1:
			break



	#Code latex
	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)	
	
	
	a1,b1=abs(Q1-Delta_Q), Q3+Delta_Q
	s_a=f"{round_half_up(a,2):.2f}".replace(".",",")
	s_b=f"{round_half_up(b,2):.2f}".replace(".",",")
	s_a1=f"{round_half_up(a1,2):.2f}".replace(".",",")
	s_b1=f"{round_half_up(b1,2):.2f}".replace(".",",")

	kq=random.choice([f"$x<{s_a}$", f"$x>{s_b}$"])
	kq_false=[
	f"$x<{s_b}$", 
	f"$x>{s_a}$",
	f"$x<{s_a1}$",
	f"$x>{s_b1}$",
	f"$x\\le {s_a}$", 
	f"$x\\ge {s_a}$",
	 ]
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	noi_dung=(f"Cho bảng số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như hình dưới đây."
		f"${{x}}$ là một giá trị ngoại lệ của bảng số liệu đã cho. Khẳng định nào sau đây là khẳng định đúng?"  )
	noi_dung_loigiai=(
	f"Tứ phân vị thứ nhất và thứ ba là: $Q_1={Q1_round}, Q_3={Q1_round}$.\n\n"
	f"Khoảng tứ phân vị là: $\\Delta_Q=Q_3-Q_1={Delta_Q_round}$.\n\n"
	f"${{x}}$ là giá trị ngoại lệ nếu $x<Q_1-1,5\\Delta_Q$ hoặc $x>Q_3+1,5\\Delta_Q$\n\n"
	f"Suy ra $x<{s_a}$ hoặc $x>{s_b}$."
	)

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#-------------------------Bài 2: Phương sai và Độ lệch chuẩn------------------------>
#[D12_C3_B2_01]-TF-M2. Tính phương sai của mẫu số liệu ghép nhóm.
def ytrzz_L12_C3_B2_01():
	
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

	#@@@# Sử dụng numpy để tính
	# Tính trung bình mỗi khoảng
	interval_means = [(a + b) / 2 for a, b in class_intervals]

	# Tính trung bình trọng số của mẫu
	weighted_mean = sum(mean * freq for mean, freq in zip(interval_means, frequencies)) / sum(frequencies)
	

	# Tính phương sai
	variance = sum(freq * (mean - weighted_mean) ** 2 for mean, freq in zip(interval_means, frequencies)) / (sum(frequencies))

	# Độ lệch chuẩn là căn bậc hai của phương sai
	std_dev = np.sqrt(variance)

	#@@@# Tính thủ công:

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
		tich_dai_dien_square_x_tan_so.append(b**2*a)
		st_b=f"{b}".replace(".",",")

		st_dai_dien_x_tan_so+=f"{a}.{st_b}+"
		st_dai_dien_square_x_tan_so+=f"{a}.{st_b}^2+"

	st_dai_dien_x_tan_so=st_dai_dien_x_tan_so[0:len(st_dai_dien_x_tan_so)-1]
	st_dai_dien_square_x_tan_so=st_dai_dien_square_x_tan_so[0:len(st_dai_dien_square_x_tan_so)-1]


	#Tính tổng các tần số
	tong_tan_so=sum(tan_so)
	so_trung_binh=f"{round_half_up(weighted_mean,2)}".replace(".",",")	

	#Tạo kết quả ảo
	tich = []	
	for a, b in zip(tan_so,gia_tri):
		t = a*b
		tich.append(t)
	tong_giatri_x_tan_so = sum(tich)

	
	kq_fasle=[
	variance+random.randint(1,3),
	variance-random.choice([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.25 ]),
	variance+random.choice([0.25,0.34,0.46,0.57,0.62,0.71,0.83,0.91]),
	sqrt(weighted_mean),
	sqrt(weighted_mean)+random.choice([0.25,0.34,0.46,0.57,0.62,0.71,0.83,0.91])
	]
	random.shuffle(kq_fasle)
	kq2,kq3,kq4=kq_fasle[0:3]

	kq=f"{round_half_up(variance,2):.2f}".replace(".",",")
	kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
	kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
	kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	

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
	f" Tính phương sai của mẫu số liệu ghép nhóm trên (kết quả làm tròn đến hàng phần trăm).\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	
	noi_dung_loigiai=(f"Các giá trị đại diện của mẫu số liệu là: {gia_tri_dai_dien}\n\n"
		f"Tổng tần số là: $n={tong_tan_so}$\n\n"
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("[","").replace("]","").replace(",",";")
	noi_dung_loigiai=noi_dung_loigiai.replace(".",",")

	noi_dung_loigiai+=(f"Số trung bình của mẫu số liệu ghép nhóm là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{{st_dai_dien_x_tan_so}}}{{ {tong_tan_so}}}={so_trung_binh}$.\n\n"
		f"Phương sai của mẫu số liệu ghép nhóm là:\n\n"
		f"$S^2=\\dfrac{{1}}{{{tong_tan_so}}}({st_dai_dien_square_x_tan_so})-{so_trung_binh}^2={kq}$.")


	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính phương sai của mẫu số liệu ghép nhóm trên.\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính phương sai của mẫu số liệu ghép nhóm trên.\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C3_B2_02]-TF-M2. Tính độ lệch chuẩn của mẫu số liệu ghép nhóm.
def ytrzz_L12_C3_B2_02():
	
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

	#@@@# Sử dụng numpy để tính
	# Tính trung bình mỗi khoảng
	interval_means = [(a + b) / 2 for a, b in class_intervals]

	# Tính trung bình trọng số của mẫu
	weighted_mean = sum(mean * freq for mean, freq in zip(interval_means, frequencies)) / sum(frequencies)

	# Tính phương sai
	variance = sum(freq * (mean - weighted_mean) ** 2 for mean, freq in zip(interval_means, frequencies)) / (sum(frequencies))

	# Độ lệch chuẩn là căn bậc hai của phương sai
	std_dev = np.sqrt(variance)

	#@@@# Tính thủ công:

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

		st_dai_dien_x_tan_so+=f"{a}.{st_b}+"
		st_dai_dien_square_x_tan_so+=f"{a}.{st_b}^2+"

	st_dai_dien_x_tan_so=st_dai_dien_x_tan_so[0:len(st_dai_dien_x_tan_so)-1]
	st_dai_dien_square_x_tan_so=st_dai_dien_square_x_tan_so[0:len(st_dai_dien_square_x_tan_so)-1]


	#Tính tổng các tần số
	tong_tan_so=sum(tan_so)
	so_trung_binh=f"{round_half_up(weighted_mean,2)}".replace(".",",")	

	#Tạo kết quả ảo
	tich = []	
	for a, b in zip(tan_so,gia_tri):
		t = a*b
		tich.append(t)
	tong_giatri_x_tan_so = sum(tich)

	
	kq_fasle=[
	variance+random.randint(1,3),
	variance-random.choice([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.25]),
	variance+random.choice([0.34,0.46,0.57,0.62,0.71,0.83,0.91]),
	sqrt(weighted_mean),
	sqrt(weighted_mean)+random.choice([0.25,0.34,0.46,0.57,0.62,0.71,0.83,0.91])
	]
	random.shuffle(kq_fasle)
	kq=sqrt(variance)
	kq2,kq3,kq4=kq_fasle[0:3]
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	variance_round=f"{round_half_up(variance,2):.2f}".replace(".",",")

	kq=f"{round_half_up(sqrt(variance),2):.2f}".replace(".",",")
	kq2=f"{round_half_up(sqrt(abs(kq2)),2):.2f}".replace(".",",")
	kq3=f"{round_half_up(sqrt(abs(kq3)),2):.2f}".replace(".",",")
	kq4=f"{round_half_up(sqrt(abs(kq4)),2):.2f}".replace(".",",")

	code_latex=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_latex)	
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""	

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
	f" Tính độ lệch chuẩn của mẫu số liệu ghép nhóm trên.\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	
	noi_dung_loigiai=(f"Các giá trị đại diện của mẫu số liệu là: {gia_tri_dai_dien}\n\n"
		f"Tổng tần số là: $n={tong_tan_so}$\n\n"
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("[","").replace("]","").replace(",",";")
	noi_dung_loigiai=noi_dung_loigiai.replace(".",",")

	noi_dung_loigiai+=(f"Số trung bình của mẫu số liệu ghép nhóm là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{{st_dai_dien_x_tan_so}}}{{ {tong_tan_so}}}={so_trung_binh}$.\n\n"
		f"Phương sai của mẫu số liệu ghép nhóm là:\n\n"
		f"$S^2=\\dfrac{{1}}{{{tong_tan_so}}}({st_dai_dien_square_x_tan_so})-{so_trung_binh}^2={variance_round}$.\n\n"
		f"Độ lệch chuẩn của mẫu số liệu ghép nhóm là: \n\n"
		f"$S=\\sqrt{{{variance_round}}}={kq}$."
		)


	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính độ lệch chuẩn của mẫu số liệu ghép nhóm trên.\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_latex}\\end{{center}}\n"\
	f" Tính độ lệch chuẩn của mẫu số liệu ghép nhóm trên.\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C3_B2_03]-TL-M2. Tính phương sai của mẫu số liệu ghép nhóm.
def ytrzz_L12_C3_B2_03():
	while True:

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

		#@@@# Sử dụng numpy để tính
		# Tính trung bình mỗi khoảng
		interval_means = [(a + b) / 2 for a, b in class_intervals]

		# Tính trung bình trọng số của mẫu
		weighted_mean = sum(mean * freq for mean, freq in zip(interval_means, frequencies)) / sum(frequencies)

		# Tính phương sai
		variance = sum(freq * (mean - weighted_mean) ** 2 for mean, freq in zip(interval_means, frequencies)) / (sum(frequencies))
		if variance<99:
			break

	# Độ lệch chuẩn là căn bậc hai của phương sai
	std_dev = np.sqrt(variance)

	#@@@# Tính thủ công:

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

		st_dai_dien_x_tan_so+=f"{a}.{st_b}+"
		st_dai_dien_square_x_tan_so+=f"{a}.{st_b}^2+"

	st_dai_dien_x_tan_so=st_dai_dien_x_tan_so[0:len(st_dai_dien_x_tan_so)-1]
	st_dai_dien_square_x_tan_so=st_dai_dien_square_x_tan_so[0:len(st_dai_dien_square_x_tan_so)-1]


	#Tính tổng các tần số
	tong_tan_so=sum(tan_so)
	so_trung_binh=f"{round_half_up(weighted_mean,2)}".replace(".",",")	

	#Tạo kết quả ảo
	tich = []	
	for a, b in zip(tan_so,gia_tri):
		t = a*b
		tich.append(t)
	tong_giatri_x_tan_so = sum(tich)


	dap_an=f"{round_half_up(variance,1):.1f}".replace(".",",")


	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)

	
	noi_dung= f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như sau:"

	debai_word=(f"{noi_dung}\n{file_name}\n"	
	f" Tính phương sai của mẫu số liệu ghép nhóm trên (kết quả làm tròn đến hàng phần mười).\n")
	
	noi_dung_loigiai=(f"Các giá trị đại diện của mẫu số liệu là: {gia_tri_dai_dien}\n\n"
		f"Tổng tần số là: $n={tong_tan_so}$\n\n"
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("[","").replace("]","").replace(",",";")
	noi_dung_loigiai=noi_dung_loigiai.replace(".",",")

	noi_dung_loigiai+=(f"Số trung bình của mẫu số liệu ghép nhóm là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{{st_dai_dien_x_tan_so}}}{{ {tong_tan_so}}}={so_trung_binh}$.\n\n"
		f"Phương sai của mẫu số liệu ghép nhóm là:\n\n"
		f"$S^2=\\dfrac{{1}}{{{tong_tan_so}}}({st_dai_dien_square_x_tan_so})-{so_trung_binh}^2={dap_an}$.\n\n"
		f"Đáp án: {dap_an}")


	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f" Tính phương sai của mẫu số liệu ghép nhóm trên (kết quả làm tròn đến hàng phần mười).\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C3_B2_04]-TL-M2. Tính độ lệch chuẩn của mẫu số liệu ghép nhóm.
def ytrzz_L12_C3_B2_04():
	while True:
	
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

		#@@@# Sử dụng numpy để tính
		# Tính trung bình mỗi khoảng
		interval_means = [(a + b) / 2 for a, b in class_intervals]

		# Tính trung bình trọng số của mẫu
		weighted_mean = sum(mean * freq for mean, freq in zip(interval_means, frequencies)) / sum(frequencies)

		# Tính phương sai
		variance = sum(freq * (mean - weighted_mean) ** 2 for mean, freq in zip(interval_means, frequencies)) / (sum(frequencies))
		if sqrt(variance)<99:
			break
	variance_round=f"{round_half_up(variance,2):.1f}".replace(".",",")
	# Độ lệch chuẩn là căn bậc hai của phương sai
	std_dev = np.sqrt(variance)

	#@@@# Tính thủ công:

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

		st_dai_dien_x_tan_so+=f"{a}.{st_b}+"
		st_dai_dien_square_x_tan_so+=f"{a}.{st_b}^2+"

	st_dai_dien_x_tan_so=st_dai_dien_x_tan_so[0:len(st_dai_dien_x_tan_so)-1]
	st_dai_dien_square_x_tan_so=st_dai_dien_square_x_tan_so[0:len(st_dai_dien_square_x_tan_so)-1]


	#Tính tổng các tần số
	tong_tan_so=sum(tan_so)
	so_trung_binh=f"{round_half_up(weighted_mean,2)}".replace(".",",")	

	#Tạo kết quả ảo
	tich = []	
	for a, b in zip(tan_so,gia_tri):
		t = a*b
		tich.append(t)
	tong_giatri_x_tan_so = sum(tich)


	dap_an=f"{round_half_up(sqrt(variance),2):.1f}".replace(".",",")


	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)

	
	noi_dung= f"Cho mẫu số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như sau:"

	debai_word=(f"{noi_dung}\n{file_name}\n"	
	f" Tính độ lệch chuẩn của mẫu số liệu ghép nhóm trên (kết quả làm tròn đến hàng phần mười).\n")
	
	noi_dung_loigiai=(f"Các giá trị đại diện của mẫu số liệu là: {gia_tri_dai_dien}\n\n"
		f"Tổng tần số là: $n={tong_tan_so}$\n\n"
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("[","").replace("]","").replace(",",";")
	noi_dung_loigiai=noi_dung_loigiai.replace(".",",")

	noi_dung_loigiai+=(f"Số trung bình của mẫu số liệu ghép nhóm là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{{st_dai_dien_x_tan_so}}}{{ {tong_tan_so}}}={so_trung_binh}$.\n\n"
		f"Phương sai của mẫu số liệu ghép nhóm là:\n\n"
		f"$S^2=\\dfrac{{1}}{{{tong_tan_so}}}({st_dai_dien_square_x_tan_so})-{so_trung_binh}^2={variance_round}$.\n\n"
		f"Độ lệch chuẩn của mẫu số liệu ghép nhóm là:\n\n"
		f"$S=\\sqrt{{{variance_round}}}={dap_an}$"
		f"Đáp án: {dap_an}")	


	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f" Tính độ lệch chuẩn của mẫu số liệu ghép nhóm trên (kết quả làm tròn đến hàng phần mười).\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C3_B2_05]-TF-M2. Xét Đ-S: số trung bình, phương sai, độ lệch chuẩn, khoảng tứ phân vị
def ytrzz_L12_C3_B2_05():
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
	
	# Tính giá trị đại diện mỗi khoảng
	interval_means = [(a + b) / 2 for a, b in class_intervals]

	# Tính trung bình trọng số của mẫu
	weighted_mean = sum(mean * freq for mean, freq in zip(interval_means, frequencies)) / sum(frequencies)

	# Tính phương sai
	variance = sum(freq * (mean - weighted_mean) ** 2 for mean, freq in zip(interval_means, frequencies)) / (sum(frequencies))
	variance_round=f"{round_half_up(variance,2):.2f}".replace(".",",")
	variance_false_round=f"{round_half_up(variance+random.choice([0.5,0.6,0.8,1]),2):.2f}".replace(".",",")

	# Độ lệch chuẩn là căn bậc hai của phương sai
	std_dev = np.sqrt(variance)

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
	Q1_round=f"{round_half_up(Q1,2):.2f}".replace(".",",")
	

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
	Q3_round=f"{round_half_up(Q3,2):.2f}".replace(".",",")

	Delta_Q=Q3-Q1
	Delta_Q_round=f"{round_half_up(Delta_Q,2):.2f}".replace(".",",")
	Delta_Q_false_round=f"{round_half_up(Delta_Q+random.randint(1,2),2):.2f}".replace(".",",")

	#@@@# Tính thủ công:

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

		st_dai_dien_x_tan_so+=f"{a}.{st_b}+"
		st_dai_dien_square_x_tan_so+=f"{a}.{st_b}^2+"

	st_dai_dien_x_tan_so=st_dai_dien_x_tan_so[0:len(st_dai_dien_x_tan_so)-1]
	st_dai_dien_square_x_tan_so=st_dai_dien_square_x_tan_so[0:len(st_dai_dien_square_x_tan_so)-1]

	#Tính tổng các tần số
	tong_tan_so=sum(tan_so)

	code_hinh=codelatex_bang_ghep_nhom(ten_nhom,list_khoang_gia_tri,ten_tan_so,list_tan_so)
	code=my_module.moi_truong_anh_latex(code_hinh)	
	file_name=my_module.pdftoimage_timename(code)
	
	noi_dung=( f"Cho bảng số liệu ghép nhóm về {ten_nhom.lower()} và {ten_tan_so.lower()} như hình dưới đây."
		f" Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm):")	


	so_trung_binh=f"{round_half_up(weighted_mean,2):.2f}".replace(".",",")
	so_trung_binh_false=f"{round_half_up(weighted_mean+random.choice([0.2,0.5,0.6,0.8,1]),2):.2f}".replace(".",",")
	
	kq1_T=f"* Số trung bình của mẫu số liệu bằng ${{{so_trung_binh}}}$" 
	kq1_F=f"Số trung bình của mẫu số liệu bằng ${{{so_trung_binh_false}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=(f"Số trung bình của mẫu số liệu ghép nhóm là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{{st_dai_dien_x_tan_so}}}{{ {tong_tan_so}}}={so_trung_binh}$.\n\n")

	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"* Phương sai của mẫu số liệu bằng ${{{variance_round}}}$"
	kq2_F=f" Phương sai của mẫu số liệu bằng ${{{variance_false_round}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=(f"Phương sai của mẫu số liệu ghép nhóm là:\n\n"
		f"$S^2=\\dfrac{{1}}{{{tong_tan_so}}}({st_dai_dien_square_x_tan_so})-{so_trung_binh}^2={variance_round}$.\n\n")
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	dolech_round=f"{round_half_up(sqrt(variance),2):.2f}".replace(".",",")
	dolech_false_round=f"{round_half_up(sqrt(variance)+random.choice([0.5,0.6,0.8,1]),2):.2f}".replace(".",",")

	kq3_T=f"* Độ lệch chuẩn của mẫu số liệu bằng ${{{dolech_round}}}$" 
	kq3_F=f"Độ lệch chuẩn của mẫu số liệu bằng ${{{dolech_false_round}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"Độ lệch chuẩn của mẫu số liệu ghép nhóm là:\n\n"
		f"$S=\\sqrt{{{variance_round}}}={dolech_round}$.")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"* Khoảng tứ phân vị của mẫu số liệu bằng ${{{Delta_Q_round}}}$"
	kq4_F=f"Khoảng tứ phân vị của mẫu số liệu bằng  ${{{Delta_Q_false_round}}}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"Tổng tần số là: $N={N}$.\n\n"

		f"Tìm tứ phân vị $Q_1$:\n\n"	
		f"Bước 1: Xác định vị trí của $Q_1$: $Q_1$ nằm ở vị trí $\\dfrac{{{N}}}{{4}}={round_half_up(N/4,2)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_1$: Tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_1$ ta được lớp $[{L_Q1};{R_Q1})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_1$.\n\n"
		f" Cận dưới của lớp $[{L_Q1};{R_Q1})$ chứa $Q_1$: $L={L_Q1}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_1$: $F={F_Q1}$\n\n"
		f" Tần số của lớp chứa $Q_1$: $f={f_Q1}$.\n\n"
		f" Độ rộng lớp chứa $Q_1$: $h={Q1_class[0][1]} - {Q1_class[0][0]}={h_Q1}$.\n\n"
		f"Áp dụng công thức: $Q_1=L+\\left(\\dfrac{{ \\dfrac{{N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q1}+\\left(\\dfrac{{ \\dfrac{{{N}}}{{4}}-{F_Q1} }}{{{f_Q1}}}\\right).{h_Q1}={phan_so(Q1)}$.\n\n"

		f"Tìm tứ phân vị $Q_3$:\n\n"
		f"Bước 1: Xác định vị trí của $Q_3$: $Q_3$ nằm ở vị trí $\\dfrac{{3.{N}}}{{4}}={round_half_up(3*N/4,2)}$.\n\n"
		f"Bước 2: Xác định lớp chứa $Q_3$: tính tần số tích lũy từ lớp đầu tiên đến khi đạt hoặc vượt qua vị trí của $Q_3$ ta được lớp $[{L_Q3};{R_Q3})$.\n\n"
		f"Bước 3: Xác định các thông số của công thức tính $Q_3$.\n\n"
		f" Cận dưới của lớp $[{L_Q3};{R_Q3})$ chứa $Q_3$: $L={L_Q3}$\n\n"
		f" Tổng tần số của các lớp trước lớp chứa $Q_3$: $F={F_Q3}$\n\n"
		f" Tần số của lớp chứa $Q_3$: $f={f_Q3}$.\n\n"
		f" Độ rộng lớp chứa $Q_3$: $h={Q3_class[0][1]} - {Q3_class[0][0]}={h_Q3}$.\n\n"
		f"Áp dụng công thức: $Q_3=L+\\left(\\dfrac{{ \\dfrac{{3N}}{{4}}-F }}{{f}}\\right).h"
		f"={L_Q3}+\\left(\\dfrac{{ \\dfrac{{3.{N}}}{{4}}-{F_Q3} }}{{{f_Q3}}}\\right).{h_Q3}={phan_so(Q3)}$.\n\n"
		f"Khoảng tứ phân vị là: $\\Delta_Q={phan_so(Q3)}-{phan_so(Q1)}={phan_so(Q3-Q1)}={Delta_Q_round}$.\n\n")
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"\
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
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an












