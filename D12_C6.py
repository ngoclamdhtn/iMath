import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
from decimal import Decimal, ROUND_HALF_UP

#Kí hiệu biến cố đối
def ngang(A):
    return f"\\overline{{{A}}}"
#Hàm tạo kí hiệu C^k_n
def ckn(k,n):
    return f"C^{{{k}}}_{{{n}}}"

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
    f" Tính xác suất $P(A|B)$."
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
    f"Cho hai biến cố ${{A}}$ và ${{B}}$ có $P(B)={st_p_b}, P(A|B)= {st_p_a_dk_b}$. Tính xác suất $P(\\overline{{A}}B)$ (kết quả làm tròn đến hàng phần trăm)."
    )
        

    p_ab=p_b*p_a_dk_b
    st_p_ab=f"{round_half_up(p_ab,2):.2f}".replace(".",",")

    kq=p_b-p_ab
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    kq_false = []
    while len(kq_false) < 10:
        num = random.random()
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(round(num,2))    
    
    kq2,kq3,kq4=random.sample(kq_false,3)
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
    f"Cho hai biến cố ${{A}}$ và ${{B}}$ có $P(A)={st_p_a}, P(B)={st_p_b}, P(AB)= {st_p_ab}$. Tính xác suất $P(\\overline{{A}}|B)$ (kết quả làm tròn đến hàng phần trăm)."
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

#[D12_C6_B1_10]-SA-M2. Tính xác suất học sinh chơi được môn A biết học sinh chơi được môn B
def newy25_L12_C6_B1_10():
    clb=["cờ tướng", "cờ vua", " cầu lông", "bóng đá", "bóng chuyền"]
    co_vua,co_tuong=random.sample(clb,2)
    lop=random.choice([f"10A{random.randint(1,9)}", f"11A{random.randint(1,9)}",f"12A{random.randint(1,9)}" ])
    n_cahai=random.randint(6,12)
    n_vua=random.randint(15,20)
    n_tuong=random.choice([i for i in range(15,20) if i!= n_vua])
    n_lop=n_vua+n_tuong-n_cahai

    noi_dung = (
    f"Lớp {lop} có ${{{n_lop}}}$ học sinh, mỗi học sinh biết chơi ít nhất một trong hai môn {co_vua} hoặc {co_tuong}."
    f" Biết rằng có ${{{n_vua}}}$ học sinh biết chơi {co_vua} và ${{{n_tuong}}}$ thành viên biết chơi {co_tuong}."
    f" Chọn ngẫu nhiên ${{1}}$ học sinh của lớp. Tính xác suất học sinh được chọn biết chơi {co_vua}, biết rằng học sinh đó biết chơi {co_tuong} (kết quả làm tròn đến hàng phần trăm)."
    )
    
    p_AB=n_cahai/n_lop
    p_B=n_tuong/n_lop
    p=p_AB/p_B
    dap_an=f"{round_half_up(p,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f'Gọi ${{A}}$ là biến cố "Học sinh được chọn biết chơi {co_vua}.\n\n'
    f' Gọi ${{B}}$ là biến cố "Học sinh được chọn biết chơi {co_tuong}.\n\n'
    f' Số học sinh biết chơi cả hai: ${n_vua}+{n_tuong}-{n_lop}={n_cahai}$.\n\n'
    f' $P(AB)=\\dfrac{{{n_cahai}}}{{{n_lop}}}={phan_so(p_AB)}$.\n\n'
    f' $P(B)=\\dfrac{{{n_tuong}}}{{{n_lop}}}={phan_so(p_B)}$.\n\n'
    f' Xác suất cần tính là: $P(A|B)=\\dfrac{{P(AB)}}{{P(B)}}=\\dfrac{{{phan_so(p_AB)}}}{{{phan_so(p_B)}}}={phan_so(p)}={dap_an}$.'

    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B1_11]-SA-M2. Lấy 1 bi hộp I bỏ vào hộp II, rồi lấy 1 bi từ hộp II. Tính xác suất hai bi cùng màu 
