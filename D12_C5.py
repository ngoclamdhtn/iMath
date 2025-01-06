import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
# Hàm làm tròn half-up
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

#Tạo hàm chứa chuỗi latex vecto
def vec(st):
    return f"\\overrightarrow{{{st}}}"

def vec2(A,B):
    return f"\\overrightarrow{{{A}{B}}}"

def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

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

def show_ptts(a,b):
    if a!=0:
        if b>0:
            t=f"{a}+{b}t"
        if  b==0:
            t=f"{a}"
        if b<0:
            t=f"{a}{b}t"            
        if b==1:
            t=f"{a}+t"
        if b==-1:
            t=f"{a}-t"
    else:
        if b>0:
            t=f"{b}t"
        if  b==0:
            t=f"0"
        if b<0:
            t=f"{b}t"           
        if b==1:
            t=f"t"
        if b==-1:
            t=f"t"
    return t
#Trả về dấu và giá trị số
def show_dau_value(a):
    dau=f"+{a}"
    if a<0:
        dau=f"{a}"
    return dau



#Tìm UCLN của ba số
def ucln_ba_so(a, b, c):
    if all([a!=0, b!=0, c!=0]):
        ucln_ab = math.gcd(a, b)
        ucln_abc = math.gcd(ucln_ab, c)
    else:
        ucln_abc = 1
    return ucln_abc

#Tìm tích có hướng
def tich_co_huong(a,b):
    a1, a2, a3=a[0], a[1], a[2]
    b1, b2, b3=b[0], b[1], b[2]
    c1= a2*b3-a3*b2
    c2= -(a1*b3-a3*b1)
    c3= a1*b2-a2*b1    
    return c1,c2,c3

def generate_random_vector():
    return [random.randint(-10, 10) for _ in range(3)]

def check_cross_product_nonzero(vec1, vec2):
    cross_product = [vec1[1]*vec2[2] - vec1[2]*vec2[1],
                     vec1[2]*vec2[0] - vec1[0]*vec2[2],
                     vec1[0]*vec2[1] - vec1[1]*vec2[0]]
    return all(cross_product)

# Tạo vector ngẫu nhiên cho đến khi tích vô hướng với vec1 bằng 0
def generate_orthogonal_vector(vec1):
    vec2 = generate_random_vector()
    
    while vec1[0]*vec2[0]+vec1[1]*vec2[1] +vec1[2]*vec2[2]!= 0:
        vec2 = generate_random_vector()
    return vec2

def thay_dau_congtru(st):
    ketqua=st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("+ +","+").replace("+ -","-").replace("- -","+").replace("- +","-")
    return ketqua

def tim_vecto_vuong_goc(a1, a2, a3):
    solutions = []
    limit=10
    
    # Duyệt qua các giá trị của b1, b2, b3 trong phạm vi [-limit, limit]
    for b1 in range(-limit, limit + 1):
        if b1 == 0:
            continue
        for b2 in range(-limit, limit + 1):
            if b2 == 0:
                continue
            for b3 in range(-limit, limit + 1):
                if b3 == 0:
                    continue
                if a1 * b1 + a2 * b2 + a3 * b3 == 0:
                    solutions.append((b1, b2, b3))
    ketqua=random.choice(solutions)
    b1, b2, b3 = ketqua      
    return b1,b2,b3

#BÀI 1 - PHƯƠNG TRÌNH MẶT PHẲNG
#[D12_C5_B1_01]-M1. Viết PTMP qua điểm và có véctơ pháp tuyến
def htd_25_xyz_L12_C5_B1_01():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({ten_mp})}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$"\
                f" và nhận vectơ $\\vec{{n}}=({a};{b};{c})$ làm véctơ pháp tuyến."

    kq= my_module.thay_dau_congtru(f"{latex(a*(x-x_0)+b*(y-y_0)+c*(z-z_0))}=0")
    kq2=my_module.thay_dau_congtru(f"{latex(a*(x+x_0)+b*(y+y_0)+c*(z+z_0))}=0")
    kq3=my_module.thay_dau_congtru(f"{latex(x_0*(x-a)+y_0*(y-b)+z_0*(z-c))}=0")
    kq4=my_module.thay_dau_congtru(f"{latex(a*x+b*y+c*z+x_0+y_0+z_0)}=0")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ có phương trình là:\n\n"\
        f" ${a}(x-{x_0})+{b}(y-{y_0})+{c}(z-{z_0})=0\\Leftrightarrow {kq}$.")  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_02]-M2. Viết PTMP qua điểm A và nhận vectơ BC làm véctơ pháp tuyến.
def htd_25_xyz_L12_C5_B1_02():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    x_B, y_B, z_B = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7)
    x_C, y_C, z_C = a+x_B, b+y_B, c+z_B

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_A=random.choice(["A","M", "E", "I" ])
    ten_B=random.choice(["B", "D","M", "H" ])
    ten_C=random.choice(["C", "G", "K"])
    d=-a*x_0-b*y_0-c*z_0+random.randint(1,20)

    noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({ten_mp})}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$"\
                f" và nhận vectơ $\\overrightarrow{{{ten_B}{ten_C}}}$ làm véctơ pháp tuyến với ${ten_B}({x_B};{y_B};{z_B})$ và ${ten_C}({x_C};{y_C};{z_C})$."

    kq= my_module.thay_dau_congtru(f"{latex(a*(x-x_0)+b*(y-y_0)+c*(z-z_0))}=0")
    kq2=my_module.thay_dau_congtru(f"{latex(a*(x+x_0)+b*(y+y_0)+c*(z+z_0))}=0")
    kq3=my_module.thay_dau_congtru(f"{latex(x_0*(x-a)+y_0*(y-b)+z_0*(z-c))}=0")
    kq4=my_module.thay_dau_congtru(f"{latex(a*x+b*y+c*z+d)}=0")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\overrightarrow{{{ten_B}{ten_C}}}=({a};{b};{c})$.\n\n"\
        f"Mặt phẳng ${{({ten_mp})}}$ có phương trình là:\n\n"\
        f" ${a}(x-{x_0})+{b}(y-{y_0})+{c}(z-{z_0})=0\\Leftrightarrow {kq}$.")  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_03]-M2. Viết PTMP qua điểm A và vuông góc với trục tọa độ.
def htd_25_xyz_L12_C5_B1_03():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_0 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    y_0=x_0-random.randint(1,6)
    z_0=x_0+random.randint(7,15)
    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_A=random.choice(["A","B","C", "M", "E", "I", "N"])
    chon=random.randint(1,3)
    chon=3
    if chon==1:
        a,b,c = 1,0,0
        noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({ten_mp})}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$"\
                    f" và vuông góc với trục ${{Ox}}$."

        kq= my_module.thay_dau_congtru(f"{latex(x-x_0)}=0")
        kq2=my_module.thay_dau_congtru(random.choice([f"{latex(y-y_0)}=0", f"{latex(x+y-y_0)}=0"]))
        kq3=my_module.thay_dau_congtru(random.choice([f"{latex(z-z_0)}=0", f"{latex(x+z-z_0)}=0"]))
        kq4=my_module.thay_dau_congtru(random.choice([f"{latex(y+z)}=0", f"{latex(y+z-z_0)}=0"]))

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ vuông góc với trục ${{Ox}}$ nên nhận vectơ $\\vec{{i}}=(1;0;0)$ làm véctơ pháp tuyến.\n\n"\
            f"Mặt phẳng ${{({ten_mp})}}$ có phương trình là:\n\n"\
            f" ${a}(x-{x_0})+{b}(y-{y_0})+{c}(z-{z_0})=0\\Leftrightarrow {kq}$.")
    if chon==2:
        a,b,c = 0,1,0
        noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({ten_mp})}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$"\
                    f" và vuông góc với trục ${{Oy}}$."

        kq= my_module.thay_dau_congtru(f"{latex(y-y_0)}=0")
        kq2=my_module.thay_dau_congtru(random.choice([f"{latex(x-x_0)}=0", f"{latex(x+y-y_0)}=0"]))
        kq3=my_module.thay_dau_congtru(random.choice([f"{latex(z-z_0)}=0", f"{latex(x+z-z_0)}=0"]))
        kq4=my_module.thay_dau_congtru(random.choice([f"{latex(y+z)}=0", f"{latex(y+z-z_0)}=0"]))

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ vuông góc với trục ${{Oy}}$ nên nhận vectơ $\\vec{{j}}=(0;1;0)$ làm véctơ pháp tuyến.\n\n"\
            f"Mặt phẳng ${{({ten_mp})}}$ có phương trình là:\n\n"\
            f" ${a}(x-{x_0})+{b}(y-{y_0})+{c}(z-{z_0})=0\\Leftrightarrow {kq}$.")

    if chon==3:
        a,b,c = 0,0,1
        noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({ten_mp})}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$"\
                    f" và vuông góc với trục ${{Oz}}$."

        kq= my_module.thay_dau_congtru(f"{latex(z-z_0)}=0")
        kq2=my_module.thay_dau_congtru(random.choice([f"{latex(x-x_0)}=0", f"{latex(x+y-y_0)}=0"]))
        kq3=my_module.thay_dau_congtru(random.choice([f"{latex(y-y_0)}=0", f"{latex(x+z-z_0)}=0"]))
        kq4=my_module.thay_dau_congtru(random.choice([f"{latex(y+z)}=0", f"{latex(y+z-z_0)}=0"]))

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ vuông góc với trục ${{Oz}}$ nên nhận vectơ $\\vec{{k}}=(0;0;1)$ làm véctơ pháp tuyến.\n\n"\
            f"Mặt phẳng ${{({ten_mp})}}$ có phương trình là:\n\n"\
            f" ${a}(x-{x_0})+{b}(y-{y_0})+{c}(z-{z_0})=0\\Leftrightarrow {kq}$.")

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_04]-M2. Viết PTMP qua điểm và song song với mặt phẳng
def htd_25_xyz_L12_C5_B1_04():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    mp_P=random.choice(["P", "R", "\\alpha" ])
    mp_Q=random.choice(["Q","\\beta", "\\gamma"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])

    d=-a*x_0-b*y_0-c*z_0+random.randint(1,20)


    noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({mp_P})}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$"\
                f" và song song với mặt phẳng ${{({mp_Q})}}:{latex(a*x+b*y+c*z+d)}=0$."

    kq= my_module.thay_dau_congtru(f"{latex(a*(x-x_0)+b*(y-y_0)+c*(z-z_0))}=0")
    kq2=my_module.thay_dau_congtru(f"{latex(a*(x+x_0)+b*(y+y_0)+c*(z+z_0))}=0")
    kq3=my_module.thay_dau_congtru(f"{latex(x_0*(x-a)+y_0*(y-b)+z_0*(z-c))}=0")
    kq4=my_module.thay_dau_congtru(f"{latex(a*x+b*y+c*z+d)}=0")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({mp_P})}}$ song song với ${{({mp_Q})}}$ nên nhận $\\overrightarrow{{n}}=({a};{b};{c})$ làm véctơ pháp tuyến.\n\n"\
        f"Mặt phẳng ${{({mp_P})}}$ có phương trình là:\n\n"\
        f" ${a}(x-{x_0})+{b}(y-{y_0})+{c}(z-{z_0})=0\\Leftrightarrow {kq}$.")  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_05]-M2. Viết PTMP trung trực của đoạn AB.
def htd_25_xyz_L12_C5_B1_05():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)

    x_B, y_B, z_B = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7)
    x_C, y_C, z_C = 2*x_0-x_B, 2*y_0-y_B, 2*z_0-z_B

    a, b, c = x_C-x_B, y_C-y_B, z_C-z_B

    t=ucln_ba_so(a,b,c)
    a1,b1,c1=int(a/t),int(b/t),int(c/t)


    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_B=random.choice(["A","M", "E", "B", "D"])
    ten_C=random.choice(["B", "G", "K", "H"])


    noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({ten_mp})}}$ là mặt phẳng trung trực của đoạn thẳng ${{{ten_B}{ten_C}}}$"\
                f" với ${ten_B}({x_B};{y_B};{z_B})$ và ${ten_C}({x_C};{y_C};{z_C})$."

    kq= my_module.thay_dau_congtru(f"{latex(a1*(x-x_0)+b1*(y-y_0)+c1*(z-z_0))}=0")
    kq2=my_module.thay_dau_congtru(f"{latex(a1*(x+x_0)+b1*(y+y_0)+c1*(z+z_0))}=0")
    kq3=my_module.thay_dau_congtru(f"{latex(x_0*(x-a1)+y_0*(y-b1)+z_0*(z-c1))}=0")
    kq4=my_module.thay_dau_congtru(f"{latex(a1*x+b1*y+c1*z+x_0+y_0+z_0)}=0")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\overrightarrow{{{ten_B}{ten_C}}}=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({ten_mp})}}$.\n\n"\
        f"Mặt phẳng ${{({ten_mp})}}$ qua trung điểm $I({x_0};{y_0};{z_0})$ của đoạn thẳng ${{{ten_B}{ten_C}}}$.\n\n"
        f"Mặt phẳng ${{({ten_mp})}}$ có phương trình là:\n\n"\
        f" ${a}(x-{x_0})+{b}(y-{y_0})+{c}(z-{z_0})=0\\Leftrightarrow {kq}$.")  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_06]-M3. Viết PTMP đi qua 3 điểm A,B,C.
def htd_25_xyz_L12_C5_B1_06():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_A,y_A,z_A = [random.randint(-8,8) for i in range(3)]
    if x_A ==0: x_A=random.randint(1,7)

    x_B, y_B, z_B = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7)
    x_C, y_C, z_C = [random.randint(-8,8) for i in range(3)]
    if y_C ==0: y_C=random.randint(1,7)

    if x_A==x_B==x_C: x_A=x_A+random.randint(1,3)
    if y_A==y_B==y_C: y_B=y_B+random.randint(1,3)
    if z_A==z_B==z_C: z_C=z_C+random.randint(1,3)

    if (x_B-x_A)*(y_C-y_A)==(x_C-x_A)*(y_B-y_A):
        x_B = x_B + random.randint(1,3)

    m=[x_B-x_A, y_B-y_A, z_B-z_A]
    n=[x_C-x_A, y_C-y_A, z_C-z_A]
    a, b, c = tich_co_huong(m,n)

    t=ucln_ba_so(a,b,c)
    a1,b1,c1=int(a/t),int(b/t),int(c/t)


    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_A=random.choice(["A","M", "D"])
    ten_B=random.choice(["B","N", "E"])
    ten_C=random.choice(["C", "G", "K", "H"])
    AB, AC=f"\\overrightarrow{{{ten_A}{ten_B}}}", f"\\overrightarrow{{{ten_A}{ten_C}}}"


    d1=-a1*x_A-b1*y_A-c1*z_A+random.randint(1,6)
    noi_dung= f"Trong không gian ${{Oxyz}}$, viết phương trình mặt phẳng ${{({ten_mp})}}$ đi qua ba điểm ${ten_A}({x_A};{y_A};{z_A})$, "\
                f" ${ten_B}({x_B};{y_B};{z_B})$ và ${ten_C}({x_C};{y_C};{z_C})$."

    kq= my_module.thay_dau_congtru(f"{latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A))}=0")
    kq2=my_module.thay_dau_congtru(f"{latex(a1*(x+x_A)+b1*(y+y_A)+c1*(z+z_A))}=0")
    kq3=my_module.thay_dau_congtru(f"{latex(x_A*(x-a1)+y_A*(y-b1)+z_A*(z-c1))}=0")
    kq4=my_module.thay_dau_congtru(f"{latex(a1*x+b1*y+c1*z+d1)}=0")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\overrightarrow{{{ten_A}{ten_B}}}=({x_B-x_A};{y_B-y_A};{z_B-z_A}), \\overrightarrow{{{ten_A}{ten_C}}}=({x_C-x_A};{y_C-y_A};{z_C-z_A})$.\n\n"\
        f"Mặt phẳng ${{({ten_mp})}}$ nhận $\\overrightarrow{{n}}=\\left[{AB}, {AC}\\right]=({a};{b};{c})$ làm một véctơ pháp tuyến.\n\n"
        f"Mặt phẳng ${{({ten_mp})}}$ qua điểm ${ten_A}({x_A};{y_A};{z_A})$.\n\n"
        f"Mặt phẳng ${{({ten_mp})}}$ có phương trình là:\n\n"\
        f" ${a}(x-{x_A})+{b}(y-{y_A})+{c}(z-{z_A})=0\\Leftrightarrow {kq}$.")  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_07]-M1. Tính khoảng cách từ điểm đến mặt phẳng
