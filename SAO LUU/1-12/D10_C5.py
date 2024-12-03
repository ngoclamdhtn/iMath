import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(10000000000000))
    return m
#Tạo hàm chứa chuỗi latex vecto
def vec(st):
	return f"\\overrightarrow{{{st}}}"

def tao_ngoac(a):
	if a>0:
		show= f"{a}"
	else:
		show=f"({a})"
	return show

def show_hieu(a,b):
	if b>=0:
		show=f"{a}-{b}"
	else:
		show=f"{a}({b})"
	return show
def show_tich(a,b):
	if b>=0:
		show=f"{a}.{b}"
	else:
		show=f"{a}.({b})"
	return show

def code_latex_hinhchunhat(A,B,C,D):
	code=f"\\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
\\coordinate ({A}) at (0,3);\n\
\\coordinate ({B}) at (5,3);\n\
\\coordinate ({D}) at (0,0);\n\
\\coordinate ({C}) at ($({B})+({D})-({A})$);\n\
\\draw({A})--({B})--({C})--({D})--cycle;\n\
\\foreach \\i/\\g in {{{A}/90,{B}/90,{C}/-90,{D}/-90}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
\\end{{tikzpicture}}\n"
	return code

def code_latex_hinhbinhhanh(a,b,c,d):
    code=rf"""\begin{{tikzpicture}}[line join=round, line cap=round,thick]
\coordinate ({a}) at (1,3);
\coordinate ({b}) at (6,3);
\coordinate ({d}) at (0,0);
\coordinate ({c}) at ($({b})+({d})-({a})$);
\draw({a})--({b})--({c})--({d})--cycle;
\foreach \i/\g in {{{a}/90,{b}/90,{c}/-90,{d}/-90}}{{\draw[fill=white](\i) circle (1.5pt) ($(\i)+(\g:3mm)$) node[scale=1]{{$\i$}};}}
\end{{tikzpicture}}"""
    return code


#Bài 1 - Các định nghĩa véctơ
#[D10_C5_B1_01]-M2. Cho tam giác đều. Tìm khẳng định sai
def y7y7u_L10_C5_B1_01():
	A=["A","B","M","D"]
	B=["B","C","N","E"]
	C=["C","D","P","F"]
	i=random.randint(0,3)
	A, B, C = A[i], B[i], C[i]
	tamgiac=f"{A}{B}{C}"
	noi_dung=f"Cho tam giác đều ${{{tamgiac}}}$. Khẳng định nào sau đây là khẳng định sai?"
	

	kq=random.choice([f'{vec(f"{A}{B}")}={vec(f"{B}{C}")}', f'{vec(f"{A}{B}")}={vec(f"{A}{C}")}', 
		f'{vec(f"{B}{A}")}={vec(f"{B}{C}")}' ])

	kq2=random.choice([f'|{vec(f"{A}{B}")}|=|{vec(f"{B}{C}")}|', f'|{vec(f"{A}{B}")}|=|{vec(f"{A}{C}")}|',
	 f'|{vec(f"{B}{A}")}|=|{vec(f"{B}{C}")}|' ])

	kq3=random.choice([f'${vec(f"{A}{B}")}$ và ${vec(f"{B}{C}")}$', f'${vec(f"{A}{B}")}$ và ${vec(f"{A}{C}")}$', 
		f'${vec(f"{B}{A}")}$ và ${vec(f"{B}{C}")}$'])

	kq4=random.choice([f'${vec(f"{A}{B}")}$ và ${vec(f"{B}{C}")}$', f'${vec(f"{A}{B}")}$ và ${vec(f"{A}{C}")}$', 
		f'${vec(f"{B}{A}")}$ và ${vec(f"{B}{C}")}$'])
	noi_dung_loigiai=f"${kq}$ là khẳng định sai."

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"{kq3} không {random.choice(["cùng phương", "cùng hướng"])}"
	pa_D= f"{kq4} không bằng nhau"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B1_02]-M2. Cho hình dạng bình hành. Tìm khẳng định sai về vectơ bằng nhau, độ dài bằng nhau.
def y7y7u_L10_C5_B1_02():
	A=["A","A","M","O", "A"]
	B=["B","B","N","A", "B"]
	C=["C","E","P","B", "M"]
	D=["D","F","Q","C", "N"]

	i=random.randint(0,4)
	A, B, C, D = A[i], B[i], C[i], D[i]
	hinh=random.choice(["hình bình hành", "hình chữ nhật", "hình vuông" ])
	ten=f"{{{A}{B}{C}{D}}}"
	noi_dung=f"Cho {hinh} ${ten}$. Khẳng định nào sau đây là khẳng định sai?"
	

	kq=random.choice([f'{vec(f"{A}{D}")}={vec(f"{C}{B}")}', f'{vec(f"{D}{A}")}={vec(f"{B}{C}")}',
	f'{vec(f"{A}{B}")}={vec(f"{C}{D}")}', f'{vec(f"{B}{A}")}={vec(f"{D}{C}")}',
	f'{vec(f"{A}{C}")}={vec(f"{B}{D}")}', f'{vec(f"{C}{A}")}={vec(f"{D}{B}")}'])

	kq2=random.choice([f'|{vec(f"{A}{D}")}|=|{vec(f"{C}{B}")}|', f'|{vec(f"{D}{A}")}|=|{vec(f"{B}{C}")}|',
	f'|{vec(f"{A}{B}")}|=|{vec(f"{C}{D}")}|', f'|{vec(f"{B}{A}")}|=|{vec(f"{D}{C}")}|'])

	kq3=random.choice([f'{vec(f"{A}{D}")}={vec(f"{B}{C}")}', f'{vec(f"{D}{A}")}={vec(f"{C}{B}")}',
	f'{vec(f"{A}{B}")}={vec(f"{D}{C}")}'])

	kq4=random.choice([f'{vec(f"{B}{A}")}={vec(f"{C}{D}")}'])

	noi_dung_loigiai=f"${kq}$ là khẳng định sai."

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B1_03]-M2. Cho hình dạng bình hành. Tìm khẳng định đúng về vectơ hướng, phương.
def y7y7u_L10_C5_B1_03():
	A=["A","A","M","O", "A"]
	B=["B","B","N","A", "B"]
	C=["C","E","P","B", "M"]
	D=["D","F","Q","C", "N"]

	i=random.randint(0,4)
	A, B, C, D = A[i], B[i], C[i], D[i]
	hinh=random.choice(["hình bình hành", "hình chữ nhật", "hình vuông" ])
	ten=f"{{{A}{B}{C}{D}}}"
	noi_dung=f"Cho {hinh} ${ten}$. Khẳng định nào sau đây là khẳng định đúng?"

	chon=random.randint(1,2)
	if chon==1:
		kq=random.choice([f'${vec(f"{A}{D}")}$ và ${vec(f"{B}{C}")}$',
						f'${vec(f"{A}{B}")}$ và ${vec(f"{D}{C}")}$',
						f'${vec(f"{D}{A}")}$ và ${vec(f"{C}{B}")}$',
						f'${vec(f"{B}{A}")}$ và ${vec(f"{C}{D}")}$',
						])
		pa_A= f"*{kq} là {random.choice(["cùng hướng", "cùng phương"])}"
	
	if chon==2:
		kq=random.choice([f'${vec(f"{A}{D}")}$ và ${vec(f"{C}{B}")}$',
						f'${vec(f"{A}{B}")}$ và ${vec(f"{C}{D}")}$',
						f'${vec(f"{D}{A}")}$ và ${vec(f"{B}{C}")}$',
						f'${vec(f"{B}{A}")}$ và ${vec(f"{D}{C}")}$',
						])
		pa_A= f"*{kq} là {random.choice(["ngược hướng", "cùng phương"])}"
	

	kq2=random.choice([f'${vec(f"{A}{B}")}$ và ${vec(f"{A}{D}")}$',
					f'${vec(f"{A}{B}")}$ và ${vec(f"{A}{C}")}$',
					f'${vec(f"{B}{A}")}$ và ${vec(f"{B}{C}")}$',
					f'${vec(f"{C}{D}")}$ và ${vec(f"{C}{B}")}$'])
	pa_B= f"{kq2} là {random.choice(["ngược hướng", "cùng hướng"])}"

	kq3=random.choice([f'${vec(f"{A}{C}")}$ và ${vec(f"{B}{D}")}$',
					f'${vec(f"{A}{D}")}$ và ${vec(f"{C}{D}")}$',
					f'${vec(f"{A}{C}")}$ và ${vec(f"{C}{D}")}$',
					f'${vec(f"{A}{B}")}$ và ${vec(f"{B}{D}")}$'
					])
	pa_C= f"{kq3} là {random.choice(["cùng phương"])}"

	kq4=random.choice([f'${vec(f"{A}{C}")}$ và ${vec(f"{C}{A}")}$',
					f'${vec(f"{B}{D}")}$ và ${vec(f"{D}{B}")}$',
					f'${vec(f"{A}{B}")}$ và ${vec(f"{C}{D}")}$',
					f'${vec(f"{C}{D}")}$ và ${vec(f"{D}{C}")}$',
					f'${vec(f"{B}{C}")}$ và ${vec(f"{A}{D}")}$'
					])
	pa_D= f"{kq4} là khác phương"

	noi_dung_loigiai=f"{kq} là khẳng định đúng."	


	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B1_04]-M2. Cho trung điểm của đoạn. Tìm khẳng định đúng về hướng, phương, véctơ bằng nhau, độ dài bằng nhau
def y7y7u_L10_C5_B1_04():
	A=["A","C","E","P", "M"]
	B=["B","D","F","Q", "N"]
	I=random.choice(["I","K","O","H"])
	i=random.randint(0,4)
	A, B= A[i], B[i]

	noi_dung=f"Gọi ${{{I}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$. Khẳng định nào sau đây là khẳng định đúng?"
	
	chon=random.randint(1,2)
	if chon==1:
		kq=random.choice([f'${vec(f"{A}{B}")}$ và ${vec(f"{A}{I}")}$',
					f'${vec(f"{B}{A}")}$ và ${vec(f"{B}{I}")}$',
					f'${vec(f"{I}{A}")}$ và ${vec(f"{B}{A}")}$',
					f'${vec(f"{I}{B}")}$ và ${vec(f"{A}{B}")}$'
					])
		pa_A= f"*{kq} là {random.choice(['cùng hướng', 'cùng phương'])}"
	
	if chon==2:
		kq=random.choice([f'${vec(f"{A}{B}")}$ và ${vec(f"{I}{A}")}$',
					f'${vec(f"{B}{A}")}$ và ${vec(f"{I}{B}")}$',
					f'${vec(f"{A}{I}")}$ và ${vec(f"{B}{A}")}$',
					f'${vec(f"{B}{I}")}$ và ${vec(f"{A}{B}")}$'
					])
		pa_A= f"*{kq} là {random.choice(['ngược hướng', 'cùng phương'])}"
	

	kq2=random.choice([f'{vec(f"{I}{A}")}={vec(f"{I}{B}")}',
					f'{vec(f"{A}{I}")}={vec(f"{B}{I}")}',
					f'{vec(f"{A}{B}")}={vec(f"{B}{A}")}',
					f'{vec(f"{A}{I}")}={vec(f"{A}{B}")}',
					f'{vec(f"{B}{I}")}={vec(f"{B}{A}")}'
					])
	pa_B= f"${kq2}$"

	kq3=random.choice([f'|{vec(f"{A}{B}")}|=|{vec(f"{I}{A}")}|',
					f'|{vec(f"{A}{B}")}|=|{vec(f"{A}{I}")}|',
					f'|{vec(f"{A}{B}")}|=|{vec(f"{B}{I}")}|',
					f'|{vec(f"{A}{B}")}|=|{vec(f"{I}{B}")}|',
					f'|{vec(f"{B}{A}")}|=|{vec(f"{B}{I}")}|',
					f'|{vec(f"{B}{A}")}|=|{vec(f"{A}{I}")}|',
		])
	pa_C= f"${kq3}$"

	chon=random.randint(1,2)
	if chon==1:
		kq4=random.choice([f'${vec(f"{A}{B}")}$ và ${vec(f"{A}{I}")}$',
					f'${vec(f"{B}{A}")}$ và ${vec(f"{B}{I}")}$',
					f'${vec(f"{I}{A}")}$ và ${vec(f"{B}{A}")}$',
					f'${vec(f"{I}{B}")}$ và ${vec(f"{A}{B}")}$'
					])
		pa_D= f"{kq4} là ngược hướng"
	
	if chon==2:
		kq4=random.choice([f'${vec(f"{A}{B}")}$ và ${vec(f"{I}{A}")}$',
					f'${vec(f"{B}{A}")}$ và ${vec(f"{I}{B}")}$',
					f'${vec(f"{A}{I}")}$ và ${vec(f"{B}{A}")}$',
					f'${vec(f"{B}{I}")}$ và ${vec(f"{A}{B}")}$'
					])
		pa_D= f"{kq4} là cùng hướng"

	noi_dung_loigiai=f"{kq} là khẳng định đúng."	
	
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B1_05]-M2. Cho 3 điểm. Tìm khẳng định về hướng và phương.
def y7y7u_L10_C5_B1_05():
	letters = [chr(i) for i in range(ord('A'), ord('N') + 1)]
	random.shuffle(letters)
	A,B,C=letters[0:3]

	chon=random.randint(1,2)
	if chon==1:
		noi_dung=f"Cho ba điểm ${{{A},{B},{C}}}$ thẳng hàng theo thứ tự đó. Khẳng định nào sau đây là sai?"
	
		kq=f"${vec(f"{C}{B}")}$ ngược hướng với ${vec(f"{B}{A}")}$"
		kq2=f"${vec(f"{A}{B}")}$ cùng hướng với ${vec(f"{B}{C}")}$"
		kq3=f"${vec(f"{A}{C}")}$ cùng hướng với ${vec(f"{B}{C}")}$"
		kq4=f"${vec(f"{B}{C}")}$ ngược hướng với ${vec(f"{B}{A}")}$"

		noi_dung_loigiai=f"{kq} là khẳng định sai."
	
	if chon==2:
		noi_dung=f"Cho ba điểm ${{{A},{B},{C}}}$ thẳng hàng theo thứ tự đó. Khẳng định nào sau đây là đúng?"
	
		kq=random.choice([f"${vec(f"{A}{B}")}$ cùng hướng với ${vec(f"{B}{C}")}$",
			f"${vec(f"{A}{C}")}$ cùng hướng với ${vec(f"{B}{C}")}$",
			f"${vec(f"{B}{C}")}$ ngược hướng với ${vec(f"{B}{A}")}$",
			f"${vec(f"{B}{A}")}$ ngược hướng với ${vec(f"{A}{C}")}$"])

		kq2=f"${vec(f"{A}{B}")}$ cùng hướng với ${vec(f"{C}{A}")}$"
		kq3=f"${vec(f"{B}{A}")}$ ngược hướng với ${vec(f"{C}{B}")}$"
		kq4=f"${vec(f"{C}{B}")}$ cùng hướng với ${vec(f"{A}{C}")}$"

		noi_dung_loigiai=f"{kq} là khẳng định đúng."	
	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B1_06]-M1. Cho hình vuông (chữ nhật). Tính độ dài vectơ cạnh.
