import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier
 
#Code trả về latex phân số
def hien_phan_so(t):
    m=latex(Rational(t).limit_denominator(1000000000000))
    return m

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(1000000000000))
    return m

def tao_dau(a):
    dau="+"
    if a<0 or a==0:
        dau=""
    return dau
def xu_li_heso_1(a):
    if a==1:
        heso=""
    elif a==-1:
        heso="-"
    elif a==0:
        heso="" 
    else:
        heso=a

    return heso
def codelatex_heva(pt1,pt2):
    kq= f"\\left\\{{ \\begin{{array}}{{l}}\n\
            {pt1} \\\\ \n\
            {pt2} \n\
\\end{{array}} \\right."  

################ Bài 1: Hàm số và đồ thị #################
#[D10_C3_B1_01]. Tính giá trị của hàm số có nhiều biểu thức tại một điểm
def npl_mk_L10_C3_B1_01():
    a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    b = random.choice([random.randint(-6, -1), random.randint(1, 6)])
    c = random.randint(-7,7)
    d = random.choice([random.randint(-8, -1), random.randint(1, 8)])
      
    x = sp.symbols('x')     
    chon_ham=random.choice(["f1","f2","f3"])
    if chon_ham=="f1":
        f = a*x**2 + b*x + c
        x_0 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
        kq = f.subs(x, x_0)
        kq2 = f.subs(x, x_0+1)
        kq3=f.subs(x, -x_0)
        kq4=f.subs(x, x_0-1)        
    elif chon_ham=="f2":
        f = a*x**3+b*x**2+c*x+d
        x_0 = random.choice([random.randint(-6, -1), random.randint(1, 6)])
        kq = f.subs(x, x_0)
        kq2 = f.subs(x, x_0+1)
        kq3=f.subs(x, -x_0)
        kq4=f.subs(x, x_0-1)
    else:
        m=random.randint (1,8)
        n=random.randint (-5,5)
        t=int(-n/m)+1
        x_0 = random.randint(t,t+7)
        f=sqrt(m*x+n)
        f_gia=m*x+n
        kq = f.subs(x, x_0)
        kq2 = f.subs(x, x_0+1)
        kq3=f_gia.subs(x, x_0)
        kq4=f_gia.subs(x, x_0-1)

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*${{ {latex(kq)} }}$"
    pa_B= f"$ {{{latex(kq2)} }}$"
    pa_C= f"$ {{{latex(kq3)}}}$"
    pa_D= f"$ {{{latex(kq4)}}}$"

    #Trộn các phương án
    noi_dung= f"Cho hàm số $f(x)={latex(f)}$. Tính $f({x_0})$.\n"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Thay giá trị ${x_0}$ và hàm số $f(x)={latex(f)}$ ta được $f({x_0})={latex(kq)}$."  
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

#[D10_C3_B1_02]. Tính giá trị của hàm số có nhiều biểu thức tại một điểm
def npl_mk_L10_C3_B1_02():
    a = random.randint(-5,5)
    if a==0:
    	a = a + 1
    b = random.randint(-7,7)
    c = random.randint(-7,7)
    d = random.randint(-7,7)
    if d==0:
    	d = d + 1
    e = random.randint(-5,5)

    x = sp.symbols('x')
    f = a*x**2 + b*x + c
    g = d*x + e 
    t = random.randint(-6,6)
    x_0 = random.randint(-6,6)
    if x_0 == 0:
    	x_0=x_0 + 1
    if x_0 >= t:
    	kq = f.subs(x, x_0)
    	kq2 = g.subs(x, x_0)
    	kq3=f.subs(x, -x_0)
    	kq4=g.subs(x, -x_0)
    else:
    	kq = g.subs(x, x_0)
    	kq2 = f.subs(x, x_0)
    	kq3=f.subs(x, -x_0)
    	kq4=g.subs(x, -x_0)
        
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    #Tạo các phương án
    pa_A= f"*${{ {latex(kq)} }}$"
    pa_B= f"$ {{{latex(kq2)} }}$"
    pa_C= f"$ {{{latex(kq3)}}}$"
    pa_D= f"$ {{{latex(kq4)}}}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho hàm số $f(x)=\\left\\{{ \\begin{{array}}{{l}} \n \
    {latex(f)} \\text{{ khi }} x \\ge {t}  \\\\ \n \
    {latex(g)} \\text{{          khi  }} x < {t}  \n \
    \\end{{array}} \\right.$. Tính $f({x_0})$.\n"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"

    if x_0>=t:
        noi_dung_loigiai=f"Vì ${x_0}\\ge {t}$ nên thay giá trị ${x_0}$ và hàm số $f(x)={latex(f)}$ ta được $f({x_0})={latex(kq)}$." 
    if x_0<t:
        noi_dung_loigiai=f"Vì ${x_0}<{t}$ nên thay giá trị ${x_0}$ và hàm số $f(x)={latex(g)}$ ta được $f({x_0})={latex(kq)}$." 
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

#[D10_C3_B1_03]. Tìm tập xác định hàm số y =(ax+b)/(cx+d)
def npl_mk_L10_C3_B1_03():
    x = sp.symbols('x')
    a = random.randint(-5,5)        
    b = random.randint(-7,7)
    c = random.randint(-8,8)
    d = random.randint(-10,10)
    if c==0:
        c = c + 1
    if d==0:
        d = d + 1
 
    f=(a*x+b)/(c*x+d)

    pa_A= f"*$D=\\mathbb{{R}} \\backslash \\{{ {latex(my_module.hien_phan_so(-d/c))} \\}}$"
    pa_B= f"$D=\\mathbb{{R}} \\backslash \\{{ {latex(my_module.hien_phan_so(d/c))} \\}}$"
    pa_C= f"$D=\\left( -\\infty ; {latex(my_module.hien_phan_so(-d/c))} \\right)$"
    pa_D= f"$D=\\left( {latex(my_module.hien_phan_so(-d/c))} ; +\\infty \\right)$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    dap_an=my_module.tra_ve_dap_an(list_PA)

    noi_dung = my_module.frac_to_dfrac(f"Tìm tập xác định của hàm số $y={latex(f)}$.")
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Hàm số xác định khi ${latex(c*x+d)}\\ne 0 \\Leftrightarrow x \\ne {latex(my_module.hien_phan_so(-d/c))}$." 
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

#[D10_C3_B1_04]. Tìm tập xác định y = căn (Ax+B)
def npl_mk_L10_C3_B1_04():
    x = sp.symbols('x')
    a = random.randint(-8,8)
    if a==0:
        a = a + 1        
    b = random.randint(-7,7)
    if b==0:
        b = b + 1 
    f=sqrt(a*x+b)
    if a>0:
        kq = f"D=\\left[{latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"
        kq2 = f"D=\\left({latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"
        kq3 = f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right)"
        kq4 = f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right]"
    else:
        kq = f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right]"
        kq2 = f"D=\\left(-\\infty;{latex(my_module.hien_phan_so(-b/a))}\\right)"
        kq3 = f"D=\\left({latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"
        kq4= f"D=\\mathbb{{R}} \\backslash \\{{{latex(my_module.hien_phan_so(-b/a))}\\}}"     
    pa_A= f"*${kq}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    noi_dung = f"Tìm tập xác định của hàm số $y={latex(f)}$."

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    dap_an=my_module.tra_ve_dap_an(list_PA)    

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"

    if a>0:
        noi_dung_loigiai=f"Hàm số xác định khi ${latex(a*x+b)}\\ge 0 \\Leftrightarrow x \\ge {latex(my_module.hien_phan_so(-b/a))}$."
    if a<0:
        noi_dung_loigiai=f"Hàm số xác định khi ${latex(a*x+b)}\\ge 0 \\Leftrightarrow x \\le {latex(my_module.hien_phan_so(-b/a))}$." 
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

#[D10_C3_B1_05]. Tìm tập xác định y = căn (A) + B/C
def npl_mk_L10_C3_B1_05():
    x = sp.symbols('x')
    a = random.randint(1,5)              
    b = random.randint(-10,10)
    if b==0:
        b = b + 1 
    m = random.randint(1,10) 
    c = random.randint(-8,8)
    if c==0:
        c = c + 1
    d = random.randint(-10,10)
    if -b/a==-d: d=d+random.randint(1,4)

    f=sqrt(a*x+b)+ m/(x+d) 
    
   
    if -b/a < -d:
        kq = f"\\left[{latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)\\backslash \\{{{-d}\\}}"            
        kq3= f"\\left[{latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"
        kq4= f"\\left[{latex(my_module.hien_phan_so(-b/a))};{-d}\\right]"
        noi_dung_loigiai=f"Hàm số xác định khi ${latex(a*x+b)}\\ge 0$ và $x \\ne {-d}$. Suy ra $x \\ge {latex(my_module.hien_phan_so(-b/a))}$ và $x \\ne {-d}$."
    else:
        kq = f"\\left[{latex(my_module.hien_phan_so(-b/a))};+\\infty\\right)"
        kq3 = f"\\left(-\\infty; {latex(my_module.hien_phan_so(-b/a))}\\right]"
        kq4= f"\\left[{d};{latex(my_module.hien_phan_so(-b/a))}\\right]"
        noi_dung_loigiai=f"Hàm số xác định khi ${latex(a*x+b)}\\ge 0$ và $x\\ne {-d}$. Suy ra $x \\ge {latex(my_module.hien_phan_so(-b/a))}$."
    kq2= f"\\mathbb{{R}} \\backslash \\{{{-d}\\}}"
    
    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Tìm tập xác định của hàm số  $y={latex(f)}$." 
 
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    dap_an=my_module.tra_ve_dap_an(list_PA)    

    debai= f"{noi_dung}\n"
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

#[D10_C3_B1_06]. Tìm tập giá trị dựa vào hình vẽ đồ thị
def npl_mk_L10_C3_B1_06():
    x_1=random.randint(-5,-2)
    x_2=x_1+random.randint(1,3)
    x_3=x_2+random.randint(1,3)

    y_1=random.randint(-5,5)
    y_2=random.randint(-3,3)
    y_3=y_2+random.randint(-2,2)

    if y_1==y_2==y_3:
        y_1=y_2-random.randint(1,3)

    min_y=min(y_1,y_2,y_3)
    max_y=max(y_1,y_2,y_3)

    code =f"\\documentclass[border=2pt]{{standalone}}\n\
\\usepackage{{tikz}}\n\
\\usetikzlibrary{{calc,intersections,patterns}}\n\
\\begin{{document}}\n\
\\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.6]\n\
\\tikzset{{everynode/.style={{scale=0.9}}}}\n\
\\draw[gray!20](-6,-6)grid(6,6);\n\
\\draw[->](-6,0)--(6,0)node[below left]{{$x$}};\n\
\\draw[->](0,-6)--(0,6)node[below left]{{$y$}};\n\
\\draw(0,0)node[below left]{{\\footnotesize$O$}};\n\
\\foreach \\x in{{-5,-4,-3,-2,-1,1,2,3,4,5}}\n\
\\draw[thin](\\x,1pt)--(\\x,-1pt)node[below]{{\\footnotesize$\\x$}};\n\
\\foreach \\y in{{-5,-4,-3,-2,-1,1,2,3,4,5}}\n\
\\draw[thin] (1pt,\\y)--(-1pt,\\y)node[left]{{\\footnotesize$\\y$}};\n\
\\draw[thick,color=blue,line width=2]({x_1},{y_1})--({x_2},{y_2})--({x_3},{y_3});\n\
\\end{{tikzpicture}}\n\
\\end{{document}}"
    code_latex=f"\\begin{{tikzpicture}}[line join=round, line cap=round,>=stealth,thick,scale=0.6]\n\
\\tikzset{{everynode/.style={{scale=0.9}}}}\n\
\\draw[gray!20](-6,-6)grid(6,6);\n\
\\draw[->](-6,0)--(6,0)node[below left]{{$x$}};\n\
\\draw[->](0,-6)--(0,6)node[below left]{{$y$}};\n\
\\draw(0,0)node[below left]{{\\footnotesize$O$}};\n\
\\foreach \\x in{{-5,-4,-3,-2,-1,1,2,3,4,5}}\n\
\\draw[thin](\\x,1pt)--(\\x,-1pt)node[below]{{\\footnotesize$\\x$}};\n\
\\foreach \\y in{{-5,-4,-3,-2,-1,1,2,3,4,5}}\n\
\\draw[thin] (1pt,\\y)--(-1pt,\\y)node[left]{{\\footnotesize$\\y$}};\n\
\\draw[thick,color=blue,line width=2]({x_1},{y_1})--({x_2},{y_2})--({x_3},{y_3});\n\
\\end{{tikzpicture}}\n"
    file_name = my_module.pdftoimage_timename(code)

    kq = f"[{min_y};{max_y}]"            
    kq2= f"[{min_y-random.randint(1,3)};{max_y}]"
    kq3= f"[{min_y};{max_y+random.randint(1,3)}]"
    kq4= f"[{min_y-random.randint(1,3)};{max_y+random.randint(1,3)}]"  
    
    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án

    noi_dung = f"Cho hàm số $y=f(x)$ xác định trên đoạn ${{[{x_1};{x_3}]}}$ có đồ thị như hình vẽ bên.Tìm tập giá trị của hàm số đã cho."
            

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA) 
    dap_an=my_module.tra_ve_dap_an(list_PA)    

    debai= f"{noi_dung}\n\n"\
    f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"
    noi_dung_loigiai=f"Dựa vào đồ thị ta thấy tập giá trị của hàm số là đoạn $[{min_y};{max_y}]$."
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"{code_latex}"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B1_07]-M2.  Tìm tập xác định y =căn(ax+b) + căn(cx+d).
def npl_mk_L10_C3_B1_07():   
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")
    a =random.randint(1,10)  
    b=random.randint(-6,6)    
    c =random.randint(-6,-1)  
    d = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    dau_b=tao_dau(b)
    dau_d=tao_dau(d)
    a1=xu_li_heso_1(a)
    b1=xu_li_heso_1(b)
    c1=xu_li_heso_1(c)

    x_1, x_2 =-b/a, -d/c
    if x_1==x_2:
        d==d+random.randint(1,3)

    t_1=latex(my_module.hien_phan_so(x_1))
    t_2=latex(my_module.hien_phan_so(x_2))     
    
    
    dau_noi=random.choice(["+","-"])
    f=f"{latex(sqrt(a*x+b))} {dau_noi} {latex(sqrt(c*x+d))}"

    if x_1<x_2:
        kq=f"\\left[{t_1} ;{t_2} \\right]"
        kq2=random.choice([f"\\left({t_1} ;{t_2} \\right)",f"\\left({t_1} ;{t_2} \\right)"])
        kq3=random.choice([f"\\left[{t_1} ;+\\infty\\right)",f"\\left[{t_2} ;+\\infty\\right)" ])
        kq4=random.choice([f"\\left(-\\infty;{t_1}\\right]",f"\\left(-\\infty;{t_2}\\right]" ])
    else:
        kq=f"\\emptyset"
        kq2=random.choice([f"\\left({t_2} ;{t_1} \\right)",f"\\left({t_2} ;{t_1} \\right)"])
        kq3=random.choice([f"\\left[{t_1} ;+\\infty\\right)",f"\\left[{t_2} ;+\\infty\\right)" ])
        kq4=random.choice([f"\\left(-\\infty;{t_1}\\right]",f"\\left(-\\infty;{t_2}\\right]" ])
 
    #Tạo các phương án
    pa_A= f"*${{D={kq}}}$"
    pa_B= f"${{D={kq2}}}$"
    pa_C= f"${{D={kq3}}}$"
    pa_D= f"${{D={kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    
    noi_dung=my_module.frac_to_dfrac(f"Tìm tập xác định của hàm số $y={f}$.")
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"    

    noi_dung_loigiai=f"Điều kiện xác định: .\n"\
                    f"$\\left\\{{ \\begin{{array}}{{l}}\n\
            {latex(a*x+b)}\\ge 0 \\\\ \n\
            {latex(c*x+d)}\\ge 0 \n\
\\end{{array}} \\right.$"  \
            f"$\\Rightarrow\\left\\{{ \\begin{{array}}{{l}}\n\
            x\\ge {t_1} \\\\ \n\
            x\\le {t_2} \n\
\\end{{array}} \\right.$" \
    f"Tập xác định là: ${{D={kq}}}$." 
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B1_08]-M2.  Tìm tập xác định y =A/(ax^2+bx+c).
def npl_mk_L10_C3_B1_08():   
    #Tạo bậc ngẫu nhiên
    x=sp.symbols("x")
    chon=random.choice([0,1,2])
    m=random.randint(-10,10)
    n=random.choice([random.randint(-10, -1), random.randint(1, 10)])
    tu_thuc=latex(m*x+n)
    if chon==0:
        #Tạo tam thức vô nghiệm
        a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        c = random.choice([random.randint(-10, -1), random.randint(1, 10)])
        if a*c<0:
            c=-c
        b=int(sqrt(4*a*c))-random.randint(1,5)
        f=latex(a*x**2+b*x+c)
        x_0=latex(my_module.hien_phan_so(-b/(2*a))) 
        kq=f"D=\\mathbb{{R}}"
        kq2=f"D=\\mathbb{{R}} \\backslash \\{{{x_0}\\}}"
        kq3=f"D=\\emptyset"
        kq4=random.choice([f"D=\\left({x_0};+\\infty\\right)",f"D=\\left(-\\infty;{x_0}\\right)"])
        noi_dung_loigiai=f"Ta có: ${f}=0$ vô nghiệm nên ${f}\\ne 0$ với mọi $x \\in \\mathbb{{R}}$. Tập xác định: ${{{kq}}}$. \n" 

    elif chon==1:
        x_0=random.choice([random.randint(-7, -1), random.randint(1, 6)])
        a=random.randint(1,3)
        f=latex(expand(a*(x-x_0)**2))        

        kq=f"D=\\mathbb{{R}} \\backslash \\left\\{{{x_0}\\right\\}}"
        kq2=f"D=\\mathbb{{R}}"
        kq3=f"D=\\emptyset"
        kq4=random.choice([f"D=\\left({x_0};+\\infty\\right)",f"D=\\left(-\\infty;{x_0}\\right)"])

        noi_dung_loigiai=f"Ta có: ${f}=0$ có nghiệm $x={x_0}$ nên ${f} \\ne 0$ với mọi $x \\ne {x_0}$. Tập xác định: ${{{kq}}}$. \n" 

    else:
        a1=random.randint(1,6)
        b1=random.randint(1,15)
        a2=random.randint(1,6)
        b2=random.randint(1,20)
        if a1*b1==a2*b2:
            a2=a1+random.randint(1,4)
        a=a1*a2
        b=a1*b2+b1*a2
        c=b1*b2       
        f=latex(a*x**2+b*x+c)
        if -b1/a1<-b2/a2:   
            x_1=latex(my_module.hien_phan_so(-b1/a1))
            x_2=latex(my_module.hien_phan_so(-b2/a2))
        else:
            x_1=latex(my_module.hien_phan_so(-b2/a2))
            x_2=latex(my_module.hien_phan_so(-b1/a1))

        kq=f"D=\\mathbb{{R}} \\backslash \\left\\{{{x_1};{x_2}\\right\\}}"
        kq2=f"D=\\left[{x_1};{x_2}\\right]"
        kq3=f"D=\\left({x_1};{x_2}\\right)"
        kq4=random.choice([f"D=\\left(-\\infty;{x_1};\\right) \\cup \\left({x_2};+\\infty\\right)"])

        noi_dung_loigiai=f"Ta có: ${f}=0$ có nghiệm $x_1={x_1},x_2={x_2}$ nên \n ${f} \\ne 0$ với mọi $x \\ne {x_1}$ và $x\\ne {x_2}$. Tập xác định: ${{{kq}}}$. \n" 
   #Tạo các phương án
    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    
    noi_dung=f"Tìm tập xác định của hàm số $y=\\dfrac{{{tu_thuc}}}{{{f}}}$.\n"
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B1_09]-SA-M2. Số các số nguyên thuộc TXD y=căn(ax+b) + căn (c-dx)
def npl_mk_L10_C3_B1_09():
    x=sp.symbols("x")
    a=random.randint(1,10) 
    b=a*random.randint(1,20)+random.randint(0,5)
    
    d=random.randint(1,8)
    c=d*random.randint(8,20)+random.randint(0,5)

    f=sqrt(a*x+b) + sqrt(c-d*x)
    x_1,x_2=-b/a, c/d
    dem=0
    for i in range(int(x_1)-1,int(x_2)+1):
        if x_1<=i and i<=x_2:
            dem+=1
    noi_dung = (
    f"Tìm số các số nguyên thuộc tập xác định của hàm số $y={latex(f)}$."
    )
    dap_an=dem

    noi_dung_loigiai=(
    f"Điều kiện xác định: \n\n"
    f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    {latex(a*x+b)}\\ge 0 \\\\ \n\
    {latex(c-d*x)}\\ge 0\n\
    \\end{{array}} \\right.$"

    f"$\\Leftrightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
    x \\ge {phan_so(-b/a)} \\\\ \n\
     x \\le {phan_so(c/d)}\n\
    \\end{{array}} \\right.$"

    f"$\\Rightarrow {phan_so(-b/a)}\\le x \\le {phan_so(c/d)}$.\n\n"
    f"Tập xác định: $D=\\left[{phan_so(-b/a)};{phan_so(c/d)}\\right]$.\n\n"
    f"Số các số nguyên thuộc tập xác định là ${{{dem}}}$."

  
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an


#[D10_C3_B1_10]-M2.  Tìm hs có TXD là R 
def npl_mk_L10_C3_B1_10():  
    x=symbols("x") 
    n=random.randint(1,4)
    a=random.choice([i for i in range(-5,5) if i!=0])
    b=random.choice([i for i in range(-5,5) if i!=0])
    c=random.choice([i for i in range(-5,5) if i!=0])
    c1=random.choice([i for i in range(-5,5) if i!=0])
    a2=random.choice([i for i in range(-5,5) if i!=0])
    c2=random.choice([i for i in range(-5,5) if i!=0])
    a3=random.choice([i for i in range(-5,5) if i!=0])
    noi_dung=f" Trong các hàm số sau hàm số nào xác định trên $\\mathbb{{R}}$?"
    noi_dung_loigiai=f" Hàm số có TXD là $\\mathbb{{R}}$ là $y={latex(a*x**n+b*x**(n-1)+c)}$"
   #Tạo các phương án
    kq= f"$y={latex(a*x**n+b*x**(n-1)+c)}$ "
    kq_F=[ f"$y={latex(expand(1/(a*(x-c)*(x-c1))))}$ ", f"$y={latex(sqrt(a*x-c1))} $", f"$y={latex(1/sqrt(a2*x-c2))} $", f" $y={latex((a2*x-a)/(b*x-c) )}$", f"$y={latex(c*x+sqrt(a3*x+c2))} $"]
    kq4, kq2, kq3=random.sample(kq_F,3)


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D10_C3_B1_11]-M2.  Tìm hs đồng biến(nghịch biến) trên R 
def npl_mk_L10_C3_B1_11():  
    x=symbols("x") 
    n=random.randint(1,4)
    a=random.choice([i for i in range(-5,5) if i!=0])
    b=random.choice([i for i in range(-5,5) if i!=0])
    c=random.choice([i for i in range(-5,5) if i!=0])
    c1=random.choice([i for i in range(-5,5) if i!=0])
    a2=random.choice([i for i in range(-5,5) if i!=0])
    c2=random.choice([i for i in range(-5,5) if i!=0])
    a3=random.choice([i for i in range(-5,5) if i!=0])
    if a>0: 
        noi_dung=f" Trong các hàm số sau hàm số nào đồng biến trên $\\mathbb{{R}}$?"
        noi_dung_loigiai=f" Hàm số đồng biến trên $\\mathbb{{R}}$ là $y={latex(a*x+c)}$"
       #Tạo các phương án
        kq= f"$y={latex(a*x+c)}$ "
        kq_F=[ f"$y={latex(-a*x+a3)}$ ", f"$y={latex(sqrt(a*x-c1))} $", f"$y={latex(1/sqrt(a2*x-c2))} $", f" $y={latex((a2*x-a)/(b*x-c) )}$", f"$y={latex(c*x+sqrt(a3*x+c2))} $"]

    if a<0: 
        noi_dung=f" Trong các hàm số sau hàm số nào nghịch biến trên $\\mathbb{{R}}$?"
        noi_dung_loigiai=f" Hàm số nghịch biến trên $\\mathbb{{R}}$ là $y={latex(a*x+c)}$"
       #Tạo các phương án
        kq= f"$y={latex(a*x+c)}$ "
        kq_F=[ f"$y={latex(-a*x-c2)}$ ", f"$y={latex(sqrt(a*x-c1))} $", f"$y={latex(1/sqrt(a2*x-c2))} $", f" $y={latex((a2*x-a)/(b*x-c) )}$", f"$y={latex(c*x+sqrt(a3*x+c2))} $", f"$y={latex(a*x**2+b*x+c)}$"]


    kq4, kq2, kq3=random.sample(kq_F,3)


    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B1_12]-M2. Tìm hàm số biểu diễn giá bán khi được giảm r% từ món thứ hai
