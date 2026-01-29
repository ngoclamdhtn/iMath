import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module

def dau_ngoac(a):
    kq=a
    if a<0:
        kq=f"({a})"
    return kq

def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m
def thay_heso_1x(st):
	ketqua=st.replace("1x^2","x^2").replace("-1x^2","-x^2").replace("1x^3","x^3").replace("-1x^3","-x^3")
	return ketqua
def frac_to_dfrac(st):
    ketqua=st.replace(f"\\frac",f"\\dfrac")
    return ketqua

def xu_li_heso_1(a):
    if a==1:
        heso=""
    elif a==-1:
        heso="-" 
    else:
        heso=a 
    return heso
 

def check_so_nguyen(so):
    ketqua=False
    if isinstance(so, int):
        ketqua=True
    return ketqua

def tra_ve_dau(a):
	ketqua = "<0"
	if a>0: ketqua=">0"
	return ketqua

#Tính nghiệm và xét dấu delta
def tinh_va_dau_delta(a,b,c):
    d=b**2-4*a*c
    if d<0:
        dau="<0"
        x_1=""
        x_2=""
    if d==0:
        dau="=0"
        x_1=-b/(2*a)
        x_2=-b/(2*a)
    if d>0:
        dau=">0"
        x_1=(-b-sp.sqrt(d))/(2*a)
        x_2=(-b+sp.sqrt(d))/(2*a)
        if x_1>x_2:
            t=x_2
            x_2=x_1
            x_1=t
    return dau, x_1, x_2

def thay_dau_congtru(st):
    ketqua=st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("+ +","+").replace("+ -","-").replace("- -","+").replace("- +","-")
    return ketqua

#Giải bất phương trình bậc hai
def solve_bpt_bac2(a,b,c,dau_bpt,bien_x):
    delta,x_1,x_2=tinh_va_dau_delta(a,b,c)
    #ax^2 + bx + c>0
    if dau_bpt==">0" and a>0:    
            if delta == "<0":
                nghiem=f"$\\forall {bien_x} \\in \\mathbb{{R}}$"
            elif delta=="=0":
                nghiem=f"${bien_x}\\ne {phan_so(x_1)}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${bien_x} < {x_1}$ hoặc ${bien_x} > {x_2}$"
    if dau_bpt==">0" and a<0:
            if delta == "<0" or delta == "=0" :
                nghiem=f"không tồn tại ${bien_x}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${x_1} < {bien_x}< {x_2}$"

    #ax^2 + bx + c<0
    if dau_bpt=="<0" and a>0:

            if delta == "<0" or delta == "=0" :
                nghiem=f"không tồn tại ${bien_x}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${x_1} < {bien_x} <{x_2}$"            
    if dau_bpt=="<0" and a<0:       
            if delta == "<0":
                nghiem=f"$\\forall {bien_x} \\in \\mathbb{{R}}$"
            elif delta=="=0":
                nghiem=f"${bien_x}\\ne {phan_so(x_1)}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${bien_x} < {x_1}$ hoặc ${bien_x} > {x_2}$"

    #ax^2 + bx + c>0
    if dau_bpt==">=0" and a>0:
        
            if delta == "<0" or delta== "=0":
                nghiem=f"$\\forall {bien_x} \\in \\mathbb{{R}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${bien_x} \\le {x_1}$ hoặc  ${bien_x}\\ge {x_2}$"
    if dau_bpt==">=0" and a<0:
            if delta == "<0":
                nghiem=f"không tồn tại ${bien_x}$"
            elif delta == "=0":
                nghiem=f"${bien_x} = {phan_so(x_1)}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${x_1} \\le {bien_x} \\le {x_2}$"
    #ax^2 + bx + c<=0
    if dau_bpt=="<=0" and a>0:
            if delta == "<0":
                nghiem=f"không tồn tại ${bien_x}$"
            elif delta == "=0":
                nghiem=f"${bien_x} = {phan_so(x_1)}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${x_1} \\le {bien_x} \\le {x_2}$"
            
    if dau_bpt=="<=0" and a<0:           

            if delta == "<0" or delta== "=0":
                nghiem=f"$\\forall {bien_x} \\in \\mathbb{{R}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"${bien_x} \\le {x_1}$ hoặc ${bien_x} \\ge {x_2}$"
    return nghiem

#Tìm tập nghiệm bất phương trình bậc hai
def tapnghiem_bpt_bac2(a,b,c,dau_bpt,bien_x):
    delta,x_1,x_2=tinh_va_dau_delta(a,b,c)
    #ax^2 + bx + c>0
    if dau_bpt==">0" and a>0:    
            if delta == "<0":
                nghiem=f"$\\mathbb{{R}}$"
            elif delta=="=0":
                nghiem=f"$\\mathbb{{R}}\\backslash \\left\\{{{phan_so(x_1)}\\right\\}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left(-\\infty; {x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
    if dau_bpt==">0" and a<0:
            if delta == "<0" or delta == "=0" :
                nghiem=f"$\\emptyset$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left({x_1};{x_2}\\right)$"

    #ax^2 + bx + c<0
    if dau_bpt=="<0" and a>0:

            if delta == "<0" or delta == "=0" :
                nghiem=f"$\\emptyset$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left({x_1};{x_2}\\right)$"            
    if dau_bpt=="<0" and a<0:       
            if delta == "<0":
                nghiem=f"$\\mathbb{{R}}$"
            elif delta=="=0":
                nghiem=f"$\\mathbb{{R}}\\backslash \\left\\{{{phan_so(x_1)}\\right\\}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left(-\\infty; {x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"

    #ax^2 + bx + c>0
    if dau_bpt==">=0" and a>0:
        
            if delta == "<0" or delta== "=0":
                nghiem=f"$\\mathbb{{R}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left(-\\infty; {x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
    if dau_bpt==">=0" and a<0:
            if delta == "<0":
                nghiem=f"$\\emptyset$"
            elif delta == "=0":
                nghiem=f"$\\left\\{{{phan_so(x_1)}\\right\\}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left[{x_1};{x_2}\\right]$"
    #ax^2 + bx + c<=0
    if dau_bpt=="<=0" and a>0:
            if delta == "<0":
                nghiem=f"$\\emptyset$"
            elif delta == "=0":
                nghiem=f"$\\left\\{{{phan_so(x_1)}\\right\\}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left[{x_1};{x_2}\\right]$"
            
    if dau_bpt=="<=0" and a<0:           

            if delta == "<0" or delta== "=0":
                nghiem=f"$\\mathbb{{R}}$"
            else:
                if check_so_nguyen(x_1):            
                    x_1=phan_so(x_1)
                    x_2=phan_so(x_2)
                else:
                    x_1=latex(x_1)
                    x_2=latex(x_2)
                nghiem=f"$\\left(-\\infty; {x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
    return nghiem


 #Trả về phép cộng với ngoặc đơn
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

#Trả về phép trừ với ngoặc đơn
def show_tich(a,b):
    if b>0:
        ketqua=f"{a}.{b}"
    else:
        ketqua=f"{a}.({b})"
    return ketqua

#Bài 1 - Dấu của tam thức bậc hai

#[D10_C7_B1_01_M1]. Cho biểu thức bậc hai luôn âm hoặc luôn dương. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_01():
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if a*c<0:
    	c=-c
    b=int(sqrt(4*a*c))-random.randint(1,5)
    x=sp.symbols("x")
    f=a*x**2+b*x+c
    if a>0:
    	kq= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}$"
    	kq2= f"$f(x)= 0,\\forall x \\in \\mathbb{{R}}$"
    	kq3= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}$"
    	kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$"
    else:
    	kq= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}$"
    	kq2= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}$"
    	kq3= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"
    	kq4= f"$f(x)=0,\\forall x \\in \\mathbb{{R}}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  
    
    noi_dung= f"Cho biểu thức $f(x)={latex(f)}$. Tìm khẳng định đúng. \n"

    dap_an=my_module.tra_ve_dap_an(list_PA) 
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f""    
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

