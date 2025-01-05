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

#[D12_C6_B1_05]-M2. Tính xác suất người mua sản phẩm trên độ tuổi nào đó.
def newy25_L12_C6_B1_05():
    phu_nu=random.choice(["phụ nữ", "đàn ông", "người đã có gia đình", "nam giới", "nữ giới", "người độc thân"])
    a=random.randint(35,65)
    tile_phunu=a/100    
    st_tile_phunu=f"{round(tile_phunu,2):.2f}".replace(".",",")

    b=a-random.randint(5,15)
    tile_tren_tuoi=(b)/100
    st_tile_tren_tuoi=f"{round(tile_tren_tuoi,2):.2f}".replace(".",",")

    do_tuoi=random.randint(35,50)

    san_pham=random.choice(["máy lọc nước", "đồng hồ thể thao đa năng", "thức ăn dinh dưỡng cho chó mèo", "balo du lịch",
    "ghế massage toàn thân", "thực phẩm hữu cơ cao cấp"])
    noi_dung=(
    f"Một công ty bán {san_pham} nhận thấy có ${a}\\%$ số người mua hàng là {phu_nu} và"
    f" có ${b}\\%$ số người mua hàng là {phu_nu} trên {do_tuoi} tuổi."
    f" Biết một người mua {san_pham} là {phu_nu}, tính xác suất để người đó trên {do_tuoi} tuổi."
    )
    

    kq=b/a
    kq_false=[
    b/(a+random.randint(1,5)),
    (100-a)/100,
    (100-b)/100]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    noi_dung_loigiai=(
    f'Gọi A là biến cố "Người mua {san_pham} là {phu_nu},'
    f' B là biến cố "Người mua {san_pham} trên {do_tuoi} tuổi.'
    f"Ta cần tính $P(B|A)$.\n\n"
    f"Do có ${a}\\%$ người mua {san_pham} là {phu_nu} nên P(A) = {st_tile_phunu}.\n\n"
    f"Do có ${b}\\%$ số người mua {san_pham} là {phu_nu} trên {do_tuoi} tuổi nên $P(AB) = {st_tile_tren_tuoi}$.\n\n"
    f"Vậy $P(A|B)=\\dfrac{{P(AB)}}{{P(A)}}=\\dfrac{{{st_tile_tren_tuoi}}}{{{st_tile_phunu}}}={phan_so(b/a)}$"
    )

    pa_A= f"* ${phan_so(kq)}$"
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

