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

    i=random.randint(0,len(sp_chung)-1)
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

#Bài 2: Công thức xác suất toàn phần
#[D12_C6_B2_01]-SA-M2. Cho P(B), P(A|B), P(A|B_ngang). Tính P(A)
def newy25_L12_C6_B2_01():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    b=random.randint(55,70)
    p_b=b/100
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    p_b_ngang=1-p_b
    st_p_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")


    a_dk_b=random.randint(5,20)
    p_a_dk_b=a_dk_b/100
    st_p_a_dk_b=f"{round_half_up(p_a_dk_b,2)}".replace(".",",")

    a_dk_b_ngang=random.randint(45,75)
    p_a_dk_b_ngang=a_dk_b_ngang/100
    st_p_a_dk_b_ngang=f"{round_half_up(p_a_dk_b_ngang,2)}".replace(".",",")

    noi_dung = (
    f"Cho hai biến cố ${{{A}}}$, ${{{B}}}$ với $P({B})={st_p_b}$; $P({A}|{B}) ={st_p_a_dk_b}$ và $P\\left({A}|\\overline{{{B}}}\\right)={st_p_a_dk_b_ngang}$."
    f" Tính $P({A})$ (kết quả làm tròn đến hàng phần trăm)."
    )
    dap_an=p_a_dk_b*p_b+p_a_dk_b_ngang*p_b_ngang
    dap_an=f"{round_half_up(dap_an,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f"Ta có: $P(\\overline{{{B}}})=1-P({B})={st_p_b_ngang}$.\n\n"
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P({A}) = P({A}|{B}). P({B}) + P\\left({A}|\\overline{{{B}}}\\right).P\\left(\\overline{{{B}}}\\right)$"
    f"$={st_p_a_dk_b}.{st_p_b}+{st_p_a_dk_b_ngang}.{st_p_b_ngang}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_02]-SA-M2. Bài toán thực tế có P(A), P(B|A), P(B|A_). Tính P(B)
