import random
import math
import my_module
from sympy import *
#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m
############## BÀI 1-DÃY SỐ ##############
#[D11_C2_B1_01]-M2. Cho dãy số có SHTQ. Hỏi số là số hạng thứ mấy
def mn8mn_L11_C2_B1_01():
    n=symbols("n")
    
    chon=random.randint(1,2)
    if chon==1:
        a = random.choice([i for i in range(-5, 5) if i!=0])
        b = random.choice([i for i in range(-6, 6) if i!=0])
        u=a*n+b
        k=random.randint(30,2000)
        uk=a*k+b
        noi_dung=f"Cho dãy số $(u_n)$ có $u_n={latex(u)}$. Số ${{{uk}}}$ là số hạng thứ mấy của dãy số đã cho?"
        noi_dung_loigiai=f"${latex(u)}={uk}\\Rightarrow n={k}$."
        
    if chon==2:
        a = random.choice([i for i in range(-5, 5) if i!=0])
        b = random.randint(-4,4)
        c = random.choice([i for i in range(-5, 5) if i!=0])
        d = random.randint(-4,4)
        if a*d-b*c==0:d=d+1

        u=(a*n+b)/(c*n+d)
        k=random.randint(20,500)
        uk=(a*k+b)/(c*k+d)
        noi_dung=f"Cho dãy số $(u_n)$ có $u_n={latex(u)}$. Số ${{{phan_so(uk)}}}$ là số hạng thứ mấy của dãy số đã cho?"
        noi_dung_loigiai=f"${latex(u)}={phan_so(uk)}\\Rightarrow n={k}$."  
    
    kq=k
    kq2=random.choice([k-1,k+1])
    kq3=random.choice([k-2,k+2])
    kq4=k+random.randint(3,7)
    

    pa_A= f"*$u_{{{kq}}}$"
    pa_B= f"$u_{{{kq2}}}$"
    pa_C= f"$u_{{{kq3}}}$"
    pa_D= f"$u_{{{kq4}}}$"
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

#[D11_C2_B1_02]-M2. Cho dãy số. Tìm 3 số đầu tiên
def mn8mn_L11_C2_B1_02():
    n=symbols("n")    
    chon=random.randint(1,2)
    if chon==1:
        a = random.choice([i for i in range(-5, 5) if i!=0])
        b = random.choice([i for i in range(-6, 6) if i!=0])
        u=a*n+b
        
        u1=u.subs(n,1)
        u2=u.subs(n,2)
        u3=u.subs(n,3)

        noi_dung=f"Cho dãy số $(u_n)$ có $u_n={latex(u)}$. Ba số hạng đầu tiên của dãy số đã cho là"

        kq=f"$u_1={u1},u_2={u2}, u_3={u3}$"
        kq2=f"$u_1={-u1},u_2={-u2}, u_3={u3}$"
        kq3=f"$u_1={u1+random.randint(1,3)},u_2={u2-random.randint(1,3)}, u_3={u3+random.randint(0,3)}$"
        kq4=f"$u_1={-u1+random.randint(1,3)},u_2={u2-random.randint(1,3)}, u_3={-u3+random.randint(0,3)}$"
        noi_dung_loigiai=f"Ba số hạng đầu tiên của dãy số đã cho là:{kq}."    
    
    if chon==2:
        a = random.choice([i for i in range(-5, 5) if i!=0])
        b = random.randint(-4,4)
        c = random.choice([i for i in range(-5, 5) if i!=0])
        d = random.randint(-4,4)
        if a*d-b*c==0:d=d+1
        while any([-d/c==1,-d/c==2,-d/c==3]):
            a = random.choice([i for i in range(-5, 5) if i!=0])
            b = random.randint(-4,4)
            c = random.choice([i for i in range(-5, 5) if i!=0])
            d = random.randint(-4,4)
            if a*d-b*c==0:d=d+1

        u=(a*n+b)/(c*n+d)
        u1=u.subs(n,1)
        u2=u.subs(n,2)
        u3=u.subs(n,3)

        noi_dung=f"Cho dãy số $(u_n)$ có $u_n={latex(u)}$. Ba số hạng đầu tiên của dãy số đã cho là"
        
        kq=f"$u_1={phan_so(u1)},u_2={phan_so(u2)}, u_3={phan_so(u3)}$"
        kq2=f"$u_1={phan_so(-u1)},u_2={phan_so(u2+1)}, u_3={phan_so(u3-1)}$"
        kq3=f"$u_1={phan_so(u1+random.randint(1,3))},u_2={phan_so(u2-random.randint(1,3))}, u_3={phan_so(u3+random.randint(0,3))}$"
        kq4=f"$u_1={phan_so(-u1+random.randint(1,3))},u_2={phan_so(u2-random.randint(1,3))}, u_3={phan_so(-u3+random.randint(0,3))}$"
        noi_dung_loigiai=f"Ba số hạng đầu tiên của dãy số đã cho là:{kq}."

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C2_B1_03]-M2. Cho dãy số dạng truy hồi. Tìm công thức tổng quát
def mn8mn_L11_C2_B1_03():
    n=symbols("n")
    chon=random.randint(1,2)
    if chon==1:
        u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
        d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
        un=u1+(n-1)*d
        he=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        u_1={u1} \\\\ \n\
        u_{{n+1}}=u_{{n}}+{d},\\forall n\\ge 2\n\
        \\end{{array}} \\right.".replace("+-","-")

        noi_dung=f"Cho dãy số $(u_n)$ xác định bởi ${he}$. Mệnh đề nào sau đây đúng?"        

        kq=f"$u_n={latex(un)}$"
        kq2=f"$u_n={latex(u1+n*d)}$"
        kq3=f"$u_n={latex(u1+(n+1)*d)}$"
        kq4=f"$u_n={latex(u1-(n+1)*d)}$"
        
    if chon==2:
        u1 = random.choice([random.randint(-5, -2), random.randint(1, 5)])
        q = random.choice([random.randint(-4, -1), random.randint(1, 4),1/2, 2/3, 3/4, 1/3])
        un=u1*q**(n-1)
        if q>0:
            st_q=q
        if q<0 or q in [1/2, 2/3, 3/4, 1/3]:
            st_q=f"\\left({phan_so(q)} \\right)"

        he=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        u_1={u1} \\\\ \n\
        u_{{n+1}}={phan_so(q)}u_{{n}},\\forall n\\ge 2\n\
        \\end{{array}} \\right.".replace("+-","-")

        noi_dung=f"Cho dãy số $(u_n)$ xác định bởi ${he}$. Mệnh đề nào sau đây đúng?"        

        kq=f"$u_n={u1}.{st_q}^{{n-1}}$"
        kq2=f"$u_n={u1}+{st_q}n$"
        kq3=f"$u_n={u1}.{st_q}^{{n}}$"
        kq4=f"$u_n={u1}.{st_q}^{{n+1}}$"
    

    noi_dung_loigiai=f"{kq} là mệnh đề đúng."

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

