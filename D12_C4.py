import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
from decimal import Decimal, ROUND_HALF_UP

def thay_log_2_ln(st):
    for i in range(1,100):
        st=st.replace(f"\\log{{\\left({i} \\right)}}",f"\\ln {i}")
    return st

def thay_sin_cos(st):
    st=st.replace(f"\\cos{{\\left(x \\right)}}",f"\\cos x")
    st=st.replace(f"\\sin{{\\left(x \\right)}}",f"\\sin x")
    st=st.replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x")
    st=st.replace(f"\\cot{{\\left(x \\right)}}",f"\\cot x")
    st=st.replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
    st=st.replace(f"\\cot^{{2}}{{\\left(x \\right)}}",f"\\cot^2 x")
    

    for i in range(1,10):
        st=st.replace(f"\\cos{{\\left({i} x \\right)}}",f"\\cos {i}x")
        st=st.replace(f"\\sin{{\\left({i} x \\right)}}",f"\\sin {i}x")
        st=st.replace(f"\\cos^{{2}}{{\\left({i} x \\right)}}",f"\\cos^2 {i}x")
        st=st.replace(f"\\cos^{{2}}{{\\left(x \\right)}}",f"\\cos^2 x")
        st=st.replace(f"\\sin^{{2}}{{\\left({i} x \\right)}}",f"\\sin^2 {i}x")
        st=st.replace(f"\\sin^{{2}}{{\\left(x \\right)}}",f"\\sin^2 x")
        
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

def thay_dau_cong_tru(st):
    st=st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+")
    return st

def tphan(x_1,x_2):
    return f"\\int \\limits_{{{x_1}}}^{{{x_2}}}"

def st_lim(x_0):
    return f"\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}}"


################ Bài 1: NGUYÊN HÀM #################

#[D12_C4_B1_01]. Tìm nguyên hàm của hàm số đa thức
def ckz_L12C4_B1_01():
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
    
         
    debai= f"{noi_dung}"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""
    
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex

    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_02]. Tìm nguyên hàm của hàm số đa thức thỏa mãn điều kiện F(x_0)=b
def ckz_L12C4_B1_02():   
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
    debai= f"{noi_dung}"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_03]. Tìm nguyên hàm của asinx+bcosx
def ckz_L12C4_B1_03():
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

    noi_dung= f"Tìm nguyên hàm $\\int {{({latex(f)}){d_x}}}$."
    noi_dung=noi_dung.replace("\\left(","").replace("\\right)","")

    dap_an=my_module.tra_ve_dap_an(list_PA)     
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_04]. Tìm nguyên hàm của asinu
def ckz_L12C4_B1_04():
   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_05]. Tìm nguyên hàm của acosu
def ckz_L12C4_B1_05():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_06]. Tìm nguyên hàm của hàm số đa thức và 1/x
def ckz_L12C4_B1_06():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_07]. Tìm nguyên hàm của m/(ax+b)
def ckz_L12C4_B1_07():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_08]. Tìm nguyên hàm của mx+n/(ax+b)
def ckz_L12C4_B1_08():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_09]. Tìm nguyên hàm của (mx^2+nx+p)/(ax+b)
def ckz_L12C4_B1_09():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_10]. Tìm nguyên hàm của e^(ax+b)
def ckz_L12C4_B1_10():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
       
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B1_11]-M1. Tìm nguyên hàm của ax+b
def ckz_L12C4_B1_11():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_12():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_13():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_14():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 4) if i!=0])
    b = random.choice([i for i in range(-5, 4) if i!=0])
    noi_dung=(
    f"Tìm nguyên hàm $\\int {{{latex((a*x+b)**2)}}} dx$."
    )
    
    f=(a*x+b)**2
    kq=f"${latex(integrate(f,x))}+C$"
    kq_false=[
    f"${latex(a*x**3+a*b*x**2+b**2)}+C$",
    f"${latex(a**2*x**3+a*x**2/2+b**2*x)}+C$",
    f"${latex(a**2*x**3/3+a*b*x**2/2)}+C$",
    f"${latex(a*x**2+2*a*b*x+b**2)}+C$"
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_15():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_16():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_17():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    while True:
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
        if -5<G.subs(x,x_1)<500:
            break


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
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_18]-SA-M2. Tìm nguyên hàm của a+b/x^2 thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_18():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    while True:
    
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
        if -5<G.subs(x,x_1)<100:
            break

    dap_an=f"{round_half_up(G.subs(x,x_1),1):.1f}".replace(".",",")

    noi_dung = (
    f"Biết $F(x)$ là một nguyên hàm của hàm số $ f(x)={latex(f)}$ thỏa mãn $F({x_0}) ={b}$. Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {phan_so(F.subs(x,x_0))}+C={b}\\Rightarrow C={phan_so(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={phan_so(G.subs(x,x_1))}={dap_an}$."    
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_19]-SA-M2. Tìm nguyên hàm của ax+b/x^2 thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_19():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    
    while True:
        pass
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
        t=random.randint(10,15)
        kq=G.subs(x,x_1)/t
        if 0<kq<100:
            break    

    
    dap_an=f"{round_half_up((G.subs(x,x_1))/t):.1f}".replace(".",",")

    noi_dung = (
    f"Biết $F(x)$ là một nguyên hàm của hàm số $ f(x)={latex(f)}$ thỏa mãn $F({x_0}) ={b}$. Tính $\\dfrac{{F({x_1})}}{{{t}}}$ (kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {phan_so(F.subs(x,x_0))}+C={b}\\Rightarrow C={phan_so(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={phan_so(G.subs(x,x_1))}$." 
    f"$\\dfrac{{F({x_1})}}{{{t}}}={dap_an}$" 
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_20]-SA-M2. Tìm nguyên hàm của ax+b+c/x^2 thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_20():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"   

    while True:
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

        if -5<G.subs(x,x_1)<100:
            break

    dap_an=f"{round_half_up(G.subs(x,x_1)):.1f}".replace(".",",")

    noi_dung = (
    f"Biết $F(x)$ là một nguyên hàm của hàm số $ f(x)={latex(f)}$ thỏa mãn $F({x_0}) ={b}$. Tính $F({x_1})$ (kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {phan_so(F.subs(x,x_0))}+C={b}\\Rightarrow C={phan_so(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n"
    f"$F({x_1})={phan_so(G.subs(x,x_1))}={dap_an}$."    
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_21]-M2. Tìm nguyên hàm của m/cos^2x
def ckz_L12C4_B1_21():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_22():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_23():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_24():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_25():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_26():
    x=sp.symbols("x")

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}"

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}"\
        f"\\choiceTFt\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B1_27]-M1. Nguyên hàm của a^x
def ckz_L12C4_B1_27():
    a=random.choice([random.randint(2,15),pi])
    noi_dung=(
    f"Tìm nguyên hàm $\\int {{{latex(a)}^x}}dx$."
    )
    

    kq=f"$\\dfrac{{{latex(a)}^x}}{{\\ln {latex(a)}}}+C$"
    kq_false=[
    f"$\\dfrac{{{latex(a)}^x}}{{{latex(a)}}}+C$",
    f"${latex(a)}^x\\ln {latex(a)}+C$",
    f"$x^{{{latex(a)}}}\\ln {latex(a)}+C$",
    f"$\\dfrac{{x^{{{latex(a)}}} }}{{\\ln {latex(a)}}}+C$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$\\int {{{latex(a)}^x}}dx=\\dfrac{{{latex(a)}^x}}{{\\ln {latex(a)}}}+C$."
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_28():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_29():
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
    f"$({latex(a*x+b)}).e^x+C$",]
    if a==-1:
        kq_false=[
    f"$e^{{{latex(a*x+b)}}}+C$",
    f"$e^{{{latex(a*x+b+random.randint(1,2))}}}+C$",
    f"$({latex(a*x+b)}).e^{{{latex(a*x)}}}+C$",]
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_30():
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

    debai= f"{noi_dung}".replace("+-","-")

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_31():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_32():
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_33():
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

    kq=f"$F(x)={latex(G)}$"
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_34():
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

    kq=f"$F(x)={latex(G)}$"
    kq_false=[
    f"$F(x)={latex(1/m*e**x-1/n*e**(-x)+C)}$",
    f"$F(x)={latex(m*e**(-x)+n*x+C)}$",
    f"$F(x)={latex(m*e**x-n*e**(-x)+C+random.randint(1,3))}$"]
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

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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
def ckz_L12C4_B1_35():
    d_x=f"\\mathrm{{\\,d}}x"
    x,e=sp.symbols("x,e")

    while True:
        m = random.choice([i for i in range(-4, 4) if i!=0])
        n = random.choice([i for i in range(-3, 3) if i!=0])   
        
        F=m*exp(x)+n*x
        x_0= random.choice([random.randint(-3, 3)])    
        b= random.randint(-6, 6)
        C=b-F.subs(x,x_0)
        G=F+C
        x_1=random.choice([i for i in range(-3,3) if i!=x_0])
        if G.subs(x,x_1)>-9 and G.subs(x,x_1)<600:
            break
    f=diff(F,x)

    
   

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

        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_36]-SA-M3. F(x) là một nguyên hàm của m.e^x + ne^(-x)  thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_36():
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

        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_37]-SA-M3. F(x) là một nguyên hàm của m.e^x + ne^(-x)+p thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_37():
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
        if G.subs(x,x_1)>-9 and G.subs(x,x_1)<500:
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

        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an


#[D12_C4_B1_38]-SA-M3. F(x) là một nguyên hàm của m.a^x+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_38():
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
        if G.subs(x,x_1)>50 and G.subs(x,x_1)<600:
            break
    f=diff(F,x)
    t=random.randint(10,20)
    dap_an=f"{round_half_up(G.subs(x,x_1)/t,1):.1f}".replace(".",",")


    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}$.\n\n"
    f"$\\dfrac{{F({x_1})}}{{{t}}}={dap_an}$."     
    )  

    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $\\dfrac{{F({x_1})}}{{{t}}}$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_log_2_ln(noi_dung)
    noi_dung_loigiai=thay_log_2_ln(noi_dung_loigiai)

        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_39]-SA-M3. F(x) là một nguyên hàm của m.a^x+n.e^x thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_39():
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
        if G.subs(x,x_1)>50 and G.subs(x,x_1)<600:
            break
    f=diff(F,x)

    t=random.randint(10,20)
    
    dap_an=f"{round_half_up(G.subs(x,x_1)/t,1):.1f}".replace(".",",")
    
    noi_dung_loigiai=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}$.\n\n"
    f"$\\Rightarrow \\dfrac{{F({x_1})}}{{{t}}}={dap_an}$." 
    )  

    
    noi_dung=(
    f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Tính $\\dfrac{{F({x_1})}}{{{t}}}$ (kết quả làm tròn đến hàng phần mười)."
    ) 
    noi_dung=thay_log_2_ln(noi_dung)
    noi_dung_loigiai=thay_log_2_ln(noi_dung_loigiai)


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_40]-SA-M3. F(x) là một nguyên hàm của m.sin(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_40():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_41]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_41():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_42]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n hoặc m.sin(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_42():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_43]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n.sin(x) thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_43():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_44]-SA-M3. F(x) là một nguyên hàm của m.cos(x)+n.sin(x)+p thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_44():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_45]-SA-M3. F(x) là một nguyên hàm của mtan^2(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_45():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_46]-SA-M3. F(x) là một nguyên hàm của mcot^2(x)+n thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_46():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_47]-SA-M3. F(x) là một nguyên hàm của mtan^2+ncot^2(x) thỏa mãn F(x_0)=y_0. Tính F(x_1)
def ckz_L12C4_B1_47():
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


        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B1_48]-TF-M3. Xét Đ-S: nguyên hàm của asinx, acosx+b, atan^2x, Tính F(x_0) theo nguyên hàm sin,cos
def ckz_L12C4_B1_48():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"    

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười):"  
 
    chon=random.randint(1,2)
    a=random.randint(2,10)
    if chon==1:
        kq1_T=f"* $\\int {latex(a*sin(x))}{d_x}={latex(-a*cos(x))}+C$" 
        kq1_F=f"$\\int {latex(a*sin(x))}{d_x}={latex(a*cos(x))}+C$"
        kq1=random.choice([kq1_T, kq1_F])
        kq1=thay_sin_cos(kq1)
        HDG=f"$\\int {latex(a*sin(x))}={latex(-a*cos(x))}+C$."
        HDG=thay_sin_cos(HDG)
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        kq1_T=f"* $\\int {latex(a*cos(x))}{d_x}={latex(a*sin(x))}+C$" 
        kq1_F=f"$\\int {latex(a*cos(x))}{d_x}={latex(-a*sin(x))}+C$"
        kq1=random.choice([kq1_T, kq1_F])
        kq1=thay_sin_cos(kq1)
        HDG=f"$\\int {latex(a*cos(x))}{d_x}={latex(a*sin(x))}+C$."
        HDG=thay_sin_cos(HDG)
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    f=a*sin(x)+b*cos(x)   
    

    kq2_T=f"* $\\int {{\\left({latex(f)}\\right){d_x}}}={latex(integrate(f, x))}+C$"
    kq2_F=f"$\\int {{\\left({latex(f)}\\right){d_x}}}={latex(diff(f, x))}+C$"
    kq2=random.choice([kq2_T, kq2_F])
    kq2=thay_sin_cos(kq2)

    HDG=f"$\\int {{\\left({latex(f)}\\right){d_x}}}={latex(integrate(f, x))}+C$"
    HDG=thay_sin_cos(HDG)
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.choice([i for i in range(-5, 5) if i!=0])
    n = random.choice([i for i in range(-5, 5) if i!=0])     
    F=m*tan(x)+n*x
    f=diff(F,x)

    kq3_T=f"* $\\int ({latex(f)}){d_x}={latex(F)}+C$" 
    kq3_F=f"$\\int ({latex(f)}){d_x}={latex(F+random.randint(1,2)*x)}+C$"
    kq3=random.choice([kq3_T, kq3_F])
    kq3=thay_sin_cos(kq3)
    HDG=f"$\\int ({latex(f)}){d_x}={latex(F)}+C$."
    HDG=thay_sin_cos(HDG)
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

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
    dap_an_false=f"{round_half_up(G.subs(x,x_1)+random.randint(1,2),1):.1f}".replace(".",",")
   
    kq4_T=f"* Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$. Khi đó $F({latex(x_1)})={dap_an}$"
    kq4_F=f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$. Khi đó $F({latex(x_1)})={dap_an_false}$" 
    kq4=random.choice([kq4_T, kq4_F])
    kq4=thay_sin_cos(kq4)
    HDG=(f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$.")
    HDG=thay_sin_cos(HDG)
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}"\
        f"\\choiceTFt\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B1_49]-TF-M3. Xét Đ-S: nguyên hàm của asinx, acosx+b, acot^2x, Tính F(x_0) theo nguyên hàm sin,cos
def ckz_L12C4_B1_49():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"    

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười):"  
 
    chon=random.randint(1,2)
    a=random.randint(2,10)
    if chon==1:
        kq1_T=f"* $\\int {latex(a*sin(x))}{d_x}={latex(-a*cos(x))}+C$" 
        kq1_F=f"$\\int {latex(a*sin(x))}{d_x}={latex(a*cos(x))}+C$"
        kq1=random.choice([kq1_T, kq1_F])
        kq1=thay_sin_cos(kq1)
        HDG=f"$\\int {latex(a*sin(x))}{d_x}={latex(-a*cos(x))}+C$."
        HDG=thay_sin_cos(HDG)
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        kq1_T=f"* $\\int {latex(a*cos(x))}{d_x}={latex(a*sin(x))}+C$" 
        kq1_F=f"$\\int {latex(a*cos(x))}{d_x}={latex(-a*sin(x))}+C$"
        kq1=random.choice([kq1_T, kq1_F])
        kq1=thay_sin_cos(kq1)
        HDG=f"$\\int {latex(a*cos(x))}={latex(a*sin(x))}+C$."
        HDG=thay_sin_cos(HDG)
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    f=a*sin(x)+b*cos(x)   
    

    kq2_T=f"* $\\int {{\\left({latex(f)}\\right){d_x}}}={latex(integrate(f, x))}+C$"
    kq2_F=f"$\\int {{\\left({latex(f)}\\right){d_x}}}={latex(diff(f, x))}+C$"
    kq2=random.choice([kq2_T, kq2_F])
    kq2=thay_sin_cos(kq2)

    HDG=f"$\\int {{\\left({latex(f)}\\right){d_x}}}={latex(integrate(f, x))}+C$"
    HDG=thay_sin_cos(HDG)
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.choice([i for i in range(-5, 5) if i!=0])
    n = random.choice([i for i in range(-5, 5) if i!=0])     
    F=m*cot(x)+n*x
    f=diff(F,x)

    kq3_T=f"* $\\int ({latex(f)}){d_x}={latex(F)}+C$" 
    kq3_F=f"$\\int ({latex(f)}){d_x}={latex(F+random.randint(1,2)*x)}+C$"
    kq3=random.choice([kq3_T, kq3_F])
    kq3=thay_sin_cos(kq3)
    HDG=f"$\\int ({latex(f)}){d_x}={latex(F)}+C$."
    HDG=thay_sin_cos(HDG)
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

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
    dap_an_false=f"{round_half_up(G.subs(x,x_1)+random.randint(1,2),1):.1f}".replace(".",",")
   
    kq4_T=f"* Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$. Khi đó $F({latex(x_1)})={dap_an}$"
    kq4_F=f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$. Khi đó $F({latex(x_1)})={dap_an_false}$" 
    kq4=random.choice([kq4_T, kq4_F])
    kq4=thay_sin_cos(kq4)
    HDG=(f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$.")
    HDG=thay_sin_cos(HDG)
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}"\
        f"\\choiceTFt\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B1_50]-TF-M3. Xét Đ-S: nguyên hàm của asinx, acosx+b, sinmx+n, Tính F(x_0) theo nguyên hàm tan,cot
def ckz_L12C4_B1_50():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"    

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười):"  
 
    chon=random.randint(1,2)
    a=random.randint(2,10)
    if chon==1:
        kq1_T=f"* $\\int {latex(a*sin(x))}{d_x}={latex(-a*cos(x))}+C$" 
        kq1_F=f"$\\int {latex(a*sin(x))}{d_x}={latex(a*cos(x))}+C$"
        kq1=random.choice([kq1_T, kq1_F])
        kq1=thay_sin_cos(kq1)
        HDG=f"$\\int {latex(a*sin(x))}{d_x}={latex(-a*cos(x))}+C$."
        HDG=thay_sin_cos(HDG)
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        kq1_T=f"* $\\int {latex(a*cos(x))}{d_x}={latex(a*sin(x))}+C$" 
        kq1_F=f"$\\int {latex(a*cos(x))}{d_x}={latex(-a*sin(x))}+C$"
        kq1=random.choice([kq1_T, kq1_F])
        kq1=thay_sin_cos(kq1)
        HDG=f"$\\int {latex(a*cos(x))}{d_x}={latex(a*sin(x))}+C$."
        HDG=thay_sin_cos(HDG)
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    f=a*sin(x)+b*cos(x)   
    

    kq2_T=f"* $\\int {{\\left({latex(f)}\\right){d_x}}}={latex(integrate(f, x))}+C$"
    kq2_F=f"$\\int {{\\left({latex(f)}\\right){d_x}}}={latex(diff(f, x))}+C$"
    kq2=random.choice([kq2_T, kq2_F])
    kq2=thay_sin_cos(kq2)

    HDG=f"$\\int {{\\left({latex(f)}\\right){d_x}}}={latex(integrate(f, x))}+C$"
    HDG=thay_sin_cos(HDG)
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.choice([i for i in range(-5, 5) if i!=0])
    n = random.choice([i for i in range(-5, 5) if i!=0])
    a=random.randint(2,9)
    chon=random.randint(1,2)
    if chon==1:
        F=m*sin(a*x)+n*x    
    if chon==2:
        F=m*cos(a*x)+n*x
    
    
    f=diff(F,x)

    kq3_T=f"* $\\int ({latex(f)}){d_x}={latex(F)}+C$" 
    kq3_F=f"$\\int ({latex(f)}){d_x}={latex(F+random.randint(1,2)*x)}+C$"
    kq3=random.choice([kq3_T, kq3_F])
    kq3=thay_sin_cos(kq3)
    HDG=f"$\\int ({latex(f)}){d_x}={latex(F)}+C$."
    HDG=thay_sin_cos(HDG)
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

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
    dap_an_false=f"{round_half_up(G.subs(x,x_1)+random.randint(1,2),1):.1f}".replace(".",",")

    
    kq4_T=f"* Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$. Khi đó $F({latex(x_1)})={dap_an}$"
    kq4_F=f"Biết $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({latex(x_0)})={b}$. Khi đó $F({latex(x_1)})={dap_an_false}$" 
    kq4=random.choice([kq4_T, kq4_F])
    kq4=thay_sin_cos(kq4)
    HDG=(
    f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({latex(x_0)})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({latex(x_1)})={latex(G.subs(x,x_1))}={dap_an}$."     
    ) 
    HDG=thay_sin_cos(HDG)
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}"\
        f"\\choiceTFt\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B1_51]-TF-M3. Xét Đ-S: nguyên hàm của: a^x, e^mx, m.e^x+n.e^(-x), Tính F(x_0) từ nguyên hàm a^x