def y7y7u_L10_C5_B1_06():
	A=["A","A","M","O", "A"]
	B=["B","B","N","A", "B"]
	C=["C","E","P","B", "M"]
	D=["D","F","Q","C", "N"]

	i=random.randint(0,4)
	A, B, C, D = A[i], B[i], C[i], D[i]
	chon=random.randint(1,2)
	if chon==1:
		ten=f"{{{A}{B}{C}{D}}}"
		m=random.randint(1,10)
		a=sp.symbols("a")
		vecto=random.choice([vec(f"{A}{B}"),vec(f"{B}{C}"), vec(f"{C}{D}"), vec(f"{D}{A}")])

		noi_dung=f"Cho hình vuông ${ten}$ có độ dài cạnh bằng ${latex(m*a)}$. Độ dài của vectơ ${vecto}$ bằng"
		kq=f"${{{latex(m*a)}}}$"
		kq2=f"${{{latex(m*a*sqrt(2))}}}$"
		kq3=f"${{{latex(m*a*sqrt(random.randint(3,6)))}}}$"
		kq4=f"${{{latex(random.randint(2,3)*m*a)}}}$"

		noi_dung_loigiai=f"$|{vecto}|={latex(m*a)}$."
	
	if chon==2:
		ten=f"{{{A}{B}{C}{D}}}"
		m=random.randint(1,8)
		n=m+random.randint(1,4)
		a=sp.symbols("a")
		vecto=random.choice([vec(f"{A}{B}"), vec(f"{C}{D}"), vec(f"{D}{C}"), vec(f"{B}{A}")])

		noi_dung=(f"Cho hình chữ nhật ${ten}$ có ${A}{B}={latex(m*a)}, {A}{D}={latex(n*a)}$."
			f" Độ dài của vectơ ${vecto}$ bằng")
		kq=f"${{{latex(m*a)}}}$"
		kq2=f"${{{latex(m*a*sqrt(2))}}}$"
		kq3=f"${{{latex(n*a*sqrt(2))}}}$"
		kq4=f"${{{latex(n*a)}}}$"

		noi_dung_loigiai=f"$|{vecto}|={latex(m*a)}$."

	if chon==3:
		ten=f"{{{A}{B}{C}{D}}}"
		m=random.randint(1,8)
		n=m+random.randint(1,4)
		a=sp.symbols("a")
		vecto=random.choice([vec(f"{A}{D}"), vec(f"{D}{A}"), vec(f"{B}{C}"), vec(f"{C}{B}")])

		noi_dung=(f"Cho hình chữ nhật ${ten}$ có ${A}{B}={latex(m*a)}, {A}{D}={latex(n*a)}$."
			f" Độ dài của vectơ ${vecto}$ bằng")
		kq=f"${{{latex(n*a)}}}$"
		kq2=f"${{{latex(m*a*sqrt(2))}}}$"
		kq3=f"${{{latex(n*a*sqrt(2))}}}$"
		kq4=f"${{{latex(m*a)}}}$"

		noi_dung_loigiai=f"$|{vecto}|={latex(n*a)}$."
	

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B1_07]-M2. Cho hình vuông (chữ nhật). Tính độ dài vectơ đường chéo.
def y7y7u_L10_C5_B1_07():
	A=["A","A","M","O", "A"]
	B=["B","B","N","A", "B"]
	C=["C","E","P","B", "M"]
	D=["D","F","Q","C", "N"]

	i=random.randint(0,4)
	A, B, C, D = A[i], B[i], C[i], D[i]
	chon=random.randint(1,2)
	
	if chon==1:
		ten=f"{{{A}{B}{C}{D}}}"
		m=random.randint(1,10)
		a=sp.symbols("a")
		vecto=random.choice([vec(f"{A}{C}"),vec(f"{C}{A}"), vec(f"{B}{D}"), vec(f"{D}{B}")])

		noi_dung=f"Cho hình vuông ${ten}$ có độ dài cạnh bằng ${latex(m*a)}$. Độ dài của vectơ ${vecto}$ bằng"
		kq=f"${{{latex(m*a*sqrt(2))}}}$"
		kq2=f"${{{latex(m*a)}}}$"
		kq3=f"${{{latex(m*a*sqrt(random.randint(4,7)))}}}$"
		kq4=f"${{{latex(m*a*sqrt(3))}}}$"

		noi_dung_loigiai=f"$|{vecto}|={latex(m*a)}.\\sqrt 2={latex(m*a*sqrt(2))}$."
	

	if chon==2:
		ten=f"{{{A}{B}{C}{D}}}"
		m=random.randint(1,8)
		n=m+random.randint(1,4)
		a=sp.symbols("a")
		vecto=random.choice([vec(f"{A}{C}"), vec(f"{C}{A}"), vec(f"{B}{D}"), vec(f"{D}{B}")])

		noi_dung=(f"Cho hình chữ nhật ${ten}$ có ${A}{B}={latex(m*a)}, {A}{D}={latex(n*a)}$."
			f" Độ dài của vectơ ${vecto}$ bằng")
		kq=f"${{{latex(sqrt(m**2+n**2)*a)}}}$"
		kq2=f"${{{latex(sqrt(m+n)*a)}}}$"
		kq3=f"${{{latex(m*a*sqrt(2))}}}$"
		kq4=f"${{{latex(n*a*sqrt(2))}}}$"

		noi_dung_loigiai=f"$|{vecto}|=\\sqrt{{({latex(m*a)})^2 + ({latex(n*a)})^2}}={latex(sqrt(m**2+n**2)*a)}$."
	

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#Bài 2 - Tổng hiệu các vectơ
#[D10_C5_B2_01]-M2. Cho trung điểm của đoạn. Tìm khẳng định tổng hiệu các vectơ.
def y7y7u_L10_C5_B2_01():
	A=["A","C","E","P", "M"]
	B=["B","D","F","Q", "N"]
	I=random.choice(["I","K","O","H"])
	i=random.randint(0,4)
	A, B= A[i], B[i]

	noi_dung=f"Gọi ${{{I}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$. Khẳng định nào sau đây là khẳng định đúng?"

	kq=random.choice([f"{vec(f"{I}{A}")}+{vec(f"{I}{B}")}={vec(f"0")}",
		f"{vec(f"{I}{B}")}+{vec(f"{I}{A}")}={vec(f"0")}",
		f"{vec(f"{B}{I}")}+{vec(f"{A}{I}")}={vec(f"0")}",
		f"{vec(f"{A}{I}")}+{vec(f"{B}{I}")}={vec(f"0")}"
		])
	kq2=random.choice([f"{vec(f"{I}{A}")}-{vec(f"{I}{B}")}={vec(f"0")}",
		f"{vec(f"{I}{B}")}-{vec(f"{I}{A}")}={vec(f"0")}",
		f"{vec(f"{B}{I}")}-{vec(f"{A}{I}")}={vec(f"0")}",
		f"{vec(f"{A}{I}")}-{vec(f"{B}{I}")}={vec(f"0")}"
		])
	kq3=random.choice([f"{I}{A}+{I}{B}=0",
		f"{I}{B}+{I}{A}=0",
		f"{B}{I}+{A}{I}=0"
	 ])
	kq4=random.choice([f"{vec(f"{I}{A}")}={vec(f"{I}{B}")}",
		f"{vec(f"{A}{I}")}={vec(f"{B}{I}")}",
		f"{vec(f"{A}{B}")}={vec(f"{B}{A}")}"
		 ])

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	
	noi_dung_loigiai=f"${kq}$ là khẳng định đúng."	
	
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B2_02]-M2. Cho các điểm. Tính tổng hiệu các vectơ
def y7y7u_L10_C5_B2_02():
	points=["A","B","C","D","E"]
	random.shuffle(points)
	A,B,C,D,E=points
	chon=random.randint(1,7)	

	if chon==1:
		noi_dung= (f"Cho các điểm ${{{A},{B},{C},{D},{E}}}$."
	f" Tính tổng ${vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{E}")}$.")	

		kq=f"${vec(f"{A}{E}")}$"
		kq2=random.choice([f"${vec(f"{A}{D}")}$", f"${vec(f"{A}{C}")}$", f"${vec(f"{B}{D}")}$", f"${vec(f"{B}{E}")}$"])
		kq3=f"${vec(f"0")}$"
		kq4=random.choice([f"${vec(f"{D}{A}")}$",f"${vec(f"{E}{A}")}$", f"${vec(f"{E}{D}")}$"])
		noi_dung_loigiai=f"${vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{E}")}={vec(f"{A}{E}")}$."
	
	if chon==2:
		noi_dung=(f"Cho các điểm ${{{A},{B},{C},{D},{E}}}$."
	f" Tính tổng ${vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{A}")}$.")	

		kq=f"${vec(f"0")}$"
		kq2=random.choice([f"${vec(f"{A}{D}")}$", f"${vec(f"{A}{C}")}$", f"${vec(f"{B}{D}")}$", f"${vec(f"{B}{E}")}$"])
		kq3=f"${vec(f"{A}{E}")}$"
		kq4=random.choice([f"${vec(f"{E}{A}")}$", f"${vec(f"{E}{D}")}$"])
		noi_dung_loigiai=f"${vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{A}")}={vec(f"{A}{A}")}={vec(f"0")}$."

	if chon==3:
		noi_dung=(f"Cho các điểm ${{{A},{B},{C},{D},{E}}}$."
	f" Tính ${vec(f"{A}{B}")}-{vec(f"{C}{B}")}+{vec(f"{C}{D}")}-{vec(f"{E}{D}")}$.")

		kq=f"${vec(f"{A}{E}")}$"
		kq2=random.choice([f"${vec(f"{A}{D}")}$", f"${vec(f"{A}{C}")}$", f"${vec(f"{B}{D}")}$", f"${vec(f"{B}{E}")}$"])
		kq3=f"${vec(f"0")}$"
		kq4=random.choice([f"${vec(f"{D}{A}")}$",f"${vec(f"{E}{A}")}$", f"${vec(f"{E}{D}")}$"])

		noi_dung_loigiai=(f"${vec(f"{A}{B}")}-{vec(f"{C}{B}")}+{vec(f"{C}{D}")}-{vec(f"{E}{D}")}="
		f"{vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{E}")}={vec(f"{A}{E}")}$.")

	if chon==4:
		noi_dung=(f"Cho các điểm ${{{A},{B},{C},{D},{E}}}$."
	f" Tính ${vec(f"{A}{B}")}-{vec(f"{C}{B}")}-{vec(f"{D}{C}")}-{vec(f"{E}{D}")}$.")

		kq=f"${vec(f"{A}{E}")}$"
		kq2=random.choice([f"${vec(f"{A}{D}")}$", f"${vec(f"{A}{C}")}$", f"${vec(f"{B}{D}")}$", f"${vec(f"{B}{E}")}$"])
		kq3=f"${vec(f"0")}$"
		kq4=random.choice([f"${vec(f"{D}{A}")}$",f"${vec(f"{E}{A}")}$", f"${vec(f"{E}{D}")}$"])
		noi_dung_loigiai=f"${vec(f"{A}{B}")}-{vec(f"{C}{B}")}-{vec(f"{D}{C}")}-{vec(f"{E}{D}")}="\
		f"{vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{E}")}={vec(f"{A}{E}")}$."
	
	if chon==5:
		noi_dung=(f"Cho các điểm ${{{A},{B},{C},{D},{E}}}$."
	f" Tính ${vec(f"{A}{C}")}-{vec(f"{A}{B}")}+{vec(f"{E}{A}")}-{vec(f"{E}{C}")}$.")

		kq=f"${vec(f"{B}{A}")}$"
		kq2=random.choice([f"${vec(f"{A}{D}")}$", f"${vec(f"{A}{C}")}$", f"${vec(f"{B}{D}")}$", f"${vec(f"{B}{E}")}$"])
		kq3=random.choice([f"${vec(f"0")}$", f"${vec(f"{A}{B}")}$"])
		kq4=random.choice([f"${vec(f"{D}{A}")}$",f"${vec(f"{E}{A}")}$", f"${vec(f"{E}{D}")}$"])

		noi_dung_loigiai=f"${vec(f"{A}{C}")}-{vec(f"{A}{B}")}+{vec(f"{E}{A}")}-{vec(f"{E}{C}")}="\
		f"{vec(f"{B}{C}")}+{vec(f"{C}{A}")}={vec(f"{B}{A}")}$."
	
	if chon==6:
		noi_dung=(f"Cho các điểm ${{{A},{B},{C},{D},{E}}}$."
	f" Tính ${vec(f"{A}{C}")}-{vec(f"{A}{B}")}-{vec(f"{E}{C}")}+{vec(f"{E}{A}")}$.")

		kq=f"${vec(f"{B}{A}")}$"
		kq2=random.choice([f"${vec(f"{A}{D}")}$", f"${vec(f"{A}{C}")}$", f"${vec(f"{B}{D}")}$", f"${vec(f"{B}{E}")}$"])
		kq3=random.choice([f"${vec(f"0")}$", f"${vec(f"{A}{B}")}$"])
		kq4=random.choice([f"${vec(f"{D}{A}")}$",f"${vec(f"{E}{A}")}$", f"${vec(f"{E}{D}")}$"])

		noi_dung_loigiai=(f"${vec(f"{A}{C}")}-{vec(f"{A}{B}")}-{vec(f"{E}{C}")}+{vec(f"{E}{A}")}="
		f"{vec(f"{B}{C}")}+{vec(f"{C}{A}")}={vec(f"{B}{A}")}$.")

	if chon==7:
		noi_dung=(f"Cho các điểm ${{{A},{B},{C},{D},{E}}}$."
	f" Tính tổng ${vec(f"{E}{A}")}+{vec(f"{A}{C}")}-{vec(f"{A}{B}")}-{vec(f"{E}{C}")}$.")

		kq=f"${vec(f"{B}{A}")}$"
		kq2=random.choice([f"${vec(f"{A}{D}")}$", f"${vec(f"{A}{C}")}$", f"${vec(f"{B}{D}")}$", f"${vec(f"{B}{E}")}$"])
		kq3=random.choice([f"${vec(f"0")}$", f"${vec(f"{A}{B}")}$"])
		kq4=random.choice([f"${vec(f"{D}{A}")}$",f"${vec(f"{E}{A}")}$", f"${vec(f"{E}{D}")}$"])

		noi_dung_loigiai=f"${vec(f"{E}{A}")}+{vec(f"{A}{C}")}-{vec(f"{A}{B}")}-{vec(f"{E}{C}")}="\
		f"{vec(f"{A}{C}")}-{vec(f"{A}{B}")}+{vec(f"{E}{A}")}-{vec(f"{E}{C}")}="\
		f"{vec(f"{B}{C}")}+{vec(f"{C}{A}")}={vec(f"{B}{A}")}$."

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

#[D10_C5_B2_03]-M2. Tìm đẳng thức đúng liên quan đến 3 điểm (phép cộng trừ)
def y7y7u_L10_C5_B2_03():
	A1=random.choice(["A", "M", "P", "F", "I"])
	B1=random.choice(["B", "N", "Q", "G", "K"])
	C1=random.choice(["C", "E", "D", "H ", "L"])	
	
	noi_dung=f"Cho các điểm ${A1}, {B1},{C1}$. Tìm khẳng định đúng."

	chon=random.randint(1,3)
	if chon==1:
		kq=f"$\\overrightarrow{{{A1}{B1}}} + \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{A1}{C1}}}$"
		kq2=f"$\\overrightarrow{{{A1}{B1}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{B1}{C1}}}$"
		kq3=f"$\\overrightarrow{{{A1}{B1}}} - \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{B1}{C1}}}$"
		kq4=f"$\\overrightarrow{{{A1}{C1}}} - \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{B1}{A1}}}$"
	
	if chon==2:
		kq=f"$\\overrightarrow{{{A1}{B1}}} - \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{C1}{B1}}}$"
		kq2=f"$\\overrightarrow{{{A1}{B1}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{B1}{C1}}}$"
		kq3=f"$\\overrightarrow{{{A1}{C1}}} + \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{A1}{B1}}}$"
		kq4=f"$\\overrightarrow{{{A1}{C1}}} - \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{B1}{A1}}}$"

	if chon==3:
		kq=f"$\\overrightarrow{{{A1}{B1}}} - \\overrightarrow{{{C1}{B1}}} = \\overrightarrow{{{A1}{C1}}}$"
		kq2=f"$\\overrightarrow{{{A1}{B1}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{B1}{C1}}}$"
		kq3=f"$\\overrightarrow{{{A1}{C1}}} + \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{A1}{B1}}}$"
		kq4=f"$\\overrightarrow{{{C1}{A1}}} - \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{A1}{B1}}}$"

	noi_dung_loigiai=f"{kq} là khẳng định đúng."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"


	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\t   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B2_04]-M2. Cho tứ giác. Tìm khẳng định đúng về quy tắc cộng trừ.
def y7y7u_L10_C5_B2_04():
	A=["A","A","E","M"]
	B=["B","B","F","N"]
	C=["C","E","G", "P"]
	D=["D","F","H","Q"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	ten_tudien=f"{{{A}{B}{C}{D}}}"
	noi_dung=f"Cho tứ giác ${ten_tudien}$. Tìm khẳng định đúng"
	chon=random.randint(1,6)
	
	if chon==1:
		kq=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{D}{B}}}-\\overrightarrow{{{D}{C}}}$"
		noi_dung_loigiai=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{D}{B}}}-\\overrightarrow{{{D}{C}}}=\\overrightarrow{{{C}{B}}}$."
	if chon==2:
		kq=f"$\\overrightarrow{{{A}{D}}}-\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{B}{D}}}-\\overrightarrow{{{B}{C}}}$"
		noi_dung_loigiai=f"$\\overrightarrow{{{A}{D}}}-\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{B}{D}}}-\\overrightarrow{{{B}{C}}}=\\overrightarrow{{{C}{D}}}$."

	if chon==3:
		kq=f"$\\overrightarrow{{{C}{D}}}-\\overrightarrow{{{C}{B}}}=\\overrightarrow{{{B}{A}}}+\\overrightarrow{{{A}{D}}}$"
		noi_dung_loigiai=f"$\\overrightarrow{{{C}{D}}}-\\overrightarrow{{{C}{B}}}=\\overrightarrow{{{B}{A}}}+\\overrightarrow{{{A}{D}}}=\\overrightarrow{{{B}{D}}}$."

	if chon==4:
		kq=f"$\\overrightarrow{{{A}{B}}}+\\overrightarrow{{{C}{A}}}=\\overrightarrow{{{D}{B}}}-\\overrightarrow{{{D}{C}}}$"
		noi_dung_loigiai=f"$\\overrightarrow{{{A}{B}}}+\\overrightarrow{{{C}{A}}}=\\overrightarrow{{{D}{B}}}-\\overrightarrow{{{D}{C}}}=\\overrightarrow{{{C}{D}}}$"

	if chon==5:
		kq=f"$\\overrightarrow{{{A}{C}}}+\\overrightarrow{{{D}{A}}}=\\overrightarrow{{{B}{C}}}-\\overrightarrow{{{B}{D}}}$"
		noi_dung_loigiai=f"$\\overrightarrow{{{A}{C}}}+\\overrightarrow{{{D}{A}}}=\\overrightarrow{{{B}{C}}}-\\overrightarrow{{{B}{D}}}=\\overrightarrow{{{D}{B}}}$"

	if chon==6:
		kq=f"$\\overrightarrow{{{C}{B}}}+\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{C}{B}}}-\\overrightarrow{{{C}{A}}}$"
		noi_dung_loigiai=f"$\\overrightarrow{{{C}{B}}}+\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{C}{B}}}-\\overrightarrow{{{C}{A}}}=\\overrightarrow{{{A}{B}}}$"
	
	
	kq2=f"$\\overrightarrow{{{A}{C}}}-\\overrightarrow{{{A}{D}}}=\\overrightarrow{{{B}{D}}}-\\overrightarrow{{{B}{C}}}$"
	kq3=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{D}}}=\\overrightarrow{{{C}{D}}}+\\overrightarrow{{{B}{C}}}$"
	kq4=f"$\\overrightarrow{{{B}{C}}}+\\overrightarrow{{{A}{B}}}=\\overrightarrow{{{D}{A}}}-\\overrightarrow{{{D}{C}}}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B2_05]-M2. Cho hình bình hành. Tìm khẳng định sai về phép toán vectơ 
