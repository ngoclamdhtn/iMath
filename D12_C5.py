import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_three(x, y, z):
    return lcm(lcm(x, y), z)

def tao_3dinh_tamgiac():   
    
    a = random.choice([random.randint(-3, -1), random.randint(1, 3)])
    b = random.choice([random.randint(-3, -1), random.randint(1, 3)])
    c = random.choice([random.randint(-3, -1), random.randint(1, 3)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    x_0,y_0,z_0 = [random.randint(-2,2) for i in range(3)]
    if x_0==y_0==z_0==0:
        x_0= random.choice([i for i in range(-2, 2) if i!=0])
        y_0= random.choice([i for i in range(-2, 2) if i!=0])

    t1=random.choice([random.randint(-3, -1), random.randint(1, 3)])
    x_1 = x_0+a*t1
    y_1 = y_0+b*t1
    z_1 = z_0+c*t1

    t2=t1+random.randint(1,2)
    x_2 = x_0+a*t2
    y_2 = y_0+b*t2
    z_2 = z_0+c*t2

    t3=random.choice([random.randint(-3, -1), random.randint(1, 3)])
    x_3 = x_0+a*(t3+random.randint(1,2))
    y_3 = y_0+b*t3
    z_3 = z_0+c*(t3-random.randint(1,2))

    while x_1==0 or x_2==0 or z_1==z_2:
        t1=random.choice([random.randint(-3, -1), random.randint(1, 3)])
        x_1 = x_0+a*t1
        y_1 = y_0+b*t1
        z_1 = z_0+c*t1

        t2=t1+random.randint(1,2)
        x_2 = x_0+a*t2
        y_2 = y_0+b*t2
        z_2 = z_0+c*t2

    x=(x_1,y_1,z_1)
    y=(x_2,y_2,z_2)
    z=(x_3,y_3,z_3)
    return x,y,z

def tao_3dinh_tamgiacvuong():
    while True:
        # Tạo ngẫu nhiên ba điểm A, B, C trong khoảng [-6, 6]
        A = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        B = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        C = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))

        # Kiểm tra các điểm không trùng nhau
        if any([A[0]==B[0],A[1]==B[1],A[2]==B[2],
            A[0]==C[0],A[1]==C[1],A[2]==C[2],
            B[0]==C[0],B[1]==C[1],B[2]==C[2]]):
            continue

        # Tính các vectơ
        AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
        AC = (C[0] - A[0], C[1] - A[1], C[2] - A[2])
        BC = (C[0] - B[0], C[1] - B[1], C[2] - B[2])

        # Tính tích vô hướng của các cặp vectơ
        dot_AB_AC = AB[0]*AC[0] + AB[1]*AC[1] + AB[2]*AC[2]
        dot_AB_BC = AB[0]*BC[0] + AB[1]*BC[1] + AB[2]*BC[2]
        dot_AC_BC = AC[0]*BC[0] + AC[1]*BC[1] + AC[2]*BC[2]

        # Kiểm tra tam giác vuông
        if dot_AB_AC == 0:  # Vuông tại A
            return A, B, C
        elif dot_AB_BC == 0:  # Vuông tại B
            return B, C, A
        elif dot_AC_BC == 0:  # Vuông tại C
            return C, A, B

def tao_3dinh_tamgiacvuong_2():
    while True:
        # Tạo ngẫu nhiên ba điểm A, B, C trong khoảng [-6, 6]
        A = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        B = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))
        C = (random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6))

        # Kiểm tra các điểm không trùng nhau
        if any([A[0]==B[0],A[1]==B[1],A[2]==B[2],
            A[0]==C[0],A[1]==C[1],A[2]==C[2],
            B[0]==C[0],B[1]==C[1],B[2]==C[2]]):
            continue

        # Tính các vectơ
        AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
        AC = (C[0] - A[0], C[1] - A[1], C[2] - A[2])
        BC = (C[0] - B[0], C[1] - B[1], C[2] - B[2])

        # Tính tích vô hướng của các cặp vectơ
        dot_AB_AC = AB[0]*AC[0] + AB[1]*AC[1] + AB[2]*AC[2]
        dot_AB_BC = AB[0]*BC[0] + AB[1]*BC[1] + AB[2]*BC[2]
        dot_AC_BC = AC[0]*BC[0] + AC[1]*BC[1] + AC[2]*BC[2]

        # Kiểm tra tam giác vuông
        if dot_AB_AC == 0:  # Vuông tại A
            return A, B, C
        elif dot_AB_BC == 0:  # Vuông tại B
            return B, A, C
        elif dot_AC_BC == 0:  # Vuông tại C
            return C, A, B

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
    a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    c = random.choice([random.randint(-5, -1), random.randint(1, 5)])

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
    kq4=my_module.thay_dau_congtru(f"{latex(a*x+b*y+c*z-a*x_0-b*y_0-c*z_0+random.randint(1,5))}=0")

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
    ten_B=random.choice(["A","M", "E", "D"])
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
    a = random.choice([random.randint(-4, -1), random.randint(1, 4)])
    b = random.choice([random.randint(-4, -1), random.randint(1, 5)])
    c = random.choice([random.randint(-4, -1), random.randint(1, 4)])
    d = random.choice([random.randint(-4, -1), random.randint(1, 5)])

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)

    ten_mp1=random.choice(["(P)","(R)", f"(\\alpha)" ])
    ten_mp2=random.choice(["(Q)",  f"(\\beta)", f"(\\gamma)" ])   


    t2=random.choice([random.randint(-2, -1), random.randint(1, 2)])
    t3=random.randint(1,2)
    a2, b2, c2, d2= a*t2, b*t2, c*t2, d*t2+t3
    m=(d*t2+t3)/t2
    mp1=latex(a*x+b*y+c*z+d)
    mp2=latex(a2*x+b2*y+c2*z+d2)    

  
    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${ten_mp1}:{mp1}=0$ và mặt phẳng ${ten_mp2}:{mp2}=0$."\
                f" Khoảng cách giữa hai mặt phẳng đã cho bằng"

    kq=abs(t3/(t2*sqrt(a**2+b**2+c**2)))
    kq2=abs(d+d2)/sqrt(a**2+b**2+c**2)
    while True:        
        kq3=random.randint(1,10)/random.randint(12,20)
        kq4=random.randint(1,7)
        if all([kq3!=kq, kq3!=kq2,kq4!=kq,kq4!=kq2, kq4!=kq3]):
            break


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

    while True:
        x_I,y_I,z_I= random.randint(-7,7), random.randint(-7,7), random.randint(-7,7)
        if a1*x_I+b1*y_I+c1*z_I+d1 !=0:
            break

    noi_dung= f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({ten_mp})}}$ có phương trình ${mp}=0$."\
                f" Điểm nào trong các điểm sau không thuộc mặt phẳng ${{({ten_mp})}}$?"
    
    kq=f"{ten_A}({x_I};{y_I};{z_I})"
    kq2=f"{ten_B}({x_B};{y_B};{z_B})"
    kq3=f"{ten_C}({x_C};{y_C};{z_C})"
    kq4=f"{ten_D}({x_A};{y_A};{z_A})"


    noi_dung_loigiai=my_module.thay_dau_congtru(f"Thay tọa độ các điểm vào phương trình mặt phẳng ${{({ten_mp})}}$"
        f"ta thấy điểm ${ten_A}({x_I};{y_I};{z_I})$ không thỏa mãn phương trình nên điểm ${{{ten_A}}}$ không thuộc mặt phẳng ${{({ten_mp})}}$.\n")  

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
        HDG=f"Tọa độ điểm ${{{A}}}({x_A};{y_A};{z_A+t})$ không thỏa mãn phương trình ${ptmp_P}=0$ nên điểm ${{{A}}}$ không thuộc mặt phẳng ${{({mp_P})}}$."
    

    
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
    kq4_F=f"Góc giữa mặt phẳng ${{({mp_P})}}$ và mặt phẳng ${{({mp_Q})}}:{latex(a1*x+b1*y+c1*z+d1)}=0$ bằng ${goc_degree_false}^\\circ$" 
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
        
        kq3_T=f"* Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d1)}=0$ trùng nhau" 
        kq3_F=f"Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d1)}=0$ {random.choice(["cắt", "vuông góc", "song song" ])} nhau"
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
    kq4_F=(f"Mặt phẳng ${{({mp_Q})}}$ đi qua hai điểm ${B}({x_A};{y_A};{z_A}), {C}({x_B};{y_B};{z_B})$ và vuông góc với ${{({mp_P})}}$ có phương trình là "
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

#[D12_C5_B1_21]-M2. Cho mặt phẳng. Xét Đ-S: VTPT, điểm thuộc mp, vị trí hai mp, PTMP vuông góc (tổng hệ số)
def htd_25_xyz_L12_C5_B1_21():
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
        
        kq3_T=f"* Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d1)}=0$ trùng nhau" 
        kq3_F=f"Mặt phẳng ${{({mp_P})}}$ và mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d1)}=0$ {random.choice(["cắt", "vuông góc", "song song" ])} nhau"
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
    d1=-a1*x_A-b1*y_A-c1*z_A

    kq4_T=(f"* Mặt phẳng ${{({mp_Q})}}$ đi qua hai điểm ${B}({x_A};{y_A};{z_A}), {C}({x_B};{y_B};{z_B})$ và vuông góc với ${{({mp_P})}}$ có phương trình dạng"
        f"$ax+by+cz+{d1}=0$. Khi đó $a+b+c={a1+b1+c1}$"
        )
    kq4_F=(f"Mặt phẳng ${{({mp_Q})}}$ đi qua hai điểm ${B}({x_A};{y_A};{z_A}), {C}({x_B};{y_B};{z_B})$ và vuông góc với ${{({mp_P})}}$ có phương trình dạng"
        f"$ax+by+cz+{d1}=0$. Khi đó $a+b+c={a1+b1+c1+random.randint(1,2)}$"
        ) 
    kq4=random.choice([kq4_T, kq4_F])
    kq4=kq4.replace("+-","-")
    HDG=(f"${vec(f"n_{mp_P}")}=({a};{b};{c}), {vec2(B,C)}=({x_AB};{y_AB};{z_AB})$.\n\n"
        f"Mặt phẳng ${{({mp_Q})}}$ nhận ${vec(f"n_{mp_P}")},{vec2(B,C)}$ làm cặp véctơ chỉ phương.\n\n"
        f"$[{vec(f"n_{mp_P}")},{vec2(B,C)}]=({a1};{b1};{c1})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_Q})}}$.\n\n"        
        f"Phương trình ${{({mp_Q})}}:{a1}({latex(x-x_A)})+{b1}({latex(y-y_A)})+{c1}({latex(z-z_A)})=0$"
        f" $\\Leftrightarrow {latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A))}=0$.\n\n"
        f"Khi đó: $a+b+c={a1+b1+c1}.$"      
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

#[D12_C5_B1_22]-SA-M3. Cho mp(P). Viết mp(Q) qua A,B vuông góc voi mp(P)(tổng hệ số)
def htd_25_xyz_L12_C5_B1_22():
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
    

    x_A,y_A,z_A=x_A+random.randint(1,2),y_A,z_A
    x_B,y_B,z_B=x_B,y_B+random.randint(1,2),z_B

    x_AB,y_AB,z_AB=x_B-x_A,y_B-y_A,z_B-z_A
    m=[x_AB, y_AB, z_AB]
    n=[a, b, c]
    
    a1,b1,c1=tich_co_huong(m,n)
    d1=-a1*x_A-b1*y_A-c1*z_A
    noi_dung= (f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({mp_P})}}$ có phương trình ${ptmp_P}=0$."
        f" Mặt phẳng ${{({mp_Q})}}$ đi qua hai điểm ${B}({x_A};{y_A};{z_A}), {C}({x_B};{y_B};{z_B})$ và vuông góc với ${{({mp_P})}}$ có phương trình dạng $ax+by+cz+{d1}=0$. Tính ${{a+b+c}}$." )
    noi_dung=noi_dung.replace("+-","-")

    dap_an=a1+b1+c1
    noi_dung_loigiai=(f"${vec(f"n_{mp_P}")}=({a};{b};{c}), {vec2(B,C)}=({x_AB};{y_AB};{z_AB})$.\n\n"
        f"Mặt phẳng ${{({mp_Q})}}$ nhận ${vec(f"n_{mp_P}")},{vec2(B,C)}$ làm cặp véctơ chỉ phương.\n\n"
        f"$[{vec(f"n_{mp_P}")},{vec2(B,C)}]=({a1};{b1};{c1})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_Q})}}$.\n\n"        
        f"Phương trình ${{({mp_Q})}}:{a1}({latex(x-x_A)})+{b1}({latex(y-y_A)})+{c1}({latex(z-z_A)})=0$"
        f" $\\Leftrightarrow {latex(a1*(x-x_A)+b1*(y-y_A)+c1*(z-z_A))}=0$.\n\n"
        f"Khi đó: $a+b+c={a1+b1+c1}.$"      
        )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_23]-SA-M3. Cho mp(P). Viết mp(Q) qua A và song song voi mp(P)(tổng hệ số)
def htd_25_xyz_L12_C5_B1_23():
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
    

    x_B,y_B,z_B=x_B+random.randint(1,2),y_B,z_B
    d1=-a*x_B-b*y_B-c*z_B
        
    
    noi_dung= (f"Trong không gian ${{Oxyz}}$, cho mặt phẳng ${{({mp_P})}}$ có phương trình ${ptmp_P}=0$."
        f" Mặt phẳng ${{({mp_Q})}}$ đi qua điểm ${B}({x_B};{y_B};{z_B})$ và song song với ${{({mp_P})}}$ có phương trình dạng ${a}x+ay+bz+c=0$. Tính ${{a+b+c}}$." )
    noi_dung=noi_dung.replace("+-","-")

    dap_an=b+c+d1
    noi_dung_loigiai=(
        f"Mặt phẳng ${{({mp_Q})}}$ nhận ${vec(f"n_{mp_P}")}=({a};{b};{c})$ làm một véctơ pháp tuyến.\n\n"            
        f"Phương trình ${{({mp_Q})}}:{a}({latex(x-x_B)})+{b}({latex(y-y_B)})+{c}({latex(z-z_B)})=0$"
        f" $\\Leftrightarrow {latex(a*(x-x_B)+b*(y-y_B)+c*(z-z_B))}=0$.\n\n"
        f"Khi đó: $a+b+c={b+c+d1}$."      
        )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_24]-SA-M3. Mp(P) qua A và chứa trục tọa độ. Tính khoảng cách từ B đến (P)