def npl_mk_L10_C3_B1_12():
    r=random.randint(3,10)    
    dip=random.choice(["khai trương", "Noel", "Tết âm lịch" ])
    chon=random.randint(1,3)
    if chon==1:
        a=random.randint(5,20)*1000        
        keo=random.choice(["gói kẹo", "hộp bánh", "phần khoai chiên", "túi bánh snack", ])        
    
    if chon==2:
        a=random.randint(15,30)*1000       
        keo=random.choice(["hộp bút chì", "hộp bút màu", "bình nước", "bộ thước kẻ"])

    if chon==3:
        a=random.randint(50,80)*1000        
        keo=random.choice([ "chai sữa tắm", "bộ xếp hình", "hộp mặt nạ dưỡng da", "tuýp kem dưỡng"])

    
    noi_dung=(
        f"Một cửa hàng nhân dịp {dip} đã đồng loạt giảm giá các sản phẩm."
        f" Trong đó có chương trình nếu mua một {keo} từ thứ hai trở đi sẽ được giảm ${{{r}\\%}}$ so với giá ban đầu."
        f" Biết giá {keo} ban đầu là {a} đồng. Gọi ${{y}}$ là số tiền chi trả khi mua ${{x}}$ {keo}."
        f" Khẳng định nào sau đây đúng?"
        )
    b=int(a*r/100)
    m=a-b
        

    kq=random.choice([f"$y={m}x+{a-m}$"])
    kq_false=[
    f"$y={m}x+{a}$",
    f"$y={a}x+{b}$",
    f"$y={a}x+{a-m}$",
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f" Gói thứ nhất người đó trả ${{{a}}}$ đồng.\n\n"
    f" Số {keo} còn lại là $x-1$ và số tiền phải trả là:\n\n"
    f" ${a}-{r}\\%.{a}={m}$.\n\n"
    f" Số tiền chi trả khi mua ${{x}}$ {keo} là:\n\n"
    f" $y={a}+(x-1).{m}={m}x+{a-m}$."
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

#[D10_C3_B1_13]-M2. Tìm hàm số biểu diễn giá taxi
def npl_mk_L10_C3_B1_13():
    a= int(round(random.uniform(12, 16), 1)*1000)
    b=int(round(random.uniform(9, 11), 1)*1000)
    t=random.randint(1,5)
    noi_dung=(
    f"Một hãng taxi đặt giá cước vận chuyển như sau:"
    f" Giá {t} km đầu tiên là {a} đồng, giá các km tiếp theo là {b} đồng."
    f" Gọi ${{x}}$ là số km khách hàng di duyển, ${{y}}$ là số tiền chi trả."
    f" Khẳng định nào sau đây đúng?"
    )


    kq=(
    f"y=\\left\\{{ \\begin{{array}}{{l}} \n\
    {a}x, \\text{{ khi }} 0<x \\le {t} \\\\ \n\
    {b}x+{a*t-b*t}, \\text{{ khi }} x>{t}\n\
    \\end{{array}} \\right.")
    kq_false=[

    f"y=\\left\\{{ \\begin{{array}}{{l}} \n\
    {a}x, \\text{{ khi }} 0< x \\le {t} \\\\ \n\
    {b}x, \\text{{ khi }} x>{t}\n\
    \\end{{array}} \\right.",

    f"y=\\left\\{{ \\begin{{array}}{{l}} \n\
    {a}x, \\text{{ khi }} 0< x \\le {t} \\\\ \n\
    {b}x+{a*t}, \\text{{ khi }} x>{t}\n\
    \\end{{array}} \\right.",

    f"y=\\left\\{{ \\begin{{array}}{{l}} \n\
    {a}x, \\text{{ khi }} 0< x \\le {t} \\\\ \n\
    {b}x-{b*t}, \\text{{ khi }} x>{t}\n\
    \\end{{array}} \\right.",

    f"y=\\left\\{{ \\begin{{array}}{{l}} \n\
    {a}x, \\text{{ khi }} 0< x \\le {t} \\\\ \n\
    {b}x-{a}, \\text{{ khi }} x>{t}\n\
    \\end{{array}} \\right.",

    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"Nếu $0<x\\le {t}$ thì số tiền chi trả là: ${{{a}x}}$.\n\n"
    f"Nếu $x>{t}$ thì số tiền chi trả là:\n\n"
    f"$y={a}.{t}+{b}.(x-{t})={b}x+{a*t-b*t}$.\n\n"
    f"Số tiền chi trả là:\n\n"
    f"$y=\\left\\{{ \\begin{{array}}{{l}} \n\
    {a}x, \\text{{ khi }} 0< x \\le {t} \\\\ \n\
    {b}x+{a*t-b*t}, \\text{{ khi }} x>{t}\n\
    \\end{{array}} \\right.$"
    )
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")

    pa_A= f"*${kq}$".replace("+-","-")
    pa_B= f"${kq2}$".replace("+-","-")
    pa_C= f"${kq3}$".replace("+-","-")
    pa_D= f"${kq4}$".replace("+-","-")
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


#[D10_C3_B1_14]-SA-M2. Tìm số vật có thể mua khi giảm giá r% từ vật thứ 2
def npl_mk_L10_C3_B1_14():
    x=sp.symbols("x")
       
    dip=random.choice(["khai trương", "Noel", "Tết âm lịch" ])
    ten=random.choice(["An", "Nam", "Minh", "Phương", "Thảo", "Hoa", "Nga"])

    chon=random.randint(1,3)
    
    if chon==1:
        a=random.randint(5,20)*1000
        tien=random.randint(80,150)*1000    
        keo=random.choice(["gói kẹo", "hộp bánh", "phần khoai chiên", "túi bánh snack", ])
    
    if chon==2:
        a=random.randint(15,30)*1000
        tien=random.randint(100,200)*1000
        keo=random.choice(["hộp bút chì", "hộp bút màu", "bình nước", "bộ thước kẻ"])

    if chon==3:
        a=random.randint(50,80)*1000
        tien=random.randint(200,500)*1000     
        keo=random.choice([ "chai sữa tắm", "bộ xếp hình", "hộp mặt nạ dưỡng da", "tuýp kem dưỡng"
   ])

    r=random.randint(3,10)
    b=int(a*r/100)
    m=a-b        
    x=random.randint(10,20)
    y=m*x+a-m
    
    noi_dung=(
        f"Một cửa hàng nhân dịp {dip} đã đồng loạt giảm giá các sản phẩm."
        f" Trong đó có chương trình nếu mua một {keo} từ thứ hai trở đi sẽ được giảm ${{{r}\\%}}$ so với giá ban đầu."
        f" Biết giá {keo} ban đầu là {a} đồng."
        f" Bạn {ten} có {tien} đồng. Hỏi bạn {ten} có thể mua được tối đa bao nhiêu {keo}?")    
    
    x_0=(tien-a+m)/m
    x_0_round=f"{round_half_up(x_0,2):.2f}".replace(".",",")

    dem=0
    for i in range(1,int(x_0)+1):
        if i <x_0:
            dem+=1
        
    dap_an=dem

    noi_dung_loigiai=(
    f" Mua {keo} thứ nhất người đó trả ${{{a}}}$ đồng.\n\n"
    f" Số {keo} còn lại là $x-1$ và số tiền phải trả là:\n\n"
    f" ${a}-{r}\\%.{a}={m}$.\n\n"
    f" Số tiền chi trả khi mua ${{x}}$ {keo} là:\n\n"
    f" $y={a}+(x-1).{m}={m}x+{a-m}$.\n\n"
    f" Ta có: ${m}x+{a-m}\\le {tien}\\Rightarrow x\\le ={x_0_round}$.\n\n"
    f" Số {keo} mà bạn {ten} có thể mua là {dem}." )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B1_15]-SA-M2. Tìm số nguyên m để y=ax+b đồng biến (nghịch biến) trên R
def npl_mk_L10_C3_B1_15():
    x,m=sp.symbols("x,m")
    k=random.randint(50,90)
    a=random.randint(1,6)
    b= random.choice([i for i in range(-9, 20) if i!=0])
    c=random.choice([i for i in range(-9, 9) if i!=0])
    d=random.choice([i for i in range(-9, 9) if i!=0])
    chon=random.randint(1,4)   

    if chon==1:
        noi_dung = (
        f"Tìm số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] để hàm số "
        f" $y=({latex(a*m+b)})x+{latex(c*m+d)}$ đồng biến trên $\\mathbb{{R}}$."
        )
        m_0=-b/a
        dem=0
        for i in range(-k,k+1):
            if i>m_0:
                dem+=1
        dap_an=dem

        noi_dung_loigiai=(
        f"$y=({latex(a*m+b)})x+{latex(c*m+d)}$ đồng biến trên $\\mathbb{{R}}$ khi\n\n"
        f"${latex(a*m+b)}>0\\Rightarrow m>{phan_so(m_0)}$.\n\n"
        f"Số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] là: {dem}."
        )
    
    if chon==2:
        noi_dung = (
        f"Tìm số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] để hàm số "
        f" $y=({latex(a*m+b)})x+{latex(c*m+d)}$ nghịch biến trên $\\mathbb{{R}}$."
        )
        m_0=-b/a
        dem=0
        for i in range(-k,k+1):
            if i<m_0:
                dem+=1
        dap_an=dem

        noi_dung_loigiai=(
        f"$y=({latex(a*m+b)})x+{latex(c*m+d)}$ nghịch biến trên $\\mathbb{{R}}$ khi\n\n"
        f"${latex(a*m+b)}<0\\Rightarrow m<{phan_so(m_0)}$.\n\n"
        f"Số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] là: {dem}."
        )

    a=random.randint(-6,-1)
    b= random.choice([i for i in range(-20, 20) if i!=0])
    if chon==3:
        noi_dung = (
        f"Tìm số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] để hàm số "
        f" $y=({latex(a*m+b)})x+{latex(c*m+d)}$ đồng biến trên $\\mathbb{{R}}$."
        )
        m_0=-b/a
        dem=0
        for i in range(-k,k+1):
            if i<m_0:
                dem+=1
        dap_an=dem

        noi_dung_loigiai=(
        f"$y=({latex(a*m+b)})x+{latex(c*m+d)}$ đồng biến trên $\\mathbb{{R}}$ khi\n\n"
        f"${latex(a*m+b)}>0\\Rightarrow m<{phan_so(m_0)}$.\n\n"
        f"Số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] là: {dem}."
        )

    if chon==4:
        noi_dung = (
        f"Tìm số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] để hàm số "
        f" $y=({latex(a*m+b)})x+{latex(c*m+d)}$ nghịch biến trên $\\mathbb{{R}}$."
        )
        m_0=-b/a
        dem=0
        for i in range(-k,k+1):
            if i>m_0:
                dem+=1
        dap_an=dem

        noi_dung_loigiai=(
        f"$y=({latex(a*m+b)})x+{latex(c*m+d)}$ nghịch biến trên $\\mathbb{{R}}$ khi\n\n"
        f"${latex(a*m+b)}<0\\Rightarrow m>{phan_so(m_0)}$.\n\n"
        f"Số các giá trị nguyên của ${{m}}$ thuộc đoạn [{-k};{k}] là: {dem}."
        )

    

    
    noi_dung=noi_dung.replace("+-","-")
    noi_dung_loigiai=noi_dung_loigiai.replace("+-","-")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B1_16]-SA-M2. Tìm số giá trị nguyên thuộc tập xác định của y=căn(ax+b)
