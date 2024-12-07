import math
import random
from fractions import Fraction
import sympy as sp
from sympy import*
import my_module
from math import gcd
from sympy import nsimplify, latex
def phan_so(t):
    m=latex(Rational(t).limit_denominator(1000000000))
    return m
def thay_cong_tru(st):
    return st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("1x","x").replace("1y","y").replace("-1x","-x").replace("-1y","-y")
def thayso(st):
    # Sử dụng biểu thức chính quy để thay thế +a thành a
    result = re.sub(r'\+(\d+)', r'\1', st)
    return result

def hien_thi_phan_so(phanso):
    tu_so = phanso.numerator
    mau_so = phanso.denominator
    return f"{tu_so}\n─\n{mau_so}"


def tim_truc_tam(A, B, C):
        # Lấy tọa độ các điểm
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C
        
        # Tính hệ số góc của các cạnh
        m_AB = (y2 - y1) / (x2 - x1) if x2 != x1 else None
        m_BC = (y3 - y2) / (x3 - x2) if x3 != x2 else None

        # Phương trình đường cao từ A và B
        if m_BC is not None:
            m_CA_vuong = -1 / m_BC
            b_CA = y1 - m_CA_vuong * x1
        else:  # BC thẳng đứng, đường cao từ A nằm ngang
            m_CA_vuong = 0
            b_CA = y1

        if m_AB is not None:
            m_BA_vuong = -1 / m_AB
            b_BA = y2 - m_BA_vuong * x2
        else:  # AB thẳng đứng, đường cao từ B nằm ngang
            m_BA_vuong = 0
            b_BA = y2

        # Giải hệ phương trình hai đường cao để tìm trực tâm
        x, y = symbols('x y')
        pt1 = Eq(y, m_CA_vuong * x + b_CA) if m_BC is not None else sp.Eq(x, x3)
        pt2 = Eq(y, m_BA_vuong * x + b_BA) if m_AB is not None else sp.Eq(x, x1)

        solution = solve([pt1, pt2], (x, y))
        gia_tri_x = solution[x]
        gia_tri_y = solution[y]

        return gia_tri_x,gia_tri_y


########Bài 3: Ứng dụng hệ thức lượng vào toán thực tế
#[D10_C4_B3_01]-TL-M3. Ứng dụng hệ thức lượng trong tam giác
def D10_C4_B3_01():
    a=random.choice([1.7, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 ])
    a1=str(a).replace(".",",")
    h=random.randint(10,30)
    x=random.randint(20,35)
    y=x+random.randint(35,40)
    AC1= (h*math.sin(math.radians(90+x)))/math.sin(math.radians(y-x))
    e=round(AC1)
    kq=round(AC1*sin(math.radians(y)) )
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
    noi_dung = f"   Bạn {A} đứng ở đỉnh của tòa nhà và quan sát chiếc diều, nhận thấy góc nâng (góc nghiêng giữa phương từ mắt của bạn {A} tới chiếc diều và phương nằm ngang) là $\\alpha={x}^{{\\circ}}$; khoảng cách từ đỉnh tòa nhà tới mắt bạn {A} là ${{{a1}}}$m. Cùng lúc đó ở dưới chân tòa nhà, bạn {B} cũng quan sát chiếc diều và thấy góc nâng là $\\beta={y}^{{\\circ}}$; khoảng cách từ mặt đất tới mắt bạn {B} cũng là ${{{a1}}}$m. Biết chiều cao của tòa nhà là $h={{{h}}}m$ (minh họa ở hình bên). Chiếc diều bay cao bao nhiêu mét so với mặt đất (làm tròn kết quả đến hàng đơn vị)?"

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
            f"$\\widehat{{C}}= 180^{{\\circ}} - \\left(\\widehat{{A}}+\\widehat{{B}}\\right) = 180^{{\\circ}} - \\left({90+x}^{{\\circ}}+{90-y}^{{\\circ}}\\right) = {y-x}^{{\\circ}}$."
            f"Áp dụng định lí sin trong tam giác ${{ABC}}$ ta có\n\n"
         f"$\\dfrac{{AB}}{{ \\sin C}} = \\dfrac{{BC}}{{\\sin A }} \\Rightarrow BC = \\dfrac{{AB\\sin A}}{{\\sin C}} = \\dfrac{{ {h}\\sin {90+x}^{{\\circ}} }}{{\\sin {y-x}^{{\\circ}} }} \\approx {e}$\n\n"
         f"Trong tam giác ${{CBH}}$ vuông tại ${{H}}$ ta có \n\n"
         f"$CH=BC\\sin B  \\approx {e}\\sin{{ {y}^{{\\circ}} }}\\approx {kq}$ m\n\n"
        f"Vậy chiếc diều bay cao khoảng ${{{kq}}}$ mét so với mặt đất.")

    debai_word= f"{noi_dung}\n"\
    f"{file_name}\n"
    loigiai_word=f"Lời giải:\n{file_name1} \n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\ \n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\shortans[oly]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n{code_hinh1} \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq
    return debai_word, loigiai_word, latex_tuluan, dap_an      