def htd_25_xyz_L12_C5_B1_24():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z") 
    ten_mp=["P","Q", "R", "\\alpha","\\beta", "\\gamma"]
    random.shuffle(ten_mp)
    mp_P, mp_Q=ten_mp[0:2]

    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,I,M=ten_diem[0:5]

    while True:
        x_A,y_A,z_A = [random.randint(-6,6) for i in range(3)]
        x_B,y_B,z_B = [random.randint(-7,7) for i in range(3)]             

        if all([x_A!=0, y_A!=0, z_A!=0, x_B!=x_A, y_B!=y_A, z_B!=z_A]):            
            break      

    chon=random.randint(1,3)
    if chon==1:
        m=[x_A, y_A, z_A]
        n=[1, 0, 0]
        
        a,b,c=tich_co_huong(m,n)
        d=-a*x_A-b*y_A-c*z_A
        ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A)) 

        
        noi_dung= (f"Trong không gian ${{Oxyz}}$, cho hai điểm ${A}({x_A};{y_A};{z_A}),{B}({x_B};{y_B};{z_B})$."
            f" Mặt phẳng ${{({mp_P})}}$ qua ${{{A}}}$ và chứa trục ${{Ox}}$. Tính khoảng cách từ điểm ${{{B}}}$ đến mặt phẳng ${{({mp_P})}}$ (kết quả làm tròn đến hàng phần mười)."
            )
        noi_dung=noi_dung.replace("+-","-").replace("+0","")

        khoang_cach=latex(nsimplify(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2)))
        dap_an=f"{round_half_up(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2),1):.1f}".replace(".",",")

        noi_dung_loigiai=(f"${vec(f"O{A}")}=({x_A};{y_A};{z_A}), {vec("i")}=(1;0;0)$.\n\n"
            f"Mặt phẳng ${{({mp_P})}}$ nhận ${vec(f"O{A}")},{vec("i")}$ làm cặp véctơ chỉ phương.\n\n"
            f"$[{vec(f"O{A}")},{vec("i")}]=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_P})}}$.\n\n"        
            f"Phương trình ${{({mp_P})}}:{a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0$"
            f" $\\Leftrightarrow {ptmp_P}=0$.\n\n"
            f"$d\\left({B},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_B)}+{show_tich(b,y_B)}+{show_tich(c,z_B)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}={dap_an}$."      
            )

    if chon==2:
        m=[x_A, y_A, z_A]
        n=[0, 1, 0]
        
        a,b,c=tich_co_huong(m,n)
        d=-a*x_A-b*y_A-c*z_A
        ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A)) 

        
        noi_dung= (f"Trong không gian ${{Oxyz}}$, cho hai điểm ${A}({x_A};{y_A};{z_A}),{B}({x_B};{y_B};{z_B})$."
            f" Mặt phẳng ${{({mp_P})}}$ qua ${{{A}}}$ và chứa trục ${{Oy}}$. Tính khoảng cách từ điểm ${{{B}}}$ đến mặt phẳng ${{({mp_P})}}$ (kết quả làm tròn đến hàng phần mười)."
            )
        noi_dung=noi_dung.replace("+-","-").replace("+0","")

        khoang_cach=latex(nsimplify(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2)))
        dap_an=f"{round_half_up(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2),1):.1f}".replace(".",",")

        noi_dung_loigiai=(f"${vec(f"O{A}")}=({x_A};{y_A};{z_A}), {vec("j")}=(0;1;0)$.\n\n"
            f"Mặt phẳng ${{({mp_P})}}$ nhận ${vec(f"O{A}")},{vec("j")}$ làm cặp véctơ chỉ phương.\n\n"
            f"$[{vec(f"O{A}")},{vec("j")}]=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_P})}}$.\n\n"        
            f"Phương trình ${{({mp_P})}}:{a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0$"
            f" $\\Leftrightarrow {ptmp_P}=0$.\n\n"
            f"$d\\left({B},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_B)}+{show_tich(b,y_B)}+{show_tich(c,z_B)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}={dap_an}$."      
            )

    if chon==3:
        m=[x_A, y_A, z_A]
        n=[0, 0, 1]
        
        a,b,c=tich_co_huong(m,n)
        d=-a*x_A-b*y_A-c*z_A
        ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A)) 

        
        noi_dung= (f"Trong không gian ${{Oxyz}}$, cho hai điểm ${A}({x_A};{y_A};{z_A}),{B}({x_B};{y_B};{z_B})$."
            f" Mặt phẳng ${{({mp_P})}}$ qua ${{{A}}}$ và chứa trục ${{Oz}}$. Tính khoảng cách từ điểm ${{{B}}}$ đến mặt phẳng ${{({mp_P})}}$ (kết quả làm tròn đến hàng phần mười)."
            )
        noi_dung=noi_dung.replace("+-","-").replace("+0","")

        khoang_cach=latex(nsimplify(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2)))
        dap_an=f"{round_half_up(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2),1):.1f}".replace(".",",")

        noi_dung_loigiai=(f"${vec(f"O{A}")}=({x_A};{y_A};{z_A}), {vec("k")}=(0;0;1)$.\n\n"
            f"Mặt phẳng ${{({mp_P})}}$ nhận ${vec(f"O{A}")},{vec("k")}$ làm cặp véctơ chỉ phương.\n\n"
            f"$[{vec(f"O{A}")},{vec("k")}]=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_P})}}$.\n\n"        
            f"Phương trình ${{({mp_P})}}:{a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0$"
            f" $\\Leftrightarrow {ptmp_P}=0$.\n\n"
            f"$d\\left({B},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_B)}+{show_tich(b,y_B)}+{show_tich(c,z_B)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}={dap_an}$."      
            )
    
    
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_25]-SA-M3. Mp(P) qua A,B và song song trục tọa độ. Tính khoảng cách từ B đến (P)
def htd_25_xyz_L12_C5_B1_25():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z") 
    ten_mp=["P","Q", "R", "\\alpha","\\beta", "\\gamma"]
    random.shuffle(ten_mp)
    mp_P, mp_Q=ten_mp[0:2]

    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,I,M=ten_diem[0:5]

    while True:
        x_A,y_A,z_A = [random.randint(-6,6) for i in range(3)]
        x_B,y_B,z_B = [random.randint(-7,7) for i in range(3)]
        x_C,y_C,z_C = [random.randint(-7,7) for i in range(3)]         

        if all([x_A!=0, y_A!=0, z_A!=0, x_B!=x_A, y_B!=y_A, z_B!=z_A,
            x_C not in [x_A,x_B], y_C not in [y_A,y_B]]):            
            break     

    chon=random.randint(1,3)
    
    if chon==1:
        x_AB,y_AB,z_AB=x_B-x_A,y_B-y_A,z_B-z_A
        m=[x_AB, y_AB, z_AB]
        n=[1, 0, 0]
        
        a,b,c=tich_co_huong(m,n)
        d=-a*x_A-b*y_A-c*z_A
        ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A)) 

        
        noi_dung= (f"Trong không gian ${{Oxyz}}$, cho các điểm ${A}({x_A};{y_A};{z_A}),{B}({x_B};{y_B};{z_B}),{C}({x_C};{y_C};{z_C})$."
            f" Mặt phẳng ${{({mp_P})}}$ qua ${{{A},{B}}}$ và song song ${{Ox}}$. Tính khoảng cách từ điểm ${{{C}}}$ đến mặt phẳng ${{({mp_P})}}$ (kết quả làm tròn đến hàng phần mười)."
            )
        noi_dung=noi_dung.replace("+-","-").replace("+0","")

        khoang_cach=latex(nsimplify(abs(a*x_C+b*y_C+c*z_C+d)/sqrt(a**2+b**2+c**2)))
        dap_an=f"{round_half_up(abs(a*x_C+b*y_C+c*z_C+d)/sqrt(a**2+b**2+c**2),1):.1f}".replace(".",",")

        noi_dung_loigiai=(f"${vec2(A,B)}=({x_AB};{y_AB};{z_AB}), {vec("i")}=(1;0;0)$.\n\n"
            f"Mặt phẳng ${{({mp_P})}}$ nhận ${vec2(A,B)},{vec("i")}$ làm cặp véctơ chỉ phương.\n\n"
            f"$[{vec2(A,B)},{vec("i")}]=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_P})}}$.\n\n"        
            f"Phương trình ${{({mp_P})}}:{a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0$"
            f" $\\Leftrightarrow {ptmp_P}=0$.\n\n"
            f"$d\\left({C},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_C)}+{show_tich(b,y_C)}+{show_tich(c,z_C)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}={dap_an}$."      
            )

    if chon==2:
        x_AB,y_AB,z_AB=x_B-x_A,y_B-y_A,z_B-z_A
        m=[x_AB, y_AB, z_AB]
        n=[0, 1, 0]
        
        a,b,c=tich_co_huong(m,n)
        d=-a*x_A-b*y_A-c*z_A
        ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A)) 

        
        noi_dung= (f"Trong không gian ${{Oxyz}}$, cho các điểm ${A}({x_A};{y_A};{z_A}),{B}({x_B};{y_B};{z_B}),{C}({x_C};{y_C};{z_C})$."
            f" Mặt phẳng ${{({mp_P})}}$ qua ${{{A},{B}}}$ và song song ${{Oy}}$. Tính khoảng cách từ điểm ${{{C}}}$ đến mặt phẳng ${{({mp_P})}}$ (kết quả làm tròn đến hàng phần mười)."
            )
        noi_dung=noi_dung.replace("+-","-").replace("+0","")

        khoang_cach=latex(nsimplify(abs(a*x_C+b*y_C+c*z_C+d)/sqrt(a**2+b**2+c**2)))
        dap_an=f"{round_half_up(abs(a*x_C+b*y_C+c*z_C+d)/sqrt(a**2+b**2+c**2),1):.1f}".replace(".",",")

        noi_dung_loigiai=(f"${vec2(A,B)}=({x_AB};{y_AB};{z_AB}), {vec("j")}=(0;1;0)$.\n\n"
            f"Mặt phẳng ${{({mp_P})}}$ nhận ${vec2(A,B)},{vec("j")}$ làm cặp véctơ chỉ phương.\n\n"
            f"$[{vec2(A,B)},{vec("j")}]=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_P})}}$.\n\n"        
            f"Phương trình ${{({mp_P})}}:{a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0$"
            f" $\\Leftrightarrow {ptmp_P}=0$.\n\n"
            f"$d\\left({C},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_C)}+{show_tich(b,y_C)}+{show_tich(c,z_C)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}={dap_an}$."      
            )
    
    if chon==3:
        x_AB,y_AB,z_AB=x_B-x_A,y_B-y_A,z_B-z_A
        m=[x_AB, y_AB, z_AB]
        n=[0, 0, 1]
        
        a,b,c=tich_co_huong(m,n)
        d=-a*x_A-b*y_A-c*z_A
        ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A)) 

        
        noi_dung= (f"Trong không gian ${{Oxyz}}$, cho các điểm ${A}({x_A};{y_A};{z_A}),{B}({x_B};{y_B};{z_B}),{C}({x_C};{y_C};{z_C})$."
            f" Mặt phẳng ${{({mp_P})}}$ qua ${{{A},{B}}}$ và song song ${{Oz}}$. Tính khoảng cách từ điểm ${{{C}}}$ đến mặt phẳng ${{({mp_P})}}$ (kết quả làm tròn đến hàng phần mười)."
            )
        noi_dung=noi_dung.replace("+-","-").replace("+0","")

        khoang_cach=latex(nsimplify(abs(a*x_C+b*y_C+c*z_C+d)/sqrt(a**2+b**2+c**2)))
        dap_an=f"{round_half_up(abs(a*x_C+b*y_C+c*z_C+d)/sqrt(a**2+b**2+c**2),1):.1f}".replace(".",",")

        noi_dung_loigiai=(f"${vec2(A,B)}=({x_AB};{y_AB};{z_AB}), {vec("k")}=(0;0;1)$.\n\n"
            f"Mặt phẳng ${{({mp_P})}}$ nhận ${vec2(A,B)},{vec("k")}$ làm cặp véctơ chỉ phương.\n\n"
            f"$[{vec2(A,B)},{vec("k")}]=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_P})}}$.\n\n"        
            f"Phương trình ${{({mp_P})}}:{a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0$"
            f" $\\Leftrightarrow {ptmp_P}=0$.\n\n"
            f"$d\\left({C},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_C)}+{show_tich(b,y_C)}+{show_tich(c,z_C)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}={dap_an}$."      
            )
    
    
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_26]-SA-M3. Mp(P) qua A và vuông góc với (Q),(R). Tính khoảng cách từ B đến (P)
def htd_25_xyz_L12_C5_B1_26():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z") 
    ten_mp=["P","Q", "R", "\\alpha","\\beta", "\\gamma"]
    random.shuffle(ten_mp)
    mp_P, mp_Q, mp_R=ten_mp[0:3]

    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B=ten_diem[0:2]


    while True:        
        a1,b1,c1 = [random.randint(-5,5) for i in range(3)]
        a2,b2,c2 = [random.randint(-5,5) for i in range(3)]
        m=[a1,b1,c1]
        n=[a2,b2,c2]    
        a,b,c=tich_co_huong(m,n)       

        if all([a1!=a2, b1!= b2, a!=0, b!=0]):            
            break

    t=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t),int(b1/t),int(c1/t)

    t=ucln_ba_so(a2,b2,c2)
    a2,b2,c2=int(a2/t),int(b2/t),int(c2/t)

    d1=random.randint(-10,10)
    d2 = random.choice([i for i in range(-10, 10) if i!=0])

    m=[a1,b1,c1]
    n=[a2,b2,c2]    
    a,b,c=tich_co_huong(m,n)
    
    while True:
        x_A,y_A,z_A = [random.randint(-4,4) for i in range(3)]
        x_B,y_B,z_B = [random.randint(-6,6) for i in range(3)]
        if all([x_A!=x_B, y_A!=y_B, a*(x_B-x_A)+b*(y_B-y_A)+c*(z_B-z_A)!=0]):            
            break

    d=-a*x_A-b*y_A-c*z_A
    ptmp_P=latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A))

    
    noi_dung= (f"Trong không gian ${{Oxyz}}$,"
        f" mặt phẳng ${{({mp_P})}}$ qua điểm ${A}({x_A};{y_A};{z_A})$ và vuông góc với hai mặt phẳng $({mp_Q}):{latex(a1*x+b1*y+c1*z+d1)}=0$ và $({mp_R}):{latex(a2*x+b2*y+c2*z+d2)}=0$."
        f" Tính khoảng cách từ điểm ${B}({x_B};{y_B};{z_B})$ đến mặt phẳng ${{({mp_P})}}$ (kết quả làm tròn đến hàng phần mười)."
        )
    noi_dung=noi_dung.replace("+-","-").replace("+0","")

    khoang_cach=latex(nsimplify(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2)))
    dap_an=f"{round_half_up(abs(a*x_B+b*y_B+c*z_B+d)/sqrt(a**2+b**2+c**2),1):.1f}".replace(".",",")

    noi_dung_loigiai=(f"${vec(f"n_{{{mp_Q}}}")}=({a1};{b1};{c1}), {vec(f"n_{{{mp_R}}}")}=({a2};{b2};{c2})$.\n\n"
        f"Mặt phẳng ${{({mp_P})}}$ nhận ${vec(f"n_{{{mp_Q}}}")},{vec(f"n_{{{mp_R}}}")}$ làm cặp véctơ chỉ phương.\n\n"
        f"$[{vec(f"n_{{{mp_Q}}}")},{vec(f"n_{{{mp_R}}}")}]=({a};{b};{c})$ là một véctơ pháp tuyến của mặt phẳng ${{({mp_P})}}$.\n\n"        
        f"Phương trình ${{({mp_P})}}:{a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0$"
        f" $\\Leftrightarrow {ptmp_P}=0$.\n\n"
        f"$d\\left({B},({mp_P})\\right)=\\dfrac{{|{show_tich(a,x_B)}+{show_tich(b,y_B)}+{show_tich(c,z_B)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={khoang_cach}={dap_an}$."      
        )

    
    
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_27]-SA-M3. Mặt phẳng (P) đi qua 3 điểm A,B,C. Tính tổng hệ số
def htd_25_xyz_L12_C5_B1_27():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")    

    while True:
        x_A,y_A,z_A = [random.randint(-6,7) for i in range(3)]
        x_B,y_B,z_B = [random.randint(-5,6) for i in range(3)]
        x_C,y_C,z_C = [random.randint(-5,6) for i in range(3)]

        x_AB,y_AB,z_AB=x_B-x_A,y_B-y_A,z_B-z_A
        x_AC,y_AC,z_AC=x_C-x_A,y_C-y_A,z_C-z_A

        m=[x_AB,y_AB,z_AB]
        n=[x_AC,y_AC,z_AC]    
        a,b,c=tich_co_huong(m,n)     

        if all([x_B!=x_A, y_B!=y_A,
            x_C not in [x_A, x_B], z_C not in [z_A,z_B],
            a!=0,b!=0,c!=0]):            
            break

    m=[x_AB,y_AB,z_AB]
    n=[x_AC,y_AC,z_AC]    
    a,b,c=tich_co_huong(m,n)

    t=ucln_ba_so(a,b,c)
    a,b,c=int(a/t),int(b/t),int(c/t)


    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,M=ten_diem[0:4]

    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])
    
    vec_AB, vec_AC=f"\\overrightarrow{{{A}{B}}}", f"\\overrightarrow{{{A}{C}}}"
    d=-a*x_A-b*y_A-c*z_A
    dap_an=a+b+c
    noi_dung= (
    f"Trong không gian ${{Oxyz}}$, mặt phẳng ${{({mp_P})}}$ đi qua ba điểm ${A}({x_A};{y_A};{z_A})$, "
        f" ${B}({x_B};{y_B};{z_B})$ và ${C}({x_C};{y_C};{z_C})$ có phương trình dạng $ax+by+c+{d}=0$."
        f" Tính tổng ${{a+b+c}}$.")
    noi_dung=noi_dung.replace("+-","-").replace("+0","")

    ptmp_P= f"{latex(a*(x-x_A)+b*(y-y_A)+c*(z-z_A))}=0"


    noi_dung_loigiai=my_module.thay_dau_congtru(f"Ta có: ${vec_AB}=({x_B-x_A};{y_B-y_A};{z_B-z_A}), {vec_AC}=({x_C-x_A};{y_C-y_A};{z_C-z_A})$.\n\n"\
        f"Mặt phẳng ${{({mp_P})}}$ nhận $\\overrightarrow{{n}}=\\left[{vec_AB}, {vec_AC}\\right]=({a};{b};{c})$ làm một véctơ pháp tuyến.\n\n"
        f"Mặt phẳng ${{({mp_P})}}$ qua điểm ${A}({x_A};{y_A};{z_A})$.\n\n"
        f"Mặt phẳng ${{({mp_P})}}$ có phương trình là:\n\n"\
        f" ${a}({latex(x-x_A)})+{b}({latex(y-y_A)})+{c}({latex(z-z_A)})=0\\Leftrightarrow {ptmp_P}$.\n\n"
        f"$a+b+c={dap_an}$.")

    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("+0","")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_28]-SA-M3. Cho mặt phẳng (P). Tính diện tích tam giác khi mp cắt 3 trục tọa độ
def htd_25_xyz_L12_C5_B1_28():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.randint(-10,11)    
    ptmp_P=f"{latex(a*x+b*y+c*z+d)}=0"   

    x_A,y_A,z_A=-d/a,0,0
    x_B,y_B,z_B=0,-d/b,0
    x_C,y_C,z_C=0,0,-d/c
    x_AB,y_AB,z_AB=x_B-x_A, y_B-y_A, z_B-z_A
    x_AC,y_AC,z_AC=x_C-x_A, y_C-y_A, z_C-z_A
    x_BC,y_BC,z_BC=x_C-x_B, y_C-y_B, z_C-z_B

    m=[d/a,-d/b,0]
    n=[d/a,0,-d/c]   
    a,b,c=tich_co_huong(m,n)


    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,M=ten_diem[0:4]

    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])
    
    vec_AB, vec_AC, vec_BC=f"\\overrightarrow{{{A}{B}}}", f"\\overrightarrow{{{A}{C}}}", f"\\overrightarrow{{{B}{C}}}"
    
    dap_an=f"{round_half_up(sqrt(a**2+b**2+c**2)/2,1):.1f}".replace(".",",")
    noi_dung= (
    f"Trong không gian ${{Oxyz}}$, cho mặt phẳng $({mp_P}):{ptmp_P}=0$ "
        f" Mặt phẳng $({mp_P})$ cắt các trục ${{Ox,Oy,Oz}}$ tại các điểm ${{{A},{B},{C}}}$."
        f" Tính diện tích tam giác ${{{A}{B}{C}}}$(kết quả làm tròn đến hàng phần mười).") 

    noi_dung_loigiai=my_module.thay_dau_congtru(
        f"Mặt phẳng $({mp_P})$ cắt các trục ${{Ox,Oy,Oz}}$ tại ${A}({phan_so(x_A)};0;0),{B}(0;{phan_so(y_B)};0), {C}(0;0;{phan_so(z_C)})$.\n\n"
        f"${vec_AB}=({phan_so(x_B-x_A)};{phan_so(y_B-y_A)};{phan_so(z_B-z_A)}), {vec_AC}=({phan_so(x_C-x_A)};{phan_so(y_C-y_A)};{phan_so(z_C-z_A)})$,"
        f"${vec_BC}=({phan_so(x_C-x_A)};{phan_so(y_C-y_A)};{phan_so(z_C-z_A)})$.\n\n"
        f"${A}{B}={latex(nsimplify(sqrt(x_AB**2+y_AB**2+z_AB**2)))}$, ${A}{C}={latex(nsimplify(sqrt(x_AC**2+y_AC**2+z_AC**2)))}$, "
        f"${B}{C}={latex(nsimplify(sqrt(x_BC**2+y_BC**2+z_BC**2)))}$.\n\n"
        f" Áp dụng công thức Hê-rông: $S=\\sqrt{{(p-{A}{B}).(p-{A}{C}).(p-{B}{C})}}$ với $p=\\dfrac{{{A}{B}+{A}{C}+{B}{C}}}{{2}}$\n\n"
        f" tính được S={dap_an}."       
        )

    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("+0","")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_29]-SA-M3. Cho mặt phẳng (P). Tính chu vi tam giác khi mp cắt 3 trục tọa độ
def htd_25_xyz_L12_C5_B1_29():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")    

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.randint(-10,11)
    ptmp_P=f"{latex(a*x+b*y+c*z+d)}=0"   

    x_A,y_A,z_A=-d/a,0,0
    x_B,y_B,z_B=0,-d/b,0
    x_C,y_C,z_C=0,0,-d/c
    x_AB,y_AB,z_AB=x_B-x_A, y_B-y_A, z_B-z_A
    x_AC,y_AC,z_AC=x_C-x_A, y_C-y_A, z_C-z_A
    x_BC,y_BC,z_BC=x_C-x_B, y_C-y_B, z_C-z_B

    m=[d/a,-d/b,0]
    n=[d/a,0,-d/c]   
    a,b,c=tich_co_huong(m,n)


    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,M=ten_diem[0:4]

    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])
    
    vec_AB, vec_AC, vec_BC=f"\\overrightarrow{{{A}{B}}}", f"\\overrightarrow{{{A}{C}}}", f"\\overrightarrow{{{B}{C}}}"
    
    AB=sqrt(x_AB**2+y_AB**2+z_AB**2)
    AC=sqrt(x_AC**2+y_AC**2+z_AC**2)
    BC=sqrt(x_BC**2+y_BC**2+z_BC**2)
    dap_an=f"{round_half_up(AB+AC+BC,1):.1f}".replace(".",",")
    noi_dung= (
    f"Trong không gian ${{Oxyz}}$, cho mặt phẳng $({mp_P}):{ptmp_P}=0$ "
        f" Mặt phẳng $({mp_P})$ cắt các trục ${{Ox,Oy,Oz}}$ tại các điểm ${{{A},{B},{C}}}$."
        f" Tính chu vi tam giác ${{{A}{B}{C}}}$(kết quả làm tròn đến hàng phần mười).")


    noi_dung_loigiai=my_module.thay_dau_congtru(
        f"Mặt phẳng $({mp_P})$ cắt các trục ${{Ox,Oy,Oz}}$ tại ${A}({phan_so(x_A)};0;0),{B}(0;{phan_so(y_B)};0), {C}(0;0;{phan_so(z_C)})$.\n\n"
        f"${vec_AB}=({phan_so(x_B-x_A)};{phan_so(y_B-y_A)};{phan_so(z_B-z_A)}), {vec_AC}=({phan_so(x_C-x_A)};{phan_so(y_C-y_A)};{phan_so(z_C-z_A)})$,"
        f"${vec_BC}=({phan_so(x_C-x_A)};{phan_so(y_C-y_A)};{phan_so(z_C-z_A)})$.\n\n"
        f"${A}{B}={latex(nsimplify(sqrt(x_AB**2+y_AB**2+z_AB**2)))}$, ${A}{C}={latex(nsimplify(sqrt(x_AC**2+y_AC**2+z_AC**2)))}$, "
        f"${B}{C}={latex(nsimplify(sqrt(x_BC**2+y_BC**2+z_BC**2)))}$.\n\n"
        f" Chu vi tam giác: ${A}{B}+{A}{C}+{B}{C}={latex(nsimplify(AB))}+{latex(nsimplify(AC))}+{latex(nsimplify(BC))}={dap_an}$\n\n"             
        )

    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("+0","")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_30]-SA-M3. Tìm hình chiếu của điểm lên mặt phẳng.