def npl_mk_L10_C3_B1_16():
    x=sp.symbols("x")
    chon=random.randint(1,2)
    
    if chon==1:
        a=random.randint(1,6)
        b= random.choice([i for i in range(-20, 20) if i!=0])
        f=sqrt(a*x+b)
        k=random.randint(50,90)
        dem=0
        for i in range(-k,k+1):
            if i>=-b/a:
                dem+=1

        noi_dung = (
        f"Gọi ${{D}}$ là tập xác định của hàm số $y={latex(f)}$."
        f" Tìm số các giá trị nguyên thuộc tập hợp $D\\cap [{-k};{k}]$." )
        

        noi_dung_loigiai=(
        f"Hàm số xác định khi: ${latex(a*x+b)}\\ge 0 \\Rightarrow x\\ge {phan_so(-b/a)}$.\n\n"
        f"Tập xác định: $D=[{phan_so(-b/a)};+\\infty)$.\n\n"
        f"Số các giá trị nguyên thuộc tập hợp $D\\cap [{-k};{k}]$ là: {dem}." )
        dap_an=dem 
    
    if chon==2:
        a=random.randint(-6,-1)
        b= random.choice([i for i in range(-20, 20) if i!=0])
        f=sqrt(a*x+b)
        k=random.randint(50,90)
        dem=0
        for i in range(-k,k+1):
            if i<=-b/a:
                dem+=1

        noi_dung = (
        f"Gọi ${{D}}$ là tập xác định của hàm số $y={latex(f)}$."
        f" Tìm số các giá trị nguyên thuộc tập hợp $D\\cap [{-k};{k}]$." )
        

        noi_dung_loigiai=(
        f"Hàm số xác định khi: ${latex(a*x+b)}\\ge 0 \\Rightarrow x\\le {phan_so(-b/a)}$.\n\n"
        f"Tập xác định: $D=(-\\infty;{phan_so(-b/a)}]$.\n\n"
        f"Số các giá trị nguyên thuộc tập hợp $D\\cap [{-k};{k}]$ là: {dem}." )
        dap_an=dem 
    
       
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an


################ Bài 2: Hàm số bậc 2 #################
#[D10_C3_B2_01]. Tìm tọa độ đỉnh của đồ thị hàm số bậc 2
def npl_mk_L10_C3_B2_01():
    x = sp.symbols('x')
    a = random.randint(-5,5)
    if a==0:
        a = random.randint(1,6)              
    b = random.randint(-6,6)
    if b==0:
        b = random.randint(-6,-1)   
    c = random.randint(-6,6)

    f=a*x**2 + b*x + c            

             
    x_0 =latex(my_module.hien_phan_so(-b/(2*a)))         
    y_0 = latex(my_module.hien_phan_so(f.subs(x, -b/(2*a))))

    x_1=latex(my_module.hien_phan_so(-b/a))
    y_1=latex(my_module.hien_phan_so(f.subs(x, -b/a)))

    x_2=latex(my_module.hien_phan_so(b/(2*a)))
    y_2=latex(my_module.hien_phan_so(f.subs(x, b/(2*a))))

    x_3=latex(my_module.hien_phan_so(b/a))
    y_3=latex(my_module.hien_phan_so(f.subs(x, b/a)))



    pa_A= f"*${{I\\left({x_0};{y_0}\\right)}}$"
    pa_B= f"${{I\\left({x_1};{y_1}\\right)}}$"
    pa_C= f"${{I\\left({x_2};{y_2}\\right)}}$"
    pa_D= f"${{I\\left({x_3};{y_3}\\right)}}$"
    #Trộn các phương án
    noi_dung = f"Tìm tọa độ đỉnh ${{I}}$ của đồ thị hàm số $y={latex(f)}$."

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)  
    
    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

    noi_dung_loigiai=f"Đồ thị hàm số $y={latex(f)}$ có tọa độ đỉnh là ${{I\\left({x_0};{y_0}\\right)}}$. "
    
    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B2_02]. Tìm trục đối xứng của đồ thị hàm số bậc 2
def npl_mk_L10_C3_B2_02():
    x = sp.symbols('x')
    a = random.randint(-5,5)
    if a==0:
        a = random.randint(1,6)              
    b = random.randint(-6,6)
    if b==0:
        b = random.randint(-6,-1)   
    c = random.randint(-6,6)

    f=a*x**2 + b*x + c    
    x_0 =latex(my_module.hien_phan_so(-b/(2*a)))
    x_1 =latex(my_module.hien_phan_so(b/(2*a)))         

    pa_A= f"*$x={x_0}$"
    pa_B= f"$y={x_0}$"
    pa_C= f"$x={x_1}$"
    pa_D= f"$y={x_1}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    noi_dung = f"Tìm trục đối xứng của đồ thị hàm số $y={latex(f)}$."

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f"Trục đối xứng của đồ thị hàm số $y={latex(f)}$ là đường thẳng $x={x_0}$."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B2_03]. Cho hàm số bậc 2. Tìm khoảng biến thiên
def npl_mk_L10_C3_B2_03():
    x = sp.symbols('x')
    a = random.randint(-5,5)
    if a==0:
        a = random.randint(1,6)              
    b = random.randint(-6,6)
    if b==0:
        b = random.randint(-6,-1)   
    c = random.randint(-6,6)
    x_0 =latex(my_module.hien_phan_so(-b/(2*a)))
    x_1 = latex(my_module.hien_phan_so(int(-b/(2*a))-1))
    bien_thien = random.choice(["đồng biến","nghịch biến"])
    if bien_thien == "đồng biến":
        if a>0:            
            kq = f"\\left({x_0} ; +\\infty\\right)"
            kq2 = f"\\left(-\\infty; {x_0}\\right)"
            kq3 = f"\\left(-\\infty; +\\infty\\right)"
            kq4 = f"\\left(-\\infty; {x_1}\\right)"            

        else:                
            kq = f"\\left(-\\infty; {x_0}\\right)"
            kq2 = f"\\left({x_0} ; +\\infty\\right)"
            kq3 = f"\\left(-\\infty; +\\infty\\right)"
            kq4 = f"\\left({x_1};+\\infty\\right)"
    else: # Tìm khoảng nghịch biến
        if a>0:            
            kq = f"\\left(-\\infty; {x_0}\\right)"
            kq2 = f"\\left({x_0} ; +\\infty\\right)"
            kq3 = f"\\left(-\\infty; +\\infty\\right)"
            kq4 = f"\\left({x_1};+\\infty\\right)"
        else:                
            kq = f"\\left({x_0} ; +\\infty\\right)"
            kq2 = f"\\left(-\\infty; {x_0}\\right)"
            kq3 = f"\\left(-\\infty; +\\infty\\right)"
            kq4 = f"\\left(-\\infty; {x_1}\\right)"
    f=a*x**2 + b*x + c 

    
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
    #Trộn các phương án

    noi_dung = f"Cho hàm số $y={latex(f)} $. Hàm số {bien_thien} trên khoảng nào trong các khoảng sau."

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f" Hàm số {bien_thien} trên khoảng ${kq}$."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B2_04].  Cho BBT hàm số bậc 2. Tìm khoảng biến thiên.
def npl_mk_L10_C3_B2_04():
    a = random.randint(-5,5)
    if a==0:
        a = random.randint(1,6)              
    b = random.randint(-6,6)         

    x_0 = latex(my_module.hien_phan_so(-b/(2*a)))
    x_1 = latex(my_module.hien_phan_so(int(-b/(2*a))+2))

    y_0 = random.randint(-10,10) 

    if a>0:
        code =f"\\documentclass[border=2pt]{{standalone}}\n\
                \\usepackage{{tkz-tab,tikz}} \n\
                \\usetikzlibrary{{calc,intersections,patterns}}\n\
                \\begin{{document}} \n\
                \\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$, ${x_0}$, $+\\infty$}} \n\
                \\tkzTabVar{{+/$+\\infty$ , -/ ${y_0}$ /, +/$+\\infty$ /}} \n\
                \\end{{tikzpicture}}\n\
                \\end{{document}}\n"
        code_latex=f"\\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$, ${x_0}$, $+\\infty$}} \n\
                \\tkzTabVar{{+/$+\\infty$ , -/ ${y_0}$ /, +/$+\\infty$ /}} \n\
                \\end{{tikzpicture}}\n"
        kq = f"Hàm số đồng biến trên khoảng $({x_1};+\\infty)$"
        kq2 = f"Hàm số đồng biến trên khoảng $(-\\infty;{x_0})$"
        kq3 = f"Hàm số nghịch biến trên khoảng $({x_0};+\\infty)$"
        kq4 = f"Hàm số nghịch biến trên khoảng $({x_0};{x_1})$"
    else:
        code =f"\\documentclass[border=2pt]{{standalone}}\n\
                \\usepackage{{tkz-tab,tikz}}\n\
                \\begin{{document}}\n \
                \\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$,${x_0}$,$+\\infty$}}\n\
                \\tkzTabVar{{-/$-\\infty$ , +/ ${y_0}$ /, -/$-\\infty$ /}}\n\
                \\end{{tikzpicture}}\n\
                \\end{{document}}\n"
        code_latex=f"\\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$,${x_0}$,$+\\infty$}}\n\
                \\tkzTabVar{{-/$-\\infty$ , +/ ${y_0}$ /, -/$-\\infty$ /}}\n\
                \\end{{tikzpicture}}\n"
        kq = f"Hàm số nghịch biến trên khoảng $({x_1};+\\infty)$" 
        kq2=f"Hàm số đồng biến trên khoảng $({x_0};+\\infty)$"
        kq3=f"Hàm số nghịch biến trên khoảng $(-\\infty;{x_1})$"
        kq4=f"Hàm số đồng biến trên khoảng $({x_0};{x_1})$" 

    file_name=my_module.pdftoimage_timename(code)

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung = f"Cho bảng biến thiên của hàm số $y=ax^2+bx+c$. Tìm khẳng định đúng.\n\n"
            

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    debai= f"{noi_dung}\n"\
        f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n     C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f"{kq} là khẳng định đúng."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C3_B2_05]. Cho bảng biến thiên. Tìm hàm số bậc hai
def npl_mk_L10_C3_B2_05():
    x = sp.symbols('x')
    a = random.randint(-5,5)
    if a==0:
        a = random.randint(1,6)              
    b = random.randint(-6,6)
    if b==0:
        b = random.randint(-6,-1)   
    c = random.randint(-6,6)

    f=a*x**2 + b*x + c       
    f2=a*x**2 - b*x + c
    f3=-a*x**2 + b*x + c
    f4=-a*x**2 + b*x - c  

    code = my_module.codelatex_bbt_bac2(a,b,c)
    file_name=my_module.pdftoimage_timename(code)
    code_latex=my_module.code_bbt_bac2(a,b,c)

    pa_A= f"*$y={latex(f)}$"
    pa_B= f"$y={latex(f2)}$"
    pa_C= f"$y={latex(f3)}$"
    pa_D= f"$y={latex(f4)}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung= f"Bảng biến thiên sau là của hàm số nào?"           

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    debai= f"{noi_dung}\n\n"\
    f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f" Bảng biến thiên trên là của hàm số $y={latex(f)}$."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B2_06]. Cho đồ thị. Tìm hàm số bậc 2.
def npl_mk_L10_C3_B2_06():
    x = sp.symbols('x')
    a = random.randint(-3,3)
    if a==0:
        a = random.randint(1,3)              
    b = random.randint(-5,5)
    if b==0:
        b = random.randint(-5,-1)   
    c = random.randint(-4,4)

    code = my_module.codelatex_dothi_bac_2(a,b,c)
    file_name = my_module.pdftoimage_timename(code)
    code_latex=my_module.codelatex_dothi_bac_2_no_header(a,b,c)

    f=a*x**2 + b*x + c       
    f2=a*x**2 - b*x + c
    f3=-a*x**2 + b*x + c
    f4=-a*x**2 + b*x - c  
    pa_A= f"*$y={latex(f)}$"
    pa_B= f"$y={latex(f2)}$"
    pa_C= f"$y={latex(f3)}$"
    pa_D= f"$y={latex(f4)}$"

    noi_dung = f"Đồ thị như hình bên là của hàm số nào trong các hàm số sau?"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    debai= f"{noi_dung}\n\n"\
    f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f" Đồ thị như hình trên là của hàm số $y={latex(f)}$."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an





#[D10_C3_B2_07]. Tìm hàm số bậc 2 có đồ thị đi qua một điểm.
def npl_mk_L10_C3_B2_07():
    x = sp.symbols('x')
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-5, 6) if i!=0])
    c = random.choice([i for i in range(-5, 6) if i!=0]) 

    f=a*x**2 + b*x + c
    

    x_0 = random.choice([i for i in range(-4, 5) if i!=0])

    y_0 = f.subs(x, x_0)        
   
    he_so_an = random.choice(["b","c"])
    if he_so_an =="b":
        dau ="+"
        if c<0:
            dau=""
        ham_so =f"y={latex(a*x**2)}+bx{dau}{c}"
        kq=f"${he_so_an}={b}$"

        kq_false = set()
        while len(kq_false) < 5:

            numbers = random.randint(b-random.randint(1,5), b+random.randint(1,5))
            if numbers!=b:
                kq_false.add(numbers)
        kq_false=list(kq_false)

        pa_A= f"*${he_so_an}={b}$"
        pa_B= f"${he_so_an}={kq_false[0]}$"
        pa_C= f"${he_so_an}={kq_false[1]}$"
        pa_D= f"${he_so_an}={kq_false[2]}$"
    else:
        dau ="+"
        if b<0:
            dau=""
        ham_so =f"y={latex(a*x**2)}{dau}{latex(b*x)}+c"

        kq_false = set()
        while len(kq_false) < 5:

            numbers = random.randint(b-random.randint(1,5), b+random.randint(1,5))
            if numbers!=c:
                kq_false.add(numbers)

        kq_false=list(kq_false)
        kq=f"${he_so_an}={c}$"
        pa_A= f"*${he_so_an}={c}$"
        pa_B= f"${he_so_an}={kq_false[0]}$"
        pa_C= f"${he_so_an}={kq_false[1]}$"
        pa_D= f"${he_so_an}={kq_false[2]}$"

    ten_diem=random.choice(["A","B","C","M","N","P"])       

    noi_dung = f"Cho hàm số ${ham_so}$. Biết đồ thị hàm số đã cho đi qua điểm ${ten_diem}({x_0};{y_0})$. Tìm ${he_so_an}$?"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    debai= f"{noi_dung}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f"Thay tọa độ điểm ${ten_diem}({x_0};{y_0})$ vào phương trình ${ham_so}$ ta được ${kq}$."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
        f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B2_08]. Tìm hàm số bậc 2 có đồ thị đi qua hai điểm.
def npl_mk_L10_C3_B2_08():
        x = sp.symbols('x')
        a = random.randint(-4,4)
        if a==0:
            a = random.randint(1,3)              
        b = random.randint(-5,5)
        if b==0:
            b = random.randint(-5,-1)   
        c = random.randint(-5,5)

        f=a*x**2 + b*x + c
        

        x_0 = random.choice([i for i in range(-4,5) if i!=0 ])       
        y_0 = f.subs(x, x_0)

        x_1=x_0 + random.randint(1,3)   
        y_1 = f.subs(x, x_1)             

        he_so_hien = random.choice(["a","b","c"])
        if he_so_hien =="a":
            he_so_an=f"$b$ và $c$"        
            ham_so =f"y={latex(a*x**2)}+bx+c"
            pa_A= f"*$b={b},c={c}$.\t"
            pa_B= f"$b={b+random.randint(1,4)},c={c}$"
            pa_C= f"$b={b-random.randint(1,4)},c={c+random.randint(1,4)}$"
            pa_D= f"$b={b},c={c+random.randint(1,5)}$"

        if he_so_hien =="b":
            dau="+"
            if b<0:
                dau=""  
            he_so_an=f"$a$ và $c$"       
            ham_so =f"y=ax^2{dau}{latex(b*x)}+c"
            pa_A= f"*$a={a},c={c}$"
            pa_B= f"$a={a},c={c+random.randint(1,5)}$"
            pa_C= f"$a={a+random.randint(1,5)},c={c+random.randint(1,5)}$"
            pa_D= f"$a={a},c={c-random.randint(1,4)}$"

        if he_so_hien =="c":
            he_so_an=f"$a$ và $b$"
            dau ="+"
            if c<0:
                dau = ""         
            ham_so =f"y=ax^2+bx{dau}{c}"
            pa_A= f"*$a={a},b={b}$"
            pa_B= f"$a={a+random.randint(1,4)},b={b}$"
            pa_C= f"$a={a-random.randint(1,4)},b={b+random.randint(1,4)}$"
            pa_D= f"$a={a},b={b+random.randint(1,5)}$"

       
        #Trộn các phương án
        list_PA =[pa_A, pa_B, pa_C, pa_D]
        random.shuffle(list_PA)
        noi_dung = f"Biết đồ thị hàm số ${ham_so}$ đi qua điểm $A({x_0};{y_0})$ và $B({x_1};{y_1})$. Tìm các hệ số {he_so_an}."
        debai= f"{noi_dung}\n"
        phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
        noi_dung_loigiai=f""
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

#[D10_C3_B2_09]. Tìm hàm số bậc 2 có đồ thị đi qua điểm và trục đối xứng.
def npl_mk_L10_C3_B2_09():
        x = sp.symbols('x')
        a = random.randint(-4,4)
        if a==0:
            a = random.randint(1,3)              
        b = random.randint(-5,5)
        if b==0:
            b = random.randint(-5,-1)   
        c = random.randint(-5,5)

        f=a*x**2 + b*x + c

        x_0 = random.randint(-3,4)        
        y_0 = f.subs(x, x_0)

        x_1 = latex(my_module.hien_phan_so(-b/(2*a)))
      
        he_so_hien = random.choice(["a","b","c"])
        if he_so_hien =="a":
            he_so_an=f"$b$ và $c$"        
            ham_so =f"y={latex(a*x**2)}+bx+c"
            pa_A= f"*$b={b},c={c}$"
            pa_B= f"$b={b+random.randint(1,5)},c={b}$"
            pa_C= f"$b={-b},c={c+random.randint(1,4)}$"
            pa_D= f"$b={b-random.randint(1,4)},c={c+random.randint(1,4)}$"

        if he_so_hien =="b":
            dau="+"
            if b<0:  
                dau=""
            he_so_an=f"$a$ và $c$"       
            ham_so =f"y=ax^2{dau}{latex(b*x)}+c"
            pa_A= f"*$a={a},c={c}$"
            pa_B= f"$a={a+1},c={c}$"
            pa_C= f"$a={-a},c={c}$"
            pa_D= f"$a={a+random.randint(1,4)},c={c-random.randint(1,4)}$"

        if he_so_hien =="c":
            he_so_an=f"$a$ và $b$"
            dau ="+"
            if c<0:
                dau = ""         
            ham_so =f"y=ax^2+bx{dau}{c}"
            pa_A= f"*$a={a},b={b}$"
            pa_B= f"$a={-a},b={b}$"
            pa_C= f"$a={a+random.randint(1,4)},b={b}$"
            pa_D= f"$a={b+random.randint(1,4)},b={c}$"

       
        #Trộn các phương án
        list_PA =[pa_A, pa_B, pa_C, pa_D]
        random.shuffle(list_PA)
        noi_dung = f"Biết đồ thị hàm số ${ham_so}$ đi qua điểm $M({x_0};{y_0})$ và nhận đường thẳng $x={x_1}$ làm trục đối xứng. Tìm {he_so_an}."
        debai= f"{noi_dung}\n"
        phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
        noi_dung_loigiai=f""
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

