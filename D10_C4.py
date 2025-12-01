import math
from sympy import *
import sympy as sp
import random
from fractions import Fraction #Thư viện chuyển về dạng phân thức
import my_module

def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier
#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(10000000000000))
    return m
def thay_cong_tru(st):
    return st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("1x","x").replace("1y","y").replace("-1x","-x").replace("-1y","-y")
def code_latex_hinhbinhhanh(a,b,c,d):
    code=rf"""\begin{{tikzpicture}}[line join=round, line cap=round,thick]
\coordinate ({a}) at (1,3);
\coordinate ({b}) at (6,3);
\coordinate ({d}) at (0,0);
\coordinate ({c}) at ($({b})+({d})-({a})$);
\draw({a})--({b})--({c})--({d})--cycle;
\foreach \i/\g in {{{a}/90,{b}/90,{c}/-90,{d}/-90}}{{\draw[fill=white](\i) circle (1.5pt) ($(\i)+(\g:3mm)$) node[scale=1]{{$\i$}};}}
\end{{tikzpicture}}"""
    return code
#BÀI 1- GIÁ TRỊ LƯỢNG GIÁC CỦA MỘT GÓC TỪ 0 ĐẾN 180

#[D10_C4_B1_01]. Tìm dấu của một giá trị lượng giác từ 0 đến 180 độ.
def yy3yy_L10_C4_B1_01():
    C_degree =random.randint(1,179)
    C_radian = math.radians(C_degree)
    ten_goc = random.choice(["sin", "cos", "tan"])
    if C_degree <90:
        if ten_goc=="sin":
            kq=f"\\sin{C_degree}^\\circ >0"
            kq2=f"\\cot {C_degree}^\\circ <0"
            kq3=f"\\cos {C_degree}^\\circ <0"
            kq4=f"\\tan {C_degree}^\\circ <0"
        if ten_goc=="cos":
            kq=f"\\cos {C_degree}^\\circ >0"
            kq2=f"\\cot {C_degree}^\\circ <0"
            kq3=f"\\cos {C_degree}^\\circ <0"
            kq4=f"\\tan {C_degree}^\\circ <0"
        if ten_goc=="tan":
            kq=f"\\tan {C_degree}^\\circ >0"
            kq2=f"\\cot {C_degree}^\\circ <0"
            kq3=f"\\cos {C_degree}^\\circ <0"
            kq4=f"\\sin {C_degree}^\\circ <0"
    else:
        if ten_goc=="sin":
            kq=f"\\sin {C_degree}^\\circ >0"
            kq2=f"\\cot {C_degree}^\\circ >0"
            kq3=f"\\cos {C_degree}^\\circ >0"
            kq4=f"\\tan {C_degree}^\\circ >0"
        if ten_goc=="cos":
            kq=f"\\cos {C_degree}^\\circ <0"
            kq2=f"\\cot {C_degree}^\\circ >0"
            kq3=f"\\sin {C_degree}^\\circ <0"
            kq4=f"\\tan {C_degree}^\\circ >0"
        if ten_goc=="tan":
            kq=f"\\tan {C_degree}^\\circ <0"
            kq2=f"\\cot {C_degree}^\\circ >0"
            kq3=f"\\cos {C_degree}^\\circ >0"
            kq4=f"\\sin {C_degree}^\\circ <0"
    #Tạo các phương án
    pa_A=f"*${{{kq}}}$"
    pa_B=f"${{{kq2}}}$"
    pa_C=f"${{{kq3}}}$"
    pa_D=f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm khẳng định đúng trong các khẳng định sau."
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  

    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
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

#[D10_C4_B1_02]. Cho giá trị lượng giác, tìm góc.
def yy3yy_L10_C4_B1_02():
    ten_goc = random.choice(["sin", "cos"])
    if ten_goc == "sin": 
        gia_tri=random.choice([1,1/2,sqrt(3)/2,sqrt(2)/2])
        kq=math.degrees(asin(gia_tri))
        kq2=math.degrees(acos(gia_tri))
        kq3=random.randint(0,40)
        kq4=random.randint(41,80)
        if gia_tri == sqrt(2)/2:
            kq2=130+random.randint(10,30)
    if ten_goc == "cos":
        gia_tri=random.choice([1,1/2,sqrt(3)/2,sqrt(2)/2,-1,-1/2,-sqrt(3)/2,-sqrt(2)/2])
        kq=math.degrees(acos(gia_tri))
        kq2=abs(math.degrees(asin(gia_tri)))
        kq3=random.randint(0,40)
        kq4=random.randint(41,80)
        
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
    noi_dung= f"Biết $\\{ten_goc}\\alpha={latex(gia_tri)}$. Tìm góc $\\alpha$."

    #Tạo các phương án
    pa_A=f"*$\\alpha={kq:.0f}^\\circ$"
    pa_B=f"$\\alpha={kq2:.0f}^\\circ$"
    pa_C=f"$\\alpha={kq3:.0f}^\\circ$"
    pa_D=f"$\\alpha={kq4:.0f}^\\circ$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  

    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
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



#[D10_C4_B1_03]-M2 Cho sin tìm cos
def yy3yy_L10_C4_B1_03():
    triples = [(a, b, c) for a in range(1, 100) 
                       for b in range(a + 1, 100) 
                       for c in range(b + 1, 100)
                       if a**2 + b**2 == c**2]
    
    # Chọn một bộ ba ngẫu nhiên từ danh sách
    a, b, c = random.choice(triples)
    u=phan_so(a/c) 
    v=phan_so(b/c)
    chon =random.randint(1,2)
    if chon ==1:
        noi_dung=f"Cho $\\sin \\alpha = {u}$ và $ 0<\\alpha < 90^{{\\circ}}$, giá trị $\\cos \\alpha$ là: "
        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 0< \\alpha < 90^{{\\circ}}$ nên $\\cos \\alpha ={v}$ "
                
        kq=f" ${{{v}}}$"
        ds=[f"${{{phan_so((b+1)/c)}}}$",
        f"${{{phan_so((b+2)/c)}}}$",
        f"${{{phan_so((b-1)/c)}}}$",
    f"${{{phan_so((b-2)/c)}}}$",
        f"${{{phan_so((b-3)/c)}}}$",
    f"${{{phan_so((b+3)/c)}}}$"]
    if chon ==2:
        noi_dung=f"Cho $\\sin \\alpha = {u}$ và $ 90^{{\\circ}} <\\alpha < 180^{{\\circ}}$, giá trị $\\cos \\alpha$ là: "
        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 90^{{\\circ}}< \\alpha < 180^{{\\circ}}$ nên $\\cos \\alpha ={phan_so(-b/c)}$ "
                
        kq=f" ${{{phan_so(-b/c)}}}$"
        ds=[f"${{{phan_so((-b+1)/c)}}}$",
        f"${{{phan_so((-b+2)/c)}}}$",
        f"${{{phan_so((-b-1)/c)}}}$",
    f"${{{phan_so((-b-2)/c)}}}$",
        f"${{{phan_so((-b-3)/c)}}}$",
    f"${{{phan_so((-b+3)/c)}}}$"]
    kq2, kq3, kq4 = random.sample(ds, 3)  


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




#[D10_C4_B1_04]-M2 Cho sin tìm tan
def yy3yy_L10_C4_B1_04():
    triples = [(a, b, c) for a in range(1, 100) 
                       for b in range(a + 1, 100) 
                       for c in range(b + 1, 100)
                       if a**2 + b**2 == c**2]
    
    # Chọn một bộ ba ngẫu nhiên từ danh sách
    a, b, c = random.choice(triples)
    u=phan_so(a/c) 
    v=phan_so(b/c) 
    z=phan_so(a/b)
    chon =random.randint(1,2)
    if chon ==1:
        noi_dung=f"Cho $\\sin \\alpha = {u}$ và $ 0<\\alpha < 90^{{\\circ}}$, giá trị $\\tan \\alpha$ là: "
        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 0< \\alpha < 90^{{\\circ}}$ nên $\\cos \\alpha ={v}$ suy ra $\\tan \\alpha ={z}$"
                
        kq=f" ${{{z}}}$"
        ds=[f"${{{phan_so((a+1)/b)}}}$",
        f"${{{phan_so((a+2)/b)}}}$",
        f"${{{phan_so((a-1)/b)}}}$",
    f"${{{phan_so((a-2)/c)}}}$",
        f"${{{phan_so((a-3)/c)}}}$",
    f"${{{phan_so((a+3)/c)}}}$"]

    if chon ==2:
        noi_dung=f"Cho $\\sin \\alpha = {u}$ và $ 90^{{\\circ}} <\\alpha < 180^{{\\circ}}$, giá trị $\\tan \\alpha$ là: "
        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 90^{{\\circ}}< \\alpha < 180^{{\\circ}}$ nên $\\cos \\alpha ={phan_so(-b/c)}$ suy ra $\\tan \\alpha ={phan_so(-a/b)}$"
                
        kq=f" ${{{phan_so(-a/b)}}}$"
        ds=[f"${{{phan_so((-a+1)/b)}}}$",
        f"${{{phan_so((-a+2)/b)}}}$",
        f"${{{phan_so((-a-1)/b)}}}$",
    f"${{{phan_so((-a-2)/c)}}}$",
        f"${{{phan_so((-a-3)/c)}}}$",
    f"${{{phan_so((-a+3)/c)}}}$"]
    kq2, kq3, kq4 = random.sample(ds, 3)  


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



#[D10_C4_B1_05]-M2 Cho cos tìm sin
def yy3yy_L10_C4_B1_05():
    triples = [(a, b, c) for a in range(1, 100) 
                       for b in range(a + 1, 100) 
                       for c in range(b + 1, 100)
                       if a**2 + b**2 == c**2]
    
    # Chọn một bộ ba ngẫu nhiên từ danh sách
    a, b, c = random.choice(triples)
    u=phan_so(a/c) 
    v=phan_so(b/c)
    chon =random.randint(1,2)
    if chon ==1:
        noi_dung=f"Cho $\\cos \\alpha = {u}$ và $ 0<\\alpha < 90^{{\\circ}}$, giá trị $\\sin \\alpha$ là: "
        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 0< \\alpha < 180^{{\\circ}}$ nên $\\sin \\alpha ={v}$ "
                
        kq=f" ${{{v}}}$"
        ds=[f"${{{phan_so((b+1)/c)}}}$",
        f"${{{phan_so((b+2)/c)}}}$",
        f"${{{phan_so((b-1)/c)}}}$",
    f"${{{phan_so((b-2)/c)}}}$",
        f"${{{phan_so((b-3)/c)}}}$",
    f"${{{phan_so((b+3)/c)}}}$"]
    if chon ==2:
        noi_dung=f"Cho $\\cos \\alpha = {phan_so(-a/c)}$ và $ 90^{{\\circ}}<\\alpha < 180^{{\\circ}}$, giá trị $\\sin \\alpha$ là: "

        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 90^{{\\circ}} < \\alpha < 180^{{\\circ}}$ nên $\\sin \\alpha ={v}$ "
                
        kq=f" ${{{v}}}$"
        ds=[f"${{{phan_so((b+1)/c)}}}$",
        f"${{{phan_so((b+2)/c)}}}$",
        f"${{{phan_so((b-1)/c)}}}$",
    f"${{{phan_so((b-2)/c)}}}$",
        f"${{{phan_so((b-3)/c)}}}$",
    f"${{{phan_so((b+3)/c)}}}$"]
    kq2, kq3, kq4 = random.sample(ds, 3)  


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


#[D10_C4_B1_06]-M2 Cho cos tìm tan
def yy3yy_L10_C4_B1_06():
    triples = [(a, b, c) for a in range(1, 100) 
                       for b in range(a + 1, 100) 
                       for c in range(b + 1, 100)
                       if a**2 + b**2 == c**2]
    
    # Chọn một bộ ba ngẫu nhiên từ danh sách
    a, b, c = random.choice(triples)
    u=phan_so(a/c) 
    v=phan_so(b/c)
    chon =random.randint(1,2)
    if chon ==1:
        noi_dung=f"Cho $\\cos \\alpha = {u}$ và $ 0<\\alpha < 90^{{\\circ}}$, giá trị $\\tan \\alpha$ là: "
        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 0< \\alpha < 90^{{\\circ}}$ nên $\\sin \\alpha ={v}$ suy ra $\\tan \\alpha = {phan_so(b/a)}$ "
                
        kq=f" ${{{phan_so(b/a)}}}$"
        ds=[f"${{{phan_so((b+1)/a)}}}$",
        f"${{{phan_so((b+2)/a)}}}$",
        f"${{{phan_so((b-1)/a)}}}$",
    f"${{{phan_so((b-2)/a)}}}$",
        f"${{{phan_so((b-3)/a)}}}$",
    f"${{{phan_so((b+4)/a)}}}$"]
    if chon ==2:
        noi_dung=f"Cho $\\cos \\alpha = {phan_so(-a/c)}$ và $ 90^{{\\circ}}<\\alpha < 180^{{\\circ}}$, giá trị $\\tan \\alpha$ là: "

        noi_dung_loigiai=f" Ta có $\\sin^{{2}} \\alpha + \\cos^{{2}} \\alpha=1$  và $ 90^{{\\circ}} < \\alpha < 180^{{\\circ}}$ nên $\\sin \\alpha ={v}$ suy ra $\\tan \\alpha = {phan_so(-b/a)}$ "
                
        kq=f" ${{{phan_so(-b/a)}}}$"
        ds=[f"${{{phan_so((-b+1)/a)}}}$",
        f"${{{phan_so((-b+2)/a)}}}$",
        f"${{{phan_so((-b-1)/a)}}}$",
    f"${{{phan_so((-b-2)/a)}}}$",
        f"${{{phan_so((-b-3)/a)}}}$",
    f"${{{phan_so((-b+3)/a)}}}$"]
    kq2, kq3, kq4 = random.sample(ds, 3)  


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



#[D10_C4_B1_07]-M2 Cho tan tính giá trị của biểu thức 
def yy3yy_L10_C4_B1_07():
    
    b=random.choice([i for i in range(-6,6) if i!=0]) 
    c=random.choice([i for i in range(-6,6) if i!=0 and i!=1]) 

    

    triples = [(e, b1, a) for e in range(-5, 5) 
                       for b1 in range(-5, 5) 
                       for a in range(-5, 5)
                       if e-b1*a!=0 and e-b1*a !=1 and e!=0 and b1!=0 and a!=0]
    
    # Chọn một bộ ba ngẫu nhiên từ danh sách
    e, b1, a = random.choice(triples)
    c1=e-b1*a
    ds= (b*a+c) /(b1*a+c1)


    noi_dung=f"Cho $\\tan \\alpha = {a}$, giá trị của biểu thức $A= \\dfrac {{ {b}\\sin\\alpha+{c}\\cos\\alpha }}{{ {b1}\\sin\\alpha+{c1}\\cos\\alpha }}$ "
    noi_dung_loigiai=f"$A= \\dfrac {{ {b}\\tan\\alpha+{c} }}{{ {b1}\\tan\\alpha+{c1}}} ={phan_so(ds)}$"
    kq=f"${{{phan_so(ds)}}}$"
    kqs=[ f"${{{phan_so(ds+1)}}}$",f"${{{phan_so(ds-1)}}}$",f"${{{phan_so(ds+2)}}}$",f"${{{phan_so(ds-2)}}}$" ]
    kq2, kq3, kq4 = random.sample(kqs, 3)  
    
    noi_dung=noi_dung.replace("1\\sin\\alpha"," \\sin\\alpha").replace("-1\\cos\\alpha"," -\\cos\\alpha").replace("-1\\sin\\alpha"," -\\sin\\alpha").replace("+ -","-")
    noi_dung=thay_cong_tru(noi_dung)
    noi_dung_loigiai=noi_dung_loigiai.replace("-1\\tan\\alpha"," -\\tan\\alpha").replace("1\\tan\\alpha"," -\\tan\\alpha")

    noi_dung_loigiai=thay_cong_tru(noi_dung_loigiai)
    


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


#[D10_C4_B1_08]-TF-M2. Cho cos. Xét Đ-S: dấu của sin, sinx, sin(180-x), tan(90-x)
def yy3yy_L10_C4_B1_08():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])

    cosx=random.choice([1/random.randint(2,7),2/3,2/5,3/4,3/5,4/5,5/6])
    noi_dung = (
    f"Cho góc ${{{x}}}$ thỏa mãn $\\cos {x}={phan_so(cosx)}$. Xét tính đúng-sai của các khẳng định sau:"
    )    
    
    kq1_T=f"* $\\sin {x}>0$" 
    kq1_F=f"$\\sin {x}<0$"
    
    HDG=f"$\\sin {x}>0$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    sinx=sqrt(1-cosx**2)
    sinx_f=sqrt(1+cosx**2)

    kq2_T=f"* $\\sin {x}={latex(nsimplify(sinx))}$"
    kq2_F=f" $\\sin {x}={latex(nsimplify(sinx_f))}$"
    
    HDG=f"$\\sin {x}=\\sqrt{{1-{phan_so(cosx**2)}}}={latex(nsimplify(sinx))}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $\\sin (180^\\circ-{x})={latex(nsimplify(sinx))}$" 
    kq3_F=f"$\\sin (180^\\circ-{x})=-{latex(nsimplify(sinx))}$"
    
    HDG=f" $\\sin (180^\\circ-{x})=\\sin {x} = {latex(nsimplify(sinx))}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    tanx=sinx/cosx
    cotx=cosx/sinx
    chon=random.randint(1,2)

    if chon==1:
        kq4_T=f"* $\\tan (90^\\circ-{x})={latex(nsimplify(cotx))}$"
        kq4_F=f"$\\tan (90^\\circ-{x})=-{latex(nsimplify(cotx))}$" 
        
        HDG=(f"$\\cot {x}={latex(nsimplify(cosx))}:{latex(nsimplify(sinx))}={latex(nsimplify(cotx))}$.\n\n"
            f" $\\tan (90^\\circ-{x})=\\cot {x}={latex(nsimplify(cotx))}$.")
    
    if chon==2:
        kq4_T=f"* $\\cot (90^\\circ-{x})={latex(nsimplify(tanx))}$"
        kq4_F=f"$\\cot (90^\\circ-{x})=-{latex(nsimplify(tanx))}$" 
        
        HDG=(f"$\\tan {x}={latex(nsimplify(sinx))}:{latex(nsimplify(cosx))}={latex(nsimplify(tanx))}$.\n\n"
            f" $\\cot (90^\\circ-{x})=\\tan {x}={latex(nsimplify(tanx))}$.")
    
    
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

#[D10_C4_B1_09]-TF-M2. Cho sin. Xét Đ-S: dấu của cos, cosx, cos(180-x), tan(90-x)
def yy3yy_L10_C4_B1_09():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sinx=random.choice([1/random.randint(2,7),2/3,2/5,3/4,3/5,4/5,5/6])
    noi_dung = (
    f"Cho góc ${x}(0^\\circ<{x}<90^\\circ) $ thỏa mãn $\\sin {x}={phan_so(sinx)}$. Xét tính đúng-sai của các khẳng định sau:"
    )    
    
    kq1_T=f"* $\\cos {x}>0$" 
    kq1_F=f"$\\cos {x}<0$"
    
    HDG=f"$\\cos {x}>0$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cosx=sqrt(1-sinx**2)
    cosx_f=sqrt(1+sinx**2)

    kq2_T=f"* $\\cos {x}={latex(nsimplify(cosx))}$"
    kq2_F=f" $\\cos {x}={latex(nsimplify(cosx_f))}$"
    
    HDG=f"$\\cos {x}=\\sqrt{{1-{phan_so(sinx**2)}}}={latex(nsimplify(cosx))}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $\\cos (180^\\circ-{x})=-{latex(nsimplify(cosx))}$" 
    kq3_F=f"$\\cos (180^\\circ-{x})={latex(nsimplify(cosx))}$"
    
    HDG=f" $\\cos (180^\\circ-{x})=-\\cos {x} = -{latex(nsimplify(cosx))}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    tanx=sinx/cosx
    cotx=cosx/sinx
    chon=random.randint(1,2)

    if chon==1:
        kq4_T=f"* $\\tan (90^\\circ-{x})={latex(nsimplify(cotx))}$"
        kq4_F=f"$\\tan (90^\\circ-{x})=-{latex(nsimplify(cotx))}$" 
        
        HDG=(f"$\\cot {x}={latex(nsimplify(cosx))}:{latex(nsimplify(sinx))}={latex(nsimplify(cotx))}$.\n\n"
            f" $\\tan (90^\\circ-{x})=\\cot {x}={latex(nsimplify(cotx))}$.")
    
    if chon==2:
        kq4_T=f"* $\\cot (90^\\circ-{x})={latex(nsimplify(tanx))}$"
        kq4_F=f"$\\cot (90^\\circ-{x})=-{latex(nsimplify(tanx))}$" 
        
        HDG=(f"$\\tan {x}={latex(nsimplify(sinx))}:{latex(nsimplify(cosx))}={latex(nsimplify(tanx))}$.\n\n"
            f" $\\cot (90^\\circ-{x})=\\tan {x}={latex(nsimplify(tanx))}$.")
    
    
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

#[D10_C4_B1_10]-SA-M2. Cho sin (góc tù). Tính biểu thức chứa sin,cosx,tan
def yy3yy_L10_C4_B1_10():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos=sp.symbols("sinx cosx")
    chon=random.randint(1,2)

    if chon==1:
        while True:
            sinx=random.choice([1/random.randint(2,7),2/3,2/5,3/4,3/5,4/5,5/6])
            m=random.randint(1,5)
            n= random.choice([i for i in range(-4, 4) if i!=0])
            cosx=sqrt(1-sinx**2)
            f=m*sin+n*cos
            kq=m*sinx+n*cosx
            if kq>-8:
                break

        noi_dung = (
        f"Cho góc ${{{x}}}$ là góc nhọn và thỏa mãn $\\sin {x}={phan_so(sinx)}$."
        f" Tính giá trị biểu thức $P={latex(f)}$ (kết quả làm tròn đến hàng phần mười)"
        )
        noi_dung=noi_dung.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}")    


        dap_an=f"{round_half_up(kq,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"$\\cos {x}=\\sqrt{{1-{phan_so(sinx**2)}}}={latex(nsimplify(cosx))}$.\n\n"
        f"${latex(f)}={dap_an}$."
        )
    
    if chon==2:
        while True:
            sinx=random.choice([1/random.randint(2,7),2/3,2/5,3/4,3/5,4/5,5/6])
            m=random.randint(1,5)
            n= random.choice([i for i in range(-4, 4) if i!=0])

            cosx=-sqrt(1-sinx**2)            
            f=m*sin+n*cos
            kq=m*sinx+n*cosx
            if kq>-8:
                break

        noi_dung = (
        f"Cho góc ${{{x}}}$ là góc tù và thỏa mãn $\\sin {x}={phan_so(sinx)}$."
        f" Tính giá trị biểu thức $P={latex(f)}$ (kết quả làm tròn đến hàng phần mười)"
        )
        noi_dung=noi_dung.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}")    


        dap_an=f"{round_half_up(kq,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"$\\cos {x}=-\\sqrt{{1-{phan_so(sinx**2)}}}={latex(nsimplify(cosx))}$.\n\n"
        f"${latex(f)}={dap_an}$."
        )
    
    

    noi_dung_loigiai=noi_dung_loigiai.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}")  

        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B1_11]-SA-M2. Cho tan. Tính biểu thức chứa sin, cos
