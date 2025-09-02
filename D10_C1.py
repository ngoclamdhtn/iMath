import random
import my_module
from sympy import *
import sympy as sp
from itertools import chain, combinations

#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(10000000000000))
    return m

def random_name():
	ten=random.choice(["Lan", "Đào", "Minh", "Phương", "Thảo", "Linh", 'Hồng', 'Ngọc', 'Hương', 'Thơm', 'Thúy', 'Mai', 'Nhi', 'Hiền','My', 'Na' ])
	return ten
def random_camxuc():
	cam_xuc=random.choice(['cao quá', 'xinh quá', 'chăm học quá', 'rất chăm học', 'rất ngoan', 'năng nổ quá', 'múa đẹp quá', 'hát hay quá' ])
	return cam_xuc

def random_monhoc():
	mon_hoc=random.choice(["môn Toán", "môn Văn", "môn Tiếng Anh", "môn Vật Lí", "môn Hóa Học", "môn Sinh học", "môn Địa Lí", "môn Lịch Sử", "môn GDKT\\&PL", "môn Tin học" ])
	return mon_hoc
def random_tinhVN():
	ten_tinh=random.choice(["Đắk Lắk", "Gia Lai", "Kon Tum", "Lâm Đồng", "Nghệ An", "Hà Tĩnh", "Khánh Hòa", "Bến Tre", "Cà Mau" ])
def tim_boi_của_n_nho_hon_m(n, m):
    multiples = []
    for i in range(0, m):
        if i % n == 0:
            multiples.append(i)
    return multiples

# Tạo ngẫu nhiên tập hợp 
def tao_taphop(so_phantu,so_batdau,so_ketthuc):
    my_set = set(random.sample(range(so_batdau, so_ketthuc), so_phantu))
    return my_set

def thay_kihieu_rong(st):    
    return st.replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{None\\}}",f"\\emptyset").replace(f"\\{{\\}}",f"\\emptyset")

def prime_factor(n):
    factors = sympy.factorint(n)
    latex_result = ' \\cdot '.join([f"{p}^{{{e}}}" if e > 1 else f"{p}" for p, e in factors.items()])
    return latex_result
import sympy

def non_prime_list_in_range(a, b):
    non_primes = []
    for num in range(a, b + 1):
        if not sympy.isprime(num):
            non_primes.append(num)
    return non_primes

# Hàm tạo tất cả các tập hợp con của một tập hợp cho trước
def all_subsets(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

# Hàm tìm tất cả các tập hợp X sao cho A là tập hợp con của X và X là tập hợp con của B
def find_subsets(A, B):
	subsets_of_B = list(all_subsets(B))
	valid_subsets = []

	for subset in subsets_of_B:
		if set(A).issubset(subset):  # Kiểm tra nếu A là tập hợp con của X
			valid_subsets.append(subset)
	st=""
	for x in valid_subsets:
		st+=f"$\\{{{x}\\}}$\n\n"

	return st

def find_subsets_and_count(A, B):
    subsets_of_B = list(all_subsets(B))
    valid_subsets = []

    for subset in subsets_of_B:
        if set(A).issubset(subset):  # Kiểm tra nếu A là tập hợp con của X
            valid_subsets.append(set(subset))

    count = len(valid_subsets)  # Đếm số tập hợp con hợp lệ
    return count


#BÀI 1 - MỆNH ĐỀ
#[D10_C1_B1_01]-TF-M2. Xét tính Đ-S của mệnh đề, mệnh đề phủ định, mệnh đề chứa biến.
def mjulk_L10_C1_B1_01():

	noi_dung = f"Xét tính đúng-sai của các mệnh đề và mệnh đề chứa biến sau. "		
	debai_word= f"{noi_dung}\n"

	a=random.randint(-100,200)
	t=random.randint(5,50)
	b=a+t
	
	kq1_T=f"*${random.choice([f"{a}<{b}", f"{a}\\le {b}", f"{b}={a}+{t}", f"{b}-{a}>0", f"{b}-{a}\\ge 0", f"{a}-{b}<0", f"{a}-{b}\\le 0"])}$".replace("--","+")
	kq1_F=f"${random.choice([f"{a}>{b}", f"{a}\\ge {b}",f"{a}={b}", f"{a}={b}+{t}",f"{b}-{a}<0", f"{b}-{a}\\le 0", f"{a}-{b}>0", f"{a}-{b}\\ge 0"])}$".replace("--","+")
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f""
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	
	if chon==1:
		a=random.choice(list(primerange(1, 100)))
		kq2_T=f"*{random.choice([f"${{{a}}}$ là số nguyên tố", f"${{{a}}}$ là số tự nhiên", f"${{{a}}}$ là số nguyên", f"${{{a}}}$ là số thực"])}"
		kq2_F=f"{random.choice([f"${{{a}}}$ không phải là số nguyên tố", f"${{{a}}}$ không phải là số tự nhiên", f"${{{a}}}$ không phải là số nguyên", f"${{{a}}}$ không phải là số thực"])}"
		kq2=random.choice([kq2_T, kq2_F])
		if kq2==f"${{{a}}}$ không phải là số nguyên tố":
			HDG=f"${{{a}}}$ là một số nguyên tố."
		else:
			HDG=""
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:		
		b=random.choice(non_prime_list_in_range(20,1000))
		kq2_T=f"*${{{b}}}$ không phải là số nguyên tố"
		kq2_F=f"${{{b}}}$ là số nguyên tố"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"Vì ${b}={prime_factor(b)}$ nên ${{b}}$ không phải là số nguyên tố."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	a=random.randint(-100,200)
	t=random.randint(5,50)
	b=a+t

	chon=random.randint(1,4)
	if chon==1:
		kq3_T=f'*Mệnh đề phủ định của "${a}<{b}$" là "${a} \\ge {b}$"'
		kq3_F=f'Mệnh đề phủ định của "${a}<{b}$" là {random.choice([f'"${a}>{b}$"',f'"${a}={b}$"', f'"${a}\\ne {b}$"'])}'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f'Mệnh đề phủ định của "${a}<{b}$" là "${a} \\ge {b}$"'
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	
	if chon==2:
		kq3_T=f'*Mệnh đề phủ định của "${a}>{b}$" là "${a} \\le {b}$"'
		kq3_F=f'Mệnh đề phủ định của "${a}>{b}$" là {random.choice([f'"${a}<{b}$"',f'"${a}={b}$"', f'"${a}\\ne {b}$"'])}'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f'Mệnh đề phủ định của "${a}>{b}$" là "${a} \\le {b}$"'
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		kq3_T=f'*Mệnh đề phủ định của "${a}\\ge {b}$" là "${a} < {b}$"'
		kq3_F=f'Mệnh đề phủ định của "${a}\\ge {b}$" là {random.choice([f'"${a}\\le {b}$"',f'"${a}={b}$"', f'"${a}\\ne {b}$"'])}'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f'Mệnh đề phủ định của "${a}\\ge {b}$" là "${a} < {b}$"'
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==4:
		kq3_T=f'*Mệnh đề phủ định của "${a}\\le {b}$" là "${a} > {b}$"'
		kq3_F=f'Mệnh đề phủ định của "${a}\\le {b}$" là {random.choice([f'"${a}\\ge {b}$"',f'"${a}={b}$"', f'"${a}\\ne {b}$"'])}'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f'Mệnh đề phủ định của "${a}\\le {b}$" là "${a} > {b}$"'
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x=sp.symbols("x")
	a = random.choice([i for i in range(1, 5) if i!=0])
	b = random.choice([i for i in range(-4, 4) if i!=0])

	chon=random.randint(1,3)
	
	if chon==1:
		t=random.randint(1,4)
		f=(a*x+b)**2 +t
		g=random.randint(1,5)*x+random.randint(-5,5)
		kq4_T=f"*$\\forall x \\in \\mathbb{{R}}:{latex(expand(f+g))} {random.choice([">", "\\ge"])} {latex(expand(g))}$"
		kq4_F=f"$\\forall x \\in \\mathbb{{R}}:{latex(expand(f+g))} {random.choice(["<", "\\le "])} {latex(expand(g))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$\\forall x \\in \\mathbb{{R}}:{latex(expand(f+g))}-({latex(expand(g))})={latex(expand(f))} ={latex(f)} {random.choice([">0", "\\ge 0"])}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==2:
		t=random.randint(1,4)
		f=-(a*x+b)**2 -t
		g=random.randint(1,5)*x+random.randint(-5,5)
		kq4_T=f"*$\\forall x \\in \\mathbb{{R}}:{latex(expand(f+g))} {random.choice(["<", "\\le"])} {latex(expand(g))}$"
		kq4_F=f"$\\forall x \\in \\mathbb{{R}}:{latex(expand(f+g))} {random.choice([">", "\\ge "])} {latex(expand(g))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$\\forall x \\in \\mathbb{{R}}:{latex(expand(f+g))}-({latex(expand(g))})={latex(expand(f))} ={latex(f)} {random.choice(["<0", "\\le 0"])}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		t=random.randint(1,4)
		f=(a*x+b)**2 +t
		g=random.randint(1,5)*x+random.randint(-5,5)
		kq4_T=f"*$\\exists x \\in \\mathbb{{R}}:{latex(expand(f+g))} {random.choice([">", "\\ge"])} {latex(expand(g))}$"
		kq4_F=f"$\\exists x \\in \\mathbb{{R}}:{latex(expand(f+g))} {random.choice(["<", "\\le "])} {latex(expand(g))}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$\\forall x \\in \\mathbb{{R}}:{latex(expand(f+g))}-({latex(expand(g))})={latex(expand(f))} ={latex(f)} {random.choice([">0", "\\ge 0"])}$."
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

#[D10_C1_B1_02]-TF-M2. Xét Đ-S về số chính phương, số hữu tỉ, số chẵn, lẻ, số chia hết.
def mjulk_L10_C1_B1_02():
	noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	chon=random.randint(1,2)	
	if chon==1:
		i=random.randint(1,100)
		a=i**2		
		kq1_T=f'*Mệnh đề "${{{a}}}$ là số chính phương" là mệnh đề đúng'
		kq1_F=f'Mệnh đề "${{{a}}}$ là số chính phương" là mệnh đề sai'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Vì ${a}={i}^2$ nên ${{{a}}}$ là số chính phương.'
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		i=random.randint(2,50)
		a=i**3		
		kq1_T=f'*Mệnh đề "${{{a}}}$ là số chính phương" là mệnh đề sai'
		kq1_F=f'Mệnh đề "${{{a}}}$ là số chính phương" là mệnh đề đúng'
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f'Vì ${a}={i}^3$ nên ${{{a}}}$ không là số chính phương.'
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	

	b=random.choice([sqrt(i) for i in range(1,100)])
	
	if b.is_integer:	
		kq2_T=f'*"${{{latex(b)}}}$ là số hữu tỉ" là mệnh đề đúng'
		kq2_F=f'"${{{latex(b)}}}$ là số hữu tỉ" là mệnh đề sai'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f'${{{latex(b)}}}$ là số hữu tỉ" là mệnh đề đúng'
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	else:
		kq2_T=f'*"${{{latex(b)}}}$ là số vô tỉ" là mệnh đề đúng'
		kq2_F=f'"${{{latex(b)}}}$ là số vô tỉ" là mệnh đề sai'
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f'${{{latex(b)}}}$ là số vô tỉ" là mệnh đề đúng'
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	c=random.randint(1,300)
	if c%2==0:
		kq3_T=f'*Mệnh đề "${{{c}}}$ là số chẵn" là mệnh đề đúng'
		kq3_F=f'Mệnh đề "${{{c}}}$ là số chẵn" là mệnh đề sai'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f'Mệnh đề "${{{c}}}$ là số chẵn" là mệnh đề đúng'
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	else:
		kq3_T=f'*Mệnh đề "${{{c}}}$ là số lẻ" là mệnh đề đúng'
		kq3_F=f'Mệnh đề "${{{c}}}$ là số lẻ" là mệnh đề sai'
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f'Mệnh đề "${{{c}}}$ là số lẻ" là mệnh đề đúng'
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)
	if chon==1:
		n=random.randint(2,5)
		t=random.choice([2,3,4,5,6,7,8])
		d=t**n
		kq4_T=f'*Mệnh đề "${{{d}}}$ chia hết cho ${{{t}}}$" là mệnh đề đúng'
		kq4_F=f'Mệnh đề "${{{d}}}$ chia hết cho ${{{t}}}$" là mệnh đề sai' 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Vì ${d}={t}^{n}$ nên ${{{d}}}$ chia hết cho ${{{t}}}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		n=random.randint(2,5)
		t=random.choice([2,3,4,5,6,7,8])
		d=t**n+1
		kq4_T=f'*Mệnh đề "${{{d}}}$ chia hết cho ${{{t}}}$" là mệnh đề sai'
		kq4_F=f'Mệnh đề "${{{d}}}$ chia hết cho ${{{t}}}$" là mệnh đề đúng' 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Vì ${d}={t}^{n}+1$ nên ${{{d}}}$ không chia hết cho ${{{t}}}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"	

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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

#[D10_C1_B1_03]-TF-M2. Cho P(n)=an^2+bn+c. Xét Đ-S: P(x_0) chẵn (lẻ),P(x_1) chia hết cho, P(ta)-P(a), ...
def mjulk_L10_C1_B1_03():
	n=sp.symbols("n")
	a = random.choice([i for i in range(-4, 4) if i!=0])
	b = random.choice([i for i in range(-5, 5) if i!=0])	
	n_0=random.choice([i for i in range(-3, 3) if i!=0])
	#f=a*n**2+b*n+c
	f=a*(n-n_0)**2+b
	a1=a

	noi_dung = f"Cho $P(n)={latex(expand(f))}$ với ${{n}}$ là số nguyên. Xét tính đúng-sai của các khẳng định sau."		
	debai_word= f"{noi_dung}\n"
	x_0=random.randint(-6,6)
	P_x0 = f.subs(n,x_0)
	if P_x0 >0:	
		kq1_T=f"*$P({x_0})$ là số dương" 
		kq1_F=f"$P({x_0})$ không phải là số dương"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$P({x_0})={P_x0}$ là số chẵn."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	else:
		kq1_T=f"*$P({x_0})$ không phải là số dương" 
		kq1_F=f"$P({x_0})$ là số dương"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$P({x_0})={P_x0}$ là số lẻ."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	x_1=random.randint(-6,6)
	if x_1==x_0:x_1+=1
	P_x1 = f.subs(n,x_1)
	if P_x1>0:
		uoc= random.choice([i for i in divisors(P_x1)])
		kq2_T=f"*$P({x_1})$ chia hết cho ${{{uoc}}}$"
		kq2_F=f"$P({x_1})$ không chia hết cho ${{{uoc}}}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$P({x_1})={P_x1}$ chia hết cho ${{{uoc}}}$"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	else:
		kq2_T=f"*$P({x_1}) \\le 0$"
		kq2_F=f"$P({x_1})>{random.randint(1,10)}$"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"$P({x_1})={P_x1}\\le 0$"
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	t=random.randint(2,4)
	a=sp.symbols("a")
	P_ta=f.subs(n,t*a)
	P_a=f.subs(n,a)

	kq3_T=f"*$P({t}a)-P({a})={latex(expand(P_ta-P_a))}$" 
	kq3_F=f"$P({t}a)-P({a})={latex(expand(P_ta-P_a+random.randint(1,4)))}$" 
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$P({t}a)-P({a})={latex(expand(P_ta))}-({latex(expand(P_a))})={latex(expand(P_ta-P_a))}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	c = random.choice([i for i in range(-5, 6) if i!=0])
	if b+c==0: c=c+1
	uoc_duong=divisors(abs(b+c))
	uoc_am=[-i for i in uoc_duong]
	list_uoc=uoc_am + uoc_duong
	list_uoc=[str(n_0+i) for i in list_uoc]
	str_list_uoc=",".join(list_uoc)
	soluong=len(list_uoc)

	kq4_T=f"*Số các số nguyên n để $\\dfrac{{P(n)+{c}}}{{{latex(n-n_0)}}}$ là số nguyên là ${{{soluong}}}$".replace("+-","-")
	kq4_F=f"Số các số nguyên n để $\\dfrac{{P(n)+{c}}}{{{latex(n-n_0)}}}$ là số nguyên là ${{{soluong+random.randint(1,3)}}}$".replace("+-","-") 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"$A=\\dfrac{{P(n)+{c}}}{{{latex(n-n_0)}}}=\\dfrac{{{latex(expand(f))}+{c}}}{{{latex(n-n_0)}}}"\
	f"=\\dfrac{{{latex(f+c)} }}{{{latex(n-n_0)}}}={a1}+\\dfrac{{{b+c}}}{{{latex(n-n_0)}}}$.\n\n"\
	f"${{A}}$ là số nguyên khi $\\dfrac{{{c}}}{{{latex(n-n_0)}}}$ là số nguyên.\n\n"\
	f"Khi đó: $n\\in \\{{{str_list_uoc}\\}}$.\n\n"\
	f"Số các số nguyên n để $\\dfrac{{P(n)+{c}}}{{{latex(n-n_0)}}}$ là số nguyên là ${{{soluong}}}$.".replace("+-","-")

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

#[D10_C1_B1_04]-M2. Tìm mệnh đề đúng (cảm thán, số là số gì, số chia hết cho, nghiệm của phương trình).
def mjulk_L10_C1_B1_04():
	noi_dung=f"Trong các phát biểu sau phát biểu nào là mệnh đề đúng?"
	
	a=random.choice(list(primerange(1, 100)))
	kq=f"{random.choice([f"${{{a}}}$ là số nguyên tố", f"${{{a}}}$ là số tự nhiên", f"${{{a}}}$ là số nguyên", f"${{{a}}}$ là số thực"])}"
	
	chon=random.randint(1,2)
	if chon==1:
		kq2=f"Bạn {random_name()} {random_camxuc()}!"
		
	if chon==2:
		kq2=f"Bạn {random_name()} có thích học {random_monhoc()} không?"
	b=random.choice([2,3,4,5,6,7])
	n=random.randint(2,6)
	p=random.randint(2,20)
	if b**n%p==0:
		kq3=f"${{{b**n}}}$ không chia hết cho ${{{p}}}$"
	else:
		kq3=f"${{{b**n}}}$ chia hết cho ${{{p}}}$"


	x=sp.symbols("x")
	x_1=random.randint(-4,4)
	x_2=x_1+random.randint(1,4)
	kq4=f"Phương trình ${latex(expand(random.randint(1,3)*(x-x_1)*(x-x_2)))}=0$ {random.choice(["vô nghiệm", "có đúng 1 nghiệm"])}"
	
	noi_dung_loigiai=f"{kq} là khẳng định đúng."

	pa_A= f"*{kq}"
	pa_C= f"{kq3}"
	pa_B= f"{kq2}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	
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

#[D10_C1_B1_05]-M2. Tìm mệnh đề sai (cảm thán, số là số gì, số chia hết cho, nghiệm của phương trình).
def mjulk_L10_C1_B1_05():
	noi_dung=f"Trong các phát biểu sau phát biểu nào là mệnh đề sai?"	
	
	chon=random.randint(1,3)
	tinh_mien_nam=random.choice(["An Giang", "Bà Rịa - Vũng Tàu", "Bạc Liêu", "Bến Tre", "Bình Dương", "Bình Phước", "Cà Mau", "Cần Thơ", "Đồng Nai", "Đồng Tháp", "Hậu Giang", "Thành phố Hồ Chí Minh", "Kiên Giang", "Lâm Đồng", "Long An", "Sóc Trăng", "Tây Ninh", "Tiền Giang", "Trà Vinh", "Vĩnh Long"])
	
	tinh_mien_bac=random.choice(["Bắc Giang", "Bắc Kạn", "Cao Bằng", "Điện Biên", "Hà Giang", "Hà Nam", "Hà Nội", "Hải Dương", "Hải Phòng", "Hòa Bình", "Hưng Yên", "Lai Châu", "Lạng Sơn", "Lào Cai", "Nam Định", "Ninh Bình", "Phú Thọ", "Quảng Ninh", "Sơn La", "Thái Bình", "Thái Nguyên", "Tuyên Quang", "Vĩnh Phúc", "Yên Bái"])
	if chon==1:
		kq=f"Tỉnh {tinh_mien_bac} thuộc miền Nam nước Việt Nam"	

	if chon==2:
		kq=f"Tỉnh {tinh_mien_nam} thuộc miền Bắc nước Việt Nam"

	if chon==3:
		a=random.choice(list(primerange(1, 100)))
		kq=f"{random.choice([f"${{{a}}}$ không phải là số nguyên tố",  f"${{{a}}}$ không phải là số nguyên"])}"

	a=random.choice(list(primerange(1, 100)))
	kq2=f"{random.choice([ f"${{{a}}}$ là số tự nhiên", f"${{{a}}}$ là số hữu tỉ"])}"

	b=random.choice([2,3,4,5,6,7])
	n=random.randint(2,6)
	kq3=f"${{{b**n}}}$ chia hết cho ${{{b}}}$"

	x=sp.symbols("x")
	x_1=random.randint(-4,4)
	x_2=x_1+random.randint(1,4)
	kq4=f"Phương trình ${latex(expand(random.randint(1,3)*(x-x_1)*(x-x_2)))}=0$ {random.choice(["có 2 nghiệm phân biệt"])}"
	
	noi_dung_loigiai=f"{kq} là khẳng định sai."

	pa_A= f"*{kq}"
	pa_C= f"{kq3}"
	pa_B= f"{kq2}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	
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

#[D10_C1_B1_06]-M2. Mệnh đề phủ định có chứa biến.
def mjulk_L10_C1_B1_06():
	taphop=random.choice(["R","N", "Q", "Z" ])
	a = random.choice([i for i in range(-10, 10) if i!=0])
	b= random.choice([i for i in range(-10, 10) if i!=0])
	c=random.randint(-10,10)
	d = random.choice([i for i in range(-10, 10) if i!=0])
	e= random.choice([i for i in range(-10, 10) if i!=0])
	if d==a: d=d+1
	if e==b: e=e+2
	x=sp.symbols("x")

	chon=random.randint(1,4)
	if chon==1:
		f=a*x**2+b*x+c		
	if chon==2:
		f=a*x+b
	if chon==3:
		f=sqrt(a*x+b)
	if chon==4:
		f=sqrt(a*x)+b
	g=random.choice([random.randint(-5,5), 0, latex(d*x+e), latex(e-d*x)])
	
	moi=random.choice(["\\forall","\\exists"])
	chon=random.randint(1,6)
	if moi=="\\forall":
		tontai="\\exists"
	else:
		tontai="\\forall"

	if chon==1:
		noi_dung=f'Mệnh đề phủ định của mệnh đề "${moi} x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$" là'
		noi_dung_loigiai=f'Mệnh đề phủ định là: ${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$.'

		kq=f"${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$"
		kq2=f"${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$"
		kq3=f"${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$"
		kq4=f"${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ge {g}$"
	
	if chon==2:
		noi_dung=f'Mệnh đề phủ định của mệnh đề "P:${moi} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ge {g}$" là'
		noi_dung_loigiai=f'Mệnh đề phủ định là: ${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$.'

		kq=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$"
		kq2=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$"
		kq3=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$"
		kq4=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ge {g}$"

	if chon==3:
		noi_dung=f'Mệnh đề phủ định của mệnh đề "P:${moi} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$" là'
		noi_dung_loigiai=f'Mệnh đề phủ định là: ${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$.'

		kq=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$"
		kq2=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$"
		kq3=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$"
		kq4=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ge {g}$"

	if chon==4:
		noi_dung=f'Mệnh đề phủ định của mệnh đề "P:${moi} x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$" là'
		noi_dung_loigiai=f'Mệnh đề phủ định là: ${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ge {g}$.'

		kq=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ge {g}$"
		kq2=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$"
		kq3=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$"
		kq4=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$"

	if chon==5:
		noi_dung=f'Mệnh đề phủ định của mệnh đề "P:${moi} x \\in \\mathbb{{{taphop}}}: {latex(f)} = {g}$" là'
		noi_dung_loigiai=f'Mệnh đề phủ định là: ${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ne {g}$.'

		kq=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ne {g}$"
		kq2=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$"
		kq3=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$"
		kq4=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$"

	if chon==6:
		noi_dung=f'Mệnh đề phủ định của mệnh đề "P:${moi} x \\in \\mathbb{{{taphop}}}: {latex(f)} \\ne  {g}$" là'
		noi_dung_loigiai=f'Mệnh đề phủ định là: ${tontai} x \\in \\mathbb{{{taphop}}}: {latex(f)} = {g}$.'

		kq=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} = {g}$"
		kq2=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} \\le {g}$"
		kq3=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} < {g}$"
		kq4=f"${tontai}  x \\in \\mathbb{{{taphop}}}: {latex(f)} > {g}$"	

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