def htd_25_xyz_L12_C5_B1_30():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")    

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.randint(-10,11)
    ptmp_P=f"{latex(a*x+b*y+c*z+d)}=0"   

    
    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,H=ten_diem[0:2]

    while True:
        x_A,y_A,z_A=random.randint(-6,6),random.randint(-6,6),random.randint(-6,6)
        if a*x_A+b*y_A+c*z_A+d !=0:
            break

    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])
    
    
    noi_dung= (
    f"Trong không gian ${{Oxyz}}$, cho mặt phẳng $({mp_P}):{ptmp_P}$ và điểm ${A}({x_A};{y_A};{z_A})$."
        f" Biết ${H}(a;b;c)$ là hình chiếu của điểm ${{{A}}}$ lên mặt phẳng ${{({mp_P})}}$."
        f" Tính ${{a+b+c}}$ (kết quả làm tròn đến hàng phần mười).")

    t=sp.symbols("t")
    eq=Eq(a*(x_A+a*t)+b*(y_A+b*t)+c*(z_A+c*t)+d,0)
    solution=solve(eq,t)

    t=solution[0]
    x_H,y_H,z_H = x_A+a*t, y_A+b*t, z_A+c*t

    dap_an=f"{round_half_up(x_H+y_H+z_H,1):.1f}".replace(".",",")
    noi_dung_loigiai=my_module.thay_dau_congtru(
        f"$(P)$ nhận ${vec("n")}=({a};{b};{c})$ làm một véctơ pháp tuyến.\n\n"
        f"${vec2(A,H)}=(a-{x_A};b-{y_A};c-{z_A})$ cùng phương với ${vec("n")}$ nên:\n\n"
        f"${vec2(A,H)}=t{vec("n")}\\Rightarrow a={x_A}+{a}t,b={y_A}+{b}t,c={z_A}+{c}t$.\n\n"
        f"${H} \\in ({mp_P}) \\Rightarrow {a}({x_A}+{a}t)+{b}({y_A}+{b}t)+{c}({z_A}+{c}t)+{d}=0$.\n\n"
        f"$\\Rightarrow t={phan_so(t)} \\Rightarrow {H}({phan_so(x_H)};{phan_so(y_H)};{phan_so(z_H)})$\n\n"
        f"$a+b+c={phan_so(x_H)}+{phan_so(y_H)}+{phan_so(z_H)}={dap_an}$."
                    
        )

    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("+0","")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_31]-SA-M3. Tìm điểm đối xưng của điểm qua mặt phẳng.
def htd_25_xyz_L12_C5_B1_31():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")    

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.randint(-10,11)
    ptmp_P=f"{latex(a*x+b*y+c*z+d)}=0"   

    
    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,H,M=ten_diem[0:3]

    while True:
        x_A,y_A,z_A=random.randint(-6,6),random.randint(-6,6),random.randint(-6,6)
        if a*x_A+b*y_A+c*z_A+d !=0:
            break

    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])
    
    
    noi_dung= (
    f"Trong không gian ${{Oxyz}}$, cho mặt phẳng $({mp_P}):{ptmp_P}$ và điểm ${A}({x_A};{y_A};{z_A})$."
        f" Biết ${M}(a;b;c)$ là điểm đối xứng với điểm ${{{A}}}$ qua mặt phẳng ${{({mp_P})}}$."
        f" Tính ${{a+b+c}}$ (kết quả làm tròn đến hàng phần mười).")

    t=sp.symbols("t")
    eq=Eq(a*(x_A+a*t)+b*(y_A+b*t)+c*(z_A+c*t)+d,0)
    solution=solve(eq,t)

    t=solution[0]
    x_H,y_H,z_H = x_A+a*t, y_A+b*t, z_A+c*t
    x_M,y_M,z_M=2*x_H-x_A, 2*y_H-y_A, 2*z_H-z_A

    dap_an=f"{round_half_up(x_M+y_M+z_M,1):.1f}".replace(".",",")
    noi_dung_loigiai=my_module.thay_dau_congtru(
        f"$(P)$ nhận ${vec("n")}=({a};{b};{c})$ làm một véctơ pháp tuyến.\n\n"
        f"Gọi ${{{H}}}$ là hình chiếu của ${{{A}}}$ lên $({mp_P})$.\n\n"
        f"${vec2(A,H)}=(a-{x_A};b-{y_A};c-{z_A})$ cùng phương với ${vec("n")}$ nên:\n\n"
        f"${vec2(A,H)}=t{vec("n")}\\Rightarrow a={x_A}+{a}t,b={y_A}+{b}t,c={z_A}+{c}t$.\n\n"
        f"${H} \\in ({mp_P}) \\Rightarrow {a}({x_A}+{a}t)+{b}({y_A}+{b}t)+{c}({z_A}+{c}t)+{d}=0$.\n\n"
        f"$\\Rightarrow t={phan_so(t)} \\Rightarrow {H}({phan_so(x_H)};{phan_so(y_H)};{phan_so(z_H)})$\n\n"
        f"$x_{M}=2.{phan_so(x_H)}-{x_A}={phan_so(x_M)}$,"
        f"$y_{M}=2.{phan_so(y_H)}-{y_A}={phan_so(y_M)}$,"
        f"$z_{M}=2.{phan_so(z_H)}-{z_A}={phan_so(z_M)}$."
        f"${M}({phan_so(x_M)};{phan_so(y_M)};{phan_so(z_M)})$.\n\n"
        f"$a+b+c={phan_so(x_M)}+{phan_so(y_M)}+{phan_so(z_M)}={dap_an}$."
                    
        )

    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-").replace("+0","")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_32]-M2. Viết PTMP qua điểm song song với (Oxy), (Oyz), (Oyz).
def htd_25_xyz_L12_C5_B1_32():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")    

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.randint(-10,11)
    ptmp_P=f"{latex(a*x+b*y+c*z+d)}=0"   

    
    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,H,M=ten_diem[0:3]
    while True:
        x_A,y_A,z_A=random.randint(-6,6),random.randint(-6,6),random.randint(-6,6)
        if all([x_A!=0, y_A!=0, z_A!=0, 
                x_A!=y_A, x_A!=z_A, y_A!=z_A]):
            break
    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])
    
    chon=random.randint(1,3)
    
    if chon==1:
        noi_dung= (
        f"Trong không gian ${{Oxyz}}$, mặt phẳng $({mp_P})$ qua điểm ${A}({x_A};{y_A};{z_A})$"
            f" và song song với mặt phẳng $(Oxy)$ có phương trình là"        
            )

        noi_dung_loigiai=(
        f"$({mp_P})$ song song với mặt phẳng $(Oxy)$ nên nhận vectơ ${vec("k")}=(0;0;1)$ là véctơ pháp tuyến.\n\n"
        f"Phương trình $({mp_P})$ là: ${latex(z-z_A)}=0$."
        )
        

        kq=f"${latex(z-z_A)}=0$"
        kq_false=[
        f"${latex(x-x_A)}=0$",
        f"${latex(y-y_A)}=0$",    
        f"${latex(x+y-z_A)}=0$",
        f"${latex(y+z-x_A)}=0$",
        f"${latex(x+z-y_A)}=0$"]
    
    if chon==2:
        noi_dung= (
        f"Trong không gian ${{Oxyz}}$, mặt phẳng $({mp_P})$ qua điểm ${A}({x_A};{y_A};{z_A})$"
            f" và song song với mặt phẳng $(Oyz)$ có phương trình là"        
            )

        noi_dung_loigiai=(
        f"$({mp_P})$ song song với mặt phẳng $(Oyz)$ nên nhận vectơ ${vec("i")}=(1;0;0)$ là véctơ pháp tuyến.\n\n"
        f"Phương trình $({mp_P})$ là: ${latex(x-x_A)}=0$."
        )
        

        kq=f"${latex(x-x_A)}=0$"
        kq_false=[
        f"${latex(z-z_A)}=0$",
        f"${latex(y-y_A)}=0$",    
        f"${latex(x+y-z_A)}=0$",
        f"${latex(y+z-x_A)}=0$",
        f"${latex(x+z-y_A)}=0$"]

    if chon==3:
        noi_dung= (
        f"Trong không gian ${{Oxyz}}$, mặt phẳng $({mp_P})$ qua điểm ${A}({x_A};{y_A};{z_A})$"
            f" và song song với mặt phẳng $(Oxz)$ có phương trình là"        
            )

        noi_dung_loigiai=(
        f"$({mp_P})$ song song với mặt phẳng $(Oxz)$ nên nhận vectơ ${vec("j")}=(0;1;0)$ là véctơ pháp tuyến.\n\n"
        f"Phương trình $({mp_P})$ là: ${latex(y-y_A)}=0$."
        )
        

        kq=f"${latex(y-y_A)}=0$"
        kq_false=[
        f"${latex(x-x_A)}=0$",
        f"${latex(y-y_A)}=0$",    
        f"${latex(x+y-z_A)}=0$",
        f"${latex(y+z-x_A)}=0$",
        f"${latex(x+z-y_A)}=0$"]
    
    
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

#[D12_C5_B1_33]-M2. Viết PTMP qua điểm A và chứa trục Ox (Oy, Oz)
def htd_25_xyz_L12_C5_B1_33():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")    

    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    d = random.randint(-10,11)
    ptmp_P=f"{latex(a*x+b*y+c*z+d)}=0"   

    
    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,H,M=ten_diem[0:3]
    while True:
        x_A,y_A,z_A=random.randint(-6,6),random.randint(-6,6),random.randint(-6,6)
        if all([x_A!=0, y_A!=0, z_A!=0, 
                x_A!=y_A, x_A!=z_A, y_A!=z_A]):
            break
    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])
    
    chon=random.randint(1,3)
    
    if chon==1:    
    
        noi_dung= (
        f"Trong không gian ${{Oxyz}}$, mặt phẳng $({mp_P})$ qua điểm ${A}({x_A};{y_A};{z_A})$"
            f" và chứa trục ${{Ox}}$ có phương trình là")

        a,b,c=tich_co_huong([1,0,0],[x_A,y_A,z_A])   

        t=ucln_ba_so(a,b,c)
        a1,b1,c1=int(a/t),int(b/t),int(c/t)

        noi_dung_loigiai=(
        f"Ta có: ${vec("i")}=(1;0;0), {vec(f"O{A}")}=({x_A};{y_A};{z_A})$. \n\n"
        f"$({mp_P})$ nhận ${vec("n")}=[{vec("i")}, {vec(f"O{A}")}]=({a};{b};{c})$ làm véctơ pháp tuyến.\n\n"
        f"Phương trình $({mp_P})$ là: ${latex(a1*x+b1*y+c1*z-(a1*x_A+b1*y_A+c1*z_A))}=0$."
        )
        

        kq=f"${latex(b1*y+c1*z)}=0$"
        kq_false=[
        f"${latex(random.randint(1,4)*x+b1*y+c1*z)}=0$",
        f"${latex(b1*x+c1*z)}=0$", 
        f"${latex(b1*y+c1*z+random.randint(1,4))}=0$" ]

    if chon==2:    
    
        noi_dung= (
        f"Trong không gian ${{Oxyz}}$, mặt phẳng $({mp_P})$ qua điểm ${A}({x_A};{y_A};{z_A})$"
            f" và chứa trục ${{Oy}}$ có phương trình là")

        a,b,c=tich_co_huong([0,1,0],[x_A,y_A,z_A])   

        t=ucln_ba_so(a,b,c)
        a1,b1,c1=int(a/t),int(b/t),int(c/t)

        noi_dung_loigiai=(
        f"Ta có: ${vec("j")}=(0;1;0), {vec(f"O{A}")}=({x_A};{y_A};{z_A})$. \n\n"
        f"$({mp_P})$ nhận ${vec("n")}=[{vec("j")}, {vec(f"O{A}")}]=({a};{b};{c})$ làm véctơ pháp tuyến.\n\n"
        f"Phương trình $({mp_P})$ là: ${latex(a1*x+b1*y+c1*z-(a1*x_A+b1*y_A+c1*z_A))}=0$."
        )
        

        kq=f"${latex(a1*x+c1*z)}=0$"
        kq_false=[
        f"${latex(random.randint(1,4)*x+random.randint(1,4)*y+random.randint(1,4)*z)}=0$",
        f"${latex(a1*y+c1*z)}=0$", 
        f"${latex(a1*x+c1*z+random.randint(1,4))}=0$"]

    if chon==3:    
    
        noi_dung= (
        f"Trong không gian ${{Oxyz}}$, mặt phẳng $({mp_P})$ qua điểm ${A}({x_A};{y_A};{z_A})$"
            f" và chứa trục ${{Oz}}$ có phương trình là")

        a,b,c=tich_co_huong([0,0,1],[x_A,y_A,z_A])   

        t=ucln_ba_so(a,b,c)
        a1,b1,c1=int(a/t),int(b/t),int(c/t)

        noi_dung_loigiai=(
        f"Ta có: ${vec("k")}=(0;0;1), {vec(f"O{A}")}=({x_A};{y_A};{z_A})$. \n\n"
        f"$({mp_P})$ nhận ${vec("n")}=[{vec("k")}, {vec(f"O{A}")}]=({a};{b};{c})$ làm véctơ pháp tuyến.\n\n"
        f"Phương trình $({mp_P})$ là: ${latex(a1*x+b1*y+c1*z-(a1*x_A+b1*y_A+c1*z_A))}=0$."
        )
        

        kq=f"${latex(a1*x+b1*y)}=0$"
        kq_false=[
        f"${latex(random.randint(1,4)*x+random.randint(1,4)*y+random.randint(1,4)*z)}=0$",
        f"${latex(a1*y+b1*z)}=0$", 
        f"${latex(a1*x+b1*y+random.randint(1,5))}=0$"]
    
    
    
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

import numpy as np

def generate_non_coplanar_points():
    while True:
        # Tạo 4 điểm ngẫu nhiên khác nhau trong không gian Oxyz
        points = set()
        while len(points) < 4:
            points.add(tuple(np.random.randint(-4, 5, size=3)))
        
        A, B, C, D = map(np.array, points)
        
        # Tính các vector AB, AC, AD
        AB = B - A
        AC = C - A
        AD = D - A
        
        # Tính định thức của ma trận chứa các vector này
        det = np.linalg.det(np.array([AB, AC, AD]))
        
        # Nếu định thức khác 0 thì 4 điểm không đồng phẳng
        if abs(det) > 1e-6:
            return A, B, C, D

#[D12_C5_B1_34]-SA-M2. Viết PTMP qua điểm A,B và song song với C,D
def htd_25_xyz_L12_C5_B1_34():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    A,B,C,D=generate_non_coplanar_points()
    x_A,y_A,z_A=A
    x_B,y_B,z_B=B
    x_C,y_C,z_C=C
    x_D,y_D,z_D=D
    
    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,D=ten_diem[0:4]
    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])

    
    x_1,y_1,z_1=x_B-x_A,y_B-y_A,z_B-z_A
    x_2,y_2,z_2=x_D-x_C,y_D-y_C,z_D-z_C
    a,b,c=tich_co_huong([x_1,y_1,z_1],[x_2,y_2,z_2])   

    t=ucln_ba_so(a,b,c)
    a1,b1,c1=int(a/t),int(b/t),int(c/t)
    d1=a1*x_A+b1*y_A+c1*z_A

    noi_dung = (
    f"Trong không gian ${{Oxyz}}$, mặt phẳng $({mp_P})$ qua điểm ${A}({x_A};{y_A};{z_A}),{B}({x_B};{y_B};{z_B})$"
    f" và song song với đường thẳng đi qua hai điểm ${C}({x_C};{y_C};{z_C}),{B}({x_D};{y_D};{z_D})$"
    f" có phương trình dạng ${a1}x+ay+bz+c=0$. Tính $a+b+c$."
    )
    dap_an=b1+c1-d1
    

    noi_dung_loigiai=(
    f"${vec2(A,B)}=({x_1};{y_1};{z_1}),{vec2(C,D)}=({x_2};{y_2};{z_2})$.\n\n"
    f" $({mp_P})$ nhận ${vec("n")}=[{vec2(A,B)},{vec2(C,D)}]=({a};{b};{c})$ làm véctơ pháp tuyến.\n\n"
    f"Phương trình $({mp_P}):{latex(a1*x+b1*y+c1*z-d1)}=0$."
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B1_35]-SA-M2. Tính khoảng cách từ một điểm đến mặt phẳng đoạn chắn
def htd_25_xyz_L12_C5_B1_35():
    x,y,z=sp.symbols("x y z")
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0])
    t=lcm_of_three(a,b,c)
    a1,b1,c1=int(t/a), int(t/b), int(t/c)

    ten_diem=["A","B","C","D","E", "F","M", "N", "G","H","I","K"]
    random.shuffle(ten_diem)
    A,B,C,M=ten_diem[0:4]

    x_M = random.choice([i for i in range(-5, 6) if i!=0])
    y_M = random.choice([i for i in range(-5, 6) if i!=0])
    z_M = random.choice([i for i in range(-5, 6) if i!=0])

    mp_P=random.choice(["P","Q", "R", "\\alpha","\\beta", "\\gamma"])   

    noi_dung= (
    f"Trong không gian ${{Oxyz}}$, cho các điểm ${A}({a};0;0),{B}(0;{b};0), {C}(0;0;{c})$."        
        f" Tính khoảng cách từ điểm ${{{M}}}({x_M};{y_M};{z_M})$ đến mặt phẳng ${{({A}{B}{C})}}$(kết quả làm tròn đến hàng phần mười).")

    khoang_cach=abs(a1*x_M+b1*y_M+c1*z_M-t)/sqrt(a1**2+b1**2+c1**2)

    dap_an=f"{round_half_up(khoang_cach,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Mặt phẳng ${{({A}{B}{C})}}$ có phương trình:\n\n"
    f" $\\dfrac{{x}}{{{a}}}+\\dfrac{{y}}{{{b}}}+\\dfrac{{z}}{{{c}}}=1$\n\n"
    f"$\\Leftrightarrow {latex(a1*x+b1*y+c1*z-t)}=0$.\n\n"
    f"$d({M},({A}{B}{C}))=\\dfrac{{|{show_tich(a1,x_M)}+{show_tich(b1,y_M)}+{show_tich(c1,z_M)}-{t}|}}{{\\sqrt{{{a1**2}+{b1**2}+{c1**2}}} }}={latex(khoang_cach)}={dap_an}$."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an


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

