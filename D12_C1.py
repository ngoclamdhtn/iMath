import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
 

def thay_heso_1x(st):
	ketqua=st.replace("1x^2","x^2").replace("-1x^2","-x^2").replace("1x^3","x^3").replace("-1x^3","-x^3")
	return ketqua

def check_so_nguyen(so):
    ketqua=False
    if isinstance(so, int):
        ketqua=True
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

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

# Xử lí trả về đáp án đúng để ghi câu Chọn đáp án
def tra_ve_dap_an(list_PA):
	st_A,st_B,st_C,st_D=list_PA[0],list_PA[1],list_PA[2],list_PA[3] 
	if "*" in st_A[0]: 
		dap_an="A"
	elif "*" in st_B[0]: 
		dap_an="B"
	elif "*" in st_C[0]: 
		dap_an="C"
	else:
		dap_an="D"   
	return dap_an

# Xử lí trả về đáp án đúng để ghi câu Chọn đáp án
def tra_ve_TF(list_PA):
    list_TF=[]
    for phan_tu in list_PA:
        if phan_tu[0]=="*":
            list_TF.append("đúng")
        else:
            list_TF.append("sai")
    return list_TF

def tim_ham_bac2_bac1():
	x=sp.symbols("x")
	x_1=random.choice([2*i for i in range(-10,10)])
	i=random.randint(1,5)
	x_2=x_1+2*i
	b, c, =(x_1+x_2), x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)
	f_ok=(f1*x-f1*x_0+c2)/(x-x_0)
	
	print(f"y={latex(f_ok)}")
	print(f"y'={latex(g)}")
	print(f"y'=0: x_1={x_1}, x_2={x_2}")
	return
def code_bbt_bac3_2nghiem(a,x_1,x_2,y_1,y_2):
    if a>0:
            code = f"\\begin{{tikzpicture}}\n \
            \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n \
            {{$x$ /0.7,$y'$ /0.7,$y$ /2}}\n \
            {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n \
            \\tkzTabLine{{,+,0,-,0,+,}} \n \
            \\tkzTabVar{{-/$-\\infty$ ,+/ ${y_1}$, -/ ${y_2}$ /, +/$+\\infty$ /}} \n\
            \\end{{tikzpicture}}\n"         
    else:
            code = f"\\begin{{tikzpicture}}\n \
            \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n \
            {{$x$ /0.7,$y'$ /0.7,$y$ /2}}\n \
            {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n \
            \\tkzTabLine{{,-,0,+,0,-,}} \n \
            \\tkzTabVar{{+/$+\\infty$ ,-/ ${y_1}$, +/ ${y_2}$ /, -/$-\\infty$ /}} \n\
            \\end{{tikzpicture}}\n"
    return code

def code_bbt_phanthucbac1(a,b,c,d):
    x_0 = phan_so(-d/c)
    y_0 = phan_so(a/c)
    if a*d-b*c<0:
        code =f"\\begin{{tikzpicture}}[scale=1]\n\
\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
{{$x$ /1,$y'$ /1,$y$ /2}}\n\
{{$-\\infty$,${x_0}$,$+\\infty$}}\n\
\\tkzTabLine{{,-, d ,-,}}\n\
\\tkzTabVar{{+/ ${y_0}$ / , -D+/ $-\\infty$ / $+\\infty$ , -/ ${y_0}$ /}}\n\
\\end{{tikzpicture}}\n"
    else:
        code =f"\\begin{{tikzpicture}}[scale=1]\n\
\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
{{$x$ /1,$y'$ /1,$y$ /2}}\n\
{{$-\\infty$,${x_0}$,$+\\infty$}}\n\
\\tkzTabLine{{,+, d ,+,}}\n\
\\tkzTabVar{{-/${y_0}$ / , +D-/ $+\\infty$ /$-\\infty$  , +/ ${y_0}$/}}\n\
\\end{{tikzpicture}}\n"
    return code

# Code latex bảng biến thiên phân thức bậc 2/1
def code_bbt_phanthucbac2(a,b,c,d,e):
    x=sp.symbols("x")
    x_0 = phan_so(-e/d)
    f=(a*x**2+b*x+c)/(d*x+e)
    g=diff(f,"x")
    equation=Eq(g,0)
    tap_nghiem=solve(equation,x)
    if "I" in str(tap_nghiem[0]):  
        if a>0:
            code =f"\\begin{{tikzpicture}}[scale=0.8]\n\
    \\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
    {{$x$ /1,$y'$ /1,$y$ /2}}\n\
    {{$-\\infty$,${x_0}$,$+\\infty$}}\n\
    \\tkzTabLine{{,+, d ,+,}}\n\
    \\tkzTabVar{{-/$-\\infty$ / , +D-/ $+\\infty$ /$-\\infty$  , +/ $+\\infty$/}}\n\
    \\end{{tikzpicture}}\n"
        else:
            code =f"\\begin{{tikzpicture}}[scale=0.8]\n\
    \\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
    {{$x$ /1,$y'$ /1,$y$ /2}}\n\
    {{$-\\infty$,${x_0}$,$+\\infty$}}\n\
    \\tkzTabLine{{,-, d ,-,}}\n\
    \\tkzTabVar{{+/ $+\\infty$ / , -D+/ $-\\infty$ / $+\\infty$ , -/ $-\\infty$ /}}\n\
    \\end{{tikzpicture}}\n"
    else:
        x_1,x_2=tap_nghiem[0],tap_nghiem[1]
        y_1=f.subs(x,x_1)
        y_2=f.subs(x,x_2)
        if check_so_nguyen(x_1):
            x_1=phan_so(x_1)
            x_2=phan_so(x_2)
        else:
            x_1=latex(x_1)
            x_2=latex(x_2)

        if check_so_nguyen(y_1):
            y_1=phan_so(y_1)
            y_2=phan_so(y_2)
        else:
            y_1=latex(y_1)
            y_2=latex(y_2)

        if a>0:
            code =f"\\begin{{tikzpicture}}[scale=0.8]\n\
    \\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
    {{$x$ /1,$y'$ /1,$y$ /2}}\n\
    {{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
\\tkzTabLine{{ ,+,z,-,d,-,z,+, }}\n\
\\tkzTabVar{{-/$-\\infty$,+/${y_1}$,-D+/$-\\infty$/$+\\infty$,-/${y_2}$,+/$+\\infty$}}\n\
    \\end{{tikzpicture}}\n"
        else:
            code =f"\\begin{{tikzpicture}}[scale=0.8]\n\
    \\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
    {{$x$ /1,$y'$ /1,$y$ /2}}\n\
    {{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
\\tkzTabLine{{ ,-,z,+,d,+,z,-, }}\n\
\\tkzTabVar{{+/$+\\infty$,-/${y_1}$,+D-/$+\\infty$/$-\\infty$,+/${y_2}$,-/$-\\infty$}}\n\
    \\end{{tikzpicture}}\n"
    return code

#Code vẽ đồ thị hàm số y=(ax^2+bx+c)/(dx+e)   
def code_dothi_phanthuc_bac2(a,b,c,d,e):
    x=sp.symbols("x")
    f=(a/d)*x+(-a*e+b*d)/d**2
    y_0=f.subs(x,-e/d)

    y_min,y_max=int(y_0)-15,int(y_0)+15    
    numbers = [f'{i}' for i in range(y_min+1, y_max) if (i!=0 and i%2==0 )]    
    chuoi_so_y = ','.join(numbers)

    x_min, x_max=int(-e/d)-8, int(-e/d)+8
    numbers = [f'{i}' for i in range(x_min+1, x_max) if (i!=0 and i%2==0)]    
    chuoi_so_x = ','.join(numbers)

    t_1=-e/d-0.1
    t_2=-e/d+0.1    
    code = f"\\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.4]\n\
\\tikzset{{every node/.style={{scale=0.9}}}}\n\
\\draw[gray!20]({x_min},{y_min})grid({x_max},{y_max});\n\
\\draw[->] ({x_min},0)--({x_max},0) node[below left] {{\\footnotesize $x$}};\n\
\\draw[->] (0,{y_min})--(0,{y_max}) node[below left] {{\\footnotesize $y$}};\n\
\\draw (0,0) node [below left] {{\\footnotesize $O$}};\n\
\\foreach \\x in {{{chuoi_so_x}}}\n\
    \\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {{\\footnotesize $\\x$}};\n\
\\foreach \\y in {{{chuoi_so_y}}}\n\
    \\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {{\\footnotesize $\\y$}};\n\
\\begin{{scope}}\n\
\\clip ({x_min},{y_min}) rectangle ({x_max},{y_max});\n\
\\draw[samples=100,domain={x_min}:{t_1},smooth,variable=\\x]\n\
plot (\\x,{{({a}*(\\x)^2+{b}*(\\x)+{c})/({d}*(\\x)+{e})}});\n\
\\draw[samples=100,domain={t_2}:{x_max},smooth,variable=\\x]\n\
plot (\\x,{{({a}*(\\x)^2+{b}*(\\x)+{c})/({d}*(\\x)+{e})}});\n\
\\draw[samples=100,domain={x_min}:{x_max},smooth,dashed,variable=\\x]\n\
plot (\\x,{{{a/d}*(\\x) + {(-a*e + b*d)/d**2}}});\n\
\\draw[dashed] ({-e/d},{y_min})--({-e/d},{y_max});\n\
\\end{{scope}}\n\
\\end{{tikzpicture}}\n"
    return code

#Code vẽ đồ thị hàm số bậc 3   
def code_dothi_bac_3(a,b,c,d):
    code = f"\\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.6]\n\
\\tikzset{{every node/.style={{scale=0.9}}}}\n\
\\draw[gray!20](-5,-5)grid(5,5);\n\
\\draw[->] (-5,0)--(5,0) node[below left] {{$x$}};\n\
\\draw[->] (0,-5)--(0,5) node[below left] {{$y$}};\n\
\\draw (0,0) node [below left] {{\\footnotesize $O$}};\n\
\\foreach \\x in {{-3,-2,-1,1,2,3}}\n\
\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {{\\footnotesize $\\x$}};\n\
\\foreach \\y in {{-3,-2,-1,1,2,3}}\n\
\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {{\\footnotesize $\\y$}};\n\
\\begin{{scope}}\n\
\\clip (-5,-5) rectangle (5,5);\n\
\\draw[samples=200,domain=-5:5,smooth,variable=\\x]\n\
plot (\\x,{{{a}*(\\x)^3+{b}*(\\x)^2+{c}*(\\x)+{d}}});\
\\end{{scope}}\n\
\\end{{tikzpicture}}\n"
    return  code

#Code vẽ đồ thị hàm số y=(ax+b)/(cx+d)
def code_dothi_phanthuc_bac1(a,b,c,d):
    x=sp.symbols("x")
    t_1=-d/c-0.1
    t_2=-d/c+0.1
    f=(a*x+b)/(c*x+d)
    x_0, y_0=-d/c, a/c
    x_min,x_max=int(x_0)-5, int(x_0)+5
    y_min, y_max=int(y_0)-5,int(y_0)+5
    if x_min>0: x_min=-1.5
    if x_max<0: x_max=1.5
    if y_min>0: y_min=-1.5
    if y_max<0: y_max=1.5

    numbers = [f'{i}' for i in range(x_min+1, x_max) if (i!=0 and i%2==0)]    
    chuoi_so_x = ','.join(numbers)
    numbers = [f'{i}' for i in range(y_min+1, y_max) if (i!=0 and i%2==0 )]    
    chuoi_so_y = ','.join(numbers)

    code = f"\\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.6]\n\
\\tikzset{{every node/.style={{scale=0.9}}}}\n\
\\draw[gray!20]({x_min},{y_min})grid({x_max},{y_max});\n\
\\draw[->] ({x_min},0)--({x_max},0) node[below left] {{$x$}};\n\
\\draw[->] (0,{y_min})--(0,{y_max}) node[below left] {{$y$}};\n\
\\draw (0,0) node [below left] {{\\footnotesize $O$}};\n\
\\foreach \\x in {{{chuoi_so_x}}}\n\
    \\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {{\\footnotesize $\\x$}};\n\
\\foreach \\y in {{{chuoi_so_y}}}\n\
    \\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {{\\footnotesize $\\y$}};\n\
\\begin{{scope}}\n\
\\clip ({x_min},{y_min}) rectangle ({x_max},{y_max});\n\
\\draw[samples=200,domain={x_min}:{t_1},smooth,variable=\\x]\n\
plot (\\x,{{({a}*(\\x)+{b})/({c}*(\\x)+{d})}});\n\
\\draw[samples=200,domain={t_2}:{x_max},smooth,variable=\\x]\n\
plot (\\x,{{({a}*(\\x)+{b})/({c}*(\\x)+{d})}});\n\
\\draw[dashed,samples=200,domain={x_min}:{x_max},smooth,variable=\\x]\n\
plot (\\x,{{({a/c}}});\n\
\\draw[dashed] ({-d/c},{y_min})--({-d/c},{y_max});\n\
\\end{{scope}}\n\
\\end{{tikzpicture}}\n"
    return  code

#Bài 1 - Sự đồng biến nghịch biến của hàm số
#[D12_C1_B1_01]-M2. Cho bảng biến thiên. Tìm khoảng đơn điệu
def prt_34_L12_C1_B1_01():
	chon=random.randint(1,3)	
	if chon==1:
		x_1 = random.randint(-5,5)
		x_2 = x_1 + random.randint(1,4)
		if x_2 == x_1: x_2 =x_1 +1
		a = random.choice([1,-1])
		y_1 = random.randint(-10,20)
		bien_thien = random.choice(["đồng biến","nghịch biến"])
		noi_dung=f'Cho hàm số $y=f(x)$ xác định với mọi $x\\in \\mathbb{{R}}$ có bảng biến thiên như hình vẽ dưới đây. Hàm số {bien_thien} trên khoảng nào trong các khoảng sau?'
		if a > 0:
			y_2 = y_1 - random.randint(1,10)			
			code_hinh = my_module.code_bbt_bac3_2nghiem(a,x_1,x_2,y_1,y_2)

			if bien_thien == "đồng biến":
				kq =   f"$({x_2};+\\infty)$"
				kq2 =  f"$({x_1};{x_2})$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_2})$"
			else:
				kq =   f"$({x_1};{x_2})$"
				kq2 =  f"$({x_2};+\\infty)$"
				kq3 =  f"$(-\\infty;{x_2})$"
				kq4 =  f"$(-\\infty;{x_1})$"

		else:
			y_2 = y_1 + random.randint(1,10)			
			code_hinh = my_module.code_bbt_bac3_2nghiem(a,x_1,x_2,y_1,y_2)

			if bien_thien == "đồng biến":
				kq =   f"$({x_1};{x_2})$"
				kq2 =  f"$({x_2};+\\infty)$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_1})$"
			else:
				kq =   f"$({x_2};+\\infty)$"
				kq2 =  f"$({x_1};{x_2})$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_2})$"
		noi_dung_loigiai=f"Hàm số đã cho {bien_thien} trên khoảng {kq}."
	if chon==2:
		a,b,c,d= [random.choice([random.randint(-10, -1), random.randint(1, 10)]) for _ in range(4)]
		if a*d-b*c==0:
			b=b+random.randint(1,3)		
		x_0=-d/c
		if a*d-b*c>0:
			noi_dung=f'Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {phan_so(x_0)}$ có bảng biến thiên như hình vẽ dưới đây. Hàm số đồng biến trên khoảng nào trong các khoảng sau?'
			kq=f'$({int(x_0+random.randint(1,4))};+\\infty)$'
			kq2=f'$(-\\infty;+\\infty)$'
			kq3=f'$(-\\infty;{int(x_0+random.randint(1,4))})$'
			kq4=f'$({int(x_0-random.randint(1,4))}; \\infty)$'				
			noi_dung_loigiai=f"Hàm số đã cho đồng biến trên khoảng {kq}."

		if a*d-b*c<0:
			noi_dung=f'Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {phan_so(x_0)}$ có bảng biến thiên như hình vẽ dưới đây. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?'
			kq=f'$({int(x_0+random.randint(1,4))};+\\infty)$'
			kq2=f'$(-\\infty;+\\infty)$'
			kq3=f'$(-\\infty;{int(x_0+random.randint(1,4))})$'
			kq4=f'$({int(x_0-random.randint(1,4))}; \\infty)$'				
			noi_dung_loigiai=f"Hàm số đã cho nghịch biến trên khoảng {kq}."
		code_hinh=code_bbt_phanthucbac1(a,b,c,d)
	if chon==3:
		x_1=random.randint(-7,1)
		x_0=x_1++random.randint(1,5)
		x_2=x_0+random.randint(1,8)
		a=random.choice([-1,1])		
		if a>0:
			y_1=random.randint(-20,10)
			y_2=y_1+random.randint(1,10)
			code_hinh =f"\\begin{{tikzpicture}}[scale=0.8]\n\
			\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
			{{$x$ /1,$y'$ /1,$y$ /2}}\n\
			{{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
			\\tkzTabLine{{ ,+,z,-,d,-,z,+, }}\n\
			\\tkzTabVar{{-/$-\\infty$,+/${y_1}$,-D+/$-\\infty$/$+\\infty$,-/${y_2}$,+/$+\\infty$}}\n\
			\\end{{tikzpicture}}\n"
		else:
			y_2=random.randint(-20,10)
			y_1=y_2+random.randint(1,10)
			code_hinh =f"\\begin{{tikzpicture}}[scale=0.8]\n\
				\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
				{{$x$ /1,$y'$ /1,$y$ /2}}\n\
				{{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
				\\tkzTabLine{{ ,-,z,+,d,+,z,-, }}\n\
				\\tkzTabVar{{+/$+\\infty$,-/${y_1}$,+D-/$+\\infty$/$-\\infty$,+/${y_2}$,-/$-\\infty$}}\n\
				\\end{{tikzpicture}}\n"
		chon=random.randint(1,2)
		if chon==1:
			noi_dung=f'Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {x_0}$ có bảng biến thiên như hình vẽ dưới đây. Hàm số đồng biến trên khoảng nào trong các khoảng sau?'
			if a>0:

				kq=random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq2=random.choice([f'$(-\\infty;{x_0})$',f'$(-\\infty;{x_2})$'])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
				f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
				f"Do đó hàm số đã cho đồng biến trên khoảng {kq}."

			if a<0:		
				kq=random.choice([f'$({x_1};{x_0})$', f'$({x_0};{x_2})$'])
				kq2= random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])				
					
				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
				f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
				f"Do đó hàm số đã cho đồng biến trên khoảng {kq}."

		if chon==2:
			noi_dung=f'Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {x_0}$ có bảng biến thiên như hình vẽ dưới đây. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?'
			if a>0:
				kq=random.choice([f'$({x_1};{x_0})$', f'$({x_0};{x_2})$'])
				kq2= random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
			f"Do đó hàm số đã cho nghịch biến trên khoảng {kq}."
			if a<0:
				kq=random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq2=random.choice([f'$(-\\infty;{x_0})$',f'$(-\\infty;{x_2})$'])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
				f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
				f"Do đó hàm số đã cho nghịch biến trên khoảng {kq}."			

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
	
	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"	

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_02]. Cho hàm số bậc 3. Tìm khoảng đồng biến, nghịch biến 
def prt_34_L12_C1_B1_02():
	x = sp.symbols('x')
	x_1 = random.randint(-2,2)
	x_2=x_1 + random.randint (1,4)

	#Tạo đa thức bậc hai nhận x_1,x_2 làm nghiệm
	a = random.randint(-3,3)
	if a==0:
	    a = random.randint(1,3)
	f=a*(x-x_1)*(x-x_2)

	#Tìm hàm bậc ba là nguyên hàm của f
	g=integrate(f, x) + random.randint(-10,10)

	bien_thien = random.choice(["đồng biến","nghịch biến"])
	if a>0:
		if bien_thien == "đồng biến":
				kq =   random.choice([f"$({x_2};+\\infty)$",f"$(-\\infty;{x_1})$"])
				kq2 =  f"$({x_1};{x_2})$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_2})$"
		else:
				kq =   f"$({x_1};{x_2})$"
				kq2 =  f"$({x_2};+\\infty)$"
				kq3 =  f"$(-\\infty;{x_2})$"
				kq4 =  f"$(-\\infty;{x_1})$"
		noi_dung_loigiai=f"$f'(x)={latex(diff(g,x))}$.\n\n"\
		f"$f'(x)=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số nghịch biến trên khoảng $({x_1};{x_2})$.\n\n"
		f"Do đó hàm số {bien_thien} trên khoảng {kq}."
	else:
		if bien_thien == "đồng biến":
				kq =   f"$({x_1};{x_2})$"
				kq2 =  f"$({x_2};+\\infty)$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_1})$"
		else:
				kq =   random.choice([f"$({x_2};+\\infty)$",f"$(-\\infty;{x_1})$"])
				kq2 =  f"$({x_1};{x_2})$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_2})$"

		noi_dung_loigiai=f"$f'(x)={latex(diff(g,x))}$.\n\n"\
		f"$f'(x)=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
		f"Hàm số đồng biến trên khoảng $({x_1};{x_2})$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$ .\n\n"
		f"Do đó hàm số {bien_thien} trên khoảng {kq}."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hàm số $y={latex(g)}$." \
		f" Hàm số {bien_thien} trên khoảng nào trong các khoảng sau đây?\n"

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

#[D12_C1_B1_03]-M2. Cho đồ thị bậc 4. Tìm khoảng đồng biến, nghịch biến. 
def prt_34_L12_C1_B1_03():
	chon=random.randint(1,4)
	if chon==1:
		x_0=random.randint(1,2)
		a, b, c = 1/4, -(x_0**2/2), random.randint(-3,3)
					
		code_hinh = my_module.code_dothi_bac_4(a,b,c)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name = my_module.pdftoimage_timename(code)
		don_dieu=random.choice(["đồng biến", "nghịch biến"])

		noi_dung = f"Cho hàm số bậc bốn $y=f(x)$ có đồ thị là đường cong trong hình dưới đây."\
		f" Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"
		if don_dieu=="đồng biến":
			kq=random.choice([f"$({-x_0};0)$", f"$({x_0};+\\infty)$", f"$({x_0+random.randint(1,3)};+\\infty)$"])
			kq2=f"$(-\\infty;{-x_0-random.randint(1,3)})$"
			kq3=f"$(0;{x_0})$"
			kq4=f"$({-x_0-random.randint(1,5)};{x_0})$"			

		if don_dieu=="nghịch biến":
			kq=random.choice([f"$(-\\infty;{-x_0-random.randint(1,3)})$", f"$(-\\infty;{-x_0})$", f"$(0;{x_0})$"])
			kq2=f"$({-x_0};0)$"
			kq3=f"$({x_0+random.randint(1,5)};+\\infty)$"
			kq4=f"$({-x_0};{x_0+random.randint(1,5)})$"
			
	
	if chon==2:
		x_0=random.randint(1,2)
		a, b, c = -1/4, x_0**2/2, random.randint(-3,3)
					
		code_hinh = my_module.code_dothi_bac_4(a,b,c)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name = my_module.pdftoimage_timename(code)
		don_dieu=random.choice(["đồng biến", "nghịch biến"])

		noi_dung = f"Cho hàm số bậc bốn $y=f(x)$ có đồ thị là đường cong trong hình dưới đây."\
		f" Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"
		if don_dieu=="đồng biến":

			kq=random.choice([f"$(-\\infty;{-x_0-random.randint(1,3)})$", f"$(-\\infty;{-x_0})$", f"$(0;{x_0})$"])
			kq2=f"$({-x_0};0)$"
			kq3=f"$({x_0+random.randint(1,5)};+\\infty)$"
			kq4=f"$({-x_0};{x_0+random.randint(1,5)})$"

		if don_dieu=="nghịch biến":
			kq=random.choice([f"$({-x_0};0)$", f"$({x_0};+\\infty)$", f"$({x_0+random.randint(1,3)};+\\infty)$"])
			kq2=f"$(-\\infty;{-x_0-random.randint(1,3)})$"
			kq3=f"$(0;{x_0})$"
			kq4=f"$({-x_0-random.randint(1,5)};{x_0})$"
	
	if chon==3:
		x_0=0
		a, b, c = 1, random.randint(1,3), random.randint(-3,3)
					
		code_hinh = my_module.code_dothi_bac_4(a,b,c)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name = my_module.pdftoimage_timename(code)
		don_dieu=random.choice(["đồng biến", "nghịch biến"])

		noi_dung = f"Cho hàm số bậc bốn $y=f(x)$ có đồ thị là đường cong trong hình dưới đây."\
		f" Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"
		if don_dieu=="đồng biến":

			kq=random.choice([f"$(0;+\\infty)$", f"$({random.randint(1,10)};+\\infty)$"])
			kq2=f"$(-\\infty;0)$"
			kq3=f"$(-\\infty;{random.randint(1,5)})$"
			kq4=f"$({-random.randint(1,5)};{random.randint(1,5)})$"

		if don_dieu=="nghịch biến":
			kq=random.choice([f"$(-\\infty;0)$", f"$(-\\infty;{random.randint(-10,-1)})$"])
			kq2=f"$(0;+\\infty)$" 
			kq3=f"$({random.randint(1,10)};+\\infty)$"
			kq4=f"$({-random.randint(1,5)};{random.randint(1,5)})$"
	
	if chon==4:
		x_0=0
		a, b, c = -1, random.randint(-3,-1), random.randint(-3,3)
					
		code_hinh = my_module.code_dothi_bac_4(a,b,c)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name = my_module.pdftoimage_timename(code)
		don_dieu=random.choice(["đồng biến", "nghịch biến"])

		noi_dung = f"Cho hàm số bậc bốn $y=f(x)$ có đồ thị là đường cong trong hình dưới đây."\
		f" Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"
		if don_dieu=="đồng biến":
			kq=random.choice([f"$(-\\infty;0)$", f"$(-\\infty;{random.randint(-10,-1)})$"])
			kq2=f"$(0;+\\infty)$" 
			kq3=f"$({random.randint(1,10)};+\\infty)$"
			kq4=f"$({-random.randint(1,5)};{random.randint(1,5)})$"		

		if don_dieu=="nghịch biến":
			kq=random.choice([f"$(0;+\\infty)$", f"$({random.randint(1,10)};+\\infty)$"])
			kq2=f"$(-\\infty;0)$"
			kq3=f"$(-\\infty;{random.randint(1,5)})$"
			kq4=f"$({-random.randint(1,5)};{random.randint(1,5)})$"

	noi_dung_loigiai=f"Hàm số đã cho {don_dieu} trên khoảng {kq}."

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
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"Hàm số đã cho {don_dieu} trên khoảng nào?"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_04]-M2. Cho hàm số y=(ax+b)/(cx+d). Tìm khoảng đơn điệu. 
def prt_34_L12_C1_B1_04():
	x=sp.symbols("x")
	a,b,c,d= [random.choice([random.randint(-10, -1), random.randint(1, 10)]) for _ in range(4)]
	if a*d-b*c==0:
		b=b+random.randint(1,3)
	f=(a*x+b)/(c*x+d)
	x_0=-d/c
	if a*d-b*c>0:
		noi_dung=f'Cho hàm số $y={latex(f)}$. Hàm số đồng biến trên khoảng nào trong các khoảng sau?'
		kq=f'$({int(x_0+random.randint(1,4))};+\\infty)$'
		kq2=f'$(-\\infty;+\\infty)$'
		kq3=f'$(-\\infty;{int(x_0+random.randint(1,4))})$'
		kq4=f'$({int(x_0-random.randint(1,4))}; +\\infty)$'	
			
		noi_dung_loigiai=f"$y'=\\dfrac{{{a*d-b*c}}}{{\\left({latex(c*x+d)}\\right)^2}}>0, \\forall x \\ne {phan_so(-d/c)}$.\n\n"\
		f"Hàm số đã cho đồng biến trên khoảng {kq}."

	if a*d-b*c<0:
		noi_dung=f'Cho hàm số $y={latex(f)}$. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?'
		kq=f'$({int(x_0+random.randint(1,4))};+\\infty)$'
		kq2=f'$(-\\infty;+\\infty)$'
		kq3=f'$(-\\infty;{int(x_0+random.randint(1,4))})$'
		kq4=f'$({int(x_0-random.randint(1,4))}; +\\infty)$'	
			
		noi_dung_loigiai=f"$y'=\\dfrac{{{a*d-b*c}}}{{\\left({latex(c*x+d)}\\right)^2}}<0, \\forall x \\ne {phan_so(-d/c)}$.\n\n"\
		f"Hàm số đã cho nghịch biến trên khoảng {kq}."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
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

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_05]-M2. Cho hàm số y=(ax^2+bx+c)/(dx+e). Tìm khoảng đơn điệu. 
def prt_34_L12_C1_B1_05():
	x=sp.symbols("x")
	x_1=random.choice([2*i for i in range(-6,6)])
	i=random.randint(1,5)
	x_2=x_1+2*i
	b, c, =(x_1+x_2), x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)
	
	a=random.choice([-1,1,-2,2])
	f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)

	chon=random.randint(1,2)	
	if chon==1:
		noi_dung=f'Cho hàm số $y={latex(f_ok)}$. Hàm số đồng biến trên khoảng nào trong các khoảng sau?'
		if a>0:
			kq=random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
			kq2=random.choice([f'$(-\\infty;{x_0})$',f'$(-\\infty;{x_2})$'])
			kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
			kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
			f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
			f"Do đó hàm số đã cho đồng biến trên khoảng {kq}."

		if a<0:		
			kq=random.choice([f'$({x_1};{x_0})$', f'$({x_0};{x_2})$'])
			kq2= random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
			kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
			kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])
				
			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
			f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
			f"Do đó hàm số đã cho đồng biến trên khoảng {kq}."
			
	if chon==2:
		noi_dung=f'Cho hàm số $y={latex(f_ok)}$. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?'
		if a>0:
			kq=random.choice([f'$({x_1};{x_0})$', f'$({x_0};{x_2})$'])
			kq2= random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
			kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
			kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó hàm số đã cho nghịch biến trên khoảng {kq}."

		if a<0:
			kq=random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
			kq2=random.choice([f'$(-\\infty;{x_0})$',f'$(-\\infty;{x_2})$'])
			kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
			kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
			f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
			f"Do đó hàm số đã cho nghịch biến trên khoảng {kq}."			
		


	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
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

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_06]-M2. Cho đồ thị bậc 3. Tìm khoảng đồng biến, nghịch biến. 
def prt_34_L12_C1_B1_06():
	x=sp.symbols("x")
	dau=random.choice(['+','-'])
	if dau=='+':
		chon=random.randint(1,5)
		if chon==1:
			a,b,c,d=1,-3,0,random.randint(-2,2)
			x_1,x_2=0,2
		if chon==2:
			a,b,c,d=1,0,-3,random.randint(-2,3)
			x_1,x_2=-1,1
		if chon==3:
			a,b,c,d=1/3,3/2,2,random.randint(-3,3)
			x_1,x_2=-2,-1
		if chon==4:
			a,b,c,d=1/3,-2,3,random.randint(-3,3)
			x_1,x_2=1,3
		if chon==5:
			a,b,c,d=1/3,1/2,0,random.randint(-3,3)
			x_1,x_2=-1,0

		don_dieu=random.choice(["đồng biến", "nghịch biến"])

		noi_dung = f"Cho hàm số $y=f(x)$ là hàm số bậc ba có đồ thị là đường cong trong hình dưới đây."\
		f" Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"
		if don_dieu=="đồng biến":
			kq=random.choice([f"$(-\\infty;{x_1-random.randint(1,3)})$", f"$({x_2+random.randint(1,3)};+\\infty)$"])
			kq2=f"$({x_1};{x_2})$" 
			kq3=f"$(-\\infty;{x_2})$"
			kq4=f"$({x_1};+\\infty)$"
		if don_dieu=="nghịch biến":
			kq=random.choice([f"$({x_1};{x_2})$"])
			kq2=random.choice([f"$(-\\infty;{x_1-random.randint(1,3)})$", f"$({x_2+random.randint(1,3)};+\\infty)$"])
			kq3=f"$(-\\infty;{x_2})$"
			kq4=f"$({x_1};+\\infty)$"

		noi_dung_loigiai=f"Dựa vào đồ thị ta thấy hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$,"\
		f" nghịch biến trên khoảng $({x_1};{x_2})$.\n\n"\
		f"Do đó, hàm số đã cho {don_dieu} trên khoảng {kq}."

	if dau=='-':
		chon=random.randint(1,5)		
		if chon==1:
			a,b,c,d=-1,3,0,random.randint(-2,2)
			x_1,x_2=0,2
		if chon==2:
			a,b,c,d=-1,0,3,random.randint(-2,3)
			x_1,x_2=-1,1
		if chon==3:
			a,b,c,d=-1/3,-3/2,-2,random.randint(-3,3)
			x_1,x_2=-2,-1
		if chon==4:
			a,b,c,d=-1/3,2,-3,random.randint(-3,3)
			x_1,x_2=1,3
		if chon==5:
			a,b,c,d=-1/3,-1/2,0,random.randint(-3,3)
			x_1,x_2=-1,0

		don_dieu=random.choice(["đồng biến", "nghịch biến"])

		noi_dung = f"Cho hàm số $y=f(x)$ là hàm số bậc ba có đồ thị là đường cong trong hình dưới đây."\
		f" Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"
		if don_dieu=="đồng biến":
			kq=random.choice([f"$({x_1};{x_2})$"])
			kq2=random.choice([f"$(-\\infty;{x_1-random.randint(1,3)})$", f"$({x_2+random.randint(1,3)};+\\infty)$"])
			kq3=f"$(-\\infty;{x_2})$"
			kq4=f"$({x_1};+\\infty)$"			
		if don_dieu=="nghịch biến":
			kq=random.choice([f"$(-\\infty;{x_1-random.randint(1,3)})$", f"$({x_2+random.randint(1,3)};+\\infty)$"])
			kq2=f"$({x_1};{x_2})$" 
			kq3=f"$(-\\infty;{x_2})$"
			kq4=f"$({x_1};+\\infty)$"			

		noi_dung_loigiai=f"Dựa vào đồ thị ta thấy hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$,"\
		f" đồng biến trên khoảng $({x_1};{x_2})$.\n\n"\
		f"Do đó, hàm số đã cho {don_dieu} trên khoảng {kq}."

	code_hinh = my_module.code_dothi_bac_3(a,b,c,d)	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

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
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"Hàm số đã cho {don_dieu} trên khoảng nào?"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_07]-M2. Cho hàm số f'(x). Tìm khoảng đơn điệu
def prt_34_L12_C1_B1_07():
	x=sp.symbols("x")
	a,b,c,d =[random.choice([random.randint(-5, -1), random.randint(1, 5)]) for _ in range(4)]
	if -b/a==-d/c: d=d+1
	f=(a*x+b)*(c*x+d)

	if -b/a<-d/c: 
		x_1, x_2=-b/a,-d/c
	else:
		x_1, x_2=-d/c,-b/a


	don_dieu=random.choice(["đồng biến", "nghịch biến"])

	noi_dung = f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có đạo hàm $f'(x)={latex(f)}$."\
	f" Hàm số đã cho {don_dieu} trên khoảng nào dưới đây?"
	if a*c>0:
		if don_dieu=="đồng biến":
			kq=random.choice([f"$(-\\infty;{int(x_1)-random.randint(1,3)})$", f"$({int(x_2)+random.randint(1,3)};+\\infty)$"])
			kq2=f"$\\left( {phan_so(x_1)};{phan_so(x_2)} \\right)$" 
			kq3=f"$\\left( -\\infty;{phan_so(x_2)} \\right)$"
			kq4=f"$\\left({phan_so(x_1)};+\\infty  \\right)$"

		if don_dieu=="nghịch biến":
			kq=random.choice([f"$\\left( {phan_so(x_1)};{phan_so(x_2)} \\right)$"])
			kq2=random.choice([f"$(-\\infty;{int(x_1)-random.randint(1,3)})$", f"$({int(x_2)+random.randint(1,3)};+\\infty)$"])
			kq3=f"$\\left( -\\infty;{phan_so(x_2)} \\right)$"
			kq4=f"$\\left( {phan_so(x_1)};+\\infty \\right)$"

		noi_dung_loigiai=f"$f'(x)=0 \\Leftrightarrow x={phan_so(x_1)},x={phan_so(x_2)}$.\n\n"\
		f"Dựa vào bảng xét dấu ta thấy hàm số đồng biến trên các khoảng $(-\\infty;{phan_so(x_1)})$ và $({phan_so(x_2)};+\\infty)$,"\
		f" nghịch biến trên khoảng $({phan_so(x_1)};{phan_so(x_2)})$.\n\n"\
		f"Do đó, hàm số đã cho {don_dieu} trên khoảng {kq}."

	if a*c<0:
		if don_dieu=="đồng biến":
			kq=random.choice([f"$\\left( {phan_so(x_1)};{phan_so(x_2)} \\right)$"])
			kq2=random.choice([f"$(-\\infty;{int(x_1)-random.randint(1,3)})$", f"$({int(x_2)+random.randint(1,3)};+\\infty)$"])
			kq3=f"$\\left( -\\infty;{phan_so(x_2)} \\right)$"
			kq4=f"$\\left( {phan_so(x_1)};+\\infty \\right)$"

		if don_dieu=="nghịch biến":
			kq=random.choice([f"$(-\\infty;{int(x_1)-random.randint(1,3)})$", f"$({int(x_2)+random.randint(1,3)};+\\infty)$"])
			kq2=f"$\\left( {phan_so(x_1)};{phan_so(x_2)} \\right)$" 
			kq3=f"$\\left( -\\infty;{phan_so(x_2)} \\right)$"
			kq4=f"$\\left({phan_so(x_1)};+\\infty  \\right)$"

		noi_dung_loigiai=f"$f'(x)=0 \\Leftrightarrow x={phan_so(x_1)},x={phan_so(x_2)}$.\n\n"\
		f"Dựa vào bảng xét dấu ta thấy hàm số nghịch biến trên các khoảng $(-\\infty;{phan_so(x_1)})$ và $({phan_so(x_2)};+\\infty)$,"\
		f" đồng biến trên khoảng $({phan_so(x_1)};{phan_so(x_2)})$.\n\n"\
		f"Do đó, hàm số đã cho {don_dieu} trên khoảng {kq}."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n\n" 
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
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

#[D12_C1_B1_08]-M2. Cho bảng xét dấu. Tìm khoảng đơn điệu
def prt_34_L12_C1_B1_08():
	chon=random.randint(1,3)
	
	if chon==1:
		x_1 = random.randint(-5,5)
		x_2 = x_1 + random.randint(1,4)
		if x_2 == x_1: x_2 =x_1 +1
		a = random.choice([1,-1])

		bien_thien = random.choice(["đồng biến","nghịch biến"])
		noi_dung=f"Cho hàm số $y=f(x)$ xác định với mọi $x\\in \\mathbb{{R}}$ và có bảng xét dấu $f'(x)$ như hình vẽ dưới đây. Hàm số {bien_thien} trên khoảng nào trong các khoảng sau?"
		if a > 0:	
			code_hinh = f"\\begin{{tikzpicture}}\n \
            \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n \
            {{$x$ /0.7,$y'$ /0.7}}\n \
            {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n \
            \\tkzTabLine{{,+,0,-,0,+,}} \n \
            \\end{{tikzpicture}}\n"         

			if bien_thien == "đồng biến":
				kq =   f"$({x_2};+\\infty)$"
				kq2 =  f"$({x_1};{x_2})$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_2})$"
			else:
				kq =   f"$({x_1};{x_2})$"
				kq2 =  f"$({x_2};+\\infty)$"
				kq3 =  f"$(-\\infty;{x_2})$"
				kq4 =  f"$(-\\infty;{x_1})$"

		if a < 0:						
			code_hinh = f"\\begin{{tikzpicture}}\n \
            \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n \
            {{$x$ /0.7,$y'$ /0.7}}\n \
            {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n \
            \\tkzTabLine{{,-,0,+,0,-,}} \n \
            \\end{{tikzpicture}}\n"

			if bien_thien == "đồng biến":
				kq =   f"$({x_1};{x_2})$"
				kq2 =  f"$({x_2};+\\infty)$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_1})$"
			else:
				kq =   f"$({x_2};+\\infty)$"
				kq2 =  f"$({x_1};{x_2})$"
				kq3 =  f"$({x_1};+\\infty)$"
				kq4 =  f"$(-\\infty;{x_2})$"
		noi_dung_loigiai=f"Hàm số đã cho {bien_thien} trên khoảng {kq}."

	if chon==2:
			
		x_0=random.randint(-8,8)
		chon=random.choice(["+","-"])
		if chon=="-":		
			noi_dung=f"Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {x_0}$ và có bảng xét dấu $f'(x)$ như hình vẽ dưới đây. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?"
			kq=random.choice([f'$(-\\infty;{x_0-random.randint(1,4)})$', f'$({x_0+random.randint(1,4)};+\\infty)$'])
			kq2=f'$(-\\infty;+\\infty)$'
			kq3=f'$(-\\infty;{int(x_0+random.randint(1,4))})$'
			kq4=f'$({int(x_0-random.randint(1,4))}; +\\infty)$'				
			noi_dung_loigiai=f"Hàm số đã cho nghịch biến trên khoảng {kq}."
			code_hinh =f"\\begin{{tikzpicture}}[scale=1]\n\
					\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
					{{$x$ /1,$y'$ /1}}\n\
					{{$-\\infty$,${phan_so(x_0)}$,$+\\infty$}}\n\
					\\tkzTabLine{{,-, d ,-,}}\n\
					\\end{{tikzpicture}}\n" 
   
		if chon=="+":
			noi_dung=f"Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {x_0}$ và có bảng xét dấu $f'(x)$ như hình vẽ dưới đây. Hàm số đồng biến trên khoảng nào trong các khoảng sau?"
			kq=random.choice([f'$(-\\infty;{x_0-random.randint(1,4)})$', f'$({x_0+random.randint(1,4)};+\\infty)$'])
			kq2=f'$(-\\infty;+\\infty)$'
			kq3=f'$(-\\infty;{x_0+random.randint(1,4)})$'
			kq4=f'$({x_0-random.randint(1,4)}; +\\infty)$'				
			noi_dung_loigiai=f"Hàm số đã cho đồng biến trên khoảng {kq}."
			code_hinh =f"\\begin{{tikzpicture}}[scale=1]\n\
					\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
					{{$x$ /1,$y'$ /1}}\n\
					{{$-\\infty$,${phan_so(x_0)}$,$+\\infty$}}\n\
					\\tkzTabLine{{,+, d ,+,}}\n\
					\\end{{tikzpicture}}\n"
	if chon==3:
		x_1=random.randint(-7,1)
		x_0=x_1++random.randint(1,5)
		x_2=x_0+random.randint(1,8)
		a=random.choice([-1,1])		
		if a>0:
			code_hinh =f"\\begin{{tikzpicture}}[scale=0.8]\n\
			\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
			{{$x$ /1,$y'$ /1}}\n\
			{{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
			\\tkzTabLine{{ ,+,z,-,d,-,z,+, }}\n\
			\\end{{tikzpicture}}\n"
		else:
			code_hinh =f"\\begin{{tikzpicture}}[scale=0.8]\n\
				\\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
				{{$x$ /1,$y'$ /1}}\n\
				{{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
				\\tkzTabLine{{ ,-,z,+,d,+,z,-, }}\n\
				\\end{{tikzpicture}}\n"
		chon=random.randint(1,2)
		if chon==1:
			noi_dung=f"Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {x_0}$ và có bảng xét dấu $f'(x)$ như hình vẽ dưới đây. Hàm số đồng biến trên khoảng nào trong các khoảng sau?"
			if a>0:

				kq=random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq2=random.choice([f'$(-\\infty;{x_0})$',f'$(-\\infty;{x_2})$'])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
				f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
				f"Do đó hàm số đã cho đồng biến trên khoảng {kq}."

			if a<0:		
				kq=random.choice([f'$({x_1};{x_0})$', f'$({x_0};{x_2})$'])
				kq2= random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])				
					
				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
				f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
				f"Do đó hàm số đã cho đồng biến trên khoảng {kq}."

		if chon==2:
			noi_dung=f"Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {x_0}$ và có bảng xét dấu $f'(x)$ như hình vẽ dưới đây. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?"
			if a>0:
				kq=random.choice([f'$({x_1};{x_0})$', f'$({x_0};{x_2})$'])
				kq2= random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
				f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
				f"Do đó hàm số đã cho nghịch biến trên khoảng {kq}."

			if a<0:
				kq=random.choice([f'$({x_2};+\\infty)$', f'$(-\\infty; {x_1})$', f'$({x_2+random.randint(1,4)};+\\infty)$', f'$(-\\infty; {x_1-random.randint(1,4)})$' ])
				kq2=random.choice([f'$(-\\infty;{x_0})$',f'$(-\\infty;{x_2})$'])
				kq3=random.choice([f'$({x_1};{x_2})$', f'$({x_1-random.randint(1,3)};{x_2+random.randint(1,3)})$'])
				kq4=random.choice([f'$({x_0}; +\\infty)$',f'$({x_1}; +\\infty)$'])

				noi_dung_loigiai=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
				f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
				f"Do đó hàm số đã cho nghịch biến trên khoảng {kq}."

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)


	debai= f"{noi_dung}\n\n"\
	f"\n{file_name}\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_09]-M2. Tìm m để hàm số bậc 3 đơn điệu trên R
def prt_34_L12_C1_B1_09():
	x=sp.symbols("x")
	m=sp.symbols("m")
	a =  random.choice([random.randint(-5, -1), random.randint(1, 5)])        
	b=random.randint(-5, 5) 
	c= random.randint(-5, 5)
	a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

	delta= (m+b)**2-4*a*(a_m*m+c)
	delta= expand((m+b)**2-4*a*(a_m*m+c))
	a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

	kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
	kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
	kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
	kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
	while any([kq==kq2, kq==kq3, kq==kq4, kq2==kq3, kq2==kq4, kq3==kq4]):
		a =  random.choice([random.randint(-5, -1), random.randint(1, 5)])        
		b=random.randint(-5, 5) 
		c= random.randint(-5, 5)
		a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

		delta= (m+b)**2-4*a*(a_m*m+c)
		delta= expand((m+b)**2-4*a*(a_m*m+c))
		a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

		kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
		kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
		kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
		kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
	#Tạo dấu bất phương trình 
	if a>0:        	
	    dau="\\ge 0"
	    don_dieu="đồng biến"
	else:
	    dau="\\le 0"
	    don_dieu="nghịch biến"

	f=thay_heso_1x(f"{a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})")
	g=thay_heso_1x(f"{phan_so(a/3)}x^3 + \\left(\\dfrac{{{m+b}}}{{2}}\\right)x^2 + \\left({latex(a_m*m+c)}\\right)x+({latex(random.randint(-7,7)*m+random.randint(-7,-1))})")

	delta= (m+b)**2-4*a*(a_m*m+c)

	delta= expand((m+b)**2-4*a*(a_m*m+c))

	a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

	noi_dung=f"Cho hàm số $f(x)={g}$. Tìm tất cả các giá trị của tham số ${{m}}$ để hàm số đã cho {don_dieu} trên khoảng $(-\\infty;+\\infty)$."

	kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
	kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
	kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
	kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")

	tich_4a=show_tich(4,a)

	noi_dung_loigiai=f"Ta có: $f'(x)= {f}$ {don_dieu} trên khoảng $(-\\infty;+\\infty)$\n\n $\\Leftrightarrow {f} {dau}$ với mọi $x\\in \\mathbb{{R}}$.\n\n"\
	f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
	f"${f} {dau}$ với mọi $x\\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta \\le 0$\n\n"\
	f"$\\Rightarrow {latex(delta)} \\le 0 \\Rightarrow$ {kq}.".replace("$1x^2","$x^2")


	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)


	debai= f"{noi_dung}\n\n"


	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

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

#[D12_C1_B1_10]-M4. Cho đồ thị f'(x). Tìm khoảng đơn điệu f(x)
def prt_34_L12_C1_B1_10():
	x=sp.symbols("x")
	x_1=random.randint(-5,1)
	x_2=x_1+random.randint(1,3)
	x_3=x_2+random.randint(1,3)
	chon=random.randint(1,2)	
	
	if chon==1:
		f_dh=(x-x_1)*(x-x_2)*(x-x_3)
		lenh_ve=f"plot (\\x,{{0.2*(\\x-{x_1})*(\\x-{x_2})*(\\x-{x_3})}});"
	if chon==2:
		f_dh=-(x-x_1)*(x-x_2)*(x-x_3)
		lenh_ve=f"plot (\\x,{{-0.2*(\\x-{x_1})*(\\x-{x_2})*(\\x-{x_3})}});"

	g=diff(f_dh,x)
	equation=Eq(g,0)
	solution = solve(equation, x)
	a,b=solution[0],solution[1]
	y_a,y_b=f_dh.subs(x,a),f_dh.subs(x,b)
	x_min, x_max= round(min(a,b)-3,1), round(max(a,b)+3,1)
	if x_max<=0: x_max=1.5
	if x_min>=0: x_min=-1.5
	y_min, y_max=round(0.5*min(y_a,y_b)-1,1), round(0.5*max(y_a,y_b)+1,1)
	chuoi_so_x=f"\\foreach \\x in {{{x_1}, {x_2},{x_3}}}\n"

	if x_1==0:
		chuoi_so_x=f"\\foreach \\x in {{{x_2},{x_3}}}\n"
	if x_2==0:
		chuoi_so_x=f"\\foreach \\x in {{{x_1},{x_3}}}\n"
	if x_3==0:
		chuoi_so_x=f"\\foreach \\x in {{{x_1},{x_2}}}\n"

	code_hinh=f"\\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.6]\n\
\\tikzset{{every node/.style={{scale=0.9}}}}\n\
\\draw[gray!20]({x_min},{y_min})grid({x_max},{y_max});\n\
\\draw[->] ({x_min},0)--({x_max},0) node[below left] {{$x$}};\n\
\\draw[->] (0,{y_min})--(0,{y_max}) node[below left] {{$y$}};\n\
\\draw (0,0) node [below left] {{\\footnotesize $O$}};\n\
{chuoi_so_x}\
\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {{\\footnotesize $\\x$}};\n\
\\foreach \\y in {{}}\n\
\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {{\\footnotesize $\\y$}};\n\
\\begin{{scope}}\n\
\\clip ({x_min},{y_min}) rectangle ({x_max},{y_max});\n\
\\draw[samples=200,domain={x_1-1}:{x_3+1},smooth,magenta, variable=\\x]\n\
{lenh_ve}\
\\end{{scope}}\n\
\\end{{tikzpicture}}\n"

	don_dieu=random.choice(["đồng biến", "nghịch biến"])
	noi_dung=f"Cho hàm số $f(x)$ liên tục trên $\\mathbb{{R}}$ có đồ thị $f'(x)$ như hình sau. Hàm số $y=f(x)$ {don_dieu} trên khoảng nào dưới đây?"
	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	if chon==1:
		if don_dieu=="đồng biến":
			kq=random.choice([f"({x_1};{x_2})", f"({x_3};+\\infty)"])
			kq2=f"(-\\infty;{x_1})"
			kq3=f"({x_2};{x_3})"
			kq4=f"({x_2};+\\infty)"
		if don_dieu=="nghịch biến":
			kq=random.choice([f"(-\\infty;{x_1})", f"({x_2};{x_3})"])
			kq2=random.choice([f"({x_1};{x_2})", f"({x_3};+\\infty)"])
			kq3=f"({x_3};+\\infty)"
			kq4=f"({x_2};+\\infty)"

		noi_dung_loigiai=f"Dựa vào đồ thị $f'(x)$ ta thấy:\n\n"\
		f"$f'(x)<0$ khi $x \\in (-\\infty;{x_1})$ hoặc $x \\in ({x_2};{x_3})$.\n\n"\
		f"$f'(x)>0$ khi $x\\in ({x_1};{x_2})$ hoặc $x \\in ({x_3};+\\infty)$.\n\n"\
		f"Do đó $f(x)$ {don_dieu} trên khoảng ${kq}$."

	if chon==2:
		if don_dieu=="nghịch biến":
			kq=random.choice([f"({x_1};{x_2})", f"({x_3};+\\infty)"])
			kq2=f"(-\\infty;{x_1})"
			kq3=f"({x_2};{x_3})"
			kq4=f"({x_2};+\\infty)"
		if don_dieu=="đồng biến":
			kq=random.choice([f"(-\\infty;{x_1})", f"({x_2};{x_3})"])
			kq2=random.choice([f"({x_1};{x_2})", f"({x_3};+\\infty)"])
			kq3=f"({x_3};+\\infty)"
			kq4=f"({x_2};+\\infty)"

		noi_dung_loigiai=f"Dựa vào đồ thị $f'(x)$ ta thấy:\n\n"\
		f"$f'(x)>0$ khi $x \\in (-\\infty;{x_1})$ hoặc $x \\in ({x_2};{x_3})$.\n\n"\
		f"$f'(x)<0$ khi $x\\in ({x_1};{x_2})$ hoặc $x \\in ({x_3};+\\infty)$.\n\n"\
		f"Do đó $f(x)$ {don_dieu} trên khoảng ${kq}$."


	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)


	debai= f"{noi_dung}\n\n"\
	f'{file_name}'

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#ĐÚNG -SAI
#[D12_C1_B1_11]-TF-M2. Cho bảng xét dấu f'(x). Xét đúng-sai:đồng biến, nghịch biến, so sánh giá trị.	
def prt_34_L12_C1_B1_11():
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,4)
	x_3= x_2 + random.randint(1,5)
	chon=random.randint(1,2)
	if chon==1:

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,+,0,-,0,+,0,-,}} \n \
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"

		khoang_db=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
		khoang_db_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
		kq1_T=f'*Hàm số đồng biến trên khoảng {khoang_db}' 
		kq1_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
		
		loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq1==kq1_F:
			loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		khoang_nb=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
		khoang_nb_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

		kq2_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}'
		kq2_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		kq3_T=f'*${so_sanh}$' 
		kq3_F=f'${so_sanh_false}$'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f''
		loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq3==kq3_F:
			loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a=random.randint(1,6)
		b=random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x=sp.symbols("x")
		f=a*x+b
		nghiem=random.choice([phan_so((x_1-b)/a), phan_so((x_2-b)/a), phan_so((x_3-b)/a)])
		nghiem_false=random.choice([phan_so((x_1+b)/a), phan_so((x_2+b)/a), phan_so((x_3+b)/a)])

		kq4_T=f"*Phương trình $f'({latex(f)})=0$ nhận $x={nghiem}$ làm nghiệm"
		kq4_F=f"Phương trình $f'({latex(f)})=0$ nhận $x={nghiem_false}$ làm nghiệm"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f'(x)=0 \\Leftrightarrow x={x_1},x={x_2},x={x_3}$. Do đó:\n\n"\
		f"$f'({latex(f)})=0 \\Leftrightarrow {latex(f)}={x_1}$ hoặc ${latex(f)}={x_2}$ hoặc ${latex(f)}={x_3}$.\n\n"\
		f"Suy ra $x={phan_so((x_1-b)/a)}$ hoặc $x={phan_so((x_2-b)/a)}$ hoặc $x={phan_so((x_3-b)/a)}$."
		loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq4==kq4_F:
			loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	if chon==2:

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,-,0,+,0,-,0,+,}} \n \
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"

		khoang_nb=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
		khoang_nb_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
		kq1_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}' 
		kq1_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
		
		loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq1==kq1_F:
			loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		khoang_db=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
		khoang_db_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

		kq2_T=f'*Hàm số đồng biến trên khoảng {khoang_db}'
		kq2_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		kq3_T=f'*${so_sanh}$' 
		kq3_F=f'${so_sanh_false}$'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f''
		loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq3==kq3_F:
			loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a=random.randint(1,6)
		b=random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x=sp.symbols("x")
		f=a*x+b
		nghiem=random.choice([phan_so((x_1-b)/a), phan_so((x_2-b)/a), phan_so((x_3-b)/a)])
		nghiem_false=random.choice([phan_so((x_1+b)/a), phan_so((x_2+b)/a), phan_so((x_3+b)/a)])

		kq4_T=f"*Phương trình $f'({latex(f)})=0$ nhận $x={nghiem}$ làm nghiệm"
		kq4_F=f"Phương trình $f'({latex(f)})=0$ nhận $x={nghiem_false}$ làm nghiệm"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f'(x)=0 \\Leftrightarrow x={x_1},x={x_2},x={x_3}$. Do đó:\n\n"\
		f"$f'({latex(f)})=0 \\Leftrightarrow {latex(f)}={x_1}$ hoặc ${latex(f)}={x_2}$ hoặc ${latex(f)}={x_3}$.\n\n"\
		f"Suy ra $x={phan_so((x_1-b)/a)}$ hoặc $x={phan_so((x_2-b)/a)}$ hoặc $x={phan_so((x_3-b)/a)}$."
		loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq4==kq4_F:
			loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n\n"\
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
	
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")


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
		st=list_PA[i]
		if st[0]=="*":
			st_new=f"\\True " + st[1:]
			list_PA[i]=st_new

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"\\choiceTFt\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"
	print(dap_an)

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B1_12]-TF-M2. Cho bảng xét dấu f'(x). Xét đúng-sai:đơn điệu, so sánh, cực trị.	
def prt_34_L12_C1_B1_12():
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,4)
	x_3= x_2 + random.randint(1,5)
	chon=random.randint(1,2)
	
	if chon==1:

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,+,0,-,0,+,0,-,}} \n \
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"
		chon = random.randint(1,2)
		if chon==1:

			khoang_db=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
			khoang_db_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
			kq1_T=f'*Hàm số đồng biến trên khoảng {khoang_db}' 
			kq1_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
			
			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'
		if chon==2:

			khoang_nb=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
			khoang_nb_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

			kq1_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}'
			kq1_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		kq2_T=f'*${so_sanh}$' 
		kq2_F=f'${so_sanh_false}$'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f''
		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		if chon==1:
			kq3_T=f'*Điểm cực tiểu của hàm số đã cho là $x={x_2}$' 
			kq3_F=f'Điểm cực tiểu của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$'
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực tiểu tại điểm $x={x_2}$.'
			loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq3==kq3_F:
				loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq4_T=f"*$f({random.choice([{x_1}, {x_3}])})$ là giá trị cực đại của hàm số đã cho"
			kq4_F=f"$f({x_2})$ là giá trị cực đại của hàm số đã cho" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Dựa vào bảng biến thiên, hàm số đã cho có giá trị cực đại là $f({x_1})$ hoặc $f({x_3})$"
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==2:
			kq3_T=f'*Điểm cực đại của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$' 
			kq3_F=f'Điểm cực đại của hàm số đã cho là $x={x_2}$'
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực đại tại điểm $x={x_1}$ hoặc $x={x_3}$.'
			loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq3==kq3_F:
				loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq4_T=f"*$f({x_2})$ là giá trị cực tiểu của hàm số đã cho"
			kq4_F=f"$f({random.choice([{x_1}, {x_3}])})$ là giá trị cực tiểu của hàm số đã cho" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Dựa vào bảng biến thiên, hàm số đã cho có giá trị cực tiểu là $f({x_2})$"
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==2:

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,-,0,+,0,-,0,+,}} \n \
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"
		chon = random.randint(1,2)
		if chon==1:

			khoang_nb=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
			khoang_nb_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
			kq1_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}' 
			kq1_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
			
			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'
		
		if chon==2:
			khoang_db=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
			khoang_db_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])
			kq1_T=f'*Hàm số đồng biến trên khoảng {khoang_db}'
			kq1_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		kq2_T=f'*${so_sanh}$' 
		kq2_F=f'${so_sanh_false}$'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f''
		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		if chon==1:
			kq3_T=f'*Điểm cực đại của hàm số đã cho là $x={x_2}$' 
			kq3_F=f'Điểm cực đại của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$'
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực đại tại điểm $x={x_2}$.'
			loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq3==kq3_F:
				loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq4_T=f"*$f({random.choice([{x_1}, {x_3}])})$ là giá trị cực tiểu của hàm số đã cho"
			kq4_F=f"$f({x_2})$ là giá trị cực tiểu của hàm số đã cho" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Dựa vào bảng biến thiên, hàm số đã cho có giá trị cực tiểu là $f({x_1})$ hoặc $f({x_3})$"
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==2:
			kq3_T=f'*Điểm cực tiểu của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$' 
			kq3_F=f'Điểm cực tiểu của hàm số đã cho là $x={x_2}$'
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực tiểu tại điểm $x={x_1}$ hoặc $x={x_3}$.'
			loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq3==kq3_F:
				loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq4_T=f"*$f({x_2})$ là giá trị cực đại của hàm số đã cho"
			kq4_F=f"$f({random.choice([{x_1}, {x_3}])})$ là giá trị cực đại của hàm số đã cho" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Dựa vào bảng biến thiên, hàm số đã cho có giá trị cực đại là $f({x_2})$"
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n\n"\
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
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"\\choiceTFt\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B1_13]-TF-M2. Cho bảng biến thiên. Xét đúng-sai:đồng biến, nghịch biến, so sánh giá trị.	
def prt_34_L12_C1_B1_13():
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,4)
	x_3= x_2 + random.randint(1,5)
	chon=random.randint(1,2)	
	if chon==1:
		y_2 = random.randint(-15,15)
		y_1 = y_2 + random.randint(1,10)
		y_3= y_2 + random.randint(1,10)

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7, $f(x)$ /2}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,+,0,-,0,+,0,-,}} \n \
		\\tkzTabVar{{-/$-\\infty$ ,+/${y_1}$,-/${y_2}$,+/${y_3}$,-/$-\\infty$}}\n\
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng biến thiên như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"

		khoang_db=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
		khoang_db_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
		kq1_T=f'*Hàm số đồng biến trên khoảng {khoang_db}' 
		kq1_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
		
		loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq1==kq1_F:
			loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		khoang_nb=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
		khoang_nb_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

		kq2_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}'
		kq2_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		kq3_T=f'*${so_sanh}$' 
		kq3_F=f'${so_sanh_false}$'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f''
		loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq3==kq3_F:
			loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a=random.randint(1,6)
		b=random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x=sp.symbols("x")
		f=a*x+b
		nghiem=random.choice([phan_so((x_1-b)/a), phan_so((x_2-b)/a), phan_so((x_3-b)/a)])
		nghiem_false=random.choice([phan_so((x_1+b)/a), phan_so((x_2+b)/a), phan_so((x_3+b)/a)])

		kq4_T=f"*Phương trình $f'({latex(f)})=0$ nhận $x={nghiem}$ làm nghiệm"
		kq4_F=f"Phương trình $f'({latex(f)})=0$ nhận $x={nghiem_false}$ làm nghiệm"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f'(x)=0 \\Leftrightarrow x={x_1},x={x_2},x={x_3}$. Do đó:\n\n"\
		f"$f'({latex(f)})=0 \\Leftrightarrow {latex(f)}={x_1}$ hoặc ${latex(f)}={x_2}$ hoặc ${latex(f)}={x_3}$.\n\n"\
		f"Suy ra $x={phan_so((x_1-b)/a)}$ hoặc $x={phan_so((x_2-b)/a)}$ hoặc $x={phan_so((x_3-b)/a)}$."
		loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq4==kq4_F:
			loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	if chon==2:
		y_2 = random.randint(-15,15)
		y_1 = y_2 - random.randint(1,10)
		y_3= y_2 - random.randint(1,10)

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7, $f(x)$ /2}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,-,0,+,0,-,0,+,}} \n \
		\\tkzTabVar{{+/$+\\infty$ ,-/${y_1}$,+/${y_2}$,-/${y_3}$,+/$+\\infty$}}\n\
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"

		khoang_nb=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
		khoang_nb_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
		kq1_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}' 
		kq1_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
		
		loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq1==kq1_F:
			loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		khoang_db=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
		khoang_db_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

		kq2_T=f'*Hàm số đồng biến trên khoảng {khoang_db}'
		kq2_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		kq3_T=f'*${so_sanh}$' 
		kq3_F=f'${so_sanh_false}$'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f''
		loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq3==kq3_F:
			loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a=random.randint(1,6)
		b=random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x=sp.symbols("x")
		f=a*x+b
		nghiem=random.choice([phan_so((x_1-b)/a), phan_so((x_2-b)/a), phan_so((x_3-b)/a)])
		nghiem_false=random.choice([phan_so((x_1+b)/a), phan_so((x_2+b)/a), phan_so((x_3+b)/a)])

		kq4_T=f"*Phương trình $f'({latex(f)})=0$ nhận $x={nghiem}$ làm nghiệm"
		kq4_F=f"Phương trình $f'({latex(f)})=0$ nhận $x={nghiem_false}$ làm nghiệm"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f'(x)=0 \\Leftrightarrow x={x_1},x={x_2},x={x_3}$. Do đó:\n\n"\
		f"$f'({latex(f)})=0 \\Leftrightarrow {latex(f)}={x_1}$ hoặc ${latex(f)}={x_2}$ hoặc ${latex(f)}={x_3}$.\n\n"\
		f"Suy ra $x={phan_so((x_1-b)/a)}$ hoặc $x={phan_so((x_2-b)/a)}$ hoặc $x={phan_so((x_3-b)/a)}$."
		loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq4==kq4_F:
			loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n\n"\
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
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"\\choiceTFt\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B1_14]-TF-M2. Cho bảng biến thiên. Xét đúng-sai:đồng biến, nghịch biến, so sánh giá trị.	
def prt_34_L12_C1_B1_14():
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,4)
	x_3= x_2 + random.randint(1,5)
	chon=random.randint(1,2)
	if chon==1:

		y_2 = random.randint(-15,15)
		y_1 = y_2 + random.randint(1,10)
		y_3= y_2 + random.randint(1,10)

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7, $f(x)$ /2}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,+,0,-,0,+,0,-,}} \n \
		\\tkzTabVar{{-/$-\\infty$ ,+/${y_1}$,-/${y_2}$,+/${y_3}$,-/$-\\infty$}}\n\
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng biến thiên như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"

		khoang_db=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
		khoang_db_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
		kq1_T=f'*Hàm số đồng biến trên khoảng {khoang_db}' 
		kq1_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
		
		loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq1==kq1_F:
			loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		khoang_nb=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
		khoang_nb_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

		kq2_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}'
		kq2_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		kq3_T=f'*${so_sanh}$' 
		kq3_F=f'${so_sanh_false}$'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f''
		loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq3==kq3_F:
			loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a=random.randint(1,6)
		b=random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x=sp.symbols("x")
		f=a*x+b
		nghiem=random.choice([phan_so((x_1-b)/a), phan_so((x_2-b)/a), phan_so((x_3-b)/a)])
		nghiem_false=random.choice([phan_so((x_1-b)/(2*a)), phan_so((x_2+b)/(2*a)), phan_so((x_3+b)/(2*a))])

		kq4_T=f"*Phương trình $f'({latex(f)})=0$ nhận $x={nghiem}$ làm nghiệm"
		kq4_F=f"Phương trình $f'({latex(f)})=0$ nhận $x={nghiem_false}$ làm nghiệm"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f'(x)=0 \\Leftrightarrow x={x_1},x={x_2},x={x_3}$. Do đó:\n\n"\
		f"$f'({latex(f)})=0 \\Leftrightarrow {latex(f)}={x_1}$ hoặc ${latex(f)}={x_2}$ hoặc ${latex(f)}={x_3}$.\n\n"\
		f"Suy ra $x={phan_so((x_1-b)/a)}$ hoặc $x={phan_so((x_2-b)/a)}$ hoặc $x={phan_so((x_3-b)/a)}$."
		loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq4==kq4_F:
			loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	if chon==2:

		y_2 = random.randint(-15,15)
		y_1 = y_2 - random.randint(1,10)
		y_3= y_2 - random.randint(1,10)

		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7, $f(x)$ /2}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,-,0,+,0,-,0,+,}} \n \
		\\tkzTabVar{{+/$+\\infty$ ,-/${y_1}$,+/${y_2}$,-/${y_3}$,+/$+\\infty$}}\n\
		\\end{{tikzpicture}}\n"    

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)  			

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng biến thiên như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"

		khoang_nb=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
		khoang_nb_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
		kq1_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}' 
		kq1_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
		
		loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq1==kq1_F:
			loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		khoang_db=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
		khoang_db_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

		kq2_T=f'*Hàm số đồng biến trên khoảng {khoang_db}'
		kq2_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

		loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq2==kq2_F:
			loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		so_sanh=random.choice([f"f({x_1})<f({x_2})", f"f({x_3})<f({x_2})",f"f({x_1-random.randint(1,3)})>f({x_1})", f"f({x_3+random.randint(1,3)})>f({x_3})"])
		so_sanh_false=random.choice([f"f({x_1})>f({x_2})", f"f({x_3})>f({x_2})",f"f({x_1-random.randint(1,3)})<f({x_1})", f"f({x_3+random.randint(1,3)})<f({x_3})"])
		kq3_T=f'*${so_sanh}$' 
		kq3_F=f'${so_sanh_false}$'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f''
		loigiai_3=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq3==kq3_F:
			loigiai_3=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a=random.randint(1,6)
		b=random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x=sp.symbols("x")
		f=a*x+b
		nghiem=random.choice([phan_so((x_1-b)/a), phan_so((x_2-b)/a), phan_so((x_3-b)/a)])
		nghiem_false=random.choice([phan_so((x_1+b)/(2*a)), phan_so((x_2+b)/(2*a)), phan_so((x_3+b)/(2*a))])

		kq4_T=f"*Phương trình $f'({latex(f)})=0$ nhận $x={nghiem}$ làm nghiệm"
		kq4_F=f"Phương trình $f'({latex(f)})=0$ nhận $x={nghiem_false}$ làm nghiệm"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f'(x)=0 \\Leftrightarrow x={x_1},x={x_2},x={x_3}$. Do đó:\n\n"\
		f"$f'({latex(f)})=0 \\Leftrightarrow {latex(f)}={x_1}$ hoặc ${latex(f)}={x_2}$ hoặc ${latex(f)}={x_3}$.\n\n"\
		f"Suy ra $x={phan_so((x_1-b)/a)}$ hoặc $x={phan_so((x_2-b)/a)}$ hoặc $x={phan_so((x_3-b)/a)}$."
		loigiai_4=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
		if kq4==kq4_F:
			loigiai_4=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n\n"\
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
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"\\choiceTFt\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,dap_an

# CỰC TRỊ CỦA HÀM SỐ

#[D12_C1_B1_15]. Cho bảng biến thiên bậc 3. Tìm điểm cực trị. 
def prt_34_L12_C1_B1_15():
		x_1 = random.randint(-10,10)
		x_2 = x_1 + random.randint(1,5)
		if x_2 == x_1: x_2 =x_1 +1
		a = random.choice([1,-1])
		y_1 = random.randint(-10,20)
		diem_cuc_tri = random.choice(["điểm cực đại","điểm cực tiểu"])
		if a > 0:
			y_2 = y_1 - random.randint(1,10)
			
			code_hinh = my_module.code_bbt_bac3_2nghiem(a,x_1,x_2,y_1,y_2)

			if diem_cuc_tri == "điểm cực đại":

				kq =   x_1
				kq2 =  x_2
				kq3 =  y_1
				kq4 =  y_2
			else:
				kq =   x_2
				kq2 =  x_1
				kq3 =  y_1
				kq4 =  y_2

		else:
			y_2 = y_1 + random.randint(1,10)
			
			code_hinh = my_module.code_bbt_bac3_2nghiem(a,x_1,x_2,y_1,y_2)

			if diem_cuc_tri == "điểm cực đại":
				kq =   x_2
				kq2 =  x_1
				kq3 =  y_1
				kq4 = y_2
			else:
				kq =  x_1
				kq2 =  x_2
				kq3 =  y_1
				kq4 = y_2
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

		pa_A= f"*$x={kq}$"
		pa_B= f"$x={kq2}$"
		pa_C= f"$x={kq3}$"
		pa_D= f"$x={kq4}$"
		#Trộn các phương án
		list_PA =[pa_A, pa_B, pa_C, pa_D]
		random.shuffle(list_PA)
		noi_dung = f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng biến thiên như hình vẽ sau." 
		

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		dap_an=my_module.tra_ve_dap_an(list_PA)
		noi_dung_loigiai=f"{diem_cuc_tri} của hàm số $y=f(x)$ là $x={kq}$."

		debai= f"{noi_dung}\n\n"\
		f"{file_name}\n" \
		f"Tìm {diem_cuc_tri} của hàm số $y=f(x)$.\n"
		phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
		
		loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
		loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

		#Tạo đề latex
		for i in range(4):
			list_PA[i]=list_PA[i].replace("*","\\True ")    

		debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"Tìm {diem_cuc_tri} của hàm số $y=f(x)$.\n"\
		f"\\choice\n"\
			f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
			f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
			f"\\end{{ex}}\n"

		latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"Tìm {diem_cuc_tri} của hàm số $y=f(x)$.\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
			f"\\end{{ex}}\n"
		return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_16]. Cho bảng biến thiên bậc 3. Tìm giá trị cực trị. 
def prt_34_L12_C1_B1_16():
		x_1 = random.randint(-5,5)
		x_2 = x_1 + random.randint(1,5)
		
		a = random.choice([1,-1])
		y_1 = random.randint(-10,20)
		gtri_cuc_tri = random.choice(["giá trị cực đại","giá trị cực tiểu"])
		if a > 0:
			y_2 = y_1 - random.randint(1,20)			
			code_hinh = my_module.code_bbt_bac3_2nghiem(a,x_1,x_2,y_1,y_2)

			if gtri_cuc_tri == "giá trị cực đại":
				kq =   y_1
				kq2 =  y_2
				kq3 =  x_1
				kq4 =  x_2
			else:
				kq =   y_2
				kq2 =  y_1
				kq3 =  x_1
				kq4 =  x_2

		else:
			y_2 = y_1 + random.randint(1,20)			
			code_hinh = my_module.code_bbt_bac3_2nghiem(a,x_1,x_2,y_1,y_2)

			if gtri_cuc_tri == "giá trị cực đại":
				kq =   y_2
				kq2 =  y_1
				kq3 =  x_1
				kq4 =  x_2
			else:
				kq =   y_1
				kq2 =  y_2
				kq3 =  x_1
				kq4 =  x_2
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)
		

		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]
		
		pa_A= f"*$y={kq}$"
		pa_B= f"$y={kq2}$"
		pa_C= f"$y={kq3}$"
		pa_D= f"$y={kq4}$"
		#Trộn các phương án
		list_PA =[pa_A, pa_B, pa_C, pa_D]
		random.shuffle(list_PA)
		noi_dung = f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng biến thiên như hình vẽ sau."
		
		dap_an=my_module.tra_ve_dap_an(list_PA)
		

		debai= f"{noi_dung}\n\n"\
		f"{file_name}\n" \
		f"Tìm {gtri_cuc_tri} của hàm số $y=f(x)$.\n"

		phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
		noi_dung_loigiai=f"{gtri_cuc_tri} của hàm số $y=f(x)$ là {kq}."
		
		loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
		loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

		#Tạo đề latex
		for i in range(4):
			list_PA[i]=list_PA[i].replace("*","\\True ")    

		debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"Tìm {gtri_cuc_tri} của hàm số $y=f(x)$.\n"\
		f"\\choice\n"\
			f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
			f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
			f"\\end{{ex}}\n"

		latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"Tìm {gtri_cuc_tri} của hàm số $y=f(x)$.\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
			f"\\end{{ex}}\n"
		return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_17]. Cho hàm số bậc 3. Tìm điểm cực trị. 
def prt_34_L12_C1_B1_17():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,3)
	a, b=-(x_1+x_2), x_1*x_2	
	m=random.choice([1,-1,3,-3,6,-6])
	f_dh= m*(x**2+a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)
	diem_cuc_tri=random.choice(["Điểm cực tiểu", "Điểm cực đại"])

	noi_dung = f"Cho hàm số $y=f(x)={latex(f)}$. {diem_cuc_tri} của hàm số đã cho là"
	if m>0:
		if diem_cuc_tri=="Điểm cực tiểu":
			kq=f"$x={x_2}$"
			kq2=f"$x={x_1}$"
			kq3=f"$x={x_1-random.randint(1,5)}$"
			kq4=f"$x={x_2+random.randint(1,5)}$"

		if diem_cuc_tri=="Điểm cực đại":
			kq=f"$x={x_1}$"
			kq2=f"$x={x_2}$"
			kq3=f"$x={x_1-random.randint(1,5)}$"
			kq4=f"$x={x_2+random.randint(1,5)}$"
	if m<0:
		if diem_cuc_tri=="Điểm cực tiểu":
			kq=f"$x={x_1}$"
			kq2=f"$x={x_2}$"
			kq3=f"$x={x_1-random.randint(1,5)}$"
			kq4=f"$x={x_2+random.randint(1,5)}$"			

		if diem_cuc_tri=="Điểm cực đại":
			kq=f"$x={x_2}$"
			kq2=f"$x={x_1}$"
			kq3=f"$x={x_1-random.randint(1,5)}$"
			kq4=f"$x={x_2+random.randint(1,5)}$"

	noi_dung_loigiai=f"$f'(x)={latex(f_dh)}$.\n\n"\
	f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"\
	f"Lập bảng biến thiên.\n\n"\
	f"{diem_cuc_tri} của hàm số là {kq}."	
	
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_18]. Cho hàm số bậc 3. Tìm giá trị cực trị. 
def prt_34_L12_C1_B1_18():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,3)
	a, b=-(x_1+x_2), x_1*x_2	
	m=random.choice([1,-1,3,-3,6,-6])
	f_dh= m*(x**2+a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)
	diem_cuc_tri=["Điểm cực tiểu", "Điểm cực đại"]
	gia_tri_cuc_tri=["Giá trị cực tiểu", "Giá trị cực đại"]
	i=random.randint(0,1)
	diem_cuc_tri, gia_tri_cuc_tri = diem_cuc_tri[i], gia_tri_cuc_tri[i]

	noi_dung = f"Cho hàm số $y=f(x)={latex(f)}$. {gia_tri_cuc_tri} của hàm số đã cho là"
	if m>0:
		if gia_tri_cuc_tri=="Giá trị cực tiểu":
			x_ct=x_2
			kq=f"${{{phan_so(f.subs(x,x_2))}}}$"
			kq2=f"${{{phan_so(f.subs(x,x_1))}}}$"
			kq3=f"${{{x_1}}}$"
			kq4=f"${{{x_2}}}$"

		if gia_tri_cuc_tri=="Giá trị cực đại":
			x_ct=x_1
			kq=f"${{{phan_so(f.subs(x,x_1))}}}$"
			kq2=f"${{{phan_so(f.subs(x,x_2))}}}$"
			kq3=f"${{{x_1}}}$"
			kq4=f"${{{x_2}}}$"
	if m<0:
		if gia_tri_cuc_tri=="Giá trị cực tiểu":
			x_ct=x_1
			kq=f"${{{phan_so(f.subs(x,x_1))}}}$"
			kq2=f"${{{phan_so(f.subs(x,x_2))}}}$"
			kq3=f"${{{x_1}}}$"
			kq4=f"${{{x_2}}}$"

		if gia_tri_cuc_tri=="Giá trị cực đại":
			x_ct=x_2
			kq=f"${{{phan_so(f.subs(x,x_2))}}}$"
			kq2=f"${{{phan_so(f.subs(x,x_1))}}}$"
			kq3=f"${{{x_1}}}$"
			kq4=f"${{{x_2}}}$"

	noi_dung_loigiai=f"$f'(x)={latex(f_dh)}$.\n\n"\
	f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"\
	f"Lập bảng biến thiên.\n\n"\
	f"{diem_cuc_tri} của hàm số là $x={x_ct}$.\n\n"\
	f"{gia_tri_cuc_tri} của hàm số là $f({x_ct})=${kq}."
	
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_19]-M2. Cho hàm số y=(ax^2+bx+c)/(dx+e). Tìm điểm cực trị. 
def prt_34_L12_C1_B1_19():
	x=sp.symbols("x")
	x_1=random.choice([2*i for i in range(-10,10)])
	i=random.randint(1,5)
	x_2=x_1+2*i
	b, c=(x_1+x_2), x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)
	
	a=random.choice([-1,1,-2,2])
	f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)
	chon=random.randint(1,2)
	
	if chon==1:
		noi_dung=f'Cho hàm số $y={latex(f_ok)}$. Điểm cực tiểu của hàm số đã cho là'
		if a>0:
			kq=f"$x={x_2}$"
			kq2=f"$x={x_1}$"
			kq3=f"$x={x_2+random.randint(1,5)}$"
			kq4=f"$x={x_1-random.randint(1,5)}$"

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực tiểu tại {kq}."

		if a<0:		
			kq=f"$x={x_1}$"
			kq2=f"$x={x_2}$"
			kq3=f"$x={x_2+random.randint(1,5)}$"
			kq4=f"$x={x_1-random.randint(1,5)}$"
			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực tiểu tại {kq}."				
		
	if chon==2:
		noi_dung=f'Cho hàm số $y={latex(f_ok)}$. Điểm cực đại của hàm số đã cho là'
		if a>0:
			kq=f"$x={x_1}$"
			kq2=f"$x={x_2}$"
			kq3=f"$x={x_2+random.randint(1,5)}$"
			kq4=f"$x={x_1-random.randint(1,5)}$"

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực tiểu tại {kq}."		

		if a<0:
			kq=f"$x={x_2}$"
			kq2=f"$x={x_1}$"
			kq3=f"$x={x_2+random.randint(1,5)}$"
			kq4=f"$x={x_1-random.randint(1,5)}$"

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực tiểu tại {kq}."		

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
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

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_20]-M2. Cho hàm số y=(ax^2+bx+c)/(dx+e). Tìm giá trị cực trị. 
def prt_34_L12_C1_B1_20():
	x=sp.symbols("x")
	x_1=random.choice([2*i for i in range(-10,10)])
	i=random.randint(1,5)
	x_2=x_1+2*i
	b, c, =(x_1+x_2), x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)
	
	a=random.choice([-1,1,-2,2])
	f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)
	chon=random.randint(1,2)	
	if chon==1:
		noi_dung=f'Cho hàm số $y={latex(f_ok)}$. Giá trị cực tiểu của hàm số đã cho là'
		if a>0:
			kq=f_ok.subs(x,x_2)
			kq2=f_ok.subs(x,x_1)
			kq3=x_1
			kq4=x_2

			pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
			kq2=pa_kotrung[1]
			kq3=pa_kotrung[2]
			kq4=pa_kotrung[3]

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực tiểu tại $x={x_2}$. Giá trị cực tiểu là $f({x_2})={phan_so(kq)}$."

		if a<0:		
			kq=f_ok.subs(x,x_1)
			kq2=f_ok.subs(x,x_2)
			kq3=x_1
			kq4=x_2
			
			pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
			kq2=pa_kotrung[1]
			kq3=pa_kotrung[2]
			kq4=pa_kotrung[3]
			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực tiểu tại $x={x_1}$. Giá trị cực tiểu là $f({x_1})={phan_so(kq)}$."			
		
	if chon==2:
		noi_dung=f'Cho hàm số $y={latex(f_ok)}$. Giá trị cực đại của hàm số đã cho là'
		if a>0:
			kq=f_ok.subs(x,x_1)
			kq2=f_ok.subs(x,x_2)
			kq3=x_1
			kq4=x_2
			
			pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
			kq2=pa_kotrung[1]
			kq3=pa_kotrung[2]
			kq4=pa_kotrung[3]

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực đại tại $x={x_1}$. Giá trị cực đại là $f({x_1})={phan_so(kq)}$."		

		if a<0:
			kq=f_ok.subs(x,x_2)
			kq2=f_ok.subs(x,x_1)
			kq3=x_1
			kq4=x_2

			pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
			kq2=pa_kotrung[1]
			kq3=pa_kotrung[2]
			kq4=pa_kotrung[3]

			noi_dung_loigiai=f"$y'={latex(a*g)}$.\n\n"\
		f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"\
		f"Do đó đạt cực đại tại $x={x_2}$. Giá trị cực đại là $f({x_2})={phan_so(kq)}$."	

	pa_A= f"*${{{phan_so(kq)}}}$"
	pa_B= f"${{{phan_so(kq2)}}}$"
	pa_C= f"${{{phan_so(kq3)}}}$"
	pa_D= f"${{{phan_so(kq4)}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
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

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_21]-M2. Tìm khoảng đơn điệu của các hàm số khác: y=căn(u), y=e^u
def prt_34_L12_C1_B1_21():
	x=sp.symbols("x")
	x_1=random.randint(-6,6)
	x_2=x_1+random.randint(2,5)
	a = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	f=a*(x-x_1)*(x-x_2)
	b=a*(-x_1-x_2)
	c=a*x_1*x_2
	x_0=-b/(2*a)
	chon=random.randint(1,3)	
	if chon==1:
		#y=căn(ax^2+bx+c)
		g=sqrt(a*x**2+b*x+c)
		chon=random.choice(["đồng biến", "nghịch biến"])
		dao_ham=f"\\dfrac{{{latex(2*a*x+b)}}}{{ \\sqrt{{{latex(expand(f))}}}}}"
		if chon=="đồng biến":
			noi_dung=f'Cho hàm số $y={latex(sqrt(expand(f)))}$. Hàm số {chon} trên khoảng nào trong các khoảng sau?'
			if a>0:
				kq=f'$({int(x_2)+random.randint(0,5)};+\\infty)$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$(-\\infty;{int(x_0)-random.randint(0,5)})$'
				kq4=f'$({x_1}; {x_2})$'	
					
				noi_dung_loigiai=f"Hàm số xác định khi: ${latex(expand(a*(x-x_1)*(x-x_2)))}\\ge 0 \\Leftrightarrow x\\in (-\\infty;{x_1}] \\cup [{x_2};+\\infty)$.\n\n"\
				f"$f'(x)={latex(diff(g,x))}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $({phan_so(x_2)};+\\infty)$ và nghịch biến trên khoảng $(-\\infty; {phan_so(x_1)})$.\n\n"\
				f"Do đó hàm số {chon} trên khoảng {kq}."
			if a<0:				
				kq=f'$({x_1};{phan_so(x_0)})$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$({int(x_0)+random.randint(1,5)};+\\infty)$'
				kq4=f'$({x_1}; {x_2})$'	
					
				noi_dung_loigiai=f"Hàm số xác định khi ${latex(expand(a*(x-x_1)*(x-x_2)))}\\ge 0 \\Leftrightarrow {x_1}\\le x \\le {x_2}$.\n\n"\
				f"$f'(x)={latex(diff(g,x))}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $({x_1}; {phan_so(x_0)})$ và nghịch biến trên khoảng $({phan_so(x_0)};{x_2})$.\n\n"\
				f"Do đó hàm số nghịch biến trên khoảng {kq}."

		if chon=="nghịch biến":
			noi_dung=f'Cho hàm số $y={latex(sqrt(expand(f)))}$. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?'
			if a>0:
				kq=f'$(-\\infty;{int(x_1)-random.randint(0,5)})$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$({int(x_0)+random.randint(0,5)};+\\infty)$'
				kq4=f'$({x_1}; {x_2})$'
					
				noi_dung_loigiai=f"Hàm số xác định khi ${latex(expand(a*(x-x_1)*(x-x_2)))}\\ge 0 \\Leftrightarrow x\\in (-\\infty;{x_1}] \\cup [{x_2};+\\infty)$.\n\n"\
				f"$f'(x)={latex(diff(g,x))}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $({phan_so(x_2)};+\\infty)$ và nghịch biến trên khoảng $(-\\infty; {phan_so(x_1)})$.\n\n"\
				f"Do đó hàm số nghịch biến trên khoảng {kq}."
			if a<0:				
				kq=f'$({phan_so(x_0)};{x_2})$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$(-\\infty;{int(x_0)-random.randint(0,5)})$'
				kq4=f'$({x_1}; {x_2})$'	
								
				noi_dung_loigiai=f"Hàm số xác định khi ${latex(expand(a*(x-x_1)*(x-x_2)))}\\ge 0 \\Leftrightarrow {x_1}\\le x \\le {x_2}$.\n\n"\
				f"$f'(x)={latex(diff(g,x))}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $({x_1}; {phan_so(x_0)})$ và nghịch biến trên khoảng $({phan_so(x_0)};{x_2})$.\n\n"\
				f"Do đó hàm số nghịch biến trên khoảng {kq}."
	if chon==2:
		chon=random.choice(["đồng biến", "nghịch biến"])
		dao_ham=f"({latex(2*a*x+b)})e^{{{latex(expand(f))}}}"
		if chon=="đồng biến":
			noi_dung=f'Cho hàm số $y={latex(exp(expand(f)))}$. Hàm số đồng biến trên khoảng nào trong các khoảng sau?'
			if a>0:
				kq=f'$({phan_so(x_0+random.randint(0,5))};+\\infty)$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$(-\\infty;{phan_so(x_0-random.randint(0,5))})$'
				kq4=f'$({x_1}; {x_2})$'	
					
				noi_dung_loigiai=f"Hàm số xác định trên $\\mathbb{{R}}$.\n\n"\
				f"$f'(x)={dao_ham}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $({phan_so(x_0)};+\\infty)$ và nghịch biến trên khoảng $(-\\infty; {phan_so(x_0)})$.\n\n"\
				f"Do đó hàm số đồng biến trên khoảng {kq}."
			if a<0:
				kq=f'$(-\\infty;{phan_so(x_0-random.randint(0,5))})$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$({phan_so(x_0+random.randint(0,5))};+\\infty)$'
				kq4=f'$({x_1}; {x_2})$'	
					
				noi_dung_loigiai=f"Hàm số xác định trên $\\mathbb{{R}}$.\n\n"\
				f"$f'(x)={dao_ham}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $(-\\infty; {phan_so(x_0)})$ và nghịch biến trên khoảng $({phan_so(x_0)};+\\infty)$.\n\n"\
				f"Do đó hàm số đồng biến trên khoảng {kq}."

		if chon=="nghịch biến":
			noi_dung=f'Cho hàm số $y={latex(exp(expand(f)))}$. Hàm số nghịch biến trên khoảng nào trong các khoảng sau?'
			if a>0:
				kq=f'$(-\\infty;{phan_so(x_0-random.randint(0,5))})$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$({phan_so(x_0+random.randint(0,5))};+\\infty)$'
				kq4=f'$({x_1}; {x_2})$'
					
				noi_dung_loigiai=f"Hàm số xác định trên $\\mathbb{{R}}$.\n\n"\
				f"$f'(x)={dao_ham}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $({phan_so(x_0)};+\\infty)$ và nghịch biến trên khoảng $(-\\infty; {phan_so(x_0)})$.\n\n"\
				f"Do đó hàm số nghịch biến trên khoảng {kq}."
			if a<0:
				kq=f'$({phan_so(x_0+random.randint(0,5))};+\\infty)$'
				kq2=f'$(-\\infty;+\\infty)$'
				kq3=f'$(-\\infty;{phan_so(x_0-random.randint(0,5))})$'
				kq4=f'$({x_1}; {x_2})$'	
					
				noi_dung_loigiai=f"Hàm số xác định trên $\\mathbb{{R}}$.\n\n"\
				f"$f'(x)={dao_ham}$.\n\n"\
				f"$f'(x)=0\\Leftrightarrow x={phan_so(x_0)}$.\n\n"\
				f"Hàm số đã cho đồng biến trên khoảng $(-\\infty; {phan_so(x_0)})$ và nghịch biến trên khoảng $({phan_so(x_0)};+\\infty)$.\n\n"\
				f"Do đó hàm số nghịch biến trên khoảng {kq}."

	if chon==3:
		a = random.randint(1,8)
		b = random.randint(1,8)
		x_1, x_2=-sqrt(b), sqrt(b)
		chon=random.choice(["đồng biến", "nghịch biến"])
		dao_ham=f"\\dfrac{{{latex(-a*x**2+a*b)}}}{{{latex((x**2+b)**2)}}}"
		noi_dung=f'Cho hàm số $y={latex(a*x/(x**2+b))}$. Hàm số {chon} trên khoảng nào trong các khoảng sau?'
		if chon=="đồng biến":						
			kq=f'$({latex(x_1)}; {latex(x_2)})$'
			kq2=random.choice([f'$(-\\infty;+\\infty)$', f'$({int(x_1-random.randint(0,5))};+\\infty)$'])
			kq3=f'$(-\\infty;{int(x_2+random.randint(0,5))})$'
			kq4=random.choice([f"$(-\\infty; {latex(x_1)})$", f"$({latex(x_2)};+\\infty)$"])	
				
		if chon=="nghịch biến":		
			kq=random.choice([f"$(-\\infty; {latex(x_1)})$", f"$({latex(x_2)};+\\infty)$"])	
			kq2=random.choice([f'$(-\\infty;+\\infty)$', f'$({int(x_1-random.randint(0,5))};+\\infty)$'])
			kq3=f'$(-\\infty;{int(x_2+random.randint(0,5))})$'
			kq4=f'$({latex(x_1)}; {latex(x_2)})$'
				
		noi_dung_loigiai=f"Hàm số xác định trên $\\mathbb{{R}}$.\n\n"\
		f"$f'(x)={dao_ham}$.\n\n"\
		f"$f'(x)=0\\Leftrightarrow x={latex(x_1)}, x={latex(x_2)}$.\n\n"\
		f"Hàm số đã cho đồng biến trên khoảng $({latex(x_1)};{latex(x_2)})$, nghịch biến trên các khoảng $(-\\infty; {latex(x_1)})$ và $({latex(x_2)};+\\infty)$.\n\n"\
		f"Do đó hàm số {chon} trên khoảng {kq}."

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	  
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

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_22]-TL-M2. Cho hàm số bậc 3 có hai điểm cực trị x_1,x_2. Tính P=ax_1 + bx_2. 
def prt_34_L12_C1_B1_22():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,3)
	a, b=-(x_1+x_2), x_1*x_2	
	m=random.choice([1,-1,3,-3,6,-6])
	f_dh= m*(x**2+a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)	
	p = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	q = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	noi_dung = f"Cho hàm số $y=f(x)={latex(f)}$ có đạt cực tiểu tại điểm $x=x_1$ và đạt cực đại tại điểm $x=x_2$. Tính $P={p}x_1+{q}x_2$."
	noi_dung=noi_dung.replace("=1x_1","=x_1").replace("=-1x_1","=-x_1").replace("+1x_2","+x_2").replace("+-1x_2","-x_2").replace("+-","-")
	if m>0:
		x_CT, x_CD=x_2, x_1
	if m<0:
		x_CT, x_CD=x_1, x_2

	noi_dung_loigiai=f"$f'(x)={latex(f_dh)}$.\n\n"\
		f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"\
		f"Lập bảng biến thiên.\n\n"\
		f"Hàm số đạt cực tiểu tại $x_1={x_CT}$, đạt cực đại tại $x_2={x_CD}$.\n\n"\
		f"$P={p}x_1+{q}x_2={p*x_CT + q*x_CD}$."
		
	noi_dung_loigiai=noi_dung_loigiai.replace("=1x_1","=x_1").replace("=-1x_1","=-x_1").replace("+1x_2","+x_2").replace("+-1x_2","-x_2").replace("+-","-")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{{p*x_CT + q*x_CD}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=p*x_CT + q*x_CD
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_23]-TL-M2. Cho hàm số bậc 3 có giá trị cực trị y_1,y_2. Tính P=ay_1 + by_2. 
def prt_34_L12_C1_B1_23():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,3)
	a, b=-(x_1+x_2), x_1*x_2	
	m=random.choice([1,-1,3,-3])
	f_dh= m*(x**2+a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)

	p = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	q = random.choice([random.randint(-4, -1), random.randint(1, 4)])

	if m>0:
		x_CT, x_CD=x_2, x_1
	if m<0:
		x_CT, x_CD=x_1, x_2

	y_CT=f.subs(x,x_CT)
	y_CD=f.subs(x,x_CD)

	while p*y_CT + q*y_CD<-9.9 or p*y_CT + q*y_CD>9999:
		x_1 = random.randint(-5,5)
		x_2 = x_1 + random.randint(1,3)
		a, b=-(x_1+x_2), x_1*x_2	
		m=random.choice([1,-1,3,-3])
		f_dh= m*(x**2+a*x+b)
		f=integrate(f_dh,x)+random.randint(-3,3)

		p = random.choice([random.randint(-4, -1), random.randint(1, 4)])
		q = random.choice([random.randint(-4, -1), random.randint(1, 4)])

		if m>0:
			x_CT, x_CD=x_2, x_1
		if m<0:
			x_CT, x_CD=x_1, x_2

		y_CT=f.subs(x,x_CT)
		y_CD=f.subs(x,x_CD)
			
	noi_dung = f"Cho hàm số $y=f(x)={latex(f)}$ có giá trị cực tiểu bằng $y_1$ và giá trị cực đại bằng $y_2$.\n\n Tính $P={p}y_1+{q}y_2$ (kết quả làm tròn đến hàng phần mười)."
	noi_dung=noi_dung.replace("=1y_1","=y_1").replace("=-1y_1","=-y_1").replace("+1y_2","+y_2").replace("+-1y_2","-y_2").replace("+-","-")

	ketqua=round(p*y_CT + q*y_CD,1)
	dap_an=f"{ketqua}".replace(".",",")

	noi_dung_loigiai=(f"$f'(x)={latex(f_dh)}$.\n\n"
		f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"
		f"Lập bảng biến thiên.\n\n"\
		f"Hàm số đạt cực tiểu tại $x_1={x_CT}$, đạt cực đại tại $x_2={x_CD}$.\n\n"
		f"$y_1=f({x_CT})={phan_so(y_CT)}, y_2=f({x_CD})={phan_so(y_CD)}$.\n\n"
		f"$P={p}y_1+{q}y_2={phan_so(p*y_CT + q*y_CD)}$.\n\n"
		f"Đáp án: {dap_an} "
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("=1y_1","=y_1").replace("=-1y_1","=-y_1").replace("+1y_2","+y_2").replace("+-1y_2","-y_2").replace("+-","-")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{${dap_an}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_24]-TL-M2. Cho y=(ax^2+bx+c)/(dx+e) có điểm cực trị x_1,x_2. Tính P=ax_1 + bx_2. 
def prt_34_L12_C1_B1_24():

	x=sp.symbols("x")
	x_1=random.choice([2*i for i in range(-10,10)])
	i=random.randint(1,5)
	x_2=x_1+2*i
	b, c, =(x_1+x_2), x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)
	
	a=random.choice([-1,1,-2,2])
	f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)
	if a>0:
		x_CT, x_CD = x_2, x_1
	if a<0:
		x_CT, x_CD = x_1, x_2

	p = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	q = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	noi_dung = f"Cho hàm số $y=f(x)={latex(f_ok)}$ có điểm cực tiểu $x=x_1$ và điểm cực đại bằng $x=x_2$.\n\n Tính $P={p}x_1+{q}x_2$."
	noi_dung=noi_dung.replace("=1x_1","=x_1").replace("=-1x_1","=-x_1").replace("+1x_2","+x_2").replace("+-1x_2","-x_2").replace("+-","-")


	noi_dung_loigiai=f"$f'(x)={latex(a*g)}$.\n\n"\
		f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"\
		f"Lập bảng biến thiên.\n\n"\
		f"Hàm số đạt cực tiểu tại $x_1={x_CT}$, đạt cực đại tại $x_2={x_CD}$.\n\n"\
		f"$P={p}x_1+{q}x_2={p*x_CT + q*x_CD}$."
	noi_dung_loigiai=noi_dung_loigiai.replace("=1x_1","=x_1").replace("=-1x_1","=-x_1").replace("+1x_2","+x_2").replace("+-1x_2","-x_2").replace("+-","-")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{${p*x_CT + q*x_CD}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=p*x_CT + q*x_CD
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_25]-TL-M2. Cho y=(ax^2+bx+c)/(dx+e) có giá trị cực trị y_1,y_2. Tính P=ay_1 + by_2.
def prt_34_L12_C1_B1_25():
	x=sp.symbols("x")
	x_1=random.choice([2*i for i in range(-10,10)])
	i=random.randint(1,5)
	x_2=x_1+2*i
	b, c, =(x_1+x_2), x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)
	
	a=random.choice([-1,1,-2,2])
	f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)
	if a>0:
		x_CT, x_CD = x_2, x_1
	if a<0:
		x_CT, x_CD = x_1, x_2

	y_CT=f_ok.subs(x,x_CT)
	y_CD=f_ok.subs(x,x_CD)

	p = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	q = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	y_1, y_2=sp.symbols("y_1 y_2")
	noi_dung = (f"Cho hàm số $y=f(x)={latex(f_ok)}$ có giá trị cực tiểu bằng $y_1$ và giá trị cực đại bằng $y_2$.\n\n Tính $P={latex(p*y_1+q*y_2)}$"
	f" (kết quả làm tròn đến hàng phần mười).")

	noi_dung_loigiai=f"$f'(x)={latex(a*g)}$.\n\n"\
		f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"\
		f"Lập bảng biến thiên.\n\n"\
		f"Hàm số đạt cực tiểu tại $x_1={x_CT}$, đạt cực đại tại $x_2={x_CD}$.\n\n"\
		f"$y_1=f({x_CT})={phan_so(y_CT)}, y_2=f({x_CD})={phan_so(y_CD)}$.\n\n"\
		f"$P={latex(p*y_1+q*y_2)}={phan_so(p*y_CT + q*y_CD)}$."
	
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	dap_an=f"{round(p*y_CT + q*y_CD,1)}".replace(".",",")

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{${dap_an}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_26]-TF-M2. Cho hàm số bậc 3. Xét Đ-S: TXD, y', đơn điệu, cực trị
def prt_34_L12_C1_B1_26():
	x=sp.symbols("x")
	x_1 = random.randint(-4,3)
	x_2 = x_1 + random.randint(1,3)
	a, b=-(x_1+x_2), x_1*x_2	
	m=random.choice([1,-1,3,-3])
	f_dh= m*(x**2+a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)

	noi_dung = f"Cho hàm số $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau."		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Tập xác định của hàm số là $\\mathbb{{R}}$" 
	kq1_F=f"Tập xác định của hàm số là ${random.choice([f"({random.randint(1,3)},+\\infty)", f"(-\\infty;{random.randint(1,3)})"])}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Hàm số là hàm đa thức nên có tập xác định là $\\mathbb{{R}}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Hàm số có đạo hàm là $y'={latex(f_dh)}$."
	kq2_F=f"Hàm số có đạo hàm là $y'={latex(f_dh+random.randint(1,6))}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Hàm số có đạo hàm là $y'={latex(f_dh)}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	y_1, y_2 = f.subs(x,x_1), f.subs(x,x_2)
	k=(y_2-y_1)/(x_2-x_1)
	if m>0:
		chon=random.choice(["+","-"])
		if chon=="+":
			kq3_T=f"*Hàm số đồng biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$" 
			kq3_F=f"Hàm số đồng biến trên khoảng $({x_1};{x_2})$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$."
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon=="-":
			kq3_T=f"*Hàm số nghịch biến trên khoảng $({x_1};{x_2})$" 
			kq3_F=f"Hàm số nghịch biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số nghịch biến trên khoảng $({x_1};{x_2})$."
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	
		
		chon=random.randint(1,3)
		
		if chon==1:
			kq4_T=f"*Giá trị cực đại của hàm số là $y={phan_so(y_1)}$"
			kq4_F=f"Giá trị cực đại của hàm số là $y={phan_so(y_2)}$ " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y_{{CD}}=f({x_1})={phan_so(y_1)}, y_{{CT}}=f({x_2})={phan_so(y_2)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon==2:
			kq4_T=f"*Giá trị cực tiểu của hàm số là $y={phan_so(y_2)}$"
			kq4_F=f"Giá trị cực tiểu của hàm số là $y={phan_so(y_1)}$ " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y_{{CD}}=f({x_1})={phan_so(y_1)}, y_{{CT}}=f({x_2})={phan_so(y_2)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==3:
			kq4_T=f"*Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$".replace("+-","-")
			kq4_F=f"Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1+random.randint(1,2))}$".replace("+-","-")
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Đồ thị hàm số có các điểm cực trị là $A({x_1};{phan_so(y_1)})$ và $B({x_2};{phan_so(y_2)})$.\n\n"\
			f"${{AB}}$ có hệ số góc $k=\\dfrac{{{y_2}-{y_1}}}{{{x_2}-{x_1}}}={phan_so(k)}$.\n\n"\
			f"Phương trình đường thẳng ${{AB}}:y={phan_so(k)}(x-{x_1})+{phan_so(y_1)}\\Leftrightarrow y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$.".replace("+-","-").replace("--","+")
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if m<0:
		chon=random.choice(["+","-"])
		if chon=="+":
			kq3_T=f"*Hàm số nghịch biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$" 
			kq3_F=f"Hàm số nghịch biến trên khoảng $({x_1};{x_2})$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$."
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon=="-":
			kq3_T=f"*Hàm số đồng biến trên khoảng $({x_1};{x_2})$" 
			kq3_F=f"Hàm số đồng biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số đồng biến trên khoảng $({x_1};{x_2})$."
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		chon=random.randint(1,3)
		
		if chon==1:
			kq4_T=f"*Giá trị cực tiểu của hàm số là $y={phan_so(y_1)}$"
			kq4_F=f"Giá trị cực tiểu của hàm số là $y={phan_so(y_2)}$ " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y_{{CD}}=f({x_1})={phan_so(y_1)}, y_{{CT}}=f({x_2})={phan_so(y_2)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon==2:
			kq4_T=f"*Giá trị cực đại của hàm số là $y={phan_so(y_2)}$"
			kq4_F=f"Giá trị cực đại của hàm số là $y={phan_so(y_1)}$ " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y_{{CD}}=f({x_1})={phan_so(y_1)}, y_{{CT}}=f({x_2})={phan_so(y_2)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==3:
			kq4_T=f"*Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$".replace("+-","-")
			kq4_F=f"Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1+random.randint(1,2))}$".replace("--","+").replace("+-","-")
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Đồ thị hàm số có các điểm cực trị là $A({x_1};{phan_so(y_1)})$ và $B({x_2};{phan_so(y_2)})$.\n\n"\
			f"${{AB}}$ có hệ số góc $k=\\dfrac{{{y_2}-{y_1}}}{{{x_2}-{x_1}}}={phan_so(k)}$.\n\n"\
			f"Phương trình đường thẳng ${{AB}}:y={phan_so(k)}(x-{x_1})+{phan_so(y_1)}\\Leftrightarrow y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$.".replace("--","+").replace("+-","-")
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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
	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B1_27]-TF-M2. Cho y=(ax^2+bx+c)/(dx+e). Xét Đ-S: TXD, y', đơn điệu, cực trị
def prt_34_L12_C1_B1_27():
	x=sp.symbols("x")
	x_0=random.choice([random.randint(-5, -1), random.randint(1, 5)])
	m=random.choice([1,2,3])
	chon=random.choice(["+","-"])
	if chon=="+":
		f=(x**2-x_0*x+m**2)/(x-x_0)
		f_dh=(x**2-2*x_0*x+x_0**2-m**2)/(x-x_0)**2
		f_dh_false=(x**2-2*x_0*x+x_0**2-m**2)/(x-x_0)
		x_1,x_2 = x_0-m, x_0+m

		kq1_T=f"*Tập xác định của hàm số là $\\mathbb{{R}} \\backslash \\{{{x_0}\\}}$" 
		kq1_F=f"Tập xác định của hàm số là $\\mathbb{{R}} \\backslash \\{{{-x_0}\\}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Hàm số xác định khi: ${latex(x-x_0)}\\ne 0 \\Leftrightarrow x \\ne {x_0}$. Suy ra $D=\\mathbb{{R}}\\backslash\\{{{x_0}\\}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq2_T=f"*Hàm số có đạo hàm là $y'={latex(f_dh)}$"
		kq2_F=f"Hàm số có đạo hàm là $y'={latex(f_dh_false)}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'=\\dfrac{{({latex(2*x-x_0)})({latex(x-x_0)})-({latex(x**2-x_0*x+m**2)})}}{{{latex((x-x_0)**2)}}}={latex(f_dh)}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		chon=random.choice(["+","-"])
		if chon=="+":
			kq3_T=f"*Hàm số đồng biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$" 
			kq3_F=f"Hàm số đồng biến trên khoảng ${random.choice([f"({x_1};{x_0})", f"({x_0};{x_2})"])}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon=="-":
			kq3_T=f"*Hàm số nghịch biến trên khoảng ${random.choice([f"({x_1};{x_0})", f"({x_0};{x_2})"])}$" 
			kq3_F=f"Hàm số nghịch biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		chon=random.randint(1,6)		
		if chon==1:
			kq4_T=f"*Hàm số có 2 điểm cực trị"
			kq4_F=f"Hàm số không có cực trị" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_2}$, đạt cực đại tại $x={x_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon==2:
			kq4_T=f"*Điểm cực đại của hàm số là $x={x_1}$"
			kq4_F=f"Điểm cực đại của hàm số là $x={x_2}$"
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_2}$, đạt cực đại tại $x={x_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon==3:
			kq4_T=f"*Điểm cực tiểu của hàm số là $x={x_2}$"
			kq4_F=f"Điểm cực tiểu của hàm số là $x={x_1}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_2}$, đạt cực đại tại $x={x_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		y_1,y_2=f.subs(x,x_1), f.subs(x,x_2)
		if chon==4:
			kq4_T=f"*Giá trị cực đại của hàm số là ${y_1}$"
			kq4_F=f"Giá trị cực đại của hàm số là ${y_2}$ " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_2}$, đạt cực đại tại $x={x_1}$.\n\n"\
			f"Giá trị cực tiểu là $y=f({x_2})={y_2}$, giá trị cực đại là $y=f({x_1})={y_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==5:
			kq4_T=f"*Giá trị cực tiểu của hàm số là ${y_2}$"
			kq4_F=f"Giá trị cực tiểu của hàm số là ${y_1}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_2}$, đạt cực đại tại $x={x_1}$.\n\n"\
			f"Giá trị cực tiểu là $y=f({x_2})={y_2}$, giá trị cực đại là $y=f({x_1})={y_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		k=(y_2-y_1)/(x_2-x_1)
		if chon==6:
			kq4_T=f"*Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$".replace("+-","-")
			kq4_F=f"Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1+random.randint(1,2))}$".replace("--","+").replace("+-","-")
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Đồ thị hàm số có các điểm cực trị là $A({x_1};{phan_so(y_1)})$ và $B({x_2};{phan_so(y_2)})$.\n\n"\
			f"${{AB}}$ có hệ số góc $k=\\dfrac{{{y_2}-{y_1}}}{{{x_2}-{x_1}}}={phan_so(k)}$.\n\n"\
			f"Phương trình đường thẳng ${{AB}}:y={phan_so(k)}(x-{x_1})+{phan_so(y_1)}\\Leftrightarrow y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$.".replace("--","+").replace("+-","-")
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon=="-":
		f=(-x**2+x_0*x-m**2)/(x-x_0)
		f_dh=(-x**2+2*x_0*x-x_0**2+m**2)/(x-x_0)**2
		f_dh_false=(-x**2+2*x_0*x-x_0**2+m**2)/(x-x_0)
		x_1,x_2 = x_0-m, x_0+m

		kq1_T=f"*Tập xác định của hàm số là $\\mathbb{{R}} \\backslash \\{{{x_0}\\}}$" 
		kq1_F=f"Tập xác định của hàm số là $\\mathbb{{R}} \\backslash \\{{{-x_0}\\}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Hàm số xác định khi: ${latex(x-x_0)}\\ne 0 \\Leftrightarrow x \\ne {x_0}$. Suy ra $D=\\mathbb{{R}}\\backslash\\{{{x_0}\\}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq2_T=f"*Hàm số có đạo hàm là $y'={latex(f_dh)}$"
		kq2_F=f"Hàm số có đạo hàm là $y'={latex(f_dh_false)}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'=\\dfrac{{({latex(2*x-x_0)})({latex(x-x_0)})-({latex(x**2-x_0*x+m**2)})}}{{{latex((x-x_0)**2)}}}={latex(f_dh)}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		chon=random.choice(["+","-"])
		if chon=="+":
			kq3_T=f"*Hàm số đồng biến trên khoảng ${random.choice([f"({x_1};{x_0})", f"({x_0};{x_2})"])}$" 
			kq3_F=f"Hàm số đồng biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon=="-":
			kq3_T=f"*Hàm số nghịch biến trên khoảng ${random.choice([f"(-\\infty;{x_1})", f"({x_2};+\\infty)"])}$" 
			kq3_F=f"Hàm số nghịch biến trên khoảng ${random.choice([f"({x_1};{x_0})", f"({x_0};{x_2})"])}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
			f"Hàm số nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};+\\infty)$.\n\n"\
			f"Hàm số đồng biến trên các khoảng $({x_1};{x_0})$ và $({x_0};{x_2})$.\n\n"
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
				
		chon=random.randint(1,6)
		if chon==1:
			kq4_T=f"*Hàm số có 2 điểm cực trị"
			kq4_F=f"Hàm số không có cực trị" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_2}$, đạt cực đại tại $x={x_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon==2:
			kq4_T=f"*Điểm cực đại của hàm số là $x={x_2}$"
			kq4_F=f"Điểm cực đại của hàm số là $x={x_1}$"
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_1}$, đạt cực đại tại $x={x_2}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if chon==3:
			kq4_T=f"*Điểm cực tiểu của hàm số là $x={x_1}$"
			kq4_F=f"Điểm cực tiểu của hàm số là $x={x_2}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực tiểu tại $x={x_1}$, đạt cực đại tại $x={x_2}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		y_1,y_2=f.subs(x,x_1), f.subs(x,x_2)
		if chon==4:
			kq4_T=f"*Giá trị cực tiểu của hàm số là ${y_1}$"
			kq4_F=f"Giá trị cực tiểu của hàm số là ${y_2}$ " 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực đại tại $x={x_2}$, đạt cực tiểu tại $x={x_1}$.\n\n"\
			f"Giá trị cực đại là $y=f({x_2})={y_2}$, giá trị cực tiểu là $y=f({x_1})={y_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==5:
			kq4_T=f"*Giá trị cực đại của hàm số là ${y_2}$"
			kq4_F=f"Giá trị cực đại của hàm số là ${y_1}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'=0 \\Leftrightarrow x={x_1},x={x_2}$. Hàm số đạt cực đại tại $x={x_2}$, đạt cực tiểu tại $x={x_1}$.\n\n"\
			f"Giá trị cực đại là $y=f({x_2})={y_2}$, giá trị cực tiểu là $y=f({x_1})={y_1}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		k=(y_2-y_1)/(x_2-x_1)
		if chon==6:
			kq4_T=f"*Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$".replace("+-","-")
			kq4_F=f"Phương trình đường thẳng đi qua các điểm cực đại và điểm cực tiểu của đồ thị hàm số là $y={phan_so(k)}x+{phan_so(-k*x_1+y_1+random.randint(1,2))}$".replace("--","+").replace("+-","-")
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"Đồ thị hàm số có các điểm cực trị là $A({x_1};{phan_so(y_1)})$ và $B({x_2};{phan_so(y_2)})$.\n\n"\
			f"${{AB}}$ có hệ số góc $k=\\dfrac{{{y_2}-{y_1}}}{{{x_2}-{x_1}}}={phan_so(k)}$.\n\n"\
			f"Phương trình đường thẳng ${{AB}}:y={phan_so(k)}(x-{x_1})+{phan_so(y_1)}\\Leftrightarrow y={phan_so(k)}x+{phan_so(-k*x_1+y_1)}$.".replace("--","+").replace("+-","-")
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	noi_dung = f"Cho hàm số $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau."		
	debai_word= f"{noi_dung}\n"

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B1_28]-M2. Cho dấu f'(x) trên khoảng (a,b) và (c,d). Tìm khẳng định đúng?
def prt_34_L12_C1_B1_28():
	x = sp.symbols('x')
	a = random.randint(-8,4)
	b = a + random.randint(2,4)
	c = b + random.randint(1,3)
	d = c + random.randint(2,4)

	chon=random.randint(1,2)
	if chon==1:
		noi_dung = f"Cho hàm số $y=f(x)$ có đạo hàm trên $\\mathbb{{R}}$ và thỏa mãn $f'(x)<0,\\forall x \\in ({a};{b})$ và "\
	f"$f'(x)>0,\\forall x \\in ({c};{d})$. Tìm khẳng định đúng?"	
		noi_dung_loigiai=f"$f'(x)<0,\\forall x \\in ({a};{b})$ suy ra $f(x)$ nghịch biến trên khoảng $({a};{b})$.\n\n"\
	f"$f'(x)>0,\\forall x \\in ({c};{d})$ suy ra $f(x)$ đồng biến trên khoảng $({c};{d})$."

		kq=random.choice([f"$f(x)$ đồng biến trên khoảng $({c};{random.choice([d,d-1])})$",f"$f(x)$ nghịch biến trên khoảng $({a};{random.choice([b,b-1])})$"])
		kq2=f"$f(x)$ đồng biến trên khoảng $({a};{b+random.randint(0,3)})$"
		kq3=f"$f(x)$ nghịch biến trên khoảng $({c};{d+random.randint(0,3)})$"
		kq4=f"$f(x)$ nghịch biến trên khoảng $({a};{d+random.randint(0,3)})$"
	
	if chon==2:
		noi_dung = f"Cho hàm số $y=f(x)$ có đạo hàm trên $\\mathbb{{R}}$ và thỏa mãn $f'(x)>0,\\forall x \\in ({a};{b})$ và "\
	f"$f'(x)<0,\\forall x \\in ({c};{d})$. Tìm khẳng định đúng?"	
		noi_dung_loigiai=f"$f'(x)>0,\\forall x \\in ({a};{b})$ suy ra $f(x)$ đồng biến trên khoảng $({a};{b})$.\n\n"\
	f"$f'(x)<0,\\forall x \\in ({c};{d})$ suy ra $f(x)$ nghịch biến trên khoảng $({c};{d})$."

		kq=random.choice([f"$f(x)$ nghịch biến trên khoảng $({c};{random.choice([d,d-1])})$",f"$f(x)$ đồng biến trên khoảng $({a};{random.choice([b,b-1])})$"])
		kq2=f"$f(x)$ đồng biến trên khoảng $({a};{b+random.randint(1,3)})$"
		kq3=f"$f(x)$ nghịch biến trên khoảng $({c};{d+random.randint(1,3)})$"
		kq4=f"$f(x)$ nghịch biến trên khoảng $({a};{d+random.randint(0,3)})$"	

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B1_29]-TL-M3. Cho f(x)=(ax+b)/(x+m). Tìm số giá trị nguyên của m để hàm số đồng biến,nghịch biến trên K.
def prt_34_L12_C1_B1_29():
	x,m=sp.symbols("x, m")
	a=random.randint(1,5)
	b=random.choice([i for i in range(-5, 6) if i!=0])
	chon=random.randint(1,2)	
	
	if chon==1:
		x_0=random.randint(int(b/a)+10,int(b/a)+random.randint(20,30))
		k=random.choice([-10*i for i in range(5,20) ])
		dem=0
		for i in range(k-1,-k+1):
			if all([i>k, i<-k, i>b/a, i<=x_0]):
				dem+=1
		dap_an=dem
		
		noi_dung=f"Cho hàm số $f(x)=\\dfrac{{{latex(-a*x+b)}}}{{x-m}}$ với ${{m}}$ là tham số."\
		f" Tìm số giá trị nguyên của ${{m}}$ thuộc khoảng $({k};{-k})$ để hàm số đồng biến trên khoảng $({x_0};+\\infty)$."

		noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{m}\\}}$.\n\n"\
		f"$f'(x)=\\dfrac{{{latex(a*m-b)}}} {{(x-m)^2}}$.\n\n"\
		f"Để hàm số đồng biến trên khoảng $({x_0};+\\infty)$ thì:\n\n"\
		f"$\\left\\{{ \\begin{{array}}{{l}}\n\
		{latex(a*m-b)}>0 \\\\ \n \
		m \\notin ({x_0};+\\infty) \n\
		\\end{{array}} \\right. \n \\Leftrightarrow "\
		f"\\left\\{{ \\begin{{array}}{{l}} \n\
		m>{phan_so(b/a)} \\\\ \n\
		m \\le {x_0}\n\
		\\end{{array}} \\right. \n"\
		f"\\Rightarrow {phan_so(b/a)}<m \\le {x_0}$.\n\n"\
		f"Số các số nguyên là: ${{{dap_an}}}$."
	
	if chon==2:
		x_0=random.randint(int(b/a)-random.randint(20,30),int(b/a)-10,)
		k=random.choice([-10*i for i in range(5,20) ])
		dem=0
		for i in range(k-1,-k+1):
			if all([i>k, i<-k, i<b/a, i>=x_0]):
				dem+=1
		dap_an=dem

		noi_dung=f"Cho hàm số $f(x)=\\dfrac{{{latex(-a*x+b)}}}{{x-m}}$ với ${{m}}$ là tham số."\
		f" Tìm số giá trị nguyên của ${{m}}$ thuộc khoảng $({k};{-k})$ để hàm số nghịch biến trên khoảng $(-\\infty;{x_0})$."

		noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{m}\\}}$.\n\n"\
		f"$f'(x)=\\dfrac{{{latex(a*m-b)}}} {{(x-m)^2}}$.\n\n"\
		f"Để hàm số nghịch biến trên khoảng $(-\\infty;{x_0})$ thì:\n\n"\
		f"$\\left\\{{ \\begin{{array}}{{l}}\n\
		{latex(a*m-b)}<0 \\\\ \n \
		m \\notin (-\\infty;{x_0}) \n\
		\\end{{array}} \\right. \n \\Leftrightarrow "\
		f"\\left\\{{ \\begin{{array}}{{l}} \n\
		m<{phan_so(b/a)} \\\\ \n\
		m \\ge {x_0}\n\
		\\end{{array}} \\right. \n"\
		f"\\Rightarrow {x_0}\\le m <{phan_so(b/a)}$.\n\n"\
		f"Số các số nguyên là: ${{{dap_an}}}$."
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{${{{dap_an}}}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_30]-TF-M3. Cho f(x)=(ax+b)/(x+m). Xét Đ-S: đạo hàm, cực trị, đồng biến, nghịch biến
def prt_34_L12_C1_B1_30():
	x,m=sp.symbols("x, m")
	a=random.randint(1,5)
	b=random.choice([i for i in range(-5, 6) if i!=0])

	noi_dung = f"Cho hàm số $f(x)=\\dfrac{{{latex(-a*x+b)}}}{{x-m}}$ với ${{m}}$ là tham số. Xét tính đúng-sai của các khẳng định sau."		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Hàm số có đạo hàm là $f'(x)=\\dfrac{{{latex(a*m-b)}}}{{(x-m)^2}}$" 
	kq1_F=f"Hàm số có đạo hàm là $f'(x)=\\dfrac{{{latex(a*m+b)}}}{{(x-m)^2}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Hàm số có $f'(x)=\\dfrac{{{latex(a*m-b)}}}{{(x-m)^2}}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)	
	if chon==1:
		kq2_T=f"*Hàm số không có cực trị với mọi $m\\ne {phan_so(b/a)}$"
		kq2_F=f"Hàm số có {random.choice(["một","hai"])} cực trị với mọi $m\\ne {phan_so(b/a)}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Với mọi $m> {phan_so(b/a)}$ thì hàm số đồng biến trên các khoảng xác định nên không có cực trị.\n\n"\
		f"Với mọi $m< {phan_so(b/a)}$ thì hàm số nghịch biến trên các khoảng xác định nên không có cực trị."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	

		kq3_T=f"*Với mọi $m> {phan_so(b/a)}$ thì hàm số đồng biến trên các khoảng xác định" 
		kq3_F=f"Với mọi $m> {phan_so(b/a)}$ thì hàm số nghịch biến trên các khoảng xác định "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$f'(x)=\\dfrac{{{latex(a*m-b)}}}{{(x-m)^2}}$.\n\n"\
		f"Do đó: với mọi $m> {phan_so(b/a)}$ thì hàm số đồng biến trên các khoảng xác định."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		x_0=int(b/a)+random.randint(5,20)
		# Lấy giá trị lớn hơn gần nhất của a (ceil) và giá trị nhỏ hơn gần nhất của b (floor)
		start = math.ceil(b/a)
		end = x_0     
		t= end - start + 1
		k=b/a
		if k.is_integer():
			t=t-2

		kq4_T=f"*Số các giá trị nguyên của ${{m}}$ để hàm số đồng biến trên khoảng $({x_0};+\\infty)$ là ${{{t}}}$"
		kq4_F=f"Số các giá trị nguyên của ${{m}}$ để hàm số đồng biến trên khoảng $({x_0};+\\infty)$ là ${{{t+random.randint(4,7)}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{m}\\}}$.\n\n"\
		f"$f'(x)=\\dfrac{{{latex(a*m-b)}}} {{(x-m)^2}}$.\n\n"\
		f"Để hàm số đồng biến trên khoảng $({x_0};+\\infty)$ thì:\n\n"\
		f"$\\left\\{{ \\begin{{array}}{{l}}\n\
		{latex(a*m-b)}>0 \\\\ \n \
		m \\notin ({x_0};+\\infty) \n\
		\\end{{array}} \\right. \n \\Leftrightarrow "\
		f"\\left\\{{ \\begin{{array}}{{l}} \n\
		m>{phan_so(b/a)} \\\\ \n\
		m \\le {x_0}\n\
		\\end{{array}} \\right. \n"\
		f"\\Rightarrow {phan_so(b/a)}<m \\le {x_0}$.\n\n"\
		f"Số các số nguyên là: ${{{t}}}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	


	if chon==2:
		t=int(b/a)+random.randint(4,10)
		kq2_T=f"*Với $m={t}$ thì $f(x)$ đồng biến trên các khoảng xác định"
		kq2_F=f"Với $m={t}$ thì $f(x)$ nghịch biến trên các khoảng xác định "
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Với $m={t}$ thì $f'(x)={latex((a*t-b)/(x+t)**2)}>0,\\forall x \\ne {-t}$ nên $f(x)$ đồng biến trên các khoảng xác định."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq3_T=f"*Với mọi $m< {phan_so(b/a)}$ thì hàm số nghịch biến trên các khoảng xác định" 
		kq3_F=f"Với mọi $m< {phan_so(b/a)}$ thì hàm số đồng biến trên các khoảng xác định "
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$f'(x)={latex((a*m-b)/(x+m)**2)}$.\n\n"\
		f"Do đó: với mọi $m< {phan_so(b/a)}$ thì hàm số nghịch biến trên các khoảng xác định."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		x_0=int(b/a)-random.randint(5,20)
		# Lấy giá trị lớn hơn gần nhất của a (ceil) và giá trị nhỏ hơn gần nhất của b (floor)
		start = x_0
		end = math.floor(b/a)  
		t= end - start + 1
		k=b/a
		if k.is_integer():
			t=t-1
		kq4_T=f"*Số giá trị nguyên của ${{m}}$ để hàm số nghịch biến trên khoảng $(-\\infty;{x_0})$ là ${{{t}}}$"
		kq4_F=f"Số giá trị nguyên của ${{m}}$ để hàm số nghịch biến trên khoảng $(-\\infty;{x_0})$ là ${{{t+random.randint(3,7)}}}$ " 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{m}\\}}$.\n\n"\
		f"$f'(x)=\\dfrac{{{latex(a*m-b)}}} {{(x+m)^2}}$.\n\n"\
		f"Để hàm số nghịch biến trên khoảng $(-\\infty;{x_0})$ thì:\n\n"\
		f"$\\left\\{{ \\begin{{array}}{{l}}\n\
		{latex(a*m-b)}<0 \\\\ \n \
		m \\notin (-\\infty;{x_0}) \n\
		\\end{{array}} \\right. \n \\Leftrightarrow "\
		f"\\left\\{{ \\begin{{array}}{{l}} \n\
		m<{phan_so(b/a)} \\\\ \n\
		m \\ge {x_0}\n\
		\\end{{array}} \\right. \n"\
		f"\\Rightarrow {x_0}\\le m <{phan_so(b/a)}$.\n\n"\
		f"Số các số nguyên là: ${{{t}}}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B1_31]-TF-M3. Cho BXD f'(x). Xét đúng-sai:đơn điệu và cực trị của f(x), đơn điệu và cực trị của f(ax+b).	
def prt_34_L12_C1_B1_31():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,4)
	x_3= x_2 + random.randint(1,5)
	chon=random.randint(1,2)	
	if chon==1:
		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,+,0,-,0,+,0,-,}} \n \
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"
		chon = random.randint(1,2)
		if chon==1:
			khoang_db=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
			khoang_db_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
			kq1_T=f'*Hàm số đồng biến trên khoảng {khoang_db}' 
			kq1_F=f'Hàm số đồng biến trên khoảng {khoang_db_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
			
			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq2_T=f'*Điểm cực tiểu của hàm số đã cho là $x={x_2}$' 
			kq2_F=f'Điểm cực tiểu của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$'
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực tiểu tại điểm $x={x_2}$.'
			loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq2==kq2_F:
				loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		if chon==2:
			khoang_nb=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
			khoang_nb_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

			kq1_T=f'*Hàm số nghịch biến trên khoảng {khoang_nb}'
			kq1_F=f'Hàm số nghịch biến trên khoảng {khoang_nb_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq2_T=f'*Điểm cực đại của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$' 
			kq2_F=f'Điểm cực đại của hàm số đã cho là $x={x_2}$'
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực đại tại điểm $x={x_1}$ hoặc $x={x_3}$.'
			loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq2==kq2_F:
				loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a = random.choice([i for i in range(-6, 6) if i!=0])
		b = random.choice([i for i in range(-8, 8) if i!=0])
		
		x_n1, x_n2, x_n3 = (x_1-b)/a, (x_2-b)/a, (x_3-b)/a
		kq3_T=f"*Hàm số $y=f({latex(a*x+b)})$ đạt cực trị tại điểm $x={phan_so(random.choice([x_n1, x_n2, x_n3]))}$" 
		kq3_F=f"Hàm số $y=f({latex(a*x+b)})$ đạt cực trị tại điểm $x={phan_so(random.choice([(x_n1+x_n2)/2, (x_n2+x_n3)/2]))}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$[f({latex(a*x+b)})]'={a}f'({latex(a*x+b)})$.\n\n"\
		f"$[f({latex(a*x+b)})]'=0\\Leftrightarrow f'({latex(a*x+b)})=0"\
		f"\\left[ \\begin{{array}}{{l}} \n\
		{latex(a*x+b)}={x_1} \\\\ \n\
		{latex(a*x+b)}={x_2} \\\\ \n\
		{latex(a*x+b)}={x_3} \n\
		\\end{{array}} \\right.$\n\n"\
		f"$\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
		x={phan_so(x_n1)} \\\\ \n\
		x={phan_so(x_n2)} \\\\ \n\
		x={phan_so(x_n3)} \n\
		\\end{{array}} \\right.$"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if a<0:
			khoang_db=f"\\left({random.choice([f"{phan_so((x_2-b)/a)};{phan_so((x_1-b)/a)}",f"-\\infty;{phan_so((x_3-b)/a)}"])}\\right)"
			khoang_nb=f"\\left({random.choice([f"{phan_so((x_3-b)/a)};{phan_so((x_2-b)/a)}",f"{phan_so((x_1-b)/a)};+\\infty"])}\\right)"

			
			kq4_T=random.choice([f"*Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_db}$", f"*Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_nb}$" ])
			kq4_F=random.choice([f"Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_db}$", f"Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_nb}$"])
			kq4=random.choice([kq4_T, kq4_F])

			HDG=f"$\\left[ f({latex(a*x+b)}) \\right]'={a}f'({latex(a*x+b)})$.\n\n"\
			f"$\\left[ f({latex(a*x+b)}) \\right]' >0 \\Leftrightarrow f'({latex(a*x+b)}) <0 \\Leftrightarrow "\
			f"\\left[ \\begin{{array}}{{l}} \n\
			{x_1}<{latex(a*x+b)}<{x_2} \\\\ \n\
			{latex(a*x+b)}>{x_3}\n\
			\\end{{array}} \\right."\
			f"\\Rightarrow\\left[ \\begin{{array}}{{l}} \n\
			{phan_so((x_2-b)/a)}<x<{phan_so((x_1-b)/a)} \\\\ \n\
			x<{phan_so((x_3-b)/a)}\n\
			\\end{{array}} \\right.$\n\n"\
			f"Vậy hàm số $y=f({latex(a*x+b)})$ đồng biến trên các khoảng $\\left({phan_so((x_2-b)/a)};{phan_so((x_1-b)/a)}\\right)$ và $\\left(-\\infty;{phan_so((x_3-b)/a)}\\right)$, "\
			f"nghịch biến trên các khoảng $\\left({phan_so((x_3-b)/a)};{phan_so((x_2-b)/a)}\\right)$ và $\\left({phan_so((x_1-b)/a)};+\\infty\\right)$."

			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if a>0:
			khoang_db=f"\\left({random.choice([f"{phan_so((x_2-b)/a)};{phan_so((x_3-b)/a)}", f"-\\infty;{phan_so((x_1-b)/a)}"])}\\right)"
			khoang_nb=f"\\left({random.choice([f"{phan_so((x_1-b)/a)};{phan_so((x_2-b)/a)}", f"{phan_so((x_3-b)/a)};+\\infty"])}\\right)"

			
			kq4_T=random.choice([f"*Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_db}$", f"*Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_nb}$" ])
			kq4_F=random.choice([f"Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_db}$", f"Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_nb}$"])
			kq4=random.choice([kq4_T, kq4_F])

			HDG=f"$\\left[ f({latex(a*x+b)}) \\right]'={a}f'({latex(a*x+b)})$.\n\n"\
			f"$\\left[ f({latex(a*x+b)}) \\right]' >0 \\Leftrightarrow f'({latex(a*x+b)}) >0 \\Leftrightarrow "\
			f"\\left[\\begin{{array}}{{l}} \n\
			{x_2}<{latex(a*x+b)}<{x_3} \\\\ \n\
			{latex(a*x+b)}<{x_1}\n\
			\\end{{array}} \\right."\
			f"\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
			{phan_so((x_2-b)/a)}<x<{phan_so((x_3-b)/a)} \\\\ \n\
			x<{phan_so((x_1-b)/a)}\n\
			\\end{{array}} \\right.$\n\n"\
			f"Vậy hàm số $y=f({latex(a*x+b)})$ đồng biến trên các khoảng $\\left({phan_so((x_2-b)/a)};{phan_so((x_3-b)/a)}\\right)$ và $\\left(-\\infty;{phan_so((x_1-b)/a)}\\right)$, "\
			f"nghịch biến trên các khoảng $\\left({phan_so((x_1-b)/a)};{phan_so((x_2-b)/a)}\\right)$ và $\\left({phan_so((x_3-b)/a)};+\\infty\\right)$."

			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon==2:
		code_hinh = f"\\begin{{tikzpicture}}\n \
		\\tkzTabInit[nocadre=false, lgt=1.3, espcl=2] \n \
		{{$x$ /0.7,$f'(x)$ /0.7}}\n \
		{{$-\\infty$,${x_1}$,${x_2}$,${x_3}$, $+\\infty$}}\n \
		\\tkzTabLine{{,-,0,+,0,-,0,+,}} \n \
		\\end{{tikzpicture}}\n"  

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		noi_dung=f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu của $f'(x)$ như hình vẽ."\
		f" Xét tính đúng sai của các khẳng định sau?"
		chon = random.randint(1,2)
		if chon==1:
			khoang_db=random.choice([f"$(-\\infty;{x_1})$", f"$({x_2};{x_3})$"])
			khoang_db_false=random.choice([f"$(-\\infty;{x_2})$", f"$({x_2};+\\infty)$",f"$({x_1};{x_3})$"])
			kq1_T=f'*Hàm số nghịch biến trên khoảng {khoang_db}' 
			kq1_F=f'Hàm số nghịch biến trên khoảng {khoang_db_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ nghịch biến trên các khoảng $(-\\infty;{x_1})$ và $({x_2};{x_3})$.'
			
			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq2_T=f'*Điểm cực đại của hàm số đã cho là $x={x_2}$' 
			kq2_F=f'Điểm cực đại của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$'
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực đại tại điểm $x={x_2}$.'
			loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq2==kq2_F:
				loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		if chon==2:
			khoang_nb=random.choice([f"$({x_3};+\\infty)$", f"$({x_1};{x_2})$"])
			khoang_nb_false=random.choice([f"$(-\\infty;{x_1+random.randint(1,5)})$", f"$({x_1};+\\infty)$"])

			kq1_T=f'*Hàm số đồng biến trên khoảng {khoang_nb}'
			kq1_F=f'Hàm số đồng biến trên khoảng {khoang_nb_false}'
			kq1=random.choice([kq1_T, kq1_F])
			HDG=HDG=f'Dựa vào bảng xét dấu ta có hàm số $y=f(x)$ đồng biến trên các khoảng $({x_1};{x_2})$ và $({x_3};+\\infty)$.'

			loigiai_1=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq1==kq1_F:
				loigiai_1=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

			kq2_T=f'*Điểm cực tiểu của hàm số đã cho là $x={random.choice([{x_1}, {x_3}])}$' 
			kq2_F=f'Điểm cực tiểu của hàm số đã cho là $x={x_2}$'
			kq2=random.choice([kq2_T, kq2_F])
			HDG=f'Dựa vào bảng biến thiên, hàm số đã cho đạt cực tiểu tại điểm $x={x_1}$ hoặc $x={x_3}$.'
			loigiai_2=f'Khẳng định đã cho là khẳng định đúng.\n\n {HDG}'
			if kq2==kq2_F:
				loigiai_2=f'Khẳng định đã cho là khẳng định sai.\n\n {HDG}'

		a = random.choice([i for i in range(-6, 6) if i!=0])
		b = random.choice([i for i in range(-8, 8) if i!=0])
			
		x_n1, x_n2, x_n3 = (x_1-b)/a, (x_2-b)/a, (x_3-b)/a
		kq3_T=f"*Hàm số $y=f({latex(a*x+b)})$ đạt cực trị tại điểm $x={phan_so(random.choice([x_n1, x_n2, x_n3]))}$" 
		kq3_F=f"Hàm số $y=f({latex(a*x+b)})$ đạt cực trị tại điểm $x={phan_so(random.choice([(x_n1+x_n2)/2, (x_n2+x_n3)/2]))}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$[f({latex(a*x+b)})]'={a}f'({latex(a*x+b)})$.\n\n"\
		f"$[f({latex(a*x+b)})]'=0\\Leftrightarrow f'({latex(a*x+b)})=0"\
		f"\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
		{latex(a*x+b)}={x_1} \\\\ \n\
		{latex(a*x+b)}={x_2} \\\\ \n\
		{latex(a*x+b)}={x_3} \n\
		\\end{{array}} \\right.$\n\n"\
		f"$\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
		x={phan_so(x_n1)} \\\\ \n\
		x={phan_so(x_n2)} \\\\ \n\
		x={phan_so(x_n3)} \n\
		\\end{{array}} \\right.$"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if a<0:
			khoang_nb=f"\\left({random.choice([f"{phan_so((x_2-b)/a)};{phan_so((x_1-b)/a)}",f"-\\infty;{phan_so((x_3-b)/a)}"])}\\right)"
			khoang_db=f"\\left({random.choice([f"{phan_so((x_3-b)/a)};{phan_so((x_2-b)/a)}",f"{phan_so((x_1-b)/a)};+\\infty"])}\\right)"

			
			kq4_T=random.choice([f"*Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_db}$", f"*Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_nb}$" ])
			kq4_F=random.choice([f"Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_db}$", f"Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_nb}$"])
			kq4=random.choice([kq4_T, kq4_F])

			HDG=f"$\\left[ f({latex(a*x+b)}) \\right]'={a}f'({latex(a*x+b)})$.\n\n"\
			f"$\\left[ f({latex(a*x+b)}) \\right]' >0 \\Leftrightarrow f'({latex(a*x+b)}) <0 \\Leftrightarrow "\
			f"\\left[ \\begin{{array}}{{l}} \n\
			{x_2}<{latex(a*x+b)}<{x_3} \\\\ \n\
			{latex(a*x+b)}<{x_1}\n\
			\\end{{array}} \\right."\
			f"\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
			{phan_so((x_3-b)/a)}<x<{phan_so((x_2-b)/a)} \\\\ \n\
			x>{phan_so((x_1-b)/a)}\n\
			\\end{{array}} \\right.$\n\n"\
			f"Vậy hàm số $y=f({latex(a*x+b)})$ nghịch biến trên các khoảng $\\left({phan_so((x_2-b)/a)};{phan_so((x_1-b)/a)}\\right)$ và $\\left(-\\infty;{phan_so((x_3-b)/a)}\\right)$, "\
			f"đồng biến trên các khoảng $\\left({phan_so((x_3-b)/a)};{phan_so((x_2-b)/a)}\\right)$ và $\\left({phan_so((x_1-b)/a)};+\\infty\\right)$."

			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		if a>0:
			khoang_nb=f"\\left({random.choice([f"{phan_so((x_2-b)/a)};{phan_so((x_3-b)/a)}", f"-\\infty;{phan_so((x_1-b)/a)}"])} \\right)"
			khoang_db=f"\\left({random.choice([f"{phan_so((x_1-b)/a)};{phan_so((x_2-b)/a)}", f"{phan_so((x_3-b)/a)};+\\infty"])} \\right)"

			
			kq4_T=random.choice([f"*Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_db}$", f"*Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_nb}$" ])
			kq4_F=random.choice([f"Hàm số $y=f({latex(a*x+b)})$ nghịch biến trên khoảng ${khoang_db}$", f"Hàm số $y=f({latex(a*x+b)})$ đồng biến trên khoảng ${khoang_nb}$"])
			kq4=random.choice([kq4_T, kq4_F])

			HDG=f"$\\left[ f({latex(a*x+b)}) \\right]'={a}f'({latex(a*x+b)})$.\n\n"\
			f"$\\left[ f({latex(a*x+b)}) \\right]' >0 \\Leftrightarrow f'({latex(a*x+b)}) >0 \\Leftrightarrow "\
			f"\\left\\{{ \\begin{{array}}{{l}} \n\
			{x_1}<{latex(a*x+b)}<{x_2} \\\\ \n\
			{latex(a*x+b)}>{x_3}\n\
			\\end{{array}} \\right."\
			f"\\left\\{{ \\begin{{array}}{{l}} \n\
			{phan_so((x_1-b)/a)}<x<{phan_so((x_2-b)/a)} \\\\ \n\
			x>{phan_so((x_3-b)/a)}\n\
			\\end{{array}} \\right.$\n\n"\
			f"Vậy hàm số $y=f({latex(a*x+b)})$ nghịch biến trên các khoảng $\\left({phan_so((x_2-b)/a)};{phan_so((x_3-b)/a)}\\right)$ và $\\left(-\\infty;{phan_so((x_1-b)/a)}\\right)$, "\
			f"đồng biến trên các khoảng $\\left({phan_so((x_1-b)/a)};{phan_so((x_2-b)/a)}\\right)$ và $\\left({phan_so((x_3-b)/a)};+\\infty\\right)$."		

			
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n\n"\
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
		f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
		f"\\choiceTFt\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B1_32]-TL-M3. Tìm m để hàm số đồng biến, nghịch biến trên khoảng.
def prt_34_L12_C1_B1_32():
	x,m=sp.symbols("x m")
	chon=random.randint(1,2)
	if chon==1:
		code_hinh=f"\\begin{{tikzpicture}}\n\
			\\tkzTabInit[lgt=1.2,espcl=4]\n\
			{{$x$/1,$f'(x)$/1,$f(x)$/2}}\n\
			{{$0$,$1$,$+\\infty$}}\n\
			\\tkzTabLine{{ ,-,z,+, }}\n\
			\\tkzTabVar{{+/,-/$-3$,+/}}\n\
			\\end{{tikzpicture}}\n"
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)
		t=random.randint(-10,0)
		a = random.choice([i for i in range(-5, 6) if i!=0])
		dap_an=-a-3
		noi_dung=f"Biết rằng với với $m \\le a$ thì hàm số $y = -x^3 + 3x^2 + ({latex(m+a)})x + {random.randint(1,10)}$ nghịch biến trên khoảng $({t}; +\\infty)$. Tìm ${{a}}$."
		
		noi_dung_loigiai=f"Đặt $K=({t};+\\infty)$.\n\n"\
		f"Ta có $y'= -3x^2 + 6x + {latex(m+a)}$.\n\n"\
		f"Hàm số đã cho nghịch biến trên khoảng $(0; +\\infty) \\Leftrightarrow y' \\leq 0, \\forall x \\in K$\n\n"\
		f"$\\Leftrightarrow -3x^2 + 6x + m \\leq 0, \\forall x \\in (0; +\\infty) \\Leftrightarrow m \\leq 3x^2 - 6x, \\forall x \\in K.$\n\n"\
		f"Xét hàm số $f(x) = 3x^2 - 6x$ với $x > 0$.\n\n"\
		f"Ta có $f'(x) = 6x - 6$.\n\n"\
		f"Khi đó $f'(x) = 0 \\Leftrightarrow x =1$.\n\n"\
		f"Bảng biến thiên\n\n"\
		f"{file_name}\n\n"\
		f"Vậy hàm số đã cho nghịch biến trên khoảng $K$ khi ${latex(m+a)} \\leq -3 \\Leftrightarrow m \\le {-a-3}$."

		noi_dung_loigiai_latex=f"Đặt $K=({t};+\\infty)$.\n\n"\
		f"Ta có $y'= -3x^2 + 6x + {latex(m+a)}$.\n\n"\
		f"Hàm số đã cho nghịch biến trên khoảng $(0; +\\infty) \\Leftrightarrow y' \\leq 0, \\forall x \\in K$\n\n"\
		f"$\\Leftrightarrow -3x^2 + 6x + m \\leq 0, \\forall x \\in (0; +\\infty) \\Leftrightarrow m \\leq 3x^2 - 6x, \\forall x \\in K.$\n\n"\
		f"Xét hàm số $f(x) = 3x^2 - 6x$ với $x > 0$.\n\n"\
		f"Ta có $f'(x) = 6x - 6$.\n\n"\
		f"Khi đó $f'(x) = 0 \\Leftrightarrow x =1$.\n\n"\
		f"Bảng biến thiên\n\n"\
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
		f"Vậy hàm số đã cho nghịch biến trên khoảng $K$ khi ${latex(m+a)} \\leq -3 \\Leftrightarrow m \\le {-a-3}$."
	
	
	if chon==2:
		t=random.randint(0,6)
		dap_an=(t+3)**2
		noi_dung=f"Biết rằng với $m^2 \\le a$ thì hàm số $y=\\dfrac{{x^2+5x+m^2+6}}{{x+3}}$ đồng biến trên khoảng $({t};+\\infty)$. Tìm ${{a}}$."

		noi_dung_loigiai=f"Ta có $y'=\\dfrac{{x^2+6x+9-m^2}}{{(x+3)^2}}$, $\\forall x\\neq -3$.\n\n\
		Hàm số đồng biến trên $({t};+\\infty)$ khi và chỉ khi $y'\\ge 0$, $\\forall x>{t}$ \n\n\
			$\\Leftrightarrow  x^2+6x+9-m^2\\ge 0, \\forall x>{t}$ \n\n\
			$\\Leftrightarrow  m^2\\le (x+3)^2, \\forall x>1$\n\n\
			$\\Leftrightarrow  m^2\\le \\min\\limits_{{[{t};+\\infty)}} (x+3)^2$ \n\n\
			$\\Leftrightarrow  m^2\\le {(t+3)**2}\\Leftrightarrow {-t-3}\\le m\\le {t+3}$."

		noi_dung_loigiai_latex=noi_dung_loigiai
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{${{{dap_an}}}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_33]-TL-M2. Tìm m để y=(ax+b)/(x+m) đơn điệu trên các khoảng.
def prt_34_L12_C1_B1_33():
	x,m=sp.symbols("x, m")
	chon=random.randint(1,2)
	if chon==1:
		a=random.randint(1,5)
		b=random.choice([i for i in range(-5, 6) if i!=0])
		c=random.choice([i for i in range(-5, 6) if i!=0])
		d=random.choice([i for i in range(1, 4) if i!=0])	
	if chon==2:
		a=random.randint(-5,-1)
		b=random.choice([i for i in range(-5, 6) if i!=0])
		c=random.choice([i for i in range(-5, 6) if i!=0])
		d=random.choice([i for i in range(-5, -1) if i!=0])	

	chon=random.randint(1,2)	
	
	if chon==1:		
		k=random.choice([-10*i for i in range(5,20) ])
		dem=0
		for i in range(k,-k):
			if all([i>k, i<-k, i>b*c/(a*d)]):
				dem+=1
		dap_an=dem
		
		noi_dung=f"Cho hàm số $f(x)={latex((a*x+b)/(c*x+d*m))}$ với ${{m}}$ là tham số."\
		f" Tìm số giá trị nguyên của ${{m}}$ thuộc khoảng $({k};{-k})$ để hàm số đồng biến trên các khoảng xác định."

		noi_dung_loigiai=(f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{latex(-d*m/c)}\\}}$.\n\n"
		f"$f'(x)=\\dfrac{{{latex(a*d*m-b*c)}}} {{{latex((c*x+d*m)**2)}}}$.\n\n"
		f"Để hàm số đồng biến trên các khoảng xác định thì:\n\n"		
		f"${latex(a*d*m-b*c)}>0 \\Rightarrow m>{phan_so(b*c/(a*d))}$.\n\n"		
		f"Số các số nguyên là: ${{{dap_an}}}$.")
	
	if chon==2:		
		k=random.choice([-10*i for i in range(5,20) ])
		dem=0
		for i in range(k,-k):
			if all([i>k, i<-k, i<b*c/(a*d)]):
				dem+=1
		dap_an=dem

		noi_dung=f"Cho hàm số $f(x)={latex((a*x+b)/(c*x+d*m))}$ với ${{m}}$ là tham số."\
		f" Tìm số giá trị nguyên của ${{m}}$ thuộc khoảng $({k};{-k})$ để hàm số nghịch biến trên các khoảng xác định."

		noi_dung_loigiai=(f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{latex(-d*m/c)}\\}}$.\n\n"
		f"$f'(x)=\\dfrac{{{latex(a*d*m-b*c)}}} {{{latex((c*x+d*m)**2)}}}$.\n\n"
		f"Để hàm số nghịch biến trên các khoảng xác định thì:\n\n"		
		f"${latex(a*d*m-b*c)}<0 \\Rightarrow m<{phan_so(b*c/(a*d))}$.\n\n"		
		f"Số các số nguyên là: ${{{dap_an}}}$.")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{${{{dap_an}}}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_34]-M2. Cho hàm số f'(x). Tìm sô cực trị của y=f(x)
def prt_34_L12_C1_B1_34():
	x=sp.symbols("x")
	x_1=random.randint(-5,-1)
	x_2=x_1+random.randint(1,3)
	x_3=x_2+random.randint(1,3)
	a = random.choice([i for i in range(1, 3) if i!=0])
	f_dh=a*(x-x_1)*(x-x_2)*(x-x_3)
	chon=random.randint(1,8)
	
	if chon==1:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực đại của hàm số $y=f(x)$ là")	
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực đại tại điểm $x={x_2}$."
	
	if chon==2:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực tiểu của hàm số $y=f(x)$ là")
		kq=2
		kq2=1
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại các điểm $x={x_1}, x={x_3}$."

	a = random.choice([i for i in range(-3, -1) if i!=0])
	f_dh=a*(x-x_1)*(x-x_2)*(x-x_3)
	if chon==3:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực đại của hàm số $y=f(x)$ là")	
		kq=2
		kq2=1
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực đại tại các điểm $x={x_1}, x={x_3}$."
	
	if chon==4:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực tiểu của hàm số $y=f(x)$ là")
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại điểm $x={x_2}$."

	a = random.choice([i for i in range(-3, -1) if i!=0])
	f_dh=a*(x-x_1)*(x-x_2)**2*(x-x_3)**3

	if chon==5:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực tiểu của hàm số $y=f(x)$ là")
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại điểm $x={x_1}$."

	if chon==6:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực đại của hàm số $y=f(x)$ là")
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại điểm $x={x_3}$."

	a = random.choice([i for i in range(1, 3) if i!=0])
	n=random.choice([2,4,6])
	m=random.choice([1,3,5 ])
	f_dh=a*(x-x_1)**n*(x-x_2)*(x-x_3)**m

	if chon==7:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực đại của hàm số $y=f(x)$ là")
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại điểm $x={x_2}$."

	if chon==8:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có $f'(x)={latex(f_dh)}$."
		f" Số điểm cực tiểu của hàm số $y=f(x)$ là")
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại điểm $x={x_3}$."


	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
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

#[D12_C1_B1_35]-M2. Cho đồ thị f'(x). Tìm điểm cực trị của y=f(x)
def prt_34_L12_C1_B1_35():
	x=sp.symbols("x")
	x_1=random.randint(-5,1)
	x_2=x_1+random.randint(1,3)
	x_3=x_2+random.randint(1,3)
	chon=random.randint(1,4)
	
	if chon==1 or chon ==2:
		f_dh=(x-x_1)*(x-x_2)*(x-x_3)
		lenh_ve=f"plot (\\x,{{0.2*(\\x-{x_1})*(\\x-{x_2})*(\\x-{x_3})}});"
	if chon==3 or chon ==4:
		f_dh=-(x-x_1)*(x-x_2)*(x-x_3)
		lenh_ve=f"plot (\\x,{{-0.2*(\\x-{x_1})*(\\x-{x_2})*(\\x-{x_3})}});"

	g=diff(f_dh,x)
	equation=Eq(g,0)
	solution = solve(equation, x)
	a,b=solution[0],solution[1]
	y_a,y_b=f_dh.subs(x,a),f_dh.subs(x,b)
	x_min, x_max= round(min(a,b)-3,1), round(max(a,b)+3,1)
	if x_max<=0: x_max=1.5
	if x_min>=0: x_min=-1.5
	y_min, y_max=round(0.5*min(y_a,y_b)-1,1), round(0.5*max(y_a,y_b)+1,1)
	chuoi_so_x=f"\\foreach \\x in {{{x_1}, {x_2},{x_3}}}\n"

	if x_1==0:
		chuoi_so_x=f"\\foreach \\x in {{{x_2},{x_3}}}\n"
	if x_2==0:
		chuoi_so_x=f"\\foreach \\x in {{{x_1},{x_3}}}\n"
	if x_3==0:
		chuoi_so_x=f"\\foreach \\x in {{{x_1},{x_2}}}\n"

	code_hinh=f"\\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.6]\n\
\\tikzset{{every node/.style={{scale=0.9}}}}\n\
\\draw[gray!20]({x_min},{y_min})grid({x_max},{y_max});\n\
\\draw[->] ({x_min},0)--({x_max},0) node[below left] {{$x$}};\n\
\\draw[->] (0,{y_min})--(0,{y_max}) node[below left] {{$y$}};\n\
\\draw (0,0) node [below left] {{\\footnotesize $O$}};\n\
{chuoi_so_x}\
\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {{\\footnotesize $\\x$}};\n\
\\foreach \\y in {{}}\n\
\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {{\\footnotesize $\\y$}};\n\
\\begin{{scope}}\n\
\\clip ({x_min},{y_min}) rectangle ({x_max},{y_max});\n\
\\draw[samples=200,domain={x_1-1}:{x_3+1},smooth,magenta, variable=\\x]\n\
{lenh_ve}\
\\end{{scope}}\n\
\\end{{tikzpicture}}\n"	
	
	if chon==1:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có đồ thị $f'(x)$ như hình vẽ."
		f" Số điểm cực đại của hàm số $y=f(x)$ là")	
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực đại tại điểm $x={x_2}$."
	if chon==2:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có đồ thị $f'(x)$ như hình vẽ."
		f" Số điểm cực tiểu của hàm số $y=f(x)$ là")	
		kq=2
		kq2=1
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại các điểm $x={x_1}, x={x_3}$."

	
	if chon==3:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có đồ thị $f'(x)$ như hình vẽ."
		f" Số điểm cực đại của hàm số $y=f(x)$ là")	
		kq=2
		kq2=1
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực đại tại các điểm $x={x_1}, x={x_3}$."
	
	if chon==4:
		noi_dung=(f"Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{{R}}$ và có đồ thị $f'(x)$ như hình vẽ."
		f" Số điểm cực tiểu của hàm số $y=f(x)$ là")
		kq=1
		kq2=2
		kq3=3
		kq4=0
		noi_dung_loigiai=f"Hàm số đạt cực tiểu tại điểm $x={x_2}$."
	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
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


#[D12_C1_B1_36]-SA-M3. Hàm bậc 3 có đường thẳng qua hai cực trị là y=ax+b. Tính bài toán liên quan.
def prt_34_L12_C1_B1_36():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,3)
	a, b=-(x_1+x_2), x_1*x_2	
	m=random.choice([1,-1,3,-3])
	f_dh= m*(x**2+a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)
	y_1,y_2=f.subs(x,x_1), f.subs(x,x_2)

	p = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	q = random.choice([random.randint(-4, -1), random.randint(1, 4)])

	st_a,st_b=sp.symbols("a b")
			
	noi_dung =(f"Đồ thị hàm số $y=f(x)={latex(f)}$ có các điểm cực trị là $A,B$."
	f" Đường thẳng đi qua ${{A}}$ và ${{B}}$ có phương trình $y=ax+b$. Tính ${latex(p*st_a+q*st_b)}$ (kết quả làm tròn đến hàng phần mười).")

	
	k_a=(y_2-y_1)/(x_2-x_1)
	k_b=-k_a*x_1+y_1
	dap_an=f"{round(p*k_a + q*k_b,1)}".replace(".",",")

	noi_dung_loigiai=(f"$f'(x)={latex(f_dh)}$.\n\n"
		f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"
		f"Hàm số đạt cực trị tại các điểm $x_1={x_1}$, $x_2={x_2}$.\n\n"
		f"$y_1=f({x_1})={phan_so(y_1)}, y_2=f({x_2})={phan_so(y_2)}$.\n\n"
		f"Đường thẳng ${{d}}$ đi qua các điểm $A\\left({x_1};{phan_so(y_1)}\\right), B\\left({x_2};{phan_so(y_2)}\\right)$ có hệ số góc là:\n\n"
		f"$k=\\dfrac{{{phan_so(y_2)}-{phan_so(y_1)}}}{{{x_2}-{x_1}}}={phan_so(k_a)}$.\n\n"
		f"Phương trình ${{d}}$: $y={phan_so(k_a)}(x-{x_1})+{phan_so(y_1)}$"
		f"$\\Leftrightarrow y={phan_so(k_a)}x+{phan_so(k_b)}$.\n\n"
		f"Ta có: $a={phan_so(k_a)},b={phan_so(k_b)}\\Rightarrow {latex(p*st_a+q*st_b)}={dap_an}$."
		
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("--","+").replace("-+","-")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n Đáp án: {dap_an}"
	

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{${dap_an}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B1_37]-SA-M3. Hàm bậc 2/bậc 1 có đường thẳng qua hai cực trị là y=ax+b. Tính bài toán liên quan.
def prt_34_L12_C1_B1_37():
	x=sp.symbols("x")
	x_1=random.choice([2*i for i in range(-10,10)])
	i=random.randint(1,5)
	x_2=x_1+2*i
	b, c, =(x_1+x_2), x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)
	
	a=random.choice([-1,1,-2,2])
	f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)

	y_1=f_ok.subs(x,x_1)
	y_2=f_ok.subs(x,x_2)

	p = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	q = random.choice([random.randint(-4, -1), random.randint(1, 4)])

	st_a,st_b=sp.symbols("a b")
			
	noi_dung =(f"Đồ thị hàm số $y=f(x)={latex(f_ok)}$ có các điểm cực trị là $A,B$."
	f" Đường thẳng đi qua ${{A}}$ và ${{B}}$ có phương trình $y=ax+b$. Tính ${latex(p*st_a+q*st_b)}$ (kết quả làm tròn đến hàng phần mười).")

	
	k_a=(y_2-y_1)/(x_2-x_1)
	k_b=-k_a*x_1+y_1
	dap_an=f"{round(p*k_a + q*k_b,1)}".replace(".",",")

	noi_dung_loigiai=(f"$f'(x)={latex(a*g)}$.\n\n"
		f"$f'(x)=0 \\Leftrightarrow x={x_1}$ hoặc $x={x_2}$.\n\n"
		f"Lập bảng biến thiên.\n\n"\
		f"Hàm số đạt cực trị tại $x_1={x_1}$, $x_2={x_2}$.\n\n"
		f"$y_1=f({x_1})={phan_so(y_1)}, y_2=f({x_2})={phan_so(y_2)}$.\n\n"

		f"Đường thẳng ${{d}}$ đi qua các điểm $A\\left({x_1};{phan_so(y_1)}\\right), B\\left({x_2};{phan_so(y_2)}\\right)$ có hệ số góc là:\n\n"
		f"$k=\\dfrac{{{phan_so(y_2)}-{phan_so(y_1)}}}{{{x_2}-{x_1}}}={phan_so(k_a)}$.\n\n"
		f"Phương trình ${{d}}$: $y={phan_so(k_a)}(x-{x_1})+{phan_so(y_1)}$"
		f"$\\Leftrightarrow y={phan_so(k_a)}x+{phan_so(k_b)}$.\n\n"
		f"Ta có: $a={phan_so(k_a)},b={phan_so(k_b)}\\Rightarrow {latex(p*st_a+q*st_b)}={dap_an}$."	
		
		)
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("--","+").replace("-+","-")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n Đáp án: {dap_an}"
	

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{${dap_an}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an
#BÀI 2: GIÁ TRỊ LỚN NHẤT- GIÁ TRỊ NHỎ NHẤT

#[D12_C1_B2_01]-M2. Tìm GTLN-GTNN của hàm bậc 3 trên đoạn
def prt_34_L12_C1_B2_01():
	x = sp.symbols('x')
	x_1=random.randint(-4,1)
	x_2=x_1+random.randint(3,5)
	
	k=random.choice([1,-1,3,-3])	

	g=(x-x_1)*(x-x_2)
	f=k*integrate(g,x)+random.randint(-5,5)

	a=f.coeff(x,3)
	b=f.coeff(x,2)
	c=f.coeff(x,1)
	d=f.as_coefficients_dict()[1]

	# Tạo đoạn [m,n]
	m= random.randint(x_1-4,x_1-1)
	n= random.randint(x_2+1,x_2+4)

	#Tính giá trị tại các điểm
	y_m=f.subs(x,m)
	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)
	y_n=f.subs(x,n)

	#Tạo giá trị ảo
	y_3=f.subs(x,m-1)
	y_4=f.subs(x,n+1)

	giatri_max=max(y_m,y_1,y_2,y_n)
	giatri_min=min(y_m,y_1,y_2,y_n)

	gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":
		ten = "M"
		kq=giatri_max
		kq2=giatri_min
		kq3=y_3
		kq4=y_4
	else:
		ten = "m"
		kq=giatri_min
		kq2=giatri_max
		kq3=y_3
		kq4=y_4

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${ten}={phan_so(kq)}$"
	pa_B= f"${ten}={phan_so(kq2)}$"
	pa_C= f"${ten}={phan_so(kq3)}$"
	pa_D= f"${ten}={phan_so(kq4)}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$."	
	noi_dung_loigiai=f"$y'={latex(expand(k*g))}$.\n\n"\
	f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
	f"$f({m})={phan_so(y_m)}, f({x_1})={phan_so(y_1)},f({x_2})={phan_so(y_2)}, f({n})={phan_so(y_n)}$.\n\n"\
	f"Vậy {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ là ${phan_so(kq)}$."

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

#[D12_C1_B2_02]. Tìm GTLN-GTNN của hàm y=(ax+b)/(cx+d) trên đoạn
def prt_34_L12_C1_B2_02():
	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	c = random.choice([random.randint(-7, -1), random.randint(1, 7)])
	d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a*d-b*c==0:
		d = d+1
	x_0=-d/c
	#Tạo đoạn [m;n]
	chon_ben=random.choice(["trái","phải"])
	if chon_ben=="trái":
		n = random.choice([int(x_0)-4,int(x_0)-1])
		m = n-random.randint(1,10)
	else:
		m = random.choice([int(x_0)+1,int(x_0)+4])
		n = m + random.randint(1,10)
	x_1=m
	x_2=n

	x=sp.symbols("x")
	f=(a*x+b)/(c*x+d)
	#Tính giá trị hai đầu mút
	y_m= f.subs(x,m)
	y_n=f.subs(x,n)

	gia_tri = random.choice(["giá trị lớn nhất", "giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":
		ten="M"		
		if a*d-b*c>0:
			y_1=y_m-random.randint(1,5)
			y_2=y_n+random.randint(1,5)
			kq = f"{ten}={phan_so(y_n)}"
			kq2= f"{ten}={phan_so(y_m)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"
			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị lớn nhất tại $x={n}, M=f({n})={phan_so(y_n)}$."
		else:
			y_1=y_m+random.randint(1,5)
			y_2=y_n-random.randint(1,5)
			kq = f"{ten}={phan_so(y_m)}"
			kq2= f"{ten}={phan_so(y_n)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"

			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị lớn nhất tại $x={m}, M=f({m})={phan_so(y_m)}$."

	else:
		ten="m"
		if a*d-b*c>0:
			y_1=y_m-random.randint(1,5)
			y_2=y_n+random.randint(1,5)
			kq = f"{ten}={phan_so(y_m)}"
			kq2= f"{ten}={phan_so(y_n)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"
			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị nhỏ nhất tại $x={m}, m=f({m})={phan_so(y_m)}$."
		else:
			y_1=y_m+random.randint(1,5)
			y_2=y_n-random.randint(1,5)
			kq = f"{ten}={phan_so(y_n)}"
			kq2= f"{ten}={phan_so(y_m)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"
			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị nhỏ nhất tại $x={n}, m=f({n})={phan_so(y_n)}$."

	pa_A= f"*$\\displaystyle {{{kq}}}$"
	pa_B= f"$\\displaystyle {{{kq2}}}$"
	pa_C= f"$\\displaystyle {{{kq3}}}$"
	pa_D= f"$\\displaystyle {{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$."
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

#[D12_C1_B2_03]-M2. Tìm GTLN-GTNN của hàm bậc 3 trên khoảng
def prt_34_L12_C1_B2_03():
	x = sp.symbols('x')
	x_1=random.randint(-4,1)
	x_2=x_1+random.randint(3,5)
	
	k=random.choice([1,-1,3,-3])	

	g=(x-x_1)*(x-x_2)
	f=k*integrate(g,x)+random.randint(-5,5)
	a=f.coeff(x,3)
	b=f.coeff(x,2)
	c=f.coeff(x,1)
	d=f.as_coefficients_dict()[1]
	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)	
	code_hinh=code_bbt_bac3_2nghiem(a,x_1,x_2,phan_so(y_1),phan_so(y_2))
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	if k>0:
		chon=random.randint(1,2)
		if chon==1:
			m= random.randint(x_1,x_2-1)
			khoang=random.choice([f"khoảng $({m};+\\infty)$", f"khoảng $({m};{x_2+random.randint(1,4)})$", f"nửa khoảng $({m};{x_2+random.randint(1,4)}]$"])
			noi_dung = f"Tìm giá trị nhỏ nhất của hàm số $\\displaystyle y={latex(f)}$ trên {khoang}.\n"
			noi_dung_loigiai=f"$y'={latex(expand(k*g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị nhỏ nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."
			
			noi_dung_loigiai_latex=f"$y'={latex(expand(k*g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị nhỏ nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."
			kq=phan_so(y_2)
			kq2=phan_so(y_1)
			kq3=phan_so(y_1-3)
			kq4=phan_so(y_2+random.randint(1,2))
		if chon==2:
			# Tạo khoảng (-vc; m)
			m= random.randint(x_1,x_2-1)
			khoang=random.choice([f"khoảng $(-\\infty;{m})$",f"khoảng $({x_1-random.randint(1,4)};{m})$",f"nửa khoảng $[{x_1-random.randint(1,4)};{m})$" ])
			noi_dung = f"Tìm giá trị lớn nhất của hàm số $\\displaystyle y={latex(f)}$ trên {khoang}.\n"
			noi_dung_loigiai=f"$y'={latex(expand(k*g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_1})={phan_so(y_1)}$."

			noi_dung_loigiai_latex=f"$y'={latex(expand(k*g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_1})={phan_so(y_1)}$."
			kq=phan_so(y_1)
			kq2=phan_so(y_2)
			kq3=phan_so(y_1-3)
			kq4=phan_so(y_2+random.randint(1,2))

	if k<0:
		chon=random.randint(1,2)

		if chon==1:
			m= random.randint(x_1,x_2-1)
			khoang=random.choice([f"khoảng $({m};+\\infty)$", f"khoảng $({m};{x_2+random.randint(1,4)})$", f"nửa khoảng $({m};{x_2+random.randint(1,4)}]$"])
			noi_dung = f"Tìm giá trị lớn nhất của hàm số $\\displaystyle y={latex(f)}$ trên {khoang}.\n"
			noi_dung_loigiai=f"$y'={latex(expand(g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."
			
			noi_dung_loigiai_latex=f"$y'={latex(expand(g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."
			kq=phan_so(y_2)
			kq2=phan_so(y_1)
			kq3=phan_so(y_1-3)
			kq4=phan_so(y_2+random.randint(1,2))
		if chon==2:
			# Tạo khoảng (-vc; m)
			m= random.randint(x_1,x_2-1)
			khoang=random.choice([f"khoảng $(-\\infty;{m})$",f"khoảng $({x_1-random.randint(1,4)};{m})$",f"nửa khoảng $[{x_1-random.randint(1,4)};{m})$" ])
			noi_dung = f"Tìm giá trị nhỏ nhất của hàm số $\\displaystyle y={latex(f)}$ trên {khoang}.\n"
			noi_dung_loigiai=f"$y'={latex(expand(g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị nhỏ nhất hàm số trên {khoang} là $f({x_1})={phan_so(y_1)}$."

			noi_dung_loigiai_latex=f"$y'={latex(expand(g))}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị nhỏ nhất hàm số trên {khoang} là $f({x_1})={phan_so(y_1)}$."
			kq=phan_so(y_1)
			kq2=phan_so(y_2)
			kq3=phan_so(y_1-3)
			kq4=phan_so(y_2+random.randint(1,2))
		

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
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
		f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B2_04]. Tìm GTLN-GTNN của hàm y=(ax+b)/(cx+d) trên nửa khoảng
def prt_34_L12_C1_B2_04():
	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	c = random.choice([random.randint(-7, -1), random.randint(1, 7)])
	d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a*d-b*c==0:
		d = d+1
	x_0=-d/c
	#Tạo đoạn [m;n]
	chon_ben=random.choice(["trái","phải"])
	if chon_ben=="trái":
		n = random.choice([int(x_0)-4,int(x_0)-1])
		m = n-random.randint(1,10)
	else:
		m = random.choice([int(x_0)+1,int(x_0)+4])
		n = m + random.randint(1,10)
	x_1=m
	x_2=n

	x=sp.symbols("x")
	f=(a*x+b)/(c*x+d)
	#Tính giá trị hai đầu mút
	y_m= f.subs(x,m)
	y_n=f.subs(x,n)

	gia_tri = random.choice(["giá trị lớn nhất", "giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":
		ten="M"				
		if a*d-b*c>0:
			noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{({m};{n}]}}$."
			y_1=y_m-random.randint(1,5)
			y_2=y_n+random.randint(1,5)
			kq = f"{ten}={phan_so(y_n)}"
			kq2= f"{ten}={phan_so(y_m)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"
			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị lớn nhất trên nửa khoảng ${{({m};{n}]}}$ tại $x={n}, M=f({n})={phan_so(y_n)}$."
		else:
			noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{[{m};{n})}}$."
			y_1=y_m+random.randint(1,5)
			y_2=y_n-random.randint(1,5)
			kq = f"{ten}={phan_so(y_m)}"
			kq2= f"{ten}={phan_so(y_n)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"

			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị lớn nhất trên nửa khoảng ${{[{m};{n})}}$ tại $x={m}, M=f({m})={phan_so(y_m)}$."

	else:
		ten="m"
		if a*d-b*c>0:
			noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{[{m};{n})}}$."
			y_1=y_m-random.randint(1,5)
			y_2=y_n+random.randint(1,5)
			kq = f"{ten}={phan_so(y_m)}"
			kq2= f"{ten}={phan_so(y_n)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"
			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị nhỏ nhất trên nửa khoảng ${{[{m};{n})}}$ tại $x={m}, m=f({m})={phan_so(y_m)}$."
		else:
			noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{({m};{n}]}}$."
			y_1=y_m+random.randint(1,5)
			y_2=y_n-random.randint(1,5)
			kq = f"{ten}={phan_so(y_n)}"
			kq2= f"{ten}={phan_so(y_m)}"
			kq3= f"{ten}={phan_so(y_1)}"
			kq4= f"{ten}={phan_so(y_2)}"
			noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
			f"Hàm số đạt giá trị nhỏ nhất trên nửa khoảng ${{({m};{n}]}}$ tại $x={n}, m=f({n})={phan_so(y_n)}$."

	pa_A= f"*$\\displaystyle {{{kq}}}$"
	pa_B= f"$\\displaystyle {{{kq2}}}$"
	pa_C= f"$\\displaystyle {{{kq3}}}$"
	pa_D= f"$\\displaystyle {{{kq4}}}$"
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

#[D12_C1_B2_05]-M2. Tìm GTLN-GTNN của hàm y=ax+b/x trên khoảng
def prt_34_L12_C1_B2_05():
	x=sp.symbols("x")
	a = random.randint(1, 9)
	b = random.randint(1, 9)
	f=a*x+b/x
	x_1, x_2 = -sqrt(b/a), sqrt(b/a)
	y_1, y_2 = nsimplify(f.subs(x,x_1)), nsimplify(f.subs(x,x_2))
	chon=random.randint(1,2)
	code_hinh=code_bbt_phanthucbac2(a,0,b,1,0)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	if chon==1:		
		t=random.randint(0,int(sqrt(b/a)))
		chon=random.randint(1,2)
		if chon==1:
			kihieu=f"({t};+\\infty)"
			khoang=f"khoảng $({t};+\\infty)$"
		if chon==2:
			kihieu=f"[{t};+\\infty)"
			khoang= f"nửa khoảng $[{t};+\\infty)$"

		noi_dung=f"Giá trị nhỏ nhất của hàm số $y={latex(f)}$ cho trên {khoang} bằng"
		noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
		f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
		f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
		f"Bảng biến thiên:\n\n"\
		f"{file_name}\n\n"\
		f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_2)}$.\n\n"

		noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
		f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
		f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
		f"Bảng biến thiên:\n\n"\
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
		f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_2)}$.\n\n"

		kq=latex(y_2)
		kq2=latex(y_1)
		kq3=latex(y_2+random.randint(1,3))
		kq4=latex(y_1-random.randint(1,3))

	if chon==2:
		t=random.randint(-int(sqrt(b/a)),0)
		chon=random.randint(1,2)
		if chon==1:
			kihieu=f"(-\\infty;{t})"
			khoang=f"khoảng $(-\\infty;{t})$"
		if chon==2:
			kihieu=f"(-\\infty;{t}]"
			khoang= f"nửa khoảng $(-\\infty;{t})$"

		noi_dung=f"Giá trị lớn nhất của hàm số $y={latex(f)}$ trên {khoang} bằng"
		noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
		f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
		f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
		f"Bảng biến thiên:\n\n"\
		f"{file_name}\n\n"\
		f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left(-{latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_1)}$.\n\n"

		noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
		f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
		f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
		f"Bảng biến thiên:\n\n"\
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
		f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left(-{latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_1)}$.\n\n"

		kq=latex(y_1)
		kq2=latex(y_2)
		kq3=latex(y_2+random.randint(1,3))
		kq4=latex(y_1-random.randint(1,3))
		

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
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
		f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B2_06]-M2. Tìm GTLN-GTNN của hàm y=(ax^2+bx+c)/(dx+e) trên khoảng
def prt_34_L12_C1_B2_06():
	x=sp.symbols("x")

	x_1=random.choice([2*i for i in range(-5,5)])
	i=random.randint(1,3)
	x_2=x_1+2*i

	b, c, =x_1+x_2, x_1*x_2 
	x_0=int(b/2)

	#Tạo hàm số g là đạo hàm của f
	g=(x**2-b*x+c)/((x-x_0)**2)
	g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
	c2=x_0**2-c

	#Tìm hàm f là nguyên hàm của g
	f=integrate(g,x)
	f1=integrate(g1,x)	
	a=random.choice([1,2])
	f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)

	y_1=f_ok.subs(x,x_1)
	y_2=f_ok.subs(x,x_2)
	if a>0:
		chon=random.randint(1,2)
		
		code_hinh =f"\\begin{{tikzpicture}}[scale=1]\n\
	    \\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
	    {{$x$ /1,$y'$ /1,$y$ /2}}\n\
	    {{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
	\\tkzTabLine{{ ,+,z,-,d,-,z,+, }}\n\
	\\tkzTabVar{{-/$-\\infty$,+/${phan_so(y_1)}$,-D+/$-\\infty$/$+\\infty$,-/${phan_so(y_2)}$,+/$+\\infty$}}\n\
	    \\end{{tikzpicture}}\n"

		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)
		
		if chon==1:		
			t=random.choice([x_0,phan_so((x_0+x_2)/2)])
			
			kihieu=f"({t};+\\infty)"
			khoang=f"khoảng $({t};+\\infty)$"
			

			noi_dung=f"Giá trị nhỏ nhất của hàm số $y={latex(f_ok)}$ cho trên {khoang} bằng"
			noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
			f"$y'={latex(a*g)}$.\n\n"\
			f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"{file_name}\n"\
			f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_2} \\right)={latex(y_2)}$.\n\n"

			noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
			f"$y'={latex(a*g)}$.\n\n"\
			f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
			f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_2} \\right)={latex(y_2)}$.\n\n"

			kq=latex(y_2)
			kq2=latex(y_1)
			kq3=latex(y_2+random.randint(1,3))
			kq4=latex(y_1-random.randint(1,3))

		if chon==2:
			t=random.choice([x_0, phan_so((x_0+x_1)/2)])
				
			kihieu=f"(-\\infty;{t})"
			khoang=f"khoảng $(-\\infty;{t})$"


			noi_dung=f"Giá trị lớn nhất của hàm số $y={latex(f_ok)}$ trên {khoang} bằng"

			noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
			f"$y'={latex(a*g)}$.\n\n"\
			f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"{file_name}\n"\
			f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_1} \\right)={latex(y_1)}$.\n\n"

			noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
			f"$y'={latex(a*g)}$.\n\n"\
			f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
			f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_1} \\right)={latex(y_1)}$.\n\n"

			kq=latex(y_1)
			kq2=latex(y_2)
			kq3=latex(y_2+random.randint(1,3))
			kq4=latex(y_1-random.randint(1,3))		

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
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
		f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D12_C1_B2_07]-TF-M2. Cho hàm số bậc 3. Xét Đ-S: y', y'=0,	f(x_0), Min-Max trên đoạn
def prt_34_L12_C1_B2_07():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(1,3)
	a, b=x_1+x_2, x_1*x_2	
	m=random.choice([1,-1,3,-3,6,-6])
	f_dh= m*(x**2-a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)
	noi_dung=f"Cho hàm số $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau"

	kq1_T=f"*$y'={latex(f_dh)}$" 
	kq1_F=f"$y'={latex(f_dh+random.randint(-3,-1)*x+random.randint(-2,2)*x**2)}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$y={latex(f)} \\Rightarrow y'={latex(f_dh)}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*$y'=0$ khi $x={x_1},x={x_2}$"
	kq2_F=f"{random.choice([f"$y'=0$ vô nghiệm",f"$y'=0$ khi $x={x_1-random.randint(1,3)},x={x_2+random.randint(0,3)}$"])} "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"$y'={latex(f_dh)}\\Rightarrow y'=0$ khi $x={x_1},x={x_2}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	m= random.randint(x_1-4,x_1-1)
	n= random.randint(x_2+1,x_2+4)
	x_0=random.choice([m,n,x_1,x_2])

	kq3_T=f"*$y({x_0})={phan_so(f.subs(x,x_0))}$" 
	kq3_F=f"$y({x_0})={phan_so(f.subs(x,x_0)+random.randint(1,6))}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$y={latex(f)}\\Rightarrow y({x_0})= {f.subs(x,x_0)}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	y_m=f.subs(x,m)
	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)
	y_n=f.subs(x,n)
	gt_max=max(y_m,y_1,y_2,y_n)
	gt_min=min(y_m,y_1,y_2,y_n)

	chon=random.randint(1,2)
	if chon==1:
		kq4_T=f"*Giá trị nhỏ nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(gt_min)}}}$"
		kq4_F=f"Giá trị nhỏ nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(gt_max)}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$y({m})={phan_so(y_m)}, y({x_1})={phan_so(y_1)}, y({x_2})={phan_so(y_2)}, y({n})={phan_so(y_n)}$.\n\n"\
		f"Do đó: $\\mathop{{\\min}}\\limits_{{[{m};{n}]}} {{y}}={phan_so(gt_min)}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==2:
		kq4_T=f"*Giá trị lớn nhất của hàm số trên đoạn ${{[{m};{n}]}}$ là ${{{phan_so(gt_max)}}}$"
		kq4_F=f"Giá trị lớn nhất của hàm số trên đoạn ${{[{m};{n}]}}$ là ${{{phan_so(gt_min)}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$y({m})={phan_so(y_m)}, y({x_1})={phan_so(y_1)}, y({x_2})={phan_so(y_2)}, y({n})={phan_so(y_n)}$.\n\n"\
		f"Do đó: $\\mathop{{\\max}}\\limits_{{[{m};{n}]}} {{y}}={phan_so(gt_max)}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B2_08]-TF-M2. Cho y=(ax+b)/(cx+d). Xét Đ-S: y', dấu y',	f(x_0), Min-Max trên đoạn
def prt_34_L12_C1_B2_08():
	x=sp.symbols("x")
	a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	b = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	c = random.choice([random.randint(-7, -1), random.randint(1, 7)])
	d = random.choice([random.randint(-8, -1), random.randint(1, 8)])
	if a*d-b*c==0:
		d = d+1	
	f=(a*x+b)/(c*x+d)	
	noi_dung=f"Cho hàm số $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau"

	f_dh=f"\\dfrac{{{a*d-b*c}}}{{({latex(c*x+d)})^2}}"
	f_dh_false=f"\\dfrac{{{-a*d+b*c}}}{{({latex(c*x+d)})^2}}"

	kq1_T=f"*$y'={f_dh}$" 
	kq1_F=f"$y'={f_dh_false}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$y={latex(f)} \\Rightarrow y'={f_dh}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if a*d-b*c>0:
		kq2_T=f"*$y'>0$ với mọi $x\\ne {phan_so(-d/c)}$"
		kq2_F=f"$y'<0$ với mọi $x\\ne {phan_so(-d/c)}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'={f_dh}\\Rightarrow y'>0$ với mọi $x\\ne {phan_so(-d/c)}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	else:
		kq2_T=f"*$y'<0$ với mọi $x\\ne {phan_so(-d/c)}$"
		kq2_F=f"$y'>0$ với mọi $x\\ne {phan_so(-d/c)}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'={f_dh}\\Rightarrow y'<0$ với mọi $x\\ne {phan_so(-d/c)}$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Tạo đoạn [m;n]
	x_0=-d/c
	chon_ben=random.choice(["trái","phải"])
	if chon_ben=="trái":
		n = random.choice([int(x_0)-4,int(x_0)-1])
		m = n-random.randint(1,5)
	else:
		m = random.choice([int(x_0)+1,int(x_0)+4])
		n = m + random.randint(1,5)

	x_0=random.choice([m,n])
	if x_0==m:
		y_0=f.subs(x,m)
		y_0_false=f.subs(x,n)
	else:
		y_0=f.subs(x,n)
		y_0_false=f.subs(x,m)

	kq3_T=f"*$y({x_0})={phan_so(y_0)}$" 
	kq3_F=f"$y({x_0})={phan_so(y_0_false)}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$y={latex(f)}\\Rightarrow y({x_0})= {phan_so(y_0)}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	y_m=f.subs(x,m)
	y_n=f.subs(x,n)

	if a*d-b*c>0:
		chon=random.randint(1,2)
		if chon==1:
			kq4_T=f"*Giá trị nhỏ nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(y_m)}}}$"
			kq4_F=f"Giá trị nhỏ nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(y_n)}}}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'={f_dh}>0, \\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"$y({m})={phan_so(y_m)}, y({n})={phan_so(y_n)}$.\n\n"\
			f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
			f"Do đó: $\\mathop{{\\min}}\\limits_{{[{m};{n}]}} {{y}}={phan_so(y_m)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==2:
			kq4_T=f"*Giá trị lớn nhất của hàm số trên đoạn ${{[{m};{n}]}}$ là ${{{phan_so(y_n)}}}$"
			kq4_F=f"Giá trị lớn nhất của hàm số trên đoạn ${{[{m};{n}]}}$ là ${{{phan_so(y_m)}}}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'={f_dh}>0, \\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"$y({m})={phan_so(y_m)}, y({n})={phan_so(y_n)}$.\n\n"\
			f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
			f"Do đó: $\\mathop{{\\max}}\\limits_{{[{m};{n}]}} {{y}}={phan_so(y_n)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if a*d-b*c<0:
		chon=random.randint(1,2)
		if chon==1:
			kq4_T=f"*Giá trị nhỏ nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(y_n)}}}$"
			kq4_F=f"Giá trị nhỏ nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(y_m)}}}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'={f_dh}>0, \\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"$y({m})={phan_so(y_m)}, y({n})={phan_so(y_n)}$.\n\n"\
			f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
			f"Do đó: $\\mathop{{\\min}}\\limits_{{[{m};{n}]}} {{y}}={phan_so(y_n)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if chon==2:
			kq4_T=f"*Giá trị lớn nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(y_m)}}}$"
			kq4_F=f"Giá trị lớn nhất của hàm số trên đoạn ${{[{m};{n}]}}$ bằng ${{{phan_so(y_n)}}}$" 
			kq4=random.choice([kq4_T, kq4_F])
			HDG=f"$y'={f_dh}>0, \\forall x \\ne {phan_so(-d/c)}$.\n\n"\
			f"$y({m})={phan_so(y_m)}, y({n})={phan_so(y_n)}$.\n\n"\
			f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
			f"Do đó: $\\mathop{{\\max}}\\limits_{{[{m};{n}]}} {{y}}={phan_so(y_m)}$."
			loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq4==kq4_F:
				loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B2_09]-TF-M2. Cho hàm số bậc 3. Xét Đ-S: y', y'=0,	f(x_0), Min-Max trên khoảng
def prt_34_L12_C1_B2_09():
	x=sp.symbols("x")
	x_1 = random.randint(-5,5)
	x_2 = x_1 + random.randint(2,3)
	a, b=-(x_1+x_2), x_1*x_2	
	k=random.choice([1,-1,3,-3,6,-6])
	f_dh= k*(x**2+a*x+b)
	f=integrate(f_dh,x)+random.randint(-3,3)

	noi_dung=f"Cho hàm số $y={latex(f)}	$. Xét tính đúng-sai của các khẳng định sau"

	kq1_T=f"*$y'={latex(f_dh)}$" 
	kq1_F=f"$y'={latex(f_dh+random.randint(-2,2)*x+random.randint(-2,2)*x**2)}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$y={latex(f)} \\Rightarrow y'={latex(f_dh)}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*$y'=0$ khi $x={x_1},x={x_2}$"
	kq2_F=f"{random.choice([f"$y'=0$ vô nghiệm",f"$y'=0$ khi $x={x_1-random.randint(1,3)},x={x_2+random.randint(0,3)}$"])} "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"$y'={latex(f_dh)}\\Rightarrow y'=0$ khi $x={x_1},x={x_2}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	m= random.randint(x_1-4,x_1-1)
	n= random.randint(x_2+1,x_2+4)
	x_0=random.choice([m,n,x_1,x_2])


	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)

	code_hinh=code_bbt_bac3_2nghiem(k,x_1,x_2,phan_so(y_1),phan_so(y_2))
	code = my_module.moi_truong_anh_latex(code_hinh)
	#file_name=my_module.pdftoimage_timename(code)
	file_name=""

	if k>0:
		chon=random.randint(1,2)
		if chon==1:
			m= random.choice([x_1, f"{phan_so(x_1+0.5)}", f"{phan_so(x_1+0.2)}", f"{phan_so(x_1+0.4)}" ])
			khoang=random.choice([f"khoảng $({m};+\\infty)$", f"khoảng $({m};{x_2+random.randint(1,4)})$", f"nửa khoảng $({m};{x_2+random.randint(1,4)}]$"])
			
			kq3_T=f"*Giá trị nhỏ nhất của hàm số trên {khoang} bằng ${phan_so(y_2)}$"
			kq3_F=f"Giá trị nhỏ nhất của hàm số trên {khoang} bằng ${phan_so(y_1)}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị nhỏ nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."

			HDG_latex=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị nhỏ nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."			

		if chon==2:
			# Tạo khoảng (-vc; m)
			m= random.choice([x_2, f"{phan_so(x_2-0.5)}", f"{phan_so(x_2-0.2)}", f"{phan_so(x_2-0.4)}" ])
			khoang=random.choice([f"khoảng $(-\\infty;{m})$",f"khoảng $({x_1-random.randint(1,4)};{m})$",f"nửa khoảng $[{x_1-random.randint(1,4)};{m})$" ])
			
			kq3_T=f"*Giá trị lớn nhất của hàm số trên {khoang} bằng ${phan_so(y_1)}$"
			kq3_F=f"Giá trị lớn nhất của hàm số trên {khoang} bằng ${phan_so(y_2)}$" 
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_1)}$."

			HDG_latex=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_1)}$."			
			

	if k<0:
		chon=random.randint(1,2)
		if chon==1:
			m= random.choice([x_2, f"{phan_so(x_2-0.5)}", f"{phan_so(x_2-0.2)}", f"{phan_so(x_2-0.4)}" ])
			
			khoang=random.choice([f"khoảng $({m};+\\infty)$", f"khoảng $({m};{x_2+random.randint(1,4)})$", f"nửa khoảng $({m};{x_2+random.randint(1,4)}]$"])
			kq3_T=f"*Giá trị lớn nhất của hàm số trên {khoang} bằng ${phan_so(y_2)}$"
			kq3_F=f"Giá trị lớn nhất của hàm số trên {khoang} bằng ${phan_so(y_1)}$" 
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."

			HDG_latex=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_2})={phan_so(y_2)}$."

		if chon==2:
			# Tạo khoảng (-vc; m)
			m= random.choice([x_1, f"{phan_so(x_1+0.5)}", f"{phan_so(x_1+0.2)}", f"{phan_so(x_1+0.4)}" ])
			khoang=random.choice([f"khoảng $(-\\infty;{m})$",f"khoảng $({x_1-random.randint(1,4)};{m})$",f"nửa khoảng $[{x_1-random.randint(1,4)};{m})$" ])
			kq3_T=f"*Giá trị nhỏ nhất của hàm số trên {khoang} bằng ${phan_so(y_1)}$"
			kq3_F=f"Giá trị nhỏ nhất của hàm số trên {khoang} bằng ${phan_so(y_2)}$" 
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Lập bảng biến thiên.\n\n"\
				f"{file_name}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_1})={phan_so(y_1)}$."

			HDG_latex=f"$y'={latex(f_dh)}$.\n\n"\
				f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
				f"Bảng biến thiên.\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"Dựa vào bảng biến thiên ta có giá trị lớn nhất hàm số trên {khoang} là $f({x_1})={phan_so(y_1)}$."
	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	loigiai_3_latex=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG_latex}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		loigiai_3_latex=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG_latex}"


	t= random.choice([i for i in range(-10, 10) if i!=0])
	chon=random.randint(1,2)
	if chon==1:
		gt_max=max(abs(y_1), abs(y_2))
		gt_max_false=gt_max+random.choice([i for i in range(-3, 3) if i!=0])
		kq4_T=f"* Giá trị lớn nhất của hàm số $y=|f(x)|+{t}$ trên đoạn $[{{{x_1};{x_2}}}]$ bằng ${{{phan_so(gt_max+t)}}}$".replace("+-","-")
		kq4_F=f" Giá trị lớn nhất của hàm số $y=|f(x)|+{t}$ trên đoạn $[{{{x_1};{x_2}}}]$ bằng ${{{phan_so(gt_max_false+t)}}}$".replace("+-","-")
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"$\\mathop{{\\max}}\\limits_{{[{x_1};{x_2}]}} {{(|f(x)|+{t})}}=\\mathop{{\\max}}\\limits_{{[{x_1};{x_2}]}} |f(x)|+{t}$"
		f"$=\\max\\left(|{phan_so(y_1)}|,|{phan_so(y_2)}|\\right)+{t}={phan_so(gt_max)}+{t}={phan_so(gt_max+t)}$."
		)
		HDG=HDG.replace("+-","-")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	
	if chon==2:
		if y_1*y_2<0:
			gt_min=0
			gt_min_false=min(abs(y_1),abs(y_2))
			HDG=(f"$\\mathop{{\\min}}\\limits_{{[{x_1};{x_2}]}} {{(|f(x)|+{t})}}=\\mathop{{\\min}}\\limits_{{[{x_1};{x_2}]}} |f(x)|+{t}$"
		f"$=0+{t}={phan_so(gt_min+t)}$."
		)
		else:
			gt_min=min(abs(y_1),abs(y_2))
			gt_min_false=0
			HDG=(f"$\\mathop{{\\min}}\\limits_{{[{x_1};{x_2}]}} {{(|f(x)|+{t})}}=\\mathop{{\\min}}\\limits_{{[{x_1};{x_2}]}} |f(x)|+{t}$"
			f"$=\\min\\left(|{phan_so(y_1)}|,|{phan_so(y_2)}|\\right)+{t}={phan_so(gt_min)}+{t}={phan_so(gt_min+t)}$."
			)

		kq4_T=f"* Giá trị nhỏ nhất của hàm số $y=|f(x)|+{t}$ trên đoạn $[{{{x_1};{x_2}}}]$ bằng ${{{phan_so(gt_min+t)}}}$".replace("+-","-")
		kq4_F=f" Giá trị nhỏ nhất của hàm số $y=|f(x)|+{t}$ trên đoạn $[{{{x_1};{x_2}}}]$ bằng ${{{phan_so(gt_min_false+t)}}}$".replace("+-","-")
		kq4=random.choice([kq4_T, kq4_F])
		
		HDG=HDG.replace("+-","-")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	loigiai=[]
	for pa in list_PA:
		if pa==kq1:
			loigiai.append(loigiai_1)
		if pa==kq2:
			loigiai.append(loigiai_2)
		if pa==kq3:
			loigiai.append(loigiai_3_latex)
		if pa==kq4:
			loigiai.append(loigiai_4)

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

#[D12_C1_B2_10]-M3. Tìm GTLN-GTNN của y=e^x.(ax^2+bx+c) trên đoạn
def prt_34_L12_C1_B2_10():
	x = sp.symbols('x')
	x_1=random.randint(-4,2)
	x_2=x_1+random.randint(3,5)
	b=-2-x_1-x_2
	c=x_1*x_2-b
	f=exp(x)*(x**2+b*x+c)
	g=diff(f,x)
	
	# Tạo đoạn [m,n]
	m= random.randint(x_1-4,x_1)
	n= random.randint(x_2,x_2+4)

	#Tính giá trị tại các điểm
	y_m=f.subs(x,m)
	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)
	y_n=f.subs(x,n)

	#Tạo giá trị ảo
	y_3=f.subs(x,m-1)
	y_4=f.subs(x,n+1)

	giatri_max=latex(max(y_m,y_1,y_2,y_n))
	giatri_min=latex(min(y_m,y_1,y_2,y_n))

	gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":		
		kq=f"${giatri_max}$"
		kq2=f"${giatri_min}$"
		kq3=f"${latex(y_3)}$"
		kq4=f"${latex(y_4)}$"
	else:		
		kq=f"${giatri_min}$"
		kq2=f"${giatri_max}$"
		kq3=f"${latex(y_3)}$"
		kq4=f"${latex(y_4)}$"	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$.\n"
	
	noi_dung_loigiai=f"$y'={latex(g)}$.\n\n"\
	f"$y'=0\\Rightarrow e^x({latex(x**2+(b+2)*x+b+c)})=0 \\Rightarrow x={x_1},x={x_2}$.\n\n"\
	f"$f({m})={latex(y_m)}, f({x_1})={latex(y_1)},f({x_2})={latex(y_2)}, f({n})={latex(y_n)}$.\n\n"\
	f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ bằng {kq}."

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

#[D12_C1_B2_11]-M3. Tìm GTLN-GTNN của y=e^(ax^2+bx+c) trên đoạn
def prt_34_L12_C1_B2_11():
	x = sp.symbols('x')
	a = random.choice([random.randint(-2, -1), random.randint(1, 2)])
	b=random.choice([2,4,-2,-4,-6,6])*a
	c=random.randint(-3,3)
	
	f=exp(a*x**2+b*x+c)
	g=diff(f,x)
	x_0=int(-b/(2*a))
	
	# Tạo đoạn [m,n]
	m= random.randint(int(x_0)-3,int(x_0))
	n= random.randint(int(x_0)+1,int(x_0)+3)

	#Tính giá trị tại các điểm
	y_m=f.subs(x,m)
	y_0=f.subs(x,x_0)
	y_n=f.subs(x,n)

	#Tạo giá trị ảo
	y_3=f.subs(x,m-1)
	y_4=f.subs(x,n+1)

	giatri_max=max(y_m,y_0,y_n)
	giatri_min=min(y_m,y_0,y_n)

	gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":		
		kq=giatri_max
		kq2=giatri_min
		kq3=y_3
		kq4=y_4
	else:		
		kq=giatri_min
		kq2=giatri_max
		kq3=y_3
		kq4=y_4	
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

	noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$.\n"	
	noi_dung_loigiai=f"$y'={latex(g)}$.\n\n"\
	f"$y'=0 \\Rightarrow x={x_0}$.\n\n"\
	f"$f({m})={latex(y_m)}, f({x_0})={latex(y_0)}, f({n})={latex(y_n)}$.\n\n"\
	f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ bằng ${latex(kq)}$."

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

#[D12_C1_B2_12]-M3. Tìm GTLN-GTNN của y=ln(ax^2+bx+c) trên đoạn
def prt_34_L12_C1_B2_12():
	x = sp.symbols('x')
	a = random.randint(1,4)
	b=random.choice([random.randint(-4, -1), random.randint(1, 4)])
	c=random.randint(2,6)
	if b==3 or b==-3: c=random.randint(3,6)
	if b==4 or b==-4: c=random.randint(4,7)
	x_0=-b/(2*a)
	while a*x_0**2+b*x_0+c<=0:
		a = random.randint(1,4)
		b=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		c=random.randint(2,6)
		if b==3 or b==-3: c=random.randint(3,6)
		if b==4 or b==-4: c=random.randint(4,7)
		x_0=-b/(2*a)

	
	f=log(a*x**2+b*x+c)
	g=diff(f,x)
	x_0=Rational(-b/(2*a)).limit_denominator(10000000000000)
	
	# Tạo đoạn [m,n]
	m= random.randint(int(x_0)-4,int(x_0)-1)
	n= random.randint(int(x_0)+2,int(x_0)+5)

	#Tính giá trị tại các điểm
	y_m=f.subs(x,m)
	y_0=f.subs(x,x_0)
	y_n=f.subs(x,n)

	#Tạo giá trị ảo
	y_3=f.subs(x,m-1)
	y_4=f.subs(x,n+1)

	giatri_max=max(y_m,y_0,y_n)
	giatri_min=min(y_m,y_0,y_n)

	gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":		
		kq=giatri_max
		kq2=giatri_min
		kq3=y_3
		kq4=y_4
	else:		
		kq=giatri_min
		kq2=giatri_max
		kq3=y_3
		kq4=y_4	
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${latex(kq)}$".replace("log","ln").replace(f"\\left(","").replace(f"\\right)","")
	pa_B= f"${latex(kq2)}$".replace("log","ln").replace(f"\\left(","").replace(f"\\right)","")
	pa_C= f"${latex(kq3)}$".replace("log","ln").replace(f"\\left(","").replace(f"\\right)","")
	pa_D= f"${latex(kq4)}$".replace("log","ln").replace(f"\\left(","").replace(f"\\right)","")
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$.\n".replace("log","ln")	
	noi_dung_loigiai=f"$y'={latex(g)}$.\n\n"\
	f"$y'=0 \\Rightarrow x={phan_so(x_0)}$.\n\n"\
	f"$f({m})={latex(y_m)}, f({phan_so(x_0)})={latex(y_0)}, f({n})={latex(y_n)}$.\n\n"\
	f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ bằng ${latex(kq)}$.".replace("log","ln")

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

#[D12_C1_B2_13]-M3. Tìm GTLN-GTNN của y=căn(x-a)+căn(b-x)
def prt_34_L12_C1_B2_13():
	x = sp.symbols('x')
	a = random.randint(-6,6)
	b= a + random.randint(1,6)
		
	f=sqrt(x-a)+sqrt(b-x)
	g=diff(f,x)
	x_0=Rational((a+b)/2).limit_denominator(10000000000000)

	#Tính giá trị tại các điểm
	y_a=f.subs(x,a)
	y_0=f.subs(x,x_0)
	y_b=f.subs(x,b)

	giatri_max=max(y_a,y_0,y_b)
	giatri_min=min(y_a,y_0,y_b)

	gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":		
		kq=giatri_max
		kq2=giatri_min
		kq3=giatri_max + random.randint(1,3)
		kq4=giatri_min - random.randint(1,3)
	else:		
		kq=giatri_min
		kq2=giatri_max
		kq3=giatri_max + random.randint(1,3)
		kq4=giatri_min - random.randint(1,3)
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

	noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Tập xác định: $D=[{a};{b}]$.\n\n"\
	f"$y'={latex(g)}=\\dfrac{{{latex(sqrt(b-x)-sqrt(x-a))} }} {{2.{latex(sqrt(x-a))}.{latex(sqrt(b-x))}}}$.\n\n"\
	f"$y'=0 \\Rightarrow x={phan_so(x_0)}$.\n\n"\
	f"$f({a})={latex(y_a)}, f({phan_so(x_0)})={latex(y_0)}, f({b})={latex(y_b)}$.\n\n"\
	f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{a};{b}]}}$ bằng ${latex(kq)}$."

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

#[D12_C1_B2_14]-M3. Tìm GTLN-GTNN của y=b.x.căn(a^2-x^2)
def prt_34_L12_C1_B2_14():
	x = sp.symbols('x')
	a = random.randint(1,10)
	b= random.choice([random.randint(-6, -1), random.randint(1, 6)])
		
	f=b*x*sqrt(a**2-x**2)
	g=diff(f,x)
	x_1, x_2=-a*sqrt(2)/2, a*sqrt(2)/2

	#Tính giá trị tại các điểm
	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)

	giatri_max=max(y_1,y_2)
	giatri_min=min(y_1,y_2)

	gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
	if gia_tri=="giá trị lớn nhất":		
		kq=giatri_max
		kq2=giatri_min
		kq3=giatri_max + random.randint(1,3)
		kq4=giatri_min - random.randint(1,3)
	else:		
		kq=giatri_min
		kq2=giatri_max
		kq3=giatri_max + random.randint(1,3)
		kq4=giatri_min - random.randint(1,3)
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

	noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"Tập xác định: $D=[{a};{b}]$.\n\n"\
	f"$y'={latex(g)}=\\dfrac{{{latex(b*(-2*x**2+a**2))}}} {{{latex(sqrt(a**2-x**2))}}}$.\n\n"\
	f"$y'=0 \\Rightarrow x_1={latex(x_1)}, x_1={latex(x_2)}$.\n\n"\
	f"$f({-a})=0, f({latex(x_1)})={latex(y_1)}, f({latex(x_2)})={latex(y_2)}, f({a})=0$.\n\n"\
	f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{a};{b}]}}$ bằng ${latex(kq)}$."

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

#[D12_C1_B2_15]-TL-M2. Cho hàm số. Tìm GTLN-GTNN trên đoạn
def prt_34_L12_C1_B2_15():
	x = sp.symbols('x')
	chon=random.randint(1,2)
	if chon==1:
		x_1=random.randint(-4,1)
		x_2=x_1+random.randint(3,5)
		
		k=random.choice([1,-1,3,-3])
		g=(x-x_1)*(x-x_2)
		f=k*integrate(g,x)+random.randint(-5,5)

		a=f.coeff(x,3)
		b=f.coeff(x,2)
		c=f.coeff(x,1)
		d=f.as_coefficients_dict()[1]

		# Tạo đoạn [m,n]
		m= random.randint(x_1-4,x_1-1)
		n= random.randint(x_2+1,x_2+4)

		#Tính giá trị tại các điểm
		y_m=f.subs(x,m)
		y_1=f.subs(x,x_1)
		y_2=f.subs(x,x_2)
		y_n=f.subs(x,n)

		giatri_max=max(y_m,y_1,y_2,y_n)
		giatri_min=min(y_m,y_1,y_2,y_n)

		gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
		if gia_tri=="giá trị lớn nhất":
			kq=f"${{{round(giatri_max,1)}}}$".replace(".",",")
		else:
			kq=f"${{{round(giatri_min,1)}}}$".replace(".",",")


		noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ (kết quả làm tròn đến hàng phần mười)."	
		noi_dung_loigiai=f"$y'={latex(expand(k*g))}$.\n\n"\
		f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"$f({m})={phan_so(y_m)}, f({x_1})={phan_so(y_1)},f({x_2})={phan_so(y_2)}, f({n})={phan_so(y_n)}$.\n\n"\
		f"Vậy {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ là {kq}."
	
	#Hàm phân thức
	if chon==2:
		a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b = random.choice([random.randint(-6, -1), random.randint(1, 6)])
		c = random.choice([random.randint(-7, -1), random.randint(1, 7)])
		d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		if a*d-b*c==0:
			d = d+1
		x_0=-d/c
		#Tạo đoạn [m;n]
		chon_ben=random.choice(["trái","phải"])
		if chon_ben=="trái":
			n = random.choice([int(x_0)-4,int(x_0)-1])
			m = n-random.randint(1,10)
		else:
			m = random.choice([int(x_0)+1,int(x_0)+4])
			n = m + random.randint(1,10)

		x=sp.symbols("x")
		f=(a*x+b)/(c*x+d)
		#Tính giá trị hai đầu mút
		y_m= f.subs(x,m)
		y_n=f.subs(x,n)
		gia_tri = random.choice(["giá trị lớn nhất", "giá trị nhỏ nhất"])
		noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ (kết quả làm tròn đến hàng phần mười)."
		
		if gia_tri=="giá trị lớn nhất":
		
			if a*d-b*c>0:
				kq = f"{round(y_n,1)}".replace(".",",")
				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số có giá trị lớn nhất bằng $f({n})={kq}$."
			else:

				kq = f"{round(y_m,1)}".replace(".",",")
				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số đạt giá trị lớn nhất bằng $f({m})={kq}$."

		else:

			if a*d-b*c>0:
				kq = f"{round(y_m,1)}".replace(".",",")
				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số đạt giá trị nhỏ nhất bằng $f({m})={kq}$."
			else:
				kq = f"{round(y_n,1)}".replace(".",",")
				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số đạt giá trị nhỏ nhất bằng $f({n})={kq}$."	

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_16]-TL-M3. Cho hàm số. Tìm GTLN-GTNN trên đoạn
def prt_34_L12_C1_B2_16():
	x = sp.symbols('x')
	chon=random.randint(1,3)
	#y=e^x.(ax^2+bx+c)
	if chon==1:
		x_1=random.randint(-4,2)
		x_2=x_1+random.randint(1,2)
		b=-2-x_1-x_2
		c=x_1*x_2-b
		f=exp(x)*(x**2+b*x+c)
		g=diff(f,x)
		
		# Tạo đoạn [m,n]
		m= random.randint(x_1-1,x_1)
		n= random.randint(x_2,x_2+1)

		#Tính giá trị tại các điểm
		y_m=f.subs(x,m)
		y_1=f.subs(x,x_1)
		y_2=f.subs(x,x_2)
		y_n=f.subs(x,n)

		giatri_max=max(y_m,y_1,y_2,y_n)
		giatri_min=min(y_m,y_1,y_2,y_n)

		gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
		if gia_tri=="giá trị lớn nhất":
			kq_latex=latex(giatri_max)	
			kq=f"{round(giatri_max,1)}".replace(".",",")
		else:
			kq_latex=latex(giatri_min)		
			kq=f"{round(giatri_min,1)}".replace(".",",")

		noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ (kết quả làm tròn đến hàng phần mười)."
		
		noi_dung_loigiai=f"$y'={latex(g)}$.\n\n"\
		f"$y'=0\\Rightarrow e^x({latex(x**2+(b+2)*x+b+c)})=0 \\Rightarrow x={x_1},x={x_2}$.\n\n"\
		f"$f({m})={latex(y_m)}, f({x_1})={latex(y_1)},f({x_2})={latex(y_2)}, f({n})={latex(y_n)}$.\n\n"\
		f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ bằng ${kq_latex}={kq}$."

	#y=e^(ax^2+bx+c)
	if chon==2:
		a = random.choice([random.randint(-2, -1), random.randint(1, 2)])
		b=random.choice([2,4,-2,-4])*a
		c=random.randint(-3,3)
		
		f=exp(a*x**2+b*x+c)
		g=diff(f,x)
		x_0=int(-b/(2*a))
		
		# Tạo đoạn [m,n]
		m= random.randint(int(x_0)-1,int(x_0))
		n= int(x_0)+1

		y_m=f.subs(x,m)
		y_0=f.subs(x,x_0)
		y_n=f.subs(x,n)

		giatri_max=max(y_m,y_0,y_n)
		giatri_min=min(y_m,y_0,y_n)

		gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
		if gia_tri=="giá trị lớn nhất":		
			kq=f"{round(giatri_max,1)}".replace(".",",")
			kq_latex=latex(giatri_max)
		else:		
			kq=f"{round(giatri_min,1)}".replace(".",",")
			kq_latex=latex(giatri_min).replace(".",",")

		noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$.\n"	
		noi_dung_loigiai=f"$y'={latex(g)}$.\n\n"\
		f"$y'=0 \\Rightarrow x={x_0}$.\n\n"\
		f"$f({m})={latex(y_m)}, f({x_0})={latex(y_0)}, f({n})={latex(y_n)}$.\n\n"\
		f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ bằng ${kq_latex}={kq}$."

	#y=ln(ax^2+bx+c)
	if chon==3:
		a = random.randint(1,4)
		b=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		c=random.randint(2,6)
		if b==3 or b==-3: c=random.randint(3,6)
		if b==4 or b==-4: c=random.randint(4,7)
		
		f=log(a*x**2+b*x+c)
		g=diff(f,x)
		x_0=Rational(-b/(2*a)).limit_denominator(10000000000000)
		
		# Tạo đoạn [m,n]
		m= random.randint(int(x_0)-3,int(x_0))
		n= random.randint(int(x_0)+1,int(x_0)+3)

		y_m=f.subs(x,m)
		y_0=f.subs(x,x_0)
		y_n=f.subs(x,n)

		giatri_max=max(y_m,y_0,y_n)
		giatri_min=min(y_m,y_0,y_n)

		gia_tri=random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"])
		if gia_tri=="giá trị lớn nhất":		
			kq_latex=latex(giatri_max)
			kq=f"{round(giatri_max,1)}".replace(".",",")
		else:		
			kq_latex=latex(giatri_min)
			kq=f"{round(giatri_min,1)}".replace(".",",")

		noi_dung = f"Tìm {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$.\n".replace("log","ln")	
		noi_dung_loigiai=f"$y'={latex(g)}$.\n\n"\
		f"$y'=0 \\Rightarrow x={phan_so(x_0)}$.\n\n"\
		f"$f({m})={latex(y_m)}, f({phan_so(x_0)})={latex(y_0)}, f({n})={latex(y_n)}$.\n\n"\
		f"Vậy {gia_tri} của hàm số $y={latex(f)}$ trên đoạn ${{[{m};{n}]}}$ bằng ${kq_latex}={kq}$.".replace("log","ln")

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_17]-TL-M3. Cho hàm số. Tìm GTLN-GTNN trên khoảng
def prt_34_L12_C1_B2_17():
	x = sp.symbols('x')
	chon=random.randint(1,3)

	#y=(ax+b)(cx+d)
	if chon==1:
		a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b = random.choice([random.randint(-6, -1), random.randint(1, 6)])
		c = random.choice([random.randint(-7, -1), random.randint(1, 7)])
		d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		if a*d-b*c==0:
			d = d+1
		x_0=-d/c
		#Tạo đoạn [m;n]
		chon_ben=random.choice(["trái","phải"])
		if chon_ben=="trái":
			n = random.choice([int(x_0)-4,int(x_0)-1])
			m = n-random.randint(1,10)
		else:
			m = random.choice([int(x_0)+1,int(x_0)+4])
			n = m + random.randint(1,10)
		x_1=m
		x_2=n

		x=sp.symbols("x")
		f=(a*x+b)/(c*x+d)
		#Tính giá trị hai đầu mút
		y_m= f.subs(x,m)
		y_n=f.subs(x,n)

		gia_tri = random.choice(["giá trị lớn nhất", "giá trị nhỏ nhất"])
		if gia_tri=="giá trị lớn nhất":			
			if a*d-b*c>0:
				noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{({m};{n}]}}$ (kết quả làm tròn đến hàng phần mười)."
				kq = f"{round(y_n,1)}".replace(".",",")
				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số đạt giá trị lớn nhất trên nửa khoảng ${{({m};{n}]}}$ bằng $f({n})={phan_so(y_n)}={kq}$."
			else:
				noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{[{m};{n})}}$ (kết quả làm tròn đến hàng phần mười)."
				kq = f"{round(y_m,1)}".replace(".",",")

				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số đạt giá trị lớn nhất trên nửa khoảng ${{[{m};{n})}}$ bằng $f({m})={phan_so(y_m)}={kq}$."

		else:
			if a*d-b*c>0:
				noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{[{m};{n})}}$ (kết quả làm tròn đến hàng phần mười)."
				kq = f"{round(y_m,1)}".replace(".",",")
				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số đồng biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số đạt giá trị nhỏ nhất trên nửa khoảng ${{[{m};{n})}}$ bằng $f({m})={phan_so(y_m)}={kq}$."
			else:
				noi_dung = f"Tìm {gia_tri} của hàm số $\\displaystyle y={latex(f)}$ trên nửa khoảng ${{({m};{n}]}}$ (kết quả làm tròn đến hàng phần mười)."
				kq = f"{round(y_n,1)}".replace(".",",")
				noi_dung_loigiai=f"$y'={latex((a*d-b*c)/(c*x+d)**2)}<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
				f"Hàm số nghịch biến trên khoảng $({m};{n})$.\n\n"\
				f"Hàm số đạt giá trị nhỏ nhất trên nửa khoảng ${{({m};{n}]}}$ bằng $f({n})={phan_so(y_n)}={kq}$."
		latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"

	#y=ax + b/x
	if chon==2:
		a = random.randint(1, 9)
		b = random.randint(1, 9)
		f=a*x+b/x
		x_1, x_2 = -sqrt(b/a), sqrt(b/a)
		y_1, y_2 = nsimplify(f.subs(x,x_1)), nsimplify(f.subs(x,x_2))
		
		code_hinh=code_bbt_phanthucbac2(a,0,b,1,0)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

		chon=random.randint(1,2)		
		if chon==1:		
			t=random.randint(0,int(sqrt(b/a)))
			chon=random.randint(1,2)
			if chon==1:
				kihieu=f"({t};+\\infty)"
				khoang=f"khoảng $({t};+\\infty)$"
			if chon==2:
				kihieu=f"[{t};+\\infty)"
				khoang= f"nửa khoảng $[{t};+\\infty)$"

			kq=f"{round(y_2,1)}".replace(".",",")

			noi_dung=f"Tìm giá trị nhỏ nhất của hàm số $y={latex(f)}$ cho trên {khoang} bằng (kết quả làm tròn đến hàng phần mười)."
			noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
			f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
			f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"{file_name}\n\n"\
			f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_2)}={kq}$.\n\n"

			
			noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
			f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
			f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
			f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_2)}={kq}$.\n\n"


		if chon==2:
			t=random.randint(-int(sqrt(b/a)),0)
			chon=random.randint(1,2)
			if chon==1:
				kihieu=f"(-\\infty;{t})"
				khoang=f"khoảng $(-\\infty;{t})$"
			if chon==2:
				kihieu=f"(-\\infty;{t}]"
				khoang= f"nửa khoảng $(-\\infty;{t})$"

			kq=f"{round(y_1,1)}".replace(".",",")

			noi_dung=f"Tìm giá trị lớn nhất của hàm số $y={latex(f)}$ trên {khoang} (kết quả làm tròn đến hàng phần mười)."
			noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
			f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
			f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"{file_name}\n\n"\
			f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left(-{latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_1)}={kq}$.\n\n"

			noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{0\\}}$.\n\n"\
			f"$y'={latex(a-b**2/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$.\n\n"\
			f"$y'=0 \\Leftrightarrow {latex(a*x**2-b)}=0 \\Leftrightarrow x_1=-{latex(nsimplify(sqrt(b/a)))}, x_2={latex(nsimplify(sqrt(b/a)))}$.\n\n"\
			f"Bảng biến thiên:\n\n"\
			f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
			f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left(-{latex(nsimplify(sqrt(b/a)))} \\right)={latex(y_1)}={kq}$.\n\n"

		latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
	f"\\end{{ex}}\n"

	#y=(ax^2+bx+c)/(dx+e)
	if chon==3:
		x_1=random.choice([2*i for i in range(-5,5)])
		i=random.randint(1,3)
		x_2=x_1+2*i

		b, c, =x_1+x_2, x_1*x_2 
		x_0=int(b/2)

		#Tạo hàm số g là đạo hàm của f
		g=(x**2-b*x+c)/((x-x_0)**2)
		g1=(x**2-b*x+x_0**2)/((x-x_0)**2)
		c2=x_0**2-c

		#Tìm hàm f là nguyên hàm của g
		f=integrate(g,x)
		f1=integrate(g1,x)	
		a=random.choice([1,2])
		f_ok=a*(f1*x-f1*x_0+c2)/(x-x_0)

		y_1=f_ok.subs(x,x_1)
		y_2=f_ok.subs(x,x_2)
		if a>0:		
			
			code_hinh =f"\\begin{{tikzpicture}}[scale=1]\n\
		    \\tkzTabInit[nocadre=false,lgt=1.5,espcl=3]\n\
		    {{$x$ /1,$y'$ /1,$y$ /2}}\n\
		    {{$-\\infty$,${x_1}$, ${x_0}$, ${x_2}$, $+\\infty$}}\n\
		\\tkzTabLine{{ ,+,z,-,d,-,z,+, }}\n\
		\\tkzTabVar{{-/$-\\infty$,+/${phan_so(y_1)}$,-D+/$-\\infty$/$+\\infty$,-/${phan_so(y_2)}$,+/$+\\infty$}}\n\
		    \\end{{tikzpicture}}\n"
			code = my_module.moi_truong_anh_latex(code_hinh)
			file_name=my_module.pdftoimage_timename(code)

			chon=random.randint(1,2)
			if chon==1:		
				t=random.choice([x_0,phan_so((x_0+x_2)/2)])
				chon=random.randint(1,2)
				if chon==1:
					kihieu=f"({t};+\\infty)"
					khoang=f"khoảng $({t};+\\infty)$"
				if chon==2:
					kihieu=f"[{t};+\\infty)"
					khoang= f"nửa khoảng $[{t};+\\infty)$"

				kq=f"{round(y_2,1)}".replace(".",",")
				noi_dung=f"Tìm giá trị nhỏ nhất của hàm số $y={latex(f_ok)}$ cho trên {khoang} (kết quả làm tròn đến hàng phần mười)."

				noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
				f"$y'={latex(a*g)}$.\n\n"\
				f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
				f"Bảng biến thiên:\n\n"\
				f"{file_name}\n"\
				f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_2} \\right)={latex(y_2)}={kq}$."

				noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
				f"$y'={latex(a*g)}$.\n\n"\
				f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
				f"Bảng biến thiên:\n\n"\
				f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
				f"$\\mathop{{\\min}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_2} \\right)={latex(y_2)}={kq}$."

			if chon==2:
				t=random.choice([x_0, phan_so((x_0+x_1)/2)])
				chon=random.randint(1,2)
				if chon==1:
					kihieu=f"(-\\infty;{t})"
					khoang=f"khoảng $(-\\infty;{t})$"
				if chon==2:
					kihieu=f"(-\\infty;{t}]"
					khoang= f"nửa khoảng $(-\\infty;{t})$"

				noi_dung=f"Tìm giá trị lớn nhất của hàm số $y={latex(f_ok)}$ trên {khoang} (kết quả làm tròn đến hàng phần mười)."

				kq=f"{round(y_1,1)}".replace(".",",")
				noi_dung_loigiai=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
				f"$y'={latex(a*g)}$.\n\n"\
				f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
				f"Bảng biến thiên:\n\n"\
				f"{file_name}\n"\
				f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_1} \\right)={latex(y_1)}$.\n\n"

				noi_dung_loigiai_latex=f"Tập xác định: $D=\\mathbb{{R}}\\backslash \\{{{x_0}\\}}$.\n\n"\
				f"$y'={latex(a*g)}$.\n\n"\
				f"$y'=0 \\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
				f"Bảng biến thiên:\n\n"\
				f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
				f"$\\mathop{{\\max}}\\limits_{{{kihieu}}} {{y}}=y\\left({x_1} \\right)={latex(y_1)}$.\n\n"
			latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
	f"\\end{{ex}}\n"

	debai_word= f"{noi_dung}\n"
	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	dap_an=kq
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_18]-TL-M3. Tìm m để y=(ax+b)/(cx+d) đạt GTLN(GTNN) bằng y_0.
def prt_34_L12_C1_B2_18():
	x,m=sp.symbols("x,m")
	a = random.choice([i for i in range(-5, 6) if i!=0])
	b = random.choice([i for i in range(-5, 6) if i!=0])
	x_0=random.choice([i for i in range(-5, 6) if i!=0])
	while a*(-x_0)-b==0 or x_0==0:
		a = random.choice([i for i in range(-5, 6) if i!=0])
		b = random.choice([i for i in range(-5, 6) if i!=0])
		x_0=random.choice([i for i in range(-5, 6) if i!=0])
		
	f=(a*x+b)/(x-x_0)
	f_m=(m*x+b)/(x-x_0)

	t_1=random.randint(x_0+1,x_0+4)
	t_2=t_1+random.randint(2,5)	

	ten_giatri=random.choice(["lớn nhất", "nhỏ nhất"])
	ten_giatri="lớn nhất"

	if ten_giatri=="lớn nhất":
		if a*(-x_0)-b>0:
			gia_tri=f.subs(x,t_2)
		else:
			gia_tri=f.subs(x,t_1)

		noi_dung =(f"Cho hàm số $y=\\dfrac{{{latex(m*x+b)}}}{{{latex(x-x_0)}}}$ với ${{m}}$ là tham số."
		f" Tìm tham số ${{m}}$ để giá trị lớn nhất của hàm số trên đoạn ${{[{t_1};{t_2}]}}$ bằng ${phan_so(gia_tri)}$ (kết quả làm tròn đến hàng phần mười).")

		f_1m=f_m.subs(x,t_1)
		pt= Eq(f_1m, gia_tri)
		nghiem= solve(pt , m)
		nghiem_1=nghiem[0]
	
		f_2m=f_m.subs(x,t_2)
		pt= Eq(f_2m, gia_tri)
		nghiem= solve(pt , m)
		nghiem_2=nghiem[0]

		noi_dung_loigiai=(			

		f"Nếu $\\mathop{{\\max f(x)}}\\limits_{{[{t_1};{t_2}]}}=f({t_1})=\\dfrac{{{t_1}m+{b}}}{{{t_1-x_0}}}$.\n\n"
		f"$\\mathop{{\\max f(x)}}\\limits_{{[{t_1};{t_2}]}}={phan_so(gia_tri)}\\Rightarrow \\dfrac{{{t_1}m+{b}}}{{{t_1-x_0}}} ={phan_so(gia_tri)} \\Rightarrow m={phan_so(nghiem_1)}$.\n\n"

		
		f"Nếu $\\mathop{{\\max f(x)}}\\limits_{{[{t_1};{t_2}]}}=f({t_2})=\\dfrac{{{t_2}m+{b}}}{{{t_2-x_0}}}$.\n\n"
		f"$\\mathop{{\\max f(x)}}\\limits_{{[{t_1};{t_2}]}}={phan_so(gia_tri)}\\Rightarrow \\dfrac{{{t_2}m+{b}}}{{{t_2-x_0}}} ={phan_so(gia_tri)} \\Rightarrow m={phan_so(nghiem_2)}$.\n\n"
		
		)
		if a*(-x_0)-b>0:
			noi_dung_loigiai+=f" Thử lại thấy $m={nghiem_2}$ thỏa mãn.\n\n"
		else:
			noi_dung_loigiai+=f" Thử lại thấy $m={nghiem_1}$ thỏa mãn.\n\n"


		

		dap_an=a
		

		
	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_19]-TL-M3. Cho hàm $y=|f(x)|+am$. Tìm m để hàm số đạt giá trị lớn nhất bằng y_0.
def prt_34_L12_C1_B2_19():
	x= sp.symbols('x')
	x_1=random.randint(-4,1)
	x_2=x_1+random.randint(3,5)
	
	k=random.choice([1,-1,3,-3])

	g=(x-x_1)*(x-x_2)
	f=k*integrate(g,x)+random.randint(-5,5)

	a=f.coeff(x,3)
	b=f.coeff(x,2)
	c=f.coeff(x,1)
	d=f.as_coefficients_dict()[1]

	# Tạo đoạn [m,n]
	m= random.randint(x_1-4,x_1-1)
	n= random.randint(x_2+1,x_2+4)

	#Tính giá trị tại các điểm
	y_m=f.subs(x,m)
	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)
	y_n=f.subs(x,n)

	g_max=max(y_m,y_1,y_2,y_n)
	g_min=min(y_m,y_1,y_2,y_n)
	t_max=max(abs(g_max),abs(g_min))

	max_value=random.randint(-5,10)

	e= random.choice([random.randint(-6, -2), random.randint(2, 6)])

	pt= Eq(t_max+e*x, max_value)	
	nghiem= solve(pt , x)
	t=nghiem[0]
	t_round=str(round(t,1)).replace(".",",")

	noi_dung = f"Cho hàm số $y=\\Bigg|{latex(f)}\\Bigg|+{e}m$ với ${{m}}$ là tham số."\
	f" Tìm ${{m}}$ sao cho giá trị lớn nhất của hàm số đã cho trên đoạn ${{[{m};{n}]}}$ bằng ${{{max_value}}}$ (kết quả làm tròn đến hàng phần mười).".replace("+-","-")

	noi_dung_loigiai=f"Đặt $g(x)={latex(f)}$.\n\n"\
	f"$g'(x)={latex(expand(k*g))}$.\n\n"\
	f"$g'(x)=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
	f"$g({m})={phan_so(y_m)}, g({x_1})={phan_so(y_1)},g({x_2})={phan_so(y_2)}, g({n})={phan_so(y_n)}$.\n\n"\
	f"Suy ra $\\mathop{{\\max}}\\limits_{{[{m};{n}]}}g(x)={phan_so(g_max)},\\mathop{{\\min}}\\limits_{{[{m};{n}]}}g(x)={phan_so(g_min)}$.\n\n"\
	f"Ta có: $\\mathop{{\\max}}\\limits_{{[{m};{n}]}}\\left(\\Bigg|{latex(f)}\\Bigg|+{e}m\\right)=\\mathop{{\\max}}\\limits_{{[{m};{n}]}}\\left(\\Bigg|{latex(f)}\\Bigg|\\right)+{e}m={phan_so(t_max)}+{e}m$.\n\n"\
	f"Theo giả thiết: ${phan_so(t_max)}+{e}m={max_value}\\Rightarrow m={phan_so(t)}$.\n\n"\
	f"Kết quả làm tròn: $m={t_round}$.".replace("+-","-")

		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{t_round}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=t_round
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_20]-TL-M3. Tìm m để y=(ax+b)/(cx+d) có min y + max y=T.
def prt_34_L12_C1_B2_20():
	x,m=sp.symbols("x,m")

	a = random.choice([i for i in range(-5, 6) if i!=0])
	b = random.choice([i for i in range(-5, 5) if i!=0])
	c = random.choice([i for i in range(-5, 5) if i!=0])
	d = random.choice([i for i in range(-6, 6) if i!=0])

	f=(a*x+b*m)/(c*x+d)
	x_0=-d/c

	chon=random.randint(1,2)
	if chon==1:
		t_1=random.randint(int(x_0)+1,int(x_0)+3)
		t_2=t_1+ random.randint(1,5)
	if chon==2:
		t_2=random.randint(int(x_0)-3,int(x_0)-1)
		t_1=t_2- random.randint(1,5)	
	
	f_1=f.subs(x,t_1)
	f_2=f.subs(x,t_2)
	T=random.randint(-5,10)

	noi_dung = f"Cho hàm số $y={latex(f)}$ với ${{m}}$ là tham số. Tìm tham số ${{m}}$ để $\\mathop{{\\min}}\\limits_{{[{t_1};{t_2}]}} {{y}}+ \\mathop{{\\max}}\\limits_{{[{t_1};{t_2}]}} {{y}}={T}$ (kết quả làm tròn đến hàng phần mười)."

	# Giải phương trình
	pt= Eq(f_1+f_2, T)	
	nghiem= solve(pt , m)
	t=nghiem[0]
	t_round=str(round(t,1)).replace(".",",")

	noi_dung_loigiai=f"$y'=\\dfrac{{{latex(a*d-b*m*c)}}}{{{latex((c*x+d)**2)}}},\\forall x\\ne {phan_so(-d/c)}$.\n\n"\
	f"Với $m\\ne {phan_so(a*d/(b*c))}$ thì:\n\n"\
	f"$\\mathop{{\\min}}\\limits_{{[{t_1};{t_2}]}} {{y}}+ \\mathop{{\\max}}\\limits_{{[{t_1};{t_2}]}} {{y}}={T}$"\
	f"$\\Leftrightarrow y({t_1})+y({t_2})={T} \\Leftrightarrow {latex(simplify(f_1))}+{latex(simplify(f_2))}={T} \\Leftrightarrow m={phan_so(t)}$.\n\n"\
	f"Kết quả làm tròn: $m={t_round}$."

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{${t_round}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=t_round
	return debai_word,loigiai_word,latex_tuluan,dap_an

# # Tạo thời gian
# 	t=random.choice([2,3])
# 	u1=random.choice([2,3])
# 	u1,t=2,2
# 	x=[u1+(i-1)*t for i in range(1,8)]

# 	# Tạo nhiệt độ
# 	y_0=random.randint(20,36)
# 	y_1=y_0-random.randint(2,5)
# 	y_2=y_1+random.randint(4,6)
# 	y_3=y_1+random.randint(1,3)
# 	y_4=y_3+random.randint(1,3)
# 	y_5=y_3-random.randint(1,2)
# 	y_6=y_5-random.randint(1,2)
# 	y=[y_0,y_1,y_2,y_3,y_4,y_5,y_6]

# 	code_hinh=rf""" \begin{{tikzpicture}}[>=stealth,x=0.25cm,y=0.15cm]
# 		\draw[->] (-2,0)--(0,0) node[below left]{{$O$}}--(28,0) node[below right]{{ $x$ (giờ) }};
# 		\draw[->] (0,-4)--(0,40) node[left]{{$t$ ($^\circ C$)}};
# 		\foreach \x/\g in {{ {x[1]}/-90, {x[2]}/-90, {x[3]}/-90,{x[4]}/-90, {x[5]}/-90, {x[6]}/-90 }}
# 		\draw[thin] (\x,2pt)--(\x,-2pt) + (\g:3mm) node {{$\x$}};
# 		%Vẽ các điểm trên trục Oy
# 		\foreach \y/\g in {{ {y[0]}/180}}
# 		\draw[thin] (2pt,\y)--(-2pt,\y) + (\g:3mm) node {{$\y$}};
# 		\path
# 		(0,{y[0]}) coordinate ({y[0]})
# 		({x[1]},{y[1]}) coordinate ({y[1]})
# 		({x[2]},{y[2]}) coordinate ({y[2]})
# 		({x[3]},{y[3]}) coordinate ({y[3]})
# 		({x[4]},{y[4]}) coordinate ({y[4]})
# 		({x[5]},{y[5]}) coordinate ({y[5]})
# 		({x[6]},{y[6]}) coordinate ({y[6]});
# 		\draw [dashed] ({x[1]},0)--({x[1]},{y[1]}) (8,0)--({x[2]},{y[2]}) ({x[3]},0)--({x[3]},{y[3]}) ({x[4]},0)--({x[4]},{y[4]}) ({x[5]},0)--({x[5]},{y[5]}) ({x[6]},0)--({x[6]},{y[6]}); 
# 		\draw[smooth, thick, red]
# 		({y[0]}) .. controls +(-10:1) and +(-180:1) .. ({y[1]})
# 		({y[1]}) .. controls +(0:1) and +(-180:1) .. ({y[2]})
# 		({y[2]}) .. controls +(0:1) and +(160:1) .. ({y[3]})
# 		({y[3]}) .. controls +(0:1) and +(-180:2) .. ({y[4]})
# 		({y[4]}) .. controls +(0:1.5) and +(130:1.5) .. ({y[5]})
# 		({y[5]}) .. controls +(-60:1.5) and +(-180:2) .. ({y[6]});
# 		\foreach \x in {{ {y[1]},{y[2]},{y[3]},{y[4]},{y[5]},{y[6]}}}
# 		\fill (\x) +(90:3mm) node {{$\x$}};
# 	\end{{tikzpicture}}"""

#[D12_C1_B2_21]-TL-M3. Tìm vận tốc lớn nhất, nhỏ nhất của chuyển động
def prt_34_L12_C1_B2_21():
	t=sp.symbols("t")
	t_0=random.randint(2,12)
	v_dh=4*t*(t**2-t_0)

	a=random.randint(200,300)
	v=integrate(v_dh,t)+a

	#Thời gian từ [0, t_1]
	t_1=int(sqrt(t_0))+random.randint(2,5)
	v_0=v.subs(t,sqrt(t_0))
	v_1=v.subs(t,t_1)
	
	chon=random.randint(1,2)
	if chon==1:
		kq=max(a,v_0,v_1)
		noi_dung=f"Một chất điểm chuyển động có vận tốc tức thời $v(t)$ phụ thuộc vào thời gian ${{t}}$ theo hàm số $v(t)={latex(v)}$ (m/s)."\
		f" Trong khoảng thời gian từ $t=0$ (s) đến $t={t_1}$ (s) chất điểm đạt vận tốc lớn nhất nhất bằng?"
		noi_dung_loigiai=(f"$v'(t)={latex(v_dh)}$.\n\n"
		f"$v'(t)=0\\Leftrightarrow t=0, t=\\pm {latex(sqrt(t_0))}$.\n\n"
		f'$v(0)={a},v({latex(sqrt(t_0))})={latex(v_0)}, v({t_1})={latex(v_1)}$.\n\n'
		f'Vận tốc lớn nhất bằng ${{{kq}}}$ (m/s).'
		)
	
	if chon==2:
		kq=min(a,v_0,v_1)
		noi_dung=f"Một chất điểm chuyển động có vận tốc tức thời $v(t)$ phụ thuộc vào thời gian ${{t}}$ theo hàm số $v(t)={latex(v)}$ (m/s)."\
		f" Trong khoảng thời gian từ $t=0$ (s) đến $t={t_1}$ (s) chất điểm đạt vận tốc nhỏ nhất nhất bằng?"
		noi_dung_loigiai=(f"$v'(t)={latex(v_dh)}$.\n\n"
		f"$v'(t)=0\\Leftrightarrow t=0, t=\\pm {latex(sqrt(t_0))}$.\n\n"
		f'$v(0)={a},v({latex(sqrt(t_0))})={latex(v_0)}, v({t_1})={latex(v_1)}$.\n\n'
		f'Vận tốc nhỏ nhất bằng ${{{kq}}}$ (m/s).'
		)		
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_22]-TL-M3. Cắt hình chữ nhật từ nửa đường tròn. Tìm diện tích lớn nhất của hình chữ nhật.
def prt_34_L12_C1_B2_22():
	code_hinh=r"""
	\begin{tikzpicture}[line join = round, line cap = round,>=stealth,font=\footnotesize,scale=1] 
			\def\R{2}
			\coordinate[label = below:$O$] (O) at (0,0); 
			\coordinate (A) at (-\R,0); 
			\coordinate (B) at ($(A)!2!(O)$);
			\coordinate[label = above right:$C$] (C) at (50:\R); 
			\coordinate[label = above left:$D$] (D) at (130:\R);
			\coordinate[label = below:$A$] (AA) at ($(A)!(D)!(B)$); 
			\coordinate[label = below:$B$] (BB) at ($(A)!(C)!(B)$); 
			\draw (A) arc(180:0:\R)--cycle;
			\draw[fill=cyan!20] (BB)--(C)--(D)--(AA)--cycle;
			\foreach \x in {AA,O,BB} \fill[black] (\x) circle (1.5pt); 
		\end{tikzpicture}
	"""

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	R=random.randint(2,10)
	x=sp.symbols("x")
	f=2*x*sqrt(R**2-x**2)
	f_dh=diff(f,x)
	f_max=f.subs(x, R/sqrt(2))

	noi_dung =(f"Từ một tấm tôn có hình dạng là nửa hình tròn bán kính $R={R}$, người ta muốn cắt ra một hình chữ nhật (như hình vẽ)."
	f" Diện tích lớn nhất có thể của tấm tôn hình chữ nhật là")

	noi_dung_loigiai=(f"Gọi chiều dài $OA=x\\Rightarrow AB=2x$ ($0<x<{R}$).\n\n"
		f"$\\Rightarrow AD=\\sqrt{{OD^2-OA^2}}=\\sqrt{{{R**2}-x^2}}$.\n\n"
		f"Diện tích hình chữ nhật là $S=AB.AD=2x\\sqrt{{{R**2}-x^2}}$.\n\n"
		f"Xét $f(x)=2x\\sqrt{{{R**2}-x^2}}$ trên $(0;{R})$, ta có\n\n"
		f"$f'(x)={latex(f_dh)}$.\n\n"
		f"$f'(x)=0 \\Rightarrow x={latex(R/sqrt(2))}$.\n\n"
		f"$f(x)$ đạt giá trị lớn nhất tại $x={latex(R/sqrt(2))}$.\n\n"
		f"Diện tích lớn nhất là $f\\left({latex(R/sqrt(2))}\\right)={f_max}$."
		)
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[4]{{{f_max}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=f_max
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_23]-TL-M3. Tìm chi phí thấp nhất để xây cái bể hình hộp chữ nhật
def prt_34_L12_C1_B2_23():
	x=sp.symbols("x")
	
	r=random.choice([i*10 for i in range(1,5)])
	d=random.choice([i*10 for i in range(6,9)])	
	f=x*(r-2*x)*(d-2*x)
	f_dh=diff(f,"x")

	eq=Eq(f_dh,0)
	solution = solve(eq, x)
	x_1=solution[0]
	x_2=solution[1]	

	a=random.randint(1,int(x_1))
	b=int(x_1)+random.randint(1,3)
	V_a=f.subs(x,a)
	V_b=f.subs(x,b)
	V_1=f"{round(f.subs(x,x_1))}"
	t=f.subs(x,x_1)
	
	while t<-9.9 or t>9999:
		r=random.choice([i*10 for i in range(1,5)])
		d=random.choice([i*10 for i in range(6,9)])	
		f=x*(r-2*x)*(d-2*x)
		f_dh=diff(f,"x")

		eq=Eq(f_dh,0)
		solution = solve(eq, x)
		x_1=solution[0]
		x_2=solution[1]	

		a=random.randint(1,int(x_1))
		b=int(x_1)+random.randint(1,3)
		V_a=f.subs(x,a)
		V_b=f.subs(x,b)
		V_1=f"{round(f.subs(x,x_1))}"
		t=f.subs(x,x_1)

	code_hinh=r"""
		\begin{tikzpicture}[line join=round, line cap=round,scale=0.9]
			\coordinate (A) at (0,3);
			\coordinate (B) at (5,3);
			\coordinate (D) at (0,0);
			\coordinate (C) at ($(B)+(D)-(A)$);			
			\draw(A)--(B)--(C)--(D)--cycle;
			\draw (0,0) rectangle (1,1) (A) rectangle (1,2) (B) rectangle (4,2) (4,1) rectangle (C);
			\draw[dashed] (1,1) rectangle (4,2);
			%	\foreach \i/\g in {A/90,B/90,C/-90,D/-90}{\draw[fill=black](\i) circle (1pt) ($(\i)+(\g:3mm)$) node[scale=1]{$\i$};}
			\draw (0,.5) node [left] {$x$};
			\draw (.5,0) node [below] {$x$};
			\draw (0,2.5) node [left] {$x$};
			\draw (0.5,3) node [above] {$x$};
			%%%%%%%%%
			\draw (4.5,0) node [below] {$x$};
			\draw (5,0.5) node [right] {$x$};
			\draw (5,2.5) node [right] {$x$};
			\draw (4.5,3) node [above] {$x$};
			%%%%%%%%
			\draw[<->] (-1,0)--(-1,3) node[above,midway,sloped]"""
	code_hinh+=f"{{${r}$cm}};\n"
	code_hinh+=r"""\draw[<->] (0,-1)--(5,-1) node[above,midway]"""
	code_hinh+=f"{{${d}$cm}};\n"
	code_hinh+=r"""\path (current bounding box.south) node[below, black]{a)}; %dưới
		\end{tikzpicture}
		\hspace*{1cm}
		\begin{tikzpicture}[scale=0.9, font=\footnotesize, line join=round, line cap=round, >=stealth]
			\def\bc{3} % cạnh BC
			\def\ba{1} % cạnh BA
			\def\h{1.5} % đường cao
			\def\gocnghieng{90} % góc nghiêng
			\def\gocB{35} % góc B của đáy
			\coordinate (B) at (0,0);
			\coordinate (A) at (\gocB:\ba);
			\coordinate (C) at (\bc,0);
			\coordinate (D) at ($(C)-(B)+(A)$);
			\coordinate (A') at ($(A)+(\gocnghieng:\h)$);
			\coordinate (B') at ($(B)-(A)+(A')$);
			\coordinate (C') at ($(C)-(A)+(A')$);
			\coordinate (D') at ($(D)-(A)+(A')$);
			\draw (B')--(B)--(C)--(D)--(D')--(A')--(B')--(C')--(D') (C)--(C');
			\draw[dashed] (A')--(A)--(D) (A)--(B);
			\path (current bounding box.south) node[below, black]{b)}; %dưới
		\end{tikzpicture}
	"""

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)	
	
	chon=random.randint(1,2)
	if chon==1:
		kq=f"{x_1:.1f}".replace(".",",")
		noi_dung = (f"Từ một tấm bìa hình chữ nhật có chiều rộng ${{{r}}}$cm và chiều dài ${{{d}}}$ cm như hình a,"
			f" người ta cắt ở bốn góc bốn hình vuông có cạnh ${{x}}$ với ${a} \\leq x \\leq {b}$ và gấp lại để tạo thành chiếc hộp có dạng hình hộp chữ nhật không nắp như hình b."
		f" Tìm $x$ để thể tích chiếc hộp là lớn nhất (kết quả làm tròn đến hàng phần mười).")

		noi_dung_loigiai=(f"Thể tích chiếc hộp là $V(x)=x({r}-2 x)({d}-2 x)={latex(expand(f))}$ với ${a} \\leq x \\leq {b}$.\n\n"
			f"Ta có: $V'={latex(expand(f_dh))}$.\n\n"
			f"$V'=0 \\Rightarrow x={latex(x_1)},x={latex(x_2)}$.\n\n"
			f"$V({a})={latex(V_a)},V({latex(x_1)})\\approx {V_1}, V({b})={latex(V_b)}$.\n\n"
			f"Thể tích hộp lớn nhất khi $x\\approx {kq}$ (cm)."
			)
	
	if chon==2:
		kq=f"{round(f.subs(x,x_1))}"
		noi_dung = (f"Từ một tấm bìa hình chữ nhật có chiều rộng ${{{r}}}$cm và chiều dài ${{{d}}}$ cm như hình a,"
			f" người ta cắt ở bốn góc bốn hình vuông có cạnh ${{x}}$ với ${a} \\leq x \\leq {b}$ và gấp lại để tạo thành chiếc hộp có dạng hình hộp chữ nhật không nắp như hình b."
		f" Tìm thể tích lớn nhất của chiếc hộp có thể tạo ra (kết quả làm tròn đến hàng đơn vị).")

		noi_dung_loigiai=(f"Thể tích chiếc hộp là $V(x)=x({r}-2 x)({d}-2 x)={latex(expand(f))}$ với ${a} \\leq x \\leq {b}$.\n\n"
			f"Ta có: $V'={latex(expand(f_dh))}$.\n\n"
			f"$V'=0 \\Rightarrow x={latex(x_1)},x={latex(x_2)}$.\n\n"
			f"$V({a})={latex(V_a)},V({latex(x_1)})\\approx {kq}, V({b})={latex(V_b)}$.\n\n"
			f"Thể tích hộp lớn nhất là $V\\approx {kq} (cm^3)$ ."
			)

		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"

	dap_an=kq
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B2_24]-M2. Cho đồ thị f(x).Tìm GTLN-GTNN
def prt_34_L12_C1_B2_24():
	chon=random.randint(1,2)
	
	p=random.randint(1,3)
	q=random.choice([i for i in range(-3, 3) if i!=0])
	
	if chon==1:
		a=random.randint(-5,-3)
		b=a+random.randint(4,8)
		if b<0: b=b+random.randint(2,3)
		x_1=random.choice([random.randint(a+2,b-2),int((a+b)/2)])
		#Tạo max=y_1, min=y_b
		y_a=random.randint(-3,3)
		y_1=y_a+random.randint(1,3)
		y_b=y_a-random.randint(1,3)

		gt_M=max(y_a,y_1,y_b)
		gt_m=min(y_a,y_1,y_b)

		kq=p*gt_M+q*gt_m
		kq2=p*(gt_M+1)+q*gt_m
		kq3=p*gt_M+q*(gt_m+1)
		kq4=p*gt_M-q*gt_m

	if chon==2:
		a=random.randint(-5,-3)
		b=a+random.randint(4,8)
		if b<0: b=b+random.randint(2,3)
		x_1=random.choice([random.randint(a+2,b-2),int((a+b)/2)])
		#Tạo max=y_1, min=y_b
		y_a=random.randint(-2,4)
		y_1=y_a-random.randint(1,3)
		y_b=y_1+random.randint(1,3)

		gt_M=max(y_a,y_1,y_b)
		gt_m=min(y_a,y_1,y_b)

		kq=p*gt_M+q*gt_m
		kq2=p*(gt_M+1)+q*gt_m
		kq3=p*gt_M+q*(gt_m+1)
		kq4=p*gt_M-q*gt_m	
	
	x_min,x_max=a-1, b+1
	y_min,y_max=gt_m-1, gt_M+1

	if y_max<=0: y_max=2
	if y_min>=0: y_min=-2

	numbers = [f'{i}' for i in range(y_min, y_max) if (i!=0 and i%2==0 )]    
	chuoi_so_y = ','.join(numbers)

	numbers = [f'{i}' for i in range(x_min, x_max) if (i!=0 and i%2==0)]    
	chuoi_so_x = ','.join(numbers)

	code_hinh=rf"""
	\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick]
\tikzset{{every node/.style={{scale=0.9}}}}
\draw[gray!20]({x_min},{y_min}) grid({x_max},{y_max});
\draw[->] ({x_min},0)--({x_max},0) node[below left] {{$x$}};
\draw[->] (0,{y_min})--(0,{y_max}) node[below left] {{$y$}};
\foreach \x in {{{chuoi_so_x}}}
    \draw[thin] (\x,1pt)--(\x,-1pt) node [below] {{\footnotesize $\x$}};
\foreach \y in {{{chuoi_so_y}}}
    \draw[thin] (1pt,\y)--(-1pt,\y) node [left] {{\footnotesize $\y$}};
\draw (0,0) node [below left] {{$O$}};
\begin{{scope}}
\clip ({x_min},{y_min}) rectangle ({x_max},{y_max});
\draw[blue] plot[smooth,tension=0.2] coordinates{{({a},{y_a}) ({x_1},{y_1}) ({b},{y_b})}};
\end{{scope}}
\end{{tikzpicture}}
	"""
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	M,m=sp.symbols("M m")
	noi_dung=(f"Cho hàm số $y=f(x)$ có đồ thị trên đoạn ${{[{a};{b}}}]$ như hình vẽ."
	f" Gọi ${{M}}$ và ${{m}}$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số đã cho trên đoạn ${{[{a};{b}}}]$."
	f" Tính ${latex(p*M+q*m)}$.")

	
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=(f"Dựa vào đồ thị ta thấy $M={gt_M}, m={gt_m}$.\n\n"
		f"Do đó: ${latex(p*M+q*m)}={kq}$."
		)

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


	

#BÀI 3 - ĐƯỜNG TIỆM CẬN

#[D12_C1_B3_01]. Đọc đường tiệm cận của đồ thị hàm số y=(ax+b)/(cx+d)
def prt_34_L12_C1_B3_01():
	a = random.choice([i for i in range(-7, 7) if i!=0])
	b = random.choice([i for i in range(-5, 6) if i!=0])
	c = random.choice([i for i in range(-5, 6) if i!=0])
	d = random.choice([i for i in range(-5, 6) if i!=0])	

	if a*d-b*c==0:
		d = d+1
	x=sp.symbols("x")

	f=(a*x+b)/(c*x+d)

	duong_tiem_can=random.choice(["đường tiệm cận đứng", "đường tiệm cận ngang"])

	if duong_tiem_can == "đường tiệm cận đứng":
		kq=-d/c
		kq2=d/c
		kq3=-d/c
		kq4=a/c

		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]


		kq=f"$\\displaystyle x={phan_so(kq)}$"
		kq2=f"$\\displaystyle x={phan_so(kq2)}$"
		kq3=f"$\\displaystyle y={phan_so(kq3)}$"
		kq4=f"$\\displaystyle y={phan_so(kq4)}$"

	else: 
		kq=f"$\\displaystyle y={phan_so(a/c)}$"
		kq2=f"$\\displaystyle x={phan_so(a/c)}$"
		kq3=f"$\\displaystyle y={phan_so((a+random.randint(1,3))/c)}$"
		kq4=f"$\\displaystyle x={phan_so(-a/c)}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

	noi_dung = f"Tìm {duong_tiem_can} của đồ thị hàm số $\\displaystyle y={latex(f)}$."
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f"{duong_tiem_can} của đồ thị hàm số $\\displaystyle y={latex(f)}$ là {kq}."

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


#[D12_C1_B3_02]. Đọc đường tiệm cận từ bảng biến thiên.
def prt_34_L12_C1_B3_02():
	chon=random.randint(1,2)
	
	duong_tiem_can=random.choice(["đường tiệm cận đứng", "đường tiệm cận ngang", "đường tiệm cận đứng và tiệm cận ngang"])
	if chon==1:
		x_1=random.randint(-6,0)
		#Điểm phân chia và không xác định
		x_2 = x_1 + random.randint(1,5)
		x_3=x_2 + random.randint(1,5)
		
		#Thiết lập thông tin cột trái
		y_1=random.choice(["-\\infty", random.randint(-10,10)])
		if y_1 == "-\\infty":
			y_2 = random.randint(-5,5)
		else:
			y_2 = y_1 + random.randint(1,10)		

		y_3=random.choice(["-\\infty", y_2 - random.randint(1,10)])

		#Thiết lập thông tin cột phải
		y_4=random.choice(["+\\infty", random.randint(-10,10)])
		if y_4 == "+\\infty":
			y_5 = random.randint(-5,5)
		else:		
			y_5 = y_4 - random.randint(1,10)

		y_6=random.choice(["+\\infty", y_5 + random.randint(1,10)])
		#Tìm số tiệm cận ngang
		so_tiemcan_ngang = 0	
		if y_1 != "-\\infty":
			so_tiemcan_ngang += 1

		if y_6 != "+\\infty":
			so_tiemcan_ngang += 1

		#Tìm số tiệm cận đứng
		so_tiemcan_dung = 0	
		if y_3=="-\\infty" or y_4== "+\\infty":
			so_tiemcan_dung = 1

		code_hinh=my_module.code_bbt_tim_tiemcan(x_1,x_2,x_3,y_1,y_2,y_3,y_4,y_5,y_6)
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)
		
		if duong_tiem_can == "đường tiệm cận đứng":
			kq=f"${{{so_tiemcan_dung}}}$"
			kq2=f"${{{so_tiemcan_dung+1}}}$"
			kq3=f"${{{so_tiemcan_dung+2}}}$"
			kq4=f"${{{so_tiemcan_dung+3}}}$"
		elif duong_tiem_can == "đường tiệm cận ngang":
			kq=f"${{{so_tiemcan_ngang}}}$"
			kq2=f"${{{so_tiemcan_ngang+1}}}$"
			kq3=f"${{{so_tiemcan_ngang+2}}}$"
			kq4=f"${{{so_tiemcan_ngang+3}}}$"
		else:
			kq=f"${{{so_tiemcan_ngang+so_tiemcan_dung}}}$"
			kq2=f"${{{so_tiemcan_ngang+so_tiemcan_dung+1}}}$"
			kq3=f"${{{so_tiemcan_ngang+so_tiemcan_dung+2}}}$"
			kq4=f"${{{so_tiemcan_ngang+so_tiemcan_dung+3}}}$"
		noi_dung_loigiai=f"Số {duong_tiem_can} của đồ thị hàm số $y=f(x)$ là {kq}.\n"

	if chon==2:
		x_0=random.randint(-8,8)
		a=random.randint(-8,8)
		c=random.randint(-5,10)
		b=c+random.randint(1,4)
		if a==c: a=a+1
		code_hinh=f"\\begin{{tikzpicture}}\n\
	\\tkzTabInit[nocadre=false,lgt=1,espcl=2.5]\n\
	{{$x$ /0.7,$y'$ /0.7,$y$ /1.7}}\n\
	{{$-\\infty$,${x_0}$,$+\\infty$}}\n\
	\\tkzTabLine{{,-, d ,-,}}\n\
	\\tkzTabVar{{+/ ${a}$ / , -D+/ $-\\infty$ / ${b}$ , -/ ${c}$ /}}\n\
	\\end{{tikzpicture}}\n"
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)
		if duong_tiem_can == "đường tiệm cận đứng":
			kq=f"${{1}}$"
			kq2=f"${{2}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"Ta có: $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}}y=-\\infty$ nên"\
			f" đồ thị hàm số có một đường tiệm cận đứng là $x={x_0}$.\n\n"\
			f"Số {duong_tiem_can} của đồ thị hàm số $y=f(x)$ là {kq}.\n"

		if duong_tiem_can == "đường tiệm cận ngang":
			kq=f"${{2}}$"
			kq2=f"${{1}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"Ta có: $\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}}y={a}$ "\
			f" và $\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}}y={b}$"\
			f" nên đồ thị hàm số có hai đường tiệm cận ngang là $y={a}$ và $y={b}$.\n\n"
			f"Số {duong_tiem_can} của đồ thị hàm số $y=f(x)$ là {kq}.\n"

		if duong_tiem_can == "đường tiệm cận đứng và tiệm cận ngang":
			kq=f"${{3}}$"
			kq2=f"${{1}}$"
			kq3=f"${{0}}$"
			kq4=f"${{2}}$"
			noi_dung_loigiai=f"Ta có: $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}}y=-\\infty$ nên"\
			f" đồ thị hàm số có một đường tiệm cận đứng là $x={x_0}$.\n\n"\
			f"Ta có: $\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}}y={a}$ "\
			f" và $\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}}y={b}$"\
			f" nên đồ thị hàm số có hai đường tiệm cận ngang là $y={a}$ và $y={b}$.\n\n"\
			f"Số {duong_tiem_can} của đồ thị hàm số $y=f(x)$ là {kq}.\n"

	noi_dung = f"Cho hàm số $y=f(x)$ có bảng biến thiên như hình vẽ sau."
			
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)	
	dap_an=my_module.tra_ve_dap_an(list_PA)		

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"\
	f"Tìm số {duong_tiem_can} của đồ thị hàm số $y=f(x)$.\n"

	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"Tìm số {duong_tiem_can} của đồ thị hàm số $y=f(x)$.\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"Tìm số {duong_tiem_can} của đồ thị hàm số $y=f(x)$.\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B3_03]-M1. Đọc đường tiệm cận đứng của đồ thị hàm số y=(ax^2+bx+c)/(dx+e)
def prt_34_L12_C1_B3_03():
	
	x=sp.symbols("x")
	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b=random.randint(-8,8)
	m = random.choice([random.randint(-7, -1), random.randint(1, 7)])

	d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	e=random.choice([random.randint(-10, -1), random.randint(1, 10)])

	#f =ax+b +m/(cx+d)
	f=latex(expand((a*x+b)*(d*x+e)+m))
	noi_dung = f"Tìm đường tiệm cận đứng của đồ thị hàm số $y=\\dfrac{{{f}}}{{{latex(d*x+e)}}}$."

	kq=-e/d
	kq2=e/d
	kq3=d/e
	kq4=a/e

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*$x={phan_so(kq)}$"
	pa_B= f"$x={phan_so(kq2)}$"
	pa_C= f"$x={phan_so(kq3)}$"
	pa_D= f"$x={phan_so(kq4)}$"
	noi_dung_loigiai=f"Ta có $y=\\dfrac{{{f}}}{{{latex(d*x+e)}}}={latex(a*x+b+m/(d*x+e))}$.\n\n"\
	f"Đường tiệm cận đứng của đồ thị hàm số là $x={phan_so(kq)}$."
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

#[D12_C1_B3_04]-M2. Đọc đường tiệm cận xiên của đồ thị hàm số y=(ax^2+bx+c)/(dx+e)
def prt_34_L12_C1_B3_04():
	
	x=sp.symbols("x")
	a = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b=random.randint(-8,8)
	m = random.choice([random.randint(-7, -1), random.randint(1, 7)])

	d = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	e=random.choice([random.randint(-7, -1), random.randint(1, 7)])

	#f =ax+b +m/(cx+d)
	f=latex(expand((a*x+b)*(d*x+e)+m))
	noi_dung = f"Tìm đường tiệm cận xiên của đồ thị hàm số $y=\\dfrac{{{f}}}{{{latex(d*x+e)}}}$."

	kq=latex(a*x+b)
	kq2=latex(d*x+e)
	kq3=latex((a+2)*x+b+random.randint(1,3))
	kq4=latex(a*x+b-random.randint(1,4))

	pa_A= f"*$y={kq}$"
	pa_B= f"$y={kq2}$"
	pa_C= f"$y={kq3}$"
	pa_D= f"$y={kq4}$"
	noi_dung_loigiai=f"Ta có $y=\\dfrac{{{f}}}{{{latex(d*x+e)}}}={latex(a*x+b+m/(d*x+e))}$.\n\n"\
	f"$\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} \\left[y -({latex(a*x+b)})\\right]=\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {latex(m/(d*x+e))}=0$.\n\n"\
	f"Đường tiệm cận xiên của đồ thị hàm số là $y={latex(a*x+b)}$."
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

#[D12_C1_B3_05]-M2. Tìm số đường tiệm cận đứng của các hàm số khác
def prt_34_L12_C1_B3_05():
	chon=random.randint(1,4)	
	x=sp.symbols("x")
	if chon==1:	
		a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
		b = random.randint(-8,8)
		c = random.choice([random.randint(-7, -1), random.randint(1, 7)])

		d = random.randint(1, 6)
		e = random.randint(1, 8)

		#f =(ax^2+bx+c)/(dx^2+e)
		f=(a*x**2+b*x+c)/(d*x**2+e)
		noi_dung = f"Số đường tiệm cận đứng của đồ thị hàm số $y={latex(f)}$ là"

		kq=0
		kq2=2
		kq3=random.choice([1,4])
		kq4=3
		noi_dung_loigiai=f"Hàm số xác định với mọi $x\\in \\mathbb{{R}}$.\n\n"\
	f"Đồ thị hàm số không có đường tiệm cận đứng."

	if chon==2:	
		a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
		b = random.randint(-8,8)
		c = random.choice([random.randint(-7, -1), random.randint(1, 7)])
		chon=random.randint(1,2)
		if chon==1:
			d = random.randint(1, 4)
			e = random.randint(-4, -1)
		if chon==2:
			d = random.randint(-4, -1)
			e = random.randint(1, 4)
		g=a*x**2+b*x+c
		x_0, x_1=sqrt(-e/d), -sqrt(-e/d)

		if g.subs(x,x_0)==0 or g.subs(x,x_0)==1: c=c+1
		f=(a*x**2+b*x+c)/(d*x**2+e)

		x_0=nsimplify(sqrt(-e/d))
		t=f.subs(x,x_0+0.1)
		if t>0: lim_x0=f"+\\infty"
		if t<0: lim_x0=f"-\\infty"

		x_1=nsimplify(-sqrt(-e/d))
		t=f.subs(x,x_1+0.1)
		if t>0: lim_x1=f"+\\infty"
		if t<0: lim_x1=f"-\\infty"		
		
		noi_dung = f"Số đường tiệm cận đứng của đồ thị hàm số $y={latex(f)}$ là"

		kq=2
		kq2=3
		kq3=random.choice([0,4])
		kq4=1
		noi_dung_loigiai=f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_0)}^+  }} {{{latex(f)}}} ={lim_x0}$.\n\n"\
	f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_1)}^+  }} {{{latex(f)}}} ={lim_x1}$.\n\n"\
	f"Đồ thị hàm số có 2 đường tiệm cận đứng $x={latex(x_0)}$ và $x={latex(x_1)}$."
	
	if chon==3:	
		a = random.randint(1, 5)
		b = random.randint(1,4)		
		
		x_0=random.randint(-4,4)
		x_1=x_0+random.randint(1,5)

		g=a*(x-x_0)**2+b
		
		f=sqrt((g))/((x-x_0)*(x-x_1))		
		t=f.subs(x,x_0+0.1)
		if t>0: lim_x0=f"+\\infty"
		if t<0: lim_x0=f"-\\infty"
		
		t=f.subs(x,x_1+0.1)
		if t>0: lim_x1=f"+\\infty"
		if t<0: lim_x1=f"-\\infty"
		ham_so=f"\\dfrac{{\\sqrt{{{latex(expand(g))}}}}} {{{latex(expand((x-x_0)*(x-x_1)))}}}"
	
		noi_dung = f"Số đường tiệm cận đứng của đồ thị hàm số $y={ham_so}$ là"

		kq=2
		kq2=4
		kq3=random.choice([0,3])
		kq4=1
		noi_dung_loigiai=f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_0)}^+  }} {{{ham_so}}} ={lim_x0}$.\n\n"\
	f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_1)}^+  }} {{{ham_so}}} ={lim_x1}$.\n\n"\
	f"Đồ thị hàm số có 2 đường tiệm cận đứng $x={latex(x_0)}$ và $x={latex(x_1)}$."
	
	if chon==4:	
		a = random.choice([random.randint(-2, -1), random.randint(1, 2)])
		x_1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x_2 = x_1 + random.randint(1, 4)
		
		m =random.choice([random.randint(-3, -1), random.randint(1, 3)])
		f=m*(x-x_1)/(a*(x-x_1)*(x-x_2))
		ham=f"\\dfrac{{{latex(m*x-m*x_1)}}} {{{latex(expand(a*(x-x_1)*(x-x_2)))}}}"
		ham_LG=f"\\dfrac{{{latex(m*(x-x_1))}}} {{{latex((a*(x-x_1)*(x-x_2)))}}}"

		lim_x1=m/(a*(x_1-x_2))

		g=m/(a*(x-x_2))
		t=g.subs(x,x_2+0.1)
		if t>0: lim_x2=f"+\\infty"
		if t<0: lim_x2=f"-\\infty"

	
		noi_dung = f"Số đường tiệm cận đứng của đồ thị hàm số $y={ham}$ là"
		kq=1
		kq2=4
		kq3=random.choice([0,3])
		kq4=2
		noi_dung_loigiai=f"Ta có: $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_1)}^+ }} {{ {ham_LG} }} ={phan_so(lim_x1)}$.\n\n"\
	f"$\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_2)}^+ }} {{{ham_LG}}} ={lim_x2}$.\n\n"\
	f"Đồ thị hàm số có 1 đường tiệm cận đứng là $x={x_2}$."

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

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

#[D12_C1_B3_06]-M2. Tìm số đường tiệm cận của các hàm số khác
def prt_34_L12_C1_B3_06():
	chon=random.randint(1,3)
	
	x=sp.symbols("x")
	if chon==1:	
		a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
		b = random.randint(-8,8)
		c = random.choice([random.randint(-7, -1), random.randint(1, 7)])

		d = random.randint(1, 6)
		e = random.randint(1, 8)

		#f =(ax^2+bx+c)/(dx^2+e)
		f=(a*x**2+b*x+c)/(d*x**2+e)
		noi_dung = f"Số đường tiệm cận của đồ thị hàm số $y={latex(f)}$ là"

		kq=1
		kq2=2
		kq3=random.choice([0,4])
		kq4=3
		noi_dung_loigiai=f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {{{latex(f)}}} ={phan_so(a/d)}$.\n\n"\
	f"Đường tiệm cận ngang của đồ thị hàm số là $y={phan_so(a/d)}$.\n\n"\
	f"Đồ thị hàm số không có đường tiệm cận đứng và đường tiệm cận xiên."

	if chon==2:	
		a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
		b = random.randint(-8,8)
		c = random.choice([random.randint(-7, -1), random.randint(1, 7)])
		chon=random.randint(1,2)
		if chon==1:
			d = random.randint(1, 4)
			e = random.randint(-4, -1)
		if chon==2:
			d = random.randint(-4, -1)
			e = random.randint(1, 4)
		g=a*x**2+b*x+c
		x_0, x_1=sqrt(-e/d), -sqrt(-e/d)

		if g.subs(x,x_0)==0 or g.subs(x,x_0)==1: c=c+1
		f=(a*x**2+b*x+c)/(d*x**2+e)

		x_0=nsimplify(sqrt(-e/d))
		t=f.subs(x,x_0+0.1)
		if t>0: lim_x0=f"+\\infty"
		if t<0: lim_x0=f"-\\infty"

		x_1=nsimplify(-sqrt(-e/d))
		t=f.subs(x,x_1+0.1)
		if t>0: lim_x1=f"+\\infty"
		if t<0: lim_x1=f"-\\infty"		
		
		noi_dung = f"Số đường tiệm cận của đồ thị hàm số $y={latex(f)}$ là"

		kq=3
		kq2=2
		kq3=random.choice([0,4])
		kq4=1
		noi_dung_loigiai=f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {{{latex(f)}}} ={phan_so(a/d)}$.\n\n"\
	f"Đường tiệm cận ngang của đồ thị hàm số là $y={phan_so(a/d)}$.\n\n"\
	f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_0)}^+  }} {{{latex(f)}}} ={lim_x0}$.\n\n"\
	f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_1)}^+  }} {{{latex(f)}}} ={lim_x1}$.\n\n"\
	f"Đồ thị hàm số không có đường tiệm cận xiên."

	if chon==3:	
		a = random.randint(1, 5)
		b = random.randint(-4,4)
		c = random.randint(1, 7)
		chon=random.randint(1,2)
		if chon==1:
			d = random.randint(1, 4)
			e = random.randint(-4, -1)
		if chon==2:
			d = random.randint(-4, -1)
			e = random.randint(1, 4)
		g=a*x**2+b*x+c
		
		x_0, x_1=sqrt(-e/d), -sqrt(-e/d)
		y_0, y_1 = nsimplify(sqrt(a)/d), nsimplify(-sqrt(a)/d)

		if g.subs(x,x_0)==0 or g.subs(x,x_0)==1: c=c+1
		f=sqrt((a*x**2+b*x+c))/(d*x**2+e)

		x_0=nsimplify(sqrt(-e/d))
		t=f.subs(x,x_0+0.1)
		if t>0: lim_x0=f"+\\infty"
		if t<0: lim_x0=f"-\\infty"

		x_1=nsimplify(-sqrt(-e/d))
		t=f.subs(x,x_1+0.1)
		if t>0: lim_x1=f"+\\infty"
		if t<0: lim_x1=f"-\\infty"
	
		noi_dung = f"Số đường tiệm cận của đồ thị hàm số $y={latex(f)}$ là"

		kq=3
		kq2=2
		kq3=random.choice([0,4])
		kq4=1
		noi_dung_loigiai=f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {{{latex(f)}}} =0$.\n\n"\
		f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to  - \\infty }} {{{latex(f)}}} =0$.\n\n"\
	f"Đồ thị hàm số tiệm cận ngang là $y=0$.\n\n"\
	f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_0)}^+  }} {{{latex(f)}}} ={lim_x0}$.\n\n"\
	f"Ta có $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_1)}^+  }} {{{latex(f)}}} ={lim_x1}$.\n\n"\
	f"Đồ thị hàm số có các tiệm cận đứng là $x={latex(x_0)}$ và $x={latex(x_1)}$ .\n\n"\
	f"Đồ thị hàm số không có đường tiệm cận xiên."

	if chon==4:	
		a = random.choice([random.randint(-2, -1), random.randint(1, 2)])
		x_1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
		x_2 = x_1 + random.randint(1, 4)
		
		m =random.choice([random.randint(-3, -1), random.randint(1, 3)])
		f=m*(x-x_1)/(a*(x-x_1)*(x-x_2))
		ham=f"\\dfrac{{{latex(m*x-m*x_1)}}} {{{latex(expand(a*(x-x_1)*(x-x_2)))}}}"
		ham_LG=f"\\dfrac{{{latex(m*(x-x_1))}}} {{{latex((a*(x-x_1)*(x-x_2)))}}}"

		lim_x1=m/(a*(x_1-x_2))

		g=m/(a*(x-x_2))
		t=g.subs(x,x_2+0.1)
		if t>0: lim_x2=f"+\\infty"
		if t<0: lim_x2=f"-\\infty"
	
		noi_dung = f"Số đường tiệm cận của đồ thị hàm số $y={ham}$ là"
		kq=2
		kq2=4
		kq3=random.choice([0,3])
		kq4=1
		noi_dung_loigiai=f"$\\mathop{{\\lim}}\\limits_{{x \\to +\\infty }} {{ {ham} }}=0$.\n\n"\
		f"Đồ thị hàm số có 1 đường tiệm cận ngang là $y=0$."\
		f"Ta có: $\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_1)}^+ }} {{ {ham_LG} }} ={phan_so(lim_x1)}$.\n\n"\
	f"$\\mathop{{\\lim}}\\limits_{{x \\to {latex(x_2)}^+ }} {{{ham_LG}}} ={lim_x2}$.\n\n"\
	f"Đồ thị hàm số có 1 đường tiệm cận đứng là $x={x_2}$."
	f"Đồ thị hàm số không có đường tiệm cận xiên."

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

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

#[D12_C1_B3_07]-M2. Tìm đường tiệm cận từ giới hạn
def prt_34_L12_C1_B3_07():
	chon=random.randint(1,3)
	
	x=sp.symbols("x")
	if chon==1:
		a = random.randint(-8,4)
		b = a + random.randint(1,6)
		lim_vc_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to -\\infty }} {{f(x)}}={a}$"
		lim_vc_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to +\\infty }} {{f(x)}}={b}$"
		
		noi_dung = f"Cho hàm số $y=f(x)$ xác định trên $\\mathbb{{R}}$ có {lim_vc_trai} và {lim_vc_phai}."\
		f" Khẳng định nào sau đây đúng?"

		kq=f"Đồ thị hàm số có hai tiệm cận ngang là $y={a}$ và $y={b}$"
		kq2=f"Đồ thị hàm số có hai tiệm cận đứng là $x={a}$ và $x={b}$"
		kq3=f"Đồ thị hàm số không có tiệm cận ngang"
		kq4=f"Đồ thị hàm số có {random.randint(1,2)} tiệm cận đứng"
		noi_dung_loigiai=f"Từ {lim_vc_trai} suy ra đồ thị hàm số có tiệm cận ngang là $y={a}$.\n\n"\
		f"Từ {lim_vc_phai} suy ra đồ thị hàm số có tiệm cận ngang là $y={b}$.\n\n"\
		f"Vậy đồ thị hàm số có 2 đường tiệm cận ngang là $y={a}$ và $y={b}$."

	if chon==2:
		x_1 = random.randint(-8,4)
		x_2 = x_1 + random.randint(1,6)

		lim_x1_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to {x_1}^- }} {{f(x)}}={random.choice([f"+\\infty",f"-\\infty"])}$"
		lim_x1_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to {x_1}^+ }} {{f(x)}}={random.choice([f"+\\infty",f"-\\infty"])}$"
		lim_x1=random.choice([lim_x1_trai, lim_x1_phai])

		lim_x2_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to {x_2}^- }} {{f(x)}}={random.choice([f"+\\infty",f"-\\infty"])}$"
		lim_x2_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to {x_2}^+ }} {{f(x)}}={random.choice([f"+\\infty",f"-\\infty"])}$"
		lim_x2=random.choice([lim_x2_trai, lim_x2_phai])
		
		noi_dung = f"Cho hàm số $y=f(x)$ có {lim_x1} và {lim_x2}."\
		f" Khẳng định nào sau đây đúng?"

		kq=f"Đồ thị hàm số có hai tiệm cận đứng là $x={x_1}$ và $x={x_2}$"
		kq2=f"Đồ thị hàm số có hai tiệm cận ngang là $y={x_1}$ và $y={x_2}$"
		kq3=f"Đồ thị hàm số không có tiệm cận ngang"
		kq4=f"Đồ thị hàm số không có tiệm cận đứng"
		noi_dung_loigiai=f"Từ {lim_x1} suy ra đồ thị hàm số có tiệm cận đứng là $x={x_1}$.\n\n"\
		f"Từ {lim_x2} suy ra đồ thị hàm số có tiệm cận đứng là $x={x_2}$.\n\n"\
		f"Vậy đồ thị hàm số có 2 đường tiệm cận đứng là $x={x_1}$ và $x={x_2}$."

	if chon==3:
		x_1 = random.randint(-8,8)
		lim_x1_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to {x_1}^- }} {{f(x)}}={random.choice([f"+\\infty",f"-\\infty"])}$"
		lim_x1_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to {x_1}^+ }} {{f(x)}}={random.choice([f"+\\infty",f"-\\infty"])}$"
		lim_x1=random.choice([lim_x1_trai, lim_x1_phai])

		a = random.randint(-8,8)
		lim_vc_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to -\\infty }} {{f(x)}}={a}$"
		lim_vc_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to +\\infty }} {{f(x)}}={a}$"
		lim_vc=random.choice([lim_vc_trai, lim_vc_phai])
		
		noi_dung = (f"Cho hàm số $y=f(x)$ có {lim_x1} và {lim_vc}."
		f" Khẳng định nào sau đây đúng?")

		kq=f"Đồ thị hàm số có ít nhất một tiệm cận đứng và ít nhất một tiệm cận ngang"
		kq2=f"Đồ thị hàm số có hai tiệm cận đứng"
		kq3=f"Đồ thị hàm số có hai tiệm cận ngang"
		kq4=random.choice([f"Đồ thị hàm số không có tiệm cận đứng",f"Đồ thị hàm số không có tiệm cận ngang"])
		noi_dung_loigiai=f"Từ {lim_x1} suy ra đồ thị hàm số có tiệm cận đứng là $x={x_1}$.\n\n"\
		f"Từ {lim_vc} suy ra đồ thị hàm số có tiệm cận ngang là $y={a}$.\n\n"\
		f"Vậy đồ thị hàm số có có một tiệm cận đứng và một tiệm cận ngang."
	
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B3_08]-TF-M2. Cho hàm số y=(ax+b)/(cx+d). Xét Đ-S: lim, tiệm cận đứng, tiệm cận ngang	
def prt_34_L12_C1_B3_08():
	x=sp.symbols("x")
	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b = random.randint(-8,8)
	c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a*d-b*c==0: b=b+1
	f=(a*x+b)/(c*x+d)
	x_0=-d/c
	if f.subs(x,x_0+0.1)>0:
		t=f"+\\infty"
	else:
		t=f"-\\infty"
	y_0=a/c
	noi_dung=f"Cho hàm $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau"

	kq1_T=f"*Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(x_0)}$"
	kq1_F=f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(-x_0)}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}}y={t}$ nên đồ thị hàm số có tiệm cận đứng là $x={phan_so(x_0)}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Tiệm cận ngang của đồ thị hàm số là đường thẳng $y={phan_so(y_0)}$"
	kq2_F=f"Tiệm cận ngang của đồ thị hàm số là đường thẳng $y={phan_so(-y_0)}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{y}}={phan_so(y_0)}$ nên đồ thị hàm số có tiệm cận ngang là $y={phan_so(y_0)}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if f.subs(x,x_0-0.1)>0:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
	else:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"

	if f.subs(x,x_0+0.1)>0:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=+\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=-\\infty$"
	else:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=-\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=+\\infty$"

	lim_x0=random.choice([lim_x0_trai, lim_x0_phai])
	lim_x0_false=random.choice([lim_x0_trai_false, lim_x0_phai_false])

	kq3_T=f"*{lim_x0}" 
	kq3_F=f"{lim_x0_false} "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Ta có: {lim_x0_trai}, {lim_x0_phai}"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	lim_vc_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{y}}={phan_so(a/c)}$"
	lim_vc_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{y}}={phan_so(-a/c)}$"
	lim_vc_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{y}}={phan_so(a/c)}$"
	lim_vc_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{y}}={phan_so(-a/c)}$"

	lim_vc=random.choice([lim_vc_trai, lim_vc_phai])
	lim_vc_false=random.choice([lim_vc_trai_false, lim_vc_phai_false])
	kq4_T=f"*{lim_vc}"
	kq4_F=f"{lim_vc_false}" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Ta có: {lim_vc_trai}, {lim_vc_phai}."
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	

	#Trộn các phương án
	list_PA =[kq3, kq4, kq1, kq2]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B3_09]-TF-M2. Cho y=(ax^2+bx+c)/(dx+e). Xét Đ-S: lim, tiệm cận đứng, tiệm cận xiên	
def prt_34_L12_C1_B3_09():
	x=sp.symbols("x")
	a = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b=random.randint(-8,8)
	m = random.choice([random.randint(-7, -1), random.randint(1, 7)])

	d = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	e=random.choice([random.randint(-7, -1), random.randint(1, 7)])

	#f =ax+b +m/(cx+d)
	f=((a*x+b)*(d*x+e)+m)/(d*x+e)
	g=latex(expand((a*x+b)*(d*x+e)+m))
	noi_dung = f"Cho hàm số $y=\\dfrac{{{g}}}{{{latex(d*x+e)}}}$. Xét tính đúng-sai của các khẳng định sau"
	x_0=-e/d
	if f.subs(x,x_0+0.1)>0:
		t=f"+\\infty"
	else:
		t=f"-\\infty"


	kq1_T=f"*Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(x_0)}$"
	kq1_F=f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(-x_0)}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}}y={t}$ nên đồ thị hàm số có tiệm cận đứng là $x={phan_so(x_0)}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Tiệm cận xiên của đồ thị hàm số là đường thẳng $y={latex(a*x+b)}$"
	kq2_F=f"Tiệm cận xiên của đồ thị hàm số là đường thẳng $y={latex(-a*x+b)}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Ta có $y=\\dfrac{{{g}}}{{{latex(d*x+e)}}}={latex(a*x+b+m/(d*x+e))}$.\n\n"\
	f"$\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} \\left[y -({latex(a*x+b)})\\right]=\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {latex(m/(d*x+e))}=0$.\n\n"\
	f"Đường tiệm cận xiên của đồ thị hàm số là $y={latex(a*x+b)}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if f.subs(x,x_0-0.1)>0:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
	else:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"

	if f.subs(x,x_0+0.1)>0:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=+\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=-\\infty$"
	else:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=-\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=+\\infty$"

	lim_x0=random.choice([lim_x0_trai, lim_x0_phai])
	lim_x0_false=random.choice([lim_x0_trai_false, lim_x0_phai_false])

	kq3_T=f"*{lim_x0}" 
	kq3_F=f"{lim_x0_false} "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Ta có: {lim_x0_trai}, {lim_x0_phai}"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	lim_vc_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{\\left[y-({latex(a*x+b)})\\right]}}=0$"
	lim_vc_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{\\left[y+({latex(a*x+b)})\\right]}}=0$"
	lim_vc_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{\\left[y-({latex(a*x+b)})\\right]}}=0$"
	lim_vc_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{\\left[y+({latex(a*x+b)})\\right]}}=0$"

	lim_vc=random.choice([lim_vc_trai, lim_vc_phai])
	lim_vc_false=random.choice([lim_vc_trai_false, lim_vc_phai_false])
	kq4_T=f"*{lim_vc}"
	kq4_F=f"{lim_vc_false}" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} \\left[y-({latex(a*x+b)})\\right]=\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {latex(m/(d*x+e))}=0$, "\
	f"$\\mathop{{\\lim}}\\limits_{{x \\to  - \\infty }} \\left[y-({latex(a*x+b)})\\right]=\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {latex(m/(d*x+e))}=0$.\n\n"
	
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B3_10]-TL-M3. Tìm m để y=(ax+b)/(cx+d) có tiệm cận
def prt_34_L12_C1_B3_10():
	x, m=sp.symbols("x m")
	a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	b = random.randint(-6,6)
	c = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	d = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	f = (a*x+b)/(c*x+d*m)
	while b*c/(a*d)<-9.9 or b*c/(a*d)>9999:
		a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
		b = random.randint(-6,6)
		c = random.choice([random.randint(-5, -1), random.randint(1, 5)])
		d = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	kq=f"{round(b*c/(a*d),1)}".replace(".",",")
	
	noi_dung=f"Biết các giá trị của tham số $m$ để đồ thị hàm số $y={latex(f)}$ có tiệm cận đứng là $m\\ne a$. \n\n"\
	f" Tính giá trị của ${{a}}$ (làm tròn đến hàng phần mười)."
	noi_dung_loigiai=f"Đồ thị hàm số đã cho có tiệm cận đứng khi"\
	f" ${show_tich(a,d)}m-{show_tich(b,c)}\\ne 0 \\Leftrightarrow m \\ne {phan_so(b*c/(a*d))} \\approx {kq}$."

	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B3_11]-TF-M3. Cho BBT của y=f(x). Xét Đ-S: Tìm TCĐ, Tìm TCN, Số TCD+TCN, Số TCN(TCD) của y= m/(f(x)+n)
def prt_34_L12_C1_B3_11():
	x_1=random.randint(-6,2)
	x_2=x_1+random.randint(1,5)

	y_3=random.randint(-10,10)
	y_2=y_3+random.randint(2,3)
	y_4=y_3+random.randint(4,5)
	y_1=y_3+random.randint(4,6)

	while y_1==0 or y_4==0 or y_4==y_1:
		y_2=y_3+random.randint(2,3)
		y_4=y_3+random.randint(4,5)
		y_1=y_3+random.randint(4,6)			

	code_hinh=f"\\begin{{tikzpicture}}\n\
		\\tkzTabInit[nocadre=false,lgt=1,espcl=2.5]\n\
		{{$x$ /0.7,$y'$ /0.7,$y$ /2}}\n\
		{{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n\
		\\tkzTabLine{{,-,d,-,0,+,}}\n\
		\\tkzTabVar{{+/ ${y_1}$ ,-D+/ $-\\infty$ / ${y_2}$,-/ ${y_3}$, +/ ${y_4}$}}\n\
		\\end{{tikzpicture}}"
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	
	noi_dung = f"Cho hàm số $y=f(x)$ có bảng biến thiên như hình vẽ. Xét tính đúng-sai của các khẳng định sau."	
	
	kq1_T=f"*Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $x={x_1}$" 
	kq1_F=f"Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $x={x_2}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}^-}} {{f(x)}}=-\\infty$ nên $x={x_1}$ là tiệm cận đứng của đồ thị hàm số $y=f(x)$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Đồ thị hàm số $y=f(x)$ nhận đường thẳng $y={random.choice([y_1,y_4])}$ làm một tiệm cận ngang"
	kq2_F=f"Đồ thị hàm số $y=f(x)$ nhận đường thẳng $y={y_3}$ làm một tiệm cận ngang"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{f(x)}}={y_1}, \\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{f(x)}}={y_4}$\n\n"\
	f" nên đồ thị hàm số $y=f(x)$ có các tiệm cận ngang là $y={y_1}$ và $y={y_4}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"*Đồ thị hàm số $y=f(x)$ có số đường tiệm cận đứng và tiệm cận ngang là ${{3}}$" 
	kq3_F=f"Đồ thị hàm số $y=f(x)$ có số đường tiệm cận đứng và tiệm cận ngang là ${{{random.choice([1,2,4])}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $x={x_1}$ và hai tiệm cận ngang là $y={y_1}, y={y_4}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	m= random.choice([i for i in range(-5, 6) if i!=0])
	n=random.choice([i for i in range(-5, 6) if i!=0])
	while n+y_1==0 or n+y_4 ==0:
		n=random.choice([i for i in range(-5, 6) if i!=0])
	
	chon=random.randint(1,3)
	if chon==1:
		kq4_T=f"*Đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)+{n}}}$ có một tiệm cận ngang là $y={random.choice([phan_so(m/(n+y_1)),phan_so(m/(n+y_4))])}$".replace("--","+").replace("+-","-")
		kq4_F=f"Đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)+{n}}}$ có một tiệm cận ngang là $y={random.choice([phan_so((n+y_1)/m), phan_so(m/y_1),phan_so(m/y_4), phan_so((n+y_3)/m)])}$".replace("--","+").replace("+-","-")
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{\\dfrac{{ {m} }}{{f(x)+{n}}}}}={phan_so(m/(n+y_1))}$,"\
		f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{\\dfrac{{ {m} }}{{f(x)+{n}}}}}={phan_so(m/(n+y_4))}$.\n\n"\
		f"Đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)+{n}}}$ có các tiệm cận ngang là $y={phan_so(m/(n+y_1))},y={phan_so(m/(n+y_4))}$.".replace("--","+").replace("+-","-")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"		
	if chon==2:
		n=y_3+1
		kq4_T=f"*Đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)-{n}}}$ có số tiệm cận đứng là ${{3}}$".replace("--","+").replace("+-","-")
		kq4_F=f"Đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)-{n}}}$ có số tiệm cận đứng là ${{{random.choice([1,2,4])}}}$".replace("--","+").replace("+-","-")
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f(x)-{n}=0 \\Leftrightarrow x=a<{x_1},x=b\\in ({x_1};{x_2}),x=c>{x_2}$.\n\n"\
		f"Khi $x \\to a$ hoặc $x \\to b$ hoặc $x \\to c$ thì $y=\\dfrac{{ {m} }}{{f(x)-{n}}} \\to \\infty$.\n\n"\
		f"Vậy đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)-{n}}}$ có 3 đường tiệm cận đứng.".replace("--","+").replace("+-","-")
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		n=y_3
		kq4_T=f"*Đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)-{n}}}$ có số tiệm cận đứng là ${{2}}$".replace("--","+").replace("+-","-")
		kq4_F=f"Đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)-{n}}}$ có số tiệm cận đứng là ${{{random.choice([1,3,4])}}}$".replace("--","+").replace("+-","-")
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$f(x)-{n}=0 \\Leftrightarrow x=a<{x_1},x={x_2}$.\n\n"\
		f"Khi $x \\to a$ hoặc $x \\to {x_2}$ thì $y=\\dfrac{{ {m} }}{{f(x)-{n}}} \\to \\infty$.\n\n"\
		f"Vậy đồ thị hàm số $y=\\dfrac{{ {m} }}{{f(x)-{n}}}$ có 2 đường tiệm cận đứng.".replace("--","+").replace("+-","-")
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

#[D12_C1_B3_12]-TF-M3. Cho hàm số y=(ax+b)/(cx+d). Xét Đ-S: TCĐ, TCN, giao điểm của TC, HCN tạo bởi 2 tiệm cận 
def prt_34_L12_C1_B3_12():
	x=sp.symbols("x")
	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b = random.randint(-8,8)
	c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a*d-b*c==0: b=b+1
	f=(a*x+b)/(c*x+d)
	x_0=-d/c
	if f.subs(x,x_0+0.1)>0:
		t=f"+\\infty"
	else:
		t=f"-\\infty"
	y_0=a/c
	noi_dung=f"Cho hàm $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau"

	kq1_T=f"*Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(x_0)}$"
	kq1_F=f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(-x_0)}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}}y={t}$ nên đồ thị hàm số có tiệm cận đứng là $x={phan_so(x_0)}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Tiệm cận ngang của đồ thị hàm số là đường thẳng $y={phan_so(y_0)}$"
	kq2_F=f"Tiệm cận ngang của đồ thị hàm số là đường thẳng $y={phan_so(-y_0)}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{y}}={phan_so(y_0)}$ nên đồ thị hàm số có tiệm cận ngang là $y={phan_so(y_0)}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if f.subs(x,x_0-0.1)>0:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
	else:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"

	if f.subs(x,x_0+0.1)>0:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=+\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
	else:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=-\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"

	kq3_T=f"*Giao điểm của tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y=f(x)$ là điểm $I\\left({phan_so(x_0)};{phan_so(y_0)}\\right)$" 
	kq3_F=f"Giao điểm của tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y=f(x)$ là điểm $I\\left({phan_so(x_0+random.randint(1,2))};{phan_so(y_0-random.randint(1,2))}\\right)$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Đồ thị hàm số $y=f(x)$ có đường tiệm cận đứng là $x={phan_so(x_0)}$ và đường tiệm cận ngang là $y={phan_so(y_0)}$.\n\n"\
	f"Giao điểm của hai đường tiệm cận là điểm $I\\left({phan_so(x_0)};{phan_so(y_0)}\\right)$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	S=abs(x_0*y_0)
	S_false=abs(1/2*x_0*y_0)
	kq4_T=f"*Hình chữ nhật giới hạn bởi 2 đường tiệm cận của đồ thị hàm số $y=f(x)$ và hai trục tọa độ có diện tích bằng ${phan_so(S)}$"
	kq4_F=f"Hình chữ nhật giới hạn bởi 2 đường tiệm cận của đồ thị hàm số $y=f(x)$ và hai trục tọa độ có diện tích bằng ${phan_so(S_false)}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Đồ thị hàm số $y=f(x)$ có đường tiệm cận đứng là $x={phan_so(x_0)}$ và đường tiệm cận ngang là $y={phan_so(y_0)}$.\n\n"\
	f"Hình chữ nhật giới hạn bởi 2 đường tiệm cận của đồ thị hàm số $y=f(x)$ và hai trục tọa độ có diện tích bằng:\n\n"\
	f"$S={phan_so(abs(x_0))}.{phan_so(abs(y_0))}={phan_so(S)}$."
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B3_13]-TF-M2. Cho limf. Xét Đ-S: TCĐ, TCN, Số TCD và TCN, TNC của y=(af+b)/(cf+d)
def prt_34_L12_C1_B3_13():
	lim_vc_trai=random.randint(-7,7)
	lim_vc_phai=random.randint(-7,7)
	x_0=random.randint(-5,5)
	lim_x0=random.choice([f"+\\infty",f"-\\infty"])
	if lim_vc_trai==lim_vc_phai: lim_vc_trai+=random.randint(1,3)
	dau=random.choice(["+","-"])

	noi_dung = f"Cho hàm số $y=f(x)$ xác định với mọi $x\\ne {x_0}$ có $\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{f(x)}}={lim_vc_trai},\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{f(x)}}={lim_vc_phai}$"\
	f" và $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^{dau}}} {{f(x)}}={lim_x0}$. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Đồ thị hàm số $y=f(x)$ có một tiệm cận ngang là $y={random.choice([lim_vc_trai,lim_vc_phai])}$" 
	kq1_F=f"Đồ thị hàm số $y=f(x)$ có một tiệm cận ngang là $x={random.choice([lim_vc_trai,lim_vc_phai])}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Đồ thị hàm số $y=f(x)$ có các tiệm cận ngang là $y={lim_vc_trai}$ và $y={lim_vc_phai}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $x={x_0}$"
	kq2_F=f"Đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $y={x_0}$ "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^{dau}}} {{f(x)}}={lim_x0}$ nên đồ thị hàm số $y=f(x)$ có tiệm cận đứng là $x={x_0}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"*Số tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y=f(x)$ là ${{3}}$" 
	kq3_F=f"Số tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y=f(x)$ là ${{{random.choice([1,2,4])}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Đồ thị hàm số $y=f(x)$ có 2 tiệm cận ngang là $y={lim_vc_trai},y={lim_vc_phai}$ và tiệm cận đứng là $x={x_0}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	a=random.randint(1,5)
	b=random.randint(-6,6)
	c = random.choice([i for i in range(-5, 5) if i!=0])
	d=random.randint(-6,6)
	while c*lim_vc_trai+d==0 or c*lim_vc_phai+d==0:
		a=random.randint(1,5)
		b=random.randint(-6,6)
		c = random.choice([i for i in range(-5, 5) if i!=0])
		d=random.randint(-6,6)
	t_1=(a*lim_vc_trai+b)/(c*lim_vc_trai+d)
	t_2=(a*lim_vc_phai+b)/(c*lim_vc_phai+d)

	f=sp.symbols("f(x)")

	ham_g=f"\\dfrac{{{a}f(x)+{b}}} {{{c}f(x)+d}}"
	ham_g=(a*f+b)/(c*f+d)

	kq4_T=f"*Đồ thị hàm số $y={latex(ham_g)}$ có một tiệm cận ngang là $y={phan_so(random.choice([t_1,t_2]))}$"
	kq4_F=f"Đồ thị hàm số $y={latex(ham_g)}$ có một tiệm cận ngang là $y={phan_so(random.choice([t_1+t_2, t_1/random.randint(2,3), t_2/random.randint(2,3)]))}$" 
	kq4=random.choice([kq4_T, kq4_F]).replace("+-","-")
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{{latex(ham_g)}}}={phan_so(t_1)}, \\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{{latex(ham_g)}}}={phan_so(t_2)}$.\n\n"\
	f"Suy ra đồ thị hàm số $y={latex(ham_g)}$ có các tiệm cận ngang là $y={phan_so(t_1)}$ và $y={phan_so(t_2)}$.".replace("+-","-")
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B3_14]-M2. Cho đường tiệm cận xiên. Tìm khẳng định đúng.
def prt_34_L12_C1_B3_14():
	f,x = sp.symbols('f(x) x')
	a = random.choice([i for i in range(-10, 10) if i!=0])
	b = random.choice([i for i in range(-10, 10) if i!=0])
	dau=random.choice(["+","-"])
	
	noi_dung=f"Cho hàm số $y=f(x)$ có đường tiệm cận xiên là $y={latex(a*x+b)}$. Tìm khẳng định đúng?"
	kq=f"{random.choice([f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{[{latex(f-(a*x+b))}]}}=0$", f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{[{latex(f-(a*x+b))}]}}=0$"])}"
	kq2=f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{[{latex(f-(a*x+b))}]}}={random.choice([a,b,"+\\infty","-\\infty"])}$"
	kq3=f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{[{latex(f-(a*x+b))}]}}={random.choice([a,b,"+\\infty","-\\infty"])}$"
	kq4=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {random.choice([a,b])}}} {{[{latex(f+(a*x+b))}]}}={dau}\\infty$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	
	dap_an=my_module.tra_ve_dap_an(list_PA)	

	debai= f"{noi_dung}\n\n"
	
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	
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

#[D12_C1_B3_15]-M2. Cho giới hạn. Tìm tiệm cận xiên.
def prt_34_L12_C1_B3_15():
	f,x = sp.symbols('f(x) x')
	a = random.choice([i for i in range(-10, 10) if i!=0])
	b = random.choice([i for i in range(-10, 10) if i!=0])
	dau=random.choice(["+","-"])
	gioi_han=f"{random.choice([f"$\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{[{latex(f-(a*x+b))}]}}=0$", f"$\\mathop{{\\lim}}\\limits_{{x \\to  -\\infty}} {{[{latex(f-(a*x+b))}]}}=0$"])}"
	
	noi_dung=f"Cho hàm số $y=f(x)$ có {gioi_han}. Tìm khẳng định đúng?"
	kq=f"Đường tiệm cận xiên của đồ thị hàm số $y=f(x)$ là $y={latex(a*x+b)}$"
	kq2=f"Đường tiệm cận xiên của đồ thị hàm số $y=f(x)$ là $y={random.choice([latex(-a*x-b), latex(-a*x+b), latex(a*x-b)])}$"
	kq3=f"Đường tiệm cận đứng của đồ thị hàm số $y=f(x)$ là $x={a}$"
	kq4=f"Đường tiệm cận ngang của đồ thị hàm số $y=f(x)$ là $y={b}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	
	dap_an=my_module.tra_ve_dap_an(list_PA)	

	debai= f"{noi_dung}\n\n"
	
	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	
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

#[D12_C1_B3_16]-M1. Đọc đường tiệm cận từ đồ thị hàm số y=(ax+b)/(cx+d)
def prt_34_L12_C1_B3_16():
	a = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	b = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	c = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	d = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	if a*d-b*c==0:
		d = d+1
	x=sp.symbols("x")

	f=(a*x+b)/(c*x+d)
	code_hinh=my_module.code_dothi_phanthuc_bac1(a,b,c,d)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	
	duong_tiem_can=random.choice(["đường tiệm cận đứng", "đường tiệm cận ngang"])

	if duong_tiem_can == "đường tiệm cận đứng":
		kq=-d/c
		kq2=d/c
		if d==0: 
			kq2=a/c
			kq3=(d+1)/c
		else:
			kq3=-c/d
		kq4=a/c
		if a/c==d/c or a/c==-d/c:
			kq4=(a+1)/c
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

		pa_A= f"*$x={phan_so(kq)}$"
		pa_B= f"$x={phan_so(kq2)}$"
		pa_C= f"$y={phan_so(kq3)}$"
		pa_D= f"$y={phan_so(kq4)}$"

	else: 
		kq=a/c
		kq2=c/a
		kq3=d/c
		kq4=-d/c
		if d==0: kq4=-a/c
		pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
		kq2=pa_kotrung[1]
		kq3=pa_kotrung[2]
		kq4=pa_kotrung[3]

		pa_A= f"*$y={phan_so(kq)}$"
		pa_B= f"$x={phan_so(kq2)}$"
		pa_C= f"$y={phan_so(kq3)}$"
		pa_D= f"$x={phan_so(kq4)}$"
	

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Cho hàm số $ y=\\dfrac{{ax+b}}{{cx+d}} (a,b,c,d \\in \\mathbb{{R}})$ có đồ thị là đường cong như hình dưới đây."\
	f" Đồ thị hàm số đã cho có {duong_tiem_can} là"
	noi_dung_loigiai=f"Dựa vào đồ thị hàm số ta có {duong_tiem_can} là {kq}."


#Trộn các phương án	

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n" \
   
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	  
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
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B3_17]-TF-M2. Cho y=(ax^2+bx+c)/(dx+e). Xét Đ-S: y',y'=0, tiệm cận đứng, tiệm cận xiên	
def prt_34_L12_C1_B3_17():
	x=sp.symbols("x")
	chon=random.randint(1,4)
	
	if chon==1:
		a = random.randint(1, 4)
		m = random.randint(1, 5)	
	if chon==2:
		a = random.randint(-4, -1)
		m = random.randint(-5, -1)
	if chon==3:
		a = random.randint(-4, -1)
		m = random.randint(1, 5)

	if chon==4:
		a = random.randint(1, 4)
		m = random.randint(-5, -1)
	
	
	b=random.randint(-5,5)	
	c = random.choice([random.randint(-5, -1), random.randint(1, 5)])	

	#f =ax+b +m/(cx+d)
	f=(a*x+b)+m/(x+c)
	g=latex(expand((a*x+b)*(x+c)+m))
	noi_dung = f"Cho hàm số $y=\\dfrac{{{g}}}{{{latex(x+c)}}}$. Xét tính đúng-sai của các khẳng định sau"
	x_0=-c
	if f.subs(x,x_0+0.1)>0:
		t=f"+\\infty"
	else:
		t=f"-\\infty"

	kq1_T=f"*Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(x_0)}$"
	kq1_F=f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(-x_0)}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}}y={t}$ nên đồ thị hàm số có tiệm cận đứng là $x={phan_so(x_0)}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Tiệm cận xiên của đồ thị hàm số là đường thẳng $y={latex(a*x+b)}$"
	kq2_F=f"Tiệm cận xiên của đồ thị hàm số là đường thẳng $y={latex(-a*x+b)}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Ta có $y=\\dfrac{{{g}}}{{{latex(x+c)}}}={latex(a*x+b+m/(x+c))}$.\n\n"\
	f"$\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} \\left[y -({latex(a*x+b)})\\right]=\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {latex(m/(x+c))}=0$.\n\n"\
	f"Đường tiệm cận xiên của đồ thị hàm số là $y={latex(a*x+b)}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if f.subs(x,x_0-0.1)>0:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
	else:
		lim_x0_trai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=-\\infty$"
		lim_x0_trai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^-}} {{y}}=+\\infty$"

	if f.subs(x,x_0+0.1)>0:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=+\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=-\\infty$"
	else:
		lim_x0_phai=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=-\\infty$"
		lim_x0_phai_false=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {phan_so(x_0)}^+}} {{y}}=+\\infty$"

	#y=(ax^2 +(ac+b)x + bc+m)/(x+c)
	a1, b1, c1, d1, e1 = a, a*c+b, b*c+m, 1, c
	f_dh=(a1*x**2+2*a1*e1*x+b1*e1-c1*d1)/(x+c)**2
	f_dh_false=(a1*x**2-2*a1*e1*x-b1*e1-c1*d1)/(x+c)**2
	kq3_T=f"* $y'={latex(f_dh)}$" 
	kq3_F=f"$y'={latex(f_dh_false)}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$y'={latex(f_dh)}$"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon==1 or chon ==2:

		kq4_T=f"* Phương trình $y'=0$ có 2 nghiệm phân biệt"
		kq4_F=f"Phương trình $y'=0$ {random.choice(["có 1 nghiệm", "vô nghiệm"])}"  
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$y'={latex(f_dh)}=0 \\Rightarrow {latex(a1*x**2-2*a1*c1*x+b1*e1-c1*d1)}=0$ (có 2 nghiệm phân biệt)."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	
	else:
		kq4_T=f"* Phương trình $y'=0$ vô nghiệm"
		kq4_F=f"Phương trình $y'=0$ {random.choice(["có 1 nghiệm", "có 2 nghiệm phân biệt"])}"  
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$y'={latex(f_dh)}=0 \\Rightarrow {latex(a1*x**2-2*a1*c1*x+b1*e1-c1*d1)}=0$ (có 2 nghiệm phân biệt)."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B3_18]-TL-M2. Cho y=(ax^2+bx+c)/(dx+e) có TCX là y=ax+b. Tính ma+nb.
def prt_34_L12_C1_B3_18():
	x=sp.symbols("x")
	a = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b=random.randint(-8,8)
	m = random.choice([random.randint(-7, -1), random.randint(1, 7)])

	d = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	e=random.choice([random.randint(-7, -1), random.randint(1, 7)])

	u = random.choice([i for i in range(1, 4) if i!=0])
	v = random.choice([i for i in range(-5, 4) if i!=0])
	t_a,t_b=sp.symbols("a b")
	#f =ax+b +m/(cx+d)
	f=latex(expand((a*x+b)*(d*x+e)+m))
	noi_dung = (f"Biết đồ thị hàm số $y=\\dfrac{{{f}}}{{{latex(d*x+e)}}}$ nhận đường thẳng $y=ax+b$ làm đường tiệm cận xiên."
		f" Tính ${latex(u*t_a+v*t_b)}$.".replace("+-","-")
		)
	dap_an=u*a+v*b

	noi_dung_loigiai=(f"Ta có $y=\\dfrac{{{f}}}{{{latex(d*x+e)}}}={latex(a*x+b+m/(d*x+e))}$.\n\n"
	f"$\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} \\left[y -({latex(a*x+b)})\\right]=\\mathop{{\\lim}}\\limits_{{x \\to  + \\infty }} {latex(m/(d*x+e))}=0$.\n\n"
	f"Đường tiệm cận xiên của đồ thị hàm số là $y={latex(a*x+b)}\\Rightarrow a={a}, b={b}$.\n\n"
	f"${latex(u*t_a+v*t_b)}={dap_an}$."
	)


	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#BÀI 5 - ĐỒ THỊ HÀM SỐ

#[D12_C1_B4_01]-M2. Cho đồ thị. Tìm hàm số bậc 3 tương ứng.
def prt_34_L12_C1_B4_01():		
	x = sp.symbols('x')
	x1=random.randint(-2,0)
	x2=random.randint(0,2)
	x3=random.randint(1,2)
	k=random.choice([1,-1])	
	f=k*x**3 - k*x**2*x1 - k*x**2*x2 - k*x**2*x3 + k*x*x1*x2 + k*x*x1*x3 + k*x*x2*x3 - k*x1*x2*x3
	a=f.coeff(x,3)
	b=f.coeff(x,2)
	c=f.coeff(x,1)
	d=f.as_coefficients_dict()[1]

	#Vẽ đồ thị
	code_hinh=my_module.code_dothi_bac_3(a,b,c,d)
	kq=f"$y={latex(f)}$"
	kq2=f"$y={latex(a*x**3-b*x**2+d)}$"
	kq3=f"$y={latex(-a*x**3+b*x**2+c*x+d)}$"
	kq4=f"$y={latex(a*x**3+b*x**2+c*x+d+random.randint(2,5))}$"
	if d!=0:
		kq4=f"$y={latex(a*x**3+b*x**2+c*x-d)}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

	noi_dung = f"Đồ thị như hình vẽ dưới đây là của hàm số nào?"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""

	debai= f"{noi_dung}\n"\
	f"{file_name}\n"
	
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_02]-M2. Cho đồ thị. Tìm hàm số bậc 4 tương ứng.
def prt_34_L12_C1_B4_02():	
	x = sp.symbols('x')
	a = random.randint(-2,2)
	if a==0:
	    a = random.choice([random.randint(1,2),random.randint(-2,-1)])
	b = random.randint(-4,4)
	if b==0:
	    b = random.choice([random.randint(1,3),random.randint(-3,-1)])
	c = random.randint(-4,4)

	f=a*x**4+b*x**2+c
	
	#Vẽ đồ thị
	code_hinh=my_module.code_dothi_bac_4(a,b,c)


	kq=f"$y={latex(f)}$"
	kq2=f"$y={latex(a*x**4-b*x**2+c)}$"
	kq3=f"$y={latex(a*x**3+b*x**2+c)}$"
	kq4=f"$y={latex(-a*x**4+b*x**2+c)}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	noi_dung = f"Đồ thị như hình vẽ dưới đây là của hàm số nào?"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)	

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"
	
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_03]-M2. Cho đồ thị. Tìm hàm số y=(ax+b)/(cx+d) tương ứng.
def prt_34_L12_C1_B4_03():
	x = sp.symbols('x')
	a = random.randint(-4,4)
	if a==0:
	    a = random.choice([random.randint(1,4),random.randint(-4,-1)])

	b = random.randint(-4,4)
	if b==0:
	    b = random.choice([random.randint(1,3),random.randint(-3,-1)])

	c = random.randint(-4,4)
	if c==0:
	    c = random.choice([random.randint(1,4),random.randint(-4,-1)])

	d = random.randint(-4,4)
	if a*d-b*c==0: 
		d = d+1

	f=(a*x+b)/(c*x+d)
	
	#Vẽ đồ thị
	code_hinh=my_module.code_dothi_phanthuc_bac1(a,b,c,d)	

	kq=f"$y={latex(f)}$"
	kq2=f"$y={latex((a*x-b)/(c*x+d))}$"
	kq3=f"$y={latex((c*x+d)/(a*x+b))}$"
	kq4=f"$y={latex((a*x+b)/(-c*x+d))}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

	noi_dung = f"Đồ thị như hình vẽ dưới đây là của hàm số nào?" 

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	dap_an=my_module.tra_ve_dap_an(list_PA)	

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"
	
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_04]-M2. Cho bảng biến thiên. Tìm hàm số y=(ax+b)/(cx+d) tương ứng.
def prt_34_L12_C1_B4_04():
	x = sp.symbols('x')
	a = random.randint(-4,4)
	if a==0:
	    a = random.choice([random.randint(1,4),random.randint(-4,-1)])

	b = random.randint(-4,4)
	if b==0:
	    b = random.choice([random.randint(1,3),random.randint(-3,-1)])

	c = random.randint(-4,4)
	if c==0:
	    c = random.choice([random.randint(1,4),random.randint(-4,-1)])

	d = random.randint(-4,4)
	if a*d-b*c==0: 
		d = d+1

	f=(a*x+b)/(c*x+d)
	
	#Vẽ đồ thị
	code_hinh=my_module.code_bbt_phanthucbac1(a,b,c,d)

	kq=f"$y={latex(f)}$"
	kq2=f"$y={latex((-a*x-b)/(c*x+d))}$"
	kq3=f"$y={latex((a*x+d)/(c*x+b+1))}$"
	kq4=f"$y={latex((a*x-b)/(-c*x+d))}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

	noi_dung= f"Bảng biến thiên như hình vẽ dưới đây là của hàm số nào?"

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	dap_an=my_module.tra_ve_dap_an(list_PA)	

	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"
	
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_05]-M2. Cho đồ thị. Tìm hàm số y=(ax^2+bx+c)/(dx+e).
def prt_34_L12_C1_B4_05():
	x = sp.symbols('x')
	chon=random.randint(1,6)
	
	if chon==1:
		x_0=random.randint(-3,3)
		a=random.choice([random.randint(-4, -1), random.randint(1, 4)])		
		f=x+a/(x-x_0)

		kq=f"$y={latex((x**2-x_0*x+a)/(x-x_0))}$"
		kq2=f"$y={latex((x**2-x_0*x+a+random.randint(1,3))/(x-x_0))}$"
		kq3=f"$y={latex((random.randint(2,4)*x**2+x_0*x+a)/(x+x_0))}$"
		kq4=f"$y={latex((x**2-x_0*x+a-random.randint(1,3))/(x-x_0))}$"

		noi_dung_loigiai=f"Đồ thị có tiệm cận đứng là $x={x_0}$.\n\n"\
		f"Đồ thị có tiệm cận xiên là $y=x$.\n\n"\
		f"Đây là đồ thị hàm số {kq}."
		#Vẽ đồ thị
		code_hinh=code_dothi_phanthuc_bac2(1,-x_0,a,1,-x_0)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

	if chon==2:
		x_0=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		a=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		f=x+x_0 +a/(x-x_0)

		kq=f"$y={latex((x**2-x_0*x+a)/(x-x_0))}$"
		kq2=f"$y={latex((x**2-x_0**2+a+random.randint(1,3))/(x-x_0))}$"
		kq3=f"$y={latex((random.randint(2,4)*x**2+x_0*x+a)/(x+x_0))}$"
		kq4=f"$y={latex((x**2-x_0**2-a)/(x-x_0))}$"

		noi_dung_loigiai=f"Đồ thị có tiệm cận đứng là $x={x_0}$.\n\n"\
		f"Đồ thị có tiệm cận xiên là $y={latex(x+x_0)}$.\n\n"\
		f"Đây là đồ thị hàm số {kq}."
	
		#Vẽ đồ thị
		code_hinh=code_dothi_phanthuc_bac2(1,-x_0,a,1,-x_0)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

	if chon==3:
		x_0=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		m=random.choice([1,2])		
		f=(x**2-x_0*x+m**2)/(x-x_0)

		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex((x**2-x_0*x+m**2+random.randint(1,3))/(x-x_0))}$"
		kq3=f"$y={latex((random.randint(2,3)*x**2+x_0*x+m)/(x+x_0))}$"
		kq4=f"$y={latex((x**2-x+m**2+random.randint(1,3))/(x-x_0))}$"

		noi_dung_loigiai=f"Đồ thị có tiệm cận đứng là $x={x_0}$.\n\n"\
		f"Đồ thị có tiệm cận xiên là $y=x$.\n\n"\
		f"Đây là đồ thị hàm số {kq}."
		
		#Vẽ đồ thị
		code_hinh=code_dothi_phanthuc_bac2(1,-x_0,m**2,1,-x_0)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

	if chon==4:
		x_0=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		m=random.choice([1,2])		
		f=(-x**2+x_0*x-m**2)/(x-x_0)

		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex((x**2+x_0*x-m**2)/(x-x_0))}$"
		kq3=f"$y={latex((random.randint(2,3)*x**2+x_0*x+m)/(x+x_0))}$"
		kq4=f"$y={latex((-x**2+x_0*x-m**2+random.randint(1,2))/(x-x_0))}$"

		noi_dung_loigiai=f"Đồ thị có tiệm cận đứng là $x={x_0}$.\n\n"\
		f"Đồ thị có tiệm cận xiên là $y=x$.\n\n"\
		f"Đây là đồ thị hàm số {kq}."
		
		#Vẽ đồ thị
		code_hinh=code_dothi_phanthuc_bac2(-1,x_0,-m**2,1,-x_0)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

	if chon==5:
		x_0=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		a=random.choice([random.randint(-2, -1), random.randint(1, 2)])
		m=random.choice([1,2])		
		f=(x**2+(a-x_0)*x-a*x_0-m)/(x-x_0)

		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex((-x**2+(a-x_0)*x-a*x_0-m)/(x-x_0))}$"
		kq3=f"$y={latex((random.randint(2,3)*x**2+x_0*x+m)/(x+x_0))}$"
		kq4=f"$y={latex((x**2+a*x-x_0-m)/(x-x_0))}$"

		noi_dung_loigiai=f"Đồ thị có tiệm cận đứng là $x={x_0}$.\n\n"\
		f"Đồ thị có tiệm cận xiên là $y={latex(x+a)}$.\n\n"\
		f"Đây là đồ thị hàm số {kq}."
		
		#Vẽ đồ thị
		code_hinh=code_dothi_phanthuc_bac2(1,a-x_0,-a*x_0-m,1,-x_0)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)

	if chon==6:
		x_0=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		a=random.choice([random.randint(-2, -1), random.randint(1, 2)])
		m=random.choice([1,2])		
		f=(-x**2-(a-x_0)*x+a*x_0+m)/(x-x_0)

		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex((x**2-(a-x_0)*x+a*x_0+m)/(x-x_0))}$"
		kq3=f"$y={latex((random.randint(-2,-1)*x**2+x_0*x+m)/(x+x_0))}$"
		kq4=f"$y={latex((-x**2-(a-x_0)*x+a*x_0+m-random.randint(1,2))/(x-x_0))}$"

		noi_dung_loigiai=f"Đồ thị có tiệm cận đứng là $x={x_0}$.\n\n"\
		f"Đồ thị có tiệm cận xiên là $y={latex(-x-a)}$.\n\n"\
		f"Đây là đồ thị hàm số {kq}."
		
		#Vẽ đồ thị
		code_hinh=code_dothi_phanthuc_bac2(-1,-a+x_0,a*x_0+m,1,-x_0)	
		code = my_module.moi_truong_anh_latex(code_hinh)
		file_name=my_module.pdftoimage_timename(code)


	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

	noi_dung = f"Đồ thị như hình vẽ dưới đây là của hàm số nào?" 

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
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_06]-TF-M2. Cho hàm số bậc 3. Xét Đ-S: y', đơn điệu, BBT, đồ thị
def prt_34_L12_C1_B4_06():
	x=sp.symbols("x")
	dau=random.choice(['+','-'])
	if dau=='+':
		chon=random.randint(1,5)		
		if chon==1:
			a,b,c,d=1,-3,0,random.randint(-2,2)
			x_1,x_2=0,2
			f=a*x**3+b*x**2+c*x+d
		if chon==2:
			a,b,c,d=1,0,-3,random.randint(-2,3)
			x_1,x_2=-1,1
			f=a*x**3+b*x**2+c*x+d
		if chon==3:
			a,b,c,d=1/3,3/2,2,random.randint(-3,3)
			x_1,x_2=-2,-1
			f=x**3/3+3*x**2/2+2*x+d
		if chon==4:
			a,b,c,d=1/3,-2,3,random.randint(-3,3)
			x_1,x_2=1,3
			f=x**3/3-2*x**2+3*x+d
		if chon==5:
			a,b,c,d=1/3,1/2,0,random.randint(-3,3)
			x_1,x_2=-1,0
			f=x**3/3+x**2/2+d

	if dau=='-':
		chon=random.randint(1,5)		
		if chon==1:
			a,b,c,d=-1,3,0,random.randint(-2,2)
			x_1,x_2=0,2
			f=a*x**3+b*x**2+c*x+d
		if chon==2:
			a,b,c,d=-1,0,3,random.randint(-2,3)
			x_1,x_2=-1,1
			f=a*x**3+b*x**2+c*x+d
		if chon==3:
			a,b,c,d=-1/3,-3/2,-2,random.randint(-3,3)
			x_1,x_2=-2,-1
			f=-x**3/3-3*x**2/2-2*x+d
		if chon==4:
			a,b,c,d=-1/3,2,-3,random.randint(-3,3)
			x_1,x_2=1,3
			f=-x**3/3+2*x**2-3*x+d
		if chon==5:
			a,b,c,d=-1/3,-1/2,0,random.randint(-3,3)
			x_1,x_2=-1,0
			f=-x**3/3-x**2/2+d	

	noi_dung = f"Cho hàm số $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau. ".replace("+-","-")
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Hàm số có đạo hàm là $y'={latex(diff(f,x))}$" 
	kq1_F=f"Hàm số có đạo hàm là $y'={latex(diff(f,x)+random.randint(1,5))}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$y'={latex(diff(f,x))}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if dau=="+":
		kq2_T=random.choice([f"*$y'>0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$", f"*$y'<0$ khi $x\\in ({x_1};{x_2})$"])
		kq2_F=random.choice([f"$y'>0$ khi $x\\in ({x_1};{x_2})$", f"$y'<0$ khi $x \\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$"])
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"$y'>0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$.\n\n"\
		f"$y'<0$ khi $x\\in ({x_1};{x_2})$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if dau=="-":
		kq2_T=random.choice([f"*$y'>0$ khi $x\\in ({x_1};{x_2})$", f"*$y'<0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$"])
		kq2_F=random.choice([f"$y'>0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$", f"$y'<0$ khi $x\\in ({x_1};{x_2})$"])
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"$y'>0$ khi $x\\in ({x_1};{x_2})$.\n\n"\
		f"$y'<0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	y_1,y_2=f.subs(x,x_1),f.subs(x,x_2)

	code_BBT=code_bbt_bac3_2nghiem(a,x_1,x_2,latex(y_1),latex(y_2))
	code = my_module.moi_truong_anh_latex(code_BBT)
	file_name=my_module.pdftoimage_timename(code)
	file_name_BBT_HDG=my_module.pdftoimage_timename(code)

	if a>0:
		code_BBT_false=code_bbt_bac3_2nghiem(a,x_1,x_2,latex(y_1+random.randint(1,3)),latex(y_2-random.randint(1,3)))
		code= my_module.moi_truong_anh_latex(code_BBT_false)
		file_name_false=my_module.pdftoimage_timename(code)
	else:
		code_BBT_false=code_bbt_bac3_2nghiem(a,x_1,x_2,latex(y_1-random.randint(1,3)),latex(y_2+random.randint(1,3)))
		code= my_module.moi_truong_anh_latex(code_BBT_false)
		file_name_false=my_module.pdftoimage_timename(code)

	kq3_T=f"*Hàm số có bảng biến thiên là\n\n"\
	f"{file_name}"	
	kq3_F=f"Hàm số có bảng biến thiên là\n\n"\
	f"{file_name_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$x={x_1}\\Rightarrow y={phan_so(y_1)}, x={x_2}\\Rightarrow y={phan_so(y_2)}$.\n\n"\
	f"Hàm số có bảng biến thiên là\n\n"\
	f"{file_name_BBT_HDG}"

	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	code_dothi=code_dothi_bac_3(a,b,c,d)
	code = my_module.moi_truong_anh_latex(code_dothi)
	file_name=my_module.pdftoimage_timename(code)
	file_name_dothi_HGD=my_module.pdftoimage_timename(code)

	code_dothi_false=code_dothi_bac_3(-a,-b,-c,-d)
	code = my_module.moi_truong_anh_latex(code_dothi_false)
	file_name_false=my_module.pdftoimage_timename(code)
	

	kq4_T=f"*Hàm số có đồ thị là\n\n"\
	f"{file_name}"
	kq4_F=f"Hàm số có đồ thị là\n\n"\
	f"{file_name_false}"
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Hàm số có đồ thị là\n\n"\
	f"{file_name_dothi_HGD}"

	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	list_TF=tra_ve_TF(list_PA)

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

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	kq3_T=f"*Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT}"	
	kq3_F=f"Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$x={x_1}\\Rightarrow y={phan_so(y_1)}, x={x_2}\\Rightarrow y={phan_so(y_2)}$.\n\n"\
	f"Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT}"

	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"*Hàm số có đồ thị là\\\\"\
	f"{code_dothi}"
	kq4_F=f"Hàm số có đồ thị là\\\\"\
	f"{code_dothi_false}"
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Hàm số có đồ thị là\n\n"\
	f"{code_dothi}"
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)	

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

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
		st=list_PA[i]
		if st[0]=="*":
			st_new=f"\\True " + st[1:]
			list_PA[i]=st_new
		else:
			list_PA[i]=st


	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B4_07]-TF-M2. Cho hàm số y=(ax+b)/(cx+d). Xét Đ-S: y', đơn điệu, BBT, đồ thị
def prt_34_L12_C1_B4_07():
	x=sp.symbols("x")
	a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	b = random.randint(-5, 5)
	c = random.choice([i for i in range(-5, 5) if i!=0])
	d = random.choice([i for i in range(-5, 5) if i!=0])
	if a*d-b*c==0: b=b+1
	f=(a*x+b)/(c*x+d)	

	noi_dung = f"Cho hàm số $y={latex(f)}$. Xét tính đúng-sai của các khẳng định sau."
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Hàm số có $y'=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$" 
	kq1_F=f"Hàm số có $y'=\\dfrac{{{-a*d+b*c}}}{{{latex((c*x+d)**2)}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$y'=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if a*d-b*c>0:
		kq2_T=f"*Hàm số đồng biến trên các khoảng $\\left(-\\infty;{phan_so(-d/c)}\\right)$ và $\\left({phan_so(-d/c)};+\\infty\\right)$"
		kq2_F=f"Hàm số nghịch biến trên các khoảng $\\left(-\\infty;{phan_so(-d/c)}\\right)$ và $\\left({phan_so(-d/c)};+\\infty\\right)$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'>0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
		f"Hàm số đồng biến trên các khoảng $\\left(-\\infty;{phan_so(-d/c)}\\right)$ và $\\left({phan_so(-d/c)};+\\infty\\right)$.\n\n"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if a*d-b*c<0:
		kq2_T=f"*Hàm số nghịch biến trên các khoảng $\\left(-\\infty;{phan_so(-d/c)}\\right)$ và $\\left({phan_so(-d/c)};+\\infty\\right)$"
		kq2_F=f"Hàm số đồng biến trên các khoảng $\\left(-\\infty;{phan_so(-d/c)}\\right)$ và $\\left({phan_so(-d/c)};+\\infty\\right)$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'<0,\\forall x \\ne {phan_so(-d/c)}$.\n\n"\
		f"Hàm số nghịch biến trên các khoảng $\\left(-\\infty;{phan_so(-d/c)}\\right)$ và $\\left({phan_so(-d/c)};+\\infty\\right)$.\n\n"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	

	code_BBT=code_bbt_phanthucbac1(a,b,c,d)
	code = my_module.moi_truong_anh_latex(code_BBT)
	file_name=my_module.pdftoimage_timename(code)
	file_name_BBT_HDG=my_module.pdftoimage_timename(code)

	
	code_BBT_false=code_bbt_phanthucbac1(-a,-b,c,d)
	code= my_module.moi_truong_anh_latex(code_BBT_false)
	file_name_false=my_module.pdftoimage_timename(code)


	kq3_T=f"*Hàm số có bảng biến thiên là\n\n"\
	f"{file_name}"	
	kq3_F=f"Hàm số có bảng biến thiên là\n\n"\
	f"{file_name_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Hàm số có bảng biến thiên là\n\n"\
	f"{file_name_BBT_HDG}"

	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	code_dothi=code_dothi_phanthuc_bac1(a,b,c,d)
	code = my_module.moi_truong_anh_latex(code_dothi)
	file_name=my_module.pdftoimage_timename(code)

	code_dothi_false=code_dothi_phanthuc_bac1(-a,-b,c,d)
	code = my_module.moi_truong_anh_latex(code_dothi_false)
	file_name_false=my_module.pdftoimage_timename(code)
	file_name_dothi_HGD=my_module.pdftoimage_timename(code)

	kq4_T=f"*Hàm số có đồ thị là\n\n"\
	f"{file_name}"
	kq4_F=f"Hàm số có đồ thị là\n\n"\
	f"{file_name_false}"
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Hàm số có đồ thị là\n\n"\
	f"{file_name_dothi_HGD}"

	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	list_TF=tra_ve_TF(list_PA)

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

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	kq3_T=f"*Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT}"	
	kq3_F=f"Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT}"

	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"*Hàm số có đồ thị là\\\\"\
	f"{code_dothi}"
	kq4_F=f"Hàm số có đồ thị là\\\\"\
	f"{code_dothi_false}"
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Hàm số có đồ thị là\n\n"\
	f"{code_dothi}"
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)	

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

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
		st=list_PA[i]
		if st[0]=="*":
			st_new=f"\\True " + st[1:]
			list_PA[i]=st_new
		else:
			list_PA[i]=st


	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B4_08]-TF-M2. Cho hàm số y=(ax^2+bx+c)/(dx+e). Xét Đ-S: y', đơn điệu, BBT, đồ thị
def prt_34_L12_C1_B4_08():
	x=sp.symbols("x")
	chon=random.randint(1,2)
	if chon==1:
		x_0=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		a=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		m=random.randint(1, 2)
		f=x+a+m**2/(x-x_0)	
		ham=(x**2+(a-x_0)*x+m**2-a*x_0)/(x-x_0)
		x_1, x_2 = x_0-m, x_0+m
		a1,b1,c1,d1,e1=1, a-x_0, m**2-a*x_0, 1, -x_0

		kq1_T=f"*Hàm số có đạo hàm là $y'=\\dfrac{{{latex(expand((x-x_0)**2-m**2))}}} {{{latex((x-x_0)**2)}}}$" 
		kq1_F=f"Hàm số có đạo hàm là $y'=\\dfrac{{{latex(expand((x-x_0)**2+m**2))}}} {{{latex((x-x_0)**2)}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$y'=\\dfrac{{{latex(expand((x-x_0)**2-m**2))}}} {{{latex((x-x_0)**2)}}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq2_T=random.choice([f"*$y'>0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$", f"*$y'<0$ khi $x\\in ({x_1};{x_0})$", f"*$y'<0$ khi $x\\in ({x_0};{x_2})$"])
		kq2_F=random.choice([f"$y'>0$ khi $x\\in ({x_1};{x_2})$", f"$y'<0$ khi $x \\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$"])
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"$y'>0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$.\n\n"\
		f"$y'<0$ khi $x\\in ({x_1};{x_2})$."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==2:
		x_0=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		a=random.choice([random.randint(-3, -1), random.randint(1, 3)])
		m=random.randint(1, 2)
		f=-x+a-m**2/(x-x_0)
		ham=(-x**2+(a+x_0)*x-m**2-a*x_0)/(x-x_0)
		x_1, x_2 = x_0-m, x_0+m
		a1,b1,c1,d1,e1=-1, a+x_0, -m**2-a*x_0, 1, -x_0

		kq1_T=f"*Hàm số có đạo hàm là $y'=\\dfrac{{{latex(expand(-(x-x_0)**2+m**2))}}} {{{latex((x-x_0)**2)}}}$" 
		kq1_F=f"Hàm số có đạo hàm là $y'=\\dfrac{{{latex(expand(-(x-x_0)**2-m**2))}}} {{{latex((x-x_0)**2)}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$y'=\\dfrac{{{latex(expand(-(x-x_0)**2+m**2))}}} {{{latex((x-x_0)**2)}}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		kq2_T=random.choice([f"*$y'>0$ khi $x\\in ({x_1};{x_0})$",f"*$y'>0$ khi $x\\in ({x_0};{x_2})$", f"*$y'<0$ khi $x \\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$"])		
		kq2_F=random.choice([f"$y'>0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$", f"$y'<0$ khi $x\\in ({x_1};{x_2})$"])
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$y'=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f"$y'>0$ khi $x\\in ({x_1};{x_2})$.\n\n"\
		f"$y'<0$ khi $x\\in (-\\infty;{x_1})\\cup ({x_2};+\\infty)$.\n\n"
		
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	

	noi_dung = f"Cho hàm số $y={latex(ham)}$. Xét tính đúng-sai của các khẳng định sau. "
	debai_word= f"{noi_dung}\n"


	code_BBT=code_bbt_phanthucbac2(a1,b1,c1,d1,e1)
	code = my_module.moi_truong_anh_latex(code_BBT)
	file_name=my_module.pdftoimage_timename(code)
	file_name_BBT_HDG=my_module.pdftoimage_timename(code)


	code_BBT_false=code_bbt_phanthucbac2(-a1,-b1,-c1,d1,e1)
	code= my_module.moi_truong_anh_latex(code_BBT_false)
	file_name_false=my_module.pdftoimage_timename(code)

	y_1, y_2 = f.subs(x,x_1), f.subs(x,x_2)
	kq3_T=f"*Hàm số có bảng biến thiên là\n\n"\
	f"{file_name}"	
	kq3_F=f"Hàm số có bảng biến thiên là\n\n"\
	f"{file_name_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$x={x_1}\\Rightarrow y={phan_so(y_1)}, x={x_2}\\Rightarrow y={phan_so(y_2)}$.\n\n"\
	f"Hàm số có bảng biến thiên là\n\n"\
	f"{file_name_BBT_HDG}"

	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	code_dothi=code_dothi_phanthuc_bac2(a1,b1,c1,d1,e1)
	code = my_module.moi_truong_anh_latex(code_dothi)
	file_name=my_module.pdftoimage_timename(code)

	code_dothi_false=code_dothi_phanthuc_bac2(-a1,-b1,-c1,d1,e1)
	code = my_module.moi_truong_anh_latex(code_dothi_false)
	file_name_false=my_module.pdftoimage_timename(code)
	file_name_dothi_HGD=my_module.pdftoimage_timename(code)

	kq4_T=f"*Hàm số có đồ thị là\n\n"\
	f"{file_name}"
	kq4_F=f"Hàm số có đồ thị là\n\n"\
	f"{file_name_false}"
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Hàm số có đồ thị là\n\n"\
	f"{file_name_dothi_HGD}"

	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	list_TF=tra_ve_TF(list_PA)

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

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	kq3_T=f"*Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT}"	
	kq3_F=f"Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT_false}"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$x={x_1}\\Rightarrow y={phan_so(y_1)}, x={x_2}\\Rightarrow y={phan_so(y_2)}$.\n\n"\
	f"Hàm số có bảng biến thiên là\n\n"\
	f"{code_BBT}"

	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"*Hàm số có đồ thị là\\\\"\
	f"{code_dothi}"
	kq4_F=f"Hàm số có đồ thị là\\\\"\
	f"{code_dothi_false}"
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Hàm số có đồ thị là\n\n"\
	f"{code_dothi}"
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)	

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

	loigiai_latex=f"\n\n a) {loigiai[0]}\n\n"\
	f"b) {loigiai[1]}\n\n"\
	f"c) {loigiai[2]}\n\n"\
	f"d) {loigiai[3]}\n\n"

	#Tạo đề latex
	for i in range(len(list_PA)):
		st=list_PA[i]
		if st[0]=="*":
			st_new=f"\\True " + st[1:]
			list_PA[i]=st_new
		else:
			list_PA[i]=st


	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
	    f"\\choiceTFt\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an


#[D12_C1_B4_09]-M2. Cho bảng biến thiên, tìm hàm số bậc 3.
def prt_34_L12_C1_B4_09():
	x=sp.symbols("x")	
	chon_ham=random.randint(1,6)		
	if chon_ham==1:
		a,b,c,d=1,-3,0,random.randint(-3,3)
		f=a*x**3 + b*x**2 +c*x+d
		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex(a*x**4 + b*x**2 +c)}$"
		kq3=f"$ y={latex((a*x+b)/(x+random.randint(1,4)))}$"
		kq4=f"$y={latex(a*x**3+(b+random.randint(1,3))*x**2+d+random.randint(1,6))}$"
	if chon_ham==2:
		a,b,c,d=-1,3,0,random.randint(-3,3)
		f=a*x**3 + b*x**2 +c*x+d
		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex(a*x**4 + b*x**2 +c)}$"
		kq3=f"$ y={latex((a*x+b)/(d*x+random.randint(1,4)))}$"
		kq4=f"$y={latex(a*x**3+(b+random.randint(1,3))*x**2+d+random.randint(-6,6))}$"
	if chon_ham==3:
		a,b,c,d=1,0,-3,random.randint(-3,3)	
		f=a*x**3 + b*x**2 +c*x+d		
		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex(a*x**4 + b*x**2 +c)}$"
		kq3=f"$ y={latex((a*x+b)/(d*x+random.randint(1,4)))}$"
		kq4=f"$y={latex(a*x**3+(c+random.randint(1,3))*x+d+random.randint(-6,6))}$"

	if chon_ham==4:
		a,b,c,d=-1,0,3,random.randint(-3,3)
		f=a*x**3 + b*x**2 +c*x+d
		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex(a*x**4 + b*x**2 +c)}$"
		kq3=f"$ y={latex((a*x+b)/(d*x+random.randint(1,4)))}$"
		kq4=f"$y={latex(a*x**3+(c+random.randint(1,4))*x+d+random.randint(-6,6))}$"
	
	if chon_ham==5:
		a,b,c,d=random.randint(1,3),0,random.randint(1,3),random.randint(-3,3)
		f=a*x**3 + b*x**2 +c*x+d
		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex(a*x**4 + b*x**2 +c)}$"
		kq3=f"$ y={latex((a*x+b)/(c*x+random.randint(1,4)))}$"
		kq4=f"$y={latex(a*x**3-c*x+d+random.randint(-6,6))}$"
		
	if chon_ham==6:
		a,b,c,d=random.randint(-3,-1),0,random.randint(-3,-1),random.randint(-3,3)
		f=a*x**3 + b*x**2 +c*x+d
		kq=f"$y={latex(f)}$"
		kq2=f"$y={latex(a*x**4 + b*x**2 +c)}$"
		kq3=f"$ y={latex((a*x+b)/(c*x+random.randint(1,4)))}$"
		kq4=f"$y={latex(a*x**3-c*x+d+random.randint(-6,6))}$"

		
	code_hinh=my_module.code_bbt_bac3(a,b,c,d)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)		
		
	noi_dung_loigiai=f"Dựa vào bảng biến thiên ta có hàm số phải có dạng $y=ax^3+bx^2+cx+d$.\n\n"\
	f"Theo dáng bảng biến thiên suy ra hàm số là {kq}."	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung = f"Hàm số nào dưới đây có bảng biến thiên như sau"


	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"   
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	  
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\\begin{{center}}{code_hinh}\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_10]. Cho hai hàm số. Tìm số giao điểm của 2 đồ thị.
def prt_34_L12_C1_B4_10():
	x = sp.symbols('x')	

	a = random.randint(-5,5)
	if a==0:
	    a = random.choice([random.randint(1,5),random.randint(-5,-1)])

	b = random.randint(-4,4)
	if b==0:
	    b = random.choice([random.randint(1,4),random.randint(-4,-1)])

	c = random.randint(-4,4)
	if c==0:
	    c = random.choice([random.randint(1,4),random.randint(-4,-1)])

	d = random.randint(-4,4)

	m = random.randint(-5,5)
	if m==0:
	    m = random.choice([random.randint(1,5),random.randint(-5,-1)])

	n = random.randint(-5,5)	

	f=(a*x+b)/(c*x+d)
	g=m*x+n

	equation = Eq((a*x+b)/(c*x+d) - m*x-n, 0)	
	solutions = solve(equation, x)
	so_nghiem=len(solutions)

	for item in solutions:
		if "I" in str(item): so_nghiem = 0

	kq=f"${{{so_nghiem}}}$" 	       	
	if so_nghiem == 0:	
		kq2=f"${{{so_nghiem + 1}}}$"
		kq3=f"${{{so_nghiem + 2}}}$"
		kq4=f"${{{so_nghiem + 3}}}$"
	if so_nghiem == 1:
		kq2=f"${{{so_nghiem - 1}}}$"
		kq3=f"${{{so_nghiem + 1}}}$"
		kq4=f"${{{so_nghiem + 2}}}$"
	if so_nghiem == 2:
		kq2=f"${{{so_nghiem - 2}}}$"
		kq3=f"${{{so_nghiem + 1}}}$"
		kq4=f"${{{so_nghiem + 2}}}$"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

	noi_dung= f"Tìm số giao điểm của đồ thị các hàm số $y={latex(f)}$ và $y={latex(g)}$."
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f""

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
	f"\\shortans[4]{{{kq}}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_11]. Cho đồ thị. Tìm số nghiệm của phương trình f(x)=m
def prt_34_L12_C1_B4_11():
	
	x = sp.symbols('x')
	x1=random.randint(-2,0)
	x2=random.randint(0,2)
	x3=random.randint(1,2)
	k=random.choice([1,-1])	
	f=k*x**3 - k*x**2*x1 - k*x**2*x2 - k*x**2*x3 + k*x*x1*x2 + k*x*x1*x3 + k*x*x2*x3 - k*x1*x2*x3
	a=f.coeff(x,3)
	b=f.coeff(x,2)
	c=f.coeff(x,1)
	d=f.as_coefficients_dict()[1]

	#Tính đạo hàm
	g=diff(f,x)
	equation = Eq(g, 0)	
	solutions = solve(equation, x)

	#Tính giá trị cực trị
	x_1=solutions[0]
	x_2=solutions[1]
	y_1=f.subs(x,x_1)
	y_2=f.subs(x,x_2)
	y_cd=max(y_1,y_2)
	y_ct=min(y_1,y_2)

	m= random.randint (-15,10)

	if y_ct<m and m<y_cd:
		so_nghiem = 3
	if m>y_cd or m< y_ct:
		so_nghiem = 1	
	if m==y_ct or m==y_cd:
		so_nghiem = 2
	kq=f"${{{so_nghiem}}}$"
	if so_nghiem == 1:
		kq2=f"${{{so_nghiem - 1}}}$"
		kq3=f"${{{so_nghiem + 1}}}$"
		kq4=f"${{{so_nghiem + 2}}}$"
	elif so_nghiem == 2:
		kq2=f"${{{so_nghiem - 2}}}$"
		kq3=f"${{{so_nghiem - 1}}}$"
		kq4=f"${{{so_nghiem + 2}}}$"
	else:		
		kq2=f"${{{so_nghiem - 1}}}$"
		kq3=f"${{{so_nghiem - 2}}}$"
		kq4=f"${{{so_nghiem + 1}}}$"
	#Vẽ đồ thị
	code_hinh=my_module.code_dothi_bac_3(a,b,c,d)
	

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)	
	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	dap_an=my_module.tra_ve_dap_an(list_PA)	

	noi_dung = f"Cho hàm số $y=f(x)$ có đồ thị như hình vẽ dưới đây."
	debai= f"{noi_dung}\n\n"\
	f"{file_name}\n"\
	f"Số nghiệm của phương trình $f(x)={m}$ là:\n"\
	
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"Số nghiệm của phương trình $f(x)={m}$ là:\n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
	f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
	f"Số nghiệm của phương trình $f(x)={m}$ là:\n"\
	f"\\shortans[4]{{{kq}}}\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_12]-M2. Tìm số giao điểm của đồ thị với trục Ox, Oy
def prt_34_L12_C1_B4_12():
	x=sp.symbols("x")
	chon=random.randint(1,7)
	
	if chon==1:
		x_1=random.randint(-5,5)
		x_2=x_1+random.randint(1,5)
		a=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		f=a*(x-x_1)**2*(x-x_2)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=2
		kq2=1
		kq3=0
		kq4=3
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Rightarrow x={x_1},x={x_2}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."

	if chon==2:
		x_1=random.randint(-5,5)
		x_2=x_1+random.randint(1,5)
		x_3=x_1+random.randint(1,5)
		a=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		f=a*(x-x_1)*(x-x_2)*(x-x_3)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=3
		kq2=1
		kq3=0
		kq4=2
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Rightarrow x={x_1},x={x_2},x={x_3}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."

	if chon==3:
		x_1=random.randint(-5,5)
		a=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		f=a*(x-x_1)*(x**2+random.randint(1,5))
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=1
		kq2=3
		kq3=0
		kq4=2
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Rightarrow x={x_1}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."

	if chon==4:
		a = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		b = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		c = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		d = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		if a*d-b*c==0:
			d = d+1		

		f=(a*x+b)/(c*x+d)
		noi_dung= f"Cho hàm số $y={latex(f)}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=1
		kq2=3
		kq3=0
		kq4=2
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Rightarrow x={phan_so(-b/a)}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."
	
	if chon==5:
		a = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		b = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		c = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		d = random.choice([random.randint(-3, -1), random.randint(1, 3)])
		if a*d-b*c==0:
			d = d+1		

		f=(a*x+b)/(c*x+d)
		noi_dung= f"Cho hàm số $y={latex(f)}$. Số giao điểm của đồ thị hàm số đã cho với trục tung là"
		kq=1
		kq2=3
		kq3=0
		kq4=2
		noi_dung_loigiai=f"Cho $x=0\\Rightarrow y={phan_so(b/d)}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục tung là ${{{kq}}}$."
	
	if chon==6:
		x_1=random.randint(-5,5)
		x_2=x_1+random.randint(1,5)
		x_3=x_1+random.randint(1,5)
		a=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		f=a*(x-x_1)*(x-x_2)*(x-x_3)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục tung là"
		kq=1
		kq2=3
		kq3=0
		kq4=2
		noi_dung_loigiai=f"Cho $x=0\\Rightarrow y={f.subs(x,0)}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."

	if chon==7:
		x_1=random.randint(-5,5)
		x_2=x_1+random.randint(1,5)
		a=random.choice([random.randint(-4, -1), random.randint(1, 4)])
		f=a*(x-x_1)**2*(x-x_2)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục tung là"
		kq=1
		kq2=2
		kq3=0
		kq4=3
		noi_dung_loigiai=f"Cho $x=0\\Rightarrow y={f.subs(x,0)}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."


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
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

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

#[D12_C1_B4_13]-M2. Cho hàm số đa thức. Tìm số giao điểm với trục Ox, Oy
def prt_34_L12_C1_B4_13():
	x=sp.symbols("x")
	chon=random.randint(1,5)
	if chon==1:
		a=random.choice([random.randint(-3,-1), random.randint(1,3)])
		x_1=random.randint(-5,0)
		x_2=x_1+random.randint(1,3)
		x_3=x_2+random.randint(1,3)
		f=a*(x-x_1)*(x-x_2)*(x-x_3)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=3
		kq2=2
		kq3=0
		kq4=1
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Leftrightarrow x={x_1},x={x_2},x={x_3}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."
	
	if chon==2:
		a=random.choice([random.randint(-3,-1), random.randint(1,3)])
		x_1=random.randint(-5,0)
		x_2=x_1+random.randint(1,3)
		x_3=x_2+random.randint(1,3)
		f=a*(x-x_1)**2*(x-x_2)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=2
		kq2=3
		kq3=0
		kq4=1
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."

	if chon==3:
		a=random.choice([random.randint(-3,-1), random.randint(1,3)])
		x_1=random.choice([random.randint(-5,-1), random.randint(1,5)])
		x_2=x_1+random.randint(1,3)
		x_3=x_2+random.randint(1,3)
		f=a*(x-x_1)**3
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=1
		kq2=3
		kq3=0
		kq4=2
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Leftrightarrow x={x_1}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."

	if chon==4:
		a=random.choice([random.randint(-3,-1), random.randint(1,3)])
		x_1=random.choice([random.randint(1,5)])
		x_2=x_1+random.randint(1,3)		
		f=a*(x**2-x_1)*(x**2-x_2)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=4
		kq2=3
		kq3=random.choice([0,1])
		kq4=2
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Leftrightarrow x^2={x_1}, x^2={x_2}\\Leftrightarrow x=\\pm {latex(sqrt(x_1))},x=\\pm {latex(sqrt(x_2))}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."

	if chon==5:
		a=random.choice([random.randint(-3,-1), random.randint(1,3)])
		x_1=random.choice([random.randint(1,5)])
		x_2=x_1+random.randint(1,3)		
		f=a*(x**2-x_1)*(x**2+x_2)
		noi_dung= f"Cho hàm số $y={latex(expand(f))}$. Số giao điểm của đồ thị hàm số đã cho với trục hoành là"
		kq=2
		kq2=3
		kq3=random.choice([0,1])
		kq4=4
		noi_dung_loigiai=f"Xét phương trình ${latex(expand(f))}=0\\Leftrightarrow x^2={x_1}\\Leftrightarrow  x=\\pm {latex(sqrt(x_1))}$.\n\n"\
		f" Vậy số giao điểm của đồ thị hàm số đã cho với trục hoành là ${{{kq}}}$."


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
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

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
		f"\\shortans[4]{{{kq}}}\n"\
		f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_14]-M2. Cho y=(ax+b)/(cx+d). Tìm tọa độ tâm đối xứng.
def prt_34_L12_C1_B4_14():
	x=sp.symbols("x")
	a=random.choice([i for i in range(-5, 6) if i!=0])
	b=random.randint(-5,5)
	c=random.choice([i for i in range(-5, 6) if i!=0])
	d=random.choice([i for i in range(-5, 5) if i!=0 and i!=-1])
	if a*d-b*c==0: d=d+1
	f=(a*x+b)/(c*x+d)
	x_0,y_0=-d/c,a/c
	y_2=-a/c

	noi_dung=f"Đồ thị hàm số $y={latex((a*x+b)/(c*x+d))}$ nhận điểm nào làm tâm đối xứng trong các điểm sau?"	

	kq=f"$\\left({phan_so(x_0)};{phan_so(y_0)}\\right)$"
	kq2=f"$\\left({phan_so(x_0)};{phan_so(y_2)}\\right)$"
	kq3=f"$\\left({phan_so(-x_0)};{phan_so(y_0)}\\right)$"
	kq4=f"$\\left({phan_so(-x_0)};{phan_so(y_2)}\\right)$"

	noi_dung_loigiai=(
		f"Đồ thị hàm số có tiệm cận ngang là đường thẳng $y={phan_so(a/c)}$"
		f" và có tiệm cận đứng là đường thẳng $x={phan_so(x_0)}$.\n\n"
		f"Đồ thị hàm số đã cho nhận điểm {kq} làm tâm đối xứng.\n"
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_15]-M2. Cho y=(ax^2+bx+c)/(dx+e). Tìm tọa độ tâm đối xứng.
def prt_34_L12_C1_B4_15():
	x=sp.symbols("x")
	d=random.choice([i for i in range(-5, 5) if i!=0])
	a=d*random.choice([i for i in range(-2, 3) if i!=0])
	b=random.randint(-5,5)
	c=random.choice([i for i in range(-5, 6)])
	
	e=random.choice([i for i in range(-5, 5) if i!=0])
	f_tu=a*x**2+b*x+c
	f_mau=d*x+e
	quotient, remainder = sp.div(f_tu, f_mau)
	while remainder==0:
		a=random.choice([i for i in range(-5, 6) if i!=0])
		b=random.randint(-5,5)
		c=random.choice([i for i in range(-5, 6)])
		d=random.choice([i for i in range(-5, 5) if i!=0])
		e=random.choice([i for i in range(-5, 5) if i!=0])
		quotient, remainder = sp.div(f_tu, f_mau)
	
	f=f_tu/f_mau
	x_0=-e/d
	y_0= quotient.subs(x,x_0)
	x_2=int(x_0)+random.randint(1,3)
	y_2=quotient.subs(x,x_2)
	x_3=int(x_0)-random.randint(1,3)
	y_4=f.subs(x,-x_0)


	noi_dung=f"Đồ thị hàm số $y={latex(f)}$ nhận điểm nào làm tâm đối xứng trong các điểm sau?"	

	kq=f"$\\left({phan_so(x_0)};{phan_so(y_0)}\\right)$"
	kq2=f"$\\left({phan_so(x_0)};{phan_so(y_2)}\\right)$"
	kq3=f"$\\left({phan_so(x_3)};{phan_so(y_0)}\\right)$"
	kq4=f"$\\left({phan_so(-x_0)};{phan_so(y_4)}\\right)$"

	noi_dung_loigiai=(
		f"$y={latex(f)}={latex(quotient+remainder/(d*x+e))}$.\n\n"
		f"Đồ thị hàm số có tiệm cận đứng là đường thẳng $x={phan_so(-e/d)}$.\n\n"
		f" Đồ thị hàm số có tiệm cận xiên là đường thẳng $y={latex(quotient)}$.\n\n"
		f"Đồ thị hàm số đã cho nhận điểm {kq} làm tâm đối xứng.\n"
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_16]-M2. Cho y=ax^3+bx^2+cx+d. Tìm tọa độ tâm đối xứng.
def prt_34_L12_C1_B4_16():
	x=sp.symbols("x")	
	a=random.choice([i for i in range(-3, 4) if i!=0])
	b=random.choice([i for i in range(-4, 4) if i!=0])
	c=random.choice([i for i in range(-5, 5)])	
	d=random.randint(-6,6)
	f=a*x**3+b*x**2+c*x+d
	f_dh1=diff(f,x)
	f_dh2=diff(f_dh1,x)
	x_0=-b/(3*a)
	y_0=f.subs(x,x_0)

	x_2=-b/(2*a)
	y_2=f.subs(x,x_2)

	x_3=-b/a
	y_3=f.subs(x,x_3)

	noi_dung=f"Đồ thị hàm số $y={latex(f)}$ nhận điểm nào làm tâm đối xứng trong các điểm sau?"	

	kq=f"$\\left({phan_so(x_0)};{phan_so(y_0)}\\right)$"
	kq2=f"$\\left(0;{d}\\right)$"
	kq3=f"$\\left({phan_so(x_3)};{phan_so(y_3)}\\right)$"
	kq4=f"$\\left({phan_so(x_2)};{phan_so(y_2)}\\right)$"

	noi_dung_loigiai=(
		f"$y'={latex(f_dh1)}$.\n\n"
		f"$y''={latex(f_dh2)}$.\n\n"
		f"$y''=0\\Rightarrow {latex(f_dh2)}=0\\Rightarrow x={phan_so(x_0)}$.\n\n"
		f"$f\\left({phan_so(x_0)}\\right)={phan_so(y_0)}$.\n\n"
		f"Đồ thị hàm số đã cho nhận điểm {kq} làm tâm đối xứng.\n"
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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C1_B4_17]-TL-M3. Cho đồ thị hàm bậc 3. Tính tổng các hệ số
def prt_34_L12_C1_B4_17():
	x = sp.symbols('x')
	x1=random.randint(-2,0)
	x2=random.randint(0,2)
	x3=random.randint(1,2)
	k=random.choice([1,-1])	
	f=k*x**3 - k*x**2*x1 - k*x**2*x2 - k*x**2*x3 + k*x*x1*x2 + k*x*x1*x3 + k*x*x2*x3 - k*x1*x2*x3
	a=f.coeff(x,3)
	b=f.coeff(x,2)
	c=f.coeff(x,1)
	d=f.as_coefficients_dict()[1]
	a1,b1,c1,d1=a,b,c,d	

	#Vẽ đồ thị
	code_hinh=my_module.code_dothi_bac_3(a,b,c,d)	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	
	kq=f"$y={latex(f)}$"

	m=random.choice([i for i in range(-4, 4) if i!=0])
	n=random.choice([i for i in range(-3, 3) if i!=0])
	p=random.choice([i for i in range(-2, 2) if i!=0])	

	a,b,c,d=sp.symbols("a b c d")
	chon=random.randint(1,3)
	chon=1
	if chon==1:
		noi_dung = f"Hàm số $y=ax^3+{latex(b1*x**2)}+cx+d$ có đồ thị như hình vẽ bên. Tính ${latex(m*a+n*c+d)}$.".replace("+-","-")
		dap_an=m*a1+n*c1+d1

		noi_dung_loigiai=(
			f"Đồ thị hàm số đi qua các điểm $A({x1};0), B({x2};0), C({x3};0)$.\n\n"
			f"Đồ thị hàm số cắt trục tung tại điểm $(0;{d1})\\Rightarrow d={d1}$.\n\n"
				f"Từ các giả thiết ta tìm được: $a={a1},b={b1},c={c1},d={d1}$.\n\n"
				f"Hàm số là $y={latex(expand(f))}$.\n\n"		
			f"Do đó: ${latex(m*a+n*c+d)}={dap_an}$.\n\n"
			f"Đáp án:{dap_an}"
			)
	
	if chon==2:
		noi_dung = f"Hàm số $y={latex(a1*x**3)}+bx^2+cx+d$ có đồ thị như hình vẽ bên. Tính ${latex(m*b+n*c+d)}$.".replace("+-","-")
		dap_an=m*b1+n*c1+d1

		noi_dung_loigiai=(
			f"Đồ thị hàm số đi qua các điểm $A({x1};0), B({x2};0), C({x3};0)$.\n\n"
			f"Đồ thị hàm số cắt trục tung tại điểm $(0;{d1})\\Rightarrow d={d1}$.\n\n"
				f"Từ các giả thiết ta tìm được: $a={a1},b={b1},c={c1},d={d1}$.\n\n"
				f"Hàm số là $y={latex(expand(f))}$.\n\n"		
			f"Do đó: ${latex(m*b+n*c+d)}={dap_an}$.\n\n"
			f"Đáp án:{dap_an}"
			)

	if chon==3:
		noi_dung = f"Hàm số $y=ax^3+bx^2+{latex(c1*x)}+d$ có đồ thị như hình vẽ bên. Tính ${latex(m*a+n*b+d)}$.".replace("+-","-")
		dap_an=m*a1+n*b1+d1

		noi_dung_loigiai=(
			f"Đồ thị hàm số đi qua các điểm $A({x1};0), B({x2};0), C({x3};0)$.\n\n"
			f"Đồ thị hàm số cắt trục tung tại điểm $(0;{d1})\\Rightarrow d={d1}$.\n\n"
				f"Từ các giả thiết ta tìm được: $a={a1},b={b1},c={c1},d={d1}$.\n\n"
				f"Hàm số là $y={latex(expand(f))}$.\n\n"		
			f"Do đó: ${latex(m*a+n*b+d)}={dap_an}$.\n\n"
			f"Đáp án:{dap_an}"
			)
	
	
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B4_18]-TL-M3. Cho đồ thị hàm y=(ax+b)/(cx+d). Tính tổng các hệ số
def prt_34_L12_C1_B4_18():
	x = sp.symbols('x')
	a = random.choice([i for i in range(-3, 3) if i!=0])
	b = random.choice([a,-a,2*a,-2*a,3*a])
	c = random.choice([i for i in range(-2, 2) if i!=0])
	d = random.choice([c,-c,2*c,-2*c,3*c])	

	if a*d-b*c==0: 
		b = b+1
	f=(a*x+b)/(c*x+d)
	x_0, y_0=-d/c, a/c
	x_Ox,y_Oy=-b/a,b/d
	a1,b1,c1,d1=a,b,c,d
	
	#Vẽ đồ thị
	code_hinh=my_module.code_dothi_phanthuc_bac1(a,b,c,d)	
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	

	m=random.choice([i for i in range(-4, 4) if i!=0])
	n=random.choice([i for i in range(-3, 3) if i!=0])
	p=random.choice([i for i in range(-2, 2) if i!=0])
	
	a,b,c,d=sp.symbols("a b c d")

	chon=random.randint(1,3)
	if chon==1:
		dap_an=m*a1+n*c1+p*d1
		ham=f"$y=\\dfrac{{ax+{b1}}}{{cx+d}}$"
		noi_dung = (
		f"Hàm số {ham} có đồ thị như hình vẽ bên. Tính ${latex(m*a+n*c+p*d)}$.".replace("+-","-")
		)
		noi_dung_loigiai=(
			f"Đồ thị hàm số có tiệm cận đứng $x=-\\dfrac{{d}}{{c}}={phan_so(x_0)}$.\n\n"
			f"Đồ thị hàm số có tiệm cận ngang $y=\\dfrac{{a}}{{c}}={phan_so(y_0)}$.\n\n"
			f"Đồ thị hàm số đi qua các điểm $A(0;{phan_so(y_Oy)}), B({phan_so(x_Ox)};0)$.\n\n"
			f"Từ các giả thiết ta tìm được: $a={a1},b={b1},c={c1},d={d1}$.\n\n"
			f"Hàm số là: $y=\\dfrac{{{latex(a1*x)}+{b1}}}{{{latex(c1*x)}+{d1}}}$.\n\n"
			f"${latex(m*a+n*c+p*d)}={dap_an}$.\n\n"
			f"Đáp án: {dap_an}")			
	
	if chon==2:
		dap_an=m*b1+n*c1+p*d1
		ham=f"$y=\\dfrac{{{latex(a1*x)}+b}}{{cx+d}}$"
		noi_dung = (
		f"Hàm số {ham} có đồ thị như hình vẽ bên. Tính ${latex(m*b+n*c+p*d)}$.".replace("+-","-")
		)
		noi_dung_loigiai=(
			f"Đồ thị hàm số có tiệm cận đứng $x=-\\dfrac{{d}}{{c}}={phan_so(x_0)}$.\n\n"
			f"Đồ thị hàm số có tiệm cận ngang $y=\\dfrac{{a}}{{c}}={phan_so(y_0)}$.\n\n"
			f"Đồ thị hàm số đi qua các điểm $A(0;{phan_so(y_Oy)}), B({phan_so(x_Ox)};0)$.\n\n"
			f"Từ các giả thiết ta tìm được: $a={a1},b={b1},c={c1},d={d1}$.\n\n"
			f"Hàm số là: $y=\\dfrac{{{latex(a1*x)}+{b1}}}{{{latex(c1*x)}+{d1}}}$.\n\n"
			f"${latex(m*b+n*c+p*d)}={dap_an}$.\n\n"
			f"Đáp án: {dap_an}")

	if chon==3:
		dap_an=m*a1+n*b1+p*d1
		ham=f"$y=\\dfrac{{ax+b}}{{{latex(c1*x)}+d}}$"
		noi_dung = (
		f"Hàm số {ham} có đồ thị như hình vẽ bên. Tính ${latex(m*a+n*b+p*d)}$.".replace("+-","-")
		)
		noi_dung_loigiai=(
			f"Đồ thị hàm số có tiệm cận đứng $x=-\\dfrac{{d}}{{c}}={phan_so(x_0)}$.\n\n"
			f"Đồ thị hàm số có tiệm cận ngang $y=\\dfrac{{a}}{{c}}={phan_so(y_0)}$.\n\n"
			f"Đồ thị hàm số đi qua các điểm $A(0;{phan_so(y_Oy)}), B({phan_so(x_Ox)};0)$.\n\n"
			f"Từ các giả thiết ta tìm được: $a={a1},b={b1},c={c1},d={d1}$.\n\n"
			f"Hàm số là: $y=\\dfrac{{{latex(a1*x)}+{b1}}}{{{latex(c1*x)}+{d1}}}$.\n\n"
			f"${latex(m*a+n*b+p*d)}={dap_an}$.\n\n"
			f"Đáp án: {dap_an}")

	noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")	
	
		
	debai_word= f"{noi_dung}\n{file_name}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B4_19]-TF-M2. Cho hàm số y=(ax^2+bx+c)/(dx+e). Xét Đ-S: TXĐ, y', TCĐ, Tâm đối xứng
def prt_34_L12_C1_B4_19():
	x=sp.symbols("x")
	d = random.choice([random.randint(1,4),random.randint(-3,-1) ])
	a = random.randint(1,2)*d
	if d not in [-1,1]: a=2*d
	b = random.randint(-5, 5)
	c = random.choice([i for i in range(-6, 6) if i!=0])    
	e = random.choice([i for i in range(-6, 6) if i!=0])
	
	g, h = div(a * x**2 + b * x + c, d * x + e, x)
	if h==0:
		c=c+random.randint(1,2)
	f=(a*x**2+b*x+c)/(d*x+e)
	g, h = div(a * x**2 + b * x + c, d * x + e, x)
	x_0=-e/d
	y_0=g.subs(x,x_0)


	noi_dung = f"Cho hàm số $y={latex(f)}$ . Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"* Tập xác định của hàm số là $D=\\mathbb{{R}} \\backslash \\left\\{{{phan_so(-e/d)}\\right\\}}$" 
	kq1_F=f"Tập xác định của hàm số là $D=\\mathbb{{R}}\\backslash \\left\\{{{phan_so(e/d)}\\right\\}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=(f"Hàm số xác định khi ${latex(d*x+e)}\\ne 0 \\Leftrightarrow x \\ne {phan_so(-e/d)}$.\n"
		f"Tập xác định là: $D=\\mathbb{{R}}\\backslash \\left\\{{{phan_so(-e/d)}\\right\\}}$.")
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	f_dh=(a*d*x**2+2*a*e*x+b*e-c*d)/(d*x+e)**2
	f_dh_false=(a*d*x**2-2*a*e*x+b*e+c*d+random.randint(1,2))/(d*x+e)**2

	kq2_T=f"* Đạo hàm của hàm số là $y'={latex(f_dh)}$"
	kq2_F=f"Đạo hàm của hàm số là $y'={latex(f_dh_false)}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Đạo hàm của hàm số là $y'={latex(f_dh)}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(-e/d)}$"
	kq3_F=random.choice([
		f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(e/d)}$",
		f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $y={phan_so(-e/d)}$",
		f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(a/d)}$"])	
	kq3=random.choice([kq3_T, kq3_F])

	HDG=f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(-e/d)}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"* Đồ thị hàm số có tâm đối xứng là điểm $I\\left({phan_so(x_0)};{phan_so(y_0)}\\right)$"
	kq4_F=f"Đồ thị hàm số có tâm đối xứng là điểm $I\\left({phan_so(e/d)};{phan_so(y_0)}\\right)$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"Tiệm cận đứng của đồ thị hàm số là đường thẳng $x={phan_so(-e/d)}$.\n\n"
		f"$y={latex(f)}={latex(g)}+\\dfrac{{{latex(h)}}}{{{latex(d*x+e)}}}$.\n\n"
		f"Tiệm cận xiên của đồ thị hàm số là đường thẳng $y={latex(g)}$.\n\n"
		f"Tâm đối xứng của đồ thị là giao điểm của hai tiệm cận: $I\\left({phan_so(x_0)};{phan_so(y_0)}\\right)$."
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
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an
	



#----------------------------BÀI 5 - TOÁN THỰC TẾ---------------------------------------#

#[D12_C1_B5_01]-TL-M4. Bài toán thực tế tìm chi phí thấp nhất
def prt_34_L12_C1_B5_01():
	a=random.randint(1,7)
	b=random.randint(1,10)/10
	st_b=f"{round(b,1):.1f}".replace(".",",")

	c=random.randint(1,7)/1000
	st_c=f"{round(c,3):.3f}".replace(".",",")

	x_max=int(sqrt(a/c)+random.randint(10,20))
	x=sp.symbols("x")
	f=(a+b*x+c*x**2)/x
	x_min=sqrt(a/c)
	y_min=f.subs(x,x_min)
	st_xmin=f"{round(x_min,0):.1f}".replace(".",",")
	st_ymin=f"{round(y_min,2):.2f}".replace(".",",")

	code_hinh=f" \\begin{{tikzpicture}}\n\
\\tkzTabInit[espcl=2.5,lgt=1.5,nocadre=false]\n\
{{$x$/1.2,$y'$/0.7,$y$/2.1}}\n\
{{$0$,$\\sqrt{{{phan_so(a/c)}}}$,$+\\infty$}}\n\
\\tkzTabLine{{d,-,0,+}}\n\
\\tkzTabVar{{+D+/$ $/$+\\infty$,-/${f"{round(y_min,2):.2f}"}$,+/$+\\infty$}}\n\
\\end{{tikzpicture}} " 


	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	noi_dung = (
	f" Tại một xí nghiệp chuyên sản xuất vật liệu xây dựng, nếu trong một ngày xí nghiệp sản xuất $x (m^3)$"
	f" sản phẩm thì phải bỏ ra các khoản chi phí bao gồm:"
	f" {a} triệu đồng chi phí cố định; {st_b} triệu đồng chi phí cho mỗi mét khối sản phẩm"
	f" và ${st_c}x^2$ triệu đồng chi phí bảo dưỡng máy móc."
	f" Biết rằng, mỗi ngày xí nghiệp sản xuất được tối đa {x_max} $m^3$ sản phẩm."
	f"  Tìm chi phí trung bình (triệu đồng) trên mỗi mét sản phẩm thấp nhất mà xí nghiệp cần bỏ ra"
	f" (làm tròn đến hàng phần trăm)."
	)

	noi_dung_loigiai=(
		f" Đáp án: {st_ymin}.\n\n"
		f" Tổng chi phí (triệu đồng) để xí nghiệp sản xuất $x (m^3)$ sản phẩm trong một ngày là:\n\n"
		f"$C(x)={a}+{st_b}x+{st_c}x^2$ với $0\\le x \\le {x_max}$.\n\n"
		f" Chi phí trung bình (triệu đồng) trên mỗi mét khối sản phẩm là:\n\n"
		f" $\\overline C(x)=\\dfrac{{C(x)}}{{x}}=\\dfrac{{{a}+{st_b}x+{st_c}x^2}}{{x}}$"
		f" $=\\dfrac{{{a}}}{{x}} + {st_b} + {st_c}x$.\n\n"
		f" $\\overline C'(x)=-\\dfrac{{{a}}}{{x^2}}+{st_c}=\\dfrac{{{st_c}x^2-{a}}}{{x^2}}$.\n\n"
		f" $\\overline C'(x)=0 \\Rightarrow x^2={phan_so(a/c)} \\Rightarrow x=\\sqrt{{{phan_so(a/c)}}}$.\n\n"
		f" Bảng biến thiên:\n {file_name}\n"		
		f" Từ bảng biến thiên ta thấy chi phí trung bình thấp nhất là:\n\n"
		f" $\\overline C(\\sqrt{{{phan_so(a/c)}}})\\approx {st_ymin}"
		f" $ đạt được khi $x=\\sqrt{{{phan_so(a/c)}}} \\approx {st_xmin}$."
		)

	noi_dung_loigiai_latex=(
		f" Đáp án:{st_ymin}.\n\n"
		f" Tổng chi phí (triệu đồng) để xí nghiệp sản xuất $x (m^3)$ sản phẩm trong một ngày là:\n\n"
		f"$C(x)={a}+{st_b}x+{st_c}x^2$ với $0\\le x \\le {x_max}$.\n\n"
		f" Chi phí trung bình (triệu đồng) trên mỗi mét khối sản phẩm là:\n\n"
		f" $\\overline C(x)=\\dfrac{{C(x)}}{{x}}=\\dfrac{{{a}+{st_b}x+{st_c}x^2}}{{x}}$"
		f" $=\\dfrac{{{a}}}{{x}} + {st_b} + {st_c}x$.\n\n"
		f" $\\overline C'(x)=-\\dfrac{{{a}}}{{x^2}}+{st_c}=\\dfrac{{{st_c}x^2-{a}}}{{x^2}}$.\n\n"
		f" $\\overline C'(x)=0 \\Rightarrow x^2={phan_so(a/c)} \\Rightarrow x=\\sqrt{{{phan_so(a/c)}}}$.\n\n"
		f" Bảng biến thiên:\n\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"	
		f" Từ bảng biến thiên ta thấy chi phí trung bình thấp nhất là:\n\n"
		f" $\\overline C(\\sqrt{{{phan_so(a/c)}}})\\approx {st_ymin}"
		f" $ đạt được khi $x=\\sqrt{{{phan_so(a/c)}}} \\approx {st_xmin}$."

		)
	dap_an=st_ymin
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B5_02]-TL-M3. Cho hàm số chi phí. Tìm chi phí trung bình thấp nhất.
def prt_34_L12_C1_B5_02():
	a=random.randint(1,7)
	b=random.randint(1,10)/10
	st_b=f"{round(b,1):.1f}".replace(".",",")

	c=random.randint(1,7)/1000
	st_c=f"{round(c,3):.3f}".replace(".",",")

	x_max=int(sqrt(a/c)+random.randint(10,20))
	x=sp.symbols("x")
	f=(a+b*x+c*x**2)/x
	x_min=sqrt(a/c)
	y_min=f.subs(x,x_min)
	st_xmin=f"{round(x_min,1):.1f}".replace(".",",")
	st_ymin=f"{round(y_min,1):.1f}".replace(".",",")

	# x_1,x_2,x_3=int(x_min)-1,int(x_min),int(x_min)+1
	# y_1,y_2,y_3=f.subs(x,x_1),f.subs(x,x_2), f.subs(x,x_3)


	code_hinh=f" \\begin{{tikzpicture}}\n\
\\tkzTabInit[espcl=2.5,lgt=1.5,nocadre=false]\n\
{{$x$/1.2,$y'$/0.7,$y$/2.1}}\n\
{{$0$,$\\sqrt{{{phan_so(a/c)}}}$,$+\\infty$}}\n\
\\tkzTabLine{{d,-,0,+}}\n\
\\tkzTabVar{{+D+/$ $/$+\\infty$,-/${f"{round(y_min,2):.2f}"}$,+/$+\\infty$}}\n\
\\end{{tikzpicture}} " 


	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""
	noi_dung = (
	f" Tại một xưởng sản xuất sản phẩm từ {random.choice(["gỗ", "đá", "bêtông", "cát"])}, chi phí để sản xuất ${{x}} (m^3)$ sản phẩm mỗi tháng là"
	f" $C(x)={a}+{st_b}x+{st_c}x^2$ (triệu đồng) với $0\\le x \\le {x_max}$. Chi phí trung bình là $\\overline{{C}}(x)=\\dfrac{{C(x)}}{{x}}$."
	f" Mỗi tháng xưởng sản xuất bao nhiêu mét khối sản phẩm thì chi phí trung bình để sản xuất là thấp nhất"
	f"(làm tròn đến hàng phần mười)"
	)

	noi_dung_loigiai=(
		f" Đáp án: {st_xmin}.\n\n"
		f" Chi phí trung bình (triệu đồng) trên mỗi mét khối sản phẩm là:\n\n"
		f" $\\overline C(x)=\\dfrac{{C(x)}}{{x}}=\\dfrac{{{a}+{st_b}x+{st_c}x^2}}{{x}}$"
		f" $=\\dfrac{{{a}}}{{x}} + {st_b} + {st_c}x$.\n\n"
		f" $\\overline C'(x)=-\\dfrac{{{a}}}{{x^2}}+{st_c}=\\dfrac{{{st_c}x^2-{a}}}{{x^2}}$.\n\n"
		f" $\\overline C'(x)=0 \\Rightarrow x^2={phan_so(a/c)} \\Rightarrow x=\\sqrt{{{phan_so(a/c)}}}$.\n\n"
		f" Bảng biến thiên:\n {file_name}\n"		
		f" Từ bảng biến thiên ta thấy chi phí trung bình thấp nhất là:\n\n"
		f" $\\overline C(\\sqrt{{{phan_so(a/c)}}})\\approx {st_ymin}"
		f" $ đạt được khi $x=\\sqrt{{{phan_so(a/c)}}} \\approx {st_xmin}$."
		)

	noi_dung_loigiai_latex=(
		f" Đáp án:{st_xmin}.\n\n"
		f" Chi phí trung bình (triệu đồng) trên mỗi mét khối sản phẩm là:\n\n"
		f" $\\overline C(x)=\\dfrac{{C(x)}}{{x}}=\\dfrac{{{a}+{st_b}x+{st_c}x^2}}{{x}}$"
		f" $=\\dfrac{{{a}}}{{x}} + {st_b} + {st_c}x$.\n\n"
		f" $\\overline C'(x)=-\\dfrac{{{a}}}{{x^2}}+{st_c}=\\dfrac{{{st_c}x^2-{a}}}{{x^2}}$.\n\n"
		f" $\\overline C'(x)=0 \\Rightarrow x^2={phan_so(a/c)} \\Rightarrow x=\\sqrt{{{phan_so(a/c)}}}$.\n\n"
		f" Bảng biến thiên:\n\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"	
		f" Từ bảng biến thiên ta thấy chi phí trung bình thấp nhất là:\n\n"
		f" $\\overline C(\\sqrt{{{phan_so(a/c)}}})\\approx {st_ymin}"
		f" $ đạt được khi $x=\\sqrt{{{phan_so(a/c)}}} \\approx {st_xmin}$."

		)
	dap_an=st_xmin
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B5_03]-TL-M3. Bài toán tìm số giếng dầu có thể khai thác thêm để sản lượng là lớn nhất
def prt_34_L12_C1_B5_03():
	x=sp.symbols("x")
	so_bandau=random.randint(8,15)
	so_sanpham=random.randint(130,160)
	so_giam=random.randint(4,8)	
	f=(so_bandau+x)*(so_sanpham-so_giam*x)
	f_dh=diff(f,x)
	equation=Eq(f_dh,0)
	solution=solve(equation,x)
	x_0=solution[0]

	while x_0<0:
		so_bandau=random.randint(8,20)
		so_sanpham=random.randint(80,150)
		so_giam=random.randint(5,10)	
		f=(so_bandau+x)*(so_sanpham-so_giam*x)
		f_dh=diff(f,x)
		equation=Eq(f_dh,0)
		solution=solve(equation,x)
		x_0=solution[0]

	y_0=f.subs(x,x_0)

	code_hinh=f" \\begin{{tikzpicture}}\n\
\\tkzTabInit[espcl=2.5,lgt=1.5,nocadre=false]\n\
{{$x$/1.2,$y'$/0.7,$y$/2.1}}\n\
{{$0$,${phan_so(x_0)}$,$+\\infty$}}\n\
\\tkzTabLine{{,+,0,-}}\n\
\\tkzTabVar{{-/,+/${f"{phan_so(y_0)}"}$,-/}}\n\
\\end{{tikzpicture}} " 

	code = my_module.moi_truong_anh_latex(code_hinh)
	#file_name=my_module.pdftoimage_timename(code)
	file_name=""

	noi_dung = (
	f"Một công ty tiến hành khai thác {so_bandau} giếng dầu trong khu vực được chỉ định."
	f" Trung bình mỗi giếng dầu chiết xuất được {so_sanpham} thùng dầu mỗi ngày."
	f" Công ty có thể khai thác nhiều hơn {so_bandau} giếng dầu nhưng cứ khai thác thêm một giếng" 
	f" thì lượng dầu mỗi giếng chiết xuất được hằng ngày sẽ giảm {so_giam} thùng."
	f" Để công ty có thể quyết định số giếng cần thêm cho phù hợp với tài chính, hãy chỉ ra số giếng công ty có thể khai thác thêm để sản lượng dầu chiết xuất đạt lớn nhất."
	)

	noi_dung_loigiai=(
	f"Gọi ${{x}}$ là số giếng dầu khai thác thêm.\n\n"
	f"Sản lượng dầu khi khai thác thêm ${{x}}$ giếng là: $({so_bandau}+x)({so_sanpham}-{so_giam}x)$ (thùng).\n\n"
	f"Xét hàm số $f(x)=({so_bandau}+x)({so_sanpham}-{so_giam}x)={latex(expand(f))}$ mô tả sản lượng thùng dầu.\n\n"
	f"Ta có: $f'(x)=0\\Leftrightarrow {latex(f_dh)}=0 \\Leftrightarrow x={phan_so(x_0)}$.\n\n"
	f"Bảng biến thiên:\n{file_name}\n"	
	)

	noi_dung_loigiai_latex=(
	f"Gọi ${{x}}$ là số giếng dầu khai thác thêm.\n\n"
	f"Sản lượng dầu khi khai thác thêm ${{x}}$ giếng là: $({so_bandau}+x)({so_sanpham}-{so_giam}x)$ (thùng).\n\n"
	f"Xét hàm số $f(x)=({so_bandau}+x)({so_sanpham}-{so_giam}x)={latex(expand(f))}$ mô tả sản lượng thùng dầu.\n\n"
	f"Ta có: $f'(x)=0\\Leftrightarrow {latex(f_dh)}=0 \\Leftrightarrow x={phan_so(x_0)}$.\n\n"
	f"Bảng biến thiên:\n\n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"	
	)
	if int(x_0)==x_0:
		dap_an=int(x_0)
		noi_dung_loigiai+=(f"Dựa vào bảng biến thiên, để sản lượng dầu chiết suất đạt cực đại, công ty có thể khai thác thêm {dap_an} giếng dầu.\n\n"
			f"Đáp án: {dap_an}")
		noi_dung_loigiai_latex+=(f"Dựa vào bảng biến thiên, để sản lượng dầu chiết suất đạt cực đại, công ty có thể khai thác thêm {dap_an} giếng dầu.\n\n"
			f"Đáp án: {dap_an}")
	else:
		x_1,x_2 = math.floor(x_0), math.ceil(x_0)
		y_1,y_2=f.subs(x,x_1), f.subs(x,x_2)
		if y_1>y_2:
			dap_an=x_1
			HDG=(f"Ta có: ${x_1}<{phan_so(x_0)}<{x_2}$ và $f({x_1})={y_1}>f({x_2})={y_2}$.\n\n"
			f"Do đó công ty có thể khai thác thêm {dap_an} giếng dầu.\n\n"
			f"Đáp án: {dap_an}")
			noi_dung_loigiai+=HDG
			noi_dung_loigiai_latex+=HDG
		else:
			dap_an=x_2
			HDG=(f"Ta có: ${x_1}<{phan_so(x_0)}<{x_2}$ và $f({x_1})={y_1}<f({x_2})={y_2}$.\n\n"
			f"Do đó công ty có thể khai thác thêm {dap_an} giếng dầu.\n\n"
			f"Đáp án: {dap_an}")
			noi_dung_loigiai+=HDG
			noi_dung_loigiai_latex+=HDG
	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B5_04]-TL-M3. Bài toán tìm tốc độ trung bình để chi phí xăng nhỏ nhất.
def prt_34_L12_C1_B5_04():
	chon=random.randint(1,2)
	if chon==1:
		m=random.randint(2,5)
		n=m+random.randint(1,3)
		k=m/n	
	if chon==2:
		m=random.choice([2,4,6,8])
		n=m+random.choice([2,4])
		k=m/n	
	
	a=random.randint(40,80)
	v=sp.symbols("v")
	f=k*v+m*a**2/(n*v)
	i=random.randint(10,15)
	v_max=10*i
	f_min=f.subs(v,a)
	f_max=f.subs(v,v_max)

	code_hinh=f" \\begin{{tikzpicture}}\n\
\\tkzTabInit[espcl=2.5,lgt=1.5,nocadre=false]\n\
{{$x$/1.2,$C(x)'$/0.7,$C(x)$/2.5}}\n\
{{$0$,${a}$,${v_max}$}}\n\
\\tkzTabLine{{d,-,0,+}}\n\
\\tkzTabVar{{+D+/$ $/$+\\infty$,-/${f"{phan_so(f_min)}"}$,+/${phan_so(f_max)}$}}\n\
\\end{{tikzpicture}} " 

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)
	#file_name=""

	noi_dung = (
	f"Giả sử chi phí tiền xăng ${{C}}$ (ngàn đồng) phụ thuộc vào tốc độ trung bình $v(km/h)$, được tính theo công thức\n\n"
	f" $C(v)={latex(m*v/n)}+{latex(m*a**2/(n*v))},0\\le v \\le {v_max}$.\n\n"
	f" Tài xế xe tải lái xe với tốc độ trung bình (đơn vị: km/h) là bao nhiêu để tiết kiệm tiền xăng nhất?"
	)

	noi_dung_loigiai=(
	f"$C'(v)={phan_so(m/n)}-{latex(m*a**2/(n*v**2))}={latex((m*v**2-m*a**2)/(n*v**2))}$.\n\n"
	f"$C'(v)=0 \\Leftrightarrow {latex((m*v**2-m*a**2))}=0 \\Leftrightarrow v={a}$ hoặc $v={-a}$ (loại).\n\n"
	f"Bảng biến thiên\n{file_name}\n"
	f"Như vậy để chi phí tiền xăng là thấp nhất thì tốc độ trung bình là $v={a} (km/h)$.\n\n"
	f"Đáp án: {a}"
	)
	noi_dung_loigiai_latex=(
	f"$C'(v)={phan_so(m/n)}-{latex(m*a**2/(n*v**2))}={latex((m*v**2-m*a**2)/(n*v**2))}$.\n\n"
	f"$C'(v)=0 \\Leftrightarrow {latex((m*v**2-m*a**2))}=0 \\Leftrightarrow v={a}$ hoặc $v={-a}$ (loại).\n\n"
	f"Bảng biến thiên\n\n"
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
	f"Như vậy để chi phí tiền xăng là thấp nhất thì tốc độ trung bình là $v={a} (km/h)$.\n\n"
	f"Đáp án: {a}"
	)
	dap_an=a
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B5_05]-TF-M3. Cho chuyển động theo hàm bậc 2. Xét Đ-S: vận tốc, gia tốc, vận tốc tăng giảm, min-max
def prt_34_L12_C1_B5_05():
    x=sp.symbols("x")
    t=sp.symbols("t")      
    k=random.randint(2,3)
    k=2
    if k==2:
        a = random.randint(1, 10)
        c = random.randint(1, 10)    
        b=  random.randint(-8, -1) 
        f=a*t**2+b*t+c     
        ham_so =f"{latex(f)}"   

    if k==3:
        a = random.randint(1, 5)
        b = random.randint(0, 5)    
        c =  random.randint(-1, 5)
        d =  random.randint(1, 8)        
        if 3<=a<=5:
            c = random.randint(-3, -1)
            d=  random.randint(3, 8)

        f=a*t**3+b*t**2+c*t+d   
        ham_so =f"{latex(f)}"

    g1=diff(f,t)
    g2=diff(g1,t)
    

    noi_dung=f"Một vật chuyển động thẳng không đều xác định bởi phương trình $s(t)={ham_so}$, "\
        f"trong đó ${{s}}$ tính bằng mét và ${{t}}$ tính bằng giây. Xét tính đúng sai của các khẳng định sau"
        
    
    t_0=random.randint(1,10)
    v_0=g1.subs(t,t_0)
    kq1_T=f"*Vận tốc chuyển động của vật tại thời điểm $t={t_0}$ là ${{{v_0}}}$ m/s"
    kq1_F=f"Vận tốc chuyển động của vật tại thời điểm $t={t_0}$ là ${{{v_0+random.randint(1,6)}}}$ m/s"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
    f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$\n\n"\
    f"$v({t_0})={v_0}$ m/s."

    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n"\
    f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$\n\n"\
    f"$v({t_0})={v_0}$ m/s."

    t_1=random.randint(1,10)
    a_1=g2.subs(t,t_1)

    kq2_T=f"*Gia tốc chuyển động của vật tại thời điểm $t={t_1}$ là ${{{a_1}}}$ m/$s^2$"
    kq2_F=f"Gia tốc chuyển động của vật tại thời điểm $t={t_1}$ là ${{{a_1+random.randint(1,6)}}}$ m/$s^2$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là đúng.\n\n"\
    f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$\n\n"\
    f"$a(t)=\\left({latex(g1)}\\right)'={latex(g2)}$.\n\n"\
    f"$a({t_1})={a_1}$ m/$s^2$."
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là sai.\n\n"\
    f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$\n\n"\
    f"$a(t)=\\left({latex(g1)}\\right)'={latex(g2)}$.\n\n"\
    f"$a({t_1})={a_1}$ m/$s^2$."

    t_3=random.randint(1,20)
    s_3=f.subs(t,t_3)
    kq3_T=f"*Quãng đường vật đi được sau ${{{t_3}}}$ giây kể từ khi bắt đầu chuyển động là ${{{s_3}}}$  m."
    kq3_F=f"Quãng đường vật đi được sau ${{{t_3}}}$ giây kể từ khi bắt đầu chuyển động là ${{{s_3+random.randint(1,6)}}}$  m."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là đúng.\n\n"\
    f"$s({t_3})={s_3}$ m."
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là sai.\n\n"\
    f"$s({t_3})={s_3}$ m."

    if a>0:        

        t_1=random.randint(1,5)
        t_2=t_1+random.randint(2,4)

        chon=random.choice(["v_min","v_max"])
        
        if chon=="v_min":
        
            v_min=g1.subs(t,t_1)
            kq4_T=f"*Vận tốc nhỏ nhất vật đạt được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ là ${{{v_min}}}$ m/s"
            kq4_F=f"Vận tốc nhỏ nhất vật đạt được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ là ${{{g1.subs(t,t_2)}}}$ m/s"
            kq4=random.choice([kq4_T, kq4_F])
            loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
            f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$ Hàm $v(t)$ là hàm số đồng biến trên $\\mathbb{{R}}$.\n\n"\
            f"Trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ thì vận tốc đạt nhỏ nhất tại $t={t_1}$.\n\n"\
            f"Vận tốc đạt được khi đó là $v\\left({t_1}\\right)={v_min}$."
            if kq4==kq4_F:  
                loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n"\
            f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$ Hàm $v(t)$ là hàm số đồng biến trên $\\mathbb{{R}}$.\n\n"\
            f"Trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ thì vận tốc đạt nhỏ nhất tại $t={t_1}$.\n\n"\
            f"Vận tốc đạt được khi đó là $v\\left({t_1}\\right)={v_min}$."

        if chon=="v_max":
        
            v_max=g1.subs(t,t_2)
            kq4_T=f"*Vận tốc lớn nhất vật đạt được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ là ${v_max}$ m/s"
            kq4_F=f"Vận tốc lớn nhất vật đạt được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ là ${g1.subs(t,t_1)}$ m/s"
            kq4=random.choice([kq4_T, kq4_F])

            loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
            f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$ Hàm $v(t)$ là hàm số đồng biến trên $\\mathbb{{R}}$.\n\n"\
            f"Trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ thì vận tốc đạt lớn nhất tại $t={t_2}$.\n\n"\
            f"Vận tốc đạt được khi đó là $v\\left({t_2}\\right)={v_max}$."

            if kq4==kq4_F:
                loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n"\
                f"Khẳng định đã cho là khẳng định sai.\n\n"\
            f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$ Hàm $v(t)$ là hàm số đồng biến trên $\\mathbb{{R}}$.\n\n"\
            f"Trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ thì vận tốc đạt lớn nhất tại $t={t_2}$.\n\n"\
            f"Vận tốc đạt được khi đó là $v\\left({t_2}\\right)={v_max}$."
    

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

    loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
    f"b) {loigiai[1]}\\\\ \n"\
    f"c) {loigiai[2]}\\\\ \n"\
    f"d) {loigiai[3]}\n"

    #Tạo đề latex
    for i in range(len(list_PA)):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"        

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B5_06]-TF-M3. Xét Đ-S: Thể tích hộp khi cắt 4 góc.
def prt_34_L12_C1_B5_06():
	x=sp.symbols("x")
	a=random.randint(4,20)*3

	code_hinh=f" \\begin{{tikzpicture}}[>=stealth,line join=round,line cap=round,font=\\footnotesize,scale=.6]\n\
				\\filldraw[pattern=north east lines] \n\
				(0,0)rectangle(1,1)(0,4)rectangle(1,5)\n\
				(4,0)rectangle(5,1)(4,4)rectangle(5,5)\n\
				;\n\
				\\draw[dashed](1,1)rectangle(4,4);\n\
				\\draw(0,0)rectangle(5,5);\n\
				\\draw[dashed](5,5)arc(45:-45:{{5*1.41/2}}) node[midway,fill=white]{{${a}$ cm}};\n\
			\\end{{tikzpicture}}"
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)

	code_hinh_2=f" \\begin{{tikzpicture}}[>=stealth,line join=round,line cap=round,font=\\footnotesize,scale=.4]	\n\
				\\tikzset{{\n\
					pics/hhChuNhat/.style n args={{8}}{{\n\
						code={{\n\
							\\tikzset{{\n\
								declare function={{a=2.5;b=1.8;goc=-135;h=0.75;}}\n\
							}}\n\
							\\path \n\
							(0,0)coordinate(#1)+(0:a)coordinate(#2)+(goc:b)coordinate(#4)+(90:h)coordinate(#5)\n\
							($(#2)+(#4)-(#1)$)coordinate(#3)\n\
							;\n\
							\\foreach \\pone/\\pname in{{#2/#6,#3/#7,#4/#8}}{{\n\
								\\path \n\
								($(\\pone)+(#5)-(#1)$)coordinate(\\pname)\n\
								;\n\
							}}\n\
							\\foreach \\pointo/\\pointt in{{#2/#3,#3/#4,#5/#6,#6/#7,#7/#8,#8/#5,#2/#6,#3/#7,#4/#8}}{{\n\
								\\draw[fill=black](\\pointo)--(\\pointt);\n\
							}}\n\
						}}\n\
					}}\n\
				}}\n\
				\\path \n\
				(0,0) pic{{hhChuNhat={{A}}{{B}}{{C}}{{D}}{{A'}}{{B'}}{{C'}}{{D'}}}}\n\
				(intersection of A--D and C'--D')coordinate(M)\n\
				(intersection of A--B and B'--C')coordinate(N)\n\
				;\n\
				\\foreach \\pointo/\\pointt in{{A/M,A/N,A/A'}}{{\n\
					\\draw[fill=black](\\pointo)--(\\pointt);\n\
				}}\n\
				\\foreach \\pointo/\\pointt in{{D/M,B/N}}{{\n\
					\\draw[fill=black,dashed](\\pointo)--(\\pointt);\n\
				}}\n\
			\\end{{tikzpicture}}"

	code = my_module.moi_truong_anh_latex(code_hinh_2)
	file_name_2=my_module.pdftoimage_timename(code)


	noi_dung =(f"Từ một tấm bìa carton hình vuông có độ dài cạnh bằng ${{{a}}}$ cm, người ta cắt bốn hình vuông bằng nhau ở bốn góc rồi gập thành một chiếc hộp"
	f" có dạng hình hộp chữ nhật không có nắp (minh họa qua hình vẽ bên). Gọi ${{x}}$ (cm) là độ dài cạnh của các hình vuông nhỏ được cắt ở bốn góc của tấm bìa."
	f" Xét tính đúng-sai của các khẳng định sau. ")
	

	chon=random.randint(1,2)
	if chon==1:
		kq1_T=f"* Nếu cắt ở mỗi góc quá ${int(a/2)+random.randint(3,5)}$ cm thì không tạo được chiếc hộp có dạng hình hộp chữ nhật" 
		kq1_F=f"Nếu cắt ở mỗi góc quá ${int(a/2)+random.randint(3,5)}$ cm thì tạo được chiếc hộp có dạng hình hộp chữ nhật"
		
		HDG=f"Điều kiện: $0<2x<{a} \\Rightarrow 0<x<{phan_so(a/2)}$"
	
	if chon==2:
		kq1_T=f"* Nếu cắt ở mỗi góc nhỏ hơn ${int(a/2)-random.randint(1,3)}$ cm thì tạo được chiếc hộp có dạng hình hộp chữ nhật" 
		kq1_F=f"Nếu cắt ở mỗi góc nhỏ hơn ${int(a/2)-random.randint(1,3)}$ cm thì không tạo được chiếc hộp có dạng hình hộp chữ nhật"
		
		HDG=f"Điều kiện: $0<2x<{a} \\Rightarrow 0<x<{phan_so(a/2)}$."
	
	
	
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	f=(a-2*x)**2*x
	f_false=(a-x)**2*x	

	kq2_T=f"* Thể tích của chiếc hộp được mô tả bởi hàm số $V(x)={latex(expand(f))}$"
	kq2_F=f"Thể tích của chiếc hộp được mô tả bởi hàm số $V(x)={latex(expand(f_false))}$"
	
	HDG=(f"Khi cắt bỏ bốn hình vuông nhỏ có cạnh $x$ cm ở bốn góc và gập lên thì ta được một chiếc hộp chữ nhật không có nắp,"
		f" có đáy là hình vuông với độ dài cạnh bằng $({a}-2 x)$ (cm) và chiều cao bằng ${{x}}$ cm. Thể tích của chiếc hộp này là:\n\n"
		f"$V(x)=({a}-2x)({a}-2x)x={latex(expand(f))}$."
		)
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	f_dh=diff(f,x)
	eq=Eq(f_dh,0)
	tap_nghiem=solve(eq,x)
	x_1=min(tap_nghiem)
	x_2=max(tap_nghiem)
	V_max=f.subs(x,x_1)

	chon=random.randint(1,2)

	if chon==1:
		t1, t2=int(x_1)-random.randint(2,4), int(x_1)-random.randint(0,1)
		kq3_T=f"* Thể tích của hộp tăng dần nếu cắt trong khoảng từ {t1} cm đến {t2} cm" 
		kq3_F=f"Thể tích của hộp giảm dần nếu cắt trong khoảng từ {t1} cm đến {t2} cm"
		
		HDG=(f"$V'(x)={latex(expand(f_dh))}$.\n\n"
			f"$V'(x)=0 \\Leftrightarrow x={phan_so(x_1)}, x={phan_so(x_2)}$.\n\n"
			f"$V'(x)>0, \\forall x \\in ({t1};{t2})$ nên thể tích $V(x)$ của hộp tăng dần nếu cắt trong khoảng từ {t1} cm đến {t2} cm")
	
	if chon==2:
		t1, t2=int(x_1)+random.randint(1,3), a/2
		kq3_T=f"* Thể tích của hộp giảm dần nếu cắt trong khoảng từ {t1} cm đến {phan_so(t2)} cm" 
		kq3_F=f"Thể tích của hộp tăng dần nếu cắt trong khoảng từ {t1} cm đến {phan_so(t2)} cm"
		
		HDG=(f"$V'(x)={latex(expand(f_dh))}$.\n\n"
			f"$V'(x)=0 \\Leftrightarrow x={phan_so(x_1)}, x={phan_so(x_2)}$.\n\n"
			f"$V'(x)<0, \\forall x \\in ({t1};{t2})$ nên thể tích $V(x)$ của hộp giảm dần nếu cắt trong khoảng từ {t1} cm đến {t2} cm")
	
	
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"* Thể tích hộp đạt lớn nhất bằng ${{{phan_so(V_max)}}}$"
	kq4_F=f"Thể tích hộp đạt lớn nhất bằng ${{{phan_so(V_max+random.randint(1,3))}}}$"

	code_hinh_BBT=f" \\begin{{tikzpicture}}[>=stealth,line join=round,line cap=round,font=\\footnotesize,scale=1]\n\
					\\tkzTabInit[nocadre=false,lgt=1.2,espcl=3,deltacl=.55]\n\
					{{$x$/0.7, $V'(x)$/0.7, $V(x)$/1.8}}\n\
					{{$0$,${phan_so(x_1)}$,${phan_so(a/2)}$}}\n\
					\\tkzTabLine{{,+,$0$,-,}}\n\
					\\tkzTabVar{{-/$0$ ,+/ ${phan_so(V_max)}$ ,-/$0$}}	\n\
				\\end{{tikzpicture}}"

	code = my_module.moi_truong_anh_latex(code_hinh_BBT)
	file_name_BBT=my_module.pdftoimage_timename(code)
	
	HDG=(f"Dựa vào bảng biến thiên ta thấy $V_max=V({phan_so(x_1)})={phan_so(V_max)}$.")
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq4==kq4_F:
		loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	#random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)

	debai= f"{noi_dung}\n{file_name}\n{file_name_2}\n"\
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

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n{file_name_BBT}\n"

	loigiai_latex=(f"\n\n a) {loigiai[0]}\n\n"
	f"b) {loigiai[1]}\n\n"
	f"c) {loigiai[2]}\n\n"
	f"d) {loigiai[3]}\n\n")

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
		f"\\begin{{center}}\n{code_hinh_2}\n\\end{{center}}\n"\
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \\begin{{center}}\n{code_hinh_BBT}\n\\end{{center}}\n \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an


#[D12_C1_B5_07]-TF-M3. Cho chi phí trung bình C(x). Xét Đ-S: C(x_0), C'(x), sự tăng giảm, C_min.
def prt_34_L12_C1_B5_07():
	x=sp.symbols("x")

	a=random.randint(1,10)
	b=random.randint(100,400)

	f=(a*x**2+b)/(x)

	noi_dung =(f"Nếu trong một ngày, một xưởng sản xuất được ${{x}}$ kilôgam sản phẩm thì chi phí trung bình (tính bằng nghìn đồng)"
	f" cho một sản phẩm được tính bởi công thức $C(x)={latex(f)}$.\n\n Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười). ")		
	
	x_0=random.randint(15,45)
	y_0=f.subs(x,x_0)
	round_y_0=f"{round(y_0,1):.1f}".replace(".",",")
	round_y_0_false=f"{round(y_0+random.randint(1,3),1):.1f}".replace(".",",")

	kq1_T=f"* Chi phí trung bình cho một sản phẩm khi sản xuất ${{{x_0}}}$ kilôgam là {round_y_0} (nghìn đồng)" 
	kq1_F=f"Chi phí trung bình cho một sản phẩm khi sản xuất ${{{x_0}}}$ kilôgam là {round_y_0_false} (nghìn đồng)"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=(f"Chi phí trung bình cho một sản phẩm khi sản xuất ${{{x_0}}}$ kilôgam là:\n\n"
		f"$C({x_0})={round_y_0}$ (nghìn đồng).")
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"* Đạo hàm số của hàm số đã cho là $C'(x)= \\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$"
	kq2_F=f"Đạo hàm số của hàm số đã cho là $C'(x)= \\dfrac{{{latex(a*x**2-b)}}}{{x}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"$C'(x)=\\left({a}x+{latex(b/x)}\\right)'={a}-{latex(b/x**2)}=\\dfrac{{{latex(a*x**2-b)}}}{{x^2}}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x_1=sqrt(b/a)
	y_1=f.subs(x,x_1)
	x_1=latex(nsimplify(x_1))
	y_1=f"{round(y_1,1):.1f}".replace(".","\\text{{,}}")

	code_hinh_BBT=f" \\begin{{tikzpicture}}[>=stealth,line join=round,line cap=round,font=\\footnotesize,scale=1]\n\
					\\tkzTabInit[nocadre=false,lgt=1.2,espcl=3,deltacl=.55]\n\
					{{$x$/0.7, $C'(x)$/0.7, $C(x)$/1.8}}\n\
					{{$0$,${x_1}$,$+\\infty$}}\n\
					\\tkzTabLine{{,-,$0$,+,}}\n\
					\\tkzTabVar{{+/$+\\infty$ ,-/ ${y_1}$ ,+/$+\\infty$}}	\n\
				\\end{{tikzpicture}}"

	code = my_module.moi_truong_anh_latex(code_hinh_BBT)
	file_name_BBT=my_module.pdftoimage_timename(code)
	

	chon=random.randint(1,2)
	if chon==1:
		x_1=int(sqrt(b/a))-random.randint(1,3)
		kq3_T=f"* Chi phí trung bình cho một sản phẩm giảm dần khi $0<x<{x_1}$" 
		kq3_F=random.choice([
			f"Chi phí trung bình cho một sản phẩm tăng dần khi $x<{x_1}$",
			f"Chi phí trung bình cho một sản phẩm giảm dần khi $x<{x_1}$"])
	if chon==2:
		x_1=int(sqrt(b/a))+random.randint(1,6)
		kq3_T=f"* Chi phí trung bình cho một sản phẩm tăng dần khi $x>{x_1}$" 
		kq3_F=f"Chi phí trung bình cho một sản phẩm giảm dần khi $x>{x_1}$"
	
	HDG=(f"$C'(x)=0\\Leftrightarrow {latex(a*x**2-b)}=0\\Rightarrow x={latex(nsimplify(sqrt(b/a)))}$.\n\n"
		f"Dựa vào bảng biến thiên ta thấy:\n\n"
		f"$C(x)$ tăng khi $x>{latex(nsimplify(sqrt(b/a)))}$, giảm khi $0<x<{latex(nsimplify(sqrt(b/a)))}$."
		)
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x_1=sqrt(b/a)
	y_1=f.subs(x,x_1)	
	y_1=f"{round(y_1,1):.1f}".replace(".",",")

	
	y_2=f.subs(x,x_1)+random.randint(1,3)
	y_2=f"{round(y_2,1):.1f}".replace(".",",")

	kq4_T=f"* Chi phí trung bình cho một sản phẩm nhỏ nhất bằng ${{{y_1}}}$ (nghìn đồng)."
	kq4_F=f"Chi phí trung bình cho một sản phẩm nhỏ nhất bằng ${{{y_2}}}$ (nghìn đồng)." 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Dựa vào bảng biến thiên ta có chi phí trung bình cho một sản phẩm nhỏ nhất bằng ${{{y_1}}}$ (nghìn đồng)."
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
	f"a) {loigiai[0]}\n"\
	f"b) {loigiai[1]}\n"\
	f"c) {loigiai[2]}\n"\
	f"d) {loigiai[3]}\n"\

	loigiai_word=f"Lời giải:\n{file_name_BBT}\n {noi_dung_loigiai} \n" \

	loigiai_latex=f"\\begin{{center}}\n{code_hinh_BBT}\n\\end{{center}}\n\n"\
	f"a) {loigiai[0]}\n\n"\
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

#[D12_C1_B5_08]-TF-M3. Cho hộp có V và h. Xét Đ-S: y=kx, S_tp, đạo hàm, Stp_min.
def prt_34_L12_C1_B5_08():
	x,y=sp.symbols("x y")

	h=random.randint(1,20)
	if h<10:
		V=h*random.choice([10*i for i in range(2,7)])
	else:
		V=h*random.choice([10*i for i in range(1,5)])


	noi_dung = (f"Người ta chế tạo một chiếc hộp chữ nhật có thể tích ${V}cm^3$, chiều cao là ${{{h}}}$ cm."
	f" Gọi $x,y$ là các kích thước còn lại của chiếc hộp với $x>0,y>0$. Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần trăm):")	
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"* $y={latex(V/(h*x))}$" 
	kq1_F=f"$y={latex(V/x)}$"
	
	HDG=f"$V={latex(x*y*h)}={V}\\Rightarrow xy={phan_so(V/h)}\\Rightarrow y={latex(V/(h*x))}$."
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"* Diện tích toàn phần của chiếc hộp là $S(x)={phan_so(2*V/h)}+{latex(2*h*x+2*V/x)}$"
	kq2_F=f"Diện tích toàn phần của chiếc hộp là $S(x)={phan_so(2*V/h)}+{latex(h*x+2*V/x)}$"


	
	HDG=(f"Diện tích toàn phần của chiếc hộp là:\n\n"
	f"$S(x)=2xy+2x.{h}+2y.{h}=2.{phan_so(V/h)}+2x.{h}+{2*h}.{latex(V/(h*x))}={phan_so(2*V/h)}+{latex(2*h*x+2*V/x)}$.")
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* $S'(x)=\\dfrac{{{2*h}x^2-{2*V}}}{{x^2}}$" 
	kq3_F=f"$S'(x)=\\dfrac{{{h}x^2-{V}}}{{x^2}}$ "
	
	HDG=f"$S'(x)={2*h}-{latex(2*V/x**2)}=\\dfrac{{{2*h}x^2-{2*V}}}{{x^2}}$."
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x_0=latex(sqrt(int(V/h)))
	x_0_false=latex(sqrt(int(V/h+random.randint(1,3))))

	f=2*V/h+2*h*x+2*V/x
	y_0=f"{round(f.subs(x,sqrt(V/h)),2):.2f}".replace(".","\\text{{,}}")
	kq4_T=f"* Chi phí vật liệu làm hộp nhỏ nhất khi $x={x_0}$"
	kq4_F=f"Chi phí vật liệu làm hộp nhỏ nhất khi $x={x_0_false}$"

	code_hinh_BBT=f" \\begin{{tikzpicture}}[>=stealth,line join=round,line cap=round,font=\\footnotesize,scale=1]\n\
					\\tkzTabInit[nocadre=false,lgt=1.2,espcl=3,deltacl=.55]\n\
					{{$x$/0.7, $S'(x)$/0.7, $S(x)$/1.8}}\n\
					{{$0$,${x_0}$,$+\\infty$}}\n\
					\\tkzTabLine{{,-,$0$,+,}}\n\
					\\tkzTabVar{{+/$+\\infty$ ,-/ ${y_0}$ ,+/$+\\infty$}}	\n\
				\\end{{tikzpicture}}"

	code = my_module.moi_truong_anh_latex(code_hinh_BBT)
	file_name_BBT=my_module.pdftoimage_timename(code)
	
	HDG=(f"$S'(x)=0 \\Leftrightarrow {2*h}x^2-{2*V}=0\\Rightarrow x={latex(sqrt(int(V/h)))}$.\n\n"
		f"Dựa vào bảng biến thiên ta có: $S(x)_{{min}}={y_0}$ khi $x={latex(sqrt(int(V/h)))}$.")
	kq4=random.choice([kq4_T, kq4_F])
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


	noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n"
	f"\n\n a) {loigiai[0]}\n"
	f"b) {loigiai[1]}\n"
	f"c) {loigiai[2]}\n"
	f"d) {loigiai[3]}\n")

	loigiai_word=f"Lời giải:\n{file_name_BBT}\n {noi_dung_loigiai} \n"

	loigiai_latex=(f"\\begin{{center}}\n{code_hinh_BBT}\n\\end{{center}}\n\n"
	f"b) {loigiai[1]}\n\n"
	f"c) {loigiai[2]}\n\n"
	f"d) {loigiai[3]}\n\n")

	#Tạo đề latex
	for i in range(len(list_PA)):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
	    f"\\choiceTFt\n"
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
	    f"\\loigiai{{ \n {loigiai_latex} \n }}"
	    f"\\end{{ex}}\n")

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B5_09]-SA-M3. Cho hàm số lượng vi khuẩn. Tìm số vi khuẩn lớn nhất
def prt_34_L12_C1_B5_09():
	t=sp.symbols("t")
	a=random.randint(100,200)
	b=random.randint(100,400)
	N=random.randint(1000,2000)
	f=N+a*t/(b+t**2)
	N_max=f"{round(f.subs(t,sqrt(b)),0):.0f}".replace(".",",")

	code_hinh_BBT=f" \\begin{{tikzpicture}}[>=stealth,line join=round,line cap=round,font=\\footnotesize,scale=1]\n\
					\\tkzTabInit[nocadre=false,lgt=1.2,espcl=3,deltacl=.55]\n\
					{{$x$/0.7, $N'(x)$/0.7, $N(x)$/1.8}}\n\
					{{$0$,${latex(sqrt(b))}$,$+\\infty$}}\n\
					\\tkzTabLine{{,+,$0$,-,}}\n\
					\\tkzTabVar{{-/$-\\infty$ ,+/ ${N_max}$ ,-/${N}$}}	\n\
				\\end{{tikzpicture}}"

	code = my_module.moi_truong_anh_latex(code_hinh_BBT)
	file_name_BBT=my_module.pdftoimage_timename(code)

	noi_dung = (
	f"	Trong một thí nghiệm y học, người ta cấy ${{{N}}}$ vi khuẩn vào môi trường dinh dưỡng."
	f" Bằng thực nghiệm, người ta xác định được số lượng vi khuẩn thay đổi theo thời gian bởi công thức:"
	f" $N(t)={latex(f)}$ (con),"
	f" trong đó $t$ là thời gian tính bằng giây. Tính số lượng vi khuẩn lớn nhất kể từ khi thực hiện cấy vi khuẩn vào môi trường dinh dưỡng"
	f" (kết quả làm tròn đến hàng đơn vị)."
	)
	dap_an=N_max

	noi_dung_loigiai=(
	f"Ta có: $N'(t)=\\dfrac{{{a}({b}+t^2)-{a}t.2t}}{{(t^2+{b})^2}}=\\dfrac{{-{a}t^2+{a*b}}}{{(t^2+{b})^2}}$.\n\n"
	f"$N'(t)=0 \\Leftrightarrow -{a}t^2+{a*b}=0 \\Rightarrow t={latex(sqrt(b))}$.\n\n"
	f"Lập bảng biến thiên, ta thấy: $N_{{max}}=N({latex(sqrt(b))})={N_max}$."

	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n{file_name_BBT}\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n \\begin{{center}}\n{code_hinh_BBT}\n\\end{{center}}\n{noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C1_B5_10]-TF-M3. Cho hàm số số lượng vi khuẩn. Xét Đ-S: SL vi khuẩn, đạo hàm, tăng-giảm, max
def prt_34_L12_C1_B5_10():
	t=sp.symbols("t")
	a=random.randint(100,200)
	b=random.randint(100,400)
	N=random.randint(1000,2000)
	f=N+a*t/(b+t**2)
	N_max=f"{round(f.subs(t,sqrt(b)),0):.0f}".replace(".",",")
	N_max_false=f"{round(f.subs(t,sqrt(b))+random.randint(10,20),0):.0f}".replace(".",",")

	code_hinh_BBT=f" \\begin{{tikzpicture}}[>=stealth,line join=round,line cap=round,font=\\footnotesize,scale=1]\n\
					\\tkzTabInit[nocadre=false,lgt=1.2,espcl=3,deltacl=.55]\n\
					{{$x$/0.7, $N'(x)$/0.7, $N(x)$/1.8}}\n\
					{{$0$,${latex(sqrt(b))}$,$+\\infty$}}\n\
					\\tkzTabLine{{,+,$0$,-,}}\n\
					\\tkzTabVar{{-/$-\\infty$ ,+/ ${N_max}$ ,-/${N}$}}	\n\
				\\end{{tikzpicture}}"

	code = my_module.moi_truong_anh_latex(code_hinh_BBT)
	file_name_BBT=my_module.pdftoimage_timename(code)

	noi_dung = (
	f"	Trong một thí nghiệm y học, người ta cấy ${{{N}}}$ vi khuẩn vào môi trường dinh dưỡng."
	f" Bằng thực nghiệm, người ta xác định được số lượng vi khuẩn thay đổi theo thời gian bởi công thức:"
	f" $N(t)={latex(f)}$ (con),"
	f" trong đó $t$ là thời gian tính bằng giây. Xét tính đúng-sai của các khẳng định sau"
	f" (kết quả làm tròn đến hàng đơn vị)."
	)
	t_0=random.randint(2,10)
	y_0=f"{round(f.subs(t,t_0),0):.0f}"
	y_0_false=f"{round(f.subs(t,t_0)+random.randint(10,20),0):.0f}"
	kq1_T=f"* Số lượng vi khuẩn sau {t_0} giây bằng ${{{y_0}}}$" 
	kq1_F=f"Số lượng vi khuẩn sau {t_0} giây bằng: ${{{y_0_false}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Số lượng vi khuẩn sau 10 giây bằng: $N({t_0})={{{y_0}}}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"* Đạo hàm của hàm số là $N'(t)=\\dfrac{{-{a}t^2+{a*b}}}{{(t^2+{b})^2}}$"
	kq2_F=f"Đạo hàm của hàm số là $N'(t)=\\dfrac{{-{a}t^2+{b}}}{{(t^2+{b})^2}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Ta có: $N'(t)=\\dfrac{{{a}({b}+t^2)-{a}t.2t}}{{(t^2+{b})^2}}=\\dfrac{{-{a}t^2+{a*b}}}{{(t^2+{b})^2}}$.\n\n"
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* Số lượng vi khuẩn tăng dần khi $0<t<{int(sqrt(b))-random.randint(1,5)}$" 
	kq3_F=f"Số lượng vi khuẩn giảm dần khi $0<t<{int(sqrt(b))-random.randint(1,5)}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"$N'(t)=0 \\Leftrightarrow -{a}t^2+{a*b}=0 \\Rightarrow t={latex(sqrt(b))}$.\n\n"
		f"$N'(t)>0$ khi $t \\in (0;{latex(sqrt(b))})$, $N'(t)<0$ khi $t \\in ({latex(sqrt(b))};+\\infty)$.")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"* Số lượng vi khuẩn đạt lớn nhất bằng ${{{N_max}}}$"
	kq4_F=f"Số lượng vi khuẩn đạt lớn nhất bằng ${{{N_max_false}}}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Lập bảng biến thiên, ta thấy: $N_{{max}}=N({latex(sqrt(b))})={N_max}$."
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

	loigiai_word=f"Lời giải:\n {file_name_BBT} \n {noi_dung_loigiai} \n" \

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
	    f"\\loigiai{{ \n \\begin{{center}}\n{code_hinh_BBT}\n\\end{{center}}\n{loigiai_latex} \n }}"\
	    f"\\end{{ex}}\n"

	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	return debai,debai_latex,loigiai_word,dap_an

#[D12_C1_B5_11]-SA-M2. Tính chi phí trung bình sản xuất đồ chơi khi x đủ lớn.
def prt_34_L12_C1_B5_11():
	toy=random.choice(["ôtô đồ chơi", "máy bay mô hình", "tàu hỏa đồ chơi", 
		"xếp hình khối gỗ", "đồ chơi ghép tranh", "búp bê Barbie", "ô tô điều khiển từ xa"])
	T=random.randint(20,60)*1000
	m=random.randint(5,20)
	noi_dung = (
	f"Tại một công ty sản xuất {toy}, công ty phải chi ${{{T}}}$ USD để thiết lập dây chuyền sản xuất ban đầu."
	f" Sau đó, cứ sản xuất được một sản phẩm đồ chơi, công ty phải chi trả ${{{m}}}$ USD cho nguyên liệu thô và nhân công."
	f" Gọi $x~(x \\ge 1)$ là số {toy} mà công ty đã sản xuất và $T(x)$ (đơn vị USD) " 
	f" là tổng số tiền bao gồm cả chi phí ban đầu mà công ty phải chi trả khi sản xuất $x$ {toy}."
	f" Người ta xác định chi phí trung bình cho mỗi sản phẩm là $M(x)=\\dfrac{{T(x)}}{{x}}$."
	f" Khi $x$ đủ lớn $(x \\to +\\infty)$ thì chi phí trung bình (USD) cho mỗi sản phẩm {toy} là bao nhiêu?"
	)
	dap_an=m

	noi_dung_loigiai=(
	f"Chi phí tổng chi phí để sản xuất ${{x}}$ sản phẩm đồ chơi là: $T(x)= {T}+{m}x$\n\n"
	f"Chi phí trung bình cho mỗi sản phẩm đồ chơi là: $M(x)=\\dfrac{{{T}+{m}x}}{{x}}$.\n\n"
	f"Khi đó: $\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}} {{M(x)}}"
	f"=\\mathop{{\\lim}}\\limits_{{x \\to  +\\infty}}\\dfrac{{{T}+{m}x}}{{x}}={m}$.\n\n"
	f" Khi $x$ đủ lớn, chi phí trung bình cho mỗi sản phẩm {toy} là ${{{m}}}$ USD"

	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an