def htd_25_xyz_L12_C5_B1_07():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
    d = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)
    mp=latex(a*x+b*y+c*z+d)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])   
    noi_dung= f"Trong không gian ${{Oxyz}}$, cho điểm ${ten_diem}({x_0};{y_0};{z_0})$ và mặt phẳng $({ten_mp}):{mp}=0$."\
                f" Khoảng cách từ điểm ${{{ten_diem}}}$ đến mặt phẳng $({ten_mp})$ bằng"

    kq=abs(a*x_0+b*y_0+c*z_0+d)/sqrt(a**2+b**2+c**2)
    kq2=abs(a*x_0+b*y_0+c*z_0)/sqrt(a**2+b**2+c**2)
    kq3=abs(a*x_0+b*y_0+c*z_0+d)/(a**2+b**2+c**2)+random.randint(1,5)
    kq4=abs(a*x_0+b*y_0+c*z_0+d)/(a**2+b**2+c**2)

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Khoảng cách từ điểm ${{{ten_diem}}}$ đến mặt phẳng $({ten_mp})$ bằng:\n\n"\
        f"$d({ten_diem},({ten_mp})=\\dfrac{{|{show_tich(a,x_0)}+{show_tich(b,y_0)}+{show_tich(c,z_0)}+{d}|}} {{\\sqrt{{ {a**2}+{b**2}+{c**2}}} }}={latex(kq)}$")


    #Tạo các phương án
    pa_A= f"*${latex(kq)}$"
    pa_B= f"${latex(kq2)}$"
    pa_C= f"${phan_so(kq3)}$"
    pa_D= f"${phan_so(kq4)}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_08]-M2. Xét vị trí tương đối giữa 2 mặt phẳng
def htd_25_xyz_L12_C5_B1_08():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
    d = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    ten_mp1=random.choice(["(P)","(R)", f"(\\alpha)" ])
    ten_mp2=random.choice(["(Q)",  f"(\\beta)", f"(\\gamma)" ])

    chon=random.randint(1,4)
    
    #Hai mặt phẳng trùng nhau
    if chon==1:
        t2=random.choice([random.randint(-3, -1), random.randint(1, 3)])
        a2, b2, c2, d2= a*t2, b*t2, c*t2, d*t2
        mp1=latex(a*x+b*y+c*z+d)
        mp2=latex(a2*x+b2*y+c2*z+d2)      
   
        noi_dung= f"Trong không gian ${{Oxyz}}$, cho các mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng  \n\n $\\displaystyle {ten_mp2}:{mp2}=0$."\
                    f" Khẳng định nào sau đây đúng?"

        kq=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
        kq2=f"${ten_mp1}$ song song ${ten_mp2}$"
        kq3=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
        kq4=f"${ten_mp1}$ vuông góc ${ten_mp2}$"

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\dfrac{{{a}}}{{{a2}}}=\\dfrac{{{b}}}{{{b2}}}=\\dfrac{{{c}}}{{{c2}}}=\\dfrac{{{d}}}{{{d2}}}$"\
        f" nên {kq}.")

    #Hai mặt phẳng song song    
    if chon==2:
        t2=random.choice([random.randint(-3, -1), random.randint(1, 3)])
        a2, b2, c2, d2= a*t2, b*t2, c*t2, d*t2+random.randint(1,6)
        mp1=latex(a*x+b*y+c*z+d)
        mp2=latex(a2*x+b2*y+c2*z+d2)      
   
        noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng  \n\n $\\displaystyle {ten_mp2}:{mp2}=0$."\
                    f" Khẳng định nào sau đây đúng?"

        kq=f"${ten_mp1}$ song song ${ten_mp2}$"
        kq2=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
        kq3=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
        kq4=f"${ten_mp1}$ vuông góc ${ten_mp2}$"

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\dfrac{{{a}}}{{{a2}}}=\\dfrac{{{b}}}{{{b2}}}=\\dfrac{{{c}}}{{{c2}}}\\ne \\dfrac{{{d}}}{{{d2}}}$"\
        f" nên {kq}.")
    #Hai mặt phẳng vuông góc
    if chon==3:
        vec1 = generate_random_vector()
        # Tạo vector thứ hai có tích vô hướng bằng 0 với vector đầu tiên
        vec2 = generate_orthogonal_vector(vec1)
        a, b, c, d= vec1[0], vec1[1], vec1[2], random.randint(-10,10)
        a2, b2, c2, d2=vec2[0], vec2[1], vec2[2], random.randint(-10,10)
        mp1=latex(a*x+b*y+c*z+d)
        mp2=latex(a2*x+b2*y+c2*z+d2)      
   
        noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng  \n\n $\\displaystyle {ten_mp2}:{mp2}=0$."\
                    f" Khẳng định nào sau đây đúng?"

        kq=f"${ten_mp1}$ vuông góc ${ten_mp2}$"
        kq2=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
        kq3=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
        kq4=f"${ten_mp1}$ song song ${ten_mp2}$"

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: ${show_tich(a,a2)}+{show_tich(b,b2)}+{show_tich(c,c2)}=0$ nên {kq}."\
        f" nên {kq}.")

    #Hai mặt phẳng cắt nhưng không vuông góc
    
    if chon==4:
        vec1 = generate_random_vector()
        # Tạo vector thứ hai có tích vô hướng bằng 0 với vector đầu tiên
        vec2 = generate_orthogonal_vector(vec1)
        a, b, c, d= vec1[0], vec1[1], vec1[2], random.randint(-10,10)
        a2, b2, c2, d2=vec2[0], vec2[1]+1, vec2[2], random.randint(-10,10)
        mp1=latex(a*x+b*y+c*z+d)
        mp2=latex(a2*x+b2*y+c2*z+d2)      
   
        noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng  \n\n $\\displaystyle {ten_mp2}:{mp2}=0$."\
                    f" Khẳng định nào sau đây đúng?"

        kq=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
        kq2=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
        kq3=f"${ten_mp1}$ vuông góc ${ten_mp2}$"
        kq4=f"${ten_mp1}$ song song ${ten_mp2}$"

        noi_dung_loigiai=my_module.thay_dau_congtru(f"${ten_mp1}$ có véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({a};{b};{c})$, "\
            f"${ten_mp2}$ có véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({a2};{b2};{c2})$.\n\n"\
            f"$\\overrightarrow{{n_1}}$ và $\\overrightarrow{{n_2}}$ khác phương nên ${ten_mp1}$ cắt ${ten_mp2}$.\n\n"\
            f"Ta có: ${show_tich(a,a2)}+{show_tich(b,b2)}+{show_tich(c,c2)}\\ne 0$ nên {kq}.")

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
        #f"{file_name}\n"
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

#[D12_C5_B1_09]-M2. Xét vị trí tương đối giữa 2 mặt phẳng. Kết quả trùng nhau
def htd_25_xyz_L12_C5_B1_09():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
    d = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    ten_mp1=random.choice(["(P)","(R)", f"(\\alpha)" ])
    ten_mp2=random.choice(["(Q)",  f"(\\beta)", f"(\\gamma)" ])  
    
    
    t2=random.choice([random.randint(-3, -1), random.randint(1, 3)])
    a2, b2, c2, d2= a*t2, b*t2, c*t2, d*t2
    mp1=latex(a*x+b*y+c*z+d)
    mp2=latex(a2*x+b2*y+c2*z+d2)      

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng \n\n $\\displaystyle {ten_mp2}:{mp2}=0$."\
                f" Khẳng định nào sau đây đúng?"

    kq=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
    kq2=f"${ten_mp1}$ song song ${ten_mp2}$"
    kq3=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
    kq4=f"${ten_mp1}$ vuông góc ${ten_mp2}$"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\dfrac{{{a}}}{{{a2}}}=\\dfrac{{{b}}}{{{b2}}}=\\dfrac{{{c}}}{{{c2}}}=\\dfrac{{{d}}}{{{d2}}}$"\
    f" nên {kq}.")

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
        #f"{file_name}\n"
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

#[D12_C5_B1_10]-M2. Xét vị trí tương đối giữa 2 mặt phẳng. KQ: song song
def htd_25_xyz_L12_C5_B1_10():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
    d = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    ten_mp1=random.choice(["(P)","(R)", f"(\\alpha)" ])
    ten_mp2=random.choice(["(Q)",  f"(\\beta)", f"(\\gamma)" ])   


    t2=random.choice([random.randint(-3, -1), random.randint(1, 3)])
    a2, b2, c2, d2= a*t2, b*t2, c*t2, d*t2+random.randint(1,6)
    if d2==d:d2=d2+random.randint(1,5)
    mp1=latex(a*x+b*y+c*z+d)
    mp2=latex(a2*x+b2*y+c2*z+d2)      

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng ${ten_mp2}:{mp2}=0$."\
                f" Khẳng định nào sau đây đúng?"

    kq=f"${ten_mp1}$ song song ${ten_mp2}$"
    kq2=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
    kq3=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
    kq4=f"${ten_mp1}$ vuông góc ${ten_mp2}$"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\dfrac{{{a}}}{{{a2}}}=\\dfrac{{{b}}}{{{b2}}}=\\dfrac{{{c}}}{{{c2}}}\\ne \\dfrac{{{d}}}{{{d2}}}$"\
    f" nên {kq}.")    

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
        #f"{file_name}\n"
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

#[D12_C5_B1_1]-M2. Xét vị trí tương đối giữa 2 mặt phẳng. KQ: vuông góc
def htd_25_xyz_L12_C5_B1_11():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
    d = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    ten_mp1=random.choice(["(P)","(R)", f"(\\alpha)" ])
    ten_mp2=random.choice(["(Q)",  f"(\\beta)", f"(\\gamma)" ])

    vec1 = generate_random_vector()
    # Tạo vector thứ hai có tích vô hướng bằng 0 với vector đầu tiên
    vec2 = generate_orthogonal_vector(vec1)
    a, b, c, d= vec1[0], vec1[1], vec1[2], random.randint(-10,10)
    a2, b2, c2, d2=vec2[0], vec2[1], vec2[2], random.randint(-10,10)
    mp1=latex(a*x+b*y+c*z+d)
    mp2=latex(a2*x+b2*y+c2*z+d2)      

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng ${ten_mp2}:{mp2}=0$."\
                f" Khẳng định nào sau đây đúng?"

    kq=f"${ten_mp1}$ vuông góc ${ten_mp2}$"
    kq2=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
    kq3=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
    kq4=f"${ten_mp1}$ song song ${ten_mp2}$"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: ${show_tich(a,a2)}+{show_tich(b,b2)}+{show_tich(c,c2)}=0$ nên {kq}."\
    f" nên {kq}.")
   

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
        #f"{file_name}\n"
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

#[D12_C5_B1_12]-M2. Xét vị trí tương đối giữa 2 mặt phẳng. KQ: cắt và không vuông góc
def htd_25_xyz_L12_C5_B1_12():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
    d = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    ten_mp1=random.choice(["(P)","(R)", f"(\\alpha)" ])
    ten_mp2=random.choice(["(Q)",  f"(\\beta)", f"(\\gamma)" ])   
    

    vec1 = generate_random_vector()
    # Tạo vector thứ hai có tích vô hướng bằng 0 với vector đầu tiên
    vec2 = generate_orthogonal_vector(vec1)
    a, b, c, d= vec1[0], vec1[1], vec1[2], random.randint(-10,10)
    a2, b2, c2, d2=vec2[0], vec2[1]+1, vec2[2], random.randint(-10,10)
    mp1=latex(a*x+b*y+c*z+d)
    mp2=latex(a2*x+b2*y+c2*z+d2)      

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng ${ten_mp2}:{mp2}=0$."\
                f" Khẳng định nào sau đây đúng?"

    kq=f"${ten_mp1}$ và ${ten_mp2}$ cắt và không vuông góc"
    kq2=f"${ten_mp1}$ và ${ten_mp2}$ trùng nhau"
    kq3=f"${ten_mp1}$ vuông góc ${ten_mp2}$"
    kq4=f"${ten_mp1}$ song song ${ten_mp2}$"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"${ten_mp1}$ có véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({a};{b};{c})$, "\
        f"${ten_mp2}$ có véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({a2};{b2};{c2})$.\n\n"\
        f"$\\overrightarrow{{n_1}}$ và $\\overrightarrow{{n_2}}$ khác phương nên ${ten_mp1}$ cắt ${ten_mp2}$.\n\n"\
        f"Ta có: ${show_tich(a,a2)}+{show_tich(b,b2)}+{show_tich(c,c2)}\\ne 0$ nên {kq}.")

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
        #f"{file_name}\n"
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

#[D12_C5_B1_13]-M2. Tính khoảng cách giữa 2 mặt phẳng song song
def htd_25_xyz_L12_C5_B1_13():
    #Tạo bậc ngẫu nhiên
   #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
    d = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    ten_mp1=random.choice(["(P)","(R)", f"(\\alpha)" ])
    ten_mp2=random.choice(["(Q)",  f"(\\beta)", f"(\\gamma)" ])   


    t2=random.choice([random.randint(-3, -1), random.randint(1, 3)])
    t3=random.randint(1,6)
    a2, b2, c2, d2= a*t2, b*t2, c*t2, d*t2+t3
    m=(d*t2+t3)/t2
    mp1=latex(a*x+b*y+c*z+d)
    mp2=latex(a2*x+b2*y+c2*z+d2)    

  
    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng ${ten_mp2}:{mp2}=0$."\
                f" Khoảng cách giữa hai mặt phẳng đã cho bằng"

    kq=abs(t3/(t2*sqrt(a**2+b**2+c**2)))
    kq2=abs(d+d2)/sqrt(a**2+b**2+c**2)
    kq3=abs(d+d2)/(abs(a)+abs(b)+abs(c))
    kq4=abs(d-m)/(abs(a)+abs(b)+abs(c))

    noi_dung_loigiai=my_module.thay_dau_congtru(
        f"${ten_mp2}:{latex(a*x+b*y+c*z)}+{phan_so(m)}=0$.\n\n"\
        f"Ta thấy hai mặt phẳng đã cho song song nhau.\n\n"\
        f"Khoảng cách giữa hai mặt phẳng đã cho bằng:\n\n"\
        f"$d({ten_mp1},{ten_mp2})=\\dfrac{{|{d}-{phan_so(m)}|}} {{\\sqrt{{ {a**2}+{b**2}+{c**2}}} }}={latex(kq)}$").replace("--","-")


    #Tạo các phương án
    pa_A= f"*${latex(kq)}$"
    pa_B= f"${latex(kq2)}$"
    pa_C= f"${phan_so(kq3)}$"
    pa_D= f"${phan_so(kq4)}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_14]-M1. Cho PTMP, đọc véctơ pháp tuyến