#[D10_C3_B2_14]-TL-M3. Toán thực tế liên quan đến đồ thị hàm bậc hai 1
def D10_C3_B2_14():
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
        f"\\shortans[oly]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n{code_hinh1} \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an    




#[D10_C2_B2_05]-TL-M3. Toán thực tế ứng dụng bpt bậc nhất 2 ẩn
def D10_C2_B2_05():
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
    f"\\shortans[only]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq

    return debai_word, loigiai_word, latex_tuluan, dap_an





#[D10_C3_B2_15]-M3. Toán thực tế ứng dụng đồ thị hàm số bậc hai tìm lợi nhuận lớn nhất
def D10_C3_B2_15():
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

    kq=f" ${{{kq}}}$ USD"
    ds=[f" ${{{phan_so((e-a*x0)*(x0-x1)-random.randint(1,2))}}}$ USD", f" ${{{phan_so((e-a*x0)*(x0-x1)+random.randint(1,2))}}}$ USD", f" ${{{phan_so((e-a*x0)*(x0-x1)-random.randint(3,4))}}}$ USD", f" ${{{phan_so((e-a*x0)*(x0-x1)+random.randint(3,4))}}}$ USD", f" ${{{phan_so((e-a*x0)*(x0-x1)-random.randint(5,6))}}}$ USD", f" ${{{phan_so((e-a*x0)*(x0-x1)+random.randint(5,6))}}}$ USD" ]
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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan



#[D10_C7_B2_10]-M3. Toán thực tế ứng dụng tìm giá bán để lợi nhuận thoả điều kiện cho trước
def D10_C7_B2_10():
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

    kq=f" $({x4};{x5})$ USD"
    ds=[f"$({phan_so(x1)};{x5})$ USD", f" $({phan_so(x1)};{x0})$ USD", f" $({phan_so(x1)};{x4})$ USD", f" $({x0};{x2})$ USD", f" $({phan_so(x4)};{x2})$ USD" ]
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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan




#[D10_C3_B2_16]-M2. Tìm trục đối xứng của Parabol khi biết toạ độ giao điểm của nó với trục hoành.
def D10_C3_B2_16():
    a=random.choice([i for i in range(-5,5) if i!=0])
    x1=random.randint(-10,10)
    x2=random.choice([i for i in range(-10,10) if i!=x1])
    x0=(x1+x2)/2 
    x0=phan_so(x0)
    x=symbols("x")
    noi_dung=f" Biết đồ thị hàm số bậc hai $y=f(x)=ax^{{2}}+bx+x$ ($ a \\ne 0$) cắt trục hoành tại hai điểm $A({x1};0)$ và $B({x2};0)$. Trục đối xứng của đồ thị là đường thẳng nào?"
    noi_dung_loigiai=f" Trục đối xứng là đường thẳng $x= \\dfrac{{{x1}+{x2}}}{{2}}={x0}$"

    kq=f" $x={x0}$"
    kq2=f"$x={phan_so(x1+x2 )}$ "
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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan



#[D10_C5_B3_06]-TL-M4. Bài tổng hợp 
def D10_C5_B3_06():
    a=random.randint(2,8)
    c=random.randint(1,5)
    b=(a+1)*c
    e=str(round((sqrt( (a*c)**2+ b**2-2*a*c*b* 0.5)),1)).replace(".", ",").replace(".0", "")
    
    M=random.choice(["H ", "G", "D", "K", "O", "J", "E", "F", "N"])


    chon=random.randint(1,2) 
    if chon ==1:
        noi_dung = f" Cho tam giác ${{ABC}}$ đều cạnh bằng ${{{b}}}$ cm. ${{{M}}}$ là điểm thoả mãn hệ thức \n\n $\\mid \\overrightarrow{{{M}A}}+{a} \\overrightarrow{{{M}B}} \\mid=\\mid \\overrightarrow{{{M}C}}- \\overrightarrow{{{M}B}} \\mid  $. Khoảng cách lớn nhất từ điểm ${{C}}$ đến điểm ${{{M}}}$ là:\n\n (Chỉ được làm tròn kết quả của phép tính cuối cùng đến chữ số thập phân thứ nhất)."

        kq=str(round(sqrt( (a*c)**2+ b**2-2*a*c*b* 0.5)+c,1 )).replace(".", ",").replace(".0", "")
        noi_dung_loigiai=(f" Gọi ${{I}}$ là điểm sao cho $\\overrightarrow{{IA}}+{a}\\overrightarrow{{IB}} = \\overrightarrow{{0}}$ \n\n"
        f"$\\mid \\overrightarrow{{{M}A}}+{a} \\overrightarrow{{{M}B}} \\mid=\\mid \\overrightarrow{{{M}C}}- \\overrightarrow{{{M}B}} \\mid  $\n\n "
            f"  $\\mid {1+a}\\overrightarrow{{{M}I}} \\mid = \\mid \\overrightarrow{{BC}} \\mid $ \n\n"
            f" ${M}I= {c} $ \n\n"
            f" Ta có $AI={a*c} $ \n\n "
            f" Áp dụng định lí cô sin ta có $IC=\\sqrt{{ IA^{{2}}+AC^{{2}} -2 \\cdot IA \\cdot AC \\cos{{60^{{\\circ}}}} }} \\approx {e}$ \n\n"
            f" Khoảng cách lớn nhất từ ${{C}}$ đến ${{M}}$ là $IC+I{M}\\approx {kq}$")
    if chon ==2:
        noi_dung = f" Cho tam giác ${{ABC}}$ đều cạnh bằng ${{{b}}}$ cm. ${{{M}}}$ là điểm thoả mãn hệ thức \n\n $\\mid \\overrightarrow{{{M}A}}+{a} \\overrightarrow{{{M}B}} \\mid=\\mid \\overrightarrow{{{M}C}}- \\overrightarrow{{{M}B}} \\mid  $. Khoảng cách nhỏ nhất từ điểm ${{C}}$ đến điểm ${{{M}}}$ là:\n\n (Chỉ được làm tròn kết quả của phép tính cuối cùng đến chữ số thập phân thứ nhất)."

        kq=str(round(abs(sqrt( (a*c)**2+ b**2-2*a*c*b* 0.5)-c),1 )).replace(".", ",").replace(".0", "")
        noi_dung_loigiai=(f" Gọi ${{I}}$ là điểm sao cho $\\overrightarrow{{IA}}+{a}\\overrightarrow{{IB}} = \\overrightarrow{{0}}$ \n\n"
        f"$\\mid \\overrightarrow{{{M}A}}+{a} \\overrightarrow{{{M}B}} \\mid=\\mid \\overrightarrow{{{M}C}}- \\overrightarrow{{{M}B}} \\mid  $\n\n "
            f"  $\\mid {1+a}\\overrightarrow{{{M}I}} \\mid = \\mid \\overrightarrow{{BC}} \\mid $ \n\n"
            f" ${M}I= {c} $ \n\n"
            f" Ta có $AI={a*c} $ \n\n "
            f" Áp dụng định lí cô sin ta có $IC=\\sqrt{{ IA^{{2}}+AC^{{2}} -2 \\cdot IA \\cdot AC \\cos{{60^{{\\circ}}}} }} \\approx {e}$ \n\n"
            f" Khoảng cách nhỏ nhất từ ${{C}}$ đến ${{M}}$ là $IC-I{M}\\approx {kq}$")
    debai_word= f"{noi_dung}\n"

    loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[only]{{{kq}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an=kq 
    return debai_word, loigiai_word, latex_tuluan, dap_an




#[D10_CX_B0_14]-TF-M3. Tổng hợp(tìm toạ độ trực tâm)
def D10_CX_B0_14():


    def tao_tam_giac():
        while True:
            x1 = random.randint(-6, 6)
            x2 = random.choice([i for i in range(-6, 7) if i != x1])
            x3 = random.choice([i for i in range(-6, 7) if i != x2])
            y1 = random.randint(-6, 6)
            y2 = random.choice([i for i in range(-6, 7) if i != y1])
            y3 = random.choice([i for i in range(-6, 7) if i != y2])

            AB2 = (x2 - x1)**2 + (y2 - y1)**2
            BC2 = (x3 - x2)**2 + (y3 - y2)**2
            CA2 = (x3 - x1)**2 + (y3 - y1)**2

            # Kiểm tra điều kiện tam giác không thẳng hàng và không vuông
            if (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1) and \
               AB2 + BC2 != CA2 and AB2 + CA2 != BC2 and BC2 + CA2 != AB2:
                return (x1, y1), (x2, y2), (x3, y3)



    # Tạo tam giác hợp lệ
    A, B, C = tao_tam_giac()

    # Tính toán

    # Lấy giá trị tọa độ các điểm
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # Nội dung bài toán
    noi_dung = f"Cho tam giác ${{ABC}}$ với $A({x1},{y1})$, $B({x2},{y2})$, $C({x3},{y3})$. Xét tính đúng sai của các khẳng định sau:"

    # Nội dung lời giải

    
    kq1_T = random.choice([f"*$\\overrightarrow{{AB}}= \\left( {x2-x1}; {y2-y1}   \\right)$",  
                           f"*$\\overrightarrow{{AC}}= \\left( {x3-x1}; {y3-y1}   \\right)$",
                           f"*$\\overrightarrow{{BC}}= \\left( {x3-x2}; {y3-y2}   \\right)$"])
    kq1_F = random.choice([f"$\\overrightarrow{{BA}}= \\left( {x2-x1}; {y2-y1}   \\right)$",  
                           f"$\\overrightarrow{{CA}}= \\left( {x3-x1}; {y3-y1}   \\right)$",
                           f"$\\overrightarrow{{CB}}= \\left( {x3-x2}; {y3-y2}   \\right)$"])
    kq1 = random.choice([kq1_T, kq1_F])
    HDG = f"{kq1_F} "
    loigiai_1 = f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1 == kq1_F:
        loigiai_1 = f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*Toạ độ trọng tâm tam giác ${{ABC}}$ là $\\left( {phan_so( (x1+x2+x3)/3)};{phan_so((y1+y2+y3)/3)} \\right)$  "
    kq2_F=f"Toạ độ trọng tâm tam giác ${{ABC}}$ là $\\left( {phan_so( (x1+x2+x3)/2)};{phan_so((y1+y2+y3)/2 )} \\right)$  "
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"Toạ độ trọng tâm tam giác ${{ABC}}$ là $\\left( {phan_so( (x1+x2+x3)/3)};{phan_so((y1+y2+y3)/3)} \\right)$ "
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    if ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/(sqrt((x3-x1)**2+(y3-y1)**2)* sqrt((x2-x1)**2+(y2-y1)**2)) <0:
    
        m=round( ((x3+x1)*(x2-x1)+(y3-y1)*(y2-y1))/(sqrt((x3-x1)**2+(y3-y1)**2)* sqrt((x2-x1)**2+(y2-y1)**2)),2 ) 
        m=str(m).replace(".",",")

        kq3_T=f"* $\\widehat{{A}}$ là góc tù" 
        kq3_F=f"$\\widehat{{A}}$ là góc nhọn"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\cos{{A}}\\approx {m} < 0$ nên $\\widehat{{A}}$ là góc tù " 
    if ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/(sqrt((x3-x1)**2+(y3-y1)**2)* sqrt((x2-x1)**2+(y2-y1)**2)) >0:
    
        m=round( ((x3+x1)*(x2-x1)+(y3-y1)*(y2-y1))/(sqrt((x3-x1)**2+(y3-y1)**2)* sqrt((x2-x1)**2+(y2-y1)**2)),2 ) 
        m=str(m).replace(".",",")

        kq3_T=f"* $\\widehat{{A}}$ là góc nhọn" 
        kq3_F=f"$\\widehat{{A}}$ là góc tù"
        kq3=random.choice([kq3_T, kq3_F])
        HDG=f"$\\cos{{A}}\\approx {round( ((x3-x1)*(x2-x1)+(y3-y1)*(y2-y1))/(sqrt((x3-x1)**2+(y3-y1)**2)* sqrt((x2-x1)**2+(y2-y1)**2)),2 )} > 0$ nên $\\widehat{{A}}$ là góc nhọn "
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

###########chỗ này là tìm trực tâm



    truc_tam_x, truc_tam_y = tim_truc_tam(A, B, C)
    debai_word= f"{noi_dung}\n"
    kq4_T=f"*Toạ độ trực tâm tam giác là $H\\left({phan_so(truc_tam_x)}, {phan_so(truc_tam_y)}\\right)$ "
    kq4_F=f"Toạ độ trực tâm tam giác là $H\\left({phan_so(truc_tam_x+random.randint(1,2))}, {phan_so(truc_tam_y+random.randint(1,2))}\\right)$  " 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=f"Trực tâm tam giác $H\\left({phan_so(truc_tam_x)}, {phan_so(truc_tam_y)}\\right)$"
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


#[D10_C5_B3_06]-TF-M3. Tổng hợp vecto
def D10_C5_B3_06():
    points = [chr(i) for i in range(ord('A'), ord('N') + 1)]
    random.shuffle(points)
    points=points[0:6]
    points.sort()
    A,B,C,M, G, I=points 
    k =random.choice([i for i in range(3,6)])
    a=random.choice([i for i in range(1,6) if i!=3])
    b=random.choice([i for i in range(1,6) if i!=3])
    if a==b==1: a=a+random.randint(1,2)
    noi_dung = f"Cho tam giác ${{{A}{B}{C}}}$ có điểm ${{{M}}}$ là trung điểm của ${{{B}{C}}}$, điểm ${{{G}}}$ là trọng tâm của tam giác. Xét tính đúng-sai của các khẳng định sau. "     
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"*$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{C}{B}}}= \\overrightarrow{{{A}{C}}} $" 
    kq1_F=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{C}{B}}}= \\overrightarrow{{{C}{A}}} $ "
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"$\\overrightarrow{{{A}{B}}}-\\overrightarrow{{{C}{B}}}= \\overrightarrow{{{A}{C}}} $ "
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"*$\\overrightarrow{{{A}{B}}}+\\overrightarrow{{{A}{C}}}= 2\\overrightarrow{{{A}{M}}} $ "
    kq2_F=random.choice([f" $\\overrightarrow{{{A}{B}}}+\\overrightarrow{{{A}{C}}}= {k}\\overrightarrow{{{A}{M}}} $", f" $\\overrightarrow{{{A}{B}}}+\\overrightarrow{{{A}{C}}}=\\overrightarrow{{{A}{M}}} $"])
    kq2=random.choice([kq2_T, kq2_F])
    HDG=f"$\\overrightarrow{{{A}{B}}}+\\overrightarrow{{{A}{C}}}= 2\\overrightarrow{{{A}{M}}} $"
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $\\overrightarrow{{{A}{G}}}= {phan_so(1/3)} \\overrightarrow{{{A}{C}}}+ {phan_so(1/3)}   \\overrightarrow{{{A}{B}}} $" 
    kq3_F=f"$\\overrightarrow{{{A}{G}}}= {phan_so(a/3)}  \\overrightarrow{{{A}{C}}}+ {phan_so(b/3)} \\overrightarrow{{{A}{B}}} $ "
    kq3=random.choice([kq3_T, kq3_F])

    HDG=(f"$\\overrightarrow{{{A}{G}}}  ={phan_so(2/3)} \\overrightarrow{{{A}{M}}}  = {phan_so(2/3)} \\left( {phan_so(1/2)}\\overrightarrow{{{A}{C}}}+{phan_so(1/2)}\\overrightarrow{{{A}{B}}} \\right)  "
    f"= {phan_so(1/3)}\\overrightarrow{{{A}{C}}}+ {phan_so(1/3)}\\overrightarrow{{{A}{B}}} $")
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"*Điểm ${{{I}}}$ thoả mãn hệ thức $\\overrightarrow{{{I}{B}}}+\\overrightarrow{{{I}{C}}}+ 4\\overrightarrow{{{I}{A}}} =\\overrightarrow{{0}}$ là trung điểm của đoạn ${{{A}{G}}}$  "
    kq4_F=random.choice([f"Điểm ${{{I}}}$ thoả mãn hệ thức $\\overrightarrow{{{I}{B}}}+\\overrightarrow{{{I}{C}}}+ 4\\overrightarrow{{{I}{A}}} =\\overrightarrow{{0}}$ là trung điểm của đoạn ${{{M}{G}}}$", f"Điểm ${{{I}}}$ thoả mãn hệ thức $\\overrightarrow{{{I}{B}}}+\\overrightarrow{{{I}{C}}}+ 4\\overrightarrow{{{I}{A}}} =\\overrightarrow{{0}}$ là trung điểm của đoạn ${{{A}{M}}}$", f"Điểm ${{{I}}}$ thoả mãn hệ thức $\\overrightarrow{{{I}{B}}}+\\overrightarrow{{{I}{C}}}+ 4\\overrightarrow{{{I}{A}}} =\\overrightarrow{{0}}$ là trọng tâm của tam giác ${{{A}{B}{M}}}$" ]) 
    kq4=random.choice([kq4_T, kq4_F])
    HDG=(f" $\\overrightarrow{{{I}{B}}}+\\overrightarrow{{{I}{C}}}+ {{4}}\\overrightarrow{{{I}{A}}} =\\overrightarrow{{0}}$ \n\n "
        f"$2\\overrightarrow{{{I}{M}}}+ {{4}}\\overrightarrow{{{I}{A}}} =\\overrightarrow{{0}}$\n\n "
        f" $\\overrightarrow{{{I}{M}}}={{-2}}\\overrightarrow{{{I}{A}}} $ \n\n"
        f" Vậy ${{{I}}}$ là trung điểm của đoạn ${{{A}{G}}}$.")
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




