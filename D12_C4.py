import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
from decimal import Decimal, ROUND_HALF_UP

def thay_log_2_ln(st):
    for i in range(1,8):
        st=st.replace(f"\\log{{\\left({i} \\right)}}",f"\\ln {i}")
    return st

def thay_sin_cos(st):
    st=st.replace(f"\\cos{{\\left(x \\right)}}",f"\\cos x")
    st=st.replace(f"\\sin{{\\left(x \\right)}}",f"\\sin x")
    st=st.replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x")
    st=st.replace(f"\\cot{{\\left(x \\right)}}",f"\\cot x")
    st=st.replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
    st=st.replace(f"\\cot^{{2}}{{\\left(x \\right)}}",f"\\cot^2 x")
    
    for i in range(1,8):
        st=st.replace(f"\\log{{\\left({i} \\right)}}",f"\\ln {i}")
    return st

# Hàm làm tròn half-up
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

#Thay thế dấu ngoặc sin(x) thành sinx
def thay_the_ngoac_sincos(st):
    str_thaythe=st.replace(f"\\cos{{\\left(x \\right)}}",f"\\cos x")
    str_thaythe=str_thaythe.replace(f"\\sin 1x",f"\\sin x")
    str_thaythe=str_thaythe.replace(f"\\cos 1x",f"\\cosx")
    str_thaythe=str_thaythe.replace(f"\\sin{{\\left(x \\right)}}",f"\\sin x")
    str_thaythe=str_thaythe.replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x")
    str_thaythe=str_thaythe.replace(f"\\cot{{\\left(x \\right)}}",f"\\cot x")
    str_thaythe=str_thaythe.replace(f"\\log{{\\left(x \\right)}}",f"\\ln |x|")   
    for i in range (1,15):
        str_thaythe=str_thaythe.replace(f"\\sin^{{{i}}}{{\\left(x \\right)}}",f"\\sin ^{{{i}}}x")
        str_thaythe=str_thaythe.replace(f"\\cos^{{{i}}}{{\\left(x \\right)}}",f"\\cos ^{{{i}}}x")
        str_thaythe=str_thaythe.replace(f"\\tan^{{{i}}}{{\\left(x \\right)}}",f"\\tan ^{{{i}}}x")
        str_thaythe=str_thaythe.replace(f"\\cot^{{{i}}}{{\\left(x \\right)}}",f"\\cot ^{{{i}}}x")
        str_thaythe=str_thaythe.replace(f"\\sin{{\\left({i} x \\right)}}",f"\\sin {i}x")
        str_thaythe=str_thaythe.replace(f"\\cos{{\\left({i} x \\right)}}",f"\\cos {i}x")
        str_thaythe=str_thaythe.replace(f"\\tan{{\\left({i} x \\right)}}",f"\\tan {i}x")
        str_thaythe=str_thaythe.replace(f"\\cot{{\\left({i} x \\right)}}",f"\\cot {i}x")
        str_thaythe=str_thaythe.replace(f"\\log{{\\left({i} x \\right)}}",f"\\ln {i}|x|")
        str_thaythe=str_thaythe.replace(f"\\ln x^{{{i}}}",f"\\ln^{{{i}}}|x|")
        for j in range (1,15):
            str_thaythe=str_thaythe.replace(f"\\sin^{{{i}}}{{\\left({j} x \\right)}}",f"\\sin ^{{{i}}}{j}x")
    str_thaythe=str_thaythe.replace("(1x)","x").replace("(-1x)","-x")
    str_thaythe=str_thaythe.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("+ +","+").replace("+ -","-").replace("- -","+").replace("- +","-")

    return str_thaythe
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

def tao_dau(a):
    dau="+"
    if a<0 or a==0:
        dau=""
    return dau
def xu_li_heso_1(a):
    if a==1:
        heso=""
    elif a==-1:
        heso="-" 
    else:
        heso=a 
    return heso

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
def thay_the_tich_phan(st):
    str_thaythe=st.replace("\\log","\\ln")
    str_thaythe=str_thaythe.replace(f"-1\\ln",f"\\ln").replace(f"1a",f"a").replace(f"1b",f"b").replace(f"1c",f"c")
    str_thaythe=str_thaythe.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+")
    return str_thaythe


################ Bài 1: NGUYÊN HÀM #################

#[D12_C4_B1_01]. Tìm nguyên hàm của hàm số đa thức
def zz8zz_L12_C4_B1_01():
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    k=random.randint(2,4)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k)) 
    kq= integrate(f, x) 
    kq2=diff(f, x)
    kq3=integrate(f, x) + random.randint(1,10)*x
    kq4=integrate(f, x) + random.randint(1,10)*x**2

   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    noi_dung= f"Tìm nguyên hàm $\\int {{({latex(f)}){d_x}}}$."


    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    
         
    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D12_C4_B1_02]. Tìm nguyên hàm của hàm số đa thức thỏa mãn điều kiện F(x_0)=b
def zz8zz_L12_C4_B1_02():   
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    #Tạo bậc k cho đa thức. Bậc ngẫu nhiên từ 1 đến 4
    k=random.randint(2,5)

    #Tạo hệ số a_i cho đa thức. i chạy từ 0 đến k-1
    #f=a_0 + a_1.x + a_2. x^2 + a_3. x^3
    a = [random.randint(-4,5) for i in range(k)]    
    f = sum(a[i]*x**i for i in range(k))

    #Tìm nguyên hàm của hàm f
    F= integrate(f, x)
    x_0= random.randint(-6, 8)
    C= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b= latex(my_module.hien_phan_so(F.subs(x,x_0) + C))


    kq= integrate(f, x) + C
    kq2=integrate(f, x) + C*random.choice([random.randint(-5, -1), random.randint(2, 7)])
    kq3=integrate(f, x) + random.randint(1,10)*x +C*random.choice([random.randint(-5, -1), random.randint(2, 7)])
    kq4=integrate(f, x) + random.randint(1,10)*x**2 +C

   
    kq= f"$ F(x)={latex(kq)}$"
    kq2=f"$ F(x)={latex(kq2)}$"
    kq3=f"$ F(x)={latex(kq3)}$"
    kq4=f"$ F(x)={latex(kq4)}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm một nguyên hàm $F(x)$ của hàm số $ f(x)={latex(f)}$ biết $F({x_0}) ={b}$."

    dap_an=my_module.tra_ve_dap_an(list_PA)     
    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C4_B1_03]. Tìm nguyên hàm của asinx+bcosx
def zz8zz_L12_C4_B1_03():
    #Tạo bậc ngẫu nhiên
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    f=a*sin(x)+b*cos(x)
    
    kq= integrate(f, x) 
    kq2=diff(f, x)
    kq3=integrate(f, x)+random.randint(1,3)*x
    kq4=integrate(f, x)*random.choice([random.randint(-5, -2), random.randint(2, 5)])

   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

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
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án

    noi_dung= f"Tìm nguyên hàm $  \\int {{\\left({latex(f)}\\right){d_x}}}$."
    noi_dung=noi_dung.replace("\\left(","").replace("\\right)","")

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

#[D12_C4_B1_04]. Tìm nguyên hàm của asinu
def zz8zz_L12_C4_B1_04():
   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = 1
    b = random.choice([random.randint(-10, -2), random.randint(2, 10)])

    f = b*sin(a*x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq= integrate(f, x) 
    kq2=diff(f, x)
    kq3=integrate(sin(a*x), x) 
    kq4=integrate(b*cos(a*x), x)

   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

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
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{ham}{d_x}}}$."

    dap_an=my_module.tra_ve_dap_an(list_PA) 
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
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

#[D12_C4_B1_05]. Tìm nguyên hàm của acosu
def zz8zz_L12_C4_B1_05():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = 1
    b = random.choice([random.randint(-10, -2), random.randint(2, 10)])

    f = b*cos(a*x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    kq= integrate(f, x) 
    kq2=diff(f, x)
    kq3=integrate(cos(a*x), x) 
    kq4=integrate(b*sin(a*x), x)

   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

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
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{ham}{d_x}}}$." 

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

#[D12_C4_B1_06]. Tìm nguyên hàm của hàm số đa thức và 1/x
def zz8zz_L12_C4_B1_06():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    k=random.randint(1,4)
    a = [random.randint(-4,5) for i in range(k)]    
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = sum(a[i]* x**i for i in range(k)) + b/x

    kq= integrate(f, x) 
    kq2=diff(f, x)
    kq3=integrate(sum(a[i]* x**i for i in range(k)), x) -b/x**2
    kq4=integrate(sum(a[i]* x**i for i in range(k)), x) +log(x)

   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

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
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{({latex(f)}){d_x}}}$."

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

#[D12_C4_B1_07]. Tìm nguyên hàm của m/(ax+b)
def zz8zz_L12_C4_B1_07():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])    
    m =  random.randint(1, 10)
    if m==a:
        m=a+random.randint(1,5)
    f = m/(a*x+b)

    kq= integrate(f, x) 
    kq2=diff(f, x)
    kq3=f"\\ln|{a}x+{b}|"
    if m==1:
        kq3=f"{a}\\ln|{a}x+{b}|"
    if a==1:
        kq4=integrate(f, x)+random.randint(1,5)*x        
    else: 
        kq4=integrate(f, x)*a       

   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {kq3}+C$"
    kq4=f"$ {latex(kq4)}+C$"

    kq=my_module.thay_the_ngoac_log(kq)
    kq3=my_module.thay_the_ngoac_log(kq3)
    kq4=my_module.thay_the_ngoac_log(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}".replace("+-","-")
    pa_B= f"{kq2}".replace("+-","-")
    pa_C= f"{kq3}".replace("+-","-")
    pa_D= f"{kq4}".replace("+-","-")
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{latex(f)}{d_x}}}$." 

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

#[D12_C4_B1_08]. Tìm nguyên hàm của mx+n/(ax+b)
def zz8zz_L12_C4_B1_08():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.randint(1, 5)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    m =  a*random.randint(2,4)
    n = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = (m*x+n)/(a*x+b)

    kq= integrate(f, x) 
    kq2=integrate(f, x)+random.randint(1,4)*x
    kq3=integrate(f, x)+random.randint(-5,-1)*x
    kq4=integrate(f, x)+random.randint(5,6)*x

   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

    kq=my_module.thay_the_ngoac_log(kq)
    kq2=my_module.thay_the_ngoac_log(kq2)
    kq3=my_module.thay_the_ngoac_log(kq3)
    kq4=my_module.thay_the_ngoac_log(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{latex(f)}{d_x}}}$." 
    
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

#[D12_C4_B1_09]. Tìm nguyên hàm của (mx^2+nx+p)/(ax+b)
def zz8zz_L12_C4_B1_09():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.randint(1, 3)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    m =  a*random.randint(2,4)
    n = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    p = random.randint(-6, 6)

    f = (m*x**2+n*x+p)/(a*x+b)
    g = (m*x**2+n*x+p)/(a*x)
    h = (m*x**2)/(a*x+b)

    kq= integrate(f, x) 
    kq2=integrate(f+1, x)
    kq3=integrate(h, x)
    kq4=integrate(g, x)
   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

    kq=my_module.thay_the_ngoac_log(kq)
    kq2=my_module.thay_the_ngoac_log(kq2)
    kq3=my_module.thay_the_ngoac_log(kq3)
    kq4=my_module.thay_the_ngoac_log(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{latex(f)}{d_x}}}$."
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

#[D12_C4_B1_10]. Tìm nguyên hàm của e^(ax+b)
def zz8zz_L12_C4_B1_10():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b = random.randint(-10, 10)
    m = random.choice([random.randint(-6, -2), random.randint(2, 6)])    

    f = m*exp(a*x+b)

    kq= integrate(f, x) 
    kq2=m*exp(a*x+b)
    kq3=m*a*exp(a*x+b)
    kq4=(m*a+random.randint(1,5))*exp(a*x+b)
   
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

    kq=my_module.thay_the_ngoac_log(kq)
    kq2=my_module.thay_the_ngoac_log(kq2)
    kq3=my_module.thay_the_ngoac_log(kq3)
    kq4=my_module.thay_the_ngoac_log(kq4)

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    if m>0:
        noi_dung= f"Tìm nguyên hàm $  \\int {{{latex(f)}{d_x}}}$."
        noi_dung_loigiai=f"$  \\int {{{latex(f)}{d_x}}}= $ {kq}" 
    if m<0:
        noi_dung= f"Tìm nguyên hàm $  \\int {{\\left({latex(f)}\\right){d_x}}}$."
        noi_dung_loigiai=f"$  \\int {{\\left({latex(f)}\\right){d_x}}}= $ {kq}" 
    
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    
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

#[D12_C4_B1_11]-M1. Tìm nguyên hàm của ax+b
def zz8zz_L12_C4_B1_11():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-7, 7) if i!=0])
    b = random.choice([i for i in range(-7, 7) if i!=0])
    noi_dung=(
    f"Tìm nguyên hàm $\\int \\left({{{latex(a*x+b)}}}\\right) dx$."
    )    

    kq=f"${latex(a*x**2/2+b*x)}+C$"
    kq_false=[f"${a}+C$",
    f"${latex(a*x**2+b*x)}+C$",
    f"${latex(a*x**2+b)}+C$",
    f"${latex(2*a*x)}+C$",]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {{{latex(a*x+b)}}} dx={latex(a*x**2/2+b*x)}+C$."
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