def yy3yy_L10_C4_B1_11():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan=sp.symbols("sinx cosx tanx")
    while True:
        a = random.choice([i for i in range(-5, 6) if i!=0])
        b = random.choice([i for i in range(-5, 6) if i!=0])
        tanx=a/b
        
        m,n,p,q=[random.choice([i for i in range(-5, 6) if i!=0]) for i in range(4)]
        if p*tanx+q==0:
            continue
        t=(m*tanx+n)/(p*tanx+q)

        if all([m*q-n*p!=0, t>-8]) :
            break

    f=(m*sin+n*cos)/(p*sin+q*cos)
    g=(m*tan+n)/(p*tan+q)

    noi_dung = (
    f"Cho góc ${{{x}}}$ thỏa mãn $\\tan {x} ={phan_so(tanx)}$. Tính giá trị biểu thức"
    f" $P={latex(f)}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(t,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$P={latex(f)}={latex(g)}={phan_so(t)}={dap_an}$."
    )

    noi_dung=noi_dung.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("tanx", f"\\tan {x}")  
    noi_dung_loigiai=noi_dung_loigiai.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("tanx", f"\\tan {x}")   
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B1_12]-SA-M2. Cho cotan. Tính biểu thức chứa sin, cos
def yy3yy_L10_C4_B1_12():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, cot=sp.symbols("sinx cosx cotx")
    while True:
        a = random.choice([i for i in range(-5, 6) if i!=0])
        b = random.choice([i for i in range(-5, 6) if i!=0])
        cotx=a/b
        
        m,n,p,q=[random.choice([i for i in range(-5, 6) if i!=0]) for i in range(4)]
        if p+q*cotx==0:
            continue
        t=(m+n*cotx)/(p+q*cotx)

        if all([m*q-n*p!=0, t>-8]) :
            break

    f=(m*sin+n*cos)/(p*sin+q*cos)
    g=(m+n*cot)/(p+q*cot)

    noi_dung = (
    f"Cho góc ${{{x}}}$ thỏa mãn $\\cot {x} ={phan_so(cotx)}$. Tính giá trị biểu thức"
    f" $P={latex(f)}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(t,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$P={latex(f)}={latex(g)}={phan_so(t)}={dap_an}$."
    )

    noi_dung=noi_dung.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("cotx", f"\\cot {x}")  
    noi_dung_loigiai=noi_dung_loigiai.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("cotx", f"\\cot {x}")     
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B1_13]-SA-M2. Cho cos. Tính biểu thức chứa tan,cot
def yy3yy_L10_C4_B1_13():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan, cot=sp.symbols("sinx cosx tanx cotx")
    while True:
        a = random.choice([i for i in range(-8, 8) if i!=0])
        b = random.choice([i for i in range(-8, 8) if i!=0])
        cosx=a/b
        if cosx<=-1 or cosx>=1:
            continue
        k=1/cosx**2-1

        m,n,p,q=[random.choice([i for i in range(-5, 6) if i!=0]) for i in range(4)]
        if p*k+q==0:
            continue

        t=(m*k+n)/(p*k+q)

        if all([m*q-n*p!=0, t>-8]) :
            break

    f=(m*tan+n*cot)/(p*tan+q*cot)
    g=(m*(1/cos**2-1)+n)/(p*(1/cos**2-1)+q)

    noi_dung = (
    f"Cho góc ${{{x}}}$ thỏa mãn $\\cos {x} ={phan_so(cosx)}$. Tính giá trị biểu thức"
    f" $P={latex(f)}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(t,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$P={latex(f)}={latex((m*tan**2+n)/(p*tan**2+q))}={latex(g)}={phan_so(t)}={dap_an}$."
    )

    noi_dung=noi_dung.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("tanx", f"\\tan {x}").replace("cotx", f"\\cot {x}")  
    noi_dung_loigiai=noi_dung_loigiai.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("tanx", f"\\tan {x}").replace("cotx", f"\\cot {x}")     
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B1_14]-SA-M2. Cho sin. Tính biểu thức chứa tan,cot
def yy3yy_L10_C4_B1_14():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan, cot=sp.symbols("sinx cosx tanx cotx")
    while True:
        a = random.choice([i for i in range(-8, 8) if i!=0])
        b = random.choice([i for i in range(-8, 8) if i!=0])
        cosx=a/b
        if cosx<=-1 or cosx>=1:
            continue
        k=1/cosx**2-1

        m,n,p,q=[random.choice([i for i in range(-5, 6) if i!=0]) for i in range(4)]
        if p*k+q==0:
            continue

        t=(m*k+n)/(p*k+q)

        if all([m*q-n*p!=0, t>-8]) :
            break

    f=(m*tan+n*cot)/(p*tan+q*cot)
    g=(m*(1/cos**2-1)+n)/(p*(1/cos**2-1)+q)
    sinx=sqrt(1-cosx**2)

    noi_dung = (
    f"Cho góc ${{{x}}}$ thỏa mãn $\\sin {x} ={latex(nsimplify(sinx))}$. Tính giá trị biểu thức"
    f" $P={latex(f)}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(t,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
        f"Ta có: $\\cos^2 {x}=1-\\sin^2 {x}={phan_so(cosx**2)}$.\n\n"
    f"$P={latex(f)}={latex((m*tan**2+n)/(p*tan**2+q))}={latex(g)}={phan_so(t)}={dap_an}$."
    )

    noi_dung=noi_dung.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("tanx", f"\\tan {x}").replace("cotx", f"\\cot {x}")  
    noi_dung_loigiai=noi_dung_loigiai.replace("sinx", f"\\sin {x}").replace("cosx", f"\\cos {x}").replace("tanx", f"\\tan {x}").replace("cotx", f"\\cot {x}")     
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B1_15]-M2. Tìm khẳng định đúng về công thức lượng giác
def yy3yy_L10_C4_B1_15():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan, cot=sp.symbols("sinx cosx tanx cotx")
    noi_dung=(
    f"Tìm mệnh đề đúng trong các mệnh đề sau"
    )
    
    kq=random.choice([
        f"\\sin (90^\\circ-{x})=\\cos {x}",
        f"\\cos (90^\\circ-{x})=\\sin {x}",
        f"\\tan (90^\\circ-{x})=\\cot {x}",
        f"\\cot (90^\\circ-{x})=\\tan {x}",
        f"\\sin (180^\\circ-{x})=\\sin {x}",
        f"\\cos (180^\\circ-{x})=-\\cos {x}",
        f"\\tan (180^\\circ-{x})=-\\tan {x} ({x}\\ne 90^\\circ)",
        f"\\cot (180^\\circ-{x})=-\\cot {x}, (0^\\circ < {x} < 180^\\circ)",
        f"\\sin^2 {x} + \\cos^2{x}=1",
        f"1+\\tan^2 {x}=\\dfrac{{1}}{{\\cos^2 {x}}}, ({x}\\ne 90^\\circ)",
        f"1+\\cot^2 {x}=\\dfrac{{1}}{{\\sin^2 {x}}}, (0^\\circ < {x} < 180^\\circ)",
        ])
    kq_false=[
    f"\\sin (90^\\circ-{x})=\\sin {x}",
    f"\\cos (90^\\circ-{x})=\\cos {x}",
    f"\\sin (180^\\circ-{x})=-\\sin {x}",
    f"\\cos (180^\\circ-{x})=\\cos {x}",
    f"\\tan (180^\\circ-{x})=\\tan {x} ({x}\\ne 90^\\circ)",
    f"\\cot (180^\\circ-{x})=\\cot {x}, (0^\\circ < {x} < 180^\\circ)",
    f"\\sin ({random.randint(2,8)*10}^\\circ-{x})=\\cos {x}",
    f"\\cos({random.randint(2,8)*10}^\\circ-{x})=\\sin {x}",
    f"\\sin^2 {x} - \\cos^2{x}=1",]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${kq}$ là khẳng định đúng."
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

#[D10_C4_B1_16]-TF-M2. Cho sinx (0<x<90). Xét Đ-S: cosx, tanx, cotx, GTLG của góc 90-x
def yy3yy_L10_C4_B1_16():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan, cot=sp.symbols("sinx cosx tanx cotx")
    while True:
        a = random.choice([i for i in range(1, 9) if i!=0])
        b = random.choice([i for i in range(1, 9) if i!=0])
        sinx=a/b
        if -1<sinx<1:
            break

    noi_dung = (
    f"Cho góc ${{{x}}} (0^\\circ < {x} <90^\\circ)$ thỏa mãn $\\sin {x}={phan_so(sinx)}$ . Xét tính đúng-sai của các khẳng định sau:"
    )    

    cosx=sqrt(1-sinx**2)
    
    kq1_T=f"* $\\cos {x}={latex(nsimplify(cosx))}$" 
    kq1_F=f" $\\cos {x}={latex(nsimplify(-cosx))}$"
    
    HDG=f"$\\cos {x}=\\sqrt{{1-\\sin^2 {x}}}= \\sqrt{{1-{phan_so(sinx**2)}}}={latex(nsimplify(cosx))}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    tanx=sinx/cosx

    kq2_T=f"* $\\tan {x}= {latex(nsimplify(tanx))}$"
    kq2_F=f"$\\tan {x}= {latex(nsimplify(-tanx))}$"
    
    HDG=f"$\\tan {x}={phan_so(sinx)}:{latex(nsimplify(cosx))}={latex(nsimplify(tanx))}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cotx=cosx/sinx
    kq3_T=f"* $\\cot {x}= {latex(nsimplify(cotx))}$" 
    kq3_F=f"$\\cot {x}= {latex(nsimplify(-cotx))}$"
    
    HDG=f"$\\cot {x}={latex(nsimplify(cosx))}:{phan_so(sinx)}={latex(nsimplify(cotx))}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,4)
    
    if chon==1:
        kq4_T=f"* $\\sin(90^\\circ - {x})={latex(nsimplify(cosx))}$"
        kq4_F=f"$\\sin(90^\\circ - {x})={latex(nsimplify(-cosx))}$" 
        
        HDG=f"$\\sin(90^\\circ - {x})=\\cos {x}={latex(nsimplify(cosx))}$."
    
    if chon==2:
        kq4_T=f"* $\\cos(90^\\circ - {x})={phan_so(sinx)}$"
        kq4_F=f"$\\cos(90^\\circ - {x})={phan_so(-sinx)}$" 
        
        HDG=f"$\\cos(90^\\circ - {x})=\\sin {x}={phan_so(sinx)}$."

    if chon==3:
        kq4_T=f"* $\\tan(90^\\circ - {x})={latex(nsimplify(cotx))}$"
        kq4_F=f"$\\tan(90^\\circ - {x})={latex(nsimplify(-cotx))}$" 
        
        HDG=f"$\\tan(90^\\circ - {x})=\\cot {x}={latex(nsimplify(cotx))}$."

    if chon==4:
        kq4_T=f"* $\\cot(90^\\circ - {x})={latex(nsimplify(tanx))}$"
        kq4_F=f"$\\cot(90^\\circ - {x})={latex(nsimplify(-tanx))}$" 
        
        HDG=f"$\\cot(90^\\circ - {x})=\\tan {x}={latex(nsimplify(tanx))}$."
    

    
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

#[D10_C4_B1_17]-TF-M2. Cho sinx (0<x<90). Xét Đ-S: cosx, tanx, cotx, GTLG của góc 180-x
def yy3yy_L10_C4_B1_17():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan, cot=sp.symbols("sinx cosx tanx cotx")
    while True:
        a = random.choice([i for i in range(1, 9) if i!=0])
        b = random.choice([i for i in range(1, 9) if i!=0])
        sinx=a/b
        if -1<sinx<1:
            break

    noi_dung = (
    f"Cho góc ${{{x}}} (0^\\circ < {x} <90^\\circ)$ thỏa mãn $\\sin {x}={phan_so(sinx)}$ . Xét tính đúng-sai của các khẳng định sau:"
    )    

    cosx=sqrt(1-sinx**2)
    
    kq1_T=f"* $\\cos {x}={latex(nsimplify(cosx))}$" 
    kq1_F=f" $\\cos {x}={latex(nsimplify(-cosx))}$"
    
    HDG=f"$\\cos {x}=\\sqrt{{1-\\sin^2 {x}}}= \\sqrt{{1-{phan_so(sinx**2)}}}={latex(nsimplify(cosx))}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    tanx=sinx/cosx

    kq2_T=f"* $\\tan {x}= {latex(nsimplify(tanx))}$"
    kq2_F=f"$\\tan {x}= {latex(nsimplify(-tanx))}$"
    
    HDG=f"$\\tan {x}={phan_so(sinx)}:{latex(nsimplify(cosx))}={latex(nsimplify(tanx))}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cotx=cosx/sinx
    kq3_T=f"* $\\cot {x}= {latex(nsimplify(cotx))}$" 
    kq3_F=f"$\\cot {x}= {latex(nsimplify(-cotx))}$"
    
    HDG=f"$\\cot {x}={latex(nsimplify(cosx))}:{phan_so(sinx)}={latex(nsimplify(cotx))}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,4)
    
    if chon==1:
        kq4_T=f"* $\\sin(180^\\circ - {x})={phan_so(sinx)}$"
        kq4_F=f"$\\sin(180^\\circ - {x})={phan_so(-sinx)}$" 
        
        HDG=f"$\\sin(180^\\circ - {x})=\\sin {x}={phan_so(sinx)}$."
    
    if chon==2:
        kq4_T=f"* $\\cos(180^\\circ - {x})={latex(nsimplify(-cosx))}$"
        kq4_F=f"$\\cos(180^\\circ - {x})={latex(nsimplify(cosx))}$" 
        
        HDG=f"$\\cos(180^\\circ - {x})=-\\cos {x}={latex(nsimplify(-cosx))}$."

    if chon==3:
        kq4_T=f"* $\\tan(180^\\circ - {x})={latex(nsimplify(-tanx))}$"
        kq4_F=f"$\\tan(180^\\circ - {x})={latex(nsimplify(tanx))}$" 
        
        HDG=f"$\\tan(180^\\circ - {x})=-\\tan {x}={latex(nsimplify(-tanx))}$."

    if chon==4:
        kq4_T=f"* $\\cot(180^\\circ - {x})={latex(nsimplify(-cotx))}$"
        kq4_F=f"$\\cot(180^\\circ - {x})={latex(nsimplify(cotx))}$" 
        
        HDG=f"$\\cot(180^\\circ - {x})=-\\cot {x}={latex(nsimplify(-cotx))}$."
    

    
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

#[D10_C4_B1_18]-TF-M2. Cho sinx (90<x<180). Xét Đ-S: cosx, tanx, cotx, GTLG của góc 90-x
def yy3yy_L10_C4_B1_18():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan, cot=sp.symbols("sinx cosx tanx cotx")
    while True:
        a = random.choice([i for i in range(1, 9) if i!=0])
        b = random.choice([i for i in range(1, 9) if i!=0])
        sinx=a/b
        if -1<sinx<1:
            break

    noi_dung = (
    f"Cho góc ${{{x}}} (90^\\circ < {x} <180^\\circ)$ thỏa mãn $\\sin {x}={phan_so(sinx)}$ . Xét tính đúng-sai của các khẳng định sau:"
    )    

    cosx=-sqrt(1-sinx**2)
    
    kq1_T=f"* $\\cos {x}={latex(nsimplify(cosx))}$" 
    kq1_F=f" $\\cos {x}={latex(nsimplify(-cosx))}$"
    
    HDG=f"$\\cos {x}=-\\sqrt{{1-\\sin^2 {x}}}=-\\sqrt{{1-{phan_so(sinx**2)}}}={latex(nsimplify(cosx))}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    tanx=sinx/cosx

    kq2_T=f"* $\\tan {x}= {latex(nsimplify(tanx))}$"
    kq2_F=f"$\\tan {x}= {latex(nsimplify(-tanx))}$"
    
    HDG=f"$\\tan {x}={phan_so(sinx)}:{latex(nsimplify(cosx))}={latex(nsimplify(tanx))}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cotx=cosx/sinx
    kq3_T=f"* $\\cot {x}= {latex(nsimplify(cotx))}$" 
    kq3_F=f"$\\cot {x}= {latex(nsimplify(-cotx))}$"
    
    HDG=f"$\\cot {x}={latex(nsimplify(cosx))}:{phan_so(sinx)}={latex(nsimplify(cotx))}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,4)
    
    if chon==1:
        kq4_T=f"* $\\sin(90^\\circ - {x})={latex(nsimplify(cosx))}$"
        kq4_F=f"$\\sin(90^\\circ - {x})={latex(nsimplify(-cosx))}$" 
        
        HDG=f"$\\sin(90^\\circ - {x})=\\cos {x}={latex(nsimplify(cosx))}$."
    
    if chon==2:
        kq4_T=f"* $\\cos(90^\\circ - {x})={phan_so(sinx)}$"
        kq4_F=f"$\\cos(90^\\circ - {x})={phan_so(-sinx)}$" 
        
        HDG=f"$\\cos(90^\\circ - {x})=\\sin {x}={phan_so(sinx)}$."

    if chon==3:
        kq4_T=f"* $\\tan(90^\\circ - {x})={latex(nsimplify(cotx))}$"
        kq4_F=f"$\\tan(90^\\circ - {x})={latex(nsimplify(-cotx))}$" 
        
        HDG=f"$\\tan(90^\\circ - {x})=\\cot {x}={latex(nsimplify(cotx))}$."

    if chon==4:
        kq4_T=f"* $\\cot(90^\\circ - {x})={latex(nsimplify(tanx))}$"
        kq4_F=f"$\\cot(90^\\circ - {x})={latex(nsimplify(-tanx))}$" 
        
        HDG=f"$\\cot(90^\\circ - {x})=\\tan {x}={latex(nsimplify(tanx))}$."
    

    
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

#[D10_C4_B1_19]-TF-M2. Cho sinx (90<x<180). Xét Đ-S: cosx, tanx, cotx, GTLG của góc 180-x
def yy3yy_L10_C4_B1_19():
    x=random.choice(["x", "a", "\\alpha", "\\beta"])
    sin, cos, tan, cot=sp.symbols("sinx cosx tanx cotx")
    while True:
        a = random.choice([i for i in range(1, 9) if i!=0])
        b = random.choice([i for i in range(1, 9) if i!=0])
        sinx=a/b
        if -1<sinx<1:
            break

    noi_dung = (
    f"Cho góc ${{{x}}} (90^\\circ < {x} <180^\\circ)$ thỏa mãn $\\sin {x}={phan_so(sinx)}$ . Xét tính đúng-sai của các khẳng định sau:"
    )    

    cosx=-sqrt(1-sinx**2)
    
    kq1_T=f"* $\\cos {x}={latex(nsimplify(cosx))}$" 
    kq1_F=f" $\\cos {x}={latex(nsimplify(-cosx))}$"
    
    HDG=f"$\\cos {x}=-\\sqrt{{1-\\sin^2 {x}}}= -\\sqrt{{1-{phan_so(sinx**2)}}}={latex(nsimplify(cosx))}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    tanx=sinx/cosx

    kq2_T=f"* $\\tan {x}= {latex(nsimplify(tanx))}$"
    kq2_F=f"$\\tan {x}= {latex(nsimplify(-tanx))}$"
    
    HDG=f"$\\tan {x}={phan_so(sinx)}:{latex(nsimplify(cosx))}={latex(nsimplify(tanx))}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cotx=cosx/sinx
    kq3_T=f"* $\\cot {x}= {latex(nsimplify(cotx))}$" 
    kq3_F=f"$\\cot {x}= {latex(nsimplify(-cotx))}$"
    
    HDG=f"$\\cot {x}={latex(nsimplify(cosx))}:{phan_so(sinx)}={latex(nsimplify(cotx))}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,4)
    
    if chon==1:
        kq4_T=f"* $\\sin(180^\\circ - {x})={phan_so(sinx)}$"
        kq4_F=f"$\\sin(180^\\circ - {x})={phan_so(-sinx)}$" 
        
        HDG=f"$\\sin(180^\\circ - {x})=\\sin {x}={phan_so(sinx)}$."
    
    if chon==2:
        kq4_T=f"* $\\cos(180^\\circ - {x})={latex(nsimplify(-cosx))}$"
        kq4_F=f"$\\cos(180^\\circ - {x})={latex(nsimplify(cosx))}$" 
        
        HDG=f"$\\cos(180^\\circ - {x})=-\\cos {x}={latex(nsimplify(-cosx))}$."

    if chon==3:
        kq4_T=f"* $\\tan(180^\\circ - {x})={latex(nsimplify(-tanx))}$"
        kq4_F=f"$\\tan(180^\\circ - {x})={latex(nsimplify(tanx))}$" 
        
        HDG=f"$\\tan(180^\\circ - {x})=-\\tan {x}={latex(nsimplify(-tanx))}$."

    if chon==4:
        kq4_T=f"* $\\cot(180^\\circ - {x})={latex(nsimplify(-cotx))}$"
        kq4_F=f"$\\cot(180^\\circ - {x})={latex(nsimplify(cotx))}$" 
        
        HDG=f"$\\cot(180^\\circ - {x})=-\\cot {x}={latex(nsimplify(-cotx))}$."
    

    
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

