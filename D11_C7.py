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
def thay_dau_congtru(st):
    ketqua=st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("+ +","+").replace("+ -","-").replace("- -","+").replace("- +","-")
    return ketqua

#Tìm UCLN của hai số
def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return a

#Tìm UCLN của ba số
def ucln_ba_so(a, b, c):
    ucln_ab = tim_ucln(a, b)
    ucln_abc = tim_ucln(ucln_ab, c)
    return ucln_abc

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

#Bài 1-Định nghĩa đạo hàm
#[D11_C7_B1_01]-M1. Tìm khẳng định đúng về đạo hàm tại điểm của f(x)
def ui5io_L11_C7_B1_01():
    x=sp.symbols("x")
    x_0= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    
    kq= f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)-f({x_0})}}{{{latex(x-x_0)}}}$"
    kq2=f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)-f({x_0})}}{{{latex(x+x_0)}}}$"
    kq3=f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)+f({x_0})}}{{{latex(x-x_0)}}}$"
    kq4=f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)+f({x_0})}}{{{latex(x+x_0)}}}$"
   
    kq= f"{kq}"
    kq2=f"{kq2}"
    kq3=f"{kq3}"
    kq4=f"{kq4}"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $y=f(x)$ xác định trên khoảng $K$ và $x_0={x_0}\\in K$. Tìm khẳng định đúng."
    noi_dung_loigiai=f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)-f({x_0})}}{{{latex(x-x_0)}}}$."

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B1_02]-M2. Cho hàm số đa thức. Biễu diễn công thức đạo hàm tại x_0
def ui5io_L11_C7_B1_02():
    x=sp.symbols("x")
    x_0= random.choice([random.randint(-10, -1), random.randint(1, 10)])

    k=random.randint(2,4)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    f_x0=f.subs(x,x_0)
    
    kq=my_module.thay_dau_congtru(f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)-{f_x0}}}{{{latex(x-x_0)}}}$")
    kq2=my_module.thay_dau_congtru(f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)-{f_x0}}}{{{latex(x+x_0)}}}$")
    kq3=my_module.thay_dau_congtru(f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)+{f_x0}}}{{{latex(x-x_0)}}}$")
    kq4=my_module.thay_dau_congtru(f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)+{f_x0}}}{{{latex(x+x_0)}}}$")
   
    kq= f"{kq}"
    kq2=f"{kq2}"
    kq3=f"{kq3}"
    kq4=f"{kq4}"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $y=f(x)={latex(f)}$ và $x_0={x_0}$. Tìm khẳng định đúng."
    noi_dung_loigiai=my_module.thay_dau_congtru(f"$\\displaystyle f'({x_0})=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)-f({x_0})}}{{{latex(x-x_0)}}}=\\lim_{{x \\rightarrow {x_0}}} \\dfrac{{f(x)-{f_x0}}}{{{latex(x-x_0)}}}$.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_01]-M2. Tính đạo hàm hàm số đa thức.
def ui5io_L11_C7_B2_01():
    x=sp.symbols("x")
    k=random.randint(2,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k)) 
    kq= diff(f, x)
    kq2=diff(f, x)+ random.randint(1,10)
    kq3=diff(f, x) + random.randint(1,10)*x
    kq4=diff(f, x) + random.randint(1,10)*x**2

   
    kq= f"$y'={latex(kq)}$"
    kq2=f"$y'={latex(kq2)}$"
    kq3=f"$y'={latex(kq3)}$"
    kq4=f"$y'={latex(kq4)}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính đạo hàm của hàm số $y={latex(f)}$."
    noi_dung_loigiai=f"$y'=({latex(f)})'={latex(diff(f, x))}$ ."

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_02]-M2. Tính đạo hàm hàm số đa thức + a/x.
def ui5io_L11_C7_B2_02():
    x=sp.symbols("x")
    k=random.randint(2,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
    b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = sum(a[i]* x**i for i in range(k)) + b/x
    kq= diff(f, x)
    kq2=diff(f, x)+ b/x + b/x**2
    kq3=diff(f, x) - b/x + b/x**2
    kq4=diff(f, x) + b/x**2 + b/x**2

   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2= my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3= my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4= my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$.")
    noi_dung_loigiai=my_module.frac_to_dfrac(f"$y'=({latex(f)})'={latex(diff(f, x))}$.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_03]-M2. Tính đạo hàm hàm số đa thức + acăn(x).
def ui5io_L11_C7_B2_03():
    x=sp.symbols("x")
    k=random.randint(2,4)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
    b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = sum(a[i]* x**i for i in range(k)) + b*sqrt(x)
    kq= diff(f, x)
    kq2=diff(f, x)+ b*sqrt(x) - diff(b*sqrt(x), x)
    kq3=diff(f, x) + b/sqrt(x) - diff(b*sqrt(x), x)
    kq4=diff(f, x) + b*sqrt(x)/2 - diff(b*sqrt(x), x)

   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2= my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3= my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4= my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$.")
    noi_dung_loigiai=my_module.frac_to_dfrac(f"$y'=({latex(f)})'={latex(diff(f, x))}$.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_04]-M3. Tính đạo hàm hàm số đa thức + acăn(x) +b/x.
def ui5io_L11_C7_B2_04():
    x=sp.symbols("x")
    k=random.randint(2,4)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
    b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = sum(a[i]* x**i for i in range(k)) + b*sqrt(x) + c/x
    kq= diff(f, x)
    kq2=diff(f, x)+ b*sqrt(x) - diff(b*sqrt(x), x)
    kq3=random.choice([diff(f, x) + b/x + b/x**2,diff(f, x) + b/x**2 + b/x**2]) 
    kq4=diff(f, x) + b*sqrt(x)/2 - diff(b*sqrt(x), x)


   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2= my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3= my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4= my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$.")
    noi_dung_loigiai=my_module.frac_to_dfrac(f"$y'=({latex(f)})'={latex(diff(f, x))}$.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_05]-M2. Tìm đạo hàm của asinu
def ui5io_L11_C7_B2_05():   

    x=sp.symbols("x")
    a = random.randint(2, 10)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = b*sin(a*x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq=diff(f, x)
    kq2=random.choice([-a*b*sin(x), -a*b*cos(x)])
    kq3=random.choice([a*b*cos(x), b*cos(a*x)])
    kq4=random.choice([b*sin(a*x), -a*b*cos(a*x)])

   
    kq= f"$y'={latex(kq)}$"
    kq2=f"$y'={latex(kq2)}$"
    kq3=f"$y'={latex(kq3)}$"
    kq4=f"$y'={latex(kq4)}$"

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham}$.")
    noi_dung_loigiai=my_module.thay_the_ngoac_sincos(f"$y'=({ham})'={latex(diff(f, x))}$")


    
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

#[D11_C7_B2_06]-M2. Tìm đạo hàm của acosu
def ui5io_L11_C7_B2_06():   

    x=sp.symbols("x")
    a = random.randint(2, 10)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = b*cos(a*x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq=diff(f, x)
    kq2=random.choice([a*b*sin(x), b*sin(a*x)])
    kq3=random.choice([a*b*cos(x), b*sin(x)])
    kq4=random.choice([b*cos(x), a*b*cos(a*x)])
   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham}$.")
    noi_dung_loigiai=my_module.thay_the_ngoac_sincos(f"$y'=({ham})'={latex(diff(f, x))}$")
    
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

#[D11_C7_B2_07]-M2. Tìm đạo hàm của asinx + bcosx
def ui5io_L11_C7_B2_07():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if a==b: b=a+random.randint(1,3)

    f = a*sin(x) + b*cos(x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq=diff(f, x)
    kq2=random.choice([a*cos(x)+b*sin(x)])
    kq3=random.choice([-a*cos(x)-b*sin(x)])
    kq4=random.choice([-a*cos(x)+b*sin(x)])
   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham}$.")
    noi_dung_loigiai=my_module.thay_the_ngoac_sincos(f"$y'=({ham})'={latex(diff(f, x))}$")
    
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

#[D11_C7_B2_08]. Tính đạo hàm hàm số y=a^x.
def ui5io_L11_C7_B2_08():
    #Tạo bậc ngẫu nhiên
    a= random.randint(2,9)   

    kq= f"{a}^x\\ln {a}"
    kq2=f"{a}^x\\log {a}"
    kq3=f"{a}^x"
    kq4=f"\\frac{{{a}^x}}{{\\ln {a}}}"

    #Tạo các phương án
    pa_A= f"*$y'={kq}$"
    pa_B= f"$y'={kq2}$"
    pa_C= f"$y'={kq3}$"
    pa_D= f"$y'={kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính đạo hàm của hàm số $y={a}^{{x}}$."
    noi_dung_loigiai=f"$y'=({a}^x)'={kq}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_09]. Tính đạo hàm hàm số y=a^u.
def ui5io_L11_C7_B2_09():
    #Tạo bậc ngẫu nhiên
    a= random.randint(2,9) 
    bac = random.randint(2,3)
    x = sp.symbols('x')
    f = my_module.random_polynomial("x",bac)[0]

    kq = latex(diff((a**f), x)).replace("log","ln")
    kq2= latex(diff((a**f/log(a)), x))
    kq3=latex(a**f)
    kq4=latex(a**f*ln(a))

    #Tạo các phương án
    pa_A= f"*$y'={kq}$"
    pa_B= f"$y'={kq2}$"
    pa_C= f"$y'={kq3}$"
    pa_D= f"$y'={kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Câu 1.Tính đạo hàm của hàm số $y={latex(a**f)}$."
    noi_dung_loigiai=f"$y'=({latex(f)})'.{latex(a**f)}.\\ln {a}={kq}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_10]-M2. Tìm đạo hàm của m/(ax+b)
def ui5io_L11_C7_B2_10():   

    x=sp.symbols("x")
    a = random.randint(1, 10)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    m =  a*random.randint(2,5)
    n = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = m/(a*x+b)

    kq=diff(f, x)
    kq2=random.choice([m*(a*x+b)**2])
    kq3=random.choice([-m/(a*x+b)])
    kq4=random.choice([m/(a*x+b)**2])
   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    # kq=my_module.thay_the_ngoac_log(kq)
    # kq2=my_module.thay_the_ngoac_log(kq2)
    # kq3=my_module.thay_the_ngoac_log(kq3)
    # kq4=my_module.thay_the_ngoac_log(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$.")
    noi_dung_loigiai=my_module.thay_the_ngoac_sincos(my_module.frac_to_dfrac(f"$y'=({latex(f)})'={latex(diff(f, x))}$"))
    
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

#[D11_C7_B2_11]-M2. Tìm đạo hàm y=(mx^2+nx+p)/(ax+b)
def ui5io_L11_C7_B2_11():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    b = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    m =  random.choice([random.randint(-6, -1), random.randint(1, 6)])
    n = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    p = random.randint(-6, 6)

    f = (m*x**2+n*x+p)/(a*x+b)
    g = (m*x**2+n*x+p)/(a*x)
    h = (m*x**2)/(a*x+b)
    k = (m*x**2+p)/(a*x+b)

    f_tu, f_mau = m*x**2+n*x+p, a*x+b

    kq=expand((2*m*x+n)*f_mau-f_tu*a)/(a*x+b)**2
    kq2=expand((2*m*x+n)*f_mau-f_tu*a)/(a*x+b)
    kq3=expand((2*m*x+n)*f_mau+f_tu*a)/(a*x+b)**2
    kq4=expand((2*m*x+n)*f_mau+f_tu*a)/(a*x+b)
   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")


    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$.")
    dao_ham=f"\\dfrac{{({latex(f_tu)})'.({latex(f_mau)})-({latex(f_tu)}).({latex(f_mau)})'}}{{({latex(f_mau)})^2}}"
    noi_dung_loigiai=my_module.thay_the_ngoac_sincos(my_module.frac_to_dfrac(f"$y'=\\left({latex(f)}\\right)'={dao_ham}={latex(expand((2*m*x+n)*f_mau-f_tu*a)/(a*x+b)**2)}$"))
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_12]. Tính đạo hàm hàm số y = đa thức + e^x.
def ui5io_L11_C7_B2_12():
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")
    k=random.randint(2,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
    m = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = sum(a[i]* x**i for i in range(k)) 
    g = m*exp(x)
    kq= diff(f, x) + g
    kq2=diff(f, x)+ m
    kq3=diff(f, x) + exp(m*x)
    kq4=diff(f, x) + exp(x)

    #Tạo các phương án
    pa_A= f"*$y'={latex(kq)}$"
    pa_B= f"$y'={latex(kq2)}$"
    pa_C= f"$y'={latex(kq3)}$"
    pa_D= f"$y'={latex(kq4)}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính đạo hàm của hàm số $y={latex(f+g)}$."
    noi_dung_loigiai=f"$y'=({latex(f+g)})'={latex(kq)}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_13]. Tính đạo hàm hàm số y = e^u.
def ui5io_L11_C7_B2_13():
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")
    k=random.randint(2,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
    m = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = exp(sum(a[i]* x**i for i in range(k)))
    g = sum(a[i]* x**i for i in range(k))
   
    kq= diff(f, x)
    kq2=exp(sum(a[i]* x**i for i in range(k)))
    kq3=exp(sum(a[i]* x**i for i in range(k))) + diff(sum(a[i]* x**i for i in range(k)), x)
    kq4=exp(diff(sum(a[i]* x**i for i in range(k)), x))

    #Tạo các phương án
    pa_A= f"*$y'={latex(kq)}$"
    pa_B= f"$y'={latex(kq2)}$"
    pa_C= f"$y'={latex(kq3)}$"
    pa_D= f"$y'={latex(kq4)}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính đạo hàm của hàm số $y={latex(f)}$."
    noi_dung_loigiai=f"$y'=({latex(f)})'=({latex(g)})'.{latex(f)}={latex(kq)}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_14]-M2. Tìm đạo hàm của y=atanx + bcotx
def ui5io_L11_C7_B2_14():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if a==b: b=a+random.randint(1,3)

    f = a*tan(x) + b*cot(x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq=a/(cos(x))**2 - b/(sin(x))**2
    kq2=random.choice([a*cot(x)+b*tan(x)])
    kq3=random.choice([-a/(cos(x))**2+b/(sin(x))**2])
    kq4=random.choice([a/cos(x)-b/sin(x)])
   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham}$.")
    noi_dung_loigiai=my_module.thay_the_ngoac_sincos(f"$y'=({ham})'={latex(a/(cos(x))**2 - b/(sin(x))**2)}$")
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_15]-M2. Tìm đạo hàm của atanu
def ui5io_L11_C7_B2_15():   

    x=sp.symbols("x")
    a = random.randint(2, 10)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = b*tan(a*x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq=a*b/(cos(a*x))**2
    kq2=random.choice([a*b*cot(a*x), -a*b*cot(a*x)])
    kq3=random.choice([b/(cos(a*x))**2, b/(sin(a*x))**2])
    kq4=random.choice([-a*b/(cos(a*x))**2, a*b/(sin(a*x))**2, -a*b/(sin(a*x))**2])

   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham}$.")
    noi_dung_loigiai=my_module.frac_to_dfrac(my_module.thay_the_ngoac_sincos(f"$y'=({ham})'={b}.({a}x)'.{latex(1/(cos(a*x))**2)}={latex(a*b/(cos(a*x))**2)}$")).replace("--","")
    
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


#[D11_C7_B2_16]-M2. Tìm đạo hàm của acotu
def ui5io_L11_C7_B2_16():   

    x=sp.symbols("x")
    a = random.randint(2, 10)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = b*cot(a*x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq=-a*b/(sin(a*x))**2
    kq2=random.choice([a*b*tan(a*x), -a*b*tan(a*x)])
    kq3=random.choice([b/(sin(a*x))**2, b/(cos(a*x))**2])
    kq4=random.choice([a*b/(sin(a*x))**2, a*b/(cos(a*x))**2,-a*b/(cos(a*x))**2])

   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham}$.")
    noi_dung_loigiai=my_module.frac_to_dfrac(my_module.thay_the_ngoac_sincos(f"$y'=({ham})'=-{b}.({a}x)'.{latex(1/(sin(a*x))**2)}={latex(-a*b/(sin(a*x))**2)}$")).replace("--","")
    
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

#[D11_C7_B2_17]-M2. Tìm đạo hàm y=(ax+b).căn(x)
def ui5io_L11_C7_B2_17():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = (a*x+b)*sqrt(x)
   

    kq=f"\\dfrac{{{latex(3*a*x+b)}}}{{2\\sqrt{{x}}}}"
    kq2=a/(2*sqrt(x))
    kq3=a+1/(2*sqrt(x))
    kq4=f"\\dfrac{{{latex(2*a*x+b)}}}{{\\sqrt{{x}}}}"

   
    kq= my_module.frac_to_dfrac(f"$y'={kq}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={kq4}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$.")
    noi_dung_loigiai=my_module.frac_to_dfrac(my_module.thay_the_ngoac_sincos(f"$y'=\\left[{latex(f)}\\right]'=({latex(a*x+b)})'.(\\sqrt{{x}})+({latex(a*x+b)}).(\\sqrt{{x}})'=\\dfrac{{{latex(3*a*x+b)}}}{{2\\sqrt{{x}}}}$")).replace("--","")
    
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

#[D11_C7_B2_18]-M2. Tìm đạo hàm y=(ax+b).sin(x)
def ui5io_L11_C7_B2_18():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = (a*x+b)*sin(x)  

    kq=a*sin(x)+(a*x+b)*cos(x)
    kq2=a*cos(x)
    kq3=a*cos(x)+b*sin(x)
    kq4=a*sin(x)+b*cos(x)
   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.thay_the_ngoac_sincos(my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$."))
    noi_dung_loigiai=my_module.frac_to_dfrac(my_module.thay_the_ngoac_sincos(f"$y'=\\left[{latex(f)}\\right]'=({latex(a*x+b)})'.(\\sin x)+({latex(a*x+b)}).(\\sin x)'={latex(a*sin(x)+(a*x+b)*cos(x))}$")).replace("--","")
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_19]-M2. Tìm đạo hàm y=(ax+b).cos(x)
def ui5io_L11_C7_B2_19():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = (a*x+b)*cos(x)  

    kq=a*cos(x)+(-a*x-b)*sin(x)
    kq2=a*cos(x)+(a*x+b)*sin(x)
    kq3=a*cos(x)+b*sin(x)
    kq4=a*sin(x)+b*cos(x)
   
    kq= my_module.frac_to_dfrac(f"$y'={latex(kq)}$")
    kq2=my_module.frac_to_dfrac(f"$y'={latex(kq2)}$")
    kq3=my_module.frac_to_dfrac(f"$y'={latex(kq3)}$")
    kq4=my_module.frac_to_dfrac(f"$y'={latex(kq4)}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.thay_the_ngoac_sincos(my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$."))
    noi_dung_loigiai=my_module.frac_to_dfrac(my_module.thay_the_ngoac_sincos(f"$y'=\\left[{latex(f)}\\right]'=({latex(a*x+b)})'.(\\cos x)-({latex(a*x+b)}).(\\cos x)'={latex(a*cos(x)+(-a*x-b)*sin(x))}$")).replace("--","")
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_20]-M2. Tìm đạo hàm y=(ax+b)/căn(x)
def ui5io_L11_C7_B2_20():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = (a*x+b)/sqrt(x)
    t=ucln_ba_so(abs(a),abs(b),2)
    a1,b1,c1=int(a/t),int(b/t),int(2/t),

    kq=f"\\dfrac{{{latex(a1*x-b1)}}}{{{c1}x\\sqrt{{x}}}}".replace("1x","x")
    kq2=random.choice([f"{latex(a/(2*sqrt(x)))}"])
    kq3=random.choice([f"{latex(a+1/(2*sqrt(x)))}", f"\\dfrac{{{latex(a1*x+b1)}}} {{2x}}"])
    kq4=f"\\dfrac{{{latex(2*a*x+b)}}}{{\\sqrt{{x}}}}"
   
    kq= my_module.frac_to_dfrac(f"$y'={kq}$")
    kq2=my_module.frac_to_dfrac(f"$y'={kq2}$")
    kq3=my_module.frac_to_dfrac(f"$y'={kq3}$")
    kq4=my_module.frac_to_dfrac(f"$y'={kq4}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$.")
    noi_dung_loigiai=my_module.frac_to_dfrac(my_module.thay_the_ngoac_sincos(\
    f"$y'=\\left[{latex(f)}\\right]'=\\dfrac{{({latex(a*x+b)})'.(\\sqrt{{x}})-({latex(a*x+b)}).(\\sqrt{{x}})'}}{{x}}=\\dfrac{{{latex(a1*x-b1)}}}{{{c1}x\\sqrt{{x}}}}$")).replace("--","").replace("1x","x")
    
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

#[D11_C7_B2_21]-M2. Tìm đạo hàm y=log_a x
def ui5io_L11_C7_B2_21():   

    x=sp.symbols("x")
    a = random.choice([random.randint(2,9), random.randint(11,99)])

    f =f"\\log_{{{a}}} x"


    kq=f"\\dfrac{{1}}{{x\\ln {a}}}"
    kq2=f"\\dfrac{{{a}}}{{\\ln x}}"
    kq3=f"\\dfrac{{{1}}}{{x\\log {a}}}"
    kq4=f"\\dfrac{{{a}}}{{\\log x}}"
   
    kq= my_module.frac_to_dfrac(f"$y'={kq}$")
    kq2=my_module.frac_to_dfrac(f"$y'={kq2}$")
    kq3=my_module.frac_to_dfrac(f"$y'={kq3}$")
    kq4=my_module.frac_to_dfrac(f"$y'={kq4}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={f}$.")
    noi_dung_loigiai=f"$y=\\left({f}\\right)'=\\dfrac{{1}}{{x\\ln {a}}}.$"
    
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

#[D11_C7_B2_22]-M2. Tìm đạo hàm y=log_a (đa thức)
def ui5io_L11_C7_B2_22():         

    x=sp.symbols("x")
    k=random.randint(2,3)    
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    if k==3:
        a = random.randint(1, 10)
        c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        if a*c<0:
            c=-c
        b=int(sqrt(4*a*c))-random.randint(1,5)
        f=a*x**2+b*x+c

    g=latex(diff(f,x))
    chon=random.randint(1,2)
    if chon==1 and k==2:
        a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        f=a*x+b
        t=math.gcd(a,b)
        a1,a2,b2=int(a/t),int(a/t),int(b/t)

        m = random.choice([random.randint(2,9), random.randint(11,20)])
        ham_so =f"\\log_{{{m}}} ({latex(f)})"
        noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.")
        noi_dung_loigiai=f"$y=\\left[{ham_so}\\right]'=\\dfrac{{({latex(f)})'}}{{({latex(f)})\\ln {m}}}=\\dfrac{{{a1}}}{{({latex(a2*x+b2)})\\ln {m}}}.$"

        kq=f"\\dfrac{{{a1}}}{{({latex(a2*x+b2)})\\ln {m}}}"
        kq2=f"\\dfrac{{{a1}}}{{{latex(a2*x+b2)}}}"
        kq3=f"\\dfrac{{{a1}}}{{({latex(a2*x+b2)})\\log {m}}}"
        kq4=f"\\dfrac{{{m}}}{{({latex(f)})\\log {m}}}"

    if chon==1 and k==3:

        m = random.choice([random.randint(2,9), random.randint(11,20)])
        ham_so =f"\\log_{{{m}}} ({latex(f)})"
        noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.")
        noi_dung_loigiai=f"$y=\\left[{ham_so}\\right]'=\\dfrac{{({latex(f)})'}}{{({latex(f)})\\ln {m}}}=\\dfrac{{{g}}}{{({latex(f)})\\ln {m}}}.$"

        kq=f"\\dfrac{{{g}}}{{({latex(f)})\\ln {m}}}"
        kq2=f"\\dfrac{{1}}{{({latex(f)})\\ln {m}}}"
        kq3=f"\\dfrac{{{g}}}{{({latex(f)})\\log {m}}}"
        kq4=f"\\dfrac{{1}}{{({latex(f)})\\log {m}}}"

    if chon==2 and k==2:
        a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        f=a*x+b
        t=math.gcd(a,b)
        a1,a2,b2=int(a/t),int(a/t),int(b/t)

        m = 10
        ham_so =f"\\log ({latex(f)})"

        noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.")
        noi_dung_loigiai=f"$y=\\left[{ham_so}\\right]'=\\dfrac{{({latex(f)})'}}{{({latex(f)})\\ln {m}}}=\\dfrac{{{a1}}}{{({latex(a2*x+b2)})\\ln {m}}}.$"

        kq=f"\\dfrac{{{a1}}}{{({latex(a2*x+b2)})\\ln {m}}}"
        kq2=f"\\dfrac{{{a1}}}{{({latex(a2*x+b2)})\\log {m}}}"
        kq3=f"\\dfrac{{{a1}}}{{{latex(a2*x+b2)}}}"
        kq4=f"\\dfrac{{{m}}}{{{latex(f)}}}"
    
    if chon==2 and k==3:
        m = 10
        ham_so =f"\\log ({latex(f)})"

        noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.")
        noi_dung_loigiai=f"$y=\\left[{ham_so}\\right]'=\\dfrac{{({latex(f)})'}}{{({latex(f)})\\ln {m}}}=\\dfrac{{{g}}}{{({latex(f)})\\ln {m}}}.$"

        kq=f"\\dfrac{{{g}}}{{({latex(f)})\\ln {m}}}"
        kq2=f"\\dfrac{{1}}{{({latex(f)})\\ln {m}}}"
        kq3=f"\\dfrac{{{g}}}{{{latex(f)}}}"
        kq4=f"\\dfrac{{1}}{{{latex(f)}}}"

   
    kq= my_module.frac_to_dfrac(f"$y'={kq}$")
    kq2=my_module.frac_to_dfrac(f"$y'={kq2}$")
    kq3=my_module.frac_to_dfrac(f"$y'={kq3}$")
    kq4=my_module.frac_to_dfrac(f"$y'={kq4}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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


#[D11_C7_B2_23]-M2. Tìm đạo hàm y=ln (đa thức)
def ui5io_L11_C7_B2_23():         

    x=sp.symbols("x")
    k=random.randint(2,4)    
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    if k==3:
        a = random.randint(1, 10)
        c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        if a*c<0:
            c=-c
        b=int(sqrt(4*a*c))-random.randint(1,5)
        f=a*x**2+b*x+c

    g=diff(f,x)

    ham_so =f"\\ln ({latex(f)})"

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.")
    noi_dung_loigiai=f"$y=\\left[{ham_so}\\right]'=\\dfrac{{{latex(g)}}}{{{latex(f)}}}={latex(g/f)}.$"

    kq=f"{latex(g/f)}"
    kq2=f"{latex(g*f)}"
    kq3=f"{latex(1/f)}"
    kq4=f"{latex(1/g)}"

   
    kq= my_module.frac_to_dfrac(f"$y'={kq}$")
    kq2=my_module.frac_to_dfrac(f"$y'={kq2}$")
    kq3=my_module.frac_to_dfrac(f"$y'={kq3}$")
    kq4=my_module.frac_to_dfrac(f"$y'={kq4}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_24]-M2. Tìm đạo hàm y=(đa thức).a^x
def ui5io_L11_C7_B2_24():         

    x=sp.symbols("x")
    k=random.randint(2,3)
    if k==2:
        a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        f=a*x+b
    if k==3:
        a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
        f = sum(a[i]*x**i for i in range(k))      
    g=diff(f,x)    
    chon=random.randint(1,2)
     
    if chon==1:
        m =random.randint(2,20)        
        ham_so =f"({latex(f)}){{{m}}}^x"
        noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.")        

        kq=f"\\left[ {latex(g)}+({latex(f)}).\\ln {m}\\right].{{{m}}}^x"
        if k==2:
            kq2=f"{a}.{{{m}}}^x"
            kq3=f"{a}.{{{m}}}^x.\\ln {m}"       

        if k==3:
            kq2=f"({latex(g)}).{{{m}}}^x"
            kq3=f"({latex(g)}).{{{m}}}^x.\\ln {m}"
        kq4=f"\\left({latex(f+g)}\\right).{{{m}}}^x"

        noi_dung_loigiai=f"$y=\\left[{ham_so}\\right]'=({latex(f)})'.{{{m}}}^x +({latex(f)})({{{m}}}^x)'$\n\n"\
        f"$=({latex(g)}).{{{m}}}^x +({latex(f)}).{{{m}}}^x.\\ln {m}={kq}$."
    
    if chon==2:
        m = "e"       
        ham_so =f"({latex(f)})e^x"
        noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.")        

        kq=f"\\left({latex(f+g)}\\right).e^x"
        if k==2:
            kq2=f"{a}.e^x"
            kq3=f"{a}.e^x.\\log e"
        if k==3:
            kq2=f"({latex(g)}).e^x"
            kq3=f"({latex(g)}).e^x.\\log e"
        kq4=f"\\left({latex(f+g)}\\right).\\log e"

        noi_dung_loigiai=f"$y=\\left[{ham_so}\\right]'=({latex(f)})'.e^x +({latex(f)})(e^x)'$\n\n"\
        f"$=({latex(g)}).e^x +({latex(f)})e^x={kq}$"
    
       
    kq= my_module.frac_to_dfrac(f"$y'={kq}$")
    kq2=my_module.frac_to_dfrac(f"$y'={kq2}$")
    kq3=my_module.frac_to_dfrac(f"$y'={kq3}$")
    kq4=my_module.frac_to_dfrac(f"$y'={kq4}$")

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_25]-M2. Tìm đạo hàm y=(ax+b)/cos(x) hoặc y=(ax+b)/sin(x)
def ui5io_L11_C7_B2_25():   

    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    chon=random.randint(1,2)
    
    if chon==1:

        f = (a*x+b)/sin(x)

        kq=f"\\dfrac{{{latex(a*sin(x)+(-a*x-b)*cos(x))}}}{{\\sin^2 x}}"
        kq2=f"\\dfrac{{{latex(a*sin(x)+(a*x+b)*cos(x))}}}{{\\sin^2 x}}"
        kq3=f"\\dfrac{{{latex(a*sin(x)+(-a*x-b)*cos(x))}}}{{\\sin 2x}}"
        kq4=f"\\dfrac{{{latex(a*cos(x)+(-a*x-b)*sin(x))}}}{{\\sin^2 x}}"
        noi_dung_loigiai=my_module.thay_the_ngoac_sincos(f"$y'=\\left({latex(f)}\\right)'="\
            f"\\dfrac{{({latex(a*x+b)})'.\\sin x-({latex(a*x+b)}).(\\sin x)'}}{{\\sin^2 x}}={kq}$").replace("--","")

    if chon==2:
        f = (a*x+b)/cos(x)
        kq=f"\\dfrac{{{latex(a*cos(x)+(a*x+b)*sin(x))}}}{{\\cos^2 x}}"
        kq2=f"\\dfrac{{{latex(a*cos(x)+(a*x+b)*sin(x))}}}{{\\cos^2 x}}"
        kq3=f"\\dfrac{{{latex(a*cos(x)+(-a*x-b)*sin(x))}}}{{\\cos 2x}}"
        kq4=f"\\dfrac{{{latex(a*cos(x)+(-a*x-b)*sin(x))}}}{{\\cos^2 x}}"
        noi_dung_loigiai=my_module.thay_the_ngoac_sincos(f"$y'=\\left({latex(f)}\\right)'="\
            f"\\dfrac{{({latex(a*x+b)})'.\\cos x-({latex(a*x+b)}).(\\cos x)'}}{{\\cos^2 x}}={kq}$").replace("--","")
   
    kq= f"$y'={kq}$"
    kq2=f"$y'={kq2}$"
    kq3=f"$y'={kq3}$"
    kq4=f"$y'={kq4}$"

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.thay_the_ngoac_sincos(my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(f)}$."))
    
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#7.2.5 Đạo hàm của hàm hợp

#[D11_C7_B2_26]-M2. Tìm đạo hàm y=căn(P(x))
def ui5io_L11_C7_B2_26():   
    x=sp.symbols("x")      
   
    k=random.randint(2,3)
    if k==2:
        a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        f=a*x+b
    if k==3:
        a = random.randint(1, 10)
        c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        if a*c<0:
            c=-c
        b=int(sqrt(4*a*c))-random.randint(1,5)
        f=a*x**2+b*x+c
    g=diff(f,x)  

    kq=f"{latex(g/(2*sqrt(f)))}"
    kq2=f"{latex(1/sqrt(f))}"
    kq3=f"\\dfrac{{1}}{{({latex(f)}){latex(sqrt(f))}}}"
    kq4=f"{latex(g*sqrt(f))}"

    noi_dung_loigiai=f"$y'=\\left({latex(f)}\\right)'="\
        f"\\dfrac{{({latex(f)})'}}{{2\\sqrt{{{latex(f)}}} }}={kq}$."

       
    kq= f"$y'={kq}$"
    kq2=f"$y'={kq2}$"
    kq3=f"$y'={kq3}$"
    kq4=f"$y'={kq4}$"

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung= my_module.thay_the_ngoac_sincos(my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={latex(sqrt(f))}$."))
    
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_27]-M2. Tìm đạo hàm y=căn(sin(ax+b))
def ui5io_L11_C7_B2_27():   
    x=sp.symbols("x")   
   
 
    a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f=sqrt(sin(a*x+b))
    if a%2!=0:
        kq=f"\\dfrac{{{a}\\cos({latex(a*x+b)})}}{{2\\sqrt{{\\sin({latex(a*x+b)})}}}}"
        kq2=f"\\dfrac{{{-a}\\cos({latex(a*x+b)})}}{{2\\sqrt{{\\sin({latex(a*x+b)})}}}}"
        kq4=f"\\dfrac{{{-a}}}{{2\\sqrt{{\\sin({latex(a*x+b)})}}}}"
    else:
        t=int(a/2)
        kq=f"\\dfrac{{{t}\\cos({latex(a*x+b)})}}{{\\sqrt{{\\sin({latex(a*x+b)})}}}}"
        kq2=f"\\dfrac{{{-t}\\cos({latex(a*x+b)})}}{{\\sqrt{{\\sin({latex(a*x+b)})}}}}"
        kq4=f"\\dfrac{{{-t}}}{{\\sqrt{{\\sin({latex(a*x+b)})}}}}"
    
    kq3=f"\\dfrac{{1}}{{2\\sqrt{{\\sin({latex(a*x+b)})}}}}"
    

    noi_dung= my_module.thay_the_ngoac_sincos(f"Tính đạo hàm của hàm số $y=\\sqrt{{\\sin({latex(a*x+b)})}}$.")

    noi_dung_loigiai=f"$y'=\\dfrac{{\\left[\\sin({latex(a*x+b)})\\right]'}} {{2\\sqrt{{\\sin({latex(a*x+b)})}}}}"\
        f"={kq}$."

       
    kq= f"$y'={kq}$"
    kq2=f"$y'={kq2}$"
    kq3=f"$y'={kq3}$"
    kq4=f"$y'={kq4}$"

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_28]-M2. Tìm đạo hàm y=căn(cos(ax+b))
def ui5io_L11_C7_B2_28():   
    x=sp.symbols("x")   
   
 
    a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    
    if a%2!=0:
        kq=f"\\dfrac{{{-a}\\sin({latex(a*x+b)})}}{{2\\sqrt{{\\cos({latex(a*x+b)})}}}}"
        kq2=f"\\dfrac{{{a}\\sin({latex(a*x+b)})}}{{2\\sqrt{{\\cos({latex(a*x+b)})}}}}"
        kq4=f"\\dfrac{{{a}}}{{2\\sqrt{{\\cos({latex(a*x+b)})}}}}"
    else:
        t=int(a/2)
        kq=f"\\dfrac{{{-t}\\sin({latex(a*x+b)})}}{{\\sqrt{{\\cos({latex(a*x+b)})}}}}"
        kq2=f"\\dfrac{{{t}\\sin({latex(a*x+b)})}}{{\\sqrt{{\\cos({latex(a*x+b)})}}}}"
        kq4=f"\\dfrac{{{t}}}{{\\sqrt{{\\cos({latex(a*x+b)})}}}}"
    
    kq3=f"\\dfrac{{1}}{{2\\sqrt{{\\cos({latex(a*x+b)})}}}}"
    

    noi_dung= my_module.thay_the_ngoac_sincos(f"Tính đạo hàm của hàm số $y=\\sqrt{{\\cos({latex(a*x+b)})}}$.")

    noi_dung_loigiai=f"$y'=\\dfrac{{\\left[\\cos({latex(a*x+b)})\\right]'}} {{2\\sqrt{{\\cos({latex(a*x+b)})}}}}"\
        f"={kq}$."

       
    kq= f"$y'={kq}$"
    kq2=f"$y'={kq2}$"
    kq3=f"$y'={kq3}$"
    kq4=f"$y'={kq4}$"

    kq=my_module.thay_the_ngoac_sincos(kq)
    kq2=my_module.thay_the_ngoac_sincos(kq2)
    kq3=my_module.thay_the_ngoac_sincos(kq3)
    kq4=my_module.thay_the_ngoac_sincos(kq4)

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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


#[D11_C7_B2_29]-M2. Tìm đạo hàm y=m/u
def ui5io_L11_C7_B2_29():         

    x=sp.symbols("x")    
    
    k=random.randint(2,3)
    if k==2:
        a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        f=a*x+b
    if k==3:
        a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
        f = sum(a[i]*x**i for i in range(k))      
   
    m =random.choice([random.randint(-10, -2), random.randint(2, 20)])      
    ham_so =f"{latex(m/f)}"
    g=diff(m/f,x)            

    kq=f"{latex(g)}"
    kq2=f"\\ln ({latex(f)})"
    kq3=f"\\dfrac{{{m}}}{{({latex(f)})^2}}"
    kq4=f"\\dfrac{{{-m}}}{{({latex(f)})^2}}"

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.") 
    noi_dung_loigiai=f"$y'=\\left[{ham_so}\\right]'=\\dfrac{{{-m}({latex(f)})'}}{{\\left({latex(f)}\\right)^2}}={kq}.$\n"     

    kq= f"$y'={kq}$"
    kq2=f"$y'={kq2}$"
    kq3=f"$y'={kq3}$"
    kq4=f"$y'={kq4}$"
    

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_30]-M2. Tìm đạo hàm (đa thức)^n
def ui5io_L11_C7_B2_30():         

    x=sp.symbols("x")    
    
    k=random.randint(2,3)
    if k==2:
        a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        f=a*x+b
    if k==3:
        a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
        f = sum(a[i]*x**i for i in range(k))      
   
    m =random.randint(3, 20)
    if m==a:m=m+random.randint(1,3)
    ham_so =f"({latex(f)})^{{{m}}}"
    g=diff(f**m,x)            

    kq=f"{latex(g)}"
    kq2=f"({latex(f)})^{{{m-1}}}"
    kq3=f"{m}({latex(f)})^{{{m-1}}}"
    if k==2:
        kq4=f"{a}({latex(f)})^{{{m-1}}}"
    else:
        kq4=f"({latex(diff(f,x) )})({latex(f)})^{{{m-1}}}"
    

    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.") 
    noi_dung_loigiai=f"$y'=\\left[{ham_so}\\right]'={m}({latex(f)})'\\left({latex(f)}\\right)^{{{m-1}}}={kq}.$\n"     

    kq= f"$y'={kq}$"
    kq2=f"$y'={kq2}$"
    kq3=f"$y'={kq3}$"
    kq4=f"$y'={kq4}$"
    

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_31]-M2. Đạo hàm cấp hai của đa thức
def ui5io_L11_C7_B2_31():         

    x=sp.symbols("x")  
    
    k=random.randint(3,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
    f = sum(a[i]*x**i for i in range(k))      

    ham_so =f"{latex(f)}"
    g=diff(f,x)
    g=diff(g,x)           

    kq=f"{latex(g)}"
    kq2=f"{latex(diff(f,x))}"
    kq3=f"{latex(g+random.randint(1,10))}"
    kq4=f"{latex(diff(f,x)+random.randint(1,10)*x)}"


    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm cấp hai của hàm số $y={ham_so}$.") 
    noi_dung_loigiai=f"$y'=\\left({ham_so}\\right)'={latex(diff(f,x))}.$\n\n"\
    f"$y''=\\left({latex(diff(f,x))}\\right)'={kq}$."   

    kq= f"$y''={kq}$"
    kq2=f"$y''={kq2}$"
    kq3=f"$y''={kq3}$"
    kq4=f"$y''={kq4}$"
    

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_32]-M2. Đạo hàm cấp hai của sin(ax+b)
def ui5io_L11_C7_B2_32():         

    x=sp.symbols("x")     
    
    a =random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = sin(a*x+b)     

    ham_so =f"\\sin({latex(a*x+b)})"
    g=diff(f,x)
    g=diff(g,x)           

    kq=f"{latex(g)}"
    kq2=f"{latex(diff(f,x))}"
    kq3=f"\\cos({latex(a*x+b)})"
    kq4=f"{latex(-g)}"


    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm cấp hai của hàm số $y={ham_so}$.") 
    noi_dung_loigiai=f"$y'=\\left[{ham_so}\\right]'={latex(diff(f,x))}.$\n\n"\
    f"$y''=\\left[{latex(diff(f,x))}\\right]'={kq}$."   

    kq= f"$y''={kq}$"
    kq2=f"$y''={kq2}$"
    kq3=f"$y''={kq3}$"
    kq4=f"$y''={kq4}$"
    

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_33]-M2. Đạo hàm cấp hai của cos(ax+b)
def ui5io_L11_C7_B2_33():         

    x=sp.symbols("x")      
    
    a =random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = cos(a*x+b)     

    ham_so =f"\\cos({latex(a*x+b)})"
    g=diff(f,x)
    g=diff(g,x)           

    kq=f"{latex(g)}"
    kq2=f"{latex(diff(f,x))}"
    kq3=f"\\sin({latex(a*x+b)})"
    kq4=f"{latex(-g)}"


    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm cấp hai của hàm số $y={ham_so}$.") 
    noi_dung_loigiai=f"$y'=\\left[{ham_so}\\right]'={latex(diff(f,x))}.$\n\n"\
    f"$y''=\\left[{latex(diff(f,x))}\\right]'={kq}$."   

    kq= f"$y''={kq}$"
    kq2=f"$y''={kq2}$"
    kq3=f"$y''={kq3}$"
    kq4=f"$y''={kq4}$"
    

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_34]-M2. Đạo hàm cấp hai của y=(ax+b)/(cx+d)
def ui5io_L11_C7_B2_34():         

    x=sp.symbols("x")      
    
    a =random.randint(-10,10)
    b =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d =random.randint(-10,10)
    if a*d-b*c==0:d=d+random.randint(1,3)

    f = (a*x+b)/(c*x+d)  

    ham_so =f"{latex(f)}"          

    kq=f"\\dfrac{{{-2*(a*d-b*c)*c}}}{{{latex((c*x+d)**3)}}}"
    kq2=f"\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}"
    kq3=f"\\dfrac{{{(a*d-b*c)}}}{{{latex((c*x+d)**4)}}}"
    kq4=f"\\dfrac{{{(a*d-b*c)*c}}}{{{latex((c*x+d)**3)}}}"


    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm cấp hai của hàm số $y={ham_so}$.") 
    noi_dung_loigiai=f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$.\n\n"\
    f"$y''=\\left[\\dfrac{{{-a*d+b*c}}}{{{latex((c*x+d)**2)}}}\\right]'=\\dfrac{{{-a*d+b*c}\\left[{latex((c*x+d)**2)}\\right]'}}{{{latex((c*x+d)**4)}}}={kq}$."   

    kq= f"$y''={kq}$"
    kq2=f"$y''={kq2}$"
    kq3=f"$y''={kq3}$"
    kq4=f"$y''={kq4}$"
    

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_35]-M2. Đạo hàm của y=(ax+b)/(cx+d)
def ui5io_L11_C7_B2_35():         

    x=sp.symbols("x")      
    
    a =random.randint(-10,10)
    b =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d =random.randint(-10,10)
    if a*d-b*c==0:d=d+random.randint(1,3)

    f = (a*x+b)/(c*x+d)  

    ham_so =f"{latex(f)}"          

    kq=f"\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}"
    kq2=f"\\dfrac{{{a*d+b*c}}}{{{latex((c*x+d)**2)}}}"
    kq3=f"\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**4)}}}"
    kq4=f"\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**3)}}}"


    noi_dung= my_module.frac_to_dfrac(f"Tính đạo hàm của hàm số $y={ham_so}$.") 
    noi_dung_loigiai=f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$."
    

    kq= f"$y'={kq}$"
    kq2=f"$y'={kq2}$"
    kq3=f"$y'={kq3}$"
    kq4=f"$y'={kq4}$"
    

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