#[D12_C4_B1_12]-M1. Tìm nguyên hàm của k
def zz8zz_L12_C4_B1_12():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-7, 7) if i!=0])
    
    noi_dung=(
    f"Tìm nguyên hàm $\\int {a} dx$."
    )    

    kq=f"${latex(a*x)}+C$"
    kq_false=[f"${{C}}$",
    f"${latex(a*x**2)}+C$",
    f"${latex(a*x/2)}+C$",
    f"${latex(2*a*x)}+C$",]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {a} dx={latex(a*x)}+C$."
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

#[D12_C4_B1_13]-M2. Tìm nguyên hàm của ax^2+bx+c
def zz8zz_L12_C4_B1_13():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-7, 7) if i!=0])
    b = random.choice([i for i in range(-7, 7) if i!=0])
    c = random.randint(-5,5)
    noi_dung=(
    f"Tìm nguyên hàm $\\int \\left({{{latex(a*x**2+b*x+c)}}}\\right) dx$."
    )    

    kq=f"${latex(a*x**3/3+b*x**2/2+c*x)}+C$"
    kq_false=[
    f"${latex(a*x**3+b*x**2+c*x)}+C$",
    f"${latex(a*x**3/3+b*x**2+c*x)}+C$",
    f"${latex(a*x**3+b*x**2/2+c)}+C$",
    f"${latex(a*x**3+b*x**2+c)}+C$",
  ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int \\left({{{latex(a*x**2+b*x+c)}}}\\right) dx={latex(a*x**3/3+b*x**2/2+c*x)}+C$."
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_14]-M2. Tìm nguyên hàm của (ax+b)^2
def zz8zz_L12_C4_B1_14():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 4) if i!=0])
    b = random.choice([i for i in range(-5, 4) if i!=0])
    noi_dung=(
    f"Tìm nguyên hàm $\\int {{{latex((a*x+b)**2)}}} dx$."
    )
    
    f=(a*x+b)**2
    kq=f"${latex(integrate(f,x))}+C$"
    kq_false=[
    f"${latex(a*x**3+a*b*x**2+b**2*x)}+C$",
    f"${latex(a*x**3/3+a*b*x**2/2+b**2*x)}+C$",
    f"${latex(a*x**3/3+a*b*x**2/2+b**2)}+C$",
    f"${latex(3*a*x**2+2*a*b*x+b**2)}+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {{{latex((a*x+b)**2)}}} dx$"
    f"$=\\int \\left({{{latex(expand((a*x+b)**2))}}}\\right) dx$"
    f"$={latex(integrate(f,x))}+C$."
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_15]-M2. Tìm nguyên hàm của a+b/x^2
def zz8zz_L12_C4_B1_15():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 4) if i!=0])
    b = random.choice([i for i in range(-5, 4) if i!=0])
    noi_dung=(
    f"Tìm nguyên hàm $\\int \\left({{{latex(a+b/x**2)}}}\\right) dx$."
    )
    
    f=a+b/x**2
    kq=f"${latex(integrate(f,x))}+C$"
    kq_false=[
    f"${latex(a*x+b/x)}+C$",
    f"${latex(a*x**2/2+b)}+C$",
    f"${latex(a*x**2-b/x)}+C$",
    f"${latex(a*x**2/2+b/x)}+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int \\left({{{latex(a+b/x**2)}}}\\right) dx$"
    f"$={latex(integrate(f,x))}+C$."
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

#[D12_C4_B1_16]-M2. Tìm nguyên hàm của ax+b/x^2+c
def zz8zz_L12_C4_B1_16():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 4) if i!=0])
    b = random.choice([i for i in range(-5, 4) if i!=0])
    c = random.choice([i for i in range(-5, 4) if i!=0])
    noi_dung=(
    f"Tìm nguyên hàm $\\int \\left({{{latex(a*x+b/x**2+c)}}}\\right) dx$."
    )
    
    f=a*x+b/x**2+c
    kq=f"${latex(integrate(f,x))}+C$"
    kq_false=[
    f"${latex(a-b/x)}+C$",
    f"${latex(a*x**2/2+b/x+c)}+C$",
    f"${latex(a*x**2/2-b/x+c)}+C$",
    f"${latex(a*x**2-b/x+c*x)}+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int \\left({{{latex(a*x+b/x**2+c)}}}\\right) dx$"
    f"$={latex(integrate(f,x))}+C$."
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_17]-SA-M2. Tìm nguyên hàm đa thức thỏa mãn F(x_0)=b
def zz8zz_L12_C4_B1_17():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    
    chon=random.randint(1,3)
    if chon==1:
        a = random.choice([i for i in range(-4, 4) if i!=0])
        b = random.choice([i for i in range(-6, 6) if i!=0])        

        F = a*x**2+b*x
    
    if chon==2:
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(-4, 4) if i!=0])
        c = random.choice([i for i in range(-5, 5) if i!=0])        
        F = a*x**3+b*x**2+c*x

    if chon==3:
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(-4, 4) if i!=0])
        c = random.choice([i for i in range(-5, 5) if i!=0])        
        F = a*x**4+b*x**2+c*x  

    
    x_0= random.randint(-6, 6)
    
    b= random.randint(-10, 10)
    x_1=random.randint(-5, 5)
    if x_1==x_0: x_1=x_1+1

    f=diff(F,x)
    C=b-F.subs(x,x_0)
    G=F+C

    dap_an=G.subs(x,x_1)

    noi_dung = (
    f"Tìm một nguyên hàm $F(x)$ của hàm số $ f(x)={latex(f)}$ biết $F({x_0}) ={b}$. Tính $F({x_1})$."
    )
    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {F.subs(x,x_0)}+C={b}\\Rightarrow C={C}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={dap_an}$."    
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_18]-SA-M2. Tìm nguyên hàm của a+b/x^2 thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_18():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    
    chon=random.randint(1,2)
    
    a = random.choice([i for i in range(-4, 4) if i!=0])
    b = random.choice([i for i in range(-5, 5) if i!=0])        

    F = a*x+b/x
   
    x_0= random.choice([i for i in range(-5, 5) if i!=0])
    
    b= random.randint(-8, 8)
    x_1=random.randint(-5, 5)

    while x_1==x_0 or x_1==0:
        x_1=random.randint(-5, 5)       
   

    f=diff(F,x)
    C=b-F.subs(x,x_0)
    G=F+C

    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung = (
    f"Tìm một nguyên hàm $F(x)$ của hàm số $ f(x)={latex(f)}$ biết $F({x_0}) ={b}$. Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {phan_so(F.subs(x,x_0))}+C={b}\\Rightarrow C={phan_so(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={phan_so(G.subs(x,x_1))}={dap_an}$."    
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_19]-SA-M2. Tìm nguyên hàm của ax+b/x^2 thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_19():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    
    chon=random.randint(1,2)
    
    a = random.choice([i for i in range(-4, 4) if i!=0])
    b = random.choice([i for i in range(-6, 6) if i!=0])        

    F = a*x**2+b/x
   
    x_0= random.choice([i for i in range(-5, 5) if i!=0])
    
    b= random.randint(-8, 8)
    x_1=random.randint(-5, 5)

    while x_1==x_0 or x_1==0:
        x_1=random.randint(-5, 5)       
   

    f=diff(F,x)
    C=b-F.subs(x,x_0)
    G=F+C

    dap_an=f"{round_half_up(G.subs(x,x_1)):.1f}".replace(".",",")

    noi_dung = (
    f"Tìm một nguyên hàm $F(x)$ của hàm số $ f(x)={latex(f)}$ biết $F({x_0}) ={b}$. Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {phan_so(F.subs(x,x_0))}+C={b}\\Rightarrow C={phan_so(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={phan_so(G.subs(x,x_1))}={dap_an}$."    
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_20]-SA-M2. Tìm nguyên hàm của ax+b+c/x^2 thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_20():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"   

    
    a = random.choice([i for i in range(-4, 4) if i!=0])
    b = random.choice([i for i in range(-4, 4) if i!=0])
    c = random.choice([i for i in range(-4, 4) if i!=0])        

    F = a*x**2+b*x+c/x   
    x_0= random.choice([i for i in range(-3, 3) if i!=0])   
    
    x_1=random.randint(-5, 5)
    while x_1==x_0 or x_1==0:
        x_1=random.randint(-4, 4)       
   
    b= random.randint(-6, 6)
    f=diff(F,x)
    C=b-F.subs(x,x_0)
    G=F+C

    dap_an=f"{round_half_up(G.subs(x,x_1)):.1f}".replace(".",",")

    noi_dung = (
    f"Tìm một nguyên hàm $F(x)$ của hàm số $ f(x)={latex(f)}$ biết $F({x_0}) ={b}$. Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {phan_so(F.subs(x,x_0))}+C={b}\\Rightarrow C={phan_so(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={phan_so(G.subs(x,x_1))}={dap_an}$."    
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_21]-M2. Tìm nguyên hàm của m/cos^2x
def zz8zz_L12_C4_B1_21():
    m= random.choice([random.randint(-10,-2), random.randint(2,10)])
    noi_dung=(
    f"Tìm nguyên hàm $\\int \\dfrac{{{m}}}{{\\cos^2 x}} dx$."
    )
    
    kq=f"${m}\\tan x+C$"
    kq_false=[
    f"${m}\\cot x+C$",
    f"${m}\\cos^2 x+C$",
    f"${m}\\sin^2 x+C$",
    f"${m}\\tan^2 x+C$",
     f"${m}\\cot^2 x+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int \\dfrac{{{m}}}{{\\cos^2 x}}dx={m}\\tan x+C$."
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

#[D12_C4_B1_22]-M2. Tìm nguyên hàm của m/sin^2x
def zz8zz_L12_C4_B1_22():
    m= random.choice([random.randint(-10,-2), random.randint(2,10)])
    noi_dung=(
    f"Tìm nguyên hàm $\\int \\dfrac{{{m}}}{{\\sin^2 x}} dx$."
    )
    
    kq=f"${-m}\\cot x+C$"
    kq_false=[
    f"${m}\\cot x+C$",
    f"${m}\\cos^2 x+C$",
    f"${m}\\sin^2 x+C$",
    f"${m}\\tan^2 x+C$",
    f"${m}\\cot^2 x+C$",
    f"$\\dfrac{{{m}}}{{\\cot^2 x}}+C$",
    f"$\\dfrac{{{m}}}{{\\tan^2 x}}+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int \\dfrac{{{m}}}{{\\sin^2 x}} dx={-m}\\cot x+C$."
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

#[D12_C4_B1_23]-M2. Tìm nguyên hàm của m(1+tan^2x)
def zz8zz_L12_C4_B1_23():
    m= random.choice([random.randint(-10,-2), random.randint(2,10)])
    noi_dung=(
    f"Tìm nguyên hàm $\\int {m}\\left(1+\\tan^2 x\\right) dx$."
    )
    
    kq=f"${m}\\tan x+C$"
    kq_false=[
    f"${m}\\cot x+C$",
    f"${m}\\cos^2 x+C$",
    f"${m}\\sin^2 x+C$",
    f"${m}\\tan^2 x+C$",
     f"${m}\\cot^2 x+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {m}\\left(1+\\tan^2 x\\right)dx={m}\\tan x+C$."
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

#[D12_C4_B1_24]-M2. Tìm nguyên hàm của m(1+cot^2x)
def zz8zz_L12_C4_B1_24():
    m= random.choice([random.randint(-10,-2),random.randint(2,10)])
    noi_dung=(
    f"Tìm nguyên hàm $\\int {m}\\left(1+\\cot^2 x\\right)dx$."
    )
    
    kq=f"${-m}\\cot x+C$"
    kq_false=[
    f"${m}\\cot x+C$",
    f"${-m}\\cos^2 x+C$",
    f"${m}\\sin^2 x+C$",
    f"${m}\\tan^2 x+C$",
    f"${m}\\cot^2 x+C$",
    f"$\\dfrac{{{-m}}}{{\\cot^2 x}}+C$",
    f"$\\dfrac{{{m}}}{{\\tan^2 x}}+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {m}\\left(1+\\cot^2 x\\right) dx={-m}\\cot x+C$."
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

#[D12_C4_B1_25]-M2. Tìm nguyên hàm của m/cos^2x + n/sin^2x
def zz8zz_L12_C4_B1_25():
    m= random.choice([random.randint(-10,-2), random.randint(2,10)])
    n= random.choice([random.randint(-10,-2), random.randint(2,10)])
    noi_dung=(
    f"Tìm nguyên hàm $\\int \\left(\\dfrac{{{m}}}{{\\cos^2 x}} +\\dfrac{{{n}}}{{\\sin^2 x}}\\right) dx$."
    )
    
    kq=f"${m}\\tan x+{-n}\\cot x+C$"
    kq_false=[
    f"${m}\\tan x+{n}\\cot x+C$",
    f"${m}\\cos^2 x+{n}\\sin^2x +C$",
    f"${m}\\cos x+{n}\\sin x$",
    f"${m}\\tan^2 x+C$",
     f"${n}\\cot^2 x+C$"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int \\left(\\dfrac{{{m}}}{{\\cos^2 x}} +\\dfrac{{{n}}}{{\\sin^2 x}}\\right) dx={m}\\tan x+{-n}\\cot x+C$."
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")

    pa_A= f"*{kq}".replace("+-","-")
    pa_B= f"{kq2}".replace("+-","-")
    pa_C= f"{kq3}".replace("+-","-")
    pa_D= f"{kq4}".replace("+-","-")
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

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_26]-TF-M2. Xét đúng-sai: nguyên hàm của ax,ax^2+bx+c, a+b/x^2, (ax+b)(cx+d)
def zz8zz_L12_C4_B1_26():
    x=sp.symbols("x")

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"

    a= random.choice([i for i in range(-10, 10) if i!=0])
    F=a*x
    
    kq1_T=f"* Hàm số $F(x)={latex(a*x)}$ là một nguyên hàm của hàm số $f(x)={a}$" 
    kq1_F=f"Hàm số $F(x)={latex(a*x**2)}$ là một nguyên hàm của hàm số $f(x)={a}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Hàm số $F(x)={latex(a*x)}+C$ là một nguyên hàm của hàm số $f(x)={a}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.choice([i for i in range(-8, 8) if i!=0])
    b= random.choice([i for i in range(-8, 8) if i!=0])
    c=random.randint(-5,5)


    kq2_T=f"* $\\int ({{{latex(a*x**2+b*x+c)}}}) dx={latex(a*x**3/3+b*x**2/2+c*x)}+C$"
    kq2_F=f"$\\int ({{{latex(a*x**2+b*x+c)}}}) dx={latex(2*a*x+b)}+C$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$\\int ({{{latex(a*x**2+b*x+c)}}}) dx={latex(a*x**3/3+b*x**2/2+c*x)}+C$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.choice([i for i in range(-8, 8) if i!=0])
    b= random.choice([i for i in range(-8, 8) if i!=0])

    c= random.choice([i for i in range(-8, 8) if i!=0])
    d= random.choice([i for i in range(-8, 8) if i!=0])
    while any([a==c,b==d]):
        c= random.choice([i for i in range(-8, 8) if i!=0])
        d= random.choice([i for i in range(-8, 8) if i!=0])

    f=(a*x+b)*(c*x+d)
    F=integrate(f,x)


    kq3_T=f"* $\\int \\left[{latex(f)}\\right]dx={latex(F)}+C$" 
    kq3_F=f"$\\int \\left[{latex(f)}\\right]dx={latex(F+random.randint(1,3)*x)}+C$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$\\int \\left[{latex(f)}\\right]dx=\\int \\left({latex(expand(f))}\\right)={latex(F)}+C$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.choice([i for i in range(-8, 8) if i!=0])
    b= random.choice([i for i in range(-8, 8) if i!=0])

    kq4_T=f"* $\\int \\left({{{latex(a+b/x**2)}}}\\right)dx={latex(a*x-b/x)}+C$"
    kq4_F=f"$\\int \\left({{{latex(a+b/x**2)}}}\\right)dx={latex(a*x+b/x)}+C$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$\\int \\left({{{latex(a+b/x**2)}}}\\right)dx={latex(a*x-b/x)}+C$."
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

#[D12_C4_B1_27]-M1. Nguyên hàm của a^x
def zz8zz_L12_C4_B1_27():
    a=random.choice([random.randint(2,15),pi])
    noi_dung=(
    f"Tìm nguyên hàm $\\int {{{latex(a)}^x}}dx$."
    )
    

    kq=f"$\\dfrac{{{latex(a)}^x}}{{\\ln {latex(a)}}}$"
    kq_false=[
    f"$\\dfrac{{{latex(a)}^x}}{{{latex(a)}}}+C$",
    f"${latex(a)}^x\\ln {latex(a)}+C$",
    f"$x^{{{latex(a)}}}\\ln {latex(a)}+C$",
    f"$\\dfrac{{x^{{{latex(a)}}} }}{{\\ln {latex(a)}}}+C$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {{{latex(a)}^x}}dx=\\dfrac{{{latex(a)}^x}}{{\\ln {latex(a)}}}$."
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

#[D12_C4_B1_28]-M2. Nguyên hàm của m.e^x
def zz8zz_L12_C4_B1_28():
    a=random.choice([random.randint(2,15), random.randint(1,9)/random.randint(10,20)])
    noi_dung=(
    f"Tìm nguyên hàm $\\int {{{phan_so(a)}.e^x}}dx$."
    )
    

    kq=f"${phan_so(a)}e^x+C$"
    kq_false=[
    f"${phan_so(a)}\\ln x+C$",
    f"$e^x+C$",
    f"$e^{{{phan_so(a)}x}}+C$",
    f"${phan_so(1/a)}e^x+C$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {{{phan_so(a)}.e^x}}dx={phan_so(a)}e^x+C$."
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

#[D12_C4_B1_29]-M2. Nguyên hàm của e^(ax+b)
def zz8zz_L12_C4_B1_29():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-8, 8) if i!=0 and i!=1])
    b = random.randint(-8,8)
    noi_dung=(
    f"Tìm nguyên hàm $\\int e^{{{latex(a*x+b)}}}dx$."
    )
    

    kq=f"${phan_so(1/a)}e^{{{latex(a*x+b)}}}+C$"
    kq_false=[
    f"${a}e^{{{latex(a*x+b)}}}+C$",
    f"$e^{{{latex(a*x+b)}}}+C$",
    f"$({latex(a*x+b)}).e^x+C$",
  ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int e^{{{latex(a*x+b)}}}dx={phan_so(1/a)}e^{{{latex(a*x+b)}}}+C$."
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

#[D12_C4_B1_30]-M2. Nguyên hàm của e^(ax)+mx+n
def zz8zz_L12_C4_B1_30():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-8, 8) if i!=0 and i!=1 and i !=-1])
    m = random.choice([i for i in range(-5, 5) if i!=0 and i!=1 and i !=-1])
    n = random.choice([i for i in range(-7, 7) if i!=0])
    
    noi_dung=(
    f"Tìm nguyên hàm $\\int (e^{{{latex(a*x)}}}+{latex(m*x+n)})dx$."
    )
    

    kq=f"${phan_so(1/a)}e^{{{latex(a*x)}}}+{latex(m*x**2/2+n*x)}+C$"
    kq_false=[
    f"$e^{{{latex(a*x)}}}+{latex(m*x**2/2+n*x)}+C$",
    f"${phan_so(1/a)}e^{{{latex(a*x)}}}+{latex(m*x**2+n*x)}+C$",
    f"${a}e^{{{latex(a*x)}}}+{m}+C$",
  ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int (e^{{{latex(a*x)}}}+{latex(m*x+n)})dx={phan_so(1/a)}e^{{{latex(a*x)}}}+{latex(m*x**2/2+n*x)}+C$"
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")

    pa_A= f"*{kq}".replace("+-","-")
    pa_B= f"{kq2}".replace("+-","-")
    pa_C= f"{kq3}".replace("+-","-")
    pa_D= f"{kq4}".replace("+-","-")
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n".replace("+-","-")

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_31]-M2. Nguyên hàm của m.e^x + n.e^(-x)
def zz8zz_L12_C4_B1_31():
    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])

    p = random.choice([i for i in range(-4, 4) if i!=0])
    e,x=sp.symbols("e x")
    f=m*e**x+n*e**(-x)

    noi_dung=(
    f"Tìm nguyên hàm của hàm số $f(x)={latex(f)}$."
    )
    

    kq=f"${latex(m*e**x-n*e**(-x))}+C$"
    kq_false=[
    f"${latex(m*e**x+n*e**(-x))}+C$",
    f"${latex(m*e**x-n*e**(-x)+random.randint(1,2))}+C$",
    f"${latex(m*e**x+n)}+C$",
    f"${latex(e**x+n*e**(-x))}+C$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int ({latex(f)})dx={latex(m*e**x-n*e**(-x))}+C$."
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_32]-M2. Nguyên hàm của m.e^x + n.e^(-x) +p
def zz8zz_L12_C4_B1_32():
    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])

    p = random.choice([i for i in range(-4, 4) if i!=0])
    e,x=sp.symbols("e x")
    f=m*e**x+n*e**(-x)+p

    noi_dung=(
    f"Tìm nguyên hàm của hàm số $f(x)={latex(f)}$."
    )
    

    kq=f"${latex(m*e**x-n*e**(-x)+p*x)}+C$"
    kq_false=[
    f"${latex(m*e**x+n*e**(-x)+p*x)}+C$",
    f"${latex(m*e**x-n*e**(-x)+p)}+C$",
    f"${latex(m*e**x+p*x)}+C$",
    f"${latex(e**x-n*e**(-x)+p*x**2)}+C$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int ({latex(f)})dx={latex(m*e**x-n*e**(-x)+p*x)}+C$."
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_33]-M2. Nguyên hàm của m.e^x + n thỏa mãn F(x_0)=y_0
def zz8zz_L12_C4_B1_33():
    d_x=f"\\mathrm{{\\,d}}x"
    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])   
    x,e=sp.symbols("x,e")
    F=m*exp(x)+n*x

    x_0= random.choice([0, random.randint(-3, 3)])   
    b= random.randint(-6, 6)  

    f=diff(F,x)
    C=b-F.subs(x,x_0)
    G=F+C

    noi_dung=(
    f"Tìm một nguyên hàm $F(x)$ của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    )    

    kq=f"${latex(G)}$"
    kq_false=[
    f"$F(x)={latex(m*e**x+n*x**2+C)}$",
    f"$F(x)={latex(m*e**(-x)+n*x+C)}$",
    f"$F(x)={latex(m*e**x-n*x+C)}$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$."     
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_34]-M3. Nguyên hàm của m.e^x + n.e^(-x) thỏa mãn F(x_0)=y_0
def zz8zz_L12_C4_B1_34():
    d_x=f"\\mathrm{{\\,d}}x"
    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])   
    x,e=sp.symbols("x,e")
    F=m*exp(x)+n*exp(-x)

    x_0= random.randint(-3, 3)
    b= random.randint(-5, 5)  

    f=diff(F,x)
    C=b-F.subs(x,x_0)
    G=F+C

    noi_dung=(
    f"Tìm một nguyên hàm $F(x)$ của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    )    

    kq=f"${latex(G)}$"
    kq_false=[
    f"$F(x)={latex(m*e**x+n*e**(-x)+C)}$",
    f"$F(x)={latex(m*e**(-x)+n*x+C)}$",
    f"$F(x)={latex(m*e**x-n+C)}$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$."     
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
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

#[D12_C4_B1_35]-SA-M3. F(x) là một nguyên hàm của m.e^x + n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_35():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")
    m = random.choice([i for i in range(-4, 4) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])   
    
    F=m*exp(x)+n*x
    x_0= random.choice([random.randint(-3, 3)])    
    b= random.randint(-6, 6)
    C=b-F.subs(x,x_0)
    G=F+C
    f=diff(F,x)  
    x_1=random.choice([i for i in range(-3,3) if i!=x_0])
    while G.subs(x,x_1)<-9.9 or G.subs(x,x_1)>9999:
        m = random.choice([i for i in range(-4, 4) if i!=0])
        n = random.choice([i for i in range(-3, 3) if i!=0])   
        
        F=m*exp(x)+n*x
        x_0= random.choice([random.randint(-3, 3)])    
        b= random.randint(-6, 6)
        C=b-F.subs(x,x_0)
        G=F+C
        x_1=random.choice([i for i in range(-3,3) if i!=x_0])
   

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )    

    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Do đó $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={latex(G.subs(x,x_1))}={dap_an}$."  
    )

        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_36]-SA-M3. F(x) là một nguyên hàm của m.e^x + ne^(-x)  thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_36():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        m = random.choice([i for i in range(-4, 4) if i!=0])
        n = random.choice([i for i in range(-3, 3) if i!=0])   
        
        F=m*exp(x)+n*exp(-x)
        x_0= random.choice([random.randint(-3, 3)])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        x_1=random.choice([i for i in range(-3,3) if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")
    noi_dung=(
    f"Tìm một nguyên hàm $F(x)$ của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )    

    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")   

        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_37]-SA-M3. F(x) là một nguyên hàm của m.e^x + ne^(-x)+p thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_37():
    d_x=f"\\mathrm{{\\,d}}x"
    e,x=sp.symbols("e x")
    while True:
        m = random.choice([i for i in range(-4, 4) if i!=0])
        n = random.choice([i for i in range(-3, 3) if i!=0])
        p = random.choice([i for i in range(-4, 4) if i!=0])  
        
        F=m*exp(x)+n*exp(-x)+p*x
        x_0= random.choice([random.randint(-3, 3)])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        x_1=random.choice([i for i in range(-3,3) if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break

    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")
    noi_dung=(
    f"Tìm một nguyên hàm $F(x)$ của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )    

    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")   

        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an


#[D12_C4_B1_38]-SA-M3. F(x) là một nguyên hàm của m.a^x+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_38():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-4, -1) if i!=0])
        n = random.choice([i for i in range(-3, 3) if i!=0])   
        
        F=m*a**(x)+n*x
        x_0= random.choice([random.randint(-3, 3)])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        x_1=random.choice([i for i in range(-4,4) if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")
    noi_dung=(
    f"Tìm một nguyên hàm $F(x)$ của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_log_2_ln(noi_dung)
    noi_dung_loigiai=thay_log_2_ln(noi_dung_loigiai)

    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")   

        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_39]-SA-M3. F(x) là một nguyên hàm của m.a^x+n.e^x thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_39():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-4, -1) if i!=0])
        n = random.choice([i for i in range(-3, 3) if i!=0])   
        
        F=m*a**(x)+n*exp(x)
        x_0= random.choice([random.randint(-3, 3)])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        x_1=random.choice([i for i in range(-4,4) if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_log_2_ln(noi_dung)
    noi_dung_loigiai=thay_log_2_ln(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_40]-SA-M3. F(x) là một nguyên hàm của m.sin(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_40():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-4, 4) if i!=0])
        n = random.choice([i for i in range(-5, 5) if i!=0])   
        
        F=m*cos(x)+n*x
        x_0= random.choice([0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_41]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_41():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-5, 5) if i!=0])
        n = random.choice([i for i in range(-5, 5) if i!=0])   
        
        F=m*sin(x)+n*x
        x_0= random.choice([0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_42]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n hoặc m.sin(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_42():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-5, 5) if i!=0])
        n = random.choice([i for i in range(-5, 5) if i!=0])
        chon=random.randint(1,2)
        if chon==1:
            F=m*sin(x)+n*x
        
        if chon==2:
            F=m*cos(x)+n*x     
        
        
        x_0= random.choice([0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_43]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n.sin(x) thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_43():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-5, 5) if i!=0])
        n = random.choice([i for i in range(-5, 5) if i!=0])      
        
        F=m*cos(x)+n*sin(x)
        
        
        x_0= random.choice([0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_44]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n.sin(x)+p thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_44():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-5, 5) if i!=0])
        n = random.choice([i for i in range(-5, 5) if i!=0])   
        p = random.choice([i for i in range(-6, 6) if i!=0])   
        
        F=m*cos(x)+n*sin(x)+p*x        
        
        x_0= random.choice([0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[0,pi/3, pi/6, pi/4, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_45]-SA-M3. F(x) là một nguyên hàm của mtan^2(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_45():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-5, 5) if i!=0])
        n = random.choice([i for i in range(-5, 5) if i!=0]) 
           
        
        F=m*tan(x)+n*x        
        
        x_0= random.choice([0,pi/3,  pi/6, pi/4, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[0,pi/3, pi/6, pi/4, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_46]-SA-M3. F(x) là một nguyên hàm của mcot^2(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_46():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-5, 5) if i!=0])
        n = random.choice([i for i in range(-5, 5) if i!=0]) 
           
        
        F=m*cot(x)+n*x        
        
        x_0= random.choice([pi/2, pi/6, pi/4, 2*pi/3, 3*pi/4, 5*pi/6, 3*pi/2])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[pi/2, pi/6, pi/4, 2*pi/3, 3*pi/4, 5*pi/6, 3*pi/2]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_47]-SA-M3. F(x) là một nguyên hàm của mtan^2+ncot^2(x) thỏa mãn F(x_0)=y_0. Tính F(x_1)