#[D10_C3_B2_10]. Cho hàm số bậc 2. Xét dấu các hệ số a,b,c.
def npl_mk_L10_C3_B2_10():
    x = sp.symbols('x')
    a = random.randint(-2,2)
    if a==0:
        a = random.randint(1,3)              
    b = random.randint(-3,3)
    if b==0:
        b = random.randint(-3,-1)   
    c = random.randint(-3,3)

    code = my_module.codelatex_dothi_bac_2(a,b,c)
    file_name = my_module.pdftoimage_timename(code)
    code_latex=my_module.codelatex_dothi_bac_2_no_header(a,b,c)

    f=a*x**2 + b*x + c  

    kq=f"a{my_module.check_dau(a)},b{my_module.check_dau(b)},c{my_module.check_dau(c)}"
    kq2=f"a{my_module.check_dau(a)},b{my_module.check_dau(-b)},c{my_module.check_dau(-c)}"
    kq3=f"a{my_module.check_dau(-a)},b{my_module.check_dau(b)},c{my_module.check_dau(c)}"
    kq4=f"a{my_module.check_dau(-a)},b{my_module.check_dau(-b)},c{my_module.check_dau(c)}"
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    noi_dung= f"Cho hàm số $y=ax^2+bx+c$ có đồ thị như hình bên. Tìm khẳng định đúng."

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA) 

    debai= f"{noi_dung}\n\n"\
    f"{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    noi_dung_loigiai=f" Đồ thị như hình trên là của hàm số $y={latex(f)}$."

    loigiai_word=f"Lời giải:\n Chọn {dap_an}\n{noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n\n"\
    f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n\n"\
    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C3_B2_11]-TF-M2. Cho hàm số bậc hai. Tạo câu hỏi đúng-sai hỗn hợp.   
def npl_mk_L10_C3_B2_11():
    x=symbols("x")
    #Tạo hàm số bậc 2
    a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b, c = random.randint(-10, 10), random.randint(-10, 10)

    f=a*x**2+b*x+c
    
    noi_dung=f"Cho hàm số $f(x)={latex(f)}$. Xét tính đúng sai của các khẳng định sau."

    kq1_T=f"*Tập xác định của hàm số là $\\mathbb{{R}}$"
    kq1_F=f"Tập xác định của hàm số là khoảng $({random.randint(-10,10)};+\\infty)$" 
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Tập xác định của hàm số là $\\mathbb{{R}}$ là khẳng định đúng vì đây là hàm số đa thức." 
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai vì tập xác định của hàm số là $\\mathbb{{R}}$."
  
    kq2_T=f"*Đồ thị hàm số có hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a))}$"
    kq2_F=f"Đồ thị hàm số có hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a)+random.randint(1,4))}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Đồ thị hàm số có hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a))}$ là khẳng định đúng." 
    if kq2==kq2_F:
        loigiai_2=f"{kq2_F} là khẳng định sai vì hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a))}$."

    if a>0:
        kq3_T=f"*Hàm số đồng biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$"
        kq3_F=f"Hàm số nghịch biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số đồng biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$ là khẳng định đúng." 
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai vì hàm số đồng biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$."

    if a<0:
        kq3_T=f"*Hàm số nghịch biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$"
        kq3_F=f"Hàm số đồng biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$"
        kq3=random.choice([kq3_T, kq3_F])
        loigiai_3=f"Hàm số nghịch biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$." 
        if kq3==kq3_F:
            loigiai_3=f"{kq3_F} là khẳng định sai vì Hàm số đồng biến trên khoảng $\\displaystyle \\left({hien_phan_so(-b/(2*a))};+\\infty \\right)$."
    

    x_1=random.randint(-5,5)
    y_1=f.subs(x, x_1)
    ten_diem=random.choice(["A","B","C","D","M","N","E"])

    kq4_T=f"*Đồ thị hàm số đi qua điểm ${ten_diem}({x_1};{y_1})$"
    kq4_F=f"Đồ thị hàm số không đi qua điểm ${ten_diem}({x_1};{y_1})$"
    kq4=random.choice([kq4_T, kq4_F]) 
    loigiai_4=f"Đồ thị hàm số đi qua điểm ${ten_diem}({x_1};{y_1})$ là khẳng định đúng vì có $f({x_1})={y_1}$." 
    if kq4==kq4_F:
        loigiai_4=f"{kq4_F} là khẳng định sai vì có $f({x_1})={y_1}$ nên đồ thị hàm số đi qua điểm ${ten_diem}({x_1};{y_1})$."
    
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)

    debai= f"{noi_dung}\n"\
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
    f"a) {loigiai[0]}\n"\
    f"b) {loigiai[1]}\n"\
    f"c) {loigiai[2]}\n"\
    f"d) {loigiai[3]}\n"\

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

    loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
    f"b) {loigiai[1]}\\\\ \n"\
    f"c) {loigiai[2]}\\\\ \n"\
    f"d) {loigiai[3]}\\\\ \n"

    #Tạo đề latex
    for i in range(len(list_PA)):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")   

    return debai,debai_latex,loigiai_word,dap_an

#[D10_C3_B2_12]-TF-M2. Cho hàm số bậc hai. Tạo câu hỏi đúng-sai về đồ thị.   
def npl_mk_L10_C3_B2_12():
    x=symbols("x")
    #Tạo hàm số bậc 2
    a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
    b, c = random.randint(-10, 10), random.randint(-10, 10)

    f = a*x**2+b*x+c
    x_0 = -b/(2*a)
    y_0 = f.subs(x,x_0)
    
    noi_dung=f"Cho hàm số $f(x)={latex(f)}$. Xét tính đúng sai của các khẳng định sau."

    kq1_T=f"*Đồ thị hàm số có tọa độ đỉnh là $\\displaystyle I\\left({hien_phan_so(x_0)};{hien_phan_so(y_0)}\\right)$"
    kq1_F=f"Đồ thị hàm số có tọa độ đỉnh là $\\displaystyle I\\left({hien_phan_so(x_0+random.randint(1,5))};{hien_phan_so(y_0-random.randint(1,5))}\\right)$" 
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Hoành độ của đỉnh là $\\displaystyle x_0=-\\dfrac{{b}}{{2a}}={hien_phan_so(x_0)}$."\
    f" Tung độ của đỉnh là $\\displaystyle y_0=f({hien_phan_so(x_0)})={hien_phan_so(y_0)}$.\n\n"\
    f"Do đó đồ thị hàm số có tọa độ đỉnh là $\\displaystyle I\\left({hien_phan_so(x_0)};{hien_phan_so(y_0)}\\right)$ là khẳng định đúng" 
    if kq1==kq1_F:
        loigiai_1=f"{kq1_F} là khẳng định sai vì hoành độ của đỉnh là $\\displaystyle x_0=-\\dfrac{{b}}{{2a}}={hien_phan_so(x_0)}$ và"\
        f" tung độ của đỉnh là $\\displaystyle y_0=f({hien_phan_so(x_0)})={hien_phan_so(y_0)}$."
  
    kq2_T=f"*Đồ thị hàm số có hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a))}$"
    kq2_F=f"Đồ thị hàm số có hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a)+random.randint(1,4))}$"
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Đồ thị hàm số có hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a))}$ là khẳng định đúng." 
    if kq2==kq2_F:
        loigiai_2=f"{kq2_F} là khẳng định sai vì hoành độ đỉnh là $\\displaystyle x_0={hien_phan_so(-b/(2*a))}$."

    kq3_T=f"*Đồ thị hàm số nhận đường thẳng $\\displaystyle x={hien_phan_so(x_0)}$ làm trục đối xứng"
    kq3_F=f"Đồ thị hàm số nhận đường thẳng $\\displaystyle y={hien_phan_so(x_0)}$ làm trục đối xứng"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Đồ thị hàm số nhận đường thẳng $\\displaystyle x={hien_phan_so(x_0)}$ làm trục đối xứng là khẳng định đúng." 
    if kq3==kq3_F:
        loigiai_3=f"{kq3_F} là khẳng định sai vì đồ thị hàm số nhận đường thẳng $\\displaystyle x={hien_phan_so(x_0)}$ làm trục đối xứng."

    
    x_1=random.randint(-5,5)
    if x_1==x_0: x_1=x_0+random.randint(1,5)
    y_1=f.subs(x, x_1)
    ten_diem=random.choice(["A","B","C","D","M","N","E"])

    kq4_T=f"*Đồ thị hàm số đi qua điểm ${ten_diem}({x_1};{y_1})$"
    kq4_F=f"Đồ thị hàm số không đi qua điểm ${ten_diem}({x_1};{y_1})$"
    kq4=random.choice([kq4_T, kq4_F]) 
    loigiai_4=f"Đồ thị hàm số đi qua điểm ${ten_diem}({x_1};{y_1})$ là khẳng định đúng vì có $f({x_1})={y_1}$." 
    if kq4==kq4_F:
        loigiai_4=f"{kq4_F} là khẳng định sai vì có $f({x_1})={y_1}$ nên đồ thị hàm số đi qua điểm ${ten_diem}({x_1};{y_1})$."
    
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)

    debai= f"{noi_dung}\n"\
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
    f"a) {loigiai[0]}\n"\
    f"b) {loigiai[1]}\n"\
    f"c) {loigiai[2]}\n"\
    f"d) {loigiai[3]}\n"\

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

    loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
    f"b) {loigiai[1]}\\\\ \n"\
    f"c) {loigiai[2]}\\\\ \n"\
    f"d) {loigiai[3]}\\\\ \n"

    #Tạo đề latex
    for i in range(len(list_PA)):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")     

    return debai,debai_latex,loigiai_word,dap_an

#[D10_C3_B2_13]-TF-M2. Cho bảng biến thiên hàm số bậc hai. Tạo câu hỏi đúng-sai.   
def npl_mk_L10_C3_B2_13():
    x=symbols("x")
    #Tạo hàm số bậc 2
    a= random.choice([i for i in range(-5, 6) if i!=0])
    b, c = random.randint(-8, 8), random.randint(-8, 8)
    f = a*x**2+b*x+c
    x_0 = -b/(2*a)
    y_0 =f.subs(x,x_0)
    if y_0==x_0: c=c+1
    x_0 = hien_phan_so(-b/(2*a))
    y_0= hien_phan_so(y_0)
    if a>0:
        code =f"\\documentclass[border=2pt]{{standalone}}\n\
                \\usepackage{{tkz-tab,tikz}} \n\
                \\usetikzlibrary{{calc,intersections,patterns}}\n\
                \\begin{{document}} \n\
                \\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$, $\\displaystyle {x_0}$, $+\\infty$}} \n\
                \\tkzTabVar{{+/$+\\infty$ , -/ $\\displaystyle {y_0}$ /, +/$+\\infty$ /}} \n\
                \\end{{tikzpicture}}\n\
                \\end{{document}}\n"
        code_latex=f"\\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$, $\\displaystyle {x_0}$, $+\\infty$}} \n\
                \\tkzTabVar{{+/$+\\infty$ , -/ $\\displaystyle {y_0}$ /, +/$+\\infty$ /}} \n\
                \\end{{tikzpicture}}\n"
    else:
        code =f"\\documentclass[border=2pt]{{standalone}}\n\
                \\usepackage{{tkz-tab,tikz}}\n\
                \\begin{{document}}\n \
                \\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$,$\\displaystyle {x_0}$,$+\\infty$}}\n\
                \\tkzTabVar{{-/$-\\infty$ , +/ $\\displaystyle {y_0}$ /, -/$-\\infty$ /}}\n\
                \\end{{tikzpicture}}\n\
                \\end{{document}}\n"
        code_latex=f"\\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=2] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$-\\infty$,$\\displaystyle {x_0}$,$+\\infty$}}\n\
                \\tkzTabVar{{-/$-\\infty$ , +/ $\\displaystyle {y_0}$ /, -/$-\\infty$ /}}\n\
                \\end{{tikzpicture}}\n"
    file_name=my_module.pdftoimage_timename(code)
    x_0 = -b/(2*a)
    y_0 = f.subs(x,x_0)
    
    noi_dung=f"Cho parabol $(P):y=ax^2+bx=c,(a\\ne 0)$ có bảng biến thiên như hình dưới đây. "

    if a>0:
        kq1_T=f"*Hàm số có hệ số $a>0$"
        kq1_F=f"Hàm số có hệ số $a<0$" 
        kq1=random.choice([kq1_T, kq1_F])
        loigiai_1=f"Dựa vào dáng của bảng biến thiên, hàm số có hệ số $a>0$ là khẳng định đúng."    
        if kq1==kq1_F:
            loigiai_1=f"{kq1_F} là khẳng định sai vì dựa vào dáng của bảng biến thiên, hàm số có hệ số $a>0$"
    if a<0:
        kq1_T=f"*Hàm số có hệ số $a<0$"
        kq1_F=f"Hàm số có hệ số $a>0$" 
        kq1=random.choice([kq1_T, kq1_F])
        loigiai_1=f"Dựa vào dáng của bảng biến thiên, hàm số có hệ số $a<0$ là khẳng định đúng."    
        if kq1==kq1_F:
            loigiai_1=f"{kq1_F} là khẳng định sai vì dựa vào dáng của bảng biến thiên, hàm số có hệ số $a<0$"

    chon=random.randint(1,2)
    if chon==1:  
        kq2_T=f"*Đồ thị hàm số có hoành độ đỉnh bằng $\\displaystyle {hien_phan_so(x_0)}$"
        kq2_F=f"Đồ thị hàm số có hoành độ đỉnh bằng $\\displaystyle {hien_phan_so(y_0)}$"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số có hoành độ đỉnh bằng $\\displaystyle {hien_phan_so(x_0)}$ là khẳng định đúng." 
        if kq2==kq2_F:
            loigiai_2=f"{kq2_F} là khẳng định sai vì hoành độ đỉnh bằng $\\displaystyle {hien_phan_so(x_0)}$."


    if chon==2:
        kq2_T=f"*Đồ thị hàm số có tung độ đỉnh bằng $\\displaystyle {hien_phan_so(y_0)}$"
        kq2_F=f"Đồ thị hàm số có tung độ đỉnh bằng $\\displaystyle {hien_phan_so(x_0)}$"
        kq2=random.choice([kq2_T, kq2_F])
        loigiai_2=f"Đồ thị hàm số có tung độ đỉnh là $\\displaystyle {hien_phan_so(y_0)}$ là khẳng định đúng." 
        if kq2==kq2_F:
            loigiai_2=f"{kq2_F} là khẳng định sai vì tung độ đỉnh là $\\displaystyle {hien_phan_so(y_0)}$."

    kq3_T=f"*Đồ thị hàm số nhận đường thẳng $\\displaystyle x={hien_phan_so(x_0)}$ làm trục đối xứng"
    kq3_F=f"Đồ thị hàm số nhận đường thẳng $\\displaystyle y={hien_phan_so(x_0)}$ làm trục đối xứng"
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Đồ thị hàm số nhận đường thẳng $\\displaystyle x={hien_phan_so(x_0)}$ làm trục đối xứng là khẳng định đúng." 
    if kq3==kq3_F:
        loigiai_3=f"{kq3_F} là khẳng định sai vì đồ thị hàm số nhận đường thẳng $\\displaystyle x={hien_phan_so(x_0)}$ làm trục đối xứng."
    
    t=x_0+random.randint(1,5)
    if a>0:
        kq4_T=f"*Trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$ thì hàm số đồng biến"
        kq4_F=f"Trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$ thì hàm số nghịch biến"
        kq4=random.choice([kq4_T, kq4_F])
        loigiai_4=f"Hàm số đồng biến trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$ là khẳng định đúng." 
        if kq4==kq4_F:
            loigiai_4=f"{kq4_F} là khẳng định sai vì hàm số đồng biến trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$."

    if a<0:
        kq4_T=f"*Trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$ thì hàm số nghịch biến"
        kq4_F=f"Trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$ thì hàm số đồng biến"
        kq4=random.choice([kq4_T, kq4_F])
        loigiai_4=f"Hàm số nghịch biến trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$." 
        if kq4==kq4_F:
            loigiai_4=f"{kq4_F} là khẳng định sai vì hàm số nghịch biến trên khoảng $\\displaystyle \\left({hien_phan_so(t)};+\\infty \\right)$."
    
    #Trộn các phương án
    list_PA =[kq1, kq2, kq3, kq4]
    random.shuffle(list_PA)
    list_TF=my_module.tra_ve_TF(list_PA)

    debai= f"{noi_dung}\n\n"\
    f"{file_name}\n\n"\
    f"Xét tính đúng sai của các khẳng định sau:\n\n"\
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
    f"a) {loigiai[0]}\n"\
    f"b) {loigiai[1]}\n"\
    f"c) {loigiai[2]}\n"\
    f"d) {loigiai[3]}\n"\

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n" \

    loigiai_latex=f"a) {loigiai[0]}\\\\ \n"\
    f"b) {loigiai[1]}\\\\ \n"\
    f"c) {loigiai[2]}\\\\ \n"\
    f"d) {loigiai[3]}\\\\ \n"

    #Tạo đề latex
    for i in range(len(list_PA)):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\begin{{center}}\n{code_latex}\n\\end{{center}}\n"\
        f"Xét tính đúng sai của các khẳng định sau:"\
        f"\\choiceTF\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {loigiai_latex} \n }}"\
        f"\\end{{ex}}\n"
    dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")      

    return debai,debai_latex,loigiai_word,dap_an