#[D10_C1_B1_07]-M2. Mệnh đề phủ định không chứa biến.
def mjulk_L10_C1_B1_07():
	chon=random.randint(1,6)
	if chon==1:
		a= random.choice([i for i in range(-50, 50) if i!=0])
		b= random.choice([i for i in range(-50, 50) if i!=0])
		c=random.randint(-40,40)
		if b==a: b=a+random.randint(1,5)
		dau=random.choice([">","<","\\ge","\\le","="])	
		noi_dung=f'Mệnh đề phủ định của mệnh đề "${a}+{b}{dau} {c}$" là'.replace("+-","-")
		if dau==">":
			kq=f'${a}+{b} \\le {c}$'
			kq2=f'${a}+{b} < {c}$'
			kq3=f'${a}+{b} \\ne {c}$'
			kq4=kq2=f'${a}+{b} \\ge {c}$'

		if dau=="\\ge":
			kq=f'${a}+{b} < {c}$'
			kq2=f'${a}+{b} \\le {c}$'
			kq3=f'${a}+{b} \\ne {c}$'
			kq4=kq2=f'${a}+{b} > {c}$'

		if dau=="<":
			kq=f'${a}+{b} \\ge {c}$'
			kq2=f'${a}+{b} \\le {c}$'
			kq3=f'${a}+{b} \\ne {c}$'
			kq4=kq2=f'${a}+{b} > {c}$'

		if dau=="\\le":
			kq=f'${a}+{b} > {c}$'
			kq2=f'${a}+{b} \\le {c}$'
			kq3=f'${a}+{b} \\ne {c}$'
			kq4=kq2=f'${a}+{b} < {c}$'

		if dau=="=":
			kq=f'${a}+{b} \\ne {c}$'
			kq2=f'${a}+{b} \\le {c}$'
			kq3=f'${a}+{b} > {c}$'
			kq4=kq2=f'${a}+{b} < {c}$'			

	if chon==2:
		a=random.randint(2,100)
		noi_dung=f'Phủ định của mệnh đề "${{{a}}}$ là số nguyên tố" là'
		kq=f"${{{a}}}$ không phải là số nguyên tố"
		kq2=f"${{{a}}}$ là số tự nhiên"
		kq3=f"${{{a}}}$ là số {random.choice(["nguyên", "hữu tỉ", "vô tỉ"])}"
		kq4=f"${{{a}}}$ không phải là {random.choice(["hợp số", "số tự nhiên", "số nguyên"])}"

	if chon==3:
		a=random.randint(2,100)
		noi_dung=f'Phủ định của mệnh đề "${{{a}}}$ là số tự nhiên" là'
		kq=f"${{{a}}}$ không phải là số tự nhiên"
		kq2=f"${{{a}}}$ là số nguyên tố"
		kq3=f"${{{a}}}$ là số {random.choice(["nguyên", "hữu tỉ", "vô tỉ"])}"
		kq4=f"${{{a}}}$ không phải là {random.choice(["hợp số", "số nguyên tố", "số nguyên"])}"

	if chon==4:
		a=random.randint(2,100)
		noi_dung=f'Phủ định của mệnh đề "${{{a}}}$ là số nguyên" là'
		kq=f"${{{a}}}$ không phải là số nguyên"
		kq2=f"${{{a}}}$ là số nguyên tố"
		kq3=f"${{{a}}}$ là số {random.choice(["thực", "hữu tỉ", "vô tỉ"])}"
		kq4=f"${{{a}}}$ không phải là {random.choice(["hợp số", "số tự nhiên", "số nguyên tố"])}"

	if chon==5:
		a=random.randint(2,100)
		noi_dung=f'Phủ định của mệnh đề "${{{a}}}$ là số chẵn" là'
		kq=f"${{{a}}}$ là số lẻ"
		kq2=f"${{{a}}}$ là số nguyên tố"
		kq3=f"${{{a}}}$ là số {random.choice(["thực", "hữu tỉ", "vô tỉ"])}"
		kq4=f"${{{a}}}$ không phải là {random.choice(["hợp số", "số tự nhiên", "số nguyên tố"])}"

	if chon==6:
		a=random.randint(2,100)
		b=random.randint(2,15)
		if b==a: b=a+1
		noi_dung=f'Phủ định của mệnh đề "${{{a}}}$ chia hết cho ${{{b}}}$" là'
		kq=f"${{{a}}}$ không chia hết cho ${{{b}}}$"
		kq2=f"${{{a}}}$ chia hết cho ${{{b+1}}}$"
		kq3=f"${{{b}}}$ không chia hết cho ${{{a}}}$"
		kq4=f"${{{b}}}$ chia hết cho ${{{a}}}$"	
	noi_dung_loigiai=f'Mệnh đề phủ định của mệnh đề đã cho là {kq}.'.replace("+-","-")

	pa_A= f"*{kq}".replace("+-","-")
	pa_B= f"{kq2}".replace("+-","-")
	pa_C= f"{kq3}".replace("+-","-")
	pa_D= f"{kq4}".replace("+-","-")
	
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

#[D10_C1_B1_08]-M3. Xét tính đúng-sai của mệnh đề kéo theo
def mjulk_L10_C1_B1_08():
	noi_dung=f"Trong các mệnh đề kéo theo sau, mệnh đề nào là mệnh đề đúng"
	a=random.randint(2,10)
	n=random.randint(2,4)
	b=a**n

	chon=random.randint(1,8)
	if chon==1:
		c=random.choice([i for i in range(2,50) if i%2 !=0])
		kq=f"Nếu ${{{b}}}$ chia hết cho ${{{a}}}$ thì ${{{c}}}$ là số lẻ"	

	if chon==2:
		c=random.choice([i for i in range(2,50) if i%2 ==0])
		kq=f"Nếu ${{{b}}}$ chia hết cho ${{{a}}}$ thì ${{{c}}}$ là số chẵn"

	if chon==3:
		a=random.choice(list(primerange(1, 100)))
		c=random.choice([i for i in range(2,50) if i%2 ==0])
		kq=f"Nếu ${{{a}}}$ là số nguyên tố thì ${{{c}}}$ là số chẵn"

	if chon==4:
		a=random.choice(list(primerange(1, 100)))
		c=random.choice([i for i in range(2,50) if i%2 !=0])
		kq=f"Nếu ${{{a}}}$ là số nguyên tố thì ${{{c}}}$ là số lẻ"

	if chon==5:
		a=random.choice(list(primerange(1, 100)))
		c=random.choice([i for i in range(2,50) if i%2 !=0])
		kq=f"Nếu ${{{c}}}$ là số lẻ thì ${{{a}}}$ là số nguyên tố"

	if chon==6:
		a=random.choice(list(primerange(1, 100)))
		c=random.choice([i for i in range(2,50) if i%2 ==0])
		kq=f"Nếu ${{{c}}}$ là số chẵn thì ${{{a}}}$ là số nguyên tố"

	if chon==7:
		a=random.choice(list(primerange(1, 100)))
		c=random.choice([i for i in range(2,50) if i%2 ==0])
		kq=f"Nếu ${{{c}}}$ là số chẵn thì ${{{a+1}}}$ không phải là số nguyên tố"

	if chon==8:
		a=random.choice(list(primerange(1, 100)))
		c=random.choice([i for i in range(2,50) if i%2 !=0])
		kq=f"Nếu ${{{c}}}$ là số lẻ thì ${{{a+1}}}$ không phải là số nguyên tố"

	c=random.choice([i for i in range(2,50) if i%2 !=0])
	
	kq2=f"Nếu ${{{c}}}$ là số lẻ thì ${{{c+1}}}$ là số lẻ"

	a=random.choice(list(primerange(1, 100)))
	c=random.choice([i for i in range(2,50) if i%2 ==0])

	kq3=f"Nếu ${{{a}}}$ là số nguyên tố thì ${{{c}}}$ là số lẻ"

	a=random.randint(1,100)
	c=random.choice(list(primerange(1, 100)))

	kq4=f"Nếu ${{{a}}}$ là số {random.choice(["tự nhiên","nguyên","hữu tỉ"])} thì ${{{c}}}$ là hợp số "

	noi_dung_loigiai=f"{kq} là khẳng định đúng"

	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"

	phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n     D. { list_PA[3]}.\n"
	
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


#BÀI 2 - TẬP HỢP
#[D10_C1_B2_01] Liệt kê các phần tử của tập hợp số nguyên"]
def mjulk_L10_C1_B2_01():
	#Tạo ngẫu nhiên hai tập hợp
	a=random.randint(-6,-1)
	b=a + random.randint(2,4)
	
	truong_hop=random.choice(["[a,b]","[a,b)", "(a,b]", "(a,b)"])	
	if truong_hop=="[a,b]":
		dieu_kien_x=f"{a} \\le x \\le {b}"
		kq=set(range(a, b + 1))
		kq2=set(range(a, b))
		kq3=set(range(a+1, b))
		kq4=set(range(a+1, b+1))
	elif truong_hop=="[a,b)":
		dieu_kien_x=f"{a} \\le x <{b}"
		kq=set(range(a, b))
		kq2=set(range(a, b-1))
		kq3=set(range(a+1, b))
		kq4=set(range(a+1, b+1))

	elif truong_hop=="(a,b]":
		dieu_kien_x=f"{a} < x \\le {b}"
		kq=set(range(a+1, b+1))
		kq2=set(range(a, b-1))
		kq3=set(range(a+1, b))
		kq4=set(range(a, b+1))
	else:
		dieu_kien_x=f"{a} < x < {b}"
		kq=set(range(a+1, b))
		kq2=set(range(a, b-1))
		kq3=set(range(a+1, b-1))
		kq4=set(range(a, b+1))

	kq=str(sorted(kq))
	kq2=str(sorted(kq2))
	kq3=str(sorted(kq3))
	kq4=str(sorted(kq4))

	kq=my_module.xoa_ngoac_vuong(kq)
	kq2=my_module.xoa_ngoac_vuong(kq2)
	kq3=my_module.xoa_ngoac_vuong(kq3)
	kq4=my_module.xoa_ngoac_vuong(kq4)

	#Tạo các phương án
	pa_A=f"*$A=\\{{{kq}\\}}$"
	pa_B=f"$A=\\{{{kq2}\\}}$"
	pa_C=f"$A=\\{{{kq3}\\}}$"
	pa_D=f"$A=\\{{{kq4}\\}}$"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Liệt kê các phần tử của tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{dieu_kien_x} \\}}$. "
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

#[D10_C1_B2_02] Liệt kê các phần tử là nghiệm của phương trình bậc 2"]
def mjulk_L10_C1_B2_02():
	x=sp.symbols("x")
	ten=random.choice(["A","B", "C", "E", "F", "M", "H" ])
	chon=random.randint(1,4)	
	if chon==1:
		a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c = random.randint(-10,10)		
		f=a*x**2+b*x+c
		delta = b**2-4*a*c
		noi_dung= f"Liệt kê các phần tử của tập hợp ${ten}=\\{{x\\in \\mathbb{{R}}|{latex(f)}=0 \\}}$."			
		if delta<0:
			x_1=(-b-sqrt(-delta))/(2*a)
			x_2=(-b+sqrt(-delta))/(2*a)
			kq=f"${ten}=\\emptyset$"
			kq2=f"${ten}=\\{{{latex(my_module.hien_phan_so(-b/(2*a)))}\\}}$"
			kq3=f"${ten}=\\{{{latex(my_module.hien_phan_so(-b/a ))}\\}}$"
			kq4=f"${ten}=\\{{{latex(x_1)}, {latex(x_2)}\\}}$"
			noi_dung_loigiai=f"Phương trình ${latex(f)}=0$ vô nghiệm nên {kq}."
		elif delta==0:
			kq=f"${ten}=\\{{{latex(my_module.hien_phan_so(-b/(2*a)))}\\}}$"
			kq2=f"${ten}=\\{{{latex(my_module.hien_phan_so(-b/a))}\\}}$"
			kq3=f"${ten}=\\{{{latex(my_module.hien_phan_so(c/a))}\\}}$"
			kq4=f"${{{ten}=\\emptyset}}$"
			noi_dung_loigiai=f"Phương trình ${latex(f)}=0$ có nghiệm $x={phan_so(-b/(2*a))}$ nên {kq}."
		else:
			x_1=(-b+sqrt(delta))/(2*a)
			x_2=(-b-sqrt(delta))/(2*a)
			kq=f"${ten}=\\{{{latex(x_1)}, {latex(x_2)}\\}}$"
			kq2=f"${ten}=\\emptyset$"
			kq3=f"${ten}=\\{{{latex(my_module.hien_phan_so(-b/(2*a)))}\\}}$"
			kq4=f"${ten}=\\{{{latex(my_module.hien_phan_so(c/a))}\\}}$"
			noi_dung_loigiai=f"Phương trình ${latex(f)}=0$ có nghiệm $x_1={latex(x_1)}, x_2={latex(x_2)}$ nên {kq}."
	if chon==2:
		x_1=random.randint(-6,-1)
		x_2=random.randint(1,10)
		a=random.randint(1,3)
		f=a*(x-x_1)*(x-x_2)
		noi_dung= f"Số phần tử của tập hợp ${ten}=\\{{x\\in \\mathbb{{N}}|{latex(expand(f))}=0 \\}}$."
		
		kq=f"${{1}}$"
		kq2=f"${{0}}$"
		kq3=f"${{2}}$"
		kq4=f"${{3}}$"
		noi_dung_loigiai=(
		f"Phương trình ${latex(expand(f))}=0$ có nghiệm $x_1={x_1}\\notin \\mathbb{{N}}, x_2={x_2} \\in \\mathbb{{N}}$.\n\n"
		f"Vậy ${ten}=\\{{{x_2}\\}}$ có 1 phần tử.")

	if chon==3:
		i=random.randint(4,10)
		a=random.randint(1,3)
		x_2=random.randint(-8,8)
		f=(i*x-a)*(x-x_2)		
		taphop=random.choice(["Z"])
		noi_dung= f"Số phần tử của tập hợp ${ten}=\\{{x\\in \\mathbb{{{taphop}}}|{latex(expand(f))}=0 \\}}$."
		
		kq=f"${{1}}$"
		kq2=f"${{0}}$"
		kq3=f"${{2}}$"
		kq4=f"${{3}}$"
		noi_dung_loigiai=(
		f"Phương trình ${latex(expand(f))}=0$ có nghiệm $x_1={phan_so(a/i)}\\notin \\mathbb{{{taphop}}}, x_2={x_2} \\in \\mathbb{{{taphop}}}$.\n\n"
		f"Vậy ${ten}=\\{{{x_2}\\}}$ có 1 phần tử.")

	if chon==4:
		i=random.randint(4,10)
		a=random.randint(1,3)
		x_2=random.randint(-8,-1)
		f=(i*x-a)*(x-x_2)		
		taphop=random.choice(["N"])
		noi_dung= f"Số phần tử của tập hợp ${ten}=\\{{x\\in \\mathbb{{{taphop}}}|{latex(expand(f))}=0 \\}}$."
		
		kq=f"${{0}}$"
		kq2=f"${{1}}$"
		kq3=f"${{2}}$"
		kq4=f"${{3}}$"
		noi_dung_loigiai=(
		f"Phương trình ${latex(expand(f))}=0$ có nghiệm $x_1={phan_so(a/i)}\\notin \\mathbb{{{taphop}}}, x_2={x_2} \\notin  \\mathbb{{{taphop}}}$.\n\n"
		f"Vậy ${ten}=\\emptyset $ có 0 phần tử.")


	#Tạo các phương án
	pa_A=f"*{kq}"
	pa_B=f"{kq2}"
	pa_C=f"{kq3}"
	pa_D=f"{kq4}"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	
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


#[D10_C1_B2_03] Liệt kê các phần tử là ước của n
def mjulk_L10_C1_B2_03():
	#Tạo ngẫu nhiên hai tập hợp
	n=random.choice([10,12,14,15,16,18,20,22,24,25,26,28,30])
	k=random.randint(2,7)
	divisors_list = divisors(n)
	divisors_greater = [divisor for divisor in divisors_list if divisor > k]
	divisors_less = [divisor for divisor in divisors_list if divisor < k]
	divisors_list_k = divisors(k)
	list_random=[i for i in range(k)]

	dau=random.choice([">","<"])
	if dau==">":
		kq=str(sorted(divisors_greater))
		kq2=str(sorted(divisors_less))
		kq3=str(sorted(divisors_list_k ))
		kq4=str(sorted(list_random))
	else:
		kq=str(sorted(divisors_less))
		kq2=str(sorted(divisors_greater))		
		kq3=str(sorted(divisors_list_k))
		kq4=str(sorted(list_random))	


	kq=my_module.xoa_ngoac_vuong(kq)
	kq2=my_module.xoa_ngoac_vuong(kq2)
	kq3=my_module.xoa_ngoac_vuong(kq3)
	kq4=my_module.xoa_ngoac_vuong(kq4)	


	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$"
	pa_B=f"$\\{{{kq2}\\}}$"
	pa_C=f"$\\{{{kq3}\\}}$"
	pa_D=f"$\\{{{kq4}\\}}$"

	pa_A=pa_A.replace("*$\\{\\}$","*${{\\emptyset}}$")
	pa_B=pa_B.replace("*$\\{\\}$","*${{\\emptyset}}$")
	pa_C=pa_C.replace("*$\\{\\}$","*${{\\emptyset}}$")
	pa_D=pa_D.replace("*$\\{\\}$","*${{\\emptyset}}$")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Liệt kê các phần tử của tập hợp $A=\\{{x\\in \\mathbb{{N}}|x {dau}{k}, x$ là ước của ${n}\\}}$. "
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

#[D10_C1_B2_04]-M2. Liệt kê các phần tử là bội của n
def mjulk_L10_C1_B2_04():
	#Tạo ngẫu nhiên hai tập hợp

	n=random.randint(3,8)
	m=random.choice([10, 12, 15, 16, 20, 24, 25, 30, 35, 40])

	kq=my_module.tim_boi_của_n_nho_hon_m(n,m)

	kq2=divisors(n)
	kq3=[n,n*3,n*5]
	kq4=list_random=[i for i in range(n) ]

	kq=str(sorted(kq))
	kq2=str(sorted(kq2))
	kq3=str(sorted(kq3))
	kq4=str(sorted(list_random))	


	kq=my_module.xoa_ngoac_vuong(kq)
	kq2=my_module.xoa_ngoac_vuong(kq2)
	kq3=my_module.xoa_ngoac_vuong(kq3)
	kq4=my_module.xoa_ngoac_vuong(kq4)

	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")

	pa_A=pa_A.replace("*$\\{\\}$","*${{\\emptyset}}$")
	pa_B=pa_B.replace("*$\\{\\}$","*${{\\emptyset}}$")
	pa_C=pa_C.replace("*$\\{\\}$","*${{\\emptyset}}$")
	pa_D=pa_D.replace("*$\\{\\}$","*${{\\emptyset}}$")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Liệt kê các phần tử của tập hợp $A=\\{{x\\in \\mathbb{{N}}|x< {m}, x$ là bội của ${n}\\}}$. "
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

#[D10_C1_B2_05]-M2. Chỉ ra tính chất đặc trưng từ tập hợp liệt kê
def mjulk_L10_C1_B2_05():
	chon=random.randint(1,2)

	if chon==1:
		ten_A=["A","C","E", "M", "P"]
		ten_B=["B","D","F", "N", "Q"]
		i=random.randint(0,4)
		ten_A, ten_B=ten_A[i], ten_B[i]
		x=sp.symbols("x")
		chon=random.randint(1,6)		
		if chon==1:
			#Tạo tập hợp A chứa các số nguyên từ a1 đến a2
			a1=random.randint(-8,3)
			a2=a1+random.randint(3,6)
			A=set(range(a1, a2 + 1))

			kq=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$"
			kq2=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x < {a2}\\}}$"
			kq3=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2}\\}}$"
			kq4=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x \\le {a2}\\}}$"
			noi_dung_loigiai=f"Ta có:{kq}."

		if chon==2:
			#Tạo tập hợp A chứa các số nguyên từ a1 đến a2-1
			a1=random.randint(-8,3)
			a2=a1+random.randint(3,6)
			A=set(range(a1, a2))

			kq= f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2}\\}}$"
			kq2=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$"
			kq3=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x < {a2}\\}}$"		
			kq4=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x \\le {a2}\\}}$"
			noi_dung_loigiai=f"Ta có:{kq}."	

		if chon==3:
			#Tạo tập hợp A chứa các số nguyên từ a1+1 đến a2
			a1=random.randint(-8,3)
			a2=a1+random.randint(3,6)
			A=set(range(a1+1, a2+1))	

			kq=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x \\le {a2}\\}}$"
			kq2=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$"
			kq3=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x < {a2}\\}}$"		
			kq4=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x <{a2}\\}}$"
			noi_dung_loigiai=f"Ta có:{kq}."	
		
		if chon==4:
			#Tạo tập hợp A chứa các số nguyên chẵn từ a1+1 đến a2
			a1=random.randint(1,10)
			a2=random.randint(12,20)
			A={i for i in range(a1, a2) if i % 2 == 0}

			kq=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2}, x \\text{{ là số chẵn }} \\right\\}}$"
			kq2=f"${ten_A}=\\left\\{{x\\in \\mathbb{{N}}|{a1} \\le x < {a2} \\right\\}}$"
			kq3=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{a1-2} \\le x < {a2+2}, x \\text{{ là số chẵn }} \\right\\}}$"
			kq4=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{a1+2} < x \\le {a2+2},, x \\text{{ là số nguyên tố }} \\right\\}}$"
			noi_dung_loigiai=f"Ta có:{kq}."	

		if chon==5:
			#Tạo tập hợp A chứa các số nguyên lẻ từ a1+1 đến a2
			a1=random.randint(1,10)
			a2=random.randint(12,20)
			A={i for i in range(a1, a2) if i % 2 != 0}

			kq=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2}, x \\text{{ là số lẻ }} \\right\\}}$"
			kq2=f"${ten_A}=\\left\\{{x\\in \\mathbb{{N}}|{a1-2} < x \\le {a2+2}, x \\text{{ là số lẻ }} \\right\\}}$"
			kq3=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2+2}, x \\text{{ là số lẻ }} \\right\\}}$"
			kq4=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2} \\right\\}}$"
			noi_dung_loigiai=f"Ta có:{kq}."
		
		if chon==6:
			a1=random.randint(-8,-1)
			a2=a1+random.randint(1,10)
			if a2==0: a2==random.randint(1,5)	
			A={a1,a2}
			f=latex(expand((x-a1)*(x-a2)))
			f2=latex(expand((x+a1)*(x+a2)))
			f3=latex(expand((x+a1)*(x-a2)))
			f4=latex(expand((x-a1)*(x+a2)))

			kq=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{f}=0 \\right\\}}$"
			kq2=f"${ten_A}=\\left\\{{x\\in \\mathbb{{N}}|{f2}=0 \\right\\}}$"
			kq3=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{f3}=0 \\right\\}}$"
			kq4=f"${ten_A}=\\left\\{{x\\in \\mathbb{{Z}}|{f4}=0 \\right\\}}$"
			noi_dung_loigiai=f"Ta có: ${f}=0 \\Leftrightarrow x={a1},x={a2}$. Do đó: {kq}."

		A=list(A)
		A=sorted(A)
		A=set(A)

		noi_dung= f"Cho tập hợp ${ten_A}=\\{{{A}\\}}$."\
			f" Viết tập hợp ${{{ten_A}}}$ dưới dạng chỉ ra tính chất đặc trưng của các phần tử."
		
		#Tạo các phương án
		pa_A=f"*{kq}"
		pa_B=f"{kq2}"
		pa_C=f"{kq3}"
		pa_D=f"{kq4}"
	
	if chon==2:
		x=symbols(" x ")
		
		# Chọn ngẫu nhiên các giá trị cho a, b, và c
		a = random.randint(6, 10)
		b = random.randint(11, 20)
		c = random.randint(6, 10)
		
		# Đảm bảo rằng b > a + 3
		while not b > a + 3:
		    a = random.randint(6, 16)
		    b = random.randint(9, 20)
		
		# Tạo các tập hợp
		A = list(range(a, b + 1))
		A_str = str(A).replace("[", "{").replace("]", "}").replace(", ", ";")
		
		# Nội dung đề bài
		noi_dung = f"Chỉ ra tính chất đặc trưng của tập hợp $ A=\\left\\{{ {A_str} \\right\\}} $. "

		noi_dung_loigiai= f"\n $ A=\\left\\{{ x \\in \\mathbb{{N}} \\mid {a} \\le x \\le {b} \\right\\}}$"
		   
		pa_A= f"*$ A=\\left\\{{ x \\in \\mathbb{{N}} \\mid {a} \\le x \\le {b} \\right\\}} $"
		pa_B= f"$ A=\\left\\{{ x \\in \\mathbb{{N}} \\mid  x \\le {b} \\right\\}} $"
		pa_C= f"$ A=\\left\\{{ x \\in \\mathbb{{N}} \\mid  x \\ge {b} \\right\\}} $"
		pa_D= f"$ A=\\left\\{{ x \\in \\mathbb{{N}}  \\mid {1} \\le x \\le {b} \\right\\}} $"
	

	
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

#ĐÚNG -SAI
#[D10_C1_B2_06]-TF-M2. Cho tập hợp dạng đặc trưng. Xét đúng-sai: Số phần tử, Liệt kê, số tập hợp con, xác định tập hợp con
def mjulk_L10_C1_B2_06():
	ten_A=["A","C","E", "M", "P"]
	ten_B=["B","D","F", "N", "Q"]
	i=random.randint(0,4)
	ten_A, ten_B=ten_A[i], ten_B[i]
	x=sp.symbols("x")	
	
	#Tạo tập hợp A chứa các số nguyên từ a1 đến a2
	a1=random.randint(-8,3)
	a2=a1+random.randint(3,6)
	A=set(range(a1, a2 + 1))
	A=list(A)
	A=sorted(A)
	A=set(A)
	n=a2-a1+1
	A_fasle=set(range(a1, a2))
	noi_dung=f"Cho tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$. Xét tính đúng-sai của các khẳng định sau?"
	
	kq1_T=f"*${ten_A}=\\{{x\\in \\mathbb{{Z}}| {A} \\}}$"
	kq1_F=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}| {A_fasle} \\}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Liệt kê các phần tử của tập hợp ta được: ${ten_A}=\\{{ {A} \\}}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Số phần tử của tập hợp ${{{ten_A}}}$ là ${{{a2-a1+1}}}$"
	kq2_F=f"Số phần tử của tập hợp ${{{ten_A}}}$ là ${{{a2-a1}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Liệt kê các phần tử của tập hợp ta được: ${ten_A}=\\{{{A}\\}}$.\n\n"\
	f"Số phần tử của tập hợp ${{{ten_A}}}$ là ${{{a2-a1+1}}}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"*Số tập hợp con của tập hợp ${{{ten_A}}}$ là ${{{2**n}}}$" 
	kq3_F=f"Số tập hợp con của tập hợp ${{{ten_A}}}$ là ${{{2**(n-1)}}}$ "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Số tập hợp con của tập hợp ${{{ten_A}}}$ là $2^{{{n}}}={2**n}$"
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	chon=random.randint(1,2)
	
	if chon==1:
		B={i for i in range(a1+1,a2-random.randint(1,2))}
		kq4_T=f"*Tập hợp $\\{{{B}\\}}$ là một tập hợp con của tập hợp ${{{ten_A}}}$"
		kq4_F=f"Tập hợp $\\{{{B}\\}}$ không phải là một tập hợp con của tập hợp ${{{ten_A}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Tập hợp $\\{{{B}\\}}$ là tập hợp con của tập hợp ${{{ten_A}}}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon==2:
		B={i for i in range(a1+1,a2-random.randint(1,2))}
		B.add(random.choice([random.randint(-11, a1-1), random.randint(a2+2, 15)]))
		kq4_T=f"*Tập hợp $\\{{{B}\\}}$ không phải là một tập hợp con của tập hợp ${{{ten_A}}}$"
		kq4_F=f"Tập hợp $\\{{{B}\\}}$ là một tập hợp con của tập hợp ${{{ten_A}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Tập hợp $\\{{{B}\\}}$ không phải là tập hợp con của tập hợp ${{{ten_A}}}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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

