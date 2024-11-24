import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module

#Code trả về latex phân số
def hien_phan_so(t):
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
        kq3 = f"D=\\left({latex(my_module.hien_phan_so(-b/a))};+\\infty\\right]"
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
    kq2= f"\\mathbb{{R}} \\backslash \\{{{latex(my_module.hien_phan_so(-d))}\\right\\}}"
    
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
        d==d+random(1,3)

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
    noi_dung = f"Tìm tọa độ đỉnh $I$ của đồ thị hàm số $y={latex(f)}$."

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
    a = random.randint(-5,5)
    if a==0:
        a = random.randint(1,3)              
    b = random.randint(-6,6)
    if b==0:
        b = random.randint(-6,-1)   
    c = random.randint(-5,5)

    if c==0:
        c = random.randint(1,5) 

    f=a*x**2 + b*x + c
    

    x_0 = random.randint(-3,4)
    if x_0==0:
        x_0 = random.randint(-3,-1) 
    y_0 = f.subs(x, x_0)        
   
    he_so_an = random.choice(["b","c"])
    if he_so_an =="b":
        dau ="+"
        if c<0:
            dau=""
        ham_so =f"y={latex(a*x**2)}+bx{dau}{c}"
        kq=f"${he_so_an}={b}$"
        pa_A= f"*${he_so_an}={b}$"
        pa_B= f"${he_so_an}={latex(-b)}$"
        pa_C= f"${he_so_an}={latex(a+b)}$"
        pa_D= f"${he_so_an}={latex(b**2)}$"
    else:
        dau ="+"
        if b<0:
            dau=""
        ham_so =f"y={latex(a*x**2)}{dau}{latex(b*x)}+c"
        kq=f"${he_so_an}={c}$"
        pa_A= f"*${he_so_an}={c}$"
        pa_B= f"${he_so_an}={latex(-c)}$"
        pa_C= f"${he_so_an}={latex(c+b)}$"
        pa_D= f"${he_so_an}={latex(c**2)}$"

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
        

        x_0 = random.randint(-4,4)        
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
    a= random.choice([random.randint(1, 10)])
    b, c = random.randint(-10, 10), random.randint(-10, 10)
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