#[D10_C4_B1_20]-M1. Tìm đẳng thức đúng dạng (sinx=a, cosx=b,tanx=c, cotx=d)
def yy3yy_L10_C4_B1_20():
    noi_dung=(
    f"Khẳng định nào sau đây là khẳng định đúng?"
    )
    

    kq=random.choice([
        f"$\\sin 0^\\circ =0$",
        f"$\\sin 30^\\circ ={phan_so(1/2)}$",
        f"$\\sin 45^\\circ ={latex(sqrt(2)/2)}$",
        f"$\\sin 60^\\circ ={latex(sqrt(3)/2)}$",
        f"$\\sin 90^\\circ =1$",
        f"$\\sin 120^\\circ ={latex(sqrt(3)/2)}$",
        f"$\\sin 150^\\circ ={phan_so(1/2)}$",
        f"$\\sin 180^\\circ =0$",
        f"$\\cos 0^\\circ =1$",
        f"$\\cos 30^\\circ ={latex(sqrt(3)/2)}$",
        f"$\\cos 45^\\circ ={latex(sqrt(2)/2)}$",
        f"$\\cos 60^\\circ ={phan_so(1/2)}$",
        f"$\\cos 90^\\circ =0$",
        f"$\\cos 120^\\circ =-{phan_so(1/2)}$",
        f"$\\cos 150^\\circ =-{latex(sqrt(3)/2)}$",
        f"$\\cos 180^\\circ =-$",
        f"$\\tan 0^\\circ =0$",
        f"$\\tan 0^\\circ = 0$",
        f"$\\tan 30^\\circ = {latex(sqrt(3)/3)}$",
        f"$\\tan 45^\\circ = 1$",
        f"$\\tan 60^\\circ = {latex(sqrt(3))}$",        
        f"$\\tan 120^\\circ = -{latex(sqrt(3))}$",
        f"$\\tan 135^\\circ = -1$",
        f"$\\tan 150^\\circ = -{latex(sqrt(3)/3)}$",
        f"$\\tan 180^\\circ = 0$",
        f"$\\cot 30^\\circ = {latex(sqrt(3))}$",
        f"$\\cot 45^\\circ = 1$",
        f"$\\cot 60^\\circ = {latex(sqrt(3)/3)}$",
        f"$\\cot 90^\\circ = 0$",
        f"$\\cot 120^\\circ = -{latex(sqrt(3)/3)}$",
        f"$\\cot 135^\\circ = -1$",
        f"$\\cot 150^\\circ = -{latex(sqrt(3))}$",])
    kq_false=[f"$\\sin 0^\\circ = 1$",                          
    f"$\\sin 15^\\circ = {phan_so(1/2)}$",            
    f"$\\sin 30^\\circ = {latex(sqrt(2)/2)}$",    
    f"$\\sin 45^\\circ = {latex(sqrt(3)/2)}$",
    f"$\\sin 60^\\circ = 1$",
    f"$\\sin 75^\\circ = 0$",
    f"$\\sin 90^\\circ = 0$",
    f"$\\sin 105^\\circ = -{phan_so(1/2)}$",
    f"$\\sin 120^\\circ = -{latex(sqrt(3)/2)}$",
    f"$\\sin 135^\\circ = -{latex(sqrt(2)/2)}$",
    f"$\\sin 150^\\circ = -{phan_so(1/2)}$",
    f"$\\sin 165^\\circ = -1$",
    f"$\\sin 180^\\circ = 1$",
    f"$\\cos 0^\\circ = 0$",                        
    f"$\\cos 15^\\circ = {phan_so(1/2)}$",
    f"$\\cos 30^\\circ = 1$",
    f"$\\cos 45^\\circ = {phan_so(1/2)}$",
    f"$\\cos 60^\\circ = {latex(sqrt(2)/2)}$",
    f"$\\cos 75^\\circ = -1$",
    f"$\\cos 90^\\circ = 1$",
    f"$\\cos 105^\\circ = {latex(sqrt(3)/2)}$",
    f"$\\cos 120^\\circ = {latex(sqrt(2)/2)}$",
    f"$\\cos 135^\\circ = {phan_so(1/2)}$",
    f"$\\cos 150^\\circ = {latex(sqrt(3)/2)}$",
    f"$\\cos 165^\\circ = {phan_so(1/2)}$",
    f"$\\cos 180^\\circ = 0$",
    f"$\\tan 0^\\circ = 1$",                          
    f"$\\tan 15^\\circ = {latex(sqrt(3)/3)}$",        
    f"$\\tan 30^\\circ = 1$",
    f"$\\tan 45^\\circ = 0$",
    f"$\\tan 60^\\circ = {phan_so(1/3)}$",
    f"$\\tan 75^\\circ = -1$",
    f"$\\tan 90^\\circ = 0$",                        
    f"$\\tan 105^\\circ = 1$",
    f"$\\tan 120^\\circ = 0$",
    f"$\\tan 135^\\circ = 1$",
    f"$\\tan 150^\\circ = {latex(sqrt(3)/3)}$",
    f"$\\tan 165^\\circ = 1$",
    f"$\\tan 180^\\circ = 1$",]
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

#[D10_C4_B1_21]-M1. Cho 2 góc bù nhau. Tìm khẳng định sai.
def yy3yy_L10_C4_B1_21():
    a,b= random.sample(["\\alpha", "\\beta", "\\gamma", "a","b", "x","y"],2)
    noi_dung=(
    f"Biết rằng ${{{a},{b}}}$ là hai góc bù nhau. Trong các khẳng định sau, khẳng định nào là khẳng định sai (giả thiết rằng các biểu thức đều có nghĩa)?"
    )
    

    kq=random.choice([
    f"$\\sin {a} = -\\sin {b}$",
    f"$\\sin {a} = \\cos {b}$",        
    f"$\\cos {a} = \\sin {b}$",        
    f"$\\tan {a} = \\tan {b}$",         
    f"$\\cot {a} = \\cot {b}$",       
    f"$\\tan {a} = \\cot {b}$",        
    f"$\\cot {a} = \\tan {b}$",        
    f"$\\sin {a} = -\\cos {b}$",       
    f"$\\cos {a} = -\\sin {b}$",       
    f"$\\tan {a} = \\sin {b}$",      
    f"$\\cot {a} = \\cos {b}$",      ])

    kq_false=[f"$\\sin {a} = \\sin {b}$",
    f"$\\cos {a} = -\\cos {b}$",
    f"$\\cos {a} + \\cos {b}=0$",
    f"$\\sin {a} + \\sin {b}=2\\sin {a}$",
    f"$\\sin {a} + \\sin {b}=2\\sin {b}$",
    f"$\\tan {a} = -\\tan {b}$",
    f"$\\cot {a} = -\\cot {b}$",
    f"$\\sin^2 {a} + \\sin^2 {b} = 2\\sin^2 {a}$",
    f"$\\cos^2 {a} + \\cos^2 {b} = 2\\cos^2 {a}$",]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"{kq} là khẳng định sai. "
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

#[D10_C4_B1_22]-M1. Cho 2 góc phụ nhau. Tìm khẳng định sai.
def yy3yy_L10_C4_B1_22():
    a,b= random.sample(["\\alpha", "\\beta", "\\gamma", "a","b", "x","y"],2)
    noi_dung=(
    f"Biết rằng ${{{a},{b}}}$ là hai góc phụ nhau. Trong các khẳng định sau, khẳng định nào là khẳng định sai (giả thiết rằng các biểu thức đều có nghĩa)?"
    )
    
    kq=random.choice([
    f"$\\sin {a} = \\sin {b}$",           # sai
    f"$\\cos {a} = \\cos {b}$",           # sai
    f"$\\tan {a} = \\tan {b}$",           # sai
    f"$\\cot {a} = \\cot {b}$",           # sai
    f"$\\sin {a} = -\\cos {b}$",          # sai
    f"$\\cos {a} = -\\sin {b}$",          # sai
    f"$\\tan {a} = -\\cot {b}$",          # sai
    f"$\\cot {a} = -\\tan {b}$",          # sai
    f"$\\sin^2 {a} + \\cos^2 {b} = 2$",   # sai
    f"$\\tan {a} \\cdot \\tan {b} = 0$",       ])

    kq_false=[f"$\\sin {a} = \\cos {b}$",
    f"$\\cos {a} = \\sin {b}$",
    f"$\\tan {a} = \\cot {b}$",
    f"$\\cot {a} = \\tan {b}$",
    f"$\\sin {a} \\cdot \\sin {b} = \\sin {a} \\cos {a}$",
    f"$\\cos {a} \\cdot \\cos {b} = \\sin {a} \\cos {a}$",
    f"$\\sin^2 {a} + \\sin^2 {b} = 1$",
    f"$\\cos^2 {a} + \\cos^2 {b} = 1$",
    f"$\\tan {a} \\cdot \\tan {b} = 1$",
    f"$\\cot {a} \\cdot \\cot {b} = 1$",]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"{kq} là khẳng định sai. "
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

#[D10_C4_B1_23]-M1. Tính giá trị lượng giác của một góc.
def yy3yy_L10_C4_B1_23():
    list_x=[pi/3,pi/6,2*pi/3,3*pi/4]
    x=random.choice(list_x) 

    list_ham=[sin(x), cos(x), tan(x), cot(x)]
    ham =random.choice(list_ham)

    list_hamkhac = [t for t in list_ham if t != ham]
    list_hamkhac.append (random.randint(-5,5))
    list_hamkhac.append (sqrt(2))  
    if ham == list_ham[0]:
        ten_ham = "sin"
    if ham == list_ham[1]:
        ten_ham = "cos"
    if ham == list_ham[2]:
        ten_ham = "tan"
    if ham == list_ham[3]:
        ten_ham = "cot"
    #Tạo các phương án
    pa_A= f"*${{ {latex((ham))} }}$"
    pa_B= f"${{ {latex((list_hamkhac[0]))} }}$"
    pa_C= f"${{ {latex((list_hamkhac[1]))} }}$"
    pa_D= f"${{ {latex((list_hamkhac[2]))} }}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính $\\{ten_ham}{latex(x*180/pi)}^\\circ$."
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
    f"\\shortans[4]{{}}\n\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an







#BÀI 2 - ĐỊNH LÍ COSIN VÀ ĐỊNH LÍ SIN

#[D10_C4_B2_01]. Tính diện tích biết 2 cạnh và góc xen giữa
def yy3yy_L10_C4_B2_01():
    a = random.randint(3,20)
    b = random.randint(5,30)
    C_degree=random.randint(10,170)
    if C_degree==90: C_degree=random.randint(10,80)    
    C= math.radians(C_degree)
    ten_goc =random.choice(["A", "B", "C"])
    if ten_goc == "A":
        ten_canh1="AC"
        ten_canh2="AB"
    elif ten_goc == "B":
        ten_canh1="BC"
        ten_canh2="BA"
    else:
        ten_canh1="CB"
        ten_canh2="CA" 
    #Tìm công thức nghiệm và nghiệm ảo
    
    kq=1/2*a*b*sin(C)
    kq2=abs(1/3*a*b*cos(C))
    kq3=1/2*a*b
    kq4=2*a*b*sin(C)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A=f"*${{{round(kq,2):.2f}}}cm^{{2}}$".replace(".",",").replace(",00","")
    pa_B=f"${{{round(kq2,2):.2f}}}cm^{{2}}$".replace(".",",").replace(",00","")
    pa_C=f"${{{round(kq3,2):.2f}}}cm^{{2}}$".replace(".",",").replace(",00","")
    pa_D=f"${{{round(kq4,2):.2f}}}cm^{{2}}$".replace(".",",").replace(",00","")


    noi_dung=(f"Cho tam giác ${{ABC}}$ có ${ten_canh1}={a}cm;{ten_canh2}={b}cm;\\widehat{{{ten_goc}}}={C_degree}^\\circ$. Tính diện tích tam giác ${{ABC}}$"
    f" (kết quả làm tròn đến hàng phần trăm)."
    )#Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    st_kq=f"{round(kq,2):.2f}".replace(".",",")



    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
    noi_dung_loigiai=f"$S=\\dfrac{{1}}{{2}}.{a}.{b}.\\sin {C_degree}^\\circ={st_kq}cm^{{2}}$."          
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

#[D10_C4_B2_02]. Cho 2 cạnh và góc xen giữa. Tính độ dài cạnh thứ 3.
def yy3yy_L10_C4_B2_02():
    a = random.randint(3,20)
    b = random.randint(5,30)
    C_degree=random.randint(10,170)
    C= math.radians(C_degree)
    ten_goc =random.choice(["A", "B", "C"])
    if ten_goc == "A":
        ten_canh1="AB"
        ten_canh2="AC"
        ten_canh3="BC"
    elif ten_goc == "B":
        ten_canh1="BC"
        ten_canh2="AB"
        ten_canh3="AC"
    else:
        ten_canh1="AC"
        ten_canh2="BC"  
        ten_canh3="AB"      
    #Tìm công thức nghiệm và nghiệm ảo 
    kq=sqrt(a**2 + b**2 -2*a*b*cos(C)) 
    kq2=sqrt(a**2 + b**2 -2*a*b*sin(C))
    kq3=sqrt(a**2 + b**2)
    kq4=1/2*a*b*sin(C)
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
    #Tạo các phương án
    pa_A=f"*${{{kq:.2f}}}$cm".replace(".",",")
    pa_B=f"${{{kq2:.2f}}}$cm".replace(".",",")
    pa_C=f"${{{kq3:.2f}}}$cm".replace(".",",")
    pa_D=f"${{{kq4:.2f}}}$cm".replace(".",",")

    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho tam giác ${{ABC}}$ có ${ten_canh1}={a}cm;{ten_canh2}={b}cm;\\widehat{{{ten_goc}}}={C_degree}^\\circ$. Tính độ dài cạnh ${{{ten_canh3}}}$."
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  

    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
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

#[D10_C4_B2_03]. Tính số đo một góc biết độ dài 3 cạnh
def yy3yy_L10_C4_B2_03():

    a = random.randint(3,7)
    b = random.randint(8,20)
    c = my_module.canh_thu_3_tg(a,b)

    while any([a==b,b==c,c==a]):
        a = random.randint(3,7)
        b = random.randint(8,20)
        c = my_module.canh_thu_3_tg(a,b)

    alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    gamma = 180 - alpha - beta
    ten_goc =random.choice(["A", "B", "C"])
    if ten_goc == "A":
        kq=alpha
        kq2=beta
        kq3=gamma
    elif ten_goc == "B":
        kq=beta
        kq2=alpha
        kq3=gamma
    else:
        kq=gamma
        kq2=alpha
        kq3=beta
    kq4=random.uniform(10,90)    
    #Tìm công thức nghiệm và nghiệm ảo 

    #Tạo các phương án
    pa_A=f"*${{{kq:.2f}}}^\\circ$".replace(".",",")
    pa_B=f"${{{kq2:.2f}}}^\\circ$".replace(".",",")
    pa_C=f"${{{kq3:.2f}}}^\\circ$".replace(".",",")
    pa_D=f"${{{kq4:.2f}}}^\\circ$".replace(".",",")
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho tam giác ${{ABC}}$ có $BC={a},AC={b},AB={c}$. Tính số đo góc $\\widehat{{{ten_goc}}}$."
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  

    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
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

#[D10_C4_B2_04]. Cho tam giác có một cạnh và góc đối diện. Tính bán kính đường tròn ngoại tiếp.
def yy3yy_L10_C4_B2_04():
    a = random.randint(2,12)
    while True:
        C_degree=random.randint(10,170)
        if all([C_degree!=90, C_degree!=45, C_degree!=135]):
            break
    C_radian= math.radians(C_degree)
    ten_goc =random.choice(["A", "B", "C"])
    if ten_goc == "A":
        ten_canh = "BC"
    elif ten_goc == "B":
        ten_canh = "AC"
    else:
        ten_canh = "AB"
    kq=a/(2*sin(C_radian))
    kq2=a/sin(C_radian)
    kq3=a/(2*abs(cos(C_radian)))
    kq4=a/(3*sin(C_radian))
    #Tìm công thức nghiệm và nghiệm ảo 

    #Tạo các phương án
    pa_A=f"*${{{kq:.2f}}}$".replace(".",",")
    pa_B=f"${{{kq2:.2f}}}$".replace(".",",")
    pa_C=f"${{{kq3:.2f}}}$".replace(".",",")
    pa_D=f"${{{kq4:.2f}}}$".replace(".",",")
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= (f"Cho tam giác ${{ABC}}$ có $\\widehat{{{ten_goc}}}={C_degree}^\\circ$ và độ dài cạnh ${{{ten_canh}}}$ bằng ${{{a}}}$."
    f" Tính bán kính ${{R}}$ của đường tròn ngoại tiếp tam giác ${{ABC}}$ (kết quả làm tròn đến hàng phần trăm).")
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  

    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
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

#[D10_C4_B2_05]. Cho tam giác có độ dài 3 cạnh. Tính diện tích tam giác.
def yy3yy_L10_C4_B2_05():
    a = random.randint(3,15)
    b = random.randint(8,20)
    c = random.randint(abs(a - b) + 1, a + b - 1)   
    kq=latex(my_module.rutgon_can(sqrt(a+b+c)*sqrt(b+c-a)*sqrt(a+b-c)*sqrt(a+c-b)/4))
    kq2=latex(my_module.rutgon_can(sqrt(a+b+c)*sqrt(b+c-a)*sqrt(a+b-c)*sqrt(a+c-b)/2))
    kq3=latex(my_module.rutgon_can(sqrt(a+b+c)*sqrt(b+c-a)*sqrt(a+b-c)*sqrt(a+c-b)))
    kq4=latex(my_module.rutgon_can(sqrt(a+b+c)*sqrt(b+c-a)*sqrt(a+b-c)*sqrt(a+c-b)/6))

    #Tạo các phương án
    pa_A=f"*${{{kq}}}$"
    pa_B=f"${{{kq2}}}$"
    pa_C=f"${{{kq3}}}$"
    pa_D=f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho tam giác ${{ABC}}$ có $BC={a},AC={b},AB={c}$. Tính diện tích tam giác ${{ABC}}$." 
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  

    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
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

#[D10_C4_B2_06]-TF-M2. Cho a,b và góc C. Xét Đ-S: cạnh C, cos A, góc B, diện tích
def yy3yy_L10_C4_B2_06():
    a=["a","b","c"]
    b=["b","c","a"]
    c=["c","a","b"]    
    A=["A","B","C"]
    B=["B","C","A"]
    C=["C","A","B"]
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_a=random.randint(1,7)
    l_b=random.randint(1,8)
    goc_C_degree=random.randint(10,130)
    goc_C= math.radians(goc_C_degree)

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},\\widehat{{{C}}}={goc_C_degree}^\\circ$. Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần trăm). "        
    debai_word= f"{noi_dung}\n"

    S=f"{1/2*l_a*l_b*sin(goc_C):.2f}".replace(".",",")
    S_false=f"{2*l_a*l_b*sin(goc_C):.2f}".replace(".",",")

    kq1_T=f"* Diện tích tam giác là $S = {S}$"
    kq1_F=f"Diện tích tam giác là $S = {S_false}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$S={phan_so(1/2)}.{l_a}.{l_b}.\\sin {goc_C_degree}^\\circ = {S}.$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    l_c=f"{sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)):.2f}".replace(".",",")
    l_c_false=f"{sqrt(l_a**2+l_b**2-l_a*l_b*cos(goc_C)):.2f}".replace(".",",")

    kq2_T=f"*${c}={l_c}$"
    kq2_F=f"${c}= {l_c_false}$"
    kq2=random.choice([kq2_T, kq2_F])

    l_c_sq=f"{sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)):.2f}".replace(".",",")

    HDG=f"${c}^2={l_a}^2+{l_b}^2-2.{l_a}.{l_b}.\\cos {{{goc_C_degree}}}^\\circ={l_c_sq} \\Rightarrow  {c}= {l_c}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #kq3
    l_c=sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C))
    cosA=f"{(l_b**2+l_c**2-l_a**2)/(2*l_b*l_c):.2f}".replace(".",",")
    cosA_false=f"{(l_b**2+l_c**2-l_a**2)/(4*l_b*l_c):.2f}".replace(".",",")

    kq3_T=f"*$\\cos {A}={cosA}$" 
    kq3_F=f"$\\cos {A}={cosA_false}$ "
    kq3=random.choice([kq3_T, kq3_F])
   
    l_c=f"{sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)):.2f}".replace(".",",")  
    HDG=f"$\\cos {A}=\\dfrac{{{l_b}^2+{l_c}^2-{l_a}^2 }}{{2.{l_b}.{l_c}}}={cosA}$.\n"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #kq4
    l_c=sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C))
    cosB=(l_a**2+l_c**2-l_b**2)/(2*l_a*l_c)
    goc_B=f"{math.degrees(acos(cosB)):.2f}".replace(".",",")

    cosB_false=(l_a**2+l_c**2-l_b**2)/(4*l_a*l_c)
    goc_B_false=f"{math.degrees(acos(cosB_false)):.2f}".replace(".",",")

    kq4_T=f"*$\\widehat{{{B}}}={goc_B}^\\circ$"
    kq4_F=f"$\\widehat{{{B}}}={goc_B_false}^\\circ$ " 
    kq4=random.choice([kq4_T, kq4_F])

    l_c=f"{sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)):.2f}".replace(".",",")
    HDG=f"$\\cos {B}=\\dfrac{{{l_a}^2+{l_c}^2-{l_a}^2}}{{2.{l_a}.{l_c}}}={cosB:.3f}\\Rightarrow \\widehat{{{B}}}={goc_B}^\\circ$."
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

#[D10_C4_B2_07]-TF-M2. Cho BC,AC và góc C. Xét Đ-S: cạnh AB, cos A, góc B, diện tích
def yy3yy_L10_C4_B2_07():
    a=["BC","AC","AB"]
    b=["AC","AB","BC"]
    c=["AB","BC","AC"]    
    A=["A","B","C"]
    B=["B","C","A"]
    C=["C","A","B"]
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_a=random.randint(1,7)
    l_b=random.randint(1,8)
    goc_C_degree=random.randint(10,130)
    goc_C= math.radians(goc_C_degree)

    noi_dung = (f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},\\widehat{{{C}}}={goc_C_degree}^\\circ$. Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần trăm). "    

    )
    debai_word= f"{noi_dung}\n"

    S=f"{round(1/2*l_a*l_b*sin(goc_C),2)}".replace(".",",")
    S_false=f"{round(l_a*l_b*sin(goc_C),2)}".replace(".",",")

    kq1_T=f"* Diện tích tam giác là $S = {S}$"
    kq1_F=f"Diện tích tam giác là $S = {S_false}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$S={phan_so(1/2)}.{l_a}.{l_b}.\\sin {goc_C_degree}^\\circ = {S}.$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    l_c=f"{round(sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)),2)}".replace(".",",")
    l_c_false=f"{round(sqrt(l_a**2+l_b**2-l_a*l_b*cos(goc_C)),2)}".replace(".",",")

    kq2_T=f"*${c}={l_c}$"
    kq2_F=f"${c}= {l_c_false}$"
    kq2=random.choice([kq2_T, kq2_F])

    l_c_sq=f"{round((l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)),2)}".replace(".",",")    

    HDG=f"${c}^2={l_a}^2+{l_b}^2-2.{l_a}.{l_b}.\\cos {{{goc_C_degree}}}^\\circ={l_c_sq} \\Rightarrow  {c}= {l_c}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #kq3
    l_c=sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C))
    cosA=f"{round((l_b**2+l_c**2-l_a**2)/(2*l_b*l_c),2)}".replace(".",",")
    cosA_false=f"{round((l_b**2+l_c**2-l_a**2)/(4*l_b*l_c),2)}".replace(".",",")

    kq3_T=f"*$\\cos {A}={cosA}$" 
    kq3_F=f"$\\cos {A}={cosA_false}$ "
    kq3=random.choice([kq3_T, kq3_F])
   
    l_c=f"{round(sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)),2)}".replace(".",",")  
    HDG=f"$\\cos {A}=\\dfrac{{{l_b}^2+{l_c}^2-{l_a}^2 }}{{2.{l_b}.{l_c}}}={cosA}$.\n"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #kq4
    l_c=sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C))
    cosB=(l_a**2+l_c**2-l_b**2)/(2*l_a*l_c)
    goc_B=f"{round(math.degrees(acos(cosB)),2)}".replace(".",",")

    cosB_false=(l_a**2+l_c**2-l_b**2)/(4*l_a*l_c)
    goc_B_false=f"{round(math.degrees(acos(cosB_false)),2)}".replace(".",",")

    kq4_T=f"*$\\widehat{{{B}}}={goc_B}^\\circ$"
    kq4_F=f"$\\widehat{{{B}}}={goc_B_false}^\\circ$ " 
    kq4=random.choice([kq4_T, kq4_F])

    l_c=f"{sqrt(l_a**2+l_b**2-2*l_a*l_b*cos(goc_C)):.2f}".replace(".",",")
    HDG=f"$\\cos {B}=\\dfrac{{{l_a}^2+{l_c}^2-{l_a}^2}}{{2.{l_a}.{l_c}}}={round(cosB,3)}\\Rightarrow \\widehat{{{B}}}={goc_B}^\\circ$."
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