def ckz_L12C4_B1_51():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười):"        
    debai_word= f"{noi_dung}"

    a=random.randint(2,9)

    kq1_T=f"* $\\int {{{a}^x}}{d_x}=\\dfrac{{{latex(a)}^x}}{{\\ln {a}}}+C$" 
    kq1_F=random.choice([
        f"$\\int {{{a}^x}}{d_x}={a}^x+C$",
        f"$\\int {{{a}^x}}{d_x}={a}^x.\\ln {a}+C$"])
    
    HDG=f"$\\int {{{a}^x}}{d_x}=\\dfrac{{{latex(a)}^x}}{{\\ln {a}}}+C$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m=random.randint(2,9)

    kq2_T=f"* $\\int e^{{{a}x}}{d_x}=\\dfrac{{1}}{{{a}}}e^{{{a}x}}+C$"
    kq2_F=f"$\\int e^{{{a}x}}{d_x}={a}e^{{{a}x}}+C$"
    
    HDG=f"$\\int e^{{{a}x}}{d_x}=\\dfrac{{1}}{{{a}}}e^{{{a}x}}+C$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])

    p = random.choice([i for i in range(-4, 4) if i!=0])
    e,x=sp.symbols("e x")
    f=m*e**x+n*e**(-x)

    kq3_T=f"* $\\int ({latex(f)}){d_x}={latex(m*e**x-n*e**(-x))}+C$" 
    kq3_F=random.choice([
        f"$\\int ({latex(f)}){d_x}={latex(m*e**x+n*e**(-x))}+C$",
        f"$\\int ({latex(f)}){d_x}={latex(-m*e**x+n*e**(-x))}+C$"])
    
    HDG=f"$\\int ({latex(f)}){d_x}={latex(m*e**x-n*e**(-x))}+C$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

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
    dap_an_false=f"{round_half_up(G.subs(x,x_1)+random.randint(1,2),1):.1f}".replace(".",",") 


    kq4_T=( f"* $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Khi đó $F({x_1})={dap_an}$")
    kq4_F=( f"$F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Khi đó $F({x_1})={dap_an_false}$")
    
    HDG=thay_log_2_ln(f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}={dap_an}$.")
    kq4=thay_log_2_ln(random.choice([kq4_T, kq4_F]))
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
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

    debai_latex= (f"\\begin{{ex}}\n {noi_dung}"
        f"\\choiceTFt\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {loigiai_latex} \n }}"
        f"\\end{{ex}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B1_52]-TF-M3. Xét Đ-S: nguyên hàm của: me^x, a^mx, a^x.b^x.c^x, Tính F(x_0) từ nguyên hàm e^x+e^(-x)
def ckz_L12C4_B1_52():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười):"        
    debai_word= f"{noi_dung}"

    a=random.randint(2,9)

    kq1_T=f"* $\\int {{{a}e^x}}{d_x}={a}e^x+C$" 
    kq1_F=f"$\\int {{{a}e^x}}{d_x}=e^{{{a}x}}+C$"
    
    HDG=f"$\\int {{{a}e^x}}{d_x}={a}e^x+C$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    
    a=random.randint(2,9)
    m=random.randint(2,4)

    kq2_T=f"* $\\int {a}^{{{m}x}}{d_x}=\\dfrac{{{a**m}^x }}{{\\ln {a**m} }}+C$"
    kq2_F=f"$\\int {a}^{{{m}x}}{d_x}=\\dfrac{{{a}^x }}{{\\ln {a*m} }}+C$"
    
    HDG=f"$\\int {a}^{{{m}x}}{d_x}=\\int {a**m}^x{d_x}=\\dfrac{{{a**m}^x }}{{\\ln {a**m} }}+C$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a=random.randint(2,4)
    b=a+random.randint(1,3)
    c=b+random.randint(1,3)

    kq3_T=f"* $\\int {a}^x.{b}^x.{c}^x{d_x}=\\dfrac{{{a*b*c}^x}}{{\\ln {a*b*c}}}+C$" 
    kq3_F=f"$\\int {a}^x.{b}^x.{c}^x{d_x}={a*b*c}^x\\ln {a*b*c}+C$"
    
    HDG=f"$\\int {a}^x.{b}^x.{c}^x{d_x}=\\int {a*b*c}^x{d_x}=\\dfrac{{{a*b*c}^x}}{{\\ln {a*b*c}}}+C$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

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
    dap_an_false=f"{round_half_up(G.subs(x,x_1)+random.randint(1,2),1):.1f}".replace(".",",") 

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
    dap_an_false=f"{round_half_up(G.subs(x,x_1)+random.randint(1,2),1):.1f}".replace(".",",")


    kq4_T=( f"* $F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Khi đó $F({x_1})={dap_an}$")
    kq4_F=( f"$F(x)$ là một nguyên hàm của hàm số $f(x)={latex(f)}$ thỏa mãn $F({x_0})={b}$."
    f" Khi đó $F({x_1})={dap_an_false}$")
    
    HDG=thay_log_2_ln(f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(F)}+C$.\n\n"
    f"$F({x_0})={b}\\Leftrightarrow {latex(F.subs(x,x_0))}+C={b}\\Rightarrow C={latex(C)}$.\n\n"
    f"Vậy $F(x)={latex(F+C)}$.\n\n" 
    f"$F({x_1})={latex(G.subs(x,x_1))}={dap_an}$." )
    kq4=thay_log_2_ln(random.choice([kq4_T, kq4_F]))
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
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

    debai_latex= (f"\\begin{{ex}}\n {noi_dung}"
        f"\\choiceTFt\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {loigiai_latex} \n }}"
        f"\\end{{ex}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B1_53]-TF-M3. Xét Đ-S: T.c nguyên hàm, công thức vận tốc-gia tốc, tìm nguyên hàm biết F(x_0), bài toán quãng đường
def ckz_L12C4_B1_53():
    x=sp.symbols("x")    
    d_x=f"\\mathrm{{\\,d}}x"

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười)."        
    debai_word= f"{noi_dung}\n"

    ten=["f(x)", "g(x)", "h(x)"]
    f,g,h=random.sample(ten,3)

    m = random.choice([i for i in range(-5, 5) if i!=0])
    n = random.choice([i for i in range(-5, 5) if i!=0])
    
    kq1_T=random.choice([
        f"* $\\int ({f}+{g}){d_x}= \\int {f}{d_x} + \\int {g}{d_x}$",
        f"* $\\int ({f}-{g}){d_x}= \\int {f}{d_x} - \\int {g}{d_x}$",
        f"* $\\int ({m}{f}+{n}{g}){d_x}= {m}\\int {f}{d_x} + {n}\\int {g}{d_x}$",
        f"* $\\int {m}{f}{d_x}= {m}\\int {f}{d_x}$",
        f"* $\\int f'(x){d_x}= f(x)+C$",
        f"* $\\int g'(x){d_x}= g(x)+C$",
        f"* $\\int h'(x){d_x}= h(x)+C$",
        f"* $\\int x^n {d_x} = \\dfrac{{x^{{n+1}} }}{{n+1}}+C$, với $n\\ne -1$",
        f"* $\\int a^x {d_x}= \\dfrac{{a^x}}{{\\ln a}}+C$, với $a>0,a\\ne 1$",
        f"* $\\int \\dfrac{{1}}{{x}} {d_x}=\\ln |x|+C$",
        f"* $\\int e^x {d_x}=e^x+C$",
        f"* $\\int k {d_x}=kx+C$",
        f"* $\\int \\sin x {d_x}=-\\cos x+C$",
        f"* $\\int \\cos x {d_x}=\\sin x+C$",
        f"* $\\int \\dfrac{{1}}{{\\cos^2 x}} {d_x}=\\tan x+C$",
        f"* $\\int \\dfrac{{1}}{{\\sin^2 x}} {d_x}=-\\cot x+C$",
        f"* $\\int (1+\\tan^2 x) {d_x}=\\tan x+C$",
        f"* $\\int (1+\\cot^2 x) {d_x}=-\\cot x+C$",
        ])
    kq1_F=random.choice([
        f"$\\int ({f}.{g}){d_x}= \\int {f}{d_x}.\\int {g}{d_x}$",
        f"$\\int (\\dfrac{{{f}}}{{{g}}}){d_x}= \\dfrac{{\\int {f}{d_x}}}{{\\int {g}{d_x}}}$",
        f"$\\int ({f}+{m}){d_x}= \\int {f}{d_x}+{m}$",
        f"$\\int x^n {d_x} = \\dfrac{{x^{{n-1}} }}{{n-1}}+C$, với $n\\ne 1$",
        f"$\\int a^x {d_x}= a^x\\ln a+C$",
        f"$\\int \\dfrac{{1}}{{x}} {d_x}=\\ln x+C$",
        f"$\\int k {d_x}=C$",
        f"$\\int e^x {d_x}=e^{{-x}}+C$",
        f"$\\int \\sin x {d_x}=\\cos x+C$",
        f"$\\int \\cos x {d_x}=-\\sin x+C$",
        f"$\\int \\tan x {d_x}=\\cot x+C$",
        f"$\\int \\cot x {d_x}=-\\tan x+C$",
        ])
    
    HDG=f" "
    kq1=random.choice([kq1_T, kq1_F])
    kq1=kq1.replace("+-","-")
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        kq2_T=(f"* Một vật chuyển động với gia tốc $a(t)$ với ${{t}}$ là thời gian tính bằng giây."
            f" Vận tốc chuyển động của vật được xác định bởi $v(t)=\\int a(t)dt$")
        kq2_F=(f"Một vật chuyển động với vận tốc $v(t)$ với ${{t}}$ là thời gian tính bằng giây."
            f" Gia tốc chuyển động của vật được xác định bởi $a(t)=\\int v(t)dt$")
    
    if chon==2:
        kq2_T=(f"Một vật chuyển động với vận tốc $s(t)$ với ${{t}}$ là thời gian tính bằng giây."
            f" Quãng chuyển động của vật được xác định bởi $s(t)=\\int v(t)dt$")
        kq2_F=(f"Một vật chuyển động với vận tốc $v(t)$ với ${{t}}$ là thời gian tính bằng giây."
            f" Gia tốc chuyển động của vật được xác định bởi $a(t)=\\int v(t)dt$") 
    
    HDG=f""
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        while True:
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
            if -5<G.subs(x,x_1)<500:
                break

        dap_an=G.subs(x,x_1)

        kq3_T=f"* Biết $F(x)$ là một nguyên hàm của hàm số $ f(x)={latex(f)}$ thỏa mãn $F({x_0}) ={b}$. Khi đó $F({x_1})={dap_an}$"
        kq3_F=f"Biết $F(x)$ là một nguyên hàm của hàm số $ f(x)={latex(f)}$ thỏa mãn $F({x_0}) ={b}$. Khi đó $F({x_1})={dap_an+random.randint(1,5)}$"
        
        HDG=(f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
        f"$F({x_0})={b}\\Leftrightarrow {F.subs(x,x_0)}+C={b}\\Rightarrow C={C}$.\n\n"
        f"Vậy $F(x)={latex(F+C)}$.\n\n"
        f"$F({x_1})={dap_an}$." )
    
    if chon==2:
        while True:
        
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
            if -5<G.subs(x,x_1)<100:
                break

        dap_an=phan_so(G.subs(x,x_1))
        dap_an_false=phan_so(G.subs(x,x_1)+random.randint(1,2))

        kq3_T = (f"* Biết $F(x)$ là một nguyên hàm của hàm số $ f(x)={latex(f)}$ thỏa mãn $F({x_0}) ={b}$."
            f" Khi đó $F({x_1})={dap_an}$")
        kq3_F = (f"Biết $F(x)$ là một nguyên hàm của hàm số $ f(x)={latex(f)}$ thỏa mãn $F({x_0}) ={b}$."
            f" Khi đó $F({x_1})={dap_an_false}$")       

        noi_dung_loigiai=(
        f"$F(x)=\\int \\left({{{latex(f)}}}\\right){d_x}={latex(integrate(f, x))}+C$.\n\n"
        f"$F({x_0})={b}\\Leftrightarrow {phan_so(F.subs(x,x_0))}+C={b}\\Rightarrow C={phan_so(C)}$.\n\n"
        f"Vậy $F(x)={latex(F+C)}$.\n\n"
        f"$F({x_1})={phan_so(G.subs(x,x_1))}={dap_an}$." )    
    
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    t=sp.symbols("t")
    
    while True:
        v_0=random.randint(12,20)
        a=v_0-random.randint(1,3)
        b=random.randint(2,7)
        v=a-b*t
        t_0=random.randint(1,5)
        s=integrate(v,(t,0,t_0))
        if s>0:
            break
    s_false=s+random.randint(1,2)
    if int(s_false)!=s_false:
        s_false=f"{round_half_up(s_false,1):.1f}".replace(".",",")
    if int(s)!=s:
        s=f"{round_half_up(s,1):.1f}".replace(".",",")  

    kq4_T=(f"* Một chiếc ôtô đang chuyển động với vận tốc ${{{v_0}}}$ m/s thì hãm phanh và chuyển động chậm dần với vận tốc "
f"$v(t)={latex(v)}$ (m/s). Kể từ khi hãm phanh, quãng đường đi được của ôtô sau ${{{t_0}}}$ giây là ${{{s}}}$ m"
        )

    kq4_F=(f"Một chiếc ôtô đang chuyển động với vận tốc ${{{v_0}}}$ m/s thì hãm phanh và chuyển động chậm dần với vận tốc "
f"$v(t)={latex(v)}$ (m/s). Kể từ khi hãm phanh, quãng đường đi được của ôtô sau ${{{t_0}}}$ giây là ${{{s}}}$ m") 
    
    HDG=(f"$s=\\int v(t)dt=\\int ({latex(v)})dt={latex(integrate(v,t))}+C$.\n\n"
        f"$s(0)=0\\Rightarrow C=0$.\n\n"
        f"Quãng đường đi được của ôtô sau ${{{t_0}}}$ giây là: $s({t_0})={s}$ (m).")
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

#[D12_C4_B1_54]-M2. Tìm khẳng định đúng về tính chất nguyên hàm
def ckz_L12C4_B1_54():
    d_x=f"\\mathrm{{\\,d}}x"
    noi_dung=(
    f"Khẳng định nào sau đây là khẳng định đúng?")   

    kq=random.choice([
        f"$\\int {d_x}=x+C$",
        f"$\\int k{d_x}=kx+C, k \\in \\mathbb{{R}}$",
        f"$\\int x^{{\\alpha}}{d_x}=\\dfrac{{x^{{\\alpha+1}}}}{{\\alpha+1}}$ với $\\alpha \\ne -1$",
        f"$\\int \\dfrac{{1}}{{x}}=\\ln |x|+C$ với $x\\ne 0$",
        f"$\\int f'(x){d_x}=f(x)+C$",
        f"$\\int kf(x){d_x}=k\\int f(x){d_x},(k\\in  \\mathbb{{R}}, k\\ne 0)$",
        f"$\\int {{[f(x)+g(x)]}}{d_x}=\\int f(x){d_x}+\\int g(x){d_x}$",
        f"$\\int {{[f(x)-g(x)]}}{d_x}=\\int f(x){d_x}-\\int g(x){d_x}$",
        f"$\\int {{[g(x)-f(x)]}}{d_x}=\\int g(x){d_x}-\\int f(x){d_x}$",
        f"Nếu $F(x)$ và $G(x)$ đều là nguyên hàm của hàm số $f(x)$ thì tồn tại số ${{C}}$ sao cho$F(x)=G(x)+C$",])
    kq_false=[
    f"$\\int 0{d_x}=x+C$",
    f"$\\int x^{{\\alpha}}{d_x}=\\dfrac{{x^{{\\alpha+1}}}}{{\\alpha+1}}$",
    f"$\\int \\dfrac{{1}}{{x}}=\\ln x+C$",
    f"Nếu $F(x)$ và $G(x)$ đều là nguyên hàm của hàm số $f(x)$ thì $F(x)=G(x)$",
    f"$\\int f(x){d_x}=f'(x)+C$",
    f"$\\int {{[f(x).g(x)]}}{d_x}= \\int f(x){d_x}. \\int g(x) {d_x}$",
    f"$\\int \\dfrac{{f(x)}}{{g(x)}}{d_x}=\\dfrac{{\\int f(x){d_x}}}{{\\int g(x) {d_x}}}$",    
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

    debai= f"{noi_dung}"

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



#------------------------------------------------------------->
#BÀI 2- NGUYÊN HÀM ĐỔI BIẾN
#[D12_C4_B2_01]. Nguyên hàm đổi biến chứa căn(ax+b)
def ckz_L12C4_B2_01():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D12_C4_B2_02]. Nguyên hàm đổi biến chứa căn(ax^2+b)
def ckz_L12C4_B2_02():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B2_03]. Nguyên hàm đổi biến sinx/căn(acosx+b){d_x}
def ckz_L12C4_B2_03():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B2_04]. Nguyên hàm đổi biến (acosx+b)sinx
def ckz_L12C4_B2_04():
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B2_05]. Nguyên hàm đổi biến (lnx)^n/x
def ckz_L12C4_B2_05():
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

    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#BÀI 3- NGUYÊN HÀM TỪNG PHẦN
#[D12_C4_B3_01]. Nguyên hàm P(x).sin hoặc P(x).cos
def ckz_L12C4_B3_01():
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

    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B3_02]. Nguyên hàm P(x).e^(ax+b) 
def ckz_L12C4_B3_02():
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

    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B3_03]. Nguyên hàm P(x).ln(mx)
def ckz_L12C4_B3_03():
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

    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    noi_dung_loigiai=f""    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

################ Bài 4: TÍCH PHÂN #################
#[D12_C4_B4_01]-M1. Cho F(a) và F(b). Tính tích phân từ a đến b.
def ckz_L12C4_B4_01():   
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

    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_02]-M1. Cho 2 tích phân theo f và g. Tính tích phân (m.f+n.g).
def ckz_L12C4_B4_02():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    tich_mf=show_tich(m,giatri_f1)
    tich_ng=show_tich(n,giatri_f2)
    noi_dung_loigiai=f"${f3}={m}{f1}{dau_n}{n1}{f2}={tich_mf}{dau_n}{tich_ng}={kq}$ ."    
    dap_an=my_module.tra_ve_dap_an(list_PA)   
 
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_03]-M1. Tính tổng tích phân trên 2 đoạn nối tiếp
def ckz_L12C4_B4_03():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"${f3}={f1} + {f2}={giatri_f1}+{giatri_f2}={kq}$ ."    
    dap_an=my_module.tra_ve_dap_an(list_PA)   
 
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_04]-M1. Cho theo f. Tính tích phân (m.f+n).
def ckz_L12C4_B4_04():   
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
    debai= f"{noi_dung}"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    tich_mf=show_tich(m,giatri_f)
    hieu=show_hieu(b,a)

    noi_dung_loigiai=f"${g}={m1}{f}{dau_n}{n1}({hieu})={tich_mf}{dau_n}{n1}.{b-a}={kq}$ ."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_05]-M2. Cho tích phân f và F(a). Tính F(b).
def ckz_L12C4_B4_05():   
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
    
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."    

      
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_06]-M1. Cho f(a) và f(b). Tính tích phân f'(x).
def ckz_L12C4_B4_06():   
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    a =random.randint(-4,10)  
    b=a+random.randint(1,6)
    F_a = random.choice([random.randint(-10, -1), random.randint(2, 10)])
    f_b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if F_a==f_b:
        f_b=F_a+random.randint(2,5)
     
    f=f"\\int\\limits_{{{a}}}^{{{b}}} {{f'(x){d_x}}}"

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
    
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."    
      
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D12_C4_B4_07]-M2. Cho tích phân f'(x) và f(a). Tính f(b).
def ckz_L12C4_B4_07():   
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
    
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."    
      
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_08]-M2. Cho tphan_a^c(f) và tphan_a^b(f). Tính tphan_b^c(f), a<b<c.
def ckz_L12C4_B4_08():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    hieu=show_hieu(giatri_f1,giatri_f2)
    noi_dung_loigiai=f"${f1}={f2} + {f3} \\Rightarrow {f3}={f1} - {f2}={hieu}={kq}$."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_09]-M2. Cho tphan_a^d(f) và tphan_b^c(f). Tính tphan_a^b(f) + tphan_c^d(f), a<b<c<d.
def ckz_L12C4_B4_09():   
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
    debai= f"{noi_dung}"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    hieu=show_hieu(giatri_f1,giatri_f2)
    noi_dung_loigiai=f"${f1}={f2} + {f3} +{f4} \\Rightarrow {f3}+{f4}={f1}-{f2}={hieu}={kq}$ ."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#4.4.2 Tích phân các hàm số thường gặp
