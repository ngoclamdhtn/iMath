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

#Trả về phép cộng với ngoặc đơn
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
    code=f"\\begin{{tikzpicture}}\n\
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
    code=f"\\begin{{tikzpicture}}[scale=0.8] \n\
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

def code_hinh_lapphuong(a,b,c,d,e,f,g,h):
    code=f"\\begin{{tikzpicture}}[scale=0.7] \n\
\\begin{{scriptsize}}\n\
\\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}};\n\
\\coordinate ({b}) at (-1,-1) node at ({b}) [left] {{${b}$}};\n\
\\coordinate ({c}) at (2,-1)  node at ({c}) [right] {{${c}$}};\n\
\\coordinate ({d}) at (3,0)   node at ({d}) [right] {{${d}$}};\n\
\\coordinate ({e}) at (0,2)   node at ({e}) [left] {{${e}$}};\n\
\\coordinate ({f}) at (-1,1) node at ({f}) [left] {{${f}$}};\n\
\\coordinate ({g}) at (2,1)  node at ({g}) [right] {{${g}$}};\n\
\\coordinate ({h}) at (3,2)   node at ({h}) [right] {{${h}$}};\n\
\\draw [dashed] ({b})--({a})--({d}) ({e})--({a});\n\
\\draw ({e})--({f})--({g})--({h})--({e}) ({f})--({b}) ({g})--({c}) ({h})--({d});\n\
\\draw ({b})--({c})--({d});\n\
\\end{{scriptsize}}\n\
\\end{{tikzpicture}}\n"
    return code

def codelatex_hinh_tu_dien(s,a,b,c):
    code=f"\\begin{{tikzpicture}}[scale=0.7]\n\
\\coordinate ({a}) at (0,0)   node at ({a}) [left] {{${a}$}};\n\
\\coordinate ({b}) at (1,-2) node at ({b}) [below] {{${b}$}};\n\
\\coordinate ({c}) at (4,0)   node at ({c}) [right] {{${c}$}};\n\
\\coordinate ({s}) at (1,3)   node at ({s}) [above] {{${s}$}};\n\
\\draw [dashed] ({a})--({c}) ; \n\
\\draw ({a})--({b}) ({b})--({c}) ({s})--({a}) ({s})--({b}) ({s})--({c});\n\
\\end{{tikzpicture}}\n"
    return code

def code_hinh_lapphuong_hetruc_gocO(A1,B1,C1,D1):
	code=f"\\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
			\\coordinate (A) at (0,0);\n\
			\\coordinate (B) at (-2,-2);\n\
			\\coordinate (D) at (5,0);\n\
			\\coordinate (C) at ($(B)+(D)-(A)$);\n\
			\\coordinate ({A1}) at ($(A)+(0,3.5)$);\n\
			\\coordinate ({B1}) at ($({A1})+(B)-(A)$);\n\
			\\coordinate ({D1}) at ($({A1})+(D)-(A)$);\n\
			\\coordinate ({C1}) at ($({B1})+({D1})-({A1})$);\n\
			\\coordinate (O) at (intersection of B--D and A--C);\n\
			\\coordinate (O') at (intersection of {B1}--{D1} and {A1}--{C1});\n\
			\\draw({A1})--({B1})--({C1})--({D1})--({A1}) (B)--(C)--(D) ({B1})--(B) ({C1})--(C) (D)--({D1})\n\
			({A1})--({C1})\n\
			({B1})--({D1});\n\
			\\draw[->] (O)--(O') ;\n\
			\\draw[->] (C)--(3.6,-2.4) ;\n\
			\\draw[->] (B)--(-3.,-2.3) ;\n\
			\\node [above] at (3.6,-2.4) {{$y$}}  ;\n\
			\\node [above] at (O') {{$z$}};\n\
			\\node [below] at	(-3,-2.3) {{$x$}};\n\
			\\draw[dashed,thin]({A1})--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D);\n\
			\\pic[draw,thin,angle radius=3mm] {{right angle = {A1}--A--D}} pic[draw,thin,angle radius=3mm] {{right angle = {A1}--A--B}} pic[draw,thin,angle radius=3mm] {{right angle = A--O--B}};\n\
			\\foreach \\i/\\g in {{{A1}/180,A/-90,B/-90,C/-90,D/-45,{B1}/120,{D1}/0,{C1}/0,O/45,O'/45}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$)node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}"
	return code
def code_hinh_lapphuong_hetruc_gocA(A1,B1,C1,D1):
	code=f"\\begin{{tikzpicture}}[line join=round, line cap=round,thick]\n\
			\\coordinate (A) at (0,0);\n\
			\\coordinate (B) at (-1,-2);\n\
			\\coordinate (D) at (5,0);\n\
			\\coordinate (C) at ($(B)+(D)-(A)$);\n\
			\\coordinate ({A1}) at ($(A)+(0,3.5)$);\n\
			\\coordinate ({B1}) at ($({A1})+(B)-(A)$);\n\
			\\coordinate ({D1}) at ($({A1})+(D)-(A)$);\n\
			\\coordinate ({C1}) at ($({B1})+({D1})-({A1})$);\n\
			\\draw({A1})--({B1})--({C1})--({D1})--({A1}) (B)--(C)--(D) ({B1})--(B) ({C1})--(C) (D)--({D1});\n\
			\\draw[->] (D)--(6,0) ;\n\
			\\draw[->] ({A1})--(0,4) ;\n\
			\\draw[->] (B)--(-1.5,-3.) ;\n\
			\\node [above] at (6,0) {{$y$}}  ;\n\
			\\node [above] at (0,4) {{$z$}};\n\
			\\node [right] at	(-1.5,-3) {{$x$}};\n\
			\\draw[dashed,thin]({A1})--(A) (A)--(B) (A)--(D);\n\
			\\pic[draw,thin,angle radius=3mm] {{right angle = {A1}--A--D}} pic[draw,thin,angle radius=3mm] {{right angle = {A1}--A--B}};\n\
			\\foreach \\i/\\g in {{{A1}/180,A/-90,B/-90,C/-90,D/-45,{B1}/120,{D1}/0,{C1}/150}}{{\\draw[fill=white](\\i) circle (1.5pt) ($(\\i)+(\\g:3mm)$) node[scale=1]{{$\\i$}};}}\n\
		\\end{{tikzpicture}}"
	return code


def show_tong(a,b):
    if b>0:
        ketqua=f"{a}+{b}"
    else:
        ketqua=f"{a}+({b})"
    return ketqua

#Trả về phép trừ với ngoặc đơn
def show_hieu(a,b):
    if b>0:
        ketqua=f"{a}-{b}"
    else:
        ketqua=f"{a}-({b})"
    return ketqua

def show_tich(a,b):
    if a>=0 and b>=0:
        ketqua=f"{a}.{b}"
    if a>0 and b<0:
        ketqua=f"{a}.({b})"
    if a<0 and b>=0:
        ketqua=f"({a}).{b}"
    if a<0 and b<0:
        ketqua=f"({a}).({b})"
    if a==0 and b<0:
        ketqua=f"{a}.({b})"
    if a==0 and b>=0:
        ketqua=f"{a}.{b}"
    
    return ketqua

#Trả về dấu của hệ số a
def tao_dau(a):
    if a==0 or a<0:
        dau=f""
    else:
        dau=f"+"
    return dau

#Trả về dấu ngoặc bao lấy hệ số a
def tao_ngoac(a):
    if a<0:
        dau=f"({a})"
    else:
        dau=f"{a}"
    return dau
#.replace("-+","-").replace("--","+").replace("+-","-")
def thay_dau_congtru(st):
	ketqua=st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("+ +","+").replace("+ -","-").replace("- -","+").replace("- +","-")
	return ketqua

#Tìm tích có hướng
def tich_co_huong(a,b):
    a1, a2, a3=a[0], a[1], a[2]
    b1, b2, b3=b[0], b[1], b[2]
    c1= a2*b3-a3*b2
    c2= -(a1*b3-a3*b1)
    c3= a1*b2-a2*b1    
    return c1,c2,c3

#Tạo hàm chứa chuỗi latex vecto
def vec(st):
	return f"\\overrightarrow{{{st}}}"

def tinh_tan(a):
    goc_rad = rad(a)       
    kq = tan(goc_rad)        
    kq = simplify(kq.rewrite(sqrt))
    return kq

def tinh_sin(a):
    goc_rad = rad(a)       
    kq = sin(goc_rad)        
    kq = simplify(kq.rewrite(sqrt))
    return kq
    
def tinh_cos(a):
    goc_rad = rad(a)       
    kq = cos(goc_rad)        
    kq = simplify(kq.rewrite(sqrt))
    return kq

def generate_random_vector():
    return [random.randint(-8, 8) for _ in range(3)]

#Tìm UCLN của ba số
def ucln_ba_so(a, b, c):
    if all([a!=0, b!=0, c!=0]):
        ucln_ab = math.gcd(a, b)
        ucln_abc = math.gcd(ucln_ab, c)
    else:
        ucln_abc = 1
    return ucln_abc

def tao_3dinh_tamgiac():
	#Tạo bậc ngẫu nhiên
	
	a = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	b = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	c = random.choice([random.randint(-3, -1), random.randint(1, 3)])   

	t_uc=ucln_ba_so(a,b,c)
	a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

	x_0,y_0,z_0 = [random.randint(-2,2) for i in range(3)]
	if x_0==y_0==z_0==0:
		x_0= random.choice([i for i in range(-2, 2) if i!=0])
		y_0= random.choice([i for i in range(-2, 2) if i!=0])

	t1=random.choice([random.randint(-3, -1), random.randint(1, 3)])
	x_1 = x_0+a*t1
	y_1 = y_0+b*t1
	z_1 = z_0+c*t1

	t2=t1+random.randint(1,2)
	x_2 = x_0+a*t2
	y_2 = y_0+b*t2
	z_2 = z_0+c*t2

	t3=random.choice([random.randint(-3, -1), random.randint(1, 3)])
	x_3 = x_0+a*(t3+random.randint(1,2))
	y_3 = y_0+b*t3
	z_3 = z_0+c*(t3-random.randint(1,2))

	x=(x_1,y_1,z_1)
	y=(x_2,y_2,z_2)
	z=(x_3,y_3,z_3)
	return x,y,z

def tao_3dinh_tamgiacvuong():
    while True:
        # Tạo ngẫu nhiên ba điểm A, B, C trong khoảng [-6, 6]
        A = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        B = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        C = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))

        # Kiểm tra các điểm không trùng nhau
        if any([A[0]==B[0],A[1]==B[1],A[2]==B[2],
        	A[0]==C[0],A[1]==C[1],A[2]==C[2],
        	B[0]==C[0],B[1]==C[1],B[2]==C[2]]):
            continue

        # Tính các vectơ
        AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
        AC = (C[0] - A[0], C[1] - A[1], C[2] - A[2])
        BC = (C[0] - B[0], C[1] - B[1], C[2] - B[2])

        # Tính tích vô hướng của các cặp vectơ
        dot_AB_AC = AB[0]*AC[0] + AB[1]*AC[1] + AB[2]*AC[2]
        dot_AB_BC = AB[0]*BC[0] + AB[1]*BC[1] + AB[2]*BC[2]
        dot_AC_BC = AC[0]*BC[0] + AC[1]*BC[1] + AC[2]*BC[2]

        # Kiểm tra tam giác vuông
        if dot_AB_AC == 0:  # Vuông tại A
            return A, B, C, "A"
        elif dot_AB_BC == 0:  # Vuông tại B
            return A, B, C, "B"
        elif dot_AC_BC == 0:  # Vuông tại C
            return A, B, C, "C"

def tao_3dinh_tamgiacvuong_2():
    while True:
        # Tạo ngẫu nhiên ba điểm A, B, C trong khoảng [-6, 6]
        A = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        B = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        C = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))

        # Kiểm tra các điểm không trùng nhau
        if any([A[0]==B[0],A[1]==B[1],A[2]==B[2],
        	A[0]==C[0],A[1]==C[1],A[2]==C[2],
        	B[0]==C[0],B[1]==C[1],B[2]==C[2]]):
            continue

        # Tính các vectơ
        AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
        AC = (C[0] - A[0], C[1] - A[1], C[2] - A[2])
        BC = (C[0] - B[0], C[1] - B[1], C[2] - B[2])

        # Tính tích vô hướng của các cặp vectơ
        dot_AB_AC = AB[0]*AC[0] + AB[1]*AC[1] + AB[2]*AC[2]
        dot_AB_BC = AB[0]*BC[0] + AB[1]*BC[1] + AB[2]*BC[2]
        dot_AC_BC = AC[0]*BC[0] + AC[1]*BC[1] + AC[2]*BC[2]

        # Kiểm tra tam giác vuông
        if dot_AB_AC == 0:  # Vuông tại A
            return A, B, C
        elif dot_AB_BC == 0:  # Vuông tại B
            return B, A, C
        elif dot_AC_BC == 0:  # Vuông tại C
            return C, A, B


#Bài 1 - Véc tơ và các phép toán trong không gian
#[D12_C2_B1_01]-M2. Cho hình hộp. Tìm vectơ bằng vectơ cho trước
def mnj_34_jkl_L12_C2_B1_01():	
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]

	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"{{ABCD.{A1}{B1}{C1}{D1}}}"

	chon=random.randint(1,13)
	if chon==1:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{AB}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{A1}{B1}}},\\overrightarrow{{DC}}, \\overrightarrow{{{D1}{C1}}}$"
		kq2=f"$\\overrightarrow{{{A1}{B1}}},\\overrightarrow{{CD}}, \\overrightarrow{{{C1}{D1}}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{CD}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BA}}, \\overrightarrow{{DC}}, \\overrightarrow{{{D1}{C1}}}$"
		
	
	if chon==2:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{A1}{B1}}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{AB}},\\overrightarrow{{DC}}, \\overrightarrow{{{D1}{C1}}}$"
		kq2=f"$\\overrightarrow{{{A1}{C1}}},\\overrightarrow{{CD}}, \\overrightarrow{{{C1}{D1}}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{CD}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BA}}, \\overrightarrow{{DC}}, \\overrightarrow{{{D1}{C1}}}$"

	if chon==3:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{C1}{D1}}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{B1}{A1}}},\\overrightarrow{{BA}}, \\overrightarrow{{CD}}$"
		kq2=f"$\\overrightarrow{{{A1}{C1}}},\\overrightarrow{{BC}}, \\overrightarrow{{{C1}{D1}}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{CD}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BA}}, \\overrightarrow{{DC}}, \\overrightarrow{{{B1}{D1}}}$"

	if chon==4:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{B1}{C1}}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{A1}{D1}}},\\overrightarrow{{AD}}, \\overrightarrow{{BC}}$"
		kq2=f"$\\overrightarrow{{{A1}{D1}}},\\overrightarrow{{DA}}, \\overrightarrow{{BC}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{AC}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BC}}, \\overrightarrow{{{C1}{B1}}}, \\overrightarrow{{{B1}{D1}}}$"

	if chon==5:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{B1}C}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{A1}D}}$"
		kq2=f"$\\overrightarrow{{{A1}{D1}}}$"
		kq3=f"$\\overrightarrow{{D{A1}}}$"
		kq4=f"$\\overrightarrow{{{D1}{A1}}}$"

	if chon==6:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{C1}B}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{D1}A}}$"
		kq2=f"$\\overrightarrow{{{A1}{D1}}}$"
		kq3=f"$\\overrightarrow{{D{A1}}}$"
		kq4=f"$\\overrightarrow{{{D1}{A1}}}$"

	if chon==7:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{C1}D}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{B1}A}}$"
		kq2=f"$\\overrightarrow{{{A1}{B1}}}$"
		kq3=f"$\\overrightarrow{{B{A1}}}$"
		kq4=f"$\\overrightarrow{{{A1}B}}$"

	if chon==8:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{B1}{D1}}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{BD}}$"
		kq2=f"$\\overrightarrow{{{D1}{B1}}}$"
		kq3=f"$\\overrightarrow{{B{A1}}}$"
		kq4=f"$\\overrightarrow{{DB}}$"

	if chon==9:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{A{B1}}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{D{C1}}}$"
		kq2=f"$\\overrightarrow{{{D1}{C1}}}$"
		kq3=f"$\\overrightarrow{{{C1}{D1}}}$"
		kq4=f"$\\overrightarrow{{DC}}$"

	if chon==10:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{B1}B}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{A1}A}},\\overrightarrow{{{C1}C}}, \\overrightarrow{{{D1}D}}$"
		kq2=f"$\\overrightarrow{{{A1}A}},\\overrightarrow{{C{C1}}}, \\overrightarrow{{D{D1}}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{AC}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BC}}, \\overrightarrow{{{C1}{B1}}}, \\overrightarrow{{{B1}{D1}}}$"

	if chon==11:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{A1}A}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{B1}B}},\\overrightarrow{{{C1}C}}, \\overrightarrow{{{D1}D}}$"
		kq2=f"$\\overrightarrow{{{A1}A}},\\overrightarrow{{C{C1}}}, \\overrightarrow{{D{D1}}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{AC}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BC}}, \\overrightarrow{{{C1}{B1}}}, \\overrightarrow{{{B1}{D1}}}$"

	if chon==12:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{D1}D}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{B1}B}},\\overrightarrow{{{C1}C}}, \\overrightarrow{{{A1}A}}$"
		kq2=f"$\\overrightarrow{{{A1}A}},\\overrightarrow{{C{C1}}}, \\overrightarrow{{D{D1}}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{AC}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BC}}, \\overrightarrow{{{C1}{B1}}}, \\overrightarrow{{{B1}{D1}}}$"

	if chon==13:
		noi_dung=f"Cho hình hộp ${ten_hop}$. Các véctơ có điểm đầu và điểm cuối là các đỉnh của hình hộp và bằng véctơ $\\overrightarrow{{{C1}C}}$ là các véctơ nào sau đây"

		kq=f"$\\overrightarrow{{{B1}B}},\\overrightarrow{{{A1}A}}, \\overrightarrow{{{D1}D}}$"
		kq2=f"$\\overrightarrow{{{A1}A}},\\overrightarrow{{C{C1}}}, \\overrightarrow{{D{D1}}}$"
		kq3=f"$\\overrightarrow{{{B1}{A1}}}, \\overrightarrow{{AC}}, \\overrightarrow{{{D1}{C1}}}$"
		kq4=f"$\\overrightarrow{{BC}}, \\overrightarrow{{{C1}{B1}}}, \\overrightarrow{{{B1}{D1}}}$"
	
	noi_dung_loigiai=f"{kq} là khẳng định đúng."
	
	
	code_hinh = codelatex_hinh_hop("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)


	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)
	
	
	debai= f"{noi_dung}\n"\
	f"{file_name}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

		
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C2_B1_02]-M2. Tìm đẳng thức đúng liên quan đến 3 điểm (phép cộng trừ)
def mnj_34_jkl_L12_C2_B1_02():
	A1=random.choice(["A", "M", "P", "F", "I"])
	B1=random.choice(["B", "N", "Q", "G", "K"])
	C1=random.choice(["C", "E", "D", "H ", "L"])	
	
	noi_dung=f"Trong không gian, cho các điểm ${{{A1}, {B1},{C1}}}$. Tìm khẳng định đúng."

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

#[D12_C2_B1_03]-M1. Nhận dạng quy tắc hình hộp
def mnj_34_jkl_L12_C2_B1_03():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"ABCD.{A1}{B1}{C1}{D1}"
	noi_dung=f"Cho hình hộp ${{{ten_hop}}}$. Tìm khẳng định đúng."

	chon=random.randint(1,6)
	if chon==1:
		kq=f"$\\overrightarrow{{{A1}A}}+\\overrightarrow{{{A1}{B1}}}+\\overrightarrow{{{A1}{D1}}}=\\overrightarrow{{{A1}C}}$"
		kq2=f"$\\overrightarrow{{{A1}A}}+\\overrightarrow{{{A1}{B1}}}+\\overrightarrow{{{A1}{D1}}}=\\overrightarrow{{C{A1}}}$"
		kq3=f"$\\overrightarrow{{{A1}A}}+\\overrightarrow{{{A1}{B1}}}+\\overrightarrow{{{A1}{D1}}}=\\overrightarrow{{{A1}{C1}}}$"
		kq4=f"$\\overrightarrow{{{A1}A}}+\\overrightarrow{{{A1}{B1}}}+\\overrightarrow{{{A1}{D1}}}=\\overrightarrow{{{C1}{A1}}}$"	

	if chon==2:
		kq=f"$\\overrightarrow{{A{A1}}}+\\overrightarrow{{AB}}+\\overrightarrow{{AD}}=\\overrightarrow{{A{C1}}}$"
		kq2=f"$\\overrightarrow{{A{A1}}}+\\overrightarrow{{AB}}+\\overrightarrow{{AD}}=\\overrightarrow{{C{A1}}}$"
		kq3=f"$\\overrightarrow{{A{A1}}}+\\overrightarrow{{AB}}+\\overrightarrow{{AD}}=\\overrightarrow{{{A1}{C1}}}$"
		kq4=f"$\\overrightarrow{{A{A1}}}+\\overrightarrow{{AB}}+\\overrightarrow{{AD}}=\\overrightarrow{{{C1}{A1}}}$"

	if chon==3:
		kq=f"$\\overrightarrow{{{B1}B}}+\\overrightarrow{{{B1}{A1}}}+\\overrightarrow{{{B1}{C1}}}=\\overrightarrow{{{B1}D}}$"
		kq2=f"$\\overrightarrow{{{B1}B}}+\\overrightarrow{{{B1}{A1}}}+\\overrightarrow{{{B1}{C1}}}=\\overrightarrow{{D{B1}}}$"
		kq3=f"$\\overrightarrow{{{B1}B}}+\\overrightarrow{{{B1}{A1}}}+\\overrightarrow{{{B1}{C1}}}=\\overrightarrow{{{B1}{D1}}}$"
		kq4=f"$\\overrightarrow{{{B1}B}}+\\overrightarrow{{{B1}{A1}}}+\\overrightarrow{{{B1}{C1}}}=\\overrightarrow{{{D1}{B1}}}$"

	if chon==4:
		kq=f"$\\overrightarrow{{B{B1}}}+\\overrightarrow{{BA}}+\\overrightarrow{{BC}}=\\overrightarrow{{B{D1}}}$"
		kq2=f"$\\overrightarrow{{B{B1}}}+\\overrightarrow{{BA}}+\\overrightarrow{{BC}}=\\overrightarrow{{{B1}D}}$"
		kq3=f"$\\overrightarrow{{B{B1}}}+\\overrightarrow{{BA}}+\\overrightarrow{{BC}}=\\overrightarrow{{{B1}{D1}}}$"
		kq4=f"$\\overrightarrow{{B{B1}}}+\\overrightarrow{{BA}}+\\overrightarrow{{BC}}=\\overrightarrow{{DB}}$"

	if chon==5:
		kq=f"$\\overrightarrow{{{C1}C}}+\\overrightarrow{{{C1}{B1}}}+\\overrightarrow{{{C1}{D1}}}=\\overrightarrow{{{C1}A}}$"
		kq2=f"$\\overrightarrow{{{C1}C}}+\\overrightarrow{{{C1}{B1}}}+\\overrightarrow{{{C1}{D1}}}=\\overrightarrow{{A{C1}}}$"
		kq3=f"$\\overrightarrow{{{C1}C}}+\\overrightarrow{{{C1}{B1}}}+\\overrightarrow{{{C1}{D1}}}=\\overrightarrow{{{C1}{A1}}}$"
		kq4=f"$\\overrightarrow{{{C1}C}}+\\overrightarrow{{{C1}{B1}}}+\\overrightarrow{{{C1}{D1}}}=\\overrightarrow{{{A1}{C1}}}$"

	if chon==6:
		kq=f"$\\overrightarrow{{{D1}D}}+\\overrightarrow{{{D1}{A1}}}+\\overrightarrow{{{D1}{C1}}}=\\overrightarrow{{{D1}B}}$"
		kq2=f"$\\overrightarrow{{{D1}D}}+\\overrightarrow{{{D1}{A1}}}+\\overrightarrow{{{D1}{C1}}}=\\overrightarrow{{{D1}{B1}}}$"
		kq3=f"$\\overrightarrow{{{D1}D}}+\\overrightarrow{{{D1}{A1}}}+\\overrightarrow{{{D1}{C1}}}=\\overrightarrow{{B{D1}}}$"
		kq4=f"$\\overrightarrow{{{D1}D}}+\\overrightarrow{{{D1}{A1}}}+\\overrightarrow{{{D1}{C1}}}=\\overrightarrow{{DB}}$"

	code_hinh = codelatex_hinh_hop("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	noi_dung_loigiai=f"{kq} là khẳng định đúng."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
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
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C2_B1_04]-M2. Cho tứ diện. Tìm khẳng định đúng về quy tắc cộng trừ.
def mnj_34_jkl_L12_C2_B1_04():
	A=["A","A_1","E","M"]
	B=["B","B_1","F","N"]
	C=["C","C_1","G", "P"]
	D=["D","D_1","H","Q"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	ten_tudien=f"{{{A}{B}{C}{D}}}"
	noi_dung=f"Cho tứ diện ${ten_tudien}$. Tìm khẳng định đúng"
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

#[D12_C2_B1_05]-M2. Cho tứ diện. Tìm khẳng định về phép toán vectơ 
def mnj_34_jkl_L12_C2_B1_05():
	A=["A","O","S","D","B","C"]
	B=["B","A","A","A","A","A"]
	C=["C","B","B","B","C","B"]
	D=["D","C","C","C","D","D"]
	i=random.randint(0,5)
	A, B, C, D = A[i], B[i], C[i], D[i]
	M=["M","H","E"]
	N=["N","I","F"]
	P=["P","K","G"]
	i=random.randint(0,2)
	M, N, P = M[i], N[i], P[i]	
	
	AB, AC, AD = f"{A}{B}", f"{A}{C}", f"{A}{D}"
	ten_tudien = f"{{{A}{B}{C}{D}}}"
	
	chon=random.randint(1,2)
	
	if chon==1:
		noi_dung=f"Cho tứ diện ${ten_tudien}$. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của các đoạn ${{{AB},{AC},{AD}}}$. Tìm khẳng định sai."
		kq=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{D}}}=2\\overrightarrow{{{M}{P}}}$"
		kq2=f"$\\overrightarrow{{{A}{D}}}+\\overrightarrow{{{C}{A}}}=2\\overrightarrow{{{N}{P}}}$"
		kq3=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{C}}}=2\\overrightarrow{{{N}{M}}}$"
		kq4=f"$\\overrightarrow{{{B}{C}}}+\\overrightarrow{{{C}{D}}}=2\\overrightarrow{{{M}{P}}}$"
		noi_dung_loigiai=f"{kq} là khẳng định sai vì $\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{A}{D}}}=2\\overrightarrow{{{P}{M}}}$."

	if chon==2:
		noi_dung=f"Cho tứ diện ${ten_tudien}$. Gọi ${{{M},{N},{P}}}$ lần lượt là trung điểm của các đoạn ${{{AB},{AC},{AD}}}$ Tìm khẳng định đúng."
		kq=f"$\\overrightarrow{{{C}{B}}}-\\overrightarrow{{{A}{C}}}=2\\overrightarrow{{{C}{M}}}$"
		kq2=f"$\\overrightarrow{{{D}{A}}}+\\overrightarrow{{{D}{C}}}=2\\overrightarrow{{{N}{D}}}$"
		kq3=f"$\\overrightarrow{{{B}{A}}}-\\overrightarrow{{{C}{B}}}=2\\overrightarrow{{{N}{B}}}$"
		kq4=f"$\\overrightarrow{{{B}{A}}}+\\overrightarrow{{{B}{D}}}=-2\\overrightarrow{{{B}{P}}}$"
		noi_dung_loigiai=f"{kq} là khẳng định đúng vì $\\overrightarrow{{{C}{B}}}-\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{C}{B}}}+\\overrightarrow{{{C}{A}}}=2\\overrightarrow{{{C}{M}}}$."
	if chon==3:
		noi_dung=f"Cho tứ diện ${ten_tudien}$. Gọi ${{G}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$. Tìm khẳng định đúng."
		kq=f"${vec(f"{AB}")}+{vec(f"{AC}")}+{vec(f"{AD}")}=3{vec(f"{A}G")}$"
		kq2=f"${vec(f"{AB}")}+{vec(f"{AC}")}+{vec(f"{AD}")}={vec("0")}$"
		kq3=f"${vec(f"G{A}")}+{vec(f"G{B}")}+{vec(f"G{C}")}={vec(f"DG")}$"
		kq4=f"${vec(f"G{A}")}+{vec(f"G{B}")}+{vec(f"G{C}")}={vec(f"GD")}$"
		noi_dung_loigiai=f"{kq} là khẳng định đúng."
	if chon==4:
		noi_dung=f"Cho tứ diện ${ten_tudien}$. Gọi ${{{M}}}$ là trung điểm của cạnh ${{{B}{C}}}$, ${{G}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$. Tìm khẳng định đúng."
		kq=f"${vec(f"G{B}")} + {vec(f"G{C}")} =- {vec(f"G{D}")}$"
		kq2=f"${vec(f"G{B}")} + {vec(f"G{C}")} ={vec(f"G{M}")}$"
		kq3=f"${vec(f"{B}{C}")} =2 {vec(f"{C}{M}")}$"
		kq4=f"${vec(f"{M}{B}")} =\\dfrac{{1}}{{2}} {vec(f"{B}{C}")}$"
		noi_dung_loigiai=f"{kq} là khẳng định đúng vì ${vec(f"G{B}")} + {vec(f"G{C}")} = 2G{M}- {vec(f"{D}G")}$."
	if chon==5:
		noi_dung=f"Cho tứ diện ${ten_tudien}$. Gọi ${{G}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$."\
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

