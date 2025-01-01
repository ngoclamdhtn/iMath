import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
from decimal import Decimal, ROUND_HALF_UP
# Hàm làm tròn half-up
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

#[D12_C6_B1_01]-M2. Lấy lần lượt 2 bi. Tính xác suất để viêb thứ 2 màu x biết viên thứ 1 màu y.
def newy25_L12_C6_B1_01():
    mau=["màu xanh", "màu đỏ", "màu vàng", "màu đen", "màu trắng", "màu nâu", "màu hồng"]
    random.shuffle(mau)
    mau_do, mau_xanh=mau[0:2]
    n_do=random.randint(5,15)
    n_xanh=random.randint(5,15)
    if n_xanh==n_do:n_xanh=n_xanh+1
    n=n_do+n_xanh

    noi_dung=(
    f"Một hộp có ${{{n}}}$ viên bi cùng kích thước và khối lượng, trong đó có ${{{n_do}}}$ viên bi {mau_do} và ${{{n_xanh}}}$ viên bi {mau_xanh}."
    f" Lấy ngẫu nhiên lần lượt ${{2}}$ viên bi và không hoàn lại. "
    f"Tính xác suất để lấy được viên bi thứ hai có {mau_xanh}, biết rằng viên bi thứ nhất có {mau_do}."
    )
    

    kq=n_xanh/(n-1)
    kq_false=[
    n_xanh/n,
    n_xanh/(n-2),
    n_do/(n-1)
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f'Gọi A là biến cố "Lấy được viên bi thứ hai có {mau_xanh}";\n\n'
    f'Gọi B là biến cố "Lấy được viên bi thứ nhất có {mau_do}";\n\n'
    f'Khi đó xác suất để lấy được viên bi thứ hai có {mau_xanh}, biết rằng viên bi thứ nhất có {mau_do}'
    f'chính là xác suất của A với điều kiện B.\n\n'
    f'Vì một viên bi {mau_do} đã được lấy ra ở lần thứ nhất nên trong hộp còn lại ${{{n-1}}}$ viên bi, trong đó có ${{{n_xanh}}}$ viên bi xanh.\n\n'
    f" Xác suất cần tính là: $P=\\dfrac{{{n_xanh}}}{{{n-1}}}={phan_so(n_xanh/(n-1))}$.\n\n"
    f"$P={phan_so(n_xanh/(n-1))}$."

    )

    pa_A= f"*${phan_so(kq)}$"
    pa_B= f"${phan_so(kq2)}$"
    pa_C= f"${phan_so(kq3)}$"
    pa_D= f"${phan_so(kq4)}$"
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

#[D12_C6_B1_02]-M2. Tính xác suất người biết chơi môn X biết răng người đó chơi được môn Y
def newy25_L12_C6_B1_02():
    mon=["cờ tướng", "cờ vua", "bóng bàn", "cầu lông", "bóng chuyền", "bóng đá", "đá cầu"]
    random.shuffle(mon)
    co_vua, co_tuong=mon[0:2]

    n_cahai = random.randint(5,10)
    n_co_vua=random.randint(9,15) + n_cahai
    n_co_tuong=random.randint(9,15) + n_cahai
    if n_co_vua==n_co_tuong: n_co_tuong = n_co_tuong + random.randint(1,2)

    n=n_co_vua+n_co_tuong-n_cahai

    noi_dung=(
    f"Câu lạc bộ thể thao của nhà trường gồm ${{{n}}}$ thành viên, mỗi thành viên biết chơi ít nhất một trong hai môn {co_vua} hoặc {co_tuong}."
    f" Biết rằng có ${{{n_co_vua}}}$ thành viên biết chơi {co_vua} và ${{{n_co_tuong}}}$ thành viên biết chơi {co_tuong}."
    f" Chọn ngẫu nhiên 1 thành viên của câu lạc bộ."
    f" Tính xác suất thành viên được chọn biết chơi {co_vua}, biết rằng thành viên đó biết chơi {co_tuong}."
    )
    

    kq=n_cahai/n_co_tuong
    kq_false=[
    n_cahai/n_co_vua,
    n_cahai/n,
    n_co_tuong/n,
    n_co_vua/n
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f'Gọi A là biến cố "Thành viên được chọn biết chơi {co_tuong}" và B là biến cố "Thành viên được chọn biết chơi {co_vua}".\n\n'
    f'Số thành viên của câu lạc bộ biết chơi cả hai môn là: ${n_co_vua}+{n_co_tuong}-{n}={n_cahai}.$\n\n'
    f'Do đó, trong số ${{{n_co_tuong}}}$ thành viên biết chơi {co_tuong}, có đúng ${{{n_cahai}}}$ thành viên biết chơi {co_vua}.\n\n'
    f'Vậy nên xác suất thành viên được chọn biết chơi {co_vua}, biết rằng thành viên đó biết chơi {co_tuong} là:\n\n'
    f'$P(B|A)=\\dfrac{{{n_cahai}}}{{{n_co_tuong}}}$.\n\n'
    f'$P(B|A)={phan_so(n_cahai/n_co_tuong)}$.'
    )

    pa_A= f"*${phan_so(kq)}$"
    pa_B= f"${phan_so(kq2)}$"
    pa_C= f"${phan_so(kq3)}$"
    pa_D= f"${phan_so(kq4)}$"
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