#[D12_C4_B4_10]. Tính tích phân của m/(ax+b)
def ckz_L12C4_B4_10():
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
    kq2=thay_the_tich_phan(f"$ {m}\\ln {latex(my_module.hien_phan_so(abs((a*x_2+b)/(a*x_1+b))))}+{random.randint(1,2)}$")
    kq3=thay_the_tich_phan(f"$ \\ln {latex(my_module.hien_phan_so(abs((a*x_1+b)/(a*x_2+b))))}$")
    kq4=thay_the_tich_phan(f"$ {m*a}\\ln {latex(my_module.hien_phan_so(abs((a*x_2+b))))}$")

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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"$ \\int\\limits_{{{x_1}}}^{{{x_2}}}{{{latex(f)}{d_x}}}={latex(my_module.hien_phan_so(m/a))}\\ln |{latex(a*x+b)}| \\bigg|_{{{x_1}}}^{{{x_2}}}$"\
    f"$= {latex(my_module.hien_phan_so(m/a))} \\left(\\ln|{latex(a*x_1+b)}| - \\ln|{latex(a*x_2+b)}|\\right)=${kq}.".replace(f"-1\\ln","\\ln")
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_11]. Tính tích phân của (mx+n)/(ax+b)
def ckz_L12C4_B4_11():
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
       
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
  
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_12]. Tính tích phân của đa thức
def ckz_L12C4_B4_12():       
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
    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{phan_so(kq2)}}}$"
    pa_C= f"${{{phan_so(kq3)}}}$"
    pa_D= f"${{{phan_so(kq4)}}}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 
    noi_dung= f"Tính tích phân $  \\int \\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right){d_x}}}$."       
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Sử dụng máy tính ta thu được kết quả bằng $ {{{phan_so(kq)}}}$."
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_13]. Tính tích phân của asinbx
def ckz_L12C4_B4_13():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"$ \\int \\limits_{{{latex(x_1)}}}^{{{latex(x_2)}}}{{{ham}{d_x}}}={phan_so(-b/a)}\\cos {latex(a*x)} \\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$"\
    f"$ = {phan_so(-b/a)}\\left(\\cos{latex(a*x_2)} - \\cos{latex(a*x_1)}\\right)= {{{latex(kq)}}}$."
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B4_14]-SA-M2. Tính tích phân của hàm số kép:ax+b và mx^2+nx+p
def ckz_L12C4_B4_14():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    while True:

        x_0= random.randint(-4,4)
        x_1 = x_0-random.randint(1,4)    
        x_2=x_0+random.randint(1,4)

        m = random.choice([i for i in range(-5, 6) if i!=0])
        n = random.choice([i for i in range(-5, 6) if i!=0])
        p=random.randint(-7,7)
        g=m*x**2+n*x+p

        a = random.choice([i for i in range(-5, 6) if i!=0])
        b = g.subs(x,x_0) -  a*x_0
        f=a*x+b

        

        tp1=integrate(f, (x,x_1,x_0))
        tp2=integrate(g, (x,x_0,x_2))
        if 0<tp1+tp2<100:
            break


    noi_dung = (f" Cho hàm số"
    f" $f(x)= \\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f)} \\text{{ khi }} x\\le {x_0} \\\\ \n\
    {latex(g)}  \\text{{ khi }} x> {x_0}\n\
    \\end{{array}} \\right.$."
    f" Tính ${tphan(x_1,x_2)} f(x){d_x}$(kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(tp1+tp2,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)} f(x){d_x}={tphan(x_1,x_0)} f(x){d_x}+{tphan(x_0,x_2)} f(x){d_x}$"
    f" $={tphan(x_1,x_0)} ({latex(f)}){d_x} + {tphan(x_0,x_2)} ({latex(g)}){d_x}$\n\n"
    f" $={phan_so(tp1)}+{phan_so(tp2)}={phan_so(tp1+tp2)}={dap_an}$."    
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-") 
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_15]-SA-M2. Tính tích phân của hàm số kép:ax+b/x^2 và mx^2+nx+p
def ckz_L12C4_B4_15():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    while True:
        x_0= random.choice([i for i in range(-4, 4) if i!=0])
        x_1 = x_0-random.randint(1,4)    
        x_2=x_0+random.randint(1,4)
        if x_1 != 0 and x_2!=0 and x_1*x_0>0:
            break

    a = random.choice([i for i in range(-5, 5) if i!=0])
    b = random.choice([i for i in range(-5, 5) if i!=0])
    f=a*x+b/x**2

    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-5, 6) if i!=0])
    p=f.subs(x,x_0)-m*x_0**2-n*x_0
    g=m*x**2+n*x+p
    

    tp1=integrate(f, (x,x_1,x_0))
    tp2=integrate(g, (x,x_0,x_2))

    dap_an=f"{round_half_up(tp1+tp2,1):.1f}".replace(".",",")


    noi_dung = (f" Cho hàm số"
    f" $f(x)= \\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f)} \\text{{ khi }} x\\le {x_0} \\\\ \n\
    {latex(g)}  \\text{{ khi }} x> {x_0}\n\
    \\end{{array}} \\right.$."
    f" Tính ${tphan(x_1,x_2)} f(x){d_x}$(kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)} f(x){d_x}={tphan(x_1,x_0)} f(x){d_x}+{tphan(x_0,x_2)} f(x){d_x}$"
    f" $={tphan(x_1,x_0)} ({latex(f)}){d_x} + {tphan(x_0,x_2)} ({latex(g)}){d_x}$\n\n"
    f" $={phan_so(tp1)}+{phan_so(tp2)}={phan_so(tp1+tp2)}={dap_an}$."    
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-") 
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an



#[D12_C4_B4_16]-SA-M3. Tính tích phân của hàm số kép (chứa tham số m) :ax+b và mx^2+nx+p 
def ckz_L12C4_B4_16():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    while True:
        a = random.choice([i for i in range(-5, 6) if i!=0])
        b = random.choice([i for i in range(-5, 6) if i!=0])
        f=a*x+b

        m = random.choice([i for i in range(-5, 6) if i!=0])
        n = random.choice([i for i in range(-5, 6) if i!=0])

        x_0= random.randint(-4,4)

        p=a*x_0+b-m*x_0**2-n*x_0    
        g=m*x**2+n*x+p

        
        x_1 = x_0-random.randint(1,4)    
        x_2=x_0+random.randint(1,4)

        tp1=integrate(f, (x,x_1,x_0))
        tp2=integrate(g, (x,x_0,x_2))
        if tp1+tp2>-9 and tp1+tp2<100:
            break


    noi_dung = (f" Cho hàm số"
    f" $f(x)= \\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f)} \\text{{ khi }} x\\le {x_0} \\\\ \n\
    {latex(m*x**2+n*x)}+m  \\text{{ khi }} x> {x_0}\n\
    \\end{{array}} \\right.$."
    f" Biết rằng hàm số $f(x)$ liên tục trên $\\mathbb{{R}}$."
    f" Tính ${tphan(x_1,x_2)} f(x){d_x}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(tp1+tp2,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Đề hàm số $f(x)$ liên tục trên $\\mathbb{{R}}$ thì hàm số liên tục tại $x_0={x_0}$.\n\n"
    f"Suy ra: ${st_lim(f"{x_0}^{{-}}")} f(x)={st_lim(f"{x_0}^{{+}}")} f(x)$\n\n"
    f"$\\Leftrightarrow {st_lim(f"{x_0}^{{-}}")} ({latex(a*x+b)})={st_lim(f"{x_0}^{{-}}")} ({latex(m*x**2+n*x)}+m)$\n\n"
    f"$\\Leftrightarrow {a*x_0+b}={m*x_0**2+n*x_0}+m \\Leftrightarrow m={p}$.\n\n"

    f"${tphan(x_1,x_2)} f(x){d_x}={tphan(x_1,x_0)} f(x){d_x}+{tphan(x_0,x_2)} f(x){d_x}$"
    f" $={tphan(x_1,x_0)} ({latex(f)}){d_x} + {tphan(x_0,x_2)} ({latex(g)}){d_x}$\n\n"
    f" $={phan_so(tp1)}+{phan_so(tp2)}={phan_so(tp1+tp2)}={dap_an}$."    
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-") 
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_17]-SA-M3. Tính tích phân của hàm số kép (chứa tham số a,b): x^2+ax+b và g(x^3)
def ckz_L12C4_B4_17():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    while True:       

        a = random.choice([i for i in range(-5, 6) if i!=0])
        b = random.choice([i for i in range(-5, 6) if i!=0])
        f_dh=2*a*x+b

        m = random.choice([i for i in range(-2, 2) if i!=0])
        n = random.choice([i for i in range(-3, 3) if i!=0])

        x_0= random.randint(-4,4)

        p=2*a*x_0+b-3*m*x_0**2-2*n*x_0    
        g_dh=3*m*x**2+2*n*x+p

        
        q = random.randint(-5,6)
        g=m*x**3+n*x**2+p*x+q    
        c=g.subs(x,x_0)-a*x_0**2-b*x_0
        f=a*x**2+b*x+c
        
        x_1 = x_0-random.randint(1,4)    
        x_2=x_0+random.randint(1,4)

        tp1=integrate(f, (x,x_1,x_0))
        tp2=integrate(g, (x,x_0,x_2))

        t=random.randint(1,10)/100
        if (tp1+tp2)*t>-9 and (tp1+tp2)*t<1000:
            break

    noi_dung = (f" Cho hàm số"
    f" $f(x)= \\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a*x**2)}+ax+b \\text{{ khi }} x\\le {x_0} \\\\ \n\
    {latex(g)}  \\text{{ khi }} x> {x_0}\n\
    \\end{{array}} \\right.$."
    f" Biết rằng hàm số $f(x)$ có đạo hàm tại điểm $x={x_0}$."
    f" Tính ${phan_so(t)}{tphan(x_1,x_2)} f(x){d_x}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up((tp1+tp2)*t,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Ta có: $f'(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(2*a*x)}+a \\text{{ khi }} x\\le {x_0}\\\\ \n\
    {latex(g_dh)} \\text{{ khi }} x> {x_0}\n\
    \\end{{array}} \\right.$\n\n"

    f"$f'(x)$ có đạo hàm tại $x={x_0}$ nên ta có: \n\n"
    f"$\\Leftrightarrow {2*a*x_0}+a={g_dh.subs(x,x_0)} \\Leftrightarrow a={b}$.\n\n"
    f"$f(x)$ liên tục tại $x={x_0}$ nên:"
    f"${st_lim(f"{x_0}^{{-}}")} f(x)={st_lim(f"{x_0}^{{+}}")} f(x)$\n\n"
    f"$\\Leftrightarrow {st_lim(f"{x_0}^{{-}}")} ({latex(a*x**2+b*x)}+b)={st_lim(f"{x_0}^{{-}}")} ({latex(g)})$\n\n"
    f"$\\Leftrightarrow b={c}$.\n\n"

    f"Suy ra: "
    f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f)} \\text{{ khi }} x\\le {x_0}\\\\ \n\
    {latex(g)} \\text{{ khi }} x> {x_0}\n\
    \\end{{array}} \\right.$\n\n"

    f"${tphan(x_1,x_2)} f(x){d_x}={tphan(x_1,x_0)} f(x){d_x}+{tphan(x_0,x_2)} f(x){d_x}$"
    f" $={tphan(x_1,x_0)} ({latex(f)}){d_x} + {tphan(x_0,x_2)} ({latex(g)}){d_x}$\n\n"
    f" $={phan_so(tp1)}+{phan_so(tp2)}={phan_so(tp1+tp2)}$.\n\n"
    f" Suy ra ${phan_so(t)}{tphan(x_1,x_2)} f(x){d_x}={dap_an}$."    
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-") 
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_18]-SA-M2. Cho tích phân f(x) trên đoạn [a;b]. Tính f(a) hoặc f(b)
def ckz_L12C4_B4_18():
    d_x=f"\\mathrm{{\\,d}}x"
    a=random.randint(-5,3)    
    b=a+random.randint(1,5)
    chon=random.randint(1,2)

    if chon==1:
        f_a=random.randint(-10,20)
        M=random.randint(-10,20)
        if M==f_a: M=f_a+random.randint(1,5)

        noi_dung = (
        f"Cho hàm số $f(x)$ có đạo hàm trên đoạn ${{[{a};{b}]}}$ và $f({a})={f_a}$."
        f" Biết ${tphan(a,b)} f'(x){d_x}= {M}$. Tính $f({b})$."
        )
        dap_an=M+f_a

        noi_dung_loigiai=(
        f"${tphan(a,b)} f'(x){d_x}=f(x)\\bigg|_{{{a}}}^{{{b}}}=f({b})-f({a})={M} \\Rightarrow f({b})={M}+f({a})={M+f_a}$."
        ) 
    
    if chon==2:
        f_b=random.randint(-10,20)
        M=random.randint(-10,20)
        if M==f_b: M=f_b+random.randint(1,5)

        noi_dung = (
        f"Cho hàm số $f(x)$ có đạo hàm trên đoạn ${{[{a};{b}]}}$ và $f({b})={f_b}$."
        f" Biết ${tphan(a,b)} f'(x){d_x}= {M}$. Tính $f({a})$."
        )
        dap_an=f_b-M

        noi_dung_loigiai=(
        f"${tphan(a,b)} f'(x){d_x}=f(x)\\bigg|_{{{a}}}^{{{b}}}=f({b})-f({a})={M} \\Rightarrow f({a})={f_b}-{M}={f_b-M}$."
        ) 
    
    
    noi_dung_loigiai=thay_dau_cong_tru(noi_dung_loigiai)
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_19]-SA-M2. Biết $F(x)=(ax^2+bx+c)e^x$ là một nguyên hàm của hàm số f(x). Tính ma+nb+pc.
def ckz_L12C4_B4_19():
    st_a,st_b,st_c, x=sp.symbols("a b c x")
    m,n,p=[random.choice([i for i in range(-3, 4) if i!=0]) for _ in range(3)]

    a = random.choice([i for i in range(-3, 4) if i!=0])
    b = random.choice([i for i in range(-4, 5) if i!=0])
    c = random.choice([i for i in range(-7, 7) if i!=0])
    noi_dung = (
    f"Biết $F(x)=(ax^2+bx+c)e^x$ là một nguyên hàm của hàm số $f(x)=({latex(a*x**2+(2*a+b)*x+b+c)})e^x$."
    f" Tính ${latex(m*st_a+n*st_b+p*st_c)}$"
    )
    dap_an=m*a+n*b+p*c

    noi_dung_loigiai=(
    f"$F'(x)=(ax^2+bx+c)\\mathrm{{e}}^x+(2ax+b)\\mathrm{{e}}^x=(ax^2+(2a+b)x+b+c)\\mathrm{{e}}^x$.\n\n"
    f"Đồng nhất hệ số với $f(x)$ ta có:\n\n"
    f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    a={a} \\\\ \n\
    2a+b={2*a+b}\\\\ \n\
    b+c={b+c}\n\
    \\end{{array}} \\right. \\Rightarrow a={a},b={b},c={c}$.\n\n"
    f"${latex(m*st_a+n*st_b+p*st_c)}={show_tich(m,a)}+{show_tich(n,b)}+{show_tich(p,c)}={dap_an}$."
    )
    noi_dung_loigiai=thay_dau_cong_tru(noi_dung_loigiai)  
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_20]-SA-M2. Tính tích phân e^x+g(x)
def ckz_L12C4_B4_20():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    while True:
        chon=random.randint(1,2)
        if chon==1:
            a=random.choice([i for i in range(-3, 3) if i!=0])
            b=random.choice([i for i in range(-4, 4) if i!=0])
            c=random.choice([random.randint(-5,5),0])
            g=a*x**2+b*x+c
        
        if chon==2:
            a=random.choice([i for i in range(-3, 3) if i!=0])
            b=random.choice([i for i in range(-3, 3) if i!=0])
            c=random.choice([random.randint(-4,4),0])
            d=random.randint(-5,5)
            g=a*x**3+b*x**2+c*x+d

        m=random.randint(2,6)    
        x_1=random.randint(1,4)
        x_2=x_1+random.randint(1,4)

        g_ngham=integrate(g,x)
        g_tphan=integrate(g, (x,x_1,x_2))
        if m+m*x_1+g_tphan>-9 and m+m*x_1+g_tphan<500:
            break
    t=random.randint(5,10)
    noi_dung = (
    f"Biết tích phân ${tphan(x_1,x_2)}(e^{{{latex(m*x)}}}+{latex(g)}){d_x}=\\dfrac{{1}}{{a}}(e^{{{m*x_2}}}-e^b)+c$."
    f" Tính $\\dfrac{{a+b+c}}{{{t}}}$ (kết quả làm tròn đến hàng phần mười)."
    )
    noi_dung=thay_dau_cong_tru(noi_dung)
    dap_an=f"{round_half_up((m+m*x_1+g_tphan)/t,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)}(e^{{{latex(m*x)}}}+{latex(g)}){d_x}=({phan_so(1/m)}e^{{{latex(m*x)}}}+{latex(g_ngham)})\\bigg|_{{{x_1}}}^{{{x_2}}}$\n\n"
    f"$={phan_so(1/m)}(e^{{{m*x_2}}}-e^{{{m*x_1}}})+{phan_so(g_tphan)}$.\n\n"
    f"Do đó: $a={m}, b={m*x_1}, c={phan_so(g_tphan)}$.\n\n"
    f"$\\dfrac{{a+b+c}}{{{t}}}={dap_an}$."
    )
    noi_dung_loigiai=thay_dau_cong_tru(noi_dung_loigiai)
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_21]-SA-M2. Bài toán thực tế tìm chi phí sản xuất C(x) biết hàm chi phí biên C'(x)
def ckz_L12C4_B4_21():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    ten=random.choice(["A","B","M","X","Y","Z" ])

    while True:

        a=random.randint(20,75)/100000
        st_a=f"{round_half_up(a,5):.5f}".replace(".",",")

        b=random.randint(1,20)/100
        st_b=f"{round_half_up(b,2):.2f}".replace(".",",")

        c=random.randint(4,12)

        C_0=random.randint(20,40)
        C_1=random.randint(70,100)    
        f=c-b*x+a*x**2
        f_tphan=integrate(f, (x,0,C_1))
        if f_tphan>10:
            break
    round_f_tphan=f"{round_half_up(f_tphan,2):.2f}".replace(".",",")

    noi_dung = (
    f"Tại một nhà máy, gọi $C(x)$ là tổng chi phí (tính theo triệu đồng) để sản xuất $x$ tấn sản phẩm {ten} trong một tháng. Khi đó, đạo hàm $C'(x)$, gọi là chi phí cận biên, cho biết tốc độ tăng tổng chi phí theo lượng sản phẩm được sản xuất. Giả sử chi phí cận biên (tính theo triệu đồng trên tấn) của nhà máy được ước lượng bởi công thức"
    f" $C^{{\\prime}}(x)={c}-{st_b}x+{st_a}x^2$ với  $0 \\leq x \\leq {C_1+random.randint(5,10)}$.\n\n"
    f"Biết rằng $C(0)={C_0}$ triệu đồng, gọi là chi phí cố định. Tính tổng chi phí khi nhà máy sản xuất ${{{C_1}}}$ tấn sản phẩm {ten} trong tháng (kết quả làm tròn đến hàng đơn vị)."
    )
    dap_an=f"{round_half_up(C_0+f_tphan,0):.0f}".replace(".",",")

    noi_dung_loigiai=(
    f"$C({C_1})-C(0)={tphan(0,C_1)}C^{{\\prime}}(x){d_x}={tphan(0,C_1)}({c}-{st_b}x+{st_a}x^2){d_x}$\n\n"
    f"$={round_f_tphan}$.\n\n"
    f"Suy ra: $C({C_1})={C_0}+{round_f_tphan}={dap_an}$."
    )

    noi_dung=thay_dau_cong_tru(noi_dung)
    noi_dung_loigiai=thay_dau_cong_tru(noi_dung_loigiai)
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_22]-SA-M2. Tìm m để tích phân (mf+g)=T.
def ckz_L12C4_B4_22():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    while True:

        a = random.choice([i for i in range(-5, 6) if i!=0])
        b= random.randint(-5,6)
        c= random.randint(-5,6)
        d = random.choice([i for i in range(-5, 6) if i!=0])
        e = random.choice([i for i in range(-5, 6) if i!=0])
        f = random.randint(-5,6)

        chon=random.randint(1,2)
        if chon==1:
            f=a*x+b
            g=d*x**2+e*x+f 
        if chon==2:
            f=a*x**2+b*x+c
            g=d*x**3+e*x+f
        x_1=random.randint(-5,2)
        x_2=x_1+random.randint(1,5)

        f_tphan=integrate(f, (x,x_1,x_2))        
        if f_tphan != 0:
            break

    g_tphan=integrate(g, (x,x_1,x_2))
    T=random.randint(-10,10)

        

    noi_dung = (
    f"Biết tích phân ${tphan(x_1,x_2)}\\left[m({latex(f)})+{latex(g)}) \\right]{d_x}={T}$."
    f" Giá trị của ${{m}}$ bằng (kết quả làm tròn đến hàng phần mười)"
    )
    dap_an=f"{round_half_up((T-g_tphan)/f_tphan,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)}\\left[m({latex(f)})+{latex(g)}) \\right]{d_x}={T}$\n\n"
    f" $\\Rightarrow m {tphan(x_1,x_2)}({latex(f)}){d_x}+{tphan(x_1,x_2)}({latex(g)}){d_x}={T}$\n\n"
    f" $\\Leftrightarrow m.\\left({phan_so(f_tphan)}\\right)+{phan_so(g_tphan)}={T}$\n\n"
    f" $\\Rightarrow m=\\dfrac{{{T}-{phan_so(g_tphan)}}}{{{phan_so(f_tphan)}}}={dap_an}$."
    )
    noi_dung=thay_dau_cong_tru(noi_dung)
    noi_dung_loigiai=thay_dau_cong_tru(noi_dung_loigiai)    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_23]-SA-M2. Tính tổng hệ số của kết quả tích phân a/x
def ckz_L12C4_B4_23():
    d_x=f"\\mathrm{{\\,d}}x"
    x,st_a,st_b=sp.symbols("x a b")
    while True:        
        x_1=random.randint(2,7)
        x_2=x_1+random.randint(1,5)
        a = random.choice([i for i in range(-5, 7) if i!=0])
        b=x_2/x_1
        m = random.choice([i for i in range(-5, 6) if i!=0])
        n = random.choice([i for i in range(-5, 6) if i!=0])
        if -5<m*a+n*b<100:
            break
    noi_dung=(
    f"Biết tích phân ${tphan(x_1,x_2)} {latex(a/x)}{d_x}=a\\ln b$. Tính ${latex(m*st_a+n*st_b)}$."
    )
    

    kq=m*a+n*b
    kq_false=[
    m*a-n*b,
    m*b+n*a,
    m*a+n*x_1/x_2
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)} {latex(a/x)}{d_x}={a}\\ln x \\bigg|_{{{x_1}}}^{{{x_2}}}={a}(\\ln {x_2}-\\ln {x_1})$"
    f"$={a}\\ln {phan_so(x_2/x_1)}$.\n\n"
    f"$\\Rightarrow a={a}, b={phan_so(x_2/x_1)}$."
    f" Vậy ${latex(m*st_a+n*st_b)}={phan_so(m*a+n*b)}$."
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

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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

#[D12_C4_B4_24]-M1. Tính tích phân a/x
def ckz_L12C4_B4_24():
    d_x=f"\\mathrm{{\\,d}}x"
    x,st_a,st_b=sp.symbols("x a b")

    x_1=random.randint(2,7)
    x_2=x_1+random.randint(1,5)
    a = random.choice([i for i in range(-5, 7) if i not in [0,1,-1]])
    b=x_2/x_1
    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-5, 6) if i!=0])
    noi_dung=(
    f"Tính tích phân ${tphan(x_1,x_2)} {latex(a/x)}{d_x}$."
    )
    

    kq=f"{a}\\ln {phan_so(x_2/x_1)}"
    kq_false=[
    f"{phan_so(1/a)}\\ln {phan_so(x_2/x_1)}",
    f"{a}\\ln {phan_so(x_1/x_2)}",
    f"{phan_so(1/a)}\\ln {phan_so(x_1/x_2)}",
    f"{a+x_1}\\ln {x_1+x_2}"
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)} {latex(a/x)}{d_x}={a}\\ln x \\bigg|_{{{x_1}}}^{{{x_2}}}={a}(\\ln {x_2}-\\ln {x_1})$"
    f"$={a}\\ln {phan_so(x_2/x_1)}$.\n\n"
    
    )

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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

#[D12_C4_B4_25]-M1. Tính tích phân me^x
def ckz_L12C4_B4_25():
    d_x=f"\\mathrm{{\\,d}}x"
    x,st_a,st_b=sp.symbols("x a b")

    x_1=random.randint(-5,2)
    x_2=x_1+random.randint(1,5)
    a = random.choice([i for i in range(-5, 7) if i not in [0,1,-1]])
    
    noi_dung=(
    f"Tính tích phân ${tphan(x_1,x_2)} {latex(a*exp(x))}{d_x}$."
    )
    

    kq=f"{latex(a*(exp(x_2)-exp(x_1)))}"
    kq_false=[
    f"{latex(a*(exp(x_2)+exp(x_1)))}",
    f"{latex(a*(exp(x_1)-exp(x_2)))}",
    f"{latex((exp(x_2)-exp(x_1)))}",
    f"{phan_so(1/a)}{latex((exp(x_2)-exp(x_1)))}",
    f"{thay_log_2_ln(latex(a*(ln(abs(x_2))-ln(abs(x_1)))))}"
    
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)} {latex(a*exp(x))}{d_x}={latex(a*exp(x))}\\bigg|_{{{x_1}}}^{{{x_2}}}={latex(a*(exp(x_2)-exp(x_1)))}$." )

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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

#[D12_C4_B4_26]-M1. Tính tích phân msinx
def ckz_L12C4_B4_26():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    list_goc=[0,pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2]
    while True:
        x_1= random.choice(list_goc)
        x_2=random.choice([i for i in list_goc  if i != x_1])
        if x_2>x_1 and cos(x_1)!=cos(x_2):
            break 
    
    a = random.choice([i for i in range(-5, 7) if i not in [0,1,-1]])
    f=a*sin(x)
    
    noi_dung=(
    f"Tính tích phân ${tphan(latex(x_1),latex(x_2))} {latex(a*sin(x))}{d_x}$."
    )
    
    

    kq=-a*(cos(x_2)-cos(x_1))
    kq_false=[
    cos(x_2)-cos(x_1),
    a*(cos(x_2)+cos(x_1)),
    a*(cos(x_2)*cos(x_1)),
    a*(cos(x_2)-cos(x_1)),  
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"${tphan(latex(x_1),latex(x_2))} {latex(a*sin(x))}{d_x}={latex(-a*cos(x))}\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}={latex(-a*(cos(x_2)-cos(x_1)))}$." )
    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)

    pa_A= f"*${latex(kq)}$"
    pa_B= f"${latex(kq2)}$"
    pa_C= f"${latex(kq3)}$"
    pa_D= f"${latex(kq4)}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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

#[D12_C4_B4_27]-M1. Tính tích phân mcosx
def ckz_L12C4_B4_27():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    list_goc=[0,pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 3*pi/2]
    while True:
        x_1= random.choice(list_goc)
        x_2=random.choice([i for i in list_goc  if i != x_1])
        if x_2>x_1 and sin(x_1)!=sin(x_2):
            break 
    
    a = random.choice([i for i in range(-5, 7) if i not in [0,1,-1]])
    f=a*sin(x)
    
    noi_dung=(
    f"Tính tích phân ${tphan(latex(x_1),latex(x_2))} {latex(a*cos(x))}{d_x}$."
    )
    

    kq=a*(sin(x_2)-sin(x_1))
    kq_false=[
    sin(x_2)-sin(x_1),
    a*(sin(x_2)+sin(x_1)),
    a*(sin(x_2)*sin(x_1)),
    -a*(sin(x_2)-sin(x_1)),  
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"${tphan(latex(x_1),latex(x_2))} {latex(a*cos(x))}{d_x}={latex(a*sin(x))}\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}={latex(a*(sin(x_2)-sin(x_1)))}$." )

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)
    pa_A= f"*${latex(kq)}$"
    pa_B= f"${latex(kq2)}$"
    pa_C= f"${latex(kq3)}$"
    pa_D= f"${latex(kq4)}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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

#[D12_C4_B4_28]-M1. Tính tích phân a/cos^2x
def ckz_L12C4_B4_28():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    list_goc=[0,pi/6, pi/4, pi/3, 2*pi/3, 3*pi/4, 5*pi/6, pi, 2*pi, 5*pi/4, 5*pi/3, 7*pi/3]
    while True:
        x_1= random.choice(list_goc)
        x_2=random.choice([i for i in list_goc  if i != x_1])
        if x_2>x_1 and sin(x_1)!=sin(x_2):
            break 
    
    a = random.choice([i for i in range(-5, 7) if i not in [0,1,-1]])
    
    
    noi_dung=(
    f"Tính tích phân ${tphan(latex(x_1),latex(x_2))} {latex(a/cos(x)**2)}{d_x}$."
    )
    

    kq=a*(tan(x_2)-tan(x_1))
    kq_false=[
    tan(x_2)-tan(x_1),
    a*(sin(x_2)+sin(x_1)),
    a*(cos(x_2)-cos(x_1)),
    -a*(tan(x_2)-tan(x_1)),  
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"${tphan(latex(x_1),latex(x_2))} {latex(a/cos(x)**2)}{d_x}={latex(a*tan(x))}\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}={latex(a*(tan(x_2)-tan(x_1)))}$." )

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)
    pa_A= f"*${latex(kq)}$"
    pa_B= f"${latex(kq2)}$"
    pa_C= f"${latex(kq3)}$"
    pa_D= f"${latex(kq4)}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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

#[D12_C4_B4_29]-M1. Tính tích phân a/sin^2x
def ckz_L12C4_B4_29():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    list_goc=[pi/6, pi/4, pi/3, 2*pi/3, 3*pi/4, 5*pi/6, pi/2, 3*pi/2, 5*pi/4, 5*pi/3, 7*pi/3]
    while True:
        x_1= random.choice(list_goc)
        x_2=random.choice([i for i in list_goc  if i != x_1])
        if x_2>x_1 and sin(x_1)!=sin(x_2):
            break 
    
    a = random.choice([i for i in range(-5, 7) if i not in [0,1,-1]])   
    
    noi_dung=(
    f"Tính tích phân ${tphan(latex(x_1),latex(x_2))} {latex(a/sin(x)**2)}{d_x}$."
    )    

    kq=-a*(cot(x_2)-cot(x_1))
    kq_false=[
    cot(x_2)-cot(x_1),
    a*(sin(x_2)+sin(x_1)),
    a*(cos(x_2)-cos(x_1)),
    a*(cot(x_2)-cot(x_1)),  
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"${tphan(latex(x_1),latex(x_2))} {latex(a/sin(x)**2)}{d_x}={latex(a*cot(x))}\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}={latex(-a*(cot(x_2)-cot(x_1)))}$." )

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loigiai=thay_sin_cos(noi_dung_loigiai)
    pa_A= f"*${latex(kq)}$"
    pa_B= f"${latex(kq2)}$"
    pa_C= f"${latex(kq3)}$"
    pa_D= f"${latex(kq4)}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}."
    
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

#[D12_C4_B4_30]-M1. Nhận dạng công thức tính tích phân
def ckz_L12C4_B4_30():
    d_x=f"\\mathrm{{\\,d}}x"
    a=random.randint(-10,5)
    b=a+random.randint(1,7)
    noi_dung=(
    f"$F(x)$ là một nguyên hàm của $f(x)$ trên tập xác định $\\mathbb{{R}}$."
    f" Mệnh đề nào sau đây đúng?" )    

    kq=random.choice([f"${tphan(a,b)}f(x){d_x}=F({b})-F({a})$"])
    kq_false=[
    f"${tphan(a,b)}f(x){d_x}=f({b})-f({a})$",
    f"${tphan(a,b)}f(x){d_x}=F({a})-F({b})$",
    f"${tphan(a,b)}f(x){d_x}=F({a})+F({b})$",
    f"${tphan(a,b)}f(x){d_x}=f({a})+f({b})$",
    f"${tphan(a,b)}f(x){d_x}=F({b})-f({a})$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(f"${tphan(a,b)}f(x){d_x}=F({b})-F({a})$.")

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}"

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

#[D12_C4_B4_31]-M1. Nhận dạng biến đổi tích phân
def ckz_L12C4_B4_31():
    d_x=f"\\mathrm{{\\,d}}x"
    d_t=f"\\mathrm{{\\,d}}t"
    a=random.randint(-10,5)
    c=a+random.randint(1,3)
    b=c+random.randint(1,4)
    chon=random.randint(1,2)    
    if chon==1:
        noi_dung=(f"Cho các hàm số $f(x),g(x)$ xác định trên $\\mathbb{{R}}$. Khẳng định nào sau đây sai?")       

        kq=random.choice([
            f"${tphan(a,b)}f(x){d_x}={tphan(b,a)}f(x){d_x}$",
            f"${tphan(a,b)}f(x){d_x}=-{tphan(a,b)}f(t){d_t}$",
            f"${tphan(a,b)}f(x){d_x}={tphan(a,b)}g(x){d_x}$",
            f"${tphan(a,b)}f(x){d_x}={tphan(c,a)}f(x){d_x}+{tphan(a,b)}f(x){d_x}$",
            f"${tphan(a,b)}g(x){d_x}={tphan(c,a)}g(x){d_x}+{tphan(a,b)}g(x){d_x}$",])
        kq_false=[
        f"${tphan(a,a)}f(x){d_x}=0$",
        f"${tphan(a,b)}{{[f(x)+g(x)]}}{d_x}={tphan(a,b)}f(x){d_x}+{tphan(a,b)}g(x){d_x}$",
        f"${tphan(a,b)}f(x){d_x}={tphan(a,b)}f(t){d_t}$",
        f"${tphan(a,b)}f(x){d_x}={tphan(a,c)}f(x){d_x}+{tphan(c,b)}f(x){d_x}$"
        ]

        noi_dung_loigiai=(f"{kq} là khẳng định sai.")
    
    if chon==2:
        noi_dung=(f"Cho các hàm số $f(x),g(x)$ xác định trên $\\mathbb{{R}}$. Khẳng định nào sau đây đúng?")       

        kq=random.choice([
            f"${tphan(a,a)}f(x){d_x}=0$",
            f"${tphan(a,b)}{{[f(x)+g(x)]}}{d_x}={tphan(a,b)}f(x){d_x}+{tphan(a,b)}g(x){d_x}$",
            f"${tphan(a,b)}f(x){d_x}={tphan(a,b)}f(t){d_t}$",
            f"${tphan(a,b)}f(x){d_x}={tphan(a,c)}f(x){d_x}+{tphan(c,b)}f(x){d_x}$"
            ])
        kq_false=[      

        f"${tphan(a,b)}f(x){d_x}={tphan(b,a)}f(x){d_x}$",
            f"${tphan(a,b)}f(x){d_x}=-{tphan(a,b)}f(t){d_t}$",           
            f"${tphan(a,b)}f(x){d_x}={tphan(c,a)}f(x){d_x}+{tphan(a,b)}f(x){d_x}$",
            f"${tphan(a,b)}g(x){d_x}={tphan(c,a)}g(x){d_x}+{tphan(a,b)}g(x){d_x}$",
        ]

        noi_dung_loigiai=(f"{kq} là khẳng định đúng.")    
    
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

    debai= f"{noi_dung}"

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