#[D10_C1_B2_07]-TF-M3. Xét đúng sai về số phần tử của: a<x<b, ax^2+bx+c=0, phương trình tích, m<ax+b<n
def mjulk_L10_C1_B2_07():

	noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	a=random.randint(-10,3)
	b=a+random.randint(4,10)
	
	chon=random.randint(1,2)	
	if chon==1:
		kq1_T=f"* Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}<x<{b}\\}}$ có số phần tử là ${{{b-a-1}}}$" 
		kq1_F=f" Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}<x<{b}\\}}$ có số phần tử là ${{{b-a}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}<x<{b}\\}}$ có số phần tử là ${{{b-a-1}}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq1_T=f"* Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a} \\le x \\le {b}\\}}$ có số phần tử là ${{{b-a+1}}}$" 
		kq1_F=f" Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}\\le x \\le {b}\\}}$ có số phần tử là ${{{b-a}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}\\le x \\le{b}\\}}$ có số phần tử là ${{{b-a+1}}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		kq1_T=f"* Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a} \\le x < {b}\\}}$ có số phần tử là ${{{b-a}}}$" 
		kq1_F=f" Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}\\le x < {b}\\}}$ có số phần tử là ${{{b-a+1}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}\\le x <{b}\\}}$ có số phần tử là ${{{b-a}}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==4:
		kq1_T=f"* Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a} < x \\le {b}\\}}$ có số phần tử là ${{{b-a}}}$" 
		kq1_F=f" Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}< x \\le {b}\\}}$ có số phần tử là ${{{b-a+1}}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"Tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a}< x \\le {b}\\}}$ có số phần tử là ${{{b-a}}}$."
		loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq1==kq1_F:
			loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	x=sp.symbols("x")
	x_1=random.randint(-6,5)
	x_2=x_1+random.randint(1,5)
	a=random.randint(1,3)
	chon=random.randint(1,2)	
	
	if chon==1:
		f=a*(x-x_1)*(x-x_2)
		kq2_T=f"* Tập hợp $B=\\{{x\\in \\mathbb{{R}}| {latex(expand(f))}=0\\}}$ có 2 phần tử"
		kq2_F=f"Tập hợp $B=\\{{x\\in \\mathbb{{R}}| {latex(expand(f))}=0\\}}$ có {random.choice([0,1,3])} phần tử"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${latex(expand(f))}=0 \\Rightarrow x={x_1},x={x_2}$. Vậy ${{B}}$ có 2 phần tử."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		f=a*(x-x_1)*(x-x_1)
		kq2_T=f"* Tập hợp $B=\\{{x\\in \\mathbb{{R}}| {latex(expand(f))}=0\\}}$ có 1 phần tử"
		kq2_F=f"Tập hợp $B=\\{{x\\in \\mathbb{{R}}| {latex(expand(f))}=0\\}}$ có {random.choice([0,2,3])} phần tử"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${latex(expand(f))}=0 \\Rightarrow x={x_1}$. Vậy ${{B}}$ có 1 phần tử."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		f=a*(x-x_1)**2+random.randint(1,9)
		kq2_T=f"* Tập hợp $B=\\{{x\\in \\mathbb{{R}}| {latex(expand(f))}=0\\}}$ có 0 phần tử"
		kq2_F=f"Tập hợp $B=\\{{x\\in \\mathbb{{R}}| {latex(expand(f))}=0\\}}$ có {random.choice([1,2,3])} phần tử"
		kq2=random.choice([kq2_T, kq2_F])
		HDG=f"${latex(expand(f))}=0$  vô nghiệm. Vậy ${{B}}$ có 0 phần tử."
		loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq2==kq2_F:
			loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	

	chon=random.randint(1,3)
	if chon==1:
		x_0=random.randint(1,5)
		x_1=random.choice([2,3,5,7,11,13])
		a=random.randint(1,5)
		b= random.choice([i for i in range(-6, 6) if i!=0])
		if b/a==x_0:b=b+1
		chon=random.randint(1,2)
		if chon==1:
			f=(x**2-x_0**2)*(x-sqrt(x_1))*(a*x+b)
			HDG=f"${latex(f)}=0 \\Rightarrow x=\\pm {x_0} \\in \\mathbb{{Q}}, x={latex(sqrt(x_1))} \\notin \\mathbb{{Q}},x={phan_so(-b/a)}\\in \\mathbb{{Q}}$.\n\n"\
			f"Do đó ${{C}}$ có 3 phần tử."
		
		if chon==2:
			f=(x**2-x_0**2)*(x+sqrt(x_1))*(a*x+b)
			HDG=f"${latex(f)}=0 \\Rightarrow x=\\pm {x_0} \\in \\mathbb{{Q}}, x=-{latex(sqrt(x_1))} \\notin \\mathbb{{Q}},x={phan_so(-b/a)}\\in \\mathbb{{Q}}$.\n\n"\
			f"Do đó ${{C}}$ có 3 phần tử."
		
		kq3_T=f"* Tập hợp $C=\\left\\{{x\\in \\mathbb{{Q}}|{latex(f)}=0 \\right\\}}$ có 3 phần tử" 
		kq3_F=f"Tập hợp $C=\\left\\{{x\\in \\mathbb{{Q}}|{latex(f)}=0 \\right\\}}$ có {random.choice([0,1,2,4])} phần tử"
	
	if chon==2:
		x_0=random.randint(1,5)
		x_1=random.choice([2,3,5,7,11,13])
		a=random.randint(1,5)
		b= random.choice([i for i in range(-6, 6) if i!=0])
		if b/a==x_0:b=b+1
		
		if chon==1:
			f=(x**2-x_0**2)*(x-sqrt(x_1))
			HDG=f"${latex(f)}=0 \\Rightarrow x=\\pm {x_0} \\in \\mathbb{{Q}}, x={latex(sqrt(x_1))}$.\n\n"\
			f"Do đó ${{C}}$ có 2 phần tử."
		
		if chon==2:
			f=(x**2-x_0**2)*(x+sqrt(x_1))
			HDG=f"${latex(f)}=0 \\Rightarrow x=\\pm {x_0} \\in \\mathbb{{Q}}, x=-{latex(sqrt(x_1))} \\notin \\mathbb{{Q}}$.\n\n"\
			f"Do đó ${{C}}$ có 2 phần tử."
		
		kq3_T=f"* Tập hợp $C=\\left\\{{x\\in \\mathbb{{Q}}|{latex(f)}=0 \\right\\}}$ có 2 phần tử" 
		kq3_F=f"Tập hợp $C=\\left\\{{x\\in \\mathbb{{Q}}|{latex(f)}=0 \\right\\}}$ có {random.choice([0,1,3])} phần tử"

	if chon==3:
		x_0=random.randint(1,5)
		x_1=random.choice([2,3,5,7,11,13])
		a=random.randint(1,5)
		b= random.choice([i for i in range(-6, 6) if i!=0])
		if b/a==x_0:b=b+1
		
		
		f=(x**2-x_0**2)*(a*x+b)**2
		HDG=f"${latex(f)}=0 \\Rightarrow x=\\pm {x_0} \\in \\mathbb{{Q}}, x={phan_so(-b/a)}$.\n\n"\
		f"Do đó ${{C}}$ có 3 phần tử."		
		
		kq3_T=f"* Tập hợp $C=\\left\\{{x\\in \\mathbb{{Q}}|{latex(f)}=0 \\right\\}}$ có 3 phần tử" 
		kq3_F=f"Tập hợp $C=\\left\\{{x\\in \\mathbb{{Q}}|{latex(f)}=0 \\right\\}}$ có {random.choice([0,1,2])} phần tử"
		
	kq3=random.choice([kq3_T, kq3_F])	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	n=sp.symbols("n")
	a=random.randint(1,5)
	b=a+random.randint(4,10)
	t_1= random.choice([i for i in range(-5, 6) if i!=0])
	t_2=random.randint(-6,6)
	#a<n<b

	kq4_T=f"* Tập hợp $D=\\left\\{{n\\in \\mathbb{{N}}|{latex(a+t_1*n+t_2)}<{latex(n+t_1*n+t_2)}<{latex(b+t_1*n+t_2)} \\right\\}}$ có ${{{b-a-1}}}$ phần tử"
	kq4_F=f"Tập hợp $D=\\left\\{{n\\in \\mathbb{{N}}|{latex(a+t_1*n+t_2)}<{latex(n+t_1*n+t_2)}<{latex(b+t_1*n+t_2)} \\right\\}}$ có ${{{b-a}}}$ phần tử" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"${latex(a+t_1*n+t_2)}<{latex(n+t_1*n+t_2)}<{latex(b+t_1*n+t_2)} \\Rightarrow {a}<n<{b}$. Suy ra ${{D}}$ có ${{{b-a-1}}}$ phần tử."
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

#[D10_C1_B2_08]-TF-M2. Cho tập hợp dạng liệt kê. Xét đúng-sai: Số phần tử, Liệt kê, số tập hợp con, xác định tập hợp con
def mjulk_L10_C1_B2_08():
	ten_A=["A","C","E", "M", "P"]
	ten_B=["B","D","F", "N", "Q"]
	i=random.randint(0,4)
	ten_A, ten_B=ten_A[i], ten_B[i]
	x=sp.symbols("x")	
	
	#Tạo tập hợp A chứa các số nguyên từ a1 đến a2
	a1=random.randint(-8,3)
	a2=a1+random.randint(3,6)
	A=set(range(a1, a2 + 1))
	A=list(A)
	A=sorted(A)
	A=set(A)
	n=a2-a1+1
	A_fasle=set(range(a1, a2))
	noi_dung=f"Cho tập hợp ${ten_A}=\\{{{A}\\}}$. Xét tính đúng-sai của các khẳng định sau?"
	
	kq1_T=f"*${ten_A}=\\{{x\\in \\mathbb{{Z}}| {a1} \\le x \\le {a2} \\}}$"
	kq1_F=f"${ten_A}=\\{{x\\in \\mathbb{{Z}}| {a1} < x < {a2} \\}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Ta có: ${ten_A}=\\{{{a1} \\le x \\le {a2}\\}}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Số phần tử của tập hợp ${{{ten_A}}}$ là ${{{a2-a1+1}}}$"
	kq2_F=f"Số phần tử của tập hợp ${{{ten_A}}}$ là ${{{a2-a1}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Số phần tử của tập hợp ${{{ten_A}}}$ là ${{{a2-a1+1}}}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"*Số tập hợp con của tập hợp ${{{ten_A}}}$ là ${{{2**n}}}$" 
	kq3_F=f"Số tập hợp con của tập hợp ${{{ten_A}}}$ là ${{{2**(n-1)}}}$ "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Số tập hợp con của tập hợp ${{{ten_A}}}$ là $2^{{{n}}}={2**n}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	chon=random.randint(1,2)
	
	if chon==1:
		B={i for i in range(a1+1,a2-random.randint(1,2))}
		kq4_T=f"*Tập hợp $\\{{{B}\\}}$ là một tập hợp con của tập hợp ${{{ten_A}}}$"
		kq4_F=f"Tập hợp $\\{{{B}\\}}$ không phải là một tập hợp con của tập hợp ${{{ten_A}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Tập hợp $\\{{{B}\\}}$ là tập hợp con của tập hợp ${{{ten_A}}}$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	if chon==2:
		B={i for i in range(a1+1,a2-random.randint(1,2))}
		B.add(random.choice([random.randint(-11, a1-1), random.randint(a2+2, 15)]))
		kq4_T=f"*Tập hợp $\\{{{B}\\}}$ không phải là một tập hợp con của tập hợp ${{{ten_A}}}$"
		kq4_F=f"Tập hợp $\\{{{B}\\}}$ là một tập hợp con của tập hợp ${{{ten_A}}}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Tập hợp $\\{{{B}\\}}$ không phải là tập hợp con của tập hợp ${{{ten_A}}}$."
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

#[D10_C1_B2_09]-M2. Liệt kê các số là nguyên tố
def mjulk_L10_C1_B2_09():
	a=random.randint(2,11)
	b=a+random.randint(10,30)
	ten=random.choice(["A", "B","C","D","E","M","N"])
	chon=random.randint(1,4)
	if chon==1:
		primerange = list(sympy.primerange(a, b + 1))
		so_phantu=len(primerange)

		noi_dung=(
		f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}\\le n \\le {b}, n \\text{{ là số nguyên tố}} \\}}$"
		)
	
	if chon==2:
		primerange = list(sympy.primerange(a+1, b))
		so_phantu=len(primerange)

		noi_dung=(
		f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}< n <{b}, n \\text{{ là số nguyên tố}} \\}}$"
		)

	if chon==3:
		primerange = list(sympy.primerange(a+1, b+1))
		so_phantu=len(primerange)

		noi_dung=(
		f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}< n \\le {b}, n \\text{{ là số nguyên tố}} \\}}$"
		)

	if chon==4:
		primerange = list(sympy.primerange(a, b))
		so_phantu=len(primerange)

		noi_dung=(
		f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}\\le n < {b}, n \\text{{ là số nguyên tố}} \\}}$"
		)
	
	

	noi_dung_loigiai=(
	f"${ten}=\\{{{primerange}\\}}$.\n\n"
	f"Số phần tử là: {so_phantu}."
	)
	noi_dung_loigiai=noi_dung_loigiai.replace("[","").replace("]","")

	kq=so_phantu
	kq_false=[so_phantu-1, so_phantu+1, so_phantu+random.randint(1,3), so_phantu-random.randint(1,3)]
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]	

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
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

#[D10_C1_B2_10]-M2. Liệt kê các số là số chẵn hoặc số lẻ
def mjulk_L10_C1_B2_10():
	a=random.randint(2,15)
	b=a+random.randint(10,15)
	ten=random.choice(["A", "B","C","D","E","M","N"])
	chon=random.choice(["chẵn","lẻ"])
	if chon=="chẵn":
		chon=random.randint(1,4)
		
		if chon==1:
			list_kq= [i for i in range(a,b+1) if i%2==0]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}\\le n \\le {b}, n \\text{{ là số chẵn}} \\}}$"
			)

		if chon==2:
			list_kq= [i for i in range(a+1,b+1) if i%2==0]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}< n \\le {b}, n \\text{{ là số chẵn}} \\}}$"
			)

		if chon==3:
			list_kq= [i for i in range(a,b) if i%2==0]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a} \\le n < {b}, n \\text{{ là số chẵn}} \\}}$"
			)

		if chon==4:
			list_kq= [i for i in range(a+1,b) if i%2==0]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}< n < {b}, n \\text{{ là số chẵn}} \\}}$"
			)
	
	if chon=="lẻ":
		chon=random.randint(1,4)

		if chon==1:
			list_kq= [i for i in range(a,b+1) if i%2]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}\\le n \\le {b}, n \\text{{ là số lẻ}} \\}}$"
			)

		if chon==2:
			list_kq= [i for i in range(a+1,b+1) if i%2]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}< n \\le {b}, n \\text{{ là số lẻ}} \\}}$"
			)

		if chon==3:
			list_kq= [i for i in range(a,b) if i%2]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a} \\le n < {b}, n \\text{{ là số lẻ}} \\}}$"
			)

		if chon==4:
			list_kq= [i for i in range(a+1,b) if i%2]
			so_phantu=len(list_kq)

			noi_dung=(
			f"Số các phần tử của tập hợp ${ten}=\\{{n\\in \\mathbb{{N}}| {a}< n < {b}, n \\text{{ là số lẻ}} \\}}$"
			)
	
	noi_dung_loigiai=(
	f"${ten}=\\{{{list_kq}\\}}$.\n\n"
	f"Số phần tử là: {so_phantu}."
	)
	noi_dung_loigiai=noi_dung_loigiai.replace("[","").replace("]","")

	kq=so_phantu
	kq_false=[so_phantu-1, so_phantu+1, so_phantu+random.randint(1,3), so_phantu-random.randint(1,3)]
	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]	

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

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

#[D10_C1_B2_11]-M2. Liệt kê phần tử thỏa mãn điều kiện tùy ý
def mjulk_L10_C1_B2_11():
	chon=random.randint(1,6)
	if chon==1:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B2_01()	
	if chon==2:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B2_02()
	if chon==3:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B2_03()
	if chon==4:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B2_04()
	if chon==5:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B2_09()
	if chon==6:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B2_10()

	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

	
#------------------------------------------------------------------------->
#BÀI 3: CÁC PHÉP TOÁN TRÊN TẬP HỢP


#[D10_C1_B3_01]. Tìm giao của 2 tập hợp dạng liệt kê
def mjulk_L10_C1_B3_01():
	#Tạo ngẫu nhiên hai tập hợp
	set_A =my_module.tao_taphop(4,-6,6)
	set_B =my_module.tao_taphop(5,-10,7)
	while set_A==set_B:
		set_A =my_module.tao_taphop(4,-6,6)
		set_B =my_module.tao_taphop(5,-10,7)

	#List kết quả
	kq = set_A & set_B 
	kq2 = set_B - set_A
	kq3= set_A-set_B
	kq4= set_A | set_B

	kq=my_module.thay_kihieu_taphop(str(kq))
	kq2=my_module.thay_kihieu_taphop(str(kq2))
	kq3=my_module.thay_kihieu_taphop(str(kq3))
	kq4=my_module.thay_kihieu_taphop(str(kq4))

	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho hai tập hợp $A=\\{{{set_A}\\}}$ và $B=\\{{{set_B}\\}}$. Tìm tập hợp $A\\cap B$. "
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

#[D10_C1_B3_02]. Tìm hợp của 2 tập hợp dạng liệt kê
def mjulk_L10_C1_B3_02():
	#Tạo ngẫu nhiên hai tập hợp
	set_A =my_module.tao_taphop(5,-5,6)
	set_B =my_module.tao_taphop(6,-8,8)
	while set_A==set_B:
		set_A =my_module.tao_taphop(5,-5,6)
		set_B =my_module.tao_taphop(6,-8,8)
	#List kết quả
	kq = set_A | set_B
	kq2 = set_B - set_A
	kq3= set_A & set_B
	kq4= set_A-set_B

	kq=my_module.thay_kihieu_taphop(str(kq))
	kq2=my_module.thay_kihieu_taphop(str(kq2))
	kq3=my_module.thay_kihieu_taphop(str(kq3))
	kq4=my_module.thay_kihieu_taphop(str(kq4))


	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho hai tập hợp $A=\\{{{set_A}\\}}$ và $B=\\{{{set_B}\\}}$. Tìm tập hợp $A\\cup B$. "
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

#[D10_C1_B3_03]. Tìm hiệu của 2 tập hợp dạng liệt kê
def mjulk_L10_C1_B3_03():
	#Tạo ngẫu nhiên hai tập hợp
	set_A =my_module.tao_taphop(5,-5,6)
	set_B =my_module.tao_taphop(6,-8,8)
	while set_A==set_B:
		set_A =my_module.tao_taphop(5,-5,6)
		set_B =my_module.tao_taphop(6,-8,8)
	#List kết quả
	kq = set_A-set_B
	kq2 = set_B - set_A
	kq3= set_A & set_B
	kq4= set_A | set_B

	kq=my_module.thay_kihieu_taphop(str(kq))
	kq2=my_module.thay_kihieu_taphop(str(kq2))
	kq3=my_module.thay_kihieu_taphop(str(kq3))
	kq4=my_module.thay_kihieu_taphop(str(kq4))

	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho hai tập hợp $A=\\{{{set_A}\\}}$ và $B=\\{{{set_B}\\}}$. Tìm tập hợp $A\\backslash B$. "
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

#[D10_C1_B3_04]-M2. Tìm phần bù của 2 tập hợp dạng liệt kê
def mjulk_L10_C1_B3_04():
	ten_A=["A","C","E", "M", "P"]
	ten_B=["B","D","F", "N", "Q"]
	i=random.randint(0,4)
	ten_A, ten_B=ten_A[i], ten_B[i]

	#Tạo ngẫu nhiên hai tập hợp
	k=random.randint(4,7)
	m=random.randint(2,k-1)

	A =set(random.sample(range(-10, 10), k))
	# Chuyển tập hợp A thành danh sách
	list_A=list(A)
	random.shuffle(list_A)
	B = set()
	for i in range(m):
		B.add(list_A[i])
	
	kq = A-B
	kq2 = B - A
	kq3= A & B
	kq4= A | B

	kq=str(kq)
	kq2=str(kq2)
	kq3=str(kq3)
	kq4=str(kq4)
	noi_dung_loigiai=f"Do ${ten_B} \\subset {ten_A}$ nên $C_{ten_A} {ten_B}={ten_A}\\backslash {ten_B}=\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")

	noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{{A}\\}}$ và ${ten_B}=\\{{{B}\\}}$. Tìm tập hợp $C_{ten_A} {ten_B}$."
	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	
	
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