#[D10_C7_B1_02]-M1. Cho biểu thức bậc hai có nghiệm kép. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_02():
	x=sp.symbols("x")
	x_0=random.choice([random.randint(-7, -1), random.randint(1, 6)])
	a=random.randint(1,3)
	f=latex(expand(a*(x-x_0)**2))	
	if a>0:
		kq= random.choice([f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$", f"$f(x)> 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"])
		kq2= f"$f(x)> 0,\\forall x \\in \\mathbb{{R}}$"
		kq3= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
	else:
		kq= random.choice([f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$",f"$f(x)< 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"])
		kq2= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
		kq3= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"
		kq4= f"$f(x)< 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho biểu thức $f(x)={f}$. Tìm khẳng định đúng. \n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
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

#[D10_C7_B1_03]-M2. Cho biểu thức bậc hai có 2 nghiệm. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_03():
	a1=random.randint(1,6)
	b1=random.randint(1,15)
	a2=random.randint(1,6)
	b2=random.randint(1,20)
	if b1/a1==b2/a2:
		a2=a1+random.randint(1,4)
	a=a1*a2
	b=a1*b2+b1*a2
	c=b1*b2
	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))

	x=sp.symbols("x")
	f=a*x**2+b*x+c
	if a>0:
		f1=f"$f(x)> 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		f2=f"$f(x)\\ge 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		f3= f"$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		f4= f"$f(x)\\le 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"

		kq= random.choice([f1,f2,f3,f4])
		kq2= f"$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3= f"$f(x)<0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$"
	else:
		f1=f"$f(x)< 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		f2=f"$f(x)\\le 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		f3= f"$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		f4= f"$f(x)\\ge 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"

		kq= random.choice([f1,f2,f3,f4])
		kq2= f"$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3= f"$f(x)>0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho biểu thức $f(x)={latex(f)}$. Tìm khẳng định đúng. \n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
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

#[D10_C7_B1_04]-M1. Tìm m để biểu thức là bậc hai.
def aaa_pry_L10_C7_B1_04():

	a1=random.choice([random.randint(-10, -1), random.randint(1, 10)])	
	b1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b2=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a3=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a1*b1==a2*b2:
		a2=a1+random.randint(1,4)
	m=sp.symbols("m")
	x=sp.symbols("x")

	t1=latex(a1*m+b1)
	t2=latex(a2*m+b2)
	dau_a3=my_module.tao_dau(a3)


	f1=f"({t1})x^2{dau_a3}{a3}x+({t2})"
	f2=f"({t1})x^2 +({t2})x{dau_a3}{a3}"
	f=random.choice([f1,f2])

	kq=f"$m\\ne {latex(my_module.hien_phan_so(-b1/a1))}$"
	kq2=f"$m\\ne {latex(my_module.hien_phan_so(-b2/a2))}$"

	kq3_1=f"$m> {latex(my_module.hien_phan_so(-b1/a1))}$"
	kq3_2=f"$m> {latex(my_module.hien_phan_so(-b2/a2))}$"
	kq3=random.choice([kq3_1,kq3_2])

	kq4_1=f"$m= {latex(my_module.hien_phan_so(-b1/a1))}$"
	kq4_2=f"$m= {latex(my_module.hien_phan_so(-b1/a1))}$"
	kq4=random.choice([kq4_1,kq4_2])
   	

	    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho biểu thức $f(x)={f}$. Tìm tất cả các giá trị của tham số $m$ để $f(x)$ là biểu thức bậc 2. \n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
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

#[D10_C7_B1_05]-M1. Xác định biểu thức nào là tam thức bậc hai.
def aaa_pry_L10_C7_B1_05():
	a1=random.randint(1,6)
	b1=random.randint(-15,15)
	c1=random.randint(-10,10)
	a2=random.randint(1,6)
	b2=random.randint(1,15)
	c2=random.randint(-10,10)
	if b1==c1==0:
		c1=random.randint(1,10)

	x=sp.symbols("x")
	f1_1=a1*x**2+b1*x+c1
	f1_2=c2+b2*x**2
	f2_1=sqrt(a2*x**2+b2*x+c2)
	f2_2=sqrt(a2*x**2+b2*x+c2)
	f3_1=a1/x**2+b2*x+c2
	f3_2=a2/x+b2*x**2+c2
	f4=a2*x+c1

	kq=latex(random.choice([f1_1,f1_2]))
	kq2=latex(random.choice([f2_1,f2_2]))
	kq3=latex(random.choice([f3_1,f3_2]))
	kq4=latex(f4)
   	

	#Tạo các phương án
	pa_A= f"*$f_1(x)={kq}$"
	pa_B= f"$f_2(x)={kq2}$"
	pa_C= f"$f_3(x)={kq3}$"
	pa_D= f"$f_4(x)={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong các biểu thức sau, biểu thức nào là tam thức bậc 2. \n" 
	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
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

#[D10_C7_B1_06]-M1. Cho đồ thị bậc hai luôn âm hoặc luôn dương. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_06():
	a = random.choice([random.randint(-2, -1), random.randint(1, 2)])
	c = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	if a*c<0:
		c=-c
	b=int(sqrt(4*a*c))-random.randint(1,3)
	x=sp.symbols("x")
	f=a*x**2+b*x+c
	if a>0:
		kq= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}$"
		kq2= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"
		kq3= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$"
	else:
		kq= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}$"
		kq2= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}$"
		kq3= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$"

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	 #Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	dap_an=my_module.tra_ve_dap_an(list_PA)

	code = my_module.codelatex_dothi_bac_2(a,b,c)
	file_name = my_module.pdftoimage_timename(code)
	code_latex = my_module.codelatex_dothi_bac_2_no_header(a,b,c)

	noi_dung=f"Cho hàm số $f(x)=ax^2+bx+c$ có đồ thị như hình vẽ. Tìm khẳng định đúng."

	debai= f"{noi_dung}\n\n" \
			f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C7_B1_07]-M1. Cho đồ thị bậc hai có nghiệm kép. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_07():
	a = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	b = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	c= latex(my_module.hien_phan_so(b**2/(4*a)))
	dau_c="+"
	if a<0:
		dau_c=""
	x_0=latex(my_module.hien_phan_so(-b/(2*a)))
	x=sp.symbols("x")	
	if a>0:
		kq= random.choice([f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$", f"$f(x)> 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"])
		kq2= f"$f(x)> 0,\\forall x \\in \\mathbb{{R}}$"
		kq3= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
	else:
		kq= random.choice([f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$",f"$f(x)< 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"])
		kq2= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
		kq3= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  
	c= b**2/(4*a)
	code = my_module.codelatex_dothi_bac_2(a,b,c)
	file_name = my_module.pdftoimage_timename(code)
	code_latex = my_module.codelatex_dothi_bac_2_no_header(a,b,c)

	noi_dung=f"Cho hàm số $f(x)=ax^2+bx+c$ có đồ thị như hình vẽ. Tìm khẳng định đúng."

	debai= f"{noi_dung}\n\n" \
			 f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f""
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C7_B1_08]-M2. Cho đồ thị bậc hai có 2 nghiệm. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_08():
	a1 = random.choice([random.randint(-2, -1), random.randint(1, 2)])
	b1 = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	a2 = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	b2 = random.choice([random.randint(-2, -1), random.randint(1, 2)])

	if b1/a1==b2/a2:
		a2=a1+1
	if a2==0: a2=1
	a=a1*a2
	b=a1*b2+b1*a2
	c=b1*b2
	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))
		

	x=sp.symbols("x")
	f=a*x**2+b*x+c
	if a>0:
		f1=f"$f(x)> 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		f2=f"$f(x)\\ge 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		f3= f"$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		f4= f"$f(x)\\le 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"
		kq= random.choice([f1,f2,f3,f4])
		kq2= f"$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3= f"$f(x)<0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$"
	else:
		f1=f"$f(x)< 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		f2=f"$f(x)\\le 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		f3= f"$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		f4= f"$f(x)\\ge 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"
		kq= random.choice([f1,f2,f3,f4])
		kq2= f"$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3= f"$f(x)>0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	code_hinh=my_module.codelatex_dothi_bac_2_no_header(a,b,c)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name=my_module.pdftoimage_timename(code)



	noi_dung=f"Cho hàm số $f(x)=ax^2+bx+c$ có đồ thị như hình vẽ. Tìm khẳng định đúng."

	debai= f"{noi_dung}\n\n" \
			 f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f""
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C7_B1_09]-M1. Cho BXD bậc hai luôn âm hoặc luôn dương. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_09():
    while True:
        a =  random.choice([i for i in range(-5, 6) if i!=0])
        b =  random.choice([i for i in range(-5, 6) if i!=0])
        c =  random.choice([i for i in range(-5, 6) if i!=0])
        delta=b**2-4*a*c
        if delta<0:
            break

    x=sp.symbols("x")
    f=a*x**2+b*x+c
    if a>0:
    	kq= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}$"
    	kq2= f"$f(x)= 0,\\forall x \\in \\mathbb{{R}}$"
    	kq3= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}$"
    	kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$"
    else:
    	kq= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}$"
    	kq2= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}$"
    	kq3= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"
    	kq4= f"$f(x)= 0,\\forall x \\in \\mathbb{{R}}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án

    code_bxd = my_module.codelatex_bxd_bac2(a,b,c)
    code = my_module.moi_truong_anh_latex(code_bxd)
    file_name = my_module.pdftoimage_timename(code)


    noi_dung=f"Cho hàm số $f(x)=ax^2+bx+c$ có bảng xét dấu như hình dưới đây. Tìm khẳng định đúng."

    debai= f"{noi_dung}\n\n" \
    		 f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
    noi_dung_loigiai=f""
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
    	list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
    	f"\\begin{{center}}\n{code_bxd}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C7_B1_10]-M1. Cho BXD bậc hai có nghiệm kép. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_10():
    while True:
        a =  random.choice([i for i in range(-5, 6) if i!=0])
        b =  random.choice([i for i in range(-5, 6) if i!=0])
        c =  random.choice([i for i in range(-5, 6) if i!=0])
        delta=b**2-4*a*c
        if delta==0:
            break
    x_0=latex(my_module.hien_phan_so(-b/(2*a)))
    x=sp.symbols("x")
    if a>0:
    	kq= random.choice([f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$", f"$f(x)> 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"])
    	kq2= f"$f(x)> 0,\\forall x \\in \\mathbb{{R}}$"
    	kq3= f"$f(x)<0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
    	kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
    else:
    	kq= random.choice([f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$",f"$f(x)< 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"])
    	kq2= f"$f(x)>0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"
    	kq3= f"$f(x)< 0,\\forall x \\in \\mathbb{{R}}$"
    	kq4= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}\\backslash\\left\\{{{x_0}\\right\\}}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  


    code_bxd = my_module.codelatex_bxd_bac2(a,b,c)
    code = my_module.moi_truong_anh_latex(code_bxd)
    file_name = my_module.pdftoimage_timename(code)


    noi_dung=f"Cho hàm số $f(x)=ax^2+bx+c$ có bảng xét dấu như hình dưới đây. Tìm khẳng định đúng."

    debai= f"{noi_dung}\n\n" \
    		 f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
    noi_dung_loigiai=f""
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
    	list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
    	f"\\begin{{center}}\n{code_bxd}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C7_B1_11]-M2. Cho bxd bậc hai có 2 nghiệm. Tìm khẳng định đúng về dấu.
def aaa_pry_L10_C7_B1_11():
	x=sp.symbols("x")
	a1 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	a2 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b2 = random.choice([random.randint(-4, -1), random.randint(1, 4)])

	if -b1/a1==-b2/a2: 
		b2=b2+random.randint(1,3)
	a=a1*a2
	b=a1*b2+b1*a2
	c=b1*b2
	f=a*x**2+b*x+c

	code_bxd = my_module.codelatex_bxd_bac2(a,b,c)
	code = my_module.moi_truong_anh_latex(code_bxd)
	file_name = my_module.pdftoimage_timename(code)

	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))	
	
	
	if a>0:
		f1=f"$f(x)> 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		f2=f"$f(x)\\ge 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		f3= f"$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		f4= f"$f(x)\\le 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"

		kq= random.choice([f1,f2,f3,f4])
		kq2= f"$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3= f"$f(x)<0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4= f"$f(x)\\le 0,\\forall x \\in \\mathbb{{R}}$"
	else:
		f1=f"$f(x)< 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		f2=f"$f(x)\\le 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		f3= f"$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		f4= f"$f(x)\\ge 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"

		kq= random.choice([f1,f2,f3,f4])
		kq2= f"$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3= f"$f(x)>0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  

	noi_dung=f"Cho biểu thức $f(x)=ax^2+bx+c$ có bảng xét dấu như hình dưới đây. Tìm khẳng định đúng."

	debai= f"{noi_dung}\n\n" \
			 f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung_loigiai=f""
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{code_bxd}\n\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	f"\\begin{{center}}\n{code_bxd}\n\\end{{center}}\n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C7_B1_12]-TF-M2. Cho biểu thức bậc hai có 2 nghiệm, tạo câu đúng-sai về dấu.
def aaa_pry_L10_C7_B1_12(): 
	x=sp.symbols("x")
	a1=random.randint(1,6)
	b1=random.randint(1,15)
	a2=random.randint(1,6)
	b2=random.randint(1,20)
	if -b1/a1==-b2/a2:
		a2=a2+random.randint(1,4)
	a=a1*a2
	b=a1*b2+b1*a2
	c=b1*b2
	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))

	x=sp.symbols("x")
	f=a*x**2+b*x+c	
	
	dau=random.choice([">0"]) # ,"<0","\\ge 0", "\\le 0"
	if a>0:
		
		kq1_1= f"*$f(x)>0 \\Leftrightarrow x\\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
		kq2_1= f"*$f(x)<0 \\Leftrightarrow x\\in\\left({x_1};{x_2}\\right)$"
		kq3_1=f"*$f(x)\\le 0 \\Leftrightarrow x\\in\\left[{x_1};{x_2}\\right]$"
		kq4_1=f"*$f(x) \\ge 0 \\Leftrightarrow x\\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"

		kq1_2=f"$f(x)>0 \\Leftrightarrow x\\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"			
		kq2_2=f"$f(x)<0 \\Leftrightarrow x\\in\\left[{x_1};{x_2}\\right]$"			
		kq3_2=f"$f(x)\\le 0 \\Leftrightarrow x\\in\\left({x_1};+\\infty\\right)$"			
		kq4_2=f"$f(x)\\ge 0$ với mọi $x\\in\\mathbb{{R}}$"
	else:
		kq1_1= f"*$f(x)<0 \\Leftrightarrow x\\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
		kq2_1= f"*$f(x)>0 \\Leftrightarrow x\\in\\left({x_1};{x_2}\\right)$"
		kq3_1=f"*$f(x)\\ge 0 \\Leftrightarrow x\\in\\left[{x_1};{x_2}\\right]$"
		kq4_1=f"*$f(x) \\le 0 \\Leftrightarrow x\\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"

		kq1_2=f"$f(x)<0 \\Leftrightarrow x\\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"			
		kq2_2=f"$f(x)>0 \\Leftrightarrow x\\in\\left[{x_1};{x_2}\\right]$"			
		kq3_2=f"$f(x)\\ge 0 \\Leftrightarrow x\\in\\left({x_1};{x_2}\\right)$"			
		kq4_2=f"$f(x)\\le 0$ với mọi $x\\in \\mathbb{{R}}$"

	kq=random.choice([kq1_1, kq1_2])
	kq2=random.choice([kq2_1, kq2_2])
	kq3=random.choice([kq3_1, kq3_2])
	kq4=random.choice([kq4_1, kq4_2])	

	#Trộn các phương án
	list_PA =[kq, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	

	noi_dung=f"Cho biểu thức $f(x)={latex(f)}$. Xét tính đúng sai của các khẳng định sau:" 

	debai= f"{noi_dung}\n"\
	f"a) {list_PA[0]}.\n"\
	f"b) {list_PA[1]}.  \n"\
	f"c) {list_PA[2]}.  \n"\
	f"d) {list_PA[3]}.  \n"

	noi_dung_loigiai=f"Ta có ${latex(f)}=0$ có 2 nghiệm $x_1={x_1},x_2={x_2}$ và hệ số $a={a}{tra_ve_dau(a)}$ nên:\n"\
	f"a) {list_PA[0]} là câu {list_TF[0]}.\n"\
	f"b) {list_PA[1]} là câu {list_TF[1]}.\n"\
	f"c) {list_PA[2]} là câu {list_TF[2]}.\n"\
	f"d) {list_PA[3]} là câu {list_TF[3]}.\n"

	noi_dung_loigiai_latex=f"Ta có ${latex(f)}=0$ có 2 nghiệm $x_1={x_1},x_2={x_2}$ và hệ số $a={a}{tra_ve_dau(a)}$ nên:\\\\"\
	f"a) {list_PA[0]} là câu {list_TF[0]}.\\\\"\
	f"b) {list_PA[1]} là câu {list_TF[1]}.\\\\"\
	f"c) {list_PA[2]} là câu {list_TF[2]}.\\\\"\
	f"d) {list_PA[3]} là câu {list_TF[3]}.\\\\"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
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
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
	
	return debai,debai_latex,loigiai_word,dap_an

#[D10_C7_B1_13]-TF-M2. Cho bảng xét dấu hai nghiệm. Tạo câu hỏi đúng-sai.
def aaa_pry_L10_C7_B1_13():
	a1 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	a2 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b2 = random.choice([random.randint(-4, -1), random.randint(1, 4)])

	if -b1/a1==-b2/a2:
		a2=a1+1
	a=a1*a2
	b=a1*b2+b1*a2
	c=b1*b2
	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))
		
	x=sp.symbols("x")
	f=a*x**2+b*x+c
	if a>0:
		kq1_1=f"*$f(x)> 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq2_1=f"*$f(x)\\ge 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		kq3_1= f"*$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq4_1= f"*$f(x)\\le 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"
		
		kq1_2= f"$f(x)\\ge 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"
		kq2_2= f"$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3_2= f"$f(x)<0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4_2= f"$f(x)\\le 0,\\forall x \\left(-\\infty;{x_1}\\right] \\cup \\left({x_2};+\\infty\\right]$"
	else:
		kq1_1=f"*$f(x)< 0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq2_1=f"*$f(x)\\le 0,\\forall x \\in \\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		kq3_1= f"*$f(x)> 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq4_1= f"*$f(x)\\ge 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"
		
		kq1_2= f"$f(x)\\le 0,\\forall x \\in \\left[{x_1};{x_2}\\right]$"
		kq2_2= f"$f(x)< 0,\\forall x \\in \\left({x_1};{x_2}\\right)$"
		kq3_2= f"$f(x)>0,\\forall x \\in \\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$"
		kq4_2= f"$f(x)\\ge 0,\\forall x \\in \\mathbb{{R}}$"     


	kq=random.choice([kq1_1, kq1_2])
	kq2=random.choice([kq2_1, kq2_2])
	kq3=random.choice([kq3_1, kq3_2])
	kq4=random.choice([kq4_1, kq4_2])  
	
	#Trộn các phương án
	list_PA =[kq, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

	code_hinh = my_module.codelatex_bxd_bac2(a,b,c)
	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code) 

	noi_dung=f"Cho biểu thức $f(x)$ xác định trên $\\mathbb{{R}}$ và có bảng xét dấu như hình vẽ. Xét tính đúng sai của các khẳng định sau:\n" \
		
	debai= f"{noi_dung}\n\n"\
		f"{file_name}\n"\
		f"a) {list_PA[0]}.\n"\
		f"b) {list_PA[1]}.  \n"\
		f"c) {list_PA[2]}.  \n"\
		f"d) {list_PA[3]}.  \n"

	noi_dung_loigiai=f" Dựa vào bảng xét dấu ta có: \n"\
		f"a) {list_PA[0]} là câu {list_TF[0]}.\n"\
		f"b) {list_PA[1]} là câu {list_TF[1]}.\n"\
		f"c) {list_PA[2]} là câu {list_TF[2]}.\n"\
		f"d) {list_PA[3]} là câu {list_TF[3]}.\n"
	noi_dung_loigiai_latex=f" Dựa vào bảng xét dấu ta có: \\\\"\
		f"a) {list_PA[0]} là câu {list_TF[0]}.\\\\"\
		f"b) {list_PA[1]} là câu {list_TF[1]}.\\\\"\
		f"c) {list_PA[2]} là câu {list_TF[2]}.\\\\"\
		f"d) {list_PA[3]} là câu {list_TF[3]}.\\\\"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,dap_an

