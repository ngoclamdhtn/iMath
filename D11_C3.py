import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

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

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(10000000000000))
    return m
def st_lim(x_0):
    return f"\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}}"


################ Bài 1: GIỚI HẠN DÃY SỐ #################

#[D11_C3_B1_01]. Tính giới hạn phân thức bậc tử bằng mẫu.
def gh11gh_L11_C3_B1_01():
    #Tạo bậc ngẫu nhiên
    bac = random.randint(2,5)
    #Tạo hai đa thức biến n với bậc ngẫu nhiên
    f, heso_bac_f, heso_tudo_f= my_module.random_polynomial("n", bac)[0:3] 
    g, heso_bac_g, heso_tudo_g = my_module.random_polynomial("n", bac)[0:3]

    kq=heso_bac_f/heso_bac_g
    kq2=heso_bac_f/heso_tudo_g
    kq3=heso_tudo_f/heso_tudo_g
    kq4=heso_bac_g/heso_tudo_f

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3] 

    #Tạo các phương án
    pa_A= f"*${{ {latex(kq)}}}$"
    pa_B= f"$ {{{latex(kq2)}}}$"
    pa_C= f"$ {{ {latex(kq3)}}}$"
    pa_D= f"$ {{{latex(kq4)}}}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính giới hạn $\\lim{latex(f/g)}$."
    noi_dung_loigiai=f""
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

#[D11_C3_B1_02]. Tính giới hạn phân thức bậc tử nhỏ hơn mẫu.
def gh11gh_L11_C3_B1_02():
    #Tạo bậc ngẫu nhiên
    bac = random.randint(3,5)
    k= random.randint(2, bac-1)
    #Tạo hai đa thức biến n với bậc ngẫu nhiên
    f, heso_bac_f, heso_tudo_f= my_module.random_polynomial("n", k)[0:3] 
    g, heso_bac_g, heso_tudo_g = my_module.random_polynomial("n", bac)[0:3]
    if heso_tudo_g==0:
        heso_tudo_g=heso_bac_f+ random.randint(3,5)
    if heso_tudo_f==0:
        heso_tudo_f=heso_bac_g+ random.randint(3,7)

    kq=0
    kq2=heso_bac_f/heso_tudo_g
    kq3=heso_tudo_f/heso_tudo_g
    kq4=heso_bac_g/heso_tudo_f

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]   
 

    #Tạo các phương án
    pa_A= f"*${{{kq}}}$"
    pa_B= f"$ {{{latex(kq2)}}}$"
    pa_C= f"$ {{ {latex(kq3)}}}$"
    pa_D= f"$ {{{latex(kq4)}}}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính giới hạn $\\lim{latex(f/g)}$."
    
    noi_dung_loigiai=f""
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
#[D11_C3_B1_03]. Tính giới hạn phân thức có tử chứa căn.
def gh11gh_L11_C3_B1_03():

    #Tạo hai đa thức biến n với bậc ngẫu nhiên
    f, heso_bac_f, heso_tudo_f= my_module.random_dathuc_bac2_luon_duong("n")[0:3] 
    g, heso_bac_g, heso_tudo_g = my_module.random_polynomial("n", 2)[0:3]
    if heso_tudo_g==0:
        heso_tudo_g =random.randint(1,10)
    
    kq=sqrt(heso_bac_f)/heso_bac_g
    kq2=heso_bac_f/heso_bac_g
    kq3=heso_tudo_f/heso_tudo_g
    kq4=sqrt(heso_bac_f+1)/heso_tudo_g

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]   

    #Tạo các phương án
    pa_A= f"*${{{latex(kq)}}}$"
    pa_B= f"$ {{{latex(kq2)} }}$"
    pa_C= f"$ {{ {latex(kq3)}}}$"
    pa_D= f"$ {{{latex(kq4)} }}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính giới hạn $\\lim{latex(sqrt(f)/g)}$."

    noi_dung_loigiai=f""
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

#[D11_C3_B1_04]. Tính giới hạn phân thức chứa lũy thừa.
def gh11gh_L11_C3_B1_04():
    #Tạo list chứa các hệ số
    a = [random.randint(-10, 10) for _ in range(4)]
    for i in range (4):
        if a[i] == 0:
            a[i] = a[i] + 1
    x = random.randint(2, 6)
    y = random.randint(x+1, x+2)
    z = random.randint(y, x+3)
    n = sp.symbols('n')
    f = a[0]*x**n + a[1]*z**n
    g = a[3]*z**n + a[2]
    
    kq=a[1]/a[3]
    kq2=a[0]/a[2]
    kq3=a[1]+a[3]
    kq4=a[2]/a[1]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
    #Tạo các phương án
    pa_A= f"*${{{latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"$ {{{latex(my_module.hien_phan_so(kq2))} }}$"
    pa_C= f"$ {{ {latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"$ {{{latex(my_module.hien_phan_so(kq4))} }}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính giới hạn $\\lim{latex(f/g)}$. "

    noi_dung_loigiai=f""
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

#[D11_C3_B1_05]. Tính tổng cấp số nhân lùi vô hạn có u1=1.
def gh11gh_L11_C3_B1_05():
    #Tạo list chứa các hệ số
    a =random.choice([random.randint(-10, -2),random.randint(2, 10)])
    q=1/a
    dau ="+"
    if q<0: 
        dau=""
    
    #Tạo các phương án
    pa_A= f"*${{ {latex(my_module.hien_phan_so(1/(1-q)))} }}$"
    pa_B= f"$ {{{latex(my_module.hien_phan_so(1/(1+q)))} }}$"
    pa_C= f"$ {{ {latex(my_module.hien_phan_so(1+1/q))}}}$"
    pa_D= f"$ {{{latex(my_module.hien_phan_so(1-1/q))} }}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    noi_dung= f"Tính tổng của cấp số nhân lùi vô hạn $S=1{dau}{latex(my_module.hien_phan_so(q))} + {latex(my_module.hien_phan_so(q**2))}+...+\\left({latex(my_module.hien_phan_so(q))}\\right)^n+...$."

    noi_dung_loigiai=f""
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
    

#[D11_C3_B1_06]. Tính tổng cấp số nhân lùi vô hạn có u1 tùy ý.
def gh11gh_L11_C3_B1_06():
    n = symbols('n')
    b = random.randint(2,9)
    q=1/b
    u1 = random.choice([random.randint(-5,-2), random.randint(1,5)])
    if u1==b or u1 == -b: 
        u1=u1+1
    u2=u1*q
    u3=u1*q**2
    dau ="+"
    if u1*q<0: 
        dau = ""
    dau_ngoac_mo = "("
    dau_ngoac_dong = ")"
    if u1>0:
        dau_ngoac_mo = ""
        dau_ngoac_dong = ""

    #Tạo các phương án
    pa_A= f"*${{{latex(my_module.hien_phan_so(u1/(1-q)))}}}$"
    pa_B= f"$ {{{latex(my_module.hien_phan_so(u1/(1+q)))} }}$"
    pa_C= f"$ {{{latex(my_module.hien_phan_so(u1/q))} }}$"
    pa_D= f"$ {{{latex(my_module.hien_phan_so(q/(1-2*u1)))} }}$"
    #Trộn các phương án        
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính tổng của cấp số nhân lùi vô hạn $S={latex(my_module.hien_phan_so(u1))}{dau}{latex(my_module.hien_phan_so(u2))}+...+{dau_ngoac_mo}{latex(my_module.hien_phan_so(u1))}{dau_ngoac_dong}\\left({latex(my_module.hien_phan_so(q))}\\right)^n+..$."

    noi_dung_loigiai=f""
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

#[D11_C3_B1_07]. Cho giới hạn của (u_n) và (v_n). Tính giới hạn tổng hiệu.
def gh11gh_L11_C3_B1_07():
    #Tạo list chứa các hệ số
    u_n = random.randint(-10,15)
    if u_n ==0:
        u_n = random.randint(3,15)

    v_n = random.randint(-10,15)
    if v_n ==0:
        v_n = random.randint(-10,-1)
    if v_n==u_n:
        v_n=u_n + random.randint(2,10)
    
    dau =random.choice(["+","-"])
    if dau =="+":
        kq= u_n+v_n
        kq2=u_n-v_n
        kq3=u_n*v_n 
        kq4=v_n-u_n
    else:
        kq= u_n-v_n
        kq2=v_n-u_n
        kq3=u_n+v_n 
        kq4=u_n*v_n

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
    
    #Tạo các phương án
    pa_A= f"*${{ {latex(my_module.hien_phan_so(kq))} }}$"
    pa_B= f"$ {{{latex(my_module.hien_phan_so(kq2))} }}$"
    pa_C= f"$ {{ {latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"$ {{{latex(my_module.hien_phan_so(kq4))} }}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    noi_dung= f"Cho hai dãy số $(u_n)$ và $(v_n)$ có $\\lim u_n ={u_n}$ và $\\lim v_n ={v_n}$. Tính giới hạn $\\lim (u_n{dau}v_n)$."

    noi_dung_loigiai=f""
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

#[D11_C3_B1_08]-TF-M3. Cho (u_n) và (v_n). Xét Đ-S: lim(u/v), lim(u/v^2), lim(u^2/v), lim (u+m)/(v+n)
def gh11gh_L11_C3_B1_08():
    n=sp.symbols("n")
    a1 = random.choice([i for i in range(-5, 5) if i!=0])
    b1 = random.choice([i for i in range(-8, 8) if i!=0])
    c1 = random.choice([i for i in range(-7, 7) if i!=0])
    u=a1*n**2+b1*n+c1

    a2 = random.choice([i for i in range(-5, 5) if i!=0])    
    b2 = random.randint(-8,8)
    c2 = random.choice([i for i in range(-8, 8) if i!=0])
    v=a2*n**2+b2*n+c2


    noi_dung = f"Cho hay dãy số $(u_n)$ và $(v_n)$ có $u_n={latex(u)},v_n={latex(v)}$. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* $\\lim \\dfrac{{u_n}}{{v_n}}={phan_so(a1/a2)}$"
    if c1/c2!=a1/a2:
        kq1_F=f"$\\lim \\dfrac{{u_n}}{{v_n}}={phan_so(c1/c2)}$"
    else:
        kq1_F=f"$\\lim \\dfrac{{u_n}}{{v_n}}={phan_so(a1/a2+random.randint(1,2))}$"

    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f" $\\lim \\dfrac{{u_n}}{{v_n}}=\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}\n"
    f"=\\lim \\dfrac{{{latex(a1+b1/n+c1/n**2)}}}{{{latex(a2+b2/n+c2/n**2)}}}={phan_so(a1/a2)}$.")
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* $\\lim \\dfrac{{u_n}}{{(v_n)^2}}=0$"
    kq2_F=f"$\\lim \\dfrac{{u_n}}{{(v_n)^2}}={phan_so(a1/a2**2)}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=(f"$\\lim \\dfrac{{u_n}}{{(v_n)^2}}=\\lim \\dfrac{{{latex(u)}}}{{{latex(v**2)}}}$\n"
        f"$=\\lim \\dfrac{{{latex(n**2*(a1+b1/n+c1/n**2))}}}{{{latex(n**2*(a2+b2/n+c2/n**2)**2)}}}$\n"
        f"$=\\lim \\dfrac{{{latex((a1+b1/n+c1/n**2))}}}{{{latex((a2+b2/n+c2/n**2)**2)}}}=0$.")
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)    
    if chon==1:
        m=random.choice([i for i in range(-5, 6) if i!=0])
        if a1+m==0: m=m+random.randint(1,2)
        if m==0:m=m+1

        kq3_T=f"*$\\lim \\dfrac{{u_n+{latex(m*n**2)}}}{{v_n}}={phan_so((a1+m)/a2)}$".replace("+-","-")
        kq3_F=f"$\\lim \\dfrac{{u_n+{latex(m*n**2)}}}{{v_n}}={phan_so((a1+m**2)/a2)}$".replace("+-","-")
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f"$\\lim \\dfrac{{u_n+{latex(m*n**2)}}}{{v_n}}=\\lim \\dfrac{{{latex(u)}+{latex(m*n**2)}}}{{{latex(v)}}}$\n"
            f"$=\\lim \\dfrac{{{latex(u+m*n**2)}}}{{{latex(v)}}}$\n"
             f"$=\\lim \\dfrac{{{latex(a1+m+b1/n+c1/n**2)}}}{{{latex(a2+b2/n+c2/n**2)}}}={phan_so((a1+m)/a2)}$.")

    if chon==2:
        m=random.choice([i for i in range(-5, 6) if i!=0])
        if a2+m==0: m=m+random.randint(1,2)
        if m==0:m=m+1

        kq3_T=f"*$\\lim \\dfrac{{u_n}}{{v_n+{latex(m*n**2)}}}={phan_so(a1/(a2+m))}$".replace("+-","-")
        kq3_F=f"$\\lim \\dfrac{{u_n}}{{v_n+{latex(m*n**2)}}}={phan_so((a1+m)/a2)}$".replace("+-","-")
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f"$\\lim \\dfrac{{u_n}}{{v_n+{latex(m*n**2)}}}=\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}+{latex(m*n**2)}}}$\n"
            f" $=\\lim \\dfrac{{{latex(u)}}}{{{latex(v+m*n**2)}}}$\n"
             f"$=\\lim \\dfrac{{{latex(a1+b1/n+c1/n**2)}}}{{{latex(a2+m+b2/n+c2/n**2)}}}={phan_so(a1/(a2+m))}$.")
    
    
    HDG=HDG.replace("+-","-")
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m=random.choice([i for i in range(-5, 6) if i!=0])
    if a1+m==0: m=m+random.randint(1,2)
    if m==0:m=m+1
    k1=random.choice([i for i in range(-5, 6) if i!=0])
    k2=random.choice([i for i in range(-5, 6) if i!=0])
    t=random.choice([i for i in range(-7, 7) if i!=0])

    kq4_T=f"*Với $m={m}$ thì $\\lim \\dfrac{{u_n+mn^2+{k1}}}{{v_n+{k2}}}={phan_so((a1+m)/a2)}$".replace("+-","-")
    kq4_F=f"Với $m={m+random.randint(1,5)}$ thì $\\lim \\dfrac{{u_n+mn^2+{k1}}}{{v_n+{k2}}}={phan_so((a1+m)/a2)}$".replace("+-","-") 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"$\\lim \\dfrac{{u_n+mn^2+{k1}}}{{v_n+{k2}}}={phan_so((a1+m)/a2)}$\n"
        f"$\\Rightarrow \\lim \\dfrac{{{latex(u)}+mn^2+{k1}}}{{{latex(v)}+{k2}}}={phan_so((a1+m)/a2)}$\n"
        f"$\\Rightarrow \\dfrac{{{a1}+m}}{{{a2}}}={phan_so((a1+m)/a2)}$\n"
        f"$\\Rightarrow m={m}$."
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

#[D11_C3_B1_09]-TF-M2. Xét Đ-S: lim a/n^k, lim q^n, lim P(n)/Q(n), lim (u+m)/(v+n)
def gh11gh_L11_C3_B1_09():
    n=sp.symbols("n")
    noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    chon=random.randint(1,2)    
    if chon==1:
        a = random.choice([i for i in range(-100, 100) if i!=0])
        k=random.randint(1,5)

        kq1_T=f"* $\\lim \\left({latex(a/n**k)}\\right)=0$" 
        kq1_F=f"$\\lim \\left({latex(a/n**k)}\\right)={random.choice([a,-a,phan_so(a/k)])}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"$\\lim \\left({latex(a/n**k)}\\right)=\\lim \\left({a}.{latex(1/n**k)}\\right)=0$."
    
    if chon==2:
        a = random.choice([i for i in range(-20, 30) if i!=0])
        k=random.randint(1,5)
        if a>0:
            kq1_T=f"* $\\lim \\left({latex(a*n**k)}\\right)=+\\infty$" 
            kq1_F=f"$\\lim \\left({latex(a*n**k)}\\right)={random.choice([a,-a,phan_so(a/k),"-\\infty"])}$"
            HDG=f"$\\lim \\left({latex(a*n**k)}\\right)=+\\infty$ vì $a>0$."
        if a<0:
            kq1_T=f"* $\\lim \\left({latex(a*n**k)}\\right)=-\\infty$" 
            kq1_F=f"$\\lim \\left({latex(a*n**k)}\\right)={random.choice([a,-a,phan_so(a/k),"+\\infty"])}$"
            HDG=f"$\\lim \\left({latex(a*n**k)}\\right)=-\\infty$ vì $a<0$."

        kq1=random.choice([kq1_T, kq1_F])
    
    
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,3)

    if chon==1:
        a=random.randint(1,15)
        b=a+random.randint(1,7)
        q=a/b
        
        kq2_T=f"* $\\lim \\left({phan_so(q)}\\right)^n=0$"
        kq2_F=f"$\\lim \\left({phan_so(q)}\\right)^n={random.choice(["+\\infty","-\\infty", phan_so(q)])}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"$\\lim \\left({phan_so(q)}\\right)^n=0$ vì $-1<{phan_so(q)}<1$."
    
    if chon==2:
        a=random.randint(1,15)
        b=a+random.randint(1,7)
        q=a/b
        
        kq2_T=f"* $\\lim \\left({phan_so(-q)}\\right)^n=0$"
        kq2_F=f"$\\lim \\left({phan_so(-q)}\\right)^n={random.choice(["+\\infty","-\\infty", phan_so(-q), phan_so(q)])}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"$\\lim \\left({phan_so(-q)}\\right)^n=0$ vì $-1<{phan_so(-q)}<1$."

    if chon==3:
        a=random.randint(1,15)
        b=a+random.randint(1,7)
        q=b/a
        chon=random.randint(1,2)
        kq2_T=f"* $\\lim \\left({phan_so(q)}\\right)^n=+\\infty$"
        kq2_F=f"$\\lim \\left({phan_so(q)}\\right)^n={random.choice([0,"-\\infty", phan_so(-q), phan_so(q)])}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"$\\lim \\left({phan_so(q)}\\right)^n=+\\infty$ vì ${phan_so(q)}>1$."

    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        a1 = random.choice([i for i in range(-5, 5) if i!=0])
        b1 = random.choice([i for i in range(-8, 8) if i!=0])
        c1 = random.choice([i for i in range(-7, 7) if i!=0])
        u=a1*n**2+b1*n+c1

        a2 = random.choice([i for i in range(-5, 5) if i!=0])    
        b2 = random.randint(-8,8)
        c2 = random.choice([i for i in range(-8, 8) if i!=0])
        v=a2*n**2+b2*n+c2    

        kq3_T=f"* $\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}={phan_so(a1/a2)}$"
        if c1/c2!=a1/a2:
            kq3_F=f"$\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}={phan_so(c1/c2)}$"
        else:
            kq3_F=f"$\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}={phan_so(a1/a2+random.randint(1,2))}$"

        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" $\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}\n"
        f"=\\lim \\dfrac{{{latex(a1+b1/n+c1/n**2)}}}{{{latex(a2+b2/n+c2/n**2)}}}={phan_so(a1/a2)}$.")

    
    if chon==2:
        a1 = random.choice([i for i in range(-5, 5) if i!=0])
        b1 = random.choice([i for i in range(-8, 8) if i!=0])
        c1 = random.choice([i for i in range(-7, 7) if i!=0])
        u=a1*n+b1

        a2 = random.choice([i for i in range(-5, 5) if i!=0])    
        b2 = random.randint(-8,8)
        c2 = random.choice([i for i in range(-8, 8) if i!=0])
        v=a2*n**2+b2*n+c2    

        kq3_T=f"* $\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}=0$"        
        kq3_F=f"$\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}={random.choice([phan_so(a1/a2), phan_so(b1/c2)])}$"     

        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f" $\\lim \\dfrac{{{latex(u)}}}{{{latex(v)}}}\n"
        f"=\\lim \\dfrac{{{latex(a1/n+b1/n**2)}}}{{{latex(a2+b2/n+c2/n**2)}}}=0$.")
    
    
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    b=random.randint(2,4)
    c=b+random.randint(1,2)
    a=b+random.randint(3,6)
    m = random.choice([i for i in range(-5, 6) if i!=0])
    p = random.choice([i for i in range(-5, 6) if i!=0])

    f=(m*a**n+b**n)/(p*a**n+c**n)

    kq4_T=f"* $\\lim {latex(f)}={phan_so(m/p)}$"
    kq4_F=f"$\\lim {latex(f)}={phan_so(m/p+random.randint(1,2))}$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$\\lim {latex(f)}=\\lim \\dfrac{{{m}+\\left({phan_so(b/a)}\\right)^n}}{{{p}+\\left({phan_so(c/a)}\\right)^n}}={phan_so(m/p)}$."
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

