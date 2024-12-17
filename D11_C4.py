import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

def code_hinh_tu_dien(s,a,b,c):
    code=f"\\begin{{tikzpicture}}[scale=0.7]\n\
\\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}};\n\
\\coordinate ({b}) at (1,-2) node at ({b}) [below] {{${b}$}};\n\
\\coordinate ({c}) at (4,0)   node at ({c}) [right] {{${c}$}};\n\
\\coordinate ({s}) at (1,3)   node at ({s}) [above] {{${s}$}};\n\
\\draw [dashed] ({a})--({c}) ; \n\
\\draw ({a})--({b}) ({b})--({c}) ({s})--({a}) ({s})--({b}) ({s})--({c});\n\
\\end{{tikzpicture}}\n"
    return code

def code_hinh_tu_dien_noname(s,a,b,c):
    code=f"\\begin{{tikzpicture}}[scale=0.7]\n\
\\coordinate ({a}) at (0,0);\n\
\\coordinate ({b}) at (1,-2);\n\
\\coordinate ({c}) at (4,0);\n\
\\coordinate ({s}) at (1,3);\n\
\\draw [dashed] ({a})--({c}); \n\
\\draw ({a})--({b}) ({b})--({c}) ({s})--({a}) ({s})--({b}) ({s})--({c});\n\
\\end{{tikzpicture}}\n"
    return code

def code_hinh_chop_deu(S,A,B,C,D):
	code=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick,scale=0.6]\n\
\\coordinate ({A}) at (0,0);\n\
\\coordinate ({B}) at (2,-2);\n\
\\coordinate ({D}) at (5,0);\n\
\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
\\coordinate (O) at ($({A})!0.5!({C})$);\n\
\\coordinate ({S}) at ($(O)+(0,5)$);\n\
\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C});\n\
\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D});\n\
\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
\\end{{tikzpicture}}\n"
	return code

def code_hinh_chop_deu_noname(S,A,B,C,D):
	code=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick,scale=0.6]\n\
\\coordinate ({A}) at (0,0);\n\
\\coordinate ({B}) at (2,-2);\n\
\\coordinate ({D}) at (5,0);\n\
\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
\\coordinate (O) at ($({A})!0.5!({C})$);\n\
\\coordinate ({S}) at ($(O)+(0,5)$);\n\
\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C});\n\
\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D});\n\
\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{}};}}\n\
\\end{{tikzpicture}}\n"
	return code

def code_hinh_chop_tugiac(S,A,B,C,D):
	code=f" \\begin{{tikzpicture}}[line cap=round,line join=round,>=stealth,x=0.7cm,y=0.7cm]\n\
			\\draw (0.0,-0.0)-- (2.0,-2.0);\n\
			\\draw (5.0,0.0)-- (3.0,3.0);\n\
			\\draw (3.0,3.0)-- (0.0,-0.0);\n\
			\\draw (3.0,3.0)-- (4.0,-1.5);\n\
			\\draw (3.0,3.0)-- (2.0,-2.0);\n\
			\\draw (4.0,-1.5)-- (2.0,-2.0);\n\
			\\draw (4.0,-1.5)-- (5.0,0.0);\n\
			\\draw [dash pattern=on 2pt off 2pt] (0.0,-0.0)-- (5.0,0.0);\n\
			\\begin{{scriptsize}}\n\
			\\draw [fill=black] (0.0,-0.0) circle (1pt);\n\
			\\draw[color=black] (-0.06,0.2) node {{${A}$}};\n\
			\\draw [fill=black] (2.0,-2.0) circle (1pt);\n\
			\\draw[color=black] (1.7,-1.95) node {{${D}$}};\n\
			\\draw [fill=black] (5.0,0.0) circle (1pt);\n\
			\\draw[color=black] (5.15,0.15) node {{${B}$}};\n\
			\\draw [fill=black] (4.0,-1.5) circle (1pt);\n\
			\\draw[color=black] (4.2,-1.65) node {{${C}$}};\n\
			\\draw [fill=black] (3.0,3.0) circle (1pt);\n\
			\\draw[color=black] (3.2,3.0) node {{${S}$}};\n\
			\\end{{scriptsize}}\n\
			\\end{{tikzpicture}}\n"
	return code



#Bài 1 - Đường thẳng và mặt phẳng trong không gian
#[D11_C4_B1_01]-M2. Cho tứ diện. Xét quan hệ giữa điểm và đường thẳng-mặt phẳng
def ghj_7_jkl_L11_C4_B1_01():
	S=["S","A","O","S","O","S"]
	A=["A","B","A","A","B","B"]
	B=["B","C","B","C","C","C"]
	C=["C","D","C","D","D","D"]
	i=random.randint(0,5)
	S,A,B,C = S[i],A[i],B[i],C[i]
	M=random.choice(["M","N","P"])
	G=random.choice(["G","I","H","K"])

	code_hinh=code_hinh_tu_dien(S,A,B,C)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)


	noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$. Gọi ${{{M}}}$ là trung điểm của cạnh ${{{B}{C}}}$."
	f" Gọi ${{{G}}}$ là trọng tâm của tam giác ${{{A}{B}{C}}}$."
	f" Tìm khẳng định đúng trong các khẳng định sau")	

	kq=random.choice([
		f"${{{G}{M}}}\\subset ({A}{B}{C})$",
		f"${{{S}{M}}}\\subset ({S}{B}{C})$",
		f"${{{S}{G}}}\\subset ({S}{A}{M})$",
		f"${{{A}{G}}}\\subset ({A}{B}{C})$",
		f"${{{B}{G}}}\\subset ({A}{B}{C})$",
		f"${{{C}{G}}}\\subset ({A}{B}{C})$",
		])
	kq2=random.choice([
		f"${G} \\in ({S}{B}{C})$",
		f"${G} \\in ({S}{A}{B})$",
		f"${G} \\in ({S}{A}{C})$",
		f"${B} \\in ({S}{A}{M})$",
		f"${C} \\in ({S}{A}{G})$",
		f"${A} \\in ({S}{G}{C})$",
		f"${A} \\in ({S}{G}{B})$",
		])
	kq3=random.choice([
		f"${S}{G} \\subset ({S}{B}{C})$",
		f"${S}{G} \\subset ({S}{A}{B})$",
		f"${S}{G} \\subset ({S}{A}{C})$",
		f"${A}{B} \\subset ({S}{B}{C})$",
		f"${A}{C} \\subset ({S}{A}{B})$",
		f"${B}{C} \\subset ({S}{A}{M})$"
		])
	kq4=random.choice([
		f"${A}\\in {S}{M}$",
		f"${B}\\in {S}{G}$",
		f"${C}\\in {S}{G}$",
		f"${M}\\in {S}{A}$",
		f"${M}\\in {S}{B}$",
		f"${M}\\in {S}{C}$"
		])

	noi_dung_loigiai=f"{kq} là khẳng định đúng."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n\n{file_name}\n"

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
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B1_02]-M2. Cho hình chóp đáy là h.b.h. Xét quan hệ giữa điểm - đường thẳng - mặt phẳng
def ghj_7_jkl_L11_C4_B1_02():
	S=["S","S","S","S","S","S"]
	A=["A","A","A","B","A","A"]
	B=["B","B","B","C","B","B"]
	C=["C","D","C","D","M","E"]
	D=["D","E","D","E","N","F"]
	i=random.randint(0,5)

	S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]
	O=random.choice(["O","H","I"])
	I=random.choice(["G","K", "P", "Q"])

	code_hinh=code_hinh_chop_deu(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là hình bình hành tâm ${{{O}}}$."
	f" Gọi ${{{I}}}$ là trung điểm của ${{{S}{O}}}$."
	f" Tìm khẳng định sai trong các khẳng định sau")
	
	if chon==2:
		noi_dung=(f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là hình bình hành tâm ${{{O}}}$."
	f" Gọi ${{{I}}}$ là điểm thuộc đoạn ${{{S}{O}}}$ sao cho ${{{I}}}$ khác điểm ${{{S}}}$ và điểm ${{{O}}}$."
	f" Tìm khẳng định sai trong các khẳng định sau")
	

	kq=random.choice([
		f"${{{random.choice([f"{O}",f"{I}"])}}} \\in ({random.choice([f"{S}{B}{C}", f"{S}{C}{D}", f"{S}{A}{D}", f"{S}{A}{B}" ])})$",

		f"${{{random.choice([f"{O}{I}",f"{I}{O}",f"{I}{A}", f"{I}{B}", f"{I}{C}", f"{I}{D}" ])}}} \\subset ({random.choice([f"{S}{B}{C}", f"{S}{C}{D}", f"{S}{A}{D}", f"{S}{A}{B}"])})$"
		])

	kq2=random.choice([
		f"${{{random.choice([f"{S}{O}", f"{I}{O}", f"{S}{I}", f"{I}{A}", f"{I}{C}", f"{A}{C}" ])}}} \\subset ({S}{A}{C})$"
		])

	kq3=random.choice([
		f"${{{random.choice([f"{I}{B}", f"{I}{D}", f"{S}{I}", f"{S}{O}" ])}}} \\subset ({S}{B}{D})$"
		])

	kq4=random.choice([
		f"${{{random.choice([f"{I}",f"{O}"])}}} \\in ({random.choice([f"{S}{B}{D}", f"{S}{A}{C}", f"{S}{A}{O}", f"{S}{O}{C}", f"{S}{O}{D}" , f"{S}{B}{O}"])})$"
		])

	noi_dung_loigiai=f"{kq} là khẳng định sai."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	#random.shuffle(list_PA)
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
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B1_03]-M2. Cho hình chóp tứ giác. Xét quan hệ giữa điểm - đường thẳng - mặt phẳng
def ghj_7_jkl_L11_C4_B1_03():
	S=["S","S","S","S","S","S"]
	A=["A","A","B","B","A","A"]
	B=["B","B","C","C","B","B"]
	C=["C","D","E","D","M","E"]
	D=["D","E","F","E","N","F"]
	i=random.randint(0,5)

	S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]
	O=random.choice(["O","H","G"])
	I=random.choice(["I","Q", "P"])

	code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(f"Cho hình chóp tứ giác ${{{S}.{A}{B}{C}{D}}}$. Gọi ${{{O}}}$ là giao điểm của các đường thẳng ${{{A}{C}}}$ và ${{{B}{D}}}$."
	f" Gọi ${{{I}}}$ là trung điểm của ${{{S}{O}}}$."
	f" Tìm khẳng định sai trong các khẳng định sau")
	
	if chon==2:
		noi_dung=(f"Cho hình chóp tứ giác ${{{S}.{A}{B}{C}{D}}}$. Gọi ${{{O}}}$ là giao điểm của các đường thẳng ${{{A}{C}}}$ và ${{{B}{D}}}$."
	f" Gọi ${{{I}}}$ là điểm thuộc đoạn ${{{S}{O}}}$ sao cho ${{{I}}}$ khác điểm ${{{S}}}$ và điểm ${{{O}}}$."
	f" Tìm khẳng định sai trong các khẳng định sau")
	
	
	kq=random.choice([
		f"${{{random.choice([f"{O}",f"{I}"])}}} \\in ({random.choice([f"{S}{B}{C}", f"{S}{C}{D}", f"{S}{A}{D}", f"{S}{A}{B}" ])})$",

		f"${{{random.choice([f"{O}{I}",f"{I}{O}",f"{I}{A}", f"{I}{B}", f"{I}{C}", f"{I}{D}" ])}}} \\subset ({random.choice([f"{S}{B}{C}", f"{S}{C}{D}", f"{S}{A}{D}", f"{S}{A}{B}"])})$"
		])

	kq2=random.choice([
		f"${{{random.choice([f"{S}{O}", f"{I}{O}", f"{S}{I}", f"{I}{A}", f"{I}{C}", f"{A}{C}" ])}}} \\subset ({S}{A}{C})$"
		])

	kq3=random.choice([
		f"${{{random.choice([f"{I}{B}", f"{I}{D}", f"{S}{I}", f"{S}{O}" ])}}} \\subset ({S}{B}{D})$"
		])

	kq4=random.choice([
		f"${{{random.choice([f"{I}",f"{O}"])}}} \\in ({random.choice([f"{S}{B}{D}", f"{S}{A}{C}", f"{S}{A}{O}", f"{S}{O}{C}", f"{S}{O}{D}" , f"{S}{B}{O}"])})$"
		])

	noi_dung_loigiai=f"{kq} là khẳng định sai."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	#random.shuffle(list_PA)
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
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B1_04]-M1. Cho tứ diện hoặc hình chóp tứ giác. Tìm giao tuyến giữa các mặt bên
def ghj_7_jkl_L11_C4_B1_04():
	S=["S","A","O","S","O","S"]
	A=["A","B","A","A","B","B"]
	B=["B","C","B","C","C","C"]
	C=["C","D","C","D","D","D"]
	i=random.randint(0,5)
	S,A,B,C = S[i],A[i],B[i],C[i]
	M=random.choice(["M","N","P"])
	G=random.choice(["G","I","H","K"])

	

	chon=random.randint(1,12)
	if chon==1:
		code_hinh=code_hinh_tu_dien(S,A,B,C)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{A}{B})$ và $({S}{A}{C})$ là đường thẳng nào trong các đường thẳng sau?")	

		kq=f"${{{S}{A}}}$"
		kq2=f"${{{A}{B}}}$"
		kq3=f"${{{S}{B}}}$"
		kq4=f"${{{A}{C}}}$"
	
	if chon==2:
		code_hinh=code_hinh_tu_dien(S,A,B,C)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là đường thẳng nào trong các đường thẳng sau?")	

		kq=f"${{{S}{B}}}$"
		kq2=f"${{{A}{B}}}$"
		kq3=f"${{{S}{A}}}$"
		kq4=f"${{{A}{C}}}$"

	if chon==3:
		code_hinh=code_hinh_tu_dien(S,A,B,C)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{A}{B})$ và $({A}{B}{C})$ là đường thẳng nào trong các đường thẳng sau?")	

		kq=f"${{{A}{B}}}$"
		kq2=f"${{{S}{B}}}$"
		kq3=f"${{{S}{A}}}$"
		kq4=f"${{{A}{C}}}$"

	if chon==4:
		code_hinh=code_hinh_tu_dien(S,A,B,C)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{A}{C})$ và $({A}{B}{C})$ là đường thẳng nào trong các đường thẳng sau?")

		kq=f"${{{A}{C}}}$"
		kq2=f"${{{S}{B}}}$"
		kq3=f"${{{S}{A}}}$"
		kq4=f"${{{A}{B}}}$"

	if chon==5:
		code_hinh=code_hinh_tu_dien(S,A,B,C)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{B}{C})$ và $({A}{B}{C})$ là đường thẳng nào trong các đường thẳng sau?")	

		kq=f"${{{B}{C}}}$"
		kq2=f"${{{S}{B}}}$"
		kq3=random.choice([f"${{{S}{A}}}$", f"${{{A}{B}}}$"])
		kq4=f"${{{A}{C}}}$"

	
	
	if chon==6:
		S=["S","S","O","O","O","S"]
		A=["A","A","A","B","A","A"]
		B=["B","C","B","C","B","B"]
		C=["C","B","C","D","E","E"]
		D=["D","D","D","E","F","F"]
		i=random.randint(0,5)

		S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]

		code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho hình chóp ${{{S}{A}{B}{C}{D}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là đường thẳng nào trong các đường thẳng sau?")

		kq=f"${{{S}{B}}}$"
		kq2=f"${{{A}{C}}}$"
		kq3=f"${{{S}{A}}}$"
		kq4=f"${{{A}{B}}}$"
	
	if chon==7:
		S=["S","S","O","O","O","S"]
		A=["A","A","A","B","A","A"]
		B=["B","C","B","C","B","B"]
		C=["C","B","C","D","E","E"]
		D=["D","D","D","E","F","F"]
		i=random.randint(0,5)

		S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]

		code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho hình chóp ${{{S}{A}{B}{C}{D}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{B}{C})$ và $({S}{C}{D})$ là đường thẳng nào trong các đường thẳng sau?")
		
		kq=f"${{{S}{C}}}$"
		kq2=random.choice([f"${{{A}{C}}}$",f"${{{S}{D}}}$" ])
		kq3=random.choice([f"${{{S}{A}}}$",f"${{{B}{C}}}$" ])
		kq4=random.choice([f"${{{A}{B}}}$", f"${{{B}{D}}}$"])

	if chon==8:
		S=["S","S","O","O","O","S"]
		A=["A","A","A","B","A","A"]
		B=["B","C","B","C","B","B"]
		C=["C","B","C","D","E","E"]
		D=["D","D","D","E","F","F"]
		i=random.randint(0,5)

		S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]

		code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho hình chóp ${{{S}{A}{B}{C}{D}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{C}{D})$ và $({S}{A}{D})$ là đường thẳng nào trong các đường thẳng sau?")
		
		kq=f"${{{S}{D}}}$"
		kq2=random.choice([f"${{{A}{C}}}$",f"${{{S}{B}}}$" ])
		kq3=random.choice([f"${{{S}{A}}}$",f"${{{B}{C}}}$" ])
		kq4=random.choice([f"${{{A}{B}}}$", f"${{{B}{D}}}$"])

	if chon==9:
		S=["S","S","O","O","O","S"]
		A=["A","A","A","B","A","A"]
		B=["B","C","B","C","B","B"]
		C=["C","B","C","D","E","E"]
		D=["D","D","D","E","F","F"]
		i=random.randint(0,5)

		S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]

		code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho hình chóp ${{{S}{A}{B}{C}{D}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{A}{B})$ và $({B}{C}{D})$ là đường thẳng nào trong các đường thẳng sau?")
		
		kq=f"${{{A}{B}}}$"
		kq2=random.choice([f"${{{A}{C}}}$",f"${{{S}{B}}}$" ])
		kq3=random.choice([f"${{{S}{A}}}$",f"${{{B}{C}}}$" ])
		kq4=random.choice([f"${{{A}{D}}}$", f"${{{B}{D}}}$"])

	if chon==10:
		S=["S","S","O","O","O","S"]
		A=["A","A","A","B","A","A"]
		B=["B","C","B","C","B","B"]
		C=["C","B","C","D","E","E"]
		D=["D","D","D","E","F","F"]
		i=random.randint(0,5)

		S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]

		code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho hình chóp ${{{S}{A}{B}{C}{D}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{B}{C})$ và $({A}{C}{D})$ là đường thẳng nào trong các đường thẳng sau?")
		
		kq=f"${{{B}{C}}}$"
		kq2=random.choice([f"${{{A}{C}}}$",f"${{{S}{B}}}$" ])
		kq3=random.choice([f"${{{S}{A}}}$",f"${{{A}{B}}}$" ])
		kq4=random.choice([f"${{{A}{D}}}$", f"${{{B}{D}}}$"])

	if chon==11:
		S=["S","S","O","O","O","S"]
		A=["A","A","A","B","A","A"]
		B=["B","C","B","C","B","B"]
		C=["C","B","C","D","E","E"]
		D=["D","D","D","E","F","F"]
		i=random.randint(0,5)

		S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]

		code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho hình chóp ${{{S}{A}{B}{C}{D}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{C}{D})$ và $({A}{B}{C})$ là đường thẳng nào trong các đường thẳng sau?")
		
		kq=f"${{{C}{D}}}$"
		kq2=random.choice([f"${{{A}{C}}}$",f"${{{S}{B}}}$" ])
		kq3=random.choice([f"${{{S}{A}}}$",f"${{{A}{B}}}$" ])
		kq4=random.choice([f"${{{A}{D}}}$", f"${{{B}{D}}}$"])


	if chon==12:
		S=["S","S","O","O","O","S"]
		A=["A","A","A","B","A","A"]
		B=["B","C","B","C","B","B"]
		C=["C","B","C","D","E","E"]
		D=["D","D","D","E","F","F"]
		i=random.randint(0,5)

		S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]

		code_hinh=code_hinh_chop_tugiac(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=(f"Cho hình chóp ${{{S}{A}{B}{C}{D}}}$."
			f" Giao tuyến giữa hai mặt phẳng $({S}{A}{D})$ và $({B}{C}{D})$ là đường thẳng nào trong các đường thẳng sau?")
		
		kq=f"${{{A}{D}}}$"
		kq2=random.choice([f"${{{A}{C}}}$",f"${{{S}{B}}}$" ])
		kq3=random.choice([f"${{{S}{A}}}$",f"${{{A}{B}}}$" ])
		kq4=random.choice([f"${{{B}{C}}}$", f"${{{B}{D}}}$"])
	
	

	noi_dung_loigiai=f"{kq} là khẳng định đúng."

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
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B1_05]-M2. Cho tứ diện. Tìm giao tuyến của các mặt phẳng
def ghj_7_jkl_L11_C4_B1_05():
	S=["S","A","O","S","O","S"]
	A=["A","B","A","A","B","B"]
	B=["B","C","B","C","C","C"]
	C=["C","D","C","D","D","D"]
	i=random.randint(0,5)
	S,A,B,C = S[i],A[i],B[i],C[i]
	M=random.choice(["M","E","P"])
	N=random.choice(["N","G","Q"])
	I=random.choice(["I","H"])
	K=random.choice(["K","F", "L"])

	code_hinh=code_hinh_tu_dien(S,A,B,C)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	chon=random.randint(1,4)
	
	if chon==1:
		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của các cạnh ${{{B}{C}, {A}{B}}}$."
		f" Gọi ${{{I}}}$ là giao điểm của ${{{A}{M}}}$ và ${{{C}{N}}}$."
		f" Giao tuyến của hai mặt phẳng $({S}{A}{I})$ và $({S}{B}{C})$ là đường thẳng")	

		kq=f"${{{S}{M}}}$"
			
		kq2=random.choice([
			f"${{{S}{N}}}$",
			f"${{{I}{N}}}$"
			])
		kq3=random.choice([
			f"${{{A}{M}}}$",
			f"${{{S}{C}}}$"
			])
		kq4=random.choice([
			f"${{{S}{B}}}$"
			])
		noi_dung_loigiai=(f"${S}\\in ({S}{A}{I}) \\cap ({S}{B}{C}), {M}\\in ({S}{A}{I}) \\cap ({S}{B}{C})$"
			f"$\\Rightarrow ({S}{A}{I}) \\cap ({S}{B}{C})={S}{M}$."	)
	
	if chon==2:

		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của các cạnh ${{{B}{C}, {A}{B}}}$."
		f" Gọi ${{{I}}}$ là giao điểm của ${{{A}{M}}}$ và ${{{C}{N}}}$."
		f" Giao tuyến của hai mặt phẳng $({S}{C}{I})$ và $({S}{A}{B})$ là đường thẳng")	

		kq=f"${{{S}{N}}}$"
			
		kq2=random.choice([
			f"${{{S}{M}}}$",
			f"${{{I}{N}}}$"
			])
		kq3=random.choice([
			f"${{{A}{M}}}$",
			f"${{{S}{C}}}$"
			])
		kq4=random.choice([
			f"${{{S}{B}}}$"
			])
		noi_dung_loigiai=(f"${S}\\in ({S}{C}{I}) \\cap ({S}{A}{B}), {N}\\in ({S}{C}{I}) \\cap ({S}{A}{B})$"
			f"$\\Rightarrow ({S}{C}{I}) \\cap ({S}{A}{B})={S}{N}$.")

	if chon==3:

		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của các cạnh ${{{B}{C}, {A}{B}}}$."
		f" Gọi ${{{I}}}$ là giao điểm của ${{{A}{M}}}$ và ${{{C}{N}}}$."
		f" Giao tuyến của hai mặt phẳng $({S}{A}{M})$ và $({S}{C}{N})$ là đường thẳng")	

		kq=f"${{{S}{I}}}$"
			
		kq2=random.choice([
			f"${{{S}{M}}}$",
			f"${{{I}{N}}}$",
			f"${{{I}{M}}}$"
			])
		kq3=random.choice([
			f"${{{A}{M}}}$",
			f"${{{A}{N}}}$",
			f"${{{S}{C}}}$",
			f"${{{S}{A}}}$",
			])
		kq4=random.choice([
			f"${{{S}{B}}}$",
			f"${{{S}{N}}}$"
			])
		noi_dung_loigiai=(f"${S}\\in ({S}{A}{M}) \\cap ({S}{C}{N}), {I}={A}{M}\\cap {C}{N}\\Rightarrow {I}\\in ({S}{A}{M}) \\cap ({S}{C}{N})$"
			f"$\\Rightarrow ({S}{A}{M}) \\cap ({S}{C}{N})={S}{I}$.")
	
	if chon==4:
		ti_so=random.choice([f"{B}{I}=2{I}{C}", f"{B}{I}=\\dfrac{{2}}{{3}}{B}{C}", f"{I}{B}=2{I}{C}", f"{I}{B}=3{I}{C}"])
		noi_dung=(f"Cho tứ diện ${{{S}{A}{B}{C}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của các cạnh ${{{A}{B}, {S}{A}}}$."
		f" Gọi ${{{I}}}$ là điểm thuộc cạnh ${{{B}{C}}}$ sao cho ${B}{I}=2{I}{C}$."
		f" Gọi ${{{K}}}$ là giao điểm của các đường thẳng ${{{M}{I}}}$ và ${{{A}{C}}}$."
		f" Giao tuyến của hai mặt phẳng $({S}{A}{C})$ và $({M}{N}{I})$ là đường thẳng")	

		kq=f"${{{N}{K}}}$"
			
		kq2=random.choice([
			f"${{{S}{M}}}$",
			f"${{{I}{N}}}$",
			f"${{{I}{M}}}$"
			])
		kq3=random.choice([
			f"${{{A}{M}}}$",
			f"${{{A}{N}}}$",
			f"${{{S}{C}}}$",
			f"${{{S}{A}}}$",
			])
		kq4=random.choice([
			f"${{{M}{I}}}$",
			f"${{{M}{K}}}$"
			])
		noi_dung_loigiai=(f"${N}\\in ({S}{A}{C}) \\cap ({M}{N}{I}), {K}={M}{I}\\cap {A}{C}\\Rightarrow {K}\\in ({S}{A}{C}) \\cap ({M}{N}{I})$"
			f"$\\Rightarrow ({S}{A}{C}) \\cap ({M}{N}{I})={N}{K}$.")
	
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
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B1_06]-M2. Cho hình chóp đáy là h.b.h.Tìm giao điểm đường thẳng - mặt phẳng
def ghj_7_jkl_L11_C4_B1_06():
	S=["S","S","S","S","S","S"]
	A=["A","A","A","B","A","B"]
	B=["B","B","B","C","B","C"]
	C=["C","C","M","D","E","E"]
	D=["D","D","N","E","F","F"]
	i=random.randint(0,5)

	S,A,B,C,D = S[i],A[i],B[i],C[i],D[i]
	O=random.choice(["O", "H", "G"])
	I=random.choice(["I", "P"])
	K=random.choice(["K", "Q"])

	code_hinh=code_hinh_chop_deu(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	chon=random.randint(1,5)
	
	if chon==1:
		noi_dung=(f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là hình bình hành tâm ${{{O}}}$."
	f" Gọi ${{{I},{K}}}$ lần lượt là trung điểm của các cạnh ${{{B}{C}}}$ và ${{{C}{D}}}$."
	f" Giao điểm của đường thẳng ${{{A}{O}}}$ và mặt phẳng $({{{S}{B}{C}}})$ là điểm nào trong các điểm sau" )

		noi_dung_loigiai=f"${A}{O} \\cap {B}{C}={C} \\Rightarrow {A}{O} \\cap ({{{S}{B}{C}}})={C}$."

		kq=f"{C}"

		kq2=random.choice([f"{B}",f"{I}"])

		kq3=random.choice([f"{S}", f"{K}"])

		kq4=random.choice([f"{A}"])

	if chon==2:
		noi_dung=(f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là hình bình hành tâm ${{{O}}}$."
	f" Gọi ${{{I},{K}}}$ lần lượt là trung điểm của các cạnh ${{{B}{C}}}$ và ${{{C}{D}}}$."
	f" Giao điểm của đường thẳng ${{{B}{O}}}$ và mặt phẳng $({{{S}{C}{D}}})$ là điểm nào trong các điểm sau" )

		noi_dung_loigiai=f"${B}{O} \\cap {C}{D}={D} \\Rightarrow {B}{O} \\cap ({{{S}{C}{D}}})={D}$."

		kq=f"{D}"

		kq2=random.choice([f"{B}",f"{I}"])

		kq3=random.choice([f"{S}", f"{K}"])

		kq4=random.choice([f"{A}",f"{C}"])

	if chon==3:
		noi_dung=(f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là hình bình hành tâm ${{{O}}}$."
	f" Gọi ${{{I},{K}}}$ lần lượt là trung điểm của các cạnh ${{{B}{C}}}$ và ${{{C}{D}}}$."
	f" Giao điểm của đường thẳng ${{{A}{C}}}$ và mặt phẳng $({{{S}{B}{D}}})$ là điểm nào trong các điểm sau" )

		noi_dung_loigiai=f"${A}{C} \\cap {B}{D}={O} \\Rightarrow {A}{C} \\cap ({{{S}{B}{D}}})={O}$."

		kq=f"{O}"

		kq2=random.choice([f"{B}",f"{I}"])

		kq3=random.choice([f"{S}", f"{K}"])

		kq4=random.choice([f"{D}",f"{C}"])

	if chon==4:
		noi_dung=(f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là hình bình hành tâm ${{{O}}}$."
	f" Gọi ${{{I},{K}}}$ lần lượt là trung điểm của các cạnh ${{{B}{C}}}$ và ${{{C}{D}}}$."
	f" Giao điểm của đường thẳng ${{{B}{D}}}$ và mặt phẳng $({{{S}{A}{C}}})$ là điểm nào trong các điểm sau" )

		noi_dung_loigiai=f"${B}{D} \\cap {A}{C}={O} \\Rightarrow {B}{D} \\cap ({{{S}{A}{C}}})={O}$."

		kq=f"{O}"

		kq2=random.choice([f"{B}",f"{I}"])

		kq3=random.choice([f"{S}", f"{K}"])

		kq4=random.choice([f"{D}",f"{C}"])
	
	if chon==5:
		noi_dung=(f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là hình bình hành tâm ${{{O}}}$."
	f" Gọi ${{{I}}}$ là trung điểm của các cạnh ${{{C}{D}}}$ và ${{{K}}}$ là giao điểm của ${{{A}{I}}}$ và ${{{B}{D}}}$."
	f" Giao điểm của đường thẳng ${{{A}{I}}}$ và mặt phẳng $({{{S}{B}{O}}})$ là điểm nào trong các điểm sau" )

		noi_dung_loigiai=f"${A}{I} \\cap {B}{O}={K} \\Rightarrow {A}{I} \\cap ({{{S}{B}{O}}})={K}$."

		kq=f"{K}"

		kq2=random.choice([f"{B}",f"{I}"])

		kq3=random.choice([f"{S}", f"{O}"])

		kq4=random.choice([f"{C}",f"{A}"])	

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	#random.shuffle(list_PA)
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
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#Bài 2 - Hai đường thẳng song song

#[D11_C4_B2_01]. Cho hình chóp-hbh. Tìm hai đường thẳng song song.
def ghj_7_jkl_L11_C4_B2_01():
	ten_hinhchop=random.choice(["S.ABCD"])
	hinh=random.choice(["hình bình hành", "hình vuông", "hình chữ nhật", "hình thoi"])
	diem_1 = random.choice(["M","I","G","P"])
	diem_2 = random.choice(["N","K","H","Q"]) 
	canh= random.choice(["${SA}$ và ${SB}$","${SB}$ và ${SC}$","${SC}$ và ${SD}$", "${SA}$ và ${SC}$"])
	if canh=="${SA}$ và ${SB}$":
		kq=f"${{{diem_1}{diem_2}}}$//${{CD}}$"
		kq2=f"${{{diem_1}{diem_2}}}$//${{BC}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{AD}}$", f"${{{diem_1}{diem_2}}}$//${{SC}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{BD}}$", f"${{{diem_1}{diem_2}}}$//${{SD}}$"])

	elif canh=="${SB}$ và ${SC}$":
		kq=f"${{{diem_1}{diem_2}}}$//${{AD}}$"
		kq2=f"${{{diem_1}{diem_2}}}$//${{AB}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{BD}}$", f"${{{diem_1}{diem_2}}}$//${{SD}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{CD}}$", f"${{{diem_1}{diem_2}}}$//${{SA}}$"])	

	elif canh=="${SC}$ và ${SD}$":
		kq=f"${{{diem_1}{diem_2}}}$//${{AB}}$"
		kq2=f"${{{diem_1}{diem_2}}}$//${{BC}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{AC}}$", f"${{{diem_1}{diem_2}}}$//${{SB}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{BD}}$", f"${{{diem_1}{diem_2}}}$//${{SA}}$"])
	else:
		kq=f"${{{diem_1}{diem_2}}}$//${{AC}}$"
		kq2=f"${{{diem_1}{diem_2}}}$//${{BC}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{AD}}$", f"${{{diem_1}{diem_2}}}$//${{SB}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{BD}}$", f"${{{diem_1}{diem_2}}}$//${{SD}}$"])
	
	code=my_module.codelatex_hinhchop_hbh_canhvg("S","A","B","C","D")
	file_name=my_module.pdftoimage_timename(code)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình chóp ${{{ten_hinhchop}}}$ có đáy là {hinh}. Gọi ${{{diem_1}}}$ và ${{{diem_2}}}$ lần lượt là trung điểm của các cạnh {canh}.Tìm khẳng định đúng." 

	debai= f"{noi_dung}\n\n"\
	    f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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