#[D10_C7_B1_14]-M2. Cho BXD bậc hai có 2 nghiệm. Tìm biểu thức bậc 2.
def aaa_pry_L10_C7_B1_14():
	x=sp.symbols("x")
	a1 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
	a2 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	b2 = random.choice([random.randint(-4, -1), random.randint(1, 4)])

	if -b1/a1==-b2/a2: 
		b2=b2+random.randint(1,3)
	a=a1*a2
	b=a1*b2+b1*a2
	c=b1*b2
	f=a*x**2+b*x+c

	code_bxd = my_module.codelatex_bxd_bac2(a,b,c)
	code = my_module.moi_truong_anh_latex(code_bxd)
	file_name = my_module.pdftoimage_timename(code)

	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))

	noi_dung=f"Bảng xét dấu như hình dưới đây là của biểu thức nào?"

	
	kq = latex(a*x**2+b*x+c)
	kq2= latex(-a*x**2-b*x-c)
	kq3= latex(a*x**2-b*x+c)
	kq4= latex(-a*x**2-b*x+c)

	if a>0:
		noi_dung_loigiai=f"Dựa vào bảng xét dấu ta có hệ số $a>0$.\n\n"\
		f"Dựa vào bảng xét dấu ta có biểu thức cần có nghiệm là $\\displaystyle x={x_1}, x={x_2}$.\n\n"\
		f"Tìm nghiệm cho các phương án thỏa mãn $a>0$ ta được $f(x)={kq}$."
	else:
		noi_dung_loigiai=f"Dựa vào bảng xét dấu ta có hệ số $a<0$.\n\n"\
		f"Dựa vào bảng xét dấu ta có biểu thức cần có nghiệm là $\\displaystyle x={x_1}, x={x_2}$.\n\n"\
		f"Tìm nghiệm cho các phương án thỏa mãn $a<0$ ta được $f(x)={kq}$."

	#Tạo các phương án
	pa_A= f"*$f(x)={kq}$"
	pa_B= f"$f(x)={kq2}$"
	pa_C= f"$f(x)={kq3}$"
	pa_D= f"$f(x)={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	

	debai= f"{noi_dung}\n\n" \
			 f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{frac_to_dfrac(code_bxd)}\n\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{frac_to_dfrac(code_bxd)}\n\\end{{center}}\n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C7_B1_15]-M2. Cho BXD bậc hai có 1 nghiệm. Tìm biểu thức bậc 2.
def aaa_pry_L10_C7_B1_15():
	x=sp.symbols("x")
	x_0 = random.randint(-10, 10)
	a1 = random.choice([random.randint(-8, -1), random.randint(1, 8)])	
	a, b, c= a1, -2*a1*x_0, a1*x_0**2

	f=expand(a1*(x-x_0)**2)

	code_bxd = my_module.codelatex_bxd_bac2(a,b,c)
	code = my_module.moi_truong_anh_latex(code_bxd)
	file_name = my_module.pdftoimage_timename(code)

	noi_dung=f"Bảng xét dấu như hình dưới đây là của biểu thức nào?"
	
	kq = latex(a*x**2+b*x+c)
	kq2= latex(-a*x**2-b*x-c)
	kq3= latex(a*x**2-b*x+c)
	kq4= latex(-a*x**2-b*x+c)

	if a>0:
		noi_dung_loigiai=f"Dựa vào bảng xét dấu ta có hệ số $a>0$.\n\n"\
		f"Dựa vào bảng xét dấu ta có biểu thức cần có nghiệm kép là $x={x_0}$.\n\n"\
		f"Tìm nghiệm cho các phương án thỏa mãn $a>0$ ta được $f(x)={kq}$."
	else:
		noi_dung_loigiai=f"Dựa vào bảng xét dấu ta có hệ số $a<0$.\n\n"\
		f"Dựa vào bảng xét dấu ta có biểu thức cần có nghiệm kép là $x={x_0}$.\n\n"\
		f"Tìm nghiệm cho các phương án thỏa mãn $a<0$ ta được $f(x)={kq}$."

	#Tạo các phương án
	pa_A= f"*$f(x)={kq}$"
	pa_B= f"$f(x)={kq2}$"
	pa_C= f"$f(x)={kq3}$"
	pa_D= f"$f(x)={kq4}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	

	debai= f"{noi_dung}\n\n" \
			 f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	dap_an=my_module.tra_ve_dap_an(list_PA)
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
	loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

	#Tạo đề latex
	for i in range(4):
		list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{frac_to_dfrac(code_bxd)}\n\\end{{center}}\n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
		f"\\begin{{center}}\n{frac_to_dfrac(code_bxd)}\n\\end{{center}}\n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an




#[D10_C7_B1_16]-TF-M3. Cho bxd của Parabol có 2 nghiệm. Tìm khẳng định đúng về Parabol.
def aaa_pry_L10_C7_B1_16():
    x=sp.symbols("x")
    x_I= random.choice([i for i in range(-5,10) if i!=0])
    x_1=random.choice([i for i in range(-10,5) if i < x_I])
    x_2= 2*x_I-x_1
    
    chon =random.randint(1,2)    
    if chon ==1:
        a=random.randint(1,5)
        c= phan_so(a*x_1*x_2)

        code_hinh =f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,-,0,+,}}\n\
                \\end{{tikzpicture}}\n"

        code = my_module.moi_truong_anh_latex(code_hinh)
        file_name=my_module.pdftoimage_timename(code)

        noi_dung = f"Cho hàm số bậc hai $y=f(x)=ax^{{2}}+bx+{c}$ có đồ thị là Parabol $(P)$. Biết biểu thức ${{f(x)}}$ có bảng xét dấu như hình vẽ. Xét tính đúng-sai của các khẳng định sau. "   
        noi_dung=thay_dau_congtru(noi_dung)  
        
        kq1_T=f"* ${{(P)}}$ có bề lõm quay lên" 
        kq1_F=f" ${{(P)}}$ có bề lõm quay xuống"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${{(P)}}$ có bề lõm quay lên vì $a>0$"


    if chon ==2:
        a=random.randint(-5,-1)
        c= phan_so(a*x_1*x_2)

        code_hinh =f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,+,0,-,}}\n\
                \\end{{tikzpicture}}\n"

        code = my_module.moi_truong_anh_latex(code_hinh)
        file_name=my_module.pdftoimage_timename(code)

        noi_dung = f"Cho hàm số bậc hai $y=f(x)=ax^{{2}}+bx+{c}$. Biết biểu thức ${{f(x)}}$ có bảng xét dấu như hình vẽ. Xét tính đúng-sai của các khẳng định sau. "   
        noi_dung=thay_dau_congtru(noi_dung)  
        debai_word= f"{noi_dung}\n"\
                    f"{file_name}"
        
        kq1_T=f"* ${{(P)}}$ có bề lõm quay xuống" 
        kq1_F=f" ${{(P)}}$ có bề lõm quay lên"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${{(P)}}$ có bề lõm quay xuống vì $a<0$"


    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* $(P)$ có trục đối xứng là $x={x_I}$"
    kq2_F=f"$(P)$ có trục đối xứng là $x={phan_so(2*x_I)}$ "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f" $(P)$ có trục đối xứng là $x=\\dfrac{{{x_1}+{x_2}}}{{2}}={x_I}$"
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $a={a}$" 
    kq3_F=f"$a={a+random.randint(1,5)}$ "
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"  Ta có $f(x)=a(x-{x_1})(x-{x_2})$ suy ra ${c}= a. {dau_ngoac(x_1)}. {dau_ngoac(x_2)}$ vậy $a={a}$" 
    HDG=thay_dau_congtru(HDG)
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* $b ={phan_so(-2*a*x_I)}$"
    kq4_F=f"$b ={phan_so(2*a*x_I)}$ " 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"   Ta có $\\dfrac{{-b}}{{2a}}= {x_I}$ nên $b ={phan_so(-2*a*x_I)}$ "
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


#[D10_C7_B1_17]-M2. Cho f(x) 2 nghiệm. Tìm bảng xét dấu.
def aaa_pry_L10_C7_B1_17():
    x=sp.symbols("x")
    while True:
        x_1, x_2=random.sample(range(-7,7),2)
        if x_1<x_2:
            break
    a= random.choice([i for i in range(-5, 6) if i!=0])
    f=expand(a*(x-x_1)*(x-x_2))
    tap_ketqua= [f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,-,0,+,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,+,0,-,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,+,0,-,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,-,0,-,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,-,0,+,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$, $+\\infty$}}\n\
                \\tkzTabLine{{,+,0,-,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,-,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,+,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,+,}}\n\
            \\end{{tikzpicture}}"

            ]

    noi_dung=(
    f"Bảng xét dấu nào sau đây là của biểu thức $f(x)={latex(f)}$?"
    )
    
    if a>0:
        kq=f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,-,0,+,}}\n\
            \\end{{tikzpicture}}"
    else:
        kq=f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,+,0,-,}}\n\
            \\end{{tikzpicture}}"

    kq_false=[x for x in tap_ketqua if x!= kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$f(x)={latex(f)}=0$ có 2 nghiệm $x={x_1},x={x_2}$.")

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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

    
    code = my_module.moi_truong_anh_latex(kq)
    file_name_kq=my_module.pdftoimage_timename(code)

    code = my_module.moi_truong_anh_latex(kq2)
    file_name_kq2=my_module.pdftoimage_timename(code)

    code = my_module.moi_truong_anh_latex(kq3)
    file_name_kq3=my_module.pdftoimage_timename(code)

    code = my_module.moi_truong_anh_latex(kq4)
    file_name_kq4=my_module.pdftoimage_timename(code)

    pa_A= f"* {file_name_kq}"
    pa_B= f"{file_name_kq2}"
    pa_C= f"{file_name_kq3}"
    pa_D= f"{file_name_kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"
    phuongan= f"A. \n{ list_PA[0]}.\n   B. \n{ list_PA[1]}.\n    C. \n{ list_PA[2]}.\n     D. \n{ list_PA[3]}.\n"
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C7_B1_18]-M2. Cho f(x) 1 nghiệm. Tìm bảng xét dấu.
def aaa_pry_L10_C7_B1_18():
    x=sp.symbols("x")
    while True:
        x_1, x_2=random.sample(range(-7,7),2)
        if x_1<x_2:
            break
    a= random.choice([i for i in range(-5, 6) if i!=0])
    f=expand(a*(x-x_1)**2)
    tap_ketqua= [


    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$, $+\\infty$}}\n\
                \\tkzTabLine{{,+,0,-,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,-,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,+,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,+,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,+,}}\n\
            \\end{{tikzpicture}}",

    f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,-,}}\n\
            \\end{{tikzpicture}}",

            ]

    noi_dung=(
    f"Bảng xét dấu nào sau đây là của biểu thức $f(x)={latex(f)}$?"
    )
    
    if a>0:
        kq=f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,+,}}\n\
            \\end{{tikzpicture}}"
    else:
        kq=f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_1}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,-,}}\n\
            \\end{{tikzpicture}}"

    kq_false=[x for x in tap_ketqua if x!= kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$f(x)={latex(f)}=0$ có nghiệm kép $x={x_1}$.")

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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

    
    code = my_module.moi_truong_anh_latex(kq)
    file_name_kq=my_module.pdftoimage_timename(code)

    code = my_module.moi_truong_anh_latex(kq2)
    file_name_kq2=my_module.pdftoimage_timename(code)

    code = my_module.moi_truong_anh_latex(kq3)
    file_name_kq3=my_module.pdftoimage_timename(code)

    code = my_module.moi_truong_anh_latex(kq4)
    file_name_kq4=my_module.pdftoimage_timename(code)

    pa_A= f"* {file_name_kq}"
    pa_B= f"{file_name_kq2}"
    pa_C= f"{file_name_kq3}"
    pa_D= f"{file_name_kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"
    phuongan= f"A. \n{ list_PA[0]}.\n   B. \n{ list_PA[1]}.\n    C. \n{ list_PA[2]}.\n     D. \n{ list_PA[3]}.\n"
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


















############# Bài 2: Bất phương trình bậc hai ########################

#[D10_C7_B2_01]-M2. Giải bất phương trình bậc hai, tam thức vô nghiệm.
def aaa_pry_L10_C7_B2_01(): 
	x=sp.symbols("x")
	#Tạo hệ số vô nghiệm
	a = random.choice([random.randint(-2, -1), random.randint(1, 2)])
	c = random.choice([random.randint(-3, -1), random.randint(1, 3)])
	if a*c<0: c=-c
	b=int(sqrt(4*a*c))-random.randint(1,3)
	t_0=latex(my_module.hien_phan_so(-b/(2*a)))
	
	f=a*x**2+b*x+c
	dau=random.choice([">0","<0","\\ge 0", "\\le 0"])
	if a>0:
		if dau==">0" or dau=="\\ge 0":
			kq= f"$S=\\mathbb{{R}}$"
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{t_0}\\right\\}}$"
			kq3= f"$S=\\emptyset$"
			kq4= random.choice([f"$S=\\left({t_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {t_0}\\right)$"])
		else:
			kq= f"$S=\\emptyset$" 
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{t_0}\\right\\}}$"
			kq3= f"$S=\\mathbb{{R}}$"
			kq4= random.choice([f"$S=\\left({t_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {t_0}\\right)$"])
	else: # a<0
		if dau==">0" or dau=="\\ge 0":
			kq= f"$S=\\emptyset$" 
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{t_0}\\right\\}}$"
			kq3= f"$S=\\mathbb{{R}}$"
			kq4= random.choice([f"$S=\\left({t_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {t_0}\\right)$"]) 			
		else: 
			kq= f"$S=\\mathbb{{R}}$"
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{t_0}\\right\\}}$"
			kq3= f"$S=\\emptyset$"
			kq4= random.choice([f"$S=\\left({t_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {t_0}\\right)$"])			
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Tìm tập nghiệm của bất phương trình ${{{latex(f)}{dau}}}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"Ta có ${latex(f)}=0$ vô nghiệm và hệ số $a={a}{tra_ve_dau(a)}$ nên tập nghiệm là: {kq}."    
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

