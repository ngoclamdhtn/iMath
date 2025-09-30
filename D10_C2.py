import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module

def tao_chuoi_so_nguyen(a, b):
    # Tạo danh sách các số nguyên từ a đến b
    danh_sach_so = list(range(a, b))
    danh_sach_so = [x for x in danh_sach_so if x != 0 and x%2!=0]
    
    # Chuyển đổi các số thành chuỗi
    chuoi_so = [str(x) for x in danh_sach_so]
    
    # Nối chuỗi bằng dấu ,
    chuoi_ket_qua = ",".join(chuoi_so)
    
    return chuoi_ket_qua

def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(10000000000000))
    return m

def ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st):
    code=f" \\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick]\n\
    \\tikzset{{every node/.style={{scale=0.9}}}}\n\
    \\begin{{scope}}\n\
        \\clip ({x_min},{y_min}) rectangle ({x_max+0.2},{y_max+0.2});\n\
        {st}\n\
        \\draw [blue, thick]({x_min},{y_1})--({x_max},{y_2});\n\
    \\end{{scope}}\n\
    \\draw[->] ({x_min},0)--({x_max+0.2},0);\n\
    \\draw({x_max+0.2},0) node[below]{{$x$}};\n\
    \\draw(0,{y_max+0.2}) node[above]{{$y$}};\n\
    \\draw[->] (0,{y_min})--(0,{y_max+0.2});\n\
    \\draw (0,0) node[below left]{{$O$}};\n\
    \\foreach \\x in {{-1,-2,1,2}}\n\
    \\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {{$\\x$}};\n\
    \\foreach \\y in {{-1,-2,1,2}}\n\
    \\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {{$\\y$}};\n\
\\end{{tikzpicture}}"
    return code


def code_latex_mien_nghiem(a,b,c,dau):
    #ax+by+c>0
    x,y=sp.symbols("x y")
    x_0, y_0=-c/a, -c/b
    f=(-a*x-c)/b

    #x_0>0, y_0<0 Đường thẳng đồng biến
    if x_0>0 and y_0 <0:        
        x_min, x_max=-4, int(x_0)+2
        y_min, y_max=int(y_0)-2, 4
        y_1=f.subs(x,x_min)
        y_2=f.subs(x,x_max)

        #Thay tọa độ phần bên dưới để thử miền nghiệm
        x_1=x_0+1
        t=a*x_1+c

        if ((dau==">0" or dau==">=0") and t>0) or ((dau=="<0" or dau=="<=0") and t<0):
        #Miền dưới là nghiệm            
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_min},{y_max})--({x_max},{y_max})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)
        
        
        #Miền trên là nghiệm
        if ((dau==">0" or dau==">=0") and t<0) or ((dau=="<0" or dau=="<=0") and t>0):                
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_min},{y_min})--({x_max},{y_min})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)

    #-------------------------------------------------------------------->
    
    #x_0>0, y_0>0 Đường thẳng nghịch biến
    if x_0>0 and y_0 >0:
        x_min, x_max=-4, int(x_0)+2
        y_min, y_max=-4, int(y_0)+2
        y_1=f.subs(x,x_min)
        y_2=f.subs(x,x_max)

        #Thay tọa độ phần bên dưới để thử miền nghiệm
        x_1=x_0-1
        t=a*x_1+c
        if ((dau==">0" or dau==">=0") and t>0) or ((dau=="<0" or dau=="<=0") and t<0):                     
            #Lấy nửa dưới            
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_max},{y_1})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)
            #Lấy nửa trên
        if ((dau==">0" or dau==">=0") and t<0) or ((dau=="<0" or dau=="<=0") and t>0):                
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_min},{y_min})--({x_max},{y_min})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)
        
    #-------------------------------------------------------------------->

    #x_0<0, y_0>0 Đường thẳng đồng biến
    if x_0<0 and y_0 >0:        
        x_min, x_max=int(x_0)-2, 4 
        y_min, y_max=-4, int(y_0)+2
        y_1=f.subs(x,x_min)
        y_2=f.subs(x,x_max)

        #Thay tọa độ phần bên dưới để thử miền nghiệm
        x_1=x_0+1
        t=a*x_1+c

        if ((dau==">0" or dau==">=0") and t>0) or ((dau=="<0" or dau=="<=0") and t<0):
        #Miền dưới là nghiệm            
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_min},{y_max})--({x_max},{y_max})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)
        
        #Miền trên là nghiệm
        if ((dau==">0" or dau==">=0") and t<0) or ((dau=="<0" or dau=="<=0") and t>0):
                
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_min},{y_min})--({x_max},{y_min})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)
    
    
    #x_0<0, y_0<0 Đường thẳng nghịch biến
    if x_0<0 and y_0 <0:
        x_min, x_max=int(x_0)-2, 4
        y_min, y_max=int(y_0)-2, 4
        y_1=f.subs(x,x_min)
        y_2=f.subs(x,x_max)

        #Thay tọa độ phần bên dưới để thử miền nghiệm
        x_1=x_0-1
        t=a*x_1+c
        if ((dau==">0" or dau==">=0") and t>0) or ((dau=="<0" or dau=="<=0") and t<0):                     
            
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_min},{y_max})--({x_max},{y_max})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)
            #Lấy nửa trên
        if ((dau==">0" or dau==">=0") and t<0) or ((dau=="<0" or dau=="<=0") and t>0):
            
            st=f"\\fill[pattern=north east lines] ({x_min},{y_1})--({x_min},{y_min})--({x_max},{y_2})--cycle;"
            code=ghep_code_ve_mien(x_min,y_min,x_max,y_max,y_1,y_2,st)
                
    return code


#BÀI 1 - BẤT PHƯƠNG TRÌNH BẬC NHẤT 2 ẨN
def mien_nghiem_BPT_2an(a,b,c,dau): 
   

    lst_nghiem=[]
    if dau==">":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a*x_0+b*y_0+c >0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
    if dau=="<":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a*x_0+b*y_0+c <0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
    random.shuffle(lst_nghiem)

    return lst_nghiem

def mien_not_nghiem_BPT_2an(a,b,c,dau):   

    lst_nghiem=[]
    if dau==">":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a*x_0+b*y_0+c <0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
    if dau=="<":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a*x_0+b*y_0+c >0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
    random.shuffle(lst_nghiem)

    return lst_nghiem

def mien_nghiem_HeBPT_2an(a1,b1,c1,dau1,a2,b2,c2,dau2):
      

    lst_nghiem=[]

    if dau1==">" and dau2==">":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 >0 and a2*x_0+b2*y_0+c2>0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if dau1==">" and dau2=="<":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 >0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if dau1=="<" and dau2==">":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 <0 and a2*x_0+b2*y_0+c2>0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if dau1=="<" and dau2=="<":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 <0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
    
    random.shuffle(lst_nghiem)

    return lst_nghiem

def mien_nghiem_He3BPT_2an(a1,b1,c1,dau1,a2,b2,c2,dau2,a3,b3,c3,dau3):

    lst_nghiem=[]

    if all([dau1==">", dau2==">", dau3==">"]):
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if all([a1*x_0+b1*y_0+c1 >0, a2*x_0+b2*y_0+c2>0, a3*x_0+b3*y_0+c3>0]):
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if all([dau1=="<", dau2=="<", dau3=="<"]):
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if all([a1*x_0+b1*y_0+c1 <0, a2*x_0+b2*y_0+c2<0, a3*x_0+b3*y_0+c3<0]):
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";")) 
    
    random.shuffle(lst_nghiem)

    return lst_nghiem

def mien_not_nghiem_He3BPT_2an(a1,b1,c1,dau1,a2,b2,c2,dau2,a3,b3,c3,dau3):
    lst_nghiem=[]

    if all([dau1==">", dau2==">", dau3==">"]):
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if all([a1*x_0+b1*y_0+c1 >0, a2*x_0+b2*y_0+c2<0, a3*x_0+b3*y_0+c3<0]):
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if all([a1*x_0+b1*y_0+c1 <0, a2*x_0+b2*y_0+c2<0, a3*x_0+b3*y_0+c3<0]):
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if all([dau1=="<", dau2=="<", dau3=="<"]):
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if all([a1*x_0+b1*y_0+c1 >0, a2*x_0+b2*y_0+c2<0, a3*x_0+b3*y_0+c3<0]):
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if all([a1*x_0+b1*y_0+c1 >0, a2*x_0+b2*y_0+c2>0, a3*x_0+b3*y_0+c3>0]):
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    
    random.shuffle(lst_nghiem)

    return lst_nghiem

def mien_not_nghiem_HeBPT_2an(a1,b1,c1,dau1,a2,b2,c2,dau2):
      

    lst_nghiem=[]

    if dau1==">" and dau2==">":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 >0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 <0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if dau1==">" and dau2=="<":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 <0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 <0 and a2*x_0+b2*y_0+c2>0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if dau1=="<" and dau2==">":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 <0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 >0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))

    if dau1=="<" and dau2=="<":
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 >0 and a2*x_0+b2*y_0+c2<0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
        for x_0 in range(-10,10):
            for y_0 in range(-10,10):
                if a1*x_0+b1*y_0+c1 >0 and a2*x_0+b2*y_0+c2>0:
                    lst_nghiem.append(f"{(x_0,y_0)}".replace(",",";"))
    
    random.shuffle(lst_nghiem)

    return lst_nghiem


##-----------------------------------------------------------------------##

#[D10_C2_B1_01] Tìm cặp số là nghiệm của BPT ax+by+c>0,>=0.
def bch_12_L10_C2_B1_01():
    #Tạo bậc ngẫu nhiên
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])    
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    x, y = symbols('x y')
    f=a*x+b*y+c
    dau=random.choice([">","\\ge" ])
    noi_dung= f"Cặp số nào sau đây là nghiệm của bất phương trình ${latex(f)} {dau} 0$."
    cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]
    kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,">")[0:3]

    kq=f"${cap_nghiem}$"
    kq2=f"${kq2}$"
    kq3=f"${kq3}$"
    kq4=f"${kq4}$"
    

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án      

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f"Thay các cặp số của các phương án vào ta thấy {kq} thỏa mãn."

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

#[D10_C2_B1_02] Tìm cặp số là nghiệm của BPT ax+by+c<0,<=0.
def bch_12_L10_C2_B1_02():
    #Tạo bậc ngẫu nhiên
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b = random.choice([random.randint(-10, -1), random.randint(1, 10)])    
    c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    x, y = symbols('x y')

    f=a*x+b*y+c   
    cap_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]
    kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,"<")[0:3]
    dau=random.choice(["<", "\\le"])
    noi_dung= f"Cặp số nào sau đây là nghiệm của bất phương trình ${latex(f)} {dau} 0$.\n"

    kq=f"${cap_nghiem}$"
    kq2=f"${kq2}$"
    kq3=f"${kq3}$"
    kq4=f"${kq4}$"

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f"Thay các cặp số của các phương án vào ta thấy {kq} thỏa mãn."
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

#[D10_C2_B1_03]-M1. Nhận dạng bất phương trình bậc nhất 2 ẩn
def bch_12_L10_C2_B1_03():
    noi_dung=f"Bất phương trình nào sau đây là bất phương trình bậc nhất hai ẩn" 

    a = random.choice([i for i in range(-10, 10) if i!=0])
    b = random.choice([i for i in range(-10, 10) if i!=0])
    c = random.choice([i for i in range(-10, 10) ])

    x,y=sp.symbols("x y")

    chon=random.randint(1,2)
    if chon==1:
        kq=f"${latex(a*x+b*y+c)}{random.choice([">","<","\\le","\\ge"])} 0$"    
    if chon==2:
        kq=f"${latex(a*x+b*y)}{random.choice([">","<","\\le","\\ge"])} {c}$"

    a = random.choice([i for i in range(-10, 10) if i!=0])
    b = random.choice([i for i in range(-10, 10) if i!=0])
    c = random.choice([i for i in range(-10, 10) ])  
    
    kq2=f"${latex(a*x**2+b*y+c)} {random.choice([">","<","\\le","\\ge"])} 0$"

    a = random.choice([i for i in range(-10, 10) if i!=0])
    b = random.choice([i for i in range(-10, 10) if i!=0])
    c = random.choice([i for i in range(-10, 10) ])
    kq3=f"${latex(a*x**2+b*y**2)} {random.choice([">","<","\\le","\\ge"])} {c}$"

    a = random.choice([i for i in range(-10, 10) if i!=0])
    b = random.choice([i for i in range(-10, 10) if i!=0])
    c = random.choice([i for i in range(-10, 10) ])
    kq4=f"${latex(a/x+b/y+c)} {random.choice([">","<","\\le","\\ge"])} 0$"

    noi_dung_loigiai=f"{kq} là bất phương trình bậc nhất 2 ẩn."

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C2_B1_04]-M2. Xác định miền nghiệm của ax+by+c>0 (<0) là nửa mặt phẳng chứa điểm nào
def bch_12_L10_C2_B1_04():
    a = random.choice([i for i in range(-5, 5) if i!=0])
    b = random.choice([i for i in range(1, 5) if i!=0])
    c = random.choice([i for i in range(-7, 10) ])

    x,y=sp.symbols("x y")
    f=a*x+b*y+c
    chon=random.randint(1,2)
    
    if chon==1:
        noi_dung=random.choice([
        f"Miền nghiệm của bất phương trình ${latex(f)}{random.choice([">","\\ge"])} 0$ là nửa mặt phẳng chứa điểm nào",
        f"Miền nghiệm của bất phương trình ${latex(a*x+b*y)}{random.choice([">","\\ge"])} {-c}$ là nửa mặt phẳng chứa điểm nào"
        ])
        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]
        kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,">")[0:3]             
    
    if chon==2:
        noi_dung=random.choice([
        f"Miền nghiệm của bất phương trình ${latex(f)}{random.choice(["<","\\le"])} 0$ là nửa mặt phẳng chứa điểm nào trong các điểm sau?",
        f"Miền nghiệm của bất phương trình ${latex(a*x+b*y)}{random.choice(["<","\\le"])} {-c}$ là nửa mặt phẳng chứa điểm nào trong các điểm sau?"
        ])
        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]
        kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,"<")[0:3]
        
    kq=f"${cap_nghiem}$"
    kq2=f"${kq2}$"
    kq3=f"${kq3}$"
    kq4=f"${kq4}$"   

    noi_dung_loigiai=f"Thay {kq} vào bất phương trình thấy thỏa mãn nên miền nghiệm là nửa mặt phẳng chứa điểm {kq}."

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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C2_B1_05]-M2. Xác định miền nghiệm của ax+by+c >(<) ex+fy+g  là nửa mặt phẳng chứa điểm nào
def bch_12_L10_C2_B1_05():
    a = random.choice([i for i in range(-5, 5) if i!=0])
    b = random.choice([i for i in range(1, 5) if i!=0])
    c = random.choice([i for i in range(-7, 10) ])
    d = random.choice([i for i in range(-5, 5) if i!=0])
    e = random.choice([i for i in range(1, 5) if i!=0])
    h = random.choice([i for i in range(-7, 10) ])


    x,y=sp.symbols("x y")
    f=a*x+b*y+c
    chon=random.randint(1,2)
    
    if chon==1:
        noi_dung=random.choice([
        f"Miền nghiệm của bất phương trình ${latex(f+d*x+e*y+h)}{random.choice([">","\\ge"])} {latex(d*x+e*y+h)}$ là nửa mặt phẳng chứa điểm nào",
        f"Miền nghiệm của bất phương trình ${latex(f+d*x+e*y+h)}{random.choice([">","\\ge"])} {latex(d*x+e*y+h)}$ là nửa mặt phẳng chứa điểm nào"
        ])
        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]
        kq2,kq3,kq4=mien_nghiem_BPT_2an(a,b,c,"<")[0:3]
    
    if chon==2:
        noi_dung=random.choice([
        f"Miền nghiệm của bất phương trình ${latex(f+d*x+e*y+h)}{random.choice(["<","\\le"])} {latex(d*x+e*y+h)}$ là nửa mặt phẳng chứa điểm nào trong các điểm sau?",
        f"Miền nghiệm của bất phương trình ${latex(f+d*x+e*y+h)}{random.choice([">","\\ge"])} {latex(d*x+e*y+h)}$ là nửa mặt phẳng chứa điểm nào trong các điểm sau?"
        ])
        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]
        kq2,kq3,kq4=mien_nghiem_BPT_2an(a,b,c,">")[0:3]

    kq=f"${cap_nghiem}$"       
    kq2=f"${kq2}$"       
    kq3=f"${kq3}$"        
    kq4=f"${kq4}$"

    noi_dung_loigiai=(
        f"Thay {kq} vào bất phương trình thấy thỏa mãn nên miền nghiệm là nửa mặt phẳng chứa điểm {kq}.")
    
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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C2_B1_06]-M2. Cặp số nào là nghiệm thuộc nửa mặt phẳng có hình vẽ minh họa.
def bch_12_L10_C2_B1_06():
    x,y=sp.symbols("x y")    
    chon=random.randint(1,2)    
    noi_dung=(f"Cặp số $(x;y)$ nào sau đây là nghiệm của bất phương trình có miền nghiệm là"
                    f" nửa mặt phẳng không bị gạch có bờ là đường thẳng $d$ như hình bên?")
    
    if chon==1:
        #ax+by+c>0
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(1, 4) if i!=0])
        c = random.choice([i for i in range(-3, 4) if i!=0])

        code_hinh=code_latex_mien_nghiem(a,b,c,">0")
        code = my_module.moi_truong_anh_latex(code_hinh)
        file_name=my_module.pdftoimage_timename(code)

        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]
        kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,">")[0:3]

    if chon==2:
        #ax+by+c<0:
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(1, 4) if i!=0])
        c = random.choice([i for i in range(-3, 4) if i!=0])
        print(a,b,c)

        code_hinh=code_latex_mien_nghiem(a,b,c,"<0")
        code = my_module.moi_truong_anh_latex(code_hinh)
        file_name=my_module.pdftoimage_timename(code)

        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]
        kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,"<")[0:3]

    kq=f"${cap_nghiem}$"       
    kq2=f"${kq2}$"       
    kq3=f"${kq3}$"        
    kq4=f"${kq4}$"
    

    noi_dung_loigiai=f"Dựa vào hình vẽ ta thấy {kq} thuộc miền nghiệm nên {kq} là nghiệm của bất phương trình."

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C2_B1_07]-M2. Tìm miền nghiệm của bất phương trình ax+by+c>0 (<0)
def bch_12_L10_C2_B1_07():
    x,y=sp.symbols("x y")
    a = random.choice([i for i in range(-3, 3) if i!=0])
    b = random.choice([i for i in range(1, 4) if i!=0])
    c = random.choice([i for i in range(-3, 4) if i!=0])
    f=a*x+b*y+c
    noi_dung=(f"Phần không bị gạch trong hình vẽ nào sau đây (không kể đường thẳng ${{d}}$) là "
f"miền nghiệm của bất phương trình ${latex(f)}>0$?")
    
    code_hinh=code_latex_mien_nghiem(a,b,c,">0")
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    kq=f"{file_name}\n"

    code_hinh_2=code_latex_mien_nghiem(a,b,c,"<0")
    code = my_module.moi_truong_anh_latex(code_hinh_2)
    file_name_2=my_module.pdftoimage_timename(code)
    kq2=f"{file_name_2}\n"

    code_hinh_3=code_latex_mien_nghiem(a,-b,c,">0")
    code = my_module.moi_truong_anh_latex(code_hinh_3)
    file_name_3=my_module.pdftoimage_timename(code)
    kq3=f"{file_name_3}\n"

    code_hinh_4=code_latex_mien_nghiem(-a,b,c,"<0")
    code = my_module.moi_truong_anh_latex(code_hinh_4)
    file_name_4=my_module.pdftoimage_timename(code)
    kq4=f"{file_name_4}\n"

    noi_dung_loigiai=f"Xét đường thẳng $d:{latex(f)}=0$. Ta có ${{d}}$ đi qua các điểm $(0;{phan_so(-c/b)})$ và $({phan_so(-c/a)};0)$.\n\n"
    if c>0:
        noi_dung_loigiai+=f"Điểm $O(0;0)$ thỏa mãn bất phương trình nên miền nghiệm là nửa mặt phẳng chứa điểm ${{O}}$."
    else:
        noi_dung_loigiai+=f"Điểm $O(0;0)$ không thỏa mãn bất phương trình nên miền nghiệm là nửa mặt phẳng không chứa điểm ${{O}}$."

    pa_A= f"*\n{kq}"
    pa_B= f"\n{kq2}"
    pa_C= f"\n{kq3}"
    pa_D= f"\n{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    list_PA =[f"* {code_hinh}", code_hinh_2, code_hinh_3, code_hinh_4]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

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