def zz8zz_L12_C4_B1_47():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")    
    while True:
        a=random.randint(2,7)
        m = random.choice([i for i in range(-7, 7) if i!=0])
        n = random.choice([i for i in range(-7, 7) if i!=0])
        p=random.randint(-5,5)
           
        
        F=m*tan(x)+n*cot(x)+p*x
        
        x_0= random.choice([pi/3, pi/6, pi/4, 2*pi/3, 3*pi/4, 5*pi/6, 7*pi/4, 5*pi/4, 5*pi/3])    
        b= random.randint(-5, 5)
        C=b-F.subs(x,x_0)
        G=F+C
        list_x=[pi/3, pi/6, pi/4, 2*pi/3, 3*pi/4, 5*pi/6, 7*pi/4, 5*pi/4, 5*pi/3]
        x_1=random.choice([i for i in list_x if i!=x_0])
        if G.subs(x,x_1)>-9.9 and G.subs(x,x_1)<9999:
            break
    f=diff(F,x)
    
    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$."
    f" Tính $F({latex(x_1)})$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_48]-TF-M3. Xét Đ-S: nguyên hàm của asinx, acosx+b, atan^2x, Tính F(x_0)
def zz8zz_L12_C4_B1_48():
    x=sp.symbols("x")

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"

    a=random.randint(2,10)
    
    kq1_T=f"* $\\int {latex(a*sin(x))}={latex(-a*cos(x))}+C$" 
    kq1_F=f"$\\int {latex(a*sin(x))}={latex(a*cos(x))}+C$"
    kq1=random.choice([kq1_T, kq1_F])
    kq1=thay_sin_cos(kq1)
    HDG=f"$\\int {latex(a*sin(x))}={latex(-a*cos(x))}+C$."
    HDG=thay_sin_cos(HDG)
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* "
    kq2_F=f" "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f""
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* " 
    kq3_F=f" "
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f""
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* "
    kq4_F=f" " 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f""
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