#[D10_C7_B2_02]-M2. Giải bất phương trình bậc hai, tam thức nghiệm kép.
def aaa_pry_L10_C7_B2_02(): 
	x=sp.symbols("x")
	x_0=random.choice([random.randint(-7, -1), random.randint(1, 6)])
	a=random.randint(1,3)
	f=latex(expand(a*(x-x_0)**2))	
	
	dau=random.choice([">0","<0","\\ge 0", "\\le 0"])
	if a>0:
		if dau==">0":
			kq= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$" 
			kq2= f"$S=\\mathbb{{R}}$"
			kq3= f"$S=\\emptyset$"
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$"])
		elif dau=="\\ge 0":
			kq= f"$S=\\mathbb{{R}}$" 
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$"
			kq3= f"$S=\\emptyset$" 
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$"])
		elif dau=="\\le 0":
			kq= f"$S=\\{{ {x_0} \\}}$" 
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$"
			kq3= f"$S=\\emptyset$" 
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$",f"$S=\\mathbb{{R}}$"])
		else:
			kq= f"$S=\\emptyset$" 
			kq2= f"$S=\\mathbb{{R}}$" 
			kq3= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$"			
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$"])

	else: # a<0
		if dau=="<0":
			kq= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$" 
			kq2= f"$S=\\mathbb{{R}}$"
			kq3= f"$S=\\emptyset$"
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$"])			
		elif dau=="\\le 0": 
			kq= f"$S=\\mathbb{{R}}$" 
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$"
			kq3= f"$S=\\emptyset$" 
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$"])

		elif dau=="\\ge 0":
			kq= f"$S=\\{{ {x_0} \\}}$" 
			kq2= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$"
			kq3= f"$S=\\emptyset$" 
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$",f"$S=\\mathbb{{R}}$"])

		else:
			kq= f"$S=\\emptyset$" 
			kq2= f"$S=\\mathbb{{R}}$" 
			kq3= f"$S=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}$"			
			kq4= random.choice([f"$S=\\left({x_0};+\\infty \\right)$", f"$S=\\left(-\\infty; {x_0}\\right)$"])			
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Tìm tập nghiệm của bất phương trình ${{{f}{dau}}}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"Ta có ${f}=0$ có nghiệm kép $x={x_0}$ và hệ số $a={a}{tra_ve_dau(a)}$ nên tập nghiệm là: {kq}."    
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


#[D10_C7_B2_03]-M2. Giải bất phương trình bậc hai, tam thức có 2 nghiệm.
def aaa_pry_L10_C7_B2_03(): 
	x=sp.symbols("x")
	a1=random.randint(1,6)
	b1=random.randint(1,15)
	a2=random.randint(1,6)
	b2=random.randint(1,20)
	
	if b1/a1==b2/a2:
		a2=a1+random.randint(1,4)
	a=a1*a2
	b=(a1*b2+b1*a2)
	c=b1*b2
	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))

	x=sp.symbols("x")
	f=a*x**2+b*x+c	
	
	dau=random.choice([">0","<0","\\ge 0", "\\le 0"])
	if a>0:
		if dau==">0":
			kq= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq2= f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq3= random.choice([f"$S=\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		elif dau=="\\ge 0":
			kq= f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$S=\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		
		elif dau=="<0":
			kq= f"$S=\\left({x_1};{x_2}\\right)$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		else:
			kq= f"$S=\\left[{x_1};{x_2}\\right]$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left({x_1};{x_2}\\right)$" ,f"$S=\\mathbb{{R}}$"])
	
	else: # a<0
		if dau=="<0":
			kq= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq3= random.choice([f"$S=\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
			
		elif dau=="\\le 0": 
			kq= f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$S=\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])	

		elif dau==">0":
			kq= f"$S=\\left({x_1};{x_2}\\right)$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
	
		else:
			kq= f"$S=\\left[{x_1};{x_2}\\right]$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$S=\\left({x_1};{x_2}\\right)$" ,f"$S=\\mathbb{{R}}$"])
			
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Tìm tập nghiệm của bất phương trình ${{{latex(f)}{dau}}}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"Ta có ${latex(f)}=0$ có 2 nghiệm $x_1={x_1},x_2={x_2}$ và hệ số $a={a}{tra_ve_dau(a)}$ nên tập nghiệm là: {kq}."    
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

