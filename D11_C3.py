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

################ Bài 1: GIỚI HẠN DÃY SỐ #################

#[D11_C3_B1_01]. Tính giới hạn phân thức bậc tử bằng mẫu.
def zz8zz_L11_C3_B1_01():
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
def zz8zz_L11_C3_B1_02():
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
def zz8zz_L11_C3_B1_03():

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
def zz8zz_L11_C3_B1_04():
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
def zz8zz_L11_C3_B1_05():
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
def zz8zz_L11_C3_B1_06():
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
def zz8zz_L11_C3_B1_07():
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
 
########################### BÀI 2 - GIỚI HẠN HÀM SỐ ###########################

#[D11_C3_B2_01]. Tính giới hạn tại điểm - thay số trực tiếp
def zz8zz_L11_C3_B2_01():
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
def zz8zz_L11_C3_B2_02():
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
def zz8zz_L11_C3_B2_03():
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
def zz8zz_L11_C3_B2_04():
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
def zz8zz_L11_C3_B2_05():
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
def zz8zz_L11_C3_B2_06():
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
def zz8zz_L11_C3_B2_07():
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
    pa_B= f"*${{{kq2}}}$"
    pa_C= f"*${{{kq3}}}$"
    pa_D= f"*${{{kq4}}}$"
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
def zz8zz_L11_C3_B2_08():
       
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
def zz8zz_L11_C3_B2_09():
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
def zz8zz_L11_C3_B2_10():
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
def zz8zz_L11_C3_B2_11():
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
def zz8zz_L11_C3_B3_01():
       
    x = sp.symbols('x')
    a= random.choice([random.randint(-8, -1), random.randint(1, 8)])   
    b= random.choice([random.randint(-7, -1), random.randint(1, 7)])         

    f=sqrt(a*x+b)

    if a>0:
        #Tạo điểm liên tục 
        x_1=random.randint(int(-b/a)+1,int(-b/a)+5)
        x_2=random.randint(int(-b/a)+6,int(-b/a)+20)

        #Tạo điểm gián đoạn
        x_3=random.randint(int(-b/a)-15,int(-b/a))
        x_4=-b/a            
    else:
        #Tạo điểm liên tục 
        x_1=random.randint(int(-b/a)-5,int(-b/a)-1)
        x_2=random.randint(int(-b/a)-20,int(-b/a)-6)

        #Tạo điểm gián đoạn
        x_3=random.randint(int(-b/a)+1,int(-b/a)+10)
        x_4=-b/a

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
def zz8zz_L11_C3_B3_02():
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
def zz8zz_L11_C3_B3_03():
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
def zz8zz_L11_C3_B3_04():
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
def zz8zz_L11_C3_B3_05():
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