#[D10_C1_B3_05]-M2. Tìm giao của 2 tập hợp dạng tính chất đặc trưng
def mjulk_L10_C1_B3_05():
	ten_A=["A","C","E", "M", "P"]
	ten_B=["B","D","F", "N", "Q"]
	i=random.randint(0,4)
	ten_A, ten_B=ten_A[i], ten_B[i]
	chon=random.randint(1,3)
	if chon==1:
		#Tạo tập hợp A chứa các số nguyên từ a1 đến a2
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)
		A=set(range(a1, a2 + 1))

		#Tạo tập hợp A chứa các số nguyên từ b1 đến b2
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		B=set(range(b1, b2 + 1))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} \\le x \\le {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\cap {ten_B}$."

	if chon==2:
		#Tạo tập hợp A chứa các số nguyên từ a1 đến a2-1
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)
		A=set(range(a1, a2))

		#Tạo tập hợp A chứa các số nguyên từ b1+1 đến b2
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		B=set(range(b1+1, b2+1))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} < x \\le {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\cap {ten_B}$."

	if chon==3:
		#Tạo tập hợp A chứa các số nguyên từ a1+1 đến a2
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)
		A=set(range(a1+1, a2+1))

		#Tạo tập hợp A chứa các số nguyên từ b1 đến b2-1
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		B=set(range(b1, b2))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x \\le {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} \\le x < {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\cap {ten_B}$."
		
	kq = A & B
	kq2 =B-A
	kq3= A-B
	kq4= A | B

	kq=str(kq)
	kq2=str(kq2)
	kq3=str(kq3)
	kq4=str(kq4)

	A, B=list(A), list(B)
	A, B=sorted(A), sorted(B)
	A, B=set(A), set(B)

	noi_dung_loigiai=f"Ta có: ${ten_A}=\\{{{A}\\}}$ và ${ten_B}=\\{{{B}\\}}$. Do đó ${ten_A}\\cap {ten_B} =\\{{{kq}\\}}$.".replace(f"\\{{set()\\}}",f"\\emptyset")
	
	
	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án	
	
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

#[D10_C1_B3_06]-M2. Tìm hợp của 2 tập hợp dạng tính chất đặc trưng
def mjulk_L10_C1_B3_06():
	ten_A=["A","C","E", "M", "P"]
	ten_B=["B","D","F", "N", "Q"]
	i=random.randint(0,4)
	ten_A, ten_B=ten_A[i], ten_B[i]
	chon=random.randint(1,3)

	if chon==1:
		#Tạo tập hợp A chứa các số nguyên từ a1 đến a2
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)
		A=set(range(a1, a2 + 1))

		#Tạo tập hợp A chứa các số nguyên từ b1 đến b2
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		B=set(range(b1, b2 + 1))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} \\le x \\le {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\cup {ten_B}$."

	if chon==2:
		#Tạo tập hợp A chứa các số nguyên từ a1 đến a2-1
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)
		A=set(range(a1, a2))

		#Tạo tập hợp A chứa các số nguyên từ b1+1 đến b2
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		B=set(range(b1+1, b2+1))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} < x \\le {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\cup {ten_B}$."

	if chon==3:
		#Tạo tập hợp A chứa các số nguyên từ a1+1 đến a2
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)
		A=set(range(a1+1, a2+1))

		#Tạo tập hợp A chứa các số nguyên từ b1 đến b2-1
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		B=set(range(b1, b2))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x \\le {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} \\le x < {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\cup {ten_B}$."
		
	kq = A | B
	kq2 =B-A
	kq3= A-B
	kq4= A & B

	kq=str(kq)
	kq2=str(kq2)
	kq3=str(kq3)
	kq4=str(kq4)

	A, B=list(A), list(B)
	A, B=sorted(A), sorted(B)
	A, B=set(A), set(B)

	noi_dung_loigiai=f"Ta có: ${ten_A}=\\{{{A}\\}}$ và ${ten_B}=\\{{{B}\\}}$. Do đó ${ten_A}\\cap {ten_B} =\\{{{kq}\\}}$.".replace(f"\\{{set()\\}}",f"\\emptyset")
	
	
	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án	
	
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

#[D10_C1_B3_07]-M2. Tìm hiệu của 2 tập hợp dạng tính chất đặc trưng
def mjulk_L10_C1_B3_07():
	ten_A=["A","C","E", "M", "P"]
	ten_B=["B","D","F", "N", "Q"]
	i=random.randint(0,4)
	ten_A, ten_B=ten_A[i], ten_B[i]
	chon=random.randint(1,3)

	if chon==1:
		#Tạo tập hợp A chứa các số nguyên từ a1 đến a2
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)		

		#Tạo tập hợp A chứa các số nguyên từ b1 đến b2
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		if a1==b1: a1=a1+1
		A=set(range(a1, a2 + 1))
		B=set(range(b1, b2 + 1))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} \\le x \\le {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\backslash {ten_B}$."

	if chon==2:
		#Tạo tập hợp A chứa các số nguyên từ a1 đến a2-1
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)		

		#Tạo tập hợp A chứa các số nguyên từ b1+1 đến b2
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)
		if a1==b1+1: a1=a1+1
		A=set(range(a1, a2))
		B=set(range(b1+1, b2+1))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x < {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} < x \\le {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\backslash {ten_B}$."

	if chon==3:
		#Tạo tập hợp A chứa các số nguyên từ a1+1 đến a2
		a1=random.randint(-7,3)
		a2=a1+random.randint(3,6)
		

		#Tạo tập hợp A chứa các số nguyên từ b1 đến b2-1
		b1=random.randint(-6,2)
		b2=b1+random.randint(3,6)

		if a1+1==b1: a1=a1+2
		A=set(range(a1+1, a2+1))
		B=set(range(b1, b2))

		noi_dung= f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} < x \\le {a2}\\}}$ và ${ten_B}=\\{{x\\in \\mathbb{{Z}}|{b1} \\le x < {b2}\\}}$."\
		f" Tìm tập hợp ${ten_A} \\backslash {ten_B}$."
		
	kq = A-B
	kq2 =B-A
	kq3= A | B
	kq4= A & B

	kq=str(kq)
	kq2=str(kq2)
	kq3=str(kq3)
	kq4=str(kq4)

	A, B=list(A), list(B)
	A, B=sorted(A), sorted(B)
	A, B=set(A), set(B)

	noi_dung_loigiai=f"Ta có: ${ten_A}=\\{{{A}\\}}$ và ${ten_B}=\\{{{B}\\}}$. Do đó ${ten_A} \\backslash {ten_B} =\\{{{kq}\\}}$.".replace(f"\\{{set()\\}}",f"\\emptyset")
	
	
	#Tạo các phương án
	pa_A=f"*$\\{{{kq}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_B=f"$\\{{{kq2}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_C=f"$\\{{{kq3}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	pa_D=f"$\\{{{kq4}\\}}$".replace(f"\\{{set()\\}}",f"\\emptyset").replace(f"\\{{\\emptyset\\}}",f"\\emptyset")
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án	
	
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

#[D10_C1_B3_08]. Tìm số tập hợp con của một tập hợp
def mjulk_L10_C1_B3_08():

	set_A =my_module.tao_taphop(random.randint(1,6),-10,20)

	#List kết quả
	kq = 2**(len(set_A))
	kq2 = len(set_A) + 1
	kq3= 2**(len(set_A)+1)
	kq4= len(set_A) + 3

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
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp $A=\\{{{set_A}\\}}$. Tìm số tập hợp con của tập hợp ${{A}}$. "
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

#[D10_C1_B3_09]. Tìm số tập hợp con gồm k phần tử
def mjulk_L10_C1_B3_09():
	#Tạo ngẫu nhiên tập hợp
	n=random.randint(4,6)
	k=random.randint(1,n-1)
	set_A =my_module.tao_taphop(n,-10,10)	

	#List kết quả
	kq = binomial(n, k)
	kq2 = len(set_A) + k
	kq3= 2**k
	kq4= 2**(len(set_A))

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
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp $A=\\{{{set_A}\\}}$. Tìm số tập hợp con gồm {k} phần tử của tập hợp ${{A}}$. "
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

#[D10_C1_B3_10]-TF-M2. Cho 2 tập hợp dạng liệt kê. Đúng-Sai: Giao, Hợp, Hiệu, Kiểm tra tập con
def mjulk_L10_C1_B3_10():
	#Tạo tập hợp A chứa các số nguyên từ a1 đến a2	
	a1=random.randint(-6,-4)
	a2=a1+random.randint(3,6)

	b1=random.randint(-6,-4)
	b2=b1+random.randint(3,6)

	if a1==b1 and a2==b2: a1=a1+random.randint(1,2)
	A=set(range(a1, a2))	
	B=set(range(b1, b2))	

	noi_dung = f"Cho hai tập hợp $A=\\{{{A}\\}}$ và $B=\\{{{B}\\}}$. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"

	giao = A & B 
	giao=thay_kihieu_rong(f"\\{{{str(giao)}\\}}")
	min_ab, max_ab=min(a1,b1), max(a2,b2)

	giao_false = A & B
	giao_false= giao_false.add(random.choice([min_ab-1,max_ab+1]))
	giao_false=thay_kihieu_rong(f"\\{{{str(giao_false)}\\}}")

	kq1_T=f"*$A\\cap B= {giao}$" 
	kq1_F=f"$A\\cap B= {giao_false}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$A\\cap B= {giao}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	hop= A | B	
	hop_size=len(hop)
	hop=thay_kihieu_rong(f"\\{{{str(hop)}\\}}")

	kq2_T=f"*Số phần tử của $A \\cup B$ là ${{{hop_size}}}$"
	kq2_F=f"Số phần tử của $A \\cup B$ là ${{{hop_size+random.randint(1,3)}}}$ "
	kq2=random.choice([kq2_T, kq2_F])	
	HDG=f"$A\\cup B={hop}$. Nên số phần tử của $A\\cup B$ là ${{{hop_size}}}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	A_hieu_B= A-B
	B_hieu_A = B-A	

	A_hieu_B=thay_kihieu_rong(f"\\{{{str(A_hieu_B)}\\}}")
	B_hieu_A= thay_kihieu_rong(f"\\{{{str(B_hieu_A)}\\}}")

	kq3_T=f"*$A \\backslash B = {A_hieu_B}$" 
	kq3_F=f"$A \\backslash B = {B_hieu_A}$ "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$A \\backslash B = {A_hieu_B}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	check_A_con_B = A.issubset(B)
	if check_A_con_B:
		kq4_T=f"*Tập hợp ${{A}}$ là tập hợp con của tập hợp ${{B}}$" 
		kq4_F=f"Tập hợp ${{A}}$ không là tập hợp con của tập hợp ${{B}}$"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Ta thấy mọi phần tử của ${{A}}$ đều nằm trong ${{B}}$ nên $A \\subset B$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	else:
		kq4_T=f"*Tập hợp ${{A}}$ là không là tập hợp con của tập hợp ${{B}}$" 
		kq4_F=f"Tập hợp ${{A}}$ là tập hợp con của tập hợp ${{B}}$"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"Ta thấy mọi phần tử của ${{A}}$ không nằm trong ${{B}}$ nên $A \\not\\subset B$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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

#[D10_C1_B3_11]-TF-M2. Cho 2 tập hợp dạng đặc trưng. Đúng-Sai: Giao, Hợp, Hiệu, Kiểm tra tập con
def mjulk_L10_C1_B3_11():
	#Tạo tập hợp A chứa các số nguyên từ a1 đến a2	
	a1=random.randint(-6,-4)
	a2=a1+random.randint(3,6)

	b1=random.randint(-6,-4)
	b2=b1+random.randint(3,6)

	if a1==b1 and a2==b2: a1=a1+1
	A=set(range(a1, a2))	
	B=set(range(b1, b2))	

	noi_dung = f"Cho hai tập hợp $A=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2-1}\\}}$ và $B=\\{{x\\in \\mathbb{{Z}}|{b1} \\le x \\le {b2-1}\\}}$. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"

	giao = A & B 
	giao=thay_kihieu_rong(f"\\{{{str(giao)}\\}}")
	min_ab, max_ab=min(a1,b1), max(a2,b2)

	giao_false = A & B
	giao_false= giao_false.add(random.choice([min_ab-1,max_ab+1]))
	giao_false=thay_kihieu_rong(f"\\{{{str(giao_false)}\\}}")

	kq1_T=f"*$A\\cap B= {giao}$" 
	kq1_F=f"$A\\cap B= {giao_false}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$A=\\{{{A}\\}},B=\\{{{B}\\}}\\Rightarrow A\\cap B= {giao}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	hop= A | B	
	hop_size=len(hop)
	hop=thay_kihieu_rong(f"\\{{{str(hop)}\\}}")

	kq2_T=f"*Số phần tử của $A \\cup B$ là ${{{hop_size}}}$"
	kq2_F=f"Số phần tử của $A \\cup B$ là ${{{hop_size+random.randint(1,3)}}}$ "
	kq2=random.choice([kq2_T, kq2_F])	
	HDG=f"$A=\\{{{A}\\}},B=\\{{{B}\\}}\\Rightarrow A\\cup B={hop}$.\n\n Nên số phần tử của $A\\cup B$ là ${{{hop_size}}}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	A_hieu_B= A-B
	B_hieu_A = B-A	

	A_hieu_B=thay_kihieu_rong(f"\\{{{str(A_hieu_B)}\\}}")
	B_hieu_A= thay_kihieu_rong(f"\\{{{str(B_hieu_A)}\\}}")

	kq3_T=f"*$A \\backslash B = {A_hieu_B}$" 
	kq3_F=f"$A \\backslash B = {B_hieu_A}$ "
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"$A=\\{{{A}\\}},B=\\{{{B}\\}}\\Rightarrow A \\backslash B = {A_hieu_B}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	
	if b1<=a1 and a2<=b2:
		kq4_T=f"*Tập hợp ${{A}}$ là tập hợp con của tập hợp ${{B}}$" 
		kq4_F=f"Tập hợp ${{A}}$ không là tập hợp con của tập hợp ${{B}}$"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$A=\\{{{A}\\}},B=\\{{{B}\\}}$.\n\n Ta thấy mọi phần tử của ${{A}}$ đều nằm trong ${{B}}$ nên $A \\subset B$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	else:
		kq4_T=f"*Tập hợp ${{A}}$ là không là tập hợp con của tập hợp ${{B}}$" 
		kq4_F=f"Tập hợp ${{A}}$ là tập hợp con của tập hợp ${{B}}$"
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$A=\\{{{A}\\}},B=\\{{{B}\\}}$.\n\n Ta thấy mọi phần tử của ${{A}}$ không nằm trong ${{B}}$ nên $A \\not\\subset B$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"


	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
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

#[D10_C1_B3_12]-TL-M3. Bài thực tế: Cho n(A) (trong đó có B), n(B) (trong đó có A). Tính n(A giao B).
def mjulk_L10_C1_B3_12():
	n_A_giao_B = random.randint(5,10)
	n_A=random.randint(9,16) + n_A_giao_B 
	n_B=random.randint(10,16) + n_A_giao_B 
	if n_A==n_B: n_A = n_A + random.randint(1,2)
	ten_A=["biết chơi bóng đá", "biết chơi cờ vua", "thích xem phim rạp", "thích môn Toán", "thích các môn Tự nhiên", "thích môn Toán", "thích môn Vật Lí", "thích nấu ăn", "thích nghe nhạc"]
	ten_B=["biết chơi bóng chuyền", "biết chơi cờ tướng", "thích xem ca nhạc", "thích môn Văn", "thích các môn Xã hội", "thích môn Tiếng Anh", "thích môn Hóa Học", "thích đọc sách", "thích xem phim"]
	i=random.randint(0,len(ten_A)-1)
	ten_A, ten_B = ten_A[i], ten_B[i]
	lop=f"{random.choice(["10","11", "12"])}{random.choice(["A","B"])}{random.randint(1,9)}"
	n_lop=n_A+n_B-n_A_giao_B


	noi_dung = (f"Lớp {lop} có tổng cộng ${{{n_lop}}}$ học sinh, các học sinh này đều {ten_A} hoặc {ten_B}."
	f" Có ${{{n_A}}}$ học sinh {ten_A} (trong số này có các học sinh {ten_B})"
	f" và ${{{n_B}}}$ học sinh {ten_B} (trong số này có các học sinh {ten_A})."
	f" Hỏi lớp {lop} có bao nhiêu học sinh {ten_A} và {ten_B}.")

	noi_dung_loigiai=f"Số học sinh chỉ {ten_A} và không {ten_B} là: ${n_lop}-{n_B}={n_lop-n_B}$.\n\n"\
	f"Số học sinh {ten_A} và {ten_B} là: ${n_A}-{n_lop-n_B}={n_A_giao_B}$." 
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{${{{n_A_giao_B}}}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=n_A_giao_B
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C1_B3_13]-TL-M3. Bài thực tế: Cho n(A) (trong đó có B), n(B) (trong đó có A), n(A giao B). Tính n(A hợp B).
def mjulk_L10_C1_B3_13():
	n_A_giao_B = random.randint(5,10)
	n_A=random.randint(9,16) + n_A_giao_B 
	n_B=random.randint(10,16) + n_A_giao_B 
	if n_A==n_B: n_A = n_A + random.randint(1,2)
	ten_A=["biết chơi bóng đá", "biết chơi cờ vua", "thích xem phim rạp", "thích môn Toán", "thích các môn Tự nhiên", "thích môn Toán", "thích môn Vật Lí", "thích nấu ăn", "thích nghe nhạc"]
	ten_B=["biết chơi bóng chuyền", "biết chơi cờ tướng", "thích xem ca nhạc", "thích môn Văn", "thích các môn Xã hội", "thích môn Tiếng Anh", "thích môn Hóa Học", "thích đọc sách", "thích xem phim"]
	i=random.randint(0,len(ten_A)-1)
	ten_A, ten_B = ten_A[i], ten_B[i]
	lop=f"{random.choice(["10","11", "12"])}{random.choice(["A","B"])}{random.randint(1,9)}"
	n_lop=n_A+n_B-n_A_giao_B


	noi_dung = f"Mỗi học sinh của lớp {lop} đều {ten_A} hoặc {ten_B}. Biết rằng lớp có ${{{n_A}}}$ bạn {ten_A} (trong số này có các bạn {ten_B}),"\
	f" có ${{{n_B}}}$ bạn {ten_B} (trong số này có các bạn {ten_A}) và có ${{{n_A_giao_B}}}$ bạn {ten_A} và {ten_B}. Hỏi lớp {lop} có tổng cộng bao nhiêu học sinh?"

	noi_dung_loigiai=f"Gọi ${{A}}$ là tập hợp các bạn {ten_A}, ta có: $n(A)={n_A}$.\n\n"\
	f"Gọi ${{B}}$ là tập hợp các bạn {ten_B}, ta có: $n(B)={n_B}$.\n\n"\
	f"$A\\cap B$ là tập hợp các bạn {ten_A} và {ten_B}, ta có: $n(A\\cap B)={n_A_giao_B}$.\n\n"\
	f"$C=A\\cup B$ là tập hợp tất cả các bạn của lớp {lop}, ta có: $n(C)={n_A}+{n_B}-{n_A_giao_B}={n_lop}$."
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{${{{n_lop}}}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=n_lop
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C1_B3_14]-TL-M3. Bài thực tế: Cho n(A) , n(B) , n(A giao B), n_khôngAB. Tính n(A hợp B).
def mjulk_L10_C1_B3_14():
	n_A_giao_B = random.randint(5,10)
	n_A = random.randint(9,16) + n_A_giao_B 
	n_B = random.randint(10,16) + n_A_giao_B
	n_khong = random.randint(4,8)
	if n_A==n_B: n_A = n_A + random.randint(1,2)
	ten_A=["biết chơi bóng đá", "biết chơi cờ vua", "thích xem phim rạp", "thích môn Toán", "thích các môn Tự nhiên", "thích môn Toán", "thích môn Vật Lí", "thích nấu ăn", "thích nghe nhạc"]
	ten_B=["biết chơi bóng chuyền", "biết chơi cờ tướng", "thích xem ca nhạc", "thích môn Văn", "thích các môn Xã hội", "thích môn Tiếng Anh", "thích môn Hóa Học", "thích đọc sách", "thích xem phim"]
	
	i=random.randint(0,len(ten_A)-1)
	ten_A, ten_B = ten_A[i], ten_B[i]

	if ten_A in ["biết chơi bóng đá", "biết chơi cờ vua"]:
		ten_chung="biết chơi cả hai"

	if ten_A in ["thích môn Toán", "thích môn Vật Lí"]:
		ten_chung="thích cả hai môn"

	if ten_A in ["thích các môn Tự nhiên"]:
		ten_chung="thích cả hai nhóm môn"

	if ten_A in ["thích nấu ăn", "thích nghe nhạc", "thích xem phim rạp"]:
		ten_chung="thích cả hai"

	lop=f"{random.choice(["10","11", "12"])}{random.choice(["A","B"])}{random.randint(1,9)}"
	n_lop=n_A+n_B-n_A_giao_B+n_khong


	noi_dung = f"Biết rằng lớp {lop} có ${{{n_A}}}$ bạn {ten_A} và ${{{n_B}}}$ bạn {ten_B}."\
	f" Trong số các bạn {ten_A} hoặc {ten_B} có ${{{n_A_giao_B}}}$ bạn {ten_chung}. Lớp vẫn còn ${{{n_khong}}}$ bạn không {ten_A} và không {ten_B}."\
	f" Hỏi lớp {lop} có tổng cộng bao nhiêu học sinh?"

	noi_dung_loigiai=f"Gọi ${{A}}$ là tập hợp các bạn {ten_A}, ta có: $n(A)={n_A}$.\n\n"\
	f"Gọi ${{B}}$ là tập hợp các bạn {ten_B}, ta có: $n(B)={n_B}$.\n\n"\
	f"$A\\cap B$ là tập hợp các bạn {ten_A} và {ten_B}, ta có: $n(A\\cap B)={n_A_giao_B}$.\n\n"\
	f"$A\\cup B$ là tập hợp tất cả các bạn {ten_A} hoặc {ten_B}, ta có: $n(A\\cup B)={n_A}+{n_B}-{n_A_giao_B}={n_A+n_B-n_A_giao_B}$.\n\n"\
	f"Tổng số học sinh của lớp là: ${n_A+n_B-n_A_giao_B}+{n_khong}={n_lop}$."
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{${{{n_lop}}}$}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=n_lop
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C1_B3_15]-TF-M3.  Bài thực tế: Cho n(A), n(B), n(A giao B), n_khôngAB. Xét Đ-S: Chỉ A, Chỉ B, A hoặc B, Tổng số.
def mjulk_L10_C1_B3_15():
	n_A_giao_B = random.randint(5,10)
	n_A = random.randint(9,16) + n_A_giao_B 
	n_B = random.randint(10,16) + n_A_giao_B
	n_A_hop_B=n_A+n_B-n_A_giao_B
	n_khong = random.randint(4,8)
	if n_A==n_B: n_A = n_A + random.randint(1,2)
	ten_A=["biết chơi bóng đá", "biết chơi cờ vua", "thích xem phim rạp", "thích môn Toán", "thích các môn Tự nhiên", "thích môn Toán", "thích môn Vật Lí", "thích nấu ăn", "thích nghe nhạc"]
	ten_B=["biết chơi bóng chuyền", "biết chơi cờ tướng", "thích xem ca nhạc", "thích môn Văn", "thích các môn Xã hội", "thích môn Tiếng Anh", "thích môn Hóa Học", "thích đọc sách", "thích xem phim"]
	
	i=random.randint(0,len(ten_A)-1)
	ten_A, ten_B = ten_A[i], ten_B[i]

	if ten_A in ["biết chơi bóng đá", "biết chơi cờ vua"]:
		ten_chung="biết chơi cả hai"

	if ten_A in ["thích môn Toán", "thích môn Vật Lí"]:
		ten_chung="thích cả hai môn"

	if ten_A in ["thích các môn Tự nhiên"]:
		ten_chung="thích cả hai nhóm môn"

	if ten_A in ["thích nấu ăn", "thích nghe nhạc", "thích xem phim rạp"]:
		ten_chung="thích cả hai"

	lop=f"{random.choice(["10","11", "12"])}{random.choice(["A","B"])}{random.randint(1,9)}"
	n_lop=n_A+n_B-n_A_giao_B+n_khong


	noi_dung = f"Biết rằng lớp {lop} có ${{{n_A}}}$ bạn {ten_A} và ${{{n_B}}}$ bạn {ten_B}."\
	f" Trong số các bạn {ten_A} hoặc {ten_B} có ${{{n_A_giao_B}}}$ bạn {ten_chung}. Lớp vẫn còn ${{{n_khong}}}$ bạn không {ten_A} và không {ten_B}."\
	f" Xét tính đúng-sai của các khẳng định sau."

	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*Số học sinh chỉ {ten_A} là ${{{n_A-n_A_giao_B}}}$" 
	kq1_F=f"Số học sinh chỉ {ten_A} là ${{{n_A-n_A_giao_B+random.randint(1,3)}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Số học sinh chỉ {ten_A} là: ${n_A}-{n_A_giao_B}={n_A-n_A_giao_B}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*Số học sinh chỉ {ten_B} là ${{{n_B-n_A_giao_B}}}$"
	kq2_F=f"Số học sinh chỉ {ten_B} là ${{{n_B-n_A_giao_B+random.randint(1,3)}}}$ "
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Số học sinh chỉ {ten_B} là: ${n_B}-{n_A_giao_B}={n_B-n_A_giao_B}$."
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"*Số học sinh {ten_A} hoặc {ten_B} là ${{{n_A_hop_B}}}$" 
	kq3_F=f"Số học sinh {ten_A} hoặc {ten_B} là ${{{n_A_hop_B+random.randint(1,3)}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=f"Số học sinh {ten_A} hoặc {ten_B} là: ${n_A}+{n_B}-{n_A_giao_B}={n_A_hop_B}$."
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq4_T=f"*Tổng số học sinh của lớp {lop} là ${{{n_lop}}}$"
	kq4_F=f"Tổng số học sinh của lớp {lop} là ${{{n_lop+random.randint(1,4)}}}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"Số học sinh {ten_A} hoặc {ten_B} là: ${n_A}+{n_B}-{n_A_giao_B}={n_A_hop_B}$.\n\n"\
	f"Tổng số học sinh của lớp là: ${n_A_hop_B}+{n_khong}={n_lop}$."
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

#[D10_C1_B3_16]-M2. Tìm một phép toán của 2 tập hợp liệt kê
def mjulk_L10_C1_B3_16():
	chon=random.randint(1,4)
	if chon==1:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B3_01()	
	if chon==2:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B3_02()
	if chon==3:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B3_03()
	if chon==4:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B3_04()	
	
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C1_B3_17]-M2. Cho A-đặc trưng, B-liệt kê. Xét Đ-S: Liệt kê A, Số tập hợp con, phép toán, A con X con B
def mjulk_L10_C1_B3_17():

	ten_A=["A","C","E", "M", "P"]
	ten_B=["B","D","F", "N", "Q"]
	i=random.randint(0,4)
	ten_A, ten_B=ten_A[i], ten_B[i]
	
	
	#Tạo tập hợp A chứa các số nguyên từ a1 đến a2
	a1=random.randint(-5,3)
	a2=a1+random.randint(2,5)
	A=set(range(a1, a2 + 1))

	#Tạo tập hợp A chứa các số nguyên từ b1 đến b2
	b1=a1+random.randint(1,2)
	b2=a2+random.randint(-1,3)
	B=set(range(b1, b2 + 1))
		
	noi_dung=( f"Cho hai tập hợp ${ten_A}=\\{{x\\in \\mathbb{{Z}}|{a1} \\le x \\le {a2}\\}}$ và ${ten_B}=\\{{{B}\\}}$."
		f" Xét tính đúng-sai của các khẳng định sau:"
		)

	debai_word= f"{noi_dung}\n"

	liet_ke_A=list(A)
	liet_ke_A=sorted(liet_ke_A)
	liet_ke_A=set(liet_ke_A)

	A_fasle=set(range(a1, a2))
	liet_ke_A_false=list(A_fasle)
	liet_ke_A_false=sorted(liet_ke_A_false)
	liet_ke_A_false=set(liet_ke_A_false)

	
	kq1_T=f"* ${ten_A}= \\{{ {liet_ke_A}\\}}$" 
	kq1_F=f"${ten_A}= \\{{ {liet_ke_A_false}\\}}$ "
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"${ten_A}= \\{{ {liet_ke_A}\\}}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	t=a2-a1+1
	kq2_T=f"* Số tập hợp con của tập hợp ${{{ten_A}}}$ là ${{{2**t}}}$"
	kq2_F=f"Số tập hợp con của tập hợp ${{{ten_A}}}$ là ${{{2**(t-1)}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"Số tập hợp con của tập hợp ${{{ten_A}}}$ là $2^{{{t}}}={{{2**t}}}.$"
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,3)
	giao=A&B
	liet_ke_giao=list(giao)
	liet_ke_giao=sorted(liet_ke_giao)
	liet_ke_giao=set(liet_ke_giao)

	hop=A|B
	liet_ke_hop=list(hop)
	liet_ke_hop=sorted(liet_ke_hop)
	liet_ke_hop=set(liet_ke_hop)

	hieu=A-B
	liet_ke_A_hieu_B=list(hieu)
	liet_ke_A_hieu_B=sorted(liet_ke_A_hieu_B)
	liet_ke_A_hieu_B=set(liet_ke_A_hieu_B)

	hieu=B-A
	liet_ke_B_hieu_A=list(hieu)
	liet_ke_B_hieu_A=sorted(liet_ke_B_hieu_A)
	liet_ke_B_hieu_A=set(liet_ke_B_hieu_A)


	if chon==1:
		kq3_T=f"* ${ten_A}\\cap {ten_B}=\\{{{liet_ke_giao}\\}}$" 
		kq3_F=f"${ten_A}\\cap {ten_B}=\\{{{liet_ke_hop}\\}}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${ten_A}\\cap {ten_B}=\\{{{liet_ke_giao}\\}}$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq3_T=f"* ${ten_A}\\cup {ten_B}=\\{{{liet_ke_hop}\\}}$" 
		kq3_F=f"${ten_A}\\cup {ten_B}=\\{{{liet_ke_giao}\\}}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${ten_A}\\cup {ten_B}=\\{{{liet_ke_hop}\\}}$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	if chon==3:
		if liet_ke_A_hieu_B=="set()":
			kq3_T=f"* ${ten_A}\\backslash {ten_B}=\\emptyset$"
			kq3_F=f"${ten_A}\\backslash {ten_B}=\\{{{liet_ke_giao}\\}}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"${ten_A}\\backslash {ten_B}=\\emptyset$."
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
		else:
			kq3_T=f"* ${ten_A}\\backslash {ten_B}=\\{{{liet_ke_A_hieu_B}\\}}$"
			kq3_F=f"${ten_A}\\backslash {ten_B}=\\{{{liet_ke_giao}\\}}$"
			kq3=random.choice([kq3_T, kq3_F])
			HDG=f"${ten_A}\\backslash {ten_B}=\\{{{liet_ke_A_hieu_B}\\}}$."
			loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
			if kq3==kq3_F:
				loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Tạo tập hợp A
	n_A=random.randint(2,3)
	A = set()
	B = set()
	while len(A) < n_A:
		num = random.randint(-8, 8)
		A.add(num)
		B.add(num)

	#Tạo tập hợp B	
	n_B=i+random.randint(1,2)
	while len(B) < n_B:
		num = random.randint(-8, 8)
		B.add(num)
	so_X=find_subsets_and_count(A,B)
	so_X_false=random.choice([so_X-1, so_X+1])

	kq4_T=f"* Số tập hợp ${{X}}$ để $\\{{{A}\\}} \\subset X \\subset \\{{{B}\\}}$ là ${{{so_X}}}$"
	kq4_F=f"Số tập hợp ${{X}}$ để $\\{{{A}\\}} \\subset X \\subset \\{{{B}\\}}$ là ${{{so_X_false}}}$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"Các tập hợp ${{X}}$ để $\\{{{A}\\}} \\subset X \\subset \\{{{B}\\}}$ là ${{{so_X}}}$ là:\n\n"
		f"{find_subsets(A,B)}".replace("'","").replace("[","").replace("]","").replace("(","").replace(")","")
		)
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