def htd_25_xyz_L12_C5_B1_14():
    #Tạo bậc ngẫu nhiê
    x,y,z=sp.symbols("x y z")
    chon=random.randint(1,3)
    if chon==1:
        a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
        d=random.randint(-20,20)

        t=ucln_ba_so(a,b,c)
        a,b,c=int(a/t),int(b/t),int(c/t)
       
        ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])    
        mp=latex(a*x+b*y+c*z+d)    


        noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({ten_mp})}}$ có phương trình ${mp}=0$."\
                    f" Mặt phẳng ${{({ten_mp})}}$ nhận vectơ nào trong các vectơ sau làm véctơ pháp tuyến."
        t1 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
        n=["n_1", "n_2", "n_3", "n_4"]
        random.shuffle(n)

        kq=f"\\overrightarrow{{{n[0]}}}=({t1*a};{t1*b};{t1*c})"
        kq2=f"\\overrightarrow{{{n[0]}}}=({a};{-b};{c})"
        kq3=f"\\overrightarrow{{{n[0]}}}=({b};{c};{d})"
        kq4=f"\\overrightarrow{{{n[0]}}}=({t1*a};{-b};{c})"
        if t1!=1:
            noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b};{c})$.\n\n"\
            f" nên cũng nhận vectơ ${kq}$ làm véctơ pháp tuyến.")
        else:
            noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b};{c})$.\n")
    
    if chon==2:
        a = 0
        b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
        d=random.randint(-20,20)

        t=math.gcd(b,c)
        a,b,c=0,int(b/t),int(c/t)
       
        ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])    
        mp=latex(a*x+b*y+c*z+d)    


        noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({ten_mp})}}$ có phương trình ${mp}=0$."\
                    f" Mặt phẳng ${{({ten_mp})}}$ nhận vectơ nào trong các vectơ sau làm véctơ pháp tuyến."
        t1 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
        n=["n_1", "n_2", "n_3", "n_4"]
        random.shuffle(n)

        kq=f"\\overrightarrow{{{n[0]}}}=(0;{t1*b};{t1*c})"
        kq2=f"\\overrightarrow{{{n[0]}}}=(0;{-b};{c})"
        kq3=f"\\overrightarrow{{{n[0]}}}=({b};0;{d})"
        kq4=f"\\overrightarrow{{{n[0]}}}=({b};{c};{d})"
        if t1!=1:
            noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b};{c})$.\n\n"\
            f" Do đó, mặt phẳng ${{({ten_mp})}}$ cũng nhận vectơ ${kq}$ làm véctơ pháp tuyến.")
        else:
            noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b};{c})$.\n")
    
    if chon==3:
        a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        b = 0        
        c = random.choice([random.randint(-9, -1), random.randint(1, 9)])
        d=random.randint(-20,20)

        t=math.gcd(a,c)
        a,b,c=int(a/t),0,int(c/t)
       
        ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])    
        mp=latex(a*x+b*y+c*z+d)    


        noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({ten_mp})}}$ có phương trình ${mp}=0$."\
                    f" Mặt phẳng ${{({ten_mp})}}$ nhận vectơ nào trong các vectơ sau làm véctơ pháp tuyến."
        t1 = random.choice([random.randint(-4, -1), random.randint(1, 4)])
        n=["n_1", "n_2", "n_3", "n_4"]
        random.shuffle(n)

        kq=f"\\overrightarrow{{{n[0]}}}=({t1*a};0;{t1*c})"
        kq2=f"\\overrightarrow{{{n[0]}}}=({-a};0;{c})"
        kq3=f"\\overrightarrow{{{n[0]}}}=({a};0;{d})"
        kq4=f"\\overrightarrow{{{n[0]}}}=({a};{b};{d})"
        if t1!=1:
            noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b};{c})$.\n\n"\
            f" Do đó, mặt phẳng ${{({ten_mp})}}$ cũng nhận vectơ ${kq}$ làm véctơ pháp tuyến.")
        else:
            noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{({ten_mp})}}$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b};{c})$.\n")


    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_15]-M2. Cho PTMP, tìm điểm thuộc mặt phẳng 
def htd_25_xyz_L12_C5_B1_15():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_A,y_A,z_A = [random.randint(-7,7) for i in range(3)]
    if x_A ==0: x_A=random.randint(1,7)

    x_B, y_B, z_B = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7)
    x_C, y_C, z_C = [random.randint(-8,8) for i in range(3)]
    if y_C ==0: y_C=random.randint(1,7)

    if x_A==x_B==x_C: x_A=x_A+random.randint(1,3)
    if y_A==y_B==y_C: y_B=y_B+random.randint(1,3)
    if z_A==z_B==z_C: z_C=z_C+random.randint(1,3)

    if (x_B-x_A)*(y_C-y_A)==(x_C-x_A)*(y_B-y_A):
        x_B = x_B + random.randint(1,3)

    m=[x_B-x_A, y_B-y_A, z_B-z_A]
    n=[x_C-x_A, y_C-y_A, z_C-z_A]
    a, b, c = tich_co_huong(m,n)

    t=ucln_ba_so(a,b,c)
    a1,b1,c1=int(a/t),int(b/t),int(c/t)


    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_A=random.choice(["A","M", "D"])
    ten_B=random.choice(["B","N", "E"])
    ten_C=random.choice(["C", "G", "I"])
    ten_D=random.choice(["D", "K", "H"])    
    mp=latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A))

    d1=-a1*x_A-b1*y_A-c1*z_A+random.randint(1,6)
    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({ten_mp})}}$ có phương trình ${mp}=0$."\
                f" Điểm nào trong các điểm sau thuộc mặt phẳng ${{({ten_mp})}}$?"

    kq=f"{ten_A}({x_A};{y_A};{z_A})"
    kq2=f"{ten_B}({x_B};{y_B};{-z_B})"
    kq3=f"{ten_C}({-x_C};{-y_C};{z_C})"
    kq4=f"{ten_D}({x_A+x_B};{y_C};{z_A+z_B})"


    noi_dung_loigiai=my_module.thay_dau_congtru(f"Thay tọa độ các điểm vào phương trình mặt phẳng ${{({ten_mp})}}$"
        f"ta thấy chỉ có điểm ${ten_A}({x_A};{y_A};{z_A})$ thỏa mãn.\n")  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_16]-M2. Cho PTMP, tìm điểm không thuộc mặt phẳng 
def htd_25_xyz_L12_C5_B1_16():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_A,y_A,z_A = [random.randint(-7,7) for i in range(3)]
    if x_A ==0: x_A=random.randint(1,7)

    x_B, y_B, z_B = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7)
    x_C, y_C, z_C = [random.randint(-8,8) for i in range(3)]
    if y_C ==0: y_C=random.randint(1,7)

    if x_A==x_B==x_C: x_A=x_A+random.randint(1,3)
    if y_A==y_B==y_C: y_B=y_B+random.randint(1,3)
    if z_A==z_B==z_C: z_C=z_C+random.randint(1,3)

    if (x_B-x_A)*(y_C-y_A)==(x_C-x_A)*(y_B-y_A):
        x_B = x_B + random.randint(1,3)

    m=[x_B-x_A, y_B-y_A, z_B-z_A]
    n=[x_C-x_A, y_C-y_A, z_C-z_A]
    a, b, c = tich_co_huong(m,n)

    t=ucln_ba_so(a,b,c)
    a1,b1,c1=int(a/t),int(b/t),int(c/t)


    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_A=random.choice(["A","M", "D"])
    ten_B=random.choice(["B","N", "E"])
    ten_C=random.choice(["C", "G", "I"])
    ten_D=random.choice(["D", "K", "H"])    
    mp=latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A))

    d1=-a1*x_A-b1*y_A-c1*z_A+random.randint(1,6)
    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({ten_mp})}}$ có phương trình ${mp}=0$."\
                f" Điểm nào trong các điểm sau không thuộc mặt phẳng ${{({ten_mp})}}$?"

    kq=f"{ten_A}({x_A+random.randint(1,3)};{y_C};{z_B})"
    kq2=f"{ten_B}({x_B};{y_B};{z_B})"
    kq3=f"{ten_C}({x_C};{y_C};{z_C})"
    kq4=f"{ten_D}({x_A};{y_A};{z_A})"


    noi_dung_loigiai=my_module.thay_dau_congtru(f"Thay tọa độ các điểm vào phương trình mặt phẳng ${{({ten_mp})}}$"
        f"ta thấy điểm ${ten_A}({x_A};{y_A};{z_A})$ không thỏa mãn phương trình nên điểm ${{{ten_A}}}$ không thuộc mặt phẳng ${{({ten_mp})}}$.\n")  

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_17]-M2. Viết phương trình mặt phẳng đoạn chắn
def htd_25_xyz_L12_C5_B1_17():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if a==b==c: 
        a=a+2
        b=b+3

    ten_mp=random.choice(["P","Q", "R", "\\alpha","\\beta" ])
    ten_A=random.choice(["A","M", "D"])
    ten_B=random.choice(["B","N", "E"])
    ten_C=random.choice(["C", "G", "I"])
    ten_D=random.choice(["D", "K", "H"])    

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({ten_mp})}}$ đi qua ba điểm ${ten_A}({a};0;0), {ten_B}(0;{b};0), {ten_C}(0;0;{c})$."\
                f" Phương trình mặt phẳng ${{({ten_mp})}}$ là"

    kq=thay_dau_congtru(f"\\dfrac{{x}}{{{a}}}+\\dfrac{{y}}{{{b}}}+\\dfrac{{z}}{{{c}}}=1")
    kq2=thay_dau_congtru(f"\\dfrac{{x}}{{{a}}}+\\dfrac{{y}}{{{b}}}+\\dfrac{{z}}{{{c}}}=0")
    kq3=thay_dau_congtru(f"{latex(a*x+b*y+c*z)}=0")
    kq4=thay_dau_congtru(f"{latex(a*x+b*y+c*z)}=1")


    noi_dung_loigiai=my_module.thay_dau_congtru(f"Phương trình mặt phẳng là: ${kq}$.")


    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B1_18]-M2. Cho mặt phẳng. Xét Đ-S: VTPT, điểm thuộc mp, khoảng cách, góc giữa 2 mp
def htd_25_xyz_L12_C5_B1_18():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_A,y_A,z_A = [random.randint(-5,5) for i in range(3)]
    if x_A ==0: x_A=random.randint(1,5)

    x_B, y_B, z_B = random.randint(-3,3),random.randint(-4,4),random.randint(-3,3)
    x_C, y_C, z_C = [random.randint(-4,4) for i in range(3)]
    if y_C ==0: y_C=random.randint(1,5)

    if x_A==x_B==x_C: x_A=x_A+random.randint(1,3)
    if y_A==y_B==y_C: y_B=y_B+random.randint(1,3)
    if z_A==z_B==z_C: z_C=z_C+random.randint(1,3)

    if (x_B-x_A)*(y_C-y_A)==(x_C-x_A)*(y_B-y_A):
        x_B = x_B + random.randint(1,3)

    while True:
        x_I, y_I, z_I = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7) 
        if all([x_I!=x_A, x_I!=x_B, x_I!=x_C,y_I!=y_A, y_I!=y_B, y_I!=y_C]):
            break


    m=[x_B-x_A, y_B-y_A, z_B-z_A]
    n=[x_C-x_A, y_C-y_A, z_C-z_A]
    a, b, c = tich_co_huong(m,n)

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)


    ten_mp=["P","Q", "R", "\\alpha","\\beta", "\\gamma"]
    random.shuffle(ten_mp)
    mp_P, mp_Q=ten_mp[0:2]

    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,I=ten_diem[0:4]   
    ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A))
    d=-a*x_A-b*y_A-c*z_A
    
    noi_dung= (f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({mp_P})}}$ có phương trình ${ptmp_P}=0$."
                f" Xét tính đúng-sai của các khẳng định sau")
    k=random.choice([i for i in range(-2, 2) if i!=0])
    chon=random.randint(1,2)
    if chon==1:
        kq1_T=f"* ${vec("n")}=({k*a};{k*b};{k*c})$ là một véctơ pháp tuyến của ${{({mp_P})}}$" 
        kq1_F=f"${vec("n")}=({k*a};{k*b};{k*c})$ không phải là một véctơ pháp tuyến của ${{({mp_P})}}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${vec("n")}=({k*a};{k*b};{k*c})$ là một véctơ pháp tuyến của ${{({mp_P})}}$"

    if chon==2:
        t=random.randint(1,2)
        kq1_T=f"* ${vec("n")}=({k*a};{k*b};{k*c+t})$ không là một véctơ pháp tuyến của ${{({mp_P})}}$" 
        kq1_F=f"${vec("n")}=({k*a};{k*b};{k*c+t})$ là một véctơ pháp tuyến của ${{({mp_P})}}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${vec("n")}=({k*a};{k*b};{k*c+t})$ không là một véctơ pháp tuyến của ${{({mp_P})}}$."
    
    
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc mặt phẳng ${{({mp_P})}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc mặt phẳng ${{({mp_P})}}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Tọa độ điểm ${{{A}}}({x_A};{y_A};{z_A})$ thỏa mãn phương trình ${ptmp_P}=0$ nên điểm ${{{A}}}$ thuộc mặt phẳng ${{({mp_P})}}$."
    
    if chon==2:
        t=random.randint(1,2)
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+t})$ không thuộc mặt phẳng ${{({mp_P})}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A+t})$ thuộc mặt phẳng ${{({mp_P})}}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Tọa độ điểm ${{{A}}}({x_A};{y_A};{z_A})$ không thỏa mãn phương trình ${ptmp_P}=0$ nên điểm ${{{A}}}$ không thuộc mặt phẳng ${{({mp_P})}}$."
    

    
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    khoang_cach=latex(nsimplify(abs(a*x_I+b*y_I+c*z_I+d)/sqrt(a**2+b**2+c**2)))
    khoang_cach_false=latex(nsimplify(abs(a*x_I+b*y_I+c*z_I+d+random.randint(1,2))/sqrt(a**2+b**2+c**2)))


    kq3_T=f"* Khoảng cách từ điểm ${I}({x_I};{y_I};{z_I})$ đến mặt phẳng ${{({mp_P})}}$ bằng ${khoang_cach}$" 
    kq3_F=f"Khoảng cách từ điểm ${I}({x_I};{y_I};{z_I})$ đến mặt phẳng ${{({mp_P})}}$ bằng ${khoang_cach_false}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$d\\left({I},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_I)}+{show_tich(b,y_I)}+{show_tich(c,z_I)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a1,b1,c1=[random.choice([i for i in range(-5, 6) if i!=0]) for _ in range(3)]
    d1=random.randint(-5,5)

    cos_goc=abs(a*a1+b*b1+c*c1)/(sqrt(a**2+b**2+c**2)*sqrt(a1**2+b1**2+c1**2))
    goc=acos(cos_goc)
    goc_degree=f"{round_half_up(math.degrees(goc),1):.1f}".replace(".",",")
    goc_degree_false=f"{round_half_up(math.degrees(goc)+random.randint(1,2),1):.1f}".replace(".",",")

    kq4_T=f"* Góc giữa mặt phẳng ${{({mp_P})}}$ và mặt phẳng ${{({mp_Q})}}:{latex(a1*x+b1*y+c1*z+d1)}=0$ bằng ${goc_degree}^\\circ$"
    kq4_F=f"Góc giữa mặt phẳng ${{({mp_P})}}$ và mặt phẳng ${{({mp_Q})}}:{latex(a1*x+b1*y+c1*z+d1)}=0$ bằng ${goc_degree}^\\circ$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"${vec(f"n_{mp_P}")}=({a};{b};{c}), {vec(f"n_{mp_Q}")}=({a1};{b1};{c1})$.\n\n"
        f"$\\cos({mp_P},{mp_Q})=\\dfrac{{|{show_tich(a,a1)}+{show_tich(b,b1)}+{show_tich(c,c1)}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}.\\sqrt{{{a1**2}+{b1**2}+{c1**2}}} }}$"
        f"$={latex(nsimplify(cos_goc))}$.\n\n"
        f"$\\Rightarrow ({mp_P},{mp_Q})={goc_degree}^\\circ$."
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

