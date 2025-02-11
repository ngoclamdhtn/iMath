import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
import datetime
# Hàm làm tròn half-up
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

#Tạo hàm bậc 2
def tao_ham_bac_2():
    x=symbols("x")
    a = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.randint(-8, 8)
    ham=a*x**2+b*x+c
    return ham,a,b,c

#Trả về dạng phân số
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

def hien_phan_so(t):
    m=Rational(t).limit_denominator(100000000000)
    return m

def tao_dau(a):
    dau="+"
    if a<0 or a==0:
        dau=""
    return dau

def tao_ngoac(a):
    giatri=f"{a}"
    if a<0:
        giatri=f"({a})"
    return giatri

def xu_li_heso_1(a):
    if a==1:
        heso=""
    elif a==-1:
        heso="-" 
    else:
        heso=a 
    return heso
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
    elif d==0:
        dau="=0"
        x_1=-b/(2*a)
        x_2=-b/(2*a)
    else:
        dau=">0"
        x_1=(-b-sp.sqrt(d))/(2*a)
        x_2=(-b+sp.sqrt(d))/(2*a)
    return dau, x_1, x_2

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
################ Bài 1: PHÉP TÍNH LŨY THỪA ########################
#[D11_C6_B1_01]. Rút gọn a^m.a^n với m,n là phân số.
def zz8zz_L11_C6_B1_01():     
    m1 = random.randint(1,10)
    n1 = random.randint(11,20)
    m2=random.randint(1,10)
    n2=random.randint(11,20)
    m, n=m1/n1, m2/n2
    if m==n: m=n+random.randint(1,4)

    co_so=random.choice(["a","b","x","y"])

    t=m+n
    t2=m*n
    t3=m-n
    t4=m/n   

    kq =f"${{{co_so}^{{{latex(my_module.hien_phan_so(t))}}}}}$"
    kq2=f"${{{co_so}^{{{latex(my_module.hien_phan_so(t2))}}}}}$"
    kq3=f"${{{co_so}^{{{latex(my_module.hien_phan_so(t3))}}}}}$"
    kq4=f"${{{co_so}^{{{latex(my_module.hien_phan_so(t4))}}}}}$"

    kq=kq.replace("\\frac","\\tfrac")
    kq2=kq2.replace("\\frac","\\tfrac")
    kq3=kq3.replace("\\frac","\\tfrac")
    kq4=kq4.replace("\\frac","\\tfrac")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Rút gọn biểu thức $P={co_so}^{{{latex(my_module.hien_phan_so(m))}}}.{co_so}^{{{latex(my_module.hien_phan_so(n))}}}$ với ${co_so}>0$."    
    noi_dung=noi_dung.replace("\\dfrac","\\tfrac")
    noi_dung=noi_dung.replace("\\frac","\\tfrac")      

    debai= f"{noi_dung}\n"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"$P={co_so}^{{{latex(my_module.hien_phan_so(m))}}}.{co_so}^{{{latex(my_module.hien_phan_so(n))}}}={co_so}^{{{latex(my_module.hien_phan_so(m))}+{latex(my_module.hien_phan_so(n))}}}=$ {kq}."    
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


#[D11_C6_B1_02]. Rút gọn (a^m.a^n)/a^p với m,n,p là phân số.
def zz8zz_L11_C6_B1_02():     
    m1 = random.randint(1,9)
    n1 = random.randint(10,15)
    m2=random.randint(1,9)
    n2=random.randint(10,16)
    m3=random.randint(1,9)
    n3=random.randint(10,16)
    m, n, p = m1/n1, m2/n2, m3/n3
    if m==n: m=n+random.randint(1,4)
    if p==m or p ==n: p=p+random.randint(1,4)

    co_so=random.choice(["a","b","x","y"])

    t=m+n-p
    t2=m-n+p
    t3=m-n-p
    t4=m+n+p   

    kq =f"${{{co_so}^{{{latex(my_module.hien_phan_so(t))}}}}}$"
    kq2=f"${{{co_so}^{{{latex(my_module.hien_phan_so(t2))}}}}}$"
    kq3=f"${{{co_so}^{{{latex(my_module.hien_phan_so(t3))}}}}}$"
    kq4=f"${{{co_so}^{{{latex(my_module.hien_phan_so(t4))}}}}}$"

    kq=kq.replace("\\frac","\\tfrac")
    kq2=kq2.replace("\\frac","\\tfrac")
    kq3=kq3.replace("\\frac","\\tfrac")
    kq4=kq4.replace("\\frac","\\tfrac")    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    a_mu_m= f"{co_so}^{{{latex(my_module.hien_phan_so(m))}}}"
    a_mu_n= f"{co_so}^{{{latex(my_module.hien_phan_so(n))}}}"
    a_mu_p= f"{co_so}^{{{latex(my_module.hien_phan_so(p))}}}"

    noi_dung=f"Rút gọn biểu thức $P=\\dfrac{{{a_mu_m}.{a_mu_n}}} {{{a_mu_p}}}$ với ${co_so}>0$." 
    noi_dung=noi_dung.replace("\\dfrac","\\tfrac")
    noi_dung=noi_dung.replace("\\frac","\\tfrac")           

    debai= f"{noi_dung}\n"
    
    noi_dung_loigiai=f"$P=\\dfrac{{{a_mu_m}.{a_mu_n}}}{{{a_mu_p}}}={co_so}^{{{latex(my_module.hien_phan_so(m))} + {latex(my_module.hien_phan_so(n))}-{latex(my_module.hien_phan_so(p))}}}=$ {kq}."    
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

#[D11_C6_B1_03]-M1. Biểu diễn căn bậc sang lũy thừa số mũ hữu tỷ.
def zz8zz_L11_C6_B1_03():    
    n = random.randint(3,7) 
    m = n+ random.randint(10,20)
    co_so=random.choice(["a","b","x","y"])
    t=m/n
    t2=n/m
    t3=m*n
    t4=m+n  

    kq =f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t))}}}}}$"
    kq2=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t2))}}}}}$"
    kq3=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t3))}}}}}$"
    kq4=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t4))}}}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    a_mu_m= f"{co_so}^{{{m}}}"

    noi_dung=f"Cho biểu thức $P=\\sqrt[{n}] {{{a_mu_m}}}$ với ${co_so}>0$. Khẳng định nào sau đây đúng?"         

    debai= f"{noi_dung}\n"


    noi_dung_loigiai=f"$P=\\sqrt[{n}] {{{a_mu_m}}} = {{{co_so}}}^{{\\frac{{{m}}}{{{n}}}}}$. Vậy $P={co_so}^{{{latex(my_module.hien_phan_so(t))}}}$."    
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=noi_dung_loigiai.replace("frac","tfrac")
    
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

#[D11_C6_B1_04]-M2. Biểu diễn tích 2 căn bậc sang lũy thừa số mũ hữu tỷ.
def zz8zz_L11_C6_B1_04():    
    n = random.randint(3,7) 
    m = random.randint(3,7)
    p = random.randint(2,8)    

    co_so=random.choice(["a","b","x","y"])

    t=(n+1/p)*(1/m)
    t2=m+n+p
    t3=m*n/p
    t4=n*p/m  

    kq =f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t))}}}}}$"
    kq2=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t2))}}}}}$"
    kq3=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t3))}}}}}$"
    kq4=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t4))}}}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    a_mu_n= f"{co_so}^{{{n}}}"

    noi_dung=f"Cho biểu thức $P=\\sqrt[{m}] {{{a_mu_n}.\\sqrt[{p}] {{{co_so}}} }}$ với ${co_so}>0$. Khẳng định nào sau đây đúng?"         

    debai= f"{noi_dung}\n"

    noi_dung_loigiai=f"$P=\\sqrt[{m}] {{{a_mu_n}.\\sqrt[{p}] {{{co_so}}}}}= {co_so}^{{\\left({n}+{latex(my_module.hien_phan_so(1/p))}\\right).{latex(my_module.hien_phan_so(1/m))}}}$. Vậy {kq}."    
    noi_dung_loigiai=noi_dung_loigiai.replace("frac","tfrac")
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

#[D11_C6_B1_05]-M3. Biểu diễn tích 3 căn bậc sang lũy thừa số mũ hữu tỷ.
def zz8zz_L11_C6_B1_05():    
    n = random.randint(3,7) 
    m = random.randint(3,7)
    p = random.randint(2,6)  
    q = random.randint(3,8)  

    co_so=random.choice(["a","b","x","y"])

    t=((p+q/2)*(1/n)+1)*(1/m)
    t2=m+n+p+q
    t3=(p+q/2)*(1/(m*n))
    t4=(p+q)*(1/(m*n))
    pa_kotrung=my_module.khong_trung_so(t,t2,t3,t4)
    t2=pa_kotrung[1]
    t3=pa_kotrung[2]
    t4=pa_kotrung[3]

    kq =f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t))}}}}}$"
    kq2=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t2))}}}}}$"
    kq3=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t3))}}}}}$"
    kq4=f"$P={{{co_so}^{{{latex(my_module.hien_phan_so(t4))}}}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    a_mu_n= f"{co_so}^{{{n}}}"

    noi_dung=f"Cho biểu thức $P=\\sqrt[{m}] {{{co_so}.\\sqrt[{n}]{{ {co_so}^{p}. \\sqrt{{{co_so}^{q}}} }} }}$ với ${co_so}>0$. Khẳng định nào sau đây đúng?"         

    debai= f"{noi_dung}\n"

    noi_dung_loigiai=f"$P=\\sqrt[{m}] {{{co_so}.\\sqrt[{n}]{{ {co_so}^{p}. \\sqrt{{{co_so}^{q}}} }} }}= {co_so}^{{\\left(({p}+\\frac{{{q}}}{{2}})\\frac 1 {n}+1\\right).\\frac 1 {m}}}$. Vậy {kq}."    
    noi_dung_loigiai=noi_dung_loigiai.replace("frac","tfrac")
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

#[D11_C6_B1_06]-M3. Tìm k để tích 3 căn bậc = x^m.
def zz8zz_L11_C6_B1_06():    
    n = random.randint(3,7) 
    m = random.randint(3,7)
    p = random.randint(2,6)  
    q = random.randint(3,12)
    k = random.randint(3,8)   

    co_so=random.choice(["a","b","x","y"])

    t=((p+q/k)*(1/n)+1)*(1/m)
    t=latex(my_module.hien_phan_so(t))
    t=t.replace("\\frac","\\tfrac")


    kq =f"${{k= {k}}}$"
    kq2=f"${{k= {k+random.randint(1,3)}}}$"
    kq3=f"${{k= {k+random.randint(4,6)}}}$"
    kq4_1=f"Không tồn tại"
    kq4_2=f"${{k= {k+random.randint(5,8)}}}$"    
    kq4=random.choice([kq4_1,kq4_2])

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    a_mu_n= f"{co_so}^{{{n}}}"

    noi_dung=f"Cho biểu thức $P=\\sqrt[{m}] {{{co_so}.\\sqrt[{n}]{{ {co_so}^{p}.\\sqrt[k]{{{co_so}^{{{q}}}}} }} }}$ với ${co_so}>0$. Tìm ${{k}}$ để $P={co_so}^{{{t}}}$."         

    debai= f"{noi_dung}\n"

    noi_dung_loigiai=f"$P=\\sqrt[{m}] {{{co_so}.\\sqrt[{n}]{{ {co_so}^{p}.\\sqrt[k]{{{co_so}^{{{q}}}}} }} }}= {co_so}^{{\\left(({p}+\\frac{{{q}}}{{k}})\\frac 1 {n}+1\\right).\\frac 1 {m}}}$.\n"\
        
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

#[D11_C6_B1_07]-TF-M2. Tạo câu đúng-sai: Tính chất lũy thừa.    
def zz8zz_L11_C6_B1_07():
    a=sp.symbols("a")      
    noi_dung=f"Cho ${{a}}$ là số thực dương tùy ý. Xét tính đúng sai của các khẳng định sau:"
    m,n=random.randint(2,15), random.randint(2,15)   
    if m==n: n=n+random.randint(1,5)
    kq1_T=f"*$(a^{{{m}}})^{{{n}}}=a^{{{m*n}}}$"
    kq1_F=f"$(a^{{{m}}})^{{{n}}}=a^{{{m+n}}}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"$(a^{{{m}}})^{{{n}}}=a^{{{m*n}}}$ là khẳng định đúng vì $(a^{{{m}}})^{{{n}}}=a^{{{m}.{n}}}=a^{{{m*n}}}$."
    if kq1==kq1_F:
        loigiai_1=f"$(a^{{{m}}})^{{{n}}}=a^{{{m+n}}}$ là khẳng định sai vì $(a^{{{m}}})^{{{n}}}=a^{{{m}.{n}}}=a^{{{m*n}}}$."


    m,n=random.randint(2,15), random.randint(2,15)   
    if m==n: n=n+random.randint(1,5)
    kq2_T=f"*$a^{{{m}}}.a^{{{n}}}=a^{{{m+n}}}$"
    kq2_F=f"$a^{{{m}}}.a^{{{n}}}=a^{{{m*n}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"$a^{{{m}}}.a^{{{n}}}=a^{{{m+n}}}$ là khẳng định đúng vì $a^{{{m}}}.a^{{{n}}}=a^{{{m}+{n}}}=a^{{{m+n}}}$."
    if kq2==kq2_F:
        loigiai_2=f"$a^{{{m}}}.a^{{{n}}}=a^{{{m*n}}}$ là khẳng định sai vì $a^{{{m}}}.a^{{{n}}}=a^{{{m}+{n}}}=a^{{{m+n}}}$."

    m,n=random.randint(2,15), random.randint(2,15)   
    if m==n: n=n+random.randint(1,5)
    kq3_T=f"*$\\dfrac{{a^{{{m}}} }} {{ a^{{{n}}} }}=a^{{{m-n}}}$"
    kq3_F=f"$\\dfrac{{a^{{{m}}} }} {{ a^{{{n}}} }}=a^{{{latex(my_module.hien_phan_so(m/n))}}}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"$\\dfrac{{a^{{{m}}} }} {{ a^{{{n}}} }}=a^{{{m-n}}}$ là khẳng định đúng vì $\\dfrac{{a^{{{m}}} }} {{a^{{{n}}} }}=a^{{{m}-{n}}}=a^{{{m-n}}}$."
    if kq3==kq3_F:
        loigiai_3=f"$\\dfrac{{a^{{{m}}} }} {{ a^{{{n}}} }}=a^{{{latex(my_module.hien_phan_so(m/n))}}}$ là khẳng định sai vì $\\dfrac{{a^{{{m}}} }} {{a^{{{n}}} }}=a^{{{m}-{n}}}=a^{{{m-n}}}$."

    m,n=random.randint(2,15), random.randint(2,15)   
    if m==n: n=n+random.randint(1,5)
    kq4_T=f"*$\\sqrt[{m}] {{ a^{{{n}}} }}= a^{{{latex(my_module.hien_phan_so(n/m))}}}$"
    kq4_F=f"$\\sqrt[{m}] {{ a^{{{n}}} }} = a^{{{latex(my_module.hien_phan_so(m/n))}}}$"
    kq4=random.choice([kq4_T, kq4_F]) 
    loigiai_4=f"$\\sqrt[{m}] {{a^{{{n}}}}}= a^{{{latex(my_module.hien_phan_so(n/m))}}}$ là khẳng định đúng."
    if kq4==kq4_F:
        loigiai_4=f"$\\sqrt[{m}] {{ a^{{{n}}} }} = a^{{{latex(my_module.hien_phan_so(m/n))}}}$ là khẳng định sai vì $\\sqrt[{m}] {{a^{{{n}}}}}= a^{{{latex(my_module.hien_phan_so(n/m))}}}$."  

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

#[D11_C6_B1_08]-TF-M2. Tạo câu đúng-sai: Tính chất của căn bậc n.    
def zz8zz_L11_C6_B1_08():
    a,b=sp.symbols("a b")      
    noi_dung=f"Cho ${{a,b}}$ là các số thực dương tùy ý. Xét tính đúng sai của các khẳng định sau:"
    m,n=random.randint(2,15), random.randint(3,9)   
    if m==n: n=n+random.randint(1,5)
    kq1_T=f"*$\\sqrt[{n}]{{a^{{{m}}}}}= a^{{\\tfrac{{{m}}}{{{n}}}}}$"
    kq1_F=f"$\\sqrt[{n}]{{a^{{{m}}}}}= a^{{\\tfrac{{{n}}}{{{m}}}}}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"$\\sqrt[{n}]a^{{{m}}}= a^{{\\tfrac{{{m}}}{{{n}}}}}$ là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"$\\sqrt[{n}]{{a^{{{m}}}}}= a^{{\\tfrac{{{n}}}{{{m}}}}}$ là khẳng định sai vì $\\sqrt[{n}]{{a^{{{m}}}}}= a^{{\\tfrac{{{m}}}{{{n}}}}}$."
    
    m, n=random.randint(2,15), random.randint(3,9)   
    if m==n: n=n+random.randint(1,5)
    kq2_T=f"*${latex(root(a,n))}. {latex(root(b,n))}={latex(root(a*b,n))}$"
    kq2_F=f"${latex(root(a,n))}. {latex(root(b,n))}={latex(root(a+b,n))}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"${latex(root(a,n))}. {latex(root(b,n))}={latex(root(a*b,n))}$ là khẳng định đúng."
    if kq2==kq2_F:
        loigiai_2=f"${latex(root(a,n))}. {latex(root(b,n))}={latex(root(a+b,n))}$ là khẳng định sai vì ${latex(root(a,n))}. {latex(root(b,n))}={latex(root(a*b,n))}$."

    m, n=random.randint(2,15), random.randint(3,9) 
    kq3_T=f"*${latex(root(a,n)/root(b,n))}={latex(root(a/b,n))}$"
    kq3_F=f"${latex(root(a,n)/root(b,n))}={latex(root(a-b,n))}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"${latex(root(a,n)/root(b,n))}={latex(root(a/b,n))}$ là khẳng định đúng."
    if kq3==kq3_F:
        loigiai_3=f"${latex(root(a,n)/root(b,n))}={latex(root(a/b,n))}$ là khẳng định sai vì ${latex(root(a,n)/root(b,n))}={latex(root(a/b,n))}$."


    m, n=random.randint(3,15), random.randint(3,9)
    kq4_T=f"*$\\sqrt[{n}]{{\\sqrt[{m}] {{ {a}}} }}={latex(root(a,m*n))}$"
    kq4_F=f"$\\sqrt[{n}]{{\\sqrt[{m}] {{ {a}}} }}={latex(root(a,m+n))}$"
    kq4=random.choice([kq4_T, kq4_F]) 
    loigiai_4=f"$\\sqrt[{n}]{{\\sqrt[{m}] {{ {a}}} }}={latex(root(a,m*n))}$ là khẳng định đúng."
    if kq4==kq4_F:
        loigiai_4=f"$\\sqrt[{n}]{{\\sqrt[{m}] {{ {a}}} }}={latex(root(a,m*n))}$ là khẳng định sai vì $\\sqrt[{n}]{{\\sqrt[{m}] {{ {a}}} }}={latex(root(a,m*n))}$."
     
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