#[D12_C6_B1_03]-M2. Tính xác suất A lấy được bi màu x biết B lấy được bi màu x.
def newy25_L12_C6_B1_03():
    mau=["bi xanh", "bi đỏ", "bi vàng", "bi đen", "bi trắng"]
    random.shuffle(mau)
    bi_den,bi_trang=mau[0:2]

    ten=["Bình", "An", "Trung", "Dũng", "Hạnh", "Phúc", "Minh", "Phương", "Hương", "Linh"]
    random.shuffle(ten)
    Binh, An=ten[0:2]

    n_den=random.randint(10,20)
    n_trang=random.randint(10,20)
    if n_den==n_trang: n_den=n_den+random.randint(1,3)

    n=n_den+n_trang

    noi_dung=(
    f"Một hộp có ${{{n_trang}}}$ viên {bi_trang} và ${{{n_den}}}$ viên {bi_den}, các viên bi có cùng kích thước và khối lượng."
    f" Bạn {Binh} lấy ngẫu nhiên một viên bi trong hộp, không trả lại."
    f" Sau đó bạn {An} lấy ngẫu nhiên một viên bi trong hộp đó."
    f" Gọi A là biến cố: “{An} lấy được viên {bi_trang}”; B là biến cố: “{Binh} lấy được viên {bi_trang}”"
    f" Tính $P(A|B)$."
    )
    

    kq=(n_trang-1)/(n-1)
    kq_false=[(n_trang)/(n-1),
    (n_trang-1)/n,
    (n_trang-1)/(n-2),
    (n_trang-2)/(n-1)
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"B xảy ra tức là {Binh} lấy được viên {bi_trang}.\n\n"
    f"Khi đó trong hộp còn lại ${{{n-1}}}$ viên bi với ${{{n_trang-1}}}$ viên {bi_trang} và ${{{n_den}}}$ viên {bi_den}."
    f"Xác suất cần tính là: $P(A|B)=\\dfrac{{{n_trang-1}}}{{{n-1}}}$.\n\n"
    f"$P(A|B)={phan_so((n_trang-1)/(n-1))}$."
    )

    pa_A= f"*${phan_so(kq)}$"
    pa_B= f"${phan_so(kq2)}$"
    pa_C= f"${phan_so(kq3)}$"
    pa_D= f"${phan_so(kq4)}$"
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

#[D12_C6_B1_04]-M2. Hộp I và II đều chứa 2 loại bi. Lấy 1 bi từ hộp I bỏ vào hộp II. Lấy tiếp 1 bi hộp II. Tính xác suất.
def newy25_L12_C6_B1_04():
    mau=["bi xanh", "bi đỏ", "bi vàng", "bi đen", "bi trắng"]
    random.shuffle(mau)
    bi_xanh,bi_do=mau[0:2]

    ten=["Bình", "An", "Trung", "Dũng", "Hạnh", "Phúc", "Minh", "Phương", "Hương", "Linh"]
    random.shuffle(ten)
    Thanh=ten[0]

    n_xanh_1=random.randint(5,10)
    n_do_1=random.randint(5,10)
    if n_xanh_1==n_do_1:
        n_xanh_1=n_xanh_1+random.randint(1,2)

    n_xanh_2=random.randint(5,10)
    n_do_2=random.randint(5,10)
    if n_xanh_2==n_do_2:
        n_xanh_2=n_xanh_2+random.randint(1,2) 

    noi_dung=(
    f"Hộp thứ nhất chứa ${{{n_xanh_1}}}$ viên {bi_xanh} và ${{{n_do_1}}}$ {bi_do}."
    f" Hộp thứ hai chứa ${{{n_xanh_2}}}$ viên {bi_xanh} và ${{{n_do_2}}}$ {bi_do}."
    f" Các viên bi có cùng kích thước và khối lượng."
    f" Bạn {Thanh} lấy ra ngẫu nhiên 1 viên bi từ hộp thứ nhất bỏ vào hộp thứ hai, sau đó lại lấy ra ngẫu nhiên 1 viên bi từ hộp thứ hai."
    f" Tính xác suất để viên bi lấy ra ở lần thứ hai là viên {bi_do}, biết viên bi lấy ra ở lần thứ nhất là viên {bi_xanh}."   
    )
    
    n=n_xanh_2+1+n_do_2
    kq=(n_do_2)/n
    kq_false=[
    (n_do_2)/(n-1),
    (n_xanh_2)/n,
    (n_do_2)/(n-2),
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    noi_dung_loigiai=(
    f"A là biến cố: “viên bi lấy ra ở lần thứ hai là viên {bi_do}”; B là biến cố: “viên bi lấy ra ở lần thứ nhất là viên {bi_xanh}.\n\n"
    f"Biến cố B xảy ra, nghĩa là lần thứ nhất lấy 1 viên {bi_xanh} và bỏ vào hộp thứ hai."
    f" Khi đó trong hộp thứ hai sẽ có ${{{n_xanh_2+1}}}$ viên {bi_xanh} và {n_do_2} viên {bi_do}.\n\n"
    f"Xác suất cần tính là: $P(A|B)=\\dfrac{{{n_do_2}}}{{{n}}}$.\n\n"
    f"$P(A|B)={phan_so((n_do_2)/n)}$."
    )

    pa_A= f"*${phan_so(kq)}$"
    pa_B= f"${phan_so(kq2)}$"
    pa_C= f"${phan_so(kq3)}$"
    pa_D= f"${phan_so(kq4)}$"
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