#[D11_C2_B1_04]-M2. Cho dãy số có SHQT xét tính tăng giảm, bị chặn
def mn8mn_L11_C2_B1_04():
    n=symbols("n")
    a = random.choice([i for i in range(-5, 5) if i!=0])
    b = random.randint(1,4)
    c = random.randint(1,7)
    chon=random.randint(1,2)    
    if chon==1:
        u=a-b/(c+n)

        noi_dung=(f"Cho dãy số $(u_n)$ xác định bởi $u_n={latex((a*c-b+a*n)/(c+n))},\\forall n \\ge 1$."
            f"Mệnh đề nào sau đây đúng?"
            )    
        
        kq=random.choice([
            f"$(u_n)$ là dãy số tăng",
            f"$(u_n)$ là dãy số tăng và bị chặn"
            ])

        kq2=random.choice([
            "$(u_n)$ là dãy số giảm",
            "$(u_n)$ là dãy số tăng và không bị chặn trên"
            ])

        kq3=random.choice([
            f"$(u_n)$ là dãy số không bị chặn",
            f"$(u_n)$ là dãy số tăng và không bị chặn"
            ])
        kq4=random.choice([
            f"$(u_n)$ là dãy số giảm và bị chặn dưới",
            f"$(u_n)$ là dãy số giảm và không bị chặn"])
        u1=u.subs(n,1)
        noi_dung_loigiai=(
            f"$u_n={latex((a*c-b+a*n)/(c+n))}={latex(a-b/(c+n))} \\Rightarrow u_{{n+1}}-u_n>0,\\forall n \\ge 1$ nên $(u_n)$ là dãy số tăng.\n\n"
            f"${phan_so(u1)}\\le {latex(a-b/(c+n))}\\le {a}$ nên $(u_n)$ là dãy số bị chặn."
            )
    
    if chon==2:
        u=a+b/(c+n)

        noi_dung=(f"Cho dãy số $(u_n)$ xác định bởi $u_n={latex((a*c+b+a*n)/(c+n))},\\forall n \\ge 1$."
            f"Mệnh đề nào sau đây đúng?"
            )    
        
        kq=random.choice([
            "$(u_n)$ là dãy số giảm",
            "$(u_n)$ là dãy số giảm và bị chặn"            
            ])

        kq2=random.choice([            
            f"$(u_n)$ là dãy số tăng",
            f"$(u_n)$ là dãy số tăng và bị chặn"
            ])

        kq3=random.choice([
            f"$(u_n)$ là dãy số không bị chặn",
            f"$(u_n)$ là dãy số giảm và không bị chặn"
            ])
        kq4=random.choice([
            f"$(u_n)$ là dãy số tăng và bị chặn dưới",
            f"$(u_n)$ là dãy số giảm và không bị chặn trên"])
        u1=u.subs(n,1)
        noi_dung_loigiai=(
            f"$u_n={latex((a*c+b+a*n)/(c+n))}={latex(a+b/(c+n))}\\Rightarrow u_{{n+1}}-u_n<0,\\forall n \\ge 1$ nên $(u_n)$ là dãy số giảm.\n\n"
            f"${a}\\le {latex(a-b/(c+n))}\\le {phan_so(u1)}$ nên $(u_n)$ là dãy số bị chặn."
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

############## BÀI 2-CẤP SỐ CỘNG ##############

#D11_C2_B2_01. Cho cấp số cộng có u1, d tìm u_k
def mn8mn_L11_C2_B2_01():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
    k = random.randint(6,40)
    pa_A= f"*$u_{{{k}}}= {latex(u1+(k-1)*d)} $"
    pa_B= f"$u_{{{k}}}={latex(u1+k*d)}$"
    pa_C= f"$u_{{{k}}}={latex((u1+(k+1)*d))}$"
    pa_D= f"$u_{{{k}}}={latex(2*u1+(k-1)*d)}$"
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f" Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1={u1}$ và công sai $d={d}$." \
        f"Tìm số hạng thứ {k} của cấp số cộng đã cho."
    if d>0:
        noi_dung_loigiai=f"$u_{{{k}}}={u1}+{k-1}.{d}= {latex(u1+(k-1)*d)}$."
    else:
        noi_dung_loigiai=f"$u_{{{k}}}={u1}+{k-1}.({d})= {latex(u1+(k-1)*d)}$."

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

#D11_C2_B2_2. Cho cấp số cộng có u1, d . Tính S_n
def mn8mn_L11_C2_B2_02():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
    k = random.randint(6,40)

    pa_A= f"*$S_{{{k}}}= {latex(my_module.hien_phan_so(k/2*(2*u1+(k-1)*d)))}$"
    pa_B= f"$S_{{{k}}}= {latex(my_module.hien_phan_so(k*(2*u1+(k-1)*d)))}$"
    pa_C= f"$S_{{{k}}}={latex(my_module.hien_phan_so(latex(k/2*(u1+(k-1)*d))))}$"
    pa_D= f"$S_{{{k}}}={latex(my_module.hien_phan_so(k/2*(2*u1+k*d)))}$"


    noi_dung = "Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1=" + str(u1) +"$" \
        + " và công sai $d=" +str(d) +"$. "\
        "Tính tổng của " + str(k) +" số hạng đầu tiên."
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

#[D11_C2_B2_03]. Cho cấp số cộng có u_k,u_m. Tìm u1
def mn8mn_L11_C2_B2_03():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
    k = random.randint(3,10)
    m = k + random.randint(2,8)

    u_k=u1+(k-1)*d
    u_m= u1+(m-1)*d

    kq=u1
    kq2=(u_k+u_m)/2
    kq3=d
    kq4=u_m-u_k

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
 
    pa_A= f"*${{u_1={latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${{u_1={latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{u_1={latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{u_1={latex(my_module.hien_phan_so(kq4))}}}$"

    noi_dung= f"Cho cấp số cộng $(u_n)$ có ${{u_{{{k}}}={u_k}}}$ và ${{u_{{{m}}}={u_m}}}$. Tìm số hạng đầu $u_1$."
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

#[D11_C2_B2_04]. Cho cấp số cộng có u_k,u_m. Tìm d
def mn8mn_L11_C2_B2_04():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
    k = random.randint(3,10)
    m = k + random.randint(2,8)

    u_k=u1+(k-1)*d
    u_m= u1+(m-1)*d

    kq=d
    if u_k!=0:
        kq2=u_m/u_k
    else:
        kq2=u_m+u_k
    kq3=u1
    kq4=u_m-u_k

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
 
    pa_A= f"*${{d={latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${{d={latex(my_module.hien_phan_so(kq2))}}}$"
    pa_C= f"${{d={latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{d={latex(my_module.hien_phan_so(kq4))}}}$"

    noi_dung= f" Cho cấp số cộng $(u_n)$ có ${{u_{{{k}}}={u_k}}}$ và ${{u_{{{m}}}={u_m}}}$. Tìm công sai $d$."
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

#[D11_C2_B2_05]. Cho CSC có u1,d. Xét Đ-S: u_k, số hạng thứ mấy, S_k, u_n
def mn8mn_L11_C2_B2_05():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
    
    noi_dung = f"Cho cấp số cộng $(u_n)$ có số hạng đầu ${{u_1={u1}}}$ và công sai ${{d={d}}}$. Xét tính đúng-sai của các khẳng định sau:"        
    debai_word= f"{noi_dung}\n"

    k = random.randint(3,40)   
    u_k=u1+(k-1)*d

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"

    kq1_T=f"* $u_{{{k}}}={u_k}$" 
    kq1_F=f"$u_{{{k}}}={u1+k*d}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$u_{{{k}}}={st_u1}+{k-1}.{st_d}={u_k}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.randint(10,40)
    if m==k: m=m+random.randint(1,6)
    u_m= u1+(m-1)*d

    kq2_T=f"* Số ${{{u_m}}}$ là số hạng thứ ${{{m}}}$ của $(u_n)$"
    kq2_F=f" Số ${{{u_m}}}$ là số hạng thứ ${{{m+random.randint(1,5)}}}$ của $(u_n)$"
    kq2=random.choice([kq2_T, kq2_F])    
    HDG=(f"${u_m}={st_u1}+(n-1).{st_d} \\Rightarrow n={m}$.\n\n"
            f" Vậy ${{{u_m}}}$ là số hạng thứ ${{{m}}}$ của $(u_n)$."
            )
            
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=random.randint(15,50)
    Sn=n*(2*u1+(n-1)*d)/2
    Sn_false=n*(u1+(n-1)*d)/2

    kq3_T=f"* Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn)}$" 
    kq3_F=f"Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn_false)}$"
    kq3=random.choice([kq3_T, kq3_F])    
        
    HDG=f"$S_{{{n}}}={phan_so(n/2)}[2.{st_u1}+{n-1}.{st_d}]={phan_so(Sn)}$."

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=symbols("n")
    kq4_T=f"* $u_n={latex(u1+(n-1)*d)}$"
    kq4_F=f"$u_n={latex(u1+n*d)}$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$u_n={st_u1}+(n-1).{st_d}={latex(u1+(n-1)*d)}$."
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

#[D11_C2_B2_06]-M2. Cho CSC có un. Tìm d
def mn8mn_L11_C2_B2_06():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
    n=symbols("n")
    un=u1+(n-1)*d
    
    noi_dung = f"Cho cấp số cộng $(u_n)$ có số hạng tổng quát là ${{u_n={latex(un)}}}$. Tìm công sai ${{d}}$."        
    debai_word= f"{noi_dung}\n"    

    kq=d
    kq2=d+random.randint(1,3)
    kq3=d-random.randint(1,3)
    kq4=-d

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=f"$d=u_{{n+1}}-u_n={latex(u1+n*d)}-({latex(un)})={d}$."

    pa_A= f"*$d={kq}$"
    pa_B= f"$d={kq2}$"
    pa_C= f"$d={kq3}$"
    pa_D= f"$d={kq4}$"
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

#[D11_C2_B2_07]-M2. Nhận dạng cấp số cộng từ SHTQ
def mn8mn_L11_C2_B2_07():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])
    n=symbols("n")
    un=u1+(n-1)*d
    noi_dung=f"Trong các dãy số $(u_n)$ được cho bởi số hạng tổng quát $u_n$ sau, dãy nào là cấp số cộng"
    

    kq=f"$u_n={latex(un)}$"
    kq2=f"$u_n={random.randint(2,5)}^n$"
    kq3=f"$u_n={random.randint(2,5)}^{{n+1}}$"
    kq4=random.choice([
        f"$u_n={latex(n**(random.randint(2,3))+random.randint(-5,5))}$",
        f"$u_n={latex(random.randint(2,10)/(n**(random.randint(2,3))+random.randint(-5,5)))}$"
        ])

    noi_dung_loigiai=f"$u_n={latex(un)}$ là số hạng tổng quát của cấp số cộng vì có  $u_{{n+1}}-u_n={d}$."

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