#[D10_C7_B2_04]-M2. Giải BPT có 2 vế là bậc hai
def aaa_pry_L10_C7_B2_04(): 
	x=sp.symbols("x")
	a1=random.randint(1,6)
	b1=random.randint(1,15)
	a2=random.randint(1,6)
	b2=random.randint(1,20)
	if a1*b1==a2*b2:
		a2=a1+random.randint(1,4)
	a=a1*a2
	b=(a1*b2+b1*a2)
	c=b1*b2
	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))

	x=sp.symbols("x")
	#Tạo hệ số cặp
	m1=random.randint(-5,5)
	m2=a-m1

	n1=random.randint(-5,6)
	n2=b-n1

	p1=random.randint(1,7)
	p2=c-p1
	f_trai=latex(m1*x**2+n1*x+p1)
	f_phai=latex(-m2*x**2-n2*x-p2)


	f=a*x**2+b*x+c	
	
	dau=random.choice([">0","<0","\\ge 0", "\\le 0"])
	if a>0:
		if dau==">0":
			dau_1=">"
			kq= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq2= f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq3= random.choice([f"$\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		elif dau=="\\ge 0":
			dau_1="\\ge"
			kq= f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		
		elif dau=="<0":
			dau_1="<"
			kq= f"$\\left({x_1};{x_2}\\right)$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		else:
			dau_1="\\le"
			kq= f"$\\left[{x_1};{x_2}\\right]$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left({x_1};{x_2}\\right)$" ,f"$S=\\mathbb{{R}}$"])
	
	else: # a<0
		if dau=="<0":
			kq= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq2= f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq3= random.choice([f"$\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
			
		elif dau=="\\le 0": 
			kq= f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$\\left({x_1};{x_2}\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left[{x_1};{x_2}\\right)$",f"$S=\\mathbb{{R}}$"])	

		elif dau==">0":
			kq= f"$\\left({x_1};{x_2}\\right)$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
	
		else:
			kq= f"$\\left[{x_1};{x_2}\\right]$" 
			kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
			kq3= random.choice([f"$\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$", f"$S=\\emptyset$"])
			kq4= random.choice([f"$\\left({x_1};{x_2}\\right)$" ,f"$S=\\mathbb{{R}}$"])
			
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Tìm tập nghiệm của bất phương trình ${{{f_trai}{dau_1}{f_phai}}}$."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	noi_dung_loigiai=f"${f_trai}{dau_1}{f_phai}\\Rightarrow {latex(f)}{dau}$.\n Ta có: ${latex(f)}=0$ có 2 nghiệm $x_1={x_1},x_2={x_2}$ và hệ số $a={a}{tra_ve_dau(a)}$ nên tập nghiệm là: {kq}."    
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

#[D10_C7_B2_05]-M3. Tìm m để ax^2 +bx+c>0 (<0)  với mọi x.
def aaa_pry_L10_C7_B2_05(): 
	x=sp.symbols("x")
	m=sp.symbols("m")

	a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	a1=xu_li_heso_1(a)
	b=random.randint(-5, 5)	
	c= random.randint(-5, 5)
	a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

	#Tạo dấu bất phương trình 
	if a>0:
		dau=">0"
	else:
		dau="<0"

	f=f"{a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau}"

	delta= (m+b)**2-4*a*(a_m*m+c)

	delta= expand((m+b)**2-4*a*(a_m*m+c))

	a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c
	kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
	kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
	kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
	kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Tìm tất cả các giá trị của tham số ${{m}}$ để bất phương trình ${f}$ nghiệm đúng với mọi $x\\in \\mathbb{{R}}$."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	tich_4a=show_tich(4,a)

	noi_dung_loigiai=f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
			f"${f}$ với mọi $x\\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta <0$\n\n"\
			f"$\\Rightarrow {latex(delta)} <0 \\Rightarrow$ {kq}."    
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

#[D10_C7_B2_06]-M3. Tìm m để ax^2 +bx+c>=0 (<=0)  với mọi x.
def aaa_pry_L10_C7_B2_06(): 
	x=sp.symbols("x")
	m=sp.symbols("m")

	a =  random.choice([random.randint(-5, -1), random.randint(1, 5)])
	a1=xu_li_heso_1(a)
	b=random.randint(-5, 5)	
	c= random.randint(-5, 5)
	a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

	#Tạo dấu bất phương trình 
	if a>0:
		dau="\\ge 0"
	else:
		dau="\\le 0"

	f=f"{a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau}"

	delta= (m+b)**2-4*a*(a_m*m+c)

	delta= expand((m+b)**2-4*a*(a_m*m+c))

	a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

	kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
	kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
	kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
	kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Tìm tất cả các giá trị của tham số ${{m}}$ để bất phương trình ${f}$ với mọi $x\\in \\mathbb{{R}}$."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	tich_4a=show_tich(4,a)

	noi_dung_loigiai=f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
				f"${f}$ với mọi $x\\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta \\le 0$\n\n"\
				f"$\\Rightarrow {latex(delta)} \\le 0 \\Rightarrow$ {kq}."    
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

#[D10_C7_B2_07]-M3. Tìm m để ax^2 +bx+c>=0 (<=0) vô nghiệm.
def aaa_pry_L10_C7_B2_07(): 
	x=sp.symbols("x")
	m=sp.symbols("m")

	a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	a1=xu_li_heso_1(a)
	b=random.randint(-5, 5)	
	c= random.randint(-5, 5)
	a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

	delta= (m+b)**2-4*a*(a_m*m+c)
	delta= expand((m+b)**2-4*a*(a_m*m+c))
	a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

	#Tạo dấu bất phương trình 
	if a>0:
		dau="\\le 0"
		dau_nguoc=">"
		f=f"{a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau}"
			
	else:
		dau="\\ge 0"
		dau_nguoc="<"
		f=f"{a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau}"
		tich_4a=show_tich(4,a)

	kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
	kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
	kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
	kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
	
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Tìm tất cả các giá trị của tham số ${{m}}$ để bất phương trình ${f}$ vô nghiệm."
	tich_4a=show_tich(4,a)
	noi_dung_loigiai=f"${f}$ vô nghiệm $\\Leftrightarrow {a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$.\n\n"\
			f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
			f"${a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta <0$\n\n"\
			f"$\\Leftrightarrow {latex(delta)} <0 \\Leftrightarrow$ {kq}."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D10_C7_B2_08]-M3. Tìm m để ax^2 +bx+c>0 (<0) vô nghiệm.
def aaa_pry_L10_C7_B2_08(): 
	x=sp.symbols("x")
	m=sp.symbols("m")

	a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	a1=xu_li_heso_1(a)
	b=random.randint(-5, 5)	
	c= random.randint(-5, 5)
	a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

	delta= (m+b)**2-4*a*(a_m*m+c)
	delta= expand((m+b)**2-4*a*(a_m*m+c))
	a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

	#Tạo dấu bất phương trình 
	if a>0:
		dau="<0"
		dau_nguoc="\\ge "
		f=f"{a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau}"
			
	else:
		dau=">0"
		dau_nguoc="\\le "
		f=f"{a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau}"
		tich_4a=show_tich(4,a)

	kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
	kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
	kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
	kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
	
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Tìm tất cả các giá trị của m để bất phương trình ${f}$ vô nghiệm."
	tich_4a=show_tich(4,a)
	noi_dung_loigiai=f"${f}$ vô nghiệm $\\Leftrightarrow {a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$.\n\n"\
			f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
			f"${a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta \\le 0$\n\n"\
			f"$\\Leftrightarrow {latex(delta)} \\le 0 \\Leftrightarrow$ {kq}."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D10_C7_B2_09]-M2. Tìm tập xác định hàm số y=căn(ax^2+bx+c)
def aaa_pry_L10_C7_B2_09(): 
	x=sp.symbols("x")
	a1=random.randint(1,6)
	b1=random.randint(1,15)
	a2=random.randint(1,6)
	b2=random.randint(1,20)
	if b1/a1==b2/a2:
		a2=a1+random.randint(1,4)
	a=a1*a2
	b=(a1*b2+b1*a2)
	c=b1*b2
	if -b1/a1<-b2/a2:	
		x_1=latex(my_module.hien_phan_so(-b1/a1))
		x_2=latex(my_module.hien_phan_so(-b2/a2))
	else:
		x_1=latex(my_module.hien_phan_so(-b2/a2))
		x_2=latex(my_module.hien_phan_so(-b1/a1))

	x=sp.symbols("x")
	f=a*x**2+b*x+c	

	if a>0:	
	
		kq= f"$D=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"
		kq2= f"$D=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
		kq3= random.choice([f"$D=\\left({x_1};{x_2}\\right)$"])
		kq4= random.choice([f"$D=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		noi_dung_loigiai=f"Hàm số xác định khi ${latex(f)} \\ge 0 \\Leftrightarrow x\\le {x_1}$ hoặc $x\\ge {x_2}$.\n\n"\
		f" Tập xác định là: {kq}." 

	if a<0:		
		kq= f"$D=\\left[{x_1};{x_2}\\right]$" 
		kq2= f"$D=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
		kq3= random.choice([f"$D=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"])
		kq4= random.choice([f"$D=\\left({x_1};{x_2}\\right)$" ,f"$S=\\mathbb{{R}}$"])
		noi_dung_loigiai=f"Hàm số xác định khi ${latex(f)} \\ge 0 \\Leftrightarrow  {x_1}\\le x \\le {x_2}$.\n\n"\
		f" Tập xác định là: {kq}."
			
			
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Tìm tập xác định của hàm số $y={latex(sqrt(f))}$."

	debai= f"{noi_dung}\n"
	phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	   
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



#[D10_C7_B2_10]-M2. Toán thực tế: tìm giá bán để lợi nhuận thoả đk cho trước
def aaa_pry_L10_C7_B2_10(): 
    x=symbols("x")
    chon =random.randint(1,2)
    if chon ==1:
        x1=random.randint(4,8)
        c=x1*3
    if chon ==2:
        x1=2*random.randint(3,4)
        c=x1*4
    a=random.randint(10,30)
    B=2*a*(x1-random.randint(1,2))
    e=B+a*c 
    x2=e/a
    x0=(x1+x2)/2 
    x4=random.choice([i for i in range(x1+1,int(x0-1))]) 
    x5 =phan_so(2*x0-x4) 
    f4 =phan_so((e-a*x4)*(x4-x1))
    x0=phan_so(x0)
    x2=phan_so(x2)
    noi_dung = f"Lợi nhuận bán sách ${{X}}$ của một cửa hàng là một hàm số bậc hai $P(x)={{{latex(expand( (e-a*x)*(x-x1)))}}}$ (USD) với ${{x}}$ (USD) là giá bán một quyển sách ${{X}}$. Muốn lợi nhuận thu được lớn hơn ${{{f4}}}$ USD thì giá bán sách phải trong phạm vi:"

    noi_dung_loigiai=(f" Giải bất phương trình $P(x)={{{latex(expand( (e-a*x)*(x-x1)))}}} \\ge {f4}$ \n\n"
                        f" Ta được $ x \\in ({x4};{x5})$ \n\n"
    f"Muốn tổng lợi nhuận thu được lớn hơn ${{{f4}}}$ USD thì giá bán mới phải thuộc khoảng $({x4};{x5})$ ")

    kq=f" $({x4};{x5})$ (USD)"
    ds=[f"$({phan_so(x1)};{x5})$ (USD)", 
    f" $({phan_so(x1)};{x0})$ (USD)", 
    f" $({phan_so(x1)};{x4})$ (USD)", 
    f" $({x0};{x2})$ (USD)",
    f" $({phan_so(x4)};{x2})$ (USD)" ]
    kq2,kq3,kq4=random.sample(ds, 3)


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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan, dap_an

#[D10_C7_B2_11]-M2. Cho BXD 2 nghiệm. Tìm tập nghiệm của BPT.
def aaa_pry_L10_C7_B2_11():
    while True:
        x_1,x_2=random.sample(range(-8,9),2)
        if x_1<x_2:
            break
    tap_ketqua=[
        f"$\\emptyset$",
        f"$\\mathbb{{R}}$",
        f"${{[{x_1};{x_2}]}}$",
        f"$({x_1};{x_2})$",
        f"$({x_1};{x_2}]$",
        f"$[{x_1};{x_2})$",
        f"$(-\\infty;{x_1})$",
        f"$(-\\infty;{x_1}]$",
        f"$({x_2};+\\infty)$",
        f"$[{x_2};+\\infty)$",  
        f"$(-\\infty;{x_1}) \\cup ({x_2};+\\infty)$",
        f"$(-\\infty;{x_1}) \\cup [{x_2};+\\infty)$",
        f"$(-\\infty;{x_1}] \\cup ({x_2};+\\infty)$",
        f"$(-\\infty;{x_1}] \\cup [{x_2};+\\infty)$",]

    chon_bang=random.randint(1,2)

    if chon_bang==1:
        code_hinh = (f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,+,0,-,}}\n\
            \\end{{tikzpicture}}")
        
        chon=random.randint(1,4)  
        
        if chon==1:
            bpt=f"$f(x)\\ge 0$"  
            kq=f"${{[{x_1};{x_2}]}}$"
        
        if chon==2:
            bpt=f"$f(x) > 0$"        
            kq=f"$({x_1};{x_2})$"

        if chon==3:
            bpt=f"$f(x) < 0$"      
            kq=f"$(-\\infty;{x_1}) \\cup ({x_2};+\\infty)$"

        if chon==4:
            bpt=f"$f(x) \\le 0$"        
            kq=f"$(-\\infty;{x_1}] \\cup [{x_2};+\\infty)$"

    if chon_bang==2:
        code_hinh = (f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$,${x_1}$,${x_2}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,-,0,+,}}\n\
            \\end{{tikzpicture}}")
        
        chon=random.randint(1,4)  
        
        if chon==1:
            bpt=f"$f(x)\\le 0$"  
            kq=f"${{[{x_1};{x_2}]}}$"
        
        if chon==2:
            bpt=f"$f(x) < 0$"        
            kq=f"$({x_1};{x_2})$"

        if chon==3:
            bpt=f"$f(x) > 0$"      
            kq=f"$(-\\infty;{x_1}) \\cup ({x_2};+\\infty)$"

        if chon==4:
            bpt=f"$f(x) \\ge 0$"        
            kq=f"$(-\\infty;{x_1}] \\cup [{x_2};+\\infty)$" 

    kq_false=[x for x in tap_ketqua if x != kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name = my_module.pdftoimage_timename(code)

    noi_dung=(
        f"Cho tam thức $f(x)=ax^2+bx+c$ có bảng xét dấu như hình vẽ."
        f" Tập nghiệm của bất phương trình {bpt} là" )

    noi_dung_loigiai=(
    f"{bpt} $\\Leftrightarrow x\\in $ {kq}."
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

#[D10_C7_B2_12]-M2. Cho BXD 1 nghiệm. Tìm tập nghiệm của BPT.
def aaa_pry_L10_C7_B2_12():
    x_0=random.choice([phan_so(random.randint(1,10)/random.randint(1,10)),
    phan_so(-random.randint(1,10)/random.randint(1,10)) ])
    tap_ketqua=[
        f"$\\mathbb{{R}}$",
        f"$\\emptyset$",
        f"$(-\\infty;{x_0})$",
        f"$(-\\infty;{x_0}]$",
        f"$({x_0};+\\infty)$",
        f"$[{x_0};+\\infty)$",  
        f"$(-\\infty;{x_0}) \\cup ({x_0};+\\infty)$",        
        f"$(-\\infty;{x_0}] \\cup [{x_0};+\\infty)$",]

    chon_bang=random.randint(1,2)

    if chon_bang==1:
        code_hinh = (f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$, ${x_0}$,$+\\infty$}}\n\
                \\tkzTabLine{{,+,0,+,}}\n\
            \\end{{tikzpicture}}")
        
        chon=random.randint(1,4) 
        
        if chon==1:
            bpt=f"$f(x)\\ge 0$"  
            kq=f"$\\mathbb{{R}}$"
        
        if chon==2:
            bpt=f"$f(x) > 0$"        
            kq=f"$(-\\infty;{x_0}) \\cup ({x_0};+\\infty)$"

        if chon==3:
            bpt=f"$f(x) < 0$"      
            kq=f"$\\emptyset$"

        if chon==4:
            bpt=f"$f(x) \\le 0$"        
            kq=f"$\\left\\{{{x_0}\\right\\}}$"

    if chon_bang==2:
        code_hinh = (f"\\begin{{tikzpicture}}\n\
                \\tkzTabInit[nocadre=false, lgt=1.5, espcl=1.3] \n\
                {{$x$ /1,$f(x)$ /1}}\n\
                {{$-\\infty$,${x_0}$,$+\\infty$}}\n\
                \\tkzTabLine{{,-,0,-,}}\n\
            \\end{{tikzpicture}}")
        
        chon=random.randint(1,4)  
        
        if chon==1:
            bpt=f"$f(x)\\le 0$"  
            kq=f"$\\mathbb{{R}}$"
        
        if chon==2:
            bpt=f"$f(x) < 0$"        
            kq=f"$(-\\infty;{x_0}) \\cup ({x_0};+\\infty)$"

        if chon==3:
            bpt=f"$f(x) > 0$"      
            kq=f"$\\emptyset$"

        if chon==4:
            bpt=f"$f(x) \\ge 0$"        
            kq=f"$\\left\\{{{x_0}\\right\\}}$"

    kq_false=[x for x in tap_ketqua if x != kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name = my_module.pdftoimage_timename(code)


    noi_dung=(
        f"Cho tam thức $f(x)=ax^2+bx+c$ có bảng xét dấu như hình vẽ."
        f" Tập nghiệm của bất phương trình {bpt} là" )

    noi_dung_loigiai=(
    f"{bpt} $\\Leftrightarrow x\\in $ {kq}."
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

#[D10_C7_B2_13]-M2. Cho parabol 2 nghiệm. Tìm tập nghiệm của BPT.
def aaa_pry_L10_C7_B2_13():
    x=sp.symbols("x")
    while True:
        x_1,x_2=random.sample(range(-4,5),2)
        if x_1<x_2:
            break
    tap_ketqua=[
        f"$\\emptyset$",
        f"$\\mathbb{{R}}$",
        f"${{[{x_1};{x_2}]}}$",
        f"$({x_1};{x_2})$",
        f"$({x_1};{x_2}]$",
        f"$[{x_1};{x_2})$",
        f"$(-\\infty;{x_1})$",
        f"$(-\\infty;{x_1}]$",
        f"$({x_2};+\\infty)$",
        f"$[{x_2};+\\infty)$",  
        f"$(-\\infty;{x_1}) \\cup ({x_2};+\\infty)$",
        f"$(-\\infty;{x_1}) \\cup [{x_2};+\\infty)$",
        f"$(-\\infty;{x_1}] \\cup ({x_2};+\\infty)$",
        f"$(-\\infty;{x_1}] \\cup [{x_2};+\\infty)$",]

    chon_bang=random.randint(1,2)

    if chon_bang==1:
        f=-0.5*(x-x_1)*(x-x_2)
        a,b,c=-0.5,0.5*(x_1+x_2), -0.5*x_1*x_2
               
        chon=random.randint(1,4)  
        
        if chon==1:
            bpt=f"$f(x)\\ge 0$"  
            kq=f"${{[{x_1};{x_2}]}}$"
        
        if chon==2:
            bpt=f"$f(x) > 0$"        
            kq=f"$({x_1};{x_2})$"

        if chon==3:
            bpt=f"$f(x) < 0$"      
            kq=f"$(-\\infty;{x_1}) \\cup ({x_2};+\\infty)$"

        if chon==4:
            bpt=f"$f(x) \\le 0$"        
            kq=f"$(-\\infty;{x_1}] \\cup [{x_2};+\\infty)$"

    if chon_bang==2:
        f=0.5*(x-x_1)*(x-x_2)
        a,b,c=0.5,-0.5*(x_1+x_2), 0.5*x_1*x_2 
        

        chon=random.randint(1,4)  
        
        if chon==1:
            bpt=f"$f(x)\\le 0$"  
            kq=f"${{[{x_1};{x_2}]}}$"
        
        if chon==2:
            bpt=f"$f(x) < 0$"        
            kq=f"$({x_1};{x_2})$"

        if chon==3:
            bpt=f"$f(x) > 0$"      
            kq=f"$(-\\infty;{x_1}) \\cup ({x_2};+\\infty)$"

        if chon==4:
            bpt=f"$f(x) \\ge 0$"        
            kq=f"$(-\\infty;{x_1}] \\cup [{x_2};+\\infty)$" 

    kq_false=[x for x in tap_ketqua if x != kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    code_hinh=my_module.codelatex_dothi_bac_2_no_header(a,b,c)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name = my_module.pdftoimage_timename(code)
    

    noi_dung=(
        f"Cho hàm số $f(x)=ax^2+bx+c$ có đồ thị như hình vẽ."
        f" Tập nghiệm của bất phương trình {bpt} là" )

    noi_dung_loigiai=(
    f"{bpt} $\\Leftrightarrow x\\in $ {kq}."
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





#Bài 3: Phương trình quy về bậc hai
#[D10_C7_B3_01]-M2. Giải PT căn(ax^2 + bx^2 + c)=căn(dx^2 + ex + f)
def aaa_pry_L10_C7_B3_01():
	x=sp.symbols("x")
	m1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	n1 = random.randint(-5,5)
	p1 = random.randint(1,10)	

	m2 = random.randint(-5, -1)
	n2 = random.randint(-5,5)
	p2 = random.randint(1,10)

	if all([m1==m2,n1==n2,p1==p2]):
		n1=n1+random(1,3)

	if m1==-m2: m1=-m2+random.randint(1,3)

	a, b, c=m1+m2, n1+n2, p1+p2			

	f=a*x**2+b*x+c	
	
	f_trai=latex(sp.sqrt(m1*x**2+n1*x+p1))
	f_phai=latex(sp.sqrt(-m2*x**2-n2*x-p2))
	f_thu=m1*x**2+n1*x+p1

	delta,x_1,x_2=tinh_va_dau_delta(a,b,c)

	#Tạo phương án và lời giải
	if delta==">0":
		x_1_round=round(x_1,3)
		x_2_round=round(x_2,3)
		y_1=f_thu.subs(x,x_1_round)
		y_2=f_thu.subs(x,x_2_round)
		if check_so_nguyen(x_1):
			x_1=latex(my_module.hien_phan_so(x_1))
			x_2=latex(my_module.hien_phan_so(x_2))
		else:
			x_1=latex(x_1)
			x_2=latex(x_2)

		if y_1>=0 and y_2>=0:
			kq=f"${{2}}$"
			kq2=f"${{1}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"${f_trai}={f_phai}\\Rightarrow {latex(m1*x**2+n1*x+p1)}={latex(-m2*x**2-n2*x-p2)}$\n"\
				   f"$\\Rightarrow {latex(f)}=0 \\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy $x_1,x_2$ đều thỏa mãn.\n Vậy số nghiệm là: {kq}."
		elif y_1>=0 and y_2<0:
			kq=f"${{1}}$"
			kq2=f"${{2}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"${f_trai}={f_phai}\\Rightarrow {latex(m1*x**2+n1*x+p1)}={latex(-m2*x**2-n2*x-p2)}$\n"\
				   f"$\\Rightarrow {latex(f)}=0 \\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta nhận $x_1$, loại $x_2$.\n Vậy số nghiệm là: {kq}."
		elif y_1<0 and y_2>=0:
			kq=f"${{1}}$"
			kq2=f"${{2}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"${f_trai}={f_phai}\\Rightarrow {latex(m1*x**2+n1*x+p1)}={latex(-m2*x**2-n2*x-p2)}$\n"\
				   f"$\\Rightarrow {latex(f)}=0 \\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy nhận $x_2$, loại $x_1$.\n Vậy số nghiệm là: {kq}."
		else:
			kq=f"${{0}}$"
			kq2=f"${{2}}$"
			kq3=f"${{1}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"${f_trai}={f_phai}\\Rightarrow {latex(m1*x**2+n1*x+p1)}={latex(-m2*x**2-n2*x-p2)}$\n "\
				   f"$\\Rightarrow {latex(f)}=0 \\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy $x_1,x_2$ không thỏa mãn.\n Vậy số nghiệm là: {kq}."

	if delta=="=0":
		y_0=f_thu.subs(x,x_1)
		if y_0>=0:		
			kq=f"${{1}}$"
			kq2=f"${{0}}$"
			kq3=f"${{2}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"${f_trai}={f_phai}\\Rightarrow {latex(m1*x**2+n1*x+p1)}={latex(-m2*x**2-n2*x-p2)}$\n "\
				   f"$\\Rightarrow {latex(f)}=0 \\Rightarrow x={x_1}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy $x={x_1}$ thỏa mãn. Vậy số nghiệm là: {kq}." 
		else:
			kq=f"${{0}}$"
			kq2=f"${{1}}$"
			kq3=f"${{2}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"${f_trai}={f_phai}\\Rightarrow {latex(m1*x**2+n1*x+p1)}={latex(-m2*x**2-n2*x-p2)}$\n "\
				   f"$\\Rightarrow {latex(f)}=0 \\Rightarrow x={x_1}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy $x={x_1}$ không thỏa mãn. Vậy số nghiệm là: {kq}." 

	if delta=="<0":
		kq=f"${{0}}$"
		kq2=f"${{1}}$"
		kq3=f"${{2}}$"
		kq4=f"${{3}}$"

		noi_dung_loigiai=my_module.frac_to_dfrac(f"${f_trai}={f_phai}\\Rightarrow {latex(m1*x**2+n1*x+p1)}={latex(-m2*x**2-n2*x-p2)}\n "\
			   f"\\Rightarrow {latex(f)}=0$(Vô nghiệm).\n Vậy số nghiệm là: {kq}.")

		
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Số nghiệm của phương trình ${{{f_trai}={f_phai}}}$."

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

	 
	loigiai_word=my_module.frac_to_dfrac(f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n")
	loigiai_traloingan=my_module.frac_to_dfrac(f"Lời giải:\n {noi_dung_loigiai} \n")
    #Tạo đề latex

	for i in range(4):
	    list_PA[i]=list_PA[i].replace("*","\\True ")    

	debai_latex= my_module.frac_to_dfrac(f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n")

	latex_tuluan=my_module.frac_to_dfrac(f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n")
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C7_B3_02]-M2. Giải PT căn(ax^2 + bx^2 + c)=dx+e
def aaa_pry_L10_C7_B3_02(): 
	x=sp.symbols("x")
	a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	b = random.randint(-5,5)
	c = random.randint(1,10)
	if b==c==0:
		b=random.randint(1,6)
	d = random.choice([random.randint(-6, -1), random.randint(1, 7)])
	e=random.randint(-6,6)

	f_trai=latex(sp.sqrt(a*x**2+b*x+c))
	f_phai=latex(d*x+e)
	f_thu=d*x+e

	if a==d**2: a=d**2+random.randint(1,3)
	a1=a-d**2

	b1=b-2*d*e
	c1=c-e**2

	st_giai=f"${f_trai}={f_phai}\\Rightarrow {latex(a*x**2+b*x+c)}={latex(d**2*x**2+2*d*e*x+e**2)}$\n "\
			   f"$\\Rightarrow {latex(a1*x**2+b1*x+c1)}=0$" 

	delta,x_1,x_2=tinh_va_dau_delta(a1,b1,c1)
	if delta=="<0":
		kq=f"${{0}}$"
		kq2=f"${{1}}$"
		kq3=f"${{2}}$"
		kq4=f"${{3}}$"
		noi_dung_loigiai=f"{st_giai}(Vô nghiệm). Vậy số nghiệm là: {kq}."
	if delta=="=0":
		y_0=f_thu.subs(x,x_1)
		if y_0 >=0:
			kq=f"${{1}}$"
			kq2=f"${{0}}$"
			kq3=f"${{2}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"{st_giai} $\\Rightarrow x={x_1}$. Thay $x={x_1}$ vào phương trình đầu thỏa mãn. Vậy số nghiệm là: {kq}."
		else:
			kq=f"${{0}}$"
			kq2=f"${{1}}$"
			kq3=f"${{2}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"{st_giai} $\\Rightarrow x={x_1}$. Thay $x={x_1}$ vào phương trình đầu không thỏa mãn. Vậy số nghiệm là: {kq}."
	if delta==">0":
		x_1_round=round(x_1,3)
		x_2_round=round(x_2,3)
		y_1=f_thu.subs(x,x_1_round)
		y_2=f_thu.subs(x,x_2_round)
		if check_so_nguyen(x_1):			
			x_1=latex(my_module.hien_phan_so(x_1))
			x_2=latex(my_module.hien_phan_so(x_2))
		else:
			x_1=latex(x_1)
			x_2=latex(x_2)

		if y_1>=0 and y_2>=0:
			kq=f"${{2}}$"
			kq2=f"${{1}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"{st_giai}\n "\
				   f"$\\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy $x_1,x_2$ đều thỏa mãn.\n Vậy số nghiệm là: {kq}."
		elif y_1>=0 and y_2<0:
			kq=f"${{1}}$"
			kq2=f"${{2}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"{st_giai}\n "\
				   f"$\\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta nhận $x_1$, loại $x_2$.\n Vậy số nghiệm là: {kq}."
		elif y_1<0 and y_2>=0:
			kq=f"${{1}}$"
			kq2=f"${{2}}$"
			kq3=f"${{0}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"{st_giai}\n "\
				   f"$\\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy nhận $x_2$, loại $x_1$.\n Vậy số nghiệm là: {kq}."
		else:
			kq=f"${{0}}$"
			kq2=f"${{2}}$"
			kq3=f"${{1}}$"
			kq4=f"${{3}}$"
			noi_dung_loigiai=f"{st_giai}\n "\
				   f"$\\Rightarrow x_1={x_1},x_2={x_2}$.\n"\
				   f"Thử lại $x_1,x_2$ vào phương trình đầu ta thấy $x_1,x_2$ không thỏa mãn.\n Vậy số nghiệm là: {kq}."
	
		
	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Số nghiệm của phương trình ${{{f_trai}={f_phai}}}$."

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

#[D10_C7_B3_03]-SA-M4. Tìm x để tổng khoảng cách 2 sợi dây đến 2 cột bằng a
def aaa_pry_L10_C7_B3_03():
    a=random.randint(2,6)
    b=a+random.randint(1,4)
    L=random.randint(3,10)
    x=sp.symbols("x")
    f=sqrt(x**2+a**2)+sqrt((L-x)**2+b**2)
    
    x_0=a*L/(a+b)
    f_x=latex(nsimplify(f.subs(x,x_0)))

    t=float(x_0)
    if t.is_integer():
        noi_dung = (
        f"Có hai chiếc cọc có chiều cao lần lượt là {a} m và {b} m, đặt cách nhau {L} m."
        f" Chúng được buộc bởi hai sợi dây từ một cái chốt trên mặt đất nằm giữa hai chân cột tới đỉnh của mỗi cột."
        f" Gọi ${{x}}$ (m) là khoảng cách từ chốt đến chân cọc ngắn. Tìm ${{x}}$ để tổng độ dài hai dây bằng ${{{f_x}}}$."
        )
        dap_an=int(t)
    else:
        noi_dung = (
        f"Có hai chiếc cọc có chiều cao lần lượt là {a} m và {b} m, đặt cách nhau {L} m."
        f" Chúng được buộc bởi hai sợi dây từ một cái chốt trên mặt đất nằm giữa hai chân cột tới đỉnh của mỗi cột."
        f" Gọi ${{x}}$ (m) là khoảng cách từ chốt đến chân cọc ngắn. Tìm ${{x}}$ để tổng độ dài hai dây bằng ${{{f_x}}}$ (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round(t,1):.1f}".replace(".",",")


    noi_dung_loigiai=(
        f"Gọi ${{A,B,M}}$ lần lượt là đỉnh của cọc thấp, cọc cao và chốt.\n\n"
        f"$AM=\\sqrt{{x^2+{a**2}}},BM=\\sqrt{{({L}-x)^2+{b**2}}}$.\n\n"
        f"Tổng chiều dài hai dây là:\n\n"
        f"$\\sqrt{{x^2+{a**2}}}+\\sqrt{{({L}-x)^2+{b**2}}}, 0<x<{L}$.\n\n"            
        f"$\\sqrt{{x^2+{a**2}}}+\\sqrt{{({L}-x)^2+{b**2}}}={f_x}\\Rightarrow \\dfrac{{x }}{{{L}-x}}={phan_so(a/b)}\\Rightarrow x={dap_an}$."

    )

    code_hinh=(f" \\begin{{tikzpicture}}[scale=0.16, every node/.style={{font=\\small}}]\n\
    % Coordinates: A = base of short pole at x=0, B = base of tall pole at x=30.\n\
    \\coordinate (A) at (0,0);\n\
    \\coordinate (B) at (30,0);\n\
    \\def\\drawx{{10}} % stake position for visualization\n\
    \\coordinate (C) at (\\drawx,0);\n\
    \n\
    \n\
    % Tops of poles\n\
    \\coordinate (T1) at ($(A)+(0,12)$); % short pole top\n\
    \\coordinate (T2) at ($(B)+(0,28)$); % tall pole top\n\
    \n\
    \n\
    % Ground line\n\
    \\draw[thick, brown] (-2,0) -- (32,0);\n\
    \n\
    \n\
    % Poles\n\
    \\draw[line width=1.5pt, blue] (A) -- (T1);\n\
    \\draw[line width=1.5pt, green!70!black] (B) -- (T2);\n\
    \n\
    \n\
    % Wires from stake to tops\n\
    \\draw[line width=1.2pt, red] (C) -- (T1);\n\
    \\draw[line width=1.2pt, orange] (C) -- (T2);\n\
    \n\
    \n\
    % Points\n\
    \\fill[black] (A) circle (0.14) node[below=3pt] {{}};\n\
    \\fill[black] (B) circle (0.14) node[below=3pt] {{cọc cao}};\n\
    \\fill[black] (C) circle (0.14) node[below=6pt] {{chốt}};\n\
    \\fill[black] (T1) circle (0.12) node[left=2pt] {{}};\n\
    \\fill[black] (T2) circle (0.12) node[right=2pt] {{}};\n\
    \n\
    \n\
    % Height labels\n\
    \\node[left, blue] at ($(A)!0.5!(T1)$) {{{a} m}};\n\
    \\node[right, green!70!black] at ($(B)!0.5!(T2)$) {{{b} m}};\n\
    \n\
    \n\
    % Ground distances (x and 30-x)\n\
    \\draw[<->] ($(A)+(0,-1.6)$) -- ($(C)+(0,-1.6)$) node[midway, below] {{$x$ m}};\n\
\n\
\n\
\\end{{tikzpicture}}")
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)


        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C7_B3_04]-SA-M3. Tìm x để quãng đường AC = t*quãng đường BC.
def aaa_pry_L10_C7_B3_04():
    import random
    import sympy as sp

    x = sp.symbols("x", real=True)

    ten = random.choice([
        "An", "Bình", "Châu", "Dương", "Hà",
        "Lan", "Minh", "Nam", "Quân", "Trang"
    ])

    # ----------------- SINH DỮ LIỆU NGẪU NHIÊN -----------------
    while True:


        NC = random.randint(8, 15)   # khoảng cách NC (m)
        k = random.randint(2, 5)     # đoạn AB (m)

        # t là tỉ số AC = t*BC
        # sinh t dạng phân số đơn giản p/q
        p = random.randint(1, 5)
        q = random.randint(p+1, 8)   # đảm bảo t<1
        t = p/q

        # AC^2 và BC^2 theo mô hình toạ độ
        AC2 = x**2 - NC*x + NC**2
        BC2 = (x + k)**2 - NC*(x + k) + NC**2

        # AC = t BC  -> AC^2 = t^2 BC^2
        eq = sp.Eq(AC2, t**2 * BC2)

        # giải nghiệm x dương
        sols = sp.solve(eq, x)
        sols_real_pos = []
        for s in sols:
            if s.is_real:
                val = float(s)
                if val > 0:
                    sols_real_pos.append(val)

        if sols_real_pos:
            x_val = min(sols_real_pos)
        else:
            # fallback an toàn
            x_val = 0
        if x_val>=1:
            break

    # làm tròn 2 chữ số
    x_rounded = round_half_up(x_val, 1)
    dap_an = f"{x_rounded:.1f}".replace(".", ",")

    # ----------------- NỘI DUNG -----------------

    s_t = f"{p}/{q}".replace("/", "\\over ")
    s_k = str(k)
    s_NC = str(NC)

    noi_dung = (
        f"Khoảng cách từ nhà {ten} ở vị trí ${{N}}$ đến cột điện ${{C}}$ là {NC} m. "
        f"Từ nhà, {ten} đi ${{x}}$ mét theo phương tạo với ${{NC}}$ một góc $60^\\circ$ đến vị trí ${{A}}$, "
        f"sau đó đi tiếp {s_k} m theo cùng phương đó đến vị trí ${{B}}$ (như hình bên). "
        f"Tìm ${{x}}$ để $AC = {phan_so(t)}BC$ (kết quả làm tròn đến hàng phần mười mét)."
    )

    # ----------------- LỜI GIẢI -----------------

    noi_dung_loigiai = (
        f"$AC =\\sqrt{{x^2 - {s_NC}x + {s_NC}^2}} ,\\quad "
        f"BC = \\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2}}.$\n\n"
        f"Theo giả thiết $AC = {phan_so(t)}BC$ nên $AC^2 = {phan_so(t**2)} BC^2$.\n\n"
        f"Giải phương trình ta được $x \\approx {dap_an}$ (m)."    )

    # ----------------- KẾT QUẢ TRẢ VỀ -----------------
    code_hinh=(f" \\begin{{tikzpicture}}[smooth,scale=1.2]\n\
            \\path\n\
            (0,0) coordinate (N)\n\
            (3,0) coordinate (C)\n\
            ($(N)!1.2!60:(C)$) coordinate (B)\n\
            ($(B)!0.3!(N)$) coordinate (A);\n\
            \\draw (N)--(C)--(B)--cycle (C)--(A)\n\
            pic[draw, angle radius=4mm]{{angle=C--N--B}};\n\
            \\path \n\
            (N)--(A) node[left,midway,scale=.8]{{$x$ }}\n\
            (A)--(B) node[above,midway,sloped,scale=.8]{{${s_k}$ }}\n\
            (N)--(C) node[above,midway,sloped,scale=.8]{{${NC}$ }};\n\
            \\foreach \\x/\\g in {{A/-160,N/-90,C/-90,B/90}} \\draw[fill=black] (\\x) circle (.05) +(\\g:.3) node{{$\\x$}};\n\
    \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai_word = f"{noi_dung}\n{file_name}\n"

    loigiai_word = (
        f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n"
    )

    latex_tuluan = (
        f"\\begin{{ex}}\n {noi_dung}\n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\n\n\\shortans[4]{{{dap_an}}}\n\n"
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n"
    )

    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C7_B3_05]-SA-M3. Tìm x để quãng đường BC = t*quãng đường AN.
def aaa_pry_L10_C7_B3_05():
    import random
    import sympy as sp

    x = sp.symbols("x", real=True)

    ten = random.choice([
        "An", "Bình", "Châu", "Dương", "Hà",
        "Lan", "Minh", "Nam", "Quân", "Trang"
    ])

    # --- SINH DỮ LIỆU ---
    while True:
        NC = random.randint(8, 15)  # NC (m)
        k = random.randint(2, 5)    # AB (m)

        # sinh t dạng p/q
        p = random.randint(1, 8)
        q = random.randint(1, 8)
        t = sp.Rational(p, q)

        # AN = x
        AN = x

        # BC^2 theo mô hình toạ độ
        BC2 = (x + k)**2 - NC*(x + k) + NC**2

        # BC = t * AN => BC^2 = t^2 * x^2
        eq = sp.Eq(BC2, (t**2) * x**2)

        sols = sp.solve(eq, x)
        sols_real_pos = []

        for s in sols:
            if s.is_real:
                val = float(s)
                if val > 0:
                    sols_real_pos.append(val)

        if sols_real_pos:
            x_val = min(sols_real_pos)
        else:
            x_val = 0  # fallback an toàn

        if x_val>1:
            break

    x_rounded = round_half_up(x_val, 1)
    dap_an = f"{x_rounded:.1f}".replace(".", ",")

    # --- format hiển thị ---
    s_t = phan_so(p/q)
    s_k = str(k)
    s_NC = str(NC)

    noi_dung = (
        f"Khoảng cách từ nhà {ten} ở vị trí ${{N}}$ đến cột điện ${{C}}$ là {NC} m. "
        f"Từ nhà, {ten} đi ${{x}}$ mét theo phương tạo với ${{NC}}$ một góc $60^\\circ$ đến vị trí ${{A}}$, "
        f"sau đó đi tiếp {s_k} m theo cùng phương đó đến vị trí ${{B}}$ (như hình bên). "
        f"Tìm $x$ để $BC = {s_t}AN$ (kết quả làm tròn đến hàng phần mười mét)."
    )

    noi_dung_loigiai = (
        f"$AN = x$.\n\n"
        f"$BC =\\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2 }}.$\n\n"
        f"Theo giả thiết $BC = {s_t}AN$ nên:\n\n"
        f"$BC^2 = {phan_so(p**2/q**2)} x^2 \\Rightarrow (x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2={phan_so(p**2/q**2)} x^2$.\n\n"
        f"Giải phương trình theo $x$ ta được $x \\approx {dap_an}$ (m)."

    )

    code_hinh=(f" \\begin{{tikzpicture}}[smooth,scale=1.2]\n\
            \\path\n\
            (0,0) coordinate (N)\n\
            (3,0) coordinate (C)\n\
            ($(N)!1.2!60:(C)$) coordinate (B)\n\
            ($(B)!0.3!(N)$) coordinate (A);\n\
            \\draw (N)--(C)--(B)--cycle (C)--(A)\n\
            pic[draw, angle radius=4mm]{{angle=C--N--B}};\n\
            \\path \n\
            (N)--(A) node[left,midway,scale=.8]{{$x$ }}\n\
            (A)--(B) node[above,midway,sloped,scale=.8]{{${s_k}$ }}\n\
            (N)--(C) node[above,midway,sloped,scale=.8]{{${NC}$ }};\n\
            \\foreach \\x/\\g in {{A/-160,N/-90,C/-90,B/90}} \\draw[fill=black] (\\x) circle (.05) +(\\g:.3) node{{$\\x$}};\n\
    \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai_word = f"{noi_dung}\n{file_name}\n"
    loigiai_word = (
        f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n"
    )
    latex_tuluan = (
        f"\\begin{{ex}}\n {noi_dung}\n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\n\n\\shortans[4]{{{dap_an}}}\n\n"
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n"
    )

    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C7_B3_06]-M2. Tính tổng các nghiệm của phương trình căn (ax^2+bx+c)=d
def aaa_pry_L10_C7_B3_06():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-4, 4) if i!=0])
        b = random.choice([i for i in range(-6, 7) if i!=0])
        c=random.randint(-5,5)
        d=random.randint(1,6)
        c1=c-d**2
        delta=b**2-4*a*c1
        if delta>0:
            break
    f=a*x**2+b*x+c

    chon=random.randint(1,2)
    if chon==1:
        noi_dung=(
        f"Tính tổng các nghiệm của phương trình ${latex(sqrt(f))}={d}$ là"
        )
    
    if chon==2:
        noi_dung=(
        f"Tính tổng các nghiệm của phương trình ${latex(sqrt(f))}-{d}=0$ là"
        )

    noi_dung=noi_dung.replace("--","+") 


    kq=-b/a
    kq_false = set()
    while len(kq_false) < 4:    
        numbers = round(random.uniform(-b/a-5, -b/a+5),1)
        if numbers!=kq:
            kq_false.add(numbers)

    kq_false=list(kq_false)
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    if a>0:

        noi_dung_loigiai=(
        f"${latex(sqrt(f))}={d}\\Rightarrow {latex(a*x**2+b*x+c)}={d**2} \\Rightarrow {latex(a*x**2+b*x+c-d**2)}=0$.\n\n"
        f"Phương trình có 2 nghiệm $x_1,x_2$ thì $x_1+x_2=-\\dfrac{{{b}}}{{2.{a}}}={phan_so(-b/a)}$."
        )
    else:
        noi_dung_loigiai=(
        f"${latex(sqrt(f))}={d}\\Rightarrow {latex(a*x**2+b*x+c)}={d**2} \\Rightarrow {latex(a*x**2+b*x+c-d**2)}=0$.\n\n"
        f"Phương trình có 2 nghiệm $x_1,x_2$ thì: $x_1+x_2=-\\dfrac{{{b}}}{{2.({a})}}={phan_so(-b/a)}$."
        )


    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{phan_so(kq2)}}}$"
    pa_C= f"${{{phan_so(kq3)}}}$"
    pa_D= f"${{{phan_so(kq4)}}}$"
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

#[D10_C7_B3_07]-M2. Tập nghiệm PT căn(ax^2+b)=căn(cx+d)
def aaa_pry_L10_C7_B3_07():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-5, 5) if i!=0])
        b = random.choice([i for i in range(-6, 7) if i!=0])
        c = random.choice([i for i in range(-6, 7) if i!=0])
        d = random.choice([i for i in range(-6, 7) if i!=0])
        a1,b1,c1=a,-c,b-d
        delta=b1**2-4*a1*c1
        if delta<=0:
            continue
        x_1=(-b1-sqrt(delta))/(2*a1)
        x_2=(-b1+sqrt(delta))/(2*a1)
        f,g = a*x**2+b, c*x+d
        g_1,g_2=g.subs(x,x_1), g.subs(x,x_2)

        if all([delta>0,g_1>=0,g_2>=0]):
            break
        
    chon=random.randint(1,2)
    if chon==1:
        noi_dung=(
        f"Tập nghiệm của phương trình ${latex(sqrt(f))}={latex(sqrt(g))}$ là"
        )
    
    if chon==2:
        noi_dung=(
        f"Tập nghiệm của phương trình ${latex(sqrt(f))}-{latex(sqrt(g))}=0$ là"
        )
    
    

    kq=f"$S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$"
    kq_false=[
    f"$S=\\left({latex(x_1)};{latex(x_2)} \\right)$",
    f"$S=\\left({latex(x_1)};{latex(x_2)} \\right]$",
    f"$S=\\left[{latex(x_1)};{latex(x_2)} \\right]$",
    f"$S=\\left\\{{{latex(x_1)} \\right\\}}$",
    f"$S=\\left\\{{{latex(x_2)} \\right\\}}$",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${latex(sqrt(f))}={latex(sqrt(g))} \\Rightarrow {latex(f)}={latex(g)} \\Rightarrow {latex(f-g)}=0$\n\n"
    f"$\\Rightarrow x={latex(x_1)}, x={latex(x_2)}$.\n\n"
    f"Thay vào PT đã cho ta được tập nghiệm: $S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$."
    )

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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