#[D12_C2_B1_06]-M2. Cho hình lập phương. Tính độ dài vectơ.
def mnj_34_jkl_L12_C2_B1_06():
	A=["A'","A_1","E"]
	B=["B'","B_1","F"]
	C=["C'","C_1","G"]
	D=["D'","D_1","H"]

	i=random.randint(0,2)
	A, B, C, D = A[i], B[i], C[i], D[i]
	ten_hop = f"ABCD.{A}{B}{C}{D}"
	m=random.randint(1,10)
	a=sp.symbols("a")
	chon=random.randint(1,2)

	if chon==1:
		noi_dung=f"Cho hình lập phương ${{{ten_hop}}}$ có độ dài cạnh bằng ${{{latex(m*a)}}}$. Tính độ dài vectơ $\\vec{{x}}={vec(f"{A}{B}")}+{vec(f"{A}{D}")}$ theo ${{a}}$."
		noi_dung_loigiai=f"$|\\vec{{x}}|=|{vec(f"{A}{B}")}+{vec(f"{A}{D}")}|=|{vec(f"{A}{C}")}|={latex(m*a)}.\\sqrt 2={latex(m*sqrt(2)*a)}$."
		
		kq=f"${latex(m*sqrt(2)*a)}$"
		kq2=f"${latex(m*sqrt(3)*a)}$"
		kq3=f"${{{latex(m*2*a)}}}$"
		kq4=f"${{{latex(m*random.randint(3,8)*a)}}}$"
		code_hinh = codelatex_hinh_hop("A","B","C","D",A,B,C,D)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name = my_module.pdftoimage_timename(code)
	
	if chon==2:
		A1=["A'","A_1","E"]
		B1=["B'","B_1","F"]
		C1=["C'","C_1","G"]
		D1=["D'","D_1","H"]
		i=random.randint(0,2)
		A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
		ten_hop = f"ABCD.{A1}{B1}{C1}{D1}"

		code_hinh = codelatex_hinh_hop("A","B","C","D",A1,B1,C1,D1)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name = my_module.pdftoimage_timename(code)

		noi_dung=f"Cho hình lập phương ${{{ten_hop}}}$ có độ dài cạnh bằng ${{{latex(m*a)}}}$. Tính độ dài vectơ $\\vec{{x}}={vec(f"A{B1}")}+{vec(f"A{D1}")}$ theo ${{a}}$."
		noi_dung_loigiai=(f"Gọi I là trung điểm của cạnh ${{{B1}{D1}}}$.\n\n"
		f"$|\\vec{{x}}|=|{vec(f"A{B1}")}+{vec(f"A{D1}")}|=|2{vec(f"AI")}|$.\n\n"
		f"Do tam giác ${{A{B1}{D1}}}$ là tam giác đều và $A{B1}={latex(m*sqrt(2)*a)}$ nên\n\n"
		f"$|\\vec{{x}}|=|2{vec(f"AI")}|=2.{latex(m*sqrt(2)*a)}.{latex(sqrt(3)/2)}={latex(m*sqrt(6)*a)}$."
		)
		
		kq=f"${latex(m*sqrt(6)*a)}$"
		kq2=f"${latex(m*sqrt(3)*a)}$"
		kq3=f"${latex(m*sqrt(2)*a)}$"
		kq4=f"${{{latex(m*random.randint(3,8)*a)}}}$"

	if chon==3:
		A1=["A'","A_1","E"]
		B1=["B'","B_1","F"]
		C1=["C'","C_1","G"]
		D1=["D'","D_1","H"]
		i=random.randint(0,2)
		A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
		ten_hop = f"ABCD.{A1}{B1}{C1}{D1}"

		code_hinh = codelatex_hinh_hop("A","B","C","D",A1,B1,C1,D1)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name = my_module.pdftoimage_timename(code)

		noi_dung=f"Cho hình lập phương ${{{ten_hop}}}$ có độ dài cạnh bằng ${{{latex(m*a)}}}$. Tính độ dài vectơ $\\vec{{x}}={vec(f"A{A1}")}+{vec(f"A{C1}")}$ theo ${{a}}$."
		noi_dung_loigiai=(f"Gọi I là trung điểm của cạnh ${{{A1}{C1}}}$.\n\n"
		f"$|\\vec{{x}}|=|{vec(f"A{A1}")}+{vec(f"A{C1}")}|=2|{vec(f"AI")}|$.\n\n"
		f"${A1}I={latex(m*sqrt(2)/2*a)}$ nên\n\n"
		f"$AI=\\sqrt{{A{A1}^2+{A1}I^2}}=\\sqrt{{{latex(m**2*a**2)} + {latex(m*sqrt(2)/2*a)}^2}}={latex(m*sqrt(6)/2*a)}$.\n\n"
		f"Vậy $|\\vec{{x}}|=2|{vec(f"AI")}|={latex(m*sqrt(6)*a)}$."
		)
		
		kq=f"${latex(m*sqrt(6)*a)}$"
		kq2=f"${latex(m*sqrt(3)*a)}$"
		kq3=f"${latex(m*sqrt(2)*a)}$"
		kq4=f"${{{latex(m*random.randint(3,8)*a)}}}$"	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C2_B1_07]-TF-M2. Cho hình hộp chữ nhật. Xét Đ-S: phép toán về vectơ, quy tắc hình bình hành, hình hộp, độ dài vectơ
def mnj_34_jkl_L12_C2_B1_07():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"ABCD.{A1}{B1}{C1}{D1}"

	code_hinh = codelatex_hinh_hop("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	

	a=sp.symbols("a")
	AB=random.randint(1,7)
	AD=random.choice([sqrt(i) for i in range(2,10)])
	AA1=random.randint(1,7)
	

	noi_dung = f"Cho hình hộp chữ nhật ${{{ten_hop}}}$ có ${random.choice(["AB", f"{A1}{B1}"])}={latex(AB*a)}, {random.choice(["AD", f"{A1}{D1}"])}={latex(AD*a)}, A{A1}={latex(AA1*a)}$. Xét tính đúng-sai của các khẳng định sau."		
	debai_word= f"{noi_dung}\n{file_name}\n"

	chon=random.randint(1,3)
	if chon==1:
		kq1_T=f"*${vec(f"A{B1}")}+{vec(f"C{D1}")}\\ne {vec("0")}$" 
		kq1_F=f"${vec(f"A{B1}")}+{vec(f"C{D1}")}={vec("0")}$ "
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"A{B1}")}+{vec(f"C{D1}")}\\ne {vec("0")}$"

	if chon==2:
		kq1_T=f"*${vec(f"A{B1}")}+{vec(f"{C1}D")}={vec("0")}$" 
		kq1_F=f"${vec(f"A{B1}")}+{vec(f"{C1}D")}\\ne {vec("0")}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"A{B1}")}+{vec(f"{C1}D")}={vec("0")}$"

	if chon==3:
		kq1_T=f"*${vec(f"{A1}D")}+{vec(f"C{B1}")}={vec("0")}$" 
		kq1_F=f"${vec(f"{A1}D")}+{vec(f"C{B1}")}\\ne {vec("0")}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"{A1}D")}+{vec(f"C{B1}")}={vec("0")}$"	
	
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,8)
	if chon==1:
		kq2_T=f"*${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}={vec(f"{A1}{C1}")}$"
		kq2_F=f"${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}={vec(f"{C1}{A1}")}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}={vec(f"{A1}{C1}")}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	
	if chon==2:
		kq2_T=f"*${vec(f"CB")}+{vec(f"C{C1}")}={vec(f"C{B1}")}$"
		kq2_F=f"${vec(f"CB")}+{vec(f"C{C1}")}={vec(f"{B1}C")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"CB")}+{vec(f"C{C1}")}={vec(f"C{B1}")}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		kq2_T=f"*${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}+{vec(f"{A1}A")}=+{vec(f"{A1}C")}$"
		kq2_F=f"${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}+{vec(f"{A1}A")}=+{vec(f"{A1}{C1}")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}+{vec(f"{A1}A")}=+{vec(f"{A1}C")}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==4:
		kq2_T=f"*${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}+{vec(f"{A1}A")}={vec(f"{A1}C")}$"
		kq2_F=f"${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}+{vec(f"{A1}A")}={vec(f"{A1}{C1}")}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${vec(f"{A1}{B1}")}+{vec(f"{A1}{D1}")}+{vec(f"{A1}A")}={vec(f"{A1}C")}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==5:
		kq2_T=f"*$\\overrightarrow{{{B1}B}}+\\overrightarrow{{{B1}{A1}}}+\\overrightarrow{{{B1}{C1}}}=\\overrightarrow{{{B1}D}}$"
		kq2_F=f"$\\overrightarrow{{{B1}B}}+\\overrightarrow{{{B1}{A1}}}+\\overrightarrow{{{B1}{C1}}}=\\overrightarrow{{{B1}C}}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$\\overrightarrow{{{B1}B}}+\\overrightarrow{{{B1}{A1}}}+\\overrightarrow{{{B1}{C1}}}=\\overrightarrow{{{B1}D}}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==6:
		kq2_T=f"*$\\overrightarrow{{{D1}D}}+\\overrightarrow{{{D1}{A1}}}+\\overrightarrow{{{D1}{C1}}}=\\overrightarrow{{{D1}B}}$"
		kq2_F=f"$\\overrightarrow{{{D1}D}}+\\overrightarrow{{{D1}{A1}}}+\\overrightarrow{{{D1}{C1}}}=\\overrightarrow{{{D1}{B1}}}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$\\overrightarrow{{{D1}D}}+\\overrightarrow{{{D1}{A1}}}+\\overrightarrow{{{D1}{C1}}}=\\overrightarrow{{{D1}B}}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==7:
		kq2_T=f"*$\\overrightarrow{{{C1}C}}+\\overrightarrow{{{C1}{B1}}}+\\overrightarrow{{{C1}{D1}}}=\\overrightarrow{{{C1}A}}$"
		kq2_F=f"$\\overrightarrow{{{C1}C}}+\\overrightarrow{{{C1}{B1}}}+\\overrightarrow{{{C1}{D1}}}=\\overrightarrow{{A{C1}}}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$\\overrightarrow{{{C1}C}}+\\overrightarrow{{{C1}{B1}}}+\\overrightarrow{{{C1}{D1}}}=\\overrightarrow{{{C1}A}}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==8:
		kq2_T=f"*$\\overrightarrow{{A{A1}}}+\\overrightarrow{{AB}}+\\overrightarrow{{AD}}=\\overrightarrow{{A{C1}}}$"
		kq2_F=f"$\\overrightarrow{{A{A1}}}+\\overrightarrow{{AB}}+\\overrightarrow{{AD}}=\\overrightarrow{{{C1}A}}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$\\overrightarrow{{A{A1}}}+\\overrightarrow{{AB}}+\\overrightarrow{{AD}}=\\overrightarrow{{A{C1}}}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	t=sqrt(AB**2+AD**2)
	t_false=sqrt(AB**2+AD**2+1)

	kq3_T=f"*$|{vec(f"AB")}+{vec(f"AD")}|={latex(t*a)}$"
	kq3_F=f"$|{vec(f"AB")}+{vec(f"AD")}|={latex(t_false*a)}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$|{vec(f"AB")}+{vec(f"AD")}|=|{vec(f"AC")}|=\\sqrt{{({AB})^2+({latex(AD)})^2}}.a={latex(t*a)}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	
	vecto_AD=random.choice([f"{vec(f"{A1}{D1}")}", f"{vec(f"{B1}{C1}")}", f"{vec(f"BC")}"])
	vecto_AA1=random.choice([f"{vec(f"A{A1}")}", f"{vec(f"B{B1}")}",f"{vec(f"C{C1}")}", f"{vec(f"D{D1}")}"])

	t=f"{latex(sqrt(AB**2+AD**2+AA1**2)*a)}"
	t_false=f"{latex(sqrt(AB**2+AD**2)*a)}"

	kq4_T=f"*$|{vec(f"AB")}+{vecto_AD}+{vecto_AA1}|={t}$"
	kq4_F=f"$|{vec(f"AB")}+{vecto_AD}+{vecto_AA1}|={t_false}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"$|{vec(f"AB")}+{vecto_AD}+{vecto_AA1}|=|{vec(f"AB")}+{vec(f"AD")}+{vec(f"A{A1}")}|=\\sqrt{{({latex(AB)})^2+({latex(AD)})^2+({latex(AA1)})^2}}.a={t}$."
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C2_B1_08]-TF-M2. Cho tứ diện đều. Xét Đ-S: các phép toán về vectơ, tích vô hướng
def mnj_34_jkl_L12_C2_B1_08():

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

	code_hinh=codelatex_hinh_tu_dien(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	m=random.randint(1,7)
	a=sp.symbols("a")

	noi_dung = (f"Cho tứ diện đều ${{{ten_tudien}}}$ có cạnh bằng ${{{latex(m*a)}}}$. Gọi ${{{M}}}$ là trung điểm của cạnh ${{{B}{C}}}$."
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
		kq2_T=f"*${vec(f"{A}{B}")}.{vec(f"{A}{C}")}={latex(m**2*a**2*1/2)}$"
		kq2_F=f"${vec(f"{A}{B}")}.{vec(f"{A}{C}")}={random.choice([latex(-m**2*a**2*1/2),latex(m**2*a**2),0])}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{A}{B}")}.{vec(f"{A}{C}")}={A}{B}.{A}{C}.\\cos({vec(f"{A}{B}")}, {vec(f"{A}{C}")})$"
			f"$={latex(m*a)}.{latex(m*a)}.({phan_so(1/2)})={latex(m**2*a**2*1/2)}$."
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

		kq2_T=f"*${vec(f"{B}{A}")}.{vec(f"{C}{A}")}={latex(m**2*a**2*1/2)}$"
		kq2_F=f"${vec(f"{B}{A}")}.{vec(f"{C}{A}")}={random.choice([latex(-m**2*a**2*1/2),latex(m**2*a**2),0])}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{B}{A}")}.{vec(f"{C}{A}")}={B}{A}.{C}{A}.\\cos({vec(f"{B}{A}")}, {vec(f"{C}{A}")})$"
			f"$={latex(m*a)}.{latex(m*a)}.{phan_so(1/2)}={latex(m**2*a**2*1/2)}$."
			)
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq3_T=f"*${vec(f"{A}{C}")}.{vec(f"{B}{D}")}=0$" 
		kq3_F=f"${vec(f"{A}{C}")}.{vec(f"{B}{D}")}={latex(random.randint(1,4)*m*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Gọi ${{N}}$ là trung điểm của ${{{B}{D}}}$.\n\n"\
		f"${B}{D}\\bot {C}N, {B}{D}\\bot {A}N \\Rightarrow  {B}{D}\\bot ({A}{C}N) \\Rightarrow {B}{D}\\bot {A}{C}$.\n\n"\
		f"Vậy ${vec(f"{A}{C}")}.{vec(f"{B}{D}")}=0$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:

		kq2_T=f"*${vec(f"{A}{B}")}.{vec(f"{C}{A}")}={latex(-m**2*a**2*1/2)}$"
		kq2_F=f"${vec(f"{A}{B}")}.{vec(f"{C}{A}")}={random.choice([latex(m**2*a**2*1/2),latex(m**2*a**2),0])}$ "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"${vec(f"{A}{B}")}.{vec(f"{C}{A}")}={A}{B}.{C}{A}.\\cos({vec(f"{A}{B}")}, {vec(f"{C}{A}")})$"
			f"$={latex(m*a)}.{latex(m*a)}.{phan_so(-1/2)}={latex(-m**2*a**2*1/2)}$."
			)
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq3_T=f"*${vec(f"{A}{B}")}.{vec(f"{C}{D}")}=0$" 
		kq3_F=f"${vec(f"{A}{B}")}.{vec(f"{C}{D}")}={latex(random.randint(1,4)*m*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"Gọi ${{N}}$ là trung điểm của ${{{C}{D}}}$.\n\n"\
		f"${C}{D}\\bot {B}N, {C}{D}\\bot {A}N \\Rightarrow  {C}{D}\\bot ({A}{B}N) \\Rightarrow {C}{D}\\bot {A}{B}$.\n\n"\
		f"Vậy ${vec(f"{A}{B}")}.{vec(f"{C}{D}")}=0$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	
	chon=random.randint(1,2)	
	if chon==1:
		kq4_T=f"*$({vec(f"{G}{B}")},{vec(f"{C}{G}")}) = 60^\\circ$"
		kq4_F=f"$({vec(f"{G}{B}")},{vec(f"{C}{G}")}) = {random.choice([45,30,90,120])}^\\circ$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$({vec(f"{G}{B}")},{vec(f"{C}{G}")})=180^\\circ-({vec(f"{G}{B}")},{vec(f"{G}{C}")})=180^\\circ - 120^\\circ=60^\\circ$"
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon==2:
		kq4_T=f"*$({vec(f"{G}{B}")},{vec(f"{G}{C}")}) = 120^\\circ$"
		kq4_F=f"$({vec(f"{G}{B}")},{vec(f"{G}{C}")}) = {random.choice([45,30,90,60])}^\\circ$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$({vec(f"{G}{B}")},{vec(f"{G}{C}")})=\\widehat{{{B}{G}{C}}}=120^\\circ$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	
	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n\n"\
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
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C2_B1_09]-TL-M3. Cho 3 lực đôi một vuông góc. Tính tổng hợp lực.
def mnj_34_jkl_L12_C2_B1_09():
	a1=random.randint(1,10)
	a2=random.randint(1,10)
	a3=random.randint(1,10)

	noi_dung = (f"Ba lực $\\vec{{F_1}}$, $\\vec{{F_2}}$, $\\vec{{F_3}}$ cùng tác động vào một vật có phương đôi một vuông góc nhau và "
	f"có độ lớn lần lượt là ${a1}$ N, ${a2}$ N, ${a3}$ N. Tính độ lớn hợp lực của ba lực đã cho.")

	kq=f"{round(sqrt(a1**2+a2**2+a3**2),1)}"
	kq=kq.replace(".",",")
	noi_dung_loigiai=(f" Dựng các hình chữ nhật ${{OBEC}}$ và ${{OEFA}}$ thì ta có:\
				$\\overrightarrow{{OB}}+\\overrightarrow{{OC}}=\\overrightarrow{{OE}}, \\overrightarrow{{OA}}+\\overrightarrow{{OE}}=\\overrightarrow{{OF}}.$\n\n\
				Do đó $\\overrightarrow{{F_1}}+\\overrightarrow{{F_2}}+\\overrightarrow{{F_3}}=\\overrightarrow{{OA}}+\\overrightarrow{{OB}}+\\overrightarrow{{OC}}=\\overrightarrow{{OA}}+\\overrightarrow{{OE}}=\\overrightarrow{{OF}}.$\n\n\
				Vậy độ lớn hợp lực của $F_1$, $\\overrightarrow{{F_2}}$ và $\\overrightarrow{{F_3}}$ là\n\n" 
 				f" $\\left|\\overrightarrow{{F_1}}+\\overrightarrow{{F_2}}+\\overrightarrow{{F_3}}\\right|=OF$\n\n\
					$=\\sqrt{{OA^2+OE^2}}$\n\n\
					$=\\sqrt{{OA^2+OB^2+OC^2}}$\n\n\
					$=\\sqrt{{{a1}^2+{a2}^2+{a3}^2}}={latex(sqrt(a1**2+a2**2+a3**2))}\\mathrm{{\\,N}}\\approx {kq} \\mathrm{{\\,N}}$.\n\n")

	code_hinh_de=r"""\usetikzlibrary{calc,intersections,patterns,angles,quotes}
	\begin{tikzpicture}[scale=1.3, font=\footnotesize, line join=round, line cap=round]
			\foreach \x\y\t in {0/0/O,0/1/a,1.3/0/b,-1.2/-1/c}
			\coordinate (\t) at (\x,\y);
			\foreach \a\b in {O/a,O/b,O/c}
			\draw[->] (\a)--(\b);
			\path (O)--(a) node[pos=0.5,left]{$\vec{F_1}$}
			(O)--(b) node[pos=0.5,above]{$\vec{F_2}$}
			(O)--(c) node[pos=0.5,above left]{$\vec{F_3}$};
			\path 
			pic[draw,angle radius=4]{right angle=a--O--b}
			pic[draw,angle radius=4]{right angle=c--O--b}
			pic[draw,angle radius=4]{right angle=c--O--a};
	\end{tikzpicture}"""
	code = my_module.moi_truong_anh_latex(code_hinh_de)
	file_name=my_module.pdftoimage_timename(code)
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	code_hinh_loigiai=r"""\usetikzlibrary{calc,intersections,patterns,angles,quotes}
	\begin{tikzpicture}[scale=1.8, font=\footnotesize, line join=round, line cap=round]
				\foreach \x\y\t in {0/0/O,0/1/A,1.3/0/B,-0.9/-1.2/C}
				\coordinate (\t) at (\x,\y);
				\coordinate (E) at ($(B)+(C)$);
				\coordinate (F) at ($(A)+(E)$);
				\foreach \a\b in {O/A,O/B,O/C,O/F,O/E}
				\draw[->] (\a)--(\b);
				\path 
				(O)--(A) node[pos=0.5,left]{$\vec{F_1}$}
				(O)--(B) node[pos=0.5,above]{$\vec{F_2}$}
				(O)--(C) node[pos=0.5,above left]{$\vec{F_3}$};
				\path 
				pic[draw,angle radius=4]{right angle=A--O--B}
				pic[draw,angle radius=4]{right angle=C--O--B}
				pic[draw,angle radius=4]{right angle=C--O--A};
				\foreach \t\g in {A/90, B/0, C/180,E/-80,F/0,O/180}
				\draw[fill=black] (\t)circle(0.1pt) +(\g:4pt)node{$\t$};
				\draw[dashed] (C)--(E)--(B) (A)--(F)--(E);
					\end{tikzpicture}"""

	dap_an=kq		

	code = my_module.moi_truong_anh_latex(code_hinh_loigiai)
	file_name_dapan=my_module.pdftoimage_timename(code)

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai}\n{file_name_dapan}\n"
		f"Đáp án: {dap_an}\n"
		)
		
	

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh_de}\n\\end{{center}}\n"\
	f"\\shortans[oly]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\begin{{center}}\n{code_hinh_loigiai}\n\\end{{center}}\n"\
	f"\\end{{ex}}\n"
	
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C2_B1_10]-TF-M2. Cho hình chóp. Xét Đ-S: Tích vô hướng, phép toán vectơ,  độ dài.
def mnj_34_jkl_L12_C2_B1_10():

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

	code_hinh=codelatex_hinhchop_tamgiac_canhvg(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	

	AB=random.randint(1,7)
	a=random.randint(1,6)

	noi_dung = (f"Cho hình chóp ${{{A}.{B}{C}{D}}}$ có ${A}{B}\\bot ({B}{C}{D}), {A}{B}={AB}$, tam giác ${{{B}{C}{D}}}$ đều có cạnh bằng ${{{a}}}$."
	f" Gọi ${{{G}}}$ là trọng tâm của tam giác ${{{B}{C}{D}}}$, điểm ${{{M}}}$ là trung điểm của ${{{C}{D}}}$. Xét tính đúng-sai của các khẳng định sau:")
	chon=random.randint(1,3)
		
	if chon==1:
		vecto=random.choice([f"{vec(f"{B}{C}")}", f"{vec(f"{C}{D}")}", f"{vec(f"{B}{D}")}", f"{vec(f"{B}{M}")}", f"{vec(f"{B}{G}")}"])
		kq1_T=f"*${vec(f"{A}{B}")}.{vecto}=0$" 
		kq1_F=f"${vec(f"{A}{B}")}.{vecto}={random.randint(1,5)}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${vec(f"{A}{B}")}.{vecto}=0$ vì ${vec(f"{A}{B}")} \\bot ({B}{C}{D}) \\Rightarrow {vec(f"{A}{B}")} \\bot {vecto}$."
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
	HDG=f"$|{vec(f"{B}{C}")}+{vec(f"{B}{D}")}|=|2{vec(f"{A}{M}")}|=2.{latex(a*sqrt(3)/2)}={latex(a*sqrt(3))}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon==1:
		ten=random.choice([f"{vec(f"{M}{C}")}",f"{vec(f"{D}{M}")}"])
	
		kq4_T=f"*$|{vec(f"{A}{D}")}+2{ten}|={latex(sqrt(AB**2+a**2))}$"
		kq4_F=f"$|{vec(f"{A}{D}")}+2{ten}|={latex(sqrt(AB**2+a**2+random.randint(1,3)))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$|{vec(f"{A}{D}")}+2{ten}|=|{vec(f"{A}{D}")}+{vec(f"{D}{C}")}|=|{vec(f"{A}{C}")}|=\\sqrt{{{AB}^2+{a}^2}}={latex(sqrt(AB**2+a**2))}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		ten=random.choice([f"{vec(f"{C}{M}")}",f"{vec(f"{M}{D}")}"])
	
		kq4_T=f"*$|{vec(f"{A}{C}")}+2{ten}|={latex(sqrt(AB**2+a**2))}$"
		kq4_F=f"$|{vec(f"{A}{C}")}+2{ten}|={latex(sqrt(AB**2+a**2+random.randint(1,3)))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$|{vec(f"{A}{C}")}+2{ten}|=|{vec(f"{A}{C}")}+{vec(f"{C}{D}")}|=|{vec(f"{A}{D}")}|=\\sqrt{{{AB}^2+{a}^2}}={latex(sqrt(AB**2+a**2))}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		
	
	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n\n"\
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
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C2_B1_11]-M2. Cho hình chóp có đáy h.b.h. Tìm khẳng định sai về phép toán vectơ 
def mnj_34_jkl_L12_C2_B1_11():
	S=["S","S","S","S"]
	A=["M","A","B","A"]
	B=["N","B","C","B"]
	C=["P","C","D","E"]
	D=["Q","D","E","F"]
	i=random.randint(0,3)
	S,A, B, C, D =S[i], A[i], B[i], C[i], D[i]
	tam=random.choice(["O", "I"])
	noi_dung=f"Cho hình chóp ${{{S}.{A}{B}{C}{D}}}$ có ${{{A}{B}{C}{D}}}$ là hình bình hành tâm ${{{tam}}}$. Tìm mệnh đề sai trong các mệnh đề sau."
	
	kq=random.choice([f"${vec(f"{A}{B}")}+{vec(f"{C}{B}")}={vec(f"{A}{C}")}$",
		f"${vec(f"{A}{C}")}+{vec(f"{B}{C}")}={vec(f"{A}{B}")}$",
		f"${vec(f"{S}{D}")}+{vec(f"{B}{D}")}={vec(f"{S}{B}")}$",
		f"${vec(f"{S}{D}")}-{vec(f"{B}{D}")}={vec(f"{B}{S}")}$",
		f"${vec(f"{S}{A}")}-{vec(f"{A}{B}")}={vec(f"{S}{B}")}$",
		f"${vec(f"{S}{C}")}-{vec(f"{B}{C}")}={vec(f"{B}{S}")}$"
		])
	kq2=f"${vec(f"{S}{A}")}-{vec(f"{S}{B}")}={vec(f"{S}{D}")}-{vec(f"{S}{C}")}$"
	kq3=f"${vec(f"{S}{B}")}-{vec(f"{S}{C}")}={vec(f"{S}{A}")}-{vec(f"{S}{D}")}$"
	kq4=random.choice([f"${vec(f"{A}{B}")}+{vec(f"{A}{D}")}={vec(f"{A}{C}")}$",
		f"${vec(f"{A}{B}")}-{vec(f"{D}{A}")}={vec(f"{A}{C}")}$",
		f"${vec(f"{B}{A}")}+{vec(f"{B}{C}")}={vec(f"{B}{D}")}$",
		f"${vec(f"{B}{A}")}-{vec(f"{C}{B}")}={vec(f"{B}{D}")}$",
		f"${vec(f"{D}{A}")}+{vec(f"{D}{C}")}={vec(f"{D}{B}")}$",
		f"${vec(f"{D}{A}")}-{vec(f"{C}{D}")}={vec(f"{D}{B}")}$",
		f"${vec(f"{C}{D}")}+{vec(f"{C}{B}")}={vec(f"{C}{A}")}$",
		f"${vec(f"{C}{D}")}-{vec(f"{B}{C}")}={vec(f"{C}{A}")}$"])

	noi_dung_loigiai=f"{kq} là mệnh đề sai."

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