#[D12_C4_B4_32]-TF-M2. Cho hàm số đa thức f(x). Xét Đ-S:tách tích phân, biểu diễn F(x), tính tích phân, tính tính phân với cận cụ thể.
def ckz_L12C4_B4_32():
    d_x=f"\\mathrm{{\\,d}}x"
    a,b,x=sp.symbols("a b x")


    m = random.choice([i for i in range(-3, 4) if i!=0])
    n = random.choice([i for i in range(-5, 6) if i!=0])
    p= random.randint(-6,6)

    f=m*x**2+n*x+p
    F=integrate(f,x)

    noi_dung = f"Cho tích phân $I={tphan(a,b)}({latex(f)}){d_x}$ . Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"*${tphan(a,b)}({latex(f)}){d_x}={tphan(a,b)}{latex(m*x**2)}{d_x}+{tphan(a,b)}{latex(n*x)}{d_x}+{tphan(a,b)}{p}{d_x}$" 
    kq1_F=f"${tphan(a,b)}({latex(f)}){d_x}={tphan(a,b)}{latex(m*x**3/3)}{d_x}-{tphan(a,b)}{latex(n*x**2/2)}{d_x}+{tphan(a,b)}{latex(p*x)}{d_x}$"
    
    HDG=f"${tphan(a,b)}({latex(f)}){d_x}={tphan(a,b)}{latex(m*x**2)}{d_x}+{tphan(a,b)}{latex(n*x)}{d_x}+{tphan(a,b)}{p}{d_x}$"
    if p==0:
        kq1_T=f"*${tphan(a,b)}({latex(f)}){d_x}={tphan(a,b)}{latex(m*x**2)}{d_x}+{tphan(a,b)}{latex(n*x)}{d_x}$" 
        kq1_F=f"${tphan(a,b)}({latex(f)}){d_x}={tphan(a,b)}{latex(m*x**3/3)}{d_x}-{tphan(a,b)}{latex(n*x**2/2)}{d_x}$"
        
        HDG=f"${tphan(a,b)}({latex(f)}){d_x}={tphan(a,b)}{latex(m*x**2)}{d_x}+{tphan(a,b)}{latex(n*x)}{d_x}$"

    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* $I=({latex(integrate(f,x))})\\bigg|_a^b$"
    kq2_F=f" $I=({latex(diff(f,x))})\\bigg|_a^b$"
    
    HDG=f"$I=({latex(integrate(f,x))})\\bigg|_a^b$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    # Biểu diễn đa thức với thứ tự biến: a trước, b sau
    p4 = F.subs(x,b)-F.subs(x,a)

    # Chuyển lại thành biểu thức (sắp xếp theo thứ tự a trước b)
    sorted_p4 = p4.as_expr()

    kq3_T=f"* $I={latex(sorted_p4)}$" 
    kq3_F=f"$I={latex(F.subs(x,a)-F.subs(x,b))}$"

    
    HDG=f"$I=({latex(integrate(f,x))})\\bigg|_a^b={latex(F.subs(x,b)-F.subs(x,a))}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    a=random.randint(-5,2)
    b=a+random.randint(1,4)
    kq4_T=f"* Với $a={a},b={b}$ thì $I={phan_so(F.subs(x,b)-F.subs(x,a))}$"
    kq4_F=f"Với $a={a},b={b}$ thì $I={phan_so(F.subs(x,a)-F.subs(x,b))}$" 
    
    HDG=f"Với $a={a},b={b}$ thì $I=({latex(integrate(f,x))})\\bigg|_{{{a}}}^{{{b}}}={phan_so(F.subs(x,b))}-{phan_so(F.subs(x,a))}={phan_so(F.subs(x,b)-F.subs(x,a))}$."
    HDG=thay_dau_cong_tru(HDG)
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

#[D12_C4_B4_33]-TF-M2. Cho tích phân trên đoạn của f(x), g(x). Xét Đ-S: tích phân f, tích phân g, tích phân f cận khác, tp hỗn hợp f và g
def ckz_L12C4_B4_33():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    name=["f(x)","g(x)","h(x)"]
    random.shuffle(name)
    f,g=name[0:2]

    a=random.randint(-9,2)
    c=a+random.randint(1,4)
    b=c+random.randint(1,4)

    f_tp=random.randint(-10,10)
    g_tp=random.randint(-10,10)
    if f_tp==g_tp:
        g_tp=g_tp+random.randint(1,2)

    f_tp_ab=random.choice([i for i in range(-10, 10) if i!=0])
    if f_tp_ab==f_tp:
        f_tp_ab=f_tp_ab+random.randint(1,3)

    while True:
        m = random.choice([i for i in range(-5, 6) if i!=0])
        n = random.choice([i for i in range(-5, 6) if i!=0])
        p = random.choice([i for i in range(-5, 6) if i!=0])
        q = random.choice([i for i in range(-5, 6) if i!=0])
        if m!=p and n!=q:
            break


    noi_dung = (f"Cho các hàm số ${f},{g}$ liên tục trên đoạn ${{[{a};{b}]}}$ thỏa mãn"
    f" ${tphan(a,c)}{{[{m}{f}+{n}{g}]}}{d_x}={m*f_tp+n*g_tp}$, ${tphan(a,c)}{{[{p}{f}+{q}{g}]}}{d_x}={p*f_tp+q*g_tp}$"
    f" và ${tphan(a,b)}{f}{d_x}={f_tp_ab}$."
    f" Xét tính đúng-sai của các khẳng định sau. "  )
    noi_dung=noi_dung.replace("[1f","[f").replace("-1f","-f").replace("+1g","+g").replace("-1g","-g").replace("[-1g","[-g").replace("[1h","[h").replace("[-1h","[-h")

    noi_dung=thay_dau_cong_tru(noi_dung)     
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* ${tphan(a,c)}{f}{d_x}={f_tp}$" 
    kq1_F=f"${tphan(a,c)}{f}{d_x}={f_tp+random.randint(1,5)}$"
    st_a,st_b=sp.symbols("a b")
    
    HDG=(f"Đặt $a={tphan(a,c)}{f}{d_x}, b= {tphan(a,c)}{g}{d_x}$, ta có hệ phương trình:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(m*st_a+n*st_b)}={m*f_tp+n*g_tp}\\\\ \n\
        {latex(p*st_a+q*st_b)}={p*f_tp+q*g_tp}\n\
        \\end{{array}} \\right.$"
        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        a={f_tp} \\\\ \n\
        b={g_tp}\n\
        \\end{{array}} \\right. \\Rightarrow {tphan(a,c)}{f}{d_x}={f_tp}, {tphan(a,c)}{g}{d_x}={g_tp}$"
        )
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* ${tphan(a,c)}{g}{d_x}={g_tp}$"
    kq2_F=f"${tphan(a,c)}{g}{d_x}={g_tp+random.randint(1,5)}$"
    
    HDG=f"${tphan(a,c)}{g}{d_x}={g_tp}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* ${tphan(c,b)}{f}{d_x}={f_tp_ab-f_tp}$" 
    kq3_F=f"${tphan(c,b)}{f}{d_x}={f_tp_ab-f_tp+random.randint(1,2)}$"
    
    HDG=(f"${tphan(a,c)}{f}{d_x}+{tphan(c,b)}{f}{d_x}={tphan(a,b)}{f}{d_x}$\n\n"
    f"$\\Rightarrow {tphan(c,b)}{f}{d_x}={tphan(a,b)}{f}{d_x}-{tphan(a,c)}{f}{d_x}={f_tp_ab}-{f_tp}={f_tp_ab-f_tp}$.")
    HDG=thay_dau_cong_tru(HDG)
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    e= random.choice([i for i in range(-5, 6) if i!=0])
    f1=random.randint(-6,6)
    m = random.choice([i for i in range(-5, 6) if i!=0])
    n = random.choice([i for i in range(-5, 6) if i!=0])

    kq=integrate(e*x+f1,(x,a,c))+m*f_tp+n*g_tp
    kq4_T=f"* ${tphan(a,c)}{{[{latex(e*x+f1)}+{m}{f}+{n}{g}]}}{d_x}={phan_so(kq)}$"
    kq4_F=f"${tphan(a,c)}{{[{latex(e*x+f1)}+{m}{f}+{n}{g}]}}{d_x}={phan_so(kq+random.randint(1,2))}$" 
    
    HDG=( f"${tphan(a,c)}{{[{latex(e*x+f1)}+{m}{f}+{n}{g}]}}{d_x}$"
        f"$={tphan(a,c)}({latex(e*x+f1)}{d_x})+{m}{tphan(a,c)}{f}{d_x}+{n}{tphan(a,c)}{g}{d_x}$"
        f"$={phan_so(integrate(e*x+f1,(x,a,c)))}+{m*f_tp}+{n*g_tp}={phan_so(kq)}$."
    )
    HDG=thay_dau_cong_tru(HDG)
    kq4=random.choice([kq4_T, kq4_F])
    kq4.replace("[1f","[f").replace("[-1f","[-f").replace("+1g","+g").replace("-1g","-g")
    kq4=thay_dau_cong_tru(kq4) 
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

#[D12_C4_B4_34]-TF-M2. Cho F(x) là nguyên hàm của f(x). Xét Đ-S: F'(x), tích phân f, tích phân f'
def ckz_L12C4_B4_34():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    chon=random.randint(1,2)
    if chon==1:
        f=a*x+b    
    if chon==2:
        f=a*x**2+b*x+c
       

    noi_dung = f"Cho $F(x)$ là một nguyên hàm của $f(x)={latex(f)}$. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* $F'(x)={latex(f)}$" 
    kq1_F=f"$F'(x)={latex(diff(f,x))}$"
    
    HDG=f"$F(x)$ là một nguyên hàm của $f(x)={latex(f)}$ nên $F'(x)=f(x)={latex(f)}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_1=random.randint(-9,3)
    x_2=x_1+random.randint(1,6)
    kq2_T=f"* ${tphan(x_1,x_2)}({latex(f)}){d_x}=F({x_2})-F({x_1})$"
    kq2_F=f"${tphan(x_1,x_2)}({latex(f)}){d_x}=F({x_2})+F({x_1})$"
    
    HDG=f"${tphan(x_1,x_2)}({latex(f)}){d_x}=F(x)\\bigg|_{{{x_1}}}^{{{x_2}}}=F({x_2})-F({x_1})$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_3=x_1+random.randint(1,3)
    x_4=x_3+random.randint(1,6)
    f_dh=diff(f,x)
    kq3_T=f"* ${tphan(x_3,x_4)}f'(x){d_x}={phan_so(integrate(f_dh,(x,x_3,x_4)))}$" 
    kq3_F=f"${tphan(x_3,x_4)}f'(x){d_x}={phan_so(integrate(f_dh,(x,x_3,x_4))+random.randint(1,3))}$"
    
    HDG=f"${tphan(x_3,x_4)}f'(x){d_x}={tphan(x_3,x_4)}({latex(f_dh)}){d_x}={phan_so(integrate(f_dh,(x,x_3,x_4)))}$"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    while True:
        x_5=random.randint(-9,3)
        x_6=x_5+random.randint(1,4)
        if x_5 not in [x_1,x_3]:
            break    

    kq4_T=f"* ${tphan(x_5,x_6)}f(x){d_x}={phan_so(integrate(f,(x,x_5,x_6)))}$"
    kq4_F=f"${tphan(x_5,x_6)}f(x){d_x}={phan_so(integrate(f,(x,x_5,x_6))+random.randint(1,2))}$" 
    
    HDG=f"${tphan(x_5,x_6)}f(x){d_x}={tphan(x_5,x_6)}({latex(f)}){d_x}=({latex(integrate(f,x))})\\bigg|_{{{x_5}}}^{{{x_6}}}={phan_so(integrate(f,(x,x_5,x_6)))}$"
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

#[D12_C4_B4_35]-TF-M2. Xét Đ-S: Tích phân liên quan đến a^x, e^x
def ckz_L12C4_B4_35():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    noi_dung =f"Xét tính đúng-sai của các khẳng định sau."        
    debai_word= f"{noi_dung}\n"

    a=random.choice([random.randint(2,9)])
    
    kq1_T=f"* $\\int {a}^x{d_x}=\\dfrac{{{a}^x }}{{\\ln {a}}}+C$" 
    kq1_F=f"$\\int {a}^x{d_x}={a}^x\\ln {a}+C$"
    
    HDG=f"$\\int {a}^x=\\dfrac{{{a}^x }}{{\\ln {a}}}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    d_x=f"\\mathrm{{\\,d}}x"
    x,st_a,st_b=sp.symbols("x a b")

    x_1=random.randint(-5,2)
    x_2=x_1+random.randint(1,5)
    a = random.choice([i for i in range(-5, 7) if i not in [0,1,-1]]) 

    kq2_T=f"* ${tphan(x_1,x_2)} {latex(a*exp(x))}{d_x}={latex(a*(exp(x_2)-exp(x_1)))}$"
    kq2_F=f"${tphan(x_1,x_2)} {latex(a*exp(x))}{d_x}={latex(a*(exp(x_1)-exp(x_2)))}$"
    
    HDG=(
    f"${tphan(x_1,x_2)} {latex(a*exp(x))}{d_x}={latex(a*exp(x))}\\bigg|_{{{x_1}}}^{{{x_2}}}={latex(a*(exp(x_2)-exp(x_1)))}$." )
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a=random.randint(0,5)
    b=random.choice([a+random.randint(1,4), log(a+random.randint(4,9))])
    
    T=random.randint(5,15)

    kq3_T=f"* Biết ${tphan(a,latex(b))}{{[f(x)+e^x]}}{d_x}={T}$. Khi đó ${tphan(a,latex(b))}f(x){d_x}={latex(T-integrate(exp(x),(x,a,b)))}$" 
    kq3_F=f"Biết ${tphan(a,latex(b))}{{[f(x)+e^x]}}{d_x}={T}$. Khi đó ${tphan(a,latex(b))}f(x){d_x}={latex(T-integrate(exp(x),(x,a,b))+random.randint(1,2))}$"
    
    HDG=(f"${tphan(a,latex(b))}{{[f(x)+e^x]}}{d_x}={T}$"
        f"$\\Rightarrow {tphan(a,latex(b))}f(x){d_x}={T}-{tphan(a,latex(b))}e^x{d_x}={T}-({latex(integrate(exp(x),(x,a,b)))})$"
        f"$={latex(T-integrate(exp(x),(x,a,b)))}$")
    HDG=thay_log_2_ln(HDG)
    kq3=random.choice([kq3_T, kq3_F])
    kq3=thay_log_2_ln(kq3)
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    f=a*x+b

    x_1=random.randint(-4,3)
    x_0=x_1+random.randint(1,4)
    x_2=x_0+random.randint(1,4)
    m=random.randint(2,6)
    n=a*x_0+b-exp(m*x_0)

    kq=integrate(exp(m*x)+n,(x,x_1,x_0))+integrate(a*x+b,(x,x_0,x_2))
    kq_false=integrate(exp(m*x)+n,(x,x_1,x_0))+integrate(a*x+b,(x,x_0,x_2))+random.randint(1,2)
    ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a*x+b)} \\text{{ khi }} x\\ge {x_0}\\\\ \n\
    {latex(exp(m*x))}+m \\text{{ khi }} x< {x_0}\n\
    \\end{{array}} \\right."
    
    kq4_T=(f"* Cho hàm số ${ham}$ liên tục trên $\\mathbb{{R}}$ (m là tham số).\n\n"
        f"Khi đó: ${tphan(x_1,x_2)}f(x){d_x}={latex(kq)}$")

    kq4_F=(f"Cho hàm số ${ham}$ liên tục trên $\\mathbb{{R}}$ (m là tham số).\n\n"
        f"Khi đó: ${tphan(x_1,x_2)}f(x){d_x}={latex(kq_false)}$")
    
    HDG=(f"Do $f(x)$ liên tục trên $\\mathbb{{R}}$ nên $f(x)$ liên tục tại $x={x_0}$\n\n"
        f"$\\Leftrightarrow {st_lim(f"{x_0}^{{-}}")}f(x)={st_lim(f"{x_0}^{{+}}")}f(x)$\n\n"
        f" $\\Rightarrow {latex(exp(m*x_0))}+m={a*x_0+b}$"
        f" $\\Rightarrow m={latex(n)}$.\n\n"
        f" ${tphan(x_1,x_2)}f(x){d_x}={tphan(x_1,x_0)}({latex(exp(m*x)+n)}){d_x}+{tphan(x_0,x_2)}({latex(a*x+b)}){d_x}$\n\n"
        f" $={latex(integrate(exp(m*x)+n,(x,x_1,x_0)))}+{phan_so(integrate(a*x+b,(x,x_0,x_2)))}$\n\n"
        f" $={latex(kq)}$."
        )
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

#[D12_C4_B4_36]-TF-M2. Cho f'(x)=m/(ax+b), f(x_1), f(x_2). Xét Đ-S: Tích phân f'(x), f(x_3), x(x_4)
def ckz_L12C4_B4_36():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a = random.randint(1,7)
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    x_1=random.randint(int(-b/a)-5,int(-b/a)-2)
    x_2=random.randint(int(-b/a)+2,int(-b/a)+6)

    while True:
        x_3=random.randint(int(-b/a)-7,int(-b/a)-2)
        if x_3 != x_1:
            break

    while True:
        x_4=random.randint(int(-b/a)+2,int(-b/a)+7)
        if x_4 != x_2:
            break


    f_1=random.randint(-4,4)
    f_2=random.randint(-5,5)
    if f_1==f_2: f_2=f_2+random.randint(1,3)


    noi_dung = (f"Cho hàm số $f(x)$ xác định trên $\\mathbb{{R}}\\backslash \\left\\{{{phan_so(-b/a)}\\right\\}}$"
    f" thỏa mãn\n\n $f'(x)={latex(c/(a*x+b))}, f({x_1})={f_1}, f({x_2})={f_2}$.\n\n"
    f"Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần mười):" )      
    debai_word= f"{noi_dung}\n"
    
    m=random.choice([i for i in range(-5, 6) if i!=0])
    kq1_T=f"* $\\int {latex(m/x)}{d_x}={m}\\ln |x|+C$" 
    kq1_F=f"$\\int {latex(m/x)}{d_x}={m}\\log |x|+C$"
    
    HDG=f"$\\int {latex(m/x)}{d_x}={m}\\ln |x|+C$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    
    kq2_T=f"* $\\int f'(x){d_x}={phan_so(c/a)}\\ln |{latex(a*x+b)}|+C$"
    kq2_F=f"$\\int f'(x){d_x}={phan_so(c/a)}\\log |{latex(a*x+b)}|+C$"
    
    HDG=(thay_dau_cong_tru(f"$\\int f'(x){d_x}={phan_so(c/a)}\\ln |{latex(a*x+b)}|+C$." ))

    kq2=random.choice([kq2_T, kq2_F])
    kq2=thay_dau_cong_tru(kq2)
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    C1=f_1-c*log(abs(a*x_1+b))
    C2=f_2-c*log(abs(a*x_2+b))

    kq3_T=f"* $f({x_3})={latex(c*log(abs(a*x_3+b))+C1)}$" 
    kq3_F=f"$f({x_3})={latex(c*log(abs(a*x_3+b))+C2)}$"
    kq3=random.choice([kq3_T, kq3_F])
    kq3=thay_log_2_ln(kq3)
    
    HDG=(f"Từ $f'(x)={latex(c/(a*x+b))}\\Rightarrow f(x)=\\int {latex(c/(a*x+b))}$"
        f"$=\\left\\{{ \\begin{{array}}{{l}} \n\
        {c}\\ln|{latex(a*x+b)}|+C_1 \\text{{ khi }} x<{phan_so(-b/a)} \\\\ \n\
        {c}\\ln|{latex(a*x+b)}|+C_2 \\text{{ khi }} x>{phan_so(-b/a)}\n\
        \\end{{array}} \\right.$\n\n"
        f"Ta có:\n\n $f({x_1})={f_1} \\Rightarrow {latex(c*log(abs(a*x_1+b)))}+C_1={f_1}\\Rightarrow C_1={latex(C1)}$.\n\n"
         f"$f({x_2})={f_2} \\Rightarrow {latex(c*log(abs(a*x_2+b)))}+C_2={f_2}\\Rightarrow C_2={latex(C2)}$.\n\n"
         f"$f({x_3})={latex(c*log(abs(a*x_3+b))+C1)}$"
        )
    HDG=thay_log_2_ln(HDG)
    

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    f_3=c*log(abs(a*x_3+b))+C1
    f_4=c*log(abs(a*x_4+b))+C2

    kq=f"{round_half_up(f_3+f_4,1):.1f}".replace(".",",")
    kq_false=f"{round_half_up(f_3+f_4+random.randint(1,2),1):.1f}".replace(".",",")

    kq4_T=f"* $f({x_3})+f({x_4})={kq}$"
    kq4_F=f"$f({x_3})+f({x_4})={kq_false}$"
    kq4=random.choice([kq4_T, kq4_F])
    kq4=thay_log_2_ln(kq4)
    
    HDG=(f"$f({x_3})={latex(f_3)}$.\n\n"
        f"$f({x_4})={latex(f_4)}$.\n\n"
        f"$f({x_3})+f({x_4})={kq}$.")
    HDG=thay_dau_cong_tru(thay_log_2_ln(HDG))

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

#[D12_C4_B4_37]-TF-M2. Xét Đ-S về biến đổi tích phân: đổi cận, tích phân hàm số chẵn, lẻ, tích phân chứa dấu ||
def ckz_L12C4_B4_37():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    f=random.choice(["f(x)","g(x)","h(x)"])
    a=random.randint(-8,2)
    b=a+random.randint(1,5)
    noi_dung = f"Cho hàm số ${f}$ liên tục trên $\\mathbb{{R}}$. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* ${tphan(a,b)}{f}{d_x}=-{tphan(b,a)}{f}{d_x}$" 
    kq1_F=f"${tphan(a,b)}{f}{d_x}=-{tphan(b,a)}{f}{d_x}$"
    
    HDG=f"${tphan(a,b)}{f}{d_x}=-{tphan(b,a)}{f}{d_x}$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    k = random.choice([i for i in range(-5, 6) if i not in [0,1,-1]])
    kq2_T=f"* ${tphan(a,b)}{f}d({latex(k*x)})={k}{tphan(a,b)}{f}{d_x}$"
    kq2_F=f"${tphan(a,b)}{f}d({latex(k*x)})={random.choice(["",phan_so(1/k)])}{tphan(a,b)}{f}{d_x}$"
    
    HDG=f"${tphan(a,b)}{f}d({latex(k*x)})={tphan(a,b)}{f}({latex(k*x)})'{d_x}={k}{tphan(a,b)}{f}{d_x}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    chon=random.randint(1,2)
    if chon==1:
        a=random.randint(1,9)
        kq3_T=random.choice([
            f"* Biết ${f}$ là hàm số chẵn. Khi đó ${tphan(-a,a)}{f}{d_x}=2{tphan(0,a)}{f}{d_x}$",        
            f"* Biết ${f}$ là hàm số chẵn. Khi đó ${tphan(-a,0)}{f}{d_x}={tphan(0,a)}{f}{d_x}$",
            ])
        kq3_F=random.choice([
            f"Biết ${f}$ là hàm số chẵn. Khi đó ${tphan(-a,a)}{f}{d_x}={tphan(0,a)}{f}{d_x}$",
            f"Biết ${f}$ là hàm số chẵn. Khi đó ${tphan(-a,a)}{f}{d_x}={tphan(-a,0)}{f}{d_x}$",
            f"Biết ${f}$ là hàm số chẵn. Khi đó ${tphan(-a,0)}{f}{d_x}=-{tphan(0,a)}{f}{d_x}$",
            ])  
        
        kq3=random.choice([kq3_T, kq3_F])
        if kq3==kq3_T:
            HDG=(f"Khẳng định đã cho là khẳng định đúng.\n\n"
                f"${f}$ là hàm số chẵn thì:\n\n"
                f"${tphan(-a,0)}{f}{d_x}={tphan(0,a)}{f}{d_x}$ và ${tphan(-a,a)}{f}{d_x}=2{tphan(0,a)}{f}{d_x}$.")
        else:
            HDG=f"Khẳng định đã cho là khẳng định sai."
    
    if chon==2:
        a=random.randint(1,9)
        kq3_T=random.choice([
            f"* Biết ${f}$ là hàm số lẻ. Khi đó ${tphan(-a,a)}{f}{d_x}=0$",        
            f"* Biết ${f}$ là hàm số lẻ. Khi đó ${tphan(-a,0)}{f}{d_x}=-{tphan(0,a)}{f}{d_x}$",
            ])
        kq3_F=random.choice([
            f"Biết ${f}$ là hàm số lẻ. Khi đó ${tphan(-a,a)}{f}{d_x}=2{tphan(0,a)}{f}{d_x}$",            
            f"Biết ${f}$ là hàm số lẻ. Khi đó ${tphan(-a,0)}{f}{d_x}={tphan(0,a)}{f}{d_x}$",
            ])  
        
        kq3=random.choice([kq3_T, kq3_F])
        if kq3==kq3_T:
            HDG=(f"Khẳng định đã cho là khẳng định đúng.\n\n"
                f"${f}$ là hàm số lẻ thì:\n\n"
                f"${tphan(-a,0)}{f}{d_x}=-{tphan(0,a)}{f}{d_x}$ và ${tphan(-a,a)}{f}{d_x}=0$.")
        else:
            HDG=f"Khẳng định đã cho là khẳng định sai."
    
    

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a=random.randint(-9,-1)    
    b=random.randint(2,9)
    x_0=random.choice([i for i in range(a,b) if i!=a and i != b])

    chon=random.randint(1,4)
    
    if chon==1:
        kq4_T=f"* Biết rằng ${f}>0$ với mọi ${{x}}\\in [{a};{b}]$. Khi đó ${tphan(a,b)}|{f}|{d_x}={tphan(a,b)}{f}{d_x}$"
        kq4_F=f"Biết rằng ${f}>0$ với mọi ${{x}}\\in [{a};{b}]$. Khi đó ${tphan(a,b)}|{f}|{d_x}=-{tphan(a,b)}{f}{d_x}$" 
        
        HDG=f"${f}>0$ với mọi ${{x}}\\in [{a};{b}]$ thì ${tphan(a,b)}|{f}|{d_x}={tphan(a,b)}{f}{d_x}$."
        kq4=random.choice([kq4_T, kq4_F])
    
    if chon==2:
        kq4_T=f"* Biết rằng ${f}<0$ với mọi ${{x}}\\in [{a};{b}]$. Khi đó ${tphan(a,b)}|{f}|{d_x}=-{tphan(a,b)}{f}{d_x}$"
        kq4_F=f"Biết rằng ${f}<0$ với mọi ${{x}}\\in [{a};{b}]$. Khi đó ${tphan(a,b)}|{f}|{d_x}={tphan(a,b)}{f}{d_x}$" 
        
        HDG=f"${f}>0$ với mọi ${{x}}\\in [{a};{b}]$ thì ${tphan(a,b)}|{f}|{d_x}=-{tphan(a,b)}{f}{d_x}$."
        kq4=random.choice([kq4_T, kq4_F])

    if chon==3:
        kq4_T=(f"* Biết rằng ${f}=0$ có nghiệm duy nhất $x={x_0}$ và ${f}\\le 0$ mọi ${{x}}\\in [{a};{x_0}]$."
        f" Khi đó ${tphan(a,b)}|{f}|{d_x}=-{tphan(a,x_0)}{f}{d_x}+{tphan(x_0,b)}{f}{d_x}$")

        kq4_F=(f"Biết rằng ${f}=0$ có nghiệm duy nhất $x={x_0}$ và ${f}\\le 0$ mọi ${{x}}\\in [{a};{x_0}]$."
        f" Khi đó ${tphan(a,b)}|{f}|{d_x}={tphan(a,x_0)}{f}{d_x}-{tphan(x_0,b)}{f}{d_x}$")
        
        HDG=(f"${f}=0$ có nghiệm duy nhất $x={x_0}$ và ${f}\\le 0$ mọi ${{x}}\\in [{a};{x_0}]$ nên:\n\n"
            f"${tphan(a,b)}|{f}|{d_x}=-{tphan(a,x_0)}{f}{d_x}+{tphan(x_0,b)}{f}{d_x}$.")
        kq4=random.choice([kq4_T, kq4_F])

    if chon==4:
        kq4_T=(f"* Biết rằng ${f}=0$ có nghiệm duy nhất $x={x_0}$ và ${f}\\ge 0$ mọi ${{x}}\\in [{a};{x_0}]$."
        f" Khi đó ${tphan(a,b)}|{f}|{d_x}={tphan(a,x_0)}{f}{d_x}-{tphan(x_0,b)}{f}{d_x}$")

        kq4_F=(f"Biết rằng ${f}=0$ có nghiệm duy nhất $x={x_0}$ và ${f}\\ge 0$ mọi ${{x}}\\in [{a};{x_0}]$."
        f" Khi đó ${tphan(a,b)}|{f}|{d_x}=-{tphan(a,x_0)}{f}{d_x}+{tphan(x_0,b)}{f}{d_x}$")
        
        HDG=(f"${f}=0$ có nghiệm duy nhất $x={x_0}$ và ${f}\\ge 0$ mọi ${{x}}\\in [{a};{x_0}]$ nên:\n\n"
            f"${tphan(a,b)}|{f}|{d_x}={tphan(a,x_0)}{f}{d_x}-{tphan(x_0,b)}{f}{d_x}$.")
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