#[D11_C3_B1_10]-TF-M2. Xét Đ-S: lim q^n, lim P(n), lim căn(P)/Q, lim csc
def gh11gh_L11_C3_B1_10():
    chon=random.randint(1,2)
    if chon==1:
        q=random.choice([sqrt(i) for i in range(2,100)])     
    if chon==2:
        q=random.randint(1,5)*pi   
    
    noi_dung = f"Xét tính đúng-sai của các khẳng định sau:"        
    debai_word= f"{noi_dung}\n"
    
    if q<10:
        kq1_T=f"* $\\lim {latex(q)}^n=+\\infty$" 
        kq1_F=f"$\\lim {latex(q)}^n={random.choice(["-\\infty", 0, latex(q)])}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"$\\lim {latex(q)}^n=+\\infty$ vì ${latex(q)}>1$."
    else:    
        kq1_T=f"* $\\lim ({latex(q)})^n=+\\infty$" 
        kq1_F=f"$\\lim ({latex(q)})^n={random.choice(["-\\infty", 0, latex(q)])}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"$\\lim ({latex(q)})^n=+\\infty$ vì ${latex(q)}>1$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c=random.randint(-5,5)
    d = random.choice([i for i in range(-5, 6) if i!=0])
    n=sp.symbols("n")

    u=a*n**3+b*n**2+c*n+d

    if a>0:
        kq2_T=f"* $\\lim ({latex(u)})=+\\infty$"
        kq2_F=f"$\\lim ({latex(u)})={random.choice(["-\\infty", 0, latex(q)])}$"    
        HDG=(f"$\\lim ({latex(u)})=\\lim n^3({latex(a+b/n+c/n**2+d/n**3)})= +\\infty$"
            f" vì $\\lim n^3=+\\infty$ và $\\lim ({latex(a+b/n+c/n**2+d/n**3)})={a}>0$.")
    else:
        kq2_T=f"* $\\lim ({latex(u)})=-\\infty$"
        kq2_F=f"$\\lim ({latex(u)})={random.choice(["+\\infty", 0, latex(q)])}$"    
        HDG=(f"Vì $\\lim n^3=+\\infty$ và $\\lim ({latex(a+b/n+c/n**2+d/n**3)})={a}<0$ nên\n\n"
            f"$\\lim ({latex(u)})=\\lim n^3({latex(a+b/n+c/n**2+d/n**3)})= +\\infty$."
            )

    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a = random.randint(1,4)
    x_0=random.choice([i for i in range(-3, 3) if i!=0])
    b=random.randint(1,4)
    
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.choice([i for i in range(-5, 6) if i!=0])

    u=f"\\sqrt{{{latex(expand(a*(n-x_0)**2))}}}"
    v=f"{latex(c*n+d)}"

    kq3_T=f"* $\\lim \\dfrac{{{u}}} {{{v}}}={latex(sqrt(a)/c)}$" 
    kq3_F=f"$\\lim \\dfrac{{{u}}} {{{v}}}={latex(sqrt(a+random.randint(1,2))/c)}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$\\lim \\dfrac{{{u}}} {{{v}}}=\\lim \\dfrac{{\\sqrt{{{latex(expand(a*(1-x_0/n)**2))}}}}} {{{latex(c+d/n)}}} ={latex(sqrt(a)/c)}$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    u1= random.choice([i for i in range(-5, 6) if i!=0])
    du= random.choice([i for i in range(-5, 6) if i!=0])
    un=f"{latex(expand(u1+(n-1)*du))}"
    u2=u1+du
    u3=u2+du
    u4=u3+du
    S1=f"{latex(n/2*(2*u1+(n-1)*du))}"

    v1=u1+random.randint(3,4)
    if v1==0:v1=random.randint(1,3)
    dv= random.choice([i for i in range(-5, 6) if i!=0])
    vn=f"{latex(expand(v1+(n-1)*dv))}"
    v2=v1+dv
    v3=v2+dv
    v4=v3+dv
    S2=f"{latex(n/2*(2*v1+(n-1)*dv))}"

    kq4_T=f"* $\\lim \\dfrac{{{u1}+{u2}+{u3}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}={phan_so(du/dv)}$".replace("+-","-")
    kq4_F=f"$\\lim \\dfrac{{{u1}+{u2}+{u3}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}={phan_so(du/dv+random.randint(1,3))}$".replace("+-","-")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"${u1},{u2},{u3},...,{un}$ lập thành cấp số cộng có $u_1={u1},d={du}$.\n\n"
        f"${v1},{v2},{v3},...,{vn}$ lập thành cấp số cộng có $v_1={v1},d={dv}$.\n\n"
        f"$\\lim \\dfrac{{{u1}+{u2}+{u3}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn}}}$\n"
        f"$=\\lim \\dfrac{{{S1}}}{{{S2}}}=\\lim \\dfrac{{{latex(expand(2*u1+(n-1)*du))}}}{{{latex(expand(2*v1+(n-1)*dv))}}}={phan_so(du/dv)}$")
    HDG=HDG.replace("+-","-")
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

#[D11_C3_B1_11]-TF-M2. Xét Đ-S: lim a, lim (an+b)/(cn+d), lim un/vn, Tổng CSN lùi vô hạn
def gh11gh_L11_C3_B1_11():
    n=sp.symbols("n")

    noi_dung = f"Xét tính đúng-sai của các khẳng định sau:"        
    debai_word= f"{noi_dung}\n"

    a=random.choice([i for i in range(-150, 200) if i!=0])
    
    kq1_T=f"* $\\lim {a}={a}$" 
    kq1_F=f"$\\lim {a}={random.choice(["+\\infty","-\\infty"])}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\lim {a}={a}$."
    if a<0:
        kq1_T=f"* $\\lim ({a})={a}$" 
        kq1_F=f"$\\lim ({a})={random.choice(["+\\infty","-\\infty"])}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"$\\lim ({a})={a}$."

    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    a,b,c,d = [random.choice([i for i in range(-5, 6) if i!=0]) for _ in range(4)]
    if a*d-b*c==0: d=d+random.randint(1,2)
    u=(a*n+b)/(c*n+d)

    kq2_T=f"* $\\lim {latex(u)}={phan_so(a/c)}$"
    kq2_F=f"$\\lim {latex(u)}={phan_so(a/c+random.randint(1,2))}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$\\lim {latex(u)}=\\lim {latex((a+b/n)/(c+d/n))}= {phan_so(a/c)}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a,b,c,d,e,f = [random.choice([i for i in range(-5, 6) if i!=0]) for _ in range(6)]
    chon=random.randint(1,4)
    
    if chon==1:
        u=(a*n**4+b*n**3+c*n+d)/(e*n**2+f)**2

        kq3_T=f"* $\\lim {latex(u)}={phan_so(a/e**2)}$"
        if a/e!=a/e**2:
            kq3_F=f"$\\lim {latex(u)}={phan_so(a/e)}$"
        else:
            kq3_F=f"$\\lim {latex(u)}={random.choice(["+\\infty","-\\infty",phan_so((a+random.randint(1,2))/e**2)])}$"

        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex(a+b/n+c/n**3+d/n**4)} }}{{{latex((e+f/n**2)**2)} }}= {phan_so(a/e**2)}$."

    if chon==2:
        u=(e*n**2+f)**2/(a*n**4+b*n**3+c*n+d)

        kq3_T=f"* $\\lim {latex(u)}={phan_so(e**2/a)}$"        
        kq3_F=f"$\\lim {latex(u)}={random.choice(["+\\infty","-\\infty",phan_so(e**2/a+random.randint(1,2))])}$"

        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex((e+f/n**2)**2)}}}{{{latex(a+b/n+c/n**3+d/n**4)} }}= {phan_so(e**2/a)}$."
    
    if chon==3:
        u=(a*n**6+b*n**4+c*n**3+d)/(e*n**2+f)**3

        kq3_T=f"* $\\lim {latex(u)}={phan_so(a/e**3)}$"
        kq3_F=f"$\\lim {latex(u)}={random.choice(["+\\infty","-\\infty",phan_so((a+random.randint(1,2))/e**3)])}$"

        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex(a+b/n**2+c/n**3+d/n**6)} }}{{{latex((e+f/n**2)**3)} }}={phan_so(a/e**3)}$."

    if chon==4:
        u=(e*n**2+f)**3/(a*n**6+b*n**4+c*n**3+d)

        kq3_T=f"* $\\lim {latex(u)}={phan_so(e**3/a)}$"
        kq3_F=f"$\\lim {latex(u)}={random.choice(["+\\infty","-\\infty",phan_so(e**3/a+random.randint(1,2))])}$"

        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex((e*n**2+f)**3)}}}{{{latex(a+b/n**2+c/n**3+d/n**6)}}}= {phan_so(e**3/a)}$."
    
    
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    a=random.randint(1,8)
    b=a+random.randint(1,8)
    u1= random.choice([i for i in range(-3, 4) if i!=0])
    q=a/b
    S=u1/(1-q)
    kq4_T=f"* $S={phan_so(u1)}+{phan_so(u1*q)}+{phan_so(u1*q**2)}+...+{u1}\\left({phan_so(q)}\\right)^{{n-1}}+...={phan_so(S)}$".replace("+-","-")
    kq4_F=f"$S={phan_so(u1)}+{phan_so(u1*q)}+{phan_so(u1*q**2)}+...+{u1}\\left({phan_so(q)}\\right)^{{n-1}}+...={phan_so(S+random.randint(1,3))}$".replace("+-","-")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"${phan_so(u1)}, {phan_so(u1*q)}, {phan_so(u1*q**2)},...$ lập thành cấp số nhân với $u_1={u1},q={phan_so(q)}$.\n\n"
        f"$S={phan_so(u1)}+{phan_so(u1*q)}+{phan_so(u1*q**2)}+...+{u1}\\left({phan_so(q)}\\right)^{{n-1}}+...=\\dfrac{{{u1}}}{{1-{phan_so(q)}}}={phan_so(S)}$."
        )
    HDG=HDG.replace("+-","-")
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

#[D11_C3_B1_12]-TF-M2. Xét Đ-S: lim q^n, lim P(n), lim căn(P)/Q, lim csn
def gh11gh_L11_C3_B1_12():    
    noi_dung = f"Xét tính đúng-sai của các khẳng định sau:"        
    debai_word= f"{noi_dung}\n"

    a=random.randint(1,9)
    b=a+random.randint(1,9)
    chon=random.randint(1,2)
    
    if chon==1:
        q=a/b  
    if chon==2:
        q=-a/b    

    kq1_T=f"* $\\lim \\left({phan_so(q)}\\right)^n=0$" 
    kq1_F=f"$\\lim\\left({phan_so(q)}\\right)^n={random.choice(["+\\infty","-\\infty", phan_so(q)])}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\lim ({phan_so(q)})^n=0$ vì $-1<{phan_so(q)}<1$."

    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c=random.randint(-5,5)
    d = random.choice([i for i in range(-5, 6) if i!=0])
    n=sp.symbols("n")

    u=a*n**3+b*n**2+c*n+d

    if a>0:
        kq2_T=f"* $\\lim ({latex(u)})=+\\infty$"
        kq2_F=f"$\\lim ({latex(u)})={random.choice(["-\\infty", 0, latex(q)])}$"    
        HDG=(f"$\\lim ({latex(u)})=\\lim n^3({latex(a+b/n+c/n**2+d/n**3)})= +\\infty$"
            f" vì $\\lim n^3=+\\infty$ và $\\lim ({latex(a+b/n+c/n**2+d/n**3)})={a}>0$.")
    else:
        kq2_T=f"* $\\lim ({latex(u)})=-\\infty$"
        kq2_F=f"$\\lim ({latex(u)})={random.choice(["+\\infty", 0, latex(q)])}$"    
        HDG=(f"Vì $\\lim n^3=+\\infty$ và $\\lim ({latex(a+b/n+c/n**2+d/n**3)})={a}<0$ nên\n\n"
            f"$\\lim ({latex(u)})=\\lim n^3({latex(a+b/n+c/n**2+d/n**3)})= +\\infty$."
            )
        
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a = random.randint(1,4)
    x_0=random.choice([i for i in range(-3, 3) if i!=0])
    b=random.randint(1,4)
    
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.choice([i for i in range(-5, 6) if i!=0])

    u=f"\\sqrt{{{latex(expand(a*(n-x_0)**2))}}}"
    v=f"{latex(c*n+d)}"

    kq3_T=f"* $\\lim \\dfrac{{{u}}} {{{v}}}={latex(sqrt(a)/c)}$" 
    kq3_F=f"$\\lim \\dfrac{{{u}}} {{{v}}}={latex(sqrt(a+random.randint(1,2))/c)}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$\\lim \\dfrac{{{u}}} {{{v}}}=\\lim \\dfrac{{\\sqrt{{{latex(expand(a*(1-x_0/n)**2))}}}}} {{{latex(c+d/n)}}} ={latex(sqrt(a)/c)}$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        u1= random.choice([i for i in range(-5, 6) if i!=0])
        q= random.randint(2,4)
        un=f"{latex(u1*q**(n-1))}"
        u2=u1*q
        u3=u2*q
        u4=u3*q
        S1=f"{latex(u1*(1-q**(n))/(1-q))}"

        v1=u1+random.randint(1,4)
        if v1==0:v1=random.randint(1,3)
        p= q
        vn=f"{latex(v1*p**(n-1))}"
        v2=v1*p
        v3=v2*p
        v4=v3*p
        S2=f"{latex(v1*(1-p**(n))/(1-p))}"

        kq,kp=phan_so(u1/1-q),phan_so(v1/1-p)

        kq4_T=f"* $\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}={phan_so(u1/v1)}$".replace("+-","-").replace("--","+")
        kq4_F=f"$\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}={phan_so(u1/v1+random.randint(1,2))}$".replace("+-","-").replace("--","+")
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f"${u1},{u2},...,{un}$ lập thành cấp số nhân có $u_1={u1},q={q}$.\n\n"
            f"${v1},{v2},...,{vn}$ lập thành cấp số nhân có $v_1={v1},q={p}$.\n\n"
            f"$\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+...+{vn}}}$\n"
            f"$=\\lim \\dfrac{{{S1}}}{{{S2}}}={phan_so(u1/v1)}$.\n"
            )
    
    if chon==2:
        u1= random.choice([i for i in range(-5, 6) if i!=0])
        q= random.randint(2,4)
        un=f"{latex(u1*q**(n-1))}"
        u2=u1*q
        u3=u2*q
        u4=u3*q
        S1=f"{latex(u1*(1-q**(n))/(1-q))}"

        v1=u1+random.randint(1,4)
        if v1==0:v1=random.randint(1,3)
        p= q+random.randint(1,3)
        vn=f"{latex(v1*p**(n-1))}"
        v2=v1*p
        v3=v2*p
        v4=v3*p
        S2=f"{latex(v1*(1-p**(n))/(1-p))}"

        kq,kp=phan_so(u1/1-q),phan_so(v1/1-p)

        kq4_T=f"* $\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}=0$".replace("+-","-").replace("--","+")
        kq4_F=f"$\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}={phan_so(u1/v1)}$".replace("+-","-").replace("--","+")
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f"${u1},{u2},...,{un}$ lập thành cấp số nhân có $u_1={u1},q={q}$.\n\n"
            f"${v1},{v2},...,{vn}$ lập thành cấp số nhân có $v_1={v1},q={p}$.\n\n"
            f"$\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+...+{vn}}}$\n"
            f"$=\\lim \\dfrac{{{S1}}}{{{S2}}}=0$.\n"
            )   

 
    HDG=HDG.replace("+-","-").replace("--","+")
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

#[D11_C3_B1_13]-TL-M3. Tính lim P(n)/Q(n)
def gh11gh_L11_C3_B1_13():
    n=sp.symbols("n")
    a,b,c,d,e,f = [random.choice([i for i in range(-5, 6) if i!=0]) for _ in range(6)]
    chon=random.randint(1,4)        
    if chon==1:
        u=(a*n**4+b*n**3+c*n+d)/(e*n**2+f)**2
        kq=a/e**2
        if kq<=-9.9:
            noi_dung=f"Tính giới hạn $\\lim {latex(u)}$ (kết quả làm tròn đến hàng đơn vị)."
            dap_an=f"{round_half_up(a/e**2,0)}".replace(".",",")
        else:
            noi_dung=f"Tính $\\lim {latex(u)}$ (kết quả làm tròn đến hàng phần trăm)."
            dap_an=f"{round_half_up(a/e**2,2):.2f}".replace(".",",")

        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex(a+b/n+c/n**3+d/n**4)} }}{{{latex((e+f/n**2)**2)} }}= {phan_so(a/e**2)}$."        

    if chon==2:
        u=(e*n**2+f)**2/(a*n**4+b*n**3+c*n+d)

        noi_dung=f"Tính giới hạn $\\lim {latex(u)}$ (kết quả làm tròn đến hàng phần mười)."

        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex((e+f/n**2)**2)}}}{{{latex(a+b/n+c/n**3+d/n**4)} }}= {phan_so(e**2/a)}$."
        dap_an=f"{round_half_up(e**2/a,1):.1f}".replace(".",",")
    
    if chon==3:
        u=(a*n**6+b*n**4+c*n**3+d)/(e*n**2+f)**3
        noi_dung=f"Tính $\\lim {latex(u)}$ (kết quả làm tròn đến hàng phần mười)."
        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex(a+b/n**2+c/n**3+d/n**6)} }}{{{latex((e+f/n**2)**2)} }}= {phan_so(a/e**3)}$."
        dap_an=f"{round_half_up(a/e**3,1):.1f}".replace(".",",")

    if chon==4:
        u=(e*n**2+f)**3/(a*n**6+b*n**4+c*n**3+d)

        noi_dung=f"Tính giới hạn $\\lim {latex(u)}$ (kết quả làm tròn đến hàng phần mười)."

        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex((e+f/n**2)**2)}}}{{{latex(a+b/n**2+c/n**3+d/n**6)}}}= {phan_so(e**3/a)}$."
        dap_an=f"{round_half_up(e**3/a,1):.1f}".replace(".",",") 
      
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B1_14]-TL-M3. Tính lim P(n)/Q(n) với P,Q là các cấp số cộng
def gh11gh_L11_C3_B1_14():
    n=sp.symbols("n")
    u1= random.choice([i for i in range(-5, 6) if i!=0])
    du= random.choice([i for i in range(-5, 6) if i!=0])

    un=f"{latex(expand(u1+(n-1)*du))}"
    u2=u1+du
    u3=u2+du
    u4=u3+du
    S1=f"{latex(n/2*(2*u1+(n-1)*du))}"

    v1=u1+random.randint(3,4)
    if v1==0: v1=random.randint(1,3)
    dv= random.choice([i for i in range(-5, 6) if i!=0])
    vn=f"{latex(expand(v1+(n-1)*dv))}"
    v2=v1+dv
    v3=v2+dv
    v4=v3+dv
    S2=f"{latex(n/2*(2*v1+(n-1)*dv))}"

    noi_dung=f"Tính $\\lim \\dfrac{{{u1}+{u2}+{u3}+...+({un})}}{{{v1}+{v2}+{v3}+...+({vn})}}$ (kết quả làm tròn đến hàng phần mười).".replace("+-","-")

    noi_dung_loigiai=(f"${u1},{u2},{u3},...,{un}$ lập thành cấp số cộng có $u_1={u1},d={du}$.\n\n"
        f"${v1},{v2},{v3},...,{vn}$ lập thành cấp số cộng có $v_1={v1},d={dv}$.\n\n"
        f"$\\lim \\dfrac{{{u1}+{u2}+{u3}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn}}}$\n"
        f"$=\\lim \\dfrac{{{S1}}}{{{S2}}}=\\lim \\dfrac{{{latex(expand(2*u1+(n-1)*du))}}}{{{latex(expand(2*v1+(n-1)*dv))}}}={phan_so(du/dv)}$")
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
    dap_an=f"{round_half_up(du/dv,1):.1f}".replace(".",",") 
    
    debai_word= f"{noi_dung}\n"
    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B1_15]-TL-M3. Tính lim P(n)/Q(n) với P,Q là các cấp số nhân