def y7y7u_L10_C5_B2_05():
	S=["H","P","G","I"]
	A=["M","A","B","A"]
	B=["N","B","C","B"]
	C=["P","C","D","E"]
	D=["Q","D","E","F"]
	i=random.randint(0,3)
	S,A, B, C, D =S[i], A[i], B[i], C[i], D[i]
	tam=random.choice(["O", "I"])
	chon=random.randint(1,2)
	if chon==1:
		noi_dung=f"Cho hình bình hành ${{{A}{B}{C}{D}}}$ và điểm ${{{S}}}$ tùy ý. Tìm mệnh đề sai trong các mệnh đề sau."
		
		kq=random.choice([
			f"${vec(f"{A}{B}")}+{vec(f"{C}{B}")}={vec(f"{A}{C}")}$",
			f"${vec(f"{A}{C}")}+{vec(f"{B}{C}")}={vec(f"{A}{B}")}$",

			f"${vec(f"{C}{A}")}+{vec(f"{B}{A}")}={vec(f"{C}{B}")}$",
			f"${vec(f"{S}{D}")}+{vec(f"{B}{D}")}={vec(f"{S}{B}")}$",
			f"${vec(f"{S}{D}")}-{vec(f"{D}{B}")}={vec(f"{S}{B}")}$",
			f"${vec(f"{S}{A}")}-{vec(f"{A}{B}")}={vec(f"{S}{B}")}$",
			f"${vec(f"{S}{C}")}-{vec(f"{B}{C}")}={vec(f"{B}{S}")}$"
			])
		kq_false=[
			f"${vec(f"{S}{A}")}-{vec(f"{S}{B}")}={vec(f"{S}{D}")}-{vec(f"{S}{C}")}$",
			f"${vec(f"{S}{B}")}-{vec(f"{S}{C}")}={vec(f"{S}{A}")}-{vec(f"{S}{D}")}$",

			f"${vec(f"{A}{B}")}+{vec(f"{A}{D}")}={vec(f"{A}{C}")}$",
			f"${vec(f"{A}{B}")}-{vec(f"{D}{A}")}={vec(f"{A}{C}")}$",

			f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={vec(f"{B}{D}")}$",
			f"${vec(f"{B}{A}")}-{vec(f"{C}{B}")}={vec(f"{B}{D}")}$",

			f"${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={vec(f"{D}{B}")}$",
			f"${vec(f"{D}{A}")}-{vec(f"{C}{D}")}={vec(f"{D}{B}")}$",

			f"${vec(f"{C}{D}")}+{vec(f"{C}{B}")}={vec(f"{C}{A}")}$",
			f"${vec(f"{C}{D}")}-{vec(f"{B}{C}")}={vec(f"{C}{A}")}$"]
		noi_dung_loigiai=f"{kq} là mệnh đề sai."
	
	if chon==2:
		noi_dung=f"Cho hình bình hành ${{{A}{B}{C}{D}}}$ và điểm ${{{S}}}$ tùy ý. Tìm mệnh đề đúng trong các mệnh đề sau."
		
		kq=random.choice([
			f"${vec(f"{S}{A}")}-{vec(f"{S}{B}")}={vec(f"{S}{D}")}-{vec(f"{S}{C}")}$",
			f"${vec(f"{S}{B}")}-{vec(f"{S}{C}")}={vec(f"{S}{A}")}-{vec(f"{S}{D}")}$",

			f"${vec(f"{A}{B}")}+{vec(f"{A}{D}")}={vec(f"{A}{C}")}$",
			f"${vec(f"{A}{B}")}-{vec(f"{D}{A}")}={vec(f"{A}{C}")}$",

			f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={vec(f"{B}{D}")}$",
			f"${vec(f"{B}{A}")}-{vec(f"{C}{B}")}={vec(f"{B}{D}")}$",

			f"${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={vec(f"{D}{B}")}$",
			f"${vec(f"{D}{A}")}-{vec(f"{C}{D}")}={vec(f"{D}{B}")}$",

			f"${vec(f"{C}{D}")}+{vec(f"{C}{B}")}={vec(f"{C}{A}")}$",
			f"${vec(f"{C}{D}")}-{vec(f"{B}{C}")}={vec(f"{C}{A}")}$"	
			
			])
		kq_false=[
			f"${vec(f"{A}{B}")}+{vec(f"{C}{B}")}={vec(f"{A}{C}")}$",
			f"${vec(f"{A}{C}")}+{vec(f"{B}{C}")}={vec(f"{A}{B}")}$",

			f"${vec(f"{C}{A}")}+{vec(f"{B}{A}")}={vec(f"{C}{B}")}$",
			f"${vec(f"{S}{D}")}+{vec(f"{B}{D}")}={vec(f"{S}{B}")}$",
			f"${vec(f"{S}{D}")}-{vec(f"{D}{B}")}={vec(f"{S}{B}")}$",
			f"${vec(f"{S}{A}")}-{vec(f"{A}{B}")}={vec(f"{S}{B}")}$",
			f"${vec(f"{S}{C}")}-{vec(f"{B}{C}")}={vec(f"{B}{S}")}$"
			]
		noi_dung_loigiai=f"{kq} là mệnh đề đúng."	

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

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
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

#[D10_C5_B2_06]-M2. Cho hình bình hành. Tính tổng hiệu các vectơ 
def y7y7u_L10_C5_B2_06():
	S=["H","P","G","I"]
	A=["M","A","B","A"]
	B=["N","B","C","B"]
	C=["P","C","D","E"]
	D=["Q","D","E","F"]
	i=random.randint(0,3)
	S,A, B, C, D =S[i], A[i], B[i], C[i], D[i]
	O=random.choice(["O", "I"])
	code_hinh=my_module.code_latex_hinhbinhhanh(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	chon=random.randint(1,3)
	if chon==1:
		phep_toan=random.choice([
			f"{vec(f"{A}{B}")}-{vec(f"{A}{C}")}+{vec(f"{B}{D}")}",
			f"{vec(f"{B}{D}")} + {vec(f"{A}{B}")} - {vec(f"{A}{C}")}",
			f"{vec(f"{B}{D}")} - {vec(f"{A}{C}")} + {vec(f"{A}{B}")}",
			f"{vec(f"{B}{D}")} - {vec(f"{A}{C}")} - {vec(f"{B}{A}")}",
			f"{vec(f"{A}{B}")} - {vec(f"{D}{B}")} - {vec(f"{A}{C}")}",
			f"{vec(f"{A}{B}")} - {vec(f"{A}{C}")} - {vec(f"{D}{B}")}",
			])
		noi_dung=f"Cho hình bình hành ${{{A}{B}{C}{D}}}$. Tính ${phep_toan}$."
		
		kq=f"{vec(f"{C}{D}")}"		
		kq2=random.choice([
			f"{vec(f"{B}{C}")}",
			f"{vec(f"{C}{B}")}"
			])
		kq3=random.choice([
			f"{vec(f"{A}{D}")}",
			f"{vec(f"{D}{A}")}"
			])
		kq4=random.choice([
			f"{vec(f"{D}{C}")}",
			f"{vec(f"{B}{D}")}",
			])
		if phep_toan==f"{vec(f"{A}{B}")}-{vec(f"{A}{C}")}+{vec(f"{B}{D}")}":
			noi_dung_loigiai=f"${phep_toan}={vec(f"{C}{B}")}+{vec(f"{B}{D}")}={{{vec(f"{C}{D}")}}}$."
		else:
			noi_dung_loigiai=f"${phep_toan}={vec(f"{A}{B}")}-{vec(f"{A}{C}")}+{vec(f"{B}{D}")}={vec(f"{C}{B}")}+{vec(f"{B}{D}")}={{{vec(f"{C}{D}")}}}$."

	
	if chon==2:
		phep_toan=random.choice([
			f"{vec(f"{O}{A}")}+{vec(f"{D}{C}")}+{vec(f"{O}{B}")}",
			f"{vec(f"{O}{A}")}-{vec(f"{C}{D}")}+{vec(f"{O}{B}")}",
			f"{vec(f"{O}{A}")}-{vec(f"{C}{D}")}-{vec(f"{B}{O}")}",
			f"{vec(f"{O}{B}")}+{vec(f"{O}{A}")}+{vec(f"{D}{C}")}",
			f"{vec(f"{O}{B}")}-{vec(f"{A}{O}")}+{vec(f"{D}{C}")}",
			f"{vec(f"{O}{B}")}-{vec(f"{A}{O}")}-{vec(f"{C}{D}")}",

			])
		noi_dung=f"Cho hình bình hành ${{{A}{B}{C}{D}}}$ có tâm ${{{O}}}$. Tính ${phep_toan}$."

		if phep_toan==f"{vec(f"{O}{A}")}+{vec(f"{D}{C}")}+{vec(f"{O}{B}")}":
			noi_dung_loigiai=f"${phep_toan} = {vec(f"{D}{C}")} + {vec(f"{C}{O}")} + {vec(f"{O}{B}")} = {vec(f"{D}{B}")}$."
		else:
			noi_dung_loigiai=(f"${phep_toan} = {vec(f"{O}{A}")}+{vec(f"{D}{C}")}+{vec(f"{O}{B}")}"
				f"={vec(f"{D}{C}")} + {vec(f"{C}{O}")} + {vec(f"{O}{B}")} = {vec(f"{D}{B}")}$.")

		kq=f"{vec(f"{D}{B}")}"
		kq2=random.choice([
			f"{vec(f"{B}{C}")}",
			f"{vec(f"{C}{B}")}",
			f"{vec(f"{O}{D}")}",
			f"{vec(f"0")}"
			])
		kq3=random.choice([
			f"{vec(f"{A}{D}")}",
			f"{vec(f"{D}{A}")}",
			f"{vec(f"{C}{O}")}"
			])
		kq4=random.choice([
			f"{vec(f"{D}{C}")}",
			f"{vec(f"{C}{D}")}",
			f"{vec(f"{B}{D}")}"
			])
	
	if chon==3:
		phep_toan=random.choice([
			f"{vec(f"{C}{D}")}+{vec(f"{C}{B}")}+{vec(f"{A}{O}")}",
			f"{vec(f"{C}{D}")}-{vec(f"{B}{C}")}+{vec(f"{A}{O}")}",
			f"{vec(f"{C}{D}")}-{vec(f"{B}{C}")}-{vec(f"{O}{A}")}",
			f"{vec(f"{A}{O}")}+{vec(f"{C}{D}")}+{vec(f"{C}{B}")}",
			f"{vec(f"{A}{O}")}+{vec(f"{C}{D}")}-{vec(f"{B}{C}")}",
			f"{vec(f"{A}{O}")}-{vec(f"{D}{C}")}-{vec(f"{B}{C}")}",
			])
		noi_dung=f"Cho hình bình hành ${{{A}{B}{C}{D}}}$ có tâm ${{{O}}}$. Tính ${phep_toan}$."

		kq=f"{vec(f"{C}{O}")}"
		kq2=random.choice([
			f"{vec(f"{B}{C}")}",
			f"{vec(f"{C}{B}")}",
			f"{vec(f"{O}{D}")}",
			f"{vec(f"0")}"
			])
		kq3=random.choice([
			f"{vec(f"{A}{D}")}",
			f"{vec(f"{D}{A}")}",
			f"{vec(f"{D}{O}")}"
			])
		kq4=random.choice([
			f"{vec(f"{D}{C}")}",
			f"{vec(f"{C}{D}")}",
			f"{vec(f"{B}{O}")}"
			])
		if phep_toan==f"{vec(f"{C}{D}")}+{vec(f"{C}{B}")}+{vec(f"{A}{O}")}":
			noi_dung_loigiai=f"${phep_toan} = {vec(f"{C}{A}")}  + {vec(f"{A}{O}")} = {vec(f"{C}{O}")}$."
		else:
			noi_dung_loigiai=(f"${phep_toan} = {vec(f"{C}{D}")}+{vec(f"{C}{B}")}+{vec(f"{A}{O}")}"
				f"={vec(f"{C}{A}")}  + {vec(f"{A}{O}")} = {vec(f"{C}{O}")}$.")

	
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
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B2_07]-M2. Cho các điểm. Tính tổng các vectơ
def y7y7u_L10_C5_B2_07():
	chon=random.randint(1,5)
	if chon==1:
		danh_sach=f"A,B,C,D,E"	
	if chon==2:
		danh_sach=f"M,N,P,Q,R"
	if chon==3:
		danh_sach=f"A,B,M,N,P"
	if chon==4:
		danh_sach=f"A,B,E,F,G"
	if chon==5:
		danh_sach=f"E,F,G,H,I"
	
	points=danh_sach.split(",")
	random.shuffle(points)
	A,B,C,D,E=points
	chon=random.randint(1,4)	

	if chon==1:
		phep_toan=f"{vec(f"{A}{B}")}+{vec(f"{C}{D}")}+{vec(f"{D}{A}")}+{vec(f"{B}{C}")}"
		noi_dung=(f"Cho các điểm ${{{danh_sach}}}$."
				f" Tính tổng ${phep_toan}$.")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{A}{B}")} + {vec(f"{B}{C}")} + {vec(f"{C}{D}")} + {vec(f"{D}{A}")}$\n\n"
		f"$={vec(f"{A}{C}")}+{vec(f"{C}{A}")}={vec(f"0")}$.")	

		kq=f"{vec(f"0")}"
		kq2=f"{vec(f"{A}{C}")}"
		kq3=random.choice([
			f"{vec(f"{C}{A}")}",
			f"{vec(f"{C}{B}")}"
			])
		kq4=random.choice([
			f"{vec(f"{B}{D}")}",
			f"{vec(f"{D}{B}")}",
			])
	
	if chon==2:
		phep_toan=f"{vec(f"{A}{B}")} + {vec(f"{D}{A}")} + {vec(f"{C}{D}")}"
		noi_dung=(f"Cho các điểm ${{{danh_sach}}}$."
				f" Tính tổng ${phep_toan}$.")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{C}{D}")}+{vec(f"{D}{A}")}+{vec(f"{A}{B}")}={vec(f"{C}{B}")}$.\n"
		)	

		kq=f"{vec(f"{C}{B}")}"
		kq2=f"{vec(f"{A}{C}")}"
		kq3=random.choice([
			f"{vec(f"{C}{A}")}",
			f"{vec(f"0")}",
			f"{vec(f"{B}{C}")}"
			])
		kq4=random.choice([
			f"{vec(f"{B}{D}")}",
			f"{vec(f"{D}{B}")}",
			])

	if chon==3:
		phep_toan=f"{vec(f"{A}{B}")}+{vec(f"{A}{C}")}+{vec(f"{D}{A}")}+{vec(f"{B}{D}")}"
		noi_dung=(f"Cho các điểm ${{{danh_sach}}}$."
				f" Tính tổng ${phep_toan}$.")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{A}{B}")}+{vec(f"{B}{D}")}+{vec(f"{D}{A}")}+{vec(f"{A}{C}")}={vec(f"{A}{C}")}$."
		)	

		kq=f"{vec(f"{A}{C}")}"
		kq2=f"{vec(f"0")}"
		kq3=random.choice([
			f"{vec(f"{C}{A}")}",
			f"{vec(f"{C}{B}")}",
			f"{vec(f"{B}{C}")}"
			])
		kq4=random.choice([
			f"{vec(f"{B}{D}")}",
			f"{vec(f"{D}{B}")}",
			])

	if chon==4:
		phep_toan=f"{vec(f"{A}{B}")}+{vec(f"{C}{D}")}+{vec(f"{B}{C}")}+{vec(f"{D}{E}")}"
		noi_dung=(f"Cho các điểm ${{{danh_sach}}}$."
				f" Tính tổng ${phep_toan}$.")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{E}")}={vec(f"{A}{E}")}$."
		)	

		kq=f"{vec(f"{A}{E}")}"
		kq2=random.choice([
			f"{vec(f"0")}",
			f"{vec(f"{C}{E}")}"
			])
		kq3=random.choice([
			f"{vec(f"{C}{A}")}",
			f"{vec(f"{C}{B}")}",
			f"{vec(f"{B}{C}")}"
			])
		kq4=random.choice([
			f"{vec(f"{B}{D}")}",
			f"{vec(f"{D}{B}")}",
			f"{vec(f"{B}{E}")}"
			])


	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B2_08]-M2. Nhận dạng quy tắc hình bình hành