#[D10_C2_B1_08]-TF-M2. Cho BPT ax+by+c>0 (<0). Xét Đ-S: nghiệm, không là nghiệm, nghiệm chứa bờ, miền nghiệm
def bch_12_L10_C2_B1_08():
    x,y=sp.symbols("x y")    
    chon=random.randint(1,4)

    if chon==1:
        #ax+by+c>0
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(1, 4) if i!=0])
        c = random.choice([i for i in range(-3, 4) if i!=0])
        f=a*x+b*y+c   

        noi_dung = f"Xét bất phương trình ${latex(f)}>0$. Xét tính đúng-sai của các khẳng định sau. "        
        debai_word= f"{noi_dung}\n"

        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]        
        
        kq1_T=f"*Cặp số ${cap_nghiem}$ là một nghiệm của bất phương trình." 
        kq1_F=f"Cặp số ${cap_nghiem}$ không là nghiệm của bất phương trình "
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Thay ${cap_nghiem}$ vào bất phương trình thấy thỏa mãn nên ${cap_nghiem}$ là một nghiệm của bất phương trình."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        not_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]  

        kq2_T=f"*Cặp số ${not_nghiem}$ không là nghiệm của bất phương trình."
        kq2_F=f"Cặp số ${not_nghiem}$ là nghiệm của bất phương trình "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Thay ${not_nghiem}$ vào bất phương trình thấy không thỏa mãn nên ${not_nghiem}$ không là nghiệm của bất phương trình."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*Miền nghiệm không chứa đường thẳng $d:{latex(f)}=0$" 
        kq3_F=f"Miền nghiệm chứa đường thẳng $d:{latex(f)}=0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Bất phương trình ${latex(f)}>0$ có miền nghiệm không chứa đường thẳng ${latex(f)}=0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*Miền nghiệm là nửa mặt phẳng chứa điểm ${cap_nghiem}$ và không chứa đường thẳng $d:{latex(f)}=0$"
        kq4_F=random.choice([f"Miền nghiệm là nửa mặt phẳng không chứa điểm ${cap_nghiem}$ và không chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng chứa điểm ${cap_nghiem}$ và chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng không chứa điểm ${cap_nghiem}$ và không chứa đường thẳng $d:{latex(f)}=0$"
            ])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Miền nghiệm là nửa mặt phẳng chứa điểm ${cap_nghiem}$ và không chứa đường thẳng $d:{latex(f)}=0$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon==2:
        #ax+by+c>=0
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(1, 4) if i!=0])
        c = random.choice([i for i in range(-3, 4) if i!=0])
        f=a*x+b*y+c   

        noi_dung = f"Xét bất phương trình ${latex(f)}\\ge 0$. Xét tính đúng-sai của các khẳng định sau. "        
        debai_word= f"{noi_dung}\n"

        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]    
        
        kq1_T=f"*Cặp số ${cap_nghiem}$ là một nghiệm của bất phương trình." 
        kq1_F=f"Cặp số ${cap_nghiem}$ không là nghiệm của bất phương trình "
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Thay ${cap_nghiem}$ vào bất phương trình thấy thỏa mãn nên ${cap_nghiem}$ là một nghiệm của bất phương trình."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        not_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]

        kq2_T=f"*Cặp số ${not_nghiem}$ không là nghiệm của bất phương trình."
        kq2_F=f"Cặp số ${not_nghiem}$ là nghiệm của bất phương trình "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Thay ${not_nghiem}$ vào bất phương trình thấy không thỏa mãn nên ${not_nghiem}$ không là nghiệm của bất phương trình."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*Miền nghiệm của bất phương trình chứa đường thẳng $d:{latex(f)}=0$" 
        kq3_F=f"Miền nghiệm của bất phương trình không chứa đường thẳng $d:{latex(f)}=0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Bất phương trình ${latex(f)}>0$ có miền nghiệm chứa đường thẳng $d:{latex(f)}=0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*Miền nghiệm là nửa mặt phẳng chứa điểm ${cap_nghiem}$ và chứa đường thẳng $d:{latex(f)}=0$"
        kq4_F=random.choice([f"Miền nghiệm là nửa mặt phẳng không chứa điểm ${cap_nghiem}$ và chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng chứa điểm ${cap_nghiem}$ và không chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng không chứa điểm ${cap_nghiem}$ và không chứa đường thẳng $d:{latex(f)}=0$"
            ])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Miền nghiệm là nửa mặt phẳng chứa điểm ${cap_nghiem}$ và chứa đường thẳng $d:{latex(f)}=0$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon==3:
        #ax+by+c<0
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(1, 4) if i!=0])
        c = random.choice([i for i in range(-3, 4) if i!=0])
        f=a*x+b*y+c 
        x_0=random.randint(-3,3)
        y_0=int((-a*x_0-c)/b) - random.randint(1,2)  

        noi_dung = f"Xét bất phương trình ${latex(f)}<0$. Xét tính đúng-sai của các khẳng định sau. "        
        debai_word= f"{noi_dung}\n"

        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]        
        
        kq1_T=f"*Cặp số ${cap_nghiem}$ là một nghiệm của bất phương trình." 
        kq1_F=f"Cặp số ${cap_nghiem}$ không là nghiệm của bất phương trình "
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Thay ${cap_nghiem}$ vào bất phương trình thấy thỏa mãn nên ${cap_nghiem}$ là một nghiệm của bất phương trình."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]

        kq2_T=f"*Cặp số ${cap_nghiem}$ không là nghiệm của bất phương trình."
        kq2_F=f"Cặp số ${cap_nghiem}$ là nghiệm của bất phương trình "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Thay ${cap_nghiem}$ vào bất phương trình thấy không thỏa mãn nên ${cap_nghiem}$ không là nghiệm của bất phương trình."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*Miền nghiệm của bất phương trình không chứa đường thẳng $d:{latex(f)}=0$" 
        kq3_F=f"Miền nghiệm của bất phương trình chứa đường thẳng $d:{latex(f)}=0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Bất phương trình ${latex(f)}<0$ có miền nghiệm không chứa đường thẳng ${latex(f)}=0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$"
        kq4_F=random.choice([f"Miền nghiệm là nửa mặt phẳng không chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và chứa đường thẳng $d:{latex(f)}=0$",
            ])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon==4:
        #ax+by+c<=0
        a = random.choice([i for i in range(-3, 3) if i!=0])
        b = random.choice([i for i in range(1, 4) if i!=0])
        c = random.choice([i for i in range(-3, 4) if i!=0])
        f=a*x+b*y+c   

        noi_dung = f"Xét bất phương trình ${latex(f)}\\le 0$. Xét tính đúng-sai của các khẳng định sau. "        
        debai_word= f"{noi_dung}\n"

        x_0=random.randint(-3,3)
        y_0=int((-a*x_0-c)/b) - random.randint(1,2)           
        
        kq1_T=f"*Cặp số $({x_0};{y_0})$ là một nghiệm của bất phương trình." 
        kq1_F=f"Cặp số $({x_0};{y_0})$ không là nghiệm của bất phương trình "
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Thay $({x_0};{y_0})$ vào bất phương trình thấy thỏa mãn nên $({x_0};{y_0})$ là một nghiệm của bất phương trình."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        x_1=random.randint(-3,3)
        y_1=int((-a*x_1-c)/b) + random.randint(1,3)

        kq2_T=f"*Cặp số $({x_1};{y_1})$ không là nghiệm của bất phương trình."
        kq2_F=f"Cặp số $({x_1};{y_1})$ là nghiệm của bất phương trình "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Thay $({x_1};{y_1})$ vào bất phương trình thấy không thỏa mãn nên $({x_1};{y_1})$ không là nghiệm của bất phương trình."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*Miền nghiệm của bất phương trình chứa đường thẳng $d:{latex(f)}=0$" 
        kq3_F=f"Miền nghiệm của bất phương trình khôngchứa đường thẳng $d:{latex(f)}=0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Bất phương trình ${latex(f)}<0$ có miền nghiệm chứa đường thẳng ${latex(f)}=0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và chứa đường thẳng $d:{latex(f)}=0$"
        kq4_F=random.choice([f"Miền nghiệm là nửa mặt phẳng không chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng không chứa điểm $({x_1};{y_1})$ và không chứa đường thẳng $d:{latex(f)}=0$"
            ])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và chứa đường thẳng $d:{latex(f)}=0$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

    return debai,debai_latex,loigiai_word,dap_an

#[D10_C2_B1_09]-M2. Lập BPT bậc nhất 2 ẩn từ bài toán thực tế
def bch_12_L10_C2_B1_09():
    x,y=sp.symbols("x y")
    ten=random.choice(["Minh", "Nga", "Lan", "Kiên", "Phương"]) 
    chon=random.randint(1,2)
    
    if chon==1:
        vat_1="cuốn vở"
        vat_2="bút bi"

        tien=random.choice([10*i for i in range (5,12)])
        a=random.randint(5,10)
        b=random.randint(9,20)

        noi_dung=(f"Bạn {ten} có {tien} nghìn đồng để mua {vat_1} và {vat_2}."
    f" {ten} mua ${{x}}$ {vat_1} với giá {a} nghìn đồng một {vat_1} và mua ${{y}}$ {vat_2} với giá {b} nghìn đồng một cái {vat_2}."
    f" Bất phương trình nào sau đây mô tả điều kiện ràng buộc đối với ${{x}}$ và ${{y}}$.")
    
    if chon==2:
        tien=random.choice([10*i for i in range (5,12)])
        a=random.randint(5,10)
        b=random.randint(10,15)
        vat_1="bánh bao"
        vat_2="mì ly"
        noi_dung=(f"Bạn {ten} có {tien} nghìn đồng để mua {vat_1} và {vat_2}."
    f" {ten} mua ${{x}}$ cái {vat_1} với giá {a} nghìn đồng một cái {vat_1} và mua ${{y}}$ hộp {vat_2} với giá {b} nghìn đồng một hộp {vat_2}."
    f" Bất phương trình nào sau đây mô tả điều kiện ràng buộc đối với ${{x}}$ và ${{y}}$.")

    if chon==3:
        so_kg=random.choice([10*i for i in range (40,80)])
        a=random.choice([5*i for i in range (6,15)])
        b=random.choice([5*i for i in range (6,15)])
        vat_1="kem dưa hấu"
        vat_2="kem ốc quế"
        noi_dung=(f"một doanh nghiệp muốn sản xuất 2 loại bánh, bánh X và bánh Y."
    f" Lượng đường cần cho mỗi loại là {a}g và {b}g. Doanh nghiệp đã nhập về {so_kg}kg đường"
    f" Bất phương trình nào sau đây mô tả điều kiện ràng buộc đối với ${{x}}$ và ${{y}}$.")
    
    ucln=gcd(a,b)
    ucln=gcd(ucln,tien)
    a1,b1,tien1=int(a/ucln),int(b/ucln), int(tien/ucln) 
   

    kq=f"${latex(a1*x+b1*y)}\\le {tien1}$"
    kq2=f"${latex(a1*x+b1*y)}< {tien1}$"
    kq3=f"${latex(a1*x+b1*y)}> {tien1}$"
    kq4=f"${latex(a1*x+b1*y)}\\ge {tien1}$"

    noi_dung_loigiai=(f"Số tiền để mua {vat_1} và {vat_2} là ${latex(a*x+b*y)}\\le {tien}$.\n\n"
        f"Điều kiện ràng buộc đối với ${{x}}$ và ${{y}}$ là: ${latex(a1*x+b1*y)}\\le {tien1}$."
        )
    
    if chon==4:

        so_kg=random.choice([10*i for i in range (40,80)])
        a=random.choice([5*i for i in range (6,15)])
        b=random.choice([5*i for i in range (8,20)])

        ucln=gcd(a,b)
        ucln=gcd(ucln,so_kg)
        a1,b1,so_kg1=int(a/ucln),int(b/ucln), int(so_kg/ucln)
        a1,b1=f"{round(a/1000,2):.2f}".replace(".",","), f"{round(b/1000,2):.2f}".replace(".",",")

        noi_dung=(f"Một doanh nghiệp muốn sản xuất 2 loại bánh gồm bánh X và bánh Y."
    f" Lượng đường cần cho mỗi loại là {a}g và {b}g. Doanh nghiệp đã nhập về {so_kg}kg đường."
    f" Gọi ${{x}}$ số bánh X và ${{x}}$ là số bánh Y."
    f" Hỏi ${{x,y}}$ phải thỏa mãn điều kiện gì để lượng đường sản suất không vượt quá lượng đường đã nhập về?")

        noi_dung_loigiai=(f"Theo bài ra ta có bất phương trình là ${a1}x+{b1}y\\le {so_kg1}$.\n\n"        
        )
        kq=f"${a1}x+{b1}y\\le {so_kg1}$"
        kq2=f"${a}x+{b}y< {so_kg1}$"
        kq3=f"${a}x+{b}y> {so_kg}$"
        kq4=f"${a1}x+{b1}y\\ge {so_kg1}$"


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


#---------------------------->
#Bài 2 - HỆ BẤT PHƯƠNG TRÌNH