#------------------------------------------------------------->
#BÀI 2- NGUYÊN HÀM ĐỔI BIẾN
#[D12_C4_B2_01]. Nguyên hàm đổi biến chứa căn(ax+b)
def zz8zz_L12_C4_B2_01():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if a<0 and b<0:
        b=random.randint(2,10)

    f = sqrt(a*x+b)   
   
    kq= f"$ {latex(my_module.hien_phan_so(2/a))}  \\int u^2du$"
    kq2=f"$ {latex(my_module.hien_phan_so(1/a))}  \\int u^2du$"
    kq3=f"$  \\int udu$"
    kq4=f"$ {latex(my_module.hien_phan_so(2/a))}  \\int udu$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho nguyên hàm $  \\int {{{latex(f)}{d_x}}}$. Sử dụng phép đổi biến $u={latex(sqrt(a*x+b))}$ ta được nguyên hàm nào?"
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



#[D12_C4_B2_02]. Nguyên hàm đổi biến chứa căn(ax^2+b)
def zz8zz_L12_C4_B2_02():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    b = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    if a<0 and b<0:
        b=random.randint(2,10)
    f = sqrt(a*x**2+b)*x
    f_1 = sqrt(a*x**2+b)
    t=latex(my_module.hien_phan_so(1/a))
    kq= f"$ {t}  \\int u^2du$"
    kq2=f"$ {a} \\int u^2du$"
    kq3=f"$  \\int u^2du$"
    kq4=f"$  \\int\\sqrt u du$"
   
    kq= f"$ {t}  \\int u^2du$"
    kq2=f"$ {a}  \\int u^2du$"
    kq3=f"$  \\int u^2du$"
    kq4=f"$  \\int\\sqrt u du$"


    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho nguyên hàm $  \\int {{{latex(f)}{d_x}}}$. Sử dụng phép đổi biến $u={latex(f_1)}$ ta được nguyên hàm nào?"
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
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

#[D12_C4_B2_03]. Nguyên hàm đổi biến sinx/căn(acosx+b){d_x}
def zz8zz_L12_C4_B2_03():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.randint(1, 10)
    f = sin(x)/sqrt(a*cos(x)+b)  
    ham=my_module.thay_the_ngoac_sincos(latex(f)) 

   
    kq= integrate(f, x) 
    kq2=sin(x)*sqrt(a*cos(x)+b) 
    kq3=cos(x)*sqrt(a*cos(x)+b)
    kq4=sqrt(a*sin(x)+b)

    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"
    kq3=kq3.replace("\\log","\\ln")

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
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{ham}{d_x}}}$."
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

#[D12_C4_B2_04]. Nguyên hàm đổi biến (acosx+b)sinx
def zz8zz_L12_C4_B2_04():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.randint(1, 10) 
    f = sin(x)*(a*cos(x)+b)
    ham=my_module.thay_the_ngoac_sincos(latex(f))   
   
    kq= cos(x)**2-b*cos(x) 
    kq2=a*sin(x)+b 
    kq3=integrate(cos(x)*(a*sin(x)+b),x)
    kq4=integrate(sin(x),x)*integrate(a*cos(x)+b,x)

    kq= f"$ {latex(my_module.hien_phan_so(-a/2))}{latex(kq)}+C$"
    kq=kq.replace("\\cos^{2}{\\left(x \\right)}","\\cos^2x")
    kq=kq.replace("\\cos{\\left(x \\right)}","\\cos x")
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"


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
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{ham}{d_x}}}$."
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

#[D12_C4_B2_05]. Nguyên hàm đổi biến (lnx)^n/x
def zz8zz_L12_C4_B2_05():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
   
    dau_b=tao_dau(b)
    a1=xu_li_heso_1(a)
    f = f"\\dfrac{{ \\left({a1}\\ln x {dau_b} {b}\\right)}}{{x}}"
    f_du=f"\\left({a1}\\ln x {dau_b} {b}\\right)d(\\ln x)"
    
    
    kq= f"$ {latex(my_module.hien_phan_so(a/2))}\\ln^2 x {dau_b}{b}\\ln x+C$"
    kq2= f"$ {latex(my_module.hien_phan_so(a/2))}\\ln^2 x {dau_b}{b}+C$"    
    kq3= f"$  \\left({a1}\\ln x {dau_b} {b} \\right)^2 +C$"  
    kq4=f"$ {latex(my_module.hien_phan_so(a/2))}\\ln^2 x {dau_b}{b}x+C$"
    
    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án

    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Tìm nguyên hàm $  \\int {{{f}{d_x}}}$."

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


#BÀI 3- NGUYÊN HÀM TỪNG PHẦN
#[D12_C4_B3_01]. Nguyên hàm P(x).sin hoặc P(x).cos
def zz8zz_L12_C4_B3_01():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a=random.randint(1,8)
    b=random.randint(-10,10)
    m=random.randint(1,10)
    
    ham=random.choice(["sin","cos"])
    ham="cos"
    if ham=="sin":        
        f = (a*x+b)*sin(m*x)
               
        kq=thay_the_ngoac_sincos(f"\\left({phan_so(-a/m)}x+{phan_so(-b/m)}\\right)\\cos {m}x +{phan_so(a/m**2)}\\sin {m}x")
        kq2=thay_the_ngoac_sincos(f"\\left({phan_so(a/m)}x+{phan_so(-b/m)}\\right)\\cos {m}x +{phan_so(a/m**2)}\\sin {m}x")
        kq3=thay_the_ngoac_sincos(f"\\left({phan_so(-a/m)}x+{phan_so(-b/m)}\\right)\\sin {m}x +{phan_so(a/m**2)}\\cos {m}x")
        kq4=thay_the_ngoac_sincos(f"\\left({phan_so(a/m)}x+{phan_so(b/m)}\\right)\\sin {m}x +{phan_so(-a/m**2)}\\cos {m}x")

    if ham=="cos":        
        f = (a*x+b)*cos(m*x)
               
        kq=thay_the_ngoac_sincos(f"\\left({phan_so(a/m)}x+{phan_so(b/m)}\\right)\\sin {m}x +{phan_so(a/m**2)}\\cos {m}x")
        kq2=thay_the_ngoac_sincos(f"\\left({phan_so(-a/m)}x+{phan_so(b/m)}\\right)\\sin {m}x +{phan_so(-a/m**2)}\\cos {m}x")
        kq3=thay_the_ngoac_sincos(f"\\left({phan_so(-a/m)}x+{phan_so(-b/m)}\\right)\\cos {m}x +{phan_so(a/m**2)}\\sin {m}x")
        kq4=thay_the_ngoac_sincos(f"\\left({phan_so(a/m)}x+{phan_so(-b/m)}\\right)\\cos {m}x +{phan_so(a/m**2)}\\sin {m}x")
       
    kq= f"$ {kq}+C$"
    kq2=f"$ {kq2}+C$"
    kq3=f"$ {kq3}+C$"
    kq4=f"$ {kq4}+C$"
    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{my_module.thay_the_ngoac_sincos(latex(f))}{d_x}}}$." 
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

#[D12_C4_B3_02]. Nguyên hàm P(x).e^(ax+b) 
def zz8zz_L12_C4_B3_02():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    k=random.randint(2,3)    
    a = [random.choice([random.randint(-5, -1), random.randint(1, 5)]) for i in range(k)]
    m=random.randint(1, 5) 
    n=random.randint(0, 5)

    t= sum(a[i]*x**i for i in range(k))     
    
    f = t*exp(m*x+n)   

    kq= integrate(f, x) 
    kq2=diff(f, x)
    kq3=integrate(f, x)*random.randint(2,5)
    kq4=integrate(t, x)*integrate(exp(m*x+n), x)  
       
    kq= f"$ {latex(kq)}+C$"
    kq2=f"$ {latex(kq2)}+C$"
    kq3=f"$ {latex(kq3)}+C$"
    kq4=f"$ {latex(kq4)}+C$"

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
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{latex(f)}{d_x}}}$."
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