#[D10_C3_B2_14]-SA-M2. Tìm hệ số của hàm bậc hai có đồ thị qua 2 điểm.
def npl_mk_L10_C3_B2_14():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-7, 7) if i!=0])
    c = random.choice([i for i in range(-7, 7) if i!=0])
    f=a*x**2+b*x+c

    points = [chr(i) for i in range(ord('A'), ord('N') + 1)]
    random.shuffle(points)
    points=points[0:2]
    points.sort()
    A,B=points

    x_1=random.randint(-5,6)
    x_2=random.choice([x for x in range(-5, 6) if x != x_1])
    y_1,y_2=f.subs(x,x_1),f.subs(x,x_2)

    m = random.choice([i for i in range(1, 3) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])
    ta,tb,tc=sp.symbols("a b c")

    chon=random.randint(1,3)
    
    if chon==1:        
        
        noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+bx+{c}$ đi qua các điểm ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$."
        f" Tính $P={latex(m*ta+n*tb)}$."
        )
        dap_an=m*a+n*b

        noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1+c)}={y_1} \\\\ \n\
        {latex(ta*x_2**2+tb*x_2+c)}={y_2}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1)}={y_1-c} \\\\ \n\
        {latex(ta*x_2**2+tb*x_2)}={y_2-c}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        b={b}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*ta+n*tb)}={dap_an}$." )    
    
    if chon==2:
        
        noi_dung = (
        f"Biết đồ thị hàm số $y={latex(a*x**2)}+bx+c$ đi qua các điểm ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$."
        f" Tính $P={latex(m*tb+n*tc)}$."
        )
        dap_an=m*b+n*c

        noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(a*x_1**2+tb*x_1+tc)}={y_1} \\\\ \n\
        {latex(a*x_2**2+tb*x_2+tc)}={y_2}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(tb*x_1+tc)}={y_1-a*x_1**2} \\\\ \n\
        {latex(tb*x_2+tc)}={y_2-a*x_2**2}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        b={b} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*tb+n*tc)}={dap_an}$." )

    if chon==3:        
        noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+{latex(b*x)}+c$ đi qua các điểm ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$."
        f" Tính $P={latex(m*ta+n*tc)}$."
        )

        dap_an=m*a+n*c

        noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+b*x_1+tc)}={y_1} \\\\ \n\
        {latex(ta*x_2**2+b*x_2+tc)}={y_2}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tc)}={y_1-b*x_1} \\\\ \n\
        {latex(ta*x_2**2+tc)}={y_2-b*x_2}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*ta+n*tc)}={dap_an}$." )

    noi_dung=noi_dung.replace("+-","-")
    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B2_15]-SA-M2. Tìm hệ số của hàm bậc hai có đồ thị qua điểm và có trục đối xứng.
def npl_mk_L10_C3_B2_15():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-7, 7) if i!=0])
    c = random.choice([i for i in range(-7, 7) if i!=0])
    f=a*x**2+b*x+c

    points = [chr(i) for i in range(ord('A'), ord('N') + 1)]
    random.shuffle(points)
    points=points[0:2]
    points.sort()
    A,B=points

    x_1=random.randint(-5,6)
    x_2=random.choice([x for x in range(-5, 6) if x != x_1])
    y_1,y_2=f.subs(x,x_1),f.subs(x,x_2)

    m = random.choice([i for i in range(1, 3) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])
    ta,tb,tc=sp.symbols("a b c")

    x_0=-b/(2*a)

    chon=random.randint(1,3)    
    
    if chon==1:
        
        noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+bx+{c}$ đi qua điểm ${A}({x_1};{y_1})$ và nhận đường thẳng $x={phan_so(x_0)}$ làm trục đối xứng."
        f" Tính $P={latex(m*ta+n*tb)}$."
        )
        dap_an=m*a+n*b

        noi_dung_loigiai=(
        f"Theo đề bài nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1+c)}={y_1} \\\\ \n\
        {latex(-tb/(2*ta))}={phan_so(x_0)}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1)}={y_1-c} \\\\ \n\
        {latex(-2*ta*x_0-tb)}=0\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        b={b}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*ta+n*tb)}={dap_an}$." )    
    
    if chon==2:
        
        noi_dung = (
        f"Biết đồ thị hàm số $y={latex(a*x**2)}+bx+c$ đi qua điểm ${A}({x_1};{y_1})$ và nhận đường thẳng $x={phan_so(x_0)}$ làm trục đối xứng."
        f" Tính $P={latex(m*tb+n*tc)}$."
        )
        dap_an=m*b+n*c

        noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(a*x_1**2+tb*x_1+tc)}={y_1} \\\\ \n\
        {latex(-tb/(2*a))}={phan_so(x_0)}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(tb*x_1+tc)}={y_1-a*x_1**2} \\\\ \n\
        b={b}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        b={b} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*tb+n*tc)}={dap_an}$." )

    if chon==3:        
        noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+{latex(b*x)}+c$ đi qua điểm ${A}({x_1};{y_1})$ và nhận đường thẳng $x={phan_so(x_0)}$ làm trục đối xứng."
        f" Tính $P={latex(m*ta+n*tc)}$."
        )

        dap_an=m*a+n*c

        noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+b*x_1+tc)}={y_1} \\\\ \n\
        {latex(-b/(2*ta))}={phan_so(x_0)}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tc)}={y_1-b*x_1} \\\\ \n\
        a={a}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*ta+n*tc)}={dap_an}$." )

    noi_dung=noi_dung.replace("+-","-")
    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B2_16]-SA-M2. Tìm hệ số của hàm bậc hai có tọa độ đỉnh
def npl_mk_L10_C3_B2_16():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-5, 6) if i!=0])
    b = random.choice([i for i in range(-7, 7) if i!=0])
    c = random.choice([i for i in range(-7, 7) if i!=0])
    f=a*x**2+b*x+c

    points = [chr(i) for i in range(ord('A'), ord('N') + 1)]
    random.shuffle(points)
    points=points[0:2]
    points.sort()
    A,B=points

    x_1=random.randint(-5,6)
    x_2=random.choice([x for x in range(-5, 6) if x != x_1])
    y_1,y_2=f.subs(x,x_1),f.subs(x,x_2)

    m = random.choice([i for i in range(1, 3) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])
    ta,tb,tc=sp.symbols("a b c")

    x_0=-b/(2*a)
    y_0=f.subs(x,x_0)

    chon=random.randint(1,3)    
    
    if chon==1:
        
        noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+bx+{c}$ có đỉnh là điểm $I({phan_so(x_0)};{phan_so(y_0)})$."
        f" Tính $P={latex(m*ta+n*tb)}$."
        )
        dap_an=m*a+n*b

        noi_dung_loigiai=(
        f"Theo đề bài nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1+c)}={y_1} \\\\ \n\
        {latex(-tb/(2*ta))}={phan_so(x_0)}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1)}={y_1-c} \\\\ \n\
        {latex(-2*ta*x_0-tb)}=0\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        b={b}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*ta+n*tb)}={dap_an}$." )    
    
    if chon==2:
        
        noi_dung = (
        f"Biết đồ thị hàm số $y={latex(a*x**2)}+bx+c$ có đỉnh là điểm $I({phan_so(x_0)};{phan_so(y_0)})$."
        f" Tính $P={latex(m*tb+n*tc)}$."
        )
        dap_an=m*b+n*c

        noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(a*x_1**2+tb*x_1+tc)}={y_1} \\\\ \n\
        {latex(-tb/(2*a))}={phan_so(x_0)}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(tb*x_1+tc)}={y_1-a*x_1**2} \\\\ \n\
        b={b}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        b={b} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*tb+n*tc)}={dap_an}$." )

    if chon==3:        
        noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+{latex(b*x)}+c$ có đỉnh là điểm $I({phan_so(x_0)};{phan_so(y_0)})$."
        f" Tính $P={latex(m*ta+n*tc)}$."
        )

        dap_an=m*a+n*c

        noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và ${B}({x_2};{y_2})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+b*x_1+tc)}={y_1} \\\\ \n\
        {latex(-b/(2*ta))}={phan_so(x_0)}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tc)}={y_1-b*x_1} \\\\ \n\
        a={a}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"
        f"$P={latex(m*ta+n*tc)}={dap_an}$." )

    noi_dung=noi_dung.replace("+-","-")    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B2_17]-SA-M2. Tìm 3 hệ số của hàm bậc hai có đồ thị đi qua 3 điểm.
def npl_mk_L10_C3_B2_17():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-4, 4) if i!=0])
    b = random.choice([i for i in range(-5, 5) if i!=0])
    c = random.choice([i for i in range(-7, 7) if i!=0])
    f=a*x**2+b*x+c

    points = [chr(i) for i in range(ord('A'), ord('N') + 1)]
    random.shuffle(points)
    points=points[0:3]
    points.sort()
    A,B,C=points

    x_1=random.randint(-4,4)
    x_2=random.choice([x for x in range(-5, 4) if x != x_1])
    x_3=random.choice([x for x in range(-5, 5) if x != x_1 and x != x_2])
    y_1,y_2,y_3=f.subs(x,x_1), f.subs(x,x_2), f.subs(x,x_3)

    m = random.choice([i for i in range(1, 3) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])
    p = random.choice([i for i in range(-3, 3) if i!=0])
    ta,tb,tc=sp.symbols("a b c")

    noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+bx+c$ đi qua các điểm ${A}({x_1};{y_1})$, ${B}({x_2};{y_2})$ và ${C}({x_3};{y_3})$."
        f" Tính $P={latex(m*ta+n*tb+p*tc)}$.")
    dap_an=m*a+n*b+p*c

    noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$, ${B}({x_2};{y_2})$ và ${C}({x_3};{y_3})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1+tc)}={y_1} \\\\ \n\
        {latex(ta*x_2**2+tb*x_2+tc)}={y_2}\\\\ \n\
        {latex(ta*x_3**2+tb*x_3+tc)}={y_3}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow\\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        b={b} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"

        f"Vậy $P={latex(m*ta+n*tb+p*tc)}={dap_an}$." )

    noi_dung=noi_dung.replace("+-","-")    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B2_18]-SA-M3. Tìm 3 hệ số của hàm bậc hai có đỉnh và đồ thị đi qua 1 điểm.
def npl_mk_L10_C3_B2_18():
    x=sp.symbols("x")
    a = random.choice([i for i in range(-4, 4) if i!=0])
    b = random.choice([2,4])*a
    c = random.choice([i for i in range(-7, 7) if i!=0])
    f=a*x**2+b*x+c

    points = [chr(i) for i in range(ord('A'), ord('N') + 1)]
    random.shuffle(points)
    A=points[0]  
 
    x_0=int(-b/(2*a))
    x_1=random.choice([i for i in range(-5, 5) if i!=x_0])

    y_0,y_1=f.subs(x,x_0), f.subs(x,x_1)

    m = random.choice([i for i in range(1, 3) if i!=0])
    n = random.choice([i for i in range(-3, 3) if i!=0])
    p = random.choice([i for i in range(-3, 3) if i!=0])
    ta,tb,tc=sp.symbols("a b c")

    noi_dung = (
        f"Biết đồ thị hàm số $y=ax^2+bx+c$ đi qua điểm ${A}({x_1};{y_1})$ và có đỉnh $I({phan_so(x_0)};{phan_so(y_0)})$."
        f" Tính $P={latex(m*ta+n*tb+p*tc)}$.")
    dap_an=m*a+n*b+p*c

    noi_dung_loigiai=(
        f"Đồ thị hàm số đi qua ${A}({x_1};{y_1})$ và có đỉnh $I({phan_so(x_0)};{phan_so(y_0)})$ nên ta có:\n\n"
        f"$\\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1+tc)}={y_1} \\\\ \n\
        {latex(ta*x_0**2+tb*x_0+tc)}={phan_so(y_0)}\\\\ \n\
        {latex(-tb/(2*ta))}={phan_so(x_0)}\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
        {latex(ta*x_1**2+tb*x_1+tc)}={y_1} \\\\ \n\
        {latex(ta*x_0**2+tb*x_0+tc)}={phan_so(y_0)}\\\\ \n\
        {latex(-2*ta*x_0+tb)}=0\n\
        \\end{{array}} \\right.$"

        f"$\\Rightarrow\\left\\{{ \\begin{{array}}{{l}} \n\
        a={a} \\\\ \n\
        b={b} \\\\ \n\
        c={c}\n\
        \\end{{array}} \\right.$\n\n"

        f"Vậy $P={latex(m*ta+n*tb+p*tc)}={dap_an}$." )

    noi_dung=noi_dung.replace("+-","-")    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B2_19]-SA-M3. Bài toán thực tế tìm tiền lãi lớn nhất
def npl_mk_L10_C3_B2_19():
    x=sp.symbols("x")
    
    t = random.randint(20, 40)
    p = t+random.randint(5,20)
    
    while (t + p) % 2 != 0:       
        
        t = random.randint(20, 40)
        p = t+random.randint(5,20)

    f=(p-x)*(x-t)
    a,b,c=-1, t+p, -t*p
    x_0=int(-b/(2*a))
    y_0=f.subs(x,x_0)

    ten=random.choice(["A","B","X","Y","Z"])
    code_hinh=(f"\\begin{{tikzpicture}} \n\
                \\tkzTabInit[nocadre=false, lgt=1, espcl=1.5] \n\
                {{$x$ /1,$y$ /2}}\n\
                {{$0$, ${x_0}$, $+\\infty$}} \n\
                \\tkzTabVar{{-/$-\\infty$ , +/ ${y_0}$ /, -/$-\\infty$ /}} \n\
                \\end{{tikzpicture}}\n")
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    noi_dung = (
    f"Một cửa hàng nhập một sản phẩm {ten} với giá là ${{{t}}}(USD)$ ."
    f" Cửa hàng ước tính rằng nếu sản phẩm này được bán với giá ${{x}}(USD)$ thì mỗi tháng khách hàng sẽ mua $({p}-x)$ sản phẩm."
    f" Hỏi cửa hàng bán sản phẩm {ten} giá bao nhiêu thì thu được nhiều lãi nhất?"
    )
    dap_an=x_0

    noi_dung_loigiai=(
    f"Gọi ${{y}}$ là số tiền lãi. Khi đó:\n\n"
    f"$y=({p}-x)(x-{t})={latex(expand(f))}$.\n\n"
    f"Bảng biến thiên:\n {file_name}\n"
    f"Ta thấy $y_{{max}}={phan_so(y_0)}$ khi $x={x_0}$."
    )

    noi_dung_loigiai_latex=(
    f"Gọi ${{y}}$ là số tiền lãi. Khi đó:\n\n"
    f"$y=({p}-x)(x-{t})={latex(expand(f))}$.\n\n"
    f"Bảng biến thiên:\n\n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
    f"Ta thấy $y_{{max}}={phan_so(y_0)}$ khi $x={x_0}$."
    )  
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai_latex} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C3_B2_20]-SA-M3. Bài toán đường đi quả bóng
def npl_mk_L10_C3_B2_20():
    t=sp.symbols("t")
    m=random.randint(-2,-1)
    n=random.randint(5,6)   

    c=random.choice([0.4, 0.5, 0.6, 0.7, 0.8, 1, 1.1, 1.2])
    st_c=f"{c}".replace(".",",")
    k=c/(m*n)

    f=k*(t-m)*(t-n)
    a,b=k, -k*m-k*n    

    t1=random.choice([0.5, 0.6, 0.8, 1, 1.2, 1.3, 1.5 ])
    t2=t1+random.choice([0.5, 1, 0.8, 2, 2.2, 2.5, 3.5])

    st_1=f"{t1}".replace(".",",")
    st_2=f"{t2}".replace(".",",")

    h1, h2 = f.subs(t,t1), f.subs(t,t2)

    chon=random.randint(1,2)

    noi_dung_loigiai=(
    f"Giả sử $h(t)=at^2+bt+c$ là độ cao của quả bóng theo thời gian ${{t}}$.\n\n"
    f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    h(0)={st_c} \\\\ \n\
    h({st_1})={phan_so(h1)}\\\\ \n\
    h({st_2})={phan_so(h2)}\n\
    \\end{{array}} \\right.$"

    f"$\\left\\{{ \\begin{{array}}{{l}} \n\
    c={st_c} \\\\ \n\
    a.{st_1}^2+b.{st_1}+{st_c}={phan_so(h1)}\\\\ \n\
    a.{st_2}^2+b.{st_2}+{st_c}={phan_so(h2)}\n\
    \\end{{array}} \\right.$ \n"

    f"$\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
    a={phan_so(a)} \\\\ \n\
    b={phan_so(b)} \\\\ \n\
    c={phan_so(c)}\n\
    \\end{{array}} \\right.$\n\n"

    f"$h(t)={phan_so(a)}t^2+{phan_so(b)}t+{phan_so(c)}$.\n\n" )
    
    if chon==1:
        x_0=-b/(2*a)
        y_0=f.subs(t,x_0)
        noi_dung = (
    f"Một quả bóng được cầu thủ sút lên rồi rơi xuống theo quỹ đạo là một parabol."
    f" Biết rằng ban đầu quả bóng được sút lên từ độ cao {st_c} m,"
    f" sau đó {st_1} giây quả bóng đạt độ cao ${phan_so(h1)}$ m và sau {st_2} giây quả bóng đạt độ cao ${phan_so(h2)}$ m."
    f" Hỏi độ cao cao nhất mà quả bóng đạt được là bao nhiêu mét (kết quả làm tròn đến hàng phần mười)?"
    )
        dap_an=f"{round(y_0,1):.1f}".replace(".",",")

        noi_dung_loigiai+=f"Độ cao của quả bóng đạt được bằng $h_{{max}}={phan_so(y_0)}={dap_an}$ m khi $t={phan_so(x_0)}$."
    
    if chon==2:
        t0=1+random.randint(1,10)/10
        while t0==t1 or t0==t2:
            t0=random.choice([1+random.randint(1,10)/10, 2+random.randint(1,10)/10, 3+random.randint(1,10)/10])

        st_t0=f"{round(t0,1):.1f}".replace(".",",")
        dap_an=f"{round(f.subs(t,t0),1):.1f}".replace(".",",")

        noi_dung = (
    f"Một quả bóng được cầu thủ sút lên rồi rơi xuống theo quỹ đạo là một parabol."
    f" Biết rằng ban đầu quả bóng được sút lên từ độ cao {st_c} m,"
    f" sau đó {st_1} giây quả bóng đạt độ cao ${phan_so(h1)}$ m và sau {st_2} giây quả bóng đạt độ cao ${phan_so(h2)}$ m."
    f" Tìm độ cao mà quả bóng đạt được sau {st_t0} giây kể từ khi sút bóng (kết quả làm tròn đến hàng phần mười)?"
    )
        noi_dung_loigiai+=f"Độ cao của quả bóng đạt được khi $t={st_t0}$ là $h={dap_an}$ m."  

     
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an