#[D10_C2_B2_01]-M2. Cho Hệ BPT ax+by+c>0 (<0). Tìm cặp số là nghiệm của hệ.
def bch_12_L10_C2_B2_01():
    x,y=sp.symbols("x y")
    a1 = random.choice([i for i in range(-4, 4) if i!=0])
    b1 = random.choice([i for i in range(1, 4) if i!=0])
    c1 = random.choice([i for i in range(-5, 5) if i!=0])
    f1=a1*x+b1*y+c1

    a2 = random.choice([i for i in range(-4, 4) if i!=0])
    b2 = random.choice([i for i in range(1, 4) if i!=0])
    c2 = random.choice([i for i in range(-5, 5) if i!=0])
    if a1==a2: a2=a1+1
    if a2==0: a2=1  
    f2=a2*x+b2*y+c2
    chon=random.randint(1,2)
    
    if chon==1:
        dau=random.choice([">","\\ge"])
        chon=random.randint(1,2)
        if chon==1:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
            {latex(f1)} {dau} 0\\\\ \
            {latex(-a2*x-b2*y-c2)} {random.choice(["<","\\le"])} 0\
            \\end{{array}} \\right."
        
        if chon==2:
        
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
            {latex(f1)} {dau} 0\\\\ \
            {latex(f2)} {dau} 0\
            \\end{{array}} \\right."

        noi_dung=f"Cặp số nào sau đây là nghiệm của hệ bất phương trình ${f}$?"
        cap_nghiem=mien_nghiem_HeBPT_2an(a1,b1,c1,">",a2,b2,c2,">")[0]
        kq2,kq3,kq4=mien_not_nghiem_HeBPT_2an(a1,b1,c1,">",a2,b2,c2,">")[0:3]

        
    
    if chon==2:
        dau=random.choice(["<","\\le"])
        chon=random.randint(1,2)
        if chon==1:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(f2)} {dau} 0\
        \\end{{array}} \\right."
        
        if chon==2:
        
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
            {latex(a1*x+b1*y+c1)} {dau} 0\\\\ \
            {latex(-a2*x-b2*y-c2)} {random.choice([">","\\ge"])} 0\
            \\end{{array}} \\right."

        cap_nghiem=mien_nghiem_HeBPT_2an(a1,b1,c1,"<",a2,b2,c2,"<")[0]
        kq2,kq3,kq4=mien_not_nghiem_HeBPT_2an(a1,b1,c1,"<",a2,b2,c2,"<")[0:3]

        noi_dung=f"Cặp số nào sau đây là nghiệm của hệ bất phương trình ${f}$?"
    
    kq=f"${cap_nghiem}$"
    kq2=f"${kq2}$"
    kq3=f"${kq3}$"
    kq4=f"${kq4}$"
    

    noi_dung_loigiai=f"Thay các cặp số lần lượt và các bất phương trình ta thấy cặp {kq} thỏa mãn cả hai bất phương trình đã cho."

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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C2_B2_02]-M2. Cho Hệ BPT ax+by+c>0 (<0). Tìm cặp số là không nghiệm của hệ.
def bch_12_L10_C2_B2_02():
    x,y=sp.symbols("x y")
    a1 = random.choice([i for i in range(-3, 2) if i!=0])
    b1 = random.choice([i for i in range(1, 3) if i!=0])
    c1 = random.choice([i for i in range(-4, 4) if i!=0])
    f1=a1*x+b1*y+c1

    a2 = random.choice([i for i in range(-3, 2) if i!=0])
    b2 = random.choice([i for i in range(1, 3) if i!=0])
    c2 = random.choice([i for i in range(-4, 4) if i!=0])
    if a1==a2: a2=a1+1
    if a2==0: a2=1  
    f2=a2*x+b2*y+c2
    chon=random.randint(1,2)
    
    if chon==1:
        dau=random.choice([">","\\ge"])
        chon=random.randint(1,2)
        if chon==1:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(f2)} {dau} 0\
        \\end{{array}} \\right."
        
        if chon==2:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(-a2*x-b2*y-c2)} {random.choice(["<","\\le"])} 0\
        \\end{{array}} \\right."      
        
        noi_dung=f"Cặp số nào sau đây không là nghiệm của hệ bất phương trình ${f}$?"

        cap_nghiem=mien_not_nghiem_HeBPT_2an(a1,b1,c1,">",a2,b2,c2,">")[0]
        kq2,kq3,kq4=mien_nghiem_HeBPT_2an(a1,b1,c1,">",a2,b2,c2,">")[0:3]
    
    if chon==2:
        dau=random.choice(["<","\\le"])
        chon=random.randint(1,2)
        if chon==1:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(f2)} {dau} 0\
        \\end{{array}} \\right."
        
        if chon==2:
        
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(-a2*x-b2*y-c2)} {random.choice([">","\\ge"])} 0\
        \\end{{array}} \\right."

        noi_dung=f"Cặp số nào sau đây không là nghiệm của hệ bất phương trình ${f}$?"
        cap_nghiem=mien_not_nghiem_HeBPT_2an(a1,b1,c1,"<",a2,b2,c2,"<")[0]
        kq2,kq3,kq4=mien_nghiem_HeBPT_2an(a1,b1,c1,"<",a2,b2,c2,"<")[0:3]

    kq=f"${cap_nghiem}$"
    kq2=f"${kq2}$"
    kq3=f"${kq3}$"
    kq4=f"${kq4}$"

    noi_dung_loigiai=f"Thay các cặp số lần lượt và các bất phương trình ta thấy cặp {kq} không thỏa mãn cả hai bất phương trình đã cho."

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

#[D10_C2_B2_03]-M2. Cho Hệ 3 BPT ax+by+c>0 (<0). Tìm cặp số là nghiệm của hệ.
def bch_12_L10_C2_B2_03():
    x,y=sp.symbols("x y")

    chon=random.randint(1,2)
    
    if chon==1:
        a1 = random.choice([i for i in range(-4, 4) if i!=0])
        b1 = random.choice([i for i in range(1, 4) if i!=0])
        c1 = random.choice([i for i in range(-5, 5) if i!=0])
        f1=a1*x+b1*y+c1

        a2 = random.choice([i for i in range(-4, 4) if i!=0])
        b2 = random.choice([i for i in range(1, 4) if i!=0])
        c2 = random.choice([i for i in range(-5, 5) if i!=0])
        if a1==a2: a2=a1+1
        if a2==0: a2=1  
        f2=a2*x+b2*y+c2
        chon=random.randint(1,2)
        if chon==1:
            a3 = 0
            b3 = random.choice([i for i in range(1, 4) if i!=0])
            c3 = random.choice([i for i in range(-2, 5) if i!=0])
        
        if chon==2:
            a3 = random.choice([i for i in range(1, 4) if i!=0])
            b3 = 0
            c3 = random.choice([i for i in range(-2, 5) if i!=0])
        
        f3=a3*x+b3*y+c3

    
        dau=random.choice([">","\\ge"])
        chon=random.randint(1,2)
        if chon==1:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(f2)} {dau} 0\\\\ \
        {latex(f3)} {dau} 0\
        \\end{{array}} \\right."
        
        if chon==2:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(-a2*x-b2*y-c2)} {random.choice(["<","\\le"])} 0\\\\ \
        {latex(f3)} {dau} 0\
        \\end{{array}} \\right."  
 
        cap_nghiem=mien_nghiem_He3BPT_2an(a1,b1,c1,">",a2,b2,c2,">", a3,b3,c3,">")[0]
        kq2,kq3,kq4=mien_not_nghiem_HeBPT_2an(a1,b1,c1,">",a2,b2,c2,">")[0:3]
      
    
    if chon==2:
        a1 = random.choice([i for i in range(-4, 4) if i!=0])
        b1 = random.choice([i for i in range(1, 4) if i!=0])
        c1 = random.choice([i for i in range(-5, 5) if i!=0])
        f1=a1*x+b1*y+c1

        a2 = random.choice([i for i in range(-4, 4) if i!=0])
        b2 = random.choice([i for i in range(1, 4) if i!=0])
        c2 = random.choice([i for i in range(-5, 5) if i!=0])
        if a1==a2: a2=a1+1
        if a2==0: a2=1  
        f2=a2*x+b2*y+c2
        chon=random.randint(1,2)
        if chon==1:
            a3 = 0
            b3 = random.choice([i for i in range(-4, 4) if i!=0])
            c3 = random.choice([i for i in range(-5, 5) if i!=0])
        
        if chon==2:
            a3 = random.choice([i for i in range(-5, 5) if i!=0])
            b3 = 0
            c3 = random.choice([i for i in range(-5, 5) if i!=0])
        
        f3=a3*x+b3*y+c3
        dau=random.choice(["<","\\le"])
        chon=random.randint(1,2)
        if chon==1:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(f2)} {dau} 0\\\\ \
        {latex(f3)} {dau} 0\
        \\end{{array}} \\right."
        
        if chon==2:
            f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(-a2*x-b2*y-c2)} {random.choice([">","\\ge"])} 0\\\\ \
        {latex(f3)} {dau} 0\
        \\end{{array}} \\right."

        cap_nghiem=mien_nghiem_He3BPT_2an(a1,b1,c1,"<",a2,b2,c2,"<", a3,b3,c3,"<")[0]
        kq2,kq3,kq4=mien_not_nghiem_HeBPT_2an(a1,b1,c1,"<",a2,b2,c2,"<")[0:3]  
        

    noi_dung=f"Cặp số nào sau đây là nghiệm của hệ bất phương trình ${f}$?"

    kq=f"${cap_nghiem}$"
    kq2=f"${kq2}$"
    kq3=f"${kq3}$"
    kq4=f"${kq4}$"  
    
    noi_dung_loigiai=f"Thay các cặp số lần lượt và các bất phương trình ta thấy cặp {kq} thỏa mãn cả ba bất phương trình đã cho."

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung} \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C2_B2_04]-TF-M2. Cho hệ 2 BPT. Xét đúng sai về nghiệm của hệ.
def bch_12_L10_C2_B2_04():
    x,y=sp.symbols("x y")
    a1 = random.choice([i for i in range(-4, 4) if i!=0])
    b1 = random.choice([i for i in range(1, 4) if i!=0])
    c1 = random.choice([i for i in range(-5, 5) if i!=0])
    f1=a1*x+b1*y+c1

    a2 = random.choice([i for i in range(-4, 4) if i!=0])
    b2 = random.choice([i for i in range(1, 4) if i!=0])
    c2 = random.choice([i for i in range(-5, 5) if i!=0])
    if a1==a2: a2=a1+1
    if a2==0: a2=1  
    f2=a2*x+b2*y+c2   

    dau=random.choice([">","\\ge"])
    chon=random.randint(1,2)
    if chon==1:
        f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(-a2*x-b2*y-c2)} {random.choice(["<","\\le"])} 0\
        \\end{{array}} \\right."
    
    if chon==2:
    
        f=f"\\left\\{{ \\begin{{array}}{{l}}\
        {latex(f1)} {dau} 0\\\\ \
        {latex(f2)} {dau} 0\
        \\end{{array}} \\right." 

    noi_dung = f"Cho hệ bất phương trình ${f}$. Xét tính đúng-sai của các khẳng định sau."        
    debai_word= f"{noi_dung}\n"

    x_0=random.randint(-5,-3)
    y_1=int((-a1*x_0-c1)/b1) + random.randint(1,3)
    y_2=int((-a2*x_0-c2)/b2) + random.randint(1,3)
    y_0=max(y_1,y_2)
    
    kq1_T=f"*$({x_0};{y_0})$ là một nghiệm của hệ bất phương trình" 
    kq1_F=f"$({x_0};{y_0})$ không là một nghiệm của hệ bất phương trình"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Thay $({x_0};{y_0})$ vào thấy thỏa mãn nên $({x_0};{y_0})$ là một nghiệm của hệ bất phương trình."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_2=random.randint(-2,0)
    y_2=int((-a1*x_2-c1)/b1) - random.randint(1,3)
    kq2_T=f"*$({x_2};{y_2})$ không là nghiệm của hệ bất phương trình"
    kq2_F=f"$({x_2};{y_2})$ là một nghiệm của hệ bất phương trình "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Thay $({x_2};{y_2})$ vào thấy không thỏa mãn nên $({x_2};{y_2})$ không là nghiệm của hệ bất phương trình."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_3=random.randint(1,3)
    y_1=int((-a1*x_3-c1)/b1) + random.randint(1,3)
    y_2=int((-a2*x_3-c2)/b2) + random.randint(1,3)
    y_3=max(y_1,y_2)

    kq3_T=f"*$({x_3};{y_3})$ là một nghiệm của hệ bất phương trình" 
    kq3_F=f"$({x_3};{y_3})$ không là nghiệm của hệ bất phương trình"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"Thay $({x_3};{y_3})$  vào thấy thỏa mãn nên $({x_3};{y_3})$ là một nghiệm của hệ bất phương trình."
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    x_4=random.randint(4,6)
    y_4=int((-a2*x_4-c2)/b2) - random.randint(1,3)    

    kq4_T=f"*$({x_4};{y_4})$ không là nghiệm của hệ bất phương trình"
    kq4_F=f"$({x_4};{y_4})$ là một nghiệm của hệ bất phương trình" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"Thay $({x_4};{y_4})$ vào thấy thỏa mãn nên $({x_4};{y_4})$ là một nghiệm của hệ bất phương trình."
    loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq4==kq4_F:
        loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    #random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

    return debai,debai_latex,loigiai_word,dap_an

#[D10_C2_B2_05]-SA-M3. Toán thực tế ứng dụng bpt bậc nhất 2 ẩn
def bch_12_L10_C2_B2_05():
    a1=random.randint(1,5)
    a2=random.choice([i for i in range(1,5) if i!=a1])
    x0=random.randint(1,5)
    y0=random.randint(1,5) 
    b1=random.randint(1,5)
    b2=random.choice([i for i in range(1,5) if i!=a1])
    if a1*b2==a2*b1: a1=a1+1
    c1=a1*x0+b1*y0
    c2=a2*x0+b2*y0
    a3=random.randint(5,20)
    if (c1/a1) < (c2/a2):
        b3_min = max(int((((c1/a1) - x0) / (y0/a3))), 1)  # Đảm bảo b3 >= 1
        b3_max = int((((c2/a2) - x0) / (y0/a3))-1)
        b3 = b3_max  # Chọn b3 lớn nhất có thể để tối ưu E
        E = a3 * x0 + b3 * y0
        A = b3 * (c2 / b2)
        B = b3 * (c1 / b1)
        C = a3 * (c1 / a1)
        D = a3 * (c2 / a2)
        kq = phan_so(E)  # Vì đã tối ưu E, không cần so sánh thêm
    if (c1/a1) > (c2/a2):
        b3_min = max(int((((c2/a2) - x0) / (y0/a3))), 1)
        b3_max = int((((c1/a1) - x0) / (y0/a3))-1)
        b3 = b3_max  # Chọn b3 lớn nhất để tối ưu E
        E = a3 * x0 + b3 * y0
        A = b3 * (c2 / b2)
        B = b3 * (c1 / b1)
        C = a3 * (c1 / a1)
        D = a3 * (c2 / a2)
        kq = phan_so(E)
    x, y=symbols("x, y")

    noi_dung = f" Một xưởng sản xuất có ${{2}}$ máy đặc chủng ${{A}}$ và ${{B}}$ để sản xuất ${{2}}$ loại sản phẩm ${{X}}$ và ${{Y}}$. Để sản xuất $ {{1}} $ tấn sản phẩm loại ${{X}}$ cần dùng máy ${{A}} $ trong $ {{{a1}}} $ giờ và dùng máy $ {{B}}$ trong $ {{{a2}}} $ giờ. Để sản xuất $ {{1}} $ tấn sản phẩm loại ${{Y}}  $ cần dùng máy $ {{A}} $ trong ${{{b1}}} $ giờ và dùng máy $B$ trong ${{{b2}}}$ giờ. Cho biết mỗi máy không thể sản xuất đồng thời ${{2}}$ loại sản phẩm. Máy ${{A}}$ làm việc không quá ${{{c1}}}$ giờ cho một lần hoạt động, máy ${{B}}$ làm việc không quá ${{{c2}}} $ giờ cho một lần hoạt động. Một tấn sản phẩm loại ${{X}}$ lãi ${{{a3}}} $ triệu đồng và $ {{1}} $ tấn sản phẩm loại ${{Y}}$ lãi ${{{b3}}}$ triệu đồng. Số tiền lãi thu được lớn nhất là:"

    noi_dung_loigiai=(f"Gọi ${{x}}$, ${{y}}$ là số tấn sản phẩm loại ${{X}}$, ${{Y}}$ cần sản xuất ($ {{x,y\\ge 0 }}$).\n\n"
            f"Theo giả thiết bài toán ta có $\\left\\{{ \\begin{{array}}{{l}}\n\
             x \\ge 0 \\\\ \n\
            y \\ge 0 \\\\ \n\
                   {latex(a1*x+b1*y)} \\le {c1} \\\\ \n\
                     {latex(a2*x+b2*y)} \\le {c2} \n\
             \\end{{array}} \\right.$\n\n"

             f"Số tiền lãi thu về là $ F(x;y) ={a3}x+{b3}y $ (triệu đồng).\n\n "
             f"Số tiền lãi lớn nhất là ${{{kq}}}$ (triệu đồng) ")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq

    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C2_B2_06]-M3. Tìm m để hệ bất phương trình vô nghiệm
def bch_12_L10_C2_B2_06():
    x1=random.randint(-5,5)
    x2=x1+random.randint(1,5) 
    c=random.randint(1,5)
    x, m=symbols("x, m")
    a=random.randint(1,5) 
    b=random.randint(1,5) 

    chon=random.randint(1,4) 
    if chon ==1:
        noi_dung=f"Hệ bất phương trình $\\left\\{{ \\begin{{array}}{{l}}\n\
            {latex(expand(c*(x-x1)*(x-x2)))} < 0 \\\\ \n\
            {latex(a*x-b*m)}<0 \n\
            \\end{{array}} \\right.$ vô nghiệm khi  "
        noi_dung_loigiai=(f"Từ ${latex(expand(c*(x-x1)*(x-x2)))} < 0$ suy ra $x \\in ({x1}; {x2})$ \n\n"
                        f" Từ $ {latex(a*x-b*m)}<0$ suy ra $x \\in \\left( -\\infty; {latex(b*m/a)} \\right)$ \n\n"
                        f" Hệ vô nghiệm khi hai tập hợp trên giao nhau bằng rỗng tức là $ {latex(b*m/a)} \\le {x1}$ hay $m \\le {phan_so(x1*a/b)}$")

        kq=f" $m \\le {phan_so(x1*a/b)}$"
        kq2=f"$m < {phan_so(x1*a/b)}$ "
        kq3=f"$m \\ge {phan_so(x1*a/b)}$ "
        kq4=f"$m > {phan_so(x1*a/b)}$ "
    if chon ==2:
        noi_dung=f"Hệ bất phương trình $\\left\\{{ \\begin{{array}}{{l}}\n\
            {latex(expand(c*(x-x1)*(x-x2)))} \\le 0 \\\\ \n\
            {latex(a*x-b*m)} \\le 0 \n\
            \\end{{array}} \\right.$ vô nghiệm khi  "
        noi_dung_loigiai=(f"Từ ${latex(expand(c*(x-x1)*(x-x2)))} \\le 0$ suy ra $x \\in \\left[ {x1}; {x2} \\right]$ \n\n"
                        f" Từ $ {latex(a*x-b*m)} \\le 0$ suy ra $x \\in \\left( -\\infty; {latex(b*m/a)} \\right ]$ \n\n"
                        f" Hệ vô nghiệm khi hai tập hợp trên giao nhau bằng rỗng tức là $ {latex(b*m/a)} < {x1}$ hay $m < {phan_so(x1*a/b)}$")

        kq2=f" $m \\le {phan_so(x1*a/b)}$"
        kq=f"$m < {phan_so(x1*a/b)}$ "
        kq3=f"$m \\ge {phan_so(x1*a/b)}$ "
        kq4=f"$m > {phan_so(x1*a/b)}$ "

    if chon ==3:
        noi_dung=f"Hệ bất phương trình $\\left\\{{ \\begin{{array}}{{l}}\n\
            {latex(expand(c*(x-x1)*(x-x2)))} \\le 0 \\\\ \n\
            {latex(a*x-b*m)}<0 \n\
            \\end{{array}} \\right.$ vô nghiệm khi  "
        noi_dung_loigiai=(f"Từ ${latex(expand(c*(x-x1)*(x-x2)))} \\le 0$ suy ra $x \\in \\left[{x1}; {x2} \\right]$ \n\n"
                        f" Từ $ {latex(a*x-b*m)}<0$ suy ra $x \\in \\left( -\\infty; {latex(b*m/a)} \\right)$ \n\n"
                        f" Hệ vô nghiệm khi hai tập hợp trên giao nhau bằng rỗng tức là $ {latex(b*m/a)} \\le {x1}$ hay $m \\le {phan_so(x1*a/b)}$")

        kq=f" $m \\le {phan_so(x1*a/b)}$"
        kq2=f"$m < {phan_so(x1*a/b)}$ "
        kq3=f"$m \\ge {phan_so(x1*a/b)}$ "
        kq4=f"$m > {phan_so(x1*a/b)}$ "
    if chon ==4:
        noi_dung=f"Hệ bất phương trình $\\left\\{{ \\begin{{array}}{{l}}\n\
            {latex(expand(c*(x-x1)*(x-x2)))} < 0 \\\\ \n\
            {latex(a*x-b*m)} \\le 0 \n\
            \\end{{array}} \\right.$ vô nghiệm khi  "
        noi_dung_loigiai=(f"Từ ${latex(expand(c*(x-x1)*(x-x2)))} < 0$ suy ra $x \\in ({x1}; {x2})$ \n\n"
                        f" Từ $ {latex(a*x-b*m)} \\le 0$ suy ra $x \\in \\left( -\\infty; {latex(b*m/a)} \\right]$ \n\n"
                        f" Hệ vô nghiệm khi hai tập hợp trên giao nhau bằng rỗng tức là $ {latex(b*m/a)} \\le {x1}$ hay $m \\le {phan_so(x1*a/b)}$")

        kq=f" $m \\le {phan_so(x1*a/b)}$"
        kq2=f"$m < {phan_so(x1*a/b)}$ "
        kq3=f"$m \\ge {phan_so(x1*a/b)}$ "
        kq4=f"$m > {phan_so(x1*a/b)}$ "
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

