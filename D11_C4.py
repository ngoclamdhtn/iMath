import math
import random
from fractions import Fraction
import my_module
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

def code_hinh_chop_deu(S,A,B,C,D):
	code=f" \\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
\\coordinate ({A}) at (0,0);\n\
\\coordinate ({B}) at (2,-2);\n\
\\coordinate ({D}) at (5,0);\n\
\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
\\coordinate (O) at ($({A})!0.5!({C})$);\n\
\\coordinate ({S}) at ($(O)+(0,7)$);\n\
\\draw({S})--({A}) ({S})--({B}) ({S})--({C}) ({A})--({B}) ({B})--({C});\n\
\\draw[dashed,thin]({A})--({C}) ({A})--({D}) ({C})--({D}) ({S})--({D}) ({B})--({D});\n\
\\foreach \\i/\\g in {{{S}/90,{A}/180,{B}/-90,{C}/-90,{D}/0}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
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
	#file_name=my_module.pdftoimage_timename(code)
	file_name=""

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
	chon=5
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

#[D11_C4_B2_01]. Cho hình chóp. Xét hai đường thẳng song song - đường trung bình.
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

#Bài 3 - Đường thẳng song song với mặt phẳng 

#[D11_C4_B3_01]. Cho hình chóp đáy h.b.h. Xét sự song song của một đường thẳng với các mp.
def ghj_7_jkl_L11_C4_B3_01():
	ten_hinhchop=random.choice(["S.ABCD"])
	hinh=random.choice(["hình bình hành", "hình vuông", "hình chữ nhật", "hình thoi"])
	diem_1 = random.choice(["M","I","G","P"])
	diem_2 = random.choice(["N","K","H","Q"]) 
	canh= random.choice(["${AB}$ và ${BC}$", "${BC}$ và ${CD}$", "${CD}$ và ${SD}$", "${SB}$ và ${SD}$"])
	if canh=="${AB}$ và ${BC}$":
		kq=f"${{{diem_1}{diem_2}}}$//${{(SAC)}}$"
		kq2=f"${{{diem_1}{diem_2}}}$//${{(ACD)}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SAD)}}$", f"${{{diem_1}{diem_2}}}$//${{(SAB)}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SBD)}}$", f"${{{diem_1}{diem_2}}}$//${{(ABCD)}}$"])

	if canh=="${BC}$ và ${CD}$":
		kq=f"${{{diem_1}{diem_2}}}$//${{(SBD)}}$"
		kq2=f"${{{diem_1}{diem_2}}}$//${{(ABD)}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SAD)}}$", f"${{{diem_1}{diem_2}}}$//${{(ABCD)}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SA{diem_1})}}$", f"${{{diem_1}{diem_2}}}$//${{(SD{diem_2})}}$"])

	if canh=="${CD}$ và ${SD}$":
		kq=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SBC)}}$", f"${{{diem_1}{diem_2}}}$//${{(SAC)}}$"])
		kq2=f"${{{diem_1}{diem_2}}}$//${{(SCD)}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SAB)}}$", f"${{{diem_1}{diem_2}}}$//${{(ABCD)}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SB{diem_1})}}$", f"${{{diem_1}{diem_2}}}$//${{(SA{diem_2})}}$"])

	if canh=="${SB}$ và ${SD}$":
		kq=random.choice([f"${{{diem_1}{diem_2}}}$//${{(ABC)}}$", f"${{{diem_1}{diem_2}}}$//${{(ABCD)}}$"])
		kq2=f"${{{diem_1}{diem_2}}}$//${{(SCD)}}$"
		kq3=random.choice([f"${{{diem_1}{diem_2}}}$//${{(SBD)}}$", f"${{{diem_1}{diem_2}}}$//${{(SAB)}}$"])
		kq4=random.choice([f"${{{diem_1}{diem_2}}}$//${{(AC{diem_1})}}$", f"${{{diem_1}{diem_2}}}$//${{(CD{diem_2})}}$"])
	
	
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