#[D12_C5_B1_19]-M2. Cho mặt phẳng. Xét Đ-S: VTPT, điểm thuộc mp, khoảng cách, phương trình mặt phẳng song song
def htd_25_xyz_L12_C5_B1_19():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_A,y_A,z_A = [random.randint(-5,5) for i in range(3)]
    if x_A ==0: x_A=random.randint(1,5)

    x_B, y_B, z_B = random.randint(-3,3),random.randint(-4,4),random.randint(-3,3)
    x_C, y_C, z_C = [random.randint(-4,4) for i in range(3)]
    if y_C ==0: y_C=random.randint(1,5)

    if x_A==x_B==x_C: x_A=x_A+random.randint(1,3)
    if y_A==y_B==y_C: y_B=y_B+random.randint(1,3)
    if z_A==z_B==z_C: z_C=z_C+random.randint(1,3)

    if (x_B-x_A)*(y_C-y_A)==(x_C-x_A)*(y_B-y_A):
        x_B = x_B + random.randint(1,3)

    while True:
        x_I, y_I, z_I = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7) 
        if all([x_I!=x_A, x_I!=x_B, x_I!=x_C,y_I!=y_A, y_I!=y_B, y_I!=y_C]):
            break


    m=[x_B-x_A, y_B-y_A, z_B-z_A]
    n=[x_C-x_A, y_C-y_A, z_C-z_A]
    a, b, c = tich_co_huong(m,n)

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)


    ten_mp=["P","Q", "R", "\\alpha","\\beta", "\\gamma"]
    random.shuffle(ten_mp)
    mp_P, mp_Q=ten_mp[0:2]

    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,I,M=ten_diem[0:5]   
    ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A))
    d=-a*x_A-b*y_A-c*z_A
    
    noi_dung= (f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({mp_P})}}$ có phương trình ${ptmp_P}=0$."
                f" Xét tính đúng-sai của các khẳng định sau")
    k=random.choice([i for i in range(-2, 2) if i!=0])
    chon=random.randint(1,2)
    if chon==1:
        kq1_T=f"* ${vec("n")}=({k*a};{k*b};{k*c})$ là một véctơ pháp tuyến của ${{({mp_P})}}$" 
        kq1_F=f"${vec("n")}=({k*a};{k*b};{k*c})$ không phải là một véctơ pháp tuyến của ${{({mp_P})}}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${vec("n")}=({k*a};{k*b};{k*c})$ là một véctơ pháp tuyến của ${{({mp_P})}}$"

    if chon==2:
        t=random.randint(1,2)
        kq1_T=f"* ${vec("n")}=({k*a};{k*b};{k*c+t})$ không là một véctơ pháp tuyến của ${{({mp_P})}}$" 
        kq1_F=f"${vec("n")}=({k*a};{k*b};{k*c+t})$ là một véctơ pháp tuyến của ${{({mp_P})}}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${vec("n")}=({k*a};{k*b};{k*c+t})$ không là một véctơ pháp tuyến của ${{({mp_P})}}$."
    
    
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc mặt phẳng ${{({mp_P})}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc mặt phẳng ${{({mp_P})}}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Tọa độ điểm ${{{A}}}({x_A};{y_A};{z_A})$ thỏa mãn phương trình ${ptmp_P}=0$ nên điểm ${{{A}}}$ thuộc mặt phẳng ${{({mp_P})}}$."
    
    if chon==2:
        t=random.randint(1,2)
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+t})$ không thuộc mặt phẳng ${{({mp_P})}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A+t})$ thuộc mặt phẳng ${{({mp_P})}}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Tọa độ điểm ${{{A}}}({x_A};{y_A};{z_A})$ không thỏa mãn phương trình ${ptmp_P}=0$ nên điểm ${{{A}}}$ không thuộc mặt phẳng ${{({mp_P})}}$."
    

    
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    khoang_cach=latex(nsimplify(abs(a*x_I+b*y_I+c*z_I+d)/sqrt(a**2+b**2+c**2)))
    khoang_cach_false=latex(nsimplify(abs(a*x_I+b*y_I+c*z_I+d+random.randint(1,2))/sqrt(a**2+b**2+c**2)))


    kq3_T=f"* Khoảng cách từ điểm ${I}({x_I};{y_I};{z_I})$ đến mặt phẳng ${{({mp_P})}}$ bằng ${khoang_cach}$" 
    kq3_F=f"Khoảng cách từ điểm ${I}({x_I};{y_I};{z_I})$ đến mặt phẳng ${{({mp_P})}}$ bằng ${khoang_cach_false}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$d\\left({I},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_I)}+{show_tich(b,y_I)}+{show_tich(c,z_I)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}$."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a1,b1,c1=[random.choice([i for i in range(-5, 6) if i!=0]) for _ in range(3)]
    d1=random.randint(-5,5)

    x_M,y_M,z_M=x_B,y_B,z_B+random.randint(1,2)

    kq4_T=(f"* Mặt phẳng ${{({mp_Q})}}$ qua điểm ${M}({x_M};{y_M};{z_M})$ và song song với ${{({mp_P})}}$ có phương trình là "
        f"${latex(a*(x-x_M)+b*(y-y_M)+c*(z-z_M))}=0$"
        )
    kq4_F=(f" Mặt phẳng ${{({mp_Q})}}$ qua điểm ${M}({x_M};{y_M};{z_M})$ và song song với ${{({mp_P})}}$ có phương trình là "
        f"${latex(a*(x-x_M)+b*(y-y_M)+c*(z-z_M)+random.randint(1,3))}=0$"
        ) 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"Mặt phẳng ${{({mp_Q})}}$ nhận ${vec(f"n_{mp_P}")}=({a};{b};{c})$ làm một véctơ pháp tuyến.\n\n"
        f"Phương trình ${{({mp_Q})}}:{a}({latex(x-x_M)})+{b}({latex(y-y_M)})+{c}({latex(z-z_M)})=0$"
        f" $\\Leftrightarrow {latex(a*(x-x_M)+b*(y-y_M)+c*(z-z_M))}=0$."      
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

#[D12_C5_B1_20]-M2. Cho mặt phẳng. Xét Đ-S: VTPT, điểm thuộc mp, vị trí hai mp, phương trình mặt phẳng vuông góc
def htd_25_xyz_L12_C5_B1_20():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    x_A,y_A,z_A = [random.randint(-5,5) for i in range(3)]
    if x_A ==0: x_A=random.randint(1,5)

    x_B, y_B, z_B = random.randint(-3,3),random.randint(-4,4),random.randint(-3,3)
    x_C, y_C, z_C = [random.randint(-4,4) for i in range(3)]
    if y_C ==0: y_C=random.randint(1,5)

    if x_A==x_B==x_C: x_A=x_A+random.randint(1,3)
    if y_A==y_B==y_C: y_B=y_B+random.randint(1,3)
    if z_A==z_B==z_C: z_C=z_C+random.randint(1,3)

    if (x_B-x_A)*(y_C-y_A)==(x_C-x_A)*(y_B-y_A):
        x_B = x_B + random.randint(1,3)

    while True:
        x_I, y_I, z_I = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7) 
        if all([x_I!=x_A, x_I!=x_B, x_I!=x_C,y_I!=y_A, y_I!=y_B, y_I!=y_C]):
            break


    m=[x_B-x_A, y_B-y_A, z_B-z_A]
    n=[x_C-x_A, y_C-y_A, z_C-z_A]
    a, b, c = tich_co_huong(m,n)

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)


    ten_mp=["P","Q", "R", "\\alpha","\\beta", "\\gamma"]
    random.shuffle(ten_mp)
    mp_P, mp_Q=ten_mp[0:2]

    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,I,M=ten_diem[0:5]   
    ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A))
    d=-a*x_A-b*y_A-c*z_A
    
    noi_dung= (f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({mp_P})}}$ có phương trình ${ptmp_P}=0$."
                f" Xét tính đúng-sai của các khẳng định sau")
    k=random.choice([i for i in range(-2, 2) if i!=0])
    chon=random.randint(1,2)
    if chon==1:
        kq1_T=f"* ${vec("n")}=({k*a};{k*b};{k*c})$ là một véctơ pháp tuyến của ${{({mp_P})}}$" 
        kq1_F=f"${vec("n")}=({k*a};{k*b};{k*c})$ không phải là một véctơ pháp tuyến của ${{({mp_P})}}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${vec("n")}=({k*a};{k*b};{k*c})$ là một véctơ pháp tuyến của ${{({mp_P})}}$"

    if chon==2:
        t=random.randint(1,2)
        kq1_T=f"* ${vec("n")}=({k*a};{k*b};{k*c+t})$ không là một véctơ pháp tuyến của ${{({mp_P})}}$" 
        kq1_F=f"${vec("n")}=({k*a};{k*b};{k*c+t})$ là một véctơ pháp tuyến của ${{({mp_P})}}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"${vec("n")}=({k*a};{k*b};{k*c+t})$ không là một véctơ pháp tuyến của ${{({mp_P})}}$."
    
    
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc mặt phẳng ${{({mp_P})}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc mặt phẳng ${{({mp_P})}}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Tọa độ điểm ${{{A}}}({x_A};{y_A};{z_A})$ thỏa mãn phương trình ${ptmp_P}=0$ nên điểm ${{{A}}}$ thuộc mặt phẳng ${{({mp_P})}}$."
    
    if chon==2:
        t=random.randint(1,2)
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+t})$ không thuộc mặt phẳng ${{({mp_P})}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A+t})$ thuộc mặt phẳng ${{({mp_P})}}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Tọa độ điểm ${{{A}}}({x_A};{y_A};{z_A})$ không thỏa mãn phương trình ${ptmp_P}=0$ nên điểm ${{{A}}}$ không thuộc mặt phẳng ${{({mp_P})}}$."
    

    
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    k=random.choice([i for i in range(-3, 3) if i!=0])
    

    chon=random.randint(1,2)
 
    if chon==1:
        a1,b1,c1=k*a,k*b,k*c
        d1=k*d+random.randint(1,2)
        kq3_T=f"* Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d1)}=0$ song song nhau" 
        kq3_F=f"Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d1)}=0$ {random.choice(["cắt", "vuông góc", "trùng" ])} nhau"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f"${vec(f"n_{mp_P}")}=({a};{b};{c}), {vec(f"n_{mp_Q}")}=({a1};{b1};{c1})$.\n\n"
            f"Ta có: ${vec(f"n_{mp_P}")}={k}{vec(f"n_{mp_Q}")}$ và ${d1}\\ne {show_tich(k,d)}$"
            f" nên  ${{({mp_P})}}$ và $({mp_Q})$ song song nhau.")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon==2:
        a1,b1,c1,d1=k*a,k*b,k*c,k*d
        
        kq3_T=f"* Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d)}=0$ trùng nhau" 
        kq3_F=f"Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d)}=0$ {random.choice(["cắt", "vuông góc", "song song" ])} nhau"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=(f"${vec(f"n_{mp_P}")}=({a};{b};{c}), {vec(f"n_{mp_Q}")}=({a1};{b1};{c1})$.\n\n"
            f"Ta có: ${vec(f"n_{mp_P}")}={k}{vec(f"n_{mp_Q}")}$ và ${d1}={show_tich(k,d)}$"
            f" nên  ${{({mp_P})}}$ và $({mp_Q})$ trùng nhau.")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}" 

    

    x_A,y_A,z_A=x_A+random.randint(1,2),y_A,z_A
    x_B,y_B,z_B=x_B,y_B+random.randint(1,2),z_B

    x_AB,y_AB,z_AB=x_B-x_A,y_B-y_A,z_B-z_A
    m=[x_AB, y_AB, z_AB]
    n=[a, b, c]
    
    a1,b1,c1=tich_co_huong(m,n)

    kq4_T=(f"* Mặt phẳng ${{({mp_Q})}}$ đi qua hai điểm ${B}({x_A};{y_A};{z_A}), {C}({x_B};{y_B};{z_B})$ và vuông góc với ${{({mp_P})}}$ có phương trình là "
        f"${latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A))}=0$"
        )
    kq4_F=(f"* Mặt phẳng ${{({mp_Q})}}$ đi qua hai điểm ${B}({x_A};{y_A};{z_A}), {C}({x_B};{y_B};{z_B})$ và vuông góc với ${{({mp_P})}}$ có phương trình là "
        f"${latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A)+random.randint(1,2))}=0$"
        ) 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"${vec(f"n_{mp_P}")}=({a};{b};{c}), {vec2(B,C)}=({x_AB};{y_AB};{z_AB})$.\n\n"
        f"Mặt phẳng ${{({mp_Q})}}$ nhận ${vec(f"n_{mp_P}")},{vec2(A,B)}$ làm cặp véctơ chỉ phương.\n\n"
        f"$[{vec(f"n_{mp_P}")},{vec2(B,C)}]=({a1};{b1};{c1})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_Q})}}$.\n\n"        
        f"Phương trình ${{({mp_Q})}}:{a1}({latex(x-x_A)})+{b1}({latex(y-y_A)})+{c1}({latex(z-z_A)})=0$"
        f" $\\Leftrightarrow {latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A))}=0$."      
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

#BÀI 3 - PHƯƠNG TRÌNH MẶT CẦU
#[D12_C5_B3_01]. Viết phương trình mặt cầu có tâm và bán kính
def htd_25_xyz_L12_C5_B3_01():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    lits_r=[sqrt(i) for i in range(1,101)]
    r=random.choice(lits_r)
    a,b,c = [random.randint(-10,10) for i in range(3)]
    if a==b==c==0:
        b=random.randint(1,5)
        c=random.randint(-10,-1) 

    noi_dung= f"Trong không gian ${{Oxyz}}$, mặt cầu ${{(S)}}$ tâm ${{I({a};{b};{c})}}$"\
                f" và bán kính ${{R}}={latex(r)}$ có phương trình là"

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(r**2)}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={latex(r**2)}"
    if r!=1:
        kq3=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={latex(r)}"
    else:
        kq3=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={latex(2*r)}"
    kq4=f"{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(4*r**2)}"

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có phương trình là: ${kq}$."    

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

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

