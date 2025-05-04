import math
import random
from fractions import Fraction
import my_module
import sympy as sp
from sympy import *
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

def thay_hinh_hoc(st):
	ketqua=st.replace("1I","I").replace("1E","E").replace("1M","M")
	ketqua=ketqua.replace("=1a","=a")
	return ketqua

#Hàm rút gọn căn thức
def rutgon_can(x):
	from sympy import nsimplify
	if x.is_number:
	    ns = nsimplify(x)
	    if ns != x and x.equals(ns):
	        return ns
	return x

#Trả về dạng phân số 
def phan_so(t):
	m=latex(Rational(t).limit_denominator(100000000000))
	return m

def return_number_vn(a):
	try:
		if a==int(a):
			t=int(a)
		else:
			t=str(round(a,2))
			t=t.replace(".",",")
	except Exception as e:
		t=a
	return t
def codelatex_hinhchop_tamgiac_canhvg(s,a,b,c):
    code=f"\\begin{{tikzpicture}}\n\
\\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}};\n\
\\coordinate ({b}) at (1,-2) node at ({b}) [left] {{${b}$}};\n\
\\coordinate ({c}) at (4,0)   node at ({c}) [right] {{${c}$}};\n\
\\coordinate ({s}) at (0,4)   node at ({s}) [above] {{${s}$}};\n\
\\draw [dashed] ({a})--({c}) ; \n\
\\draw ({a})--({b}) ({b})--({c}) ({s})--({a}) ({s})--({b}) ({s})--({c}); \n\
\\end{{tikzpicture}}\n"
    return code

def codelatex_hinhchop_hbh_canhvg(s,a,b,c,d):
    code=f"\\begin{{tikzpicture}}[scale=0.6]\n\
\\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}};\n\
\\coordinate ({b}) at (-1,-1) node at ({b}) [left] {{${b}$}};\n\
\\coordinate ({c}) at (3,-1)  node at ({c}) [right] {{${c}$}};\n\
\\coordinate ({d}) at (4,0)   node at ({d}) [right] {{${d}$}};\n\
\\coordinate ({s}) at (0,4)   node at ({s}) [above] {{${s}$}};\n\
\\draw [dashed] ({b})--({a})--({d}) ({s})--({a}); \n\
\\draw ({b})--({c})--({d}) ({s})--({b}) ({s})--({c}) ({s})--({d}); \n\
\\end{{tikzpicture}}\n"
    return code

def codelatex_hinh_hop(a,b,c,d,e,f,g,h):
    code=f"\\begin{{tikzpicture}}[scale=0.6] \n\
\\begin{{scriptsize}}\n\
\\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}};\n\
\\coordinate ({b}) at (-1,-1) node at ({b}) [left] {{${b}$}};\n\
\\coordinate ({c}) at (3,-1)  node at ({c}) [right] {{${c}$}};\n\
\\coordinate ({d}) at (4,0)   node at ({d}) [right] {{${d}$}};\n\
\\coordinate ({e}) at (0,2)   node at ({e}) [left] {{${e}$}};\n\
\\coordinate ({f}) at (-1,1) node at ({f}) [left] {{${f}$}};\n\
\\coordinate ({g}) at (3,1)  node at ({g}) [right] {{${g}$}};\n\
\\coordinate ({h}) at (4,2)   node at ({h}) [right] {{${h}$}};\n\
\\draw [dashed] ({b})--({a})--({d}) ({e})--({a});\n\
\\draw ({e})--({f})--({g})--({h})--({e}) ({f})--({b}) ({g})--({c}) ({h})--({d});\n\
\\draw ({b})--({c})--({d});\n\
\\end{{scriptsize}}\n\
\\end{{tikzpicture}}\n"
    return code

def code_hinh_langtruxien_tamgiac(a,b,c,a1,b1,c1):
    code=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}}; \n\
    \\coordinate ({b}) at (2,-1) node at ({b}) [below] {{${b}$}}; \n\
    \\coordinate ({c}) at (4,0)  node at ({c}) [below] {{${c}$}}; \n\
    \\coordinate ({a1}) at (1,4)   node at ({a1}) [above] {{${a1}$}}; \n\
    \\coordinate ({b1}) at (3,3)   node at ({b1}) [above] {{${b1}$}}; \n\
    \\coordinate ({c1}) at (5,4)   node at ({c1}) [above] {{${c1}$}};\n\
    \\draw [dashed] ({a})--({c}); \n\
    \\draw ({a})--({b})--({b1})--({a1})--({a}); \n\
    \\draw ({b1})--({c1})--({c})--({b}) ({a1})--({c1})--({c}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
    return code

def code_hinh_langtrudung_tamgiac(a,b,c,a1,b1,c1):
    code=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}}; \n\
    \\coordinate ({b}) at (2,-1) node at ({b}) [below] {{${b}$}}; \n\
    \\coordinate ({c}) at (4,0)  node at ({c}) [below] {{${c}$}}; \n\
    \\coordinate ({a1}) at (0,4)   node at ({a1}) [above] {{${a1}$}}; \n\
    \\coordinate ({b1}) at (2,3)   node at ({b1}) [above] {{${b1}$}}; \n\
    \\coordinate ({c1}) at (4,4)   node at ({c1}) [above] {{${c1}$}};\n\
    \\draw [dashed] ({a})--({c}); \n\
    \\draw ({a})--({b})--({b1})--({a1})--({a}); \n\
    \\draw ({b1})--({c1})--({c})--({b}) ({a1})--({c1})--({c}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
    return code

#Bài 1- Hai đường thẳng vuông góc
#[D11_C8_B1_01]-M1. Cho hình lập phương. Xác định góc giữa hai đường thẳng.
def uvxy9_L11_C8_B1_01():   	
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	#Tạo các cặp đường thẳng
	ten_lapphuong = f"ABCD.{A1}{B1}{C1}{D1}"

	chon=random.choice([90,45,60])
	if chon==90:
		duong_1=[f"{A1}{B1}", f"{A1}{D1}", f"{A1}{C1}", f"A{B1}", f"{B1}C"]
		duong_2=[f"BC", f"CD", f"BD" , f"C{D1}", f"A{D1}"]
		j=random.randint(0,len(duong_1)-1)
		duong_1, duong_2 = duong_1[j], duong_2[j]		
		
		if duong_1==f"{A1}{B1}" and duong_2==f"BC":
			noi_dung_loigiai=f"$({A1}{B1}, BC)= ({A1}{B1},{B1}{C1})=90^\\circ$."

		elif duong_1==f"{A1}{D1}" and duong_2==f"CD":
			noi_dung_loigiai=f"$({A1}{D1}, CD)= ({A1}{D1},{C1}{D1})=90^\\circ$."

		elif duong_1==f"{A1}{C1}" and duong_2==f"BD":
			noi_dung_loigiai=f"$({A1}{C1}, BD)= ({A1}{C1},{B1}{D1})=90^\\circ$."

		elif duong_1==f"A{B1}" and duong_2==f"C{D1}":
			noi_dung_loigiai=f"$(A{B1}, C{D1})= (A{B1},B{A1})=90^\\circ$."
		else:
			noi_dung_loigiai=f"$({B1}C, A{D1})= ({B1}C,B{C1})=90^\\circ$."

		kq, kq2, kq3, kq4 =90, 60, random.randint(30,40), random.randint(0,29)

	elif chon==45:
		duong_1=[f"{A1}{B1}", f"{A1}{D1}", f"{A1}{C1}", f"D{C1}", f"{B1}C"]
		duong_2=[f"BD", f"AC", f"BC" , f"AB", f"AD"]
		j=random.randint(0,len(duong_1)-1)
		duong_1, duong_2 = duong_1[j], duong_2[j]	
		if duong_1==f"{A1}{B1}" and duong_2==f"BD":
			noi_dung_loigiai=f"$({A1}{B1}, BD)= ({A1}{B1},{B1}{D1})=45^\\circ$."

		elif duong_1==f"{A1}{D1}" and duong_2==f"AC":
			noi_dung_loigiai=f"$({A1}{D1}, AC)= ({A1}{D1},{A1}{C1})=45^\\circ$."

		elif duong_1==f"{A1}{C1}" and duong_2==f"BC":
			noi_dung_loigiai=f"$({A1}{C1}, BC)= ({A1}{C1},{B1}{C1})=45^\\circ$."

		elif duong_1==f"D{C1}" and duong_2==f"AB":
			noi_dung_loigiai=f"$(D{C1}, AB)= (D{C1},CD)=45^\\circ$."
		else:
			noi_dung_loigiai=f"$({B1}C, AD)= ({B1}C,BC)=45^\\circ$."

		kq, kq2, kq3, kq4 =45, 60, random.randint(61,90), random.randint(0,30)

	else:
		duong_1=[f"{A1}B", f"{A1}{C1}", f"{B1}{D1}", f"{A1}D"]
		duong_2=[f"BD", f"{C1}D", f"{B1}C" , f"A{B1}", f"{A1}{C1}"]
		j=random.randint(0,len(duong_1)-1)
		duong_1, duong_2 = duong_1[j], duong_2[j]	
		if duong_1==f"{A1}B" and duong_2==f"BD":
			noi_dung_loigiai=f"Vì tam giác ${{{A1}BD}}$ đều nên $({A1}B, BD)= 60^\\circ$."

		elif duong_1==f"{A1}{C1}" and duong_2==f"{C1}D":
			noi_dung_loigiai=f"Vì tam giác ${{{A1}{C1}D}}$ đều nên $({A1}{C1}, {C1}D)= 60^\\circ$."

		elif duong_1==f"{B1}{D1}" and duong_2==f"{B1}C":
			noi_dung_loigiai=f"Vì tam giác ${{{B1}{D1}C}}$ đều nên $({B1}{D1}, {B1}C)= 60^\\circ$."
		else:
			noi_dung_loigiai=f"Vì tam giác ${{{A1}D{C1}}}$ đều nên $({A1}D, {A1}{C1})= 60^\\circ$."
		kq, kq2, kq3, kq4 =60, 90, random.randint(61,89), random.randint(0,60)
		
	pa_A= f"*${{{kq}^\\circ}}$"
	pa_B= f"${{{kq2}^\\circ}}$"
	pa_C= f"${{{kq3}^\\circ}}$"
	pa_D= f"${{{kq4}^\\circ}}$"

	code_hinh = codelatex_hinh_hop("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	noi_dung=f"Cho hình lăng trụ ${{{ten_lapphuong}}}$ có 6 mặt đều là hình vuông. Tính góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$."
	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B1_02]-M2. H.chóp có cạnh bên vuông góc, đáy h.c.n. Tính góc giữa 2 đường thẳng
def uvxy9_L11_C8_B1_02(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	canh_SA1 =random.choice([sqrt(2),sqrt(3),sqrt(5),random.randint(3,8)])
	canh_A1B1 = random.randint(1,7)	
	canh_A1D1 =canh_A1B1 + random.randint(1,5)	
	canh_SD1=sqrt(canh_SA1**2+canh_A1D1**2)

	chon=random.randint(1,3)
	if chon == 1:
		duong_1=[f"S{A1}"]
		duong_2=[f"{C1}{D1}"]
		i=random.randint(0,len(duong_1)-1)
		duong_1, duong_2 = duong_1[i], duong_2[i]

		if duong_1==f"S{A1}" and duong_2==f"{C1}{D1}":

			noi_dung_loigiai=f"${{ (S{A1},{C1}{D1}) = (S{A1},{A1}{B1}) = 90\\circ }}$."

			kq,kq2,kq3,kq4=90, random.randint(0,44), random.randint(45,59), random.randint(60,89)

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật,"\
			f" ${A1}{B1}={latex(canh_A1B1*a)}, {A1}{D1}={latex(canh_A1D1*a)}, S{A1}={latex(canh_SA1*a)}$."\
			f" Biết $S{A1}\\bot {A1}{B1},S{A1}\\bot {A1}{D1}$. Tính góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$."
	elif chon==2:
		duong_1=[f"S{B1}"]
		duong_2=[f"{C1}{D1}"]
		i=random.randint(0,len(duong_1)-1)
		duong_1, duong_2 = duong_1[i], duong_2[i]

		if duong_1==f"S{B1}" and duong_2==f"{C1}{D1}":
			t=canh_SA1/canh_A1B1			
			goc=round(atan(t).evalf() * 180 / pi,2)
			if "." in str(t):
				t=latex(my_module.hien_phan_so(t))
			else:
				t=latex(t)

			kq=return_number_vn(goc)
			kq2=return_number_vn(goc+(random.randint(10,90))/10)
			kq3=return_number_vn(goc+(random.randint(90,130))/10)
			kq4=return_number_vn(goc+(random.randint(140,200))/10)

			noi_dung_loigiai=f"$ (S{B1},{C1}{D1}) = (S{B1},{A1}{B1}) = \\widehat{{S{B1}{A1}}}$.\n"\
			f"$\\tan S{B1}{A1}=\\dfrac{{S{A1}}} {{{A1}{B1}}}= \\dfrac{{{latex(canh_SA1*a)}}} {{{latex(canh_A1B1*a)}}}={t}$.\n"\
			f"Suy ra $(S{B1},{C1}{D1})=\\widehat{{S{B1}{A1}}} = {kq}^\\circ$."

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật,"\
			f" ${A1}{B1}={latex(canh_A1B1*a)}, {A1}{D1}={latex(canh_A1D1*a)}, S{A1}={latex(canh_SA1*a)}$."\
			f" Biết $S{A1}\\bot {A1}{B1},S{A1}\\bot {A1}{D1}$. Tính góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$."
	else:
		duong_1=[f"S{D1}"]
		duong_2=[f"{B1}{C1}"]
		i=random.randint(0,len(duong_1)-1)
		duong_1, duong_2 = duong_1[i], duong_2[i]

		if duong_1==f"S{D1}" and duong_2==f"{B1}{C1}":
			t=canh_SA1/canh_SD1			
			goc=round(asin(t).evalf() * 180 / pi,2)

			kq=return_number_vn(goc)
			kq2=return_number_vn(goc+(random.randint(10,90))/10)
			kq3=return_number_vn(goc+(random.randint(90,130))/10)
			kq4=return_number_vn(goc+(random.randint(140,200))/10)

		noi_dung_loigiai=f"$ (S{D1},{B1}{C1}) = (S{D1},{A1}{D1}) = \\widehat{{S{D1}{A1}}}$.\n"\
			f"$\\sin S{D1}{A1}=\\dfrac{{S{A1}}} {{S{D1}}}= \\dfrac{{{latex(canh_SA1*a)}}} {{{latex(canh_SD1*a)}}}={latex(t)}$.\n"\
			f"Suy ra $(S{D1},{B1}{C1})=\\widehat{{S{D1}{A1}}} = {kq}^\\circ$."		

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật,"\
			f" ${A1}{B1}={latex(canh_A1B1*a)}, S{D1}={latex(canh_SD1*a)}, S{A1}={latex(canh_SA1*a)}$."\
			f" Biết $S{A1}\\bot {A1}{B1},S{A1}\\bot {A1}{D1}$. Tính góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$."	

	
    #Tạo các phương án
	pa_A= f"*${{{kq}^\\circ}}$"
	pa_B= f"${{{kq2}^\\circ}}$"
	pa_C= f"${{{kq3}^\\circ}}$"
	pa_D= f"${{{kq4}^\\circ}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B1_03]-M2. H.chóp có cạnh bên vuông góc. Tìm cặp đường thẳng vuông góc
def uvxy9_L11_C8_B1_03(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	

	chon=random.randint(1,3)
	if chon == 1:
		duong_1=[f"S{A1}"]
		duong_2=[f"{C1}{D1}", f"{B1}{C1}", f"{M1}{N1}"]
		i=random.randint(0,len(duong_2)-1)
		duong_1, duong_2 = duong_1[0], duong_2[i]

		if duong_1==f"S{A1}" and duong_2==f"{C1}{D1}":
			noi_dung_loigiai=f"${{ (S{A1},{C1}{D1}) = (S{A1},{A1}{B1}) = 90^\\circ }}$."
		elif duong_1==f"S{A1}" and duong_2==f"{B1}{C1}":
			noi_dung_loigiai=f"${{ (S{A1},{B1}{C1}) = (S{A1},{A1}{D1}) = 90^\\circ }}$."
		else:
			noi_dung_loigiai=f"${{ (S{A1},{M1}{N1}) = (S{A1},{A1}{B1}) = 90^\\circ }}$."
		
		kq = f"${{ {duong_1}}}$ và ${{{duong_2}}}$"
		kq2=random.choice([f"${{ {duong_1} }}$ và ${{ S{C1} }}$",f"${{ {duong_1} }}$ và ${{ {A1}{N1} }}$" ])
		kq3=random.choice([f"${{ S{B1} }}$ và ${{ {A1}{B1} }}$", f"${{ {A1}{M1} }}$ và ${{ {A1}{C1} }}$"])
		kq4=random.choice([f"${{ {A1}{B1} }}$ và ${{ {B1}{D1} }}$", f"${{{ A1}{B1} }}$ và ${{ S{C1} }}$"])

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot{{{A1}{B1}}},S{A1}\\bot{{{A1}{D1}}}$."\
				f" Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{S{C1}}},{{S{D1}}}$. Cặp đường thẳng nào sau đây là vuông góc nhau?"
	elif chon == 2:
		duong_1=[f"S{A1}"]
		duong_2=[f"{M1}{N1}"]
		i=random.randint(0,len(duong_2)-1)
		duong_1, duong_2 = duong_1[0], duong_2[i]

		if duong_1==f"S{A1}" and duong_2==f"{M1}{N1}":
			noi_dung_loigiai=f"${{ (S{A1},{M1}{N1}) = (S{A1},{A1}{D1}) = 90^\\circ }}$."

		kq = f"${{ {duong_1}}}$ và ${{{duong_2}}}$"
		kq2=random.choice([f"${{ {duong_1} }}$ và ${{ S{C1} }}$",f"${{ {duong_1} }}$ và ${{ {A1}{N1} }}$" ])
		kq3=random.choice([f"${{ S{B1} }}$ và ${{ {A1}{B1} }}$", f"${{ {B1}{M1} }}$ và ${{ {C1}{D1} }}$"])
		kq4=random.choice([f"${{ {A1}{B1} }}$ và ${{ {B1}{D1} }}$", f"${{{ A1}{B1} }}$ và ${{ S{C1} }}$"])

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot{{{A1}{B1}}},S{A1}\\bot{{{A1}{D1}}}$."\
				f" Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{S{A1}}},{{S{D1}}}$. Cặp đường thẳng nào sau đây là vuông góc nhau?"
	else:
		duong_1=[f"{B1}{D1}"]
		duong_2=[f"{M1}{N1}"]
		i=random.randint(0,len(duong_2)-1)
		duong_1, duong_2 = duong_1[0], duong_2[i]

		t=random.randint(1,4)
		t1=my_module.xu_li_heso_1(t)
		if duong_1==f"{B1}{D1}" and duong_2==f"{M1}{N1}":
			noi_dung_loigiai=f"Từ giả thiết suy ra $\\dfrac{{S{M1}}}{{S{A1}}}=\\dfrac{{S{N1}}}{{S{C1}}}=\\dfrac{{{t1}}}{{{t+1}}} \\Rightarrow {{{M1}{N1}}}$//${{{A1}{C1}}}$ "\
			f"nên ${{ ({B1}{D1},{M1}{N1}) = ({B1}{D1},{A1}{C1}) = 90^\\circ }}$."

		kq = f"${{{duong_1}}}$ và ${{{duong_2}}}$"
		kq2=f"${{{B1}{D1}}}$ và ${{S{B1}}}$"
		kq3=f"${{S{D1}}}$ và ${{{M1}{N1}}}$"
		kq4=f"${{{B1}{M1}}}$ và ${{{C1}{D1}}}$"


		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot{{{A1}{B1}}},S{A1}\\bot{{{A1}{D1}}}$. Gọi ${{{M1},{N1}}}$ lần lượt là các điểm thuộc các cạnh ${{S{A1}}},{{S{C1}}}$"\
				f" sao cho $S{M1}={t1}{M1}{A1}, {t+1} S{N1}={t1}S{C1}$. Cặp đường thẳng nào sau đây là vuông góc nhau?"


    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B1_04]-TF-M2. Cho hình lập phương. Tạo câu đúng-sai: góc giữa 2 đường thẳng.
def uvxy9_L11_C8_B1_04(): 
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	#Tạo các cặp đường thẳng
	ten_lapphuong = f"ABCD.{A1}{B1}{C1}{D1}"	
	
	duong_1=[f"{A1}{B1}", f"{A1}{D1}", f"{A1}{C1}"]
	duong_2=[f"BC", f"CD", f"BD"]
	j=random.randint(0,2)
	duong_1, duong_2 = duong_1[j], duong_2[j]

	code_hinh = codelatex_hinh_hop("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
				
	noi_dung=f"Cho hình lập phương ${{{ten_lapphuong}}}$. Xét tính đúng sai của các khẳng định sau\n\n"	

	#Tạo kết quả 1
	kq1_T=f"*Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{90^\\circ}}$"
	kq1_F=f"Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{{random.choice([30,45,60])}^\\circ}}$"

	if duong_1==f"{A1}{B1}" and duong_2==f"BC":	
		loigiai_1=f"$({A1}{B1}, BC)= ({A1}{B1},{B1}{C1})=90^\\circ$."

	if duong_1==f"{A1}{D1}" and duong_2==f"CD":
		loigiai_1=f"$({A1}{D1}, CD)= ({A1}{D1},{C1}{D1})=90^\\circ$."

	if duong_1==f"{A1}{C1}" and duong_2==f"BD":
		loigiai_1=f"$({A1}{C1}, BD)= ({A1}{C1},{B1}{D1})=90^\\circ$."

	#Tạo kết quả 2
	duong_1=[ f"A{B1}", f"{B1}C"]
	duong_2=[f"C{D1}", f"A{D1}"]
	j=random.randint(0,1)
	duong_1, duong_2 = duong_1[j], duong_2[j]

	kq2_T=f"*Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{90^\\circ}}$"
	kq2_F=f"Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{{random.choice([30,45,60])}^\\circ}}$"	

	if duong_1==f"A{B1}" and duong_2==f"C{D1}":
		loigiai_2=f"$(A{B1}, C{D1})= (A{B1},B{A1})=90^\\circ$."

	if duong_1==f"{B1}C" and duong_2==f"A{D1}":
		loigiai_2=f"$({B1}C, A{D1})= ({B1}C,B{C1})=90^\\circ$."

	#Tạo kết quả 3

	duong_1=[f"{A1}{B1}", f"{A1}{D1}", f"{A1}{C1}", f"D{C1}", f"{B1}C"]
	duong_2=[f"BD", f"AC", f"BC" , f"AB", f"AD"]
	j=random.randint(0,len(duong_1)-1)
	duong_1, duong_2 = duong_1[j], duong_2[j]

	kq3_T=f"*Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{45^\\circ}}$"
	kq3_F=f"Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{{random.choice([30,60,90])}^\\circ}}$"

	if duong_1==f"{A1}{B1}" and duong_2==f"BD":
		loigiai_3=f"$({A1}{B1}, BD)= ({A1}{B1},{B1}{D1})=45^\\circ$."

	if duong_1==f"{A1}{D1}" and duong_2==f"AC":
		loigiai_3=f"$({A1}{D1}, AC)= ({A1}{D1},{A1}{C1})=45^\\circ$."

	if duong_1==f"{A1}{C1}" and duong_2==f"BC":
		loigiai_3=f"$({A1}{C1}, BC)= ({A1}{C1},{B1}{C1})=45^\\circ$."

	if duong_1==f"D{C1}" and duong_2==f"AB":
		loigiai_3=f"$(D{C1}, AB)= (D{C1},CD)=45^\\circ$."

	if duong_1==f"{B1}C" and duong_2==f"AD":
		loigiai_3=f"$({B1}C, AD)= ({B1}C,BC)=45^\\circ$."

	#Tạo kết quả 4
	duong_1=[f"{A1}B", f"{A1}{C1}", f"{B1}{D1}", f"{A1}D"]
	duong_2=[f"BD", f"{C1}D", f"{B1}C", f"{A1}{C1}"]
	j=random.randint(0,3)
	duong_1, duong_2 = duong_1[j], duong_2[j]

	kq4_T=f"*Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{60^\\circ}}$"
	kq4_F=f"Góc giữa hai đường thẳng ${{{duong_1}}}$ và ${{{duong_2}}}$ bằng ${{{random.choice([30,45,90])}^\\circ}}$"

	if duong_1==f"{A1}B" and duong_2==f"BD":
		loigiai_4=f"Vì tam giác ${{{A1}BD}}$ đều nên $({A1}B, BD)= 60^\\circ$."

	if duong_1==f"{A1}{C1}" and duong_2==f"{C1}D":
		loigiai_4=f"Vì tam giác ${{{A1}{C1}D}}$ đều nên $({A1}{C1}, {C1}D)= 60^\\circ$."

	if duong_1==f"{B1}{D1}" and duong_2==f"{B1}C":
		loigiai_4=f"Vì tam giác ${{{B1}{D1}C}}$ đều nên $({B1}{D1}, {B1}C)= 60^\\circ$."

	if duong_1==f"{A1}D" and duong_2==f"{A1}{C1}":
		loigiai_4=f"Vì tam giác ${{{A1}D{C1}}}$ đều nên $({A1}D, {A1}{C1})= 60^\\circ$."
	
	
	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"\
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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
	f"b) {loigiai[1]}\\\\ \n"\
	f"c) {loigiai[2]}\\\\ \n"\
	f"d) {loigiai[3]}\\\\ \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
	f"\\begin{{center}}\n{code_hinh}\\end{{center}}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"	
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#Bài 2: Đường thẳng vuông góc với mặt phẳng 

#[D11_C8_B2_01]-M1. S.ABCD: cạnh v.g đáy h.vuông. Tìm đường vg mặt.
def uvxy9_L11_C8_B2_01(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	
	duong=[f"{B1}{C1}",f"{C1}{D1}", f"{B1}{D1}" ]
	mat=[f"S{A1}{B1}", f"S{A1}{D1}", f"S{A1}{C1}"]
	i=random.randint(0,len(duong)-1)
	duong, mat = duong[i], mat[i]

	if duong==f"{B1}{C1}" and mat==f"S{A1}{B1}":
		noi_dung_loigiai=f"Ta có: ${{{B1}{C1}\\bot {A1}{B1}}}$ và ${{{B1}{C1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${B1}{C1}\\bot (S{A1}{B1})$."
	if duong==f"{C1}{D1}" and mat==f"S{A1}{D1}":
		noi_dung_loigiai=f"Ta có: ${{{C1}{D1}\\bot {A1}{D1}}}$ và ${{{C1}{D1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${C1}{D1}\\bot (S{A1}{D1})$."
		
	if duong==f"{B1}{D1}" and mat==f"S{A1}{C1}":
		noi_dung_loigiai=f"Ta có: ${{{B1}{D1}\\bot {A1}{C1}}}$ và ${{{B1}{D1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${B1}{D1}\\bot (S{A1}{C1})$."			
	
	kq = f"${{{duong} \\bot ({mat})}}$"
	kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$",f"$S{A1}\\bot (S{B1}{D1})$",f"$S{A1}\\bot (S{C1}{D1})$"])
	kq3=random.choice([f"${B1}{C1}\\bot (S{A1}{C1})$", f"${B1}{C1}\\bot (S{C1}{D1})$", f"${B1}{D1}\\bot (S{A1}{D1})$"])
	kq4=random.choice([f"${C1}{D1}\\bot (S{B1}{D1})$", f"${C1}{D1}\\bot (S{B1}{C1})$", f"${B1}{D1}\\bot (S{B1}{C1})$"])

	noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Tìm khẳng định đúng?"

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word, phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C8_B2_02]-M1. S.ABCD: cạnh v.g đáy h.chữ nhật. Tìm đường vg mặt
def uvxy9_L11_C8_B2_02(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	
	duong=[f"{B1}{C1}",f"{C1}{D1}", f"{B1}{D1}" ]
	mat=[f"S{A1}{B1}", f"S{A1}{D1}", f"S{A1}{M1}"]
	i=random.randint(0,len(duong)-1)
	duong, mat = duong[i], mat[i]

	if duong==f"{B1}{C1}" and mat==f"S{A1}{B1}":
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
			f" Tìm khẳng định đúng?"
		noi_dung_loigiai=f"Ta có: ${{{B1}{C1}\\bot {A1}{B1}}}$ và ${{{B1}{C1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${B1}{C1}\\bot (S{A1}{B1})$."
		debai_TL=f"Câu 1: Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
			f" Chứng minh: ${B1}{C1}\\bot (S{A1}{B1})$."

	if duong==f"{C1}{D1}" and mat==f"S{A1}{D1}":
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
			f" Tìm khẳng định đúng?"
		noi_dung_loigiai=f"Ta có: ${{{C1}{D1}\\bot {A1}{D1}}}$ và ${{{C1}{D1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${C1}{D1}\\bot (S{A1}{D1})$."
		debai_TL=f"Câu 1: Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
			f" Chứng minh: ${C1}{D1}\\bot (S{A1}{D1})$."
		
	if duong==f"{B1}{D1}" and mat==f"S{A1}{M1}":
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
			f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{{B1}{D1}}}$. Tìm khẳng định đúng?"

		noi_dung_loigiai=f"Ta có: ${{{B1}{D1}\\bot {A1}{M1}}}$ và ${{{B1}{D1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${B1}{D1}\\bot (S{A1}{M1})$."

		debai_TL=f"Câu 1: Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
			f" Chứng minh: ${B1}{D1}\\bot (S{A1}{M1})$."		
	
	kq = f"${{{duong} \\bot ({mat})}}$"
	kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$",f"$S{A1}\\bot (S{B1}{D1})$",f"$S{A1}\\bot (S{C1}{D1})$"])
	kq3=random.choice([f"${B1}{C1}\\bot (S{A1}{C1})$", f"${B1}{C1}\\bot (S{C1}{D1})$", f"${B1}{D1}\\bot (S{A1}{D1})$"])
	kq4=random.choice([f"${C1}{D1}\\bot (S{B1}{D1})$", f"${C1}{D1}\\bot (S{B1}{C1})$", f"${B1}{D1}\\bot (S{B1}{C1})$"])	

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {debai_TL}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n".replace("Câu 1:","")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_03]-M1. S.ABCD: cạnh v.g đáy h.thoi. Tìm đường vg mặt
def uvxy9_L11_C8_B2_03(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	
	duong=[f"{C1}{M1}",f"{C1}{N1}", f"{B1}{D1}" ]
	mat=[f"S{A1}{B1}", f"S{A1}{D1}", f"S{A1}{C1}"]
	i=random.randint(0,len(duong)-1)
	duong, mat = duong[i], mat[i]

	if duong==f"{C1}{M1}" and mat==f"S{A1}{B1}":
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình thoi, $S{A1}\\bot (ABCD)$."\
			f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{C1}}}$ trên đường thẳng ${{{A1}{B1}}}$."\
			f" ${{{N1}}}$ là hình chiếu vuông góc của ${{{C1}}}$ trên đường thẳng ${{{A1}{D1}}}$. Tìm khẳng định đúng?"
		debai_TL=f"Câu 1: Cho hình chóp ${{S.ABCD}}$ có đáy là hình thoi, $S{A1}\\bot (ABCD)$."\
			f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{C1}}}$ trên đường thẳng ${{{A1}{B1}}}$."\
			f" Chứng minh: ${C1}{M1}\\bot (S{A1}{B1})$."

		noi_dung_loigiai=f"Ta có: ${{{C1}{M1}\\bot {A1}{B1}}}$ và ${{{C1}{M1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${C1}{M1}\\bot (S{A1}{B1})$."

		kq = f"${{{duong} \\bot ({mat})}}$"
		kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$",f"$S{A1}\\bot (S{B1}{D1})$",f"$S{A1}\\bot (S{C1}{D1})$",f"${A1}{C1}\\bot (S{B1}{D1})$" ])
		kq3=random.choice([f"${B1}{C1}\\bot (S{A1}{C1})$", f"${B1}{C1}\\bot (S{C1}{D1})$", f"${B1}{D1}\\bot (S{A1}{D1})$"])
		kq4=random.choice([f"${C1}{N1}\\bot (S{B1}{D1})$",f"${C1}{N1}\\bot (S{A1}{B1})$"])

	if duong==f"{C1}{N1}" and mat==f"S{A1}{D1}":
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình thoi, $S{A1}\\bot (ABCD)$."\
			f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{C1}}}$ trên đường thẳng ${{{A1}{B1}}}$."\
			f" ${{{N1}}}$ là hình chiếu vuông góc của ${{{C1}}}$ trên đường thẳng ${{{A1}{D1}}}$. Tìm khẳng định đúng?"
		debai_TL=f"Câu 1: Cho hình chóp ${{S.ABCD}}$ có đáy là hình thoi, $S{A1}\\bot (ABCD)$."\
			f" Gọi ${{{N1}}}$ là hình chiếu vuông góc của ${{{C1}}}$ trên đường thẳng ${{{A1}{D1}}}$."\
			f" Chứng minh: ${C1}{N1}\\bot (S{A1}{D1})$."

		noi_dung_loigiai=f"Ta có: ${{{C1}{N1}\\bot {A1}{D1}}}$ và ${{{C1}{N1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${C1}{N1}\\bot (S{A1}{D1})$."
		kq = f"${{{duong} \\bot ({mat})}}$"
		kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$",f"$S{A1}\\bot (S{B1}{D1})$",f"$S{A1}\\bot (S{C1}{D1})$",f"${A1}{C1}\\bot (S{B1}{D1})$" ])
		kq3=random.choice([f"${B1}{C1}\\bot (S{A1}{C1})$", f"${B1}{C1}\\bot (S{C1}{D1})$", f"${B1}{D1}\\bot (S{A1}{D1})$"])
		kq4=random.choice([f"${C1}{M1}\\bot (S{B1}{D1})$", f"${C1}{M1}\\bot (S{A1}{C1})$"])	
		
	if duong==f"{B1}{D1}" and mat==f"S{A1}{C1}":
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình thoi, $S{A1}\\bot (ABCD)$."\
		f" Tìm khẳng định đúng?"

		debai_TL=f"Câu 1: Cho hình chóp ${{S.ABCD}}$ có đáy là hình thoi, $S{A1}\\bot (ABCD)$."\
		f" Chứng minh: ${B1}{D1}\\bot (S{A1}{C1})$."

		noi_dung_loigiai=f"Ta có: ${{{B1}{D1}\\bot {A1}{C1}}}$ và ${{{B1}{D1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABCD))$ nên ${B1}{D1}\\bot (S{A1}{C1})$."	
		kq = f"${{{duong} \\bot ({mat})}}$"
		kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$",f"$S{A1}\\bot (S{B1}{D1})$",f"$S{A1}\\bot (S{C1}{D1})$",f"${A1}{C1}\\bot (S{B1}{D1})$" ])
		kq3=random.choice([f"${B1}{C1}\\bot (S{A1}{C1})$", f"${B1}{C1}\\bot (S{C1}{D1})$", f"${B1}{D1}\\bot (S{A1}{D1})$"])
		kq4=random.choice([f"${C1}{D1}\\bot (S{B1}{D1})$", f"${C1}{D1}\\bot (S{B1}{C1})$", f"${B1}{D1}\\bot (S{B1}{C1})$"])		
	
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {debai_TL}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n".replace("Câu 1:","")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_04]-M2. S.ABCD: cạnh v.g đáy h.tam giác vuông. Tìm đường vg mặt
def uvxy9_L11_C8_B2_04(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]

	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])	
	
	duong=[f"{A1}{B1}", f"{A1}{C1}", f"{B1}{C1}"]
	mat=[f"S{A1}{C1}", f"S{A1}{B1}", f"S{A1}{M1}"]
	i=random.randint(0,len(duong)-1)
	duong, mat = duong[i], mat[i]

	if duong==f"{A1}{B1}" and mat==f"S{A1}{C1}":
		noi_dung_loigiai=f"Ta có: ${{{A1}{B1}\\bot {A1}{C1}}}$ và ${{{A1}{B1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${A1}{B1}\\bot (S{A1}{C1})$."

	if duong==f"{A1}{C1}" and mat==f"S{A1}{B1}":
		noi_dung_loigiai=f"Ta có: ${{{A1}{C1}\\bot {A1}{B1}}}$ và ${{{A1}{C1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${A1}{C1}\\bot (S{A1}{B1})$."

	if duong==f"{B1}{C1}" and mat==f"S{A1}{M1}":
		noi_dung_loigiai=f"Ta có: ${{{A1}{M1}\\bot {B1}{C1}}}$ và ${{{A1}{M1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${A1}{M1}\\bot (S{B1}{C1})$."
			
	
	kq = f"${{{duong} \\bot ({mat})}}$"
	kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$",f"$S{A1}\\bot (S{M1}{B1})$", f"$S{A1}\\bot (S{M1}{C1})$" ])
	kq3=random.choice([f"${A1}{B1}\\bot (S{A1}{M1})$", f"${A1}{B1}\\bot (S{B1}{C1})$"])
	kq4=random.choice([f"${A1}{C1}\\bot (S{A1}{M1})$", f"${A1}{C1}\\bot (S{B1}{C1})$"])

	noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
			f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{{B1}{C1}}}$. Tìm khẳng định đúng?"

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_05]-M2. S.ABCD: cạnh v.g đáy h.tam giác đều. Tìm đường vg mặt
def uvxy9_L11_C8_B2_05(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]

	M1=["M", "G", "N"]
	N1=["N", "H", "P"]
	P1=["P", "I", "Q"]
	i=random.randint(0,2)
	M1, N1, P1 = M1[i], N1[i], P1[i]		
	
	duong=[f"{B1}{C1}", f"{B1}{N1}", f"{C1}{P1}"]
	mat=[f"S{A1}{M1}", f"S{A1}{C1}", f"S{A1}{B1}"]
	i=random.randint(0,len(duong)-1)
	duong, mat = duong[i], mat[i]

	if duong==f"{B1}{C1}" and mat==f"S{A1}{M1}":
		noi_dung_loigiai=f"Ta có: ${{{B1}{C1}\\bot {A1}{M1}}}$ và ${{{B1}{C1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${B1}{C1}\\bot (S{A1}{M1})$."

	if duong==f"{B1}{N1}" and mat==f"S{A1}{C1}":
		noi_dung_loigiai=f"Ta có: ${{{B1}{N1}\\bot {A1}{C1}}}$ và ${{{B1}{N1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${B1}{N1}\\bot (S{A1}{C1})$."

	if duong==f"{C1}{P1}" and mat==f"S{A1}{B1}":
		noi_dung_loigiai=f"Ta có: ${{{C1}{P1}\\bot {A1}{B1}}}$ và ${{{C1}{P1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${C1}{P1}\\bot (S{A1}{B1})$."
	
	
	kq = f"${{{duong} \\bot ({mat})}}$"
	kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$", f"${A1}{M1}\\bot (S{B1}{C1})$" ])
	kq3=random.choice([f"${A1}{B1}\\bot (S{A1}{M1})$", f"${A1}{B1}\\bot (S{A1}{C1})$"])
	kq4=random.choice([f"${A1}{C1}\\bot (S{A1}{M1})$", f"${A1}{C1}\\bot (S{A1}{B1})$"])

	noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$."\
			f" Gọi ${{{M1}, {N1},{P1}}}$ lần lượt là trung điểm của ${{{B1}{C1}, {A1}{C1}, {A1}{B1}}}$. Tìm khẳng định đúng?"

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_06]-M3. S.ABC: cạnh v.g đáy h.tam giác đều, có hình chiếu lên cạnh bên. Tìm đường vg mặt
def uvxy9_L11_C8_B2_06(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	S1="S"
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]

	M1=["M", "N", "N", "M"]
	N1=["N", "M", "P", "N"]
	P1=["P", "P", "Q", "I"]
	H1=["G", "I", "H", "K"]
	i=random.randint(0,3)
	M1, N1, P1, H1 = M1[i], N1[i], P1[i], H1[i]
		
	
	duong=[f"{A1}{H1}", f"S{C1}", f"S{B1}"]
	mat=[f"(S{B1}{C1})", f"({H1}{B1}{N1})", f"({H1}{C1}{P1})" ]
	i=random.randint(0,len(duong)-1)
	duong, mat = duong[i], mat[i]

	if duong==f"{A1}{H1}" and mat==f"(S{B1}{C1})":		
		kq = f"${{{duong} \\bot {mat}}}$"
		kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$", f"${A1}{M1}\\bot (S{B1}{C1})$" ])
		kq3=random.choice([f"${A1}{B1}\\bot (S{A1}{M1})$", f"${A1}{B1}\\bot (S{A1}{C1})$"])
		kq4=random.choice([f"${A1}{C1}\\bot (S{A1}{M1})$", f"${A1}{C1}\\bot (S{A1}{B1})$"])

		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$."\
				f" Gọi ${{{M1}, {N1},{P1}}}$ lần lượt là trung điểm của ${{{B1}{C1}, {A1}{C1}, {A1}{B1}}}$."\
				f" Gọi ${{{H1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{S{M1}}}$. Tìm khẳng định đúng?"

		code_hinhloigiai=f"\\begin{{tikzpicture}}\n\
			\\coordinate ({A1}) at (0,0)   node at ({A1}) [left] {{${A1}$}};\n\
			\\coordinate ({B1}) at (1,-2) node at ({B1}) [left] {{${B1}$}};\n\
			\\coordinate ({C1}) at (4,0)   node at ({C1}) [right] {{${C1}$}};\n\
			\\coordinate ({M1}) at (2.5,-1)   node at ({M1}) [below right] {{${M1}$}};\n\
			\\coordinate ({S1}) at (0,4)   node at ({S1}) [above] {{${S1}$}};\n\
			\\coordinate ({H1}) at (1.25,1.5)   node at ({H1}) [above right] {{${H1}$}};\n\
			\\draw [dashed] ({A1})--({C1}) ; \n\
			\\draw ({A1})--({B1}) ({B1})--({C1}) ({S1})--({A1}) ({S1})--({B1}) ({S1})--({C1}); \n\
			\\draw ({S1})--({M1}); \n\
			\\draw [dashed] ({A1})--({M1}) ({A1})--({H1}) ; \n\
			\\end{{tikzpicture}}\n"
		code = my_module.moi_truong_anh_latex(code_hinhloigiai)
		file_name_loigiai = my_module.pdftoimage_timename(code)

		noi_dung_loigiai=f" Ta có: ${{{B1}{C1}\\bot {A1}{M1}}}$ và ${{{B1}{C1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${B1}{C1}\\bot (S{A1}{M1})$.\n\nSuy ra ${A1}{H1}\\bot {B1}{C1}\\subset (S{B1}{C1})$."\
						f" Theo giả thiết ta có: ${A1}{H1} \\bot S{M1} \\subset (S{B1}{C1})$. Vậy ${A1}{H1}\\bot (S{B1}{C1})$."
	
	if duong==f"S{C1}" and mat==f"({H1}{B1}{N1})":
		kq = f"${{{duong} \\bot {mat}}}$"
		kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$", f"${A1}{M1}\\bot (S{B1}{C1})$",f"$S{C1}\\bot (S{A1}{B1})$" ])
		kq3=random.choice([f"${A1}{B1}\\bot (S{A1}{M1})$", f"${A1}{B1}\\bot (S{A1}{C1})$", f"${A1}{B1}\\bot (S{C1}{P1})$"])
		kq4=random.choice([f"${A1}{C1}\\bot (S{A1}{M1})$", f"${A1}{C1}\\bot (S{A1}{B1})$", f"${A1}{C1}\\bot (S{B1}{N1})$"])

		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$."\
				f" Gọi ${{{M1}, {N1},{P1}}}$ lần lượt là trung điểm của ${{{B1}{C1}, {A1}{C1}, {A1}{B1}}}$."\
				f" Gọi ${{{H1}}}$ là hình chiếu vuông góc của ${{{B1}}}$ trên đường thẳng ${{S{C1}}}$. Tìm khẳng định đúng?"
		code_hinhloigiai=f"\\begin{{tikzpicture}}\n\
			\\coordinate ({A1}) at (0,0)   node at ({A1}) [left] {{${A1}$}};\n\
			\\coordinate ({B1}) at (1,-2) node at ({B1}) [left] {{${B1}$}};\n\
			\\coordinate ({C1}) at (4,0)   node at ({C1}) [right] {{${C1}$}};\n\
			\\coordinate ({N1}) at (2,0)   node at ({N1}) [below right] {{${N1}$}};\n\
			\\coordinate ({S1}) at (0,4)   node at ({S1}) [above] {{${S1}$}};\n\
			\\coordinate ({H1}) at (1.5,2.5)   node at ({H1}) [above] {{${H1}$}};\n\
			\\draw [dashed] ({A1})--({C1}) ; \n\
			\\draw ({A1})--({B1}) ({B1})--({C1}) ({S1})--({A1}) ({S1})--({B1}) ({S1})--({C1}); \n\
			\\draw ({B1})--({H1}); \n\
			\\draw [dashed] ({B1})--({N1}) ({H1})--({N1}) ; \n\
			\\end{{tikzpicture}}\n"
		code = my_module.moi_truong_anh_latex(code_hinhloigiai)
		file_name_loigiai = my_module.pdftoimage_timename(code)

		noi_dung_loigiai=f" Ta có: ${{{B1}{N1}\\bot {A1}{C1}}}$ và ${{{B1}{N1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${B1}{N1}\\bot (S{A1}{C1})$.\n\nSuy ra $S{C1}\\bot {B1}{N1}\\subset ({H1}{B1}{N1})$."\
						f" Theo giả thiết ta có: $S{C1} \\bot {B1}{H1} \\subset ({H1}{B1}{N1})$. Vậy $S{C1}\\bot ({H1}{B1}{N1})$."

	if duong==f"S{B1}" and mat==f"({H1}{C1}{P1})":
		kq = f"${{{duong} \\bot {mat}}}$"
		kq2=random.choice([f"$S{A1}\\bot (S{B1}{C1})$", f"${A1}{M1}\\bot (S{B1}{C1})$",f"$S{C1}\\bot (S{A1}{B1})$" ])
		kq3=random.choice([f"${A1}{B1}\\bot (S{A1}{M1})$", f"${A1}{B1}\\bot (S{A1}{C1})$", f"${A1}{B1}\\bot (S{C1}{P1})$"])
		kq4=random.choice([f"${A1}{C1}\\bot (S{A1}{M1})$", f"${A1}{C1}\\bot (S{A1}{B1})$", f"${A1}{C1}\\bot (S{B1}{N1})$"])

		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$."\
				f" Gọi ${{{M1}, {N1},{P1}}}$ lần lượt là trung điểm của ${{{B1}{C1}, {A1}{C1}, {A1}{B1}}}$."\
				f" Gọi ${{{H1}}}$ là hình chiếu vuông góc của ${{{C1}}}$ trên đường thẳng ${{S{B1}}}$. Tìm khẳng định đúng?"
		code_hinhloigiai=f"\\begin{{tikzpicture}}\n\
			\\coordinate ({A1}) at (0,0)   node at ({A1}) [left] {{${A1}$}};\n\
			\\coordinate ({B1}) at (1,-2) node at ({B1}) [left] {{${B1}$}};\n\
			\\coordinate ({C1}) at (4,0)   node at ({C1}) [right] {{${C1}$}};\n\
			\\coordinate ({P1}) at (0.5,-1)   node at ({P1}) [below left] {{${P1}$}};\n\
			\\coordinate ({S1}) at (0,4)   node at ({S1}) [above] {{${S1}$}};\n\
			\\coordinate ({H1}) at (1/3,2)   node at ({H1}) [above right] {{${H1}$}};\n\
			\\draw [dashed] ({A1})--({C1}); \n\
			\\draw ({A1})--({B1}) ({B1})--({C1}) ({S1})--({A1}) ({S1})--({B1}) ({S1})--({C1}); \n\
			\\draw ({C1})--({H1}) ({H1})--({P1}); \n\
			\\draw [dashed] ({C1})--({P1}); \n\
			\\end{{tikzpicture}}\n"
		code = my_module.moi_truong_anh_latex(code_hinhloigiai)
		file_name_loigiai = my_module.pdftoimage_timename(code)

		noi_dung_loigiai=f" Ta có: ${{{C1}{P1}\\bot {A1}{B1}}}$ và ${{{C1}{P1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${C1}{P1}\\bot (S{A1}{B1})$.\n\nSuy ra $S{B1}\\bot {C1}{P1}\\subset ({H1}{C1}{P1})$."\
						f" Theo giả thiết ta có: $S{B1} \\bot {C1}{H1} \\subset ({H1}{C1}{P1})$. Vậy $S{B1}\\bot ({H1}{C1}{P1})$."
	

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n\n {file_name_loigiai} Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n\n \\begin{{center}}\n {code_hinhloigiai} \\end{{center}}\n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_07]-M3. S.ABC: cạnh v.g đáy h.tam giác đều, có hình chiếu lên cạnh bên. Tìm đường vg đường
def uvxy9_L11_C8_B2_07(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	S1="S"
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]

	M1=["M", "N", "N", "M"]
	N1=["N", "M", "P", "N"]
	P1=["P", "P", "Q", "I"]
	H1=["G", "I", "H", "K"]
	i=random.randint(0,3)
	M1, N1, P1, H1 = M1[i], N1[i], P1[i], H1[i]
		
	
	duong_1=[f"{A1}{H1}", f"{A1}{H1}"]
	duong_2=[ f"S{B1}", f"S{C1}"]
	i=random.randint(0,len(duong_1)-1)
	i=1
	duong_1, duong_2 = duong_1[i], duong_2[i]

		
	if duong_1==f"{A1}{H1}" and any([duong_2==f"S{B1}",duong_2==f"S{C1}"]):
		kq = f"${duong_1} \\bot {duong_2}$"
		kq2=random.choice([f"$S{A1}\\bot S{B1}$", f"$S{A1}\\bot S{C1}$", f"$S{N1}\\bot {A1}{B1}$"])
		kq3=random.choice([f"${A1}{B1}\\bot S{B1}$", f"${A1}{B1}\\bot S{C1}$",f"$S{N1}\\bot {B1}{C1}$"])
		kq4=random.choice([f"$S{P1}\\bot {A1}{B1}$", f"$S{P1}\\bot {A1}{C1}$"])

		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$."\
				f" Gọi ${{{M1}, {N1},{P1}}}$ lần lượt là trung điểm của ${{{B1}{C1}, {A1}{C1}, {A1}{B1}}}$."\
				f" Gọi ${{{H1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{S{M1}}}$. Tìm khẳng định đúng?"
		code_hinhloigiai=f"\\begin{{tikzpicture}}\n\
			\\coordinate ({A1}) at (0,0)   node at ({A1}) [left] {{${A1}$}};\n\
			\\coordinate ({B1}) at (1,-2) node at ({B1}) [left] {{${B1}$}};\n\
			\\coordinate ({C1}) at (4,0)   node at ({C1}) [right] {{${C1}$}};\n\
			\\coordinate ({M1}) at (2.5,-1)   node at ({M1}) [below right] {{${M1}$}};\n\
			\\coordinate ({S1}) at (0,4)   node at ({S1}) [above] {{${S1}$}};\n\
			\\coordinate ({H1}) at (1.25,1.5)   node at ({H1}) [above right] {{${H1}$}};\n\
			\\draw [dashed] ({A1})--({C1}) ; \n\
			\\draw ({A1})--({B1}) ({B1})--({C1}) ({S1})--({A1}) ({S1})--({B1}) ({S1})--({C1}); \n\
			\\draw ({S1})--({M1}); \n\
			\\draw [dashed] ({A1})--({M1}) ({A1})--({H1}) ; \n\
			\\end{{tikzpicture}}\n"
		code = my_module.moi_truong_anh_latex(code_hinhloigiai)
		file_name_loigiai = my_module.pdftoimage_timename(code)

		noi_dung_loigiai=f" Ta có: ${{{B1}{C1}\\bot {A1}{M1}}}$ và ${{{B1}{C1}\\bot S{A1}}}$"\
						f" (Do $S{A1}\\bot (ABC))$ nên ${B1}{C1}\\bot (S{A1}{M1})$.\n\nSuy ra ${A1}{H1}\\bot {B1}{C1}\\subset (S{B1}{C1})$."\
						f" Theo giả thiết ta có: ${A1}{H1} \\bot S{M1} \\subset (S{B1}{C1})$. \n\n"\
						f"Suy ra ${A1}{H1}\\bot (S{B1}{C1})$."\
						f" Vì ${duong_2}\\subset (S{B1}{C1})$ nên ${A1}{H1}\\bot {duong_2}$."	

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n\n {file_name_loigiai} Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n\n \\begin{{center}}\n {code_hinhloigiai} \\end{{center}}\n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_08]-TF-M2. S.ABCD: cạnh v.g đáy h.vuông. Xét tính đúng sai về đường vuông góc đường 
def uvxy9_L11_C8_B2_08():
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	

	kq1_T=f"*Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{C1}}}$ vuông góc nhau"
	kq1_F=f"Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{C1}}}$ không vuông góc"
	loigiai_1=f"Do $S{A1}\\bot (ABCD)$ và ${B1}{C1}\\subset (ABCD)$ nên ${{S{A1}}} \\bot {{{B1}{C1}}}$."

	kq2_T=f"*Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{D1}}}$ vuông góc nhau"
	kq2_F=f"Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{D1}}}$ không vuông góc"
	loigiai_2=f"Do $S{A1}\\bot (ABCD)$ và ${B1}{D1}\\subset (ABCD)$ nên ${{S{A1}}} \\bot {{{B1}{D1}}}$."

	kq3_T=f"*Hai đường thẳng ${{{C1}{D1}}}$ và ${{S{D1}}}$ vuông góc nhau"
	kq3_F=f"Hai đường thẳng ${{{C1}{D1}}}$ và ${{S{D1}}}$ không vuông góc"
	loigiai_3=f"Do ${C1}{D1}\\bot {A1}{D1}$ và ${C1}{D1}\\bot S{A1}$ nên ${C1}{D1}\\bot (S{A1}{D1}) \\Rightarrow {C1}{D1} \\bot S{D1}$."

	kq4_T=f"*Hai đường thẳng ${{{B1}{D1}}}$ và ${{S{C1}}}$ vuông góc nhau"
	kq4_F=f"Hai đường thẳng ${{{B1}{D1}}}$ và ${{S{C1}}}$ không vuông góc"
	loigiai_4=f"Do ${B1}{D1} \\bot {A1}{C1}$ và ${B1}{D1}\\bot S{A1}$ nên ${{{B1}{D1}}} \\bot (S{A1}{C1}) \\Rightarrow {B1}{D1} \\bot S{C1}$."
	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
				
	noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Xét tính đúng sai của các khẳng định sau?\n\n"		
	
	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"\
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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
	f"b) {loigiai[1]}\\\\ \n"\
	f"c) {loigiai[2]}\\\\ \n"\
	f"d) {loigiai[3]}\\\\ \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
	f"\\begin{{center}}\n{code_hinh}\\end{{center}}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"	
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B2_09]-TF-M2. S.ABCD: cạnh v.g đáy h.vuông. Tạo câu đúng-sai: đường vuông góc mặt.
def uvxy9_L11_C8_B2_09():
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	

	kq1_T=f"*Đường thẳng ${{S{A1}}}$ không vuông góc với mặt phẳng ${{(S{C1}{D1})}}$"
	kq1_F=f"Đường thẳng ${{S{A1}}}$ vuông góc với mặt phẳng ${{(S{C1}{D1})}}$"
	loigiai_1=f"Nếu $S{A1}\\bot {{(S{C1}{D1})}}$ thì ${{S{A1}}} \\bot {{S{D1}}}$ (vô lí). Do đó ${{S{A1}}}$ không vuông góc với mặt phẳng ${{(S{C1}{D1})}}$."

	kq2_T=f"*Đường thẳng ${{{B1}{C1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
	kq2_F=f"Đường thẳng ${{{B1}{C1}}}$ vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
	loigiai_2=f"Do ${{{B1}{A1}}}$ không vuông góc với ${{{A1}{C1}}}$ nên ${{{B1}{C1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$."

	t_3=random.randint(1,2)
	if t_3==1:
		kq3_T=f"*Đường thẳng ${{{C1}{D1}}}$ vuông góc với mặt phẳng ${{(S{A1}{D1})}}$"
		kq3_F=f"Đường thẳng ${{{C1}{D1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{D1})}}$"
		loigiai_3=f"Do ${C1}{D1}\\bot {A1}{D1}$ và ${C1}{D1}\\bot S{A1}$ nên ${C1}{D1}\\bot (S{A1}{D1})$."
	if t_3==2:
		kq3_T=f"*Đường thẳng ${{{B1}{C1}}}$ vuông góc với mặt phẳng ${{(S{A1}{B1})}}$"
		kq3_F=f"Đường thẳng ${{{B1}{C1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{B1})}}$"
		loigiai_3=f"Do ${B1}{C1}\\bot {A1}{B1}$ và ${B1}{C1}\\bot S{A1}$ nên ${B1}{C1}\\bot (S{A1}{B1})$."

	kq4_T=f"*Đường thẳng ${{{B1}{D1}}}$ vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
	kq4_F=f"Đường thẳng ${{{B1}{D1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
	loigiai_4=f"Do ${B1}{D1}\\bot {A1}{C1}$ và ${B1}{D1}\\bot S{A1}$ nên ${{{B1}{D1}}} \\bot (S{A1}{C1})$."
	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
				
	noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Xét tính đúng sai của các khẳng định sau?\n\n"		
	
	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"\
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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
	f"b) {loigiai[1]}\\\\ \n"\
	f"c) {loigiai[2]}\\\\ \n"\
	f"d) {loigiai[3]}\\\\ \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
	f"\\begin{{center}}\n{code_hinh}\\end{{center}}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"	
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B2_10]-TF-M2. S.ABCD: cạnh v.g đáy h.chữ nhật. Tạo câu đúng-sai: đường vuông góc đường 
def uvxy9_L11_C8_B2_10():
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	

	kq1_T=f"*Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{C1}}}$ vuông góc nhau"
	kq1_F=f"Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{C1}}}$ không vuông góc"
	loigiai_1=f"Do $S{A1}\\bot (ABCD)$ và ${B1}{C1}\\subset (ABCD)$ nên ${{S{A1}}} \\bot {{{B1}{C1}}}$."

	kq2_T=f"*Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{D1}}}$ vuông góc nhau"
	kq2_F=f"Hai đường thẳng ${{S{A1}}}$ và ${{{B1}{D1}}}$ không vuông góc"
	loigiai_2=f"Do $S{A1}\\bot (ABCD)$ và ${B1}{D1}\\subset (ABCD)$ nên ${{S{A1}}} \\bot {{{B1}{D1}}}$."

	kq3_T=f"*Hai đường thẳng ${{{C1}{D1}}}$ và ${{S{D1}}}$ vuông góc nhau"
	kq3_F=f"Hai đường thẳng ${{{C1}{D1}}}$ và ${{S{D1}}}$ không vuông góc"
	loigiai_3=f"Do ${C1}{D1}\\bot {A1}{D1}$ và ${C1}{D1}\\bot S{A1}$ nên ${C1}{D1}\\bot (S{A1}{D1}) \\Rightarrow {C1}{D1} \\bot S{D1}$."

	kq4_T=f"*Hai đường thẳng ${{{B1}{D1}}}$ và ${{S{C1}}}$ không vuông góc"
	kq4_F=f"Hai đường thẳng ${{{B1}{D1}}}$ và ${{S{C1}}}$ vuông góc nhau"
	loigiai_4=f"Do ${B1}{D1} \\bot {A1}{C1}$ nên nếu ${B1}{D1}\\bot S{C1}$ thì ${{{B1}{D1}}} \\bot (S{A1}{C1})$ suy ra ${B1}{D1} \\bot {A1}{C1}$(vô lí). Do đó hai đường thẳng ${{{B1}{D1}}}$ và ${{S{C1}}}$ không vuông góc."
	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
				
	noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Xét tính đúng sai của các khẳng định sau?\n\n"		
	
	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"\
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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
	f"b) {loigiai[1]}\\\\ \n"\
	f"c) {loigiai[2]}\\\\ \n"\
	f"d) {loigiai[3]}\\\\ \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
	f"\\begin{{center}}\n{code_hinh}\\end{{center}}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"	
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B2_11]-TF-M2. S.ABCD: cạnh v.g đáy h.chữ nhật. Tạo câu đúng-sai: đường vuông góc mặt.
def uvxy9_L11_C8_B2_11():
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	

	kq1_T=f"*Đường thẳng ${{S{A1}}}$ không vuông góc với mặt phẳng ${{(S{C1}{D1})}}$"
	kq1_F=f"Đường thẳng ${{S{A1}}}$ vuông góc với mặt phẳng ${{(S{C1}{D1})}}$"
	loigiai_1=f"Nếu $S{A1}\\bot {{(S{C1}{D1})}}$ thì ${{S{A1}}} \\bot {{S{D1}}}$ (vô lí). Do đó ${{S{A1}}}$ không vuông góc với mặt phẳng ${{(S{C1}{D1})}}$."

	kq2_T=f"*Đường thẳng ${{{B1}{C1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
	kq2_F=f"Đường thẳng ${{{B1}{C1}}}$ vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
	loigiai_2=f"Do ${{{B1}{A1}}}$ không vuông góc với ${{{A1}{C1}}}$ nên ${{{B1}{C1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$."

	t_3=random.randint(1,2)
	if t_3==1:
		kq3_T=f"*Đường thẳng ${{{C1}{D1}}}$ vuông góc với mặt phẳng ${{(S{A1}{D1})}}$"
		kq3_F=f"Đường thẳng ${{{C1}{D1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{D1})}}$"
		loigiai_3=f"Do ${C1}{D1}\\bot {A1}{D1}$ và ${C1}{D1}\\bot S{A1}$ nên ${C1}{D1}\\bot (S{A1}{D1})$."
	if t_3==2:
		kq3_T=f"*Đường thẳng ${{{B1}{C1}}}$ vuông góc với mặt phẳng ${{(S{A1}{B1})}}$"
		kq3_F=f"Đường thẳng ${{{B1}{C1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{B1})}}$"
		loigiai_3=f"Do ${B1}{C1}\\bot {A1}{B1}$ và ${B1}{C1}\\bot S{A1}$ nên ${B1}{C1}\\bot (S{A1}{B1})$."

	t_4=random.randint(1,2)
	if t_4==1:
		kq4_T=f"*Đường thẳng ${{{B1}{D1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
		kq4_F=f"Đường thẳng ${{{B1}{D1}}}$ vuông góc với mặt phẳng ${{(S{A1}{C1})}}$"
		loigiai_4=f"Nếu ${B1}{D1}\\bot {{(S{A1}{C1})}}$ thì ${{{B1}{D1}}} \\bot {{{A1}{D1}}}$ (vô lí). Do đó ${{{B1}{D1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$."
	if t_4==2:
		kq4_T=f"*Đường thẳng ${{{B1}{D1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{B1})}}$"
		kq4_F=f"Đường thẳng ${{{B1}{D1}}}$ vuông góc với mặt phẳng ${{(S{A1}{B1})}}$"
		loigiai_4=f"Nếu ${B1}{D1}\\bot {{(S{A1}{B1})}}$ thì ${{{B1}{D1}}} \\bot {{{A1}{B1}}}$ (vô lí). Do đó ${{{B1}{D1}}}$ không vuông góc với mặt phẳng ${{(S{A1}{C1})}}$."

	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
				
	noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Xét tính đúng sai của các khẳng định sau?\n\n"		
	
	kq1=random.choice([kq1_T, kq1_F])
	kq2=random.choice([kq2_T, kq2_F])
	kq3=random.choice([kq3_T, kq3_F])
	kq4=random.choice([kq4_T, kq4_F])	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"\
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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
	f"b) {loigiai[1]}\\\\ \n"\
	f"c) {loigiai[2]}\\\\ \n"\
	f"d) {loigiai[3]}\\\\ \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
	f"\\begin{{center}}\n{code_hinh}\\end{{center}}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"	
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B2_12]-TF-M2. S.ABCD: cạnh v.g đáy h.vuông. Tạo câu đúng-sai: lập luận đường vuông góc mặt.
def uvxy9_L11_C8_B2_12():
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	

	kq1_T=f"*Vì ${C1}{D1}\\bot {A1}{D1}$ và ${C1}{D1}\\bot S{A1}$ (do $S{A1}\\bot (ABCD))$ nên ${C1}{D1}\\bot (S{A1}{D1})$"
	kq1_F=f"Vì ${C1}{D1}\\bot {A1}{D1}$ nên ${C1}{D1}\\bot (S{A1}{D1})$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Vì ${C1}{D1}\\bot {A1}{D1}$ và ${C1}{D1}\\bot S{A1}$ (do $S{A1}\\bot (ABCD))$ nên ${C1}{D1}\\bot (S{A1}{D1})$ là lập luận đúng."

	kq2_T=f"*Vì ${B1}{D1}\\bot {A1}{C1}$ và ${B1}{D1}\\bot S{A1}$ (do $S{A1}\\bot (ABCD))$ nên ${B1}{D1}\\bot (S{A1}{C1})$"
	kq2_F=f"Vì ${B1}{D1}\\bot {A1}{C1}$ nên ${B1}{D1}\\bot (S{A1}{C1})$"
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Vì ${B1}{D1}\\bot {A1}{C1}$ và ${B1}{D1}\\bot S{A1}$ (do $S{A1}\\bot (ABCD))$ nên ${B1}{D1}\\bot (S{A1}{C1})$ là lập luận đúng."

	t_3=random.randint(1,2)
	if t_3==1:
		kq3_T=f"*Vì ${{{B1}{C1}}}$ không vuông góc với ${{{B1}{D1}}}$ nên ${{{B1}{C1}}}$ không vuông góc với ${{(S{B1}{D1})}}$"
		kq3_F=f"Vì ${{{B1}{C1}}}$ không vuông góc với ${{{B1}{D1}}}$ nên ${{{B1}{C1}}}$ vuông góc với ${{(S{B1}{D1})}}$"
		kq3=random.choice([kq3_T, kq3_F])
		if kq3==kq3_T:
			loigiai_3=f"Vì ${{{B1}{C1}}}$ không vuông góc với ${{{B1}{D1}}}$ nên ${{{B1}{C1}}}$ không vuông góc với ${{(S{B1}{D1})}}$ là lập luận đúng."
		if kq3==kq3_F:
			loigiai_3=f"ì ${{{B1}{C1}}}$ không vuông góc với ${{{B1}{D1}}}$ nên ${{{B1}{C1}}}$ vuông góc với ${{(S{B1}{D1})}}$ là lập luận sai."
	if t_3==2:
		kq3_T=f"*Vì ${{{B1}{D1}}}$ không vuông góc với ${{{A1}{B1}}}$ nên ${{{B1}{D1}}}$ không vuông góc với ${{(S{A1}{B1})}}$"
		kq3_F=f"Vì ${{{B1}{D1}}}$ không vuông góc với ${{(S{A1}{B1}}}$ nên ${{{B1}{C1}}}$ không vuông góc với ${{S{A1}}}$"
		kq3=random.choice([kq3_T, kq3_F])
		if kq3==kq3_T:
			loigiai_3=f"Vì ${{{B1}{D1}}}$ không vuông góc với ${{{A1}{B1}}}$ nên ${{{B1}{D1}}}$ không vuông góc với ${{(S{A1}{B1})}}$ là lập luận đúng."
		if kq3==kq3_F:
			loigiai_3=f"Vì ${{{B1}{D1}}}$ không vuông góc với ${{(S{A1}{B1}}}$ nên ${{{B1}{C1}}}$ không vuông góc với ${{S{A1}}}$ là lập luận sai."
	
	
	kq4_T=f"*Vì ${{{A1}{C1}}}$ không vuông góc với ${{{C1}{D1}}}$ nên ${{{A1}{C1}}}$ không vuông góc với ${{(S{C1}{D1})}}$"
	kq4_F=f"Vì ${{{A1}{C1}}}$ vuông góc với ${{{B1}{D1}}}$ nên ${{{A1}{C1}}}$ vuông góc với ${{(S{B1}{D1})}}$"
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Vì ${{{A1}{C1}}}$ không vuông góc với ${{{C1}{D1}}}$ nên ${{{A1}{C1}}}$ không vuông góc với ${{(S{C1}{D1})}}$ là lập luận đúng."
	if kq4==kq4_F:
		loigiai_4=f"Vì ${{{A1}{C1}}}$ vuông góc với ${{{B1}{D1}}}$ nên ${{{A1}{C1}}}$ vuông góc với ${{(S{B1}{D1})}}$ là lập luận sai."
	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
				
	noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Xét tính đúng sai của các khẳng định sau?\n\n"		
	
	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"\
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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
	f"b) {loigiai[1]}\\\\ \n"\
	f"c) {loigiai[2]}\\\\ \n"\
	f"d) {loigiai[3]}\\\\ \n"

	#Tạo đề latex
	for i in range(len(list_PA)):
 		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
	f"\\begin{{center}}\n{code_hinh}\\end{{center}}\n"\
		f"\\choiceTF\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"	
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B2_13]-M2. S.ABCD: cạnh v.g đáy h.vuông. Tìm hình chiếu của điểm trên mặt phẳng.
def uvxy9_L11_C8_B2_13(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,8)

	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{Q1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{D1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{A1}}}$"
		kq2= f"Điểm ${{{B1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{Q1}}}$"
		noi_dung_loigiai=f"${D1}{A1}\\bot {A1}{B1},{D1}{A1}\\bot S{A1} \\Rightarrow {D1}{A1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{{D1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{A1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{D1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{M1}}}$"
		noi_dung_loigiai=f"${C1}{D1}\\bot {A1}{D1},{C1}{A1}\\bot S{A1} \\Rightarrow {C1}{D1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{D1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{Q1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{B1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{Q1}}}$"
		noi_dung_loigiai=f"${C1}{B1}\\bot {A1}{B1},{C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{B1}}}$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{A1}}}$"
		kq2= f"Điểm ${{{D1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{M1}}}$"
		noi_dung_loigiai=f"${B1}{A1}\\bot {A1}{D1},{B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{A1}}}$."

	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{M1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{D1}}}$"
		noi_dung_loigiai=f"$O{M1}\\bot {A1}{D1},O{M1}\\bot S{A1} \\Rightarrow O{M1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{M1}}}$."

	if chon==6:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{Q1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{Q1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{B1}}}$"
		noi_dung_loigiai=f"$O{Q1}\\bot {A1}{B1},O{Q1}\\bot S{A1} \\Rightarrow O{Q1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{Q1}}}$."

	if chon==7:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của ${{{A1}{D1}}}, {{{B1}{C1}}}$."\
		f" Tìm hình chiếu của điểm ${{{N1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{M1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{D1}}}$"
		noi_dung_loigiai=f"${N1}{M1}\\bot {A1}{D1},{N1}{M1}\\bot S{A1} \\Rightarrow {N1}{M1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{N1}}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{M1}}}$."

	if chon==8:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{P1},{Q1}}}$ lần lượt là trung điểm của ${{{C1}{D1}}}, {{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{P1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{Q1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{B1}}}$"
		noi_dung_loigiai=f"${P1}{Q1}\\bot {A1}{B1},{P1}{Q1}\\bot S{A1} \\Rightarrow {P1}{Q1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{P1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{Q1}}}$."

	if chon==9:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{P1},{Q1}}}$ lần lượt là trung điểm của ${{{C1}{D1}}}, {{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$?"
		kq= f"Điểm ${{O}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f'Điểm ${{{random.choice(["C1","D1",f"{P1}",f"{Q1}"])}}}$'
		noi_dung_loigiai=f"${B1}O\\bot {A1}{C1},{B1}O\\bot S{A1} \\Rightarrow {B1}O\\bot (S{A1}{C1})$."\
		f" Do đó hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$ là điểm ${{O}}$."

	if chon==10:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{P1},{Q1}}}$ lần lượt là trung điểm của ${{{C1}{D1}}}, {{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{D1}}}$ trên mặt phẳng $(S{A1}{C1})$?"
		kq= f"Điểm ${{O}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f'Điểm ${{{random.choice(["C1","D1",f"{P1}",f"{Q1}"])}}}$'
		noi_dung_loigiai=f"${D1}O\\bot {A1}{C1},{D1}O\\bot S{A1} \\Rightarrow {D1}O\\bot (S{A1}{C1})$."\
		f" Do đó hình chiếu của điểm ${{{D1}}}$ trên mặt phẳng $(S{A1}{C1})$ là điểm ${{O}}$."


    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_14]-M2. S.ABCD: cạnh v.g đáy h.chữ nhật. Tìm hình chiếu của điểm trên mặt phẳng.
def uvxy9_L11_C8_B2_14(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,8)

	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{Q1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{D1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{A1}}}$"
		kq2= f"Điểm ${{{B1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{Q1}}}$"
		noi_dung_loigiai=f"${D1}{A1}\\bot {A1}{B1},{D1}{A1}\\bot S{A1} \\Rightarrow {D1}{A1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{{D1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{A1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{D1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{M1}}}$"
		noi_dung_loigiai=f"${C1}{D1}\\bot {A1}{D1},{C1}{A1}\\bot S{A1} \\Rightarrow {C1}{D1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{D1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{Q1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{B1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{Q1}}}$"
		noi_dung_loigiai=f"${C1}{B1}\\bot {A1}{B1},{C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{B1}}}$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{A1}}}$"
		kq2= f"Điểm ${{{D1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{M1}}}$"
		noi_dung_loigiai=f"${B1}{A1}\\bot {A1}{D1},{B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{A1}}}$."

	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{M1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{D1}}}$"
		noi_dung_loigiai=f"$O{M1}\\bot {A1}{D1},O{M1}\\bot S{A1} \\Rightarrow O{M1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{M1}}}$."

	if chon==6:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{Q1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{Q1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{B1}}}$"
		noi_dung_loigiai=f"$O{Q1}\\bot {A1}{B1},O{Q1}\\bot S{A1} \\Rightarrow O{Q1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{Q1}}}$."

	if chon==7:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của ${{{A1}{D1}}}, {{{B1}{C1}}}$."\
		f" Tìm hình chiếu của điểm ${{{N1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"Điểm ${{{M1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{D1}}}$"
		noi_dung_loigiai=f"${N1}{M1}\\bot {A1}{D1},{N1}{M1}\\bot S{A1} \\Rightarrow {N1}{M1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{N1}}}$ trên mặt phẳng $(S{A1}{D1})$ là điểm ${{{M1}}}$."

	if chon==8:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{P1},{Q1}}}$ lần lượt là trung điểm của ${{{C1}{D1}}}, {{{A1}{B1}}}$."\
		f" Tìm hình chiếu của điểm ${{{P1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"Điểm ${{{Q1}}}$"
		kq2= f"Điểm ${{{A1}}}$"
		kq3= f"Điểm ${{S}}$"
		kq4= f"Điểm ${{{B1}}}$"
		noi_dung_loigiai=f"${P1}{Q1}\\bot {A1}{B1},{P1}{Q1}\\bot S{A1} \\Rightarrow {P1}{Q1}\\bot (S{A1}{D1})$."\
		f" Do đó hình chiếu của điểm ${{{P1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{Q1}}}$."


    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_15]-M2. S.ABC: đáy tam giác vuông. Tìm hình chiếu của điểm lên mặt
def uvxy9_L11_C8_B2_15(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]

	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])
	chon_tamgiac=random.choice(["vuông", "đều"])

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	chon_tamgiac="vuông"
	if chon_tamgiac=="vuông":
		chon=random.randint(1,4)
		if chon==1:
			noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{B1}}}$, $S{A1}\\bot (ABC)$. Gọi ${{{M1}}}$ là hình chiếu vuông góc của điểm ${{{B1}}}$ trên đường thẳng ${{{A1}{C1}}}$."\
			f"Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$. Tìm hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
			kq=f"Điểm ${{{B1}}}$"
			kq2=f"Điểm ${{{A1}}}$"
			kq3=f'Điểm ${{{random.choice([f"{M1}", f"{{S}}"])}}}$'
			kq4=f"Điểm ${{{N1}}}$"
			noi_dung_loigiai=f"${C1}{B1}\\bot {A1}{B1},{C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{B1}}}$."

		if chon==2:
			noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{B1}}}$, $S{A1}\\bot (ABC)$. Gọi ${{{M1}}}$ là hình chiếu vuông góc của điểm ${{{B1}}}$ trên đường thẳng ${{{A1}{C1}}}$."\
			f"Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$. Tìm hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$?"
			kq=f"Điểm ${{{M1}}}$"
			kq2=f"Điểm ${{{A1}}}$"
			kq3=f'Điểm ${{{random.choice([f"{N1}", f"{{S}}"])}}}$'
			kq4=f"Điểm ${{{C1}}}$"
			noi_dung_loigiai=f"${B1}{M1}\\bot {A1}{C1},{B1}{M1}\\bot S{A1} \\Rightarrow {B1}{M1}\\bot (S{A1}{C1})$."\
		f" Do đó hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$ là điểm ${{{M1}}}$."

		if chon==3:
			noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông cân tại ${{{C1}}}$, $S{A1}\\bot (ABC)$. Gọi ${{{M1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$."\
			f"Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{C1}}}$. Tìm hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$?"
			kq=f"Điểm ${{{C1}}}$"
			kq2=f"Điểm ${{{A1}}}$"
			kq3=f"Điểm ${{{M1}}}$"
			kq4=f'Điểm ${{{random.choice([f"{N1}"])}}}$'
			noi_dung_loigiai=f"${B1}{M1}\\bot {A1}{C1},{B1}{M1}\\bot S{A1} \\Rightarrow {B1}{M1}\\bot (S{A1}{C1})$."\
		f" Do đó hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$ là điểm ${{{M1}}}$."

		if chon==4:
			noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông cân tại ${{{C1}}}$, $S{A1}\\bot (ABC)$. Gọi ${{{M1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$."\
			f"Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{C1}}}$. Tìm hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
			kq=f"Điểm ${{{M1}}}$"
			kq2=f"Điểm ${{{A1}}}$"
			kq3=f"Điểm ${{S}}$"
			kq4=f'Điểm ${{{random.choice([f"{B1}",f"{N1}"])}}}$'
			noi_dung_loigiai=f"${C1}{M1}\\bot {A1}{B1},{C1}{M1}\\bot S{A1} \\Rightarrow {C1}{M1}\\bot (S{A1}{B1})$."\
		f" Do đó hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{M1}}}$."
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	


	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_16]-M2. S.ABC: đáy tam giác đều. Tìm hình chiếu của điểm lên mặt
def uvxy9_L11_C8_B2_16(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]

	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])
	chon_tamgiac=random.choice(["vuông", "đều"])

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)


	chon=random.randint(1,2)
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${A1}{B1}$ và ${A1}{C1}$."\
		f"Tìm hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq=f"Điểm ${{{M1}}}$"
		kq2=f"Điểm ${{{A1}}}$"
		kq3=f"Điểm ${{S}}$"
		kq4=f'Điểm ${{{random.choice([f"{B1}", f"{N1}"])}}}$'
		noi_dung_loigiai=f"${C1}{M1}\\bot {A1}{B1},{C1}{M1}\\bot S{A1} \\Rightarrow {C1}{M1}\\bot (S{A1}{B1})$."\
	f" Do đó hình chiếu của điểm ${{{C1}}}$ trên mặt phẳng $(S{A1}{B1})$ là điểm ${{{M1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${A1}{B1}$ và ${A1}{C1}$."\
		f"Tìm hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$?"
		kq=f"Điểm ${{{N1}}}$"
		kq2=f"Điểm ${{{A1}}}$"
		kq3=f"Điểm ${{S}}$"
		kq4=f'Điểm ${{{random.choice([f"{C1}", f"{M1}"])}}}$'
		noi_dung_loigiai=f"${B1}{N1}\\bot {A1}{C1},{B1}{N1}\\bot S{A1} \\Rightarrow {B1}{N1}\\bot (S{A1}{C1})$."\
	f" Do đó hình chiếu của điểm ${{{B1}}}$ trên mặt phẳng $(S{A1}{C1})$ là điểm ${{{N1}}}$."

			
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	


	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_17]-M3. S.ABCD: cạnh v.g đáy h.vuông. Tìm hình chiếu của điểm trên mặt phẳng.
def uvxy9_L11_C8_B2_17(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]	

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "H"])
	P1=random.choice(["P", "G", "K"])
	chon=random.randint(1,5)
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{C1}{D1}}}$."\
		f" Gọi ${{{N1},{P1}}}$ lần lượt là hình chiếu của điểm ${{{A1}}}$ trên các đường thẳng $S{{{D1}}}$ và $S{{{M1}}}$."\
		f" Tìm hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{C1}{D1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{C1}}}$"
		kq3= f"Điểm ${{{D1}}}$"
		kq4= f'Điểm ${{{random.choice([f"{P1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{N1}\\bot S{D1}$ (theo giả thiết)."\
		f" Do ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1}\\bot (S{A1}{D1}) \\Rightarrow {C1}{D1} \\bot {A1}{N1}$.\n\n"\
		f"Suy ra ${A1}{N1} \\bot (S{C1}{D1})$. Do đó hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{C1}{D1})$ là điểm ${{{N1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{B1}{C1}}}$."\
		f" Gọi ${{{N1},{P1}}}$ lần lượt là hình chiếu của điểm ${{{A1}}}$ trên các đường thẳng $S{{{B1}}}$ và $S{{{M1}}}$."\
		f" Tìm hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{C1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{C1}}}$"
		kq3= f"Điểm ${{{B1}}}$"
		kq4= f'Điểm ${{{random.choice([f"{P1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{N1}\\bot S{B1}$ (theo giả thiết)."\
		f" Do ${B1}{C1}\\bot {A1}{B1},{B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1}\\bot (S{A1}{B1}) \\Rightarrow {B1}{C1} \\bot {A1}{N1}$.\n\n"\
		f"Suy ra ${A1}{N1} \\bot (S{B1}{C1})$. Do đó hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{C1})$ là điểm ${{{N1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1},{P1}}}$ lần lượt là hình chiếu của ${{{A1}}}$ trên các đường thẳng $SO,S{{{B1}}},S{{{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{D1})$?"
		kq= f"Điểm ${{{M1}}}$"
		kq2= f"Điểm ${{{N1}}}$"
		kq3= f"Điểm ${{{P1}}}$"
		kq4= f'Điểm ${{{random.choice([f"O","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{M1}\\bot SO$ (theo giả thiết)."\
		f" Do ${B1}{D1}\\bot {A1}{C1},{B1}{D1}\\bot S{A1} \\Rightarrow {B1}{D1}\\bot (S{A1}{C1}) \\Rightarrow {B1}{D1} \\bot SO$.\n\n"\
		f"Suy ra ${A1}{M1} \\bot (S{B1}{D1})$. Do đó hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{D1})$ là điểm ${{{M1}}}$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là hình chiếu của ${{{A1}}}$ trên đường thẳng $S{{{D1}}}$."\
		f" Gọi ${{{N1}}}$ là trung điểm của đoạn thẳng ${{{C1}{M1}}}$. Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{C1}{D1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{M1}}}$"
		kq3= f'Điểm ${{{random.choice([f"{C1}", f"{B1}"])}}}$'
		kq4= f'Điểm ${{{random.choice([f"{D1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{M1}\\bot SO$ (theo giả thiết)."\
		f" Do ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1}\\bot (S{A1}{D1}) \\Rightarrow {C1}{D1} \\bot {A1}{M1}$.\n\n"\
		f"Suy ra ${A1}{M1} \\bot (S{C1}{D1})$. Vì $O{N1}$ song song với ${A1}{M1}$ nên $O{N1} \\bot (S{C1}{D1})$. Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{C1}{D1})$ là điểm ${{{N1}}}$."

	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là hình chiếu của ${{{A1}}}$ trên đường thẳng $S{{{B1}}}$."\
		f" Gọi ${{{N1}}}$ là trung điểm của đoạn thẳng ${{{C1}{M1}}}$. Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{B1}{C1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{M1}}}$"
		kq3= f'Điểm ${{{random.choice([f"{C1}", f"{B1}"])}}}$'
		kq4= f'Điểm ${{{random.choice([f"{D1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{M1}\\bot SO$ (theo giả thiết)."\
		f" Do ${B1}{C1}\\bot {A1}{B1},{B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1}\\bot (S{A1}{B1}) \\Rightarrow {B1}{C1} \\bot {A1}{M1}$.\n\n"\
		f"Suy ra ${A1}{M1} \\bot (S{B1}{C1})$. Vì $O{N1}$ song song với ${A1}{M1}$ nên $O{N1} \\bot (S{B1}{C1})$. Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{B1}{C1})$ là điểm ${{{N1}}}$."
	

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_18]-M3. S.ABCD: cạnh v.g đáy h.chữ nhật. Tìm hình chiếu của điểm trên mặt phẳng.
def uvxy9_L11_C8_B2_18(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]	

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "H"])
	P1=random.choice(["P", "G", "K"])
	chon=random.randint(1,5)
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{C1}{D1}}}$."\
		f" Gọi ${{{N1},{P1}}}$ lần lượt là hình chiếu của điểm ${{{A1}}}$ trên các đường thẳng $S{{{D1}}}$ và $S{{{M1}}}$."\
		f" Tìm hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{C1}{D1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{C1}}}$"
		kq3= f"Điểm ${{{D1}}}$"
		kq4= f'Điểm ${{{random.choice([f"{P1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{N1}\\bot S{D1}$ (theo giả thiết)."\
		f" Do ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1}\\bot (S{A1}{D1}) \\Rightarrow {C1}{D1} \\bot {A1}{N1}$.\n\n"\
		f"Suy ra ${A1}{N1} \\bot (S{C1}{D1})$. Do đó hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{C1}{D1})$ là điểm ${{{N1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{B1}{C1}}}$."\
		f" Gọi ${{{N1},{P1}}}$ lần lượt là hình chiếu của điểm ${{{A1}}}$ trên các đường thẳng $S{{{B1}}}$ và $S{{{M1}}}$."\
		f" Tìm hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{C1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{C1}}}$"
		kq3= f"Điểm ${{{B1}}}$"
		kq4= f'Điểm ${{{random.choice([f"{P1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{N1}\\bot S{B1}$ (theo giả thiết)."\
		f" Do ${B1}{C1}\\bot {A1}{B1},{B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1}\\bot (S{A1}{B1}) \\Rightarrow {B1}{C1} \\bot {A1}{N1}$.\n\n"\
		f"Suy ra ${A1}{N1} \\bot (S{B1}{C1})$. Do đó hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{C1})$ là điểm ${{{N1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1},{P1}}}$ lần lượt là hình chiếu của ${{{A1}}}$ trên các đường thẳng $SO,S{{{B1}}},S{{{D1}}}$."\
		f" Tìm hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{D1})$?"
		kq= f"Điểm ${{{M1}}}$"
		kq2= f"Điểm ${{{N1}}}$"
		kq3= f"Điểm ${{{P1}}}$"
		kq4= f'Điểm ${{{random.choice([f"O","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{M1}\\bot SO$ (theo giả thiết)."\
		f" Do ${B1}{D1}\\bot {A1}{C1},{B1}{D1}\\bot S{A1} \\Rightarrow {B1}{D1}\\bot (S{A1}{C1}) \\Rightarrow {B1}{D1} \\bot SO$.\n\n"\
		f"Suy ra ${A1}{M1} \\bot (S{B1}{D1})$. Do đó hình chiếu của điểm ${{{A1}}}$ trên mặt phẳng $(S{B1}{D1})$ là điểm ${{{M1}}}$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là hình chiếu của ${{{A1}}}$ trên đường thẳng $S{{{D1}}}$."\
		f" Gọi ${{{N1}}}$ là hình chiếu của điểm ${{O}}$ trên đường thẳng ${{{C1}{M1}}}$. Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{C1}{D1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{M1}}}$"
		kq3= f'Điểm ${{{random.choice([f"{C1}", f"{B1}"])}}}$'
		kq4= f'Điểm ${{{random.choice([f"{D1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{M1}\\bot SO$ (theo giả thiết)."\
		f" Do ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1}\\bot (S{A1}{D1}) \\Rightarrow {C1}{D1} \\bot {A1}{M1}$.\n\n"\
		f"Suy ra ${A1}{M1} \\bot (S{C1}{D1})$. Vì $O{N1}$ song song với ${A1}{M1}$ nên $O{N1} \\bot (S{C1}{D1})$. Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{C1}{D1})$ là điểm ${{{N1}}}$."

	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là hình chiếu của ${{{A1}}}$ trên đường thẳng $S{{{B1}}}$."\
		f" Gọi ${{{N1}}}$ là hình chiếu của điểm ${{O}}$ trên đường thẳng ${{{C1}{M1}}}$. Tìm hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{B1}{C1})$?"
		kq= f"Điểm ${{{N1}}}$"
		kq2= f"Điểm ${{{M1}}}$"
		kq3= f'Điểm ${{{random.choice([f"{C1}", f"{B1}"])}}}$'
		kq4= f'Điểm ${{{random.choice([f"{D1}","S"])}}}$'
		noi_dung_loigiai=f"Ta có: ${A1}{M1}\\bot SO$ (theo giả thiết)."\
		f" Do ${B1}{C1}\\bot {A1}{B1},{B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1}\\bot (S{A1}{B1}) \\Rightarrow {B1}{C1} \\bot {A1}{M1}$.\n\n"\
		f"Suy ra ${A1}{M1} \\bot (S{B1}{C1})$. Vì $O{N1}$ song song với ${A1}{M1}$ nên $O{N1} \\bot (S{B1}{C1})$. Do đó hình chiếu của điểm ${{O}}$ trên mặt phẳng $(S{B1}{C1})$ là điểm ${{{N1}}}$."
	

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_19]-M1. S.ABCD: ABCD h.vuông. Tìm hình chiếu của đường thẳng trên mặt đáy.
def uvxy9_L11_C8_B2_19(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của đường thẳng ${{S{B1}}}$ trên mặt phẳng $(ABCD)$?"
		kq= f"${{{A1}{B1}}}$"
		kq2= f"${{{B1}{C1}}}$"
		kq3= random.choice([f"${{{C1}{D1}}}$",f"${{{M1}{C1}}}$"])
		kq4= random.choice([f"${{S{A1}}}$",f"${{S{M1}}}$", f"${{{B1}{D1}}}$"])
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{B1}}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{B1}}}$.\n\n"\
		f"Do đó hình chiếu của đường thẳng ${{S{B1}}}$ trên mặt phẳng $(ABCD)$ là ${{{A1}{B1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của đường thẳng ${{S{C1}}}$ trên mặt phẳng $(ABCD)$?"
		kq= f"${{{A1}{C1}}}$"
		kq2= f"${{{B1}{C1}}}$"
		kq3= random.choice([f"${{{C1}{D1}}}$",f"${{{M1}{C1}}}$"])
		kq4= random.choice([f"${{S{A1}}}$",f"${{S{M1}}}$", f"${{{B1}{D1}}}$"])
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{C1}}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{C1}}}$.\n\n"\
		f"Do đó hình chiếu của đường thẳng ${{S{C1}}}$ trên mặt phẳng $(ABCD)$ là ${{{A1}{C1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của đường thẳng ${{S{D1}}}$ trên mặt phẳng $(ABCD)$?"
		kq= f"${{{A1}{D1}}}$"
		kq2= f"${{{B1}{C1}}}$"
		kq3= random.choice([f"${{{C1}{D1}}}$",f"${{{M1}{D1}}}$"])
		kq4= random.choice([f"${{S{A1}}}$",f"${{S{M1}}}$", f"${{{B1}{D1}}}$"])
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{D1}}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{D1}}}$.\n\n"\
		f"Do đó hình chiếu của đường thẳng ${{S{D1}}}$ trên mặt phẳng $(ABCD)$ là ${{{A1}{D1}}}$."
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_20]-M2. S.ABCD: ABCD h.vuông. Tìm hình chiếu của đường thẳng trên mặt đứng.
def uvxy9_L11_C8_B2_20(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,4)

	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của đường thẳng ${{{A1}{C1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"${{{A1}{B1}}}$"
		kq2= f"${{{B1}{C1}}}$"
		kq3= random.choice([f"${{{C1}{D1}}}$",f"${{{M1}{C1}}}$"])
		kq4= random.choice([f"${{S{A1}}}$",f"${{S{M1}}}$", f"${{{B1}{D1}}}$"])
		noi_dung_loigiai=f"Điểm ${{{A1}}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{A1}}}$."\
		f" Vì ${{{C1}{B1}}}\\bot {A1}{B1},{{{C1}{B1}}}\\bot S{A1} \\Rightarrow {{{C1}{B1}}}\\bot (S{A1}{B1})$.\n\n"\
		f"Nên điểm ${{{C1}}}$ có hình chiếu trên $(S{A1}{B1})$ là điểm ${{{B1}}}$."\
		f" Do đó hình chiếu của đường thẳng ${{{A1}{C1}}}$ trên mặt phẳng $(S{A1}{B1})$ là ${{{A1}{B1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của đường thẳng ${{{A1}{C1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"${{{A1}{D1}}}$"
		kq2= random.choice([f"${{{B1}{C1}}}$",f"${{S{D1}}}$"])
		kq3= random.choice([f"${{{C1}{D1}}}$",f"${{{M1}{A1}}}$"])
		kq4= random.choice([f"${{S{A1}}}$",f"${{S{M1}}}$", f"${{{B1}{D1}}}$"])
		noi_dung_loigiai=f"Điểm ${{{A1}}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{A1}}}$."\
		f" Vì ${{{C1}{D1}}}\\bot {A1}{D1},{{{C1}{D1}}}\\bot S{A1} \\Rightarrow {{{C1}{D1}}}\\bot (S{A1}{D1})$.\n\n"\
		f"Nên điểm ${{{C1}}}$ có hình chiếu trên $(S{A1}{D1})$ là điểm ${{{D1}}}$."\
		f" Do đó hình chiếu của đường thẳng ${{{A1}{C1}}}$ trên mặt phẳng $(S{A1}{D1})$ là ${{{A1}{D1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{D1}}}$."\
		f" Tìm hình chiếu của đường thẳng ${{{B1}{D1}}}$ trên mặt phẳng $(S{A1}{D1})$?"
		kq= f"${{{A1}{D1}}}$"
		kq2= random.choice([f"${{{B1}{C1}}}$",f"${{S{D1}}}$"])
		kq3= random.choice([f"${{{C1}{D1}}}$",f"${{{M1}{B1}}}$"])
		kq4= random.choice([f"${{S{A1}}}$",f"${{S{M1}}}$", f"${{S{D1}}}$"])
		noi_dung_loigiai=f"Điểm ${{{D1}}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{D1}}}$."\
		f" Vì ${{{B1}{D1}}}\\bot {A1}{D1},{{{B1}{D1}}}\\bot S{A1} \\Rightarrow {{{B1}{D1}}}\\bot (S{A1}{D1})$.\n\n"\
		f"Nên điểm ${{{B1}}}$ có hình chiếu trên $(S{A1}{D1})$ là điểm ${{{A1}}}$."\
		f" Do đó hình chiếu của đường thẳng ${{{B1}{D1}}}$ trên mặt phẳng $(S{A1}{D1})$ là ${{{A1}{D1}}}$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1}}}$ là trung điểm của ${{{A1}{B1}}}$."\
		f" Tìm hình chiếu của đường thẳng ${{{B1}{D1}}}$ trên mặt phẳng $(S{A1}{B1})$?"
		kq= f"${{{A1}{B1}}}$"
		kq2= f"${{{B1}{C1}}}$"
		kq3= random.choice([f"${{{C1}{D1}}}$",f"${{{M1}{D1}}}$"])
		kq4= random.choice([f"${{S{A1}}}$",f"${{S{M1}}}$", f"${{S{B1}}}$"])
		noi_dung_loigiai=f"Điểm ${{{B1}}}$ có hình chiếu trên $(ABCD)$ là điểm ${{{B1}}}$."\
		f" Vì ${{{D1}{B1}}}\\bot {A1}{B1},{{{D1}{B1}}}\\bot S{A1} \\Rightarrow {{{D1}{B1}}}\\bot (S{A1}{B1})$.\n\n"\
		f"Nên điểm ${{{D1}}}$ có hình chiếu trên $(S{A1}{B1})$ là điểm ${{{A1}}}$."\
		f" Do đó hình chiếu của đường thẳng ${{{A1}{C1}}}$ trên mặt phẳng $(S{A1}{B1})$ là ${{{A1}{B1}}}$."	
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B2_21]-TF-M3. S.ABCD: ABCD h.vuông. Xét Đ-S: Hình chiếu của đường lên mặt, đường vuông góc đường, đường vuông góc mặt, góc giữa 2 đường
def uvxy9_L11_C8_B2_21(): 
	a=sp.symbols("a")  	
	A=["A","B","C","D", "C", "A"]
	B=["B","C","D","A", "D", "B"]
	C=["C","D","A","B", "E", "E"]
	D=["D","A","B","C", "F", "F"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]	

	ten=["M", "N", "K", "P", "Q", "G", "H", "I"]
	M,N,P,H,I,K=random.sample(ten,6)
	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A, B, C, D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	AB=random.randint(1,7)
	SA=random.randint(1,7)
	chon=random.randint(1,4)

	noi_dung = (f"Cho hình chóp ${{S.{A}{B}{C}{D}}}$ có $S{A}\\bot ({A}{B}{C}{D})$, đáy là hình vuông tâm ${{O}}$, ${A}{B}={latex(a*AB)},S{A}={latex(a*SA)}$."
	f" Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười):")		
	

	chon=random.randint(1,4)
	if chon==1:
		kq1_T=f"* Hình chiếu của đường thẳng ${{S{B}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${{{A}{B}}}$" 
		kq1_F=f"Hình chiếu của đường thẳng ${{S{B}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${random.choice([f"{{{A}{C}}}", f"{{{A}{D}}}", f"{{{B}{D}}}", f"{{{C}{D}}}"])}$"
		HDG=f"Hình chiếu của đường thẳng ${{S{B}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${{{A}{B}}}$."

	if chon==2:
		kq1_T=f"* Hình chiếu của đường thẳng ${{S{C}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${{{A}{C}}}$" 
		kq1_F=f"Hình chiếu của đường thẳng ${{S{C}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${random.choice([f"{{{A}{B}}}", f"{{{A}{D}}}", f"{{{B}{D}}}", f"{{{C}{D}}}"])}$"
		HDG=f"Hình chiếu của đường thẳng ${{S{C}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${{{A}{C}}}$."

	if chon==3:
		kq1_T=f"* Hình chiếu của đường thẳng ${{S{D}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${{{A}{D}}}$" 
		kq1_F=f"Hình chiếu của đường thẳng ${{S{C}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${random.choice([f"{{{A}{B}}}", f"{{{A}{D}}}", f"{{{B}{D}}}", f"{{{C}{D}}}"])}$"
		HDG=f"Hình chiếu của đường thẳng ${{S{C}}}$ trên mặt phẳng $({A}{B}{C}{D})$ là đường thẳng ${{{A}{C}}}$."

	if chon==4:
		kq1_T=f"* Hình chiếu của đường thẳng ${{{A}{C}}}$ trên mặt phẳng $(S{A}{B})$ là đường thẳng ${{{A}{B}}}$" 
		kq1_F=f"Hình chiếu của đường thẳng ${{{A}{C}}}$ trên mặt phẳng $(S{A}{B})$ là đường thẳng ${random.choice([f"{{S{B}}}", f"{{S{A}}}", f"{{{B}{C}}}", f"{{{C}{D}}}"])}$"
		HDG=f"Hình chiếu của đường thẳng ${{{A}{C}}}$ trên mặt phẳng $(S{A}{B})$ là đường thẳng ${{{A}{B}}}$."

	if chon==5:
		kq1_T=f"* Hình chiếu của đường thẳng ${{{A}{C}}}$ trên mặt phẳng $(S{A}{D})$ là đường thẳng ${{{A}{D}}}$" 
		kq1_F=f"Hình chiếu của đường thẳng ${{{A}{C}}}$ trên mặt phẳng $(S{A}{D})$ là đường thẳng ${random.choice([f"{{S{D}}}", f"{{S{A}}}", f"{{{B}{D}}}", f"{{{C}{D}}}"])}$"
		HDG=f"Hình chiếu của đường thẳng ${{{A}{C}}}$ trên mặt phẳng $(S{A}{D})$ là đường thẳng ${{{A}{D}}}$."

	if chon==6:
		kq1_T=f"* Hình chiếu của đường thẳng ${{{S}{B}}}$ trên mặt phẳng $(S{A}{C})$ là đường thẳng ${{SO}}$" 
		kq1_F=f"Hình chiếu của đường thẳng ${{{S}{B}}}$ trên mặt phẳng $(S{A}{C})$ là đường thẳng ${random.choice([f"{{{A}O", f"{{S{A}}}", f"{{{A}{C}}}", f"{{S{C}}}"])}$"
		HDG=f"Hình chiếu của đường thẳng ${{{S}{B}}}$ trên mặt phẳng $(S{A}{C})$ là đường thẳng ${{SO}}$."	
	
	
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,6)

	if chon==1:
		dt=random.choice([f"${{{B}{C}}}$", f"${{{B}{D}}}$", f"${{{C}{D}}}$"])
		kq2_T=f"* Hai đường thẳng ${{S{A}}}$ và {dt} vuông góc nhau"
		kq2_F=f"Hai đường thẳng ${{S{A}}}$ và {dt} không vuông góc nhau"
		HDG=f"Hai đường thẳng ${{S{A}}}$ và {dt} vuông góc nhau."
	
	if chon==2:
		dt_1=[f"${{{B}{C}}}$", f"${{{A}{D}}}$", f"${{{A}{C}}}$", f"${{{A}{C}}}$" ]
		dt_2=[f"${{S{D}}}$", f"${{S{C}}}$", f"${{S{B}}}$", f"${{S{D}}}$"]
		i=random.randint(0,3)
		dt_1,dt_2=dt_1[i],dt_2[i]
		kq2_T=f"* Hai đường thẳng {dt_1} và {dt_2} không vuông góc nhau"
		kq2_F=f"Hai đường thẳng {dt_1} và {dt_2} vuông góc nhau"
		HDG=f"Hai đường thẳng {dt_1} và {dt_2} không vuông góc nhau."

	if chon==3:
		kq2_T=f"* Hai đường thẳng ${{{B}{C}}}$ và ${{S{B}}}$ vuông góc nhau"
		kq2_F=f"Hai đường thẳng ${{{B}{C}}}$ và ${{S{B}}}$ không vuông góc nhau"
		HDG=(f"${B}{C}\\bot {A}{B}, {B}{C}\\bot S{A} \\Rightarrow {B}{C}\\bot (S{A}{B}) \\Rightarrow {B}{C}\\bot S{B}.$")

	if chon==4:
		kq2_T=f"* Hai đường thẳng ${{{B}{D}}}$ và ${{S{C}}}$ vuông góc nhau"
		kq2_F=f"Hai đường thẳng ${{{B}{D}}}$ và ${{S{C}}}$ không vuông góc nhau"
		HDG=(f"${B}{D}\\bot {A}{C}, {B}{D}\\bot S{A} \\Rightarrow {B}{D}\\bot (S{A}{C}) \\Rightarrow {B}{D}\\bot S{C}.$")

	if chon==5:
		kq2_T=f"* Hai đường thẳng ${{{C}{D}}}$ và ${{S{D}}}$ vuông góc nhau"
		kq2_F=f"Hai đường thẳng ${{{C}{D}}}$ và ${{S{D}}}$ không vuông góc nhau"
		HDG=(f"${C}{D}\\bot {A}{D}, {C}{D}\\bot S{A} \\Rightarrow {C}{D}\\bot (S{A}{D}) \\Rightarrow {C}{D}\\bot S{D}.$")

	if chon==6:
		kq2_T=f"* Hai đường thẳng ${{{A}{D}}}$ và ${{S{B}}}$ vuông góc nhau"
		kq2_F=f"Hai đường thẳng ${{{A}{D}}}$ và ${{S{B}}}$ không vuông góc nhau"
		HDG=(f"${A}{D}\\bot {A}{B}, {A}{D}\\bot S{A} \\Rightarrow {A}{D}\\bot (S{A}{B}) \\Rightarrow {A}{D}\\bot S{B}.$")	

	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	
	kq3_T=random.choice([
		f"* ${{{B}{C}}}\\bot (S{A}{B})$",
		f"* ${{{C}{D}}}\\bot (S{A}{D})$",
		f"* ${{{B}{D}}}\\bot (S{A}{C})$"])

	kq3_F=random.choice([
		f"${{{B}{C}}}\\bot (S{A}{C})$",
		f"${{{C}{D}}}\\bot (S{B}{D})$",
		f"${{{A}{C}}}\\bot (S{B}{C})$",])	
	kq3=random.choice([kq3_T, kq3_F])

	#HDG đúng:
	if kq3==f"* ${{{B}{C}}}\\bot (S{A}{B})$":	
		HDG=f"${B}{C}\\bot {A}{B},{B}{C}\\bot S{A}\\Rightarrow {B}{C}\\bot (S{A}{B})$."

	if kq3==f"* ${{{C}{D}}}\\bot (S{A}{D})$":	
		HDG=f"${C}{D}\\bot {A}{D},{C}{D}\\bot S{A}\\Rightarrow {C}{D}\\bot (S{A}{D})$."

	if kq3==f"* ${{{B}{D}}}\\bot (S{A}{C})$":	
		HDG=f"${B}{D}\\bot {A}{C},{B}{D}\\bot S{A}\\Rightarrow {B}{D}\\bot (S{A}{C})$."

	#HDG sai:
	if kq3==f"${{{B}{C}}}\\bot (S{A}{C})$":	
		HDG=f"Nếu ${B}{C}\\bot (S{A}{C})\\Rightarrow {B}{C} \\bot {A}{C}$ (vô lí)."

	if kq3==f"${{{C}{D}}}\\bot (S{B}{D})$":	
		HDG=f"Nếu ${C}{D}\\bot (S{B}{D})\\Rightarrow {C}{D} \\bot {B}{D}$ (vô lí)."

	if kq3==f"${{{A}{C}}}\\bot (S{B}{C})$":	
		HDG=f"Nếu ${A}{C}\\bot (S{B}{C})\\Rightarrow {A}{C} \\bot {B}{C}$ (vô lí)."

	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	AM=(SA*AB)/sqrt(SA**2+AB**2)
	AC=AB*sqrt(2)
	t=asin(AM/AC)
	goc=f"{round_half_up(math.degrees(t),1):.1f}".replace(".",",")
	goc_false=f"{round_half_up(math.degrees(t)+random.randint(1,3),1):.1f}".replace(".",",")

	chon=random.randint(1,4)
	
	if chon==1:
		kq4_T=(f"* Gọi ${{{M}}}$ là hình chiếu vuông góc của ${{{A}}}$ trên ${{S{B}}}$."
			f" Góc giữa hai đường thẳng ${A}{C}$ và ${M}{C}$ bằng ${goc}^\\circ$")

		kq4_F=(f"Gọi ${{{M}}}$ là hình chiếu vuông góc của ${{{A}}}$ trên ${{S{B}}}$."
			f" Góc giữa hai đường thẳng ${A}{C}$ và ${M}{C}$ bằng ${goc_false}^\\circ$") 
		
		HDG=(f"${A}{M}\\bot S{B}, {A}{M}\\bot {B}{C}$ (do ${B}{C} \\bot (S{A}{B})$) suy ra ${A}{M}\\bot {M}{C}$.\n\n"
			f"${A}{C}={latex(AC*a)}$.\n\n"
			f"${A}{M}=\\dfrac{{S{A}.{A}{B}}}{{\\sqrt{{S{A}^2+{A}{B}^2}}}} = \\dfrac{{{latex(SA*a)}.{latex(AB*a)}}}{{\\sqrt{{{latex((SA*a)**2)}+{latex((AB*a)**2)} }}}}={latex(nsimplify(AM)*a)}$.\n\n"
			f"$\\sin\\widehat{{{A}{C}{M}}}=\\dfrac{{{A}{M}}}{{{A}{C}}}={latex(nsimplify(AM/AC))}$"
			f"$\\Rightarrow \\widehat{{{A}{C}{M}}}={goc}^\\circ$."
			)
	
	if chon==2:
		kq4_T=(f"* Gọi ${{{M}}}$ là hình chiếu vuông góc của ${{{A}}}$ trên ${{S{D}}}$."
			f" Góc giữa hai đường thẳng ${{{A}{C}}}$ và ${{{M}{C}}}$ bằng ${goc}^\\circ$")

		kq4_F=(f"Gọi ${{{M}}}$ là hình chiếu vuông góc của ${{{A}}}$ trên ${{S{D}}}$."
			f" Góc giữa hai đường thẳng ${{{A}{C}}}$ và ${{{M}{C}}}$ bằng ${goc_false}^\\circ$") 
		
		HDG=(f"${A}{M}\\bot S{D}, {A}{M}\\bot {C}{D}$ (do ${C}{D} \\bot (S{A}{D})$) suy ra ${A}{M}\\bot {M}{C}$.\n\n"
			f"${A}{C}={latex(AC*a)}$.\n\n"
			f"${A}{M}=\\dfrac{{S{A}.{A}{D}}}{{\\sqrt{{S{A}^2+{A}{D}^2}}}} = \\dfrac{{{latex(SA*a)}.{latex(AB*a)}}}{{\\sqrt{{{latex((SA*a)**2)}+{latex((AB*a)**2)} }}}}={latex(nsimplify(AM)*a)}$.\n\n"
			f"$\\sin \\widehat{{{A}{C}{M}}}=\\dfrac{{{A}{M}}}{{{A}{C}}}={latex(nsimplify(AM/AC))}$"
			f"$\\Rightarrow \\widehat{{{A}{C}{M}}}={goc}^\\circ$."
			)
	AM=(SA*AB)/sqrt(SA**2+AB**2)
	AC=AB*sqrt(2)
	NH=AC/4
	NP=sqrt(AB**2/4+SA**2/4)
	t=acos(NH/NP)
	goc=f"{round_half_up(math.degrees(t),1):.1f}".replace(".",",")
	goc_false=f"{round_half_up(math.degrees(t)+random.randint(1,3),1):.1f}".replace(".",",")

	if chon==3:
		kq4_T=(f"* Gọi ${{{M},{N}}}$ lần lượt là trung điểm các cạnh ${{{A}{B},{A}{D}}}$."
			f" Góc giữa hai đường thẳng ${{{M}{N}}}$ và ${{S{D}}}$ bằng ${goc}^\\circ$")

		kq4_F=(f"Gọi ${{{M},{N}}}$ lần lượt là trung điểm các cạnh ${{{A}{B},{A}{D}}}$."
			f" Góc giữa hai đường thẳng ${{{M}{N}}}$ và ${{S{D}}}$ bằng ${goc_false}^\\circ$") 
		
		HDG=(f"Gọi ${{{P}}}$ là trung điểm của cạnh ${{S{A}}}$. Gọi ${{{H}}}$ là trung điểm của cạnh ${{{M}{N}}}$.\n\n"
			f" Ta có: $({M}{N},S{D})=({M}{N},{N}{P})$.\n\n"
			f"${N}{H}=\\dfrac{{{M}{N}}}{{2}}=\\dfrac{{{B}{D}}}{{4}}={latex(NH*a)}$.\n\n"
			f"${N}{P}=\\sqrt{{{A}{N}^2+{A}{P}^2}}=\\sqrt{{{latex(AB**2*a**2/4)}+{latex(SA**2*a**2/4)}}}={latex(nsimplify(NP)*a)}$.\n\n"
			f"$\\cos \\widehat{{{M}{N}{P}}}=\\cos \\widehat{{{H}{N}{P}}}=\\dfrac{{{N}{H}}}{{{N}{P}}}={latex(nsimplify(NH/NP))}$.\n\n"
			f"$\\Rightarrow \\widehat{{{M}{N}{P}}}={goc}^\\circ$."
			)

	if chon==4:
		kq4_T=(f"* Gọi ${{{I},{K}}}$ lần lượt là trung điểm các cạnh ${{{B}{C},{C}{D}}}$."
			f" Góc giữa hai đường thẳng ${{{I}{K}}}$ và $S{D}$ bằng ${goc}^\\circ$")

		kq4_F=(f"Gọi ${{{I},{K}}}$ lần lượt là trung điểm các cạnh ${{{B}{C},{C}{D}}}$."
			f" Góc giữa hai đường thẳng ${{{I}{K}}}$ và $S{D}$ bằng ${goc_false}^\\circ$") 
		
		HDG=(f"Gọi ${{{M},{N}}}$ lần lượt là trung điểm các cạnh ${{{A}{B},{A}{D}}}$."
			f"Gọi ${{{P}}}$ là trung điểm của cạnh ${{S{A}}}$. Gọi ${{{H}}}$ là trung điểm của cạnh ${{{M}{N}}}$.\n\n"
			f" Ta có: $({I}{K},S{D})=({M}{N},{N}{P})$.\n\n"
			f"${N}{H}=\\dfrac{{{M}{N}}}{{2}}=\\dfrac{{{B}{D}}}{{4}}={latex(NH*a)}$.\n\n"
			f"${N}{P}=\\sqrt{{{A}{N}^2+{A}{P}^2}}=\\sqrt{{{latex(AB**2*a**2/4)}+{latex(SA**2*a**2/4)}}}={latex(nsimplify(NP)*a)}$.\n\n"
			f"$\\cos \\widehat{{{M}{N}{P}}}=\\cos \\widehat{{{H}{N}{P}}}=\\dfrac{{{N}{H}}}{{{N}{P}}}={latex(nsimplify(NH/NP))}$.\n\n"
			f"$\\Rightarrow \\widehat{{{M}{N}{P}}}={goc}^\\circ$."
			)
	
	

	
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n{file_name}\n\n"\
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
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B2_22]-M2. Cho hình lập phương. Tìm cặp đường thẳng vuông góc (cạnh bên vuông góc cạnh đáy).
def uvxy9_L11_C8_B2_22():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	code_hinh = my_module.code_hinh_lapphuong("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	
	noi_dung=(
	f"Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$."
	f" Khẳng định nào sau đây đúng?")	

	kq=random.choice([
	f"$A{A1}\\bot AB$", f"$A{A1}\\bot BC$", f"$A{A1}\\bot CD$", f"$A{A1}\\bot AD$", f"$A{A1}\\bot AC$", f"$A{A1}\\bot BD$",
	f"$B{B1}\\bot AB$",f"$B{B1}\\bot BC$", f"$B{B1}\\bot CD$", f"$B{B1}\\bot AD$",f"$B{B1}\\bot BD$", f"$B{B1}\\bot AC$",
	f"$C{C1}\\bot AB$",f"$C{C1}\\bot BC$", f"$C{C1}\\bot CD$", f"$C{C1}\\bot AD$",f"$C{C1}\\bot BD$", f"$C{C1}\\bot AC$",
	f"$D{D1}\\bot AB$",f"$D{D1}\\bot BC$", f"$D{D1}\\bot CD$", f"$D{D1}\\bot AD$",f"$D{D1}\\bot BD$", f"$D{D1}\\bot AC$",
	])
	kq_false=[f"$A{A1}\\bot C{C1}$", f"$A{A1}\\bot {B1}C$", f"$A{A1}\\bot C{C1}$",
	f"$AC\\bot A{C1}$", f"$BD\\bot {A1}{D1}$", 
	f"$D{B1}\\bot A{D1}$", f"$B{D1}\\bot BD$",  f"${A1}{C1}\\bot CD$",
	f"${B1}C\\bot {A1}D$",f"${B1}{C1}\\bot AC$", f"${B1}{C1}\\bot AD$",
	f"${A1}C\\bot {B1}D$",f"$B{D1}\\bot {B1}D$", 
	f"${D1}C\\bot {B1}{D1}$",
	f"$D{A1}\\bot {A1}B$",
	f"$B{C1}\\bot {C1}D$",]
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

#[D11_C8_B2_23]-M2. Cho hình lập phương. Tìm cặp đường thẳng vuông góc.
def uvxy9_L11_C8_B2_23():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	code_hinh = my_module.code_hinh_lapphuong("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	
	noi_dung=(
	f"Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$."
	f" Khẳng định nào sau đây đúng?")	

	kq=random.choice([
	f"${B1}{D1}\\bot AC$",f"$BD\\bot {A1}{C1}$",
	f"$B{C1}\\bot {A1}{B1}$",f"$B{C1}\\bot {C1}{D1}$",
	f"${B1}C\\bot A{D1}$", f"${B1}C\\bot AB$", f"${B1}C\\bot {C1}{D1}$",
	f"$C{D1}\\bot A{B1}$", f"$C{D1}\\bot AD$", f"$C{D1}\\bot BC$",
	f"$A{D1}\\bot {C1}{D1}$", f"$A{D1}\\bot CD$", f"$A{D1}\\bot {A1}{B1}$",
	f"$A{D1}\\bot AB$", 

	])
	kq_false=[f"$A{A1}\\bot C{C1}$", f"$A{A1}\\bot {B1}C$", f"$A{A1}\\bot C{C1}$",
	f"$AC\\bot A{C1}$", f"$BD\\bot {A1}{D1}$", 
	f"$D{B1}\\bot A{D1}$", f"$B{D1}\\bot BD$",  f"${A1}{C1}\\bot CD$",
	f"${B1}C\\bot {A1}D$", f"${B1}C\\bot {B1}{D1}$",
	f"${B1}{C1}\\bot AC$", f"${B1}{C1}\\bot AD$",
	f"${A1}C\\bot {B1}D$",f"$B{D1}\\bot {B1}D$", 
	f"${D1}C\\bot {B1}{D1}$",
	f"$D{A1}\\bot {A1}B$",
	f"$B{C1}\\bot {C1}D$",
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

#BÀI 3 - HAI MẶT PHẲNG VUÔNG GÓC
#[D11_C8_B3_01]-M2. S.ABCD: ABCD h.vuông. Xác định 2 mặt phẳng vuông góc.
def uvxy9_L11_C8_B3_01(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{A1}{D1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot ({A1}{B1}{C1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{B1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{N1}{B1})\\bot (S{B1}{D1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$"])
		noi_dung_loigiai=f" Vì $S{A1} \\bot (ABCD), S{A1}\\subset (S{A1}{B1}) \\Rightarrow (S{A1}{B1}) \\bot (ABCD)$."
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{B1}{C1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{C1})\\bot ({A1}{B1}{C1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{B1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{B1})$", f"$(S{D1}{M1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$"])
		noi_dung_loigiai=f" Vì $S{A1} \\bot (ABCD), S{A1}\\subset (S{A1}{C1}) \\Rightarrow (S{A1}{C1}) \\bot (ABCD)$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{A1}{D1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{D1})\\bot ({A1}{B1}{C1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{B1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{B1})$", f"$(S{C1}{N1})\\bot (S{B1}{M1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$"])
		noi_dung_loigiai=f" Vì $S{A1} \\bot (ABCD), S{A1}\\subset (S{A1}{D1}) \\Rightarrow (S{A1}{D1}) \\bot (ABCD)$."	

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B3_02]-M3. S.ABCD: ABCD h.vuông. Xác định 2 mặt phẳng vuông góc.
def uvxy9_L11_C8_B3_02(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,4)

	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{A1}{D1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot (S{B1}{C1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${B1}{C1} \\bot {A1}{B1}, {B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{B1})$ và ${B1}{C1} \\subset (S{B1}{C1})$"\
		f" nên $(S{A1}{B1})\\bot (S{B1}{C1})$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{B1}{C1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot (S{B1}{C1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${B1}{C1} \\bot {A1}{B1}, {B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{B1})$ và ${B1}{C1} \\subset (S{B1}{C1})$"\
		f" nên $(S{A1}{B1})\\bot (S{B1}{C1})$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{B1}{C1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{C1})\\bot (S{B1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${B1}{D1} \\bot {A1}{C1}, {B1}{D1} \\bot S{A1} \\Rightarrow {B1}{D1} \\bot (S{A1}{C1})$ và ${B1}{D1} \\subset (S{B1}{D1})$"\
		f" nên $(S{A1}{C1})\\bot (S{B1}{D1})$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{B1}{C1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{C1}{D1})\\bot (S{A1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${C1}{D1} \\bot {A1}{D1}, {C1}{D1} \\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$ và ${C1}{D1} \\subset (S{C1}{D1})$"\
		f" nên $(S{C1}{D1})\\bot (S{A1}{D1})$."

	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1},{P1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}, {{{B1}{C1}}}$ và $S{A1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$({P1}{C1}{D1})\\bot (S{A1}{D1})$"
		kq2= random.choice([f"$({P1}{B1}{D1})\\bot (S{A1}{B1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$({M1}{N1}{P1})\\bot (S{A1}{D1})$", f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${C1}{D1} \\bot {A1}{D1}, {C1}{D1} \\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$ và ${C1}{D1} \\subset ({P1}{C1}{D1})$"\
		f" nên $({P1}{C1}{D1})\\bot (S{A1}{D1})$."

	if chon==6:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1},{P1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}, {{{B1}{C1}}}$ và $S{A1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot ({B1}{C1}){P1}$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${B1}{C1} \\bot {A1}{B1}, {B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{B1})$ và ${B1}{C1} \\subset ({B1}{C1}{P1})$"\
		f" nên $(S{A1}{B1})\\bot ({B1}{C1}{P1})$."

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B3_03]-M2. S.ABCD: ABCD h.chữ nhật. Xác định 2 mặt phẳng vuông góc.
def uvxy9_L11_C8_B3_03(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{A1}{D1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot ({A1}{B1}{C1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{B1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{N1}{B1})\\bot (S{B1}{D1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$"])
		noi_dung_loigiai=f" Vì $S{A1} \\bot (ABCD), S{A1}\\subset (S{A1}{B1}) \\Rightarrow (S{A1}{B1}) \\bot (ABCD)$."
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{B1}{C1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{C1})\\bot ({A1}{B1}{C1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{B1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{B1})$", f"$(S{D1}{M1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$"])
		noi_dung_loigiai=f" Vì $S{A1} \\bot (ABCD), S{A1}\\subset (S{A1}{C1}) \\Rightarrow (S{A1}{C1}) \\bot (ABCD)$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{A1}{D1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{D1})\\bot ({A1}{B1}{C1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{B1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{B1})$", f"$(S{C1}{N1})\\bot (S{B1}{M1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$"])
		noi_dung_loigiai=f" Vì $S{A1} \\bot (ABCD), S{A1}\\subset (S{A1}{D1}) \\Rightarrow (S{A1}{D1}) \\bot (ABCD)$."	

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B3_04]-M3. S.ABCD: ABCD h.chữ nhật. Xác định 2 mặt phẳng vuông góc.
def uvxy9_L11_C8_B3_04(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,4)

	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{A1}{D1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot (S{B1}{C1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${B1}{C1} \\bot {A1}{B1}, {B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{B1})$ và ${B1}{C1} \\subset (S{B1}{C1})$"\
		f" nên $(S{A1}{B1})\\bot (S{B1}{C1})$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{B1}{C1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot (S{B1}{C1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${B1}{C1} \\bot {A1}{B1}, {B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{B1})$ và ${B1}{C1} \\subset (S{B1}{C1})$"\
		f" nên $(S{A1}{B1})\\bot (S{B1}{C1})$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1}}}$ là trung điểm của các cạnh ${{{A1}{B1}}}$ và ${{{B1}{C1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{C1}{D1})\\bot (S{A1}{D1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${C1}{D1} \\bot {A1}{D1}, {C1}{D1} \\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$ và ${C1}{D1} \\subset (S{C1}{D1})$"\
		f" nên $(S{C1}{D1})\\bot (S{A1}{D1})$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1},{P1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}$, ${{{B1}{C1}}}$ và ${{S{A1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$({P1}{C1}{D1})\\bot (S{A1}{D1})$"
		kq2= random.choice([f"$({P1}{B1}{D1})\\bot (S{A1}{B1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$({M1}{N1}{P1})\\bot (S{A1}{D1})$", f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${C1}{D1} \\bot {A1}{D1}, {C1}{D1} \\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$ và ${C1}{D1} \\subset ({P1}{C1}{D1})$"\
		f" nên $({P1}{C1}{D1})\\bot (S{A1}{D1})$."

	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Gọi ${{{M1},{N1},{P1}}}$ lần lượt là trung điểm của các cạnh ${{{A1}{B1}}}, {{{B1}{C1}}}$ và ${{S{A1}}}$."\
		f" Tìm khẳng định đúng?"
		kq= f"$(S{A1}{B1})\\bot ({B1}{C1}{P1})$"
		kq2= random.choice([f"$(S{A1}{B1})\\bot (S{A1}{C1})$", f"$(S{A1}{D1})\\bot (S{M1}{N1})$" ])
		kq3= random.choice([f"$(S{A1}{B1})\\bot (S{B1}{D1})$", f"$(S{B1}{D1})\\bot (S{M1}{N1})$"])
		kq4= random.choice([f"$(S{A1}{C1})\\bot (S{A1}{D1})$", f"$(S{B1}{C1})\\bot (S{M1}{N1})$", f"$(S{B1}{C1})\\bot (S{C1}{D1})$])"])
		noi_dung_loigiai=f" Vì ${B1}{C1} \\bot {A1}{B1}, {B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{B1})$ và ${B1}{C1} \\subset ({B1}{C1}{P1})$"\
		f" nên $(S{A1}{B1})\\bot ({B1}{C1}{P1})$."

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B3_05]-M2. S.ABC: ABC vuông tại A. Tìm 2 mpvg.
def uvxy9_L11_C8_B3_05(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])

	chon=random.randint(1,3)
	chon=4
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$."\
		f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{{B1}{C1}}}$. Tìm khẳng định đúng?"

		kq=f"$(S{A1}{B1})\\bot ({A1}{B1}{C1})$"
		kq2=random.choice([f"$(S{A1}{B1})\\bot (S{A1}{N1})$", f"$(S{C1}{N1})\\bot (S{A1}{B1})$" ])
		kq3=random.choice([f"$(S{A1}{B1})\\bot (S{B1}{C1})$",f"$(S{A1}{M1})\\bot (S{A1}{C1})$" ])
		kq4=random.choice([f"$(S{M1}{N1})\\bot (S{A1}{B1})$", f"$(S{A1}{M1})\\bot (S{C1}{N1})$" ])

		noi_dung_loigiai=f"$S{A1} \\bot (ABC), S{A1} \\subset (S{A1}{B1}) \\Rightarrow (S{A1}{B1}) \\bot (ABC)$."
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$."\
		f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{{B1}{C1}}}$. Tìm khẳng định đúng?"

		kq=f"$(S{A1}{C1})\\bot ({A1}{B1}{C1})$"
		kq2=random.choice([f"$(S{A1}{B1})\\bot (S{A1}{N1})$", f"$(S{C1}{N1})\\bot (S{A1}{B1})$" ])
		kq3=random.choice([f"$(S{A1}{B1})\\bot (S{B1}{C1})$",f"$(S{A1}{M1})\\bot (S{A1}{C1})$" ])
		kq4=random.choice([f"$(S{M1}{N1})\\bot (S{A1}{B1})$", f"$(S{A1}{M1})\\bot (S{C1}{N1})$" ])

		noi_dung_loigiai=f"$S{A1} \\bot (ABC), S{A1} \\subset (S{A1}{C1}) \\Rightarrow (S{A1}{C1}) \\bot (ABC)$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$."\
		f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{{B1}{C1}}}$. Tìm khẳng định đúng?"

		kq=f"$(S{A1}{B1})\\bot (S{A1}{C1})$"
		kq2=random.choice([f"$(S{A1}{B1})\\bot (S{C1}{M1})$", f"$(S{C1}{N1})\\bot (S{A1}{B1})$" ])
		kq3=random.choice([f"$(S{A1}{B1})\\bot (S{B1}{C1})$",f"$(S{A1}{M1})\\bot (S{A1}{C1})$" ])
		kq4=random.choice([f"$(S{M1}{N1})\\bot (S{A1}{B1})$", f"$(S{A1}{M1})\\bot (S{C1}{N1})$" ])

		noi_dung_loigiai=f"${A1}{C1} \\bot {A1}{B1}, {A1}{C1} \\bot S{A1} \\Rightarrow {A1}{C1} \\bot (S{A1}{B1})$."\
		f" Mà ${A1}{C1} \\subset (S{A1}{C1}) \\Rightarrow (S{A1}{C1}) \\bot (S{A1}{B1})$."

	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Gọi ${{{N1}}}$ là trung điểm của cạnh ${{{A1}{B1}}}$."\
		f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của ${{{A1}}}$ trên đường thẳng ${{{B1}{C1}}}$. Tìm khẳng định đúng?"

		kq=f"$(S{B1}{C1})\\bot (S{A1}{M1})$"
		kq2=random.choice([f"$(S{A1}{B1})\\bot (S{C1}{M1})$", f"$(S{C1}{N1})\\bot (S{A1}{B1})$" ])
		kq3=random.choice([f"$(S{A1}{B1})\\bot (S{B1}{C1})$",f"$(S{A1}{M1})\\bot (S{A1}{C1})$" ])
		kq4=random.choice([f"$(S{M1}{N1})\\bot (S{A1}{B1})$", f"$(S{A1}{M1})\\bot (S{C1}{N1})$" ])

		noi_dung_loigiai=f"${B1}{C1} \\bot {A1}{M1},{B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{M1})$."\
		f" Mà ${B1}{C1} \\subset (S{B1}{C1}) \\Rightarrow (S{B1}{C1}) \\bot (S{A1}{M1})$."

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#Góc giữa 2 mặt phẳng
#[D11_C8_B3_06]-M2. S.ABCD: ABCD h.vuông. Tìm vị trí góc (mặt nghiêng, mặt đáy).
def uvxy9_L11_C8_B3_06(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,3)	
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$."\
		f" Tìm góc giữa mặt phẳng $(S{B1}{C1})$ và mặt phẳng ${{(ABCD)}}$."
		kq= f"$\\widehat{{S{B1}{A1}}}$"
		kq2= random.choice([f"$\\widehat{{S{B1}{D1}}}$", f"$\\widehat{{{A1}{B1}{C1}}}$", f"$\\widehat{{{A1}{C1}{B1}}}$"])
		kq3= random.choice([f"$\\widehat{{S{C1}{D1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{S{B1}{D1}}}$", f"$\\widehat{{S{B1}{C1}}}$"])
		noi_dung_loigiai=f"Ta có: $(S{B1}{C1})\\cap (ABCD)={B1}{C1}$.\n\n"\
		f"${B1}{C1}\\bot {A1}{B1}\\subset(ABCD)$\n\n"\
		f"Lại có ${B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1} \\bot S{B1}\\subset (S{B1}{C1})$.\n\n"\
		f"Suy ra góc $\\bigg( (S{B1}{C1}), (ABCD) \\bigg)= (S{B1},{A1}{B1})=$ {kq}."
	
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$."\
		f" Tìm góc giữa mặt phẳng $(S{C1}{D1})$ và mặt phẳng ${{(ABCD)}}$."
		kq= f"$\\widehat{{S{D1}{A1}}}$"
		kq2= random.choice([f"$\\widehat{{S{D1}{C1}}}$", f"$\\widehat{{{A1}{C1}{D1}}}$", f"$\\widehat{{{B1}{C1}{D1}}}$"])
		kq3= random.choice([f"$\\widehat{{S{C1}{B1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{S{A1}{D1}}}$", f"$\\widehat{{S{C1}{D1}}}$"])
		noi_dung_loigiai=f"Ta có: $(S{C1}{D1})\\cap (ABCD)={C1}{D1}$.\n\n"\
		f"${C1}{D1}\\bot {A1}{D1}\\subset(ABCD)$\n\n"\
		f"Lại có ${C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot S{D1}\\subset (S{C1}{D1})$.\n\n"\
		f"Suy ra góc $\\bigg( (S{C1}{D1}), (ABCD) \\bigg)= (S{D1},{A1}{D1})=$ {kq}."
	
	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông tâm ${{O}}$, $S{A1}\\bot (ABCD)$."\
		f" Tìm góc giữa mặt phẳng $(S{B1}{D1})$ và mặt phẳng ${{(ABCD)}}$."
		kq= f"$\\widehat{{SO{A1}}}$"
		kq2= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{{A1}{D1}{B1}}}$"])
		kq3= random.choice([f"$\\widehat{{S{D1}{A1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{S{A1}O}}$", f"$\\widehat{{S{C1}O}}$"])
		noi_dung_loigiai=f"Ta có: $(S{B1}{D1}) \\cap (ABCD)={B1}{D1}$.\n\n"\
		f"${B1}{D1}\\bot {A1}O \\subset(ABCD)$\n\n"\
		f"Lại có ${B1}{D1}\\bot S{A1} \\Rightarrow {B1}{D1} \\bot SO\\subset (S{B1}{D1})$.\n\n"\
		f"Suy ra góc $\\bigg( (S{B1}{D1}), (ABCD) \\bigg)= (SO,{A1}O)=$ {kq}."	

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B3_07]-M2. S.ABCD: ABCD h.chữ nhật. Tìm vị trí góc (mặt nghiêng, mặt đáy).
def uvxy9_L11_C8_B3_07(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I", "N", "F", "K", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,3)
	
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
		f" Tìm góc giữa mặt phẳng $(S{B1}{C1})$ và mặt phẳng ${{(ABCD)}}$."
		kq= f"$\\widehat{{S{B1}{A1}}}$"
		kq2= random.choice([f"$\\widehat{{S{B1}{D1}}}$", f"$\\widehat{{{A1}{B1}{C1}}}$", f"$\\widehat{{{A1}{C1}{B1}}}$"])
		kq3= random.choice([f"$\\widehat{{S{C1}{D1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{S{B1}{D1}}}$", f"$\\widehat{{S{B1}{C1}}}$"])
		noi_dung_loigiai=f"Ta có: $(S{B1}{C1})\\cap (ABCD)={B1}{C1}$.\n\n"\
		f"${B1}{C1}\\bot {A1}{B1}\\subset(ABCD)$\n\n"\
		f"Lại có ${B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1} \\bot S{B1}\\subset (S{B1}{C1})$.\n\n"\
		f"Suy ra góc $\\bigg( (S{B1}{C1}), (ABCD) \\bigg)= (S{B1},{A1}{B1})=$ {kq}."
	
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$."\
		f" Tìm góc giữa mặt phẳng $(S{C1}{D1})$ và mặt phẳng ${{(ABCD)}}$."
		kq= f"$\\widehat{{S{D1}{A1}}}$"
		kq2= random.choice([f"$\\widehat{{S{D1}{C1}}}$", f"$\\widehat{{{A1}{C1}{D1}}}$", f"$\\widehat{{{B1}{C1}{D1}}}$"])
		kq3= random.choice([f"$\\widehat{{S{C1}{B1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{S{A1}{D1}}}$", f"$\\widehat{{S{C1}{D1}}}$"])
		noi_dung_loigiai=f"Ta có: $(S{C1}{D1})\\cap (ABCD)={C1}{D1}$.\n\n"\
		f"${C1}{D1}\\bot {A1}{D1}\\subset(ABCD)$\n\n"\
		f"Lại có ${C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot S{D1}\\subset (S{C1}{D1})$.\n\n"\
		f"Suy ra góc $\\bigg( (S{C1}{D1}), (ABCD) \\bigg)= (S{D1},{A1}{D1})=$ {kq}."
	
	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$."\
		f" Gọi ${{{M1}}}$ là hình chiếu vuông góc của điểm ${{{A1}}}$ trên đường thẳng ${{{B1}{D1}}}$."\
		f" Tìm góc giữa mặt phẳng $(S{B1}{D1})$ và mặt phẳng ${{(ABCD)}}$."
		kq= f"$\\widehat{{S{M1}{A1}}}$"
		kq2= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{{A1}{D1}{B1}}}$"])
		kq3= random.choice([f"$\\widehat{{S{D1}{A1}}}$", f"$\\widehat{{S{C1}O}}$"])
		kq4= random.choice([f"$\\widehat{{SO{A1}}}$"])
		noi_dung_loigiai=f"Ta có: $(S{B1}{D1}) \\cap (ABCD)={B1}{D1}$.\n\n"\
		f"${B1}{D1}\\bot {A1}{M1} \\subset(ABCD)$\n\n"\
		f"Lại có ${B1}{D1}\\bot S{A1} \\Rightarrow {B1}{D1} \\bot S{M1}\\subset (S{B1}{D1})$.\n\n"\
		f"Suy ra góc $\\bigg( (S{B1}{D1}), (ABCD) \\bigg)= (S{M1},{A1}{M1})=$ {kq}."		
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B3_08]-M2. S.ABC: ABC đều. Tính góc(mặt nghiêng, mặt đáy).
def uvxy9_L11_C8_B3_08():
	a=sp.symbols("a")  	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]

	i=random.randint(0,2)
	A1, B1, C1= A1[i], B1[i], C1[i]
		
	AB=random.randint(1,9)
	SA=random.choice([sqrt(i) for i in range(1,100)])

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	AM=AB*sqrt(3)/2
	t=SA/AM
	goc=round(atan(t).evalf() * 180 / pi,2)
	
	kq=return_number_vn(goc)
	kq2=return_number_vn(goc+(random.randint(10,90))/10)
	kq3=return_number_vn(goc+(random.randint(90,130))/10)
	kq4=return_number_vn(goc+(random.randint(140,200))/10)

	noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều có $S{A1}\\bot (ABC), {A1}{B1}={AB}a,S{A1}={latex(SA)}a$. Tính góc giữa hai mặt phẳng $(S{B1}{C1})$ và $(ABC)$.")
		
	noi_dung_loigiai=f"Gọi M là trung điểm của ${{{B1}{C1}}}, {A1}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
	f"Góc giữa $(S{B1}{C1})$ và ${{(ABC)}}$ là $\\widehat{{S{A1}M}}$.\n\n"\
	f"$\\tan \\widehat{{SM{A1}}}=\\dfrac{{S{A1}}}{{{A1}M}}=\\dfrac{{{latex(SA)}a}}{{{latex(AM)}a}}={latex(t)}\\Rightarrow \\widehat{{S{A1}M}}={return_number_vn(goc)}^\\circ$."
		
	
    #Tạo các phương án
	pa_A= f"*${kq}^\\circ$"
	pa_B= f"${kq2}^\\circ$"
	pa_C= f"${kq3}^\\circ$"
	pa_D= f"${kq4}^\\circ$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B3_09]-M2. S.ABC: ABC vuông. Tính góc(mặt nghiêng, mặt đáy).
def uvxy9_L11_C8_B3_09():
	a=sp.symbols("a")  	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]

	i=random.randint(0,2)
	A1, B1, C1= A1[i], B1[i], C1[i]
		
	AB=random.randint(1,9)
	BC=random.randint(1,9)
	AC=sqrt(AB**2+BC**2)

	SA=random.choice([sqrt(i) for i in range(1,100)])
	SB=sqrt(SA**2+AB**2)

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)	
	t=SA/AB
	goc=round(atan(t).evalf() * 180 / pi,2)
	
	kq=return_number_vn(goc)
	kq2=return_number_vn(goc+(random.randint(10,90))/10)
	kq3=return_number_vn(goc+(random.randint(90,130))/10)
	kq4=return_number_vn(goc+(random.randint(140,200))/10)

	noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{B1}}}, S{A1}\\bot (ABC), {A1}{C1}={latex(AC)}a,{B1}{C1}={latex(BC)}a,S{A1}={latex(SA)}a$."\
	f" Tính góc giữa hai mặt phẳng $(S{B1}{C1})$ và $(ABC)$.")
		
	noi_dung_loigiai=f"$(S{B1}{C1})\\cap (ABC)={B1}{C1}, {A1}{B1}\\bot {B1}{C1},S{B1}\\bot {B1}{C1}$.\n\n"\
	f"Góc giữa $(S{B1}{C1})$ và ${{(ABC)}}$ là $\\widehat{{S{B1}{A1}}}$.\n\n"\
	f"${A1}{B1}=\\sqrt{{{A1}{C1}^2-{B1}{C1}^2}}={latex(AC**2-BC**2)}a$.\n\n"\
	f"$\\tan \\widehat{{S{B1}{A1}}}=\\dfrac{{S{A1}}}{{{A1}{B1}}}=\\dfrac{{{latex(SA)}a}}{{{latex(AB)}a}}={latex(t)}\\Rightarrow \\widehat{{S{B1}{A1}}}={return_number_vn(goc)}^\\circ$."
		
	
    #Tạo các phương án
	pa_A= f"*${kq}^\\circ$"
	pa_B= f"${kq2}^\\circ$"
	pa_C= f"${kq3}^\\circ$"
	pa_D= f"${kq4}^\\circ$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#Bài 4- Khoảng cách trong không gian
#[D11_C8_B6_01]. Cho hình chóp có diện tích đáy và chiều cao. Tính thể tích.
def uvxy9_L11_C8_B6_01():
	S_day = random.randint(2,15)
	h = random.randint(2,10)
	kq=1/3*S_day*h
	kq2=S_day*h
	kq3=1/2*S_day*h
	kq4=1/3*(S_day+h)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=latex(my_module.hien_phan_so(kq))
	kq2=latex(my_module.hien_phan_so(kq2))
	kq3=latex(my_module.hien_phan_so(kq3))
	kq4=latex(my_module.hien_phan_so(kq4))	
	

	pa_A= f"*${{V={kq}}}$"
	pa_B= f"${{V={kq2}}}$"
	pa_C= f"${{V={kq3}}}$"
	pa_D= f"${{V={kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Cho hình chóp có diện tích đáy bằng ${{{S_day}}}$ và chiều cao bằng ${{{h}}}$. Tính thể tích ${{V}}$ của khối chóp đã cho."

	noi_dung_loigiai=f"$V=\\dfrac{{1}}{{3}}.{S_day}.{h}={kq}$."

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an
	

#[D11_C8_B6_02]. Cho hình chóp có đáy là tam giác đều và chiều cao. Tính thể tích.
def uvxy9_L11_C8_B6_02():
	a = random.randint(1,10)
	h = random.randint(2,10)
	S_day=a**2/4

	kq=1/3*S_day*h
	kq2=S_day*h
	kq3=1/2*S_day*h
	kq4=1/6*a**2*h

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{latex(my_module.hien_phan_so(kq))}\\sqrt 3"
	kq2=f"{latex(my_module.hien_phan_so(kq2))}\\sqrt 3"
	kq3=f"{latex(my_module.hien_phan_so(kq3))}\\sqrt 3"
	kq4=f"{latex(my_module.hien_phan_so(kq4))}\\sqrt 3"	
	

	pa_A= f"*${{V={kq}}}$"
	pa_B= f"${{V={kq2}}}$"
	pa_C= f"${{V={kq3}}}$"
	pa_D= f"${{V={kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Cho hình chóp có đáy là tam giác đều cạnh bằng ${{{a}}}$ và chiều cao bằng ${{{h}}}$. Tính thể tích $V$ của khối chóp đã cho." 


	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung_loigiai=f"$V=\\dfrac{{1}}{{3}}.{a}^2{latex(sqrt(3)/4)}.{h}={kq}$."

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_03]. Cho hình chóp có đáy là tam giác vuông và chiều cao. Tính thể tích.
def uvxy9_L11_C8_B6_03():
	a = random.randint(1,10)
	b = random.randint(1,10)
	h = random.randint(2,10)
	S_day=1/2*a*b

	kq=1/3*S_day*h
	kq2=S_day*h
	kq3=1/2*S_day*h
	kq4=a*b*h

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=latex(my_module.hien_phan_so(kq))
	kq2=latex(my_module.hien_phan_so(kq2))
	kq3=latex(my_module.hien_phan_so(kq3))
	kq4=latex(my_module.hien_phan_so(kq4))		
	
	pa_A= f"*$\\displaystyle {{V={kq}a^3}}$"
	pa_B= f"$\\displaystyle {{V={kq2}a^3}}$"
	pa_C= f"$\\displaystyle {{V={kq3}a^3}}$"
	pa_D= f"$\\displaystyle {{V={kq4}a^3}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung =thay_hinh_hoc( f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại $A$, ${{AB={a}a}}$ và ${{AC={b}a}}$, $SA\\bot(ABC), SA={h}a$. Tính thể tích $V$ của khối chóp đã cho.")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung_loigiai=thay_hinh_hoc(f"$V=\\dfrac{{1}}{{3}}.\\dfrac{{1}}{{2}}.{a}a.{b}a.{h}a={kq}a^3$.")

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_04]-M2 Cho hình chóp có đáy là tam giác đều và góc giữa cạnh bên và đáy. Tính thể tích.
def uvxy9_L11_C8_B6_04():
	a = random.randint(1,10)
	goc = random.choice([30,45,60])
	h=a*my_module.hien_tan(goc)
	canh_ben =random.choice(["SB","SC"])
	if goc in [30,60]:		
		S_day=a**2*sqrt(3)/4
		kq=1/3*S_day*h
		kq2=S_day*h
		kq3=1/2*S_day*h
		kq4=1/6*S_day*h
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
		kq=f"{latex(my_module.hien_phan_so(kq))}"
		kq2=f"{latex(my_module.hien_phan_so(kq2))}"
		kq3=f"{latex(my_module.hien_phan_so(kq3))}"
		kq4=f"{latex(my_module.hien_phan_so(kq4))}"	
	else:
		S_day=a**2/4
		h==a
		kq=1/3*S_day*h
		kq2=S_day*h
		kq3=1/2*S_day*h
		kq4=1/6*a**2*h

		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

		kq=f"{latex(my_module.hien_phan_so(kq))}\\sqrt 3"
		kq2=f"{latex(my_module.hien_phan_so(kq2))}\\sqrt 3"
		kq3=f"{latex(my_module.hien_phan_so(kq3))}\\sqrt 3"
		kq4=f"{latex(my_module.hien_phan_so(kq4))}\\sqrt 3"		
	
	pa_A= f"*$\\displaystyle {{V={kq}a^3}}$"
	pa_B= f"$\\displaystyle {{V={kq2}a^3}}$"
	pa_C= f"$\\displaystyle {{V={kq3}a^3}}$"
	pa_D= f"$\\displaystyle {{V={kq4}a^3}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung = thay_hinh_hoc(f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều cạnh bằng ${{{a}a}}$, $SA\\bot(ABC)$. Góc giữa cạnh ${{{canh_ben}}}$ và đáy bằng ${goc}^\\circ$. Tính thể tích $V$ của khối chóp đã cho.")

	noi_dung_loigiai=thay_hinh_hoc(f"$SA={canh_ben}.\\tan {goc}^\\circ ={latex(h)}a.$\n\n"\
	f"$V=\\dfrac{{1}}{{3}}.{latex(a**2*sqrt(3)/4)}a^2.{latex(h)}a={kq}a^3$.")

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_05]-M1. Cho hình lăng trụ có diện tích đáy và chiều cao. Tính thể tích
def uvxy9_L11_C8_B6_05():
	S_day = random.randint(2,15)
	h = random.randint(2,10)
	kq=S_day*h
	kq2=1/3*S_day*h
	kq3=1/2*S_day*h
	kq4=1/3*(S_day+h)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=latex(my_module.hien_phan_so(kq))
	kq2=latex(my_module.hien_phan_so(kq2))
	kq3=latex(my_module.hien_phan_so(kq3))
	kq4=latex(my_module.hien_phan_so(kq4))	
	

	pa_A= f"*$\\displaystyle {{V={kq}}}$"
	pa_B= f"$\\displaystyle {{V={kq2}}}$"
	pa_C= f"$\\displaystyle {{V={kq3}}}$"
	pa_D= f"$\\displaystyle {{V={kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	

	noi_dung = thay_hinh_hoc(f"Cho khối lăng trụ có diện tích đáy bằng ${{{S_day}}}$ và chiều cao bằng ${{{h}}}$. Tính thể tích ${{V}}$ của khối lăng trụ đã cho.")
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"$V={S_day}.{h}={kq}$."

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_06]. Cho hình lăng trụ có đáy là tam giác đều và chiều cao. Tính thể tích.
def uvxy9_L11_C8_B6_06():
	a = random.randint(1,10)
	h = random.randint(2,10)
	S_day=a**2/4

	kq=rutgon_can(sqrt(a**4*3*h**2)/sqrt(16))
	kq2=1/3*S_day*h
	kq3=1/2*S_day*h
	kq4=1/6*a**2*h

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{latex(kq)}"
	kq2=f"{latex(my_module.hien_phan_so(kq2))}\\sqrt{{3}}"
	kq3=f"{latex(my_module.hien_phan_so(kq3))}\\sqrt{{3}}"
	kq4=f"{latex(my_module.hien_phan_so(kq4))}\\sqrt{{3}}"	
	

	pa_A= f"*$\\displaystyle {{V={kq}}}$"
	pa_B= f"$\\displaystyle {{V={kq2}}}$"
	pa_C= f"$\\displaystyle {{V={kq3}}}$"
	pa_D= f"$\\displaystyle {{V={kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = thay_hinh_hoc(f"Cho hình lăng trụ có đáy là tam giác đều cạnh bằng ${{{a}}}$ và chiều cao bằng ${{{h}}}$. Tính thể tích $V$ của khối lăng trụ đã cho.")


	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung_loigiai=f"$V={a}^2{latex(sqrt(3)/4)}.{h}={kq}$."

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_07]-M1. Cho hình lăng trụ có đáy là tam giác vuông và chiều cao. Tính thể tích.
def uvxy9_L11_C8_B6_07():
	a = random.randint(1,10)
	b = random.randint(1,10)
	h = random.randint(2,10)
	S_day=1/2*a*b

	kq=S_day*h
	kq2=1/3*S_day*h
	kq3=1/2*S_day*h
	kq4=a*b*h

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=latex(my_module.hien_phan_so(kq))
	kq2=latex(my_module.hien_phan_so(kq2))
	kq3=latex(my_module.hien_phan_so(kq3))
	kq4=latex(my_module.hien_phan_so(kq4))		
	
	pa_A= f"*${{V={kq}a^3}}$"
	pa_B= f"${{V={kq2}a^3}}$"
	pa_C= f"${{V={kq3}a^3}}$"
	pa_D= f"${{V={kq4}a^3}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác vuông tại $A$, $AB={a}a, AC={b}a, AA'={h}a$. Tính thể tích $V$ của khối lăng trụ đã cho.")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung_loigiai=thay_hinh_hoc(f"$V=\\dfrac{{1}}{{2}}.{a}a.{b}a.{h}a={kq}a^3$.")

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_08]-M1. Cho hình lăng trụ có đáy là h.vuông,h.c.n và chiều cao. Tính thể tích.
def uvxy9_L11_C8_B6_08():
	a = random.randint(2,10)
	b = random.randint(1,10)
	h = random.randint(2,10)
	chon=random.randint(1,2)

	if chon==1:
		noi_dung = thay_hinh_hoc(f"Cho hình lăng trụ đứng có đáy là hình vuông cạnh bằng ${{{a}a}}$ và chiều cao bằng ${{{h}a}}$. Tính thể tích $V$ của khối lăng trụ đã cho.")

		S_day=a**2
		kq=S_day*h
		kq2=1/3*S_day*h
		kq3=1/2*S_day*h
		kq4=random.choice([2*a*h,2*a*h*random.randint(2,6)])
		noi_dung_loigiai=thay_hinh_hoc(f"$V={a}^2a.{h}a={kq}a^3$.")

	if chon==2:
		ten_h=random.choice(["AA'","BB'","CC'","DD'"])
		noi_dung = thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABCD.A'B'C'D'}}$ có đáy là hình chữ nhật cạnh $AB={a}a,AD={b}a, {ten_h}={h}a$. Tính thể tích $V$ của khối lăng trụ đã cho.")

		S_day=a*b
		kq=S_day*h
		kq2=1/3*S_day*h
		kq3=1/2*S_day*h
		kq4=random.choice([2*a*h,2*a*h*random.randint(2,6)])
		noi_dung_loigiai=thay_hinh_hoc(f"$V={a}a.{b}a.{h}a={kq}a^3$.")

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=latex(my_module.hien_phan_so(kq))
	kq2=latex(my_module.hien_phan_so(kq2))
	kq3=latex(my_module.hien_phan_so(kq3))
	kq4=latex(my_module.hien_phan_so(kq4))		
	
	pa_A= f"*${{V={kq}a^3}}$"
	pa_B= f"${{V={kq2}a^3}}$"
	pa_C= f"${{V={kq3}a^3}}$"
	pa_D= f"${{V={kq4}a^3}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_09]-M3. S.ABCD: ABCD h.cn có góc giữa 2 đường thẳng. Tính V.
def uvxy9_L11_C8_B6_09(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	chon=random.randint(1,3)

	if chon==1:
		AB=random.randint(1,8)
		BC=AB+ random.randint(1,5)
		AC=sqrt(AB**2+BC**2)
		goc=45
		tan=my_module.hien_tan(goc)
		SA=BC*tan
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a,{A1}{C1}={latex(AC)}a$."\
		f" Góc giữa hai đường thẳng ${{S{D1}}}$ và ${{{B1}{C1}}}$ bằng ${{{goc}^\\circ}}$."\
		f" Tính thể tích của khối chóp ${{S.ABCD}}$."
		noi_dung=thay_hinh_hoc(noi_dung)

		kq=1/3*AB*BC*SA
		kq2=1/3*1/2*AB*BC*SA
		kq3=1/2*AB*BC*SA
		kq4=AB*BC*SA
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

		kq= f"{latex(my_module.hien_phan_so(kq))}a^3"
		kq2=f"{latex(my_module.hien_phan_so(kq2))}a^3"
		kq3=f"{latex(my_module.hien_phan_so(kq3))}a^3"
		kq4= f"{latex(my_module.hien_phan_so(kq4))}a^3"

		noi_dung_loigiai=f"Ta có: ${B1}{C1}=\\sqrt{{{A1}{C1}^2- {A1}{B1}^2}}=\\sqrt{{{AC**2}a^2-{AB**2}a^2}}={BC}a$.\n\n"\
		f" Góc  $({{S{D1},{B1}{C1}}})=({{S{D1},{A1}{D1}}})=\\widehat{{S{D1}{A1}}}={goc}^\\circ$.\n\n"\
		f"$S{A1}={A1}{D1}.\\tan {goc}^\\circ={latex(SA)}a$.\n\n Thể tích của khối chóp đã cho là:\n\n"\
		f"$V=\\dfrac{{1}}{{3}}.{A1}{B1}.{B1}{C1}.S{A1}=\\dfrac{{1}}{{3}}{AB}a.{BC}a.{latex(SA)}a={kq}$."

	if chon==2:
		AB=random.randint(1,8)
		BC=AB+ random.randint(1,5)
		AC=sqrt(AB**2+BC**2)
		goc=60
		tan=my_module.hien_tan(goc)
		SA=BC*tan
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a,{A1}{C1}={latex(AC)}a$."\
		f" Góc giữa hai đường thẳng ${{S{D1}}}$ và ${{{B1}{C1}}}$ bằng ${{{goc}^\\circ}}$."\
		f" Tính thể tích của khối chóp ${{S.ABCD}}$."
		noi_dung=thay_hinh_hoc(noi_dung)

		kq=1/3*AB*BC*BC
		kq2=1/3*1/2*AB*BC*BC
		kq3=1/2*AB*BC*BC
		kq4=AB*BC*BC
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

		kq= f"{latex(my_module.hien_phan_so(kq))}\\sqrt{{3}}a^3"
		kq2=f"{latex(my_module.hien_phan_so(kq2))}\\sqrt{{3}}a^3"
		kq3=f"{latex(my_module.hien_phan_so(kq3))}\\sqrt{{3}}a^3"
		kq4= f"{latex(my_module.hien_phan_so(kq4))}\\sqrt{{3}}a^3"

		noi_dung_loigiai=f"Ta có: ${B1}{C1}=\\sqrt{{{A1}{C1}^2- {A1}{B1}^2}}=\\sqrt{{{AC**2}a^2-{AB**2}a^2}}={BC}a$.\n\n"\
		f" Góc  $({{S{D1},{B1}{C1}}})=({{S{D1},{A1}{D1}}})=\\widehat{{S{D1}{A1}}}={goc}^\\circ$.\n\n"\
		f"$S{A1}={A1}{D1}.\\tan {goc}^\\circ={latex(SA)}a$.\n\n Thể tích của khối chóp đã cho là:\n\n"\
		f"$V=\\dfrac{{1}}{{3}}.{A1}{B1}.{B1}{C1}.S{A1}=\\dfrac{{1}}{{3}}{AB}a.{BC}a.{latex(SA)}a={kq}$."

	if chon==3:
		AB=random.randint(1,8)
		BC=AB+ random.randint(1,5)
		AC=sqrt(AB**2+BC**2)
		goc=30
		tan=my_module.hien_tan(goc)
		SA=BC*tan
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a,{A1}{C1}={latex(AC)}a$."\
		f" Góc giữa hai đường thẳng ${{S{D1}}}$ và ${{{B1}{C1}}}$ bằng ${{{goc}^\\circ}}$."\
		f" Tính thể tích của khối chóp ${{S.ABCD}}$."
		noi_dung=thay_hinh_hoc(noi_dung)

		kq=1/9*AB*BC*BC
		kq2=1/3*1/2*AB*BC*BC
		kq3=1/3*AB*BC*BC
		kq4=1/2*AB*BC*BC
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

		kq= f"{latex(my_module.hien_phan_so(kq))}\\sqrt{{3}}a^3"
		kq2=f"{latex(my_module.hien_phan_so(kq2))}\\sqrt{{3}}a^3"
		kq3=f"{latex(my_module.hien_phan_so(kq3))}\\sqrt{{3}}a^3"
		kq4= f"{latex(my_module.hien_phan_so(kq4))}\\sqrt{{3}}a^3"

		noi_dung_loigiai=f"Ta có: ${B1}{C1}=\\sqrt{{{A1}{C1}^2- {A1}{B1}^2}}=\\sqrt{{{AC**2}a^2-{AB**2}a^2}}={BC}a$.\n\n"\
		f" Góc  $({{S{D1},{B1}{C1}}})=({{S{D1},{A1}{D1}}})=\\widehat{{S{D1}{A1}}}={goc}^\\circ$.\n\n"\
		f"$S{A1}={A1}{D1}.\\tan {goc}^\\circ={latex(SA)}a$.\n\n Thể tích của khối chóp đã cho là:\n\n"\
		f"$V=\\dfrac{{1}}{{3}}.{A1}{B1}.{B1}{C1}.S{A1}=\\dfrac{{1}}{{3}}{AB}a.{BC}a.{latex(SA)}a={kq}$."

	
	noi_dung_loigiai=thay_hinh_hoc(noi_dung_loigiai)

	
	
    #Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n")
	phuongan=thay_hinh_hoc(phuongan)
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_01]-M2. S.ABCD: ABCD h.chữ nhật. Tính k.c từ điểm đến mặt đứng.
def uvxy9_L11_C8_B4_01(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,6)

	if chon==1:
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$.\n\n"\
		f" Tính khoảng cách từ điểm ${{{D1}}}$ đến mặt phẳng $(S{A1}{B1})$?"
		kq= thay_hinh_hoc(f"${{{AD}a}}$")
		kq2=thay_hinh_hoc(f"${{{AB}a}}$")
		kq3= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"
		kq4= f"${{{latex(sqrt(AB+AD))}a}}$"
		noi_dung_loigiai=f" Vì ${D1}{A1} \\bot {A1}{B1}, {D1}{A1}\\bot S{A1} \\Rightarrow {D1}{A1} \\bot (S{A1}{B1})$."\
		f" Vậy $d({D1},(S{A1}{B1}))={D1}{A1}={AD}a$."

	if chon==2:
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Tính khoảng cách từ điểm ${{{B1}}}$ đến mặt phẳng $(S{A1}{D1})$?"
		kq=thay_hinh_hoc( f"${{{AB}a}}$")
		kq2= thay_hinh_hoc(f"${{{AD}a}}$")
		kq3= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"
		kq4= f"${{{latex(sqrt(AB+AD))}a}}$"
		noi_dung_loigiai=f" Vì ${B1}{A1} \\bot {A1}{D1}, {B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{B1})$."\
		f" Vậy $d({B1},(S{A1}{D1}))={B1}{A1}={AB}a$."

	if chon==3:
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Tính khoảng cách từ điểm ${{{C1}}}$ đến mặt phẳng $(S{A1}{D1})$?"
		kq= thay_hinh_hoc(f"${{{AB}a}}$")
		kq2= thay_hinh_hoc(f"${{{AD}a}}$")
		kq3= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"
		kq4= f"${{{latex(sqrt(AB+AD))}a}}$"
		noi_dung_loigiai=f" Vì ${C1}{D1} \\bot {A1}{D1}, {C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$."\
		f" Vậy $d({C1},(S{A1}{D1}))={C1}{D1}={AB}a$."

	if chon==4:
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Tính khoảng cách từ điểm ${{{C1}}}$ đến mặt phẳng $(S{A1}{B1})$?"
		kq= thay_hinh_hoc(f"${{{AD}a}}$")
		kq2= thay_hinh_hoc(f"${{{AB}a}}$")
		kq3= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"
		kq4= f"${{{latex(sqrt(AB+AD))}a}}$"
		noi_dung_loigiai=f" Vì ${C1}{B1} \\bot {A1}{B1}, {C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$."\
		f" Vậy $d({C1},(S{A1}{B1}))={C1}{B1}={AD}a$."

	if chon==5:
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Tính khoảng cách từ điểm ${{O}}$ đến mặt phẳng $(S{A1}{B1})$?"
		kq= thay_hinh_hoc(f"${{{latex(my_module.hien_phan_so(AD/2))}a}}$")
		kq2=random.choice([thay_hinh_hoc(f"${{{AB}a}}$"), f"${{{latex(my_module.hien_phan_so(AB/2))}a}}$"])
		kq3= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"
		kq4= f"${{{latex(sqrt(AB+AD))}a}}$"
		noi_dung_loigiai=f"Gọi ${{M}}$ là trung điểm của cạnh ${{{A1}{B1}}}$.\n\n"\
		f"Vì $OM \\bot {A1}{B1}, OM \\bot S{A1} \\Rightarrow OM \\bot (S{A1}{B1})$."\
		f" Vậy $d(O,(S{A1}{B1}))=OM={my_module.hien_phan_so(AD/2)}a$."

	if chon==6:
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật tâm ${{O}}$, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Tính khoảng cách từ điểm ${{O}}$ đến mặt phẳng $(S{A1}{D1})$?"
		kq= thay_hinh_hoc(f"${{{latex(my_module.hien_phan_so(AB/2))}a}}$")
		kq2=random.choice([thay_hinh_hoc(f"${{{AB}a}}$"), f"${{{latex(my_module.hien_phan_so(AD/2))}a}}$"])
		kq3= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"
		kq4= f"${{{latex(sqrt(AB+AD))}a}}$"
		noi_dung_loigiai=f"Gọi ${{M}}$ là trung điểm của cạnh ${{{A1}{D1}}}$.\n\n"\
		f"Vì $OM \\bot {A1}{D1}, OM \\bot S{A1} \\Rightarrow OM \\bot (S{A1}{D1})$."\
		f" Vậy $d(O,(S{A1}{D1}))=OM={my_module.hien_phan_so(AD/2)}a$."


	noi_dung=thay_hinh_hoc(noi_dung)		
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_02]-M3. S.ABCD: ABCD h.chữ nhật. Tính k.c từ điểm đến mặt đứng.
def uvxy9_L11_C8_B4_02(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I", "N", "F", "K", "P", "G"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,4)
	t=random.randint(1,4)
	if t==1:
		t1=""
	else:
		t1=t

	if chon==1:
		
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Gọi ${{{M1}}}$ là điểm thuộc cạnh ${{S{C1}}}$ sao cho $S{{{M1}}}={t1}{M1}{C1}$. Tính khoảng cách từ điểm ${{{M1}}}$ đến mặt phẳng $(S{A1}{D1})$."
		kq= thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AB))}a")
		kq2=thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AD))}a")
		kq3= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so((t+1)/t*AB))}a", f"{latex(my_module.hien_phan_so((t+1)/t*AD))}a"] ))
		kq4= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so(t*AB))}a",f"{latex(my_module.hien_phan_so(t*AD))}a" ]))
		noi_dung_loigiai=f" Vì ${C1}{D1} \\bot {A1}{D1}, {C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$."\
		f" Suy ra $d({C1},(S{A1}{D1}))={C1}{D1}={AB}a$.\n\n"\
		f"$\\dfrac{{ d({M1},(S{A1}{D1})) }} {{ d({C1},(S{A1}{D1})) }} = \\dfrac{{S{M1}}} {{S{C1}}} = {latex(my_module.hien_phan_so(t/(t+1)))}$"\
		f"$\\Rightarrow d({M1},(S{A1}{D1}) = {latex(my_module.hien_phan_so(t/(t+1)))} d({C1},(S{A1}{D1})) = {latex(my_module.hien_phan_so(t/(t+1)))} {AB}a={latex(my_module.hien_phan_so(t/(t+1)*AB))}a$."
		noi_dung_loigiai=thay_hinh_hoc(noi_dung_loigiai)

	if chon==2:
		
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Gọi ${{{M1}}}$ là điểm thuộc cạnh ${{S{C1}}}$ sao cho $S{{{M1}}}={t1}{M1}{C1}$. Tính khoảng cách từ điểm ${{{M1}}}$ đến mặt phẳng $(S{A1}{B1})$."
		
		kq= thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AD))}a")
		kq2= thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AB))}a")
		kq3= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so((t+1)/t*AB))}a", f"{latex(my_module.hien_phan_so((t+1)/t*AD))}a"] ))
		kq4= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so(t*AB))}a",f"{latex(my_module.hien_phan_so(t*AD))}a" ]))
		
		noi_dung_loigiai=f" Vì ${C1}{B1} \\bot {A1}{B1}, {C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$."\
		f" Suy ra $d({C1},(S{A1}{B1}))={C1}{B1}={AD}a$.\n\n"\
		f"$\\dfrac{{ d({M1},(S{A1}{B1})) }} {{ d({C1},(S{A1}{B1})) }} = \\dfrac{{S{M1}}} {{S{C1}}} = {latex(my_module.hien_phan_so(t/(t+1)))}$"\
		f"$\\Rightarrow d({M1},(S{A1}{B1}) = {latex(my_module.hien_phan_so(t/(t+1)))} d({C1},(S{A1}{B1})) = {latex(my_module.hien_phan_so(t/(t+1)))} {AD}a={latex(my_module.hien_phan_so(t/(t+1)*AD))}a$."
		noi_dung_loigiai=thay_hinh_hoc(noi_dung_loigiai)

	
	if chon==3:		
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Gọi ${{{M1}}}$ là điểm thuộc cạnh ${{S{B1}}}$ sao cho $S{{{M1}}}={t1}{M1}{B1}$. Tính khoảng cách từ điểm ${{{M1}}}$ đến mặt phẳng $(S{A1}{D1})$."
		
		kq= thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AB))}a")
		kq2= thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AD))}a")
		kq3= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so((t+1)/t*AB))}a", f"{latex(my_module.hien_phan_so((t+1)/t*AD))}a"] ))
		kq4= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so(t*AB))}a",f"{latex(my_module.hien_phan_so(t*AD))}a" ]))
		
		noi_dung_loigiai=f" Vì ${B1}{A1} \\bot {A1}{D1}, {B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{D1})$."\
		f" Suy ra $d({B1},(S{A1}{D1}))={B1}{A1}={AB}a$.\n\n"\
		f"$\\dfrac{{ d({M1},(S{A1}{D1})) }} {{ d({B1},(S{A1}{D1})) }} = \\dfrac{{S{M1}}} {{S{B1}}} = {latex(my_module.hien_phan_so(t/(t+1)))}$"\
		f"$\\Rightarrow d({M1},(S{A1}{D1}) = {latex(my_module.hien_phan_so(t/(t+1)))} d({B1},(S{A1}{D1})) = {latex(my_module.hien_phan_so(t/(t+1)))} {AB}a={latex(my_module.hien_phan_so(t/(t+1)*AB))}a$."
		noi_dung_loigiai=thay_hinh_hoc(noi_dung_loigiai)

	
	if chon==4:		
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a$."\
		f" Gọi ${{{M1}}}$ là điểm thuộc cạnh ${{S{D1}}}$ sao cho $S{{{M1}}}={t1}{M1}{D1}$. Tính khoảng cách từ điểm ${{{M1}}}$ đến mặt phẳng $(S{A1}{B1})$."
		
		kq= thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AD))}a")
		kq2= thay_hinh_hoc(f"{latex(my_module.hien_phan_so(t/(t+1)*AB))}a")
		kq3= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so((t+1)/t*AB))}a", f"{latex(my_module.hien_phan_so((t+1)/t*AD))}a"] ))
		kq4= thay_hinh_hoc(random.choice([f"{latex(my_module.hien_phan_so(t*AB))}a",f"{latex(my_module.hien_phan_so(t*AD))}a" ]))
		
		noi_dung_loigiai=f" Vì ${D1}{A1} \\bot {A1}{B1}, {D1}{A1}\\bot S{A1} \\Rightarrow {D1}{A1} \\bot (S{A1}{B1})$."\
		f" Suy ra $d({D1},(S{A1}{B1}))={D1}{A1}={AD}a$.\n\n"\
		f"$\\dfrac{{ d({M1},(S{A1}{B1})) }} {{ d({D1},(S{A1}{B1})) }} = \\dfrac{{S{M1}}} {{S{D1}}} = {latex(my_module.hien_phan_so(t/(t+1)))}$"\
		f"$\\Rightarrow d({M1},(S{A1}{D1}) = {latex(my_module.hien_phan_so(t/(t+1)))} d({D1},(S{A1}{B1})) = {latex(my_module.hien_phan_so(t/(t+1)))} {AD}a={latex(my_module.hien_phan_so(t/(t+1)*AD))}a$."
		noi_dung_loigiai=thay_hinh_hoc(noi_dung_loigiai)		


	noi_dung=thay_hinh_hoc(noi_dung)	

	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_03]-M3. S.ABCD: ABCD h.chữ nhật. Tính k.c từ chân đường cao đến mặt nghiêng.
def uvxy9_L11_C8_B4_03(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I", "N", "F", "K", "P", "G"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,2)
	
	if chon==1:		
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		SA=random.choice([sqrt(2), sqrt(3), sqrt(5), random.randint(2,6) ])

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a, S{A1}={latex(SA)}a$."\
		f" Tính khoảng cách từ điểm ${{{A1}}}$ đến mặt phẳng $(S{C1}{D1})$."

		kq= (SA*AD)/sqrt(SA**2+AD**2)
		kq2=(SA*AD)/sqrt(SA**2+AB**2)
		kq3= random.choice([(SA+AD)/sqrt(SA**2+AB**2), (AB*AD)/sqrt(AB**2+AD**2)])
		kq4= random.choice([(SA+AB)/sqrt(SA**2+AB**2), (AB+AD)/sqrt(AB**2+AD**2)])
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]		

		noi_dung_loigiai=f" Vì ${C1}{D1} \\bot {A1}{D1}, {C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$."\
		f" Kẻ ${A1}H \\bot S{D1}$. Ta có: ${A1}H \\bot {C1}{D1} \\Rightarrow {A1}H \\bot (S{C1}{D1})$.\n\n"\
		f"$\\Rightarrow d({A1}, (S{C1}{D1}))={A1}H=\\dfrac{{S{A1}.{A1}{D1}}} {{\\sqrt{{S{A1}^2 + {A1}{D1}^2 }} }}$"\
		f"$=\\dfrac{{{latex(SA)}a.{AD}a}} {{\\sqrt{{ {SA**2}a^2 + {AD**2}a^2 }} }} ={latex(kq)}a$."
		noi_dung_loigiai=thay_hinh_hoc(noi_dung_loigiai)

	
	if chon==2:
		
		AB=random.randint(1,9)
		AD=AB + random.randint(1,6)
		SA=random.choice([sqrt(2), sqrt(3), sqrt(5), random.randint(2,6) ])

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Biết ${A1}{B1}={AB}a,{A1}{D1}={AD}a, S{A1}={latex(SA)}a$."\
		f" Tính khoảng cách từ điểm ${{{A1}}}$ đến mặt phẳng $(S{B1}{C1})$."

		kq= (SA*AB)/sqrt(SA**2+AB**2)
		kq2=(SA*AD)/sqrt(SA**2+AD**2)
		kq3= random.choice([(SA+AD)/sqrt(SA**2+AB**2), (AB*AD)/sqrt(AB**2+AD**2)])
		kq4= random.choice([(SA+AB)/sqrt(SA**2+AB**2), (AB+AD)/sqrt(AB**2+AD**2)])
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]		

		noi_dung_loigiai=f" Vì ${C1}{B1} \\bot {A1}{B1}, {C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$."\
		f" Kẻ ${A1}H \\bot S{B1}$. Ta có: ${A1}H \\bot {C1}{B1} \\Rightarrow {A1}H \\bot (S{B1}{C1})$.\n\n"\
		f"$\\Rightarrow d({A1}, (S{B1}{C1}))={A1}H=\\dfrac{{S{A1}.{A1}{B1}}} {{\\sqrt{{S{A1}^2 + {A1}{B1}^2 }} }}$"\
		f"$=\\dfrac{{{latex(SA)}a.{AB}a}} {{\\sqrt{{ {SA**2}a^2 + {AB**2}a^2 }} }} ={latex(kq)}a$."
		noi_dung_loigiai=thay_hinh_hoc(noi_dung_loigiai)

	noi_dung=thay_hinh_hoc(noi_dung)	

	#Tạo các phương án
	pa_A= thay_hinh_hoc(f"*${{{latex(kq)}}}a$")
	pa_B= thay_hinh_hoc(f"${{{latex(kq2)}}}a$")
	pa_C= thay_hinh_hoc(f"${{{latex(kq3)}}}a$")
	pa_D= thay_hinh_hoc(f"${{{latex(kq4)}}}a$")



	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_04]-M2. Cho hình lăng trụ đứng tam giác. Tính khoảng cách từ điểm đến mặt đứng
def uvxy9_L11_C8_B4_04():
	A=["A","B","C"]
	B=["B","C","A"]
	C=["C","A","B"]
	A1=["A'","B'","C'"]
	B1=["B'","C'","A'"]
	C1=["C'","A'","B'"]
	
	i=random.randint(0,2)
	A, B, C, A1, B1, C1 = A[i], B[i], C[i], A1[i], B1[i], C1[i]
	code_hinh=my_module.code_hinh_langtrudung_tamgiac(A,B,C,A1,B1,C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	ten_langtru = f"{A}{B}{C}.{A1}{B1}{C1}"
	ten_AB=random.choice([f"{A}{B}",f"{A1}{B1}"])
	ten_BC=random.choice([f"{B}{C}",f"{B1}{C1}"])
	ten_AC=random.choice([f"{A}{C}",f"{A1}{C1}"])
	ten_AA1=random.choice([f"{A}{A1}", f"{B}{B1}", f"{C}{C1}"])

	chon=random.randint(1,4)
	if chon==1:
		AB, AC=random.randint(1,10), random.randint(1,10)
		BC=sqrt(AB**2+AC**2)
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác vuông tại ${{{A}}}, {ten_BC}={latex(BC)}a, {ten_AC}={AC}a,$\n\n${ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{C}}}$ đến mặt phẳng ${{({A}{B}{B1}{A1})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có ${C}{A}\\bot {A}{B},{C}{A}\\bot {A}{A1} \\Rightarrow {C}{A}\\bot {{({A}{B}{B1}{A1})}}$.\n\n"\
		f"Do đó: $d\\left({C},({A}{B}{B1}{A1})\\right)={C}{A}={AC}a$.")

		kq=AC
		kq2=BC
		kq3=AA1
		if AB!= AC:
			kq4=AB
		else:
			kq4=random.randint(2,5)*AA1
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
		
	    #Tạo các phương án
		pa_A= f"*${{{kq}}}a$"
		pa_B= f"${{{latex(kq2)}}}a$"
		pa_C= f"${{{latex(kq3)}}}a$"
		pa_D= f"${{{latex(kq4)}}}a$"
	if chon ==2:
	
		AB, AC=random.randint(1,10), random.randint(1,10)
		BC=sqrt(AB**2+AC**2)
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác vuông tại ${{{A}}}, {ten_AB}={latex(AB)}a, {ten_AC}={AC}a,$\n\n${ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{B}}}$ đến mặt phẳng ${{({A}{C}{C1}{A1})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có ${B}{A}\\bot {A}{C},{B}{A}\\bot {A}{A1} \\Rightarrow {B}{A}\\bot {{({A}{C}{C1}{A1})}}$.\n\n"\
		f"Do đó: $d\\left({B},({A}{C}{C1}{A1})\\right)={B}{A}={AB}a$.")

		kq=AB
		kq2=BC
		kq3=AA1
		if AB!= AC:
			kq4=AC
		else:
			kq4=random.randint(2,5)*AA1
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
		
	    #Tạo các phương án
		pa_A= f"*${{{kq}}}a$"
		pa_B= f"${{{latex(kq2)}}}a$"
		pa_C= f"${{{latex(kq3)}}}a$"
		pa_D= f"${{{latex(kq4)}}}a$"

	if chon==3:
		AB, BC=random.randint(1,10), random.randint(1,10)
		AC=sqrt(AB**2+BC**2)
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác vuông tại ${{{B}}}, {ten_AB}={latex(AB)}a, {ten_AC}={latex(AC)}a,$\n\n${ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{A}}}$ đến mặt phẳng ${{({B}{C}{C1}{B1})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có ${A}{B}\\bot {B}{C},{A}{B}\\bot {A}{A1} \\Rightarrow {A}{B}\\bot {{({B}{C}{C1}{B1})}}$.\n\n"\
		f"Do đó: $d\\left({A},({B}{C}{C1}{B1})\\right)={A}{B}={AB}a$.")

		kq=AB
		kq2=AC
		kq3=AA1
		if AB!= BC:
			kq4=BC
		else:
			kq4=random.randint(2,5)*AA1
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
		
	    #Tạo các phương án
		pa_A= f"*${{{kq}}}a$"
		pa_B= f"${{{latex(kq2)}}}a$"
		pa_C= f"${{{latex(kq3)}}}a$"
		pa_D= f"${{{latex(kq4)}}}a$"

	if chon==4:
		AB, BC=random.randint(1,10), random.randint(1,10)
		AC=sqrt(AB**2+BC**2)
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác vuông tại ${{{B}}}, {ten_BC}={BC}a, {ten_AC}={latex(AC)}a,$\n\n${ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{C}}}$ đến mặt phẳng ${{({A}{B}{B1}{A1})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có ${C}{B}\\bot {A}{B},{C}{B}\\bot {A}{A1} \\Rightarrow {C}{B}\\bot {{({A}{B}{B1}{A1})}}$.\n\n"\
		f"Do đó: $d\\left({C},({A}{B}{B1}{A1})\\right)={C}{B}={BC}a$.")

		kq=BC
		kq2=AC
		kq3=AA1
		if AB!= BC:
			kq4=BC
		else:
			kq4=random.randint(2,5)*AA1
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
		
	    #Tạo các phương án
		pa_A= f"*${{{kq}}}a$"
		pa_B= f"${{{latex(kq2)}}}a$"
		pa_C= f"${{{latex(kq3)}}}a$"
		pa_D= f"${{{latex(kq4)}}}a$"	

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n    {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_09]-M3. Cho hình lăng trụ đứng tam giác. Tính khoảng cách từ điểm đến mặt nghiêng
def uvxy9_L11_C8_B4_09():
	A=["A","B","C"]
	B=["B","C","A"]
	C=["C","A","B"]
	A1=["A'","B'","C'"]
	B1=["B'","C'","A'"]
	C1=["C'","A'","B'"]
	
	i=random.randint(0,2)
	A, B, C, A1, B1, C1 = A[i], B[i], C[i], A1[i], B1[i], C1[i]
	code_hinh=my_module.code_hinh_langtrudung_tamgiac(A,B,C,A1,B1,C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	ten_langtru = f"{A}{B}{C}.{A1}{B1}{C1}"
	ten_AB=random.choice([f"{A}{B}",f"{A1}{B1}"])
	ten_BC=random.choice([f"{B}{C}",f"{B1}{C1}"])
	ten_AC=random.choice([f"{A}{C}",f"{A1}{C1}"])
	ten_AA1=random.choice([f"{A}{A1}", f"{B}{B1}", f"{C}{C1}"])

	chon=random.randint(1,4)
	
	if chon==1:
		BC, AC=random.randint(1,10), random.randint(1,10)
		AB=sqrt(BC**2+AC**2)
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác vuông tại ${{{C}}}, {ten_BC}={latex(BC)}a, {ten_AC}={latex(AC)}a,$\n\n${ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{A}}}$ đến mặt phẳng ${{({A1}{B}{C})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có: ${B}{C}\\bot ({A}{C}{C1}{A1})$. Kẻ ${A}H\\bot {A1}{C} \\Rightarrow {A}H\\bot {{({A1}{B}{C})}}$.\n\n"\
		f"Do đó: $d\\left({A},({A1}{B}{C})\\right)={A}H=\\dfrac{{{A1}{A}.{A}{C}}} {{{A1}{C}}}=\\dfrac{{{latex(AA1)}a.{latex(AC)}a.}} {{\\sqrt{{{latex(AA1**2)}a^2+{latex(AC**2)}a^2}}}}$"\
		f"$={latex(AA1*AC/sqrt(AA1**2+AC**2))}a.$")

		kq=(AA1*AC)/sqrt(AA1**2+AC**2)
		kq2=BC
		kq3=AA1
		kq4=(AA1*BC)/sqrt(AA1**2+BC**2)
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
		


	if chon==2:
		AB, BC=random.randint(1,10), random.randint(1,10)
		AC=sqrt(AB**2+BC**2)
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác vuông tại ${{{B}}}, {ten_BC}={latex(BC)}a, {ten_AC}={latex(AC)}a,$\n\n${ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{A}}}$ đến mặt phẳng ${{({A1}{B}{C})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có: ${B}{C}\\bot ({A}{B}{B1}{A1})$. Kẻ ${A}H\\bot {A1}{B} \\Rightarrow {A}H\\bot {{({A1}{B}{C})}}$.\n\n"\
		f"Do đó: $d\\left({A},({A1}{B}{C})\\right)={A}H=\\dfrac{{{A1}{A}.{A}{B}}} {{{A1}{B}}}=\\dfrac{{{latex(AA1)}a.{latex(AB)}a.}} {{\\sqrt{{{latex(AA1**2)}a^2+{latex(AB**2)}a^2}}}}$"\
		f"$={latex(AA1*AB/sqrt(AA1**2+AB**2))}a.$")

		kq=(AA1*AB)/sqrt(AA1**2+AB**2)
		kq2=BC
		kq3=AA1
		kq4=(AA1*BC)/sqrt(AA1**2+BC**2)
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]


	if chon==3:
		ten_canh=random.choice(["AB","BC","AC"])
		AB=random.randint(1,8)
		AM=AB*sqrt(3)/2
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác đều, ${ten_canh}={AB}a,{ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{A}}}$ đến mặt phẳng ${{({A1}{B}{C})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"Gọi ${{M}}$ là trung điểm cạnh ${{{B}{C}}}\\Rightarrow {B}{C}\\bot ({A1}{A}M), {A}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
			f"Kẻ ${A}H\\bot {A1}M \\Rightarrow {A}H\\bot {{({A1}{B}{C})}}$.\n\n"\
		f"Do đó: $d\\left({A},({A1}{B}{C})\\right)={A}H=\\dfrac{{{A1}{A}.{A}M}} {{{A1}M}}=\\dfrac{{{latex(AA1)}a.{latex(AM)}a}} {{\\sqrt{{{latex(AA1**2)}a^2+{latex(AM**2)}a^2}}}}$"\
		f"$={latex(AA1*AM/sqrt(AA1**2+AM**2))}a.$")

		kq=(AA1*AM)/sqrt(AA1**2+AM**2)
		kq2=AB
		kq3=AA1
		kq4=(AA1*AB)/sqrt(AA1**2+AB**2)
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
	

	if chon==4:
		ten_canh=random.choice(["AB","BC","AC"])
		AB=random.randint(1,8)
		AM=AB*sqrt(3)/2
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác đều, ${ten_canh}={AB}a,{ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{B1}}}$ đến mặt phẳng ${{({A1}{B}{C})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"${{{A}{B1}}}$ cắt $({A1}{B}{C})$ tại trung điểm nên $d\\left({B1},({A1}{B}{C})\\right)=d\\left({A},({A1}{B}{C})\\right)$.\n\n"\
			f"Gọi ${{M}}$ là trung điểm cạnh ${{{B}{C}}}\\Rightarrow {B}{C}\\bot ({A1}{A}M), {A}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
			f"Kẻ ${A}H\\bot {A1}M \\Rightarrow {A}H\\bot {{({A1}{B}{C})}}$.\n\n"\
		f"Do đó: $d\\left({A},({A1}{B}{C})\\right)={A}H=\\dfrac{{{A1}{A}.{A}M}} {{{A1}M}}=\\dfrac{{{latex(AA1)}a.{latex(AM)}a}} {{\\sqrt{{{latex(AA1**2)}a^2+{latex(AM**2)}a^2}}}}$"\
		f"$={latex(AA1*AM/sqrt(AA1**2+AM**2))}a.$")

		kq=(AA1*AM)/sqrt(AA1**2+AM**2)
		kq2=AB
		kq3=AA1
		kq4=(AA1*AB)/sqrt(AA1**2+AB**2)
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

	if chon==5:
		ten_canh=random.choice(["AB","BC","AC"])
		AB=random.randint(1,8)
		AM=AB*sqrt(3)/2
		
		list_AA1=[sqrt(i) for i in range(1,20)]
		random.shuffle(list_AA1)
		AA1 = random.choice([random.randint(1,10),list_AA1[0]])
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{ABC.A'B'C'}}$ có đáy là tam giác đều, ${ten_canh}={AB}a,{ten_AA1}={latex(AA1)}a$."\
		f" Khoảng cách từ điểm ${{{C1}}}$ đến mặt phẳng ${{({A1}{B}{C})}}$ bằng")

		noi_dung_loigiai=thay_hinh_hoc(f"${{{A}{C1}}}$ cắt $({A1}{B}{C})$ tại trung điểm nên $d\\left({C1},({A1}{B}{C})\\right)=d\\left({A},({A1}{B}{C})\\right)$.\n\n"\
			f"Gọi ${{M}}$ là trung điểm cạnh ${{{B}{C}}}\\Rightarrow {B}{C}\\bot ({A1}{A}M), {A}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
			f"Kẻ ${A}H\\bot {A1}M \\Rightarrow {A}H\\bot {{({A1}{B}{C})}}$.\n\n"\
		f"Do đó: $d\\left({A},({A1}{B}{C})\\right)={A}H=\\dfrac{{{A1}{A}.{A}M}} {{{A1}M}}=\\dfrac{{{latex(AA1)}a.{latex(AM)}a}} {{\\sqrt{{{latex(AA1**2)}a^2+{latex(AM**2)}a^2}}}}$"\
		f"$={latex(AA1*AM/sqrt(AA1**2+AM**2))}a.$")

		kq=(AA1*AM)/sqrt(AA1**2+AM**2)
		kq2=AB
		kq3=AA1
		kq4=(AA1*AB)/sqrt(AA1**2+AB**2)
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{latex(kq)}}}a$"
	pa_B= f"${{{latex(kq2)}}}a$"
	pa_C= f"${{{latex(kq3)}}}a$"
	pa_D= f"${{{latex(kq4)}}}a$"


	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n    {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_10]-SA-M4. L.trụ đứng tam giác. Tính khoảng cách điểm đến mặt.
def uvxy9_L11_C8_B4_10():
	chon=random.randint(1,3)
	if chon==1:
		A,B,C,A1,B1,C1="A","B","C","A'","B'","C'"
	
	if chon==2:
		A,B,C,A1,B1,C1="A","B","C","A_1","B_1","C_1"

	if chon==3:
		A,B,C,A1,B1,C1="A","B","C","D","E","F"	
	

	code_hinh=my_module.code_hinh_langtrudung_tamgiac(A,B,C,A1,B1,C1)
	
	
	ten_lt= f"{A}{B}{C}.{A1}{B1}{C1}"
	ten_AB=random.choice([f"{A}{B}",f"{A1}{B1}"])
	ten_BC=random.choice([f"{B}{C}",f"{B1}{C1}"])
	ten_AC=random.choice([f"{A}{C}",f"{A1}{C1}"])
	ten_AA1=random.choice([f"{A}{A1}", f"{B}{B1}", f"{C}{C1}"])
	ten_diem=["M","N","P","Q"]
	M,N=random.sample(ten_diem,2)
	
	BM=random.randint(1,4)
	BC=BM*2
	AB=sqrt(random.randint(1,9))	
	AA1=random.choice([1,2,3,4,sqrt(2),sqrt(3),sqrt(5),sqrt(7)])
	BI=(AB*BM)/sqrt(AB**2+BM**2)
	BN=AA1/2
	BH=(BN*BI)/sqrt(BN**2+BI**2)
	dap_an=f"{round_half_up(BH,1):.1f}".replace(".",",")
	
	chon=random.randint(1,3)
	code_LG=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}}; \n\
    \\coordinate ({B}) at (2,-1) node at ({B}) [below] {{${B}$}}; \n\
    \\coordinate ({C}) at (4,0)  node at ({C}) [below] {{${C}$}}; \n\
    \\coordinate ({A1}) at (0,4)   node at ({A1}) [above] {{${A1}$}}; \n\
    \\coordinate ({B1}) at (2,3)   node at ({B1}) [above] {{${B1}$}}; \n\
    \\coordinate ({C1}) at (4,4)   node at ({C1}) [above] {{${C1}$}};\n\
    \\coordinate ({M}) at ($({B})!0.5!({C})$) node at ({M}) [below] {{${M}$}};\n\
    \\coordinate ({N}) at ($({B1})!0.5!({B})$) node at ({N}) [above right] {{${N}$}};\n\
    \\coordinate (I) at ($({A})!0.5!({M})$) node at (I) [below] {{$I$}};\n\
    \\coordinate (H) at ($({N})!0.5!(I)$) node at (H) [left] {{$H$}};\n\
    \\draw [dashed] ({A})--({C}) ({A})--({M})  ({B})--(I) ({B})--(H) ({N})--(I); \n\
    \\draw ({A})--({B})--({B1})--({A1})--({A}) ({A})--({N}) ({M})--({N}) ; \n\
    \\draw ({B1})--({C1})--({C})--({B}) ({A1})--({C1})--({C}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
	code = my_module.moi_truong_anh_latex(code_LG)
	file_name = my_module.pdftoimage_timename(code)

	
	if chon==1:
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có đáy là tam giác vuông tại ${{{B}}}$ và có độ dài các cạnh"
			f" ${ten_BC}={latex(BC)}, {ten_AB}={latex(AB)},{ten_AA1}={latex(AA1)}$."
			f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{B}{C}}}$ và ${{{B}{B1}}}$."
		f" Tính khoảng cách từ điểm ${{{B}}}$ đến mặt phẳng ${{({A}{M}{N})}}$(kết quả làm tròn đến hàng phần mười).")	

		noi_dung_loigiai=(
		f"Kẻ ${B}I\\bot {A}{M}, {B}H \\bot {N}I$. Chứng minh được ${B}H\\bot ({A}{M}{N})$,\n\n"
		f"Suy ra $d({B},({A}{M}{N}))={B}H$.\n\n"
		f"${B}{M}=\\dfrac{{{B}{C}}}{{2}}={BM}, {B}{N}=\\dfrac{{{B}{B1}}}{{2}}={latex(AA1/2)}$.\n\n"
		f"${B}I=\\dfrac{{{B}{A}.{B}{M}}}{{\\sqrt{{{B}{A}^2+{B}{M}^2}}}}=\\dfrac{{{latex(AB)}.{BM} }}{{\\sqrt{{{AB**2}+{BM**2}}}}}={latex(nsimplify(BI))}$.\n\n"
		f"${B}H=\\dfrac{{{B}{N}.{B}I}}{{\\sqrt{{{B}{N}^2+{B}{I}^2}}}}=\\dfrac{{{latex(BN)}.{latex(nsimplify(BI))}}}{{\\sqrt{{{phan_so(BN**2)}+{phan_so(BI**2)}}}}}$"
		f"$={latex(nsimplify(BH))}={dap_an}$.")
	
	if chon==2:
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có đáy là tam giác vuông tại ${{{B}}}$ và có độ dài các cạnh"
			f" ${ten_BC}={latex(BC)}, {ten_AB}={latex(AB)},{ten_AA1}={latex(AA1)}$."
			f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{B}{C}}}$ và ${{{B}{B1}}}$."
		f" Tính khoảng cách từ điểm ${{{C}}}$ đến mặt phẳng ${{({A}{M}{N})}}$(kết quả làm tròn đến hàng phần mười).")	

		noi_dung_loigiai=(
		f"Do ${{{B}{C}}}$ cắt mặt phẳng ${{({A}{M}{N})}}$ tại trung điểm ${{{M}}}$ nên $d({C},({A}{M}{N}))=d({B},({A}{M}{N}))$.\n\n"
		f"Kẻ ${B}I\\bot {A}{M}, {B}H \\bot {N}I$. Chứng minh được ${B}H\\bot ({A}{M}{N})$,\n\n"
		f"Suy ra $d({B},({A}{M}{N}))={B}H$.\n\n"
		f"${B}{M}=\\dfrac{{{B}{C}}}{{2}}={BM}, {B}{N}=\\dfrac{{{B}{B1}}}{{2}}={latex(AA1/2)}$.\n\n"
		f"${B}I=\\dfrac{{{B}{A}.{B}{M}}}{{\\sqrt{{{B}{A}^2+{B}{M}^2}}}}=\\dfrac{{{latex(AB)}.{BM} }}{{\\sqrt{{{AB**2}+{BM**2}}}}}={latex(nsimplify(BI))}$.\n\n"
		f"${B}H=\\dfrac{{{B}{N}.{B}I}}{{\\sqrt{{{B}{N}^2+{B}{I}^2}}}}=\\dfrac{{{latex(BN)}.{latex(nsimplify(BI))}}}{{\\sqrt{{{phan_so(BN**2)}+{phan_so(BI**2)}}}}}$"
		f"$={latex(nsimplify(BH))}={dap_an}$.")

	if chon==3:
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có đáy là tam giác vuông tại ${{{B}}}$ và có độ dài các cạnh"
			f" ${ten_BC}={latex(BC)}, {ten_AB}={latex(AB)},{ten_AA1}={latex(AA1)}$."
			f" Gọi ${{{M},{N}}}$ lần lượt là trung điểm của ${{{B}{C}}}$ và ${{{B}{B1}}}$."
		f" Tính khoảng cách từ điểm ${{{B1}}}$ đến mặt phẳng ${{({A}{M}{N})}}$(kết quả làm tròn đến hàng phần mười).")	

		noi_dung_loigiai=(
		f"Do ${{{B}{B1}}}$ cắt mặt phẳng ${{({A}{M}{N})}}$ tại trung điểm ${{{N}}}$ nên $d({B1},({A}{M}{N}))=d({B},({A}{M}{N}))$.\n\n"
		f"Kẻ ${B}I\\bot {A}{M}, {B}H \\bot {N}I$. Chứng minh được ${B}H\\bot ({A}{M}{N})$,\n\n"
		f"Suy ra $d({B},({A}{M}{N}))={B}H$.\n\n"
		f"${B}{M}=\\dfrac{{{B}{C}}}{{2}}={BM}, {B}{N}=\\dfrac{{{B}{B1}}}{{2}}={latex(AA1/2)}$.\n\n"
		f"${B}I=\\dfrac{{{B}{A}.{B}{M}}}{{\\sqrt{{{B}{A}^2+{B}{M}^2}}}}=\\dfrac{{{latex(AB)}.{BM} }}{{\\sqrt{{{AB**2}+{BM**2}}}}}={latex(nsimplify(BI))}$.\n\n"
		f"${B}H=\\dfrac{{{B}{N}.{B}I}}{{\\sqrt{{{B}{N}^2+{B}{I}^2}}}}=\\dfrac{{{latex(BN)}.{latex(nsimplify(BI))}}}{{\\sqrt{{{phan_so(BN**2)}+{phan_so(BI**2)}}}}}$"
		f"$={latex(nsimplify(BH))}={dap_an}$.")
	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name}\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{\\begin{{center}}\n{code_LG}\n\\end{{center}} \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an


#KHOẢNG CÁCH GIỮA 2 ĐƯỜNG CHÉO NHAU
#[D11_C8_B4_05]-M2. Cho hình lập phương. Tính khoảng cách giữa 2 đường chéo nhau (kẻ đường vuông góc chung)
def uvxy9_L11_C8_B4_05():   	
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	a=random.choice([sqrt(i) for i in range(2,100)])
	chon=random.randint(1,7)

	if chon==1:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{A{A1}}}$ và ${{BC}}$ bằng"
		noi_dung_loigiai=f"Ta có: $AB\\bot BC, AB \\bot A{A1} \\Rightarrow d(A{A1},BC)=AB={latex(a)}a$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2
	
	if chon==2:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{A{A1}}}$ và ${{CD}}$ bằng"
		noi_dung_loigiai=f"Ta có: $AD\\bot CD, AD \\bot A{A1} \\Rightarrow d(A{A1},CD)=AD={latex(a)}$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2

	if chon==3:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{A{A1}}}$ và ${{{C1}{D1}}}$ bằng"
		noi_dung_loigiai=f"Ta có: ${A1}{D1}\\bot {C1}{D1}, {A1}{D1} \\bot A{A1} \\Rightarrow d(A{A1},{C1}{D1})={A1}{D1}={latex(a)}$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2

	if chon==4:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{A{A1}}}$ và ${{{B1}{C1}}}$ bằng"
		noi_dung_loigiai=f"Ta có: ${A1}{B1}\\bot {B1}{C1}, {A1}{B1} \\bot A{A1} \\Rightarrow d(A{A1},{B1}{C1})={A1}{B1}={latex(a)}$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2
	
	if chon==5:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{B{B1}}}$ và ${{AD}}$ bằng"
		noi_dung_loigiai=f"Ta có: $AB\\bot B{B1}, AB \\bot AD \\Rightarrow d(B{B1},AD)=AB={latex(a)}$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2

	if chon==6:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{B{B1}}}$ và ${{{A1}{D1}}}$ bằng"
		noi_dung_loigiai=f"Ta có: ${A1}{B1}\\bot B{B1}, {A1}{B1} \\bot {A1}{D1} \\Rightarrow d(B{B1},{A1}{D1})={A1}{B1}={latex(a)}$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2

	if chon==7:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{A{A1}}}$ và ${{BD}}$ bằng"
		noi_dung_loigiai=f"Gọi $O=AC\\cap BD$.\n\n"\
		f"Ta có: $AO\\bot BD, AO \\bot A{A1} \\Rightarrow d(A{A1},BD)=AO={latex(a*sqrt(2)/2)}a$."
		kq=a*sqrt(2)/2
		kq2=a*sqrt(2)
		kq3=a
		kq4=a**2
	if chon==7:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{A{A1}}}$ và ${{BD}}$ bằng"
		noi_dung_loigiai=f"Gọi $O=AC\\cap BD$.\n\n"\
		f"Ta có: $AO\\bot BD, AO \\bot A{A1} \\Rightarrow d(A{A1},BD)=AO={latex(a*sqrt(2)/2)}a$."
		kq=a*sqrt(2)/2
		kq2=a*sqrt(2)
		kq3=a
		kq4=a**2

	if chon==8:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{B{B1}}}$ và ${{AC}}$ bằng"
		noi_dung_loigiai=f"Gọi $O=AC\\cap BD$.\n\n"\
		f"Ta có: $BO\\bot AC, BO \\bot B{B1} \\Rightarrow d(B{B1},AC)=BO={latex(a*sqrt(2)/2)}a$."
		kq=a*sqrt(2)/2
		kq2=a*sqrt(2)
		kq3=a
		kq4=a**2
	if chon==9:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{A{A1}}}$ và ${{{B1}{D1}}}$ bằng"
		noi_dung_loigiai=f"Gọi $O={A1}{C1}\\cap {B1}{D1}$.\n\n"\
		f"Ta có: ${A1}O\\bot {B1}{D1}, {A1}O \\bot A{A1} \\Rightarrow d(A{A1},{B1}{D1})={A1}O={latex(a*sqrt(2)/2)}a$."
		kq=a*sqrt(2)/2
		kq2=a*sqrt(2)
		kq3=a
		kq4=a**2

	if chon==10:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{B{B1}}}$ và ${{{A1}{C1}}}$ bằng"
		noi_dung_loigiai=f"Gọi $O={A1}{C1}\\cap {B1}{D1}$.\n\n"\
		f"Ta có: ${B1}O\\bot {A1}{C1}, {B1}O \\bot B{B1} \\Rightarrow d(B{B1},{A1}{C1})={B1}O={latex(rutgon_can(a*sqrt(2)/2))}a$."
		kq=a*sqrt(2)/2
		kq2=a*sqrt(2)
		kq3=a
		kq4=a**2
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	
    #Tạo các phương án
	pa_A= f"*${{{latex(rutgon_can(kq))}a}}$"
	pa_B= f"${{{latex(kq2)}a}}$"
	pa_C= f"${{{latex(kq3)}a}}$"
	pa_D= f"${{{latex(kq4)}a}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	  	

	code_hinh = my_module.code_hinh_lapphuong("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	
	debai= f"{noi_dung}\n\n"\
			f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n    {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_06]-M3. Cho hình lập phương. Tính khoảng cách giữa 2 đường chéo nhau (dựng mặt song song đường)
def uvxy9_L11_C8_B4_06():   	
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	a=random.choice([sqrt(i) for i in range(2,100)])
	chon=random.randint(1,4)
		
	if chon==1:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{{A1}B}}$ và ${{AD}}$ bằng"
		noi_dung_loigiai=f"Ta có: $AD//({A1}BC{D1}),{A1}B \\subset ({A1}BC{D1}) \\Rightarrow d({A1}B,AD)=d\\left(AD,({A1}BC{D1}))\\right)=d(A,(({A1}BC{D1}))$.\n\n"\
		f"Kẻ $AI\\bot {A1}B$ với $I$ là trung điểm của ${{A{B1}}}$ $\\Rightarrow  AI \\bot ({A1}BC{D1}) \\Rightarrow d({A1}B,BC)=AI=\\dfrac{{A{B1}}}{{2}}={latex(rutgon_can(a*sqrt(2)/2))}a$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2
	
	if chon==2:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{C{D1}}}$ và ${{AD}}$ bằng"
		noi_dung_loigiai=f"Ta có: $AD//({A1}BC{D1}),C{D1}\\subset ({A1}BC{D1}) \\Rightarrow d(C{D1},AD)=d\\left(AD,({A1}BC{D1}))\\right)=d(A,(({A1}BC{D1}))$.\n\n"\
		f"Kẻ $AI\\bot {A1}B$ với $I$ là trung điểm của ${{A{B1}}}$ $\\Rightarrow  AI \\bot ({A1}BC{D1}) \\Rightarrow d({A1}B,BC)=AI=\\dfrac{{A{B1}}}{{2}}={latex(rutgon_can(a*sqrt(2)/2))}a$."
		kq=a
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2

	if chon==3:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{{A1}B}}$ và ${{{B1}{C1}}}$ bằng"
		noi_dung_loigiai=f"Ta có: ${B1}{C1}//({A1}BC{D1}),{A1}B \\subset ({A1}BC{D1}) \\Rightarrow d({A1}B,{B1}{C1})=d\\left({B1}{C1},({A1}BC{D1}))\\right)=d({B1},(({A1}BC{D1}))$.\n\n"\
		f"Kẻ ${B1}I\\bot {A1}B$ với $I$ là trung điểm của ${{A{B1}}}$\n\n $\\Rightarrow  {B1}I \\bot ({A1}BC{D1}) \\Rightarrow d({A1}B,{B1}{C1})={B1}I=\\dfrac{{A{B1}}}{{2}}={latex(rutgon_can(a*sqrt(2)/2))}a$."
		kq=a*sqrt(2)/2
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2

	if chon==4:
		noi_dung=f" Cho hình lập phương ${{ABCD.{A1}{B1}{C1}{D1}}}$ có cạnh bằng ${{{latex(a)}a}}$."\
		f" Khoảng cách giữa hai đường thẳng ${{C{D1}}}$ và ${{{B1}{C1}}}$ bằng"
		noi_dung_loigiai=f"Ta có: ${B1}{C1}//({A1}BC{D1}),C{D1} \\subset ({A1}BC{D1}) \\Rightarrow d(C{D1},{B1}{C1})=d\\left({B1}{C1},({A1}BC{D1}))\\right)=d({B1},(({A1}BC{D1}))$.\n\n"\
		f"Kẻ ${B1}I\\bot {A1}B$ với $I$ là trung điểm của ${{A{B1}}}$ \n\n$\\Rightarrow  {B1}I \\bot ({A1}BC{D1}) \\Rightarrow d({A1}B,{B1}{C1})={B1}I=\\dfrac{{A{B1}}}{{2}}={latex(rutgon_can(a*sqrt(2)/2))}a$."
		kq=a*sqrt(2)/2
		kq2=a*sqrt(2)
		kq3=a*2
		kq4=a**2
	
	
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	
    #Tạo các phương án
	pa_A= f"*${{{latex(rutgon_can(kq))}a}}$"
	pa_B= f"${{{latex(kq2)}a}}$"
	pa_C= f"${{{latex(kq3)}a}}$"
	pa_D= f"${{{latex(kq4)}a}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	  	

	code_hinh = my_module.code_hinh_lapphuong("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	dap_an=my_module.tra_ve_dap_an(list_PA) 
	
	debai= f"{noi_dung}\n\n"\
			f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n    {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_07]-M2. S.ABCD: ABCD h.chữ nhật. Tính k.c 2 đường chéo nhau (đoạn vuông góc chung).
def uvxy9_L11_C8_B4_07(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I", "N", "F", "K", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	AB=random.randint(1,10)
	AD=AB+random.randint(2,4)
	SA=random.choice([sqrt(i) for i in range(1,100)])
	chon=random.randint(1,3)

	if chon==1:		
		noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a, {A1}{D1}={AD}a,S{A1}={latex(SA)}a$."\
			f" Tính khoảng cách giữa các đường thẳng ${{S{A1}}}$ và ${{{B1}{C1}}}$.")
		kq= f"${{{AB}a}}$"
		kq2= f"${{{AD}a}}$"
		kq3= f"${{{AB+AD}a}}$"
		kq4= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có: ${A1}{B1}\\bot {B1}{C1}, {A1}{B1}\\bot S{A1} \\Rightarrow d(S{A1},{B1}{C1})={A1}{B1}={AB}a$.")
	
	if chon==2:		
		noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a, {A1}{D1}={AD}a,S{A1}={latex(SA)}a$."\
			f" Tính khoảng cách giữa các đường thẳng ${{S{A1}}}$ và ${{{C1}{D1}}}$.")
		kq= f"${{{AD}a}}$"
		kq2= f"${{{AB}a}}$"
		kq3= f"${{{AB+AD}a}}$"
		kq4= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"

		noi_dung_loigiai=thay_hinh_hoc(f"Ta có: ${A1}{D1}\\bot {C1}{D1}, {A1}{D1}\\bot S{A1} \\Rightarrow d(S{A1},{C1}{D1})={A1}{D1}={AD}a$.")

	
	if chon==3:		
		noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a, {A1}{D1}={AD}a,S{A1}={latex(SA)}a$."\
			f" Tính khoảng cách giữa các đường thẳng ${{S{A1}}}$ và ${{{B1}{D1}}}$.")
		d=(AB*AD)/sqrt(AB**2+AD**2)
		kq= f"${{{latex(d)}a}}$"
		kq2= f"${{{AB}a}}$"
		kq3= f"${{{AB+AD}a}}$"
		kq4= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"

		noi_dung_loigiai=thay_hinh_hoc(f"Kẻ ${A1}H\\bot {B1}{D1}\\Rightarrow {A1}H\\bot {B1}{D1}, {A1}H\\bot S{A1}\
			\\Rightarrow d(S{A1},{B1}{D1})={A1}H=\\dfrac{{{AB}a.{AD}a}}{{\\sqrt{{{AB**2}a^2+{AD**2}a^2}} }}={latex(d)}a$.")
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_08]-M2. S.ABCD: ABCD h.chữ nhật. Tính k.c 2 đường chéo nhau (tạo mặt song song đường).
def uvxy9_L11_C8_B4_08(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I", "N", "F", "K", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	AB=random.randint(1,10)
	AD=AB+random.randint(2,4)
	SA=random.choice([sqrt(i) for i in range(1,50)])
	chon=random.randint(1,4)
	
	if chon==1:		
		noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a, {A1}{D1}={AD}a,S{A1}={latex(SA)}a$."\
			f" Tính khoảng cách giữa các đường thẳng ${{S{B1}}}$ và ${{{A1}{D1}}}$.")
		d=(SA*AB)/sqrt(SA**2+AB**2)
		d1=(SA*AD)/sqrt(SA**2+AD**2)

		kq= f"${{{latex(d)}a}}$"
		kq2= random.choice([f"${{{AB}a}}$", f"${{{AD}a}}$" ])
		kq3= f"${{{latex(d1)}a}}$"
		kq4= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"

		noi_dung_loigiai=thay_hinh_hoc(f"${A1}{D1} // (S{B1}{C1}), S{B1} \\subset (S{B1}{C1}) \\Rightarrow d(S{B1},{A1}{D1})=d({A1}{D1},(S{B1}{C1}))"\
			f"=d({A1},(S{B1}{C1})$.\n\n"\
			f"Kẻ ${A1}H\\bot S{B1}\\Rightarrow {A1}H\\bot (S{B1}{C1})"\
			f"\\Rightarrow d({A1},(S{B1}{C1}))={A1}H=\\dfrac{{{latex(SA)}a.{AB}a}}{{\\sqrt{{{SA**2}a^2+{AB**2}a^2}} }}={latex(d)}a$.")

	if chon==2:		
		noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a, {A1}{D1}={AD}a,S{A1}={latex(SA)}a$."\
			f" Tính khoảng cách giữa các đường thẳng ${{S{D1}}}$ và ${{{A1}{B1}}}$.")
		d=(SA*AD)/sqrt(SA**2+AD**2)
		d1=(SA*AB)/sqrt(SA**2+AB**2)

		kq= f"${{{latex(d)}a}}$"
		kq2= random.choice([f"${{{AB}a}}$", f"${{{AD}a}}$" ])
		kq3= f"${{{latex(d1)}a}}$"
		kq4= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"

		noi_dung_loigiai=thay_hinh_hoc(f"${A1}{B1} // (S{C1}{D1}), S{D1} \\subset (S{C1}{D1}) \\Rightarrow d(S{D1},{A1}{B1})=d({A1}{B1},(S{C1}{D1}))"\
			f"=d({A1},(S{C1}{D1})$.\n\n"\
			f"Kẻ ${A1}H\\bot S{D1}\\Rightarrow {A1}H\\bot (S{C1}{D1})"\
			f"\\Rightarrow d({A1},(S{C1}{D1}))={A1}H=\\dfrac{{{latex(SA)}a.{AD}a}}{{\\sqrt{{{SA**2}a^2+{AD**2}a^2}} }}={latex(d)}a$.")
	
	if chon==3:		
		noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a, {A1}{D1}={AD}a,S{A1}={latex(SA)}a$."\
			f" Tính khoảng cách giữa các đường thẳng ${{S{C1}}}$ và ${{{A1}{D1}}}$.")
		d=(SA*AB)/sqrt(SA**2+AB**2)
		d1=(SA*AD)/sqrt(SA**2+AD**2)

		kq= f"${{{latex(d)}a}}$"
		kq2= random.choice([f"${{{AB}a}}$", f"${{{AD}a}}$" ])
		kq3= f"${{{latex(d1)}a}}$"
		kq4= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"

		noi_dung_loigiai=thay_hinh_hoc(f"${A1}{D1} // (S{B1}{C1}), S{C1} \\subset (S{B1}{C1}) \\Rightarrow d(S{C1},{A1}{D1})=d({A1}{D1},(S{B1}{C1}))"\
			f"=d({A1},(S{B1}{C1})$.\n\n"\
			f"Kẻ ${A1}H\\bot S{B1}\\Rightarrow {A1}H\\bot (S{B1}{C1})"\
			f"\\Rightarrow d({A1},(S{B1}{C1}))={A1}H=\\dfrac{{{latex(SA)}a.{AB}a}}{{\\sqrt{{{SA**2}a^2+{AB**2}a^2}} }}={latex(d)}a$.")
    
	if chon==4:
		noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD), {A1}{B1}={AB}a, {A1}{D1}={AD}a,S{A1}={latex(SA)}a$."\
			f" Tính khoảng cách giữa các đường thẳng ${{S{C1}}}$ và ${{{A1}{B1}}}$.")
		d=(SA*AD)/sqrt(SA**2+AD**2)
		d1=(SA*AB)/sqrt(SA**2+AB**2)

		kq= f"${{{latex(d)}a}}$"
		kq2= random.choice([f"${{{AB}a}}$", f"${{{AD}a}}$" ])
		kq3= f"${{{latex(d1)}a}}$"
		kq4= f"${{{latex(sqrt(AB**2+AD**2))}a}}$"

		noi_dung_loigiai=thay_hinh_hoc(f"${A1}{B1} // (S{C1}{D1}), S{C1} \\subset (S{C1}{D1}) \\Rightarrow d(S{C1},{A1}{B1})=d({A1}{B1},(S{C1}{D1}))"\
			f"=d({A1},(S{C1}{D1})$.\n\n"\
			f"Kẻ ${A1}H\\bot S{D1}\\Rightarrow {A1}H\\bot (S{C1}{D1})"\
			f"\\Rightarrow d({A1},(S{C1}{D1}))={A1}H=\\dfrac{{{latex(SA)}a.{AD}a}}{{\\sqrt{{{SA**2}a^2+{AD**2}a^2}} }}={latex(d)}a$.")
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B4_12]-SA-M4. L.trụ đứng tam giác. Tính khoảng cách hai đường chéo nhau.
def uvxy9_L11_C8_B4_12():
	chon=random.randint(1,3)
	if chon==1:
		A,B,C,A1,B1,C1="A","B","C","A'","B'","C'"
	
	if chon==2:
		A,B,C,A1,B1,C1="A","B","C","A_1","B_1","C_1"

	if chon==3:
		A,B,C,A1,B1,C1="A","B","C","D","E","F"
	
	ten_lt= f"{A}{B}{C}.{A1}{B1}{C1}"
	ten_AB=random.choice([f"{A}{B}",f"{A1}{B1}"])
	ten_BC=random.choice([f"{B}{C}",f"{B1}{C1}"])
	ten_AC=random.choice([f"{A}{C}",f"{A1}{C1}"])
	ten_AA1=random.choice([f"{A}{A1}", f"{B}{B1}", f"{C}{C1}"])
	ten_diem=["M","N","P","Q"]
	M,N=random.sample(ten_diem,2)
	
	BM=random.randint(1,4)
	BC=BM*2
	AB=sqrt(random.randint(1,9))	
	AA1=random.choice([1,2,3,4,sqrt(2),sqrt(3),sqrt(5),sqrt(7)])
	BI=(AB*BM)/sqrt(AB**2+BM**2)
	BN=AA1/2
	BH=(BN*BI)/sqrt(BN**2+BI**2)
	dap_an=f"{round_half_up(BH,2):.2f}".replace(".",",")
	
	code_LG=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}}; \n\
    \\coordinate ({B}) at (2,-1) node at ({B}) [below] {{${B}$}}; \n\
    \\coordinate ({C}) at (4,0)  node at ({C}) [below] {{${C}$}}; \n\
    \\coordinate ({A1}) at (0,4)   node at ({A1}) [above] {{${A1}$}}; \n\
    \\coordinate ({B1}) at (2,3)   node at ({B1}) [above] {{${B1}$}}; \n\
    \\coordinate ({C1}) at (4,4)   node at ({C1}) [above] {{${C1}$}};\n\
    \\coordinate ({M}) at ($({B})!0.5!({C})$) node at ({M}) [below] {{${M}$}};\n\
    \\coordinate ({N}) at ($({B1})!0.5!({B})$) node at ({N}) [above right] {{${N}$}};\n\
    \\coordinate (I) at ($({A})!0.5!({M})$) node at (I) [below] {{$I$}};\n\
    \\coordinate (H) at ($({N})!0.5!(I)$) node at (H) [left] {{$H$}};\n\
    \\draw [dashed] ({A})--({C}) ({A})--({M})  ({B})--(I) ({B})--(H) ({N})--(I); \n\
    \\draw ({A})--({B})--({B1})--({A1})--({A}) ({A})--({N}) ({M})--({N}) ({B1})--({C}) ; \n\
    \\draw ({B1})--({C1})--({C})--({B}) ({A1})--({C1})--({C}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
	
	code = my_module.moi_truong_anh_latex(code_LG)
	file_name = my_module.pdftoimage_timename(code)
	
	
	noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có đáy là tam giác vuông tại ${{{B}}}$ và có độ dài các cạnh"
		f" ${ten_BC}={latex(BC)}, {ten_AB}={latex(AB)},{ten_AA1}={latex(AA1)}$."
		f" Gọi ${{{M}}}$ là trung điểm của ${{{B}{C}}}$."
	f" Tính khoảng cách giữa ${{{A}{M}}}$ và ${{{B1}{C}}}$(kết quả làm tròn đến hàng phần trăm).")	

	noi_dung_loigiai=(
	f"Gọi ${{{N}}}$ là trung điểm của ${B}{B1}$. Ta có: ${M}{N}//{B1}{C}\\Rightarrow {B1}{C}//({A}{M}{N})$.\n\n"
	f"Do đó: $d({A}{M},{B1}{C})=d(({A}{M}{N}),{B1}{C})=d({B1},({A}{M}{N}))=d({B},({A}{M}{N}))$.\n\n"
	f"Kẻ ${B}I\\bot {A}{M}, {B}H \\bot {N}I$. Chứng minh được ${B}H\\bot ({A}{M}{N})$,\n\n"
	f"Suy ra $d({B},({A}{M}{N}))={B}H$.\n\n"
	f"${B}{M}=\\dfrac{{{B}{C}}}{{2}}={BM}, {B}{N}=\\dfrac{{{B}{B1}}}{{2}}={latex(AA1/2)}$.\n\n"
	f"${B}I=\\dfrac{{{B}{A}.{B}{M}}}{{\\sqrt{{{B}{A}^2+{B}{M}^2}}}}=\\dfrac{{{latex(AB)}.{BM} }}{{\\sqrt{{{AB**2}+{BM**2}}}}}={latex(nsimplify(BI))}$.\n\n"
	f"${B}H=\\dfrac{{{B}{N}.{B}I}}{{\\sqrt{{{B}{N}^2+{B}{I}^2}}}}=\\dfrac{{{latex(BN)}.{latex(nsimplify(BI))}}}{{\\sqrt{{{phan_so(BN**2)}+{phan_so(BI**2)}}}}}$"
	f"$={latex(nsimplify(BH))}={dap_an}$.")	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name}\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{\\begin{{center}}\n{code_LG}\n\\end{{center}} \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C8_B4_13]-SA-M3. L.trụ đứng tam giác có 3 cạnh. Tính khoảng cách cạnh bên và cạnh đáy
def uvxy9_L11_C8_B4_13():
	chon=random.randint(1,3)
	if chon==1:
		A,B,C,A1,B1,C1="A","B","C","A'","B'","C'"
	
	if chon==2:
		A,B,C,A1,B1,C1="A","B","C","A_1","B_1","C_1"

	if chon==3:
		A,B,C,A1,B1,C1="A","B","C","D","E","F"	
	

	code_hinh=my_module.code_hinh_langtrudung_tamgiac(A,B,C,A1,B1,C1)
	
	
	ten_lt= f"{A}{B}{C}.{A1}{B1}{C1}"
	ten_AB=random.choice([f"{A}{B}",f"{A1}{B1}"])
	ten_BC=random.choice([f"{B}{C}",f"{B1}{C1}"])
	ten_AC=random.choice([f"{A}{C}",f"{A1}{C1}"])
	ten_AA1=random.choice([f"{A}{A1}", f"{B}{B1}", f"{C}{C1}"])
	ten_diem=["M","N","P","Q"]
	M,N=random.sample(ten_diem,2)
	
	while True:
		AB=random.randint(1,7)
		AC=random.randint(1,7)
		BC=random.randint(1,7)
		if all([AB+AC>BC, AB+BC>AC, AC+BC>AB]):
			break
	
	p=(AB+AC+BC)/2
	S=sqrt(p*(p-AB)*(p-AC)*(p-BC))
	AH=2*S/BC
	dap_an=f"{round_half_up(AH,2):.2f}".replace(".",",")

	chon=random.randint(1,4)	
	
	if chon==1:
		code_LG=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}}; \n\
    \\coordinate ({B}) at (2,-1) node at ({B}) [below] {{${B}$}}; \n\
    \\coordinate ({C}) at (4,0)  node at ({C}) [below] {{${C}$}}; \n\
    \\coordinate ({A1}) at (0,4)   node at ({A1}) [above] {{${A1}$}}; \n\
    \\coordinate ({B1}) at (2,3)   node at ({B1}) [above] {{${B1}$}}; \n\
    \\coordinate ({C1}) at (4,4)   node at ({C1}) [above] {{${C1}$}};\n\
    \\coordinate (H) at ($({B})!0.4!({C})$) node at (H) [right] {{$H$}};\n\
    \\draw [dashed] ({A})--({C})  ({A})--(H) ; \n\
    \\draw ({A})--({B})--({B1})--({A1})--({A}); \n\
    \\draw ({B1})--({C1})--({C})--({B}) ({A1})--({C1})--({C}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có ${ten_AB}={AB}, {ten_BC}={BC}, {ten_AC}={AC}$."
		f" Tính khoảng cách giữa ${{{A}{A1}}}$ và ${{{B}{C}}}$(kết quả làm tròn đến hàng phần trăm).")	

		noi_dung_loigiai=(
			f"Kẻ ${A}H\\bot {B}{C}$. Ta có: ${A}{A1}\\bot {A}H$ nên $d({A}{A1},{B}{C})={A}H$.\n\n"
			f"Xét tam giác ${{{A}{B}{C}}}$ có $p=\\dfrac{{{AB}+{AC}+{BC}}}{{2}}={phan_so(p)}$.\n\n"
			f"$S_{{{A}{B}{C}}}=\\sqrt{{{phan_so(p)}({phan_so(p)}-{AB})({phan_so(p)}-{AC})({phan_so(p)}-{BC})}}={{{latex(nsimplify(S))}}}$.\n\n"
			f"${A}H=\\dfrac{{2S_{{{A}{B}{C}}}}}{{{B}{C}}}=\\dfrac{{2.{latex(nsimplify(S))}}}{{{BC}}}={{{latex(nsimplify(AH))}}}={dap_an}$.")
	
	if chon==2:
		code_LG=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}}; \n\
    \\coordinate ({B}) at (2,-1) node at ({B}) [below] {{${B}$}}; \n\
    \\coordinate ({C}) at (4,0)  node at ({C}) [below] {{${C}$}}; \n\
    \\coordinate ({A1}) at (0,4)   node at ({A1}) [above] {{${A1}$}}; \n\
    \\coordinate ({B1}) at (2,3)   node at ({B1}) [above] {{${B1}$}}; \n\
    \\coordinate ({C1}) at (4,4)   node at ({C1}) [above] {{${C1}$}};\n\
    \\coordinate (H) at ($({B1})!0.4!({C1})$) node at (H) [right] {{$H$}};\n\
    \\draw [dashed] ({A})--({C}) ; \n\
    \\draw ({A})--({B})--({B1})--({A1})--({A}) ({A1})--(H); \n\
    \\draw ({B1})--({C1})--({C})--({B}) ({A1})--({C1})--({C}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có ${ten_AB}={AB}, {ten_BC}={BC}, {ten_AC}={AC}$."
		f" Tính khoảng cách giữa ${{{A}{A1}}}$ và ${{{B1}{C1}}}$(kết quả làm tròn đến hàng phần trăm).")	

		noi_dung_loigiai=(
			f"Kẻ ${A1}H\\bot {B1}{C1}$. Ta có: ${A}{A1}\\bot {A1}H$ nên $d({A}{A1},{B1}{C1})={A1}H$.\n\n"
			f"Xét tam giác ${{{A1}{B1}{C1}}}$ có $p=\\dfrac{{{AB}+{AC}+{BC}}}{{2}}={phan_so(p)}$.\n\n"
			f"$S_{{{A1}{B1}{C1}}}=\\sqrt{{{phan_so(p)}({phan_so(p)}-{AB})({phan_so(p)}-{AC})({phan_so(p)}-{BC})}}={{{latex(nsimplify(S))}}}$.\n\n"
			f"${A}H=\\dfrac{{2S_{{{A1}{B1}{C1}}}}}{{{B1}{C1}}}=\\dfrac{{2.{latex(nsimplify(S))}}}{{{BC}}}={{{latex(nsimplify(AH))}}}={dap_an}$.")
	
	BH=2*S/AC
	dap_an=f"{round_half_up(BH,2):.2f}".replace(".",",")	

	if chon==3:
		code_LG=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}}; \n\
    \\coordinate ({B}) at (2,-1) node at ({B}) [below] {{${B}$}}; \n\
    \\coordinate ({C}) at (4,0)  node at ({C}) [below] {{${C}$}}; \n\
    \\coordinate ({A1}) at (0,4)   node at ({A1}) [above] {{${A1}$}}; \n\
    \\coordinate ({B1}) at (2,3)   node at ({B1}) [above] {{${B1}$}}; \n\
    \\coordinate ({C1}) at (4,4)   node at ({C1}) [above] {{${C1}$}};\n\
    \\coordinate (H) at ($({A})!0.4!({C})$) node at (H) [above] {{$H$}};\n\
    \\draw [dashed] ({A})--({C}) ({B})--(H); \n\
    \\draw ({A})--({B})--({B1})--({A1})--({A}) ; \n\
    \\draw ({B1})--({C1})--({C})--({B}) ({A1})--({C1})--({C}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có ${ten_AB}={AB}, {ten_BC}={BC}, {ten_AC}={AC}$."
		f" Tính khoảng cách giữa ${{{B}{B1}}}$ và ${{{A}{C}}}$(kết quả làm tròn đến hàng phần trăm).")	

		noi_dung_loigiai=(
			f"Kẻ ${B}H\\bot {A}{C}$. Ta có: ${B}{B1}\\bot {B}H$ nên $d({B}{B1},{A}{C})={B}H$.\n\n"
			f"Xét tam giác ${{{A}{B}{C}}}$ có $p=\\dfrac{{{AB}+{AC}+{BC}}}{{2}}={phan_so(p)}$.\n\n"
			f"$S_{{{A}{B}{C}}}=\\sqrt{{{phan_so(p)}({phan_so(p)}-{AB})({phan_so(p)}-{AC})({phan_so(p)}-{BC})}}={{{latex(nsimplify(S))}}}$.\n\n"
			f"${B}H=\\dfrac{{2S_{{{A}{B}{C}}}}}{{{A}{C}}}=\\dfrac{{2.{latex(nsimplify(S))}}}{{{AC}}}={{{latex(nsimplify(BH))}}}={dap_an}$.")

	CH=2*S/AB
	dap_an=f"{round_half_up(CH,2):.2f}".replace(".",",")	

	if chon==4:
		code_LG=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}} \n\
    \\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}}; \n\
    \\coordinate ({B}) at (2,-1) node at ({B}) [below] {{${B}$}}; \n\
    \\coordinate ({C}) at (4,0)  node at ({C}) [below] {{${C}$}}; \n\
    \\coordinate ({A1}) at (0,4)   node at ({A1}) [above] {{${A1}$}}; \n\
    \\coordinate ({B1}) at (2,3)   node at ({B1}) [above] {{${B1}$}}; \n\
    \\coordinate ({C1}) at (4,4)   node at ({C1}) [above] {{${C1}$}};\n\
    \\coordinate (H) at ($({A})!0.4!({B})$) node at (H) [left] {{$H$}};\n\
    \\draw [dashed] ({A})--({C}) ({C})--(H); \n\
    \\draw ({A})--({B})--({B1})--({A1})--({A}) ; \n\
    \\draw ({B1})--({C1})--({C})--({B}) ({A1})--({C1})--({C}); \n\
\\end{{scriptsize}} \n\
\\end{{tikzpicture}} \n"
		noi_dung=thay_hinh_hoc(f"Cho hình lăng trụ đứng ${{{ten_lt}}}$ có ${ten_AB}={AB}, {ten_BC}={BC}, {ten_AC}={AC}$."
		f" Tính khoảng cách giữa ${{{C}{C1}}}$ và ${{{A}{B}}}$(kết quả làm tròn đến hàng phần trăm).")	

		noi_dung_loigiai=(
			f"Kẻ ${C}H\\bot {A}{B1}$. Ta có: ${C}{C1}\\bot {C}H$ nên $d({C}{C1},{A}{B})={C}H$.\n\n"
			f"Xét tam giác ${{{A}{B}{C}}}$ có $p=\\dfrac{{{AB}+{AC}+{BC}}}{{2}}={phan_so(p)}$.\n\n"
			f"$S_{{{A}{B}{C}}}=\\sqrt{{{phan_so(p)}({phan_so(p)}-{AB})({phan_so(p)}-{AC})({phan_so(p)}-{BC})}}={{{latex(nsimplify(S))}}}$.\n\n"
			f"${C}H=\\dfrac{{2S_{{{A}{B}{C}}}}}{{{A}{B}}}=\\dfrac{{2.{latex(nsimplify(S))}}}{{{AB}}}={{{latex(nsimplify(CH))}}}={dap_an}$.")
		
	
	code = my_module.moi_truong_anh_latex(code_LG)
	file_name = my_module.pdftoimage_timename(code)
		
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name}\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{\\begin{{center}}\n{code_LG}\n\\end{{center}} \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C8_B4_14]-SA-M3. H.chóp S.ABC, đáy tam giác đều. Tính d(A,(SBC))
def uvxy9_L11_C8_B4_14():
	A,B,C=random.sample(["A","B","C"],3)
	AB=sqrt(random.randint(1,9))
	SA=sqrt(random.randint(1,10))
	AM=AB*sqrt(3)/2
	AH=(SA*AM)/sqrt(SA**2+AM**2)
	code_hinh=f"\\begin{{tikzpicture}}\n\
\\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}};\n\
\\coordinate ({B}) at (1,-2) node at ({B}) [left] {{${B}$}};\n\
\\coordinate ({C}) at (4,0)   node at ({C}) [right] {{${C}$}};\n\
\\coordinate ({S}) at (0,4)   node at ({S}) [above] {{${S}$}};\n\
\\coordinate (M) at ($({B})!0.5!({C})$) node at (M) [right] {{$M$}};\n\
\\coordinate (H) at ($({S})!0.5!(M)$) node at (H) [right] {{$H$}};\n\
\\draw [dashed] ({A})--({C}) ({A})--(M) ({A})--(H); \n\
\\draw ({A})--({B}) ({B})--({C}) ({S})--({A}) ({S})--({B}) ({S})--({C}) ({S})--(M); \n\
\\end{{tikzpicture}}\n"	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	noi_dung = (
	f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều có cạnh bằng ${{{latex(AB)}}}$, $S{A}\\bot (ABC),S{A}={latex(SA)}$."
	f" Tính khoảng cách từ điểm ${{{A}}}$ đến mặt phẳng $(S{B}{C})$ (kết quả làm tròn đến hàng phần mười)."
	)
	dap_an=f"{round_half_up(AH,1):.1f}".replace(".",",")

	noi_dung_loigiai=(
	f"Gọi ${{M}}$ là trung điểm của ${{{B}{C}}}$. Ta có ${A}M={latex(AM)}$.\n\n"
	f"Ta có: ${B}{C}\\bot (S{A}M)$. Dựng ${A}H\\bot SM$. Suy ra ${A}H\\bot (S{B}{C})$.\n\n"
	f"$d({A},(S{B}{C}))={A}H=\\dfrac{{S{A}.{A}M}}{{\\sqrt{{S{A}^2+{A}M^2}}}}="
	f"\\dfrac{{{latex(SA)}.{latex(nsimplify(AM))} }}{{\\sqrt{{{latex(SA**2)}+{latex(AM**2)}}}}}$"
	f"$={{{latex(nsimplify(AH))}}}={dap_an}$."
	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name} {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \\begin{{center}}\n{code_hinh}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C8_B4_15]-SA-M3. H.chóp S.ABC, đáy t.giác vuông. Tính d(A,(SBC))
def uvxy9_L11_C8_B4_15():
	A,B,C=random.sample(["A","B","C"],3)
	AB=sqrt(random.randint(1,9))
	AC=sqrt(random.randint(1,9))
	SA=sqrt(random.randint(1,10))
	AM=(AB*AC)/sqrt(AB**2+AC**2)
	AH=(SA*AM)/sqrt(SA**2+AM**2)
	code_hinh=f"\\begin{{tikzpicture}}\n\
\\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}};\n\
\\coordinate ({B}) at (1,-2) node at ({B}) [left] {{${B}$}};\n\
\\coordinate ({C}) at (4,0)   node at ({C}) [right] {{${C}$}};\n\
\\coordinate ({S}) at (0,4)   node at ({S}) [above] {{${S}$}};\n\
\\coordinate (M) at ($({B})!0.5!({C})$) node at (M) [right] {{$M$}};\n\
\\coordinate (H) at ($({S})!0.5!(M)$) node at (H) [right] {{$H$}};\n\
\\draw [dashed] ({A})--({C}) ({A})--(M) ({A})--(H); \n\
\\draw ({A})--({B}) ({B})--({C}) ({S})--({A}) ({S})--({B}) ({S})--({C}) ({S})--(M); \n\
\\end{{tikzpicture}}\n"	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	noi_dung = (
	f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A}}}$, ${{{A}{B}={latex(AB)}, {A}{C}={latex(AC)}}}$, $S{A}\\bot (ABC),S{A}={latex(SA)}$."
	f" Tính khoảng cách từ điểm ${{{A}}}$ đến mặt phẳng $(S{B}{C})$ (kết quả làm tròn đến hàng phần mười)."
	)
	dap_an=f"{round_half_up(AH,1):.1f}".replace(".",",")

	noi_dung_loigiai=(
	f"Dựng ${A}M\\bot {B}{C}$. Ta có ${A}M=\\dfrac{{{A}{B}.{A}{C}}} {{\\sqrt{{{A}{B}^2+{A}{C}^2}}}}=$"
	f"$\\dfrac{{{latex(AB)}.{latex(AC)}}} {{\\sqrt{{{AB**2}+{AC**2}}}}}={{{latex(nsimplify(AM))}}}$.\n\n"
	f"Ta có: ${B}{C}\\bot (S{A}M)$. Dựng ${A}H\\bot SM$. Suy ra ${A}H\\bot (S{B}{C})$.\n\n"
	f"$d({A},(S{B}{C}))={A}H=\\dfrac{{S{A}.{A}M}}{{\\sqrt{{S{A}^2+{A}M^2}}}}="
	f"\\dfrac{{{latex(SA)}.{latex(nsimplify(AM))} }}{{\\sqrt{{{latex(SA**2)}+{latex(AM**2)}}}}}$"
	f"$={{{latex(nsimplify(AH))}}}={dap_an}$."
	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name} {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \\begin{{center}}\n{code_hinh}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C8_B4_16]-SA-M3. H.chóp S.ABC, đáy t.giác vuông cân. Tính d(A,(SBC))
def uvxy9_L11_C8_B4_16():
	A,B,C=random.sample(["A","B","C"],3)
	AB=sqrt(random.randint(1,9))
	AC=AB
	BC=sqrt(AB**2+AB**2)
	SA=sqrt(random.randint(1,10))
	AM=(AB*AC)/sqrt(AB**2+AC**2)
	AH=(SA*AM)/sqrt(SA**2+AM**2)
	code_hinh=f"\\begin{{tikzpicture}}\n\
\\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}};\n\
\\coordinate ({B}) at (1,-2) node at ({B}) [left] {{${B}$}};\n\
\\coordinate ({C}) at (4,0)   node at ({C}) [right] {{${C}$}};\n\
\\coordinate ({S}) at (0,4)   node at ({S}) [above] {{${S}$}};\n\
\\coordinate (M) at ($({B})!0.5!({C})$) node at (M) [right] {{$M$}};\n\
\\coordinate (H) at ($({S})!0.5!(M)$) node at (H) [right] {{$H$}};\n\
\\draw [dashed] ({A})--({C}) ({A})--(M) ({A})--(H); \n\
\\draw ({A})--({B}) ({B})--({C}) ({S})--({A}) ({S})--({B}) ({S})--({C}) ({S})--(M); \n\
\\end{{tikzpicture}}\n"	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	noi_dung = (
	f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông cân tại ${{{A}}}$, ${{{B}{C}={latex(BC)}}}$, $S{A}\\bot (ABC),S{A}={latex(SA)}$."
	f" Tính khoảng cách từ điểm ${{{A}}}$ đến mặt phẳng $(S{B}{C})$ (kết quả làm tròn đến hàng phần mười)."
	)
	dap_an=f"{round_half_up(AH,1):.1f}".replace(".",",")

	noi_dung_loigiai=(
	f"Ta có: ${A}{B}^2+{A}{C}^2={B}{C}^2\\Rightarrow 2{A}{B}^2={B}{C}^2 \\Rightarrow {A}{B}={A}{C}=\\dfrac{{{B}{C}}}{{\\sqrt{{2}}}}={latex(AB)}$.\n\n"
	f"Dựng ${A}M\\bot {B}{C}$. Ta có ${A}M=\\dfrac{{{A}{B}.{A}{C}}} {{\\sqrt{{{A}{B}^2+{A}{C}^2}}}}=$"
	f"$\\dfrac{{{latex(AB)}.{latex(AC)}}} {{\\sqrt{{{AB**2}+{AC**2}}}}}={{{latex(nsimplify(AM))}}}$.\n\n"
	f"Ta có: ${B}{C}\\bot (S{A}M)$. Dựng ${A}H\\bot SM$. Suy ra ${A}H\\bot (S{B}{C})$.\n\n"
	f"$d({A},(S{B}{C}))={A}H=\\dfrac{{S{A}.{A}M}}{{\\sqrt{{S{A}^2+{A}M^2}}}}="
	f"\\dfrac{{{latex(SA)}.{latex(nsimplify(AM))} }}{{\\sqrt{{{latex(SA**2)}+{latex(AM**2)}}}}}$"
	f"$={{{latex(nsimplify(AH))}}}={dap_an}$."
	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name} {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \\begin{{center}}\n{code_hinh}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C8_B4_17]-SA-M3. H.chóp S.ABC, đáy tam giác đều, trọng tâm G. Tính d(G,(SBC))
def uvxy9_L11_C8_B4_17():
	A,B,C=random.sample(["A","B","C"],3)
	AB=sqrt(random.randint(1,9))
	SA=sqrt(random.randint(1,10))
	AM=AB*sqrt(3)/2
	AH=(SA*AM)/sqrt(SA**2+AM**2)
	d_G=1/3*AH
	code_hinh=f"\\begin{{tikzpicture}}\n\
\\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}};\n\
\\coordinate ({B}) at (1,-2) node at ({B}) [left] {{${B}$}};\n\
\\coordinate ({C}) at (4,0)   node at ({C}) [right] {{${C}$}};\n\
\\coordinate ({S}) at (0,4)   node at ({S}) [above] {{${S}$}};\n\
\\coordinate (M) at ($({B})!0.5!({C})$) node at (M) [right] {{$M$}};\n\
\\coordinate (H) at ($({S})!0.5!(M)$) node at (H) [right] {{$H$}};\n\
\\coordinate (G) at ($({A})!0.6!(M)$) node at (G) [below] {{$G$}};\n\
\\draw [dashed] ({A})--({C}) ({A})--(M) ({A})--(H); \n\
\\draw ({A})--({B}) ({B})--({C}) ({S})--({A}) ({S})--({B}) ({S})--({C}) ({S})--(M); \n\
\\end{{tikzpicture}}\n"	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	noi_dung = (
	f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều có cạnh bằng ${{{latex(AB)}}}$, $S{A}\\bot (ABC),S{A}={latex(SA)}$."
	f" Gọi ${{G}}$ là trọng tâm của tam giác ${{ABC}}$."
	f" Tính khoảng cách từ điểm ${{G}}$ đến mặt phẳng $(S{B}{C})$ (kết quả làm tròn đến hàng phần mười)."
	)
	dap_an=f"{round_half_up(d_G,1):.1f}".replace(".",",")

	noi_dung_loigiai=(
	f"Gọi ${{M}}$ là trung điểm của ${{{B}{C}}}$. Ta có ${A}M={latex(AM)}$.\n\n"
	f"Ta có: ${B}{C}\\bot (S{A}M)$. Dựng ${A}H\\bot SM$. Suy ra ${A}H\\bot (S{B}{C})$.\n\n"
	f"$d({A},(S{B}{C}))={A}H=\\dfrac{{S{A}.{A}M}}{{\\sqrt{{S{A}^2+{A}M^2}}}}="
	f"\\dfrac{{{latex(SA)}.{latex(nsimplify(AM))} }}{{\\sqrt{{{latex(SA**2)}+{latex(AM**2)}}}}}$"
	f"$={{{latex(nsimplify(AH))}}}$.\n\n"
	f"$\\dfrac{{d(G,(S{B}{C}))}}{{d({A},(S{B}{C}))}}=\\dfrac{{MG}}{{M{A}}}=\\dfrac{{1}}{{3}}$.\n\n"
	f"Suy ra: $d(G,(S{B}{C}))=\\dfrac{{1}}{{3}}d({A},(S{B}{C}))=\\dfrac{{1}}{{3}}{{{latex(nsimplify(AH))}}}={latex(nsimplify(d_G))}={dap_an}$."
	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name} {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \\begin{{center}}\n{code_hinh}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#BÀI 5 - GÓC GIỮA ĐƯỜNG THẲNG VÀ MẶT PHẲNG

#[D11_C8_B5_01]-M1. S.ABCD: ABCD h.vuông. Xác định góc giữa đường thẳng và mặt phẳng.
def uvxy9_L11_C8_B5_01(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng $(ABCD)$ là"
		kq= f"$\\widehat{{S{B1}{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{D1}}}$"
		kq3= f"$\\widehat{{S{C1}{B1}}}$"
		kq4= random.choice([f"$\\widehat{{S{A1}{B1}}}$", f"$\\widehat{{S{D1}{B1}}}$"])
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{B1}}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{B1}}}$.\n\n"\
		f" Do đó $S{{{B1}}}$ có hình chiếu trên ${{(ABCD)}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(ABCD)\\right)= \\left(S{B1}, {A1}{B1}\\right)=\\widehat{{S{B1}{A1}}}$."	

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng $(ABCD)$ là"
		kq= f"$\\widehat{{S{C1}{A1}}}$"
		kq2= f"$\\widehat{{S{C1}{D1}}}$"
		kq3= f"$\\widehat{{S{C1}{B1}}}$"
		kq4= random.choice([f"$\\widehat{{S{A1}{C1}}}$", f"$\\widehat{{S{B1}{C1}}}$"])
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{C1}}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{C1}}}$.\n\n"\
		f" Do đó $S{{{C1}}}$ có hình chiếu trên ${{(ABCD)}}$ là ${{{A1}{C1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(ABCD)\\right)= \\left(S{C1}, {A1}{C1}\\right)=\\widehat{{S{C1}{A1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{D1}}}$ và mặt phẳng $(ABCD)$ là"
		kq= f"$\\widehat{{S{D1}{A1}}}$"
		kq2= f"$\\widehat{{S{D1}{C1}}}$"
		kq3= f"$\\widehat{{S{D1}{B1}}}$"
		kq4= random.choice([f"$\\widehat{{S{A1}{D1}}}$", f"$\\widehat{{S{C1}{D1}}}$"])
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{D1}}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{D1}}}$.\n\n"\
		f" Do đó $S{{{D1}}}$ có hình chiếu trên ${{(ABCD)}}$ là ${{{A1}{D1}}}$.\n\n"\
		f"Suy ra $\\left(S{D1},(ABCD)\\right)= \\left(S{D1}, {A1}{D1}\\right)=\\widehat{{S{D1}{A1}}}$."

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B5_02]-M2. S.ABCD: ABCD h.vuông. Xác định góc giữa đường thẳng và mặt phẳng.
def uvxy9_L11_C8_B5_02(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,6)	
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{B1}S{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{A1}}}$"
		kq3= f"$\\widehat{{S{B1}{D1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{D1}}}$", f"$\\widehat{{{D1}{B1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: ${B1}{A1}\\bot {A1}{D1},{B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó $S{{{B1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{S{A1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(S{A1}{D1})\\right)= \\left(S{B1}, S{A1}\\right)=\\widehat{{{B1}S{A1}}}$."
	
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{C1}S{D1}}}$"
		kq2= f"$\\widehat{{S{C1}{A1}}}$"
		kq3= f"$\\widehat{{S{C1}{D1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}{A1}{D1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó $S{{{C1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{S{D1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(S{A1}{D1})\\right)= \\left(S{C1}, S{D1}\\right)=\\widehat{{{C1}S{D1}}}$."
	
	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{B1}}})$ là"
		kq= f"$\\widehat{{{C1}S{B1}}}$"
		kq2= f"$\\widehat{{S{C1}{A1}}}$"
		kq3= f"$\\widehat{{S{C1}{B1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}{A1}{B1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{B1}\\bot {A1}{B1},{C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$.\n\n"\
		f"Do đó $S{{{C1}}}$ có hình chiếu trên ${{(S{A1}{B1})}}$ là ${{S{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(S{A1}{B1})\\right)= \\left(S{C1}, S{B1}\\right)=\\widehat{{{C1}S{B1}}}$."

	
	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng ${{{A1}{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{B1}}})$ là"
		kq= f"$\\widehat{{{C1}{A1}{B1}}}$"
		kq2= f"$\\widehat{{S{C1}{A1}}}$"
		kq3= f"$\\widehat{{S{C1}{B1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}{B1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{B1}\\bot {A1}{B1},{C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$.\n\n"\
		f"Do đó ${{{A1}{C1}}}$ có hình chiếu trên ${{(S{A1}{B1})}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left({A1}{C1},(S{A1}{B1})\\right)= \\left({A1}{C1}, {A1}{B1}\\right)=\\widehat{{{C1}{A1}{B1}}}$."

	
	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng ${{{A1}{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{C1}{A1}{D1}}}$"
		kq2= f"$\\widehat{{S{C1}{D1}}}$"
		kq3= f"$\\widehat{{S{C1}{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}S{D1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó ${{{A1}{C1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{{A1}{D1}}}$.\n\n"\
		f"Suy ra $\\left({A1}{C1},(S{A1}{D1})\\right)= \\left({A1}{C1}, {A1}{D1}\\right)=\\widehat{{{C1}{A1}{D1}}}$."

	if chon==6:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng ${{{B1}{D1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{B1}{D1}{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{D1}}}$"
		kq3= f"$\\widehat{{S{B1}{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{A1}}}$", f"$\\widehat{{{B1}S{D1}}}$"])
		noi_dung_loigiai=f"Ta có: ${B1}{A1}\\bot {A1}{D1},{B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó ${{{B1}{D1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{{A1}{D1}}}$.\n\n"\
		f"Suy ra $\\left({B1}{D1},(S{A1}{D1})\\right)= \\left({B1}{D1}, {A1}{D1}\\right)=\\widehat{{{B1}{D1}{A1}}}$."

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B5_03]-M2. S.ABCD: ABCD h.chữ nhật. Xác định góc giữa đường thẳng và mặt phẳng.
def uvxy9_L11_C8_B5_03(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,6)
	
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{B1}S{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{A1}}}$"
		kq3= f"$\\widehat{{S{B1}{D1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{D1}}}$", f"$\\widehat{{{D1}{B1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: ${B1}{A1}\\bot {A1}{D1},{B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó $S{{{B1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{S{A1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(S{A1}{D1})\\right)= \\left(S{B1}, S{A1}\\right)=\\widehat{{{B1}S{A1}}}$."
	
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{C1}S{D1}}}$"
		kq2= f"$\\widehat{{S{C1}{A1}}}$"
		kq3= f"$\\widehat{{S{C1}{D1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}{A1}{D1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó $S{{{C1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{S{D1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(S{A1}{D1})\\right)= \\left(S{C1}, S{D1}\\right)=\\widehat{{{C1}S{D1}}}$."
	
	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{B1}}})$ là"
		kq= f"$\\widehat{{{C1}S{B1}}}$"
		kq2= f"$\\widehat{{S{C1}{A1}}}$"
		kq3= f"$\\widehat{{S{C1}{B1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}{A1}{B1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{B1}\\bot {A1}{B1},{C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$.\n\n"\
		f"Do đó $S{{{C1}}}$ có hình chiếu trên ${{(S{A1}{B1})}}$ là ${{S{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(S{A1}{B1})\\right)= \\left(S{C1}, S{B1}\\right)=\\widehat{{{C1}S{B1}}}$."

	
	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng ${{{A1}{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{B1}}})$ là"
		kq= f"$\\widehat{{{C1}{A1}{B1}}}$"
		kq2= f"$\\widehat{{S{C1}{A1}}}$"
		kq3= f"$\\widehat{{S{C1}{B1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}{B1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{B1}\\bot {A1}{B1},{C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$.\n\n"\
		f"Do đó ${{{A1}{C1}}}$ có hình chiếu trên ${{(S{A1}{B1})}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left({A1}{C1},(S{A1}{B1})\\right)= \\left({A1}{C1}, {A1}{B1}\\right)=\\widehat{{{C1}{A1}{B1}}}$."

	
	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng ${{{A1}{C1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{C1}{A1}{D1}}}$"
		kq2= f"$\\widehat{{S{C1}{D1}}}$"
		kq3= f"$\\widehat{{S{C1}{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{C1}S{D1}}}$"])
		noi_dung_loigiai=f"Ta có: ${C1}{D1}\\bot {A1}{D1},{C1}{D1}\\bot S{A1} \\Rightarrow {C1}{D1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó ${{{A1}{C1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{{A1}{D1}}}$.\n\n"\
		f"Suy ra $\\left({A1}{C1},(S{A1}{D1})\\right)= \\left({A1}{C1}, {A1}{D1}\\right)=\\widehat{{{C1}{A1}{D1}}}$."

	if chon==6:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$. Góc giữa đường thẳng ${{{B1}{D1}}}$ và mặt phẳng $(S{{{A1}}}{{{D1}}})$ là"
		kq= f"$\\widehat{{{B1}{D1}{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{D1}}}$"
		kq3= f"$\\widehat{{S{B1}{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{A1}}}$", f"$\\widehat{{{B1}S{D1}}}$"])
		noi_dung_loigiai=f"Ta có: ${B1}{A1}\\bot {A1}{D1},{B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{D1})$.\n\n"\
		f"Do đó ${{{B1}{D1}}}$ có hình chiếu trên ${{(S{A1}{D1})}}$ là ${{{A1}{D1}}}$.\n\n"\
		f"Suy ra $\\left({B1}{D1},(S{A1}{D1})\\right)= \\left({B1}{D1}, {A1}{D1}\\right)=\\widehat{{{B1}{D1}{A1}}}$."

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B5_04]-M1. S.ABC: ABC tam giác vuông. Xác định góc giữa đường thẳng và mặt phẳng.
def uvxy9_L11_C8_B5_04(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])
	chon=random.randint(1,6)
	
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng ${{(ABC)}}$ là"

		kq= f"$\\widehat{{S{B1}{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{C1}}}$"
		kq3= f"$\\widehat{{{B1}S{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: $S{A1} \\bot (ABC)$."\
		f" Do đó ${{S{B1}}}$ có hình chiếu trên ${{(ABC)}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(ABC)\\right)= \\left(S{B1}, {A1}{B1}\\right)=\\widehat{{S{B1}{A1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{B1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng ${{(ABC)}}$ là"

		kq= f"$\\widehat{{S{B1}{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{C1}}}$"
		kq3= f"$\\widehat{{{B1}S{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: $S{A1} \\bot (ABC)$."\
		f" Do đó ${{S{B1}}}$ có hình chiếu trên ${{(ABC)}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(ABC)\\right)= \\left(S{B1}, {A1}{B1}\\right)=\\widehat{{S{B1}{A1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{C1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng ${{(ABC)}}$ là"

		kq= f"$\\widehat{{S{B1}{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{C1}}}$"
		kq3= f"$\\widehat{{{B1}S{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: $S{A1} \\bot (ABC)$."\
		f" Do đó ${{S{B1}}}$ có hình chiếu trên ${{(ABC)}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(ABC)\\right)= \\left(S{B1}, {A1}{B1}\\right)=\\widehat{{S{B1}{A1}}}$."
	
	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng ${{(ABC)}}$ là"

		kq= f"$\\widehat{{S{C1}{A1}}}$"
		kq2= f"$\\widehat{{S{C1}{B1}}}$"
		kq3= f"$\\widehat{{{C1}S{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: $S{A1} \\bot (ABC)$."\
		f" Do đó ${{S{C1}}}$ có hình chiếu trên ${{(ABC)}}$ là ${{{A1}{C1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(ABC)\\right)= \\left(S{C1}, {A1}{C1}\\right)=\\widehat{{S{C1}{A1}}}$."

	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{B1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng ${{(ABC)}}$ là"

		kq= f"$\\widehat{{S{C1}{A1}}}$"
		kq2= f"$\\widehat{{S{C1}{B1}}}$"
		kq3= f"$\\widehat{{{C1}S{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: $S{A1} \\bot (ABC)$."\
		f" Do đó ${{S{C1}}}$ có hình chiếu trên ${{(ABC)}}$ là ${{{A1}{C1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(ABC)\\right)= \\left(S{C1}, {A1}{C1}\\right)=\\widehat{{S{C1}{A1}}}$."

	if chon==6:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{C1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng ${{(ABC)}}$ là"

		kq= f"$\\widehat{{S{C1}{A1}}}$"
		kq2= f"$\\widehat{{S{C1}{B1}}}$"
		kq3= f"$\\widehat{{{C1}S{A1}}}$"
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])
		noi_dung_loigiai=f"Ta có: $S{A1} \\bot (ABC)$."\
		f" Do đó ${{S{C1}}}$ có hình chiếu trên ${{(ABC)}}$ là ${{{A1}{C1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(ABC)\\right)= \\left(S{C1}, {A1}{C1}\\right)=\\widehat{{S{C1}{A1}}}$."


    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B5_05]-M2. S.ABC: ABC tam giác vuông. Xác định góc giữa đường thẳng và mặt bên.
def uvxy9_L11_C8_B5_05(): 	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]
	i=random.randint(0,2)
	A1, B1, C1 = A1[i], B1[i], C1[i]
	M1=random.choice(["M", "I", "P", "E"])
	N1=random.choice(["N", "H", "Q", "F"])
	chon=random.randint(1,6)	
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng ${{(S{A1}{C1})}}$ là"

		kq= f"$\\widehat{{{B1}S{A1}}}$"
		kq2= f"$\\widehat{{S{B1}{C1}}}$"
		kq3= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])

		noi_dung_loigiai=f"Ta có: ${B1}{A1}\\bot {A1}{C1}, {B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{C1})$."\
		f" Do đó ${{S{B1}}}$ có hình chiếu trên ${{(S{A1}{C1})}}$ là ${{S{A1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(S{A1}{C1})\\right)= \\left(S{B1}, S{A1}\\right)=\\widehat{{{B1}S{A1}}}$."

	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{C1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng ${{(S{A1}{C1})}}$ là"

		kq= f"$\\widehat{{{B1}S{C1}}}$"
		kq2= f"$\\widehat{{S{B1}{C1}}}$"
		kq3= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{{B1}S{A1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])

		noi_dung_loigiai=f"Ta có: ${B1}{C1}\\bot {A1}{C1}, {B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{C1})$."\
		f" Do đó ${{S{B1}}}$ có hình chiếu trên ${{(S{A1}{C1})}}$ là ${{S{C1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(S{A1}{C1})\\right)= \\left(S{B1}, S{C1}\\right)=\\widehat{{{B1}S{C1}}}$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{A1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng ${{(S{A1}{B1})}}$ là"

		kq= f"$\\widehat{{{C1}S{A1}}}$"
		kq2= f"$\\widehat{{S{C1}{B1}}}$"
		kq3= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{{B1}S{C1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])

		noi_dung_loigiai=f"Ta có: ${B1}{A1}\\bot {A1}{C1}, {B1}{A1}\\bot S{A1} \\Rightarrow {B1}{A1} \\bot (S{A1}{C1})$."\
		f" Do đó ${{S{C1}}}$ có hình chiếu trên ${{(S{A1}{C1})}}$ là ${{S{A1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(S{A1}{C1})\\right)= \\left(S{C1}, S{A1}\\right)=\\widehat{{{C1}S{A1}}}$."
	
	if chon==4:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{B1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng ${{(S{A1}{B1})}}$ là"

		kq= f"$\\widehat{{{C1}S{B1}}}$"
		kq2= f"$\\widehat{{S{C1}{B1}}}$"
		kq3= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{{C1}S{A1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])

		noi_dung_loigiai=f"Ta có: ${C1}{B1}\\bot {A1}{B1}, {C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$."\
		f" Do đó ${{S{C1}}}$ có hình chiếu trên ${{(S{A1}{B1})}}$ là ${{S{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(S{A1}{B1})\\right)= \\left(S{C1}, S{B1}\\right)=\\widehat{{{C1}S{B1}}}$."
	
	if chon==5:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{B1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng ${{{A1}{C1}}}$ và mặt phẳng ${{(S{A1}{B1})}}$ là"

		kq= f"$\\widehat{{{C1}{A1}{B1}}}$"
		kq2= f"$\\widehat{{S{C1}{B1}}}$"
		kq3= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{{C1}S{B1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])

		noi_dung_loigiai=f"Ta có: ${C1}{B1}\\bot {A1}{B1}, {C1}{B1}\\bot S{A1} \\Rightarrow {C1}{B1} \\bot (S{A1}{B1})$."\
		f" Do đó ${{{A1}{C1}}}$ có hình chiếu trên ${{(S{A1}{B1})}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left({A1}{C1},(S{A1}{B1})\\right)= \\left({A1}{C1}, {A1}{B1}\\right)=\\widehat{{{C1}{A1}{B1}}}$."

	if chon==6:
		noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông tại ${{{C1}}}$, $S{A1}\\bot (ABC)$."\
		f" Góc giữa đường thẳng ${{{A1}{B1}}}$ và mặt phẳng ${{(S{A1}{C1})}}$ là"

		kq= f"$\\widehat{{{B1}{A1}{C1}}}$"
		kq2=  random.choice([f"$\\widehat{{S{B1}{C1}}}$", f"$\\widehat{{{B1}S{C1}}}$"])
		kq3= random.choice([f"$\\widehat{{S{B1}{A1}}}$", f"$\\widehat{{S{C1}{A1}}}$"])
		kq4= random.choice([f"$\\widehat{{{B1}S{A1}}}$", f"$\\widehat{{{B1}{C1}{A1}}}$"])

		noi_dung_loigiai=f"Ta có: ${B1}{C1}\\bot {A1}{C1}, {B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}{C1})$."\
		f" Do đó ${{{A1}{B1}}}$ có hình chiếu trên ${{(S{A1}{C1})}}$ là ${{{A1}{C1}}}$.\n\n"\
		f"Suy ra $\\left({A1}{B1},(S{A1}{C1})\\right)= \\left({A1}{B1}, {A1}{C1}\\right)=\\widehat{{{B1}{A1}{C1}}}$."
	

    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C8_B5_06]-M2. S.ABCD, đáy h.c.n. Tính số đo góc phẳng nhị diện tạo bởi mặt nghiêng và đáy.
def uvxy9_L11_C8_B5_06(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	canh_SA1 =random.choice([sqrt(2),sqrt(3),sqrt(5),random.randint(3,8)])
	canh_A1B1 = random.randint(1,7)	
	canh_A1D1 =canh_A1B1 + random.randint(1,5)	
	canh_SD1=sqrt(canh_SA1**2+canh_A1D1**2)
	chon=random.randint(1,3)	
	if chon == 1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$,"\
		f" ${A1}{B1}={latex(canh_A1B1*a)}, {A1}{D1}={latex(canh_A1D1*a)}, S{A1}={latex(canh_SA1*a)}$."\
		f" Tính số đo góc phẳng nhị diện ${{[{A1},{B1}{C1},{S}]}}$."		
		
		t=canh_SA1/canh_A1B1			
		goc=round(atan(t).evalf() * 180 / pi,2)
		if "." in str(t):
			t=latex(my_module.hien_phan_so(t))
		else:
			t=latex(t)

		kq=return_number_vn(goc)
		kq2=return_number_vn(goc+(random.randint(10,90))/10)
		kq3=return_number_vn(goc+(random.randint(90,130))/10)
		kq4=return_number_vn(goc+(random.randint(140,200))/10)

		noi_dung_loigiai=f"Ta có: ${A1}{B1} \\bot {B1}{C1}, {B1}{C1} \\bot S{A1} \\Rightarrow {B1}{C1} \\bot S{B1}$."\
		f" Do đó ${{[{A1},{B1}{C1},{S}]}} =\\widehat{{S{B1}{A1}}}$.\n\n"\
		f"$\\displaystyle \\tan \\widehat{{S{B1}{A1}}}=\\dfrac{{S{A1}}} {{{A1}{B1}}}= \\dfrac{{{latex(canh_SA1*a)}}} {{{latex(canh_A1B1*a)}}}={t}$.\n"\
		f"Suy ra $\\widehat{{S{B1}{A1}}} = {kq}^\\circ$."
	
	
	if chon==2:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$,"\
			f" ${A1}{B1}={latex(canh_A1B1*a)}, S{D1}={latex(canh_SD1*a)}, S{A1}={latex(canh_SA1*a)}$."\
		f" Tính số đo góc phẳng nhị diện ${{[{A1},{C1}{D1},{S}]}}$."	
		t=canh_SA1/canh_SD1			
		goc=round(asin(t).evalf() * 180 / pi,2)
		if "." in str(t):
			t=latex(my_module.hien_phan_so(t))
		else:
			t=latex(t)
		kq=return_number_vn(goc)
		kq2=return_number_vn(goc+(random.randint(10,90))/10)
		kq3=return_number_vn(goc+(random.randint(90,130))/10)
		kq4=return_number_vn(goc+(random.randint(140,200))/10)

		noi_dung_loigiai=f"Ta có: ${A1}{D1} \\bot {C1}{D1}, {C1}{D1} \\bot S{A1} \\Rightarrow {C1}{D1} \\bot S{D1}$."\
		f" Do đó ${{[{A1},{C1}{D1},{S}]}} =\\widehat{{S{D1}{A1}}}$.\n\n"\
		f"$\\displaystyle \\sin \\widehat{{S{D1}{A1}}}=\\dfrac{{S{A1}}} {{S{D1}}}= \\dfrac{{{latex(canh_SA1*a)}}} {{{latex(canh_SD1*a)}}}={t}$.\n"\
		f"Suy ra $\\widehat{{S{D1}{A1}}} = {kq}^\\circ$."

	if chon==3:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$,"\
			f" ${A1}{B1}={latex(canh_A1B1*a)}, {A1}{D1}={latex(canh_A1D1*a)}, S{A1}={latex(canh_SA1*a)}$."\
		f" Tính số đo góc phẳng nhị diện ${{[{A1},{B1}{D1},{S}]}}$."
		canh_AH=(canh_A1B1*canh_A1D1)/sqrt(canh_A1B1**2+canh_A1D1**2)
		t=canh_SA1/canh_AH	
		goc=round(atan(t).evalf() * 180 / pi,2)
		if "." in str(t):
			t=latex(my_module.hien_phan_so(t))
		else:
			t=latex(t)

		kq=return_number_vn(goc)
		kq2=return_number_vn(goc+(random.randint(10,90))/10)
		kq3=return_number_vn(goc+(random.randint(90,130))/10)
		kq4=return_number_vn(goc+(random.randint(140,200))/10)

		noi_dung_loigiai=f"Dựng ${A1}H \\bot {B1}{D1},{B1}{D1} \\bot S{A1} \\Rightarrow SH \\bot {B1}{D1}$."\
		f" Do đó ${{[{A1},{B1}{D1},{S}]}} =\\widehat{{SH{A1}}}$.\n\n"\
		f"$\\displaystyle AH= \\dfrac{{{A1}{B1}.{A1}{D1}}} {{\\sqrt{{{A1}{B1}^2 + {A1}{D1}^2}}}}= {latex((canh_A1B1*canh_A1D1)/sqrt(canh_A1B1**2+canh_A1D1**2))}a$.\n\n"\
		f"$\\displaystyle \\tan \\widehat{{SH{A1}}}=\\dfrac{{S{A1}}} {{{A1}H}}= \\dfrac{{{latex(canh_SA1*a)}}} {{{latex(canh_AH*a)}}}={t}$.\n"\
		f"Suy ra $\\widehat{{SH{A1}}} = {kq}^\\circ$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}^\\circ}}$"
	pa_B= f"${{{kq2}^\\circ}}$"
	pa_C= f"${{{kq3}^\\circ}}$"
	pa_D= f"${{{kq4}^\\circ}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C8_B5_07]-M3. S.ABCD, đáy h.c.n. Tính số đo góc phẳng nhị diện tạo bởi mặt nghiêng và đáy.
def uvxy9_L11_C8_B5_07(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	canh_SA1 =random.choice([sqrt(2),sqrt(3),sqrt(5),random.randint(3,8)])
	canh_A1B1 = random.randint(1,7)	
	canh_A1D1 =canh_A1B1 + random.randint(1,5)	
	canh_SD1=sqrt(canh_SA1**2+canh_A1D1**2)

	chon=random.randint(1,3)
	chon=1
	if chon==1:
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình chữ nhật, $S{A1}\\bot (ABCD)$,"\
			f" ${A1}{B1}={latex(canh_A1B1*a)}, {A1}{D1}={latex(canh_A1D1*a)}, S{A1}={latex(canh_SA1*a)}$."\
		f" Tính số đo góc phẳng nhị diện ${{[{A1},{B1}{D1},{S}]}}$."
		canh_AH=(canh_A1B1*canh_A1D1)/sqrt(canh_A1B1**2+canh_A1D1**2)
		t=canh_SA1/canh_AH	
		goc=round(atan(t).evalf() * 180 / pi,2)

		kq=return_number_vn(goc)
		kq2=return_number_vn(goc+(random.randint(10,90))/10)
		kq3=return_number_vn(goc+(random.randint(90,130))/10)
		kq4=return_number_vn(goc+(random.randint(140,200))/10)

		noi_dung_loigiai=f"Dựng ${A1}H \\bot {B1}{D1},{B1}{D1} \\bot S{A1} \\Rightarrow SH \\bot {B1}{D1}$."\
		f" Do đó ${{[{A1},{B1}{D1},{S}]}} =\\widehat{{SH{A1}}}$.\n\n"\
		f"$\\displaystyle AH= \\dfrac{{{A1}{B1}.{A1}{D1}}} {{\\sqrt{{{A1}{B1}^2 + {A1}{D1}^2}}}}= {latex((canh_A1B1*canh_A1D1)/sqrt(canh_A1B1**2+canh_A1D1**2))}a$.\n\n"\
		f"$\\displaystyle \\tan \\widehat{{SH{A1}}}=\\dfrac{{S{A1}}} {{{A1}H}}= \\dfrac{{{latex(canh_SA1*a)}}} {{{latex(canh_AH*a)}}}={latex(t)}$.\n"\
		f"Suy ra $\\widehat{{SH{A1}}} = {kq}^\\circ$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}^\\circ}}$"
	pa_B= f"${{{kq2}^\\circ}}$"
	pa_C= f"${{{kq3}^\\circ}}$"
	pa_D= f"${{{kq4}^\\circ}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B5_08]-M2. S.ABCD: ABCD h.vuông. Xác định góc giữa đường thẳng và mặt phẳng.
def uvxy9_L11_C8_B5_08(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	chon=random.randint(1,3)
	
	if chon==1:
		AB= random.choice([sqrt(i) for i in range(1,100)])
		SA= random.choice([sqrt(i) for i in range(1,100)])
		t=SA/AB
		goc=round(atan(t).evalf() * 180 / pi,2)
		if "." in str(t):
			t=latex(my_module.hien_phan_so(t))
		else:
			t=latex(t)
		kq=return_number_vn(goc)
		kq2=return_number_vn(goc+(random.randint(10,90))/10)
		kq3=return_number_vn(goc+(random.randint(90,130))/10)
		kq4=return_number_vn(goc+(random.randint(140,200))/10)

		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông cạnh bằng ${latex(AB)}a$ , $S{A1}\\bot (ABCD), S{A1}={latex(SA)}a$.\n\n"\
		f" Số đo góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng $(ABCD)$ là"

		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{B1}}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{B1}}}$.\n\n"\
		f" Do đó $S{{{B1}}}$ có hình chiếu trên ${{(ABCD)}}$ là ${{{A1}{B1}}}$.\n\n"\
		f"Suy ra $\\left(S{B1},(ABCD)\\right)= \\left(S{B1}, {A1}{B1}\\right)=\\widehat{{S{B1}{A1}}}$.\n\n"\
		f"$\\tan \\widehat{{S{B1}{A1}}}=\\dfrac{{S{A1}}} {{{A1}{B1}}}= \\dfrac{{{latex(SA*a)}}} {{{latex(AB*a)}}}={t}$.\n\n"\
			f"Suy ra $\\widehat{{S{B1}{A1}}} = {kq}^\\circ$."
	
	if chon==2:
		AB= random.choice([sqrt(i) for i in range(1,100)])
		SA= random.choice([sqrt(i) for i in range(1,100)])
		AC=AB*sqrt(2)
		t=SA/AC
		goc=round(atan(t).evalf() * 180 / pi,2)
		if "." in str(t):
			t=latex(my_module.hien_phan_so(t))
		else:
			t=latex(t)
		kq=return_number_vn(goc)
		kq2=return_number_vn(goc+(random.randint(10,90))/10)
		kq3=return_number_vn(goc+(random.randint(90,130))/10)
		kq4=return_number_vn(goc+(random.randint(140,200))/10)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông cạnh bằng ${latex(AB)}a$ , $S{A1}\\bot (ABCD), S{A1}={latex(SA)}a$.\n\n"\
		f" Số đo góc giữa đường thẳng $S{{{C1}}}$ và mặt phẳng $(ABCD)$ là"
		
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{C1}}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{C1}}}$.\n\n"\
		f" Do đó $S{{{C1}}}$ có hình chiếu trên ${{(ABCD)}}$ là ${{{A1}{C1}}}$.\n\n"\
		f"Suy ra $\\left(S{C1},(ABCD)\\right)= \\left(S{C1}, {A1}{C1}\\right)=\\widehat{{S{C1}{A1}}}$.\n\n"\
		f"${A1}{C1}={A1}{B1}\\sqrt{{2}}a={latex(AC*a)}$.\n\n"\
		f"$\\tan \\widehat{{S{C1}{A1}}}=\\dfrac{{S{C1}}} {{{A1}{C1}}}= \\dfrac{{{latex(SA*a)}}} {{{latex(AC*a)}}}={t}$.\n\n"\
			f"Suy ra $\\widehat{{S{C1}{A1}}} = {kq}^\\circ$."
	
	if chon==3:
		AB= random.choice([sqrt(i) for i in range(1,100)])
		SA= random.choice([sqrt(i) for i in range(1,100)])
		t=SA/AB
		goc=round(atan(t).evalf() * 180 / pi,2)
		if "." in str(t):
			t=latex(my_module.hien_phan_so(t))
		else:
			t=latex(t)
		kq=return_number_vn(goc)
		kq2=return_number_vn(goc+(random.randint(10,90))/10)
		kq3=return_number_vn(goc+(random.randint(90,130))/10)
		kq4=return_number_vn(goc+(random.randint(140,200))/10)
		noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông cạnh bằng ${latex(AB)}a$ , $S{A1}\\bot (ABCD), S{A1}={latex(SA)}a$."\
		f" Số đo góc giữa đường thẳng $S{{{D1}}}$ và mặt phẳng $(ABCD)$ là"
		
		noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{A1}}}$."\
		f" Điểm ${{{D1}}}$ có hình chiếu trên ${{(ABCD)}}$ là điểm ${{{D1}}}$.\n\n"\
		f" Do đó $S{{{D1}}}$ có hình chiếu trên ${{(ABCD)}}$ là ${{{A1}{D1}}}$.\n\n"\
		f"Suy ra $\\left(S{D1},(ABCD)\\right)= \\left(S{D1}, {A1}{D1}\\right)=\\widehat{{S{D1}{A1}}}$.\n\n"\
		f"$\\tan \\widehat{{S{D1}{A1}}}=\\dfrac{{S{D1}}} {{{A1}{D1}}}= \\dfrac{{{latex(SA*a)}}} {{{latex(AB*a)}}}={t}$.\n\n"\
		f"Suy ra $\\widehat{{S{D1}{A1}}} = {kq}^\\circ$."

	
    #Tạo các phương án
	pa_A= f"*${kq}^\\circ$"
	pa_B= f"${kq2}^\\circ$"
	pa_C= f"${kq3}^\\circ$"
	pa_D= f"${kq4}^\\circ$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B5_09]-M3. S.ABCD: ABCD h.vuông. Xác định góc giữa đường thẳng và mặt phẳng.
def uvxy9_L11_C8_B5_09(): 
	a=sp.symbols("a")  	
	A1=["A","B","C","D"]
	B1=["B","C","D","A"]
	C1=["C","D","A","B"]
	D1=["D","A","B","C"]
	M1=random.choice(["M", "E", "I"])
	N1=random.choice(["N", "F", "K"])
	P1=random.choice(["P", "G", "L"])
	Q1=random.choice(["Q", "H"])

	i=random.randint(0,3)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]	
	
	
	AB= random.choice([sqrt(i) for i in range(1,64)])
	SA= random.choice([sqrt(i) for i in range(1,64)])
	OB=AB*sqrt(2)/2
	SB=sqrt(SA**2+AB**2)
	t=OB/SB
	goc_rad=asin(t)
	goc_deg=math.degrees(goc_rad)

	#goc=round(asin(t).evalf() * 180 / pi,2)
	goc=round(goc_deg,2)
	if "." in str(t):
		t=latex(my_module.hien_phan_so(t))
	else:
		t=latex(t)
	kq=return_number_vn(goc)
	kq2=return_number_vn(goc+(random.randint(10,90))/10)
	kq3=return_number_vn(goc+(random.randint(90,130))/10)
	kq4=return_number_vn(goc+(random.randint(140,200))/10)

	noi_dung=f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông tâm ${{O}}$, cạnh bằng ${latex(AB)}a$ , $S{A1}\\bot (ABCD), S{A1}={latex(SA)}a$."\
	f" Số đo góc giữa đường thẳng $S{{{B1}}}$ và mặt phẳng $(S{A1}{C1})$ là"

	noi_dung_loigiai=f"Điểm ${{S}}$ có hình chiếu trên ${{(S{A1}{C1})}}$ là điểm ${{S}}$."\
	f" Điểm ${{{B1}}}$ có hình chiếu trên ${{(S{A1}{C1})}}$ là điểm ${{O}}$.\n\n"\
	f" Do đó $S{{{B1}}}$ có hình chiếu trên ${{(S{A1}{C1})}}$ là ${{SO}}$.\n\n"\
	f"Suy ra $\\left(S{B1},(S{A1}{C1})\\right)= \\left(S{B1}, SO\\right)=\\widehat{{{B1}SO}}$.\n\n"\
	f"$O{B1}=\\dfrac{{{B1}{D1}}}{{2}}=\\dfrac{{{A1}{B1}\\sqrt 2}}{{2}}={latex(OB)}$.\n\n"\
	f"$S{B1}=\\sqrt{{S{A1}^2+{A1}{B1}^2}}={latex(SB)}$.\n\n"\
	f"$\\sin \\widehat{{{B1}SO}}=\\dfrac{{O{B1}}} {{S{B1}}}= \\dfrac{{{latex(OB*a)}}} {{{latex(SB*a)}}}={t}$.\n\n"\
		f"Suy ra $\\widehat{{{B1}SO}} = {kq}^\\circ$."
	
	#Tạo các phương án
	pa_A= f"*${kq}^\\circ$"
	pa_B= f"${kq2}^\\circ$"
	pa_C= f"${kq3}^\\circ$"
	pa_D= f"${kq4}^\\circ$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A1, B1, C1, D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"{code_hinh}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

###################################################

#[D11_C8_B6_10]-M1. Nhận dạng hình lăng trụ
def uvxy9_L11_C8_B6_10(): 
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	
	ten_langtru = f"ABCD.{A1}{B1}{C1}{D1}"
	noi_dung=f"Cho hình lăng trụ đều ${{{ten_langtru}}}$. Khẳng định nào sau đây đúng"
	
	kq=random.choice([f'${{{A1}{B1}{C1}{D1}}}$ là hình vuông',f'Các cạnh bên của hình lăng trụ vuông góc với 2 đáy',
	 f'Các cạnh bên của hình lăng trụ bằng nhau',f'Hai đáy có diện tích bằng nhau',
	 f'Các mặt bên vuông góc với các mặt đáy', f'Các mặt bên có diện tích bằng nhau'])
	kq2=random.choice([f'${{{A1}{B1}{C1}{D1}}}$ là hình chữ nhật',f'${{ABCD}}$ là hình thang'])
	kq3=random.choice([f'Các mặt bên là hình vuông',f'Các mặt bên có diện tích bằng mặt đáy'])
	kq4=random.choice([f'Độ dài các cạnh bên bằng độ dài các cạnh đáy',f'Hai đáy là các tam giác đều',
		f'Các cạnh bên có độ dài bằng cạnh đáy'])
	
    #Tạo các phương án
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
	noi_dung_loigiai=f"{kq} là khẳng định đúng."
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n    {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C8_B6_11]-M1. Cho hình lập phương có độ dài cạnh. Tính thể tích.
def uvxy9_L11_C8_B6_11():
	a=random.choice([sqrt(i) for i in range(1,100)])
	
	kq=a**3
	kq2=a**2
	kq3=1/2*a**2
	kq4=random.choice([2*a,3*a])

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=latex(kq)
	kq2=kq2
	kq3=latex(my_module.hien_phan_so(kq3))
	kq4=latex(kq4)	
	

	pa_A= f"*$\\displaystyle {{V={kq}}}a^3$"
	pa_B= f"$\\displaystyle {{V={kq2}}}a^3$"
	pa_C= f"$\\displaystyle {{V={kq3}}}a^3$"
	pa_D= f"$\\displaystyle {{V={kq4}}}a^3$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	

	noi_dung = thay_hinh_hoc(f"Cho khối lập phương có cạnh bằng ${{{latex(a)}}}a$. Thể tích ${{V}}$ của khối lập phương đã cho bằng")
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"$V={latex(a)}^3a^3={latex(a**3)}a^3$."

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_12]-M1. Cho hình hộp chữ nhật có độ dài cạnh. Tính thể tích.
def uvxy9_L11_C8_B6_12():
	a=random.choice([i for i in range(1,10)])
	b=random.choice([i for i in range(1,10)])
	c=random.choice([i for i in range(1,10)])
	
	kq=a*b*c
	kq2=1/2*a*b*c
	kq3=1/3*a*b*c
	kq4=1/6*a*b*c

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=latex(kq)
	kq2=phan_so(kq2)
	kq3=phan_so(kq3)
	kq4=phan_so(kq4)
	

	pa_A= f"*$\\displaystyle {{V={kq}}}a^3$"
	pa_B= f"$\\displaystyle {{V={kq2}}}a^3$"
	pa_C= f"$\\displaystyle {{V={kq3}}}a^3$"
	pa_D= f"$\\displaystyle {{V={kq4}}}a^3$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	AB=random.choice(["AB", "A'B'", "CD", "C'D'"])
	AD=random.choice(["AD", "A'B'", "BC", "B'C'"])
	AA=random.choice(["AA'", "BB'", "CC'", "DD'"])
	

	noi_dung = thay_hinh_hoc(f"Cho khối hộp chữ nhật ${{ABCD.A'B'C'D'}}$ có ${AB}={a}a, {AD}={b}a,{AA}={c}a$."\
		f" Thể tích ${{V}}$ của khối hộp chữ nhật đã cho bằng")
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"$V={latex(a)}.{latex(b)}.{latex(c)}a^3={latex(a*b*c)}a^3$."

	debai= f"{noi_dung}\n\n"
	phuongan= thay_hinh_hoc(f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n")
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C8_B6_13]-M2. H.chóp đáy tam giác vuông cân, mặt bên vuông góc đáy. Tính thể tích
def uvxy9_L11_C8_B6_13():
	a=sp.symbols("a")
	AB=sqrt(random.randint(1,10))*a
	A,B,C=random.sample(["A","B","C"],3)


	noi_dung=(
	f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông cân tại ${{{B}}}$ và ${A}{B}={latex(AB)}$."
	f" Tam giác ${{S{A}{B}}}$ đều nằm trong mặt phẳng vuông góc với đáy. Thể tích ${{V}}$ của khối chóp ${{S.ABC}}$ là"
	)

	
	AM=AB*sqrt(3)/2
	S=1/2*(AB)**2
	V=1/3*S*AM
	AM_f=AB*sqrt(2)/2

	kq=latex(nsimplify(V))
	kq2=latex(nsimplify(S*AM))
	kq3=latex(nsimplify(S*AM_f))
	kq4=latex(nsimplify(1/3*S*AM_f))

	noi_dung_loigiai=(
	f"$S_{{ABC}}=\\dfrac{{1}}{{2}}.{A}{B}.{B}{C}=\\dfrac{{1}}{{2}}.{latex(AB)}.{latex(AB)}={latex(nsimplify(S))}$.\n\n"
	f"Gọi ${{M}}$ là trung điểm của ${{{A}{B}}}$. Khi đó: $SM\\bot (ABC)$.\n\n"
	f" $SM=\\dfrac{{{latex(AB*sqrt(3))}}}{{2}}={{{latex(nsimplify(AM))}}}$.\n\n"
	f" $V=\\dfrac{{1}}{{3}}.{{S_{{ABC}}}}.SM={{{latex(nsimplify(V))}}}$.")

	pa_A= f"*$V={kq}$"
	pa_B= f"$V={kq2}$"
	pa_C= f"$V={kq3}$"
	pa_D= f"$V={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}"

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

#[D11_C8_B6_14]-M2. H.chóp đáy tam giác đều, mặt bên vuông góc đáy. Tính thể tích
def uvxy9_L11_C8_B6_14():
	a=sp.symbols("a")
	AB=sqrt(random.randint(1,10))*a
	A,B,C=random.sample(["A","B","C"],3)


	noi_dung=(
	f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều và ${A}{B}={latex(AB)}$."
	f" Tam giác ${{S{A}{B}}}$ đều nằm trong mặt phẳng vuông góc với đáy. Thể tích ${{V}}$ của khối chóp ${{S.ABC}}$ là"
	)

	
	AM=AB*sqrt(3)/2
	S=(AB)**2*sqrt(3)/4
	V=1/3*S*AM
	AM_f=AB*sqrt(2)/2

	kq=latex(nsimplify(V))
	kq2=latex(nsimplify(S*AM))
	kq3=latex(nsimplify(S*AM_f))
	kq4=latex(nsimplify(1/3*S*AM_f))

	noi_dung_loigiai=(
	f"$S_{{ABC}}=\\dfrac{{{A}{B}^2\\sqrt 3}}{{4}}={latex(nsimplify(S))}$.\n\n"
	f"Gọi ${{M}}$ là trung điểm của ${{{A}{B}}}$. Khi đó: $SM\\bot (ABC)$.\n\n"
	f" $SM=\\dfrac{{{latex(AB*sqrt(3))}}}{{2}}={{{latex(nsimplify(AM))}}}$.\n\n"
	f" $V=\\dfrac{{1}}{{3}}.{{S_{{ABC}}}}.SM={{{latex(nsimplify(V))}}}$.")

	pa_A= f"*$V={kq}$"
	pa_B= f"$V={kq2}$"
	pa_C= f"$V={kq3}$"
	pa_D= f"$V={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}"

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

#[D11_C8_B6_15]-M2. H.chóp đáy h.vuông, cạnh bên v.g đáy. Tính V
def uvxy9_L11_C8_B6_15():
	a=sp.symbols("a")
	while True:
		AB=sqrt(random.randint(1,10))*a
		SA=sqrt(random.randint(1,10))*a
		if AB!=SA:
			break
	A,B,C,D=random.sample(["A","B","C","D"],4)


	noi_dung=(
	f"Cho hình chóp ${{S.ABCD}}$ có đáy là hình vuông và ${A}{B}={latex(AB)}$."
	f" Biết $S{A}\\bot (ABCD)$ và $S{A}={latex(SA)}$. Thể tích ${{V}}$ của khối chóp ${{S.ABCD}}$ là"
	)	
	
	S=(AB)**2
	V=1/3*S*SA

	kq=latex(nsimplify(V))
	kq2=latex(nsimplify(S*SA))
	kq3=latex(nsimplify(1/2*S*SA))
	kq4=latex(nsimplify(2*S*SA))

	noi_dung_loigiai=(
	f"$S_{{ABCD}}={A}{B}^2={latex(nsimplify(S))}$.\n\n"		
	f" $V=\\dfrac{{1}}{{3}}.{{S_{{ABCD}}}}.S{A}=\\dfrac{{1}}{{3}}.{latex(nsimplify(S))}.{latex(SA)}={{{latex(nsimplify(V))}}}$.")

	pa_A= f"*$V={kq}$"
	pa_B= f"$V={kq2}$"
	pa_C= f"$V={kq3}$"
	pa_D= f"$V={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}"

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

#[D11_C8_B6_16]-M2. H.chóp đáy h.chữ nhật, cạnh bên v.g đáy. Tính V
def uvxy9_L11_C8_B6_16():
	a=sp.symbols("a")
	SA=sqrt(random.randint(1,10))*a
	while True:
		AB=sqrt(random.randint(1,10))*a		
		AD=sqrt(random.randint(1,10))*a
		if AB!=AD:
			break
	A,B,C,D=random.sample(["A","B","C","D"],4)


	noi_dung=(
	f"Cho hình chóp ${{S.ABCD}}$ có đáy là chữ nhật với ${A}{B}={latex(AB)}, {A}{D}={latex(AD)}$."
	f" Biết $S{A}\\bot (ABCD)$ và $S{A}={latex(SA)}$. Thể tích ${{V}}$ của khối chóp ${{S.ABCD}}$ là"
	)	
	
	S=AB*AD
	V=1/3*S*SA

	kq=latex(nsimplify(V))
	kq2=latex(nsimplify(S*SA))
	kq3=latex(nsimplify(1/2*S*SA))
	kq4=latex(nsimplify(2*S*SA))

	noi_dung_loigiai=(
	f"$S_{{ABCD}}={A}{B}.{A}{D}={latex(nsimplify(S))}$.\n\n"		
	f" $V=\\dfrac{{1}}{{3}}.{{S_{{ABCD}}}}.S{A}=\\dfrac{{1}}{{3}}.{latex(nsimplify(S))}.{latex(SA)}={{{latex(nsimplify(V))}}}$.")

	pa_A= f"*$V={kq}$"
	pa_B= f"$V={kq2}$"
	pa_C= f"$V={kq3}$"
	pa_D= f"$V={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}"

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

#[D11_C8_B6_17]-M2. H.chóp đáy tam giác vuông cân, cạnh bên v.g đáy. Tính V
def uvxy9_L11_C8_B6_17():
	a=sp.symbols("a")
	SA=sqrt(random.randint(1,10))*a
	BC=sqrt(random.randint(1,10))*a

	A,B,C=random.sample(["A","B","C"],3)

	noi_dung=(
	f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác vuông cân tại ${{{A}}}$ với ${B}{C}={latex(BC)}$."
	f" Biết $S{A}\\bot (ABC)$ và $S{A}={latex(SA)}$. Thể tích ${{V}}$ của khối chóp ${{S.ABCD}}$ là")	
	
	S=1/4*BC**2
	V=1/3*S*SA

	kq=latex(nsimplify(V))
	kq2=latex(nsimplify(S*SA))
	kq3=latex(nsimplify(1/2*S*SA))
	kq4=latex(nsimplify(2*S*SA))

	noi_dung_loigiai=(
	f"$S_{{ABC}}=\\dfrac{{1}}{{4}}{B}{C}^2={latex(nsimplify(S))}$.\n\n"		
	f" $V=\\dfrac{{1}}{{3}}.{{S_{{ABC}}}}.S{A}=\\dfrac{{1}}{{3}}.{latex(nsimplify(S))}.{latex(SA)}={{{latex(nsimplify(V))}}}$.")

	pa_A= f"*$V={kq}$"
	pa_B= f"$V={kq2}$"
	pa_C= f"$V={kq3}$"
	pa_D= f"$V={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}"

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

#[D11_C8_B6_18]-M2. H.chóp đáy h.chữ nhật có cạnh đáy và cạnh bên SB. Tính V
def uvxy9_L11_C8_B6_18():
	a=sp.symbols("a")
	SA=sqrt(random.randint(1,10))*a
	while True:
		AB=sqrt(random.randint(1,10))*a		
		AD=sqrt(random.randint(1,10))*a
		if AB!=AD:
			break
	SB=sqrt(SA**2+AB**2)
	A,B,C,D=random.sample(["A","B","C","D"],4)


	noi_dung=(
	f"Cho hình chóp ${{S.ABCD}}$ có đáy là chữ nhật với ${A}{B}={latex(AB)}, {A}{D}={latex(AD)}$."
	f" Biết $S{A}\\bot (ABCD)$ và $S{B}={latex(SB)}$. Thể tích ${{V}}$ của khối chóp ${{S.ABCD}}$ là"
	)	
	
	S=AB*AD
	V=1/3*S*SA

	kq=latex(nsimplify(V))
	kq2=latex(nsimplify(S*SA))
	kq3=latex(nsimplify(1/2*S*SA))
	kq4=latex(nsimplify(2*S*SA))

	noi_dung_loigiai=(
	f"$S{A}=\\sqrt{{S{B}^2-{A}{B}^2}}={latex(SA)}$.\n\n"
	f"$S_{{ABCD}}={A}{B}.{A}{D}={latex(nsimplify(S))}$.\n\n"		
	f" $V=\\dfrac{{1}}{{3}}.{{S_{{ABCD}}}}.S{A}=\\dfrac{{1}}{{3}}.{latex(nsimplify(S))}.{latex(SA)}={{{latex(nsimplify(V))}}}$.")

	pa_A= f"*$V={kq}$"
	pa_B= f"$V={kq2}$"
	pa_C= f"$V={kq3}$"
	pa_D= f"$V={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}"

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

#BÀI 7 -  GÓC

#[D11_C8_B7_01]-TF-M2. S.ABC: đáy tam giác. Tạo câu đúng-sai: Thể tích, Góc đường mặt, Góc mặt mặt, Đường vuông góc mặt
def uvxy9_L11_C8_B7_01():
	a=sp.symbols("a")  	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]

	i=random.randint(0,2)
	A1, B1, C1= A1[i], B1[i], C1[i]
		
	AB=random.randint(1,9)
	SA=random.choice([sqrt(i) for i in range(1,100)])

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều có $S{A1}\\bot (ABC), {A1}{B1}={AB}a,S{A1}={latex(SA)}a$.\n\n"\
	f"{file_name}\n"\
	f" Xét tính đúng sai của các khẳng định sau")
		
	S=AB**2*sqrt(3)/4
	V=1/3*S*SA
	V=sqrt(AB**4*SA**2*3/144)

	kq1_T=f"*Thể tích của khối chóp đã cho bằng ${latex(rutgon_can(V))}a^3$"
	kq1_F=f"Thể tích của khối chóp đã cho bằng ${latex(rutgon_can(S*SA))}a^3$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là đúng.\n\n"\
	f"$V=\\dfrac{{1}}{{3}}S_{{ABC}}.S{A1}=\\dfrac{{1}}{{3}}.\\dfrac{{{AB**2}\\sqrt{{3}}}}{{4}}a^2.{latex(SA)}a={latex(rutgon_can(V))}a^3$"
	if kq1==kq1_F:
	    loigiai_1=f"Khẳng định đã cho là sai\n\n"\
	f"$V=\\dfrac{{1}}{{3}}S_{{ABC}}.S{A1}=\\dfrac{{1}}{{3}}.\\dfrac{{{AB**2}\\sqrt{{3}}}}{{4}}a^2.{latex(SA)}a={latex(rutgon_can(V))}a^3$"
	
	chon=random.randint(1,2)
	ten_goc=random.choice([f"$\\widehat{{S{B1}{C1}}}$", f"$\\widehat{{{A1}{B1}{C1}}}$", f"$\\widehat{{{C1}{B1}{A1}}}$"])
	if chon==1:	
		kq2_T=f"*Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{B1}{A1}}}$"
		kq2_F=f"Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là {ten_goc}"
		kq2=random.choice([kq2_T, kq2_F])
		loigiai_2=f"Khẳng định đã cho là đúng.\n\n"\
		f"Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{B1}{A1}}}$.\n\n"	
		if kq2==kq2_F:
		    loigiai_2=f"Khẳng định đã cho là sai.\n\n"\
		f"Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{B1}{A1}}}$.\n\n"

	if chon==2:	
		kq2_T=f"*Góc giữa đường thẳng ${{S{C1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{C1}{A1}}}$"
		kq2_F=f"Góc giữa đường thẳng ${{S{C1}}}$ và mặt phẳng ${{(ABC)}}$ là {ten_goc}"
		kq2=random.choice([kq2_T, kq2_F])
		loigiai_2=f"Khẳng định đã cho là đúng.\n\n"\
		f"Góc giữa đường thẳng ${{S{C1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{C1}{A1}}}$."	
		if kq2==kq2_F:
		    loigiai_2=f"Khẳng định đã cho là sai.\n\n"\
		f"Góc giữa đường thẳng ${{S{C1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{C1}{A1}}}$."

	chon=random.randint(1,2)
	if chon==1:
		mat=random.choice([f"\\widehat{{S{B1}{A1}}}", f"\\widehat{{S{B1}{C1}}}"])	
		kq3_T=f"*Góc giữa hai mặt phẳng $(S{B1}{C1})$ và $(ABC)$ là $\\widehat{{S{A1}M}}$ với M là trung điểm của ${{{B1}{C1}}}$"
		kq3_F=f"Góc giữa hai mặt phẳng $(S{B1}{C1})$ và $(ABC)$ là $\\widehat{{S{B1}{A1}}}$"
		kq3=random.choice([kq3_T, kq3_F])
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
		f"Gọi M là trung điểm của ${{{B1}{C1}}}, {A1}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
		f"Góc giữa $(S{B1}{C1})$ và ${{(ABC)}}$ là $\\widehat{{S{A1}M}}$."	
		if kq3==kq3_F:
		    loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f"Gọi M là trung điểm của ${{{B1}{C1}}}, {A1}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
		f"Góc giữa $(S{B1}{C1})$ và ${{(ABC)}}$ là $\\widehat{{S{A1}M}}$."
	if chon==2:
		goc=random.choice([30,45,60])
		mat=random.choice([f"\\widehat{{S{B1}{A1}}}", f"\\widehat{{S{B1}{C1}}}"])	
		kq3_T=f"*Góc giữa hai mặt phẳng $(S{A1}{B1})$ và $(ABC)$ bằng $90^\\circ$"
		kq3_F=f"Góc giữa hai mặt phẳng $(S{A1}{B1})$ và $(ABC)$ bằng ${goc}^\\circ$"
		kq3=random.choice([kq3_T, kq3_F])
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
		f"$S{A1}\\bot (ABC),S{A1} \\subset (S{A1}{B1})\\Rightarrow (S{A1}{B1})\\bot (ABC)$."
	
		if kq3==kq3_F:
		    loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n"\
		f"$S{A1}\\bot (ABC),S{A1} \\subset (S{A1}{B1})\\Rightarrow (S{A1}{B1})\\bot (ABC)$."	
	
	mat=random.choice([f"(S{A1}{B1})", f"(S{A1}{C1})"])
	kq4_T=f"*$(S{A1}M)\\bot (S{B1}{C1})$ với M là trung điểm cạnh ${{{B1}{C1}}}$"
	kq4_F=f"$(S{A1}M)\\bot {mat}$ với M là trung điểm cạnh ${{{B1}{C1}}}$"
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
	f"Gọi M là trung điểm của ${{{B1}{C1}}}$.\n\n"\
	f"${B1}{C1}\\bot {A1}M,{B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}M)$.\n\n"\
	f"$\\Rightarrow (S{A1}M)\\bot (S{B1}{C1})$."
	if kq4==kq4_F:
	    loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n"\
	f"Gọi M là trung điểm của ${{{B1}{C1}}}$.\n\n"\
	f"${B1}{C1}\\bot {A1}M,{B1}{C1}\\bot S{A1} \\Rightarrow {B1}{C1} \\bot (S{A1}M)$.\n\n"\
	f"$\\Rightarrow (S{A1}M)\\bot (S{B1}{C1})$."

	#Trộn các phương án
	list_PA =[kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_PA.append(kq1)
	list_TF=my_module.tra_ve_TF(list_PA)

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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")
	noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$. Biết ${A1}{B1}={AB}a,S{A1}={latex(SA)}a$.\n\n"\
	f"{code_hinh}\n"\
	f" Xét tính đúng sai của các khẳng định sau"

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\choiceTF\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"        
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B7_02]-TF-M3. S.ABC: đáy tam giác. Tạo câu đúng-sai: Thể tích, Góc đường mặt, Góc mặt mặt, Khoảng cách
def uvxy9_L11_C8_B7_02():
	a=sp.symbols("a")  	
	A1=["A","B","C"]
	B1=["B","C","A"]
	C1=["C","A","B"]

	i=random.randint(0,2)
	A1, B1, C1= A1[i], B1[i], C1[i]
		
	AB=random.randint(1,9)
	SA=random.choice([sqrt(i) for i in range(1,100)])

	code_hinh = codelatex_hinhchop_tamgiac_canhvg("S",A1, B1, C1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	noi_dung=thay_hinh_hoc(f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều có $S{A1}\\bot (ABC), {A1}{B1}={AB}a,S{A1}={latex(SA)}a$.\n\n"\
	f"{file_name}\n"\
	f" Xét tính đúng sai của các khẳng định sau")
		
	S=AB**2*sqrt(3)/4
	V=1/3*S*SA
	V=sqrt(AB**4*SA**2*3/144)

	kq1_T=f"*Thể tích của khối chóp đã cho bằng ${latex(rutgon_can(V))}a^3$"
	kq1_F=f"Thể tích của khối chóp đã cho bằng ${latex(rutgon_can(S*SA))}a^3$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là đúng.\n\n"\
	f"$V=\\dfrac{{1}}{{3}}S_{{ABC}}.S{A1}=\\dfrac{{1}}{{3}}.\\dfrac{{{AB**2}\\sqrt{{3}}}}{{4}}a^2.{latex(SA)}a={latex(rutgon_can(V))}a^3$"
	if kq1==kq1_F:
	    loigiai_1=f"Khẳng định đã cho là sai\n\n"\
	f"$V=\\dfrac{{1}}{{3}}S_{{ABC}}.S{A1}=\\dfrac{{1}}{{3}}.\\dfrac{{{AB**2}\\sqrt{{3}}}}{{4}}a^2.{latex(SA)}a={latex(rutgon_can(V))}a^3$"
	t=SA/AB
	goc=round(atan(t).evalf() * 180 / pi,2)
	goc_2=goc+random.randint(1,3)

	ten_goc=random.choice([f"$\\widehat{{S{B1}{C1}}}$", f"$\\widehat{{{A1}{B1}{C1}}}$", f"$\\widehat{{{C1}{B1}{A1}}}$"])	
	
	kq2_T=f"*Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{B1}{A1}}}$"
	kq2_F=f"Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là {ten_goc}"
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là đúng.\n\n"\
	f"Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{B1}{A1}}}$.\n\n"\
	f"$\\tan \\widehat{{S{B1}{A1}}}=\\dfrac{{S{A1}}}{{{A1}{B1}}}=\\dfrac{{{latex(SA)}a}}{{{AB}a}}={latex(t)}\\Rightarrow \\widehat{{S{B1}{A1}}}={return_number_vn(goc)}^\\circ$."
	if kq2==kq2_F:
	    loigiai_2=f"Khẳng định đã cho là sai.\n\n"\
	f"Góc giữa đường thẳng ${{S{B1}}}$ và mặt phẳng ${{(ABC)}}$ là $\\widehat{{S{B1}{A1}}}$.\n\n"\
	f"$\\tan \\widehat{{S{B1}{A1}}}=\\dfrac{{S{A1}}}{{{A1}{B1}}}=\\dfrac{{{latex(SA)}a}}{{{AB}a}}={latex(t)}\\Rightarrow \\widehat{{S{B1}{A1}}}={return_number_vn(goc)}^\\circ$."

	AM=AB*sqrt(3)/2
	t=SA/AM		
	goc=round(atan(t).evalf() * 180 / pi,2)
	goc_2=round(atan(SA/AB).evalf() * 180 / pi,2)
	
	kq3_T=f"*Góc giữa hai mặt phẳng $(S{B1}{C1})$ và $(ABC)$ bằng ${return_number_vn(goc)}^\\circ$"
	kq3_F=f"Góc giữa hai mặt phẳng $(S{B1}{C1})$ và $(ABC)$ bằng ${return_number_vn(goc_2)}^\\circ$"
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
	f"Gọi M là trung điểm của ${{{B1}{C1}}}, {A1}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
	f"Góc giữa $(S{B1}{C1})$ và ${{(ABC)}}$ là $\\widehat{{S{A1}M}}$.\n\n"\
	f"$\\tan \\widehat{{S{A1}M}}=\\dfrac{{S{A1}}}{{{A1}M}}=\\dfrac{{{latex(SA)}a}}{{{latex(AM)}a}}={latex(t)}\\Rightarrow \\widehat{{S{A1}M}}={return_number_vn(goc)}^\\circ$."
	if kq3==kq3_F:
	    loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n"\
	f"Gọi M là trung điểm của ${{{B1}{C1}}}, {A1}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
	f"Góc giữa $(S{B1}{C1})$ và ${{(ABC)}}$ là $\\widehat{{S{A1}M}}$.\n\n"\
	f"$\\tan \\widehat{{S{A1}M}}=\\dfrac{{S{A1}}}{{{A1}M}}=\\dfrac{{{latex(SA)}a}}{{{latex(AM)}a}}={latex(t)}\\Rightarrow \\widehat{{S{A1}M}}={return_number_vn(goc)}^\\circ$."
	
	BM=AB*sqrt(3)/2
	kq4_T=f"*Khoảng cách từ điểm ${{{B1}}}$ đến mặt phẳng ${{(S{A1}{C1})}}$ bằng ${latex(BM)}a$"
	kq4_F=f" Khoảng cách từ điểm ${{{B1}}}$ đến mặt phẳng ${{(S{A1}{C1})}}$ bằng ${latex(AB*sqrt(3))}a$"
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
	f"Gọi M là trung điểm của ${{{A1}{C1}}}, {B1}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
	f"${B1}M\\bot {A1}{C1},{B1}M\\bot S{A1} \\Rightarrow {B1}M \\bot (S{A1}{C1})$.\n\n"\
	f"$d({B1},(S{A1}{C1}))={B1}M={latex(BM)}a$."
	if kq4==kq4_F:
	    loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n"\
	f"Gọi M là trung điểm của ${{{A1}{C1}}}, {B1}M={latex(AB*sqrt(3)/2)}a$.\n\n"\
	f"${B1}M\\bot {A1}{C1},{B1}M\\bot S{A1} \\Rightarrow {B1}M \\bot (S{A1}{C1})$.\n\n"\
	f"$d({B1},(S{A1}{C1}))={B1}M={latex(BM)}a$."

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3]
	random.shuffle(list_PA)
	list_PA.append(kq4)
	list_TF=my_module.tra_ve_TF(list_PA)

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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")
	noi_dung=f"Cho hình chóp ${{S.ABC}}$ có đáy là tam giác đều, $S{A1}\\bot (ABC)$. Biết ${A1}{B1}={AB}a,S{A1}={latex(SA)}a$.\n\n"\
	f"{code_hinh}\n"\
	f" Xét tính đúng sai của các khẳng định sau"

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\choiceTF\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"        
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B7_03]-TF-M3. S.ABCD: đáy hình vuông. Xét Đ-S: đường cao, 2 mặt vuông góc, d(điểm,mp), V
def uvxy9_L11_C8_B7_03():
	a=sp.symbols("a")
	S="S"
	A=["A","B","C","D"]
	B=["B","C","D","A"]
	C=["C","D","A","B"]
	D=["D","A","B","C"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	O=random.choice(["O","I","E" ])

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	AB=random.randint(1,6)
	SA=random.randint(1,6)
	SB=sqrt(AB**2+SA**2)

	noi_dung = f"Cho hình chóp ${{S.{A}{B}{C}{D}}}$ có ${S}{A}\\bot ({A}{B}{C}{D})$, đáy là hình vuông tâm ${{{O}}}$ cạnh bằng ${{{AB}}}$, ${{{S}{B}={latex(SB)}}}$."
	f" Xét tính đúng-sai của các khẳng định sau."
	
	
	kq1_T=f"* Chiều cao của hình chóp ${{S.{A}{B}{C}{D}}}$ là độ dài cạnh ${{{S}{A}}}$" 
	kq1_F=f"Chiều cao của hình chóp ${{S.{A}{B}{C}{D}}}$ là độ dài cạnh ${{{random.choice([f"{S}{B}",f"{S}{C}", f"{S}{D}",  ])}}}$"
	
	HDG=f"Chiều cao của hình chóp ${{S.{A}{B}{C}{D}}}$ là độ dài cạnh ${{{S}{A}}}$."
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,6)
	
	
	if chon==1:
		kq2_T=f"* Hai mặt phẳng $({S}{A}{B})$ và $({S}{A}{D})$ là hai mặt phẳng vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{A}{D})$ là hai mặt phẳng không vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{A}{D})$ là vuông góc nhau vì có ${A}{B}\\bot ({S}{A}{D})$ và ${A}{B}\\subset ({S}{A}{B})$."	
	if chon==2:
		kq2_T=f"* Hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là hai mặt phẳng vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là hai mặt phẳng không vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là vuông góc nhau vì có ${B}{C}\\bot ({S}{A}{B})$ và ${B}{C}\\subset ({S}{B}{C})$."

	if chon==3:
		kq2_T=f"* Hai mặt phẳng $({S}{A}{D})$ và $({S}{C}{D})$ là hai mặt phẳng vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{A}{D})$ và $({S}{C}{D})$ là hai mặt phẳng không vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{A}{D})$ và $({S}{C}{D})$ là vuông góc nhau vì có ${C}{D}\\bot ({S}{A}{D})$ và ${C}{D}\\subset ({S}{C}{D})$."

	if chon==4:
		kq2_T=f"* Hai mặt phẳng $({S}{B}{D})$ và $({A}{B}{C}{D})$ là hai mặt phẳng không vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{B}{D})$ và $({A}{B}{C}{D})$ là hai mặt phẳng vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{B}{D})$ và $({A}{B}{C}{D})$ là không vuông góc nhau."

	if chon==5:
		kq2_T=f"* Hai mặt phẳng $({S}{B}{C})$ và $({A}{B}{C}{D})$ là hai mặt phẳng không vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{B}{C})$ và $({S}{C}{D})$ là hai mặt phẳng vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{B}{C})$ và $({A}{B}{C}{D})$ là hai mặt phẳng không vuông góc."

	if chon==6:
		kq2_T=f"* Hai mặt phẳng $({S}{B}{C})$ và $({S}{A}{D})$ là hai mặt phẳng không vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{B}{C})$ và $({S}{A}{D})$ là hai mặt phẳng vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{B}{C})$ và $({S}{A}{D})$ là hai mặt phẳng không vuông góc."
	
	
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	V=1/3*AB**2*SA
	V_f=AB**2*SA

	kq3_T=f"* Thể tích của khối chóp đã cho bằng ${latex(nsimplify(V))}$" 
	kq3_F=f"Thể tích của khối chóp đã cho bằng ${latex(nsimplify(V_f))}$"
	
	HDG=(f"${S}{A}^2={S}{B}^2-{A}{B}^2={SB**2}-{AB**2}={SA**2}\\Rightarrow S{A}={SA}$.\n\n"
		f"Thể tích của khối chóp đã cho bằng:\n\n"
		f" $V=\\dfrac{{1}}{{3}}.S_{{{A}{B}{C}{D}}}.S{A}=\\dfrac{{1}}{{3}}.{AB**2}.{SA}={latex(nsimplify(V))}$.")
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,3)

	if chon==1:
		d=latex(nsimplify((SA*AB)/sqrt(SA**2+AB**2)))
		d_f=latex(nsimplify((SA*AB)/(SA**2+AB**2+random.randint(1,2))))
		kq4_T=f"* Khoảng cách từ điểm ${{{D}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d}$"
		kq4_F=f" Khoảng cách từ điểm ${{{D}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d_f}$"

		
		HDG=(f"Ta có: ${B}{C}\\bot S{A},{B}{C}\\bot {A}{B}$.\n\n"
			f"Kẻ ${A}H\\bot {S}{B}$, suy ra ${A}H\\bot (S{B}{C})$.\n\n"
			f"Vì ${A}{D}//({S}{B}{C})$ nên $d({D},({S}{B}{C}))=d({A},({S}{B}{C}))={A}H=\\dfrac{{{S}{A}.{A}{B}}}{{\\sqrt{{{S}{A}^2+{A}{B}^2}}}}$"
			f"$=\\dfrac{{{SA}.{AB}}}{{\\sqrt{{{SA**2}+{AB**2}}}}}={d}$.")
	
	if chon==2:
		d=latex(nsimplify(1/2*(SA*AB)/sqrt(SA**2+AB**2)))
		d_f=latex(nsimplify(2*(SA*AB)/sqrt(SA**2+AB**2)))
		kq4_T=f"* Khoảng cách từ điểm ${{{O}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d}$"
		kq4_F=f" Khoảng cách từ điểm ${{{O}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d_f}$"

		
		HDG=(f"Ta có: ${B}{C}\\bot S{A},{B}{C}\\bot {A}{B}$.\n\n"
			f"Kẻ ${A}H\\bot {S}{B}$, suy ra ${A}H\\bot (S{B}{C})$.\n\n"
			f"$d({O},({S}{B}{C}))=\\dfrac{{1}}{{2}}d({A},({S}{B}{C}))=\\dfrac{{1}}{{2}}{A}H=\\dfrac{{1}}{{2}}\\dfrac{{{S}{A}.{A}{B}}}{{\\sqrt{{{S}{A}^2+{A}{B}^2}}}}$"
			f"$=\\dfrac{{1}}{{2}}\\dfrac{{{SA}.{AB}}}{{\\sqrt{{{SA**2}+{AB**2}}}}}={d}$.")

	if chon==3:
		M=random.choice(["M","N","P"])
		d=latex(nsimplify((SA*AB)/sqrt(SA**2+AB**2)))
		d_f=latex(nsimplify((SA*AB)/(SA**2+AB**2+random.randint(1,2))))
		kq4_T=(f"* Gọi ${{{M}}}$ là điểm thuộc cạnh ${{{A}{D}}}$ sao cho ${A}{M}={random.randint(2,4)}{M}{D}$."
			f" Khoảng cách từ điểm ${{{M}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d}$")
		kq4_F=(f"Gọi ${{{M}}}$ là điểm thuộc cạnh ${{{A}{D}}}$ sao cho ${A}{M}={random.randint(2,4)}{M}{D}$."
			f" Khoảng cách từ điểm ${{{M}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d_f}$")

		
		HDG=(f"Ta có: ${B}{C}\\bot S{A},{B}{C}\\bot {A}{B}$.\n\n"
			f"Kẻ ${A}H\\bot {S}{B}$, suy ra ${A}H\\bot (S{B}{C})$.\n\n"
			f"$d({M},({S}{B}{C}))=d({A},({S}{B}{C}))={A}H=\\dfrac{{{S}{A}.{A}{B}}}{{\\sqrt{{{S}{A}^2+{A}{B}^2}}}}$"
			f"$=\\dfrac{{{SA}.{AB}}}{{\\sqrt{{{SA**2}+{AB**2}}}}}={d}$.")
	
	
	kq4=random.choice([kq4_T, kq4_F])
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
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D11_C8_B7_04]-TF-M3. S.ABCD: đáy hình chữ nhật. Xét Đ-S: đường cao, 2 mặt vuông góc, d(điểm,mp), V
def uvxy9_L11_C8_B7_04():
	a=sp.symbols("a")
	S="S"
	A=["A","B","C","D"]
	B=["B","C","D","A"]
	C=["C","D","A","B"]
	D=["D","A","B","C"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	O=random.choice(["O","I","E" ])

	code_hinh = codelatex_hinhchop_hbh_canhvg("S",A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	#file_name = my_module.pdftoimage_timename(code)
	file_name=""

	AB=random.randint(1,5)
	AD=AB+random.randint(1,3)
	SA=random.choice([sqrt(i) for i in range(1,10)])
	SB=sqrt(SA**2+AB**2)

	noi_dung = f"Cho hình chóp ${{S.{A}{B}{C}{D}}}$ có ${S}{A}\\bot ({A}{B}{C}{D})$, đáy là hình chữ nhật tâm ${{{O}}}$, ${A}{B}={AB},{A}{D}={AD}$, ${{{S}{B}={latex(SB)}}}$."
	f" Xét tính đúng-sai của các khẳng định sau:"
	
	
	kq1_T=f"* Chiều cao của hình chóp ${{S.{A}{B}{C}{D}}}$ bằng ${{{latex(SA)}}}$" 
	kq1_F=f"Chiều cao của hình chóp ${{S.{A}{B}{C}{D}}}$ bằng ${{{latex(SB)}}}$"
	
	HDG=f"Chiều cao của hình chóp ${{S.{A}{B}{C}{D}}}$ là độ dài cạnh ${{{S}{A}}}=\\sqrt{{{S}{B}^2-{A}{B}^2}}=\\sqrt{{{SB**2}-{AB**2}}}={latex(SA)}$."
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,6)
	
	
	if chon==1:
		kq2_T=f"* Hai mặt phẳng $({S}{A}{B})$ và $({S}{A}{D})$ là hai mặt phẳng vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{A}{D})$ là hai mặt phẳng không vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{A}{D})$ là vuông góc nhau vì có ${A}{B}\\bot ({S}{A}{D})$ và ${A}{B}\\subset ({S}{A}{B})$."	
	if chon==2:
		kq2_T=f"* Hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là hai mặt phẳng vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là hai mặt phẳng không vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{A}{B})$ và $({S}{B}{C})$ là vuông góc nhau vì có ${B}{C}\\bot ({S}{A}{B})$ và ${B}{C}\\subset ({S}{B}{C})$."

	if chon==3:
		kq2_T=f"* Hai mặt phẳng $({S}{A}{D})$ và $({S}{C}{D})$ là hai mặt phẳng vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{A}{D})$ và $({S}{C}{D})$ là hai mặt phẳng không vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{A}{D})$ và $({S}{C}{D})$ là vuông góc nhau vì có ${C}{D}\\bot ({S}{A}{D})$ và ${C}{D}\\subset ({S}{C}{D})$."

	if chon==4:
		kq2_T=f"* Hai mặt phẳng $({S}{B}{D})$ và $({A}{B}{C}{D})$ là hai mặt phẳng không vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{B}{D})$ và $({A}{B}{C}{D})$ là hai mặt phẳng vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{B}{D})$ và $({A}{B}{C}{D})$ là không vuông góc nhau."

	if chon==5:
		kq2_T=f"* Hai mặt phẳng $({S}{B}{C})$ và $({A}{B}{C}{D})$ là hai mặt phẳng không vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{B}{C})$ và $({S}{C}{D})$ là hai mặt phẳng vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{B}{C})$ và $({A}{B}{C}{D})$ là hai mặt phẳng không vuông góc."

	if chon==6:
		kq2_T=f"* Hai mặt phẳng $({S}{B}{D})$ và $({S}{A}{D})$ là hai mặt phẳng không vuông góc"
		kq2_F=f"Hai mặt phẳng $({S}{B}{D})$ và $({S}{A}{D})$ là hai mặt phẳng vuông góc"		
		HDG=f"Hai mặt phẳng $({S}{B}{D})$ và $({S}{A}{D})$ là hai mặt phẳng không vuông góc."
	
	
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	V=1/3*AB*AD*SA
	V_f=AB*AD*SA

	kq3_T=f"* Thể tích của khối chóp đã cho bằng ${latex(nsimplify(V))}$" 
	kq3_F=f"Thể tích của khối chóp đã cho bằng ${latex(nsimplify(V_f))}$"
	
	HDG=(f"$S{A}={latex(SA)}$.\n\n"
		f"Thể tích của khối chóp đã cho bằng:\n\n"
		f" $V=\\dfrac{{1}}{{3}}.S_{{{A}{B}{C}{D}}}.S{A}=\\dfrac{{1}}{{3}}.{AB}.{AD}.{latex(SA)}={latex(nsimplify(V))}$.")
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,3)

	if chon==1:
		d=latex(nsimplify((SA*AB)/sqrt(SA**2+AB**2)))
		d_f=latex(nsimplify((SA*AB)/(SA**2+AB**2+random.randint(1,2))))
		kq4_T=f"* Khoảng cách từ điểm ${{{D}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d}$"
		kq4_F=f" Khoảng cách từ điểm ${{{D}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d_f}$"

		
		HDG=(f"Ta có: ${B}{C}\\bot S{A},{B}{C}\\bot {A}{B}$.\n\n"
			f"Kẻ ${A}H\\bot {S}{B}$, suy ra ${A}H\\bot (S{B}{C})$.\n\n"
			f"$d({D},({S}{B}{C}))=d({A},({S}{B}{C}))={A}H=\\dfrac{{{S}{A}.{A}{B}}}{{\\sqrt{{{S}{A}^2+{A}{B}^2}}}}$"
			f"$=\\dfrac{{{latex(SA)}.{AB}}}{{\\sqrt{{{SA**2}+{AB**2}}}}}={d}$.")
	
	if chon==2:
		d=latex(nsimplify(1/2*(SA*AB)/sqrt(SA**2+AB**2)))
		d_f=latex(nsimplify(2*(SA*AB)/sqrt(SA**2+AB**2)))
		kq4_T=f"* Khoảng cách từ điểm ${{{O}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d}$"
		kq4_F=f" Khoảng cách từ điểm ${{{O}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d_f}$"

		
		HDG=(f"Ta có: ${B}{C}\\bot S{A},{B}{C}\\bot {A}{B}$.\n\n"
			f"Kẻ ${A}H\\bot {S}{B}$, suy ra ${A}H\\bot (S{B}{C})$.\n\n"
			f"$d({O},({S}{B}{C}))=\\dfrac{{1}}{{2}}d({A},({S}{B}{C}))=\\dfrac{{1}}{{2}}{A}H=\\dfrac{{1}}{{2}}\\dfrac{{{S}{A}.{A}{B}}}{{\\sqrt{{{S}{A}^2+{A}{B}^2}}}}$"
			f"$=\\dfrac{{1}}{{2}}\\dfrac{{{latex(SA)}.{AB}}}{{\\sqrt{{{SA**2}+{AB**2}}}}}={d}$.")

	if chon==3:
		M=random.choice(["M","N","P"])
		d=latex(nsimplify((SA*AB)/sqrt(SA**2+AB**2)))
		d_f=latex(nsimplify((SA*AB)/(SA**2+AB**2+random.randint(1,2))))
		kq4_T=(f"* Gọi ${{{M}}}$ là điểm thuộc cạnh ${{{A}{D}}}$ sao cho ${A}{M}={random.randint(2,4)}{M}{D}$."
			f" Khoảng cách từ điểm ${{{M}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d}$")
		kq4_F=(f"Gọi ${{{M}}}$ là điểm thuộc cạnh ${{{A}{D}}}$ sao cho ${A}{M}={random.randint(2,4)}{M}{D}$."
			f" Khoảng cách từ điểm ${{{M}}}$ đến mặt phẳng $({S}{B}{C})$ bằng ${d_f}$")

		
		HDG=(f"Ta có: ${B}{C}\\bot S{A},{B}{C}\\bot {A}{B}$.\n\n"
			f"Kẻ ${A}H\\bot {S}{B}$, suy ra ${A}H\\bot (S{B}{C})$.\n\n"
			f"$d({M},({S}{B}{C}))=d({A},({S}{B}{C}))={A}H=\\dfrac{{{S}{A}.{A}{B}}}{{\\sqrt{{{S}{A}^2+{A}{B}^2}}}}$"
			f"$=\\dfrac{{{latex(SA)}.{AB}}}{{\\sqrt{{{SA**2}+{AB**2}}}}}={d}$.")
	
	
	kq4=random.choice([kq4_T, kq4_F])
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
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an