def newy25_L12_C6_B1_11():
    while True:
        X1=random.randint(4,10)
        D1=random.randint(5,10)
        X2=random.randint(5,10)
        D2=random.randint(4,10)
        if all([X1!=D1, X2!=D2,X1!=X2]):
            break

    noi_dung = (
    f"Hộp thứ nhất có ${{{X1}}}$ viên bi xanh và ${{{D1}}}$ viên bi đỏ. Hộp thứ hai có ${{{X2}}}$ viên bi xanh và ${{{D2}}}$ viên bi đỏ."
    f" Các viên bi có cùng kích thước và khối lượng. Lấy ra ngẫu nhiên ${{1}}$ viên bi từ hộp thứ nhất chuyển sang hộp thứ hai."
    f" Sau đó lại lấy ra ngẫu nhiên ${{1}}$ viên bi từ hộp thứ hai."
    f" Tính xác suất của các biến cố hai viên bi lấy ra có cùng màu (kết quả làm tròn đến hàng phần trăm).")
    p_x=X1/(X1+D1)
    p_x_ngang=1-p_x
    p_y_dk_x=D2/(X2+D2+1)
    p_y_ngang_dk_x=1-p_y_dk_x
    p_y_dk_x_ngang=(D2+1)/(X2+D2+1)
    p_y_ngang_dk_x_ngang=1-p_y_dk_x_ngang

    p_a=p_x*p_y_ngang_dk_x+p_x_ngang*p_y_dk_x_ngang
    dap_an=f"{round_half_up(p_a,2):.2f}".replace(".",",")

    code_hinh=f"\\begin{{tikzpicture}}\n\
                \\def\\gocm{{20}}\n\
                \\def\\gocn{{10}}\n\
                \\def\\r{{4}}\n\
                \\tikzset{{s/.style={{outer sep=0.5 mm,draw=magenta,rectangle,minimum width=2.75cm,rounded corners=1mm}}}}\n\
                \\path(0,0)node(O){{}}++(\\gocm:\\r)node[s](A1){{X}}++(\\gocn:\\r)node[s](A2){{$Y$}};\n\
                \\path(A1)++({{-\\gocn}}:\\r)node[s](a2){{$\\overline{{Y}}$}};\n\
                \\path(O)++(-\\gocm:\\r)node[s](B1){{$\\overline{{X}}$}}++(\\gocn:\\r)node[s](B2){{$Y$}};\n\
                \\path(B1)++({{-\\gocn}}:\\r)node[s](b2){{$\\overline{{Y}}$}};\n\
                \\foreach \\x/\\y in {{\n\
                    O/A1,A1/A2,\n\
                    O/B1,B1/B2,\n\
                    A1/a2,\n\
                    B1/b2}}\n\
                \\draw[-stealth](\\x.east)--(\\y.west);\n\
                \\path(O)--(A1.west)node[pos=0.5,above,sloped]{{${phan_so(p_x)}$}}(O)--(B1.west)node[pos=0.5,below,sloped]{{${phan_so(p_x_ngang)}$}}(B1.east)--(B2.west)node[pos=0.5,above,sloped]{{${phan_so(p_y_dk_x_ngang)}$}}(A1.east)--(A2.west)node[pos=0.5,above,sloped]{{${phan_so(p_y_dk_x)}$}}\n\
                (A1.east)--(a2.west)node[pos=0.5,below,sloped]{{${phan_so(p_y_ngang_dk_x)}$}}\n\
                (B1.east)--(b2.west)node[pos=0.5,below,sloped]{{${phan_so(p_y_ngang_dk_x_ngang)}$}};\n\
                \n\
            \\end{{tikzpicture}}" 

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    

    noi_dung_loigiai=(    
    f'Gọi ${{X}}$ là biến cố: "Viên bi lấy ra từ hộp thứ nhất có màu xanh".\n\n'
    f'Gọi ${{Y}}$ là biến cố: "Viên bi lấy ra từ hộp thứ hai có màu đỏ".\n\n'
    f'Gọi ${{A}}$ là biến cố: "Hai viên bi lấy ra có cùng màu".\n\n'
    f'$P(X)={phan_so(p_x)}, P(Y|X)={phan_so(p_y_dk_x)}$.\n\n'
    f"$P(\\overline{{Y}}|X)=1-P(Y|X)=1-{phan_so(p_y_dk_x)}={phan_so(p_y_ngang_dk_x)}$.\n\n"
    f'$P(\\overline{{X}})=1-P(X)={phan_so(p_x_ngang)}$.\n\n'
    f'$P(Y|\\overline{{X}})={phan_so(p_y_dk_x_ngang)}$.\n\n'
    f'Ta có: $P(A)=P(X\\overline{{Y}})+P(\\overline{{X}}Y)={phan_so(p_x)}.{phan_so(p_y_ngang_dk_x)}+{phan_so(p_x_ngang)}.{phan_so(p_y_dk_x_ngang)}={phan_so(p_a)}={dap_an}$.'
    )

        
    debai_word= f"{noi_dung}"
    loigiai_word=(f"Lời giải:\n {file_name} {noi_dung_loigiai} \n")
    


    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung}\n"
   
    f"\\loigiai{{ \\begin{{center}}\n {code_hinh}\n \\end{{center}}\n {noi_dung_loigiai} \n }}"
    f"\\end{{ex}}\n")
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B1_12]-SA-M2. Lấy 1 bi hộp I bỏ vào hộp II, rồi lấy 1 bi từ hộp II. Tính xác suất hai bi khác màu 
def newy25_L12_C6_B1_12():
    while True:
        X1=random.randint(4,10)
        D1=random.randint(5,10)
        X2=random.randint(5,10)
        D2=random.randint(4,10)
        if all([X1!=D1, X2!=D2]):
            break

    noi_dung = (
    f"Hộp thứ nhất có ${{{X1}}}$ viên bi xanh và ${{{D1}}}$ viên bi đỏ. Hộp thứ hai có ${{{X2}}}$ viên bi xanh và ${{{D2}}}$ viên bi đỏ."
    f" Các viên bi có cùng kích thước và khối lượng. Lấy ra ngẫu nhiên ${{1}}$ viên bi từ hộp thứ nhất chuyển sang hộp thứ hai."
    f" Sau đó lại lấy ra ngẫu nhiên ${{1}}$ viên bi từ hộp thứ hai."
    f" Tính xác suất của các biến cố hai viên bi lấy ra khác màu (kết quả làm tròn đến hàng phần trăm).")
    p_x=X1/(X1+D1)
    p_x_ngang=1-p_x
    p_y_dk_x=D2/(X2+D2+1)
    p_y_ngang_dk_x=1-p_y_dk_x
    p_y_dk_x_ngang=(D2+1)/(X2+D2+1)
    p_y_ngang_dk_x_ngang=1-p_y_dk_x_ngang

    p_a=p_x*p_y_dk_x+p_x_ngang*p_y_ngang_dk_x_ngang
    
    dap_an=f"{round_half_up(p_a,2):.2f}".replace(".",",")

    code_hinh=f"\\begin{{tikzpicture}}\n\
                \\def\\gocm{{20}}\n\
                \\def\\gocn{{10}}\n\
                \\def\\r{{4}}\n\
                \\tikzset{{s/.style={{outer sep=0.5 mm,draw=magenta,rectangle,minimum width=2.75cm,rounded corners=1mm}}}}\n\
                \\path(0,0)node(O){{}}++(\\gocm:\\r)node[s](A1){{X}}++(\\gocn:\\r)node[s](A2){{$Y$}};\n\
                \\path(A1)++({{-\\gocn}}:\\r)node[s](a2){{$\\overline{{Y}}$}};\n\
                \\path(O)++(-\\gocm:\\r)node[s](B1){{$\\overline{{X}}$}}++(\\gocn:\\r)node[s](B2){{$Y$}};\n\
                \\path(B1)++({{-\\gocn}}:\\r)node[s](b2){{$\\overline{{Y}}$}};\n\
                \\foreach \\x/\\y in {{\n\
                    O/A1,A1/A2,\n\
                    O/B1,B1/B2,\n\
                    A1/a2,\n\
                    B1/b2}}\n\
                \\draw[-stealth](\\x.east)--(\\y.west);\n\
                \\path(O)--(A1.west)node[pos=0.5,above,sloped]{{${phan_so(p_x)}$}}(O)--(B1.west)node[pos=0.5,below,sloped]{{${phan_so(p_x_ngang)}$}}(B1.east)--(B2.west)node[pos=0.5,above,sloped]{{${phan_so(p_y_dk_x_ngang)}$}}(A1.east)--(A2.west)node[pos=0.5,above,sloped]{{${phan_so(p_y_dk_x)}$}}\n\
                (A1.east)--(a2.west)node[pos=0.5,below,sloped]{{${phan_so(p_y_ngang_dk_x)}$}}\n\
                (B1.east)--(b2.west)node[pos=0.5,below,sloped]{{${phan_so(p_y_ngang_dk_x_ngang)}$}};\n\
                \n\
            \\end{{tikzpicture}}" 

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    noi_dung_loigiai=(    
    f'Gọi ${{X}}$ là biến cố: "Viên bi lấy ra từ hộp thứ nhất có màu xanh".\n\n'
    f'Gọi ${{Y}}$ là biến cố: "Viên bi lấy ra từ hộp thứ hai có màu đỏ".\n\n'
    f'Gọi ${{A}}$ là biến cố: "Hai viên bi lấy ra có cùng màu".\n\n'
    f'$P(X)={phan_so(p_x)}, P(Y|X)={phan_so(p_y_dk_x)}$.\n\n'
    f"$P(\\overline{{Y}}|X)=1-P(Y|X)=1-{phan_so(p_y_dk_x)}={phan_so(p_y_ngang_dk_x)}$.\n\n"
    f'$P(\\overline{{X}})=1-P(X)={phan_so(p_x_ngang)}$.\n\n'
    f'$P(Y|\\overline{{X}})={phan_so(p_y_dk_x_ngang)}$.\n\n'
    f'$P(A)=P(XY)+P(\\overline{{X}}\\overline{{Y}})={phan_so(p_x)}.{phan_so(p_y_dk_x)}+{phan_so(p_x_ngang)}.{phan_so(p_y_ngang_dk_x_ngang)}={phan_so(p_a)}={dap_an}$.'
    
    )

        
    debai_word= f"{noi_dung}"
    loigiai_word=(f"Lời giải:\n {file_name} {noi_dung_loigiai} \n")
    


    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung}\n"    
    f"\\loigiai{{\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n \n {noi_dung_loigiai} \n }}"
    f"\\end{{ex}}\n")
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B1_13]-SA-M2. x.s giao: Tính x.s sinh viên không tốt nghiệp loại X và làm việc đúng chuyên ngành
def newy25_L12_C6_B1_13():
    p_g=random.randint(10,30)
    p_k=100-p_g
    p_d_dk_g=random.randint(78,95)
    p_d_dk_k=random.randint(55,75)
    p_d_ngang_dk_g=100-p_d_dk_g
    p_d_ngang_dk_k=100-p_d_dk_k
    st_p_g=f"{round_half_up(p_g/100,2):.2f}".replace(".",",")
    st_p_k=f"{round_half_up(p_k/100,2):.2f}".replace(".",",")
    st_p_d_dk_g=f"{round_half_up(p_d_dk_g/100,2):.2f}".replace(".",",")
    st_p_d_dk_k=f"{round_half_up(p_d_dk_k/100,2):.2f}".replace(".",",")
    st_p_d_ngang_dk_g=f"{round_half_up(p_d_ngang_dk_g/100,2):.2f}".replace(".",",")
    st_p_d_ngang_dk_k=f"{round_half_up(p_d_ngang_dk_k/100,2):.2f}".replace(".",",")


    chon=random.randint(1,2)
    
    if chon==1:
        noi_dung = (
        f"Một trường đại học tiến hành khảo sát tình trạng việc làm sau khi tốt nghiệp của sinh viên."
        f" Kết quả khảo sát cho thấy tỉ lệ người tìm được việc làm đúng chuyên ngành là ${p_d_dk_g}\\%$ đối với sinh viên tốt nghiệp loại giỏi"
        f" và ${p_d_dk_k}\\%$ đối với sinh viên tốt nghiệp loại khác."
        f" Tỉ lệ sinh viên tốt nghiệp loại giỏi là ${p_g}\\%$."
        f" Chọn ngẫu nhiên một sinh viên đã tốt nghiệp của trường."
        f" Tính xác suất sinh viên đó không tốt nghiệp loại giỏi và được việc làm đúng chuyên ngành (kết quả làm tròn đến hàng phần trăm)."

        )
        dap_an=f"{round_half_up((p_k*p_d_dk_k)/10000,2):.2f}".replace(".",",")

        noi_dung_loigiai=(
        f'Gọi G là biến cố: "Sinh viên tốt nghiệp loại giỏi".\n\n'
        f'Gọi $K=\\overline{{G}}$ là biến cố: "Sinh viên tốt nghiệp loại khác".\n\n'
        f'Khi đó D|G là biến cố: "Sinh viên làm đúng chuyên ngành nếu tốt nghiệp loại giỏi".\n\n'
        f'Khi đó D|K là biến cố: "Sinh viên làm đúng chuyên ngành nếu tốt nghiệp loại khác".\n\n'
        f"Ta có: $P(G)={st_p_g},P(K)={st_p_k}, P(D|G)={st_p_d_dk_g}, P(D|K)={st_p_d_dk_k}$.\n\n"
        f"Xác suất để sinh viên đó không tốt nghiệp loại giỏi và được việc làm đúng chuyên ngành:\n\n"
        f"$P(KD)=P(K).P(D|K)={st_p_k}.{st_p_d_dk_k}={dap_an}$."
        )   
    
    if chon==2:
        noi_dung = (
        f"Một trường đại học tiến hành khảo sát tình trạng việc làm sau khi tốt nghiệp của sinh viên."
        f" Kết quả khảo sát cho thấy tỉ lệ người tìm được việc làm đúng chuyên ngành là ${p_d_dk_g}\\%$ đối với sinh viên tốt nghiệp loại giỏi"
        f" và ${p_d_dk_k}\\%$ đối với sinh viên tốt nghiệp loại khác."
        f" Tỉ lệ sinh viên tốt nghiệp loại giỏi là ${p_g}\\%$."
        f" Chọn ngẫu nhiên một sinh viên đã tốt nghiệp của trường."
        f" Tính xác suất sinh viên đó tốt nghiệp loại giỏi và được việc làm đúng chuyên ngành (kết quả làm tròn đến hàng phần trăm)."

        )
        dap_an=f"{round_half_up((p_g*p_d_dk_g)/10000,2):.2f}".replace(".",",")

        noi_dung_loigiai=(
        f'Gọi G là biến cố: "Sinh viên tốt nghiệp loại giỏi".\n\n'
        f'Gọi $K=\\overline{{G}}$ là biến cố: "Sinh viên tốt nghiệp loại khác".\n\n'
        f'Khi đó D|G là biến cố: "Sinh viên làm đúng chuyên ngành nếu tốt nghiệp loại giỏi".\n\n'
        f'Khi đó D|K là biến cố: "Sinh viên làm đúng chuyên ngành nếu tốt nghiệp loại khác".\n\n'
        f"Ta có: $P(G)={st_p_g},P(K)={st_p_k}, P(D|G)={st_p_d_dk_g}, P(D|K)={st_p_d_dk_k}$.\n\n"
        f"Xác suất để sinh viên đó tốt nghiệp loại giỏi và được việc làm đúng chuyên ngành:\n\n"
        f"$P(GD)=P(G).P(D|G)={st_p_g}.{st_p_d_dk_g}={dap_an}$."
        )

    code_hinh=f"\\begin{{tikzpicture}}\n\
                \\def\\gocm{{20}}\n\
                \\def\\gocn{{10}}\n\
                \\def\\r{{4}}\n\
                \\tikzset{{s/.style={{outer sep=0.5 mm,draw=magenta,rectangle,minimum width=2.75cm,rounded corners=1mm}}}}\n\
                \\path(0,0)node(O){{}}++(\\gocm:\\r)node[s](A1){{$G$}}++(\\gocn:\\r)node[s](A2){{$D$}};\n\
                \\path(A1)++({{-\\gocn}}:\\r)node[s](a2){{$\\overline{{D}}$}};\n\
                \\path(O)++(-\\gocm:\\r)node[s](B1){{$K$}}++(\\gocn:\\r)node[s](B2){{$D$}};\n\
                \\path(B1)++({{-\\gocn}}:\\r)node[s](b2){{$\\overline{{D}}$}};\n\
                \\foreach \\x/\\y in {{\n\
                    O/A1,A1/A2,\n\
                    O/B1,B1/B2,\n\
                    A1/a2,\n\
                    B1/b2}}\n\
                \\draw[-stealth](\\x.east)--(\\y.west);\n\
                \\path(O)--(A1.west)node[pos=0.5,above,sloped]{{${st_p_g}$}}(O)--(B1.west)node[pos=0.5,below,sloped]{{${st_p_k}$}}(B1.east)--(B2.west)node[pos=0.5,above,sloped]{{${st_p_d_dk_k}$}}(A1.east)--(A2.west)node[pos=0.5,above,sloped]{{${st_p_d_dk_g}$}}\n\
                (A1.east)--(a2.west)node[pos=0.5,below,sloped]{{${st_p_d_ngang_dk_g}$}}\n\
                (B1.east)--(b2.west)node[pos=0.5,below,sloped]{{${st_p_d_ngang_dk_k}$}};\n\
                \n\
            \\end{{tikzpicture}}" 

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)
    


     
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {file_name}\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B1_14]-M2. X.S giao: Cho x% thực hiện việc A, trong số đó có y% thực hiện việc B. Tính P(AB)
def newy25_L12_C6_B1_14():
    p_a=random.randint(15,40)
    st_p_a=f"{round_half_up(p_a/100,2):.2f}".replace(".",",")
    p_b_dk_a=random.randint(65,95)
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a/100,2):.2f}".replace(".",",")

    kq=p_a*p_b_dk_a/10000
    st_kq=f"{round_half_up(p_a*p_b_dk_a/10000,2):.2f}".replace(".",",")
    # Tạo 10 số ngẫu nhiên khác nhau trong [0, 1), làm tròn 2 chữ số
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    chon=random.randint(1,6)     

    if chon==1:
        noi_dung=(
        f" Một nhà máy có ${p_a}\\%$ công nhân đã qua lớp đào tạo kỹ năng nâng cao."
        f" Trong số công nhân đã được đào tạo, có ${p_b_dk_a}\\%$ hoàn thành công việc đúng thời hạn."
        f" Chọn ngẫu nhiên một công nhân."
        f" Tính xác suất người đó được đào tạo và hoàn thành công việc đúng hạn (kết quả làm tròn đến hàng phần trăm).")

        noi_dung_loigiai=(
        f'Gọi ${{A}}$ là biến cố: "công nhân được đào tạo kỹ năng nâng cao".\n\n'
        f'Gọi ${{B}}$ là biến cố: "công nhân hoàn thành công việc đúng thời hạn".\n\n'
        f"Ta có: $P(A)={st_p_a}, P(B|A)={st_p_b_dk_a}$.\n\n"
        f'Xác suất cần tính: $P(AB)=P(A).P(B|A)={st_kq}$.')
    
    if chon==2:
        noi_dung=(
        f" Một khảo sát sử dụng laptop cho thấy có ${p_a}\\%$ người dùng là sinh viên."
        f" Trong số các người dùng là sinh viên, có ${p_b_dk_a}\\%$ sử dụng laptop cá nhân để học tập."
        f" Chọn ngẫu nhiên một người tham gia khảo sát."
        f" Tính xác suất người đó là sinh viên và có sử dụng laptop cá nhân để học (kết quả làm tròn đến hàng phần trăm).")

        noi_dung_loigiai=(
        f'Gọi ${{A}}$ là biến cố: "người dùng là sinh viên".\n\n'
        f'Gọi ${{B}}$ là biến cố: "người dùng sử dụng laptop cá nhân để học tập".\n\n'
        f"Ta có: $P(A)={st_p_a}, P(B|A)={st_p_b_dk_a}$.\n\n"
        f'Xác suất cần tính: $P(AB)=P(A).P(B|A)={st_kq}$.')

    if chon==3:
        noi_dung=(
        f" Qua khảo sát một trường THPT cho thấy có ${p_a}\\%$ học sinh tham gia câu lạc bộ thể thao."
        f" Trong số đó có ${p_b_dk_a}\\%$ tham gia đều đặn hàng tuần."
        f" Chọn ngẫu nhiên một học sinh tham gia khảo sát."
        f" Tính xác suất học sinh đó tham gia câu lạc bộ thể thao và đi tập đều đặn hàng tuần (kết quả làm tròn đến hàng phần trăm).")

        noi_dung_loigiai=(
        f'Gọi ${{A}}$ là biến cố: "học sinh tham gia câu lạc bộ thể thao".\n\n'
        f'Gọi ${{B}}$ là biến cố: "học sinh đi tập đều đặn hàng tuần".\n\n'        
        f"Ta có: $P(A)={st_p_a}, P(B|A)={st_p_b_dk_a}$.\n\n"
        f'Xác suất cần tính: $P(AB)=P(A).P(B|A)={st_kq}$.')

    if chon==4:
        noi_dung=(
        f" Một trang thương mại điện tử thống kê có ${p_a}\\%$ khách hàng là thành viên VIP."
        f" Trong số đó có ${p_b_dk_a}\\%$ sẽ mua hàng ít nhất một lần mỗi tháng."
        f" Chọn ngẫu nhiên một khách hàng."
        f" Tính xác suất người đó là thành viên VIP và có mua hàng mỗi tháng (kết quả làm tròn đến hàng phần trăm).")

        noi_dung_loigiai=(
        f'Gọi ${{A}}$ là biến cố: "khách hàng là thành viên VIP".\n\n'
        f'Gọi ${{B}}$ là biến cố: "khách hàng mua hàng ít nhất một lần mỗi tháng".\n\n'        
        f"Ta có: $P(A)={st_p_a}, P(B|A)={st_p_b_dk_a}$.\n\n"
        f'Xác suất cần tính: $P(AB)=P(A).P(B|A)={st_kq}$.')

    if chon==5:
        noi_dung=(
        f" Một công ty có ${p_a}\\%$ nhân viên đi làm bằng xe buýt."
        f" Trong số đó có ${p_b_dk_a}\\%$ đến đúng giờ mỗi ngày."
        f" Chọn ngẫu nhiên một nhân viên của công ty."
        f" Tính xác suất người đó đi làm bằng xe buýt và đến đúng giờ (kết quả làm tròn đến hàng phần trăm).")

        noi_dung_loigiai=(
        f'Gọi ${{A}}$ là biến cố: "nhân viên đi làm bằng xe buýt".\n\n'
        f'Gọi ${{B}}$ là biến cố: "nhân viên đến đúng giờ mỗi ngày".\n\n'        
        f"Ta có: $P(A)={st_p_a}, P(B|A)={st_p_b_dk_a}$.\n\n"
        f'Xác suất cần tính: $P(AB)=P(A).P(B|A)={st_kq}$.')

    if chon==6:
        noi_dung=(
        f" Một công ty khảo sát kỹ năng ngoại ngữ của ứng viên. Kết quả cho thấy có ${p_a}\\%$ ứng viên có chứng chỉ IELTS."
        f" Trong số ứng viên có chứng chỉ IELTS có ${p_b_dk_a}\\%$ có khả năng giao tiếp tiếng Anh tốt."
        f" Chọn ngẫu nhiên một ứng viên."
        f" Tính xác suất ứng viên đó có chứng chỉ IELTS và giao tiếp tiếng Anh tốt (kết quả làm tròn đến hàng phần trăm).")

        noi_dung_loigiai=(
        f'Gọi ${{A}}$ là biến cố: "ứng viên có chứng chỉ IELTS".\n\n'
        f'Gọi ${{B}}$ là biến cố: "ứng viên giao tiếp tiếng Anh tốt".\n\n'        
        f"Ta có: $P(A)={st_p_a}, P(B|A)={st_p_b_dk_a}$.\n\n"
        f'Xác suất cần tính: $P(AB)=P(A).P(B|A)={st_kq}$.')
    

    

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
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


#[D12_C6_B1_15]-SA-M2. X.S A|B: Tính xác suất chọn k bạn cùng giới tính có ít nhất 1 nam (hoặc 1 nữ)
def newy25_L12_C6_B1_15():
    so_nam=random.randint(5,9)
    so_nu=random.randint(5,9)
    tong=so_nam+so_nu
    k=random.randint(2,4)
    nhiemvu=random.choice(["tưới cây", "quét sân", "lau dọn phòng học", "đổ rác" ])
    giaovien=random.choice(["Thầy chủ nhiệm", "Cô chủ nhiệm", "Giáo viên" ])

    chon=random.randint(1,2)
    
    if chon==1:
        noi_dung = (
        f" Một nhóm ${{{so_nam}}}$ học sinh nam và ${{{so_nu}}}$ học sinh nữ tham gia lao động trên sân trường."
        f" {giaovien} chọn ngẫu nhiên đồng thời ${{{k}}}$ bạn trong nhóm đi {nhiemvu}."
        f" Tính xác suất để các bạn được chọn có cùng giới tính, biết rằng có ít nhất ${{1}}$ bạn nam được chọn (kết quả làm tròn đến hàng phần trăm)."
        )
        
        n_B=binomial(tong,k)-binomial(so_nu,k)
        n_AB=binomial(so_nam,k)
        dap_an=f"{round_half_up(n_AB/n_B,2):.2f}".replace(".",",")

        noi_dung_loigiai=(

        f"Số cách chọn ${{{k}}}$ bạn tùy ý: $n(\\Omega)=C^{k}_{{{tong}}}={binomial(tong,k)}$.\n\n"
        f'Gọi ${{A}}$ là biến cố "${{{k}}}$ bạn được chọn cùng giới tính".\n\n'
        f'Gọi ${{B}}$ là biến cố "${{{k}}}$ bạn được chọn có ít nhất ${{1}}$ nam".\n\n'
        f"$n(B)=C^{k}_{{{tong}}}-C^{k}_{{{so_nu}}}={binomial(tong,k)}-{binomial(so_nu,k)}={n_B}.$\n\n"
        f"Số cách chọn vừa cùng giới tính vừa ít nhất ${{1}}$ nam: $n(AB)=C^{k}_{{{so_nam}}}={n_AB}$.\n\n"
        f'Xác suất cần tính: $P(A|B)=\\dfrac{{n(AB)}}{{n(B)}}=\\dfrac{{{n_AB}}}{{{n_B}}}={dap_an}$.'
        )  
    
    if chon==2:
        noi_dung = (
        f" Một nhóm ${{{so_nam}}}$ học sinh nam và ${{{so_nu}}}$ học sinh nữ tham gia lao động trên sân trường."
        f" {giaovien} chọn ngẫu nhiên đồng thời ${{{k}}}$ bạn trong nhóm đi {nhiemvu}."
        f" Tính xác suất để các bạn được chọn có cùng giới tính, biết rằng có ít nhất ${{1}}$ bạn nữ được chọn (kết quả làm tròn đến hàng phần trăm)."
        )
        
        n_B=binomial(tong,k)-binomial(so_nam,k)
        n_AB=binomial(so_nu,k)
        dap_an=f"{round_half_up(n_AB/n_B,2):.2f}".replace(".",",")

        noi_dung_loigiai=(

        f"Số cách chọn ${{{k}}}$ bạn tùy ý: $n(\\Omega)=C^{k}_{{{tong}}}={binomial(tong,k)}$.\n\n"
        f'Gọi ${{A}}$ là biến cố "${{{k}}}$ bạn được chọn cùng giới tính".\n\n'
        f'Gọi ${{B}}$ là biến cố "${{{k}}}$ bạn được chọn có ít nhất ${{1}}$ nữ".\n\n'
        f"$n(B)=C^{k}_{{{tong}}}-C^{k}_{{{so_nam}}}={binomial(tong,k)}-{binomial(so_nam,k)}={n_B}.$\n\n"
        f"Số cách chọn vừa cùng giới tính vừa ít nhất ${{1}}$ nữ: $n(AB)=C^{k}_{{{so_nu}}}={n_AB}$.\n\n"
        f'Xác suất cần tính: $P(A|B)=\\dfrac{{n(AB)}}{{n(B)}}=\\dfrac{{{n_AB}}}{{{n_B}}}={dap_an}$.'
        )     

    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B1_16]-M2. X.S giao: cho sơ đồ cây có P(A), P(B|A), P(B_|A_). Tính P(AB_) hoặc P(A_B) hoặc P(A_B_)