#[D12_C4_B4_38]-SA-M2. Tính tổng các hệ số của kết quả tích phân acot^2x+b.
def ckz_L12C4_B4_38():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a= random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    list_can=[pi/6, pi/3, pi/4, 2*pi/3, 3*pi/4, 5*pi/6]
  
    while True:
        x_1=random.choice(list_can)
        x_2=random.choice(list_can)
        if x_1 in [pi/4, 3*pi/4] and x_2 in [pi/4, 3*pi/4]:
            continue
        if x_1<x_2:
            break
    F=a*cot(x)+b*x
    f=diff(F,x)

    result = sp.simplify(integrate(f,(x,x_1,x_2)))

    # Tìm các hệ số a, b, c
    a = result.as_coefficients_dict()[pi]
    b = result.as_coefficients_dict()[sqrt(3)]
    c = result - a*pi - b*sp.sqrt(3)
  
    dap_an=f"{round_half_up(a+b+c,1):.1f}".replace(".",",")
    noi_dung = (
    f"Biết ${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=a{latex(pi)}+b{latex(sqrt(3))}+c$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười)."
    )    

    noi_dung_loigiai=(
    thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
    f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
    f"$\\Rightarrow a={phan_so(a)},b={phan_so(b)},c={latex(c)}$.\n\n"
    f"$a+b+c={dap_an}$."))

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loi_giai=thay_sin_cos(noi_dung_loigiai) 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_39]-SA-M2. Tính tổng các hệ số của kết quả tích phân acot^2x+b.
def ckz_L12C4_B4_39():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a= random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])

    chon=random.randint(1,6)    
    if chon==1:
        x_1, x_2=pi/6, pi/3    
    if chon==2:
        x_1, x_2=pi/4, pi/3
    if chon==3:
        x_1, x_2=pi/6, pi/4
    if chon==4:
        x_1, x_2=3*pi/4, 2*pi/3
    if chon==5:
        x_1, x_2=3*pi/4, 5*pi/6
    if chon==6:
        x_1, x_2=2*pi/3, 5*pi/6

    F=a*tan(x)+b*x
    f=diff(F,x)

    result = sp.simplify(integrate(f,(x,x_1,x_2)))

    # Tìm các hệ số a, b, c
    a = result.as_coefficients_dict().get(sp.pi, 0)
    b = result.as_coefficients_dict().get(sp.sqrt(3), 0)
    c = result - a*pi - b*sp.sqrt(3)
  
    dap_an=f"{round_half_up(a+b+c,1):.1f}".replace(".",",")    
    noi_dung = (
    f"Biết ${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=a{latex(pi)}+b{latex(sqrt(3))}+c$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười)."
    )    

    noi_dung_loigiai=(
    thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
    f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
    f"$\\Rightarrow a={latex(a)},b={latex(b)},c={latex(c)}$.\n\n"
    f"$a+b+c={dap_an}$."))

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loi_giai=thay_sin_cos(noi_dung_loigiai) 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_40]-SA-M2. Tính tổng các hệ số của kết quả tích phân asinmx+bcosnx.
def ckz_L12C4_B4_40():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a= random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    m=random.randint(1,3)
    n=random.randint(1,4)
    F=a*sin(m*x)+b*cos(n*x)
    f=diff(F,x)
    chon=random.randint(1,2)    
    if chon==1:
        list_can=[pi/6, pi/3, 2*pi/3, 5*pi/6]
        random.shuffle(list_can)
        x_1, x_2=list_can[0:2]
        result = sp.simplify(integrate(f,(x,x_1,x_2)))

        # Tìm các hệ số a, b, c
        a = result.as_coefficients_dict().get(sp.sqrt(3), 0)
        b =  result-a*sp.sqrt(3)       
        
        dap_an=f"{round_half_up(a+b,1):.1f}".replace(".",",")    
        noi_dung = (
        f"Biết ${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=a{latex(pi)}+b{latex(sqrt(3))}$. Tính $a+b$ (kết quả làm tròn đến hàng phần mười)."
        )    

        noi_dung_loigiai=(
        thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
        f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
        f"$\\Rightarrow a={latex(a)},b={latex(b)}$.\n\n"
        f"$a+b={dap_an}$."))

    if chon==2:
        x_1=random.choice([pi/6, pi/3, 2*pi/3, 5*pi/6])        
        x_2=random.choice([pi/4, 3*pi/4])  
        result = sp.simplify(integrate(f,(x,x_1,x_2)))

        # Tìm các hệ số a, b, c
        a = result.as_coefficients_dict().get(sp.sqrt(2), 0)
        b = result.as_coefficients_dict().get(sp.sqrt(3), 0)
        c = result - a*sqrt(2) - b*sp.sqrt(3)      
        
        dap_an=f"{round_half_up(a+b+c,1):.1f}".replace(".",",")    
        noi_dung = (
        f"Biết ${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=a{latex(sqrt(2))}+b{latex(sqrt(3))}+c$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười)."
        )    

        noi_dung_loigiai=(
        thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
        f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
        f"$\\Rightarrow a={latex(a)},b={latex(b)},c={latex(c)}$.\n\n"
        f"$a+b+c={dap_an}$."))    

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loi_giai=thay_sin_cos(noi_dung_loigiai) 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_41]-SA-M2. Tính tổng các hệ số của kết quả tích phân asinx+bcosx+cx.
def ckz_L12C4_B4_41():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a= random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-3, 3) if i!=0])

    F=a*sin(x)+b*cos(x)+c*x**2
    f=diff(F,x)   
    
    list_can=[pi/6, pi/3, 2*pi/3, 5*pi/6, pi/2, 0]
    random.shuffle(list_can)
    x_1, x_2=list_can[0:2]
    result = sp.simplify(integrate(f,(x,x_1,x_2)))

    # Tìm các hệ số a, b, c
    a = result.as_coefficients_dict()[pi**2]
    b = result.as_coefficients_dict()[sqrt(3)]
    c = result - a*pi**2 - b*sqrt(3)      
    
    dap_an=f"{round_half_up(a+b+c,1):.1f}".replace(".",",")    
    noi_dung = (
    f"Biết ${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=a{latex(pi**2)}+b{latex(sqrt(3))}+c$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười)."
    )    

    noi_dung_loigiai=(
    thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
    f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
    f"$\\Rightarrow a={latex(a)},b={latex(b)},c={latex(c)}$.\n\n"
    f"$a+b+c={dap_an}$."))      

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loi_giai=thay_sin_cos(noi_dung_loigiai) 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_41]-SA-M2. Tính tổng các hệ số của kết quả tích phân asinx+bcosx+cx.
def ckz_L12C4_B4_41():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    a= random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-3, 3) if i!=0])
    
    F=a*sin(x)+b*cos(x)+c*x**2
    f=diff(F,x)   
    
    list_can=[pi/6, pi/3, 2*pi/3, 5*pi/6, pi/2, 0]
    random.shuffle(list_can)
    x_1, x_2=list_can[0:2]
    result = sp.simplify(integrate(f,(x,x_1,x_2)))

    # Tìm các hệ số a, b, c
    a = result.as_coefficients_dict()[pi**2]
    b = result.as_coefficients_dict()[sqrt(3)]
    c = result - a*pi**2 - b*sqrt(3)      
    
    dap_an=f"{round_half_up(a+b+c,1):.1f}".replace(".",",")    
    noi_dung = (
    f"Biết ${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=a{latex(pi**2)}+b{latex(sqrt(3))}+c$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười)."
    )    

    noi_dung_loigiai=(
    thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}({latex(f)}){d_x}=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
    f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
    f"$\\Rightarrow a={latex(a)},b={latex(b)},c={latex(c)}$.\n\n"
    f"$a+b+c={dap_an}$."))      

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loi_giai=thay_sin_cos(noi_dung_loigiai) 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_42]-SA-M2. Tính tổng các hệ số của kết quả tích phân asin^2(x/2) hoặc acos^2(x/2).
def ckz_L12C4_B4_42():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    m= random.choice([2*i for i in range(-3, 4) if i!=0])   

    chon=random.randint(1,2)

    if chon==1:
        f=m*sin(x/2)**2
        F=m*(x-sin(x))/2    
    if chon==2:
        f=m*cos(x/2)**2
        F=m*(x+sin(x))/2   
    
    
    list_can=[pi/6, pi/3, 2*pi/3, 5*pi/6, pi/2, 0]
    random.shuffle(list_can)
    x_1, x_2=list_can[0:2]
    result = sp.simplify(integrate(f,(x,x_1,x_2)))

    # Tìm các hệ số a, b, c
    a = result.as_coefficients_dict()[pi]
    b = result.as_coefficients_dict()[sqrt(3)]
    c = result - a*pi - b*sqrt(3)     
    
    dap_an=f"{round_half_up(a+b+c,1):.1f}".replace(".",",")    
    noi_dung = (
    f"Biết ${tphan(latex(x_1),latex(x_2))}\\left[{latex(f)}\\right]{d_x}=a{latex(pi)}+b{latex(sqrt(3))}+c$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười)."
    )
    if chon==1:

        noi_dung_loigiai=(
        thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}\\left[{latex(f)}\\right]{d_x}={tphan(latex(x_1),latex(x_2))}\\left[{m}\\dfrac{{1-\\sin x }}{{2}}\\right]{d_x}"
        f"=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
        f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
        f"$\\Rightarrow a={latex(a)},b={latex(b)},c={latex(c)}$.\n\n"
        f"$a+b+c={dap_an}$."))

    if chon==2:

        noi_dung_loigiai=(
        thay_sin_cos(f"${tphan(latex(x_1),latex(x_2))}\\left[{latex(f)}\\right]{d_x}={tphan(latex(x_1),latex(x_2))}\\left[{m}\\dfrac{{1+\\cos x }}{{2}}\\right]{d_x}"
        f"=\\left[{latex(F)}\\right]\\bigg|_{{{latex(x_1)}}}^{{{latex(x_2)}}}$\n\n"
        f"$={latex(F.subs(x,x_2))}-({latex(F.subs(x,x_1))})={latex(F.subs(x,x_2)-F.subs(x,x_1))}$.\n\n"
        f"$\\Rightarrow a={latex(a)},b={latex(b)},c={latex(c)}$.\n\n"
        f"$a+b+c={dap_an}$."))       

    noi_dung=thay_sin_cos(noi_dung)
    noi_dung_loi_giai=thay_sin_cos(noi_dung_loigiai) 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_43]-SA-M2. Tích phân e^(ax+b)
def ckz_L12C4_B4_43():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    while True:
        a=random.randint(2,6)
        b=random.choice([i for i in range(-4, 6) if i!=0])

        x_1=random.randint(-3,4)
        x_2=x_1+random.randint(1,4)

        m=random.choice([i for i in range(-3, 3) if i!=0])
        n=random.choice([i for i in range(-3, 3) if i!=0])
        p=random.choice([i for i in range(-3, 3) if i!=0])
        s_a,s_b, s_c=sp.symbols("a b c")

        f_a=a*x_1+b
        f_b=a*x_2+b
        if -5<m*1/a+n*f_b+p*f_a<100:
            break

    dap_an=f"{round_half_up(m*1/a+n*f_b+p*f_a,1):.1f}".replace(".",",")

    noi_dung = (
    f"Biết ${tphan(x_1,x_2)} {{{latex(exp(a*x+b))}}}{d_x}=a(e^b-e^c)$. Tính ${latex(m*s_a+n*s_b+p*s_c)}$ (kết quả làm tròn đến hàng phần mười)."
    )
    

    noi_dung_loigiai=(
    f"${tphan(x_1,x_2)} {{{latex(exp(a*x+b))}}}{d_x} ={phan_so(1/a)}{latex(exp(a*x+b))}\\bigg|_{{{x_1}}}^{{{x_2}}}$\n\n"
    f"$={phan_so(1/a)}(e^{{{f_b}}}-e^{{{f_a}}})$.\n\n"
    f"$\\Rightarrow a={phan_so(1/a)},b={f_b},c={f_a}$.\n\n"
    f"$\\Rightarrow {latex(m*s_a+n*s_b+p*s_c)}={phan_so(m*1/a+n*f_b+p*f_a)}={dap_an}$.\n\n"
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B4_44]-TF-M2. Xét Đ-S: công thức tích phân, tính tích phân, tích phân của f('x'), cho vận tốc tìm quãng đường
def ckz_L12C4_B4_44():

    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
    ten=["f(x)", "g(x)", "h(x)"]

    f,g=random.sample(ten,2)
    a=random.randint(-8,3)
    b=a+random.randint(2,5)
    c=b+random.randint(1,4)
    k= random.choice([i for i in range(-5, 6) if i!=0])

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=random.choice([
        f"* ${tphan(a,b)}[{f}+{g}]{d_x}={tphan(a,b)}{f}{d_x}+{tphan(a,b)}{g}{d_x}$",
        f"* ${tphan(a,b)}[{f}-{g}]{d_x}={tphan(a,b)}{f}{d_x}-{tphan(a,b)}{g}{d_x}$" ,
        f"* ${tphan(a,b)}{k}{f}{d_x}={k}{tphan(a,b)}{f}{d_x}$" ,
        f"* ${tphan(a,b)}f'(x){d_x}=f({b})-f({a})$" ,
        f"* ${tphan(a,b)}g'(x){d_x}=g({b})-g({a})$" ,
        f"* ${tphan(a,a)}{f}{d_x}=0$" ,
        f"* ${tphan(a,c)}{f}{d_x}={tphan(a,b)}{f}{d_x}+{tphan(b,c)}{f}{d_x}$" ,
        ])
    kq1_F=random.choice([
        f"${tphan(a,b)}[{f}.{g}]{d_x}={tphan(a,b)}{f}{d_x}.{tphan(a,b)}{g}{d_x}$",
        f"${tphan(a,b)}f'(x){d_x}=f({a})+f({b})$" ,
        f"${tphan(a,b)}f'(x){d_x}=f({a})-f({b})$" ,
        f"${tphan(a,c)}{f}{d_x}={tphan(a,b)}{f}{d_x}-{tphan(b,c)}{f}{d_x}$" ,
        f"${tphan(-a,a)}{f}{d_x}=2{tphan(0,a)}{f}{d_x}$" ,
        ])
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f" "
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    
    if chon==1:
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
        f=f"\\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
        g=f"\\int\\limits_{{{a}}}^{{{b}}} {{\\left[ {m1}f(x){dau_n}{n1}\\right]{d_x}}}"

        giatri_f = random.choice([random.randint(-15, -1), random.randint(1, 15)])        
        kq =m*giatri_f + n*(b-a)

        tich_mf=show_tich(m,giatri_f)
        hieu=show_hieu(b,a)

        kq2_T=f"* Cho tích phân ${f}={giatri_f}$. Khi đó ${g}={kq}$"
        kq2_F=f"Cho tích phân ${f}={giatri_f}$. Khi đó ${g}={kq+random.randint(1,3)}$"
        HDG=f"${g}={m1}{f}{dau_n}{n1}({hieu})={tich_mf}{dau_n}{n1}.{b-a}={kq}$."
    
    if chon==2:
        b=a+random.randint(1,6)
        F_a = random.choice([random.randint(-10, -1), random.randint(2, 10)])
        F_b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        if F_a==F_b:
            F_b=F_a+random.randint(2,5)     
        f=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f(x){d_x}}}"
        hieu=show_hieu(F_b,F_a)  
        kq2_T=f"* Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $ F({a})={F_a},F({b})={F_b}$. Khi đó ${f}={F_b-F_a}$"
        kq2_F=f"Biết $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $ F({a})={F_a},F({b})={F_b}$. Khi đó ${f}={F_b+F_a}$"
        HDG=f"${f}=F({b})-F({a})={hieu}={F_b-F_a}$."

    kq2=random.choice([kq2_T, kq2_F])
     
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a =random.randint(-4,10)  
    b=a+random.randint(1,6)
    F_a = random.choice([random.randint(-10, -1), random.randint(2, 10)])
    f_b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if F_a==f_b:
        f_b=F_a+random.randint(2,5)
     
    f=f"  \\int\\limits_{{{a}}}^{{{b}}} {{f'(x){d_x}}}"

    kq=f_b - F_a

    kq3_T=f"* Cho hàm số $f(x)$ có đạo hàm trên đoạn ${{[{a};{b}]}}$, $f({a})={F_a}$ và $f({b})={f_b}$. Khi đó ${f}={kq}$"
    kq3_F=f"Cho hàm số $f(x)$ có đạo hàm trên đoạn ${{[{a};{b}]}}$, $f({a})={F_a}$ và $f({b})={f_b}$. Khi đó ${f}={kq+random.randint(1,2)}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"${f}=f({b})-f({a})={hieu}={kq}$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

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

    kq4_T=(f"* Một vật chuyển động với tốc độ $v(t)={latex(f)} ({m_s})$, với thời gian ${{t}}$ tính bằng giây."
    f" Quãng đường vật đi được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ bằng ${phan_so(kq)}$")
    kq4_F=(f"Một vật chuyển động với tốc độ $v(t)={latex(f)} ({m_s})$, với thời gian ${{t}}$ tính bằng giây."
    f" Quãng đường vật đi được trong khoảng thời gian từ $t={t_1}$ đến $t={t_2}$ bằng ${phan_so(kq+random.randint(1,2))}$")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"Quãng đường đi được là: $  \\int\\limits_{{{t_1}}}^{{{t_2}}} {{\\left({latex(f)}\\right){d_t}}}={phan_so(kq)}$."  
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



    

################ Bài 5: ỨNG DỤNG CỦA TÍCH PHÂN #################
#[D12_C4_B5_01]. Diện tích hình phẳng: y=f(x),Ox,x=a,x=b
def ckz_L12C4_B5_01():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Diện tích hình phẳng xác định bởi: $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f)}\\right|{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_02]. Diện tích hình phẳng: y=f(x),y=g(x),x=a,x=b
def ckz_L12C4_B5_02():   
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
    debai= f"{noi_dung}"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Diện tích hình phẳng xác định bởi: $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f1)}-({latex(f2)})\\right|{d_x}}}$.\n"\
                     f"$=  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f)}\\right|{d_x}}}=$ {kq}"   
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D12_C4_B5_03]. Tìm công thức tính diện tích từ hình vẽ có 1 đồ thị.
def ckz_L12C4_B5_03():   
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
    debai= f"{noi_dung}"\
           f"{file_name}\n"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Diện tích hình phẳng xác định bởi: {kq}.\n"\
       
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_04]. Diện tích hình phẳng: y=f(x),y=g(x)
def ckz_L12C4_B5_04():   
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
    debai= f"{noi_dung}"
    phuongan=f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Xét phương trình ${latex(f1)}={latex(f2)}\\Leftrightarrow {latex(f)}=0\\Leftrightarrow x={x_1},x={x_2}$.\n"\
    f"Diện tích hình phẳng: $S=  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f1)}-({latex(f2)})\\right|{d_x}}}$"\
                     f"$=  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left|{latex(f)}\\right|{d_x}}}=$ {kq}"   
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_05]. Thể tích quay quanh Ox bởi hình: y=f(x),Ox,x=a,x=b
def ckz_L12C4_B5_05():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_06]. Thể tích quay quanh Ox bởi hình: y=ax+b,Ox,x=a,x=b
def ckz_L12C4_B5_06():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_07]. Thể tích quay quanh Ox bởi hình: y=ax^2+bx+c,Ox,x=a,x=b
def ckz_L12C4_B5_07():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_08]. Thể tích quay quanh Ox bởi hình: y=căn(ax+b),Ox,x=a,x=b
def ckz_L12C4_B5_08():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_09]-M3. Thể tích quay quanh Ox bởi hình: y=ae^x+b,Ox,x=a,x=b
def ckz_L12C4_B5_09():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_10]. Thể tích quay quanh Ox bởi hình: y=ax^2+bx+c, Ox
def ckz_L12C4_B5_10():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Xét phương trình: ${latex(f)}=0\\Leftrightarrow x={x_1}, x={x_2}$.\n\n"\
    f"Thể tích khối tròn xoay xác định bởi: $  \\pi\\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#4.5.3 BÀI TOÁN CHUYỂN ĐỘNG

#[D12_C4_B5_11]-M2. Cho hàm số vận tốc. Tính quãng đường đi được từ t1 đến t2.
def ckz_L12C4_B5_11():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Quãng đường đi được là: $  \\int\\limits_{{{t_1}}}^{{{t_2}}} {{\\left({latex(f)}\\right){d_t}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_12]-M3. Cho hàm số vận tốc. Tính quãng đường đi được từ t1 đến t2.
def ckz_L12C4_B5_12():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thời gian để ô tô dừng hẳn là: $v(t)=0\\Leftrightarrow {latex(f)}=0 \\Leftrightarrow t={int(v_0/a)}$,\n\n"\
    f"Quãng đường đi được là: $  \\int\\limits_{{{t_1}}}^{{{t_2}}} {{\\left({latex(f)}\\right){d_t}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_13]-M3. Xe tăng tốc với gia tốc. Tính quãng đường đi được trong khoảng thời gian
def ckz_L12C4_B5_13():   
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
 
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Vận tốc của  ô tô dừng hẳn là: $  \\int\\limits {{\\left({latex(f)}\\right){d_t}}}={latex(a*t**2/2)}+{latex(v_0*t)}+C$,\n\n"\
    f"Theo giả thiết ta có: $v(0)={v_0} \\Rightarrow C={v_0}$.\n\n"\
    f"Quãng đường ôtô đi được là: $  \\int\\limits_{{{t_1}}}^{{{str_t_2}}} {{\\left({latex(a*t**2/2)}+{latex(v_0*t)}+{v_0}\\right){d_t}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_14]-M2. Thể tích vật thể có thiết diện là hình chữ nhật.
def ckz_L12C4_B5_14():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right){d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_14]-M2. Thể tích vật thể có thiết diện là hình chữ nhật.
def ckz_L12C4_B5_14():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right){d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_15]-M2. Thể tích vật thể có thiết diện là hình vuông.
def ckz_L12C4_B5_15():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_16]-M2. Thể tích vật thể có thiết diện là hình tam giác đều.
def ckz_L12C4_B5_16():   
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
    debai= f"{noi_dung}"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}."

    noi_dung_loigiai=f"Thể tích khối tròn xoay xác định bởi:"\
    f" $  \\int\\limits_{{{x_1}}}^{{{x_2}}} {{{latex(sqrt(3)/4)}\\left({latex(f)}\\right)^2{d_x}}}=${kq}."    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_17]-SA-M2. Tính diện tích hình phẳng giới hạn bởi y=(a*x+b)/(c*x+d) và các trục tọa độ