#[D10_C2_B2_07]-SA-M3. Hệ: ax-y+b>=0, cx-y+d>=0, y>=0. Tìm min F=mx+n
def bch_12_L10_C2_B2_07():
    x,y=sp.symbols("x y")
    while True:
        
        a=random.randint(1,5)
        b=random.randint(-5,-1)
        c=random.randint(-6,-1)
        d=random.randint(1,6)
        m=random.choice([i for i in range(-5, 6) if i!=0])
        n=random.choice([i for i in range(-5, 6) if i!=0])

        # Khai báo các phương trình
        eq1 = Eq(a*x-y+b, 0)
        eq2 = Eq(c*x-y+d, 0)

        # Giải hệ phương trình
        solution = solve((eq1, eq2), (x, y))

        # In kết quả
        if solution:
            x_C = solution[x]
            y_C = solution[y]
        x_A,y_A=-b/a, 0
        x_B,y_B=-d/c, 0

        F_A=m*x_A + n*y_A
        F_B=m*x_B + n*y_B
        F_C=m*x_C + n*y_C
        min_F=min(F_A,F_B,F_C)
        if all([min_F>-9, min_F<999]):
            break

    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a*x-y+b)} \\ge 0 \\\\ \n\
    {latex(c*x-y+d)} \\ge 0 \\\\ \n\
    y \\le 0 \n\
    \\end{{array}} \\right."

    
    t=min_F.is_integer
    if t:
        noi_dung = (
        f"Tìm giá trị nhỏ nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$.")
        dap_an=int(min_F)
    else:
        noi_dung = (
        f"Tìm giá trị nhỏ nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$ (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round_half_up(min_F,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Đường thẳng $d_1:{latex(a*x-y+b)}=0$ cắt ${{Ox}}$ tại điểm $A({phan_so(-b/a)};0)$.\n\n"
    f"Đường thẳng $d_2:{latex(c*x-y+d)}=0$ cắt ${{Ox}}$ tại điểm $B({phan_so(-d/c)};0)$.\n\n"
    f"$d_1$ cắt $d_2$ tại điểm $C({phan_so(x_C)};{phan_so(y_C)})$.\n\n"
    f"Miền nghiệm là hình tam giác ${{ABC}}$.\n\n"
    f"$F({phan_so(x_A)};0)={phan_so(F_A)}, F({phan_so(x_B)};0)={phan_so(F_B)}, F({phan_so(x_C)};0)={phan_so(F_C)}$.\n\n"
    f"Giá trị nhỏ nhất của $F(x;y)$ là ${{{phan_so(min_F)}}}={dap_an}$."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_08]-SA-M3. Hệ: ax-y+b>=0, cx-y+d>=0, y>=0. Tìm max F=mx+n
def bch_12_L10_C2_B2_08():
    x,y=sp.symbols("x y")
    while True:
        
        a=random.randint(1,5)
        b=random.randint(-5,-1)
        c=random.randint(-6,-1)
        d=random.randint(1,6)
        m=random.choice([i for i in range(-5, 6) if i!=0])
        n=random.choice([i for i in range(-5, 6) if i!=0])

        # Khai báo các phương trình
        eq1 = Eq(a*x-y+b, 0)
        eq2 = Eq(c*x-y+d, 0)

        # Giải hệ phương trình
        solution = solve((eq1, eq2), (x, y))

        # In kết quả
        if solution:
            x_C = solution[x]
            y_C = solution[y]
        x_A,y_A=-b/a, 0
        x_B,y_B=-d/c, 0

        F_A=m*x_A + n*y_A
        F_B=m*x_B + n*y_B
        F_C=m*x_C + n*y_C
        max_F=max(F_A,F_B,F_C)
        if all([max_F>-9, max_F<999]):
            break

    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a*x-y+b)} \\ge 0 \\\\ \n\
    {latex(c*x-y+d)} \\ge 0 \\\\ \n\
    y \\le 0 \n\
    \\end{{array}} \\right."

    
    t=max_F.is_integer
    if t:
        noi_dung = (
        f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$.")
        dap_an=int(max_F)
    else:
        noi_dung = (
        f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$ (kết quả làm tròn đến hàng phần mười)."
        )
        dap_an=f"{round_half_up(max_F,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
    f"Đường thẳng $d_1:{latex(a*x-y+b)}=0$ cắt ${{Ox}}$ tại điểm $A({phan_so(-b/a)};0)$.\n\n"
    f"Đường thẳng $d_2:{latex(c*x-y+d)}=0$ cắt ${{Ox}}$ tại điểm $B({phan_so(-d/c)};0)$.\n\n"
    f"$d_1$ cắt $d_2$ tại điểm $C({phan_so(x_C)};{phan_so(y_C)})$.\n\n"
    f"Miền nghiệm là hình tam giác ${{ABC}}$.\n\n"
    f"$F({phan_so(x_A)};0)={phan_so(F_A)}, F({phan_so(x_B)};0)={phan_so(F_B)}, F({phan_so(x_C)};0)={phan_so(F_C)}$.\n\n"
    f"Giá trị lớn nhất của $F(x;y)$ là ${{{phan_so(max_F)}}}={dap_an}$."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_09]-SA-M3. Hệ: ax+by+c>=0, dx+ey+f>=0, x<=0. Tìm max F=mx+n.
def bch_12_L10_C2_B2_09():
    x,y=sp.symbols("x y")
    while True:
        a1=random.randint(-5,-1)
        b1=random.randint(1,4)
        c1=a1*b1

        a2=a1
        b2=random.randint(5,8)
        c2=a2*b2

        if all([gcd(a1,b1)==1, gcd(a2,b2)==1]):
            break

    m=random.choice([i for i in range(-5, 6) if i!=0])
    n=random.choice([i for i in range(-5, 6) if i!=0])
    x_A1, y_A1 = a1, 0
    x_A2, y_A2 = a1, 0
    x_B1, y_B1 = 0, b1
    x_B2, y_B2 = 0, b2

    F_A=m*x_A1 + n*y_A1
    F_B1=m*x_B1 + n*y_B1
    F_B2=m*x_B2 + n*y_B2
    max_F=max(F_A,F_B1,F_B2)
 
    f1=b1*x+a1*y-c1
    f2=b2*x+a2*y-c2


    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f1)} \\le 0 \\\\ \n\
    {latex(f2)} \\ge 0 \\\\ \n\
    x \\le 0 \n\
    \\end{{array}} \\right."

    

    noi_dung = (
    f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$.")
    dap_an=int(max_F)

    noi_dung_loigiai=(
        f"Đường thẳng $d_1:{latex(f1)}=0$ qua điểm $A({phan_so(x_A1)};0)$ và $B_1(0;{phan_so(y_B1)})$.\n\n"
        f"Đường thẳng $d_2:{latex(f2)}=0$ qua điểm $A({phan_so(x_A2)};0)$ và $B_2(0;{phan_so(y_B2)})$.\n\n"
        f"Miền nghiệm của ${latex(f1)} \\ge 0$ là nửa mặt phẳng chứa $d_1$ và không chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của ${latex(f2)} \\le 0$ là nửa mặt phẳng chứa $d_2$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của $x\\le 0$ là nửa mặt phẳng bên trái trục ${{Oy}}$.\n\n"
        f"Miện nghiệm của hệ đã cho là hình tam giác ${{AB_1B_2}}$.\n\n"
        f"$F({phan_so(x_A1)};0)={phan_so(F_A)}, F(0;{phan_so(y_B1)})={phan_so(F_B1)}, F(0;{phan_so(y_B2)})={phan_so(F_B2)}$.\n\n"
        f"Giá trị lớn nhất của $F(x;y)$ là ${{{dap_an}}}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_10]-SA-M3. Hệ: ax+by+c>=0, dx+ey+f>=0, x<=0. Tìm min F=mx+n.
def bch_12_L10_C2_B2_10():
    x,y=sp.symbols("x y")
    while True:
        a1=random.randint(-5,-1)
        b1=random.randint(1,4)
        c1=a1*b1

        a2=a1
        b2=random.randint(5,8)
        c2=a2*b2

        if all([gcd(a1,b1)==1, gcd(a2,b2)==1]):
            break

    m=random.choice([i for i in range(-5, 6) if i!=0])
    n=random.choice([i for i in range(-5, 6) if i!=0])
    x_A1, y_A1 = a1, 0
    x_A2, y_A2 = a1, 0
    x_B1, y_B1 = 0, b1
    x_B2, y_B2 = 0, b2

    F_A=m*x_A1 + n*y_A1
    F_B1=m*x_B1 + n*y_B1
    F_B2=m*x_B2 + n*y_B2
    min_F=min(F_A,F_B1,F_B2)
 
    f1=b1*x+a1*y-c1
    f2=b2*x+a2*y-c2


    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f1)} \\le 0 \\\\ \n\
    {latex(f2)} \\ge 0 \\\\ \n\
    x \\le 0 \n\
    \\end{{array}} \\right."

    

    noi_dung = (
    f"Tìm giá trị nhỏ nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$.")
    dap_an=min_F

    noi_dung_loigiai=(
        f"Đường thẳng $d_1:{latex(f1)}=0$ qua điểm $A({phan_so(x_A1)};0)$ và $B_1(0;{phan_so(y_B1)})$.\n\n"
        f"Đường thẳng $d_2:{latex(f2)}=0$ qua điểm $A({phan_so(x_A2)};0)$ và $B_2(0;{phan_so(y_B2)})$.\n\n"
        f"Miền nghiệm của ${latex(f1)} \\ge 0$ là nửa mặt phẳng chứa $d_1$ và không chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của ${latex(f2)} \\le 0$ là nửa mặt phẳng chứa $d_2$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của $x\\le 0$ là nửa mặt phẳng bên trái trục ${{Oy}}$.\n\n"
        f"Miện nghiệm của hệ đã cho là hình tam giác ${{AB_1B_2}}$.\n\n"
        f"$F({phan_so(x_A1)};0)={phan_so(F_A)}, F(0;{phan_so(y_B1)})={phan_so(F_B1)}, F(0;{phan_so(y_B2)})={phan_so(F_B2)}$.\n\n"
        f"Giá trị nhỏ nhất của $F(x;y)$ là ${{{dap_an}}}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_11]-SA-M3. Hệ: ax+by+c>=0, x>=0, y>=0. Tìm min F=mx+n.
def bch_12_L10_C2_B2_11():
    x,y=sp.symbols("x y")
    while True:
        a1=random.randint(-5,-1)
        b1=random.randint(1,4)
        c1=a1*b1

        a2=a1
        b2=random.randint(5,8)
        c2=a2*b2

        if all([gcd(a1,b1)==1, gcd(a2,b2)==1]):
            break

    m=random.choice([i for i in range(-5, 6) if i!=0])
    n=random.choice([i for i in range(-5, 6) if i!=0])
    x_A1, y_A1 = a1, 0
    x_A2, y_A2 = a1, 0
    x_B1, y_B1 = 0, b1
    x_B2, y_B2 = 0, b2

    F_A=m*x_A1 + n*y_A1
    F_B1=m*x_B1 + n*y_B1
    F_B2=m*x_B2 + n*y_B2
    min_F=min(F_A,F_B1,F_B2)
 
    f1=b1*x+a1*y-c1
    f2=b2*x+a2*y-c2


    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f1)} \\le 0 \\\\ \n\
    {latex(f2)} \\ge 0 \\\\ \n\
    x \\le 0 \n\
    \\end{{array}} \\right."

    

    noi_dung = (
    f"Tìm giá trị nhỏ nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$.")
    dap_an=min_F

    noi_dung_loigiai=(
        f"Đường thẳng $d_1:{latex(f1)}=0$ qua điểm $A({phan_so(x_A1)};0)$ và $B_1(0;{phan_so(y_B1)})$.\n\n"
        f"Đường thẳng $d_2:{latex(f2)}=0$ qua điểm $A({phan_so(x_A2)};0)$ và $B_2(0;{phan_so(y_B2)})$.\n\n"
        f"Miền nghiệm của ${latex(f1)} \\ge 0$ là nửa mặt phẳng chứa $d_1$ và không chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của ${latex(f2)} \\le 0$ là nửa mặt phẳng chứa $d_2$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của $x\\le 0$ là nửa mặt phẳng bên trái trục ${{Oy}}$.\n\n"
        f"Miện nghiệm của hệ đã cho là hình tam giác ${{AB_1B_2}}$.\n\n"
        f"$F({phan_so(x_A1)};0)={phan_so(F_A)}, F(0;{phan_so(y_B1)})={phan_so(F_B1)}, F(0;{phan_so(y_B2)})={phan_so(F_B2)}$.\n\n"
        f"Giá trị nhỏ nhất của $F(x;y)$ là ${{{dap_an}}}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_12]-SA-M3. Hệ: ax+by+c>=0, x>=0, y>=0. Tìm max F=mx+n.
def bch_12_L10_C2_B2_12():
    x,y=sp.symbols("x y")
    while True:
        a1=random.randint(-5,-1)
        b1=random.randint(1,4)
        c1=a1*b1

        a2=a1
        b2=random.randint(5,8)
        c2=a2*b2

        if all([gcd(a1,b1)==1, gcd(a2,b2)==1]):
            break

    m=random.choice([i for i in range(-5, 6) if i!=0])
    n=random.choice([i for i in range(-5, 6) if i!=0])
    x_A1, y_A1 = a1, 0
    x_A2, y_A2 = a1, 0
    x_B1, y_B1 = 0, b1
    x_B2, y_B2 = 0, b2

    F_A=m*x_A1 + n*y_A1
    F_B1=m*x_B1 + n*y_B1
    F_B2=m*x_B2 + n*y_B2
    max_F=max(F_A,F_B1,F_B2)
 
    f1=b1*x+a1*y-c1
    f2=b2*x+a2*y-c2


    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f1)} \\le 0 \\\\ \n\
    {latex(f2)} \\ge 0 \\\\ \n\
    x \\le 0 \n\
    \\end{{array}} \\right."

    

    noi_dung = (
    f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(m*x+n*y)}$ thỏa mãn điều kiện ${hedk}$.")
    dap_an=max_F

    noi_dung_loigiai=(
        f"Đường thẳng $d_1:{latex(f1)}=0$ qua điểm $A({phan_so(x_A1)};0)$ và $B_1(0;{phan_so(y_B1)})$.\n\n"
        f"Đường thẳng $d_2:{latex(f2)}=0$ qua điểm $A({phan_so(x_A2)};0)$ và $B_2(0;{phan_so(y_B2)})$.\n\n"
        f"Miền nghiệm của ${latex(f1)} \\ge 0$ là nửa mặt phẳng chứa $d_1$ và không chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của ${latex(f2)} \\le 0$ là nửa mặt phẳng chứa $d_2$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của $x\\le 0$ là nửa mặt phẳng bên trái trục ${{Oy}}$.\n\n"
        f"Miện nghiệm của hệ đã cho là hình tam giác ${{AB_1B_2}}$.\n\n"
        f"$F({phan_so(x_A1)};0)={phan_so(F_A)}, F(0;{phan_so(y_B1)})={phan_so(F_B1)}, F(0;{phan_so(y_B2)})={phan_so(F_B2)}$.\n\n"
        f"Giá trị lớn nhất của $F(x;y)$ là ${{{dap_an}}}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an


#[D10_C2_B2_13]-SA-M3. Hệ: ax+by+c>=0, dx+ey+f>=0, x>=0, y>=0. Tìm min F=mx+n+p.
def bch_12_L10_C2_B2_13():
    x,y=sp.symbols("x y")
    while True:
        a1=random.randint(1,5)
        b1=random.randint(-5,-1)
        a2=random.randint(1,10)
        b2=random.randint(1,6)
        c1, c2 = -a1*b1, -a2*b2

        m=random.choice([i for i in range(-5, 6) if i!=0])
        n=random.choice([i for i in range(-5, 6) if i!=0])
        p=random.choice([i for i in range(-5, 6) if i!=0])
        x_A1, y_A1 = a1, 0
        x_A2, y_A2 = a2, 0
        x_B1, y_B1 = 0, b1
        x_B2, y_B2 = 0, b2

        # Khai báo các phương trình
        eq1 = Eq(b1*x+a1*y+c1, 0)
        eq2 = Eq(b2*x+a2*y+c2, 0)

        # Giải hệ phương trình
        solution = solve((eq1, eq2), (x, y))

        # In kết quả
        if solution:
            x_C = solution[x]
            y_C = solution[y]

        f=m*x+n*y+p
        F_A1=f.subs({x:x_A1, y:y_A1})
        F_B1=f.subs({x:x_B1, y:y_B1})
        F_B2=f.subs({x:x_B2, y:y_B2})
        F_C=f.subs({x:x_C, y:y_C})
        min_F=min(0,F_A1,F_B2, F_C)  
        if all([a2>a1, min_F>-9]):
            break
    
 
    f1=b1*x+a1*y+c1
    f2=b2*x+a2*y+c2


    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f1)} \\ge 0 \\\\ \n\
    {latex(f2)} \\le 0 \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."

    t=min_F.is_integer
    if t:
        noi_dung = (
        f"Tìm giá trị nhỏ nhất của biểu thức $F(x;y)={latex(f)}$ thỏa mãn điều kiện ${hedk}$.")
        dap_an=min_F
    else:
        noi_dung = (
        f"Tìm giá trị nhỏ nhất của biểu thức $F(x;y)={latex(f)}$ thỏa mãn điều kiện ${hedk}$ (kết quả làm tròn đến hàng phần mười).")
        dap_an=f"{round_half_up(min_F,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
        f"Đường thẳng $d_1:{latex(f1)}=0$ qua điểm $A_1({phan_so(x_A1)};0)$ và $B_1(0;{phan_so(y_B1)})$.\n\n"
        f"Đường thẳng $d_2:{latex(f2)}=0$ qua điểm $A_2({phan_so(x_A2)};0)$ và $B_2(0;{phan_so(y_B2)})$.\n\n"
        f"Miền nghiệm của ${latex(f1)} \\ge 0$ là nửa mặt phẳng chứa $d_1$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của ${latex(f2)} \\le 0$ là nửa mặt phẳng chứa $d_2$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của $x\\ge 0$ là nửa mặt phẳng bên phải trục ${{Oy}}$.\n\n"
        f"Miền nghiệm của $y\\ge 0$ là nửa mặt phẳng bên trên trục ${{Ox}}$.\n\n"
        f"$d_1$ và $d_2$ cắt nhau tại điểm $C({phan_so(x_C)};{phan_so(y_C)})$.\n\n"
        f"Miện nghiệm của hệ đã cho là miền trong hình tứ giác ${{OA_1CB_2}}$.\n\n"
        f"$F(0;0)=0; F({phan_so(x_A1)};0)={phan_so(F_A1)}, F(0;{phan_so(y_B2)})={phan_so(F_B2)}, F({phan_so(x_C)};{phan_so(y_C)})={phan_so(F_C)}$.\n\n"
        f"Giá trị nhỏ nhất của $F(x;y)$ là ${{{dap_an}}}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_14]-SA-M3. Hệ: ax+by+c>=0, dx+ey+f>=0, x>=0, y>=0. Tìm max F=mx+n+p.