#[D12_C2_B1_12]-M2. Cho hai vectơ có độ dài và góc. Tính tích vô hướng.
def mnj_34_jkl_L12_C2_B1_12():
	goc=random.choice([30,45,60,120,135,150,180])
	
	a=random.randint(1,10)
	b=random.randint(1,10)
	ten_a=random.choice(["a","m","u"])
	ten_b=random.choice(["b","n","v"])
	vec_a=f"{vec(f"{ten_a}")}"
	vec_b=f"{vec(f"{ten_b}")}"
	noi_dung=(f"Cho hai vectơ ${vec_a}$ và ${vec_b}$ thỏa mãn $|{vec_a}|={a},|{vec_b}|={b}$ và góc giữa hai vectơ bằng ${{{goc}}}^\\circ$."
	f"Tính tích vô hướng ${vec_a}.{vec_b}$."
	)	

	kq=a*b*tinh_cos(goc)
	kq2=a*b*tinh_tan(goc)
	kq3=a*b*tinh_sin(goc)
	kq4=a*b

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"${vec_a}.{vec_b}={a}.{b}.\\cos {goc}^\\circ={{{latex(kq)}}}$."	

	pa_A= f"*${{{latex(kq)}}}$"
	pa_B= f"${{{latex(kq2)}}}$"
	pa_C= f"${{{latex(kq3)}}}$"
	pa_D= f"${{{latex(kq4)}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	kq=f"{round(kq,1)}".replace(".",",")
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=(f"Lời giải:\n {noi_dung_loigiai} \n"
	f"Đáp án: {kq}")

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\shortans[oly]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C2_B1_13]-M2. Cho hai vectơ có độ dài và tích vô hướng. Tính góc giữa hai vectơ.
def mnj_34_jkl_L12_C2_B1_13():
	lst=[30,45,60,120,135,150,180]
	goc=random.choice([30,45,60,120,135,150,180])
	
	a=random.randint(1,10)
	b=random.randint(1,10)
	ten_a=random.choice(["a","m","u"])
	ten_b=random.choice(["b","n","v"])
	vec_a=f"{vec(f"{ten_a}")}"
	vec_b=f"{vec(f"{ten_b}")}"
	tichvh=a*b*tinh_cos(goc)
	noi_dung=(f"Cho hai vectơ ${vec_a}$ và ${vec_b}$ thỏa mãn $|{vec_a}|={a},|{vec_b}|={b}$ và ${vec_a}.{vec_b}={latex(tichvh)}$."
	f" Góc giữa hai vectơ đã cho là"
	)	

	kq=goc
	kq2= random.choice([x for x in lst if x != goc])
	kq3= random.choice([x for x in lst if x != goc and x != kq2])
	kq4= random.choice([x for x in lst if x != goc and x != kq2 and x!= kq3])

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=(
		f"$\\cos ({vec_a},{vec_b})=\\dfrac{{{vec_a}.{vec_b}}}{{|{vec_a}|.|{vec_b}|}}=\\dfrac{{{latex(tichvh)}}}{{{a}.{b}}}={latex(tichvh/(a*b))}$.\n\n"
		f"Suy ra $({vec_a},{vec_b})={goc}^\\circ$."
	)
	pa_A= f"*${kq}^\\circ$"
	pa_B= f"${kq2}^\\circ$"
	pa_C= f"${kq3}^\\circ$"
	pa_D= f"${kq4}^\\circ$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=(f"Lời giải:\n {noi_dung_loigiai} \n"
	f"Đáp án: {kq}")

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\shortans[oly]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C2_B1_14]-M2. Cho hai vectơ a,b có độ dài và tích vô hướng. Tính |ma+nb|.
def mnj_34_jkl_L12_C2_B1_14():	
	
	a=random.randint(1,5)
	b=random.randint(1,5)
	tich_vh=random.choice([i for i in range(-8, 8) if i!=0])

	m=random.randint(1,5)
	n=random.choice([i for i in range(-5, 5) if i!=0])

	ten_a=random.choice(["a","m","u"])
	ten_b=random.choice(["b","n","v"])

	vec_a=f"{vec(f"{ten_a}")}"
	vec_b=f"{vec(f"{ten_b}")}"
	noi_dung=(f"Cho hai vectơ ${vec_a}$ và ${vec_b}$ thỏa mãn $|{vec_a}|={a},|{vec_b}|={b}$ và ${vec_a}.{vec_b}={tich_vh}$."
	f" Tính $|{m}{vec_a}+{n}{vec_b}|$."
	)
	noi_dung=noi_dung.replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")

	kq=sqrt((m*a)**2+2*m*n*tich_vh+(n*b)**2)
	kq2=sqrt((m*a)**2+(n*b)**2+abs(m*n*tich_vh))
	kq3=sqrt(abs(m*a+n*b))
	kq4=sqrt(a+b)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	if tich_vh>0:
		noi_dung_loigiai=(
		f"$|{m}{vec_a}+{n}{vec_b}|^2=({m}{vec_a}+{n}{vec_b})^2={m**2}{vec_a}^2+{2*m*n}{vec_a}{vec_b}+{n**2}{vec_b}$\n\n"
		f"$={m**2}.{a}^2+{2*m*n}.{tich_vh}+{n**2}.{b}^2={(m*a)**2+2*m*n*tich_vh+(n*b)**2}$.\n\n"
		f"Suy ra $|{m}{vec_a}+{n}{vec_b}|={latex(kq)}$.")
	else:
		noi_dung_loigiai=(
		f"$|{m}{vec_a}+{n}{vec_b}|^2=({m}{vec_a}+{n}{vec_b})^2={m**2}{vec_a}^2+{2*m*n}{vec_a}{vec_b}+{n**2}{vec_b}$\n\n"
		f"$={m**2}.{a}^2+{2*m*n}.({tich_vh})+{n**2}.{b}^2={(m*a)**2+2*m*n*tich_vh+(n*b)**2}$.\n\n"
		f"Suy ra $|{m}{vec_a}+{n}{vec_b}|={latex(kq)}$.")

	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("1\\overrightarrow","\\overrightarrow").replace("-1\\overrightarrow","-\\overrightarrow")

	pa_A= f"*${{{latex(kq)}}}$"
	pa_B= f"${{{latex(kq2)}}}$"
	pa_C= f"${{{latex(kq3)}}}$"
	pa_D= f"${{{latex(kq4)}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n".replace("+-","-")

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	kq=f"{round(kq,1)}".replace(".",",")
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=(f"Lời giải:\n {noi_dung_loigiai} \n"
	f"Đáp án: {kq}")

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\shortans[oly]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C2_B1_15]-TL-M3. Cho hai vectơ a,b và độ dài |ma+nb|. Tính cos(a,b)
def mnj_34_jkl_L12_C2_B1_15():
	a=random.randint(1,5)
	b=random.randint(1,5)

	cos=random.choice([1,-1,1/2,-1/2, 1/4,3/4,-1/4,-3/4])
	tich_vh=int(a*b*cos)

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

#[D12_C2_B1_16]-TL-M3. Cho hai vectơ a,b có |a|, |b|, ab. Đặt x=ma+nb, y=pa+qb. Tính cos(x,y)
def mnj_34_jkl_L12_C2_B1_16():
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

