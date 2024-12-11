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
    noi_dung = f"Tính tổng của cấp số nhân lùi vô hạn $S={latex(my_module.hien_phan_so(u1))}{dau}{latex(my_module.hien_phan_so(u2))}+...+{dau_ngoac_mo}{latex(my_module.hien_phan_so(u1))}{dau_ngoac_dong}\\left({latex(my_module.hien_phan_so(q))}\\right)^n+..$.. "

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
            noi_dung=f"Tính $\\lim {latex(u)}={phan_so(a/e**2)}$ (kết quả làm tròn đến hàng đơn vị)."
            dap_an=f"{N(a/e**2,1)}".replace(".",",")
        else:
            noi_dung=f"Tính $\\lim {latex(u)}={phan_so(a/e**2)}$ (kết quả làm tròn đến hàng phần trăm)."
            dap_an=f"{N(a/e**2,3):.2f}".replace(".",",")

        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex(a+b/n+c/n**3+d/n**4)} }}{{{latex((e+f/n**2)**2)} }}= {phan_so(a/e**2)}$."
        

    if chon==2:
        u=(e*n**2+f)**2/(a*n**4+b*n**3+c*n+d)

        noi_dung=f"Tính $\\lim {latex(u)}$ (kết quả làm tròn đến hàng phần mười)."

        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex((e+f/n**2)**2)}}}{{{latex(a+b/n+c/n**3+d/n**4)} }}= {phan_so(e**2/a)}$."
        dap_an=f"{N(e**2/a,2):.1f}".replace(".",",")
    
    if chon==3:
        u=(a*n**6+b*n**4+c*n**3+d)/(e*n**2+f)**3
        noi_dung=f"Tính $\\lim {latex(u)}$ (kết quả làm tròn đến hàng phần mười)."
        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex(a+b/n**2+c/n**3+d/n**6)} }}{{{latex((e+f/n**2)**2)} }}= {phan_so(a/e**3)}$."
        dap_an=f"{N(a/e**3,2):.1f}".replace(".",",")

    if chon==4:
        u=(e*n**2+f)**3/(a*n**6+b*n**4+c*n**3+d)

        noi_dung=f"Tính $\\lim {latex(u)}$ (kết quả làm tròn đến hàng phần mười)."

        noi_dung_loigiai=f"$\\lim {latex(u)}=\\lim \\dfrac{{{latex((e+f/n**2)**2)}}}{{{latex(a+b/n**2+c/n**3+d/n**6)}}}= {phan_so(e**3/a)}$."
        dap_an=f"{N(e**3/a,2):.1f}".replace(".",",") 
      
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

    noi_dung=f"Tính $\\lim \\dfrac{{{u1}+{u2}+{u3}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}$ (kết quả làm tròn đến hàng phần mười).".replace("+-","-")

    noi_dung_loigiai=(f"${u1},{u2},{u3},...,{un}$ lập thành cấp số cộng có $u_1={u1},d={du}$.\n\n"
        f"${v1},{v2},{v3},...,{vn}$ lập thành cấp số cộng có $v_1={v1},d={dv}$.\n\n"
        f"$\\lim \\dfrac{{{u1}+{u2}+{u3}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn}}}$\n"
        f"$=\\lim \\dfrac{{{S1}}}{{{S2}}}=\\lim \\dfrac{{{latex(expand(2*u1+(n-1)*du))}}}{{{latex(expand(2*v1+(n-1)*dv))}}}={phan_so(du/dv)}$")
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
    dap_an=f"{N(du/dv,2):.1f}".replace(".",",") 
    
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

    noi_dung=f"Tính $\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+{v3}+...+{vn} }}$(kết quả làm tròn đến hàng phần mười).".replace("+-","-").replace("--","+")   

    noi_dung_loigiai=(f"${u1},{u2},...,{un}$ lập thành cấp số nhân có $u_1={u1},q={q}$.\n\n"
        f"${v1},{v2},...,{vn}$ lập thành cấp số nhân có $v_1={v1},q={p}$.\n\n"
        f"$\\lim \\dfrac{{{u1}+{u2}+...+{un}}}{{{v1}+{v2}+...+{vn}}}$\n"
        f"$=\\lim \\dfrac{{{S1}}}{{{S2}}}={phan_so(u1/v1)}$.\n" )

    dap_an=f"{N(u1/v1,2):.1f}".replace(".",",") 
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
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