#[D11_C2_B2_08]-M2. Nhận dạng dãy số hữu hạn là 1 cấp số cộng
def mn8mn_L11_C2_B2_08():
    n=symbols("n")
    
    noi_dung=f"Trong các dãy số sau, dãy nào là một cấp số cộng"

    u1 = random.choice([i for i in range(-7, 7) if i!=0])
    d = random.choice([i for i in range(-8, 8) if i!=0])
    u1,u2,u3,u4=[u1+(i-1)*d for i in range(4)]

    kq=f"${u1};{u2};{u3};{u4}$"
    noi_dung_loigiai=f"{kq} là một cấp số cộng với $u_1={u1},d={d}$."

    u1 = random.choice([i for i in range(-5, 5) if i!=0])
    d = random.choice([i for i in range(2, 4) if i!=0])
    u1,u2,u3,u4=[u1*d**i for i in range(4)]

    kq2=f"${u1};{u2};{u3};{u4}$"

    u1 = random.choice([i for i in range(-10, 10) if i!=0])
    d = random.choice([i for i in range(-3, -2) if i!=0])
    u1,u2,u3,u4=[u1+d**i for i in range(4)]

    kq3=f"${u1};{u2};{u3};{u4}$"

    u1 = random.choice([i for i in range(-5, 5) if i!=0])
    d = random.choice([i for i in range(2, 3) if i!=0])
    u1,u2,u3,u4=[u1-d**i for i in range(4)]

    kq4=f"${u1};{u2};{u3};{u4}$"

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

#[D11_C2_B2_09]-TF-M3. CSC có u_m,u_n. Xét Đ-S: u_1,d, số hạng thứ mấy, S_k, u_n
def mn8mn_L11_C2_B2_09():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])

    k = random.randint(3,40)   
    u_k=u1+(k-1)*d

    m = random.randint(10,40)
    if m==k: m=m+random.randint(1,6)
    u_m= u1+(m-1)*d

    k_1=random.randint(5,12)
    k_2=k_1+random.randint(5,10)
    while any([k_1==k, k_1==m, k_2==k, k_2==m]):
        k_1=random.randint(5,10)
        k_2=k_1+random.randint(5,10)
        
    u_k1, u_k2 = u1+(k_1-1)*d, u1+(k_2-1)*d
    
    noi_dung = f"Cho cấp số cộng $(u_n)$ có số hạng đầu $u_{{{k_1}}}={u_k1}$ và $u_{{{k_2}}}={u_k2}$ . Xét tính đúng-sai của các khẳng định sau:"        
    debai_word= f"{noi_dung}\n"

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"

    kq1_T=f"* $u_1={u1}, d={d}$" 
    kq1_F=random.choice([
        f"$u_1={u1+random.randint(1,5)}, d={d}$",
        f"$u_1={u1}, d={d+random.randint(1,5)}$",
        f"$u_1={u1-random.randint(1,5)}, d={d+random.randint(1,5)}$"
        ])
    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    u_{{{k_1}}}=u_1+{k_1-1}d={u_k1} \\\\ \n\
    u_{{{k_2}}}=u_1+{k_2-1}d={u_k2}\n\
    \\end{{array}} \\right."
    f"\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
    u_1={u1} \\\\ \n\
    d={d}\n\
    \\end{{array}} \\right.$"
    )
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"* Số ${{{u_m}}}$ là số hạng thứ ${{{m}}}$ của $(u_n)$"
        kq2_F=f" Số ${{{u_m}}}$ là số hạng thứ ${{{m+random.randint(1,5)}}}$ của $(u_n)$"
        kq2=random.choice([kq2_T, kq2_F])    
        HDG=(f"${u_m}={st_u1}+(n-1).{st_d} \\Rightarrow n={m}$.\n\n"
                f" Vậy ${{{u_m}}}$ là số hạng thứ ${{{m}}}$ của $(u_n)$."
                )    
    if chon==2:
        kq2_T=f"* $u_{{{k}}}={u_k}$"
        kq2_F=f"$u_{{{k}}}={u1+k*d}$"
        kq2=random.choice([kq2_T, kq2_F])    
        HDG=f"$u_{{{k}}}={st_u1}+{k-1}.{st_d}={u_k}$."              
            
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=random.randint(15,50)
    Sn=n*(2*u1+(n-1)*d)/2
    Sn_false=n*(u1+(n-1)*d)/2

    kq3_T=f"* Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn)}$" 
    kq3_F=f"Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn_false)}$"
    kq3=random.choice([kq3_T, kq3_F])    
        
    HDG=f"$S_{{{n}}}={phan_so(n/2)}[2.{st_u1}+{n-1}.{st_d}]={phan_so(Sn)}$."

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=symbols("n")
    kq4_T=f"* $u_n={latex(u1+(n-1)*d)}$"
    kq4_F=f"$u_n={latex(u1+n*d)}$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$u_n={st_u1}+(n-1).{st_d}={latex(u1+(n-1)*d)}$."
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