def gh11gh_L11_C3_B1_15():
    n=sp.symbols("n")
    u1= random.choice([i for i in range(-5, 6) if i!=0])
    q= random.randint(2,4)
    un=f"{latex(u1*q**(n-1))}"
    u2=u1*q
    u3=u2*q
    u4=u3*q
    S1=f"{latex(u1*(1-q**(n))/(1-q))}"

    v1=u1+random.randint(1,4)
    if v1==0:v1=random.randint(1,3)
    p= q
    vn=f"{latex(v1*p**(n-1))}"
    v2=v1*p
    v3=v2*p
    v4=v3*p
    S2=f"{latex(v1*(1-p**(n))/(1-p))}"

    kq,kp=phan_so(u1/1-q),phan_so(v1/1-p)

    noi_dung=f"Tính $\\lim \\dfrac{{{u1}+{u2}+...+({un})}}{{{v1}+{v2}+{v3}+...+({vn})}}$(kết quả làm tròn đến hàng phần mười).".replace("+-","-").replace("--","+")   

    noi_dung_loigiai=(f"${u1},{u2},...,{un}$ lập thành cấp số nhân có $u_1={u1},q={q}$.\n\n"
        f"${v1},{v2},...,{vn}$ lập thành cấp số nhân có $v_1={v1},q={p}$.\n\n"
        f"$\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+...+{vn}}}$\n"
        f"$=\\lim \\dfrac{{{S1}}}{{{S2}}}={phan_so(u1/v1)}$.\n" )

    dap_an=f"{round_half_up(u1/v1,1):.1f}".replace(".",",") 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B1_16]-M2. Cho lim (u_n) và (v_n). Tính lim (a.un + b.vn +c)
def gh11gh_L11_C3_B1_16():
    #Tạo list chứa các hệ số
    u_n = random.choice([i for i in range(-8, 8) if i!=0])
    v_n = random.choice([i for i in range(-10, 10) if i!=0])

    if v_n==u_n:
        v_n=u_n + random.randint(2,5)
    
    a= random.choice([i for i in range(-4, 4) if i!=0])
    b= random.choice([i for i in range(-4, 4) if i!=0])
    c=random.randint(-7,7)

    u,v=sp.symbols("u_n v_n")
    dayso=a*u+b*v+c

    kq= a*u_n+b*v_n+c
    kq2=a*v_n+b*u_n+c
    kq3=a*u_n+b*v_n +c+random.randint(1,2)
    kq4=a*u_n+v_n-c

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    
    #Tạo các phương án
    pa_A= f"*${{ {phan_so(kq)} }}$"
    pa_B= f"$ {{{phan_so(kq2)} }}$"
    pa_C= f"$ {{ {phan_so(kq3)}}}$"
    pa_D= f"$ {{{phan_so(kq4)} }}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    noi_dung= f"Cho hai dãy số $(u_n)$ và $(v_n)$ có $\\lim u_n ={u_n}$ và $\\lim v_n ={v_n}$. Tính giới hạn $\\lim ({latex(dayso)})$."

    noi_dung_loigiai=f" $\\lim ({latex(dayso)})={a}.{tao_ngoac(u_n)}+{b}.{tao_ngoac(v_n)}+{c}={phan_so(kq)}$.".replace("+-","-")
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

#[D11_C3_B1_17]-M2. Cho lim (u_n) và (v_n). Tính lim (a.u_n+b/c.v_n)
def gh11gh_L11_C3_B1_17():
    #Tạo list chứa các hệ số
    u_n = random.choice([i for i in range(-8, 8) if i!=0])
    v_n = random.choice([i for i in range(-10, 10) if i!=0])

    if v_n==u_n:
        v_n=u_n + random.randint(2,5)
    
    a= random.choice([i for i in range(-4, 4) if i!=0])
    b= random.choice([i for i in range(-4, 4) if i!=0])
    c= random.choice([i for i in range(-4, 4) if i!=0])

    u,v=sp.symbols("u_n v_n")
    chon=random.randint(1,2)
    if chon==1:
        dayso=(a*u+b)/(c*v)        

        kq= (a*u_n+b)/(c*v_n)
        kq2=a*u_n+b/(c*v_n)
        kq3=(a*u_n)/(c*v_n)
        kq4=(a*v_n+b)/(c*u_n)

        noi_dung_loigiai=f" $\\lim ({latex(dayso)})=\\dfrac{{{a}.{tao_ngoac(u_n)}+{b}}}{{{c*v_n} }}={phan_so(kq)}$.".replace("+-","-")
    
    if chon==2:

        dayso=(a*v+b)/(c*u)        

        kq= (a*v_n+b)/(c*u_n)
        kq2=a*u_n+b/(c*v_n)
        kq3=(a*u_n)/(c*v_n)
        kq4=(a*u_n+b)/(c*v_n)

        noi_dung_loigiai=f" $\\lim ({latex(dayso)})=\\dfrac{{{a}.{tao_ngoac(v_n)}+{b}}}{{{c*u_n} }}={phan_so(kq)}$.".replace("+-","-")
    
    

    noi_dung= f"Cho hai dãy số $(u_n)$ và $(v_n)$ có $\\lim u_n ={u_n}$ và $\\lim v_n ={v_n}$. Tính giới hạn $\\lim ({latex(dayso)})$."
    
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    
    #Tạo các phương án
    pa_A= f"*${{ {phan_so(kq)} }}$"
    pa_B= f"$ {{{phan_so(kq2)} }}$"
    pa_C= f"$ {{ {phan_so(kq3)}}}$"
    pa_D= f"$ {{{phan_so(kq4)} }}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    

    
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