#[D11_C7_B2_36]-M2. Cho hàm số đa thức. Giải phương trình chứa đạo hàm cấp hai.
def ui5io_L11_C7_B2_36():
    x=sp.symbols("x")
    k=5
    a1=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    a2=random.randint(-5, 5)
    a3=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    a4=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    a5=random.randint(-5, 5)
    t=random.randint(-7,7)
    f = a1*x**4+a2*x**3+a3*x**2+a4*x+a5
    dh_1=diff(f, x)
    dh_2=diff(dh_1, x)
    a, b, c = 12*a1, 6*a2, 2*a3-t
    delta,x1,x2=tinh_va_dau_delta(a,b,c)
    if delta=="<0":   
        kq= f"Phương trình vô nghiệm"
        kq2=f"$x={phan_so(c/a)}$"
        kq3=f"$x={phan_so(-b/a)}$"
        kq4=f"$x_1={phan_so(-b/a)},x_2={phan_so(c/a)} $"
        noi_dung_loigiai=f"$y'=({latex(f)})'={latex(diff(f, x))}$.\n\n"\
    f"$y''=({latex(dh_1)})'={latex(dh_2)}$.\n\n"\
    f"$y''={t}\\Leftrightarrow {latex(dh_2)}={t} \\Leftrightarrow {latex(dh_2-t)}=0$. Phương trình này vô nghiệm."

    if delta=="=0":   
        kq= f"$x={phan_so(-b/a)}$"
        kq2=f"$x={phan_so(c/a)}$"
        kq3=f"Phương trình vô nghiệm"
        kq4=f"$x_1={phan_so(-b/a)},x_2={phan_so(c/a)} $"
        noi_dung_loigiai=f"$y'=({latex(f)})'={latex(diff(f, x))}$.\n\n"\
    f"$y''=({latex(dh_1)})'={latex(dh_2)}$.\n\n"\
    f"$y''={t}\\Leftrightarrow {latex(dh_2)}={t}\\Leftrightarrow {latex(dh_2-t)}=0 \\Leftrightarrow x={phan_so(-b/a)}$."

    if delta==">0":   
        kq= f"$x_1={latex(x1)},x_2={latex(x2)} $"
        kq2=f"$x={phan_so(c/a)}$"
        kq3=f"Phương trình vô nghiệm"
        kq4=f"$x_1={phan_so(-b/a)},x_2={phan_so(c/a)} $"
        noi_dung_loigiai=f"$y'=({latex(f)})'={latex(diff(f, x))}$.\n\n"\
    f"$y''=({latex(dh_1)})'={latex(dh_2)}$.\n\n"\
    f"$y''={t}\\Leftrightarrow {latex(dh_2)}={t}\\Leftrightarrow {latex(dh_2-t)}=0 \\Leftrightarrow x_1={latex(x1)},x_2={latex(x2)}$."

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $y={latex(f)}$. Phương trình $y''={t}$ có nghiệm là"    

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B2_37]-M2. Đạo hàm cấp hai của đa thức tại điểm x_0
def ui5io_L11_C7_B2_37():         

    x=sp.symbols("x")  
    
    k=random.randint(3,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]
    f = sum(a[i]*x**i for i in range(k))
    x_0=random.randint(-5,5)      

    ham_so =f"{latex(f)}"
    g1=diff(f,x)
    g2=diff(g1,x)

    kq= g2.subs(x,x_0)
    kq2= g1.subs(x,x_0)
    kq3= f.subs(x,x_0)
    kq4= f.subs(x,x_0)+random.randint(1,5)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung= my_module.frac_to_dfrac(f"Đạo hàm cấp hai của hàm số $y={ham_so}$ tại điểm $x_0={x_0}$ bằng") 
    noi_dung_loigiai=f"$y'=\\left({ham_so}\\right)'={latex(diff(f,x))}.$\n\n"\
    f"$y''=\\left({latex(diff(f,x))}\\right)'={latex(g2)}$.\n\n"\
    f"$y''({x_0})={kq}$."   
    
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