#[D12_C5_B3_09]-TF-M3. Cho PTMC. Xét Đ-S: Tâm, bán kính, vị trí của điểm, mặt phẳng tiếp xúc mặt cầu
def htd_25_xyz_L12_C5_B3_09():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    while True:
        a,b,c = [random.randint(-5,6) for i in range(3)]
        x_0,y_0,z_0=[random.randint(-5,6) for i in range(3)]
        if all([a!=x_0,b!=y_0, x_0!=0, y_0!=0,z_0!=0]):
            break
    r=sqrt((a-x_0)**2+(b-y_0)**2+(c-z_0)**2)
    chon=random.randint(1,2)
    
    if chon==1:
        ptmc=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}+{latex((z-z_0)**2)}={r**2}"
    
    if chon==2:
        ptmc=f"x^2+y^2+z^2+{-2*x_0}x+{-2*y_0}y+{-2*z_0}z+{x_0**2+y_0**2+z_0**2-r**2}=0"
        ptmc=ptmc.replace("+-","-")
    
    
          

    noi_dung= (f"Trong hệ trục ${{Oxyz}}$, cho mặt cầu ${{(S)}}$ có phương trình"
                f" ${ptmc}$. Xét tính đúng-sai của các khẳng định sau:")
    
    kq1_T=f"* Tâm của mặt cầu ${{(S)}}$ là điểm $I({x_0};{y_0};{z_0})$" 
    kq1_F=f"Tâm của mặt cầu ${{(S)}}$ là điểm $I({-x_0};{-y_0};{-z_0})$"
    
    HDG=f"Tâm của mặt cầu ${{(S)}}$ là điểm $I({x_0};{y_0};{z_0})$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Bán kính của mặt cầu ${{(S)}}$ là $R={latex(r)}$"
    kq2_F=f"Bán kính của mặt cầu ${{(S)}}$ là $R={latex(r**2)}$"
    
    HDG=f"Bán kính của mặt cầu ${{(S)}}$ là $R=\\sqrt{{{r**2}}}={latex(r)}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    
    ten=["A","B","H","M","N","E","F","D"]
    A,B=random.sample(ten,2)
   
    chon=random.randint(1,2)    
    if chon==1:
        while True:        
            x_1,y_1,z_1=[random.randint(-7,7) for i in range(3)]
            r_1=sqrt((x_1-x_0)**2+(y_1-y_0)**2+(z_1-z_0)**2)
            if all([x_1!=x_0,y_1!=y_0, x_1!=a, y_1!=b, r_1>r]):
                break
        kq3_T=f"* Điểm ${A}({x_1};{y_1};{z_1})$ nằm ngoài mặt cầu ${{(S)}}$" 
        kq3_F=f"Điểm ${A}({x_1};{y_1};{z_1})$ nằm trong mặt cầu ${{(S)}}$"
        
        HDG=(f"$I{A}=\\sqrt{{{(x_1-x_0)**2}+{(y_1-y_0)**2}+{(z_1-z_0)**2}}}={latex(r_1)}>{latex(r)}$.\n\n"
        f"Suy ra điểm ${A}({x_1};{y_1};{z_1})$ nằm ngoài mặt cầu ${{(S)}}$.")
        kq3=random.choice([kq3_T, kq3_F])
    
    if chon==2:
        while True:        
            x_1,y_1,z_1=[random.randint(-7,7) for i in range(3)]
            r_1=sqrt((x_1-x_0)**2+(y_1-y_0)**2+(z_1-z_0)**2)
            if all([x_1!=x_0,y_1!=y_0, x_1!=a, y_1!=b, r_1<r]):
                break
        kq3_T=f"* Điểm ${A}({x_1};{y_1};{z_1})$ nằm trong mặt cầu ${{(S)}}$" 
        kq3_F=f"Điểm ${A}({x_1};{y_1};{z_1})$ nằm ngoài mặt cầu ${{(S)}}$"
        
        HDG=(f"$I{A}=\\sqrt{{{(x_1-x_0)**2}+{(y_1-y_0)**2}+{(z_1-z_0)**2}}}={latex(r_1)}<{latex(r)}$.\n\n"
        f"Suy ra điểm ${A}({x_1};{y_1};{z_1})$ nằm trong mặt cầu ${{(S)}}$.")
        kq3=random.choice([kq3_T, kq3_F])
    
    
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    n1,n2,n3=a-x_0,b-y_0,c-z_0
    t=ucln_ba_so(n1,n2,n3)
    n1,n2,n3=int(n1/t), int(n2/t), int(n3/t)
    ptmp=f"{latex(n1*(x-a)+n2*(y-b)+n3*(z-c))}=0"
    ptmp_false=f"{latex(n1*(x-a)+n2*(y-b)+n3*(z-c)+random.randint(1,2))}=0"

    kq4_T=f"* Mặt phẳng $(P)$ tiếp xúc với mặt cầu ${{(S)}}$ tại điểm ${B}({a};{b};{c})$ có phương trình là ${ptmp}$"
    kq4_F=f"Mặt phẳng $(P)$ tiếp xúc với mặt cầu ${{(S)}}$ tại điểm ${B}({a};{b};{c})$ có phương trình là ${ptmp}$" 
    
    HDG=(f"Mặt phẳng $(P)$ qua điểm ${B}({a};{b};{c})$, nhận vectơ ${vec2("I",B)}=({a-x_0};{b-y_0};{c-z_0})$ làm một véctơ pháp tuyến.\n\n"
        f"Phương trình $(P):{n1}({latex(x-a)})+{n2}({latex(y-b)})+{n3}({latex(z-c)})=0\\Leftrightarrow {ptmp}$."
        )
    HDG=HDG.replace("+-","-")
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

#[D12_C5_B3_10]-TF-M3. Cho PTMC. Xét Đ-S: tâm, bán kính, vị trí của điểm, mặt phẳng cắt mặt cầu
def htd_25_xyz_L12_C5_B3_10():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    while True:
        a,b,c = [random.randint(-5,6) for i in range(3)]
        x_0,y_0,z_0=[random.randint(-5,6) for i in range(3)]
        if all([a!=x_0,b!=y_0, x_0!=0, y_0!=0]):
            break
    r=sqrt((a-x_0)**2+(b-y_0)**2+(c-z_0)**2)
    chon=random.randint(1,2)
    
    if chon==1:
        ptmc=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}+{latex((z-z_0)**2)}={r**2}"
    
    if chon==2:
        ptmc=f"x^2+y^2+z^2+{-2*x_0}x+{-2*y_0}y+{-2*z_0}z+{x_0**2+y_0**2+z_0**2-r**2}=0"
        ptmc=ptmc.replace("+-","-")
          

    noi_dung= (f"Trong hệ trục ${{Oxyz}}$, cho mặt cầu ${{(S)}}$ có phương trình"
                f" ${ptmc}$. Xét tính đúng-sai của các khẳng định sau:")
    
    kq1_T=f"* Tâm của mặt cầu ${{(S)}}$ là điểm $I({x_0};{y_0};{z_0})$" 
    kq1_F=f"Tâm của mặt cầu ${{(S)}}$ là điểm $I({-x_0};{-y_0};{-z_0})$"
    
    HDG=f"Tâm của mặt cầu ${{(S)}}$ là điểm $I({x_0};{y_0};{z_0})$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Bán kính của mặt cầu ${{(S)}}$ là $R={latex(r)}$"
    kq2_F=f"Bán kính của mặt cầu ${{(S)}}$ là $R={latex(r**2)}$"
    
    HDG=f"Bán kính của mặt cầu ${{(S)}}$ là $R=\\sqrt{{{r**2}}}={latex(r)}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    
    ten=["A","B","H","M","N","E","F","D"]
    A,B=random.sample(ten,2)
   
    chon=random.randint(1,2)    
    if chon==1:
        while True:        
            x_1,y_1,z_1=[random.randint(-7,7) for i in range(3)]
            r_1=sqrt((x_1-x_0)**2+(y_1-y_0)**2+(z_1-z_0)**2)
            if all([x_1!=x_0,y_1!=y_0, x_1!=a, y_1!=b, r_1>r]):
                break
        kq3_T=f"* Điểm ${A}({x_1};{y_1};{z_1})$ nằm ngoài mặt cầu ${{(S)}}$" 
        kq3_F=f"Điểm ${A}({x_1};{y_1};{z_1})$ nằm trong mặt cầu ${{(S)}}$"
        
        HDG=(f"$I{A}=\\sqrt{{{(x_1-x_0)**2}+{(y_1-y_0)**2}+{(z_1-z_0)**2}}}={latex(r_1)}>{latex(r)}$.\n\n"
        f"Suy ra điểm ${A}({x_1};{y_1};{z_1})$ nằm ngoài mặt cầu ${{(S)}}$.")
        kq3=random.choice([kq3_T, kq3_F])
    
    if chon==2:
        while True:        
            x_1,y_1,z_1=[random.randint(-7,7) for i in range(3)]
            r_1=sqrt((x_1-x_0)**2+(y_1-y_0)**2+(z_1-z_0)**2)
            if all([x_1!=x_0,y_1!=y_0, x_1!=a, y_1!=b, r_1<r]):
                break
        kq3_T=f"* Điểm ${A}({x_1};{y_1};{z_1})$ nằm trong mặt cầu ${{(S)}}$" 
        kq3_F=f"Điểm ${A}({x_1};{y_1};{z_1})$ nằm ngoài mặt cầu ${{(S)}}$"
        
        HDG=(f"$I{A}=\\sqrt{{{(x_1-x_0)**2}+{(y_1-y_0)**2}+{(z_1-z_0)**2}}}={latex(r_1)}<{latex(r)}$.\n\n"
        f"Suy ra điểm ${A}({x_1};{y_1};{z_1})$ nằm trong mặt cầu ${{(S)}}$.")
        kq3=random.choice([kq3_T, kq3_F])
    
    
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    n1,n2,n3=a-x_0,b-y_0,c-z_0
    t=ucln_ba_so(n1,n2,n3)
    n1,n2,n3=int(n1/t), int(n2/t), int(n3/t)
    ptmp=f"{latex(n1*(x-a)+n2*(y-b)+n3*(z-c))}=0"
    ptmp_false=f"{latex(n1*(x-a)+n2*(y-b)+n3*(z-c)+random.randint(1,2))}=0"

    while True:
        n1=random.randint(-4,5)
        n2,n3=[random.randint(-4,5) for i in range(2)]
        n4=random.randint(-4,5)
        t=ucln_ba_so(n1,n2,n3)
        n1,n2,n3=int(n1/t), int(n2/t), int(n3/t)
        d=abs(n1*x_0+n2*y_0+n3*z_0+n4)/sqrt(n1**2+n2**2+n3**2)
        if d<r:
            break 
    d=abs(n1*x_0+n2*y_0+n3*z_0+n4)/sqrt(n1**2+n2**2+n3**2)    
    
    ptmp=f"{latex(n1*x+n2*y+n3*z+n4)}=0"
    r_3=sqrt(r**2-d**2)
    r_3_false=sqrt(r**2+d**2)

    kq4_T=f"* Mặt phẳng $(P):{ptmp}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có bán kính bằng ${{{latex(r_3)}}}$"
    kq4_F=f"Mặt phẳng $(P):{ptmp}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có bán kính bằng ${{{latex(r_3_false)}}}$" 
    
    HDG=(f"${{(S)}}$ có tâm $I({x_0};{y_0};{z_0})$ và bán kính $R={latex(r)}$.\n\n"
        f"Khoảng cách từ tâm ${{I}}$ đến mặt phẳng $(P)$:\n\n"
        f"$d(I,(P))=\\dfrac{{|{show_tich(n1,x_0)}+{show_tich(n2,y_0)}+{show_tich(n3,z_0)}+{n4}|}}{{\\sqrt{{{n1**2}+{n2**2}+{n3**2}}}}}={latex(d)}<{latex(r)}$\n\n"
        f"Mặt phẳng $(P):{ptmp}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có bán kính bằng:\n\n"
        f"$r=\\sqrt{{R^2-d^2}}=\\sqrt{{{latex(r**2)}-{latex(d**2)}}}={latex(r_3)}$."
       
        )
    HDG=HDG.replace("+-","-")
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

#[D12_C5_B3_11]-TF-M3. Cho PTMC và PTMP. Xét Đ-S: tâm, bán kính, vị trí của điểm, mặt phẳng cắt mặt cầu
def htd_25_xyz_L12_C5_B3_11():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    while True:        
        x_0,y_0,z_0=[random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(3)]
        a,b,c,d=[random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(4)]
        R=random.choice([sqrt(i) for i in range(145)])
        d_IP=abs(a*x_0+b*y_0+c*z_0+c+d)/(sqrt(a**2+b**2+c**2))
        d_IP_false=abs(a*x_0+b*y_0+c*z_0+c+d+random.randint(1,2))/(sqrt(a**2+b**2+c**2))
        if all([d_IP<R]):
            break
    d_IP=abs(a*x_0+b*y_0+c*z_0+c+d)/(sqrt(a**2+b**2+c**2))
    d_IP_false=abs(a*x_0+b*y_0+c*z_0+c+d+random.randint(1,2))/(sqrt(a**2+b**2+c**2))
    ptmp=f"{latex(a*x+b*y+c*z+d)}=0"
    
    chon=random.randint(1,2)
    
    if chon==1:
        ptmc=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}+{latex((z-z_0)**2)}={R**2}"
    
    if chon==2:
        ptmc=f"x^2+y^2+z^2+{-2*x_0}x+{-2*y_0}y+{-2*z_0}z+{x_0**2+y_0**2+z_0**2-R**2}=0"
        ptmc=ptmc.replace("+-","-")
          

    noi_dung= (f"Trong hệ trục ${{Oxyz}}$, cho mặt cầu ${{(S)}}:{ptmc}$"
                f" và mặt phẳng $(P):{ptmp}$. Xét tính đúng-sai của các khẳng định sau:")
    
    kq1_T=f"* Mặt cầu ${{(S)}}$ có tâm $I({x_0};{y_0};{z_0})$ và bán kính $R={latex(R)}$" 
    kq1_F=f"Mặt cầu ${{(S)}}$ có tâm $I({-x_0};{-y_0};{-z_0})$ và bán kính $R={latex(R)}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Mặt cầu ${{(S)}}$ có tâm $I({x_0};{y_0};{z_0})$ và bán kính $R={latex(R)}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* Khoảng cách từ tâm ${{I}}$ đến mặt phẳng $(P)$ bằng ${latex(d_IP)}$"
    kq2_F=f"Khoảng cách từ tâm ${{I}}$ đến mặt phẳng $(P)$ bằng ${latex(d_IP_false)}$"
    kq2=random.choice([kq2_T, kq2_F])
    HDG=(f"Khoảng cách từ tâm ${{I}}$ đến mặt phẳng $(P)$ bằng:\n\n"
    f"$d(I,(P))=\\dfrac{{|{show_tich(a,x_0)}+{show_tich(b,y_0)}+{show_tich(c,z_0)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={latex(d_IP)}$.")
    HDG=HDG.replace("+-","-")
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    r=sqrt(R**2-d_IP**2)
    r_false=sqrt(R**2+d_IP**2)

    kq3_T=f"* Mặt phẳng ${{(P)}}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có bán kính bằng ${latex(r)}$" 
    kq3_F=f"Mặt phẳng ${{(P)}}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có bán kính bằng ${latex(r_false)}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=(f"$d(I,(P))=\\dfrac{{|{show_tich(a,x_0)}+{show_tich(b,y_0)}+{show_tich(c,z_0)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={latex(d_IP)}<{latex(R)}$.\n\n"
        f"Mặt phẳng ${{(P)}}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có bán kính:\n\n"
        f"$r=\\sqrt{{R^2-d^2(I,(P))}}=\\sqrt{{{R**2}-{latex(d_IP**2)}}}={latex(r)}$."
        )
    HDG=HDG.replace("+-","-")
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    eq=Eq(a*(x_0+a*t)+b*(y_0+b*t)+c*(z_0+c*t),0)
    solution=solve(eq,t)
    t_0=solution[0]
    x_H,y_H,z_H=phan_so(x_0+a*t_0),phan_so(y_0+b*t_0),phan_so(z_0+c*t_0)
    x_H_f,y_H_f,z_H_f=phan_so(x_0+a*t_0),phan_so(y_0+b*t_0+random.randint(1,2)),phan_so(z_0+c*t_0+random.randint(-1,2))

    kq4_T=f"* Mặt phẳng ${{(P)}}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có tâm là điểm $H\\left({x_H};{y_H};{z_H}\\right)$"
    kq4_F=f"Mặt phẳng ${{(P)}}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có tâm là điểm $H\\left({x_H_f};{y_H_f};{z_H_f}\\right)$" 
    kq4=random.choice([kq4_T, kq4_F])
    
    HDG=(f"Đường thẳng ${{IH}}$ qua $I({x_0};{y_0};{z_0})$ và nhận vectơ ${vec("n_P")}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        x={x_0}+{a}t \\\\ \n\
        y={y_0}+{b}t \\\\ \n\
        z={z_0}+{c}t\n\
        \\end{{array}} \\right.$\n\n"
        f"Gọi $H({latex(x_0+a*t)};{latex(y_0+b*t)};{latex(z_0+c*t)})$.\n\n"
        f"Thay tọa độ ${{H}}$ vào phương trình mặt phẳng $(P)$ ta được:\n\n"
        f"${a}({latex(x_0+a*t)})+{b}({latex(y_0+b*t)})+{c}({latex(z_0+c*t)})=0$"
        f"$\\Leftrightarrow t={phan_so(t_0)}$.\n\n"
        f"$\\Rightarrow H\\left({x_H};{y_H};{z_H}\\right)$"
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

#[D12_C5_B3_12]-SA-M3. Cho mặt cầu có tâm I và cắt trục Ox(Oy,Oz). Tính bán kính.
def htd_25_xyz_L12_C5_B3_12():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    
    x_0,y_0,z_0=[random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(3)]    
    
    ten_diem=["A","B","C","D","I","E","F"]
    I,B,C=random.sample(ten_diem,3)
    BC=random.randint(1,8)
    chon=random.randint(1,3)    

    if chon==1:
        IH=sqrt(y_0**2+z_0**2)
        R=sqrt(IH**2+BC**2/4)    
        dap_an=f"{round_half_up(R,1):.1f}".replace(".",",")

        noi_dung = (
        f"Trong hệ trục ${{Oxyz}}$, mặt cầu ${{(S)}}$ có tâm ${I}({x_0};{y_0};{z_0})$ và"
        f" cắt trục ${{Ox}}$ tại các điểm ${{{B},{C}}}$ sao cho ${B}{C}={BC}$ có bán kính bằng bao nhiêu(kết quả làm tròn đến hàng phần mười)?"
        )
        noi_dung_loigiai=(
        f"Hình chiếu vuông góc của điểm ${{{I}}}$ lên trục ${{Ox}}$ là $H({x_0};0;0)$.\n\n"
        f"Bán kính mặt cầu là: $R=\\sqrt{{{I}H^2+\\dfrac{{{B}{C}^2}}{{4}}}}=\\sqrt{{{IH**2}+{phan_so(BC**2/4)}}}={latex(nsimplify(R))}={dap_an}$."
        ) 
    
    if chon==2:
        IH=sqrt(x_0**2+z_0**2)
        R=sqrt(IH**2+BC**2/4)    
        dap_an=f"{round_half_up(R,1):.1f}".replace(".",",")

        noi_dung = (
        f"Trong hệ trục ${{Oxyz}}$, mặt cầu ${{(S)}}$ có tâm ${I}({x_0};{y_0};{z_0})$ và"
        f" cắt trục ${{Oy}}$ tại các điểm ${{{B},{C}}}$ sao cho ${B}{C}={BC}$ có bán kính bằng bao nhiêu(kết quả làm tròn đến hàng phần mười)?"
        )
        noi_dung_loigiai=(
        f"Hình chiếu vuông góc của điểm ${{{I}}}$ lên trục ${{Oy}}$ là $H(0;{y_0};0)$.\n\n"
        f"Bán kính mặt cầu là: $R=\\sqrt{{{I}H^2+\\dfrac{{{B}{C}^2}}{{4}}}}=\\sqrt{{{IH**2}+{phan_so(BC**2/4)}}}={latex(nsimplify(R))}={dap_an}$."
        )

    if chon==3:
        IH=sqrt(x_0**2+y_0**2)
        R=sqrt(IH**2+BC**2/4)    
        dap_an=f"{round_half_up(R,1):.1f}".replace(".",",")

        noi_dung = (
        f"Trong hệ trục ${{Oxyz}}$, mặt cầu ${{(S)}}$ có tâm ${I}({x_0};{y_0};{z_0})$ và"
        f" cắt trục ${{Oz}}$ tại các điểm ${{{B},{C}}}$ sao cho ${B}{C}={BC}$ có bán kính bằng bao nhiêu(kết quả làm tròn đến hàng phần mười)?"
        )
        noi_dung_loigiai=(
        f"Hình chiếu vuông góc của điểm ${{{I}}}$ lên trục ${{Oz}}$ là $H(0;0;{z_0})$.\n\n"
        f"Bán kính mặt cầu là: $R=\\sqrt{{{I}H^2+\\dfrac{{{B}{C}^2}}{{4}}}}=\\sqrt{{{IH**2}+{phan_so(BC**2/4)}}}={latex(nsimplify(R))}={dap_an}$."
        )  
    
       
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B3_13]-SA-M3. Cho mặt cầu cắt mặt phẳng. Tìm bán kính đường tròn giao tuyến
def htd_25_xyz_L12_C5_B3_13():

    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    while True:        
        x_0,y_0,z_0=[random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(3)]
        a,b,c,d=[random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(4)]
        R=random.choice([sqrt(i) for i in range(145)])
        d_IP=abs(a*x_0+b*y_0+c*z_0+c+d)/(sqrt(a**2+b**2+c**2))
        d_IP_false=abs(a*x_0+b*y_0+c*z_0+c+d+random.randint(1,2))/(sqrt(a**2+b**2+c**2))
        if all([d_IP<R]):
            break
    d_IP=abs(a*x_0+b*y_0+c*z_0+c+d)/(sqrt(a**2+b**2+c**2))
    ptmp=f"{latex(a*x+b*y+c*z+d)}=0"
    r=sqrt(R**2-d_IP**2)
    
    chon=random.randint(1,2)
    
    if chon==1:
        ptmc=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}+{latex((z-z_0)**2)}={R**2}"
    
    if chon==2:
        ptmc=f"x^2+y^2+z^2+{-2*x_0}x+{-2*y_0}y+{-2*z_0}z+{x_0**2+y_0**2+z_0**2-R**2}=0"
        ptmc=ptmc.replace("+-","-")
          

    noi_dung= (f"Trong hệ trục ${{Oxyz}}$, cho mặt cầu ${{(S)}}:{ptmc}$"
                f" và mặt phẳng $(P):{ptmp}$. Mặt cầu ${{(S)}}$ cắt mặt phẳng $(P):{ptmp}$ theo một đường tròn có bán kính bằng bao nhiêu? (kết quả làm tròn đến hàng phần mười)")
    dap_an=f"{round_half_up(r,1):.1f}".replace(".",",")

    noi_dung_loigiai=(f"$d(I,(P))=\\dfrac{{|{show_tich(a,x_0)}+{show_tich(b,y_0)}+{show_tich(c,z_0)}+{d}|}}{{\\sqrt{{{a**2}+{b**2}+{c**2}}}}}={latex(d_IP)}<{latex(R)}$.\n\n"
        f"Mặt phẳng ${{(P)}}$ cắt mặt cầu ${{(S)}}$ theo một đường tròn có bán kính:\n\n"
        f"$r=\\sqrt{{R^2-d^2(I,(P))}}=\\sqrt{{{R**2}-{latex(d_IP**2)}}}={latex(r)}={dap_an}$.")    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B3_14]-SA-M3. Cho mặt cầu cắt mặt phẳng. Tìm tọa độ tâm đường tròn giao tuyến