#[D10_C2_B2_06]-M3. Tìm m để hệ bất phương trình vô nghiệm
def D10_C2_B2_06():

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
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan



#[D10_C3_B2_17]-TL-M4. Tìm m để phương trình f(|x|)=m có nhiều nghiệm nhất
def D10_C3_B2_17():
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
        f"\\shortans[oly]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an    




#[D10_C3_B2_18]-TF-M4. Tìm m để phương trình f(|x|)=m có nghiệm thoả đk  
def D10_C3_B2_18():
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
    
    kq3_T=f"*Đỉnh của ${{(P)}}$ có toạ độ là $({phan_so( (x1+x2)/2)}; {phan_so(u)})$" 
    kq3_F=f"Đỉnh của ${{(P)}}$ có toạ độ là $({phan_so( (x1-x2)/2)}; {phan_so(u)})$ "
    kq3=random.choice([kq3_T, kq3_F])
    HDG=f"Đỉnh của ${{(P)}}$ có toạ độ là $({phan_so( (x1+x2)/2)}; {phan_so(u)})$ "
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

    kq1_T=f"* ${{P}}$ đi qua điểm có toạ độ $({x3}; {phan_so(f)})$" 
    kq1_F=f"${{P}}$ đi qua điểm có toạ độ $({x3}; {phan_so(f+1)})$"
    kq1=random.choice([kq1_T, kq1_F])
    HDG=f"${{P}}$ đi qua điểm có toạ độ $({x3}; {phan_so(f)})$ "
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

#[D10_C3_B2_19]-TL-M3. Tính chiều cao của cổng Parabol
def D10_C3_B2_19():
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
        f"\\shortans[oly]{{${{{kq}}}$}}\n\n"\
            f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    dap_an= kq
    return debai_word, loigiai_word, latex_tuluan, dap_an    