#[D10_C1_B3_18]-TL-M4. Bài toán thực tế liên quan 3 tập hợp (biết ít nhất 1 môn)
def mjulk_L10_C1_B3_18():
	n_A_giao_B_giao_C = random.randint(2,5)
	n_A_giao_B = n_A_giao_B_giao_C+random.randint(1,2)
	n_A_giao_C = n_A_giao_B_giao_C+random.randint(3,4)
	n_B_giao_C = n_A_giao_B_giao_C+random.randint(1,4)	

	n_A = random.randint(2,4) + n_A_giao_B + n_A_giao_C + n_A_giao_B_giao_C
	n_B = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
	n_C = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
	
	if n_A==n_B: n_A = n_A + random.randint(1,2)
	if n_C==n_B: n_C = n_C  + random.randint(1,2)

	n_lop=n_A+n_B+n_C-n_A_giao_B - n_A_giao_C - n_B_giao_C + n_A_giao_B_giao_C

	while n_lop<35 or n_lop>45:
		n_A_giao_B_giao_C = random.randint(2,5)
		n_A_giao_B = n_A_giao_B_giao_C+random.randint(1,2)
		n_A_giao_C = n_A_giao_B_giao_C+random.randint(3,4)
		n_B_giao_C = n_A_giao_B_giao_C+random.randint(1,4)		

		n_A = random.randint(2,4) + n_A_giao_B + n_A_giao_C + n_A_giao_B_giao_C
		n_B = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
		n_C = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
		
		if n_A==n_B: n_A = n_A + random.randint(1,2)
		if n_C==n_B: n_C = n_C  + random.randint(1,2)

		n_lop=n_A+n_B+n_C-n_A_giao_B - n_A_giao_C - n_B_giao_C + n_A_giao_B_giao_C

	dap_an=n_lop
	lop=f"{random.choice(["10","11", "12"])}{random.choice(["A","B"])}{random.randint(1,9)}"
	chon=random.randint(1,3)
	

	if chon==1:
		mon=["biết chơi bóng đá", "biết chơi cờ vua","biết chơi bóng chuyền", "biết chơi cờ tướng", "biết chơi cầu lông"]
		random.shuffle(mon)
		ten_A,ten_B,ten_C=mon[0:3]	

		noi_dung =(f"Lớp {lop} có ${{{n_A}}}$ bạn {ten_A}, ${{{n_B}}}$ bạn {ten_B}, ${{{n_C}}}$ bạn {ten_C},"
	f" ${{{n_A_giao_B}}}$ bạn {ten_A} và {ten_B}, ${{{n_B_giao_C}}}$ bạn {ten_B} và {ten_C},"
	f" ${{{n_A_giao_C}}}$ bạn {ten_A} và {ten_C} và ${{{n_A_giao_B_giao_C}}}$ biết chơi cả ba môn."
	f" Hỏi lớp {lop} có tất cả bao nhiêu học sinh biết ít nhất một môn thể thao?")

		noi_dung_loigiai=(
	f"Gọi A là tập hợp các bạn {ten_A}, B là tập hợp các bạn {ten_B}, C là tập hợp các bạn {ten_C}.\n\n"
	f"Ta có: $n(A)={n_A}, n(B)={n_B}, n(C)={n_C}$.\n\n"
	f"$n(A\\cap B)={n_A_giao_B}, n(A\\cap C)={n_A_giao_C}, n(B\\cap C)={n_B_giao_C}$.\n\n"
	f"$n(A\\cap B \\cap C)={n_A_giao_B_giao_C}$.\n\n"
	f"Số học sinh biết ít nhất một môn thể thao là:\n\n"
	f"$n(A\\cup B \\cup C)=n(A)+n(B)+n(C)+n(A\\cap B \\cap C)-n(A\\cap B)-n(A\\cap C)-n(B\\cap C)$\n\n"
	f"$={n_A}+{n_B}+{n_C}+{n_A_giao_B_giao_C}-{n_A_giao_B}-{n_A_giao_C}-{n_B_giao_C}={n_lop}$.\n\n"
	f"Đáp án: {dap_an}"
	)
	
	if chon==2:
		mon=["thích môn Toán", "thích môn Vật Lí", "thích môn Ngữ Văn", "thích môn Tiếng Anh", "thích môn Hóa Học", "thích môn Lịch Sử", "thích môn Địa Lí",
		"thích môn Tin học", "thích môn Sinh Học"]		
		random.shuffle(mon)
		ten_A,ten_B,ten_C=mon[0:3]

		noi_dung =(f"Lớp {lop} có ${{{n_A}}}$ bạn {ten_A}, ${{{n_B}}}$ bạn {ten_B}, ${{{n_C}}}$ bạn {ten_C},"
	f" ${{{n_A_giao_B}}}$ bạn {ten_A} và {ten_B}, ${{{n_B_giao_C}}}$ bạn {ten_B} và {ten_C},"
	f" ${{{n_A_giao_C}}}$ bạn {ten_A} và {ten_C} và ${{{n_A_giao_B_giao_C}}}$ thích cả ba môn."
	f" Hỏi lớp {lop} có tất cả bao nhiêu học sinh thích ít nhất một môn học?")

		noi_dung_loigiai=(
	f"Gọi A là tập hợp các bạn {ten_A}, B là tập hợp các bạn {ten_B}, C là tập hợp các bạn {ten_C}.\n\n"
	f"Ta có: $n(A)={n_A}, n(B)={n_B}, n(C)={n_C}$.\n\n"
	f"$n(A\\cap B)={n_A_giao_B}, n(A\\cap C)={n_A_giao_C}, n(B\\cap C)={n_B_giao_C}$.\n\n"
	f"$n(A\\cap B \\cap C)={n_A_giao_B_giao_C}$.\n\n"
	f"Số học sinh thích ít nhất một môn học là:\n\n"
	f"$n(A\\cup B \\cup C)=n(A)+n(B)+n(C)+n(A\\cap B \\cap C)-n(A\\cap B)-n(A\\cap C)-n(B\\cap C)$\n\n"
	f"$={n_A}+{n_B}+{n_C}+{n_A_giao_B_giao_C}-{n_A_giao_B}-{n_A_giao_C}-{n_B_giao_C}={n_lop}$.\n\n"
	f"Đáp án: {dap_an}"
	)

	if chon==3:
		mon=["thích xem phim rạp", "thích đọc truyện", "thích nấu ăn", "thích nghe nhạc", "thích đọc sách", "thích xem phim cổ trang", "thích đi du lịch"]
		random.shuffle(mon)
		ten_A,ten_B,ten_C=mon[0:3]

		noi_dung =(f"Lớp {lop} có ${{{n_A}}}$ bạn {ten_A}, ${{{n_B}}}$ bạn {ten_B}, ${{{n_C}}}$ bạn {ten_C},"
		f" ${{{n_A_giao_B}}}$ bạn {ten_A} và {ten_B}, ${{{n_B_giao_C}}}$ bạn {ten_B} và {ten_C},"
		f" ${{{n_A_giao_C}}}$ bạn {ten_A} và {ten_C}, ${{{n_A_giao_B_giao_C}}}$ có cả ba sở thích."
		f" Hỏi lớp {lop} có tất cả bao nhiêu học sinh có ít nhất một sở thích?")

		noi_dung_loigiai=(
	f"Gọi A là tập hợp các bạn {ten_A}, B là tập hợp các bạn {ten_B}, C là tập hợp các bạn {ten_C}.\n\n"
	f"Ta có: $n(A)={n_A}, n(B)={n_B}, n(C)={n_C}$.\n\n"
	f"$n(A\\cap B)={n_A_giao_B}, n(A\\cap C)={n_A_giao_C}, n(B\\cap C)={n_B_giao_C}$.\n\n"
	f"$n(A\\cap B \\cap C)={n_A_giao_B_giao_C}$.\n\n"
	f"Số học sinh có ít nhất một sở thích là:\n\n"
	f"$n(A\\cup B \\cup C)=n(A)+n(B)+n(C)+n(A\\cap B \\cap C)-n(A\\cap B)-n(A\\cap C)-n(B\\cap C)$\n\n"
	f"$={n_A}+{n_B}+{n_C}+{n_A_giao_B_giao_C}-{n_A_giao_B}-{n_A_giao_C}-{n_B_giao_C}={n_lop}$.\n\n"
	f"Đáp án: {dap_an}")


		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C1_B3_19]-TL-M4. Bài toán thực tế liên quan 3 tập hợp (Chỉ biết 1 môn)
def mjulk_L10_C1_B3_19():
	n_A_giao_B_giao_C = random.randint(2,5)
	n_A_giao_B = n_A_giao_B_giao_C+random.randint(1,2)
	n_A_giao_C = n_A_giao_B_giao_C+random.randint(3,4)
	n_B_giao_C = n_A_giao_B_giao_C+random.randint(1,4)	

	n_A = random.randint(2,4) + n_A_giao_B + n_A_giao_C + n_A_giao_B_giao_C
	n_B = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
	n_C = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
	
	if n_A==n_B: n_A = n_A + random.randint(1,2)
	if n_C==n_B: n_C = n_C  + random.randint(1,2)

	n_lop=n_A+n_B+n_C-n_A_giao_B - n_A_giao_C - n_B_giao_C + n_A_giao_B_giao_C

	while n_lop<35 or n_lop>45:
		n_A_giao_B_giao_C = random.randint(2,5)
		n_A_giao_B = n_A_giao_B_giao_C+random.randint(1,2)
		n_A_giao_C = n_A_giao_B_giao_C+random.randint(3,4)
		n_B_giao_C = n_A_giao_B_giao_C+random.randint(1,4)		

		n_A = random.randint(2,4) + n_A_giao_B + n_A_giao_C + n_A_giao_B_giao_C
		n_B = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
		n_C = random.randint(2,4) + n_A_giao_B + n_B_giao_C + n_A_giao_B_giao_C
		
		if n_A==n_B: n_A = n_A + random.randint(1,2)
		if n_C==n_B: n_C = n_C  + random.randint(1,2)

		n_lop=n_A+n_B+n_C-n_A_giao_B - n_A_giao_C - n_B_giao_C + n_A_giao_B_giao_C

	n_only_A=n_A - n_A_giao_B - n_A_giao_C + n_A_giao_B_giao_C
	n_only_B=n_B - n_A_giao_B - n_B_giao_C + n_A_giao_B_giao_C
	n_only_C=n_C - n_B_giao_C - n_A_giao_C + n_A_giao_B_giao_C
	dap_an=n_only_A + n_only_B + n_only_C

	
	lop=f"{random.choice(["10","11", "12"])}{random.choice(["A","B"])}{random.randint(1,9)}"
	chon=random.randint(1,3)	

	if chon==1:
		mon=["biết chơi bóng đá", "biết chơi cờ vua","biết chơi bóng chuyền", "biết chơi cờ tướng", "biết chơi cầu lông"]
		random.shuffle(mon)
		ten_A,ten_B,ten_C=mon[0:3]	

		noi_dung =(f"Lớp {lop} có ${{{n_A}}}$ bạn {ten_A}, ${{{n_B}}}$ bạn {ten_B}, ${{{n_C}}}$ bạn {ten_C},"
	f" ${{{n_A_giao_B}}}$ bạn {ten_A} và {ten_B}, ${{{n_B_giao_C}}}$ bạn {ten_B} và {ten_C},"
	f" ${{{n_A_giao_C}}}$ bạn {ten_A} và {ten_C} và ${{{n_A_giao_B_giao_C}}}$ biết chơi cả ba môn."
	f" Hỏi lớp {lop} có tất cả bao nhiêu học sinh chỉ giỏi đúng một môn thể thao trong các môn kể trên.")		

		noi_dung_loigiai=(
	f"Gọi A là tập hợp các bạn {ten_A}, B là tập hợp các bạn {ten_B}, C là tập hợp các bạn {ten_C}.\n\n"
	f"Ta có: $n(A)={n_A}, n(B)={n_B}, n(C)={n_C}$.\n\n"
	f"$n(A\\cap B)={n_A_giao_B}, n(A\\cap C)={n_A_giao_C}, n(B\\cap C)={n_B_giao_C}$.\n\n"
	f"$n(A\\cap B \\cap C)={n_A_giao_B_giao_C}$.\n\n"

	f"Số học sinh chỉ {ten_A} là: ${n_A}-{n_A_giao_B}-{n_A_giao_C}+{n_A_giao_B_giao_C}={n_only_A}$\n\n"
	f"Số học sinh chỉ {ten_B} là: ${n_B}-{n_A_giao_B}-{n_B_giao_C}+{n_A_giao_B_giao_C}={n_only_B}$\n\n"
	f"Số học sinh chỉ {ten_C} là: ${n_C}-{n_A_giao_C}-{n_B_giao_C}+{n_A_giao_B_giao_C}={n_only_C}$\n\n"

	f"Số học sinh chỉ giỏi một môn thể thao là: ${n_only_A}+{n_only_B}+{n_only_C}={dap_an}$.\n\n"

	f"Đáp án: {dap_an}"
	)
	
	if chon==2:
		mon=["thích môn Toán", "thích môn Vật Lí", "thích môn Ngữ Văn", "thích môn Tiếng Anh", "thích môn Hóa Học", "thích môn Lịch Sử", "thích môn Địa Lí",
		"thích môn Tin học", "thích môn Sinh Học"]		
		random.shuffle(mon)
		ten_A,ten_B,ten_C=mon[0:3]

		noi_dung =(f"Lớp {lop} có ${{{n_A}}}$ bạn {ten_A}, ${{{n_B}}}$ bạn {ten_B}, ${{{n_C}}}$ bạn {ten_C},"
	f" ${{{n_A_giao_B}}}$ bạn {ten_A} và {ten_B}, ${{{n_B_giao_C}}}$ bạn {ten_B} và {ten_C},"
	f" ${{{n_A_giao_C}}}$ bạn {ten_A} và {ten_C} và ${{{n_A_giao_B_giao_C}}}$ thích cả ba môn."
	f" Hỏi lớp {lop} có tất cả bao nhiêu học sinh chỉ thích một môn học trong các môn kể trên?")

		noi_dung_loigiai=(
	f"Gọi A là tập hợp các bạn {ten_A}, B là tập hợp các bạn {ten_B}, C là tập hợp các bạn {ten_C}.\n\n"
	f"Ta có: $n(A)={n_A}, n(B)={n_B}, n(C)={n_C}$.\n\n"
	f"$n(A\\cap B)={n_A_giao_B}, n(A\\cap C)={n_A_giao_C}, n(B\\cap C)={n_B_giao_C}$.\n\n"
	f"$n(A\\cap B \\cap C)={n_A_giao_B_giao_C}$.\n\n"

	f"Số học sinh chỉ {ten_A} là: ${n_A}-{n_A_giao_B}-{n_A_giao_C}+{n_A_giao_B_giao_C}={n_only_A}$\n\n"
	f"Số học sinh chỉ {ten_B} là: ${n_B}-{n_A_giao_B}-{n_B_giao_C}+{n_A_giao_B_giao_C}={n_only_B}$\n\n"
	f"Số học sinh chỉ {ten_C} là: ${n_C}-{n_A_giao_C}-{n_B_giao_C}+{n_A_giao_B_giao_C}={n_only_C}$\n\n"

	f"Số học sinh chỉ thích một môn học là: ${n_only_A}+{n_only_B}+{n_only_C}={dap_an}$.\n\n"
	)

	if chon==3:
		mon=["thích xem phim rạp", "thích đọc truyện", "thích nấu ăn", "thích nghe nhạc", "thích đọc sách", "thích xem phim cổ trang", "thích đi du lịch"]
		random.shuffle(mon)
		ten_A,ten_B,ten_C=mon[0:3]

		noi_dung =(f"Lớp {lop} có ${{{n_A}}}$ bạn {ten_A}, ${{{n_B}}}$ bạn {ten_B}, ${{{n_C}}}$ bạn {ten_C},"
		f" ${{{n_A_giao_B}}}$ bạn {ten_A} và {ten_B}, ${{{n_B_giao_C}}}$ bạn {ten_B} và {ten_C},"
		f" ${{{n_A_giao_C}}}$ bạn {ten_A} và {ten_C}, ${{{n_A_giao_B_giao_C}}}$ có cả ba sở thích."
		f" Hỏi lớp {lop} có tất cả bao nhiêu học sinh chỉ có đúng một sở thích trong các sở thích trên?")

		noi_dung_loigiai=(
	f"Gọi A là tập hợp các bạn {ten_A}, B là tập hợp các bạn {ten_B}, C là tập hợp các bạn {ten_C}.\n\n"
	f"Ta có: $n(A)={n_A}, n(B)={n_B}, n(C)={n_C}$.\n\n"
	f"$n(A\\cap B)={n_A_giao_B}, n(A\\cap C)={n_A_giao_C}, n(B\\cap C)={n_B_giao_C}$.\n\n"
	f"$n(A\\cap B \\cap C)={n_A_giao_B_giao_C}$.\n\n"

	f"Số học sinh chỉ {ten_A} là: ${n_A}-{n_A_giao_B}-{n_A_giao_C}+{n_A_giao_B_giao_C}={n_only_A}$\n\n"
	f"Số học sinh chỉ {ten_B} là: ${n_B}-{n_A_giao_B}-{n_B_giao_C}+{n_A_giao_B_giao_C}={n_only_B}$\n\n"
	f"Số học sinh chỉ {ten_C} là: ${n_C}-{n_A_giao_C}-{n_B_giao_C}+{n_A_giao_B_giao_C}={n_only_C}$\n\n"

	f"Số học sinh chỉ có đúng một sở thích: ${n_only_A}+{n_only_B}+{n_only_C}={dap_an}$.\n\n"
	f"Đáp án: {dap_an}")


		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an