#[D11_C6_B1_09]-SA-M2. Cho a^x=t. Tính P=m.a^(2x)+n/a^(2x)+p
def zz8zz_L11_C6_B1_09():
    #a=random.choice(["a","\\alpha", "\\beta", "x", "m" ])
    a=sp.symbols("a")
    while  True:        
        p= random.randint(2,7)
        m= random.choice([i for i in range(-3, 3) if i!=0])
        n= random.choice([i for i in range(-3, 4) if i!=0])

        t_1=random.randint(1,8)
        t_2=t_1+random.randint(1,5)
        t=t_1/t_2
        q= random.choice([i for i in range(-10, 10) if i!=0])
        random.choice([i for i in range(-10, 10) if i!=0])
        if (m*t+n*1/t)**2-2*m*n+q>-9 and (m*t+n*1/t)**2-2*m*n+q<99:
            break 

    noi_dung = (
    f"Cho biết ${p}^{{{a}}}={phan_so(t)}$. Tính giá trị biểu thức $P={latex(m**2*(p**2)**a+n**2*(p**2)**(-a)+q)}$ (kết quả làm tròn đến hàng phần mười)."
    )
    kq=(m*t+n*1/t)**2-2*m*n+q
    dap_an=f"{round_half_up(kq,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$P={latex(m**2*(p**2)**a+n**2*(p**2)**(-a)+q)}=({latex(m*p**a+n*p**(-a))})^2-{2*m*n}+{q}=({m}.{phan_so(t)}+{n}.{phan_so(1/t)})^2+{-2*m*n+q}={dap_an}$."
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("--","+").replace("+-","-")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C6_B1_10]-SA-M2. Cho a^x+a^(-x)=t. Tính P=m.a^(2x)+n.a^(-2x)+p
def zz8zz_L11_C6_B1_10():
    #a=random.choice(["a","\\alpha", "\\beta", "x", "m" ])
    a=sp.symbols("a")
    while  True:        
        p= random.randint(2,7)
        m= random.choice([i for i in range(-3, 3) if i!=0])
        n= random.choice([i for i in range(-3, 4) if i!=0])

        a_0=random.choice([i for i in range(-3, 3) if i!=0])        
        t=m*p**a_0+n*p**(-a_0)
        q= random.choice([i for i in range(-10, 10) if i!=0])
        if t**2-2*m*n+q>-9 and t**2-2*m*n+q<99:
            break 

    noi_dung = (
    f"Cho biết ${latex(m*p**a+n*p**(-a))}={phan_so(t)}$. Tính giá trị biểu thức $P={latex(m**2*(p**2)**a+n**2*(p**2)**(-a)+q)}$ (kết quả làm tròn đến hàng phần mười)."
    )
    kq=(t)**2-2*m*n+q
    dap_an=f"{round_half_up(kq,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$P={latex(m**2*(p**2)**a+n**2*(p**2)**(-a)+q)}=({latex(m*p**a+n*p**(-a))})^2-{2*m*n}+{q}=({phan_so(t)})^2+{-2*m*n+q}={dap_an}$."
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("--","+").replace("+-","-")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C6_B1_11]-SA-M2. Cho m.a^(2x)+n.a^(-2x)=t. Tính P=a^x+a^(-x)+p
def zz8zz_L11_C6_B1_11():
    #a=random.choice(["a","\\alpha", "\\beta", "x", "m" ])
    a=sp.symbols("a")
    while  True:        
        p= random.randint(2,7)
        m= random.choice([i for i in range(1, 3) if i!=0])
        n= random.choice([i for i in range(1, 4) if i!=0])

        a_0=random.choice([i for i in range(-3, 3) if i!=0])        
        t=m*p**a_0+n*p**(-a_0)
        q= random.choice([i for i in range(-10, 10) if i!=0])
        if t**2-2*m*n+q>0 and t**2-2*m*n+q<99:
            break
    

    noi_dung = (
    f"Cho ${latex(m**2*(p**2)**a+n**2*(p**2)**(-a)+q)}={phan_so(t**2-2*m*n+q)}$. Tính giá trị biểu thức $P={latex(m*p**a+n*p**(-a))}$ biết $P>0$ (kết quả làm tròn đến hàng phần mười)."
    )
    kq=t
    dap_an=f"{round_half_up(kq,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$P={latex(m**2*(p**2)**a+n**2*(p**2)**(-a)+q)}=({latex(m*p**a+n*p**(-a))})^2-{2*m*n}+{q}$.\n\n"
    f" Suy ra $({latex(m*p**a+n*p**(-a))})^2={phan_so(t**2-2*m*n+q)}+{2*m*n-q}$.\n\n"
    f" $\\Rightarrow {latex(m*p**a+n*p**(-a))}=\\sqrt{{{phan_so(t**2)}}}={dap_an}$."
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("--","+").replace("+-","-")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C6_B1_12]-SA-M3. Cho a^x=m, a^y=n. Tính giá trị biểu thức chứa lũy thừa a^px, a^qy
def zz8zz_L11_C6_B1_12():
    chon=random.randint(1,2)
    if chon==1:
        a=sp.symbols("a")
    
    if chon==2:
        a=sp.symbols("b")
    x=["\\alpha", "x", "m", "\\beta"]
    y=["\\beta","y", "n", "\\alpha"]
    i=random.randint(0,3)
    x,y=x[i],y[i]
    chon=random.randint(1,2)
    if chon==1:
        x,y=sp.symbols("x y")
    
    if chon==2:
        x,y=sp.symbols("m n")
    while True:
    
        m=random.randint(2,5)
        n=m+random.randint(1,3)

        k_1,k_2,k_3,k_4=random.randint(1,3),random.randint(-3,-1), random.randint(-4,-1), random.randint(1,3)
        q=random.randint(1,10)
        kq=m**(k_1-k_3)*n**(k_2-k_4)+q

        if 0<kq<99:
            break
    
    noi_dung = (
    f"Biết ${a}^{{{x}}}={m}, {a}^{{{y}}}={n}$. Tính $P=\\dfrac{{ {latex((a**k_1)**x)}.{latex((a**k_1)**y)} }} {{ {latex((a**k_3)**x)}.{latex((a**k_1)**y)} }}+{q}$"
    f"(kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(m**(k_1-k_3)*n**(k_2-k_4)+q,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$P=\\dfrac{{ {latex((a**k_1)**x)}.{latex((a**k_1)**y)} }} {{ {latex((a**k_3)**x)}.{latex((a**k_1)**y)} }}$"
    f"  $={latex((a**(k_1-k_3))**x)}.{latex((a**(k_2-k_4))**y)}+{q}={phan_so(m**(k_1-k_3))}.{phan_so(n**(k_2-k_4))}+{q}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

################ Bài 2: PHÉP TÍNH LOGARIT #########################
#[D11_C6_B2_01]-M1. Tìm khẳng định đúng về log_a (a^m)
def zz8zz_L11_C6_B2_01():   
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")

    m =random.randint(2,20)
    
    kq=m
    kq2=f"\\dfrac{{1}}{{{m}}}"
    kq3=-m
    kq4=f"-\\dfrac{{1}}{{{m}}}"


    #Tạo các phương án
    pa_A= f"*$\\log_a a^{{{m}}}={kq}$"
    pa_B= f"$\\log_a a^{{{m}}}={kq2}$"
    pa_C= f"$\\log_a a^{{{m}}}={kq3}$"
    pa_D= f"$\\log_a a^{{{m}}}={kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f" Cho $a$ là số thực dương khác 1. Mệnh đề nào dưới đây đúng?"
    debai= f"{noi_dung}\n"    

    
    noi_dung_loigiai=f"Theo công thức logarit ta có: $\\log_a a^{{{m}}}={kq}$."    
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

#[D11_C6_B2_02]-M1. Tìm khẳng định đúng về log_a (1/a^m)
def zz8zz_L11_C6_B2_02():   
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")

    m =random.randint(2,20)
    
    kq=-m
    kq2=f"\\dfrac{{1}}{{{m}}}"
    kq3=m
    kq4=f"-\\dfrac{{1}}{{{m}}}"


    #Tạo các phương án
    pa_A= f"*$\\log_a \\dfrac{{1}}{{a^{{{m}}}}}={kq}$"
    pa_B= f"$\\log_a \\dfrac{{1}}{{a^{{{m}}}}}={kq2}$"
    pa_C= f"$\\log_a \\dfrac{{1}}{{a^{{{m}}}}}={kq3}$"
    pa_D= f"$\\log_a \\dfrac{{1}}{{a^{{{m}}}}}={kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f" Cho $a$ là số thực dương khác 1. Mệnh đề nào dưới đây đúng?"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    
    noi_dung_loigiai=f"Theo công thức logarit ta có: $\\log_a \\dfrac{{1}}{{a^{{{m}}}}}=\\log_a a^{{{-m}}}={kq}$."    
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

#[D11_C6_B2_03]-M2. Tìm khẳng định đúng về log_can[n](a) (1/a^m)
def zz8zz_L11_C6_B2_03():   
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")

    b =random.randint(2,10)
    n=random.choice([2,3,5,7,])
    n1=n
    if n==2:
        n1=""
        
    kq=-b*n
    kq2=f"\\dfrac{{1}}{{{b*n}}}"
    kq3=b*n
    kq4=f"-\\dfrac{{1}}{{{b*n}}}"


    #Tạo các phương án
    pa_A= f"*$\\log_{{\\sqrt[{{{n1}}}]{{a}}}} \\left(\\dfrac{{1}}{{ a^{{{b}}} }}\\right)={kq}$"
    pa_B= f"$\\log_{{\\sqrt[{{{n1}}}]{{a}}}} \\left(\\dfrac{{1}}{{ a^{{{b}}} }}\\right)={kq2}$"
    pa_C= f"$\\log_{{\\sqrt[{{{n1}}}]{{a}}}} \\left(\\dfrac{{1}}{{ a^{{{b}}} }}\\right)={kq3}$"
    pa_D= f"$\\log_{{\\sqrt[{{{n1}}}]{{a}}}} \\left(\\dfrac{{1}}{{ a^{{{b}}} }}\\right)={kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f" Cho $a$ là số thực dương khác 1. Mệnh đề nào dưới đây đúng?"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
    noi_dung_loigiai=f"Ta có: $\\log_{{\\sqrt[{{{n1}}}]{{a}}}} \\left(\\dfrac{{1}}{{ a^{{{b}}} }}\\right)=\\log_{{a^{{ \\frac{{1}}{{{n}}} }} }} a^{{{-b}}}={-b}.{n}\\log_a a={-b*n}$."    
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

#[D11_C6_B2_04]-M1. Tính giá trị biểu thức chứa logarit bằng máy tính
def zz8zz_L11_C6_B2_04():   
    a=random.choice([2,3,5,7])
    p=a+random.randint(1,3)

    n=random.randint(1,6)
    m=random.randint(2,6)

    b1=a**(n)/p
    b1_tex=latex(my_module.hien_phan_so(a**n/p))
    b2=a**m*a*p 
    b=latex(my_module.hien_phan_so(b1*b2))

    
    kq=n+m+1
    kq2=kq+random.randint(1,7)
    kq3=kq-random.randint(1,7)
    kq4=kq+random.randint(8,15)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Tính giá trị biểu thức $P=\\log_{a}{{{b1_tex}}} + \\log_{a}{{{b2}}}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
    noi_dung_loigiai=f"$P=\\log_{a}{{{b1_tex}}} + \\log_{a}{{{b2}}}=\\log_{a}\\left( {{{b1_tex}.{b2}}} \\right)=\\log_{a} {{{b}}} ={kq}$."    
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

#[D11_C6_B2_05]-M2. Biễu diễn một logarit theo một logarit khác
def zz8zz_L11_C6_B2_05():   
    a=sp.symbols("a")
    b=random.randint(2,5)
    m=random.randint(2,6)
    n=random.randint(1,5)

    c=b**m*10**n   
    
    kq=latex(m*a+n)
    kq2_1=latex(m*a-n)
    kq2_2=latex(n*a-m)
    kq2=random.choice([kq2_1,kq2_2])
    kq3=latex(m*n*a)
    kq4=latex(2*m-3*n*a)
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho $\\log {b}=a$. Biểu diễn $\\log {c}$ theo $a$ ta được"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
    noi_dung_loigiai=f"$\\log {c}=\\log \\left({b}^{m}.10^{n}\\right)=\\log {b}^{m} +\\log 10^{n}={m}\\log {b} +{n}={kq}$."    
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

#[D11_C6_B2_06]-M2. Tìm khẳng định đúng của log_a(a^m.b^n)
def zz8zz_L11_C6_B2_06():   
    a=sp.symbols("a")
    b=sp.symbols("b")

    
    m=random.choice([random.randint(-10, -1), random.randint(1, 10)])
    n=random.choice([random.randint(-10, -1), random.randint(1, 10)])

    c=latex(a**m*b**n)
    n1=xu_li_heso_1(n)
    dau_n=tao_dau(n)
    
    kq=f"{m} {dau_n}{n1}\\log_a b"
    kq2=f"{m*n}\\log_a b"
    kq3=f"{m}\\log_a b"
    kq4=f"{m+n}\\log_a b"

    #Tạo các phương án
    pa_A= f"*$P={{{kq}}}$"
    pa_B= f"$P={{{kq2}}}$"
    pa_C= f"$P={{{kq3}}}$"
    pa_D= f"$P={{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho $P=\\log_a {c}$ với $a>0,b>0$. Tìm khẳng định đúng."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
    noi_dung_loigiai=f"$P=\\log_a {c}=\\log_a a^{{{m}}} +\\log_a b^{{{n}}} ={kq}$."    
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

#[D11_C6_B2_07]-M3. Biểu diễn một logarit theo 2 logarit khác.
def zz8zz_L11_C6_B2_07():   
    
    m=random.randint(2, 7)
    n=random.randint(1, 5)
    n1=xu_li_heso_1(n)
    p=random.randint(1, 5)
    c=random.choice([2,3,5,7,10])
    if c==3 or c==7:
        c1=latex(my_module.hien_phan_so(5*c**m))
        c2=2**n*c**p
        #a=\\log_c 2, b=\\log_c 5        
        kq=f"\\dfrac{{b + {m}}}{{{n1}a +{p}}}"
        kq2=f"\\dfrac{{{m}b}}{{{n1}a +{p+random.randint(1,4)}}}"
        kq3=f"\\dfrac{{{m}b +{p}}}{{{n1}a}}"
        kq4=f"\\dfrac{{b -{m}}}{{{n1}a - {2*p}}}"

        noi_dung=f"Cho $a=\\log_{c} 2, b=\\log_{c} 5$. Hãy biểu diễn $\\log_{{{c2}}}{{{c1}}}$ theo $a$ và $b$."
        noi_dung_loigiai=f"$P=\\log_{{{c2}}}{{{c1}}}=\\dfrac{{ \\log_{c} (5.{c}^{{{m}}}) }} {{ \\log_{c} (2^{{{n1}}}.{c}^{{{p}}}) }}\n"\
                        f"= \\dfrac{{\\log_{c} 5 + \\log_{c} {c}^{{{m}}} }}{{ \\log_{c} 2^{{{n1}}}+ \\log_{c} {c}^{{{p}}} }} ={kq}$."
    elif c==5:
        c1=latex(my_module.hien_phan_so(3*c**m))
        c2=2**n*c**p
        #a=\\log_c 2, b=\\log_c 5        
        kq=f"\\dfrac{{b + {m}}}{{{n1}a +{p}}}"
        kq2=f"\\dfrac{{{m}b}}{{{n1}a +{p+random.randint(1,4)}}}"
        kq3=f"\\dfrac{{{m}b +{p}}}{{{n1}a}}"
        kq4=f"\\dfrac{{b -{m}}}{{{n1}a - {2*p}}}"

        noi_dung=f"Cho $a=\\log_{c} 2, b=\\log_{c} 3$. Hãy biểu diễn $\\log_{{{c2}}}{{{c1}}}$ theo $a$ và $b$."
        noi_dung_loigiai=f"$P=\\log_{{{c2}}}{{{c1}}}=\\dfrac{{ \\log_{c} (3.{c}^{{{m}}}) }} {{ \\log_{c} (2^{{{n1}}}.{c}^{{{p}}}) }}\n"\
                        f"= \\dfrac{{\\log_{c} 3 + \\log_{c} {c}^{{{m}}} }}{{ \\log_{c} 2^{{{n1}}}+ \\log_{c} {c}^{{{p}}} }} ={kq}$."
    elif c==2:
        c1=latex(my_module.hien_phan_so(5*c**m))
        c2=3**n*c**p
        #a=\\log_c 2, b=\\log_c 5        
        kq=f"\\dfrac{{b + {m}}}{{{n1}a +{p}}}"
        kq2=f"\\dfrac{{{m}b}}{{{n1}a +{p+random.randint(1,4)}}}"
        kq3=f"\\dfrac{{{m}b +{p}}}{{{n1}a}}"
        kq4=f"\\dfrac{{b -{m}}}{{{n1}a - {2*p}}}"

        noi_dung=f"Cho $a=\\log_{c} 3, b=\\log_{c} 5$. Hãy biểu diễn $\\log_{{{c2}}}{{{c1}}}$ theo $a$ và $b$."
        noi_dung_loigiai=f"$P=\\log_{{{c2}}}{{{c1}}}=\\dfrac{{ \\log_{c} (5.{c}^{{{m}}}) }} {{ \\log_{c} (3^{{{n1}}}.{c}^{{{p}}}) }}\n"\
                        f"= \\dfrac{{\\log_{c} 5 + \\log_{c} {c}^{{{m}}} }}{{ \\log_{c} 3^{{{n1}}}+ \\log_{c} {c}^{{{p}}} }} ={kq}$."
    else:
        c1=latex(my_module.hien_phan_so(5*2**m))
        c2=2**n*5**p
        #a=\\log_c 2, b=\\log_c 5        
        kq=f"\\dfrac{{b + {m}a}}{{{n1}a +{p}b}}"
        kq2=f"\\dfrac{{{m}b}}{{{n1}a +{p+random.randint(1,4)}}}"
        kq3=f"\\dfrac{{{m}b +{p}}}{{{n1}a}}"
        kq4=f"\\dfrac{{b -{m}}}{{{n1}a - {2*p}}}"

        noi_dung=f"Cho $a=\\log 2, b=\\log 5$. Hãy biểu diễn $\\log_{{{c2}}}{{{c1}}}$ theo $a$ và $b$."
        noi_dung_loigiai=f"$P=\\log_{{{c2}}}{{{c1}}}=\\dfrac{{ \\log (5.2^{{{m}}}) }} {{ \\log (2^{{{n1}}}.5^{{{p}}}) }}\n"\
                        f"= \\dfrac{{\\log 5 + \\log 2^{{{m}}} }}{{ \\log 2^{{{n1}}}+ \\log 5^{{{p}}} }} ={kq}$."



    #Tạo các phương án
    pa_A= f"*$P={{{kq}}}$"
    pa_B= f"$P={{{kq2}}}$"
    pa_C= f"$P={{{kq3}}}$"
    pa_D= f"$P={{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D11_C6_B2_08]-TF-M2. Tạo câu đúng-sai: Tính chất của logarit.    
def zz8zz_L11_C6_B2_08():
    a,b=sp.symbols("a b")      
    noi_dung=f"Cho ${{a,b}}$ là các số thực dương tùy ý. Xét tính đúng sai của các khẳng định sau:"
    m, n=random.randint(2,15), random.randint(3,9)   
    if m==n: n=n+random.randint(1,5)
    kq1_T=f"*$\\log_{{{latex(a**m)}}} {{{b}}}={latex(1/m)}\\log_{{{a}}} {{{b}}}$."
    kq1_F=f"$\\log_{{{latex(a**m)}}} {{{b}}}={m}\\log_{{{a}}} {{{b}}}$"
    loigiai_1=f"$\\log_{{{latex(a**m)}}} {{{b}}}={latex(1/m)}\\log_{{{a}}} {{{b}}}$."

    kq2_T=f"*${latex(log(a**m))}{b}={latex(m*log(a)+log(b))}$."
    kq2_F=random.choice([f"${latex(log(a**m))}{b}={latex(log(a)+m*log(b))}$",\
                        f"${latex(log(a**m))}{b}={latex(my_module.hien_phan_so(1/m))}{latex(log(a)+log(b))}$"\
                        f"${latex(log(a**m))}{b}={latex(m*(log(a))+log(b))}$"])
    loigiai_2=f"$$."

    kq3_T=f"*$$."
    kq3_F=f"$$"
    loigiai_3=f"$$."

    kq4_T=f"*$$."
    kq4_F=f"$$"
    loigiai_4=f"$$."
    
    
    kq1=random.choice([kq1_T, kq1_F])
    kq2=random.choice([kq2_T, kq2_F])
    kq3=random.choice([kq3_T, kq3_F])
    kq4=random.choice([kq4_T, kq4_F])   

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    return debai,debai_latex,loigiai_word,dap_an



################ Bài 3: HÀM SỐ MŨ- HÀM SỐ LOGARIT #################

#[D11_C6_B3_01]. Tập xác định hàm số y=(ax+b)^n với n là số nguyên âm.
def zz8zz_L11_C6_B3_01():
    #Tạo bậc ngẫu nhiên
    a= random.randint(-6,8)
    if a==0:
        a= random.randint(1,8)
    b= random.randint(-6,8)
    if b==0:
        b= random.randint(-10,-1)
    if a==b:
        b=a*2
    if a==-b:
        b=a*2
    n= random.randint(-10,-2)
    x = sp.symbols('x')
    f=latex(a*x+b)
    kq= f"\\displaystyle D=\\mathbb{{R}} \\backslash \\{{{latex(my_module.hien_phan_so(-b/a))}\\}}"
    kq2=f"\\displaystyle D=\\mathbb{{R}} \\backslash \\{{{latex(my_module.hien_phan_so(-a/b))}\\}}"
    kq3=f"\\displaystyle D= ({latex(my_module.hien_phan_so(-b/a))};+\\infty)"
    kq4=f"\\displaystyle D=(-\\infty;{latex(my_module.hien_phan_so(-b/a))})"

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm tập xác định của hàm số $y=({f})^{{{n}}}$."
    noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(a*x+b)}\\ne 0 \\Leftrightarrow x \\ne {latex(my_module.hien_phan_so(-b/a))}$.\n\n"\
    f"Tập xác định: ${kq}$."
    dap_an=my_module.tra_ve_dap_an(list_PA)   
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D11_C6_B3_02]. Tập xác định hàm số y=(ax+b)^n với n là số không nguyên.
def zz8zz_L11_C6_B3_02():
    #Tạo bậc ngẫu nhiên
    a= random.randint(-6,8)
    if a==0:
        a= random.randint(-8,-1)
    b= random.randint(-6,8)
    if b==0:
        b= random.randint(-10,-1)
    if a==b:
        b=a*2
    if a==-b:
        b=a**2+1
    n= random.choice(["e","\\pi","-e", "\\dfrac{1}{3}","-\\dfrac{3}{4}","0,5"])
    x = sp.symbols('x')
    f=latex(a*x+b)
    if a > 0:        
        kq=f"D= \\left({latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"
        kq2=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(-a/b))}\\right\\}}"
        kq3=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(a/b))}\\right\\}}"
        kq4=f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right)"
        
        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(a*x+b)}> 0 \\Leftrightarrow x > {latex(my_module.hien_phan_so(-b/a))}$.\n\n"\
                        f"Tập xác định: $\\displaystyle {kq}$."
    else:
        kq=f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right)"
        kq2=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(-a/b))}\\right\\}}"
        kq3=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(a/b))}\\right\\}}"
        kq4=f"D= \\left({latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"

        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(a*x+b)}> 0 \\Leftrightarrow x < {latex(my_module.hien_phan_so(-b/a))}$.\n\n"\
                        f"Tập xác định: $\\displaystyle {kq}$."

    #Tạo các phương án
    pa_A= f"*$\\displaystyle {kq}$"
    pa_B= f"$\\displaystyle {kq2}$"
    pa_C= f"$\\displaystyle {kq3}$"
    pa_D= f"$\\displaystyle {kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án

    dap_an=my_module.tra_ve_dap_an(list_PA)
    noi_dung= f"Tìm tập xác định của hàm số $y=({f})^{{{n}}}$ . \n"
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D11_C6_B3_03]-M2. TXĐ hàm số y=(ax^2+bx+c)^n với n là số nguyên âm.
def zz8zz_L11_C6_B3_03():   
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")
    chon=random.randint(0,2)
    m=random.randint(-20,-2)
    
    if chon==0:
        #Tạo tam thức vô nghiệm
        a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        if a*c<0:
            c=-c
        b=int(sqrt(4*a*c))-random.randint(1,5)
        f=latex(a*x**2+b*x+c)
        x_0=latex(my_module.hien_phan_so(-b/(2*a))) 
        kq=f"D=\\mathbb{{R}}"
        kq2=f"D=\\mathbb{{R}} \\backslash \\{{{x_0}\\}}"
        kq3=f"D=\\emptyset"
        kq4=random.choice([f"D=\\left({x_0};+\\infty\\right)",f"D=\\left(-\\infty;{x_0}\\right)"])
        noi_dung_loigiai=f"Ta có: ${f}=0$ vô nghiệm nên ${f}\\ne 0$ với mọi $x \\in \\mathbb{{R}}$.\n Tập xác định: ${{{kq}}}$. \n" 

    if chon==1:
        x_0=random.choice([random.randint(-7, -1), random.randint(1, 6)])
        a=random.randint(1,3)
        f=latex(expand(a*(x-x_0)**2))        

        kq=f"D=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}"
        kq2=f"D=\\mathbb{{R}}"
        kq3=f"D=\\emptyset"
        kq4=random.choice([f"D=\\left({x_0};+\\infty\\right)",f"D=\\left(-\\infty;{x_0}\\right)"])

        noi_dung_loigiai=f"Ta có: ${f}=0$ có nghiệm $x={x_0}$ nên ${f} \\ne 0$ với mọi $x \\ne {x_0}$.\n Tập xác định: ${{{kq}}}$. \n" 

    if chon==2:
        a1=random.randint(1,6)
        b1=random.randint(1,15)
        a2=random.randint(1,6)
        b2=random.randint(1,20)
        if a1*b1==a2*b2:
            a2=a1+random.randint(1,4)
        a=a1*a2
        b=a1*b2+b1*a2
        c=b1*b2       
        f=latex(a*x**2+b*x+c)
        if -b1/a1<-b2/a2:   
            x_1=latex(my_module.hien_phan_so(-b1/a1))
            x_2=latex(my_module.hien_phan_so(-b2/a2))
        else:
            x_1=latex(my_module.hien_phan_so(-b2/a2))
            x_2=latex(my_module.hien_phan_so(-b1/a1))

        kq=f"D=\\mathbb{{R}} \\backslash \\left\\{{{x_1};{x_2}\\right\\}}"
        kq2=f"D=\\left[{x_1};{x_2}\\right]"
        kq3=f"D=\\left({x_1};{x_2}\\right)"
        kq4=random.choice([f"D=\\left(-\\infty;{x_1};\\right) \\cup \\left({x_2};+\\infty\\right)"])

        noi_dung_loigiai=f"Ta có: ${f}=0$ có nghiệm $\\displaystyle x_1={x_1},x_2={x_2}$ nên \n ${f} \\ne 0$ với mọi $\\displaystyle x \\ne {x_1}$ và $\\displaystyle x\\ne {x_2}$.\n Tập xác định: ${{{kq}}}$. \n" 

    
    #Tạo các phương án
    pa_A= f"*$\\displaystyle {{{kq}}}$"
    pa_B= f"$\\displaystyle {{{kq2}}}$"
    pa_C= f"$\\displaystyle {{{kq3}}}$"
    pa_D= f"$\\displaystyle {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    
    noi_dung=f"Tìm tập xác định của hàm số $y=\\left({f}\\right)^{{{m}}}$.\n"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

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