#[D11_C3_B1_18]-M2. Cho phóng xạ. Xét Đ-S: SHTQ, tìm u_n, limu_n, thời gian hết độc hại
def gh11gh_L11_C3_B1_18():
    u1=random.randint(5,30)/10
    u1_round=f"{round_half_up(u1,1):.1f}".replace(".",",")
    T=random.randint(15,30)*1000
    k=random.randint(-10,-5)
    u2=u1/2
    u2_round=f"{round_half_up(u2,1):.1f}".replace(".",",")
    u2_false=random.choice([u1/4,u1/3 ])
    u2_false=f"{round_half_up(u2,1):.1f}".replace(".",",")

    noi_dung = (
    f"  Có ${{{u1_round}}}$ kg chất phóng xạ độc hại. Biết rằng, cứ sau một khoảng thời gian $T={{{T}}}$ năm thì một nửa số chất phóng xạ này bị phân rã thành chất khác không độc hại đối với sức khoẻ của con người (${{T}}$ được gọi là chu kì bán rã). Biết rằng chất phóng xạ này sẽ không độc hại nữa nếu khối lượng chất phóng xạ còn lại bé hơn $10^{{{k}}}$ gam."
    f" Gọi ${{u_n}}$ là khối lượng chất phóng xạ còn lại sau chu kì thứ ${{n}}$"
    f" Xét tính đúng-sai của các khẳng định sau:")    
    
    kq1_T=f"* $u_2={u2_round}$" 
    kq1_F=f"$u_2={u2_false}$"
    
    HDG=f"$u_2={phan_so(1/2)}u_1={phan_so(1/2)}.{u1_round}={u2_round}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*$u_n={u1_round}.\\left({phan_so(1/2)}\\right)^{{n-1}}$, với $n \\in \\mathbb{{N}}$"
    kq2_F=f"$u_n={u1_round}.\\left({phan_so(1/2)}\\right)^{{n}}$, với $n \\in \\mathbb{{N}}$"
    
    HDG=(f"$u_n$ là cấp số nhân với $u_1={u1_round}, q={phan_so(1/2)}$.\n\n"
        f"Do đó: $u_n={u1_round}.\\left({phan_so(1/2)}\\right)^{{n-1}}$, với $n \\in \\mathbb{{N}}$."
        )
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    t=random.choice([random.randint(-10,-1), random.randint(1,10) ])

    kq3_T=f"* $\\lim (u_n+{t})={t}$" 
    kq3_F=f"$\\lim (u_n+{t})={-t}$"
    
    HDG=f"$\\lim (u_n+{t})=0+{t}={t}$."
    HDG=HDG.replace("+-","-").replace("-+","-").replace("--","+")
    kq3=random.choice([kq3_T, kq3_F])
    kq3=kq3.replace("+-","-").replace("-+","-").replace("--","+")
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

     
    
    a=10**(k-3)/u1
    b=log(a)/log(1/2)
    n_0=f"{round_half_up(b,2):.2f}".replace(".",",")
    n_1=f"{round_half_up(b+1,2):.2f}".replace(".",",")
    
    n, n_2=int(b+1),int(b+2)
    if n>b+1:
        nam=n
    else:
        nam=n_2

    kq4_T=f"* Sau ít nhất ${{{nam}}}$ chu kì khối lượng chất phóng xạ đã cho ban đầu không còn độc hại đối với con người"
    kq4_F=f"Sau ít nhất ${{{nam-random.randint(1,2)}}}$ chu kì khối lượng chất phóng xạ đã cho ban đầu không còn độc hại đối với con người"
    HDG=(f" Để chất phóng xạ bé hơn $10^{{{k}}}$ gam thì:\n\n"
        f"${u1_round}.10^3.\\left({phan_so(1/2)}\\right)^{{n-1}} < 10^{{{k}}}$\n\n"
        f"$\\Rightarrow \\left({phan_so(1/2)}\\right)^{{n-1}}<\\dfrac{{10^{{{k-3}}}}}{{{u1_round}}}$\n\n"
        f"$\\Rightarrow n-1>{n_0} \\Rightarrow n>{n_1}$.\n\n"
        f"Do đó: sau ít nhất ${{{nam}}}$ chu kì khối lượng chất phóng xạ đã cho ban đầu không còn độc hại đối với con người."

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

#[D11_C3_B1_19]-M3. Tính tổng diện tích các hình vuông tăng vô hạn
def gh11gh_L11_C3_B1_19():
    a=sqrt(random.randint(2,16))
    st_a=f"{latex(a)}".replace(".0","")
    code_hinh=(f" \\begin{{tikzpicture}}\n\
            \\def\\a{{3}}\n\
            \\def\\b{{0.5}}\n\
            \\def\\levels{{10}}\n\
            \\coordinate (A0) at (0, \\a);\n\
            \\coordinate (B0) at (\\a, 2*\\a);\n\
            \\coordinate (C0) at (2*\\a, \\a);\n\
            \\coordinate (D0) at (\\a, 0);\n\
            \\foreach \\i in {{1,...,\\levels}} {{\n\
                \\coordinate (A\\i) at ($(A\\the\\numexpr\\i-1\\relax)!\\b!(B\\the\\numexpr\\i-1\\relax)$);\n\
                \\coordinate (B\\i) at ($(B\\the\\numexpr\\i-1\\relax)!\\b!(C\\the\\numexpr\\i-1\\relax)$);\n\
                \\coordinate (C\\i) at ($(C\\the\\numexpr\\i-1\\relax)!\\b!(D\\the\\numexpr\\i-1\\relax)$);\n\
                \\coordinate (D\\i) at ($(D\\the\\numexpr\\i-1\\relax)!\\b!(A\\the\\numexpr\\i-1\\relax)$);\n\
                \\draw  (A\\i) -- (B\\i) -- (C\\i) -- (D\\i) -- cycle;\n\
            }}\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    noi_dung = (
    f"Từ hình vuông đầu tiên có cạnh bằng ${{{st_a}}}$, nối các trung điểm của bốn cạnh để tạo hình vuông tiếp theo."
    f" Tính tổng diện tích ${{T}}$ của các hình vuông khi cho số hình vuông tăng lên vô hạn."
    )
    dap_an=2*a**2
    n=sp.symbols("n")
    q=sqrt(2)/2
    canh_2=a*sqrt(2)/2
    canh_3=canh_2*sqrt(2)/2
    canh_n=a*q**(n-1)
    noi_dung_loigiai=(
    f"Diện tích hình vuông đầu tiên: $S_1 = {latex(a**2)}$.\n\n"
    f"Cạnh hình vuông thứ 2 là: ${latex(canh_2)}\\Rightarrow S_2 = {latex((canh_2)**2)}$.\n\n"
    f"Cạnh hình vuông thứ 3 là: ${latex(canh_3)}\\Rightarrow S_2 = {latex((canh_3)**2)}$.\n\n"
    f"Cạnh hình vuông thứ n là: ${latex(a)}\\left({latex(q)}\\right)^{{n-1}}\\Rightarrow S_n = {latex((canh_n)**2)}$.\n\n"
    f" $S_n$ là cấp số nhân lùi vô hạn với $u_1={a**2},q={phan_so(1/2)}$.\n\n"

    f"$T={latex(a**2)}+{latex((canh_2)**2)}+{latex((canh_3)**2)}+ \\cdots+ {latex((canh_n)**2)}=\\dfrac{{{a**2}}}{{1-{phan_so(1/2)}}}={2*a**2}$.\n\n"
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

#[D11_C3_B1_20]-SA-M3. Tính tổng diện tích các hình vuông tăng vô hạn
def gh11gh_L11_C3_B1_20():
    a=sqrt(random.randint(2,16))
    S_1=a**2
    st_a=f"{latex(a)}".replace(".0","")
    q=5/8
    T=float(S_1/(1-q))
    if T.is_integer():
        noi_dung = (
        f"Cho hình vuông $C_1$ có cạnh bằng ${{{st_a}}}$. Người ta chia mỗi cạnh thành ${{4}}$ phần bằng nhau và nối các điểm chia để tạo hình vuông ${{C_2}}$."
        f" Tiếp tục quá trình này, tính tổng diện tích của các hình vuông."
        )
        dap_an=int(T)
        noi_dung_loigiai=(
        f"  Gọi hình vuông $C_1$ có cạnh $a_1 = {st_a}$ và có diện tích là $S_1 = a_1^2$.\n\n\
            Cạnh của hình vuông $C_2$ là\n\n\
            $ a_2 = \\sqrt{{\\left( \\dfrac{{3}}{{4}} a_1 \\right)^2 + \\left( \\dfrac{{1}}{{4}} a_1 \\right)^2}} = \\dfrac{{a_1 \\sqrt{{10}}}}{{4}}.$\n\n\
            Diện tích của hình vuông $C_2$ là\n\n\
            $S_2 = \\dfrac{{5}}{{8}} a_1^2 = \\dfrac{{5}}{{8}} S_1.$\n\n\
            Cạnh của hình vuông $C_3$ là\n\n\
            $a_3 = \\sqrt{{\\left( \\dfrac{{3}}{{4}} a_2 \\right)^2 + \\left( \\dfrac{{1}}{{4}} a_2 \\right)^2}} = \\dfrac{{a_2 \\sqrt{{10}}}}{{4}} = a_1 \\left( \\dfrac{{\\sqrt{{10}}}}{{4}} \\right)^2.$\n\n\
            Diện tích của hình vuông $C_3$ là\n\n\
            $S_3 = \\left( \\dfrac{{5}}{{8}} \\right)^2 a_1^2 = \\left( \\dfrac{{5}}{{8}} \\right)^2 S_1.$\n\n\
            Dãy các hình vuông $C_1$, $C_2$, $C_3$, $\\ldots$ , $C_n$, $\\ldots$ có các diện tích lần lượt là $S_1$, $S_2$, $S_3$, $\\ldots$ , $S_n$, $\\ldots$ tạo thành một cấp số nhân lùi vô hạn với số hạng đầu là $u_1 = S_1 = {S_1}$ và công bội $q = \\dfrac{{5}}{{8}}$.\n\n\n\
            Vậy tổng diện tích của các hình vuông là\n\n\
            $S = S_1 + S_2 + S_3 + \\cdots + S_n + \\cdots = \\dfrac{{u_1}}{{1 - q}} = \\dfrac{{16}}{{1 - \\dfrac{{5}}{{8}}}} = {dap_an}$." 

        )  
    else:
        noi_dung = (
        f"Cho hình vuông $C_1$ có cạnh bằng ${{{st_a}}}$. Người ta chia mỗi cạnh thành ${{4}}$ phần bằng nhau và nối các điểm chia để tạo hình vuông ${{C_2}}$."
        f" Tiếp tục quá trình này, tính tổng diện tích của các hình vuông (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round_half_up(T,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"  Gọi hình vuông $C_1$ có cạnh $a_1 = {st_a}$ và có diện tích là $S_1 = a_1^2$.\n\n\
            Cạnh của hình vuông $C_2$ là\n\n\
            $ a_2 = \\sqrt{{\\left( \\dfrac{{3}}{{4}} a_1 \\right)^2 + \\left( \\dfrac{{1}}{{4}} a_1 \\right)^2}} = \\dfrac{{a_1 \\sqrt{{10}}}}{{4}}.$\n\n\
            Diện tích của hình vuông $C_2$ là\n\n\
            $S_2 = \\dfrac{{5}}{{8}} a_1^2 = \\dfrac{{5}}{{8}} S_1.$\n\n\
            Cạnh của hình vuông $C_3$ là\n\n\
            $a_3 = \\sqrt{{\\left( \\dfrac{{3}}{{4}} a_2 \\right)^2 + \\left( \\dfrac{{1}}{{4}} a_2 \\right)^2}} = \\dfrac{{a_2 \\sqrt{{10}}}}{{4}} = a_1 \\left( \\dfrac{{\\sqrt{{10}}}}{{4}} \\right)^2.$\n\n\
            Diện tích của hình vuông $C_3$ là\n\n\
            $S_3 = \\left( \\dfrac{{5}}{{8}} \\right)^2 a_1^2 = \\left( \\dfrac{{5}}{{8}} \\right)^2 S_1.$\n\n\
            Dãy các hình vuông $C_1$, $C_2$, $C_3$, $\\ldots$ , $C_n$, $\\ldots$ có các diện tích lần lượt là $S_1$, $S_2$, $S_3$, $\\ldots$ , $S_n$, $\\ldots$ tạo thành một cấp số nhân lùi vô hạn với số hạng đầu là $u_1 = S_1 = {S_1}$ và công bội $q = \\dfrac{{5}}{{8}}$.\n\n\n\
            Vậy tổng diện tích của các hình vuông là\n\n\
            $S = S_1 + S_2 + S_3 + \\cdots + S_n + \\cdots = \\dfrac{{u_1}}{{1 - q}} = \\dfrac{{16}}{{1 - \\dfrac{{5}}{{8}}}} = {dap_an}$." 

        )  
    code_hinh=(f" \\begin{{tikzpicture}}\n\
            \\def\\a{{3}}\n\
            \\def\\b{{0.25}}\n\
            \\def\\levels{{10}}\n\
            \\coordinate (A0) at (0, 0);\n\
            \\coordinate (B0) at (\\a, 0);\n\
            \\coordinate (C0) at (\\a, \\a);\n\
            \\coordinate (D0) at (0, \\a);\n\
            \\foreach \\i in {{1,...,\\levels}} {{\n\
                \\coordinate (A\\i) at ($(A\\the\\numexpr\\i-1\\relax)!\\b!(B\\the\\numexpr\\i-1\\relax)$);\n\
                \\coordinate (B\\i) at ($(B\\the\\numexpr\\i-1\\relax)!\\b!(C\\the\\numexpr\\i-1\\relax)$);\n\
                \\coordinate (C\\i) at ($(C\\the\\numexpr\\i-1\\relax)!\\b!(D\\the\\numexpr\\i-1\\relax)$);\n\
                \\coordinate (D\\i) at ($(D\\the\\numexpr\\i-1\\relax)!\\b!(A\\the\\numexpr\\i-1\\relax)$);\n\
                \\draw  (A\\i) -- (B\\i) -- (C\\i) -- (D\\i) -- cycle;\n\
            }}\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
      
        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B1_21]-SA-M3. Tính tổng diện tích các tam giác đều lùi vô hạn
def gh11gh_L11_C3_B1_21():
    a=sqrt(random.randint(2,16))
    S_0=a**2*sqrt(3)/4
    S_1=S_0/4
    st_a=f"{latex(a)}".replace(".0","")
    q=1/4
    T=S_1/(1-q)

    noi_dung = (
    f"Cho tam giác đều ${{ABC}}$ có cạnh bằng ${{{st_a}}}$. Nối các trung điểm $A_1$, $B_1$, $C_1$ của ${{BC}}$, ${{CA}}$, ${{AB}}$ được tam giác đều ${{A_1B_1C_1}}$."
    f" Tiếp tục nối các trung điểm $A_2$, $B_2$, $C_2$ của các cạnh $B_1C_1, C_1A_1, A_1B_1$ ta được tam giác đều $A_2B_2C_2$."
    f" Tiếp tục nối các trung điểm đến vô hạn. Gọi $S_n$ là diện tích tam giác $A_nB_nC_n$."
    f" Tính $S_1+S_2+\\cdots+S_n+\\cdots$ (kết quả làm tròn đến hàng phần trăm).")
    dap_an=f"{round_half_up(T,2):.2f}".replace(".",",")

    noi_dung_loigiai=(

    f" Diện tích tam giác ${{ABC}}$ là $S_0 = {latex(S_0)}$.\n\n\
$S_1 = \\dfrac{{1}}{{4}} S_0$, $S_2 = \\dfrac{{1}}{{4}} S_1$, $S_3 = \\dfrac{{1}}{{4}} S_2$, $\\ldots $\n\n\
Do đó, $(S_n)$ là một cấp số nhân với công bội $q = \\dfrac{{1}}{{4}}$.\n\n\
Tổng diện tích các tam giác đều $A_n B_n C_n$ là tổng của một cấp số nhân lùi vô hạn với công bội $q = \\dfrac{{1}}{{4}}$.\n\n\
Do đó, tổng diện tích là\n\n\
$S = S_1 + S_2 + S_3 + \\cdots + S_n + \\cdots = \\dfrac{{S_1}}{{1 - q}} = \\dfrac{{{latex(S_1)}}}{{1 - \\dfrac{{1}}{{4}}}}={dap_an}$." 

    )  
    code_hinh=(f"   \\begin{{tikzpicture}}\n\
            \\def\\a{{4}}\n\
            \\newcommand{{\\drawtriangle}}[3]{{\n\
                \\draw (#1) -- (#2) -- (#3) -- cycle;\n\
            }}\n\
            \\newcommand{{\\midpoint}}[3]{{\n\
                \\coordinate (#3) at ($(#1)!0.5!(#2)$);\n\
            }}\n\
            \\newcommand{{\\equilateraltriangle}}[3]{{\n\
                \\coordinate (#3) at (0, 0);\n\
                \\coordinate (#3-1) at (#1, 0); t\n\
                \\coordinate (#3-2) at ($(#3-1)!1!(#3)$);\n\
                \\coordinate (#3-3) at (rotate around={{60:(#3-1)}});\n\
                \\draw (#3-1) -- (#3-2) -- (#3-3) -- cycle;\n\
            }}\n\
            \\coordinate (A) at (\\a/2, {{\\a*sqrt(3)/2}});\n\
            \\coordinate (B) at (0, 0);\n\
            \\coordinate (C) at (\\a, 0);\n\
            \\drawtriangle{{A}}{{B}}{{C}};\n\
            \\node at (A) [above] {{\\scriptsize $A$}};\n\
            \\node at (B) [left] {{\\scriptsize $B$}};\n\
            \\node at (C) [right] {{\\scriptsize $C$}};\n\
            \\midpoint{{B}}{{C}}{{A1}}\n\
            \\midpoint{{C}}{{A}}{{B1}}\n\
            \\midpoint{{A}}{{B}}{{C1}}\n\
            \\fill[gray!20] (A1) -- (B1) -- (C1) -- cycle;\n\
            \\drawtriangle{{A1}}{{B1}}{{C1}};\n\
            \\node at (A1) [below] {{\\scriptsize $A_1$}};\n\
            \\node at (B1) [right] {{\\scriptsize $B_1$}};\n\
            \\node at (C1) [left] {{\\scriptsize $C_1$}};\n\
            \\midpoint{{B1}}{{C1}}{{A2}}\n\
            \\midpoint{{C1}}{{A1}}{{B2}}\n\
            \\midpoint{{A1}}{{B1}}{{C2}}\n\
            \\fill[gray!35] (A2) -- (B2) -- (C2) -- cycle;\n\
            \\drawtriangle{{A2}}{{B2}}{{C2}};\n\
            \\node at (A2) [above] {{\\scriptsize $A_2$}};\n\
            \\node at (B2) [left] {{\\scriptsize $B_2$}};\n\
            \\node at (C2) [right] {{\\scriptsize $C_2$}};\n\
            \\midpoint{{B2}}{{C2}}{{A3}}\n\
            \\midpoint{{C2}}{{A2}}{{B3}}\n\
            \\midpoint{{A2}}{{B2}}{{C3}}\n\
            \\fill[gray!50] (A3) -- (B3) -- (C3) -- cycle;\n\
            \\drawtriangle{{A3}}{{B3}}{{C3}};\n\
            \\node at (A3) [below] {{\\scriptsize $A_3$}};\n\
            \\node at (B3) [right] {{\\scriptsize $B_3$}};\n\
            \\node at (C3) [left] {{\\scriptsize $C_3$}};\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)  
        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B1_22]-SA-M2. Tính tổng các cạnh của các tam giác đều lùi vô hạn
def gh11gh_L11_C3_B1_22():
    a=sqrt(random.randint(2,16))
    u1=a*sqrt(3)/2
    u2=u1*1/2
    u3=u2*1/2
    st_a=f"{latex(a)}".replace(".0","")
    q=1/2
    T=u1/(1-q)

    noi_dung = (
    f"Cho tam giác đều ${{ABC}}$ có cạnh bằng ${{{st_a}}}$. Nối các trung điểm $A_1$, $B_1$, $C_1$ của ${{BC}}$, ${{CA}}$, ${{AB}}$ được tam giác đều ${{A_1B_1C_1}}$."
    f" Tiếp tục nối các trung điểm $A_2$, $B_2$, $C_2$ của các cạnh $B_1C_1, C_1A_1,A_1B_1$ ta được tam giác đều $A_2B_2C_2$."
    f" Tiếp tục nối các trung điểm đến vô hạn."
    f"  Tính tổng các độ dài $l = A A_1 + A_1 A_2 + A_2 A_3 + \\cdots + A_{{n-1}} A_n + \\cdots$ (kết quả làm tròn đến hàng phần trăm).")
    dap_an=f"{round_half_up(T,2):.2f}".replace(".",",")

    noi_dung_loigiai=(

    f" Đặt $u_1 = A A_1$, $u_2 = A_1 A_2$, $u_3 = A_2 A_3$,$\\ldots$, $u_n = A_{{n-1}} A_n$.\n\n\
$u_1 = {latex(u1)}$, $u_2 =\\dfrac{{1}}{{2}} u_1={latex(u2)}$, $u_3 =\\dfrac{{1}}{{2}} u_2={latex(u3)}$,$\\ldots$, $u_n = \\dfrac{{1}}{{2}} u_{{n-1}}$,$\\ldots$\n\n\
Do đó, $(u_n)$ là một cấp số nhân lùi vô hạn với công bội $q = \\dfrac{{1}}{{2}}$.\n\n\
$l = \\dfrac{{u_1}}{{1 - q}} = \\dfrac{{{latex(u1)}}}{{1 -{phan_so(1/2)}}} = {dap_an}.$\n\
 " 


    )  
    code_hinh=(f"   \\begin{{tikzpicture}}\n\
            \\def\\a{{4}}\n\
            \\newcommand{{\\drawtriangle}}[3]{{\n\
                \\draw (#1) -- (#2) -- (#3) -- cycle;\n\
            }}\n\
            \\newcommand{{\\midpoint}}[3]{{\n\
                \\coordinate (#3) at ($(#1)!0.5!(#2)$);\n\
            }}\n\
            \\newcommand{{\\equilateraltriangle}}[3]{{\n\
                \\coordinate (#3) at (0, 0);\n\
                \\coordinate (#3-1) at (#1, 0); t\n\
                \\coordinate (#3-2) at ($(#3-1)!1!(#3)$);\n\
                \\coordinate (#3-3) at (rotate around={{60:(#3-1)}});\n\
                \\draw (#3-1) -- (#3-2) -- (#3-3) -- cycle;\n\
            }}\n\
            \\coordinate (A) at (\\a/2, {{\\a*sqrt(3)/2}});\n\
            \\coordinate (B) at (0, 0);\n\
            \\coordinate (C) at (\\a, 0);\n\
            \\drawtriangle{{A}}{{B}}{{C}};\n\
            \\node at (A) [above] {{\\scriptsize $A$}};\n\
            \\node at (B) [left] {{\\scriptsize $B$}};\n\
            \\node at (C) [right] {{\\scriptsize $C$}};\n\
            \\midpoint{{B}}{{C}}{{A1}}\n\
            \\midpoint{{C}}{{A}}{{B1}}\n\
            \\midpoint{{A}}{{B}}{{C1}}\n\
            \\fill[gray!20] (A1) -- (B1) -- (C1) -- cycle;\n\
            \\drawtriangle{{A1}}{{B1}}{{C1}};\n\
            \\node at (A1) [below] {{\\scriptsize $A_1$}};\n\
            \\node at (B1) [right] {{\\scriptsize $B_1$}};\n\
            \\node at (C1) [left] {{\\scriptsize $C_1$}};\n\
            \\midpoint{{B1}}{{C1}}{{A2}}\n\
            \\midpoint{{C1}}{{A1}}{{B2}}\n\
            \\midpoint{{A1}}{{B1}}{{C2}}\n\
            \\fill[gray!35] (A2) -- (B2) -- (C2) -- cycle;\n\
            \\drawtriangle{{A2}}{{B2}}{{C2}};\n\
            \\node at (A2) [above] {{\\scriptsize $A_2$}};\n\
            \\node at (B2) [left] {{\\scriptsize $B_2$}};\n\
            \\node at (C2) [right] {{\\scriptsize $C_2$}};\n\
            \\midpoint{{B2}}{{C2}}{{A3}}\n\
            \\midpoint{{C2}}{{A2}}{{B3}}\n\
            \\midpoint{{A2}}{{B2}}{{C3}}\n\
            \\fill[gray!50] (A3) -- (B3) -- (C3) -- cycle;\n\
            \\drawtriangle{{A3}}{{B3}}{{C3}};\n\
            \\node at (A3) [below] {{\\scriptsize $A_3$}};\n\
            \\node at (B3) [right] {{\\scriptsize $B_3$}};\n\
            \\node at (C3) [left] {{\\scriptsize $C_3$}};\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)  
        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B1_23]-SA-M2. Tính tổng cấp số nhân lùi vô hạn có u1 tùy ý.
def gh11gh_L11_C3_B1_23():
    n = symbols('n')
    chon=random.randint(1,2)
    chon=2
    if chon==1:
        while True:
            b = random.randint(2,9)
            q=1/b
            u1 = random.choice([random.randint(-5,-2), random.randint(1,5)])
            if all([u1!=b, u1!=-b, u1/(1-q)>-5]):
                break
    
    if chon==2:
        while True:
            a =  random.choice([i for i in range(-5, 6) if i!=0])
            b=a+random.randint(1,3)
            if b==0:
                continue

            q=a/b
            if q>=1:
                continue
            u1 = random.choice([random.randint(-5,-2), random.randint(1,5)])
            if all([u1!=1, u1!=-1, u1/(1-q)>-5]):
                break
    

    S=float(u1/(1-q))
    u2=u1*q
    u3=u1*q**2
    dau ="+"
    if u1*q<0: 
        dau = ""
    dau_ngoac_mo = "("
    dau_ngoac_dong = ")"
    if u1>0:
        dau_ngoac_mo = ""
        dau_ngoac_dong = ""

    if S.is_integer():
        noi_dung = f"Tính tổng của cấp số nhân lùi vô hạn $S={phan_so(u1)}{dau}{phan_so(u2)}+...+{dau_ngoac_mo}{phan_so(u1)}{dau_ngoac_dong}\\left({phan_so(q)}\\right)^n+..$."


        dap_an=int(S)

        noi_dung_loigiai=(
        f"Ta có: $u_1={u1},q={phan_so(q)}\\Rightarrow S=\\dfrac{{{u1}}}{{1-{phan_so(q)}}}={dap_an}$."
        ) 
    else:
        noi_dung = f"Tính tổng của cấp số nhân lùi vô hạn $S={phan_so(u1)}{dau}{phan_so(u2)}+...+{dau_ngoac_mo}{phan_so(u1)}{dau_ngoac_dong}\\left({phan_so(q)}\\right)^n+..$. (kết quả làm tròn đến hàng phần mười)."


        dap_an=f"{round_half_up(u1/(1-q),1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"Ta có: $u_1={u1},q={phan_so(q)}\\Rightarrow S=\\dfrac{{{u1}}}{{1-{phan_so(q)}}}={phan_so(S)}={dap_an}$."
        ) 

   
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B1_24]-SA-M3. Tính tổng diện tích các hình tròn lùi vô hạn
def gh11gh_L11_C3_B1_24():
    R=random.randint(4,12)
    code_hinh=(f" \\begin{{tikzpicture}}\n\
            \\begin{{scope}}\n\
                \\fill[blue!30] (0,0) circle(1.5);\n\
                \\draw (0,0) circle(1.5);\n\
                \\node at (0,-1.9) {{a)}};\n\
            \\end{{scope}}\n\
            \\begin{{scope}}[xshift=4cm]\n\
                \\fill[blue!30] (0,0) circle(1.5);\n\
                \\foreach \\x in {{-0.75, 0.75}} {{\n\
                    \\fill[yellow!30] (\\x,0) circle(0.75);\n\
                    \\draw (\\x,0) circle(0.75);\n\
                }}\n\
                \\draw (0,0) circle(1.5);\n\
                \\node at (0,-1.9) {{b)}};\n\
            \\end{{scope}}\n\
            \\begin{{scope}}[xshift=8cm]\n\
                \\fill[blue!30] (0,0) circle(1.5);\n\
                \\foreach \\x in {{-0.75, 0.75}} {{\n\
                    \\fill[yellow!30] (\\x,0) circle(0.75);\n\
                    \\draw (\\x,0) circle(0.75);\n\
                }}\n\
                \\foreach \\x in {{-1.125, -0.375, 0.375, 1.125}} {{\n\
                    \\fill[green!30] (\\x,0) circle(0.375);\n\
                    \\draw (\\x,0) circle(0.375);\n\
                }}\n\
                \\draw (0,0) circle(1.5);\n\
                \\node at (0,-1.9) {{c)}};\n\
            \\end{{scope}}\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    noi_dung = (
    f"  Từ tờ giấy, cắt một hình tròn bán kính $R={R}$ cm. Tiếp theo, cắt hai hình tròn bán kính $\\dfrac{{R}}{{2}}$ chồng lên hình tròn đầu tiên. Tiếp tục cắt bốn hình tròn bán kính $\\dfrac{{R}}{{4}}$ và chồng lên các hình trước, tiếp tục quá trình này mãi mãi. Tính tổng diện tích của các hình tròn  (kết quả làm tròn đến hàng đơn vị)."
    )
    dap_an=f"{round_half_up(2*pi*R**2,0):.0f}".replace(".",",")

    noi_dung_loigiai=(
    f"Gọi $u_1$ là diện tích của hình tròn đầu tiên, ta có $u_1 = \\pi R^2$.\n\n"
    f"Gọi $u_2$ là tổng diện tích của 2 hình tròn cắt lần thứ hai:\n\n "
    f"$u_2 = 2 \\pi \\left( \\dfrac{{R}}{{2}}\\right)^2 = \\pi R^2 \\cdot {phan_so(1/2)}$.\n\n"
    f"Gọi $u_3$ là tổng diện tích của 4 hình tròn cắt lần thứ ba:\n\n"
    f"$u_3 = 4 \\pi \\left( \\dfrac{{R}}{{4}} \\right)^2 = \\pi R^2 \\cdot \\dfrac{{1}}{{4}}$.\n\n"
    f"$u_n$ là tổng diện tích của $2^{{n-1}}$ hình tròn cắt lần thứ $n$:\n\n"
    f"$u_n = 2^{{n-1}} \\pi \\left( \\dfrac{{R}}{{2^{{n-1}}}} \\right)^2 = \\pi R^2 \\cdot \\dfrac{{1}}{{2^{{n-1}}}}$.\n\n"
    f"Vậy tổng diện tích của các hình tròn là:\n\n" 
    f"$S = \\pi R^2 + \\pi R^2 \\cdot \\dfrac{{1}}{{2}} + \\pi R^2 \\cdot \\dfrac{{1}}{{4}} + \\cdots = \\dfrac{{\\pi R^2}}{{1 - \\dfrac{{1}}{{2}}}} = 2 \\pi R^2 = 2 \\pi \\cdot 10^2 \\approx {dap_an}$." 


    )    
        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung}\n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
    f"\\end{{ex}}\n")
    return debai_word,loigiai_word,latex_tuluan,dap_an

    
 
########################### BÀI 2 - GIỚI HẠN HÀM SỐ ###########################

#[D11_C3_B2_01]. Tính giới hạn tại điểm - thay số trực tiếp
def gh11gh_L11_C3_B2_01():
    x = symbols('x')
    chon=random.randint(1,2)
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c= random.choice([i for i in range(-5, 6) if i!=0])
    d= random.choice([i for i in range(-5, 6) if i!=0])

    chon=random.randint(1,2)
    if chon==1:
        x_0=random.randint(-5,5)
        f=a*x**2+b*x+c
        noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} ({latex(f)})$." 
    if chon==2:
        if a*d-b*c==0: d=d+random.randint(1,2)
        f=(a*x+b)/(c*x+d)
        x_0=random.choice([random.randint(int(-d/c)-6, int(-d/c)-1), random.randint(int(-d/c)+2, int(-d/c)+5)])
        noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} {latex(f)}$." 
    if chon==3:        
        f=a/(c*x+d)
        x_0=random.choice([random.randint(int(-d/c)-6, int(-d/c)-1), random.randint(int(-d/c)+2, int(-d/c)+5)])
        noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} {latex(f)}$." 

    kq=f.subs(x,x_0)
    kq2=random.choice(["+\\infty","-\\infty"])
    kq_false=[kq+random.randint(1,3),kq+random.randint(4,5),kq-random.randint(4,5),kq-random.randint(1,2)]
    random.shuffle(kq_false)
    kq3,kq4=kq_false[0:2]

  
    #Trộn các phương án

    pa_A= f"*${{{latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${kq2}$"
    pa_C= f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{{latex(my_module.hien_phan_so(kq4))}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    

    noi_dung_loigiai=f""
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

#[D11_C3_B2_02]. Tính giới hạn dạng 0/0 - Bậc 2/Bậc 1
def gh11gh_L11_C3_B2_02():
    x = symbols('x')
    x_0 = random.choice([random.randint(-5, -1),random.randint(1, 5)])
    a = random.choice([random.randint(-10, -1),random.randint(1, 10)])
    b = random.randint(-10, 10)
    d = random.choice([random.randint(-15, -1), random.randint(1, 15)]) 
    e =-d*x_0
    c =-a*x_0**(2)-b*x_0
    f = (a*x**2 + b*x +c)/(d*x+e) 
    kq= limit(f, x, x_0)
    kq2=a/d
    kq3=a/e
    kq4=c/e
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{{latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{{latex(my_module.hien_phan_so(kq4))}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} {latex(f)}$."

    noi_dung_loigiai=f""
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


#[D11_C3_B2_03]-M3. Tính giới hạn dạng 0/0 - Bậc 2/Bậc 2
def gh11gh_L11_C3_B2_03():
    x = symbols('x')
    x_0 =  random.choice([i for i in range(-6, 6) ])
    x_1 =  random.choice([i for i in range(-5, 5) if i!=x_0])
    x_2 =  random.choice([i for i in range(-4, 4) if i!=x_0 and i!=x_1])

    a = random.choice([i for i in range(-3, 3) if i!=0])
    b = random.choice([i for i in range(-3, 3) if i!=0])
    
    kq= a*(x_0-x_1)/(b*(x_0-x_2))
    kq2=a/b
    kq3=a*(x_0+x_1+random.randint(1,2))/(b*(x_0-x_2))
    kq4=(a*x_1+random.randint(1,2))/b*x_2
    
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{phan_so(kq2)}}}$"
    pa_C= f"${{{phan_so(kq3)}}}$"
    pa_D= f"${{{phan_so(kq4)}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)

    f_tu=latex(expand(a*(x-x_0)*(x-x_1)))
    f_mau=latex(expand(b*(x-x_0)*(x-x_2)))
    
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} \\dfrac{{{f_tu}}}{{{f_mau}}}$."

    noi_dung_loigiai=(
        f"${st_lim(x_0)}\\dfrac{{{f_tu}}}{{{f_mau}}} $"
        f"$={st_lim(x_0)} \\dfrac{{{latex(a*(x-x_0)*(x-x_1))}}}{{{latex(b*(x-x_0)*(x-x_2))}}}$\n\n"
        f"$={st_lim(x_0)} \\dfrac{{{latex(a*(x-x_1))}}}{{{latex(b*(x-x_2))}}}$"
        f"$={phan_so(a*(x_0-x_1)/(b*(x_0-x_2)))}$."
        )
    
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