def bch_12_L10_C2_B2_14():
    x,y=sp.symbols("x y")
    while True:
        a1=random.randint(1,5)
        b1=random.randint(-5,-1)
        a2=random.randint(1,10)
        b2=random.randint(1,6)
        c1, c2 = -a1*b1, -a2*b2

        m=random.choice([i for i in range(-5, 6) if i!=0])
        n=random.choice([i for i in range(-5, 6) if i!=0])
        p=random.choice([i for i in range(-5, 6) if i!=0])
        x_A1, y_A1 = a1, 0
        x_A2, y_A2 = a2, 0
        x_B1, y_B1 = 0, b1
        x_B2, y_B2 = 0, b2

        # Khai báo các phương trình
        eq1 = Eq(b1*x+a1*y+c1, 0)
        eq2 = Eq(b2*x+a2*y+c2, 0)

        # Giải hệ phương trình
        solution = solve((eq1, eq2), (x, y))

        # In kết quả
        if solution:
            x_C = solution[x]
            y_C = solution[y]

        f=m*x+n*y+p
        F_A1=f.subs({x:x_A1, y:y_A1})
        F_B1=f.subs({x:x_B1, y:y_B1})
        F_B2=f.subs({x:x_B2, y:y_B2})
        F_C=f.subs({x:x_C, y:y_C})
        max_F=max(0,F_A1,F_B2, F_C)  
        if all([a2>a1, max_F>-9]):
            break
    
 
    f1=b1*x+a1*y+c1
    f2=b2*x+a2*y+c2


    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(f1)} \\ge 0 \\\\ \n\
    {latex(f2)} \\le 0 \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."

    t=max_F.is_integer
    if t:
        noi_dung = (
        f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(f)}$ thỏa mãn điều kiện ${hedk}$.")
        dap_an=max_F
    else:
        noi_dung = (
        f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(f)}$ thỏa mãn điều kiện ${hedk}$ (kết quả làm tròn đến hàng phần mười).")
        dap_an=f"{round_half_up(max_F,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
        f"Đường thẳng $d_1:{latex(f1)}=0$ qua điểm $A_1({phan_so(x_A1)};0)$ và $B_1(0;{phan_so(y_B1)})$.\n\n"
        f"Đường thẳng $d_2:{latex(f2)}=0$ qua điểm $A_2({phan_so(x_A2)};0)$ và $B_2(0;{phan_so(y_B2)})$.\n\n"
        f"Miền nghiệm của ${latex(f1)} \\ge 0$ là nửa mặt phẳng chứa $d_1$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của ${latex(f2)} \\le 0$ là nửa mặt phẳng chứa $d_2$ và chứa điểm ${{O}}$.\n\n"
        f"Miền nghiệm của $x\\ge 0$ là nửa mặt phẳng bên phải trục ${{Oy}}$.\n\n"
        f"Miền nghiệm của $y\\ge 0$ là nửa mặt phẳng bên trên trục ${{Ox}}$.\n\n"
        f"$d_1$ và $d_2$ cắt nhau tại điểm $C({phan_so(x_C)};{phan_so(y_C)})$.\n\n"
        f"Miện nghiệm của hệ đã cho là miền trong hình tứ giác ${{OA_1CB_2}}$.\n\n"
        f"$F(0;0)=0; F({phan_so(x_A1)};0)={phan_so(F_A1)}, F(0;{phan_so(y_B2)})={phan_so(F_B2)}, F({phan_so(x_C)};{phan_so(y_C)})={phan_so(F_C)}$.\n\n"
        f"Giá trị lớn nhất của $F(x;y)$ là ${{{dap_an}}}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

def sinh_duong_thang_khong_qua_O():
        while True:
            a = random.choice([i for i in range(-4, 4) if i!=0])
            b = random.choice([i for i in range(-4, 4) if i!=0])
            c = random.choice([i for i in range(-4, 6) if i!=0])
            # Không đồng thời bằng 0 và không đi qua gốc tọa độ
            if all([a*0 + b*0 + c != 0]):
                return (a, b, c)

def kiem_tra_cat_nhau(d1, d2):
    x,y=symbols("x y")
    # Giải hệ hai phương trình d1 và d2
    a1, b1, c1 = d1
    a2, b2, c2 = d2

    pt1 = Eq(a1*x + b1*y + c1, 0)
    pt2 = Eq(a2*x + b2*y + c2, 0)
    nghiem = solve((pt1, pt2), (x, y), dict=True)
    return len(nghiem) == 1  # Có nghiệm duy nhất (giao điểm)

#[D10_C2_B2_15]-SA-M3. Hệ: 3 BPT hai ẩn. Tìm max F=mx+n+p.
def bch_12_L10_C2_B2_15():
    x,y=symbols("x y")   

    noi_dung=""
    noi_dung_loigiai=""
    dap_an=""

    while True:
            # Sinh ba đường thẳng
            d1 = sinh_duong_thang_khong_qua_O()
            d2 = sinh_duong_thang_khong_qua_O()
            d3 = sinh_duong_thang_khong_qua_O()
            a1,b1,c1=d1
            a2,b2,c2=d2
            a3,b3,c3=d3
            x1,x2,x3=-c1/a1, -c2/a2,-c3/a3
            y1,y2,y3=-c1/b1,-c2/b2,-c3/b3
            k1,k2,k3=-a1/b1,-a2/b2,-a3/b3
            if any([k1<0,k2<0,k3>0,y1<0,y2>0,y3<0,c1<0,c2<0,c3<0,k2>k1]):
                continue
            
            # Kiểm tra đôi một cắt nhau
            if all([kiem_tra_cat_nhau(d1, d2),
                kiem_tra_cat_nhau(d1, d3),
                kiem_tra_cat_nhau(d2, d3),x1<0,x3>0, x2>x3, y1>0,y2<0,y3>y1]):
                break
        

    f1=a1*x+b1*y+c1
    f2=a2*x+b2*y+c2
    f3=a3*x+b3*y+c3

    chon=random.randint(1,6)
    
    if chon==1:
        bpt_1=f"{latex(f1)}\\ge 0"
        bpt_2=f"{latex(f2)}\\ge 0"
        bpt_3=f"{latex(f3)}\\ge 0"
    
    if chon==2:
        bpt_1=f"{latex(-f1)}\\le 0"
        bpt_2=f"{latex(-f2)}\\le 0"
        bpt_3=f"{latex(-f3)}\\le 0"

    if chon==3:
        bpt_1=f"{latex(-f1)}\\le 0"
        bpt_2=f"{latex(f2)}\\ge 0"
        bpt_3=f"{latex(f3)}\\ge 0"

    if chon==4:
        bpt_1=f"{latex(f1)}\\ge 0"
        bpt_2=f"{latex(f2)}\\ge 0"
        bpt_3=f"{latex(-f3)}\\le 0"

    if chon==5:
        bpt_1=f"{latex(f1)}\\ge 0"
        bpt_2=f"{latex(-f2)}\\le 0"
        bpt_3=f"{latex(-f3)}\\le 0"

    if chon==6:
        bpt_1=f"{latex(-f1)}\\le 0"
        bpt_2=f"{latex(-f2)}\\le 0"
        bpt_3=f"{latex(f3)}\\ge 0"

    
    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {bpt_1} \\\\ \n\
    {bpt_2} \\\\ \n\
    {bpt_3}\n\
    \\end{{array}} \\right."

    # Khai báo các phương trình
    eq1 = Eq(a1*x+b1*y+c1, 0)
    eq2 = Eq(a2*x+b2*y+c2, 0)
    eq3 = Eq(a3*x+b3*y+c3, 0)

    # Giải hệ phương trình
    sol_1 = solve((eq1, eq2), (x, y))
    x_1, y_1 = sol_1[x], sol_1[y]

    sol_2 = solve((eq2, eq3), (x, y))
    x_2, y_2 = sol_2[x], sol_2[y]

    sol_3 = solve((eq1, eq3), (x, y))
    x_3, y_3 = sol_3[x], sol_3[y]

    m=random.choice([i for i in range(-5, 6) if i!=0])
    n=random.choice([i for i in range(-5, 6) if i!=0])

    f=m*x+n*y
    F_1=f.subs({x:x_1, y:y_1})
    F_2=f.subs({x:x_2, y:y_2})
    F_3=f.subs({x:x_3, y:y_3})
    max_F=max(F_1,F_2,F_3)

    t=max_F.is_integer
    if t:
        noi_dung = (
        f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(f)}$ thỏa mãn điều kiện ${hedk}$.")
        dap_an=max_F
    else:
        noi_dung = (
        f"Tìm giá trị lớn nhất của biểu thức $F(x;y)={latex(f)}$ thỏa mãn điều kiện ${hedk}$ (kết quả làm tròn đến hàng phần mười).")
        dap_an=f"{round_half_up(max_F,1):.1f}".replace(".",",")

    noi_dung_loigiai=(
        f"$d_1$ và $d_2$ cắt nhau tại điểm $A({phan_so(x_1)};{phan_so(y_1)})$.\n\n"
        f"$d_2$ và $d_3$ cắt nhau tại điểm $B({phan_so(x_2)};{phan_so(y_2)})$.\n\n"
        f"$d_1$ và $d_3$ cắt nhau tại điểm $C({phan_so(x_3)};{phan_so(y_3)})$.\n\n"
        f"Miện nghiệm của hệ đã cho là miền trong hình tam giác ${{ABC}}$.\n\n"
        f"$F({phan_so(x_1)};{phan_so(y_1)})={phan_so(F_1)}, F({phan_so(x_2)};{phan_so(y_2)})={phan_so(F_2)}, F({phan_so(x_3)};{phan_so(y_3)})={phan_so(F_3)}$.\n\n"
        f"Giá trị lớn nhất của $F(x;y)$ là ${{{dap_an}}}$."
    )  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_16]-SA-M3. Tìm lợi nhuận lớn nhất khi sản xuất 2 sản phẩm bằng 2 máy.