#[D11_C4_B2_02]-M2. Cho tứ diện. Xét quan hệ song song, chéo nhau, cắt nhau
def ghj_7_jkl_L11_C4_B2_02():
	A=["A","O","S","S","S"]
	B=["B","A","A","B","O"]
	C=["C","B","B","C","A"]
	D=["D","C","C","D","B"]
	i=random.randint(0,4)
	A, B, C, D = A[i], B[i], C[i], D[i]

	M=random.choice(["M","E","I" ])
	N=random.choice(["N","F","J" ])
	P=random.choice(["P","G","K" ])
	Q=random.choice(["Q","H","L" ])
	t=random.randint(2,3)

	code_hinh=code_hinh_tu_dien(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(
		f"Cho tứ diện ${{{A}{B}{C}{D}}}$. Gọi ${{{M},{N},{Q}}}$ lần lượt là trung điểm của các cạnh ${{{A}{B},{B}{C}}}$ và ${{{A}{D}}}$."
		f" Gọi ${{{P}}}$ là điểm thuộc cạnh ${{{C}{D}}}$ sao cho ${{{P}{C}={t}{P}{D}}}$. Tìm khẳng định đúng trong các khẳng định sau."
		)
		

		kq=random.choice([
			f"${{{A}{B}}}$ và ${{{C}{D}}}$ chéo nhau",
			f"${{{A}{C}}}$ và ${{{B}{D}}}$ chéo nhau",
			f"${{{A}{D}}}$ và ${{{B}{C}}}$ chéo nhau",
			f"${{{A}{N}}}$ và ${{{B}{D}}}$ chéo nhau",
			f"${{{A}{M}}}$ và ${{{C}{P}}}$ chéo nhau",
			f"${{{D}{N}}}$ và ${{{A}{C}}}$ chéo nhau",
			f"${{{B}{P}}}$ và ${{{A}{D}}}$ chéo nhau",

			f"${{{M}{N}}}$ và ${{{A}{C}}}$ song song",
			f"${{{M}{Q}}}$ và ${{{B}{D}}}$ song song",

			f"${{{A}{M}}}$ và ${{{C}{N}}}$ cắt nhau",
			f"${{{C}{P}}}$ và ${{{A}{Q}}}$ cắt nhau",
			f"${{{A}{Q}}}$ và ${{{D}{P}}}$ cắt nhau",
			f"${{{N}{P}}}$ và ${{{B}{D}}}$ cắt nhau",
			f"${{{Q}{P}}}$ và ${{{A}{C}}}$ cắt nhau"
			])
		kq_false=[
			f"${{{A}{B}}}$ và ${{{C}{D}}}$ cắt nhau",
			f"${{{N}{P}}}$ và ${{{A}{C}}}$ cắt nhau",
			f"${{{M}{P}}}$ và ${{{A}{D}}}$ cắt nhau",
			f"${{{N}{Q}}}$ và ${{{B}{D}}}$ cắt nhau",
			f"${{{C}{Q}}}$ và ${{{A}{B}}}$ cắt nhau",

			f"${{{M}{Q}}}$ và ${{{N}{P}}}$ song song",
			f"${{{P}{Q}}}$ và ${{{A}{C}}}$ song song",
			f"${{{P}{M}}}$ và ${{{A}{D}}}$ song song",
			f"${{{B}{N}}}$ và ${{{P}{Q}}}$ song song",
			f"${{{B}{Q}}}$ và ${{{C}{D}}}$ song song"

		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]
		noi_dung_loigiai=(
		f"{kq} là khẳng định đúng."
		)
	
	if chon==2:
		noi_dung=(
		f"Cho tứ diện ${{{A}{B}{C}{D}}}$. Gọi ${{{M},{N},{Q}}}$ lần lượt là trung điểm của các cạnh ${{{A}{B},{B}{C}}}$ và ${{{A}{D}}}$."
		f" Gọi ${{{P}}}$ là điểm thuộc cạnh ${{{C}{D}}}$ sao cho ${{{P}{C}={t}{P}{D}}}$. Tìm khẳng định sai trong các khẳng định sau."
		)		

		kq=random.choice([
			f"${{{A}{B}}}$ và ${{{C}{D}}}$ cắt nhau",
			f"${{{N}{P}}}$ và ${{{A}{C}}}$ cắt nhau",
			f"${{{M}{P}}}$ và ${{{A}{D}}}$ cắt nhau",
			f"${{{N}{Q}}}$ và ${{{B}{D}}}$ cắt nhau",
			f"${{{C}{Q}}}$ và ${{{A}{B}}}$ cắt nhau",

			f"${{{M}{Q}}}$ và ${{{N}{P}}}$ song song",
			f"${{{P}{Q}}}$ và ${{{A}{C}}}$ song song",
			f"${{{P}{M}}}$ và ${{{A}{D}}}$ song song",
			f"${{{B}{N}}}$ và ${{{P}{Q}}}$ song song",
			f"${{{B}{Q}}}$ và ${{{C}{D}}}$ song song"			
			])
		kq_false=[
			f"${{{A}{B}}}$ và ${{{C}{D}}}$ chéo nhau",
			f"${{{A}{C}}}$ và ${{{B}{D}}}$ chéo nhau",
			f"${{{A}{D}}}$ và ${{{B}{C}}}$ chéo nhau",
			f"${{{A}{N}}}$ và ${{{B}{D}}}$ chéo nhau",
			f"${{{A}{M}}}$ và ${{{C}{P}}}$ chéo nhau",
			f"${{{D}{N}}}$ và ${{{A}{C}}}$ chéo nhau",
			f"${{{B}{P}}}$ và ${{{A}{D}}}$ chéo nhau",

			f"${{{M}{N}}}$ và ${{{A}{C}}}$ song song",
			f"${{{M}{Q}}}$ và ${{{B}{D}}}$ song song",

			f"${{{A}{M}}}$ và ${{{C}{N}}}$ cắt nhau",
			f"${{{C}{P}}}$ và ${{{A}{Q}}}$ cắt nhau",
			f"${{{A}{Q}}}$ và ${{{D}{P}}}$ cắt nhau",
			f"${{{N}{P}}}$ và ${{{B}{D}}}$ cắt nhau",
			f"${{{Q}{P}}}$ và ${{{A}{C}}}$ cắt nhau"
		
		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]
		noi_dung_loigiai=(
		f"{kq} là khẳng định sai."
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

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B2_03]-M2. Cho a nằm trong (P) và b//(P). Tìm khẳng định đúng hoặc sai
def ghj_7_jkl_L11_C4_B2_03():
	name_lines=["a","m","d","b","n","\\Delta"]
	random.shuffle(name_lines)
	a,b=name_lines[0:2]
	P=random.choice(["(P)","(Q)","(R)", "(\\alpha)", "(\\beta)", "(\\gamma)"])
	M=random.choice(["A","B","M","N", "E","F","I","H",])
	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(
		f"Trong không gian cho đường thẳng ${{{a}}}$ chứa trong mặt phẳng ${{{P}}}$,"
		f" điểm ${{{M}}}$ thuộc mặt phẳng ${{{P}}}$,"
		f" đường thẳng ${{{b}}}$ và mặt phẳng ${{{P}}}$ không có điểm chung."		
		f" Tìm khẳng định đúng trong các khẳng định sau."
		)	

		kq=random.choice([
		f"${{{a}}}$ và ${{{b}}}$ không có điểm chung",		
		f"Điểm ${{{M}}}$ không thuộc đường thẳng ${{{b}}}$",
		f"Điểm ${{{M}}}$ và ${{{a}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{b}}}$ và song song với ${{{a}}}$"
		 ])
		kq_false=[
		f"${{{a}}}$ và ${{{b}}}$ song song",
		f"${{{a}}}$ và ${{{b}}}$ chéo nhau",
		f"${{{a}}}$ và ${{{b}}}$ cắt nhau",
		f"Điểm ${{{M}}}$ thuộc đường thẳng ${{{a}}}$",
		f"${{{a}}}$ và ${{{b}}}$ cùng thuộc một mặt phẳng",
		f"Điểm ${{{M}}}$ và ${{{b}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{M}}}$ và song song với ${{{b}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{a}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{b}}}$"

		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
		f"{kq} là khẳng định đúng."
		)
	
	if chon==2:
		noi_dung=(
		f"Trong không gian cho đường thẳng ${{{a}}}$ chứa trong mặt phẳng ${{{P}}}$,"
		f" điểm ${{{M}}}$ thuộc mặt phẳng ${{{P}}}$,"
		f" đường thẳng ${{{b}}}$ và mặt phẳng ${{{P}}}$ không có điểm chung."
		f" Tìm khẳng định sai trong các khẳng định sau."
		)	

		kq=random.choice([
		f"${{{a}}}$ và ${{{b}}}$ song song",
		f"${{{a}}}$ và ${{{b}}}$ chéo nhau",
		f"${{{a}}}$ và ${{{b}}}$ cắt nhau",
		f"Điểm ${{{M}}}$ thuộc đường thẳng ${{{a}}}$",
		f"${{{a}}}$ và ${{{b}}}$ cùng thuộc một mặt phẳng",
		f"Điểm ${{{M}}}$ và ${{{b}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{M}}}$ và song song với ${{{b}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{a}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{b}}}$"
		
		 ])
		kq_false=[
		f"${{{a}}}$ và ${{{b}}}$ không có điểm chung",		
		f"Điểm ${{{M}}}$ không thuộc đường thẳng ${{{b}}}$",
		f"Điểm ${{{M}}}$ và ${{{a}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{b}}}$ và song song với ${{{a}}}$",


		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
		f"{kq} là khẳng định sai."
		)
	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


def ghj_7_jkl_L11_C4_B2_04():
	a=random.choice(["a","m","d"])
	b=random.choice(["b","n","\\Delta" ])
	P=random.choice(["(P)","(Q)","(R)", "(\\alpha)", "(\\beta)", "(\\gamma)"])
	M=random.choice(["M","E","F"])
	N=random.choice(["N","K","G"])
	A=random.choice(["A","C","I"])
	B=random.choice(["B","D","H"])
	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(
			f"Trong không gian cho đường thẳng ${{{a}}}$ chứa trong mặt phẳng ${{{P}}}$, ${{{a}}}$ qua hai điểm ${{{A},{B}}}$ phân biệt."
			f" Đường thẳng ${{{b}}}$ cắt mặt phẳng ${{{P}}}$ tại điểm ${{{M}}}$"
			f" và ${{{M}}}$ không thuộc ${{{a}}}$. Gọi ${{{N}}}$ là điểm bất kì thuộc ${{{b}}}$ và không trùng với điểm ${{{M}}}$."
			f" Tìm khẳng định đúng trong các khẳng định sau."
		)
		

		kq=random.choice([
			f"${{{a}}}$ và ${{{b}}}$ chéo nhau",
			f"${{{M},{A},{B}}}$ đồng phẳng",
			f"${{{N},{A},{B}}}$ đồng phẳng",
			f"${{{A}{B}}}$ và ${{{M}{N}}}$ chéo nhau",
			f"${{{N}{A}}}$ không chứa trong mặt phẳng ${{{P}}}$",
			f"${{{N}{B}}}$ không chứa trong mặt phẳng ${{{P}}}$",
			f"${{{A},{B},{M},{N}}}$ không đồng phẳng",
			f"${{{N}{A}}}$ và ${{{M}{B}}}$ chéo nhau",
			f"${{{N}}}$ không thuộc mặt phẳng ${{{P}}}$",
			f"${{{M}}}$ không thuộc mặt phẳng ${{({A}{B}{N})}}$",
			])
		kq_false=[
			f"${{{a}}}$ và ${{{b}}}$ cắt nhau",
			f"${{{a}}}$ và ${{{b}}}$ song song",
			f"${{{a}}}$ và ${{{b}}}$ trùng nhau",
			f"${{{A}{N}}}$ và ${{{B}{M}}}$ cắt nhau",
			f"${{{A}{M}}}$ và ${{{B}{N}}}$ cắt nhau",
			f"${{{N}}}$ thuộc mặt phẳng ${{{P}}}$",
			f"${{{N}}}$ thuộc mặt phẳng ${{({A}{B}{M})}}$"		
		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
		f"{kq} là khẳng định đúng."
		)
	
	if chon==2:
		noi_dung=(
			f"Trong không gian cho đường thẳng ${{{a}}}$ chứa trong mặt phẳng ${{{P}}}$, ${{{a}}}$ qua hai điểm ${{{A},{B}}}$ phân biệt."
			f" Đường thẳng ${{{b}}}$ cắt mặt phẳng ${{{P}}}$ tại điểm ${{{M}}}$"
			f" và ${{{M}}}$ không thuộc ${{{a}}}$. Gọi ${{{N}}}$ là điểm bất kì thuộc ${{{b}}}$ và không trùng với điểm ${{{M}}}$."
			f" Tìm khẳng định sai trong các khẳng định sau."
		)
		

		kq=random.choice([
			f"${{{a}}}$ và ${{{b}}}$ cắt nhau",
			f"${{{a}}}$ và ${{{b}}}$ song song",
			f"${{{a}}}$ và ${{{b}}}$ trùng nhau",
			f"${{{A}{N}}}$ và ${{{B}{M}}}$ cắt nhau",
			f"${{{A}{M}}}$ và ${{{B}{N}}}$ cắt nhau",
			f"${{{N}}}$ thuộc mặt phẳng ${{{P}}}$",
			f"${{{N}}}$ thuộc mặt phẳng ${{({A}{B}{M})}}$"			
			])
		kq_false=[			

			f"${{{a}}}$ và ${{{b}}}$ chéo nhau",
			f"${{{M},{A},{B}}}$ đồng phẳng",
			f"${{{N},{A},{B}}}$ đồng phẳng",
			f"${{{A}{B}}}$ và ${{{M}{N}}}$ chéo nhau",
			f"${{{N}{A}}}$ không chứa trong mặt phẳng ${{{P}}}$",
			f"${{{N}{B}}}$ không chứa trong mặt phẳng ${{{P}}}$",
			f"${{{A},{B},{M},{N}}}$ không đồng phẳng",
			f"${{{N}{A}}}$ và ${{{M}{B}}}$ chéo nhau",
			f"${{{N}}}$ không thuộc mặt phẳng ${{{P}}}$",
			f"${{{M}}}$ không thuộc mặt phẳng ${{({A}{B}{N})}}$"
		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
		f"{kq} là khẳng định sai."
		)

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B2_05]-M3. Cho hình chóp tam giác. Tìm khẳng định đúng về song song, cắt nhau, chéo nhau
def ghj_7_jkl_L11_C4_B2_05():
	S=["A","O","S","S","S"]
	A=["B","A","A","B","O"]
	B=["C","B","B","C","A"]
	C=["D","C","C","D","B"]
	i=random.randint(0,4)
	S,A,B,C = S[i], A[i], B[i], C[i]

	trong_tam=["G","I","K","H"]
	random.shuffle(trong_tam)
	G,K=trong_tam[0:2]

	trung_diem=["M","P","E","N","Q","F"]
	random.shuffle(trung_diem)
	M,N=trung_diem[0:2]

	code_hinh=code_hinh_tu_dien(S,A,B,C)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của các cạnh ${{{A}{B},{A}{C}}}$."
		f" Gọi ${{{G},{K}}}$ lần lượt là trọng tâm của các tam giác ${{{S}{A}{B},{S}{A}{C}}}$."
		f" Khẳng định nào sau đây là đúng?"
		)	

		kq=random.choice([
			f"${{{G}{K}}}$ và ${{{A}{C}}}$ song song",
			f"${{{G}{K}}}$ và ${{{M}{N}}}$ song song",
			f"${{{M}{N}}}$ và ${{{A}{C}}}$ song song",

			f"${{{G}{M}}}$ và ${{{N}{K}}}$ cắt nhau",
			f"${{{G}{N}}}$ và ${{{M}{K}}}$ cắt nhau",
			f"${{{S}{G}}}$ và ${{{A}{B}}}$ cắt nhau",
			f"${{{A}{M}}}$ và ${{{C}{N}}}$ cắt nhau",

			f"${{{S}{C}}}$ và ${{{A}{B}}}$ chéo nhau",
			f"${{{S}{B}}}$ và ${{{A}{C}}}$ chéo nhau",
			f"${{{S}{M}}}$ và ${{{A}{N}}}$ chéo nhau",
			f"${{{S}{N}}}$ và ${{{C}{M}}}$ chéo nhau",
			])

		kq_false=[
			f"${{{S}{G}}}$ và ${{{B}{C}}}$ cắt nhau",
			f"${{{S}{K}}}$ và ${{{A}{C}}}$ cắt nhau",			
			f"${{{S}{B}}}$ và ${{{M}{N}}}$ cắt nhau",

			f"${{{M}{K}}}$ và ${{{B}{C}}}$ song song",
			f"${{{N}{G}}}$ và ${{{A}{B}}}$ song song",
			f"${{{A}{G}}}$ và ${{{M}{K}}}$ song song",
			f"${{{C}{M}}}$ và ${{{G}{K}}}$ song song",
			f"${{{A}{N}}}$ và ${{{G}{K}}}$ song song",

			f"${{{A}{G}}}$ và ${{{S}{B}}}$ chéo nhau",
			f"${{{A}{N}}}$ và ${{{C}{M}}}$ chéo nhau",
			f"${{{C}{K}}}$ và ${{{B}{N}}}$ chéo nhau",
			f"${{{B}{C}}}$ và ${{{S}{K}}}$ chéo nhau",
			]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]


		noi_dung_loigiai=(
		f"{kq} là khẳng định đúng."
		)
	
	if chon==2:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của các cạnh ${{{A}{B},{A}{C}}}$."
		f" Gọi ${{{G},{K}}}$ lần lượt là trọng tâm của các tam giác ${{{S}{A}{B},{S}{A}{C}}}$."
		f" Khẳng định nào sau đây là sai?"
		)	

		kq=random.choice([
			f"${{{S}{G}}}$ và ${{{B}{C}}}$ cắt nhau",
			f"${{{S}{K}}}$ và ${{{A}{C}}}$ cắt nhau",			
			f"${{{S}{B}}}$ và ${{{M}{N}}}$ cắt nhau",

			f"${{{M}{K}}}$ và ${{{B}{C}}}$ song song",
			f"${{{N}{G}}}$ và ${{{A}{B}}}$ song song",
			f"${{{A}{G}}}$ và ${{{M}{K}}}$ song song",
			f"${{{C}{M}}}$ và ${{{G}{K}}}$ song song",
			f"${{{A}{N}}}$ và ${{{G}{K}}}$ song song",

			f"${{{A}{G}}}$ và ${{{S}{B}}}$ chéo nhau",
			f"${{{A}{N}}}$ và ${{{C}{M}}}$ chéo nhau",
			f"${{{C}{K}}}$ và ${{{B}{N}}}$ chéo nhau",
			f"${{{B}{C}}}$ và ${{{S}{K}}}$ chéo nhau",
			f"${{{M}{N}}}$ và ${{{A}{C}}}$ song song",
			
			])
		kq_false=[
			f"${{{G}{K}}}$ và ${{{A}{C}}}$ song song",
			f"${{{G}{K}}}$ và ${{{M}{N}}}$ song song",			

			f"${{{G}{M}}}$ và ${{{N}{K}}}$ cắt nhau",
			f"${{{G}{N}}}$ và ${{{M}{K}}}$ cắt nhau",
			f"${{{S}{G}}}$ và ${{{A}{B}}}$ cắt nhau",
			f"${{{A}{M}}}$ và ${{{C}{N}}}$ cắt nhau",

			f"${{{S}{C}}}$ và ${{{A}{B}}}$ chéo nhau",
			f"${{{S}{B}}}$ và ${{{A}{C}}}$ chéo nhau",
			f"${{{S}{M}}}$ và ${{{A}{N}}}$ chéo nhau",
			f"${{{S}{N}}}$ và ${{{C}{M}}}$ chéo nhau",			
			]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]


		noi_dung_loigiai=(
		f"{kq} là khẳng định sai."
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

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B2_06]-M2. Cho hình chóp tam giác. Tìm cặp đường song song
def ghj_7_jkl_L11_C4_B2_06():
	S=["A","O","S","S","S"]
	A=["B","A","A","B","O"]
	B=["C","B","B","C","A"]
	C=["D","C","C","D","B"]
	i=random.randint(0,4)
	S,A,B,C = S[i], A[i], B[i], C[i]

	trong_tam=["G","I","K","H"]
	random.shuffle(trong_tam)
	G,K=trong_tam[0:2]

	trung_diem=["M","P","E","N","Q","F"]
	random.shuffle(trung_diem)
	M,N=trung_diem[0:2]

	code_hinh=code_hinh_tu_dien_noname(S,A,B,C)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của các cạnh ${{{A}{B},{A}{C}}}$."
		f" Gọi ${{{G},{K}}}$ lần lượt là trọng tâm của các tam giác ${{{S}{A}{B},{S}{A}{C}}}$."
		f" Khẳng định nào sau đây là đúng?"
		)

		kq=random.choice([
			f"${{{G}{K}}}$ // ${{{A}{C}}}$",
			f"${{{G}{K}}}$ // ${{{M}{N}}}$",
			f"${{{M}{N}}}$ // ${{{A}{C}}}$"])

		kq_false=[
			f"${{{S}{G}}}$ // ${{{B}{C}}}$",
			f"${{{S}{K}}}$ // ${{{A}{C}}}$",
			f"${{{S}{K}}}$ // ${{{A}{B}}}$",
			f"${{{S}{B}}}$ // ${{{M}{N}}}$",

			f"${{{M}{K}}}$ // ${{{B}{C}}}$",
			f"${{{N}{G}}}$ // ${{{A}{B}}}$",
			f"${{{A}{G}}}$ // ${{{M}{K}}}$",
			f"${{{C}{M}}}$ // ${{{G}{K}}}$",
			f"${{{A}{N}}}$ // ${{{G}{K}}}$",
			]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		if kq==f"${{{M}{N}}}$ // ${{{A}{C}}}$":
			noi_dung_loigiai=(
				f"${{{M}{N}}}$ là đường trung bình của tam giác ${{{A}{B}{C}}}$ nên ${{{M}{N}}}$ // ${{{A}{C}}}$.")

		if kq==f"${{{G}{K}}}$ // ${{{M}{N}}}$":
			noi_dung_loigiai=(
				f"$\\dfrac{{{S}{G}}}{{{S}{M}}}=\\dfrac{{{S}{K}}}{{{S}{N}}}=\\dfrac{{2}}{{3}} \\Rightarrow {G}{K}$ // ${{{M}{N}}}$.")

		if kq==f"${{{G}{K}}}$ // ${{{A}{C}}}$":
			noi_dung_loigiai=(
				f"$\\dfrac{{{S}{G}}}{{{S}{M}}}=\\dfrac{{{S}{K}}}{{{S}{N}}}=\\dfrac{{2}}{{3}} \\Rightarrow {G}{K}$ // ${{{M}{N}}}$.\n\n"
				f"${{{M}{N}}}$ là đường trung bình của tam giác ${{{A}{B}{C}}}$ nên ${{{M}{N}}}$ // ${{{A}{C}}}$.\n\n"
				f" Suy ra ${{{G}{K}}}$ // ${{{A}{C}}}$.")
	
	if chon==2:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}}}$."
		f" Gọi ${{{G},{K}}}$ lần lượt là trọng tâm của các tam giác ${{{S}{A}{B},{A}{B}{C}}}$."
		f" Khẳng định nào sau đây là đúng?"
		)
		kq=random.choice([			
			f"${{{S}{C}}}$ // ${{{G}{K}}}$",
			f"${{{S}{C}}}$ // ${{{K}{G}}}$",
			f"${{{C}{S}}}$ // ${{{K}{G}}}$",
			f"${{{G}{K}}}$ // ${{{S}{C}}}$",
			])

		kq_false=[
			f"${{{G}{K}}}$ // ${{{S}{A}}}$",
			f"${{{G}{K}}}$ // ${{{S}{B}}}$",
			f"${{{S}{K}}}$ // ${{{A}{C}}}$",
			f"${{{A}{G}}}$ // ${{{B}{K}}}$",
			f"${{{A}{K}}}$ // ${{{S}{C}}}$",
			
			]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
			f"Gọi ${{J}}$ là trung điểm của ${{{A}{B}}}$.\n\n"
			f"$\\dfrac{{{S}{G}}}{{{S}J}}=\\dfrac{{{C}{K}}}{{{C}J}}=\\dfrac{{2}}{{3}} \\Rightarrow {G}{K}$ // ${{{S}{C}}}$.\n\n"
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
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B2_07]-M2. Cho hình chóp-hbh. Tìm cặp đường song song
def ghj_7_jkl_L11_C4_B2_07():
	S="S"
	vertex=random.choice([
		["A","B","C","D"],["A","B","C","E"],["B","C","D","E"], 
		["C","D","E","F"], ["A","B","E","F"], ["B","C","E","F"]])
	
	A,B,C,D=vertex

	name_points=["M","N","P","Q","G","H","J","K"]
	random.shuffle(name_points)
	M,N,G,H=name_points[0:4]
	
	O=random.choice(["O", "I"])

	name_bottom=random.choice(["hình bình hành", "hình chữ nhật", "hình thoi", "hình vuông" ])
	t=random.randint(2,3)

	code_hinh=code_hinh_chop_deu_noname(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	chon=random.randint(1,6)
	if chon==1:
		noi_dung=(
	f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
	f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các cạnh ${{{S}{A},{S}{B}}}$ sao cho ${M}{A}={t}{S}{M}, {N}{B}={t}{S}{N}$."
	f" Khẳng định nào sau đây là khẳng định đúng?")
	
	if chon==2:
		noi_dung=(
	f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
	f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các cạnh ${{{S}{A},{S}{B}}}$ sao cho ${M}{A}={t}{S}{M}, {S}{B}={t+1}{S}{N}$."
	f" Khẳng định nào sau đây là khẳng định đúng?")

	if chon==3:
		noi_dung=(
	f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
	f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các cạnh ${{{S}{A},{S}{B}}}$ sao cho ${S}{A}={t+1}{S}{M}, {N}{B}={t}{S}{N}$."
	f" Khẳng định nào sau đây là khẳng định đúng?")
	

	kq=random.choice([
		f"${{{M}{N}}}$ // ${{{A}{B}}}$",
		f"${{{A}{B}}}$  // ${{{M}{N}}}$",
		f"${{{M}{N}}}$ // ${{{C}{D}}}$",
		f"${{{C}{D}}}$ // ${{{M}{N}}}$"
		])

	kq_false=[
		f"${{{M}{N}}}$ // ${{{B}{C}}}$",
		f"${{{M}{C}}}$ // ${{{S}{B}}}$",
		f"${{{A}{N}}}$ // ${{{B}{D}}}$",
		f"${{{M}{D}}}$ // ${{{C}{N}}}$",
		f"${{{O}{M}}}$ // ${{{S}{A}}}$",
		f"${{{O}{M}}}$ // ${{{S}{C}}}$",
		f"${{{O}{N}}}$ // ${{{S}{C}}}$",
		f"${{{O}{N}}}$ // ${{{S}{D}}}$",
		f"${{{D}{N}}}$ // ${{{C}{M}}}$",
		]

	noi_dung_loigiai=(
	f"$\\dfrac{{{S}{M}}}{{{S}{A}}}=\\dfrac{{{S}{N}}}{{{S}{B}}}={phan_so(1/(t+1))}\\Rightarrow {M}{N}$ // ${{{A}{B}}}$ // ${{{C}{D}}}$."
	)
	if chon in [1,2,3]:
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!{round(t/(t+1),1)}!({S})$);\n\
		\\coordinate ({N}) at ($({B})!{round(t/(t+1),1)}!({S})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ;\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({O})--({M}) ({O})--({N}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"	
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)
	
	if chon==4:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các đoạn thẳng ${{{S}{A},{A}{C}}}$ sao cho ${A}{M}={t}{S}{M}, {A}{N}={t}{N}{C}$."
		f" Khẳng định nào sau đây là khẳng định đúng?")

		noi_dung_loigiai=(
		f"$\\dfrac{{{A}{M}}}{{{S}{A}}}=\\dfrac{{{A}{N}}}{{{A}{C}}}={phan_so(t/(t+1))}\\Rightarrow {M}{N}$ // ${{{S}{C}}}$."
		)
		kq=random.choice([
			f"${{{M}{N}}}$ // ${{{S}{C}}}$",
			f"${{{S}{C}}}$  // ${{{M}{N}}}$",
			])

		kq_false=[
			f"${{{M}{N}}}$ // ${{{B}{C}}}$",
			f"${{{M}{C}}}$ // ${{{S}{B}}}$",
			f"${{{A}{N}}}$ // ${{{B}{D}}}$",
			f"${{{M}{D}}}$ // ${{{C}{N}}}$",
			f"${{{O}{M}}}$ // ${{{S}{A}}}$",
			f"${{{O}{M}}}$ // ${{{S}{C}}}$",
			f"${{{O}{N}}}$ // ${{{S}{C}}}$",
			f"${{{O}{N}}}$ // ${{{S}{D}}}$",
			f"${{{D}{N}}}$ // ${{{C}{M}}}$",]

		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!{round(t/(t+1),1)}!({S})$);\n\
		\\coordinate ({N}) at ($({A})!{round(t/(t+1),1)}!({C})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ;\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"	
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

	if chon==5:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các đoạn thẳng ${{{S}{B},{B}{D}}}$ sao cho ${B}{M}={t}{S}{M}, {B}{N}={t}{N}{D}$."
		f" Khẳng định nào sau đây là khẳng định đúng?")

		noi_dung_loigiai=(
		f"$\\dfrac{{{B}{M}}}{{{S}{B}}}=\\dfrac{{{B}{N}}}{{{B}{D}}}={phan_so(t/(t+1))}\\Rightarrow {M}{N}$ // ${{{S}{D}}}$."
		)
		kq=random.choice([
			f"${{{M}{N}}}$ // ${{{S}{D}}}$",
			f"${{{S}{D}}}$  // ${{{M}{N}}}$",
			])

		kq_false=[
			f"${{{M}{N}}}$ // ${{{B}{C}}}$",
			f"${{{M}{C}}}$ // ${{{S}{B}}}$",
			f"${{{A}{N}}}$ // ${{{B}{D}}}$",
			f"${{{M}{D}}}$ // ${{{C}{N}}}$",
			f"${{{O}{M}}}$ // ${{{S}{A}}}$",
			f"${{{O}{M}}}$ // ${{{S}{C}}}$",
			f"${{{O}{N}}}$ // ${{{S}{C}}}$",
			f"${{{O}{N}}}$ // ${{{S}{D}}}$",
			f"${{{D}{N}}}$ // ${{{C}{M}}}$",]

		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!{round(1/(t+1),1)}!({B})$);\n\
		\\coordinate ({N}) at ($({S})!{round(1/(t+1),1)}!({D})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ;\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"	
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

	if chon==6:

		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là các trung điểm của ${{{A}{B},{C}{D}}}$"
		f" và ${{{G},{H}}}$ lần lượt là trọng tâm các tam giác ${{{S}{A}{B},{S}{C}{D}}}$."
		f" Khẳng định nào sau đây là khẳng định đúng?")
		
		chon=random.randint(1,2)
		if chon==1:
			kq=random.choice([
				f"${{{G}{H}}}$ // ${{{M}{N}}}$",
				f"${{{G}{H}}}$  // ${{{A}{D}}}$",
				f"${{{G}{H}}}$  // ${{{B}{C}}}$",
				f"${{{G}{H}}}$  // ${{{O}{M}}}$",
				f"${{{G}{H}}}$  // ${{{O}{N}}}$",				
				])
			noi_dung_loigiai=(
			f"$\\dfrac{{{S}{G}}}{{{S}{M}}}=\\dfrac{{{S}{H}}}{{{S}{N}}}={phan_so(2/3)}\\Rightarrow {G}{H}$ // ${{{M}{N}}}$.\n\n"
			f"Suy ra {kq} là khẳng định đúng."
		)
		
		if chon==2:
			kq=random.choice([				
				f"${{{M}{C}}}$  // ${{{A}{N}}}$",
				f"${{{D}{M}}}$  // ${{{B}{N}}}$",
				])
			noi_dung_loigiai=(			
			f"{kq} là khẳng định đúng.")		
		
		kq_false=[
			f"${{{G}{H}}}$ // ${{{C}{D}}}$",
			f"${{{G}{C}}}$ // ${{{A}{N}}}$",
			f"${{{H}{B}}}$ // ${{{A}{D}}}$",
			f"${{{H}{M}}}$ // ${{{B}{N}}}$",
			f"${{{O}{G}}}$ // ${{{S}{N}}}$",
			f"${{{O}{H}}}$ // ${{{S}{M}}}$",
			f"${{{M}{C}}}$ // ${{{G}{N}}}$",]

		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({C})!0.5!({D})$);\n\
		\\coordinate ({G}) at ($({S})!{2/3}!({M})$);\n\
		\\coordinate ({H}) at ($({S})!{2/3}!({N})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({S})--({M});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N}) ({G})--({H}) ({S})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90, {G}/-180, {H}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"	
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {file_name}\n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B2_08]-M2. Cho hình chóp-hbh. Tìm giao tuyến của 2 mặt chứa 2 đường song song
def ghj_7_jkl_L11_C4_B2_08():
	S="S"
	vertex=random.choice([
		["A","B","C","D"],["A","B","C","E"],["B","C","D","E"], 
		["C","D","E","F"], ["A","B","E","F"], ["B","C","E","F"]])
	
	A,B,C,D=vertex

	M=random.choice(["M", "G", "P"])
	N=random.choice(["N", "H", "Q" ])
	O=random.choice(["O", "I", "J" ])

	name_bottom=random.choice(["hình bình hành", "hình chữ nhật", "hình thoi", "hình vuông" ])
	
	code_hinh=code_hinh_chop_deu_noname(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	chon=random.randint(1,6)
	
	if chon==1:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom}."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{A}{B},{C}{D}}}$."
		f" Giao tuyến của hai mặt phẳng $({S}{A}{D})$ và $({S}{B}{C})$ là đường thẳng song song với đường thẳng nào sau đây?")
		kq=random.choice([f"{A}{D}",f"{B}{C}", f"{M}{N}"])
		kq_false=[
		f"{A}{C}", f"{B}{D}",f"{A}{B}",
		f"{C}{D}",f"{D}{M}",f"{B}{N}",
		]
		code_hinh_LG=code_hinh_chop_deu(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{A}{D}\\subset ({S}{A}{D}) \\\\ \n\
			{B}{C}\\subset ({S}{B}{C})\\\\ \n\
			{A}{D} // {B}{C} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({S}{A}{D}) \\cap ({S}{B}{C})=Sx // {A}{D} //{B}{C} //{M}{N}$."
			)

	if chon==2:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom}."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{A}{D},{B}{C}}}$."
		f" Giao tuyến của hai mặt phẳng $({S}{A}{B})$ và $({S}{C}{D})$ là đường thẳng song song với đường thẳng nào sau đây?")
		kq=random.choice([f"{A}{B}",f"{C}{D}", f"{M}{N}"])
		kq_false=[
		f"{A}{C}", f"{B}{D}",f"{A}{D}",
		f"{B}{C}",f"{D}{M}",f"{B}{N}",
		]
		code_hinh_LG=code_hinh_chop_deu(S,A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{A}{B}\\subset ({S}{A}{B}) \\\\ \n\
			{C}{D}\\subset ({S}{C}{D})\\\\ \n\
			{A}{B} // {C}{D} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({S}{A}{B}) \\cap ({S}{C}{D})=Sx // {A}{B} //{C}{D} //{M}{N}$.")	

	if chon==3:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{B}}}$."
		f" Giao tuyến của hai mặt phẳng $({O}{M}{N})$ và $({A}{B}{C}{D})$ là")

		kq=random.choice([
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{B}}}$",
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{C}{D}}}$",
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{B}{C}}}$",
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{B}{C}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{B}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{C}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{M}{N}}}$",		
		]
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!0.5!({A})$);\n\
		\\coordinate ({N}) at ($({S})!0.5!({B})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({M})--({N});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D});\n\
		\\draw[dashed,thin]({O})--({M}) ({O})--({N}) ;\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{O}/-90,{M}/180,{N}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{M}{N}\\subset ({O}{M}{N}) \\\\ \n\
			{A}{B}\\subset ({A}{B}{C}{D})\\\\ \n\
			{M}{N} // {A}{B} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({O}{M}{N}) \\cap ({A}{B}{C}{D})={O}x // {A}{B} //{M}{N} //{C}{D}$."
			)
	
	if chon==4:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{S}{B},{S}{C}}}$."
		f" Giao tuyến của hai mặt phẳng $({O}{M}{N})$ và $({A}{B}{C}{D})$ là")

		kq=random.choice([
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{D}}}$",			
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{B}}}$",
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{C}{D}}}$",		
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{B}{C}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{B}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{C}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{M}{N}}}$",		
		]
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({S})!0.5!({C})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({M})--({N});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D});\n\
		\\draw[dashed,thin]({O})--({M}) ({O})--({N}) ;\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{O}/-90,{M}/180,{N}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"
		
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{M}{N}\\subset ({O}{M}{N}) \\\\ \n\
			{B}{C}\\subset ({A}{B}{C}{D})\\\\ \n\
			{M}{N} // {B}{C} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({O}{M}{N}) \\cap ({A}{B}{C}{D})={O}x // {B}{C} //{M}{N} //{A}{D}$."
			)

	
	if chon==5:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{D}}}$."
		f" Giao tuyến của hai mặt phẳng $({O}{M}{N})$ và $({A}{B}{C}{D})$ là")

		kq=random.choice([
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{D}}}$",			
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{B}}}$",
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{C}{D}}}$",		
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{B}{C}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{B}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{C}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{M}{N}}}$",		
		]
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!0.5!({A})$);\n\
		\\coordinate ({N}) at ($({S})!0.5!({D})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ;\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D});\n\
		\\draw[dashed,thin]({O})--({M}) ({O})--({N}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{O}/-90,{M}/180,{N}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"
		
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{M}{N}\\subset ({O}{M}{N}) \\\\ \n\
			{A}{D}\\subset ({A}{B}{C}{D})\\\\ \n\
			{M}{N} // {A}{D} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({O}{M}{N}) \\cap ({A}{B}{C}{D})={O}x // {A}{D} //{M}{N} //{B}{C}$."
			)

	if chon==6:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{S}{C},{S}{D}}}$."
		f" Giao tuyến của hai mặt phẳng $({O}{M}{N})$ và $({A}{B}{C}{D})$ là")

		kq=random.choice([
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{B}}}$",
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{C}{D}}}$",
			f"đường thẳng qua ${{{O}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{B}{C}}}$",
		f"đường thẳng qua ${{{O}}}$ và song song với ${{{A}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{B}{C}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{A}{B}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{C}{D}}}$",
		f"đường thẳng qua ${{{S}}}$ và song song với ${{{M}{N}}}$",		
		]
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!0.5!({C})$);\n\
		\\coordinate ({N}) at ($({S})!0.5!({D})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ;\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D});\n\
		\\draw[dashed,thin]({O})--({M}) ({O})--({N}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{O}/-90,{M}/180,{N}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{M}{N}\\subset ({O}{M}{N}) \\\\ \n\
			{C}{D}\\subset ({A}{B}{C}{D})\\\\ \n\
			{M}{N} // {C}{D} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({O}{M}{N}) \\cap ({A}{B}{C}{D})={O}x // {C}{D} //{M}{N} //{A}{B}$.")


	#Xử lí phương án	
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	if chon in [1,2]:
		pa_A= f"*${{{kq}}}$"
		pa_B= f"${{{kq2}}}$"
		pa_C= f"${{{kq3}}}$"
		pa_D= f"${{{kq4}}}$"

		list_PA =[pa_A, pa_B, pa_C, pa_D]
		random.shuffle(list_PA)
		dap_an=my_module.tra_ve_dap_an(list_PA)		
		phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	if chon in [3,4,5,6]:
		pa_A= f"*{kq}"
		pa_B= f"{kq2}"
		pa_C= f"{kq3}"
		pa_D= f"{kq4}"

		list_PA =[pa_A, pa_B, pa_C, pa_D]
		random.shuffle(list_PA)
		dap_an=my_module.tra_ve_dap_an(list_PA)		
		phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
	#Trộn các phương án
	

	debai= f"{noi_dung}\n{file_name}\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {file_name_LG}\n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B2_09]-M2. Cho hình chóp tam giác. Tìm giao tuyến của 2 mặt chứa 2 đường song song
def ghj_7_jkl_L11_C4_B2_09():	
	vertex=random.choice([
		["A","B","C","D"],["S","A","B","C"],["B","C","D","E"], 
		["S","C","D","E"], ["A","B","E","F"], ["B","C","E","F"],["C","D","E","F"] ])
	
	A,B,C,D=vertex

	M=random.choice(["M", "I", "P"])
	N=random.choice(["N", "J", "Q" ])
	G=random.choice(["G", "O", "K"])

	code_hinh=code_hinh_tu_dien_noname(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	chon=random.randint(1,4)
	if chon==1:
		noi_dung=(
		f"Cho tứ diện ${{{A}{B}{C}{D}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{A}{B},{A}{D}}}$."
		f" Giao tuyến của hai mặt phẳng $({C}{M}{N})$ và $({B}{C}{D})$ là"
		)	

		kq=random.choice([
			f"đường thẳng qua ${{{C}}}$ và song song với ${{{B}{D}}}$",
			f"đường thẳng qua ${{{C}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
			f"đường thẳng qua ${{{B}}}$ và song song với ${{{C}{N}}}$",
			f"đường thẳng qua ${{{C}}}$ và song song với ${{{D}{M}}}$",
			f"đường thẳng qua ${{{M}}}$ và song song với ${{{C}{D}}}$",
			f"đường thẳng qua ${{{N}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{M}{N}}}$",]

		code_hinh_LG=(f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$) node at ({M}) [left] {{${M}$}};\n\
		\\coordinate ({N}) at ($({A})!0.5!({D})$) node at ({N}) [right] {{${N}$}};\n\
		\\draw [dashed] ({B})--({D}) ({M})--({N}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({C})--({M}) ({C})--({N}) ;\n\
		\\end{{tikzpicture}}\n")
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
				f"$\\left\\{{ \\begin{{array}}{{l}} \n\
				{M}{N}\\subset ({C}{M}{N}) \\\\ \n\
				{B}{D}\\subset ({B}{C}{D})\\\\ \n\
				{M}{N} // {B}{D} \n\
				\\end{{array}} \\right.$"
				f"$\\Rightarrow ({C}{M}{N}) \\cap ({A}{B}{C})={C}x // {M}{N} //{B}{D}$.")
		
	if chon==2:
		noi_dung=(
		f"Cho tứ diện ${{{A}{B}{C}{D}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{A}{B},{A}{D}}}$."
		f" Gọi ${{{G}}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$"
		f"Giao tuyến của hai mặt phẳng $({G}{M}{N})$ và $({B}{C}{D})$ là"
		)	

		kq=random.choice([
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{B}{D}}}$",
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
			f"đường thẳng qua ${{{B}}}$ và song song với ${{{C}{N}}}$",
			f"đường thẳng qua ${{{C}}}$ và song song với ${{{D}{M}}}$",
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{C}{D}}}$",
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{M}{N}}}$",]

		code_hinh_LG=(f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$) node at ({M}) [left] {{${M}$}};\n\
		\\coordinate ({N}) at ($({A})!0.5!({D})$) node at ({N}) [right] {{${N}$}};\n\
		\\coordinate ({G}) at (5/3,-2/3)   node at ({G}) [right] {{${G}$}};\n\
		\\draw [dashed] ({B})--({D}) ({M})--({N}) ({G})--({M}) ({G})--({N}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D})  ;\n\
		\\end{{tikzpicture}}\n")
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
				f"$\\left\\{{ \\begin{{array}}{{l}} \n\
				{M}{N}\\subset ({C}{M}{N}) \\\\ \n\
				{B}{D}\\subset ({B}{C}{D})\\\\ \n\
				{M}{N} // {B}{D} \n\
				\\end{{array}} \\right.$"
				f"$\\Rightarrow ({C}{M}{N}) \\cap ({A}{B}{C})={G}x // {M}{N} //{B}{D}$."
				)
	
	if chon==3:
		noi_dung=(
		f"Cho tứ diện ${{{A}{B}{C}{D}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{A}{C},{A}{D}}}$."
		f" Giao tuyến của hai mặt phẳng $({B}{M}{N})$ và $({B}{C}{D})$ là"
		)	

		kq=random.choice([
			f"đường thẳng qua ${{{B}}}$ và song song với ${{{C}{D}}}$",
			f"đường thẳng qua ${{{B}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
			f"đường thẳng qua ${{{B}}}$ và song song với ${{{C}{N}}}$",
			f"đường thẳng qua ${{{C}}}$ và song song với ${{{D}{M}}}$",
			f"đường thẳng qua ${{{M}}}$ và song song với ${{{C}{D}}}$",
			f"đường thẳng qua ${{{N}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{C}{N}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{M}{N}}}$",]

		code_hinh_LG=(f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({C})$) node at ({M}) [right] {{${M}$}};\n\
		\\coordinate ({N}) at ($({A})!0.5!({D})$) node at ({N}) [right] {{${N}$}};\n\
		\\draw [dashed] ({B})--({D})  ({B})--({N}) ; \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({B})--({M}) ({M})--({N});\n\
		\\end{{tikzpicture}}\n")
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
				f"$\\left\\{{ \\begin{{array}}{{l}} \n\
				{M}{N}\\subset ({B}{M}{N}) \\\\ \n\
				{C}{D}\\subset ({B}{C}{D})\\\\ \n\
				{M}{N} // {C}{D} \n\
				\\end{{array}} \\right.$"
				f"$\\Rightarrow ({B}{M}{N}) \\cap ({B}{C}{D})={B}x // {M}{N} //{C}{D}$.")

	

	if chon==4:
		t=random.randint(2,3)
		noi_dung=(
		f"Cho tứ diện ${{{A}{B}{C}{D}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{A}{B},{A}{D}}}$."
		f" Gọi ${{{G}}}$ là điểm thuộc cạnh ${{{B}{C}}}$ sao cho ${G}{B}={t}{G}{C}$."
		f"Giao tuyến của hai mặt phẳng $({G}{M}{N})$ và $({B}{C}{D})$ là"
		)	

		kq=random.choice([
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{B}{D}}}$",
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{M}{N}}}$"])
		kq_false=[
			f"đường thẳng qua ${{{B}}}$ và song song với ${{{C}{N}}}$",
			f"đường thẳng qua ${{{C}}}$ và song song với ${{{D}{M}}}$",
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{C}{D}}}$",
			f"đường thẳng qua ${{{G}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{B}{C}}}$",
			f"đường thẳng qua ${{{D}}}$ và song song với ${{{M}{N}}}$",]

		code_hinh_LG=(f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$) node at ({M}) [left] {{${M}$}};\n\
		\\coordinate ({N}) at ($({A})!0.5!({D})$) node at ({N}) [right] {{${N}$}};\n\
		\\coordinate ({G}) at ($({B})!{t/(t+1)}!({C})$) node at ({G}) [left] {{${G}$}};\n\
		\\draw [dashed] ({B})--({D}) ({M})--({N}) ({G})--({N}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D})  ({G})--({M});\n\
		\\end{{tikzpicture}}\n")
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)

		noi_dung_loigiai=(
				f"$\\left\\{{ \\begin{{array}}{{l}} \n\
				{M}{N}\\subset ({C}{M}{N}) \\\\ \n\
				{B}{D}\\subset ({B}{C}{D})\\\\ \n\
				{M}{N} // {B}{D} \n\
				\\end{{array}} \\right.$"
				f"$\\Rightarrow ({C}{M}{N}) \\cap ({A}{B}{C})={G}x // {M}{N} //{B}{D}$.")


	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"
	
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {file_name_LG}\n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B2_10]-TF-M2. Cho hình chóp-hbh. Xét Đ-S:chéo nhau, cắt nhau, song song, giao điểm đường-mặt
def ghj_7_jkl_L11_C4_B2_10():
	S="S"
	vertex=random.choice([
		["A","B","C","D"],["A","B","C","E"],["B","C","D","E"], 
		["C","D","E","F"], ["A","B","E","F"], ["B","C","E","F"]])
	A,B,C,D=vertex

	list_point=["M","N","P","Q", "G","H","K"]
	random.shuffle(list_point)
	M,N,P=list_point[0:3]

	O=random.choice(["O", "I", "J" ])

	name_bottom=random.choice(["hình bình hành", "hình chữ nhật", "hình thoi", "hình vuông" ])
	
	code_hinh=code_hinh_chop_deu_noname(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
\\coordinate ({A}) at (0,0);\n\
\\coordinate ({D}) at (2,-2);\n\
\\coordinate ({B}) at (5,0);\n\
\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
\\coordinate ({S}) at ($({O})+(0,7)$);\n\
\\coordinate ({M}) at ($({S})!0.5!({A})$);\n\
\\coordinate ({N}) at ($({S})!0.5!({B})$);\n\
\\draw ({S})--({A}) ({S})--({D}) ({S})--({C}) ({A})--({D}) ({C})--({D})  ({D})--({M});\n\
\\draw[dashed,thin]({S})--({B}) ({A})--({B}) ({B})--({C}) ({A})--({C})   ({B})--({D}) ({C})--({N}) ({S})--({O}) ({M})--({N});\n\
\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/-90, {M}/180, {N}/0, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
\\end{{tikzpicture}}\n"
	code = my_module.moi_truong_anh_latex(code_hinh_LG)
	file_name_LG=my_module.pdftoimage_timename(code)

	noi_dung = (f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ là {name_bottom} tâm ${{{O}}}$. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{B}}}$."
	f" Xét tính đúng-sai của các khẳng định sau: ")
	chon=random.randint(1,2)
	if chon==1:
		duong=random.choice([f"{B}{C}", f"{C}{D}", f"{B}{D}", f"{D}{N}", f"{C}{N}",  f"{O}{N}"])
		kq1_T=f"* ${{{S}{A}}}$ và ${{{duong}}}$ chéo nhau" 
		kq1_F=f"${{{S}{A}}}$ và ${{{duong}}}$ {random.choice(["cắt nhau", "song song"])}"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${{{S}{A}}}$ và ${{{duong}}}$ chéo nhau."
	
	if chon==2:
		duong=random.choice([f"{A}{B}", f"{A}{D}", f"{B}{D}", f"{D}{N}", f"{D}{M}",  f"{O}{N}"])
		kq1_T=f"* ${{{S}{C}}}$ và ${{{duong}}}$ chéo nhau" 
		kq1_F=f"${{{S}{C}}}$ và ${{{duong}}}$ {random.choice(["cắt nhau", "song song"])}"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${{{S}{C}}}$ và ${{{duong}}}$ chéo nhau."

	if chon==2:
		duong=random.choice([f"{C}{D}", f"{A}{D}", f"{A}{C}",f"{D}{M}",  f"{O}{M}"])
		kq1_T=f"* ${{{S}{B}}}$ và ${{{duong}}}$ chéo nhau" 
		kq1_F=f"${{{S}{B}}}$ và ${{{duong}}}$ {random.choice(["cắt nhau", "song song"])}"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${{{S}{B}}}$ và ${{{duong}}}$ chéo nhau."	
	

	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	duong_1=[f"{M}{N}", f"{M}{N}", f"{O}{M}", f"{O}{N}"]
	duong_2=[f"{A}{B}", f"{C}{D}", f"{S}{C}", f"{S}{D}"]
	i=random.randint(0,3)
	duong_1,duong_2=duong_1[i],duong_2[i]
	kq2_T=f"* ${{{duong_1}}}$ và ${{{duong_2}}}$ song song"
	kq2_F=f"${{{duong_1}}}$ và ${{{duong_2}}}$ {random.choice(["cắt nhau", "chéo nhau"])}"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"${{{duong_1}}}$ và ${{{duong_2}}}$ song song."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	duong_1=[f"{D}{M}", f"{O}{D}", f"{O}{B}", f"{O}{A}", f"{O}{C}"]
	duong_2=[f"{C}{N}", f"{A}{B}", f"{A}{D}", f"{C}{D}", f"{A}{D}" ]
	i=random.randint(0,3)
	duong_1,duong_2=duong_1[i],duong_2[i]

	kq3_T=f"* ${{{duong_1}}}$ và ${{{duong_2}}}$ cắt nhau" 
	kq3_F=f"${{{duong_1}}}$ và ${{{duong_2}}}$ {random.choice(["song song", "chéo nhau"])}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"${{{duong_1}}}$ và ${{{duong_2}}}$ cắt nhau."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,9)
	if chon==1:
		duong=random.choice([f"{S}{A}", f"{S}{C}", f"{A}{C}", f"{O}{A}", f"{O}{C}"])
		kq4_T=f"* Giao điểm của ${{{D}{N}}}$ và mặt phẳng $({S}{A}{C})$ là giao điểm giữa ${{{D}{N}}}$ và ${{{S}{O}}}$"
		kq4_F=f"Giao điểm của ${{{D}{N}}}$ và mặt phẳng $({S}{A}{C})$ là giao điểm giữa ${{{D}{N}}}$ và ${{{duong}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{D}{N}}}$ và mặt phẳng $({S}{A}{C})$ là giao điểm giữa ${{{D}{N}}}$ và ${{{S}{O}}}$."
	
	if chon==2:
		duong=random.choice([f"{S}{B}", f"{S}{D}", f"{B}{D}", f"{O}{D}", f"{O}{B}" ])
		kq4_T=f"* Giao điểm của ${{{C}{M}}}$ và mặt phẳng $({S}{B}{D})$ là giao điểm giữa ${{{C}{M}}}$ và ${{{S}{O}}}$"
		kq4_F=f"Giao điểm của ${{{C}{M}}}$ và mặt phẳng $({S}{B}{D})$ là giao điểm giữa ${{{C}{M}}}$ và ${{{duong}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{C}{M}}}$ và mặt phẳng $({S}{B}{D})$ là giao điểm giữa ${{{C}{M}}}$ và ${{{S}{O}}}$."

	if chon==3:
		duong=random.choice([f"{S}{B}", f"{S}{C}", f"{B}{C}", f"{A}{C}", f"{S}{O}" ])
		kq4_T=f"* Giao điểm của ${{{D}{M}}}$ và mặt phẳng $({S}{B}{C})$ là giao điểm giữa ${{{D}{M}}}$ và ${{{C}{N}}}$"
		kq4_F=f"Giao điểm của ${{{D}{M}}}$ và mặt phẳng $({S}{B}{C})$ là giao điểm giữa ${{{D}{M}}}$ và ${{{duong}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{D}{M}}}$ và mặt phẳng $({S}{B}{C})$ là giao điểm giữa ${{{D}{M}}}$ và ${{{C}{N}}}$."

	if chon==4:
		duong=random.choice([f"{S}{A}", f"{S}{C}", f"{A}{D}", f"{B}{D}", f"{S}{O}" ])
		kq4_T=f"* Giao điểm của ${{{C}{N}}}$ và mặt phẳng $({S}{A}{D})$ là giao điểm giữa ${{{C}{N}}}$ và ${{{D}{M}}}$"
		kq4_F=f"Giao điểm của ${{{C}{N}}}$ và mặt phẳng $({S}{A}{D})$ là giao điểm giữa ${{{C}{N}}}$ và ${{{duong}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{C}{N}}}$ và mặt phẳng $({S}{A}{D})$ là giao điểm giữa ${{{C}{N}}}$ và ${{{D}{M}}}$."

	if chon==5:
		duong=random.choice([f"{D}{N}", f"{C}{M}"])
		duong_false=random.choice([f"{D}{M}", f"{C}{N}", f"{M}{N}", f"{C}{D}" ])
		kq4_T=f"* Giao điểm của ${{{S}{O}}}$ và mặt phẳng $({M}{N}{C}{D})$ là giao điểm giữa ${{{S}{O}}}$ và ${{{duong}}}$"
		kq4_F=f"Giao điểm của ${{{S}{O}}}$ và mặt phẳng $({M}{N}{C}{D})$ là giao điểm giữa ${{{S}{O}}}$ và ${{{duong_false}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{S}{O}}}$ và mặt phẳng $({M}{N}{C}{D})$ là giao điểm giữa ${{{S}{O}}}$ và ${{{duong}}}$."

	if chon==6:		
		duong_false=random.choice([f"{S}{B}", f"{S}{D}", f"{M}{N}", f"{B}{D}" ])
		kq4_T=f"* Giao điểm của ${{{C}{M}}}$ và mặt phẳng $({S}{B}{D})$ là giao điểm giữa ${{{C}{M}}}$ và ${{{S}{O}}}$"
		kq4_F=f"Giao điểm của ${{{C}{M}}}$ và mặt phẳng $({S}{B}{D})$ là giao điểm giữa ${{{C}{M}}}$ và ${{{duong_false}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{C}{M}}}$ và mặt phẳng $({S}{B}{D})$ là giao điểm giữa ${{{C}{M}}}$ và ${{{S}{O}}}$."

	if chon==7:		
		duong_false=random.choice([f"{S}{A}", f"{S}{C}", f"{A}{C}", f"{A}{B}" ])
		kq4_T=f"* Giao điểm của ${{{D}{N}}}$ và mặt phẳng $({S}{A}{C})$ là giao điểm giữa ${{{D}{N}}}$ và ${{{S}{O}}}$"
		kq4_F=f"Giao điểm của ${{{D}{N}}}$ và mặt phẳng $({S}{A}{C})$ là giao điểm giữa ${{{D}{N}}}$ và ${{{duong_false}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{D}{N}}}$ và mặt phẳng $({S}{A}{C})$ là giao điểm giữa ${{{D}{N}}}$ và ${{{S}{O}}}$."

	if chon==8:		
		duong_false=random.choice([f"{N}{C}", f"{N}{D}", f"{C}{D}", f"{N}{B}" ])
		kq4_T=f"* Giao điểm của ${{{S}{A}}}$ và mặt phẳng $({N}{C}{D})$ là giao điểm giữa ${{{S}{A}}}$ và ${{{M}{N}}}$"
		kq4_F=f"Giao điểm của ${{{S}{A}}}$ và mặt phẳng $({N}{C}{D})$ là giao điểm giữa ${{{S}{A}}}$ và ${{{duong_false}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{S}{A}}}$ và mặt phẳng $({N}{C}{D})$ là giao điểm giữa ${{{S}{A}}}$ và ${{{M}{N}}}$."

	if chon==9:		
		duong_false=random.choice([f"{M}{D}", f"{M}{C}", f"{C}{D}", f"{D}{O}" ])
		kq4_T=f"* Giao điểm của ${{{S}{B}}}$ và mặt phẳng $({M}{C}{D})$ là giao điểm giữa ${{{S}{B}}}$ và ${{{M}{N}}}$"
		kq4_F=f"Giao điểm của ${{{S}{B}}}$ và mặt phẳng $({M}{C}{D})$ là giao điểm giữa ${{{S}{B}}}$ và ${{{duong_false}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Giao điểm của ${{{S}{B}}}$ và mặt phẳng $({M}{C}{D})$ là giao điểm giữa ${{{S}{B}}}$ và ${{{M}{N}}}$."
	
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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
	f"{file_name_LG}\n"
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
	    f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D11_C4_B2_11]-TF-M2. Cho hình chóp-hbh. Xét Đ-S:chéo nhau, cắt nhau, song song, giao điểm đường-mặt