#[D11_C3_B2_04]. Tính giới hạn dạng 0/0: [Căn(ax+b)-c]/(dx+e)
def gh11gh_L11_C3_B2_04():
    x = symbols('x')
    x_0 = random.randint(-5, 5)

    #Tạo list chứa các hệ số
    a = [random.choice([random.randint(1,4),random.randint(-4,-1) ]) for _ in range(3)]

    x_0 = random.randint(1, 6)
    t=int(-a[1]/a[0])
    if a[0]>0:
        x_0=random.randint(t+1, t+10)
    else:
        x_0=random.randint(t-10, t-1)
    c = sqrt(a[0]*x_0+a[1])
    d =-a[2]*x_0
    f =(sqrt(a[0]*x+a[1])-c)/(a[2]*x+d) 

    kq= limit(f, x, x_0)
    kq2= a[0]/a[2]
    kq3= a[0]
    kq4=c/a[2]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{{latex(kq)}}}$"
    pa_B= f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{{latex(kq3)}}}$"
    pa_D= f"${{{latex(kq4)}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} {latex(f)}$."

    noi_dung_loigiai=f""
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

#[D11_C3_B2_05]. Tính giới hạn x-->00: Bậc tử = Bậc mẫu
def gh11gh_L11_C3_B2_05():
    bac = random.randint(2,4)
    f, heso_bac_f, heso_tudo_f = my_module.random_polynomial("x",bac)[0:3]
    g, heso_bac_g, heso_tudo_g  = my_module.random_polynomial("x",bac)[0:3]
    if heso_tudo_g==0:
        heso_tudo_g=heso_bac_f+1

    dau = random.choice(["+","-"])
    kq=heso_bac_f/heso_bac_g
    kq2=heso_bac_g/heso_bac_f
    kq3=heso_tudo_f/heso_tudo_g
    kq4=heso_tudo_f/heso_bac_g

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{{latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{{latex(my_module.hien_phan_so(kq4))}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {dau}\\infty}} {latex(f/g)}$."

    noi_dung_loigiai=f""
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

#[D11_C3_B2_06]. Tính giới hạn x-->00: Bậc tử < Bậc mẫu
def gh11gh_L11_C3_B2_06():
    bac = random.randint(3,4)
    f, heso_bac_f, heso_tudo_f = my_module.random_polynomial("x",bac-1)[0:3]
    g, heso_bac_g, heso_tudo_g  = my_module.random_polynomial("x",bac)[0:3]

    if heso_tudo_g==0:
        heso_tudo_g=heso_bac_f+1

    dau = random.choice(["+","-"])
    kq=0
    kq2=heso_bac_f/heso_bac_g
    kq3=heso_bac_g/heso_bac_f
    kq4=heso_tudo_f/heso_tudo_g

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{{kq}}}$. \t"
    pa_B= f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{{latex(my_module.hien_phan_so(kq4))}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {dau}\\infty}} {latex(f/g)}$."
    noi_dung_loigiai=f""
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

#[D11_C3_B2_07]. Tính giới hạn x-->00: Căn(A)/B
def gh11gh_L11_C3_B2_07():
    x=sp.symbols("x")
    x_0= random.choice([i for i in range(-5, 6) if i!=0])
    a= random.randint(2,3)
    b= random.randint(1,5)
    b=-2*a*x_0
    c=a*x_0**2+b
    f=a*x**2-2*a*x_0*x+a*x_0**2+b

    m = random.choice([i for i in range(-5, 6) if i!=0 and i!=1 and i!=-1])
    n = random.choice([i for i in range(-5, 6) if i!=0 and i!=1 and i!=-1])
    if n==m:n=n+random.randint(1,3)
    if n==0: n=n+random.randint(1,3)
    g=m*x+n

    dau = random.choice(["+","-"])
    vo_cung=f"{dau}\\infty"
    
    if dau=="+":
        kq=f"{latex(sqrt(a)/m)}"
        kq2=f"{latex(-sqrt(a)/m)}"
        kq3=random.choice([0,"+\\infty","-\\infty"])
        kq4=f"{random.choice([phan_so(a/m),phan_so(-a/m),phan_so(a/n),phan_so(-a/m),latex(sqrt(a)/n)])}"

    else:
        kq=f"{latex(-sqrt(a)/m)}"
        kq2=f"{latex(sqrt(a)/m)}"
        kq3=random.choice([0,"+\\infty","-\\infty"])
        kq4=f"{random.choice([phan_so(a/m),phan_so(-a/m),phan_so(a/n),phan_so(-a/m),latex(sqrt(a)/n) ])}" 

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {vo_cung}}} {latex(sqrt(f)/g)}$."
    noi_dung_loigiai=f""
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

#[D11_C3_B2_08]. Tính giới hạn x-->00: A/căn(B)
def gh11gh_L11_C3_B2_08():
       
    f, heso_bac_f, heso_tudo_f = my_module.random_dathuc_bac2_luon_duong("x")[0:3]
    g, heso_bac_g, heso_tudo_g  = my_module.random_polynomial("x",2)[0:3]
    if heso_tudo_g==0:
        heso_tudo_g=heso_bac_f+1      

    dau = random.choice(["+","-"])
    vo_cung=dau + "oo"
    kq=limit(g/sqrt(f),"x",vo_cung)
    kq1=heso_bac_g/heso_bac_f
    kq2=heso_tudo_f/heso_tudo_g
    if kq1==kq:
        kq1=kq+random.randint(1,10)
    if kq2==kq:
        kq2=kq-random.randint(1,10)
    if kq1==kq2:
        kq1=kq+2
        kq2=kq-2   

    pa_A= f"*${{{latex(kq)}}}$"
    pa_B= f"${{{latex(kq1)}}}$"
    pa_C= f"${{{latex(kq2)}}}$"
    pa_D= f"${{{dau}\\infty}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {dau}\\infty}} {latex(g/sqrt(f))}$."
    noi_dung_loigiai=f""
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

#[D11_C3_B2_09]. Cho limf(x) và limg(x). Tính lim f(x)g(x) hoặc lim f(x)/g(x).
def gh11gh_L11_C3_B2_09():
    x_0 = random.choice([i for i in range(-5, 6) if i!=0])
    lim_f = random.choice([i for i in range(-5, 6) if i!=0])

    lim_g = random.choice([i for i in range(-5, 6) if i!=0])

    if lim_g==lim_f:
        lim_g=x_0*lim_f      

    dau = random.choice(["*","/"])
    if dau=="*":
        kq=lim_f*lim_g
        kq2=lim_f/lim_g
        kq3=lim_g/lim_f
        kq4=lim_f+lim_g
        ham_so= f"[f(x)g(x)]"
    else:            
        kq=lim_f/lim_g
        kq2=lim_g/lim_f
        kq3=lim_f*lim_g
        kq4=lim_f+lim_g
        ham_so= "\\frac{{f(x)}}{{g(x)}}"
        
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    pa_A= f"*${{{latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${{{latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{{latex(my_module.hien_phan_so(kq4))}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Biết $\\lim \\limits_{{x \\to {x_0}}} f(x)= {lim_f}$ và $\\lim \\limits_{{x \\to {x_0}}} g(x)= {lim_g}$. Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} {ham_so}$."
    noi_dung_loigiai=f""
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

#[D11_C3_B2_10]. Tính giới hạn x-->00: Đa thức
def gh11gh_L11_C3_B2_10():
    bac=random.randint(3,5)
    f, heso_bac_f, heso_tudo_f  = my_module.random_polynomial("x",bac)[0:3]      

    dau = random.choice(["+","-"])
    vo_cung=dau + "oo"
    kq=limit(f,"x",vo_cung)
    if latex(kq)=="\\infty":
        kq="+\\infty"
    else:
        kq="-\\infty"        

    kq2=limit(-f,"x",vo_cung)
    if latex(kq2)=="\\infty":
        kq2="+\\infty"
    else:
        kq2="-\\infty"  
    kq3=heso_tudo_f
    kq4=heso_bac_f
    if kq3==kq4:
        kq4=kq3+random.randint(1,5)

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{latex(kq3)}}}$"
    pa_D= f"${{{latex(kq4)}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {dau}\\infty}}({latex(f)})$."
    noi_dung_loigiai=f""
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

#[D11_C3_B2_11]. Tính giới hạn dạng 0/0 - Bậc 1/Bậc 2
def gh11gh_L11_C3_B2_11():
    x = symbols('x')
    x_0 = random.choice([i for i in range(-6, 6) if i!=0])
    a = random.choice([i for i in range(-5, 5) if i!=0])
    f_tu=a*(x-x_0)

    x_1=random.choice([i for i in range(-6, 6) if i !=x_0])    
    m = random.choice([i for i in range(-3, 3) if i!=0])
    f_mau=m*(x-x_0)*(x-x_1)
    
    f = a/(m*(x-x_1))    
    kq=f.subs(x,x_0)

    kq2=a/m
    kq3=f.subs(x,x_0)+random.randint(1,3)
    kq4=f.subs(x,x_0)-random.randint(1,3)
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    
    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{phan_so(kq2)}}}$"
    pa_C= f"${{{phan_so(kq3)}}}$"
    pa_D= f"${{{phan_so(kq4)}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tính giới hạn $\\lim \\limits_{{x \\to {x_0}}} \\dfrac{{{latex(expand(f_tu))}}}{{{latex(expand(f_mau))}}}$."
    noi_dung_loigiai=(f"$\\lim \\limits_{{x \\to {x_0}}} \\dfrac{{{latex(expand(f_tu))}}}{{{latex(expand(f_mau))}}}$"
     f"$=\\lim \\limits_{{x \\to {x_0}}} \\dfrac{{{latex(f_tu)}}}{{{m}(x-{x_0})(x-{x_1})}}$\n\n"
    f"$=\\lim \\limits_{{x \\to {x_0}}}{latex(f)}={phan_so(kq)}$.")
    noi_dung_loigiai= noi_dung_loigiai.replace("--","+")
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C3_B2_12]-TF-M3. Cho hàm số kép. Xét Đ-S: lim x->a, giới hạn 1 bên, giới hạn tại x_0
def gh11gh_L11_C3_B2_12():
    x=sp.symbols("x")    
    chon=random.randint(1,2)    
    if chon==1:
        x_0 = random.choice([i for i in range(-5, 6) if i!=0])
        a = random.choice([i for i in range(-10, 10) if i!=0])
        b = random.choice([i for i in range(-10, 10) if i!=0])
        f=a*x+b

        m = random.choice([i for i in range(-2, 3) if i!=0])
        n = random.choice([i for i in range(-4, 4) if i!=0])
        p = random.choice([i for i in range(1, 5) if i!=0])
        g=sqrt(m**2*x**2+2*m*n*x+n**2+p)
        
    
    if chon==2:
        a = random.choice([i for i in range(-10, 10) if i!=0])
        b = random.choice([i for i in range(-10, 10) if i!=0])
        if a>0:
            x_0 = random.randint(int(-b/a)+2,int(-b/a)+7)
        else:
            x_0 = random.randint(int(-b/a)-6,int(-b/a)-2)

        f=a*x+b
        y_0=f.subs(x,x_0)        
      
        m =  y_0**2-x_0**2
        g=sqrt(x**2+m)    
    

    chon=random.randint(1,2)
    if chon==1:
        ham=f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(f)} \\text{{ khi }} x \\ge {x_0} \\\\ \n\
        {latex(g)} \\text{{ khi }} x < {x_0} \n\
        \\end{{array}} \\right.$"
    
    if chon==2:
        ham=f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(g)} \\text{{ khi }} x < {x_0} \\\\ \n\
        {latex(f)} \\text{{ khi }} x \\ge {x_0} \n\
        \\end{{array}} \\right.$" 

    
    noi_dung = f"Cho hàm số {ham}. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    x_1 = random.randint(x_0+1,x_0+6)
    f_1=f.subs(x,x_1)
    g_1=g.subs(x,x_1)
    if g_1==f_1: g_1=f_1+random.randint(1,3)
    kq1_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}={f_1}$" 
    kq1_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}={latex(g_1)}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} ({latex(f)})={f_1}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_2 = random.randint(x_0-6,x_0-1)    
    g_2=g.subs(x,x_2)
    f_2=f.subs(x,x_2)
    if f_2==g_2: f_2=f_2+random.randint(1,2)

    kq2_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}={latex(g_2)}$"
    kq2_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}={f_2}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} ({latex(g)})={latex(g_2)}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    f_0=f.subs(x,x_0)
    g_0=g.subs(x,x_0)
    chon=random.randint(1,2)

    if chon==1:
        
        kq3_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={f_0}$" 
        kq3_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={f_0+random.randint(1,3)}$"        
        HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$."
    
    if chon==2:
        
        kq3_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}={latex(g_0)}$" 
        kq3_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={latex(g_0+random.randint(1,2))}$"        
        HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(f)}) = {latex(g_0)}$."    
    
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if f_0==g_0:
        kq4_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}={f_0}$"
        kq4_F=f" Hàm số không tồn tại giới hạn tại ${{{x_0}}}$" 
    
        HDG=(f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(g)}) = {latex(g_0)}$.\n\n"
        f"Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}$"
        f" nên $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}={f_0}$."
        )
    else:
        kq4_T=f"*Hàm số không tồn tại giới hạn tại ${{{x_0}}}$"
        kq4_F=f"  Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}={f_0}$"

        HDG=(f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(g)}) = {latex(g_0)}$.\n\n"
        f"Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}\\ne \\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}$"
        f" nên hàm số không tồn tại giới hạn tại ${{{x_0}}}$."
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

#[D11_C3_B2_13]-TF-M3. Cho f(x)=ax+b và mx^2+nx+p. Xét Đ-S: lim x->a, giới hạn 1 bên, giới hạn tại x_0
def gh11gh_L11_C3_B2_13():
    x=sp.symbols("x")    
    chon=random.randint(1,2)
       
    if chon==1:
        x_0 = random.choice([i for i in range(-5, 6) if i!=0])
        a = random.choice([i for i in range(-10, 10) if i!=0])
        b = random.choice([i for i in range(-10, 10) if i!=0])
        f=a*x+b

        m = random.choice([i for i in range(-2, 3) if i!=0])
        n = random.choice([i for i in range(-4, 4) if i!=0])
        p = random.choice([i for i in range(1, 5) if i!=0])
        g=m**2*x**2+2*m*n*x+n**2+p
        
    
    if chon==2:
        a = random.choice([i for i in range(-10, 10) if i!=0])
        b = random.choice([i for i in range(-10, 10) if i!=0])
        if a>0:
            x_0 = random.randint(int(-b/a)+2,int(-b/a)+7)
        else:
            x_0 = random.randint(int(-b/a)-6,int(-b/a)-2)

        f=a*x+b
        y_0=f.subs(x,x_0)        
      
        m = random.choice([i for i in range(-2, 3) if i!=0])
        n = random.choice([i for i in range(-4, 4) if i!=0])
        p=y_0-m*x_0**2-n*x_0
        g=m*x**2+n*x+p
    

    chon=random.randint(1,2)
    if chon==1:
        ham=f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(f)} \\text{{ khi }} x \\ge {x_0} \\\\ \n\
        {latex(g)} \\text{{ khi }} x < {x_0} \n\
        \\end{{array}} \\right.$"
    
    if chon==2:
        ham=f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(g)} \\text{{ khi }} x < {x_0} \\\\ \n\
        {latex(f)} \\text{{ khi }} x \\ge {x_0} \n\
        \\end{{array}} \\right.$" 

    
    noi_dung = f"Cho hàm số {ham}. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    x_1 = random.randint(x_0+1,x_0+6)
    f_1=f.subs(x,x_1)
    g_1=g.subs(x,x_1)
    if g_1==f_1: g_1=f_1+random.randint(1,3)
    kq1_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}={f_1}$" 
    kq1_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}={latex(g_1)}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} ({latex(f)})={f_1}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_2 = random.randint(x_0-6,x_0-1)    
    g_2=g.subs(x,x_2)
    f_2=f.subs(x,x_2)
    if f_2==g_2: f_2=f_2+random.randint(1,2)

    kq2_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}={latex(g_2)}$"
    kq2_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}={f_2}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} ({latex(g)})={latex(g_2)}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    f_0=f.subs(x,x_0)
    g_0=g.subs(x,x_0)
    chon=random.randint(1,2)

    if chon==1:
        
        kq3_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={f_0}$" 
        kq3_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={f_0+random.randint(1,3)}$"        
        HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$."
    
    if chon==2:
        
        kq3_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}={latex(g_0)}$" 
        kq3_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={latex(g_0+random.randint(1,2))}$"        
        HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(f)}) = {latex(g_0)}$."    
    
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if f_0==g_0:
        kq4_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}={f_0}$"
        kq4_F=f" Hàm số không tồn tại giới hạn tại ${{{x_0}}}$" 
    
        HDG=(f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(g)}) = {latex(g_0)}$.\n\n"
        f"Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}$"
        f" nên $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}={f_0}$."
        )
    else:
        kq4_T=f"*Hàm số không tồn tại giới hạn tại ${{{x_0}}}$"
        kq4_F=f"  Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}={f_0}$"

        HDG=(f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(g)}) = {latex(g_0)}$.\n\n"
        f"Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}\\ne \\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}$"
        f" nên hàm số không tồn tại giới hạn tại ${{{x_0}}}$."
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