def ckz_L12C4_B5_17():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    
    if chon==1:
        while True:
            c =  random.choice([i for i in range(-2, 2) if i!=0])
            a =  c*random.randint(1,2)            
            a= random.choice([i for i in range(-5, 6) if i!=0])
            b = random.choice([i for i in range(-5, 6) if i!=0])
            d = random.choice([i for i in range(-5, 6) if i!=0])
            if all([a*d-b*c !=0, -b/a >0,-d/c<0]) :
                break
        f=(a*x+b)/(c*x+d)
        
        x_2=phan_so(-b/a)    
        f_abs=abs((a*x+b)/(c*x+d))

        noi_dung = (
        f"  Gọi ${{S}}$ là hình phẳng giới hạn bởi đồ thị hàm số $(H):y=\\dfrac{{{latex(a*x+b)}}}{{{latex(c*x+d)}}}$ và các trục tọa độ."
        f" Tính diện tích hình phẳng ${{S}}$ (kết quả làm tròn đến hàng phần trăm)."
        )

        
        dap_an=f"{round_half_up(integrate(f_abs,(x,0,-b/a)),2):.2f}".replace(".",",")

        noi_dung_loigiai=(
        f" Điều kiện: $x\\ne {phan_so(-d/c)}$.\n\n"
        f" Hoành độ giao điểm của đồ thị hàm số và trục ${{Ox}}$ là nghiệm của phương trình:\n\n"
        f" ${latex(f)}=0 \\Leftrightarrow x={phan_so(-b/a)}$.\n\n"
        f" Diện tích hình phẳng là:\n\n"
        f" $S={tphan(0,x_2)}\\bigg|{latex(f)}\\bigg|={dap_an}$."
        )
    
    if chon==2:
        while True:
            c =  random.choice([i for i in range(-2, 2) if i!=0])
            a =  c*random.randint(1,2)            
            a= random.choice([i for i in range(-5, 6) if i!=0])
            b = random.choice([i for i in range(-5, 6) if i!=0])
            d = random.choice([i for i in range(-5, 6) if i!=0])
            if all([a*d-b*c !=0, -b/a <0,-d/c>0]) :
                break
        f=(a*x+b)/(c*x+d)
        
        x_2=phan_so(-b/a)    
        f_abs=abs((a*x+b)/(c*x+d))

        noi_dung = (
        f"  Gọi ${{S}}$ là hình phẳng giới hạn bởi đồ thị hàm số $(H):y=\\dfrac{{{latex(a*x+b)}}}{{{latex(c*x+d)}}}$ và các trục tọa độ."
        f" Tính diện tích hình phẳng ${{S}}$ (kết quả làm tròn đến hàng phần trăm).") 
        
        dap_an=f"{round_half_up(integrate(f_abs,(x,-b/a,0)),2):.2f}".replace(".",",")

        noi_dung_loigiai=(
        f" Điều kiện: $x\\ne {phan_so(-d/c)}$.\n\n"
        f" Hoành độ giao điểm của đồ thị hàm số và trục ${{Ox}}$ là nghiệm của phương trình:\n\n"
        f" ${latex(f)}=0 \\Leftrightarrow x={phan_so(-b/a)}$.\n\n"
        f" Diện tích hình phẳng là:\n\n"
        f" $S={tphan(x_2,0)}\\bigg|{latex(f)}\\bigg|={dap_an}$."
        )
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B5_18]-SA-M2. Tính diện tích hình phẳng giới hạn bởi đường thẳng và parabol
def ckz_L12C4_B5_18():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")    
           
        
    a= random.choice([i for i in range(-3, 4) if i!=0])
    x_1=random.randint(-4,4)
    x_2=x_1+random.randint(1,4)      

    f=a*(x-x_1)*(x-x_2)

    d = random.choice([i for i in range(-5, 6) if i!=0])
    e= random.choice([i for i in range(-5, 6) if i!=0])
    g=d*x+e   

    noi_dung = (
    f"Tính diện tích của hình phẳng giới hạn bởi đường thẳng $y={latex(expand(g))}$ và đồ thị hàm số"
    f" $y={latex(expand(f+g))}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(abs(integrate(f,(x,x_1,x_2))),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Xét phương trình:\n\n ${latex(expand(f+g))}={latex(expand(g))}\\Leftrightarrow {latex(expand(f))}=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"
    f" Diện tích hình phẳng:\n\n"
    f" $S={tphan(x_1,x_2)}|({latex(expand(f+g))})-({latex(g)})|{d_x}={tphan(x_1,x_2)}|{latex(expand(f))}|{d_x}={phan_so(integrate(f,(x,x_1,x_2)))}={dap_an}$.\n\n")    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B5_19]-SA-M2. Tính V khối tròn xoay khi quay hình giới hạn bởi đường thẳng và parabol quanh Ox
def ckz_L12C4_B5_19():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    while True:
           
        x_0=random.randint(-3,3)    
        a= random.randint(1,3)
        b= random.randint(1,3)     

        f=a*(x-x_0)**2+b

        x_1=random.randint(-3,4)
        x_2=x_1+random.randint(1,3)
        y_1,y_2=f.subs(x,x_1), f.subs(x,x_2)
        k=(y_2-y_1)/(x_2-x_1)
        g=k*(x-x_1)+y_1

        if int(k)==k and pi*integrate(f**2-g**2,(x,x_1,x_2))<900:
            break    

    t=random.randint(8,15)

    noi_dung = (
    f"Gọi ${{V}}$ là thể tích của khối tròn xoay khi quay hình phẳng giới hạn bởi đường thẳng $y={latex(expand(g))}$ và đồ thị hàm số"
    f" $y={latex(expand(f))}$ quanh trục ${{Ox}}$. Tính $\\dfrac{{V}}{{{t}}}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(abs(pi*integrate(f**2-g**2,(x,x_1,x_2)))/t,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Xét phương trình:\n\n ${latex(expand(f))}={latex(expand(g))}\\Leftrightarrow {latex(expand(f-g))}=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"
    f" Thể tích của khối tròn xoay:\n\n $V=\\pi{tphan(x_1,x_2)}|({latex(expand(f))})^2-({latex(g)})^2|{d_x}={phan_so(abs(integrate(f**2-g**2,(x,x_1,x_2))))}\\pi$.\n\n"
    f" Suy ra $\\dfrac{{V}}{{{15}}}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B5_20]-SA-M3. Tính diện tích hình phẳng giới hạn bởi đường thẳng, parabol, trục Ox
def ckz_L12C4_B5_20():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")
                                        
    a= random.randint(1,2)
    x_1=random.randint(-4,1)      

    f=a*(x-x_1)**2

    x_2=x_1+random.randint(1,3)
    y_2=f.subs(x,x_2)
    x_3=x_2+random.randint(1,3)

    k=-y_2/(x_3-x_2)
    g=k*(x-x_3)

    eq = Eq(f, g)

    # Giải phương trình
    solution = solve(eq, x)

    x_a,x_b=solution[0:2]
    tp1=integrate(f,(x,x_1,x_2))
    tp2=integrate(g,(x,x_2,x_3))


    code_hinh=f" \\begin{{tikzpicture}}[>=stealth,x=1cm,y=1cm,scale=0.75]\n\
            \\draw[->] ({x_1-2},0)--({x_3+2},0) node[below]{{$x$}};\n\
            \\draw[->] (0,-2) --(0,{y_2+2}) node[right]{{$y$}};\n\
            \\begin{{scope}}\n\
            \\clip ({x_1-2},-1) rectangle ({x_3+2},{y_2+2});\n\
            \\draw [samples=100, domain={x_1-2}:{x_3}] plot (\\x, {{{a}*(\\x-{x_1})^2}});\n\
            \\draw [samples=100, domain={x_1-2}:{x_3+1}] plot (\\x, {{{k}*(\\x-{x_3})}});\n\
            \\end{{scope}}\n\
            \\fill [pattern=north west lines,draw=none] ({x_1},0)-- plot[domain={x_1}:{x_2}] (\\x, {{{a}*(\\x-{x_1})^2}})-- plot[domain={x_2}:{x_3}] (\\x, {{{k}*(\\x-{x_3})}})--({x_1},0);\n\
            \\fill (0,0) node[shift={{(-120:1.5ex)}}]{{\\footnotesize $O$}} circle(1pt);\n\
            %\\fill ({x_3},0) node[shift={{(-90:1.5ex)}}]{{\\footnotesize ${x_3}$}} circle(1pt);\n\
            %\\fill ({x_2},0) node[shift={{(-90:1.5ex)}}]{{\\footnotesize ${x_2}$}} circle(1pt);\n\
            %\\draw ({x_3},0) node[shift={{(90:1.5ex)}}]{{\\footnotesize $B$}};\n\
            %\\fill ({x_2},{y_2}) node[shift={{(0:1.5ex)}}]{{\\footnotesize $A$}} circle(1pt);\n\
    \\end{{tikzpicture}}" 

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    noi_dung = (
    f"Gọi tam giác cong là hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(expand(g))}$,"
    f" $y={latex(expand(f))}$ và $y=0$ (phần gạch chéo trong hình vẽ dưới đây). "
    f"Tính diện tích của tam giác cong đã cho (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(abs(tp1)+abs(tp2),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Xét phương trình:\n\n ${latex(expand(f))}={latex(expand(g))}\\Leftrightarrow {latex(expand(f-g))}=0 \\Leftrightarrow x={phan_so(x_a)},x={phan_so(x_b)}$.\n\n"
    f" Diện tích hình phẳng:\n\n"
    f" $S={tphan(x_1,x_2)}({latex(expand(f))}){d_x}+{tphan(x_2,x_3)}({latex(expand(g))}){d_x}"
    f"={phan_so(abs(tp1))}+{phan_so(abs(tp2))}={phan_so(abs(tp1)+abs(tp2))}={dap_an}$.\n\n")    
        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B5_21]-SA-M3. Tính diện tích hình phẳng giới hạn bởi đồ thị bậc 3 và parabol
def ckz_L12C4_B5_21():
    d_x=f"\\mathrm{{\\,d}}x"
    x=sp.symbols("x")

    while True:        
        x_1 = random.randint(-5,-1)
        x_2 = x_1+random.randint(1,4)
        x_3 = x_2+random.randint(1,4)
        m = random.choice([i for i in range(-2, 2) if i!=0])

        f=m*(x-x_1)*(x-x_2)*(x-x_3)

        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(-4, 5) if i!=0])
        c = random.randint(-6,6)

        g=a*x**2+b*x+c

        tp1=integrate(f,(x,x_1,x_2))
        tp2=integrate(f,(x,x_2,x_3))
        kq=abs(tp1)+abs(tp2)
        if kq<100:
            break
    dap_an=f"{round_half_up(abs(tp1)+abs(tp2),1):.1f}".replace(".",",")

    noi_dung = ( f"Tính diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(expand(f+g))}$ và $y={latex(g)}$(kết quả làm tròn đến hàng phần mười).")    

    noi_dung_loigiai=(
    f" Xét phương trình:\n\n ${latex(expand(f+g))}={latex(g)}$\n\n $\\Leftrightarrow {latex(expand(f))}=0$ \n\n $\\Rightarrow x={x_1},x={x_2},x={x_3}$.\n\n"
    f" Diện tích hình phẳng là:\n\n "
    f"${tphan(x_1,x_2)}|{latex(expand(f))}|{d_x}+{tphan(x_2,x_3)}|{latex(expand(f))}|{d_x}={phan_so(abs(tp1))}+{phan_so(abs(tp2))}={dap_an}$."    
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B5_22]-SA-M3. Toán thực tế: Tính diện tích phần còn lại của hình vuông sau khi khoét đi 4 parabol.
def ckz_L12C4_B5_22():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    a=random.randint(10,20)
    AB=random.randint(4,8)
    OH= int(a/2)-random.randint(2,5)
    if OH==0:OH=1
    k=-4*OH/AB**2
    f=k*x**2+OH
    S_0=integrate(f,(x,-AB/2,AB/2))
    t=random.randint(6,15)

    dap_an=f"{round_half_up((a**2-4*S_0)/t,1):.1f}".replace(".",",")
    code_hinh=f" \\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.5]\n\
            \\tikzset{{every node/.style={{scale=0.9}}}}\n\
                \\begin{{scope}}\n\
                    \\fill[black] (0,0)--(10,0)--(10,10)--(0,10)--cycle;\n\
                    \\fill[white](2.5,0)--plot[samples=200,domain=2.5:7.5,smooth,variable=\\x] (\\x,{{-16/25*(\\x-2.5)^2+16/5*(\\x-2.5)}})--(7.5,0);\n\
                    \\fill[white](2.5,10)--plot[samples=200,domain=2.5:7.5,smooth,variable=\\x] (\\x,{{16/25*(\\x-2.5)^2-16/5*(\\x-2.5)+10}})--(7.5,10);\n\
                    \\fill[white] plot[samples=200,domain=6:10,smooth,variable=\\x] (\\x,{{sqrt(1.5625*((\\x)-6))+5}})--(10,5)--plot[samples=200,domain=6:10,smooth,variable=\\x] (\\x,{{-sqrt(1.5625*((\\x)-6))+5}})--(10,5);\n\
                    \\fill[white] plot[samples=200,domain=4:0,smooth,variable=\\x] (\\x,{{sqrt(1.5625*(4-(\\x)))+5}})--(0,5)--plot[samples=200,domain=4:0,smooth,variable=\\x] (\\x,{{-sqrt(1.5625*(4-(\\x)))+5}})--(0,5);              \n\
                \\end{{scope}}\n\
                \\draw[fill=white](6,5) circle (1.5pt) node[above right]{{$O$}} (10,2.5) circle (1.5pt) node[right]{{$B$}} (10,7.5) circle (1.5pt) node[right]{{$A$}} (10,5) circle (1.5pt) node[right]{{$H$}};\n\
                \\draw[dashed] (6,5)--(10,5) (10,2.5)--(10,7.5);\n\
            \\end{{tikzpicture}}\n"

        
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    noi_dung = (
    f"Một hoa văn trang trí được tạo ra từ một miếng bìa hình vuông cạnh bằng ${{{a}}}$ cm"
    f" bằng cách khoét đi bốn phần bằng nhau có hình dạng parabol như hình vẽ bên."
    f" Biết $AB={AB}$ cm, $OH={OH}$ cm. Gọi ${{S}}$ là diện tích của bề mặt hoa văn đó (đơn vị: cm$^2$)."
    f" Tính $\\dfrac{{S}}{{{t}}}$ (kết quả làm tròn đến chữ số thập phân thứ nhất)."
    )
    
    noi_dung_loigiai=(
    f"Diện tích bề mặt hoa văn là $S={a}^2-4S_0$, trong đó $ S_0 $ là diện tích của Parabol.\n\n"
    f" Đưa parabol vào hệ trục ${{Oxy}}$ sao cho parabol qua các điểm $A({phan_so(-AB/2)};0),B({phan_so(AB/2)};0)$ và $C(0;{OH})$.\n\n"
    f" Parabol có dạng $y=kx^2+c$.\n\n"
    f" Parabol qua điểm $(0;{OH})\\Rightarrow c={OH}$.\n\n"
    f" Parabol qua điểm  $\\left({phan_so(AB/2)};0\\right)$"
    f" $\\Rightarrow k.{phan_so(AB**2/4)}+{OH}=0$"
    f" $\\Rightarrow k={phan_so(k)}$.\n\n"
    f" $\\Rightarrow (P):y={phan_so(k)}x^2+{OH}$.\n\n"
    f" Diện tích của một parabol là: ${tphan(phan_so(-AB/2),phan_so(AB/2))}({phan_so(k)}x^2+{OH}){d_x}={phan_so(S_0)}$.\n\n"
    f" Diện tích cần tính là: ${a}^2-4.{phan_so(S_0)}={phan_so(a**2-4*S_0)}$.\n\n"
    f" $\\dfrac{{S}}{{{t}}}={dap_an}$"
    )    
        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B5_23]-M3. Cho hình phẳng giới hạn bởi 2 parabol. Tìm công thức tính diện tích
def ckz_L12C4_B5_23():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"   

    while True:
        a1 = random.choice([i for i in range(-3, 3) if i!=0])
        b1=random.randint(-4,4)
        c1=random.randint(-4,4)

        f=a1*x**2+b1*x+c1
        x_1=random.randint(-4,1)
        x_2=x_1+random.randint(1,3)
        f_1=f.subs(x,x_1)
        f_2=f.subs(x,x_2)

        a2 = random.choice([i for i in range(-3, 3) if i!=0])
        b2 = random.randint(-5,5)
        c2 = random.randint(-5,5)
        g=a2*x**2+b2*x+c2
        g_1=g.subs(x,x_1)
        g_2=g.subs(x,x_2)

        s1=f.subs(x,-b1/(2*a1))
        s2=g.subs(x,-b2/(2*a2))
        if all([a1>0, a2<0, g_1==f_1, g_2==f_2, -4<=s1<=4,-4<=s2<=4,]):
            break
    x_f=x_1-0.2
    y_f=f.subs(x,x_f)
    x_g=x_2+0.2
    y_g=g.subs(x,x_g)

    x_min, x_max=x_1-1.5, x_2+1.5
    if x_min>=0:x_min=-2
    if x_max<=0: x_max=2


    y_min, y_max=-4,4
    if s1>=0 and s2>=0:
        y_min, y_max=-2, int(max(s1,s2))+1
    if s1<0 and s2<0:
        y_min, y_max=int(min(s1,s2))-1,2  


    noi_dung=(f"Diện tích phần hình phẳng gạch chéo trong hình vẽ bên dưới được tính theo công thức nào dưới đây?")

    
    kq=random.choice([f"${tphan(x_1,x_2)}({latex(g-f)}){d_x}$"])
    kq_false=[
    f"${tphan(x_1,x_2)}({latex(f-g)}){d_x}$",
    f"${tphan(x_1,x_2)}({latex(f+g)}){d_x}$",
    f"${tphan(x_1,x_2)}|{latex(f)}|{d_x}$",
    f"${tphan(x_1,x_2)}|{latex(g)}|{d_x}$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]


    code_hinh=f" \\begin{{tikzpicture}}[yscale=.8,xscale=.8,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n\
            \\def\\xmin{{{x_min}}} \\def\\xmax{{{x_max}}}\n\
            \\def\\ymin{{{y_min}}} \\def\\ymax{{{y_max}}} \n\
            \\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{{$x$}};\n\
            \\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{{$y$}};\n\
            \\node [left] at ({x_f},{y_f}){{$y={latex(f)}$}};\n\
            \\node [right] at ({x_g},{y_g}){{$y={latex(g)}$}};\n\
            \\begin{{scope}}\n\
            \\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n\
            \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a1}*(\\x)^2+{b1}*(\\x)+{c1}}}) ;\n\
            \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a2}*(\\x)^2+{b2}*(\\x)+{c2}}});\n\
            \\draw[pattern=north east lines,draw=none]\n\
            plot[domain={x_1}:{x_2}](\\x,{{{a1}*(\\x)^2+{b1}*(\\x)+{c1}}}) plot[domain={x_2}:{x_1}](\\x,{{{a2}*(\\x)^2+{b2}*(\\x)+{c2}}});\n\
            \\node at (0,0) [below right]{{$O$}};\n\
            \\draw[dashed] ({x_1},0) node [below]{{${x_1}$}}--({x_1},{g_1});\n\
            \\draw[dashed] ({x_2},0) node [below]{{${x_2}$}}--({x_2},{g_2});\n\
            \\end{{scope}}\n\
        \\end{{tikzpicture}}"
    if x_1==0:
        code_hinh=f" \\begin{{tikzpicture}}[yscale=.8,xscale=.8,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n\
                \\def\\xmin{{{x_min}}} \\def\\xmax{{{x_max}}}\n\
                \\def\\ymin{{{y_min}}} \\def\\ymax{{{y_max}}} \n\
                \\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{{$x$}};\n\
                \\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{{$y$}};\n\
                \\node [left] at ({x_f},{y_f}){{$y={latex(f)}$}};\n\
                \\node [right] at ({x_g},{y_g}){{$y={latex(g)}$}};\n\
                \\begin{{scope}}\n\
                \\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a1}*(\\x)^2+{b1}*(\\x)+{c1}}}) ;\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a2}*(\\x)^2+{b2}*(\\x)+{c2}}});\n\
                \\draw[pattern=north east lines,draw=none]\n\
                plot[domain={x_1}:{x_2}](\\x,{{{a1}*(\\x)^2+{b1}*(\\x)+{c1}}}) plot[domain={x_2}:{x_1}](\\x,{{{a2}*(\\x)^2+{b2}*(\\x)+{c2}}});\n\
                \\node at (0,0) [below right]{{$O$}};\n\
                \\draw[dashed] ({x_1},0) node [below]{{}}--({x_1},{g_1});\n\
                \\draw[dashed] ({x_2},0) node [below]{{${x_2}$}}--({x_2},{g_2});\n\
                \\end{{scope}}\n\
            \\end{{tikzpicture}}"
    if x_2==0:
        code_hinh=f" \\begin{{tikzpicture}}[yscale=.8,xscale=.8,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n\
                \\def\\xmin{{{x_min}}} \\def\\xmax{{{x_max}}}\n\
                \\def\\ymin{{{y_min}}} \\def\\ymax{{{y_max}}} \n\
                \\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{{$x$}};\n\
                \\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{{$y$}};\n\
                \\node [left] at ({x_f},{y_f}){{$y={latex(f)}$}};\n\
                \\node [right] at ({x_g},{y_g}){{$y={latex(g)}$}};\n\
                \\begin{{scope}}\n\
                \\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a1}*(\\x)^2+{b1}*(\\x)+{c1}}}) ;\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a2}*(\\x)^2+{b2}*(\\x)+{c2}}});\n\
                \\draw[pattern=north east lines,draw=none]\n\
                plot[domain={x_1}:{x_2}](\\x,{{{a1}*(\\x)^2+{b1}*(\\x)+{c1}}}) plot[domain={x_2}:{x_1}](\\x,{{{a2}*(\\x)^2+{b2}*(\\x)+{c2}}});\n\
                \\node at (0,0) [below right]{{$O$}};\n\
                \\draw[dashed] ({x_1},0) node [below]{{${x_1}$}}--({x_1},{g_1});\n\
                \\draw[dashed] ({x_2},0) node [below]{{}}--({x_2},{g_2});\n\
                \\end{{scope}}\n\
            \\end{{tikzpicture}}"


    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)


    noi_dung_loigiai=(f"Diện tích hình phẳng là:\n\n ${tphan(x_1,x_2)}|{latex(f)}-({latex(g)})|{d_x}$\n\n"
    f" $={tphan(x_1,x_2)}\\left[{latex(g)}-({latex(f)})\\right]$"
    f" $={tphan(x_1,x_2)}({latex(g-f)}){d_x}$.")

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

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_24]-M3. Cho hình phẳng giới hạn bởi đường thẳng và parabol. Tìm công thức tính diện tích
def ckz_L12C4_B5_24():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    chon=random.randint(1,2)    
    if chon==1:
        while True:
            a = random.choice([i for i in range(1, 3) if i!=0])
            b = random.randint(-4,4)
            c = random.randint(-3,3)
            f = a*x**2+b*x+c
            x_0=-b/(2*a)
            y_0=f.subs(x,x_0)
            x_1=int(x_0)-random.randint(2,4)
            x_2=int(x_0)+random.randint(2,4)
            y_1,y_2=f.subs(x,x_1),f.subs(x,x_2)
            if all([-3<=y_1<=5, -3<=y_2<=5, y_1 != y_2]):
                break

        k=(y_2-y_1)/(x_2-x_1)
        g=k*(x-x_1)+y_1

        x_min, x_max=x_1-1.5, x_2+1.5
        if x_min>=0:x_min=-2
        if x_max<=0: x_max=2


        y_min, y_max=-4,4
        if y_0>=0 :
            y_min, y_max=-2, max(y_1,y_2)+1
        if y_0<0:
            y_min, y_max=y_0-1, max(y_1,y_2)+1

        x_f=x_1-0.2
        y_f=f.subs(x,x_f)
        x_g=x_2+0.2
        y_g=g.subs(x,x_g)

        code_hinh=f" \\begin{{tikzpicture}}[yscale=.8,xscale=.8,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n\
                \\def\\xmin{{{x_min}}} \\def\\xmax{{{x_max}}}\n\
                \\def\\ymin{{{y_min}}} \\def\\ymax{{{y_max}}} \n\
                \\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{{$x$}};\n\
                \\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{{$y$}};\n\
                \\node [left] at ({x_f},{y_f}){{$y={latex(f)}$}};\n\
                \\node [right] at ({x_g},{y_g}){{$y={latex(g)}$}};\n\
                \\begin{{scope}}\n\
                \\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a}*(\\x)^2+{b}*(\\x)+{c}}}) ;\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{k}*((\\x)-{x_1})+{y_1}}});\n\
                \\draw[pattern=north east lines,draw=none]\n\
                plot[domain={x_1}:{x_2}](\\x,{{{a}*(\\x)^2+{b}*(\\x)+{c}}}) plot[domain={x_2}:{x_1}](\\x,{{{k}*((\\x)-{x_1})+{y_1}}});\n\
                \\node at (0,0) [below right]{{$O$}};\n\
                \\draw[dashed] ({x_1},0) node [below]{{${x_1}$}}--({x_1},{y_1});\n\
                \\draw[dashed] ({x_2},0) node [below]{{${x_2}$}}--({x_2},{y_2});\n\
                \\end{{scope}}\n\
            \\end{{tikzpicture}}"

        noi_dung_loigiai=(
        f"Diện tích hình phẳng là:\n\n ${tphan(x_1,x_2)}|{latex(f)}-({latex(g)})|{d_x}$\n\n"
        f" $={tphan(x_1,x_2)}\\left[{latex(g)}-({latex(f)})\\right]$"
        f" $={tphan(x_1,x_2)}({latex(g-f)}){d_x}$.")
        

        kq=random.choice([f"${tphan(x_1,x_2)}({latex(g-f)}){d_x}$"])
        kq_false=[
        f"${tphan(x_1,x_2)}({latex(f-g)}){d_x}$",
        f"${tphan(x_1,x_2)}({latex(f+g)}){d_x}$",
        f"${tphan(x_1,x_2)}|{latex(f)}|{d_x}$",
        f"${tphan(x_1,x_2)}|{latex(g)}|{d_x}$"]
      
    if chon==2:

        while True:
            a = random.randint(-2,-1)
            b = random.randint(-3,2)
            c = random.randint(-4,3)
            f = a*x**2+b*x+c
            x_0=-b/(2*a)
            y_0=f.subs(x,x_0)
            x_1=int(x_0)-random.randint(2,4)
            x_2=int(x_0)+random.randint(2,4)
            y_1,y_2=f.subs(x,x_1),f.subs(x,x_2)

            if all([-5<=y_1<=5, -5<=y_2<=5, y_1 != y_2]):
                break

        k=(y_2-y_1)/(x_2-x_1)
        g=k*(x-x_1)+y_1

        x_min, x_max=x_1-1.5, x_2+1.5
        if x_min>=0:x_min=-2
        if x_max<=0: x_max=2


        y_min, y_max=-4,4
        if y_0>=0 :
            y_min, y_max=min(y_1,y_2)-1, y_0+1
        if y_0<0:
            y_min, y_max=min(y_1,y_2)-1, 2

        x_f=x_1-0.2
        y_f=f.subs(x,x_f)
        x_g=x_2+0.2
        y_g=g.subs(x,x_g)

        code_hinh=f" \\begin{{tikzpicture}}[yscale=.8,xscale=.8,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n\
                \\def\\xmin{{{x_min}}} \\def\\xmax{{{x_max}}}\n\
                \\def\\ymin{{{y_min}}} \\def\\ymax{{{y_max}}} \n\
                \\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{{$x$}};\n\
                \\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{{$y$}};\n\
                \\node [left] at ({x_f},{y_f}){{$y={latex(f)}$}};\n\
                \\node [right] at ({x_g},{y_g}){{$y={latex(g)}$}};\n\
                \\begin{{scope}}\n\
                \\clip (\\xmin,\\ymin) rectangle (\\xmax,\\ymax);\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{a}*(\\x)^2+{b}*(\\x)+{c}}}) ;\n\
                \\draw[smooth,samples=300] plot[domain={x_1-1.5}:{x_2+1.5}](\\x,{{{k}*((\\x)-{x_1})+{y_1}}});\n\
                \\draw[pattern=north east lines,draw=none]\n\
                plot[domain={x_1}:{x_2}](\\x,{{{a}*(\\x)^2+{b}*(\\x)+{c}}}) plot[domain={x_2}:{x_1}](\\x,{{{k}*((\\x)-{x_1})+{y_1}}});\n\
                \\node at (0,0) [below right]{{$O$}};\n\
                \\draw[dashed] ({x_1},0) node [above]{{${x_1}$}}--({x_1},{y_1});\n\
                \\draw[dashed] ({x_2},0) node [above]{{${x_2}$}}--({x_2},{y_2});\n\
                \\end{{scope}}\n\
            \\end{{tikzpicture}}"

        noi_dung_loigiai=(
        f"Diện tích hình phẳng là:\n\n ${tphan(x_1,x_2)}|{latex(f)}-({latex(g)})|{d_x}$\n\n"
        f" $={tphan(x_1,x_2)}\\left[{latex(f)}-({latex(g)})\\right]{d_x}$"
        f" $={tphan(x_1,x_2)}({latex(f-g)}){d_x}$.")
        

        kq=random.choice([f"${tphan(x_1,x_2)}({latex(f-g)}){d_x}$"])
        kq_false=[
        f"${tphan(x_1,x_2)}({latex(g-f)}){d_x}$",
        f"${tphan(x_1,x_2)}({latex(f+g)}){d_x}$",
        f"${tphan(x_1,x_2)}|{latex(f)}|{d_x}$",
        f"${tphan(x_1,x_2)}|{latex(g)}|{d_x}$"]     
    
    noi_dung=(
    f"Diện tích phần hình phẳng gạch chéo trong hình vẽ bên dưới được tính theo công thức nào dưới đây?"
    )

    
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
    
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"\
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C4_B5_25]-M2. Tính diện tích hình phẳng tạo bởi y=e^x, y=a, x=b.
def ckz_L12C4_B5_25():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    a=random.randint(1,4)
    b=random.randint(-4,4)

    noi_dung=(
    f"Hình phẳng giới hạn bởi đồ thị hàm số $y=e^x$ và các đường thẳng $y={a},x={b}$ có diện tích là"
    )
    if log(a)>b:
        noi_dung_loigiai=(
        f"Xét phương trình: $e^x={a}\\Rightarrow x=\\ln {a}$.\n\n"
        f" Diện tích hình phẳng là:\n\n"
        f" ${tphan(b, f"\\ln {a}")} |e^x-{a}| {d_x}=\\bigg|e^x-{a}x\\bigg|_{{{b}}}^{{\\ln {a}}} \\bigg|={latex(integrate(exp(x),(x,b,log(a))))}$."
        )
        kq=abs(integrate(exp(x)-a,(x,b,log(a))))

    else:
        noi_dung_loigiai=(
        f"Xét phương trình: $e^x={a}\\Rightarrow x=\\ln {a}$.\n\n"
        f" Diện tích hình phẳng là:\n\n"
        f" ${tphan(f"\\ln {a}",b)} |e^x-{a}| {d_x}=\\bigg|e^x-{a}x\\bigg|_{{{b}}}^{{\\ln {a}}} \\bigg|={latex(integrate(exp(x),(x,log(a),b)))}$."
        )
        kq=abs(integrate(exp(x)-a,(x,log(a),b)))
    
    kq_false=[
    exp(b),
    exp(a+b),
    abs(integrate(exp(x),(x,a,b))),
    abs(integrate(exp(-x),(x,a,b)))
    ]   

    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3] 

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