#[D11_C2_B2_10]-TF-M3. CSC có u_1,S_n. Xét Đ-S: u_1,d, u_k, S_k, u_n
def mn8mn_L11_C2_B2_10():
    u1 = random.choice([random.randint(-10, -1), random.randint(1, 20)])
    d = random.choice([random.randint(-5, -1), random.randint(1, 15)])

    k = random.randint(3,40)   
    u_k=u1+(k-1)*d

    m = random.randint(10,40)
    if m==k: m=m+random.randint(1,6)
    u_m= u1+(m-1)*d

    k_1=random.randint(5,12)
    k_2=k_1+random.randint(5,10)
    while any([k_1==k, k_1==m, k_2==k, k_2==m]):
        k_1=random.randint(5,10)
        k_2=k_1+random.randint(5,10)
        
    u_k1, u_k2 = u1+(k_1-1)*d, u1+(k_2-1)*d

    i=random.randint(10,20)
    S_i=i*(2*u1+(i-1)*d)/2
    
    noi_dung = (f"Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1={u1}$ và tổng của ${{{i}}}$ số hạng đầu tiên $S_{{{i}}}={phan_so(S_i)}$."
    f" Xét tính đúng-sai của các khẳng định sau:") 
    debai_word= f"{noi_dung}\n"

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"

    kq1_T=f"* $d={d}$" 
    kq1_F=random.choice([f"d={d+random.randint(1,5)}",f"d={d-random.randint(1,5)}" ])
    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f"$S_{{{i}}}={phan_so(i/2)}[2{st_u1}+{i-1}.{st_d}]={phan_so(S_i)}\\Rightarrow d={d}.$"
    )
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
        
    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"* Số ${{{u_m}}}$ là số hạng thứ ${{{m}}}$ của $(u_n)$"
        kq2_F=f" Số ${{{u_m}}}$ là số hạng thứ ${{{m+random.randint(1,5)}}}$ của $(u_n)$"
        kq2=random.choice([kq2_T, kq2_F])    
        HDG=(f"${u_m}={st_u1}+(n-1).{st_d} \\Rightarrow n={m}$.\n\n"
                f" Vậy ${{{u_m}}}$ là số hạng thứ ${{{m}}}$ của $(u_n)$."
                )    
    if chon==2:
        kq2_T=f"* $u_{{{k}}}={u_k}$"
        kq2_F=f"$u_{{{k}}}={u1+k*d}$"
        kq2=random.choice([kq2_T, kq2_F])    
        HDG=f"$u_{{{k}}}={st_u1}+{k-1}.{st_d}={u_k}$."              
            
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=random.randint(15,50)
    Sn=n*(2*u1+(n-1)*d)/2
    Sn_false=n*(u1+(n-1)*d)/2

    kq3_T=f"* Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn)}$" 
    kq3_F=f"Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn_false)}$"
    kq3=random.choice([kq3_T, kq3_F])    
        
    HDG=f"$S_{{{n}}}={phan_so(n/2)}[2.{st_u1}+{n-1}.{st_d}]={phan_so(Sn)}$."

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=symbols("n")
    kq4_T=f"* $u_n={latex(u1+(n-1)*d)}$"
    kq4_F=f"$u_n={latex(u1+n*d)}$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$u_n={st_u1}+(n-1).{st_d}={latex(u1+(n-1)*d)}$."
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

#[D11_C2_B2_11]-TF-M3. Xét đúng-sai từ bài toán thực tế liên quan cấp số cộng
def mn8mn_L11_C2_B2_11():
    u1 = random.randint(600,999)
    d = random.choice([-5*i for i in range (1,10)])    

    noi_dung = (f"Giá của một cái máy phục vụ sản xuất lúc mới mua là ${{{u1}}}$ triệu đồng."
    f" Cứ sau mỗi năm sử dụng, giá của chiếc máy đó giảm ${{{-d}}}$ triệu đồng."
    " Gọi $u_n$ (triệu đồng) là giá của chiếc máy trong năm thứ ${{n}}$ sử dụng." 
    f" Xét tính đúng-sai của các khẳng định sau.")        
    debai_word= f"{noi_dung}\n"
    
    n=random.randint(2,4)
    u_n=u1+(n-1)*d

    kq1_T=f"* $u_{n}={u_n}$" 
    kq1_F=f"$u_{n}={u1+n*d}$ "
    kq1=random.choice([kq1_T, kq1_F])
    HDG=(f"$(u_n)$ là cấp số cộng với $u_1={u1}$ và $d={d}$."
         f" Do đó: $u_{n}={u1}+{n-1}.({d})={u_n}$.")
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Dãy số $(u_n)$ là một cấp số cộng có công sai $d={-d}$"
    kq2_F=f"Dãy số $(u_n)$ là một cấp số cộng có công sai $d={d}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Dãy số $(u_n)$ là một cấp số cộng có công sai $d={-d}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=random.randint(5,15)
    u_n=u1+(n-1)*d

    kq3_T=f"* Giá chiếc máy sau ${{{n}}}$ năm sử dụng nhỏ hơn ${u_n+random.randint(10,20)}$ triệu đồng" 
    kq3_F=f"Giá chiếc máy sau ${{{n}}}$ năm sử dụng nhỏ hơn ${u_n-random.randint(10,20)}$ triệu đồng"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=(f"Giá chiếc máy sau ${{{n}}}$ năm sử dụng là: $u_{n+1}={u1}+{n}.({d})={u_n}$.\n\n"
        )

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    n=symbols("n")
    equation=Eq(u1+(n-1)*d,1/2*u1)
    solution=solve(equation,n)
    so_nam_goc=f"{round(solution[0],2):.2f}".replace(".",",")

    if int(solution[0])<solution[0]:
        so_nam=int(solution[0])+1
    else:
        so_nam=int(solution[0])

    kq4_T=f"* Sau ít nhất {so_nam} thì giá chiếc máy nhỏ hơn một nữa giá trị ban đầu"
    kq4_F=f"Sau ít nhất {so_nam-random.randint(2,3)} thì giá chiếc máy nhỏ một nữa giá trị ban đầu" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(
    f"Ta có: $u_n<{phan_so(u1/2)}\\Rightarrow {u1}+({n-1}).({d})<{phan_so(u1/2)} \\Rightarrow n>{so_nam_goc}$.\n\n"
    f"Sau ít nhất ${so_nam}$ thì giá chiếc máy nhỏ hơn một nữa giá trị ban đầu.")
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