#[D11_C3_B2_14]-TF-M3. Cho f(x)=(ax^2+bx+c)/(dx+e). Xét Đ-S: lim x->a, khử vô định, giới hạn tại x_0
def gh11gh_L11_C3_B2_14():
    x=sp.symbols("x")    
    x_1 = random.choice([i for i in range(-7, 7) if i!=0])
    x_2 = random.choice([i for i in range(-7,7) if i != x_1  and i!=0])

    a = random.choice([i for i in range(-3, 3) if i!=0])
    b,c=-a*(x_1+x_2),a*x_1*x_2

    f_tu=latex(a*x**2+b*x+c)
    m = random.choice([i for i in range(-5, 5) if i!=0 and i!=1])
    f_mau=latex(m*(x-x_1))

    g=a*(x-x_2)/m

    ham=f"\\dfrac{{{f_tu}}}{{{f_mau}}}"

    noi_dung = f"Cho hàm số $f(x)={ham}$. Xét tính đúng-sai của các khẳng định sau:"        
    debai_word= f"{noi_dung}\n"

    x_0 = random.choice([i for i in range(-7,7) if i != x_1  and i != x_2])
    kq=g.subs(x,x_0)

    kq1_T=f"* ${st_lim(x_0)} {ham}= {phan_so(kq)}$" 
    kq1_F=f"${st_lim(x_0)} {ham}= {phan_so(kq+random.randint(1,2))}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"${st_lim(x_0)} {ham}= {phan_so(kq)}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    kq=g.subs(x,x_1)
    kq2_T=f"* ${st_lim(x_1)} {ham}= {phan_so(kq)}$"
    kq2_F=f"${st_lim(x_1)} {ham}= {phan_so(kq+random.randint(1,2))}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=(f"${st_lim(x_1)} {ham}={st_lim(x_1)} \\dfrac{{{a}({latex(x-x_1)})({latex(x-x_2)})}}{{{m}({latex(x-x_1)})}}$"
    f"$={st_lim(x_1)} \\dfrac{{{a}({latex(x-x_2)})}}{{{m}}}={phan_so(kq)}$.")
    HDG=HDG.replace("-1(","-1(").replace("1(","(")
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    chon=random.randint(1,2)

    if chon==1:
        if a/m>0:
            kq3_T=f"* ${st_lim("+\\infty")} {ham}=+\\infty$" 
            kq3_F=f"${st_lim("+\\infty")} {ham}=-\\infty$"
            HDG=(f"${st_lim("+\\infty")} {ham}= {st_lim("+\\infty")} \\dfrac{{{a}({latex(x-x_2)})}}{{{m}}}=+\\infty$.\n\n"
        f"Vì: ${st_lim("+\\infty")} {phan_so(a/m)}>0$ và ${st_lim("+\\infty")}({latex(x-x_2)})=+\\infty$.")
        else:
            kq3_T=f"* ${st_lim("+\\infty")} {ham}=-\\infty$" 
            kq3_F=f"${st_lim("+\\infty")} {ham}=+\\infty$"
            HDG=(f"${st_lim("+\\infty")} {ham}= {st_lim("+\\infty")} \\dfrac{{{a}({latex(x-x_2)})}}{{{m}}}=-\\infty$.\n\n"
        f"Vì: ${st_lim("+\\infty")} {phan_so(a/m)}<0$ và ${st_lim("+\\infty")}({latex(x-x_2)})=+\\infty$.")
    
    if chon==2:
        if a/m>0:
            kq3_T=f"* ${st_lim("-\\infty")} {ham}=-\\infty$" 
            kq3_F=f"${st_lim("-\\infty")} {ham}=+\\infty$"
            HDG=(f"${st_lim("-\\infty")} {ham}= {st_lim("-\\infty")} \\dfrac{{{a}({latex(x-x_2)})}}{{{m}}}=-\\infty$.\n\n"
        f"Vì: ${st_lim("-\\infty")} {phan_so(a/m)}>0$ và ${st_lim("-\\infty")}({latex(x-x_2)})=-\\infty$.")
        else:
            kq3_T=f"* ${st_lim("-\\infty")} {ham}=+\\infty$" 
            kq3_F=f"${st_lim("-\\infty")} {ham}=-\\infty$"
            HDG=(f"${st_lim("-\\infty")} {ham}= {st_lim("-\\infty")} \\dfrac{{{a}({latex(x-x_2)})}}{{{m}}}=+\\infty$.\n\n"
        f"Vì: ${st_lim("-\\infty")} {phan_so(a/m)}<0$ và ${st_lim("-\\infty")}({latex(x-x_2)})=-\\infty$.")
    
    
    kq3=random.choice([kq3_T, kq3_F])
    HDG=HDG.replace("-1(","-1(").replace("1(","(")
    
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    p= random.choice([i for i in range(-10, 10) if i!=0])
    t_p=sp.symbols("a")
    x_4 = random.choice([i for i in range(-7,7) if i!=x_1 and i!=x_0])

    d= random.choice([i for i in range(-5, 6) if i!=0])
    e= random.choice([i for i in range(-5, 6) if i!=0])


    kq4_T=f"* Biết ${st_lim(x_4)} \\left[{ham}-a\\right]={g.subs(x,x_4)-p}$. Khi đó ${latex(d*t_p+e)}={d*p+e}$"
    kq4_F=f"Biết ${st_lim(x_4)} \\left[{ham}-a\\right]={g.subs(x,x_4)-p}$. Khi đó ${latex(d*t_p+e)}={d*p+e+random.randint(1,2)}$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"${st_lim(x_4)} \\left[{ham}-a\\right]={st_lim(x_4)} {ham}-a={g.subs(x,x_4)}-a$\n\n"
        f"Suy ra ${g.subs(x,x_4)}-a={g.subs(x,x_4)-p}$"
    f"$\\Rightarrow a={p} \\Rightarrow {latex(d*t_p+e)}={d*p+e}$.")
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

#[D11_C3_B2_15]-SA-M2. f(x)= (căn(ax+b)-c)/(x+d). Tìm lim->x_0
def gh11gh_L11_C3_B2_15():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-7, 8) if i!=0])
        b = random.choice([i for i in range(-7, 8) if i!=0])
        if a>0:
            x_0=int(-b/a)+random.randint(1,5)
        else:
            x_0=int(-b/a)-random.randint(1,5)

        c=sqrt(a*x_0+b)
        if sqrt(a*x_0+b)+c==0:
            continue  

        d=-x_0
        f=(sqrt(a*x+b)-c)/(x+d)
        thuong, du = div(a*x+b-c**2, x+d)
        f_lh=(a*x+b-c**2)/((x+d)*(sqrt(a*x+b)+c))

        g=thuong/(sqrt(a*x+b)+c)
        #lim_value=g.subs(x,x_0)
        lim_value=limit(f, x, x_0)
        if all([x_0!=0,lim_value>-5]):
            break
    if float(lim_value).is_integer():
        noi_dung = (
        f"Tính giới hạn ${st_lim(x_0)}{latex(f)}$."
        )
        dap_an=f"{round_half_up(lim_value,1):.1f}".replace(".",",")
    else:

        noi_dung = (
        f"Tính giới hạn ${st_lim(x_0)}{latex(f)}$ (kết quả làm tròn đến hàng phần mười)"
        )
        dap_an=f"{round_half_up(lim_value,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"${st_lim(x_0)}{latex(f)}={st_lim(x_0)}\\dfrac{{{latex(a*x+b)}-{c**2}}}{{({latex(x+d)})({latex(sqrt(a*x+b)+c)})}}$\n\n"
    f"$={st_lim(x_0)}{latex(thuong/(sqrt(a*x+b)+c))}={latex(lim_value)}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B2_16]-SA-M2. f(x)= (x+d)/(căn(ax+b)-c). Tìm lim->x_0
def gh11gh_L11_C3_B2_16():
    x=sp.symbols("x")
    while True:
        a = random.choice([i for i in range(-7, 8) if i!=0])
        b = random.choice([i for i in range(-7, 8) if i!=0])
        if a>0:
            x_0=int(-b/a)+random.randint(1,5)
        else:
            x_0=int(-b/a)-random.randint(1,5)

        c=sqrt(a*x_0+b)
        if sqrt(a*x_0+b)+c==0:
            continue  

        d=-x_0
        f=(x+d)/(sqrt(a*x+b)-c)
        
        f_lh=((x+d)*(sqrt(a*x+b)+c))/(a*x+b-c**2)
        thuong, du = div(x+d, a*x+b-c**2)

        g=thuong*(sqrt(a*x+b)+c)
        #lim_value=g.subs(x,x_0)
        lim_value=limit(f, x, x_0)
        if all([x_0!=0,lim_value>-5]):
            break
    if float(lim_value).is_integer():
        noi_dung = (
        f"Tính giới hạn ${st_lim(x_0)}{latex(f)}$."
        )
        dap_an=f"{round_half_up(lim_value,1):.1f}".replace(".",",")
    else:

        noi_dung = (
        f"Tính giới hạn ${st_lim(x_0)}{latex(f)}$ (kết quả làm tròn đến hàng phần mười)"
        )
        dap_an=f"{round_half_up(lim_value,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"${st_lim(x_0)}{latex(f)}={st_lim(x_0)}\\dfrac{{({latex(x+d)})({latex(sqrt(a*x+b)+c)})}}{{{latex(a*x+b)}-{c**2}}}$\n\n"
    f"$={st_lim(x_0)}({latex(thuong*(sqrt(a*x+b)+c))})={latex(lim_value)}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B2_17]-SA-M2. f(x)= (ax^2+bx+c)/(mx^2+dx+e). Tìm lim->x_0
def gh11gh_L11_C3_B2_17():
    x=sp.symbols("x")
    while True:
        x1,x2,x3=random.sample(range(-6,7),3)
        
        a= random.choice([i for i in range(-3, 4) if i!=0])
        m= random.choice([i for i in range(-3, 4) if i!=0])

        f_tu=a*(x-x1)*(x-x2)
        f_mau=m*(x-x1)*(x-x3)
        f=f_tu/f_mau
        lim_value=limit(f,x,x1)
        if lim_value>-5:
            break
    ham=f"{st_lim(x1)}\\dfrac{{{latex(expand(f_tu))}}}{{{latex(expand(f_mau))}}}"
    if float(lim_value).is_integer():

        noi_dung = (
        f"Tính giới hạn ${ham}$."
        )
        dap_an=lim_value

        noi_dung_loigiai=(
        f"${ham}={st_lim(x1)}\\dfrac{{{latex(f_tu)}}}{{{latex(f_mau)}}}={st_lim(x1)}\\dfrac{{{latex(a*(x-x2))}}}{{{latex(m*(x-x3))}}}={phan_so(lim_value)}.$"
        )
    else:
        noi_dung = (
        f"Tính giới hạn ${ham}$ (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round_half_up(lim_value,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"${ham}={st_lim(x1)}\\dfrac{{{latex(f_tu)}}}{{{latex(f_mau)}}}={st_lim(x1)}\\dfrac{{{latex(a*(x-x2))}}}{{{latex(m*(x-x3))}}}={phan_so(lim_value)}={dap_an}.$"
        )    
              
            
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B2_18]-SA-M2. f(x)= (ax^2+bx+c)/(dx+e). Tìm lim->x_0
def gh11gh_L11_C3_B2_18():
    x=sp.symbols("x")
    while True:
        x1,x2,x3=random.sample(range(-6,7),3)
        
        a= random.choice([i for i in range(-3, 4) if i!=0])
        m= random.choice([i for i in range(-5, 6) if i not in [0,1,-2]])

        f_tu=a*(x-x1)*(x-x2)
        f_mau=m*(x-x1)
        f=f_tu/f_mau
        lim_value=limit(f,x,x1)
        if lim_value>-5:
            break
    ham=f"{st_lim(x1)}\\dfrac{{{latex(expand(f_tu))}}}{{{latex(f_mau)}}}"
    if float(lim_value).is_integer():

        noi_dung = (
        f"Tính giới hạn ${ham}$."
        )
        dap_an=lim_value

        noi_dung_loigiai=(
        f"${ham}={st_lim(x1)}\\dfrac{{{latex(f_tu)}}}{{{latex(f_mau)}}}={st_lim(x1)}\\dfrac{{{latex(a*(x-x2))}}}{{{m}}}={phan_so(lim_value)}.$"
        )
    else:
        noi_dung = (
        f"Tính giới hạn ${ham}$ (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round_half_up(lim_value,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"${ham}={st_lim(x1)}\\dfrac{{{latex(f_tu)}}}{{{latex(f_mau)}}}={st_lim(x1)}\\dfrac{{{latex(a*(x-x2))}}}{{{m}}}={phan_so(lim_value)}={dap_an}.$"
        )    
              
            
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B2_19]-SA-M2. f(x)= (ax^3+bx^2+cx+d)/(mx^2+nx+p). Tìm lim->x_0
def gh11gh_L11_C3_B2_19(): 
    x = sp.symbols("x")
    while True:
        # 3 nghiệm khác nhau cho tử
        x1, x2, x3 = random.sample(range(-6, 6), 3)

        # 2 nghiệm (1 trùng x1 để tạo 0/0) và 1 nghiệm khác
        x4 = x1
        while True:
            x5 = random.choice(range(-6, 6))
            if x5 not in [x1,x2,x3]:
                break

        # hệ số
        a = random.choice([i for i in range(-3, 4) if i != 0])
        m = random.choice([i for i in range(-4, 4) if i !=0])

        # Tử bậc 3, mẫu bậc 2 (đảm bảo dạng 0/0 tại x1)
        f_tu = a * (x - x1) * (x - x2) * (x - x3)
        f_mau = m * (x - x4) * (x - x5)
        f = f_tu / f_mau

        lim_value = limit(f, x, x1)

        # Điều kiện tránh số quá lớn
        if lim_value>-5:
            break

    ham = f"{st_lim(x1)}\\dfrac{{{latex(expand(f_tu))}}}{{{latex(expand(f_mau))}}}"

    # ======= TRƯỜNG HỢP ĐÁP ÁN LÀ SỐ NGUYÊN =======
    if float(lim_value).is_integer():
        dap_an = lim_value
        noi_dung = f"Tính giới hạn ${ham}$."

        noi_dung_loigiai = (
            f"${ham}"
            f"={st_lim(x1)}\\dfrac{{{latex(f_tu)}}}{{{latex(f_mau)}}}"
            f"={st_lim(x1)}\\dfrac{{{latex(a*(x-x2)*(x-x3))}}}{{{latex(m*(x-x5))}}}"
            f"={phan_so(lim_value)}.$"
        )

    # ======= TRƯỜNG HỢP KẾT QUẢ LẺ =======
    else:
        dap_an = f"{round_half_up(lim_value,1):.1f}".replace(".",",")

        noi_dung = (
            f"Tính giới hạn ${ham}$ (kết quả làm tròn đến hàng phần mười)."
        )

        noi_dung_loigiai = (
            f"${ham}"
            f"={st_lim(x1)}\\dfrac{{{latex(f_tu)}}}{{{latex(f_mau)}}}"
            f"={st_lim(x1)}\\dfrac{{{latex(a*(x-x2)*(x-x3))}}}{{{latex(m*(x-x5))}}}"
            f"={phan_so(lim_value)}={dap_an}.$"
        )

    # ====== XUẤT DỮ LIỆU ======
    debai_word = f"{noi_dung}\n"

    loigiai_word = (
        f"Lời giải:\n {noi_dung_loigiai}\n"
        f"Đáp án: {dap_an}\n"
    )

    latex_tuluan = (
        "\\begin{ex}\n"
        f"{noi_dung}\n\n"
        f"\\shortans[4]{{{dap_an}}}\n\n"
        f"\\loigiai{{\n{noi_dung_loigiai}\n}}\n"
        "\\end{ex}\n"
    )

    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C3_B2_20]-SA-M3. f(x)= (căn(ax+b)-c)/(mx^2+nx+p). Tìm lim->x_0
def gh11gh_L11_C3_B2_20():
    x = sp.symbols("x")

    while True:
        # ===== 1. Chọn nghiệm x0 =====
        x0,x1 = random.sample(range(-5, 6),2)

        m = random.choice([i for i in range(-2, 3) if i!=0])

        # ===== 3. Tạo tử số bảo đảm √(a x0 + b) = c và ax0+b > 0 =====
        a = random.choice([i for i in range(-5, 5) if i !=0])
        c = random.choice([i for i in range(-5, 5) if i != 0])  # đảm bảo căn >0
        b = c**2 - a * x0

        if a*x0 + b <= 0:     # kiểm tra điều kiện căn
            continue
        if sqrt(a*x0+b)+c==0:
            continue
        f_tu=sp.sqrt(a*x + b) - c
        f_mau=m*(x-x0)*(x-x1)
        k=random.randint(4,10)

        f = k*f_tu / f_mau
        lim_value = limit(f, x, x0)
        if lim_value>-5:
            break
    n=-m*x0-m*x1
    p=m*x0*x1

    ham = f"{st_lim(x0)}\\dfrac{{{latex(k*f_tu)}}}{{{latex(expand(f_mau))}}}"


    if float(lim_value).is_integer():
        dap_an = lim_value
        noi_dung = f"Tính giới hạn ${ham}$."

        noi_dung_loigiai = (
            f"${ham}"
            f"={st_lim(x0)}{k}\\dfrac{{{latex(a*x+b)}-{c**2}}}{{{latex(f_mau)}({latex(sqrt(a*x+b)+c)})}}"
            f"={phan_so(lim_value)}.$"
        )

    else:
        dap_an = f"{round_half_up(lim_value,1):.1f}".replace(".",",")

        noi_dung = (
            f"Tính giới hạn ${ham}$ (kết quả làm tròn đến hàng phần mười)."
        )

        noi_dung_loigiai = (
            f"${ham}"
            f"={st_lim(x0)}{k}\\dfrac{{{latex(a*x+b)}-{c**2}}}{{{latex(f_mau)}({latex(sqrt(a*x+b)+c)})}}"
            f"={phan_so(lim_value)}={dap_an}.$"
        )

    # ======== 10. Xuất dataset ========
    debai_word = f"{noi_dung}\n"

    loigiai_word = (
        f"Lời giải:\n {noi_dung_loigiai}\n"
        f"Đáp án: {dap_an}\n"
    )

    latex_tuluan = (
        "\\begin{ex}\n"
        f"{noi_dung}\n\n"
        f"\\shortans[4]{{{dap_an}}}\n\n"
        f"\\loigiai{{\n{noi_dung_loigiai}\n}}\n"
        "\\end{ex}\n"
    )

    return debai_word, loigiai_word, latex_tuluan, dap_an




############# BÀI 3 - HÀM SỐ LIÊN TỤC 
#[D11_C3_B3_01]. Cho f(x)=căn(ax+b). Xét tính liên tục tại điểm.
def gh11gh_L11_C3_B3_01():
       
    x = sp.symbols('x')
    a= random.choice([random.randint(-8, -1), random.randint(1, 8)])   
    b= random.choice([random.randint(-7, -1), random.randint(1, 7)])         

    f=sqrt(a*x+b)

    if a>0:
        #Tạo điểm liên tục 
        x_1=random.randint(int(-b/a)+2,int(-b/a)+5)
        x_2=random.randint(int(-b/a)+6,int(-b/a)+20)

        #Tạo điểm gián đoạn
        x_3=random.randint(int(-b/a)-9,int(-b/a))
        x_4=random.randint(int(-b/a)-15,int(-b/a)-10)           
    else:
        #Tạo điểm liên tục 
        x_1=random.randint(int(-b/a)-5,int(-b/a)-2)
        x_2=random.randint(int(-b/a)-20,int(-b/a)-6)

        #Tạo điểm gián đoạn
        x_3=random.randint(int(-b/a)+1,int(-b/a)+9)
        x_4=random.randint(int(-b/a)+10,int(-b/a)+15)

    kq=f"Hàm số liên tục tại điểm $x={x_1}$"            
    kq2=f"Hàm số gián đoạn tại điểm $x={x_2}$"
    kq3=f"Hàm số liên tục tại điểm $x={x_3}$"
    kq4=f"Hàm số liên tục tại điểm $x={latex(my_module.hien_phan_so(x_4))}$"    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Cho hàm số $y={latex(f)}$. Tìm khẳng định đúng."
    noi_dung_loigiai=f""
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