#[D11_C3_B2_03]. Tính giới hạn dạng 0/0 - Bậc 2/Bậc 2
def gh11gh_L11_C3_B2_03():
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
    kq= limit(f, x, x_0)
    kq2=a[0]/a[2]
    kq3=a[1]/a[2]
    kq4=a[1]/a[2]
    
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

#[D11_C3_B2_04]. Tính giới hạn dạng 0/0: [Căn(ax+b)-c]/(dx+e)
def gh11gh_L11_C3_B2_04():
    x = symbols('x')
    x_0 = random.randint(-5, 5)

    #Tạo list chứa các hệ số
    a = [random.randint(-4, 4) for _ in range(3)]
    for j in range(3):
        if a[j]==0:
            a[j] = random.randint(1, 5)
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
        kq4=f"{random.choice([phan_so(a/m),phan_so(-a/m),phan_so(a/n),phan_so(-a/m),latex(sqrt(a)/n),latex(-sqrt(a)/m) ])}"

    else:
        kq=f"{latex(sqrt(a)/m)}"
        kq2=f"{latex(-sqrt(a)/m)}"
        kq3=random.choice([0,"+\\infty","-\\infty"])
        kq4=f"{random.choice([phan_so(a/m),phan_so(-a/m),phan_so(a/n),phan_so(-a/m),latex(sqrt(a)/n),latex(-sqrt(a)/m) ])}" 

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

############# BÀI 3 - HÀM SỐ LIÊN TỤC 
#[D11_C3_B3_01]. Cho f(x)=căn(ax+b). Xét tính liên tục tại điểm.
def gh11gh_L11_C3_B3_01():
       
    x = sp.symbols('x')
    a= random.choice([random.randint(-8, -1), random.randint(1, 8)])   
    b= random.choice([random.randint(-7, -1), random.randint(1, 7)])         

    f=sqrt(a*x+b)

    if a>0:
        #Tạo điểm liên tục 
        x_1=random.randint(int(-b/a)+1,int(-b/a)+5)
        x_2=random.randint(int(-b/a)+6,int(-b/a)+20)

        #Tạo điểm gián đoạn
        x_3=random.randint(int(-b/a)-9,int(-b/a))
        x_4=random.randint(int(-b/a)-15,int(-b/a)-10)           
    else:
        #Tạo điểm liên tục 
        x_1=random.randint(int(-b/a)-5,int(-b/a)-1)
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
    x_0 = random.randint(-4,4)
    if x_0==0:
        x_0 = random.randint(2,5)

    a = random.randint(-4,4)
    if a==0:
        a = random.randint(1,4)
    b = random.randint(-4,4)
    c = random.randint(-5,5)
    if c==0:
        c==random.randint(1,3)
    d=-a*x_0**3-b*x_0**2-c*x_0
    #Tạo hàm số thứ nhất
    f = a*x**3 + b*x**2 + c*x + d

    a1 = random.randint(-3,3)    
    b1 = random.randint(-4,4)
    if b1==0:
        b1=random.randint(1,3)

    c1=-a1*x_0**2-b1*x_0
    g=a1*x**2 + b1*x +c1 

    #Tạo hàm thứ 2: mx+b2
    b2 = random.randint(-4,4)
    if b2==0:
        b2 = random.randint(1,3)
    dau="+"
    if b2<0:
        dau=""
        
    kq=latex((limit(f/g, x, x_0)-b2)/x_0)
    kq2 = latex((limit(f/g, x, x_0)+b2)/x_0)
    kq3=latex(limit(f/g, x, x_0)/x_0)
    kq4=latex(limit(g/f, x, x_0)/x_0)

    #Tạo các phương án
    pa_A= f"*$m={kq}$"
    pa_B= f"$m={kq2}$"
    pa_C= f"$m={kq3}$"
    pa_D= f"$m={kq4}$"

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


