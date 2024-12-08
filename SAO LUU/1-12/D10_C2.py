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
        f"Miền nghiệm của bất phương trình ${latex(a*x+b*y+d*x+e*y+h)}{random.choice([">","\\ge"])} {latex(-c+d*x+e*y+h)}$ là nửa mặt phẳng chứa điểm nào"
        ])
        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,">")[0]
        kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,">")[0:3]
    
    if chon==2:
        noi_dung=random.choice([
        f"Miền nghiệm của bất phương trình ${latex(f+d*x+e*y+h)}{random.choice(["<","\\le"])} {latex(d*x+e*y+h)}$ là nửa mặt phẳng chứa điểm nào trong các điểm sau?",
        f"Miền nghiệm của bất phương trình ${latex(a*x+b*y+d*x+e*y+h)}{random.choice([">","\\ge"])} {latex(-c+d*x+e*y+h)}$ là nửa mặt phẳng chứa điểm nào trong các điểm sau?"
        ])
        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]
        kq2,kq3,kq4=mien_not_nghiem_BPT_2an(a,b,c,"<")[0:3]

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

        not_nghiem=mien_not_nghiem_BPT_2an(a,b,c,">")[0]  

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

        cap_nghiem=mien_nghiem_BPT_2an(a,b,c,"<")[0]    
        
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

        noi_dung = f"Xét bất phương trình ${latex(f)}<0$. Xét tính đúng-sai của các khẳng định sau. "        
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
            f"Miền nghiệm là nửa mặt phẳng không chứa điểm $({x_1};{y_1})$ và không chứa đường thẳng $d:{latex(f)}=0$"
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

        kq3_T=f"*Miền nghiệm của bất phương trình không chứa đường thẳng $d:{latex(f)}=0$" 
        kq3_F=f"Miền nghiệm của bất phương trình chứa đường thẳng $d:{latex(f)}=0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Bất phương trình ${latex(f)}<0$ có miền nghiệm không chứa đường thẳng ${latex(f)}=0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và chứa đường thẳng $d:{latex(f)}=0$"
        kq4_F=random.choice([f"Miền nghiệm là nửa mặt phẳng không chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$",
            f"Miền nghiệm là nửa mặt phẳng không chứa điểm $({x_1};{y_1})$ và không chứa đường thẳng $d:{latex(f)}=0$"
            ])
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Miền nghiệm là nửa mặt phẳng chứa điểm $({x_0};{y_0})$ và không chứa đường thẳng $d:{latex(f)}=0$."
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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

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