#[D11_C2_B2_12]-TL-M3. CSC có u_k,u_m. Tính u_n
def mn8mn_L11_C2_B2_12():
    u1 = random.choice([random.randint(-150, -8), random.randint(1, 10)])
    d = random.choice([random.randint(-20, -5), random.randint(5, 10)])
    k = random.randint(3,10)
    m = k + random.randint(2,8)

    u_k=u1+(k-1)*d
    u_m= u1+(m-1)*d
    n=random.randint(15,35)
    u_n= u1+(n-1)*d

    while any([u_n<-9, u_n>9999]):
        u1 = random.choice([random.randint(-150, -8), random.randint(1, 10)])
        d = random.choice([random.randint(-20, -3), random.randint(3, 10)])
        k = random.randint(3,10)
        m = k + random.randint(2,8)
        n=random.randint(15,35)
        u_n= u1+(n-1)*d

    u_k=u1+(k-1)*d
    u_m= u1+(m-1)*d
    

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"

    noi_dung = (
    f"Cho cấp số cộng $(u_n)$ có $u_{{{k}}}={u_k},u_{{{m}}}={u_m}$. Tính $u_{{{n}}}$."
    )
    dap_an=u_n

    noi_dung_loigiai=(   
    f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    u_{{{k}}}={u_k} \\\\ \n\
    u_{{{m}}}={u_m} \n\
    \\end{{array}} \\right.$"

    f"$\\Rightarrow\\left\\{{ \\begin{{array}}{{l}} \n\
    u_1 +{k-1}d={u_k} \\\\ \n\
    u_1+{m-1}d={u_m}\n\
    \\end{{array}} \\right.$"

    f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
    u_1={u1} \\\\ \n\
    d={d}\n\
    \\end{{array}} \\right.$\n\n"
    f"$u_{{{n}}}={u1} +{n-1}.{st_d}={u_n}$.\n\n"
    f"Đáp án: {dap_an}"
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_13]-TL-M3. CSC có u_k,u_m. Tính S_n
def mn8mn_L11_C2_B2_13():
    u1 = random.choice([random.randint(-150, -8), random.randint(1, 10)])
    d = random.choice([random.randint(-20, -5), random.randint(5, 10)])
    k = random.randint(3,10)
    m = k + random.randint(2,8)

    u_k=u1+(k-1)*d
    u_m= u1+(m-1)*d
    n=random.randint(15,35)
    S_n=n*(2*u1+(n-1)*d)/2

    while any([S_n<-9, S_n>9999]):
        u1 = random.choice([random.randint(-150, -8), random.randint(1, 10)])
        d = random.choice([random.randint(-20, -3), random.randint(3, 10)])
        k = random.randint(3,10)
        m = k + random.randint(2,8)
        n=random.randint(15,35)
        S_n=n*(2*u1+(n-1)*d)/2

    u_k=u1+(k-1)*d
    u_m= u1+(m-1)*d
    

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"

    if int(S_n)==S_n:
        noi_dung = (
        f"Cho cấp số cộng $(u_n)$ có $u_{{{k}}}={u_k},u_{{{m}}}={u_m}$."
        f" Tính tổng của ${{{n}}}$ số hạng đầu tiên của cấp số cộng đã cho."
        )
        dap_an=f"{int(S_n)}"
    else:

        noi_dung = (
        f"Cho cấp số cộng $(u_n)$ có $u_{{{k}}}={u_k},u_{{{m}}}={u_m}$."
        f" Tính tổng của ${{{n}}}$ số hạng đầu tiên của cấp số cộng đã cho (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round(S_n,1):.1f}"

    noi_dung_loigiai=(   
    f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    u_{{{k}}}={u_k} \\\\ \n\
    u_{{{m}}}={u_m} \n\
    \\end{{array}} \\right.$"

    f"$\\Rightarrow\\left\\{{ \\begin{{array}}{{l}} \n\
    u_1 +{k-1}d={u_k} \\\\ \n\
    u_1+{m-1}d={u_m}\n\
    \\end{{array}} \\right.$"

    f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
    u_1={u1} \\\\ \n\
    d={d}\n\
    \\end{{array}} \\right.$\n\n"
    f"$S_{{{n}}}={phan_so(n/2)}[2.{st_u1} +{n-1}.{st_d}]={phan_so(S_n)}$.\n\n"
    f"Đáp án: {dap_an}"
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_14]-TL-M3. CSC có u_m+u_n=S. Tính u_p+u_q
def mn8mn_L11_C2_B2_14():
    t=random.randint(4,8)
    m = t+ random.randint(3,10)
    n = m + random.randint(2,8)
    S=random.randint(15,60) 

    k = random.choice([i for i in range(-15, 25) if i!=0])
    chon=random.randint(1,2)

    if chon==1:
        dap_an=S+k
        noi_dung = (
        f"Cho cấp số cộng $(u_n)$ có $u_{{{m+t}}}+u_{{{n-t}}}={S}$."
        f" Tính giá trị biểu thức $P=u_{{{m}}}+u_{{{n}}}+{k}$."
        )

        noi_dung=noi_dung.replace("+-","-")

        noi_dung_loigiai=(
        f"$u_{{{m+t}}}+u_{{{n-t}}}={S}\\Rightarrow u_{{{m}}}+{t}d + u_{{{n}}}-{t}d={S}$\n\n"
        f"$\\Rightarrow u_{{{m}}} + u_{{{n}}}={S}$.\n\n"
        f"$\\Rightarrow P=u_{{{m}}} + u_{{{n}}}+{k}={S+k}$.\n\n"
        f"Đáp án: {dap_an}")
    
    if chon==2:
        dap_an=k-S
        noi_dung = (
        f"Cho cấp số cộng $(u_n)$ có $u_{{{m+t}}}+u_{{{n-t}}}={S}$."
        f" Tính giá trị biểu thức $P={k}-u_{{{m}}}-u_{{{n}}}$."
        )

        noi_dung=noi_dung.replace("+-","-")

        noi_dung_loigiai=(
        f"$u_{{{m+t}}}+u_{{{n-t}}}={S}\\Rightarrow u_{{{m}}}+{t}d + u_{{{n}}}-{t}d={S}$\n\n"
        f"$\\Rightarrow u_{{{m}}} + u_{{{n}}}={S}$.\n\n"
        f"$\\Rightarrow P={k}-u_{{{m}}}-u_{{{n}}}={k}-(u_{{{m}}}+u_{{{n}}})={k-S}$.\n\n"
        f"Đáp án: {dap_an}")
    
    

    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")   
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_15]-TL-M2. Tính giá của một cái máy sau n năm sử dụng
def mn8mn_L11_C2_B2_15():
    u1 = random.randint(600,999)
    d = random.choice([-5*i for i in range (1,10)])   
    n=random.randint(5,15)
    u_n=u1+n*d

    noi_dung = (f"Giá của một cái máy phục vụ sản xuất lúc mới mua là ${{{u1}}}$ triệu đồng."
    f" Cứ sau mỗi năm sử dụng, giá của chiếc máy đó giảm ${{{-d}}}$ triệu đồng."    
    f" Giá của chiếc máy sau ${{{n}}}$ năm sử dụng.")        
    debai_word= f"{noi_dung}\n"    
    
    dap_an=u_n

    noi_dung_loigiai=(
    f"Giá của cái máy lập cấp số cộng với $u_1={u1}$ và $d={d}$.\n\n"    
   f"Giá chiếc máy sau ${{{n}}}$ năm sử dụng là: $u_{n+1}={u1}+{n}.({d})={u_n}$.\n\n"
        
    f"Đáp án: {dap_an}" )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_16]-TL-M2. Bài toán trồng cây theo cấp số cộng