#[D12_C2_B1_17]-TF-M2. Cho hình lập phương. Xét Đ-S: hướng, phương, góc, tích vô hướng, độ dài vectơ
def mnj_34_jkl_L12_C2_B1_17():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]
	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"ABCD.{A1}{B1}{C1}{D1}"

	code_hinh = code_hinh_lapphuong("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	

	a=sp.symbols("a")
	AB=random.randint(1,7)
	AD=AB
	duong_cheo=random.choice(["AC", f"{A1}{C1}", "BD", f"{B1}{D1}", f"{B1}C", f"A{D1}"])

	noi_dung = f"Cho hình lập phương ${{{ten_hop}}}$ có ${duong_cheo}={latex(AB*a*sqrt(2))}$. Xét tính đúng-sai của các khẳng định sau."		
	debai_word= f"{noi_dung}\n{file_name}\n"

	chon=random.randint(1,4)
	if chon==1:
		vecto=random.choice([f"{vec(f"AB")}", f"{vec(f"{A1}{B1}")}", f"{vec(f"AD")}", f"{vec(f"{A1}{D1}")}", 
			f"{vec(f"{B1}{C1}")}", f"{vec(f"BC")}", f"{vec(f"CD")}", f"{vec(f"{C1}{D1}")}" ])
		huong=random.choice([f"cùng hướng", "bằng" ])
		kq1_T=f"* Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {huong} với vectơ ${vecto}$ là ${{3}}$" 
		kq1_F=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {huong} với vectơ ${vecto}$ là ${{{random.choice([1,2,4,5,6])}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {huong} với vectơ ${vecto}$ là ${{3}}$."


	if chon==2:
		vecto=random.choice([f"{vec(f"AB")}", f"{vec(f"{A1}{B1}")}", f"{vec(f"AD")}", f"{vec(f"{A1}{D1}")}", 
			f"{vec(f"{B1}{C1}")}", f"{vec(f"BC")}", f"{vec(f"CD")}", f"{vec(f"{C1}{D1}")}" ])
		huong=random.choice([f"ngược hướng"])
		kq1_T=f"* Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {huong} với vectơ ${vecto}$ là ${{4}}$" 
		kq1_F=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {huong} với vectơ ${vecto}$ là ${{{random.choice([1,2,3,5,6])}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {huong} với vectơ ${vecto}$ là ${{4}}$."


	if chon==3:
		vecto=random.choice([f"{vec(f"AB")}", f"{vec(f"{A1}{B1}")}", f"{vec(f"AD")}", f"{vec(f"{A1}{D1}")}", 
			f"{vec(f"{B1}{C1}")}", f"{vec(f"BC")}", f"{vec(f"CD")}", f"{vec(f"{C1}{D1}")}" ])
		phuong="cùng phương"
		kq1_T=f"* Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {phuong} với vectơ ${vecto}$ là ${{7}}$" 
		kq1_F=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {phuong} với vectơ ${vecto}$ là ${{{random.randint(1,6)}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {phuong} với vectơ ${vecto}$ là ${{7}}$."


	if chon==4:
		vecto=random.choice([f"{vec(f"AC")}", f"{vec(f"{A1}{C1}")}", f"{vec(f"BD")}", f"{vec(f"{B1}{D1}")}", 
			f"{vec(f"{A1}D")}", f"{vec(f"B{C1}")}", f"{vec(f"C{D1}")}", f"{vec(f"{C1}D")}" ])
		phuong="cùng phương"
		kq1_T=f"* Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {phuong} với vectơ ${vecto}$ là ${{3}}$" 
		kq1_F=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {phuong} với vectơ ${vecto}$ là ${{{random.choice([1,2,4,5,6])}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Số vectơ có điểm đầu và điểm cuối là các đỉnh của hình lập phương {phuong} với vectơ ${vecto}$ là ${{3}}$."
	
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	chon=random.randint(1,2)
	if chon==1:
		vecto_1=[f"{vec(f"{A1}D")}",  f"{vec(f"{B1}A")}", f"{vec(f"{C1}D")}", f"{vec(f"{D1}A")}", f"{vec(f"D{A1}")}"]
		vecto_2=[f"{vec(f"{A1}B")}", f"{vec(f"{B1}C")}" , f"{vec(f"{C1}B")}", f"{vec(f"{D1}C")}", f"{vec(f"D{C1}")}"]
		i=random.choice([0,4])
		vecto_1, vecto_2 = vecto_1[i], vecto_2[i]

		kq2_T=f"* Góc giữa ${vecto_1}$ và ${vecto_2}$ bằng $60^\\circ$"
		kq2_F=f"Góc giữa ${vecto_1}$ và ${vecto_2}$ bằng ${random.choice([30,45,90,120,135,150])}^\\circ$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Góc giữa ${vecto_1}$ và ${vecto_2}$ bằng $60^\\circ$"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==2:
		vecto_1=[f"{vec(f"{A1}D")}",  f"{vec(f"{B1}A")}", f"{vec(f"{C1}D")}", f"{vec(f"{D1}A")}", f"{vec(f"D{A1}")}"]
		vecto_2=[f"{vec(f"B{A1}")}", f"{vec(f"C{B1}")}" , f"{vec(f"B{C1}")}", f"{vec(f"C{D1}")}", f"{vec(f"{C1}D")}"]
		i=random.choice([0,4])
		vecto_1, vecto_2 = vecto_1[i], vecto_2[i]

		kq2_T=f"* Góc giữa ${vecto_1}$ và ${vecto_2}$ bằng $120^\\circ$"
		kq2_F=f"Góc giữa ${vecto_1}$ và ${vecto_2}$ bằng ${random.choice([30,45,90,60,135,150])}^\\circ$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Góc giữa ${vecto_1}$ và ${vecto_2}$ bằng $120^\\circ$"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phuong an 3		
	chon=random.randint(1,4)
	if chon==1:
		vecto_1=[f"{vec(f"AC")}", f"{vec(f"B{C1}")}", f"{vec(f"{A1}B")}", f"{vec(f"{B1}{D1}")}"]
		vecto_2=[f"{vec(f"AD")}", f"{vec(f"B{B1}")}", f"{vec(f"{A1}A")}", f"{vec(f"{B1}{A1}")}"]
		i=random.randint(0,3)
		vecto_1, vecto_2=vecto_1[i], vecto_2[i]
		
		
		kq3_T=f"* ${vecto_1}.{vecto_2}={latex(AB**2*a**2)}$" 
		kq3_F=f"${vecto_1}.{vecto_2}={latex(-AB**2*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=(f"Do ${duong_cheo}={latex(AB*sqrt(2)*a)}$ nên hình lập phương có cạnh $AB={latex(AB*a)}$.\n\n"
			f"${vecto_1}.{vecto_2}={latex(AB*sqrt(2)*a)}.{latex(AB*a)}.\\cos 45^\\circ={latex(AB**2*a**2)}$."
			)
	
	if chon==2:
		vecto_1=[f"{vec(f"AC")}", f"{vec(f"B{C1}")}", f"{vec(f"{A1}B")}", f"{vec(f"{B1}{D1}")}"]
		vecto_2=[f"{vec(f"DA")}", f"{vec(f"{B1}B")}", f"{vec(f"A{A1}")}", f"{vec(f"{A1}{B1}")}"]
		i=random.randint(0,3)
		vecto_1, vecto_2=vecto_1[i], vecto_2[i]
		
		
		kq3_T=f"* ${vecto_1}.{vecto_2}={latex(-AB**2*a**2)}$" 
		kq3_F=f"${vecto_1}.{vecto_2}={latex(AB**2*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=(f"Do ${duong_cheo}={latex(AB*sqrt(2)*a)}$ nên hình lập phương có cạnh $AB={latex(AB*a)}$.\n\n"
			f"${vecto_1}.{vecto_2}={latex(AB*sqrt(2)*a)}.{latex(AB*a)}.\\cos 135^\\circ={latex(-AB**2*a**2)}$."
			)

	if chon==3:
		vecto_1=[f"{vec(f"AC")}", f"{vec(f"{B1}{D1}")}", f"{vec(f"{A1}{D1}")}", f"{vec(f"{C1}{D1}")}", f"{vec(f"{A1}{D1}")}"]
		vecto_2=[f"{vec(f"B{B1}")}", f"{vec(f"C{C1}")}", f"{vec(f"B{B1}")}", f"{vec(f"BC")}", f"{vec(f"CD")}"]
		i=random.randint(0,4)
		vecto_1, vecto_2=vecto_1[i], vecto_2[i]		
		
		kq3_T=f"* ${vecto_1}.{vecto_2}=0$" 
		kq3_F=f"${vecto_1}.{vecto_2}={latex(AB**2*a**2)}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=(f"Do ${duong_cheo}={latex(AB*sqrt(2)*a)}$ nên hình lập phương có cạnh $AB={latex(AB*a)}$.\n\n"
			f"${vecto_1}.{vecto_2}={latex(AB*sqrt(2)*a)}.{latex(AB*a)}.\\cos 90^\\circ=0$."
			)

	if chon==4:
		vecto_1=[f"{vec(f"AC")}", f"{vec(f"{B1}{D1}")}", f"{vec(f"{A1}D")}", f"{vec(f"{C1}D")}", f"{vec(f"C{D1}")}"]
		vecto_2=[f"{vec(f"A{D1}")}", f"{vec(f"{B1}C")}", f"{vec(f"{A1}B")}", f"{vec(f"{C1}B")}", f"{vec(f"C{B1}")}"]
		i=random.randint(0,4)
		vecto_1, vecto_2=vecto_1[i], vecto_2[i]
		
		kq3_T=f"* ${vecto_1}.{vecto_2}={latex(AB**2*a**2)}$" 
		kq3_F=f"${vecto_1}.{vecto_2}={latex(AB**2*a**2*sqrt(2))}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${vecto_1}.{vecto_2}={latex(AB*sqrt(2)*a)}.{latex(AB*sqrt(2)*a)}.\\cos 60^\\circ={latex(AB**2*a**2)}$."
	

	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	#Phuong an 4

	chon=random.randint(1,2)
	if chon==1:	

		kq4_T=f"*$|{vec(f"AB")}+{vec(f"AD")}|={latex(a*sqrt(2)*AB)}$"
		kq4_F=f"$|{vec(f"AB")}+{vec(f"AD")}|={latex(a*sqrt(2+random.randint(1,3))*AB)}$"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Do ${duong_cheo}={latex(AB*sqrt(2)*a)}$ nên hình lập phương có cạnh $AB={latex(AB*a)}$.\n\n"
			f"$|{vec(f"AB")}+{vec(f"AD")}|=|{vec(f"AC")}|=\\sqrt{{({AB})^2+({latex(AD)})^2}}.a={latex(a*sqrt(2)*AB)}$."
			)
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		vecto_AD=random.choice([f"{vec(f"{A1}{D1}")}", f"{vec(f"{B1}{C1}")}", f"{vec(f"BC")}"])
		vecto_AA1=random.choice([f"{vec(f"A{A1}")}", f"{vec(f"B{B1}")}",f"{vec(f"C{C1}")}", f"{vec(f"D{D1}")}"])

		t=f"{latex(sqrt(3)*AB*a)}"
		t_false=f"{latex(sqrt(3+random.randint(1,3))*AB*a)}"

		kq4_T=f"*$|{vec(f"AB")}+{vecto_AD}+{vecto_AA1}|={t}$"
		kq4_F=f"$|{vec(f"AB")}+{vecto_AD}+{vecto_AA1}|={t_false}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(
			f"Do ${duong_cheo}={latex(AB*sqrt(2)*a)}$ nên hình lập phương có cạnh $AB={latex(AB*a)}$.\n\n"
			f"$|{vec(f"AB")}+{vecto_AD}+{vecto_AA1}|=|{vec(f"AB")}+{vec(f"AD")}+{vec(f"A{A1}")}|=\\sqrt{{{AB}^2+{AB}^2+{AB}^2}}.a={latex(sqrt(3)*AB*a)}$."
			)
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an
	
#[D12_C2_B1_18]-M2. Cho hình lập phương. Tìm góc giữa hai vectơ
def mnj_34_jkl_L12_C2_B1_18():	
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]

	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"{{ABCD.{A1}{B1}{C1}{D1}}}"

	code_hinh = code_hinh_lapphuong("A","B","C","D",A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	chon=random.randint(1,3)
	if chon==1:
		vecto_1=[vec(f"A{B1}"), vec(f"{A1}{B1}"), vec(f"{B1}{C1}"), vec(f"{C1}C")]
		vecto_2=[vec(f"A{A1}"), vec(f"AC"), vec(f"BD"), vec(f"{C1}D")]
		i=random.randint(0,3)
		vecto_1, vecto_2= vecto_1[i], vecto_2[i]

		noi_dung=f"Cho hình lập phương ${ten_hop}$. Góc giữa hai vectơ ${vecto_1}$ và ${vecto_2}$ bằng"

		kq=f"$45^\\circ$"
		kq2=random.choice([f"$60^\\circ$", f"$0^\\circ$"])
		kq3=random.choice([f"$120^\\circ$", f"$180^\\circ$", f"$90^\\circ$"])
		kq4=f"$135^\\circ$"
	
	if chon==2:
		vecto_1=[vec(f"A{B1}"), vec(f"{A1}{B1}"), vec(f"{B1}{C1}"), vec(f"{C1}C")]
		vecto_2=[vec(f"{A1}A"), vec(f"CA"), vec(f"DB"), vec(f"D{C1}")]
		i=random.randint(0,3)
		vecto_1, vecto_2= vecto_1[i], vecto_2[i]

		noi_dung=f"Cho hình lập phương ${ten_hop}$. Góc giữa hai vectơ ${vecto_1}$ và ${vecto_2}$ bằng"

		kq=f"$135^\\circ$"
		kq2=random.choice([f"$60^\\circ$", f"$0^\\circ$"])
		kq3=random.choice([f"$120^\\circ$", f"$180^\\circ$", f"$90^\\circ$"])
		kq4=f"$45^\\circ$"

	if chon==3:
		vecto_1=[vec(f"A{B1}"), vec(f"{A1}{B1}"), vec(f"{B1}{C1}"), vec(f"{C1}C")]
		vecto_2=[vec(f"{A1}{D1}"), vec(f"BC"), vec(f"AB"), vec(f"{D1}{B1}")]
		i=random.randint(0,3)
		vecto_1, vecto_2= vecto_1[i], vecto_2[i]

		noi_dung=f"Cho hình lập phương ${ten_hop}$. Góc giữa hai vectơ ${vecto_1}$ và ${vecto_2}$ bằng"

		kq=f"$90^\\circ$"
		kq2=random.choice([f"$60^\\circ$", f"$0^\\circ$"])
		kq3=random.choice([f"$120^\\circ$", f"$180^\\circ$"])
		kq4=f"$45^\\circ$"
		

	noi_dung_loigiai=f"Góc $({vecto_1}, {vecto_2})=$ {kq}."

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
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan,loigiai_traloingan,dap_an

#[D12_C2_B1_19]-M2. Cho hình tứ diện đều. Tính tích vô hướng
def mnj_34_jkl_L12_C2_B1_19():
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

	code_hinh=codelatex_hinh_tu_dien(A,B,C,D)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	m=random.randint(1,7)
	a=sp.symbols("a")	

	chon=random.randint(1,2)
	
	if chon==1:
		noi_dung = f"Cho tứ diện đều ${{{ten_tudien}}}$ có cạnh bằng ${{{latex(m*a)}}}$. Tính tích vô hướng ${vec(f"{A}{B}")}.{vec(f"{A}{C}")}$."
	
		kq=f"${latex(m**2*a**2*1/2)}$"
		kq2=f"${latex(-m**2*a**2*1/2)}$"
		kq3=f"${latex(m**2*a**2)}$"
		kq4=f"${{0}}$"
		
		noi_dung_loigiai=(f"${vec(f"{A}{B}")}.{vec(f"{A}{C}")}={A}{B}.{A}{C}.\\cos({vec(f"{A}{B}")}, {vec(f"{A}{C}")})$"
			f"$={latex(m*a)}.{latex(m*a)}.({phan_so(1/2)})={latex(m**2*a**2*1/2)}$."
			)
	
	if chon==2:
		noi_dung = f"Cho tứ diện đều ${{{ten_tudien}}}$ có cạnh bằng ${{{latex(m*a)}}}$. Tính tích vô hướng ${vec(f"{B}{C}")}.{vec(f"{A}{D}")}$."

		kq=f"*${{0}}$" 
		kq2=f"${latex(random.randint(1,4)*m*a**2)}$"
		kq3=f"${latex(random.randint(-4,-1)*m*a**2)}$"
		kq4=f"${latex(random.randint(5,7)*m*a**2)}$"
		
		noi_dung_loigiai=f"${B}{C}\\bot {A}{M}, {B}{C}\\bot {D}{M} \\Rightarrow  {B}{C}\\bot ({A}{D}{M}) \\Rightarrow {B}{C}\\bot {A}{D}$.\n\n"\
		f"Vậy ${vec(f"{B}{C}")}.{vec(f"{A}{D}")}=0$."	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n{file_name}"

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

	
#--------------------------------------------------------------->
#Bài 2 - Tọa độ vectơ 
#[D12_C2_B2_01]. Đọc tọa độ vectơ theo vectơ đơn vị i, j, k
def mnj_34_jkl_L12_C2_B2_01():	
	a = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	c = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	dau_b=my_module.tao_dau(b)
	dau_c=my_module.tao_dau(c)
	if a==b==c==0:
		a=random.randint(1,10)
	ten_vt=random.choice(["u", "v", "w", "a", "b", "c"])

	kq=f"${{ ({a}; {b}; {c}) }}$"

	kq2_1=f"${{ ({a}; 0; {c}) }}$"
	kq2_2=f"${{ (0; {a}; {c}) }}$"
	kq2_3=f"${{ ({a}; {b}; 0) }}$"
	kq2=random.choice([kq2_1,kq2_2,kq2_3])

	kq3=f"${{({-a}; {-b}; {c})}}$"
	kq4=f"${{({a}; {-b}; {-c})}}$"


	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho vectơ $\\overrightarrow{{{ten_vt}}}={a}\\overrightarrow{{i}}{dau_b}{b}\\overrightarrow{{j}}{dau_c}{c}\\overrightarrow{{k}}$."\
			 f"Tìm tọa độ vectơ ${{\\overrightarrow{{{ten_vt}}}}}$."
	
	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f" Theo định nghĩa tọa độ vectơ ta có: $\\overrightarrow{{{ten_vt}}}=({a};{b};{c})$."	
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

#[D12_C2_B2_02]. Cho vectơ u=OA. Tìm tọa độ điểm A.
def mnj_34_jkl_L12_C2_B2_02():	
	a = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	c = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	dau_b=my_module.tao_dau(b)
	dau_c=my_module.tao_dau(c)
	if a==b==c==0:
		a=random.randint(1,10)
	ten_vt=random.choice(["u", "v", "w", "a", "b", "c"])
	diem=random.choice(["A","B","C","D","M","N","P"])

	kq=f"${{ ({a}; {b}; {c}) }}$"

	kq2_1=f"${{ ({a}; 0; {c}) }}$"
	kq2_2=f"${{ (0; {a}; {c}) }}$"
	kq2_3=f"${{ ({a}; {b}; 0) }}$"
	kq2=random.choice([kq2_1,kq2_2,kq2_3])

	kq3=f"${{({-a}; {-b}; {c})}}$"
	kq4=f"${{({a}; {-b}; {-c})}}$"


	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho vectơ ${{\\overrightarrow{{{ten_vt}}}=({a};{b};{c})}}$ và điểm ${{{diem}}}$.\n"\
			  f"Biết $\\overrightarrow{{O{diem}}}=\\overrightarrow {{{ten_vt}}}$. Tìm tọa độ điểm ${{{diem}}}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f" Theo định nghĩa tọa độ vectơ ta có: ${{{diem}}}=({a};{b};{c})$."	
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

#[D12_C2_B2_03]. Cho hai điểm. Tìm tọa độ vectơ tạo bởi 2 điểm.
def mnj_34_jkl_L12_C2_B2_03():	
	a1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if a1==a2==a3==0:
		a1=random.randint(1,10)
	if a2==a3==0:
		a2=random.randint(1,10)

	b1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if b1==b2==b3==0:
		b1=random.randint(1,10)
	if b2==b3==0:
		b2=random.randint(1,10)
	diem_A=random.choice(["A","C","E","M","P"])
	diem_B=random.choice(["B","D","F","N","Q"])

	kq=f"${{ ({b1-a1}; {b2-a2}; {b3-a3}) }}$"
	kq2=f"${{ ({a1+b1}; {a2+b2}; {a3+b3}) }}$"
	kq3=f"${{ ({a1-b1}; {a2-b2}; {a3-b3}) }}$"
	kq4=f"${{ ({a1*b1}; {a2*b2}; {a3*b3}) }}$"
	

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho hai điểm ${{{diem_A}({a1};{a2};{a3})}}$ và ${{{diem_B}({b1};{b2};{b3})}}$.\n"\
			f"Tìm tọa độ vectơ ${{\\overrightarrow{{{diem_A}{diem_B}}} }}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
			
	t1,t2,t3=show_hieu(b1,a1),show_hieu(b2,a2),show_hieu(b3,a3)

	noi_dung_loigiai=f" Ta có: $\\overrightarrow{{{diem_A}{diem_B}}}=({t1};{t1};{t3})=({b1-a1}; {b2-a2}; {b3-a3})$."	
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

#[D12_C2_B2_04]. Cho vectơ u và điểm A. Tìm tọa độ điểm B sao cho vto(AB)=vto(u)
def mnj_34_jkl_L12_C2_B2_04():	
	a1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if a1==a2==a3==0:
		a1=random.randint(1,10)
	if a2==a3==0:
		a2=random.randint(1,10)

	u1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	u2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	u3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if u1==u2==u3==0:
		b1=random.randint(1,10)
	if u2==u3==0:
		u2=random.randint(1,10)
	diem_A=random.choice(["A","C","E","M","P"])
	diem_B=random.choice(["B","D","F","N","Q"])
	ten_vt=random.choice(["u", "v", "w", "a", "b", "c"])

	kq=f"${{ ({u1+a1}; {u2+a2}; {u3+a3}) }}$"
	kq2=f"${{ ({u1-a1}; {u2-a2}; {u3-a3}) }}$"
	kq3=f"${{ ({a1-u1}; {a2-u2}; {a3-u3}) }}$"
	kq4=f"${{ ({u1+a1}; {u2-a2}; {u3-a3}) }}$"
	

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho hai điểm ${{{diem_A}({a1};{a2};{a3})}}$ và vectơ ${{\\overrightarrow{{{ten_vt}}}=({u1};{u2};{u3})}}$.\n"\
			f"Tìm tọa độ điểm ${{{diem_B}}}$ biết $\\overrightarrow{{{diem_A}{diem_B}}}=\\overrightarrow{{{ten_vt}}}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f" Ta có: $\\overrightarrow{{{diem_B}}}=({a1}+{u1};{a2}+{u2};{a3}+{u3})=({u1+a1}; {u2+a2}; {u3+a3})$."	
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

#[D12_C2_B2_05]. Cho điểm A. Tìm hình chiếu của điểm A trên các hệ trục tọa độ.
def mnj_34_jkl_L12_C2_B2_05():	
	a1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if a1==a2==a3:
		a1=random.randint(1,10)
		a2=a1+random.randint(1,3)
	if a2==a3:
		a3=a2+random.randint(1,10)

	mat_phang=random.choice(["(Oxy)","(Oyz)","(Oxz)"])	
	diem_A=random.choice(["A","C","E","M","P","B","D","F","N","Q"])
	if mat_phang=="(Oxy)":
		kq=f"${{ ({a1}; {a2}; 0) }}$"
		kq2=f"${{ (0; {a2}; {a3}) }}$"
		kq3=f"${{ ( {a1}; 0;{a3}) }}$"
		kq4=f"${{ (0; 0; {a3}) }}$"
	elif mat_phang=="(Oyz)":
		kq=f"${{ (0; {a2}; {a3}) }}$"
		kq2=f"${{ ({a1}; {a2}; 0) }}$"
		kq3=f"${{ ( {a1}; 0;{a3}) }}$"
		kq4=f"${{ ({a1}; 0; 0) }}$"
	else:
		kq=f"${{ ( {a1}; 0;{a3}) }}$"
		kq2=f"${{ ({a1}; {a2}; 0) }}$"
		kq3=f"${{ (0; {a2}; {a3}) }}$"
		kq4=f"${{ (0; {a2}; 0) }}$"	

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho điểm ${{{diem_A}({a1};{a2};{a3})}}$."\
			f"Tìm tọa độ hình chiếu của điểm ${{{diem_A}}}$ trên mặt phẳng ${{{mat_phang}}}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"Hình chiếu của điểm ${{{diem_A}}}$ trên mặt phẳng ${{{mat_phang}}}$ là {kq}."	
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

#[D12_C2_B2_06]. Cho các điểm A,B,C. Tìm D sao cho ABCD là hình bình hành.
def mnj_34_jkl_L12_C2_B2_06():	
	a1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a2 = random.randint(-10, 10)
	a3 = random.randint(-10, 10)

	b1 = random.randint(-10, 10)
	b2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])

	c1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	c2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	c3 = random.randint(-10, 10)

	diem_A=random.choice(["A","E","M"])
	diem_B=random.choice(["B","F","N"])
	diem_C=random.choice(["C","G","H"])
	diem_D=random.choice(["D","I","P","K"])


	kq=f"${{ ({c1+a1-b1}; {c2+a2-b2}; {c3+a3-b3}) }}$"
	kq2=f"${{ ({a1+b1-c1}; {a2+b2-c2}; {a3+b3-c3}) }}$"
	kq3=f"${{ ({a1-b1-c1}; {a2-b2-c2}; {a3-b3-c3}) }}$"
	kq4=f"${{ ({a1+b1+c1}; {a2+b2+c2}; {a3+b3+c3}) }}$"
	

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho các điểm ${{{diem_A}({a1};{a2};{a3}), {diem_B}({b1};{b2};{b3})}}$ và ${{{diem_C}({c1};{c2};{c3})}}$ .\n"\
			f"Tìm tọa độ điểm ${{{diem_D}}}$ sao cho ${{{diem_A}{diem_B}{diem_C}{diem_D}}}$ là hình bình hành."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=thay_dau_congtru(f" ${{{diem_A}{diem_B}{diem_C}{diem_D}}}$ là hình bình hành khi ${{\\overrightarrow{{{diem_A}{diem_B}}}=\\overrightarrow{{{diem_D}{diem_C}}}}}$.\n"\
					 f"Suy ra: ${{{diem_D}=({c1}+{a1}-{b1}; {c2}+{a2}-{b2}; {c3}+{a3}-{b3})=}}$ {kq}.")
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

#[D12_C2_B2_07]-TL-M2. Cho h.hộp chữ nhật được tọa độ hóa tại A. Tìm tọa độ điểm hoặc vectơ.
def mnj_34_jkl_L12_C2_B2_07():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]

	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"{{ABCD.{A1}{B1}{C1}{D1}}}"
	code_hinh=code_hinh_lapphuong_hetruc_gocA(A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)	

	l_A1=random.randint(1,7)
	l_B=random.randint(1,7)
	l_D=random.randint(1,7)

	
	I=random.choice(["I", "K"])
	M=random.choice(["M", "P",])
	N=random.choice(["N", "Q"])

	m=random.randint(1,3)
	n=random.choice([i for i in range(-3, 3) if i!=0])
	p=random.choice([i for i in range(-3, 3) if i!=0])
	a,b,c=sp.symbols("a b c")
	
	x_A,y_A,z_A=0,0,0
	x_B,y_B,z_B=l_B,0,0
	x_C,y_C,z_C=l_B,l_D,0
	x_D,y_D,z_D=0,l_D,0
	x_A1,y_A1,z_A1=0,0,l_A1
	x_B1,y_B1,z_B1=l_B,0,l_A1
	x_C1,y_C1,z_C1=l_B,l_D,l_A1
	x_D1,y_D1,z_D1=0,l_D,l_A1

	chon=random.randint(1,5)
	chon=1

	if chon==1:
		noi_dung=(
		f"Cho hình hộp chữ nhật ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${M}(a;b;c)$ là trung điểm của ${{A{C1}}}$. Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		x_M, y_M, z_M=(x_A+x_C1)/2, (y_A+y_C1)/2, (z_A+z_C1)/2
	
	if chon==2:
		noi_dung=(
		f"Cho hình hộp ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{M}(a;b;c)}}$ là trung điểm của ${{{A1}{C1}}}$."
		f" Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười).")
		
		x_M, y_M, z_M=(x_A1+x_C1)/2, (y_A1+y_C1)/2, (z_A1+z_C1)/2
	
	if chon==3:
		noi_dung=(
		f"Cho hình hộp chữ nhật ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{M}(a;b;c)}}$ là tâm của hình bình hành ${{C{C1}{D1}D}}$."
		f" Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		x_M, y_M, z_M=(x_C1+x_D)/2, (y_C1+y_D)/2, (z_C1+z_D)/2			

	if chon==4:
		noi_dung=(
		f"Cho hình hộp chữ nhật ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{M}(a;b;c)}}$ là tâm của hình bình hành ${{C{C1}{B1}B}}$."
		f" Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		x_M, y_M, z_M=(x_C1+x_B)/2, (y_C1+y_B)/2, (z_C1+z_B)/2

	if chon==5:
		noi_dung=(
		f"Cho hình hộp chữ nhật ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{M}(a;b;c)}}$ là tâm của hình bình hành ${{AB{B1}{A1}}}$."
		f" Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		x_M, y_M, z_M=(x_A1+x_B)/2, (y_A1+y_B)/2, (z_A1+z_B)/2

	if chon==6:
		noi_dung=(
		f"Cho hình hộp chữ nhật ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{M}(a;b;c)}}$ là tâm của hình bình hành ${{AB{B1}{A1}}}$."
		f" Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		x_M, y_M, z_M=(x_A1+x_C)/2, (y_A1+y_C)/2, (z_A1+z_C)/2

	dap_an=f"{round(m*x_M+n*y_M+p*z_M,1)}".replace(".",",")

	noi_dung_loigiai=(
		f"Ta có: $A(0;0;0), B({x_B};0;0), C({x_C};{y_C};0), D(0;{y_D};0), $.\n\n"
		f" ${B1}({x_B1};{y_B1};{z_B1}), {C1}({x_C1};{y_C1};{z_C1}), {D1}({x_D1};{y_D1};{z_D1})$.\n\n"			
		f"${M}\\left({phan_so(x_M)}; {phan_so(y_M)}; {phan_so(z_M)} \\right)$.\n\n"
		f"$P={latex(m*a+n*b+p*c)}={dap_an}$.")
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"		
		f"Đáp án: {dap_an}\n")

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an

def tao_toa_do():
	x_A,y_A,z_A=[random.randint(-5,5) for i in range(3)]
	while all([x_A==0,y_A==0,z_A==0]):
		x_A,y_A,z_A=[random.randint(-5,5) for i in range(3)]
	return x_A,y_A,z_A


#[D12_C2_B2_08]-TF-M2. H.hộp chữ nhật tọa độ hóa gốc A. Xét Đ-S: tọa độ vectơ, tọa độ điểm
def mnj_34_jkl_L12_C2_B2_08():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]

	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"{{ABCD.{A1}{B1}{C1}{D1}}}"
	code_hinh=code_hinh_lapphuong_hetruc_gocA(A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)	

	l_A1=random.randint(1,7)
	l_B=random.randint(1,7)
	l_D=random.randint(1,7)

	
	I=random.choice(["I", "K"])
	M=random.choice(["M", "P",])
	N=random.choice(["N", "Q"])

	m=random.randint(1,3)
	n=random.choice([i for i in range(-3, 3) if i!=0])
	p=random.choice([i for i in range(-3, 3) if i!=0])
	a,b,c=sp.symbols("a b c")
	
	x_A,y_A,z_A=0,0,0
	x_B,y_B,z_B=l_B,0,0
	x_C,y_C,z_C=l_B,l_D,0
	x_D,y_D,z_D=0,l_D,0
	x_A1,y_A1,z_A1=0,0,l_A1
	x_B1,y_B1,z_B1=l_B,0,l_A1
	x_C1,y_C1,z_C1=l_B,l_D,l_A1
	x_D1,y_D1,z_D1=0,l_D,l_A1

	
	noi_dung=(
	f"Cho hình hộp chữ nhật ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
	f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."	
	)
	debai_word= f"{noi_dung}\n"
	chon=random.randint(1,2)
	if chon==1:
		kq1_T=f"* Tọa độ điểm ${C1}=({x_C1};{y_C1};{z_C1})$" 
		kq1_F=f"Tọa độ điểm ${C1}=({x_C1+random.randint(1,2)};{y_C1-random.randint(1,2)};{z_C1})$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${C1}=({x_C1};{y_C1};{z_C1})$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq1_T=f"* Tọa độ điểm ${B1}=({x_B1};{y_B1};{z_B1})$" 
		kq1_F=f"Tọa độ điểm ${B1}=({x_C1};{y_C1};{z_C1})$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${B1}=({x_B1};{y_B1};{z_B1})$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		kq1_T=f"* Tọa độ điểm ${D1}=({x_D1};{y_D1};{z_D1})$" 
		kq1_F=f"Tọa độ điểm ${D1}=({x_A1};{y_A1};{z_A1})$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${D1}=({x_D1};{y_D1};{z_D1})$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==4:
		kq1_T=f"* Tọa độ điểm $B=({x_B};{y_B};{z_B})$" 
		kq1_F=f"Tọa độ điểm $B=({x_D};{y_D};{z_D})$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$B=({x_B};{y_B};{z_B})$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==5:
		kq1_T=f"* Tọa độ điểm $C=({x_C};{y_C};{z_C})$" 
		kq1_F=f"Tọa độ điểm $C=({x_C};{y_C};{z_C+random.randint(1,2)})$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$C=({x_C};{y_C};{z_C})$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	

	i,j,k=f"{vec(f"i")}",f"{vec(f"j")}",f"{vec(f"k")}"

	chon=random.randint(1,3)
	if chon==1:
		kq2_T=f"* ${vec(f"{A1}{B1}")}={x_B1-x_A1}{i}+{y_B1-y_A1}{j}+{z_B1-z_A1}{k}$".replace("+-","-")
		kq2_F=f"${vec(f"{A1}{B1}")}={x_A1-x_B1}{i}+{y_A1-y_B1}{j}+{z_A1-z_B1}{k}$".replace("+-","-")
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"Ta có: $A(0;0;0), B({x_B};{y_B};{z_B})$.\n\n"		
			f"${vec(f"{A1}{B1}")}={vec(f"AB")}={x_B-x_A}{i}+{y_B-y_A}{j}+{z_B-z_A}{k}$".replace("+-","-"))
	
	if chon==2:
		kq2_T=f"* ${vec(f"{A1}{C1}")}={x_C1-x_A1}{i}+{y_C1-y_A1}{j}+{z_C1-z_A1}{k}$".replace("+-","-")
		kq2_F=f"${vec(f"{A1}{C1}")}={x_A1-x_C1}{i}+{y_A1-y_C1}{j}+{z_A1-z_C1}{k}$".replace("+-","-")
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"Ta có: $A(0;0;0), C({x_C};{y_C};{z_C})$.\n\n"		
			f"${vec(f"{A1}{C1}")}={vec(f"AC")}={x_C-x_A}{i}+{y_C-y_A}{j}+{z_C-z_A}{k}$".replace("+-","-"))

	if chon==3:
		kq2_T=f"* ${vec(f"{D1}{C1}")}={x_C1-x_D1}{i}+{y_C1-y_D1}{j}+{z_C1-z_D1}{k}$".replace("+-","-")
		kq2_F=f"${vec(f"{D1}{C1}")}={x_D1-x_C1}{i}+{y_D1-y_C1}{j}+{z_D1-z_C1}{k}$".replace("+-","-")
		kq2=random.choice([kq2_T, kq2_F])
		HDG=(f"Ta có: $A(0;0;0), B({x_B};{y_B};{z_B})$.\n\n"		
			f"${vec(f"{D1}{C1}")}={x_C1-x_D1}{i}+{y_C1-y_D1}{j}+{z_C1-z_D1}{k}$".replace("+-","-"))

	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x_D,y_D,z_D = x_C+x_A-x_B, y_C+y_A-y_B, z_C+z_A-z_B

	kq3_T=f"* Tọa độ điểm ${D1}({x_D1};{y_D1};{z_D1})$" 
	kq3_F=f" Tọa độ điểm ${D1}({x_D1+random.randint(1,2)};{y_D1+random.randint(-2,2)};{z_D1+random.randint(-2,2)})$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"Tọa độ điểm ${D1}({x_D1};{y_D1};{z_D1})$\n\n"		)
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x_I,y_I,z_I=(x_A1+x_C1)/2,(y_A1+y_C1)/2,(z_A1+z_C1)/2
	kq4_T=f"* Tọa độ tâm ${{I}}$ của hình bình hành ${A1}{B1}{C1}{D1}$ là $I\\left({phan_so(x_I)};{phan_so(y_I)};{phan_so(z_I)}\\right)$"
	kq4_F=f"Tọa độ tâm ${{I}}$ của hình bình hành ${A1}{B1}{C1}{D1}$ là $I\\left({phan_so(x_I+random.randint(1,2))};{phan_so(y_I+random.randint(-1,1))};{phan_so(z_I+random.randint(-1,1))}\\right)$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f" Tâm $I\\left({phan_so(x_I)};{phan_so(y_I)};{phan_so(z_I)}\\right)$."
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

#[D12_C2_B2_09]-TF-M2. Cho hộp chữ nhật tọa độ hóa gốc O. Xét Đ-S: tọa độ vectơ, tọa độ điểm, tọa độ tâm 
def mnj_34_jkl_L12_C2_B2_09():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]

	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]

	O=["O","I" ]
	O1=["O'","I'" ]
	i=random.randint(0,1)
	O, O1, = O[i], O1[i]
	ten_hop = f"{{ABCD.{A1}{B1}{C1}{D1}}}"
	code_hinh=code_hinh_lapphuong_hetruc_gocO(A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)


	l_A1=random.randint(1,7)
	l_B=l_A1
	l_D=l_A1
	OA,OB=sqrt(l_B**2+l_D**2)/2, sqrt(l_B**2+l_D**2)/2

	
	I=random.choice(["I", "K"])
	M=random.choice(["M", "P",])
	N=random.choice(["N", "Q"])

	x_A,y_A,z_A=0,-OA,0
	x_B,y_B,z_B=OB,0,0
	x_C,y_C,z_C=0,OA,0
	x_D,y_D,z_D=-OB,0,0
	x_A1,y_A1,z_A1=0,y_A,l_A1
	x_B1,y_B1,z_B1=x_B,0,l_A1
	x_C1,y_C1,z_C1=0,y_C,l_A1
	x_D1,y_D1,z_D1=x_D,0,l_A1

	canh=random.choice([f"AB={l_B}", f"AD={l_D}",f"A{A1}={l_A1}"])
	noi_dung=(
	f"Cho hình hộp lập phương ${ten_hop}$ có ${{{canh}}}$. Gọi ${{{O},{O1}}}$ lần lượt là tâm của ${{ABCD}}$ và ${{{A1}{B1}{C1}{D1}}}$."
	f" Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với tâm của ${{ABCD}}$,"
	f" các điểm ${{B,C,{O1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."	
	)
	debai_word= f"{noi_dung}\n"
	chon=random.randint(1,2)
	if chon==1:
		kq1_T=f"* Tọa độ điểm ${C1}=(0;{latex(y_C1)};{z_C1})$" 
		kq1_F=f"Tọa độ điểm ${C1}=(0;{latex(y_C1)};{z_C1})$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${C1}=(0;{latex(y_C1)};{z_C1})$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq1_T=f"* Tọa độ điểm ${A1}=(0;{latex(y_A1)};{z_A1})$" 
		kq1_F=f"Tọa độ điểm ${A1}=(0;{latex(-y_A1)};{z_A1})$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"${A1}=(0;{latex(y_A1)};{z_A1})$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	
	
	
	kq2_T=f"* Tọa độ điểm ${B1}=({latex(x_B1)};0;{z_B1})$" 
	kq2_F=f"Tọa độ điểm ${B1}=({latex(-x_B1)};0;{z_B1})$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=(f"$OA=OB=OC=OD=\\dfrac{{AC}}{{2}}=\\dfrac{{{l_B}^2+{l_D}^2}}{{2}}={latex(OA)}$.\n\n"
		f"${B1}=({latex(x_B1)};0;{latex(z_B1)})$.")
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	kq3_T=f"* Tọa độ điểm ${D1}=({latex(x_D1)};0;{z_D1})$" 
	kq3_F=f"Tọa độ điểm ${D1}=({latex(-x_D1)};0;{-z_D1})$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"$OA=OB=OC=OD=\\dfrac{{AC}}{{2}}=\\dfrac{{{l_B}^2+{l_D}^2}}{{2}}={latex(OA)}$.\n\n"
		f"${D1}=({latex(x_D1)};0;{z_D1})$.")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon==1:
		kq4_T=f"* Tọa độ điểm $B=({latex(x_B)};0;0)$" 
		kq4_F=f"Tọa độ điểm $B=({latex(y_B)};0;0)$"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"$OA=OB=OC=OD=\\dfrac{{AC}}{{2}}=\\dfrac{{{l_B}^2+{l_D}^2}}{{2}}={latex(OA)}$.\n\n"
			f"$B=(0;{latex(y_B)};0)$.")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq4_T=f"* Tọa độ điểm $C=(0;{latex(y_C)};0)$" 
		kq4_F=f"Tọa độ điểm $C=(0;{latex(-y_C)};0)$"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"$OA=OB=OC=OD=\\dfrac{{AC}}{{2}}=\\dfrac{{{l_B}^2+{l_D}^2}}{{2}}={latex(OA)}$.\n\n"
			f"$C=({latex(x_C)};0;0)$.")
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
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C2_B2_10]-TL-M2. Bài toán thực tế: Tìm tọa độ máy bay
def mnj_34_jkl_L12_C2_B2_10():
	M=random.choice(["M","N","P"])
	H=random.choice(["H","I","K"])

	code_hinh=f" \\begin{{tikzpicture}}[line join = round, line cap=round,>=stealth,font=\\footnotesize,scale=0.75]\n\
			\\path \n\
			(0,0) coordinate (O)\n\
			(-2,-2) coordinate (A')\n\
			(4,0) coordinate (B')\n\
			(0,3) coordinate (C')\n\
			($(O)!0.3!(C')$) coordinate (C1)\n\
			($(O)!0.3!(B')$) coordinate (B1)\n\
			($(O)!0.3!(A')$) coordinate (A1)\n\
			($(O)!0.8!(C')$) coordinate (C)\n\
			($(O)!0.8!(B')$) coordinate (B)\n\
			($(O)!0.8!(A')$) coordinate (A)\n\
			;\n\
			\n\
			\\foreach \\diem/\\t/\\r in{{A'/x/-90,\n\
				B'/y/60,\n\
				C'/z/60,\n\
				A1/\\overrightarrow{{i}}/-60,\n\
				B1/\\overrightarrow{{j}}/-90,\n\
				C1/\\overrightarrow{{k}}/180}}	\n\
			\\draw[->,line width=1pt] 	(O)--(\\diem)node[shift={{(\\r:4mm)}},scale=1.2]{{$\\t$}};\n\
			\n\
			\n\
			\n\
			\\draw[dashed] \n\
			(A)--($(A)+(B)-(O)$) coordinate ({H}) --(B)\n\
			(C)--($(C)+({H})-(O)$)coordinate ({M}) node[above=0.5cm]{{${M}$}}--({H})\n\
			({H})--(O)--({M});\n\
			\n\
			\\draw ({M}) node[]{{	\n\
				\\begin{{tikzpicture}}[line join = round, line cap=round,>=stealth,font=\\footnotesize,scale=0.15,rotate=30]\n\
					%%%%%%%%%%%%%%	\n\
					\\draw[fill=black] \n\
					(0,0) .. controls +(20:1) and +(90:1) .. (8,0)\n\
					..controls +(-90:1) and +(-20:1) .. (0,0)--cycle\n\
					;\n\
					%%%%%%%%%%%%%%	\n\
					\\draw [fill=black]\n\
					(4,0)--(3,4)--(3.5,4)--(6,0)--cycle\n\
					(4,0)--(3,-4)--(3.5,-4)--(6,0)--cycle\n\
					(0.5,0)--(0,1)--(0.5,1)--(1.3,0)--cycle\n\
					(0.5,0)--(0,-1)--(0.5,-1)--(1.3,0)--cycle\n\
					;\n\
					%%%%%%%%%%%%%\n\
				\\end{{tikzpicture}}	\n\
			}};\n\
			\\draw pic[draw,angle radius=4mm] {{right angle = O--A--{H}}}; \n\
			\\draw pic[draw,angle radius=4mm] {{right angle = O--B--{H}}}; \n\
			\\draw pic[draw,angle radius=4mm] {{right angle = O--C--{M}}}; \n\
			\\draw[cyan,line width=2pt,->] (O)--({M});	\n\
			\n\
			\\foreach \\p/\\r in {{A/160,B/90,C/180,{H}/-45,O/160}}\n\
			\\fill (\\p) circle (1.2pt) node[shift={{(\\r:3mm)}}]{{$\\p$}};\n\
		\\end{{tikzpicture}}" 

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""

	l_M=random.randint(40,60)
	goc_HOA=random.randint(50,70)
	goc_HOA_rad=math.radians(goc_HOA)

	goc_HOM=random.randint(40,60)
	goc_HOM_rad=math.radians(goc_HOM)

	noi_dung = (f"Ở một sân bay, vị trí của máy bay được xác định bởi điểm ${{{M}}}$ trong không gian ${{Oxyz}}$ như hình vẽ."
	f" Gọi ${{{H}}}$ là hình chiếu vuông góc của ${{{M}}}(a;b;c)$ xuống mặt phẳng $(Oxy)$.\n\n"
	f" Cho biết $O{M} = {l_M}$, $\\left({vec(f"i")},{vec(f"O{H}")}\\right) = {goc_HOA}^\\circ$,"
	f" $\\left({vec(f"O{H}")},{vec(f"O{M}")}\\right) = {goc_HOM}^\\circ$. Tính $a+b+c$ (làm tròn đến hàng phần mười).")

	OH=l_M*cos(goc_HOM_rad)
	OC=l_M*sin(goc_HOM_rad)
	OA=OH*cos(goc_HOA_rad)
	OB=OH*sin(goc_HOA_rad)

	r_OH=f"{round(OH,2):.2f}".replace(".",",")
	r_OA=f"{round(OA,2):.2f}".replace(".",",")
	r_OB=f"{round(OB,2):.2f}".replace(".",",")
	r_OC=f"{round(OC,2):.2f}".replace(".",",")

	dap_an=f"{round(OA+OB+OC,1):.1f}".replace(".",",")

	noi_dung_loigiai=(
	f"Ta có: $O{H}=O{M}\\cos {goc_HOM}^\\circ={r_OH}$\n\n"
	f"$OC=O{M}\\sin {goc_HOM}^\\circ={r_OC}$\n\n"
	f"$OA=O{H}\\cos {goc_HOA}^\\circ={r_OA}$\n\n"
	f"$OB=A{H}=O{H}\\sin {goc_HOA}^\\circ={r_OB}$\n\n"
	f"$\\Rightarrow {M}({r_OA};{r_OB};{r_OC})\\Rightarrow a+b+c={dap_an}$."
	)
	
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an