def newy25_L12_C6_B1_16():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")

    b=random.randint(10,20)
    p_b=b/100
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")    

    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    chon=random.randint(1,3)
    
    if chon==1:
        kq=p_a*p_b_ngang_dk_a
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Ta có: $P({A})={st_a},P({B}|{A})={st_b_dk_a}\\Rightarrow P(\\overline{{{B}}}|{A})=1-{st_b_dk_a}={st_b_ngang_dk_a}$.\n\n"
        f"$P({A}\\overline{{{B}}})=P({A}).P(\\overline{{{B}}}|{A})={st_a}.{st_b_ngang_dk_a}={st_kq}$." )
    
    if chon==2:
        kq=p_a_ngang*p_b_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Ta có: $P({A})={st_a},P({B}|{A})={st_b_dk_a}\\Rightarrow P(\\overline{{{B}}}|{A})=1-{st_b_dk_a}={st_b_ngang_dk_a}$.\n\n"
        f"$P({B}|\\overline{{{A}}})=1-P(\\overline{{{B}}}|\\overline{{{A}}})={st_b_dk_a_ngang}$.\n\n"
        f"$P(\\overline{{{A}}}{B})=P(\\overline{{{A}}}).P({B}|\\overline{{{A}}})={st_kq}$." )

    if chon==3:
        kq=p_a_ngang*p_b_ngang_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}\\,\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Ta có: $P({A})={st_a},P({B}|{A})={st_b_dk_a}\\Rightarrow P(\\overline{{{B}}}|{A})=1-{st_b_dk_a}={st_b_ngang_dk_a}$.\n\n"
        f"$P({B}|\\overline{{{A}}})=1-P(\\overline{{{B}}}|\\overline{{{A}}})={st_b_dk_a_ngang}$.\n\n"
        f"$P(\\overline{{{A}}}\\overline{{{B}}})=P(\\overline{{{A}}}).P(\\overline{{{B}}}|\\overline{{{A}}})={st_kq}$." )




    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        
    f"\\loigiai{{ \\begin{{center}}\n{code_hinh}\n\\end{{center}}\n\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B1_17]-M2. X.S giao: cho sơ đồ cây có P(A), P(B_|A), P(B_|A_). Tính P(AB_) hoặc P(A_B) hoặc P(A_B_)
def newy25_L12_C6_B1_17():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")

    b=random.randint(10,20)
    p_b=b/100
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")    

    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S B_ngang|A\n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    chon=random.randint(1,3)
    
    if chon==1:
        kq=p_a*p_b_ngang_dk_a
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P({A}\\overline{{{B}}})=P({A}).P(\\overline{{{B}}}|{A})={st_a}.{st_b_ngang_dk_a}={st_kq}$." )
    
    if chon==2:
        kq=p_a_ngang*p_b_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P(\\overline{{{A}}}{B})=P(\\overline{{{A}}}).P({B}|\\overline{{{A}}})={st_kq}$." )

    if chon==3:
        kq=p_a_ngang*p_b_ngang_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}\\,\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P(\\overline{{{A}}}\\overline{{{B}}})=P(\\overline{{{A}}}).P(\\overline{{{B}}}|\\overline{{{A}}})={st_kq}$." )




    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B1_18]-M2. X.S giao: cho sơ đồ cây có P(A_), P(B|A), P(B_|A_). Tính P(AB_) hoặc P(A_B) hoặc P(A_B_)
def newy25_L12_C6_B1_18():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")

    b=random.randint(10,20)
    p_b=b/100
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")    

    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A\n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    chon=random.randint(1,3)
    
    if chon==1:
        kq=p_a*p_b_ngang_dk_a
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P({A}\\overline{{{B}}})=P({A}).P(\\overline{{{B}}}|{A})={st_a}.{st_b_ngang_dk_a}={st_kq}$." )
    
    if chon==2:
        kq=p_a_ngang*p_b_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P(\\overline{{{A}}}{B})=P(\\overline{{{A}}}).P({B}|\\overline{{{A}}})={st_kq}$." )

    if chon==3:
        kq=p_a_ngang*p_b_ngang_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}\\,\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P(\\overline{{{A}}}\\overline{{{B}}})=P(\\overline{{{A}}}).P(\\overline{{{B}}}|\\overline{{{A}}})={st_kq}$." )



    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B1_19]-M2. X.S giao: cho sơ đồ cây có P(A_), P(B_|A), P(B|A_). Tính P(AB_) hoặc P(A_B) hoặc P(A_B_)
def newy25_L12_C6_B1_19():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")

    b=random.randint(10,20)
    p_b=b/100
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")    

    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S B_ngang|A\n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{$$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" 
)
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    chon=random.randint(1,3)
    
    if chon==1:
        kq=p_a*p_b_ngang_dk_a
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P({A}\\overline{{{B}}})=P({A}).P(\\overline{{{B}}}|{A})={st_a}.{st_b_ngang_dk_a}={st_kq}$." )
    
    if chon==2:
        kq=p_a_ngang*p_b_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P(\\overline{{{A}}}{B})=P(\\overline{{{A}}}).P({B}|\\overline{{{A}}})={st_kq}$." )

    if chon==3:
        kq=p_a_ngang*p_b_ngang_dk_a_ngang
        st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
        noi_dung=(
        f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left(\\overline{{{A}}}\\,\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
        )
        noi_dung_loigiai=(
        f"Dựa vào sơ đồ cây ta được:\n\n"
        f"$P(\\overline{{{A}}}\\overline{{{B}}})=P(\\overline{{{A}}}).P(\\overline{{{B}}}|\\overline{{{A}}})={st_kq}$." )


    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B1_20]-M2. Cho P(A) và P(B|A). Xét Đ-S: P(A_), P(AB_), P(AB)
def newy25_L12_C6_B1_20():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    a=random.randint(15,75)
    p_a=a/100
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")

    p_a_ngang=1-p_a
    st_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")
    while True:
        x = random.random()
        if x!=p_a_ngang:
            break
    st_a_ngang_f=f"{round_half_up(x,2)}".replace(".",",")

    b_dk_a=random.randint(40,70)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    p_ba=p_b_dk_a*p_a
    st_ba=f"{round_half_up(p_ba,2)}".replace(".",",")
    while True:
        x = random.random()
        if x!=p_ba:
            break
    st_ba_f=f"{round_half_up(x,2)}".replace(".",",")

    p_a_ngangb=p_a-p_ba
    st_a_ngangb=f"{round_half_up(p_a_ngangb,2)}".replace(".",",")
    while True:
        x = random.random()
        if x!=p_a_ngangb:
            break
    st_a_ngangb_f=f"{round_half_up(x,2)}".replace(".",",")



    noi_dung = f"Cho hai biến cố ${{{A},{B}}}$ có $P({A})={st_a}$ và $P({B}|{A})={st_b_dk_a}$. Xét tính đúng-sai của các khẳng định sau (kết quả làm tròn đến hàng phần trăm):"        
    debai_word= f"{noi_dung}\n"
    
    kq1_T=f"*$P({ngang(A)})={st_a_ngang}$" 
    kq1_F=f"$P({ngang(A)})={st_a_ngang_f}$"
    
    HDG=f"$P({ngang(A)})=1-P({A})=1-{st_a}={st_a_ngang}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
    chon=random.randint(1,2)
    if chon==1:
        kq2_T=f"* $P({A}{ngang(B)})=P({A})-P({A}{B})$"
            
    if chon==2:
        kq2_T=f"* $P({A}{ngang(B)})+P({A}{B})=P({A})$"        
    
    kq2_F=random.choice([
        f"$P({A}{ngang(B)})=P({A})+P({A}{B})$",
        f"$P({A}{ngang(B)})=1-P({A}{B})$"
        ])
    HDG=f"$P({A}{ngang(B)})=P({A})-P({A}{B})\\Rightarrow P({A}{ngang(B)})+P({A}{B})=P({A})$."    
    
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* $P({B}{A})={st_ba}$" 
    kq3_F=f"$P({B}{A})={st_ba_f}$"
    
    HDG=f"$P({B}{A})=P({B}|{A}).P({A})={st_b_dk_a}.{st_a}={st_ba}$."
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq4_T=f"* $P({A}{ngang(B)})={st_a_ngangb}$"
    kq4_F=f"$P({A}{ngang(B)})={st_a_ngangb_f}$" 
    
    HDG=f"$P({A}{ngang(B)})=P({A})-P({A}{B})={st_a}-{st_ba}={st_a_ngangb}$."
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

#[D12_C6_B1_21]-M2. Chọn lần lượt 2 học sinh lên bảng. Xét Đ-S: không gian mẫu, n(A), n(A|B), n(B|A)
def newy25_L12_C6_B1_21():
    tong=random.randint(30,35)
    n_nam=random.randint(10,20)
    n_nu=tong-n_nam
    lop=[]
    for i in range(1,10):
        lop.append(f"12A{i}")
        lop.append(f"11A{i}")
        lop.append(f"10A{i}")
    lop=random.choice(lop)
    chon=random.randint(1,2)
    if chon==1:
        nam="nam"
        nu="nữ"    
    if chon==2:
        nam="nữ"
        nu="nam"
    
    noi_dung = (f"Lớp ${{{lop}}}$ có ${{{tong}}}$ học sinh trong đó có ${{{n_nam}}}$ học sinh {nam}."
        f" Giáo viên gọi ngẫu nhiên lần lượt hai bạn lên bảng làm bài tập."
        f'  Gọi ${{A}}$ là biến cố "Bạn thứ nhất được chọn là một học sinh {nam}".'
        f'  Gọi ${{B}}$ là biến cố "Bạn thứ hai được chọn là một học sinh {nam}".'
        f" Xét tính đúng-sai của các khẳng định sau." )      
    debai_word= f"{noi_dung}\n"
    n_kgm=tong*(tong-1)
    
    kq1_T=f"* Số phần tử của không gian mẫu là ${{{n_kgm}}}$" 
    kq1_F=f"Số phần tử của không gian mẫu là ${{{tong}}}$"
    
    HDG=( f"Số phần tử của không gian mẫu là ${tong}.{tong-1}={{{n_kgm}}}$.")
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n_B=n_nam*(n_nam-1)+n_nu*n_nam
    kq2_T=f"* $n(B)={n_B}$"
    kq2_F=f"$n(B)={n_nam*(n_nam-1)}$"
    
    HDG=(f"TH1: Bạn thứ nhất là {nam} và bạn thứ hai là {nam} thì số cách chọn là ${n_nam}.{n_nam-1}={n_nam*(n_nam-1)}$.\n\n"
        f"TH2: Bạn thứ nhất là {nu} và bạn thứ hai là {nam} thì số cách chọn là ${n_nu}.{n_nam}={n_nu*n_nam}$.\n\n"
        f" Số cách chọn để bạn thứ hai được chọn là {nam} là: ${n_nam*(n_nam-1)}+{n_nu*n_nam}={n_B}$.")
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    kq3_T=f"* Xác suất để bạn thứ hai là {nam} biết bạn thứ nhất là {nam} bằng ${phan_so((n_nam-1)/(tong-1))}$" 
    kq3_F=f"Xác suất để bạn thứ hai là {nam} biết bạn thứ nhất là {nam} bằng ${phan_so((n_nam-1)/(tong))}$"
    
    HDG=(f"Chọn bạn thứ nhất là {nam} thì lúc này lớp còn lại ${{{n_nam-1}}}$ {nam} và ${{{n_nu}}}$ {nu}.\n\n"
        f"Xác suất để chọn được tiếp bạn thứ hai là {nam} từ số người còn lại là:\n\n"
        f" $\\dfrac{{{n_nam-1}}}{{{n_nam-1}+{n_nu}}}={phan_so((n_nam-1)/(tong-1))}$.")
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    n_4=phan_so((n_nu/tong)*(n_nu-1)/(tong-1))
    n_4_f=phan_so((n_nu-1)/(tong-1))

    kq4_T=f"* Xác suất để cả hai bạn được chọn đều là {nu} là ${n_4}$"
    kq4_F=f"Xác suất để cả hai bạn được chọn đều là {nu} là ${n_4_f}$" 
    
    HDG=(f"Xác suất chọn ngẫu nhiên một học sinh {nu} đầu tiên là: $P(\\text{{{nu} thứ 1}})=\\dfrac{{{n_nu}}}{{{tong}}}={phan_so(n_nu/tong)}$.\n\n"
        f"Xác suất bạn thứ hai là {nu} (sau khi đã chọn một {nu} đầu tiên) là:\n\n"
        f"$P(\\text{{{nu} thứ 2}}|\\text{{{nu} thứ 1}})=\\dfrac{{{n_nu-1}}}{{{tong-1}}}={phan_so((n_nu-1)/(tong-1))}$.\n\n"
        f"Xác suất để cả hai bạn được chọn đều là {nu} là:\n\n"
        f"$P(\\text{{Cả hai {nu}}})={phan_so(n_nu/tong)}.{phan_so((n_nu-1)/(tong-1))}={n_4}$.")
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