def mn8mn_L11_C2_B2_16():
    u1 = random.randint(1, 4)
    d = random.randint(1, 4)

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"

    n=random.choice([i for i in range(15,25) if i%2==0 ])    
    S_n=int(n*(2*u1+(n-1)*d)/2)
    
    noi_dung = (f"Người ta trồng ${{{S_n}}}$ cái cây vào khuôn viên của một công viên hình tam giác với quy luật như sau:"
        f" hàng thứ nhất có ${{{u1}}}$ cây, hàng thứ hai có ${{{u1+d}}}$ cây, hàng thứ ba có ${{{u1+2*d}}}$ cây,..."
        f" Tính số hàng cây được trồng."
    )    
  
    dap_an=n

    noi_dung_loigiai=(
    f"Cách trồng ${{{S_n}}}$ cây trong khuôn viên hình tam giác như trên lập thành một cấp số cộng $(u_n)$ với"
    f" số ${{u_n}}$ là số cây ở hàng thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
    f"Tổng số cây được trồng là: $S_n={S_n}\\Leftrightarrow \\dfrac{{n}}{{2}}[2.{u1}+(n-1).{d}]={S_n}\\Rightarrow n={n}$.\n\n"
    f"Như vậy số hàng trồng cây là: ${{{n}}}$.\n\n"
    f"Đáp án: {dap_an}"
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_17]-TL-M3. Bài toán tính số lượng thỏa mãn cấp số cộng
def mn8mn_L11_C2_B2_17():
    chon=random.randint(1,3)
    if chon==1:
        u1 = random.randint(10, 20)
        d = random.randint(3, 7)
        n=random.randint(15,25)
        u_n=u1+(n-1)*d

        S_n=int(n*(2*u1+(n-1)*d)/2)


        noi_dung = (f"Một rạp hát được thiết kế các hàng ghế ngồi của khán giả hình vòng cung với ${{{u1}}}$ chỗ ngồi trong hàng đầu tiên,"
            f" ${{{u1+d}}}$ chỗ ngồi trong hàng thứ hai, ${{{u1+2*d}}}$ chỗ ngồi trong hàng thứ ba, và cứ thế tiếp tục."
            f" Tính tổng số chỗ ngồi của rạp hát biết rạp hát có ${{{n}}}$ hàng ghế."
        )    

        dap_an=S_n

        noi_dung_loigiai=(
        f"Số chỗ ở mỗi hàng lập thành một cấp số cộng $(u_n)$ với"
        f" số ${{u_n}}$ là số chỗ ở hàng thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
        f" Tổng số chỗ ngồi: $S_{{{n}}}=\\dfrac{{{n}}}{{2}}[2.{u1}+{n-1}.{d}]={S_n}$.\n\n"
        f"Đáp án: {dap_an}")
    
    if chon==2:
        u1 = random.randint(10, 20)
        d = random.randint(2, 5)
        n=random.randint(8,15)
        u_n=u1+(n-1)*d

        S_n=int(n*(2*u1+(n-1)*d)/2)

        noi_dung = (f"Một rạp chiếu phim ngoài trời có chỗ cho ${{{u1}}}$ xe trong hàng đỗ xe đầu tiên,"
            f"${{{u1+d}}}$ xe trong hàng thứ hai, ${{{u1+2*d}}}$ xe trong hàng thứ ba, và cứ thế tiếp tục."
            f" Hãy tìm số xe có thể đỗ được nếu có ${{{n}}}$ hàng đỗ trong rạp."
        )        
        dap_an=u_n
        noi_dung_loigiai=(
        f"Số xe ở mỗi hàng lập thành một cấp số cộng $(u_n)$ với"
        f" số ${{u_n}}$ là số xe ở hàng thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
        f" Số xe đỗ ở hàng thứ ${{{n}}}$: $u_{{{n}}}={u1}+{n-1}.{d}={u1+(n-1)*d}$.\n\n"
        f"Đáp án: {dap_an}")
    
    if chon==3:
        u1 = random.randint(1, 4)
        d = random.randint(1, 3)

        n=random.randint(5,10)
        t=random.randint(2,4) 

        so_hs=random.randint(30,40)
        u1_new=u1*so_hs
        d_new=d*so_hs

        S_n=int(n*(2*u1_new+(n-1)*d_new)/2)
        dap_an=f"{round(S_n/1000,2):.2f}".replace(".",",")

        lop=f"{random.choice(["10","11", "12"])}{random.choice(["A","B"])}{random.randint(1,9)}"

        noi_dung = (f"Hưởng ứng lời kêu gọi của Đoàn trường, lớp {lop} dự kiến quyên góp tiền để đi làm từ thiện như sau:"
            f" ngày đầu quyên góp được mỗi bạn bỏ ${{{u1}}}$ (ngàn đồng) vào lợn đất,"
            f" các ngày sau cứ {t} ngày một lần mỗi bạn bỏ vào lợn hơn lần trước là ${{{d}}}$ (ngàn đồng)."
            f" Hỏi sau ${{{t*n}}}$ ngày thì lớp {lop} quyên góp được bao nhiêu tiền (triệu đồng) biết lớp có {so_hs} học sinh."
        )        
   
        noi_dung_loigiai=(
        f" Gọi $u_n$ là số tiền quyên góp được của lần thứ ${{n}}$.\n\n"
        f" Lần đầu tiên cả lớp quyên góp được $u_1={so_hs}.{u1}={u1_new}$ (ngàn đồng).\n\n"
        f" Từ các lần sau trở đi, lớp quyên góp được hơn lần trước $d={so_hs}.{d}={d_new}$ (ngàn đồng).\n\n"
        f" Dãy $(u_n)$ là cấp số cộng với $u_1={so_hs*u1}$, công sai $d={d_new}.$\n\n"
        f" Số tiền quyên góp được sau ${{{t*n}}}$ ngày (ứng với lần thứ {n}) là:\n\n"
        f" $S_{{{n}}}=\\dfrac{{{n}}}{{2}}[2.{u1_new}+{n-1}.{d_new}]={S_n}$ (ngàn đồng) ={dap_an} (triệu đồng).\n\n"
        f"Đáp án: {dap_an}")   
    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_18]-TL-M2. Bài toán tính số vật khi xếp chồng và giảm dần theo cấp số cộng
def mn8mn_L11_C2_B2_18():
    u1 = random.randint(20, 30)
    d = random.randint(-4, -1)
    n=random.randint(7,15)
    u_n=u1+(n-1)*d
    while u_n<=3:
        u1 = random.randint(20, 30)
        d = random.randint(-4, -1)
        n=random.randint(7,15)
        u_n=u1+(n-1)*d

    S_n=int(n*(2*u1+(n-1)*d)/2)

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"

    chon=random.randint(1,2)    

    if chon==1:
        noi_dung = (f"Người ta xếp các cột điện cao thế nằm chồng lên nhau trong sân theo quy luật như sau:"
            f" lớp đầu tiên có ${{{u1}}}$ cột, lớp thứ hai có ${{{u1+d}}}$ cột, lớp thứ ba có ${{{u1+2*d}}}$ cột, và cứ tiếp tục giảm dần."
            f" Nếu có tổng cộng ${{{n}}}$ lớp thì có tất cả bao nhiêu cột điện đã được xếp."
        )    
        
        dap_an=S_n

        noi_dung_loigiai=(
        f"Số cột điện ở mỗi lớp  lập thành một cấp số cộng $(u_n)$ với"
        f" số ${{u_n}}$ là số cột điện ở lớp thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
        f" Số cột điện ở lớp thứ ${{{n}}}$: $u_{{{n}}}={u1}+{n-1}.{st_d}={u1+(n-1)*d}$.\n\n"
        f" Tổng số cột điện là: $S_{{{n}}}=\\dfrac{{{n}}}{{2}}[2.{u1}+{n-1}.{st_d}]={S_n}$.\n\n"

        f"Đáp án: {dap_an}"
        )   
     
    if chon==2:
        do_vat=["vỏ lon nước ngọt", "mảnh giấy bìa nhỏ", "chai thủy tinh", "mảnh giấy màu", "hộp quà" ]
        ten_chung=["vỏ lon", "mảnh giấy", "chai", "mảnh giấy", "hộp" ]
        i=random.randint(0,4)
        do_vat, ten_chung=do_vat[i], ten_chung[i]
        noi_dung = (f"Người ta xếp các {do_vat} thành dạng hình tháp theo quy luật như sau:"
            f" tầng dưới cùng có ${{{u1}}}$ {ten_chung}, tầng thứ hai có ${{{u1+d}}}$ {ten_chung}, tầng thứ ba có ${{{u1+2*d}}}$ {ten_chung}, và cứ tiếp tục giảm dần."
            f" Nếu có tổng cộng ${{{n}}}$ tầng thì có tất cả bao nhiêu {ten_chung} đã được xếp."
        )    
        
        dap_an=S_n

        noi_dung_loigiai=(
        f"Số {ten_chung} ở mỗi tầng lập thành một cấp số cộng $(u_n)$ với"
        f" số ${{u_n}}$ là số {ten_chung} ở tầng thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
        f" Số {ten_chung} ở tầng thứ ${{{n}}}$: $u_{{{n}}}={u1}+{n-1}.{st_d}={u1+(n-1)*d}$.\n\n"
        f" Tổng số {ten_chung} được xếp là: $S_{{{n}}}=\\dfrac{{{n}}}{{2}}[2.{u1}+{n-1}.{st_d}]={S_n}$.\n\n"

        f"Đáp án: {dap_an}"
        )    
    
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_19]-TL-M3. Bài toán tính số hàng khi xếp đồ vật và giảm dần theo cấp số cộng
def mn8mn_L11_C2_B2_19():
    u1 = random.randint(20, 30)
    d = random.randint(-4, -1)
    n=random.randint(7,15)
    u_n=u1+(n-1)*d
    while u_n<=3:
        u1 = random.randint(20, 30)
        d = random.randint(-4, -1)
        n=random.randint(7,15)
        u_n=u1+(n-1)*d

    S_n=int(n*(2*u1+(n-1)*d)/2)

    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if d>0:
        st_d=d
    else:
        st_d=f"({d})"


    do_vat=["vỏ lon nước ngọt", "mảnh giấy bìa nhỏ", "chai thủy tinh", "mảnh giấy màu", "hộp quà" ]
    ten_chung=["vỏ lon", "mảnh giấy", "chai", "mảnh giấy", "hộp" ]
    i=random.randint(0,4)
    do_vat, ten_chung=do_vat[i], ten_chung[i]
    noi_dung = (f"Người ta xếp ${{{S_n}}}$ {do_vat} thành dạng hình tháp theo quy luật như sau:"
        f" tầng dưới cùng có ${{{u1}}}$ {ten_chung}, tầng thứ hai có ${{{u1+d}}}$ {ten_chung}, tầng thứ ba có ${{{u1+2*d}}}$ {ten_chung}, và cứ tiếp tục giảm dần."
        f" Tính số tầng đã xếp."
    )    
    
    dap_an=n

    noi_dung_loigiai=(
    f"Số {ten_chung} ở mỗi tầng lập thành một cấp số cộng $(u_n)$ với"
    f" số ${{u_n}}$ là số {ten_chung} ở tầng thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
    f" Tổng số {ten_chung} được xếp là: $S_n=\\dfrac{{n}}{{2}}[2.{u1}+(n-1).{st_d}]={S_n} \\Rightarrow n={n}$.\n\n"

    f"Đáp án: {dap_an}"
    )    

    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D11_C2_B2_20]-TL-M2. Bài toán tính số hàng khi xếp tăng dần theo cấp số cộng