def htd_25_xyz_L12_C5_B3_14():

    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    while True:        
        x_0,y_0,z_0=[random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(3)]
        a,b,c,d=[random.choice([random.randint(-5,-1),random.randint(1,5)]) for i in range(4)]
        R=random.choice([sqrt(i) for i in range(145)])
        d_IP=abs(a*x_0+b*y_0+c*z_0+c+d)/(sqrt(a**2+b**2+c**2))
        d_IP_false=abs(a*x_0+b*y_0+c*z_0+c+d+random.randint(1,2))/(sqrt(a**2+b**2+c**2))
        if all([d_IP<R]):
            break    
    ptmp=f"{latex(a*x+b*y+c*z+d)}=0"    
    eq=Eq(a*(x_0+a*t)+b*(y_0+b*t)+c*(z_0+c*t),0)
    solution=solve(eq,t)
    t_0=solution[0]
    x_H,y_H,z_H=x_0+a*t_0, y_0+b*t_0, z_0+c*t_0
    
    chon=random.randint(1,2)
    
    if chon==1:
        ptmc=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}+{latex((z-z_0)**2)}={R**2}"
    
    if chon==2:
        ptmc=f"x^2+y^2+z^2+{-2*x_0}x+{-2*y_0}y+{-2*z_0}z+{x_0**2+y_0**2+z_0**2-R**2}=0"
        ptmc=ptmc.replace("+-","-")
          

    noi_dung= (f"Trong hệ trục ${{Oxyz}}$, cho mặt cầu ${{(S)}}:{ptmc}$"
                f" và mặt phẳng $(P):{ptmp}$. Mặt cầu ${{(S)}}$ cắt mặt phẳng $(P):{ptmp}$ theo một đường tròn có tâm $H(a;b;c)$."
    f" Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười).")
    dap_an=f"{round_half_up(x_H+y_H+z_H,1):.1f}".replace(".",",")
    x_H,y_H,z_H=phan_so(x_0+a*t_0),phan_so(y_0+b*t_0),phan_so(z_0+c*t_0)
    
    noi_dung_loigiai=(f"Đường thẳng ${{IH}}$ qua $I({x_0};{y_0};{z_0})$ và nhận vectơ ${vec("n_P")}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        x={x_0}+{a}t \\\\ \n\
        y={y_0}+{b}t \\\\ \n\
        z={z_0}+{c}t\n\
        \\end{{array}} \\right.$\n\n"
        f"Gọi $H({latex(x_0+a*t)};{latex(y_0+b*t)};{latex(z_0+c*t)})$.\n\n"
        f"Thay tọa độ ${{H}}$ vào phương trình mặt phẳng $(P)$ ta được:\n\n"
        f"${a}({latex(x_0+a*t)})+{b}({latex(y_0+b*t)})+{c}({latex(z_0+c*t)})=0$"
        f"$\\Leftrightarrow t={phan_so(t_0)}$.\n\n"
        f"$\\Rightarrow H\\left({x_H};{y_H};{z_H}\\right)$.\n\n"
        f"$\\Rightarrow a+b+c={dap_an}$."
        )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B3_15]-SA-M3. Tìm bán kính mặt cầu ngoại tiếp OABC với A,B,C thuộc 3 trục tọa độ
def htd_25_xyz_L12_C5_B3_15():
    a= random.choice([i for i in range(-5, 6) if i!=0])
    b= random.choice([i for i in range(-5, 6) if i!=0])
    c= random.choice([i for i in range(-5, 6) if i!=0])
    ten_diem=["A","B", "C", "D", "E", "F"]
    A,B,C=random.sample(ten_diem,3)

    noi_dung = (
    f"Trong hệ trục ${{Oxyz}}$, cho ba điểm ${A}({a};0;0), {B}(0;{b};0), {C}(0;0;{c})$."
    f" Tính bán kính mặt cầu ngoại tiếp tứ diện ${{O{A}{B}{C}}}$ (kết quả làm tròn đến hàng phần mười)."
    )
    dap_an=f"{round_half_up(sqrt(a**2/4+b**2/4+c**2/4),1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Gọi ${{S}}$ là mặt cầu ngoại tiếp tứ diện ${{O{A}{B}{C}}}$.\n\n"
    f"Phương trình mặt cầu ${{S}}$ có dạng: $x^2+y^2+z^2+ax+by+cz+d=0$.\n\n"
    f"Vì ${{O,{A},{B},{C}}}$ thuộc ${{S}}$ nên ta có:\n\n"
    f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    d={0} \\\\ \n\
    {a**2}+{a}a+d=0 \\\\ \n\
    {b**2}+{b}b+d=0 \\\\ \n\
    {c**2}+{c}c+d=0 \n\
        \\end{{array}} \\right.$"
    f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
    a={-a} \\\\ \n\
    b={-b} \\\\ \n\
    c={-c}\n\
    \\end{{array}} \\right.$\n\n"
    
    f"Bán kính mặt cầu ${{S}}$ là $R=\\sqrt{{{phan_so(a**2/4)}+{phan_so(b**2/4)}+{phan_so(c**2/4)}}}={latex(nsimplify(sqrt((a**2+b**2+c**2)/4)))}={dap_an}$.") 
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B3_16]-M2. Tìm điểm thuộc mặt cầu.
def htd_25_xyz_L12_C5_B3_16():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    while True:
        a,b,c = [random.randint(-5,6) for i in range(3)]
        x_0,y_0,z_0=[random.randint(-5,6) for i in range(3)]
        if all([a!=x_0,b!=y_0, x_0!=0, y_0!=0]):
            break
    r=sqrt((a-x_0)**2+(b-y_0)**2+(c-z_0)**2)
    chon=random.randint(1,2)
    
    if chon==1:
        ptmc=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}+{latex((z-z_0)**2)}={r**2}"
    
    if chon==2:
        ptmc=f"x^2+y^2+z^2+{-2*x_0}x+{-2*y_0}y+{-2*z_0}z+{x_0**2+y_0**2+z_0**2-r**2}=0"
        ptmc=ptmc.replace("+-","-")
          

    noi_dung= (f"Trong hệ trục ${{Oxyz}}$, cho mặt cầu ${{(S)}}$ có phương trình"
                f" ${ptmc}$. Mặt cầu ${{(S)}}$ đi qua điểm có tọa độ nào sau đây?")
    while True:
        x_1,y_1,z_1=[random.randint(-5,6) for i in range(3)]
        x_2,y_2,z_2=[random.randint(-5,6) for i in range(3)]
        x_3,y_3,z_3=[random.randint(-5,6) for i in range(3)]
        r1=sqrt((x_1-x_0)**2+(y_1-y_0)**2+(z_1-z_0)**2)
        r2=sqrt((x_2-x_0)**2+(y_2-y_0)**2+(z_2-z_0)**2)
        r3=sqrt((x_3-x_0)**2+(y_3-y_0)**2+(z_3-z_0)**2)
        
        if all([r1!=r, r2!=r, r3!=r, x_1!=x_2, x_2!=x_3, x_1!=x_3]):
            break      


    kq=f"$({a};{b};{c})$"
    kq_false=[f"$({x_1};{y_1};{z_1})$",
    f"$({x_2};{y_2};{z_2})$",
    f"$({x_3};{y_3};{z_3})$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"Thay tọa độ các điểm vào phương trình mặt cầu ${{(S)}}$ ta được điểm $({a};{b};{c})$ thỏa mãn."
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

#[D12_C5_B3_17]-SA-M3. Tìm m để bán kính mặt cầu là nhỏ nhất
def htd_25_xyz_L12_C5_B3_17():

    m=symbols("m")
    a=random.choice([i for i in range(-5,6) if i!=0])
    b=random.choice([i for i in range(-4,6) if i!=0])
    a1=random.choice([i for i in range(-5,6) if i!=0 and i!=a])
    b1=random.choice([i for i in range(-4,6) if i!=0])
    a2=random.choice([i for i in range(-3,4) if i!=0])
    c=random.randint(1,10)
    expr = (a*m + b)**2 + (a1*m + b1)**2 + a2**2*m**2 + c
    # Tính đạo hàm theo m
    expr_diff = diff(expr, m)

    # Tìm nghiệm của phương trình đạo hàm bằng 0
    critical_points = solve(expr_diff, m)
    m_min=critical_points[0]

    # Kiểm tra giá trị nhỏ nhất
    min_value = expr.subs(m,m_min)
    
    noi_dung=f"Trong hệ trục ${{Oxyz}}$, cho mặt cầu $(C_{{m}}): x^{{2}}+y^{{2}}+z^2+({latex(2*(a*m+b))})x+({latex(2*(a1*m+b1))})y+{2*a2}mz-{c}=0$ với ${{m}}$ là tham số. Mặt cầu có bán kính nhỏ nhất bằng ${{a}}$. Tính ${{a^{{2}}}}$. (kết quả làm tròn đến hàng phần mười)."
    noi_dung_loigiai=(
        f"$R^{{2}}= ({latex((a1*m+b1))})^{{2}}+({latex((a*m+b))})^{{2}}+{a2**2}m^2+{c}$ \n\n"
        f"$={latex(expand((a*m+b)**2+(a1*m+b1)**2+a2**2*m**2+c))}$.\n\n"
    f" ${{R^2}}$ đạt giá trị nhỏ nhất khi $m={phan_so(m_min)}$ \n\n"
    f" Vậy min $R^{{2}}= {phan_so(min_value)}$.")
    dap_an=f"{round_half_up(min_value,1):.1f}".replace(".",",")


    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an


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

#[D12_C5_B2_27]-SA-M2. Tìm giao điểm của đường thẳng và mặt phẳng
def htd_25_xyz_L12_C5_B2_27():
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
    
    dap_an=x_0+y_0+z_0

    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, tọa độ giao điểm của đường thẳng ${{{ten_dt}}}:\\dfrac{{{latex(x-x_1)}}}{{{a}}}=\\dfrac{{{latex(y-y_1)}}}{{{b}}}=\\dfrac{{{latex(z-z_1)}}}{{{c}}}$"\
                f" và mặt phẳng ${ten_mp}:{mp}=0$ là điểm $H(a;b;c)$. Tính $P=a+b+c$.")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ có phương trình tham số là ${ptts}$.\n\n"\
        f"Xét phương trình ${n1}({latex((x_1+a*t))})+{n2}({latex((y_1+b*t))})+{n3}({latex((z_1+c*t))})+{d}=0\\Rightarrow t={-t1}$.\n\n"\
        f"Tọa độ giao điểm của ${{{ten_dt}}}$ và ${{{ten_mp}}}$ là $H({x_0};{y_0};{z_0})$.\n\n Vậy $P={x_0}+{y_0}+{z_0}={dap_an}$.")      
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B2_28]-SA-M2. Bài toán đường thẳng cắt và vuông góc với đường thẳng khác
def htd_25_xyz_L12_C5_B2_28():

    x,y,z,t=sp.symbols("x y z t")
    while True:
        a = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        b = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        if all([a!=0, b!=0, c!=0, a!=b,b!=c, c!=a]):
            break
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
    ten=["A","B","C", "D", "E","F", "M", "N"]
    random.shuffle(ten)
    ten_diem1, ten_diem2, M=ten[0:3]
    i=random.randint(0,2)
    ten_dt1, ten_dt2= ten_dt1[i], ten_dt2[i]

    chon=random.randint(1,2)
    
    if chon==1:
        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt1}}}:{dt1}$."\
                    f" Đường thẳng ${{{ten_dt2}}}$ đi qua ${{{ten_diem1}}}({x_0};{y_0};{z_0})$ cắt và vuông góc với đường thẳng ${{{ten_dt1}}}$, "
                    f" ${{{ten_dt2}}}$ cắt mặt phẳng $(Oxy)$ tại điểm ${M}(a;b;c)$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười).")

        t_0=-z_0/c
        x, y = x_0+a*t_0, y_0+b*t_0
        dap_an=f"{round_half_up(x+y,1):.1f}".replace(".",",")

        dt2=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        x={latex(x_0+a*t)} \\\\ \n\
        y={latex(y_0+b*t)} \\\\ \n\
        z={latex(z_0+c*t)}\n\
        \\end{{array}} \\right."
        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({b1};{b2};{b3})$.\n\n"\
            f"Gọi ${ten_diem2}({latex(x_2+b1*t)};{latex(y_2+b2*t)};{latex(z_2+b3*t)} ) \\in {ten_dt2}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({latex(x_2+b1*t-x_0)};{latex(y_2+b2*t-y_0)};{latex(z_2+b3*t-z_0)})$.\n\n"\
            f"Do $\\overrightarrow{{{ten_diem1}{ten_diem2}}}\\bot\\overrightarrow{{u_1}}$ nên $\\overrightarrow{{{ten_diem1}{ten_diem2}}}.\\overrightarrow{{u_1}}=0\\Leftrightarrow {b1}({latex(x_2+b1*t-x_0)})+{b2}({latex(y_2+b2*t-y_0)})+{b3}({latex(z_2+b3*t-z_0)})=0\\Rightarrow t={-m}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ qua điểm ${ten_diem1}({x_0};{y_0};{z_0})$ nhận $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({x_2+b1*m-x_0};{y_2+b2*m-y_0};{z_2+b3*m-z_0})$ hoặc $\\overrightarrow{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là\n\n"\
            f"${{{ten_dt2}}}:{dt2}$.\n\n"
            f"${{{ten_dt2}}}$ cắt mặt phẳng $(Oxy)$ khi $c=0\\Rightarrow {latex(z_0+c*t)}=0\\Rightarrow t={phan_so(-z_0/c)}$.\n\n"
            f"$\\Rightarrow x={phan_so(x)},y={phan_so(y)} \\Rightarrow a+b+c={phan_so(x)}+{phan_so(y)}+0={phan_so(x+y)}={dap_an}$.")
    
    if chon==2:
        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt1}}}:{dt1}$."\
                    f" Đường thẳng ${{{ten_dt2}}}$ đi qua ${{{ten_diem1}}}({x_0};{y_0};{z_0})$ cắt và vuông góc với đường thẳng ${{{ten_dt1}}}$, "
                    f" ${{{ten_dt2}}}$ cắt mặt phẳng $(Oyz)$ tại điểm ${M}(a;b;c)$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười).")

        t_0=-x_0/a
        y, z = y_0+b*t_0, z_0+c*t_0
        dap_an=f"{round_half_up(y+z,1):.1f}".replace(".",",")

        dt2=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        x={latex(x_0+a*t)} \\\\ \n\
        y={latex(y_0+b*t)} \\\\ \n\
        z={latex(z_0+c*t)}\n\
        \\end{{array}} \\right."
        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({b1};{b2};{b3})$.\n\n"\
            f"Gọi ${ten_diem2}({latex(x_2+b1*t)};{latex(y_2+b2*t)};{latex(z_2+b3*t)} ) \\in {ten_dt2}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({latex(x_2+b1*t-x_0)};{latex(y_2+b2*t-y_0)};{latex(z_2+b3*t-z_0)})$.\n\n"\
            f"Do $\\overrightarrow{{{ten_diem1}{ten_diem2}}}\\bot\\overrightarrow{{u_1}}$ nên $\\overrightarrow{{{ten_diem1}{ten_diem2}}}.\\overrightarrow{{u_1}}=0\\Leftrightarrow {b1}({latex(x_2+b1*t-x_0)})+{b2}({latex(y_2+b2*t-y_0)})+{b3}({latex(z_2+b3*t-z_0)})=0\\Rightarrow t={-m}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ qua điểm ${ten_diem1}({x_0};{y_0};{z_0})$ nhận $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({x_2+b1*m-x_0};{y_2+b2*m-y_0};{z_2+b3*m-z_0})$ hoặc $\\overrightarrow{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là\n\n"\
            f"${{{ten_dt2}}}:{dt2}$.\n\n"
            f"${{{ten_dt2}}}$ cắt mặt phẳng $(Oyz)$ khi $a=0\\Rightarrow {latex(x_0+a*t)}=0\\Rightarrow t={phan_so(-x_0/a)}$.\n\n"
            f"$\\Rightarrow y={phan_so(y)},z={phan_so(z)} \\Rightarrow a+b+c=0+{phan_so(y)}+{phan_so(z)}={phan_so(y+z)}={dap_an}$.")
         
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B2_29]-SA-M2. Tìm hình chiếu của điểm lên đường thẳng.
def htd_25_xyz_L12_C5_B2_29():

    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    while True:
        a = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        b = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-6, -1), random.randint(1, 7)])

        t_uc=ucln_ba_so(a,b,c)
        a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

        x_0,y_0,z_0 = [random.randint(-6,6) for i in range(3)]
        if x_0 ==0: x_0=random.randint(1,7)
        ten_dt=random.choice(["d","\\Delta"])
        ten_diem=random.choice(["A","B","C","E","F","G","I","M","N"])

        x_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        y_1 = random.randint(-6, -6)
        z_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

        phuongtrinh=Eq(a*(x_0+a*t-x_1)+b*(y_0+b*t-y_1)+c*(z_0+c*t-z_1),0)
        t_0=solve(phuongtrinh,t)[0]
        x_H, y_H, z_H =x_0+a*t_0, y_0+b*t_0, z_0 +c*t_0
        tong=x_H+y_H+z_H

        if all([a!=0, b!=0, c!=0, a!=b,b!=c, c!=a,  tong >-9, tong <99 ]):
            break

    dap_an=f"{round_half_up(x_H+y_H+z_H,1):.1f}".replace(".",",")


    noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}$"
        f" và điểm ${ten_diem}({x_1};{y_1};{z_1})$.\n\n Hình chiếu vuông góc của điểm ${ten_diem}$ trên đường thẳng ${{{ten_dt}}}$ là điểm $H(a;b;c)$. Tính $P=a+b+c$ (kết quả làm tròn đến hàng phần mười).")

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ có véctơ chỉ phương là $\\vec{{u}}=({a};{b};{c})$.\n\n"\
        f"Gọi $H({x_0}+{a}t;{y_0}+{b}t;{z_0}+{c}t)$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}=({latex(x_0+a*t-x_1)};{latex(y_0+b*t-y_1)};{latex(z_0+c*t-z_1)})$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}.\\overrightarrow{{u}}=0\\Leftrightarrow {a}({latex(x_0+a*t-x_1)})+{b}({latex(y_0+b*t-y_1)})+{c}({latex(z_0+c*t-z_1)})=0$"
        f"$\\Rightarrow t={phan_so(t_0)}$. \n\n"\
        f"Tọa độ điểm $H({phan_so(x_H)};{phan_so(y_H)};{phan_so(z_H)})$. \n\nVậy $P={phan_so(x_H)}+{phan_so(y_H)}+{phan_so(z_H)}={phan_so(x_H+y_H+z_H)}={dap_an}$.")
    

    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B2_30]-SA-M4. Tìm đường thẳng đi qua điểm, cắt đường thẳng khác và song song mặt phẳng