#[D11_C6_B3_04]. Tập xác định hàm số y=(ax^2+bx+c)^n không nguyên.
def zz8zz_L11_C6_B3_04():
    x_1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
    x_2= x_1 + random.randint(1,7)
    a=random.choice([random.randint(-3, -1), random.randint(1, 3)])  
    x = sp.symbols('x')
    b=random.randint(1,20)
    c=b+random.randint(2,4)

    n1=random.choice(["\\pi", "e", f"{random.randint(2,8)}e", f"{random.randint(-8,-1)}e",f"{random.randint(2,15)}\\pi"])
    n2=latex(my_module.hien_phan_so(b/c))
    n=random.choice([n1,n2])

    f=sp.expand(a*(x-x_1)*(x-x_2))
    if a > 0:        
        kq=f"D=(-\\infty;{x_1}) \\cup ({x_2};+\\infty)"
        kq2=f"D=({x_1};{x_2})"
        kq3=f"D=[{x_1};{x_2}]"
        kq4=f"D=(-\\infty;{x_1}] \\cup [{x_2};+\\infty)"
        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(f)}>0 \\Leftrightarrow x<{x_1}$ hoặc $x>{x_2}$.\n\n"\
        f"Tập xác định: ${kq}$."
    else:
        kq=f"D=({x_1};{x_2})"
        kq2=f"D=[{x_1};{x_2}]"
        kq3=f"D=(-\\infty;{x_1}) \\cup ({x_2};+\\infty)"
        kq4=f"D=(-\\infty;{x_1}] \\cup [{x_2};+\\infty)"
        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(f)}>0 \\Leftrightarrow {x_1}<x<{x_2}$.\n\n"\
        f"Tập xác định: ${kq}$."

    #Tạo các phương án
    pa_A= f"*$\\displaystyle {kq}$"
    pa_B= f"$\\displaystyle {kq2}$"
    pa_C= f"$\\displaystyle {kq3}$"
    pa_D= f"$\\displaystyle {kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)

    noi_dung= f"Tìm tập xác định của hàm số $\\displaystyle y=\\left({latex(f)}\\right)^{{{n}}}$."

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

#[D11_C6_B3_05]. Tập xác định hàm số y=log(ax+b).
def zz8zz_L11_C6_B3_05():
    a= random.randint(-6,8)
    if a==0:
        a= random.randint(-8,-1)
    b= random.randint(-6,8)
    if b==0:
        b= random.randint(-10,-1)
    if a==b:
        b=a*2
    n= random.randint(2,9)
    x = sp.symbols('x')
    f=latex(a*x+b)
    if a > 0:        
        kq=f"D= \\left( {latex(my_module.hien_phan_so(-b/a))};+\\infty \\right)"
        kq2=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(-a/b))}\\right\\}}"
        kq3=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(-b/a))}\\right\\}}"
        kq4=f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right)"
        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(a*x+b)}> 0 \\Leftrightarrow x > {latex(my_module.hien_phan_so(-b/a))}$.\n\n"\
                        f"Tập xác định: ${kq}$."
    else:
        kq=f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right)"
        kq2=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(-a/b))}\\right\\}}"
        kq3=f"D=\\mathbb{{R}} \\backslash \\left\\{{{latex(my_module.hien_phan_so(-b/a))}\\right\\}}"
        kq4=f"D= \\left({latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"
        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(a*x+b)}> 0 \\Leftrightarrow x < {latex(my_module.hien_phan_so(-b/a))}$.\n\n"\
                        f"Tập xác định: ${kq}$."

    #Tạo các phương án
    pa_A= f"*$\\displaystyle {kq}$"
    pa_B= f"$\\displaystyle {kq2}$"
    pa_C= f"$\\displaystyle {kq3}$"
    pa_D= f"$\\displaystyle {kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm tập xác định của hàm số $\\displaystyle y=\\log_{{{n}}}({f})$." 

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

#[D11_C6_B3_06]. Tập xác định hàm số y=log(ax^2+bx+c).
def zz8zz_L11_C6_B3_06():
    x_1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
    x_2= x_1 + random.randint(1,7)
    a=random.choice([random.randint(-3, -1), random.randint(1, 3)])  
    x = sp.symbols('x')
    n=random.randint(2,9)
    f=sp.expand(a*(x-x_1)*(x-x_2))
    if a > 0:        
        kq=f"D=(-\\infty;{x_1}) \\cup ({x_2};+\\infty)"
        kq2=f"D=({x_1};{x_2})"
        kq3=f"D=[{x_1};{x_2}]"
        kq4=f"D=(-\\infty;{x_1}] \\cup [{x_2};+\\infty)"
        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(f)}>0 \\Leftrightarrow x<{x_1}$ hoặc $x>{x_2}$.\n\n"\
        f"Tập xác định: $\\displaystyle {kq}$."
    else:
        kq=f"D=({x_1};{x_2})"
        kq2=f"D=[{x_1};{x_2}]"
        kq3=f"D=(-\\infty;{x_1}) \\cup ({x_2};+\\infty)"
        kq4=f"D=(-\\infty;{x_1}] \\cup [{x_2};+\\infty)"
        noi_dung_loigiai=f"Điều kiện xác định: $\\displaystyle {latex(f)}>0 \\Leftrightarrow {x_1}<x<{x_2}$.\n\n"\
        f"Tập xác định: $\\displaystyle {kq}$."

    #Tạo các phương án
    pa_A= f"*$\\displaystyle {kq}$"
    pa_B= f"$\\displaystyle {kq2}$"
    pa_C= f"$\\displaystyle {kq3}$"
    pa_D= f"$\\displaystyle {kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm tập xác định của hàm số $y=\\log_{{{n}}}({latex(f)})$."
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