#[D10_C7_B3_08]-M2. Tập nghiệm PT căn(ax+b)=x+d
def aaa_pry_L10_C7_B3_08():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-8, 8) if i!=0])
        b = random.choice([i for i in range(-8, 8) if i!=0])            
        d = random.choice([i for i in range(-8, 8) if i!=0])       
        a1,b1,c1=1,2*d-a,d**2-b        
        delta=b1**2-4*a1*c1
        if delta<=0:
            continue
        x_1=(-b1-sqrt(delta))/(2*a1)
        x_2=(-b1+sqrt(delta))/(2*a1)
        f,g = a*x+b, x+d
        g_1,g_2=g.subs(x,x_1), g.subs(x,x_2)

        if all([delta>0,g_1>=0,g_2>=0]):
            break  
     
    chon=random.randint(1,4)
    if chon==1:
        noi_dung=(f"Tập nghiệm của phương trình ${latex(sqrt(f))}={latex(g)}$ là")

    if chon==2:
        noi_dung=(f"Tập nghiệm của phương trình ${latex(sqrt(f))}-{d}=x$ là")

    if chon==3:
        noi_dung=(f"Tập nghiệm của phương trình ${latex(sqrt(f))}-x={d}$ là")

    if chon==4:
        noi_dung=(f"Tập nghiệm của phương trình ${latex(sqrt(f))}-x-{d}=0$ là")
        
    noi_dung=noi_dung.replace("--","+") 

    kq=f"$S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$"
    kq_false=[
    f"$S=\\left({latex(x_1)};{latex(x_2)} \\right)$",
    f"$S=\\left({latex(x_1)};{latex(x_2)} \\right]$",
    f"$S=\\left[{latex(x_1)};{latex(x_2)} \\right]$",
    f"$S=\\left\\{{{latex(x_1)} \\right\\}}$",
    f"$S=\\left\\{{{latex(x_2)} \\right\\}}$",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${latex(sqrt(f))}={latex(g)} \\Rightarrow {latex(f)}={latex(g**2)} \\Rightarrow {latex(expand(f-g**2))}=0$\n\n"
    f"$\\Rightarrow x={latex(x_1)}, x={latex(x_2)}$.\n\n"
    f"Thay vào PT đã cho ta được tập nghiệm: $S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$."
    )

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
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