def y7y7u_L10_C5_B2_08():
	chon=random.randint(1,6)
	if chon==1:
		danh_sach=["A","B","C","D"]	
	if chon==2:
		danh_sach=["M","N","P","Q"]
	if chon==3:
		danh_sach=["A","B","M","N"]	
	if chon==4:
		danh_sach=["A","B","E","F"]
	if chon==5:
		danh_sach=["O","A","B","C"]
	if chon==6:
		danh_sach=["E","F","G","H"]
	
	A,B,C,D=danh_sach
	# code_hinh=my_module.code_latex_hinhbinhhanh(A,B,C,D)
	# code = my_module.moi_truong_anh_latex(code_hinh)
	#file_name=my_module.pdftoimage_timename(code)
	chon=random.randint(1,4)
	
	if chon==1:
		phep_toan=f"{vec(f"{A}{B}")}+{vec(f"{A}{D}")}"
		noi_dung=(f"Cho hình bình hành ${{{A}{B}{C}{D}}}$."
				f" Tính tổng ${phep_toan}$.")
		noi_dung=noi_dung.replace(",","")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{A}{C}")}$\n\n"
		)	

		kq=f"{vec(f"{A}{C}")}"
		kq2=f"{vec(f"{C}{A}")}"
		kq3=random.choice([
			f"{vec(f"{B}{D}")}",
			f"{vec(f"{C}{B}")}"
			])
		kq4=random.choice([
			f"{vec(f"{D}{B}")}"
			])

	if chon==2:
		phep_toan=f"{vec(f"{B}{A}")}+{vec(f"{B}{C}")}"
		noi_dung=(f"Cho hình bình hành ${{{A}{B}{C}{D}}}$."
				f" Tính tổng ${phep_toan}$.")
		noi_dung=noi_dung.replace(",","")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{B}{D}")}$\n\n"
		)	

		kq=f"{vec(f"{B}{D}")}"
		kq2=f"{vec(f"{C}{A}")}"
		kq3=random.choice([
			f"{vec(f"{A}{C}")}",
			f"{vec(f"{C}{B}")}"
			])
		kq4=random.choice([
			f"{vec(f"{D}{B}")}"
			])

	if chon==3:
		phep_toan=f"{vec(f"{C}{B}")}+{vec(f"{C}{D}")}"
		noi_dung=(f"Cho hình bình hành ${{{A}{B}{C}{D}}}$."
				f" Tính tổng ${phep_toan}$.")
		noi_dung=noi_dung.replace(",","")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{C}{A}")}$\n\n"
		)	

		kq=f"{vec(f"{C}{A}")}"
		kq2=f"{vec(f"{B}{D}")}"
		kq3=random.choice([
			f"{vec(f"{A}{C}")}",
			f"{vec(f"{C}{B}")}"
			])
		kq4=random.choice([
			f"{vec(f"{D}{B}")}"
			])

	if chon==4:
		phep_toan=f"{vec(f"{D}{A}")}+{vec(f"{D}{C}")}"
		noi_dung=(f"Cho hình bình hành ${{{A}{B}{C}{D}}}$."
				f" Tính tổng ${phep_toan}$.")
		noi_dung=noi_dung.replace(",","")

		noi_dung_loigiai=(
		f"${phep_toan}={vec(f"{D}{B}")}$\n\n"
		)	

		kq=f"{vec(f"{D}{B}")}"
		kq2=f"{vec(f"{B}{D}")}"
		kq3=random.choice([
			f"{vec(f"{A}{C}")}",
			f"{vec(f"{C}{B}")}"
			])
		kq4=random.choice([
			f"{vec(f"{A}{B}")}",
			f"{vec(f"{B}{A}")}"
			])

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B2_09]-TF-M2. Cho h.b.h. Xét Đ-S:quy tắc h.b.h, tổng-hiệu các vectơ.
def y7y7u_L10_C5_B2_09():
	chon=random.randint(1,3)
	if chon==1:
		danh_sach=f"A,B,C,D"	
	if chon==2:
		danh_sach=f"C,D,E,F"
	if chon==3:
		danh_sach=f"A,B,E,F"
	
	O=random.choice(["O","I"])
	M=random.choice(["M","P", "G"])
	N=random.choice(["N","Q", "H"])
	
	points=danh_sach.split(",")
	random.shuffle(points)
	A,B,C,D=points
	code_hinh=my_module.code_latex_hinhbinhhanh(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	a=random.randint(1,8)
	b=random.randint(1,8)
	BAD=random.choice([pi/6,pi/4,pi/3])
	BAD_degree=latex(math.degrees(BAD)).replace(".0","")

	noi_dung=(f"Cho hình bình hành ${{{A}{B}{C}{D}}}$ có tâm ${{{O}}}$, ${A}{B}={a}, {B}{C}={b}$ và góc $\\widehat{{{B}{A}{D}}}={BAD_degree}^\\circ$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{B}{C}}}$ và ${{{A}{D}}}$."
				f" Xét tính đúng-sai của các khẳng định sau.")	
		
	debai_word= f"{noi_dung}\n"
	chon=random.randint(1,3)
	if chon==1:
		kq_F=random.choice([f"{vec(f"{B}{C}")}", f"{vec(f"{C}{A}")}", f"{vec(f"{B}{D}")}", f"{vec(f"{D}{B}")}" ])
		kq1_T=f"*${vec(f"{A}{B}")} + {vec(f"{A}{D}")}={vec(f"{A}{C}")}$" 
		kq1_F=f"${vec(f"{A}{B}")} + {vec(f"{A}{D}")}={kq_F}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"{A}{B}")} + {vec(f"{A}{D}")}={vec(f"{A}{C}")}$"
	
	if chon==2:
		kq_F=random.choice([f"{vec(f"{B}{C}")}", f"{vec(f"{C}{A}")}", f"{vec(f"{C}{D}")}", f"{vec(f"{D}{B}")}" ])
		kq1_T=f"*${vec(f"{B}{A}")} + {vec(f"{B}{C}")}={vec(f"{B}{D}")}$" 
		kq1_F=f"${vec(f"{B}{A}")} + {vec(f"{B}{C}")}={kq_F}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"{B}{A}")} + {vec(f"{B}{C}")}={vec(f"{B}{D}")}$"

	if chon==3:
		kq_F=random.choice([f"{vec(f"{B}{C}")}", f"{vec(f"{A}{C}")}", f"{vec(f"{D}{A}")}", f"{vec(f"{D}{B}")}" ])
		kq1_T=f"*${vec(f"{C}{B}")} + {vec(f"{C}{D}")}={vec(f"{C}{A}")}$" 
		kq1_F=f"${vec(f"{C}{B}")} + {vec(f"{C}{D}")}={kq_F}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"{C}{B}")} + {vec(f"{C}{D}")}={vec(f"{C}{A}")}$"
	
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phương án 2
	chon=random.randint(1,4)
	if chon==1:
		kq_F=random.choice([f"{vec(f"{O}{D}")}", f"{vec(f"{A}{D}")}", f"{vec(f"{A}{C}")}" ])
		kq2_T=f"*${vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")}={vec(f"{D}{O}")}$"
		kq2_F=f"${vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")}={kq_F}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")}={vec(f"{O}{A}")}+{vec(f"{O}{C}")}+{vec(f"{O}{B}")}$"
			f"$={vec(f"{O}{B}")}={vec(f"{D}{O}")}$."
			)

	if chon==2:
		kq_F=random.choice([f"{vec(f"{O}{D}")}", f"{vec(f"{A}{D}")}", f"{vec(f"{A}{C}")}" ])
		kq2_T=f"*${vec(f"{O}{A}")} - {vec(f"{B}{O}")} + {vec(f"{O}{C}")}={vec(f"{D}{O}")}$"
		kq2_F=f"${vec(f"{O}{A}")} - {vec(f"{B}{O}")} + {vec(f"{O}{C}")}={kq_F}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{O}{A}")} - {vec(f"{B}{O}")} + {vec(f"{O}{C}")}={vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")}$"
			f"$={vec(f"{O}{A}")}+{vec(f"{O}{C}")}+{vec(f"{O}{B}")}={vec(f"{O}{B}")}={vec(f"{D}{O}")}$."
			)

	if chon==3:
		kq_F=random.choice([f"{vec(f"{B}{D}")}", f"{vec(f"{A}{D}")}", f"{vec(f"{A}{C}")}", f"{vec(f"{B}{C}")}" ])
		kq2_T=f"*${vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")} + {vec(f"{O}{D}")}={vec(f"0")}$"
		kq2_F=f"${vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")}={kq_F}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")} + {vec(f"{O}{D}")}"
			f"=({vec(f"{O}{A}")}+{vec(f"{O}{C}")}) + ({vec(f"{O}{B}")} + {vec(f"{O}{D}")} )$"
			f"$={vec(f"0")}+{vec(f"0")}={vec(f"0")}$."
			)

	if chon==4:
		kq_F=random.choice([f"{vec(f"{B}{D}")}", f"{vec(f"{A}{D}")}", f"{vec(f"{A}{C}")}", f"{vec(f"{B}{C}")}" ])
		kq2_T=f"*${vec(f"{O}{A}")} - {vec(f"{B}{O}")} + {vec(f"{O}{C}")} - {vec(f"{D}{O}")}={vec(f"0")}$"
		kq2_F=f"${vec(f"{O}{A}")} - {vec(f"{B}{O}")}+ {vec(f"{O}{C}")} - {vec(f"{D}{O}")}={kq_F}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{O}{A}")} - {vec(f"{B}{O}")} + {vec(f"{O}{C}")} - {vec(f"{D}{O}")}={vec(f"{O}{A}")} + {vec(f"{O}{B}")} + {vec(f"{O}{C}")} + {vec(f"{O}{D}")}"
			f"=({vec(f"{O}{A}")}+{vec(f"{O}{C}")}) + ({vec(f"{O}{B}")} + {vec(f"{O}{D}")} )$"
			f"$={vec(f"0")}+{vec(f"0")}={vec(f"0")}$."
			)
	
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phương án 3
	chon=random.randint(1,4)
	if chon==1:
		kq_F=random.choice([f"{vec(f"{B}{D}")}", f"{vec(f"{A}{M}")}", f"{vec(f"{C}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{N}{C}")} + {vec(f"{M}{C}")} = {vec(f"{A}{C}")}$" 
		kq3_F=f"${vec(f"{N}{C}")} + {vec(f"{M}{C}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{N}{C}")} + {vec(f"{M}{C}")}= {vec(f"{A}{M}")}+{vec(f"{M}{C}")}={vec(f"{A}{C}")}$."

	if chon==2:
		kq_F=random.choice([f"{vec(f"{B}{D}")}", f"{vec(f"{A}{M}")}", f"{vec(f"{C}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{N}{C}")} - {vec(f"{C}{M}")} = {vec(f"{A}{C}")}$" 
		kq3_F=f"${vec(f"{N}{C}")} - {vec(f"{C}{M}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{N}{C}")} - {vec(f"{C}{M}")}={vec(f"{N}{C}")} + {vec(f"{M}{C}")}= {vec(f"{A}{M}")}+{vec(f"{M}{C}")}={vec(f"{A}{C}")}$."
	
	if chon==3:
		kq_F=random.choice([f"{vec(f"{D}{N}")}", f"{vec(f"{A}{C}")}", f"{vec(f"{N}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{A}{M}")} + {vec(f"{C}{D}")} = {vec(f"{N}{D}")}$" 
		kq3_F=f"${vec(f"{A}{M}")} + {vec(f"{C}{D}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{A}{M}")} + {vec(f"{C}{D}")}= {vec(f"{N}{C}")}+{vec(f"{C}{D}")}={vec(f"{N}{D}")}$."

	if chon==4:
		kq_F=random.choice([f"{vec(f"{D}{N}")}", f"{vec(f"{A}{C}")}", f"{vec(f"{N}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{A}{M}")} - {vec(f"{D}{C}")} = {vec(f"{N}{D}")}$" 
		kq3_F=f"${vec(f"{A}{M}")} - {vec(f"{D}{C}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{A}{M}")} - {vec(f"{D}{C}")} = {vec(f"{A}{M}")} + {vec(f"{C}{D}")}= {vec(f"{N}{C}")}+{vec(f"{C}{D}")}={vec(f"{N}{D}")}$."
	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phương án 4
	goc=pi-BAD
	goc_degree=latex(math.degrees(goc)).replace(".0","")
	kq=latex(sqrt(a**2+b**2-2*a*b*cos(goc)))
	kq_F=latex(sqrt(a**2+b**2-a*b*cos(goc)))
	kq4_T=f"*$|{vec(f"{A}{B}")}+{vec(f"{A}{D}")}|={kq}$"
	kq4_F=f"$|{vec(f"{A}{B}")}+{vec(f"{A}{D}")}|={kq_F}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"$\\widehat{{{B}{A}{D}}}={BAD_degree}^\\circ \\Rightarrow \\widehat{{{A}{B}{C}}}={goc_degree}^\\circ$.\n\n"
		f"$|{vec(f"{A}{B}")}+{vec(f"{A}{D}")}|=|{vec(f"{A}{C}")}|= \\sqrt{{{A}{B}^2+{B}{C}^2-2.{A}{B}.{B}{C}.\\cos  \\widehat{{{A}{B}{C}}}}}$\n\n"
		f"$=\\sqrt{{{a}^2+{b}^2-2.{a}.{b}.\\cos {goc_degree}^\\circ}}={kq}$.")

	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)	

	debai= f"{noi_dung}\n{file_name}\n\n"\
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

#[D10_C5_B2_10]-TL-M2. Cho hai lực hợp góc. Tính độ lớn của tổng lực.
def y7y7u_L10_C5_B2_10():
	M=random.choice(["M","N", "O", "I"])
	A=["A","C", "E"]
	B=["B", "D", "F"]
	i=random.randint(0,2)
	A,B=A[i], B[i]
	v_F1, v_F2 = f"{vec(f"F_1")}", f"{vec(f"F_2")}"	
	v_MA, v_MB = f"{vec(f"{M}{A}")}", f"{vec(f"{M}{B}")}"
	F1, F2=random.randint(10,200), random.randint(10,200)

	goc= random.choice([pi/3, pi/4, pi/6, 2*pi/3, 3*pi/4, 4*pi/5])
	goc_degree=sp.deg(goc)	

	code_hinh=rf"""
	\begin{{tikzpicture}}[smooth,font=\footnotesize,scale=0.8]
			\path
			(0,0) coordinate ({M})
			(3,0) coordinate ({A})
			($({M})!1!60:({A})$)coordinate ({B});
			\fill[ball color=red]({M}) circle (0.16);
			\draw[->] ({M})--({A});
			\draw[->] ({M})--({B});
			\foreach \x/\g in {{{A}/0,{B}/60,{M}/-90}} \draw [fill=black] (\x) circle (.05) + (\g:.5) node{{$\x$}};
			\begin{{scope}}
				\clip ({B})--({M})--({A});
				\draw[double] ({M}) circle(0.7cm);
			\end{{scope}}
		\node[right] at (0.6,0.5) {{${goc_degree}^\circ$}};
	\end{{tikzpicture}}
	"""
	code = my_module.moi_truong_anh_latex(code_hinh)
	#file_name=my_module.pdftoimage_timename(code)
	file_name=""

	while sqrt(F1**2+F2**2-2*F1*F2*cos(goc))>9999:
		F1, F2=random.randint(10,200), random.randint(10,200)
		goc= random.choice([pi/3, pi/4, pi/6, 2*pi/3, 3*pi/4, 4*pi/5])

	goc_bu=pi-goc
	goc_bu_degree=sp.deg(goc_bu)
	F=sqrt(F1**2+F2**2-2*F1*F2*cos(goc_bu))
	
	dap_an=f"{F:.0f}".replace(".",",")

	noi_dung =(f"Cho hai lực ${v_F1}={v_MA},{v_F2}={v_MB}$ cùng tác động vào một vật tại điểm ${{{M}}}$."
		f" Cường độ hai lực ${v_F1}, {v_F2}$ lần lượt là ${{{F1}}}$ (N) và ${{{F2}}}$ (N)" 
		f" và góc $\\widehat{{{A}{M}{B}}}={goc_degree}^\\circ$."
		f" Tính cường độ của lực tổng hợp tác động vào vật. (làm tròn đến hàng đơn vị)"

	)
	noi_dung_loigiai=(f"Gọi ${vec(f"F")}={v_F1}+{v_F2}$. \n\n"
		f"Dựng hình bình hành ${{{M}{A}D{B}}}$. Ta có $\\widehat{{{M}{A}{B}}}={goc_bu_degree}^\\circ$. \n\n"
    f"Khi đó: $|{vec(f"F")}|=|{v_MA}+{v_MB}|=|{vec(f"{M}D")}|=\\sqrt{{{F1}^2+{F2}^2-2.{F1}.{F2}.\\cos {goc_bu_degree}^\\circ}}={latex(F)}$.\n\n"
    f"Kết quả làm tròn: {dap_an}"
		)
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C5_B2_11]-TF-M2. Cho h.c.n. Xét Đ-S:hướng-phương-bằng, quy tắc h.b.h, tổng-hiệu, độ dài các vectơ.
def y7y7u_L10_C5_B2_11():
	chon=random.randint(1,3)
	if chon==1:
		danh_sach=f"A,B,C,D"	
	if chon==2:
		danh_sach=f"C,D,E,F"
	if chon==3:
		danh_sach=f"A,B,E,F"
	
	O=random.choice(["O","I"])
	M=random.choice(["M","P", "G"])
	N=random.choice(["N","Q", "H"])
	
	points=danh_sach.split(",")
	random.shuffle(points)
	A,B,C,D=points
	code_hinh=code_latex_hinhchunhat(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	
	a=random.randint(1,8)
	b=random.randint(1,8)
	BAD=random.choice([pi/6,pi/4,pi/3])
	BAD_degree=latex(math.degrees(BAD)).replace(".0","")

	noi_dung=(f"Cho hình chữ nhật ${{{A}{B}{C}{D}}}$ có tâm ${{{O}}}$, ${A}{B}={a}, {B}{C}={b}$."
		f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{B}{C}}}$ và ${{{A}{D}}}$."
				f" Xét tính đúng-sai của các khẳng định sau.")

	debai_word= f"{noi_dung}\n{file_name}\n"
	

	vecto_1=[vec(f"{A}{B}"), vec(f"{A}{D}"), vec(f"{O}{A}"), vec(f"{A}{O}"), vec(f"{O}{B}"), vec(f"{B}{O}") ]
	vecto_2=[vec(f"{D}{C}"), vec(f"{B}{C}"), vec(f"{C}{O}"), vec(f"{O}{C}"), vec(f"{D}{O}"), vec(f"{O}{D}")]
	i=random.randint(0,5)
	vecto_1, vecto_2  = vecto_1[i], vecto_2[i]

	chon=random.randint(1,5)
	if chon==1:
		kq1_T=f"* Hai vectơ ${vecto_1}$ và ${vecto_2}$ bằng nhau" 
		kq1_F=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ đối nhau"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ bằng nhau vì chúng cùng hướng và cùng độ dài."
	
	if chon==2:
		kq1_T=f"* Hai vectơ ${vecto_1}$ và ${vecto_2}$ cùng hướng" 
		kq1_F=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ ngược hướng"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ là cùng hướng."

	if chon==3:
		kq1_T=f"* Hai vectơ ${vecto_1}$ và ${vecto_2}$ cùng phương" 
		kq1_F=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ khác phương"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ là cùng phương."

	vecto_1=[vec(f"{A}{B}"), vec(f"{A}{D}"), vec(f"{O}{A}"), vec(f"{A}{O}"), vec(f"{O}{B}"), vec(f"{B}{O}") ]
	vecto_2=[vec(f"{C}{D}"), vec(f"{C}{B}"), vec(f"{O}{C}"), vec(f"{C}{O}"), vec(f"{O}{D}"), vec(f"{D}{O}")]
	i=random.randint(0,5)
	vecto_1, vecto_2  = vecto_1[i], vecto_2[i]

	if chon==4:
		kq1_T=f"* Hai vectơ ${vecto_1}$ và ${vecto_2}$ ngược hướng" 
		kq1_F=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ cùng hướng"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ là ngược hướng."

	if chon==5:
		kq1_T=f"* Hai vectơ ${vecto_1}$ và ${vecto_2}$ đối nhau" 
		kq1_F=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ bằng nhau"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Hai vectơ ${vecto_1}$ và ${vecto_2}$ là đối nhau vì chúng ngược hướng và có độ dài bằng nhau."	

	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#PA2: Quy tắc hình bình hành
	chon=random.randint(1,4)
	if chon==1:
		kq2_T=f"*${vec(f"{A}{B}")}+{vec(f"{A}{D}")}={vec(f"{A}{C}")}$"
		kq2_F=f"${vec(f"{A}{B}")}+{vec(f"{A}{D}")}={vec(f"{C}{A}")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{A}{B}")}+{vec(f"{A}{D}")}={vec(f"{A}{C}")}$."
	
	if chon==2:
		kq2_T=f"*${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={vec(f"{B}{D}")}$"
		kq2_F=f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={vec(f"{D}{B}")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={vec(f"{B}{D}")}$."

	if chon==3:
		kq2_T=f"* ${vec(f"{C}{B}")}+{vec(f"{C}{D}")}={vec(f"{C}{A}")}$"
		kq2_F=f"${vec(f"{C}{B}")}+{vec(f"{C}{D}")}={vec(f"{A}{C}")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{C}{B}")}+{vec(f"{C}{D}")}={vec(f"{C}{A}")}$."

	if chon==4:
		kq2_T=f"* ${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={vec(f"{D}{B}")}$"
		kq2_F=f"${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={vec(f"{B}{D}")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={vec(f"{D}{B}")}$."

	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#PA2: Tổng hiệu các vectơ
	#Phương án 3
	chon=random.randint(1,4)
	if chon==1:
		kq_F=random.choice([f"{vec(f"{B}{D}")}", f"{vec(f"{A}{M}")}", f"{vec(f"{C}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{N}{C}")} + {vec(f"{M}{C}")} = {vec(f"{A}{C}")}$" 
		kq3_F=f"${vec(f"{N}{C}")} + {vec(f"{M}{C}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{N}{C}")} + {vec(f"{M}{C}")}= {vec(f"{A}{M}")}+{vec(f"{M}{C}")}={vec(f"{A}{C}")}$."

	if chon==2:
		kq_F=random.choice([f"{vec(f"{B}{D}")}", f"{vec(f"{A}{M}")}", f"{vec(f"{C}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{N}{C}")} - {vec(f"{C}{M}")} = {vec(f"{A}{C}")}$" 
		kq3_F=f"${vec(f"{N}{C}")} - {vec(f"{C}{M}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{N}{C}")} - {vec(f"{C}{M}")}={vec(f"{N}{C}")} + {vec(f"{M}{C}")}= {vec(f"{A}{M}")}+{vec(f"{M}{C}")}={vec(f"{A}{C}")}$."
	
	if chon==3:
		kq_F=random.choice([f"{vec(f"{D}{N}")}", f"{vec(f"{A}{C}")}", f"{vec(f"{N}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{A}{M}")} + {vec(f"{C}{D}")} = {vec(f"{N}{D}")}$" 
		kq3_F=f"${vec(f"{A}{M}")} + {vec(f"{C}{D}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{A}{M}")} + {vec(f"{C}{D}")}= {vec(f"{N}{C}")}+{vec(f"{C}{D}")}={vec(f"{N}{D}")}$."

	if chon==4:
		kq_F=random.choice([f"{vec(f"{D}{N}")}", f"{vec(f"{A}{C}")}", f"{vec(f"{N}{A}")}", f"{vec(f"{M}{N}")}" ])
		kq3_T=f"*${vec(f"{A}{M}")} - {vec(f"{D}{C}")} = {vec(f"{N}{D}")}$" 
		kq3_F=f"${vec(f"{A}{M}")} - {vec(f"{D}{C}")} = {kq_F}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{A}{M}")} - {vec(f"{D}{C}")} = {vec(f"{A}{M}")} + {vec(f"{C}{D}")}= {vec(f"{N}{C}")}+{vec(f"{C}{D}")}={vec(f"{N}{D}")}$."

	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		
	AC=sqrt(a**2+b**2)
	
	kq4_T=f"*$|{vec(f"{A}{M}")}+{vec(f"{N}{D}")}|={latex(AC)}$"
	kq4_F=f"$|{vec(f"{A}{M}")}+{vec(f"{N}{D}")}|={a+b}$"
	if a+b==AC:
		kq4_F=f"$|{vec(f"{A}{M}")}+{vec(f"{N}{D}")}|={a+b+1}$."
	 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"$|{vec(f"{A}{M}")}+{vec(f"{N}{D}")}|=|{vec(f"{A}{M}")}+{vec(f"{M}{C}")}|=|{vec(f"{A}{C}")}|"
	f"=\\sqrt{{{a}^2+{b}^2}}={latex(AC)}$."
	)
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

#[D10_C5_B2_12]-TL-M3. Cho tam giác vuông. Tính độ dài của vectơ có điểm thỏa mãn đẳng thức vectơ.
def y7y7u_L10_C5_B2_12():
	A=['A', 'B', 'D', 'P', 'O', 'O']
	B=['B', 'C',' E', 'Q', 'A', 'B']
	C=['C', 'D', 'F', 'R', 'B', 'C']

	M=random.choice(['M','N','K'])
	I=random.choice(['I','G','H'])
	i=random.randint(0,5)
	A,B,C=A[i],B[i],C[i]

	l_AB= random.randint(1,5)
	l_AC= random.randint(1,7)

	chon=random.randint(1,2)

	if chon==1:
		dang_thuc=random.choice([
			f"${vec(f"{A}{C}")}-{vec(f"{A}{B}")}-{vec(f"{A}{M}")}={vec("0")}$",
			f"${vec(f"{A}{C}")}+{vec(f"{B}{A}")}-{vec(f"{A}{M}")}={vec("0")}$"
			f"${vec(f"{A}{C}")}+{vec(f"{B}{A}")}={vec(f"{A}{M}")}$"
			])
		noi_dung = (
		f"Cho tam giác vuông ${{{A}{B}{C}}}$ có các cạnh góc vuông là ${A}{B}={l_AB}, {A}{C}={l_AC}$."
		f" Điểm ${{{M}}}$ thỏa mãn {dang_thuc}."
		f" Tính độ dài vectơ ${vec(f"{A}{M}")}$."
		)

		if int(sqrt(l_AB**2+l_AC**2))==sqrt(l_AB**2+l_AC**2):		
			dap_an=f"{int(sqrt(l_AB**2+l_AC**2))}"
		else:
			dap_an=f"{round(sqrt(l_AB**2+l_AC**2),1):.1f}".replace(".",",")	

		noi_dung_loigiai=(
		f"Ta có: {dang_thuc} $\\Rightarrow {vec(f"{A}{C}")}-{vec(f"{A}{B}")}={vec(f"{A}{M}")}\\Rightarrow {vec(f"{A}{M}")}={vec(f"{B}{C}")}$.\n\n"
		f"Do đó: $|{vec(f"{A}{M}")}|=|{vec(f"{B}{C}")}|=\\sqrt{{{l_AB}^2+{l_AC}^2}}={latex(sqrt(l_AB**2+l_AC**2))}$.\n\n"
		f" Đáp án: {dap_an}")
	
	
	if chon==2:
		vecto=random.choice([vec(f"{A}{I}"), vec(f"{B}{I}"), vec(f"{C}{I}") ])
		dap_an=f"{round(sqrt(l_AB**2+l_AC**2)/2,1):1f}".replace(".",",")

		dang_thuc=random.choice([
		f"${vec(f"{I}{M}")}+{vec(f"{A}{C}")}={vec(f"{A}{I}")}+{vec(f"{B}{M}")}$",
		f"${vec(f"{I}{M}")}-{vec(f"{C}{A}")}={vec(f"{B}{M}")}-{vec(f"{I}{A}")}$",
		f"${vec(f"{I}{M}")}-{vec(f"{C}{A}")}={vec(f"{A}{I}")}-{vec(f"{M}{B}")}$",
		f"${vec(f"{I}{M}")}-{vec(f"{C}{A}")}-{vec(f"{A}{I}")}+{vec(f"{M}{B}")}={vec("0")}$"

		])

		noi_dung = (
		f"Cho tam giác vuông ${{{A}{B}{C}}}$ có các cạnh góc vuông là ${A}{B}={l_AB}, {A}{C}={l_AC}$."
		f" Gọi ${{{M}}}$ là trung điểm của cạnh ${A}{C}$."
		f" Gọi ${{{I}}}$ là điểm thỏa mãn {dang_thuc}."
		f" Tính độ dài vectơ ${vecto}$. (kết quả làm tròn đến hàng phần mười)")

		noi_dung_loigiai=(
		f"{dang_thuc}"
		f"$\\Rightarrow {vec(f"{I}{M}")}+{vec(f"{M}{B}")}+{vec(f"{I}{A}")}+{vec(f"{A}{C}")}={vec(f"0")}$\n\n"
		f"$\\Rightarrow {vec(f"{I}{B}")}+{vec(f"{I}{C}")}={vec(f"0")}$. Suy ra ${{{I}}}$ là trung điểm của ${{{B}{C}}}$.\n\n"
		f"$|{vecto}|=\\dfrac{{{B}{C}}}{{2}}=\\dfrac{{{l_AB}^2+{l_AC}^2}}{{2}}={latex(sqrt(l_AB**2+l_AC**2)/2)}$.\n\n"\
		f"Đáp án: {dap_an}"	)
	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C5_B2_13]-TL-M3. Cho h.c.n. Tính độ dài tổng-hiệu, độ dài các vectơ.
def y7y7u_L10_C5_B2_13():
	A=['A', 'A', 'A', 'P', 'C', 'B']
	B=['B', 'B', 'B', 'Q', 'D', 'C']
	C=['C', 'E', 'P', 'R', 'E', 'D']
	D=['D', 'F', 'Q', 'S', 'F', 'E']

	i=random.randint(0,5)
	A,B,C,D=A[i],B[i],C[i],D[i]
	
	O=random.choice(["O","I"])
	M=random.choice(["M","J","G"])
	N=random.choice(["N","L", "H"])


	code_hinh=code_latex_hinhchunhat(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	
	l_AB=random.randint(1,6)
	l_AD=l_AB+random.randint(1,3)
	BAD=random.choice([pi/6,pi/4,pi/3])
	BAD_degree=latex(math.degrees(BAD)).replace(".0","")

	ten_vt=random.choice(["a","u","x","v","m"])
	chon=random.randint(1,3)

	if chon==1:
		noi_dung=(f"Cho hình chữ nhật ${{{A}{B}{C}{D}}}$ có tâm ${{{O}}}$, ${A}{B}={l_AB}, {A}{D}={l_AD}$."
			f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{B}{C}}}$ và ${{{A}{D}}}$."
			f" Tính độ dài của vectơ ${vec(f"{ten_vt}")}={vec(f"{A}{M}")}+{vec(f"{N}{D}")}$ (kết quả làm tròn đến hàng phần mười)."
			)

		AC=sqrt(l_AB**2+l_AD**2)
		dap_an=f"{round(AC,1):.1f}".replace(".",",")

		noi_dung_loigiai=(f"$|{vec(f"{A}{M}")}+{vec(f"{N}{D}")}|=|{vec(f"{A}{M}")}+{vec(f"{M}{C}")}|=|{vec(f"{A}{C}")}|"
		f"=\\sqrt{{{l_AB}^2+{l_AD}^2}}={latex(AC)}$.\n\n"
		f"Đáp án: {dap_an}"	)
	
	
	if chon==2:
		dang_thuc=random.choice([
		f"{vec(f"{M}{B}")}-{vec(f"{M}{D}")}-{vec(f"{C}{D}")}",
		f"{vec(f"{O}{B}")}-{vec(f"{O}{D}")}+{vec(f"{D}{C}")}"
		])
		noi_dung=(f"Cho hình chữ nhật ${{{A}{B}{C}{D}}}$ có tâm ${{{O}}}$, ${A}{B}={l_AB}, {A}{D}={l_AD}$."
			f" Gọi ${{{M}}}$ là trung điểm của ${{{B}{C}}}$."
			f" Tính độ dài của vectơ ${vec(f"{ten_vt}")}={dang_thuc}$ (kết quả làm tròn đến hàng phần mười)."
			)

		DK=sqrt(l_AD**2+(2*l_AB)**2)
		dap_an=f"{round(DK,1):.1f}".replace(".",",")

		noi_dung_loigiai=(f"Gọi ${{K}}$ là điểm đối xứng với ${{{A}}}$ qua ${{{B}}}$.\n\n"
			f"Tứ giác ${{{B}{D}{C}K}}$ là hình bình hành.\n\n"
		f"${vec(f"{ten_vt}")}={dang_thuc}={vec(f"{D}{B}")}+{vec(f"{D}{C}")}={vec(f"{D}K")}$.\n\n"
		f"$|{vec(f"{ten_vt}")}|=|{vec(f"{D}K")}|=\\sqrt{{{D}{A}^2+{A}K^2}}=\\sqrt{{{l_AD}^2+{l_AB*2}^2}}={latex(DK)}$.\n\n"
		
		f"Đáp án: {dap_an}")

	if chon==3:
		dang_thuc=f"{vec(f"{D}{O}")}-{vec(f"{M}{D}")}+{vec(f"{O}{B}")}-{vec(f"{C}{M}")}"
		
		noi_dung=(f"Cho hình chữ nhật ${{{A}{B}{C}{D}}}$ có tâm ${{{O}}}$, ${A}{B}={l_AB}, {A}{D}={l_AD}$."
			f" Gọi ${{{M}}}$ là trung điểm của ${{{B}{C}}}$."
			f" Tính độ dài của vectơ ${vec(f"{ten_vt}")}={dang_thuc}$ (kết quả làm tròn đến hàng phần mười)."
			)

		DK=sqrt(l_AD**2+(2*l_AB)**2)
		dap_an=f"{round(DK,1):.1f}".replace(".",",")

		noi_dung_loigiai=(f"Gọi ${{K}}$ là điểm đối xứng với ${{{A}}}$ qua ${{{B}}}$.\n\n"
			f"Tứ giác ${{{B}{D}{C}K}}$ là hình bình hành.\n\n"
		f"${vec(f"{ten_vt}")}={dang_thuc}={vec(f"{D}{O}")}+{vec(f"{O}{B}")}+{vec(f"{M}{C}")}-{vec(f"{M}{D}")}"
		f"={vec(f"{D}{B}")}+{vec(f"{D}{C}")}={vec(f"{D}K")}$.\n\n"
		f"$|{vec(f"{ten_vt}")}|=|{vec(f"{D}K")}|=\\sqrt{{{D}{A}^2+{A}K^2}}=\\sqrt{{{l_AD}^2+{l_AB*2}^2}}={latex(DK)}$.\n\n"
		
		f"Đáp án: {dap_an}"	)
	

	
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an
#--------------------------------------------------------------------------->
#Bài 3 - Tích vectơ với một số
#[D10_C5_B3_01]-M2. Cho tứ giác. Tìm khẳng định đúng về quy tắc cộng trừ.
def y7y7u_L10_C5_B3_01():
	A=["A","O","C","O","O","A"]
	B=["B","A","D","B","C","B"]
	C=["C","B","E","C","D","E"]
	D=["D","C","F","D","E","F"]
	i=random.randint(0,5)
	A, B, C, D = A[i], B[i], C[i], D[i]
	M=["M","H", "G"]
	N=["N","I", "H"]
	P=["P","K", "I"]
	i=random.randint(0,2)
	M, N, P = M[i], N[i], P[i]	
	
	AB, AC, AD = f"{A}{B}", f"{A}{C}", f"{A}{D}"
	ten_tudien = f"{{{A}{B}{C}{D}}}"
	
	chon=random.randint(1,5)
	
	if chon==1:
		noi_dung=f"Cho tứ giác ${ten_tudien}$. Gọi ${M},{N},{P}$ lần lượt là trung điểm của các đoạn ${AB},{AC},{AD}$. Tìm khẳng định sai."
		kq=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{D}}}=2\\overrightarrow{{{M}{P}}}$"
		kq2=f"$\\overrightarrow{{{A}{D}}}+\\overrightarrow{{{C}{A}}}=2\\overrightarrow{{{N}{P}}}$"
		kq3=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{C}}}=2\\overrightarrow{{{N}{M}}}$"
		kq4=f"$\\overrightarrow{{{B}{C}}}+\\overrightarrow{{{C}{D}}}=2\\overrightarrow{{{M}{P}}}$"
		noi_dung_loigiai=f"{kq} là khẳng định sai vì $\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{D}}}=2\\overrightarrow{{{P}{M}}}$."

	if chon==2:
		noi_dung=f"Cho tứ giác ${ten_tudien}$. Gọi ${M},{N},{P}$ lần lượt là trung điểm của các đoạn ${AB},{AC},{AD}$ Tìm khẳng định đúng."
		kq=f"$\\overrightarrow{{{C}{B}}}-\\overrightarrow{{{A}{C}}}=2\\overrightarrow{{{C}{M}}}$"
		kq2=f"$\\overrightarrow{{{D}{A}}}+\\overrightarrow{{{D}{C}}}=2\\overrightarrow{{{N}{D}}}$"
		kq3=f"$\\overrightarrow{{{B}{A}}}-\\overrightarrow{{{C}{B}}}=2\\overrightarrow{{{N}{B}}}$"
		kq4=f"$\\overrightarrow{{{B}{A}}}+\\overrightarrow{{{B}{D}}}=-2\\overrightarrow{{{B}{P}}}$"
		noi_dung_loigiai=f"{kq} là khẳng định đúng vì $\\overrightarrow{{{C}{B}}}-\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{C}{B}}}+\\overrightarrow{{{C}{A}}}=2\\overrightarrow{{{C}{M}}}$."
	if chon==3:
		noi_dung=f"Cho tứ giác ${ten_tudien}$. Gọi ${{G}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$. Tìm khẳng định đúng."
		kq=f"${vec(f"{AB}")}+{vec(f"{AC}")}+{vec(f"{AD}")}=3{vec(f"{A}G")}$"
		kq2=f"${vec(f"{AB}")}+{vec(f"{AC}")}+{vec(f"{AD}")}={vec("0")}$"
		kq3=f"${vec(f"G{A}")}+{vec(f"G{B}")}+{vec(f"G{C}")}={vec(f"DG")}$"
		kq4=f"${vec(f"G{A}")}+{vec(f"G{B}")}+{vec(f"G{C}")}={vec(f"GD")}$"
		noi_dung_loigiai=f"{kq} là khẳng định đúng."
	if chon==4:
		noi_dung=f"Cho tứ giác ${ten_tudien}$. Gọi ${{{M}}}$ là trung điểm của cạnh ${B}{C}$, ${{G}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$. Tìm khẳng định đúng."
		kq=f"${vec(f"G{B}")} + {vec(f"G{C}")} =- {vec(f"G{D}")}$"
		kq2=f"${vec(f"G{B}")} + {vec(f"G{C}")} ={vec(f"G{M}")}$"
		kq3=f"${vec(f"{B}{C}")} =2 {vec(f"{C}{M}")}$"
		kq4=f"${vec(f"{M}{B}")} =\\dfrac{{1}}{{2}} {vec(f"{B}{C}")}$"
		noi_dung_loigiai=f"{kq} là khẳng định đúng vì ${vec(f"G{B}")} + {vec(f"G{C}")} = 2G{M}- {vec(f"{D}G")}$."
	if chon==5:
		noi_dung=f"Cho tứ giác ${ten_tudien}$. Gọi ${{G}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$."\
		f" Gọi ${vec("x")}={vec(f"{AB}")}+{vec(f"{AC}")}+{vec(f"{AD}")}$. Tìm khẳng định đúng."
		kq=f"${vec("x")}={vec(f"{A}G")}$"
		kq2=f"${vec("x")}=\\dfrac{{2}}{{3}}{vec(f"{A}G")}$"
		kq3=f"${vec("x")}=\\dfrac{{3}}{{2}}{vec(f"{A}G")}$"
		kq4=f"${vec("x")}=3{vec(f"{A}G")}$"
		noi_dung_loigiai=f"{kq} là khẳng định đúng."
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B3_02]-M2. Cho tam giác. Tìm đẳng thức đúng về vectơ
def y7y7u_L10_C5_B3_02():
	chon=random.randint(1,3)
	if chon==1:
		danh_sach=["A","B","C"]
		ten="ABC"
	
	if chon==2:
		danh_sach=["B","C","D"]
		ten="BCD"

	if chon==3:
		danh_sach=["O","A","B"]
		ten="OAB"
	random.shuffle(danh_sach)
	A,B,C=danh_sach

	M=random.choice(["M","N","P"])
	G=random.choice(["G","H"])

	noi_dung=(
	f"Cho tam giác ${{{ten}}}$ có trung tuyến ${{{A}{M}}}$ và trọng tâm ${{{G}}}$."
	f" Tìm khẳng định đúng trong các khẳng định nào sau."
	)	

	kq=random.choice([
	f"${vec(f"{A}{G}")}=\\dfrac{{2}}{{3}}{vec(f"{A}{M}")}$",
	f"${vec(f"{A}{G}")}=-\\dfrac{{2}}{{3}}{vec(f"{M}{A}")}$",
	f"${vec(f"{A}{G}")}=2{vec(f"{G}{M}")}$",
	f"${vec(f"{A}{G}")}=-2{vec(f"{M}{G}")}$",
	f"${vec(f"{A}{M}")}=\\dfrac{{3}}{{2}}{vec(f"{A}{G}")}$",
	f"${vec(f"{A}{M}")}=-\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}$",
		])

	kq_false=[
	f"${vec(f"{A}{G}")}=-\\dfrac{{1}}{{3}}{vec(f"{A}{M}")}$",
	f"${vec(f"{A}{G}")}=\\dfrac{{1}}{{2}}{vec(f"{G}{M}")}$",
	f"${vec(f"{G}{A}")}=2{vec(f"{G}{M}")}$",
	f"${vec(f"{G}{A}")}=-2{vec(f"{M}{G}")}$",
	f"${vec(f"{M}{G}")}=\\dfrac{{1}}{{3}}{vec(f"{A}{M}")}$",
	f"${vec(f"{A}{G}")}=\\dfrac{{2}}{{3}}{vec(f"{M}{A}")}$",
	f"${vec(f"{M}{B}")}={vec(f"{M}{C}")}$",
	f"${vec(f"{G}{A}")}={vec(f"{G}{M}")}$"
	]
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	noi_dung_loigiai=(
	f"{kq} là khẳng định đúng."
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

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
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

#[D10_C5_B3_03]-M2. Cho MA=kMB. Tìm đẳng thức đúng về vectơ
def y7y7u_L10_C5_B3_03():
	A=random.choice(["A", "C", "E", "I"])
	B=random.choice(["B", "D", "F", "K"])
	M=random.choice(["O","M", "N", "P"])
	chon=random.randint(1,2)
	
	if chon==1:
		noi_dung=(f" Cho đoạn thẳng ${{{A}{B}}}$ có trung điểm ${{{M}}}$."
		f" Tìm khẳng định đúng trong các khẳng định nào sau."
		)

		kq=random.choice([
		f"{vec(f"{A}{B}")}=2{vec(f"{M}{B}")}",
		f"{vec(f"{A}{B}")}=2{vec(f"{A}{M}")}",
		f"{vec(f"{B}{A}")}=2{vec(f"{B}{M}")}",
		f"{vec(f"{A}{M}")}=\\dfrac{{1}}{{2}}{vec(f"{A}{B}")}",
		f"{vec(f"{B}{M}")}=\\dfrac{{1}}{{2}}{vec(f"{B}{A}")}",
		f"{vec(f"{B}{M}")}=-\\dfrac{{1}}{{2}}{vec(f"{A}{B}")}",
		f"{vec(f"{A}{M}")}=-\\dfrac{{1}}{{2}}{vec(f"{B}{A}")}"
		])
		kq_false=[
		f"{vec(f"{A}{M}")}={vec(f"{B}{M}")}",
		f"{vec(f"{M}{A}")}={vec(f"{M}{B}")}",
		f"{vec(f"{A}{B}")}=3{vec(f"{A}{M}")}",
		f"{vec(f"{B}{A}")}=2{vec(f"{A}{M}")}",
		f"{vec(f"{A}{M}")}=\\dfrac{{1}}{{2}}{vec(f"{B}{A}")}",
		f"{vec(f"{B}{M}")}=\\dfrac{{1}}{{2}}{vec(f"{A}{B}")}",
		]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]

		noi_dung_loigiai=(
		f"${kq}$ là khẳng định đúng."
		)
	
	if chon==2:
		k=random.randint(2,4)
		noi_dung=(f" Cho đoạn thẳng ${{{A}{B}}}$. Gọi ${{{M}}}$ là điểm thuộc đoạn ${{{A}{B}}}$ sao cho"
		f" ${M}{A}={k}{M}{B}$. Tìm khẳng định đúng trong các khẳng định nào sau."
		)
		kq=random.choice([
			f"{vec(f"{M}{A}")}=-{k}{vec(f"{M}{B}")}",
			f"{vec(f"{A}{M}")}={k}{vec(f"{M}{B}")}",
			f"{vec(f"{A}{M}")}={phan_so(k/(k+1))}{vec(f"{A}{B}")}",
			f"{vec(f"{A}{M}")}=-{phan_so(k/(k+1))}{vec(f"{B}{A}")}",
			f"{vec(f"{M}{A}")}={phan_so(k/(k+1))}{vec(f"{B}{A}")}",
			f"{vec(f"{M}{B}")}={phan_so(1/k)}{vec(f"{A}{M}")}",
			f"{vec(f"{M}{B}")}=-{phan_so(1/k)}{vec(f"{M}{A}")}",
			])
		kq_false=[
			f"{vec(f"{M}{B}")}=-{k}{vec(f"{M}{A}")}",
			f"{vec(f"{M}{B}")}={k}{vec(f"{A}{M}")}",
			f"{vec(f"{A}{B}")}={phan_so(k/(k+1))}{vec(f"{A}{M}")}",
			f"{vec(f"{A}{B}")}=-{phan_so(k/(k+1))}{vec(f"{B}{M}")}",
			f"{vec(f"{M}{A}")}={k}{vec(f"{M}{B}")}",
			f"{vec(f"{M}{A}")}={k+1}{vec(f"{A}{M}")}",
			f"{vec(f"{A}{B}")}=-{k+1}{vec(f"{M}{B}")}",
			f"{vec(f"{B}{A}")}={k+2}{vec(f"{A}{M}")}",
			]
		random.shuffle(kq_false)
		kq2,kq3,kq4=kq_false[0:3]
		noi_dung_loigiai=(f"${kq}$ là khẳng định đúng.")
	

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
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

	debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\choice\n"
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B3_04]-M2. Cho hình bình hành. Tìm đẳng thức đúng về vectơ
def y7y7u_L10_C5_B3_04():
	danh_sach=["A","B","C","D"]
	random.shuffle(danh_sach)
	A,B,C,D=danh_sach
	I=random.choice(["O","I"])
	G=random.choice(["G","H","J"])

	code_hinh=code_latex_hinhbinhhanh(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	noi_dung=(
	f"Cho hình bình hành ${{{A}{B}{C}{D}}}$ có tâm ${{{I}}}$, ${{{G}}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$."
	f"Tìm khẳng định đúng trong các khẳng định sau."
	)
	k=random.randint(2,4)

	kq=random.choice([
	f"{vec(f"{A}{B}")}+{vec(f"{A}{C}")}+{vec(f"{A}{D}")}=3{vec(f"{A}{G}")}",
	f"{vec(f"{I}{A}")}+{vec(f"{I}{B}")}+{vec(f"{I}{C}")}+{vec(f"{I}{D}")}={vec(f"0")}",
	f"{vec(f"{A}{B}")}+{vec(f"{A}{C}")}+{vec(f"{A}{D}")}=3{vec(f"{A}{G}")}",
	f"{vec(f"{A}{B}")}+{vec(f"{A}{C}")}+{vec(f"{A}{D}")}=3{vec(f"{A}{C}")}",
	f"{vec(f"{A}{B}")}+{k}{vec(f"{A}{C}")}+{vec(f"{A}{D}")}={k+1}{vec(f"{A}{C}")}",
	f"{vec(f"{A}{B}")}-{k}{vec(f"{A}{C}")}+{vec(f"{A}{D}")}={1-k}{vec(f"{A}{C}")}",
	f"{vec(f"{I}{A}")}+{vec(f"{I}{B}")}={vec(f"{D}{A}")}",
	f"{vec(f"{I}{A}")}+{vec(f"{I}{B}")}={vec(f"{C}{B}")}",
	f"{vec(f"{G}{A}")}=-2{vec(f"{G}{C}")}",
	f"{vec(f"{G}{A}")}=2{vec(f"{C}{G}")}",
	f"{vec(f"{A}{C}")}=-3{vec(f"{C}{G}")}",
	f"{vec(f"{A}{C}")}=3{vec(f"{G}{C}")}",
	f"{vec(f"{A}{B}")}+{vec(f"{A}{D}")}=2{vec(f"{A}{I}")}",
	f"{vec(f"{A}{B}")}+{vec(f"{A}{D}")}=2{vec(f"{I}{C}")}",
	f"{vec(f"{C}{B}")}+{vec(f"{C}{D}")}=2{vec(f"{C}{I}")}",
	f"{vec(f"{C}{B}")}+{vec(f"{C}{D}")}=-2{vec(f"{I}{C}")}",
	f"{vec(f"{D}{A}")}+{vec(f"{D}{C}")}=-2{vec(f"{D}{I}")}",
	f"{vec(f"{B}{A}")}+{vec(f"{B}{C}")}=-2{vec(f"{B}{I}")}",
	f"{vec(f"{A}{B}")}+{vec(f"{A}{D}")}=2{vec(f"{A}{I}")}",
	f"{vec(f"{A}{B}")}+{vec(f"{A}{D}")}=2{vec(f"{I}{C}")}",
	 ])

	kq_false=[
	f"{vec(f"{A}{B}")}+{vec(f"{A}{D}")}={random.randint(3,5)}{vec(f"{A}{I}")}",
	f"{vec(f"{C}{A}")}+{vec(f"{C}{B}")}={vec(f"{C}{I}")}",
	f"{vec(f"{G}{C}")}=\\dfrac{{1}}{{3}}{vec(f"{G}{A}")}",
	f"{vec(f"{C}{I}")}=\\dfrac{{1}}{{3}}{vec(f"{C}{A}")}",
	f"{vec(f"{A}{C}")}=3{vec(f"{A}{G}")}",
	f"{vec(f"{B}{D}")}=2{vec(f"{D}{I}")}",
	f"{vec(f"{G}{A}")}=3{vec(f"{G}{I}")}",
	f"{vec(f"{I}{C}")}=-3{vec(f"{I}{G}")}",
	f"{vec(f"{A}{I}")}=-\\dfrac{{1}}{{2}}{vec(f"{C}{A}")}",
	f"{vec(f"{A}{B}")}+{vec(f"{B}{I}")}=-\\dfrac{{1}}{{2}}{vec(f"{B}{D}")}",
	f"{vec(f"{D}{C}")}+{vec(f"{I}{A}")}=-\\dfrac{{1}}{{2}}{vec(f"{D}{B}")}",
	f"{vec(f"{C}{D}")}+{vec(f"{C}{A}")}+{vec(f"{C}{B}")}=3{vec(f"{C}{A}")}",
	f"{vec(f"{C}{D}")}+{vec(f"{C}{B}")}=4{vec(f"{C}{I}")}",
	f"{vec(f"{C}{D}")}+{vec(f"{C}{B}")}=4{vec(f"{I}{A}")}",
	f"{vec(f"{B}{D}")}={random.randint(3,4)}{vec(f"{B}{I}")}",
	f"{vec(f"{A}{C}")}={random.randint(3,4)}{vec(f"{A}{I}")}",
	]
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]


	noi_dung_loigiai=(
	f"${kq}$ là khẳng định đúng"
	)

	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
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