def ghj_7_jkl_L11_C4_B2_11():
	S="S"
	vertex=random.choice([
		["A","B","C","D"],["A","B","C","E"],["B","C","D","E"], 
		["C","D","E","F"], ["A","B","E","F"], ["B","C","E","F"]])
	A,B,C,D=vertex

	list_point=["M","N","P","G","H","I","J","K"]
	random.shuffle(list_point)
	M,N,P,I,J=list_point[0:5]
	
	O=random.choice(["O"])

	name_bottom=random.choice(["hình bình hành", "hình chữ nhật", "hình thoi", "hình vuông" ])
	
	code_hinh=code_hinh_chop_deu_noname(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	noi_dung = (f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ là {name_bottom} tâm ${{{O}}}$."	
	f" Gọi ${{{M}}}$ là điểm tùy ý thuộc cạnh ${{{S}{A}}}$ không trùng với ${{{S}}}$ và ${{{A}}}$.")
	chon=random.randint(1,3)
	if chon==1:
		noi_dung +=f" Gọi ${{{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C}}}$."
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({D}) at (2,-2);\n\
		\\coordinate ({B}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!0.5!({A})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({A})$);\n\
		\\coordinate ({P}) at ($({B})!0.5!({C})$);\n\
		\\draw ({S})--({A}) ({S})--({D}) ({S})--({C}) ({A})--({D}) ({C})--({D});\n\
		\\draw[dashed,thin]({S})--({B}) ({A})--({B}) ({B})--({C}) ({A})--({C}) ({B})--({D}) ({S})--({O}) ({M})--({N}) ({N})--({P}) ({M})--({P});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/-90, {M}/180, {N}/-90, {P}/-90, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"
	
	if chon==2:
		t=random.randint(2,3)
		noi_dung +=f" Gọi ${{{N},{P}}}$ là các điểm lần lượt thuộc ${{{A}{B},{B}{C}}}$ sao cho ${B}{N}={t}{N}{A},{B}{P}={t}{P}{C}$."
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({D}) at (2,-2);\n\
		\\coordinate ({B}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!0.5!({A})$);\n\
		\\coordinate ({N}) at ($({B})!{t/(t+1)}!({A})$);\n\
		\\coordinate ({P}) at ($({B})!{t/(t+1)}!({C})$);\n\
		\\draw ({S})--({A}) ({S})--({D}) ({S})--({C}) ({A})--({D}) ({C})--({D});\n\
		\\draw[dashed,thin]({S})--({B}) ({A})--({B}) ({B})--({C}) ({A})--({C}) ({B})--({D}) ({S})--({O}) ({M})--({N}) ({N})--({P}) ({M})--({P});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/-90, {M}/180, {N}/-90,{P}/-90, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"
	if chon==3:
		t=random.randint(2,3)
		noi_dung +=f" Gọi ${{{N},{P}}}$ là các điểm lần lượt thuộc ${{{A}{B},{B}{C}}}$ sao cho ${B}{N}={t}{N}{A},{B}{P}={phan_so(t/(t+1))}{B}{C}$."
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({D}) at (2,-2);\n\
		\\coordinate ({B}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({S})!0.5!({A})$);\n\
		\\coordinate ({N}) at ($({A})!{t/(t+1)}!({B})$);\n\
		\\coordinate ({P}) at ($({B})!{t/(t+1)}!({C})$);\n\
		\\draw ({S})--({A}) ({S})--({D}) ({S})--({C}) ({A})--({D}) ({C})--({D});\n\
		\\draw[dashed,thin]({S})--({B}) ({A})--({B}) ({B})--({C}) ({A})--({C}) ({B})--({D}) ({S})--({O}) ({M})--({N}) ({N})--({P}) ({M})--({P});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/-90, {M}/180, {N}/-90,{P}/-90, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

	code = my_module.moi_truong_anh_latex(code_hinh_LG)
	file_name_LG=my_module.pdftoimage_timename(code)

	noi_dung +=f" Xét tính đúng-sai của các khẳng định sau: "
	debai_word= f"{noi_dung}\n"

	chon=random.randint(1,3)
	if chon==1:
		duong=random.choice([f"{S}{A}", f"{S}{B}", f"{S}{C}", f"{S}{D}", f"{B}{M}", f"{C}{M}", f"{D}{M}" ])	
		kq1_T=f"* ${{{N}{P}}}$ và ${{{duong}}}$ chéo nhau" 
		kq1_F=f"${{{N}{P}}}$ và ${{{duong}}}$ {random.choice(["song song", "cắt nhau"])}"	
		HDG=f"${{{N}{P}}}$ và ${{{duong}}}$ chéo nhau."
	
	if chon==2:
		duong=random.choice([f"{A}{D}", f"{C}{D}", f"{B}{D}", f"{O}{D}" ])	
		kq1_T=f"* ${{{N}{P}}}$ và ${{{duong}}}$ cắt nhau" 
		kq1_F=f"${{{N}{P}}}$ và ${{{duong}}}$ {random.choice(["chéo nhau", "song song" ])}"	
		HDG=f"${{{N}{P}}}$ và ${{{duong}}}$ cắt nhau."

	if chon==3:
		duong_1=[f"{A}{C}", f"{M}{N}", f"{O}{M}", f"{O}{N}"]
		duong_2=[f"{N}{P}", f"{S}{B}", f"{S}{C}", f"{B}{C}"]
		i=random.randint(0,3)
		duong_1,duong_2=duong_1[i], duong_2[i]
		kq1_T=f"* ${{{duong_1}}}$ và ${{{duong_2}}}$ song song" 
		kq1_F=f"${{{duong_1}}}$ và ${{{duong_2}}}$ {random.choice(["chéo nhau", "cắt nhau" ])}"	
		HDG=f"${{{duong_1}}}$ và ${{{duong_2}}}$ song song."
	
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,4)
	if chon==1:
		duong=random.choice([f"{A}{D}", f"{B}{C}"])
		duong_false=random.choice([f"{A}{B}", f"{C}{D}"])

		kq2_T=f"* Giao tuyến của $({M}{B}{C})$ và $({S}{A}{D})$ là đường thẳng qua {M} và song song với ${{{duong}}}$"
		kq2_F=f"Giao tuyến của $({M}{B}{C})$ và $({S}{A}{D})$ là đường thẳng qua {M} và song song với ${{{duong_false}}}$"
		
		HDG=(f"$\\left\\{{ \\begin{{array}}{{l}} \n\
		{M} \\in ({M}{B}{C})\\cap ({S}{A}{D})\\\\ \n\
		{B}{C} \\subset ({M}{B}{C})\\\\ \n\
		{A}{D} \\subset ({S}{A}{D}) \n\
		\\end{{array}} \\right.\\Rightarrow ({M}{B}{C}) \\cap ({S}{A}{D}) ={M}x//{B}{C}//{A}{D}$.")	
	if chon==2:
		duong=random.choice([f"{A}{C}", f"{N}{P}"])
		duong_false=random.choice([f"{A}{B}",f"{B}{C}", f"{C}{D}", f"{B}{D}"])
		kq2_T=f"* Giao tuyến của $({M}{N}{P})$ và $({S}{A}{C})$ là đường thẳng qua {M} và song song với ${{{duong}}}$"
		kq2_F=f"Giao tuyến của $({M}{N}{P})$ và $({S}{A}{C})$ là đường thẳng qua {M} và song song với ${{{duong_false}}}$"
		
		HDG=(f"$\\left\\{{ \\begin{{array}}{{l}} \n\
		{M} \\in ({M}{N}{P})\\cap ({S}{A}{C})\\\\ \n\
		{N}{P} \\subset ({M}{N}{P})\\\\ \n\
		{A}{C} \\subset ({S}{A}{C}) \n\
		\\end{{array}} \\right.\\Rightarrow ({M}{N}{P}) \\cap ({S}{A}{C})={M}x//{N}{P}//{A}{C}$.")

	if chon==3:
		duong=random.choice([f"{A}{D}", f"{B}{C}"])
		duong_false=random.choice([f"{A}{B}",f"{B}{C}", f"{C}{D}", f"{B}{D}"])
		kq2_T=f"* Giao tuyến của $({S}{A}{D})$ và $({S}{B}{C})$ là đường thẳng qua {S} và song song với ${{{duong}}}$"
		kq2_F=f"Giao tuyến của $({S}{A}{D})$ và $({S}{B}{C})$ là đường thẳng qua {M} và song song với ${{{duong}}}$"
		
		HDG=(f"$\\left\\{{ \\begin{{array}}{{l}} \n\
		{S} \\in ({S}{A}{D})\\cap ({S}{B}{C})\\\\ \n\
		{A}{D} \\subset ({S}{A}{D})\\\\ \n\
		{B}{C} \\subset ({S}{B}{C}) \n\
		\\end{{array}} \\right.\\Rightarrow ({S}{A}{D}) \\cap ({S}{B}{C})={S}x//{A}{D}//{B}{C}$.")

	if chon==4:
		duong=random.choice([f"{A}{B}", f"{C}{D}"])
		duong_false=random.choice([f"{A}{C}",f"{B}{D}", f"{B}{C}", f"{A}{D}"])
		kq2_T=f"* Giao tuyến của $({S}{A}{B})$ và $({S}{C}{D})$ là đường thẳng qua {S} và song song với ${{{duong}}}$"
		kq2_F=f"Giao tuyến của $({S}{A}{B})$ và $({S}{C}{D})$ là đường thẳng qua {S} và song song với ${{{duong_false}}}$"
		
		HDG=(f"$\\left\\{{ \\begin{{array}}{{l}} \n\
		{S} \\in ({S}{A}{B})\\cap ({S}{C}{D})\\\\ \n\
		{A}{B} \\subset ({S}{A}{B})\\\\ \n\
		{C}{D} \\subset ({S}{C}{D}) \n\
		\\end{{array}} \\right.\\Rightarrow ({S}{A}{B}) \\cap ({S}{C}{D})={S}x//{A}{B}//{C}{D}$.")


	kq2=random.choice([kq2_T, kq2_F])
	
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon==1:
		duong=random.choice([f"{C}{D}",f"{S}{A}", f"{S}{D}", f"{B}{D}"])
		kq3_T=f"* Giao tuyến của $({S}{N}{P})$ và $({S}{A}{D})$ là đường thẳng qua {S}{I} với ${I}={N}{P}\\cap {A}{D}$" 
		kq3_F=f"Giao tuyến của $({S}{N}{P})$ và $({S}{A}{D})$ là đường thẳng qua {S}{I} với ${I}={N}{P}\\cap {duong}$"		
		HDG=(f"${S}\\in ({S}{N}{P}) \\cap ({S}{A}{D})$.\n\n"
			f"${I}={N}{P}\\cap {A}{D}\\Rightarrow {I}\\in ({S}{N}{P}) \\cap ({S}{A}{D})$\n\n"
			f"$\\Rightarrow ({S}{N}{P}) \\cap ({S}{A}{D})={S}{I}$.")
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	
	if chon==2:
		duong=random.choice([f"{A}{D}",f"{S}{C}", f"{S}{D}", f"{B}{D}"])
		kq3_T=f"* Giao tuyến của $({S}{N}{P})$ và $({S}{C}{D})$ là đường thẳng qua {S}{I} với ${I}={N}{P}\\cap {C}{D}$" 
		kq3_F=f"Giao tuyến của $({S}{N}{P})$ và $({S}{C}{D})$ là đường thẳng qua {S}{I} với ${I}={N}{P}\\cap {duong}$"
		
		HDG=(f"${S}\\in ({S}{N}{P}) \\cap ({S}{C}{D})$.\n\n"
			f"${I}={N}{P}\\cap {C}{D}\\Rightarrow {I}\\in ({S}{N}{P}) \\cap ({S}{C}{D})$\n\n"
			f"$\\Rightarrow ({S}{N}{P}) \\cap ({S}{C}{D})={S}{I}$.")
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"

	kq3=random.choice([kq3_T, kq3_F])
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,4)
	if chon==1:
		duong=random.choice([f"{S}{B}",f"{S}{D}", f"{B}{D}"])
		kq4_T=f"* Giao điểm của ${{{C}{M}}}$ và $({S}{B}{D})$ là điểm ${{{J}}}$ với ${J}={C}{M}\\cap {S}{O}$"
		kq4_F=f"Giao điểm của ${{{C}{M}}}$ và $({S}{B}{D})$ là điểm ${{{J}}}$ với ${J}={C}{M}\\cap {duong}$"

		HDG=(f"${J}={C}{M}\\cap {S}{O}\\Rightarrow {J}\\in {C}{M}, {J}\\in {S}{O} \\subset ({S}{B}{D})$.\n\n"
			f"$\\Rightarrow {C}{M}\\cap ({S}{B}{D}) ={J}$."	)
	
	if chon==2:
		duong=random.choice([f"{M}{C}",f"{M}{D}", f"{B}{D}"])
		kq4_T=f"* Giao điểm của ${{{A}{P}}}$ và $({M}{C}{D})$ là điểm ${{{J}}}$ với ${J}={A}{P}\\cap {C}{D}$"
		kq4_F=f"Giao điểm của ${{{A}{P}}}$ và $({M}{C}{D})$ là điểm ${{{J}}}$ với ${J}={A}{P}\\cap {duong}$"
		
		HDG=(f"${J}={A}{P}\\cap {C}{D}\\Rightarrow {J}\\in {A}{P}, {J}\\in {C}{D} \\subset ({M}{C}{D})$.\n\n"
			f"$\\Rightarrow {A}{P}\\cap ({M}{C}{D}) ={J}$.")

	if chon==3:
		duong=random.choice([f"{M}{N}",f"{M}{P}", f"{A}{P}"])
		kq4_T=f"* Giao điểm của ${{{C}{D}}}$ và $({M}{N}{P})$ là điểm ${{{J}}}$ với ${J}={C}{D}\\cap {N}{P}$"
		kq4_F=f"Giao điểm của ${{{C}{D}}}$ và $({M}{N}{P})$ là điểm ${{{J}}}$ với ${J}={C}{D}\\cap {duong}$"
		
		HDG=(f"${J}={C}{D}\\cap {N}{P}\\Rightarrow {J}\\in {C}{D}, {J}\\in {N}{P} \\subset ({M}{N}{P})$.\n\n"
			f"$\\Rightarrow {C}{D}\\cap ({M}{N}{P}) ={J}$.")

	if chon==4:
		duong=random.choice([f"{M}{N}",f"{M}{P}", f"{A}{P}"])
		kq4_T=f"* Giao điểm của ${{{A}{D}}}$ và $({M}{N}{P})$ là điểm ${{{J}}}$ với ${J}={A}{D}\\cap {N}{P}$"
		kq4_F=f"Giao điểm của ${{{A}{D}}}$ và $({M}{N}{P})$ là điểm ${{{J}}}$ với ${J}={A}{D}\\cap {duong}$"
		
		HDG=(f"${J}={A}{D}\\cap {N}{P}\\Rightarrow {J}\\in {A}{D}, {J}\\in {N}{P} \\subset ({M}{N}{P})$.\n\n"
			f"$\\Rightarrow {A}{D}\\cap ({M}{N}{P}) ={J}$.")	

	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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

	loigiai_word=f"Lời giải:{file_name_LG}\n {noi_dung_loigiai} \n" \

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
	    f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#Bài 3 - Đường thẳng song song với mặt phẳng 