def generate_triangle_sides():
    while True:
        # Tạo ba số ngẫu nhiên từ 1 đến 10
        a = sp.Rational(random.randint(1, 8))
        b = sp.Rational(random.randint(1, 8))
        c = sp.Rational(random.randint(1, 8))
        
        # Kiểm tra điều kiện bất đẳng thức tam giác
        if a + b > c and a + c > b and b + c > a:
            return a, b, c

#[D10_C4_B2_08]-TF-M2. Cho a,b c. Xét Đ-S: p, S, r, R
def yy3yy_L10_C4_B2_08():
    chon=random.randint(1,2)
    if chon==1:
        a=["a","b","c"]
        b=["b","c","a"]
        c=["c","a","b"]   
    
    if chon==2:
        a=["BC","AC","AB"]
        b=["AC","AB","BC"]
        c=["AB","BC","AC"]    
  
    A=["A","B","C"]
    B=["B","C","A"]
    C=["C","A","B"]
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_a, l_b, l_c=generate_triangle_sides()
    goc_C_degree=random.randint(10,130)
    goc_C= math.radians(goc_C_degree)

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},{c}={l_c}$. Xét tính đúng-sai của các khẳng định sau:"        
    debai_word= f"{noi_dung}\n"

    p=(l_a+l_b+l_c)/2

    kq1_T=f"* $p={phan_so(p)}$" 
    kq1_F=f" $p={l_a+l_b+l_c}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$p=\\dfrac{{{l_a}+{l_b}+{l_c}}}{{2}}={phan_so(p)}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    S=sqrt(p*(p-l_a)*(p-l_b)*(p-l_c))
    S_false=sqrt((p-l_a)*(p-l_b)*(p-l_c))

    kq2_T=f"* $S={latex(nsimplify(S))}$"
    kq2_F=f"$S={latex(nsimplify(S_false))}$ "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{l_a}).({phan_so(p)}-{l_b}).({phan_so(p)}-{l_c})}}={latex(nsimplify(S))}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $r={latex(S/p)}$" 
    kq3_F=f"$r={latex(S/(2*p))}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$r=\\dfrac{{S}}{{p}}=\\dfrac{{{latex(nsimplify(S))}}} {{{phan_so(p)}}}={latex(S/p)}$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    R=(l_a*l_b*l_c)/(4*S)
    R_false=(l_a*l_b*l_c)/(2*S)

    kq4_T=f"* $R={latex(R)}$"
    kq4_F=f"$R={latex(R_false)}$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$S=\\dfrac{{abc}}{{4R}}\\Rightarrow R=\\dfrac{{abc}}{{4S}}=\\dfrac{{{l_a}.{l_b}.{l_c}}}{{4.{latex(S)}}}={latex(R)}$."
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

#[D10_C4_B2_09]-TF-M2. Cho a,b,c. Xét Đ-S: cosA, B, S, sinC, R, r
def yy3yy_L10_C4_B2_09():
    a=["a","b","c"]
    b=["b","c","a"]
    c=["c","a","b"]   
 
    A=["A","B","C"]
    B=["B","C","A"]
    C=["C","A","B"]
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_a, l_b, l_c=generate_triangle_sides()
    goc_C_degree=random.randint(10,130)
    goc_C= math.radians(goc_C_degree)

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},{c}={l_c}$. Xét tính đúng-sai của các khẳng định sau(kết quả làm tròn đến hàng phần trăm):"        
    debai_word= f"{noi_dung}\n"

    cosA=(l_b**2+l_c**2-l_a**2)/(2*l_b*l_c)
    cosA_false=(l_b**2+l_c**2-l_a**2)/(4*l_b*l_c)

    kq1_T=f"* $\\cos {A}={phan_so(cosA)}$" 
    kq1_F=f"$\\cos {A}={phan_so(cosA_false)}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\cos {A}=\\dfrac{{{l_b}^2+{l_c}^2-{l_a}^2}}{{2.{l_b}.{l_c}}}={phan_so(cosA)}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    p=(l_a+l_b+l_c)/2
    S=sqrt(p*(p-l_a)*(p-l_b)*(p-l_c))
    S_false=sqrt((p-l_a)*(p-l_b)*(p-l_c))

    kq2_T=f"* $S={latex(nsimplify(S))}$"
    kq2_F=f"$S={latex(nsimplify(S_false))}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=(f"$p=\\dfrac{{{l_a}+{l_b}+{l_c}}}{{2}}={phan_so(p)}$.\n\n"
        f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{l_a}).({phan_so(p)}-{l_b}).({phan_so(p)}-{l_c})}}={latex(nsimplify(S))}$.\n")
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cosB=(l_a**2+l_c**2-l_b**2)/(2*l_a*l_c)
    cosB_false=(l_a**2+l_c**2-l_b**2)/(4*l_a*l_c)
    goc_B=f"{math.degrees(acos(cosB)):.2f}".replace(".",",")
    goc_B_false=f"{math.degrees(acos(cosB_false)):.2f}".replace(".",",")

    kq3_T=f"*$\\widehat{{{B}}}={goc_B}^\\circ$" 
    kq3_F=f"$\\widehat{{{B}}}={goc_B_false}^\\circ$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$\\cos {B}=\\dfrac{{{l_a}^2+{l_c}^2-{l_b}^2}}{{2.{l_a}.{l_c}}}={phan_so(cosB)} \\Rightarrow \\widehat{{{B}}}={goc_B}^\\circ$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,3)
    
    if chon==1:
        R=(l_a*l_b*l_c)/(4*S)
        R_false=(l_a*l_b*l_c)/(2*S)

        kq4_T=f"* $R={latex(R)}$"
        kq4_F=f"$R={latex(R_false)}$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$S=\\dfrac{{abc}}{{4R}}\\Rightarrow R=\\dfrac{{abc}}{{4S}}=\\dfrac{{{l_a}.{l_b}.{l_c}}}{{4.{latex(S)}}}={latex(R)}$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        kq4_T=f"* $r={latex(S/p)}$" 
        kq4_F=f"$r={latex(S/(2*p))}$"
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$r=\\dfrac{{S}}{{p}}=\\dfrac{{{latex(nsimplify(S))}}} {{{phan_so(p)}}}={latex(S/p)}$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon==3:
        cosC=(l_a**2+l_b**2-l_c**2)/(2*l_a*l_b)
        cosC_false=(l_a**2+l_b**2-l_c**2)/(4*l_a*l_b)

        sinC=sqrt(1-cosC**2)
        sinC_false=sqrt(1-cosC_false**2)

        kq4_T=f"* $\\sin {{{C}}}={latex(nsimplify(sinC))}$"
        kq4_F=f"$\\sin {{{C}}}={latex(nsimplify(sinC_false))}$ " 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$\\cos {C}=\\dfrac{{{l_a}^2+{l_b}^2-{l_c}^2}}{{2.{l_a}.{l_b}}}={phan_so(cosC)} \\Rightarrow \\sin {C}=\\sqrt{{1-\\left({phan_so(cosC)}\\right)^2}}={latex(nsimplify(sinC))}$."
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

#[D10_C4_B2_10]-TF-M2. Cho AB,BC,AC. Xét Đ-S: cosA, B, S, sinC, R, r
def yy3yy_L10_C4_B2_10():
    chon=random.randint(1,2)
    if chon==1:
        a=["BC","AC","AB"]
        b=["AC","AB","BC"]
        c=["AB","BC","AC"]    

        A=["A","B","C"]
        B=["B","C","A"]
        C=["C","A","B"]
        tamgiac="ABC"
    
    if chon==2:
        a=["MN","NP","MP"]
        b=["NP","MP","MN"]
        c=["MP","MN","NP"]    

        A=["P","M","N"]
        B=["M","N","P"]
        C=["N","P","M"]
        tamgiac="MNP"
 
    
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_a, l_b, l_c=generate_triangle_sides()
    goc_C_degree=random.randint(10,130)
    goc_C= math.radians(goc_C_degree)

    noi_dung = f"Cho tam giác ${{{tamgiac}}}$ có ${a}={l_a},{b}={l_b},{c}={l_c}$. Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần trăm):"        
    debai_word= f"{noi_dung}\n"

    cosA=(l_b**2+l_c**2-l_a**2)/(2*l_b*l_c)
    cosA_false=(l_b**2+l_c**2-l_a**2)/(4*l_b*l_c)

    kq1_T=f"* $\\cos {A}={phan_so(cosA)}$" 
    kq1_F=f"$\\cos {A}={phan_so(cosA_false)}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\cos {A}=\\dfrac{{{l_b}^2+{l_c}^2-{l_a}^2}}{{2.{l_b}.{l_c}}}={phan_so(cosA)}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    p=(l_a+l_b+l_c)/2
    S=sqrt(p*(p-l_a)*(p-l_b)*(p-l_c))
    S_false=sqrt((p-l_a)*(p-l_b)*(p-l_c))

    kq2_T=f"* $S={latex(nsimplify(S))}$"
    kq2_F=f"$S={latex(nsimplify(S_false))}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=(f"$p=\\dfrac{{{l_a}+{l_b}+{l_c}}}{{2}}={phan_so(p)}$.\n\n"
        f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{l_a}).({phan_so(p)}-{l_b}).({phan_so(p)}-{l_c})}}={latex(nsimplify(S))}$.\n")
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cosB=(l_a**2+l_c**2-l_b**2)/(2*l_a*l_c)
    cosB_false=(l_a**2+l_c**2-l_b**2)/(4*l_a*l_c)
    goc_B=f"{math.degrees(acos(cosB)):.2f}".replace(".",",")
    goc_B_false=f"{math.degrees(acos(cosB_false)):.2f}".replace(".",",")

    kq3_T=f"*$\\widehat{{{B}}}={goc_B}^\\circ$" 
    kq3_F=f"$\\widehat{{{B}}}={goc_B_false}^\\circ$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$\\cos {B}=\\dfrac{{{l_a}^2+{l_c}^2-{l_b}^2}}{{2.{l_a}.{l_c}}}={phan_so(cosB)} \\Rightarrow \\widehat{{{B}}}={goc_B}^\\circ$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,3)
    
    if chon==1:
        R=(l_a*l_b*l_c)/(4*S)
        R_false=(l_a*l_b*l_c)/(2*S)

        kq4_T=f"* $R={latex(R)}$"
        kq4_F=f"$R={latex(R_false)}$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$S=\\dfrac{{abc}}{{4R}}\\Rightarrow R=\\dfrac{{abc}}{{4S}}=\\dfrac{{{l_a}.{l_b}.{l_c}}}{{4.{latex(S)}}}={latex(R)}$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        kq4_T=f"* $r={latex(S/p)}$" 
        kq4_F=f"$r={latex(S/(2*p))}$"
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$r=\\dfrac{{S}}{{p}}=\\dfrac{{{latex(nsimplify(S))}}} {{{phan_so(p)}}}={latex(S/p)}$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon==3:
        cosC=(l_a**2+l_b**2-l_c**2)/(2*l_a*l_b)
        cosC_false=(l_a**2+l_b**2-l_c**2)/(4*l_a*l_b)

        sinC=sqrt(1-cosC**2)
        sinC_false=sqrt(1-cosC_false**2)

        kq4_T=f"* $\\sin {{{C}}}={latex(nsimplify(sinC))}$"
        kq4_F=f"$\\sin {{{C}}}={latex(nsimplify(sinC_false))}$ " 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$\\cos {C}=\\dfrac{{{l_a}^2+{l_b}^2-{l_c}^2}}{{2.{l_a}.{l_b}}}={phan_so(cosC)} \\Rightarrow \\sin {C}=\\sqrt{{1-\\left({phan_so(cosC)}\\right)^2}}={latex(nsimplify(sinC))}$."
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

#[D10_C4_B2_11]-TF-M2. Cho A,B và cạnh a. Xét Đ-S: góc C, cạnh a, cạnh b, diện tích
def yy3yy_L10_C4_B2_11():
    a=["a","b","c"]
    b=["b","c","a"]
    c=["c","a","b"]    
    A=["A","B","C"]
    B=["B","C","A"]
    C=["C","A","B"]
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_a=random.randint(1,7)
    
    goc_A_degree=random.randint(10,80)
    goc_A= math.radians(goc_A_degree)

    goc_B_degree=random.randint(10,60)
    if goc_B_degree==goc_A_degree:
        goc_B_degree=goc_B_degree+random.randint(5,10)
    goc_B= math.radians(goc_B_degree)

    goc_C_degree=180-goc_A_degree-goc_B_degree
    goc_C_degree_false=goc_A_degree+goc_B_degree
    goc_C=math.radians(goc_C_degree)

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},\\widehat{{{A}}}={goc_A_degree}^\\circ, \\widehat{{{B}}}={goc_B_degree}^\\circ$. Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần trăm): "        
    debai_word= f"{noi_dung}\n"    

    kq1_T=f"* $\\widehat{{{C}}} = {goc_C_degree}^\\circ$"
    kq1_F=f"$\\widehat{{{C}}} = {goc_C_degree_false}^\\circ$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\widehat{{{C}}}=180^\\circ - {goc_A_degree}^\\circ-{goc_B_degree}^\\circ={goc_C_degree}^\\circ$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    l_b=f"{round(l_a*sin(goc_B)/sin(goc_A),2):.2f}".replace(".",",")
    l_b_false=f"{round(l_a*sin(goc_A)/sin(goc_B),2):.2f}".replace(".",",")

    kq2_T=f"*${b}={l_b}$"
    kq2_F=f"${b}= {l_b_false}$"
    kq2=random.choice([kq2_T, kq2_F])


    HDG=f"$\\dfrac{{{b}}}{{\\sin {B}}}=\\dfrac{{{a}}}{{\\sin {A}}}\\Rightarrow {b}=\\dfrac{{{a}\\sin {B}}}{{\\sin {A}}}={l_b}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #kq3
    l_c=f"{round(l_a*sin(goc_C)/sin(goc_A),2):.2f}".replace(".",",")
    l_c_false=f"{round(2*l_a*sin(goc_C)/sin(goc_C),2):.2f}".replace(".",",")

    kq3_T=f"*${c}={l_c}$"
    kq3_F=f"${c}= {l_c_false}$"
    kq3=random.choice([kq3_T, kq3_F])
   
    
    HDG=f"$\\dfrac{{{c}}}{{\\sin {C}}}=\\dfrac{{{a}}}{{\\sin {A}}}\\Rightarrow {c}=\\dfrac{{{a}\\sin {C}}}{{\\sin {A}}}={l_c}$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #kq4
    l_b=l_a*sin(goc_B)/sin(goc_A)
    S=f"{round(1/2*l_a*l_b*sin(goc_C),2):.2f}".replace(".",",")
    S_false=f"{round(l_a*l_b*sin(goc_C),2):.2f}".replace(".",",")

    kq4_T=f"* Diện tích tam giác đã cho bằng ${{{S}}}$"
    kq4_F=f"Diện tích tam giác đã cho bằng ${{{S_false}}}$" 
    kq4=random.choice([kq4_T, kq4_F])
    l_b=f"{round(l_a*sin(goc_B)/sin(goc_A),2)}".replace(".",",")

   
    HDG=f"$S=\\dfrac{{1}}{{2}}.{l_a}.{l_b}.\\sin {C}={S}$."
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
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

#[D10_C4_B2_12]-M2. Cho A,B và cạnh a. Tính cạnh b hoặc c
def yy3yy_L10_C4_B2_12():
    a=["a","b","c"]
    b=["b","c","a"]
    c=["c","a","b"]    
    A=["A","B","C"]
    B=["B","C","A"]
    C=["C","A","B"]
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_a=random.randint(1,7)

    while True:
    
        goc_A_degree=random.randint(10,80)
        goc_A= math.radians(goc_A_degree)

        goc_B_degree=random.randint(10,60)
        if goc_B_degree==goc_A_degree:
            goc_B_degree=goc_B_degree+random.randint(5,10)
        goc_B= math.radians(goc_B_degree)

        goc_C_degree=180-goc_A_degree-goc_B_degree
        goc_C_degree_false=goc_A_degree+goc_B_degree
        goc_C=math.radians(goc_C_degree)
        if all([goc_C_degree!=45]):
            break

    l_c=f"{round(l_a*sin(goc_C)/sin(goc_A),2):.1f}".replace(".",",")
    l_c_false=f"{round(2*l_a*sin(goc_C)/sin(goc_C),2):.1f}".replace(".",",")

    l_b=f"{round(l_a*sin(goc_B)/sin(goc_A),2):.1f}".replace(".",",")
    l_b_false=f"{round(l_a*sin(goc_A)/sin(goc_B),2):.1f}".replace(".",",")

    HDG=f"$\\dfrac{{{b}}}{{\\sin {B}}}=\\dfrac{{{a}}}{{\\sin {A}}}\\Rightarrow {b}=\\dfrac{{{a}\\sin {B}}}{{\\sin {A}}}={l_b}$."

    noi_dung = (f"Cho tam giác ${{ABC}}$ có ${a}={l_a},\\widehat{{{A}}}={goc_A_degree}^\\circ, \\widehat{{{B}}}={goc_B_degree}^\\circ$."
        f" Độ dài cạnh ${{{c}}}$ bằng (kết quả làm tròn đến hàng phần mười)."
    )    

    kq=l_a*sin(goc_C)/sin(goc_A)
   
    numbers = set()
    while len(numbers) <5:        
        numbers.add(round(random.uniform(2, 10), 1))  # 4 chữ số thập phân

    kq_false = list(numbers)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(f"$\\widehat{{{C}}}=180^\\circ-{goc_A_degree}^\\circ-{goc_B_degree}^\\circ={goc_C_degree}^\\circ$.\n\n"
        f"$\\dfrac{{{c}}}{{\\sin {C}}}=\\dfrac{{{a}}}{{\\sin {A}}}\\Rightarrow {c}=\\dfrac{{{a}\\sin {C}}}{{\\sin {A}}}={l_c}$."
        )

    pa_A= f"*${{{round(kq,2):.1f}}}$".replace(".",",")
    pa_B= f"${{{round(kq2,2):.1f}}}$".replace(".",",")
    pa_C= f"${{{round(kq3,2):.1f}}}$".replace(".",",")
    pa_D= f"${{{round(kq4,2):.1f}}}$".replace(".",",")
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
        f"\\shortans[4]{{{l_b}}}\n"
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C4_B2_13]-TL-M3. Cho b,c và góc C. Tính cạnh a
def yy3yy_L10_C4_B2_13():
    a=["a","b","c"]
    b=["b","c","a"]
    c=["c","a","b"]    
    A=["A","B","C"]
    B=["B","C","A"]
    C=["C","A","B"]
    i=random.randint(0,2)
    a,b,c,A,B,C=a[i], b[i], c[i], A[i], B[i], C[i]

    l_b=random.randint(1,7)
    l_c=l_b+random.randint(1,5)
    
    goc_C_degree=random.randint(10,80)
    goc_C= math.radians(goc_C_degree)

    sin_B=l_b*math.sin(goc_C)/l_c
    goc_B=math.asin(sin_B)
    goc_B_degree=math.degrees(goc_B)

    goc_A=pi-goc_B-goc_C


    l_a=f"{round(l_c*sin(goc_A)/sin(goc_C),1):.1f}".replace(".",",")
    dap_an=l_a


    noi_dung = (f"Cho tam giác ${{ABC}}$ có ${b}={l_b},{c}={l_c}, \\widehat{{{C}}}={goc_C_degree}^\\circ$."
        f" Tính độ dài cạnh ${{{a}}}$ (kết quả làm tròn đến hàng phần mười)."
    )

    noi_dung_loigiai=(
     f"$\\dfrac{{{b}}}{{\\sin {B}}}=\\dfrac{{{c}}}{{\\sin {C}}}"
     f"\\Rightarrow \\sin {B}=\\dfrac{{{b}\\sin {C}}}{{{c}}}={round(l_b*sin(goc_C)/l_c,3)}$\n\n"
     f"$\\Rightarrow \\widehat{{{B}}}={round(goc_B_degree,2)}^\\circ$\n\n"
     f"$\\widehat{{{A}}}=180^\\circ-{round(goc_B_degree,2)}^\\circ-{round(goc_C_degree,2)}^\\circ={round(180-goc_B_degree-goc_C_degree,2)}^\\circ$\n\n"
     f"$\\dfrac{{{a}}}{{\\sin {A}}}=\\dfrac{{{c}}}{{\\sin {C}}}\\Rightarrow {a}=\\dfrac{{{c}\\sin {A} }}{{\\sin {C} }}={l_a}$"
     )

    noi_dung_loigiai=noi_dung_loigiai.replace(".",",")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B2_14]-TL-M3. Ứng dụng hệ thức lượng trong tam giác