#[D11_C7_B2_38]-M2. Cho hàm số quãng đường. Tính vận tốc tại thời điểm t_0.
def ui5io_L11_C7_B2_38():         

    t=sp.symbols("t")      
    k=random.randint(2,3)
    
    if k==2:
        a = random.randint(1, 10)
        c = random.randint(1, 10)    
        b=int(sqrt(4*a*c))-random.randint(1,5)    
        f=a*t**2+b*t+c        
        x_0=random.randint(1,10)   
        ham_so =f"{latex(f)}"   

    if k==3:
        a = random.randint(1, 5)
        b = random.randint(0, 5)    
        c=  random.randint(-1, 5)
        d=  random.randint(1, 8)        
        if 3<=a<=5:
            c = random.randint(-3, -1)
            d=  random.randint(3, 8)

        f=a*t**3+b*t**2+c*t+d        
        x_0=random.randint(1,10)   
        ham_so =f"{latex(f)}"
    g1=diff(f,t)
    g2=diff(g1,t)

    kq= g1.subs(t,x_0)
    kq2= g2.subs(t,x_0)
    kq3= f.subs(t,x_0)
    kq4= f.subs(t,x_0)+random.randint(1,5)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung=f"Một vật chuyển động thẳng không đều xác định bởi phương trình $s(t)={ham_so}$, "\
        f"trong đó ${{s}}$ tính bằng mét và ${{t}}$ tính bằng giây."\
        f" Tính vận tốc của chuyển động tại thời điểm $t={x_0}$."
    noi_dung_loigiai=f"$v(t)=\\left({ham_so}\\right)'={latex(diff(f,t))}.$\n\n"\
    f"$v({x_0})={kq} $ m/s."   
    
    #Tạo các phương án
    pa_A= f"*${{{kq} }}$ m/s"
    pa_B= f"${{{kq2} }}$ m/s"
    pa_C= f"${{{kq3} }}$ m/s"
    pa_D= f"${{{kq4} }}$ m/s"
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