#[D11_C4_B3_01]-M2. Cho hình chóp-hbh. Tìm đường song song-mặt
def ghj_7_jkl_L11_C4_B3_01():
	S="S"
	vertex=random.choice([
		["A","B","C","D"],["A","B","C","E"],["B","C","D","E"], 
		["C","D","E","F"], ["A","B","E","F"], ["B","C","E","F"]])
	
	A,B,C,D=vertex

	name_points=["M","N","P","Q","G","H","J","K"]
	random.shuffle(name_points)

	M,N,G,H=name_points[0:4]
	O=random.choice(["O", "I"])

	name_bottom=random.choice(["hình bình hành", "hình chữ nhật", "hình thoi", "hình vuông" ])	

	code_hinh=code_hinh_chop_deu_noname(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	
	chon=random.randint(1,6)
	t=random.randint(2,3)
	if chon==1:		
		noi_dung=(
	f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
	f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các cạnh ${{{S}{A},{S}{B}}}$ sao cho ${M}{A}={t}{S}{M}, {N}{B}={t}{S}{N}$."
	f" Khẳng định nào sau đây là khẳng định đúng?")
	
	if chon==2:
		noi_dung=(
	f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
	f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các cạnh ${{{S}{A},{S}{B}}}$ sao cho ${M}{A}={t}{S}{M}, {S}{B}={t+1}{S}{N}$."
	f" Khẳng định nào sau đây là khẳng định đúng?")

	if chon==3:
		noi_dung=(
	f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
	f" Gọi ${{{M},{N}}}$ lần lượt là các điểm thuộc các cạnh ${{{S}{A},{S}{B}}}$ sao cho ${S}{A}={t+1}{S}{M}, {N}{B}={t}{S}{N}$."
	f" Khẳng định nào sau đây là khẳng định đúng?")

	code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
\\coordinate ({A}) at (0,0);\n\
\\coordinate ({B}) at (2,-2);\n\
\\coordinate ({D}) at (5,0);\n\
\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
\\coordinate ({S}) at ($({O})+(0,7)$);\n\
\\coordinate ({M}) at ($({A})!{round(t/(t+1),1)}!({S})$);\n\
\\coordinate ({N}) at ($({B})!{round(t/(t+1),1)}!({S})$);\n\
\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ;\n\
\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({O})--({M}) ({O})--({N}) ({M})--({N});\n\
\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
\\end{{tikzpicture}}\n"	
	code = my_module.moi_truong_anh_latex(code_hinh_LG)
	file_name_LG=my_module.pdftoimage_timename(code)

	kq=random.choice([
		f"{M}{N}//({A}{B}{C}{D})",
		f"{M}{N}//({S}{C}{D})",
		f"{M}{N}//({B}{C}{D})",
		f"{M}{N}//({A}{C}{D})",
		f"{M}{N}//({O}{A}{B})",		
		
		f"{B}{C}//({S}{A}{D})",
		f"{C}{D}//({S}{A}{B})",
		f"{C}{D}//({O}{M}{N})",		
		f"{A}{B}//({O}{M}{N})",
		f"{A}{B}//({D}{M}{N})",
		f"{A}{B}//({C}{M}{N})",
		f"{A}{B}//({S}{C}{D})",

		f"{A}{D}//({S}{B}{C})",
		])

	kq_false=[
		f"{M}{N}//({S}{A}{B})",
		f"{O}{M}//({S}{B}{C})",
		f"{O}{N}//({S}{C}{D})",	
		f"{A}{C}//({S}{B}{D})",
		f"{B}{D}//({S}{A}{C})",		
		f"{C}{D}//({D}{M}{N})",		
		f"{B}{C}//({O}{M}{N})",
		f"{M}{D}//({S}{B}{C})",
		
		]
	if f"{M}{N}" in kq:
		noi_dung_loigiai=(
		f"$\\dfrac{{{S}{M}}}{{{S}{A}}}=\\dfrac{{{S}{N}}}{{{S}{B}}}={phan_so(1/(t+1))}\\Rightarrow {M}{N}$ // ${{{A}{B}}}$ // ${{{C}{D}}}$"
		f"$\\Rightarrow {kq}$."
		)
	else:
		noi_dung_loigiai=f"{kq} là khẳng định đúng."
	
	if chon==4:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{C}}}$."
		f" Khẳng định nào sau đây là khẳng định đúng?")
	
		kq=random.choice([
			f"{M}{N}//({A}{B}{C}{D})",
			f"{M}{N}//({A}{B}{C})",
			f"{M}{N}//({A}{C}{D})",
			f"{M}{N}//({B}{C}{D})",

			f"{A}{C}//({B}{M}{N})",
			f"{A}{C}//({D}{M}{N})",

			f"{O}{M}//({S}{B}{C})",
			f"{O}{M}//({S}{C}{D})",

			f"{O}{N}//({S}{A}{B})",
			f"{O}{N}//({S}{A}{D})",
			])

		kq_false=[
			f"{M}{N}//({S}{A}{B})",
			f"{M}{N}//({S}{A}{C})",	
			f"{O}{N}//({S}{C}{D})",
			f"{A}{C}//({S}{B}{D})",
			f"{B}{D}//({S}{A}{C})",			
			f"{C}{D}//({B}{M}{N})",		
			f"{B}{C}//({O}{M}{N})",
			f"{M}{D}//({S}{B}{C})",
			f"{B}{N}//({S}{A}{D})",
			]
		noi_dung_loigiai=f"${kq}$ là khẳng định đúng."
		if f"{M}{N}" in kq:
			noi_dung_loigiai=(
		f"${M}{N} // {A}{C} \\Rightarrow {kq}$.")

		if f"{O}{M}" in kq:
			noi_dung_loigiai=(f"${O}{M} // {S}{C}\\Rightarrow {kq}$.")

		if f"{O}{N}" in kq:
			noi_dung_loigiai=(f"${O}{N} // {S}{A}\\Rightarrow {kq}$.")

		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!0.5!({S})$);\n\
		\\coordinate ({N}) at ($({C})!0.5!({S})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ;\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({O})--({M}) ({O})--({N}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"	
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)
	
	if chon==5:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{S}{B},{B}{D}}}$."
		f" Khẳng định nào sau đây là khẳng định đúng?")		
		kq=random.choice([
			f"{M}{N}//({A}{B}{C}{D})",
			f"{M}{N}//({A}{B}{C})",
			f"{M}{N}//({A}{C}{D})",
			f"{M}{N}//({B}{C}{D})",

			f"{B}{D}//({A}{M}{N})",
			f"{B}{D}//({C}{M}{N})",

			f"{O}{M}//({S}{C}{D})",
			f"{O}{M}//({S}{A}{D})",

			f"{O}{N}//({S}{A}{B})",
			f"{O}{N}//({S}{B}{C})",	])

		kq_false=[
			f"{M}{N}//({S}{A}{B})",
			f"{M}{N}//({S}{A}{C})",	
			f"{O}{N}//({S}{C}{D})",
			f"{A}{C}//({S}{B}{D})",
			f"{B}{D}//({S}{A}{C})",
			f"{C}{D}//({B}{M}{N})",
			f"{B}{C}//({O}{M}{N})",
			f"{M}{D}//({S}{B}{C})",
			f"{B}{N}//({S}{A}{D})",
			f"{B}{N}//({S}{A}{C})",]

		noi_dung_loigiai=f"${kq}$ là khẳng định đúng."
		if f"{M}{N}" in kq:
			noi_dung_loigiai=(f"${M}{N} // {B}{D} \\Rightarrow {kq}$.")

		if f"{O}{M}" in kq:
			noi_dung_loigiai=(f"${O}{M} // {S}{D}\\Rightarrow {kq}$.")

		if f"{O}{N}" in kq:
			noi_dung_loigiai=(f"${O}{N} // {S}{B}\\Rightarrow {kq}$.")

		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({B})!0.5!({S})$);\n\
		\\coordinate ({N}) at ($({D})!0.5!({S})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({O})--({M}) ({O})--({N}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"	
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)	

	if chon==6:
		noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là các trung điểm của ${{{A}{B},{C}{D}}}$"
		f" và ${{{G},{H}}}$ lần lượt là trọng tâm các tam giác ${{{S}{A}{B},{S}{C}{D}}}$."
		f" Khẳng định nào sau đây là khẳng định đúng?")		
		
		kq=random.choice([
			f"{G}{H} // ({A}{B}{C}{D})",
			f"{G}{H} // ({A}{B}{D})",
			f"{G}{H} // ({B}{C}{D})",
			f"{B}{C} // ({S}{G}{H})",
			f"{B}{C} // ({S}{M}{N})",			
			f"{A}{D} // ({S}{G}{H})",
			f"{A}{D} // ({S}{M}{N})",])

		kq_false=[
			f"{M}{N}//({S}{A}{B})",
			f"{M}{N}//({S}{C}{D})",	
			f"{O}{N}//({S}{C}{D})",
			f"{O}{H}//({S}{C}{D})",
			f"{O}{G}//({S}{A}{B})",
			f"{B}{H}//({S}{A}{D})",
			f"{B}{G}//({S}{C}{D})",
			]

		noi_dung_loigiai=(
			f"$\\dfrac{{{S}{G}}}{{{S}{M}}}=\\dfrac{{{S}{H}}}{{{S}{N}}}={phan_so(2/3)}\\Rightarrow {G}{H} // {M}{N} // {A}{C} // {B}{D}$.\n\n"
			f"Suy ra ${kq}$ là khẳng định đúng."	)

		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({C})!0.5!({D})$);\n\
		\\coordinate ({G}) at ($({S})!{2/3}!({M})$);\n\
		\\coordinate ({H}) at ($({S})!{2/3}!({N})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({S})--({M});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N}) ({G})--({H}) ({S})--({N});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90, {G}/-180, {H}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"	
		code = my_module.moi_truong_anh_latex(code_hinh_LG)
		file_name_LG=my_module.pdftoimage_timename(code)	


	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {file_name}\n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B3_02]. Cho hình chóp đáy hình thang. Xét sự song song của một đường thẳng với các mp.