#[D12_C6_B1_22]-M1. Cho P(A), P(AB). Tính xác suất P(B|A)
def newy25_L12_C6_B1_22():
    ten=["A","B","C","D","E","F"]
    A,B=random.sample(ten,2)
    p_a=random.randint(30,80)
    st_a=f"{round(p_a/100,2):.2f}".replace(".",",")

    p_ab=p_a-random.randint(5,28)

    st_ab=f"{round(p_ab/100,2):.2f}".replace(".",",")

    noi_dung=(
    f"Cho hai biến cố ${{{A}}}$ và ${{{B}}}$ có $P({A})={st_a}$ và $P({A}{B})= {st_ab}$. Tính xác suất $P({B}|{A})$ (kết quả làm tròn đến hàng phần trăm)."
    )
        

    kq=p_ab/p_a
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    kq_false = []
    while len(kq_false) < 10:
        num = random.random()
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(round(num,2))    
    
    kq2,kq3,kq4=random.sample(kq_false,3)
    st_kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    st_kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    st_kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    noi_dung_loigiai=(
    f"$P({B}|{A})=\\dfrac{{P({B}{A})}}{{P({A})}}=\\dfrac{{{st_ab}}}{{{st_a}}}={st_kq}$.\n\n"
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

#[D12_C6_B1_23]-M1. Cho A,B độc lập và có P(A). Tính xác suất P(A|B)
def newy25_L12_C6_B1_23():
    ten=["A","B","C","D","E","F"]
    A,B=random.sample(ten,2)
    p_a=random.randint(30,80)
    st_a=f"{round(p_a/100,2):.2f}".replace(".",",")

    p_ab=p_a-random.randint(5,28)

    st_ab=f"{round(p_ab/100,2):.2f}".replace(".",",")

    noi_dung=(
    f"Cho hai biến cố ${{{A}}}$ và ${{{B}}}$ độc lập có $P({A})={st_a}$. Tính xác suất $P({A}|{B})$ (kết quả làm tròn đến hàng phần trăm)."
    )
        

    kq=p_a/100
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    kq_false = [1-p_a/100]
    while len(kq_false) < 4:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)    
    
    kq2,kq3,kq4=random.sample(kq_false,3)
    st_kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    st_kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    st_kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    noi_dung_loigiai=(
    f"$P({A}|{B})=\\dfrac{{P({A}{B})}}{{P({B})}}=\\dfrac{{P({A})P({B})}}{{P({B})}}=P({A})={st_kq}$.\n\n"
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

#[D12_C6_B1_24]-M2. Cho P(A), P(B|A). Tính xác suất P(AB)
def newy25_L12_C6_B1_24():
    ten=["A","B","C","D","E","F"]
    A,B=random.sample(ten,2)
    p_a=random.randint(30,80)/100
    p_b_dk_a=random.randint(5,78)/100
    st_a=f"{round(p_a,2):.2f}".replace(".",",")
    st_b_dk_a=f"{round(p_b_dk_a,2):.2f}".replace(".",",")

    noi_dung=(
    f"Cho hai biến cố ${{{A}}}$ và ${{{B}}}$ có $P({A})={st_a}$ và $P({B}|{A})={st_b_dk_a}$. Tính xác suất $P({A}{B})$ (kết quả làm tròn đến hàng phần trăm)."
    )
        

    kq=p_a*p_b_dk_a
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)    
    
    kq2,kq3,kq4=random.sample(kq_false,3)
    st_kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    st_kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    st_kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    noi_dung_loigiai=(
    f"$P({B}|{A})=\\dfrac{{P({B}{A})}}{{P({A})}}\\Rightarrow P({A}{B})=P({A}).P({B}|{A})={st_a}.{st_b_dk_a}={st_kq}$.\n\n"
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

#[D12_C6_B1_25]-M2. Cho P(A) và P(AB). Tính xác suất P(B_|A)
def newy25_L12_C6_B1_25():
    ten=["A","B","C","D","E","F"]
    A,B=random.sample(ten,2)
    p_a=random.randint(35,80)/100
    p_ab=p_a-random.randint(5,30)/100
    st_a=f"{round(p_a,2):.2f}".replace(".",",")
    st_ab=f"{round(p_ab,2):.2f}".replace(".",",")

    noi_dung=(
    f"Cho hai biến cố ${{{A}}}$ và ${{{B}}}$ có $P({A})={st_a}$ và $P({A}{B})={st_ab}$. Tính xác suất $P(\\overline{{{B}}}|{A})$ (kết quả làm tròn đến hàng phần trăm).")
        

    kq=1-p_ab/p_a
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)    
    
    kq2,kq3,kq4=random.sample(kq_false,3)
    st_kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    st_kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    st_kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    noi_dung_loigiai=(
    f"$P(\\overline{{{B}}}|{A})=1-P({B}|{A})=1-\\dfrac{{P({B}{A})}}{{P({A})}}=\\dfrac{{{st_ab}}}{{{st_a}}}={st_kq}$.\n\n"
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

#[D12_C6_B1_26]-M2. Cho P(A), P(B), P(B|A). Tính xác suất P(A|B)
def newy25_L12_C6_B1_26():
    ten=["A","B","C","D","E","F"]
    A,B=random.sample(ten,2)
    

    ab=random.randint(5,40)
    a=ab+random.randint(30,50)
    b=ab+random.randint(20,40)
    b_dk_a=random.randint(10,50)

    st_a=f"{round(a/100,2):.2f}".replace(".",",")
    st_b=f"{round(b/100,2):.2f}".replace(".",",")
    st_ab=f"{round(a*b_dk_a/10000,2):.2f}".replace(".",",")
    st_b_dk_a=f"{round(b_dk_a/100,2):.2f}".replace(".",",")

    noi_dung=(
    f"Cho hai biến cố ${{{A}}}$ và ${{{B}}}$ có $P({A})={st_a}; P({B})={st_b}$ và $P({B}|{A})= {st_b_dk_a}$. Tính xác suất $P({A}|{B})$ (kết quả làm tròn đến hàng phần trăm)."
    )
        

    kq=(a*b_dk_a/b)/100
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    kq_false = []
    while len(kq_false) < 10:
        num = random.random()
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(round(num,2))    
    
    kq2,kq3,kq4=random.sample(kq_false,3)
    st_kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    st_kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    st_kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    noi_dung_loigiai=(
    f"$P({A}{B})=P({A}).P({B}|{A})={st_a}.{st_b_dk_a}={st_ab}$.\n\n"
    f"$P({A}|{B})=\\dfrac{{P({A}{B})}}{{P({B})}}=\\dfrac{{{st_ab}}}{{{st_b}}}={st_kq}$.\n\n"
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

#[D12_C6_B1_27]-M2. Cho P(A), P(B), P(AUB). Tính xác suất P(B|A)
def newy25_L12_C6_B1_27():
    ten=["A","B","C","D","E","F"]
    A,B=random.sample(ten,2)
    

    ab=random.randint(5,40)
    a=ab+random.randint(30,50)
    b=ab+random.randint(20,40)
    a_u_b=a+b-ab
    

    st_a=f"{round(a/100,2):.2f}".replace(".",",")
    st_b=f"{round(b/100,2):.2f}".replace(".",",")
    st_a_u_b=f"{round(a_u_b/100,2):.2f}".replace(".",",")    
    st_ab=f"{round(ab/100,2):.2f}".replace(".",",")

    noi_dung=(
    f"Cho hai biến cố ${{{A}}}$ và ${{{B}}}$ có $P({A})={st_a}; P({B})={st_b}$ và $P({A}\\cup {B})= {st_a_u_b}$. Tính xác suất $P({B}|{A})$ (kết quả làm tròn đến hàng phần trăm)."
    )
        

    kq=ab/a
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    kq_false = []
    while len(kq_false) < 10:
        num = random.random()
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(round(num,2))    
    
    kq2,kq3,kq4=random.sample(kq_false,3)
    st_kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    st_kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    st_kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    noi_dung_loigiai=(
    f"$P({B}{A})=P({A})+P({B})-P({A}\\cup {B})={st_a}+{st_b}-{st_a_u_b}={st_ab}$.\n\n"
    f"$P({B}|{A})=\\dfrac{{P({B}{A})}}{{P({A})}}=\\dfrac{{{st_ab}}}{{{st_a}}}={st_kq}$.\n\n"
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
    f" Tính xác suất $P({A})$ (kết quả làm tròn đến hàng phần trăm)."
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
    f"\\shortans[4]{{{dap_an}}}\n\n"\
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
f" Tính xác suất khách hàng không hài lòng về dịch vụ thuộc chi nhánh {ten_1} (kết quả làm tròn đến hàng phần trăm).")
    dap_an=st_p_a_dk_l

    noi_dung_loigiai=(
    f'Gọi A là biến cố "Khách hàng do chi nhánh {ten_1} phục vụ".\n\n'
    f'Gọi B là biến cố "Khách hàng do chi nhánh {ten_2} phục vụ".\n\n'
    f'Gọi L là biến cố "Khách hàng không hài lòng".\n\n'
    f'Xác suất khách hàng do chi nhánh {ten_1} phục vụ: $P(A)={p_a}\\%={st_p_a}$.\n\n'
    f'Xác suất khách hàng do chi nhánh {ten_1} phục vụ: $P(B)={p_b}\\%={st_p_b}$.\n\n'
    f'Xác suất khách hàng không hài lòng do chi nhánh {ten_1} phục vụ: $P(L|A)={p_l_dk_a}\\%={st_p_l_dk_a}$.\n\n'
    f'Xác suất khách hàng không hài lòng do chi nhánh {ten_2} phục vụ: $P(L|B)={p_l_dk_b}\\%={st_p_l_dk_b}$.\n\n'

    f'Xác suất để khách hàng không hài lòng của toàn bộ công ty:\n\n'
    f'$P(L)=P(A)P(L|A)+P(B)P(L|B)={st_p_a}.{st_p_l_dk_a}+{st_p_b}.{st_p_l_dk_b}={st_p_l}$.\n\n'
    f'Xác suất khách hàng không hài lòng do chi nhánh {ten_1} phục vụ:\n\n'
    f'$P(A|L)=\\dfrac{{P(A).P(L|A)}}{{P(L)}}=\\dfrac{{{st_p_a}.{st_p_l_dk_a}}}{{{st_p_l}}}={st_p_a_dk_l}.$')    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")

    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\shortans[4]{{{dap_an}}}\n\n"\
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
    f"\\shortans[4]{{{dap_an}}}\n\n"\
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
    f"\\shortans[4]{{{dap_an}}}\n\n"\
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
    f"\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_13]-SA-M2. X.s toàn phần: Tính x.s sinh viên làm việc đúng chuyên ngành
def newy25_L12_C6_B2_13():
    p_g=random.randint(10,30)
    p_k=100-p_g
    p_d_dk_g=random.randint(80,95)
    p_d_dk_k=random.randint(65,78)
    st_p_g=f"{round_half_up(p_g/100,2):.2f}".replace(".",",")
    st_p_k=f"{round_half_up(p_k/100,2):.2f}".replace(".",",")
    st_p_d_dk_g=f"{round_half_up(p_d_dk_g/100,2):.2f}".replace(".",",")
    st_p_d_dk_k=f"{round_half_up(p_d_dk_k/100,2):.2f}".replace(".",",")


    noi_dung = (
    f"Một trường đại học tiến hành khảo sát tình trạng việc làm sau khi tốt nghiệp của sinh viên."
    f" Kết quả khảo sát cho thấy tỉ lệ người tìm được việc làm đúng chuyên ngành là ${p_d_dk_g}\\%$ đối với sinh viên tốt nghiệp loại giỏi"
    f" và ${p_d_dk_k}\\%$ đối với sinh viên tốt nghiệp loại khác."
    f" Tỉ lệ sinh viên tốt nghiệp loại giỏi là ${p_g}\\%$."
    f" Chọn ngẫu nhiên một sinh viên đã tốt nghiệp của trường."
    f" Tính xác suất sinh viên đó tìm được việc làm đúng chuyên ngành (kết quả làm tròn đến hàng phần trăm)."

    )
    dap_an=f"{round_half_up((p_g*p_d_dk_g+p_k*p_d_dk_k)/10000,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f'Gọi G là biến cố: "Sinh viên tốt nghiệp loại giỏi".\n\n'
    f'Gọi K là biến cố: "Sinh viên tốt nghiệp loại khác".\n\n'
    f'Khi đó D|G là biến cố: "Sinh viên làm đúng chuyên ngành nếu tốt nghiệp loại giỏi".\n\n'
    f'Khi đó D|K là biến cố: "Sinh viên làm đúng chuyên ngành nếu tốt nghiệp loại khác".\n\n'
    f"Ta có: $P(G)={st_p_g},P(K)={st_p_k}, P(D|G)={st_p_d_dk_g}, P(D|K)={st_p_d_dk_k}$.\n\n"
    f"Xác suất để sinh viên đó tìm được việc làm đúng chuyên ngành:\n\n"
    f"$P(D)=P(G).P(D|G)+P(K).P(D|K)={st_p_g}.{st_p_d_dk_g}+{st_p_k}.{st_p_d_dk_k}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_14]-M2. X.s toàn phần:  Cho P(B), P(A|B), P(A|B_ngang). Tính P(A)
def newy25_L12_C6_B2_14():
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
    f" Tính xác suất $P({A})$ (kết quả làm tròn đến hàng phần trăm)."
    )
    kq=p_a_dk_b*p_b+p_a_dk_b_ngang*p_b_ngang
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f"Ta có: $P(\\overline{{{B}}})=1-P({B})={st_p_b_ngang}$.\n\n"
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P({A}) = P({A}|{B}). P({B}) + P\\left({A}|\\overline{{{B}}}\\right).P\\left(\\overline{{{B}}}\\right)$"
    f"$={st_p_a_dk_b}.{st_p_b}+{st_p_a_dk_b_ngang}.{st_p_b_ngang}={kq}$."
    )   
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D12_C6_B2_15]-M2. X.s toàn phần:  Cho P(B), tỉ lệ A xảy ra nếu B, A xảy ra nếu B không xảy ra. Tính P(A).
def newy25_L12_C6_B2_15():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    b=random.randint(10,70)
    p_b=b/100
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    p_b_ngang=1-p_b
    st_p_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")


    a_dk_b=random.randint(5,40)
    p_a_dk_b=a_dk_b/100
    st_p_a_dk_b=f"{round_half_up(p_a_dk_b,2)}".replace(".",",")

    a_dk_b_ngang=random.randint(45,75)
    p_a_dk_b_ngang=a_dk_b_ngang/100
    st_p_a_dk_b_ngang=f"{round_half_up(p_a_dk_b_ngang,2)}".replace(".",",")

    noi_dung=(
    f"Cho ${{{A},{B}}}$ là các biến cố. Biết $P({B})={st_p_b}$."
    f" Nếu ${{{B}}}$ xảy ra thì tỉ lệ ${{{A}}}$ xảy ra là ${a_dk_b}\\%$."
    f" Nếu ${{{B}}}$ không xảy ra thì tỉ lệ ${{{A}}}$ xảy ra là ${a_dk_b_ngang}\\%$."
    f" Tính xác suất của biến cố ${{{A}}}$ (kết quả làm tròn đến hàng phần trăm)." )
    

    kq=p_a_dk_b*p_b+p_a_dk_b_ngang*p_b_ngang
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
  

    noi_dung_loigiai=(
    f"Ta có: $P(\\overline{{{B}}})=1-P({B})={st_p_b_ngang}, P({A}|{B})={st_p_a_dk_b}, P({A}|\\overline{{{B}}})={st_p_a_dk_b_ngang}$.\n\n"
    f"$P({A})=P({A}|{B}).P({B})+P({A}|\\overline{{{B}}}).P(\\overline{{{B}}})$"
    f" $={st_p_a_dk_b}.{st_p_b}+{st_p_a_dk_b_ngang}.{st_p_b_ngang}={kq}$."
    )

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D12_C6_B2_16]-M2. X.s toàn phần:  Cho P(A), P(A|B), P(A|B_ngang). Tính P(B).
def newy25_L12_C6_B2_16():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    b=random.randint(35,70)
    p_b=b/100
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    p_b_ngang=1-p_b
    st_p_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")


    a_dk_b=random.randint(45,60)
    p_a_dk_b=a_dk_b/100
    st_p_a_dk_b=f"{round_half_up(p_a_dk_b,2)}".replace(".",",")

    a_dk_b_ngang=random.randint(5,20)
    p_a_dk_b_ngang=a_dk_b_ngang/100
    st_p_a_dk_b_ngang=f"{round_half_up(p_a_dk_b_ngang,2)}".replace(".",",")

    a=random.randint(22,40)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    noi_dung = (
    f"Cho hai biến cố ${{{A}}}$, ${{{B}}}$ với $P({A})={st_p_a}$; $P({A}|{B}) ={st_p_a_dk_b}$ và $P\\left({A}|\\overline{{{B}}}\\right)={st_p_a_dk_b_ngang}$."
    f" Tính xác suất $P({B})$ (kết quả làm tròn đến hàng phần trăm)."
    )

    x=sp.symbols("x")
    eq=Eq(p_a,p_a_dk_b*x+p_a_dk_b_ngang*(1-x))
    tap_nghiem=solve(eq,x)
    p_b=tap_nghiem[0]
    kq=f"{round_half_up(p_b,2):.2f}".replace(".",",")

    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    noi_dung_loigiai=(
    f"Đặt $P({B})=x \\Rightarrow P(\\overline{{{B}}})=1-x$.\n\n"
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P({A}) = P({A}|{B}). P({B}) + P\\left({A}|\\overline{{{B}}}\\right).P\\left(\\overline{{{B}}}\\right)$\n\n"
    f"$\\Leftrightarrow {st_p_a}={st_p_a_dk_b}x+{st_p_a_dk_b_ngang}(1-x)$\n\n"
    f"$\\Rightarrow x={kq}$."
    )   
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D12_C6_B2_17]-M2. X.s tphần:  Cho P(B):Tỉ lệ tiêm vắc xin, P(A|B):tỉ lệ mắc bệnh nếu tiêm , P(A|B_ngang):tỉ lệ mắc bệnh nếu chưa tiêm. Tính P(A): x.s mắc bệnh
def newy25_L12_C6_B2_17():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    b=random.randint(50,75)
    p_b=b/100
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    p_b_ngang=1-p_b
    st_p_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")


    a_dk_b=random.randint(5,20)
    p_a_dk_b=a_dk_b/100
    st_p_a_dk_b=f"{round_half_up(p_a_dk_b,2)}".replace(".",",")

    a_dk_b_ngang=random.randint(45,85)
    p_a_dk_b_ngang=a_dk_b_ngang/100
    st_p_a_dk_b_ngang=f"{round_half_up(p_a_dk_b_ngang,2)}".replace(".",",")

    noi_dung = (
    f"Tỉ lệ người dân đã tiêm vắc xin phòng bệnh X ở một địa phương là ${b}\\%$."
    f" Trong số những người đã tiêm phòng, tỉ lệ mắc bệnh X là ${a_dk_b}\\%$,"
    f" còn trong số những người chưa tiêm, tỉ lệ mắc bệnh X là ${a_dk_b_ngang}\\%$."
    f" Gặp ngẫu nhiên một người ở địa phương đó. Xác suất người đó mắc bệnh X là (kết quả làm tròn đến hàng phần trăm)."
    )
    kq=p_a_dk_b*p_b+p_a_dk_b_ngang*p_b_ngang
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f' Gọi ${{M}}$ là biến cố "người được gặp mắc bệnh".\n\n'
    f' Gọi ${{T}}$ là biến cố "người được gặp đã tiêm phòng vắc xin".\n\n'
    f' Suy ra $\\overline{{T}}$ là biến cố "người được gặp chưa tiêm phòng vắc xin".\n\n'
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P(M) = P(M|T). P(T) + P\\left(M|\\overline{{T}}\\right).P\\left(\\overline{{T}}\\right)$"
    f"$={st_p_a_dk_b}.{st_p_b}+{st_p_a_dk_b_ngang}.{st_p_b_ngang}={kq}$."
    )   
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D12_C6_B2_18]-M2. X.s tphần:  Cho tỉ lệ hút thuốc, tỉ lệ mắc bệnh nếu hút, tỉ lệ mắc bệnh nếu không hút. Tính x.s mắc bệnh
def newy25_L12_C6_B2_18():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    b=random.randint(15,35)
    p_b=b/100
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    p_b_ngang=1-p_b
    st_p_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")


    a_dk_b=random.randint(55,85)
    p_a_dk_b=a_dk_b/100
    st_p_a_dk_b=f"{round_half_up(p_a_dk_b,2)}".replace(".",",")

    a_dk_b_ngang=random.randint(5,25)
    p_a_dk_b_ngang=a_dk_b_ngang/100
    st_p_a_dk_b_ngang=f"{round_half_up(p_a_dk_b_ngang,2)}".replace(".",",")

    noi_dung = (
    f"Kết quả khảo sát tại một xã cho thấy có ${b}\\%$ cư dân hút thuốc lá."
    f" Tỉ lệ cư dân thường xuyên gặp các vấn đề sức khoẻ về đường hô hấp trong số những người hút thuốc lá và không hút thuốc lá lần lượt là ${a_dk_b}\\%$, ${a_dk_b_ngang}\\%$."
    f" Tỉ lệ gặp một cư dân của xã thì xác suất người đó thường xuyên gặp các vấn đề sức khoẻ về đường hô hấp là bao nhiêu phần trăm (kết quả làm tròn đến hàng đơn vị)?"
    )
    kq=p_a_dk_b*p_b+p_a_dk_b_ngang*p_b_ngang
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    kq=f"{round_half_up(kq*100,0)}".replace(".0","")

    noi_dung_loigiai=(
    f' Gọi ${{B}}$ là biến cố "người được gặp thường xuyên gặp các vấn đề sức khoẻ về đường hô hấp".\n\n'
    f' Gọi ${{H}}$ là biến cố "người được gặp có hút thuốc lá".\n\n'
    f' Suy ra $\\overline{{H}}$ là biến cố "người được gặp không hút thuốc lá".\n\n'
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P(B) = P(B|H). P(H) + P\\left(B|\\overline{{H}}\\right).P\\left(\\overline{{H}}\\right)$"
    f"$={st_p_a_dk_b}.{st_p_b}+{st_p_a_dk_b_ngang}.{st_p_b_ngang}={kq}\\%$."
    )   
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=f"{round_half_up(kq2*100,0)}".replace(".0","")
    kq3=f"{round_half_up(kq3*100,0)}".replace(".0","")
    kq4=f"{round_half_up(kq4*100,0)}".replace(".0","")
    

    pa_A= f"*${{{kq}}}\\%$"
    pa_B= f"${{{kq2}}}\\%$"
    pa_C= f"${{{kq3}}}\\%$"
    pa_D= f"${{{kq4}}}\\%$"
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