#[D11_C7_B2_39]-M2. Cho hàm số quãng đường. Tính gia tốc tại thời điểm t_0.
def ui5io_L11_C7_B2_39():         
    t=sp.symbols("t")      
    k=random.randint(2,3)
    if k==2:
        a = random.randint(1, 10)
        c = random.randint(1, 10)    
        b=int(sqrt(4*a*c))-random.randint(1,5)    
        f=a*t**2+b*t+c        
        x_0=random.randint(1,10)   
        ham_so =f"{latex(f)}"   

    if k==3:
        a = random.randint(1, 5)
        b = random.randint(0, 5)    
        c=  random.randint(-1, 5)
        d=  random.randint(1, 8)        
        if 3<=a<=5:
            c = random.randint(-3, -1)
            d=  random.randint(3, 8)

        f=a*t**3+b*t**2+c*t+d        
        x_0=random.randint(1,10)   
        ham_so =f"{latex(f)}"
    g1=diff(f,t)
    g2=diff(g1,t)

    kq= g2.subs(t,x_0)
    kq2= g1.subs(t,x_0)
    kq3= f.subs(t,x_0)
    kq4= f.subs(t,x_0)+random.randint(1,5)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung=f"Một vật chuyển động thẳng không đều xác định bởi phương trình $s(t)={ham_so}$, "\
        f"trong đó ${{s}}$ tính bằng mét và ${{t}}$ tính bằng giây."\
        f" Tính gia tốc của chuyển động tại thời điểm $t={x_0}$."
    noi_dung_loigiai=f"$v(t)=\\left({ham_so}\\right)'={latex(g1)}.$\n\n"\
    f"$a(t)=\\left({latex(g1)}\\right)'={latex(g2)}$.\n\n"\
    f"$a({x_0})={kq}$ $m/s^2$."   
    
    #Tạo các phương án
    pa_A= f"*${{{kq}}}$ $m/s^2$"
    pa_B= f"${{{kq2}}}$ $m/s^2$"
    pa_C= f"${{{kq3}}}$ $m/s^2$"
    pa_D= f"${{{kq4}}}$ $m/s^2$"
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