#[D12_C5_B3_02]-M1. Đọc tọa độ tâm từ phương trình mặt cầu thu gọn
def htd_25_xyz_L12_C5_B3_02():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    lits_r=[sqrt(i) for i in range(1,101)]
    r=random.choice(lits_r)
    a,b,c = [random.choice([random.randint(-10,-1),random.randint(1,10)]) for i in range(3)]
    if a==b==c:
        b=random.randint(1,5)
        c=random.randint(-10,-1)

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt cầu ${{(S)}}:{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(r**2)}$."\
                f" Tọa độ tâm ${{I}}$ của mặt cầu ${{(S)}}$ là"

    kq= f"{{I({a};{b};{c})}}"
    kq2=f"{{I({-a};{-b};{-c})}}"
    kq3=random.choice([f"{{I({a};{-b};{-c})}}", f"{{I({a};{b};{-c})}}", f"{{I({a};{-b};{c})}}"])
    kq4=random.choice([f"{{I({-a};{b};{-c})}}",f"{{I({-a};{-b};{c})}}", f"{{I({-a};{b};{c})}}"])

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có tọa độ tâm là: ${kq}$."    

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B3_03]-M1. Đọc bán kính từ phương trình mặt cầu thu gọn
def htd_25_xyz_L12_C5_B3_03():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    lits_r=[i for i in range(1,50)]
    r=random.choice(lits_r)
    a,b,c = [random.choice([random.randint(-10,-1),random.randint(1,10)]) for i in range(3)]
    if a==b==c:
        b=random.randint(1,5)
        c=random.randint(-10,-1)

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt cầu ${{(S)}}:{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(r**2)}$."\
                f" Bán kính của mặt cầu ${{(S)}}$ là"

    kq= f"{{R={latex(r)}}}"
    kq2=f"{{R={latex(r**2)}}}"
    kq3=f"{{R={latex(sqrt(r))}}}"
    kq4=f"{{R={latex(r*2)}}}"

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có tọa độ bán kính là: $R=\\sqrt{{{latex(r**2)}}}={latex(r)}$."    

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B3_04]-M1. Đọc tọa độ tâm từ phương trình mặt cầu khai triển
def htd_25_xyz_L12_C5_B3_04():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a,b,c = [random.choice([random.randint(-8,-1),random.randint(1,8)]) for i in range(3)]
    if a==b==c:
        b=random.randint(1,5)
        c=random.randint(-10,-1)
    
    d=a**2 +b**2 + c**2-random.randint(1,30)
    dau_a, dau_b, dau_c, dau_d = tao_dau(-a),tao_dau(-b), tao_dau(-c), tao_dau(d)
    if a!=0:
        hs_ax=latex(-2*a*x)
    else:
        hs_ax=""

    if b!=0:
        hs_by=latex(-2*b*y)
    else:
        hs_by=""

    if c!=0:
        hs_cz=latex(-2*c*z)
    else:
        hs_cz=""

    if d!=0:
        hs_d=d
    else:
        hs_d=""
    ptmc=f"x^2+y^2+z^2 {dau_a}{hs_ax} {dau_b}{hs_by} {dau_c}{hs_cz} {dau_d}{d} =0"

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt cầu ${{(S)}}:{ptmc}$."\
                f" Tọa độ tâm ${{I}}$ của mặt cầu ${{(S)}}$ là"

    kq= f"{{I({a};{b};{c})}}"
    kq2=f"{{I({-a};{-b};{-c})}}"
    kq3=random.choice([f"{{I({a};{-b};{-c})}}", f"{{I({a};{b};{-c})}}", f"{{I({a};{-b};{c})}}"])
    kq4=random.choice([f"{{I({-a};{b};{-c})}}",f"{{I({-a};{-b};{c})}}", f"{{I({-a};{b};{c})}}"])

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có tọa độ tâm là: ${kq}$."    

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B3_05]-M2. Đọc bán kính từ phương trình mặt cầu khai triển
def htd_25_xyz_L12_C5_B3_05():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a,b,c = [random.choice([random.randint(-8,-1),random.randint(1,8)]) for i in range(3)]
    if a==b==c:
        b=random.randint(1,5)
        c=random.randint(-10,-1)
    
    d=a**2 +b**2 + c**2-random.randint(1,30)
    dau_a, dau_b, dau_c, dau_d = tao_dau(-a),tao_dau(-b), tao_dau(-c), tao_dau(d)
    if a!=0:
        hs_ax=latex(-2*a*x)
    else:
        hs_ax=""

    if b!=0:
        hs_by=latex(-2*b*y)
    else:
        hs_by=""

    if c!=0:
        hs_cz=latex(-2*c*z)
    else:
        hs_cz=""

    if d!=0:
        hs_d=d
    else:
        hs_d=""
    ptmc=f"x^2+y^2+z^2 {dau_a}{hs_ax} {dau_b}{hs_by} {dau_c}{hs_cz} {dau_d}{d} =0"

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt cầu ${{(S)}}:{ptmc}$."\
                f" Tính bán kính mặt cầu ${{(S)}}$."

    kq= sqrt(a**2 +b**2 + c**2-d)
    kq2=sqrt(a**2 +b**2 + c**2)
    kq3=sqrt(abs(a) +abs(b) + abs(c))
    kq4=a**2 +b**2 + c**2-d
    
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có bán kính là:"\
        f" $R=\\sqrt{{{tao_ngoac(a)}^2 + {tao_ngoac(b)}^2 +{tao_ngoac(c)}^2 -{tao_ngoac(d)}}}={latex(sqrt(a**2 +b**2 + c**2-d))}$."    

    #Tạo các phương án
    pa_A= f"*${{R={latex(kq)}}}$"
    pa_B= f"${{R={latex(kq2)}}}$"
    pa_C= f"${{R={latex(kq3)}}}$"
    pa_D= f"${{R={latex(kq4)}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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


#[D12_C5_B3_06]-M2. Viết phương trình mặt cầu có tâm và đường kính
def htd_25_xyz_L12_C5_B3_06():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    lits_r=[i for i in range(1,101)]
    r=random.choice(lits_r)
    a,b,c = [random.choice([random.randint(-10,-1),random.randint(1,10)]) for i in range(3)]
    if a==b==c:
        b=random.randint(1,5)
        c=random.randint(-10,-1)

    noi_dung= f"Trong không gian ${{Oxyz}}$, mặt cầu ${{(S)}}$ tâm ${{I({a};{b};{c})}}$"\
                f" và đường kính bằng ${{{latex(2*r)}}}$ có phương trình là"

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(r**2)}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={latex(r**2)}"
    kq3=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={latex(r)}"
    kq4=f"{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(4*r**2)}"

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có tâm ${{I({a};{b};{c})}}$ và bán kính $R=\\dfrac{{{latex(2*r)}}}{{2}}={latex(r)}$.\n\n"\
                f"Phương trình mặt cầu: ${kq}$."

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B3_07]-M3. Viết phương trình mặt cầu có đường kính AB
def htd_25_xyz_L12_C5_B3_07():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    diem_A=["A","M","P","C"]
    diem_B=["B","N","Q","D"]
    i=random.randint(0,3)
    diem_A,diem_B =diem_A[i], diem_B[i]

    a1,a2,a3 = [random.randint(-10,10) for i in range(3)]
    if a1==a2==a3==0:
        a1=random.randint(1,10)
        a3=random.randint(-10,-1) 
    
    a,b,c = [random.randint(-10,10) for i in range(3)]
    if a==b==c==0:
        b=random.randint(1,5)
        c=random.randint(-10,-1) 

    b1, b2, b3 = 2*a-a1, 2*b-a2, 2*c-a3

    r=sqrt((a1-b1)**2+(a2-b2)**2+(a3-b3)**2)/2

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho hai điểm ${diem_A}({a1};{a2};{a3}),{diem_B}({b1};{b2};{b3})$."\
                f" Mặt cầu ${{(S)}}$ có đường kính ${{{diem_A}{diem_B}}}$ có phương trình là"               

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(r**2)}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={latex(r**2)}"
    kq3=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={latex(r)}"
    kq4=f"{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={latex(4*r**2)}"

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có tâm ${{I({a};{b};{c})}}$ là trung điểm của đoạn thẳng ${{{diem_A}{diem_B}}}$. \n\n"\
    f"${{{diem_A}{diem_B}}}=\\sqrt{{\\left({show_hieu(b1,a1)}\\right)^2 + \\left({show_hieu(b2,a2)}\\right)^2 + \\left({show_hieu(b3,a3)}\\right)^2}}= {latex(sqrt((a1-b1)**2+(a2-b2)**2+(a3-b3)**2))}$.\n\n"\
    f" ${{(S)}}$ có bán kính $R=\\dfrac{{{diem_A}{diem_B}}}{{2}}={latex(r)}$.\n\n"\
    f"Phương trình mặt cầu: ${kq}$."

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B3_08]. Viết phương trình mặt cầu có tâm và đi qua điểm
def htd_25_xyz_L12_C5_B3_08():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a,b,c = [random.randint(-10,10) for i in range(3)]
    x_0,y_0,z_0=[random.randint(-10,10) for i in range(3)]
    if x_0 ==a and y_0==b:
        x_0=x_0+random.randint(1,3)
        y_0=y_0-random.randint(1,4)
    ten_tam=random.choice(["A","B","I","H"])
    ten_diem=random.choice(["M","N","E","F","D","K"])
    r=sqrt((a-x_0)**2+(b-y_0)**2+(c-z_0)**2)
          

    noi_dung= f"Trong hệ trục ${{Oxyz}}$, phương trình mặt cầu ${{(S)}}$ có tâm ${{{ten_tam}({a};{b};{c})}}$"\
                f" và đi qua điểm ${ten_diem}({x_0};{y_0};{z_0})$ là"

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}+{latex((z-c)**2)}={r**2}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}+{latex((z+c)**2)}={r**2}"
    kq3=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}+{latex((z-z_0)**2)}={r**2}"
    kq4=f"{latex((x+x_0)**2)}+{latex((y+y_0)**2)}+{latex((z+z_0)**2)}={r**2}"

    noi_dung_loigiai=f"Mặt cầu ${{(S)}}$ có bán kính là ${{{ten_tam}{ten_diem}}}=\\sqrt{{({show_hieu(x_0,a)})^2+({show_hieu(y_0,b)})^2+({show_hieu(z_0,c)})^2}}={latex(r)}$.\n\n"\
    f"Mặt cầu ${{(S)}}$ có phương trình là: ${kq}$.".replace("(0)","0")

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

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

#BÀI 2 - PHƯƠNG TRÌNH ĐƯỜNG THẲNG
#[D12_C5_B2_01]-M1. Viết PTDT qua điểm và có véctơ chỉ phương 
def htd_25_xyz_L12_C5_B2_01():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$"\
                f" và nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{a}}}=\\dfrac{{{latex(y+y_0)}}}{{{b}}}=\\dfrac{{{latex(z+z_0)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-a)}}}{{{x_0}}}=\\dfrac{{{latex(y-b)}}}{{{y_0}}}=\\dfrac{{{latex(z-c)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_02]-M2. Viết PTĐT qua điểm A và nhận vectơ BC làm véctơ chỉ phương.
def htd_25_xyz_L12_C5_B2_02():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    x_B, y_B, z_B = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7)
    x_C, y_C, z_C = a+x_B, b+y_B, c+z_B

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_A=random.choice(["A","M", "E", "I" ])
    ten_B=random.choice(["B", "D","M", "H" ])
    ten_C=random.choice(["C", "G", "K"])
    d=-a*x_0-b*y_0-c*z_0+random.randint(1,20)

    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$"\
                f" và nhận vectơ $\\overrightarrow{{{ten_B}{ten_C}}}$ làm véctơ chỉ phương với ${ten_B}({x_B};{y_B};{z_B})$ và ${ten_C}({x_C};{y_C};{z_C})$ có phương trình là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{a}}}=\\dfrac{{{latex(y+y_0)}}}{{{b}}}=\\dfrac{{{latex(z+z_0)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-a)}}}{{{x_0}}}=\\dfrac{{{latex(y-b)}}}{{{y_0}}}=\\dfrac{{{latex(z-c)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\overrightarrow{{{ten_B}{ten_C}}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\overrightarrow{{{ten_B}{ten_C}}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là: ${kq}$.")

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_03]-M2. Viết PTDT qua điểm và song song với đường thẳng
def htd_25_xyz_L12_C5_B2_03():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    t1=random.choice([random.randint(-3, -1), random.randint(1, 3)])
    a1, b1, c1 = a*t1, b*t1, c*t1

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_dt2=random.choice(["d_1", "d'","\\Delta_1"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$"\
                f" và song song với đường thẳng ${ten_dt2}:\\dfrac{{{latex(x-x_0+random.randint(1,4))}}}{{{a1}}}=\\dfrac{{{latex(y-y_0-random.randint(-4,4))}}}{{{b1}}}=\\dfrac{{{latex(z-z_0+random.randint(-4,4))}}}{{{c1}}}$ có phương trình là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{a}}}=\\dfrac{{{latex(y+y_0)}}}{{{b}}}=\\dfrac{{{latex(z+z_0)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-a)}}}{{{x_0}}}=\\dfrac{{{latex(y-b)}}}{{{y_0}}}=\\dfrac{{{latex(z-c)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a1};{b1};{c1})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ song song với ${{{ten_dt2}}}$ nên có một véctơ chỉ phương là vectơ $\\vec{{u}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_04]-M2. Viết PT chính tắc qua điểm và vuông góc với mặt phẳng
def htd_25_xyz_L12_C5_B2_04():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)



    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_mp=random.choice(["(P)", "(Q)","(\\alpha)", "(\\beta)", "(\\gamma)"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$"\
                f" và vuông góc với mặt phẳng ${ten_mp}:{latex(a*x+b*y+c*z+random.randint(-10,10))}=0$ có phương trình là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{a}}}=\\dfrac{{{latex(y+y_0)}}}{{{b}}}=\\dfrac{{{latex(z+z_0)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-a)}}}{{{x_0}}}=\\dfrac{{{latex(y-b)}}}{{{y_0}}}=\\dfrac{{{latex(z-c)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Mặt phẳng ${{{ten_mp}}}$ có véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ vuông góc với ${{{ten_mp}}}$ nên có một véctơ chỉ phương là vectơ $\\vec{{u}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_05]-M1. Viết PT chính tắc đường thẳng qua 2 điểm.
def htd_25_xyz_L12_C5_B2_05():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    x_1, y_1, z_1 =x_0+a, y_0+b, z_0+c
    
    ten_diem1=random.choice(["A", "C", "M", "E", "I" ])
    ten_diem2=random.choice(["B", "D", "N", "F", "H" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng đi qua hai điểm ${{{ten_diem1}({x_0};{y_0};{z_0})}}$"\
                f" và ${{{ten_diem2}({x_1};{y_1};{z_1})}}$ có phương trình là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_1)}}}{{{a}}}=\\dfrac{{{latex(y+y_1)}}}{{{b}}}=\\dfrac{{{latex(z+z_1)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_1)}}}{{{x_0}}}=\\dfrac{{{latex(y-y_1)}}}{{{y_0}}}=\\dfrac{{{latex(z-z_1)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_1)}}}{{{a}}}=\\dfrac{{{latex(y-y_1)}}}{{{-b}}}=\\dfrac{{{latex(z-z_1)}}}{{{c}}}")
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_diem1}{ten_diem2}}}$ đi qua điểm ${{{ten_diem1}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\overrightarrow {{{ten_diem1}{ten_diem2}}}=({a};{b};{c})$"\
        f" làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_06]-M3. Viết PT chính tắc đường thẳng d song song d' và vuông góc với (P).
def htd_25_xyz_L12_C5_B2_06():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    #Tạo véctơ chỉ phương của d'
    vec1 = [random.choice([random.randint(-8, -1), random.randint(1, 8)]) for i in range(3)]
    vec2 = generate_random_vector()
    
    while not check_cross_product_nonzero(vec1, vec2) and vec2[0]==0:
        vec2 = generate_random_vector()
    a1,b1,c1= vec1
    a2,b2,c2= vec2

    a,b,c=tich_co_huong(vec1,vec2)
    a_d,b_d,c_d=a, b, c

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_dt2=random.choice(["d_1", "\\Delta_1"])
    ten_diem=random.choice(["A","B", "C","M", "N", "E", "I" ])
    ten_mp=random.choice(["(P)", "(Q)","(\\alpha)", "(\\beta)", "(\\gamma)"])

    dt2=f"\\dfrac{{{latex(x-x_0+random.randint(1,3))}}}{{{a1}}}=\\dfrac{{{latex(y-y_0+random.randint(1,4))}}}{{{b1}}}=\\dfrac{{{latex(z-z_0)}}}{{{c1}}}"
    mp=f"{latex(a2*x+b2*y+c2*z+random.randint(-10,10))}=0"
    noi_dung= f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$."\
                f" Biết ${{{ten_dt}}}$ vuông góc với đường thẳng ${ten_dt2}:{dt2}$ và song song với mặt phẳng ${ten_mp}:{mp}$."\
                f" Phương trình đường thẳng ${{{ten_dt}}}$ là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{a}}}=\\dfrac{{{latex(y+y_0)}}}{{{b}}}=\\dfrac{{{latex(z+z_0)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-a)}}}{{{x_0}}}=\\dfrac{{{latex(y-b)}}}{{{y_0}}}=\\dfrac{{{latex(z-c)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"${ten_dt2}:{dt2}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a1};{b1};{c1})$.\n\n"\
        f" ${ten_mp}:{mp}$ có véctơ pháp tuyến là  $\\vec{{n}}=({a2};{b2};{c2})$.\n\n"\
        f"Ta có: $\\left[\\overrightarrow{{u_1}},\\vec{{n}}\\right]=({a_d};{b_d};{c_d})$ là một véctơ chỉ phương của ${{{ten_dt}}}$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_07]-M3. Viết PT chính tắc đường thẳng d và vuông góc với (P) và (Q).
def htd_25_xyz_L12_C5_B2_07():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    #Tạo véctơ chỉ phương của d'
    vec1 = [random.choice([random.randint(-8, -1), random.randint(1, 8)]) for i in range(3)]
    vec2 = generate_random_vector()
    
    while not check_cross_product_nonzero(vec1, vec2) and vec2[0]==0:
        vec2 = generate_random_vector()
    a1,b1,c1= vec1
    a2,b2,c2= vec2

    a,b,c=tich_co_huong(vec1,vec2)
    a_d,b_d,c_d=a, b, c

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C","M", "N", "E", "I" ])
    ten_mp1=random.choice(["(P)", "(\\alpha)", "(\\beta)"])
    ten_mp2=random.choice([ "(Q)","(\\beta)", "(\\gamma)"])
    mp1=latex(a1*x+b1*y+c1*z+random.randint(-10,10))
    mp2=latex(a2*x+b2*y+c2*z+random.randint(-10,10))

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$."\
                f" Biết ${{{ten_dt}}}$ song song với cả hai mặt phẳng ${ten_mp1}:{mp1}=0$ và ${ten_mp2}:{mp2}=0$."\
                f" Phương trình đường thẳng ${{{ten_dt}}}$ là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{a}}}=\\dfrac{{{latex(y+y_0)}}}{{{b}}}=\\dfrac{{{latex(z+z_0)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-a)}}}{{{x_0}}}=\\dfrac{{{latex(y-b)}}}{{{y_0}}}=\\dfrac{{{latex(z-c)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"${ten_mp1}:{mp1}=0$ có véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({a1};{b1};{c1})$.\n\n"\
        f"${ten_mp2}:{mp2}=0$ có véctơ pháp tuyến là $\\overrightarrow{{n_2}}=({a2};{b2};{c2})$.\n\n"\
        f"Ta có: $\\left[\\overrightarrow{{n_1}},\\overrightarrow{{n_2}}\\right]=({a_d};{b_d};{c_d})$ là một véctơ chỉ phương của ${{{ten_dt}}}$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_08]-M1. Viết PTTS đường thẳng qua điểm và có véctơ chỉ phương 
def htd_25_xyz_L12_C5_B2_08():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$"\
                f" và nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là"


    kq= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."
    kq2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)}\\\\ \
y = {show_ptts(b,y_0)}\\\\\
z = {show_ptts(c,z_0)}\
\\end{{array}} \\right."
    kq3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_0,a)}\\\\ \