#[D12_C6_B2_19]-M3. X.s tphần:  Cho 2 phòng khả năng chọn như nhau, cho tỉ lệ bệnh nhân nam ở các phòng. Tính x.s người bệnh là nam
def newy25_L12_C6_B2_19():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    b=50
    p_b=b/100
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    p_b_ngang=1-p_b
    st_p_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")


    a_dk_b=random.randint(55,75)
    p_a_dk_b=a_dk_b/100
    st_p_a_dk_b=f"{round_half_up(p_a_dk_b,2)}".replace(".",",")

    a_dk_b_ngang=random.randint(45,65)
    if a_dk_b_ngang==a_dk_b:
        a_dk_b_ngang+=5
    p_a_dk_b_ngang=a_dk_b_ngang/100
    st_p_a_dk_b_ngang=f"{round_half_up(p_a_dk_b_ngang,2)}".replace(".",",")

    nam=random.choice(["nam", "nữ"])

    noi_dung = (
    f"Một bệnh viện có hai phòng khám là phòng ${{A}}$ và phòng ${{B}}$ với khả năng lựa chọn của bệnh nhân là như nhau."
    f" Tỉ lệ bệnh nhân {nam} có ở phòng ${{A}}$ và phòng ${{B}}$ lần lượt là lần lượt là ${a_dk_b}\\%$ và ${a_dk_b_ngang}\\%$."
    f" Chọn ngẫu nhiên một người bệnh từ hai phòng khám. Xác suất người bệnh này là {nam} là (kết quả làm tròn đến hàng phần trăm)"
    )
    kq=p_a_dk_b*p_b+p_a_dk_b_ngang*p_b_ngang
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f' Gọi ${{N}}$ là biến cố "người bệnh được chọn là {nam}".\n\n'
    f' Gọi ${{A}}$ là biến cố "người bệnh được chọn ở phòng khám A".\n\n'
    f' Gọi ${{B}}$ là biến cố "người bệnh được chọn ở phòng khám B".\n\n'
    f' Ta có: $P(A)=P(B)=0,5$.\n\n'
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P(N) = P(N|A). P(A) + P\\left(N|B\\right).P(B)$"
    f"$={st_p_a_dk_b}.{st_p_b}+{st_p_a_dk_b_ngang}.{st_p_b_ngang}={kq}$."
    )   
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D12_C6_B2_20]-M3. X.s tphần:  Lấy 1 bi từ hộp I bỏ qua hộp II. Tính x.s hai bi lấy từ hộp hai có màu nào đó.
def newy25_L12_C6_B2_20():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)   

    mau=["xanh", "đỏ", "trắng", "đen", "vàng"]
    xanh, do=random.sample(mau,2)
    while True:
        X1=random.randint(3,8)
        D1=random.randint(3,9)
        X2=random.randint(3,10)
        D2=random.randint(4,11)
        if X1!=X2 or D1!=D2:
            break

    noi_dung = (
    f"Hộp thứ nhất có ${{{X1}}}$ viên bi {xanh} và ${{{D1}}}$ viên bi {do}. Hộp thứ hai có ${{{X2}}}$ viên bi {xanh} và ${{{D2}}}$ viên bi {do}."
    f" Các viên bi có cùng kích thước và khối lượng. Lấy ra ngẫu nhiên 1 viên bi từ hộp thứ nhất" 
    f" chuyển sang hộp thứ hai. Sau đó lại lấy ra ngẫu nhiên đồng thời 2 viên bi từ hộp thứ hai." 
    f" Xác suất để hai viên bi lấy ra từ hộp thứ hai là bi {xanh} là"   )   

    
    tong=X2+D2+1
    p_a=X1/(X1+D1)
    p_a_ngang=1-p_a
    p_b_dk_a=binomial(X2+1,2)/binomial(tong,2)
    p_b_dk_a_ngang=binomial(X2,2)/binomial(tong,2)
    kq=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang

    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    noi_dung_loigiai=(
    f' Gọi ${{A}}$ là biến cố "Viên bi được chuyển từ hộp thứ nhất sang hộp thứ hai là viên bi {xanh}".\n\n'
    f' Gọi ${{B}}$ là biến cố "Hai viên bi được lấy ngẫu nhiên đồng thời từ hộp thứ hai là bi {xanh}".\n\n'
    f' Ta có: $P(A)=\\dfrac{{{X1}}}{{{X1}+{D1}}}={phan_so(p_a)}$.\n\n'
    f' Ta có: $P(\\overline{{A}})=1-{phan_so(X1/(X1+D1))}={phan_so(p_a_ngang)}$.\n\n'
    f' $P(B|A)=\\dfrac{{{ckn(2,X1+X2)}}}{{{ckn(2,tong)}}}={phan_so(p_b_dk_a)}$.\n\n'
    f' $P(B|\\overline{{A}})=\\dfrac{{{ckn(2,X2)}}}{{{ckn(2,tong)}}}={phan_so(p_b_dk_a_ngang)}$.\n\n'

    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P(B) = P(B|A). P(A) + P\\left(B|\\overline{{A}}\\right).P(\\overline{{A}})$"
    f"$={phan_so(p_b_dk_a)}.{phan_so(p_a)}+{phan_so(p_b_dk_a_ngang)}.{phan_so(p_a_ngang)}={phan_so(kq)}$."
    )  
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=phan_so(kq2)
    kq3=phan_so(kq3)
    kq4=phan_so(kq4)
    

    pa_A= f"*${{{phan_so(kq)}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D12_C6_B2_21]-SA-M3. X.s tphần:  Lấy 1 bi từ hộp I bỏ qua hộp II. Tính x.s hai bi lấy từ hộp hai có màu nào đó.
def newy25_L12_C6_B2_21():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)   

    mau=["xanh", "đỏ", "trắng", "đen", "vàng"]
    xanh, do=random.sample(mau,2)
    while True:
        X1=random.randint(3,8)
        D1=random.randint(3,9)
        X2=random.randint(3,10)
        D2=random.randint(4,11)
        if X1!=X2 or D1!=D2:
            break

    noi_dung = (
    f"Hộp thứ nhất có ${{{X1}}}$ viên bi {xanh} và ${{{D1}}}$ viên bi {do}. Hộp thứ hai có ${{{X2}}}$ viên bi {xanh} và ${{{D2}}}$ viên bi {do}."
    f" Các viên bi có cùng kích thước và khối lượng. Lấy ra ngẫu nhiên 1 viên bi từ hộp thứ nhất" 
    f" chuyển sang hộp thứ hai. Sau đó lại lấy ra ngẫu nhiên đồng thời 2 viên bi từ hộp thứ hai." 
    f" Xác suất để hai viên bi lấy ra từ hộp thứ hai là bi {xanh} là (kết quả làm tròn đến hàng phần trăm)"   )   

    
    tong=X2+D2+1
    p_a=X1/(X1+D1)
    p_a_ngang=1-p_a
    p_b_dk_a=binomial(X2+1,2)/binomial(tong,2)
    p_b_dk_a_ngang=binomial(X2,2)/binomial(tong,2)
    kq=f"{round_half_up(p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang,2):.2f}".replace(".",",")

    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    noi_dung_loigiai=(
    f' Gọi ${{A}}$ là biến cố "Viên bi được chuyển từ hộp thứ nhất sang hộp thứ hai là viên bi {xanh}".\n\n'
    f' Gọi ${{B}}$ là biến cố "Hai viên bi được lấy ngẫu nhiên đồng thời từ hộp thứ hai là bi {xanh}".\n\n'
    f' Ta có: $P(A)=\\dfrac{{{X1}}}{{{X1}+{D1}}}={phan_so(p_a)}$.\n\n'
    f' Ta có: $P(\\overline{{A}})=1-{phan_so(X1/(X1+D1))}={phan_so(p_a_ngang)}$.\n\n'
    f' $P(B|A)=\\dfrac{{{ckn(2,X1+X2)}}}{{{ckn(2,tong)}}}={phan_so(p_b_dk_a)}$.\n\n'
    f' $P(B|\\overline{{A}})=\\dfrac{{{ckn(2,X2)}}}{{{ckn(2,tong)}}}={phan_so(p_b_dk_a_ngang)}$.\n\n'

    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P(B) = P(B|A). P(A) + P\\left(B|\\overline{{A}}\\right).P(\\overline{{A}})$"
    f"$={phan_so(p_b_dk_a)}.{phan_so(p_a)}+{phan_so(p_b_dk_a_ngang)}.{phan_so(p_a_ngang)}={kq}$." )  
    
    
    dap_an=kq
    

    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_22]-M2. X.s tphần:  Cho x.s mắc ung thư, x.s chẩn đoán đúng, x.s chẩn đoán sai. Tính x.s chẩn đoán không ung thư