#[D11_C7_B2_40]-M2. Cho hàm số bậc 3. Giải phương trình chứa đạo hàm
def ui5io_L11_C7_B2_40():
    x=sp.symbols("x")
    a1 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
    b1 = random.randint(-5,5)
    c1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    d1 = random.randint(-10,10) 
    f=a1*x**3+b1*x**2+c1*x+d1
    ham_so =f"{latex(f)}"
    t=random.randint(-5,5)   
    ham_so =f"{latex(f)}"
    g1=diff(f,x)
    a, b, c = 3*a1, 2*b1, c1-t
    noi_dung=f"Cho hàm số $f(x)={ham_so}$. Nghiệm của phương trình $f'(x)={t}$ là"
    delta,x1,x2=tinh_va_dau_delta(a,b,c)
    if delta=="<0":   
        kq= f"Phương trình vô nghiệm"
        kq2=f"$x={phan_so(c/a)}$"
        kq3=f"$x={phan_so(-b/a)}$"
        kq4=f"$x_1={phan_so(-b/a)},x_2={phan_so(c/a)} $"
        noi_dung_loigiai=f"$f'(x)=({latex(f)})'={latex(diff(f, x))}$.\n\n"\
    f"$f'(x)={t}\\Leftrightarrow {latex(g1)}={t} \\Leftrightarrow {latex(g1-t)}=0$. Phương trình này vô nghiệm."

    if delta=="=0":   
        kq= f"$x={phan_so(-b/a)}$"
        kq2=f"$x={phan_so(c/a)}$"
        kq3=f"Phương trình vô nghiệm"
        kq4=f"$x_1={phan_so(-b/a)},x_2={phan_so(c/a)} $"
        noi_dung_loigiai=f"$f'(x)=({latex(f)})'={latex(diff(f, x))}$.\n\n"\
    f"$f'(x)={t}\\Leftrightarrow {latex(g1)}={t}\\Leftrightarrow {latex(g1-t)}=0 \\Leftrightarrow x={phan_so(-b/a)}$."

    if delta==">0":   
        kq= f"$x_1={latex(x1)},x_2={latex(x2)} $"
        kq2=f"$x={phan_so(c/a)}$"
        kq3=f"Phương trình vô nghiệm"
        kq4=f"$x_1={phan_so(-b/a)},x_2={phan_so(c/a)} $"
        noi_dung_loigiai=f"$f'(x)=({latex(f)})'={latex(diff(f, x))}$.\n\n"\
    f"$f'(x)={t}\\Leftrightarrow {latex(g1)}={t}\\Leftrightarrow {latex(g1-t)}=0 \\Leftrightarrow x_1={latex(x1)},x_2={latex(x2)}$."

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

#[D11_C7_B2_41]-M2. Cho hàm số bậc 3. Giải bất phương trình chứa đạo hàm
def ui5io_L11_C7_B2_41():
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
    t= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f=a*x**2+b*x+c
    g=integrate(f+t,x)+random.randint(-10,10)
    dau=random.choice([">0","<0","\\ge 0", "\\le 0"])
    noi_dung=f"Cho hàm số $f(x)={latex(g)}$. Tập nghiệm của bất phương trình $f'(x)-{t}{dau}$ là".replace("--","+")
    
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

    noi_dung_loigiai=f"$f'(x)=\\left({latex(g)}\\right)'={latex(diff(g,x))}$.\n\n"\
    f"$f'(x)-{t}{dau}\\Leftrightarrow {latex(f)}{dau} \\Rightarrow$ {kq}.".replace("--","+")

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
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
      
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