def ghj_7_jkl_L11_C4_B3_02():
	ten_hinhchop=random.choice(["S.ABCD"])
	day_lon="AB"
	diem_1 = random.choice(["M","I","G","P"])
	diem_2 = random.choice(["N","K","H","Q"]) 
	canh= random.choice(["${AD}$ và ${BC}$", "${AD}$ và ${SA}$", "${BC}$ và ${SB}$","${SC}$ và ${SD}$"])

	if canh=="${AD}$ và ${BC}$":
		kq=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SCD)}}$", f"${{{diem_1}{diem_2}}}$//${{(SAB)}}$"])
		kq2=f"${{{diem_1}{diem_2}}}$//${{(SBC)}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SAD)}}$", f"${{{diem_1}{diem_2}}}$//${{(SAC)}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SBD)}}$", f"${{{diem_1}{diem_2}}}$//${{(ABCD)}}$"])

	if canh=="${AD}$ và ${SA}$":
		kq=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SCD)}}$", f"${{{diem_1}{diem_2}}}$//${{(SBD)}}$"])
		kq2=f"${{{diem_1}{diem_2}}}$//${{(SBC)}}$"
		kq3=f"${{{diem_1}{diem_2}}}$//${{(SAC)}}$"
		kq4=f"${{{diem_1}{diem_2}}}$//${{(ABCD)}}$"

	if canh=="${BC}$ và ${SB}$":
		kq=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SCD)}}$", f"${{{diem_1}{diem_2}}}$//${{(SAC)}}$"])
		kq2=f"${{{diem_1}{diem_2}}}$//${{(SBD)}}$"
		kq3=f"${{{diem_1}{diem_2}}}$//${{(SAD)}}$"
		kq4=f"${{{diem_1}{diem_2}}}$//${{(SA{diem_1})}}$"

	if canh=="${SC}$ và ${SD}$":
		kq=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SAB)}}$", f"${{{diem_1}{diem_2}}}$//${{(ABCD)}}$"])
		kq2=f"${{{diem_1}{diem_2}}}$//${{(SBD)}}$"
		kq3=f"${{{diem_1}{diem_2}}}$//${{(SAC)}}$"
		kq4=f"${{{diem_1}{diem_2}}}$//${{(SA{diem_2})}}$"	
	
	code=my_module.codelatex_hinhchop_hinhthang("S","A","B","C","D")
	file_name=my_module.pdftoimage_timename(code)
	
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình chóp ${{{ten_hinhchop}}}$ có đáy là hình thang đáy lớn ${{{day_lon}}}$. Gọi ${{{diem_1}}}$ và ${{{diem_2}}}$ lần lượt là trung điểm của các cạnh {canh}. Tìm khẳng định đúng."
	
	debai= f"{noi_dung}\n\n"\
	    f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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