#[D12_C6_B1_06]-M2. Cho P(A),P(B) và P(A|B). Tính xác suất P(ngang(A)B)
def newy25_L12_C6_B1_06():
    p_a=random.randint(10,80)/100
    st_p_a=f"{round(p_a,2):.2f}".replace(".",",")

    p_b=random.randint(10,80)/100
    while p_b==p_a:
        p_b=random.randint(10,80)/100        
    st_p_b=f"{round(p_b,2):.2f}".replace(".",",")

    p_a_dk_b=random.randint(30,60)/100
    st_p_a_dk_b=f"{round(p_a_dk_b,2):.2f}".replace(".",",")

    noi_dung=(
    f"Cho hai biến cố ${{A}}$ và ${{B}}$ có $P(A)={st_p_a}, P(B)={st_p_b}, P(A|B)= {st_p_a_dk_b}$. Tính $P(\\overline{{A}}B)$."
    )
        

    p_ab=p_b*p_a_dk_b
    st_p_ab=f"{round_half_up(p_ab,2):.2f}".replace(".",",")

    kq=p_b-p_ab
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    kq_false=[
    p_ab,
    p_a*p_b,
    p_a*p_a_dk_b,
    p_a*p_b*p_a_dk_b
    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    st_kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    st_kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    st_kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    noi_dung_loigiai=(
    f"Theo công thức nhân xác suất, ta có $P(AB) = P(B)P(A|B) = {st_p_b}.{st_p_a_dk_b}={st_p_ab}$.\n\n"
    f"Vì $\\overline{{A}}B$ và ${{AB}}$ là hai biên cố xung khắc và $\\overline{{A}}B \\cup AB=B$ nên:\n\n"
    f"$P(\\overline{{A}}B)=P(B)-P(AB)={st_kq}$."
    )

    pa_A= f"*${{{st_kq}}}$"
    pa_B= f"${{{st_kq2}}}$"
    pa_C= f"${{{st_kq3}}}$"
    pa_D= f"${{{st_kq4}}}$"
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

#[D12_C6_B1_07]-SA-M3. Cho P(A),P(B) và P(A|B). Tính xác suất P(ngang(A)|B)
def newy25_L12_C6_B1_07():

    p_a=random.randint(10,80)/100
    st_p_a=f"{round(p_a,2):.2f}".replace(".",",")

    b=random.randint(50,80)
    p_b=b/100
    while p_b==p_a:
        p_b=random.randint(10,80)/100        
    st_p_b=f"{round(p_b,2):.2f}".replace(".",",")

    p_ab=(b-random.randint(5,30))/100
    st_p_ab=f"{round(p_ab,2):.2f}".replace(".",",")

    p_a_dk_b=p_ab/p_b
    st_p_a_dk_b=f"{round(p_a_dk_b,2):.2f}".replace(".",",")


    noi_dung=(
    f"Cho hai biến cố ${{A}}$ và ${{B}}$ có $P(A)={st_p_a}, P(B)={st_p_b}, P(AB)= {st_p_ab}$. Tính $P(\\overline{{A}}|B)$ (kết quả làm tròn đến hàng phần trăm)."
    )
        

    p_ab=p_b*p_a_dk_b
    st_p_ab=f"{round_half_up(p_ab,2):.2f}".replace(".",",")

    p_ngang_a_b=p_b-p_ab

    st_p_ngang_a_b=f"{round_half_up(p_ngang_a_b,2):.2f}".replace(".",",")

    p_ngang_a_dk_b=1-p_a_dk_b
    dap_an=f"{round_half_up(p_ngang_a_dk_b,2):.2f}".replace(".",",")

    

    noi_dung_loigiai=(
    f"Ta có $P(A|B) = \\dfrac{{P(AB)}}{{P(B) }} = \\dfrac{{{st_p_ab} }}{{{st_p_b}}}={st_p_a_dk_b}$.\n\n"
    
    f"$P(\\overline{{A}}|B)=1-P(A|B)=1-{st_p_a_dk_b}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B1_08]-TF-M3. Cho tỉ lệ % mua hàng thỏa mãn 2 biến cố A,B. Xét Đ-S: P(ngang(A)), P(B|A), P(AB), P(ngang(A)ngang(B))
def newy25_L12_C6_B1_08():
    sp_chung=["máy lọc nước", "đồng hồ", "xe máy", "balo",
    "ghế massage", "xe ô tô"]

    sp_rieng=["máy lọc nước RO", "đồng hồ thể thao đa năng" ,"xe tay ga", "balo du lịch",
     "ghế massage nhiệt hồng ngoại", "xe ô tô số tự động"  ]

    i=random.randint(0,len(sp_chung))
    sp_chung,sp_rieng=sp_chung[i], sp_rieng[i]

    if sp_chung=="máy lọc nước":
        sp_rieng=random.choice(["máy lọc nước RO", "máy lọc nước Nano", "máy lọc nước điện phân" ])

    if sp_chung=="đồng hồ":
        sp_rieng=random.choice(["đồng hồ thông minh", "đồng hồ cơ", "đồng hồ thể thao đa năng"])

    if sp_chung=="ghế massage":
        sp_rieng=random.choice(["ghế massage nhiệt hồng ngoại", "ghế massage văn phòng", "ghế massage cho người cao tuổi", "ghế massage thông minh (AI)"])
   
    a=random.randint(55,70)
    p_a=a/100
    st_p_a=f"{round_half_up(a/100,2)}".replace(".",",")
    st_p_ngang_a=f"{round_half_up(1-a/100,2)}".replace(".",",")

    b=random.randint(10,20)
    p_b=b/100
    st_p_b=f"{round_half_up(b/100,2)}".replace(".",",")

    b_dk_a=random.randint(5,15)
    p_b_dk_a=b_dk_a/100

    st_p_b_dk_a=f"{round_half_up(b_dk_a/100,2)}".replace(".",",")
    st_p_b_dk_a_false=f"{round_half_up(1-b_dk_a/100,2)}".replace(".",",")

    noi_dung = (f"Một công ty kinh doanh {sp_chung} sau khi kiểm tra nhóm khách hàng mua sản phẩm của mình đã thu thập được các thông tin sau:\n\n"
        f" - Tất cả khách hàng đều mua ít nhất một chiếc {sp_chung}.\n\n"
        f" - Có ${a}\\%$ khách hàng mua nhiều hơn một chiếc {sp_chung}.\n\n"
        f" - Có ${b}\\%$ khách hàng mua {sp_rieng}.\n\n"
        f" Trong số những khách hàng mua nhiều hơn một chiếc {sp_chung}, có ${b_dk_a}\\%$ mua {sp_rieng}.\n\n"
        f' Gọi A là biến cố: "Khách hàng mua nhiều hơn một chiếc {sp_chung}".\n\n'
        f' Gọi B là biến cố: "Khách hàng mua {sp_rieng}".\n\n'
        f" Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần trăm):")  
      
    
    kq1_T=f"* $P(\\overline{{A}})={st_p_ngang_a}$" 
    kq1_F=f"$P(\\overline{{A}})={st_p_a}$"
    
    HDG=f"Do có ${a}\\%$ khách hàng mua nhiều hơn một chiếc {sp_chung} nên $P(A)={st_p_a}$ và $P(\\overline{{A}})={st_p_ngang_a}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq2_T=f"* $P(B|A)={st_p_b_dk_a}$"
    kq2_F=f" $P(B|A)={st_p_b_dk_a_false}$"
    
    HDG=f"Do trong số những khách hàng mua nhiều hơn một chiếc {sp_chung}, có ${b_dk_a}\\%$ mua {sp_rieng} nên $P(B|A)={st_p_b_dk_a}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_ab=p_b_dk_a*p_a
    st_p_ab=f"{round_half_up(p_ab,2)}".replace(".",",")
    st_p_ab_false=f"{round_half_up(1-p_ab,2)}".replace(".",",")


    kq3_T=f"* $P(AB)={st_p_ab}$" 
    kq3_F=f"$P(AB)={st_p_ab_false}$"
    
    HDG=f"Áp dụng công thức nhân xác suất: $P(AB)=P(B|A).P(A)={st_p_b_dk_a}.{st_p_a}={st_p_ab}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_ngang_a_ngang_b=1-p_a-p_b+p_ab    
    st_p_ngang_a_ngang_b=f"{round_half_up(p_ngang_a_ngang_b,2)}".replace(".",",")

    p_ngang_a_ngang_b_false=1-p_a-p_b
    st_p_ngang_a_ngang_b_false=f"{round_half_up(p_ngang_a_ngang_b_false,2)}".replace(".",",")

    kq4_T=f"* Xác suất một khách hàng chỉ mua đúng một chiếc {sp_chung} và chiếc {sp_chung} đó không phải là {sp_rieng} bằng {st_p_ngang_a_ngang_b}"
    kq4_F=f"Xác suất một khách hàng chỉ mua đúng một chiếc {sp_chung} và chiếc {sp_chung} đó không phải là {sp_rieng} bằng {st_p_ngang_a_ngang_b_false}" 
    
    HDG=(f"Xác suất một khách hàng chỉ mua đúng một chiếc {sp_chung} và chiếc {sp_chung} đó không phải là {sp_rieng} bằng:\n\n"
        f"$P(\\overline{{A}}\\overline{{B}})=1-P(A\\cup B)=1-P(A)-P(B)+P(AB)=1-{st_p_a}-{st_p_b}+{st_p_ab}={st_p_ngang_a_ngang_b}$.")
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

#[D12_C6_B1_09]-M1. Nhận dạng công thức xác suất có điều kiện
def newy25_L12_C6_B1_09():
    bien_co=["A","B","C","D","E","F"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    noi_dung=(
    f"Cho  ${{{A},{B}}}$ là các biến cố trong đó $P({B})>0$. Khẳng định nào sau đây đúng"
    )    

    kq=random.choice([
        f"$P({A}|{B})=\\dfrac{{P({A}{B})}}{{P({B})}}$",
        f"$P({A}|{B})=\\dfrac{{P({A}\\cap {B})}}{{P({B})}}$",
        f"$P({A}{B})=P({B})P({A}|{B})$",
        f"$P(\\overline{{{A}}}|{B})=\\dfrac{{P(\\overline{{{A}}}{B})}}{{P({B})}}$",
        f"$P(\\overline{{{A}}}|{B})=1-P({A}|{B})$"
        ])
    kq_false=[
    f"$P({A}|{B})=\\dfrac{{P({A}\\cup {B})}}{{P({B})}}$",
    f"$P({A}|{B})=\\dfrac{{P({B})}}{{P({A}{B})}}$",
    f"$P({A}|{B})=P({A})-P({B})$",
    f"$P({A}{B})=P({A})P({B})$",
    f"$P({A}{B})=1-P({A}|{B})$",
    f"$P(\\overline{{{A}}}|{B})=P({A}|{B})$",
    f"$P(\\overline{{{A}}}|{B})=P({A}|\\overline{{{B}}})$",

    ]
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    noi_dung_loigiai=(
    f"{kq} là khẳng định đúng. "
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

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an