def newy25_L12_C6_B2_22():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    a=random.randint(5,15)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    p_a_ngang=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(55,80)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(5,30)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")
    tuoi=random.choice([10*i for i in range(3,7) ])

    noi_dung = (
    f"Ở một địa phương $X$, xác suất để một người lớn trên ${{40}}$ tuổi mắc bệnh ung thư là ${{{st_p_a}}}$."
    f"  Xác suất bác sĩ chẩn đoán đúng một người mắc bệnh ung thư là ${{{st_p_b_dk_a}}}$"
    f" và chẩn đoán sai (không bị ung thư nhưng được chẩn đoán mắc bệnh) là ${{{st_p_b_dk_a_ngang}}}$."
    f" Xác suất để một người nhận được kết quả chẩn đoán không bị ung thư bằng (kết quả làm tròn đến hàng phần trăm)."
    )
    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    kq=1-p_b

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=round(kq, 2), num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f' Gọi ${{A}}$ là biến cố "Người đó mắc ung thư".\n\n'
    f' Gọi ${{B}}$ là biến cố "Bác sĩ chẩn đoán người đó bị ung thư".\n\n'
    f' $\\overline{{B}}$ là biến cố "Bác sĩ chẩn đoán người đó không bị ung thư".\n\n'
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P(B) = P(B|A). P(A) + P\\left(B|\\overline{{A}}\\right).P\\left(\\overline{{A}}\\right)$"
    f"$={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={phan_so(p_b)}$.\n\n"
    f"Xác suất để một người nhận được kết quả chẩn đoán không bị ung thư:\n\n"
    f"$P(\\overline{{B}})=1-P(B)=1-{phan_so(p_b)}={kq}$."
    )
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")
    

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
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

#[D12_C6_B2_23]-SA-M3. x.s tphần:  Cho x.s mắc ung thư, x.s chẩn đoán đúng, x.s chẩn đoán sai. Tính x.s chẩn đoán không ung thư
def newy25_L12_C6_B2_23():
    bien_co=["A","B","C","D","E","F"]    
    A,B=random.sample(bien_co,2)

    a=random.randint(5,15)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    p_a_ngang=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(55,80)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(5,30)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")
    tuoi=random.choice([10*i for i in range(3,7) ])

    noi_dung = (
    f"Ở một địa phương $X$, xác suất để một người lớn trên ${{40}}$ tuổi mắc bệnh ung thư là ${{{st_p_a}}}$."
    f"  Xác suất bác sĩ chẩn đoán đúng một người mắc bệnh ung thư là ${{{st_p_b_dk_a}}}$"
    f" và chẩn đoán sai (không bị ung thư nhưng được chẩn đoán mắc bệnh) là ${{{st_p_b_dk_a_ngang}}}$."
    f" Xác suất để một người nhận được kết quả chẩn đoán không bị ung thư bằng (kết quả làm tròn đến hàng phần trăm)."
    )
    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    kq=1-p_b

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)

    dap_an=f"{round_half_up(kq,2):.2f}".replace(".",",")

    noi_dung_loigiai=(
    f' Gọi ${{A}}$ là biến cố "Người đó mắc ung thư".\n\n'
    f' Gọi ${{B}}$ là biến cố "Bác sĩ chẩn đoán người đó bị ung thư".\n\n'
    f' $\\overline{{B}}$ là biến cố "Bác sĩ chẩn đoán người đó không bị ung thư".\n\n'
    f"Áp dụng công thức toàn phần ta có:\n\n"
    f"$P(B) = P(B|A). P(A) + P\\left(B|\\overline{{A}}\\right).P\\left(\\overline{{A}}\\right)$"
    f"$={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={phan_so(p_b)}$.\n\n"
    f"Xác suất để một người nhận được kết quả chẩn đoán không bị ung thư:\n\n"
    f"$P(\\overline{{B}})=1-P(B)=1-{phan_so(p_b)}={dap_an}$."
    )    
        
    debai_word= f"{noi_dung}\n"

    loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
        f"Đáp án: {dap_an}\n")


    latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
    f"\\end{{ex}}\n"
    return debai_word,loigiai_word,latex_tuluan,dap_an

#[D12_C6_B2_24]-TF-M3. Cho tỉ lệ nam tham gia, tỉ lệ nam đậu sát hạch, nữ đậu sát hạch. Xét Đ-S: tỉ lệ nữ, x.s nam đậu, x.s nữ đậu, x.s đậu
def newy25_L12_C6_B2_24():
    a=random.randint(60,75)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    b=100-a
    p_a_ngang=1-p_a
    p_b=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(65,90)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(55,85)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    p_not_d_dk_nu=1-p_b_dk_a_ngang
    st_p_not_d_dk_nu=f"{round_half_up(p_not_d_dk_nu,2)}".replace(".",",")

    noi_dung = f" Trong một kì sát hạch lái xe có ${a}\\%$ thí sinh nam. Biết rằng ${b_dk_a}\\%$ thí sinh nam và ${b_dk_a_ngang}\\% $ thí sinh nữ đỗ sát hạch kì này. Chọn ngẫu nhiên một thí sinh trong kỳ sát hạch. Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm)."        
    debai_word= f"{noi_dung}\n"

    
    kq1_T=f"* Tỉ lệ chọn được một thí sinh nữ là ${b}\\%$" 
    kq1_F=f"Tỉ lệ chọn được một thí sinh nữ là ${b-random.randint(1,5)}\\%$"
    
    HDG=f"Theo đề bài ta có: $P(M)={a}\\%={st_p_a} \\Rightarrow P(N)={b}\\%={st_p_b}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_d_nam=f"{round_half_up(p_b_dk_a*p_a,2)}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b_dk_a*p_a, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_d_nam_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")


    kq2_T=f"* Xác suất chọn được một thí sinh nam và đỗ sát hạch là ${{{p_d_nam}}}$"
    kq2_F=f"Xác suất chọn được một thí sinh nam và đỗ sát hạch là ${{{p_d_nam_false}}}$"
    
    HDG=f"Xác suất chọn được một thí sinh nam và đỗ sát hạch là: \n\n $P(DM)=P(D|M).P(M)={b_dk_a}.{p_a}={p_d_nam}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_not_d_nu=f"{round_half_up(p_not_d_dk_nu*p_b,2):.2f}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_not_d_dk_nu*p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_not_d_nu_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")

    kq3_T=f"* Xác suất chọn được một thí sinh nữ và không đỗ sát hạch là ${{{p_not_d_nu}}}$" 
    kq3_F=f"Xác suất chọn được một thí sinh nữ và không đỗ sát hạch là ${{{p_not_d_nu_false}}}$"
    
    HDG=(f" Xác suất chọn được một không đỗ sát hạch là nữ bằng:\n\n"
        f" $P(\\overline{{D}}N)=P(\\overline{{D}}|N).P(N)={st_p_not_d_dk_nu}.{st_p_b}={p_not_d_nu}$.\n\n"
        )
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)

    kq_false=random.choice(kq_false)
    st_p_b_false=f"{round_half_up(kq_false,2)}".replace(".",",")

    kq4_T=f"* Xác suất chọn được một thí sinh đỗ sát hạch là ${{{st_p_b}}}$"
    kq4_F=f"Xác suất chọn được một thí sinh đỗ sát hạch là ${{{st_p_b_false}}}$" 
    
    HDG=(f"Xác suất chọn được một thí sinh đỗ sát hạch là:\n\n"
        f"$P(D)=P(D|M).P(M)+P(D|N).P(N)={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={st_p_b}$.")
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

    noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n\n"
        f"Xét các biến cố sau:\n\n"
        f"${{D}}$: Thí sinh đỗ kì sát hạch\n\n"
        f"${{M}}$: Thí sinh là nam giới\n\n"
        f"${{N}}$: Thí sinh là nữ giới\n\n"
        f"${{D|M}}$: Thí sinh nam đỗ kì sát hạch\n\n"
        f"${{D|N}}$: Thí sinh nữ đỗ kì sát hạch\n\n"
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

#[D12_C6_B2_25]-TF-M3. Cho tỉ lệ ứng viên có kinh nghiệm, tỉ lệ ứng viên có kinh nghiệ vượt qua vòng phỏng vấn. Xét Đ-S: x.s giao, x.s toàn phần
def newy25_L12_C6_B2_25():
    a=random.randint(60,75)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    b=100-a
    p_a_ngang=1-p_a
    p_b=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(65,90)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(45,65)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    p_not_d_dk_nu=1-p_b_dk_a_ngang
    st_p_not_d_dk_nu=f"{round_half_up(p_not_d_dk_nu,2)}".replace(".",",")

    noi_dung = f" Trong một đợt tuyển dụng của công ty, có ${a}\\%$ ứng viên có kinh nghiệm. Biết rằng ${b_dk_a}\\%$ ứng viên có kinh nghiệm và ${b_dk_a_ngang}\\% $ ứng viên chưa có kinh nghiệm vượt qua vòng phỏng vấn. Chọn ngẫu nhiên một ứng viên trong đợt tuyển dụng. Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm)."        
    debai_word= f"{noi_dung}\n"

    
    kq1_T=f"* Tỉ lệ chọn được một ứng viên chưa có kinh nghiệm là ${b}\\%$" 
    kq1_F=f"Tỉ lệ chọn được một ứng viên chưa có kinh nghiệm ${b-random.randint(1,5)}\\%$"
    
    HDG=f"Theo đề bài ta có: $P(M)={a}\\%={st_p_a} \\Rightarrow P(N)={b}\\%={st_p_b}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_d_nam=f"{round_half_up(p_b_dk_a*p_a,2)}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b_dk_a*p_a, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_d_nam_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")


    kq2_T=f"* Xác suất chọn được một ứng viên có kinh nghiệm và vượt qua phỏng vấn là ${{{p_d_nam}}}$"
    kq2_F=f"Xác suất chọn được một ứng viên có kinh nghiệm và vượt qua phỏng vấn là ${{{p_d_nam_false}}}$"
    
    HDG=f"Xác suất chọn được một ứng viên có kinh nghiệm và vượt qua phỏng vấn là: \n\n $P(DM)=P(D|M).P(M)={b_dk_a}.{p_a}={p_d_nam}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_not_d_nu=f"{round_half_up(p_not_d_dk_nu*p_b,2):.2f}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_not_d_dk_nu*p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_not_d_nu_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")

    kq3_T=f"* Xác suất chọn được một ứng viên chưa có kinh nghiệm và không vượt qua phỏng vấn là ${{{p_not_d_nu}}}$" 
    kq3_F=f"Xác suất chọn được một ứng viên chưa có kinh nghiệm và không vượt qua phỏng vấn là ${{{p_not_d_nu_false}}}$"
    
    HDG=(f" Xác suất chọn được một ứng viên chưa có kinh nghiệm và không vượt qua phỏng vấn là:\n\n"
        f" $P(\\overline{{D}}N)=P(\\overline{{D}}|N).P(N)={st_p_not_d_dk_nu}.{st_p_b}={p_not_d_nu}$.\n\n"
        )
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)

    kq_false=random.choice(kq_false)
    st_p_b_false=f"{round_half_up(kq_false,2)}".replace(".",",")

    kq4_T=f"* Xác suất chọn được một ứng viên vượt qua phỏng vấn là ${{{st_p_b}}}$"
    kq4_F=f"Xác suất chọn được một ứng viên vượt qua phỏng vấn là ${{{st_p_b_false}}}$" 
    
    HDG=(f"Xác suất chọn được một ứng viên vượt qua phỏng vấn là:\n\n"
        f"$P(D)=P(D|M).P(M)+P(D|N).P(N)={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={st_p_b}$.")
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

    noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n\n"
        f"Xét các biến cố sau:\n\n"
        f"${{D}}$: ứng viên vượt qua vòng phỏng vấn\n\n"
        f"${{M}}$: ứng viên có kinh nghiệm\n\n"
        f"${{N}}$: ứng viên không có kinh nghiệm\n\n"
        f"${{D|M}}$: ứng viên vượt qua vòng phỏng vấn với điều kiện có kinh nghiệm\n\n"
        f"${{D|N}}$: ứng viên vượt qua vòng phỏng vấn với điều kiện không có kinh nghiệm\n\n"
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

#[D12_C6_B2_26]-TF-M3. Cho tỉ lệ sinh viên ngành kĩ thuật-kinh thế, tỉ lệ sinh viên vượt qua kỳ thi cuối kỳ. Xét Đ-S: x.s giao, x.s toàn phần
def newy25_L12_C6_B2_26():
    a=random.randint(60,75)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    b=100-a
    p_a_ngang=1-p_a
    p_b=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(65,90)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(55,85)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    p_not_d_dk_nu=1-p_b_dk_a_ngang
    st_p_not_d_dk_nu=f"{round_half_up(p_not_d_dk_nu,2)}".replace(".",",")

    noi_dung = f" Trong một khoá học, có ${a}\\%$ sinh viên học ngành Kỹ thuật, số còn lại học ngành Kinh tế. Biết rằng ${b_dk_a}\\%$ sinh viên Kỹ thuật và ${b_dk_a_ngang}\\% $ sinh viên Kinh tế vượt qua kỳ thi cuối kỳ. Chọn ngẫu nhiên một sinh viên trong khóa học. Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm)."        
    debai_word= f"{noi_dung}\n"

    
    kq1_T=f"* Tỉ lệ sinh viên học ngành Kinh tế là ${b}\\%$" 
    kq1_F=f"Tỉ lệ sinh viên học ngành Kinh tế là ${b-random.randint(1,5)}\\%$"
    
    HDG=f"Theo đề bài ta có: $P(M)={a}\\%={st_p_a} \\Rightarrow P(N)={b}\\%={st_p_b}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_d_nam=f"{round_half_up(p_b_dk_a*p_a,2)}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b_dk_a*p_a, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_d_nam_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")


    kq2_T=f"* Xác suất chọn được sinh viên Kỹ thuật vượt qua kỳ thi là ${{{p_d_nam}}}$"
    kq2_F=f"Xác suất chọn được sinh viên Kỹ thuật vượt qua kỳ thi là ${{{p_d_nam_false}}}$"
    
    HDG=f"Xác suất chọn được sinh viên Kỹ thuật vượt qua kỳ thi là: \n\n $P(DM)=P(D|M).P(M)={b_dk_a}.{p_a}={p_d_nam}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_not_d_nu=f"{round_half_up(p_not_d_dk_nu*p_b,2):.2f}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_not_d_dk_nu*p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_not_d_nu_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")

    kq3_T=f"* Xác suất chọn được sinh viên Kinh tế không vượt qua kỳ thi là ${{{p_not_d_nu}}}$" 
    kq3_F=f"Xác suất chọn được sinh viên Kinh tế không vượt qua kỳ thi là ${{{p_not_d_nu_false}}}$"
    
    HDG=(f" Xác suất chọn được sinh viên Kinh tế không vượt qua kỳ thi là:\n\n"
        f" $P(\\overline{{D}}N)=P(\\overline{{D}}|N).P(N)={st_p_not_d_dk_nu}.{st_p_b}={p_not_d_nu}$.\n\n"
        )
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)

    kq_false=random.choice(kq_false)
    st_p_b_false=f"{round_half_up(kq_false,2)}".replace(".",",")

    kq4_T=f"*  Xác suất chọn được sinh viên vượt qua kỳ thi là ${{{st_p_b}}}$"
    kq4_F=f"Xác suất chọn được sinh viên vượt qua kỳ thi là ${{{st_p_b_false}}}$" 
    
    HDG=(f" Xác suất chọn được sinh viên vượt qua kỳ thi là:\n\n"
        f"$P(D)=P(D|M).P(M)+P(D|N).P(N)={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={st_p_b}$.")
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

    noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n\n"
        f"Xét các biến cố sau:\n\n"
        f"${{D}}$: sinh viên vượt qua kỳ thi\n\n"
        f"${{M}}$: sinh viên học Kỹ thuật\n\n"
        f"${{N}}$: sinh viên học Kinh tế\n\n"
        f"${{D|M}}$: sinh viên vượt qua kỳ thi với điều kiện là sinh viên Kỹ thuật\n\n"
        f"${{D|N}}$: sinh viên vượt qua kỳ thi với điều kiện là sinh viên Kinh tế\n\n"
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