def htd_25_xyz_L12_C5_B2_30():
    x,y,z,t=sp.symbols("x y z t")
    while True:
        a = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        b = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        if all([a!=0, b!=0, c!=0, a!=b, b!=c, c!=a]):
            break
    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    ten_dt1=["d","\\Delta", "\\Delta_1"]
    ten_dt2=["d'","\\Delta'", "\\Delta_2"]
    ten=["A","E","M", "B","F","N", "C", "D"]
    random.shuffle(ten)
    ten_diem1, ten_diem2, M=ten[0:3]
    i=random.randint(0,2)
    ten_dt1, ten_dt2 = ten_dt1[i], ten_dt2[i]
    ten_mp=random.choice(["P", "Q", f"\\alpha", f"\\beta", f"\\gamma"])

    #Tạo tọa độ điểm A và điểm cắt B
    chon=random.randint(1,2)
    
    if chon==1:
        while True:

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
            x_3 = x_0+a*m+random.randint(1,2)
            y_3 = y_0+b*m
            z_3 = z_0+c*m

            t_0=-z_0/c
            x_kq, y_kq = x_0+a*t_0, y_0+b*t_0
            if x_kq+y_kq>-9:
                break

        dap_an=f"{round_half_up(x_kq+y_kq,1):.1f}".replace(".",",")
       
        mp=f"{latex(b1*(x-x_3)+b2*(y-y_3)+b3*(z-z_3))}" 
            

        dt2=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        x={latex(x_0+a*t)} \\\\ \n\
        y={latex(y_0+b*t)} \\\\ \n\
        z={latex(z_0+c*t)}\n\
        \\end{{array}} \\right."
        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt1}}}:{dt1}$.\n\n"\
                    f"Đường thẳng ${{{ten_dt2}}}$ đi qua ${{{ten_diem1}({x_0};{y_0};{z_0})}}$ cắt đường thẳng ${{{ten_dt1}}}$ và song song với mặt phẳng $({{{ten_mp}}}):{mp}=0$."
                    f" Biết ${{{ten_dt2}}}$ cắt mặt phẳng $(Oxy)$ tại điểm ${M}(a;b;c)$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười).")    

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a1};{a2};{a3})$.\n\n"\
            f"Gọi ${ten_diem2}({latex(x_2+a1*t)};{latex(y_2+a2*t)};{latex(z_2+a3*t)} ) \\in {ten_dt1}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({latex(x_2+a1*t-x_0)};{latex(y_2+a2*t-y_0)};{latex(z_2+a3*t-z_0)})$.\n\n"\
            f"Mặt phẳng $({{{ten_mp}}}):{mp}=0$ có véctơ pháp tuyến là $\\overrightarrow{{n}}=({b1};{b2};{b3})$.\n\n"\
            f"Do $\\overrightarrow{{{ten_diem1}{ten_diem2}}}\\bot\\overrightarrow{{n}}$ nên $\\overrightarrow{{{ten_diem1}{ten_diem2}}}.\\overrightarrow{{n}}=0\\Leftrightarrow {b1}({latex(x_2+a1*t-x_0)})+{b2}({latex(y_2+a2*t-y_0)})+{b3}({latex(z_2+a3*t-z_0)})=0\\Rightarrow t={-m}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ qua điểm ${ten_diem1}({x_0};{y_0};{z_0})$ nhận $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({x_2+a1*m-x_0};{y_2+a2*m-y_0};{z_2+a3*m-z_0})$ hoặc $\\overrightarrow{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là:\n\n"\
            f"${{{ten_dt2}}}:{dt2}$.\n\n"
            f"${{{ten_dt2}}}$ cắt mặt phẳng $(Oxy)$ khi $c=0\\Rightarrow {latex(z_0+c*t)}=0\\Rightarrow t={phan_so(-z_0/c)}$.\n\n"
                f"$\\Rightarrow x={phan_so(x_kq)},y={phan_so(y_kq)} \\Rightarrow a+b+c={phan_so(x_kq)}+{phan_so(y_kq)}+0={phan_so(x_kq+y_kq)}={dap_an}$.")
    
    if chon==2:
        while True:

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
            x_3 = x_0+a*m+random.randint(1,2)
            y_3 = y_0+b*m
            z_3 = z_0+c*m

            t_0=-x_0/a
            y_kq, z_kq = y_0+b*t_0, z_0+c*t_0                     

            if y_kq+z_kq>-9:
                break

        dap_an=f"{round_half_up(y_kq+z_kq,1):.1f}".replace(".",",")
        mp=f"{latex(b1*(x-x_3)+b2*(y-y_3)+b3*(z-z_3))}" 

        dt2=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        x={latex(x_0+a*t)} \\\\ \n\
        y={latex(y_0+b*t)} \\\\ \n\
        z={latex(z_0+c*t)}\n\
        \\end{{array}} \\right."
            

        noi_dung= my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt1}}}:{dt1}$.\n\n"\
                    f"Đường thẳng ${{{ten_dt2}}}$ đi qua ${{{ten_diem1}({x_0};{y_0};{z_0})}}$ cắt đường thẳng ${{{ten_dt1}}}$ và song song với mặt phẳng $({{{ten_mp}}}):{mp}=0$."
                    f" Biết ${{{ten_dt2}}}$ cắt mặt phẳng $(Oyz)$ tại điểm ${M}(a;b;c)$. Tính $a+b+c$ (kết quả làm tròn đến hàng phần mười).")    

        noi_dung_loigiai=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}=({a1};{a2};{a3})$.\n\n"\
            f"Gọi ${ten_diem2}({latex(x_2+a1*t)};{latex(y_2+a2*t)};{latex(z_2+a3*t)} ) \\in {ten_dt1}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ có véctơ chỉ phương là $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({latex(x_2+a1*t-x_0)};{latex(y_2+a2*t-y_0)};{latex(z_2+a3*t-z_0)})$.\n\n"\
            f"Mặt phẳng $({{{ten_mp}}}):{mp}=0$ có véctơ pháp tuyến là $\\overrightarrow{{n}}=({b1};{b2};{b3})$.\n\n"\
            f"Do $\\overrightarrow{{{ten_diem1}{ten_diem2}}}\\bot\\overrightarrow{{n}}$ nên $\\overrightarrow{{{ten_diem1}{ten_diem2}}}.\\overrightarrow{{n}}=0\\Leftrightarrow {b1}({latex(x_2+a1*t-x_0)})+{b2}({latex(y_2+a2*t-y_0)})+{b3}({latex(z_2+a3*t-z_0)})=0\\Rightarrow t={-m}$.\n\n"
            f"Đường thẳng ${{{ten_dt2}}}$ qua điểm ${ten_diem1}({x_0};{y_0};{z_0})$ nhận $\\overrightarrow{{{ten_diem1}{ten_diem2}}}=({x_2+a1*m-x_0};{y_2+a2*m-y_0};{z_2+a3*m-z_0})$ hoặc $\\overrightarrow{{u}}=({a};{b};{c})$ làm véctơ chỉ phương có phương trình là:\n\n"\
            f"${{{ten_dt2}}}:{dt2}$.\n\n"
            f"${{{ten_dt2}}}$ cắt mặt phẳng $(Oyz)$ khi $a=0\\Rightarrow {latex(x_0+a*t)}=0\\Rightarrow t={phan_so(-x_0/a)}$.\n\n"
            f"$\\Rightarrow y={phan_so(y_kq)},z={phan_so(z_kq)} \\Rightarrow a+b+c=0+{phan_so(y_kq)}+{phan_so(z_kq)}={phan_so(y_kq+z_kq)}={dap_an}$.")   

     
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C5_B2_31]-TF-M3. Cho PTCT của đường thẳng. Xét Đ-S: VTCP, điểm thuộc, vị trí 2 đường, giao điểm của đường và mặt.
def htd_25_xyz_L12_C5_B2_31():
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    n1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    n2 = random.randint(-6, -6)
    n3 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

    if a*n1+b*n2+c*n3==0:
        n2=n2+random.randint(1,3)       

    x_0,y_0,z_0 = [random.randint(-5,5) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,5)
    ten_dt=random.choice(["d","\\Delta"])
    ten_dt2=random.choice(["d_1","\\Delta_1"])
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
    
   
    ptdt=f"\\dfrac{{{latex(x-x_1)}}}{{{a}}}=\\dfrac{{{latex(y-y_1)}}}{{{b}}}=\\dfrac{{{latex(z-z_1)}}}{{{c}}}"      

    noi_dung = my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:{ptdt}$."
    f" Xét tính đúng-sai của các khẳng định sau:")
    
    
    kq1_T=f"* Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$" 
    kq1_F=random.choice([
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{-c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$"])
    
    HDG=f"Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    t_names=["A","B","C","D","E","F", "M","N"]
    A, H, B = random.sample(t_names, 3)

    t_A = random.choice([i for i in range(-2, 2) if i!=0])
    x_A,y_A,z_A = x_1 + a*t_A, y_1 + b*t_A, z_1 + c*t_A
    chon=random.randint(1,3)
    
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Với $t={t_A}$ thay vào phương trình ${{{ten_dt}}}$ ta được"
            f" $x={x_A}, y={y_A}, z={z_A}$ nên điểm ${A}({x_A};{y_A};{z_A})$ thuộc ${{{ten_dt}}}$.")
    
    if chon==2:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Với $t={t_A}$ thay vào phương trình ${{{ten_dt}}}$ ta được"
            f" $x={x_A}, y={y_A}, z={z_A}\\ne {z_A+k}$ nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")

    if chon==3:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A+k};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A+k};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Với $t={t_A}$ thay vào phương trình ${{{ten_dt}}}$ ta được"
            f" $x={x_A}, y={y_A}\\ne {y_A+k}, z={z_A}$ nên điểm ${A}({x_A};{y_A+k};{z_A})$ không thuộc ${{{ten_dt}}}$.")    
    
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Tạo 2 đường vuông góc
    chon=random.randint(1,3)    
    
    if chon==1:
        while True:
            a1 = random.choice([i for i in range(-5, 6) if i!=0])
            b1 = random.choice([i for i in range(-5, 6) if i!=0])
            c1 = random.choice([i for i in range(-5, 6) if i!=0])
            if a*a1+b*b1+c*c1==0:
                break
        x_1= random.choice([i for i in range(-5, 6) if i!=0])
        y_1= random.choice([i for i in range(-5, 6) if i!=0])
        z_1=random.randint(-5,5)
        ptdt_2= f"\\left\\{{ \\begin{{array}}{{l}}\
                x = {show_ptts(x_1,a1)}\\\\ \
                y = {show_ptts(y_1,b1)}\\\\\
                z = {show_ptts(z_1,c1)}\
                \\end{{array}} \\right."     

        kq3_T=f"* Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ vuông góc với đường thẳng ${{{ten_dt}}}$" 
        chon=random.randint(1,2)
        if chon==1:
            kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ {random.choice(["song song", " trùng" ])} nhau"    
        if chon==2:
            kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ cắt và không vuông góc nhau"    
        
        HDG=(f"Đường thẳng ${{{ten_dt2}}}$ có một véctơ chỉ phương là ${vec("u_1")}=({a1};{b1};{c1})$.\n\n"
            f"${vec("u")}.{vec("u_1")}={show_tich(a,a1)}+{show_tich(b,b1)}+{show_tich(c,c1)}=0 \\Rightarrow {vec("u")} \\bot {vec("u_1")}$."
            f" Suy ra ${ten_dt}\\bot {ten_dt2}$."
            )
        kq3=random.choice([kq3_T, kq3_F])

    #Tạo 2 đường song song 
    if chon==2:
        t_0=random.randint(1,2)
        a1, b1, c1 =  a*t_0, b*t_0, c*t_0
        x_1, y_1, z_1 = x_0+a*t_0+random.randint(-1,1), y_0+b*t_0, z_0+c*t_0+random.randint(1,2)
        ptdt_2= f"\\left\\{{ \\begin{{array}}{{l}}\
                x = {show_ptts(x_1,a1)}\\\\ \
                y = {show_ptts(y_1,b1)}\\\\\
                z = {show_ptts(z_1,c1)}\
                \\end{{array}} \\right."
        kq3_T=f"* Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ song song với đường thẳng ${{{ten_dt}}}$"
        kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ {random.choice(["vuông góc", " trùng", "cắt" ])} nhau"  
        HDG=(f" ${{{ten_dt2}}}$ có một véctơ chỉ phương là ${vec("u_1")}=({a1};{b1};{c1})$ cùng phương với ${vec("u")}=({a};{b};{c})$.\n\n"
            f"${{{ten_dt2}}}$ qua điểm ${B}({latex(x_1)};{latex(y_1)};{latex(z_1)})$. Tọa độ ${{{B}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$.\n\n"
            f"Suy ra đường thẳng ${{{ten_dt2}}}$ song song với đường thẳng ${{{ten_dt}}}$."
            )
        kq3=random.choice([kq3_T, kq3_F])

    #Tạo 2 đường cắt nhau
    if chon==3:
        t_0=random.randint(1,2)
        while True:
            a1 = random.choice([i for i in range(-5, 6) if i!=0])
            b1 = random.choice([i for i in range(-5, 6) if i!=0])
            c1 = random.choice([i for i in range(-5, 6) if i!=0])
            if a/a1 != b/b1 or a/a1 != c/c1:
                break
        x_1= x_0+a*t_0
        y_1= y_0+b*t_0
        z_1= z_0+c*t_0
        ptdt_2= f"\\left\\{{ \\begin{{array}}{{l}}\
                x = {show_ptts(x_1,a1)}\\\\ \
                y = {show_ptts(y_1,b1)}\\\\\
                z = {show_ptts(z_1,c1)}\
                \\end{{array}} \\right."     

        kq3_T=f"* Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ cắt với đường thẳng ${{{ten_dt}}}$"        
        kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ {random.choice(["song song", " trùng" ])} nhau"    
          
        
        HDG=(f"Đường thẳng ${{{ten_dt2}}}$ có một véctơ chỉ phương là ${vec("u_1")}=({a1};{b1};{c1})$.\n\n"
            f"${vec("u")}$ và ${vec("u_1")}$ khác phương.\n\n"
            f"${{{ten_dt2}}}$ qua điểm ${B}({latex(x_1)};{latex(y_1)};{latex(z_1)})$. Tọa độ ${{{B}}}$ thỏa mãn phương trình ${{{ten_dt}}}$.\n\n"
            f"Suy ra đường thẳng ${{{ten_dt2}}}$ và đường thẳng ${{{ten_dt}}}$ cắt nhau."
            )
        kq3=random.choice([kq3_T, kq3_F])

    
    
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    tong=x_0+y_0+z_0
    tong_false=x_0+y_0+z_0+random.randint(1,3)

    kq4_T=f"* Gọi điểm ${H}(a;b;c)$ là giao điểm của đường thẳng ${{{ten_dt}}}$ và mặt phẳng ${ten_mp}:{mp}=0$. Khi đó $a+b+c={tong}$"
    kq4_F=f" Gọi điểm ${H}(a;b;c)$ là giao điểm của đường thẳng ${{{ten_dt}}}$ và mặt phẳng ${ten_mp}:{mp}=0$. Khi đó $a+b+c={tong_false}$"
    
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f"Đường thẳng ${{{ten_dt}}}$ có phương trình tham số là ${ptts}$.\n\n"
        f"Xét phương trình ${n1}({latex((x_1+a*t))})+{n2}({latex((y_1+b*t))})+{n3}({latex((z_1+c*t))})+{d}=0\\Rightarrow t={-t1}$.\n\n"
        f"Tọa độ giao điểm của ${{{ten_dt}}}$ và ${{{ten_mp}}}$ là $H({x_0};{y_0};{z_0})$.\n\n Vậy $a+b=c={x_0}+{y_0}+{z_0}={x_0+y_0+z_0}$.")
    HDG=thay_dau_congtru(HDG)
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
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
        f"\\choiceTFt\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {loigiai_latex} \n }}"
        f"\\end{{ex}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C5_B2_32]-TF-M3. Cho PTTS của đường thẳng. Xét Đ-S: VTCP, điểm thuộc, vị trí 2 đường, giao điểm của đường và mặt.