#[D12_C4_B3_03]. Nguyên hàm P(x).ln(mx)
def zz8zz_L12_C4_B3_03():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)]) 
    m=random.randint(1, 10)    
  
    f = f"\\left({latex(a*x+b)}\\right)\\ln {m}x"
    f=f.replace("1x","x")

    
    kq= f"$ \\left({latex(a*x**2/2+b*x)}\\right)\\ln {m}x - \\left({latex(a*x**2/4 + b*x)}\\right) +C$"
    kq2=f"$ \\left({latex(a*x**2/2+b*x)}\\right)\\ln {m}x + \\left({latex(a*x**2 + b*m*x)}\\right) +C$"
    kq3=f"$ \\left({latex(a*x**2+b*x)}\\right)\\ln x - \\left({latex(a*x**2/4 + b*x)}\\right) +C$"
    kq4=f"$ \\left({latex(a*x**2/2+b*x)}\\right)\\ln {m}x + \\left({latex(a*m*x**2 + b*m*x)}\\right) +C$"

    kq=kq.replace("1x","x")
    kq2=kq2.replace("1x","x")
    
    kq3=kq3.replace("1x","x")
    kq4=kq4.replace("1x","x")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm nguyên hàm $  \\int {{{f}{d_x}}}$."
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

################ Bài 4: TÍCH PHÂN #################
#[D12_C4_B4_01]-M1. Cho F(a) và F(b). Tính tích phân từ a đến b.
def zz8zz_L12_C4_B4_01():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.randint(-4,10)  
    b=a+random.randint(1,6)
    F_a = random.choice([random.randint(-10, -1), random.randint(2, 10)])
    F_b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if F_a==F_b:
        F_b=F_a+random.randint(2,5)
     
    f=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
 
    kq =F_b - F_a
    kq2=F_a + F_b
    kq3=F_a - F_b
    kq4=F_a * F_b

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $ F({a})={F_a},F({b})={F_b}$. Tính ${f}$.\n"

    hieu=show_hieu(F_b,F_a)

    noi_dung_loigiai=f"${f}=F({b})-F({a})={hieu}={kq}$ ."    
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

#[D12_C4_B4_02]-M1. Cho 2 tích phân theo f và g. Tính tích phân (m.f+n.g).
def zz8zz_L12_C4_B4_02():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.randint(-10,10)  
    b=a+random.randint(1,10)
    m = random.choice([random.randint(-10, -1), random.randint(2, 10)])
    n = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if n==m:
        n=m+random.randint(2,5)
        if n==0: n=1
    dau_n=tao_dau(n)
    n1=xu_li_heso_1(n)
     
    f1=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
    f2=f"  \\int\\limits_{{{a}}}^{{{b}}} {{g(x){d_x}}}"
    f3=f"  \\int\\limits_{{{a}}}^{{{b}}} {{\\left[ {m}f(x){dau_n}{n1}g(x)\\right]{d_x}}}"

    giatri_f1 = random.choice([random.randint(-15, -1), random.randint(1, 15)])
    giatri_f2 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if giatri_f1==giatri_f2:
        giatri_f2=giatri_f1 + random.randint(1,10)
 
    kq =m*giatri_f1 + n*giatri_f2
    kq2=m*giatri_f1 - n*giatri_f2
    kq3=giatri_f1 + m*giatri_f2
    kq4_1=m*(giatri_f1 + giatri_f2) 
    kq4_2=n*(giatri_f1 - giatri_f2)  
    kq4=random.choice([kq4_1,kq4_2])

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho $ {f1}={giatri_f1},{f2}={giatri_f2}$. Tính ${f3}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    tich_mf=show_tich(m,giatri_f1)
    tich_ng=show_tich(n,giatri_f2)
    noi_dung_loigiai=f"${f3}={m}{f1}{dau_n}{n1}{f2}={tich_mf}{dau_n}{tich_ng}={kq}$ ."    
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

#[D12_C4_B4_03]-M1. Tính tổng tích phân trên 2 đoạn nối tiếp
def zz8zz_L12_C4_B4_03():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.choice([random.randint(-6, -1), random.randint(1, 6)]) 
    b=a+random.randint(1,5)  
    c=b+random.randint(1,10)  
    f1=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
    f2=f"  \\int\\limits_{{{b}}}^{{{c}}} {{f(x){d_x}}}"
    f3=f"  \\int\\limits_{{{a}}}^{{{c}}} {{f(x){d_x}}}"

    giatri_f1 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
    giatri_f2 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
    if giatri_f1==giatri_f2:
        giatri_f2=giatri_f1 + random.randint(1,10)
 
    kq =giatri_f1 + giatri_f2
    kq2=giatri_f1 - giatri_f2
    kq3=giatri_f2 - giatri_f1
    kq4=giatri_f1*giatri_f2  

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho ${f1}={giatri_f1},{f2}={giatri_f2}$. Tính ${f3}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"${f3}={f1} + {f2}={giatri_f1}+{giatri_f2}={kq}$ ."    
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

#[D12_C4_B4_04]-M1. Cho theo f. Tính tích phân (m.f+n).
def zz8zz_L12_C4_B4_04():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.randint(-4,10)  
    b=a+random.randint(2,8)
    m = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    n = random.choice([random.randint(-10, -2), random.randint(2, 10)])
    if n==m:
        n=m+random.randint(2,5)
        if n==0: n=1

    dau_n=tao_dau(n)
    if n==-1 or n==1:
        n1=1
    else:
        n1= xu_li_heso_1(n)
    m1=xu_li_heso_1(m)
    f=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
    g=f"  \\int\\limits_{{{a}}}^{{{b}}} {{\\left[ {m1}f(x){dau_n}{n1}\\right]{d_x}}}"

    giatri_f = random.choice([random.randint(-15, -1), random.randint(1, 15)])
 
    kq =m*giatri_f + n*(b-a)
    kq2=m*giatri_f + n
    kq3=m*giatri_f + n*(a-b)
    kq4=m*giatri_f +n*b-a

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho tích phân ${f}={giatri_f}$. Tính tích phân ${g}$."
    debai= f"{noi_dung}\n"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    tich_mf=show_tich(m,giatri_f)
    hieu=show_hieu(b,a)

    noi_dung_loigiai=f"${g}={m1}{f}{dau_n}{n1}({hieu})={tich_mf}{dau_n}{n1}.{b-a}={kq}$ ."    
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

#[D12_C4_B4_05]-M2. Cho tích phân f và F(a). Tính F(b).
def zz8zz_L12_C4_B4_05():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.randint(-4,10)  
    b=a+random.randint(1,6)
    F_a = random.choice([random.randint(-10, -1), random.randint(2, 10)])
    F_b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if F_a==F_b:
        F_b=F_a+random.randint(2,5)
     
    f=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
    giatri_f = random.choice([random.randint(-15, -1), random.randint(1, 15)])
    chon= random.choice(["F_a","F_b"])
    hieu_b_a=show_hieu(F_b,F_a)
    hieu_F_b=show_hieu(F_b, giatri_f)
    tong_F_a=show_tong(giatri_f,F_a)
    if chon=="F_a":
        noi_dung=f"Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn ${f}={giatri_f},F({b})={F_b}$. Tính ${{F({a})}}$.\n"
        kq=F_b - giatri_f
        kq2=F_b + giatri_f
        kq3=giatri_f - F_b
        kq4=giatri_f*F_b
        noi_dung_loigiai=f"${f}=F({b})-F({a})={F_b}-F({a})$. Do đó: $F({a})={hieu_F_b}={kq}$."  
    else: 
        noi_dung=f"Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn ${f}={giatri_f},F({a})={F_a}$. Tính ${{F({b})}}$.\n"

        kq=F_a + giatri_f
        kq2=F_a - giatri_f
        kq3=giatri_f - F_a
        kq4=giatri_f * F_a
        noi_dung_loigiai=f"${f}=F({b})-F({a})=F({b})-({F_a})$. Do đó: $F({b})={tong_F_a}={kq}$."  

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

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

#[D12_C4_B4_06]-M1. Cho f(a) và f(b). Tính tích phân f'(x).
def zz8zz_L12_C4_B4_06():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.randint(-4,10)  
    b=a+random.randint(1,6)
    F_a = random.choice([random.randint(-10, -1), random.randint(2, 10)])
    f_b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if F_a==f_b:
        f_b=F_a+random.randint(2,5)
     
    f=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f'(x){d_x}}}"

    kq=f_b - F_a
    kq2=f_b + F_a
    kq3=F_a-f_b
    kq4=F_a*f_b

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    hieu=show_hieu(f_b,F_a)
    noi_dung=f"Cho hàm số $f(x)$ có đạo hàm trên đoạn ${{[{a};{b}]}}$, $f({a})={F_a}$ và $f({b})={f_b}$. Tính ${f}$.\n"
    noi_dung_loigiai=f"${f}=f({b})-f({a})={hieu}={kq}$." 
    
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


#[D12_C4_B4_07]-M2. Cho tích phân f'(x) và f(a). Tính f(b).
def zz8zz_L12_C4_B4_07():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.randint(-4,10)  
    b=a+random.randint(1,6)
    f_a = random.choice([random.randint(-10, -1), random.randint(2, 10)])
    f_b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if f_a==f_b:
        f_b=f_a+random.randint(2,5)
     
    f=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f'(x){d_x}}}"
    giatri_f = random.choice([random.randint(-15, -1), random.randint(1, 15)])
    chon= random.choice(["f_a","f_b"])
    hieu_b_a=show_hieu(f_b,f_a)
    hieu_f_b=show_hieu(f_b, giatri_f)
    tong_f_a=show_tong(giatri_f, f_a)
    if chon=="f_a":
        noi_dung=f"Biết ${f}={giatri_f},f({b})={f_b}$. Tính ${{f({a})}}$.\n"

        kq=f_b - giatri_f
        kq2=f_b + giatri_f
        kq3=giatri_f - f_b
        kq4=giatri_f*f_b

        pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
        kq2=pa_kotrung[1]
        kq3=pa_kotrung[2]
        kq4=pa_kotrung[3]

        noi_dung_loigiai=f"${f}=f({b})-f({a})={f_b}-f({a})$. Do đó: $f({a})={hieu_f_b}={kq}$."  
    else: 
        noi_dung=f"Biết ${f}={giatri_f},f({a})={f_a}$. Tính ${{f({b})}}$.\n"

        kq=f_a + giatri_f
        kq2=f_a - giatri_f
        kq3=giatri_f - f_a
        kq4=giatri_f * f_a

        pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
        kq2=pa_kotrung[1]
        kq3=pa_kotrung[2]
        kq4=pa_kotrung[3]

        noi_dung_loigiai=f"${f}=f({b})-f({a})=f({b})-({f_a})$. Do đó: $f({b})={tong_f_a}={kq}$."  



    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    
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

#[D12_C4_B4_08]-M2. Cho tphan_a^c(f) và tphan_a^b(f). Tính tphan_b^c(f), a<b<c.
def zz8zz_L12_C4_B4_08():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.choice([random.randint(-6, -1), random.randint(1, 6)]) 
    b=a+random.randint(1,5)  
    c=b+random.randint(1,10)  
    f1=f"  \\int\\limits_{{{a}}}^{{{c}}} {{f(x){d_x}}}"
    f2=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
    f3=f"  \\int\\limits_{{{b}}}^{{{c}}} {{f(x){d_x}}}"

    giatri_f1 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
    giatri_f2 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
    if giatri_f1==giatri_f2:
        giatri_f2=giatri_f1 + random.randint(1,10)
 
    kq =giatri_f1 - giatri_f2
    kq2=giatri_f1 + giatri_f2
    kq3=giatri_f2 - giatri_f1
    kq4=giatri_f1*giatri_f2  

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho ${f1}={giatri_f1},{f2}={giatri_f2}$. Tính ${f3}$.\n"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    hieu=show_hieu(giatri_f1,giatri_f2)
    noi_dung_loigiai=f"${f1}={f2} + {f3} \\Rightarrow {f3}={f1} - {f2}={hieu}={kq}$."    
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

#[D12_C4_B4_09]-M2. Cho tphan_a^d(f) và tphan_b^c(f). Tính tphan_a^b(f) + tphan_c^d(f), a<b<c<d.
def zz8zz_L12_C4_B4_09():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.choice([random.randint(-6, -1), random.randint(1, 6)]) 
    b=a+random.randint(1,5)  
    c=b+random.randint(1,10)  
    d=c+random.randint(1,7)

    f1=f"  \\int\\limits_{{{a}}}^{{{d}}} {{f(x){d_x}}}"
    f2=f"  \\int\\limits_{{{b}}}^{{{c}}} {{f(x){d_x}}}"
    f3=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
    f4=f"  \\int\\limits_{{{c}}}^{{{d}}} {{f(x){d_x}}}"

    giatri_f1 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
    giatri_f2 = random.choice([random.randint(-20, -1), random.randint(1, 20)])
    if giatri_f1==giatri_f2:
        giatri_f2=giatri_f1 + random.randint(1,10)
 
    kq =giatri_f1 - giatri_f2
    kq2=giatri_f1 + giatri_f2
    kq3=giatri_f2 - giatri_f1
    kq4=giatri_f1*giatri_f2  

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {{{kq}}}$"
    pa_B= f"$ {{{kq2}}}$"
    pa_C= f"$ {{{kq3}}}$"
    pa_D= f"$ {{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho ${f1}={giatri_f1},{f2}={giatri_f2}$. Tính ${f3}+{f4}$.\n"
    debai= f"{noi_dung}\n"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    hieu=show_hieu(giatri_f1,giatri_f2)
    noi_dung_loigiai=f"${f1}={f2} + {f3} +{f4} \\Rightarrow {f3}+{f4}={f1}-{f2}={hieu}={kq}$ ."    
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