#[D12_C6_B2_27]-TF-M3. Cho tỉ lệ người có bảo hiểm, tỉ lệ người có-không có bảo hiểm và được hỗ trợ chi phí. Xét Đ-S: x.s giao, x.s toàn phần
def newy25_L12_C6_B2_27():
    a=random.randint(60,75)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    b=100-a
    p_a_ngang=1-p_a
    p_b=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(80,90)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(45,65)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    p_not_d_dk_nu=1-p_b_dk_a_ngang
    st_p_not_d_dk_nu=f"{round_half_up(p_not_d_dk_nu,2)}".replace(".",",")

    noi_dung = f" Trong một khảo sát, có ${a}\\%$ người tham gia có bảo hiểm y tế. Biết rằng ${b_dk_a}\\%$ người có bảo hiểm và ${b_dk_a_ngang}\\% $ người không có bảo hiểm được hỗ trợ chi phí khám chữa bệnh. Chọn ngẫu nhiên một người từ khảo sát. Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm)."        
    debai_word= f"{noi_dung}\n"

    
    kq1_T=f"* Tỉ lệ người không có bảo hiểm y tế là ${b}\\%$" 
    kq1_F=f"Tỉ lệ người không có bảo hiểm y tế là ${b-random.randint(1,5)}\\%$"
    
    HDG=f"Theo đề bài ta có: $P(M)={a}\\%={st_p_a} \\Rightarrow P(N)={b}\\%={st_p_b}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_d_nam=f"{round_half_up(p_b_dk_a*p_a,2)}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b_dk_a*p_a, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_d_nam_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")


    kq2_T=f"* Xác suất chọn được người có bảo hiểm và được hỗ trợ chi phí là ${{{p_d_nam}}}$"
    kq2_F=f"Xác suất chọn được người có bảo hiểm và được hỗ trợ chi phí là ${{{p_d_nam_false}}}$"
    
    HDG=f"Xác suất chọn được người có bảo hiểm và được hỗ trợ chi phí là: \n\n $P(DM)=P(D|M).P(M)={b_dk_a}.{p_a}={p_d_nam}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_not_d_nu=f"{round_half_up(p_not_d_dk_nu*p_b,2):.2f}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_not_d_dk_nu*p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_not_d_nu_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")

    kq3_T=f"* Xác suất chọn được người không có bảo hiểm và không được hỗ trợ là ${{{p_not_d_nu}}}$" 
    kq3_F=f"Xác suất chọn được người không có bảo hiểm và không được hỗ trợ là ${{{p_not_d_nu_false}}}$"
    
    HDG=(f" Xác suất chọn được người không có bảo hiểm và không được hỗ trợ là:\n\n"
        f" $P(\\overline{{D}}N)=P(\\overline{{D}}|N).P(N)={st_p_not_d_dk_nu}.{st_p_b}={p_not_d_nu}$.\n\n"
        )
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)

    kq_false=random.choice(kq_false)
    st_p_b_false=f"{round_half_up(kq_false,2)}".replace(".",",")

    kq4_T=f"*  Xác suất chọn được người được hỗ trợ là ${{{st_p_b}}}$"
    kq4_F=f"Xác suất chọn được người được hỗ trợ là ${{{st_p_b_false}}}$" 
    
    HDG=(f" Xác suất chọn được người được hỗ trợ là:\n\n"
        f"$P(D)=P(D|M).P(M)+P(D|N).P(N)={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={st_p_b}$.")
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

    noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n\n"
        f"Xét các biến cố sau:\n\n"
        f"${{D}}$: Người được hỗ trợ\n\n"
        f"${{M}}$: Người có bảo hiểm y tế\n\n"
        f"${{N}}$: Người không có bảo hiểm y tế\n\n"
        f"${{D|M}}$: Người được hỗ trợ với điều kiện có bảo hiểm y tế\n\n"
        f"${{D|N}}$: Người được hỗ trợ với điều kiện không có bảo hiểm y tế\n\n"
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

#[D12_C6_B2_28]-TF-M3. Cho tỉ lệ khách hàng thân thiết, tỉ lệ khách mua hàng. Xét Đ-S: x.s giao, x.s toàn phần
def newy25_L12_C6_B2_28():
    a=random.randint(35,55)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    b=100-a
    p_a_ngang=1-p_a
    p_b=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(80,90)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(45,65)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    p_not_d_dk_nu=1-p_b_dk_a_ngang
    st_p_not_d_dk_nu=f"{round_half_up(p_not_d_dk_nu,2)}".replace(".",",")

    noi_dung = f" Trong một sàn thương mại điện tử, có ${a}\\%$ khách hàng là khách hàng thân thiết. Biết rằng ${b_dk_a}\\%$ khách hàng thân thiết và ${b_dk_a_ngang}\\% $ khách hàng không phải là khách hàng thân thiết thường xuyên quay lại mua hàng. Chọn ngẫu nhiên một khách hàng của sàn thương mại điện tử đó. Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm)."        
    debai_word= f"{noi_dung}\n"

    
    kq1_T=f"* Tỉ lệ khách hàng không thân thiết là ${b}\\%$" 
    kq1_F=f"Tỉ lệ khách hàng không thân thiết là ${b-random.randint(1,5)}\\%$"
    
    HDG=f"Theo đề bài ta có: $P(M)={a}\\%={st_p_a} \\Rightarrow P(N)={b}\\%={st_p_b}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_d_nam=f"{round_half_up(p_b_dk_a*p_a,2)}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b_dk_a*p_a, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_d_nam_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")


    kq2_T=f"* Xác suất chọn được khách hàng thân thiết và quay lại mua là  ${{{p_d_nam}}}$"
    kq2_F=f"Xác suất chọn được khách hàng thân thiết và quay lại mua là  ${{{p_d_nam_false}}}$"
    
    HDG=f"Xác suất chọn được khách hàng thân thiết và quay lại mua là : \n\n $P(DM)=P(D|M).P(M)={b_dk_a}.{p_a}={p_d_nam}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_not_d_nu=f"{round_half_up(p_not_d_dk_nu*p_b,2):.2f}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_not_d_dk_nu*p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_not_d_nu_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")

    kq3_T=f"* Xác suất chọn được khách hàng không thân thiết và không quay lại mua là ${{{p_not_d_nu}}}$" 
    kq3_F=f"Xác suất chọn được khách hàng không thân thiết và không quay lại mua là ${{{p_not_d_nu_false}}}$"
    
    HDG=(f"Xác suất chọn được khách hàng không thân thiết và không quay lại mua là:\n\n"
        f" $P(\\overline{{D}}N)=P(\\overline{{D}}|N).P(N)={st_p_not_d_dk_nu}.{st_p_b}={p_not_d_nu}$.\n\n"
        )
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)

    kq_false=random.choice(kq_false)
    st_p_b_false=f"{round_half_up(kq_false,2)}".replace(".",",")

    kq4_T=f"* Xác suất chọn được khách hàng quay lại mua là ${{{st_p_b}}}$"
    kq4_F=f"Xác suất chọn được khách hàng quay lại mua là ${{{st_p_b_false}}}$" 
    
    HDG=(f" Xác suất chọn được khách hàng quay lại mua là:\n\n"
        f"$P(D)=P(D|M).P(M)+P(D|N).P(N)={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={st_p_b}$.")
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

    noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n\n"
        f"Xét các biến cố sau:\n\n"
        f"${{D}}$: Khách hàng quay lại mua\n\n"
        f"${{M}}$: Khách hàng là thân thiết\n\n"
        f"${{N}}$: Khách hàng không phải là khách hàng thân thiết\n\n"
        f"${{D|M}}$: Khách hàng quay lại mua với điều kiện khách hàng thân thiết\n\n"
        f"${{D|N}}$: Khách hàng quay lại mua với điều kiện không phải là khách hàng thân thiết\n\n"
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

#[D12_C6_B2_29]-TF-M3. Cho tỉ lệ diện tích trồng cây, tỉ lệ đạt năng suất cao. Xét Đ-S: x.s giao, x.s toàn phần
def newy25_L12_C6_B2_29():
    a=random.randint(55,65)
    p_a=a/100
    st_p_a=f"{round_half_up(p_a,2)}".replace(".",",")

    b=100-a
    p_a_ngang=1-p_a
    p_b=1-p_a
    st_p_a_ngang=f"{round_half_up(p_a_ngang,2)}".replace(".",",")
    st_p_b=f"{round_half_up(p_a_ngang,2)}".replace(".",",")


    b_dk_a=random.randint(75,85)
    p_b_dk_a=b_dk_a/100
    st_p_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    b_dk_a_ngang=random.randint(65,75)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_p_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    p_not_d_dk_nu=1-p_b_dk_a_ngang
    st_p_not_d_dk_nu=f"{round_half_up(p_not_d_dk_nu,2)}".replace(".",",")
    cay=["lúa", "ngô", "củ mì", "đậu xanh", "đậu đen", "khoai lang"]
    lua,ngo=random.sample(cay,2)

    noi_dung = f"Trong một trang trại trồng 2 loại cây, có ${a}\\%$ diện tích trồng {lua}, phần còn lại trồng {ngo}. Biết rằng ${b_dk_a}\\%$ diện tích trồng {lua} và ${b_dk_a_ngang}\\% $ diện tích trồng {ngo} cho năng suất cao. Chọn ngẫu nhiên một mảnh đất. Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần trăm)."        
    debai_word= f"{noi_dung}\n"

    
    kq1_T=f"* Tỉ lệ diện tích trồng {ngo} là ${b}\\%$" 
    kq1_F=f"Tỉ lệ diện tích trồng {ngo} là ${b-random.randint(1,5)}\\%$"
    
    HDG=f"Theo đề bài ta có: $P(M)={a}\\%={st_p_a} \\Rightarrow P(N)={b}\\%={st_p_b}$."
    kq1=random.choice([kq1_T, kq1_F])
    loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq1==kq1_F:
        loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_d_nam=f"{round_half_up(p_b_dk_a*p_a,2)}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b_dk_a*p_a, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_d_nam_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")


    kq2_T=f"* Xác suất chọn được mảnh trồng {lua} và cho năng suất cao là ${{{p_d_nam}}}$"
    kq2_F=f"Xác suất chọn được mảnh trồng {lua} và cho năng suất cao là ${{{p_d_nam_false}}}$"
    
    HDG=f"Xác suất chọn được mảnh trồng {lua} và cho năng suất cao là: \n\n $P(DM)=P(D|M).P(M)={b_dk_a}.{p_a}={p_d_nam}$."
    kq2=random.choice([kq2_T, kq2_F])
    loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq2==kq2_F:
        loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_not_d_nu=f"{round_half_up(p_not_d_dk_nu*p_b,2):.2f}".replace(".",",")
    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_not_d_dk_nu*p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)
    p_not_d_nu_false=f"{round_half_up(random.choice(kq_false),2):.2f}".replace(".",",")

    kq3_T=f"* Xác suất chọn được mảnh trồng {ngo} và không cho năng suất cao là ${{{p_not_d_nu}}}$" 
    kq3_F=f"Xác suất chọn được mảnh trồng {ngo} và không cho năng suất cao là ${{{p_not_d_nu_false}}}$"
    
    HDG=(f"Xác suất chọn được mảnh trồng {ngo} và không cho năng suất cao là:\n\n"
        f" $P(\\overline{{D}}N)=P(\\overline{{D}}|N).P(N)={st_p_not_d_dk_nu}.{st_p_b}={p_not_d_nu}$.\n\n"
        )
    kq3=random.choice([kq3_T, kq3_F])
    loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
    if kq3==kq3_F:
        loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

    p_b=p_b_dk_a*p_a+p_b_dk_a_ngang*p_a_ngang
    st_p_b=f"{round_half_up(p_b,2)}".replace(".",",")

    kq_false = []
    while len(kq_false) < 3:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=p_b, num!=0]):  # Kiểm tra trùng lặp
            kq_false.append(num)

    kq_false=random.choice(kq_false)
    st_p_b_false=f"{round_half_up(kq_false,2)}".replace(".",",")

    kq4_T=f"* Xác suất chọn được mảnh đất cho năng suất cao là ${{{st_p_b}}}$"
    kq4_F=f"Xác suất chọn được mảnh đất cho năng suất cao là ${{{st_p_b_false}}}$" 
    
    HDG=(f" Xác suất chọn được mảnh đất cho năng suất cao là:\n\n"
        f"$P(D)=P(D|M).P(M)+P(D|N).P(N)={st_p_b_dk_a}.{st_p_a}+{st_p_b_dk_a_ngang}.{st_p_a_ngang}={st_p_b}$.")
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

    noi_dung_loigiai=(f"a-{list_TF[0]}, b-{list_TF[1]}, c-{list_TF[2]}, d-{list_TF[3]}.\n\n"
        f"Xét các biến cố sau:\n\n"
        f"${{D}}$: Mảnh đất cho năng suất cao\n\n"
        f"${{M}}$: Mảnh đất trồng {lua}\n\n"
        f"${{N}}$: Mảnh đất trồng {ngo}\n\n"
        f"${{D|M}}$: Mảnh đất cho năng suất cao với điều kiện trồng {lua}\n\n"
        f"${{D|N}}$: Mảnh đất cho năng suất cao với điều kiện trồng {ngo}\n\n"
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


#[D12_C6_B2_30]-M2. X.S Bayes: cho sơ đồ cây có P(A), P(B|A), P(B_|A_). Tính P(A|B)
def newy25_L12_C6_B2_30():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")    

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")

    #P(AB)
    p_ab=p_a*p_b_dk_a
    st_ab=f"{round_half_up(p_ab,2)}".replace(".",",")

    #P(B)    
    p_b=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #Cho P(A_), P(B_|A), P(B|A_)
    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" )
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)    
    
    
    

    kq=p_ab/p_b
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    noi_dung=(
    f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}|{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
    )
    noi_dung_loigiai=(
    f"Dựa vào sơ đồ cây ta có:"               
    f"$P({A}|{B})=\\dfrac{{P({A}).P({B}|{A}) }}{{P({B})}}=\\dfrac{{{st_a}.{st_b_dk_a} }}{{{st_a}.{st_b_dk_a}+{st_a_ngang}.{st_b_dk_a_ngang}}}={st_kq}$." )

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B2_31]-M2. X.S Bayes: Cho sơ đồ cây chứa P(A_), P(B_|A),P(B|A_). Tính P(A|B)
def newy25_L12_C6_B2_31():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")    

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")

    #P(AB)
    p_ab=p_a*p_b_dk_a
    st_ab=f"{round_half_up(p_ab,2)}".replace(".",",")

    #P(B)    
    p_b=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #Cho sơ đồ cây chứa P(A_), P(B_|A),P(B|A_). Tính P(A|B)
    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{$$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" )
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)    
    
    
    

    kq=p_ab/p_b
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    noi_dung=(
    f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}|{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
    )
    noi_dung_loigiai=(
    f"Dựa vào sơ đồ cây ta có:"               
    f"$P({A}|{B})=\\dfrac{{P({A}).P({B}|{A}) }}{{P({B})}}=\\dfrac{{{st_a}.{st_b_dk_a} }}{{{st_a}.{st_b_dk_a}+{st_a_ngang}.{st_b_dk_a_ngang}}}={st_kq}$." )

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B2_32]-M2. X.S Bayes: cho sơ đồ cây có P(A_), P(B|A), P(B_|A_). Tính P(A|B)
def newy25_L12_C6_B2_32():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")    

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")

    #P(AB)
    p_ab=p_a*p_b_dk_a
    st_ab=f"{round_half_up(p_ab,2)}".replace(".",",")

    #P(B)    
    p_b=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #Cho P(A_), P(B|A),P(B_|A_)
    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" )
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)    
    
    
    

    kq=p_ab/p_b
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    noi_dung=(
    f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}|{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
    )
    noi_dung_loigiai=(
    f"Dựa vào sơ đồ cây ta có:"               
    f"$P({A}|{B})=\\dfrac{{P({A}).P({B}|{A}) }}{{P({B})}}=\\dfrac{{{st_a}.{st_b_dk_a} }}{{{st_a}.{st_b_dk_a}+{st_a_ngang}.{st_b_dk_a_ngang}}}={st_kq}$." )

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B2_33]-M2. X.S Bayes: cho sơ đồ cây có P(A), P(B_|A), P(B|A_). Tính P(A|B)
def newy25_L12_C6_B2_33():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")    

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")

    #P(AB)
    p_ab=p_a*p_b_dk_a
    st_ab=f"{round_half_up(p_ab,2)}".replace(".",",")

    #P(B)    
    p_b=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")

    #Cho P(A_), P(B|A),P(B_|A_)
    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{$$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" )
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)  
    
    

    kq=p_ab/p_b
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    noi_dung=(
    f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}|{B}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
    )
    noi_dung_loigiai=(
    f"Dựa vào sơ đồ cây ta có:"               
    f"$P({A}|{B})=\\dfrac{{P({A}).P({B}|{A}) }}{{P({B})}}=\\dfrac{{{st_a}.{st_b_dk_a} }}{{{st_a}.{st_b_dk_a}+{st_a_ngang}.{st_b_dk_a_ngang}}}={st_kq}$." )

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#[D12_C6_B2_34]-M2. x.s Bayes: Cho sơ đồ cây tùy ý. Tính P(A|B)
def newy25_L12_C6_B2_34():
    chon=random.randint(1,4)
    if chon==1:
        debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=newy25_L12_C6_B2_30()
    
    if chon==2:
        debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=newy25_L12_C6_B2_31()

    if chon==3:
        debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=newy25_L12_C6_B2_32()

    if chon==4:
        debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=newy25_L12_C6_B2_33()

    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D12_C6_B2_35]-M2. X.S Bayes: cho sơ đồ cây có P(A), P(B|A), P(B_|A_). Tính P(A|B_)