def htd_25_xyz_L12_C5_B2_32():
    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    n1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    n2 = random.randint(-6, -6)
    n3 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

    if a*n1+b*n2+c*n3==0:
        n2=n2+random.randint(1,3)       

    x_0,y_0,z_0 = [random.randint(-5,5) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,5)
    ten_dt=random.choice(["d","\\Delta"])
    ten_dt2=random.choice(["d_1","\\Delta_1"])
    ten_mp=random.choice(["(P)","(Q)", "(R)", f"(\\alpha)", f"(\\beta)", f"(\\gamma)"])

    mp=latex(expand(n1*(x-x_0)+n2*(y-y_0)+n3*(z-z_0)))
    d=-n1*x_0-n2*y_0-n3*z_0

    t1= random.choice([random.randint(-4, -1), random.randint(1, 4)])
    x_1, y_1, z_1 = x_0+a*t1, y_0+b*t1, z_0+c*t1
    
    ptdt= f"\\left\\{{ \\begin{{array}}{{l}}\
        x = {show_ptts(x_1,a)}\\\\ \
        y = {show_ptts(y_1,b)}\\\\\
        z = {show_ptts(z_1,c)}\
\\end{{array}} \\right."   
   
          
    t_names=["A","B","C","D","E","F", "M","N"]
    A, H, B = random.sample(t_names, 3)

    t_A = random.choice([i for i in range(-2, 2) if i!=0])
    x_A,y_A,z_A = x_1 + a*t_A, y_1 + b*t_A, z_1 + c*t_A
    
    noi_dung = my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:{ptdt}$."
    f" Xét tính đúng-sai của các khẳng định sau:")

    tong=x_0+y_0+z_0
    tong_false=x_0+y_0+z_0+random.randint(1,3)

    kq4_T=f"* Gọi điểm ${H}(a;b;c)$ là giao điểm của đường thẳng ${{{ten_dt}}}$ và mặt phẳng ${ten_mp}:{mp}=0$. Khi đó $a+b+c={tong}$"
    kq4_F=f" Gọi điểm ${H}(a;b;c)$ là giao điểm của đường thẳng ${{{ten_dt}}}$ và mặt phẳng ${ten_mp}:{mp}=0$. Khi đó $a+b+c={tong_false}$"
    
    kq4=random.choice([kq4_T, kq4_F])
    HDG=( f"Xét phương trình ${n1}({latex((x_1+a*t))})+{n2}({latex((y_1+b*t))})+{n3}({latex((z_1+c*t))})+{d}=0\\Rightarrow t={-t1}$.\n\n"
        f"Tọa độ giao điểm của ${{{ten_dt}}}$ và ${{{ten_mp}}}$ là $H({x_0};{y_0};{z_0})$.\n\n Vậy $a+b=c={x_0}+{y_0}+{z_0}={x_0+y_0+z_0}$.")
    HDG=thay_dau_congtru(HDG)
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    
    kq1_T=f"* Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$" 
    kq1_F=random.choice([
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{-c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$"])
    
    HDG=f"Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    
    chon=random.randint(1,3)
    
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Với $t={t_A}$ thay vào phương trình ${{{ten_dt}}}$ ta được"
            f" $x={x_A}, y={y_A}, z={z_A}$ nên điểm ${A}({x_A};{y_A};{z_A})$ thuộc ${{{ten_dt}}}$.")
    
    if chon==2:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Với $t={t_A}$ thay vào phương trình ${{{ten_dt}}}$ ta được"
            f" $x={x_A}, y={y_A}, z={z_A}\\ne {z_A+k}$ nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")

    if chon==3:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A+k};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A+k};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Với $t={t_A}$ thay vào phương trình ${{{ten_dt}}}$ ta được"
            f" $x={x_A}, y={y_A}\\ne {y_A+k}, z={z_A}$ nên điểm ${A}({x_A};{y_A+k};{z_A})$ không thuộc ${{{ten_dt}}}$.")    
    
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Tạo 2 đường vuông góc
    chon=random.randint(1,3)    
    
    if chon==1:
        while True:
            a1 = random.choice([i for i in range(-5, 6) if i!=0])
            b1 = random.choice([i for i in range(-5, 6) if i!=0])
            c1 = random.choice([i for i in range(-5, 6) if i!=0])
            if a*a1+b*b1+c*c1==0:
                break
        x_1= random.choice([i for i in range(-5, 6) if i!=0])
        y_1= random.choice([i for i in range(-5, 6) if i!=0])
        z_1=random.randint(-5,5)
        ptdt_2= f"\\left\\{{ \\begin{{array}}{{l}}\
                x = {show_ptts(x_1,a1)}\\\\ \
                y = {show_ptts(y_1,b1)}\\\\\
                z = {show_ptts(z_1,c1)}\
                \\end{{array}} \\right."     

        kq3_T=f"* Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ vuông góc với đường thẳng ${{{ten_dt}}}$" 
        chon=random.randint(1,2)
        if chon==1:
            kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ {random.choice(["song song", " trùng" ])} nhau"    
        if chon==2:
            kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ cắt và không vuông góc nhau"    
        
        HDG=(f"Đường thẳng ${{{ten_dt2}}}$ có một véctơ chỉ phương là ${vec("u_1")}=({a1};{b1};{c1})$.\n\n"
            f"${vec("u")}.{vec("u_1")}={show_tich(a,a1)}+{show_tich(b,b1)}+{show_tich(c,c1)}=0 \\Rightarrow {vec("u")} \\bot {vec("u_1")}$."
            f" Suy ra ${ten_dt}\\bot {ten_dt2}$."
            )
        kq3=random.choice([kq3_T, kq3_F])

    #Tạo 2 đường song song 
    if chon==2:
        t_0=random.randint(1,2)
        a1, b1, c1 =  a*t_0, b*t_0, c*t_0
        x_1, y_1, z_1 = x_0+a*t_0+random.randint(-1,1), y_0+b*t_0, z_0+c*t_0+random.randint(1,2)
        ptdt_2= f"\\left\\{{ \\begin{{array}}{{l}}\
                x = {show_ptts(x_1,a1)}\\\\ \
                y = {show_ptts(y_1,b1)}\\\\\
                z = {show_ptts(z_1,c1)}\
                \\end{{array}} \\right."
        kq3_T=f"* Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ song song với đường thẳng ${{{ten_dt}}}$"
        kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ {random.choice(["vuông góc", " trùng", "cắt" ])} nhau"  
        HDG=(f" ${{{ten_dt2}}}$ có một véctơ chỉ phương là ${vec("u_1")}=({a1};{b1};{c1})$ cùng phương với ${vec("u")}=({a};{b};{c})$.\n\n"
            f"${{{ten_dt2}}}$ qua điểm ${B}({latex(x_1)};{latex(y_1)};{latex(z_1)})$. Tọa độ ${{{B}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$.\n\n"
            f"Suy ra đường thẳng ${{{ten_dt2}}}$ song song với đường thẳng ${{{ten_dt}}}$."
            )
        kq3=random.choice([kq3_T, kq3_F])

    #Tạo 2 đường cắt nhau
    if chon==3:
        t_0=random.randint(1,2)
        while True:
            a1 = random.choice([i for i in range(-5, 6) if i!=0])
            b1 = random.choice([i for i in range(-5, 6) if i!=0])
            c1 = random.choice([i for i in range(-5, 6) if i!=0])
            if a/a1 != b/b1 or a/a1 != c/c1:
                break
        x_1= x_0+a*t_0
        y_1= y_0+b*t_0
        z_1= z_0+c*t_0
        ptdt_2= f"\\left\\{{ \\begin{{array}}{{l}}\
                x = {show_ptts(x_1,a1)}\\\\ \
                y = {show_ptts(y_1,b1)}\\\\\
                z = {show_ptts(z_1,c1)}\
                \\end{{array}} \\right."     

        kq3_T=f"* Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ cắt với đường thẳng ${{{ten_dt}}}$"        
        kq3_F=f" Đường thẳng ${{{ten_dt2}}}:{ptdt_2}$ và đường thẳng ${{{ten_dt}}}$ {random.choice(["song song", " trùng" ])} nhau"    
          
        
        HDG=(f"Đường thẳng ${{{ten_dt2}}}$ có một véctơ chỉ phương là ${vec("u_1")}=({a1};{b1};{c1})$.\n\n"
            f"${vec("u")}$ và ${vec("u_1")}$ khác phương.\n\n"
            f"${{{ten_dt2}}}$ qua điểm ${B}({latex(x_1)};{latex(y_1)};{latex(z_1)})$. Tọa độ ${{{B}}}$ thỏa mãn phương trình ${{{ten_dt}}}$.\n\n"
            f"Suy ra đường thẳng ${{{ten_dt2}}}$ và đường thẳng ${{{ten_dt}}}$ cắt nhau."
            )
        kq3=random.choice([kq3_T, kq3_F])
    
    
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    

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
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung}\n"
        f"\\choiceTFt\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {loigiai_latex} \n }}"
        f"\\end{{ex}}\n")

    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

    return debai,debai_latex,loigiai_word,dap_an

#[D12_C5_B2_33]-TF-M3. Cho điểm và PTCT của dt. Xét Đ-S: VTCP, điểm thuộc, mặt phẳng vuông góc đường thẳng, hình chiếu của điểm
def htd_25_xyz_L12_C5_B2_33():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    while True:
        a = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        b = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-6, -1), random.randint(1, 7)])

        t_uc=ucln_ba_so(a,b,c)
        a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

        x_0,y_0,z_0 = [random.randint(-6,6) for i in range(3)]
        if x_0 ==0: x_0=random.randint(1,7)
        ten_dt=random.choice(["d","\\Delta"])
        ten_diem=random.choice(["A","B","C","E","F","G","I","M","N"])

        x_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        y_1 = random.randint(-6, -6)
        z_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

        phuongtrinh=Eq(a*(x_0+a*t-x_1)+b*(y_0+b*t-y_1)+c*(z_0+c*t-z_1),0)
        t_0=solve(phuongtrinh,t)[0]
        x_H, y_H, z_H =x_0+a*t_0, y_0+b*t_0, z_0 +c*t_0
        tong=x_H+y_H+z_H

        if all([a!=0, b!=0, c!=0, a!=b,b!=c, c!=a,  tong >-9, tong <99 ]):
            break

    t_names=["A","B","C","D","E","F", "M","N"]
    A, H, B = random.sample(t_names, 3)

    t_A = random.choice([i for i in range(-2, 2) if i!=0])
    x_A,y_A,z_A = x_1 + a*t_A, y_1 + b*t_A, z_1 + c*t_A    
    
    noi_dung = my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}$"
        f" và điểm ${ten_diem}({x_1};{y_1};{z_1})$."
        f" Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười):")        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$" 
    kq1_F=random.choice([
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{-c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$"])
    
    HDG=f"Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,3)
    k=random.randint(1,2)
    
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"* Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc ${{{ten_dt}}}$.")
    
    if chon==2:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"* Điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")

    if chon==3:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A+k};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"* Điểm ${A}({x_A};{y_A+k};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_B = random.choice([i for i in range(-5, 6) if i!=0])
    y_B = random.randint(-5,5)
    z_B = random.randint(-5,5)
    ptmp=f"{latex(a*(x-x_B)+b*(y-y_B)+c*(z-z_B))}=0"
    ptmp_false=f"{latex(a*(x+x_B)+b*(y+y_B)+c*(z+z_B)+random.randint(-2,2))}=0"

    kq3_T=f"* Mặt phẳng đi qua điểm ${B}({x_B};{y_B};{z_B})$ và vuông góc với ${{{ten_dt}}}$ có phương trình là ${ptmp}$" 
    kq3_F=f"Mặt phẳng đi qua điểm ${B}({x_B};{y_B};{z_B})$ và vuông góc với ${{{ten_dt}}}$ có phương trình là ${ptmp_false}$"
    
    HDG=thay_dau_congtru(f"Mặt phẳng đi qua điểm ${B}({x_B};{y_B};{z_B})$ và vuông góc với ${{{ten_dt}}}$ nhận  "
        f" vectơ ${vec("u")}=({a};{b};{c})$ làm véctơ pháp tuyến.\n\n"
        f" Phương trình mặt phẳng là: ${a}(x-{x_B})+{b}(y-{y_B})+{c}(z-{z_B})=0 \\Leftrightarrow {ptmp}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    dap_an=f"{round_half_up(x_H+y_H+z_H,1):.1f}".replace(".",",")
    dap_an_false=f"{round_half_up(x_H+y_H+z_H+random.randint(1,2),1):.1f}".replace(".",",")

    kq4_T=f"* Hình chiếu vuông góc của điểm ${ten_diem}$ trên đường thẳng ${{{ten_dt}}}$ là điểm $H(a;b;c)$. Khi đó $a+b+c={dap_an}$"
    kq4_F=f"Hình chiếu vuông góc của điểm ${ten_diem}$ trên đường thẳng ${{{ten_dt}}}$ là điểm $H(a;b;c)$. Khi đó $a+b+c={dap_an_false}$"


    HDG=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ có véctơ chỉ phương là $\\vec{{u}}=({a};{b};{c})$.\n\n"\
        f"Gọi $H({x_0}+{a}t;{y_0}+{b}t;{z_0}+{c}t)$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}=({latex(x_0+a*t-x_1)};{latex(y_0+b*t-y_1)};{latex(z_0+c*t-z_1)})$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}.\\overrightarrow{{u}}=0\\Leftrightarrow {a}({latex(x_0+a*t-x_1)})+{b}({latex(y_0+b*t-y_1)})+{c}({latex(z_0+c*t-z_1)})=0$"
        f"$\\Rightarrow t={phan_so(t_0)}$. \n\n"\
        f"Tọa độ điểm $H({phan_so(x_H)};{phan_so(y_H)};{phan_so(z_H)})$. \n\nVậy $P={phan_so(x_H)}+{phan_so(y_H)}+{phan_so(z_H)}={phan_so(x_H+y_H+z_H)}={dap_an}$.")
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

#[D12_C5_B2_34]-TF-M3. Cho điểm và PTTS của dt. Xét Đ-S: VTCP, điểm thuộc, mặt phẳng vuông góc đường thẳng, hình chiếu của điểm
def htd_25_xyz_L12_C5_B2_34():
    #Tạo bậc ngẫu nhiên
    x,y,z,t=sp.symbols("x y z t")
    while True:
        a = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        b = random.choice([random.randint(-6, -1), random.randint(1, 7)])
        c = random.choice([random.randint(-6, -1), random.randint(1, 7)])

        t_uc=ucln_ba_so(a,b,c)
        a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

        x_0,y_0,z_0 = [random.randint(-6,6) for i in range(3)]
        if x_0 ==0: x_0=random.randint(1,7)
        ten_dt=random.choice(["d","\\Delta"])       

        x_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
        y_1 = random.randint(-6, -6)
        z_1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

        phuongtrinh=Eq(a*(x_0+a*t-x_1)+b*(y_0+b*t-y_1)+c*(z_0+c*t-z_1),0)
        t_0=solve(phuongtrinh,t)[0]
        x_H, y_H, z_H =x_0+a*t_0, y_0+b*t_0, z_0 +c*t_0
        tong=x_H+y_H+z_H

        if all([a!=0, b!=0, c!=0, a!=b,b!=c, c!=a,  tong >-9, tong <99 ]):
            break

    t_names=["A","B","C","D","E","F","G","I", "M","N"]
    A, H, B, ten_diem = random.sample(t_names, 4)

    t_A = random.choice([i for i in range(-2, 2) if i!=0])
    x_A,y_A,z_A = x_1 + a*t_A, y_1 + b*t_A, z_1 + c*t_A

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
                x = {show_ptts(x_0,a)}\\\\ \
                y = {show_ptts(y_0,b)}\\\\\
                z = {show_ptts(z_0,c)}\
                \\end{{array}} \\right."
    ptct=f"\\dfrac{{{latex(x-x_0)}}}{{{a}}}=\\dfrac{{{latex(y-y_0)}}}{{{b}}}=\\dfrac{{{latex(z-z_0)}}}{{{c}}}"
    
    noi_dung = my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:{ptts}$"
        f" và điểm ${ten_diem}({x_1};{y_1};{z_1})$."
        f" Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười):")        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$" 
    kq1_F=random.choice([
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{-b};{c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{-c})$",
        f" Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({-a};{-b};{c})$"])
    
    HDG=f"Một véctơ chỉ phương của đường thẳng ${{{ten_dt}}}$ là ${vec("u")}=({a};{b};{c})$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,3)
    k=random.randint(1,2)
    
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"* Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc ${{{ten_dt}}}$.")
    
    if chon==2:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"* Điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")

    if chon==3:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A+k};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"* Điểm ${A}({x_A};{y_A+k};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_B = random.choice([i for i in range(-5, 6) if i!=0])
    y_B = random.randint(-5,5)
    z_B = random.randint(-5,5)
    ptmp=f"{latex(a*(x-x_B)+b*(y-y_B)+c*(z-z_B))}=0"
    ptmp_false=f"{latex(a*(x+x_B)+b*(y+y_B)+c*(z+z_B)+random.randint(-2,2))}=0"

    kq3_T=f"* Mặt phẳng đi qua điểm ${B}({x_B};{y_B};{z_B})$ và vuông góc với ${{{ten_dt}}}$ có phương trình là ${ptmp}$" 
    kq3_F=f"Mặt phẳng đi qua điểm ${B}({x_B};{y_B};{z_B})$ và vuông góc với ${{{ten_dt}}}$ có phương trình là ${ptmp_false}$"
    
    HDG=thay_dau_congtru(f"Mặt phẳng đi qua điểm ${B}({x_B};{y_B};{z_B})$ và vuông góc với ${{{ten_dt}}}$ nhận  "
        f" vectơ ${vec("u")}=({a};{b};{c})$ làm véctơ pháp tuyến.\n\n"
        f" Phương trình mặt phẳng là: ${a}(x-{x_B})+{b}(y-{y_B})+{c}(z-{z_B})=0 \\Leftrightarrow {ptmp}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    dap_an=f"{round_half_up(x_H+y_H+z_H,1):.1f}".replace(".",",")
    dap_an_false=f"{round_half_up(x_H+y_H+z_H+random.randint(1,2),1):.1f}".replace(".",",")

    kq4_T=f"* Hình chiếu vuông góc của điểm ${ten_diem}$ trên đường thẳng ${{{ten_dt}}}$ là điểm $H(a;b;c)$. Khi đó $a+b+c={dap_an}$"
    kq4_F=f"Hình chiếu vuông góc của điểm ${ten_diem}$ trên đường thẳng ${{{ten_dt}}}$ là điểm $H(a;b;c)$. Khi đó $a+b+c={dap_an_false}$"


    HDG=my_module.thay_dau_congtru(f"Đường thẳng ${{{ten_dt}}}$ có véctơ chỉ phương là $\\vec{{u}}=({a};{b};{c})$.\n\n"\
        f"Gọi $H({x_0}+{a}t;{y_0}+{b}t;{z_0}+{c}t)$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}=({latex(x_0+a*t-x_1)};{latex(y_0+b*t-y_1)};{latex(z_0+c*t-z_1)})$.\n\n"\
        f"$\\overrightarrow{{{ten_diem}H}}.\\overrightarrow{{u}}=0\\Leftrightarrow {a}({latex(x_0+a*t-x_1)})+{b}({latex(y_0+b*t-y_1)})+{c}({latex(z_0+c*t-z_1)})=0$"
        f"$\\Rightarrow t={phan_so(t_0)}$. \n\n"\
        f"Tọa độ điểm $H({phan_so(x_H)};{phan_so(y_H)};{phan_so(z_H)})$. \n\nVậy $P={phan_so(x_H)}+{phan_so(y_H)}+{phan_so(z_H)}={phan_so(x_H+y_H+z_H)}={dap_an}$.")
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

#[D12_C5_B2_35]-TF-M3. Cho (P) và PTCT của d. Xét Đ-S: điểm thuộc d,VTPT của (P), PTTS d, d giao (P)
def htd_25_xyz_L12_C5_B2_35():

    x,y,z,t=sp.symbols("x y z t")
    a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a,b,c)
    a,b,c=int(a/t_uc),int(b/t_uc),int(c/t_uc)

    n1 = random.choice([random.randint(-7, -1), random.randint(1, 7)])
    n2 = random.randint(-6, -6)
    n3 = random.choice([random.randint(-7, -1), random.randint(1, 7)])

    if a*n1+b*n2+c*n3==0:
        n2=n2+random.randint(1,3)       

    x_0,y_0,z_0 = [random.randint(-5,5) for i in range(3)]
    if x_0 ==0: x_0=random.randint(1,5)
    ten_dt=random.choice(["d","\\Delta"])
    ten_dt2=random.choice(["d_1","\\Delta_1"])
    ten_mp=random.choice(["(P)","(Q)", "(R)", f"(\\alpha)", f"(\\beta)", f"(\\gamma)"])

    mp=f"{latex(expand(n1*(x-x_0)+n2*(y-y_0)+n3*(z-z_0)))}=0"
    d=-n1*x_0-n2*y_0-n3*z_0

    t1= random.choice([random.randint(-4, -1), random.randint(1, 4)])
    x_1, y_1, z_1 = x_0+a*t1, y_0+b*t1, z_0+c*t1
    
        
    ptct=f"\\dfrac{{{latex(x-x_1)}}}{{{a}}}=\\dfrac{{{latex(y-y_1)}}}{{{b}}}=\\dfrac{{{latex(z-z_1)}}}{{{c}}}"
   
          
    t_names=["A","B","C","D","E","F", "M","N"]
    A, H, B = random.sample(t_names, 3)

    t_A = random.choice([i for i in range(-2, 2) if i!=0])
    x_A,y_A,z_A = x_1 + a*t_A, y_1 + b*t_A, z_1 + c*t_A
    
    noi_dung = my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho đường thẳng ${{{ten_dt}}}:{ptct}$ và mặt phẳng ${ten_mp}:{mp}$."
    f" Xét tính đúng-sai của các khẳng định sau:")

    tong=x_0+y_0+z_0
    tong_false=x_0+y_0+z_0+random.randint(1,3)

    kq4_T=f"* Gọi điểm ${H}(a;b;c)$ là giao điểm của đường thẳng ${{{ten_dt}}}$ và mặt phẳng ${ten_mp}:{mp}=0$. Khi đó $a+b+c={tong}$"
    kq4_F=f" Gọi điểm ${H}(a;b;c)$ là giao điểm của đường thẳng ${{{ten_dt}}}$ và mặt phẳng ${ten_mp}:{mp}=0$. Khi đó $a+b+c={tong_false}$"
    
    kq4=random.choice([kq4_T, kq4_F])
    HDG=( f"Xét phương trình ${n1}({latex((x_1+a*t))})+{n2}({latex((y_1+b*t))})+{n3}({latex((z_1+c*t))})+{d}=0\\Rightarrow t={-t1}$.\n\n"
        f"Tọa độ giao điểm của ${{{ten_dt}}}$ và ${{{ten_mp}}}$ là $H({x_0};{y_0};{z_0})$.\n\n Vậy $a+b=c={x_0}+{y_0}+{z_0}={x_0+y_0+z_0}$.")
    HDG=thay_dau_congtru(HDG)
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    kq1_T=f"* ${ten_mp}$ có một véctơ pháp tuyến là ${vec("n")}=({n1};{n2};{n3})$" 
    kq1_F= random.choice([
            f"${ten_mp}$ có một véctơ pháp tuyến là ${vec("n")}=({n1};{n2};{n3+random.randint(1,2)})$",
            f"${ten_mp}$ có một véctơ pháp tuyến là ${vec("n")}=({n1+random.randint(1,2)};{n2};{n3})$",
            f"${ten_mp}$ có một véctơ pháp tuyến là ${vec("n")}=({-n1};{-n2};{n3+random.randint(1,2)})$"])
    
    HDG=f"$({ten_mp})$ có một véctơ pháp tuyến là ${vec("n")}=({n1};{n2};{n3})$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,3)
    k=random.randint(1,2)
    
    if chon==1:
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc ${{{ten_dt}}}$.")
    
    if chon==2:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A};{z_A+k})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")

    if chon==3:
        k= random.choice([i for i in range(-3, 3) if i!=0])
        kq2_T=f"* Điểm ${A}({x_A};{y_A+k};{z_A})$ không thuộc đường thẳng ${{{ten_dt}}}$"
        kq2_F=f"Điểm ${A}({x_A};{y_A+k};{z_A})$ thuộc đường thẳng ${{{ten_dt}}}$"
        
        HDG=(f"Tọa độ điểm ${{{A}}}$ không thỏa mãn phương trình ${{{ten_dt}}}$"
            f" nên điểm ${A}({x_A};{y_A};{z_A+k})$ không thuộc ${{{ten_dt}}}$.")

    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    ptts= f"\\left\\{{ \\begin{{array}}{{l}}\
        x = {show_ptts(x_1,a)}\\\\ \
        y = {show_ptts(y_1,b)}\\\\\
        z = {show_ptts(z_1,c)}\
\\end{{array}} \\right."
    
    ptts_false= f"\\left\\{{ \\begin{{array}}{{l}}\
        x = {show_ptts(-x_1,a)}\\\\ \
        y = {show_ptts(-y_1,b)}\\\\\
        z = {show_ptts(z_1+random.randint(-1,2),c)}\
\\end{{array}} \\right."


    kq3_T=f"* Phương trình tham số của ${{{ten_dt}}}$ là ${ptts}$" 
    kq3_F=f"Phương trình tham số của ${{{ten_dt}}}$ là ${ptts_false}$"
    
    HDG=(f"${{{ten_dt}}}$ qua ${B}({x_1};{y_1};{z_1})$ nhận ${vec("u")}=({a};{b};{c})$ làm véctơ chỉ phương.\n\n"
        f"Phương trình tham số của ${{{ten_dt}}}$ là ${ptts}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

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

def generate_random_goc(a, count=10, min_val=0, max_val=90):
    numbers = set()
    while len(numbers) < count:
        num = round_half_up(random.uniform(min_val, max_val), 2)  # Làm tròn đến 2 chữ số thập phân
        if num != a:
            numbers.add(num)
    return list(numbers)

#[D12_C5_B2_36]-M2. Cho 2 đường thẳng dạng PTCT. Tìm góc.
def htd_25_xyz_L12_C5_B2_36():

    x,y,z,t=sp.symbols("x y z t")
    a1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

    a2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a2,b2,c2)
    a2,b2,c2=int(a2/t_uc),int(b2/t_uc),int(c2/t_uc)

    while True:
        x_1,y_1,z_1=[random.randint(-4,4) for _ in range(3)]
        x_2,y_2,z_2=[random.randint(-4,4) for _ in range(3)]
        if all([x_1 != x_2, y_1!=y_2]):
            break
    pt_d1=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"
    pt_d2=f"\\dfrac{{{latex(x-x_2)}}}{{{a2}}}=\\dfrac{{{latex(y-y_2)}}}{{{b2}}}=\\dfrac{{{latex(z-z_2)}}}{{{c2}}}"


    d1=["d", "d_1", "\\Delta_1"]
    d2=["d'", "d_2",  "\\Delta_2"]
    i=random.randint(0,2)
    d1, d2=d1[i], d2[i]

    noi_dung=my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, góc giữa hai đường thẳng ${d1}:{pt_d1}$ và ${d2}:{pt_d2}$ bằng"
        f" (kết quả làm tròn đến hàng phần trăm)" )

    tich_vh=a1*a2+b1*b2+c1*c2
    dodai_1=sqrt(a1**2+b1**2+c1**2)
    dodai_2=sqrt(a2**2+b2**2+c2**2)

    cos_goc=abs(tich_vh)/(dodai_1*dodai_2)
    goc_rad=math.acos(cos_goc)
    goc_deg=math.degrees(goc_rad)    

    kq=goc_deg
    kq_false=generate_random_goc(goc_deg)
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    if kq=="0,00": kq="0"
    kq2=f"{kq2}".replace(".",",")
    kq3=f"{kq3}".replace(".",",")
    kq4=f"{kq4}".replace(".",",")

    vec_1,vec_2=vec("u_1"), vec("u_2")
    noi_dung_loigiai=(
    f"${{{d1}}}$ có véctơ chỉ phương ${vec_1}=({a1};{b1};{c1})$.\n\n"
    f"${{{d2}}}$ có véctơ chỉ phương ${vec_2}=({a2};{b2};{c2})$.\n\n"
    f"$\\cos({d1},{d2})=\\dfrac{{|{vec_1}.{vec_2}|}}{{|{vec_1}|.|{vec_2}|}}"
    f"=\\dfrac{{{abs(tich_vh)}}}{{{latex(dodai_1)}.{latex(dodai_2)}}}={{{latex(nsimplify(cos_goc))}}}$.\n\n"
    f"$\\Rightarrow ({d1},{d2}) = {kq}^\\circ$."
    )

    pa_A= f"*${kq}^\\circ$"
    pa_B= f"${kq2}^\\circ$"
    pa_C= f"${kq3}^\\circ$"
    pa_D= f"${kq4}^\\circ$"
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