#[D10_C7_B3_09]-M2. Tính tổng các nghiệm PT căn(ax+b)=x+d
def aaa_pry_L10_C7_B3_09():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-8, 8) if i!=0])
        b = random.choice([i for i in range(-8, 8) if i!=0])            
        d = random.choice([i for i in range(-8, 8) if i!=0])       
        a1,b1,c1=1, 2*d-a, d**2-b        
        delta = b1**2-4*a1*c1
        if delta<=0:
            continue
        x_1=(-b1-sqrt(delta))/(2*a1)
        x_2=(-b1+sqrt(delta))/(2*a1)
        f,g = a*x+b, x+d
        g_1,g_2=g.subs(x,x_1), g.subs(x,x_2)

        if all([delta>0,g_1>=0,g_2>=0]):
            break
    chon=random.randint(1,4)
    if chon==1:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}={latex(g)}$ là")

    if chon==2:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}-{d}=x$ là")

    if chon==3:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}-x={d}$ là")

    if chon==4:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}-x-{d}=0$ là")

    noi_dung=noi_dung.replace("--","+")  
     
    

    kq=-b1/a1
    kq_false = set()
    while len(kq_false) < 4:
    
        numbers = round(random.uniform(kq-random.randint(1,5), kq+random.randint(1,5)),1)
        if numbers!=kq:
            kq_false.add(numbers)
    kq_false=list(kq_false)

    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${latex(sqrt(f))}={latex(g)} \\Rightarrow {latex(f)}={latex(g**2)} \\Rightarrow {latex(expand(f-g**2))}=0$\n\n"
    f"$\\Rightarrow x={latex(x_1)}, x={latex(x_2)}$.\n\n"
    f"Thay vào PT đã cho ta được tập nghiệm: $S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$.\n\n"
    f"Tổng các nghiệm bằng ${{{phan_so(kq)}}}$."
    )

    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{phan_so(kq2)}}}$"
    pa_C= f"${{{phan_so(kq3)}}}$"
    pa_D= f"${{{phan_so(kq4)}}}$"
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