#[D10_C1_B3_20]-M2. Cho n(A),n(B),n(hợp). Tìm n(giao)
def mjulk_L10_C1_B3_20():
	A,B=random.sample(["A","B","C","D","E","M","N"],2)
	giao=random.randint(7,15)
	while True:
		a=random.randint(8,15)+giao
		b=random.randint(8,20)+giao
		if a!=b:
			break
	hop=a+b-giao
	noi_dung=(
	f"Cho hai tập hợp ${{{A}}}$ và ${{{B}}}$ biết "
	f"$n({A})={a},n({B})={b}, n({A}\\cup {B})={hop}$."
	f" Tính $n({A}\\cap {B})$."
	)
 
	kq=giao
	kq_false=[a+b,
	abs(a-b),
	random.randint(b,a+b),
	hop-a,
	hop-b
	]
	kq_false=[i for i in kq_false if i!=kq]

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	noi_dung_loigiai=(
	f"$n({A}\\cap {B})=n({A})+n({B})-n({A}\\cup {B}) ={a}+{b}-{hop}={giao}$."
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

#[D10_C1_B3_21]-M2. Cho n(A),n(B),n(giao). Tìm n(hợp)
def mjulk_L10_C1_B3_21():
	A,B=random.sample(["A","B","C","D","E","M","N"],2)
	giao=random.randint(7,15)
	while True:
		a=random.randint(8,15)+giao
		b=random.randint(8,20)+giao
		if a!=b:
			break
	hop=a+b-giao
	noi_dung=(
	f"Cho hai tập hợp ${{{A}}}$ và ${{{B}}}$ biết "
	f"$n({A})={a},n({B})={b}, n({A}\\cap {B})={giao}$."
	f" Tính $n({A}\\cup {B})$."
	)
 
	kq=hop
	kq_false=[a+b,
	random.randint(b,a+b),
	giao+a,
	giao+b,
	hop+random.randint(1,5)
	]
	kq_false=[i for i in kq_false if i!=kq]

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	noi_dung_loigiai=(
	f"$n({A}\\cup {B})=n({A})+n({B})-n({A}\\cap {B}) ={a}+{b}-{giao}={hop}$."
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

#[D10_C1_B3_22]-M2. Cho n(A), n(giao), n(hợp). Tính n(B).
def mjulk_L10_C1_B3_22():
	A,B=random.sample(["A","B","C","D","E","M","N"],2)
	giao=random.randint(7,15)
	while True:
		a=random.randint(8,15)+giao
		b=random.randint(8,20)+giao
		if a!=b:
			break
	hop=a+b-giao
	noi_dung=(
	f"Cho hai tập hợp ${{{A}}}$ và ${{{B}}}$ biết "
	f"$n({A})={a},n({A}\\cap {B})={giao}, n({A}\\cup {B})={hop}$."
	f" Tính $n({B})$."
	)
 
	kq=b
	kq_false=[a+b,
	random.randint(b,a+b),
	hop-a,
	hop-b,
	hop+random.randint(1,5)
	]
	kq_false=[i for i in kq_false if i!=kq]

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

	noi_dung_loigiai=(
	f"$n({B})=n({A}\\cup {B})+n({A}\\cap {B})-n({A})={hop}+{giao}-{a}={b}$."
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



#----------------------------------------------------------------------->
#Bài 4 - Các tập hợp con của R
#[D10_C1_B4_01]. Cho kí hiệu khoảng,đoạn. Mô tả dạng tính chất đặc trưng
def mjulk_L10_C1_B4_01():
	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b=a+random.randint(1,6)
	ten_th=random.choice(["A","B","D", "M","E","F","G","H"])
	chon_dang=random.choice(["(a;b)","[a;b]","(a;b]","[a;b)"])
	if chon_dang=="(a;b)":
		tap_hop_A=f"({a};{b})"
		kq=f"\\{{ x\\in \\mathbb{{R}}| {a}<x<{b}\\}}"
		kq2=f"\\{{ x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}"
		kq3=f"\\{{ x\\in \\mathbb{{N}}| {a}\\le  x <{b}\\}}"
		kq4=f"\\{{ x\\in \\mathbb{{R}}| {a}<  x \\le {b}\\}}"
	elif chon_dang=="[a;b]":
		tap_hop_A=f"[{a};{b}]"
		kq=f"\\{{ x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}"
		kq2=f"\\{{ x\\in \\mathbb{{R}}| {a}< x < {b}\\}}"
		kq3=f"\\{{ x\\in \\mathbb{{N}}| {a}\\le x < {b}\\}}"
		kq4=f"\\{{ x\\in \\mathbb{{R}}| {a}< x \\le {b}\\}}"
	elif chon_dang=="(a;b]":
		tap_hop_A=f"({a};{b}]"
		kq=f"\\{{ x\\in \\mathbb{{R}}| {a}< x \\le {b}\\}}"
		kq2=f"\\{{ x\\in \\mathbb{{R}}| {a}< x < {b}\\}}"
		kq3=f"\\{{ x\\in \\mathbb{{N}}| {a}< x \\le {b}\\}}"
		kq4=f"\\{{ x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}"
	else: #[a;b)
		tap_hop_A=f"[{a};{b})"
		kq=f"\\{{ x\\in \\mathbb{{R}}| {a}\\le x <{b}\\}}"
		kq2=f"\\{{ x\\in \\mathbb{{R}}| {a}< x < {b}\\}}"
		kq3=f"\\{{ x\\in \\mathbb{{R}}| {a}< x \\le {b}\\}}"
		kq4=f"\\{{ x\\in \\mathbb{{N}}| {a}\\le x <{b}\\}}"


	#Tạo các phương án
	pa_A=f"*${ten_th}={{{kq}}}$"
	pa_B=f"${ten_th}={{{kq2}}}$"
	pa_C=f"${ten_th}={{{kq3}}}$"
	pa_D=f"${ten_th}={{{kq4}}}$"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp ${ten_th}={tap_hop_A}$. Tìm khẳng định đúng. "
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

#[D10_C1_B4_02]. Cho tính chất đặc trưng tìm kí hiệu khoảng đoạn
def mjulk_L10_C1_B4_02():
	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b=a+random.randint(1,10)
	ten_th=random.choice(["A","B","D", "M","E","F","G","H"])
	chon_dang=random.choice(["(a;b)","[a;b]","(a;b]","[a;b)"])
	if chon_dang=="(a;b)":
		tap_hop_A=f"\\{{ x\\in \\mathbb{{R}}| {a}<x<{b}\\}}" 
		kq=f"({a};{b})"
		kq2=f"[{a};{b})"
		kq3=f"({a};{b}]"
		kq4=f"[{a};{b}]"
	elif chon_dang=="[a;b]":
		tap_hop_A=f"\\{{ x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}" 
		kq=f"[{a};{b}]"
		kq2=f"[{a};{b})"
		kq3=f"({a};{b}]"
		kq4=f"({a};{b})"
	elif chon_dang=="(a;b]":
		tap_hop_A=f"\\{{ x\\in \\mathbb{{R}}| {a}< x \\le {b}\\}}" 
		kq=f"({a};{b}]"
		kq2=f"[{a};{b})"
		kq3=f"[{a};{b}]"
		kq4=f"({a};{b})"
	else:
		tap_hop_A=f"\\{{ x\\in \\mathbb{{R}}| {a}\\le x < {b}\\}}" 
		kq=f"[{a};{b})"
		kq2=f"({a};{b}]"
		kq3=f"[{a};{b}]"
		kq4=f"({a};{b})"	

	#Tạo các phương án
	pa_A=f"*${ten_th}={{{kq}}}$"
	pa_B=f"${ten_th}={{{kq2}}}$"
	pa_C=f"${ten_th}={{{kq3}}}$"
	pa_D=f"${ten_th}={{{kq4}}}$"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp ${ten_th}={tap_hop_A}$. Tìm khẳng định đúng. "
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

#[D10_C1_B4_03]. Tìm giao các khoảng, đoạn
def mjulk_L10_C1_B4_03():
	#Tạo ngẫu nhiên tập hợp
	a1=random.randint(-7,0)
	a2=a1 + random.randint(2,5)

	b1=a1+random.randint(1,3)
	if b1==a2:
		b1=a2 + random.randint(1,3)
	b2=b1 + random.randint(2,5)
	if b2==a2:
		b2=b2+random.randint(2,5)

	dau_a1=random.choice(["(","["])

	dau_a2=random.choice([")","]"])
	if dau_a2==")":
		dau_nguoc_a2="("
	else:
		dau_nguoc_a2="["
	dau_b1=random.choice(["(","["])
	if dau_b1=="(":
		dau_nguoc_b1=")"
	else:
		dau_nguoc_b1="]"

	dau_b2=random.choice([")","]"])

	#TH1:a1 < b1 <a2 <b2
	if a1<b1<a2<b2:
		kq=f"{dau_b1}{b1};{a2}{dau_a2}"
		kq2=f"{dau_a1}{a1};{b2}{dau_b2}"
		kq3=f"{dau_a1}{a1};{b1}{dau_nguoc_b1}"
		kq4=f"{dau_a1}{a1};{a2}{dau_a2}"

	elif a1<a2<b1<b2:
		kq=f"\\emptyset"
		kq2=f"{dau_a1}{a1};{b2}{dau_b2}"
		kq3=f"{dau_nguoc_a2}{a2};{b1}{dau_nguoc_b1}"
		kq4=f"{dau_a1}{a1};{b1}{dau_nguoc_b1}"

	else:
		kq=f"{dau_b1}{b1};{b2}{dau_b2}"
		kq2=f"{dau_b1}{b1};{a2}{dau_a2}"
		kq3=f"{dau_a1}{a1};{b2}{dau_b2}"
		kq4=f"{dau_a1}{a1};{b1}{dau_nguoc_b1}"

	#Tạo các phương án
	pa_A=f"*${{{kq}}}$"
	pa_B=f"${{{kq2}}}$"
	pa_C=f"${{{kq3}}}$"
	pa_D=f"${{{kq4}}}$"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp $A={dau_a1}{a1};{a2}{dau_a2}$ và $B={dau_b1}{b1};{b2}{dau_b2}$ . Tìm ${{A\\cap B}}$. "
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

#[D10_C1_B4_04]. Tìm hợp các khoảng, đoạn
def mjulk_L10_C1_B4_04():
	#Tạo ngẫu nhiên tập hợp
	a1=random.randint(-7,0)
	a2=a1 + random.randint(2,5)

	b1=a2-random.randint(1,5)
	if b1==a1:
		b1=a1+1
	b2=b1 + random.randint(2,5)
	if b2==a2: b2=b2+1

	dau_a1=random.choice(["(","["])
	if dau_a1==")":
		dau_nguoc_a1=")"
	else:
		dau_nguoc_a1="]"

	dau_a2=random.choice([")","]"])
	if dau_a2==")":
		dau_nguoc_a2="("
	else:
		dau_nguoc_a2="["
	dau_b1=random.choice(["(","["])
	if dau_b1=="(":
		dau_nguoc_b1=")"
	else:
		dau_nguoc_b1="]"

	dau_b2=random.choice([")","]"])

	#TH1:a1 < b1 <a2 <b2
	if a1<b1<a2<b2:
		kq=f"{dau_a1}{a1};{b2}{dau_b2}"
		kq2=f"{dau_nguoc_a2}{a2};{b2}{dau_b2}"
		kq3=f"{dau_b1}{b1};{a2}{dau_a2}"
		kq4=f"{dau_a1}{a1};{a2}{dau_a2}"

	elif a1<b1<b2<a2:
		kq=f"{dau_a1}{a1};{a2}{dau_a2}"
		kq2=f"{dau_b1}{b1};{b2}{dau_b2}"
		kq3=f"{dau_nguoc_a2}{a2};{b2}{dau_b2}"
		kq4=f"{dau_a1}{a1};{b1}{dau_nguoc_b1}"

	elif b1<a1<a2<b2:
		kq=f"{dau_b1}{b1};{b2}{dau_b2}"
		kq2=f"{dau_b1}{b1};{a2}{dau_a2}"
		kq3=f"{dau_a1}{a1};{a2}{dau_a2}"
		kq4=f"{dau_b1}{b1};{a1}{dau_nguoc_a1}"
	else:
		kq=f"{dau_b1}{b1};{a2}{dau_a2}"
		kq2=f"{dau_b1}{b1};{b2}{dau_b2}"
		kq3=f"{dau_a1}{a1};{b2}{dau_b2}"
		kq4=f"{dau_b1}{b1};{a1}{dau_nguoc_a1}"

	#Tạo các phương án
	pa_A=f"*${{{kq}}}$"
	pa_B=f"${{{kq2}}}$"
	pa_C=f"${{{kq3}}}$"
	pa_D=f"${{{kq4}}}$"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp $A={dau_a1}{a1};{a2}{dau_a2}$ và $B={dau_b1}{b1};{b2}{dau_b2}$ . Tìm ${{A\\cup B}}$. "
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

#[D10_C1_B4_05]. Tìm hiệu các khoảng, đoạn
def mjulk_L10_C1_B4_05():
	#Tạo ngẫu nhiên tập hợp
	a1=random.randint(-7,0)	
	b1=a1 + random.randint(1,5)
	a2=b1 + random.randint(1,5)
	b2=a2 + random.randint(1,5)

	dau_a1=random.choice(["(","["])

	if dau_a1==")":
		dau_nguoc_a1=")"
	else:
		dau_nguoc_a1="]"

	dau_a2=random.choice([")","]"])
	if dau_a2==")":
		dau_nguoc_a2="["
	else:
		dau_nguoc_a2="("

	dau_b1=random.choice(["(","["])
	if dau_b1=="(":
		dau_nguoc_b1="]"
	else:
		dau_nguoc_b1=")"

	dau_b2=random.choice([")","]"])

	chon=random.choice(["A\\backslash B", "B\\backslash A"])
	if chon=="A\\backslash B":
		kq=f"{dau_a1}{a1};{b1}{dau_nguoc_b1}"
		kq2=f"{dau_nguoc_a2}{a2};{b2}{dau_b2}"
		kq3=f"{dau_b1}{b1};{a2}{dau_a2}"
		kq4=f"{dau_a1}{a1};{a2}{dau_a2}"
	else:
		kq=f"{dau_nguoc_a2}{a2};{b2}{dau_b2}"
		kq2=f"{dau_a1}{a1};{b1}{dau_nguoc_b1}"
		kq3=f"{dau_b1}{b1};{a2}{dau_a2}"
		kq4=f"{dau_a1}{a1};{a2}{dau_a2}"


	#Tạo các phương án
	pa_A=f"*${{{kq}}}$"
	pa_B=f"${{{kq2}}}$"
	pa_C=f"${{{kq3}}}$"
	pa_D=f"${{{kq4}}}$"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp $A={dau_a1}{a1};{a2}{dau_a2}$ và $B={dau_b1}{b1};{b2}{dau_b2}$ . Tìm ${{{chon}}}$. "
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

#[D10_C1_B4_06]. Tìm phần bù các khoảng, đoạn
def mjulk_L10_C1_B4_06():
	#Tạo ngẫu nhiên tập hợp
	a=random.randint(-10,0)	
	b=a + random.randint(1,10)
	chon_dang=random.choice(["(a;+vc)","[a;+vc)","(-vc;a)","(a;b]","[a;b)","(a;b)","[a;b]"])
	ten_th=random.choice(["A","B","D", "M","E","F","G","H"])
	if chon_dang=="(a;+vc)":
		tap_hop_A=f"({a};+\\infty)"

		kq=f"(-\\infty;{a}]"
		kq2=f"(-\\infty;{a})"
		kq3=f"({a-random.randint(1,10)};{a})"
		kq4=f"[{a};+\\infty)"
	elif chon_dang=="[a;+vc)":
		tap_hop_A=f"[{a};+\\infty)"

		kq=f"(-\\infty;{a})"
		kq2=f"(-\\infty;{a}]"
		kq3=f"(0;{a}]"
		kq4=f"({a};+\\infty)"

	elif chon_dang=="(-vc;a)":
		tap_hop_A=f"(-\\infty;{a})"

		kq=f"[{a};+\\infty)"
		kq2=f"({a};+\\infty)"
		kq3=f"[{a};{a+random.randint(1,10)}]"
		kq4=f"(-\\infty;a]"

	elif chon_dang=="(a;b]":
		tap_hop_A=f"({a};{b}]"

		kq=f"(-\\infty;{a}]\\cup ({b};+\\infty)"
		kq2=f"(-\\infty;{a})\\cup [{b};+\\infty)"
		kq3=f"(-\\infty;{a}]\\cup [{b};+\\infty)"
		kq4=f"[{a};{b})"

	elif chon_dang=="[a;b)":
		tap_hop_A=f"[{a};{b})"

		kq=f"(-\\infty;{a})\\cup [{b};+\\infty)"
		kq2=f"(-\\infty;{a}]\\cup ({b};+\\infty)"
		kq3=f"(-\\infty;{a}]\\cup [{b};+\\infty)"
		kq4=f"({a};{b}]"

	elif chon_dang=="(a;b)":
		tap_hop_A=f"({a};{b})"
		kq=f"(-\\infty;{a}]\\cup [{b};+\\infty)"
		kq2=f"(-\\infty;{a})\\cup ({b};+\\infty)"
		kq3=f"(-\\infty;{a})\\cup [{b};+\\infty)"
		kq4=f"[{a};{b}]"

	else: #[a;b]
		tap_hop_A=f"[{a};{b}]"
		kq=f"(-\\infty;{a})\\cup ({b};+\\infty)"
		kq2=f"(-\\infty;{a})\\cup [{b};+\\infty)"
		kq3=f"(-\\infty;{a}]\\cup [{b};+\\infty)"
		kq4=f"(-\\infty;{a}]\\cup ({b};+\\infty)"


	#Tạo các phương án
	pa_A=f"*${{{kq}}}$"
	pa_B=f"${{{kq2}}}$"
	pa_C=f"${{{kq3}}}$"
	pa_D=f"${{{kq4}}}$"
	#Trộn các phương án   
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Cho tập hợp ${ten_th}={tap_hop_A}$. Tìm $C_\\mathbb{{R}}{ten_th}$. "
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
def convert_vuong_tron(st):
	if st=="[":
		return "("
	if st=="(":
		return "["
	if st==")":
		return "]"
	if st=="]":
		return ")"

def tao_dau_phep_hieu(st):
	if st=="[":
		return ")"
	if st=="(":
		return "]"
	if st==")":
		return "["
	if st=="]":
		return "("

#[D10_C1_B4_07]-TF-M2. Cho A, B là các khoảng đoạn. Xét Đ-S: A giao B, A hợp B, A\B, C_R(A)
def mjulk_L10_C1_B4_07():
	a= random.randint(-10,2)
	c= a + random.randint(1,4)
	b= c + random.randint(1,4)
	d= b + random.randint(1,4)
	A=random.choice(["A", "M", "G", "D" ])
	B=random.choice(["B", "C", "H", "E", "N" ])
	dau_a=random.choice(["[","("])
	dau_b=random.choice(["]",")"])
	dau_c=random.choice(["[","("])
	dau_d=random.choice(["]",")"])

	chuyen_dau_a=convert_vuong_tron(dau_a)
	chuyen_dau_b=convert_vuong_tron(dau_b)
	chuyen_dau_c=convert_vuong_tron(dau_c)
	chuyen_dau_d=convert_vuong_tron(dau_d)

	noi_dung = f"Cho hai tập hợp ${A}={dau_a}{a};{b}{dau_b}$ và ${B}={dau_c}{c};{d}{dau_d}$. Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	kq1_T=f"*${A} \\cap {B} = {dau_c}{c};{b}{dau_b}$" 
	kq1_F=f"${A} \\cap {B}={chuyen_dau_c}{c};{b}{chuyen_dau_b} $"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"${A} \\cap {B} = {dau_c}{c};{b}{dau_b}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq2_T=f"*${A} \\cup {B} = {dau_a}{a};{d}{dau_d}$" 
	kq2_F=f"${A} \\cup {B}= {chuyen_dau_a}{a};{d}{chuyen_dau_d}$"
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"${A} \\cup {B} = {dau_a}{a};{d}{dau_d}$"
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,2)

	if chon==1:
		kq3_T=f"*${A} \\backslash {B} = {dau_a}{a};{c}{tao_dau_phep_hieu(dau_c)}$" 
		kq3_F=f"${A} \\backslash {B} = {dau_a}{a};{d}{dau_d}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${A} \\backslash {B} = {dau_a}{a};{c}{tao_dau_phep_hieu(dau_c)}$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if dau_a=="[":
			dau_a_false="]"
		if dau_a=="(":
			dau_a_false=")"

		if dau_b=="]":
			dau_b_false="["
		if dau_b==")":
			dau_b_false="("

		kq4_T=f"*$C_\\mathbb{{R}}{A}=(-\\infty;{a}{tao_dau_phep_hieu(dau_a)} \\cup {tao_dau_phep_hieu(dau_b)}{b};+\\infty)$"
		kq4_F=f"$C_\\mathbb{{R}}{A}=(-\\infty;{a}{dau_a_false} \\cup {dau_b_false}{b};+\\infty)$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$C_\\mathbb{{R}}{A}=(-\\infty;{a}{tao_dau_phep_hieu(dau_a)} \\cup {tao_dau_phep_hieu(dau_b)}{b};+\\infty)$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq3_T=f"*${B} \\backslash {A} = {tao_dau_phep_hieu(dau_b)}{b};{d}{dau_d}$" 
		kq3_F=f"${B} \\backslash {A} = {dau_c}{c};{d}{dau_d}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"${B} \\backslash {A} = {tao_dau_phep_hieu(dau_b)}{b};{d}{dau_d}$."
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

		if dau_c=="[":
			dau_c_false="]"
		if dau_c=="(":
			dau_c_false=")"

		if dau_d=="]":
			dau_d_false="["
		if dau_d==")":
			dau_d_false="("

		kq4_T=f"*$C_\\mathbb{{R}}{B}=(-\\infty;{c}{tao_dau_phep_hieu(dau_c)} \\cup {tao_dau_phep_hieu(dau_d)}{d};+\\infty)$"
		kq4_F=f"$C_\\mathbb{{R}}{B}=(-\\infty;{c}{dau_c_false} \\cup {dau_d_false}{d};+\\infty)$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=f"$C_\\mathbb{{R}}{B}=(-\\infty;{c}{tao_dau_phep_hieu(dau_c)} \\cup {tao_dau_phep_hieu(dau_d)}{d};+\\infty)$."
		loigiai_4=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq4==kq4_F:
			loigiai_4=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if dau_a=="[":
		dau_a_false="]"
	if dau_a=="(":
		dau_a_false=")"

	if dau_b=="]":
		dau_b_false="["
	if dau_b==")":
		dau_b_false="("	

	kq4_T=f"*$C_\\mathbb{{R}}{A}=(-\\infty;{a}{tao_dau_phep_hieu(dau_a)} \\cup {tao_dau_phep_hieu(dau_b)}{b};+\\infty)$"
	kq4_F=f"$C_\\mathbb{{R}}{A}=(-\\infty;{a}{dau_a_false} \\cup {dau_b_false}{b};+\\infty)$" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=f"$C_\\mathbb{{R}}{A}=(-\\infty;{a}{tao_dau_phep_hieu(dau_a)} \\cup {tao_dau_phep_hieu(dau_b)}{b};+\\infty)$."
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


#[D10_C1_B4_08]-TL-M3. Cho A, B là các khoảng đoạn. Tìm m để A giao B có đúng 1 phần tử
def mjulk_L10_C1_B4_08():
	m=sp.symbols("m")
	t=random.randint(1,4)
	a1=random.randint(-5,3)
	a2=a1+random.randint(1,10)
	
	ten_A=random.choice(["A","M","C","E"])

	b1=random.randint(-10,5)
	b2=b1+random.randint(1,10)	
	ten_B=random.choice(["B","N","D","F"])
	chon=random.randint(1,3)	

	if chon==1:
		A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
		B=random.choice([f"({b1};{b2}]"])

		kq=f"{(b2-a1)/t:.1f}".replace(".",",")

		noi_dung = f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}={B}$. Tìm ${{m}}$ để tập hợp ${ten_A}\\cap {ten_B}$ có chung đúng một phần tử"\
		f" ( kết quả làm tròn đến hàng phần mười )."

		noi_dung_loigiai=f"Để tập hợp ${ten_A}\\cap {ten_B}$ có chung đúng một phần tử thì ${latex(t*m+a1)}={b2}\\Rightarrow m={phan_so((b2-a1)/t)}.$\n\n"\
		f"Kết quả làm tròn: $m={kq}$."
	
	if chon==2:
		A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
		B=random.choice([f"[{b1};{b2})"])

		kq=f"{(b1-a2)/t:.1f}".replace(".",",")

		noi_dung = f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}={B}$. Tìm ${{m}}$ để tập hợp ${ten_A}\\cap {ten_B}$ có chung đúng một phần tử"\
		f" ( kết quả làm tròn đến hàng phần mười )."

		noi_dung_loigiai=f"Để tập hợp ${ten_A}\\cap {ten_B}$ có chung đúng một phần tử thì ${latex(t*m+a2)}={b1}\\Rightarrow m={phan_so((b1-a2)/t)}.$\n\n"\
		f"Kết quả làm tròn: $m={kq}$."

	if chon==3:
		A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
		B=random.choice([f"({b1};{b2}]"])
		R_B=f"(-\\infty;{b1}]\\cup ({b2};+\\infty)"

		kq=f"{(b2-a1)/t:.1f}".replace(".",",")

		noi_dung = f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}={R_B}$. Tìm ${{m}}$ để tập hợp ${ten_A}\\cap C_{{\\mathbb{{R}}}}{ten_B}$ có chung đúng một phần tử"\
		f" ( kết quả làm tròn đến hàng phần mười )."

		noi_dung_loigiai=(f"Ta có: $C_{{\\mathbb{{R}}}}{ten_B}={B}$.\n\n"
		f"${ten_A}\\cap C_{{\\mathbb{{R}}}}{ten_B}= {A}\\cap {B}$ có chung đúng một phần tử thì ${latex(t*m+a1)}={b2}\\Rightarrow m={phan_so((b2-a1)/t)}.$\n\n"\
		f"Kết quả làm tròn: $m={kq}$.")

	if chon==4:
		A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
		B=random.choice([f"[{b1};{b2})"])
		R_B=f"(-\\infty;{b1})\\cup [{b2};+\\infty)"

		kq=f"{(b1-a2)/t:.1f}".replace(".",",")

		noi_dung = f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}={R_B}$. Tìm ${{m}}$ để tập hợp ${ten_A}\\cap C_{{\\mathbb{{R}}}}{ten_B}$ có chung đúng một phần tử"\
		f" ( kết quả làm tròn đến hàng phần mười )."

		noi_dung_loigiai=(f"Ta có: $C_{{\\mathbb{{R}}}}{ten_B}={B}$.\n\n"
			f" ${ten_A}\\cap C_{{\\mathbb{{R}}}}{ten_B}= {A}\\cap {B}$ có chung đúng một phần tử thì ${latex(t*m+a2)}={b1}\\Rightarrow m={phan_so((b1-a2)/t)}.$\n\n"\
		f"Kết quả làm tròn: $m={kq}$.")
	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C1_B4_09]-TL-M3. Cho A, B là các khoảng đoạn. Tìm m để A giao B khác rỗng.