y = {show_ptts(-y_0,b)}\\\\\
z = {show_ptts(-z_0,c)}\
\\end{{array}} \\right."
    
    kq4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(-y_0,-b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."

    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_09]-M2. Viết PTTS đường thẳng qua điểm A và nhận vectơ BC làm véctơ chỉ phương.
def htd_25_xyz_L12_C5_B2_09():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")

    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    x_B, y_B, z_B = random.randint(-7,7),random.randint(-7,7),random.randint(-7,7)
    x_C, y_C, z_C = a+x_B, b+y_B, c+z_B

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_A=random.choice(["A","M", "E", "I" ])
    ten_B=random.choice(["B", "D","M", "H" ])
    ten_C=random.choice(["C", "G", "K"])
    d=-a*x_0-b*y_0-c*z_0+random.randint(1,20)

    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$"\
                f" và nhận vectơ $\\overrightarrow{{{ten_B}{ten_C}}}$ làm véctơ chỉ phương với ${ten_B}({x_B};{y_B};{z_B})$ và ${ten_C}({x_C};{y_C};{z_C})$ có phương trình là"

    kq= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."
    kq2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)}\\\\ \
y = {show_ptts(b,y_0)}\\\\\
z = {show_ptts(c,z_0)}\
\\end{{array}} \\right."
    kq3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_0,a)}\\\\ \
y = {show_ptts(-y_0,b)}\\\\\
z = {show_ptts(-z_0,c)}\
\\end{{array}} \\right."
    
    kq4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(-y_0,-b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: $\\overrightarrow{{{ten_B}{ten_C}}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_A}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\overrightarrow{{{ten_B}{ten_C}}}=({x_C-x_B};{y_C-y_B};{z_C-z_B})$ làm véctơ chỉ phương có phương trình là: ${kq}$.")

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_10]-M2. Viết PTTS đường thẳng qua điểm và song song với đường thẳng
def htd_25_xyz_L12_C5_B2_10():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    t1=random.choice([random.randint(-3, -1), random.randint(1, 3)])
    a1, b1, c1 = a*t1, b*t1, c*t1

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_dt2=random.choice(["d_1", "d'","\\Delta_1"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$"\
                f" và song song với đường thẳng ${ten_dt2}:\\dfrac{{{latex(x-x_0+random.randint(1,4))}}}{{{a1}}}=\\dfrac{{{latex(y-y_0-random.randint(-4,4))}}}{{{b1}}}=\\dfrac{{{latex(z-z_0+random.randint(-4,4))}}}{{{c1}}}$ có phương trình là"

    kq= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."
    kq2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)}\\\\ \
y = {show_ptts(b,y_0)}\\\\\
z = {show_ptts(c,z_0)}\
\\end{{array}} \\right."
    kq3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_0,a)}\\\\ \
y = {show_ptts(-y_0,b)}\\\\\
z = {show_ptts(-z_0,c)}\
\\end{{array}} \\right."
    
    kq4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(-y_0,-b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a1};{b1};{c1})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ song song với ${{{ten_dt2}}}$ nên có một véctơ chỉ phương là vectơ $\\vec{{u}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_11]-M1. Cho phương trình chính tắc viết phương trình tham số
def htd_25_xyz_L12_C5_B2_11():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])


    noi_dung= f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}: \\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}$."\
                f" Phương trình tham số của đường thẳng ${{{ten_dt}}}$ là"

    kq= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."
    kq2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)}\\\\ \
y = {show_ptts(b,y_0)}\\\\\
z = {show_ptts(c,z_0)}\
\\end{{array}} \\right."
    kq3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_0,a)}\\\\ \
y = {show_ptts(-y_0,b)}\\\\\
z = {show_ptts(-z_0,c)}\
\\end{{array}} \\right."
    
    kq4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(-y_0,-b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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


#[D12_C5_B2_12]-M2. Cho phương trình tham số viết phương trình chính tắc
def htd_25_xyz_L12_C5_B2_12():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."
    noi_dung= f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:{ptts}$."\
                f" Phương trình chính tắc của đường thẳng ${{{ten_dt}}}$ là"

    kq= my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    kq2=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{a}}}=\\dfrac{{{latex(y+y_0)}}}{{{b}}}=\\dfrac{{{latex(z+z_0)}}}{{{c}}}")
    if all([x_0!=0, y_0!=0, z_0!=0]):
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-a)}}}{{{x_0}}}=\\dfrac{{{latex(y-b)}}}{{{y_0}}}=\\dfrac{{{latex(z-c)}}}{{{z_0}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+a)}}}{{{x_0}}}=\\dfrac{{{latex(y+b)}}}{{{y_0}}}=\\dfrac{{{latex(z+c)}}}{{{z_0}}}")
    else:
        kq3=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x+x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{-c}}}")
        kq4=my_module.thay_dau_congtru(f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}")
    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ đi qua điểm ${{{ten_diem}({x_0};{y_0};{z_0})}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương có phương trình là: ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_13]-M1. Đọc VTCP từ phương trình tham số
def htd_25_xyz_L12_C5_B2_13():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."


    noi_dung= f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:{ptts}$."\
                f" Đường thẳng ${{{ten_dt}}}$ nhận vectơ nào sau đây làm véctơ chỉ phương?"
    u=["u_1","u_2","u_3","u_4"]
    random.shuffle(u)
    t1 = random.choice([random.randint(-3, -1), random.randint(1, 3)])

    kq=f"\\overrightarrow{{{u[0]}}}=({a*t1};{b*t1};{c*t1})"
    kq2=f"\\overrightarrow{{{u[1]}}}=({x_0};{y_0};{z_0})"
    kq3=f"\\overrightarrow{{{u[2]}}}=({-x_0};{-y_0};{-z_0})"
    kq4=f"\\overrightarrow{{{u[3]}}}=({-a};{b};{-c})"    

    if t1!=1:
        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương nên cũng nhận vectơ "\
            f"${kq}$ làm véctơ chỉ phương.")
    else:
        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương.")

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_14]-M2. Đọc tọa độ điểm từ phương trình tham số
def htd_25_xyz_L12_C5_B2_14():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."


    noi_dung= f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:{ptts}$."\
                f" Đường thẳng ${{{ten_dt}}}$ đi qua điểm nào trong các điểm sau?"
    u=["A","B","C","D"]
    random.shuffle(u)
    t=random.randint(-3,3)
    x_1, y_1, z_1 =x_0+a*t, y_0 + b*t, z_0 +c*t
    kq=f"{u[0]}=({x_1};{y_1};{z_1})"
    kq2=f"{u[1]}=({a};{b};{c})"
    kq3=f"{u[2]}=({-x_0};{-y_0};{-z_0})"
    kq4=f"{u[3]}=({x_1+random.randint(1,3)};{y_1-random.randint(1,5)};{-c})"
    

    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Tồn tại $t={t} \\Rightarrow x={x_1},y={y_1},z={z_1}$ nên đường thẳng ${{{ten_dt}}}$ đi qua ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_15]-M2. Đọc VTCP từ phương trình chính tắc
def htd_25_xyz_L12_C5_B2_15():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."


    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}$."\
                f" Đường thẳng ${{{ten_dt}}}$ nhận vectơ nào sau đây làm véctơ chỉ phương?")
    u=["u_1","u_2","u_3","u_4"]
    random.shuffle(u)
    t1 = random.choice([random.randint(-3, -1), random.randint(1, 3)])

    kq=f"\\overrightarrow{{{u[0]}}}=({a*t1};{b*t1};{c*t1})"
    kq2=f"\\overrightarrow{{{u[1]}}}=({x_0};{y_0};{z_0})"
    kq3=f"\\overrightarrow{{{u[2]}}}=({-x_0};{-y_0};{-z_0})"
    kq4=f"\\overrightarrow{{{u[3]}}}=({-a};{b};{-c})"    

    if t1!=1:
        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương nên cũng nhận vectơ "\
            f"${kq}$ làm véctơ chỉ phương.")
    else:
        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ nhận vectơ $\\vec{{u}}=({a};{b};{c})$ làm véctơ chỉ phương.")

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_16]-M2. Đọc tọa độ điểm từ phương trình chính tắc
def htd_25_xyz_L12_C5_B2_16():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    c = random.choice([random.randint(-9, -1), random.randint(1, 9)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B", "C", "D","M", "N", "E", "I" ])

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\\\\\
z = {show_ptts(z_0,c)}\
\\end{{array}} \\right."


    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}$."\
                f" Đường thẳng ${{{ten_dt}}}$ đi qua điểm nào trong các điểm sau?")
    u=["A","B","C","D"]
    random.shuffle(u)
    t=random.randint(-3,3)
    x_1, y_1, z_1 =x_0+a*t, y_0 + b*t, z_0 +c*t
    kq=f"{u[0]}=({x_1};{y_1};{z_1})"
    kq2=f"{u[1]}=({a};{b};{c})"
    kq3=f"{u[2]}=({-x_0};{-y_0};{-z_0})"
    kq4=f"{u[3]}=({x_1+random.randint(1,3)};{y_1-random.randint(1,5)};{-c})"
    

    
    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ có phương trình tham số là ${ptts}$.\n\n"\
        f"Tồn tại $t={t} \\Rightarrow x={x_1},y={y_1},z={z_1}$ nên đường thẳng ${{{ten_dt}}}$ đi qua ${kq}$.")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_17]-M2. Tìm giao điểm của đường thẳng và mặt phẳng
def htd_25_xyz_L12_C5_B2_17():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    n1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    n2 = random.randint(-6, -6)
    n3 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

    if a*n1+b*n2+c*n3==0:
        n2=n2+random.randint(1,3)       

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_mp=random.choice(["(P)","(Q)", "(R)", f"(\\alpha)", f"(\\beta)", f"(\\gamma)"])

    mp=latex(expand(n1*(x-x_0)+n2*(y-y_0)+n3*(z-z_0)))
    d=-n1*x_0-n2*y_0-n3*z_0

    t1= random.choice([random.randint(-4, -1), random.randint(1, 4)])
    x_1, y_1, z_1 = x_0+a*t1, y_0+b*t1, z_0+c*t1

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_1,a)}\\\\ \
y = {show_ptts(y_1,b)}\\\\\
z = {show_ptts(z_1,c)}\
\\end{{array}} \\right."
    kq=x_0+y_0+z_0
    kq2=random.randint(1,3)*x_0+y_0+random.randint(-4,-1)*z_0
    kq3=x_0+random.randint(1,3)*y_0+random.randint(-4,-1)*z_0
    kq4=x_0-y_0+random.randint(1,3)*z_0
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, tọa độ giao điểm của đường thẳng ${{{ten_dt}}}:\\dfrac{{{latex(x-x_1)}}}{{{a}}}=\\dfrac{{{latex(y-y_1)}}}{{{b}}}=\\dfrac{{{latex(z-z_1)}}}{{{c}}}$"\
                f" và mặt phẳng ${ten_mp}:{mp}=0$ là điểm $H(a;b;c)$. Tính $P=a+b+c$.")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ có phương trình tham số là ${ptts}$.\n\n"\
        f"Xét phương trình ${n1}({latex((x_1+a*t))})+{n2}({latex((y_1+b*t))})+{n3}({latex((z_1+c*t))})+{d}=0\\Rightarrow t={-t1}$.\n\n"\
        f"Tọa độ giao điểm của ${{{ten_dt}}}$ và ${{{ten_mp}}}$ là $H({x_0};{y_0};{z_0})$.\n\n Vậy $P={x_0}+{y_0}+{z_0}={kq}$.")
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
        #f"{file_name}\n"
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