#[D12_C5_B2_37]-M2. Cho 2 mặt phẳng. Tìm góc.
def htd_25_xyz_L12_C5_B2_37():

    x,y,z,t=sp.symbols("x y z t")
    a1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

    a2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a2,b2,c2)
    a2,b2,c2=int(a2/t_uc),int(b2/t_uc),int(c2/t_uc)

    while True:
        x_1,y_1,z_1=[random.randint(-4,4) for _ in range(3)]
        x_2,y_2,z_2=[random.randint(-4,4) for _ in range(3)]
        if all([x_1 != x_2, y_1!=y_2]):
            break
    pt_P1=f"{latex(a1*(x-x_1)+b1*(y-y_1)+c1*(z-z_1))}=0"
    pt_P2=f"{latex(a2*(x-x_2)+b2*(y-y_2)+c2*(z-z_2))}=0"


    P1=["P", "P_1", "Q_1", "R_1", "P", "Q", "R", "\\alpha", "\\alpha", "\\beta"]
    P2=["Q", "P_2",  "Q_2", "R_2", "R", "R", "Q", "\\beta", "\\gamma", "\\gamma"]
    i=random.randint(0,len(P1)-1)
    P1, P2=P1[i], P2[i]

    noi_dung=my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, góc giữa hai mặt phẳng $({P1}):{pt_P1}$ và $({P2}):{pt_P2}$ bằng"
        f" (kết quả làm tròn đến hàng phần trăm)." )

    tich_vh=a1*a2+b1*b2+c1*c2
    dodai_1=sqrt(a1**2+b1**2+c1**2)
    dodai_2=sqrt(a2**2+b2**2+c2**2)

    cos_goc=abs(tich_vh)/(dodai_1*dodai_2)
    goc_rad=math.acos(cos_goc)
    goc_deg=math.degrees(goc_rad)    

    kq=goc_deg
    kq_false=generate_random_goc(goc_deg)
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    if kq=="0,00": kq="0"
    kq2=f"{kq2}".replace(".",",")
    kq3=f"{kq3}".replace(".",",")
    kq4=f"{kq4}".replace(".",",")

    vec_1,vec_2=vec("n_1"), vec("n_2")
    noi_dung_loigiai=(
    f"${{({P1})}}$ có véctơ pháp tuyến ${vec_1}=({a1};{b1};{c1})$.\n\n"
    f"${{({P2})}}$ có véctơ pháp tuyến ${vec_2}=({a2};{b2};{c2})$.\n\n"
    f"$\\cos\\left(({P1}),({P2})\\right)=\\dfrac{{|{vec_1}.{vec_2}|}}{{|{vec_1}|.|{vec_2}|}}"
    f"=\\dfrac{{{abs(tich_vh)}}}{{{latex(dodai_1)}.{latex(dodai_2)}}}={{{latex(nsimplify(cos_goc))}}}$.\n\n"
    f"$\\Rightarrow \\left(({P1}),({P2})\\right) = {kq}^\\circ$."
    )

    pa_A= f"*${kq}^\\circ$"
    pa_B= f"${kq2}^\\circ$"
    pa_C= f"${kq3}^\\circ$"
    pa_D= f"${kq4}^\\circ$"
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

#[D12_C5_B2_38]-M3. Cho 2 đường thẳng dạng PTTS. Tìm góc.
def htd_25_xyz_L12_C5_B2_38():

    x,y,z,t=sp.symbols("x y z t")
    a1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

    a2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a2,b2,c2)
    a2,b2,c2=int(a2/t_uc),int(b2/t_uc),int(c2/t_uc)

    while True:
        x_1,y_1,z_1=[random.randint(-4,4) for _ in range(3)]
        x_2,y_2,z_2=[random.randint(-4,4) for _ in range(3)]
        if all([x_1 != x_2, y_1!=y_2]):
            break
    pt_d1= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_1,a1)}\\\\ \
y = {show_ptts(y_1,b1)}\\\\\
z = {show_ptts(z_1,c1)}\
\\end{{array}} \\right."
    
    pt_d2= f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_2,a2)}\\\\ \
y = {show_ptts(y_2,b2)}\\\\\
z = {show_ptts(z_2,c2)}\
\\end{{array}} \\right."


    d1=["d", "d_1", "\\Delta_1"]
    d2=["d'", "d_2",  "\\Delta_2"]
    i=random.randint(0,2)
    d1, d2=d1[i], d2[i]

    noi_dung=my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, góc giữa hai đường thẳng ${d1}:{pt_d1}$ và ${d2}:{pt_d2}$ bằng"
        f" (kết quả làm tròn đến hàng phần trăm)." )

    tich_vh=a1*a2+b1*b2+c1*c2
    dodai_1=sqrt(a1**2+b1**2+c1**2)
    dodai_2=sqrt(a2**2+b2**2+c2**2)

    cos_goc=abs(tich_vh)/(dodai_1*dodai_2)
    goc_rad=math.acos(cos_goc)
    goc_deg=math.degrees(goc_rad)    

    kq=goc_deg
    kq_false=generate_random_goc(goc_deg)
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    if kq=="0,00": kq="0"
    kq2=f"{kq2}".replace(".",",")
    kq3=f"{kq3}".replace(".",",")
    kq4=f"{kq4}".replace(".",",")

    vec_1,vec_2=vec("u_1"), vec("u_2")
    noi_dung_loigiai=(
    f"${{{d1}}}$ có véctơ chỉ phương ${vec_1}=({a1};{b1};{c1})$.\n\n"
    f"${{{d2}}}$ có véctơ chỉ phương ${vec_2}=({a2};{b2};{c2})$.\n\n"
    f"$\\cos({d1},{d2})=\\dfrac{{|{vec_1}.{vec_2}|}}{{|{vec_1}|.|{vec_2}|}}"
    f"=\\dfrac{{{abs(tich_vh)}}}{{{latex(dodai_1)}.{latex(dodai_2)}}}={{{latex(nsimplify(cos_goc))}}}$.\n\n"
    f"$\\Rightarrow ({d1},{d2}) = {kq}^\\circ$."
    )

    pa_A= f"*${kq}^\\circ$"
    pa_B= f"${kq2}^\\circ$"
    pa_C= f"${kq3}^\\circ$"
    pa_D= f"${kq4}^\\circ$"
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

#[D12_C5_B2_39]-M3. Cho 2 đường thẳng dạng PTTS+PTCT. Tìm góc.
def htd_25_xyz_L12_C5_B2_39():

    x,y,z,t=sp.symbols("x y z t")
    a1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

    a2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a2,b2,c2)
    a2,b2,c2=int(a2/t_uc),int(b2/t_uc),int(c2/t_uc)

    while True:
        x_1,y_1,z_1=[random.randint(-4,4) for _ in range(3)]
        x_2,y_2,z_2=[random.randint(-4,4) for _ in range(3)]
        if all([x_1 != x_2, y_1!=y_2]):
            break
    chon=random.randint(1,2)
    if chon==1:
        pt_d1=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"
        pt_d2= f"\\left\\{{ \\begin{{array}}{{l}}\
            x = {show_ptts(x_2,a2)}\\\\ \
            y = {show_ptts(y_2,b2)}\\\\\
            z = {show_ptts(z_2,c2)}\
            \\end{{array}} \\right."
    
    if chon==2:
        pt_d1= f"\\left\\{{ \\begin{{array}}{{l}}\
        x = {show_ptts(x_1,a1)}\\\\ \
        y = {show_ptts(y_1,b1)}\\\\\
        z = {show_ptts(z_1,c1)}\
        \\end{{array}} \\right."   
    
        pt_d2=f"\\dfrac{{{latex(x-x_2)}}}{{{a2}}}=\\dfrac{{{latex(y-y_2)}}}{{{b2}}}=\\dfrac{{{latex(z-z_2)}}}{{{c2}}}"  

    d1=["d", "d_1", "\\Delta_1"]
    d2=["d'", "d_2",  "\\Delta_2"]
    i=random.randint(0,2)
    d1, d2=d1[i], d2[i]

    noi_dung=my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, cho hai đường thẳng ${d1}:{pt_d1}$ và ${d2}:{pt_d2}$. Góc giữa hai đường thẳng đã cho bằng"
        f" (kết quả làm tròn đến hàng phần trăm)." )

    tich_vh=a1*a2+b1*b2+c1*c2
    dodai_1=sqrt(a1**2+b1**2+c1**2)
    dodai_2=sqrt(a2**2+b2**2+c2**2)

    cos_goc=abs(tich_vh)/(dodai_1*dodai_2)
    goc_rad=math.acos(cos_goc)
    goc_deg=math.degrees(goc_rad)    

    kq=goc_deg
    kq_false=generate_random_goc(goc_deg)
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    if kq=="0,00": kq="0"
    kq2=f"{kq2}".replace(".",",")
    kq3=f"{kq3}".replace(".",",")
    kq4=f"{kq4}".replace(".",",")

    vec_1,vec_2=vec("u_1"), vec("u_2")
    noi_dung_loigiai=(
    f"${{{d1}}}$ có véctơ chỉ phương ${vec_1}:({a1};{b1};{c1})$.\n\n"
    f"${{{d2}}}$ có véctơ chỉ phương ${vec_2}:({a2};{b2};{c2})$.\n\n"
    f"$\\cos({d1},{d2})=\\dfrac{{|{vec_1}.{vec_2}|}}{{|{vec_1}|.|{vec_2}|}}"
    f"=\\dfrac{{{abs(tich_vh)}}}{{{latex(dodai_1)}.{latex(dodai_2)}}}={{{latex(nsimplify(cos_goc))}}}$.\n\n"
    f"$\\Rightarrow ({d1},{d2}) = {kq}^\\circ$."
    )

    pa_A= f"*${kq}^\\circ$"
    pa_B= f"${kq2}^\\circ$"
    pa_C= f"${kq3}^\\circ$"
    pa_D= f"${kq4}^\\circ$"
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

#[D12_C5_B2_40]-M2. Cho đường thẳng và mặt phẳng. Tìm góc.
def htd_25_xyz_L12_C5_B2_40():

    x,y,z,t=sp.symbols("x y z t")
    a1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c1 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a1,b1,c1)
    a1,b1,c1=int(a1/t_uc),int(b1/t_uc),int(c1/t_uc)

    a2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    c2 = random.choice([random.randint(-5, -1), random.randint(1, 5)])   

    t_uc=ucln_ba_so(a2,b2,c2)
    a2,b2,c2=int(a2/t_uc),int(b2/t_uc),int(c2/t_uc)

    while True:
        x_1,y_1,z_1=[random.randint(-4,4) for _ in range(3)]
        x_2,y_2,z_2=[random.randint(-4,4) for _ in range(3)]
        if all([x_1 != x_2, y_1!=y_2]):
            break
    chon=random.randint(1,2)
    if chon==1:
        pt_d=f"\\dfrac{{{latex(x-x_1)}}}{{{a1}}}=\\dfrac{{{latex(y-y_1)}}}{{{b1}}}=\\dfrac{{{latex(z-z_1)}}}{{{c1}}}"
    
    if chon==2:    
        pt_d= f"\\left\\{{ \\begin{{array}}{{l}}\
    x = {show_ptts(x_1,a1)}\\\\ \
    y = {show_ptts(y_1,b1)}\\\\\
    z = {show_ptts(z_1,c1)}\
    \\end{{array}} \\right." 

    pt_P=f"{latex(a2*(x-x_2)+b2*(y-y_2)+c2*(z-z_2))}=0"

    P=random.choice(["P", "Q", "R", "\\alpha", "\\gamma", "\\beta"])
    d=random.choice(["d", "d_1", "\\Delta" ])


    noi_dung=my_module.thay_dau_congtru(f"Trong không gian ${{Oxyz}}$, góc giữa đường thẳng ${d}:{pt_d}$ và mặt phẳng $({P}):{pt_P}$ bằng"
        f" (kết quả làm tròn đến hàng phần trăm)." )

    tich_vh=a1*a2+b1*b2+c1*c2
    dodai_1=sqrt(a1**2+b1**2+c1**2)
    dodai_2=sqrt(a2**2+b2**2+c2**2)

    sin_goc=abs(tich_vh)/(dodai_1*dodai_2)
    goc_rad=math.asin(sin_goc)
    goc_deg=math.degrees(goc_rad)    

    kq=goc_deg
    kq_false=generate_random_goc(goc_deg)
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    if kq=="0,00": kq="0"
    kq2=f"{kq2}".replace(".",",")
    kq3=f"{kq3}".replace(".",",")
    kq4=f"{kq4}".replace(".",",")

    vec_1,vec_2=vec("u"), vec("n")
    noi_dung_loigiai=(
    f"${{{d}}}$ có véctơ chỉ phương ${vec_1}=({a1};{b1};{c1})$.\n\n"
    f"${{({P})}}$ có véctơ pháp tuyến ${vec_2}=({a2};{b2};{c2})$.\n\n"
    f"$\\sin({d},({P}))=\\dfrac{{|{vec_1}.{vec_2}|}}{{|{vec_1}|.|{vec_2}|}}"
    f"=\\dfrac{{{abs(tich_vh)}}}{{{latex(dodai_1)}.{latex(dodai_2)}}}={{{latex(nsimplify(sin_goc))}}}$.\n\n"
    f"$\\Rightarrow ({d},({P})) = {kq}^\\circ$."
    )

    pa_A= f"*${kq}^\\circ$"
    pa_B= f"${kq2}^\\circ$"
    pa_C= f"${kq3}^\\circ$"
    pa_D= f"${kq4}^\\circ$"
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