#[D11_C3_B3_02]. Cho f(x)=(ax+b)/(cx+d). Tìm khoảng liên tục.
def gh11gh_L11_C3_B3_02():
    x = sp.symbols('x')
    a = random.randint(-8,8)
    if a==0:
        a = a + random.randint(1,8)       
    b = random.randint(-7,7)

    c = random.randint(-4,4)
    if c==0:
        c = c + random.randint(1,5)
    d = random.randint(-5,5)

    if a*d-b*c==0:
        d=d+1     
    f=(a*x+b)/(c*x+d)

    x_0=-d/c
    x_1=int(x_0)+random.randint(1,4)
    x_2=int(x_0)-random.randint(1,4)

    t=random.randint(1,4)
    if t==1:
        khoang_lien_tuc=f"({latex(my_module.hien_phan_so(x_0))};+\\infty)"
    if t==2:
        khoang_lien_tuc=f"(-\\infty;{latex(my_module.hien_phan_so(x_0))})"
    if t==3:
        khoang_lien_tuc=f"(-\\infty;{x_2})"
    if t==4:
        khoang_lien_tuc=f"({x_1};+\\infty)"


    kq=f"Hàm số liên tục trên khoảng ${khoang_lien_tuc}$"            
    kq2=f"Hàm số liên tục trên khoảng $(-\\infty;{x_1})$"
    kq3=f"Hàm số liên tục trên khoảng $({x_2};+\\infty)$"
    kq4=f"Hàm số liên tục trên khoảng $({x_2};{x_1})$"    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Cho hàm số $y={latex(f)}$. Tìm khẳng định đúng."
    noi_dung_loigiai=f""
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

#[D11_C3_B3_03]. Cho f(x) có >=,<. Xét tính liên tục tại điểm.
def gh11gh_L11_C3_B3_03():
    #Tạo hàm thứ nhất
    a = random.randint(-3,3)
    if a==0:
        a = a + 1
    b = random.randint(-4,4)
    c = random.randint(-5,3)
    
    x = sp.symbols('x')
    f = a*x**2 + b*x + c

    #Tạo t là điểm phân chia hàm
    x_0 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
   
    f_x = f.subs(x, x_0)

    #Tạo hàm thứ hai và đảm bảo liên tục tại x_0
    d = random.randint(-7,7)
    if d==0:
        d = d + 1
    e = f_x - d*x_0
    g = d*x + e

    #Tạo hàm số không liên tục tại x_0
    h= (d+1)*x +e

    chon= random.choice(["h","g"])
    if chon == "g":
        ham_so = g
        khang_dinh = "sai"
        kq=f"Hàm số không liên tục tại $x={x_0}$"
        kq2 = f"Hàm số liên tục tại $x={x_0}$"
        kq3=f"Hàm số liên tục tại $x={x_0+random.randint(1,10)}$"
        kq4=f"Hàm số liên tục tại mọi $x\\in \\mathbb{{R}}$"
    else:
        ham_so = h
        khang_dinh = "đúng"
        kq=f"Hàm số không liên tục tại $x={x_0}$"
        kq2 = f"Hàm số liên tục tại $x={x_0}$"
        kq3=f"Hàm số không liên tục tại $x={x_0+random.randint(1,10)}$"
        kq4=f"Hàm số liên tục tại mọi $x\\in \\mathbb{{R}}$"   

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $f(x)=\\left\\{{ \\begin{{array}}{{l}} \n \
 {latex(f)} \\text{{ khi }} x \\ge {x_0}  \\\\ \n \
{latex(ham_so)} \\text{{          khi  }} x < {x_0}  \n \
\\end{{array}} \\right.$. Tìm khẳng định {khang_dinh}."

    noi_dung_loigiai=f""
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

#[D11_C3_B3_04]. Cho f(x) có phân thức bậc 3. Tìm m để f(x) liên tục tại x_0.
def gh11gh_L11_C3_B3_04():
    #Tạo hàm thứ nhất
    x = sp.symbols('x')
    x_0 = random.choice([i for i in range(-5, 6) if i!=0])
    x_1=x_0+random.randint(1,4)


    a1 = random.choice([i for i in range(-3, 3) if i!=0])
    b1 = random.choice([i for i in range(-4, 4) if i!=0])
    c1=random.randint(-5,5)

    #Tạo hàm số thứ nhất
    f = (x-x_0)*(a1*x**2+b1*x+c1)
    a2 = random.choice([i for i in range(-5, 6) if i!=0])
  
    g=a2*(x-x_0)*(x-x_1)

    #Tạo hàm thứ 2: mx+b2
    b2 = random.choice([i for i in range(-5, 6) if i!=0])
    dau="+"
    if b2<0:
        dau=""
        
    kq=(limit(f/g, x, x_0)-b2)/x_0
    kq2 = (limit(f/g, x, x_0)+b2)/x_0
    kq3=(limit(f/g, x, x_0))/x_0
    kq4=(limit(f/g, x, x_0))/x_1

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*$m={latex(kq)}$"
    pa_B= f"$m={latex(kq2)}$"
    pa_C= f"$m={latex(kq3)}$"
    pa_D= f"$m={latex(kq4)}$"

     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $f(x)=\\left\\{{ \\begin{{array}}{{l}} \n \
 {latex(f/g)} \\text{{ khi }} x \\ne {x_0}  \\\\ \n \
mx{dau}{b2} \\text{{          khi  }} x = {x_0}  \n \
\\end{{array}} \\right.$. Tìm m để hàm số đã cho liên tục tại điểm $x={x_0}$."
    noi_dung_loigiai=f""
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

#[D11_C3_B3_05]. Cho f(x) có phân thức bậc 2. Tìm m để f(x) liên tục tại x_0.
def gh11gh_L11_C3_B3_05():
    x = symbols('x')
    x_0 = random.randint(-5, 5)
    if x_0==0:
        x_0=random.randint(1, 5)

    #Tạo list chứa các hệ số
    a = [random.randint(-4, 4) for _ in range(4)]
    if a[0]==0:
        a[0] = random.randint(1, 5)
    if a[2]==0:
        a[2] = random.randint(1, 5)
    c_1 = -a[0]*x_0**(2)-a[1]*x_0
    c_2 = -a[2]*x_0**(2)-a[3]*x_0

    f = (a[0]*x**2 + a[1]*x + c_1)/(a[2]*x**2 + a[3]*x +c_2)

    gioi_han = limit(f, x, x_0)        

    #Tạo hàm thứ 2: mx+b2
    b2 = random.randint(-4,4)
    if b2==0:
        b2 = random.randint(1,3)
    dau="+"
    if b2<0:
        dau=""

    kq=(gioi_han-b2)/x_0
    kq2=(gioi_han+b2)/x_0
    kq3=gioi_han/x_0
    kq4=gioi_han-b2

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=latex(kq)
    kq2 =latex(kq2)
    kq3=latex(kq3)
    kq4=latex(kq4)

    #Tạo các phương án
    pa_A= f"*$m={kq}$"
    pa_B= f"$m={kq2}$"
    pa_C= f"$m={kq3}$"
    pa_D= f"$m={kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $f(x)=\\left\\{{ \\begin{{array}}{{l}} \n \
 {latex(f)} \\text{{ khi }} x \\ne {x_0}  \\\\ \n \
mx{dau}{b2} \\text{{          khi  }} x = {x_0}  \n \
\\end{{array}} \\right.$. Tìm m để hàm số đã cho liên tục tại điểm $x={x_0}$."
    noi_dung_loigiai=f""
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


#[D11_C3_B3_06]-TF-M2. f(x) là 2 hàm đa thức. Xét Đ-S: giới hạn, liên tục tại x_0.
def gh11gh_L11_C3_B3_06():
    x=sp.symbols("x")    
    chon=random.randint(1,2)
       
    if chon==1:
        x_0 = random.choice([i for i in range(-5, 6) if i!=0])
        a = random.choice([i for i in range(-10, 10) if i!=0])
        b = random.choice([i for i in range(-10, 10) if i!=0])
        f=a*x+b

        m = random.choice([i for i in range(-2, 3) if i!=0])
        n = random.choice([i for i in range(-4, 4) if i!=0])
        p = random.choice([i for i in range(1, 5) if i!=0])
        g=m**2*x**2+2*m*n*x+n**2+p
        
    
    if chon==2:
        a = random.choice([i for i in range(-10, 10) if i!=0])
        b = random.choice([i for i in range(-10, 10) if i!=0])
        if a>0:
            x_0 = random.randint(int(-b/a)+2,int(-b/a)+7)
        else:
            x_0 = random.randint(int(-b/a)-6,int(-b/a)-2)

        f=a*x+b
        y_0=f.subs(x,x_0)        
      
        m = random.choice([i for i in range(-2, 3) if i!=0])
        n = random.choice([i for i in range(-4, 4) if i!=0])
        p=y_0-m*x_0**2-n*x_0
        g=m*x**2+n*x+p
    

    chon=random.randint(1,2)
    if chon==1:
        ham=f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(f)} \\text{{ khi }} x \\ge {x_0} \\\\ \n\
        {latex(g)} \\text{{ khi }} x < {x_0} \n\
        \\end{{array}} \\right.$"
    
    if chon==2:
        ham=f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(g)} \\text{{ khi }} x < {x_0} \\\\ \n\
        {latex(f)} \\text{{ khi }} x \\ge {x_0} \n\
        \\end{{array}} \\right.$" 

    
    noi_dung = f"Cho hàm số {ham}. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    x_1 = random.randint(x_0+1,x_0+6)
    f_1=f.subs(x,x_1)
    g_1=g.subs(x,x_1)
    if g_1==f_1: g_1=f_1+random.randint(1,3)
    kq1_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}={f_1}$" 
    kq1_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}={latex(g_1)}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_1}}} ({latex(f)})={f_1}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_2 = random.randint(x_0-6,x_0-1)    
    g_2=g.subs(x,x_2)
    f_2=f.subs(x,x_2)
    if f_2==g_2: f_2=f_2+random.randint(1,2)

    kq2_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}={latex(g_2)}$"
    kq2_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}={f_2}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_2}}} ({latex(g)})={latex(g_2)}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    f_0=f.subs(x,x_0)
    g_0=g.subs(x,x_0)
    chon=random.randint(1,2)

    if chon==1:
        
        kq3_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={f_0}$" 
        kq3_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={f_0+random.randint(1,3)}$"        
        HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$."
    
    if chon==2:
        
        kq3_T=f"* Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}={latex(g_0)}$" 
        kq3_F=f"Giới hạn $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}={latex(g_0+random.randint(1,2))}$"        
        HDG=f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(f)}) = {latex(g_0)}$."    
    
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if f_0==g_0:
        kq4_T=f"*Hàm số liên tục tại $x={{{x_0}}}$"
        kq4_F=f"Hàm số không liên tục tại $x={{{x_0}}}$" 
    
        HDG=(
        f"$f({x_0})={f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(g)}) = {latex(g_0)}$.\n\n"
        f"Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}$"
        f" nên $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}={f_0}$.\n\n"
        f" Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}}} {{f(x)}}=f({x_0})$ nên hàm số liên tục tại $x={{{x_0}}}$."
        )
    else:
        kq4_T=f"*Hàm số không liên tục tại $x={{{x_0}}}$"
        kq4_F=f"Hàm số liên tục tại $x={{{x_0}}}$"

        HDG=(
        f"$f({x_0})={f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} ({latex(f)}) = {f_0}$.\n\n"
        f"$\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}=\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} ({latex(g)}) = {latex(g_0)}$.\n\n"
        f"Vì $\\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^+}} {{f(x)}}\\ne \\mathop{{\\lim}}\\limits_{{x \\to  {x_0}^-}} {{f(x)}}$"
        f" nên hàm số không tồn tại giới hạn tại ${{{x_0}}}$.\n\n"
        f'Do đó hàm số không liên tục tại ${{{x_0}}}$.'
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

#[D11_C3_B3_07]-TF-M2. f(x)= phân thức + đa thức. Xét Đ-S: giới hạn, liên tục tại x_0.
def gh11gh_L11_C3_B3_07():
    x,m=sp.symbols("x m")    
    x_1 = random.choice([i for i in range(-7, 7) if i!=0])
    x_2 = random.choice([i for i in range(-7,7) if i != x_1  and i!=0])

    a = random.choice([i for i in range(-3, 3) if i!=0])
    b,c=-a*(x_1+x_2),a*x_1*x_2

    f_tu=latex(a*x**2+b*x+c)
    k = random.choice([i for i in range(-5, 5) if i!=0 and i!=1])
    f_mau=latex(k*(x-x_1))

    g=a*(x-x_2)/k

    p= random.choice([i for i in range(-5, 6) if i!=0])
    q= random.choice([i for i in range(-5, 6) if i!=0])
    chon=random.randint(1,2)

    f_2=p*m*x+q

    ham=(
    f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
    \\dfrac{{{f_tu}}}{{{f_mau}}} \\text{{ khi }} x\\ne {x_1}\\\\ \n\
    {latex(p*m*x+q)} \\text{{ khi }} x = {x_1}\n\
    \\end{{array}} \\right.$")

    noi_dung = f"Cho hàm số {ham}. Xét tính đúng-sai của các khẳng định sau:"  


    kq1_T=f"* Tập xác định của hàm số là $\\mathbb{{R}}$." 
    kq1_F=f"Tập xác định của hàm số là $\\mathbb{{R}}\\backslash {{{x_1}}}$."
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Hàm số xác định với mọi ${{x}}$ nên tập xác định của hàm số là $\\mathbb{{R}}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* ${st_lim(x_1)}f(x)={phan_so(g.subs(x,x_1))}$"
    kq2_F=f"${st_lim(x_1)}f(x)={phan_so(g.subs(x,x_1)+random.randint(1,3))}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=(
        f"Ta có: ${st_lim(x_1)}f(x)={st_lim(x_1)}\\dfrac{{{f_tu}}}{{{f_mau}}}={st_lim(x_1)}\\dfrac{{{latex(a*(x-x_1)*(x-x_2))}}}{{{f_mau}}}$"
        f"$={st_lim(x_1)}({latex(g)})={phan_so(g.subs(x,x_1))}$."
        )
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $f({x_1})={latex(f_2.subs(x,x_1))}$" 
    kq3_F=f"$f({x_1})={latex(f_2.subs(x,x_1)+random.randint(1,3))}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$f({x_1})={latex(f_2.subs(x,x_1))}$"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m_0=(g.subs(x,x_1)-q)/(p*x_1)
    chon=random.randint(1,2)
    if chon==1:
        kq4_T=f"* Hàm số liên tục tại $x={x_1}$ khi $m={phan_so(m_0)}$"
        kq4_F=f"Hàm số liên tục tại $x={x_1}$ khi $m={phan_so(m_0+random.choice([random.randint(1,4),random.randint(-4,-1)]))}$" 
        
        HDG=(f"Ta có: ${st_lim(x_1)}f(x)={phan_so(g.subs(x,x_1))}$.\n\n"
            f"$f({x_1})={latex(f_2.subs(x,x_1))}$.\n\n"
            f"Hàm số liên tục tại $x={x_1}$ khi ${latex(f_2.subs(x,x_1))}={phan_so(g.subs(x,x_1))}$.\n\n"
            f"Suy ra $m={phan_so(m_0)}$")
    
    if chon==2:
        kq4_T=f"* Hàm số liên tục trên $\\mathbb{{R}}$ khi $m={phan_so(m_0)}$"
        kq4_F=f"Hàm số liên tục trên $\\mathbb{{R}}$ khi $m={phan_so(m_0+random.choice([random.randint(1,4),random.randint(-4,-1)]))}$" 
        
        HDG=(f"Dễ thấy hàm số liên tục trên các khoảng $(-\\infty;{x_1})$ và $({x_1};+\\infty)$.\n\n"
            f"Hàm số liên tục trên $\\mathbb{{R}}$ khi và chỉ khi hàm số liên tục tại $x={x_1}$"
            f"Ta có: ${st_lim(x_1)}f(x)={phan_so(g.subs(x,x_1))}$.\n\n"
            f"$f({x_1})={latex(f_2.subs(x,x_1))}$.\n\n"
            f"Hàm số liên tục tại $x={x_1}$ khi ${latex(f_2.subs(x,x_1))}={phan_so(g.subs(x,x_1))}$.\n\n"
            f"Suy ra $m={phan_so(m_0)}$")
    
    
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

#[D11_C3_B3_08]-SA-M2. f(x)= phân thức + đa thức. Tìm m để liên tục tại x_0.
def gh11gh_L11_C3_B3_08():
    x,m=sp.symbols("x m")    
    x_1 = random.choice([i for i in range(-7, 7) if i!=0])
    x_2 = random.choice([i for i in range(-7,7) if i != x_1  and i!=0])

    a = random.choice([i for i in range(-3, 3) if i!=0])
    b,c=-a*(x_1+x_2),a*x_1*x_2

    f_tu=latex(a*x**2+b*x+c)
    k = random.choice([i for i in range(-5, 5) if i!=0 and i!=1])
    f_mau=latex(k*(x-x_1))

    g=a*(x-x_2)/k
    p= random.choice([i for i in range(-5, 6) if i!=0])
    q= random.choice([i for i in range(-5, 6) if i!=0])
    f_2=p*m*x+q

    ham=(
    f"$f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
    \\dfrac{{{f_tu}}}{{{f_mau}}} \\text{{ khi }} x\\ne {x_1}\\\\ \n\
    {latex(p*m*x+q)} \\text{{ khi }} x = {x_1}\n\
    \\end{{array}} \\right.$")

    noi_dung = (
    f"Tìm giá trị của tham số ${{m}}$ để hàm số {ham} liên tục tại $x={x_1}$ \n(kết quả làm tròn đến hàng phần trăm)."
    )
    m_0=(g.subs(x,x_1)-q)/(p*x_1)
    dap_an=f"{round_half_up(m_0,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f"Ta có: ${st_lim(x_1)}f(x)={phan_so(g.subs(x,x_1))}$.\n\n"
            f"$f({x_1})={latex(f_2.subs(x,x_1))}$.\n\n"
            f"Hàm số liên tục tại $x={x_1}$ khi ${latex(f_2.subs(x,x_1))}={phan_so(g.subs(x,x_1))}$.\n\n"
            f"Suy ra $m={phan_so(m_0)}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B3_09]-TF-M2. f(x)= đa thức + đa thức có m. Xét Đ-S: f(x_0),  lim->a, lim 1 bên, Tìm m để liên tục tại x_0.
def gh11gh_L11_C3_B3_09():
    x,m=sp.symbols("x,m")
    a,b,c=random.sample([i for i in range(-5,5) if i!=0],3)
    chon=random.randint(1,4)
    if chon==1:
        f=a*x**3+b*x+c   
    if chon==2:
        f=a*x**3+b*x**2+c
    if chon==3:
        f=a*x**3+b*x**2+c*x
    if chon==4:
        f=a*x**2+b*x**2+c
    a2,b2,c2=random.sample([i for i in range(-5,5) if i!=0],3)
    x_0 = random.choice([i for i in range(-6, 7) if i!=0])

    chon=random.randint(1,2)
    if chon==1:
        g=(a2*m+b2)*x**2+c2
        ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
        ({latex(a2*m+b2)})x^2+{c2} {{\\text{{ khi }}}} x< {x_0}\n\
        \\end{{array}} \\right."
    
    if chon==2:
        g=(a2*m+b2)*x**2+c2*x
        ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
        ({latex(a2*m+b2)})x^2+{latex(c2*x)} {{\\text{{ khi }}}} x< {x_0}\n\
        \\end{{array}} \\right."
    

    noi_dung = (
    f"Cho hàm số ${ham}$."
    f" Xét tính đúng-sai của các khẳng định sau:")

    noi_dung=noi_dung.replace("+-","-").replace("-+","-").replace("--","+")

    f_x0=f.subs(x,x_0)     
    
    kq1_T=f"*$f({x_0})={f_x0}$" 
    kq1_F=f"$f({x_0})={f_x0+random.randint(1,5)}$"
    
    HDG=f"Thay $x={x_0}$ vào hàm số $f(x)={latex(f)}$ ta được $f({x_0})={f_x0}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    
    if chon==1:
        x_1=x_0+random.randint(1,5)
        lim_x1=f.subs(x,x_1)

        kq2_T=f"*${st_lim(x_1)}f(x)={lim_x1}$"
        kq2_F=f"${st_lim(x_1)}f(x)={lim_x1+random.randint(1,3)}$"
        
        HDG=f"${st_lim(x_1)}f(x)={st_lim(x_1)}({latex(f)})={lim_x1}$."
    
    if chon==2:
        x_1=x_0-random.randint(1,5)
        lim_x1=g.subs(x,x_1)

        kq2_T=f"*${st_lim(x_1)}f(x)={latex(lim_x1)}$"
        kq2_F=f"${st_lim(x_1)}f(x)={latex(lim_x1+random.randint(1,3))}$"
        if g==(a2*m+b2)*x**2+c2:
        
            HDG=f"${st_lim(x_1)}f(x)={st_lim(x_1)}(({latex(a2*m+b2)})x^2+{c2})={latex(lim_x1)}$."
        else:
            HDG=f"${st_lim(x_1)}f(x)={st_lim(x_1)}(({latex(a2*m+b2)})x^2+{latex(c2*x)})={latex(lim_x1)}$."


    HDG=HDG.replace("+-","-").replace("-+","-").replace("--","+")    
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)    
    if chon==1:
        kq3_T=f"*${st_lim(f"{x_0}^+")}f(x)={f_x0}$" 
        kq3_F=f"${st_lim(f"{x_0}^+")}f(x)={latex(g.subs(x,x_0))}$"
        
        HDG=f"${st_lim(f"{x_0}^+")}f(x)={f_x0}$."
    
    if chon==2:
        kq3_T=f"*${st_lim(f"{x_0}^-")}f(x)={latex(g.subs(x,x_0))}$" 
        kq3_F=f"${st_lim(f"{x_0}^-")}f(x)={f_x0}$"
        
        HDG=f"${st_lim(f"{x_0}^-")}f(x)={latex(g.subs(x,x_0))}$."    
    
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    if g==(a2*m+b2)*x**2+c2:
        eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2)
    else:
        eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2*x_0)
    solution = solve(eq, m)
    m_0=solution[0]

    kq4_T=f"*Hàm số $f(x)$ liên tục tại $x={x_0}$ khi $m={phan_so(m_0)}$"
    kq4_F=f"Hàm số $f(x)$ liên tục tại $x={x_0}$ khi $m={phan_so(m_0+random.randint(1,3))}$" 
    
    HDG=(f"Hàm số $f(x)$ liên tục tại $x={x_0}$ khi:\n\n"
        f"${st_lim(f"{x_0}^-")}f(x)={st_lim(f"{x_0}^+")}f(x)=f({x_0})$\n\n"
        f"$\\Rightarrow {latex(g.subs(x,x_0))}={f_x0} \\Rightarrow m={phan_so(m_0)}$.")
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