#[D12_C5_B2_18]-M2. Tìm hình chiếu của điểm trên đường thẳng
def htd_25_xyz_L12_C5_B2_18():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,7)
    ten_dt=random.choice(["d","\\Delta"])
    ten_diem=random.choice(["A","B","C","E","F","G","I","M","N"])

    x_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    y_1 = random.randint(-6, -6)
    z_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

    phuongtrinh=Eq(a*(x_0+a*t-x_1)+b*(y_0+b*t-y_1)+c*(z_0+c*t-z_1),0)
    t_0=solve(phuongtrinh,t)[0]
    x_H, y_H, z_H =x_0+a*t_0, y_0+b*t_0, z_0 +c*t_0

    kq=x_H+y_H+z_H
    kq2=random.randint(1,3)*x_H+y_H+random.randint(-4,-1)*z_H
    kq3=x_H+random.randint(1,3)*y_H+random.randint(-4,-1)*z_H
    kq4=x_H-y_H+random.randint(1,3)*z_H
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}$"\
                f" và điểm ${ten_diem}({x_1};{y_1};{z_1})$.\n\n Hình chiếu vuông góc của điểm ${ten_diem}$ trên đường thẳng ${{{ten_dt}}}$ là điểm $H(a;b;c)$. Tính $P=a+b+c$.")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ có véctơ chỉ phương là $\\vec{{u}}=({a};{b};{c})$.\n\n"\
        f"Gọi $H({x_0}+{a}t;{y_0}+{b}t;{z_0}+{c}t)$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}=({latex(x_0+a*t-x_1)};{latex(y_0+b*t-y_1)};{latex(z_0+c*t-z_1)})$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}.\\overrightarrow{{u}}=0\\Leftrightarrow {a}({latex(x_0+a*t-x_1)})+{b}({latex(y_0+b*t-y_1)})+{c}({latex(z_0+c*t-z_1)})=0$"
        f"$\\Rightarrow t={phan_so(t_0)}$. \n\n"\
        f"Tọa độ điểm $H({phan_so(x_H)};{phan_so(y_H)};{phan_so(z_H)})$. Vậy $P={phan_so(x_H)}+{phan_so(y_H)}+{phan_so(z_H)}={phan_so(kq)}$.")
    #Tạo các phương án
    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{phan_so(kq2)}}}$"
    pa_C= f"${{{phan_so(kq3)}}}$"
    pa_D= f"${{{phan_so(kq4)}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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


#[D12_C5_B2_19]-M2. Xét vị trí 2 đường thẳng. Kết quả là song song
def htd_25_xyz_L12_C5_B2_19():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    
    ten_dt1=["d","\\Delta", "\\Delta_1"]
    ten_dt2=["d'","\\Delta'", "\\Delta_2"]
    i=random.randint(0,2)
    ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i]

    t=random.choice([random.randint(-4, -1), random.randint(2, 4)])
    

    x_1 = x_0+a*t
    y_1 = y_0+b*t+random.randint(1,3)
    z_1 = z_0+c*t-random.randint(1,3)
    a1,b1,c1=a*t,b*t,c*t

    dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
    dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
        f"Ta có $\\overrightarrow{{u_2}}={t}\\overrightarrow{{u_1}}\\Rightarrow \\overrightarrow{{u_1}}$ và $\\overrightarrow{{u_2}}$ cùng phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ song song hoặc trùng nhau.\n\n"
        f"Đường thẳng ${{{ten_dt1}}}$ qua điểm $A({x_0};{y_0};{z_0})$. Tọa độ điểm A không thỏa mãn phương trình của ${{{ten_dt2}}}$ nên $A \\notin {{{ten_dt2}}}$.\n\n"\
        f" Vậy ${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$."

       )
    #Tạo các phương án
    pa_A= f"*${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
    pa_B= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"
    pa_C= f"${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
    pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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


#[D12_C5_B2_20]-M2. Xét vị trí 2 đường thẳng. Kết quả là trùng nhau
def htd_25_xyz_L12_C5_B2_20():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    
    ten_dt1=["d","\\Delta", "\\Delta_1"]
    ten_dt2=["d'","\\Delta'", "\\Delta_2"]
    i=random.randint(0,2)
    ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i]

    t=random.choice([random.randint(-4, -1), random.randint(2, 4)])
    

    x_1 = x_0+a*t
    y_1 = y_0+b*t
    z_1 = z_0+c*t
    a1,b1,c1=a*t,b*t,c*t

    dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
    dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
        f"Ta có $\\overrightarrow{{u_2}}={t}\\overrightarrow{{u_1}}\\Rightarrow \\overrightarrow{{u_1}}$ và $\\overrightarrow{{u_2}}$ cùng phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ song song hoặc trùng nhau.\n\n"
        f"Đường thẳng ${{{ten_dt1}}}$ qua điểm $A({x_0};{y_0};{z_0})$. Tọa độ điểm A thỏa mãn phương trình của ${{{ten_dt2}}}$ nên $A \\in {{{ten_dt2}}}$.\n\n"\
        f" Vậy ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau."

       )
    #Tạo các phương án
    pa_A= f"*${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"
    pa_B= f"${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
    pa_C= f"${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
    pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_21]-M2. Xét vị trí 2 đường thẳng. Kết quả là cắt nhau
def htd_25_xyz_L12_C5_B2_21():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    a1 = random.choice([random.randint(-8, -2), random.randint(1, 8)])
    b1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    t_uc=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

    if a/a1==b/b1==c/c1:
        a1=abs(a1+1)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    
    ten_dt1=["d","\\Delta", "\\Delta_1"]
    ten_dt2=["d'","\\Delta'", "\\Delta_2"]
    i=random.randint(0,2)
    ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i]

    t=random.choice([random.randint(-2, -1), random.randint(1, 2)])    

    x_1 = x_0+a1*t
    y_1 = y_0+b1*t
    z_1 = z_0+c1*t
    

    dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
    dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")
    u,u1=[a,b,c], [a1,b1,c1]
    m1,m2,m3=tich_co_huong(u,u1)
    ten_vt=f"\\overrightarrow{{u}}"
    ten_vt1=f"\\overrightarrow{{u_1}}"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
        f"Ta có $\\overrightarrow{{u_2}}$ và $\\overrightarrow{{u_1}}$ khác phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ cắt nhau hoặc chéo nhau.\n\n"
        f"Đường thẳng ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ lần lượt đi qua $A({x_0};{y_0};{z_0})$ và $B({x_1};{y_1};{z_1})$.\n\n"\
        f"Ta có: $\\left[{ten_vt},{ten_vt1} \\right]=({m1};{m2};{m3}), \\overrightarrow{{AB}}=({x_1-x_0};{y_1-y_0};{z_1-z_0})$.\n\n"\
        f"$\\left[{ten_vt},{ten_vt1} \\right].\\overrightarrow{{AB}}={m1*(x_1-x_0)+m2*(y_1-y_0)+m3*(z_1-z_0)}$."\
        f" Vậy ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ cắt nhau."

       )
    #Tạo các phương án
    pa_A= f"*${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
    pa_B= f"${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
    pa_C= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"
    pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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


#[D12_C5_B2_22]-M2. Xét vị trí 2 đường thẳng. Kết quả là chéo nhau
def htd_25_xyz_L12_C5_B2_22():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
    b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    a1 = random.choice([random.randint(-8, -2), random.randint(1, 8)])
    b1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    t_uc=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

    if a/a1==b/b1==c/c1:
        a1=abs(a1+1)

    x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
    x_1,y_1,z_1 = [random.randint(-8,8) for i in range(3)]
    
    ten_dt1=["d","\\Delta", "\\Delta_1"]
    ten_dt2=["d'","\\Delta'", "\\Delta_2"]
    i=random.randint(0,2)
    ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i] 

    u,u1=[a,b,c], [a1,b1,c1]
    m1,m2,m3=tich_co_huong(u,u1)
    if m1*(x_1-x_0)+m2*(y_1-y_0)+m3*(z_1-z_0) ==0:
        x_1=x_1+random.randint(1,3)
    ten_vt=f"\\overrightarrow{{u}}"
    ten_vt1=f"\\overrightarrow{{u_1}}"    

    dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
    dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")
    

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
        f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
        f"Ta có $\\overrightarrow{{u_2}}$ và $\\overrightarrow{{u_1}}$ khác phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ cắt nhau hoặc chéo nhau.\n\n"
        f"Đường thẳng ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ lần lượt đi qua $A({x_0};{y_0};{z_0})$ và $B({x_1};{y_1};{z_1})$.\n\n"\
        f"Ta có: $\\left[{ten_vt},{ten_vt1} \\right]=({m1};{m2};{m3}), \\overrightarrow{{AB}}=({x_1-x_0};{y_1-y_0};{z_1-z_0})$.\n\n"\
        f"$\\left[{ten_vt},{ten_vt1} \\right].\\overrightarrow{{AB}}={m1*(x_1-x_0)+m2*(y_1-y_0)+m3*(z_1-z_0)} \\ne 0$."\
        f" Vậy ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau."

       )
    #Tạo các phương án
    pa_A= f"*${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"
    pa_B= f"${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
    pa_C= f"${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
    pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_23]-M2. Tổng hợp xét vị trí tương đối giữa 2 đường thẳng 

def htd_25_xyz_L12_C5_B2_23():
    chon=random.randint(1,4)
    if chon==1:
        #Tạo bậc ngẫu nhiên
        x,y,z,t=sp.symbols("x y z t")
        a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
        b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-7, -1), random.randint(1, 7)])

        t_uc=ucln_ba_so(a,b,c)
        a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

        x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
        
        ten_dt1=["d","\\Delta", "\\Delta_1"]
        ten_dt2=["d'","\\Delta'", "\\Delta_2"]
        i=random.randint(0,2)
        ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i]

        t=random.choice([random.randint(-4, -1), random.randint(2, 4)])
        

        x_1 = x_0+a*t
        y_1 = y_0+b*t+random.randint(1,3)
        z_1 = z_0+c*t-random.randint(1,3)
        a1,b1,c1=a*t,b*t,c*t

        dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
        dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                    f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
            f"Ta có $\\overrightarrow{{u_2}}={t}\\overrightarrow{{u_1}}\\Rightarrow \\overrightarrow{{u_1}}$ và $\\overrightarrow{{u_2}}$ cùng phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ song song hoặc trùng nhau.\n\n"
            f"Đường thẳng ${{{ten_dt1}}}$ qua điểm $A({x_0};{y_0};{z_0})$. Tọa độ điểm A không thỏa mãn phương trình của ${{{ten_dt2}}}$ nên $A \\notin {{{ten_dt2}}}$.\n\n"\
            f" Vậy ${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$."

           )
        #Tạo các phương án
        pa_A= f"*${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
        pa_B= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"
        pa_C= f"${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
        pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"
        

    if chon==2:
        #Tạo bậc ngẫu nhiên
        x,y,z,t=sp.symbols("x y z t")
        a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
        b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

        t_uc=ucln_ba_so(a,b,c)
        a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

        x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
        
        ten_dt1=["d","\\Delta", "\\Delta_1"]
        ten_dt2=["d'","\\Delta'", "\\Delta_2"]
        i=random.randint(0,2)
        ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i]

        t=random.choice([random.randint(-4, -1), random.randint(2, 4)])
        

        x_1 = x_0+a*t
        y_1 = y_0+b*t
        z_1 = z_0+c*t
        a1,b1,c1=a*t,b*t,c*t

        dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
        dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                    f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
            f"Ta có $\\overrightarrow{{u_2}}={t}\\overrightarrow{{u_1}}\\Rightarrow \\overrightarrow{{u_1}}$ và $\\overrightarrow{{u_2}}$ cùng phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ song song hoặc trùng nhau.\n\n"
            f"Đường thẳng ${{{ten_dt1}}}$ qua điểm $A({x_0};{y_0};{z_0})$. Tọa độ điểm A thỏa mãn phương trình của ${{{ten_dt2}}}$ nên $A \\in {{{ten_dt2}}}$.\n\n"\
            f" Vậy ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau."

           )
        #Tạo các phương án
        pa_A= f"*${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"
        pa_B= f"${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
        pa_C= f"${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
        pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"
        

    if chon==3:
        #Tạo bậc ngẫu nhiên
        x,y,z,t=sp.symbols("x y z t")
        a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
        b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

        t_uc=ucln_ba_so(a,b,c)
        a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

        a1 = random.choice([random.randint(-8, -2), random.randint(1, 8)])
        b1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        c1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        t_uc=ucln_ba_so(a1,b1,c1)
        a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

        if a/a1==b/b1==c/c1:
            a1=abs(a1+1)

        x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
        
        ten_dt1=["d","\\Delta", "\\Delta_1"]
        ten_dt2=["d'","\\Delta'", "\\Delta_2"]
        i=random.randint(0,2)
        ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i]

        t=random.choice([random.randint(-2, -1), random.randint(1, 2)])    

        x_1 = x_0+a1*t
        y_1 = y_0+b1*t
        z_1 = z_0+c1*t
        

        dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
        dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                    f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")
        u,u1=[a,b,c], [a1,b1,c1]
        m1,m2,m3=tich_co_huong(u,u1)
        ten_vt=f"\\overrightarrow{{u}}"
        ten_vt1=f"\\overrightarrow{{u_1}}"

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
            f"Ta có $\\overrightarrow{{u_2}}$ và $\\overrightarrow{{u_1}}$ khác phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ cắt nhau hoặc chéo nhau.\n\n"
            f"Đường thẳng ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ lần lượt đi qua $A({x_0};{y_0};{z_0})$ và $B({x_1};{y_1};{z_1})$.\n\n"\
            f"Ta có: $\\left[{ten_vt},{ten_vt1} \\right]=({m1};{m2};{m3}), \\overrightarrow{{AB}}=({x_1-x_0};{y_1-y_0};{z_1-z_0})$.\n\n"\
            f"$\\left[{ten_vt},{ten_vt1} \\right].\\overrightarrow{{AB}}={m1*(x_1-x_0)+m2*(y_1-y_0)+m3*(z_1-z_0)}$."\
            f" Vậy ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ cắt nhau."

           )
        #Tạo các phương án
        pa_A= f"*${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
        pa_B= f"${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
        pa_C= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"
        pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"
        
    if chon==4:

        #Tạo bậc ngẫu nhiên
        x,y,z,t=sp.symbols("x y z t")
        a = random.choice([random.randint(-8, -1), random.randint(1, 8)])
        b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-7, -1), random.randint(1, 7)])   

        t_uc=ucln_ba_so(a,b,c)
        a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

        a1 = random.choice([random.randint(-8, -2), random.randint(1, 8)])
        b1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        c1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        t_uc=ucln_ba_so(a1,b1,c1)
        a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

        if a/a1==b/b1==c/c1:
            a1=abs(a1+1)

        x_0,y_0,z_0 = [random.randint(-8,8) for i in range(3)]
        x_1,y_1,z_1 = [random.randint(-8,8) for i in range(3)]
        
        ten_dt1=["d","\\Delta", "\\Delta_1"]
        ten_dt2=["d'","\\Delta'", "\\Delta_2"]
        i=random.randint(0,2)
        ten_dt1, ten_dt2=ten_dt1[i], ten_dt2[i] 

        u,u1=[a,b,c], [a1,b1,c1]
        m1,m2,m3=tich_co_huong(u,u1)
        if m1*(x_1-x_0)+m2*(y_1-y_0)+m3*(z_1-z_0) ==0:
            x_1=x_1+random.randint(1,3)
        ten_vt=f"\\overrightarrow{{u}}"
        ten_vt1=f"\\overrightarrow{{u_1}}"    

        dt1=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
        dt2=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"

        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${{{ten_dt1}}}:{dt1}$"\
                    f" \n\nvà ${{{ten_dt2}}}:{dt2}$. Xét vị trí tương đối của hai đường thẳng đã cho.")
        

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a};{b};{c})$.\n\n"\
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}=({a1};{b1};{c1})$.\n\n"\
            f"Ta có $\\overrightarrow{{u_2}}$ và $\\overrightarrow{{u_1}}$ khác phương nên ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ cắt nhau hoặc chéo nhau.\n\n"
            f"Đường thẳng ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ lần lượt đi qua $A({x_0};{y_0};{z_0})$ và $B({x_1};{y_1};{z_1})$.\n\n"\
            f"Ta có: $\\left[{ten_vt},{ten_vt1} \\right]=({m1};{m2};{m3}), \\overrightarrow{{AB}}=({x_1-x_0};{y_1-y_0};{z_1-z_0})$.\n\n"\
            f"$\\left[{ten_vt},{ten_vt1} \\right].\\overrightarrow{{AB}}={m1*(x_1-x_0)+m2*(y_1-y_0)+m3*(z_1-z_0)} \\ne 0$."\
            f" Vậy ${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau."

           )
        #Tạo các phương án
        pa_A= f"*${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ chéo nhau"
        pa_B= f"${{{ten_dt1}}}$ song song với ${{{ten_dt2}}}$"
        pa_C= f"${{{ten_dt1}}}$ cắt ${{{ten_dt2}}}$"
        pa_D= f"${{{ten_dt1}}}$ và ${{{ten_dt2}}}$ trùng nhau"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_24]-M4. Tìm đường thẳng đi qua điểm cắt và vuông góc với đường thẳng khác