########### Bài 3: Các phép toán về vectơ ###########
#[D12_C2_B3_01]. Cho hai vectơ. Tìm tọa độ vectơ tổng.
def mnj_34_jkl_L12_C2_B3_01():	
	a1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if a1==a2==a3==0:
		a1=random.randint(1,10)
	if a2==a3==0:
		a2=random.randint(1,10)

	b1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if b1==b2==b3==0:
		b1=random.randint(1,10)
	if b2==b3==0:
		b2=random.randint(1,10)
	vto_a=random.choice(["a","c","u","m"])
	vto_b=random.choice(["b","d","v","n"])

	kq=f"${{ ({a1+b1}; {a2+b2}; {a3+b3}) }}$"
	kq2=f"${{ ({b1-a1}; {b2-a2}; {b3-a3}) }}$"
	kq3=f"${{ ({a1-b1}; {a2-b2}; {a3-b3}) }}$"
	kq4=f"${{ ({a1*b1}; {a2*b2}; {a3*b3}) }}$"
	

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho hai vectơ $\\overrightarrow{{{vto_a}}}({a1};{a2};{a3})$ và $\\overrightarrow{{{vto_b}}}({b1};{b2};{b3})$."\
			f"Tìm tọa độ vectơ ${{ \\overrightarrow{{{vto_a}}} + \\overrightarrow{{{vto_b}}} }}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=thay_dau_congtru(f" Ta có: $\\overrightarrow{{{vto_a}}} + \\overrightarrow{{{vto_b}}}=({a1}+{b1};{a2}+{b2};{a3}+{b3})=({a1+b1}; {a2+b2}; {a3+b3})$.")
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


#[D12_C2_B3_02]. Cho hai vectơ. Tìm tọa độ vectơ hiệu.
def mnj_34_jkl_L12_C2_B3_02():	
	a1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	a3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if a1==a2==a3==0:
		a1=random.randint(1,10)
	if a2==a3==0:
		a2=random.randint(1,10)

	b1 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b2 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	b3 = random.choice([random.randint(-15, -1), random.randint(1, 10)])
	if b1==b2==b3==0:
		b1=random.randint(1,10)
	if b2==b3==0:
		b2=random.randint(1,10)
	vto_a=random.choice(["a","c","u","m"])
	vto_b=random.choice(["b","d","v","n"])

	kq=f"${{ ({a1-b1}; {a2-b2}; {a3-b3}) }}$"
	kq2=f"${{ ({b1-a1}; {b2-a2}; {b3-a3}) }}$"
	kq3=f"${{ ({a1+b1}; {a2+b2}; {a3+b3}) }}$"
	kq4=f"${{ ({a1*b1}; {a2*b2}; {a3*b3}) }}$"
	

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian với hệ tọa độ ${{Oxyz}}$, cho hai vectơ $\\overrightarrow{{{vto_a}}}({a1};{a2};{a3})$ và $\\overrightarrow{{{vto_b}}}({b1};{b2};{b3})$."\
			f"Tính ${{\\overrightarrow{{{vto_a}}} - \\overrightarrow{{{vto_b}}} }}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=thay_dau_congtru(f" Ta có: $\\overrightarrow{{{vto_a}}} - \\overrightarrow{{{vto_b}}}=({a1}-{b1};{a2}-{b2};{a3}-{b3})=({a1-b1}; {a2-b2}; {a3-b3})$.")	
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

#[D12_C2_B3_03]-M1. Cho hai véctơ tính tích vô hướng.
def mnj_34_jkl_L12_C2_B3_03():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a3= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b2= random.randint(-10,10)
	b3= random.randint(-10,10)

	if b1==a1: b1=a1+random.randint(1,4)

	vt_A=random.choice(["a","u", "m", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	kq=a1*b1+a2*b2+a3*b3
	kq2=a1*b2+a2*b3+a3*b1
	if kq2==kq:
		kq2=kq+random.randint(1,5)
	kq3=(a1+a2+a3)*(b1+b2+b3)	
	kq4=a1*a2+b1*b2+a3*b3

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{vt_A}.{vt_B}= {kq}}}$"
	pa_B= f"${{{vt_A}.{vt_B}={kq2}}}$"
	pa_C= f"${{{vt_A}.{vt_B}={kq3}}}$"
	pa_D= f"${{{vt_A}.{vt_B}={kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong hệ trục tọa độ ${{Oxyz}}$, cho hai véctơ ${vt_A}({a1};{a2};{a3})$ và ${vt_B}({b1};{b2};{b3})$. Tích vô hướng ${{{vt_A}.{vt_B}}}$ bằng"

	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"${{{vt_A}.{vt_B}={show_tich(a1,b1)}+{show_tich(a2,b2)}+{show_tich(a3,b3)}={kq}}}$."
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