#[D10_C7_B3_10]-TF-M2. PT căn(ax+b)=x+d. Xét Đ-S: Điều kiện, bình phương, nghiệm, tổng-tích các nghiệm
def aaa_pry_L10_C7_B3_10():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-8, 8) if i!=0])
        b = random.choice([i for i in range(-8, 8) if i!=0])            
        d = random.choice([i for i in range(-8, 8) if i!=0])       
        a1,b1,c1=1,2*d-a,d**2-b        
        delta=b1**2-4*a1*c1
        if delta<=0:
            continue
        x_1=(-b1-sqrt(delta))/(2*a1)
        x_2=(-b1+sqrt(delta))/(2*a1)
        f,g = a*x+b, x+d
        g_1,g_2=g.subs(x,x_1), g.subs(x,x_2)

        if all([delta>0,g_1>=0,g_2>=0]):
            break  
     

    noi_dung=(f"Cho phương trình ${latex(sqrt(f))}={latex(g)}$ (1).")
    
    noi_dung+=f" Xét tính đúng-sai của các khẳng định sau"
        
    noi_dung=noi_dung.replace("--","+")

    noi_dung+=  f"Xét tính đúng-sai của các khẳng định sau:"  
    
    kq1_T=f"* Nếu $x_0$ là một nghiệm của phương trình (1) thì $x_0+{d}\\ge 0$" 
    kq1_F=f"Nếu $x_0$ là một nghiệm của phương trình (1) thì $x_0+{d}\\le 0$"
    
    HDG=f"Nếu $x_0$ là một nghiệm của phương trình (1) thì $x_0+{d}\\ge 0$."
    HDG=thay_dau_congtru(HDG)
    kq1=random.choice([kq1_T, kq1_F])
    kq1=thay_dau_congtru(kq1)
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Bình phương hai vế và rút gọn ta được phương trình ${latex(expand(f-g**2))}=0$"
    kq2_F=f"Bình phương hai vế và rút gọn ta được phương trình ${latex(expand(f-g**2+random.randint(1,5)))}=0$"
    
    HDG=f"Bình phương hai vế và rút gọn ta được phương trình ${latex(expand(f-g**2))}=0$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Phương trình (1) có các nghiệm là $x={latex(x_1)},x={latex(x_2)}$" 
    kq3_F=random.choice([
        f"Phương trình (1) có nghiệm duy nhất là $x={latex(x_1)}$",
        f"Phương trình (1) có nghiệm duy nhất là $x={latex(x_2)}$",
        f"Phương trình (1) vô nghiệm",  ])
    
    HDG=(f"${latex(sqrt(f))}={latex(g)} \\Rightarrow {latex(f)}={latex(g**2)} \\Rightarrow {latex(expand(f-g**2))}=0$\n\n"
    f"$\\Rightarrow x={latex(x_1)}, x={latex(x_2)}$.\n\n"
    f"Thay vào PT đã cho ta được tập nghiệm: $S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        kq4_T=f"* Tổng các nghiệm của phương trình bằng ${{{phan_so(-b1/a1)}}}$"
        kq4_F=f"Tổng các nghiệm của phương trình bằng ${{{phan_so(-b1/a1+random.randint(1,4))}}}$" 
        
        HDG=f"$x_1+x_2={latex(x_1)}+{latex(x_2)}={phan_so(-b1/a1)}$."
    
    if chon==2:
        kq4_T=f"* Tích các nghiệm của phương trình bằng ${{{phan_so(c1/a1)}}}$"
        kq4_F=f"Tích các nghiệm của phương trình bằng ${{{phan_so(c1/a)}}}$" 
        
        HDG=f"$x_1.x_2=({latex(x_1)}).({latex(x_2)})={phan_so(c1/a1)}$."

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

#[D10_C7_B3_11]-TF-M2. PT căn(ax+b)=cx+d. Xét Đ-S: Điều kiện, bình phương, nghiệm, tổng-tích các nghiệm
def aaa_pry_L10_C7_B3_11():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-8, 8) if i!=0])
        b = random.choice([i for i in range(-8, 8) if i!=0])
        c = random.choice([i for i in range(-4, 5) if i!=0])         
        d = random.choice([i for i in range(-8, 8) if i!=0])       
        a1,b1,c1=c, 2*c*d-a, d**2-b      
        delta=b1**2-4*a1*c1
        if delta<=0:
            continue
        x_1=(-b1-sqrt(delta))/(2*a1)
        x_2=(-b1+sqrt(delta))/(2*a1)
        f,g = a*x+b, c*x+d
        g_1,g_2=g.subs(x,x_1), g.subs(x,x_2)

        if all([delta>0,g_1>=0,g_2>=0]):
            break  
     

    noi_dung=(f"Cho phương trình ${latex(sqrt(f))}={latex(g)}$ (1).")
    
    noi_dung+=f" Xét tính đúng-sai của các khẳng định sau"
        
    noi_dung=noi_dung.replace("--","+")

    noi_dung+=  f"Xét tính đúng-sai của các khẳng định sau:"  
    
    kq1_T=f"* Nếu $x_0$ là một nghiệm của phương trình (1) thì ${c}x_0+{d}\\ge 0$" 
    kq1_F=f"Nếu $x_0$ là một nghiệm của phương trình (1) thì ${c}x_0+{d}\\le 0$"
    
    HDG=f"Nếu $x_0$ là một nghiệm của phương trình (1) thì ${c}x_0+{d}\\ge 0$."
    HDG=thay_dau_congtru(HDG)
    kq1=random.choice([kq1_T, kq1_F])
    kq1=thay_dau_congtru(kq1)
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Bình phương hai vế và rút gọn ta được phương trình ${latex(expand(f-g**2))}=0$"
    kq2_F=f"Bình phương hai vế và rút gọn ta được phương trình ${latex(expand(f-g**2+random.randint(1,5)))}=0$"
    
    HDG=f"Bình phương hai vế và rút gọn ta được phương trình ${latex(expand(f-g**2))}=0$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Phương trình (1) có các nghiệm là $x={latex(x_1)},x={latex(x_2)}$" 
    kq3_F=random.choice([
        f"Phương trình (1) có nghiệm duy nhất là $x={latex(x_1)}$",
        f"Phương trình (1) có nghiệm duy nhất là $x={latex(x_2)}$",
        f"Phương trình (1) vô nghiệm",  ])
    
    HDG=(f"${latex(sqrt(f))}={latex(g)} \\Rightarrow {latex(f)}={latex(g**2)} \\Rightarrow {latex(expand(f-g**2))}=0$\n\n"
    f"$\\Rightarrow x={latex(x_1)}, x={latex(x_2)}$.\n\n"
    f"Thay vào PT đã cho ta được tập nghiệm: $S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        kq4_T=f"* Tổng các nghiệm của phương trình bằng ${{{phan_so(-b1/a1)}}}$"
        kq4_F=f"Tổng các nghiệm của phương trình bằng ${{{phan_so(-b1/a1+random.randint(1,4))}}}$" 
        
        HDG=f"$x_1+x_2={latex(x_1)}+{latex(x_2)}={phan_so(-b1/a1)}$."
    
    if chon==2:
        kq4_T=f"* Tích các nghiệm của phương trình bằng ${{{phan_so(c1/a1)}}}$"
        kq4_F=f"Tích các nghiệm của phương trình bằng ${{{phan_so(c1/a)}}}$" 
        
        HDG=f"$x_1.x_2=({latex(x_1)}).({latex(x_2)})={phan_so(c1/a1)}$."

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

#[D10_C7_B3_12]-M2. Tính tổng các nghiệm PT căn(ax+b)=cx+d
def aaa_pry_L10_C7_B3_12():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-8, 8) if i!=0])
        b = random.choice([i for i in range(-8, 8) if i!=0])
        c = random.choice([i for i in range(-4, 5) if i!=0])         
        d = random.choice([i for i in range(-8, 8) if i!=0])       
        a1,b1,c1=c, 2*c*d-a, d**2-b      
        delta=b1**2-4*a1*c1
        if delta<=0:
            continue
        x_1=(-b1-sqrt(delta))/(2*a1)
        x_2=(-b1+sqrt(delta))/(2*a1)
        f,g = a*x+b, c*x+d
        g_1,g_2=g.subs(x,x_1), g.subs(x,x_2)

        if all([delta>0,g_1>=0,g_2>=0]):
            break
    chon=random.randint(1,4)
    if chon==1:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}={latex(g)}$ là")

    if chon==2:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}-{d}={c}x$ là")

    if chon==3:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}-{c}x={d}$ là")

    if chon==4:
        noi_dung=(f"Tổng các nghiệm của phương trình ${latex(sqrt(f))}-{c}x-{d}=0$ là")

    noi_dung=noi_dung.replace("--","+").replace("1x","x").replace("-1x","-x") 
    

    kq=-b1/a1
    kq_false = set()
    while len(kq_false) < 4:
    
        numbers = round(random.uniform(kq-random.randint(1,5), kq+random.randint(1,5)),1)
        if numbers!=kq:
            kq_false.add(numbers)
    kq_false=list(kq_false)

    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${latex(sqrt(f))}={latex(g)} \\Rightarrow {latex(f)}={latex(g**2)} \\Rightarrow {latex(expand(f-g**2))}=0$\n\n"
    f"$\\Rightarrow x={latex(x_1)}, x={latex(x_2)}$.\n\n"
    f"Thay vào PT đã cho ta được tập nghiệm: $S=\\left\\{{{latex(x_1)};{latex(x_2)} \\right\\}}$."
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("--","+").replace("1x","x").replace("-1x","-x")

    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{phan_so(kq2)}}}$"
    pa_C= f"${{{phan_so(kq3)}}}$"
    pa_D= f"${{{phan_so(kq4)}}}$"
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

#[D10_C7_B3_13]-TF-M3. Bài toán đúng-sai về quãng đường đi hình tam giác.
def aaa_pry_L10_C7_B3_13():
    import random
    import sympy as sp

    x = sp.symbols("x", real=True)

    ten = random.choice([
        "An", "Bình", "Châu", "Dương", "Hà",
        "Lan", "Minh", "Nam", "Quân", "Trang"
    ])

    # ----------------- SINH DỮ LIỆU NGẪU NHIÊN -----------------
    while True:


        NC = random.randint(8, 15)   # khoảng cách NC (m)
        k = random.randint(2, 5)     # đoạn AB (m)

        # t là tỉ số AC = t*BC
        # sinh t dạng phân số đơn giản p/q
        p = random.randint(1, 5)
        q = random.randint(p+1, 8)   # đảm bảo t<1
        t = p/q

        # AC^2 và BC^2 theo mô hình toạ độ
        AC2 = x**2 - NC*x + NC**2
        BC2 = (x + k)**2 - NC*(x + k) + NC**2

        # AC = t BC  -> AC^2 = t^2 BC^2
        eq = sp.Eq(AC2, t**2 * BC2)

        # giải nghiệm x dương
        sols = sp.solve(eq, x)
        sols_real_pos = []
        for s in sols:
            if s.is_real:
                val = float(s)
                if val > 0:
                    sols_real_pos.append(val)

        if sols_real_pos:
            x_val = min(sols_real_pos)
        else:
            # fallback an toàn
            x_val = 0
        if x_val>=1:
            break

    # làm tròn 2 chữ số
    x_rounded = round_half_up(x_val, 1)
    s_x = f"{x_rounded:.1f}".replace(".", ",")
    s_x_f = f"{round_half_up(x_val+random.randint(1,2), 1):.1f}".replace(".", ",")

    # ----------------- NỘI DUNG -----------------

    s_t = f"{p}/{q}".replace("/", "\\over ")
    s_k = str(k)
    s_NC = str(NC)

    noi_dung = (
        f"Khoảng cách từ nhà {ten} ở vị trí ${{N}}$ đến cột điện ${{C}}$ là {NC} m. "
        f"Từ nhà, {ten} đi ${{x}}$ mét theo phương tạo với ${{NC}}$ một góc $60^\\circ$ đến vị trí ${{A}}$, "
        f"sau đó đi tiếp {s_k} m theo cùng phương đó đến vị trí ${{B}}$ (như hình bên). "
        f" Biết rằng $AC = {phan_so(t)}BC$."
        f" Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười mét):"
    )

    # ----------------- LỜI GIẢI -----------------

    
    kq1_T=f"* $AC =\\sqrt{{x^2 - {s_NC}x + {s_NC}^2}}$" 
    kq1_F=f"$AC =\\sqrt{{x^2 +{s_NC}x + {s_NC}^2}}$"
    
    HDG=f"Áp dụng định lí cosin ta có: $AC =\\sqrt{{x^2 - {s_NC}x + {s_NC}^2}}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* $BC = \\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2}}$"
    kq2_F=f"$BC = \\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2}}$"
    
    HDG=f"Áp dụng định lí cosin ta có: $BC = \\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $\\sqrt{{x^2 - {s_NC}x + {s_NC}^2}}={phan_so(t)}\\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2}}$" 
    kq3_F=f"$\\sqrt{{x^2 +{s_NC}x + {s_NC}^2}}={phan_so(t)}\\sqrt{{(x+{s_k})^2 + {s_NC}(x+{s_k}) + {s_NC}^2}}$"
    
    HDG=f"$\\sqrt{{x^2 - {s_NC}x + {s_NC}^2}}={phan_so(t)}\\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2}}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Để $AC = {phan_so(t)}BC$ thì $x \\approx {s_x}$"
    kq4_F=f"Để $AC = {phan_so(t)}BC$ thì $x \\approx {s_x_f}$" 
    
    HDG=(
        f"$AC =\\sqrt{{x^2 - {s_NC}x + {s_NC}^2}} ,\\quad "
        f"BC = \\sqrt{{(x+{s_k})^2 - {s_NC}(x+{s_k}) + {s_NC}^2}}.$\n\n"
        f"Theo giả thiết $AC = {phan_so(t)}BC$ nên $AC^2 = {phan_so(t**2)} BC^2$.\n\n"
        f"Giải phương trình ta được $x \\approx {s_x}$ (m).")
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)


    code_hinh=(f" \\begin{{tikzpicture}}[smooth,scale=1.2]\n\
            \\path\n\
            (0,0) coordinate (N)\n\
            (3,0) coordinate (C)\n\
            ($(N)!1.2!60:(C)$) coordinate (B)\n\
            ($(B)!0.3!(N)$) coordinate (A);\n\
            \\draw (N)--(C)--(B)--cycle (C)--(A)\n\
            pic[draw, angle radius=4mm]{{angle=C--N--B}};\n\
            \\path \n\
            (N)--(A) node[left,midway,scale=.8]{{$x$ }}\n\
            (A)--(B) node[above,midway,sloped,scale=.8]{{${s_k}$ }}\n\
            (N)--(C) node[above,midway,sloped,scale=.8]{{${NC}$ }};\n\
            \\foreach \\x/\\g in {{A/-160,N/-90,C/-90,B/90}} \\draw[fill=black] (\\x) circle (.05) +(\\g:.3) node{{$\\x$}};\n\
    \\end{{tikzpicture}}")
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

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