def yy3yy_L10_C4_B2_14():
    a=random.choice([1.7, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 ])
    a1=str(a).replace(".",",")
    h=random.randint(10,30)
    x=random.randint(20,35)
    y=x+random.randint(35,40)
    AC1= (h*math.sin(math.radians(90+x)))/math.sin(math.radians(y-x))
    e=round(AC1)
    kq= f"{round(AC1*sin(math.radians(y)) +a,2):.1f}".replace(".",",")
    code_hinh=r"""
    \begin{tikzpicture}[scale=.8,font=\footnotesize,line cap=round,line join=round,>=stealth]
    \draw (0,0) coordinate(O)grid (2,6);
    \draw (2,6)--(2,6.5) coordinate(A) (2,.5) coordinate(B);
    \path[shift={(B)}] (75:1) coordinate(b);
    \path[shift={(A)}] (35:1) coordinate(a);
    \path (intersection of A--a and B--b) coordinate(C) ($(A)!.8!(C)$) coordinate(D) ($(O)!(C)!(5,0)$) coordinate(H) ($(C)!(A)!(H)$) coordinate(I) ($(C)!(B)!(H)$) coordinate(J);
    \path[shift={(C)}] (65:.4) coordinate(E) (140:1) coordinate(F) ($(C)!.6!(F)$) coordinate(G);
    \fill[cyan!80] (C)--(D) .. controls + (130:.5) and +(-100:.3) .. (F) .. controls +(10:.3) and +(120:.4) ..(E) .. controls +(-120:.3) and +(70:.2) .. cycle;
    \fill[blue!80!black] (C)--(G) .. controls +(50:.3) and +(130:.2) .. (E) .. controls +(-120:.3) and +(70:.2) .. cycle;
    \fill[blue!80!black] (D) .. controls + (130:.5) and +(-100:.3) .. (F) -- (G) .. controls +(-130:.3) and +(110:.2) .. cycle;
    \draw[color=blue!80!red] (C) .. controls +(-10:.6) and +(150:.5) .. (5,7);
    \draw[color=blue!80!red] (C) .. controls +(-15:.6) and +(150:.5) .. (4.8,6.9);
    \draw (A)--(C)--(B) (2,0)--(H);
    \draw[dashed] (C)--(H) (A)--(I) (B)--(J);
    \path (O)--(0,6) node[midway,left]{$h$} (A) node[shift={(180:.3)}]{$A$} (B) node[shift={(-45:.3)}]{$B$};
    \begin{scope}
        \clip (C)--(A)--(I);
        \draw (A) circle(.4) node[shift={(15:.5)}]{$\alpha$};
    \end{scope}
    \begin{scope}
        \clip (C)--(B)--(J);
        \draw[double] (B) circle(.4) node[shift={(35:.55)}]{$\beta$};
    \end{scope}
    
\end{tikzpicture}
    """
    code_hinh1=r"""
\begin{tikzpicture}[scale=.8,font=\footnotesize,line cap=round,line join=round,>=stealth]
    \path (0,0) coordinate(B) (0,6) coordinate(A) + (35:1) coordinate(a) (75:1) coordinate(b) (intersection of A--a and B--b) coordinate(C) ($(B)!(C)!(1,0)$) coordinate(H) ($(C)!(A)!(H)$) coordinate(K);
    \draw (A)--(B)--(C)--cycle (C)--(H)--(B) (A)--(K);
    \foreach \d/\g in {A/180, B/-135, C/45, H/-45, K/0}
    \fill (\d) circle(1pt) node[shift={(\g:.3)}]{$\d$};
    \path pic[draw,angle radius=.15cm]{right angle=A--K--C} pic[draw,angle radius=.15cm]{right angle=B--H--C};
       
    
\end{tikzpicture}
    """
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    code1 = my_module.moi_truong_anh_latex(code_hinh1)
    file_name1=my_module.pdftoimage_timename(code1)
    A=random.choice(["Hiếu", "Hoàng", "Lam", "Minh", "Khôi", "Quân", "Nghĩa"])
    B=random.choice(["Hồng", "Hà", "Lan", "Mạnh", "Khánh", "Quyên", "Nga"])
    noi_dung = f"   Bạn {A} đứng ở đỉnh của tòa nhà và quan sát chiếc diều, nhận thấy góc nâng (góc nghiêng giữa phương từ mắt của bạn {A} tới chiếc diều và phương nằm ngang) là $\\alpha={x}^{{\\circ}}$; khoảng cách từ đỉnh tòa nhà tới mắt bạn {A} là ${{{a1}}}$m. Cùng lúc đó ở dưới chân tòa nhà, bạn {B} cũng quan sát chiếc diều và thấy góc nâng là $\\beta={y}^{{\\circ}}$; khoảng cách từ mặt đất tới mắt bạn {B} cũng là ${{{a1}}}$m. Biết chiều cao của tòa nhà là $h={{{h}}}m$ (minh họa ở hình bên). Chiếc diều bay cao bao nhiêu mét so với mặt đất (làm tròn kết quả đến hàng phần mười)?"

    noi_dung_loigiai=(f"Kí hiệu ${{C}}$ là vị trí của chiếc diều.\n\n"
             f"Từ điểm ${{B}}$ vẽ đường thẳng $Bx$ vuông góc với ${{AB}}$.\n\n"
             f"Từ điểm ${{C}}$ kẻ $CH\\perp Bx$ (${{H}}$ thuộc ${{Bx}}$).\n\n"
           f"Từ điểm ${{A}}$ kẻ $AK\\perp CH$ (${{K}}$ thuộc ${{CH}}$).\n\n"
             f"Khi đó $\\widehat{{CAK}}=\\alpha$ và $\\widehat{{CBH}}=\\beta$.\n\n" 
            f"Chiều cao của diều so với mặt đất chính là độ dài đoạn thẳng ${{CH}}$.\n\n"
            f"Vì khoảng cách từ đỉnh tòa nhà tới mắt bạn ${{A}}$ và khoảng cách từ mặt đất tới mắt bạn ${{B}}$ đều là ${{{a1}}}$m nên ${{AB=h={h}}}$m.\n\n"
            f"Tứ giác ${{ABHK}}$ là hình chữ nhật.\n\n"
             f"$\\widehat{{CAB}} = \\widehat{{CAK}}+\\widehat{{KAB}} = {x}^{{\\circ}} + 90^{{\\circ}} = {90+x}^{{\\circ}}$.\n\n"
            f"$\\widehat{{CBA}} = \\widehat{{ABH}}-\\widehat{{CBH}} = 90^{{\\circ}}-{y}^{{\\circ}} = {90-y}^{{\\circ}}$.\n\n"
             f"Trong tam giác ${{ABC}}$ ta có \n\n"
            f"$\\widehat{{C}}= 180^{{\\circ}} - \\left(\\widehat{{A}}+\\widehat{{B}}\\right) = 180^{{\\circ}} - \\left({90+x}^{{\\circ}}+{90-y}^{{\\circ}}\\right) = {y-x}^{{\\circ}}$.\n\n"
            f"Áp dụng định lí sin trong tam giác ${{ABC}}$ ta có\n\n"
         f"$\\dfrac{{AB}}{{ \\sin C}} = \\dfrac{{BC}}{{\\sin A }} \\Rightarrow BC = \\dfrac{{AB\\sin A}}{{\\sin C}} = \\dfrac{{ {h}\\sin {90+x}^{{\\circ}} }}{{\\sin {y-x}^{{\\circ}} }} \\approx {e}$\n\n"
         f"Trong tam giác ${{CBH}}$ vuông tại ${{H}}$ ta có \n\n"
         f"$CH=BC\\sin B  \\approx {e}\\sin{{ {y}^{{\\circ}} }}\\approx {round(AC1*sin(math.radians(y)))}$ m\n\n"
        f"Vậy chiếc diều bay cao khoảng ${{{kq}}}$ mét so với mặt đất.")

    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n{file_name1} \n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n{code_hinh1} \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an



#[D10_C4_B2_15]-TL-M3. Ứng dụng hệ thức lượng vào thực tế 2
def yy3yy_L10_C4_B2_15():
    a=random.choice([2.7, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3, 3.2, 3.4, 3.5, 3.6 ])
    a1=str(a).replace(".","{,}")
    
    x=random.randint(40,50)
    y=x+random.randint(60,65)
    c= (a*math.sin(math.radians(x)))/math.sin(math.radians(180-y-x))
    
    kq=f"{round(0.5*a*c*math.sin(math.radians(y)),1):.1f}".replace(".",",")
    c=round(c)
    code_hinh=fr"""

    \begin{{tikzpicture}}[smooth,font=\footnotesize,scale=0.5]
    \path
    (0,0) coordinate (A)
    (0.5,-1) coordinate (B)
    (7,-1) coordinate (C)
    (8.5,0.6) coordinate (D)
    ($(A)!0.45!(D)$)coordinate (O)
    ($(O)+(0,6.5)$)coordinate (O')
    ($(O)!0.1!(O')$)coordinate (M)
    ($(O)!0.8!(O')$)coordinate (N)
    ($(M)+(-0.1,0)$)coordinate (M1)
    ($(N)+(-0.1,0)$)coordinate (N1)
    ($(A)!0.85!(D)$)coordinate (O2)
    ($(M)+(+0.1,0)$)coordinate (M2)
    ($(N)+(+0.1,0)$)coordinate (N2)
    %
    ($(O)!0.85!(O')$)coordinate (C1)
    ($(O)!0.95!(O')$)coordinate (C2)
    ($(C1)!0.5!(C2)$)coordinate (C0)
    ($(C0)+(-2,0)$)coordinate (C3)
    ;
    %\coordinate (S) at ($(A)+(0,3)$);
    %\coordinate (M) at ($(B)!0.5!(C)$);
    \draw[line width=1pt,gray] (A)--(B)--(C)--(D)--cycle;
    \fill[red](C1)--(C3)--(C2);
    \fill[ball color=gray!50](A)--(B)--(C)--(D)--cycle;
    \draw[line width=3pt,brown] (O)--(O');
    \fill[cyan!40] (A)--(M1)--(N1)--cycle;
    \fill[ball color=yellow!50] (O2)--(M2)--(N2)--cycle;
    \draw (A)--(M1)--(N1)--cycle (O2)--(M2)--(N2)--cycle;
    \pic[draw, angle radius=7mm]{{angle=M1--A--N1}};
    \pic[ draw=none, angle radius=16mm]{{angle=M1--A--N1}};
    
    \pic[draw, angle radius=4mm]{{angle=N1--M1--A}};
    \pic[draw=none, angle radius=12mm]{{angle=N1--M1--A}};
    \path (A)--(M1) node[below,midway,sloped,scale=.8]{{\scriptsize ${a1}$m }};
\end{{tikzpicture}}

    """
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
   
    
    

    noi_dung = f" Tính diện tích một cánh buồm hình tam giác. Biết cánh buồm đó có chiều dài một cạnh là ${{{a1}}}$ m và hai góc kề cạnh đó có số đo là ${x}^{{\\circ}}$ và ${y}^{{\\circ}}$. Làm tròn kết quả đến hàng phần mười."

    noi_dung_loigiai=(f"Cánh buồn có dạng hình tam giác ${{ABC}}$ như hình vẽ bên.\n\n"
            f"Ta có $\\widehat{{C}}=180^{{\\circ}}-\\left( \\widehat{{A}}+\\widehat{{B}}\\right)=180^{{\\circ}}-({x}^{{\\circ}}+{y}^{{\\circ}}) ={180-x-y}^{{\\circ}}$.\n\n"
            f"Áp dụng hệ quả định lý sin cho tam giác ${{ABC}}$, ta được \n\n" 
            f"$BC=\\dfrac{{AB\\cdot \\sin A}}{{\\sin C}}=\\dfrac{{{a1}\\cdot \\sin {x}^{{\\circ}}}}{{\\sin {180-y-x}^{{\\circ}} }}\\approx    {c}m$\n\n"
            f"Vậy diện tích của cánh buồm là \n\n"
            f"$S=\\dfrac{{1}}{{2}}\\cdot BA\\cdot BC\\cdot \\sin B=\\dfrac{{1}}{{2}}\\cdot {a1}\\cdot {c}\\cdot \\sin {y}^{{\\circ}}\\approx {kq} m^{{2}}$")

    debai_word= f"{noi_dung}\n{file_name}\n"

    code_hinh1=fr"""
\begin{{tikzpicture}}[line join=round, line cap=round, >=stealth,scale=1]     
    \path (0,0)     coordinate(A)
    ++(10:3)coordinate(B)
    +(90:3)coordinate(C);
    \draw
    (A)--(B)--(C)--cycle    
    (A)+(30:1)node[scale=.7]{{${x}^\circ$}}
    (B)+(135:.7)node[scale=.7]{{${y}^\circ$}};
    \path
    (A)--(B)node[midway,below,scale=0.7]{{${a1}$ m}};   
    \tkzMarkAngles[size=.4](B,A,C C,B,A)
    \foreach \x/\g in {{C/90,A/210,B/-30}} \draw (\x)+(\g:0.3)node{{$\x$}};
\end{{tikzpicture}} """

    code1 = my_module.moi_truong_anh_latex(code_hinh1)
    file_name1=my_module.pdftoimage_timename(code1)
    

    loigiai_word=f"Lời giải:\n\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n{code_hinh1} \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an



#[D10_C4_B2_16]-SA-M3. Ứng dụng hệ thức lượng vào thực tế 3
def yy3yy_L10_C4_B2_16():
    a=random.randint(60,80)
    a1=str(a).replace(".",",")
    
    x=random.randint(40,50)
    y=x+random.randint(10,20)
    
    
    kq=f"{round(a*math.sin(math.radians(y))*math.sin(math.radians(x))/math.sin(math.radians(y-x)),1):.1f}".replace(".",",")
    
    code_hinh=fr"""
    \begin{{tikzpicture}}[scale=1, font=\footnotesize, line join=round, line cap=round,>=stealth]
    \path
    (1,0) coordinate (A)
    (2,0) coordinate (B)
    (4,3.5) coordinate (C)
    (4,0) coordinate (H)
    (3.75,0) coordinate (U)
    (4.25,0) coordinate (V)
    ;
    \draw[thick] (U)--(C)--(V); 
    \draw (B)--(C)--(A)--(V) ;
    \draw[dashed] (C)--(H) ;  
    \draw  
    ($(C)!{1}!(U)$)--($(C)!{{0.9}}!(V)$)
    --($(C)!{{0.8}}!(U)$)--($(C)!{{0.7}}!(V)$)
    --($(C)!{{0.6}}!(U)$)--($(C)!{{0.5}}!(V)$)
    --($(C)!{{0.4}}!(U)$)--($(C)!{{0.3}}!(V)$)
    --($(C)!{{0.2}}!(U)$)--($(C)!{{0.1}}!(V)$)
    ;
    
    \tkzMarkAngle[arc=l, size=0.6,mark=0](H,A,C)
    \tkzLabelAngle[pos=1](H,A,C) {{${x}^\circ$}}
    \tkzMarkAngle[arc=ll, size=0.6,mark=0](H,B,C)
    \tkzLabelAngle[pos=1](H,B,C) {{${y}^\circ$}}
    \foreach \x/\g in {{A/-90,B/-90,C/90,H/-90}} 
    \fill[black] (\x) circle (1pt)+(\g:3mm) node {{$\x$}};
\end{{tikzpicture}}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)


    noi_dung = f"Để đo chiều cao ${{CH}}$ của một tháp truyền hình, người ta chọn hai điểm quan sát ${{A}}$, ${{B}}$ trên mặt đất (hình vẽ).  Biết $\\widehat{{CAH}} ={x}^{{\\circ}}$, $\\widehat{{CBH}} ={y}^{{\\circ}}$ và $AB={a}m$, tính chiều cao của tháp. Làm tròn kết quả đến hàng phần mười."

    noi_dung_loigiai=(f"    Ta có $\\widehat{{ACB}}=\\widehat{{CBH}} - \\widehat{{CAH}}=  {y}^{{\\circ}} -{x}^{{\\circ}}= {y-x}^{{\\circ}}$. \n\n"
        f"Áp dụng định lí sin ta có \n\n"
        f"$\\dfrac{{AB}}{{\\sin \\widehat{{ACB}}}} = \\dfrac{{BC}}{{\\sin \\widehat{{CAH}} }} \\Rightarrow BC = \\dfrac{{AB\\sin \\widehat{{CAH}} }}{{\\sin \\widehat{{ACB}} }}  = \\dfrac{{{a}\\sin {x}^{{\\circ}}}}{{\\sin {y-x}^{{\\circ}}}}$\n\n"
        f"Suy ra $CH =BC\\sin \\widehat{{CBH}} = \\dfrac{{{a} \\sin {x}^{{\\circ}} \\sin {y}^{{\\circ}}}}{{\\sin {y-x}^{{\\circ}} }}\\approx {kq}m$.")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_C4_B2_17]-SA-M3. Ứng dụng hệ thức lượng vào thực tế 4
def yy3yy_L10_C4_B2_17():
    ten=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    a=random.randint(60,70)
    b=a+random.randint(5,12)

    c=random.randint(20,30)
    
    
    
    kq=f"{round(c*math.sin(math.radians(b))/math.sin(math.radians(180-a-b)),1):.1f}".replace(".",",")
    
    code_hinh=fr"""
  \begin{{tikzpicture}}[scale=1,font=\footnotesize,line cap=round,line join=round,>=stealth]
    \def\a{{3.75}}
    \path (0:0) coordinate(A) (59.95:1) coordinate(a) (0:\a) coordinate(C)  + (97.85:1) coordinate(c)  (intersection of A--a and C--c) coordinate(B);
    \fill[cyan!60] (-.5,2) .. controls +(-70:2) and +(150:1) .. (2.5,1) .. controls +(-15:2) and +(-30:1) .. (4.5,3.5) .. controls +(150:1) and +(40:1) .. (2,4) .. controls +(-150:1.5) and +(100:2) .. cycle;
    \draw (A)--(B)--(C)--cycle;
    \foreach \d/\g in {{A/-135, B/90, C/-45}}
    \fill (\d) circle(1pt) node[shift={{(\g:.3)}}]{{$\d$}};
    \path (A)--(C) node[midway,below]{{${c}$ m}} pic[draw,angle radius=.3cm]{{angle=C--A--B}} (A) node[shift={{(20:.8)}}]{{${a}^\circ$}} pic[draw,angle radius=.3cm]{{angle=B--C--A}} pic[draw,angle radius=.35cm]{{angle=B--C--A}} (C) node[shift={{(150:.7)}}]{{${b}^\circ$}};
    
 \end{{tikzpicture}}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)


    noi_dung = f"   Để đo khoảng cách từ vị trí ${{A}}$ đến vị trí ${{B}}$ ở hai bên bờ một cái ao, bạn {ten} đi dọc bờ ao từ vị trí ${{A}}$ đến vị trí ${{C}}$ và tiến hành đo các góc ${{BAC}}$, ${{BCA}}$. Biết ${{AC={c} m}}$, $\\widehat{{BAC}}={a}^{{\\circ}}$, $\\widehat{{BCA}}={b}^{{\\circ}}$ (hình vẽ bên). Hỏi khoảng cách từ vị trí ${{A}}$ đến vị trí ${{B}}$ là bao nhiêu mét (làm tròn kết quả đến hàng đơn vị)?"

    noi_dung_loigiai=(f"Trong tam giác ${{ABC}}$ ta có\n\n"
        f"$\\widehat{{A}}+\\widehat{{B}}+\\widehat{{C}}=180^{{\\circ}} \\Rightarrow \\widehat{{B}}=180^{{\\circ}} - \\left(\\widehat{{A}}+\\widehat{{C}}\\right) \\Rightarrow \\widehat{{B}} = 180^{{\\circ}} - \\left({a}^{{\\circ}} + {b}^{{\\circ}}\\right) = {180-a-b}^{{\\circ}}$ \n\n"
        f"Áp dụng định lí sin trong tam giác ${{ABC}}$ ta có\n\n"
        f"$\\dfrac{{AB}}{{\\sin C}} = \\dfrac{{AC}}{{\\sin B}} \\Rightarrow AB = \\dfrac{{AC\\sin C}}{{\\sin B}} = \\dfrac{{{c}\\sin {b}^\\circ}}{{\\sin {180-a-b}^{{\\circ}} }} \\approx {kq} m$ \n\n"
        f"Vậy khoảng cách từ vị trí ${{A}}$ đến vị trí ${{B}}$ gần bằng ${{{kq}}}$ mét.")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C4_B2_18]-SA-M3. Ứng dụng hệ thức lượng vào thực tế 5
def yy3yy_L10_C4_B2_18():
    ten=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    a=random.randint(20,30)
    b=random.randint(100,120)

    c=random.randint(150,300)
    
    kq=f"{round(c*math.sin(math.radians(a))/math.sin(math.radians(180-a-b)),0):.0f}".replace(".",",")
    
    code_hinh=r"""
    \begin{tikzpicture}[scale=1]
            \coordinate (X) at (1,1);
            \foreach \i in {0,...,6}
            \foreach \j  in {0,...,2}  
            \draw[blue] ($(X)+({\i+0.5},{0.6*(\j)+0.4})$)--($(X)+({\i+0.7},{0.6*(\j)+0.4})$);
            \coordinate [label=above left:$A$](A) at (3,3);
            \coordinate [label=below left:$B$](B) at (3,1);
            \coordinate [label=right:$C$](C) at (5,0.5);
            \draw (X)--(8,1) (8,3)--(1,3) (A)--(B)--(C)--(A);
            \foreach \i in {A,B,C} \draw[fill=black] (\i) circle(1.2pt);
        \end{tikzpicture}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)


    noi_dung = f"Để đo chiều rộng ${{AB}}$ của một khúc sông, người ta chọn điểm ${{C}}$.  Sau đó,  đo khoảng cách ${{BC}}$, các góc ${{B}}$ và ${{C}}$. Biết rằng ${{BC = {c}}}$ m, $\\widehat{{B}} = {b}^{{\\circ}}$,  $\\widehat{{C}} = {a}^{{\\circ}}$. Tìm chiều rộng ${{AB}}$ của khúc sông đó (làm tròn đến chữ số hàng đơn vị)."

    noi_dung_loigiai=( f" Ta có $\\widehat{{A}}= 180^{{\\circ}} -  \\widehat{{B}} -\\widehat{{C}} =180^{{\\circ}}- {b}^{{\\circ}} - {a}^{{\\circ}}={180-b-a}^{{\\circ}}$. \n\n"
       f" Áp dụng định lí sin ta có \n\n" 
        f"$\\dfrac{{AB}}{{\\sin C}} = \\dfrac{{BC}}{{\\sin A}} \\Rightarrow AB = \\dfrac{{BC\\sin C}}{{\\sin A}}  = \\dfrac{{{c}\\sin {a}^{{\\circ}}}}{{\\sin {180-b-a}^{{\\circ}}}} \\approx {kq} m $.")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an







#[D10_C4_B2_19]-SA-M3. Ứng dụng hệ thức lượng vào thực tế 6
def yy3yy_L10_C4_B2_19():
    ten=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    a=random.randint(20,30)
    a_radian = math.radians(a)
    b=random.randint(10,20)
    t=random.randint(2,4)
    c=random.choice([i for i in range(15,30) if i!=b])

    khoangcach=(t*b)**2+(t*c)**2-2*t*b*t*c*cos(a_radian)
    
    kq1=f"{round(khoangcach,1):.1f}".replace(".",",")
    kq=f"{round(sqrt(khoangcach),1):.1f}".replace(".",",")    
    code_hinh=r"""
    \begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.75]
            \foreach \x in {1,2,3}
            \foreach \y in {0,1,2,3,4,5}
            \draw(0.25+\y,\x-0.25)--(\y,\x-0.25) ;
            \foreach \x in {1,2,3}
            \foreach \y in {0,1,2,3,4,5}
            \draw(-0.25+\y,\x-0.75)--(\y,\x-0.75) ;
            \tkzDefPoints{0/0/A,4/0/B,1.5/2.5/C}
            \tkzDrawPoints[fill=black](A,B,C)
            \tkzDrawSegments(A,B A,C)
            \fill plot [smooth cycle] coordinates{(3.75,0)(4.25,0)(4.3,0.2)(4.15,0.2)(4.15,0.3)(4.05,0.3)(4.05,0.4)(3.95,0.4)(3.95,0.3)(3.85,0.3)(3.85,0.2)(3.7,0.2)} ;
            \fill plot [smooth cycle] coordinates{(1.25,2.5)(1.75,2.5)(1.8,2.7)(1.65,2.7)(1.65,2.8)(1.55,2.8)(1.55,2.9)(1.45,2.9)(1.45,2.8)(1.35,2.8)(1.35,2.7)(1.2,2.7)} ;
            \tkzLabelPoints[below](A,B,C)
        
        \end{tikzpicture}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    noi_dung = f"Hai chiếc tàu thủy cùng xuất phát từ một vị trí $ {{A}}$, đi thẳng theo hai hướng tạo với nhau góc ${a}^{{\\circ}}$. Tàu $ {{B}}$ chạy với tốc độ ${{{b}}}$ hải lí một giờ. Tàu ${{C}}$ chạy với tốc độ ${{{c}}}$ hải lí một giờ. Hỏi sau ${{{t}}}$ giờ, hai tàu cách nhau bao nhiêu hải lí?"

    noi_dung_loigiai=( f"Sau ${{{t}}}$ giờ tàu ${{B}}$ đi được ${{{phan_so(t*b)}}}$ hải lí, tàu ${{C}}$ đi được ${{{phan_so(t*c)}}}$ hải lí. \n\n"
        f"Vậy tam giác ${{ABC}}$ có ${{AB={phan_so(t*b)}}}$, ${{AC={phan_so(t*c)}}}$ và $ \\widehat{{A}}={a}^{{\\circ}}$. \n\n"
        f"Áp dụng định lí cô-sin vào tam giác $ {{ABC}}$, ta có \n\n"
        f"$ {{a^2=b^2+c^2-2bc\\cdot\\cos A={phan_so(t*b)}^{{2}}+ {phan_so(t*c)}^{{2}}-2\\cdot {phan_so(t*b)}\\cdot {phan_so(t*c)}\\cdot \\cos {a}^{{\\circ}}= {kq1}\\Rightarrow a\\approx  {kq} }}$ \n\n" 
       f" Vậy sau ${{{t}}}$ giờ, hai tàu cách nhau khoảng ${kq}$ hải lí.")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an