def mn8mn_L11_C2_B2_20():
    chon=random.randint(1,2)
    if chon==1:
    
        u1 = random.randint(2, 6)
        d = random.randint(3, 7)

        if u1>0:
            st_u1=u1
        else:
            st_u1=f"({u1})"

        if d>0:
            st_d=d
        else:
            st_d=f"({d})"

        n=random.choice([i for i in range(7,18) if i%2==0 ])    
        S_n=int(n*(2*u1+(n-1)*d)/2)

        su_kien=random.choice(["chúc mừng khai trương", "trang trí đám cưới", "chúc mừng sinh nhật", 
            "chúc mừng ngày Quốc tế Phụ nữ", "chúc mừng ngày Phụ nữ Việt Nam"])
        
        noi_dung = (f"Mộp shop hoa tươi nhận được yêu cầu làm một kệ hoa {su_kien} gồm ${{{S_n}}}$"
            f" bông hoa sắp xếp thành các vòng tròn kế tiếp nhau theo quy luật như sau:"
            f" vòng trong cùng có ${{{u1}}}$ bông hoa, vòng thứ hai có ${{{u1+d}}}$ bông hoa, vòng thứ ba có ${{{u1+2*d}}}$ bông hoa,..."
            f" Tính số vòng hoa được làm để thỏa mãn quy luật trên."
        )    
      
        dap_an=n

        noi_dung_loigiai=(
        f"Cách làm ${{{S_n}}}$ bông hoa thành các vòng như quy luật đã cho lập thành một cấp số cộng $(u_n)$ với"
        f"số ${{u_n}}$ là số bông hoa ở vòng thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
        f"Tổng số vòng hoa là: $S_n={S_n}\\Leftrightarrow \\dfrac{{n}}{{2}}[2.{u1}+(n-1).{d}]={S_n}\\Rightarrow n={n}$.\n\n"
        f"Như vậy số vòng hoa cần làm là: ${{{n}}}$.\n\n"
        f"Đáp án: {dap_an}"
        )    
    
    if chon==2:   

        u1 = random.randint(10, 20)
        d = random.randint(3, 7)
        n=random.randint(15,25)
        u_n=u1+(n-1)*d

        S_n=int(n*(2*u1+(n-1)*d)/2)

        if u1>0:
            st_u1=u1
        else:
            st_u1=f"({u1})"

        if d>0:
            st_d=d
        else:
            st_d=f"({d})"


        noi_dung = (f"Một kiến trúc sư thiết kế một rạp hát với ${{{u1}}}$ chỗ ngồi trong hàng đầu tiên,"
            f" ${{{u1+d}}}$ chỗ ngồi trong hàng thứ hai, ${{{u1+2*d}}}$ chỗ ngồi trong hàng thứ ba, và cứ thế tiếp tục."
            f" Nếu muốn rạp hát có sức chứa ${{{S_n}}}$ chỗ ngồi thì kiến trúc sư phải thiết kế bao nhiêu hàng ghế."
        )    

        dap_an=n

        noi_dung_loigiai=(
        f"Số chỗ ở mỗi hàng lập thành một cấp số cộng $(u_n)$ với"
        f" số ${{u_n}}$ là số chỗ ở hàng thứ ${{n}}$ và $u_1={u1}$ và công sai $d={d}$.\n\n"
        f" Tổng số chỗ ngồi: $S_n=\\dfrac{{n}}{{2}}[2.{u1}+(n-1).{d}]={S_n}\\Rightarrow n={n}$.\n\n"
        f"Đáp án: {dap_an}")
    
    
     
    
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

############## CẤP SỐ NHÂN ##############
#D11_C2_B3_01. Cho cấp số nhân có u1, q. Tìm số hạng thứ k
def mn8mn_L11_C2_B3_01():
    u1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])    
    list_q=[-3,-2,-0.5, 0.4, 0.5, 1.5, 2, 2.5, 3, 3.5, 4]
    q = random.choice(list_q)
    k = random.randint(3,10)         
    pa_A= f"*$u_{{{k}}}= {latex(my_module.hien_phan_so(u1*q**(k-1)))}$"
    pa_B= f"$u_{{{k}}}={latex(my_module.hien_phan_so((u1*q**(k))))} $"
    pa_C= f"$u_{{{k}}}={latex(my_module.hien_phan_so((u1*q**(k+1))))}$"
    pa_D= f"$u_{{{k}}}={latex(my_module.hien_phan_so((u1+(k-1)*q)))}$"

    noi_dung= f"Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1={u1}$ và công bội $q= {latex(my_module.hien_phan_so(q))}$. Tìm số hạng $u_{{{k}}}$."
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

#D11_C2_B3_02. Cho cấp số nhân có u_n, u_m. Tìm  q.
def mn8mn_L11_C2_B3_02():
    u1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])    
    if u1==0:
        u1=random.randint(1,6)

    u2 = random.randint(-6,6)
    if u2==0:
        u2=random.randint(1,6)

    if u2==u1:
        u2=u1 + random.randint(1,6)
    n = random.randint(1,10)
    
    kq=latex(my_module.hien_phan_so(u2/u1))
    kq2=latex(my_module.hien_phan_so(u1/u2))
    kq3=latex(my_module.hien_phan_so(u2-u1))
    kq4=latex(my_module.hien_phan_so(u1-u2))

    pa_A= f"*${{q={kq}}}$"
    pa_B= f"${{q={kq2}}}$"
    pa_C= f"${{q={kq3}}}$"
    pa_D= f"${{q={kq4}}}$"
    #Trộn các phương án

    noi_dung= f"Cho cấp số nhân $(u_n)$ có  ${{u_{{{n}}}={u1}}}$ và ${{u_{{{n+1}}}={u2}}}$. Tìm công bội $q$ cấp số nhân đã cho."
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


#D11_C2_B3_03. Cho cấp số nhân có u1, q. Tính tổng vài số hạng.
def mn8mn_L11_C2_B3_03():
    u1 = random.choice([random.randint(-6, -1), random.randint(1, 6)])    
    list_q=[-3,-2, 0.5, 1.5, 2, 2.5, 3, 3.5, 4]
    q = random.choice(list_q)
    k_1 = random.randint(2,4)            
    k_2 = random.randint(5,7)    
    k_3 = random.randint(8,10)
    pa_A= f"*$S= {u1*q**(k_1-1) + u1*q**(k_2-1) + u1*q**(k_3-1)}$"
    pa_B= f"$S= {u1*q**(k_1) + u1*q**(k_2) + u1*q**(k_3)}$"
    pa_C= f"$S= {u1 +(k_1-1)*q + u1 +(k_2-1)*q + u1 +(k_3-1)*q}$"
    pa_D= f"$S= {u1*(q**(k_3-1)-1)/(q-1)}$"
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1={u1}$" \
        f" và công bội $q={latex(my_module.hien_phan_so(q))}$. "\
        f"Tính $S = u_{{{k_1}}}  + u_{{{k_2}}} + u_{{{k_3}}}$." 
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