def mjulk_L10_C1_B4_09():
	m,a,b=sp.symbols("m a b")
	t=random.randint(1,4)
	a1=random.randint(-5,3)
	a2=a1+random.randint(1,10)	
	ten_A=random.choice(["A","M","C","E"])

	b1=random.randint(-10,5)
	b2=b1+random.randint(1,10)	
	ten_B=random.choice(["B","G","D","F"])

	A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
	B=random.choice([f"({b1};{b2})"])
	R_B=f"(-\\infty;{b1}]\\cup [{b2};+\\infty)"

	c=random.randint(1,4)
	d=random.choice([i for i in range(-5, 6) if i!=0])

	kq=f"{c*((b1-a2)/t)+d*((b2-a1)/t):.1f}".replace(".",",")
	chon=random.randint(1,2)	
	if chon==1:
		noi_dung = f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}={B}$. Biết rằng với $a< m < b$ thì tập hợp ${ten_A}\\cap {ten_B}$ khác tập rỗng."\
		f" Tính $P={latex(c*a+d*b)}$ ( kết quả làm tròn đến hàng phần mười )."

		

		noi_dung_loigiai=(f"Để tập hợp ${ten_A}\\cap {ten_B}$ bằng rỗng thì\n\n"
		f"$\\left[ \\begin{{array}}{{l}} \n\
		{latex(t*m+a2)} \\le {b1} \\\\ \n\
		{latex(t*m+a1)} \\ge {b2}\n\
		\\end{{array}} \\right.$\n"
		f"$\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
		m \\le {phan_so((b1-a2)/t)} \\\\ \n\
		m \\ge {phan_so((b2-a1)/t)} \n\
		\\end{{array}} \\right.$\n\n"
		f"Vậy để ${ten_A}\\cap {ten_B}$ khác tập rỗng thì ${phan_so((b1-a2)/t)} < m < {phan_so((b2-a1)/t)}$.\n\n"
		f"Suy ra $a={phan_so((b1-a2)/t)}, b={phan_so((b2-a1)/t)}$.\n\n"
		f"Do đó: $P={latex(c*a+d*b)}={phan_so(c*((b1-a2)/t)+d*((b2-a1)/t))}$.\n\n"
		f"Kết quả làm tròn: $P\\approx {kq}$."
		)
	
	if chon==2:

		noi_dung = f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}={R_B}$. Biết rằng với $a< m < b$ thì tập hợp ${ten_A}\\cap C_{{\\mathbb{{R}}}}{ten_B}$ khác tập rỗng."\
		f" Tính $P={latex(c*a+d*b)}$ ( kết quả làm tròn đến hàng phần mười )."

		noi_dung_loigiai=(f"Ta có: $C_{{\\mathbb{{R}}}}{ten_B}={B}$.\n\n"
			f"${ten_A}\\cap C_{{\\mathbb{{R}}}}{ten_B}= {A}\\cap {B}$ bằng rỗng thì\n\n"
		f"$\\left[ \\begin{{array}}{{l}} \n\
		{latex(t*m+a2)} \\le {b1} \\\\ \n\
		{latex(t*m+a1)} \\ge {b2}\n\
		\\end{{array}} \\right.$\n"
		f"$\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
		m \\le {phan_so((b1-a2)/t)} \\\\ \n\
		m \\ge {phan_so((b2-a1)/t)} \n\
		\\end{{array}} \\right.$\n\n"
		f"Vậy để ${ten_A}\\cap {ten_B}$ khác tập rỗng thì ${phan_so((b1-a2)/t)} < m < {phan_so((b2-a1)/t)}$.\n\n"
		f"Suy ra $a={phan_so((b1-a2)/t)}, b={phan_so((b2-a1)/t)}$.\n\n"
		f"Do đó: $P={latex(c*a+d*b)}={phan_so(c*((b1-a2)/t)+d*((b2-a1)/t))}$.\n\n"
		f"Kết quả làm tròn: $P\\approx {kq}$."
		)
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C1_B4_10]-TL-M3. Cho A, B là các khoảng đoạn. Tìm m để A giao B là tập rỗng.
def mjulk_L10_C1_B4_10():
	m,a,b=sp.symbols("m a b")
	t=random.randint(1,4)
	a1=random.randint(-5,3)
	a2=a1+random.randint(1,10)	
	ten_A=random.choice(["A","M","C","E"])

	b1=random.randint(-10,5)
	b2=b1+random.randint(1,10)	
	ten_B=random.choice(["B","G","D","F"])

	A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
	B=random.choice([f"({b1};{b2})"])

	c=random.randint(1,4)
	d=random.choice([i for i in range(-5, 6) if i!=0])

	kq=f"{c*((b1-a2)/t)+d*((b2-a1)/t):.1f}".replace(".",",")
	chon=random.randint(1,2)
	
	if chon==1:
		noi_dung = f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}={B}$. Biết rằng với $m \\le a$ hoặc $m \\ge b$ thì tập hợp ${ten_A}\\cap {ten_B}$ là tập rỗng."\
		f" Tính $P={latex(c*a+d*b)}$ ( kết quả làm tròn đến hàng phần mười )."

		noi_dung_loigiai=(f"Để tập hợp ${ten_A}\\cap {ten_B}$ là tập rỗng thì\n\n"
		f"$\\left[ \\begin{{array}}{{l}} \n\
		{latex(t*m+a2)} \\le {b1} \\\\ \n\
		{latex(t*m+a1)} \\ge {b2}\n\
		\\end{{array}} \\right.$\n"
		f"$\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
		m \\le {phan_so((b1-a2)/t)} \\\\ \n\
		m \\ge {phan_so((b2-a1)/t)} \n\
		\\end{{array}} \\right.$\n\n"	
		f"Suy ra $a={phan_so((b1-a2)/t)}, b={phan_so((b2-a1)/t)}$.\n\n"
		f"Do đó: $P={latex(c*a+d*b)}={phan_so(c*((b1-a2)/t)+d*((b2-a1)/t))}$.\n\n"
		f"Kết quả làm tròn: $P\\approx {kq}$."
		)
	
	if chon==2:
		x=sp.symbols("x")
		k=random.choice([i for i in range(-10, 10) if i!=0])
		noi_dung = (f"Cho hai tập hợp ${ten_A}={A}$ và ${ten_B}=\\{{x\\in \\mathbb{{R}}| {b1+k}<{latex(x+k)}<{b2+k}\\}}$." 
		f" Biết rằng với $m \\le a$ hoặc $m \\ge b$ thì tập hợp ${ten_A}\\cap {ten_B}$ là tập rỗng."\
		f" Tính $P={latex(c*a+d*b)}$ ( kết quả làm tròn đến hàng phần mười ).")

		noi_dung_loigiai=(
		f"${b1+k}<{latex(x+k)}<{b2+k} \\Rightarrow {b1}<x<{b2}$. Suy ra ${ten_B}={B}$.\n\n"
		f"Để tập hợp ${ten_A}\\cap {ten_B}$ là tập rỗng thì\n\n"
		f"$\\left[ \\begin{{array}}{{l}} \n\
		{latex(t*m+a2)} \\le {b1} \\\\ \n\
		{latex(t*m+a1)} \\ge {b2}\n\
		\\end{{array}} \\right.$\n"
		f"$\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
		m \\le {phan_so((b1-a2)/t)} \\\\ \n\
		m \\ge {phan_so((b2-a1)/t)} \n\
		\\end{{array}} \\right.$\n\n"	
		f"Suy ra $a={phan_so((b1-a2)/t)}, b={phan_so((b2-a1)/t)}$.\n\n"
		f"Do đó: $P={latex(c*a+d*b)}={phan_so(c*((b1-a2)/t)+d*((b2-a1)/t))}$.\n\n"
		f"Kết quả làm tròn: $P\\approx {kq}$."
		)
	
	
			
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C1_B4_11]-TL-M3. Cho A, B là các khoảng đoạn. Tìm m để A hợp B =A.
def mjulk_L10_C1_B4_11():
	m,a,b=sp.symbols("m a b")

	t=random.randint(1,3)
	b1=random.randint(-10,5)
	a1=b1-random.randint(1,5)
	a2=a1+random.randint(10,20)
	b2=random.randint(3,20)

	ten_A=random.choice(["A","M","C","E"])
	ten_B=random.choice(["B","G","D","F"])

	chon=random.randint(1,4)
	if chon==1:
		#A=[a1;a2]
		A=random.choice([f"[{a1};{a2}]"])	
		#B1=[b1; t*m+b2], b1>a1
		B=f"[{b1};{latex(t*m+b2)}]"
	
	if chon==2:
		#A=[a1;a2]
		A=random.choice([f"({a1};{a2})"])	
		#B1=[b1; t*m+b2], b1>a1
		B=f"({b1};{latex(t*m+b2)})"

	if chon==3:
		#A=[a1;a2]
		A=random.choice([f"({a1};{a2}]"])	
		#B1=[b1; t*m+b2], b1>a1
		B=f"({b1};{latex(t*m+b2)})"

	if chon==4:
		#A=[a1;a2]
		A=random.choice([f"({a1};{a2}]"])	
		#B1=[b1; t*m+b2], b1>a1
		B=f"[{b1};{latex(t*m+b2)})"
	

	x_0=random.choice([-10*i for i in range(5,20) ])
	dem=0
	for i in range(x_0,-x_0):
		if all([i>x_0, i<=(a2-b2)/t, i>(b1-b2)/t]):
			dem+=1
	kq=dem
	taphop=random.choice([f"${ten_A}={A}$ và ${ten_B}={B}$ ", f"${ten_B}={B}$ và ${ten_A}={A}$" ])
	noi_dung = (f"Cho hai tập hợp {taphop}."
	f" Tìm số các giá trị nguyên của ${{m}}$ thuộc khoảng $({x_0};{-x_0})$ để ${ten_A} \\cup {ten_B}={ten_A}$.")


	noi_dung_loigiai=(f"Để ${ten_A} \\cup {ten_B}={ten_A}$ thì ${latex(t*m+b2)} \\le {a2}$ và  ${latex(t*m+b2)}>{b1}$\n\n"
		f"$\\Rightarrow m \\le {phan_so((a2-b2)/t)}$ và $m>{phan_so((b1-b2)/t)}$.\n\n"
		f"Suy ra: ${phan_so((b1-b2)/t)} < m \\le {phan_so((a2-b2)/t)}$.\n\n"
		f"Số các giá trị nguyên ${{m}}$ thuộc khoảng $({x_0};{-x_0})$ để là ${{{kq}}}$."
	)
	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C1_B4_12]-TL-M3. Cho A, B là các khoảng đoạn. Tìm m để A con B.
def mjulk_L10_C1_B4_12():
	m,a,b=sp.symbols("m a b")
	t=random.randint(1,4)
	a1=random.randint(-10,3)
	a2=a1+random.randint(3,7)	
	ten_A=random.choice(["A","M","C","E"])

	b1=random.randint(-20,-1)
	b2=random.randint(5,30)	
	ten_B=random.choice(["B","G","D","F"])

	A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
	B=random.choice([f"({b1};{b2})"])

	x_0=random.choice([-10*i for i in range(5,10) ])
	dem=0
	for i in range(int((b1-a1)/t)-1,int((b2-a2)/t)+1):
		if all([i>x_0,i>(b1-a1)/t, i<(b2-a2)/t]):
			dem+=1
	kq=dem

	taphop=random.choice([f"${ten_A}={A}$ và ${ten_B}={B}$ ", f"${ten_B}={B}$ và ${ten_A}={A}$" ])
	noi_dung = (f"Cho hai tập hợp {taphop}."
	f" Tìm số các giá trị nguyên của ${{m}}$ thuộc khoảng $({x_0};{-x_0})$ để ${ten_A} \\subset {ten_B}$.")
	noi_dung_loigiai=(f"Để ${A} \\subset {B}$ thì "
		f"$\\left\\{{ \\begin{{array}}{{l}} \n\
		{latex(t*m+a1)}>{b1} \\\\ \n\
		{latex(t*m+a2)}<{b2}\n\
		\\end{{array}} \\right."
		f"\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
		m>{phan_so((b1-a1)/t)} \\\\ \n\
		m<{phan_so((b2-a2)/t)}\n\
		\\end{{array}} \\right."
		f"\\Rightarrow {phan_so((b1-a1)/t)}<m<{phan_so((b2-a2)/t)}$.\n\n"
		f"Số các giá trị nguyên thuộc khoảng $({x_0};{-x_0})$ để ${phan_so((b1-a1)/t)}<m<{phan_so((b2-a2)/t)}$ là ${{{kq}}}$."
		)

	
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{kq}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	dap_an=kq
	return debai_word, loigiai_word, latex_tuluan, dap_an


#[D10_C1_B4_13]-TF-M2. Xét đúng-sai về kí hiệu khoảng, đoạn, nữa khoảng.
def mjulk_L10_C1_B4_13():

	noi_dung = f"Xét tính đúng-sai của các khẳng định sau."		
	debai_word= f"{noi_dung}\n"

	a=random.randint(-10,3)
	b=a+random.randint(3,10)
	
	kq1_T=f"* $[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le x \\le {b} \\}}$" 
	kq1_F=random.choice([
		f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x < {b} \\}}$",
		f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le x <{b} \\}}$",
		f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$" 
	 ])
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le x \\le {b} \\}}$"
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	a=random.randint(-10,3)
	b=a+random.randint(3,10)

	kq2_T=f"* $({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} < x < {b} \\}}$"
	kq2_F=random.choice([
		f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le x \\le {b} \\}}$",
		f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$",
		f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le x < {b} \\}}$"
		])
	kq2=random.choice([kq2_T, kq2_F])
	HDG=f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} < x < {b} \\}}$"
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	a=random.randint(-10,3)
	b=a+random.randint(3,10)
	chon=random.randint(1,2)
	if chon==1:
		kq3_T=f"* $({a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$" 
		kq3_F=f"$({a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le  x < {b} \\}}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$({a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"
	
	if chon==2:
		kq3_T=f"* $[{a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le  x < {b} \\}}$" 
		kq3_F=f"$[{a};{b})=\\{{x\\in \\mathbb{{R}}| {a} <  x \\le {b} \\}}$"
		kq3=random.choice([kq3_T, kq3_F])
		HDG=f"$[{a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le  x < {b} \\}}$"
		loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
		if kq3==kq3_F:
			loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	a=random.randint(-10,10)
	
	chon=random.randint(1,4)
	if chon==1:
		kq4_T=f"* $[{a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x \\ge {a} \\}}$"
		kq4_F=random.choice([
			f"$[{a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x > {a} \\}}$" ,
			f"$[{a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x \\le {a} \\}}$",
			f"$[{a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x < {a} \\}}$",
			])		
		HDG=f"$[{a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x \\ge {a} \\}}$"
	
	if chon==2:
		kq4_T=f"* $({a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x > {a} \\}}$"
		kq4_F=random.choice([
			f"$({a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x < {a} \\}}$" ,
			f"$({a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x \\le {a} \\}}$",
			f"$({a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x \\ge {a} \\}}$",
			])		
		HDG=f"$({a};+\\infty)=\\{{x\\in \\mathbb{{R}}| x > {a} \\}}$"

	if chon==3:
		kq4_T=f"* $(-\\infty;{a})=\\{{x\\in \\mathbb{{R}}| x < {a} \\}}$"
		kq4_F=random.choice([
			f"$(-\\infty;{a})=\\{{x\\in \\mathbb{{R}}| x > {a} \\}}$" ,
			f"$(-\\infty;{a})=\\{{x\\in \\mathbb{{R}}| x \\le {a} \\}}$",
			f"$(-\\infty;{a})=\\{{x\\in \\mathbb{{R}}| x \\ge {a} \\}}$",
			])

	if chon==4:
		kq4_T=f"* $(-\\infty;{a}]=\\{{x\\in \\mathbb{{R}}| x \\le {a} \\}}$"
		kq4_F=random.choice([
			f"$(-\\infty;{a}]=\\{{x\\in \\mathbb{{R}}| x > {a} \\}}$" ,
			f"$(-\\infty;{a}]=\\{{x\\in \\mathbb{{R}}| x < {a} \\}}$",
			f"$(-\\infty;{a}]=\\{{x\\in \\mathbb{{R}}| x \\ge {a} \\}}$",
			])

	kq4=random.choice([kq4_T, kq4_F])	
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

#[D10_C1_B4_14]-M3. Tìm kí hiệu khoảng, đoạn ứng với tập hợp chứa điều kiện.
def mjulk_L10_C1_B4_14():
	ten=random.choice(["A","B","C","D","E","F","G","H"])
	x=sp.symbols("x")
	m=random.choice([i for i in range(-5, 5) if i!=0])
	n=random.choice([i for i in range(-5, 5) if i!=0])
	chon=random.randint(1,4)

	if chon==1:
		#ax>b---> x>b/a
		a=random.choice([i for i in range(1, 8) if i!=0])
		b=random.choice([i for i in range(-8, 8) if i!=0])

		noi_dung=f"Cho tập hợp ${ten}=\\{{x\\in \\mathbb{{R}}| {latex(a*x+m*x+n)}>{latex(b+m*x+n)}\\}}$. Hãy viết lại tập hợp ${{{ten}}}$ bằng "\
		f"kí hiệu khoảng, đoạn, nữa khoảng."
		

		kq=f"${ten}=\\left({phan_so(b/a)};+\\infty\\right)$"
		kq2=f"${ten}=\\left[{phan_so(b/a)};+\\infty\\right)$"
		kq3=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right)$"
		kq4=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right]$"

		noi_dung_loigiai=f"${latex(a*x+m*x+n)}>{latex(b+m*x+n)} \\Rightarrow {latex(a*x)}>{b} \\Rightarrow x>{phan_so(b/a)}$. Do đó: ${ten}=\\left({phan_so(b/a)};+\\infty\\right)$."
	
	if chon==2:
		#ax>b---> x<b/a
		a=random.choice([i for i in range(-8, -1) if i!=0])
		b=random.choice([i for i in range(-8, 8) if i!=0])

		noi_dung=f"Cho tập hợp ${ten}=\\{{x\\in \\mathbb{{R}}| {latex(a*x+m*x+n)}>{latex(b+m*x+n)}\\}}$. Hãy viết lại tập hợp ${{{ten}}}$ bằng "\
		f"kí hiệu khoảng, đoạn, nữa khoảng."
		

		kq=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right)$"
		kq2=f"${ten}=\\left[{phan_so(b/a)};+\\infty\\right)$"
		kq3=f"${ten}=\\left({phan_so(b/a)};+\\infty\\right)$"
		kq4=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right]$"

		noi_dung_loigiai=f"${latex(a*x+m*x+n)}>{latex(b+m*x+n)} \\Rightarrow {latex(a*x)}>{b} \\Rightarrow x<{phan_so(b/a)}$. Do đó: ${ten}=\\left(-\\infty;{phan_so(b/a)}\\right)$."
	
	if chon==3:
		#ax>=b---> x>=b/a
		a=random.choice([i for i in range(1, 8) if i!=0])
		b=random.choice([i for i in range(-8, 8) if i!=0])

		noi_dung=f"Cho tập hợp ${ten}=\\{{x\\in \\mathbb{{R}}| {latex(a*x+m*x+n)}\\ge {latex(b+m*x+n)}\\}}$. Hãy viết lại tập hợp ${{{ten}}}$ bằng "\
		f"kí hiệu khoảng, đoạn, nữa khoảng."
		

		kq=f"${ten}=\\left[{phan_so(b/a)};+\\infty\\right)$"
		kq2=f"${ten}=\\left({phan_so(b/a)};+\\infty\\right)$"
		kq3=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right)$"
		kq4=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right]$"

		noi_dung_loigiai=f"${latex(a*x+m*x+n)} \\ge {latex(b+m*x+n)} \\Rightarrow {latex(a*x)}\\ge {b} \\Rightarrow x\\ge {phan_so(b/a)}$. Do đó: ${ten}=\\left[{phan_so(b/a)};+\\infty\\right)$."
	
	if chon==4:
		#ax>=b---> x<=b/a
		a=random.choice([i for i in range(-8, -1) if i!=0])
		b=random.choice([i for i in range(-8, 8) if i!=0])

		noi_dung=f"Cho tập hợp ${ten}=\\{{x\\in \\mathbb{{R}}| {latex(a*x+m*x+n)}\\ge {latex(b+m*x+n)}\\}}$. Hãy viết lại tập hợp ${{{ten}}}$ bằng "\
		f"kí hiệu khoảng, đoạn, nữa khoảng."
		

		kq=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right]$"
		kq2=f"${ten}=\\left[{phan_so(b/a)};+\\infty\\right)$"
		kq3=f"${ten}=\\left({phan_so(b/a)};+\\infty\\right)$"
		kq4=f"${ten}=\\left(-\\infty; {phan_so(b/a)}\\right)$"

		noi_dung_loigiai=f"${latex(a*x+m*x+n)}\\ge {latex(b+m*x+n)} \\Rightarrow {latex(a*x)} \\ge {b} \\Rightarrow x \\le {phan_so(b/a)}$. Do đó: ${ten}=\\left(-\\infty;{phan_so(b/a)}\\right]$."
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

#[D10_C1_B4_15]-TF-M3. Xét Đ-S: Kí hiệu, phép toán, Giao với N,Z,  tìm m
def mjulk_L10_C1_B4_15():

	noi_dung = f"Xét tính đúng-sai của các khẳng định sau. "		
	debai_word= f"{noi_dung}\n"
	
	a=random.randint(-10,3)
	b=a+random.randint(3,10)

	#Phương án 1

	chon=random.randint(1,4)

	if chon==1:
		kq1_T=f"* $[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le x \\le {b} \\}}$" 
		kq1_F=random.choice([
			f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x < {b} \\}}$",
			f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le x <{b} \\}}$",
			f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$" 
		 ])

		HDG=f"$[{a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le x \\le {b} \\}}$."
	
	if chon==2:
		a=random.randint(-10,3)
		b=a+random.randint(3,10)

		kq1_T=f"* $({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} < x < {b} \\}}$"
		kq1_F=random.choice([
			f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le x \\le {b} \\}}$",
			f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$",
			f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le x < {b} \\}}$"
			])
		HDG=f"$({a};{b})=\\{{x\\in \\mathbb{{R}}| {a} < x < {b} \\}}$."
	a=random.randint(-10,3)
	b=a+random.randint(3,10)

	if chon==3:
		kq1_T=f"* $({a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$" 
		kq1_F=f"$({a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} \\le  x < {b} \\}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$({a};{b}]=\\{{x\\in \\mathbb{{R}}| {a} < x \\le {b} \\}}$"

	if chon==4:
		kq1_T=f"* $[{a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le  x < {b} \\}}$" 
		kq1_F=f"$[{a};{b})=\\{{x\\in \\mathbb{{R}}| {a} <  x \\le {b} \\}}$"
		kq1=random.choice([kq1_T, kq1_F])
		HDG=f"$[{a};{b})=\\{{x\\in \\mathbb{{R}}| {a} \\le  x < {b} \\}}$."

	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phương án 2- Tìm hợp
	chon=random.randint(1,3)
	
	if chon==1:
		#Tạo ngẫu nhiên tập hợp
		a1=random.randint(-7,0)
		a2=a1 + random.randint(2,5)

		b1=a2-random.randint(1,5)
		if b1==a1:
			b1=a1+1
		b2=b1 + random.randint(2,5)
		if b2==a2: b2=b2+1

		dau_a1=random.choice(["(","["])
		if dau_a1==")":
			dau_nguoc_a1=")"
		else:
			dau_nguoc_a1="]"

		dau_a2=random.choice([")","]"])
		if dau_a2==")":
			dau_nguoc_a2="("
		else:
			dau_nguoc_a2="["
		dau_b1=random.choice(["(","["])
		if dau_b1=="(":
			dau_nguoc_b1=")"
		else:
			dau_nguoc_b1="]"

		dau_b2=random.choice([")","]"])

		#TH1:a1 < b1 <a2 <b2
		if a1<b1<a2<b2:
			kq=f"{dau_a1}{a1};{b2}{dau_b2}"
			kq_false=f"{dau_nguoc_a2}{a2};{b2}{dau_b2}"

		elif a1<b1<b2<a2:
			kq=f"{dau_a1}{a1};{a2}{dau_a2}"
			kq_false=f"{dau_b1}{b1};{b2}{dau_b2}"


		elif b1<a1<a2<b2:
			kq=f"{dau_b1}{b1};{b2}{dau_b2}"
			kq_false=f"{dau_b1}{b1};{a2}{dau_a2}"

		else:
			kq=f"{dau_b1}{b1};{a2}{dau_a2}"
			kq_false=f"{dau_b1}{b1};{b2}{dau_b2}"

		kq2_T=f"* ${dau_a1}{a1};{a2}{dau_a2} \\cup {dau_b1}{b1};{b2}{dau_b2} ={kq}$"
		kq2_F=f"${dau_a1}{a1};{a2}{dau_a2} \\cup {dau_b1}{b1};{b2}{dau_b2} ={kq_false}$"		
		HDG=f"${dau_a1}{a1};{a2}{dau_a2} \\cup {dau_b1}{b1};{b2}{dau_b2} ={kq}$."

	#Phương án 2- Tìm giao
	if chon==2:	

		a1=random.randint(-7,0)
		a2=a1 + random.randint(2,5)

		b1=a1+random.randint(1,3)
		if b1==a2:
			b1=a2 + random.randint(1,3)
		b2=b1 + random.randint(2,5)

		dau_a1=random.choice(["(","["])

		dau_a2=random.choice([")","]"])
		if dau_a2==")":
			dau_nguoc_a2="("
		else:
			dau_nguoc_a2="["
		dau_b1=random.choice(["(","["])
		if dau_b1=="(":
			dau_nguoc_b1=")"
		else:
			dau_nguoc_b1="]"

		dau_b2=random.choice([")","]"])

		#TH1:a1 < b1 <a2 <b2
		if a1<b1<a2<b2:
			kq=f"{dau_b1}{b1};{a2}{dau_a2}"
			kq_false=f"{dau_a1}{a1};{b2}{dau_b2}"

		elif a1<a2<b1<b2:
			kq=f"\\emptyset"
			kq_false=f"{dau_b1}{b1};{a2}{dau_a2}"

		else:
			kq=f"{dau_b1}{b1};{b2}{dau_b2}"
			kq_false=f"{dau_b1}{b1};{a2}{dau_a2}"

		kq2_T=f"* ${dau_a1}{a1};{a2}{dau_a2} \\cap {dau_b1}{b1};{b2}{dau_b2} ={kq}$"
		kq2_F=f"${dau_a1}{a1};{a2}{dau_a2} \\cap {dau_b1}{b1};{b2}{dau_b2} ={kq_false}$"		
		HDG=f"${dau_a1}{a1};{a2}{dau_a2} \\cap {dau_b1}{b1};{b2}{dau_b2} ={kq}$."

	#Phuowng an 2 - Tìm hiệu
	if chon==3:
		a1=random.randint(-7,0)	
		b1=a1 + random.randint(1,5)
		a2=b1 + random.randint(1,5)
		b2=a2 + random.randint(1,5)

		dau_a1=random.choice(["(","["])

		if dau_a1==")":
			dau_nguoc_a1=")"
		else:
			dau_nguoc_a1="]"

		dau_a2=random.choice([")","]"])
		if dau_a2==")":
			dau_nguoc_a2="["
		else:
			dau_nguoc_a2="("

		dau_b1=random.choice(["(","["])
		if dau_b1=="(":
			dau_nguoc_b1="]"
		else:
			dau_nguoc_b1=")"

		dau_b2=random.choice([")","]"])

		kq=f"{dau_a1}{a1};{b1}{dau_nguoc_b1}"
		kq_false=f"{dau_nguoc_a2}{a2};{b2}{dau_b2}"


		kq2_T=f"* ${dau_a1}{a1};{a2}{dau_a2} \\backslash {dau_b1}{b1};{b2}{dau_b2} ={kq}$"
		kq2_F=f"${dau_a1}{a1};{a2}{dau_a2} \\backslash {dau_b1}{b1};{b2}{dau_b2} ={kq_false}$"
		HDG=f"${dau_a1}{a1};{a2}{dau_a2} \\backslash {dau_b1}{b1};{b2}{dau_b2} ={kq}$."

	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	chon=random.randint(1,3)
	if chon==1:
		a=random.randint(-4,2)
		b=a+random.randint(3,5)
		list_nguyen=f"{list(range(a+1, b+1))}".replace("[","").replace("]","")
		list_nguyen_false=f"{list(range(a, b+1))}".replace("[","").replace("]","")

		kq3_T=f"* $({a};{b}] \\cap \\mathbb{{Z}}=\\{{{list_nguyen}\\}}$"
		kq3_F=f"$({a};{b}] \\cap \\mathbb{{Z}}=\\{{{list_nguyen_false}\\}}$"
		HDG=f"$({a};{b}] \\cap \\mathbb{{Z}}=\\{{{list_nguyen}\\}}$"


	if chon==2:
		a=random.randint(-4,2)
		b=a+random.randint(3,5)
		list_nguyen=f"{list(range(a, b))}".replace("[","").replace("]","")
		list_nguyen_false=f"{list(range(a, b+1))}".replace("[","").replace("]","")

		kq3_T=f"* $[{a};{b}) \\cap \\mathbb{{Z}}=\\{{{list_nguyen}\\}}$"
		kq3_F=f"$[{a};{b}) \\cap \\mathbb{{Z}}=\\{{{list_nguyen_false}\\}}$"
		HDG=f"$[{a};{b}) \\cap \\mathbb{{Z}}=\\{{{list_nguyen}\\}}$"

	if chon==3:
		a=random.randint(-4,2)
		b=a+random.randint(3,5)
		list_nguyen=f"{[i for i in range(a+1,b+1) if i>=0]}".replace("[","").replace("]","")
		list_nguyen_false=f"{[i for i in range(a+1,b+1) if i>=0 and i <b]}".replace("[","").replace("]","")

		kq3_T=f"* $({a};{b}] \\cap \\mathbb{{N}}=\\{{{list_nguyen}\\}}$"
		kq3_F=f"$({a};{b}] \\cap \\mathbb{{N}}=\\{{{list_nguyen_false}\\}}$"
		HDG=f"$({a};{b}] \\cap \\mathbb{{N}}=\\{{{list_nguyen}\\}}$"

	if chon==4:
		a=random.randint(-4,2)
		b=a+random.randint(3,5)
		list_nguyen=f"{[i for i in range(a,b) if i>=0 and i<b]}".replace("[","").replace("]","")
		list_nguyen_false=f"{[i for i in range(a,b+1) if i>=0 and i <=b]}".replace("[","").replace("]","")

		kq3_T=f"* $[{a};{b}) \\cap \\mathbb{{N}}=\\{{{list_nguyen}\\}}$"
		kq3_F=f"$[{a};{b}) \\cap \\mathbb{{N}}=\\{{{list_nguyen_false}\\}}$"
		HDG=f"$[{a};{b}) \\cap \\mathbb{{N}}=\\{{{list_nguyen}\\}}$"
		
	kq3=random.choice([kq3_T, kq3_F])	
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	#Phương án 4
	chon=random.randint(1,2)
	
	if chon==1:
		m,a,b=sp.symbols("m a b")
		t=random.randint(1,4)
		a1=random.randint(-10,3)
		a2=a1+random.randint(3,7)	
		ten_A=random.choice(["A","M","C","E"])

		b1=random.randint(-20,-1)
		b2=random.randint(5,30)	
		ten_B=random.choice(["B","G","D","F"])

		A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
		B=random.choice([f"({b1};{b2})"])

		x_0=random.choice([-10*i for i in range(5,10) ])
		dem=0
		for i in range(int((b1-a1)/t)-1,int((b2-a2)/t)+1):
			if all([i>x_0,i>(b1-a1)/t, i<(b2-a2)/t]):
				dem+=1
		kq=dem

		taphop=random.choice([f"${ten_A}={A}$ và ${ten_B}={B}$ ", f"${ten_B}={B}$ và ${ten_A}={A}$" ])
		kq4_T=f"* ${A} \\subset {B}$ khi ${phan_so((b1-a1)/t)}<m<{phan_so((b2-a2)/t)}$"
		kq4_F=f" ${A} \\subset {B}$ khi ${phan_so((b1-a1-1)/t)}<m<{phan_so((b2-a2+1)/t)}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Để ${A} \\subset {B}$ thì "
			f"$\\left\\{{ \\begin{{array}}{{l}} \n\
			{latex(t*m+a1)}>{b1} \\\\ \n\
			{latex(t*m+a2)}<{b2}\n\
			\\end{{array}} \\right."
			f"\\Rightarrow \\left\\{{ \\begin{{array}}{{l}} \n\
			m>{phan_so((b1-a1)/t)} \\\\ \n\
			m<{phan_so((b2-a2)/t)}\n\
			\\end{{array}} \\right."
			f"\\Rightarrow {phan_so((b1-a1)/t)}<m<{phan_so((b2-a2)/t)}$.\n\n")	

	
	if chon==2:
	
		m,a,b=sp.symbols("m a b")
		t=random.randint(1,4)
		a1=random.randint(-5,3)
		a2=a1+random.randint(1,10)	
		ten_A=random.choice(["A","M","C","E"])

		b1=random.randint(-10,5)
		b2=b1+random.randint(1,10)	
		ten_B=random.choice(["B","G","D","F"])

		A=f"[{latex(t*m+a1)};{latex(t*m+a2)}]"
		B=random.choice([f"({b1};{b2})"])
		R_B=f"(-\\infty;{b1}]\\cup [{b2};+\\infty)"

		c=random.randint(1,4)
		d=random.choice([i for i in range(-5, 6) if i!=0])
		
		kq4_T=f"* ${A}\\cap {B} \\ne \\emptyset$ khi ${phan_so((b1-a2)/t)} < m < {phan_so((b2-a1)/t)}$"
		kq4_F=f"${A}\\cap {B} \\ne \\emptyset$ khi ${phan_so((b1-a2-1)/t)} < m < {phan_so((b2-a1+1)/t)}$" 
		kq4=random.choice([kq4_T, kq4_F])
		HDG=(f"Để tập hợp ${ten_A}\\cap {ten_B}$ bằng rỗng thì\n\n"
			f"$\\left[ \\begin{{array}}{{l}} \n\
			{latex(t*m+a2)} \\le {b1} \\\\ \n\
			{latex(t*m+a1)} \\ge {b2}\n\
			\\end{{array}} \\right.$\n"
			f"$\\Rightarrow \\left[ \\begin{{array}}{{l}} \n\
			m \\le {phan_so((b1-a2)/t)} \\\\ \n\
			m \\ge {phan_so((b2-a1)/t)} \n\
			\\end{{array}} \\right.$\n\n"
			f"Vậy để ${ten_A}\\cap {ten_B}$ khác tập rỗng thì ${phan_so((b1-a2)/t)} < m < {phan_so((b2-a1)/t)}$.\n\n"
			)
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