def newy25_L12_C6_B2_02():
    a=random.randint(55,80)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    p_a_ngang=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")

    b_dk_a=random.randint(30,45)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(65,85)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    dap_an=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    dap_an=f"{round_half_up(dap_an,2):.2f}".replace(".",",")
    chon=random.randint(1,8)

    if chon==1:
        noi_dung = (
            f"Số khán giả đến xem buổi biểu diễn ca nhạc ngoài trời phụ thuộc vào thời tiết."
            f" Giả sử, nếu trời không mưa thì xác suất để bán hết vé là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu trời mưa thì xác suất để bán hết vé chỉ là ${{{st_p_b_dk_a}}}$. "
            f"Dự báo thời tiết cho thấy xác suất để trời mưa vào buổi biểu diễn là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để nhà tổ chức sự kiện bán hết vé? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Trời mưa", ${{B}}$ là biến cố "Bán hết vé".\n\n')


    if chon==2:
        noi_dung = (
            f"Một nhà hàng hải sản phục vụ ngoài trời phụ thuộc vào thời tiết."
            f" Giả sử, nếu trời không mưa thì xác suất để khách ngồi kín các bàn là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu trời mưa thì xác suất để khách ngồi kín các bàn chỉ là ${{{st_p_b_dk_a}}}$. "
            f"Dự báo thời tiết cho thấy xác suất để trời mưa vào ngày mai là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để nhà hàng kín chỗ vào ngày mai? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Trời mưa", ${{B}}$ là biến cố "Khách ngồi kín các bàn".\n\n')

    if chon==3:
        noi_dung = (
            f"Một công ty vận tải đánh giá xác suất giao hàng đúng hạn phụ thuộc vào tình trạng giao thông."
            f" Nếu đường thông thoáng, xác suất giao đúng hạn là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu đường tắc, xác suất này giảm xuống còn ${{{st_p_b_dk_a}}}$. "
            f"Dữ liệu giao thông cho thấy xác suất xảy ra ùn tắc vào ngày giao hàng là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để hàng được giao đúng hạn? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Đường bị tắc", ${{B}}$ là biến cố "Hàng được giao đúng hạn".\n\n')

    if chon==4:
        noi_dung = (
            f"Năng suất thu hoạch nông sản của một nông trại phụ thuộc vào điều kiện thời tiết."
            f" Nếu trời thuận lợi, xác suất để đạt năng suất cao là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu thời tiết xấu, xác suất này giảm xuống còn ${{{st_p_b_dk_a}}}$. "
            f"Theo dự báo, xác suất thời tiết xấu trong mùa thu hoạch là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để nông trại đạt năng suất cao? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Thời tiết xấu", ${{B}}$ là biến cố "Đạt năng suất cao".\n\n')

    if chon==4:
        noi_dung = (
            f"Tỷ lệ học sinh đạt điểm cao trong một kỳ thi chịu ảnh hưởng bởi mức độ khó của đề thi."
            f" Nếu đề thi dễ, xác suất học sinh đạt điểm cao là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu đề thi khó, xác suất này giảm xuống còn ${{{st_p_b_dk_a}}}$. "
            f"Theo phân tích, xác suất đề thi khó là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để một học sinh bất kỳ đạt điểm cao trong kỳ thi? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Đề thi khó", ${{B}}$ là biến cố "các học sinh đạt điểm cao".\n\n')

    if chon==5:
        noi_dung = (
            f"Một cửa hàng điện thoại bán chạy hơn vào dịp cuối tuần."
            f" Nếu hôm đó là cuối tuần, xác suất để bán hết số điện thoại nhập về là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu là ngày trong tuần, xác suất này chỉ là ${{{st_p_b_dk_a}}}$. "
            f"Xác suất để một ngày bất kỳ trong tháng là cuối tuần là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để cửa hàng bán hết số điện thoại nhập về trong một ngày bất kỳ? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Ngày trong tuần", ${{B}}$ là biến cố "Bán hết số điện thoại nhập về".\n\n')

    if chon==6:
        noi_dung = (
            f"Một nhà máy sản xuất linh kiện điện tử có tỷ lệ sản phẩm đạt tiêu chuẩn phụ thuộc vào nguồn nguyên liệu."
            f" Nếu nguyên liệu đầu vào là loại tốt, xác suất sản phẩm đạt tiêu chuẩn là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu nguyên liệu loại trung bình, xác suất này giảm xuống còn ${{{st_p_b_dk_a}}}$. "
            f"Nhà máy nhập nguyên liệu từ hai nguồn với tỷ lệ nguyên liệu tốt chiếm ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để một sản phẩm bất kỳ đạt tiêu chuẩn? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Nguyên liệu loại trung bình", ${{B}}$ là biến cố "Sản phẩm bất kỳ đạt tiêu chuẩn".\n\n')

    if chon==7:
        noi_dung = (
            f"Hiệu quả của một loại thuốc điều trị bệnh phụ thuộc vào phản ứng của bệnh nhân."
            f" Nếu bệnh nhân không có cơ địa kháng thuốc, xác suất thuốc có hiệu quả là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu bệnh nhân có cơ địa kháng thuốc, xác suất này chỉ là ${{{st_p_b_dk_a}}}$. "
            f"Theo thống kê, xác suất một bệnh nhân có cơ địa kháng thuốc là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để thuốc có hiệu quả trên một bệnh nhân bất kỳ? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Bệnh nhân có cơ địa kháng thuốc", ${{B}}$ là biến cố "Thuốc có hiệu quả".\n\n')

    if chon==8:
        noi_dung = (
            f"Một hệ thống máy chủ có nguy cơ bị quá tải trong giờ cao điểm."
            f" Nếu không bị quá tải, xác suất xử lý yêu cầu thành công là ${{{st_p_b_dk_a_ngang}}}$; "
            f"còn nếu bị quá tải, xác suất này chỉ là ${{{st_p_b_dk_a}}}$. "
            f"Theo số liệu theo dõi, xác suất xảy ra tình trạng quá tải trong một khoảng thời gian bất kỳ là ${{{st_p_a_ngang}}}$. "
            f"Tính xác suất để một yêu cầu gửi đến hệ thống được xử lý thành công? (kết quả làm tròn đến hàng phần trăm)")
        noi_dung_loigiai=(
            f'Gọi ${{A}}$ là biến cố "Hệ thống máy chủ bị quá tải", ${{B}}$ là biến cố "Một yêu cầu gửi đến hệ thống được xử lý thành công".\n\n')  

    
    

    noi_dung_loigiai+=(    
    f"$P(\\overline{{A}})={st_p_a_ngang}, P(B|A)={st_p_b_dk_a}, P(B|\\overline{{A}})={st_p_b_dk_a_ngang}$.\n\n"
    f"Xác suất cần tìm: \n\n"
    f"$P(B)=P(A).P(B|A)+P(\\overline{{A}}).P(B|\\overline{{A}})={st_p_a}.{st_p_b_dk_a}+{st_p_a_ngang}.{st_p_b_dk_a_ngang}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_03]-SA-M2. Xác suất toàn phần: Tính xác suất đậu đại học khi chọn khối.
def newy25_L12_C6_B2_03():
    a=random.randint(60,85)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")


    p_a_ngang=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")

    b_dk_a=random.randint(50,75)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    while True:
        b_dk_a_ngang=random.randint(50,75)
        if b_dk_a_ngang != b_dk_a:
            break
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    dap_an=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    dap_an=f"{round_half_up(dap_an,2):.1f}".replace(".",",")
    
    to_hop_mon = {
    "A00": ["Toán", "Vật lí", "Hóa học"],
    "A01": ["Toán", "Vật lí", "Tiếng Anh"],
    "A02": ["Toán", "Vật lí", "Sinh học"],
    "A03": ["Toán", "Vật lí", "Lịch sử"],
    "A04": ["Toán", "Vật lí", "Địa lí"],
    "B00": ["Toán", "Hóa học", "Sinh học"],
    "B01": ["Toán", "Sinh học", "Lịch sử"],
    "B02": ["Toán", "Sinh học", "Địa lí"],
    "B03": ["Toán", "Sinh học", "Ngữ văn"],
    "C00": ["Ngữ văn", "Lịch sử", "Địa lí"],
    "C01": ["Ngữ văn", "Toán", "Vật lí"],
    "C02": ["Ngữ văn", "Toán", "Hóa học"],
    "D00": ["Toán", "Ngữ văn", "Tiếng Anh"],
    "D01": ["Toán", "Ngữ văn", "Tiếng Anh"],
    "D07": ["Toán", "Hóa học", "Tiếng Anh"]}

    # Lấy danh sách các tổ hợp
    to_hop_list = list(to_hop_mon.keys())

    # Lấy danh sách các môn tương ứng theo từng tổ hợp
    mon_thi_list = list(to_hop_mon.values())
    index_random = random.randint(0, len(to_hop_list) - 1)
    to_hop = to_hop_list[index_random]

    mon_thi = mon_thi_list[index_random]
    mon_thi=", ".join(mon_thi)


    noi_dung = (
    f"Trong một kì thi tốt nghiệp trung học phổ thông, một tỉnh X có ${a} \\%$ học sinh lựa chọn tổ hợp {to_hop} (gồm các môn {mon_thi})."
    f" Biết rằng, nếu một học sinh chọn tổ hợp {to_hop} thì xác suất để học sinh đó đỗ đại học là ${{{st_p_b_dk_a}}}$;"
    f" còn nếu một học sinh không chọn tổ hợp {to_hop} thì xác suất để học sinh đó đỗ đại học là ${{{st_p_b_dk_a_ngang}}}$."
    f" Chọn ngẫu nhiên một học sinh của tỉnh X đã tốt nghiệp trung học phổ thông trong kì thi trên. Tính xác suất để học sinh đó đỗ đại học."
    f"(kết quả làm tròn đến hàng phần trăm)"
    )
    

    noi_dung_loigiai=(
    f"Gọi $A$ là biến cố: Học sinh đó chọn tổ hợp {to_hop}; $B$ là biến cố: Học sinh đó đỗ đại học.\n\n"
    f"$P(A)={st_p_a},P(\\overline{{A}})=1-P(A)={st_p_a_ngang}$.\n\n"
    f"$P(B|A)$ là xác suất để một học sinh đỗ đại học với điều kiện học sinh đó chọn tổ hợp {to_hop}.\n\n"
    f"$\\Rightarrow P(B|A)={st_p_b_dk_a}$.\n\n"
    f"$P(B|\\overline{{A}})$ là xác suất để một học sinh đỗ đại học với điều kiện học sinh đó chọn tổ hợp {to_hop}.\n\n"
    f"$\\Rightarrow P(B|\\overline{{A}})={st_p_b_dk_a_ngang}$.\n\n"
    f"Thay vào công thức xác suất toàn phần ta được:\n\n"
    f"$P(B)=P(A).P(B|A)+P(\\overline{{A}}).P(B|\\overline{{A}})={st_p_a}.{st_p_b_dk_a}+{st_p_a_ngang}.{st_p_b_dk_a_ngang}={dap_an}$."

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_04]-SA-M3. X.S toàn phần: Tính xác suất hái bông hoa.
def newy25_L12_C6_B2_04():
    lop=[]
    for i in range(1,10):
        lop.append(f"12A{i}")
        lop.append(f"11A{i}")
        lop.append(f"10A{i}")
    lop=random.choice(lop)
    
    so_trung=random.randint(5,15)
    tong=so_trung+random.randint(5,10)

    p_b=so_trung/tong
    p_b_ngang=1-p_b
    p_a_dk_b=(so_trung-1)/(tong-1)
    p_a_dk_b_ngang=(so_trung)/(tong-1)
    kq=p_b*p_a_dk_b+p_b_ngang*p_a_dk_b_ngang
    dap_an=f"{round_half_up(kq,2):.2f}".replace(".",",")

    ten=[ "An", "Bảo", "Cường", "Dũng", "Hưng", "Khánh", "Minh", "Phúc", "Quân", "Tuấn", "Anh", "Chi", "Diệu", "Hạnh", "Lan", "Linh", "Mai", "Ngọc", "Thảo", "Vy"]
    A,B = random.sample(ten,2)
    noi_dung = (
    f"Trong trò chơi hái hoa có thưởng của lớp {lop}, cô giáo treo ${{{tong}}}$ bông hoa trên cành cây, trong đó có ${{{so_trung}}}$ bông hoa chứa phiếu có thưởng. Bạn {B} hái bông hoa đầu tiên, sau đó bạn {A} hái bông hoa thứ hai."
    f" Tính xác suất để bạn {A} hái được bông hoa chứa phiếu có thưởng (kết quả làm tròn đến hàng phần trăm)."
    )   
    

    noi_dung_loigiai=(
    f"Xét hai biến cố:\n\n"
    f'"A: Bông hoa bạn {A} hái được chứa phiếu có thưởng."\n\n'
    f'"B: Bông hoa bạn {B} hái được chứa phiếu có thưởng."\n\n'
    f"$P(B)={phan_so(p_b)}, P(\\overline{{B}})=1-P(B)={phan_so(p_b_ngang)}$.\n\n"
    f"$P(A|B)={phan_so(p_a_dk_b)}, P(A|\\overline{{B}})={phan_so(p_a_dk_b_ngang)}$.\n\n"
    f"Xác suất bạn {A} hái được bông hoa chứa phiếu có thưởng:\n\n"
    f"$P(A)=P(B).P(A|B)+P(\\overline{{B}}).P(A|\\overline{{B}})={phan_so(p_b)}.{phan_so(p_a_dk_b)}+{phan_so(p_b_ngang)}.{phan_so(p_a_dk_b_ngang)}={phan_so(kq)}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_05]-SA-M3. X.S toàn phần: Tính xác suất lấy viên bi có màu nào đó.
def newy25_L12_C6_B2_05():
    lop=[]
    for i in range(1,10):
        lop.append(f"12A{i}")
        lop.append(f"11A{i}")
        lop.append(f"10A{i}")
    lop=random.choice(lop)
    
    so_trung=random.randint(5,15)
    tong=so_trung+random.randint(5,10)

    p_b=so_trung/tong
    p_b_ngang=1-p_b
    p_a_dk_b=(so_trung-1)/(tong-1)
    p_a_dk_b_ngang=(so_trung)/(tong-1)
    kq=p_b*p_a_dk_b+p_b_ngang*p_a_dk_b_ngang
    dap_an=f"{round_half_up(kq,2):.2f}".replace(".",",")

    ten=[ "An", "Bảo", "Cường", "Dũng", "Hưng", "Khánh", "Minh", "Phúc", "Quân", "Tuấn", "Anh", "Chi", "Diệu", "Hạnh", "Lan", "Linh", "Mai", "Ngọc", "Thảo", "Vy"]
    A,B = random.sample(ten,2)
    mau=random.choice(["đỏ", "xanh", "vàng", "tím", "trắng", "đen" ])
    noi_dung = (
    f"Một hộp chứa ${{{tong}}}$ viên bi, trong đó có ${{{so_trung}}}$ viên bi màu {mau}. Bạn {B} rút ngẫu nhiên một viên bi trước, sau đó bạn {A} rút một viên bi."
    f" Tính xác suất để bạn {A} rút được một viên bi màu {mau} (kết quả làm tròn đến hàng phần trăm)."
    )   
    

    noi_dung_loigiai=(
    f"Xét hai biến cố:\n\n"
    f'"A: Bạn {A} rút được viên bi màu {mau}."\n\n'
    f'"B: Bạn {B} rút được viên bi màu {mau}."\n\n'
    f"$P(B)={phan_so(p_b)}, P(\\overline{{B}})=1-P(B)={phan_so(p_b_ngang)}$.\n\n"
    f"$P(A|B)={phan_so(p_a_dk_b)}, P(A|\\overline{{B}})={phan_so(p_a_dk_b_ngang)}$.\n\n"
    f"Xác suất bạn {A} rút được viên bi màu {mau}:\n\n"
    f"$P(A)=P(B).P(A|B)+P(\\overline{{B}}).P(A|\\overline{{B}})={phan_so(p_b)}.{phan_so(p_a_dk_b)}+{phan_so(p_b_ngang)}.{phan_so(p_a_dk_b_ngang)}={phan_so(kq)}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_06]-SA-M3. X.S toàn phần: Tính xác suất chọn ly thủy tinh.
def newy25_L12_C6_B2_06():
    lop=[]
    for i in range(1,10):
        lop.append(f"12A{i}")
        lop.append(f"11A{i}")
        lop.append(f"10A{i}")
    lop=random.choice(lop)
    
    so_trung=random.randint(8,15)
    tong=so_trung+random.randint(4,10)

    p_b=so_trung/tong
    p_b_ngang=1-p_b
    p_a_dk_b=(so_trung-1)/(tong-1)
    p_a_dk_b_ngang=(so_trung)/(tong-1)
    kq=p_b*p_a_dk_b+p_b_ngang*p_a_dk_b_ngang
    dap_an=f"{round_half_up(kq,2):.2f}".replace(".",",")

    ten=[ "An", "Bảo", "Cường", "Dũng", "Hưng", "Khánh", "Minh", "Phúc", "Quân", "Tuấn", "Anh", "Chi", "Diệu", "Hạnh", "Lan", "Linh", "Mai", "Ngọc", "Thảo", "Vy"]
    A,B = random.sample(ten,2)
    
    noi_dung = (
    f"Trên kệ có ${{{tong}}}$ chiếc ly, trong đó có ${{{so_trung}}}$ chiếc  còn lại là ly nhựa. Bạn {B} lấy ngẫu nhiên một chiếc ly trước, sau đó đến lượt bạn {A} lấy một chiếc ly."
    f" Tính xác suất để bạn {A} lấy được chiếc ly thủy tinh (kết quả làm tròn đến hàng phần trăm)."
    )   
    

    noi_dung_loigiai=(
    f"Xét hai biến cố:\n\n"
    f'"A: Bạn {A} lấy được chiếc ly thủy tinh."\n\n'
    f'"B: Bạn {B} lấy được chiếc ly thủy tinh."\n\n'
    f"$P(B)={phan_so(p_b)}, P(\\overline{{B}})=1-P(B)={phan_so(p_b_ngang)}$.\n\n"
    f"$P(A|B)={phan_so(p_a_dk_b)}, P(A|\\overline{{B}})={phan_so(p_a_dk_b_ngang)}$.\n\n"
    f"Xác suất bạn {A} lấy được chiếc ly thủy tinh:\n\n"
    f"$P(A)=P(B).P(A|B)+P(\\overline{{B}}).P(A|\\overline{{B}})={phan_so(p_b)}.{phan_so(p_a_dk_b)}+{phan_so(p_b_ngang)}.{phan_so(p_a_dk_b_ngang)}={phan_so(kq)}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_07]-SA-M3. X.S toàn phần: Tính xác suất chọn sách thuộc về 1 thể loại
def newy25_L12_C6_B2_07():
    lop=[]
    for i in range(1,10):
        lop.append(f"12A{i}")
        lop.append(f"11A{i}")
        lop.append(f"10A{i}")
    lop=random.choice(lop)
    
    so_trung=random.randint(8,20)
    tong=so_trung+random.randint(4,10)

    p_b=so_trung/tong
    p_b_ngang=1-p_b
    p_a_dk_b=(so_trung-1)/(tong-1)
    p_a_dk_b_ngang=(so_trung)/(tong-1)
    kq=p_b*p_a_dk_b+p_b_ngang*p_a_dk_b_ngang
    dap_an=f"{round_half_up(kq,2):.2f}".replace(".",",")

    ten=[ "An", "Bảo", "Cường", "Dũng", "Hưng", "Khánh", "Minh", "Phúc", "Quân", "Tuấn", "Anh", "Chi", "Diệu", "Hạnh", "Lan", "Linh", "Mai", "Ngọc", "Thảo", "Vy"]
    A,B = random.sample(ten,2)
    loai_sach=random.choice(["sách Toán", "sách Văn", "sách Tiếng Anh", "Tin học", "truyện cổ tích", "truyện khoa học viễn tưởng" ])
    noi_dung = (
    f"Trên kệ có ${{{tong}}}$ cuốn sách , trong đó có ${{{so_trung}}}$ {loai_sach} khác nhau. Bạn {B} lấy ngẫu nhiên một cuốn sách, sau đó đến lượt bạn {A} lấy một cuốn khác từ kệ."
    f" Tính xác suất để bạn {A} lấy được cuốn {loai_sach} (kết quả làm tròn đến hàng phần trăm)."
    )   
    

    noi_dung_loigiai=(
    f"Xét hai biến cố:\n\n"
    f'"A: Bạn {A} lấy được cuốn {loai_sach}."\n\n'
    f'"B: Bạn {B} lấy được cuốn {loai_sach}."\n\n'
    f"$P(B)={phan_so(p_b)}, P(\\overline{{B}})=1-P(B)={phan_so(p_b_ngang)}$.\n\n"
    f"$P(A|B)={phan_so(p_a_dk_b)}, P(A|\\overline{{B}})={phan_so(p_a_dk_b_ngang)}$.\n\n"
    f"Xác suất bạn {A} lấy được cuốn {loai_sach}:\n\n"
    f"$P(A)=P(B).P(A|B)+P(\\overline{{B}}).P(A|\\overline{{B}})={phan_so(p_b)}.{phan_so(p_a_dk_b)}+{phan_so(p_b_ngang)}.{phan_so(p_a_dk_b_ngang)}={phan_so(kq)}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_08]-SA-M3. X.S Bayes: Tính xác suất sản phẩm kiểm tra từ nhà máy bị lỗi do phân xưởng X sẩn xuất.
def newy25_L12_C6_B2_08():
    p_a=random.randint(40,70)
    p_b=100-p_a
    st_p_a=f"{round_half_up(p_a/100,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_b/100,2)}".replace(".",",")
    while True:
        p_l_dk_a=random.randint(2,10)
        p_l_dk_b=random.randint(2,10)
        if p_l_dk_a!=p_l_dk_b:
            break

    st_p_l_dk_a=f"{round(p_l_dk_a/100,2):.2f}".replace(".",",")
    st_p_l_dk_b=f"{round(p_l_dk_b/100,2):.2f}".replace(".",",")

    p_l=p_a*p_l_dk_a+p_b*p_l_dk_b
    st_p_l=f"{round_half_up(p_l/10000,3)}".replace(".",",")

    p_a_dk_l=((p_a/100)*(p_l_dk_a/100))/(p_l/10000)
    st_p_a_dk_l=f"{round_half_up(p_a_dk_l,2):.2f}".replace(".",",")
    chon=random.randint(1,2)
    if chon==1:
        ten_1="I"
        ten_2="II"
    
    if chon==2:
        ten_1="A"
        ten_2="B"  
    noi_dung = (f"Một nhà máy có hai phân xưởng {ten_1} và {ten_2}. Phân xưởng {ten_1} sản xuất ${p_a}\\%$ số sản phẩm"
f"và phân xưởng {ten_2} sản xuất ${p_b}\\%$ số sản phẩm. "
f"Tỉ lệ sản phẩm bị lỗi của phân xưởng {ten_1} là ${p_l_dk_a}\\%$ và của phân xưởng {ten_2} là ${p_l_dk_b}\\%$."
f" Kiểm tra ngẫu nhiên một sản phẩm của nhà máy và thấy sản phẩm bị lỗi."
f" Tính xác suất sản phẩm lỗi đó do phân xưởng {ten_1} sản xuất (kết quả làm tròn đến hàng phần trăm).")
    dap_an=st_p_a_dk_l

    noi_dung_loigiai=(
    f'Gọi A là biến cố "Sản phẩm do phân xưởng {ten_1} sản xuất".\n\n'
    f'Gọi B là biến cố "Sản phẩm do phân xưởng {ten_2} sản xuất".\n\n'
    f'Gọi L là biến cố "Sản phẩm được kiểm tra bị lỗi".\n\n'
    f'Xác suất sản phẩm do phân xưởng {ten_1} sản xuất: $P(A)={p_a}\\%={st_p_a}$.\n\n'
    f'Xác suất sản phẩm do phân xưởng {ten_2} sản xuất: $P(B)={p_b}\\%={st_p_b}$.\n\n'
    f'Xác suất sản phẩm lỗi nếu do phân xưởng {ten_1} sản xuất: $P(L|A)={p_l_dk_a}\\%={st_p_l_dk_a}$.\n\n'
    f'Xác suất sản phẩm lỗi nếu do phân xưởng {ten_1} sản xuất: $P(L|B)={p_l_dk_b}\\%={st_p_l_dk_b}$.\n\n'

    f'Xác suất để sản phẩm kiểm tra bị lỗi từ toàn bộ nhà máy:\n\n'
    f'$P(L)=P(A)P(L|A)+P(B)P(L|B)={st_p_a}.{st_p_l_dk_a}+{st_p_b}.{st_p_l_dk_b}={st_p_l}$.\n\n'
    f'Xác suất sản phẩm kiểm tra bị lỗi do phân xưởng {ten_1} sản xuất:\n\n'
    f'$P(A|L)=\\dfrac{{P(A).P(L|A)}}{{P(L)}}=\\dfrac{{{st_p_a}.{st_p_l_dk_a}}}{{{st_p_l}}}={st_p_a_dk_l}.$')    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_09]-SA-M3. X.S Bayes: Tính xác suất ý kiến khách hàng không hài lòng
def newy25_L12_C6_B2_09():
    p_a=random.randint(40,70)
    p_b=100-p_a
    st_p_a=f"{round_half_up(p_a/100,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_b/100,2)}".replace(".",",")
    while True:
        p_l_dk_a=random.randint(2,10)
        p_l_dk_b=random.randint(2,10)
        if p_l_dk_a!=p_l_dk_b:
            break

    st_p_l_dk_a=f"{round(p_l_dk_a/100,2):.2f}".replace(".",",")
    st_p_l_dk_b=f"{round(p_l_dk_b/100,2):.2f}".replace(".",",")

    p_l=p_a*p_l_dk_a+p_b*p_l_dk_b
    st_p_l=f"{round_half_up(p_l/10000,3)}".replace(".",",")

    p_a_dk_l=((p_a/100)*(p_l_dk_a/100))/(p_l/10000)
    st_p_a_dk_l=f"{round_half_up(p_a_dk_l,2):.2f}".replace(".",",")
    chon=random.randint(1,2)
    if chon==1:
        ten_1="I"
        ten_2="II"
    
    if chon==2:
        ten_1="A"
        ten_2="B"  
    noi_dung = (f"Một công ty có hai chi nhánh {ten_1} và {ten_2}. Chi nhánh {ten_1} chiếm ${p_a}\\%$ tổng số khác hàng"
f"và chi nhánh {ten_2} chiếm ${p_b}\\%$ tổng số khác hàng. "
f"Theo khảo sát, có {ten_1} ${p_l_dk_a}\\%$ không hài lòng về dịch vụ trong khi ở chi nhánh {ten_2} tỷ lệ này là ${p_l_dk_b}\\%$."
f" Chọn ngẫu nhiên một khách hàng không hài lòng."
f" Tính xác suất khách hàng đó thuộc chi nhánh {ten_1} sản xuất (kết quả làm tròn đến hàng phần trăm).")
    dap_an=st_p_a_dk_l

    noi_dung_loigiai=(
    f'Gọi A là biến cố "Khách hàng do chi nhánh {ten_1} phục vụ".\n\n'
    f'Gọi B là biến cố "Khách hàng do chi nhánh {ten_2} sản xuất".\n\n'
    f'Gọi L là biến cố "Khách hàng không hài lòng".\n\n'
    f'Xác suất khách hàng do chi nhánh {ten_1} phục vụ: $P(A)={p_a}\\%={st_p_a}$.\n\n'
    f'Xác suất khách hàng do chi nhánh {ten_1} phục vụ: $P(B)={p_b}\\%={st_p_b}$.\n\n'
    f'Xác suất khách hàng không hài lòng do chi nhánh {ten_1} phục vụ: $P(L|A)={p_l_dk_a}\\%={st_p_l_dk_a}$.\n\n'
    f'Xác suất khách hàng không hài lòng do chi nhánh {ten_2} phục vụ: $P(L|B)={p_l_dk_b}\\%={st_p_l_dk_b}$.\n\n'

    f'Xác suất để khách hàng không hài lòng của toàn bộ công ty:\n\n'
    f'$P(L)=P(A)P(L|A)+P(B)P(L|B)={st_p_a}.{st_p_l_dk_a}+{st_p_b}.{st_p_l_dk_b}={st_p_l}$.\n\n'
    f'Xác suất khách hàng không hài lòng do phân xưởng {ten_1} khi kiểm tra toàn bộ công ty:\n\n'
    f'$P(A|L)=\\dfrac{{P(A).P(L|A)}}{{P(L)}}=\\dfrac{{{st_p_a}.{st_p_l_dk_a}}}{{{st_p_l}}}={st_p_a_dk_l}.$')    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_10]-SA-M3. X.S Bayes: Tính xác suất sản xuất xe bị lỗi
def newy25_L12_C6_B2_10():
    p_a=random.randint(40,70)
    p_b=100-p_a
    st_p_a=f"{round_half_up(p_a/100,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_b/100,2)}".replace(".",",")
    while True:
        p_l_dk_a=random.randint(2,10)
        p_l_dk_b=random.randint(2,10)
        if p_l_dk_a!=p_l_dk_b:
            break

    st_p_l_dk_a=f"{round(p_l_dk_a/100,2):.2f}".replace(".",",")
    st_p_l_dk_b=f"{round(p_l_dk_b/100,2):.2f}".replace(".",",")

    p_l=p_a*p_l_dk_a+p_b*p_l_dk_b
    st_p_l=f"{round_half_up(p_l/10000,3)}".replace(".",",")

    p_a_dk_l=((p_a/100)*(p_l_dk_a/100))/(p_l/10000)
    st_p_a_dk_l=f"{round_half_up(p_a_dk_l,2):.2f}".replace(".",",")
    chon=random.randint(1,2)
    if chon==1:
        ten_1="Sedan"
        ten_2="SUV"
    
    if chon==2:
        ten_1="xe 5 chỗ"
        ten_2="xe 7 chỗ"
    

     
    noi_dung = (f"Một nhà máy sản xuất hai dòng xe {ten_1} và {ten_2}. Dòng {ten_1} chiếm ${p_a}\\%$ tổng sản lượng,"
f"còn dòng {ten_2} chiếm ${p_b}\\%$ tổng sản lượng. "
f"Xác suất một chiếc Sedan gặp lỗi kỹ thuật là ${p_l_dk_a}\\%$ và trong khi xác suất này với {ten_2} là ${p_l_dk_b}\\%$."
f" Một chiếc xe được chọn ngẫu nhiên và phát hiện bị lỗi."
f" Tính  xác suất chiếc xe đó thuộc dòng {ten_1} (kết quả làm tròn đến hàng phần trăm).")
    dap_an=st_p_a_dk_l

    noi_dung_loigiai=(
    f'Gọi A là biến cố "Xe được chọn là dòng {ten_1}".\n\n'
    f'Gọi B là biến cố "Xe được chọn là dòng {ten_2}".\n\n'
    f'Gọi L là biến cố "Xe được chọn bị lỗi kỹ thuật".\n\n'
    f'Xác suất xe được chọn là dòng {ten_1}: $P(A)={p_a}\\%={st_p_a}$.\n\n'
    f'Xác suất xe được chọn là dòng {ten_2}: $P(B)={p_b}\\%={st_p_b}$.\n\n'
    f'Xác suất xe được chọn bị lỗi kỹ thuật là dòng {ten_1}: $P(L|A)={p_l_dk_a}\\%={st_p_l_dk_a}$.\n\n'
    f'Xác suất xe được chọn bị lỗi kỹ thuật là dòng {ten_2}: $P(L|B)={p_l_dk_b}\\%={st_p_l_dk_b}$.\n\n'
    f'Xác suất để xe được chọn bị lỗi kỹ thuật của tổng sản lượng sản xuất:\n\n'
    f'$P(L)=P(A)P(L|A)+P(B)P(L|B)={st_p_a}.{st_p_l_dk_a}+{st_p_b}.{st_p_l_dk_b}={st_p_l}$.\n\n'
    f'Xác suất xe được chọn bị lỗi kỹ thuật là dòng {ten_1} khi chọn ngẫu nhiên toàn bộ các xe:\n\n'
    f'$P(A|L)=\\dfrac{{P(A).P(L|A)}}{{P(L)}}=\\dfrac{{{st_p_a}.{st_p_l_dk_a}}}{{{st_p_l}}}={st_p_a_dk_l}.$')    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_11]-SA-M3. X.S Bayes: Tính xác suất mắc bệnh
def newy25_L12_C6_B2_11():
    p_a=random.randint(40,70)
    p_b=100-p_a
    st_p_a=f"{round_half_up(p_a/100,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_b/100,2)}".replace(".",",")
    while True:
        p_l_dk_a=random.randint(2,10)
        p_l_dk_b=random.randint(60,95)
        if p_l_dk_a!=p_l_dk_b:
            break

    st_p_l_dk_a=f"{round(p_l_dk_a/100,2):.2f}".replace(".",",")
    st_p_l_dk_b=f"{round(p_l_dk_b/100,2):.2f}".replace(".",",")

    p_l=p_a*p_l_dk_a+p_b*p_l_dk_b
    st_p_l=f"{round_half_up(p_l/10000,3)}".replace(".",",")

    p_b_dk_l=((p_b/100)*(p_l_dk_b/100))/(p_l/10000)
    st_p_b_dk_l=f"{round_half_up(p_b_dk_l,2):.2f}".replace(".",",")
    chon=random.randint(1,2)
    ten_1="khỏe mạnh"
    ten_2="mắc bệnh"

     
    noi_dung = (f"Một bệnh viện thực hiện xét nghiệm phát hiện một loại bệnh."
        f" Trong số các bệnh nhân đến xét nghiệm, có ${p_a}\\%$ là người khỏe mạnh và ${p_b}\\%$ là người mắc bệnh."
f" Xét nghiệm có xác suất cho kết quả dương tính sai ở người khỏe mạnh là ${p_l_dk_a}\\%$ "
f"và xác suất cho kết quả dương tính đúng ở người mắc bệnh là ${p_l_dk_b}\\%$."
f" Một người có kết quả xét nghiệm là dương tính."
f" Tính xác suất người đó thực sự mắc bệnh (kết quả làm tròn đến hàng phần trăm).")
    dap_an=st_p_b_dk_l

    noi_dung_loigiai=(
    f'Gọi K là biến cố "Người xét nghiệm là {ten_1}".\n\n'
    f'Gọi M là biến cố "Người xét nghiệm là {ten_2}".\n\n'
    f'Gọi D là biến cố "người có kết quả xét nghiệm là dương tính".\n\n'
    f'Xác suất người xét nghiệm là {ten_1}: $P(K)={p_a}\\%={st_p_a}$.\n\n'
    f'Xác suất người xét nghiệm là {ten_2}: $P(M)={p_b}\\%={st_p_b}$.\n\n'
    f'Xác suất dương tính sai (người khỏe mạnh có kết quả dương tính): $P(D|K)={p_l_dk_a}\\%={st_p_l_dk_a}$.\n\n'
    f'Xác suất dương tính đúng (người mắc bệnh có kết quả dương tính): $P(D|M)={p_l_dk_b}\\%={st_p_l_dk_b}$.\n\n'
    f'Xác suất tổng thể của việc có kết quả dương tính:\n\n'
    f'$P(D)=P(K)P(D|K)+P(M)P(D|M)={st_p_a}.{st_p_l_dk_a}+{st_p_b}.{st_p_l_dk_b}={st_p_l}$.\n\n'
    f'Xác suất người đó thực sự mắc bệnh:\n\n'
    f'$P(M|D)=\\dfrac{{P(M).P(D|M)}}{{P(D)}}=\\dfrac{{{st_p_b}.{st_p_l_dk_b}}}{{{st_p_l}}}={st_p_b_dk_l}.$')    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_12]-SA-M3. X.S Bayes: Tính xác suất ý kiến khách hàng không hài lòng
def newy25_L12_C6_B2_12():
    p_a=random.randint(40,70)
    p_b=100-p_a
    st_p_a=f"{round_half_up(p_a/100,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_b/100,2)}".replace(".",",")
    while True:
        p_l_dk_a=random.randint(2,10)
        p_l_dk_b=random.randint(2,10)
        if p_l_dk_a!=p_l_dk_b:
            break

    st_p_l_dk_a=f"{round(p_l_dk_a/100,2):.2f}".replace(".",",")
    st_p_l_dk_b=f"{round(p_l_dk_b/100,2):.2f}".replace(".",",")

    p_l=p_a*p_l_dk_a+p_b*p_l_dk_b
    st_p_l=f"{round_half_up(p_l/10000,3)}".replace(".",",")

    p_a_dk_l=((p_a/100)*(p_l_dk_a/100))/(p_l/10000)
    st_p_a_dk_l=f"{round_half_up(p_a_dk_l,2):.2f}".replace(".",",")
    chon=random.randint(1,2)
    if chon==1:
        ten_1="Team Alpha"
        ten_2="Team Beta"
    
    if chon==2:
        ten_1="Team Quantum"
        ten_2="Team Nexus"

    if chon==2:
        ten_1="Team Phoenix"
        ten_2="Team Dragon" 
    noi_dung = (f"Một công ty phần mềm có hai đội phát triển là {ten_1} và {ten_2}. Biết rằng {ten_1} phát triển ${p_a}\\%$ số sản phẩm"
f"và {ten_2} phát triển ${p_b}\\%$ số sản phẩm. "
f"Tỉ lệ sản phẩm có lỗi từ {ten_1} là ${p_l_dk_a}\\%$ và từ {ten_2} là ${p_l_dk_b}\\%$."
f" Chọn ngẫu nhiên một sản phẩm do các đội phát triển và thấy sản phẩm bị lỗi."
f" Tính xác suất sản phẩm đó được phát triển bởi {ten_1} (kết quả làm tròn đến hàng phần trăm).")
    dap_an=st_p_a_dk_l

    noi_dung_loigiai=(
    f'Gọi A là biến cố "Sản phẩm do {ten_1} phát triển".\n\n'
    f'Gọi B là biến cố "Sản phẩm do {ten_2} sản xuất".\n\n'
    f'Gọi L là biến cố "Sản phẩm phát triển bị lỗi".\n\n'
    f'Xác suất sản phẩm do {ten_1} phát triển: $P(A)={p_a}\\%={st_p_a}$.\n\n'
    f'Xác suất sản phẩm do {ten_2} phát triển: $P(B)={p_b}\\%={st_p_b}$.\n\n'
    f'Xác suất sản phẩm lỗi do {ten_1}: $P(L|A)={p_l_dk_a}\\%={st_p_l_dk_a}$.\n\n'
    f'Xác suất sản phẩm lỗi do {ten_2}: $P(L|B)={p_l_dk_b}\\%={st_p_l_dk_b}$.\n\n'

    f'Xác suất để sản phẩm bị lỗi khi chọn ngẫu nhiên toàn bộ sản phẩm:\n\n'
    f'$P(L)=P(A)P(L|A)+P(B)P(L|B)={st_p_a}.{st_p_l_dk_a}+{st_p_b}.{st_p_l_dk_b}={st_p_l}$.\n\n'
    f'Xác suất sản phẩm bị lỗi do {ten_1} phát triển:\n\n'
    f'$P(A|L)=\\dfrac{{P(A).P(L|A)}}{{P(L)}}=\\dfrac{{{st_p_a}.{st_p_l_dk_a}}}{{{st_p_l}}}={st_p_a_dk_l}.$')    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[oly]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an
