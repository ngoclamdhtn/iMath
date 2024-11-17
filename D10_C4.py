import math
from sympy import *
import sympy as sp
import random
from fractions import Fraction #Thư viện chuyển về dạng phân thức
import my_module
#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(10000000000000))
    return m

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
        ten_canh1="b"
        ten_canh2="c"
    elif ten_goc == "B":
        ten_canh1="a"
        ten_canh2="c"
    else:
        ten_canh1="a"
        ten_canh2="b" 
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
    pa_A=f"*${{{round(kq,2):.2f}}}$".replace(".",",")
    pa_B=f"${{{round(kq2,2):.2f}}}$".replace(".",",")
    pa_C=f"${{{round(kq3,2):.2f}}}$".replace(".",",")
    pa_D=f"${{{round(kq4,2):.2f}}}$".replace(".",",")


    noi_dung=(f"Cho tam giác ${{ABC}}$ có ${ten_canh1}={a},{ten_canh2}={b},\\widehat{{{ten_goc}}}={C_degree}^\\circ$. Tính diện tích tam giác ${{ABC}}$"
    f" (kết quả làm tròn đến hàng phần trăm)."
    )#Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    st_kq=f"{round(kq,2):.2f}".replace(".",",")



    debai= f"{noi_dung}\n"             
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    dap_an=my_module.tra_ve_dap_an(list_PA)
    noi_dung_loigiai=f"$S=\\dfrac{{1}}{{2}}.{a}.{b}.\\sin {C_degree}^\\circ={st_kq}$."          
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
    #Tạo các phương án
    pa_A=f"*${{{kq:.2f}}}$".replace(".",",")
    pa_B=f"${{{kq2:.2f}}}$".replace(".",",")
    pa_C=f"${{{kq3:.2f}}}$".replace(".",",")
    pa_D=f"${{{kq4:.2f}}}$".replace(".",",")

    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho tam giác ${{ABC}}$ có ${ten_canh1}={a},{ten_canh2}={b},\\widehat{{{ten_goc}}}={C_degree}^\\circ$. Tính độ dài cạnh ${{{ten_canh3}}}$."
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
    a = random.randint(3,7)
    C_degree=random.randint(10,170)
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
    kq3=a/abs(cos(C_radian))
    kq4=a/(2*abs(cos(C_radian)))
    #Tìm công thức nghiệm và nghiệm ảo 

    #Tạo các phương án
    pa_A=f"*${{{kq:.2f}}}$".replace(".",",")
    pa_B=f"${{{kq2:.2f}}}$".replace(".",",")
    pa_C=f"${{{kq3:.2f}}}$".replace(".",",")
    pa_D=f"${{{kq4:.2f}}}$".replace(".",",")
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho tam giác ${{ABC}}$ có $\\widehat{{{ten_goc}}}={C_degree}^\\circ$ và độ dài cạnh ${{{ten_canh}}}$ bằng ${{{a}}}$. Tính bán kính ${{R}}$ của đường tròn ngoại tiếp tam giác ${{ABC}}$."
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

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},\\widehat{{{C}}}={goc_C_degree}^\\circ$. Xét tính đúng-sai của các khẳng định sau. "        
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

    noi_dung = (f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},\\widehat{{{C}}}={goc_C_degree}^\\circ$. Xét tính đúng-sai của các khẳng định sau. "        
    f"(Các kết quả làm tròn đến hàng phần trăm)"
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

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},{c}={l_c}$. Xét tính đúng-sai của các khẳng định sau."        
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

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},{b}={l_b},{c}={l_c}$. Xét tính đúng-sai của các khẳng định sau."        
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

    noi_dung = f"Cho tam giác ${{{tamgiac}}}$ có ${a}={l_a},{b}={l_b},{c}={l_c}$. Xét tính đúng-sai của các khẳng định sau."        
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

    noi_dung = f"Cho tam giác ${{ABC}}$ có ${a}={l_a},\\widehat{{{A}}}={goc_A_degree}^\\circ, \\widehat{{{B}}}={goc_B_degree}^\\circ$. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"    

    kq1_T=f"* $\\widehat{{{C}}} = {goc_C_degree}^\\circ$"
    kq1_F=f"$\\widehat{{{C}}} = {goc_C_degree_false}^\\circ$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\widehat{{{C}}}=180^\\circ-{goc_A_degree}^\\circ-{goc_B_degree}^\\circ={goc_C_degree}^\\circ$"
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
    
    goc_A_degree=random.randint(10,80)
    goc_A= math.radians(goc_A_degree)

    goc_B_degree=random.randint(10,60)
    if goc_B_degree==goc_A_degree:
        goc_B_degree=goc_B_degree+random.randint(5,10)
    goc_B= math.radians(goc_B_degree)

    goc_C_degree=180-goc_A_degree-goc_B_degree
    goc_C_degree_false=goc_A_degree+goc_B_degree
    goc_C=math.radians(goc_C_degree)

    l_c=f"{round(l_a*sin(goc_C)/sin(goc_A),2):.1f}".replace(".",",")
    l_c_false=f"{round(2*l_a*sin(goc_C)/sin(goc_C),2):.1f}".replace(".",",")

    l_b=f"{round(l_a*sin(goc_B)/sin(goc_A),2):.1f}".replace(".",",")
    l_b_false=f"{round(l_a*sin(goc_A)/sin(goc_B),2):.1f}".replace(".",",")

    HDG=f"$\\dfrac{{{b}}}{{\\sin {B}}}=\\dfrac{{{a}}}{{\\sin {A}}}\\Rightarrow {b}=\\dfrac{{{a}\\sin {B}}}{{\\sin {A}}}={l_b}$."

    noi_dung = (f"Cho tam giác ${{ABC}}$ có ${a}={l_a},\\widehat{{{A}}}={goc_A_degree}^\\circ, \\widehat{{{B}}}={goc_B_degree}^\\circ$."
        f" Độ dài cạnh ${{{c}}}$ bằng "
    )    

    kq=l_a*sin(goc_C)/sin(goc_A)
    kq2=2*l_a*sin(goc_C)/sin(goc_C)
    kq3=l_a*sin(goc_B)/sin(goc_A)
    kq4=l_a*sin(goc_A)/sin(goc_B)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

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
        f"\\shortans[oly]{{{l_b}}}\n"
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


    l_a=f"{round(l_c*sin(goc_A)/sin(goc_C),2):.1f}".replace(".",",")
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
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an