#[D12_C4_B5_26]-M2. Tính diện tích hình phẳng tạo bởi y=e^x, x=a, x=b, Ox.
def ckz_L12C4_B5_26():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    a=random.randint(-5,4)
    b=a+random.randint(1,4)

    noi_dung=(
    f"Hình phẳng giới hạn bởi đồ thị hàm số $y=e^x$, các đường thẳng $x={a},x={b}$ và trục ${{Ox}}$ có diện tích là"
    )
    
    noi_dung_loigiai=(    
    f" Diện tích hình phẳng là:\n\n"
    f" ${tphan(a,b)} e^x {d_x}=e^x \\bigg|_{{{a}}}^{{{b}}}={latex(integrate(exp(x),(x,a,b)))}$."
    )
    kq=integrate(exp(x),(x,a,b))
    
    kq_false=[
    exp(a),
    exp(b),
    exp(a+b),
    abs(integrate(exp(2*x),(x,a,b))),
    abs(integrate(exp(-x),(x,a,b)))
    ]   

    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3] 

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

#[D12_C4_B5_27]-M2. Tính diện tích hình phẳng tạo bởi y=m/x, x=a, x=b, Ox.
def ckz_L12C4_B5_27():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    m=random.randint(-8,8)

    chon=random.randint(1,2)
    if chon==1:
        a=random.randint(1,5)
        b=a+random.randint(1,4)
   
    if chon==2:
        a=random.randint(-5,-1)
        b=a-random.randint(1,4)          

    noi_dung=(
    f"Hình phẳng giới hạn bởi đồ thị hàm số $y={latex(m/x)}$, các đường thẳng $x={a},x={b}$ và trục ${{Ox}}$ có diện tích là"
    )
    
    noi_dung_loigiai=(    
    f" Diện tích hình phẳng là:\n\n"
    f" ${tphan(a,b)} {latex(m/x)} {d_x}=\\ln |{latex(m/x)}| \\bigg|_{{{a}}}^{{{b}}}={latex(abs(integrate(m/x,(x,a,b))))}$."
    )
    noi_dung_loigiai=thay_log_2_ln(noi_dung_loigiai)

    kq=abs(integrate(m/x,(x,a,b)))
    
    kq_false=[
    abs(integrate(m*x,(x,a,b))),
    abs(integrate(exp(x),(x,a,b))),
    abs(integrate(m*x+random.randint(1,2),(x,a,b))),
    abs(integrate(m/(x+random.randint(1,2)),(x,a,b)))    
    ]   

    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    thay_log_2_ln

    pa_A= thay_log_2_ln(f"*${{{latex(kq)}}}$")
    pa_B= thay_log_2_ln(f"${{{latex(kq2)}}}$")
    pa_C= thay_log_2_ln(f"${{{latex(kq3)}}}$")
    pa_D= thay_log_2_ln(f"${{{latex(kq4)}}}$")

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

#[D12_C4_B5_28]-M1. Tìm công thức tính diện tích hình phẳng tạo bởi y=a^x, x=a, x=b, Ox.
def ckz_L12C4_B5_28():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    m = random.choice(["e",random.randint(2,9),"\\pi" ])

    a=random.randint(-6,3)
    b=a+random.randint(1,4)
    noi_dung=(
    f"Gọi ${{S}}$ là diện tích của hình phẳng giới hạn bởi các đường $y={m}^x,y=0,x={a},x={b}$."
    f" Khẳng định nào sau đây đúng?")
    

    kq=random.choice([
        f"$S={tphan(a,b)}{m}^x{d_x}$"])
    kq_false=[
    f"$S=\\pi{tphan(a,b)}{m}^x{d_x}$",
    f"$S={tphan(b,a)}{m}^x{d_x}$",
    f"$S=\\pi{tphan(a,b)}{m}^{{2x}}{d_x}$",
    f"$S={tphan(a,b)}{m}^{{2x}}{d_x}$",
    f"$S={tphan(0,a)}{m}^{{2x}}{d_x}$",
    f"$S={tphan(0,b)}{m}^{{2x}}{d_x}$",

    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$S={tphan(a,b)}|{m}^x|{d_x}={tphan(a,b)}{m}^x{d_x}$.")

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

#[D12_C4_B5_29]-M1. Tìm công thức tính diện tích hình phẳng: y=f(x),x=a,x=b,Ox (lí thuyết)
def ckz_L12C4_B5_29():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    f = random.choice(["f(x)", "g(x)", "h(x)"])
    a=random.randint(-6,3)
    b=a+random.randint(1,4)

    noi_dung=(
    f"Gọi ${{S}}$ là diện tích của hình phẳng giới hạn bởi các đường $y={f},y=0,x={a},x={b}$."
    f" Khẳng định nào sau đây đúng?")
    

    kq=random.choice([
        f"$S={tphan(a,b)}|{f}|{d_x}$"])

    kq_false=[
    f"$S=\\pi{tphan(a,b)} {f}{d_x}$",
    f"$S={tphan(b,a)} {f}{d_x}$",
    f"$S={tphan(a,b)} {f}{d_x}$",
    f"$S=\\pi{tphan(a,b)} {{[{f}]^2}}{d_x}$",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$S={tphan(a,b)}|{f}|{d_x}$.")

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

#[D12_C4_B5_30]-M1. (Lí thuyết)Tìm công thức tính diện tích hình phẳng: y=f(x),y=g(x),x=a,x=b,Ox 
def ckz_L12C4_B5_30():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"
    ten=["f(x)", "g(x)", "h(x)"]
    random.shuffle(ten)
    f,g,h = ten[0:3]
    a=random.randint(-6,3)
    b=a+random.randint(1,4)

    noi_dung=(
    f"Gọi ${{S}}$ là diện tích của hình phẳng giới hạn bởi các đường $y={f},y={g},x={a},x={b}$."
    f" Khẳng định nào sau đây đúng?")
    

    kq=random.choice([
        f"$S={tphan(a,b)}|{f}-{g}|{d_x}$",
        f"$S={tphan(a,b)}|{g}-{f}|{d_x}$"])

    kq_false=[
    f"$S=\\pi{tphan(a,b)} ({f}-{g}){d_x}$",
    f"$S={tphan(a,b)} {{[{f}+{g}]}}{d_x}$",
    f"$S={tphan(a,b)} |{f}|{d_x}-{tphan(a,b)} |{g}|{d_x}$",
    f"$S=\\pi{tphan(a,b)} {{[|{f}|-|{g}|]}}{d_x}$",
    f"$S=\\pi{tphan(a,b)} {{[|{g}|-|{h}|]}}{d_x}$",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$S={tphan(a,b)}|{f}-{g}|{d_x}={tphan(a,b)}|{g}-{f}|{d_x}$.")

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

#[D12_C4_B5_31]-TF-M3. Xét Đ-S: Công thức tính diện tích, diện tích 1 f(x), diện tích f và g, diện tích f,g,h
def ckz_L12C4_B5_31():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười)."        
    debai_word= f"{noi_dung}\n"
    a=random.randint(-5,2)
    b=a+random.randint(1,4)
    f=random.choice(["f(x)","g(x)","h(x)"])
    
    kq1_T=(f"* Hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ có diện tích xác định bởi công thức"
        f" $S={tphan(a,b)}|{f}|{d_x}$")
    chon=random.randint(1,2)
    if chon==1:
        kq1_F=(f"Hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ có diện tích xác định bởi công thức"
            f" $S={tphan(a,b)}{f}{d_x}$")    
    if chon==2:
        kq1_F=(f"Hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ có diện tích xác định bởi công thức"
            f" $S=\\bigg|{tphan(a,b)}{f}{d_x}\\bigg|$")
    
    
    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f"Hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ có diện tích xác định bởi công thức"
        f" $S={tphan(a,b)}|{f}|{d_x}$")
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.choice([i for i in range(-5, 6) if i!=0])
    n=random.randint(-6,6)
    a=random.randint(-5,2)
    b=a+random.randint(1,4)

    f=a*x+b
    S=abs(integrate(f,(x,a,b)))

    kq2_T=f"* Hình phẳng giới hạn bởi các đường $y={latex(f)},x={a},x={b},y=0$ có diện tích bằng ${{{latex(S)}}}$"
    kq2_F=f" Hình phẳng giới hạn bởi các đường $y={latex(f)},x={a},x={b},y=0$ có diện tích bằng ${{{latex(S+random.randint(1,3))}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Diện tích hình phẳng là: $S={tphan(a,b)} |{latex(f)}|{d_x}={latex(S)}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.choice([i for i in range(-3, 4) if i!=0])
    x_1=random.randint(-4,4)
    x_2=x_1+random.randint(1,4)      

    f=a*(x-x_1)*(x-x_2)

    d = random.choice([i for i in range(-5, 6) if i!=0])
    e= random.choice([i for i in range(-5, 6) if i!=0])
    g=d*x+e   

    dap_an=phan_so(abs(integrate(f,(x,x_1,x_2))))
    dap_an_false=phan_so(abs(integrate(f,(x,x_1,x_2)))+random.randint(1,2))

    kq3_T=(f"* Diện tích của hình phẳng giới hạn bởi đường thẳng $y={latex(expand(g))}$ và đồ thị hàm số"
    f" $y={latex(expand(f+g))}$ bằng ${dap_an}$")

    kq3_F=(f" Diện tích của hình phẳng giới hạn bởi đường thẳng $y={latex(expand(g))}$ và đồ thị hàm số"
    f" $y={latex(expand(f+g))}$ bằng ${dap_an_false}$")
    kq3=random.choice([kq3_T, kq3_F])
    HDG=(f"Xét phương trình:\n\n ${latex(expand(f+g))}={latex(expand(g))}\\Leftrightarrow {latex(expand(f))}=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"
    f" Diện tích hình phẳng:\n\n"
    f" $S={tphan(x_1,x_2)}|({latex(expand(f+g))})-({latex(g)})|{d_x}={tphan(x_1,x_2)}|{latex(expand(f))}|{d_x}={phan_so(integrate(f,(x,x_1,x_2)))}={dap_an}$.\n\n")
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.randint(1,2)
    x_1=random.randint(-4,1)      

    f=a*(x-x_1)**2

    x_2=x_1+random.randint(1,3)
    y_2=f.subs(x,x_2)
    x_3=x_2+random.randint(1,3)

    k=-y_2/(x_3-x_2)
    g=k*(x-x_3)

    eq = Eq(f, g)

    # Giải phương trình
    solution = solve(eq, x)

    x_a,x_b=solution[0:2]
    tp1=integrate(f,(x,x_1,x_2))
    tp2=integrate(g,(x,x_2,x_3))


    code_hinh=f" \\begin{{tikzpicture}}[>=stealth,x=1cm,y=1cm,scale=0.75]\n\
            \\draw[->] ({x_1-2},0)--({x_3+2},0) node[below]{{$x$}};\n\
            \\draw[->] (0,-2) --(0,{y_2+2}) node[right]{{$y$}};\n\
            \\begin{{scope}}\n\
            \\clip ({x_1-2},-1) rectangle ({x_3+2},{y_2+2});\n\
            \\draw [samples=100, domain={x_1-2}:{x_3}] plot (\\x, {{{a}*(\\x-{x_1})^2}});\n\
            \\draw [samples=100, domain={x_1-2}:{x_3+1}] plot (\\x, {{{k}*(\\x-{x_3})}});\n\
            \\end{{scope}}\n\
            \\fill [pattern=north west lines,draw=none] ({x_1},0)-- plot[domain={x_1}:{x_2}] (\\x, {{{a}*(\\x-{x_1})^2}})-- plot[domain={x_2}:{x_3}] (\\x, {{{k}*(\\x-{x_3})}})--({x_1},0);\n\
            \\fill (0,0) node[shift={{(-120:1.5ex)}}]{{\\footnotesize $O$}} circle(1pt);\n\
            %\\fill ({x_3},0) node[shift={{(-90:1.5ex)}}]{{\\footnotesize ${x_3}$}} circle(1pt);\n\
            %\\fill ({x_2},0) node[shift={{(-90:1.5ex)}}]{{\\footnotesize ${x_2}$}} circle(1pt);\n\
            %\\draw ({x_3},0) node[shift={{(90:1.5ex)}}]{{\\footnotesize $B$}};\n\
            %\\fill ({x_2},{y_2}) node[shift={{(0:1.5ex)}}]{{\\footnotesize $A$}} circle(1pt);\n\
    \\end{{tikzpicture}}" 

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    
    dap_an=phan_so(abs(tp1)+abs(tp2))
    dap_an_false=phan_so(abs(tp1)+abs(tp2)+random.randint(1,2))

    
    kq4_T=(f"* Gọi tam giác cong là hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(expand(g))}$,"
    f" $y={latex(expand(f))}$ và $y=0$ (phần gạch chéo trong hình vẽ). \n{file_name}\n"
    f" Diện tích của tam giác cong đã cho bằng ${{{dap_an}}}$ ")
    kq4_F=(f"Gọi tam giác cong là hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(expand(g))}$,"
    f" $y={latex(expand(f))}$ và $y=0$ (phần gạch chéo trong hình vẽ). \n{file_name}\n"
    f" Diện tích của tam giác cong đã cho bằng ${{{dap_an_false}}}$")
    kq4=random.choice([kq4_T, kq4_F])

    HDG=(
    f"Xét phương trình:\n\n ${latex(expand(f))}={latex(expand(g))}\\Leftrightarrow {latex(expand(f-g))}=0 \\Leftrightarrow x={phan_so(x_a)},x={phan_so(x_b)}$.\n\n"
    f" Diện tích hình phẳng:\n\n"
    f" $S={tphan(x_1,x_2)}({latex(expand(f))}){d_x}+{tphan(x_2,x_3)}({latex(expand(g))}){d_x}"
    f"={phan_so(abs(tp1))}+{phan_so(abs(tp2))}={phan_so(abs(tp1)+abs(tp2))}$.\n\n")
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


    debai_latex=debai_latex.replace(file_name,f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")


    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B5_32]-TF-M3. Xét Đ-S: Công thức tính thể tích, thể tích 1 f(x), diện tích f và g, diện tích f,g,h
def ckz_L12C4_B5_32():
    x=sp.symbols("x")
    d_x=f"\\mathrm{{\\,d}}x"

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười)."        
    debai_word= f"{noi_dung}\n"
    a=random.randint(-5,2)
    b=a+random.randint(1,4)
    f=random.choice(["f(x)","g(x)","h(x)"])
    
    kq1_T=(f"* Thể tích của vật thể tròn xoay được tạo thành khi quay hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ quanh trục ${{Ox}}$ "
        f" có công thức là $V=\\pi{tphan(a,b)}{{[{f}]^2}}{d_x}$")
    chon=random.randint(1,2)
    if chon==1:
        kq1_F=(f"Thể tích của vật thể tròn xoay được tạo thành khi quay hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ quanh trục ${{Ox}}$ "
        f" có công thức là $V={tphan(a,b)}{{[{f}]^2}}{d_x}$")    
    if chon==2:
        kq1_F=(f"Thể tích của vật thể tròn xoay được tạo thành khi quay hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ quanh trục ${{Ox}}$ "
        f" có công thức là $V={tphan(a,b)}|{f}|{d_x}$")
    
    
    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f"Thể tích của vật thể tròn xoay được tạo thành khi quay hình phẳng giới hạn bởi các đường $y={f},x={a},x={b},y=0$ quanh trục ${{Ox}}$ "
        f" có công thức là $V=\\pi{tphan(a,b)}{{[{f}]^2}}{d_x}$")
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.choice([i for i in range(-5, 6) if i!=0])
    n=random.randint(-6,6)
    a=random.randint(-5,2)
    b=a+random.randint(1,4)

    f=a*x+b
    V=pi*(integrate((a*x+b)**2,(x,a,b)))
    V_false=(integrate((a*x+b)**2,(x,a,b)))

    kq2_T=f"* Quay hình phẳng giới hạn bởi các đường $y={latex(f)},x={a},x={b},y=0$ quanh trục ${{Ox}}$ tạo thành vật thể tròn xoay có thể tích bằng ${{{latex(V)}}}$"
    kq2_F=f" Quay hình phẳng giới hạn bởi các đường $y={latex(f)},x={a},x={b},y=0$ quanh trục ${{Ox}}$ tạo thành vật thể tròn xoay có thể tích bằng ${{{latex(V_false)}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Thể tích của vật thể là: $V=\\pi{tphan(a,b)} {latex((a*x+b)**2)}{d_x}={latex(V)}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.choice([i for i in range(-3, 4) if i!=0])
    x_1=random.randint(-4,4)
    x_2=x_1+random.randint(1,4)      

    f=a*(x-x_1)*(x-x_2)

    d = random.choice([i for i in range(-5, 6) if i!=0])
    e= random.choice([i for i in range(-5, 6) if i!=0])
    g=d*x+e   

    dap_an=phan_so(abs(integrate(f,(x,x_1,x_2))))
    dap_an_false=phan_so(abs(integrate(f,(x,x_1,x_2)))+random.randint(1,2))

    kq3_T=(f"* Diện tích của hình phẳng giới hạn bởi đường thẳng $y={latex(expand(g))}$ và đồ thị hàm số"
    f" $y={latex(expand(f+g))}$ bằng ${{{dap_an}}}$")

    kq3_F=(f" Diện tích của hình phẳng giới hạn bởi đường thẳng $y={latex(expand(g))}$ và đồ thị hàm số"
    f" $y={latex(expand(f+g))}$ bằng ${{{dap_an_false}}}$")
    kq3=random.choice([kq3_T, kq3_F])
    HDG=(f"Xét phương trình:\n\n ${latex(expand(f+g))}={latex(expand(g))}\\Leftrightarrow {latex(expand(f))}=0 \\Leftrightarrow x={x_1},x={x_2}$.\n\n"
    f" Diện tích hình phẳng:\n\n"
    f" $S={tphan(x_1,x_2)}|({latex(expand(f+g))})-({latex(g)})|{d_x}={tphan(x_1,x_2)}|{latex(expand(f))}|{d_x}={phan_so(integrate(f,(x,x_1,x_2)))}={dap_an}$.\n\n")
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.randint(1,2)
    x_1=random.randint(-4,1)      

    f=a*(x-x_1)**2

    x_2=x_1+random.randint(1,3)
    y_2=f.subs(x,x_2)
    x_3=x_2+random.randint(1,3)

    k=-y_2/(x_3-x_2)
    g=k*(x-x_3)

    eq = Eq(f, g)

    # Giải phương trình
    solution = solve(eq, x)

    x_a,x_b=solution[0:2]
    tp1=integrate(f,(x,x_1,x_2))
    tp2=integrate(g,(x,x_2,x_3))


    code_hinh=f" \\begin{{tikzpicture}}[>=stealth,x=1cm,y=1cm,scale=0.75]\n\
            \\draw[->] ({x_1-2},0)--({x_3+2},0) node[below]{{$x$}};\n\
            \\draw[->] (0,-2) --(0,{y_2+2}) node[right]{{$y$}};\n\
            \\begin{{scope}}\n\
            \\clip ({x_1-2},-1) rectangle ({x_3+2},{y_2+2});\n\
            \\draw [samples=100, domain={x_1-2}:{x_3}] plot (\\x, {{{a}*(\\x-{x_1})^2}});\n\
            \\draw [samples=100, domain={x_1-2}:{x_3+1}] plot (\\x, {{{k}*(\\x-{x_3})}});\n\
            \\end{{scope}}\n\
            \\fill [pattern=north west lines,draw=none] ({x_1},0)-- plot[domain={x_1}:{x_2}] (\\x, {{{a}*(\\x-{x_1})^2}})-- plot[domain={x_2}:{x_3}] (\\x, {{{k}*(\\x-{x_3})}})--({x_1},0);\n\
            \\fill (0,0) node[shift={{(-120:1.5ex)}}]{{\\footnotesize $O$}} circle(1pt);\n\
            %\\fill ({x_3},0) node[shift={{(-90:1.5ex)}}]{{\\footnotesize ${x_3}$}} circle(1pt);\n\
            %\\fill ({x_2},0) node[shift={{(-90:1.5ex)}}]{{\\footnotesize ${x_2}$}} circle(1pt);\n\
            %\\draw ({x_3},0) node[shift={{(90:1.5ex)}}]{{\\footnotesize $B$}};\n\
            %\\fill ({x_2},{y_2}) node[shift={{(0:1.5ex)}}]{{\\footnotesize $A$}} circle(1pt);\n\
    \\end{{tikzpicture}}" 

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    
    dap_an=phan_so(abs(tp1)+abs(tp2))
    dap_an_false=phan_so(abs(tp1)+abs(tp2)+random.randint(1,2))

    
    kq4_T=(f"* Gọi tam giác cong là hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(expand(g))}$,"
    f" $y={latex(expand(f))}$ và $y=0$.\n{file_name}\n"
    f" Diện tích của tam giác cong đã cho bằng ${{{dap_an}}}$")
    kq4_F=(f"Gọi tam giác cong là hình phẳng giới hạn bởi đồ thị các hàm số $y={latex(expand(g))}$,"
    f" $y={latex(expand(f))}$ và $y=0$.\n{file_name}\n"
    f" Diện tích của tam giác cong đã cho bằng ${{{dap_an_false}}}$")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(
    f"Xét phương trình:\n\n ${latex(expand(f))}={latex(expand(g))}\\Leftrightarrow {latex(expand(f-g))}=0 \\Leftrightarrow x={phan_so(x_a)},x={phan_so(x_b)}$.\n\n"
    f" Diện tích hình phẳng:\n\n"
    f" $S={tphan(x_1,x_2)}({latex(expand(f))}){d_x}+{tphan(x_2,x_3)}({latex(expand(g))}){d_x}"
    f"={phan_so(abs(tp1))}+{phan_so(abs(tp2))}={phan_so(abs(tp1)+abs(tp2))}$.\n\n")
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

    debai_latex=debai_latex.replace(file_name,f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C4_B5_33]-TF-M3. Xét Đ-S: diện tích giới hạn bởi y=e^x, x=a,x=k,x=b.