#D11_C2_B3_04. Cho cấp số nhân có u1, q. Tính tổng S_n.
def mn8mn_L11_C2_B3_04():
    u1 = random.choice([random.randint(-6, -1), random.randint(1, 6)]) 
    list_q=[-3,-2, 0.5, 1.5, 2, 2.5, 3, 3.5, 4]
    q = random.choice(list_q)

    n = random.randint(4,10)

    kq=latex(my_module.hien_phan_so(u1*(q**n-1)/(q-1)))
    kq2=latex(my_module.hien_phan_so(u1/(q-1)))
    kq3=latex(my_module.hien_phan_so(u1+(n-1)*q))
    kq4=latex(my_module.hien_phan_so(u1*(q**n)/(q-1)))

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"

    noi_dung = f"Cho cấp số nhân $(u_n)$ có số hạng đầu ${{u_1={u1}}}$ và công bội ${{q={latex(my_module.hien_phan_so(q))}}}$. Tính tổng của ${{{n}}}$ số hạng đầu tiên của cấp số nhân đã cho."
    
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

#D11_C2_B3_05. Tính số virut tạo ra sau một số khoảng thời gian.
def mn8mn_L11_C2_B3_05():
    u1 = random.randint(2,7)  
    p = random.randint(3,6)
    #Số lần phát triển
    n = random.randint(4,10)
    #Số phút
    so_phut=random.choice([5, 10, 15, 20, 30])
    thoi_gian=n*so_phut
    q=p+1

    kq=u1*(q**n)
    kq2=u1*q**(n+1)
    kq3=u1*(q**(n)+1)
    kq4=u1*q**(n-1)

    pa_A= f"*${{{latex(my_module.hien_phan_so(kq))}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{latex(my_module.hien_phan_so(kq3))}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án

    noi_dung= f"Một loại virus máy tính cứ {so_phut} phút thì một máy sẽ lây nhiễm cho {p} máy trong cùng hệ thống.\n" \
    f"Biết rằng ban đầu có {u1} máy tính bị nhiễm phải virus này. Tính tổng số máy tính bị nhiễm virus sau ${{{thoi_gian}}}$ phút."

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


#D11_C2_B3_06. Tính số virut tạo ra sau một số khoảng thời gian.
def mn8mn_L11_C2_B3_06():
    u1 = random.randint(2,7)  
    p = random.randint(3,6)
    #Số lần phát triển
    n = random.randint(4,10)
    #Số phút
    so_phut=random.choice([5, 10, 15, 20, 30])
    thoi_gian=latex(my_module.hien_phan_so(n*so_phut/60))
    q=p+1
    kq=u1*q**n
    kq2=u1*q**(n+1)
    kq3=u1*q**(n-2)
    kq4=u1*q**(n-1)

    pa_A= f"*${{{latex(kq)}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án

    noi_dung= f"Một loại virus máy tính cứ {so_phut} phút thì một máy sẽ lây nhiễm cho {p} máy trong cùng hệ thống.\n" \
    f"Biết rằng ban đầu có {u1} máy tính bị nhiễm phải virus này. Tính tổng số máy tính bị nhiễm virus sau ${{{thoi_gian}}}$ giờ."
    
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

#[D11_C2_B3_07]-TF-M3. Cho CSN có un,u_n+1. Xét Đ-S: q, u_k, S_k, u_n
def mn8mn_L11_C2_B3_07():
    u1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    q = random.choice([random.randint(-5, -2), random.randint(2, 5),1/2, 2/3, 3/4, -1/2])
    u2=u1*q
    u4=u1*q**3 
    
    if u1>0:
        st_u1=u1
    else:
        st_u1=f"({u1})"

    if q>0:
        st_q=phan_so(q)   
        
    if q in [1/2, 2/3, 3/4, -1/2] or q<0:
        st_q=f"\\left({phan_so(q)}\\right)"

    chon=random.randint(1,2)    
    if chon==1:
        noi_dung = f"Cho cấp số nhân $(u_n)$ có ${{u_1={u1}}}$ và ${{u_4={phan_so(u4)}}}$. Xét tính đúng-sai của các khẳng định sau:" 
        kq1_T=f"* Công bội của $(u_n)$ là $q={phan_so(q)}$" 
        kq1_F=f"Công bội của $(u_n)$ là $q={random.choice([phan_so(q+1),phan_so(-q), phan_so(q-1)])}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"$u_4={phan_so(u4)}={st_u1}.q^3\\Rightarrow q^3={phan_so(q**3)}\\Rightarrow q={phan_so(q)}$."

    if chon==2:
        n=random.randint(1,4)
        m=n+1
        un=phan_so(u1*q**(n-1))
        um=phan_so(u1*q**(m-1))
        noi_dung = f"Cho cấp số nhân $(u_n)$ có ${{u_{n}={un}}}$ và ${{u_{m}={um}}}$. Xét tính đúng-sai của các khẳng định sau:" 
        kq1_T=f"* Công bội của $(u_n)$ là $q={phan_so(q)}$" 
        kq1_F=f"Công bội của $(u_n)$ là $q={random.choice([phan_so(q+1),phan_so(-q), phan_so(q-1)])}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"$q=\\dfrac{{u_{m}}}{{u_{n}}}=\\dfrac{{{um}}}{{{un}}}\\Rightarrow q={phan_so(q)}$."    

    
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    m = random.randint(6,11)    
    u_m= u1*q**(m-1)

    kq2_T=f"* $u_{{{m}}}={phan_so(u_m)}$"
    kq2_F=f" $u_{{{m}}}={phan_so(u1*q**(m))}$"
    kq2=random.choice([kq2_T, kq2_F])    
    HDG=(f"$u_{{{m}}}={st_u1}.{st_q}^{{{m-1}}}={phan_so(u_m)}$."
            )
            
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=random.randint(4,10)
    Sn=u1*(q**n-1)/(q-1)
    Sn_false=u1*(q**n-1)/(q+1)

    kq3_T=f"* Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn)}$" 
    kq3_F=f"Tổng của ${{{n}}}$ số hạng đầu tiên của $(u_n)$ bằng ${phan_so(Sn_false)}$"
    kq3=random.choice([kq3_T, kq3_F])    
        
    HDG=f"$S_{{{n}}}={st_u1}\\dfrac{{{st_q}^{{{n}}}-1}}{{{st_q}-1}}={phan_so(Sn)}$."

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=symbols("n")
    kq4_T=f"* $u_n={st_u1}.{st_q}^{{n-1}}$"
    kq4_F=f"$u_n={st_u1}.{st_q}^{{n}}$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$u_n={st_u1}.{st_q}^{{n-1}}$."
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

#[D11_C2_B3_08]-M2. Nhận dạng dãy số hữu hạn là 1 cấp số nhân
def mn8mn_L11_C2_B3_08():
    n=symbols("n")
    
    noi_dung=f"Trong các dãy số sau, dãy nào là một cấp số nhân"

    u1 = random.choice([i for i in range(-3, 3) if i!=0])
    q = random.choice([i for i in range(-4, 4) if i!=0])
    u1,u2,u3,u4=[u1*q**i for i in range(4)]

    kq=f"${u1};{u2};{u3};{u4}$"
    noi_dung_loigiai=f"{kq} là một cấp số nhân với $u_1={u1},q={q}$."

    u1 = random.choice([i for i in range(-5, 5) if i!=0])
    q = random.choice([i for i in range(2, 4) if i!=0])
    u1,u2,u3,u4=[u1+i*q for i in range(4)]

    kq2=f"${u1};{u2};{u3};{u4}$"

    u1 = random.choice([i for i in range(-10, 10) if i!=0])
    q = random.choice([i for i in range(-3, -2) if i!=0])
    u1,u2,u3,u4=[i+q**i for i in range(4)]

    kq3=f"${u1};{u2};{u3};{u4}$"

    u1 = random.choice([i for i in range(-5, 5) if i!=0])
    q = random.choice([i for i in range(2, 3) if i!=0])
    u1,u2,u3,u4=[u1*q**(i+1) for i in range(4)]

    kq4=f"${u1};{u2};{u3};{u4+1}$"

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    #random.shuffle(list_PA)
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