#[D10_C5_B3_05]-TF-M3. Cho hình bình hành. Xét đúng sai các đẳng thức vectơ
def y7y7u_L10_C5_B3_05():
	danh_sach=["A","B","C","D"]
	random.shuffle(danh_sach)
	A,B,C,D=danh_sach
	I=random.choice(["O","I"])
	G=random.choice(["G","H","J"])
	M=random.choice(["M","N","P"])

	code_hinh=code_latex_hinhbinhhanh(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	noi_dung=(
	f"Cho hình bình hành ${{{A}{B}{C}{D}}}$ có tâm ${{{I}}}$, ${{{G}}}$ là trọng tâm của tam giác ${{{A}{B}{C}}}$."
	f" Gọi ${{{M}}}$ là trung điểm của cạnh ${{{A}{B}}}$. Xét tính đúng-sai của các khẳng định sau."
	)

	debai_word= f"{noi_dung}\n{file_name}\n"
	chon=random.randint(1,4)
	if chon==1:
		kq1_T=f"* ${vec(f"{G}{D}")}=-2{vec(f"{G}{B}")}$" 
		kq1_F=f"${vec(f"{G}{D}")}={random.choice([-3,3,2])}{vec(f"{G}{B}")}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${G}{B}=2{G}{I}\\Rightarrow {G}{D}=2{G}{B} \\Rightarrow {vec(f"{G}{D}")}=-2{vec(f"{G}{B}")}$."
	
	if chon==2:
		kq1_T=f"* ${vec(f"{B}{G}")}=\\dfrac{{2}}{{3}}{vec(f"{B}{I}")}$" 
		kq1_F=f"${vec(f"{B}{G}")}=-\\dfrac{{2}}{{3}}{vec(f"{B}{I}")}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${G}{C}=2{G}{I}\\Rightarrow {G}{A}=2{G}{C} \\Rightarrow {vec(f"{G}{A}")}=-2{vec(f"{G}{C}")}$."

	if chon==3:
		kq1_T=f"* ${vec(f"{D}{G}")}=4{vec(f"{I}{G}")}$" 
		kq1_F=f"${vec(f"{D}{G}")}={random.choice([-3,3,2,-4])}{vec(f"{I}{G}")}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"{D}{G}")}=4{vec(f"{I}{G}")}$."

	if chon==4:
		kq1_T=f"* ${vec(f"{B}{I}")}=\\dfrac{{3}}{{2}}{vec(f"{B}{G}")}$" 
		kq1_F=f"${vec(f"{B}{I}")}=\\dfrac{{2}}{{3}}{vec(f"{B}{G}")}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"{B}{I}")}=\\dfrac{{3}}{{2}}{vec(f"{B}{G}")}$."
	
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,4)
	if chon==1:
		kq2_T=f"* ${vec(f"{A}{B}")}+{vec(f"{A}{D}")}=2{vec(f"{A}{I}")}$"
		kq2_F=f" ${vec(f"{A}{B}")}+{vec(f"{A}{D}")}={random.randint(3,5)}{vec(f"{A}{I}")}$"		
		HDG=f"${vec(f"{A}{B}")}+{vec(f"{A}{D}")}=2{vec(f"{A}{I}")}$."

	if chon==2:
		kq2_T=f"* ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=2{vec(f"{B}{I}")}$"
		kq2_F=f" ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={random.randint(3,5)}{vec(f"{B}{I}")}$"		
		HDG=f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=2{vec(f"{B}{I}")}$."

	if chon==3:
		kq2_T=f"* ${vec(f"{C}{B}")}+{vec(f"{C}{D}")}=2{vec(f"{C}{I}")}$"
		kq2_F=f" ${vec(f"{C}{B}")}+{vec(f"{C}{D}")}={random.randint(3,5)}{vec(f"{C}{I}")}$"
		HDG=f"${vec(f"{C}{B}")}+{vec(f"{C}{D}")}=2{vec(f"{C}{I}")}$."

	if chon==4:
		kq2_T=f"* ${vec(f"{D}{A}")}+{vec(f"{D}{C}")}=2{vec(f"{D}{I}")}$"
		kq2_F=f" ${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={random.randint(3,5)}{vec(f"{D}{I}")}$"
		HDG=f"${vec(f"{D}{A}")}+{vec(f"{D}{C}")}=2{vec(f"{C}{I}")}$."

	kq2=random.choice([kq2_T, kq2_F])
	
	
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,4)
	if chon==1:
		kq3_T=f"* ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=3{vec(f"{B}{G}")}$" 
		kq3_F=f" ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={random.choice([2,4,-2,-3,-4])}{vec(f"{B}{G}")}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=3{vec(f"{B}{G}")}$."
	
	if chon==2:
		kq3_T=f"* ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=6{vec(f"{G}{I}")}$" 
		kq3_F=f" ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={random.choice([2,3,4,-2,-3,-4,-6])}{vec(f"{G}{I}")}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=6{vec(f"{G}{I}")}$."

	if chon==3:
		kq3_T=f"* ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=-6{vec(f"{I}{G}")}$" 
		kq3_F=f" ${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={random.choice([2,3,4,-2,-3,-4,6])}{vec(f"{G}{I}")}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}=-6{vec(f"{I}{G}")}$."

	if chon==4:
		kq3_T=f"* ${vec(f"{D}{A}")}+{vec(f"{D}{C}")}=6{vec(f"{I}{G}")}$" 
		kq3_F=f" ${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={random.choice([2,3,4,-2,-3,-4,-6])}{vec(f"{I}{G}")}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{D}{A}")}+{vec(f"{D}{C}")}=6{vec(f"{I}{G}")}$."
	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,5)
	if chon==1:
		kq4_T=f"* ${vec(f"{G}{A}")}=\\dfrac{{1}}{{3}}{vec(f"{B}{D}")}-\\dfrac{{2}}{{3}}{vec(f"{M}{C}")}$"
		kq4_F=f"${vec(f"{G}{A}")}=\\dfrac{{2}}{{3}}{vec(f"{B}{D}")}-\\dfrac{{1}}{{3}}{vec(f"{M}{C}")}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec(f"{G}{A}")}=-({vec(f"{G}{B}")}+{vec(f"{G}{C}")})"
			f"=-(-\\dfrac{{1}}{{3}}{vec(f"{B}{D}")}+\\dfrac{{2}}{{3}}{vec(f"{M}{C}")})"
			f"=\\dfrac{{1}}{{3}}{vec(f"{B}{D}")}-\\dfrac{{2}}{{3}}{vec(f"{M}{C}")}$."
			)
	
	if chon==2:
		kq4_T=f"* ${vec(f"{B}{I}")}=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{C}{G}")}$"
		kq4_F=f"${vec(f"{B}{I}")}=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}+\\dfrac{{1}}{{2}}{vec(f"{C}{G}")}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec(f"{B}{I}")}=3{vec(f"{G}{I}")}=3.\\dfrac{{1}}{{2}}({vec(f"{G}{A}")}+{vec(f"{G}{C}")})"
			f"=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{C}{G}")}$."
			)

	if chon==3:
		kq4_T=f"* ${vec(f"{I}{B}")}=-\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{G}{C}")}$"
		kq4_F=f"${vec(f"{I}{B}")}=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}+\\dfrac{{3}}{{2}}{vec(f"{G}{C}")}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec(f"{I}{B}")}=-3{vec(f"{G}{I}")}=-3.\\dfrac{{1}}{{2}}({vec(f"{G}{A}")}+{vec(f"{G}{C}")})"
			f"=-\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{G}{C}")}$."
			)

	if chon==4:
		kq4_T=f"* ${vec(f"{D}{I}")}=-\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{G}{C}")}$"
		kq4_F=f"${vec(f"{D}{I}")}=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}+\\dfrac{{3}}{{2}}{vec(f"{G}{C}")}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec(f"{D}{I}")}={vec(f"{I}{B}")}=-3{vec(f"{G}{I}")}=-3.\\dfrac{{1}}{{2}}({vec(f"{G}{A}")}+{vec(f"{G}{C}")})"
			f"=-\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{G}{C}")}$."
			)

	if chon==5:
		kq4_T=f"* ${vec(f"{I}{D}")}=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{C}{G}")}$"
		kq4_F=f"${vec(f"{I}{D}")}=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}+\\dfrac{{1}}{{2}}{vec(f"{C}{G}")}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec(f"{I}{D}")}={vec(f"{B}{I}")}=3{vec(f"{G}{I}")}=3.\\dfrac{{1}}{{2}}({vec(f"{G}{A}")}+{vec(f"{G}{C}")})"
			f"=\\dfrac{{3}}{{2}}{vec(f"{G}{A}")}-\\dfrac{{3}}{{2}}{vec(f"{C}{G}")}$."
			)
	

	
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#------------------------------------------------------------------------>