#[D11_C4_B3_03]-M2. Cho a nằm trong (P) và b//(P). Tìm khẳng định đúng hoặc sai
def ghj_7_jkl_L11_C4_B3_03():
	name_lines=["a","m","d","b","n","\\Delta"]
	random.shuffle(name_lines)
	a,b=name_lines[0:2]
	P=random.choice(["(P)","(Q)","(R)", "(\\alpha)", "(\\beta)", "(\\gamma)"])
	M=random.choice(["A","B","M","N", "E","F","I","H",])
	chon=random.randint(1,2)
	if chon==1:
		noi_dung=(
		f"Trong không gian cho đường thẳng ${{{a}}}$ chứa trong mặt phẳng ${{{P}}}$,"
		f" đường thẳng ${{{b}}}$ song song với mặt phẳng ${{{P}}}$"
		f" và điểm ${{{M}}}$ thuộc mặt phẳng ${{{P}}}$."
		f" Tìm khẳng định đúng trong các khẳng định sau."
		)	

		kq=random.choice([
		f"${{{a}}}$ và ${{{b}}}$ không có điểm chung",
		f"${{{b}}}$ và mặt phẳng ${{{P}}}$ không có điểm chung",
		f"Điểm ${{{M}}}$ không thuộc đường thẳng ${{{b}}}$",
		f"Điểm ${{{M}}}$ và ${{{a}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{b}}}$ và song song với ${{{a}}}$"
		 ])
		kq_false=[
		f"${{{a}}}$ và ${{{b}}}$ song song",
		f"${{{a}}}$ và ${{{b}}}$ chéo nhau",
		f"${{{a}}}$ và ${{{b}}}$ cắt nhau",
		f"Điểm ${{{M}}}$ thuộc đường thẳng ${{{a}}}$",
		f"${{{a}}}$ và ${{{b}}}$ cùng thuộc một mặt phẳng",
		f"Điểm ${{{M}}}$ và ${{{b}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{M}}}$ và song song với ${{{b}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{a}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{b}}}$"

		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
		f"{kq} là khẳng định đúng."
		)
	
	if chon==2:
		noi_dung=(
		f"Trong không gian cho đường thẳng ${{{a}}}$ chứa trong mặt phẳng ${{{P}}}$,"
		f" đường thẳng ${{{b}}}$ song song với mặt phẳng ${{{P}}}$"
		f" và điểm ${{{M}}}$ thuộc mặt phẳng ${{{P}}}$."
		f" Tìm khẳng định sai trong các khẳng định sau."
		)	

		kq=random.choice([
		f"${{{a}}}$ và ${{{b}}}$ song song",
		f"${{{a}}}$ và ${{{b}}}$ chéo nhau",
		f"${{{a}}}$ và ${{{b}}}$ cắt nhau",
		f"Điểm ${{{M}}}$ thuộc đường thẳng ${{{a}}}$",
		f"${{{a}}}$ và ${{{b}}}$ cùng thuộc một mặt phẳng",
		f"Điểm ${{{M}}}$ và ${{{b}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{M}}}$ và song song với ${{{b}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{a}}}$",
		f"Có vô số đường thẳng đi qua ${{{M}}}$ và song song với ${{{b}}}$"
		
		 ])
		kq_false=[
		f"${{{a}}}$ và ${{{b}}}$ không có điểm chung",
		f"${{{b}}}$ và mặt phẳng ${{{P}}}$ không có điểm chung",
		f"Điểm ${{{M}}}$ không thuộc đường thẳng ${{{b}}}$",
		f"Điểm ${{{M}}}$ và ${{{a}}}$ cùng nằm trong một mặt phẳng",
		f"Có duy nhất một mặt phẳng chứa điểm ${{{b}}}$ và song song với ${{{a}}}$",
		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
		f"{kq} là khẳng định sai.")	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B3_04]-M2. Câu hỏi lý thuyết về quan hệ song song giữa đường-mặt