#[D10_C4_B2_20]-SA-M2. Ứng dụng hệ thức lượng vào thực tế 7
def yy3yy_L10_C4_B2_20():

    b=random.randint(10,20)
    c=Fraction(random.randint(50,150), 10)

    kq=f"{round(c/(2*math.sin(math.radians(b))),1):.1f}".replace(".",",").replace(",0"," ")
    c="{:g}".format(float(c)).replace(".",",").replace(".0", " ")
    code_hinh=r"""
        \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round,>=stealth]
            \coordinate (O) at (0,0); 
            \coordinate (A) at ($(O)+(131.4:3)$) ; 
            \coordinate (B) at ($(O)+(101.6:3)$) ; 
            \coordinate (C) at ($(O)+(41.7:3)$) ; 
            \coordinate (D) at ($(O)+(140:3)$) ; 
            \coordinate (E) at ($(O)+(90:1)$) ; 
            \coordinate (F) at ($(O)+(18:3)$) ; 
            \draw
            (D) 
            .. controls ++(0:0.5) and ++(150:0.5) .. (E)
            .. controls ++(180:-0.5) and ++(160: 0.5) .. (F)
            ;
            \draw (A)--(B)--(C)--(A)  ; 
            \draw  (F) arc (18:140:3);
            \foreach \x/\g in {A/140,B/90,C/60} 
            \fill[black] (\x) circle (1.1pt)+(\g:3mm) node {$\x$};
        \end{tikzpicture}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    noi_dung = f"Để đo bán kính của một chiếc đĩa cổ chỉ còn lại một phần, các nhà khảo cổ chọn ${{3}}$ điểm trên chiếc đĩa (hình vẽ) và tiến hành đo được kết quả như sau: $\\widehat{{A}}={b}^{{\\circ}}$, $BC={c}cm$. Tính bán kính của chiếc đĩa (làm tròn kết quả đến hàng phần mười)."

    noi_dung_loigiai=( f"   Áp dụng định lí sin suy ra bán kính của chiếc đĩa là\n\n"
        f"$R = \\dfrac{{BC}}{{2\\sin A}} = \\dfrac{{{c}}}{{2\\sin {b}^{{\\circ}}}} \\approx {kq} $cm")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an



#[D10_C4_B2_21]-SA-M2. Ứng dụng hệ thức lượng vào thực tế 8
def yy3yy_L10_C4_B2_21():

    b=random.randint(100,120)
    c=random.randint(100,110)
    g=random.randint(50,80)
    kq1=f"{round((b)**2+(c)**2-2*b*c*math.cos(math.radians(g)),0):.0f}".replace(".",",")
    kq=f"{round(sqrt((b)**2+(c)**2-2*b*c*math.cos(math.radians(g))),0):.0f}".replace(".",",").replace(",0"," ")    
    code_hinh=r"""
  \begin{tikzpicture}[scale=1, font=\footnotesize, line join = round, line cap = round]
        \tkzDefPoints{0/0/A,5/0/B,2/3/C,1/0/M,4/0/N}
        \tkzDrawPoints[](A,B,C)
        \tkzDrawSegments(C,A C,B A,M N,B)
        \tkzLabelPoints[below](A,B)
        \tkzLabelPoints[above](C)
        \draw plot [smooth cycle] coordinates{(1,0)(1.5,1.2) (2,1) (3,1.5) (4,0)(3,-1.2) (2.5,-0.75) (2,-1)};
        \fill[pattern=north east lines,opacity=0.5] plot [smooth cycle] coordinates{(1,0)(1.5,1.2) (2,1) (3,1.5) (4,0)(3,-1.2) (2.5,-0.75) (2,-1)};
\end{tikzpicture}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    noi_dung = f"Khoảng cách từ ${{A}}$ đến ${{B}}$ không thể đo trực tiếp được vì phải qua một đầm lầy. Người ta xác định được một điểm ${{C}}$ mà từ đó có thể nhìn được ${{A}}$ và ${{B}}$ dưới một góc ${g}^{{\\circ}}$. Biết ${{CA={b}}}$ m, ${{CB={c}}}$ m. Khoảng cách ${{AB}}$ bằng bao nhiêu?(kết quả làm tròn đến hàng đơn vị)"

    noi_dung_loigiai=( f"$AB^{{2}}=CA^{{2}}+CB^{{2}}-2\\cdot CA\\cdot CB\\cdot \\cos {g}^{{\\circ}} \\Rightarrow AB={kq}$ m")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an