#[D11_C7_B2_42]-M3. f(x)=a.căn(x)+ bx +c. Giải BPT f'(x) > 0.
def ui5io_L11_C7_B2_42():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    if chon==1:
        a=random.randint(-7,-1)
        b=random.randint(1,8)
        c=random.randint(-20,20)
        f=a*sqrt(x)+b*x+c      
        dau=random.choice([">","\\ge"])
        noi_dung=f"Cho hàm số $f(x)={latex(f)}$. Tập nghiệm của bất phương trình $f'(x) {dau} 0$ là" 

        if dau ==">":
            kq=f'$\\left( {phan_so(a**2/(4*b**2))}; +\\infty \\right)$'
            kq2=f'$\\left[{phan_so(a**2/(4*b**2))}; +\\infty \\right)$'
            kq3=f'$\\left(-\\infty;{phan_so(a**2/(4*b**2))}; \\right)$'
            kq4=f'$\\left(-\\infty;{phan_so(a**2/(4*b**2))}; \\right]$'
        else:
            kq=f'$\\left[{phan_so(a**2/(4*b**2))}; +\\infty \\right)$'
            kq2=f'$\\left( {phan_so(a**2/(4*b**2))}; +\\infty \\right)$'
            kq3=f'$\\left(-\\infty;{phan_so(a**2/(4*b**2))}; \\right)$'
            kq4=f'$\\left(-\\infty;{phan_so(a**2/(4*b**2))}; \\right]$'

        noi_dung_loigiai=f"$f'(x){dau} 0 \\Leftrightarrow \\frac{{{a}}}{{2\\sqrt x}}+ {b} {dau} 0$. (Điều kiện: $x>0$)\n\n"\
        f"${2*b}\\sqrt x {dau} {-a} \\Leftrightarrow \\sqrt x {dau} {phan_so(-a/(2*b))} \\Leftrightarrow x {dau} {phan_so(a**2/(4*b**2))}$ (thỏa mãn điều kiện).\n\n"\
        f"Vậy tập nghiệm là: {kq}."


    if chon==2:
        a=random.randint(-7,-1)
        b=random.randint(1,8)
        c=random.randint(-20,20)
        f=a*sqrt(x)+b*x+c
        dau=random.choice([">","\\le"])
        noi_dung=f"Cho hàm số $f(x)={latex(f)}$. Tập nghiệm của bất phương trình $f'(x) {dau} 0$ là"
        if dau =="<":
            
            kq=f'$\\left( 0; {phan_so(a**2/(4*b**2))} \\right)$'
            kq2=f'$\\left({phan_so(a**2/(4*b**2))}; +\\infty \\right)$'
            kq3=f'$\\left(-\\infty;{phan_so(a**2/(4*b**2))}; \\right)$'
            kq4=f'$\\left[0; {phan_so(a**2/(4*b**2))} \\right)$'
        else:
            
            kq=f'$\\left(0; {phan_so(a**2/(4*b**2))}\\right]$'
            kq2=f'$\\left( {phan_so(a**2/(4*b**2))}; +\\infty \\right)$'
            kq3=f'$\\left(-\\infty;{phan_so(a**2/(4*b**2))}; \\right)$'
            kq4=f'$\\left(0; {phan_so(a**2/(4*b**2))}\\right)$'

        noi_dung_loigiai=f"$f'(x){dau} 0 \\Leftrightarrow \\frac{{{a}}}{{2\\sqrt x}}+ {b} {dau} 0$. (Điều kiện: $x>0$)\n\n"\
        f"${2*b}\\sqrt x {dau} {-a} \\Leftrightarrow \\sqrt x {dau} {phan_so(-a/(2*b))} \\Leftrightarrow x {dau} {phan_so(a**2/(4*b**2))}$.\n\n"\
        f"Kết hợp điều kiện ta được tập nghiệm là: {kq}."

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

#[D11_C7_B2_43]-M4. Cho f(x) là hàm bậc 3. Tìm m để f'(x)>0 (<0) với mọi x.
def ui5io_L11_C7_B2_43(): 
    x=sp.symbols("x")
    m=sp.symbols("m")
    chon = random.randint(1,4)
    if chon==1:
        a = random.choice([random.randint(-5, -1), random.randint(1, 5)])    
        b=random.randint(-5, 5) 
        c= random.randint(-5, 5)
        a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

        #Tạo dấu bất phương trình 
        if a>0:
            dau=">0"
        else:
            dau="<0"

        f=f"{a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        g=f"{phan_so(a/3)}x^3 + \\left(\\dfrac{{{m+b}}}{{2}}\\right)x^2 + \\left({latex(a_m*m+c)}\\right)x+{latex(random.randint(-7,7)*m+random.randint(-7,-1))}".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        noi_dung=f"Cho hàm số $f(x)={g}$. Tìm tất cả các giá trị của tham số ${{m}}$ để bất phương trình $f'(x) {dau}$ với mọi $x\\in \\mathbb{{R}}$.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        delta= (m+b)**2-4*a*(a_m*m+c)

        delta= expand((m+b)**2-4*a*(a_m*m+c))
        a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

        tich_4a=show_tich(4,a)

        
        kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
        kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
        kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
        kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")

        noi_dung_loigiai=f"Ta có: $f'(x)= {f}$.\n\n"\
        f"$\\Delta ={latex((m+b)**2)}-{tich_4a}.\\left({latex(a_m*m+c)}\\right)={latex(delta)}$.\n\n"\
            f"${f} {dau}$ với mọi $x\\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta <0$\n\n"\
            f"$\\Rightarrow {latex(delta)} <0 \\Rightarrow$ {kq}.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
    if chon==2:
        a =  random.choice([random.randint(-5, -1), random.randint(1, 5)])        
        b=random.randint(-5, 5) 
        c= random.randint(-5, 5)
        a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

        #Tạo dấu bất phương trình 
        if a>0:
            dau="\\ge 0"
        else:
            dau="\\le 0"

        f=f"{a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        g=f"{phan_so(a/3)}x^3 + \\left(\\dfrac{{{m+b}}}{{2}}\\right)x^2 + \\left({latex(a_m*m+c)}\\right)x+{latex(random.randint(-7,7)*m+random.randint(-7,-1))}".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")

        delta= (m+b)**2-4*a*(a_m*m+c)

        delta= expand((m+b)**2-4*a*(a_m*m+c))

        a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c

        noi_dung=f"Cho hàm số $f(x)={g}$. Tìm tất cả các giá trị của tham số ${{m}}$ để bất phương trình $f'(x) {dau}$ với mọi $x\\in \\mathbb{{R}}$.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")

        kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
        kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")
        kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
        kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")

        tich_4a=show_tich(4,a)

        noi_dung_loigiai=f"Ta có: $f'(x)= {f}$.\n\n"\
        f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
                f"${f} {dau}$ với mọi $x\\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta \\le 0$\n\n"\
                f"$\\Rightarrow {latex(delta)} \\le 0 \\Rightarrow$ {kq}.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")


    if chon==3:
        a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
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
        else:
            dau="\\ge 0"
            dau_nguoc="<"

        f=f"{a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau}".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        g=f"{phan_so(a/3)}x^3 + \\left(\\dfrac{{{m+b}}}{{2}}\\right)x^2 + ({latex(a_m*m+c)})x+{latex(random.randint(-7,7)*m+random.randint(-7,-1))}".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")

        tich_4a=show_tich(4,a)
        noi_dung=f"Cho hàm số $f(x)={g}$. Tìm tất cả các giá trị của tham số ${{m}}$ để bất phương trình $f'(x) {dau}$ vô nghiệm.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        

        kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
        kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
        kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
        kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")

        noi_dung_loigiai=f"Ta có: $f'(x)={f}$.\n\n"\
        f"${f} {dau}$ vô nghiệm $\\Leftrightarrow {a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$.\n\n"\
            f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
            f"${a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta <0$\n\n"\
            f"$\\Leftrightarrow {latex(delta)} <0 \\Leftrightarrow$ {kq}.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
    if chon==4:
        a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
        b=random.randint(-5, 5) 
        c= random.randint(-5, 5)
        a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])

        delta= (m+b)**2-4*a*(a_m*m+c)
        delta= expand((m+b)**2-4*a*(a_m*m+c))
        a1_m, b1_m, c1_m =delta.coeff(m**2), delta.coeff(m), b**2-4*a*c
        f=f"{a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        g=f"{phan_so(a/3)}x^3 + \\left(\\dfrac{{{m+b}}}{{2}}\\right)x^2 + ({latex(a_m*m+c)})x+{latex(random.randint(-7,7)*m+random.randint(-7,-1))}".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")

        #Tạo dấu bất phương trình 
        if a>0:
            dau="<0"
            dau_nguoc="\\ge "           
                
        else:
            dau=">0"
            dau_nguoc="\\le "            
        tich_4a=show_tich(4,a)

        kq=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<=0","m")
        kq2=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,"<0","m")
        kq3=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">0","m")
        kq4=my_module.solve_bpt_bac2(a1_m,b1_m,c1_m,">=0","m")

        noi_dung=noi_dung=f"Cho hàm số $f(x)={g}$. Tìm tất cả các giá trị của tham số ${{m}}$ để bất phương trình $f'(x) {dau}$ vô nghiệm.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
        tich_4a=show_tich(4,a)
        noi_dung_loigiai=f"Ta có: $f'(x)={f}$.\n\n"\
        f"${f} {dau}$ vô nghiệm $\\Leftrightarrow {a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$.\n\n"\
            f"Ta có: $\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
            f"${a}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) {dau_nguoc}0, \\forall x \\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta \\le 0$\n\n"\
            f"$\\Leftrightarrow {latex(delta)} \\le 0 \\Leftrightarrow$ {kq}.".replace("$1x^2","$x^2").replace("$-1x^2","$-x^2").replace("$1x^3","$x^3").replace("$-1x^3","$-x^3")
            
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

################################################################################
#BÀI 3 - PHƯƠNG TRÌNH TIẾP TUYẾN 

