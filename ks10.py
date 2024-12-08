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
    
    