#[D12_C2_B3_04]. Cho hai véctơ. Tìm m để 2 vectơ vuông góc.
def mnj_34_jkl_L12_C2_B3_04():
	m=sp.symbols("m")
	a1 = random.choice([random.randint(-8, -1), random.randint(1, 8)])
	a2, a3, a4 = random.randint(-8,8), random.randint(-6,6), random.choice([random.randint(-7, -1), random.randint(1, 7)])	

	b2 = random.choice([random.randint(-8, -1), random.randint(1, 8)])
	b1, b3, b4 = random.randint(-8,8), random.randint(-6,6), random.choice([random.randint(-7, -1), random.randint(1, 7)])

	if a1*b1+a3*b2==0: a1=a1+random.randint(1,3)
	if a1==b2: b2=b2+random.randint(1,3)
	
	vt_A=random.choice(["a","u", "n", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	# Giải phương trình	
	eq1 = Eq((a1*m + a2)*b1+(b2*m+b3)*a3+a4*b4, 0)
	tap_nghiem=solve(eq1,m)
	x_0=tap_nghiem[0]

	eq2 = Eq(a1*m + a2, b2*m+b3)
	tap_nghiem=solve(eq2,m)
	x_2=tap_nghiem[0]

	eq3 = Eq(a1*m + a2*b1+ b3*a3,b2*m+ a4*b4)
	tap_nghiem=solve(eq3,m)
	x_3=tap_nghiem[0]

		
	noi_dung= f"Trong hệ trục tọa độ ${{Oxyz}}$, cho hai véctơ ${vt_A}=({latex(a1*m + a2)};{a3};{a4})$ và ${vt_B}=({b1};{latex(b2*m+b3)};{b4})$."\
		f" Tìm các giá trị của ${{{m}}}$ để vectơ ${{{vt_A}}}$ và vectơ ${{{vt_B}}}$ vuông góc."
	noi_dung_loigiai=f"${vt_A}\\bot {vt_B} \\Leftrightarrow {vt_A}.{vt_B}=0$"\
	f"$\\displaystyle \\Leftrightarrow ({latex(a1*m + a2)}).{tao_ngoac(b1)} + {tao_ngoac(a3)}({latex(b2*m + b3)}) +{show_tich(a4,b4)}=0\\Leftrightarrow m={latex(x_0)}$."


	kq=x_0
	kq2=x_2
	kq3=x_3
	kq4=x_0+random.randint(1,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*$\\displaystyle {{m={latex(kq)}}}$"
	pa_B= f"$\\displaystyle {{m={latex(kq2)}}}$"
	pa_C= f"$\\displaystyle {{m={latex(kq3)}}}$"
	pa_D= f"$\\displaystyle {{m={latex(kq4)}}}$"

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C2_B3_05]. Cho vectơ. Tính độ dài.
def mnj_34_jkl_L12_C2_B3_05():	
	a1 = random.randint(-7, 7)
	a2 = random.randint(-7, 7)
	a3 = random.randint(-8, 8)
	if a1==a2==a3==0:
		a1=random.randint(1,10)
	if a2==a3==0:
		a2=random.randint(1,10)

	vto_a=random.choice(["a","c","u","m","b","d","v","n"])

	kq=sqrt(a1**2+a2**2+a3**2)
	kq2=abs(a1+a2+a3)
	kq3=abs(a1)+abs(a2)+abs(a3)
	kq4=a1**2+a2**2+a3**2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	

	#Tạo các phương án
	pa_A= f"*${{{latex(kq)}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)	  

	noi_dung=f"Trong không gian ${{Oxyz}}$, cho vectơ $\\overrightarrow{{{vto_a}}}=({a1};{a2};{a3})$."\
			f" Độ dài vectơ $\\overrightarrow{{{vto_a}}}$ bằng."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=thay_dau_congtru(f"$|\\overrightarrow{{{vto_a}}}|=\\sqrt{{{a1**2}+{a2**2}+{a3**2}}}={latex(sqrt(a1**2+a2**2+a3**2))}$.")
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

#[D12_C2_B3_06]-M2. Cho hai véctơ tính tích có hướng.
def mnj_34_jkl_L12_C2_B3_06():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a3= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b2= random.randint(-10,10)
	b3= random.randint(-10,10)

	if b1==a1: b1=a1+random.randint(1,4)

	vt_A=random.choice(["a","u", "m", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	m=[a1, a2, a3]
	n=[b1, b2, b3]
	a, b, c = tich_co_huong(m,n)

	kq=f"({a};{b};{c})"
	if b!=0:
		kq2=f"({a};{b+random.randint(1,4)};{c-random.randint(1,5)})"
	else:
		kq2=f"({a-random.randint(1,4)};{random.randint(1,5)};{random.randint(10,20)})"
	kq3=f"({a+random.randint(1,4)};{b-random.randint(1,4)};{c+random.randint(1,4)})"
	kq4=f"({a-random.randint(1,4)};{b+random.randint(1,4)};{c-random.randint(1,4)})"


	#Tạo các phương án
	pa_A= f"*$\\left[{vt_A},{vt_B}\\right]= {kq}$"
	pa_B= f"$\\left[{vt_A},{vt_B}\\right]={kq2}$"
	pa_C= f"$\\left[{vt_A},{vt_B}\\right]={kq3}$"
	pa_D= f"$\\left[{vt_A},{vt_B}\\right]={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong hệ trục tọa độ ${{Oxyz}}$, cho hai véctơ ${vt_A}({a1};{a2};{a3})$ và ${vt_B}({b1};{b2};{b3})$."\
	f" Tọa độ tích có hướng $\\left[{vt_A},{vt_B}\\right]$ là"

	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"$\\left[{vt_A}.{vt_B}\\right]={kq}$."
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

#[D12_C2_B3_07]-M2. Cho hai véctơ a và b. Tính ma+nb
def mnj_34_jkl_L12_C2_B3_07():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a3= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b2= random.randint(-10,10)
	b3= random.randint(-10,10)

	if b1==a1: b1=a1+random.randint(1,4)

	vt_A=random.choice(["a","u", "m", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	m=random.choice([random.randint(-6, -1), random.randint(1, 6)])
	n=random.choice([random.randint(-6, -1), random.randint(2, 6)])
	noi_dung= thay_dau_congtru(f"Trong hệ trục tọa độ ${{Oxyz}}$, cho hai véctơ ${vt_A}({a1};{a2};{a3})$ và ${vt_B}({b1};{b2};{b3})$."\
	f" Tọa độ vectơ ${m}{vt_A}+{n}{vt_B}$ là")

	kq=f"({m*a1+n*b1}; {m*a2+n*b2}; {m*a3+n*b3})"
	kq2=f"({a1+b1}; {a2+b2}; {a3+b3})"
	kq3=f"({m*a1+b1}; {n*a2+b2}; {m*a3+b3})"
	kq4=f"({n*a1+b1}; {m*a2+n*b2}; {a3+n*b3})"

	noi_dung_loigiai=thay_dau_congtru(f"${m}{vt_A}+{n}{vt_B}={kq}$.")

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	

	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	
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

#[D12_C2_B3_08]-TF-M2. Cho h.b.h có A,B,C. Xét Đ-S: tọa độ vectơ, tọa độ điểm, tọa độ tâm 
def mnj_34_jkl_L12_C2_B3_08():
	A=["A","A","M","C"]
	B=["B","B","N","D"]
	C=["C","M","P","E"]
	D=["D","N","Q","F"]
	i=random.randint(0,3)
	A,B,C,D=A[i],B[i],C[i],D[i]

	x_A,y_A,z_A=tao_toa_do()
	x_B,y_B,z_B=tao_toa_do()
	x_AB,y_AB,z_AB=x_B-x_A,y_B-y_A,z_B-z_A
	k=random.randint(1,2)
	x_C,y_C,z_C=k*x_AB,(k+random.randint(1,2))*y_AB, random.randint(-5,5)

	noi_dung = (f"Trong không gian ${{Oxyz}}$, cho hình bình hành ${{{A}{B}{C}{D}}}$"
	f" với ${A}({x_A};{y_A};{z_A}), {B}({x_B};{y_B};{z_B}), {C}({x_C};{y_C};{z_C})$."
	f" Xét tính đúng-sai của các khẳng định sau. "	
	)	
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"* Tọa độ vectơ ${vec(f"{B}{C}")}=({x_C-x_B};{y_C-y_B};{z_C-z_B})$" 
	kq1_F=f"Tọa độ vectơ ${vec(f"{B}{C}")}=({x_B-x_C};{y_B-y_C};{z_B-z_C})$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"${vec(f"{B}{C}")}=({x_C-x_B};{y_C-y_B};{z_C-z_B})$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	i,j,k=f"{vec(f"i")}",f"{vec(f"j")}",f"{vec(f"k")}"

	kq2_T=f"* ${vec(f"{A}{B}")}={x_B-x_A}{i}+{y_B-y_A}{j}+{z_B-z_A}{k}$".replace("+-","-")
	kq2_F=f"${vec(f"{A}{B}")}={x_A-x_B}{i}+{y_A-y_B}{j}+{z_A-z_B}{k}$".replace("+-","-")
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"${vec(f"{A}{B}")}=({x_B-x_A};{y_B-y_A};{z_B-z_A})={x_B-x_A}{i}+{y_B-y_A}{j}+{z_B-z_A}{k}$".replace("+-","-")
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	x_D,y_D,z_D = x_C+x_A-x_B, y_C+y_A-y_B, z_C+z_A-z_B

	kq3_T=f"* Tọa độ điểm ${D}({x_D};{y_D};{z_D})$" 
	kq3_F=f" Tọa độ điểm ${D}({x_D+random.randint(1,2)};{y_D+random.randint(-2,2)};{z_D+random.randint(-2,2)})$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"Gọi ${D}(x;y;z)$.\n\n Ta có: ${vec(f"{A}{B}")}=({x_B-x_A};{y_B-y_A};{z_B-z_A})$\n\n"
		f"${vec(f"{D}{C}")}=({x_C}-x;{y_C}-y;{z_C}-z)$.\n\n"
		f"${vec(f"{A}{B}")}={vec(f"{D}{C}")}\\Rightarrow x={x_D},y={y_D},z={z_D}$."
		)
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x_I,y_I,z_I=(x_A+x_C)/2,(y_A+y_C)/2,(z_A+z_C)/2
	kq4_T=f"* Tọa độ tâm ${{I}}$ của hình bình hành ${{{A}{B}{C}{D}}}$ là $I\\left({phan_so(x_I)};{phan_so(y_I)};{phan_so(z_I)}\\right)$"
	kq4_F=f"Tọa độ tâm ${{I}}$ của hình bình hành ${{{A}{B}{C}{D}}}$ là $I\\left({phan_so(x_I+random.randint(1,2))};{phan_so(y_I+random.randint(-1,1))};{phan_so(z_I+random.randint(-1,1))}\\right)$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f" Tâm I là trung điểm của ${{{A}{C}}}$ nên có tọa độ là $I\\left({phan_so(x_I)};{phan_so(y_I)};{phan_so(z_I)}\\right)$."
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

#[D12_C2_B3_09]-M2. Cho h.hộp chữ nhật được tọa độ hóa gốc O. Tìm tọa độ điểm hoặc vectơ.
def mnj_34_jkl_L12_C2_B3_09():
	A1=["A'","A_1","E"]
	B1=["B'","B_1","F"]
	C1=["C'","C_1","G"]
	D1=["D'","D_1","H"]

	i=random.randint(0,2)
	A1, B1, C1, D1 = A1[i], B1[i], C1[i], D1[i]
	ten_hop = f"{{ABCD.{A1}{B1}{C1}{D1}}}"
	code_hinh=code_hinh_lapphuong_hetruc_gocA(A1,B1,C1,D1)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	l_A1=random.randint(1,7)
	l_B=random.randint(1,7)
	l_D=random.randint(1,7)

	
	I=random.choice(["I", "K"])
	M=random.choice(["M", "P",])
	N=random.choice(["N", "Q"])

	m=random.randint(1,3)
	n=random.choice([i for i in range(-3, 3) if i!=0])
	p=random.choice([i for i in range(-3, 3) if i!=0])
	a,b,c=sp.symbols("a b c")
	
	x_A,y_A,z_A=0,0,0
	x_B,y_B,z_B=l_B,0,0
	x_C,y_C,z_C=l_B,l_D,0
	x_D,y_D,z_D=0,l_D,0
	x_A1,y_A1,z_A1=0,0,l_A1
	x_B1,y_B1,z_B1=l_B,0,l_A1
	x_C1,y_C1,z_C1=l_B,l_D,l_A1
	x_D1,y_D1,z_D1=0,l_D,l_A1

	chon=random.randint(1,4)

	if chon==1:
		noi_dung=(
		f"Cho hình hộp ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${M}(a;b;c)$ là trung điểm của ${{A{C1}}}$. Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		dap_an=f"{round(m*l_B/2+n*l_D/2+p*z_A1/2,1)}".replace(".",",")
		noi_dung_loigiai=(

			f"Ta có: $A(0;0;0), B({l_B};0;0), D(0;{l_D};0), C({l_B};{l_D};0), {C1}({l_B};{l_D};{l_A1})$.\n\n"			
			f"Trung điểm ${{{M}}}$ của ${{A{C1}}}$ có tọa độ là:\n\n"
			f"${M}\\left({phan_so(l_B/2)}; {phan_so(l_D/2)};{latex(l_A1/2)} \\right)$.\n\n"
			f"$P={latex(m*a+n*b+p*c)}={dap_an}$."

			)
	
	if chon==2:
		noi_dung=(
		f"Cho hình hộp ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{I}}}$ là tâm của ${{ABCD}}$, ${{{M}}}$ là trung điểm của đoạn thẳng $B{B1}$."
		f" Điểm ${{{N}}}(a;b;c)$ là trung điểm của đoạn thẳng ${{{I}{M}}}$." 
		f" Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		x_I, y_I, z_I=l_B/2, l_D/2, 0
		x_M, y_M, z_M=l_B, 0, l_A1/2
		x_N, y_N, z_N=(x_I+x_M)/2, (y_I+y_M)/2, (z_I+z_M)/2

		dap_an=f"{round(m*x_N+n*y_N+p*z_N,1)}".replace(".",",")
		noi_dung_loigiai=(

			f"Ta có: $A(0;0;0), B({l_B};0;0), D(0;{l_D};0), C({l_B};{l_D};0), {B1}({l_B};0;{l_A1})$.\n\n"
			f"Tâm ${{{I}}}\\left( {phan_so(x_I)};  {phan_so(y_I)}; 0\\right)$.\n\n"

			f"Trung điểm ${{{M}}}$ của ${{B{B1}}}$ có tọa độ là:"
			f" ${M}\\left({x_M}; 0; {phan_so(z_M)} \\right)$.\n\n"

			f"Trung điểm ${{{N}}}$ của ${{{I}{M}}}$ có tọa độ là:"
			f" ${N}\\left({phan_so(x_N)}; {phan_so(y_N)}; {phan_so(z_N)} \\right)$.\n\n"
			f"$P={latex(m*a+n*b+p*c)}={dap_an}$."
			)

	if chon==3:
		noi_dung=(
		f"Cho hình hộp ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{M}}}$ là trung điểm của đoạn thẳng ${A1}{B1}$."
		f" ${{{N}}}$ là trung điểm của đoạn thẳng ${{C{D1}}}$." 
		f" Tọa độ vectơ ${vec(f"{M}{N}")}=(a;b;c)$. Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		x_M, y_M, z_M=(x_A1+x_B1)/2, (y_A1+y_B1)/2, (z_A1+z_B1)/2
		x_N, y_N, z_N=(x_C+x_D1)/2, (y_C+y_D1)/2, (z_C+z_D1)/2
		x_MN, y_MN, z_MN=x_N-x_M, y_N-y_M, z_N-z_M

		dap_an=f"{round(m*x_MN+n*y_MN+p*z_MN,1)}".replace(".",",")
		noi_dung_loigiai=(

			f"Ta có: $A(0;0;0), B({l_B};0;0), D(0;{l_D};0), C({l_B};{l_D};0),{A1}(0;0;{l_A1}), {B1}({l_B};0;{l_A1})$.\n\n"

			f"Trung điểm ${{{M}}}$ của ${{{A1}{B1}}}$ có tọa độ là:"
			f" ${M}\\left({x_M}; 0; {phan_so(z_M)} \\right)$.\n\n"

			f"Trung điểm ${{{N}}}$ của ${{C{D1}}}$ có tọa độ là:"
			f" ${N}\\left({phan_so(x_N)}; {phan_so(y_N)}; {phan_so(z_N)} \\right)$.\n\n"

			f"${vec(f"{M}{N}")}=({phan_so(x_MN)}; {phan_so(y_MN)}; {phan_so(z_MN)})$.\n\n"
			f"$P={latex(m*a+n*b+p*c)}={dap_an}$."

			)
	
	if chon==4:
		noi_dung=(
		f"Cho hình hộp ${ten_hop}$ có ${{AB={l_B}, AD={l_D}, A{A1}={l_A1}}}$. Xét hệ trục tọa độ ${{Oxyz}}$ có gốc ${{O}}$ trùng với điểm ${{A}}$, "
		f"các điểm ${{B,D,{A1}}}$ lần lượt nằm trên các tia ${{Ox, Oy, Oz}}$."
		f" Gọi ${{{M}(a;b;c)}}$ là trọng tâm của tam giác ${{{B1}{C1}{D1}}}$."
		f" Tính $P={latex(m*a+n*b+p*c)}$ (kết quả làm tròn đến hàng phần mười)."
		)
		
		x_M, y_M, z_M=(x_B1+x_C1+x_D1)/3, (y_B1+y_C1+y_D1)/3, (z_B1+z_C1+z_D1)/3
		dap_an=f"{round(m*x_M+n*y_M+p*z_M,1)}".replace(".",",")
		noi_dung_loigiai=(

			f"Ta có: $A(0;0;0), B({l_B};0;0), D(0;{l_D};0), C({l_B};{l_D};0), {B1}({l_B};0;{l_A1})$.\n\n"
			f"${C1}({x_C1};{y_C1};{z_C1}), {D1}({x_D1};{y_D1};{z_D1})$.\n\n"

			f"Trọng tâm ${{{M}}}$ của tam giác ${{{B1}{C1}{D1}}}$ có tọa độ là:"
			f" ${M}\\left({phan_so(x_M)}; {phan_so(y_M)}; {latex(z_M)} \\right)$.\n\n"
			f"$P={latex(m*a+n*b+p*c)}={dap_an}$."

			)	
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D12_C2_B3_10]-TF-M2. Cho hai vectơ. Xét Đ-S: tổng, hiệu, độ dài, cos
def mnj_34_jkl_L12_C2_B3_10():
	a1,a2,a3=[random.randint(-8, 8) for _ in range(3)]
	b1,b2,b3=[random.randint(-8, 8) for _ in range(3)]
	while a1==b1 and a2==b2:
		a1,a2,a3=[random.randint(-8, 8) for _ in range(3)]
		b1,b2,b3=[random.randint(-8, 8) for _ in range(3)]
	ten=["a","b","c","d","u","v","m","n"]
	random.shuffle(ten)
	ten_a,ten_b=ten[0:2]
	vec_a, vec_b=vec(f"{ten_a}"), vec(f"{ten_b}")


	noi_dung = f"Trong không gian ${{Oxyz}}$, cho hai vectơ ${vec_a}=({a1};{a2};{a3}),{vec_b}=({b1};{b2};{b3})$."
	f"Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	chon=random.randint(1,2)
	
	if chon==1:
		kq_false=random.choice([f"({a1+b1};{a2+b2+random.randint(1,2)};{a3+b3})",
		f"({a1+b1+random.randint(1,2)};{a2+b2};{a3+b3})",
		f"({a1+b1};{a2+b2};{a3+b3+random.randint(1,2)})",
		f"({a1+b1};{a2+b2};{a3+b3+random.randint(-2,-1)})"
		])
		
		kq1_T=f"* ${vec_a}+{vec_b}=({a1+b1};{a2+b2};{a3+b3})$" 
		kq1_F=f"${vec_a}+{vec_b}={kq_false}$"
		HDG=f"${vec_a}+{vec_b}=({a1+b1};{a2+b2};{a3+b3})$."
	
	if chon==2:	
		kq_false=random.choice([f"({a1-b1};{a2-b2+random.randint(1,2)};{a3-b3})",
		f"({a1-b1+random.randint(1,2)};{a2-b2};{a3-b3})",
		f"({a1-b1};{a2-b2};{a3-b3+random.randint(1,2)})",
		f"({a1-b1};{a2-b2};{a3-b3+random.randint(-2,-1)})"
		])
		
		kq1_T=f"* ${vec_a}-{vec_b}=({a1-b1};{a2-b2};{a3-b3})$" 
		kq1_F=f"${vec_a}-{vec_b}={kq_false}$"
		HDG=f"${vec_a}-{vec_b}=({a1-b1};{a2-b2};{a3-b3})$."
	
	kq1=random.choice([kq1_T, kq1_F])
	
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	m=random.choice([random.randint(-4,-2), random.randint(2,4)])
	n=random.choice([random.randint(-5,-1), random.randint(2,5)])

	x,y,z=m*a1+n*b1, m*a2+n*b2, m*a3+n*b3
	kq_false=random.choice([
		f"({x};{y+random.randint(1,2)};{z})",
		f"({x};{y};{z+random.randint(1,2)})",
		f"({x+random.randint(1,2)};{y};{z})"
		])

	kq2_T=f"* ${m}{vec_a}+{n}{vec_b}=({x};{y};{z})$".replace("$1","$").replace("-1\\","-\\").replace("+1","+").replace("+-","-").replace("1\\","\\")
	kq2_F=f"${m}{vec_a}+{n}{vec_b}={kq_false}$".replace("$1","$").replace("-1\\","-\\").replace("+1","+").replace("+-","-").replace("1\\","\\")
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"${m}{vec_a}+{n}{vec_b}=({x};{y};{z})$".replace("$1","$").replace("-1\\","-\\").replace("+1","+").replace("+-","-").replace("1\\","\\")
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon==1:
		kq3_T=f"* $|{vec_a}|={latex(sqrt(a1**2+a2**2+a3**2))}$" 
		kq3_F=f"$|{vec_a}|={latex(sqrt(a1**2+a2**2+a3**2+random.randint(1,3)))}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$|{vec_a}|=\\sqrt{{{a1**2}+{a2**2}+{a3**2}}}={latex(sqrt(a1**2+a2**2+a3**2))}$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq3_T=f"* $|{vec_b}|={latex(sqrt(b1**2+b2**2+b3**2))}$" 
		kq3_F=f"$|{vec_b}|={latex(sqrt(b1**2+b2**2+b3**2+random.randint(1,3)))}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$|{vec_b}|=\\sqrt{{{b1**2}+{b2**2}+{b3**2}}}={latex(sqrt(b1**2+b2**2+b3**2))}$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	ab=a1*b1+a2*b2+a3*b3
	len_a=sqrt(a1**2+a2**2+a3**2)
	len_b=sqrt(b1**2+b2**2+b3**2)
	kq=ab/(len_a*len_b)
	kq_false=ab/(random.randint(2,3)*len_a*len_b)

	kq4_T=f"* $\\cos({vec_a};{vec_b})={latex(kq)}$"
	kq4_F=f"$\\cos({vec_a};{vec_b})={latex(kq_false)}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f" $\\cos({vec_a};{vec_b})=\\dfrac{{{ab}}}{{{latex(len_a)}.{latex(len_b)}}}={latex(kq)}$."
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

#[D12_C2_B3_11]-TL-M2. Tìm vectơ x để m.vec(a)+nvec(x)=p.vec(b)
def mnj_34_jkl_L12_C2_B3_11():
	m = random.choice([i for i in range(2, 4) if i!=0])
	n = random.choice([i for i in range(-2, 2) if i!=0])
	p = random.choice([i for i in range(-3, 4) if i!=0])

	a1,a2,a3=[random.randint(-8, 8) for _ in range(3)]
	b1,b2,b3=[random.randint(-8, 8) for _ in range(3)]
	while a1==b1 and a2==b2:
		a1,a2,a3=[random.randint(-8, 8) for _ in range(3)]
		b1,b2,b3=[random.randint(-8, 8) for _ in range(3)]
	ten=["a","b","c","d","u","v","m","n"]
	random.shuffle(ten)
	ten_a,ten_b=ten[0:2]
	vec_a, vec_b, vec_x=vec(f"{ten_a}"), vec(f"{ten_b}"), vec("x")
	a,b,c=(p*b1-m*a1)/n,(p*b2-m*a2)/n, (p*b3-m*a3)/n

	if a+b+c==int(a+b+c):
		noi_dung =(f"Trong không gian ${{Oxyz}}$, cho hai vectơ ${vec_a}=({a1};{a2};{a3}),{vec_b}=({b1};{b2};{b3})$.\n"
			f" Biết vectơ ${vec_x}=(a;b;c)$ thỏa mãn ${m}{vec_a}+{n}{vec_x}={p}{vec_b}$."
			f" Tính $a+b+c$.")
		noi_dung=noi_dung.replace("$1","$").replace("+1","+").replace("+-","-").replace("-1\\","-\\").replace("1\\","\\")
		dap_an=int(a+b+c)
	else:
		noi_dung =(f"Trong không gian ${{Oxyz}}$, cho hai vectơ ${vec_a}=({a1};{a2};{a3}),{vec_b}=({b1};{b2};{b3})$.\n"
			f" Biết vectơ ${vec_x}=(a;b;c)$ thỏa mãn ${m}{vec_a}+{n}{vec_x}={p}{vec_b}$."
			f" Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười.")
		noi_dung=noi_dung.replace("$1","$").replace("+1","+").replace("+-","-").replace("-1\\","-\\").replace("1\\","\\")

		dap_an=f"{round(a+b+c,1):.1f}".replace(".",",")

	noi_dung_loigiai=(
		f"${m}{vec_a}+{n}{vec_x}={p}{vec_b}\\Rightarrow {n}{vec_x}={p}{vec_b}-{m}{vec_a}=({p*b1-m*a1};{p*b2-m*a2};{p*b3-m*a3})$.\n\n"
		f"$\\Rightarrow {vec_x}={phan_so(1/n)}({p*b1-m*a1};{p*b2-m*a2};{p*b3-m*a3})=({phan_so(a)};{phan_so(b)};{phan_so(c)})$.\n\n"
		f"$\\Rightarrow a+b+c={dap_an}$.\n\n"
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("$1","$").replace("+1","+").replace("+-","-").replace("1(","(").replace("-1\\","-\\").replace("1\\","\\")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
		)


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C2_B3_12]-M2. Cho hai điểm A,B. Tìm tọa độ C để AC nhận B làm trung điểm.
def mnj_34_jkl_L12_C2_B3_12():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a2==a1: a2=a1+random.randint(1,5)

	b1=random.randint(-10,10)
	b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	if b1==a1:
		b1=a1+random.randint(1,4)
	diem_A=random.choice(["A","M", "E", "G"])
	diem_B=random.choice(["B","N", "F", "H"])
	diem_C=random.choice(["C","P", "D", "K"])

	c1,c2,c3=2*b1-a1, 2*b2-a2,2*b3-a3

	kq=f"{diem_C}({c1};{c2};{c3})"
	kq2=f"{diem_C}({-c1};{-c2};{c3})"
	kq3=f"{diem_C}({c1+random.randint(1,5)};{c2-random.randint(1,5)};{c3-random.randint(1,2)})"
	kq4=f"{diem_C}({c1-random.randint(6,10)};{c2+random.randint(6,10)};{c3+random.randint(1,2)})"

	
	noi_dung=(f"Trong không gian ${{Oxyz}}$, cho hai điểm ${diem_A}({a1};{a2};{a3})$ và ${diem_B}({b1};{b2};{b3})$."
	f" Tìm tọa độ điểm ${{{diem_C}}}$ sao cho ${{{diem_A}}}$ và ${{{diem_C}}}$ đối xứng nhau qua ${{{diem_B}}}$.")

	noi_dung_loigiai=(f"Đoạn thẳng ${{{diem_A}{diem_C}}}$ nhận điểm {diem_B} làm trung điểm nên:\n\n"
	f" $x_{diem_C}=2x_{diem_B}-x_{diem_A}={show_tich(2,b1)}-{tao_ngoac(a1)}={c1}$.\n\n"
	f" $y_{diem_C}=2y_{diem_B}-y_{diem_A}={show_tich(2,b2)}-{tao_ngoac(a2)}={c2}$.\n\n"
	f" $z_{diem_C}=2z_{diem_B}-z_{diem_A}={show_tich(2,b3)}-{tao_ngoac(a3)}={c3}$.\n\n"
	f"Vậy ${{{diem_C}=({c1};{c2};{c3})}}$.")			


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
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n" \

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

#[D12_C2_B3_13]-TL-M2. Cho hai điểm A,B. Tìm tọa độ C để AC nhận B làm trung điểm.
def mnj_34_jkl_L12_C2_B3_13():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a2==a1: a2=a1+random.randint(1,5)

	b1=random.randint(-10,10)
	b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	if b1==a1:
		b1=a1+random.randint(1,4)
	diem_A=random.choice(["A","M", "E", "G"])
	diem_B=random.choice(["B","N", "F", "H"])
	diem_C=random.choice(["C","P", "D", "K"])

	c1,c2,c3=2*b1-a1, 2*b2-a2,2*b3-a3

	if c1+c2+c3==int(c1+c2+c3):
		dap_an=c1+c2+c3	
		noi_dung=(f"Trong không gian ${{Oxyz}}$, cho hai điểm ${diem_A}({a1};{a2};{a3})$ và ${diem_B}({b1};{b2};{b3})$."
		f" Biết điểm ${{{diem_C}}}=(a;b;c)$ thỏa mãn ${{{diem_A}}}$ và ${{{diem_C}}}$ đối xứng nhau qua ${{{diem_B}}}$."
		f" Tính $a+b+c$.")

	else:
		dap_an=f"{round(c1+c2+c3,1):.1f}".replace(".",",")
		noi_dung=(f"Trong không gian ${{Oxyz}}$, cho hai điểm ${diem_A}({a1};{a2};{a3})$ và ${diem_B}({b1};{b2};{b3})$."
		f" Biết điểm ${{{diem_C}}}(a;b;c)$ thỏa mãn ${{{diem_A}}}$ và ${{{diem_C}}}$ đối xứng nhau qua ${{{diem_B}}}$."
		f" Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười).")

	noi_dung_loigiai=(f"Đoạn thẳng ${{{diem_A}{diem_C}}}$ nhận điểm {diem_B} làm trung điểm nên:\n\n"
		f" $x_{diem_C}=2x_{diem_B}-x_{diem_A}={show_tich(2,b1)}-{tao_ngoac(a1)}={c1}$.\n\n"
		f" $y_{diem_C}=2y_{diem_B}-y_{diem_A}={show_tich(2,b2)}-{tao_ngoac(a2)}={c2}$.\n\n"
		f" $z_{diem_C}=2z_{diem_B}-z_{diem_A}={show_tich(2,b3)}-{tao_ngoac(a3)}={c3}$.\n\n"
		f"Vậy ${{{diem_C}=({c1};{c2};{c3})}}$.\n\n"
		)
		
	debai_word= f"{noi_dung}\n"
	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
		)
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C2_B3_14]-TL-M2. Cho hai véctơ. Tìm m để 2 vectơ vuông góc.
def mnj_34_jkl_L12_C2_B3_14():
	m=sp.symbols("m")
	a1 = random.choice([random.randint(-8, -1), random.randint(1, 8)])
	a2, a3, a4 = random.randint(-8,8), random.randint(-6,6), random.choice([random.randint(-7, -1), random.randint(1, 7)])	

	b2 = random.choice([random.randint(-8, -1), random.randint(1, 8)])
	b1, b3, b4 = random.randint(-8,8), random.randint(-6,6), random.choice([random.randint(-7, -1), random.randint(1, 7)])

	if a1*b1+a3*b2==0: a1=a1+random.randint(1,3)
	if a1==b2: b2=b2+random.randint(1,3)
	
	vt_A=random.choice(["a","u", "n", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	# Giải phương trình	
	eq1 = Eq((a1*m + a2)*b1+(b2*m+b3)*a3+a4*b4, 0)
	tap_nghiem=solve(eq1,m)
	x_0=tap_nghiem[0]

	if x_0==int(x_0):
		dap_an=x_0
		noi_dung=(f"Trong hệ trục tọa độ ${{Oxyz}}$, cho hai véctơ ${vt_A}=({latex(a1*m + a2)};{a3};{a4})$ và ${vt_B}=({b1};{latex(b2*m+b3)};{b4})$."
			f" Tìm giá trị của ${{{m}}}$ để vectơ ${{{vt_A}}}$ và vectơ ${{{vt_B}}}$ vuông góc.")
	else:
		dap_an=f"{round(x_0,1):.1f}".replace(".",",")
		noi_dung=(f"Trong hệ trục tọa độ ${{Oxyz}}$, cho hai véctơ ${vt_A}=({latex(a1*m + a2)};{a3};{a4})$ và ${vt_B}=({b1};{latex(b2*m+b3)};{b4})$."
			f" Tìm giá trị của ${{{m}}}$ để vectơ ${{{vt_A}}}$ và vectơ ${{{vt_B}}}$ vuông góc (kết quả làm tròn đến hàng phần mười).")


	noi_dung_loigiai=(f"${vt_A}\\bot {vt_B} \\Leftrightarrow {vt_A}.{vt_B}=0$"
	f"$\\displaystyle \\Leftrightarrow ({latex(a1*m + a2)}).{tao_ngoac(b1)} + {tao_ngoac(a3)}({latex(b2*m + b3)}) +{show_tich(a4,b4)}=0\\Leftrightarrow m={latex(x_0)}$.\n\n"
	)	


	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
		)

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C2_B3_15]-M2. Cho hai điểm A,B. Tìm tọa độ trung điểm.
def mnj_34_jkl_L12_C2_B3_15():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a2==a1: a2=a1+random.randint(1,5)

	b1=random.randint(-10,10)
	b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	if b1==a1:
		b1=a1+random.randint(1,4)
	diem_A=random.choice(["A","M", "E", "G"])
	diem_B=random.choice(["B","N", "F", "H"])
	diem_C=random.choice(["C","P", "D", "K"])

	c1,c2,c3=(a1+b1)/2, (a2+b2)/2, (a3+b3)/2

	
	noi_dung=(f"Trong không gian ${{Oxyz}}$, cho hai điểm ${diem_A}({a1};{a2};{a3})$ và ${diem_B}({b1};{b2};{b3})$."
	f" Tìm tọa độ điểm ${{{diem_C}}}$ là trung điểm của đoạn thẳng ${{{diem_A}{diem_B}}}$.")

	noi_dung_loigiai=(f"Ta có:\n\n"
	f" $x_{diem_C}=\\dfrac{{{a1}+{b1}}}{{2}}={phan_so(c1)}$.\n\n"
	f" $y_{diem_C}=\\dfrac{{{a2}+{b2}}}{{2}}={phan_so(c2)}$.\n\n"
	f" $z_{diem_C}=\\dfrac{{{a3}+{b3}}}{{2}}={phan_so(c3)}$.\n\n"
	f"Vậy ${{{diem_C}=({phan_so(c1)};{phan_so(c2)};{phan_so(c3)})}}$.")

	kq=f"{diem_C}({phan_so(c1)};{phan_so(c2)};{phan_so(c3)})"
	kq_false=[
	f"{diem_C}({phan_so(-c1)};{phan_so(-c2)};{phan_so(c3)})",
	f"{diem_C}({phan_so(c1+random.randint(1,5))};{phan_so(c2-random.randint(1,5))};{phan_so(c3-random.randint(1,2))})",
	f"{diem_C}({phan_so(c1-random.randint(6,10))};{phan_so(c2+random.randint(6,10))};{phan_so(c3+random.randint(1,2))})",
	f"{diem_C}({phan_so(c1)};{phan_so(c2+random.randint(1,5))};{phan_so(c3+random.randint(1,5))})",
	f"{diem_C}({phan_so(c1+random.randint(1,5))};{phan_so(c2)};{phan_so(c3+random.randint(1,5))})",
	f"{diem_C}({phan_so(c1)};{phan_so(c2)};{phan_so(c3+random.randint(1,5))})",
	f"{diem_C}({phan_so(c1)};{phan_so(c2)};{phan_so(c3-random.randint(1,5))})",
	f"{diem_C}({phan_so(c1+random.randint(1,5))};{phan_so(c2)};{phan_so(c3)})",
	f"{diem_C}({phan_so(c1)};{phan_so(c2+random.randint(1,5))};{phan_so(c3)})",
	]

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

    #Tạo các phương án
	pa_A= f"* ${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n" \

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



#[D12_C2_B3_16]-M2. Cho tam giác ABC. Tìm tọa độ trọng tâm.
def mnj_34_jkl_L12_C2_B3_16():
	ten=["A","B","C","D","E","M","N","P"]
	random.shuffle(ten)
	A,B,C=ten[0:3]
	G=random.choice(["G", "H", "I", "K" ])
	bo_toa_do=tao_3dinh_tamgiac()
	a1,a2,a3=bo_toa_do[0]
	b1,b2,b3=bo_toa_do[1]
	c1,c2,c3=bo_toa_do[2]

	noi_dung=(
	f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3}), {C}({c1};{c2};{c3})$."
	f" Tọa độ trọng tâm ${{{G}}}$ của tam giác ${{{A}{B}{C}}}$ là"
	)
	
	x,y,z=(a1+b1+c1)/3,(a2+b2+c2)/3,(a3+b3+c3)/3	
	x_G,y_G,z_G=phan_so(x),phan_so(y),phan_so(z)
	
	kq_false=[
	[x, y+random.randint(1,3), z],
	[x+random.randint(1,3), y, z],
	[x, y, z+random.randint(1,3)],
	[x+random.randint(1,3), y, z+random.randint(1,3)],
	[x+random.randint(1,3), y-random.randint(1,3), z-random.randint(1,3)],
	[x-random.randint(1,3), y+random.randint(1,3), z],
	[x-random.randint(1,3), y-random.randint(1,3), z+random.randint(1,3)],	
	[x-random.randint(1,3), y+random.randint(1,3), z-random.randint(1,3)],
	]	
	random.shuffle(kq_false)

	kq=f"({x_G}; {y_G}; {z_G})"
	kq2,kq3,kq4=kq_false[0:3]
	x2,y2,z2=kq2
	x3,y3,z3=kq3
	x4,y4,z4=kq4
	kq2=f"({phan_so(x2)}; {phan_so(y2)}; {phan_so(x2)})"
	kq3=f"({phan_so(x3)}; {phan_so(y3)}; {phan_so(x3)})"
	kq4=f"({phan_so(x4)}; {phan_so(y4)}; {phan_so(x4)})"

	noi_dung_loigiai=(
	f"${G}=(\\dfrac{{{a1}+{b1}+{c1}}}{{3}}; \\dfrac{{{a2}+{b2}+{c2}}}{{3}}; \\dfrac{{{a3}+{b3}+{c3}}}{{3}})=({x_G}, {y_G}, {z_G})$."
	)
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")

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

#[D12_C2_B3_17]-M2. Cho A, vto_AB, vto_AC. Tìm tọa độ trọng tâm.
def mnj_34_jkl_L12_C2_B3_17():
	ten=["A","B","C","D","E","M","N","P"]
	random.shuffle(ten)
	A,B,C=ten[0:3]
	G=random.choice(["G", "H", "I", "K" ])
	bo_toa_do=tao_3dinh_tamgiac()
	a1,a2,a3=bo_toa_do[0]
	b1,b2,b3=bo_toa_do[1]
	c1,c2,c3=bo_toa_do[2]
	AB=f"{vec(f"{A}{B}")}({b1-a1};{b2-a2};{b3-a3})"
	AC=f"{vec(f"{A}{C}")}({c1-a1};{c2-a2};{c3-a3})"

	noi_dung=(
	f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${A}({a1};{a2};{a3}), {AB}$ và ${AC}$."
	f" Tọa độ trọng tâm ${{{G}}}$ của tam giác ${{{A}{B}{C}}}$ là"
	)
	
	x,y,z=(a1+b1+c1)/3,(a2+b2+c2)/3,(a3+b3+c3)/3	
	x_G,y_G,z_G=phan_so(x),phan_so(y),phan_so(z)
	
	kq_false=[
	[x, y+random.randint(1,3), z],
	[x+random.randint(1,3), y, z],
	[x, y, z+random.randint(1,3)],
	[x+random.randint(1,3), y, z+random.randint(1,3)],
	[x+random.randint(1,3), y-random.randint(1,3), z-random.randint(1,3)],
	[x-random.randint(1,3), y+random.randint(1,3), z],
	[x-random.randint(1,3), y-random.randint(1,3), z+random.randint(1,3)],	
	[x-random.randint(1,3), y+random.randint(1,3), z-random.randint(1,3)],
	]	
	random.shuffle(kq_false)

	kq=f"({x_G}; {y_G}; {z_G})"
	kq2,kq3,kq4=kq_false[0:3]
	x2,y2,z2=kq2
	x3,y3,z3=kq3
	x4,y4,z4=kq4
	kq2=f"({phan_so(x2)}; {phan_so(y2)}; {phan_so(x2)})"
	kq3=f"({phan_so(x3)}; {phan_so(y3)}; {phan_so(x3)})"
	kq4=f"({phan_so(x4)}; {phan_so(y4)}; {phan_so(x4)})"

	noi_dung_loigiai=(
		f"Từ ${A}({a1};{a2};{a3}), {AB}, {AC}$\n\n$\\Rightarrow {B}({b1};{b2};{b3}),{C}({c1};{c2};{c3})$.\n\n"
	f"${G}=(\\dfrac{{{a1}+{b1}+{c1}}}{{3}}; \\dfrac{{{a2}+{b2}+{c2}}}{{3}}; \\dfrac{{{a3}+{b3}+{c3}}}{{3}})=({x_G}, {y_G}, {z_G})$."
	)
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")

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

#[D12_C2_B3_18]-M3. Cho A,B,G. Tìm C để ABC nhận G làm trọng tâm
def mnj_34_jkl_L12_C2_B3_18():
	ten=["A","B","C","D","E","M","N","P"]
	random.shuffle(ten)
	A,B,C=ten[0:3]
	G=random.choice(["G", "H", "I", "K" ])
	bo_toa_do=tao_3dinh_tamgiac()
	a1,a2,a3=bo_toa_do[0]
	b1,b2,b3=bo_toa_do[1]
	c1,c2,c3=bo_toa_do[2]
	AB=f"{vec(f"{A}{B}")}({b1-a1};{b2-a2};{b3-a3})"
	AC=f"{vec(f"{A}{C}")}({c1-a1};{c2-a2};{c3-a3})"

	g1,g2,g3=(a1+b1+c1)/3,(a2+b2+c2)/3,(a3+b3+c3)/3
	x_G,y_G,z_G=phan_so(g1),phan_so(g2),phan_so(g3)

	noi_dung=(
	f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3})$."
	f" Tam giác ${{{A}{B}{C}}}$ nhận ${{{G}({x_G};{y_G};{z_G})}}$ làm trọng tâm. Tọa độ điểm ${{{C}}}$ là"
	)	
	
	x,y,z=c1,c2,c3
	kq_false=[
	[x, y+random.randint(1,3), z],
	[x+random.randint(1,3), y, z],
	[x, y, z+random.randint(1,3)],
	[x+random.randint(1,3), y, z+random.randint(1,3)],
	[x+random.randint(1,3), y-random.randint(1,3), z-random.randint(1,3)],
	[x-random.randint(1,3), y+random.randint(1,3), z],
	[x-random.randint(1,3), y-random.randint(1,3), z+random.randint(1,3)],	
	[x-random.randint(1,3), y+random.randint(1,3), z-random.randint(1,3)],
	]	
	random.shuffle(kq_false)

	kq=f"({c1}; {c2}; {c3})"
	kq2,kq3,kq4=kq_false[0:3]
	x2,y2,z2=kq2
	x3,y3,z3=kq3
	x4,y4,z4=kq4
	kq2=f"({phan_so(x2)}; {phan_so(y2)}; {phan_so(x2)})"
	kq3=f"({phan_so(x3)}; {phan_so(y3)}; {phan_so(x3)})"
	kq4=f"({phan_so(x4)}; {phan_so(y4)}; {phan_so(x4)})"

	if g1<0: x_G=f"({x_G})"
	if g2<0: y_G=f"({y_G})"
	if g3<0: z_G=f"({z_G})"

	noi_dung_loigiai=(
		f"${{{G}}}$ là trọng tâm của tam giác ${{{A}{B}{C}}}$ nên\n\n"	
	f"$\\left\\{{ \\begin{{array}}{{l}} \n\
	x_{A}+x_{B}+x_{C}=3x_{G} \\\\ \n\
	y_{A}+y_{B}+y_{C}=3y_{G} \\\\ \n\
	z_{A}+z_{B}+z_{C}=3z_{G} \n\
	\\end{{array}} \\right.$"
	f"$\\Rightarrow\\left\\{{ \\begin{{array}}{{l}} \n\
	x_{C}=3x_{G}-x_{A}-x_{B} \\\\ \n\
	y_{C}=3y_{G}-y_{A}-y_{B} \\\\ \n\
	z_{C}=3z_{G}-z_{A}-z_{B} \n\
	\\end{{array}} \\right.$\n\n"
	f"$\\Rightarrow\\left\\{{ \\begin{{array}}{{l}} \n\
	x_{C}=3.{x_G}-{a1}-{b1}={c1}\\\\ \n\
	y_{C}=3.{y_G}-{a2}-{b2}={c2} \\\\ \n\
	z_{C}=3.{z_G}-{a3}-{b3}={c3} \n\
	\\end{{array}} \\right.$"
	)
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("--","+")

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

