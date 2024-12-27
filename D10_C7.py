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
	a = random.choice([random.randint(-4, -1), random.randint(1, 4)])
	c = random.choice([random.randint(-4, -1), random.randint(1, 4)])
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
	c= b**2/(4*a)

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

	code_bxd = my_module.codelatex_bxd_bac2(a,b,c)
	code = my_module.moi_truong_anh_latex(code_bxd)
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
		kq3= random.choice([f"$S=\\left({x_1};{x_2}\\right)$"])
		kq4= random.choice([f"$S=\\left[{x_1};{x_2}\\right]$",f"$S=\\mathbb{{R}}$"])
		noi_dung_loigiai=f"Hàm số xác định khi ${latex(f)} \\ge 0 \\Leftrightarrow x\\le {x_1}$ hoặc $x\\ge {x_2}$.\n\n"\
		f" Tập xác định là: {kq}." 

	if a<0:		
		kq= f"$S=\\left[{x_1};{x_2}\\right]$" 
		kq2= f"$S=\\left(-\\infty;{x_1}\\right) \\cup \\left({x_2};+\\infty\\right)$" 
		kq3= random.choice([f"$S=\\left(-\\infty;{x_1}\\right] \\cup \\left[{x_2};+\\infty\\right)$"])
		kq4= random.choice([f"$S=\\left({x_1};{x_2}\\right)$" ,f"$S=\\mathbb{{R}}$"])
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

