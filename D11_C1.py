import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module

# Hàm kiểm tra số hữu tỉ
def is_rational(number):
    # Chuyển đổi số thành biểu thức SymPy
    expr = nsimplify(number)
    # Kiểm tra xem biểu thức có phải là số hữu tỉ hay không
    return expr.is_rational

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

def thay_frac_1pi(st):
    return st.replace(f"\\frac{{1\\pi}}", f"\\frac{{\\pi}}").replace(f"\\frac{{-1\\pi}}", f"\\frac{{-\\pi}}")

def degree_to_radian(degree):
    return latex(sp.rad(degree))

def thay_sin_cos(st):
    st_new=st.replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x").replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
    st_new=st_new.replace(f"\\sin{{\\left(x \\right)}}",f"\\sin x").replace(f"\\sin^{{2}}{{\\left(x \\right)}}",f"\\sin^2 x")
    st_new=st_new.replace(f"\\cos{{\\left(x \\right)}}",f"\\cos x").replace(f"\\cos^{{2}}{{\\left(x \\right)}}",f"\\cos^2 x")
    return st_new

################ Bài 1: Góc lượng giác #################
#[D11_C1_B1_02]-M1. Đổi số đo từ độ sang radian
def ngh_kjg_L11_C1_B1_02():
    t=random.randint(-5,5)
    goc_bandau=[0,10,15,20,30,45,60,75,90,120,150,180]
    goc_degree=random.choice([i+t*180 for i in goc_bandau])
    goc_radian = degree_to_radian(goc_degree)
    goc_radian_2=degree_to_radian(goc_degree+10)
    goc_radian_3=degree_to_radian(goc_degree+30)
    goc_radian_4=degree_to_radian(goc_degree-20)


    #Tạo các phương án
    pa_A= f"*${goc_radian}$"
    pa_B= f"${goc_radian_2}$"
    pa_C= f"${goc_radian_3}$"
    pa_D= f"${goc_radian_4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đổi số đo của góc ${goc_degree}^\\circ$ sang radian ta được kết quả bằng"
    noi_dung_loigiai=f"Áp dụng công thức chuyển đổi: ${goc_degree}^\\circ=\\dfrac{{{goc_degree}.\\pi}}{{180}}={goc_radian}$."
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
    

#[D11_C1_B1_03]-M1. Đổi số đo từ radian sang độ
def ngh_kjg_L11_C1_B1_03():
    t=random.randint(-5,5)
    goc_bandau=[0,10,15,20,30,45,60,75,90,120,150,180]
    goc_degree=random.choice([i+t*180 for i in goc_bandau])
    goc_radian = degree_to_radian(goc_degree)
    goc_degree_2=goc_degree+10
    goc_degree_3=goc_degree+30
    goc_degree_4=goc_degree-random.randint(20,50)


    #Tạo các phương án
    pa_A= f"*${goc_degree}^\\circ$"
    pa_B= f"${goc_degree_2}^\\circ$"
    pa_C= f"${goc_degree_3}^\\circ$"
    pa_D= f"${goc_degree_4}^\\circ$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Đổi số đo của góc ${goc_radian}$ sang độ ta được kết quả bằng"
    noi_dung_loigiai=f"Áp dụng công thức chuyển đổi: ${goc_radian}=\\left(\\dfrac{{{goc_radian}.180}}{{\\pi}}\\right)^\\circ={goc_degree}^\\circ$."
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

#[D11_C1_B1_04]-M2. Tìm góc có điểm biểu diễn trùng nhau
def ngh_kjg_L11_C1_B1_04():
    t=random.choice([random.randint(-2, -1), random.randint(1, 2)])
    goc_degree=random.choice([5*i for i in range(1,35)])

    goc_radian = degree_to_radian(goc_degree)
    goc_trung=degree_to_radian(goc_degree+t*360)

    goc_2=degree_to_radian(goc_degree+10)
    goc_3=degree_to_radian(goc_degree+random.randint(20, 40))
    goc_4=degree_to_radian(goc_degree-random.randint(20, 40))


    #Tạo các phương án
    pa_A= f"*${goc_radian}$"
    pa_B= f"${goc_2}$"
    pa_C= f"${goc_3}$"
    pa_D= f"${goc_4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Góc lượng giác ${goc_trung}$ có cùng điểm biểu diễn trên đường tròn lượng giác với góc lượng giác nào sau đây?"
    noi_dung_loigiai=f"Ta có: ${goc_trung}={goc_radian} +{t}.2\\pi$ nên ${goc_trung}$ có cùng điểm biểu diễn trên đường tròn lượng giác với góc ${goc_radian}$.".replace("+-","-")
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

#[D11_C1_B1_05]-M2. Tìm góc lượng giác có điểm biểu diễn cho trước
def ngh_kjg_L11_C1_B1_05():
    t= random.choice([random.randint(-2, -1), random.randint(1, 2)])
    goc_bandau=random.choice([0,30,45,60,90,120,150,180])
    goc_degree=goc_bandau+t*360
    goc_radian = degree_to_radian(goc_degree)
    goc_2=degree_to_radian(goc_bandau+random.choice([30,45,60,90]))
    goc_3=degree_to_radian(goc_bandau+180)
    goc_4=degree_to_radian(goc_bandau+270)

    code_hinh=f"\\begin{{tikzpicture}}[scale=3, line width=1pt] \n\
 \\trucLG \n\
\\pointLG{{{goc_bandau}}}{{1}}{{*}}{{red}} \n\
\\end{{tikzpicture}}"
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    #Tạo các phương án
    pa_A= f"*${goc_radian}$"
    pa_B= f"${goc_2}$"
    pa_C= f"${goc_3}$"
    pa_D= f"${goc_4}$"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Điểm biểu diễn trên đường tròn lượng giác như hình vẽ bên là của  góc lượng giác nào sau đây?"
    noi_dung_loigiai=f"Ta có: ${goc_radian}={degree_to_radian(goc_bandau)} +{t}.2\\pi$ nên ${goc_radian}$ là góc có điểm biểu diễn trùng với góc ${degree_to_radian(goc_bandau)}$ trên đường tròn lượng giác như hình vẽ bên.".replace("+-","-")
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)
    

    debai=(f"{noi_dung}\n"
    f"{file_name}\n")      
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"     
   
    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
    f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
    f"\\begin{{center}}{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C1_B1_06]-M2. Cho bán kính và góc radian. Tính độ dài của cung.
def ngh_kjg_L11_C1_B1_06():
    r=random.randint(1,20)
    chon=random.randint(1,2)
    if chon==1:    
        t= random.randint(1, 2)
        goc_bandau=random.choice([30,45,60,90,120,150,180])
        goc_degree=goc_bandau+t*90
        goc_radian = sp.rad(goc_degree)

        kq=r*goc_radian
        kq2=r*goc_radian*random.randint(2,4)
        kq3=r*goc_radian/2
        kq4=r*goc_radian/4

        #Tạo các phương án
        pa_A= f"*${latex(kq)}$"
        pa_B= f"${latex(kq2)}$"
        pa_C= f"${latex(kq3)}$"
        pa_D= f"${latex(kq4)}$"
        noi_dung= f"Một đường tròn có bán kính bằng ${{{r}}}$ cm. Cung trên đường tròn đó có số đo là ${{{latex(goc_radian)}}}$ thì có độ dài bằng"  

        noi_dung_loigiai=f"Độ dài của cung tròn là: $l={r}.{goc_radian}={latex(kq)}$."

    if chon==2:
        a= random.randint(1,10)
        b= random.randint(1,20)
        t=a/b        
        goc_radian=random.choice([random.randint(1,15),t])

        kq=r*goc_radian
        kq2=r+goc_radian
        kq3=r/(2*goc_radian)
        kq4=goc_radian/r

        pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
        kq2=pa_kotrung[1]
        kq3=pa_kotrung[2]
        kq4=pa_kotrung[3]

        #Tạo các phương án
        pa_A= f"*${phan_so(kq)}$"
        pa_B= f"${phan_so(kq2)}$"
        pa_C= f"${phan_so(kq3)}$"
        pa_D= f"${phan_so(kq4)}$"

        noi_dung= f"Một đường tròn có bán kính bằng ${{{r}}}$ cm. Cung trên đường tròn đó có số đo là ${{{phan_so(goc_radian)}}}$ thì có độ dài bằng"  

        noi_dung_loigiai=f"Độ dài của cung tròn là: $l={r}.{phan_so(goc_radian)}={phan_so(kq)}$."
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

     
    debai= f"{noi_dung}\n\n"    
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

#[D11_C1_B1_07]-M2. Cho bán kính và góc độ. Tính độ dài của cung.
def ngh_kjg_L11_C1_B1_07():
    r=random.randint(1,20)
    goc_degree=random.randint(1,540)
    goc_radian = rad(goc_degree)

    kq=r*goc_radian
    kq2=(r+random.randint(1,3))*goc_radian
    kq3=r*goc_radian/2
    kq4=r*goc_radian/3

    #Tạo các phương án
    pa_A= f"*${latex(kq)}$"
    pa_B= f"${latex(kq2)}$"
    pa_C= f"${latex(kq3)}$"
    pa_D= f"${latex(kq4)}$"
    noi_dung= f"Một đường tròn có bán kính bằng ${{{r}}}$ cm. Cung trên đường tròn đó có số đo là ${{{goc_degree}}}^\\circ$ thì có độ dài bằng"  

    noi_dung_loigiai=f"Độ dài của cung tròn là: $l=\\dfrac{{{r}.{goc_degree}}}{{180}}\\pi={latex(kq)}$."


     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

     
    debai= f"{noi_dung}\n\n"    
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

#[D11_C1_B1_08]-TF-M2. Cho góc radian. Xét đúng-sai: Đổi sang độ, Điểm biểu diễn thuộc phần tư, Góc cùng điểm biểu diễn, Đếm số điểm biểu diễn
def ngh_kjg_L11_C1_B1_08():

    goc_duong=[5,10,15,20,30,45,60,75,120,135,150]
    goc_am=[-i for i in goc_duong]
    goc=random.choice(goc_duong + goc_am)
    t=random.choice([-2,-1,1,2,3])
    goc_degree=goc + t*360
    goc_radian = degree_to_radian(goc_degree) 

    noi_dung=f"Cho góc lượng giác ${goc_radian }$. Xét tính đúng-sai của các khẳng định sau"    

    kq1_T=f"*${goc_radian}={goc_degree}^\\circ$" 
    kq1_F=f"${goc_radian}={goc_degree+random.randint(1,20)}^\\circ$ "
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Ta có: ${goc_radian}=\\left(\\dfrac{{{goc_radian}.180}}{{\\pi}}\\right)^\\circ={goc_degree}^\\circ$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*Góc lượng giác đã cho có cùng điểm biểu diễn trên đường tròn lượng giác với góc ${degree_to_radian(goc)}$"
    kq2_F=f"Góc lượng giác đã cho có cùng điểm biểu diễn trên đường tròn lượng giác với góc ${degree_to_radian(-goc)}$ "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Vì: ${goc_radian}={degree_to_radian(goc)} +{t}.2\\pi$".replace("+1.2\\pi","+2\\pi").replace("+-","-")

    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if 0<goc<90:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ I" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["II","III","IV"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_radian}={degree_to_radian(goc)} +{t}.2\\pi$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ I.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if 90<goc<180:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ II" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["I","III","IV"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_radian}={degree_to_radian(goc)} +{t}.2\\pi$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ II.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if -180<goc<-90:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ III" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["II","IV","I"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_radian}={degree_to_radian(goc)} +{t}.2\\pi$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ III.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if -90<goc<0:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ IV" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["II","III","I"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_radian}={degree_to_radian(goc)} +{t}.2\\pi$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ IV.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=random.randint(1,8)
    kq4_T=f"*Số điểm biểu diễn trên đường tròn lượng giác của góc ${goc_radian}+k{latex(2*pi/n)},k \\in \\mathbb{{Z}}$ là ${{{n}}}$".replace(f"k1\\pi", f"k\\pi")
    kq4_F=f"Số điểm biểu diễn trên đường tròn lượng giác của góc ${goc_radian}+k{latex(2*pi/n)},k \\in \\mathbb{{Z}}$ là ${{{n+random.randint(1,3)}}}$".replace(f"k1\\pi", f"k\\pi")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"${goc_radian}+k{latex(2*pi/n)}={goc_radian}+\\dfrac{{k2\\pi}}{{{n}}}$ nên có ${{{n}}}$ điểm biểu diễn trên đường tròn lượng giác."
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

#[D11_C1_B1_09]-TF-M2. Cho góc độ. Xét đúng-sai: Đổi sang radian, Điểm biểu diễn thuộc phần tư, Góc cùng điểm biểu diễn, Đếm số điểm biểu diễn
def ngh_kjg_L11_C1_B1_09():

    goc_duong=[5,10,15,20,30,45,60,75,120,135,150]
    goc_am=[-i for i in goc_duong]
    goc=random.choice(goc_duong + goc_am)
    t=random.choice([-2,-1,1,2,3])
    goc_degree=goc + t*360
    goc_radian = degree_to_radian(goc_degree) 

    noi_dung=f"Cho góc lượng giác ${goc_degree}^\\circ$. Xét tính đúng-sai của các khẳng định sau"    

    kq1_T=f"*${goc_degree}^\\circ={goc_radian}$" 
    kq1_F=f"${goc_degree}^\\circ={degree_to_radian(goc_degree+random.randint(1,20))}$ "
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Ta có: ${goc_degree}^\\circ=\\dfrac{{{goc_degree}.\\pi}}{{180}}={goc_radian}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*Góc lượng giác đã cho có cùng điểm biểu diễn trên đường tròn lượng giác với góc ${goc}^\\circ$"
    kq2_F=f"Góc lượng giác đã cho có cùng điểm biểu diễn trên đường tròn lượng giác với góc ${-goc}^\\circ$ "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Vì: ${goc_degree}^\\circ={goc}^\\circ +{t}.360^\\circ$".replace("+1.360^","360^").replace("+-","-")

    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if 0<goc<90:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ I" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["II","III","IV"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_degree}^\\circ={goc}^\\circ +{t}.360^\\circ$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ I.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if 90<goc<180:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ II" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["I","III","IV"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_degree}^\\circ={goc}^\\circ +{t}.360^\\circ$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ II.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if -180<goc<-90:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ III" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["II","IV","I"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_degree}^\\circ={goc}^\\circ +{t}.360^\\circ$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ III.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if -90<goc<0:
        kq3_T=f"*Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ IV" 
        kq3_F=f"Điểm biểu diễn trên đường tròn lượng giác của góc đã cho thuộc phần tư thứ {random.choice(["II","III","I"])}"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì: ${goc_degree}^\\circ={goc}^\\circ +{t}.360^\\circ$ nên điểm biểu diễn của góc đã cho thuộc phần tư thứ IV.".replace("+-","-")
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n=random.randint(1,10)
    kq4_T=f"*Số điểm biểu diễn trên đường tròn lượng giác của góc ${goc_degree}^\\circ +k{phan_so(360/n)}^\\circ,k \\in \\mathbb{{Z}}$ là ${{{n}}}$"
    kq4_F=f"Số điểm biểu diễn trên đường tròn lượng giác của góc ${goc_degree}^\\circ +k{phan_so(360/n)}^\\circ,k \\in \\mathbb{{Z}}$ là ${{{n+random.randint(1,3)}}}$"
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"${goc_degree}^\\circ +k{phan_so(360/n)}^\\circ={goc_degree}^\\circ +\\dfrac{{k360^\\circ}}{{{n}}}$ nên có ${{{n}}}$ điểm biểu diễn trên đường tròn lượng giác."
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

#[D11_C1_B1_10]-TL-M3. Cho số vòng quay bánh xe sau t1 giây. Tính góc radian sau khi quay trong t2 giây
def ngh_kjg_L11_C1_B1_10():
    #Tạo số vòng quay ban đầu
    n= random.randint(4,12)

    #Tạo thời gian
    t1=random.randint(3,6)

    #Tạo số giây cần đo góc
    t2= random.randint(3,10)
    if t2==t1: t2=t1-1

    noi_dung = f"Một bánh xe của một loại xe quay được {n} vòng trong {t1} giây."\
    f" Tính góc theo rađian mà bánh xe quay được trong {t2} giây (kết quả làm tròn đến hàng phần chục)."
    kq=str(round((2*n*t2*pi)/t1,1)).replace(".",",")

    noi_dung_loigiai=f"Một giây bánh xe quay được số vòng là: ${phan_so(n/t1)}$.\n\n"\
    f"Một vòng quay ứng với góc $2\\pi$. Sau ${{{t2}}}$ giây có ${phan_so(n/t1)}.{t2}={phan_so(n/t1*t2)}$ vòng quay ứng với góc:\n\n"\
    f"${phan_so(n/t1*t2)}.2\\pi={phan_so(2*n/t1*t2)}\\pi={kq}$."
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B1_11]-TL-M3. Cho số vòng quay bánh xe sau t1 giây. Tính quãng đường đi được sau t2 giây
def ngh_kjg_L11_C1_B1_11():
    #Tạo bán kính
    r= random.randint(40,60)
    #Tạo số vòng quay ban đầu
    n= random.randint(4,12)

    #Tạo thời gian
    t1=random.randint(3,6)

    #Tạo số giây cần đo góc
    t2= random.randint(3,10)
    if t2==t1: t2=t1-1

    noi_dung = f"Một bánh xe của một loại xe có bán kính ${{{r}}}$ cm và quay được {n} vòng trong {t1} giây."\
    f" Tính độ dài quãng đường (theo đơn vị mét) xe đi được trong {t2} giây (kết quả làm tròn đến hàng phần mười)."
    r_m=r/100
    
    kq=str(round((n*t2*2*r_m*pi)/t1,1)).replace(".",",")

    noi_dung_loigiai=f"Một giây bánh xe quay được số vòng là: ${phan_so(n/t1)}$.\n\n"\
    f"Một vòng quay ứng với quãng đường là $2\\pi.\\dfrac{{{r}}}{{100}}=2\\pi.{phan_so(r_m)}={phan_so(2*r_m)}\\pi$.\n\n"\
    f"Sau ${{{t2}}}$ giây quãng đường đi được là: ${phan_so(n/t1)}.{t2}.{phan_so(2*r_m)}\\pi={phan_so(n*t2*2*r_m/t1)}\\pi={kq}$.\n\n"\

        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung} \n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"

    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B1_12]-TL-M3. Cho đường kính của bánh trước và bánh sau, vận tốc n vòng/phút. Tính quãng đường xe đi.