#[D10_C3_B2_21]-SA-M3. Bài toán thực tế về đồ thị bậc 2
def npl_mk_L10_C3_B2_21():
    a=random.choice([  1/3,  1/4, 1/5 , 2/3,  3/8, 3/10, 2/5, 2/7, 1/6, 1/8, 1/12, 1/7]) 
    a1=random.randint(3,8)
    b=phan_so(a*a1**2)
    c=a1-random.randint(1,2)

    a2=phan_so(a)
    x=symbols("x")
    code_hinh=r"""
        \begin{tikzpicture}
            
            % Vẽ parabol
            \draw[thick, blue] 
            plot[domain=-4:4, samples=100] (\x, {0.12*\x*\x}); % Parabol y = -0.5x^2 + 4
            % Đánh dấu và ghi nhãn hai chân cổng
            \fill[green] (-4, 1.92) circle(2pt); % Chân trái (x = -sqrt(8))
            \node[below left] at (-4, 1.92) {\( A \)}; % Nhãn chân trái là A
            
            \fill[green] (4, 1.92) circle(2pt); % Chân phải (x = sqrt(8))
            \node[below right] at (4, 1.92) {\( B \)}; % Nhãn chân phải là B
            
            % Nối hai chân cổng bằng nét đứt
                \draw[dashed, gray] (-4, 1.92) -- (-2, 0.48);
                    \draw[dashed, gray] (4, 1.92) -- (2, 0.48);  % 
            \draw[thick](-4, 0) -- (4, 0); %
            \draw[thick](-4, 0) -- (4, 0); % 
                \draw[thick](-4, 1.92) -- (-4, 0); %
                \draw[thick](4, 1.92) -- (4, 0); %
                    \fill[green] (-4, 0) circle(2pt); % Chân trái (x = -sqrt(8))
                \node[below left] at (-4, 0) {\( C \)}; % Nhãn chân trái là A
                
                \fill[green] (4, 0) circle(2pt); % Chân phải (x = sqrt(8))
                \node[below right] at (4, 0) {\( D \)}; % Nhãn chân phải là B
                    \draw[dashed, gray] (-2, 0.48) -- (2, 0.48); % 
                            \fill[green] (-2, 0.48) circle(2pt); % Chân trái (x = -sqrt(8))
                    \node[below left] at (-2, 0.48) {\( M \)}; % Nhãn chân trái là A
                    
                    \fill[green] (2, 0.48) circle(2pt); % Chân phải (x = sqrt(8))
                    \node[below right] at (2, 0.48) {\(N \)}; % Nhãn chân phải là B
        \end{tikzpicture}
    """
    code_hinh1=r"""
        \begin{tikzpicture}
            \draw[->] (-4.5,0) -- (4.5, 0) node[right] {\( x \)}; % Trục Ox
            \draw[->] (0, -1) -- (0, 5) node[above] {\( y \)};    % Trục Oy
        % Vẽ parabol
        \draw[thick, blue] 
        plot[domain=-4:4, samples=100] (\x, {0.12*\x*\x}); % Parabol y = -0.5x^2 + 4
        % Đánh dấu và ghi nhãn hai chân cổng
        \fill[green] (-4, 1.92) circle(2pt); % Chân trái (x = -sqrt(8))
        \node[below left] at (-4, 1.92) {\( A \)}; % Nhãn chân trái là A
        
        \fill[green] (4, 1.92) circle(2pt); % Chân phải (x = sqrt(8))
        \node[below right] at (4, 1.92) {\( B \)}; % Nhãn chân phải là B
        
        % Nối hai chân cổng bằng nét đứt
            \draw[dashed, gray] (-4, 1.92) -- (-2, 0.48);
                    \draw[dashed, gray] (4, 1.92) -- (2, 0.48);
        \draw[thick](-4, 0) -- (4, 0); % 
        \draw[dashed, gray](-4, 1.92) -- (4, 1.92); % 
        \draw[thick](-4, 1.92) -- (-4, 0); %
        \draw[thick](4, 1.92) -- (4, 0); %
        \fill[green] (-4, 0) circle(2pt); % Chân trái (x = -sqrt(8))
        \node[below left] at (-4, 0) {\( C \)}; % Nhãn chân trái là A
        
        \fill[green] (4, 0) circle(2pt); % Chân phải (x = sqrt(8))
        \node[below right] at (4, 0) {\( D \)}; % Nhãn chân phải là B
        \draw[dashed, gray] (-2, 0.48) -- (2, 0.48); % 
        \fill[green] (-2, 0.48) circle(2pt); % Chân trái (x = -sqrt(8))
        \node[below left] at (-2, 0.48) {\( M \)}; % Nhãn chân trái là A
        
        \fill[green] (2, 0.48) circle(2pt); % Chân phải (x = sqrt(8))
        \node[below right] at (2, 0.48) {\(N \)}; % Nhãn chân phải là B
    \end{tikzpicture}
    """
    noi_dung = (f"Một mô hình mô phỏng cây cầu treo có trụ tháp đôi cao $BD=AC={phan_so(a*a1**2)}$ m và cách nhau $AB={2*a1}$ m. "
                f"Các dây cáp có dạng đồ thị là một Parabol như hình. Một dây nối hai điểm ${{M}}$ và ${{N}}$ trên dây cáp như hình. Biết dây nối cách mặt của cây cầu là ${{{phan_so(a*(c/2)**2)}}}$. Người ta muốn chăng một đoạn dây đèn trang trí nối thẳng từ điểm ${{A}}$ đến ${{M}}$ đến ${{N}}$ đến ${{B}}$. Chiều dài đoạn dây đèn là bao nhiêu. (Chỉ làm tròn kết quả cuối cùng đến chữ số thập phân thứ nhất) ")
    t1=a*a1**2 
    t2=a*(c/2)**2
    kq=round(  abs(c)+ 2*sqrt( (a1-(c/2))**2+(t2-t1)**2 ), 1)
    kq=str(kq).replace(".",",")
    noi_dung_loigiai=(f" Đặt hệ trục toạ độ Oxy vào hình vẽ sao cho đỉnh Parabol trùng với gốc toạ độ. \n\n"
                    f" Parabol đi qua điểm $B\\left({a1}; {b}\\right)$ nên tìm được hệ số $a={a2}$ \n\n"
                    f"Điểm ${{M}}$, ${{N}}$ có tung độ là ${{{phan_so(a*(c/2)**2)}}}$ suy ra hoành độ của ${{N}}$ là ${{{phan_so(c/2)}}}$ và hoành độ của ${{M}}$ là ${{{phan_so(-c/2)}}}$\n\n"
                  f" Độ dài $MN={abs(c)}$m, $AM=BN= \\sqrt{{ \\left({a1}-{phan_so(c/2)} \\right)^{{2}}+ \\left({b}-{phan_so(a*(c/2)**2)} \\right)^{{2}} }}$ \n\n"
                  f" Chiều dài dây đèn là $MN+AM+BN \\approx {kq} $" 
                  )

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    code1 = my_module.moi_truong_anh_latex(code_hinh1)
    file_name1=my_module.pdftoimage_timename(code1)
    loigiai_word=f"Lời giải:\n {file_name1} \n\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n{code_hinh1} \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an


#[D10_C3_B2_22]-M3. Toán thực tế ứng dụng đồ thị hàm số bậc hai tìm lợi nhuận lớn nhất
def npl_mk_L10_C3_B2_22():
    x=symbols("x")
    chon =random.randint(1,2)
    if chon ==1:
        x1=random.randint(4,8)
        c=x1*3
    if chon ==2:
        x1=2*random.randint(3,4)
        c=x1*4
    a=random.randint(10,30)
    B=2*a*(x1-random.randint(1,2))
    e=B+a*c 
    x2=e/a
    x0=(x1+x2)/2 
    
    if x0==c: 
        c=x1+2*random.randint(1,4)
        e=B+a*c 
        x2=e/a
        x0=(x1+x2)/2 
    kq= phan_so((e-a*x0)*(x0-x1))
    noi_dung = f"Lợi nhuận bán sách ${{X}}$ của một cửa hàng là một hàm số bậc hai $P(x)={{{latex(expand( (e-a*x)*(x-x1)))}}}$ (USD) với ${{x}}$ (USD) là giá bán một quyển sách ${{X}}$. Lợi nhuận cao nhất mà của hàng đạt được là:"

    noi_dung_loigiai=(
    f"Đồ thị ${{P(x)}}$ là một parabol có đỉnh $I({phan_so(x0)};{kq})$.\n\n"
    f"Do đó lợi nhuận cao nhất là ${{{kq}}}$ USD khi giá một cuốn sách bán ra là ${{{phan_so(x0)}}}$ USD.")

    kq=f" ${{{kq}}}$ (USD)"
    ds=[f" ${{{phan_so((e-a*x0)*(x0-x1)-random.randint(1,2))}}}$ (USD)",
    f" ${{{phan_so((e-a*x0)*(x0-x1)+random.randint(1,2))}}}$ (USD)",
    f" ${{{phan_so((e-a*x0)*(x0-x1)-random.randint(3,4))}}}$ (USD)",
    f" ${{{phan_so((e-a*x0)*(x0-x1)+random.randint(3,4))}}}$ (USD)",
    f" ${{{phan_so((e-a*x0)*(x0-x1)-random.randint(5,6))}}}$ (USD)", 
    f" ${{{phan_so((e-a*x0)*(x0-x1)+random.randint(5,6))}}}$ (USD)" ]
    kq2,kq3,kq4=random.sample(ds, 3)


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

#[D10_C3_B2_23]-M3. Toán thực tế ứng dụng tìm giá bán để lợi nhuận thoả điều kiện cho trước
def npl_mk_L10_C3_B2_23():
    x=symbols("x")
    chon =random.randint(1,2)
    if chon ==1:
        x1=random.randint(4,8)
        c=x1*3
    if chon ==2:
        x1=2*random.randint(3,4)
        c=x1*4
    a=random.randint(10,30)
    B=2*a*(x1-random.randint(1,2))
    e=B+a*c 
    x2=e/a
    x0=(x1+x2)/2 
    

    x4=random.choice([i for i in range(x1+1,int(x0-1))]) 
    x5 =phan_so(2*x0-x4) 
    f4 =phan_so((e-a*x4)*(x4-x1))
    x0=phan_so(x0)
    x2=phan_so(x2)
    noi_dung = f"Lợi nhuận bán sách ${{X}}$ của một cửa hàng là một hàm số bậc hai $P(x)={{{latex(expand( (e-a*x)*(x-x1)))}}}$ (USD) với ${{x}}$ (USD) là giá bán một quyển sách ${{X}}$. Muốn lợi nhuận thu được lớn hơn ${{{f4}}}$ USD thì giá bán sách phải trong phạm vi:"

    noi_dung_loigiai=(f" Giải bất phương trình $P(x)={{{latex(expand( (e-a*x)*(x-x1)))}}} \\ge {f4}$ \n\n"
                        f" Ta được $ x \\in ({x4};{x5})$ \n\n"
    f"Muốn tổng lợi nhuận thu được lớn hơn ${{{f4}}}$ USD thì giá bán mới phải thuộc khoảng $({x4};{x5})$ ")

    kq=f" $({x4};{x5})$ (USD)"
    ds=[f"$({phan_so(x1)};{x5})$ (USD)", 
    f" $({phan_so(x1)};{x0})$ (USD)", 
    f" $({phan_so(x1)};{x4})$ (USD)", 
    f" $({x0};{x2})$ (USD)",
    f" $({phan_so(x4)};{x2})$ (USD)" ]
    kq2,kq3,kq4=random.sample(ds, 3)


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

def thay_cong_tru(st):
    return st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("1x","x").replace("1y","y").replace("-1x","-x").replace("-1y","-y")
    
#[D10_C3_B2_24]-M3. Tìm trục đối xứng của Parabol khi biết toạ độ giao điểm của nó với trục hoành.
def npl_mk_L10_C3_B2_24():
    a=random.choice([i for i in range(-5,5) if i!=0])
    while True:
        x1,x2=random.sample([i for i in range(-10,10)],2)
        if x1+x2!=0:
            break
    x0=(x1+x2)/2 
    x0=phan_so(x0)
    x=symbols("x")
    noi_dung=f" Biết đồ thị hàm số bậc hai $y=f(x)=ax^{{2}}+bx+c$ ($ a \\ne 0$) cắt trục hoành tại hai điểm $A({x1};0)$ và $B({x2};0)$. Trục đối xứng của đồ thị là đường thẳng nào?"
    noi_dung_loigiai=f" Trục đối xứng là đường thẳng $x= \\dfrac{{{x1}+{x2}}}{{2}}={x0}$"

    kq=f" $x={x0}$"
    kq2=f"$x={phan_so(x1+x2)}$ "
    kq3=f"$x={phan_so((x1+x2)/3)}$"
    kq4=f"$x={phan_so((x1+x2)/4)}$ "
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

#[D10_C3_B2_25]-TL-M4. Tìm m để phương trình f(|x|)=m có nhiều nghiệm nhất
def npl_mk_L10_C3_B2_25():
    x=symbols("x")
    a=random.randint(1,5)
    x1=random.randint(1,4) 
    x2=x1+random.randint(1,4)
    u= (-a*(x2-x1)**2)/4
    v=a*x1*x2   
    kq=len([x for x in range(int(u+1), int(v)) if u < x < v])

    noi_dung = f"Có bao nhiêu giá trị nguyên của ${{m}}$ để phương trình ${latex(expand(a*(abs(x)-x1)*(abs(x)-x2)))}=m$ có nhiều nghiệm nhất."

    noi_dung_loigiai=(f" Vẽ đồ thị hàm số $y={latex(expand(a*(abs(x)-x1)*(abs(x)-x2)))}$ \n\n"
    f" Khi ${phan_so(u)}<m < {phan_so(v)}$ thì đường thẳng ${{y=m}}$ cắt đồ thị hàm số tại nhiều điểm nhất. \n\n"
    f"Có ${{{kq}}}$ giá trị nguyên của ${{m}}$ để phương trình ${latex(expand(a*(abs(x)-x1)*(abs(x)-x2)))}=m$ có nhiều nghiệm nhất.")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an


#[D10_C3_B2_26]-TF-M4. Tìm m để phương trình f(|x|)=m có nghiệm thoả đk
def npl_mk_L10_C3_B2_26():
    x=symbols("x")
    a=random.randint(1,5)
    x1=random.randint(1,4) 
    x2=x1+random.randint(1,4)
    x3=random.choice([i for i in range(-6,6) if i!=x1 and i!=x2])
    f= a*(x3-x1)*(x3-x2)
    u= (-a*(x2-x1)**2)/4
    v=a*x1*x2   
    kq=len([x for x in range(int(u+1), int(v)) if u < x < v])
    noi_dung = f"Cho hàm số $y=f(x)={latex(expand(a*(x-x1)*(x-x2)))}$ có đồ thị là parabol ${{(P)}}$ . Xét tính đúng-sai của các khẳng định sau. "     
    debai_word= f"{noi_dung}\n"
    
    kq3_T=f"*Đỉnh của ${{(P)}}$ có toạ độ là $\\left({phan_so( (x1+x2)/2)}; {phan_so(u)} \\right)$" 
    kq3_F=f"Đỉnh của ${{(P)}}$ có toạ độ là $\\left({phan_so( (x1-x2)/2)}; {phan_so(u)} \\right)$ "
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"Đỉnh của ${{(P)}}$ có toạ độ là $\\left({phan_so( (x1+x2)/2)}; {phan_so(u)} \\right)$ "
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*${{(P)}}$ cắt trục hoành tại hai điểm phân biệt là ${{({x1};0)}}$ và ${{({x2};0)}}$ "
    kq2_F=random.choice([f"${{(P)}}$ cắt trục hoành tại hai điểm phân biệt là ${{({x1-1};0)}}$ và ${{({x2};0)}}$", f"${{(P)}}$ nằm hoàn toàn phía trên trục hoành", f"${{(P)}}$ nằm hoàn toàn phía dưới trục hoành" ])
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"${{(P)}}$ cắt trục hoành tại hai điểm phân biệt là ${{({x1};0)}}$ và ${{({x2};0)}}$  "
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq1_T=f"* ${{P}}$ đi qua điểm có toạ độ $\\left({x3}; {phan_so(f)} \\right)$" 
    kq1_F=f"${{P}}$ đi qua điểm có toạ độ $\\left({x3}; {phan_so(f+1)} \\right)$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"${{P}}$ đi qua điểm có toạ độ $\\left({x3}; {phan_so(f)} \\right)$ "
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"*Có ${{{kq}}}$ giá trị nguyên của ${{m}}$ để phương trình ${latex(expand(a*(abs(x)-x1)*(abs(x)-x2)))}=m$ có nhiều nghiệm nhất "
    kq4_F=f"Có ${{{kq+random.randint(1,2)}}}$ giá trị nguyên của ${{m}}$ để phương trình ${latex(expand(a*(abs(x)-x1)*(abs(x)-x2)))}=m$ có nhiều nghiệm nhất " 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f" Vẽ đồ thị hàm số $y={latex(expand(a*(abs(x)-x1)*(abs(x)-x2)))}$ \n\n"
    f" Khi ${phan_so(u)} <m < {phan_so(v)}$ thì đường thẳng ${{y=m}}$ cắt đồ thị hàm số tại nhiều điểm nhất. \n\n"
    f"Có ${{{kq}}}$ giá trị nguyên của ${{m}}$ để phương trình ${latex(expand(a*(abs(x)-x1)*(abs(x)-x2)))}=m$ có nhiều nghiệm nhất")
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