def ghj_7_jkl_L11_C4_B3_04():
	name_lines=["a","m","d","b","n","l","\\Delta"]
	random.shuffle(name_lines)
	a,b,c=name_lines[0:3]

	name_planes=(["(P)","(Q)","(R)", "(\\alpha)", "(\\beta)", "(\\gamma)"])
	random.shuffle(name_planes)
	mp_P,mp_Q=name_planes[0:2]

	M=random.choice(["A","B","M","N", "E","F","I","H",])
	noi_dung=(f"Cho các đường thẳng ${{{a},{b}}}$ và các mặt phẳng ${{{mp_P}, {mp_Q}}}$. Khẳng định nào sau đây là khẳng định đúng?")	

	kq=random.choice([
	f"${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ khi và chỉ khi ${{{a}}}$ và ${{{mp_P}}}$ không có điểm chung",
	f"Nếu ${mp_P}\\cap {mp_Q}={a}$ và ${{{b}}}$ song song với cả hai mặt phẳng ${{{mp_P}, {mp_Q}}}$ thì ${{{a}}}$ song song ${{{b}}}$",
	f"Nếu ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ và ${b}\\subset {mp_P}$ thì ${{{a}}}$ song song ${{{b}}}$ hoặc ${{{a},{b}}}$ chéo nhau",
	f"Cho ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$. Nếu mặt phẳng ${{{mp_Q}}}$ chứa ${{{a}}}$ cắt ${{{mp_P}}}$ theo giao tuyến ${{{c}}}$ thì ${{{c}}}$ song song với ${{{a}}}$",
	f"Nếu đường thẳng ${{{a}}}$ không nằm trong mặt phẳng ${{{mp_P}}}$ và song song với một đường thẳng nào đó nằm trong ${{{mp_P}}}$ thì ${{{a}}}$ song song với ${{{mp_P}}}$",
	f"Nếu ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ và ${b}\\subset {mp_P}$ thì ${{{a}}}$ và ${{{b}}}$ không có điểm chung",
	f"Nếu ${{{a}}}$ song song với ${{{b}}}$ và ${{{b}}}$ song song với ${{{c}}}$ thì ${{{a}}}$ song song với ${{{c}}}$ hoặc ${{{a},{c}}}$ chéo nhau",
	f"Nếu ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ thì có vô số đường thẳng nằm trong ${{{mp_P}}}$ và song song với ${{{a}}}$",
	f"Nếu ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ thì có một đường thẳng ${{{c}}}$ nằm trong ${{{mp_P}}}$ sao ${{{a}}}$ và ${{{c}}}$ đồng phẳng",
	])

	kq_false=[
	f"Nếu ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ thì ${{{a}}}$ song song với mọi đường thẳng nằm trên mặt phẳng ${{{mp_P}}}$",
	f"Nếu ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ thì mọi mặt phẳng chứa ${{{a}}}$ đều song song với mặt phẳng ${{{mp_P}}}$",
	f"Nếu ${{{a}}}$ song song với ${{{b}}}$ và ${{{b}}}$ song song với mặt phẳng ${{{mp_P}}}$ thì ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$",
	f"Nếu ${{{a}}}$ song song với mặt phẳng ${{{mp_P}}}$ và ${b}\\subset {mp_P}$ thì ${{{a},{b}}}$ chéo nhau",
	f"Nếu ${{{a}}}$ song song với ${{{b}}}$ và ${b}\\subset {mp_P}$ thì ${{{a}}}$ song song với ${{{mp_P}}}$",
	f"Nếu hai đường thẳng phân biệt ${{{a},{b}}}$ cùng song song với mặt phẳng ${{{mp_P}}}$ thì ${{{a},{b}}}$ song song nhau",
	f"Nếu đường thẳng ${{{a}}}$ không nằm trong mặt phẳng ${{{mp_P}}}$ thì ${{{a}}}$ song song với ${{{mp_P}}}$",
	f"Nếu đường thẳng ${{{a}}}$ song song với một đường thẳng ${{{b}}}$ nào đó nằm trong ${{{mp_P}}}$ thì ${{{a}}}$ song song với ${{{mp_P}}}$",
	f"Qua một điểm ${{{M}}}$ nằm ngoài mặt phẳng ${{{mp_P}}}$ có một và chỉ một đường thẳng song song với mặt phẳng ${{{mp_P}}}$",
	f"Nếu ${{{a}}}$ song song với ${{{b}}}$ và ${{{b}}}$ song song với ${{{c}}}$ thì ${{{a}}}$ song song với ${{{c}}}$"
	]
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	noi_dung_loigiai=(f"{kq} là khẳng định đúng.")

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B3_05]-M2. Cho hình chóp tam giác. Tìm đường song song-mặt phẳng
def ghj_7_jkl_L11_C4_B3_05():	
	vertex=random.choice([
		["A","B","C","D"],["S","A","B","C"],["B","C","D","E"], 
		["S","C","D","E"], ["A","B","E","F"], ["B","C","E","F"],["C","D","E","F"] ])
	
	A,B,C,D=vertex
	ten_hinhchop=random.choice([f"tứ diện ${{{A}{B}{C}{D}}}$", f"hình chóp ${{{A}.{B}{C}{D}}}$"])

	name_points=["M","N","P","Q", "I","J"]
	random.shuffle(name_points)
	M,N,P=name_points[0:3]

	code_hinh=code_hinh_tu_dien_noname(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	chon=random.randint(1,4)
	if chon==1:
		t=random.randint(2,3)		
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({A})!{t/(t+1)}!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ; \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N});\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/0,{P}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{A}{B},{A}{C}}}$."
		f"Gọi ${{{P}}}$ là điểm thuộc cạnh ${{{A}{D}}}$ sao cho ${P}{A}={t}{P}{D}$"
		f" Đường thẳng ${{{M},{N}}}$ song song với mặt phẳng nào sau đây?"
		)	

		kq=[f"({B}{C}{D})", f"({P}{B}{C})", f"({B}{C}{P})", f"({D}{B}{C})"]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"({A}{B}{C})", f"({A}{C}{D})", f"({A}{B}{D})", f"({M}{N}{P})", f"({C}{M}{N})",
		f"({D}{M}{N})", f"({C}{M}{P})", f"({M}{C}{D})", f"({N}{B}{D})"
		]
		noi_dung_loigiai=(
		f"${M}{N}//{B}{C}\\subset {kq},{M}{N} \\not \\subset {kq} \\Rightarrow {M}{N}//{kq}$."
		)
	if chon==2:
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({A})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/0,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{A}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định đúng?"
		)	

		kq=[
		f"{M}{N}//({A}{C}{D})", f"{M}{N}//({P}{C}{D})", f"{M}{N}//({A}{P}{C})", 
		f"{M}{P}//({B}{C}{D})", f"{M}{P}//({N}{C}{D})",	f"{M}{P}//({B}{D}{N})", f"{M}{P}//({D}{N}{C})",
		f"{A}{C}//({M}{N}{P})", f"{A}{C}//({D}{M}{N})",
		f"{B}{D}//({M}{N}{P})", f"{B}{D}//({C}{M}{P})",
		]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{M}{N}//({A}{B}{C})", f"{M}{P}//({A}{B}{D})", f"{C}{D}//({M}{N}{P})",
		f"{B}{C}//({M}{N}{P})", f"{M}{D}//({A}{B}{C})",
		f"{C}{M}//({A}{N}{D})", f"{D}{N}//({A}{B}{C})",
		f"{B}{D}//({A}{N}{P})", f"{C}{D}//({A}{M}{N})",
		]
		noi_dung_loigiai=(f"${kq}$ là khẳng định đúng.")

	if chon==3:		
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({A})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/0,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{A}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định sai?"
		)	

		kq=[
		f"{M}{N}//({A}{B}{C})", f"{M}{P}//({A}{B}{D})", f"{C}{D}//({M}{N}{P})",
		f"{B}{C}//({M}{N}{P})", f"{M}{D}//({A}{B}{C})",
		f"{C}{M}//({A}{N}{D})", f"{D}{N}//({A}{B}{C})",
		f"{B}{D}//({A}{N}{P})", f"{C}{D}//({A}{M}{N})",
		]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{M}{N}//({A}{C}{D})", f"{M}{N}//({P}{C}{D})", f"{M}{N}//({A}{P}{C})", 
		f"{M}{P}//({B}{C}{D})", f"{M}{P}//({N}{C}{D})",	f"{M}{P}//({B}{D}{N})", f"{M}{P}//({D}{N}{C})",
		f"{A}{C}//({M}{N}{P})", f"{A}{C}//({D}{M}{N})",
		f"{B}{D}//({M}{N}{P})", f"{B}{D}//({C}{M}{P})",		
		]
		noi_dung_loigiai=(f"${kq}$ là khẳng định sai.")	

	if chon==4:
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({B})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/-180,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{B}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định đúng?"
		)	

		kq=[
		f"{M}{N}//({A}{C}{D})", f"{A}{C}//({M}{N}{P})", f"{A}{C}//({M}{N}{D})", 
		f"{M}{P}//({A}{C}{D})", f"{M}{P}//({N}{A}{D})",
		f"{N}{P}//({A}{C}{D})", f"{C}{D}//({M}{N}{P})", f"{A}{D}//({M}{N}{P})",
		]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{M}{N}//({B}{C}{D})",	f"{N}{P}//({A}{B}{D})",	f"{D}{M}//({A}{B}{C})",	f"{A}{N}//({M}{C}{D})",
		f"{A}{P}//({B}{C}{D})",	f"{A}{B}//({M}{N}{P})",	f"{A}{D}//({C}{M}{N})", f"{A}{C}//({B}{M}{N})",
		f"{A}{D}//({B}{M}{P})",	]
		noi_dung_loigiai=(f"${kq}$ là khẳng định đúng.")

	if chon==5:
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({B})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/-180,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{B}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định sai?"
		)	

		kq=[
		f"{M}{N}//({B}{C}{D})",	f"{N}{P}//({A}{B}{D})",	f"{D}{M}//({A}{B}{C})",	f"{A}{N}//({M}{C}{D})",
		f"{A}{P}//({B}{C}{D})",	f"{A}{B}//({M}{N}{P})",	f"{A}{D}//({C}{M}{N})", f"{A}{C}//({B}{M}{N})",
		f"{A}{D}//({B}{M}{P})",			
		]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{M}{N}//({A}{C}{D})", f"{A}{C}//({M}{N}{P})", f"{A}{C}//({M}{N}{D})", 
		f"{M}{P}//({A}{C}{D})", f"{M}{P}//({N}{A}{D})",
		f"{N}{P}//({A}{C}{D})", f"{C}{D}//({M}{N}{P})", f"{A}{D}//({M}{N}{P})",
		]
		noi_dung_loigiai=(f"${kq}$ là khẳng định sai.")

	code = my_module.moi_truong_anh_latex(code_hinh_LG)
	file_name_LG=my_module.pdftoimage_timename(code)

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]	

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n {file_name_LG}\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {file_name_LG}\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"		
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"	
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B3_06]-M2. Cho hình chóp tam giác. Xé quan hệ: thuộc, song song, chứa trong
def ghj_7_jkl_L11_C4_B3_06():	
	vertex=random.choice([
		["A","B","C","D"],["S","A","B","C"],["B","C","D","E"], 
		["S","C","D","E"], ["A","B","E","F"], ["B","C","E","F"],["C","D","E","F"] ])
	
	A,B,C,D=vertex
	ten_hinhchop=random.choice([f"tứ diện ${{{A}{B}{C}{D}}}$", f"hình chóp ${{{A}.{B}{C}{D}}}$"])

	name_points=["M","N","P","Q", "I","J"]
	random.shuffle(name_points)
	M,N,P=name_points[0:3]

	code_hinh=code_hinh_tu_dien_noname(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
		
	chon=random.randint(1,4)
	
	if chon==1:
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({A})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/0,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{A}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định đúng?"
		)	

		kq=[
		f"{M}{N}//({A}{C}{D})", f"{M}{N}//({P}{C}{D})", f"{M}{N}//({A}{P}{C})", f"{M}{P}//({B}{C}{D})", 
		f"{M}{N} \\subset ({A}{B}{C})", f"{M}{P} \\subset ({A}{B}{D})",
		f"{B}{M} \\subset ({A}{N}{C})", f"{N}{D} \\subset ({B}{C}{D})",
		f"{C} \\in ({B}{M}{N})", f"{D} \\in ({A}{M}{P})",
		f"{B} \\in ({A}{M}{P})", f"{N} \\in ({A}{B}{C})",	
		
		]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{C}{M}//({A}{N}{D})", f"{D}{N}//({A}{B}{C})",	f"{B}{D}//({A}{N}{P})", 
		f"{M}{C} \\subset ({A}{C}{D})", f"{N}{P} \\subset ({A}{B}{D})",
		f"{M}{P} \\subset ({A}{B}{C})", f"{D}{M} \\subset ({M}{N}{P})",
		f"{N} \\in ({A}{C}{D})", f"{M} \\in ({C}{N}{P})",
		f"{A} \\in ({M}{N}{P})", f"{P} \\in ({B}{C}{D})",

		]
		noi_dung_loigiai=(f"${kq}$ là khẳng định đúng.")

	if chon==2:
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({A})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/0,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{A}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định sai?"
		)	

		kq=[
		f"{C}{M}//({A}{N}{D})", f"{D}{N}//({A}{B}{C})",	f"{B}{D}//({A}{N}{P})", 
		f"{M}{C} \\subset ({A}{C}{D})", f"{N}{P} \\subset ({A}{B}{D})",
		f"{M}{P} \\subset ({A}{B}{C})", f"{D}{M} \\subset ({M}{N}{P})",
		f"{N} \\in ({A}{C}{D})", f"{M} \\in ({C}{N}{P})",
		f"{A} \\in ({M}{N}{P})", f"{P} \\in ({B}{C}{D})",	
		
		]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{M}{N}//({A}{C}{D})", f"{M}{N}//({P}{C}{D})", f"{M}{N}//({A}{P}{C})", f"{M}{P}//({B}{C}{D})", 
		f"{M}{N} \\subset ({A}{B}{C})", f"{M}{P} \\subset ({A}{B}{D})",
		f"{B}{M} \\subset ({A}{N}{C})", f"{N}{D} \\subset ({B}{C}{D})",
		f"{C} \\in ({B}{M}{N})", f"{D} \\in ({A}{M}{P})",
		f"{B} \\in ({A}{M}{P})", f"{N} \\in ({A}{B}{C})",
		]
		noi_dung_loigiai=(f"${kq}$ là khẳng định sai.")

	if chon==3:
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({B})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/-180,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{B}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định đúng?")	

		kq=[
		f"{M}{N}//({A}{C}{D})", f"{A}{C}//({M}{N}{P})", 
		f"{M}{P}//({N}{A}{D})", f"{C}{D}//({M}{N}{P})", f"{A}{D}//({M}{N}{P})"]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{M}{N}//({B}{C}{D})",	f"{N}{P}//({A}{B}{D})",	f"{D}{M}//({A}{B}{C})",
		f"{M} \\in ({B}{C}{D})", f"{N} \\in ({A}{C}{D})", f"{P} \\in ({A}{B}{C})",
		f"{M}{D}\\subset ({A}{B}{C})", f"{A}{N}\\subset ({A}{C}{D})",f"{C}{D}\\subset ({M}{N}{P})"


			]
		noi_dung_loigiai=(f"${kq}$ là khẳng định đúng.")

	if chon==4:
		code_hinh_LG=f"\\begin{{tikzpicture}}[scale=0.7]\n\
		\\coordinate ({B}) at (0,0)   node at ({B}) [left] {{${B}$}};\n\
		\\coordinate ({C}) at (1,-2) node at ({C}) [below] {{${C}$}};\n\
		\\coordinate ({D}) at (4,0)   node at ({D}) [right] {{${D}$}};\n\
		\\coordinate ({A}) at (1,3)   node at ({A}) [above] {{${A}$}};\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({B})!0.5!({C})$);\n\
		\\coordinate ({P}) at ($({B})!0.5!({D})$);\n\
		\\draw [dashed] ({B})--({D}) ({M})--({P}) ({N})--({P}); \n\
		\\draw ({B})--({C}) ({C})--({D}) ({A})--({B}) ({A})--({C}) ({A})--({D}) ({M})--({N}) ;\n\
		\\foreach \\i/\\g in {{{M}/180, {N}/-180,{P}/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

		noi_dung=(
		f"Cho {ten_hinhchop}. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của ${{{A}{B},{B}{C},{B}{D}}}$."		
		f" Khẳng định nào sau đây là khẳng định sai?")	

		kq=[
		f"{M}{N}//({B}{C}{D})",	f"{N}{P}//({A}{B}{D})",	f"{D}{M}//({A}{B}{C})",
		f"{M} \\in ({B}{C}{D})", f"{N} \\in ({A}{C}{D})", f"{P} \\in ({A}{B}{C})",
		f"{M}{D}\\subset ({A}{B}{C})", f"{A}{N}\\subset ({A}{C}{D})",f"{C}{D}\\subset ({M}{N}{P})"]
		random.shuffle(kq)
		kq=kq[0]

		kq_false=[
		f"{M}{N}//({A}{C}{D})", f"{A}{C}//({M}{N}{P})", 
		f"{M}{P}//({N}{A}{D})", f"{C}{D}//({M}{N}{P})", f"{A}{D}//({M}{N}{P})"]
		noi_dung_loigiai=(f"${kq}$ là khẳng định sai.")
	
	code = my_module.moi_truong_anh_latex(code_hinh_LG)
	file_name_LG=my_module.pdftoimage_timename(code)
	

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]	

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n{file_name}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n{file_name_LG}\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n{file_name_LG}\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"		
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
		f"\\loigiai{{\\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"	
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C4_B3_07]-TF-M2. Cho h.chóp-hbh. Xét Đ-S:quan hệ thuộc, chứa trong, song song, giao điểm
def ghj_7_jkl_L11_C4_B3_07():
	S="S"
	vertex=random.choice([
		["A","B","C","D"],["A","B","C","E"],["B","C","D","E"], 
		["C","D","E","F"], ["A","B","E","F"], ["B","C","E","F"]])
	
	A,B,C,D=vertex

	name_points=["M","N","P","Q","G","H","J","K","L"]
	random.shuffle(name_points)

	M,N,G,H,P=name_points[0:5]
	O=random.choice(["O", "I"])

	name_bottom=random.choice(["hình bình hành", "hình chữ nhật", "hình thoi", "hình vuông" ])	

	code_hinh=code_hinh_chop_deu_noname(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là các trung điểm của ${{{A}{B},{C}{D}}}$"
		f" và ${{{G},{H}}}$ lần lượt là trọng tâm các tam giác ${{{S}{A}{B},{S}{C}{D}}}$."
		f" Xét tính đúng-sai của các khẳng định sau:")

	code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
	\\coordinate ({A}) at (0,0);\n\
	\\coordinate ({B}) at (2,-2);\n\
	\\coordinate ({D}) at (5,0);\n\
	\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
	\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
	\\coordinate ({S}) at ($({O})+(0,7)$);\n\
	\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
	\\coordinate ({N}) at ($({C})!0.5!({D})$);\n\
	\\coordinate ({G}) at ($({S})!{2/3}!({M})$);\n\
	\\coordinate ({H}) at ($({S})!{2/3}!({N})$);\n\
	\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({S})--({M});\n\
	\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N}) ({G})--({H}) ({S})--({N});\n\
	\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90, {G}/-180, {H}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
	\\end{{tikzpicture}}\n"	
	code = my_module.moi_truong_anh_latex(code_hinh_LG)
	file_name_LG=my_module.pdftoimage_timename(code)


	kq=random.choice([		
		f"${A}{B}//{M}{N}$",
		f"${G}{H}//{B}{C}$",
		f"${G}{H}//{A}{D}$",
		f"${G}{H}//{M}{N}$",
])

	kq_false=random.choice([
		f"${C}{D}//{G}{H}$",
		f"${A}{B}//{G}{H}$",
		f"${O}{H}//{S}{M}$",
		f"${O}{G}//{S}{N}$",
			])
	
	kq1_T=f"* {kq}" 
	kq1_F=f"{kq_false}"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f" "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq=random.choice([
		f"${G}{H} // ({A}{B}{C}{D})$",
		f"${G}{H} // ({A}{B}{D})$",
		f"${G}{H} // ({B}{C}{D})$",
		f"${B}{C} // ({S}{G}{H})$",
		f"${B}{C} // ({S}{M}{N})$",
		f"${A}{D} // ({S}{G}{H})$",
		f"${A}{D} // ({S}{M}{N})$",])

	kq_false=random.choice([
		f"${M}{N}//({S}{A}{B})$",
		f"${M}{N}//({S}{C}{D})$",	
		f"${O}{N}//({S}{C}{D})$",
		f"${O}{H}//({S}{C}{D})$",
		f"${O}{G}//({S}{A}{B})$",
		f"${B}{H}//({S}{A}{D})$",
		f"${B}{G}//({S}{C}{D})$",])		

	kq2_T=f"* {kq}"
	kq2_F=f" {kq_false}"
	kq2=random.choice([kq2_T, kq2_F])
	if f"{G}{H}" in kq2:
		HDG=(f"$\\dfrac{{{S}{G}}}{{{S}{M}}}=\\dfrac{{{S}{H}}}{{{S}{N}}}={phan_so(2/3)}\\Rightarrow {G}{H} // {M}{N} // {A}{C} // {B}{D}$.\n\n"
			f"Suy ra ${kq}$ là khẳng định đúng.")
			
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq=random.choice([
		f"${O} \\in ({S}{M}{N})$",
		f"${M} \\in ({S}{O}{N})$",
		f"${M} \\in ({S}{G}{N})$",
		f"${N} \\in ({S}{O}{M})$",
		f"${N} \\in ({S}{H}{M})$",
		f"${G} \\notin ({S}{A}{C})$",
		f"${H} \\notin ({S}{B}{D})$",
		f"${O} \\notin ({S}{C}{D})$",
		f"${O} \\notin ({S}{A}{D})$",
		])

	kq_false=random.choice([
		f"${O} \\notin ({S}{M}{N})$",
		f"${M} \\notin ({S}{O}{N})$",
		f"${M} \\notin ({S}{G}{N})$",
		f"${N} \\notin ({S}{O}{M})$",
		f"${N} \\notin ({S}{H}{M})$",

		f"${G} \\in ({S}{A}{C})$",
		f"${H} \\in ({S}{B}{D})$",
		f"${O} \\in ({S}{C}{D})$",
		f"${O} \\in ({S}{A}{D})$",
		])	
	kq3_T=f"* {kq}" 
	kq3_F=f"{kq_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f""
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,6)
	if chon==1:
		kq4_T=f"* Giao điểm của ${{{B}{G}}}$ và $({S}{A}{D})$ là trung điểm của ${{{S}{A}}}$"
		kq4_F=f"Giao điểm của ${{{B}{G}}}$ và $({S}{A}{D})$ là điểm thuộc ${{{random.choice([f"{S}{D}", f"{A}{D}"])}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Vì ${{{G}}}$ là trọng tâm tam giác ${{{S}{A}{B}}}$ nên ${{{B}{G}}}$ đi qua trung điểm ${{{P}}}$ của ${{{S}{A}}}$.\n\n"
			f"Do đó ${B}{G} \\cap ({S}{A}{D})={P}$.")
	
	if chon==2:
		kq4_T=f"* Giao điểm của ${{{C}{H}}}$ và $({S}{A}{D})$ là trung điểm của ${{{S}{D}}}$"
		kq4_F=f"Giao điểm của ${{{C}{H}}}$ và $({S}{A}{D})$ là điểm thuộc ${{{random.choice([f"{S}{A}", f"{A}{D}"])}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Vì ${{{H}}}$ là trọng tâm tam giác ${{{S}{C}{D}}}$ nên ${{{C}{H}}}$ đi qua trung điểm ${{{P}}}$ của ${{{S}{D}}}$.\n\n"
			f"Do đó ${C}{H} \\cap ({S}{A}{D})={P}$.")

	if chon==3:
		kq4_T=f"* Giao điểm của ${{{D}{H}}}$ và $({S}{B}{C})$ là trung điểm của ${{{S}{C}}}$"
		kq4_F=f"Giao điểm của ${{{D}{H}}}$ và $({S}{B}{C})$ là điểm thuộc ${{{random.choice([f"{S}{B}", f"{B}{C}"])}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Vì ${{{H}}}$ là trọng tâm tam giác ${{{S}{C}{D}}}$ nên ${{{D}{H}}}$ đi qua trung điểm ${{{P}}}$ của ${{{S}{C}}}$.\n\n"
			f"Do đó ${D}{H} \\cap ({S}{B}{C})={P}$.")

	if chon==4:
		kq4_T=f"* Giao điểm của ${{{A}{G}}}$ và $({S}{B}{C})$ là trung điểm của ${{{S}{B}}}$"
		kq4_F=f"Giao điểm của ${{{A}{G}}}$ và $({S}{B}{C})$ là điểm thuộc ${{{random.choice([f"{S}{C}", f"{B}{C}"])}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Vì ${{{G}}}$ là trọng tâm tam giác ${{{S}{A}{B}}}$ nên ${{{A}{G}}}$ đi qua trung điểm ${{{P}}}$ của ${{{S}{B}}}$.\n\n"
			f"Do đó ${A}{G} \\cap ({S}{B}{C})={P}$.")

	if chon==5:
		kq4_T=f"* Giao điểm của ${{{M}{C}}}$ và $({S}{A}{D})$ là giao điểm của ${{{M}{C}}}$ và ${{{A}{D}}}$"
		kq4_F=f"Giao điểm của ${{{M}{C}}}$ và $({S}{A}{D})$ là giao điểm của ${{{M}{C}}}$ và ${{{random.choice([f"{S}{A}", f"{S}{D}"])}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Gọi ${P}={M}{C} \\cap {A}{D} \\Rightarrow {P}={M}{C} \\cap ({S}{A}{D})$.")

	if chon==6:
		kq4_T=f"* Giao điểm của ${{{M}{D}}}$ và $({S}{B}{C})$ là giao điểm của ${{{M}{D}}}$ và ${{{B}{C}}}$"
		kq4_F=f"Giao điểm của ${{{M}{D}}}$ và $({S}{B}{C})$ là giao điểm của ${{{M}{D}}}$ và ${{{random.choice([f"{S}{B}", f"{S}{C}"])}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Gọi ${P}={M}{D} \\cap {B}{C} \\Rightarrow {P}={M}{D} \\cap ({S}{B}{C})$.")

	
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

	loigiai_word=f"Lời giải:\n{file_name_LG}\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"    
	    f"\\loigiai{{ \n \\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D11_C4_B3_08]-TF-M2. Cho h.chóp-hbh. Xét Đ-S:quan hệ thuộc, chứa trong, song song, giao tuyến
def ghj_7_jkl_L11_C4_B3_08():
	S="S"
	vertex=random.choice([
		["A","B","C","D"],["A","B","C","E"],["B","C","D","E"], 
		["C","D","E","F"], ["A","B","E","F"], ["B","C","E","F"]])
	
	A,B,C,D=vertex

	name_points=["M","N","P","Q","G","H","J","K","L"]
	random.shuffle(name_points)

	M,N,G,H,P,Q=name_points[0:6]
	O=random.choice(["O", "I"])

	name_bottom=random.choice(["hình bình hành", "hình chữ nhật", "hình thoi", "hình vuông" ])	

	code_hinh=code_hinh_chop_deu_noname(S,A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({C})!0.5!({D})$);\n\
		\\coordinate ({G}) at ($({S})!{2/3}!({M})$);\n\
		\\coordinate ({H}) at ($({S})!{2/3}!({N})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({S})--({M}) ({B})--({G});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N}) ({G})--({H}) ({S})--({N}) ({C})--({H});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90, {G}/-180, {H}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"
	

	noi_dung=(
		f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có đáy là {name_bottom} tâm ${{{O}}}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là các trung điểm của ${{{A}{B},{C}{D}}}$"
		f" và ${{{G},{H}}}$ lần lượt là trọng tâm các tam giác ${{{S}{A}{B},{S}{C}{D}}}$."
		f" Xét tính đúng-sai của các khẳng định sau:")


	kq=random.choice([		

		f"${{{G}{H}}}$ và ${{{C}{D}}}$ chéo nhau",
		f"${{{B}{H}}}$ và ${{{M}{N}}}$ chéo nhau",
		f"${{{C}{G}}}$ và ${{{M}{N}}}$ chéo nhau",
		f"${{{C}{G}}}$ và ${{{M}{N}}}$ chéo nhau",
		f"${{{S}{M}}}$ và ${{{C}{D}}}$ chéo nhau",
		f"${{{S}{N}}}$ và ${{{A}{B}}}$ chéo nhau",

		f"${{{O}{H}}}$ và ${{{S}{M}}}$ cắt nhau",
		f"${{{O}{G}}}$ và ${{{S}{N}}}$ cắt nhau",

		f"${{{C}{M}}}$ và ${{{A}{D}}}$ cắt nhau",
		f"${{{B}{N}}}$ và ${{{A}{D}}}$ cắt nhau",
		f"${{{D}{M}}}$ và ${{{B}{C}}}$ cắt nhau",
		f"${{{A}{N}}}$ và ${{{B}{C}}}$ cắt nhau",])

	kq_false=random.choice([
		
		f"${{{G}{H}}}$ và ${{{C}{D}}}$ {random.choice(["song song", "cắt nhau"])}",
		f"${{{B}{H}}}$ và ${{{M}{N}}}$ {random.choice(["song song", "cắt nhau"])}",
		f"${{{C}{G}}}$ và ${{{M}{N}}}$ {random.choice(["song song", "cắt nhau"])}",
		f"${{{C}{G}}}$ và ${{{M}{N}}}$ {random.choice(["song song", "cắt nhau"])}",
		f"${{{S}{M}}}$ và ${{{C}{D}}}$ {random.choice(["song song", "cắt nhau"])}",

		f"${{{C}{M}}}$ và ${{{A}{D}}}$ {random.choice(["song song", "cắt nhau"])}",
		f"${{{B}{N}}}$ và ${{{A}{D}}}$ {random.choice(["song song", "cắt nhau"])}",
		f"${{{D}{M}}}$ và ${{{B}{C}}}$ {random.choice(["song song", "cắt nhau"])}",
		f"${{{A}{N}}}$ và ${{{B}{C}}}$ {random.choice(["song song", "cắt nhau"])}",	])
	
	kq1_T=f"* {kq}" 
	kq1_F=f"{kq_false}"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f" "
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq=random.choice([
		f"${G}{H} // ({A}{B}{C}{D})$",
		f"${G}{H} // ({A}{B}{D})$",
		f"${G}{H} // ({B}{C}{D})$",
		f"${B}{C} // ({S}{G}{H})$",
		f"${B}{C} // ({S}{M}{N})$",
		f"${A}{D} // ({S}{G}{H})$",
		f"${A}{D} // ({S}{M}{N})$",])

	kq_false=random.choice([
		f"${M}{N}//({S}{A}{B})$",
		f"${M}{N}//({S}{C}{D})$",	
		f"${O}{N}//({S}{C}{D})$",
		f"${O}{H}//({S}{C}{D})$",
		f"${O}{G}//({S}{A}{B})$",
		f"${B}{H}//({S}{A}{D})$",
		f"${B}{G}//({S}{C}{D})$",])		

	kq2_T=f"* {kq}"
	kq2_F=f" {kq_false}"
	kq2=random.choice([kq2_T, kq2_F])
	if f"{G}{H}" in kq2:
		HDG=(f"$\\dfrac{{{S}{G}}}{{{S}{M}}}=\\dfrac{{{S}{H}}}{{{S}{N}}}={phan_so(2/3)}\\Rightarrow {G}{H} // {M}{N} // {A}{C} // {B}{D}$.\n\n"
			f"Suy ra ${kq}$ là khẳng định đúng.")
			
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq=random.choice([
		f"${O}{G} \\subset ({S}{M}{N})$",
		f"${O}{H} \\subset ({S}{M}{N})$",
		f"${M}{H} \\subset ({S}{M}{N})$",
		f"${C}{H} \\subset ({S}{D}{N})$",
		f"${A}{G} \\subset ({S}{B}{M})$",
		f"${B}{G} \\subset ({S}{A}{M})$",
		f"${B}{H} \\subset ({S}{B}{N})$",
		f"${C}{G} \\subset ({S}{M}{C})$",
		])

	kq_false=random.choice([
		f"${O}{G} \\subset ({S}{A}{C})$",
		f"${A}{G} \\subset ({S}{A}{C})$",
		f"${O}{H} \\subset ({S}{B}{D})$",
		f"${D}{H} \\subset ({S}{B}{D})$",
		f"${A}{D} \\subset ({G}{B}{C})$",
		f"${C}{G} \\subset ({S}{A}{C})$",
		f"${B}{H} \\subset ({S}{B}{D})$",
		])	
	kq3_T=f"* {kq}" 
	kq3_F=f"{kq_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f""
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,6)
	
	if chon==1:
		kq4_T=f"* $({G}{B}{C}) \\cap ({S}{A}{D})={P}{Q}$ với ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{D}}}$"
		kq4_F=f"$({G}{B}{C}) \\cap ({S}{A}{D})={random.choice([f"{G}{H}", f"{A}{D}", f"{G}{N}"])}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Gọi ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{D}}}$.\n\n"
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{P}={B}{G}\\cap {S}{A}\\\\ \n\
			{B}{C}\\subset({G}{B}{C})\\\\ \n\
			{A}{D}\\subset({S}{A}{D})\\\\ \n\
			{B}{C} // {A}{D} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({G}{B}{C}) \\cap ({S}{A}{D})={P}{Q}$."
			)	

	if chon==2:
		kq4_T=f"* $({H}{B}{C}) \\cap ({S}{A}{D})={P}{Q}$ với ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{D}}}$"
		kq4_F=f"$({H}{B}{C}) \\cap ({S}{A}{D})={random.choice([f"{G}{H}", f"{A}{D}", f"{M}{N}"])}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Gọi ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{A},{S}{D}}}$.\n\n"
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{P}={B}{G}\\cap {S}{A}\\\\ \n\
			{B}{C}\\subset({H}{B}{C})\\\\ \n\
			{A}{D}\\subset({S}{A}{D})\\\\ \n\
			{B}{C} // {A}{D} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({H}{B}{C}) \\cap ({S}{A}{D})={P}{Q}$."
			)

	if chon==3:
		kq4_T=f"* $({H}{A}{D}) \\cap ({S}{B}{C})={P}{Q}$ với ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{B},{S}{C}}}$"
		kq4_F=f"$({H}{A}{D}) \\cap ({S}{B}{C})={random.choice([f"{G}{H}", f"{A}{D}", f"{M}{N}"])}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Gọi ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{B},{S}{C}}}$.\n\n"
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{Q}={H}{D}\\cap {S}{C}\\\\ \n\
			{B}{C}\\subset({S}{B}{C})\\\\ \n\
			{A}{D}\\subset({H}{A}{D})\\\\ \n\
			{B}{C} // {A}{D} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({H}{A}{D}) \\cap ({S}{B}{C})={P}{Q}$."
			)

	if chon==4:
		kq4_T=f"* $({G}{A}{D}) \\cap ({S}{B}{C})={P}{Q}$ với ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{B},{S}{C}}}$"
		kq4_F=f"$({G}{A}{D}) \\cap ({S}{B}{C})={random.choice([f"{G}{H}", f"{A}{D}", f"{M}{N}"])}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Gọi ${{{P},{Q}}}$ lần lượt là trung điểm của ${{{S}{B},{S}{C}}}$.\n\n"
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{P}={H}{D}\\cap {S}{C}\\\\ \n\
			{B}{C}\\subset({S}{B}{C})\\\\ \n\
			{A}{D}\\subset({G}{A}{D})\\\\ \n\
			{B}{C} // {A}{D} \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({G}{A}{D}) \\cap ({S}{B}{C})={P}{Q}$."
			)

	if chon==5:
		kq4_T=f"* $({G}{M}{N}) \\cap ({S}{C}{D})={S}{N}$"
		kq4_F=f"$({G}{M}{N})  \\cap ({S}{C}{D}) ={random.choice([f"{G}{D}", f"{G}{C}", f"{G}{N}", f"{M}{N}", f"{M}{D}"])}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{S}\\in ({G}{M}{N}) \\cap ({S}{C}{D})\\\\ \n\
			{N}\\in ({G}{M}{N}) \\cap ({S}{C}{D}) \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow ({G}{A}{D}) \\cap ({S}{B}{C})={S}{N}$."
			)

	if chon==6:
		kq4_T=f"* $({H}{M}{N}) \\cap ({S}{A}{B})={S}{M}$"
		kq4_F=f"$({H}{M}{N}) \\cap ({S}{A}{B}) ={random.choice([f"{G}{D}", f"{G}{C}", f"{G}{N}", f"{M}{N}", f"{M}{D}"])}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{S}\\in ({H}{M}{N}) \\cap ({S}{A}{B})\\\\ \n\
			{M}\\in ({H}{M}{N}) \\cap ({S}{A}{B}) \n\
			\\end{{array}} \\right.$"
			f"$\\Rightarrow({H}{M}{N}) \\cap ({S}{A}{B})={S}{M}$."
			)
	
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon in [1,2]:
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({C})!0.5!({D})$);\n\
		\\coordinate ({P}) at ($({S})!0.5!({A})$);\n\
		\\coordinate ({Q}) at ($({S})!0.5!({D})$);\n\
		\\coordinate ({G}) at ($({S})!{2/3}!({M})$);\n\
		\\coordinate ({H}) at ($({S})!{2/3}!({N})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({S})--({M}) ({B})--({G});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N}) ({G})--({H}) ({S})--({N}) ({C})--({H});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90, {G}/-180, {H}/0, {P}/-180, {Q}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

	if chon in [3,4]:
		code_hinh_LG=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
		\\coordinate ({A}) at (0,0);\n\
		\\coordinate ({B}) at (2,-2);\n\
		\\coordinate ({D}) at (5,0);\n\
		\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
		\\coordinate ({O}) at ($({A})!0.5!({C})$);\n\
		\\coordinate ({S}) at ($({O})+(0,7)$);\n\
		\\coordinate ({M}) at ($({A})!0.5!({B})$);\n\
		\\coordinate ({N}) at ($({C})!0.5!({D})$);\n\
		\\coordinate ({P}) at ($({S})!0.5!({B})$);\n\
		\\coordinate ({Q}) at ($({S})!0.5!({C})$);\n\
		\\coordinate ({G}) at ($({S})!{2/3}!({M})$);\n\
		\\coordinate ({H}) at ($({S})!{2/3}!({N})$);\n\
		\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C}) ({S})--({M}) ({A})--({G});\n\
		\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D}) ({M})--({N}) ({G})--({H}) ({S})--({N}) ({D})--({H});\n\
		\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0,{M}/-180,{N}/0, {O}/-90, {G}/-180, {H}/0, {P}/-180, {Q}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}\n"

	code = my_module.moi_truong_anh_latex(code_hinh_LG)
	file_name_LG=my_module.pdftoimage_timename(code)

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

	loigiai_word=f"Lời giải:\n{file_name_LG}\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"    
	    f"\\loigiai{{ \n \\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#Bài 4 - Hai mặt phẳng song song