def ngh_kjg_L11_C1_B1_12():   

    #Tạo bán kính bánh trước
    r_t= random.randint(35,50)

    #Tạo bán kính bánh sau
    r_s= random.randint(75,95)    

    #Tạo thời gian
    t=random.randint(5,15)
    chon=random.randint(1,2)

    if chon==1:
        #Tạo vận tốc bánh sau
        n= random.randint(4,12)
        noi_dung = f"Một máy kéo nông nghiệp với bánh xe trước có đường kính là ${{{2*r_t}}}$ cm, bánh xe sau có đường kính là ${{{2*r_s}}}$ cm, "\
        f" xe chuyển động với vận tốc không đổi trên một đoạn đường thẳng."\
        f" Biết rằng vận tốc của bánh xe sau trong chuyển động này là ${{{n}}}$ vòng/ phút."\
        f" Tính quãng đường mà máy kéo đi được (bằng km) trong ${{{t}}}$ phút (làm tròn đến hàng phần mười)."\
        
        s_km=str((n*t*2*r_s)/(10**5)).replace(".",",")

        kq=str(round((n*t*2*r_s)/(10**5)*pi,1)).replace(".",",")

        noi_dung_loigiai=f"Chu vi của bánh sau là: $2\\pi.{r_s}={2*r_s}\\pi$.\n\n"\
        f"Tức là bánh xe sau đi mỗi vòng được quãng đường có độ dài là ${2*r_s}\\pi$.\n\n"\
        f"Vận tốc của bánh xe sau là ${{{n}}}$ vòng/ phút nên trong ${{{t}}}$ phút bánh xe sau chuyển động được:\\[{n}.{t}={n*t}\\text{{(vòng)}}.\\]\n\n"\
        f"Quãng đường đi được của máy kéo trong ${{{t}}}$ phút là quãng đường đi được khi bánh xe sau lăn ${{{n*t}}}$ vòng:\n\n"\
        f"${n*t}.{2*r_s}\\pi={n*t*2*r_s}\\pi$ (cm) $={s_km}\\pi$ (km) $={kq}$ (km)."

    if chon==2:
        #Tạo vận tốc bánh trước
        n= random.randint(8,20)
        noi_dung = f"Một máy kéo nông nghiệp với bánh xe trước có đường kính là ${{{2*r_t}}}$ cm, bánh xe sau có đường kính là ${{{2*r_s}}}$ cm, "\
        f" xe chuyển động với vận tốc không đổi trên một đoạn đường thẳng."\
        f" Biết rằng vận tốc của bánh xe trước trong chuyển động này là ${{{n}}}$ vòng/ phút."\
        f" Tính quãng đường mà máy kéo đi được (bằng km) trong ${{{t}}}$ phút (làm tròn đến hàng phần mười)."\
        
        s_km=str((n*t*2*r_t)/(10**5)).replace(".",",")

        kq=str(round((n*t*2*r_t)/(10**5)*pi,1)).replace(".",",")

        noi_dung_loigiai=f"Chu vi của bánh trước là: $2\\pi.{r_t}={2*r_t}\\pi$.\n\n"\
        f"Tức là bánh xe trước đi mỗi vòng được quãng đường có độ dài là ${2*r_t}\\pi$.\n\n"\
        f"Vận tốc của bánh xe trước là ${{{n}}}$ vòng/ phút nên trong ${{{t}}}$ phút bánh xe trước chuyển động được:\\[{n}.{t}={n*t}\\text{{(vòng)}}.\\]\n\n"\
        f"Quãng đường đi được của máy kéo trong ${{{t}}}$ phút là quãng đường đi được khi bánh xe trước lăn ${{{n*t}}}$ vòng:\n\n"\
        f"${n*t}.{2*r_t}\\pi={n*t*2*r_t}\\pi$ (cm) $={s_km}\\pi$ (km) $={kq}$ (km)."
   
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B2_02]-TL-M2. Cho sinx (hoặc cosx), x thuộc (a;b). Tìm cosx (hoặc sinx)
def ngh_kjg_L11_C1_B2_02():
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])

    cung=random.choice([cung_I, cung_II, cung_III, cung_IV])  

    a = random.randint(1,15)
    b = a+ random.randint(1,5)
    chon=random.choice(["sin", "cos"])
    if chon=="sin":
        gia_tri_LG=f"\\cos\\alpha"

        if cung in [cung_I, cung_II]:
            sin_value=a/b
        else:
            sin_value=-a/b
        noi_dung=f"Cho góc lượng giác $\\alpha$ thỏa mãn $\\sin \\alpha={phan_so(sin_value)}, \\alpha \\in {cung}$. Tính ${gia_tri_LG}$ (kết quả làm tròn đến hàng phần mười)."

        if cung in [cung_I, cung_IV]:       
            cos_value=sqrt(b**2-a**2)/b            
            kq=str(round(cos_value,1)).replace(".",",")
            noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\cos\\alpha > 0$.\n\n"\
            f"$\\cos\\alpha =\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}={kq}$."            

        if cung in [cung_II, cung_III]:
            cos_value=-sqrt(b**2-a**2)/b           
            kq=str(round(cos_value,2)).replace(".",",")
            noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\cos\\alpha < 0$.\n\n"\
            f"$\\cos\\alpha =-\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}={kq}$."            

    if chon=="cos":
        gia_tri_LG=f"\\sin\\alpha"
        if cung in [cung_I, cung_IV]:
            cos_value=a/b
        else:
            cos_value=-a/b
        noi_dung=f"Cho góc lượng giác $\\alpha$ thỏa mãn $\\cos \\alpha={phan_so(cos_value)}, \\alpha \\in {cung}$. Tính ${gia_tri_LG}$ (kết quả làm tròn đến hàng phần mười)."

        if cung in [cung_I, cung_II]:       
            sin_value=sqrt(b**2-a**2)/b            
            kq=str(round(sin_value,1)).replace(".",",")
            noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\sin\\alpha > 0$.\n\n"\
            f"$\\sin\\alpha =\\sqrt{{1-{phan_so(cos_value**2)}}}={latex(sin_value)}={kq}$."            

        if cung in [cung_III, cung_IV]:
            sin_value=-sqrt(b**2-a**2)/b            
            kq=str(round(sin_value,2)).replace(".",",")
            noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\sin\\alpha < 0$.\n\n"\
            f"$\\sin\\alpha =\\sqrt{{1-{phan_so(cos_value**2)}}}={latex(sin_value)}={kq}$."

    noi_dung_loigiai+=f"Đáp án: {kq}"              
   
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B2_03]-TL-M3. Cho sinx (hoặc cosx), x thuộc (a;b). Tìm tanx (hoặc cotx)
def ngh_kjg_L11_C1_B2_03():
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])

    cung=random.choice([cung_I, cung_II, cung_III, cung_IV])    
    a = random.randint(1,15)
    b = a+random.randint(1,5)
    gia_tri_LG=random.choice([f"\\tan\\alpha", f"\\cot\\alpha"])
    chon=random.choice(["sin", "cos"])
    if chon=="sin":        
        if cung in [cung_I, cung_II]:
            sin_value=a/b
        else:
            sin_value=-a/b
        noi_dung=f"Cho góc lượng giác $\\alpha$ thỏa mãn $\\sin \\alpha={phan_so(sin_value)}, \\alpha \\in {cung}$. Tính ${gia_tri_LG}$ (kết quả làm tròn đến hàng phần mười)."

        if cung in [cung_I, cung_IV]:       
            cos_value=sqrt(b**2-a**2)/b            

            if gia_tri_LG==f"\\tan\\alpha":
                tan_value=sin_value/cos_value
                kq=str(round(tan_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\cos\\alpha > 0$.\n\n"\
                f"$\\cos\\alpha =\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$.\n\n"\
                f"$\\tan\\alpha={phan_so(sin_value)}:{latex(cos_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"

            if gia_tri_LG==f"\\cot\\alpha":
                cot_value=cos_value/sin_value
                kq=str(round(cot_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\cos\\alpha > 0$.\n\n"\
                f"$\\cos\\alpha =\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$.\n\n"\
                f"$\\cot\\alpha={latex(cos_value)}:{phan_so(sin_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"

        if cung in [cung_II, cung_III]:
            cos_value=-sqrt(b**2-a**2)/b           

            if gia_tri_LG==f"\\tan\\alpha":
                tan_value=sin_value/cos_value
                kq=str(round(tan_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\cos\\alpha < 0$.\n\n"\
                f"$\\cos\\alpha =-\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$.\n\n"\
                f"$\\tan\\alpha={phan_so(sin_value)}:{latex(cos_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"

            if gia_tri_LG==f"\\cot\\alpha":
                cot_value=cos_value/sin_value
                kq=str(round(cot_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\cos\\alpha < 0$.\n\n"\
                f"$\\cos\\alpha =-\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$.\n\n"\
                f"$\\cot\\alpha={latex(cos_value)}:{phan_so(sin_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"

    if chon=="cos":
        if cung in [cung_I, cung_IV]:
            cos_value=a/b
        else:
            cos_value=-a/b
        noi_dung=f"Cho góc lượng giác $\\alpha$ thỏa mãn $\\cos \\alpha={phan_so(cos_value)}, \\alpha \\in {cung}$. Tính ${gia_tri_LG}$ (kết quả làm tròn đến hàng phần mười)."

        if cung in [cung_I, cung_II]:       
            sin_value=sqrt(b**2-a**2)/b

            if gia_tri_LG==f"\\tan\\alpha":
                tan_value=sin_value/cos_value
                kq=str(round(tan_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\sin\\alpha > 0$.\n\n"\
                f"$\\sin\\alpha =\\sqrt{{1-{phan_so(cos_value**2)}}}={latex(sin_value)}={kq}$.\n\n"\
                f"$\\tan\\alpha={latex(sin_value)}:{phan_so(cos_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"

            if gia_tri_LG==f"\\cot\\alpha":
                cot_value=cos_value/sin_value
                kq=str(round(cot_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\sin\\alpha > 0$.\n\n"\
                f"$\\sin\\alpha =\\sqrt{{1-{phan_so(cos_value**2)}}}={latex(sin_value)}={kq}$.\n\n"\
                f"$\\cot\\alpha={latex(cos_value)}:{latex(sin_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"

        if cung in [cung_III, cung_IV]:
            sin_value=-sqrt(b**2-a**2)/b

            if gia_tri_LG==f"\\tan\\alpha":
                tan_value=sin_value/cos_value
                kq=str(round(tan_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\sin\\alpha < 0$.\n\n"\
                f"$\\sin\\alpha =\\sqrt{{1-{phan_so(cos_value**2)}}}={latex(sin_value)}={kq}$.\n\n"\
                f"$\\tan\\alpha={latex(sin_value)}:{latex(cos_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"

            if gia_tri_LG==f"\\cot\\alpha":
                cot_value=cos_value/sin_value
                kq=str(round(cot_value,1)).replace(".",",")

                noi_dung_loigiai=f"Vì $\\alpha \\in {cung}$ nên $\\sin\\alpha < 0$.\n\n"\
                f"$\\sin\\alpha =\\sqrt{{1-{phan_so(cos_value**2)}}}={latex(sin_value)}={kq}$.\n\n"\
                f"$\\cot\\alpha={latex(cos_value)}:{latex(sin_value)}={kq}$.\n\n"\
                f"Đáp án: {kq}"   
           
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B2_04]-TL-M3. Cho tanx (hoặc cotx). Tìm P=(asinx+bcosx)/(csinx+dcosx)
def ngh_kjg_L11_C1_B2_04():
    tan_value=random.choice([random.randint(-6, -1), random.randint(1, 6)])
    a,b,c,d=[random.choice([random.randint(-6, -1), random.randint(1, 6)]) for _ in range(4)]
    if a*d-b*c==0: a=a+1
    if a==0: a=1
    if c*tan_value+d==0:
        d=d+1
    sinx, cosx, tanx=sp.symbols("sinx cosx tanx")
    noi_dung=f"Cho góc lượng giác ${{x}}$ thỏa mãn $\\tan x={tan_value}$."\
    f" Tính giá trị biểu thức $P={latex((a*sinx+b*cosx)/(c*sinx+d*cosx))}$ (kết quả làm tròn đến hàng phần mười).".replace("sinx",f"\\sin x").replace("cosx",f"\\cos x").replace("tanx",f"\\tan x")
    kq=str(round((a*tan_value+b)/(c*tan_value+d),1)).replace(".",",")

    noi_dung_loigiai=(f"$P={latex((a*sinx+b*cosx)/(c*sinx+d*cosx))}={latex((a*tanx+b)/(c*tanx+d))}={phan_so((a*tan_value+b)/(c*tan_value+d))}={kq}$.\n\n"
    f"Đáp án: {kq}").replace("sinx",f"\\sin x").replace("cosx",f"\\cos x").replace("tanx",f"\\tan x")
    
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B2_05]-TL-M3. Cho tanx (hoặc cotx). Tìm P=(asin^2 x+bsinxcosx)/(csin^2 x+dcos^2 x)
def ngh_kjg_L11_C1_B2_05():
    tan_value=random.choice([random.randint(-6, -1), random.randint(1, 6)])
    a,b,c,d=[random.choice([random.randint(-6, -1), random.randint(1, 6)]) for _ in range(4)]
    if a*d-b*c==0: a=a+1
    if a==0: a=1
    if c*tan_value**2+d==0:
        d=d+1
    x=sp.symbols("x")
    noi_dung=f"Cho góc lượng giác ${{x}}$ thỏa mãn $\\tan x={tan_value}$."\
    f" Tính giá trị biểu thức $P=\\dfrac{{{a}\\sin^2 x +{b}\\sin x \\cos x}}{{{c}\\sin^2x+{d}\\cos^2x}}$ (kết quả làm tròn đến hàng phần mười).".replace("+-","-")
    kq=str(round((a*tan_value**2+b*tan_value)/(c*tan_value**2+d),1)).replace(".",",")

    noi_dung_loigiai=(f"$P=\\dfrac{{{a}\\sin^2 x +{b}\\sin x \\cos x}}{{{c}\\sin^2x+{d}\\cos^2x}}=\\dfrac{{{a}\\tan^2x+{b}\\tan x}}{{{c}\\tan^2x +{d}}}={phan_so((a*tan_value**2+b*tan_value)/(c*tan_value**2+d))}={kq}$.\n\n"
    f"Đáp án: {kq}").replace("+-","-")
    
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
    f"\\shortans[4]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B2_06]-TF-M2. Cho góc lượng giác thuộc cung phần tư. Xét Đ-S dấu của sin, cos, tan, cot
def ngh_kjg_L11_C1_B2_06():
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])

    cung=random.choice([cung_I, cung_II, cung_III, cung_IV])   

    noi_dung = f"Cho góc lượng giác $\\alpha \\in {cung}$. Xét tính đúng-sai của các khẳng định sau."        
    debai_word= f"{noi_dung}\n"
    if cung == cung_I:
        kq1_T=f"*$\\sin \\alpha > 0$" 
        kq1_F=f"$\\sin \\alpha < 0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha > 0$."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq2_T=f"*$\\cos \\alpha > 0$"
        kq2_F=f"$\\cos \\alpha < 0$ "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\cos \\alpha > 0$."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*$\\tan \\alpha > 0$" 
        kq3_F=f"$\\tan \\alpha < 0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha > 0, \\cos \\alpha > 0 \\Rightarrow \\tan \\alpha >0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*$\\cot \\alpha > 0$"
        kq4_F=f"$\\cot \\alpha < 0$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha > 0, \\cos \\alpha > 0 \\Rightarrow \\cot \\alpha >0$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung == cung_II:
        kq1_T=f"*$\\sin \\alpha > 0$" 
        kq1_F=f"$\\sin \\alpha < 0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha > 0$."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq2_T=f"*$\\cos \\alpha < 0$"
        kq2_F=f"$\\cos \\alpha > 0$ "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\cos \\alpha < 0$."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*$\\tan \\alpha < 0$" 
        kq3_F=f"$\\tan \\alpha > 0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha > 0, \\cos \\alpha < 0 \\Rightarrow \\tan \\alpha <0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*$\\cot \\alpha < 0$"
        kq4_F=f"$\\cot \\alpha > 0$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha > 0, \\cos \\alpha < 0 \\Rightarrow \\cot \\alpha <0$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung == cung_III:
        kq1_T=f"*$\\sin \\alpha < 0$" 
        kq1_F=f"$\\sin \\alpha > 0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha < 0$."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq2_T=f"*$\\cos \\alpha < 0$"
        kq2_F=f"$\\cos \\alpha > 0$ "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\cos \\alpha < 0$."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*$\\tan \\alpha > 0$" 
        kq3_F=f"$\\tan \\alpha < 0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha < 0, \\cos \\alpha < 0 \\Rightarrow \\tan \\alpha >0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*$\\cot \\alpha > 0$"
        kq4_F=f"$\\cot \\alpha < 0$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha < 0, \\cos \\alpha < 0 \\Rightarrow \\cot \\alpha >0$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung == cung_IV:
        kq1_T=f"*$\\sin \\alpha < 0$" 
        kq1_F=f"$\\sin \\alpha > 0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha < 0$."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq2_T=f"*$\\cos \\alpha > 0$"
        kq2_F=f"$\\cos \\alpha < 0$ "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\cos \\alpha < 0$."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq3_T=f"*$\\tan \\alpha < 0$" 
        kq3_F=f"$\\tan \\alpha > 0$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha < 0, \\cos \\alpha > 0 \\Rightarrow \\tan \\alpha <0$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"*$\\cot \\alpha < 0$"
        kq4_F=f"$\\cot \\alpha > 0$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\sin \\alpha < 0, \\cos \\alpha > 0 \\Rightarrow \\cot \\alpha <0$."
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

#[D11_C1_B2_07]-TF-M2. Cho tanx. Xét Đ-S: cotx, sin^2 x, cos^2x, (asinx+bcosx)/(csinx+dcosx)
def ngh_kjg_L11_C1_B2_07():    
    tan_value=random.choice([random.randint(-6, -2), random.randint(1, 6)])
    a,b,c,d=[random.choice([random.randint(-6, -1), random.randint(1, 6)]) for _ in range(4)]
    if a*d-b*c==0: a=a+1
    if a==0: a=1
    if c*tan_value+d==0: d=d+1
    sinx, cosx, tanx=sp.symbols("sinx cosx tanx")  

    noi_dung = f"Cho góc lượng giác ${{x}}$ thỏa mãn $\\tan x={tan_value}$. Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"*$\\cot x= {phan_so(1/tan_value)}$" 
    kq1_F=f"$\\cot x= {phan_so(1/tan_value+random.randint(1,3))}$ "
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\cot x=\\dfrac{{1}}{{\\tan x}}=1:{phan_so(tan_value)}={phan_so(1/tan_value)}$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*$\\cos^2x={phan_so(1/(1+tan_value**2))}$"
    kq2_F=f"$\\cos^2x={phan_so(1/(1+tan_value))}$ "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$1+\\tan^2x=\\dfrac{{1}}{{\\cos^2x}} \\Rightarrow \\cos^2x=\\dfrac{{1}}{{1+\\tan^2x}}={phan_so(1/(1+tan_value**2))}$"
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"        

    kq3_T=f"*$\\sin^2x={phan_so(1-1/(1+tan_value**2))}$" 
    kq3_F=f"$\\sin^2x={phan_so(1+1/(1+tan_value**2))}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$\\sin^2x=1-\\cos^2x=1-\\dfrac{{1}}{{1+\\tan^2x}}={phan_so(1-1/(1+tan_value**2))}$"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq=(a*tan_value+b)/(c*tan_value+d)

    kq4_T=f"*$P={latex((a*sinx+b*cosx)/(c*sinx+d*cosx))}={phan_so(kq)}$".replace("sinx",f"\\sin x").replace("cosx",f"\\cos x").replace("tanx",f"\\tan x")
    kq4_F=f"$P={latex((a*sinx+b*cosx)/(c*sinx+d*cosx))}={phan_so(kq+random.randint(1,3))}$".replace("sinx",f"\\sin x").replace("cosx",f"\\cos x").replace("tanx",f"\\tan x")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$P={latex((a*sinx+b*cosx)/(c*sinx+d*cosx))}={latex((a*tanx+b)/(c*tanx+d))}={phan_so((a*tan_value+b)/(c*tan_value+d))}$.".replace("sinx",f"\\sin x").replace("cosx",f"\\cos x").replace("tanx",f"\\tan x")
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

#[D11_C1_B2_08]-TF-M3. Chon cosx (a<x<b). Xét đúng sai: dấu của sinx, sinx, sin(x+kpi/2), P=f(tanx).
def ngh_kjg_L11_C1_B2_08():
    x=sp.symbols("x")
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])
    cung=random.choice([cung_I,cung_II,cung_III, cung_IV])       
   
    if cung==cung_I:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=a/b
            cos_value=sqrt(b**2-a**2)/b

            if is_rational(cos_value):
                cos_value_latex=phan_so(cos_value)
            else:
                cos_value_latex=latex(cos_value)

            tan_value=sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=sqrt(a)/t
            cos_value=sqrt(t**2-a)/t
            tan_value=sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(t**2-a)/t
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\sin x={sin_value_latex}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*$\\cos x >0$" 
        kq1_F=f"$\\cos x <0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x >0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(cos_value_false)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\cos x > 0$.\n\n"\
                f"$\\cos x =\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

    if cung==cung_II:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=a/b
            cos_value=-sqrt(b**2-a**2)/b
            tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=sqrt(a)/t
            cos_value=-sqrt(t**2-a)/t
            tan_value=-sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\sin x={sin_value_latex}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"

        kq1_T=f"*$\\cos x <0$" 
        kq1_F=f"$\\cos x >0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x <0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(-cos_value)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\cos x < 0$.\n\n"\
                f"$\\cos x=-\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung==cung_III:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=-a/b
            cos_value=-sqrt(b**2-a**2)/b
            tan_value=sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=-sqrt(a)/t
            cos_value=-sqrt(t**2-a)/t
            tan_value=sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\sin x={sin_value_latex}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"

        kq1_T=f"*$\\cos x <0$" 
        kq1_F=f"$\\cos x >0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x <0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(-cos_value)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\cos x < 0$.\n\n"\
                f"$\\cos x=-\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung==cung_IV:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=-a/b
            cos_value=sqrt(b**2-a**2)/b
            tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=-sqrt(a)/t
            cos_value=sqrt(t**2-a)/t
            tan_value=-sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)           
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\sin x={sin_value_latex}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"

        kq1_T=f"*$\\cos x >0$" 
        kq1_F=f"$\\cos x <0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x >0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(-cos_value)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $\\alpha \\in {cung}$ nên $\\cos x > 0$.\n\n"\
                f"$\\cos x=\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        
        k=random.randint(1,4)
        kq3_T=f"*$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)=-{sin_value_latex}$".replace("--","")
        kq3_F=f"$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)={sin_value_latex}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)=\\cos \\left( x+{latex(pi/2)}+{k}.2\\pi \\right)=\\cos \\left(x+{latex(pi/2)}\\right)"\
        f"=\\cos \\left[ {latex(pi/2)}-(-x) \\right]=\\sin (-x)=-\\sin x={latex(-sin_value)}$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        k=random.randint(1,4)
        kq3_T=f"*$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)={latex(cos_value)}$" 
        kq3_F=f"$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)={latex(-cos_value)}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)=\\sin \\left( x+{latex(pi/2)}+{k}.2\\pi \\right)=\\sin\\left(x+{latex(pi/2)}\\right)"\
        f"=\\sin \\left[ {latex(pi/2)}-(-x) \\right]=\\cos (-x)=\\cos x={latex(cos_value)}$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a=random.choice([sqrt(i) for i in range(1, 16)])
    b= random.choice([i for i in range(-5, 6) if i!=0])
    c= random.choice([i for i in range(-5, 6) if i!=0])

    # tan_value=sin_value/cos_value
    f=a*tan(x)/(b*tan(x)**2+c)
    kq=latex(a*tan_value/(b*tan_value**2+c))

    kq4_T=f"*$P={latex(f)}={latex(a*tan_value/(b*tan_value**2+c))}$".replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x").replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
    kq4_F=f"$P={latex(f)}={latex(-a*tan_value/(b*tan_value**2+c))}$".replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x").replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$\\tan x={sin_value_latex}:{latex(cos_value)}={latex(tan_value)}$.\n\n"\
    f"$\\Rightarrow P={latex(f)}={kq}$.".replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x").replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
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

#[D11_C1_B2_09]-TF-M3. Chon cosx (a<x<b). Xét đúng sai: dấu của sinx, sinx, sin(x+kpi/2), P=f(tanx).
def ngh_kjg_L11_C1_B2_09():
    x=sp.symbols("x")
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])
    cung=random.choice([cung_I,cung_II,cung_III, cung_IV])
    cung=cung_III   
   
    if cung==cung_I:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=a/b
            cos_value=sqrt(b**2-a**2)/b

            if is_rational(cos_value):
                cos_value_latex=phan_so(cos_value)
            else:
                cos_value_latex=latex(cos_value)

            tan_value=sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=sqrt(a)/t
            cos_value=sqrt(t**2-a)/t
            tan_value=sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(t**2-a)/t
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\cos x={latex(cos_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*$\\sin x >0$" 
        kq1_F=f"$\\sin x <0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\sin x >0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\sin x={sin_value_latex}$"
        kq2_F=f"$\\sin x=-{sin_value_latex}$".replace("--","")
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\sin x > 0$.\n\n"\
                f"$\\sin x =\\sqrt{{1-{phan_so(cos_value**2)}}}={sin_value_latex}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"       

    if cung==cung_II:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=a/b
            cos_value=-sqrt(b**2-a**2)/b
            tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=sqrt(a)/t
            cos_value=-sqrt(t**2-a)/t
            tan_value=-sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\cos x={latex(cos_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*$\\sin x >0$" 
        kq1_F=f"$\\sin x <0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\sin x >0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\sin x={sin_value_latex}$"
        kq2_F=f"$\\sin x=-{sin_value_latex}$".replace("--","")
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\sin x > 0$.\n\n"\
                f"$\\sin x =\\sqrt{{1-{phan_so(cos_value**2)}}}={sin_value_latex}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung==cung_III:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=-a/b
            cos_value=-sqrt(b**2-a**2)/b
            tan_value=sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=-sqrt(a)/t
            cos_value=-sqrt(t**2-a)/t
            tan_value=sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\cos x={latex(cos_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*$\\sin x <0$" 
        kq1_F=f"$\\sin x >0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\sin x >0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\sin x={sin_value_latex}$"
        kq2_F=f"$\\sin x=-{sin_value_latex}$".replace("--","")
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\sin x > 0$.\n\n"\
                f"$\\sin x =-\\sqrt{{1-{phan_so(cos_value**2)}}}={sin_value_latex}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung==cung_IV:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=-a/b
            cos_value=sqrt(b**2-a**2)/b
            tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=phan_so(sin_value)            

        if chon==2:
            [2,3,5,7,10,11,13]
            a=random.choice([2,3,5,7,10,11])
            t=a+random.randint(1,4)
            sin_value=-sqrt(a)/t
            cos_value=sqrt(t**2-a)/t
            tan_value=-sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)           
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\cos x={latex(cos_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*$\\sin x <0$" 
        kq1_F=f"$\\sin x >0$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\sin x <0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\sin x={sin_value_latex}$"
        kq2_F=f"$\\sin x=-{sin_value_latex}$".replace("--","")
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\sin x > 0$.\n\n"\
                f"$\\sin x =-\\sqrt{{1-{phan_so(cos_value**2)}}}={sin_value_latex}$."  
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        
        k=random.randint(1,4)
        kq3_T=f"*$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)=-{sin_value_latex}$".replace("--","")
        kq3_F=f"$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)={sin_value_latex}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)=\\cos \\left( x+{latex(pi/2)}+{k}.2\\pi \\right)=\\cos \\left(x+{latex(pi/2)}\\right)"\
        f"=\\cos \\left[ {latex(pi/2)}-(-x) \\right]=\\sin (-x)=-\\sin x={latex(-sin_value)}$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        k=random.randint(1,4)
        kq3_T=f"*$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)={latex(cos_value)}$" 
        kq3_F=f"$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)={latex(-cos_value)}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)=\\sin \\left( x+{latex(pi/2)}+{k}.2\\pi \\right)=\\sin\\left(x+{latex(pi/2)}\\right)"\
        f"=\\sin \\left[ {latex(pi/2)}-(-x) \\right]=\\cos (-x)=\\cos x={latex(cos_value)}$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a=random.choice([sqrt(i) for i in range(1, 16)])
    b= random.choice([i for i in range(-5, 6) if i!=0])
    c= random.choice([i for i in range(-5, 6) if i!=0])

    # tan_value=sin_value/cos_value
    f=a*tan(x)/(b*tan(x)**2+c)
    kq=latex(a*tan_value/(b*tan_value**2+c))

    kq4_T=f"*$P={latex(f)}={latex(a*tan_value/(b*tan_value**2+c))}$".replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x").replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
    kq4_F=f"$P={latex(f)}={latex(-a*tan_value/(b*tan_value**2+c))}$".replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x").replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$\\tan x={sin_value_latex}:{latex(cos_value)}={latex(tan_value)}$.\n\n"\
    f"$\\Rightarrow P={latex(f)}={kq}$.".replace(f"\\tan{{\\left(x \\right)}}",f"\\tan x").replace(f"\\tan^{{2}}{{\\left(x \\right)}}",f"\\tan^2 x")
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


#[D11_C1_B2_10]-TF-M3. Cho tanx (a<x<b). Xét đúng sai: dấu của sinx, sinx, sin(x+kpi/2), P=f(tanx).
def ngh_kjg_L11_C1_B2_10():
    x=sp.symbols("x")
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])
    cung=random.choice([cung_I,cung_II,cung_III, cung_IV])    
    
    if cung==cung_I:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=a/b
            cos_value=sqrt(b**2-a**2)/b

            if is_rational(cos_value):
                cos_value_latex=phan_so(cos_value)
            else:
                cos_value_latex=latex(cos_value)

            tan_value=sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:            
            a=random.choice([2,3,5,7])
            t=a+random.randint(1,4)
            sin_value=sqrt(a)/t
            cos_value=sqrt(t**2-a)/t
            tan_value=sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(t**2-a)/t
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\tan x={latex(tan_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*{random.choice([f"$\\cos x >0$", f"$\\sin x >0$"])}" 
        kq1_F=f"{random.choice([f"$\\cos x <0$", f"$\\sin x <0$"])}"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x >0, \\sin x >0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(-cos_value)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\cos x > 0$.\n\n"\
        f"$\\cos x=\\sqrt{{\\dfrac{{1}}{{1+\\tan^2x}}}}=\\sqrt{{\\dfrac{{1}} {{1+{phan_so(tan_value**2)}}} }}={latex(cos_value)}$"
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"       

    if cung==cung_II:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=a/b
            cos_value=-sqrt(b**2-a**2)/b
            tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=phan_so(sin_value)            

        if chon==2:            
            a=random.choice([2,3,5,7])
            t=a+random.randint(1,4)
            sin_value=sqrt(a)/t
            cos_value=-sqrt(t**2-a)/t
            tan_value=-sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\tan x={latex(tan_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*{random.choice([f"$\\cos x <0$", f"$\\sin x <0$"])}" 
        kq1_F=f"{random.choice([f"$\\cos x >0$", f"$\\sin x <0$"])}"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x <0, \\sin x<0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(-cos_value)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\cos x < 0$.\n\n"\
        f"$\\cos x=-\\sqrt{{\\dfrac{{1}}{{1+\\tan^2x}}}}=-\\sqrt{{\\dfrac{{1}} {{1+{phan_so(tan_value**2)}}} }}={latex(cos_value)}$"
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung==cung_III:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=-a/b
            cos_value=-sqrt(b**2-a**2)/b
            tan_value=sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:            
            a=random.choice([2,3,5,7])
            t=a+random.randint(1,4)
            sin_value=-sqrt(a)/t
            cos_value=-sqrt(t**2-a)/t
            tan_value=sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\tan x={latex(tan_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*{random.choice([f"$\\cos x <0$", f"$\\sin x <0$"])}" 
        kq1_F=f"{random.choice([f"$\\cos x >0$", f"$\\sin x >0$"])}"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x <0, \\sin x <0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(-cos_value)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\cos x < 0$.\n\n"\
        f"$\\cos x=-\\sqrt{{\\dfrac{{1}}{{1+\\tan^2x}}}}=-\\sqrt{{\\dfrac{{1}} {{1+{phan_so(tan_value**2)}}} }}={latex(cos_value)}$"
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung==cung_IV:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,10)
            b=a+random.randint(1,4) 
            sin_value=-a/b
            cos_value=sqrt(b**2-a**2)/b
            tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)            
            sin_value_latex=phan_so(sin_value)            

        if chon==2:            
            a=random.choice([2,3,5,7])
            t=a+random.randint(1,4)
            sin_value=-sqrt(a)/t
            cos_value=sqrt(t**2-a)/t
            tan_value=-sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)           
            sin_value_latex=latex(sin_value)

        noi_dung = f"Cho $\\tan x={latex(tan_value)}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*{random.choice([f"$\\cos x >0$", f"$\\sin x <0$"])}" 
        kq1_F=f"{random.choice([f"$\\cos x <0$", f"$\\sin x >0$"])}"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Với $x \\in {cung} $ thì $\\cos x >0, \\sin x <0$"
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"    

        kq2_T=f"*$\\cos x={latex(cos_value)}$"
        kq2_F=f"$\\cos x={latex(-cos_value)}$"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\cos x > 0$.\n\n"\
        f"$\\cos x=\\sqrt{{\\dfrac{{1}}{{1+\\tan^2x}}}}=\\sqrt{{\\dfrac{{1}} {{1+{phan_so(tan_value**2)}}} }}={latex(cos_value)}$"
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    chon=random.randint(1,2)
    if chon==1:
        
        k=random.randint(1,4)
        kq3_T=f"*$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)=-{sin_value_latex}$".replace("--","")
        kq3_F=f"$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)={sin_value_latex}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\cos\\left(x+ {latex((1+4*k)*pi/2)} \\right)=\\cos \\left( x+{latex(pi/2)}+{k}.2\\pi \\right)=\\cos \\left(x+{latex(pi/2)}\\right)"\
        f"=\\cos \\left[ {latex(pi/2)}-(-x) \\right]=\\sin (-x)=-\\sin x={latex(-sin_value)}$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    
    if chon==2:
        k=random.randint(1,4)
        kq3_T=f"*$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)={latex(cos_value)}$" 
        kq3_F=f"$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)={latex(-cos_value)}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\sin\\left(x+ {latex((1+4*k)*pi/2)} \\right)=\\sin \\left( x+{latex(pi/2)}+{k}.2\\pi \\right)=\\sin\\left(x+{latex(pi/2)}\\right)"\
        f"=\\sin \\left[ {latex(pi/2)}-(-x) \\right]=\\cos (-x)=\\cos x={latex(cos_value)}$."
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    a= random.choice([i for i in range(-5, 6) if i!=0])
    b= random.choice([i for i in range(-5, 6) if i!=0])
    c= random.choice([i for i in range(-5, 6) if i!=0])
    d= random.choice([i for i in range(-5, 6) if i!=0])

    # tan_value=sin_value/cos_value
    f=(a*sin(x)**2+b*sin(x)*cos(x))/(c*sin(x)**2+d*sin(x)*cos(x))
    f_tan=(a*tan(x)**2+b*tan(x))/(c*tan(x)**2+d*tan(x))
    kq=latex(a*tan_value**2+b*tan_value/(c*tan_value**2+d))

    kq4_T=thay_sin_cos(f"*$P={latex(f)}={kq}$")
    kq4_F=thay_sin_cos(f"$P={latex(f)}={latex(-a*tan_value**2+b*tan_value/(c*tan_value**2+d))}$")
    kq4=random.choice([kq4_T, kq4_F])
    HDG= thay_sin_cos(f"$P={latex(f)}={latex(f_tan)}={kq}$.")
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





################  Bài 2: Các giá trị lượng giác.################

#D11_C1_B2_01. Tính giá trị đặc biệt của một góc lượng giác.
def ngh_kjg_L11_C1_B2_01():
    list_x=[2*pi/3, 13*pi/6 , 25*pi/3, 37*pi/6 , 103*pi/3]
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
    pa_A= f"*$ {latex((ham))} $"
    pa_B= f"$ {latex((list_hamkhac[0]))} $"
    pa_C= f"$ {latex((list_hamkhac[1]))} $"
    pa_D= f"$ {latex((list_hamkhac[2]))} $"
     #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tính $\\{ten_ham}{latex(x)}$."
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

    

################  Bài 3: Các công thức lượng giác.################

#[D11_C1_B3_01]  Cho sina, cosa. Tính sin2a.
def ngh_kjg_L11_C1_B3_01():
    fraction =  my_module.tao_2_phanso()  
    value_sina = fraction[0]
    value_cosa = fraction[1]
    #Tạo các phương án
    pa_A= f"*$ {latex((2*value_sina*value_cosa))} $"
    pa_B= f"$ {latex(value_sina*value_cosa)} $"    
    pa_C= f"$ {latex(2*value_sina)} $"  
    pa_D= f"$ {latex(2*value_cosa)} $"  
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho $\\sin a= {latex(value_sina)}, \\cos a={latex(value_cosa)}$. Tính giá trị $\\sin 2a$. "

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


#[D11_C1_B3_02] Cho sina hoặc cosa. Tính cos2a.
def ngh_kjg_L11_C1_B3_02():
    list_sin= [-1/2, -1/4, -1/8, 5/6, 2/3, 3/7]
    t = random.choice(list_sin)
    latex_t=latex(Rational(t).limit_denominator(100))
     #Tạo các phương án
    pa_A= f"*$ {latex(Rational(1-2*t*t).limit_denominator(100))} $"  
    pa_B= f"$ {latex(Rational(2*t*t-1).limit_denominator(100))} $" 
    pa_C= f"$ {latex(Rational(1-t*t).limit_denominator(100))} $" 
    pa_D= f"$ {latex(Rational(2*t).limit_denominator(100))} $" 
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Cho $\\sin a= {latex_t}$. Tính giá trị $\\cos 2a$. "

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

#[D11_C1_B3_03]-M2. Tìm khẳng định đúng về công thức đối
def ngh_kjg_L11_C1_B3_03():
    x=random.choice(["x","a", "\\alpha", "\\beta", f"{random.randint(2,5)}x", f"{random.randint(2,5)}a", f"{random.randint(2,5)}\\beta"])
    noi_dung=f"Cho ${{{x}}}$ là góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos (-{x})=\\cos {x}",
        f"\\sin (-{x})=-\\sin {x}",
        f"\\tan (-{x})=-\\tan {x}",
        f"\\cot (-{x})=-\\cot {x}"
        ])

    kq2=random.choice([
        f"\\cos (-{x})=-\\cos {x}",
        f"\\cos (-{x})=\\sin {x}",
        ])

    kq3=random.choice([
        f"\\sin (-{x})=\\sin {x}",
        f"\\sin (-{x})=\\cos {x}"
        ])

    kq4=random.choice([
    f"\\tan (-{x})=\\tan {x}",
    f"\\tan (-{x})=\\cot {x}",
    f"\\cot (-{x})=\\tan {x}"
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_04]-M2. Tìm khẳng định đúng về hai góc bù nhau
def ngh_kjg_L11_C1_B3_04():
    x=random.choice(["x","a", "\\alpha", "\\beta", f"{random.randint(2,5)}x", f"{random.randint(2,5)}a", f"{random.randint(2,5)}\\beta"])
    noi_dung=f"Cho ${{{x}}}$ là góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos (\\pi-{x})=-\\cos {x}",
        f"\\sin (\\pi-{x})=\\sin {x}",
        f"\\tan (\\pi-{x})=-\\tan {x}",
        f"\\cot (\\pi-{x})=-\\cot {x}"
        ])

    kq2=random.choice([
        f"\\cos (\\pi-{x})=\\cos {x}",
        f"\\cos (\\pi-{x})=\\sin {x}"
        ])

    kq3=random.choice([
        f"\\sin (\\pi-{x})=-\\sin {x}",
        f"\\sin (\\pi-{x})=\\cos {x}"
        ])

    kq4=random.choice([
    f"\\tan (\\pi-{x})=\\tan {x}",
    f"\\tan (\\pi-{x})=\\cot {x}",
    f"\\cot (\\pi-{x})=\\tan {x}",
    f"\\cot (\\pi-{x})=\\cot {x}"
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_05]-M2. Tìm khẳng định đúng về hai góc phụ nhau
def ngh_kjg_L11_C1_B3_05():
    x=random.choice(["x","a", "\\alpha", "\\beta", f"{random.randint(2,5)}x", f"{random.randint(2,5)}a", f"{random.randint(2,5)}\\beta"])
    noi_dung=f"Cho ${{{x}}}$ là góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos \\left({latex(pi/2)}-{x}\\right)=\\sin {x}",
        f"\\sin \\left({latex(pi/2)}-{x}\\right)=\\cos {x}",
        f"\\tan \\left({latex(pi/2)}-{x}\\right)=\\cot {x}",
        f"\\cot \\left({latex(pi/2)}-{x}\\right)=\\tan {x}"
        ])

    kq2=random.choice([
        f"\\cos \\left({latex(pi/2)}-{x}\\right)=\\cos {x}",
        f"\\sin \\left({latex(pi/2)}-{x}\\right)=\\sin {x}"
        ])

    kq3=random.choice([
        f"\\sin \\left({latex(pi/2)}-{x}\\right)=-\\sin {x}",
        f"\\cos \\left({latex(pi/2)}-{x}\\right)=-\\cos {x}"
        ])

    kq4=random.choice([
    f"\\tan \\left({latex(pi/2)}-{x}\\right)=\\tan {x}",
    f"\\tan \\left({latex(pi/2)}-{x}\\right)=-\\tan {x}",
    f"\\cot \\left({latex(pi/2)}-{x}\\right)=\\cot {x}",
    f"\\cot \\left({latex(pi/2)}-{x}\\right)=-\\cot {x}"
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_06]-M2. Tìm khẳng định đúng về hai góc bù nhau
def ngh_kjg_L11_C1_B3_06():
    x=random.choice(["x","a", "\\alpha", "\\beta", f"{random.randint(2,5)}x", f"{random.randint(2,5)}a", f"{random.randint(2,5)}\\beta"])
    noi_dung=f"Cho ${{{x}}}$ là góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos (\\pi+{x})=-\\cos {x}",
        f"\\sin (\\pi+{x})=-\\sin {x}",
        f"\\tan (\\pi+{x})=\\tan {x}",
        f"\\cot (\\pi+{x})=\\cot {x}",
        ])

    kq2=random.choice([
        f"\\cos (\\pi+{x})=\\cos {x}",
        f"\\cos (\\pi+{x})=\\sin {x}",
        ])

    kq3=random.choice([
        f"\\sin (\\pi+{x})=\\sin {x}",
        f"\\sin (\\pi+{x})=\\cos {x}",
        ])

    kq4=random.choice([
    f"\\tan (\\pi+{x})=-\\tan {x}",
    f"\\tan (\\pi+{x})=\\cot {x}",
    f"\\cot (\\pi+{x})=\\tan {x}",
    f"\\cot (\\pi+{x})=-\\cot {x}",
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_07]-M2. Tìm khẳng định đúng về hai góc liên quan tùy ý
def ngh_kjg_L11_C1_B3_07():
    x=random.choice(["x","a","b", "\\alpha", "\\beta", f"\\gamma"])
    noi_dung=f"Cho ${{{x}}}$ là góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos (-{x})=\\cos {x}",
        f"\\sin (-{x})=-\\sin {x}",
        f"\\tan (-{x})=-\\tan {x}",
        f"\\cot (-{x})=-\\cot {x}",

        f"\\cos (\\pi-{x})=-\\cos {x}",
        f"\\sin (\\pi-{x})=\\sin {x}",
        f"\\tan (\\pi-{x})=-\\tan {x}",
        f"\\cot (\\pi-{x})=-\\cot {x}",

        f"\\cos \\left({latex(pi/2)}-{x}\\right)=\\sin {x}",
        f"\\sin \\left({latex(pi/2)}-{x}\\right)=\\cos {x}",
        f"\\tan \\left({latex(pi/2)}-{x}\\right)=\\cot {x}",
        f"\\cot \\left({latex(pi/2)}-{x}\\right)=\\tan {x}",

        f"\\cos (\\pi+{x})=-\\cos {x}",
        f"\\sin (\\pi+{x})=-\\sin {x}",
        f"\\tan (\\pi+{x})=\\tan {x}",
        f"\\cot (\\pi+{x})=\\cot {x}"        
        ])

    kq2=random.choice([
        f"\\cos (-{x})=-\\cos {x}",
        f"\\cos (-{x})=\\sin {x}",

        f"\\cos (\\pi-{x})=\\cos {x}",
        f"\\cos (\\pi-{x})=\\sin {x}",

        f"\\cos (\\pi+{x})=\\cos {x}",
        f"\\cos (\\pi+{x})=\\sin {x}",

        f"\\cos \\left({latex(pi/2)}-{x}\\right)=\\cos {x}",
        f"\\sin \\left({latex(pi/2)}-{x}\\right)=\\sin {x}"
        ])

    kq3=random.choice([
        f"\\sin (\\pi+{x})=\\sin {x}",
        f"\\sin (\\pi+{x})=\\cos {x}",

        f"\\sin (\\pi-{x})=-\\sin {x}",
        f"\\sin (\\pi-{x})=\\cos {x}",

        f"\\sin (-{x})=\\sin {x}",
        f"\\sin (-{x})=\\cos {x}",

        f"\\sin \\left({latex(pi/2)}-{x}\\right)=-\\sin {x}",
        f"\\cos \\left({latex(pi/2)}-{x}\\right)=-\\cos {x}"
        ])

    kq4=random.choice([
    f"\\tan (-{x})=\\tan {x}",
    f"\\tan (-{x})=\\cot {x}",  

    f"\\tan (\\pi-{x})=\\tan {x}",
    f"\\tan (\\pi-{x})=\\cot {x}",
    f"\\cot (\\pi-{x})=\\tan {x}",
    f"\\cot (\\pi-{x})=\\cot {x}",

    f"\\tan (\\pi+{x})=-\\tan {x}",
    f"\\tan (\\pi+{x})=\\cot {x}",
    f"\\cot (\\pi+{x})=\\tan {x}",
    f"\\cot (\\pi+{x})=-\\cot {x}",

    f"\\tan \\left({latex(pi/2)}-{x}\\right)=\\tan {x}",
    f"\\tan \\left({latex(pi/2)}-{x}\\right)=-\\tan {x}",
    f"\\cot \\left({latex(pi/2)}-{x}\\right)=\\cot {x}",
    f"\\cot \\left({latex(pi/2)}-{x}\\right)=-\\cot {x}"
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_08]-M2. Tìm khẳng định đúng về công thức nhân đôi
def ngh_kjg_L11_C1_B3_08():
    x=random.choice(["x","a","b", "\\alpha", "\\beta", "\\gamma"])
    noi_dung=f"Cho ${{{x}}}$ là góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos 2{x}=2\\cos^2 {x}-1",
        f"\\cos 2{x}=1-2\\sin^2 {x}",
        f"\\cos 2{x}=\\cos^2 {x}-\\sin^2 {x}",
        f"\\sin 2{x}=2\\sin {x}\\cos {x}",
        f"\\tan 2{x}=\\dfrac{{2\\tan {x}}}{{1-\\tan^2 {x}}}"
        ])

    kq2=random.choice([
        f"\\cos 2{x}=1-2\\cos^2 {x}",
        f"\\cos 2{x}=2\\sin^2 {x}-1",
        f"\\cos 2{x}=\\sin^2 {x}-\\cos^2 {x}",
        f"\\cos 2{x}=2\\sin {x}\\cos {x}"
        ])

    kq3=random.choice([
        f"\\sin 2{x}=\\sin {x}\\cos {x}",
        f"\\sin 2{x}=\\sin {x}+\\cos {x}",
        f"\\sin 2{x}=2\\sin {x}"
        ])

    kq4=random.choice([
    f"\\tan 2{x}=\\dfrac{{2\\tan {x}}}{{1+\\tan^2 {x}}}",
    f"\\tan 2{x}=\\dfrac{{\\tan {x}}}{{1-\\tan^2 {x}}}",
    f"\\tan 2{x}=\\dfrac{{\\tan {x}}}{{1-2\\tan^2 {x}}}"
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_09]-M2. Tìm khẳng định đúng về công thức cộng
def ngh_kjg_L11_C1_B3_09():
    a=["x","a", "\\alpha", "u"]
    b=["y","b", "\\beta", "v"]
    i=random.randint(0,3)
    a,b=a[i], b[i]

    noi_dung=f"Cho ${{{a},{b}}}$ là các góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos ({a}+{b})=\\cos {a} \\cos {b}-\\sin {a} \\sin {b}",
        f"\\cos ({a}-{b})=\\cos {a} \\cos {b}+\\sin {a} \\sin {b}",
        f"\\sin ({a}+{b})=\\sin {a} \\cos {b}+\\cos {a} \\sin {b} ",
        f"\\sin ({a}-{b})=\\sin {a} \\cos {b}-\\cos {a} \\sin {b} " , 
        f"\\tan ({a}+{b})=\\dfrac{{\\tan {a} + \\tan {b} }} {{1-\\tan {a} \\tan {b} }}",
        f"\\tan ({a}-{b})=\\dfrac{{\\tan {a} - \\tan {b} }} {{1+\\tan {a} \\tan {b} }}"
        ])

    kq2=random.choice([
        f"\\cos ({a}+{b})=\\cos {a} \\cos {b}+\\sin {a} \\sin {b}",
        f"\\cos ({a}-{b})=\\cos {a} \\cos {b}-\\sin {a} \\sin {b}" ,
         f"\\cos ({a}+{b})=\\cos {a} +\\cos {b}" ,
         f"\\cos ({a}-{b})=\\cos {a} -\\cos {b}"     
        ])

    kq3=random.choice([
        f"\\sin ({a}+{b})=\\sin {a} \\cos {b}- \\cos {a} \\sin {b}",
        f"\\sin ({a}-{b})=\\sin {a} \\cos {b}+\\cos {a} \\sin {b} ",
        f"\\sin ({a}+{b})=\\sin {a} +\\sin {b}",
        f"\\sin ({a}-{b})=\\sin {a} -\\sin {b}"        
        ])

    kq4=random.choice([
    f"\\tan ({a}+{b})=\\dfrac{{\\tan {a} + \\tan {b} }} {{1+\\tan {a} \\tan {b} }}",
    f"\\tan ({a}-{b})=\\dfrac{{\\tan {a} - \\tan {b} }} {{1-\\tan {a} \\tan {b} }}" ,
    f"\\tan ({a}+{b})=\\tan {a} + \\tan {b}",
    f"\\tan ({a}-{b})=\\tan {a} - \\tan {b}"    
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_10]-M2. Tìm khẳng định đúng về công thức tổng thành tích
def ngh_kjg_L11_C1_B3_10():
    a=["x","a", "\\alpha", "u"]
    b=["y","b", "\\beta", "v"]
    i=random.randint(0,3)
    a,b=a[i], b[i]

    noi_dung=f"Cho ${{{a},{b}}}$ là các góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos {a} + \\cos {b}=2\\cos \\dfrac{{{a}+{b}}}{{2}} \\cos \\dfrac{{{a}-{b}}}{{2}}", 
        f"\\cos {a} - \\cos {b}=-2\\sin \\dfrac{{{a}+{b}}}{{2}} \\sin \\dfrac{{{a}-{b}}}{{2}}",
        f"\\sin {a} + \\sin {b}=2\\sin \\dfrac{{{a}+{b}}}{{2}} \\cos \\dfrac{{{a}-{b}}}{{2}}" ,
        f"\\sin {a} - \\sin {b}=2\\cos \\dfrac{{{a}+{b}}}{{2}} \\sin \\dfrac{{{a}-{b}}}{{2}}"  
        ])

    kq2=random.choice([
        f"\\cos {a} + \\cos {b}=\\cos \\dfrac{{{a}+{b}}}{{2}} \\cos \\dfrac{{{a}-{b}}}{{2}}", 
        f"\\cos {a} - \\cos {b}=-\\sin \\dfrac{{{a}+{b}}}{{2}} \\sin \\dfrac{{{a}-{b}}}{{2}}"  
        ])

    kq3=random.choice([
        f"\\sin {a} + \\sin {b}=2\\cos \\dfrac{{{a}+{b}}}{{2}} \\sin \\dfrac{{{a}-{b}}}{{2}}" ,
        f"\\sin {a} + \\cos {b}=2\\cos \\dfrac{{{a}+{b}}}{{2}} \\cos \\dfrac{{{a}-{b}}}{{2}}",    
        ])

    kq4=random.choice([
    f"\\sin {a} - \\sin {b}=2\\sin \\dfrac{{{a}+{b}}}{{2}} \\cos \\dfrac{{{a}-{b}}}{{2}}",
    f"\\sin {a} - \\cos {b}=-2\\sin \\dfrac{{{a}+{b}}}{{2}} \\sin \\dfrac{{{a}-{b}}}{{2}}",
  
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_11]-M2. Tìm khẳng định đúng về công thức tích thành tổng
def ngh_kjg_L11_C1_B3_11():
    a=["x","a", "\\alpha", "u"]
    b=["y","b", "\\beta", "v"]
    i=random.randint(0,3)
    a,b=a[i], b[i]

    noi_dung=f"Cho ${{{a},{b}}}$ là các góc lượng giác. Tìm khẳng định đúng trong các khẳng định sau."   

    kq=random.choice([
        f"\\cos {a} \\cos {b}=\\dfrac 1 2[\\cos({a}+{b}) + \\cos({a}-{b})]", 
        f"\\sin {a} \\sin {b}=\\dfrac 1 2[\\cos({a}-{b}) - \\cos({a}+{b})]",
        f"\\sin {a} \\cos {b}=\\dfrac 1 2[\\sin({a}+{b}) + \\sin({a}-{b})]"        
        ])

    kq2=random.choice([
        f"\\cos {a} \\cos {b}=\\dfrac 1 2[\\cos({a}+{b}) - \\cos({a}-{b})]", 
        f"\\cos {a} \\cos {b}=-\\dfrac 1 2[\\cos({a}+{b}) + \\cos({a}-{b})]"
       
        ])

    kq3=random.choice([
       f"\\sin {a} \\sin {b}=-\\dfrac 1 2[\\cos({a}-{b}) - \\cos({a}+{b})]",
       f"\\sin {a} \\sin {b}=\\dfrac 1 2[\\cos({a}+{b}) - \\cos({a}-{b})]"       
        ])

    kq4=random.choice([
    f"\\sin {a} \\cos {b}=\\dfrac 1 2[\\sin({a}+{b}) - \\sin({a}-{b})]",
    f"\\sin {a} \\cos {b}=\\dfrac 1 2[\\cos({a}+{b}) - \\cos({a}-{b})]"
  
    ])

    noi_dung_loigiai=f"${kq}$ là khẳng định đúng."

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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

#[D11_C1_B3_12]-TF-M2. Cho tanx. Xét Đ-S: cotx, cos2x, sin2x, tan2x
def ngh_kjg_L11_C1_B3_12():
    tan_value=random.choice([i for i in range(-8, 10) if i!=0])
    while 2/(tan_value**2+1)-1==0:
        tan_value=random.choice([i for i in range(-8, 10) if i!=0])
    
    x=random.choice(["x","a","b", "\\alpha", "\\beta", "\\gamma"])

    noi_dung = f"Cho $\\tan {x}={tan_value}$ . Xét tính đúng-sai của các khẳng định sau."        
    debai_word= f"{noi_dung}\n"
    
        
    kq1_T=f"*$\\cot {x}={phan_so(1/tan_value)}$" 
    kq1_F=f"$\\cot {x}={phan_so(1/tan_value+random.randint(1,4))}$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\cot {x} = {phan_so(1/tan_value)}$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    cos2x=2/(tan_value**2+1)-1
    cos2x_false=2/(tan_value**2+1)-random.randint(2,4)

    kq2_T=f"*$\\cos 2{x}={phan_so(cos2x)}$"
    kq2_F=f"$\\cos 2{x}={phan_so(cos2x_false)}$ "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$\\cos 2{x}=2\\cos^2 {x}-1=\\dfrac{{2}}{{1+\\tan^2 {x}}}-1={phan_so(cos2x)}$."
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    sin2x=2*tan_value/(1+tan_value**2)
    sin2x_false=2*tan_value/(1+tan_value**2)+random.randint(1,3)

    kq3_T=f"*$\\sin 2{x}={phan_so(sin2x)}$" 
    kq3_F=f"$\\sin 2{x}={phan_so(sin2x_false)}$"
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"$\\sin 2{x}=2\\sin {x} \\cos {x}=2\\tan {x} \\cos^2 {x}=\\dfrac{{2\\tan {x}}} {{1+\\tan^2 {x}}}={phan_so(sin2x)}$"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    tan2x=sin2x/cos2x
    tan2x_false=sin2x/cos2x+random.randint(1,3)
    kq4_T=f"*$\\tan 2{x}={phan_so(tan2x)}$"
    kq4_F=f"$\\tan 2{x}={phan_so(sin2x)}:{phan_so(cos2x)}={phan_so(tan2x_false)}$ " 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"$\\tan 2{x}=\\dfrac{{\\sin 2{x}}}{{\\cos 2{x}}}={phan_so(tan2x)}$."
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

#[D11_C1_B3_13]-TF-M2. Cho sinx. Xét Đ-S: cosx, sin2x, sin(x+a), cos(x+b)
def ngh_kjg_L11_C1_B3_13():
    x=random.choice(["x","a","\\alpha","\\beta", "\\gamma" ])
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])
    cung=random.choice([cung_I,cung_II])       
    
    if cung==cung_I:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,9)
            b=a+random.randint(1,3) 
            sin_value=a/b
            cos_value=sqrt(b**2-a**2)/b

            if is_rational(cos_value):
                cos_value_latex=phan_so(cos_value)
            else:
                cos_value_latex=latex(cos_value)

            tan_value=sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:            
            a=random.choice([2,3,5,6,7])
            t=a+random.randint(1,3)
            sin_value=sqrt(a)/t
            cos_value=sqrt(t**2-a)/t
            if is_rational(cos_value):
                cos_value_latex=phan_so(cos_value)
            else:
                cos_value_latex=latex(cos_value)

            tan_value=sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=-sqrt(t**2-a)/t
            sin_value_latex=latex(sin_value)


        noi_dung = f"Cho $\\sin {x}={sin_value_latex}, {x}\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*$\\cos {x}={cos_value_latex}$"
        kq1_F=f"$\\cos {x}={latex(cos_value_false)}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Vì ${x} \\in {cung}$ nên $\\cos {x} > 0$.\n\n"\
                f"$\\cos {x} =\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$."  
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"  

        sin2x=2*sin_value*cos_value
        sin2x_false=sin_value*cos_value       


        kq2_T=f"*$\\sin 2{x}={latex(nsimplify(sin2x).rewrite(sqrt))}$"
        kq2_F=f"$\\sin 2{x}={latex(nsimplify(sin2x_false).rewrite(sqrt))}$ "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"$\\sin 2{x}=2\\sin {x} \\cos {x}=2.{sin_value_latex}.{cos_value_latex}={latex(nsimplify(sin2x).rewrite(sqrt))}$."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        cos2x=1-2*sin_value**2
        cos2x_false=2*sin_value**2-1

        kq3_T=f"*$\\cos 2{x}={phan_so(cos2x)}$" 
        kq3_F=f"$\\cos 2{x}={phan_so(cos2x_false)}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\cos 2{x}=1-2\\sin^2 {x}=1-2.{phan_so(sin_value**2)}={phan_so(cos2x)}$"
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        m=random.choice([pi, pi/2, pi/3, pi/4,pi/6, -pi/2, -pi/3, -pi/4,-pi/6,-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4])
        t=sin_value*cos(m)+cos_value*sin(m)
        t_false=sin_value+cos_value

        kq4_T=f"*$\\sin\\left({x}+{latex(m)}\\right)={latex(nsimplify(t))}$".replace("+-","-")
        kq4_F=f"$\\sin\\left({x}+{latex(m)}\\right)={latex(nsimplify(t_false))}$".replace("+-","-") 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$\\sin\\left({x}+{latex(m)}\\right)=\\sin {x}\\cos ({latex(m)})+\\cos {x} \\sin ({latex(m)})=$"\
        f"${sin_value_latex}.({latex(cos(m))})+{latex(cos_value)}.({latex(sin(m))})={latex(nsimplify(t))}$.".replace("+-","-")
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if cung==cung_II:    
        chon=random.randint(1,2)        
        if chon==1:        
            a=random.randint(1,9)
            b=a+random.randint(1,3) 
            sin_value=a/b
            cos_value=-sqrt(b**2-a**2)/b

            if is_rational(cos_value):
                cos_value_latex=phan_so(cos_value)
            else:
                cos_value_latex=latex(cos_value)

            tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=sqrt(b**2-a**2)/b
            sin_value_latex=phan_so(sin_value)            

        if chon==2:            
            a=random.choice([2,3,5,6,7])
            t=a+random.randint(1,3)
            sin_value=sqrt(a)/t
            cos_value=-sqrt(t**2-a)/t
            if is_rational(cos_value):
                cos_value_latex=phan_so(cos_value)
            else:
                cos_value_latex=latex(cos_value)

            tan_value=-sqrt(a)/sqrt(t**2-a)
            tan_value_latex=tan_value.rewrite(sqrt)

            cos_value_false=sqrt(t**2-a)/t
            sin_value_latex=latex(sin_value)


        noi_dung = f"Cho $\\sin x={sin_value_latex}, x\\in {cung}$. Xét tính đúng-sai của các khẳng định sau."
        debai_word= f"{noi_dung}\n"      

        kq1_T=f"*$\\cos {x}={cos_value_latex}$"
        kq1_F=f"$\\cos {x}={latex(cos_value_false)}$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Vì $x \\in {cung}$ nên $\\cos x < 0$.\n\n"\
                f"$\\cos x =-\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$."  
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"  

        sin2x=2*sin_value*cos_value
        sin2x_false=sin_value*cos_value       


        kq2_T=f"*$\\sin 2{x}={latex(nsimplify(sin2x).rewrite(sqrt))}$"
        kq2_F=f"$\\sin 2{x}={latex(nsimplify(sin2x_false).rewrite(sqrt))}$ "
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"$\\sin 2{x}=2\\sin {x} \\cos {x}=2.{sin_value_latex}.({cos_value_latex})={latex(nsimplify(sin2x).rewrite(sqrt))}$."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        cos2x=1-2*sin_value**2
        cos2x_false=2*sin_value**2-1

        kq3_T=f"*$\\cos 2{x}={phan_so(cos2x)}$" 
        kq3_F=f"$\\cos 2{x}={phan_so(cos2x_false)}$ "
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\cos 2{x}=1-2\\sin^2 {x}=1-2.{phan_so(sin_value**2)}={phan_so(cos2x)}$"
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        m=random.choice([pi, pi/2, pi/3, pi/4,pi/6, -pi/2, -pi/3, -pi/4,-pi/6,-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4])
        t=sin_value*cos(m)+cos_value*sin(m)
        t_false=sin_value+cos_value

        kq4_T=f"*$\\sin\\left({x}+{latex(m)}\\right)={latex(nsimplify(t))}$".replace("+-","-")
        kq4_F=f"$\\sin\\left({x}+{latex(m)}\\right)={latex(nsimplify(t_false))}$".replace("+-","-") 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"$\\sin\\left({x}+{latex(m)}\\right)=\\sin {x}\\cos ({latex(m)})+\\cos {x} \\sin ({latex(m)})=$"\
        f"${sin_value_latex}.({latex(cos(m))})+({latex(cos_value)}).({latex(sin(m))})={latex(nsimplify(t))}$.".replace("+-","-")
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

#[D11_C1_B3_14]-M3. Cho sinx. Tính sin(x+a) hoặc cos(x+b)
def ngh_kjg_L11_C1_B3_14():
    x=random.choice(["x","a","\\alpha","\\beta", "\\gamma" ])
    cung_I=random.choice([f"\\left( 0;{latex(pi/2)} \\right)", f"\\left( 2\\pi;{latex(5*pi/2)} \\right)"])
    cung_II=random.choice([f"\\left( {latex(pi/2)};\\pi \\right)", f"\\left( {latex(5*pi/2)};3\\pi \\right)", f"\\left( {latex(-3*pi/2)};{latex(-pi)} \\right)"])
    cung_III=random.choice([f"\\left( \\pi;{latex(3*pi/2)} \\right)", f"\\left( {latex(3*pi)};{latex(7*pi/2)} \\right)", f"\\left( {latex(-pi)}; {latex(-pi/2)} \\right)"])
    cung_IV=random.choice([f"\\left( {latex(3*pi/2)}; 2\\pi \\right)", f"\\left( {latex(7*pi/2)}; 4\\pi \\right)", f"\\left( {latex(-pi/2)}; 0 \\right)"])
    cung=random.choice([cung_I,cung_II])   
    
    if cung==cung_I:
     
        a=random.randint(1,9)
        b=a+random.randint(1,3) 
        sin_value=a/b
        cos_value=sqrt(b**2-a**2)/b

        if is_rational(cos_value):
            cos_value_latex=phan_so(cos_value)
        else:
            cos_value_latex=latex(cos_value)

        tan_value=sqrt(a**2)/sqrt(b**2-a**2)
        tan_value_latex=tan_value.rewrite(sqrt)

        cos_value_false=-sqrt(b**2-a**2)/b
        sin_value_latex=phan_so(sin_value)
        m=random.choice([pi/3, pi/6, -pi/3, -pi/4,-pi/6, 2*pi/3, 3*pi/4, 5*pi/6, -2*pi/3, -3*pi/4, -5*pi/6])

        kq=sin_value*cos(m)+cos_value*sin(m)
        kq2=sin_value+cos_value
        kq3=sin_value*cos(m)-cos_value*sin(m)
        kq4=cos_value*cos(m)+sin_value*sin(m)

        pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
        kq2=pa_kotrung[1]
        kq3=pa_kotrung[2]
        kq4=pa_kotrung[3]
        
        noi_dung=(f"Cho $\\sin {x}={sin_value_latex}$ với ${x}\\in {cung}$."
        f" Tính $\\sin\\left({x}+{latex(m)}\\right)$.".replace("+-","-"))

        noi_dung_loigiai=(f"Vì ${x} \\in {cung}$ nên $\\cos {x} > 0$.\n\n"
                f"$\\cos {x} =\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$.\n\n" 
                f"$\\sin\\left({x}+{latex(m)}\\right)=\\sin {x}\\cos ({latex(m)})+\\cos {x} \\sin ({latex(m)})=$"
        f"${sin_value_latex}.({latex(cos(m))})+{latex(cos_value)}.({latex(sin(m))})={latex(nsimplify(kq))}$.".replace("+-","-"))

    if cung==cung_II:
     
        a=random.randint(1,9)
        b=a+random.randint(1,3) 
        sin_value=a/b
        cos_value=-sqrt(b**2-a**2)/b

        if is_rational(cos_value):
            cos_value_latex=phan_so(cos_value)
        else:
            cos_value_latex=latex(cos_value)

        tan_value=-sqrt(a**2)/sqrt(b**2-a**2)
        tan_value_latex=tan_value.rewrite(sqrt)

        cos_value_false=sqrt(b**2-a**2)/b
        sin_value_latex=phan_so(sin_value)
        m=random.choice([pi/3, pi/6, -pi/3, -pi/4,-pi/6, 2*pi/3, 3*pi/4, 5*pi/6, -2*pi/3, -3*pi/4, -5*pi/6])

        kq=sin_value*cos(m)+cos_value*sin(m)
        kq2=sin_value+cos_value
        kq3=sin_value*cos(m)-cos_value*sin(m)
        kq4=cos_value*cos(m)+sin_value*sin(m)
        
        pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
        kq2=pa_kotrung[1]
        kq3=pa_kotrung[2]
        kq4=pa_kotrung[3]
        
        noi_dung=(f"Cho $\\sin {x}={sin_value_latex}$ với ${x}\\in {cung}$."
        f" Tính $\\sin\\left({x}+{latex(m)}\\right)$.".replace("+-","-"))

        noi_dung_loigiai=(f"Vì ${x} \\in {cung}$ nên $\\cos {x} < 0$.\n\n"
                f"$\\cos {x} =-\\sqrt{{1-{phan_so(sin_value**2)}}}={latex(cos_value)}$.\n\n" 
                f"$\\sin\\left({x}+{latex(m)}\\right)=\\sin {x}\\cos ({latex(m)})+\\cos {x} \\sin ({latex(m)})=$"
        f"${sin_value_latex}.({latex(cos(m))})+({latex(cos_value)}).({latex(sin(m))})={latex(nsimplify(kq))}$.".replace("+-","-"))
    

    kq=f"${latex(nsimplify(kq))}$"
    kq2=f"${latex(nsimplify(kq2))}$"
    kq3=f"${latex(nsimplify(kq3))}$"
    kq4=f"${latex(nsimplify(kq4))}$"

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

################  Bài 4: Hàm số lượng giác và đồ thị.################
#[D11_C1_B4_01]. Tìm tập xác định hàm số y=a/sinx hoặc y=a/cosx
def ngh_kjg_L11_C1_B4_01():
    x=sp.symbols("x")
    a = random.randint(1,10)
    b = random.choice([-5,5])
    mau = random.choice(["sinx", "cosx"])
    if mau == "sinx":
        f=(a*cos(x)+b)/sin(x)
        kq=f"D=\\mathbb{{R}}\\backslash\\{{ k{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq2=f"D=\\mathbb{{R}}\\backslash\\{{ k2{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq3=f"D=\\mathbb{{R}}\\backslash\\{{{latex(pi/2)}+ k2{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq4=f"D=\\mathbb{{R}}\\backslash\\{{{latex(pi/2)}+ k{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
    else:
        f=(a*sin(x)+b)/cos(x)
        kq=f"D=\\mathbb{{R}}\\backslash\\{{{latex(pi/2)}+ k{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq2=f"D=\\mathbb{{R}}\\backslash\\{{ k2{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq3=f"D=\\mathbb{{R}}\\backslash\\{{{latex(pi/2)}+ k2{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq4=f"D=\\mathbb{{R}}\\backslash\\{{ k{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
    ham_so=latex(f).replace("\\left("," ")
    ham_so=ham_so.replace("\\right)","")
    pa_A=f"*${kq}$"
    pa_B=f"${kq2}$"
    pa_C=f"${kq3}$"
    pa_D=f"${kq4}$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm tập xác định của hàm số $y={ham_so}$."

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

    #[D11_C1_B4_02]. Tìm tập xác định hàm số y=a/sinkx hoặc y=a/coskx

def ngh_kjg_L11_C1_B4_02():
    x=sp.symbols("x")
    a = random.randint(1,10)
    b = random.choice([-5,5])
    m= random.randint(2,10)
    mau = random.choice(["sin", "cos"])
    if mau == "sin":
        f=(a*cos(x)+b)/sin(m*x)
        kq=f"D=\\mathbb{{R}}\\backslash\\{{\\frac{{k\\pi}}{{{m}}},k\\in \\mathbb{{Z}} \\}}"
        kq2=f"D=\\mathbb{{R}}\\backslash\\{{ k\\pi,k\\in \\mathbb{{Z}} \\}}"
        kq3=f"D=\\mathbb{{R}}\\backslash\\{{{latex(my_module.hien_phan_so(1/(2*m)))}\\pi+ k{latex(pi/m)},k\\in \\mathbb{{Z}} \\}}"
        kq4=f"D=\\mathbb{{R}}\\backslash\\{{{latex(pi/2)}+ k{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
    else:
        f=(a*sin(x)+b)/cos(m*x)
        kq=f"D=\\mathbb{{R}}\\backslash\\{{{latex(my_module.hien_phan_so(1/(2*m)))}\\pi+ k{latex(pi/m)},k\\in \\mathbb{{Z}} \\}}"
        kq2=f"D=\\mathbb{{R}}\\backslash\\{{ k{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq3=f"D=\\mathbb{{R}}\\backslash\\{{{latex(pi/2)}+ k{latex(pi)},k\\in \\mathbb{{Z}} \\}}"
        kq4=f"D=\\mathbb{{R}}\\backslash\\{{\\frac{{k\\pi}}{{{m}}},k\\in \\mathbb{{Z}} \\}}"
    ham_so=latex(f).replace("\\left("," ")
    ham_so=ham_so.replace("\\right)","")
    pa_A=f"*${kq}$"
    pa_B=f"${kq2}$"
    pa_C=f"${kq3}$"
    pa_D=f"${kq4}$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm tập xác định của hàm số $y={ham_so}$."

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

#[D11_C1_B4_03]. Tìm tập xác định hàm số y=tan(ax+bpi)
def ngh_kjg_L11_C1_B4_03():
    a = random.randint(1,10)
    b = random.choice([-5,5])  
    dau=""
    if b>0: dau="+"
    x=latex(Rational((1-2*b)/(2*a)).limit_denominator(100))
    x2=latex(Rational((1-2*b)/(a)).limit_denominator(100))
    x3=latex(Rational((1-b)/(a)).limit_denominator(100))
    x4=latex(Rational((1-b)/(2*a)).limit_denominator(100))
    #Tìm công thức nghiệm và nghiệm ảo  
    kq=f"D=\\mathbb{{R}}\\backslash\\{{ {x}\\pi + k {latex(Rational(1/a).limit_denominator(100))}\\pi\\}}"
    kq2=f"D=\\mathbb{{R}}\\backslash\\{{ {x2}\\pi + k {latex(Rational(1/a).limit_denominator(100))}\\pi\\}}"
    kq3=f"D=\\mathbb{{R}}\\backslash\\{{ {x3}\\pi + k {latex(Rational(1/a).limit_denominator(100))}\\pi\\}}"
    kq4=f"D=\\mathbb{{R}}\\backslash\\{{ {x4}\\pi + k {latex(Rational(1/a).limit_denominator(100))}\\pi\\}}"
    #Tạo các phương án
    pa_A=f"*${kq}$"
    pa_B=f"${kq2}$"
    pa_C=f"${kq3}$"
    pa_D=f"${kq4}$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm tập xác định của hàm số $y=\\tan({a}x{dau}{b}\\pi)$."
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

#[D11_C1_B4_04]. Tìm GTLN,GTNN của hàm số sin, cos
def ngh_kjg_L11_C1_B4_04():
    a = random.randint(-10,10)
    b = random.choice([-10,10])
    m = random.choice([2,5])
    dau=""
    if b>0: 
        dau="+"
    ham = random.choice (["\\sin", "\\cos"])
    gt= random.choice(["giá trị lớn nhất","giá trị nhỏ nhất"]) 
    #Tìm công thức nghiệm và nghiệm ảo  
    if gt == "giá trị lớn nhất": 
        kq=max([a+b,-a+b])
        kq2=min([a+b,-a+b])
    if gt == "giá trị nhỏ nhất": 
        kq=min([a+b,-a+b])
        kq2=max([a+b,-a+b])
    kq3=random.randint(abs(a),20)
    kq4=random.randint(-20, abs(b))
    
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]
    #Tạo các phương án
    pa_A=f"*${{{kq}}}$"
    pa_B=f"${{{kq2}}}$"
    pa_C=f"${{{kq3}}}$"
    pa_D=f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Tìm {gt} của hàm số ${{y={a}{ham}{m}x {dau}{b}}}$. "
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

#[D11_C1_B4_05]-TF-M2. Cho hàm số y=acos(mx+n)+b. Xét Đ-S: TXĐ, GTLN, GTNN, TGT
def ngh_kjg_L11_C1_B4_05():
    x=sp.symbols("x")
    a= random.choice([i for i in range(-8, 8) if i!=0])
    b= random.choice([i for i in range(-8, 8) if i!=0])
    m= random.choice([i for i in range(-4, 4) if i!=0])

    k=random.choice([i for i in range(-10, 10) if i!=0])
    goc=[(k*pi)/i for i in range(1, 10)]
    n=random.choice(goc)
    chon=random.randint(1,2)
    if chon==1:
        f=a*sin(m*x+n)+b    
    if chon==2:
        f=a*cos(m*x+n)+b   

    noi_dung = f"Cho hàm số $y={latex(f)}$ . Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* Hàm số có tập xác định là $D=\\mathbb{{R}}$" 
    kq1_F=random.choice([f"Hàm số có tập xác định là $D=[{random.randint(-10,-1)};{random.randint(1,10)}]$ ",
        f"Hàm số có tập xác định là $D=\\mathbb{{R}}\\backslash \\{{{latex(n)}\\}}$"])

    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Hàm số có tập xác định là $D=\\mathbb{{R}}$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    t_min=min(a+b,-a+b)
    t_max=max(a+b,-a+b)
    kq2_T=f"* Giá trị lớn nhất của hàm số bằng ${{{t_max}}}$"
    kq2_F=f"Giá trị lớn nhất của hàm số bằng ${{{t_max+random.randint(1,5)}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    if chon==1:
        HDG=f"$-1\\le {latex(sin(m*x+n))} \\le 1 \\Rightarrow {-(abs(a))} \\le {latex(a*sin(m*x+n))} \\le {(abs(a))} $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị lớn nhất của hàm số bằng ${{{t_max}}}$"
    if chon==2:
        HDG=f"$-1\\le {latex(cos(m*x+n))} \\le 1 \\Rightarrow {-(abs(a))} \\le {latex(a*cos(m*x+n))} \\le {(abs(a))} $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị lớn nhất của hàm số bằng ${{{t_max}}}$"

    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Giá trị nhỏ nhất của hàm số bằng ${{{t_min}}}$" 
    kq3_F=f"Giá trị nhỏ nhất của hàm số bằng ${{{t_min-random.randint(1,5)}}}$"
    kq3=random.choice([kq3_T, kq3_F])
    if chon==1:
        HDG=f"$-1\\le {latex(sin(m*x+n))} \\le 1 \\Rightarrow {-(abs(a))} \\le {latex(a*sin(m*x+n))} \\le {(abs(a))} $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị nhỏ nhất của hàm số bằng ${{{t_min}}}$"
    if chon==2:
        HDG=f"$-1\\le {latex(cos(m*x+n))} \\le 1 \\Rightarrow {-(abs(a))} \\le {latex(a*cos(m*x+n))} \\le {(abs(a))} $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị nhỏ nhất của hàm số bằng ${{{t_min}}}$"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Tập giá trị của hàm số là $T=[{t_min};{t_max}]$"
    kq4_F=f"Tập giá trị của hàm số là $T=[{t_min-random.randint(1,3)};{t_max+random.randint(1,3)}]$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"Vì $ {t_min}\\le {latex(f)} \\le {t_max}$ nên tập giá trị của hàm số là $T=[{t_min};{t_max}]$."
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

#[D11_C1_B4_06]-TF-M2. Cho hàm số y=acos^2(mx+n)+b. Xét Đ-S: TXĐ, GTLN, GTNN, TGT
def ngh_kjg_L11_C1_B4_06():
    x=sp.symbols("x")
    a= random.choice([i for i in range(-8, 8) if i!=0 and i!=1])
    b= random.choice([i for i in range(-8, 8) if i!=0])
    m= random.choice([i for i in range(-4, 4) if i!=0])

    k=random.choice([i for i in range(-10, 10) if i!=0])
    goc=[(k*pi)/i for i in range(1, 10)]
    n=random.choice(goc)
    chon=random.randint(1,2)
    if chon==1:
        f=a*sin(m*x+n)**2+b    
    if chon==2:
        f=a*cos(m*x+n)**2+b   

    noi_dung = f"Cho hàm số $y={latex(f)}$ . Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"* Hàm số có tập xác định là $D=\\mathbb{{R}}$" 
    kq1_F=random.choice([f"Hàm số có tập xác định là $D=[{random.randint(-10,-1)};{random.randint(1,10)}]$ ",
        f"Hàm số có tập xác định là $D=\\mathbb{{R}}\\backslash \\{{{latex(n)}\\}}$"])

    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Hàm số có tập xác định là $D=\\mathbb{{R}}$"
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    t_min=min(b,a+b)
    t_max=max(b,a+b)
    kq2_T=f"* Giá trị lớn nhất của hàm số bằng ${{{t_max}}}$"
    kq2_F=f"Giá trị lớn nhất của hàm số bằng ${{{t_max+random.randint(1,5)}}}$"
    kq2=random.choice([kq2_T, kq2_F])
    if chon==1:
        HDG=f"$0\\le {latex(sin(m*x+n)**2)} \\le 1 $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị lớn nhất của hàm số bằng ${{{t_max}}}$"
    if chon==2:
        HDG=f"$0\\le {latex(cos(m*x+n)**2)} \\le 1 $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị lớn nhất của hàm số bằng ${{{t_max}}}$"

    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Giá trị nhỏ nhất của hàm số bằng ${{{t_min}}}$" 
    kq3_F=f" Giá trị nhỏ nhất của hàm số bằng ${{{t_min-random.randint(1,5)}}}$"
    kq3=random.choice([kq3_T, kq3_F])
    if chon==1:
        HDG=f"$0\\le {latex(sin(m*x+n)**2)} \\le 1 $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị nhỏ nhất của hàm số bằng ${{{t_min}}}$"
    if chon==2:
        HDG=f"$0\\le {latex(cos(m*x+n)**2)} \\le 1$"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy giá trị nhỏ nhất của hàm số bằng ${{{t_min}}}$"
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* Tập giá trị của hàm số là $T=[{t_min};{t_max}]$"
    kq4_F=f"Tập giá trị của hàm số là $T=[{t_min-random.randint(1,3)};{t_max+random.randint(1,3)}]$" 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"Vì $ {t_min}\\le {latex(f)} \\le {t_max}$ nên tập giá trị của hàm số là $T=[{t_min};{t_max}]$."
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

#[D11_C1_B4_07]-TF-M2. Cho y=acosmx+b hoặc y=asinmx+b. Xét Đ-S: TXĐ, Chẵn-Lẻ, TGT, Cắt trục Oy
def ngh_kjg_L11_C1_B4_07():
    
    x=sp.symbols("x")
    a= random.choice([i for i in range(-8, 8) if i!=0])
    b= random.choice([i for i in range(-8, 8) if i!=0])
    m= random.choice([i for i in range(-10, 10) if i!=0])
    
    chon=random.randint(1,2)

    if chon==1:
        f=a*cos(m*x)+b

        noi_dung = f"Cho hàm số $y={latex(f)}$ . Xét tính đúng-sai của các khẳng định sau. "        
        debai_word= f"{noi_dung}\n"
        
        kq1_T=f"* Tập xác định của hàm số là $D=\\mathbb{{R}}$" 
        kq1_F=f"Tập xác định của hàm số là $D=[{-abs(a)};{abs(a)}]$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Tập xác định của hàm số là $D=\\mathbb{{R}}$."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq2_T=f"* Hàm số đã cho là hàm số chẵn"
        kq2_F=f"Hàm số đã cho là hàm số lẻ"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Ta có: Với mọi $x\\in \\mathbb{{R}}$ thì $-x\\in \\mathbb{{R}}$.\n\n"\
        f"$f(-x)={latex(a*cos(m*(-x))+b)}={latex(f)}$. Vậy hàm số $y={latex(f)}$ là hàm số chẵn."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        t_min=min(a+b,-a+b)
        t_max=max(a+b,-a+b)

        kq3_T=f"* Tập giá trị của hàm số đã cho là $T={{[{t_min};{t_max}]}}$" 
        kq3_F=f"Tập giá trị của hàm số đã cho là $T={{[{t_min-random.randint(1,5)};{t_max+random.randint(1,5)}]}}$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Ta có: ${t_min} \\le {latex(f)} \\le {t_max}$ nên tập giá trị là ${{[{t_min};{t_max}]}}$"
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"* Đồ thị cắt trục tung tại điểm có tung độ bằng ${{{a+b}}}$"
        kq4_F=f" Đồ thị cắt trục tung tại điểm có tung độ bằng ${{{a+b+ random.randint(1,3)}}}$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Cho $x=0\\Rightarrow y={a+b}$. Suy ra đồ thị cắt trục tung tại điểm có tung độ bằng ${{{a+b}}}$."
        loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq4==kq4_F:
            loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if chon==2:
        f=a*sin(m*x)+b

        noi_dung = f"Cho hàm số $y={latex(f)}$ . Xét tính đúng-sai của các khẳng định sau. "        
        debai_word= f"{noi_dung}\n"
        
        kq1_T=f"* Tập xác định của hàm số là $D=\\mathbb{{R}}$" 
        kq1_F=f"Tập xác định của hàm số là $D=[{-abs(a)};{abs(a)}]$"
        kq1=random.choice([kq1_T, kq1_F])
        HDG=f"Tập xác định của hàm số là $D=\\mathbb{{R}}$."
        loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq1==kq1_F:
            loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq2_T=f"* Hàm số đã cho là hàm số không chẵn, không lẻ"
        kq2_F=f"Hàm số đã cho là hàm số {random.choice(["lẻ", "chẵn"])}"
        kq2=random.choice([kq2_T, kq2_F])
        HDG=f"Ta có: Với mọi $x\\in \\mathbb{{R}}$ thì $-x\\in \\mathbb{{R}}$.\n\n"\
        f"$f(-x)={latex(a*sin(m*(-x))+b)}\\ne f(x), f(-x)\\ne -f(x)$.\n\n"\
        f"Vậy hàm số $y={latex(f)}$ là hàm số không chẵn, không lẻ."
        loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq2==kq2_F:
            loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        t_min=min(a+b,-a+b)
        t_max=max(a+b,-a+b)

        kq3_T=f"* Tập giá trị của hàm số đã cho là $T={{[{t_min};{t_max}]}}$" 
        kq3_F=f"Tập giá trị của hàm số đã cho là $T={{[{t_min-random.randint(1,5)};{t_max+random.randint(1,5)}]}}$"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"Ta có: ${t_min} \\le {latex(f)} \\le {t_max}$ nên tập giá trị là ${{[{t_min};{t_max}]}}$"
        loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
        if kq3==kq3_F:
            loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

        kq4_T=f"* Đồ thị cắt trục tung tại điểm có tung độ bằng ${{{b}}}$"
        kq4_F=f" Đồ thị cắt trục tung tại điểm có tung độ bằng ${{{b+ random.randint(1,5)}}}$" 
        kq4=random.choice([kq4_T, kq4_F])
        HDG=f"Cho $x=0\\Rightarrow y={b}$. Suy ra đồ thị cắt trục tung tại điểm có tung độ bằng ${{{b}}}$."
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

#[D11_C1_B4_08]-TF-M2. Tìm tập giá trị của HSLG
def ngh_kjg_L11_C1_B4_08():
    x=sp.symbols("x")
    a= random.choice([i for i in range(-8, 8) if i!=0])
    b= random.choice([i for i in range(-8, 8) if i!=0])
    m= random.choice([i for i in range(-10, 10) if i!=0])
    k=random.choice([i for i in range(-10, 10) if i!=0])
    goc=[(k*pi)/i for i in range(1, 10)]
    n=random.choice(goc)
    t_min=min(a+b,-a+b)
    t_max=max(a+b,-a+b)
    chon=random.randint(1,2)
    if chon==1:
        f=a*sin(m*x+n)+b
        noi_dung_loigiai=f"$-1\\le {latex(sin(m*x+n))} \\le 1 \\Rightarrow {-(abs(a))} \\le {latex(a*sin(m*x+n))} \\le {(abs(a))} $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
         f"Vậy tập giá trị của hàm số là $T=[{t_min};{t_max}]$."
    if chon==2:
        f=a*cos(m*x+n)+b
        noi_dung_loigiai=f"$-1\\le {latex(cos(m*x+n))} \\le 1 \\Rightarrow {-(abs(a))} \\le {latex(a*cos(m*x+n))} \\le {(abs(a))} $"\
        f"$\\Rightarrow {t_min}\\le {latex(f)} \\le {t_max}$.\n\n"\
        f"Vậy tập giá trị của hàm số là $T=[{t_min};{t_max}]$."
    
    noi_dung=f"Tập giá trị của hàm số $y={latex(f)}$ là"

    kq=f"$[{t_min};{t_max}]$"
    kq2=f"$[{t_min-random.randint(1,3)};{t_max}]$"
    kq3=f"$[{t_min};{t_max+random.randint(1,3)}]$"
    kq4=f"$[{t_min-random.randint(1,3)};{t_max+random.randint(1,3)}]$"    

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

#[D11_C1_B4_09]-TF-M2. Tìm chu kì tuần hoàn của HSLG
def ngh_kjg_L11_C1_B4_09():
    x=sp.symbols("x")
    a= random.choice([i for i in range(-10, 10) if i!=0])
    b= random.choice([i for i in range(-8, 8) if i!=0])
    m= random.choice([i for i in range(2, 10) if i!=0])
    k=random.choice([i for i in range(-10, 10) if i!=0])
    goc=[(k*pi)/i for i in range(1, 10)]
    n=random.choice(goc)
    chon=random.randint(1,2)
    if chon==1:
        chon=random.randint(1,2)
        if chon==1:
            f=a*sin(m*x+n)    
        if chon==2:
            f=a*cos(m*x+n)    
        noi_dung=f"Hàm số $y={latex(f)}$ có chu kỳ tuần hoàn là"
        noi_dung_loigiai=f"Hàm số đã cho có chu kỳ tuần hoàn là: $T=\\dfrac{{2\\pi }}{{|{m}|}}={latex(2*pi/(abs(m)))}$."

        kq=f"{latex(2*pi/(abs(m)))}"
        kq2=f"{latex(pi/(abs(m)))}"
        kq3=f"{latex(2*pi*(abs(m)))}"
        kq4=f"{latex(pi*(abs(m)))}"
    
    if chon==2:
        chon=random.randint(1,2)
        if chon==1:
            f=a*tan(m*x+n)    
        if chon==2:
            f=a*cot(m*x+n)    
        noi_dung=f"Hàm số $y={latex(f)}$ có chu kỳ tuần hoàn là"
        noi_dung_loigiai=f"Hàm số đã cho có chu kỳ tuần hoàn là: $T=\\dfrac{{\\pi }}{{|{m}|}}={latex(pi/(abs(m)))}$."

        kq=f"{latex(pi/(abs(m)))}"
        kq2=f"{latex(2*pi/(abs(m)))}"
        kq3=f"{latex(2*pi*(abs(m)))}"
        kq4=f"{latex(pi*(abs(m)))}"
    
    

    

    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"
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


################  Bài 5: Phương trình lượng giác.################
#[D11_C1_B5_01]. Giải phương trình cos(ax) = b
def ngh_kjg_L11_C1_B5_01():
    m = random.randint(2,10)
    b = random.choice([-sqrt(2),-sqrt(3),sqrt(2),sqrt(3)])
    dau =""
    if b > 0: dau = "+"

    #Tìm công thức nghiệm và nghiệm ảo
    x=acos(-b/2)
    x1=f"{latex(x/m)} + k{latex(2*pi/m)}"
    x2=f"{latex(-x/m)} + k{latex(2*pi/m)}"
    #nghiệm ảo
    x3=f"{latex(x)} + k{latex(pi)}"
    x4=f"{latex(-x)} + k{latex(pi)}"
    #Giả làm nghiệm của sin
    x5=f"{latex((asin(-b/2)/m))} + k{latex(pi)}"
    x6=f"{latex(-(asin(-b/2)/m))} + k{latex(pi)}"
    #Tạo các phương án
    pa_A=f"*$x={x1}, x={x2}(k \\in \\mathbb{{Z}})$"
    pa_B=f"$x={x3}, x={x4}(k \\in \\mathbb{{Z}})$"
    pa_C=f"$x={x1}, x={x5}(k \\in \\mathbb{{Z}})$"
    pa_D=f"$x={x5}, x={x6}(k \\in \\mathbb{{Z}})$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Giải phương trình $2\\cos{m}x {dau}{latex(b)}=0$. "

    noi_dung_loigiai=f""
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)


    debai= f"{noi_dung}\n"      
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D11_C1_B5_02]. Giải phương trình sin(mx) = b
def ngh_kjg_L11_C1_B5_02():
    m = random.randint(2,10)
    b = random.choice([-sqrt(2)/2,-sqrt(3)/2,sqrt(2)/2,sqrt(3)/2])
    dau =""
    if b > 0: dau = "+"

    #Tìm công thức nghiệm và nghiệm ảo
    x=asin(b)
    x1=f"{latex(x/m)} + k{latex(2*pi/m)}"
    x2=f"{latex((pi-x)/m)} + k{latex(2*pi/m)}"
    #nghiệm ảo
    x3=f"{latex(x)} + k{latex(pi)}"
    x4=f"{latex(pi-x)} + k{latex(pi)}"
    #Giả làm nghiệm của sin
    x5=f"{latex((acos(-b)/m))} + k{latex(2*pi)}"
    x6=f"{latex(-(acos(-b)/m))} + k{latex(2*pi)}"
    #Tạo các phương án
    pa_A=f"*$x={x1}, x={x2}(k \\in \\mathbb{{Z}})$"
    pa_B=f"$x={x3}, x={x4}(k \\in \\mathbb{{Z}})$"
    pa_C=f"$x={x4}, x={x5}(k \\in \\mathbb{{Z}})$"
    pa_D=f"$x={x5}, x={x6}(k \\in \\mathbb{{Z}})$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Giải phương trình $\\sin{m}x={latex(b)}$."

    noi_dung_loigiai=f""
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)


    debai= f"{noi_dung}\n"      
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D11_C1_B5_03]. Giải phương trình tan cơ bản
def ngh_kjg_L11_C1_B5_03():
    m = random.randint(1,10)    
    b = random.choice([-1,1,sqrt(3),sqrt(3)/3])
    if m==1:
        x= atan(b)
        x1=f"{latex(x)} + k{latex(pi)}"
        x2=f"{latex(x)} + k2{latex(pi)}"
        x3=f"{latex(abs(x))} + k\\frac{{\\pi}}{{2}}"
        x4=f"\\pm{latex(abs(x))} + k{latex(pi)}"

    else:
        x= atan(b)/pi/m
        x1=f"{latex(x)}\\pi + k{latex(pi/m)}"     
        x2=f"{latex(x)}\\pi + k{latex(pi)}"
        x3=f"{latex(atan(b))} + k{latex(pi)}"
        x4=f"\\pm{latex(abs(x))}\\pi + k{latex(pi/m)}"


    #Tạo các phương án
    pa_A=f"*$x={x1}$,$k \\in \\mathbb{{Z}}$"
    pa_B=f"$x={x2}$,$k \\in \\mathbb{{Z}}$"
    pa_C=f"$x={x3}$,$k \\in \\mathbb{{Z}}$"
    pa_D=f"$x={x4}$, $k \\in \\mathbb{{Z}}$"

    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Giải phương trình $\\tan{m}x ={latex(b)}$."
    noi_dung_loigiai=f""
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)


    debai= f"{noi_dung}\n"      
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D11_C1_B5_04]. Tìm m để phương trình sin, cos có nghiệm.
def ngh_kjg_L11_C1_B5_04():
    x,m=sp.symbols("x m")
    t = random.randint(1,10)
    a = random.randint(1,10)
    b = random.choice([i for i in range(-5, 6) if i!=0])
    k = random.randint(1,5)

    chon=random.randint(1,2)
    if chon==1:
        f=a*sin(t*x) -k*m+b
        noi_dung= f"Tìm các giá trị của tham số $m$ để phương trình ${latex(a*sin(t*x))}+{latex(-k*m+b)}=0$ có nghiệm.".replace("\\left(","").replace("\\right)","")
        
        noi_dung_loigiai=(f"${latex(a*sin(t*x))}+{latex(-k*m+b)}=0 \\Rightarrow {latex(sin(t*x))}=\\dfrac{{{latex(k*m-b)} }}{{{a}}}$ có nghiệm khi"
            f"$-1\\le \\dfrac{{{latex(k*m-b)} }}{{{a}}} \\le 1 $\n\n"
            f"$\\Rightarrow {-a} \\le {latex(k*m-b)} \\le {a}"
            f"\\Rightarrow {phan_so((-a+b)/k)} \\le m \\le {phan_so((a+b)/k)}$."
            )
    if chon==2:
        f=a*cos(t*x) -k*m+b
        noi_dung= f"Tìm các giá trị của tham số $m$ để phương trình ${latex(a*cos(t*x))}+{latex(-k*m+b)}=0$ có nghiệm.".replace("\\left(","").replace("\\right)","")
        noi_dung_loigiai=(f"${latex(a*sin(t*x))}+{latex(-k*m+b)}=0 \\Rightarrow {latex(cos(t*x))}=\\dfrac{{{latex(k*m-b)} }}{{{a}}}$ có nghiệm khi"
            f"$-1\\le \\dfrac{{{latex(k*m-b)} }}{{{a}}}\\le 1 $\n\n"
            f"$\\Rightarrow {-a} \\le {latex(k*m-b)} \\le {a}"
            f"\\Rightarrow {phan_so((-a+b)/k)} \\le m \\le {phan_so((a+b)/k)}$."
            )
    noi_dung=noi_dung.replace("+-","-")
    noi_dung_loigiai=noi_dung_loigiai.replace("\\left(","").replace("\\right)","").replace("+-","-")


    #Tạo các phương án
    pa_A=f"*${latex(Rational((-a+b)/k).limit_denominator(100))} \\le m \\le {latex(Rational((a+b)/k).limit_denominator(100))}$"
    pa_B=f"${latex(Rational(a/k).limit_denominator(100))} \\le m \\le {latex(Rational(b/k).limit_denominator(100))}$"
    pa_C=f"${latex(-a+b)} \\le m \\le {latex(a+b)}$"
    pa_D=f"${latex(a-b)} \\le m \\le {latex(a+b)}$"

   
    
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

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C1_B5_05]. Giải phương trình cosx = b
def ngh_kjg_L11_C1_B5_05():
    m = 1
    b = random.choice([-sqrt(2),-sqrt(3),sqrt(2),sqrt(3)])
    
    dau =""
    if b > 0: dau = "+"

    #Tìm công thức nghiệm và nghiệm ảo
    # x=acos(b/2)/pi
    # x1=f"{latex(x)}\\pi + k{latex(2*pi)}"
    # x2=f"{latex(-x)}\\pi + k{latex(2*pi)}"

    x=acos(b/2)
    x1=f"{latex(x)} + k{latex(2*pi)}"
    x2=f"{latex(-x)} + k{latex(2*pi)}"
    #nghiệm ảo
    x3=f"{latex(x)} + k{latex(pi)}"
    x4=f"{latex(-x)} + k{latex(pi)}"
    #Giả làm nghiệm của sin
    x5=f"{latex((asin(-b/2)))} + k{latex(2*pi)}"
    x6=f"{latex(-(asin(-b/2)))} + k{latex(2*pi)}"

    if b==sqrt(2):
        x3=f"{latex(2*pi/3)} + k2{latex(pi)}"
        x4=f"{latex(-2*pi/3)} + k2{latex(pi)}"
        #Giả làm nghiệm của sin
        x5=f"{latex(3*pi/4)} + k2{latex(pi)}"
        x6=f"{latex(-3*pi/4)} + k2{latex(pi)}"

    #Tạo các phương án
    pa_A=f"*$x={x1}, x={x2}(k \\in \\mathbb{{Z}})$"
    pa_B=f"$x={x3}, x={x4}(k \\in \\mathbb{{Z}})$"
    pa_C=f"$x={x1}, x={x5}(k \\in \\mathbb{{Z}})$"
    pa_D=f"$x={x5}, x={x6}(k \\in \\mathbb{{Z}})$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Giải phương trình $\\cos x ={latex(b/2)}$."

    noi_dung_loigiai=f""
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)


    debai= f"{noi_dung}\n"      
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D11_C1_B5_06]-M2. Giải phương trình sin(x) = b
def ngh_kjg_L11_C1_B5_06():

    b = random.choice([-sqrt(2)/2,-sqrt(3)/2,sqrt(2)/2,sqrt(3)/2])
    dau =""
    if b > 0: dau = "+"

    #Tìm công thức nghiệm và nghiệm ảo
    x=asin(b)/pi
    x1=f"{latex(x)}\\pi + k{latex(2*pi)}"
    x2=f"{latex(1-x)}\\pi + k{latex(2*pi)}"
    #nghiệm ảo
    x3=f"{latex(x)}\\pi + k{latex(pi)}"
    x4=f"{latex(1-x)}\\pi + k{latex(pi)}"
    #Giả làm nghiệm của sin
    x5=f"{latex((acos(-b)/pi))}\\pi + k{latex(2*pi)}"
    x6=f"{latex(-(acos(-b)/pi))}\\pi + k{latex(2*pi)}"
    #Tạo các phương án
    pa_A=f"*$x={x1}, x={x2}(k \\in \\mathbb{{Z}})$"
    pa_B=f"$x={x3}, x={x4}(k \\in \\mathbb{{Z}})$"
    pa_C=f"$x={x4}, x={x5}(k \\in \\mathbb{{Z}})$"
    pa_D=f"$x={x5}, x={x6}(k \\in \\mathbb{{Z}})$"
    #Trộn các phương án
    list_PA =[pa_A,pa_B,pa_C,pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    noi_dung= f"Giải phương trình $\\sin x={latex(b)}$. "
    noi_dung_loigiai=f""
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)


    debai= f"{noi_dung}\n"      
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D11_C1_B5_07]. Giải phương trình cot(ax)=b
def ngh_kjg_L11_C1_B5_07():
    x=sp.symbols("x")
    m = random.randint(1,10)    
    b = random.choice([-1,1,sqrt(3),sqrt(3)/3])    
    
    if 1/b==1:
        t=1
    elif 1/b==-1:
        t=-1
    else:
        t=latex(1/b)
    noi_dung= f"Giải phương trình $\\cot {latex(m*x)}={t}$."
    if m==1:
        x_0= atan(b)
        x1=f"{latex(x_0)} + k{latex(pi)}"
        x2=f"{latex(x_0)} + k2{latex(pi)}"
        x3=f"{latex(abs(x_0))} + k\\frac{{\\pi}}{{2}}"
        x4=f"\\pm{latex(abs(x_0))} + k{latex(pi)}"
        noi_dung_loigiai=f"$\\cot {latex(m*x)}={t} \\Leftrightarrow \\cot {latex(m*x)} =\\cot {latex(x_0)}$\n\n"\
    f"$\\Leftrightarrow {latex(m*x)}= {latex(x_0)}+k\\pi, k\\in \\mathbb{{Z}}$."

    else:
        x_0= atan(b)
        x1=f"{latex(x_0/m)} + k{latex(pi/m)}"     
        x2=f"{latex(x_0/m)} + k{latex(pi)}"
        x3=f"{latex(atan(b))} + k{latex(pi)}"
        x4=f"\\pm{latex(abs(x_0))}\\pi + k{latex(pi/m)}"
        noi_dung_loigiai=f"$\\cot {latex(m*x)}={t} \\Leftrightarrow \\cot {latex(m*x)} =\\cot {latex(x_0)}$\n\n"\
    f"$\\Leftrightarrow {latex(m*x)}= {latex(x_0)}+k\\pi \\Leftrightarrow x= {latex(x_0/m)} + k{latex(pi/m)}, k\\in \\mathbb{{Z}}$."

    #Tạo các phương án
    pa_A=f"*$x={x1}$,$k \\in \\mathbb{{Z}}$"
    pa_B=f"$x={x2}$,$k \\in \\mathbb{{Z}}$"
    pa_C=f"$x={x3}$,$k \\in \\mathbb{{Z}}$"
    pa_D=f"$x={x4}$, $k \\in \\mathbb{{Z}}$"

    
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
    dap_an=my_module.tra_ve_dap_an(list_PA)


    debai= f"{noi_dung}\n"      
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n" 

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

#[D11_C1_B5_08]-M3. Giải phương trình cos(ax+m)=cos(bx+n)
def ngh_kjg_L11_C1_B5_08():
    x,k=sp.symbols("x,k")
    b=random.randint(1,3)
    a=b+random.randint(1,3)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6])
    n=random.choice([-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4, ])
    noi_dung=f"Nghiệm của phương trình $\\cos\\left({latex(a*x+m)}\\right)=\\cos\\left({latex(b*x+n)}\\right)$ là"
    
    x_1, x_2=(n-m)/(a-b), (-n-m)/(a+b)
    x_3, x_4=(n+2*m)/(a+b), (m-n)/(a-b)
    kq=f"$x={latex(x_1)}+k{latex(2*pi/(a-b))}, x={latex(x_2)}+k{latex(2*pi/(a+b))} (k\\in \\mathbb{{Z}})$"
    kq2=f"$x={latex(x_1)}+k{latex(pi/(a+b))}, x={latex(x_2)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq3=f"$x={latex(x_3)}+k{latex(2*pi)}, x={latex(x_4)}+k{latex(2*pi)} (k\\in \\mathbb{{Z}})$"
    kq4=f"$x={latex(x_3)}+k{latex(2*pi/(a-b))}, x={latex(x_4)}+k{latex(2*pi/(a+b))} (k\\in \\mathbb{{Z}})$"

    noi_dung_loigiai=(f"$\\cos\\left({latex(a*x+m)}\\right)=\\cos\\left({latex(b*x+n)}\\right)"

        f"\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        {latex(a*x+m)}={latex(b*x+n)} +k{latex(2*pi)} \\\\ \n\
        {latex(a*x+m)}={latex(-b*x-n)}+k{latex(2*pi)}\n\
        \\end{{array}} \\right.$\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        {latex((a-b)*x)}={latex(n-m)} +k{latex(2*pi)} \\\\ \n\
        {latex((a+b)*x)}={latex(-n-m)}+k{latex(2*pi)}\n\
        \\end{{array}} \\right. $\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        x={latex(x_1)} + k{latex(2*pi/(a-b))} \\\\ \n\
        x={latex(x_2)}+ k{latex(2*pi/(a+b))}\n\
        \\end{{array}} \\right. , k\\in \\mathbb{{Z}} $\n\n"

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C1_B5_09]-M3. Giải phương trình cos(ax+m)=sin(bx+n)
def ngh_kjg_L11_C1_B5_09():
    x,k=sp.symbols("x,k")
    b=random.randint(1,3)
    a=b+random.randint(1,3)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6])
    n=random.choice([-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4, ])
    noi_dung=f"Nghiệm của phương trình $\\cos\\left({latex(a*x+m)}\\right)=\\sin\\left({latex(pi/2-b*x-n)}\\right)$ là"
    
    x_1, x_2=(n-m)/(a-b), (-n-m)/(a+b)
    x_3, x_4=(n+2*m)/(a+b), (m-n)/(a-b)
    kq=f"$x={latex(x_1)}+k{latex(2*pi/(a-b))}, x={latex(x_2)}+k{latex(2*pi/(a+b))} (k\\in \\mathbb{{Z}})$"
    kq2=f"$x={latex(x_1)}+k{latex(pi/(a+b))}, x={latex(x_2)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq3=f"$x={latex(x_3)}+k{latex(2*pi)}, x={latex(x_4)}+k{latex(2*pi)} (k\\in \\mathbb{{Z}})$"
    kq4=f"$x={latex(x_3)}+k{latex(2*pi/(a-b))}, x={latex(x_4)}+k{latex(2*pi/(a+b))} (k\\in \\mathbb{{Z}})$"

    noi_dung_loigiai=(
        f"$\\cos\\left({latex(a*x+m)}\\right)=\\sin\\left({latex(pi/2-b*x-n)}\\right) \\Leftrightarrow \\cos\\left({latex(a*x+m)}\\right)=\\cos\\left({latex(b*x+n)}\\right)$\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        {latex(a*x+m)}={latex(b*x+n)} +k{latex(2*pi)} \\\\ \n\
        {latex(a*x+m)}={latex(-b*x-n)}+k{latex(2*pi)}\n\
        \\end{{array}} \\right.$\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        {latex((a-b)*x)}={latex(n-m)} +k{latex(2*pi)} \\\\ \n\
        {latex((a+b)*x)}={latex(-n-m)}+k{latex(2*pi)}\n\
        \\end{{array}} \\right. $\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        x={latex(x_1)} + k{latex(2*pi/(a-b))} \\\\ \n\
        x={latex(x_2)}+ k{latex(2*pi/(a+b))}\n\
        \\end{{array}} \\right. , k\\in \\mathbb{{Z}} $\n\n"

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C1_B5_10]-M3. Giải phương trình sin(ax+m)=sin(bx+n)
def ngh_kjg_L11_C1_B5_10():
    x,k=sp.symbols("x,k")
    b=random.randint(1,3)
    a=b+random.randint(1,3)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6])
    n=random.choice([-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4, ])
    noi_dung=f"Nghiệm của phương trình $\\sin\\left({latex(a*x+m)}\\right)=\\sin\\left({latex(b*x+n)}\\right)$ là"
    
    x_1, x_2=(n-m)/(a-b), (pi-n-m)/(a+b)
    
    x_3, x_4=(n-m)/(a-b), (-n-m)/(a+b)
    kq=f"$x={latex(x_1)}+k{latex(2*pi/(a-b))}, x={latex(x_2)}+k{latex(2*pi/(a+b))} (k\\in \\mathbb{{Z}})$"
    kq2=f"$x={latex(x_1)}+k{latex(pi/(a+b))}, x={latex(x_2)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq3=f"$x={latex(x_3)}+k{latex(2*pi)}, x={latex(x_4)}+k{latex(2*pi)} (k\\in \\mathbb{{Z}})$"
    kq4=f"$x={latex(x_3)}+k{latex(2*pi/(a-b))}, x={latex(x_4)}+k{latex(2*pi/(a+b))} (k\\in \\mathbb{{Z}})$"

    noi_dung_loigiai=(
        f"$\\sin\\left({latex(a*x+m)}\\right)=\\sin \\left({latex(b*x+n)}\\right)"

        f"\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        {latex(a*x+m)}={latex(b*x+n)} +k{latex(2*pi)} \\\\ \n\
        {latex(a*x+m)}=\\pi-({latex(b*x+n)})+k{latex(2*pi)}\n\
        \\end{{array}} \\right.$\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        {latex(a*x+m)}={latex(b*x+n)} +k{latex(2*pi)} \\\\ \n\
        {latex(a*x+m)}={latex(pi-b*x-n)}+k{latex(2*pi)}\n\
        \\end{{array}} \\right.$\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        {latex((a-b)*x)}={latex(n-m)} +k{latex(2*pi)} \\\\ \n\
        {latex((a+b)*x)}={latex(pi-n-m)}+k{latex(2*pi)}\n\
        \\end{{array}} \\right. $\n\n"

        f"$\\Leftrightarrow \\left[ \\begin{{array}}{{l}} \n\
        x={latex(x_1)} + k{latex(2*pi/(a-b))} \\\\ \n\
        x={latex(x_2)}+ k{latex(2*pi/(a+b))}\n\
        \\end{{array}} \\right. , k\\in \\mathbb{{Z}} $\n\n"

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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C1_B5_11]-M2. Giải phương trình tan(ax+m)=tan(bx+n)
def ngh_kjg_L11_C1_B5_11():
    x,k=sp.symbols("x,k")
    b=random.randint(1,3)
    a=b+random.randint(1,3)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6])
    n=random.choice([-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4, ])
    noi_dung=f"Nghiệm của phương trình $\\tan\\left({latex(a*x+m)}\\right)=\\tan\\left({latex(b*x+n)}\\right)$ là"
    
    x_1=(n-m)/(a-b)
    x_2 = random.choice([(m-n)/(a-b), (-n-m)/(a+b), (n-m)/(a+b), (m-n)/(a+b)])
    kq=f"$x={latex(x_1)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq2=f"$x={latex(x_1)}+k{latex(2*pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq3=f"$x={latex(x_2)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq4=f"$x={latex(x_2)}+k{latex(2*pi/(a-b))}, (k\\in \\mathbb{{Z}})$"

    noi_dung_loigiai=(f"$\\tan \\left({latex(a*x+m)}\\right)=\\tan\\left({latex(b*x+n)}\\right)$"

        f"$\\Leftrightarrow {latex(a*x+m)}={latex(b*x+n)} +k{latex(2*pi)}$\n\n"

        f"$\\Leftrightarrow  {latex((a-b)*x)}={latex(n-m)} +k{latex(2*pi)}$ "

        f"$\\Leftrightarrow x={latex(x_1)} + k{latex(2*pi/(a-b))}, k\\in \\mathbb{{Z}} $\n\n"
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C1_B5_12]-M2. Giải phương trình cot(ax+m)=cot(bx+n)
def ngh_kjg_L11_C1_B5_12():
    x,k=sp.symbols("x,k")
    b=random.randint(1,3)
    a=b+random.randint(1,3)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6])
    n=random.choice([-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4, ])
    noi_dung=f"Nghiệm của phương trình $\\cot\\left({latex(a*x+m)}\\right)=\\cot\\left({latex(b*x+n)}\\right)$ là"
    
    x_1=(n-m)/(a-b)
    x_2 = random.choice([(m-n)/(a-b), (-n-m)/(a+b), (n-m)/(a+b), (m-n)/(a+b)])
    kq=f"$x={latex(x_1)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq2=f"$x={latex(x_1)}+k{latex(2*pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq3=f"$x={latex(x_2)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq4=f"$x={latex(x_2)}+k{latex(2*pi/(a-b))}, (k\\in \\mathbb{{Z}})$"

    noi_dung_loigiai=(f"$\\cot \\left({latex(a*x+m)}\\right)=\\cot\\left({latex(b*x+n)}\\right)$"

        f"$\\Leftrightarrow {latex(a*x+m)}={latex(b*x+n)} +k{latex(2*pi)}$\n\n"

        f"$\\Leftrightarrow  {latex((a-b)*x)}={latex(n-m)} +k{latex(2*pi)}$ "

        f"$\\Leftrightarrow x={latex(x_1)} + k{latex(2*pi/(a-b))}, k\\in \\mathbb{{Z}} $\n\n"
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C1_B5_12]-M2. Giải phương trình tan(ax+m)=cot(bx+n)
def ngh_kjg_L11_C1_B5_12():
    x,k=sp.symbols("x,k")
    b=random.randint(1,3)
    a=b+random.randint(1,3)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6])
    n=random.choice([-pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4, ])
    noi_dung=f"Nghiệm của phương trình $\\tan\\left({latex(a*x+m)}\\right)=\\cot\\left({latex(pi/2-b*x-n)}\\right)$ là"
    
    x_1=(n-m)/(a-b)
    x_2 = random.choice([(m-n)/(a-b), (-n-m)/(a+b), (n-m)/(a+b), (m-n)/(a+b)])
    kq=f"$x={latex(x_1)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq2=f"$x={latex(x_1)}+k{latex(2*pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq3=f"$x={latex(x_2)}+k{latex(pi/(a-b))} (k\\in \\mathbb{{Z}})$"
    kq4=f"$x={latex(x_2)}+k{latex(2*pi/(a-b))}, (k\\in \\mathbb{{Z}})$"

    noi_dung_loigiai=(f"$\\tan\\left({latex(a*x+m)}\\right)=\\cot\\left({latex(pi/2-b*x-n)}\\right)$"
        f"$\\Leftrightarrow \\tan\\left({latex(a*x+m)}\\right)=\\tan\\left({latex(pi/2)}-({latex(pi/2-b*x-n)})\\right)$\n\n"
        f"$\\Leftrightarrow \\tan \\left({latex(a*x+m)}\\right)=\\tan\\left({latex(b*x+n)}\\right)$"
        f"$\\Leftrightarrow {latex(a*x+m)}={latex(b*x+n)} +k{latex(2*pi)}$\n\n"

        f"$\\Leftrightarrow  {latex((a-b)*x)}={latex(n-m)} +k{latex(2*pi)}$ "

        f"$\\Leftrightarrow x={latex(x_1)} + k{latex(2*pi/(a-b))}, k\\in \\mathbb{{Z}} $\n\n"
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

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C1_B5_13]-M2. Tìm số nghiệm thuộc khoảng đoạn của sinu=m
def ngh_kjg_L11_C1_B5_13():
    x=sp.symbols("x")    
    a=random.randint(1,4)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6, -pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4])    
    b=random.randint(1,10)
    chon=random.randint(1,6)
    
    if chon==1:
        noi_dung = f"Số nghiệm thuộc đoạn $[{latex(-b*pi)};{latex(b*pi)}]$ của phương trình $\\sin \\left({latex(a*x+m)}\\right)=0$ là"

        eq=Eq(-m/a+x*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<=i and i<=x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\sin \\left({latex(a*x+m)}\\right)=0 \\Leftrightarrow {latex(a*x+m)} = k\\pi \\Leftrightarrow x={latex(-m/a)}+k{latex(pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in [{latex(-b*pi)};{latex(b*pi)}]$ nên ${latex(-b*pi)}\\le {latex(-m/a)}+k{latex(pi/a)} \\le {latex(b*pi)} \\Rightarrow {latex(x_1)}\\le k \\le {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )
    
    if chon==2:
        noi_dung = f"Số nghiệm thuộc khoảng $({latex(-b*pi)};{latex(b*pi)})$ của phương trình $\\sin \\left({latex(a*x+m)}\\right)=0$ là"

        eq=Eq(-m/a+x*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<i and i<x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\sin \\left({latex(a*x+m)}\\right)=0 \\Leftrightarrow {latex(a*x+m)} = k\\pi \\Leftrightarrow x={latex(-m/a)}+k{latex(pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in ({latex(-b*pi)};{latex(b*pi)})$ nên ${latex(-b*pi)}< {latex(-m/a)}+k{latex(pi/a)}< {latex(b*pi)} \\Rightarrow {latex(x_1)}< k <{latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==3:
        noi_dung = f"Số nghiệm thuộc đoạn $[{latex(-b*pi)};{latex(b*pi)}]$ của phương trình $\\sin \\left({latex(a*x+m)}\\right)=1$ là"

        eq=Eq(-m/a+pi/(2*a)+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+pi/(2*a)+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<=i and i<=x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\sin \\left({latex(a*x+m)}\\right)=1 \\Leftrightarrow {latex(a*x+m)} ={latex(pi/2)}+k2\\pi \\Leftrightarrow x={latex(-m/a+pi/(2*a))}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in [{latex(-b*pi)};{latex(b*pi)}]$ nên ${latex(-b*pi)}\\le {latex(-m/a+pi/(2*a))}+k{latex(2*pi/a)} \\le {latex(b*pi)} \\Rightarrow {latex(x_1)}\\le k \\le {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==4:
        noi_dung = f"Số nghiệm thuộc khoảng $({latex(-b*pi)};{latex(b*pi)})$ của phương trình $\\sin \\left({latex(a*x+m)}\\right)=1$ là"

        eq=Eq(-m/a+pi/(2*a)+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+pi/(2*a)+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<i and i<x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\sin \\left({latex(a*x+m)}\\right)=1 \\Leftrightarrow {latex(a*x+m)} ={latex(pi/2)}+k2\\pi \\Leftrightarrow x={latex(-m/a+pi/(2*a))}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in ({latex(-b*pi)};{latex(b*pi)})$ nên ${latex(-b*pi)}<{latex(-m/a+pi/(2*a))}+k{latex(2*pi/a)} < {latex(b*pi)} \\Rightarrow {latex(x_1)}< k < {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==5:
        noi_dung = f"Số nghiệm thuộc đoạn $[{latex(-b*pi)};{latex(b*pi)}]$ của phương trình $\\sin \\left({latex(a*x+m)}\\right)=-1$ là"

        eq=Eq(-m/a-pi/(2*a)+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a-pi/(2*a)+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<=i and i<=x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\sin \\left({latex(a*x+m)}\\right)=-1 \\Leftrightarrow {latex(a*x+m)} ={latex(-pi/2)}+k2\\pi \\Leftrightarrow x={latex(-m/a-pi/(2*a))}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in [{latex(-b*pi)};{latex(b*pi)}]$ nên ${latex(-b*pi)}\\le {latex(-m/a-pi/(2*a))}+k{latex(2*pi/a)} \\le {latex(b*pi)} \\Rightarrow {latex(x_1)}\\le k \\le {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==6:
        noi_dung = f"Số nghiệm thuộc khoảng $({latex(-b*pi)};{latex(b*pi)})$ của phương trình $\\sin \\left({latex(a*x+m)}\\right)=-1$ là"

        eq=Eq(-m/a-pi/(2*a)+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a-pi/(2*a)+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<i and i<x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\sin \\left({latex(a*x+m)}\\right)=-1 \\Leftrightarrow {latex(a*x+m)} ={latex(-pi/2)}+k2\\pi \\Leftrightarrow x={latex(-m/a-pi/(2*a))}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in ({latex(-b*pi)};{latex(b*pi)})$ nên ${latex(-b*pi)}<{latex(-m/a-pi/(2*a))}+k{latex(2*pi/a)} <{latex(b*pi)} \\Rightarrow {latex(x_1)}< k < {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dem}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=dem
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B5_14]-M2. Tìm số nghiệm thuộc khoảng đoạn của cosu=m
def ngh_kjg_L11_C1_B5_14():
    x=sp.symbols("x")    
    a=random.randint(1,4)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6, -pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4])    
    b=random.randint(1,10)
    chon=random.randint(1,6)    
    
    if chon==1:
        noi_dung = f"Số nghiệm thuộc đoạn $[{latex(-b*pi)};{latex(b*pi)}]$ của phương trình $\\cos \\left({latex(a*x+m)}\\right)=0$ là"

        eq=Eq(-m/a+pi/(2*a)+x*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+pi/(2*a)+x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi-1),int(b*pi+1)):
            if x_1<=i and i<=x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\cos \\left({latex(a*x+m)}\\right)=0 \\Leftrightarrow {latex(a*x+m)} ={latex(pi/2)}+k\\pi \\Leftrightarrow x={latex(-m/a+pi/(2*a))}+k{latex(pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in ({latex(-b*pi)};{latex(b*pi)})$ nên ${latex(-b*pi)}< {latex(-m/a+pi/(2*a))}+k{latex(pi/a)} < {latex(b*pi)} \\Rightarrow {latex(x_1)}< k < {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==2:
        noi_dung = f"Số nghiệm thuộc khoảng $({latex(-b*pi)};{latex(b*pi)})$ của phương trình $\\cos \\left({latex(a*x+m)}\\right)=0$ là"

        eq=Eq(-m/a+pi/(2*a)+x*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+pi/(2*a)+x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi-1),int(b*pi+1)):
            if x_1<i and i<x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\cos \\left({latex(a*x+m)}\\right)=0 \\Leftrightarrow {latex(a*x+m)} ={latex(pi/2)}+k\\pi \\Leftrightarrow x={latex(-m/a+pi/(2*a))}+k{latex(pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in ({latex(-b*pi)};{latex(b*pi)})$ nên ${latex(-b*pi)}< {latex(-m/a+pi/(2*a))}+k{latex(pi/a)} < {latex(b*pi)} \\Rightarrow {latex(x_1)}< k < {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==3:
        noi_dung = f"Số nghiệm thuộc đoạn $[{latex(-b*pi)};{latex(b*pi)}]$ của phương trình $\\cos \\left({latex(a*x+m)}\\right)=1$ là"

        eq=Eq(-m/a+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi-1),int(b*pi+1)):
            if x_1<=i and i<=x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\cos \\left({latex(a*x+m)}\\right)=1 \\Leftrightarrow {latex(a*x+m)} = k2\\pi \\Leftrightarrow x={latex(-m/a)}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in [{latex(-b*pi)};{latex(b*pi)}]$ nên ${latex(-b*pi)}\\le {latex(-m/a)}+k{latex(2*pi/a)} \\le {latex(b*pi)} \\Rightarrow {latex(x_1)}\\le k \\le {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==4:
        noi_dung = f"Số nghiệm thuộc khoảng $({latex(-b*pi)};{latex(b*pi)})$ của phương trình $\\cos \\left({latex(a*x+m)}\\right)=1$ là"

        eq=Eq(-m/a+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi-1),int(b*pi+1)):
            if x_1<i and i<x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\cos \\left({latex(a*x+m)}\\right)=1 \\Leftrightarrow {latex(a*x+m)} = k2\\pi \\Leftrightarrow x={latex(-m/a)}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in ({latex(-b*pi)};{latex(b*pi)})$ nên ${latex(-b*pi)} < {latex(-m/a)}+k{latex(2*pi/a)} < {latex(b*pi)} \\Rightarrow {latex(x_1)}< k < {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==5:
        noi_dung = f"Số nghiệm thuộc đoạn $[{latex(-b*pi)};{latex(b*pi)}]$ của phương trình $\\cos \\left({latex(a*x+m)}\\right)=-1$ là"

        eq=Eq(-m/a+pi/a+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+pi/a+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi-1),int(b*pi+1)):
            if x_1<=i and i<=x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\cos \\left({latex(a*x+m)}\\right)=-1 \\Leftrightarrow {latex(a*x+m)} =\\pi+ k2\\pi \\Leftrightarrow x={latex(-m/a+pi/a)}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in [{latex(-b*pi)};{latex(b*pi)}]$ nên ${latex(-b*pi)}\\le {latex(-m/a+pi/a)}+k{latex(2*pi/a)} \\le {latex(b*pi)} \\Rightarrow {latex(x_1)}\\le k \\le {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==6:
        noi_dung = f"Số nghiệm thuộc khoảng $({latex(-b*pi)};{latex(b*pi)})$ của phương trình $\\cos \\left({latex(a*x+m)}\\right)=-1$ là"

        eq=Eq(-m/a-pi/a+x*2*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a-pi/a+x*2*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi-1),int(b*pi+1)):
            if x_1<i and i<x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\cos \\left({latex(a*x+m)}\\right)=-1 \\Leftrightarrow {latex(a*x+m)} =-\\pi+ k2\\pi \\Leftrightarrow x={latex(-m/a-pi/a)}+k{latex(2*pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in [{latex(-b*pi)};{latex(b*pi)}]$ nên ${latex(-b*pi)}< {latex(-m/a-pi/a)}+k{latex(2*pi/a)} < {latex(b*pi)} \\Rightarrow {latex(x_1)}< k < {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )
    
    dap_an=dem
       
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B5_15]-M2. Tìm số nghiệm thuộc khoảng đoạn của tanu=m
def ngh_kjg_L11_C1_B5_15():
    x=sp.symbols("x")    
    a=random.randint(1,4)
    m=random.choice([pi, pi/2, pi/3, pi/4,pi/5,pi/6, -pi/2, -pi/3, -pi/4,-pi/5,-pi/6, -pi, 2*pi/3, 3*pi/4, -2*pi/3, -3*pi/4])    
    b=random.randint(1,10)
    
    tan_value=random.choice([0,1,-1,sqrt(3),sqrt(3)/3])
    x_0=atan(tan_value)
    chon=random.randint(1,2)    
    
    if chon==1:
        noi_dung = f"Số nghiệm thuộc đoạn $[{latex(-b*pi)};{latex(b*pi)}]$ của phương trình $\\tan \\left({latex(a*x+m)}\\right)={latex(tan_value)}$ là"

        eq=Eq(-m/a+x_0/a+x*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+x_0/a+x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<=i and i<=x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\tan \\left({latex(a*x+m)}\\right)={latex(tan_value)} \\Leftrightarrow {latex(a*x+m)} ={latex(x_0)}+ k\\pi \\Leftrightarrow x={latex(-m/a+x_0/a)}+k{latex(pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in [{latex(-b*pi)};{latex(b*pi)}]$ nên ${latex(-b*pi)}\\le {latex(-m/a+x_0/a)}+k{latex(pi/a)} \\le {latex(b*pi)} \\Rightarrow {latex(x_1)}\\le k \\le {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )

    if chon==2:
        noi_dung = f"Số nghiệm thuộc khoảng $({latex(-b*pi)};{latex(b*pi)})$ của phương trình $\\tan \\left({latex(a*x+m)}\\right)={latex(tan_value)}$ là"

        eq=Eq(-m/a+x_0/a+x*pi/a,-b*pi)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(-m/a+x_0/a+x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        dem=0
        for i in range(int(-b*pi)-1,int(b*pi+1)):
            if x_1<i and i<x_2:
                dem+=1

        noi_dung_loigiai=(
            f"$\\tan \\left({latex(a*x+m)}\\right)={latex(tan_value)} \\Leftrightarrow {latex(a*x+m)} ={latex(x_0)}+ k\\pi \\Leftrightarrow x={latex(-m/a+x_0/a)}+k{latex(pi/a)}, k\\in \\mathbb{{Z}}$.\n\n"
            f"Do $x\\in ({latex(-b*pi)};{latex(b*pi)})$ nên ${latex(-b*pi)}< {latex(-m/a+x_0/a)}+k{latex(pi/a)} < {latex(b*pi)} \\Rightarrow {latex(x_1)}< k < {latex(x_2)}$.\n\n"
            f"Có ${{{dem}}}$ số k thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm."
            )
    
    dap_an=dem
       
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word, loigiai_word, latex_tuluan, dap_an

#[D11_C1_B5_16]-TF-M3. Cho sinax=m. Xét Đ-S: sinax=sinv, tập nghiệm, số nghiệm thuộc khoảng, tổng các nghiệm thuộc đoạn
def ngh_kjg_L11_C1_B5_16():
    x=sp.symbols("x")
    a=random.randint(2,8)
    m=random.choice([1,-1,0])     
    x_0=asin(m)

    noi_dung = f"Cho phương trình $\\sin {a}x={m}$ (1). Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"

    if m==1:    
        kq1_T=f"* Phương trình (1) $\\Leftrightarrow \\sin {a}x=\\sin {latex(x_0+random.randint(0,2)*2*pi)}$"

    if m==-1:    
        kq1_T=f"* Phương trình (1) $\\Leftrightarrow \\sin {a}x=\\sin \\left({latex(x_0+random.randint(0,2)*2*pi)}\\right)$"

    if m==0:    
        kq1_T=f"* Phương trình (1) $\\Leftrightarrow \\sin {a}x=\\sin {latex(x_0+random.randint(0,2)*2*pi)}$"

    kq1_F=random.choice([
        f"Phương trình (1) $\\Leftrightarrow \\sin {a}x=\\sin {latex(random.choice([pi/random.randint(3,8)]))}$",
        f"Phương trình (1) $\\Leftrightarrow \\sin {a}x=\\sin \\left({latex(random.choice([-pi/random.randint(3,8)]))}\\right)$",
         f"Phương trình (1) $\\Leftrightarrow \\sin {a}x=\\sin {latex(x_0+pi)}$"
        ])
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Phương trình (1) $\\Leftrightarrow \\sin {a}x=\\sin {latex(x_0)}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Phương án 2:

    kq2_T=f"*Phương trình (1) có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
    kq2_F=f"Phương trình (1) có nghiệm là $x={latex(x_0/(2*a))}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
    HDG=f"$(1)\\Leftrightarrow {a}x={latex(x_0)}+k2\\pi \\Leftrightarrow x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$"

    if m==0:
         kq2_T=f"*Phương trình (1) có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$."
         kq2_F=f"Phương trình (1) có nghiệm là $x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
         HDG=f"$(1)\\Leftrightarrow {a}x=k\\pi \\Leftrightarrow x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$"
    
    kq2=random.choice([kq2_T, kq2_F])    
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Tìm các cận của k
    b=random.randint(1,3)

    eq=Eq(x_0/a+x*2*pi/a,0)
    sol= solve(eq , x)
    x_1=sol[0]

    eq=Eq(x_0/a+x*2*pi/a,b*pi)
    sol= solve(eq , x)
    x_2=sol[0]

    #Đếm các số k: x_1<k<x_2
    dem=0
    for k in range(int(x_1)-1,int(x_2+1)):
        if x_1<k and k<x_2:
            dem+=1

    kq3_T=f"* Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem}}}$" 
    kq3_F=f"Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem+random.randint(1,2)}}}$"
    
    HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
        f"Xét: $0<{latex(x_0/a)}+k{latex(2*pi/a)}<{latex(b*pi)}$"
        f"$\\Rightarrow {latex(x_1)}<k<{latex(x_2)}$. \n\n"
        f"Có ${{{dem}}}$ số nguyên ${{k}}$ thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm thuộc khoảng $(0;{latex(b*pi)})$.")
    if m==0:
        #Tìm các cận của k
        b=random.randint(1,3)

        eq=Eq(x*pi/a,0)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        #Đếm các số k: x_1<k<x_2
        dem=0
        for k in range(int(x_1)-1,int(x_2+1)):
            if x_1<k and k<x_2:
                dem+=1

        kq3_T=f"* Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem}}}$" 
        kq3_F=f"Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem+random.randint(1,2)}}}$"
        
        HDG=(f"$(1)$ có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
            f"Xét: $0<k{latex(pi/a)}<{latex(b*pi)}$"
            f"$\\Rightarrow {latex(x_1)}<k<{latex(x_2)}$. \n\n"
            f"Có ${{{dem}}}$ số nguyên ${{k}}$ thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm thuộc khoảng $(0;{latex(b*pi)})$.")

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    kq3=random.choice([kq3_T, kq3_F])
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    # Phương án 4:
    chon=random.randint(1,2)
    # Tìm nghiệm âm lớn nhất
    if chon==1:
        if m==0:
            kq4_T=f"* Nghiệm âm lớn nhất của phương trình là $x={latex(-pi/a)}$"
            kq4_F=f" Nghiệm âm lớn nhất của phương trình là $x={latex(-pi/(random.randint(2,3)*a))}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k=-1$. Khi đó $x={latex(-pi/a)}$.")               

        if m in [-1,1]:
            k = 5    
            while True:                
                x = x_0/a+k*2*pi/a
                k-=1                
                if x < 0:
                    break
            max_am,k=x,k+1       

            kq4_T=f"* Nghiệm âm lớn nhất của phương trình là $x={latex(max_am)}$"
            kq4_F=f" Nghiệm âm lớn nhất của phương trình là $x={latex(max_am-random.randint(1,2)*pi)}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k={k}$. Khi đó $x={latex(max_am)}$.")
    
    #Tìm nghiệm dương nhỏ nhất    
    if chon==2:
        if m==0:
            kq4_T=f"* Nghiệm dương nhỏ nhất của phương trình là $x={latex(pi/a)}$"
            kq4_F=f" Nghiệm âm nhỏ nhất của phương trình là $x={latex(pi/(random.randint(2,3)*a))}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k=1$. Khi đó $x={latex(pi/a)}$.")    
        if m in [-1,1]:
            k = -5    
            while True:
                # Tính giá trị x cho k
                x = x_0/a+k*2*pi/a
                k+=1
                
                if x > 0:
                    break
            max_duong,k=x,k-1       

            kq4_T=f"* Nghiệm dương nhỏ nhất của phương trình là $x={latex(max_duong)}$"
            kq4_F=f" Nghiệm dương nhỏ nhất của phương trình là $x={latex(max_duong+random.randint(1,2)*pi)}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm dương nhỏ nhất ứng với $k={k}$. Khi đó $x={latex(max_duong)}$.") 
   
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

#[D11_C1_B5_17]-TF-M3. Cho cosax=m. Xét Đ-S: cosax=cosv, tập nghiệm, số nghiệm thuộc khoảng, tổng các nghiệm thuộc đoạn
def ngh_kjg_L11_C1_B5_17():
    x=sp.symbols("x")
    a=random.randint(2,8)
    m=random.choice([1,-1,0])    
    x_0=acos(m)

    noi_dung = f"Cho phương trình $\\cos {a}x={m}$ (1). Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"

       
    kq1_T=f"* Phương trình (1) $\\Leftrightarrow \\cos {a}x=\\cos {latex(x_0+random.randint(0,2)*2*pi)}$"  
    kq1_F=random.choice([
        f"Phương trình (1) $\\Leftrightarrow \\cos {a}x=\\cos {latex(random.choice([pi/random.randint(3,8)]))}$",
        f"Phương trình (1) $\\Leftrightarrow \\cos {a}x=\\cos \\left({latex(random.choice([-pi/random.randint(3,8)]))}\\right)$",
         f"Phương trình (1) $\\Leftrightarrow \\cos {a}x=\\cos {latex(x_0+pi)}$"
        ])
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"Phương trình (1) $\\Leftrightarrow \\cos {a}x=\\cos {latex(x_0)}$."
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Phương án 2:

    kq2_T=f"*Phương trình (1) có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
    kq2_F=f"Phương trình (1) có nghiệm là $x={latex(x_0/(2*a))}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
    HDG=f"$(1)\\Leftrightarrow {a}x={latex(x_0)}+k2\\pi \\Leftrightarrow x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$"

    if m==1:
        kq2_T=f"*Phương trình (1) có nghiệm là $x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
        kq2_F=f"Phương trình (1) có nghiệm là $x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
        HDG=f"$(1)\\Leftrightarrow {a}x=k2\\pi \\Leftrightarrow x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$"

    if m==0:
         kq2_T=f"*Phương trình (1) có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$."
         kq2_F=f"Phương trình (1) có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
         HDG=f"$(1)\\Leftrightarrow {a}x={latex(x_0)}+k\\pi \\Leftrightarrow x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$"
    
    kq2=random.choice([kq2_T, kq2_F])    
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Tìm các cận của k
    b=random.randint(1,3)

    eq=Eq(x_0/a+x*2*pi/a,0)
    sol= solve(eq , x)
    x_1=sol[0]

    eq=Eq(x_0/a+x*2*pi/a,b*pi)
    sol= solve(eq , x)
    x_2=sol[0]

    #Đếm các số k: x_1<k<x_2
    dem=0
    for k in range(int(x_1)-1,int(x_2+1)):
        if x_1<k and k<x_2:
            dem+=1

    kq3_T=f"* Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem}}}$" 
    kq3_F=f"Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem+random.randint(1,2)}}}$" 

    HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
        f"Xét: $0<{latex(x_0/a)}+k{latex(2*pi/a)}<{latex(b*pi)}$"
        f"$\\Rightarrow {latex(x_1)}<k<{latex(x_2)}$. \n\n"
        f"Có ${{{dem}}}$ số nguyên ${{k}}$ thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm thuộc khoảng $(0;{latex(b*pi)})$.")
    if m==1:
        HDG=(f"$(1)$ có nghiệm là $x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
        f"Xét: $0<k{latex(2*pi/a)}<{latex(b*pi)}$"
        f"$\\Rightarrow {latex(x_1)}<k<{latex(x_2)}$. \n\n"
        f"Có ${{{dem}}}$ số nguyên ${{k}}$ thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm thuộc khoảng $(0;{latex(b*pi)})$.")


    if m==0:
        #Tìm các cận của k
        b=random.randint(1,3)

        eq=Eq(x_0/a+x*pi/a,0)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(x_0/a+x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        #Đếm các số k: x_1<k<x_2
        dem=0
        for k in range(int(x_1)-1,int(x_2+1)):
            if x_1<k and k<x_2:
                dem+=1

        kq3_T=f"* Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem}}}$" 
        kq3_F=f"Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem+random.randint(1,2)}}}$"
        
        HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
            f"Xét: $0<{latex(x_0/a)}+k{latex(pi/a)}<{latex(b*pi)}$"
            f"$\\Rightarrow {latex(x_1)}<k<{latex(x_2)}$. \n\n"
            f"Có ${{{dem}}}$ số nguyên ${{k}}$ thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm thuộc khoảng $(0;{latex(b*pi)})$.")

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    kq3=random.choice([kq3_T, kq3_F])
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    # Phương án 4:
    chon=random.randint(1,2)

    # Tìm nghiệm âm lớn nhất
    if chon==1:        
        if m==0:            
            k = 5    
            while True:                
                x = x_0/a+k*pi/a
                k-=1                    
                if x < 0:
                    break                    
            max_am,k=x,k+1

            kq4_T=f"* Nghiệm âm lớn nhất của phương trình là $x={latex(max_am)}$"
            kq4_F=f" Nghiệm âm lớn nhất của phương trình là $x={latex(max_am-random.randint(1,2)*pi)}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k={k}$. Khi đó $x={latex(max_am)}$.")

            

        if m in [-1,1]:
            
            k = 5    
            while True:                
                x = x_0/a+k*2*pi/a
                k-=1
                
                if x < 0:
                    break
                    
            max_am,k=x,k+1       

            kq4_T=f"* Nghiệm âm lớn nhất của phương trình là $x={latex(max_am)}$"
            kq4_F=f" Nghiệm âm lớn nhất của phương trình là $x={latex(max_am-random.randint(1,2)*pi)}$"            
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k={k}$. Khi đó $x={latex(max_am)}$.")
            if m==1:
                HDG=(f"$(1)$ có nghiệm là $x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                    f" Nghiệm âm lớn nhất ứng với $k={k}$. Khi đó $x={latex(max_am)}$.")
    
    #Tìm nghiệm dương nhỏ nhất    
    if chon==2:
        if m==0:
            
            k = -5    
            while True:
                # Tính giá trị x cho k
                x = x_0/a+k*pi/a
                k+=1
                
                if x > 0:
                    break
            max_duong,k=x,k-1
            kq4_T=f"* Nghiệm dương nhỏ nhất của phương trình là $x={latex(max_duong)}$"
            kq4_F=f" Nghiệm âm nhỏ nhất của phương trình là $x={latex(max_duong+random.randint(1,2)*pi)}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k={k}$. Khi đó $x={latex(max_duong)}$.")        

        if m in [-1,1]:
            
            k = -5    
            while True:
                # Tính giá trị x cho k
                x = x_0/a+k*2*pi/a
                k+=1                    
                if x > 0:
                    break
            max_duong,k=x,k-1       

            kq4_T=f"* Nghiệm dương nhỏ nhất của phương trình là $x={latex(max_duong)}$"
            kq4_F=f" Nghiệm dương nhỏ nhất của phương trình là $x={latex(max_duong+random.randint(1,2)*pi)}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm dương nhỏ nhất ứng với $k={k}$. Khi đó $x={latex(max_duong)}$.")
            if m==1:
                HDG=(f"$(1)$ có nghiệm là $x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm dương nhỏ nhất ứng với $k={k}$. Khi đó $x={latex(max_duong)}$.")
   
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

#[D11_C1_B5_18]-TF-M3. Cho tanax=m. Xét Đ-S: tanx=tanv, tập nghiệm, số nghiệm thuộc khoảng, tổng các nghiệm thuộc đoạn
def ngh_kjg_L11_C1_B5_18():
    x=sp.symbols("x")
    a=random.randint(2,8)
    m=random.choice([sqrt(3),-sqrt(3),1,-1,0,sqrt(3)/3,-sqrt(3)/3])     
    x_0=atan(m)

    noi_dung = f"Cho phương trình $\\tan {a}x={latex(m)}$ (1). Xét tính đúng-sai của các khẳng định sau. "        
    debai_word= f"{noi_dung}\n"

    
    kq1_T=f"* Phương trình (1) $\\Leftrightarrow \\tan {a}x=\\tan {latex(x_0+random.randint(0,2)*pi)}$"  
    kq1_F=f"Phương trình (1) $\\Leftrightarrow \\tan {a}x=\\tan {latex(x_0+pi/2)}$"
    HDG=f"Phương trình (1) $\\Leftrightarrow \\tan {a}x=\\tan {latex(x_0)}$."
    if x_0<0:
        kq1_T=f"* Phương trình (1) $\\Leftrightarrow \\tan {a}x=\\tan \\left({latex(x_0+random.randint(0,2)*pi)}\\right)$"  
        kq1_F=f"Phương trình (1) $\\Leftrightarrow \\tan {a}x=\\tan \\left({latex(x_0+pi/2)}\\right)$"
        HDG=f"Phương trình (1) $\\Leftrightarrow \\tan {a}x=\\tan \\left({latex(x_0)}\\right)$."

    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Phương án 2:

    kq2_T=f"*Phương trình (1) có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$."
    kq2_F=f"Phương trình (1) có nghiệm là $x={latex(x_0/a)}+k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
    HDG=f"$(1)\\Leftrightarrow {a}x={latex(x_0)}+k\\pi \\Leftrightarrow x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$"

    if m==0:
         kq2_T=f"*Phương trình (1) có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$."
         kq2_F=f"Phương trình (1) có nghiệm là $x=k{latex(2*pi/a)},k\\in \\mathbb{{Z}}$."
         HDG=f"$(1)\\Leftrightarrow {a}x=k\\pi \\Leftrightarrow x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$"
    
    kq2=random.choice([kq2_T, kq2_F])    
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    #Tìm các cận của k
    b=random.randint(1,3)

    eq=Eq(x_0/a+x*pi/a,0)
    sol= solve(eq , x)
    x_1=sol[0]

    eq=Eq(x_0/a+x*pi/a,b*pi)
    sol= solve(eq , x)
    x_2=sol[0]

    #Đếm các số k: x_1<k<x_2
    dem=0
    for k in range(int(x_1)-1,int(x_2+1)):
        if x_1<k and k<x_2:
            dem+=1

    kq3_T=f"* Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem}}}$" 
    kq3_F=f"Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem+random.randint(1,2)}}}$" 

    HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
        f"Xét: $0<{latex(x_0/a)}+k{latex(pi/a)}<{latex(b*pi)}$"
        f"$\\Rightarrow {latex(x_1)}<k<{latex(x_2)}$. \n\n"
        f"Có ${{{dem}}}$ số nguyên ${{k}}$ thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm thuộc khoảng $(0;{latex(b*pi)})$.")

    if m==0:
        #Tìm các cận của k
        b=random.randint(1,3)

        eq=Eq(x*pi/a,0)
        sol= solve(eq , x)
        x_1=sol[0]

        eq=Eq(x*pi/a,b*pi)
        sol= solve(eq , x)
        x_2=sol[0]

        #Đếm các số k: x_1<k<x_2
        dem=0
        for k in range(int(x_1)-1,int(x_2+1)):
            if x_1<k and k<x_2:
                dem+=1

        kq3_T=f"* Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem}}}$" 
        kq3_F=f"Số nghiệm thuộc khoảng $(0;{latex(b*pi)})$ là ${{{dem+random.randint(1,2)}}}$"
        
        HDG=(f"$(1)$ có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
            f"Xét: $0<k{latex(pi/a)}<{latex(b*pi)}$"
            f"$\\Rightarrow {latex(x_1)}<k<{latex(x_2)}$. \n\n"
            f"Có ${{{dem}}}$ số nguyên ${{k}}$ thỏa mãn nên phương trình có ${{{dem}}}$ nghiệm thuộc khoảng $(0;{latex(b*pi)})$.")

    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    kq3=random.choice([kq3_T, kq3_F])
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    # Phương án 4:
    chon=random.randint(1,2)
    # Tìm nghiệm âm lớn nhất
    if chon==1:
        if m==0:
            kq4_T=f"* Nghiệm âm lớn nhất của phương trình là $x={latex(-pi/a)}$"
            kq4_F=f" Nghiệm âm lớn nhất của phương trình là $x={latex(-pi/(random.randint(2,3)*a))}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k=-1$. Khi đó $x={latex(-pi/a)}$.")            

        else:            
            k = 5    
            while True:                
                x = x_0/a+k*pi/a
                k-=1
                
                if x < 0:
                    break
            max_am,k=x,k+1      

            kq4_T=f"* Nghiệm âm lớn nhất của phương trình là $x={latex(max_am)}$"
            kq4_F=f" Nghiệm âm lớn nhất của phương trình là $x={latex(max_am-random.randint(1,2)*pi)}$"            
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k={k}$. Khi đó $x={latex(max_am)}$.")
    
    #Tìm nghiệm dương nhỏ nhất    
    if chon==2:
        if m==0:
            kq4_T=f"* Nghiệm dương nhỏ nhất của phương trình là $x={latex(pi/a)}$"
            kq4_F=f" Nghiệm âm nhỏ nhất của phương trình là $x={latex(pi/(random.randint(2,3)*a))}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x=k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm âm lớn nhất ứng với $k=1$. Khi đó $x={latex(pi/a)}$.")

        else:            
            k = -5    
            while True:
                # Tính giá trị x cho k
                x = x_0/a+k*pi/a
                k+=1
                
                if x > 0:
                    break
            max_duong,k=x,k-1     

            kq4_T=f"* Nghiệm dương nhỏ nhất của phương trình là $x={latex(max_duong)}$"
            kq4_F=f" Nghiệm dương nhỏ nhất của phương trình là $x={latex(max_duong+random.randint(1,2)*pi)}$" 
        
            HDG=(f"$(1)$ có nghiệm là $x={latex(x_0/a)}+k{latex(pi/a)},k\\in \\mathbb{{Z}}$.\n\n"
                f" Nghiệm dương nhỏ nhất ứng với $k={k}$. Khi đó $x={latex(max_duong)}$.") 
   
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