def htd_25_xyz_L12_C5_B2_24():
   
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    b = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    if a==b==c: a=a+random.randint(2,3)
    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    #Tạo tọa độ điểm A và điểm cắt B

    x_0, y_0, z_0 = [random.randint(-6,6) for i in range(3)]
    x_1, y_1, z_1 =x_0+a, y_0+b, z_0+c

    #Tìm vectơ vuông góc với đường thẳng ban đầu
    b1,b2,b3=tim_vecto_vuong_goc(a, b, c)

    t_uc=ucln_ba_so(b1,b2,b3)
    b1,b2,b3=int(b1/t_uc),int(b2/t_uc),int(b3/t_uc)

    #Tạo điểm mới thuộc đường thẳng d1 là đường bị cắt
    m=random.choice([random.randint(-3, -1), random.randint(2, 3)])
    x_2 = x_1+b1*m
    y_2 = y_1+b2*m
    z_2 = z_1+b3*m
    #Tạo đường thẳng bị cắt
    dt1=f"\\dfrac{{{latex(x-x_2)}}}{{{b1}}}=\\dfrac{{{latex(y-y_2)}}}{{{b2}}}=\\dfrac{{{latex(z-z_2)}}}{{{b3}}}"
    
    ten_dt1=["d","\\Delta", "\\Delta_1"]
    ten_dt2=["d'","\\Delta'", "\\Delta_2"]
    ten_diem1=["A","E","M"]
    ten_diem2=["B","F","N"]
    i=random.randint(0,2)
    ten_dt1, ten_dt2, ten_diem1, ten_diem2 = ten_dt1[i], ten_dt2[i], ten_diem1[i], ten_diem2[i]
    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho điểm ${{{ten_diem1}({x_0};{y_0};{z_0})}}$ và đường thẳng ${{{ten_dt1}}}:{dt1}$.\n\n"\
                f"Đường thẳng ${{{ten_dt2}}}$ đi qua ${{{ten_diem1}}}$ cắt và vuông góc với đường thẳng ${{{ten_dt1}}}$ có phương trình là")

    kq=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({b1};{b2};{b3})$.\n\n"\
        f"Gọi ${ten_diem2}({latex(x_2+b1*t)};{latex(y_2+b2*t)};{latex(z_2+b3*t)} ) \\in {ten_dt2}$.\n\n"
        f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({latex(x_2+b1*t-x_0)};{latex(y_2+b2*t-y_0)};{latex(z_2+b3*t-z_0)})$.\n\n"\
        f"Do $\\overrightarrow{{{ten_diem1}{ten_diem2}}}\\bot\\overrightarrow{{u_1}}$ nên $\\overrightarrow{{{ten_diem1}{ten_diem2}}}.\\overrightarrow{{u_1}}=0\\Leftrightarrow {b1}({latex(x_2+b1*t-x_0)})+{b2}({latex(y_2+b2*t-y_0)})+{b3}({latex(z_2+b3*t-z_0)})=0\\Rightarrow t={-m}$.\n\n"
        f"Đường thẳng ${{{ten_dt2}}}$ qua điểm ${ten_diem1}({x_0};{y_0};{z_0})$ nhận $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({x_2+b1*m-x_0};{y_2+b2*m-y_0};{z_2+b3*m-z_0})$ hoặc $\\overrightarrow{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là\n\n"\
        f"${{{ten_dt2}}}:{kq}$.")

    
    kq2=f"\\dfrac{{{latex(x-x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
    kq3=f"\\dfrac{{{latex(x-x_0+random.randint(1,3))}}}{{{a}}}=\\dfrac{{{latex(y-y_0+random.randint(1,3))}}}{{{-b}}}=\\dfrac{{{latex(z-z_0-random.randint(1,3))}}}{{{c}}}"
    kq4=f"\\dfrac{{{latex(x-x_1+random.randint(1,3))}}}{{{b1}}}=\\dfrac{{{latex(y-y_1+random.randint(1,3))}}}{{{b2}}}=\\dfrac{{{latex(z-z_1-random.randint(1,3))}}}{{{b3}}}"

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D12_C5_B2_25]-M4. Tìm đường thẳng đi qua điểm, cắt đường thẳng khác và song song mặt phẳng
def htd_25_xyz_L12_C5_B2_25():
   
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    b = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    if a==b==c: a=a+random.randint(2,3)
    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    #Tạo tọa độ điểm A và điểm cắt B

    x_0, y_0, z_0 = [random.randint(-6,6) for i in range(3)]
    x_1, y_1, z_1 =x_0+a, y_0+b, z_0+c

    #Tạo điểm mới thuộc đường thẳng d1 là đường bị cắt
    a1 = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    a2 = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    a3 = random.choice([random.randint(-6, -1), random.randint(1, 7)])
    t_uc=ucln_ba_so(a1,a2,a3)
    a1,a2,a3=int(a1/t_uc),int(a2/t_uc),int(a3/t_uc)

    #Tạo đường thẳng cắt
    m=random.choice([random.randint(-2, -1), random.randint(1, 1)])
    x_2 = x_1+a1*m
    y_2 = y_1+a2*m
    z_2 = z_1+a3*m
    dt1=f"\\dfrac{{{latex(x-x_2)}}}{{{a1}}}=\\dfrac{{{latex(y-y_2)}}}{{{a2}}}=\\dfrac{{{latex(z-z_2)}}}{{{a3}}}"

    #Tạo mặt phẳng song song    
    b1,b2,b3=tim_vecto_vuong_goc(a, b, c)
    t_uc=ucln_ba_so(b1,b2,b3)
    b1,b2,b3=int(b1/t_uc),int(b2/t_uc),int(b3/t_uc)
    x_3 = x_0-a*m
    y_3 = y_0+b*m
    z_3 = z_0-c*m
    
    mp=latex(b1*(x-x_3)+b2*(y-y_3)+b3*(z-z_3))
    
    ten_dt1=["d","\\Delta", "\\Delta_1"]
    ten_dt2=["d'","\\Delta'", "\\Delta_2"]
    ten_diem1=["A","E","M"]
    ten_diem2=["B","F","N"]
    i=random.randint(0,2)
    ten_dt1, ten_dt2, ten_diem1, ten_diem2 = ten_dt1[i], ten_dt2[i], ten_diem1[i], ten_diem2[i]
    ten_mp=random.choice(["P", "Q", f"\\alpha", f"\\beta", f"\\gamma"])
    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho điểm ${{{ten_diem1}({x_0};{y_0};{z_0})}}$ và đường thẳng ${{{ten_dt1}}}:{dt1}$.\n\n"\
                f"Đường thẳng ${{{ten_dt2}}}$ đi qua ${{{ten_diem1}}}$ cắt đường thẳng ${{{ten_dt1}}}$ và song song với mặt phẳng $({{{ten_mp}}}):{mp}=0$ có phương trình là")

    kq=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({b1};{b2};{b3})$.\n\n"\
        f"Gọi ${ten_diem2}({latex(x_2+a1*t)};{latex(y_2+a2*t)};{latex(z_2+a3*t)} ) \\in {ten_dt1}$.\n\n"
        f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({latex(x_2+a1*t-x_0)};{latex(y_2+a2*t-y_0)};{latex(z_2+a3*t-z_0)})$.\n\n"\
        f"Mặt phẳng $({{{ten_mp}}}):{mp}=0$ có véctơ pháp tuyến là $\\overrightarrow{{n}}=({b1};{b2};{b3})$.\n\n"\
        f"Do $\\overrightarrow{{{ten_diem1}{ten_diem2}}}\\bot\\overrightarrow{{n}}$ nên $\\overrightarrow{{{ten_diem1}{ten_diem2}}}.\\overrightarrow{{n}}=0\\Leftrightarrow {b1}({latex(x_2+a1*t-x_0)})+{b2}({latex(y_2+a2*t-y_0)})+{b3}({latex(z_2+a3*t-z_0)})=0\\Rightarrow t={-m}$.\n\n"
        f"Đường thẳng ${{{ten_dt2}}}$ qua điểm ${ten_diem1}({x_0};{y_0};{z_0})$ nhận $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({x_2+a1*m-x_0};{y_2+a2*m-y_0};{z_2+a3*m-z_0})$ hoặc $\\overrightarrow{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là:\n\n"\
        f"${{{ten_dt2}}}:{kq}$.")

    
    kq2=f"\\dfrac{{{latex(x-x_0)}}}{{{-a}}}=\\dfrac{{{latex(y-y_0)}}}{{{-b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
    kq3=f"\\dfrac{{{latex(x-x_0+random.randint(1,3))}}}{{{a}}}=\\dfrac{{{latex(y-y_0+random.randint(1,3))}}}{{{-b}}}=\\dfrac{{{latex(z-z_0-random.randint(1,3))}}}{{{c}}}"
    kq4=f"\\dfrac{{{latex(x-x_1+random.randint(1,3))}}}{{{b1}}}=\\dfrac{{{latex(y-y_1+random.randint(1,3))}}}{{{b2}}}=\\dfrac{{{latex(z-z_1-random.randint(1,3))}}}{{{b3}}}"

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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
        
#[D12_C5_B2_26]-M4. Viết PTMP qua A,B cách M một khoảng lớn nhất
def htd_25_xyz_L12_C5_B2_26():
   
    x,y,z=sp.symbols("x y z")
    #Tạo véctơ pháp tuyến
    n1, n2, n3 = [random.choice([random.randint(-6, -1), random.randint(1, 7)]) for _ in range(3)]
    t_uc=ucln_ba_so(n1,n2,n3)
    n1, n2, n3=int(n1/t_uc),int(n2/t_uc),int(n3/t_uc)

    #Tạo điểm M
    x_m, y_m, z_m= [random.choice([random.randint(-6, -1), random.randint(1, 7)]) for _ in range(3)]
    if all([n1==x_m, n2==y_m, n3==z_m]): 
        x_m = x_m+random.randint(1,2)
        z_m = z_m-random.randint(1,2)
    ten_M=random.choice(["M", "N", "I"])

    #Tạo điểm K là hình chiếu của M:    
    x_k, y_k, z_k = x_m+n1, y_m+n2, z_m + n3

    #Tạo mặt phẳng (P)
    mp=f"{latex(n1*(x-x_k)+n2*(y-y_k)+n3*(z-z_k))} = 0"
    d=-n1*x_k-n2*y_k-n3*z_k
    ten_mp=random.choice(["P", "Q", f"\\alpha", f"\\beta", f"\\gamma"])

    #Tạo véctơ chỉ phương cho đường thẳng AB vuông góc với MK
    u1,u2,u3=tim_vecto_vuong_goc(n1, n2, n3)
    t_uc=ucln_ba_so(u1,u2,u3)
    u1,u2,u3=int(u1/t_uc),int(u2/t_uc),int(u3/t_uc)

    #Tạo tọa độ A,B
    t= 1
    a1,a2,a3 = x_k+t*u1, y_k+t*u2, z_k+t*u3
    t= -1
    b1,b2,b3 = x_k+t*u1, y_k+t*u2, z_k+t*u3  
    ten_A=random.choice(["A", "C", "E"])
    ten_B=random.choice(["B", "D", "F"])

    #Tạo hệ số nhân với pháp tuyến:
    a,b,c=[random.choice([random.randint(-4, -1), random.randint(1, 4)]) for _ in range(3)]
    e=random.randint(3, 10)
    T=a*n1+b*n2+c*n3+e

    
    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai điểm ${{{ten_A}({a1};{a2};{a3})}}$ và ${{{ten_B}({b1};{b2};{b3})}}$."\
                f" Gọi ${{({ten_mp})}}$ là mặt phẳng đi qua hai điểm ${{{ten_A}}}$, ${{{ten_B}}}$ và không đi qua điểm ${{{ten_M}({x_m};{y_m};{z_m})}}$ sao cho"\
                f" khoảng cách từ ${{{ten_M}}}$ đến mặt phẳng ${{({ten_mp})}}$ đạt giá trị lớn nhất. Biết ${{({ten_mp})}}:ax+by+cz+{d}$=0 với ${{a,b,c}}$ là các số nguyên."\
                f" Tính $T={a}a+{b}b+{c}c+{e}$.").replace("1a","a").replace("-1a","-a").replace("-1b","-b").replace("-1c","-c")

    kq=a*n1+b*n2+c*n3+e
    kq2=kq-random.randint(1,10)
    kq3=a+b+c+e
    kq4=kq+random.randint(1,5)
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
    t=sp.symbols("t")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Gọi ${{H}}$ là hình chiếu của điểm ${{{ten_M}}}$ trên ${{({ten_mp})}}$, ${{K}}$ là hình chiếu  của điểm ${{{ten_M}}}$ trên ${{{ten_A}{ten_B}}}$.\n\n"\
        f"Ta có: $d\\left({ten_M},({ten_mp})\\right)={ten_M}H \\le {ten_M}K$. Do ${{{ten_A},{ten_B}}}$ cố định nên ${{{ten_M}K}}$ không đổi.\n\n"\
        f"Suy ra $d\\left({ten_M},({ten_mp})\\right)$ đạt giá trị lớn nhất khi ${ten_M}H = {ten_M}K$.\n\n Khi đó $H \\equiv K$, hay ${{H}}$ là hình chiếu của điểm ${{{ten_M}}}$ trên ${{{ten_A}{ten_B}}}$.\n\n"\
        f"${{{ten_A}{ten_B}}}$ có véctơ chỉ phương là $\\overrightarrow{{{ten_A}{ten_B}}}=({b1-a1};{b2-a2};{b3-a3})$ hoặc $\\overrightarrow{{u}}=({u1};{u2};{u3})$.\n\n"\
        f"Gọi $H({a1}+{u1}t;{a2}+{u2}t;{a3}+{u3}t) \\in {{{ten_A}{ten_B}}}$.\n\n"\
        f"$\\overrightarrow{{{ten_M}H}}=({latex(a1+u1*t-x_m)};{latex(a2+u2*t-y_m)};{latex(a3+u3*t-z_m)})$.\n\n"\
        f"$\\overrightarrow{{{ten_M}H}}.\\overrightarrow{{u}}=0\\Leftrightarrow {u1}({latex(a1+u1*t-x_m)})+{u2}({latex(a2+u2*t-y_m)})+{u3}({latex(a3+u3*t-y_m)})=0 \\Leftrightarrow t={phan_so(-(a1-x_k)/u1)}.$\n\n"\
        f"Tọa độ điểm $H({x_k};{y_k};{z_k})$. ${{({ten_mp})}}$ có véctơ pháp tuyến là $\\overrightarrow{{{ten_M}H}}=({n1};{n2};{n3})$.\n\n"\
        f"Phương trình mặt phẳng ${{({ten_mp})}}:{n1}(x-{a1})+{n2}(y-{a2})+{n3}(z-{a3})=0\\Leftrightarrow {mp}$.\n\n"\
        f"Vậy: $T={a}a+{b}b+{c}c+{e}={T}$.").replace("1a","a").replace("-1a","-a").replace("-1b","-b").replace("-1c","-c")
    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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