#[D10_C4_B2_22]-SA-M2. Ứng dụng hệ thức lượng vào thực tế 9
def yy3yy_L10_C4_B2_22():

    b=random.randint(30,45)
    c=random.randint(65,80)
    a=random.randint(50,80)
    kq=f"{round(a*math.sin(math.radians(c))/math.sin(math.radians(180-b-c)),1):.1f}".replace(".",",").replace(",0"," ")
   
    code_hinh=fr"""
    \begin{{tikzpicture}}[scale=0.7, font=\footnotesize, line join = round, line cap = round,>=stealth]
    \clip (-4.39,3.2) rectangle (4,-4);
    \draw[pattern=north east lines,opacity=0.3] plot[smooth] coordinates{{(-4.39,1.43)(-2.43,1.46) (-1.48,1.67)(1.43,2.12)(2.01,2.09)(4,1.64) (4.1,-1.06)(3.02,-0.77)(1.85,-1.38)(0.95,-1.48)(0.13,-1.72)(-1.48,-1.67)(-2.46,-1.51)(-3.57,-0.98)(-4.37,-1.08)}};
    \draw[opacity=3] plot[smooth] coordinates{{(-4.39,1.43)(-2.43,1.46) (-1.48,1.67)(1.43,2.12)(2.01,2.09)(4,1.64) (4.1,-1.06)(3.02,-0.77)(1.85,-1.38)(0.95,-1.48)(0.13,-1.72)(-1.48,-1.67)(-2.46,-1.51)(-3.57,-0.98)(-4.37,-1.08)}};
    \draw[fill=white] plot[smooth  cycle] coordinates{{(-2.75,-0.08)(-1.83,0.32) (-0.03,0.42) (1,0) (0.24,-0.48)(-0.58,-0.79)(-1.38,-0.77)(-1.91,-0.71)}};
    \draw[fill=black!70]  plot[smooth  cycle] coordinates{{(-2.14,0.58)(-2.09,0.24)(-2.33,-0.13) (-1.19,-0.13) (-1.38,-0.13) (-1.69,0.21)(-1.75,0.53)}};
    \draw[fill=blue!30]  plot[smooth  cycle] coordinates{{(-1.75,0.53)(-1.46,0.79) (-1.01,0.58) (-1.08,1.06) (-0.64,1.08)(-0.93,1.59)(-0.53,1.85)(-0.93,2.2)(-1.38,2.7)(-2.04,3.18)(-2.49,2.91)(-3.07,2.91)(-3.2,2.22)(-3.73,1.96)(-3.1,1.3)(-3.31,1.01)(-2.83,1.01)(-2.99,0.69)(-2.14,0.58)}};
    \tkzDefPoints{{-1.38/-0.13/C,-2/-3/B,3/-2/A}}
    \tkzDrawPoints[fill=black](A,B,C)
    \tkzDrawPolygon(A,B,C)
    \tkzDefMidPoint(A,B) 
    \tkzLabelPoints[below](A,B)
    \tkzLabelPoints[above right](C)
    \tkzMarkAngles[size=1cm,arc=l,mark=|](C,A,B)
    \tkzMarkAngles[size=1cm,arc=l,mark=||](A,B,C)
    \tkzLabelAngles[left=1cm,pos=0.5,rotate=-20](B,A,C){{\footnotesize$\alpha$}}
    \tkzLabelAngles[right,pos=1](A,B,C){{\footnotesize$\beta$}}
 \end{{tikzpicture}}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    noi_dung = f"   Để đo khoảng cách từ một điểm ${{A}}$ trên bờ sông đến gốc cây ${{C}}$ trên cù lao giữa sông, người ta chọn một điểm ${{B}}$ cùng ở trên bờ với ${{A}}$ sao cho từ ${{A}}$ và ${{B}}$ có thể nhìn thấy điểm ${{C}}$. Ta đo được khoảng cách $ {{AB={a}}}$ m, $ \\widehat{{CAB}}={b}^{{\\circ}}$ và $ \\widehat{{CBA}}={c}^{{\\circ}}$. Tính độ dài ${{AC}}$ (Làm tròn kết quả đến hàng phần mười)."

    noi_dung_loigiai=( f"$\\widehat{{C}}=180^{{\\circ}}-(\\widehat{{A}}+\\widehat{{B}})={180-b-c}^{{\\circ}}$.\n\n"
        f"Áp dụng định lí sin vào tam giác ${{ABC}}$, ta có \n\n"
        f"$ \\dfrac{{AC}}{{\\sin B}}=\\dfrac{{AB}}{{\\sin C}}\\Rightarrow AC=\\dfrac{{AB\\cdot \\sin B}}{{\\sin C}}=\\dfrac{{{a}\\cdot \\sin {c}^\\circ}}{{\\sin {180-b-c}^{{\\circ}}}}\\approx  {kq} m$")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an



#[D10_C4_B2_23]-SA-M3. Ứng dụng hệ thức lượng vào thực tế 10
def yy3yy_L10_C4_B2_23():

    c=random.randint(30,45)
    b=c+random.randint(25,35)
    a=random.randint(50,80)
    kq=f"{round(a*math.sin(math.radians(c))*math.sin(math.radians(90-b))/math.sin(math.radians(b-c)),1):.1f}".replace(".",",").replace(",0"," ")
   
    code_hinh=fr"""
    \begin{{tikzpicture}}[scale=1, font=\footnotesize, line join=round, line cap=round, >=stealth]
            \path 
            (0,0) coordinate (X)
            (1.1,2) coordinate (Y)
            (2,2) coordinate (Z)
            (5,0) coordinate (A)
            (1.5,5) coordinate (B)
            (1.5,2) coordinate (C)
            (1.5,0) coordinate (K)
            (1.3,2) coordinate (U)
            (1.8,2) coordinate (V) 
            (5,2) coordinate (H);
            \draw  
            ($(B)!{1}!(U)$)--($(B)!{{0.9}}!(V)$)
            --($(B)!{{0.8}}!(U)$)--($(B)!{{0.7}}!(V)$)
            --($(B)!{{0.6}}!(U)$)--($(B)!{{0.5}}!(V)$)
            --($(B)!{{0.4}}!(U)$)--($(B)!{{0.3}}!(V)$)
            --($(B)!{{0.2}}!(U)$)--($(B)!{{0.1}}!(V)$)
            ;
            \draw[thick]  (X)--(A)--(Z)--(Y)--(X);
            \draw (A)--(B)  (U)--(B)--(V) (Y)--($(Y)!{{1.2}}!(H)$)  (X)--($(X)!{{1.2}}!(A)$);
            \draw[->] (A)--(H) ; 
            \draw ($(A)!0.5!(H)$) node[right]{{$h$}};
            \draw[dashed](B)--(K) (A)--(C);
            
            \tkzMarkAngle[arc=l, size=0.6,mark=0](K,C,A)
            \tkzLabelAngle[pos=0.9](K,C,A) {{${b}^{{\circ}}$}}
            \tkzMarkAngle[arc=ll, size=0.7,mark=0](K,B,A)
            \tkzLabelAngle[pos=1.1](V,B,A) {{${c}^{{\circ}}$}}
            \foreach \x/\g in{{A/-90,B/90,C/-130,H/90}}
            \fill[black](\x) ($(\x)+(\g:3mm)$)node{{$\x$}}; 
        \end{{tikzpicture}}
    """

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    noi_dung = f"Trên ngọn đồi có một cái tháp cao ${{{a}}}$m. Đỉnh tháp ${{B}}$ và chân tháp ${{C}}$ nhìn điểm ${{A}}$ ở chân đồi dưới các góc tương ứng bằng ${c}^{{\\circ}}$ và ${b}^{{\\circ}}$ so với phương thẳng đứng. Xác định chiều cao ${{HA}}$ của ngọn đồi. (Làm tròn đến phần mười)."

    noi_dung_loigiai=(f"Ta có $\\widehat{{BAC}} = {b}^{{\\circ}} - {c}^{{\\circ}} ={b-c}^{{\\circ}};  \\widehat{{ACH}} = 90^{{\\circ}} - {b}^{{\\circ}} ={90-b}^{{\\circ}} $\n\n"
        f"Áp dụng định lí sin ta có \n\n"
        f"$\\dfrac{{AC}}{{\\sin \\widehat{{ABC}} }} = \\dfrac{{BC}}{{\\sin \\widehat{{BAC}} }}\\Rightarrow AC =  \\dfrac{{BC\\sin \\widehat{{ABC}} }}{{\\sin \\widehat{{BAC}}}}=\\dfrac{{{a}\\sin {c}^{{\\circ}}}}{{\\sin {b-c}^{{\\circ}}}}$.\n\n"
        f"Suy ra $AH =AC \\sin \\widehat{{ACH}} = \\dfrac{{{a} \\sin {90-b}^{{\\circ}} \\sin {c}^{{\\circ }} }} {{\\sin {b-c}^{{\\circ}}}} \\approx {kq}m$")


    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{  \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C4_B2_24]-SA-M3. Ứng dụng hệ thức lượng vào thực tế 10
def yy3yy_L10_C4_B2_24():
    chon=random.randint(1,10)
    if chon==1:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_14()    
    if chon==2:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_15()
    if chon==3:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_16()
    if chon==4:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_17()
    if chon==5:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_18()
    if chon==6:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_19()
    if chon==7:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_20()
    if chon==8:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_21()
    if chon==9:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_22()
    if chon==10:
        debai_word, loigiai_word, latex_tuluan, dap_an=yy3yy_L10_C4_B2_23()

    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C4_B2_25]-M2. Cho hình thoi có cạnh và một góc. Tính S.
def yy3yy_L10_C4_B2_25():
    a=random.randint(1,7)
    ten_goc=random.choice(["\\widehat{BAD}", "\\widehat{ABC}", "\\widehat{BCD}", "\\widehat{ADC}"])
    goc=random.choice([30,45,60,120,135,150])
    goc_rad= math.radians(goc)
    noi_dung=(
    f"Cho hình thoi ${{ABCD}}$ có cạnh bằng ${{{a}}}$ và góc ${ten_goc}={goc}^\\circ$."
    f" Diện tích hình thoi đã cho bằng"
    )
    

    kq=a**2*sin(goc_rad)
    kq_f=[
    1/2*a**2*sin(goc_rad), 
    4*a**2*sin(goc_rad),
    3*a**2*sin(goc_rad)
    ]
    kq_false=[i for i in kq_f if i != kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$S_{{ABCD}}=2.{a}.{a}.\\sin {goc}^\\circ={latex(nsimplify(kq))}.$"
    )
    
    pa_A= f"*${{{latex(nsimplify(kq))}}}$"
    pa_B= f"${{{latex(nsimplify(kq2))}}}$"
    pa_C= f"${{{latex(nsimplify(kq3))}}}$"
    pa_D= f"${{{latex(nsimplify(kq4))}}}$"
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

#[D10_C4_B2_26]-M2. Cho a,b,c. Tính R.
def yy3yy_L10_C4_B2_26():
    while True:
        a,b,c=[random.randint(1,6) for i in range(3)]
        if all([a+b>c,a+c>b,b+c>a]):
            break

    noi_dung=(
    f"Cho tam giác ${{ABC}}$ có độ dài ba cạnh lần lượt là ${{{a},{b},{c}}}$."
    f" Bán kính đường tròn ngoại tiếp tam giác ${{ABC}}$ bằng (kết quả làm tròn đến hàng phần mười)"
    )

    p=(a+b+c)/2
    S=sqrt(p*(p-a)*(p-b)*(p-c))
    R=(a*b*c)/(4*S)
    

    kq=R
    kq_f=[
    (a*b*c)/(2*S),
    (a*b*c)/(S),
    S/p,
    S/(2*p)
    ]
    kq_false=[i for i in kq_f if i != kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,1):.1f}".replace(".",",")
    kq2=f"{round_half_up(kq2,1):.1f}".replace(".",",")
    kq3=f"{round_half_up(kq3,1):.1f}".replace(".",",")
    kq4=f"{round_half_up(kq4,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Ta có: $p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$.\n\n"
    f"Diện tích tam giác ${{ABC}}$:\n\n"
    f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{a}).({phan_so(p)}-{b}).({phan_so(p)}-{c})}}={latex(nsimplify(S))}$.\n\n"
    f"$S=\\dfrac{{abc}}{{4R}}\\Rightarrow R=\\dfrac{{abc}}{{4S}}=\\dfrac{{{a}.{b}.{c}}}{{4.{latex(nsimplify(S))}}}={kq}$."

    )


    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D10_C4_B2_27]-M2. Cho a,b,c. Tính r.
def yy3yy_L10_C4_B2_27():
    while True:
        a,b,c=[random.randint(1,6) for i in range(3)]
        if all([a+b>c,a+c>b,b+c>a]):
            break

    noi_dung=(
    f"Cho tam giác ${{ABC}}$ có độ dài ba cạnh lần lượt là ${{{a},{b},{c}}}$."
    f" Bán kính đường tròn nội tiếp tam giác ${{ABC}}$ bằng (kết quả làm tròn đến hàng phần mười)"
    )

    p=(a+b+c)/2
    S=sqrt(p*(p-a)*(p-b)*(p-c))
    r=S/p
    

    kq=r
    kq_f=[
    (a*b*c)/(2*S),
    (a*b*c)/(4*S),
    S/(4*p),
    S/(2*p)
    ]
    kq_false=[i for i in kq_f if i != kq]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,1):.1f}".replace(".",",")
    kq2=f"{round_half_up(kq2,1):.1f}".replace(".",",")
    kq3=f"{round_half_up(kq3,1):.1f}".replace(".",",")
    kq4=f"{round_half_up(kq4,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Ta có: $p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$.\n\n"
    f"Diện tích tam giác ${{ABC}}$:\n\n"
    f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{a}).({phan_so(p)}-{b}).({phan_so(p)}-{c})}}={latex(nsimplify(S))}$.\n\n"
    f"$S=p.r\\Rightarrow r=\\dfrac{{S}}{{p}}=\\dfrac{{{latex(nsimplify(S))}}}{{{phan_so(p)}}}={kq}$."

    )


    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D10_C4_B2_28]-M2. Cho a,b,c. Tính h.
def yy3yy_L10_C4_B2_28():
    while True:
        a,b,c=[random.randint(1,6) for i in range(3)]
        if all([a+b>c,a+c>b,b+c>a]):
            break
    chon=random.randint(1,3)

    if chon==1:
        noi_dung=(
        f"Cho tam giác ${{ABC}}$ có độ dài ba cạnh lần lượt là ${{a={a},b={b},c={c}}}$."
        f" Chiều cao xuất phát từ đỉnh ${{A}}$ của tam giác ${{ABC}}$ bằng (kết quả làm tròn đến hàng phần mười)"
        )

        p=(a+b+c)/2
        S=sqrt(p*(p-a)*(p-b)*(p-c))
        h_a=2*S/a
        h_b=2*S/b
        h_c=2*S/c    

        kq=h_a
        kq_f=[
        h_b,
        h_c,
        S/a,
        S/b,
        S/c,
        S/(2*b),
        S/(2*a),
        S/(2*c)
        ]
        kq_false=[i for i in kq_f if i != kq]
        random.shuffle(kq_false)
        kq2,kq3,kq4=kq_false[0:3]

        kq=f"{round_half_up(kq,1):.1f}".replace(".",",")
        kq2=f"{round_half_up(kq2,1):.1f}".replace(".",",")
        kq3=f"{round_half_up(kq3,1):.1f}".replace(".",",")
        kq4=f"{round_half_up(kq4,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"Ta có: $p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$.\n\n"
        f"Diện tích tam giác ${{ABC}}$:\n\n"
        f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{a}).({phan_so(p)}-{b}).({phan_so(p)}-{c})}}={latex(nsimplify(S))}$.\n\n"
        f"$S={phan_so(1/2)}a.h_a\\Rightarrow h_a=\\dfrac{{2S}}{{a}}=\\dfrac{{2.{latex(nsimplify(S))}}}{{{a}}}={kq}$.")
    
    if chon==2:
        noi_dung=(
        f"Cho tam giác ${{ABC}}$ có độ dài ba cạnh lần lượt là ${{a={a},b={b},c={c}}}$."
        f" Chiều cao xuất phát từ đỉnh ${{B}}$ của tam giác ${{ABC}}$ bằng (kết quả làm tròn đến hàng phần mười)"
        )

        p=(a+b+c)/2
        S=sqrt(p*(p-a)*(p-b)*(p-c))
        h_a=2*S/a
        h_b=2*S/b
        h_c=2*S/c    

        kq=h_b
        kq_f=[
        h_a,
        h_c,
        S/a,
        S/b,
        S/c,
        S/(2*b),
        S/(2*a),
        S/(2*c)
        ]
        kq_false=[i for i in kq_f if i != kq]
        random.shuffle(kq_false)
        kq2,kq3,kq4=kq_false[0:3]

        kq=f"{round_half_up(kq,1):.1f}".replace(".",",")
        kq2=f"{round_half_up(kq2,1):.1f}".replace(".",",")
        kq3=f"{round_half_up(kq3,1):.1f}".replace(".",",")
        kq4=f"{round_half_up(kq4,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"Ta có: $p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$.\n\n"
        f"Diện tích tam giác ${{ABC}}$:\n\n"
        f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{a}).({phan_so(p)}-{b}).({phan_so(p)}-{c})}}={latex(nsimplify(S))}$.\n\n"
        f"$S={phan_so(1/2)}b.h_b\\Rightarrow h_b=\\dfrac{{2S}}{{b}}=\\dfrac{{2.{latex(nsimplify(S))}}}{{{b}}}={kq}$.")

    if chon==3:
        noi_dung=(
        f"Cho tam giác ${{ABC}}$ có độ dài ba cạnh lần lượt là ${{a={a},b={b},c={c}}}$."
        f" Chiều cao xuất phát từ đỉnh ${{C}}$ của tam giác ${{ABC}}$ bằng (kết quả làm tròn đến hàng phần mười)"
        )

        p=(a+b+c)/2
        S=sqrt(p*(p-a)*(p-b)*(p-c))
        h_a=2*S/a
        h_b=2*S/b
        h_c=2*S/c    

        kq=h_c
        kq_f=[
        h_a,
        h_b,
        S/a,
        S/b,
        S/c,
        S/(2*b),
        S/(2*a),
        S/(2*c)
        ]
        kq_false=[i for i in kq_f if i != kq]
        random.shuffle(kq_false)
        kq2,kq3,kq4=kq_false[0:3]

        kq=f"{round_half_up(kq,1):.1f}".replace(".",",")
        kq2=f"{round_half_up(kq2,1):.1f}".replace(".",",")
        kq3=f"{round_half_up(kq3,1):.1f}".replace(".",",")
        kq4=f"{round_half_up(kq4,1):.1f}".replace(".",",")

        noi_dung_loigiai=(
        f"Ta có: $p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$.\n\n"
        f"Diện tích tam giác ${{ABC}}$:\n\n"
        f"$S=\\sqrt{{{phan_so(p)}.({phan_so(p)}-{a}).({phan_so(p)}-{b}).({phan_so(p)}-{c})}}={latex(nsimplify(S))}$.\n\n"
        f"$S={phan_so(1/2)}c.h_c\\Rightarrow h_c=\\dfrac{{2S}}{{c}}=\\dfrac{{2.{latex(nsimplify(S))}}}{{{c}}}={kq}$.")
    
    


    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D10_C4_B2_29]-M1. Nhận dạng định lí sin
def yy3yy_L10_C4_B2_29():
    noi_dung=(
    f"Cho tam giác ${{ABC}}$ có ${{BC=a, AC=b, AB=c}}$. Trong các khẳng định sau, khẳng định nào là khẳng định đúng?"
    )
    

    kq=random.choice([
        f"a^2=b^2+c^2-2bc\\cos A",
        f"b^2=a^2+c^2-2ac\\cos B",
        f"c^2=a^2+b^2-2ab\\cos C",
        ])
    kq_false=[
        f"a^2=b^2+c^2+2bc\\cos A",
        f"b^2=a^2+c^2+2ac\\cos B",
        f"c^2=a^2+b^2+2ab\\cos C",

        f"a^2=b^2+c^2-2bc\\sin A",
        f"b^2=a^2+c^2-2ac\\sin B",
        f"c^2=a^2+b^2-2ab\\sin C",

        f"a^2=b^2-c^2+2bc\\cos A",
        f"b^2=a^2-c^2+2ac\\cos B",
        f"c^2=a^2-b^2+2ab\\cos C",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${kq}$ là khẳng định đúng."
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

#[D10_C4_B2_30]-M1. Nhận dạng định lí sin
def yy3yy_L10_C4_B2_30():
    noi_dung=(
    f"Cho tam giác ${{ABC}}$ có ${{BC=a, AC=b, AB=c}}$. Trong các khẳng định sau, khẳng định nào là khẳng định đúng?"
    )
    

    kq=random.choice([
        f"\\dfrac{{a}}{{\\sin A}}=\\dfrac{{b}}{{\\sin B}}",
        f"\\dfrac{{a}}{{\\sin A}}=\\dfrac{{c}}{{\\sin C}}",
        f"\\dfrac{{b}}{{\\sin B}}=\\dfrac{{c}}{{\\sin C}}",
        ])
    kq_false=[
        f"a\\sin A = b\\sin B",
        f"b\\sin B = c\\sin C",
        f"a\\sin B = b\\sin C",
        f"a\\sin C = c\\sin B",
        f"\\dfrac{{a}}{{\\cos A}}=\\dfrac{{b}}{{\\cos B}}",
        f"\\dfrac{{b}}{{\\cos B}}=\\dfrac{{c}}{{\\cos C}}",
        f"\\dfrac{{a}}{{\\sin 2A}}=\\dfrac{{b}}{{\\sin 2B}}",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${kq}$ là khẳng định đúng."
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

#[D10_C4_B2_31]-M1. Nhận dạng công thức diện tích
def yy3yy_L10_C4_B2_31():
    noi_dung=(
    f"Cho tam giác ${{ABC}}$ có ${{BC=a, AC=b, AB=c}}$. Gọi ${{p,S,r,R}}$ lần lượt là nữa chu vi, diện tích, bán kính đường tròn nội tiếp và bán kính đường tròn ngoại tiếp của tam giác ${{ABC}}$. Trong các khẳng định sau, khẳng định nào là khẳng định đúng?"
    )
    

    kq=random.choice([
        f"S=pr",
        f"S=\\dfrac{{abc}}{{4R}}",
        f"S={phan_so(1/2)}ab\\sin C",
        f"S={phan_so(1/2)}bc\\sin A",
        f"S={phan_so(1/2)}ac\\sin B",
        f"S=\\sqrt{{p(p-a)(p-b)(p-c)}}"

        ])
    kq_false=[
    f"S=\\dfrac{{p}}{{r}}",
    f"S=\\dfrac{{abc}}{{2R}}",
    f"S={phan_so(1/2)}ab\\cos C",
    f"S={phan_so(1/2)}bc\\cos A",
    f"S={phan_so(1/2)}ac\\cos B",
    f"S=bc\\sin A",
    f"S=ab\\sin C",
    f"S=p(p-a)(p-b)(p-c)",
    f"S=\\sqrt{{(p-a)(p-b)(p-c)}}",

    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${kq}$ là khẳng định đúng."
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

#[D10_C4_B2_32]-M2. Nhận dạng công thức hỗn hợp
def yy3yy_L10_C4_B2_32():
    noi_dung=(
    f"Cho tam giác ${{ABC}}$ có ${{BC=a, AC=b, AB=c}}$. Gọi ${{p,S,r,R}}$ lần lượt là nữa chu vi, diện tích, bán kính đường tròn nội tiếp và bán kính đường tròn ngoại tiếp của tam giác ${{ABC}}$. Trong các khẳng định sau, khẳng định nào là khẳng định đúng?"
    )
    

    kq=random.choice([
        f"a^2=b^2+c^2-2bc\\cos A",
        f"b^2=a^2+c^2-2ac\\cos B",
        f"c^2=a^2+b^2-2ab\\cos C",
        f"S=pr",
        f"S=\\dfrac{{abc}}{{4R}}",
        f"S={phan_so(1/2)}ab\\sin C",
        f"S={phan_so(1/2)}bc\\sin A",
        f"S=\\sqrt{{p(p-a)(p-b)(p-c)}}",
        f"\\dfrac{{a}}{{\\sin A}}=\\dfrac{{b}}{{\\sin B}}",
        f"\\dfrac{{a}}{{\\sin A}}=\\dfrac{{c}}{{\\sin C}}",
        f"\\dfrac{{b}}{{\\sin B}}=\\dfrac{{c}}{{\\sin C}}",

        ])
    kq_false=[
    f"a^2=b^2+c^2+2bc\\cos A",
    f"b^2=a^2+c^2+2ac\\cos B",
    f"c^2=a^2+b^2+2ab\\cos C",
    f"S=\\dfrac{{p}}{{r}}",
    f"S=\\dfrac{{abc}}{{2R}}",
    f"S={phan_so(1/2)}ac\\cos B",
    f"a\\sin B = b\\sin C",
    f"a\\sin C = c\\sin B",
    f"\\dfrac{{a}}{{\\cos A}}=\\dfrac{{b}}{{\\cos B}}",
    f"\\dfrac{{b}}{{\\cos B}}=\\dfrac{{c}}{{\\cos C}}",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"${kq}$ là khẳng định đúng."
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

#[D10_C4_B2_33]-M2. Tìm khẳng định đúng về bán kính R
def yy3yy_L10_C4_B2_33():
    noi_dung=(
    f"Cho tam giác ${{ABC}}$ với $BC=a,AC=b,AB=c$. Gọi ${{R}}$ là bán kính đường tròn ngoại tiếp tam giác ${{ABC}}$."
    f" Khẳng định nào sau đây đúng"
    )
    

    kq=random.choice([f"$\\dfrac{{a}}{{\\sin A}}=2R$",
        f"$\\dfrac{{b}}{{\\sin B}}=2R$",
        f"$\\dfrac{{c}}{{\\sin C}}=2R$",
        f"$\\dfrac{{BC}}{{\\sin A}}=2R$",
        f"$\\dfrac{{AC}}{{\\sin B}}=2R$",
       f"$\\dfrac{{AB}}{{\\sin C}}=2R$",])
    kq_false=[f"$\\dfrac{{a}}{{\\cos A}}=2R$",        # sai (cos thay vì sin)
    f"$\\dfrac{{b}}{{\\tan B}}=2R$",        # sai
    f"$\\dfrac{{c}}{{\\cos C}}=2R$",        # sai
    f"$\\dfrac{{a}}{{\\sin B}}=2R$",        # sai (trộn góc khác)
    f"$\\dfrac{{b}}{{\\sin C}}=2R$",        # sai
    f"$\\dfrac{{c}}{{\\sin A}}=2R$",        # sai
    f"$\\dfrac{{a}}{{\\sin A}}=R$",         # sai (thiếu hệ số 2)
    f"$\\dfrac{{BC}}{{\\cos A}}=2R$",       # sai
    f"$\\dfrac{{AB}}{{\\sin A}}=2R$",    ]
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

#[D10_C4_B2_34]-M2. Tính bình phương đường trung tuyến
def yy3yy_L10_C4_B2_34():
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        if all([a+b>c, a+c>b, b+c>a]):
            break   
    chon=random.randint(1,3)
    
    if chon==1:
        noi_dung=(
        f" Cho tam giác ${{ABC}}$ có độ dài ba cạnh là $a={a},b={b},c={c}$."
        f" Gọi ${{m_a}}$ là độ dài đường trung tuyến xuất phát từ đỉnh ${{A}}$ của tam giác ${{ABC}}$. Tính $m_a^2$."
        )        

        kq=(b**2+c**2)/2-a**2/4
        kq_false=[
        (b**2+c**2)/2+a**2/4,
        (b**2+c**2)-a**2/4,
        (b**2+c**2)-a**2/2,
        ]
        
        noi_dung_loigiai=(
        f"$m_a^2=\\dfrac{{b^2+c^2}}{{2}}-\\dfrac{{a^2}}{{4}}=\\dfrac{{{b}^2+{c}^2}}{{2}}-\\dfrac{{{a}^2}}{{4}}={phan_so(kq)}$."
        )
    
    if chon==2:
        noi_dung=(
        f" Cho tam giác ${{ABC}}$ có độ dài ba cạnh là $a={a},b={b},c={c}$."
        f" Gọi ${{m_b}}$ là độ dài đường trung tuyến xuất phát từ đỉnh ${{B}}$ của tam giác ${{ABC}}$. Tính $m_b^2$."
        )        

        kq=(a**2+c**2)/2-b**2/4
        kq_false=[
        (a**2+c**2)/2+b**2/4,
        (a**2+c**2)-b**2/4,
        (a**2+c**2)-b**2/2,
        ]
        
        noi_dung_loigiai=(
        f"$m_b^2=\\dfrac{{a^2+c^2}}{{2}}-\\dfrac{{b^2}}{{4}}=\\dfrac{{{a}^2+{c}^2}}{{2}}-\\dfrac{{{b}^2}}{{4}}={phan_so(kq)}$."
        )

    if chon==3:
        noi_dung=(
        f" Cho tam giác ${{ABC}}$ có độ dài ba cạnh là $a={a},b={b},c={c}$."
        f" Gọi ${{m_c}}$ là độ dài đường trung tuyến xuất phát từ đỉnh ${{C}}$ của tam giác ${{ABC}}$. Tính $m_c^2$."
        )        

        kq=(a**2+b**2)/2-c**2/4
        kq_false=[
        (a**2+b**2)/2+c**2/4,
        (a**2+b**2)-c**2/4,
        (a**2+b**2)-c**2/2,
        ]
        
        noi_dung_loigiai=(
        f"$m_c^2=\\dfrac{{a^2+b^2}}{{2}}-\\dfrac{{c^2}}{{4}}=\\dfrac{{{a}^2+{b}^2}}{{2}}-\\dfrac{{{c}^2}}{{4}}={phan_so(kq)}$."
        )

    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
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

#[D10_C4_B2_35]-M2. Tính độ dài đường trung tuyến
def yy3yy_L10_C4_B2_35():
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        if all([a+b>c, a+c>b, b+c>a]):
            break

    chon=random.randint(1,3)
    
    if chon==1:
        noi_dung=(
        f" Cho tam giác ${{ABC}}$ có độ dài ba cạnh là $a={a},b={b},c={c}$."
        f" Gọi ${{m_a}}$ là độ dài đường trung tuyến xuất phát từ đỉnh ${{A}}$ của tam giác ${{ABC}}$. Tính ${{m_a}}$ (kết quả làm tròn đến hàng phần mười)."
        )        

        kq=(b**2+c**2)/2-a**2/4
        dap_an=f"{round_half_up(sqrt(kq),1):.1f}".replace(".",",")        
        
        noi_dung_loigiai=(
        f"$m_a^2=\\dfrac{{b^2+c^2}}{{2}}-\\dfrac{{a^2}}{{4}}=\\dfrac{{{b}^2+{c}^2}}{{2}}-\\dfrac{{{a}^2}}{{4}}={phan_so(kq)}$.\n\n"
        f"$m_a=\\sqrt{{{phan_so(kq)}}}={dap_an}$."
        )
    
    if chon==2:
        noi_dung=(
        f" Cho tam giác ${{ABC}}$ có độ dài ba cạnh là $a={a},b={b},c={c}$."
        f" Gọi ${{m_b}}$ là độ dài đường trung tuyến xuất phát từ đỉnh ${{B}}$ của tam giác ${{ABC}}$. Tính ${{m_b}}$ (kết quả làm tròn đến hàng phần mười)."
        )        

        kq=(a**2+c**2)/2-b**2/4
        dap_an=f"{round_half_up(sqrt(kq),1):.1f}".replace(".",",") 

        noi_dung_loigiai=(
        f"$m_b^2=\\dfrac{{a^2+c^2}}{{2}}-\\dfrac{{b^2}}{{4}}=\\dfrac{{{a}^2+{c}^2}}{{2}}-\\dfrac{{{b}^2}}{{4}}={phan_so(kq)}$.\n\n"
        f"$m_b=\\sqrt{{{phan_so(kq)}}}={dap_an}$."
        )

    if chon==3:
        noi_dung=(
        f" Cho tam giác ${{ABC}}$ có độ dài ba cạnh là $a={a},b={b},c={c}$."
        f" Gọi ${{m_c}}$ là độ dài đường trung tuyến xuất phát từ đỉnh ${{C}}$ của tam giác ${{ABC}}$. Tính $m_c$ (kết quả làm tròn đến hàng phần mười)."
        )        

        kq=(a**2+b**2)/2-c**2/4
        dap_an=f"{round_half_up(sqrt(kq),1):.1f}".replace(".",",") 
        
        noi_dung_loigiai=(
        f"$m_c^2=\\dfrac{{a^2+b^2}}{{2}}-\\dfrac{{c^2}}{{4}}=\\dfrac{{{a}^2+{b}^2}}{{2}}-\\dfrac{{{c}^2}}{{4}}={phan_so(kq)}$.\n\n"
        f"$m_c=\\sqrt{{{phan_so(kq)}}}={dap_an}$."
        )
 
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B2_36]-M2. Lấy điểm M thuộc BC. Tính AM
def yy3yy_L10_C4_B2_36():
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        if all([a+b>c, a+c>b, b+c>a]):
            break
    A,B,C=random.sample(["A","B","C"],3)
    M=random.choice(["M","N","P","I","E"])

    t=random.randint(2,4)
    noi_dung = (
    f"Cho tam giác ${{ABC}}$ có ${A}{B}={c},{B}{C}={a},{A}{C}={b}$."
    f" Gọi ${{{M}}}$ là điểm thuộc cạnh ${B}{C}$ sao cho ${B}{M}={t}{M}{C}$."
    f" Tính độ dài đoạn thẳng ${{{A}{M}}}$ (kết quả làm tròn đến hàng phần mười)."

    )
    
    cosB=(a**2+c**2-b**2)/(2*a*c)
    BM=a*t/(t+1)
    dap_an=f"{round_half_up(sqrt(c**2+BM**2-2*c*BM*cosB),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"$\\cos {B}=\\dfrac{{{a}^2+{c}^2-{b}^2}}{{2.{a}.{c}}}={phan_so(cosB)}$.\n\n"
    f"${B}{M}={phan_so(t/(t+1))}{B}{C}={phan_so(BM)}$.\n\n"
    f"${A}{M}=\\sqrt{{{c}^2+{phan_so(BM**2)}-2.{c}.{phan_so(BM)}.{phan_so(cosB)}}}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B2_37]-M2. Cho a,b, cosC. Tính diện tích tam giác.
def yy3yy_L10_C4_B2_37():
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        if all([a+b>c, a+c>b, b+c>a]):
            break
    while True:
     m=random.randint(1,6)
     n=random.randint(1,6)
     if m<n:
        break
    cosC=m/n
    sinC=sqrt(1-cosC**2)
    chon=random.randint(1,3)
    if chon==1:
        st_a, st_b, st_c, st_cosC, st_sinC = "a", "b", "c", "\\cos C", "\\sin C"
    
    if chon==2:
        st_a, st_b, st_c, st_cosC, st_sinC  = "b", "c", "a", "\\cos A", "\\sin A"

    if chon==3:
        st_a, st_b, st_c, st_cosC, st_sinC = "a", "c", "b", "\\cos B", "\\sin B"
    
    noi_dung=(
    f"Cho tam giác ${{ABC}}$ có ${st_a}={a}, {st_b}={b}, {st_cosC}={phan_so(cosC)}$."
    f" Tính diện tích tam giác ${{ABC}}$ (kết quả làm tròn đến hàng phần mười)."
    )
    
    S=1/2*a*b*sinC
    kq=f"{round_half_up(S,1):.1f}".replace(".",",")
    kq_false=[
    a*b*sinC,
    1/3*a*b*sinC,
    1/2*a*b*cosC
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq2=f"{round_half_up(kq2,1):.1f}".replace(".",",")
    kq3=f"{round_half_up(kq3,1):.1f}".replace(".",",")
    kq4=f"{round_half_up(kq4,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"${st_sinC}=\\sqrt{{1-{st_cosC}^2}}=\\sqrt{{1-{phan_so(cosC**2)}}}={latex(nsimplify(sinC))}$.\n\n"
    f"$S={phan_so(1/2)}.{a}.{b}.{latex(nsimplify(sinC))}={kq}$."
    )

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D10_C4_B2_38]-SA-M3. Cho AB,BC,AC. Tính đường cao AH (hoặc BH,CH)
def yy3yy_L10_C4_B2_38():
    while True:
        a=random.randint(1,7)
        b=random.randint(1,7)
        c=random.randint(1,7)
        if all([a+b>c, a+c>b, b+c>a]):
            break
    chon=random.randint(1,3)
    
    if chon==1:
        p=(a+b+c)/2
        S=sqrt(p*(p-a)*(p-b)*(p-c))
        r_S=f"{round_half_up(S,2):.2f}".replace(".",",")
        AH=float(2*S/a)

        if AH.is_integer():
            noi_dung = (
            f"Cho tam giác ${{ABC}}$ có ${{AB={c}, BC={a}, AC={b}}}$. Tính độ dài đường cao ${{AH}}$."
            )
            dap_an=int(AH)

            noi_dung_loigiai=(
            f"$p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$\n\n"

            f"Diện tích tam giác là:\n\n"
            f"$S=\\sqrt{{{phan_so(p)}.{phan_so(p-a)}.{phan_so(p-b)}.{phan_so(p-c)}}}={r_S}$.\n\n"
            f"$S={phan_so(1/2)}AH.BC\\Rightarrow AH=\\dfrac{{2S}}{{BC}}=\\dfrac{{2.{r_S}}}{{{a}}}={dap_an}$."
             )
        else:
            noi_dung = (
            f"Cho tam giác ${{ABC}}$ có ${{AB={c}, BC={a}, AC={b}}}$. Tính độ dài đường cao ${{AH}}$ (kết quả làm tròn đến hàng phần mười)."
            )
            dap_an=f"{round_half_up(AH,1):.1f}".replace(".",",")

            noi_dung_loigiai=(
            f"$p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$\n\n"

            f"Diện tích tam giác là:\n\n"
            f"$S=\\sqrt{{{phan_so(p)}.{phan_so(p-a)}.{phan_so(p-b)}.{phan_so(p-c)}}}={r_S}$.\n\n"
            f"$S={phan_so(1/2)}AH.BC\\Rightarrow AH=\\dfrac{{2S}}{{BC}}=\\dfrac{{2.{r_S}}}{{{a}}}={dap_an}$"
        
            )  
    
    if chon==2:
        p=(a+b+c)/2
        S=sqrt(p*(p-a)*(p-b)*(p-c))
        r_S=f"{round_half_up(S,2):.2f}".replace(".",",")
        BH=float(2*S/b)

        if BH.is_integer():
            noi_dung = (
            f"Cho tam giác ${{ABC}}$ có ${{AB={c}, BC={a}, AC={b}}}$. Tính độ dài đường cao ${{BH}}$."
            )
            dap_an=int(BH)

            noi_dung_loigiai=(
            f"$p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$\n\n"

            f"Diện tích tam giác là:\n\n"
            f"$S=\\sqrt{{{phan_so(p)}.{phan_so(p-a)}.{phan_so(p-b)}.{phan_so(p-c)}}}={r_S}$.\n\n"
            f"$S={phan_so(1/2)}BH.AC\\Rightarrow BH=\\dfrac{{2S}}{{AC}}=\\dfrac{{2.{r_S}}}{{{b}}}={dap_an}$."
             )
        else:
            noi_dung = (
            f"Cho tam giác ${{ABC}}$ có ${{AB={c}, BC={a}, AC={b}}}$. Tính độ dài đường cao ${{BH}}$ (kết quả làm tròn đến hàng phần mười)."
            )
            dap_an=f"{round_half_up(BH,1):.1f}".replace(".",",")

            noi_dung_loigiai=(
            f"$p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$\n\n"

            f"Diện tích tam giác là:\n\n"
            f"$S=\\sqrt{{{phan_so(p)}.{phan_so(p-a)}.{phan_so(p-b)}.{phan_so(p-c)}}}={r_S}$.\n\n"
            f"$S={phan_so(1/2)}BH.AC\\Rightarrow BH=\\dfrac{{2S}}{{AC}}=\\dfrac{{2.{r_S}}}{{{b}}}={dap_an}$."      
            )

    if chon==3:
        p=(a+b+c)/2
        S=sqrt(p*(p-a)*(p-b)*(p-c))
        r_S=f"{round_half_up(S,2):.2f}".replace(".",",")
        CH=float(2*S/c)

        if CH.is_integer():
            noi_dung = (
            f"Cho tam giác ${{ABC}}$ có ${{AB={c}, BC={a}, AC={b}}}$. Tính độ dài đường cao ${{CH}}$."
            )
            dap_an=int(BH)

            noi_dung_loigiai=(
            f"$p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$\n\n"

            f"Diện tích tam giác là:\n\n"
            f"$S=\\sqrt{{{phan_so(p)}.{phan_so(p-a)}.{phan_so(p-b)}.{phan_so(p-c)}}}={r_S}$.\n\n"
            f"$S={phan_so(1/2)}BH.AC\\Rightarrow CH=\\dfrac{{2S}}{{AB}}=\\dfrac{{2.{r_S}}}{{{b}}}={dap_an}$."
             )
        else:
            noi_dung = (
            f"Cho tam giác ${{ABC}}$ có ${{AB={c}, BC={a}, AC={b}}}$. Tính độ dài đường cao ${{CH}}$ (kết quả làm tròn đến hàng phần mười)."
            )
            dap_an=f"{round_half_up(CH,1):.1f}".replace(".",",")

            noi_dung_loigiai=(
            f"$p=\\dfrac{{{a}+{b}+{c}}}{{2}}={phan_so(p)}$\n\n"

            f"Diện tích tam giác là:\n\n"
            f"$S=\\sqrt{{{phan_so(p)}.{phan_so(p-a)}.{phan_so(p-b)}.{phan_so(p-c)}}}={r_S}$.\n\n"
            f"$S={phan_so(1/2)}CH.AB\\Rightarrow CH=\\dfrac{{2S}}{{AB}}=\\dfrac{{2.{r_S}}}{{{b}}}={dap_an}$."      
            )
    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B2_39]-SA-M4. Cho tam giác đều. Tính tổng khoảng cách đến 3 cạnh.
def yy3yy_L10_C4_B2_39():
    a=random.randint(4,10)
    S=a**2*sqrt(3)/4    
    d=S/a
    chon=random.randint(1,4)
    if chon==1:
        noi_dung = (
        f"Một mảnh sân hình tam giác đều có độ dài cạnh bằng ${{{a}}}$ m."
        f" Người thợ muốn đặt một vòi phun nước ở vị trí sao cho nằm trong sân. Tính tổng khoảng cách từ vòi phun nước đó đến ba cạnh của sân (kết quả làm tròn đến hàng phần mười).")
    
    if chon==2:
        noi_dung = (
        f"Một khu đất có dạng là một tam giác đều có độ dài cạnh bằng ${{{a}}}$ m."
        f" Một cột đèn được đặt bên trong khu đất. Tính tổng khoảng cách từ chân cột đèn đó đến ba cạnh của khu đất (kết quả làm tròn đến hàng phần mười).")

    if chon==3:
        noi_dung = (
        f"Một vườn cây hình tam giác đều có độ dài cạnh bằng ${{{a}}}$ m."
        f" Người quản lý muốn đặt một trụ đo độ ẩm đất ở bên trong vườn. Tính tổng khoảng cách từ trụ đo độ ẩm đến ba cạnh của khu đất (kết quả làm tròn đến hàng phần mười).")

    if chon==4:
        noi_dung = (
        f"Một vườn cây hình tam giác đều có độ dài cạnh bằng ${{{a}}}$ m."
        f" Người quản lý muốn đặt một trụ đo độ ẩm đất ở bên trong vườn. Tính tổng khoảng cách từ trụ đo độ ẩm đến ba cạnh của khu đất (kết quả làm tròn đến hàng phần mười).")    

    dap_an=f"{round_half_up(d,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Gọi ${{A,B,C}}$ là 3 đỉnh của khu đất và ${{I}}$ là chân trụ.\n\n"
    f"Gọi ${{IM,IH,IK}}$ lần lượt là các khoảng cách từ điểm ${{I}}$ đến ${{AB,BC,AC}}$.\n\n"
    f"$S_{{ABC}}=\\dfrac{{{a}^2\\sqrt{{3}} }}{{4}}={latex(S)}$.\n\n"
    f"$S_{{ABC}}=S_{{IAB}}+S_{{IBC}}+S_{{IAC}}$\n\n"
    f"$={phan_so(1/2)}IM.AB+{phan_so(1/2)}IH.BC+{phan_so(1/2)}IK.AC$\n\n"
    f"$={phan_so(1/2)}.{a}(IM+IH+IK)$\n\n"
    f"$\\Rightarrow IM+IH+IK=\\dfrac{{2S_{{ABC}}}}{{{a}}}={latex(d)}={dap_an}$."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung}\n"
    f"\\shortans[oly]{{{dap_an}}}\n\n"
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
    f"\\end{{ex}}\n")
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C4_B2_40]-TF-M4. Vật ở giữa sông. Xét Đ-S:góc B, định lí cosin, định lí sin, AB.
def yy3yy_L10_C4_B2_40():

    ten=random.choice(["Minh", "Hùng", "An", "Dũng", "Linh" ])
    vat=random.choice(["phao báo mực nước", "chiếc thuyền đánh cá bị mắc cạn", "một chiếc bè gỗ bị mắc kẹt", "một thân cây lớn trôi dạt bị mắc kẹt" ])
    AC=random.randint(20,35)
    goc_A, goc_C=random.sample([i for i in range(40,70)],2)
    goc_B=180-goc_A-goc_C
    goc_B_false=goc_B+random.randint(1,5)
    goc_B_rad=math.radians(goc_B)
    goc_C_rad= math.radians(goc_C)

    AB=AC*sin(goc_C_rad)/sin(goc_B_rad)
    AB_round=f"{round_half_up(AB,0):.0f}".replace(".",",")
    AB_false=f"{round_half_up(AB+random.randint(2,4),0):.0f}".replace(".",",")
    noi_dung = (
    f" Để đo khoảng cách từ vị trí ${{A}}$ trên bờ sông đến vị trí ${{B}}$ của {vat} gần một cù lao giữa sông, bạn {ten} đi dọc bờ sông từ vị trí ${{A}}$ đến vị trí ${{C}}$ cách ${{A}}$ một khoảng bằng ${{{AC}}}$ m và đo các góc $\\widehat{{BAC}}={goc_A}^{{\\circ}}$, $\\widehat{{BCA}}={goc_C}^{{\\circ}}$."
    f" Xét tính đúng-sai của các khẳng định sau(làm tròn kết quả đến hàng đơn vị): "
    )    
    
    kq1_T=f"*$\\widehat{{BAC}}={goc_B}$" 
    kq1_F=f"$\\widehat{{BAC}}={goc_B_false}$"

    
    HDG=f"$\\widehat{{BAC}}=180^\\circ - {goc_A}^\\circ-{goc_C}^\\circ={goc_B}^\\circ$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*$AB^2=BC^2+AC^2-{2*AC}\\cdot BC\\cdot \\cos {goc_C}^\\circ$"
    kq2_F=f"$AB^2=BC^2+AC^2-{AC}\\cdot BC\\cdot\\cos {goc_C}^\\circ$"
    
    HDG=f"$AB^2=BC^2+AC^2-2\\cdot AC\\cdot BC\\cdot\\cos C=BC^2+AC^2-{2*AC}\\cdot BC\\cos {goc_C}^\\circ$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"*$AB=\\dfrac{{AC\\sin C}}{{\\sin B}}$" 
    kq3_F=random.choice([
        f"$AB=\\dfrac{{AC\\sin B}}{{\\sin C}}$",
        f"$AB=\\dfrac{{AC\\cos B}}{{\\sin C}}$",
        f"$AB=\\dfrac{{AC\\cos C}}{{\\cos B}}$"
         ])
    
    HDG=f"$\\dfrac{{AB}}{{\\sin C}}=\\dfrac{{AC}}{{\\sin B}}\\Rightarrow AB=\\dfrac{{AC\\sin C}}{{\\sin B}}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* $AB={AB_round}$"
    kq4_F=f"$AB={AB_false}$" 
    
    HDG=f"$AB=\\dfrac{{AC\\sin C}}{{\\sin B}}=\\dfrac{{{AC}\\sin {goc_C}^\\circ }}{{\\sin {goc_B}^\\circ }}={AB_round}$."
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)

    code_hinh=(f"\\begin{{tikzpicture}}[scale=1, font=\\footnotesize,line join=round, line cap=round, >=stealth]\n\
            \\path \n\
            (0,0) coordinate (A)\n\
            (1,3) coordinate (B)\n\
            (6,0) coordinate (C)\n\
            (-3,4) coordinate (D)\n\
            (7,4) coordinate (E)\n\
            (-3,1) coordinate (F)\n\
            (7,1) coordinate (G);\n\
            \\draw[line width=.2cm] (D)--(E) (F)--(G);\n\
            \\draw[decorate,decoration={{coil,aspect=0}}](2,2.5)  -- (4,2.5);\n\
            \\draw[decorate,decoration={{coil,aspect=0}}](-2,2.5)  -- (0,2.5);\n\
            \\draw[decorate,decoration={{coil,aspect=0}}](0,3)  -- (1,3);\n\
            \\draw[decorate,decoration={{coil,aspect=0}}](2,3)  -- (3,3);\n\
            \\draw[decorate,decoration={{coil,aspect=0.4}}](1,2)  -- (2,2);\n\
            \\draw[decorate,decoration={{coil,aspect=1}}](3,2)  -- (4,2);\n\
            \\draw[decorate,decoration={{coil,aspect=0}}](1,1)  -- (2,1);\n\
            \\draw[decorate,decoration={{coil,aspect=0}}](3,1.5)  -- (4,1.5);\n\
            \\draw[decorate,decoration={{coil,aspect=0}}](4.3,1.5)  -- (5,1.5);\n\
            \\draw (A)--(C) node[midway,above left]{{${AC}$m}}\n\
            (A)--(B) (B)--(C); \n"
            f'\\draw pic[draw,double,angle radius=.15cm]{{angle=C--A--B}};\n'
            f'\\draw pic[draw,angle radius=.15cm]{{angle=B--C--A}};\n'
            f'\\foreach \\i/\\g in {{A/-90,B/90,C/-90}}\n'
            f'\\fill[black] (\\i) circle(1pt)+(\\g:4mm)node[scale=1]{{$\\i$}};\n \\end{{tikzpicture}}')
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai= f"{noi_dung}\n\n{file_name}"\
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

#[D10_C4_B2_41]-TF-M4. Quan sát đỉnh núi từ 2 điểm A,B. Xét Đ-S:góc ABC, góc ACB, AC, CH.
def yy3yy_L10_C4_B2_41():
    AB=random.randint(50,70)
    goc_A=random.randint(30,45)
    goc_ACH=90-goc_A
    goc_BCH=goc_ACH+random.randint(4,10)
    goc_B=90-goc_BCH
    goc_BAC=90-goc_A
    goc_ABC=90+goc_B

    goc_ACB=180-goc_BAC-goc_ABC
    
    goc_ABC_rad= math.radians(goc_ABC)
    goc_ACB_rad= math.radians(goc_ACB)
    goc_A_rad=math.radians(goc_A)

    AC=AB*sin(goc_ABC_rad)/sin(goc_ACB_rad)
    AC_round=f"{round_half_up(AC,1):.1f}".replace(".",",")
    AC_false=f"{round_half_up(AC+random.randint(1,3),1):.1f}".replace(".",",")

    CH=round_half_up(AC,1)*sin(goc_A_rad)
    CH_round=f"{round_half_up(CH,1):.1f}".replace(".",",")
    CH_false=f"{round_half_up(CH+random.randint(1,3),1):.1f}".replace(".",",")



    noi_dung = (
    f"Từ hai vị trí ${{A}}$, ${{B}}$ của một tòa nhà người ta quan sát đỉnh ${{C}}$ của ngọn núi. Biết rằng độ cao ${{AB}}$ bằng ${{{AB}}}$ m, phương nhìn ${{AC}}$ tạo với phương nằm ngang một góc ${goc_A}^{{\\circ}}$, phương nhìn ${{BC}}$ tạo với phương nằm ngang một góc ${goc_B}^\\circ$ (các kết quả làm tròn đến hàng phần trăm)."
    f" Xét tính đúng-sai của các khẳng định sau:"
    )    
    
    kq1_T=f"*$\\widehat{{ACB}}={goc_ACB}^\\circ$" 
    kq1_F=f"$\\widehat{{ACB}}={goc_ACB+random.randint(1,5)}^\\circ$"
    
    HDG=f"$\\widehat{{ACB}}=180^\\circ-(\\widehat{{BAC}}+\\widehat{{ABC}})=180^\\circ-({goc_BAC}^\\circ+{goc_ABC}^\\circ)={goc_ACB}^\\circ$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*$\\widehat{{ABC}}={goc_ABC}^\\circ$"
    kq2_F=f"$\\widehat{{ABC}}={goc_ABC+random.randint(3,6)}^\\circ$"
    
    HDG=f"$\\widehat{{ABC}}=90^\\circ+{goc_B}^\\circ={goc_ABC}^\\circ$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"*$AC={AC_round}$" 
    kq3_F=f"$AC={AC_false}$"
    
    HDG=(f" Ta có $\\dfrac{{AB}}{{\\sin \\widehat{{ACB}}}}=\\dfrac{{AC}}{{\\sin \\widehat{{ABC}}}}$.\n\n"
    f"Nên $AC=\\dfrac{{AB\\sin \\widehat{{ABC}}}}{{\\sin \\widehat{{ACB}}}}$"
    f"$=\\dfrac{{{AB}\\sin {goc_ABC}^\\circ }}{{\\sin {goc_ACB}^\\circ}}={AC_round}$." )

    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"*$CH={CH_round}$"
    kq4_F=f"$CH={CH_false}$" 
    
    HDG=f"$CH=AC.\\sin \\widehat{{CAH}}={AC_round}.\\sin {goc_A}^\\circ={CH_round}$."
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq2, kq1, kq3, kq4]
    #random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)

    code_hinh=f'\\begin{{tikzpicture}}[scale=1, font=\\footnotesize,line join=round, line cap=round, >=stealth]\n\
            \\path \n\
            (0,0) coordinate (E)\n\
            (1,0) coordinate (A)\n\
            (1,2) coordinate (B)\n\
            (0,2) coordinate (D)\n\
            (6,5) coordinate (C)\n\
            (6,0) coordinate (H)\n\
            (6,2) coordinate (G);\n\
            \\fill[pattern=fivepointed stars](E)--(A)--(B)--(D)--cycle;\n\
            \\draw \n\
            (E)--(A)--(B)--(D)--(E) \n\
            (E)--(H)--(C)\n\
            (C)--(B)--(G)\n\
            (C)--(A)\n\
            (A)--(B)node[midway,right]{{${AB}$}};\n\
            \\draw pic[draw,double,angle eccentricity=2,angle radius=7mm]{{angle=G--B--C}};\n\
            \\draw pic[draw,angle eccentricity=2,angle radius=4mm]{{angle=H--A--C}};\n\
            \\node at ($(A)+(0.8,0.25)$) {{${goc_A}^\\circ$}}; \n\
    \\node at ($(B)+(1,0.25)$) {{${goc_B}^\\circ$}};\n\
            \\foreach \\i/\\g in {{A/-90,B/90,C/0,H/0}}\n\
            \\fill[black] (\\i) circle(1pt)+(\\g:4mm)node[scale=1]{{$\\i$}};\n\
        \\end{{tikzpicture}}\n'
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
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choiceTFt\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {loigiai_latex} \n }}"
        f"\\end{{ex}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D10_C4_B2_42]-TF-M2. Quan sát tòa nhà từ 2 điểm A,B. Xét Đ-S: góc ABC, AC, BC, CH.
def yy3yy_L10_C4_B2_42():
    AB=random.randint(15,30)
    goc_A=random.randint(40,60)
    goc_B=goc_A-random.randint(8,15)
    goc_ACB=goc_A-goc_B

    goc_A_rad=math.radians(goc_A)
    goc_B_rad=math.radians(goc_B)
    goc_ACB_rad=math.radians(goc_ACB)

    AC=AB*sin(goc_B_rad)/sin(goc_ACB_rad)
    AC_round=f"{round_half_up(AC,1):.1f}".replace(".",",")
    AC_false=f"{round_half_up(AC+random.randint(1,3),1):.1f}".replace(".",",")

    BC=AB*sin(goc_A_rad)/sin(goc_ACB_rad)
    BC_round=f"{round_half_up(BC,1):.1f}".replace(".",",")
    BC_false=f"{round_half_up(BC+random.randint(1,3),1):.1f}".replace(".",",")
    

    noi_dung = (
    f"Hai người dân đứng cách nhau ${{{AB}}}$ m cùng nhìn lên đỉnh của một tòa nhà theo góc nhìn lần lượt là ${goc_B}^{{\\circ}}$ và ${goc_A}^{{\\circ}}$ (tham khảo hình vẽ). Kết quả làm tròn đến hàng phần chục."
    f"Xét tính đúng-sai của các khẳng định sau:")

    kq1_T=f"*Góc nhìn từ đỉnh tòa nhà về hai phía $A$ và $B$ nơi hai người đang đứng là góc $\\widehat{{ACB}}$ có số đo ${goc_ACB}^{{\\circ}}$" 
    kq1_F=f"Góc nhìn từ đỉnh tòa nhà về hai phía $A$ và $B$ nơi hai người đang đứng là góc $\\widehat{{ACB}}$ có số đo ${goc_A+goc_B}^{{\\circ}}$"
    
    HDG=f"$\\widehat{{ACB}}={goc_A}^\\circ-{goc_B}^\\circ={goc_ACB}^{{\\circ}}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*Khoảng cách từ vị trí người ${{A}}$ tới nóc của tòa nhà là ${{{AC_round}}}$ (m)"
    kq2_F=f"Khoảng cách từ vị trí người ${{A}}$ tới nóc của tòa nhà là ${{{AC_false}}}$ (m)"
    
    HDG=(f"$\\dfrac{{AB}}{{\\sin C}}=\\dfrac{{AC}}{{\\sin B}}$"
        f"$\\Rightarrow AC=\\dfrac{{AB.\\sin B}}{{\\sin C}}=\\dfrac{{{AB}.\\sin {goc_B}^\\circ }}{{\\sin {goc_ACB}^\\circ}}={AC_round}$.")
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"*Khoảng cách từ vị trí người ${{B}}$ tới nóc của tòa nhà là ${{{BC_round}}}$ (m)" 
    kq3_F=f"Khoảng cách từ vị trí người ${{B}}$ tới nóc của tòa nhà là ${{{BC_false}}}$ (m)"
    
    HDG=(f"$\\dfrac{{AB}}{{\\sin C}}=\\dfrac{{BC}}{{\\sin A}}$"
        f"$\\Rightarrow BC=\\dfrac{{AB.\\sin A}}{{\\sin C}}=\\dfrac{{{AB}.\\sin {goc_A}^\\circ }}{{\\sin {goc_ACB}^\\circ}}={BC_round}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    AC=round(AC,1)
    AC_round=f"{AC:.1f}".replace(".",",")
    CH=AC*sin(goc_A_rad)
    CH_round=f"{round_half_up(CH,1):.1f}".replace(".",",")
    CH_false=f"{round_half_up(CH+random.randint(1,3),1):.1f}".replace(".",",")

    kq4_T=f"*Chiều cao của tòa nhà là khoảng ${{{CH_round}}}$ m"
    kq4_F=f"Chiều cao của tòa nhà là khoảng ${{{CH_false}}}$ m" 
    
    HDG=f"$CH=AC.\\sin A={AC_round}.\\sin {goc_A}^\\circ={CH_round}$."
    kq4=random.choice([kq4_T, kq4_F])
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)

    code_hinh=f"\\begin{{tikzpicture}}[scale=1, font=\\footnotesize,line join=round, line cap=round, >=stealth]\n\
        \\foreach \\n in {{0,1,...,2}}\n\
        {{\n\
            \\node [rectangle,draw,minimum width=1cm,minimum height=1cm,pattern=north west lines] at (1.1*\\n cm, 0) {{}};\n\
            \\node [rectangle,draw,minimum width=1cm,minimum height=1cm,pattern=dots] at (1.1*\\n cm, 1.1) {{}};\n\
            \\node [rectangle,draw,minimum width=1cm,minimum height=1cm,pattern=north west lines] at (1.1*\\n cm, 2.1) {{}};\n\
            \\node [rectangle,draw,minimum width=1cm,minimum height=1cm,pattern=dots] at (1.1*\\n cm, 3.1) {{}};\n\
            \\node [rectangle,draw,minimum width=1cm,minimum height=1cm,pattern=north west lines] at (1.1*\\n cm, 4.1) {{}};\n\
            \\node [rectangle,draw,minimum width=1cm,minimum height=1cm,pattern=dots] at (1.1*\\n cm, 5.1) {{}};\n\
        }}\n\
        \\path \n\
        (0,0) coordinate (E)\n\
        (6,-.5) coordinate (A)\n\
        (8,-.5) coordinate (B)\n\
        (2.7,5.6) coordinate (C)\n\
        (2.7,-.5) coordinate (H);\n\
        \\draw \n\
        (H)--(B)--(C)\n\
        (C)--(A);\n\
        \\draw [<->](6,-.6)--(8,-.6)node[midway,below]{{$30$m}};\n\
        \\draw pic[draw,double,angle eccentricity=2,angle radius=5mm]{{angle=C--B--A}};\n\
        \\draw pic[draw,angle eccentricity=2,angle radius=4mm]{{angle=C--A--H}};\n\
        \\node at ($(A)-(0.8,-0.5)$) {{${goc_A}^\\circ$}};\n\
        \\node at ($(B)-(0.8,-0.5)$) {{${goc_B}^\\circ$}};    \n\
        \\foreach \\i/\\g in {{A/-90,B/-90,C/90,H/-90}}\n\
        \\fill[black] (\\i) circle(1pt)+(\\g:4mm)node[scale=1]{{$\\i$}};\n\
    \\end{{tikzpicture}}\n" 

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
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choiceTFt\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {loigiai_latex} \n }}"
        f"\\end{{ex}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an