def bch_12_L10_C2_B2_16():
    x,y=symbols("x y")
    X, Y ="X", "Y"
    A, B ="A", "B"
    while True:

        #Hệ số thời gian cho máy A
        a1=random.randint(1,6)
        b1=random.randint(1,4)
        c1=random.randint(7,12)

        #Hệ số thời gian cho máy B
        a2=random.randint(1,6)
        b2=random.randint(1,4)
        c2=random.randint(7,10)

        x_1, x_2 = c1/a1, c2/a2
        y_1, y_2 = c1/b1, c2/b2
        if all([x_2 > x_1, y_1>y_2]):
            break
    while True:
        m=random.randint(2,10)
        n=random.randint(2,10)
        if m!=n:
            break
    f1=a1*x+b1*y-c1
    f2=a2*x+b2*y-c2
    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a1*x+b1*y)}\\le {c1} \\\\ \n\
    {latex(a2*x+b2*y)}\\le {c2} \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."
    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        a1*x + b1*y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(a1*x + b1*y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$({phan_so(pt[x])}, {phan_so(pt[y])}) \\Rightarrow T = {phan_so(m*pt[x] + n*pt[y])}$\n\n"

    noi_dung = (
    f"Một xưởng sản xuất có hai máy đặc chủng là máy {A} và máy {B} để sản xuất hai loại sản phẩm {X} và {Y}."
    f" Để sản xuất 1 tấn sản phẩm loại {X} cần dùng máy {A} trong {a1} giờ và dùng máy {B} trong {a2} giờ."
    f" Để sản xuất 1 tấn sản phẩm loại {Y} cần dùng máy {A} trong {b1} giờ và dùng máy {B} trong {b2} giờ."
    f" Cho biết mỗi máy không thể sản xuất đồng thời hai loại sản phẩm."
    f" Máy {A} làm việc không quá {c1} giờ một ngày, máy {B} làm việc không quá {c2} giờ một ngày."
    f" Một sản phẩm {X} lãi {m} triệu đồng và một sản phẩm loại {Y} lãi {n} triệu đồng."
    f" Tính số tiền lãi có thể thu được lớn nhất."
    )
    t=best_Z .is_integer
    if t:
        dap_an=best_Z
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        noi_dung+=f" (kết quả làm tròn đến hàng phần mười)"

    noi_dung_loigiai=(
    f"Gọi ${{x}}$, ${{y}}$ là số tấn sản phẩm loại ${{{X}}}$, ${{{Y}}}$ cần sản xuất ($ x,y\\ge 0 $).\n\n"
    f"Thời gian để máy {A} làm việc: ${latex(a1*x+b1*y)} \\le {c1}$.\n\n"
    f"Thời gian để máy {B} làm việc: ${latex(a2*x+b2*y)} \\le {c2}$.\n\n"
    f"Ta có hệ điều kiện:\n\n"
    f"${hedk}$.\n\n"
    f"Lợi nhuận thu được: $T={latex(m*x+n*y)}$.\n\n"
    f" Các đỉnh của miền nghiệm:\n\n {st}\n\n"
    f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n"
    f" Lợi nhuận lớn nhất: T = {dap_an} triệu đồng."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_17]-SA-M3. Tìm lợi nhuận lớn nhất khi sản xuất bàn và ghế
def bch_12_L10_C2_B2_17():
    x,y=symbols("x y")

    X = "bàn học sinh"
    Y = "ghế gỗ"
    A = "cưa gỗ tự động"
    B = "đánh bóng bề mặt" 

    while True:
        while True:
            m=random.randint(100,150)
            n=random.randint(70,90)
            if m!=n:
                break

        #Hệ số thời gian cho máy A
        a1=random.randint(1,4)
        b1=random.randint(1,4)
        c1=random.randint(8,12)

        #Hệ số thời gian cho máy B
        a2=random.randint(1,4)
        b2=random.randint(1,4)
        c2=random.randint(8,12)

        x_1, x_2 = c1/a1, c2/a2
        y_1, y_2 = c1/b1, c2/b2

        if a1*b2-a2*b1==0:
            continue

        #Giải hệ giao điểm 
        eq1=Eq(a1*x + b1*y , c1)
        eq2=Eq(a2*x + b2*y , c2)
        sol = solve((eq1, eq2), (x, y))
        if sol:
            x_0, y_0 = sol[x], sol[y]

        constraints = [
            a1*x + b1*y - c1 <= 0,
            a2*x + b2*y - c2 <= 0,
            x >= 0,
            y >= 0
        ]

        # Các đường biên để tìm giao điểm (dưới dạng phương trình)
        lines = [
            Eq(a1*x + b1*y , c1),
            Eq(a2*x + b2*y , c2),
            Eq(x, 0),
            Eq(y, 0)
        ]

        # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
        from itertools import combinations

        vertices = []
        for eq1, eq2 in combinations(lines, 2):
            sol = solve((eq1, eq2), (x, y), dict=True)
            if sol:
                pt = sol[0]
                # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
                if all(ineq.subs(pt) for ineq in constraints):
                    vertices.append(pt)

        # Tính giá trị hàm mục tiêu tại các đỉnh
        best_Z = -float('inf')
        best_point = None

        for pt in vertices:
            Z = m * pt[x] + n * pt[y]
            if Z > best_Z:
                best_Z = Z
                best_point = pt

        if all([x_2 > x_1, y_1>y_2, c1%a1==0, c2%a2==0, c1%b1==0, c2%b2==0, x_0.is_integer, y_0.is_integer]):
            break

    f1=a1*x+b1*y-c1
    f2=a2*x+b2*y-c2
    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a1*x+b1*y)}\\le {c1} \\\\ \n\
    {latex(a2*x+b2*y)}\\le {c2} \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."
    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        a1*x + b1*y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(a1*x + b1*y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$({phan_so(pt[x])}, {phan_so(pt[y])}) \\Rightarrow T = {phan_so(m*pt[x] + n*pt[y])}$\n\n"

    noi_dung = (
    f"Một xưởng sản xuất có hai loại máy là máy {A} và máy {B} để sản xuất hai loại sản phẩm {X} và {Y}."
    f" Để sản xuất 1 cái {X} cần dùng máy {A} trong {a1} giờ và dùng máy {B} trong {a2} giờ."
    f" Để sản xuất 1 cái {Y} cần dùng máy {A} trong {b1} giờ và dùng máy {B} trong {b2} giờ."
    f" Cho biết mỗi máy không thể sản xuất đồng thời hai loại sản phẩm."
    f" Máy {A} làm việc không quá {c1} giờ một ngày, máy {B} làm việc không quá {c2} giờ một ngày."
    f" Một cái {X} lãi {m} ngàn đồng và một cái {Y} lãi {n} ngàn đồng."
    f" Tính số tiền lãi (ngàn đồng) có thể thu được lớn nhất."
    )
    t=best_Z.is_integer
    if t:
        dap_an=best_Z
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        noi_dung+=f" (kết quả làm tròn đến hàng phần mười)"

    noi_dung_loigiai=(
    f"Gọi ${{x}}$, ${{y}}$ lần lượt là số cái {X} và {Y} cần sản xuất ($ x,y\\ge 0 $).\n\n"
    f"Thời gian để máy {A} làm việc: ${latex(a1*x+b1*y)} \\le {c1}$.\n\n"
    f"Thời gian để máy {B} làm việc: ${latex(a2*x+b2*y)} \\le {c2}$.\n\n"
    f"Ta có hệ điều kiện:\n\n"
    f"${hedk}$.\n\n"
    f"Lợi nhuận thu được: $T={latex(m*x+n*y)}$.\n\n"
    f" Các đỉnh của miền nghiệm:\n\n {st}\n\n"
    f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n"
    f" Lợi nhuận lớn nhất: T = {dap_an} ngàn đồng."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_18]-SA-M3. Tìm lợi nhuận lớn nhất khi sản xuất áo và quần
def bch_12_L10_C2_B2_18():
    x,y=symbols("x y")
    chon=random.randint(1,4)
    chon=2
    
    if chon==2:
        X = "áo sơ mi nam"
        Y = "quần tây nữ"
        A = "cắt vải CNC"
        B = "may công nghiệp"

    if chon==3:
        X = "khung xe đạp"
        Y = "tay lái xe máy"
        A = "hàn tự động"
        B = "phay CNC"

    if chon==4:
        X = "bình hoa sứ"
        Y = "tô sứ cao cấp"
        A = "tạo hình khuôn"
        B = "nung điện công nghiệp"



    while True:
        while True:
            m=random.randint(80,120)
            n=random.randint(80,120)
            if m!=n:
                break

        #Hệ số thời gian cho máy A
        a1=random.randint(1,5)
        b1=random.randint(1,4)
        c1=random.randint(8,12)

        #Hệ số thời gian cho máy B
        a2=random.randint(1,4)
        b2=random.randint(1,4)
        c2=random.randint(8,12)

        x_1, x_2 = c1/a1, c2/a2
        y_1, y_2 = c1/b1, c2/b2

        if a1*b2-a2*b1==0:
            continue

        #Giải hệ giao điểm 
        eq1=Eq(a1*x + b1*y , c1)
        eq2=Eq(a2*x + b2*y , c2)
        sol = solve((eq1, eq2), (x, y))
        if sol:
            x_0, y_0 = sol[x], sol[y]

        constraints = [
            a1*x + b1*y - c1 <= 0,
            a2*x + b2*y - c2 <= 0,
            x >= 0,
            y >= 0
        ]

        # Các đường biên để tìm giao điểm (dưới dạng phương trình)
        lines = [
            Eq(a1*x + b1*y , c1),
            Eq(a2*x + b2*y , c2),
            Eq(x, 0),
            Eq(y, 0)
        ]

        # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
        from itertools import combinations

        vertices = []
        for eq1, eq2 in combinations(lines, 2):
            sol = solve((eq1, eq2), (x, y), dict=True)
            if sol:
                pt = sol[0]
                # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
                if all(ineq.subs(pt) for ineq in constraints):
                    vertices.append(pt)

        # Tính giá trị hàm mục tiêu tại các đỉnh
        best_Z = -float('inf')
        best_point = None

        for pt in vertices:
            Z = m * pt[x] + n * pt[y]
            if Z > best_Z:
                best_Z = Z
                best_point = pt

        if all([x_2 > x_1, y_1>y_2, c1%a1==0, c2%a2==0, c1%b1==0, c2%b2==0, x_0.is_integer, y_0.is_integer]):
            break

    f1=a1*x+b1*y-c1
    f2=a2*x+b2*y-c2
    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a1*x+b1*y)}\\le {c1} \\\\ \n\
    {latex(a2*x+b2*y)}\\le {c2} \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."
    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        a1*x + b1*y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(a1*x + b1*y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    

    noi_dung = (
    f"Một công ty may mặc có hai loại máy là máy {A} và máy {B} để sản xuất hai loại sản phẩm {X} và {Y}."
    f" Để sản xuất 1 cái {X} cần dùng máy {A} trong {a1} giờ và dùng máy {B} trong {a2} giờ."
    f" Để sản xuất 1 cái {Y} cần dùng máy {A} trong {b1} giờ và dùng máy {B} trong {b2} giờ."
    f" Cho biết mỗi máy không thể sản xuất đồng thời hai loại sản phẩm."
    f" Máy {A} làm việc không quá {c1} giờ một ngày, máy {B} làm việc không quá {c2} giờ một ngày."
    f" Một cái {X} lãi {m} ngàn đồng và một cái {Y} lãi {n} ngàn đồng."
    f" Tính số tiền lãi (ngàn đồng) có thể thu được lớn nhất."
    )
    t=best_Z.is_integer
    if t:
        dap_an=best_Z
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        noi_dung+=f" (kết quả làm tròn đến hàng phần mười)"

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$({phan_so(pt[x])}, {phan_so(pt[y])}) \\Rightarrow T = {phan_so(m*pt[x] + n*pt[y])}$\n\n"

    noi_dung_loigiai=(
    f"Gọi $x$, $y$ lần lượt là số cái {X} và {Y} cần sản xuất ($ x,y\\ge 0 $).\n\n"
    f"Thời gian để máy {A} làm việc: ${latex(a1*x+b1*y)} \\le {c1}$.\n\n"
    f"Thời gian để máy {B} làm việc: ${latex(a2*x+b2*y)} \\le {c2}$.\n\n"
    f"Ta có hệ điều kiện:\n\n"
    f"${hedk}$.\n\n"
    f"Lợi nhuận thu được: $T={latex(m*x+n*y)}$.\n\n"
    f" Các đỉnh của miền nghiệm:\n\n {st}\n\n"
    f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n"
    f" Lợi nhuận lớn nhất: T = {dap_an} ngàn đồng."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_19]-SA-M3. Tìm lợi nhuận lớn nhất khi trồng 2 loại cây
def bch_12_L10_C2_B2_19():
    x,y=sp.symbols("x y")
    chon=random.randint(1,3)
    if chon==1:
        ngo,dauxanh="ngô", "đậu xanh"
        m,n=random.randint(3,5),random.randint(5,8)
    
    if chon==2:
        ngo,dauxanh="lúa", "khoai lang"
        m,n=random.randint(3,6),random.randint(4,8)

    if chon==3:
        ngo,dauxanh="cà chua", "dưa leo"
        m,n=random.randint(5,10),random.randint(4,8)
    
    
    while True:
        c1=random.randint(4,12)
        c2=random.randint(20,40)
        a2=random.randint(3,8)
        b2=random.randint(3,8)
        #Giao của đường ngày công với các trục
        x2,y2 = c2/a2, c2/b2
        if all([x2>c1, y2<c1, c2%a2==0,c2%b2==0]):
            break
    #Giải hệ giao điểm 
    eq1=Eq(x + y , c1)
    eq2=Eq(a2*x + b2*y , c2)
    sol = solve((eq1, eq2), (x, y))
    if sol:
        x_0, y_0 = sol[x], sol[y]
    f=m*x+n*y
    f_A=int(f.subs({x: 0, y: y2}))
    f_B=int(f.subs({x: x_0, y: y_0}))
    f_C=int(f.subs({x: c1, y: 0}))


    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(x + y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        x + y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$({phan_so(pt[x])}, {phan_so(pt[y])}) \\Rightarrow F = {phan_so(m*pt[x] + n*pt[y])}$\n\n"
    

    nguoi=random.choice(["Bác Nam", "Ông An", "Chú Minh", "Bác Hùng", "Ông Lâm", 
"Chú Quang", "Bác Tín", "Ông Phúc", "Chú Hải", "Bác Sơn" ])

    noi_dung = (
    f"{nguoi} dự định trồng {ngo} và {dauxanh} trên một mảnh đất có diện tích {c1} sào."
    f" Nếu trồng 1 sào {ngo} thì cần {a2} ngày công và thu được {m} triệu đồng."
    f" Nếu trồng 1 sào {dauxanh} thì cần {b2} ngày công và thu được {n} triệu đồng."
    f" Tổng số ngày công mà {nguoi} có thể sử dụng không quá {c2} ngày công."
    f" Tìm số tiền (triệu đồng) mà {nguoi} có thể thu được nhiều nhất?"
    )
    t=best_Z.is_integer
    if t:
        dap_an=best_Z
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        noi_dung+=f" (kết quả làm tròn đến hàng phần mười)"
    

    
    noi_dung_loigiai=(
    f"Gọi ${{x,y}}$ là diện tích đất để trồng {ngo} và {dauxanh}.\n\n"
    f"$x\\ge 0,y \\ge 0$.\n\n"
    f"Diện tích đất cần dùng: $x+y \\le {c1}$.\n\n"
    f"Số ngày công cần dùng: ${a2}x+{b2}y \\le {c2}$.\n\n"
    f"Miền nghiệm của hệ điều kiện là tứ giác ${{OABC}}$"
    f"với $O(0;0),A(0;{int(y2)}),B({phan_so(x_0)};{phan_so(y_0)}),C({c1};0)$.\n\n"
    #f" Các đỉnh của miền nghiệm:\n\n {st}\n\n"
    f"Lợi nhuận thu được: $F={m}x+{n}y$.\n\n"
    f"$F(0;0)=0, F(0;{int(y2)})={f_A}, F({phan_so(x_0)};{phan_so(y_0)})={f_B}, F({c1};0)={f_C}$.\n\n"
    f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n"
    f" Lợi nhuận lớn nhất: {dap_an} triệu đồng."


    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_20]-SA-M3. Tìm lợi nhuận lớn nhất khi làm 2 đồ vật bán chợ Tết
def bch_12_L10_C2_B2_20():
    x,y=sp.symbols("x y")
    while True:
        #Số lượng thiệp cần tạo tối thiểu
        c1=random.randint(10,20)

        #Số giờ làm 2 loại thiệp
        a2=random.randint(2,8)
        b2=random.randint(3,8)


        #Số giờ tối đa để làm thiệp
        c2=random.randint(20,40)

        #Giao của đường ngày công với các trục
        x2,y2 = c2/a2, c2/b2
        if all([x2<c1, y2>c1, c2%a2==0,c2%b2==0]):
            break
    #Giá tiền mỗi loại
    n=random.randint(8,15)
    m=n+random.randint(5,15)
    
    

    #Giải hệ giao điểm 
    eq1=Eq(x + y , c1)
    eq2=Eq(a2*x + b2*y , c2)
    sol = solve((eq1, eq2), (x, y))
    if sol:
        x_0, y_0 = sol[x], sol[y]    


    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(x + y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        x + y - c1 >= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$({phan_so(pt[x])}, {phan_so(pt[y])}) \\Rightarrow F = {phan_so(m*pt[x] + n*pt[y])}$\n\n"
 

    t=best_Z.is_integer
    if t:
        dap_an=best_Z
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        noi_dung+=f" (kết quả làm tròn đến hàng phần mười)"
    
    
        
    ten=random.choice(["An", "Minh", "Hoa", "Nam", "Lan", 
 "Bình", "Hương", "Phúc", "Mai", "Khôi"])

    chon=random.randint(1,3)
    
    if chon==1:
        vat_1, vat_2="tấm thiệp loại lớn"  ,"tấm thiệp loại nhỏ"   
        ten_chung="tấm thiệp"
    
    if chon==2:
        vat_1, vat_2="bao lì xì đặc biệt"  ,"bao lì xì thường"
        ten_chung="bao lì xì"

    if chon==3:
        vat_1, vat_2="dây loại cầu kỳ", "dây loại đơn giản",         
        ten_chung="dây trang trí"

    noi_dung = (
    f"Bạn {ten} dự định làm thủ công các {ten_chung} để bán trong một hội chợ Tết."
    f" Cần {a2} giờ để làm một {vat_1} có giá {m} nghìn đồng và {b2} giờ để làm một {vat_2} có giá {n} nghìn đồng."
    f" Bạn {ten} chỉ có {c2} giờ để làm các {ten_chung} và ban tổ chức hội chợ yêu cầu phải làm ít nhất {c1} {ten_chung}."
    f" Tìm số tiền mà bạn {ten} có thể thu được nhiều nhất khi bán hết các {ten_chung}."
    )

    f=m*x+n*y
    f_A=int(f.subs({x: 0, y: c1}))
    f_B=int(f.subs({x: x_0, y: y_0}))
    f_C=int(f.subs({x: 0, y: int(c2/b2)}))
    
    noi_dung_loigiai=(
    f"Gọi ${{x,y}}$ là số lượng {vat_1} và {vat_2}.\n\n"
   f"$x\\ge 0,y \\ge 0$.\n\n"
   f"Số lượng {ten_chung} cần làm: $x+y \\ge {c1}$.\n\n"
   f"Số giờ cần dùng: ${a2}x+{b2}y \\le {c2}$.\n\n"
   f"Miền nghiệm của hệ điều kiện là tam giác ${{ABC}}$"
   f" với $A(0;{c1}),B({phan_so(x_0)};{phan_so(y_0)}),C(0;{int(c2/b2)})$.\n\n"
   f"{st}\n\n"
   f"Số tiền thu được: $F={m}x+{n}y$.\n\n"
   f"Số tiền thu về lớn nhất khi:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$."
    f"Số tiền thu về lớn nhất là {dap_an} ngàn đồng."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_21]-TF-M3. Trồng 2 loại cây. Xét Đ-S: Diện tích đất, điều kiện, lợi nhuận max
def bch_12_L10_C2_B2_21():
    x,y=sp.symbols("x y")
    chon=random.randint(1,3)
    if chon==1:
        ngo,dauxanh="ngô", "đậu xanh"
        m,n=random.randint(3,5),random.randint(5,8)
    
    if chon==2:
        ngo,dauxanh="lúa", "khoai lang"
        m,n=random.randint(3,6),random.randint(4,8)

    if chon==3:
        ngo,dauxanh="cà chua", "dưa leo"
        m,n=random.randint(5,10),random.randint(4,8)
    
    
    while True:
        c1=random.randint(4,12)
        c2=random.randint(20,40)
        a2=random.randint(3,8)
        b2=random.randint(3,8)
        #Giao của đường ngày công với các trục
        x2,y2 = c2/a2, c2/b2
        if all([x2>c1, y2<c1, c2%a2==0,c2%b2==0]):
            break
    #Giải hệ giao điểm 
    eq1=Eq(x + y , c1)
    eq2=Eq(a2*x + b2*y , c2)
    sol = solve((eq1, eq2), (x, y))
    if sol:
        x_0, y_0 = sol[x], sol[y]
    f=m*x+n*y
    f_A=int(f.subs({x: 0, y: y2}))
    f_B=int(f.subs({x: x_0, y: y_0}))
    f_C=int(f.subs({x: c1, y: 0}))


    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(x + y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        x + y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$({phan_so(pt[x])}, {phan_so(pt[y])}) \\Rightarrow F = {phan_so(m*pt[x] + n*pt[y])}$\n\n"
    

    nguoi=random.choice(["Bác Nam", "Ông An", "Chú Minh", "Bác Hùng", "Ông Lâm", 
    "Chú Quang", "Bác Tín", "Ông Phúc", "Chú Hải", "Bác Sơn" ])

    t=best_Z.is_integer
    if t:
        dap_an=best_Z
        dap_an_f=best_Z+random.randint(1,5)
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        dap_an_f=f"{round_half_up(best_Z+random.randint(1,5),1):.1f}".replace(".",",")
        

    noi_dung = (f"{nguoi} dự định trồng {ngo} và {dauxanh} trên một mảnh đất có diện tích {c1} sào."
        f" Nếu trồng 1 sào {ngo} thì cần {a2} ngày công và thu được {m} triệu đồng."
        f" Nếu trồng 1 sào {dauxanh} thì cần {b2} ngày công và thu được {n} triệu đồng."
        f" Tổng số ngày công mà {nguoi} có thể sử dụng không quá {c2} ngày công."
        f" Gọi ${{x, y}}$ lần lượt là diện tích đất trồng {ngo} và {dauxanh} (đơn vị: sào)."
        f" Xét tính đúng-sai của các khẳng định sau:"
    )    
    
    kq1_T=f"* Tổng diện tích đất cần dùng là $x+y$" 
    kq1_F=f" Tổng diện tích đất cần dùng là ${a2}x+{b2}y$"
    
    HDG=f"Tổng diện tích đất cần dùng là $x+y$"
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* $x+y \\le {c1}$"
    kq2_F=f"$x+y \\le {c1}$"
    
    HDG=f"$x+y \\le {c1}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"*  ${a2}x+{b2}y \\le {c2}$" 
    kq3_F=f"${a2}x+{b2}y \\ge {c2}$"
    
    HDG=f"${a2}x+{b2}y \\le {c2}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Lợi nhuận lớn nhất thu được là {dap_an} triệu đồng"
    kq4_F=f"Lợi nhuận lớn nhất thu được là {dap_an_f} triệu đồng" 
    
    HDG=(f"Gọi ${{x,y}}$ là diện tích đất để trồng {ngo} và {dauxanh}.\n\n"
        f"$x\\ge 0,y \\ge 0$.\n\n"
        f"Diện tích đất cần dùng: $x+y \\le {c1}$.\n\n"
        f"Số ngày công cần dùng: ${a2}x+{b2}y \\le {c2}$.\n\n"
        f"Miền nghiệm của hệ điều kiện là tứ giác ${{OABC}}$"
        f"với $O(0;0),A(0;{int(y2)}),B({phan_so(x_0)};{phan_so(y_0)}),C({c1};0)$.\n\n"
        #f" Các đỉnh của miền nghiệm:\n\n {st}\n\n"
        f"Lợi nhuận thu được: $F={m}x+{n}y$.\n\n"
        f"$F(0;0)=0, F(0;{int(y2)})={f_A}, F({phan_so(x_0)};{phan_so(y_0)})={f_B}, F({c1};0)={f_C}$.\n\n"
        f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n"
        f" Lợi nhuận lớn nhất: F = {dap_an} triệu đồng.")
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

#[D10_C2_B2_22]-TF-M3. Làm 2 đồ vật bán chợ Tết. Xét Đ-S: hệ điều kiện, lợi nhuận max
def bch_12_L10_C2_B2_22():

    x,y=sp.symbols("x y")
    while True:
       #Số lượng thiệp cần tạo tối thiểu
       c1=random.randint(10,20)

       #Số giờ làm 2 loại thiệp
       a2=random.randint(2,8)
       b2=random.randint(3,8)


       #Số giờ tối đa để làm thiệp
       c2=random.randint(20,40)

       #Giao của đường ngày công với các trục
       x2,y2 = c2/a2, c2/b2
       if all([x2<c1, y2>c1, c2%a2==0,c2%b2==0]):
           break
    #Giá tiền mỗi loại
    n=random.randint(8,15)
    m=n+random.randint(5,15)



    #Giải hệ giao điểm 
    eq1=Eq(x + y , c1)
    eq2=Eq(a2*x + b2*y , c2)
    sol = solve((eq1, eq2), (x, y))
    if sol:
       x_0, y_0 = sol[x], sol[y]    


    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
       Eq(x + y , c1),
       Eq(a2*x + b2*y , c2),
       Eq(x, 0),
       Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    # Ràng buộc dưới dạng bất phương trình
    constraints = [
       x + y - c1 >= 0,
       a2*x + b2*y - c2 <= 0,
       x >= 0,
       y >= 0
    ]

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
       sol = solve((eq1, eq2), (x, y), dict=True)
       if sol:
           pt = sol[0]
           # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
           if all(ineq.subs(pt) for ineq in constraints):
               vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
       Z = m * pt[x] + n * pt[y]
       if Z > best_Z:
           best_Z = Z
           best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
       st+=f"$F ({phan_so(pt[x])}, {phan_so(pt[y])}) = {phan_so(m*pt[x] + n*pt[y])}$\n\n"


    t=best_Z.is_integer
    if t:
       dap_an=best_Z
    else:
       dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
       noi_dung+=f" (kết quả làm tròn đến hàng phần mười)"


       
    ten=random.choice(["An", "Minh", "Hoa", "Nam", "Lan", "Bình", "Hương", "Phúc", "Mai", "Khôi"])

    chon=random.randint(1,3)
   
    if chon==1:
       vat_1, vat_2="tấm thiệp loại lớn"  ,"tấm thiệp loại nhỏ"   
       ten_chung="tấm thiệp"

    if chon==2:
       vat_1, vat_2="bao lì xì đặc biệt"  ,"bao lì xì thường"
       ten_chung="bao lì xì"

    if chon==3:
       vat_1, vat_2="dây loại cầu kỳ", "dây loại đơn giản",         
       ten_chung="dây trang trí"


    f=m*x+n*y
    f_A=int(f.subs({x: 0, y: c1}))
    f_B=int(f.subs({x: x_0, y: y_0}))
    f_C=int(f.subs({x: 0, y: int(c2/b2)}))
   


    noi_dung = (    f"Bạn {ten} dự định làm thủ công các {ten_chung} để bán trong một hội chợ Tết."
    f" Cần {a2} giờ để làm một {vat_1} có giá {m} nghìn đồng và {b2} giờ để làm một {vat_2} có giá {n} nghìn đồng."
    f" Bạn {ten} chỉ có {c2} giờ để làm các {ten_chung} và ban tổ chức hội chợ yêu cầu phải làm ít nhất {c1} {ten_chung}."
    f" Gọi ${{x,y}}$ lần lượt là số lượng {vat_1} và {vat_2}."  
    f" Xét tính đúng-sai của các khẳng định sau. "
    )    
    
    kq1_T=f"* $x+y \\ge {c1}$" 
    kq1_F=f" $x+y \\le {c1}$"
    
    HDG=f"$x+y \\ge {c1}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*  ${a2}x+{b2}y \\le {c2}$"
    kq2_F=f" ${a2}x+{b2}y \\ge {c2}$"
    
    HDG=f"${a2}x+{b2}y \\le {c2}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Với $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$ thì số tiền thu về là lớn nhất" 
    kq3_F=f"Với $x = {phan_so(best_point[x]+random.randint(1,2))}, y = {phan_so(best_point[y]+random.randint(1,2))}$ thì số tiền thu về là lớn nhất"
    
    HDG=(f"Gọi ${{x,y}}$ là số lượng {vat_1} và {vat_2}.\n\n"
   f"$x\\ge 0,y \\ge 0$.\n\n"
   f"Số lượng {ten_chung} cần làm: $x+y \\ge {c1}$.\n\n"
   f"Số giờ cần dùng: ${a2}x+{b2}y \\le {c2}$.\n\n"
   f"Miền nghiệm của hệ điều kiện là tam giác ${{ABC}}$"
   f" với $A(0;{c1}),B({phan_so(x_0)};{phan_so(y_0)}),C(0;{int(c2/b2)})$.\n\n"
   f"{st}\n\n"
   f"Lợi nhuận thu được: $F={m}x+{n}y$.\n\n"
   f"Số tiền thu về lớn nhất khi:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Số tiền có thể thu về được nhiều nhất khi bán hết các {ten_chung} là {dap_an} ngàn đồng"
    kq4_F=f"Số tiền có thể thu về được nhiều nhất khi bán hết các {ten_chung} là {dap_an+random.randint(4,10)} ngàn đồng" 
    
    HDG=f"Số tiền có thể thu về được nhiều nhất: F({phan_so(best_point[x])},{phan_so(best_point[y])}) = {dap_an} ngàn đồng."
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

#[D10_C2_B2_23]-TF-M3. Sản xuất bằng 2 máy. Xét Đ-S: hệ điều kiện, lợi nhuận max
def bch_12_L10_C2_B2_23():
    x,y=symbols("x y")
    X, Y ="X", "Y"
    A, B ="A", "B"
    while True:

        #Hệ số thời gian cho máy A
        a1=random.randint(1,6)
        b1=random.randint(1,4)
        c1=random.randint(7,12)

        #Hệ số thời gian cho máy B
        a2=random.randint(1,6)
        b2=random.randint(1,4)
        c2=random.randint(7,10)

        x_1, x_2 = c1/a1, c2/a2
        y_1, y_2 = c1/b1, c2/b2
        if all([x_2 > x_1, y_1>y_2]):
            break
    while True:
        m=random.randint(2,10)
        n=random.randint(2,10)
        if m!=n:
            break
    f1=a1*x+b1*y-c1
    f2=a2*x+b2*y-c2
    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a1*x+b1*y)}\\le {c1} \\\\ \n\
    {latex(a2*x+b2*y)}\\le {c2} \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."
    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        a1*x + b1*y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(a1*x + b1*y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$T({phan_so(pt[x])}, {phan_so(pt[y])}) = {phan_so(m*pt[x] + n*pt[y])}$\n\n"


    t=best_Z .is_integer
    if t:
        dap_an=best_Z
        dap_an_f=best_Z+random.randint(1,5)
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        dap_an_f=f"{round_half_up(best_Z+random.randint(1,5),1):.1f}".replace(".",",")

    noi_dung = (
    f"Một xưởng sản xuất có hai máy đặc chủng là máy {A} và máy {B} để sản xuất hai loại sản phẩm {X} và {Y}."
    f" Để sản xuất 1 tấn sản phẩm loại {X} cần dùng máy {A} trong {a1} giờ và dùng máy {B} trong {a2} giờ."
    f" Để sản xuất 1 tấn sản phẩm loại {Y} cần dùng máy {A} trong {b1} giờ và dùng máy {B} trong {b2} giờ."
    f" Cho biết mỗi máy không thể sản xuất đồng thời hai loại sản phẩm."
    f" Máy {A} làm việc không quá {c1} giờ một ngày, máy {B} làm việc không quá {c2} giờ một ngày."
    f" Một cái {X} lãi {m} triệu đồng và một sản phẩm loại {Y} lãi {n} triệu đồng."
    f" Gọi ${{x,y}}$ lần lượt là số tấn sản phẩm loại {X} và loại {Y} cần sản xuất."
    f" Xét tính đúng-sai của các khẳng định sau:"
    )    
    
    kq1_T=f"* ${latex(a1*x + b1*y - c1)} \\le 0$" 
    kq1_F=f"${latex(a1*x + b1*y - c1)} \\ge 0$"
    
    HDG=f"Thời gian để máy {A} làm việc: ${latex(a1*x + b1*y - c1)} \\le 0$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* ${latex(a2*x + b2*y - c2)} \\le 0$"
    kq2_F=f"${latex(a2*x + b2*y - c2)} \\ge 0$"
    
    HDG=f"Thời gian để máy {B} làm việc: ${latex(a2*x + b2*y - c2)} \\le 0$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Với $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$ thì lợi nhuận thu được là lớn nhất" 
    kq3_F=f"Với $x = {phan_so(best_point[x]+random.randint(1,2))}, y = {phan_so(best_point[y]+random.randint(1,2))}$ thì lợi nhuận thu được là lớn nhất"
    
    HDG=(f"Gọi ${{x}}$, ${{y}}$ là số tấn sản phẩm loại ${{{X}}}$, ${{{Y}}}$ cần sản xuất ($ x,y\\ge 0 $).\n\n"
    f"Thời gian để máy {A} làm việc: ${latex(a1*x+b1*y)} \\le {c1}$.\n\n"
    f"Thời gian để máy {B} làm việc: ${latex(a2*x+b2*y)} \\le {c2}$.\n\n"
    f"Ta có hệ điều kiện:\n\n"
    f"${hedk}$.\n\n"
    f"Lợi nhuận thu được: $T={latex(m*x+n*y)}$.\n\n"
    f" Lợi nhuận tại các đỉnh của miền nghiệm:\n\n {st}\n\n"
    f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Lợi nhuận lớn nhất đạt được là {dap_an} triệu đồng"
    kq4_F=f"Lợi nhuận lớn nhất đạt được là {dap_an_f} triệu đồng " 
    
    HDG=f"Lợi nhuận lớn nhất đạt được là $F({phan_so(best_point[x])},{phan_so(best_point[y])})={dap_an}$ triệu đồng."
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

#[D10_C2_B2_24]-TF-M3. Sản xuất bàn và ghế. Xét Đ-S: hệ điều kiện, lợi nhuận max
def bch_12_L10_C2_B2_24():
    x,y=symbols("x y")

    X = "bàn học sinh"
    Y = "ghế gỗ"
    A = "cưa gỗ tự động"
    B = "đánh bóng bề mặt" 

    while True:
        while True:
            m=random.randint(100,150)
            n=random.randint(70,90)
            if m!=n:
                break

        #Hệ số thời gian cho máy A
        a1=random.randint(1,4)
        b1=random.randint(1,4)
        c1=random.randint(8,12)

        #Hệ số thời gian cho máy B
        a2=random.randint(1,4)
        b2=random.randint(1,4)
        c2=random.randint(8,12)

        x_1, x_2 = c1/a1, c2/a2
        y_1, y_2 = c1/b1, c2/b2

        if a1*b2-a2*b1==0:
            continue

        #Giải hệ giao điểm 
        eq1=Eq(a1*x + b1*y , c1)
        eq2=Eq(a2*x + b2*y , c2)
        sol = solve((eq1, eq2), (x, y))
        if sol:
            x_0, y_0 = sol[x], sol[y]

        constraints = [
            a1*x + b1*y - c1 <= 0,
            a2*x + b2*y - c2 <= 0,
            x >= 0,
            y >= 0
        ]

        # Các đường biên để tìm giao điểm (dưới dạng phương trình)
        lines = [
            Eq(a1*x + b1*y , c1),
            Eq(a2*x + b2*y , c2),
            Eq(x, 0),
            Eq(y, 0)
        ]

        # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
        from itertools import combinations

        vertices = []
        for eq1, eq2 in combinations(lines, 2):
            sol = solve((eq1, eq2), (x, y), dict=True)
            if sol:
                pt = sol[0]
                # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
                if all(ineq.subs(pt) for ineq in constraints):
                    vertices.append(pt)

        # Tính giá trị hàm mục tiêu tại các đỉnh
        best_Z = -float('inf')
        best_point = None

        for pt in vertices:
            Z = m * pt[x] + n * pt[y]
            if Z > best_Z:
                best_Z = Z
                best_point = pt

        if all([x_2 > x_1, y_1>y_2, c1%a1==0, c2%a2==0, c1%b1==0, c2%b2==0, x_0.is_integer, y_0.is_integer]):
            break

    f1=a1*x+b1*y-c1
    f2=a2*x+b2*y-c2
    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a1*x+b1*y)}\\le {c1} \\\\ \n\
    {latex(a2*x+b2*y)}\\le {c2} \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."
    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        a1*x + b1*y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(a1*x + b1*y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$T({phan_so(pt[x])}, {phan_so(pt[y])}) = {phan_so(m*pt[x] + n*pt[y])}$\n\n"


    t=best_Z .is_integer
    if t:
        dap_an=best_Z
        dap_an_f=best_Z+random.randint(1,5)
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        dap_an_f=f"{round_half_up(best_Z+random.randint(1,5),1):.1f}".replace(".",",")


    noi_dung = (
    f"Một xưởng sản xuất có hai loại máy là máy {A} và máy {B} để sản xuất hai loại sản phẩm {X} và {Y}."
    f" Để sản xuất 1 cái {X} cần dùng máy {A} trong {a1} giờ và dùng máy {B} trong {a2} giờ."
    f" Để sản xuất 1 cái {Y} cần dùng máy {A} trong {b1} giờ và dùng máy {B} trong {b2} giờ."
    f" Cho biết mỗi máy không thể sản xuất đồng thời hai loại sản phẩm."
    f" Máy {A} làm việc không quá {c1} giờ một ngày, máy {B} làm việc không quá {c2} giờ một ngày."
    f" Một cái {X} lãi {m} ngàn đồng và một cái {Y} lãi {n} ngàn đồng."
    f" Gọi ${{x}}$, ${{y}}$ lần lượt là số cái {X} và {Y} cần sản xuất."
    f" Xét tính đúng-sai của các khẳng định sau:"
    )    
    
    kq1_T=f"* ${latex(a1*x + b1*y - c1)} \\le 0$" 
    kq1_F=f"${latex(a1*x + b1*y - c1)} \\ge 0$"
    
    HDG=f"Thời gian để máy {A} làm việc: ${latex(a1*x + b1*y - c1)} \\le 0$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* ${latex(a2*x + b2*y - c2)} \\le 0$"
    kq2_F=f"${latex(a2*x + b2*y - c2)} \\ge 0$"
    
    HDG=f"Thời gian để máy {B} làm việc: ${latex(a2*x + b2*y - c2)} \\le 0$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Với $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$ thì lợi nhuận thu được là lớn nhất" 
    kq3_F=f"Với $x = {phan_so(best_point[x]+random.randint(1,2))}, y = {phan_so(best_point[y]+random.randint(1,2))}$ thì lợi nhuận thu được là lớn nhất"
    
    HDG=(f"Gọi ${{x}}$, ${{y}}$ lần lượt là số cái {X} và {Y} cần sản xuất ($ x,y\\ge 0 $).\n\n"
    f"Thời gian để máy {A} làm việc: ${latex(a1*x+b1*y)} \\le {c1}$.\n\n"
    f"Thời gian để máy {B} làm việc: ${latex(a2*x+b2*y)} \\le {c2}$.\n\n"
    f"Ta có hệ điều kiện:\n\n"
    f"${hedk}$.\n\n"
    f"Lợi nhuận thu được: $T={latex(m*x+n*y)}$.\n\n"
    f" Lợi nhuận tại các đỉnh của miền nghiệm:\n\n {st}\n\n"
    f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Lợi nhuận lớn nhất đạt được là {dap_an} ngàn đồng"
    kq4_F=f"Lợi nhuận lớn nhất đạt được là {dap_an_f} ngàn đồng " 
    
    HDG=f"Lợi nhuận lớn nhất đạt được là $F({phan_so(best_point[x])},{phan_so(best_point[y])})={dap_an}$ ngàn đồng."
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

#[D10_C2_B2_25]-TF-M3. Sản xuất áo và quần. Xét Đ-S: hệ điều kiện, lợi nhuận max
def bch_12_L10_C2_B2_25():
    x,y=symbols("x y")
    chon=random.randint(1,4)
    chon=2
    
    if chon==2:
        X = "áo sơ mi nam"
        Y = "quần tây nữ"
        A = "cắt vải CNC"
        B = "may công nghiệp"

    if chon==3:
        X = "khung xe đạp"
        Y = "tay lái xe máy"
        A = "hàn tự động"
        B = "phay CNC"

    if chon==4:
        X = "bình hoa sứ"
        Y = "tô sứ cao cấp"
        A = "tạo hình khuôn"
        B = "nung điện công nghiệp"



    while True:
        while True:
            m=random.randint(80,120)
            n=random.randint(80,120)
            if m!=n:
                break

        #Hệ số thời gian cho máy A
        a1=random.randint(1,5)
        b1=random.randint(1,4)
        c1=random.randint(8,12)

        #Hệ số thời gian cho máy B
        a2=random.randint(1,4)
        b2=random.randint(1,4)
        c2=random.randint(8,12)

        x_1, x_2 = c1/a1, c2/a2
        y_1, y_2 = c1/b1, c2/b2

        if a1*b2-a2*b1==0:
            continue

        #Giải hệ giao điểm 
        eq1=Eq(a1*x + b1*y , c1)
        eq2=Eq(a2*x + b2*y , c2)
        sol = solve((eq1, eq2), (x, y))
        if sol:
            x_0, y_0 = sol[x], sol[y]

        constraints = [
            a1*x + b1*y - c1 <= 0,
            a2*x + b2*y - c2 <= 0,
            x >= 0,
            y >= 0
        ]

        # Các đường biên để tìm giao điểm (dưới dạng phương trình)
        lines = [
            Eq(a1*x + b1*y , c1),
            Eq(a2*x + b2*y , c2),
            Eq(x, 0),
            Eq(y, 0)
        ]

        # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
        from itertools import combinations

        vertices = []
        for eq1, eq2 in combinations(lines, 2):
            sol = solve((eq1, eq2), (x, y), dict=True)
            if sol:
                pt = sol[0]
                # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
                if all(ineq.subs(pt) for ineq in constraints):
                    vertices.append(pt)

        # Tính giá trị hàm mục tiêu tại các đỉnh
        best_Z = -float('inf')
        best_point = None

        for pt in vertices:
            Z = m * pt[x] + n * pt[y]
            if Z > best_Z:
                best_Z = Z
                best_point = pt

        if all([x_2 > x_1, y_1>y_2, c1%a1==0, c2%a2==0, c1%b1==0, c2%b2==0, x_0.is_integer, y_0.is_integer]):
            break

    f1=a1*x+b1*y-c1
    f2=a2*x+b2*y-c2
    hedk=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a1*x+b1*y)}\\le {c1} \\\\ \n\
    {latex(a2*x+b2*y)}\\le {c2} \\\\ \n\
    x \\ge 0 \\\\ \n\
    y \\ge 0 \n\
    \\end{{array}} \\right."
    # Ràng buộc dưới dạng bất phương trình
    constraints = [
        a1*x + b1*y - c1 <= 0,
        a2*x + b2*y - c2 <= 0,
        x >= 0,
        y >= 0
    ]

    # Các đường biên để tìm giao điểm (dưới dạng phương trình)
    lines = [
        Eq(a1*x + b1*y , c1),
        Eq(a2*x + b2*y , c2),
        Eq(x, 0),
        Eq(y, 0)
    ]

    # Tìm tất cả giao điểm 2-2 của các đường để xét đỉnh miền nghiệm
    from itertools import combinations

    vertices = []
    for eq1, eq2 in combinations(lines, 2):
        sol = solve((eq1, eq2), (x, y), dict=True)
        if sol:
            pt = sol[0]
            # Kiểm tra điểm có thỏa mãn tất cả ràng buộc không
            if all(ineq.subs(pt) for ineq in constraints):
                vertices.append(pt)

    # Tính giá trị hàm mục tiêu tại các đỉnh
    best_Z = -float('inf')
    best_point = None

    for pt in vertices:
        Z = m * pt[x] + n * pt[y]
        if Z > best_Z:
            best_Z = Z
            best_point = pt

    

    # Kết quả
    st=""
    for pt in vertices:
        st+=f"$T({phan_so(pt[x])}, {phan_so(pt[y])}) = {phan_so(m*pt[x] + n*pt[y])}$\n\n"


    t=best_Z .is_integer
    if t:
        dap_an=best_Z
        dap_an_f=best_Z+random.randint(1,5)
    else:
        dap_an=f"{round_half_up(best_Z,1):.1f}".replace(".",",")
        dap_an_f=f"{round_half_up(best_Z+random.randint(1,5),1):.1f}".replace(".",",")

    noi_dung = (
    f"Một công ty may mặc có hai loại máy là máy {A} và máy {B} để sản xuất hai loại sản phẩm {X} và {Y}."
    f" Để sản xuất 1 cái {X} cần dùng máy {A} trong {a1} giờ và dùng máy {B} trong {a2} giờ."
    f" Để sản xuất 1 cái {Y} cần dùng máy {A} trong {b1} giờ và dùng máy {B} trong {b2} giờ."
    f" Cho biết mỗi máy không thể sản xuất đồng thời hai loại sản phẩm."
    f" Máy {A} làm việc không quá {c1} giờ một ngày, máy {B} làm việc không quá {c2} giờ một ngày."
    f" Một cái {X} lãi {m} ngàn đồng và một cái {Y} lãi {n} ngàn đồng."
    f" Gọi $x$, $y$ lần lượt là số cái {X} và {Y} cần sản xuất."
    f" Xét tính đúng-sai của các khẳng định sau:"
    )    
    
    kq1_T=f"* ${latex(a1*x + b1*y - c1)} \\le 0$" 
    kq1_F=f"${latex(a1*x + b1*y - c1)} \\ge 0$"
    
    HDG=f"Thời gian để máy {A} làm việc: ${latex(a1*x + b1*y - c1)} \\le 0$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* ${latex(a2*x + b2*y - c2)} \\le 0$"
    kq2_F=f"${latex(a2*x + b2*y - c2)} \\ge 0$"
    
    HDG=f"Thời gian để máy {B} làm việc: ${latex(a2*x + b2*y - c2)} \\le 0$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Với $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$ thì lợi nhuận thu được là lớn nhất" 
    kq3_F=f"Với $x = {phan_so(best_point[x]+random.randint(1,2))}, y = {phan_so(best_point[y]+random.randint(1,2))}$ thì lợi nhuận thu được là lớn nhất"
    
    HDG=(f"Gọi ${{x}}$, ${{y}}$ lần lượt là số cái {X} và {Y} cần sản xuất ($ x,y\\ge 0 $).\n\n"
    f"Thời gian để máy {A} làm việc: ${latex(a1*x+b1*y)} \\le {c1}$.\n\n"
    f"Thời gian để máy {B} làm việc: ${latex(a2*x+b2*y)} \\le {c2}$.\n\n"
    f"Ta có hệ điều kiện:\n\n"
    f"${hedk}$.\n\n"
    f"Lợi nhuận thu được: $T={latex(m*x+n*y)}$.\n\n"
    f" Lợi nhuận tại các đỉnh của miền nghiệm:\n\n {st}\n\n"
    f" Điểm thỏa mãn lợi nhuận lớn nhất:  $x = {phan_so(best_point[x])}, y = {phan_so(best_point[y])}$\n\n")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Lợi nhuận lớn nhất đạt được là {dap_an} ngàn đồng"
    kq4_F=f"Lợi nhuận lớn nhất đạt được là {dap_an_f} ngàn đồng " 
    
    HDG=f"Lợi nhuận lớn nhất đạt được là $F({phan_so(best_point[x])},{phan_so(best_point[y])})={dap_an}$ ngàn đồng."
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

#[D10_C2_B2_26]-SA-M2. Cho miền đa giác. Tìm giá trị lớn nhất hoặc nhỏ nhất.
def bch_12_L10_C2_B2_26():
    x,y=sp.symbols("x y")
    while True:
        x_A,x_B,x_C,x_D=[random.randint(-5,5) for _ in range(4)]
        y_A,y_B,y_C,y_D=[random.randint(-5,5) for _ in range(4)]
        if all([x_A<x_B<x_C<x_D,y_B<y_A<=y_D<y_C]):
            break
    x_min,x_max=min(x_A,x_B,x_C,x_D)-1,max(x_A,x_B,x_C,x_D)+1
    y_min,y_max=min(y_A,y_B,y_C,y_D)-1,max(y_A,y_B,y_C,y_D)+1
    if x_min>=0:
        x_min=-1
    if y_min>=0:
        y_min=-1
    m,n=random.sample([i for i in range(-5,6) if i!=0],2)
    f=m*x+n*y
    F_A=f.subs({x:x_A, y:y_A})
    F_B=f.subs({x:x_B, y:y_B})
    F_C=f.subs({x:x_C, y:y_C})
    F_D=f.subs({x:x_D, y:y_D})
    max_F=max(F_A,F_B,F_C,F_D)
    min_F=min(F_A,F_B,F_C,F_D)
    so_truc_x=tao_chuoi_so_nguyen(int(x_min), int(x_max))
    so_truc_y=tao_chuoi_so_nguyen(int(y_min), int(y_max) )

    code_hinh=(

    f" \\begin{{tikzpicture}}[scale=1]\n\
    % Vẽ lưới\n\
    \\draw [gray!50,thin] ({x_min},{y_min}) grid ({x_max},{y_max});\n\
    % Vẽ trục tọa độ\n\
    \\draw[->,thick] ({x_min},0) -- ({x_max},0) node[below] {{$x$}};\n\
    \\draw[->,thick] (0,{y_min}) -- (0,{y_max}) node[left] {{$y$}};\n\
    \n\
    % Đặt tên gốc O\n\
    \\node[below left] at (0,0) {{$O$}};\n\
    \n\
    % Đánh số trên trục x\n\
    \\foreach \\x in {{{so_truc_x}}}\n\
    \\node[below] at (\\x,0) {{\\x}};\n\
    \n\
    % Đánh số trên trục y\n\
    \\foreach \\y in {{{so_truc_y}}}\n\
    \\node[left] at (0,\\y) {{\\y}};\n\
    \n\
    % Vẽ và tô miền đa giác\n\
    \\filldraw[pattern=north east lines,pattern color=blue,draw=black,thick] \n\
    ({x_A},{y_A}) -- ({x_B},{y_B}) -- ({x_D},{y_D})-- ({x_C},{y_C}) -- cycle;\n\
    \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    chon=random.randint(1,2)
    if chon==1:
        noi_dung = (
        f"Tìm giá trị lớn nhất của biểu thức $F={latex(m*x+n*y)}$ với $(x;y)$ là các điểm thuộc miền tứ giác như hình vẽ.")
        dap_an=max_F

        noi_dung_loigiai=(
        f"$F({x_A};{y_A})={F_A},F({x_B};{y_B})={F_B},F({x_C};{y_C})={F_C},F({x_D};{y_D})={F_D}$.\n\n"
        f"Giá trị lớn nhất là ${{{max_F}}}$.")  
    
    if chon==2:
        noi_dung = (
        f"Tìm giá trị nhỏ nhất của biểu thức $F={latex(m*x+n*y)}$ với $(x;y)$ là các điểm thuộc miền tứ giác như hình vẽ.")
        dap_an=max_F

        noi_dung_loigiai=(
        f"$F({x_A};{y_A})={F_A},F({x_B};{y_B})={F_B},F({x_C};{y_C})={F_C},F({x_D};{y_D})={F_D}$.\n\n"
        f"Giá trị nhỏ nhất là ${{{max_F}}}$.")  

  
        
    debai_word= f"{noi_dung}\n{file_name}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C2_B2_27]-M2. Cho miền đa giác. Tìm khẳng định đúng về F(x;y)
def bch_12_L10_C2_B2_27():
    x,y=sp.symbols("x y")
    while True:
        x_A,x_B,x_C,x_D=[random.randint(-4,5) for _ in range(4)]
        y_A,y_B,y_C,y_D=[random.randint(-4,5) for _ in range(4)]
        if all([x_A<x_B<x_D<x_C,y_B<y_A<y_C<y_D]):
            break
    x_min,x_max=min(x_A,x_B,x_C,x_D)-1,max(x_A,x_B,x_C,x_D)+1
    y_min,y_max=min(y_A,y_B,y_C,y_D)-1,max(y_A,y_B,y_C,y_D)+1
    if x_min>=0:
        x_min=-1
    if y_min>=0:
        y_min=-1
    m,n=random.sample([i for i in range(-5,6) if i!=0],2)
    f=m*x+n*y
    F_A=f.subs({x:x_A, y:y_A})
    F_B=f.subs({x:x_B, y:y_B})
    F_C=f.subs({x:x_C, y:y_C})
    F_D=f.subs({x:x_D, y:y_D})
    max_F=max(F_A,F_B,F_C,F_D)
    min_F=min(F_A,F_B,F_C,F_D)
    so_truc_x=tao_chuoi_so_nguyen(int(x_min), int(x_max))
    so_truc_y=tao_chuoi_so_nguyen(int(y_min), int(y_max) )

    code_hinh=(

    f" \\begin{{tikzpicture}}[scale=1]\n\
    % Vẽ lưới\n\
    \\draw [gray!50,thin] ({x_min},{y_min}) grid ({x_max},{y_max});\n\
    % Vẽ trục tọa độ\n\
    \\draw[->,thick] ({x_min},0) -- ({x_max},0) node[below] {{$x$}};\n\
    \\draw[->,thick] (0,{y_min}) -- (0,{y_max}) node[left] {{$y$}};\n\
    \n\
    % Đặt tên gốc O\n\
    \\node[below left] at (0,0) {{$O$}};\n\
    \n\
    % Đánh số trên trục x\n\
    \\foreach \\x in {{{so_truc_x}}}\n\
    \\node[below] at (\\x,0) {{\\x}};\n\
    \n\
    % Đánh số trên trục y\n\
    \\foreach \\y in {{{so_truc_y}}}\n\
    \\node[left] at (0,\\y) {{\\y}};\n\
    \n\
    % Vẽ và tô miền đa giác\n\
    %\\filldraw[pattern=north east lines,pattern color=blue,draw=black,thick] \n\
    \\draw[-, very thick, color=blue]({x_A},{y_A}) -- ({x_B},{y_B}) -- ({x_C},{y_C})-- ({x_D},{y_D}) -- cycle;\n\
    \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)   
    #file_name=""
    

    noi_dung = (
    f"Cho biểu thức $F={latex(m*x+n*y)}$ với $(x;y)$ là các điểm thuộc miền trong hình tứ giác như hình vẽ."
    f" Tìm khẳng định đúng.")    
    

    kq=random.choice([
        f"$F({x_A};{y_A})={F_A}$",
        f"$F({x_B};{y_B})={F_B}$",
        f"$F({x_C};{y_C})={F_C}$",
        f"$F({x_D};{y_D})={F_D}$"
        ])
    kq_false=[
    f"$F({x_A};{y_A})={F_A+random.randint(1,3)}$",
    f"$F({x_B};{y_B})={F_B-random.randint(1,5)}$",
    f"$F({x_C};{y_C})={F_C+random.randint(1,5)}$",
    f"$F({x_D};{y_D})={F_D-random.randint(1,5)}$",
    f"$F(0;0)={random.choice([random.randint(-5,-1),random.randint(1,5)])}$"]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$F({x_A};{y_A})={F_A},F({x_B};{y_B})={F_B},F({x_C};{y_C})={F_C},F({x_D};{y_D})={F_D}$.\n\n"
    f"{kq} là khẳng định đúng.")

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

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C2_B2_28]-M2. Tìm nghiệm của hệ ax+by+c>0, x>a, y<b
def bch_12_L10_C2_B2_28():
    x,y=sp.symbols("x y")
    while True:
        a=random.choice([i for i in range(-4,6) if i!=0  ])
        b=random.choice([i for i in range(-4,6) if i!=0])
        c=random.choice([i for i in range(-6,-1) if i!=0  ])
        x_1, y_1=-c/a,-c/b
        x_2=int(x_1)+random.randint(5,9)
        y_3=int(y_1)+random.randint(5,9)
        if all([x_1>0,y_1>0]):
            break
    #Tìm cặp nghiệm
    while  True:
        x_0=random.randint(0,9)
        y_0=random.randint(0,9)
        if all([a*x_0+b*y_0+c>=0,x_0>=x_2, y_0<=y_3]):
            break
    
    #Tìm cặp không là nghiệm
    no_sol = []
    while len(no_sol) < 6:
        # chọn ngẫu nhiên x,y trong khoảng [-10, 20] cho đa dạng
        m = random.randint(-10, 20)
        n = random.randint(-10, 20)
        if any([a*m+b*n+c<0,m<x_2, n>y_3]):  # không thỏa mãn hệ        
            no_sol.append((m, n))

    f=f"\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a*x+b*y+c)} \\ge 0\\\\ \n\
    x\\ge {x_2}\\\\ \n\
    y \\le {y_3}\n\
    \\end{{array}} \\right."

    noi_dung=(
    f"Cặp số nào sau đây là nghiệm của hệ bất phương trình ${f}$?"
    )
    

    kq=random.choice([f"$({x_0};{y_0})$"])
    kq_false= no_sol
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"$({x_0};{y_0})$ thỏa mãn hệ bất phương trình đã cho."
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

#[D10_C2_B2_29]-M2. Tính diện tích miền nghiệm của hệ ax+by+c>=0, x>=0, y>=0.
def bch_12_L10_C2_B2_29():
    x,y=sp.symbols("x y")
    while True:
        a=random.choice([i for i in range(-6,10) if i!=0  ])
        b=random.choice([i for i in range(-6,10) if i!=0])
        c=random.choice([i for i in range(-50,30) if i!=0  ])
        x_1, y_1=-c/a,-c/b
        if all([x_1>0,y_1>0,c>0,c%a==0,c%b==0]):
            break
    chon=random.randint(1,3)
    if chon==1:
        f=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(a*x+b*y+c)} \\ge 0\\\\ \n\
        x\\ge 0\\\\ \n\
        y \\ge 0\n\
        \\end{{array}} \\right."
    
    if chon==2:    
        f=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(a*x+b*y)} \\ge {-c}\\\\ \n\
        x\\ge 0\\\\ \n\
        y \\ge 0\n\
        \\end{{array}} \\right."

    if chon==3:    
        f=f"\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(-a*x-b*y-c)} \\le 0\\\\ \n\
        x\\ge 0\\\\ \n\
        y \\ge 0\n\
        \\end{{array}} \\right."

    noi_dung=(
    f"Tính diện tích miền nghiệm của hệ bất phương trình sau\n\n ${f}$."
    )
    S=1/2*x_1*y_1
    

    kq=S
    tap_hop= [
    x_1*y_1,
    x_1+y_1,
    2*x_1*y_1,   
    random.randint(10,60)
    ]
    kq_false=random.sample(tap_hop, 4)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"Miền nghiệm của hệ bất phương trình là tam giác ${{OAB}}$ với $A({phan_so(x_1)};0), B(0;{phan_so(y_1)})$.\n\n"
    f" Diện tích tam giác ${{OAB}}$ là: $S={phan_so(1/2)}.{phan_so(x_1)}.{phan_so(y_1)}={phan_so(S)}$."
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