#Bài 4 - Tích vô hướng của 2 vectơ 
#[D10_C5_B4_01]. Cho hai véctơ có độ dài và góc. Tính tích vô hướng
def y7y7u_L10_C5_B4_01():
	ten_vta=random.choice(["a","m","u","c"])
	ten_vtb=random.choice(["b","n","v","d"])
	vt_a=f"\\overrightarrow{{{ten_vta}}}"
	vt_b=f"\\overrightarrow{{{ten_vtb}}}"
	dodai_a=random.randint(1,12)
	dodai_b=dodai_a+random.randint(5,10)
	goc=random.choice([30,45,60,90,120,135,150,180])
	
	tich_vh=dodai_a*dodai_b*my_module.hien_sin_cos(goc,"cos")

	kq=tich_vh
	kq2=dodai_a*dodai_b
	if goc!= 45:
		kq3=dodai_a*dodai_b*my_module.hien_sin_cos(goc,"sin")
	else:
		kq3=(dodai_a+dodai_b)*my_module.hien_sin_cos(goc,"cos")
	kq4=dodai_a+dodai_b*my_module.hien_sin_cos(goc,"cos")

	if my_module.check_so_nguyen(kq):
		kq=latex(my_module.hien_phan_so(kq))
	else:
		kq=latex(kq)

	if my_module.check_so_nguyen(kq2):
		kq2=latex(my_module.hien_phan_so(kq2))
	else:
		kq2=latex(kq2)

	if my_module.check_so_nguyen(kq3):
		kq3=latex(my_module.hien_phan_so(kq3))
	else:
		kq3=latex(kq3)

	if my_module.check_so_nguyen(kq4):
		kq4=latex(my_module.hien_phan_so(kq4))
	else:
		kq4=latex(kq4)

		#Tạo các phương án
	pa_A= f"*${{{vt_a}.{vt_b}={kq}}}$"
	pa_B= f"${{{vt_a}.{vt_b}={kq2}}}$"
	pa_C= f"${{{vt_a}.{vt_b}={kq3}}}$"
	pa_D= f"${{{vt_a}.{vt_b}={kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong hệ trục ${{Oxy}}$, cho hai véctơ ${vt_a}$ và ${vt_b}$ có $|{vt_a}|={dodai_a}$, $|{vt_b}|={dodai_b}$ và góc $({vt_a},{vt_b})={goc}^\\circ$. Tính tích vô hướng ${vt_a}.{vt_b}$."
	debai= f"{noi_dung} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	noi_dung_loigiai=f"${vt_a}.{vt_b}={kq}$.\n"\

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B4_02]. Cho hai véctơ có độ dài và tích vô hướng. Tìm góc
def y7y7u_L10_C5_B4_02():
	ten_vta=random.choice(["a","m","u","c"])
	ten_vtb=random.choice(["b","n","v","d"])
	vt_a=f"\\overrightarrow{{{ten_vta}}}"
	vt_b=f"\\overrightarrow{{{ten_vtb}}}"

	dodai_a=random.randint(1,12)
	dodai_b=dodai_a+random.randint(5,10)
	list_goc=[30,45,60,90,120,135,150,180]
	goc=random.choice(list_goc)	
	tich_vh=latex(dodai_a*dodai_b*my_module.hien_sin_cos(goc,"cos"))

	kq=goc
	goc_khac=[i for i in list_goc if i != goc]
	kq2=goc_khac[0]
	kq3=goc_khac[1]
	kq4=goc_khac[2]

	#Tạo các phương án
	pa_A= f"*${{{kq}}}^\\circ$"
	pa_B= f"${{{kq2}}}^\\circ$"
	pa_C= f"${{{kq3}}}^\\circ$"
	pa_D= f"${{{kq4}}}^\\circ$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho hai véctơ ${vt_a}$ và ${vt_b}$ có $|{vt_a}|={dodai_a}$, $|{vt_b}|={dodai_b}$ và ${vt_a}.{vt_b}={tich_vh}$. Tìm góc ${{({vt_a},{vt_b})}}$."
	debai= f"{noi_dung} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	noi_dung_loigiai=f""

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B4_03]. Cho hai véctơ có độ dài và góc. Tính |vta+vtb|
def y7y7u_L10_C5_B4_03():
	ten_vta=random.choice(["a","m","u","c"])
	ten_vtb=random.choice(["b","n","v","d"])
	vt_a=f"\\overrightarrow{{{ten_vta}}}"
	vt_b=f"\\overrightarrow{{{ten_vtb}}}"

	dodai_a=random.randint(1,8)
	dodai_b=dodai_a+random.randint(5,10)
	goc=random.choice([0,60,120,90,180])
	
	tich_vh=dodai_a*dodai_b*my_module.hien_sin_cos(goc,"cos")
	
	kq=sqrt(dodai_a**2 + dodai_b**2 + 2*tich_vh)

	kq2=sqrt(dodai_a**2+dodai_b**2 + 2*dodai_a*dodai_b*my_module.hien_sin_cos(goc,"sin"))

	kq3=dodai_a+dodai_b

	kq4=sqrt(dodai_a+dodai_b)

	if goc==0:
		kq2=dodai_a+dodai_b+random.randint(11,20)
	if goc==60:
		kq=sqrt(dodai_a**2 + dodai_b**2+dodai_a*dodai_b)
		kq2=sqrt(dodai_a**2 + dodai_b**2-dodai_a*dodai_b)
	if goc==120:
		kq=sqrt(dodai_a**2 + dodai_b**2 - dodai_a*dodai_b)
		kq2=sqrt(dodai_a**2 + dodai_b**2 + dodai_a*dodai_b)
	
	
	if goc==90:
		kq3=dodai_a+dodai_b+random.randint(1,10)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]	

	kq=latex(my_module.rutgon_can(kq))
	kq2=latex(kq2)
	kq3=latex(kq3)
	kq4=latex(kq4)

		#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_a}$ và ${vt_b}$ có $|{vt_a}|={dodai_a}$, $|{vt_b}|={dodai_b}$ và góc $({vt_a},{vt_b})={goc}^\\circ$. Tính $|{vt_a}+{vt_b}|$."
	debai= f"{noi_dung} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	noi_dung_loigiai=f""

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C5_B4_04]. Cho hai véctơ có độ dài và góc. Tính |vta-vtb|
def y7y7u_L10_C5_B4_04():
	ten_vta=random.choice(["a","m","u","c"])
	ten_vtb=random.choice(["b","n","v","d"])
	vt_a=f"\\overrightarrow{{{ten_vta}}}"
	vt_b=f"\\overrightarrow{{{ten_vtb}}}"

	dodai_a=random.randint(1,8)
	dodai_b=dodai_a+random.randint(5,10)
	goc=random.choice([0,60,120,90,180])	
	tich_vh=dodai_a*dodai_b*my_module.hien_sin_cos(goc,"cos")
	t=dodai_a**2 + dodai_b**2 - 2*tich_vh
	while t<0:
		dodai_a=random.randint(1,8)
		dodai_b=dodai_a+random.randint(5,10)
		goc=random.choice([0,60,120,90,180])	
		tich_vh=dodai_a*dodai_b*my_module.hien_sin_cos(goc,"cos")
		t=dodai_a**2 + dodai_b**2 - 2*tich_vh

	kq=sqrt(dodai_a**2 + dodai_b**2 - 2*tich_vh)

	kq2=sqrt(dodai_a**2+dodai_b**2 - 2*dodai_a*dodai_b*my_module.hien_sin_cos(goc,"sin"))

	kq3=abs(dodai_a-dodai_b)

	kq4=sqrt(abs(dodai_a**2-dodai_b**2))

	if goc==0:
		kq2=abs(dodai_a-dodai_b)+random.randint(11,20)
	if goc==60:
		kq=sqrt(dodai_a**2 + dodai_b**2-dodai_a*dodai_b)
		kq2=sqrt(dodai_a**2 + dodai_b**2+dodai_a*dodai_b)
	if goc==120:
		kq=sqrt(dodai_a**2 + dodai_b**2 + dodai_a*dodai_b)
		kq2=sqrt(dodai_a**2 + dodai_b**2 - dodai_a*dodai_b)
		
	if goc==90:
		kq3=abs(dodai_a-dodai_b)+random.randint(1,10)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]	

	kq=latex(my_module.rutgon_can(kq))
	kq2=latex(kq2)
	kq3=latex(kq3)
	kq4=latex(kq4)

		#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_a}$ và ${vt_b}$ có $|{vt_a}|={dodai_a}$, $|{vt_b}|={dodai_b}$ và góc $({vt_a},{vt_b})={goc}^\\circ$. Tính $|{vt_a}-{vt_b}|$."
	debai= f"{noi_dung} \n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	noi_dung_loigiai=f""

	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C5_B4_05]-TF-M2. Cho hình vuông. Xét Đ-S: các phép toán về vectơ, tích vô hướng