#[D11_C7_B3_01]-M2. Cho hàm số đa thức. Viết phương trình tiếp tuyến tại điểm M(x0;y0)
def ui5io_L11_C7_B3_01():
    x=sp.symbols("x")
    k=random.randint(3,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    g=diff(f, x)

    x_0=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    y_0=f.subs(x,x_0)
    f_dh=g.subs(x,x_0)

    kq= f"$y={latex(f_dh*(x-x_0)+y_0)}$"
    kq2=f"$y={latex(f_dh*(x+x_0)+y_0)}$"
    kq3=f"$y={latex(f_dh*x-y_0)}$"
    kq4=f"$y={latex(x-x_0+y_0)}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
    ten_diem=random.choice(["A","B","M","N","P","E","H"])
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $y={latex(f)}$. Viết phương trình tiếp tuyến của đồ thị hàm số đã cho tại điểm ${ten_diem}({x_0};{y_0})$."
    noi_dung_loigiai=thay_dau_congtru(f"Ta có: $f'(x)={latex(g)} \\Rightarrow f'({x_0})={f_dh}$.\n\n"\
    f"Phương trình tiếp tuyến là: $y={f_dh}(x-{x_0})+{y_0} \\Leftrightarrow $ {kq}.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B3_02]-M2. Cho hàm số đa thức. Viết phương trình tiếp tuyến tại điểm có hoành độ x_0
def ui5io_L11_C7_B3_02():
    x=sp.symbols("x")
    k=random.randint(3,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    g=diff(f, x)

    x_0=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    y_0=f.subs(x,x_0)
    f_dh=g.subs(x,x_0)

    kq= f"$y={latex(f_dh*(x-x_0)+y_0)}$"
    kq2=f"$y={latex(f_dh*(x+x_0)+y_0)}$"
    kq3=f"$y={latex(f_dh*x-y_0)}$"
    kq4=f"$y={latex(x-x_0+y_0)}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
    ten_diem=random.choice(["A","B","M","N","P","E","H"])
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $y={latex(f)}$. Tiếp tuyến của đồ thị hàm số đã cho tại điểm ${{{ten_diem}}}$ có hoành độ bằng ${{{x_0}}}$ có phương trình là"
    noi_dung_loigiai=thay_dau_congtru(f"Ta có: $f'(x)={latex(g)} \\Rightarrow f'({x_0})={f_dh}$.\n\n"\
    f"$x_0={x_0}\\Rightarrow y_0=f({x_0})={y_0}$.\n\n"\
    f"Phương trình tiếp tuyến là: $y={f_dh}(x-{x_0})+{y_0} \\Leftrightarrow $ {kq}.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B3_03]-M2. Cho hàm số đa thức. Viết phương trình tiếp tuyến tại điểm có tung độ y_0
def ui5io_L11_C7_B3_03():
    x=sp.symbols("x")
    k=3
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    g=diff(f, x)

    x_0=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    y_0=f.subs(x,x_0)
    f_dh=g.subs(x,x_0)

    kq= f"$y={latex(f_dh*(x-x_0)+y_0)}$"
    kq2=f"$y={latex(f_dh*(x+x_0)+y_0)}$"
    kq3=f"$y={latex(f_dh*x-y_0)}$"
    kq4=f"$y={latex(x-x_0+y_0)}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    
    ten_diem=random.choice(["A","B","M","N","P","E","H"])
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $y={latex(f)}$. Tiếp tuyến của đồ thị hàm số đã cho tại điểm ${{{ten_diem}}}$ có tung độ bằng ${{{y_0}}}$ có phương trình là"
    noi_dung_loigiai=thay_dau_congtru(f"Xét phương trình: ${latex(f)}={y_0} \\Rightarrow x={x_0}$.\n\n"\
        f"$f'(x)={latex(g)} \\Rightarrow f'({x_0})={f_dh}$.\n\n"\
    f"Phương trình tiếp tuyến là: $y={f_dh}(x-{x_0})+{y_0} \\Leftrightarrow $ {kq}.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B3_04]-M1. Cho hàm số. Tính hệ số góc của tiếp tuyến tại điểm x_0
def ui5io_L11_C7_B3_04():
    x=sp.symbols("x")
    k=random.randint(3,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    g=diff(f, x)

    x_0=random.randint(1, 6)
    y_0=f.subs(x,x_0)
    k=g.subs(x,x_0)    

    kq= k
    kq2=y_0
    kq3=k+random.randint(1,5)
    kq4=y_0-random.randint(1,5)

    #Tạo các phương án
    pa_A= f"*${{k={kq}}}$"
    pa_B= f"${{k={kq2}}}$"
    pa_C= f"${{k={kq3}}}$"
    pa_D= f"${{k={kq4}}}$"
    
    ten_diem=random.choice(["A","B","M","N","P","E","H"])
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $y={latex(f)}$. Tiếp tuyến của đồ thị hàm số đã cho tại điểm có hoành độ $x_0={x_0}$ có hệ số góc k bằng."
    noi_dung_loigiai=thay_dau_congtru(f"Ta có: $f'(x)={latex(g)} \\Rightarrow k=f'({x_0})={k}$.")

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D11_C7_B4_01]-TF-M2. Tạo câu đúng-sai: Đạo hàm của hàm số đa thức 
def ui5io_L11_C7_B4_01():
    x=sp.symbols("x")
    k=random.randint(3,5)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k))
    if k==5:
        a=random.choice([random.randint(-3,-1),random.randint(1,3)]) 
        b=random.randint(-4,4)
        c=random.randint(-6,6)
        f=a*x**4+b*x**2+c
    f_1=diff(f, x)
    f_2=diff(f_1, x)    
    
    noi_dung=f"Cho hàm số $y={latex(f)}$. Xét tính đúng sai của các khẳng định sau"

    
    kq1_T=f"*Đạo hàm của hàm số đã cho là $y'={latex(f_1)}$"
    kq1_F=f"Đạo hàm của hàm số đã cho là $y'={latex(f_1+random.randint(1,4)*x+random.randint(1,4))}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Đạo hàm của hàm số đã cho là $y'={latex(f_1)}$ là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai vì $y'={latex(f_1)}$."


    kq2_T=f"* Đạo hàm cấp hai của hàm số đã cho là $y''={latex(f_2)}$"
    kq2_F=f"Đạo hàm cấp hai của hàm số đã cho là $y''={latex(f_2+random.randint(0,5)*x+random.randint(1,5))}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f" Đạo hàm cấp hai của hàm số đã cho là $y''={latex(f_2)}$ là khẳng định đúng.\n\n"\
    f"$y'={latex(f_1)}, y''={latex(f_2)}$"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai vì:\n\n"\
        f"$y'={latex(f_1)}, y''={latex(f_2)}$"
    
    x_0=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    hsg=f_1.subs(x,x_0)
    kq3_T=f"*Tiếp tuyến của đồ thị hàm số đã cho tại điểm có hoành độ bằng {x_0} có hệ số góc bằng {hsg}"
    kq3_F=f"Tiếp tuyến của đồ thị hàm số đã cho tại điểm có hoành độ bằng {x_0} có hệ số góc bằng {hsg+random.randint(1,10)}"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là đúng vì:\n\n"\
    f"$y'={latex(f_1)}$ nên hệ số góc là $k=y'({x_0})={hsg}$."
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là sai vì:\n\n"\
    f"$y'={latex(f_1)}$ nên hệ số góc là $k=y'({x_0})={hsg}$."

    x_0=x_0+random.randint(-3, 3)
    if x_0==0: x_0=random.randint(1,4)
    y_0=f.subs(x,x_0)
    hsg=f_1.subs(x,x_0)
    ten_diem=random.choice(["A","B","M","N","P","E","H"])
    kq4_T=f"*Tiếp tuyến của đồ thị hàm số đã cho tại điểm ${ten_diem}({x_0};{y_0})$ có phương trình là $y={latex(hsg*(x-x_0)+y_0)}$"
    kq4_F=f"Tiếp tuyến của đồ thị hàm số đã cho tại điểm ${ten_diem}({x_0};{y_0})$ có phương trình là $y={latex(hsg*(x+x_0)-y_0)}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=thay_dau_congtru(f"Khẳng định đã cho là đúng.\n\n"\
    f"Ta có: $f'(x)={latex(f_1)} \\Rightarrow f'({x_0})={hsg}$.\n\n"\
    f"Phương trình tiếp tuyến là: $y={hsg}(x-{x_0})+{y_0} \\Leftrightarrow y={latex(hsg*(x-x_0)+y_0)}$.")
    if kq4==kq4_F:
        loigiai_4=thay_dau_congtru(f"Khẳng định đã cho là sai.\n\n"\
    f"Ta có: $f'(x)={latex(f_1)} \\Rightarrow f'({x_0})={hsg}$.\n\n"\
    f"Phương trình tiếp tuyến là: $y={hsg}(x-{x_0})+{y_0} \\Leftrightarrow y={latex(hsg*(x-x_0)+y_0)}$.")


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
    f"d) {loigiai[3]}\\\\ \n"

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

#[D11_C7_B4_02]-TF-M2. Tạo câu đúng-sai: Đạo hàm cấp 1,2,tiếp tuyến của y=(ax+b)/(cx+d)
def ui5io_L11_C7_B4_02():
    x=sp.symbols("x")
    a =random.randint(-10,10)
    b =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c =random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d =random.randint(-10,10)
    if a*d-b*c==0:d=d+random.randint(1,3)

    f = (a*x+b)/(c*x+d)  

    ham_so =f"{latex(f)}"          

    kq=f"\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}"


    noi_dung=f"Cho hàm số ${ham_so}$. Xét tính đúng sai của các khẳng định sau"

    kq1_T=f"*Hàm số có $y'=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$"
    kq1_F=f"Hàm số có $y'=\\dfrac{{{a*d+b*c}}}{{{latex((c*x+d)**2)}}}$ "
    kq1=random.choice([kq1_T, kq1_F])

    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
    f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$."
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n"\
    f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$."

    kq2_T=f"*Hàm số có $y''=\\dfrac{{{-2*(a*d-b*c)*c}}}{{{latex((c*x+d)**3)}}}$"
    kq2_F=f"Hàm số có $y''=\\dfrac{{{(a*d-b*c)*c}}}{{{latex((c*x+d)**3)}}}$"
    kq2=random.choice([kq2_T, kq2_F])

    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
    f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$.\n\n"\
    f"$y''=\\left[\\dfrac{{{-a*d+b*c}}}{{{latex((c*x+d)**2)}}}\\right]'=\\dfrac{{{-a*d+b*c}\\left[{latex((c*x+d)**2)}\\right]'}}{{{latex((c*x+d)**4)}}}=\\dfrac{{{-2*(a*d-b*c)*c}}}{{{latex((c*x+d)**3)}}}$." 
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n"\
        f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$.\n\n"\
    f"$y''=\\left[\\dfrac{{{-a*d+b*c}}}{{{latex((c*x+d)**2)}}}\\right]'=\\dfrac{{{-a*d+b*c}\\left[{latex((c*x+d)**2)}\\right]'}}{{{latex((c*x+d)**4)}}}=\\dfrac{{{-2*(a*d-b*c)*c}}}{{{latex((c*x+d)**3)}}}$."

    x_0=random.choice([random.randint(-5, -1), random.randint(1, 5)])
    if x_0==-d/c: x_0=x_0+1
    f_1=diff(f,x)
    hsg=f_1.subs(x,x_0)

    kq3_T=f"*Tiếp tuyến của đồ thị hàm số đã cho tại điểm có hoành độ bằng ${{{x_0}}}$ có hệ số góc bằng ${{{phan_so(hsg)}}}$"
    kq3_F=f"Tiếp tuyến của đồ thị hàm số đã cho tại điểm có hoành độ bằng ${{{x_0}}}$ có hệ số góc bằng ${{{phan_so(hsg+random.randint(1,10))}}}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là đúng vì:\n\n"\
    f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$ nên hệ số góc là $k=y'({x_0})={phan_so(hsg)}$."
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là sai vì:\n\n"\
    f"$y'=\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}$ nên hệ số góc là $k=y'({x_0})={phan_so(hsg)}$."

    

    x_0=x_0+random.randint(-3, 3)
    if x_0==-d/c: x_0=x_0+1
    y_0=f.subs(x,x_0)
    hsg=f_1.subs(x,x_0)
    ten_diem=random.choice(["A","B","M","N","P","E","H"])
    f_dh=f"\\left({ham_so}\\right)'=\\dfrac{{{show_tich(a,d)}-{show_tich(b,c)}}}{{{latex((c*x+d)**2)}}}=\\dfrac{{{a*d-b*c}}}{{{latex((c*x+d)**2)}}}"
    kq4_T=f"*Tiếp tuyến của đồ thị hàm số đã cho tại điểm có hoành độ $x={x_0}$ có phương trình là $y={latex(hsg*(x-x_0)+y_0)}$"
    kq4_F=f"Tiếp tuyến của đồ thị hàm số đã cho tại điểm có hoành độ $x={x_0}$ có phương trình là $y={latex(hsg*(x+x_0)-y_0)}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=thay_dau_congtru(f"Khẳng định đã cho là đúng.\n\n"\
    f"$x_0={x_0}\\Rightarrow y_0={phan_so(y_0)}$.\n\n"\
    f"Ta có: $f'(x)={f_dh} \\Rightarrow f'({x_0})={phan_so(hsg)}$.\n\n"\
    f"Phương trình tiếp tuyến là: $y={phan_so(hsg)}(x-{x_0})+{phan_so(y_0)} \\Leftrightarrow y={latex(hsg*(x-x_0)+y_0)}$.")
    if kq4==kq4_F:
        loigiai_4=thay_dau_congtru(f"Khẳng định đã cho là sai.\n\n"\
    f"$x_0={x_0}\\Rightarrow y_0={phan_so(y_0)}$.\n\n"\
    f"Ta có: $f'(x)={f_dh} \\Rightarrow f'({x_0})={phan_so(hsg)}$.\n\n"\
    f"Phương trình tiếp tuyến là: $y={phan_so(hsg)}(x-{x_0})+{phan_so(y_0)} \\Leftrightarrow y={latex(hsg*(x-x_0)+y_0)}$.")
    

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
    f"d) {loigiai[3]}\\\\ \n"

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

#[D11_C7_B4_03]-TF-M2. Tạo câu đúng-sai: Đạo hàm của y=msin(ax)+cos(x+b)
def ui5io_L11_C7_B4_03():
    x=sp.symbols("x")
    m = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    a = random.randint(2, 10)
    b=random.choice([-pi/3,-pi/4,-pi/6,-pi/2,pi/2,pi/4,pi/6,pi/2,pi,-pi])

    f=m*sin(a*x)+cos(x+b)
    f_1=diff(f,x)
    noi_dung=f"Cho hàm số $y={latex(f)}$. Xét tính đúng sai của các khẳng định sau"

    kq1_T=thay_dau_congtru(f"*$y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}$")
    kq1_F=thay_dau_congtru(random.choice([f"$y'={latex(m*cos(a*x))}+{latex(sin(x+b))}$",f"$y'={latex(a*m*cos(a*x))}+{latex(sin(x+b))}$"]))
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là đúng."
    if kq1==kq1_F:
        loigiai_1=thay_dau_congtru(f"Khẳng định đã cho là sai vì $y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}$.")

    kq2_T=thay_dau_congtru(f"*$y''={latex(-a*a*m*sin(a*x))}-{latex(cos(x+b))}$")
    kq2_F=thay_dau_congtru(random.choice([f"$y''={latex(-2*a*sin(a*x))}-{latex(cos(x+b))}$",f"$y''={latex(-a*m*sin(a*x))}+{latex(cos(x+b))}$"]))
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=thay_dau_congtru(f"Khẳng định đã cho là đúng vì\n\n"\
    f"$y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}\\Rightarrow y''={latex(-a*a*m*sin(a*x))}-{latex(cos(x+b))}$.")
    if kq2==kq2_F:
        loigiai_2=thay_dau_congtru(f"Khẳng định đã cho là sai vì\n\n"\
    f"$y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}\\Rightarrow y''={latex(-a*a*m*sin(a*x))}-{latex(cos(x+b))}$.")


    x_0=random.choice([-pi/3,-pi/4,-pi/6,-pi/2,pi/2,pi/4,pi/6,pi/2,pi,-pi])
    y_0=f_1.subs(x,x_0)
    kq3_T=f"*$y'\\left({latex(x_0)}\\right)={latex(y_0)}$"
    kq3_F=f"$y'\\left({latex(x_0)}\\right)={latex(y_0+pi)}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=thay_dau_congtru(f"Khẳng định đã cho là đúng vì\n\n"\
    f"$y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}\\Rightarrow y'\\left({latex(x_0)}\\right)={latex(y_0)}$.")

    if kq3==kq3_F:
        loigiai_3=thay_dau_congtru(f"Khẳng định đã cho là sai vì\n\n"\
        f"$y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}\\Rightarrow y'\\left({latex(x_0)}\\right)={latex(y_0)}$.")

    x_1=random.choice([-pi,-pi/3,-pi/4,-pi/6,-pi/2])
    y_1=f_1.subs(x,x_1)
    f_2=diff(f_1,x)
    x_2=random.choice([0,pi/2,pi/4,pi/6,pi/2,pi])
    y_2=f_2.subs(x,x_2)
    c=random.choice([random.randint(-4, -1), random.randint(1, 4)])
    t=y_1+c*y_2

    kq4_T=thay_dau_congtru(f"*$y'\\left({latex(x_1)}\\right) +{c}y''\\left({latex(x_2)}\\right)={latex(t)}$")
    kq4_F=thay_dau_congtru(f"$y'\\left({latex(x_1)}\\right) +{c}y''\\left({latex(x_2)}\\right)={latex(t+random.randint(1,5))}$")
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=thay_dau_congtru(f"Khẳng định đã cho là đúng vì\n\n"\
    f"$y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}\\Rightarrow y'\\left({latex(x_1)}\\right)={latex(y_1)}$.\n\n"\
    f"$y''={latex(-a*a*m*sin(a*x))}-{latex(cos(x+b))} \\Rightarrow  y''\\left({latex(x_2)}\\right)={latex(y_2)}$.\n\n"
    f"Suy ra $y'\\left({latex(x_1)}\\right) +{c}y''\\left({latex(x_2)}\\right)={latex(t)}$.")
    if kq4==kq4_F:
        loigiai_4=thay_dau_congtru(f"Khẳng định đã cho là sai vì\n\n"\
    f"$y'={latex(a*m*cos(a*x))}-{latex(sin(x+b))}\\Rightarrow y'\\left({latex(x_1)}\\right)={latex(y_1)}$.\n\n"\
    f"$y''={latex(-a*a*m*sin(a*x))}-{latex(cos(x+b))} \\Rightarrow  y''\\left({latex(x_2)}\\right)={latex(y_2)}$.\n\n"
    f"Suy ra $y'\\left({latex(x_1)}\\right) +{c}y''\\left({latex(x_2)}\\right)={latex(t)}$.")



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
    f"d) {loigiai[3]}\\\\ \n"

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