#4.4.2 Tích phân các hàm số thường gặp
#[D12_C4_B4_10]. Tính tích phân của m/(ax+b)
def zz8zz_L12_C4_B4_10():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    m =  random.randint(2,10)
    if m==a: m=m+random.randint(1,3)
    n = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = m/(a*x+b)

    x_1=int((-b/a))+random.randint(2,5)
    x_2=x_1 + random.randint(1,5)

    kq= thay_the_tich_phan(f"$ {latex(my_module.hien_phan_so(m/a))}\\ln {latex(my_module.hien_phan_so(abs((a*x_2+b)/(a*x_1+b))))}$")
    kq2=thay_the_tich_phan(f"$ {m}\\ln {latex(my_module.hien_phan_so(abs((a*x_2+b)/(a*x_1+b))))}$")
    kq3=thay_the_tich_phan(f"$ \\ln {latex(my_module.hien_phan_so(abs((a*x_2+b)/(a*x_1+b))))}$")
    kq4=thay_the_tich_phan(f"$ {latex(my_module.hien_phan_so(m/a))}\\ln {latex(my_module.hien_phan_so(abs((a*x_2+b)*(a*x_1+b))))}$")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    noi_dung= f"Tính tích phân $  \\int \\limits_{{{x_1}}}^{{{x_2}}}{{{latex(f)}{d_x}}}$."       
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"$ \\int\\limits_{{{x_1}}}^{{{x_2}}}{{{latex(f)}{d_x}}}={latex(my_module.hien_phan_so(m/a))}\\ln |{latex(a*x+b)}| \\bigg|_{{{x_1}}}^{{{x_2}}}$"\
    f"$= {latex(my_module.hien_phan_so(m/a))} \\left(\\ln|{latex(a*x_1+b)}| - \\ln|{latex(a*x_2+b)}|\\right)=${kq}.".replace(f"-1\\ln","\\ln")
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

#[D12_C4_B4_11]. Tính tích phân của (mx+n)/(ax+b)
def zz8zz_L12_C4_B4_11():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.randint(1, 5)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    t = random.randint(2,4)
    m =  a*t
    n = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    f = (m*x+n)/(a*x+b)

    x_1=int((-b/a))+random.randint(2,5)
    x_2=x_1 + random.randint(2,5)
    t_1,t_2=random.randint(1,3),random.randint(1,3)
    a_1, b_1, c_1 = t*(x_2-x_1), (n-b*t)/a, abs((a*x_2+b)/(a*x_1+b))
    noi_dung= thay_the_tich_phan(f"Biết tích phân $  \\int \\limits_{{{x_1}}}^{{{x_2}}}{{{latex(f)}{d_x}}}=a+b\\ln {phan_so(c_1)}$, với $a,b\\in \\mathbb{{R}}$."\
        f" Tính $P={t_1}a+{t_2}b$.")
    
    kq=t_1*a_1 + t_2*b_1 
    kq2=t_1*a_1 - t_2*b_1
    kq3=t_1*a_1 + t_2*b_1 -random.randint(1,3)
    kq4=t_1*a_1 + t_2*b_1 +random.randint(1,3)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=thay_the_tich_phan(f"$ \\int\\limits_{{{x_1}}}^{{{x_2}}}{{{latex(f)}{d_x}}}$"\
    f"$= \\int\\limits_{{{x_1}}}^{{{x_2}}} {{({t}+{latex((n-b*t)/(a*x+b))}){d_x}}}$"\
    f"$= ({t}+{phan_so((n-b*t)/(a))}\\ln |{latex(a*x+b)}|) \\bigg|_{{{x_1}}}^{{{x_2}}}={t*(x_2-x_1)}+{phan_so(((n-b*t)/a))}\\ln {phan_so((abs((a*x_2+b)/(a*x_1+b))))}$.\n\n"\
    f"Do đó: $a={a_1}, b={phan_so(b_1)}$. Suy ra $ P={t_1}a+{t_2}b={phan_so(kq)}$."
    )

    # kq= thay_the_tich_phan(f"$ {t*(x_2-x_1)}+{phan_so(((n-b*t)/a))}\\ln {phan_so((abs((a*x_2+b)/(a*x_1+b))))}$")
    # kq2=thay_the_tich_phan(f"$ {phan_so((m/a))}\\ln {latex(my_module.hien_phan_so(abs((a*x_2+b)/(a*x_1+b))))}$")
    # kq3=thay_the_tich_phan(f"$ {(x_2-x_1)}{phan_so(((n-b*t)/a))}\\ln {phan_so((abs((a*x_2+b)/(a*x_1+b))))}$")
    # kq4=thay_the_tich_phan(f"$ {t}+{phan_so((n-b*t)/a)}\\ln {phan_so((abs((a*x_2+b)/(a*x_1+b))))}$")

    #Tạo các phương án
    pa_A= f"*$ P={phan_so(kq)}$"
    pa_B= f"$ P={phan_so(kq2)}$"
    pa_C= f"$ P={phan_so(kq3)}$"
    pa_D= f"$ P={phan_so(kq4)}$"
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

#[D12_C4_B4_12]. Tính tích phân của đa thức
def zz8zz_L12_C4_B4_12():       
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    k=random.randint(2,4)
    a = [random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(k)]    
    f = sum(a[i]* x**i for i in range(k)) 

    x_1=random.randint(-5,4)
    x_2=x_1 + random.randint(1,5)

    kq=integrate(f, (x,{x_1},{x_2}))
    kq2=integrate(f+1, (x,{x_1},{x_2}))
    kq3=integrate(f+x, (x,{x_1},{x_2}))
    kq4=integrate(f-2, (x,{x_1},{x_2}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {phan_so(kq)}$"
    pa_B= f"$ {phan_so(kq2)}$"
    pa_C= f"$ {phan_so(kq3)}$"
    pa_D= f"$ {phan_so(kq4)}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    noi_dung= f"Tính tích phân $  \\int \\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right){d_x}}}$."       
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Sử dụng máy tính ta thu được kết quả bằng $ {{{phan_so(kq)}}}$."
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

#[D12_C4_B4_13]. Tính tích phân của asinbx
def zz8zz_L12_C4_B4_13():   
    x=sp.symbols("x") 
    d_x=f"\\mathrm{{\\,d}}x"    
    a = random.randint(1, 10)
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    f = b*sin(a*x)
    ham=my_module.thay_the_ngoac_sincos(latex(f))

    x_1=random.choice([0, pi/6, pi/4,pi/3, pi/2])
    if x_1==0:
        x_2=random.choice([pi/6,pi/4, pi/3, 2*pi/3, 3*pi/4, 5*pi/6, pi,2*pi])

    if x_1==pi/6:
        x_2=random.choice([pi/4, pi/3, 2*pi/3, 3*pi/4, 5*pi/6, pi,2*pi])

    if x_1==pi/4:
        x_2=random.choice([pi/3, 2*pi/3, 3*pi/4, 5*pi/6, pi , 2*pi])

    if x_1==pi/3:
        x_2=random.choice([2*pi/3, 3*pi/4, 5*pi/6, pi , 2*pi])

    if x_1==pi/2:
        x_2=random.choice([2*pi/3, 3*pi/4, 5*pi/6, pi , 2*pi])

    kq=integrate(f, (x,{x_1},{x_2}))
    kq2=integrate(f+cos(x), (x,{x_1},{x_2}))
    kq3=integrate(f+1, (x,{x_1},{x_2}))
    kq4=integrate(f-sin(x), (x,{x_1},{x_2}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$ {latex(kq)}$"
    pa_B= f"$ {latex(kq2)}$"
    pa_C= f"$ {latex(kq3)}$"
    pa_D= f"$ {latex(kq4)}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    noi_dung= f"Tính tích phân $  \\int \\limits_{{{latex(x_1)}}}^{{{latex(x_2)}}} {{{ham}{d_x}}}$."       
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"$ \\int \\limits_{{{latex(x_1)}}}^{{{latex(x_2)}}}{{{ham}{d_x}}}={phan_so(-b/a)}\\cos {latex(a*x)} \\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$"\
    f"$ = {phan_so(-b/a)}\\left(\\cos{latex(a*x_2)} - \\cos{latex(a*x_1)}\\right)= {{{latex(kq)}}}$."
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

################ Bài 5: ỨNG DỤNG CỦA TÍCH PHÂN #################
#[D12_C4_B5_01]. Diện tích hình phẳng: y=f(x),Ox,x=a,x=b
def zz8zz_L12_C4_B5_01():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    chon=random.choice([1,2])
    if chon==1: #Hàm bậc nhất
        a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
        x_0=random.randint(-5,5) 
        f=expand(a*(x-x_0))
        can =random.choice([1,2])
        if can==1:
            x_1=x_0+random.randint(1,5)
            x_2=x_1+random.randint(1,5)
        else:
            x_2=x_0-random.randint(4,7)
            x_1=x_2-random.randint(1,5)
        
    else: #Hàm bậc hai
        a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
        x_01=random.randint(-5,5)
        x_02=x_01+random.randint(1,3)
        f=expand(a*(x-x_01)*(x-x_02))
        can =random.choice([1,3])
        if can==1:
            x_1=x_01
            x_2=x_02
        elif can==2:
            x_1=x_02+random.randint(1,4)
            x_2=x_1+random.randint(1,4)
        else:
            x_2=x_01-random.randint(1,4)
            x_1=x_2-random.randint(1,4)

    kq= abs(integrate(f, (x,{x_1},{x_2})))
    kq2=abs(integrate(f, (x,{x_1},{x_2+1})))
    kq3=abs(integrate(f, (x,{x_1-3},{x_2})))
    kq4=abs(integrate(f, (x,{x_1-4},{x_2})))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{{latex(my_module.hien_phan_so(kq))}}}$"
    kq2=f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    kq3=f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    kq4=f"${{{latex(my_module.hien_phan_so(kq4))}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $y={latex(f)}$, trục ${{Ox}}$ và các đường thẳng $x={x_1},x={x_2}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Diện tích hình phẳng xác định bởi: $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f)}\\right|{d_x}}}=${kq}."    
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

#[D12_C4_B5_02]. Diện tích hình phẳng: y=f(x),y=g(x),x=a,x=b
def zz8zz_L12_C4_B5_02():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    x_1=random.randint(-10,10) 
    x_2=x_1+random.randint(1,6)
    b=random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c=random.randint(-5,5)
    d=random.randint(-6,6)

    chon=random.choice([1,2])
    if chon==1:
        f1=expand(a*(x-x_1)*(x-x_2)+b*x+c)
        f2=b*x+c
    else:
        f1=expand(a*(x-x_1)*(x-x_2)+b*x**2+c*x+d)
        f2=b*x**2+c*x+d

    f=f1-f2

    kq= abs(integrate(f, (x,{x_1},{x_2})))
    kq2=abs(integrate(f, (x,{x_1-3},{x_2+1})))
    kq3=abs(integrate(f, (x,{x_1-1},{x_2-1})))
    kq4=abs(integrate(f, (x,{x_1},{x_2+3})))

    kq =f"${{{latex(my_module.hien_phan_so(kq))}}}$"
    kq2=f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    kq3=f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    kq4=f"${{{latex(my_module.hien_phan_so(kq4))}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Tính diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(f1)},y={latex(f2)}$ và các đường thẳng $x={x_1},x={x_2}$.\n"
    debai= f"{noi_dung}\n"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Diện tích hình phẳng xác định bởi: $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f1)}-({latex(f2)})\\right|{d_x}}}$.\n"\
                     f"$=  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f)}\\right|{d_x}}}=$ {kq}"   
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