#[D10_C3_B2_27]-SA-M3. Tính chiều cao của cổng Parabol
def npl_mk_L10_C3_B2_27():
    A=random.choice(["Nam", "Lam","Nghĩa", "Hà", "Khôi", "Quân", "Xuân", "Tâm", "Hoàng"])
    x1=random.randint(5,20)
    a= random.randint(-5, -1)
    b=-x1*a 
    x2=random.choice([0.5, 1, 1.5, 1.2, 1.3, 1.4, 1.6])
    x=symbols("x")

    c=a*x2**2+b*x2 
    x0=-b/(2*a) 
    y0=a*x0**2+b*x0 

    x2=str(x2).replace(".",",")
    c=str(round(c,2)).replace(".",",").replace(",0","")
    y0=str(round(y0,1)).replace(".",",").replace(",0","")
    kq=y0

    noi_dung = f" Bạn {A} muốn đo chiều cao của một cái cổng hình Parabol. Biết khoảng cách giữa hai chân cổng là ${{{x1}}}$ mét, chiều cao của cổng tính từ điểm trên mặt đất cách chân cổng ${{{x2}}}$m là ${{{c}}}$m. Em hãy giúp {A} tính xem chiều cao của cổng là bao nhiêu. (Chỉ được làm tròn kết quả cuối cùng đến hàng phần mười)."

    noi_dung_loigiai=(f" Chọn hệ trục toạ độ ${{Oxy}}$ sao cho một chân của cổng trùng gốc toạ độ, chân còn lại trên tia ${{Ox}}$. Khi đó cổng là một phần của Parabol có dạng ${{y=ax^{{2}}+bx }}$ \n\n"
    f" Parabol đi qua các điểm có toạ độ $({x2}; {c})$ và $({x1}; 0)$ \n\n nên ta tìm được phương trình là $y={latex(a*x**2+b*x)}$.\n\n"
    f" Chiều cao của cổng chính là $f \\left(\\dfrac{{-b}}{{2a}} \\right)= {kq}$ mét")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an    


#[D10_C3_B2_28]-SA-M3. Tính chiều cao của cổng Parabol 2
def npl_mk_L10_C3_B2_28():
    x1=random.randint(5,20)
    A= random.choice([-0.25, -1/3, -0.2, -0.4])
    c=random.randint(4,8)
    
    a=int(sqrt(-c/A))-1
    
    x=symbols("x")
    b=A*(a/2)**2+c
    
    y0=f"{round(2*sqrt(-c/A),1):.1f}".replace(".",",").replace(",0","")
    kq=y0
    code_hinh=r"""

\begin{tikzpicture}[scale=0.5,thick,>=stealth,font=\footnotesize,cyan]
        \draw[line width=3pt,magenta,smooth,samples=100,domain=-4:4] plot(\x,{-0.25*(\x)^2});
        \draw[dashed,thin](2,-1)node[above]{ E};
        \draw[dashed,thin](-2,-1)node[above]{F};
        \draw[dashed,thin](-4,-4)node[below]{ A};
        \draw[dashed,thin](4,-4)node[below]{B};
        \draw[thick](2,-1)--(-2,-1)--(-2,-4)node[below]{ C}--(2,-4)node[below]{D}--(2,-1);
        \draw[thick](-4,-4)--(4,-4);
        \draw (0,0) node[above] { $G$};
        \end{tikzpicture}
    """
    noi_dung = f"   Một chiếc cổng hình Parabol bao gồm một cửa chính hình chữ nhật ở giữa và hai cánh cửa phụ hai bên như hình vẽ. Biết chiều cao cổng Parabol là ${{{c}}}$ m còn kích thước cửa ở giữa là $CD={{{phan_so(a)}}}$m; $DE={{{phan_so(b)}}}$ m. Khoảng cách giữa hai điểm ${{A}}$ và ${{B}}$ là: \n\n(Làm tròn kết quả đến hàng phần mười)."

    noi_dung_loigiai=(f" Chọn hệ trục toạ độ ${{Oxy}}$ sao cho gốc toạ độ là trung điểm của ${{AB}}$, ${{Ox}}$ trùng với đường thẳng ${{AB}}$. Khi đó cổng là một phần của Parabol có dạng ${{y=ax^{{2}}+c}}$ \n\n"
    f" Parabol đi qua các điểm có toạ độ $\\left({phan_so(a/2)}; {phan_so(b)}\\right)$ và $\\left( 0; {c} \\right)$ \n\n nên ta tìm được phương trình là $y={latex(nsimplify(A*x**2+c))}$.\n\n"
    f" Toạ độ $B\\left( {latex(nsimplify(sqrt(-c/A)))}; 0 \\right)$ \n\n"
    f" Khoảng cách $AB= {latex(nsimplify(2*sqrt(-c/A)))} \\approx {kq}$ mét.")
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)            
    debai_word= f"{noi_dung}\n {file_name}"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an    





#[D10_C3_B2_29]-TF-M3. Các câu hỏi về chuyển động của vật khi biết v(t) là hàm số bậc hai. 
def npl_mk_L10_C3_B2_29():
    t=symbols("t")
    a=random.randint(-5,-1)
    x1=2*random.randint(10,20)
    x2=x1-2*random.randint(2,6)
    t3=x1+random.randint(3,10)
    t0=x1-random.randint(3,16)
    t01=(x1-x2)/2
    t5=random.randint(x1-random.randint(4,16),x1)

    noi_dung = f" Một vật chuyển động có hàm vận tốc $v(t)={latex(expand(a*(t-x1)*(t+x2)))}$ (m/t) với ${{t}}$ là thời gian tính bằng giây. Xét tính đúng-sai của các khẳng định sau. "     
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* Tại thời điểm $t={t0}$ giây thì vận tốc của vật là ${{{phan_so(a*(t0-x1)*(t0+x2))}}}$ m/s" 
    kq1_F=f" Tại thời điểm $t={t0}$ giây thì vận tốc của vật là ${{{phan_so(a*(t0-x1)*(t0+x2)+random.randint(5,10))}}}$ m/s"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Tại thời điểm $t={t0}$ giây thì vận tốc của vật là ${{{phan_so(a*(t0-x1)*(t0+x2))}}}$ m/s "
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*Sau ${{{x1}}}$ giây thì vật ngừng chuyển động "
    kq2_F=f"Sau ${{{t3}}}$ giây thì vật ngừng chuyển động  "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Tại thời điểm vật ngừng chuyển động là khi ${{v=0}}$. Giải phương trình ta tìm được sau ${{{x1}}}$ giây thì vật ngừng chuyển động "
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"*Vận tốc lớn nhất mà vật đạt được trong cả quá trình chuyển động là ${{{phan_so(a*(t01-x1)*(t01+x2))}}}$ m/s " 
    kq3_F=f"Vận tốc lớn nhất mà vật đạt được trong cả quá trình chuyển động là ${{{phan_so(a*(t01-x1)*(t01+x2)+random.randint(5,10) )}}}$ m/s "
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f" Vận tốc lớn nhất mà vật đạt được trong cả quá trình chuyển động là ${{{phan_so(a*(t01-x1)*(t01+x2) )}}}$ m/s"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    if t5 > t01:

        kq4_T=f"*Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t01-x1)*(t01+x2))}}}$ m/s  "
        kq4_F=f"Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t5-x1)*(t5+x2))}}}$ m/s " 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" $v(t) $ là hàm số bậc hai đồng biến trên khoảng $(-\\infty; {phan_so(t01)})$ và nghịch biến trên khoảng $({phan_so(t01)};+\\infty)$\n\n "
            f"Vì ${{{phan_so(t5)}}} > {phan_so(t01)}$ nên \n\n"
            f"Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t01-x1)*(t01+x2))}}}$ m/s ")


    if t5==t01:
        t6=t5+random.randint(1,5)
        kq4_T=f"*Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t01-x1)*(t01+x2))}}}$ m/s  "
        kq4_F=f"Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t6-x1)*(t6+x2))}}}$ m/s " 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" $v(t) $ là hàm số bậc hai đồng biến trên khoảng $(-\\infty; {phan_so(t01)})$ và nghịch biến trên khoảng $({phan_so(t01)};+\\infty)$\n\n "
            f"Vì ${{{phan_so(t5)}}} = {phan_so(t01)}$ nên \n\n"
        f"Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t01-x1)*(t01+x2))}}}$ m/s ")

    if t5< t01: 
        kq4_F=f"Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t01-x1)*(t01+x2))}}}$ m/s  "
        kq4_T=f"*Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  ${{{phan_so(a*(t5-x1)*(t5+x2))}}}$ m/s " 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=(f" $v(t) $ là hàm số bậc hai đồng biến trên khoảng $(-\\infty; {phan_so(t01)})$ và nghịch biến trên khoảng $({phan_so(t01)};+\\infty)$\n\n "
            f"Vì ${{{phan_so(t5)}}} < {phan_so(t01)}$ nên \n\n"
        f"Trong ${{{t5}}}$ giây đầu tiên, vận tốc lớn nhất của vật là  $v({t5})={{{phan_so(a*(t5-x1)*(t5+x2))}}}$ m/s ")

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







#[D10_C3_B2_30]-M3. Tìm m để hàm số bậc hai đồng biến, nghịch biến trên khoảng K
def npl_mk_L10_C3_B2_30():
    a=random.choice([i for i in range(-5,5) if i!=0])
    c=random.randint(-10,10)
    u=random.choice([i for i in range(-5,5)])
    v=u+random.randint(1,10)

    x, m=symbols("x m")
    
    if a>0: 
        noi_dung=f" Cho hàm số bậc hai $y={latex(a*x**2-2*m*x+c)}$, với giá trị nào của ${{m}}$ thì hàm số đồng biến trên khoảng $({u}; {v})$?"
        noi_dung_loigiai=f" Hàm số đồng biến trên khoảng $\\left({latex(m/a)}; +\\infty \\right)$ nên để hàm số đồng biến trên khoảng $({u}; {v})$ thì ${latex(m/a)} \\le {u}$ suy ra $m \\le {phan_so(a*u)} $"

        kq=f" $m \\le {phan_so(a*u)}$"
        kq2=f"$m < {phan_so(a*u)}$ "
        kq3=f"$m \\ge {phan_so(a*u)}$"
        kq4=f"$m > {phan_so(a*u)}$ "


    if a>0: 
        noi_dung=f" Cho hàm số bậc hai $y={latex(a*x**2-2*m*x+c)}$, với giá trị nào của ${{m}}$ thì hàm số nghịch biến trên khoảng $({u}; {v})$?"
        noi_dung_loigiai=f" Hàm số nghịch biến trên khoảng $\\left( -\\infty; {latex(m/a)} \\right)$ nên để hàm số nghịch biến trên khoảng $({u}; {v})$ thì ${latex(m/a)} \\ge {v}$ suy ra $m \\ge {phan_so(a*v)}$ "

        kq3=f" $m \\le {phan_so(a*v)}$"
        kq2=f"$m < {phan_so(a*v)}$ "
        kq=f"$m \\ge {phan_so(a*v)}$"
        kq4=f"$m > {phan_so(a*v)}$ "

    if a<0: 
        noi_dung=f" Cho hàm số bậc hai $y={latex(a*x**2-2*m*x+c)}$, với giá trị nào của ${{m}}$ thì hàm số đồng biến trên khoảng $({u}; {v})$?"
        noi_dung_loigiai=f" Hàm số đồng biến trên khoảng $\\left({latex(m/a)}; +\\infty \\right)$ nên để hàm số đồng biến trên khoảng $({u}; {v})$ thì ${latex(m/a)} \\ge {v}$ suy ra $m \\le {phan_so(a*v)} $"

        kq=f" $m \\le {phan_so(a*v)}$"
        kq2=f"$m < {phan_so(a*v)}$ "
        kq3=f"$m \\ge {phan_so(a*u)}$"
        kq4=f"$m > {phan_so(a*u)}$ "


    if a<0: 
        noi_dung=f" Cho hàm số bậc hai $y={latex(a*x**2-2*m*x+c)}$, với giá trị nào của ${{m}}$ thì hàm số nghịch biến trên khoảng $({u}; {v})$?"
        noi_dung_loigiai=f" Hàm số nghịch biến trên khoảng $\\left( -\\infty; {latex(m/a)} \\right)$ nên để hàm số nghịch biến trên khoảng $({u}; {v})$ thì ${latex(m/a)} \\le {u}$ suy ra $m \\ge {phan_so(a*u)}$" 

        kq3=f" $m \\le {phan_so(a*v)}$"
        kq2=f"$m < {phan_so(a*v)}$ "
        kq=f"$m \\ge {phan_so(a*u)}$"
        kq4=f"$m > {phan_so(a*v)}$ "


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






#[D10_C3_B2_31]-M3. Tìm m để hàm số xác định trên đoạn [a,b]
def npl_mk_L10_C3_B2_31():
    a=random.choice([i for i in range(1,5) if i!=0])
    a1=random.choice([i for i in range(-5,5) if i!=0])
    b=random.choice([i for i in range(-5,5) if i!=0])
    u=random.choice([i for i in range(-5,5)])
    v=u+random.randint(1,10)
    x0=-b/(2*a)
    z=a*x0**2+b*x0
    z1=a*u**2+b*u
    z2=a*v**2+b*v 
    x, m =symbols("x m")
    noi_dung=f"Giá trị của tham số ${{m}}$ để hàm số $y=\\dfrac{{{a1}}}{{\\sqrt {{ {latex(a*x**2+b*x-m)}}}}}$ xác định trên $\\left[ {u}; {v} \\right]$ là: "
    if a>0 and u<x0<v:
        noi_dung_loigiai=(f" DKXD là ${latex(a*x**2+b*x-m)} > 0$ với mọi $x \\in \\left[ {u}; {v} \\right]$ \n\n"

                        f" Vẽ BBT của hàm số bậc hai $y={latex(a*x**2+b*x-m)}$ ta có GTNN của hàm số trên $\\left[ {u}; {v} \\right]$ là  ${latex(nsimplify(a*x0**2+b*x0-m))}$ \n\n"
                        f" ${latex(nsimplify(a*x0**2+b*x0-m))} > 0 $ suy ra $m < {phan_so(z)}$")


        pa_A= f"*$m < {phan_so(z)}$"
        pa_B= f"$m > {phan_so(z)}$"
        pa_C= f"$m \\le {phan_so(z)}$"
        pa_D= f"$m \\ge {phan_so(z)}$"

    if a>0 and x0>=v:
        noi_dung_loigiai=(f" DKXD là ${latex(a*x**2+b*x-m)} > 0$ với mọi $x \\in \\left[ {u}; {v} \\right]$ \n\n"
                        f"  Vẽ BBT của hàm số bậc hai $y={latex(a*x**2+b*x-m)}$ ta có GTNN của hàm số trên $\\left[ {u}; {v} \\right]$ là  ${latex(nsimplify(a*v**2+b*v-m))}$ \n\n"
                        f" ${latex(nsimplify(a*v**2+b*v-m))} > 0 $ suy ra $m < {phan_so(z2)}$")


        pa_A= f"*$m < {phan_so(z2)}$"
        pa_B= f"$m > {phan_so(z2)}$"
        pa_C= f"$m \\le {phan_so(z2)}$"
        pa_D= f"$m \\ge {phan_so(z2)}$"


    if a>0 and x0<=u:
        noi_dung_loigiai=(f" DKXD là ${latex(a*x**2+b*x-m)} > 0$ với mọi $x \\in \\left[ {u}; {v} \\right]$ \n\n"
                        f"  Vẽ BBT của hàm số bậc hai $y={latex(a*x**2+b*x-m)}$ ta có  GTNN của hàm số trên $\\left[ {u}; {v} \\right]$ là  ${latex(nsimplify(a*u**2+b*u-m))}$ \n\n"
                        f" ${latex(nsimplify(a*u**2+b*u-m))} > 0 $ suy ra $m < {phan_so(z1)}$")


        pa_A= f"*$m < {phan_so(z1)}$"
        pa_B= f"$m > {phan_so(z1)}$"
        pa_C= f"$m \\le {phan_so(z1)}$"
        pa_D= f"$m \\ge {phan_so(z1)}$"

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





#[D10_C3_B2_32]-TF-M3. Bài tổng hợp về diện tích mảnh vườn
def npl_mk_L10_C3_B2_32():
    A=random.choice(["Xuân", "Thu", "Đông", "Hà", "Mai", "Giang"])
    a=2*random.randint(5,15)
    x=symbols("x")
    x0=a/2 
    x1=x0-random.randint(2,6)
    x2= 2*x0-x1
    u=x1*(a-x1)
    d1=x0*(a-x0)
    e=random.randint(int(d1)-random.randint(1,5),int(d1)+random.randint(1,6) )
    x0=phan_so(x0)
    d=phan_so(d1)
    x1=phan_so(x1)
    x2=phan_so(x2)
    noi_dung = f"Bác {A} dùng ${{{2*a}}}$ mét lưới thép gai rào một mảnh vườn hình chữ nhật để trồng rau. Gọi ${{x}}$ là chiều rộng của mảnh vườn hình chữ nhật. Xét tính đúng-sai của các khẳng định sau. "     
    debai_word= f"{noi_dung}\n"


    kq1_T=f"*Diện tích mảnh vườn $S(x)={latex(expand(x*(a-x)))}$ "
    kq1_F=f"Diện tích mảnh vườn $S(x)={latex(expand(x*(2*a-x)))}$ "
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Diện tích mảnh vườn $S(x)={latex(expand(x*(a-x)))}$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


    if 0<e <= d1: 
        kq2_T=f"* Bác {A} có thể rào mảnh vườn có diện tích là ${{{e}}}m^{{2}}$ " 
        kq2_F=f"Bác {A} không thể rào mảnh vườn có diện tích là ${{{e}}}m^{{2}}$  "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Bác {A} có thể rào mảnh vườn có diện tích là ${{{e}}}m^{{2}}$ vì phương trình có nghiệm dương "
    if e > d1 : 
        kq2_T=f"* Bác {A} không thể rào mảnh vườn có diện tích là ${{{e}}}m^{{2}}$ " 
        kq2_F=f"Bác {A} có thể rào mảnh vườn có diện tích là ${{{e}}}m^{{2}}$  "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Bác {A} không thể rào mảnh vườn có diện tích là ${{{e}}}m^{{2}}$ vì phương trình vô nghiệm"
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"



    kq3_T=f"*Muốn diện tích lớn hơn ${{{phan_so(u)}}}m^{{2}}$ thì chiều rộng phải thuộc khoảng $\\left({x1};{x0}  \\right]$  " 
    kq3_F=f"Muốn diện tích lớn hơn ${{{phan_so(u)}}}m^{{2}}$ thì chiều rộng phải thuộc khoảng $\\left({x1};{x2}  \\right]$ "
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"${latex(expand(x*(a-x)))} > {phan_so(u)}$ \n\n ${latex(nsimplify(expand(x*(a-x)-u)))} > 0$ \n\n ${x1}<x< {x2}$ \n\n Vì $x \\le {x0}$ nên $x\\in \\left({x1};{x0}  \\right].$ "
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"*Mảnh vườn có diện tích lớn nhất nếu chiều rộng là ${{{x0}}}$ m  "
    kq4_F=f"Mảnh vườn có diện tích lớn nhất nếu chiều rộng là ${{{phan_so((a/2)+random.randint(2,10))}}}$ m  " 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"Mảnh vườn có diện tích lớn nhất nếu chiều rộng là ${{{x0}}}$ m "
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