#[D11_C6_B3_07]-M2. Đồ thị hàm số y=a^x
def zz8zz_L11_C6_B3_07():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    a=random.randint(2,7)
    
    if chon==1:
        f=a**x
        x_1, x_2 =-2, 2
        y_1, y_2 = f.subs(x,x_1), f.subs(x,x_2)
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[above left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw (0,{a}) node[left]{{\\footnotesize${a}$}}; \n\
            \\tkzDefPoints{{1/{a}/A}} \n\
            \\tkzDrawPoints[fill=black](A) \n\
            \\draw [dashed] (0,{a})--(1,{a})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{a+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1}:{x_2+0.01}] plot (\\x,{{({a})^(\\x)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
        kq=f"y={a}^x"
        kq2=f"y=\\left({latex(my_module.hien_phan_so(1/a))}\\right)^x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y=x^{a}"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số mũ, đi qua điểm $(1,{a})$ nên đây là đồ thị hàm số ${kq}$." 
    else:
        
        f=a**(-x)
        x_1, x_2 =-2, 2
        y_1, y_2 = f.subs(x,x_2), f.subs(x,x_1)        
        
        code_hinh=f"\\begin{{tikzpicture}}[yscale=.7,>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[right]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw (0,{1/a}) node[left]{{\\footnotesize$\\frac{{1}}{{{a}}}$}}; \n\
            \\tkzDefPoints{{1/{1/a}/A}} \n\
            \\tkzDrawPoints[fill=black](A) \n\
            \\draw [dashed] (0,{1/a})--(1,{1/a})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{a+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1-0.01}:{x_2}] plot (\\x,{{({a})^(-\\x)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"

        kq=f"y=\\left({latex(my_module.hien_phan_so(1/a))}\\right)^x"
        kq2=f"y={a}^x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y=x^{a}"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số mũ, đi qua điểm $(1,{my_module.hien_phan_so(1/a)})$ nên đây là đồ thị hàm số ${kq}$." 
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"

    file_name = my_module.pdftoimage_timename(code)   
 

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đồ thị như hình vẽ dưới đây là của hàm số nào trong các hàm số sau?"
    debai= f"{noi_dung}\n"\
            f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C6_B3_08]-M1. Đồ thị hàm số y=log_a^x
def zz8zz_L11_C6_B3_08():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    a=random.randint(2,7)  
    if chon==1:                 
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] (-1,0) -- ({a+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1.5) -- (0,2.5) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw ({a},0) node[below]{{${a}$}}; \n\
            \\draw[fill=black] ({a}, 1) circle (1pt);\n\
            \\draw [dashed] (0,1)--({a},1)--({a},0); \n\
            \\begin{{scope}}\n\
             \\clip (-1,-1.5) rectangle ({a+0.5},2.5);\n\
            \\draw[color=blue,thick,smooth, samples = 200, domain=0.001:{a+0.5}] plot (\\x,{{(ln(\\x)/ln({a})}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
        kq=f"y=\\log_{a} x"
        kq2=f"y=\\log_{{{latex(my_module.hien_phan_so(1/a))}}} x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y={a}^x"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số logarit, đi qua điểm $({a},1)$ nên đây là đồ thị hàm số ${kq}$." 
    else:    
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] (-1,0) -- ({a+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-2) -- (0,2) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw ({1/a},0) node[below]{{$\\frac{{1}}{{{a}}}$}}; \n\
            \\draw[fill=black] (1,{a}) circle (1pt);\n\
            \\draw [dashed] (0,1)--({1/a},1)--({1/a},0); \n\
            \\begin{{scope}}\n\
             \\clip (-1,-2) rectangle ({a+0.5},2);\n\
            \\draw[color=blue,thick,smooth, samples = 200, domain=0.001:{a+0.5}] plot (\\x,{{(ln(\\x)/ln({1/a})}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"

        kq=f"y=\\log_{{\\frac{{1}}{{{a}}}}} x"
        kq2=f"y=\\log_{a} x"
        kq3=f"y={{{latex(sqrt(a))}}}^x"
        kq4=f"y={a}^x"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số logarit, đi qua điểm $({my_module.hien_phan_so(1/a)},1)$ nên đây là đồ thị hàm số ${kq}$." 

        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"

    file_name = my_module.pdftoimage_timename(code)      

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đồ thị như hình vẽ dưới đây là của hàm số nào trong các hàm số sau?"
    debai= f"{noi_dung}\n"\
            f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C6_B3_09]-M2. Đồ thị hàm số y=căn(a)^x
def zz8zz_L11_C6_B3_09():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    a=random.choice([2,3,5,7,11,13,15])
    b=round(sqrt(a),3)
    chon=1
    if chon==1:
        f=a**(x/2)
        x_1, x_2 =-2, 1.3
        y_1, y_2 = f.subs(x,x_1), f.subs(x,x_2)
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{b+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[above left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw (0,{b}) node[left]{{\\footnotesize $\\sqrt{{{a}}}$}}; \n\
            \\draw[fill=black] (1,{b}) circle (1pt);\n\
            \\draw [dashed] (0,{b})--(1,{b})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{a+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1}:{x_2+0.01}] plot (\\x,{{({b})^(\\x)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"

        kq=f"y=\\sqrt{{{a}}}^x"
        kq2=f"y=\\left( {latex(my_module.hien_phan_so(1/a))} \\right)^x"
        kq3=f"y={{{a}}}^x"
        kq4=f"y=x^{{{a}}}"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số mũ, đi qua điểm $(1,{latex(sqrt(a))})$ nên đây là đồ thị hàm số ${kq}$."
    else:
        
        f=a**(-x/2)
        x_1, x_2 =-2, 1.3
        y_1, y_2 = f.subs(x,x_2), f.subs(x,x_1)
        b=round(sqrt(1/a),3)     
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{b+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[right]{{\\footnotesize $1$}}; \n\
            \\draw (1,0) node[below]{{\\footnotesize $1$}}; \n\
            \\draw (0,{1/b}) node[left]{{\\footnotesize $\\frac{{1}}{{\\sqrt{{{a}}}}}$}}; \n\
            \\draw[fill=black] (1,{1/b}) circle (1pt);\n\
            \\draw [dashed] (0,{1/b})--(1,{1/b})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{b+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1-0.01}:{x_2}] plot (\\x,{{({b})^(-\\x/2)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"

        kq=f"y=\\left(\\dfrac{{1}}{{ \\sqrt{{{a}}} }} \\right)^x"
        kq2=f"y=\\left({latex(my_module.hien_phan_so(1/a))}\\right)^x"
        kq3=f"y={a}^x"
        kq4=f"y=x^{{{a}}}"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số mũ, đi qua điểm $(1,{latex(1/sqrt(a))})$ nên đây là đồ thị hàm số ${kq}$."

        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"

    file_name = my_module.pdftoimage_timename(code)     

      

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đồ thị như hình vẽ dưới đây là của hàm số nào trong các hàm số sau?"
    debai= f"{noi_dung}\n"\
            f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C6_B3_10]-M3. Tìm m để log (ax^2 +bx+c)  có tập xác định là R.
def zz8zz_L11_C6_B3_10(): 
    x=sp.symbols("x")
    m=sp.symbols("m")

    a = random.randint(1, 7)
    n = random.choice([random.randint(2, 9),10,"e", random.randint(11, 20)])

    a1=xu_li_heso_1(a)
    b=random.randint(-5, 5) 
    c= random.randint(-5, 5)
    a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])
    f=f"\\log_{{{n}}} \\left[ {a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) \\right]"
    if n==10:
        f=f"\\log \\left[ {a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) \\right]"
    if n=="e":
        f=f"\\ln \\left[ {a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)}) \\right]"


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

    noi_dung=f"Tìm các giá trị của m để hàm số $y={f}$ xác định với mọi $x\\in \\mathbb{{R}}$."

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

    tich_4a=show_tich(4,a)

    noi_dung_loigiai=f"Ta có: $y={f}$ xác định khi ${a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})>0$.\n\n"\
    f"$\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
            f"${a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})>0$ với mọi $x\\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta <0$\n\n"\
            f"$\\Rightarrow {latex(delta)} <0 \\Rightarrow$ {kq}."       

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

#[D11_C6_B3_11]-M3. Tìm m để e^a/căn(ax^2 +bx+c)  có tập xác định là R.
def zz8zz_L11_C6_B3_11(): 
    x=sp.symbols("x")
    m=sp.symbols("m")

    a = random.randint(1, 7)
    n = random.choice([random.randint(2, 10),"e"])

    a1=xu_li_heso_1(a)
    b=random.randint(-5, 5) 
    c= random.randint(-5, 5)
    a_m = random.choice([random.randint(-5, -1), random.randint(1, 6)])
    f=f"{n}^{{ \\frac{{ {random.randint(1,30)} }} {{ \\sqrt{{ {a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})}} }} }}"
    
    if n=="e":
        f=f"e^{{ \\frac{{ {random.randint(1,30)} }} {{ \\sqrt{{ {a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})}} }} }}"


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

    noi_dung=f"Tìm các giá trị của m để hàm số $y={f}$ xác định với mọi $x\\in \\mathbb{{R}}$."

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

    tich_4a=show_tich(4,a)

    noi_dung_loigiai=f"Ta có: $y={f}$ xác định khi ${a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})>0$.\n\n"\
    f"$\\Delta ={latex((m+b)**2)}-{tich_4a}.({latex(a_m*m+c)})={latex(delta)}$.\n\n"\
            f"${a1}x^2 + ({latex(m+b)})x + ({latex(a_m*m+c)})>0$ với mọi $x\\in \\mathbb{{R}}$ khi và chỉ khi $\\Delta <0$\n\n"\
            f"$\\Rightarrow {latex(delta)} <0 \\Rightarrow$ {kq}."       

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


#[D11_C6_B3_12]-TF-M2. Cho y=a^x, a>1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_12():
    a=random.randint(2,9)
    kq1_T=f"*Hàm số đã cho đồng biến trên $\\mathbb{{R}}$"
    kq1_F=f"Hàm số đã cho nghịch biến trên $\\mathbb{{R}}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Vì ${{{a}}}>1$ nên hàm số đã cho đồng biến trên $\\mathbb{{R}}$."

    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"*Đồ thị hàm số đã cho luôn nằm phía trên trục hoành"
        kq2_F=f'Đồ thị hàm số đã cho luôn nằm {random.choice([f"bên trái trục tung", f"bên phải trục tung", f"phía dưới trục hoành"])}'
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số đã cho luôn nằm phía trên trục hoành là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"Đồ thị hàm số đã cho luôn nằm phía dưới trục hoành là khẳng định sai."

        kq3_T=f"*Hàm số đã cho có tập xác định là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    if chon==2:
        diem_T=random.choice([f"(0;1)", f"(1;{a})", f"(2;{a**2})", f"(3;{a**3})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
        diem_F=random.choice([f"(1;0)",f"({a};1)", f"({a**2};2)", f"({a**3};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
        kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
        kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"Đồ thị hàm số đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

        kq3_T=f"*Hàm số đã cho có tập giá trị là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định sai. Hàm số đã cho có tập giá trị là $(0;+\\infty)$."

    kq4_T=f"*Hàm số liên tục trên $\\mathbb{{R}}$"
    kq4_F=f"Hàm số không liên tục trên $\\mathbb{{R}}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Hàm số liên tục trên $\\mathbb{{R}}$ là khẳng định đúng."
    if kq4==kq4_F:
        loigiai_4=f"Hàm số không liên tục trên $\\mathbb{{R}}$ là khẳng định sai."
               
    noi_dung=f"Cho hàm số $y={a}^{{x}}$. Xét tính đúng sai của các khẳng định sau\n\n"     
 
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S") 
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B3_13]-TF-M2. Cho y=a^x, 0<a<1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_13():
    m=random.randint(2,20)
    n=m+random.randint(4,10)
    a=m/n
    kq1_T=f"*Hàm số đã cho nghịch biến trên $\\mathbb{{R}}$"
    kq1_F=f"Hàm số đã cho đồng biến trên $\\mathbb{{R}}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Vì $0<{{{latex(my_module.hien_phan_so(a))}}}<1$ nên hàm số đã cho nghịch biến trên $\\mathbb{{R}}$."

    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"*Đồ thị hàm số đã cho luôn nằm phía trên trục hoành"
        kq2_F=f'Đồ thị hàm số đã cho luôn nằm {random.choice([f"bên trái trục tung", f"bên dưới trục hoành", f"bên phải trục tung"])}'
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số đã cho luôn nằm phía trên trục hoành là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"Đồ thị hàm số đã cho luôn nằm phía dưới trục hoành là khẳng định sai."

        kq3_T=f"*Hàm số đã cho có tập xác định là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    if chon==2:
        diem_T=random.choice([f"(0;1)", f"(1;{latex(my_module.hien_phan_so(a))})", f"(2;{latex(my_module.hien_phan_so(a**2))})", f"(3;{latex(my_module.hien_phan_so(a**3))})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
        diem_F=random.choice([f"(1;0)",f"({latex(my_module.hien_phan_so(a))};1)", f"({latex(my_module.hien_phan_so(a**2))};2)", f"({latex(my_module.hien_phan_so(a**3))};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
        kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
        kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

        kq3_T=f"*Hàm số đã cho có tập giá trị là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định sai. Hàm số đã cho có tập giá trị là $(0;+\\infty)$."

    kq4_T=f"*Hàm số đã cho liên tục trên $\\mathbb{{R}}$"
    kq4_F=f"Hàm số đã cho không liên tục trên $\\mathbb{{R}}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Hàm số đã cho liên tục trên $\\mathbb{{R}}$ là khẳng định đúng."
    if kq4==kq4_F:
        loigiai_4=f"Hàm số đã cho không liên tục trên $\\mathbb{{R}}$ là khẳng định sai."
               
    noi_dung=f"Cho hàm số $y=\\left({latex(my_module.hien_phan_so(a))}\\right)^{{x}}$. Xét tính đúng sai của các khẳng định sau\n\n"     
    

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S") 
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B3_14]-TF-M2. Cho y=log_a x, a>1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_14():
    a=random.randint(2,9)

    khoang=f"$({random.randint(0,10)};+\\infty)$"
    kq1_T=f"*Trên khoảng {khoang} thì hàm số đã cho đồng biến"
    kq1_F=f"Trên khoảng {khoang} thì hàm số đã cho nghịch biến"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Trên khoảng {khoang} thì hàm số đã cho đồng biến là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai.Trên khoảng {khoang} thì hàm số đã cho đồng biến."


    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"*Đồ thị hàm số đã cho luôn nằm bên phải trục tung"
        kq2_F=f'Đồ thị hàm số đã cho luôn nằm {random.choice([f"bên trái trục tung", f"bên trên trục hoành", f"bên dưới trục hoành"])}'
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"{kq2_T} là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"{kq2_F} là khẳng định sai. Đồ thị hàm số đã cho luôn nằm bên phải trục tung."

        khoang=random.choice([f"$\\mathbb{{R}}$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập xác định là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho tập xác định là $(0;+\\infty)$."

    if chon==2:
        diem_F=random.choice([f"(0;1)", f"(1;{a})", f"(2;{a**2})", f"(3;{a**3})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
        diem_T=random.choice([f"(1;0)",f"({a};1)", f"({a**2};2)", f"({a**3};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
        kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
        kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"Đồ thị hàm số đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

        khoang=random.choice([f"$({random.randint(0,10)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập giá trị là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    khoang=random.choice([f"$({random.randint(-10,-1)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])

    kq4_T=f"*Hàm số liên tục trên khoảng $({random.randint(0,10)};+\\infty)$"
    kq4_F=f"Hàm số liên tục trên khoảng {khoang}"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"{kq4_T} là khẳng định đúng."
    loigiai_4=loigiai_4.replace("*","")
    if kq4==kq4_F:
        loigiai_4=f"{kq4_F} là khẳng định sai. Hàm số đã cho liên tục trên $(0;+\\infty)$."
               
    noi_dung=f"Cho hàm số $y=\\log_{{{a}}} x$. Xét tính đúng sai của các khẳng định sau\n\n"     
 
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B3_15]-TF-M2. Cho y=log_a x, 0<a<1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_15():
    m=random.randint(2,15)
    n=m+random.randint(4,10)
    a=m/n
    khoang=f"$({random.randint(0,10)};+\\infty)$"

    kq1_T=f"*Trên khoảng {khoang} thì hàm số đã cho nghịch biến"
    kq1_F=f"Trên khoảng {khoang} thì hàm số đã cho đồng biến"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Trên khoảng {khoang} thì hàm số đã cho nghịch biến là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai.Trên khoảng {khoang} thì hàm số đã cho nghịch biến."


    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"*Đồ thị hàm số đã cho luôn nằm bên phải trục tung"
        kq2_F=f'Đồ thị hàm số đã cho luôn nằm {random.choice([f"bên trái trục tung", f"bên trên trục hoành", f"bên dưới trục hoành"])}'
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số đã cho luôn nằm bên phải trục tung là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"{kq2_F} là khẳng định sai. Đồ thị hàm số đã cho luôn nằm bên phải trục tung."

        khoang=random.choice([f"$\\mathbb{{R}}$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập xác định là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho tập xác định là $(0;+\\infty)$."

    if chon==2:
        diem_F=random.choice([f"(0;1)", f"(1;{latex(my_module.hien_phan_so(a))})", f"(2;{latex(my_module.hien_phan_so(a**2))})", f"(3;{latex(my_module.hien_phan_so(a**3))})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
        diem_T=random.choice([f"(1;0)",f"({latex(my_module.hien_phan_so(a))};1)", f"({latex(my_module.hien_phan_so(a**2))};2)", f"({latex(my_module.hien_phan_so(a**3))};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
        kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
        kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
        if kq2==kq2_F:
            loigiai_2=f"Đồ thị hàm số đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

        khoang=random.choice([f"$({random.randint(0,10)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập giá trị là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    khoang=random.choice([f"$({random.randint(-10,-1)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])

    kq4_T=f"*Hàm số liên tục trên khoảng $({random.randint(0,10)};+\\infty)$"
    kq4_F=f"Hàm số liên tục trên khoảng {khoang}"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"{kq4_T} là khẳng định đúng."
    loigiai_4=loigiai_4.replace("*","")
    if kq4==kq4_F:
        loigiai_4=f"{kq4_F} là khẳng định sai. Hàm số đã cho liên tục trên $(0;+\\infty)$."
               
    noi_dung=f"Cho hàm số $y=\\log_{{{latex(my_module.hien_phan_so(a))}}} x$. Xét tính đúng sai của các khẳng định sau\n\n"
    noi_dung=noi_dung.replace("\\dfrac","\\tfrac")  
 
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")   
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B3_16]-M2. Đồ thị hàm số y=a^x, a>1
def zz8zz_L11_C6_B3_16():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    a=random.randint(2,7)
    chon=1    
    if chon==1:
        f=a**x
        x_1, x_2 =-2, 2
        y_1, y_2 = f.subs(x,x_1), f.subs(x,x_2)
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[above left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw (0,{a}) node[left]{{\\footnotesize${a}$}}; \n\
            \\tkzDefPoints{{1/{a}/A}} \n\
            \\tkzDrawPoints[fill=black](A) \n\
            \\draw [dashed] (0,{a})--(1,{a})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{a+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1}:{x_2+0.01}] plot (\\x,{{({a})^(\\x)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
        kq=f"y={a}^x"
        kq2=f"y=\\left({latex(my_module.hien_phan_so(1/a))}\\right)^x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y=x^{a}"
    else:
        
        f=a**(-x)
        x_1, x_2 =-2, 2
        y_1, y_2 = f.subs(x,x_2), f.subs(x,x_1)        
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[right]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw (0,{1/a}) node[left]{{\\footnotesize$\\frac{{1}}{{{a}}}$}}; \n\
            \\tkzDefPoints{{1/{1/a}/A}} \n\
            \\tkzDrawPoints[fill=black](A) \n\
            \\draw [dashed] (0,{1/a})--(1,{1/a})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{a+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1-0.01}:{x_2}] plot (\\x,{{({a})^(-\\x)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"

        kq=f"y=\\left({latex(my_module.hien_phan_so(1/a))}\\right)^x"
        kq2=f"y={a}^x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y=x^{a}"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"

    file_name = my_module.pdftoimage_timename(code)      

    
    noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số mũ, đi qua điểm $(1,{4})$ nên đây là đồ thị hàm số ${kq}$."  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đồ thị như hình vẽ dưới đây là của hàm số nào trong các hàm số sau?"
    debai= f"{noi_dung}\n"\
            f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C6_B3_17]-M2. Đồ thị hàm số y=a^x, 0<a<1
def zz8zz_L11_C6_B3_17():
    x=sp.symbols("x")
    a=random.randint(2,7)
    chon=2    
    if chon==1:
        f=a**x
        x_1, x_2 =-2, 2
        y_1, y_2 = f.subs(x,x_1), f.subs(x,x_2)
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[above left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw (0,{a}) node[left]{{\\footnotesize${a}$}}; \n\
            \\tkzDefPoints{{1/{a}/A}} \n\
            \\tkzDrawPoints[fill=black](A) \n\
            \\draw [dashed] (0,{a})--(1,{a})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{a+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1}:{x_2+0.01}] plot (\\x,{{({a})^(\\x)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
        kq=f"y={a}^x"
        kq2=f"y=\\left({latex(my_module.hien_phan_so(1/a))}\\right)^x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y=x^{a}"
    else:
        
        f=a**(-x)
        x_1, x_2 =-2, 2
        y_1, y_2 = f.subs(x,x_2), f.subs(x,x_1)        
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[right]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw (0,{1/a}) node[left]{{\\footnotesize$\\frac{{1}}{{{a}}}$}}; \n\
            \\tkzDefPoints{{1/{1/a}/A}} \n\
            \\tkzDrawPoints[fill=black](A) \n\
            \\draw [dashed] (0,{1/a})--(1,{1/a})--(1,0); \n\
            \\begin{{scope}}\n\
             \\clip (-2,-0.5) rectangle (2,{a+1});\n\
            \\draw[color=blue,very thick,smooth,samples=200, domain={x_1-0.01}:{x_2}] plot (\\x,{{({a})^(-\\x)}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"

        kq=f"y=\\left({latex(my_module.hien_phan_so(1/a))}\\right)^x"
        kq2=f"y={a}^x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y=x^{a}"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"

    file_name = my_module.pdftoimage_timename(code)      

    
    noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số mũ, đi qua điểm $(1,{my_module.hien_phan_so(1/a)})$ nên đây là đồ thị hàm số ${kq}$."  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đồ thị như hình vẽ dưới đây là của hàm số nào trong các hàm số sau?"
    debai= f"{noi_dung}\n"\
            f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C6_B3_18]-M1. Đồ thị hàm số y=log_a^x, a>1
def zz8zz_L11_C6_B3_18():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    a=random.randint(2,7)
    chon=1   
    if chon==1:                 
        
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] (-1,0) -- ({a+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1.5) -- (0,2.5) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw ({a},0) node[below]{{${a}$}}; \n\
            \\draw[fill=black] ({a}, 1) circle (1pt);\n\
            \\draw [dashed] (0,1)--({a},1)--({a},0); \n\
            \\begin{{scope}}\n\
             \\clip (-1,-1.5) rectangle ({a+0.5},2.5);\n\
            \\draw[color=blue,thick,smooth, samples = 200, domain=0.001:{a+0.5}] plot (\\x,{{(ln(\\x)/ln({a})}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"
        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
        kq=f"y=\\log_{a} x"
        kq2=f"y=\\log_{{{latex(my_module.hien_phan_so(1/a))}}} x"
        kq3=f"y={latex(sqrt(a))}^x"
        kq4=f"y={a}^x"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số logarit, đi qua điểm $({a},1)$ nên đây là đồ thị hàm số ${kq}$." 
    else:    
        code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] (-1,0) -- ({a+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-2) -- (0,2) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw ({1/a},0) node[below]{{$\\frac{{1}}{{{a}}}$}}; \n\
            \\draw[fill=black] (1,{a}) circle (1pt);\n\
            \\draw [dashed] (0,1)--({1/a},1)--({1/a},0); \n\
            \\begin{{scope}}\n\
             \\clip (-1,-2) rectangle ({a+0.5},2);\n\
            \\draw[color=blue,thick,smooth, samples = 200, domain=0.001:{a+0.5}] plot (\\x,{{(ln(\\x)/ln({1/a})}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"

        kq=f"y=\\log_{{\\frac{{1}}{{{a}}}}} x"
        kq2=f"y=\\log_{a} x"
        kq3=f"y={{{latex(sqrt(a))}}}^x"
        kq4=f"y={a}^x"
        noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số logarit, đi qua điểm $({my_module.hien_phan_so(1/a)},1)$ nên đây là đồ thị hàm số ${kq}$." 

        code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"

    file_name = my_module.pdftoimage_timename(code)   

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đồ thị như hình vẽ dưới đây là của hàm số nào trong các hàm số sau?"
    debai= f"{noi_dung}\n"\
            f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C6_B3_19]-M1. Đồ thị hàm số y=log_a^x, 0<a<1
def zz8zz_L11_C6_B3_19():
    x=sp.symbols("x")    
    a=random.randint(2,7)    
    code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
        \\draw[->] (-1,0) -- ({a+0.5},0) node[below] {{$x$}}; \n\
        \\draw[->] (0,-2) -- (0,2) node[left] {{$y$}}; \n\
        \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
        \\draw (0,1) node[left]{{$1$}}; \n\
        \\draw (1,0) node[below]{{$1$}}; \n\
        \\draw ({1/a},0) node[below]{{$\\frac{{1}}{{{a}}}$}}; \n\
        \\draw[fill=black] (1,{a}) circle (1pt);\n\
        \\draw [dashed] (0,1)--({1/a},1)--({1/a},0); \n\
        \\begin{{scope}}\n\
         \\clip (-1,-2) rectangle ({a+0.5},2);\n\
        \\draw[color=blue,thick,smooth, samples = 200, domain=0.001:{a+0.5}] plot (\\x,{{(ln(\\x)/ln({1/a})}}); \n\
        \\end{{scope}}\n\
        \\end{{tikzpicture}} \n"

    kq=f"y=\\log_{{\\frac{{1}}{{{a}}}}} x"
    kq2=f"y=\\log_{a} x"
    kq3=f"y={{{latex(sqrt(a))}}}^x"
    kq4=f"y={a}^x"
    noi_dung_loigiai=f"Đồ thị có hình dáng đồ thị của hàm số logarit, đi qua điểm $({my_module.hien_phan_so(1/a)},1)$ nên đây là đồ thị hàm số ${kq}$." 

    code=f"\\documentclass[border=2pt]{{standalone}}\n\
    \\usepackage{{tkz-tab,tikz}} \n\
    \\usetikzlibrary{{calc,intersections,patterns}}\n\
    \\begin{{document}} \n\
    {code_hinh}\
    \\end{{document}}\n"

    file_name = my_module.pdftoimage_timename(code)   

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đồ thị như hình vẽ dưới đây là của hàm số nào trong các hàm số sau?"
    debai= f"{noi_dung}\n"\
            f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C6_B3_20]-M2. Cho hàm số y=a^x. Xét tính đồng biến, nghịch biến.
def zz8zz_L11_C6_B3_20():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    if chon==1:
        a=random.choice([random.randint(2,50),"e",f"\\pi"])
        noi_dung= f"Cho hàm số $y={a}^x$. Tìm khẳng định đúng trong các khẳng định sau."
    
        kq=f"Hàm số đồng biến trên $ {{ \\mathbb{{R}} }}$"
        kq2=f"Hàm số nghịch biến trên ${{\\mathbb{{R}} }}$"
        kq3=f"Hàm số nghịch biến trên khoảng $(-\\infty; {random.randint(-3,10)})$"
        kq4=f"Hàm số chỉ đồng biến trên khoảng $(0; +\\infty)$"

        noi_dung_loigiai=f"Hàm số $y={a}^x$ có cơ số ${a}>1$ nên hàm số đồng biến trên ${{\\mathbb{{R}} }}$." 

    if chon==2:
        m= random.randint(2,18)
        n=m+random.randint(2,7) 
        a= m/n
        noi_dung= f"Cho hàm số $y=\\left({latex(my_module.hien_phan_so(a))}\\right)^x$. Tìm khẳng định đúng trong các khẳng định sau."
        
        kq=f"Hàm số nghịch biến trên ${{ \\mathbb{{R}} }}$"
        kq2=f"Hàm số đồng biến trên ${{\\mathbb{{R}} }}$"
        kq3=f"Hàm số đồng biến trên khoảng $(-\\infty; {random.randint(-3,10)})$"
        kq4=f"Hàm số chỉ nghịch biến trên khoảng $(0; +\\infty)$"

        noi_dung_loigiai=f"Hàm số $y=\\left({latex(my_module.hien_phan_so(a))}\\right)^x$ có cơ số $0<{latex(my_module.hien_phan_so(a))}<1$ nên hàm số nghịch biến trên ${{\\mathbb{{R}}}}$." 
    noi_dung=my_module.frac_to_dfrac(noi_dung)
    noi_dung_loigiai=my_module.frac_to_dfrac(noi_dung_loigiai)
    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    
    debai= f"{noi_dung}\n"

    phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n     C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

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

#[D11_C6_B3_21]-M2. Cho hàm số y=log_a(x). Xét tính đồng biến, nghịch biến.
def zz8zz_L11_C6_B3_21():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    chon=1
    if chon==1:
        a=random.choice([random.randint(2,50),"e",f"\\pi"])
        noi_dung= f"Cho hàm số $y=\\log_{{{a}}} x$. Tìm khẳng định đúng trong các khẳng định sau."

        khoang_F=random.choice([f"({random.randint(-10,-1)};+\\infty)"])
    
        kq=f"Hàm số đồng biến trên $(0; +\\infty)$" 
        kq2=f"Hàm số nghịch biến trên ${{\\mathbb{{R}} }}$"
        kq3=f"Hàm số nghịch biến trên khoảng ${khoang_F}$"
        kq4=f"Hàm số đồng biến trên khoảng ${khoang_F}$"
        noi_dung_loigiai=f"Hàm số $y=\\log_{{{a}}} x$ có cơ số ${a}>1$ nên hàm số đồng biến trên $(0; +\\infty)$." 

    if chon==2:
        m= random.randint(2,18)
        n=m+random.randint(2,7) 
        a= m/n        
        noi_dung= f"Cho hàm số $y=\\log_{{{latex(my_module.hien_phan_so(a))}}} x$. Tìm khẳng định đúng trong các khẳng định sau."

        khoang_F=random.choice([f"({random.randint(-10,-1)};+\\infty)"])
    
        kq=f"Hàm số nghịch biến trên $(0; +\\infty)$" 
        kq2=f"Hàm số đồng biến trên ${{\\mathbb{{R}}}}$"
        kq3=f"Hàm số nghịch biến trên khoảng ${khoang_F}$"
        kq4=f"Hàm số đồng biến trên khoảng ${khoang_F}$"
        noi_dung_loigiai=f"Hàm số $y=\\log_{{{latex(my_module.hien_phan_so(a))}}} x$ có cơ số ${latex(my_module.hien_phan_so(a))}>1$ nên hàm số đồng biến trên $(0; +\\infty)$."  
    noi_dung_loigiai=my_module.frac_to_dfrac(noi_dung_loigiai)
    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    
    debai= f"{noi_dung}\n"

    phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n     C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)

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

#[D11_C6_B3_22]-TF-M2. Cho đồ thị y=a^x, 0<a<1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_22():
    x=sp.symbols("x")
    a=random.randint(2,7)
    f=a**(-x)
    x_1, x_2 =-2, 2
    y_1, y_2 = f.subs(x,x_2), f.subs(x,x_1)        
    
    code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
        \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
        \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
        \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
        \\draw (0,1) node[right]{{$1$}}; \n\
        \\draw (1,0) node[below]{{$1$}}; \n\
        \\draw (0,{1/a}) node[left]{{\\footnotesize$\\frac{{1}}{{{a}}}$}}; \n\
        \\tkzDefPoints{{1/{1/a}/A}} \n\
        \\tkzDrawPoints[fill=black](A) \n\
        \\draw [dashed] (0,{1/a})--(1,{1/a})--(1,0); \n\
        \\begin{{scope}}\n\
         \\clip (-2,-0.5) rectangle (2,{a+1});\n\
        \\draw[color=blue,very thick,smooth,samples=200, domain={x_1-0.01}:{x_2}] plot (\\x,{{({a})^(-\\x)}}); \n\
        \\end{{scope}}\n\
        \\end{{tikzpicture}} \n"
    code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
    file_name = my_module.pdftoimage_timename(code)

    khoang=f"$({random.randint(0,10)};+\\infty)$"

    kq1_T=f"*Trên khoảng {khoang} thì hàm số đã cho nghịch biến"
    kq1_F=f"Trên khoảng {khoang} thì hàm số đã cho đồng biến"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Trên khoảng {khoang} thì hàm số đã cho nghịch biến là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai.Trên khoảng {khoang} thì hàm số đã cho nghịch biến."
    
    diem_F=random.choice([f"(0;1)", f"(1;{latex(my_module.hien_phan_so(a))})", f"(2;{latex(my_module.hien_phan_so(a**2))})", f"(3;{latex(my_module.hien_phan_so(a**3))})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
    diem_T=random.choice([f"(1;0)",f"({latex(my_module.hien_phan_so(a))};1)", f"({latex(my_module.hien_phan_so(a**2))};2)", f"({latex(my_module.hien_phan_so(a**3))};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
    kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
    kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={phan_so(1/a)} \\Rightarrow y={phan_so(1/a)}^x$ nên đồ thị hàm số đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
    if kq2==kq2_F:
        loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={phan_so(1/a)} \\Rightarrow y={phan_so(1/a)}^x$ nên đồ thị hàm số đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

    chon=random.randint(1,2)
    if chon==1:
        khoang=random.choice([f"$\\mathbb{{R}}$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập xác định là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho tập xác định là $(0;+\\infty)$."
    if chon==2:
        khoang=random.choice([f"$({random.randint(0,10)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập giá trị là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    khoang=random.choice([f"$({random.randint(-10,-1)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])

    kq4_T=f"*Trên khoảng $({random.randint(0,10)};+\\infty)$ thì hàm số liên tục"
    kq4_F=f"Hàm số chỉ liên tục trên khoảng {khoang}"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"{kq4_T} là khẳng định đúng."
    loigiai_4=loigiai_4.replace("*","")
    if kq4==kq4_F:
        loigiai_4=f"{kq4_F} là khẳng định sai. Hàm số đã cho liên tục trên $(0;+\\infty)$."
               
    noi_dung=f"Cho đồ thị hàm số $y=a^x$ với $a>0$ có đồ thị như hình vẽ. Xét tính đúng sai của các khẳng định sau\n\n"

 
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
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B3_23]-TF-M2. Cho đồ thị y=log_a x, a>1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_23():
    a=random.randint(2,9)
    code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
            \\draw[->] (-1,0) -- ({a+0.5},0) node[below] {{$x$}}; \n\
            \\draw[->] (0,-1.5) -- (0,2.5) node[left] {{$y$}}; \n\
            \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
            \\draw (0,1) node[left]{{$1$}}; \n\
            \\draw (1,0) node[below]{{$1$}}; \n\
            \\draw ({a},0) node[below]{{${a}$}}; \n\
            \\draw[fill=black] ({a}, 1) circle (1pt);\n\
            \\draw [dashed] (0,1)--({a},1)--({a},0); \n\
            \\begin{{scope}}\n\
             \\clip (-1,-1.5) rectangle ({a+0.5},2.5);\n\
            \\draw[color=blue,thick,smooth, samples = 200, domain=0.001:{a+0.5}] plot (\\x,{{(ln(\\x)/ln({a})}}); \n\
            \\end{{scope}}\n\
            \\end{{tikzpicture}} \n"
    code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
    file_name = my_module.pdftoimage_timename(code)

    khoang=f"$({random.randint(0,10)};+\\infty)$"
    kq1_T=f"*Trên khoảng {khoang} thì hàm số đã cho đồng biến"
    kq1_F=f"Trên khoảng {khoang} thì hàm số đã cho nghịch biến"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Trên khoảng {khoang} thì hàm số đã cho đồng biến là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai.Trên khoảng {khoang} thì hàm số đã cho đồng biến."

    diem_F=random.choice([f"(0;1)", f"(1;{a})", f"(2;{a**2})", f"(3;{a**3})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
    diem_T=random.choice([f"(1;0)",f"({a};1)", f"({a**2};2)", f"({a**3};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
    kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
    kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={a}\\Rightarrow y=\\log_{a} x$ nên đồ thị hàm số đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
    if kq2==kq2_F:
        loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={a}\\Rightarrow y=\\log_{a} x$ nên đồ thị hàm số đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

    chon=random.randint(1,2)
    if chon==1:
        khoang=random.choice([f"$\\mathbb{{R}}$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập xác định là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho tập xác định là $(0;+\\infty)$."
    if chon==2:
        khoang=random.choice([f"$({random.randint(0,10)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập giá trị là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    khoang=random.choice([f"$({random.randint(-10,-1)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])
    kq4_T=f"*Trên khoảng $({random.randint(0,10)};+\\infty)$ thì hàm số liên tục"
    kq4_F=f"Hàm số liên tục trên khoảng {khoang}"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"{kq4_T} là khẳng định đúng."
    loigiai_4=loigiai_4.replace("*","")
    if kq4==kq4_F:
        loigiai_4=f"{kq4_F} là khẳng định sai. Hàm số đã cho liên tục trên $(0;+\\infty)$."
         
    noi_dung=f"Cho đồ thị hàm số $y=\\log_a x$ với $a>0,a \\ne 1$ có đồ thị như hình vẽ. Xét tính đúng sai của các khẳng định sau\n\n"
 
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
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B3_24]-TF-M2. Cho đồ thị y=log_a x, 0<a<1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_24():
    x=sp.symbols("x")    
    a=random.randint(2,7)    
    code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
        \\draw[->] (-1,0) -- ({a+0.5},0) node[below] {{$x$}}; \n\
        \\draw[->] (0,-2) -- (0,2) node[left] {{$y$}}; \n\
        \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
        \\draw (0,1) node[left]{{$1$}}; \n\
        \\draw (1,0) node[below]{{$1$}}; \n\
        \\draw ({1/a},0) node[below]{{$\\frac{{1}}{{{a}}}$}}; \n\
        \\draw[fill=black] (1,{a}) circle (1pt);\n\
        \\draw [dashed] (0,1)--({1/a},1)--({1/a},0); \n\
        \\begin{{scope}}\n\
         \\clip (-1,-2) rectangle ({a+0.5},2);\n\
        \\draw[color=blue,thick,smooth, samples = 200, domain=0.001:{a+0.5}] plot (\\x,{{(ln(\\x)/ln({1/a})}}); \n\
        \\end{{scope}}\n\
        \\end{{tikzpicture}} \n"
    
    code=f"\\documentclass[border=2pt]{{standalone}}\n\
        \\usepackage{{tkz-tab,tikz}} \n\
        \\usetikzlibrary{{calc,intersections,patterns}}\n\
        \\begin{{document}} \n\
        {code_hinh}\
        \\end{{document}}\n"
    file_name = my_module.pdftoimage_timename(code)

    khoang=f"$({random.randint(0,10)};+\\infty)$"

    kq1_T=f"*Trên khoảng {khoang} thì hàm số đã cho nghịch biến"
    kq1_F=f"Trên khoảng {khoang} thì hàm số đã cho đồng biến"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Trên khoảng {khoang} thì hàm số đã cho nghịch biến là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai.Trên khoảng {khoang} thì hàm số đã cho nghịch biến."

    diem_F=random.choice([f"(0;1)", f"(1;{latex(my_module.hien_phan_so(a))})", f"(2;{latex(my_module.hien_phan_so(a**2))})", f"(3;{latex(my_module.hien_phan_so(a**3))})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
    diem_T=random.choice([f"(1;0)",f"({latex(my_module.hien_phan_so(a))};1)", f"({latex(my_module.hien_phan_so(a**2))};2)", f"({latex(my_module.hien_phan_so(a**3))};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
    kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
    kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={phan_so(1/a)}\\Rightarrow y=\\log_{{{phan_so(1/a)}}} x$ nên đồ thị hàm số đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
    if kq2==kq2_F:
        loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={phan_so(1/a)}\\Rightarrow y=\\log_{{{phan_so(1/a)}}} x$ nên đồ thị hàm số đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

    chon=random.randint(1,2)
    if chon==1:
        khoang=random.choice([f"$\\mathbb{{R}}$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập xác định là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho tập xác định là $(0;+\\infty)$."
    if chon==2:
        khoang=random.choice([f"$({random.randint(0,10)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])
        kq3_T=f"*Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập giá trị là {khoang}"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    khoang=random.choice([f"$({random.randint(-10,-1)}; +\\infty)$",f"$(-\\infty;{random.randint(0,10)})$"])

    kq4_T=f"*Trên khoảng $({random.randint(0,10)};+\\infty)$ thì hàm số liên tục"
    kq4_F=f"Hàm số liên tục trên khoảng {khoang}"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"{kq4_T} là khẳng định đúng."
    loigiai_4=loigiai_4.replace("*","")
    if kq4==kq4_F:
        loigiai_4=f"{kq4_F} là khẳng định sai. Hàm số đã cho liên tục trên $(0;+\\infty)$."
             
    noi_dung=f"Cho đồ thị hàm số $y=\\log_a x$ với $a>0,a \\ne 1$ có đồ thị như hình vẽ. Xét tính đúng sai của các khẳng định sau\n\n"
 
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
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B3_25]-TF-M2. Cho đồ thị y=a^x, a>1. Tạo câu hỏi đúng-sai.
def zz8zz_L11_C6_B3_25():
    x=sp.symbols("x")
    a=random.randint(2,7)
    f=a**x
    x_1, x_2 =-2, 2
    y_1, y_2 = f.subs(x,x_1), f.subs(x,x_2)
    
    code_hinh=f"\\begin{{tikzpicture}}[>=stealth] \n\
        \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
        \\draw[->] (0,-1) -- (0,{a+1}) node[left] {{$y$}}; \n\
        \\draw[fill=black] (0,0) node[below right]{{$O$}} circle (1pt);\n\
        \\draw (0,1) node[above left]{{$1$}}; \n\
        \\draw (1,0) node[below]{{$1$}}; \n\
        \\draw (0,{a}) node[left]{{\\footnotesize${a}$}}; \n\
        \\tkzDefPoints{{1/{a}/A}} \n\
        \\tkzDrawPoints[fill=black](A) \n\
        \\draw [dashed] (0,{a})--(1,{a})--(1,0); \n\
        \\begin{{scope}}\n\
         \\clip (-2,-0.5) rectangle (2,{a+1});\n\
        \\draw[color=blue,very thick,smooth,samples=200, domain={x_1}:{x_2+0.01}] plot (\\x,{{({a})^(\\x)}}); \n\
        \\end{{scope}}\n\
        \\end{{tikzpicture}} \n"
    code=f"\\documentclass[border=2pt]{{standalone}}\n\
    \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
    \\usetikzlibrary{{calc,intersections,patterns}}\n\
    \\begin{{document}} \n\
    {code_hinh}\
    \\end{{document}}\n"    
    file_name = my_module.pdftoimage_timename(code)
    kq1_T=f"*Hàm số đã cho đồng biến trên $\\mathbb{{R}}$"
    kq1_F=f"Hàm số đã cho nghịch biến trên $\\mathbb{{R}}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Vì ${{{a}}}>1$ nên hàm số đã cho đồng biến trên $\\mathbb{{R}}$."

    diem_T=random.choice([f"(0;1)", f"(1;{a})", f"(2;{a**2})", f"(3;{a**3})", f"(-1;{latex(my_module.hien_phan_so(1/a))})", f"(-2;{latex(my_module.hien_phan_so(1/a**2))})"])
    diem_F=random.choice([f"(1;0)",f"({a};1)", f"({a**2};2)", f"({a**3};3)", f"({latex(my_module.hien_phan_so(1/a))};-1)", f"({latex(my_module.hien_phan_so(1/a**2))};-2)"])
    kq2_T=f"*Đồ thị hàm số đã cho đi qua điểm ${{{diem_T}}}$"
    kq2_F=f"Đồ thị hàm số đã cho đi qua điểm ${{{diem_F}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={a} \\Rightarrow y={a}^x$ nên đồ thị hàm số đi qua điểm ${{{diem_T}}}$ là khẳng định đúng."
    if kq2==kq2_F:
        loigiai_2=f"Dựa vào đồ thị ta có $\\displaystyle a={a} \\Rightarrow y={a}^x$ nên đồ thị hàm số đi qua điểm ${{{diem_F}}}$ là khẳng định sai."

    chon=random.randint(1,2)
    if chon==1:
        kq3_T=f"*Hàm số đã cho có tập xác định là $\\mathbb{{R}}$"
        kq3_F=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập xác định là $\\mathbb{{R}}$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"Hàm số đã cho có tập xác định là $(0;+\\infty)$ là khẳng định sai. Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$."

    if chon==2:
        kq3_T=f"*Hàm số đã cho có tập giá trị là $(0;+\\infty)$"
        kq3_F=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đã cho có tập giá trị là $(0;+\\infty)$ là khẳng định đúng"
        if kq3==kq3_F:
            loigiai_3=f"Hàm số đã cho có tập giá trị là $\\mathbb{{R}}$ là khẳng định sai. Hàm số đã cho có tập giá trị là $(0;+\\infty)$."

    kq4_T=f"*Hàm số liên tục trên $\\mathbb{{R}}$"
    kq4_F=f"Hàm số không liên tục trên $\\mathbb{{R}}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Hàm số liên tục trên $\\mathbb{{R}}$ là khẳng định đúng."
    if kq4==kq4_F:
        loigiai_4=f"Hàm số không liên tục trên $\\mathbb{{R}}$ là khẳng định sai."   
               
    noi_dung=f"Cho đồ thị hàm số $y=a^x$ với $a>0$ có đồ thị như hình vẽ. Xét tính đúng sai của các khẳng định sau\n\n"

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
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#BÀI 4 PHƯƠNG TRÌNH MŨ - PHƯƠNG TRÌNH LOGARIT

#[D11_C6_B4_01]. Giải phương trình a^x=b.
def zz8zz_L11_C6_B4_01():
    #Tạo bậc ngẫu nhiên
    x_0 = random.choice([random.randint(-5,-1), random.randint(1, 6)])
    a= random.randint(2,7)     
    b= a**(x_0)
    x = sp.symbols('x')

    kq=x_0
    kq2=x_0+random.randint(1,5)
    kq3=x_0+random.randint(6,10)
    kq4=x_0-random.randint(6,10)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{x={kq}}}$"
    pa_B= f"${{x={kq2}}}$"
    pa_C= f"${{x={kq3}}}$"
    pa_D= f"${{x={kq4}}}$"
     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nghiệm của phương trình  ${latex(a**x)}={latex(my_module.hien_phan_so(b))}$."
    noi_dung_loigiai=f"${latex(a**x)}={latex(my_module.hien_phan_so(b))} \\Leftrightarrow x=\\log_{a} {latex(my_module.hien_phan_so(b))}={kq}$"

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
    
#[D11_C6_B4_02]. Giải phương trình a^(x-m)=b.
def zz8zz_L11_C6_B4_02():
    #Tạo bậc ngẫu nhiên
    x_0 = random.choice([random.randint(-5,-1), random.randint(1, 6)])
    a= random.randint(2,7) 
    m= random.choice([random.randint(-5,-1), random.randint(1, 5)])
    b= a**(x_0-m)
    x = sp.symbols('x')

    kq=x_0
    kq2=x_0+random.randint(1,5)
    kq3=x_0+random.randint(6,10)
    kq4=x_0-random.randint(6,10)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{x={kq}}}$"
    pa_B= f"${{x={kq2}}}$"
    pa_C= f"${{x={kq3}}}$"
    pa_D= f"${{x={kq4}}}$"
     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nghiệm của phương trình ${latex(a**(x-m))}={latex(my_module.hien_phan_so(b))}$."
    noi_dung_loigiai=f"${latex(a**(x-m))}={latex(my_module.hien_phan_so(b))} \\Leftrightarrow {latex(x-m)}=\\log_{a} {latex(my_module.hien_phan_so(b))}\\Leftrightarrow x={kq}$."

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

#[D11_C6_B4_03]. Phương trình dạng a^(mx+n)=b^(px+q)
def zz8zz_L11_C6_B4_03():
    x=sp.symbols("x")
    a=random.randint(2,9)
    t=random.randint(2,5)
    
    m,n,p,q=[random.choice([random.randint(-10, -1), random.randint(1, 10)]) for i in range(4)]
    if m-t*p==0: m=m+random.randint(1,4)

    b=a**t
    f_trai=a**(m*x+n)
    f_phai=b**(p*x+q)
    f=f"{latex(f_trai)}={latex(f_phai)}"
    equation = Eq(m*x+n, t*p*x+t*q)   
    kq = (t*q-n)/(m-t*p)
    if m-p!=0:
        kq2=(q-n)/(m-p)
        kq3=(t*q-n)/(m-p)
    else:
        kq2=(q-n)/(m-p+1)
        kq3=(t*q-n)/(m-p+1)
    kq4=kq + random.randint(1,5)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung= f"Tìm nghiệm của phương trình: ${f}$."
    kq=f"{latex(my_module.hien_phan_so(kq))}"
    kq2=f"{latex(my_module.hien_phan_so(kq2))}"
    kq3=f"{latex(my_module.hien_phan_so(kq3))}"
    kq4=f"{latex(my_module.hien_phan_so(kq4))}"

    f_phai=a**(t*(p*x+q))

    noi_dung_loigiai=f"${f} \\Leftrightarrow {latex(f_trai)}={latex(f_phai)}"\
    f"\\Leftrightarrow {latex(m*x+n)}={latex(t*(p*x+q))}\\Leftrightarrow x={kq}$."

    #Tạo các phương án
    pa_A= f"*${{x={kq}}}$"
    pa_B= f"${{x={kq2}}}$"
    pa_C= f"${{x={kq3}}}$"
    pa_D= f"${{x={kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.\n    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

      
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

#[D11_C6_B4_04]. Giải phương trình bậc 2 đối với a^x
def zz8zz_L11_C6_B4_04():
    #Tạo 2 nghiệm
   
    a1=random.randint(1,6)
    b1=random.randint(1,15)
    c1=random.randint(1,6)
    d1=random.randint(1,20)
    a=a1*c1
    b=-(a1*d1+b1*c1)
    c=b1*d1

    #Tạo cơ số m    
    m= random.randint(2,7)
    x = sp.symbols('x')
    f=a*m**(2*x) +b*m**x +c
    t=m**2
    g=a*t**x +b*m**x +c
    chon_ham= random.choice([f,g])

    t_1=(-b-sqrt(b**2-4*a*c))/(2*a)
    t_2=(-b+sqrt(b**2-4*a*c))/(2*a)
    tich=nsimplify(t_1*t_2)
    kq=simplify(log(tich)/log(m))

    if kq.is_Integer == False:
        tam=latex(my_module.hien_phan_so(c/a))
        kq=f"\\log_{m} {tam}"
        kq3=f"{kq}+{random.randint(2,10)}"
    else:
        kq=latex(kq)
        kq3=latex(random.randint(2,10)+simplify(log(tich)/log(m)))

    kq2=t_1+t_2
    kq4=tich*random.randint(2,5)

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{latex(kq2)}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{latex(kq4)}}}$"
     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính tổng các nghiệm của phương trình  ${latex(chon_ham)}=0$."
    noi_dung_loigiai=f""

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

#[D11_C6_B4_05]. Giải phương trình logarit log_a(x)=b
def zz8zz_L11_C6_B4_05():
    #Tạo bậc ngẫu nhiên
    a= random.randint(2,7) 
    b = random.choice([random.randint(-6, -2), random.randint(3, 8)])
    x = sp.symbols('x')

    kq=a**b
    kq2=b**a
    kq3=a*b
    kq4=a+b
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{x={latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${{x={latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{x={latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{x={latex(my_module.hien_phan_so(kq4))}}}$"
     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nghiệm của phương trình  $\\log_{a} x = {b}$."
    noi_dung_loigiai=f"$\\log_{a} x = {b} \\Leftrightarrow x={a}^{{{b}}}={latex(my_module.hien_phan_so(kq))}$."
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

#[D11_C6_B4_09]-TF-M2. Tạo câu hỏi đúng-sai: phương trình a^x=b.
def zz8zz_L11_C6_B4_09():    
    a=random.randint(2,9)
    b=a+random.randint(3,7)    
    kq1_T=f"*Phương trình ${{{a}^x={b}}}$ có nghiệm là $x=\\log_{a} {b}$"
    kq1_F=f"Phương trình ${{{a}^x={b}}}$ có nghiệm là $x=\\log_{b} {a}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Phương trình ${{{a}^x={b}}}$ có nghiệm là $x=\\log_{a} {b}$ là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"Phương trình ${{{a}^x={b}}}$ có nghiệm là $x=\\log_{b} {a}$ là khẳng định sai."

    a=random.randint(2,9)
    b=random.randint(-100,-1)   
    kq2_T=f"*Phương trình ${{{a}^x={b}}}$ vô nghiệm"
    kq2_F=f"Phương trình ${{{a}^x={b}}}$ có nghiệm"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Phương trình ${{{a}^x={b}}}$ có nghiệm là khẳng định đúng."
    if kq2==kq2_F:
        loigiai_2=f"Phương trình ${{{a}^x={b}}}$ có nghiệm là khẳng định sai."


    a=random.randint(2,7)
    n=random.randint(2,6)
    b=a**n  
    kq3_T=f"*Phương trình ${{{a}^x={b}}}$ có nghiệm là ${{x={n}}}$"
    kq3_F=f"Phương trình ${{{a}^x={b}}}$ có nghiệm là ${{x={n+random.randint(1,10)}}}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Phương trình ${{{a}^x={b}}}$ có nghiệm là ${{x={n}}}$ là khẳng định đúng vì ${a}^x={b}\\Leftrightarrow {a}^x={a}^{{{n}}}\\Leftrightarrow x={n}$."
    if kq3==kq3_F:
        loigiai_3=f"{kq3_F} là khẳng định sai vì ${a}^x={b}\\Leftrightarrow {a}^x={a}^{{{n}}}\\Leftrightarrow x={n}$."

    a=random.randint(2,8)
    n=random.randint(2,6)
    b=a**n 
    
    kq4_T=f"*Phương trình ${{{a}^{{x^2}}={b}}}$ có 2 nghiệm phân biệt"
    kq4_F=f'Phương trình ${{{a}^{{x^2}}={b}}}$ {random.choice([f"vô nghiệm", f"có đúng 1 nghiệm", f"có 4 nghiệm phân biệt"])}'
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f" ${{{a}^{{x^2}}={b}}}\\Leftrightarrow {a}^{{x^2}}={a}^{{{n}}}\\Leftrightarrow x^2={n} \\Leftrightarrow x=\\pm {latex(sqrt(n))}$. Vậy phương trình có nghiệm phân biệt."
    
    noi_dung=f"Xét tính đúng sai của các khẳng định sau:\n\n"
   
 
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B4_10]-TF-M2. Tạo câu hỏi đúng-sai: phương trình log_a x=b.
def zz8zz_L11_C6_B4_10():    
    a=random.randint(2,7)
    b=random.choice([a+random.randint(1,3), random.randint(-3,-1)])   
    kq1_T=f"*Phương trình ${{\\log_{a} x={b}}}$ có nghiệm là $x={latex(my_module.hien_phan_so(a**b))}$"
    kq1_F=f"Phương trình ${{\\log_{a} x={b}}}$ có nghiệm là $x={latex(my_module.hien_phan_so(a*b))}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"${{\\log_{a} x={b}}}\\Leftrightarrow x= {a}^{{{b}}}= {latex(my_module.hien_phan_so(a**b))}$."

    
    b=random.randint(1,100)   
    kq2_T=f"*Phương trình ${{\\log_{a} x=\\log_{a} {b}}}$ có nghiệm là ${{x={b}}}$"
    kq2_F=f"Phương trình ${{\\log_{a} x=\\log_{a} {b}}}$ có nghiệm là ${{x={a*b}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"$\\log_{a} x=\\log_{a} {b} \\Leftrightarrow x= {b}$."

    
    b=random.randint(5,20)   
    kq3_T=f"*Phương trình ${{\\log x={b}}}$ có nghiệm là $x=10^{{{b}}}$"
    kq3_F=f"Phương trình ${{\\log x={b}}}$ có nghiệm là $x=e^{{{b}}}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"$\\log x={b} \\Leftrightarrow x=10^{{{b}}}$."

    b=random.randint(5,20)   
    kq4_T=f"*Phương trình ${{\\ln x={b}}}$ có nghiệm là $x=e^{{{b}}}$"
    kq4_F=f"Phương trình ${{\\ln x={b}}}$ có nghiệm là $x=10^{{{b}}}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"${{\\ln x={b}}}\\Leftrightarrow x=e^{{{b}}}$."
    
  
    noi_dung=f"Xét tính đúng sai của các khẳng định sau:\n\n"
   
 
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an

#[D11_C6_B4_10]-TF-M2. Tạo câu hỏi đúng-sai: phương trình log_a x=b.
def zz8zz_L11_C6_B4_10():    
    a=random.randint(2,7)
    b=random.choice([a+random.randint(1,3), random.randint(-3,-1)])   
    kq1_T=f"*Phương trình ${{\\log_{a} x={b}}}$ có nghiệm là $x={latex(my_module.hien_phan_so(a**b))}$"
    kq1_F=f"Phương trình ${{\\log_{a} x={b}}}$ có nghiệm là $x={latex(my_module.hien_phan_so(a*b))}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"${{\\log_{a} x={b}}}\\Leftrightarrow x= {a}^{{{b}}}= {latex(my_module.hien_phan_so(a**b))}$."

    
    b=random.randint(1,100)   
    kq2_T=f"*Phương trình ${{\\log_{a} x=\\log_{a} {b}}}$ có nghiệm là ${{x={b}}}$"
    kq2_F=f"Phương trình ${{\\log_{a} x=\\log_{a} {b}}}$ có nghiệm là ${{x={a*b}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"$\\log_{a} x=\\log_{a} {b} \\Leftrightarrow x= {b}$."

    
    b=random.randint(5,20)   
    kq3_T=f"*Phương trình ${{\\log x={b}}}$ có nghiệm là $x=10^{{{b}}}$"
    kq3_F=f"Phương trình ${{\\log x={b}}}$ có nghiệm là $x=e^{{{b}}}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"$\\log x={b} \\Leftrightarrow x=10^{{{b}}}$."

    b=random.randint(5,20)   
    kq4_T=f"*Phương trình ${{\\ln x={b}}}$ có nghiệm là $x=e^{{{b}}}$"
    kq4_F=f"Phương trình ${{\\ln x={b}}}$ có nghiệm là $x=10^{{{b}}}$"
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"${{\\ln x={b}}}\\Leftrightarrow x=e^{{{b}}}$."
    
  
    noi_dung=f"Xét tính đúng sai của các khẳng định sau:\n\n"
   
 
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an



#BÀI 5 BẤT PHƯƠNG TRÌNH MŨ - PHƯƠNG TRÌNH LOGARIT
#[D11_C6_B5_01]. Giải bất phương trình log_a x > b (a>1)
def zz8zz_L11_C6_B5_01():
    a= random.randint(2,7) 
    b = random.choice([random.randint(-4, -1), random.randint(1, 5)])
    if a==b: b=a+random.randint(1,3)
    dau=random.choice([">",">="])

    if dau==">": 
        latex_dau=">"   
        kq=f"$S=\\left({latex(my_module.hien_phan_so(a**b))};+\\infty\\right)$"
        kq2=f"$S=\\left({latex(my_module.hien_phan_so(b**a))};+\\infty\\right)$"
        kq3=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(a**b))}\\right)$"
        kq4=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(b**a))}\\right)$"
        noi_dung_loigiai=f"${{\\log_{a}x > {b}}} \\Leftrightarrow x>{a}^{{{b}}} \\Leftrightarrow x>{latex(my_module.hien_phan_so(a**b))}$."
    else:
        latex_dau="\\ge"  
        kq=f"$S=\\left[{latex(my_module.hien_phan_so(a**b))};+\\infty\\right)$"
        kq2=f"$S=\\left({latex(my_module.hien_phan_so(b**a))};+\\infty\\right)$"
        kq3=f"$S=\\left[-\\infty;{latex(my_module.hien_phan_so(a**b))}\\right)$"
        kq4=f"$S=\\left[-\\infty;{latex(my_module.hien_phan_so(b**a))}\\right)$"
        noi_dung_loigiai=f"${{\\log_{a}x \\ge {b}}} \\Leftrightarrow x \\ge {a}^{{{b}}} \\Leftrightarrow x \\ge {latex(my_module.hien_phan_so(a**b))}$."

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình ${{\\log_{a}x {latex_dau} {b}}}$."
    
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

#[D11_C6_B5_02]. Giải bất phương trình log_a (x+m) > b (a>1)
def zz8zz_L11_C6_B5_02():
    a= random.randint(2,5) 
    b = random.randint(2, 6)
    m = random.choice([random.randint(-20, -1), random.randint(1, 20)])

    dau="+"
    if m<0:
        dau=""
    dau_bpt=random.choice([">",">="])
    #x=sp.symbols("x")

    if dau_bpt==">": 
        latex_dau_bpt=">"   
        kq=f"$S=({latex(my_module.hien_phan_so(a**b-m))};+\\infty)$"
        kq2=f"$S=[{latex(my_module.hien_phan_so(a**b-m))};+\\infty)$"
        kq3=f"$S=({latex(my_module.hien_phan_so(a**b+m))};+\\infty)$"
        kq4=f"$S=(-\\infty;{latex(my_module.hien_phan_so(a**b+m))})$"
        noi_dung_loigiai=f"$\\log_{a}(x{dau}{m}) {latex_dau_bpt} {b} \\Leftrightarrow (x{dau}{m})>{a}^{{{b}}} \\Leftrightarrow x>{latex(my_module.hien_phan_so(a**b-m))}$."
    else:
        latex_dau_bpt="\\ge"  
        kq=f"$S=[{latex(my_module.hien_phan_so(a**b-m))};+\\infty)$"
        kq2=f"$S=({latex(my_module.hien_phan_so(a**b-m))};+\\infty)$"
        kq3=f"$S=[{latex(my_module.hien_phan_so(a**b+m))};+\\infty)$"
        kq4=f"$S=(-\\infty;{latex(my_module.hien_phan_so(a**b+m))}]$"
        noi_dung_loigiai=f"$\\log_{a}(x{dau}{m}) {latex_dau_bpt} {b} \\Leftrightarrow (x{dau}{m})\\ge {a}^{{{b}}} \\Leftrightarrow x\\ge {latex(my_module.hien_phan_so(a**b-m))}$."

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình $\\log_{a}(x{dau}{m}) {latex_dau_bpt} {b}$."
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

#[D11_C6_B5_03]. Giải BPT log_m(ax+b) > log_m(cx+d), (a>1)
def zz8zz_L11_C6_B5_03():
    x=sp.symbols("x")
    m= random.randint(2,8)
    c = random.randint(1, 3) 
    a = c+ random.randint(1, 5)    
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    if b>0:
        dau_b="+"
    else:
        dau_b=""
    if d>0:
        dau_d="+"
    else:
        dau_d=""
    dau_bpt=random.choice([">",">="])

    x_1=(d-b)/(a-c)
    x_2=-d/c
    x_max=max(x_1,x_2)
    x_min=min(x_1,x_2)


    if dau_bpt==">": 
        latex_dau_bpt=">"   
        kq=f"$S=({latex(my_module.hien_phan_so(x_max))};+\\infty)$"
        kq2=f"$S=({latex(my_module.hien_phan_so(x_min))};+\\infty)$"
        kq3=f"$S=({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))})$"
        kq4=f"$S=(-\\infty;{latex(my_module.hien_phan_so(x_max))})$"

        noi_dung_loigiai=f"Điều kiện:${latex(a*x+b)}>0, {latex(c*x+d)}>0$.\n\n"\
    f"$\\log_{m}({latex(a*x+b)}) {latex_dau_bpt} \\log_{m}({latex(c*x+d)}) \\Leftrightarrow {latex(a*x+b)} {latex_dau_bpt} {latex(c*x+d)}$\n\n"\
    f"$\\Leftrightarrow x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_1))}$. Kết hợp điều kiện ta được nghiệm là: \n\n"\
    f"$x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_max))}$."
        
        
    else:
        latex_dau_bpt="\\ge"
        if x_max==x_1:  
            kq=f"$S=[{latex(my_module.hien_phan_so(x_1))};+\\infty)$"
            noi_dung_loigiai=f"Điều kiện:${latex(a*x+b)}>0, {latex(c*x+d)}>0$.\n\n"\
    f"$\\log_{m}({latex(a*x+b)}) {latex_dau_bpt} \\log_{m}({latex(c*x+d)}) \\Leftrightarrow {latex(a*x+b)} {latex_dau_bpt} {latex(c*x+d)}$\n\n"\
    f"$\\Leftrightarrow x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_1))}$. Kết hợp điều kiện ta được nghiệm là: \n\n"\
    f"$x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_max))}$."

        else:
            kq=f"$S=({latex(my_module.hien_phan_so(x_2))};+\\infty)$"
            noi_dung_loigiai=f"Điều kiện:${latex(a*x+b)}>0, {latex(c*x+d)}>0$.\n\n"\
    f"$\\log_{m}({latex(a*x+b)}) {latex_dau_bpt} \\log_{m}({latex(c*x+d)}) \\Leftrightarrow {latex(a*x+b)} {latex_dau_bpt} {latex(c*x+d)}$\n\n"\
    f"$\\Leftrightarrow x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_1))}$. Kết hợp điều kiện ta được nghiệm là: \n\n"\
    f"$x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_2))}$."

        kq2=f"$S=({latex(my_module.hien_phan_so(x_min))};+\\infty)$"
        kq3=f"$S=({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}]$"
        kq4=f"$S=(-\\infty;{latex(my_module.hien_phan_so(x_max))})$"


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình $\\log_{m}({a}x{dau_b}{b}) {latex_dau_bpt} \\log_{m}({c}x{dau_d}{d})$."
    noi_dung=noi_dung.replace("1x","x")

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

#[D11_C6_B5_04]. Giải bất phương trình a^x > b (a>1)
def zz8zz_L11_C6_B5_04():
    a= random.randint(2,7) 
    t=random.randint(3,10)
    b = random.randint(3, 300)
    x_0=simplify(log(b)/log(a))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem=f"\\log_{a} {b}"
    dau=random.choice([">",">="])

    if dau==">": 
        latex_dau=">"   
        kq=f"$S=({nghiem};+\\infty)$"
        kq2=f"$S=(-\\infty;{nghiem})$"
        kq3=f"$S=[{nghiem};+\\infty)$"
        kq4=f"$S=(-\\infty;{nghiem}]$"
    else:
        latex_dau="\\ge"  
        kq=f"$S=[{nghiem};+\\infty)$"
        kq2=f"$S=(-\\infty;{nghiem})$"
        kq3=f"$S=({nghiem};+\\infty)$"
        kq4=f"$S=(-\\infty;{nghiem}]$"

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình ${a}^x {latex_dau} {b}$ là"
    noi_dung_loigiai=f"${a}^x {latex_dau} {b} \\Leftrightarrow x {latex_dau} \\log_{a} {b} \\Leftrightarrow x {latex_dau} {nghiem}$."

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

#[D11_C6_B5_05]. Giải bất phương trình a^x < b (a>1)
def zz8zz_L11_C6_B5_05():
    a= random.randint(2,7)     
    b = random.randint(3, 300)
    x_0=simplify(log(b)/log(a))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem=f"\\log_{a} {b}"
    dau=random.choice(["<","\\le"])

    if dau=="<": 
        latex_dau="<"   
        kq=f"$S=(-\\infty;{nghiem})$"
        kq2=f"$S=(-\\infty;{nghiem}]$"
        kq3=f"$S=[{nghiem};+\\infty)$"
        kq4=f"$S=({nghiem};+\\infty)$"
    else:
        latex_dau="\\le"  
        kq=f"$S=(-\\infty;{nghiem}]$"
        kq2=f"$S=(-\\infty;{nghiem})$"
        kq3=f"$S=({nghiem};+\\infty)$"
        kq4=f"$S=[{nghiem};+\\infty)$"

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình ${a}^x {latex_dau} {b}$ là"
    noi_dung_loigiai=f"${a}^x {latex_dau} {b} \\Leftrightarrow x {latex_dau} \\log_{a} {b} \\Leftrightarrow x {latex_dau} {nghiem}$."

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

#[D11_C6_B5_06]. Giải bất phương trình a^x < b (0<a<1)
def zz8zz_L11_C6_B5_06():
    m= random.randint(2,18)
    n=m+random.randint(2,7) 
    a= m/n     
    b = random.randint(3, 300)
    x_0=simplify(log(b)/log(a))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem=f"\\log_{{{latex(my_module.hien_phan_so(a))}}} {b}"

    dau=random.choice(["<","\\le"])

    if dau=="<": 
        latex_dau="<"   
        kq=f"$S=\\left({nghiem};+\\infty\\right)$"
        kq2=f"$S=\\left(-\\infty;{nghiem}\\right)$"
        kq3=f"$S=\\left[{nghiem};+\\infty\\right)$"
        kq4=f"$S=\\left(-\\infty;{nghiem}\\right]$"
        noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(a))}\\right)^x < {b} \\Leftrightarrow x > \\log_{{{latex(my_module.hien_phan_so(a))}}} {b} \\Leftrightarrow x > {nghiem}$."
    else:
        latex_dau="\\le"  
        kq=f"$S=\\left[{nghiem};+\\infty\\right)$"
        kq2=f"$S=\\left(-\\infty;{nghiem}\\right)$"
        kq3=f"$S=\\left({nghiem};+\\infty\\right)$"
        kq4=f"$S=\\left(-\\infty;{nghiem}\\right]$"

        noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(a))}\\right)^x \\le {b} \\Leftrightarrow x \\ge \\log_{{{latex(my_module.hien_phan_so(a))}}} {b} \\Leftrightarrow x \\ge {nghiem}$."

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình $\\left({latex(my_module.hien_phan_so(a))}\\right)^x {latex_dau} {b}$ là"
    noi_dung=noi_dung.replace("\\frac","\\dfrac")
    

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

#[D11_C6_B5_07]. Giải bất phương trình a^x > b (0<a<1)
def zz8zz_L11_C6_B5_07():
    m= random.randint(2,18)
    n=m+random.randint(2,7)
    a= m/n     
    b = random.randint(3, 300)
    x_0=simplify(log(b)/log(a))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem=f"\\log_{{{latex(my_module.hien_phan_so(a))}}} {b}"

    dau=random.choice([">","\\ge"])

    if dau==">": 
        latex_dau=">"   
        kq=f"$S=\\left(-\\infty;{nghiem}\\right)$"
        kq2=f"$S=\\left({nghiem};+\\infty\\right)$"
        kq3=f"$S=\\left[{nghiem};+\\infty\\right)$"
        kq4=f"$S=\\left(-\\infty;{nghiem}\\right]$"
        noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(a))}\\right)^x > {b} \\Leftrightarrow x < \\log_{{{latex(my_module.hien_phan_so(a))}}} {b} \\Leftrightarrow x < {nghiem}$."
    else:
        latex_dau="\\ge"  
        kq=f"$S=\\left(-\\infty;{nghiem}\\right]$"
        kq2=f"$S=\\left(-\\infty;{nghiem}\\right)$"
        kq3=f"$S=\\left({nghiem};+\\infty\\right)$"
        kq4=f"$S=\\left[{nghiem};+\\infty\\right)$"

        noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(a))}\\right)^x \\ge {b} \\Leftrightarrow x \\le \\log_{{{latex(my_module.hien_phan_so(a))}}} {b} \\Leftrightarrow x \\le {nghiem}$."

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình $\\left({latex(my_module.hien_phan_so(a))}\\right)^x {latex_dau} {b}$ là"
    noi_dung=noi_dung.replace("\\frac","\\dfrac")
    

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

#[D11_C6_B5_08]. Giải BPT m^(ax+b) > m^(cx+d), (m>1)
def zz8zz_L11_C6_B5_08():
    x=sp.symbols("x")
    m= random.randint(2,17)
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    a = c + random.randint(1, 7)
    if a==0: a=random.randint(1,8)
    if a==-c: a=a+random.randint(1,8)

    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    
    dau_bpt=random.choice([">",">="])

    x_1=(d-b)/(a-c)
    x_2=(b+d)/(a+c)
    x_max=max(x_1,x_2)
    x_min=min(x_1,x_2)

    if a-c>0:
        if dau_bpt==">": 
            latex_dau_bpt=">"   
            kq=f"$S=\\left({latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq2=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right)$"
            kq4=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right)$"

            noi_dung_loigiai=f"${m}^{{{latex(a*x+b)}}} {latex_dau_bpt} {m}^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} {latex_dau_bpt} {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_1))}$.\n\n"
            
        else:
            latex_dau_bpt="\\ge"         
            
            noi_dung_loigiai=f"${m}^{{{latex(a*x+b)}}} {latex_dau_bpt} {m}^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} {latex_dau_bpt} {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x {latex_dau_bpt} {latex(my_module.hien_phan_so(x_1))}$."
            
            kq=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq2=f"$S=\\left({latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right]$"
            kq4=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right)$"
    if a-c<0:
        if dau_bpt==">": 
            latex_dau_bpt=">"   
            kq=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right)$"
            kq2=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right)$"
            kq4=f"$S=\\left({latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"

            noi_dung_loigiai=f"${m}^{{{latex(a*x+b)}}} {latex_dau_bpt} {m}^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} {latex_dau_bpt} {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x <{latex(my_module.hien_phan_so(x_1))}$.\n\n"
            
        else:
            latex_dau_bpt="\\ge"         
            
            noi_dung_loigiai=f"${m}^{{{latex(a*x+b)}}} {latex_dau_bpt} {m}^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} {latex_dau_bpt} {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x \\le {latex(my_module.hien_phan_so(x_1))}$."
            
            kq=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right]$"
            kq2=f"$S=\\left({latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right]$"
            kq4=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình ${m}^{{{latex(a*x+b)}}} {latex_dau_bpt} {m}^{{{latex(c*x+d)}}}$ là"
    noi_dung=noi_dung.replace("1x","x")

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

#[D11_C6_B5_09]. Giải BPT m^(ax+b) > m^(cx+d), (0<m<1)
def zz8zz_L11_C6_B5_09():
    x=sp.symbols("x")
    t_1=random.randint(1,20)
    t_2=t_1+random.randint(2,10)
    m= t_1/t_2

    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    a = c + random.randint(1, 7)
    if a==0: a=random.randint(1,8)
    if a==-c: a=a+random.randint(1,8)

    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    
    dau_bpt=random.choice([">",">="])

    x_1=(d-b)/(a-c)
    x_2=(b+d)/(a+c)
    x_max=max(x_1,x_2)
    x_min=min(x_1,x_2)

    if a-c>0:
        if dau_bpt==">": 
            latex_dau_bpt=">"   
            kq=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right)$"
            kq2=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right)$"
            kq4=f"$S=\\left[{latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right)$"

            noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(a*x+b)}}} > \\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} < {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x < {latex(my_module.hien_phan_so(x_1))}$.\n\n"
            
        else:
            latex_dau_bpt="\\ge"         
            
            noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(a*x+b)}}} \\ge \\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} \\le {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x \\le  {latex(my_module.hien_phan_so(x_1))}$."
            
            kq=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right]$"
            kq2=f"$S=\\left({latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right]$"
            kq4=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
    if a-c<0:
        if dau_bpt==">": 
            latex_dau_bpt=">"   
            kq=f"$S=\\left({latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq2=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right)$"
            kq4=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right)$"

            noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(a*x+b)}}} > \\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} < {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x > {latex(my_module.hien_phan_so(x_1))}$.\n\n"
            
        else:
            latex_dau_bpt="\\ge"         
            
            noi_dung_loigiai=f"$\\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(a*x+b)}}} \\ge \\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} \\le {latex(c*x+d)}$"\
        f"$\\Leftrightarrow x \\ge  {latex(my_module.hien_phan_so(x_1))}$."
            
            kq=f"$S=\\left[{latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$" 
            kq2=f"$S=\\left({latex(my_module.hien_phan_so(x_1))};+\\infty\\right)$"
            kq3=f"$S=\\left({latex(my_module.hien_phan_so(x_min))};{latex(my_module.hien_phan_so(x_max))}\\right]$"
            kq4=f"$S=\\left(-\\infty;{latex(my_module.hien_phan_so(x_1))}\\right]$"

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tập nghiệm của bất phương trình $\\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(a*x+b)}}} {latex_dau_bpt} \\left({latex(my_module.hien_phan_so(m))}\\right)^{{{latex(c*x+d)}}}$ là"
    noi_dung=noi_dung.replace("1x","x")

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

#[D11_C6_B5_10]-TF-M2. Tạo câu hỏi đúng-sai: bất phương trình chứa a^x.
def zz8zz_L11_C6_B5_10():
    #Phương án 1    
    a= random.randint(2,9)    
    b = random.randint(3, 300)
    x_0=simplify(log(b)/log(a))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem=f"\\log_{a} {b}"

    dau=random.choice([">","\\ge"])
    dau_nguoc=random.choice(["<","\\le"])
    kq1_T=f"* Bất phương trình ${{{a}^x {dau} {b}}}$ có nghiệm là $x {dau} {nghiem}$"
    kq1_F=f"Bất phương trình ${{{a}^x {dau} {b}}}$ có nghiệm là $x {dau_nguoc} {nghiem}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Bất phương trình ${{{a}^x {dau} {b}}}$ có nghiệm là $x {dau} {nghiem}$ là khẳng định đúng."
    if kq1==kq1_F:
        loigiai_1=f"Bất phương trình ${{{a}^x {dau} {b}}}$ có nghiệm là $x {dau_nguoc} {nghiem}$ là khẳng định sai.\n\n"\
        f"${{{a}^x {dau} {b}}} \\Leftrightarrow x {dau} {nghiem}$."

    #Phương án 2
    a= random.randint(2,9)    
    b = random.randint(-20, -1)
    dau=random.choice(["<",">","\\le", "\\ge"])
    if dau=="<"or dau=="\\le":    
        kq2_T=f"* Bất phương trình ${{{a}^x {dau} {b}}}$ vô nghiệm"
        kq2_F=f"Bất phương trình ${{{a}^x {dau} {b}}}$ có tập nghiệm là $\\mathbb{{R}}$"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Bất phương trình ${{{a}^x {dau} {b}}}$ vô nghiệm là khẳng định đúng vì ${{{a}^x >0}}$ và ${b}<0$."
        if kq2==kq2_F:
            loigiai_2=f"Bất phương trình ${{{a}^x {dau} {b}}}$ có tập nghiệm là $\\mathbb{{R}}$ là khẳng định sai"\
            f" vì ${{{a}^x >0}}$ và ${b}<0$."

    if dau==">" or dau=="\\ge":    
        kq2_T=f"* Bất phương trình ${{{a}^x {dau} {b}}}$ có tập nghiệm là $\\mathbb{{R}}$"
        kq2_F=f"Bất phương trình ${{{a}^x {dau} {b}}}$ vô nghiệm"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Bất phương trình ${{{a}^x {dau} {b}}}$ có tập nghiệm là $\\mathbb{{R}}$ là khẳng định đúng.\n\n"\
        f"Vì ${{{a}^x >0}}$ và ${b}<0$ nên ${{{a}^x {dau} {b}}}$ với mọi $x\\in \\mathbb{{R}}$."
        if kq2==kq2_F:
            loigiai_2=f"Bất phương trình ${{{a}^x {dau} {b}}}$ vô nghiệm là $\\mathbb{{R}}$ là khẳng định sai.\n\n"\
            f"Vì ${{{a}^x >0}}$ và ${b}<0$ nên ${{{a}^x {dau} {b}}}$ với mọi $x\\in \\mathbb{{R}}$."

    #Phương án 3
    m= random.randint(2,18)
    n=m+random.randint(2,7) 
    a= m/n     
    b = random.randint(3, 300)
    x_0=simplify(log(b)/log(a))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem=f"\\log_{{{latex(my_module.hien_phan_so(a))}}} {b}"

    dau=random.choice(["<","\\le"])
    if dau=="<":
        dau_nguoc=">"
    if dau=="\\le":
        dau_nguoc="\\ge"
    kq3_T=f"* Bất phương trình ${{\\left({latex(my_module.hien_phan_so(a))}\\right)^x {dau} {b}}}$ có nghiệm là $x {dau_nguoc} {nghiem}$"
    kq3_F=f"Bất phương trình ${{\\left({latex(my_module.hien_phan_so(a))}\\right)^x {dau} {b}}}$ có nghiệm là $x {dau} {nghiem}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Bất phương trình ${{{latex(my_module.hien_phan_so(a))}^x {dau} {b}}}$ có nghiệm là $x {dau_nguoc} {nghiem}$ là khẳng định đúng."
    if kq3==kq3_F:
        loigiai_3=f"Bất phương trình ${{{latex(my_module.hien_phan_so(a))}^x {dau} {b}}}$ có nghiệm là $x {dau} {nghiem}$ là khẳng định sai.\n\n"\
        f"${{\\left({latex(my_module.hien_phan_so(a))}\\right)^x {dau} {b}}} \\Leftrightarrow x {dau_nguoc} {nghiem}$."

    #Phương án 4
    x=sp.symbols("x")
    m= random.randint(2,17)
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    a = c + random.randint(1, 7)
    if a==0: a=random.randint(1,8)
    if a==-c: a=a+random.randint(1,8)

    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    
    dau=random.choice([">","\\ge"])
    dau_nguoc=random.choice(["<","\\le"])

    x_1=latex(my_module.hien_phan_so(d-b)/(a-c))
    kq4_T=f"* Bất phương trình ${m}^{{{latex(a*x+b)}}} {dau} {m}^{{{latex(c*x+d)}}}$ có nghiệm là $x {dau} {x_1}$".replace("1x","x")
    kq4_F=f"Bất phương trình ${m}^{{{latex(a*x+b)}}} {dau} {m}^{{{latex(c*x+d)}}}$ có nghiệm là $x {dau_nguoc} {x_1}$".replace("1x","x")
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"${m}^{{{latex(a*x+b)}}} {dau} {m}^{{{latex(c*x+d)}}} \\Leftrightarrow {latex(a*x+b)} {dau} {latex(c*x+d)}$ "\
    f"$\\Leftrightarrow x {dau} {x_1}$."

    noi_dung=f"Xét tính đúng sai của các khẳng định sau:\n\n"   
 
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"    
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")
    return debai,debai_latex,loigiai_word,dap_an



#BÀI 6 - BÀI TOÁN LÃI SUẤT, TĂNG TRƯỞNG.
#[D11_C6_B6_01]. Cho số tiền và lãi suất theo năm. Tính tổng tiền thu được.
def zz8zz_L11_C6_B6_01():
    a= random.randint(10,300) 
    n=random.randint(3,20)
    r=random.choice([4.5, 4.6, 4.7, 4.8, 5, 5.4, 5.5 ,5.6, 6, 7])
    r_phay=str(r)
    r_phay=r_phay.replace(".",",")
    kq=a*(1+r/100)**n
    kq2=a*(1+r/100)**(n-1)
    kq3=a*(1+r/100)**(n+1)
    kq4=a*(1+r/100)**(n-2)

    pa_A= f"*{kq:.2f} triệu đồng"
    pa_B= f"{kq2:.2f} triệu đồng"
    pa_C= f"{kq3:.2f} triệu đồng"
    pa_D= f"{kq4:.2f} triệu đồng"

    pa_A=pa_A.replace(".",",")
    pa_B=pa_B.replace(".",",")
    pa_C=pa_C.replace(".",",")
    pa_D=pa_D.replace(".",",")
     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= (f"Một người gửi tiết kiệm ngân hàng số tiền {a} triệu đồng theo hình thức lãi suất kép với lãi suất ${r_phay}\\%$/năm. "
           f"Tính tổng tiền cả vốn lẫn lãi người đó nhận được sau {n} năm.")
    tong=f"{kq:.2f}"
    tong=tong.replace(".",",")
    noi_dung_loigiai=f"Tổng tiền cả vốn lẫn lãi người đó nhận được sau {n} năm:\n\n"\
                    f"$S={a}\\left(1+{r_phay}\\%\\right)^{{{n}}}={tong}$ (triệu đồng)."

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

#[D11_C6_B6_02]. Cho số tiền và lãi suất theo tháng. Tính tổng tiền thu được sau n tháng.
def zz8zz_L11_C6_B6_02():
    a= random.randint(10,300) 
    n=random.randint(2,8)
    r=random.choice([0.3, 0.35, 0.36, 0.37, 0.4, 0.41, 0.42 ,0.43, 0.44, 0.45,0.46])
    r_phay=str(r)
    r_phay=r_phay.replace(".",",")
    kq=a*(1+r/100)**n
    kq2=a*(1+r/100)**(n-1)
    kq3=a*(1+r/100)**(n+1)
    kq4=a*(1+r/100)**(n-2)

    pa_A= f"*{kq:.2f} triệu đồng"
    pa_B= f"{kq2:.2f} triệu đồng"
    pa_C= f"{kq3:.2f} triệu đồng"
    pa_D= f"{kq4:.2f} triệu đồng"

    pa_A=pa_A.replace(".",",")
    pa_B=pa_B.replace(".",",")
    pa_C=pa_C.replace(".",",")
    pa_D=pa_D.replace(".",",")
     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Một người gửi tiết kiệm ngân hàng số tiền {a} triệu đồng theo hình thức lãi suất kép với lãi suất {r_phay}\\%/tháng. " \
           f"Tính tổng tiền cả vốn lẫn lãi người đó nhận được sau {n} tháng."
    tong=f"{kq:.2f}"
    tong=tong.replace(".",",")

    noi_dung_loigiai=f"Tổng tiền cả vốn lẫn lãi người đó nhận được sau {n} tháng:\n\n"\
                    f"$S={a}\\left(1+{r_phay}\\%\\right)^{{{n}}}={tong}$ (triệu đồng)."

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

#[D11_C6_B6_03]. Cho số tiền và lãi suất/năm. Tính số năm để thu được khoản tiền nào đó.
def zz8zz_L11_C6_B6_03():
    a= random.randint(10,300) 
    n=random.randint(3,20)
    r=random.choice([4.5, 4.6, 4.7, 4.8, 5, 5.4, 5.5 ,5.6, 6, 7])
    r_phay=str(r)
    r_phay=r_phay.replace(".",",")
    tong_tien= int(a*(1+r/100)**n)+1
    kq=n+1
    kq2=n-1
    kq3=n
    kq4=n+2

    pa_A= f"*{kq} năm"
    pa_B= f"{kq2} năm"
    pa_C= f"{kq3} năm"
    pa_D= f"{kq4} năm"

    pa_A=pa_A.replace(".",",")
    pa_B=pa_B.replace(".",",")
    pa_C=pa_C.replace(".",",")
    pa_D=pa_D.replace(".",",")
     #Trộn các phương án

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Một người gửi tiết kiệm ngân hàng số tiền {a} triệu đồng theo hình thức lãi suất kép với lãi suất {r_phay}\\%/năm. " \
           f"Tính thời gian tối thiểu để người đó nhận được số tiền là {tong_tien} triệu đồng."
    nam=f"{kq}"
    nam=nam.replace(".",",")

    noi_dung_loigiai=f"Tổng tiền cả vốn lẫn lãi người đó nhận được sau {n} năm:\n\n"\
                    f"$S={a}\\left(1+{r_phay}\\%\\right)^{{n}}={tong_tien}\\Leftrightarrow n={nam}$ (năm)."

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

#[D11_C6_B6_04]. Cho số tiền và kì hạn theo quý, lãi suất theo năm. Tính tổng tiền thu được sau n năm.
def zz8zz_L11_C6_B6_04():
    a= random.randint(10,300) 
    n=random.randint(3,6)
    r=random.choice([4.5, 4.6, 4.7, 4.8, 5, 5.4, 5.5 ,5.6, 6, 7])
    r_phay=str(r)
    r_phay=r_phay.replace(".",",")
    n_3thang=n*4
    r_3thang=r/4
    r_3thang_phay=str(r_3thang)
    r_3thang_phay=r_3thang_phay.replace(".",",")

    kq=a*(1+r_3thang/100)**n_3thang
    kq2=a*(1+r/100)**n
    kq3=a*(1+r_3thang/100)**n
    kq4=a*(1+r/100)**n_3thang

    pa_A= f"*{kq:.2f} triệu đồng"
    pa_B= f"{kq2:.2f} triệu đồng"
    pa_C= f"{kq3:.2f} triệu đồng"
    pa_D= f"{kq4:.2f} triệu đồng"

    pa_A=pa_A.replace(".",",")
    pa_B=pa_B.replace(".",",")
    pa_C=pa_C.replace(".",",")
    pa_D=pa_D.replace(".",",")
    
    ketqua=f"{kq:.2f}"
    ketqua=ketqua.replace(".",",")

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  
    dap_an=my_module.tra_ve_dap_an(list_PA)   
    noi_dung= f"Một người gửi tiết kiệm ngân hàng số tiền {a} triệu đồng theo hình thức lãi suất kép với kì hạn 3 tháng và lãi suất {r_phay}\\%/năm. " \
           f"Tính tổng tiền cả vốn lẫn lãi người đó nhận được sau {n} năm."
    noi_dung_loigiai=f"Số quý sau {n} năm là: {n_3thang}.\n\n"\
    f"Lãi suất của một quý là: $\\dfrac{{{r}\\%}}{{12}}.3={r_3thang_phay}%$\n\n"\
    f"Tổng tiền cả vốn lẫn lãi người đó nhận được sau {n} năm:\n\n"\
                    f"$S={a}\\left(1+{r_3thang_phay}%\\right)^{{{n_3thang}}}={ketqua}$ (triệu đồng)."
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

#[D11_C6_B6_05]-M2. Cho số dân và tỉ lệ tăng trưởng. Tính số dân sau n năm.
def zz8zz_L11_C6_B6_05():   
    a= random.randint(100,300)/100
    a_phay=str(a)
    a_phay= a_phay.replace(".",",")
    r=random.randint(8,16)/10
    r_phay=str(r)
    r_phay=r_phay.replace(".",",")

    # Lấy ngày và thời gian hiện tại
    ngay_hien_tai = datetime.datetime.now()      

    nam=random.randint(2019,ngay_hien_tai.year)
    thang=ngay_hien_tai.month

    n=random.randint(3,10)
    nam_ketthuc=nam+n

    name_city=random.choice(["A", "B", "C", "X", "Y","Z"])
    
    noi_dung= (f"Biết rằng vào ngày 01/{thang}/{nam}, dân số của thành phố {name_city} có khoảng {a_phay} (triệu người)." 
            f" Nếu tỉ lệ tăng dân số của thành phố {name_city} là {r_phay}\\%/năm và giữ ổn định qua các năm thì vào ngày 01/{thang}/{nam_ketthuc}, dân số của thành phố {name_city} là")    

    kq=a*(1+r/100)**n
    kq2=a*(1+r/100)**(n-1)
    kq3=a*(1+r/100)**(n+1)
    kq4=a*(1+r/100)**(n-2)

    pa_A= f"*{kq:.2f} (triệu người)"
    pa_B= f"{kq2:.2f} (triệu người)"
    pa_C= f"{kq3:.2f} (triệu người)"
    pa_D= f"{kq4:.2f} (triệu người)"

    pa_A=pa_A.replace(".",",")
    pa_B=pa_B.replace(".",",")
    pa_C=pa_C.replace(".",",")
    pa_D=pa_D.replace(".",",")
    
    ketqua=f"{kq:.2f}"
    ketqua=ketqua.replace(".",",")

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  
    dap_an=my_module.tra_ve_dap_an(list_PA)

    noi_dung_loigiai=f"Dân số của thành phố {name_city} sau {n} năm là:\n\n"\
                    f"$S={a_phay}\\left(1+{r_phay}\\%\\right)^{{{n}}}={ketqua}$ (triệu người)."
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

#[D11_C6_B6_06]-M2. Cho mức tiền lương và tỉ lệ tăng lương. Tính mức lương nhận được sau n năm.
def zz8zz_L11_C6_B6_06():   
    a= random.randint(500,900)/100
    a_phay=str(a)
    a_phay= a_phay.replace(".",",")
    r=random.randint(30,40)
    r_phay=str(r)
    r_phay=r_phay.replace(".",",")

    # Lấy ngày và thời gian hiện tại
    ngay_hien_tai = datetime.datetime.now()      

    nam=random.randint(2020,ngay_hien_tai.year)
    thang=ngay_hien_tai.month

    n=random.randint(10, 25)
    so_nam=random.randint(2,3)
    so_lan=int(n/so_nam)
    
    name_cv=random.choice(["công nhân", "nhân viên văn phòng", "kế toán", "kỹ sư", "nhân viên giao hàng","nhân viên bán hàng"])
    
    noi_dung= f"Một người {name_cv} làm việc trong một công ty với mức lương khởi điểm là {a_phay} triệu đồng/tháng." \
            f" Cứ sau {so_nam} năm thì mức lương tăng lên thêm {r_phay}\\%/năm so với mức lương cũ."\
            f" Nếu {name_cv} này làm việc liên tục trong {n} năm thì mức lương hàng tháng của năm thứ {n} là bao nhiêu?"        

    kq=a*(1+r/100)**(so_lan)
    kq2=a*(1+r/100)**(so_lan-1)
    kq3=a*(1+r/100)**(so_lan+1)
    kq4=random.choice([kq+random.randint(10,40)/10,kq-random.randint(10,40)/10])

    pa_A= f"*{kq:.2f} (triệu đồng)"
    pa_B= f"{kq2:.2f} (triệu đồng)"
    pa_C= f"{kq3:.2f} (triệu đồng)"
    pa_D= f"{kq4:.2f} (triệu đồng)"

    pa_A=pa_A.replace(".",",")
    pa_B=pa_B.replace(".",",")
    pa_C=pa_C.replace(".",",")
    pa_D=pa_D.replace(".",",")
    
    ketqua=f"{kq:.2f}"
    ketqua=ketqua.replace(".",",")

    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  
    dap_an=my_module.tra_ve_dap_an(list_PA)

    noi_dung_loigiai=f"Số lần được tăng lương sau {n} năm là: {so_lan-1}.\n\n"\
                    f"Mức lương của người {name_cv} sau {n} năm là:\n\n"\
                    f"$S={a_phay}\\left(1+{r_phay}\\%\\right)^{{{so_lan}}}={ketqua}$ (triệu đồng)."
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

#Phương trình logarit

#[D11_C6_B4_06]-M2. Giải phương trình log_a(mx+n)=b
def zz8zz_L11_C6_B4_06():   

    x=sp.symbols("x")
    a=random.randint(2,5)
    b=random.randint(1,7)
    m = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    n = random.choice([random.randint(-10, -1), random.randint(1, 10)])    
    
    noi_dung=f"Nghiệm của phương trình $\\log_{{{a}}}({latex(m*x+n)})={b}$ là."
    kq=(a**b-n)/m
    kq2=(a*b-n)/m
    kq3=a**b-n
    kq4=kq+random.randint(1,4)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=latex(my_module.hien_phan_so(kq))
    kq2=latex(my_module.hien_phan_so(kq2))
    kq3=latex(my_module.hien_phan_so(kq3))
    kq4=latex(my_module.hien_phan_so(kq4))

      
    #Tạo các phương án
    pa_A= f"*$x={{{kq}}}$"
    pa_B= f"$x={{{kq2}}}$"
    pa_C= f"$x={{{kq3}}}$"
    pa_D= f"$x={{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)     

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"$\\log_{{{a}}}({latex(m*x+n)})={b} \\Rightarrow {latex(m*x+n)}={a}^{b}\\Rightarrow x=\\dfrac{{{a**b}-{tao_ngoac(n)}}} {{{m}}}"\
                    f"\\Rightarrow x= {kq}$."
   
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

#[D11_C6_B4_07]-M3. Giải phương trình log_m(ax+b) - log_m(cx+d) = e
def zz8zz_L11_C6_B4_07():   

    x=sp.symbols("x")
    m=random.randint(2,6)
    e=random.randint(1,4)
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d = random.choice([random.randint(-10, -1), random.randint(1, 10)])  

    if a==c: c=a+random.randint(1,3)  
    
    equation = Eq(a*x + b, m**e*(c*x+d))   
    x_0 = solve(equation, x)

    x_0,tam=x_0[0],my_module.hien_phan_so(x_0[0])

    equation_1 = Eq(a*x + b, m*e*(c*x+d))   
    x_1 = solve(equation, x)
    x_1=x_1[0]

    equation_2 = Eq(a*x + b, e*(c*x+d))   
    x_2 = solve(equation, x)
    x_2=x_2[0]
    
    noi_dung=f"Nghiệm của phương trình $\\log_{m}({latex(a*x+b)}) - \\log_{m}({latex(c*x+d)})={e}$ là."
    kq=x_0
    kq2=x_1
    kq3=x_2
    kq4=kq+random.randint(1,4)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=latex(my_module.hien_phan_so(kq))
    kq2=latex(my_module.hien_phan_so(kq2))
    kq3=latex(my_module.hien_phan_so(kq3))
    kq4=latex(my_module.hien_phan_so(kq4))
    t_kq=f"${{x={kq}}}$"

    pa_A= f"*${{x={kq}}}$"
    if a*x_0+b<=0 or c*x_0+d<=0:
        pa_A= f"*Phương trình vô nghiệm"
        t_kq="phương trình vô nghiệm"
      
    #Tạo các phương án   
    pa_B= f"${{x={kq2}}}$"
    pa_C= f"${{x={kq3}}}$"
    pa_D= f"${{x={kq4}}}$"


    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)     

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Điều kiện: ${latex(a*x+b)}>0$ và ${latex(c*x+d)}>0$.\n\n"\
                    f"$\\log_{m}({latex(a*x+b)}) - \\log_{m}({latex(c*x+d)})={e}"\
                    f"\\Leftrightarrow \\log_{m}{latex((a*x+b)/(c*x+d))}={e}"\
                    f"\\Leftrightarrow {latex((a*x+b)/(c*x+d))}={m}^{e}$\n\n"\
                    f"$\\Leftrightarrow {latex(a*x+b)}={m**e}({latex(c*x+d)})"\
                    f"\\Leftrightarrow x={latex(tam)}$.\n\n"\
                    f"Kết hợp điều kiện ta được {t_kq}."
    noi_dung_loigiai=noi_dung_loigiai.replace("frac","dfrac")      
   
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

#[D11_C6_B4_08]-M3. Giải phương trình log_m(ax+b) + log_m(cx+d) = e
def zz8zz_L11_C6_B4_08():   
    x=sp.symbols("x")
    m=random.randint(2,6)
    e=random.randint(1,4)
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    d = random.choice([random.randint(-10, -1), random.randint(1, 10)])  

    if a==c: c=a+random.randint(1,3)  
    #Tính delta và nghiệm
    a1, b1, c1 = a*c, a*d+b*c, b*d-m**e
    delta,x_1,x_2=my_module.tinh_va_dau_delta(a1,b1,c1)[0:3]
    if delta=="<0":
        kq=0
        kq2=-b1/a1
        kq3=c1/a1
        kq4=-b1/a1+random.randint(1,5)

        pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
        kq2=pa_kotrung[1]
        kq3=pa_kotrung[2]
        kq4=pa_kotrung[3]

        pa_A= f"*Phương trình vô nghiệm"    
        pa_B= f"${{x={latex(my_module.hien_phan_so(kq2))}}}$"
        pa_C= f"${{x={latex(my_module.hien_phan_so(kq3))}}}$"
        pa_D= f"${{x={latex(my_module.hien_phan_so(kq4))}}}$"

        noi_dung_loigiai=f"Điều kiện: ${latex(a*x+b)}>0$ và ${latex(c*x+d)}>0$.\n\n"\
                    f"$\\log_{m}({latex(a*x+b)}) + \\log_{m}({latex(c*x+d)})={e}"\
                    f"\\Leftrightarrow \\log_{m}{latex((a*x+b)*(c*x+d))}={e}"\
                    f"\\Leftrightarrow {latex(expand((a*x+b)*(c*x+d)))}={m}^{e}$\n\n"\
                    f"$\\Leftrightarrow {latex(expand((a*x+b)*(c*x+d)-m**e))}=0$ (vô nghiệm).\n\n"\
                    f" Vậy phương trình đã cho vô nghiệm."
    elif delta=="=0":       
        kq=x_1
        kq2=-b1/a1
        kq3=c1/a1
        kq4=-b1/a1+random.randint(1,5)      

        pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
        kq2=pa_kotrung[1]
        kq3=pa_kotrung[2]
        kq4=pa_kotrung[3]

        if a*x_1+b<=0 or c*x_1+d<=0:
            pa_A= f"*Phương trình vô nghiệm"    
            pa_B= f"${{x={latex(my_module.hien_phan_so(kq))}}}$"
            pa_C= f"${{x={latex(my_module.hien_phan_so(kq2))}}}$"
            pa_D= f"${{x={latex(my_module.hien_phan_so(kq3))}}}$"
        else:
            pa_A= f"*${{x={latex(my_module.hien_phan_so(kq))}}}$"   
            pa_B= f"${{x={latex(my_module.hien_phan_so(kq2))}}}$"
            pa_C= f"${{x={latex(my_module.hien_phan_so(kq3))}}}$"
            pa_D= f"${{x={latex(my_module.hien_phan_so(kq4))}}}$"

            noi_dung_loigiai=f"Điều kiện: ${latex(a*x+b)}>0$ và ${latex(c*x+d)}>0$.\n\n"\
                    f"$\\log_{m}({latex(a*x+b)}) + \\log_{m}({latex(c*x+d)})={e}"\
                    f"\\Leftrightarrow \\log_{m}{latex((a*x+b)*(c*x+d))}={e}"\
                    f"\\Leftrightarrow {latex(expand((a*x+b)*(c*x+d)))}={m}^{e}$\n\n"\
                    f"$\\Leftrightarrow {latex(expand((a*x+b)*(c*x+d)-m**e))}=0\\Leftrightarrow x={latex(hien_phan_so(x_1))}$.\n\n"\
                    f" Kết hợp điều kiện ta được {pa_A.lower()}."
    else:
        y_11,y_12=a*x_1+b,c*x_1+d        
        y_21, y_22=a*x_2+b, c*x_2+d
        if my_module.check_so_nguyen(x_1):            
            x_1=latex(hien_phan_so(x_1))
            x_2=latex(hien_phan_so(x_2))
        else:
            x_1=latex(x_1)
            x_2=latex(x_2)
        if all([y_11>0,y_12>0,y_21>0,y_22>0]):
            pa_A= f"*${{x={x_1},x={x_2}}}$"   
            pa_B= f"${{x={x_1}}}$"
            pa_C= f"${{x={x_2}}}$"
            pa_D= f"${{x={latex(hien_phan_so(-b1/a1))},x={latex(hien_phan_so(c1/a1))}}}$"
        elif all([y_11>0,y_12>0]) and any([y_21<0,y_22<0]):
            pa_A= f"*${{x={x_1}}}$" 
            pa_B= f"${{x={x_1},x={x_2}}}$" 
            pa_C= f"${{x={x_2}}}$"
            pa_D= f"${{x={latex(hien_phan_so(-b1/a1))},x={latex(hien_phan_so(c1/a1))}}}$"
        elif all([y_21>0,y_22>0]) and any([y_11<0,y_12<0]):
            pa_A= f"*${{x={x_2}}}$" 
            pa_B= f"${{x={x_1},x={x_2}}}$" 
            pa_C= f"${{x={x_1}}}$"
            pa_D= f"${{x={latex(hien_phan_so(-b1/a1))},x={latex(hien_phan_so(c1/a1))}}}$"
        else:
            pa_A= f"*Phương trình vô nghiệm" 
            pa_B= f"${{x={x_1},x={x_2}}}$" 
            pa_C= f"${{x={x_1}}}$"
            pa_D= f"${{x={latex(hien_phan_so(-b1/a1))},x={latex(hien_phan_so(c1/a1))}}}$"
        noi_dung_loigiai=f"Điều kiện: ${latex(a*x+b)}>0$ và ${latex(c*x+d)}>0$.\n\n"\
                    f"$\\log_{m}({latex(a*x+b)}) + \\log_{m}({latex(c*x+d)})={e}"\
                    f"\\Leftrightarrow \\log_{m}{latex((a*x+b)*(c*x+d))}={e}"\
                    f"\\Leftrightarrow {latex(expand((a*x+b)*(c*x+d)))}={m}^{e}$\n\n"\
                    f"$\\Leftrightarrow {latex(expand((a*x+b)*(c*x+d)-m**e))}=0\\Leftrightarrow x={x_1},x={x_2}$.\n\n"\
                    f" Kết hợp điều kiện ta được {pa_A.lower()}."

    noi_dung=f"Nghiệm của phương trình $\\log_{m}({latex(a*x+b)})+\\log_{m}({latex(c*x+d)})={e}$ là"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)     

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    
    noi_dung_loigiai=noi_dung_loigiai.replace("frac","dfrac")      
   
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

#[D11_C6_B4_11]-M3. Giải phương trình m.a^x + n.b^x = p.a^x +q.b^x
def zz8zz_L11_C6_B4_11():   
    x=sp.symbols("x")
    m=random.randint(2,15)
    p=random.randint(-15,-1)

    n=random.randint(-20,-2)
    q=random.randint(1,20)

    a = random.randint(2, 9)
    b = a+random.randint(2, 6)

    t_1=(q-n)/(m-p)
    x_0=simplify(log(t_1)/log(a/b))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem =f"\\log_{{{latex(my_module.hien_phan_so(a/b))}}} \\left({latex(my_module.hien_phan_so(t_1))}\\right)"
    
    t_2=m/q
    x_0=simplify(log(t_2)/log(a/b))
    if x_0.is_Integer:
        nghiem_2 = latex((x_0))
    else:
        nghiem_2 =f"\\log_{{{latex(my_module.hien_phan_so(a/b))}}} \\left({latex(my_module.hien_phan_so(t_2))}\\right)"

    t_3=(q-n)/(m-p)
    x_0=simplify(log(t_3)/log(b/a))
    if x_0.is_Integer:
        nghiem_3 = latex((x_0))
    else:
        nghiem_3 =f"\\log_{{{latex(my_module.hien_phan_so(b/a))}}} \\left({latex(my_module.hien_phan_so(t_3))}\\right)"

    t_4=(q-n)/(m-p)+random.randint(1,5)
    x_0=simplify(log(t_4)/log(a/b))
    if x_0.is_Integer:
        nghiem_4 = latex((x_0))
    else:
        nghiem_4 =f"\\log_{{{latex(my_module.hien_phan_so(a/b))}}} \\left({latex(my_module.hien_phan_so(t_4))}\\right)"

    kq=f"{nghiem}"
    kq2=f"{nghiem_2}"
    kq3=f"{nghiem_3}"
    kq4=f"{nghiem_4}"
    
    pa_A= f"*$x={{{kq}}}$" 
    pa_B= f"$x={{{kq2}}}$" 
    pa_C= f"$x={{{kq3}}}$"
    pa_D= f"$x={{{kq4}}}$"

    noi_dung_loigiai=f"${latex(m*a**x+n*b**x)}={latex(p*a**x+q*b**x)}\\Leftrightarrow {latex(m*a**x-p*a**x)}={latex(q*b**x-n*b**x)}$ \n\n"\
        f" $\\Leftrightarrow \\left({latex(my_module.hien_phan_so(a/b))}\\right)^x={latex(my_module.hien_phan_so((q-n)/(m-p)))}$"\
        f"$\\Leftrightarrow x={kq}$.".replace("\\cdot",".")

    noi_dung=f"Nghiệm của phương trình ${latex(m*a**x+n*b**x)}={latex(p*a**x+q*b**x)}$ là".replace("\\cdot",".")


    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)     

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    
    noi_dung_loigiai=noi_dung_loigiai.replace("frac","dfrac")      
   
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

#[D11_C6_B4_12]-M3. Giải phương trình a^x + a^(x+m) +a^(x-n) = b^x + b^(x+p) + b^(x-q)
def zz8zz_L11_C6_B4_12():   
    x=sp.symbols("x")
    a = random.randint(2, 5)
    b = a+random.randint(1, 3)

    m = random.choice([random.randint(-3, -1), random.randint(1, 3)])
    n = m+random.randint(1,3)

    p = random.choice([random.randint(-3, -1), random.randint(1, 3)])
    q = p+random.randint(1,3)


    t_1=(1+b**p+b**q)/(1+a**m+a**n)
    x_0=simplify(log(t_1)/log(a/b))
    if x_0.is_Integer:
        nghiem = latex((x_0))
    else:
        nghiem =f"\\log_{{{latex(my_module.hien_phan_so(a/b))}}} \\left({latex(my_module.hien_phan_so(t_1))}\\right)"
    
    t_2=(1+abs(p)+abs(q))/(1+abs(m)+abs(n))
    x_0=simplify(log(t_2)/log(a/b))
    if x_0.is_Integer:
        nghiem_2 = latex((x_0))
    else:
        nghiem_2 =f"\\log_{{{latex(my_module.hien_phan_so(a/b))}}} \\left({latex(my_module.hien_phan_so(t_2))}\\right)"

    t_3=(b**p+b**q)/(a**m+a**n)
    x_0=simplify(log(t_3)/log(b/a))
    if x_0.is_Integer:
        nghiem_3 = latex((x_0))
    else:
        nghiem_3 =f"\\log_{{{latex(my_module.hien_phan_so(b/a))}}} \\left({latex(my_module.hien_phan_so(t_3))}\\right)"

    t_4=t_1+random.randint(1,5)
    x_0=simplify(log(t_4)/log(a/b))
    if x_0.is_Integer:
        nghiem_4 = latex((x_0))
    else:
        nghiem_4 =f"\\log_{{{latex(my_module.hien_phan_so(a/b))}}} \\left({latex(my_module.hien_phan_so(t_4))}\\right)"

    kq=f"{nghiem}"
    kq2=f"{nghiem_2}"
    kq3=f"{nghiem_3}"
    kq4=f"{nghiem_4}"
    
    pa_A= f"*$x={{{kq}}}$" 
    pa_B= f"$x={{{kq2}}}$" 
    pa_C= f"$x={{{kq3}}}$"
    pa_D= f"$x={{{kq4}}}$"

    noi_dung_loigiai=f"${latex(a**x+a**(x+m)+a**(x+n))}={latex(b**x+b**(x+p)+b**(x+q))}\\Leftrightarrow {a}^x+{latex(my_module.hien_phan_so(a**m))}.{a}^x+{latex(my_module.hien_phan_so(a**p))}.{a}^x={b}^x+{latex(my_module.hien_phan_so(b**p))}.{b}^x+{latex(my_module.hien_phan_so(b**q))}.{b}^x$ \n\n"\
        f"$\\Leftrightarrow {latex(my_module.hien_phan_so(1+a**m+a**n))}.{a}^x={latex(my_module.hien_phan_so(1+b**p+b**q))}.{b}^x \\Leftrightarrow \\left( {latex(my_module.hien_phan_so(a/b))}\\right)^x={latex(my_module.hien_phan_so(t_1))}$"\
        f"$\\Leftrightarrow x={kq}$.".replace("\\cdot",".")

    noi_dung=f"Nghiệm của phương trình ${latex(a**x+a**(x+m)+a**(x+n))}={latex(b**x+b**(x+p)+b**(x+q))}$ là".replace("\\cdot",".")


    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)     

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    
    noi_dung_loigiai=noi_dung_loigiai.replace("frac","dfrac")      
   
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

#[D11_C6_B4_13]. Phương trình dạng m^f(x)=m^g(x), đưa về bậc hai
def zz8zz_L11_C6_B4_13():
    x=sp.symbols("x")
    m=random.randint(2,9)
    f, a1, b1, c1 = tao_ham_bac_2()
    g, a2, b2, c2= tao_ham_bac_2()
    ham_trai = m**f
    ham_phai = m**g
    equation=Eq(f,g)
    tap_nghiem=solve(Eq,x)
    a, b, c=a1-a2, b1-b2, c1-c2


    

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung= f"Phương trình: ${latex(ham_trai)}={latex(ham_phai)}$ có nghiệm là"
    kq=f"{latex(my_module.hien_phan_so(kq))}"
    kq2=f"{latex(my_module.hien_phan_so(kq2))}"
    kq3=f"{latex(my_module.hien_phan_so(kq3))}"
    kq4=f"{latex(my_module.hien_phan_so(kq4))}"

    

    noi_dung_loigiai=f"${f} \\Leftrightarrow {latex(f_trai)}={latex(f_phai)}"\
    f"\\Leftrightarrow {latex(m*x+n)}={latex(t*(p*x+q))}\\Leftrightarrow x={kq}$."

    #Tạo các phương án
    pa_A= f"*${{x={kq}}}$"
    pa_B= f"${{x={kq2}}}$"
    pa_C= f"${{x={kq3}}}$"
    pa_D= f"${{x={kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.\n    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

      
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