#[D11_C3_B3_10]-TF-M2. f(x)= đa thức + đa thức có m. Xét Đ-S: f(x_0),  lim->a, lim 1 bên, Tìm m để liên tục trên R.
def gh11gh_L11_C3_B3_10():
    x,m=sp.symbols("x,m")
    a,b,c=random.sample([i for i in range(-5,5) if i!=0],3)
    chon=random.randint(1,4)
    if chon==1:
        f=a*x**3+b*x+c   
    if chon==2:
        f=a*x**3+b*x**2+c
    if chon==3:
        f=a*x**3+b*x**2+c*x
    if chon==4:
        f=a*x**2+b*x**2+c
    a2,b2,c2=random.sample([i for i in range(-5,5) if i!=0],3)
    x_0 = random.choice([i for i in range(-6, 7) if i!=0])

    chon=random.randint(1,2)
    if chon==1:
        g=(a2*m+b2)*x**2+c2
        ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
        ({latex(a2*m+b2)})x^2+{c2} {{\\text{{ khi }}}} x< {x_0}\n\
        \\end{{array}} \\right."
    
    if chon==2:
        g=(a2*m+b2)*x**2+c2*x
        ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
        ({latex(a2*m+b2)})x^2+{latex(c2*x)} {{\\text{{ khi }}}} x< {x_0}\n\
        \\end{{array}} \\right."
    

    noi_dung = (
    f"Cho hàm số ${ham}$."
    f" Xét tính đúng-sai của các khẳng định sau:")

    noi_dung=noi_dung.replace("+-","-").replace("-+","-").replace("--","+")

    f_x0=f.subs(x,x_0)     
    
    kq1_T=f"*$f({x_0})={f_x0}$" 
    kq1_F=f"$f({x_0})={f_x0+random.randint(1,5)}$"
    
    HDG=f"Thay $x={x_0}$ vào hàm số $f(x)={latex(f)}$ ta được $f({x_0})={f_x0}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    
    if chon==1:
        x_1=x_0+random.randint(1,5)
        lim_x1=f.subs(x,x_1)

        kq2_T=f"*${st_lim(x_1)}f(x)={lim_x1}$"
        kq2_F=f"${st_lim(x_1)}f(x)={lim_x1+random.randint(1,3)}$"
        
        HDG=f"${st_lim(x_1)}f(x)={st_lim(x_1)}({latex(f)})={lim_x1}$."
    
    if chon==2:
        x_1=x_0-random.randint(1,5)
        lim_x1=g.subs(x,x_1)

        kq2_T=f"*${st_lim(x_1)}f(x)={latex(lim_x1)}$"
        kq2_F=f"${st_lim(x_1)}f(x)={latex(lim_x1+random.randint(1,3))}$"
        if g==(a2*m+b2)*x**2+c2:
        
            HDG=f"${st_lim(x_1)}f(x)={st_lim(x_1)}(({latex(a2*m+b2)})x^2+{c2})={latex(lim_x1)}$."
        else:
            HDG=f"${st_lim(x_1)}f(x)={st_lim(x_1)}(({latex(a2*m+b2)})x^2+{latex(c2*x)})={latex(lim_x1)}$."


    HDG=HDG.replace("+-","-").replace("-+","-").replace("--","+")    
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)    
    if chon==1:
        kq3_T=f"*${st_lim(f"{x_0}^+")}f(x)={f_x0}$" 
        kq3_F=f"${st_lim(f"{x_0}^+")}f(x)={latex(g.subs(x,x_0))}$"
        
        HDG=f"${st_lim(f"{x_0}^+")}f(x)={f_x0}$."
    
    if chon==2:
        kq3_T=f"*${st_lim(f"{x_0}^-")}f(x)={latex(g.subs(x,x_0))}$" 
        kq3_F=f"${st_lim(f"{x_0}^-")}f(x)={f_x0}$"
        
        HDG=f"${st_lim(f"{x_0}^-")}f(x)={latex(g.subs(x,x_0))}$."    
    
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if g==(a2*m+b2)*x**2+c2:
        eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2)
    else:
        eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2*x_0)

    solution = solve(eq, m)
    m_0=solution[0]

    kq4_T=f"*Hàm số $f(x)$ liên tục với mọi $x\\in \\mathbb{{R}}$ khi $m={phan_so(m_0)}$"
    kq4_F=f"Hàm số $f(x)$ liên tục với mọi $x\\in \\mathbb{{R}}$ khi $m={phan_so(m_0+random.randint(1,3))}$" 
    
    HDG=(f"Hàm số $f(x)$ liên tục với mọi $x\\in \\mathbb{{R}}$ khi liên tục tại $x={x_0}$:\n\n"
        f"${st_lim(f"{x_0}^-")}f(x)={st_lim(f"{x_0}^+")}f(x)=f({x_0})$\n\n"
        f"$\\Rightarrow {latex(g.subs(x,x_0))}={f_x0} \\Rightarrow m={phan_so(m_0)}$.")
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

#[D11_C3_B3_11]-SA-M2. f(x)= đa thức + đa thức có m. Tìm m để liên tục tại x_0.
def gh11gh_L11_C3_B3_11():

    x,m=sp.symbols("x,m")
    while True:
        a,b,c=random.sample([i for i in range(-5,5) if i!=0],3)
        chon=random.randint(1,4)
        if chon==1:
            f=a*x**3+b*x+c   
        if chon==2:
            f=a*x**3+b*x**2+c
        if chon==3:
            f=a*x**3+b*x**2+c*x
        if chon==4:
            f=a*x**2+b*x**2+c

        a2,b2,c2=random.sample([i for i in range(-5,5) if i!=0],3)
        x_0 = random.choice([i for i in range(-6, 7) if i!=0])
        chon=random.randint(1,2)
        if chon==1:
            g=(a2*m+b2)*x**2+c2
            ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
            {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
            ({latex(a2*m+b2)})x^2+{c2} {{\\text{{ khi }}}} x< {x_0}\n\
            \\end{{array}} \\right."
            f_x0=f.subs(x,x_0) 
            eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2)
        
        if chon==2:
            g=(a2*m+b2)*x**2+c2*x
            ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
            {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
            ({latex(a2*m+b2)})x^2+{latex(c2*x)} {{\\text{{ khi }}}} x< {x_0}\n\
            \\end{{array}} \\right."
            f_x0=f.subs(x,x_0) 
            eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2*x_0)        
        
        solution = solve(eq, m)
        m_0=float(solution[0])
        if m_0>-5:
            break
    if m_0.is_integer():
        dap_an=int(m_0)
        noi_dung=f"Cho hàm số $f(x)={ham}$. Tìm giá trị của tham số ${{m}}$ để hàm số liên tục tại $x={x_0}$."
    else:
        dap_an=f"{round_half_up(m_0,1):.1f}".replace(".",",")
        noi_dung=f"Cho hàm số $f(x)={ham}$. Tìm giá trị của tham số ${{m}}$ để hàm số liên tục tại $x={x_0}$ (kết quả làm tròn đến hàng phần mười)."
    
    noi_dung=noi_dung.replace("+-","-").replace("-+","-").replace("--","+")
    noi_dung_loigiai=(
f"Ta có: $f({x_0})={f_x0}$.\n\n"
f"${st_lim(f"{x_0}^+")}f(x)={f_x0}$.\n\n"
f"${st_lim(f"{x_0}^-")}f(x)={latex(g.subs(x,x_0))}$.\n\n"
f"Hàm số $f(x)$ liên tục tại $x={x_0}$ khi:\n\n"
f"${st_lim(f"{x_0}^-")}f(x)={st_lim(f"{x_0}^+")}f(x)=f({x_0})$\n\n"
f"$\\Rightarrow {latex(g.subs(x,x_0))}={f_x0} \\Rightarrow m={phan_so(m_0)}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B3_12]-SA-M2. f(x)= đa thức + đa thức có m. Tìm m để liên tục trên R.
def gh11gh_L11_C3_B3_12():

    x,m=sp.symbols("x,m")
    while True:
        a,b,c=random.sample([i for i in range(-5,5) if i!=0],3)
        chon=random.randint(1,4)
        if chon==1:
            f=a*x**3+b*x+c   
        if chon==2:
            f=a*x**3+b*x**2+c
        if chon==3:
            f=a*x**3+b*x**2+c*x
        if chon==4:
            f=a*x**2+b*x**2+c

        a2,b2,c2=random.sample([i for i in range(-5,5) if i!=0],3)
        x_0 = random.choice([i for i in range(-6, 7) if i!=0])
        chon=random.randint(1,2)
        if chon==1:
            g=(a2*m+b2)*x**2+c2
            ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
            {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
            ({latex(a2*m+b2)})x^2+{c2} {{\\text{{ khi }}}} x< {x_0}\n\
            \\end{{array}} \\right."
            f_x0=f.subs(x,x_0) 
            eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2)
        
        if chon==2:
            g=(a2*m+b2)*x**2+c2*x
            ham=f"f(x)=\\left\\{{ \\begin{{array}}{{l}} \n\
            {latex(f)} {{\\text{{ khi }}}} x\\ge {x_0}  \\\\ \n\
            ({latex(a2*m+b2)})x^2+{latex(c2*x)} {{\\text{{ khi }}}} x< {x_0}\n\
            \\end{{array}} \\right."
            f_x0=f.subs(x,x_0) 
            eq = Eq(f_x0, (a2*m+b2)*x_0**2+c2*x_0)        
        
        solution = solve(eq, m)
        m_0=float(solution[0])
        if m_0>-5:
            break
    if m_0.is_integer():
        dap_an=int(m_0)
        noi_dung=f"Cho hàm số $f(x)={ham}$. Tìm giá trị của tham số ${{m}}$ để hàm số liên tục tại mọi $x\\in \\mathbb{{R}}$."
    else:
        dap_an=f"{round_half_up(m_0,1):.1f}".replace(".",",")
        noi_dung=f"Cho hàm số $f(x)={ham}$. Tìm giá trị của tham số ${{m}}$ để hàm số liên tục tại mọi $x\\in \\mathbb{{R}}$ (kết quả làm tròn đến hàng phần mười)."
    
    noi_dung=noi_dung.replace("+-","-").replace("-+","-").replace("--","+")
    noi_dung_loigiai=(
f"Ta có: $f({x_0})={f_x0}$.\n\n"
f"${st_lim(f"{x_0}^+")}f(x)={f_x0}$.\n\n"
f"${st_lim(f"{x_0}^-")}f(x)={latex(g.subs(x,x_0))}$.\n\n"
f"Hàm số $f(x)$ liên tục với mọi $x\\in \\mathbb{{R}}$ khi liên tục tại $x={x_0}$:\n\n"
f"${st_lim(f"{x_0}^-")}f(x)={st_lim(f"{x_0}^+")}f(x)=f({x_0})$\n\n"
f"$\\Rightarrow {latex(g.subs(x,x_0))}={f_x0} \\Rightarrow m={phan_so(m_0)}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C3_B3_13]-SA-M2. Hỏi lý thuyết về liên tục tại điểm 
def gh11gh_L11_C3_B3_13():
    f=random.choice(["f", "g", "h" ])
    a=random.randint(-7,8)

    noi_dung=(
    f"Cho hàm số $y={f}(x)$ xác định trên ${{D}}$ và ${a}\\in D$."
    f" Hàm số $y={f}(x)$ liên tục tại $x={a}$ khi"
    )
    

    kq=f"${st_lim(a)}{f}(x)={f}({a})$"
    kq_false=[
    f"${st_lim("+\\infty")}{f}(x)={f}({a})$",
    f"${st_lim("-\\infty")}{f}(x)={f}({a})$",
    f"${st_lim(f"{a}")}{f}({a})={f}(x)$",
    f"${st_lim(f"{a}")}{f}(x)=0$",
    f"${st_lim(f"{a}")}{f}(x)=+\\infty$",
    f"${st_lim(f"{a}")}{f}(x)=-\\infty$",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
     f"Hàm số $y={f}(x)$ liên tục tại $x={a}$ khi ${st_lim(a)}{f}(x)={f}{a}$."
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


#[D11_C3_B3_14]-SA-M2. Cho y=(ax+b)/(cx+d). Tìm điểm gián đoạn
def gh11gh_L11_C3_B3_14():
    x=sp.symbols("x")
    while True:
        a,b,c,d=random.sample([i for i in range(-8,9) if i!=0],4)
        if a*d-b*c!=0:
            break
    f=(a*x+b)/(c*x+d)
    x_0=-d/c
    noi_dung=(
    f"Cho hàm số $y={latex(f)}$. Hàm số gián đoạn tại điểm nào sau đây"
    )
    
    list_1=[i for i in range(int(x_0)-15, int(x_0)-2)]
    list_2=[i for i in range(int(x_0)+2, int(x_0)+15)]
    list_lt=list_1+list_2


    kq=x_0
    kq_false=list_lt
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"Hàm số gián đoạn khi ${latex(c*x+d)}= 0 \\Rightarrow x= {phan_so(-d/c)}$."
    )

    pa_A= f"*$x={phan_so(kq)}$"
    pa_B= f"$x={kq2}$"
    pa_C= f"$x={kq3}$"
    pa_D= f"$x={kq4}$"
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

#[D11_C3_B3_15]-SA-M2. Cho y=(ax+b)/(mx^2+nx+p). Tìm điểm gián đoạn
def gh11gh_L11_C3_B3_15():
    x=sp.symbols("x")
    x_1,x_2=random.sample(range(-8,9),2)
    while True:
        a,b=random.sample([i for i in range(-5,5) if i!=0],2)
        m= random.choice([i for i in range(-3, 4) if i!=0])
        if -b/a not in [x_1,x_2]:
            break
    f=m*(x-x_1)*(x-x_2)

    noi_dung=(
    f"Cho hàm số $y=\\dfrac{{{latex(a*x+b)}}}{{{latex(expand(f))} }}$. Hàm số gián đoạn tại điểm nào sau đây"
    )

    kq=random.choice([x_1,x_2])
    kq_false=[i for i in range(-10,10) if i not in [x_1,x_2]]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"Hàm số gián đoạn khi ${latex(expand(f))}=0 \\Rightarrow x= {x_1}$ hoặc $x={x_2}$."
    )

    pa_A= f"*$x={kq}$"
    pa_B= f"$x={kq2}$"
    pa_C= f"$x={kq3}$"
    pa_D= f"$x={kq4}$"
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

#[D11_C3_B3_16]-SA-M2. Cho y=(ax+b)/(mx^2+nx+p). Tìm khẳng định đúng về liên tục, gián đoạn tại điểm
def gh11gh_L11_C3_B3_16():
    x=sp.symbols("x")
    x_1,x_2=random.sample(range(-8,9),2)
    while True:
        a,b=random.sample([i for i in range(-5,5) if i!=0],2)
        m= random.choice([i for i in range(-3, 4) if i!=0])
        if -b/a not in [x_1,x_2]:
            break
    f=m*(x-x_1)*(x-x_2)
    list_lt=[i for i in range(-10,10) if i not in [x_1,x_2]]
    x_3,x_4,x_5,x_6=list_lt[0:4]

    noi_dung=(
    f"Cho hàm số $y=\\dfrac{{{latex(a*x+b)}}}{{{latex(expand(f))} }}$. Khẳng định nào sau đây đúng?"
    )

    kq=random.choice([        
        f"Hàm số gián đoạn tại $x={x_1}$",
        f"Hàm số gián đoạn tại $x={x_2}$",
        f"Hàm số liên tục tại $x={x_3}$",        ])
    kq_false= [f"Hàm số liên tục tại $x={x_1}$",
    f"Hàm số liên tục tại $x={x_2}$",
    f"Hàm số gián đoạn tại $x={x_4}$",
    f"Hàm số gián đoạn tại $x={x_5}$",
    f"Hàm số gián đoạn tại $x={x_6}$",
    f"Hàm số liên tục tại mọi $x\\in \\mathbb{{R}}$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"Hàm số gián đoạn khi ${latex(expand(f))}=0 \\Rightarrow x= {x_1}$ hoặc $x={x_2}$.\n\n"
        f"Hàm số liên tục tại mọi $x\\in \\mathbb{{R}} \\backslash \\left\\{{{x_1},{x_2} \\right\\}}$.\n\n"
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

    phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
    
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

#[D11_C3_B3_17]-SA-M2. Tìm hàm số gián đoạn tại x_0
def gh11gh_L11_C3_B3_17():
    x=sp.symbols("x")
    x_0= random.choice([i for i in range(-5, 6) if i!=0])
    while True:
        a= random.choice([i for i in range(-5, 6) if i!=0])
        b= random.choice([i for i in range(-5, 6) if i!=0])
        c= random.choice([i for i in range(-2, 2) if i!=0])
        d=-c*x_0
        if a*d-b*c!=0:
            break
    f=(a*x+b)/(c*x+d)
    while True:
        a= random.choice([i for i in range(-5, 6) if i!=0])
        b= random.choice([i for i in range(-5, 6) if i!=0])
        c= random.choice([i for i in range(-2, 2) if i!=0])
        d=c*x_0
        if a*d-b*c!=0:
            break
    f2=(a*x+b)/(c*x+d)

    a= random.choice([i for i in range(-5, 6) if i!=0])
    b= random.choice([i for i in range(-5, 6) if i!=0])
    c= random.choice([i for i in range(-2, 2) if i!=0])
    f3=a*x**2+b*x+c

    a= random.choice([i for i in range(-5, 6) if i!=0])
    b= random.choice([i for i in range(-5, 6) if i!=0])
    c= random.choice([i for i in range(-2, 2) if i!=0])
    d = random.choice([i for i in range(-5, 6) if i!=0])
    f4=(a*x+b)/(c*x**2+d)

    noi_dung=(
    f"Hàm số nào sau đây gián đoạn tại điểm $x={x_0}$?"
    )    

    kq=f"$y={latex(f)}$"
    kq_false=[
    f"$y={latex(f2)}$",
    f"$y={latex(f3)}$",
    f"$y={latex(f4)}$",]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"Hàm số  {kq} là gián đoạn tại điểm $x={x_0}$."
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