#[D12_C4_B5_03]. Tìm công thức tính diện tích từ hình vẽ có 1 đồ thị.
def zz8zz_L12_C4_B5_03():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    x_1=random.randint(-6,-1)
    x_2=random.randint(1,6)    

    chon=random.randint(1,2)    
    if chon==1:
        f_1=x**2-x_1*x
        y_1=round(f_1.subs(x,x_1/2),2)-0.5

        f_2=-x**2+x_2*x
        y_2=round(f_2.subs(x,x_2/2),2)+0.5
        code_hinh=f"\\begin{{tikzpicture}}[yscale=.7,>=stealth] \n\
        \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
        \\draw[->] (0,{y_1}) -- (0,{y_2}) node[left] {{$y$}}; \n\
        \\tkzDefPoints{{0/0/O}} \n\
        \\tkzDrawPoints[fill=black](O) \n\
        \\tkzLabelPoint[below right](O){{$O$}} \n\
        \\draw ({x_1},0) node[below left]{{${x_1}$}}; \n\
        \\draw ({x_2},0) node[below right]{{${x_2}$}}; \n\
        %Vẽ nữa dưới\n \
        \\draw[color=blue,very thick, domain={x_1}:0] plot (\\x,{{(\\x)*(\\x-{x_1})}}); \n\
        \\draw [draw=none, pattern = north west lines, pattern color=gray!100, samples=100]\n\
        plot[domain={x_1}:0] (\\x, {{(\\x)*(\\x-{x_1})}})--({x_1},0)--(0,0)--cycle; \n\
        %Vẽ nữa trên\n \
        \\draw[color=blue,very thick, domain=0:{x_2}] plot (\\x,{{(-\\x)*(\\x-{x_2})}}); \n\
        \\draw [draw=none, pattern = north west lines, pattern color=gray!100, samples=100]\n\
        plot[domain=0:{x_2}] (\\x, {{(-\\x)*(\\x-{x_2})}})--(0,0)--({x_2},0)--cycle; \n\
        \\end{{tikzpicture}} \n"

        kq =f"$S=-  \\int\\limits_{{{x_1}}}^0 f(x)\\mathrm{{\\,d}}x+\\int\\limits_0^{{{x_2}}}  f(x)\\mathrm{{\\,d}}x$"   
        kq2=f"$S=   \\int\\limits_{{{x_1}}}^0 f(x)\\mathrm{{\\,d}}x-\\int\\limits_0^{{{x_2}}} f(x)\\mathrm{{\\,d}}x$"
        kq3=f"$S=  \\int\\limits_{{{x_1}}}^{{{x_2}}} f(x)\\mathrm{{\\,d}}x$"
        kq4= f"$S=  \\int\\limits_{{{x_1}}}^0 f(x)\\mathrm{{\\,d}}x+\\int\\limits_0^{{{x_2}}} f(x)\\mathrm{{\\,d}}x$"
    else:
        f_1=-x**2+x_1*x
        y_1=round(f_1.subs(x,x_1/2),2)+0.5

        f_2=x**2-x_2*x
        y_2=round(f_2.subs(x,x_2/2),2)-0.5
        code_hinh=f"\\begin{{tikzpicture}}[yscale=.7,>=stealth] \n\
        \\draw[->] ({x_1-0.5},0) -- ({x_2+0.5},0) node[below] {{$x$}}; \n\
        \\draw[->] (0,{y_2}) -- (0,{y_1}) node[left] {{$y$}}; \n\
        \\tkzDefPoints{{0/0/O}} \n\
        \\tkzDrawPoints[fill=black](O) \n\
        \\tkzLabelPoint[below left](O){{$O$}} \n\
        \\draw ({x_1},0) node[below]{{${x_1}$}}; \n\
        \\draw ({x_2},0) node[below]{{${x_2}$}}; \n\
        %Vẽ nữa dưới\n \
        \\draw[color=blue,very thick, domain={x_1}:0] plot (\\x,{{(-\\x)*(\\x-{x_1})}}); \n\
        \\draw [draw=none, pattern = north west lines, pattern color=gray!100, samples=100]\n\
        plot[domain={x_1}:0] (\\x, {{(-\\x)*(\\x-{x_1})}})--({x_1},0)--(0,0)--cycle; \n\
        %Vẽ nữa trên\n \
        \\draw[color=blue,very thick, domain=0:{x_2}] plot (\\x,{{(\\x)*(\\x-{x_2})}}); \n\
        \\draw [draw=none, pattern = north west lines, pattern color=gray!100, samples=100]\n\
        plot[domain=0:{x_2}] (\\x, {{(\\x)*(\\x-{x_2})}})--(0,0)--({x_2},0)--cycle; \n\
        \\end{{tikzpicture}} \n"

        kq =f"$S=   \\int\\limits_{{{x_1}}}^0 f(x)\\mathrm{{\\,d}}x-\\int\\limits_0^{{{x_2}}} f(x)\\mathrm{{\\,d}}x$"  
        kq2=f"$S=-  \\int\\limits_{{{x_1}}}^0 f(x)\\mathrm{{\\,d}}x+\\int\\limits_0^{{{x_2}}}  f(x)\\mathrm{{\\,d}}x$" 
        
        kq3=f"$S=  \\int\\limits_{{{x_1}}}^{{{x_2}}} f(x)\\mathrm{{\\,d}}x$"
        kq4= f"$S=  \\int\\limits_{{{x_1}}}^0 f(x)\\mathrm{{\\,d}}x+\\int\\limits_0^{{{x_2}}} f(x)\\mathrm{{\\,d}}x$"

    code=f"\\documentclass[border=2pt]{{standalone}}\n\
    \\usepackage{{tkz-tab,tikz,tkz-euclide}} \n\
    \\usetikzlibrary{{calc,intersections,patterns}}\n\
    \\begin{{document}} \n\
    {code_hinh}\
    \\end{{document}}\n"
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

    noi_dung=f"Cho hàm số $y=f(x)$ có đồ thị như hình vẽ. Gọi ${{S}}$ là diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=f(x)$ và trục hoành (phần gạch chéo trong hình). Khẳng định nào sau đây đúng.\n\n"
    debai= f"{noi_dung}\n"\
           f"{file_name}\n"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Diện tích hình phẳng xác định bởi: {kq}.\n"\
       
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
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_04]. Diện tích hình phẳng: y=f(x),y=g(x)
def zz8zz_L12_C4_B5_04():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    x_1=random.randint(-10,10) 
    x_2=x_1+random.randint(1,6)
    b=random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c=random.randint(-5,5)
    d=random.randint(-6,6)

    chon=random.choice([1,2])
    if chon==1:
        f1=expand(a*(x-x_1)*(x-x_2)+b*x+c)
        f2=b*x+c
    else:
        f1=expand(a*(x-x_1)*(x-x_2)+b*x**2+c*x+d)
        f2=b*x**2+c*x+d

    f=f1-f2

    kq= abs(integrate(f, (x,{x_1},{x_2})))
    kq2=abs(integrate(f, (x,{x_1-3},{x_2+1})))
    kq3=abs(integrate(f, (x,{x_1-1},{x_2-1})))
    kq4=abs(integrate(f, (x,{x_1},{x_2+3})))

    kq =f"${{{latex(my_module.hien_phan_so(kq))}}}$"
    kq2=f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    kq3=f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    kq4=f"${{{latex(my_module.hien_phan_so(kq4))}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Tính diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(f1)}$ và $y={latex(f2)}$."
    debai= f"{noi_dung}\n"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Xét phương trình ${latex(f1)}={latex(f2)}\\Leftrightarrow {latex(f)}=0\\Leftrightarrow x={x_1},x={x_2}$.\n"\
    f"Diện tích hình phẳng: $S=  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f1)}-({latex(f2)})\\right|{d_x}}}$"\
                     f"$=  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f)}\\right|{d_x}}}=$ {kq}"   
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

#[D12_C4_B5_05]. Thể tích quay quanh Ox bởi hình: y=f(x),Ox,x=a,x=b
def zz8zz_L12_C4_B5_05():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    chon=random.randint(1,3)
    if chon==1: #Hàm bậc nhất
        a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
        x_0=random.randint(-5,5) 
        f=expand(a*(x-x_0))
        can =random.choice([1,2])
        if can==1:
            x_1=x_0+random.randint(1,3)
            x_2=x_1+random.randint(1,4)
        else:
            x_2=x_0-random.randint(1,3)
            x_1=x_2-random.randint(1,4)
        
    if chon==2: #Hàm bậc hai
        a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
        x_01=random.randint(-5,5)
        x_02=x_01+random.randint(1,3)
        f=expand(a*(x-x_01)*(x-x_02))
        can =random.choice([1,3])
        if can==1:
            x_1=x_01
            x_2=x_02
        elif can==2:
            x_1=x_02+random.randint(1,4)
            x_2=x_1+random.randint(1,4)
        else:
            x_2=x_01-random.randint(1,4)
            x_1=x_2-random.randint(1,4)

    if chon==3: #Hàm căn(ax+b)
        a = random.choice([random.randint(1, 10)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        x_1=random.randint(int(-b/a)+1,int(-b/a)+5)
        x_2=x_1+random.randint(1,5)
        f=sqrt(a*x+b)
        

    kq= integrate(f**2, (x,{x_1},{x_2}))
    kq2=integrate(f**2, (x,{x_1},{x_2+1}))
    kq3=integrate(f**2, (x,{x_1},{x_2}))+random.randint(2,4)
    kq4=integrate(f**2, (x,{x_1},{x_2+random.randint(2,4)}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    kq =f"${{ {latex(my_module.hien_phan_so(kq))}\\pi}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}\\pi}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}\\pi$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho hình phẳng giới hạn bởi đồ thị hàm số $y={latex(f)}$, trục hoành và các đường thẳng $x={x_1},x={x_2}$."\
    f" Tính thể tích khối tròn xoay tạo thành khi cho hình phẳng đó quay quanh trục ${{Ox}}.$"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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

#[D12_C4_B5_06]. Thể tích quay quanh Ox bởi hình: y=ax+b,Ox,x=a,x=b
def zz8zz_L12_C4_B5_06():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    x_0=random.randint(-5,5) 
    f=expand(a*(x-x_0))
    can =random.choice([1,2])
    if can==1:
        x_1=x_0+random.randint(1,3)
        x_2=x_1+random.randint(1,4)
    else:
        x_2=x_0-random.randint(1,3)
        x_1=x_2-random.randint(1,4)        
   

    kq= integrate(f**2, (x,{x_1},{x_2}))
    kq2=integrate(f**2, (x,{x_1},{x_2+1}))
    kq3=integrate(f**2, (x,{x_1},{x_2}))+random.randint(2,4)
    kq4=integrate(f**2, (x,{x_1},{x_2+random.randint(2,4)}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    kq =f"${{ {latex(my_module.hien_phan_so(kq))}\\pi}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}\\pi}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}\\pi$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho hình phẳng giới hạn bởi đồ thị hàm số $y={latex(f)}$, trục hoành và các đường thẳng $x={x_1},x={x_2}$."\
    f" Tính thể tích khối tròn xoay tạo thành khi cho hình phẳng đó quay quanh trục ${{Ox}}.$"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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

#[D12_C4_B5_07]. Thể tích quay quanh Ox bởi hình: y=ax^2+bx+c,Ox,x=a,x=b
def zz8zz_L12_C4_B5_07():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")      

    a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    x_01=random.randint(-5,5)
    x_02=x_01+random.randint(1,3)
    f=expand(a*(x-x_01)*(x-x_02))
    can =random.choice([1,3])
    if can==1:
        x_1=x_01
        x_2=x_02
    elif can==2:
        x_1=x_02+random.randint(1,4)
        x_2=x_1+random.randint(1,4)
    else:
        x_2=x_01-random.randint(1,4)
        x_1=x_2-random.randint(1,4)    

    kq= integrate(f**2, (x,{x_1},{x_2}))
    kq2=integrate(f**2, (x,{x_1},{x_2+1}))
    kq3=integrate(f**2, (x,{x_1},{x_2}))+random.randint(2,4)
    kq4=integrate(f**2, (x,{x_1},{x_2+random.randint(2,4)}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}\\pi}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}\\pi}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}\\pi$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho hình phẳng giới hạn bởi đồ thị hàm số $y={latex(f)}$, trục hoành và các đường thẳng $x={x_1},x={x_2}$."\
    f" Tính thể tích khối tròn xoay tạo thành khi cho hình phẳng đó quay quanh trục ${{Ox}}.$"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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

#[D12_C4_B5_08]. Thể tích quay quanh Ox bởi hình: y=căn(ax+b),Ox,x=a,x=b
def zz8zz_L12_C4_B5_08():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")    
   
    a = random.choice([random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    x_1=random.randint(int(-b/a)+1,int(-b/a)+5)
    x_2=x_1+random.randint(1,5)
    f=sqrt(a*x+b)        

    kq= integrate(f**2, (x,{x_1},{x_2}))
    kq2=integrate(f**2, (x,{x_1},{x_2+1}))
    kq3=integrate(f**2, (x,{x_1},{x_2}))+random.randint(2,4)
    kq4=integrate(f**2, (x,{x_1},{x_2+random.randint(2,4)}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    kq =f"${{ {latex(my_module.hien_phan_so(kq))}\\pi}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}\\pi}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho hình phẳng giới hạn bởi đồ thị hàm số $y={latex(f)}$, trục hoành và các đường thẳng $x={x_1},x={x_2}$."\
    f" Tính thể tích khối tròn xoay tạo thành khi cho hình phẳng đó quay quanh trục ${{Ox}}.$"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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

#[D12_C4_B5_09]-M3. Thể tích quay quanh Ox bởi hình: y=ae^x+b,Ox,x=a,x=b
def zz8zz_L12_C4_B5_09():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")    
   
    a = random.choice([random.randint(1, 5)])
    b = random.choice([random.randint(1, 3)])
    x_1=random.randint(0,5)
    x_2=x_1+random.randint(1,5)
    f=a*x*exp(b*x)   

    kq= integrate(f**2, (x,{x_1},{x_2}))
    kq2=integrate(f**2, (x,{x_1},{x_2+1}))
    kq3=abs(integrate(f, (x,{x_1},{x_2})))
    kq4=integrate(f**2, (x,{x_1},{x_2+random.randint(2,4)}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    kq =f"${{  \\left({latex(kq)}\\right)\\pi}}$"
    kq2=f"${{  \\left({latex(kq2)}\\right)\\pi}}$"
    kq3=f"${{  \\left({latex(kq3)}\\right)\\pi}}$"
    kq4=f"${{  \\left({latex(kq4)}\\right)\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho hình phẳng giới hạn bởi đồ thị hàm số $y={latex(f)}$, trục hoành và các đường thẳng $x={x_1},x={x_2}$."\
    f" Tính thể tích khối tròn xoay tạo thành khi cho hình phẳng đó quay quanh trục ${{Ox}}.$"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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

#[D12_C4_B5_10]. Thể tích quay quanh Ox bởi hình: y=ax^2+bx+c, Ox
def zz8zz_L12_C4_B5_10():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")      
    a = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    x_1=random.randint(-6,6)
    x_2=x_1+random.randint(1,4)
    f=expand(a*(x-x_1)*(x-x_2))     

    kq= integrate(f**2, (x,{x_1},{x_2}))
    kq2=integrate(f**2, (x,{x_1},{x_2+1}))
    kq3=integrate(f**2, (x,{x_1},{x_2}))+random.randint(2,4)
    kq4=integrate(f**2, (x,{x_1},{x_2+random.randint(2,4)}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}\\pi}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}\\pi}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}\\pi$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Cho hình phẳng giới hạn bởi đồ thị hàm số $y={latex(f)}$, trục hoành và các đường thẳng $x={x_1},x={x_2}$."\
    f" Tính thể tích khối tròn xoay tạo thành khi cho hình phẳng đó quay quanh trục ${{Ox}}.$"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Xét phương trình: ${latex(f)}=0\\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
    f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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

#4.5.3 BÀI TOÁN CHUYỂN ĐỘNG

#[D12_C4_B5_11]-M2. Cho hàm số vận tốc. Tính quãng đường đi được từ t1 đến t2.
def zz8zz_L12_C4_B5_11():   
    d_t=f"\\mathrm{{\\,d}}t"
    m_s=f"\\mathrm{{\\,(m}}/\\mathrm{{\\,s)}}"
    m=f"\\mathrm{{\\,(m)}}"
    t=sp.symbols("t")      
    a = random.randint(1,10)
    b = random.randint(1,10)
    t_1=random.randint(0,8)
    t_2=t_1+random.randint(1,10)

    f=a*t+b 

    kq= integrate(f, (t,{t_1},{t_2}))
    kq2=integrate(f**2, (t,{t_1},{t_2}))
    kq3=integrate(f, (t,{t_1},{t_2}))+random.randint(1,4)
    kq4=abs(f.subs(t,t_2)-f.subs(t,t_1))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}{m}}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}{m}}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}{m}}}$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}{m}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Một vật chuyển động với tốc độ $v(t)={latex(f)} ({m_s})$, với thời gian ${{t}}$ tính bằng giây."\
    f" Tính quãng đường vật đi được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Quãng đường đi được là: $  \\int\\limits_{{{t_1}}}^{{{t_2}}} {{\\left({latex(f)}\\right){d_t}}}=${kq}."    
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