#[D12_C2_B3_19]-M1. Cho A,B. Tìm tọa độ vectơ AB
def mnj_34_jkl_L12_C2_B3_19():
	letters = [chr(i) for i in range(ord('A'), ord('N') + 1)]
	random.shuffle(letters)	
	A,B,C=letters[0:3]	
	a1,a2,a3=[random.randint(-7,7) for i in range(3)]
	b1,b2,b3=[random.randint(-7,7) for i in range(3)]
	while any([all([a1==0,a2==0,a3==0]),all([b1==0,b2==0,b3==0]),a1==b1,a2==b2,a3==b3]):
		a1,a2,a3=[random.randint(-7,7) for i in range(3)]
		b1,b2,b3=[random.randint(-7,7) for i in range(3)]

	chon=random.randint(1,2)
	if chon==1:
		x,y,z=b1-a1,b2-a2,b3-a3
		noi_dung=(
		f" Trong không gian ${{Oxyz}}$, cho hai điểm ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3})$."
		f" Tọa độ vectơ ${vec(f"{A}{B}")}$ là")

		noi_dung_loigiai=(f"${vec(f"{A}{B}")}=({b1}-{a1};{b2}-{a2};{b3}-{a3})=({x};{y};{z})$.")
	
	if chon==2:
		x,y,z=a1-b1,a2-b2,a3-b3
		noi_dung=(
		f" Trong không gian ${{Oxyz}}$, cho hai điểm ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3})$."
		f" Tọa độ vectơ ${vec(f"{B}{A}")}$ là")

		noi_dung_loigiai=(f"${vec(f"{B}{A}")}=({a1}-{b1};{a2}-{b2};{a3}-{b3})=({x};{y};{z})$.")	

	kq_false=[
	(-x, -y, -z),
	(x, y+random.randint(1,3), z),
	(x+random.randint(1,3), y, z),
	(x, y, z+random.randint(1,3)),
	]	
	random.shuffle(kq_false)

	kq=f"({x}; {y}; {z})"
	kq2,kq3,kq4=kq_false[0:3]

	
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("--","+")

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

#[D12_C2_B3_20]-M1. Cho A,B. Tính độ dài đoạn thẳng AB
def mnj_34_jkl_L12_C2_B3_20():
	ten=["A","B","C","D","E","M","N","P"]
	random.shuffle(ten)
	A,B,C=ten[0:3]	
	a1,a2,a3=[random.randint(-7,7) for i in range(3)]
	b1,b2,b3=[random.randint(-7,7) for i in range(3)]
	while any([all([a1==0,a2==0,a3==0]),all([b1==0,b2==0,b3==0]),a1==b1,a2==b2,a3==b3]):
		a1,a2,a3=[random.randint(-7,7) for i in range(3)]
		b1,b2,b3=[random.randint(-7,7) for i in range(3)]


	x,y,z=b1-a1,b2-a2,b3-a3
	kq=sqrt(x**2+y**2+z**2)
	AB=random.choice([f"{{{A}{B}}}",f"{{{B}{A}}}"])
	noi_dung=(
	f" Trong không gian ${{Oxyz}}$, cho hai điểm ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3})$."
	f" Độ dài đoạn thẳng ${AB}$ bằng")

	noi_dung_loigiai=(
	f"${vec(f"{A}{B}")}=({b1}-{a1};{b2}-{a2};{b3}-{a3})=({x};{y};{z})$.\n\n"
	f"${A}{B}=\\sqrt{{{x**2}+{y**2}+{z**2}}}={latex(kq)}$.")
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("--","+")

	kq_false=[
	abs(x+y+z),
	sqrt((a1+b1)**2+(a2+b2)**2+(a3+b3)**2),
	sqrt(x**2+y**2+abs(z)),
	sqrt(x**2+y**2+z**2+random.randint(1,3))	
	]	
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]	

	pa_A= f"*${latex(kq)}$"
	pa_B= f"${latex(kq2)}$"
	pa_C= f"${latex(kq3)}$"
	pa_D= f"${latex(kq4)}$"
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


#[D12_C2_B3_21]-M3. Cho A,B,C(a;y_C;b),G(x_G;c;z_G). Tính a+b+c
def mnj_34_jkl_L12_C2_B3_21():

	ten=["A","B","C","D","E","M","N","P"]
	random.shuffle(ten)
	A,B,C=ten[0:3]
	G=random.choice(["G", "H", "I", "K" ])
	bo_toa_do=tao_3dinh_tamgiac()
	a1,a2,a3=bo_toa_do[0]
	b1,b2,b3=bo_toa_do[1]
	c1,c2,c3=bo_toa_do[2]
	
	g1,g2,g3=(a1+b1+c1)/3,(a2+b2+c2)/3,(a3+b3+c3)/3	
	x_G,y_G,z_G=phan_so(g1),phan_so(g2),phan_so(g3)

	if c1+c3+g2==int(c1+c3+g2):
		dap_an=int(c1+c3+g2)
		noi_dung=(
		f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3}), {C}(a;{c2};b)$."
		f" Tam giác ${{{A}{B}{C}}}$ có trọng tâm ${G}({x_G};c;{z_G})$. Tính $a+b+c$."
		)
	else:

		dap_an=f"{round(c1+c3+g2,1):.1f}".replace(".",",")
		noi_dung=(
		f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3}), {C}(a;{c2};b)$."
		f" Tam giác ${{{A}{B}{C}}}$ có trọng tâm ${G}({x_G};c;{z_G})$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười)."
		)

	noi_dung_loigiai=(
	f"Do ${{{G}}}$ là trọng tâm của tam giác ${{{A}{B}{C}}}$ nên ta có:\n\n"
	f"${a1}+{b1}+a=3.{x_G} \\Rightarrow a={c1}$.\n\n"
	f"${a2}+{b2}+{c2}=3.c \\Rightarrow c={phan_so(g2)}$.\n\n"
	f"${a3}+{b3}+b=3.{z_G} \\Rightarrow b={c3}$.\n\n"
	f"Vậy $a+b+c={c1}+{c3}+{phan_so(g2)}={phan_so(c1+c3+g2)}$.\n\n"
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C2_B3_22]-M3. Tìm m để ba điểm lập thành tam giác vuông
def mnj_34_jkl_L12_C2_B3_22():
	ten=["A","B","C","D","E","M","N","P"]
	random.shuffle(ten)
	A,B,C=ten[0:3]
	G=random.choice(["G", "H", "I", "K" ])
	bo_toa_do=tao_3dinh_tamgiacvuong()
	a1,a2,a3=bo_toa_do[0]
	b1,b2,b3=bo_toa_do[1]
	c1,c2,c3=bo_toa_do[2]	
	
	m=sp.symbols("m")

	d1 = random.choice([i for i in range(-5, 6) if i!=0])
	d2 = random.choice([i for i in range(-5, 6) if i!=0])
	if (c1-d2)/d1==N((c1-d2)/d1,0):
		dap_an=int((c1-d2)/d1)
	else:
		dap_an=f"{N((c1-d2)/d1,1):.1f}".replace(".",",")

	if bo_toa_do[3]=="A":
		vitri=f"{A}"
		noi_dung_loigiai=(
		f"${vec(f"{A}{B}")}=({b1-a1};{b2-a2};{b3-a3})$.\n\n"
		f"${vec(f"{A}{C}")}=({latex(d1*m+d2-a1)};{c2-a2};{c3-a3})$.\n\n"
		f"Tam giác ${{{A}{B}{C}}}$ vuông tại ${{{A}}}$ khi ${vec(f"{A}{B}")}.{vec(f"{A}{C}")}=0$\n\n"
		f"$\\Rightarrow {b1-a1}.({latex(d1*m+d2-a1)})+{b2-a2}.{tao_ngoac(c2-a2)}+{b3-a3}.{tao_ngoac(c3-a3)}=0$\n\n"
		f"$\\Rightarrow {latex((b1-a1)*(d1*m+d2-a1)+(b2-a2)*(c2-a2)+(b3-a3)*(c3-a3))}=0$\n\n"
		f"$\\Rightarrow m={phan_so((c1-d2)/d1)}$.\n\n")

	if bo_toa_do[3]=="B":
		vitri=f"{B}"
		noi_dung_loigiai=(
		f"${vec(f"{B}{A}")}=({a1-b1};{a2-b2};{a3-b3})$.\n\n"
		f"${vec(f"{B}{C}")}=({latex(d1*m+d2-b1)};{c2-b2};{c3-b3})$.\n\n"
		f"Tam giác ${{{A}{B}{C}}}$ vuông tại ${{{B}}}$ khi ${vec(f"{B}{A}")}.{vec(f"{B}{C}")}=0$\n\n"
		f"$\\Rightarrow {a1-b1}.({latex(d1*m+d2-b1)})+{a2-b2}.{tao_ngoac(c2-b2)}+{a3-b3}.{tao_ngoac(c3-b3)}=0$\n\n"
		f"$\\Rightarrow {latex((a1-b1)*(d1*m+d2-b1)+(a2-b2)*(c2-b2)+(a3-b3)*(c3-b3))}=0$\n\n"
		f"$\\Rightarrow m={phan_so((c1-d2)/d1)}$.\n\n")

	if bo_toa_do[3]=="C":
		vitri=f"{B}"
		noi_dung_loigiai=(
		f"${vec(f"{B}{A}")}=({a1-b1};{a2-b2};{a3-b3})$.\n\n"
		f"${vec(f"{B}{C}")}=({latex(d1*m+d2-b1)};{c2-b2};{c3-b3})$.\n\n"
		f"Tam giác ${{{A}{B}{C}}}$ vuông tại ${{{B}}}$ khi ${vec(f"{B}{A}")}.{vec(f"{B}{C}")}=0$\n\n"
		f"$\\Rightarrow {a1-b1}.({latex(d1*m+d2-b1)})+{a2-b2}.{tao_ngoac(c2-b2)}+{a3-b3}.{tao_ngoac(c3-b3)}=0$\n\n"
		f"$\\Rightarrow {latex((a1-b1)*(d1*m+d2-b1)+(a2-b2)*(c2-b2)+(a3-b3)*(c3-b3))}=0$\n\n"
		f"$\\Rightarrow m={phan_so((c1-d2)/d1)}$.\n\n")

	chon=random.randint(1,3)
	if chon==1:
		noi_dung=f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3}), {C}({latex(d1*m+d2)};{c2};{c3})$."
	
	if chon==2:
		noi_dung=f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${A}({a1};{a2};{a3}),{C}({latex(d1*m+d2)};{c2};{c3})$, {B}({b1};{b2};{b3})."

	if chon==3:
		noi_dung=f" Trong không gian ${{Oxyz}}$, cho tam giác ${{{A}{B}{C}}}$ với ${C}({latex(d1*m+d2)};{c2};{c3})$, {A}({a1};{a2};{a3}),{B}({b1};{b2};{b3})."

	if (c1-d2)/d1==N((c1-d2)/d1,0):	
		
		noi_dung+=f" Tìm giá trị của ${{m}}$ để tam giác ${{{A}{B}{C}}}$ vuông tại ${{{vitri}}}$."
		
	else:
		noi_dung+=f" Tìm giá trị của ${{m}}$ để tam giác ${{{A}{B}{C}}}$ vuông tại ${{{vitri}}}$ (kết quả làm tròn đến hàng phần mười)."

	
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
		)


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C2_B3_23]-TL-M3. Bài toán liên quan trung điểm (VDT)
def mnj_34_jkl_L12_C2_B3_23():
	
	A=random.choice(["A","C", "E", "P"])
	B=random.choice(["B","D", "F"])
	M=random.choice(["M","N", "K"])

	I=random.choice(["I","H","G"])

	chon=random.randint(1,3)
	if chon==1:
		a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		a2 = 0
		a3 = 0

		b1=0
		b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		
		m1,m2,m3=(a1+b1)/2, (a2+b2)/2, (a3+b3)/2

		x,y,z=(b1+m1)/2, (b2+m2)/2, (b3+m3)/2

		noi_dung=(f"Trong không gian ${{Oxyz}}$, cho điểm ${M}({phan_so(m1)};{phan_so(m2)};{phan_so(m3)})$."
			f" Biết điểm ${{{A}}}$ thuộc trục ${{Ox}}$ và điểm ${{{B}}}$ thuộc mặt phẳng ${{(Oyz)}}$"
			f" sao cho ${{{M}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$."
			f" Gọi ${{{I}(m;n;p)}}$ là trung điểm của ${{{B}{M}}}$.")

		if x+y+z==int(x+y+z):
			dap_an=int(m1+m2+m3)
			noi_dung+=f"Tính $m+n+p$."
		else:
			dap_an=f"{round(x+y+z,1):.1f}".replace(".",",")
			noi_dung+=f"Tính $m+n+p$((kết quả làm tròn đến hàng phần mười)."

		noi_dung_loigiai=(
			f"Gọi ${A}(a;0;0), {B}(0;b;c)$.\n\n"
			f"Vì ${{{M}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$ nên"
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			\\dfrac{{a}}{{2}}={phan_so(m1)} \\\\ \n\
			\\dfrac{{b}}{{2}}={phan_so(m2)} \\\\ \n\
			\\dfrac{{c}}{{2}}={phan_so(m3)}\n\
			\\end{{array}} \\right. \\Rightarrow a={a1},b={b2},c={b3}$.\n\n"
			f"Suy ra ${B}({b1};{b2};{b3})$.\n\n"
			f"${{{I}}}$ là trung điểm của ${{{B}{M}}} \\Rightarrow $"
			f"${I}({phan_so(x)};{phan_so(y)};{phan_so(z)})$.\n\n"
			f"$m+n+p={phan_so(x)}+{phan_so(y)}+{phan_so(z)}={phan_so(x+y+z)}$.\n\n")
	if chon==2:
		a1 = 0
		a2 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		a3 = 0

		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b2= 0
		b3= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		

		m1,m2,m3=(a1+b1)/2, (a2+b2)/2, (a3+b3)/2

		x,y,z=(b1+m1)/2, (b2+m2)/2, (b3+m3)/2

		noi_dung=(f"Trong không gian ${{Oxyz}}$, cho điểm ${M}({phan_so(m1)};{phan_so(m2)};{phan_so(m3)})$."
			f" Biết điểm ${{{A}}}$ thuộc trục ${{Oy}}$ và điểm ${{{B}}}$ thuộc mặt phẳng ${{(Oxz)}}$"
			f" sao cho ${{{M}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$."
			f" Gọi ${{{I}(m;n;p)}}$ là trung điểm của ${{{B}{M}}}$.")

		if x+y+z==int(x+y+z):
			dap_an=int(m1+m2+m3)
			noi_dung+=f" Tính $m+n+p$."
		else:
			dap_an=f"{round(x+y+z,1):.1f}".replace(".",",")
			noi_dung+=f" Tính $m+n+p$ (kết quả làm tròn đến hàng phần mười)."

		noi_dung_loigiai=(
			f"Gọi ${A}(0;a;0), {B}(b;0;c)$.\n\n"
			f"Vì ${{{M}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$ nên"
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			\\dfrac{{b}}{{2}}={phan_so(m1)} \\\\ \n\
			\\dfrac{{a}}{{2}}={phan_so(m2)} \\\\ \n\
			\\dfrac{{c}}{{2}}={phan_so(m3)}\n\
			\\end{{array}} \\right. \\Rightarrow a={a2},b={b1},c={b3}$.\n\n"
			f"Suy ra ${B}({b1};{b2};{b3})$.\n\n"
			f"${{{I}}}$ là trung điểm của ${{{B}{M}}} \\Rightarrow $"
			f"${I}({phan_so(x)};{phan_so(y)};{phan_so(z)})$.\n\n"
			f"$m+n+p={phan_so(x)}+{phan_so(y)}+{phan_so(z)}={phan_so(x+y+z)}$.\n\n")

	if chon==3:
		a1 = 0
		a2 = 0
		a3 = random.choice([random.randint(-10, -1), random.randint(1, 10)])

		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b3= 0		

		m1,m2,m3=(a1+b1)/2, (a2+b2)/2, (a3+b3)/2

		x,y,z=(b1+m1)/2, (b2+m2)/2, (b3+m3)/2

		noi_dung=(f"Trong không gian ${{Oxyz}}$, cho điểm ${M}({phan_so(m1)};{phan_so(m2)};{phan_so(m3)})$."
			f" Biết điểm ${{{A}}}$ thuộc trục ${{Oz}}$ và điểm ${{{B}}}$ thuộc mặt phẳng ${{(Oxy)}}$"
			f" sao cho ${{{M}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$."
			f" Gọi ${{{I}(m;n;p)}}$ là trung điểm của ${{{B}{M}}}$.")

		if x+y+z==int(x+y+z):
			dap_an=int(m1+m2+m3)
			noi_dung+=f" Tính $m+n+p$."
		else:
			dap_an=f"{round(x+y+z,1):.1f}".replace(".",",")
			noi_dung+=f" Tính $m+n+p$ (kết quả làm tròn đến hàng phần mười)."

		noi_dung_loigiai=(
			f"Gọi ${A}(0;0;a), {B}(b;c;0)$.\n\n"
			f"Vì ${{{M}}}$ là trung điểm của đoạn thẳng ${{{A}{B}}}$ nên"
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			\\dfrac{{b}}{{2}}={phan_so(m1)} \\\\ \n\
			\\dfrac{{c}}{{2}}={phan_so(m2)} \\\\ \n\
			\\dfrac{{a}}{{2}}={phan_so(m3)}\n\
			\\end{{array}} \\right. \\Rightarrow a={a3},b={b1},c={b2}$.\n\n"
			f"Suy ra ${B}({b1};{b2};{b3})$.\n\n"
			f"${{{I}}}$ là trung điểm của ${{{B}{M}}} \\Rightarrow $"
			f"${I}({phan_so(x)};{phan_so(y)};{phan_so(z)})$.\n\n"
			f"$m+n+p={phan_so(x)}+{phan_so(y)}+{phan_so(z)}={phan_so(x+y+z)}$.\n\n")

	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
		
	debai_word= f"{noi_dung}\n"
	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
		)
	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[oly]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C2_B3_24]-TL-M3. Tìm hình chiếu của điểm lên trục tọa độ