def newy25_L12_C6_B2_35():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")    

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")

    #P(AB)
    p_ab=p_a*p_b_dk_a
    st_ab=f"{round_half_up(p_ab,2)}".replace(".",",")

    #P(AB_)
    p_ab_ngang=p_a*p_b_ngang_dk_a
    st_ab_ngang=f"{round_half_up(p_ab_ngang,2)}".replace(".",",")

    #P(B)    
    p_b=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    p_b_ngang=1-p_b
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")
    st_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")

    #Cho P(A_), P(B_|A), P(B|A_)
    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" )
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)    


    kq=p_ab_ngang/p_b_ngang
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    noi_dung=(
    f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}|\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
    )
    noi_dung_loigiai=(
    f"Dựa vào sơ đồ cây ta có:"               
    f"$P({A}|\\overline{{{B}}})=\\dfrac{{P({A}).P(\\overline{{{B}}}|{A}) }}{{P(\\overline{{{B}}})}}=\\dfrac{{{st_a}.{st_b_ngang_dk_a} }}{{{st_a}.{st_b_ngang_dk_a}+{st_a_ngang}.{st_b_ngang_dk_a_ngang}}}={st_kq}$." )

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D12_C6_B2_36]-M2. X.S Bayes: cho sơ đồ cây có P(A), P(B_|A), P(B|A_). Tính P(A|B_)
def newy25_L12_C6_B2_36():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")    

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")

    #P(AB)
    p_ab=p_a*p_b_dk_a
    st_ab=f"{round_half_up(p_ab,2)}".replace(".",",")

    #P(AB_)
    p_ab_ngang=p_a*p_b_ngang_dk_a
    st_ab_ngang=f"{round_half_up(p_ab_ngang,2)}".replace(".",",")

    #P(B)    
    p_b=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    p_b_ngang=1-p_b
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")
    st_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")

    #Cho P(A_), P(B_|A), P(B|A_)
    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{$$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{$$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" )
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)    


    kq=p_ab_ngang/p_b_ngang
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    noi_dung=(
    f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}|\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
    )
    noi_dung_loigiai=(
    f"Dựa vào sơ đồ cây ta có:"               
    f"$P({A}|\\overline{{{B}}})=\\dfrac{{P({A}).P(\\overline{{{B}}}|{A}) }}{{P(\\overline{{{B}}})}}=\\dfrac{{{st_a}.{st_b_ngang_dk_a} }}{{{st_a}.{st_b_ngang_dk_a}+{st_a_ngang}.{st_b_ngang_dk_a_ngang}}}={st_kq}$." )

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D12_C6_B2_37]-M2. X.S Bayes: cho sơ đồ cây có P(A_), P(B_|A), P(B|A_). Tính P(A|B_)
def newy25_L12_C6_B2_37():
    bien_co=["A","B","C","D","E","F", "X", "Y"]
    random.shuffle(bien_co)
    A,B=bien_co[0:2]

    #P(A)
    a=random.randint(55,70)
    p_a=a/100
    p_a_ngang=1-p_a
    st_a=f"{round_half_up(p_a,2)}".replace(".",",")
    st_a_ngang=f"{round_half_up(1-p_a,2)}".replace(".",",")    

    #P(B|A)
    b_dk_a=random.randint(5,45)
    p_b_dk_a=b_dk_a/100
    st_b_dk_a=f"{round_half_up(p_b_dk_a,2)}".replace(".",",")

    #P(B_ngang|A)
    p_b_ngang_dk_a=1-p_b_dk_a
    st_b_ngang_dk_a=f"{round_half_up(p_b_ngang_dk_a,2)}".replace(".",",")

    #P(B|A_ngang)
    b_dk_a_ngang=random.randint(5,45)
    p_b_dk_a_ngang=b_dk_a_ngang/100
    st_b_dk_a_ngang=f"{round_half_up(p_b_dk_a_ngang,2)}".replace(".",",")

    #P(B_ngang|A_ngang)
    p_b_ngang_dk_a_ngang=1-b_dk_a_ngang/100
    st_b_ngang_dk_a_ngang=f"{round_half_up(p_b_ngang_dk_a_ngang,2)}".replace(".",",")

    #P(AB)
    p_ab=p_a*p_b_dk_a
    st_ab=f"{round_half_up(p_ab,2)}".replace(".",",")

    #P(AB_)
    p_ab_ngang=p_a*p_b_ngang_dk_a
    st_ab_ngang=f"{round_half_up(p_ab_ngang,2)}".replace(".",",")

    #P(B)    
    p_b=p_a*p_b_dk_a+p_a_ngang*p_b_dk_a_ngang
    p_b_ngang=1-p_b
    st_b=f"{round_half_up(p_b,2)}".replace(".",",")
    st_b_ngang=f"{round_half_up(p_b_ngang,2)}".replace(".",",")

    #Cho P(A_), P(B_|A), P(B|A_)
    code_hinh=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{$$}};\n\
            %X.S B|A_ngang \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{$$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
        \\end{{tikzpicture}}" )
    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)    


    kq=p_ab_ngang/p_b_ngang
    st_kq=f"{round_half_up(kq,2):.2f}".replace(".",",")
    noi_dung=(
    f"Cho các biến cố ${{{A},{B}}}$ có sơ đồ cây như hình vẽ. Tính xác suất $P\\left({A}|\\overline{{{B}}}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
    )
    noi_dung_loigiai=(
    f"Dựa vào sơ đồ cây ta có:"               
    f"$P({A}|\\overline{{{B}}})=\\dfrac{{P({A}).P(\\overline{{{B}}}|{A}) }}{{P(\\overline{{{B}}})}}=\\dfrac{{{st_a}.{st_b_ngang_dk_a} }}{{{st_a}.{st_b_ngang_dk_a}+{st_a_ngang}.{st_b_ngang_dk_a_ngang}}}={st_kq}$." )

    
    kq_false = []
    while len(kq_false) < 10:
        num = round(random.random(), 2)
        if all([num not in kq_false, num!=kq, num!=0]):
            kq_false.append(num)
    
    random.shuffle(kq_false)
    kq2,kq3,kq4=kq_false[0:3]

    kq=f"{round_half_up(kq,2):.2f}".replace(".",",")


    p_b_a=f"{round_half_up(p_a*p_b_dk_a,2):.2f}".replace(".",",")
    p_b_ngang_a=f"{round_half_up(p_a*p_b_ngang_dk_a,2):.2f}".replace(".",",")
    p_b_a_ngang=f"{round_half_up(p_a_ngang*p_b_dk_a_ngang,2):.2f}".replace(".",",")
    p_b_ngang_a_ngang=f"{round_half_up(p_a_ngang*p_b_ngang_dk_a_ngang,2):.2f}".replace(".",",")
    code_hinh_giai=(f" \\begin{{tikzpicture}}[>=stealth]\n\
            %Mui ten A, A_ngang\n\
            %X.S A\n\
            \\draw [->] (2.2,-0.5)--(3.8,1.6) node[pos=0.5,sloped,above]{{${st_a}$}};\n\
            %X.S A_ngang\n\
            \\draw [->] (2.2,-0.5)--(3.8,-2.6) node[pos=0.5,sloped,below]{{${st_a_ngang}$}}; \n\
            %Khung A\n\
            \\draw (3.8,1.1) rectangle (5.1,2.1);\n\
            \\draw (8.9/2,1.6) node{{${A}$}} ;\n\
            %Khung A_ngang\n\
            \\draw (3.8,-2.1) rectangle (5.1,-3.1);\n\
            \\draw (8.9/2,-2.6) node{{$\\overline{{{A}}}$}} ;\n\
            %Mui ten B|A, B_ngang|A\n\
            %X.S B|A\n\
            \\draw [->] (5.1,1.6)--(6.5,2.6) node[pos=0.5,sloped,above]{{${st_b_dk_a}$}};\n\
            %X.S B_ngang|A \n\
            \\draw [->] (5.1,1.6)--(6.5,0.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a}$}}; \n\
            %Mui ten B|A_ngang, B_ngang|A_ngang\n\
            \\draw [->] (5.1,-2.6)--(6.5,-1.6) node[pos=0.5,sloped,above]{{${st_b_dk_a_ngang}$}};\n\
            \\draw [->] (5.1,-2.6)--(6.5,-3.6) node[pos=0.5,sloped,below]{{${st_b_ngang_dk_a_ngang}$}};\n\
            %Khung 3.1\n\
            \\draw (6.5,2.2) rectangle (7.7,3.2);\n\
            \\draw (7.1,5.4/2) node{{${B}$}} ;\n\
            %Khung B|A, B|A_ngang\n\
            \\draw (6.5,1.2) rectangle (7.7,0.2);\n\
            \\draw (7.1,1.4/2) node{{$\\overline{{{B}}}$}} ;\n\
            %Khung B_ngang|A_ngang, B_ngang|A_ngang\n\
            \\draw (6.5,-1.1) rectangle (7.7,-2.1);\n\
            \\draw (7.1,-3.2/2) node{{${B}$}} ;           \n\
            \\draw (6.5,-2.9) rectangle (7.7,-3.9);\n\
            \\draw (7.1,-3.4) node{{$\\overline{{{B}}}$}} ;\n\
            %Kết quả\n\
            \\draw (9.5,3.7) node{{\\textbf{{Kết quả}}}};   \n\
            \\draw (9.5,2.7) node{{${A}{B}$}};\n\
            \\draw (9.5,0.7) node{{${A}\\overline{{{B}}}$}};\n\
            \\draw (9.5,-1.6) node{{$\\overline{{{A}}}{B}$}};\n\
            \\draw (9.5,-3.4) node{{$\\overline{{{A}}}\\cdot\\overline{{{B}}}$}};\n\
            %Xác suất\n\
            \\draw (12.5,3.7) node{{\\textbf{{Xác suất}}}}; \n\
            \\draw (12.5,2.7) node{{${p_b_a}$}};\n\
            \\draw (12.5,0.7) node{{${p_b_ngang_a}$}};\n\
            \\draw (12.5,-1.6) node{{${p_b_a_ngang}$}};\n\
            \\draw (12.5,-3.4) node{{${p_b_ngang_a_ngang}$}};\n\
        \\end{{tikzpicture}}" 
)
    

    
    kq2=f"{round_half_up(kq2,2):.2f}".replace(".",",")
    kq3=f"{round_half_up(kq3,2):.2f}".replace(".",",")
    kq4=f"{round_half_up(kq4,2):.2f}".replace(".",",")

    pa_A= f"*${{{kq}}}$"
    pa_B= f"${{{kq2}}}$"
    pa_C= f"${{{kq3}}}$"
    pa_D= f"${{{kq4}}}$"
    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n{file_name}\n"

    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
    

    code = my_module.moi_truong_anh_latex(code_hinh_giai)
    file_name=my_module.pdftoimage_timename(code)

    loigiai_word=f"Lời giải:\n Chọn {dap_an} \n{file_name}\n {noi_dung_loigiai} \n"
    loigiai_traloingan=f"Lời giải:\n {noi_dung_loigiai} \n"

    #Tạo đề latex
    for i in range(4):
        list_PA[i]=list_PA[i].replace("*","\\True ")    

    debai_latex= (f"\\begin{{ex}}\n {noi_dung} \n"
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\choice\n"
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"
        f"\\loigiai{{ \\begin{{center}}\n{code_hinh_giai}\n\\end{{center}}\n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")

    latex_tuluan=(f"\\begin{{ex}}\n {noi_dung} \n"
        f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
    f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
        f"\\end{{ex}}\n")
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an
    