def y7y7u_L10_C5_B4_05():

	A=["A","O","A","O"]
	B=["B","A","B","B"]
	C=["C","B","E","C"]
	D=["D","C","F","D"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	ten_tudien=f"{A}{B}{C}{D}"
	G=random.choice(["G","H"])
	M=["M","N","P"]
	i=random.randint(0,1)
	M= M[i]


	m=random.randint(1,7)
	a=sp.symbols("a")

	noi_dung = (f"Cho hình vuông ${{{ten_tudien}}}$ có cạnh bằng ${{{latex(m*a)}}}$. Gọi ${{{M}}}$ là trung điểm của cạnh ${{{B}{C}}}$."
	f" Gọi ${{{G}}}$ là trọng tâm tam giác ${{{B}{C}{D}}}$. Xét tính đúng-sai của các khẳng định sau.")

	kq1_T=f"*${vec(f"{A}{B}")}+{vec(f"{C}{D}")}+{vec(f"{B}{C}")}+{vec(f"{D}{A}")}={vec(f"0")}$" 
	kq1_F=f"${vec(f"{A}{B}")}+{vec(f"{C}{D}")}+{vec(f"{B}{C}")}+{vec(f"{D}{A}")}={random.choice(["",2,3,4])}{random.choice([vec(f"{A}{C}"),vec(f"{B}{D}"), vec(f"{C}{A}")])}$ "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"${vec(f"{A}{B}")}+{vec(f"{C}{D}")}+{vec(f"{B}{C}")}+{vec(f"{D}{A}")}={vec(f"{A}{B}")}+{vec(f"{B}{C}")}+{vec(f"{C}{D}")}+{vec(f"{D}{A}")}={vec(f"{A}{A}")}={vec(f"0")}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,3)
	
	if chon==1:
		kq2_T=f"*${vec(f"{A}{B}")}.{vec(f"{A}{C}")}={latex(m**2*a**2)}$"
		kq2_F=f"${vec(f"{A}{B}")}.{vec(f"{A}{C}")}={random.choice([latex(-m**2*a**2*1/2),latex(m**2*a**2*sqrt(2)/2),0])}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{A}{B}")}.{vec(f"{A}{C}")}={A}{B}.{A}{C}.\\cos({vec(f"{A}{B}")}, {vec(f"{A}{C}")})$"
			f"$={latex(m*a)}.{latex(m*a*sqrt(2))}.({latex(sqrt(2)/2)})={latex(m**2*a**2)}$."
			)
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq3_T=f"*${vec(f"{B}{C}")}.{vec(f"{A}{D}")}=0$" 
		kq3_F=f"${vec(f"{B}{C}")}.{vec(f"{A}{D}")}={latex(random.randint(1,4)*m*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${B}{C}\\bot {A}{M}, {B}{C}\\bot {D}{M} \\Rightarrow  {B}{C}\\bot ({A}{D}{M}) \\Rightarrow {B}{C}\\bot {A}{D}$.\n\n"\
		f"Vậy ${vec(f"{B}{C}")}.{vec(f"{A}{D}")}=0$. "
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:

		kq2_T=f"*${vec(f"{B}{A}")}.{vec(f"{C}{A}")}={latex(m**2*a**2)}$"
		kq2_F=f"${vec(f"{B}{A}")}.{vec(f"{C}{A}")}={random.choice([latex(-m**2*a**2*1/2),latex(m**2*a**2*sqrt(2)/2),0])}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{B}{A}")}.{vec(f"{C}{A}")}={B}{A}.{C}{A}.\\cos({vec(f"{B}{A}")}, {vec(f"{C}{A}")})$"
			f"$={latex(m*a)}.{latex(m*a*sqrt(2))}.{latex(sqrt(2)/2)}={latex(m**2*a**2)}$."
			)
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq3_T=f"*${vec(f"{A}{C}")}.{vec(f"{B}{D}")}=0$" 
		kq3_F=f"${vec(f"{A}{C}")}.{vec(f"{B}{D}")}={latex(random.randint(1,4)*m*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${A}{C}\\bot {B}{D}\\Rightarrow {vec(f"{A}{C}")}.{vec(f"{B}{D}")}=0$."

		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:

		kq2_T=f"*${vec(f"{A}{B}")}.{vec(f"{C}{A}")}={latex(-m**2*a**2)}$"
		kq2_F=f"${vec(f"{A}{B}")}.{vec(f"{C}{A}")}={random.choice([latex(m**2*a**2),latex(m**2*a**2*sqrt(2)),0])}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{A}{B}")}.{vec(f"{C}{A}")}={A}{B}.{C}{A}.\\cos({vec(f"{A}{B}")}, {vec(f"{C}{A}")})$"
			f"$={latex(m*a)}.{latex(m*a*sqrt(2))}.{latex(-sqrt(2)/2)}={latex(-m**2*a**2)}$."
			)
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq3_T=f"*${vec(f"{A}{B}")}.{vec(f"{C}{D}")}={latex(-m**2*a**2)}$" 
		kq3_F=f"${vec(f"{A}{B}")}.{vec(f"{C}{D}")}={latex(random.randint(1,4)*m*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vec(f"{A}{B}")}.{vec(f"{C}{D}")}={latex(m*a)}.{latex(m*a)}.\\cos 180^\\circ={latex(-m**2*a**2)}$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	
	chon=random.randint(1,2)	
	if chon==1:
		kq4_T=f"*$({vec(f"{G}{B}")},{vec(f"{D}{G}")}) = 45^\\circ$"
		kq4_F=f"$({vec(f"{G}{B}")},{vec(f"{D}{G}")}) = {random.choice([30,90,120,135,150])}^\\circ$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$({vec(f"{G}{B}")},{vec(f"{D}{G}")})=180^\\circ-({vec(f"{G}{B}")},{vec(f"{G}{D}")})=180^\\circ - 135^\\circ=45^\\circ$"
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==2:
		kq4_T=f"*$({vec(f"{G}{B}")},{vec(f"{G}{D}")}) = 135^\\circ$"
		kq4_F=f"$({vec(f"{G}{B}")},{vec(f"{G}{D}")}) = {random.choice([45,30,90,60,120,150])}^\\circ$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$({vec(f"{G}{B}")},{vec(f"{G}{D}")})=\\widehat{{{B}{G}{C}}}=180^\\circ-\\widehat{{{G}{B}{D}}}-\\widehat{{{G}{D}{B}}}=135^\\circ$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	
	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_C5_B4_06]-TF-M2. Cho tam giác. Xét Đ-S: Tích vô hướng, phép toán vectơ,  độ dài.