#[D11_C4_B4_03]. Cho hình lăng trụ tam giác. Xét sự song song của 2 mp.
def ghj_7_jkl_L11_C4_B4_03():
	ten_hinhlangtru=random.choice(["ABC.A'B'C'", "ABC.A_1B_1C_1"])
	if ten_hinhlangtru=="ABC.A'B'C'":
		a,b,c,a1,b1,c1="A","B","C","A'","B'","C'"
	else:
		a,b,c,a1,b1,c1="A","B","C","A_1","B_1","C_1"

	diem_1 = random.choice(["D","E","F"])
	diem_2 = random.choice(["G","H","I"])
	diem_3 =random.choice(["K","M","N"])

	canh= f"${{{a}{a1}}},{{{b}{b1}}}$ và ${{{c}{c1}}}$"

	mp=f"${{({diem_1}{diem_2}{diem_3})}}$" 
	kq=random.choice([f"{mp}// ${{(ABC)}}$", f"{mp}// ${{({a1}{b1}{c1})}}$"])
	kq2=random.choice([f"{mp}// ${{({a1}BC)}}$", f"{mp}// ${{({b1}AC)}}$", f"{mp}// ${{({c1}AB)}}$"])
	kq3=random.choice([f"{mp}// ${{(A{b1}{c1})}}$", f"{mp}// ${{(B{c1}{a1})}}$", f"{mp}// ${{(C{b1}{a1})}}$"])
	kq4=random.choice([f"{mp}// ${{(AB{b1}{a1})}}$", f"{mp}// ${{(AC{c1}{a1})}}$", f"{mp}// ${{(BC{c1}{b1})}}$"])	
	
	code=my_module.codelatex_hinh_langtruxien_tamgiac(a,b,c,a1,b1,c1)
	file_name=my_module.pdftoimage_timename(code)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình lăng trụ ${{{ten_hinhlangtru}}}$. Gọi ${{{diem_1},{diem_2}}}$ và ${{{diem_3}}}$ lần lượt là trung điểm của các cạnh {canh}. Tìm khẳng định đúng." 
	debai= f"{noi_dung}\n\n"\
	    f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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

#[D11_C4_B4_09]. (THÔNG HIỂU) Cho hình lăng trụ tam giác. Xét sự song song của 2 mp. 
def ghj_7_jkl_L11_C4_B4_09():
	ten_hinhlangtru=random.choice(["ABC.A'B'C'", "ABC.A_1B_1C_1"])
	if ten_hinhlangtru=="ABC.A'B'C'":
		a,b,c,a1,b1,c1="A","B","C","A'","B'","C'"
	else:
		a,b,c,a1,b1,c1="A","B","C","A_1","B_1","C_1"
	#Tạo M,N,P là trung điểm AA',BB',CC' trong hình gốc
	diem_M = random.choice(["D","E","F"])
	diem_N = random.choice(["G","H","I"])
	diem_P =random.choice(["K","M","N"])

	canh= f"${{{a}{a1}}},{{{b}{b1}}}$ và ${{{c}{c1}}}$"

	chon_mp=random.choice(["mp1","mp2","mp3"])
	if chon_mp=="mp1":	
		mp1=f"${{({diem_M}BC)}}$" 
		kq=f"{mp1}//${{({a1}{diem_N}{diem_P})}}$"
		kq2=random.choice([f"{mp1}//${{({a1}BC)}}$", f"{mp1}//${{({b1}AC)}}$", f"{mp1}//${{({c1}AB)}}$"])
		kq3=random.choice([f"{mp1}//${{({a1}{b1}{c1})}}$", f"{mp1}//${{(B{c1}{a1})}}$", f"{mp1}//${{(C{b1}{a1})}}$"])
		kq4=random.choice([f"{mp1}//${{({diem_M}{b1}{c1})}}$", f"{mp1}//${{(A{b1}{c1})}}$", f"{mp1}//${{(ABC)}}$"])
	
	if chon_mp=="mp2":
		mp2=f"${{({c1}{diem_M}{diem_N})}}$" 
		kq=f"{mp2}//${{({diem_P}AB)}}$"
		kq2=random.choice([f"{mp2}//${{({a1}BC)}}$", f"{mp2}//${{({b1}AC)}}$", f"{mp2}//${{({c1}AB)}}$"])
		kq3=f"{mp2}//${{({diem_P}{a1}{b1})}}$"	
		kq4=random.choice([f"{mp2}//${{(ABC)}}$", f"{mp2}//${{({a1}{b1}{c1})}}$"])
	
	if chon_mp=="mp3":
		mp3=f"${{({b1}{diem_M}{diem_P})}}$" 
		kq=f"{mp3}//${{({diem_N}AC)}}$"
		kq2=random.choice([f"{mp3}//${{({a1}BC)}}$", f"{mp3}//${{({b1}AC)}}$", f"{mp3}//${{({c1}AB)}}$"])
		kq3=random.choice([f"{mp3}//${{({a1}AC)}}$", f"{mp3}//${{({diem_N}{a1}{c1})}}$" ])
		kq4=random.choice([f"{mp3}//${{(ABC)}}$", f"{mp3}//${{({a1}{b1}{c1})}}$"])	
	
	code=my_module.codelatex_hinh_langtruxien_tamgiac(a,b,c,a1,b1,c1)
	file_name=my_module.pdftoimage_timename(code)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình lăng trụ ${{{ten_hinhlangtru}}}$. Gọi ${{{diem_M},{diem_N}}}$ và ${{{diem_P}}}$ lần lượt là trung điểm của các cạnh {canh}. Tìm khẳng định đúng." 
	debai= f"{noi_dung}\n\n"\
	    f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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

#[D11_C4_B4_05]. Tìm khẳng định đúng về hình lăng trụ.
def ghj_7_jkl_L11_C4_B4_05():	
	chon=random.randint(1,6)
	if chon == 1:
		kq=random.choice(["Các cạnh bên song song và bằng nhau"])
		kq2=random.choice(["Độ dài cạnh bên bằng độ dài cạnh đáy", "Độ dài cạnh bên gấp đôi độ dài cạnh đáy"])
		kq3=random.choice(["Các mặt bên là hình chữ nhật", "Các mặt bên là hình vuông"])
		kq4=random.choice(["Đáy là tam giác đều", "Đáy là tam giác cân", "Đáy là tam giác vuông"])
	elif chon == 2:
		kq=random.choice(["Các mặt bên là các hình bình hành"])
		kq2=random.choice(["Cạnh bên vuông góc với cạnh đáy", "Cạnh bên và cạnh đáy là các đường chéo nhau"])
		kq3=random.choice(["Hình lăng trụ tứ giác có đáy là hình vuông", "Hình lăng trụ tứ giác có đáy là hình bình hành"])
		kq4=random.choice(["Các cạnh bên là các đường chéo nhau", "Các cạnh bên là đôi một cắt nhau"])
	elif chon==3:
		kq=random.choice(["Hai đáy có diện tích bằng nhau", "Hai đáy có chu vi bằng nhau"])
		kq2="Hai đáy là hai hình bình hành"
		kq3="Hai đáy là hai hình tam giác"
		kq4="Hai đáy là hai hình vuông"
	elif chon==4:
		kq=random.choice(["Hình lăng trụ tam giác có đáy là hình tam giác"])
		kq2="Hình lăng trụ tam giác có đáy là các tam giác cân"
		kq3="Hình lăng trụ tam giác có đáy là các tam giác đều"
		kq4="Hình lăng trụ tam giác có đáy là các tam giác vuông"
	else:
		kq=random.choice(["Hình lăng trụ tứ giác có đáy là hình tứ giác"])
		kq2="Hình lăng trụ tứ giác có đáy là các hình vuông"
		kq3="Hình lăng trụ tứ giác có đáy là các hình bình hành"
		kq4="Hình lăng trụ tứ giác có đáy là các hình chữ nhật"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Tìm khẳng định đúng về hình lăng trụ."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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


#[D11_C4_B4_06]. Tìm cặp điểm đối diện của hình hộp.
def ghj_7_jkl_L11_C4_B4_06():
	ten_langtru=random.choice(["ABCD.A'B'C'D'", "ABCD.EFGH", "ABCD.A_1B_1C_1D_1"])
	if ten_langtru=="ABCD.A'B'C'D'":
		code=my_module.codelatex_hinh_hop("A","B","C","D","A'","B'","C'","D'")
		kq=random.choice(["$A$ và ${{C'}}$", "$B$ và ${{D'}}$", "$C$ và ${{A'}}$", "$D$ và ${{B'}}$"])
		kq2=random.choice(["$A$ và $C$", "${{A'}}$ và $D$"])
		kq3=random.choice(["${{A'}}$ và ${{C'}}$", "${{B'}}$ và ${{D'}}$"])
		kq4=random.choice(["$A$ và ${{B'}}$", "$B$ và ${{C'}}$"])

	elif ten_langtru=="ABCD.EFGH":
		code=my_module.codelatex_hinh_hop("A","B","C","D","E","F","G","H")
		kq=random.choice(["$A$ và $G$", "$B$ và $H$", "$C$ và $E$", "$D$ và $F$"])
		kq2=random.choice(["$A$ và $C$", "$E$ và $D$"])
		kq3=random.choice(["$E$ và $G$", "$F$ và $H$"])
		kq4=random.choice(["$A$ và $F$", "$B$ và $G$"])
	else:
		code=my_module.codelatex_hinh_hop("A","B","C","D","A_1","B_1","C_1","D_1")
		kq=random.choice(["$A$ và ${{C_1}}$", "$B$ và ${{D_1}}$", "$C$ và ${{A_1}}$", "$D$ và ${{B_1}}$"])
		kq2=random.choice(["$A$ và $C$", "${{A_1}}$ và $D$"])
		kq3=random.choice(["${{A_1}}$ và ${{C_1}}$", "${{B_1}}$ và ${{D_1}}$"])
		kq4=random.choice(["$A$ và ${{B_1}}$", "$B$ và ${{C_1}}$"])	

	file_name=my_module.pdftoimage_timename(code)

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình hộp ${{{ten_langtru}}}$. Cặp điểm nào sau đây là hai đỉnh đối diện." 
	debai= f"{noi_dung}\n\n"\
	    f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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

#[D11_C4_B4_07]. Cho hình hộp. Xác định sự song song của một đường với các đường.
def ghj_7_jkl_L11_C4_B4_07():
	ten_langtru=random.choice(["ABCD.A'B'C'D'", "ABCD.EFGH", "ABCD.A_1B_1C_1D_1"])	
	de_MN=""
	#Tìm 2 đường song song.
	if ten_langtru=="ABCD.A'B'C'D'":
		code=my_module.codelatex_hinh_hop("A","B","C","D","A'","B'","C'","D'")
		chon_duong=random.choice(["MN", "CD'", "AB'", "B'C"])
		if chon_duong=="MN":
			de_MN="Gọi ${{M,N}}$ lần lượt là các trung điểm của các cạnh ${{AB,CD}}$. "
			kq=random.choice([f"${{MN}}$//${{A'D'}}$", "${{MN}}$//${{B'C'}}$","${{MN}}$//${{BC}}$"])
			kq2=random.choice([f"${{MN}}$//${{C'D'}}$", "${{MN}}$//${{A'B'}}$"])
			kq3=random.choice([f"${{MN}}$//${{BB'}}$", "${{MN}}$//${{CC'}}$"])
			kq4=random.choice([f"${{MN}}$//${{B'D'}}$", "${{MN}}$//${{A'C'}}$"])
		if chon_duong=="CD'":
			kq=f"${{CD'}}$//${{A'B}}$"
			kq2=f"${{CD'}}$//${{AB'}}$"
			kq3=f"${{CD'}}$//${{B'D}}$"
			kq4=f"${{CD'}}$//${{AB}}$"
		if chon_duong=="AB'":
			kq=f"${{AB'}}$//${{C'D}}$"
			kq2=f"${{AB'}}$//${{CD'}}$"
			kq3=f"${{AB'}}$//${{CD}}$"
			kq4=f"${{AB'}}$//${{BC}}$"
		if chon_duong=="B'C":
			kq=f"${{B'C}}$//${{A'D}}$"
			kq2=f"${{B'C}}$//${{AD'}}$"
			kq3=f"${{B'C}}$//${{AD}}$"
			kq4=f"${{B'C}}$//${{AB}}$"
	elif ten_langtru=="ABCD.EFGH":
		code=my_module.codelatex_hinh_hop("A","B","C","D","E","F","G","H")
		chon_duong=random.choice(["MN", "CH", "AF", "FC"])
		if chon_duong=="MN":
			de_MN="Gọi ${{M,N}}$ lần lượt là các trung điểm của các cạnh ${{AB,CD}}$. "
			kq=random.choice([f"${{MN}}$//${{EH}}$", "${{MN}}$//${{FG}}$","${{MN}}$//${{BC}}$"])
			kq2=random.choice([f"${{MN}}$//${{GH}}$", "${{MN}}$//${{EF}}$"])
			kq3=random.choice([f"${{MN}}$//${{BF}}$", "${{MN}}$//${{CG}}$"])
			kq4=random.choice([f"${{MN}}$//${{FH}}$", "${{MN}}$//${{EG}}$"])
		if chon_duong=="CH":
			kq=f"${{CH}}$//${{EB}}$"
			kq2=f"${{CH}}$//${{AF}}$"
			kq3=f"${{CH}}$//${{FD}}$"
			kq4=f"${{CH}}$//${{AB}}$"
		if chon_duong=="AF":
			kq=f"${{AF}}$//${{GD}}$"
			kq2=f"${{AF}}$//${{CH}}$"
			kq3=f"${{AF}}$//${{CD}}$"
			kq4=f"${{AF}}$//${{BC}}$"
		if chon_duong=="FC":
			kq=f"${{FC}}$//${{ED}}$"
			kq2=f"${{FC}}$//${{AH}}$"
			kq3=f"${{FC}}$//${{AD}}$"
			kq4=f"${{FC}}$//${{AB}}$"	
	else:
		code=my_module.codelatex_hinh_hop("A","B","C","D","A_1","B_1","C_1","D_1")
		chon_duong=random.choice(["MN", "CD_1", "AB_1", "B_1C"])
		if chon_duong=="MN":
			de_MN="Gọi ${{M,N}}$ lần lượt là các trung điểm của các cạnh ${{AB,CD}}$. "
			kq=random.choice([f"${{MN}}$//${{A_1D_1}}$", "${{MN}}$//${{B_1C_1}}$","${{MN}}$//${{BC}}$"])
			kq2=random.choice([f"${{MN}}$//${{C_1D_1}}$", "${{MN}}$//${{A_1B_1}}$"])
			kq3=random.choice([f"${{MN}}$//${{BB_1}}$", "${{MN}}$//${{CC_1}}$"])
			kq4=random.choice([f"${{MN}}$//${{B_1D_1}}$", "${{MN}}$//${{A_1C_1}}$"])
		if chon_duong=="CD_1":
			kq=f"${{CD_1}}$//${{A_1B}}$"
			kq2=f"${{CD_1}}$//${{AB_1}}$"
			kq3=f"${{CD_1}}$//${{B_1D}}$"
			kq4=f"${{CD_1}}$//${{AB}}$"
		if chon_duong=="AB_1":
			kq=f"${{AB_1}}$//${{C_1D}}$"
			kq2=f"${{AB_1}}$//${{CD_1}}$"
			kq3=f"${{AB_1}}$//${{CD}}$"
			kq4=f"${{AB_1}}$//${{BC}}$"
		if chon_duong=="B_1C":
			kq=f"${{B_1C}}$//${{A_1D}}$"
			kq2=f"${{B_1C}}$//${{AD_1}}$"
			kq3=f"${{B_1C}}$//${{AD}}$"
			kq4=f"${{B_1C}}$//${{AB}}$"

	file_name=my_module.pdftoimage_timename(code)

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình hộp ${{{ten_langtru}}}$.{de_MN} Tìm khẳng định đúng."
	debai= f"{noi_dung}\n\n"\
	    f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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

#[D11_C4_B4_08]. Cho hình hộp. Xác định sự song song của hai đường tùy ý.
def ghj_7_jkl_L11_C4_B4_08():

	ten_langtru=random.choice(["ABCD.A'B'C'D'", "ABCD.EFGH", "ABCD.A_1B_1C_1D_1"])
	#Tìm 2 đường song song.
	if ten_langtru=="ABCD.A'B'C'D'":
		code=my_module.codelatex_hinh_hop("A","B","C","D","A'","B'","C'","D'")
	
		kq=random.choice([f"${{MN}}$//${{B'D'}}$", "${{A'B}}$//${{CD'}}$", \
							"${{A'M}}$//${{D'P}}$", "$NP$//${{A'C'}}$"])

		kq2=random.choice(["${{BB'}}$//${{D'M}}$", "${{B'N}}$//${{D'P}}$", "${{BC}}$//${{A'C'}}$"])

		kq3=random.choice(["${{A'B}}$//${{C'D}}$", "${{MP}}$//${{B'D'}}$", "${{CD}}$//${{MN}}$"])

		kq4=random.choice(["${{AM}}$//${{BD}}$", "${{C'P}}$//${{A'N}}$", "${{BM}}$//${{B'D'}}$"])

	elif ten_langtru=="ABCD.EFGH":
		code=my_module.codelatex_hinh_hop("A","B","C","D","E","F","G","H")

		kq=random.choice([f"${{MN}}$//${{FH}}$", "${{EB}}$//${{CH}}$", \
							"${{EM}}$//${{HP}}$", "${{NP}}$//${{EG}}$"])

		kq2=random.choice(["${{BF}}$//${{HM}}$", "${{FN}}$//${{HP}}$", "${{BC}}$//${{EG}}$"])

		kq3=random.choice(["${{EB}}$//${{GD}}$", "${{MP}}$//${{FH}}$", "${{CD}}$//${{MN}}$"])

		kq4=random.choice(["${{AM}}$//${{BD}}$", "${{GP}}$//${{EN}}$", "${{BM}}$//${{FH}}$"])		

	else:
		code=my_module.codelatex_hinh_hop("A","B","C","D","A_1","B_1","C_1","D_1")
		kq=random.choice([f"${{MN}}$//${{B_1D_1}}$", "${{A_1B}}$//${{CD_1}}$", \
							"${{A_1M}}$//${{D_1P}}$", "${{NP}}$//${{A_1C_1}}"])

		kq2=random.choice(["${{BB_1}}$//${{D_1M}}$", "${{B_1N}}$//${{D_1P}}$", "${{BC}}$//${{A_1C_1}}$"])

		kq3=random.choice(["${{A_1B}}$//${{C_1D}}$", "${{MP}}$//${{B_1D_1}}$", "${{CD}}$//${{MN}}$"])

		kq4=random.choice(["${{AM}}$//${{BD}}$", "${{C_1P}}$//${{A_1N}}$", "${{BM}}$//${{B_1D_1}}$"])

	file_name=my_module.pdftoimage_timename(code)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình hộp ${{{ten_langtru}}}$. Gọi ${{M,N,P}}$ lần lượt là các trung điểm của các cạnh ${{AB,AD,CD}}$. Tìm khẳng định đúng."
	debai= f"{noi_dung}\n\n"\
	    f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t   C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

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