def ckz_L12C4_B5_33():
    x,k=sp.symbols("x k")
    d_x=f"\\mathrm{{\\,d}}x"
    a=random.randint(-4,2)
    b=a+random.randint(1,4)

    noi_dung =(
        f"Gọi $S_1$ là diện tích hình phẳng giới hạn bởi các đường $y=e^x,x={a},x=k,y=0$.\n\n"
        f" Gọi $S_2$ là diện tích hình phẳng giới hạn bởi các đường $y=e^x,x=k,x={b},y=0$.\n\n"
        f" Gọi ${{S}}$ là diện tích hình phẳng giới hạn bởi các đường $y=e^x,x={a},x={b},y=0$.\n\n"
        f" Gọi ${{V}}$ là thể tích khối tròn xoay khi quay ${{S}}$ quanh trục ${{Ox}}$.\n\n"
        f" Biết ${a}<k<{b}$. Xét tính đúng-sai của các khẳng định sau:" )      
    debai_word= f"{noi_dung}\n"
    S=integrate(exp(x),(x,a,b))
    S_false=integrate(exp(x),(x,a,b+1))
    
    kq1_T=f"* $S={latex(S)}$" 
    kq1_F=f"$S={latex(S_false)}$"
    
    HDG=f"$S={tphan(a,b)} e^x {d_x}=e^x\\bigg|_{{{a}}}^{{{b}}}={latex(S)}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    V=pi*integrate(exp(2*x),(x,a,b))
    V_false=pi*integrate(exp(x),(x,a,b))
    kq2_T=f"* $V={latex(V)}$"
    kq2_F=f"$V={latex(V_false)}$"
    
    HDG=f"$V=\\pi{tphan(a,b)}e^{{2x}}{d_x}=\\pi.{phan_so(1/2)}e^{{2x}}\\bigg|_{{{a}}}^{{{b}}}={latex(V)}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,3)
    if chon==1:
        kq3_T=f"* $S_1=S-{tphan("k",b)}e^x{d_x}$" 
        kq3_F=f"$S_1=S-{tphan(b,"k")}e^x{d_x}$"
        
        HDG=f"$S_1=S-{tphan("k",b)}e^x{d_x}$."
    
    if chon==2:
        kq3_T=f"* $S_2=S-{tphan(a,"k")}e^x{d_x}$" 
        kq3_F=f"$S_2=S-{tphan("k",a)}e^x{d_x}$"
        
        HDG=f"$S_2=S-{tphan(a,"k")}e^x{d_x}$."

    if chon==3:
        kq3_T=f"* $S=S_1+S_2$" 
        kq3_F=f"$S=S_1-S_2$"
        
        HDG=f"$S=S_1+S_2$."    

    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m=random.randint(1,3)

    eq = Eq(exp(b)-exp(k),m*(exp(k)-exp(a)))    
    solution = solve(eq, k)

    k=solution[0]
    k_false=solution[0]+random.randint(1,2)
    kq4_T=f"* Với $k={latex(k)}$ thì $S_2={m}S_1$"
    kq4_F=f"Với $k={latex(k_false)}$ thì $S_2={m}S_1$"
    
    HDG=(f"$S_2={m}S_1\\Rightarrow {tphan("k",b)}e^x{d_x}={m}{tphan(a,"k")}e^x{d_x}$"
        f"$\\Rightarrow e^{{{b}}}-e^k={m}(e^k-e^{{{a}}})$\n\n"
        f"$\\Rightarrow k={latex(k)}$.")
    if m==1:
        kq4_T=f"* Với $k={latex(k)}$ thì $S_2=S_1$"
        kq4_F=f"Với $k={latex(k_false)}$ thì $S_2=S_1$"
        
        HDG=(f"$S_2={m}S_1\\Rightarrow {tphan("k",b)}e^x{d_x}={tphan(a,"k")}e^x{d_x}$"
            f"$\\Rightarrow e^{{{b}}}-e^k=(e^k-e^{{{a}}})$\n\n"
            f"$\\Rightarrow k={latex(k)}$.")

    kq4=random.choice([kq4_T, kq4_F])
    kq4=kq4.replace("\\log", "\\ln")
    HDG=HDG.replace("\\log", "\\ln")

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

#[D12_C4_B5_34]-TF-M3. Cho 2 chất điểm chuyển động ngược chiều. Xét Đ-S: hàm số quãng đường, quãng đường đi được, khoảng cách giữa 2 chất điểm
def ckz_L12C4_B5_34():
    while True:
        t1=random.randint(2,6)
        a1=random.randint(1,4)
        b1=a1*t1

        t2=random.randint(2,7)
        a2=random.randint(1,5)
        b2=a2*t2

        if all([t1!=t2, a1!=a2]):
            break    
    t=sp.symbols("t")
    v1=b1-a1*t
    v2=b2-a2*t


    noi_dung =(f"Hai chất điểm chuyển động ngược chiều nhau thì xảy ra va chạm, hai chất điểm tiếp tục di"
f" chuyển theo chiều ban đầu thêm một quãng đường nữa thì dừng hẳn."
f" Biết rằng sau khi va chạm, một chất điểm di chuyển tiếp với vận tốc $v_1(t)={latex(v1)}$,"
f" chất điểm còn lại di chuyển với vận tốc $v_2(t)={latex(v2)}$."
 f" Xét tính đúng-sai của các khẳng định sau." )      
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm được biểu diễn bởi hàm số $s_1(t)={latex(integrate(v1,t))}+C$" 
    kq1_F=f"Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm được biểu diễn bởi hàm số $s_1(t)={latex(integrate(v1,t)+random.randint(1,2)*t)}+C$"
    
    HDG=(f"Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm được biểu diễn bởi hàm số:\n\n"
    f" $s_1(t)=\\int ({latex(v1)})dt={latex(integrate(v1,t))}+C$.")
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm được biểu diễn bởi hàm số $s_2(t)={latex(integrate(v2,t))}+C$" 
    kq2_F=f"Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm được biểu diễn bởi hàm số $s_1(t)={latex(integrate(v2,t)+random.randint(1,2)*t)}+C$"
    
    HDG=(f"Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm được biểu diễn bởi hàm số:\n\n"
    f" $s_2(t)=\\int ({latex(v2)})dt={latex(integrate(v2,t))}+C$.")
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    s1=integrate(v1,(t,0,t1))

    kq3_T=f"* Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm là ${{{phan_so(s1)}}}$ m" 
    kq3_F=f"Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm là ${{{phan_so(s1+random.randint(1,2))}}}$ m"
    
    HDG=(f" Thời gian để chất điểm thứ nhất dừng lại là: ${latex(v1)}=0\\Rightarrow t={t1}$.\n\n"
        f"Quãng đường chất điểm thứ nhất di chuyển sau khi va chạm là:\n\n ${tphan(0,t1)}({latex(v1)})dt={phan_so(s1)}$ m.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    s2=integrate(v2,(t,0,t2))
    kq4_T=f"* Khoảng cách hai chất điểm khi đã dừng hẳn là ${phan_so(s1+s2)}$ m"
    kq4_F=f"Khoảng cách hai chất điểm khi đã dừng hẳn là ${phan_so(abs(s1-s2))}$ m" 
    
    HDG=(f" Thời gian để chất điểm thứ hai dừng lại là: ${latex(v2)}=0\\Rightarrow t={t2}$.\n\n"
        f"Quãng đường chất điểm thứ hai di chuyển sau khi va chạm là:\n\n ${tphan(0,t2)}({latex(v2)})dt={phan_so(s2)}$ m.\n\n"
        f"Khoảng cách hai chất điểm khi đã dừng hẳn: ${phan_so(s1)}+{phan_so(s2)}={phan_so(s1+s2)} m.$")

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

#[D12_C4_B5_35]-TF-M3. Bài toán về oto. Xét Đ-S: vận tốc, gia tốc, tìm v(t_0), tìm t để đi được quãng đường s
def ckz_L12C4_B5_35():
    t=sp.symbols("t")

    v=random.randint(2,4)*18
    v_met=int(v*5/18)
    t1=random.randint(2,4)
    s1=v_met*t1

    a=random.randint(3,6)

    v_t=a*t+v_met
    t2=random.choice([4,6,8,10])
    s2=integrate(v_t,(t,0,t2))
    s_tong=s1+s2
    s_round=f"{round_half_up(s_tong,1):.1f}".replace(".",",")

    noi_dung = (
        f"Một người điều khiển ô tô với tốc độ không đổi của ô tô là {v} km/h trên quãng đường dài {s_tong}m."
        f" Sau {t1} giây thì ô tô bắt đầu tăng tốc với gia tốc không đổi $a(a\\in \\mathbb{{R}}, a>0)$"
        f" trong đó ${{t}}$ là thời gian tính bằng giây kể từ khi bắt đầu tăng tốc."
        f" Biết rằng ô tô đi hết quãng đường trên trong {t2} giây."
        f" Xét tính đúng-sai của các khẳng định sau. "  )      
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* Vận tốc của ô tô vào thời điểm bắt đầu tăng tốc là ${{{phan_so(v_met)}}}$ m/s" 
    kq1_F=f"Vận tốc của ô tô vào thời điểm bắt đầu tăng tốc là ${{{phan_so(v_met+random.randint(1,2))}}}$ m/s"
    
    HDG=(f"Đổi {v} km/h = {v}. $\\dfrac{{5}}{{18}}$ m/s $= {phan_so(v_met)}$ m/s.\n\n"
        f"Gia tốc của vật là ${{a}}$ nên phương trình vận tốc của vật là: $v(t)=at+C$.\n\n"
        f"Do ô tô đang có tốc độ là ${{{phan_so(v_met)}}}$ m/s và bắt đầu tăng tốc nên $v(0)=C={phan_so(v_met)}$."

        )
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Gia tốc của ô tô là ${{{a}m/s^2}}$"
    kq2_F=f" Gia tốc của ô tô là ${{{a+random.randint(1,4)}m/s^2}}$"
    
    HDG=(f"Quãng đường ô tô đi được khi bắt đầu tăng tốc là: ${s_tong}-{phan_so(v_met)}.{t1}={s2}$ m.\n\n"
        f" Ta có: ${tphan(0,t2)}(at+{v_met})dt={s2}$\n\n"
        f"$\\Rightarrow a{tphan(0,t2)} tdt+{tphan(0,t2)}{v_met}dt={s2}\\Rightarrow a={a}$."
   
        )
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    t_3=random.randint(5,10)
    v_3=a*t_3+v_met
    v_3_cong=v_3+random.randint(1,5)
    kq3_T=f"* Kể từ lúc bắt đầu tăng tốc, sau {t_3} giây vận tốc của ô tô không vượt quá {v_3_cong} m/s" 
    kq3_F=f"Kể từ lúc bắt đầu tăng tốc, sau {t_3} giây vận tốc của ô tô lớn hơn {v_3_cong} m/s"
    
    HDG=(f"Ta có: $v(t)={a}t+{v_met}$.\n\n"
        f"$v(t) \\le {v_3_cong}\\Rightarrow {a}t+{v_met}\\le {v_3_cong} \\Rightarrow t\\le {phan_so((v_3_cong-v_met)/a)}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    t_4=random.randint(8,15)
    s_4=integrate(v_t,(t,0,t_4))
    s_4_km=f"{round_half_up(s_4/1000,4):.4f}".replace(".",",")

    kq4_T=f"* Kể từ lúc bắt đầu tăng tốc, thời gian để ô tô đi được quãng đường {s_4_km} km là {t_4} giây"
    kq4_F=f"Kể từ lúc bắt đầu tăng tốc, thời gian để ô tô đi được quãng đường {s_4_km} km là {t_4-random.randint(1,3)} giây" 
    
    HDG=(f"${s_4_km}km={phan_so(s_4)}m$.\n\n"
        f" Quãng đường đi được là: ${tphan(0,"t_2")}({latex(v_t)})dt={s_4}\\Rightarrow ({phan_so(a/2)}t^2+{v_met}t)\\bigg|^{{t_2}}_0={s_4}$\n\n"
        f"$\\Rightarrow {phan_so(a/2)}t_2^2+{v_met}t_2={s_4} \\Rightarrow {phan_so(a/2)}t_2^2+{v_met}t_2-{s_4}=0\\Rightarrow t_2={t_4}$.")
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

#[D12_C4_B5_36]-SA-M3. Tính diện tích cánh hoa trong hình vuông
def ckz_L12C4_B5_36():
    x=sp.symbols("x")
    a=random.randint(2,10)
    b=a*2
    S=8*integrate(x-x**2/a,(x,0,a))

    code_hinh=f"\\begin{{tikzpicture}}[>=stealth, line join=round,line cap=round,scale=0.9]\n\
    \\foreach \\i in {{0,90,180,270}}\n\
    \\draw [rotate=\\i, fill=gray,smooth, samples=200] (0,0)-- plot [domain=0:2] (\\x, {{0.5*(\\x)^2}}) -- plot [domain=2:0](\\x, {{sqrt(2*\\x)}})--cycle;\n\
    \\draw (-2,-2) rectangle (2,2);\n\
    \\end{{tikzpicture}}"
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    code_hinh_LG=f"\\begin{{tikzpicture}}[>=stealth, line join=round,line cap=round,scale=0.9]\n\
    \\foreach \\i in {{0,90,180,270}}\n\
    \\draw [rotate=\\i, fill=gray,smooth, samples=200] (0,0)-- plot [domain=0:2] (\\x, {{0.5*(\\x)^2}}) -- plot [domain=2:0](\\x, {{sqrt(2*\\x)}})--cycle;\n\
    \\draw (-2,-2) rectangle (2,2);\n\
    \\draw[->] (-2.2,0) -- (2.2,0) node[below right] {{$x$}};\n\
    \\draw[->] (0,-2.2) -- (0,2.2) node[above left] {{$y$}};\n\
    \\draw[dashed, thick, red] (-2,-2) -- (2,2) node[above right] {{$y = x$}};\n\
    \\end{{tikzpicture}}"
    code = my_module.moi_truong_anh_latex(code_hinh_LG)
    file_name_LG=my_module.pdftoimage_timename(code)

    if S.is_integer:
        noi_dung = (
        f"Một viên gạch hoa hình vuông có cạnh bằng ${b}$ cm. Người ta thiết kế sử dụng 4 đường parabol cùng chung đỉnh tại tâm của viên gạch và đi qua hai đỉnh kề nhau của viên gạch để tạo thành bông hoa như hình vẽ. Diện tích của bông hoa (phần tô đậm trong hình vẽ) là."
        )
        dap_an=S
        noi_dung_loigiai=(
        f"Chọn hệ trục tọa độ $(Oxy)$ sao cho ${{O}}$ là tâm của hình vuông.\n\n"
        f" Xét cánh hoa thuộc góc phần tư thứ nhất.\n\n"
        f" Cánh hoa được tạo bởi đường thẳng $y=x$ và parabol $y=mx^2 (P)$.\n\n"
        f" $(P)$ qua A({a};{a}) nên: ${a}=m.{a}^2\\Rightarrow m={phan_so(1/a)}$.\n\n"
        f" Suy ra $(P):y={phan_so(1/a)}x^2$.\n\n"
        f" Diện tích của bông hoa là:\n\n"
        f"$S=4.2{tphan(0,a)} (x-\\dfrac{{x^2}}{{{a}}})={dap_an}$."
        )  
    else:
        noi_dung = (
        f"Một viên gạch hoa hình vuông có cạnh bằng ${b}$ cm. Người ta thiết kế sử dụng 4 đường parabol cùng chung đỉnh tại tâm của viên gạch và đi qua hai đỉnh kề nhau của viên gạch để tạo thành bông hoa như hình vẽ. Diện tích của bông hoa (phần tô đậm trong hình vẽ) là (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round_half_up(S,1):.1f}".replace(".",",")
        noi_dung_loigiai=(
        f"Chọn hệ trục tọa độ $(Oxy)$ sao cho ${{O}}$ là tâm của hình vuông.\n\n"
        f" Xét cánh hoa thuộc góc phần tư thứ nhất.\n\n"
        f" Cánh hoa được tạo bởi đường thẳng $y=x$ và parabol $y=mx^2 (P)$.\n\n"
        f" $(P)$ qua A({a};{a}) nên: ${a}=m.{a}^2\\Rightarrow m={phan_so(1/a)}$.\n\n"
        f" Suy ra $(P):y={phan_so(1/a)}x^2$.\n\n"
        f" Diện tích của bông hoa là:\n\n"
        f"$S=4.2{tphan(0,a)} (x-\\dfrac{{x^2}}{{{a}}})={phan_so(S)}={dap_an}$.")  
       
    debai_word= f"{noi_dung}\n{file_name}"

    loigiai_word=(f"Lời giải:\n {file_name_LG}\n{noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n \\begin{{center}}\n{code_hinh_LG}\n\\end{{center}}\n}}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C4_B5_37]-TF-M3. Cho đường gấp khúc. Xét Đ-S: tích phân các đoạn, diện tích
def ckz_L12C4_B5_37():
    x=sp.symbols("x")
    x_1=random.randint(-4,-1)
    x_2=x_1+random.randint(1,3)
    x_3=x_2+random.randint(1,2)
    x_4=2*x_3-x_2
    y_1=random.randint(1,3)
    y_4=-y_1

    st=""
    for i in range(x_1,x_4+1):
        if all([i!=0, i!=x_4]):
            st+=f"{i},"

    code_hinh=f" \\begin{{tikzpicture}}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n\
            \\tikzset{{label style/.style={{font=\\footnotesize}}}}\n\
            \\def \\xmin{{{x_1-0.5}}}\\def \\xmax{{{x_4+0.5}}}\\def \\ymin{{{y_4-0.5}}}\\def \\ymax{{{y_1+1}}}\n\
            \\draw[->] (\\xmin,0)--(\\xmax,0) node[shift=(-90:0.25)] {{$x$}};\n\
            \\draw[->] (0,\\ymin)--(0,\\ymax) node[shift=(0:0.25)] {{$y$}};\n\
            \\foreach \\x in {{{st}}}\n\
            \\fill[black] (\\x,0) node[below]{{$\\x$}}circle(1pt);\n\
            \\fill[black]\n\
            (0,0) node [below left]{{$O$}} circle(1pt)\n\
            ({x_4},0)node [above]{{${x_4}$}} circle(1pt)\n\
            (0,{y_4})node [left]{{${y_4}$}} circle(1pt)\n\
            (0,{y_1})node [above left]{{${y_1}$}} circle(1pt)\n\
            ;\n\
            \\draw[dashed] ({x_4},0)|-(0,{y_4}) ({x_1},0)--({x_1},{y_1}) ({x_2},0)--({x_2},{y_1});\n\
            \\draw[thick] ({x_1},{y_1})node[above]{{$A$}}--({x_2},{y_1})node[above]{{$B$}}--({x_4},{y_4})node[below]{{$C$}};\n\
        \\end{{tikzpicture}} "
    if x_4+0.5<=0:
        code_hinh=f" \\begin{{tikzpicture}}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n\
            \\tikzset{{label style/.style={{font=\\footnotesize}}}}\n\
            \\def \\xmin{{{x_1-0.5}}}\\def \\xmax{{1.5}}\\def \\ymin{{{y_4-0.5}}}\\def \\ymax{{{y_1+1}}}\n\
            \\draw[->] (\\xmin,0)--(\\xmax,0) node[shift=(-90:0.25)] {{$x$}};\n\
            \\draw[->] (0,\\ymin)--(0,\\ymax) node[shift=(0:0.25)] {{$y$}};\n\
            \\foreach \\x in {{{st}}}\n\
            \\fill[black] (\\x,0) node[below]{{$\\x$}}circle(1pt);\n\
            \\fill[black]\n\
            (0,0) node [below left]{{$O$}} circle(1pt)\n\
            ({x_4},0)node [above]{{${x_4}$}} circle(1pt)\n\
            (0,{y_4})node [left]{{${y_4}$}} circle(1pt)\n\
            (0,{y_1})node [above left]{{${y_1}$}} circle(1pt)\n\
            ;\n\
            \\draw[dashed] ({x_4},0)|-(0,{y_4}) ({x_1},0)--({x_1},{y_1}) ({x_2},0)--({x_2},{y_1});\n\
            \\draw[thick] ({x_1},{y_1})node[above]{{$A$}}--({x_2},{y_1})node[above]{{$B$}}--({x_4},{y_4})node[below]{{$C$}};\n\
        \\end{{tikzpicture}} "

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)


    noi_dung = (
    f"Đường gấp khúc ${{ABC}}$ trong hình bên là đồ thị của hàm số $y=f(x)$ trên đoạn ${{[{x_1};{x_4}]}}$. Xét tính đúng-sai của các khẳng định sau. "
    )

    solve1=integrate(y_1,(x,x_1,x_2))
    solve1_f= integrate(y_1,(x,x_1,x_2))+random.randint(1,3)  
    
    kq1_T=f"* Tích phân ${tphan(x_1,x_2)} f(x)dx$ bằng ${{{solve1}}}$" 
    kq1_F=f"Tích phân ${tphan(x_1,x_2)} f(x)dx$ bằng ${{{solve1_f}}}$"
    
    HDG=f"${tphan(x_1,x_2)} f(x)dx = {tphan(x_1,x_2)} {y_1}dx={solve1}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    solve2=1/2*(x_3-x_2)*y_1
    solve2_f= 1/2*(x_3-x_2)*y_1+random.randint(1,3) 

    kq2_T=f"* Tích phân ${tphan(x_2,x_3)} f(x)dx$ bằng ${{{phan_so(solve2)}}}$"
    kq2_F=f"Tích phân ${tphan(x_2,x_3)} f(x)dx$ bằng ${{{phan_so(solve2_f)}}}$"
    
    HDG=f"${tphan(x_2,x_3)} f(x)dx = {phan_so(1/2)}.{x_3-x_2}.{y_1}={phan_so(solve2)}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    kq3_T=f"* Tích phân ${tphan(x_2,x_4)} f(x)dx$ bằng ${{{phan_so(2*solve2)}}}$" 
    kq3_F=f" Tích phân ${tphan(x_2,x_4)} f(x)dx$ bằng ${{{phan_so(2*solve2+random.randint(1,2))}}}$"
    
    HDG=f"${tphan(x_2,x_4)} f(x)dx = 2.{tphan(x_2,x_3)}f(x)d(x)={phan_so(2*solve2)}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    S=solve1+2*solve2

    kq4_T=f"* Diện tích hình phẳng giới hạn bởi đồ thị $y=f(x)$, trục Ox, các đường thẳng $x={x_1},x={x_4}$ bằng ${phan_so(S)}$"
    kq4_F=f"Diện tích hình phẳng giới hạn bởi đồ thị $y=f(x)$, trục Ox, các đường thẳng $x={x_1},x={x_4}$ bằng ${phan_so(S+random.randint(1,3))}$" 
    
    HDG=f"$S={tphan(x_1,x_2)}f(x)+2{tphan(x_2,x_3)}f(x)dx={phan_so(solve1)}+2.{phan_so(solve2)}={phan_so(S)}$."
    kq4=random.choice([kq4_T, kq4_F])
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