#[D11_C7_B4_04]-TF-M2. Tạo câu đúng-sai: Đạo hàm của hàm số lượng giác
def ui5io_L11_C7_B4_04():
    x=sp.symbols("x")
    m1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    m2 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    a = random.randint(2, 10)
    b=random.choice([-pi/3,-pi/4,-pi/6,-pi/2,pi/2,pi/4,pi/6,pi/2,pi,-pi])

    f=m1*sin(x)+m2*cos(x)
    f_1=diff(f,x)
    f_2=diff(f_1,x)
    x_0=random.choice([-pi/3,-pi/4,-pi/6,-pi/2,pi/2,pi/4,pi/6,pi/2,pi,-pi])
    y_0=f_2.subs(x,x_0)

    noi_dung=f"Xét tính đúng sai của các khẳng định sau"
    kq1_T=my_module.thay_the_ngoac_sincos(f"*Hàm số $y={latex(f)}$ có $y''\\left({latex(x_0)}\\right)={latex(y_0)}$")
    kq1_F=my_module.thay_the_ngoac_sincos(f"Hàm số $y={latex(f)}$ có $y''\\left({latex(x_0)}\\right)={latex(y_0+random.randint(1,5))}$")
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=my_module.thay_the_ngoac_sincos(f"Khẳng định đã cho là đúng.\n\n"\
    f"$y'={latex(m1*cos(x)-m2*sin(x))}\\Rightarrow y''={latex(-m1*sin(x)-m2*cos(x))}$.\n\n"\
    f"$y''({latex(x_0)})={latex(y_0)}$.")
    if kq1==kq1_F:
        loigiai_1=my_module.thay_the_ngoac_sincos(f"Khẳng định đã cho là sai.\n\n"\
    f"$y'={latex(m1*cos(x)-m2*sin(x))}\\Rightarrow y''={latex(-m1*sin(x)-m2*cos(x))}$.\n\n"\
    f"$y''({latex(x_0)})={latex(y_0)}$.")

    m1 = random.choice([random.randint(1, 7)])
    m2 = random.choice([random.randint(1, 7)])
    
    f=tan(m1*x)+cot(m2*x)

    kq2_T=my_module.thay_the_ngoac_sincos(f"*Hàm số $y={latex(f)}$ có $y'={m1-m2}+{latex(m1*tan(m1*x)**2-m2*cot(m2*x)**2)}$")
    kq2_F=my_module.thay_the_ngoac_sincos(f"Hàm số $y={latex(f)}$ có $y'={m1+m2}+{latex(m1*tan(m1*x)**2+m2*cot(m2*x)**2)}$")
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=my_module.thay_the_ngoac_sincos(f"Khẳng định đã cho là đúng.\n\n"\
    f"$y={latex(f)}\\Rightarrow y'={m1}[1+{latex(tan(m1*x)**2)}]-{m2}[1+{latex(cot(m2*x)**2)}]={m1-m2}+{latex(m1*tan(m1*x)**2-m2*cot(m2*x)**2)}$.")
    if kq2==kq2_F:
        loigiai_2=my_module.thay_the_ngoac_sincos(f"Khẳng định đã cho là sai.\n\n"\
        f"$y={latex(f)}\\Rightarrow y'={m1}[1+{latex(tan(m1*x)**2)}]-{m2}[1+{latex(cot(m2*x)**2)}]={m1-m2}+{latex(m1*tan(m1*x)**2-m2*cot(m2*x)**2)}$.")

    m = random.randint(2, 5)
    a = random.randint(2, 10)
    b=random.choice([-pi/3,-pi/4,-pi/6,-pi/2,pi/2,pi/4,pi/6,pi/2,pi,-pi])
    x_0=random.choice([-pi/3,-pi/4,-pi/6,-pi/2,pi/2,pi/4,pi/6,pi/2,pi,-pi])
    f=cos(a*x+b)**m
    f1=diff(f,x)
    y_0=f1.subs(x,x_0)

    kq3_T=f"*Hàm số $y={latex(f)}$ có đạo hàm là $y'={latex(-m*a*cos(a*x+b)**(m-1))}\\sin({latex(a*x+b)})$"
    kq3_F=f"Hàm số $y={latex(f)}$ có đạo hàm là $y'={latex(m*cos(a*x+b)**(m-1))}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=my_module.thay_the_ngoac_sincos(f"Khẳng định đã cho là khẳng định đúng.\n\n"\
    f"$y={latex(f)} \\Rightarrow y'={latex(m*cos(a*x+b)**(m-1))}\\left[\\cos({latex(a*x+b)})\\right]'= {latex(-m*a*cos(a*x+b)**(m-1))}\\sin\\left({latex(a*x+b)}\\right)$")
    if kq3==kq3_F:
        loigiai_3=my_module.thay_the_ngoac_sincos(f"Khẳng định đã cho là sai.\n\n"\
        f"$y={latex(f)} \\Rightarrow y'={latex(m*cos(a*x+b)**(m-1))}\\left[\\cos({latex(a*x+b)})\\right]'= {latex(-m*a*cos(a*x+b)**(m-1))}\\sin\\left({latex(a*x+b)}\\right)$.")

    a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f=sqrt(sin(a*x+b))
    if a%2!=0:
        f1=f"\\dfrac{{{a}\\cos({latex(a*x+b)})}}{{2\\sqrt{{\\sin({latex(a*x+b)})}}}}"
        f1_false=f"\\dfrac{{{1}\\cos({latex(a*x+b)})}}{{\\sqrt{{\\sin({latex(a*x+b)})}}}}"
    else:
        t=int(a/2)
        f1=f"\\dfrac{{{t}\\cos({latex(a*x+b)})}}{{\\sqrt{{\\sin({latex(a*x+b)})}}}}"
        f1_false=f"\\dfrac{{{t}\\cos({latex(a*x+b)})}}{{\\sqrt{{\\sin({latex(x+b)})}}}}"

    kq4_T=f"*Hàm số $y={latex(f)}$ có $y'={f1}$"
    kq4_F=f"Hàm số $y={latex(f)}$ có $y'={f1_false}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n"\
    f"$y'=\\dfrac{{\\left[\\sin({latex(a*x+b)})\\right]'}} {{2\\sqrt{{\\sin\\left({latex(a*x+b)}\\right)}}}}"\
        f"={f1}$.".replace(f"{{1\\cos","{{\\cos")
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n"\
        f"$y'=\\dfrac{{\\left[\\sin({latex(a*x+b)})\\right]'}} {{2\\sqrt{{\\sin\\left({latex(a*x+b)}\\right)}}}}"\
        f"={f1}$."
   
    #Trộn các phương án
    list_PA =[kq1, kq2]
    random.shuffle(list_PA)
    list_PA.append(kq3)
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
    f"d) {loigiai[3]}\\\\ \n"

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

#[D11_C7_B4_05]-TF-M2. Tạo câu đúng-sai: 
def ui5io_L11_C7_B4_05():
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
            kq4_T=f"*Vận tốc nhỏ nhất vật đạt được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ là ${v_min}$ m/s"
            kq4_F=f"Vận tốc nhỏ nhất vật đạt được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ là ${g1.subs(t,t_2)}$ m/s"
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