#[D10_C3_B2_33]-SA-M4. Toán thực tế uốn cong miếng tôn 
def npl_mk_L10_C3_B2_33():
    x=symbols("x")
    a=random.randint(7,15)
    x=symbols("x")
    kq=a
    code_hinh=fr"""
        \begin{{tikzpicture}}[scale=1, font=\footnotesize, line join=round, line cap=round, >=stealth]
    \draw (0,0)--(4,0)--++(60:5)--++(180:4)--(0,0);
    \draw (1,0)--++(60:5) (3,0)--++(60:5);
    \draw[stealth-stealth,yshift=-.5cm] (0,0)--(4,0) node[midway,fill=white] {{${4*a}$ cm}};
    \draw[stealth-stealth,yshift=.5cm] (60:5)--++(0:1) node[midway,fill=white] {{$x$ cm}};
    \draw[stealth-stealth,yshift=.5cm] ($(4,0)+(60:5)$)--++(180:1) node[midway,fill=white] {{$x$ cm}};
    \draw[stealth-stealth,yshift=.2cm] (60:5)--++(0:1);
    \draw[stealth-stealth,yshift=.2cm] ($(4,0)+(60:5)$)--++(180:1);
    \draw (8,0)--(10,0)--++(60:5)--++(180:2)--(8,0);
    \draw (8,0)--(8,1)--++(60:5)--++(-90:1);
    \draw (10,0)--(10,1)--++(60:5)--++(-90:1);
 \end{{tikzpicture}}  
 """
    noi_dung = f"Một miếng tôn có bề ngang ${{{4*a}}}$ cm được uốn cong tạo thành máng dẫn nước bằng chia tấm tôn thành ba phần rồi gấp 2 bên lại theo một góc vuông. Hỏi cần gấp hai đầu cùng một đoạn bao nhiêu để tạo ra máng có diện tích mặt cắt lớn nhất cho nước chảy qua được nhiều nhất?"

    noi_dung_loigiai=(f" Gọi ${{x}}$ là độ dài hai đầu gấp tấm tôn \n\n"
    f" Diện tích bề ngang là $S(x)={latex(expand((4*a-2*x)*x))}$\n\n"
    f"${{S(x)}}$ lớn nhất khi $x={a}$ cm")


    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
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


#[D10_C3_B2_34]-SA-M4. Toán thực tế về định giá sản phẩm
def npl_mk_L10_C3_B2_34():
    x=symbols("x")
    a=random.randint(6,12)
    x0=random.randint(1,int(a/2)-1)
    b=random.randint(150,300)
    A=(a-2*x0)*b
    m=random.randint(10,30)
    n=m+a
    x=symbols("x")
    kq=phan_so(n-x0) 
    A1=phan_so(A)
    noi_dung = (f"Một cửa hàng kinh doạnh mặt hàng A với chi phí sản xuất là ${{{m}}}$ triệu đồng và dự định bán ra với giá là ${{{n}}}$ triệu đồng. Với giá bán đó, số sản phẩm mà bên khách hàng đối tác sẽ mua trong một năm là ${{{A1}}}$ sản phẩm. "
                f" Nhằm mục đích đẩy mạnh sản xuất và tiêu thụ sản phẩm này, chủ cửa hàng dự định giảm giá bán và ước tính rằng nếu cứ giảm ${{1}}$ triệu đồng mỗi sản phẩm thì số lượng sản phẩm bán ra trong một năm sẽ tăng thêm ${{{b}}}$ sản phẩm. Cửa hàng phải định giá bán mới của sản phẩm là bao nhiêu, để sau khi thực hiện giảm giá, lợi nhuận thu được sẽ là cao nhất.")

    noi_dung_loigiai=(f" Gọi ${{x}}$ (triệu đồng) là số tiền dự định giảm giá của sản phẩm ($0 \\le x \\le {a}$) \n\n"
    f" Lợi nhuận thu được khi bán mỗi sản phẩm là ${n}-x-{m}={a}-x$\n\n"
    f" Số sản phẩm mà cửa hàng bán ra trong một năm là ${A}+{b}x$ \n\n"
    f"Lợi nhuận mà cửa hàng thu được trong một năm là \n\n $f(x)={latex((a-x)*(A+b*x))}= {latex(nsimplify(expand((a-x)*(A+b*x))))}$ \n\n"
    f"${{f(x)}}$ lớn nhất khi $x={x0}$ \n\n"
    f" Vậy giá bán mới của mỗi sản phẩm A là ${{{n-x0}}}$ triệu đồng thì lợi nhuận thu được cao nhất.")
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\shortans[4]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C3_B2_35]-M1. Tìm điểm thuộc đồ thị hàm số
def npl_mk_L10_C3_B2_35():
    x=symbols("x")
    a=random.choice([i for i in range(-5,5) if i!=0])
    b=random.choice([i for i in range(-5,5) if i!=0]) 
    c=random.choice([i for i in range(-5,5) if i!=0 and i!=a])
    x0,x1,x2,x3=random.sample(range(-5,6),4)

    noi_dung=f" Cho hàm số bậc hai $y={latex(a*x**2+b*x+c)}$ có đồ thị là Parabol ${{(P)}}$, trong các điểm sau điểm nào thuộc đồ thị hàm số?"

    noi_dung_loigiai=f" Điểm thuộc đồ thị hàm số là $\\left( {x0};{phan_so(a*x0**2+b*x0+c)} \\right)$"


    pa_A= f"*$\\left( {x0};{phan_so(a*x0**2+b*x0+c)} \\right)$"
    pa_B= f"$\\left( {x1};{phan_so(a*x1**2+b*x1)} \\right)$"
    pa_C= f"$\\left( {x2};{phan_so(a*x2**2+b*x2)} \\right)$"
    pa_D= f"$\\left( {x3};{phan_so(a*x3**2+b*x3)} \\right)$"

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








#[D10_C3_B2_36]-M2. Tìm GTLN (GTNN) của hàm số bậc hai trên R
def npl_mk_L10_C3_B2_36():
    x=symbols("x")
    b=random.choice([i for i in range(-5,5) if i!=0]) 
    c=random.choice([i for i in range(-5,5) if i!=0 ])

    chon =random.randint(1,2)
    if chon ==1:
        a=random.randint(-5,-1)
        x0=-b/(2*a)
        y0=a*x0**2+b*x0+c
        noi_dung=f" Giá trị lớn nhất của hàm số bậc hai $y={latex(a*x**2+b*x+c)}$ là:"

        noi_dung_loigiai=f" Giá trị lớn nhất của hàm số là ${{{phan_so(y0)}}}$."
    if chon ==2:
        a=random.randint(1,5)
        x0=-b/(2*a)
        y0=a*x0**2+b*x0+c
        noi_dung=f" Giá trị nhỏ nhất của hàm số bậc hai $y={latex(a*x**2+b*x+c)}$ là:"

        noi_dung_loigiai=f" Giá trị nhỏ nhất của hàm số là ${{{phan_so(y0)}}}$."
    kq=f"${{{phan_so(y0)}}}$ "
    kq_F=[  f"${{{phan_so(y0+random.randint(1,2))}}}$ ", f"${{{phan_so(y0-random.randint(1,2))}}}$ ", f"${{{phan_so(y0-random.randint(3,4))}}}$ ", f"${{{phan_so(y0+random.randint(3,4))}}}$ ", f"${{{phan_so(y0-random.randint(5,6))}}}$ "]
    kq2,kq3,kq4=random.sample(kq_F,3)

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





#[D10_C3_B2_37]-M2. Tìm GTLN (GTNN) của hàm số bậc hai trên [a,b]
def npl_mk_L10_C3_B2_37():
    x=symbols("x")
    b=random.choice([i for i in range(-5,5) if i!=0]) 
    c=random.choice([i for i in range(-5,5) if i!=0 ])
    m=random.randint(-5,5)
    n=m+random.randint(2,5)
    chon =random.randint(1,2)
    a=random.choice([i for i in range(-5,5) if i!=0]) 
    x0=-b/(2*a)
    y01=a*x0**2+b*x0+c
    y02=a*m**2+b*m+c
    y03=a*n**2+b*n+c
    if m <= x0 <=n: 
        y0=max(y01,y02,y03)
        y=min(y01,y02,y03)
    if x0< m or x0> n: 
        y0=max(y02,y03)
        y=min(y02,y03)
    if chon ==1:

        noi_dung=f" Giá trị lớn nhất của hàm số bậc hai $y={latex(a*x**2+b*x+c)}$ trên $\\left[ {m}; {n} \\right]$ là "

        noi_dung_loigiai=f" Sử dụng BBT ta tìm được giá trị lớn nhất của hàm số ${{{phan_so(y0)}}}$ trên $\\left[ {m}; {n} \\right]$ là ${{{phan_so(y0)}}}$"
        kq=f"${{{phan_so(y0)}}}$ "
        kq_F=[  f"${{{phan_so(y0+random.randint(1,2))}}}$ ", f"${{{phan_so(y0-random.randint(1,2))}}}$ ", f"${{{phan_so(y0-random.randint(3,4))}}}$ ", f"${{{phan_so(y0+random.randint(3,4))}}}$ ", f"${{{phan_so(y0-random.randint(5,6))}}}$ "]
    if chon ==2:

        noi_dung=f" Giá trị nhỏ nhất của hàm số bậc hai $y={latex(a*x**2+b*x+c)}$ trên $\\left[ {m}; {n} \\right]$ là:"

        noi_dung_loigiai=f" Sử dụng BBT ta tìm được giá trị nhỏ nhất của hàm số ${{{phan_so(y0)}}}$ trên $\\left[ {m}; {n} \\right]$ là ${{{phan_so(y)}}}$."

        kq=f"${{{phan_so(y)}}}$ "
        kq_F=[  f"${{{phan_so(y+random.randint(1,2))}}}$ ", f"${{{phan_so(y-random.randint(1,2))}}}$ ", f"${{{phan_so(y-random.randint(3,4))}}}$ ", f"${{{phan_so(y+random.randint(3,4))}}}$ ", f"${{{phan_so(y-random.randint(5,6))}}}$ "]


    kq2,kq3,kq4=random.sample(kq_F,3)

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


#[D10_C3_B2_38]-M1. Nhận dạng hàm số bậc hai
def npl_mk_L10_C3_B2_38():
    x=symbols("x")
    b=random.choice([i for i in range(-5,5) if i!=0]) 
    c=random.choice([i for i in range(-5,5) if i!=0 ])
    a2=random.choice([i for i in range(-5,5) if i!=0]) 
    a3=random.choice([i for i in range(-5,5) if i!=0]) 
    c1=random.choice([i for i in range(-5,5) if i!=0 ])
    c2=random.choice([i for i in range(-5,5) if i!=0 ])
    chon =random.randint(1,2)
    a=random.choice([i for i in range(-5,5) if i!=0]) 
    noi_dung=f" Trong các hàm số sau, hàm số nào là hàm số bậc hai?"

    noi_dung_loigiai=f" Hàm số bậc hai là $y={latex(a*x**2+b*x+c)}$."

    kq=f" $y={latex(a*x**2+b*x+c)}$"

    kq_F=[ f"$y={latex(expand(1/(a*(x-c)*(x-c1))))}$ ", f"$y={latex(sqrt(a*x-c1))} $", f"$y={latex(1/sqrt(a2*x-c2))} $", f" $y={latex((a2*x-a)/(b*x-c) )}$", f"$y={latex(c*x+sqrt(a3*x+c2))} $", f"$y={latex(a3*x**3+b*x**2+c)}$" ]
    kq4, kq2, kq3=random.sample(kq_F,3)


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



#[D10_C3_B2_39]-M1. Tìm số giao điểm của (P) và trục hoành
def npl_mk_L10_C3_B2_39():
    x=symbols("x")
    b=random.choice([i for i in range(-5,5) if i!=0]) 
    c=random.choice([i for i in range(-5,5) if i!=0 ])
    a2=random.choice([i for i in range(-5,5) if i!=0])  
    a1=random.choice([i for i in range(-5,5) if i!=0 and i!=a2 ])
    c2=random.choice([i for i in range(-5,5) if i!=0 ])
    chon =random.randint(1,2)
    a=random.choice([i for i in range(-5,5) if i!=0]) 
    a4=random.choice([i for i in range(-5,5) if i!=0])
    b4=random.choice([i for i in range(-5,5) if i!=0 and i*a4>0])
    chon =random.randint(1,3)
    if chon ==1:
        noi_dung=f" Số giao điểm của ${{(P)}}$:  $y={latex(expand(a*(x-a1)*(x-a2)))}$ với trục hoành là?"

        noi_dung_loigiai=f"Vì phương trình hoành độ giao điểm ${latex(expand(a*(x-a1)*(x-a2)))} =0$ có hai nghiệm phân biệt nên số giao điểm của Parabol với trục hoành bằng ${{2}}$."

        kq=f" ${{2}}$"

        kq_F=[ f"${{0}}$ ", f"${{1}}$", f"${{3}}$", f" ${{4}}$", f"${{5}}$", f"${{6}}$" ]


    if chon ==2:
        noi_dung=f" Số giao điểm của ${{(P)}}$:  $y={latex(expand(a4*(x-a1)*(x-a1)+b4))}$ với trục hoành là?"

        noi_dung_loigiai=f"Vì phương trình hoành độ giao điểm ${latex(expand(a*(x-a1)*(x-a2)))} =0$ vô nghiệm phân biệt nên số giao điểm của Parabol với trục hoành bằng ${{0}}$."

        kq=f" ${{0}}$"

        kq_F=[ f"${{2}}$ ", f"${{1}}$", f"${{3}}$", f" ${{4}}$", f"${{5}}$", f"${{6}}$" ]



    if chon ==3:
        noi_dung=f" Số giao điểm của ${{(P)}}$:  $y={latex(expand(a*(x-a1)*(x-a1)))}$ với trục hoành là?"

        noi_dung_loigiai=f"Vì phương trình hoành độ giao điểm ${latex(expand(a*(x-a1)*(x-a1)))} =0$ có nghiệm kép nên số giao điểm của Parabol với trục hoành bằng ${{1}}$."

        kq=f" ${{1}}$"

        kq_F=[ f"${{0}}$ ", f"${{2}}$", f"${{3}}$", f" ${{4}}$", f"${{5}}$", f"${{6}}$" ]


    kq4, kq2, kq3=random.sample(kq_F,3)

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



#[D10_C3_B2_40]-M1. Tìm toạ độ giao điểm Parabol với trục tung
def npl_mk_L10_C3_B2_40():
    x=symbols("x")
    b=random.choice([i for i in range(-5,5) if i!=0]) 
    c=random.choice([i for i in range(-5,5) if i!=0 ])
    a2=random.choice([i for i in range(-5,5) if i!=0])  
    a1=random.choice([i for i in range(-5,5) if i!=0 ])
    c2=random.choice([i for i in range(-5,5) if i!=0 ])
    chon =random.randint(1,2)
    a=random.choice([i for i in range(-5,5) if i!=0]) 
    a4=random.choice([i for i in range(-5,5) if i!=0])
    b4=random.choice([i for i in range(-5,5) if i!=0 and i*a4>0])

    noi_dung=f" Giao điểm của ${{(P)}}$  $y={latex(expand(a*x**2+b*x+c))}$ với trục tung có toạ độ là:"

    noi_dung_loigiai=f"Giao điểm của ${{(P)}}$  $y={latex(expand(a*x**2+b*x+c))}$ với trục tung có toạ độ là $\\left({{0}}; {c} \\right)$"

    kq=f" $\\left({{0}}; {c} \\right)$"

    kq_F=[ f"$\\left({{0}}; {c+random.randint(1,2)} \\right)$ ", f"$\\left({{0}}; {c-random.randint(1,2)} \\right)$", f"$\\left({c} ;{{0}} \\right)$", f" $\\left({c+random.randint(1,2)}; {{0}} \\right)$", f"$\\left({c+random.randint(1,2)}; {{{b}}} \\right)$" ]

    kq4, kq2, kq3=random.sample(kq_F,3)

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



#[D10_C3_B2_41]-M2. Tìm toạ độ giao điểm Parabol với đường thẳng y=ax+b
def npl_mk_L10_C3_B2_41():
    x=symbols("x")
    x0=random.choice([i for i in range(-5,5) if i!=0])  
    x1=random.choice([i for i in range(-5,5) if i!=0 and i!=x0 ])
    a=random.choice([i for i in range(-5,5) if i!=0]) 
    m=random.choice([i for i in range(-5,5) if i!=0])
    n=random.choice([i for i in range(-5,5) if i!=0])
    y0= m*x0+n
    y1= m*x1+n
    noi_dung=f" Giao điểm của ${{(P)}}$  $y={latex(expand(a*(x-x0)*(x-x1)+m*x+n))}$ với đường thẳng $y={latex(m*x+n)}$ có toạ độ là:"

    noi_dung_loigiai=(f"Xét phương trình hoành độ giao điểm \n\n ${latex(expand(a*(x-x0)*(x-x1)+m*x+n))} = {latex(m*x+n)}$ \n\n ${latex(a*(x-x0)*(x-x1))}=0$ suy ra ${{x={x0}; x={x1}}}$ \n\n "
    f" Với ${{x={x0}}}$ thì ${{y={y0}}}$ \n\n"
f" Với ${{x={x1}}}$ thì ${{y={y1}}}$ ")
    kq=f" $\\left({x0}; {phan_so(y0)} \\right)$ và $\\left({x1}; {phan_so(y1)} \\right)$ "

    kq_F=[ f"$\\left({x0}; {phan_so(y0+1)} \\right)$ và $\\left({x1}; {phan_so(y1)} \\right)$ ", f"$\\left({x0}; {phan_so(y0)} \\right)$ và $\\left({x1}; {phan_so(y1+1)} \\right)$", f"$\\left({x0}; {phan_so(y0+1)} \\right)$ và $\\left({x1}; {phan_so(y1+1)} \\right)$", f" $\\left({x0}; {phan_so(y0-1)} \\right)$ và $\\left({x1}; {phan_so(y1-1)} \\right)$", f"$\\left({x0}; {phan_so(y0-2)} \\right)$ và $\\left({x1}; {phan_so(y1-2)} \\right)$" ]

    kq4, kq2, kq3=random.sample(kq_F,3)

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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan, dap_an