def mnj_34_jkl_L12_C2_B3_24():
	A=random.choice(["A","C","E","P","B","D","F","M","N","K"])	
	H=random.choice(["I","H","G"])

	# Tạo danh sách các số nguyên từ -10 đến 10, bỏ qua số 0
	numbers = list(range(-10, 0)) + list(range(1, 11))

	# Lấy ngẫu nhiên ba số đôi một khác nhau
	result = random.sample(numbers, 3)
	a1,a2,a3=result
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là hình chiếu vuông góc của điểm ${{{A}}}$ lên trục ${{Ox}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({a1};0;0)"
		kq_false=[
		f"({a1};{a2};0)",
		f"(0;{a2};0)",
		f"(0;0;{a3})",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Hình chiếu vuông góc của điểm ${{{A}}}$ lên trục ${{Ox}}$ là ${{{H}}}{kq}$."
	)
	
	if chon==2:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là hình chiếu vuông góc của điểm ${{{A}}}$ lên trục ${{Oy}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"(0;{a2};0)"
		kq_false=[
		f"({a1};{a2};0)",
		f"({a1};0;0)",
		f"(0;0;{a3})",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Hình chiếu vuông góc của điểm ${{{A}}}$ lên trục ${{Oy}}$ là ${{{H}}}{kq}$."
	)

	if chon==3:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là hình chiếu vuông góc của điểm ${{{A}}}$ lên trục ${{Oz}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"(0;0;{a3})"
		kq_false=[
		f"({a1};{a2};0)",
		f"({a1};0;0)",
		f"(0;{a2};0)",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Hình chiếu vuông góc của điểm ${{{A}}}$ lên trục ${{Oz}}$ là ${{{H}}}{kq}$."
	)
	
	
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]


	

	pa_A= f"*${H}{kq}$"
	pa_B= f"${H}{kq2}$"
	pa_C= f"${H}{kq3}$"
	pa_D= f"${H}{kq4}$"
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

#[D12_C2_B3_25]-TL-M3. Tìm hình chiếu của điểm lên mặt phẳng tọa độ
def mnj_34_jkl_L12_C2_B3_25():
	A=random.choice(["A","C","E","P","B","D","F","M","N","K"])	
	H=random.choice(["I","H","G"])

	# Tạo danh sách các số nguyên từ -10 đến 10, bỏ qua số 0
	numbers = list(range(-10, 0)) + list(range(1, 11))

	# Lấy ngẫu nhiên ba số đôi một khác nhau
	result = random.sample(numbers, 3)
	a1,a2,a3=result
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là hình chiếu vuông góc của điểm ${{{A}}}$ lên mặt phẳng ${{(Oxy)}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({a1};{a2};0)"
		kq_false=[
		f"({a1};0;0)",
		f"(0;{a2};0)",
		f"(0;0;{a3})",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Hình chiếu vuông góc của điểm ${{{A}}}$ lên trục mặt phẳng ${{(Oxy)}}$ là ${{{H}}}{kq}$."
	)
	
	if chon==2:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là hình chiếu vuông góc của điểm ${{{A}}}$ lên trục ${{(Oxz)}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({a1};0;{a3})"
		kq_false=[
		f"({a1};{a2};0)",
		f"({a1};0;0)",
		f"(0;0;{a3})",
		f"(0;{a2};{a3})",
		f"(0;{a2};0)"
		]
		noi_dung_loigiai=(
	f"Hình chiếu vuông góc của điểm ${{{A}}}$ lên trục mặt phẳng ${{(Oxz)}}$ là ${{{H}}}{kq}$."
	)

	if chon==3:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là hình chiếu vuông góc của điểm ${{{A}}}$ lên mặt phẳng ${{(Oyz)}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"(0;{a2};{a3})"
		kq_false=[
		f"(0;0;{a3})",
		f"({a1};0;0)",
		f"(0;{a2};0)",
		f"({a1};{a2};0)",
		f"({a1};0;{a3})"]

		noi_dung_loigiai=(
	f"Hình chiếu vuông góc của điểm ${{{A}}}$ lên trục mặt phẳng ${{(Oyz)}}$ là ${{{H}}}{kq}$."
	)
	
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]


	

	pa_A= f"*${H}{kq}$"
	pa_B= f"${H}{kq2}$"
	pa_C= f"${H}{kq3}$"
	pa_D= f"${H}{kq4}$"
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

#[D12_C2_B3_26]-TL-M3. Tìm điểm đối xứng của điểm qua trục tọa độ
def mnj_34_jkl_L12_C2_B3_26():
	A=random.choice(["A","B","C","D","E","F","M","N","P"])	
	H=random.choice(["I","H","G","K"])

	# Tạo danh sách các số nguyên từ -10 đến 10, bỏ qua số 0
	numbers = list(range(-10, 0)) + list(range(1, 11))

	# Lấy ngẫu nhiên ba số đôi một khác nhau
	result = random.sample(numbers, 3)
	a1,a2,a3=result
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là điểm đối xứng với điểm ${{{A}}}$ qua trục ${{Ox}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({a1};{-a2};{-a3})"
		kq_false=[
		f"({a1};{a2};{-a3})",
		f"({-a1};{a2};{a3})",
		f"({a1};{-a2};{a3})",
		f"({-a1};{-a2};{a3})",
		f"({-a1};{a2};{-a3})",
		f"({a1};{a2};0)",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Điểm đối xứng với điểm ${{{A}}}$ qua trục ${{Ox}}$ là ${{{H}}}{kq}$."
	)
	
	if chon==2:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là điểm đối xứng với điểm ${{{A}}}$ qua trục ${{Oy}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({-a1};{a2};{-a3})"
		kq_false=[
		f"({a1};{a2};{-a3})",
		f"({-a1};{a2};{a3})",
		f"({a1};{-a2};{a3})",
		f"({-a1};{-a2};{a3})",
		f"({a1};{-a2};{-a3})",
		f"({a1};{a2};0)",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Điểm đối xứng với điểm ${{{A}}}$ qua trục ${{Oy}}$ là ${{{H}}}{kq}$."
	)

	if chon==3:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là điểm đối xứng với điểm ${{{A}}}$ qua trục ${{Oz}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({-a1};{-a2};{a3})"
		kq_false=[
		f"({a1};{a2};{-a3})",
		f"({-a1};{a2};{a3})",
		f"({a1};{-a2};{a3})",
		f"({-a1};{a2};{-a3})",
		f"({a1};{-a2};{-a3})",
		f"({a1};{a2};0)",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Điểm đối xứng với điểm ${{{A}}}$ qua trục ${{Oz}}$ là ${{{H}}}{kq}$."	)
	
	
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]	

	pa_A= f"*${H}{kq}$"
	pa_B= f"${H}{kq2}$"
	pa_C= f"${H}{kq3}$"
	pa_D= f"${H}{kq4}$"
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

#[D12_C2_B3_27]-TL-M3. Tìm điểm đối xứng của điểm qua mặt phẳng tọa độ
def mnj_34_jkl_L12_C2_B3_27():
	A=random.choice(["A","B","C","D","E","F","M","N","P"])	
	H=random.choice(["I","H","G","K"])

	# Tạo danh sách các số nguyên từ -10 đến 10, bỏ qua số 0
	numbers = list(range(-10, 0)) + list(range(1, 11))

	# Lấy ngẫu nhiên ba số đôi một khác nhau
	result = random.sample(numbers, 3)
	a1,a2,a3=result
	chon=random.randint(1,3)
	if chon==1:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là điểm đối xứng với điểm ${{{A}}}$ qua mặt phẳng ${{(Oxy)}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({a1};{a2};{-a3})"
		kq_false=[
		f"({a1};{-a2};{-a3})",
		f"({-a1};{a2};{a3})",
		f"({a1};{-a2};{a3})",
		f"({-a1};{-a2};{a3})",
		f"({-a1};{a2};{-a3})",
		f"({a1};{a2};0)",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Điểm đối xứng với điểm ${{{A}}}$ qua trục mặt phẳng ${{(Oxy)}}$ là ${{{H}}}{kq}$."
	)
	
	if chon==2:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là điểm đối xứng với điểm ${{{A}}}$ qua mặt phẳng ${{(Oyz)}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({-a1};{a2};{a3})"
		kq_false=[
		f"({a1};{a2};{-a3})",
		f"({-a1};{a2};{-a3})",
		f"({a1};{-a2};{a3})",
		f"({-a1};{-a2};{a3})",
		f"({a1};{-a2};{-a3})",
		f"({a1};{a2};0)",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Điểm đối xứng với điểm ${{{A}}}$ qua mặt phẳng ${{(Oyz)}}$ là ${{{H}}}{kq}$."
	)

	if chon==3:
		noi_dung=(
		f"Trong không gian ${{Oxyz}}$, cho điểm ${A}({a1};{a2};{a3})$."
		f" Gọi ${{{H}}}$ là điểm đối xứng với điểm ${{{A}}}$ qua mặt phẳng ${{(Oxz)}}$."
		f" Tọa độ điểm ${{{H}}}$ là")		

		kq=f"({a1};{-a2};{a3})"
		kq_false=[
		f"({a1};{a2};{-a3})",
		f"({-a1};{a2};{a3})",
		f"({-a1};{-a2};{a3})",
		f"({-a1};{a2};{-a3})",
		f"({a1};{-a2};{-a3})",
		f"({a1};{a2};0)",
		f"(0;{a2};{a3})",
		f"({a1};0;{a3})"]
		noi_dung_loigiai=(
	f"Điểm đối xứng với điểm ${{{A}}}$ qua mặt phẳng ${{(Oxz)}}$ là ${{{H}}}{kq}$."	)
	
	
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]	

	pa_A= f"*${H}{kq}$"
	pa_B= f"${H}{kq2}$"
	pa_C= f"${H}{kq3}$"
	pa_D= f"${H}{kq4}$"
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

#[D12_C2_B3_28]-TF-M3. Cho tam giác. Xét Đ-S: Độ dài, tọa độ vectơ, R, S.
def mnj_34_jkl_L12_C2_B3_28():
	ten=["A","B","C","D","E","M","N","P"]
	random.shuffle(ten)
	A,B,C=ten[0:3]
	
	#Tạo tam giác vuông tại A
	bo_toa_do=tao_3dinh_tamgiacvuong_2()
	a1,a2,a3=bo_toa_do[0]
	b1,b2,b3=bo_toa_do[1]
	c1,c2,c3=bo_toa_do[2]
	chon=random.randint(1,3)
	if chon==1:
		noi_dung = f"Cho các điểm ${A}({a1};{a2};{a3}), {B}({b1};{b2};{b3}), {C}({c1};{c2};{c3})$. Xét tính đúng-sai của các khẳng định sau:"	
	
	if chon==2:
		noi_dung = f"Cho các điểm ${B}({b1};{b2};{b3}), {A}({a1};{a2};{a3}), {C}({c1};{c2};{c3})$. Xét tính đúng-sai của các khẳng định sau:"

	if chon==3:
		noi_dung = f"Cho các điểm ${C}({c1};{c2};{c3}), {B}({b1};{b2};{b3}), {A}({a1};{a2};{a3})$. Xét tính đúng-sai của các khẳng định sau:"
	
		
	x_AB,y_AB,z_AB=b1-a1,b2-a2,b3-a3
	x_AC,y_AC,z_AC=c1-a1,c2-a2,c3-a3
	x_BC,y_BC,z_BC=c1-b1,c2-b2,c3-b3

	vec_AB=f"{vec(f"{A}{B}")}"
	vec_AC=f"{vec(f"{A}{C}")}"
	vec_BC=f"{vec(f"{B}{C}")}"

	AB=sqrt(x_AB**2+y_AB**2+z_AB**2)
	AB_false=sqrt(x_AB**2+y_AB**2+z_AB**2+random.randint(1,3))
	
	kq1_T=f"* Độ dài đoạn thẳng ${{{A}{B}}}$ bằng ${latex(AB)}$" 
	kq1_F=f"Độ dài đoạn thẳng ${{{A}{B}}}$ bằng ${latex(AB_false)}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=(f"${vec(f"{A}{B}")}=({x_AB};{y_AB};{z_AB})\\Rightarrow $"
		f"${A}{B}=\\sqrt{{{x_AB**2}+{y_AB**2}+{z_AB**2}}}={latex(AB)}$."
		)
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	ten=vec(f"{random.choice(["x","y","a","b"])}")

	m = random.choice([i for i in range(-4, 4) if i!=0])
	n = random.choice([i for i in range(-3, 3) if i!=0])
	a,b=sp.symbols("veca vecb")

	x,y,z=m*x_AB+n*x_AC, m*y_AB+n*y_AC, m*z_AB+n*z_AC


	kq2_T=f"* Tọa độ vectơ ${ten}={latex(m*a+n*b)}$ là $({x};{y};{z})$".replace("veca",f"{vec_AB}").replace("vecb",f"{vec_AC}")
	kq2_F=f"Tọa độ vectơ ${ten}={latex(m*a+n*b)}$ là $({x+random.randint(-2,2)};{y-random.randint(-2,2)};{z+random.randint(1,2)})$".replace("veca",f"{vec_AB}").replace("vecb",f"{vec_AC}")
	kq2=random.choice([kq2_T, kq2_F])
	HDG=(f"${vec(f"{A}{B}")}=({x_AB};{y_AB};{z_AB})$, "
		f"${vec(f"{A}{C}")}=({x_AC};{y_AC};{z_AC})$\n\n"
		f"${ten}={latex(m*a+n*b)}=({x};{y};{z})$."
		)
	HDG=HDG.replace("veca",f"{vec_AB}").replace("vecb",f"{vec_AC}")

	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phương án 3

	ten=vec(f"{random.choice(["u","v","w", "c", "d"])}")
	m = random.choice([i for i in range(-3, 3) if i!=0])
	n = random.choice([i for i in range(-3, 3) if i!=0])
	p = random.choice([i for i in range(-2, 2) if i!=0])
	k = random.choice([i for i in range(-3, 3) if i!=0])
	vecu,veca,vecb,vecc=sp.symbols("vecu veca vecb vecc")

	x,y,z=(k*x_BC-n*x_AB-p*x_AC)/m,(k*y_BC-n*y_AB-p*y_AC)/m,(k*z_BC-n*z_AB-p*z_AC)/m

	kq3_T=f"* Vectơ ${ten}$ thỏa mãn ${latex(m*vecu+n*veca+p*vecb)}={latex(k*vecc)}$ thì tọa độ vectơ ${ten}$ là $({phan_so(x)};{phan_so(y)};{phan_so(z)})$".replace("veca",f"{vec_AB}").replace("vecb",f"{vec_AC}").replace("vecc",f"{vec_BC}").replace("vecu",f"{ten}")
	kq3_F=f"Vectơ ${ten}$ thỏa mãn ${latex(m*vecu+n*veca+p*vecb)}={latex(k*vecc)}$ thì tọa độ vectơ ${ten}$ là $({phan_so(x+random.randint(1,2))};{phan_so(y-random.randint(-2,2))};{phan_so(z+random.randint(-2,2))})$".replace("veca",f"{vec_AB}").replace("vecb",f"{vec_AC}").replace("vecc",f"{vec_BC}").replace("vecu",f"{ten}")
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"${latex(m*vecu+n*veca+p*vecb)}={latex(k*vecc)}\\Rightarrow {ten}={phan_so(1/m)}({latex(k*vecc-n*veca-p*vecb)})=({phan_so(x)};{phan_so(y)};{phan_so(z)})$"
	HDG=HDG.replace("veca",f"{vec_AB}").replace("vecb",f"{vec_AC}").replace("vecc",f"{vec_BC}").replace("vecu",f"{ten}")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phương án 4
	chon=random.randint(1,3)
	
	if chon==1:
		R=sqrt(x_BC**2+y_BC**2+z_BC**2)/2
		R_false=random.choice([sqrt(x_AC**2+y_AC**2+z_AC**2)/2,sqrt(x_AB**2+y_AB**2+z_AB**2)/2])

		kq4_T=f"* Bán kính đường tròn ngoại tiếp tam giác ${{{A}{B}{C}}}$ là ${{{latex(R)}}}$"
		kq4_F=f"Bán kính đường tròn ngoại tiếp tam giác ${{{A}{B}{C}}}$ là ${{{latex(R_false)}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec_AB}=({x_AB};{y_AB};{z_AB}),{vec_AC}=({x_AC};{y_AC};{z_AC})$.\n\n"
		f"${vec_AB}.{vec_AC}=0\\Rightarrow $ tam giác ${{{A}{B}{C}}}$ vuông tại ${{{A}}}$.\n\n"
		f"${vec_BC}=({x_BC};{y_BC};{z_BC})\\Rightarrow {B}{C}={latex(sqrt(x_BC**2+y_BC**2+z_BC**2))}$.\n\n"
		f"$R=\\dfrac{{{B}{C}}}{{2}}={latex(R)}$.")
	
	if chon==2:
		AB=sqrt(x_AB**2+y_AB**2+z_AB**2)
		AC=sqrt(x_AC**2+y_AC**2+z_AC**2)
		S=nsimplify(1/2*AB*AC)
		S_false=nsimplify(AB*AC)

		kq4_T=f"* Diện tích tam giác ${{{A}{B}{C}}}$ bằng ${{{latex(S)}}}$"
		kq4_F=f"Diện tích tam giác ${{{A}{B}{C}}}$ là ${{{latex(S_false)}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec_AB}=({x_AB};{y_AB};{z_AB}),{vec_AC}=({x_AC};{y_AC};{z_AC}) \\Rightarrow {A}{B}={latex(AB)},{A}{C}={latex(AC)}$.\n\n"
		f"${vec_AB}.{vec_AC}=0\\Rightarrow $ tam giác ${{{A}{B}{C}}}$ vuông tại ${{{A}}}$.\n\n"		
		f"$S=\\dfrac{{1}}{{2}}.{A}{B}.{A}{C}={latex(S)}$.")

	if chon==3:
		AB=sqrt(x_AB**2+y_AB**2+z_AB**2)
		AC=sqrt(x_AC**2+y_AC**2+z_AC**2)
		AH=(AB*AC)/sqrt(AB**2+AC**2)
		AH_false=(AB*AC)/sqrt(AB**2+AC**2+random.randint(1,2))
		H=random.choice(["G", "H", "I", "K" ])
		
		kq4_T=f"* Gọi ${{{H}}}$ là chân đường cao hạ từ của ${{{A}}}$ của tam giác ${{{A}{B}{C}}}$. Độ dài ${{{A}{H}}}$ bằng ${{{latex(AH)}}}$"
		kq4_F=f"Gọi ${{{H}}}$ là chân đường cao hạ từ của ${{{A}}}$ của tam giác ${{{A}{B}{C}}}$. Độ dài ${{{A}{H}}}$ bằng ${{{latex(AH_false)}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"${vec_AB}=({x_AB};{y_AB};{z_AB}),{vec_AC}=({x_AC};{y_AC};{z_AC}) \\Rightarrow {A}{B}={latex(AB)},{A}{C}={latex(AC)}$.\n\n"
		f"${vec_AB}.{vec_AC}=0\\Rightarrow $ tam giác ${{{A}{B}{C}}}$ vuông tại ${{{A}}}$.\n\n"		
		f"${A}{H}=\\dfrac{{{A}{B}.{A}{C}}}{{\\sqrt{{{A}{B}^2+{A}{C}^2}}}}=\\dfrac{{{latex(AB)}.{latex(AC)}}}{{\\sqrt{{{AB**2}+{AB**2}}}}}={latex(AH)}$.")	
	
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