def y7y7u_L10_C5_B4_06():
	A=["A","S","S","D"]
	B=["B","A","B","A"]
	C=["C","B","C","B"]
	D=["D","C","D","C"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	ten_tudien=f"{A}{B}{C}{D}"

	G=random.choice(["G","H"])
	M=["M","E"]
	N=["N","F"]
	i=random.randint(0,1)
	M, N = M[i], N[i]
	I= random.choice(["I","K"])
	P= random.choice(["P","Q"])
	

	AB=random.randint(1,7)
	a=random.randint(1,6)

	noi_dung = (f"Cho tam giác ${{{B}{C}{D}}}$ đều có cạnh bằng ${{{a}}}$. Gọi ${{{A}}}$ là điểm tùy ý."
	f" Gọi ${{{G}}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$, điểm ${{{M}}}$ là trung điểm của ${{{C}{D}}}$."
	f" Xét tính đúng-sai của các khẳng định sau.")
	chon=random.randint(1,3)
		
	if chon==1:
		vecto_1=[f"{vec(f"{B}{C}")}", f"{vec(f"{B}{C}")}", f"{vec(f"{C}{D}")}", f"{vec(f"{C}{D}")}", f"{vec(f"{C}{G}")}"]
		vecto_2=[f"{vec(f"{G}{D}")}", f"{vec(f"{D}{G}")}", f"{vec(f"{B}{M}")}", f"{vec(f"{G}{M}")}", f"{vec(f"{B}{D}")}"]

		i=random.randint(0,4)		
		vecto_1,vecto_2=vecto_1[i],vecto_2[i]

		kq1_T=f"*${vecto_1}.{vecto_2}=0$" 
		kq1_F=f"${vecto_1}.{vecto_2}={random.choice([random.randint(1,5),random.randint(-5,-1) ])}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vecto_1}.{vecto_2}=0$ vì ${vecto_1} \\bot {vecto_2}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==2:
		vecto_1=[f"{vec(f"{B}{C}")}", f"{vec(f"{C}{B}")}", f"{vec(f"{D}{C}")}" ]
		vecto_2=[f"{vec(f"{B}{D}")}", f"{vec(f"{C}{D}")}", f"{vec(f"{D}{B}")}" ]

		i=random.randint(0,2)
		vecto_1, vecto_2 = vecto_1[i], vecto_2[i]

		kq1_T=f"*${vecto_1}.{vecto_2}={phan_so(a**2/2)}$" 
		kq1_F=f"${vecto_1}.{vecto_2}={phan_so(-a**2/2)}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vecto_1}.{vecto_2}={a}.{a}.\\cos ({vecto_1},{vecto_2})={a**2}.\\cos 60^\\circ={phan_so(a**2/2)}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		vecto_1=[f"{vec(f"{B}{C}")}", f"{vec(f"{C}{B}")}", f"{vec(f"{D}{C}")}", f"{vec(f"{C}{D}")}" , f"{vec(f"{B}{C}")}"]
		vecto_2=[f"{vec(f"{D}{B}")}", f"{vec(f"{D}{C}")}", f"{vec(f"{B}{D}")}", f"{vec(f"{B}{C}")}" , f"{vec(f"{C}{D}")}"]

		i=random.randint(0,3)
		vecto_1, vecto_2 = vecto_1[i], vecto_2[i]

		kq1_T=f"*${vecto_1}.{vecto_2}={phan_so(-a**2/2)}$" 
		kq1_F=f"${vecto_1}.{vecto_2}={phan_so(a**2/2)}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vecto_1}.{vecto_2}={a}.{a}.\\cos ({vecto_1},{vecto_2})={a**2}.\\cos 120^\\circ={phan_so(-a**2/2)}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,3)
	
	if chon==1:
		kq2_T=f"*${vec(f"{B}{G}")}+2{vec(f"{M}{G}")}={vec("0")}$"
		kq2_F=f"${vec(f"{B}{G}")}+2{vec(f"{M}{G}")}={vec(f"{M}{B}")}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{B}{G}")}=-2{vec(f"{M}{G}")} \\Rightarrow {vec(f"{B}{G}")}+2{vec(f"{M}{G}")}={vec("0")}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	

	if chon==2:
		kq2_T=f"*${vec(f"{A}{B}")}+{vec(f"{A}{C}")}+{vec(f"{A}{D}")}=3{vec(f"{A}{G}")}$"
		kq2_F=f"${vec(f"{A}{B}")}+{vec(f"{A}{C}")}+{vec(f"{A}{D}")}={vec(f"{A}{G}")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Ta có: ${vec(f"{G}{B}")}+{vec(f"{G}{C}")}+{vec(f"{G}{D}")}={vec(f"0")}$.\n\n"\
		f"${vec(f"{A}{B}")}+{vec(f"{A}{C}")}+{vec(f"{A}{D}")}=3{vec(f"{A}{G}")}+{vec(f"{G}{B}")}+{vec(f"{G}{C}")}+{vec(f"{G}{D}")}=3{vec(f"{A}{G}")}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		kq2_T=f"*${vec(f"{G}{C}")}+{vec(f"{G}{D}")}={vec(f"{B}{G}")}$"
		kq2_F=f"${vec(f"{G}{C}")}+{vec(f"{G}{D}")}={vec(f"{G}{B}")}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{G}{C}")}+{vec(f"{G}{D}")}=2{vec(f"{G}{M}")}={vec(f"{B}{G}")}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	

	kq3_T=f"*$|{vec(f"{B}{C}")}+{vec(f"{B}{D}")}|={latex(a*sqrt(3))}$" 
	kq3_F=f"$|{vec(f"{B}{C}")}+{vec(f"{B}{D}")}|={latex(a*sqrt(3)/2)}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$|{vec(f"{B}{C}")}+{vec(f"{B}{D}")}|=|2{vec(f"{B}{M}")}|=2.{latex(a*sqrt(3)/2)}={latex(a*sqrt(3))}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,5)
	if chon==1:
		ten=random.choice([f"{vec(f"{M}{C}")}",f"{vec(f"{D}{M}")}"])
	
		kq4_T=f"*$|{vec(f"{B}{D}")}+{ten}|={latex(a*sqrt(3)/2)}$"
		kq4_F=f"$|{vec(f"{B}{D}")}+{ten}|={latex(random.randint(1,3)*a)}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$|{vec(f"{B}{D}")}+{ten}|=|{vec(f"{B}{D}")}+{vec(f"{D}{M}")}|=|{vec(f"{B}{M}")}|=\\sqrt{{{a}^2+\\left({phan_so(a/2)}\\right)^2}}={latex(a*sqrt(3))}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:	
	
		kq4_T=f"*$|{vec(f"{G}{C}")}+{vec(f"{G}{D}")}|={latex(a*sqrt(3)/3)}$"
		kq4_F=f"$|{vec(f"{G}{C}")}+{vec(f"{G}{D}")}|={latex(random.choice([a*sqrt(3)/2, a*sqrt(3)/4, a/2, a/4]))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$|{vec(f"{G}{C}")}+{vec(f"{G}{D}")}|=|2{vec(f"{G}{M}")}|=|{vec(f"{B}{G}")}|={phan_so(2/3)}.{latex(a*sqrt(3)/2)}={latex(a*sqrt(3)/3)}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:	
	
		kq4_T=f"*$|{vec(f"{G}{B}")}+{vec(f"{G}{C}")}|={latex(a*sqrt(3)/3)}$"
		kq4_F=f"$|{vec(f"{G}{B}")}+{vec(f"{G}{C}")}|={latex(random.choice([a*sqrt(3)/2, a*sqrt(3)/4, a/2, a/4]))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$|{vec(f"{G}{B}")}+{vec(f"{G}{C}")}|=|{vec(f"{D}{G}")}|={phan_so(2/3)}.{latex(a*sqrt(3)/2)}={latex(a*sqrt(3)/3)}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==4:		
		kq4_T=f"*$|{vec(f"{G}{B}")}+{vec(f"{G}{D}")}|={latex(a*sqrt(3)/3)}$"
		kq4_F=f"$|{vec(f"{G}{B}")}+{vec(f"{G}{D}")}|={latex(random.choice([a*sqrt(3)/2, a*sqrt(3)/4, a/2, a/4]))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$|{vec(f"{G}{B}")}+{vec(f"{G}{D}")}|=|{vec(f"{C}{G}")}|={phan_so(2/3)}.{latex(a*sqrt(3)/2)}={latex(a*sqrt(3)/3)}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==5:		
		kq4_T=f"*$|{vec(f"{M}{B}")}+{vec(f"{G}{A}")}+{vec(f"{G}{M}")}-{vec(f"{D}{A}")}|={latex(a*sqrt(3)/3)}$"
		kq4_F=f"$|{vec(f"{M}{B}")}+{vec(f"{G}{A}")}+{vec(f"{G}{M}")}-{vec(f"{D}{A}")}|={latex(random.choice([a*sqrt(3)/2, a*sqrt(3)/4, a/2, a/4]))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"$|{vec(f"{M}{B}")}+{vec(f"{G}{A}")}+{vec(f"{G}{M}")}-{vec(f"{D}{A}")}|$"
			f"$=|{vec(f"{G}{M}")}+{vec(f"{M}{B}")}+{vec(f"{G}{A}")}+{vec(f"{A}{D}")}|$"
			f"$=|{vec(f"{G}{B}")}+{vec(f"{G}{D}")}|=|{vec(f"{C}{G}")}|={phan_so(2/3)}.{latex(a*sqrt(3)/2)}={latex(a*sqrt(3)/3)}$.")
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

#[D10_C5_B4_07]-TL-M2. Cho hai vectơ a,b có độ dài và tích vô hướng. Tính |ma+nb|.
def y7y7u_L10_C5_B4_07():
	a=random.randint(1,5)
	b=random.randint(1,5)
	cos=random.choice([1,-1,1/2,-1/2, 1/4,3/4,-1/4,-3/4])
	tich_vh=a*b*cos	

	m=random.randint(1,5)
	n=random.choice([i for i in range(-5, 5) if i!=0])

	ten_a=random.choice(["a","m","u"])
	ten_b=random.choice(["b","n","v"])

	vec_a=f"{vec(f"{ten_a}")}"
	vec_b=f"{vec(f"{ten_b}")}"
	noi_dung=(f"Cho hai vectơ ${vec_a}$ và ${vec_b}$ thỏa mãn $|{vec_a}|={a},|{vec_b}|={b}$ và ${vec_a}.{vec_b}={tich_vh}$."
	f" Tính $|{m}{vec_a}+{n}{vec_b}|$(kết quả làm tròn đến hàng phần mười)."
	)
	noi_dung=noi_dung.replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")

	kq=sqrt((m*a)**2+2*m*n*tich_vh+(n*b)**2)
	dap_an=f"{round(kq,1):.1f}".replace(".",",")

	if tich_vh>0:
		noi_dung_loigiai=(
		f"$|{m}{vec_a}+{n}{vec_b}|^2=({m}{vec_a}+{n}{vec_b})^2={m**2}{vec_a}^2+{2*m*n}{vec_a}{vec_b}+{n**2}{vec_b}$\n\n"
		f"$={m**2}.{a}^2+{2*m*n}.{tich_vh}+{n**2}.{b}^2={(m*a)**2+2*m*n*tich_vh+(n*b)**2}$.\n\n"
		f"Suy ra $|{m}{vec_a}+{n}{vec_b}|={round(kq,1):.1f}$.")
	else:
		noi_dung_loigiai=(
		f"$|{m}{vec_a}+{n}{vec_b}|^2=({m}{vec_a}+{n}{vec_b})^2={m**2}{vec_a}^2+{2*m*n}{vec_a}{vec_b}+{n**2}{vec_b}$\n\n"
		f"$={m**2}.{a}^2+{2*m*n}.({tich_vh})+{n**2}.{b}^2={(m*a)**2+2*m*n*tich_vh+(n*b)**2}$.\n\n"
		f"Suy ra $|{m}{vec_a}+{n}{vec_b}|={round(kq,1):.1f}$.")

	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")

			
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C5_B4_08]-TL-M3. Cho hai vectơ a,b và độ dài |ma+nb|. Tính cos(a,b)
def y7y7u_L10_C5_B4_08():
	a=random.randint(1,5)
	b=random.randint(1,5)

	cos=random.choice([1,-1,1/2,-1/2, 1/4,3/4,-1/4,-3/4])
	tich_vh=a*b*cos

	m=random.choice([i for i in range(-5, 5) if i!=0])
	n=random.choice([i for i in range(-5, 5) if i!=0])

	ten_a=["a","m","u"]
	ten_b=["b","n","v"]
	i=random.randint(0,2)
	ten_a, ten_b=ten_a[i], ten_b[i]

	vec_a=f"{vec(f"{ten_a}")}"
	vec_b=f"{vec(f"{ten_b}")}"
	modun=sqrt((m*a)**2+2*m*n*tich_vh+(n*b)**2)	

	kq=f"{round(tich_vh/(a*b),1)}".replace(".",",")
	noi_dung=(f"Cho hai vectơ ${vec_a}$ và ${vec_b}$ thỏa mãn $|{vec_a}|={a},|{vec_b}|={b}$ và $|{m}{vec_a}+{n}{vec_b}|={latex(nsimplify(modun))}$."
	f" Tính $\\cos({vec_a},{vec_b})$ (kết quả làm tròn đến hàng phần mười)."
	)
	noi_dung=noi_dung.replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")

	
	noi_dung_loigiai=(
		f"$|{m}{vec_a}+{n}{vec_b}|^2=({m}{vec_a}+{n}{vec_b})^2={m**2}{vec_a}^2+{2*m*n}{vec_a}{vec_b}+{n**2}{vec_b}$\n\n"
		f"$={m**2}.{a}^2+{2*m*n}.{vec_a}{vec_b}+{n**2}.{b}^2={(m*a)**2+(n*b)**2}+{2*m*n}.{vec_a}{vec_b}$.\n\n"
		f"Ta có: $|{m}{vec_a}+{n}{vec_b}|^2={modun**2}\\Rightarrow {(m*a)**2+(n*b)**2}+{2*m*n}.{vec_a}{vec_b}={modun**2}$.\n\n"
		f"$\\Rightarrow {vec_a}.{vec_b}={tich_vh}$.\n\n"
		f"$\\cos({vec_a},{vec_b})=\\dfrac{{{vec_a}.{vec_b}}}{{|{vec_a}|.|{vec_b}|}}=\\dfrac{{{tich_vh}}}{{{a}.{b}}}={phan_so(tich_vh/(a*b))}$.\n\n"
		f"Đáp án: {kq}"
		)
	
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}\n"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word,loigiai_word,latex_tuluan,dap_an


#[D10_C5_B4_09]-TL-M3. Cho hai vectơ a,b có |a|, |b|, ab. Đặt x=ma+nb, y=pa+qb. Tính cos(x,y)
def y7y7u_L10_C5_B4_09():
	a=random.randint(1,5)
	b=random.randint(1,5)
	cos=random.choice([1,-1,1/2,-1/2, 1/4,3/4,-1/4,-3/4])
	tich_vh=int(a*b*cos)

	m=random.choice([i for i in range(-3, 3) if i!=0])
	n=random.choice([i for i in range(-3, 3) if i!=0])

	p=random.choice([i for i in range(-3, 3) if i!=0])
	q=random.choice([i for i in range(-3, 3) if i!=0])
	xy=m*p*a**2+n*q*b**2+(m*q+n*p)*tich_vh
	kq=xy/(sqrt((m*a)**2+(n*b)**2+(2*m*n*tich_vh))*sqrt((p*a)**2+(q*b)**2+(2*p*q*tich_vh)))
	while math.isnan(kq):
		a=random.randint(1,5)
		b=random.randint(1,5)
		cos=random.choice([1,-1,1/2,-1/2, 1/4,3/4,-1/4,-3/4])	

		m=random.choice([i for i in range(-3, 3) if i!=0])
		n=random.choice([i for i in range(-3, 3) if i!=0])

		p=random.choice([i for i in range(-3, 3) if i!=0])
		q=random.choice([i for i in range(-3, 3) if i!=0])		

	ten_a=["a","m","u"]
	ten_b=["b","n","v"]
	i=random.randint(0,2)
	ten_a, ten_b=ten_a[i], ten_b[i]

	vec_a=f"{vec(f"{ten_a}")}"
	vec_b=f"{vec(f"{ten_b}")}"
	vec_x=f"{vec("x")}"
	vec_y=f"{vec("y")}"
	modun=sqrt((m*a)**2+2*m*n*tich_vh+(n*b)**2)	

	kq=f"{round(tich_vh/(a*b),1)}".replace(".",",")
	noi_dung=(f"Cho hai vectơ ${vec_a}$ và ${vec_b}$ thỏa mãn $|{vec_a}|={a},|{vec_b}|={b}$ và ${vec_a}.{vec_b}={tich_vh}$."
	f" Xét hai vectơ ${vec_x}={m}{vec_a}+{n}{vec_b}$ và ${vec_y}={p}{vec_a}+{q}{vec_b}$. Tính $\\cos({vec_x},{vec_y})$ (kết quả làm tròn đến hàng phần mười)."
	)
	noi_dung=noi_dung.replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")

	
	modun_x=f"{latex(sqrt((m*a)**2+(n*b)**2+(2*m*n*tich_vh)))}"
	modun_y=f"{latex(sqrt((p*a)**2+(q*b)**2+(2*p*q*tich_vh)))}"
	kq=xy/(sqrt((m*a)**2+(n*b)**2+(2*m*n*tich_vh))*sqrt((p*a)**2+(q*b)**2+(2*p*q*tich_vh)))
	kq=f"{round(kq,1)}".replace(".",",")
	if tich_vh>0:
		noi_dung_loigiai=(
			f"${vec_x}.{vec_y}=({m}{vec_a}+{n}{vec_b}).({p}{vec_a}+{q}{vec_b})={m*p}{vec_a}^2+{n*q}{vec_b}^2+{m*q+n*p}{vec_a}.{vec_b}"
			f"={m*p}.{a}^2+{n*q}.{b}^2++{m*q+n*p}.{tich_vh}"
			f"={m*p*a**2+n*q*b**2+(m*q+n*p)*tich_vh}$.\n\n"

			f"$|{vec_x}|=\\sqrt{{{vec_x}^2}}=\\sqrt{{({m}{vec_a}+{n}{vec_b})^2}}=\\sqrt{{{m**2}{vec_a}^2+{n**2}{vec_b}^2+{2*m*n}.{vec_a}.{vec_b}}}"
			f"=\\sqrt{{{m**2}.{a}^2+{n**2}.{b}^2+{2*m*n}.{tich_vh}}}"
			f"={latex(sqrt((m*a)**2+(n*b)**2+(2*m*n*tich_vh)))}$.\n\n"

			f"$|{vec_y}|=\\sqrt{{{vec_y}^2}}=\\sqrt{{({p}{vec_a}+{q}{vec_b})^2}}=\\sqrt{{{p**2}{vec_a}^2+{q**2}{vec_b}^2+{2*p*q}.{vec_a}.{vec_b}}}"
			f"=\\sqrt{{{p**2}.{a}^2+{q**2}.{b}^2+{2*p*q}.{tich_vh}}}"
			f"={latex(sqrt((p*a)**2+(q*b)**2+(2*p*q*tich_vh)))}$.\n\n"

			f"$\\cos({vec_x},{vec_y})=\\dfrac{{{vec_x}.{vec_y}}}{{|{vec_x}|.|{vec_y}|}}=\\dfrac{{{xy}}}{{{modun_x}.{modun_y}}}\\approx {kq}$\n\n"

			f"Đáp án: {kq}"
			)
	else:
		noi_dung_loigiai=(
			f"${vec_x}.{vec_y}=({m}{vec_a}+{n}{vec_b}).({p}{vec_a}+{q}{vec_b})={m*p}{vec_a}^2+{n*q}{vec_b}^2+{m*q+n*p}{vec_a}.{vec_b}"
			f"={m*p}.{a}^2+{n*q}.{b}^2++{m*q+n*p}.({tich_vh})"
			f"={m*p*a**2+n*q*b**2+(m*q+n*p)*tich_vh}$.\n\n"

			f"$|{vec_x}|=\\sqrt{{{vec_x}^2}}=\\sqrt{{({m}{vec_a}+{n}{vec_b})^2}}=\\sqrt{{{m**2}{vec_a}^2+{n**2}{vec_b}^2+{2*m*n}.{vec_a}.{vec_b}}}"
			f"=\\sqrt{{{m**2}.{a}^2+{n**2}.{b}^2+{2*m*n}.({tich_vh})}}"
			f"={latex(sqrt((m*a)**2+(n*b)**2+(2*m*n*tich_vh)))}$.\n\n"

			f"$|{vec_y}|=\\sqrt{{{vec_y}^2}}=\\sqrt{{({p}{vec_a}+{q}{vec_b})^2}}=\\sqrt{{{p**2}{vec_a}^2+{q**2}{vec_b}^2+{2*p*q}.{vec_a}.{vec_b}}}"
			f"=\\sqrt{{{p**2}.{a}^2+{q**2}.{b}^2+{2*p*q}.({tich_vh})}}"
			f"={latex(sqrt((p*a)**2+(q*b)**2+(2*p*q*tich_vh)))}$.\n\n"

			f"$\\cos({vec_x},{vec_y})=\\dfrac{{{vec_x}.{vec_y}}}{{|{vec_x}|.|{vec_y}|}}=\\dfrac{{{xy}}}{{{modun_x}.{modun_y}}}\\approx {kq}$\n\n"

			f"Đáp án: {kq}"
			)

	
	noi_dung_loigiai=noi_dung_loigiai.replace("++","+").replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=(f"\\begin{{ex}}\n {noi_dung}\n"
	f"\\shortans[oly]{{{kq}}}\n\n"
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}\n"
	f"\\end{{ex}}\n")

	dap_an=kq

	return debai_word,loigiai_word,latex_tuluan,dap_an


	