#[D12_C4_B5_12]-M3. Cho hàm số vận tốc. Tính quãng đường đi được từ t1 đến t2.
def zz8zz_L12_C4_B5_12():   
    d_t=f"\\mathrm{{\\,d}}t"
    m_s=f"\\mathrm{{\\,(m}}/\\mathrm{{\\,s)}}"
    m=f"\\mathrm{{\\,(m)}}"
    t=sp.symbols("t")
   
    a = random.randint(2,10)
    v_0=a*random.randint(1,5)

    t_1=0
    t_2=int(v_0/a)

    f=-a*t+v_0

    kq= integrate(f, (t,{t_1},{t_2}))
    kq2=integrate(f**2, (t,{t_1},{t_2}))
    kq3=integrate(f, (t,{t_1},{t_2}))+random.randint(1,4)
    kq4=abs(f.subs(t,t_2)+f.subs(t,t_1))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}{m}}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}{m}}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}{m}}}$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}{m}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Một ô tô đang chạy với tốc độ với tốc độ ${v_0}{m_s}$ thì người lái đạp phanh, từ thời điểm đó ô tô chuyển động chậm dần đều với"\
    f" vận tộc $v(t)={latex(f)}$, trong đó thời gian ${{t}}$ tính bằng giây, kể từ lúc bắt đầu đạp phanh."\
    f" Hỏi từ lúc đạp phanh đến khi dừng hẳn, ô tô còn di chuyển bao nhiêu mét."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thời gian để ô tô dừng hẳn là: $v(t)=0\\Leftrightarrow {latex(f)}=0 \\Leftrightarrow t={int(v_0/a)}$,\n\n"\
    f"Quãng đường đi được là: $  \\int\\limits_{{{t_1}}}^{{{t_2}}} {{\\left({latex(f)}\\right){d_t}}}=${kq}."    
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

#[D12_C4_B5_13]-M3. Xe tăng tốc với gia tốc. Tính quãng đường đi được trong khoảng thời gian
def zz8zz_L12_C4_B5_13():   
    d_t=f"\\mathrm{{\\,d}}t"
    km_h=f"\\mathrm{{\\,(km}}/\\mathrm{{\\,h)}}"
    km_h_2=f"\\mathrm{{\\,(km}}/\\mathrm{{\\,h^2)}}"
    km=f"\\mathrm{{\\,(km)}}"
    t=sp.symbols("t")
   
    a = random.randint(2,10)
    v_0=random.randint(2,10)

    t_1=0
    t_2=random.choice([0.5, 1.5, 2.5, 3.5, random.randint(1,5)])
    str_t_2=str(t_2).replace(".",",")

    f=a*t+v_0
    g=a*t**2/2+v_0*t+v_0

    kq= integrate(g, (t,{t_1},{t_2}))
    kq2=integrate(f, (t,{t_1},{t_2}))
    kq3=integrate(g, (t,{t_1},{t_2}))+random.randint(1,4)
    kq4=integrate(a*t**2/2+v_0*t, (t,{t_1},{t_2}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}{km}}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}{km}}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}{km}}}$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}{km}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)   

    noi_dung=f"Một ô tô đang chạy với tốc độ với tốc độ ${v_0}{km_h}$  thì tăng tốc với gia tốc"\
    f"  $a(t)={latex(f)}{km_h_2}$. Tính quãng đường ô tô đi được trong vòng ${{{str_t_2}}}$ giờ kể từ khi tăng tốc."
 
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Vận tốc của  ô tô dừng hẳn là: $  \\int\\limits {{\\left({latex(f)}\\right){d_t}}}={latex(a*t**2/2)}+{latex(v_0*t)}+C$,\n\n"\
    f"Theo giả thiết ta có: $v(0)={v_0} \\Rightarrow C={v_0}$.\n\n"\
    f"Quãng đường ôtô đi được là: $  \\int\\limits_{{{t_1}}}^{{{str_t_2}}} {{\\left({latex(a*t**2/2)}+{latex(v_0*t)}+{v_0}\\right){d_t}}}=${kq}."    
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

#[D12_C4_B5_14]-M2. Thể tích vật thể có thiết diện là hình chữ nhật.
def zz8zz_L12_C4_B5_14():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")      
    a = random.randint(1,15)
    m = random.randint(1,7)

    f=(m*x*sqrt(a**2-x**2))
    x_1=0
    x_2=a

    kq= integrate(f, (x,{x_1},{x_2}))
    kq2=abs(integrate(f**2, (x,{x_1},{x_2+1})))
    kq3=abs(integrate(f, (x,{x_1},{x_2}))+random.randint(2,4))
    kq4=integrate(f, (x,{x_1},{x_2}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}\\pi$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)


    noi_dung=f"Tính thể tích ${{V}}$ của phần vật thể giới hạn bởi hai mặt phẳng $x={x_1}$ và $x={x_2}$,"\
    f"  biết rằng khi cắt vật thể bởi mặt phẳng tùy ý vuông góc với trục $Ox$ tại điểm có hoành độ $x$ $({x_1}\\le x\\le {x_2})$"\
    f"  thì được thiết diện là một hình chữ nhật có hai cạnh là ${{{latex(m*x)}}}$ và ${latex(sqrt(a**2-x**2))}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right){d_x}}}=${kq}."    
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

#[D12_C4_B5_14]-M2. Thể tích vật thể có thiết diện là hình chữ nhật.
def zz8zz_L12_C4_B5_14():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a = random.randint(1,10)
    m = random.randint(1,7)

    f=(m*x*sqrt(a**2-x**2))
    x_1=0
    x_2=a

    kq= integrate(f, (x,{x_1},{x_2}))
    kq2=abs(integrate(f**2, (x,{x_1},{x_2+1})))
    kq3=abs(integrate(f, (x,{x_1},{x_2}))+random.randint(2,4))
    kq4=integrate(f, (x,{x_1},{x_2}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}\\pi$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}\\pi}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)


    noi_dung=f"Tính thể tích ${{V}}$ của phần vật thể giới hạn bởi hai mặt phẳng $x={x_1}$ và $x={x_2}$,"\
    f"  biết rằng khi cắt vật thể bởi mặt phẳng tùy ý vuông góc với trục ${{Ox}}$ tại điểm có hoành độ $x$ $({x_1}\\le x\\le {x_2})$"\
    f"  thì được thiết diện là một hình chữ nhật có hai cạnh là ${{{latex(m*x)}}}$ và ${latex(sqrt(a**2-x**2))}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right){d_x}}}=${kq}."    
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

#[D12_C4_B5_15]-M2. Thể tích vật thể có thiết diện là hình vuông.
def zz8zz_L12_C4_B5_15():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")      
    a = random.randint(2,10)
    b = random.randint(1,10)
    m = random.randint(1,7)

    f=(x*sqrt(a*x**2-b))

    x_1=int(sqrt(b/a))+random.randint(2,5)
    x_2=x_1 + random.randint(1,5)

    kq= integrate(f**2, (x,{x_1},{x_2}))
    kq2=abs(integrate(f**2, (x,{x_1},{x_2+1})))
    kq3=abs(integrate(f**2, (x,{x_1},{x_2}))+random.randint(2,4))
    kq4=integrate(a*x**3-b*x, (x,{x_1},{x_2}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{ {latex(my_module.hien_phan_so(kq))}}}$"
    kq2=f"${{ {latex(my_module.hien_phan_so(kq2))}}}$"
    kq3=f"${{ {latex(my_module.hien_phan_so(kq3))}}}$"
    kq4=f"${{ {latex(my_module.hien_phan_so(kq4))}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)


    noi_dung=f"Tính thể tích ${{V}}$ của phần vật thể giới hạn bởi hai mặt phẳng $x={x_1}$ và $x={x_2}$,"\
    f"  biết rằng khi cắt vật thể bởi mặt phẳng tùy ý vuông góc với trục ${{Ox}}$ tại điểm có hoành độ $x$ $({x_1}\\le x\\le {x_2})$"\
    f"  thì được thiết diện là một hình vuông có cạnh là ${latex(f)}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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

#[D12_C4_B5_16]-M2. Thể tích vật thể có thiết diện là hình tam giác đều.
def zz8zz_L12_C4_B5_16():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")      
    a = random.randint(1,8)
    b = random.randint(1,8)
    m = random.randint(1,6)

    f=(x*sqrt(a*x**2-b))

    x_1=int(sqrt(b/a))+random.randint(2,5)
    x_2=x_1 + random.randint(1,5)

    kq= integrate(f**2*sqrt(3)/4, (x,{x_1},{x_2}))
    kq2=abs(integrate(f**2*sqrt(3)/2, (x,{x_1},{x_2})))
    kq3=abs(integrate(f**2*sqrt(3), (x,{x_1},{x_2})))
    kq4=integrate(a*x**3-b*x, (x,{x_1},{x_2}))

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq =f"${{  {latex((kq))}}}$"
    kq2=f"${{  {latex((kq2))}}}$"
    kq3=f"${{  {latex((kq3))}}}$"
    kq4=f"${{  {latex((kq4))}}}$"    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)


    noi_dung=f"Tính thể tích ${{V}}$ của phần vật thể giới hạn bởi hai mặt phẳng $x={x_1}$ và $x={x_2}$,"\
    f"  biết rằng khi cắt vật thể bởi mặt phẳng tùy ý vuông góc với trục ${{Ox}}$ tại điểm có hoành độ $x$ $({x_1}\\le x\\le {x_2})$"\
    f"  thì được thiết diện là một hình tam giác đều có cạnh là ${latex(f)}$."
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{{latex(sqrt(3)/4)}\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
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