#[D10_C1_B4_16]-M2. Tìm giao (hoặc hợp, hiệu, phần bù) các tập con của R
def mjulk_L10_C1_B4_16():
	chon=random.randint(1,4)
	#Tìm giao
	if chon==1:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_03()

	#Tìm hợp	
	if chon==2:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_04()

	#Tìm hiệu	
	if chon==3:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_05()

	#Tìm phần bù	
	if chon==4:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_06()	
	
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C1_B4_17]-TL-M2. Bài toán tìm m để thỏa mãn phép toán liên quan khoảng đoạn
def mjulk_L10_C1_B4_17():
	chon=random.randint(1,6)
	if chon==1:
		debai_word,loigiai_word,latex_tuluan,dap_an=mjulk_L10_C1_B4_08()

	if chon==2:
		debai_word,loigiai_word,latex_tuluan,dap_an=mjulk_L10_C1_B4_09()

	if chon==3:
		debai_word,loigiai_word,latex_tuluan,dap_an=mjulk_L10_C1_B4_09()

	if chon==4:
		debai_word,loigiai_word,latex_tuluan,dap_an=mjulk_L10_C1_B4_10()

	if chon==5:
		debai_word,loigiai_word,latex_tuluan,dap_an=mjulk_L10_C1_B4_11()

	if chon==6:
		debai_word,loigiai_word,latex_tuluan,dap_an=mjulk_L10_C1_B4_12()
	
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C1_B4_18]-TL-M2. Tìm số phần tử là số nguyên của một phép toán khoảng đoạn
def mjulk_L10_C1_B4_18():
	A=random.choice(["A", "M", "G", "D" ])
	B=random.choice(["B", "C", "H", "E", "N" ])

	a1=random.randint(-9,5)
	b1=a1+random.randint(2,5)
	a2=b1+random.randint(7,15)
	b2=a2+random.randint(3,5)

	chon=random.randint(1,9)
	
	if chon==1:
		noi_dung = (
		f"Cho hai tập hợp ${A}=[{a1};{a2})$ và ${B}=({b1};{b2}]$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\cap {B}$.\n\n"
		)

		dap_an=a2-b1-1

		noi_dung_loigiai=(
		f"${A}\\cap {B}=({b1};{a2})$.\n\n"
		f"Các phần tử là số nguyên là: ${b1+1};{b1+2};...;{a2-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\cap {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}"	)
	
	if chon==2:
		noi_dung = (
		f"Cho hai tập hợp ${A}=({a1};{a2})$ và ${B}=[{b1};{b2}]$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\cap {B}$.\n\n"
		)
		dap_an=a2-b1

		noi_dung_loigiai=(
		f"${A}\\cap {B}=[{b1};{a2})$.\n\n"
		f"Các phần tử là số nguyên là: ${b1};{b1+1};...;{a2-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\cap {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}"	)

	if chon==3:
		noi_dung = (
		f"Cho hai tập hợp ${A}=[{a1};{a2})$ và ${B}=[{b1};{b2})$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\cap {B}$.\n\n"
		)
		dap_an=a2-b1

		noi_dung_loigiai=(
		f"${A}\\cap {B}=[{b1};{a2})$.\n\n"
		f"Các phần tử là số nguyên là: ${b1};{b1+1};...;{a2-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\cap {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}"	)
	

	if chon==4:
		noi_dung = (
		f"Cho hai tập hợp ${A}=[{a1};{a2})$ và ${B}=[{b1};{b2})$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\cup {B}$.\n\n"
		)
		dap_an=b2-a1

		noi_dung_loigiai=(
		f"${A}\\cup {B}=[{a1};{b2})$.\n\n"
		f"Các phần tử là số nguyên là: ${a1};{a1+1};...;{b2-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\cap {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}"	)
	

	if chon==5:
		noi_dung = (
		f"Cho hai tập hợp ${A}=[{a1};{a2})$ và ${B}=({b1};{b2}]$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\cup {B}$.\n\n"
		)
		dap_an=b2-a1+1

		noi_dung_loigiai=(
		f"${A}\\cup {B}=[{a1};{b2}]$.\n\n"
		f"Các phần tử là số nguyên là: ${a1};{a1+1};...;{b2}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\cap {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}"	)
	

	if chon==6:
		noi_dung = (
		f"Cho hai tập hợp ${A}=({a1};{a2})$ và ${B}=({b1};{b2})$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\cup {B}$.\n\n"
		)
		dap_an=b2-a1-1

		noi_dung_loigiai=(
		f"${A}\\cup {B}=({a1};{b2})$.\n\n"
		f"Các phần tử là số nguyên là: ${a1+1};{a1+2};...;{b2-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\cap {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}")

	if chon==7:
		noi_dung = (
		f"Cho hai tập hợp ${A}=({a1};{a2}]$ và ${B}=[{b1};{b2})$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\cup {B}$.\n\n"
		)
		dap_an=b2-a1-1

		noi_dung_loigiai=(
		f"${A}\\cup {B}=({a1};{b2})$.\n\n"
		f"Các phần tử là số nguyên là: ${a1+1};{a1+2};...;{b2-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\cap {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}")

	a1=random.randint(-9,5)
	b1=a1+random.randint(6,10)
	a2=b1+random.randint(7,15)
	b2=a2+random.randint(5,10)
	

	if chon==8:
		noi_dung = (
		f"Cho hai tập hợp ${A}=({a1};{a2}]$ và ${B}=[{b1};{b2})$. Tìm số phần tử là số nguyên thuộc tập hợp ${A}\\backslash {B}$.\n\n"
		)
		dap_an=b1-a1-1

		noi_dung_loigiai=(
		f"${A}\\backslash {B}=({a1};{b1})$.\n\n"
		f"Các phần tử là số nguyên là: ${a1+1};{a1+2};...;{b1-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\backslash {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}")
	

	if chon==9:
		noi_dung = (
		f"Cho hai tập hợp ${A}=({a1};{a2}]$ và ${B}=[{b1};{b2})$. Tìm số phần tử là số nguyên thuộc tập hợp ${B}\\backslash {A}$.\n\n"
		)
		dap_an=b2-a2-1

		noi_dung_loigiai=(
		f"${A}\\backslash {B}=({a2};{b2})$.\n\n"
		f"Các phần tử là số nguyên là: ${a2+1};{a2+2};...;{b2-1}$.\n\n"
		f"Số phần tử là số nguyên của tập hợp ${A}\\backslash {B}$ là {dap_an}.\n\n"
		f"Đáp án: {dap_an}")

	
	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=f"Lời giải:\n {noi_dung_loigiai} \n"


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C1_B4_19]-M2. Tìm giao hai khoảng dạng {x in R| a<x<b}
def mjulk_L10_C1_B4_19():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)

	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}$."
		f"  Tập hợp ${A}\\cap {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}$."
		f"  Tập hợp ${A}\\cap {B}$ là")])
	

	kq=f"${A}\\cap {B}=({c};{b})$"
	kq_false=[
	f"${A}\\cap {B}=({a};{b})$",
	f"${A}\\cap {B}=({a};{d})$",
	f"${A}\\cap {B}=({c};{d})$",
	f"${A}\\cap {B}=({a};{c})$",
	f"${A}\\cap {B}=({b};{d})$",
	f"${A}\\cap {B}=({c};{b}]$",
	f"${A}\\cap {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}=({a};{b})$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}=({c};{d})$.\n\n"
	f"${A}\\cap {B}=({c};{b})$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_20]-M2. Tìm hợp hai khoảng dạng {x in R| a<x<b}
def mjulk_L10_C1_B4_20():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)
	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}$."
		f"  Tập hợp ${A}\\cup {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}$."
		f"  Tập hợp ${A}\\cup {B}$ là")])
	

	kq=f"${A}\\cup {B}=({a};{d})$"
	kq_false=[
	f"${A}\\cup {B}=({a};{b})$",
	f"${A}\\cup {B}=[{a};{d}]$",
	f"${A}\\cup {B}=({c};{d})$",
	f"${A}\\cup {B}=({a};{c})$",
	f"${A}\\cup {B}=({b};{d})$",
	f"${A}\\cup {B}=({c};{b}]$",
	f"${A}\\cup {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}=({a};{b})$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}=({c};{d})$.\n\n"
	f"${A}\\cup {B}=({a};{d})$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_21]-M2. Tìm hiêu hai khoảng dạng {x in R| a<x<b}
def mjulk_L10_C1_B4_21():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)
	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}$."
		f"  Tập hợp ${A}\\backslash {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}$."
		f"  Tập hợp ${A}\\backslash {B}$ là")])
	

	kq=f"${A}\\backslash {B}=({a};{c}]$"
	kq_false=[
	f"${A}\\backslash {B}=[{a};{c}]$",
	f"${A}\\backslash {B}=({a};{c})$",
	f"${A}\\backslash {B}=({a};{b})$",
	f"${A}\\backslash {B}=[{a};{d}]$",
	f"${A}\\backslash {B}=({c};{d})$",	
	f"${A}\\backslash {B}=({b};{d})$",
	f"${A}\\backslash {B}=({c};{b}]$",
	f"${A}\\backslash {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}<x<{b}\\}}=({a};{b})$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c}<x<{d}\\}}=({c};{d})$.\n\n"
	f"${A}\\backslash {B}=({a};{c}]$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_22]-M2. Tìm giao hai đoạn dạng {x in R| a<=x<=b}
def mjulk_L10_C1_B4_22():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)

	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a} \\le x\\le {b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}\\le x \\le {d}\\}}$."
		f"  Tập hợp ${A}\\cap {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c} \\le x \\le{d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}$."
		f"  Tập hợp ${A}\\cap {B}$ là")])
	

	kq=f"${A}\\cap {B}=[{c};{b}]$"
	kq_false=[
	f"${A}\\cap {B}=[{a};{b}]$",
	f"${A}\\cap {B}=[{a};{d}]$",
	f"${A}\\cap {B}=[{c};{d}]$",
	f"${A}\\cap {B}=[{a};{c}]$",
	f"${A}\\cap {B}=[{b};{d})$",
	f"${A}\\cap {B}=({c};{b}]$",
	f"${A}\\cap {B}=({c};{b})$",
	f"${A}\\cap {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x\\le {b}\\}}=[{a};{b}]$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c} \\le x\\le {d}\\}}=[{c};{d}]$.\n\n"
	f"${A}\\cap {B}=[{c};{b}]$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_23]-M2. Tìm hợp hai đoạn dạng {x in R| a<=x<=b}
def mjulk_L10_C1_B4_23():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)
	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a} \\le x \\le {b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}\\le x \\le{d}\\}}$."
		f"  Tập hợp ${A}\\cup {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c}\\le x \\le {d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}$."
		f"  Tập hợp ${A}\\cup {B}$ là")])
	

	kq=f"${A}\\cup {B}=[{a};{d}]$"
	kq_false=[
	f"${A}\\cup {B}=[{a};{b}]$",
	f"${A}\\cup {B}=({a};{d})$",
	f"${A}\\cup {B}=[{c};{d}]$",
	f"${A}\\cup {B}=[{a};{c}]$",
	f"${A}\\cup {B}=({b};{d})$",
	f"${A}\\cup {B}=({c};{b}]$",
	f"${A}\\cup {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}=[{a};{b}]$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c}\\le x \\le {d}\\}}=[{c};{d}]$.\n\n"
	f"${A}\\cup {B}=[{a};{d}]$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_24]-M2. Tìm hiệu hai đoạn dạng {x in R| a<=x<=b}
def mjulk_L10_C1_B4_24():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)
	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c} \\le x \\le  {d}\\}}$."
		f"  Tập hợp ${A}\\backslash {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c} \\le x \\le  {d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}$."
		f"  Tập hợp ${A}\\backslash {B}$ là")])
	

	kq=f"${A}\\backslash {B}=[{a};{c})$"
	kq_false=[
	f"${A}\\backslash {B}=[{a};{c}]$",
	f"${A}\\backslash {B}=({a};{c})$",
	f"${A}\\backslash {B}=({a};{b})$",
	f"${A}\\backslash {B}=[{a};{d}]$",
	f"${A}\\backslash {B}=({c};{d})$",	
	f"${A}\\backslash {B}=({b};{d})$",
	f"${A}\\backslash {B}=({c};{b}]$",
	f"${A}\\backslash {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x \\le {b}\\}}=[{a};{b}]$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c}\\le x \\le {d}\\}}=[{c};{d}]$.\n\n"
	f"${A}\\backslash {B}=[{a};{c})$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_25]-M2. Tìm giao nữa khoảng dạng {x in R| a<=x<b}
def mjulk_L10_C1_B4_25():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)

	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a} \\le x < {b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}< x \\le {d}\\}}$."
		f"  Tập hợp ${A}\\cap {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c} < x \\le {d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x < {b}\\}}$."
		f"  Tập hợp ${A}\\cap {B}$ là")])
	

	kq=f"${A}\\cap {B}=({c};{b})$"
	kq_false=[
	f"${A}\\cap {B}=[{a};{b}]$",
	f"${A}\\cap {B}=[{a};{d}]$",
	f"${A}\\cap {B}=[{c};{d}]$",
	f"${A}\\cap {B}=[{a};{c}]$",
	f"${A}\\cap {B}=[{b};{d})$",
	f"${A}\\cap {B}=({c};{b}]$",
	f"${A}\\cap {B}=({c};{b}]$",
	f"${A}\\cap {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x < {b}\\}}=[{a};{b})$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c} < x \\le {d}\\}}=({c};{d}]$.\n\n"
	f"${A}\\cap {B}=({c};{b})$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_26]-M2. Tìm hợp nữa khoảng dạng {x in R| a<=x<b}
def mjulk_L10_C1_B4_26():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)

	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a} \\le x < {b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}< x \\le {d}\\}}$."
		f"  Tập hợp ${A}\\cup {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c} < x \\le {d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x < {b}\\}}$."
		f"  Tập hợp ${A}\\cup {B}$ là")])
	

	kq=f"${A}\\cup {B}=[{a};{d}]$"
	kq_false=[
	f"${A}\\cup {B}=[{a};{b}]$",
	f"${A}\\cup {B}=[{a};{d})$",
	f"${A}\\cup {B}=[{c};{d}]$",
	f"${A}\\cup {B}=[{a};{c}]$",
	f"${A}\\cup {B}=[{b};{d})$",
	f"${A}\\cup {B}=({c};{b}]$",
	f"${A}\\cup {B}=({c};{b}]$",
	f"${A}\\cup {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x < {b}\\}}=[{a};{b})$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c} < x \\le {d}\\}}=({c};{d}]$.\n\n"
	f"${A}\\cup {B}=[{a};{d}]$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_27]-M2. Tìm hiệu nữa khoảng dạng {x in R| a<=x<b}
def mjulk_L10_C1_B4_27():
	while True:
		a,b,c,d=[random.randint(-10,10) for i in range(4)]
		if a<c<b<d:
			break
	A,B=random.sample(["A","B","C","D","E","F","M","N"],2)

	
	noi_dung=random.choice([
		(f"Cho hai tập hợp ${A}=\\{{x\\in \\mathbb{{R}}| {a} \\le x < {b}\\}}$"
		f" và ${B}=\\{{x\\in \\mathbb{{R}}| {c}< x \\le {d}\\}}$."
		f"  Tập hợp ${A}\\backslash {B}$ là"),

		(f"Cho hai tập hợp ${B}=\\{{x\\in \\mathbb{{R}}| {c} < x \\le {d}\\}}$"
		f" và ${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x < {b}\\}}$."
		f"  Tập hợp ${A}\\backslash {B}$ là")])
	

	kq=f"${A}\\backslash {B}=[{a};{c}]$"
	kq_false=[
	f"${A}\\backslash {B}=[{a};{b}]$",
	f"${A}\\backslash {B}=[{a};{d})$",
	f"${A}\\backslash {B}=[{c};{d}]$",
	f"${A}\\backslash {B}=[{a};{c})$",
	f"${A}\\backslash {B}=[{b};{d})$",
	f"${A}\\backslash {B}=({c};{b}]$",
	f"${A}\\backslash {B}=({c};{b}]$",
	f"${A}\\backslash {B}=[{c};{b})$",
	]	

	noi_dung_loigiai=(
	f"${A}=\\{{x\\in \\mathbb{{R}}| {a}\\le x < {b}\\}}=[{a};{b})$.\n\n"
	f"${B}=\\{{x\\in \\mathbb{{R}}| {c} < x \\le {d}\\}}=({c};{d}]$.\n\n"
	f"${A}\\backslash {B}=[{a};{c}]$.")

	random.shuffle(kq_false)
	kq2,kq3,kq4=kq_false[0:3]

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

#[D10_C1_B4_28]-M2. Tìm giao các khoảng, đoạn, nữa khoảng dạng {x in R| ...x...}
def mjulk_L10_C1_B4_28():
	chon=random.randint(1,3)
	if chon==1:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_19()
	
	if chon==2:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_22()

	if chon==3:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_25()
	
	
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C1_B4_29]-M2. Tìm hợp các khoảng, đoạn, nữa khoảng dạng {x in R| ...x...}
def mjulk_L10_C1_B4_29():
	chon=random.randint(1,3)
	if chon==1:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_20()
	
	if chon==2:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_23()

	if chon==3:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_26()
	
	
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C1_B4_30]-M2. Tìm hiệu các khoảng, đoạn, nữa khoảng dạng {x in R| ...x...}
def mjulk_L10_C1_B4_30():
	chon=random.randint(1,3)
	if chon==1:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_21()
	
	if chon==2:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_24()

	if chon==3:
		debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an=mjulk_L10_C1_B4_27()
	
	
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D10_C1_B4_31]-SA-M2. Tìm số phần tử nguyên của A∩B∩C.
def mjulk_L10_C1_B4_31():
	while True:
		a,b,c,d,e,f=[random.randint(-30,30) for i in range(6)]
		if a<c<e<b<d<f and b-e>5:
			break
	A,B,C =random.sample(["A","B","C","D","E","F","G","H"], 3)

	noi_dung = (
	f"Cho các tập hợp ${A}=[{a};{b}], {B}=({c};{d})$ và ${C}=[{e};{f})$."
	f" Tìm số phần tử là số nguyên của tập hợp ${A}\\cap {B}\\cap {C}$."
	)
	dap_an=b-e

	noi_dung_loigiai=(
	f"${A}\\cap {B}\\cap {C}=[{e};{b})$.\n\n"
	f" Số phần tử là số nguyên của tập hợp ${A}\\cap {B}\\cap {C}$ là: ${{{dap_an}}}$."
	)

		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C1_B4_32]-SA-M2. Tìm số phần tử nguyên của A∪B∪C.
def mjulk_L10_C1_B4_32():
	while True:
		a,b,c,d,e,f=[random.randint(-30,30) for i in range(6)]
		if a<c<e<b<d<f and f-a>10:
			break
	A,B,C =random.sample(["A","B","C","D","E","F","G","H"], 3)

	noi_dung = (
	f"Cho các tập hợp ${A}=[{a};{b}], {B}=({c};{d})$ và ${C}=[{e};{f})$."
	f" Tìm số phần tử là số nguyên của tập hợp ${A}\\cup {B}\\cup {C}$."
	)
	dap_an=f-a

	noi_dung_loigiai=(
	f"${A}\\cap {B}\\cap {C}=[{a};{f})$.\n\n"
	f" Số phần tử là số nguyên của tập hợp ${A}\\cup {B}\\cup {C}$ là: ${{{dap_an}}}$."
	)

		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C1_B4_33]-SA-M2. Tìm số phần tử nguyên của (A∩B)\C.
def mjulk_L10_C1_B4_33():
	while True:
		a,b,c,d,e,f=[random.randint(-30,30) for i in range(6)]
		if a<c<e<b<d<f and e-c-1>5:
			break
	A,B,C =random.sample(["A","B","C","D","E","F","G","H"], 3)

	noi_dung = (
	f"Cho các tập hợp ${A}=[{a};{b}], {B}=({c};{d})$ và ${C}=[{e};{f})$."
	f" Tìm số phần tử là số nguyên của tập hợp $({A}\\cap {B})\\backslash {C}$."
	)
	dap_an=e-c-1

	noi_dung_loigiai=(
	f"${A}\\cap {B}=({c};{b}]$.\n\n"
	f"$({A}\\cap {B})\\backslash {C}=({c};{b}]\\backslash [{e};{f})=({c};{e})$.\n\n"
	f" Số phần tử là số nguyên của tập hợp $({A}\\cap {B})\\backslash {C}$ là: ${{{dap_an}}}$."
	)

		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an