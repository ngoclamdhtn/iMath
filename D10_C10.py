import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
#Trả về dạng phân số 
def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m
def gcd(a,b):
	while b!=0:
		tam=b		
		b= a%b
		a=tam		
	return a

def xu_li_heso_1(a):
    if a==0 or a==1:
        heso=""
    elif a==-1:
        heso="-" 
    else:
        heso=a 
    return heso

def show_num(a):
	if a==0:
		t=""
	else:
		t=a
	return t

def show_num_with_variable(b,st):
 	if b>0:
 		t=f"+{b}{st}"
 	if  b==0:
 		t=f""
 	if b<0:
 		t=f"{b}{st}" 	 		
 	if b==1:
 		t=f"+{st}"
 	if b==-1:
 		t=f"-{st}"
 	return t

def show_ptts(a,b):
	if a!=0:
		if b>0:
	 		t=f"{a}+{b}t"
		if  b==0:
	 		t=f"{a}"
		if b<0:
	 		t=f"{a}{b}t" 	 		
		if b==1:
	 		t=f"{a}+t"
		if b==-1:
	 		t=f"{a}-t"
	else:
		if b>0:
	 		t=f"{b}t"
		if  b==0:
	 		t=f"0"
		if b<0:
	 		t=f"{b}t" 	 		
		if b==1:
	 		t=f"t"
		if b==-1:
			t=f"t"
	return t
#Trả về dấu và giá trị số
def show_dau_value(a):
    dau=f"+{a}"
    if a<0:
        dau=f"{a}"
    return dau

#Trả về véctơ pháp tuyến từ véctơ chỉ phương
def tim_vtpt_tu_vtcp(a,b):
		if a!=0 and b!=0:
			t=[b,-a,-b,a]
			i=random.choice([1,2])
			if i==1:
				a1=t[0]
				b1=t[1]
			else:
				a1=t[2]
				b1=t[3]
		k = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		if a==0 and b!=0:			
			a1=random.choice([k,b])
			b1=0

		if a!=0 and b==0:	
			a1=0
			b1=random.choice([k,a])
		return a1,b1

#Trả về phép cộng với ngoặc đơn
def show_tong(a,b):
    if b>0:
        ketqua=f"{a}+{b}"
    else:
        ketqua=f"{a}+({b})"
    return ketqua

def show_tich(a,b):
    if a>=0 and b>=0:
        ketqua=f"{a}.{b}"
    if a>0 and b<0:
        ketqua=f"{a}.({b})"
    if a<0 and b>=0:
        ketqua=f"({a}).{b}"
    if a<0 and b<0:
        ketqua=f"({a}).({b})"
    if a==0 and b<0:
        ketqua=f"{a}.({b})"
    if a==0 and b>=0:
        ketqua=f"{a}.{b}"    
    return ketqua

#Trả về phép trừ với ngoặc đơn
def show_hieu(a,b):
    if b>0:
        ketqua=f"{a}-{b}"
    else:
        ketqua=f"{a}-({b})"
    return ketqua

#Trả về dấu của hệ số a
def tao_dau(a):
    if a==0 or a<0:
        dau=f""
    else:
        dau=f"+"
    return dau
#Trả về dấu ngoặc bao lấy hệ số a
def tao_ngoac(a):
    if a<0:
        dau=f"({a})"
    else:
        dau=f"{a}"
    return dau
#.replace("-+","-").replace("--","+").replace("+-","-")
def thay_dau_congtru(st):
	ketqua=st.replace("-+","-").replace("--","+").replace("+-","-").replace("++","+").replace("+ +","+").replace("+ -","-").replace("- -","+").replace("- +","-")
	return ketqua
def thay_conic(st):
	ketqua=st.replace("=1x","=x").replace("=-1x","=-x")
	return ketqua

#Bài 0 - Tọa độ véctơ

#[D10_CX_B0_01]. Cho hai điểm. Tìm tọa độ véctơ 
def gghik_L10_CX_B0_01():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,-1)
	b2=random.randint(-10,-1)
	diem_A=random.choice(["A","M", "N", "E","G"])
	diem_B=random.choice(["B","C", "D", "F","H"])
	vto_AB=f"\\overrightarrow{{{diem_A}{diem_B}}}"

	if b1==b2 and b1==0:
		b1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if b1==a1:
		b1=a1+random.randint(1,4)

	kq=f"({b1-a1};{b2-a2})"
	kq2=f"({a1-b1};{a2-b2})"
	kq3=f"({a1+b1};{a2+b2})"
	kq4=f"({latex(my_module.hien_phan_so((a1+b1)/2))};{latex(my_module.hien_phan_so((a2+b2)/2))})"
		#Tạo các phương án
	pa_A= f"*${{{vto_AB}={kq}}}$"
	pa_B= f"${{{vto_AB}={kq2}}}$"
	pa_C= f"${{{vto_AB}={kq3}}}$"
	pa_D= f"${{{vto_AB}={kq4}}}$"

	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai điểm ${diem_A}({a1};{a2})$ và ${diem_B}({b1};{b2})$. Tìm tọa độ véctơ ${vto_AB}$.\n"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	dap_an=my_module.tra_ve_dap_an(list_PA)
	

	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	noi_dung_loigiai=f"${vto_AB}=({b1-a1};{b2-a2})$."
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

#[D10_CX_B0_02]. Cho hai véctơ. Tìm tọa độ véctơ tổng.
def gghik_L10_CX_B0_02():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,-1)
	b2=random.randint(-10,-1)
	vt_A=random.choice(["a","u", "m", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	if b1==b2 and b1==0:
		b1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if b1==a1:
		b1=a1+random.randint(1,4)

	kq=f"({a1+b1};{a2+b2})"
	kq2=f"({a1+a2};{b1+b2})"
	kq3=f"({b1-a1};{b2-a2})"	
	kq4=f"({a1*b1};{a2*b2})"

	#Tạo các phương án
	pa_A= f"*${{{vt_A}+{vt_B}= {kq}}}$"
	pa_B= f"${{{vt_A}+{vt_B}={kq2}}}$"
	pa_C= f"${{{vt_A}+{vt_B}={kq3}}}$"
	pa_D= f"${{{vt_A}+{vt_B}={kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_A}=({a1};{a2})$ và ${vt_B}=({b1};{b2})$. Tìm tọa độ véctơ ${{{vt_A}+{vt_B}}}$."	

	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	noi_dung_loigiai=f"${{{vt_A}+{vt_B}}}=({a1+b1};{a2+b2})$."
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

#[D10_CX_B0_03]. Cho hai véctơ. Tìm tọa độ véctơ hiệu.
def gghik_L10_CX_B0_03():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,-1)
	b2=random.randint(-10,-1)
	vt_A=random.choice(["a","u", "m", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	if b1==b2 and b1==0:
		b1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if b1==a1:
		b1=a1+random.randint(1,4)

	kq=f"({a1-b1};{a2-b2})"
	kq2=f"({a1+b1};{a2+b2})"
	kq3=f"({b1-a1};{b2-a2})"	
	kq4=f"({a1-b2};{a2-b1})"

	#Tạo các phương án
	pa_A= f"*${{{vt_A}-{vt_B}= {kq}}}$"
	pa_B= f"${{{vt_A}-{vt_B}={kq2}}}$"
	pa_C= f"${{{vt_A}-{vt_B}={kq3}}}$"
	pa_D= f"${{{vt_A}-{vt_B}={kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án

	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_A}=({a1};{a2})$ và ${vt_B}=({b1};{b2})$. Tìm tọa độ véctơ ${{{vt_A}-{vt_B}}}$."

	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	noi_dung_loigiai=f"${{{vt_A}-{vt_B}= {kq}}}$."
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

#[D10_CX_B0_04]. Cho hai véctơ tính tích vô hướng.
def gghik_L10_CX_B0_04():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,10)
	b2=random.randint(-10,10)
	vt_A=random.choice(["a","u", "m", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	if b1==b2 and b1==0:
		b1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if b1==a1:
		b1=a1+random.randint(1,4)

	kq=a1*b1+a2*b2
	kq2=a1*b2+a2*b1
	if kq2==kq:
		kq2=kq+random.randint(1,5)
	kq3=(a1+b1)*(a2+b2)	
	kq4=a1*a2+b1*b2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*${{{vt_A}.{vt_B}= {kq}}}$"
	pa_B= f"${{{vt_A}.{vt_B}={kq2}}}$"
	pa_C= f"${{{vt_A}.{vt_B}={kq3}}}$"
	pa_D= f"${{{vt_A}.{vt_B}={kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_A}=({a1};{a2})$ và ${vt_B}=({b1};{b2})$. Tính tích vô hướng ${{{vt_A}.{vt_B}}}$."

	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	noi_dung_loigiai=f"${{{vt_A}.{vt_B}= {kq}}}$."
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

#[D10_CX_B0_05]. Cho véctơ. Tính độ dài véctơ.
def gghik_L10_CX_B0_05():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if abs(a1)==abs(a2):
		a2=a1+random.randint(2,5)
	vt_A=random.choice(["a","u", "m", "d", "b","c", "v", "w"])
	vt_A=f"\\overrightarrow{{{vt_A}}}"


	kq=(sqrt(a1**2+a2**2))
	kq2=a1**2+a2**2
	kq3=(sqrt(abs(a1)+abs(a2)))
	kq4=(sqrt(abs(a2-a1)))

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]


	#Tạo các phương án
	pa_A= f"*${{|{vt_A}|= {latex(kq)}}}$"
	pa_B= f"${{|{vt_A}|={kq2}}}$"
	pa_C= f"${{|{vt_A}|={latex(kq3)}}}$"
	pa_D= f"${{|{vt_A}|={latex(kq4)}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho véctơ ${vt_A}=({a1};{a2})$. Tính độ dài của véctơ ${{{vt_A}}}$."

	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	noi_dung_loigiai=f"${{|{vt_A}|= {latex(kq)}}}$."
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

#[D10_CX_B0_06]. Cho hai điểm. Tìm độ dài đoạn thẳng.
def gghik_L10_CX_B0_06():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,-1)
	b2=random.randint(-10,-1)
	diem_A=random.choice(["A","M", "N", "E","G"])
	diem_B=random.choice(["B","C", "D", "F","H"])
	vto_AB=f"\\overrightarrow{{{diem_A}{diem_B}}}"

	if b1==b2 and b1==0:
		b1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if b1==a1:
		b1=a1+random.randint(1,4)

	kq=sqrt((a1-b1)**2+(a2-b2)**2)
	kq2=abs(a1-b1) + abs(a2-b2)
	kq3=abs(a1+b1) + abs(a2+b2)
	kq4=(a1-b1)**2+(a2-b2)**2
		#Tạo các phương án
	pa_A= f"*${{{diem_A}{diem_B}={latex(kq)}}}$"
	pa_B= f"${{{diem_A}{diem_B}={kq2}}}$"
	pa_C= f"${{{diem_A}{diem_B}={kq3}}}$"
	pa_D= f"${{{diem_A}{diem_B}={kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  # Xáo trộn danh sách đáp án
	noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai điểm ${diem_A}({a1};{a2})$ và ${diem_B}({b1};{b2})$. Tìm độ dài đoạn thẳng ${{{diem_A}{diem_B}}}$."
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	debai= f"{noi_dung}\n"	   
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"	
	
	noi_dung_loigiai=f"${{{diem_A}{diem_B}={latex(kq)}}}$."
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

#[D10_CX_B0_07]-M1. Cho hai điểm. Tìm tọa độ trung điểm.
def gghik_L10_CX_B0_07():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,-1)
	b2=random.randint(-10,-1)
	if b1==b2 and b1==0:
		b1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if b1==a1:
		b1=a1+random.randint(1,4)
	diem_A=random.choice(["A","M", "N", "E","G"])
	diem_B=random.choice(["B","C", "D", "F","H"])

	kq=f"\\left({phan_so((a1+b1)/2)};{phan_so((a2+b2)/2)} \\right)"
	kq2=f"\\left({phan_so((a1-b1)/2)};{phan_so((a2-b2)/2)} \\right)"
	kq3=f"\\left({phan_so(a1+b1)};{phan_so(a2+b2)} \\right)"
	kq4=f"\\left({phan_so((a1+a2)/2)};{phan_so((b1+b2)/2)} \\right)"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai điểm ${diem_A}({a1};{a2})$ và ${diem_B}({b1};{b2})$. Tìm tọa độ trung điểm của đoạn thẳng ${{{diem_A}{diem_B}}}$."
	noi_dung_loigiai=f" Tọa độ trung điểm của đoạn thẳng ${{{diem_A}{diem_B}}}$ là:"\
	f" $\\left(\\dfrac{{x_{diem_A}+x_{diem_B}}}{{2}};\\dfrac{{y_{diem_A}+y_{diem_B}}}{{2}}\\right)={kq}$.\n"\
					

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

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

#[D10_CX_B0_08]-M1. Cho tam giác. Tìm tọa độ trọng tâm.
def gghik_L10_CX_B0_08():  
	x=sp.symbols("x")
	y=sp.symbols("y")
	
	diem_A=random.choice(["A","M","D"])
	diem_B=random.choice(["B","N","E"])
	diem_C=random.choice(["C","P","F"])

	a_1=random.randint(-6,6)
	a_2=random.randint(-7,7)

	b_1=a_1+random.randint(1,4)
	b_2=a_2+ random.randint(1,4)

	c_1=a_1-random.randint(1,5)
	c_2=a_2-random.randint(1,4)

	t_1=(c_2-a_2)*(b_1-a_1)-(b_2-a_2)*(c_1-a_1)
	if t_1==0:c_1=c_1+random.randint(1,3)	

	
	kq=f"\\left({latex(my_module.hien_phan_so((a_1+b_1+c_1)/3))};{phan_so((a_2+b_2+c_2)/3)} \\right)"
	kq2=f"\\left({phan_so((a_1+b_1+c_1)/2)};{phan_so((a_2+b_2+c_2)/2)} \\right)"
	kq3=f"\\left({phan_so(a_1+b_1+c_1)};{phan_so(a_2+b_2+c_2)} \\right)"
	kq4=f"\\left({phan_so((a_1+b_1+c_1)/4)};{phan_so((a_2+b_2+c_2)/4)} \\right)"
	ABC=f"{diem_A}{diem_B}{diem_C}"

	noi_dung=f"Trong mặt phẳng ${{Oxy}}$, cho tam giác ${{{diem_A}{diem_B}{diem_C}}}$ có ${diem_A}({a_1};{a_2}),{diem_B}({b_1};{b_2})$ và ${{{diem_C}({c_1};{c_2})}}$."\
			 f" Tìm tọa độ trọng tâm của tam giác ${{{diem_A}{diem_B}{diem_C}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f" Tọa độ trọng tâm của tam giác ${{{diem_A}{diem_B}{diem_C}}}$ là:"\
	f" $\\left(\\dfrac{{x_{diem_A}+x_{diem_B}+x_{diem_C}}}{{3}};\\dfrac{{y_{diem_A}+y_{diem_B}+y_{diem_C}}}{{3}}\\right)={kq}$.\n"

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

#[D10_CX_B0_09]-M2. Cho hai điểm A,B. Tìm tọa độ C để AC nhận B làm trung điểm.
def gghik_L10_CX_B0_09():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a2==a1: a2=a1+random.randint(1,5)

	b1=random.randint(-10,10)
	b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	if b1==a1:
		b1=a1+random.randint(1,4)
	diem_A=random.choice(["A","M", "E", "G"])
	diem_B=random.choice(["B","N", "F", "H"])
	diem_C=random.choice(["C","P", "D", "K"])

	c1,c2=2*b1-a1, 2*b2-a2

	kq=f"{diem_C}({c1};{c2})"
	kq2=f"{diem_C}({-c1};{-c2})"
	kq3=f"{diem_C}({c1+random.randint(1,5)};{c2-random.randint(1,5)})"
	kq4=f"{diem_C}({c1-random.randint(6,10)};{c2+random.randint(6,10)})"

	
	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai điểm ${diem_A}({a1};{a2})$ và ${diem_B}({b1};{b2})$."\
	f" Tìm tọa độ điểm ${{{diem_C}}}$ sao cho ${{{diem_A}}}$ và ${{{diem_C}}}$ đối xứng nhau qua ${{{diem_B}}}$."
	noi_dung_loigiai=f"Đoạn thẳng ${{{diem_A}{diem_C}}}$ nhận điểm {diem_B} làm trung điểm nên:\n\n"\
	f" $x_{diem_C}=2x_{diem_B}-x_{diem_A}={show_tich(2,b1)}-{tao_ngoac(a1)}={c1}$.\n\n"\
	f" $y_{diem_C}=2y_{diem_B}-y_{diem_A}={show_tich(2,b2)}-{tao_ngoac(a2)}={c2}$.\n\n"\
	f"Vậy ${{{diem_C}=({c1};{c2})}}$."				


    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n" \

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


#[D10_CX_B0_10]-M2. Cho ba điểm A,B,G. Tìm tọa độ C để ABC nhận G làm trọng tâm.
def gghik_L10_CX_B0_10():
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a2==a1: a2=a1+random.randint(1,5)
	
	b1=random.randint(-10,10)
	b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	if b1==a1:
		b1=a1+random.randint(1,4)

	g1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	g2=random.randint(-10,10)
	

	diem_A=random.choice(["A","M", "E"])
	diem_B=random.choice(["B","N", "F"])
	diem_C=random.choice(["C","D", "K"])
	diem_G=random.choice(["G","H", "I"])

	c1,c2=3*g1-a1-b1, 3*g2-a2-b2

	kq=f"{diem_C}({c1};{c2})"
	kq2=f"{diem_C}({-c1};{-c2})"
	kq3=f"{diem_C}({c1+random.randint(1,5)};{c2-random.randint(1,5)})"
	kq4=f"{diem_C}({c1-random.randint(6,10)};{c2+random.randint(6,10)})"
	ABC=f"{diem_A}{diem_B}{diem_C}"

	
	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho ba điểm ${diem_A}({a1};{a2}), {diem_B}({b1};{b2})$ và ${{{diem_G}({g1};{g2})}}$."\
	f" Tìm tọa độ điểm ${{{diem_C}}}$ sao cho tam giác ${{{diem_A}{diem_B}{diem_C}}}$ nhận ${{{diem_G}({g1};{g2})}}$ làm trọng tâm."
	noi_dung_loigiai=f"Tam giác ${{{diem_A}{diem_B}{diem_C}}}$ nhận ${{{diem_G}({g1};{g2})}}$ làm trọng tâm nên:\n"\
	f" $x_{diem_C}=3x_{diem_G}-x_{diem_A}-x_{diem_B}={show_tich(3,g1)}-{tao_ngoac(a1)}-{tao_ngoac(b1)}={c1}$.\n"\
	f" $y_{diem_C}=3y_{diem_G}-y_{diem_A}-y_{diem_B}={show_tich(3,g2)}-{tao_ngoac(a1)}-{tao_ngoac(b2)}={c2}$.\n"\
	f"Vậy ${{{diem_C}=({c1};{c2})}}$."				

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n" \

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

#[D10_CX_B0_11]. Cho hai véctơ. Tìm m để 2 vectơ cùng phương.
def gghik_L10_CX_B0_11():
	m=sp.symbols("m")
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,10)
	c1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])

	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b2=random.randint(-10,10)
	c2 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a1==a2: a1=a1+random.randint(1,4)
	if a1==a2 and b1==b2: a2=a2+random.randint(1,4)
	
	vt_A=random.choice(["a","u", "n", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	# Giải hệ phương trình	
	eq1 = Eq((a1*m + b1)*c2,(a2*m + b2)*c1)
	tap_nghiem=solve(eq1,m)
	x_0=tap_nghiem[0]

	eq2 = Eq((a1*m + b1),(a2*m + b1))
	tap_nghiem=solve(eq2,m)
	x_2=tap_nghiem[0]

	eq3 = Eq(a1*m + b1+c1,a2*m + b2+c2)
	tap_nghiem=solve(eq3,m)
	x_3=tap_nghiem[0]

	chon=random.randint(1,2)
	if chon==1:		
		noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_A}=({latex(a1*m+b1)};{c1})$ và ${vt_B}=({latex(a2*m+b2)};{c2})$."\
		f" Tìm các giá trị của ${{{m}}}$ để vectơ ${{{vt_A}}}$ và vectơ ${{{vt_B}}}$ cùng phương."
		noi_dung_loigiai=f"${vt_A}=({latex(a1*m+b1)};{c1})$ và ${vt_B}=({latex(a2*m+b2)};{c2})$ cùng phương\n\n"\
	f"$ \\Leftrightarrow {latex((a1*m+b1)/(a2*m+b2))}=\\dfrac{{{c1}}}{{{c2}}} \\Leftrightarrow m={latex(x_0)}$."

	if chon==2:	
		noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_A}=({c1};{latex(a1*m+b1)})$ và ${vt_B}=({c2};{latex(a2*m+b2)})$."\
		f" Tìm các giá trị của ${{{m}}}$ để vectơ ${{{vt_A}}}$ và vectơ ${{{vt_B}}}$ cùng phương."
		noi_dung_loigiai=f"${vt_A}=({c1};{latex(a1*m+b1)})$ và ${vt_B}=({c2};{latex(a2*m+b2)})$ cùng phương\n\n"\
	f"$ \\Leftrightarrow \\dfrac{{{c1}}}{{{c2}}}={latex((a1*m+b1)/(a2*m+b2))} \\Leftrightarrow m={latex(x_0)}$."
	
	kq=x_0
	kq2=x_2
	kq3=x_3
	kq4=x_0+random.randint(1,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*$ {{m={latex(kq)}}}$"
	pa_B= f"$ {{m={latex(kq2)}}}$"
	pa_C= f"$ {{m={latex(kq3)}}}$"
	pa_D= f"$ {{m={latex(kq4)}}}$"

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_CX_B0_12]. Cho hai véctơ. Tìm m để 2 vectơ vuông góc.
def gghik_L10_CX_B0_12():
	m=sp.symbols("m")
	a1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b1=random.randint(-10,10)
	c1 = random.choice([random.randint(-10, -1), random.randint(1, 10)])

	a2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b2=random.randint(-10,10)
	c2 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a1==a2: a1=a1+random.randint(1,4)
	if a1==a2 and b1==b2: a2=a2+random.randint(1,4)
	if a1*c1+a2*c2==0: b2=b2+random.randint(1,4)
	
	vt_A=random.choice(["a","u", "n", "d"])
	vt_B=random.choice(["b","c", "v", "w"])

	vt_A=f"\\overrightarrow{{{vt_A}}}"
	vt_B=f"\\overrightarrow{{{vt_B}}}"

	# Giải hệ phương trình	
	eq1 = Eq((a1*m + b1)*c1+(a2*m + b2)*c2,0)
	tap_nghiem=solve(eq1,m)
	x_0=tap_nghiem[0]

	eq2 = Eq((a1*m + b1),(a2*m + b1))
	tap_nghiem=solve(eq2,m)
	x_2=tap_nghiem[0]

	eq3 = Eq(a1*m + b1+c1,a2*m + b2+c2)
	tap_nghiem=solve(eq3,m)
	x_3=tap_nghiem[0]

	chon=random.randint(1,2)
	if chon==1:		
		noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_A}=({latex(a1*m+b1)};{latex(a2*m+b2)})$ và ${vt_B}=({c1};{c2})$."\
		f" Tìm các giá trị của ${{{m}}}$ để vectơ ${{{vt_A}}}$ và vectơ ${{{vt_B}}}$ vuông góc."
		noi_dung_loigiai=f"${vt_A}=({latex(a1*m+b1)};{latex(a2*m+b2)})$ và ${vt_B}=({c1};{c2})$ vuông góc\n\n"\
	f"$ \\Leftrightarrow ({latex(a1*m+b1)}).{tao_ngoac(c1)}+({latex(a2*m+b2)}).{tao_ngoac(c2)}=0 \\Leftrightarrow m={latex(x_0)}$."

	if chon==2:	
		noi_dung= f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai véctơ ${vt_A}=({c1};{c2})$ và ${vt_B}=({latex(a1*m+b1)};{latex(a2*m+b2)})$."\
		f" Tìm các giá trị của ${{{m}}}$ để vectơ ${{{vt_A}}}$ và vectơ ${{{vt_B}}}$ vuông góc."
		noi_dung_loigiai=f" ${vt_A}=({c1};{c2})$ và ${vt_B}=({latex(a1*m+b1)};{latex(a2*m+b2)})$ vuông góc\n\n"\
	f"$ \\Leftrightarrow {tao_ngoac(c1)}.({latex(a1*m+b1)})+{tao_ngoac(c2)}.({latex(a2*m+b2)})=0\\Leftrightarrow m={latex(x_0)}$."
	
	kq=x_0
	kq2=x_2
	kq3=x_3
	kq4=x_0+random.randint(1,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	#Tạo các phương án
	pa_A= f"*$ {{m={latex(kq)}}}$"
	pa_B= f"$ {{m={latex(kq2)}}}$"
	pa_C= f"$ {{m={latex(kq3)}}}$"
	pa_D= f"$ {{m={latex(kq4)}}}$"

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\choice\n"\
		f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\\\\ \n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"
	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_CX_B0_13]. Tìm A thuộc Ox cách B một khoảng cho trước.
def gghik_L10_CX_B0_13():
	x=sp.symbols("x")
	x_0=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	r=sqrt((a-x_0)**2+b**2)
	diem_A=random.choice(["A","M", "P", "C"])
	diem_B=random.choice(["B","N", "Q","D"])
	kq= f"${diem_A}({x_0};0)$"
	kq2=f"${diem_A}(0;{x_0})$"
	kq3=f"${diem_A}({x_0+random.randint(1,5)};0)$"
	kq4=f"${diem_A}(0;{x_0+random.randint(1,5)})$"

	#Tạo các phương án
	pa_A= f"{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  
	dap_an=my_module.tra_ve_dap_an(list_PA)
	noi_dung=f"Tìm tọa độ điểm ${diem_A} \\in Ox$ sao cho ${diem_A}{diem_B}={latex(r)}$ với ${diem_B}({a};{b})$."
	noi_dung_loigiai=f"Gọi $A(x;0)\\in Ox$. Khi đó: $AB={latex(sqrt((a-x)**2+b**2))}={latex(r)}$"\
	f"$\\Leftrightarrow {latex((a-x)**2+b**2)}={r**2}\\Rightarrow x={x_0}$."

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
			
#Bài 1 - Phương trình đường thẳng
#10.1.1. Véctơ chỉ phương, véctơ pháp tuyến

#[D10_CX_B1_01]-M1. Cho véctơ pháp tuyến tìm véctơ chỉ phương và ngược lại
def gghik_L10_CX_B1_01():   
	#Tạo bậc ngẫu nhiên
	ten_vtn=random.choice(["véctơ pháp tuyến","véctơ chỉ phương"])
	if ten_vtn=="véctơ pháp tuyến":
		vecto_n="\\overrightarrow{{n}}"
		ten_vtu="véctơ chỉ phương"
		vecto_u="\\overrightarrow{{u}}"		
	else:
		vecto_n="\\overrightarrow{{u}}"
		ten_vtu="véctơ pháp tuyến"
		vecto_u="\\overrightarrow{{n}}"		
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a==-b:
		b=a+random.randint(1,4)
	if a!=0 and b!=0:
		kq=random.choice([f"{vecto_u}=({b};{-a})", f"{vecto_u}=({-b};{a})"])
		kq2=f"{vecto_u}=({-b};{-a})"
		kq3=f"{vecto_u}=({-a};{-b})"
		kq4=f"{vecto_u}=({b};{a})"
	if a==0 and b!=0:
		k = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		kq=f"{vecto_u}=({k};0)"
		kq2=f"{vecto_u}=(0;{k})"
		kq3=f"{vecto_u}=({b};{k})"
		kq4=f"{vecto_u}=({-b};{-k})"
	if a!=0 and b==0:
		k = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		kq=f"{vecto_u}=(0;{k})"
		kq2=f"{vecto_u}=({k};0)"
		kq3=f"{vecto_u}=({a};{k})"
		kq4=f"{vecto_u}=({-a};{-k})"		

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}$ có một {ten_vtn} là ${vecto_n}({a};{b})$."\
			 f"Véctơ nào sau đây là một {ten_vtu} của đường thẳng ${{d}}$?"
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Đường thẳng ${{d}}$ có {ten_vtn} là ${vecto_n}=(a;b)$ thì có {ten_vtu} là ${vecto_u}=(b;-a)$ hoặc ${vecto_u}=(-b;a)$.\n "\
					f"Do đó dường thẳng ${{d}}$ có {ten_vtu} là : ${kq}$.\n"
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

#[D10_CX_B1_02]-M2. Đọc véctơ pháp tuyến(véctơ chỉ phương) từ phương trình tổng quát
def gghik_L10_CX_B1_02():   
	#Tạo bậc ngẫu nhiên
	ten_vt=random.choice(["véctơ pháp tuyến","véctơ chỉ phương"])
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	if a==b: b=b+random.randint(1,5)
	if a==-b: b=b+random.randint(1,5)
	c=random.randint(-10,10)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a==b or a==-b: a=a+random.randint(1,3)
	x=sp.symbols("x")
	y=sp.symbols("y")
	f=a*x+b*y+c
	k = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if ten_vt=="véctơ pháp tuyến":
		vecto="\\overrightarrow{{n}}"		
		if a!=0 and b!=0:
			kq=random.choice([f"{vecto}=({a};{b})", f"{vecto}=({-a};{-b})"])	
			kq2=f"{vecto}=({-b};{-a})"
			kq3=f"{vecto}=({-a};{b})"
			kq4=f"{vecto}=({b};{a})"
		if a==0 and b!=0:
			kq=random.choice([f"{vecto}=(0;{k})", f"{vecto}=(0;{b})"])
			kq2=f"{vecto}=({k};0)"
			kq3=f"{vecto}=({b};{k})"
			kq4=f"{vecto}=({-b};{-k})"
		if a!=0 and b==0:	
			kq=random.choice([f"{vecto}=({k};0)", f"{vecto}=({a};0)"])
			kq2=f"{vecto}=(0;{k})"
			kq3=f"{vecto}=({a};{k})"
			kq4=f"{vecto}=({-a};{-k})"	
	else:
		vecto="\\overrightarrow{{u}}"
		if a!=0 and b!=0:
			kq=random.choice([f"{vecto}=({b};{-a})", f"{vecto}=({-b};{a})"])	
			kq2=f"{vecto}=({a};{b})"
			kq3=f"{vecto}=({-a};{b})"
			kq4=f"{vecto}=({b};{a})"
		if a==0 and b!=0:
			kq=random.choice([f"{vecto}=({k};0)", f"{vecto}=({b};0)"])
			kq2=random.choice([f"{vecto}=(0;{k})", f"{vecto}=(0;{b})"])
			kq3=f"{vecto}=({b};{k})"
			kq4=f"{vecto}=({-b};{-k})"
		if a!=0 and b==0:	
			kq=random.choice([f"{vecto}=(0;{k})",f"{vecto}=(0;{a})"])
			kq2=random.choice([f"{vecto}=({k};0)", f"{vecto}=({a};0)"])
			kq3=f"{vecto}=({a};{k})"
			kq4=f"{vecto}=({-a};{-k})"	


	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}:{latex(f)}=0$."\
			 f"Véctơ nào sau đây là một {ten_vt} của đường thẳng ${{d}}$?"
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Đường thẳng ${{d}}:{latex(f)}=0$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b})$ hoặc $\\overrightarrow{{n}}=({-a};{-b})$,\n"\
					f"có một véctơ chỉ phương là $\\overrightarrow{{u}}=({b};{-a})$ hoặc $\\overrightarrow{{u}}=({-b};{a})$.\n"
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

#[D10_CX_B1_03]-M2. Đọc véctơ pháp tuyến(véctơ chỉ phương) từ phương trình tham số
def gghik_L10_CX_B1_03():   
	#Tạo bậc ngẫu nhiên
	ten_vt=random.choice(["véctơ pháp tuyến","véctơ chỉ phương"])
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	if a==b: b=a+random.randint(1,3)
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if a==b or a==-b: a=a+random.randint(1,3)
	x=sp.symbols("x")
	y=sp.symbols("y")
	t=sp.symbols("t")

	f=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)}\\\\ \
y = {show_ptts(y_0,b)}\
\\end{{array}} \\right.,t \\in \\mathbb{{R}}"

	k = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if ten_vt=="véctơ chỉ phương":
		vecto="\\overrightarrow{{u}}"		
		if a!=0 and b!=0:
			kq=random.choice([f"{vecto}=({a};{b})", f"{vecto}=({-a};{-b})"])	
			kq2=f"{vecto}=({-b};{-a})"
			kq3=random.choice([f"{vecto}=({x_0};{y_0})", f"{vecto}=({-a};{b})"])
			kq4=f"{vecto}=({b};{a})"
		if a==0 and b!=0:
			kq=random.choice([f"{vecto}=(0;{k})", f"{vecto}=(0;{b})"])
			kq2=f"{vecto}=({k};0)"
			kq3=f"{vecto}=({b};{k})"
			kq4=f"{vecto}=({-b};{-k})"
		if a!=0 and b==0:	
			kq=random.choice([f"{vecto}=({k};0)", f"{vecto}=({a};0)"])
			kq2=f"{vecto}=(0;{k})"
			kq3=f"{vecto}=({a};{k})"
			kq4=f"{vecto}=({-a};{-k})"	
	else:
		vecto="\\overrightarrow{{n}}"
		if a!=0 and b!=0:
			kq=random.choice([f"{vecto}=({b};{-a})", f"{vecto}=({-b};{a})"])	
			kq2=random.choice([f"{vecto}=({x_0};{y_0})",f"{vecto}=({a};{b})"])
			kq3=f"{vecto}=({-a};{b})"
			kq4=f"{vecto}=({b};{a})"
		if a==0 and b!=0:
			kq=random.choice([f"{vecto}=({k};0)", f"{vecto}=({b};0)"])
			kq2=random.choice([f"{vecto}=(0;{k})", f"{vecto}=(0;{b})"])
			kq3=f"{vecto}=({b};{k})"
			kq4=f"{vecto}=({-b};{-k})"
		if a!=0 and b==0:	
			kq=random.choice([f"{vecto}=(0;{k})",f"{vecto}=(0;{a})"])
			kq2=random.choice([f"{vecto}=({k};0)", f"{vecto}=({a};0)"])
			kq3=f"{vecto}=({a};{k})"
			kq4=f"{vecto}=({-a};{-k})"	


	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}:{f}$."\
			 f"Véctơ nào sau đây là một {ten_vt} của đường thẳng ${{d}}$?"
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Đường thẳng ${{d}}:{f}$ có một véctơ chỉ phương là $\\overrightarrow{{n}}=({a};{b})$ hoặc $\\overrightarrow{{n}}=({-a};{-b})$,\n"\
					f"có một véctơ pháp tuyến là $\\overrightarrow{{u}}=({b};{-a})$ hoặc $\\overrightarrow{{u}}=({-b};{a})$.\n"
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

#[D10_CX_B1_04]-M1. Cho tọa độ điểm và véctơ pháp tuyến, viết phương trình tổng quát
def gghik_L10_CX_B1_04():   
	#Tạo bậc ngẫu nhiên
	ten_vt=random.choice(["véctơ pháp tuyến","véctơ chỉ phương"])
	ten_diem=random.choice(["A","B","C","D","E","M","N","P"])
	vecto_n="\\overrightarrow{{n}}"
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	if a==b: b=b+random.randint(1,5)
	if a==-b: b=b+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	x=sp.symbols("x")
	y=sp.symbols("y")

	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	ucln=gcd(abs(x_0),abs(y_0))
	x_1,y_1=int(x_0/ucln),int(y_0/ucln)

	kq=f"{latex(a*(x-x_0)+b*(y-y_0))}=0"
	kq2=f"{latex(a*(x+x_0)+b*(y+y_0))}=0"
	kq3=f"{latex(x_1*(x-a)+y_1*(y-b))}=0"
	kq4=f"{latex(b*(x-x_0)-a*(y-y_0))}=0"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}$ đi qua điểm ${{{ten_diem}}}({x_0};{y_0})$"\
			 f"và nhận vectơ ${vecto_n}({a};{b})$ làm véctơ pháp tuyến. Viết phương trình tổng quát của đường thẳng ${{d}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	noi_dung_loigiai=f""

	
	#noi_dung_loigiai=f"Phương trình tổng quát của đường thẳng ${{d}}:{a}\\left({my_module.show_hieu('x',x_0)}\\right){b1}\\left({my_module.show_hieu('y',y_0)}\\right)=0$\n"\
					#f"suy ra: ${kq}$.\n"
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

#[D10_CX_B1_05]-M1. Cho tọa độ điểm và véctơ pháp tuyến, viết phương trình tổng quát
def gghik_L10_CX_B1_05():   
	#Tạo bậc ngẫu nhiên
	ten_diem=random.choice(["A","B","C","D","E","M","N","P"])
	vecto_u="\\overrightarrow{{u}}"
	vecto_n="\\overrightarrow{{n}}"
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==b: b=b+random.randint(1,5)
	if a==-b: b=b+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	x=sp.symbols("x")
	y=sp.symbols("y")

	#Tìm véctơ pháp tuyến
	vtpt=tim_vtpt_tu_vtcp(a,b)
	A,B=vtpt[0],vtpt[1]

	#Tìm UCLN của véctơ pháp tuyến:	

	ucln=gcd(abs(A),abs(B))
	A,B=int(A/ucln),int(B/ucln)
	B1=show_dau_value(B)

	ucln=gcd(abs(x_0),abs(y_0))
	x_1,y_1=int(x_0/ucln),int(y_0/ucln)

	kq=f"{latex(A*(x-x_0)+B*(y-y_0))}=0"
	kq2=f"{latex(A*(x+x_0)+B*(y+y_0))}=0"
	kq3=f"{latex(x_1*(x-A)+y_1*(y-B))}=0"
	kq4=f"{latex(a*(x-x_0)+b*(y-y_0))}=0"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}$ đi qua điểm ${{{ten_diem}}}({x_0};{y_0})$"\
			 f"và nhận vectơ ${vecto_u}({a};{b})$ làm véctơ chỉ phương. Viết phương trình tổng quát của đường thẳng ${{d}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

	
	noi_dung_loigiai=f""
	#noi_dung_loigiai=f"Đường thẳng ${{d}}$ có véctơ chỉ phương là ${vecto_u}({a};{b})$ nên có một véctơ pháp tuyến là ${vecto_n}({A};{B})$\n"\
	#f"Phương trình tổng quát của đường thẳng ${{d}}:{A}\\left({my_module.show_hieu('x',x_0)}\\right){B1}\\left({my_module.show_hieu('y',y_0)}\\right)=0$\n"\
					#f"suy ra: ${kq}$.\n"
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

#[D10_CX_B1_06]-M2. Viết phương trình tổng quát đường thẳng qua điểm song song với đường thẳng.
def gghik_L10_CX_B1_06():   
	#Tạo bậc ngẫu nhiên
	
	ten_diem=random.choice(["A","B","C","D","E","M","N","P"])
	ten_d=random.choice(["d'","d_1","\\Delta"])
	vecto_n="\\overrightarrow{{n}}"
	
	a=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)

	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==b: b=b+random.randint(1,5)
	if a==-b: b=b+random.randint(1,5)
	
	x=sp.symbols("x")
	y=sp.symbols("y")

	#Tạo đường thẳng d1 song song với đường thẳng d
	x1=x_0+random.randint(1,5)
	y1=y_0-random.randint(1,5)
	d1=a*(x-x1)+b*(y-y1)

	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	ucln=gcd(abs(x_0),abs(y_0))
	x_1,y_1=int(x_0/ucln),int(y_0/ucln)

	kq=f"{latex(a*(x-x_0)+b*(y-y_0))}=0"
	kq2=f"{latex(a*(x+x_0)+b*(y+y_0))}=0"
	kq3=f"{latex((a+random.randint(1,5))*(x-x_0)-b*(y-y_0)+random.randint(1,5))}=0"
	kq4=f"{latex(b*(x-x_0)-a*(y-y_0)+random.randint(1,5))}=0"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}$ đi qua điểm ${{{ten_diem}}}({x_0};{y_0})$"\
			 f"và song song với đường thẳng ${ten_d}:{latex(d1)}=0$. Viết phương trình tổng quát của đường thẳng ${{d}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Đường thẳng ${ten_d}:{latex(d1)}=0$ có một véctơ pháp tuyến là $\\overrightarrow{{n}}=({a};{b})$.\n"\
			f"Đường thẳng ${{d}}$ song song với đường thẳng ${{{ten_d}}}$ nên ${{d}}$ cũng nhận $\\overrightarrow{{n}}$ làm véctơ pháp tuyến.\n"\
			f"Phương trình tổng quát của ${{d}}:{a}\\left({my_module.show_hieu('x',x_0)}\\right){b1}\\left({my_module.show_hieu('y',y_0)}\\right)=0$\n"\
			f"suy ra: ${kq}$.\n"
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


#[D10_CX_B1_07]-M2. Viết phương trình tổng quát đường thẳng qua điểm vuông góc với đường thẳng.
def gghik_L10_CX_B1_07():   
	#Tạo bậc ngẫu nhiên
	
	ten_diem=random.choice(["A","B","C","D","E","M","N","P"])
	ten_d=random.choice(["d'","d_1","\\Delta"])
	vecto_n="\\overrightarrow{{n}}"
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==b: b=b+random.randint(1,5)
	if a==-b: b=b+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	x=sp.symbols("x")
	y=sp.symbols("y")

	#Tạo đường thẳng d1 song song với đường thẳng d
	x1=x_0+random.randint(1,5)
	y1=y_0-random.randint(1,5)

	d1=b*(x-x1)-a*(y-y1)

	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	kq=f"{latex(a*(x-x_0)+b*(y-y_0))}=0"
	kq2=f"{latex(a*(x+x_0)+b*(y+y_0))}=0"
	kq3=f"{latex((a+random.randint(1,5))*(x-x_0)-b*(y-y_0) +random.randint(1,5))}=0"
	kq4=f"{latex(b*(x-x_0)-a*(y-y_0) +random.randint(1,5))}=0"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}$ đi qua điểm ${{{ten_diem}}}({x_0};{y_0})$"\
			 f"và vuông góc với đường thẳng ${ten_d}:{latex(d1)}=0$. Viết phương trình tổng quát của đường thẳng ${{d}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Đường thẳng ${ten_d}:{latex(d1)}=0$ có một véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({b};{-a})$.\n"\
			f"Đường thẳng ${{d}}$ vuông góc với đường thẳng ${{{ten_d}}}$ nên ${{d}}$ nhận $\\overrightarrow{{n}}=({a};{b})$ làm véctơ pháp tuyến.\n"\
			f"Phương trình tổng quát của ${{d}}:{a}\\left({my_module.show_hieu('x',x_0)}\\right){b1}\\left({my_module.show_hieu('y',y_0)}\\right)=0$\n"\
			f"suy ra: ${kq}$.\n"
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

#[D10_CX_B1_08]-M2. Viết phương trình tổng quát đường thẳng qua 2 điểm
def gghik_L10_CX_B1_08():  
	
	ten_diem_1=random.choice(["A","M","C","E"])
	ten_diem_2=random.choice(["B","N","D","F"])
	ten_d=random.choice(["d","d_1","\\Delta"])
	vecto_n="\\overrightarrow{{n}}"


	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)	
	if x_0==y_0: y_0=x_0+random.randint(1,3)

	x_1 = x_0 + random.randint(1,6)
	y_1 = y_0 - random.randint(1,6)

	a_cp, b_cp =x_1-x_0, y_1 - y_0
	t=tim_vtpt_tu_vtcp(a_cp, b_cp)
	a, b =t[0], t[1]

	x=sp.symbols("x")
	y=sp.symbols("y")	


	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	kq=f"{latex(a*(x-x_0)+b*(y-y_0))}=0"
	kq2=f"{latex(a*(x+x_0)+b*(y+y_0))}=0"
	kq3=f"{latex(a*(x-x_0)-b*(y-y_0) +random.randint(1,5))}=0"
	kq4=f"{latex(b*(x-x_0)-a*(y-y_0) +random.randint(1,5))}=0"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{d}}$ đi qua hai điểm ${{{ten_diem_1}}}({x_0};{y_0})$"\
			 f"và ${{{ten_diem_2}}}({x_1};{y_1})$. Viết phương trình tổng quát của đường thẳng ${{d}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Đường thẳng ${ten_d}$ có một véctơ chỉ phương là $\\overrightarrow{{{ten_diem_1}{ten_diem_2}}}=({a_cp};{b_cp})$.\n"\
			f"Suy ra ${{d}}$ nhận $\\overrightarrow{{n}}=({a};{b})$ làm véctơ pháp tuyến.\n"\
			f"Phương trình tổng quát của ${{d}}:{a}\\left({my_module.show_hieu('x',x_0)}\\right){b1}\\left({my_module.show_hieu('y',y_0)}\\right)=0$\n"\
			f"suy ra: ${kq}$.\n"
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


#[D10_CX_B1_09]-M2. Cho tam giác. Viết phương trình tổng quát đường cao
def gghik_L10_CX_B1_09():  
	x=sp.symbols("x")
	y=sp.symbols("y")
	
	ten_diem_1=random.choice(["A","M","D"])
	ten_diem_2=random.choice(["B","N","E"])
	ten_diem_3=random.choice(["C","P","F"])

	x_1=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	y_1=random.randint(-7,7)

	x_2=x_1+random.randint(1,4)
	y_2=y_1+ random.randint(1,4)

	x_3=x_1-random.randint(1,5)
	y_3=y_1-random.randint(1,4)

	t_1=(x_2-x_1)*(y_3-y_1)-(y_2-y_1)*(x_3-x_1)
	if t_1==0:x_3=x_3+random.randint(1,3)	

	a, b =x_3-x_2, y_3-y_2


	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	kq=f"{latex(a*(x-x_1)+b*(y-y_1))}=0"
	kq2=f"{latex(a*(x+x_1)+b*(y+y_1)+random.randint(1,10))}=0"
	kq3=f"{latex((a+random.randint(1,5))*(x-x_1)+b*(y-y_1))}=0"
	kq4=f"{latex(a*(x-x_1)+(b+random.randint(1,5))*(y-y_1))}=0"
	ABC=f"{ten_diem_1}{ten_diem_2}{ten_diem_3}"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho tam giác ${{{ABC}}}$ có ${ten_diem_1}({x_1};{y_1}),{ten_diem_2}({x_2};{y_2})$ và ${{{ten_diem_3}({x_3};{y_3})}}$."\
			 f"Viết phương trình tổng quát của đường cao xuất phát từ đỉnh ${{{ten_diem_1}}}$ của tam giác ${{{ABC}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Đường cao ${{d}}$ xuất phát từ đỉnh ${{{ten_diem_1}({x_1};{y_1})}}$ nhận véctơ $\\overrightarrow{{{ten_diem_2}{ten_diem_3}}}=({a};{b})$ làm một véctơ pháp tuyến.\n"\
			f"Phương trình tổng quát của ${{d}}:{a}\\left({my_module.show_hieu('x',x_1)}\\right){b1}\\left({my_module.show_hieu('y',y_1)}\\right)=0$\n"\
			f"suy ra: ${kq}$.\n"
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

#[D10_CX_B1_010]-M2. Cho tam giác. Viết phương trình tổng quát đường trung trực
def gghik_L10_CX_B1_10():  
	x=sp.symbols("x")
	y=sp.symbols("y")
	
	ten_diem_1=random.choice(["A","M","D"])
	ten_diem_2=random.choice(["B","N","E"])
	ten_diem_3=random.choice(["C","P","F"])


	x_1=random.randint(-6,6)
	y_1=random.randint(-7,7)	

	x_2=x_1+random.randint(1,4)
	y_2=y_1+ random.randint(1,4)	

	x_I=random.randint(-6,6)
	y_I=random.randint(-6,6)

	x_3=2*x_I-x_2
	y_3=2*y_I-y_2

	a, b =x_3-x_2, y_3-y_2	

	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=math.gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	kq=f"{latex(a*(x-x_I)+b*(y-y_I))}=0"
	kq2=f"{latex(a*(x-x_I)+b*(y-y_I)+random.randint(1,5))}=0"
	kq3=f"{latex(a*(x-x_1)+(b+random.randint(2,4))*(y-y_1))}=0"
	kq4=f"{latex((b+random.randint(1,5))*(x-x_1)-a*(y-y_1))}=0"
	ABC=f"{ten_diem_1}{ten_diem_2}{ten_diem_3}"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho tam giác ${{{ABC}}}$ có ${ten_diem_1}({x_1};{y_1}),{ten_diem_2}({x_2};{y_2})$ và ${{{ten_diem_3}({x_3};{y_3})}}$."\
			 f"Viết phương trình tổng quát của đường trung trực của đoạn thẳng ${{{ten_diem_2}{ten_diem_3}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"Gọi $I=({x_I};{y_I})$ là trung điểm của đoạn ${{{ten_diem_2}{ten_diem_3}}}$.\n"\
		f"Đường trung trực ${{d}}$ của đoạn thẳng ${{{ten_diem_2}{ten_diem_3}}}$ đi qua trung điểm $I=({x_I};{y_I})$"\
		f"và nhận vectơ $\\overrightarrow{{{ten_diem_2}{ten_diem_3}}}=({a};{b})$ làm một véctơ pháp tuyến.\n"\
		f"Phương trình tổng quát của ${{d}}:{a}\\left({my_module.show_hieu('x',x_I)}\\right){b1}\\left({my_module.show_hieu('y',y_I)}\\right)=0$\n"\
		f"suy ra: ${kq}$.\n"
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

#[D10_CX_B1_11]-M2. Cho tam giác. Viết phương trình tổng quát đường trung tuyến
def gghik_L10_CX_B1_11():  
	x=sp.symbols("x")
	y=sp.symbols("y")
	
	ten_diem_1=random.choice(["A","M","D"])
	ten_diem_2=random.choice(["B","N","E"])
	ten_diem_3=random.choice(["C","P","F"])	

	x_1=random.randint(-6,6)
	y_1=random.randint(-7,7)	

	x_2=x_1+random.randint(1,4)
	y_2=y_1+ random.randint(1,4)	

	x_I=random.randint(-6,6)
	y_I=random.randint(-6,6)

	x_3=2*x_I-x_2
	y_3=2*y_I-y_2

	a, b =y_I-y_1, -(x_I-x_1)

	#Tìm UCLN của véctơ pháp tuyến:	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	kq=f"{latex(a*(x-x_I)+b*(y-y_I))}=0"
	kq2=f"{latex(a*(x+x_I)+b*(y+y_I))}=0"
	kq3=f"{latex(a*(x-x_1)-(b+random.randint(1,3))*(y-y_1))}=0"
	kq4=f"{latex(b*(x-x_1)-(a+random.randint(1,3))*(y-y_1)+random.randint(1,3))}=0"

	ABC=f"{ten_diem_1}{ten_diem_2}{ten_diem_3}"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho tam giác ${{{ABC}}}$ có ${ten_diem_1}({x_1};{y_1}),{ten_diem_2}({x_2};{y_2})$ và ${{{ten_diem_3}({x_3};{y_3})}}$."\
			 f"Viết phương trình tổng quát của đường trung tuyến xuất phát từ đỉnh ${{{ten_diem_1}}}$ của tam giác ${{{ABC}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"Gọi $I=({x_I};{y_I})$ là trung điểm của đoạn ${{{ten_diem_2}{ten_diem_3}}}$.\n"\
		f"Đường trung tuyến ${{{ten_diem_1}I}}$ nhận vectơ $\\overrightarrow{{{ten_diem_1}I}}=({x_I-x_1};{y_I-y_1})$ làm véctơ chỉ phương.\n"\
		f"và nhận vectơ $\\overrightarrow{{n}}=({a};{b})$ làm một véctơ pháp tuyến.\n"\
		f"Phương trình tổng quát của ${{{ten_diem_1}I}}:{a}\\left({my_module.show_hieu('x',x_I)}\\right){b1}\\left({my_module.show_hieu('y',y_I)}\\right)=0$\n"\
		f"suy ra: ${kq}$.\n"
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

#10.1.2 Phương trình tham số

#[D10_CX_B1_12]-M1. Lập PTTS của d qua điểm và có VT chỉ phương
def gghik_L10_CX_B1_12():   

	x=sp.symbols("x")
	y=sp.symbols("y")
	t=sp.symbols("t")

	ten_diem=random.choice(["A","B","C","D","E","M","N","P"])
	ten_d=random.choice(["d","d_1","\\Delta"])	
	vecto_u="\\overrightarrow{{u}}"
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	a1,b1 =a,b
	if a==b: b=a+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	
	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=math.gcd(abs(a),abs(b))
	a, b=int(a/ucln), int(b/ucln)


	f=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)} \\\\ \
y = {show_ptts(y_0,b)}\
\\end{{array}} \\right."


	f2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)} \\\\ \
y = {show_ptts(b,y_0)}\
\\end{{array}} \\right."


	f3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,-a)} \\\\ \
y = {show_ptts(x_0,-b)}\
\\end{{array}} \\right."

	f4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_0,a)} \\\\ \
y = {show_ptts(-y_0,b)}\
\\end{{array}} \\right."
	
	kq=f"{f}"
	kq2=f"{f2}"
	kq3=f"{f3}"
	kq4=f"{f4}"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{{ten_d}}}$ đi qua điểm ${{{ten_diem}}}({x_0};{y_0})$"\
			 f"và nhận vectơ ${vecto_u}({a1};{b1})$ làm véctơ chỉ phương. Viết phương trình tham số của đường thẳng ${{{ten_d}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Đường thẳng ${{{ten_d}}}$ qua điểm ${{{ten_diem}}}({x_0};{y_0})$ nhận vectơ ${vecto_u}({a};{b})$ làm véctơ chỉ phương\n"\
						f"có phương trình tham số là:${f}$\n"		
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

#[D10_CX_B1_13]-M1. Lập PTTS của d qua điểm và có VT pháp tuyến
def gghik_L10_CX_B1_13():   

	x=sp.symbols("x")
	y=sp.symbols("y")
	t=sp.symbols("t")

	ten_diem=random.choice(["A","B","C","D","E","M","N","P"])
	ten_d=random.choice(["d","d_1","\\Delta"])	
	vecto_u="\\overrightarrow{{u}}"
	vecto_n="\\overrightarrow{{u}}"
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	if a==b: b=a+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	x_0=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	y_0=random.randint(-10,10)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	
	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)


	f=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)} \\\\ \
y = {show_ptts(y_0,b)}\
\\end{{array}} \\right."


	f2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)} \\\\ \
y = {show_ptts(b,y_0)}\
\\end{{array}} \\right."


	f3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,-a)} \\\\ \
y = {show_ptts(y_0,b+1)}\
\\end{{array}} \\right."

	f4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_0,a)} \\\\ \
y = {show_ptts(-y_0,b)}\
\\end{{array}} \\right."
	
	kq=f"{f}"
	kq2=f"{f2}"
	kq3=f"{f3}"
	kq4=f"{f4}"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{{ten_d}}}$ đi qua điểm ${{{ten_diem}}}({x_0};{y_0})$"\
			 f"và nhận vectơ ${vecto_n}({b};{-a})$ làm véctơ pháp tuyến. Viết phương trình tham số của đường thẳng ${{{ten_d}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Đường thẳng ${{{ten_d}}}$ nhận ${vecto_n}=({b};{-a})$ làm véctơ pháp tuyến nên có một véctơ chỉ phương là ${vecto_u}=({a};{b})$.\n"\
	f"Phương trình tham số của đường thẳng ${{{ten_d}}}:{f}$\n"		
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

#[D10_CX_B1_14]-M2. Lập PTTS của d qua 2 điểm 
def gghik_L10_CX_B1_14():   

	x=sp.symbols("x")
	y=sp.symbols("y")
	t=sp.symbols("t")

	ten_diem_1=random.choice(["A","M","C","E"])
	ten_diem_2=random.choice(["B","N","D","F"])
	ten_d=random.choice(["d","d_1","\\Delta"])	

	x_0=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	y_0=random.randint(-10,10)	
	if x_0==y_0: y_0=x_0+random.randint(1,3)

	x_1 = x_0 + random.randint(1,6)
	y_1 = y_0 - random.randint(1,6)

	a, b =x_1-x_0, y_1 - y_0
	vecto_u=f"\\overrightarrow{{{ten_diem_1}{ten_diem_2}}}"
	
	#Tìm UCLN của véctơ pháp tuyến:
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)

	f_1=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)} \\\\ \
y = {show_ptts(y_0,b)}\
\\end{{array}} \\right."

	f_2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_1,a)} \\\\ \
y = {show_ptts(y_1,b)}\
\\end{{array}} \\right."
	
	f=random.choice([f_1,f_2])


	f2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)} \\\\ \
y = {show_ptts(b,y_0)}\
\\end{{array}} \\right."


	f3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,x_1)} \\\\ \
y = {show_ptts(y_0,y_1)}\
\\end{{array}} \\right."

	f4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_1,a)} \\\\ \
y = {show_ptts(-y_1,b)}\
\\end{{array}} \\right."
	
	kq=f"{f}"
	kq2=f"{f2}"
	kq3=f"{f3}"
	kq4=f"{f4}"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{{ten_d}}}$ đi qua hai điểm ${{{ten_diem_1}}}({x_0};{y_0})$ và ${{{ten_diem_2}}}({x_1};{y_1})$."\
			 f" Viết phương trình tham số của đường thẳng ${{{ten_d}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Đường thẳng ${{{ten_d}}}$ nhận ${vecto_u}=({x_1-x_0};{y_1-y_0})$ làm một véctơ chỉ phương.\n"\
	f"Phương trình tham số của đường thẳng ${{{ten_d}}}:{f}$\n"		
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

#[D10_CX_B1_15]-M2. Lập PTTS của d từ PTTQ
def gghik_L10_CX_B1_15():   

	x=sp.symbols("x")
	y=sp.symbols("y")
	t=sp.symbols("t")

	ten_diem=random.choice(["A","B","C","D","E","M","N","P"])
	vecto_u="\\overrightarrow{{u}}"
	vecto_n="\\overrightarrow{{n}}"
	ten_d=random.choice(["d","d_1","\\Delta"])	
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	a1,b1 =a,b
	if a==b: b=a+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	
	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)


	f=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)} \\\\ \
y = {show_ptts(y_0,b)}\
\\end{{array}} \\right."


	f2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(a,x_0)} \\\\ \
y = {show_ptts(b,y_0)}\
\\end{{array}} \\right."


	f3=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,-a)} \\\\ \
y = {show_ptts(x_0,-b)}\
\\end{{array}} \\right."

	f4=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(-x_0,a)} \\\\ \
y = {show_ptts(-y_0,b)}\
\\end{{array}} \\right."
	
	kq=f"{f}"
	kq2=f"{f2}"
	kq3=f"{f3}"
	kq4=f"{f4}"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{{ten_d}}}$ có phương trình tổng quát ${latex(b*(x-x_0)-a*(y-y_0))}=0$."\
			 f"Viết phương trình tham số của đường thẳng ${{{ten_d}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Cho $x={x_0}$ suy ra ${{{ten_d}}}$ qua điểm ${{{ten_diem}}}({x_0};{y_0})$ nhận vectơ ${vecto_n}({b};{-a})$ là một véctơ pháp tuyến."\
		f" Suy ra ${{{ten_d}}}$ nhận ${vecto_u}({a};{b})$ làm véctơ chỉ phương.\n"\
		f"${{{ten_d}}}$ có phương trình tham số là:${f}$\n"		
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

#[D10_CX_B1_16]-M2. Lập PTTQ từ PTTS
def gghik_L10_CX_B1_16():   

	x=sp.symbols("x")
	y=sp.symbols("y")

	vecto_n="\\overrightarrow{{n}}"
	vecto_u="\\overrightarrow{{u}}"
	ten_d=random.choice(["d","d_1","\\Delta"])	
	
	a=random.randint(-10,10)
	b=random.randint(-10,10)
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	if a==b==0:
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	

	f=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,b)} \\\\ \
y = {show_ptts(y_0,-a)}\
\\end{{array}} \\right."

	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(b)

	ucln=gcd(abs(x_0),abs(y_0))
	x_1,y_1=int(x_0/ucln),int(y_0/ucln)

	kq=f"{latex(a*(x-x_0)+b*(y-y_0))}=0"
	kq2=f"{latex(a*(x+x_0)+b*(y+y_0))}=0"
	kq3=f"{latex(x_1*(x-a)+y_1*(y-b))}=0"
	kq4=f"{latex(b*(x-x_0)-a*(y-y_0))}=0"

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{{ten_d}}}$ có phương trình tham số là ${f}$."\
			 f" Viết phương trình tổng quát của đường thẳng ${{{ten_d}}}$."
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Theo đề bài ta có ${{{ten_d}}}$ qua điểm ${{A({x_0};{y_0})}}$ và nhận vectơ ${vecto_u}=({-b};{a})$ làm véctơ chỉ phương.\n"\
	f"Suy ra ${{{ten_d}}}$ nhận vectơ ${vecto_n}=({a};{b})$ làm véctơ pháp tuyến.\n"\
	f"Phương trình tổng quát của ${{{ten_d}}}:{a}\\left({my_module.show_hieu('x',x_0)}\\right){b1}\\left({my_module.show_hieu('y',y_0)}\\right)=0$\n"\
					f"suy ra: ${kq}$.\n"
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

#[D10_CX_B1_17]-M1. Tìm điểm thuộc d biết PTTS.
def gghik_L10_CX_B1_17():   

	x=sp.symbols("x")
	y=sp.symbols("y")
	t=sp.symbols("t")

	ten_d=random.choice(["d","d_1","\\Delta"])	
	vecto_u="\\overrightarrow{{u}}"
	vecto_n="\\overrightarrow{{n}}"
	
	a=random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b=random.choice([random.randint(-10, -1), random.randint(1, 10)])

	if a==b: b=a+random.randint(1,5)
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	t1=random.randint(1,3)
	t2=random.randint(-3,-1)
	t3=random.randint(4,6)
	t4=random.randint(-6,-4)
	
	
	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=math.gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(-a)


	f=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_0,a)} \\\\ \
y = {show_ptts(y_0,b)}\
\\end{{array}} \\right."

	chon=random.choice(["thuộc", "không thuộc"])
	if chon=="thuộc":
		kq=random.choice([f"({x_0};{y_0})", f"({x_0+a*t1};{y_0+b*t1})", f"({x_0+a*t2};{y_0+b*t2})", f"({x_0+a*t3};{y_0+b*t3})"])
		kq2=f"({x_0};{y_0+1})"
		kq3=random.choice([f"({a};{b})", f"({-x_0+a*t3};{y_0-b*t3})"])
		kq4=random.choice([f"({x_0+a*t1};{x_0+b*t1})",f"({x_0+a*t2};{-y_0-b*t2})"])
	else:
		kq=random.choice([f"({a};{b})", f"({-x_0+a*t3};{y_0-b*t3})", f"({x_0+a*t2};{-y_0-b*t2})" ])
		kq2=random.choice([f"({x_0};{y_0})", f"({x_0+a*t1};{y_0+b*t1})"])
		kq3=random.choice([f"({x_0+a*t2};{y_0+b*t2})", f"({x_0+a*t3};{y_0+b*t3})"])
		kq4=f"({x_0+a*t4};{y_0+b*t4})"


	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{{ten_d}}}$ có phương trình tham số là ${f}$."\
			 f" Điểm nào sau đây {chon} đường thẳng ${{{ten_d}}}$?"
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Theo đề bài ta có ${{{ten_d}}}$ qua điểm ${{A({x_0};{y_0})}}$ và nhận vectơ ${vecto_u}=({a};{b})$ làm véctơ chỉ phương.\n"\
	f"Suy ra ${{{ten_d}}}$ nhận vectơ ${vecto_n}=({b};{-a})$ làm véctơ pháp tuyến.\n"\
	f"Phương trình tổng quát của ${{{ten_d}}}:{b}\\left({my_module.show_hieu('x',x_0)}\\right){b1}\\left({my_module.show_hieu('y',y_0)}\\right)=0 \\Leftrightarrow {latex(b*(x-x_0)-a*(y-y_0))}=0$.\n"\
	f"Thay tọa độ các điểm từ các phương án vào phương trình tổng quát ta được điểm ${{{kq}}}$ {chon} ${{{ten_d}}}$."
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

#[D10_CX_B1_18]-M1. Tìm điểm thuộc d biết PTTQ.
def gghik_L10_CX_B1_18():   

	x=sp.symbols("x")
	y=sp.symbols("y")
	t=sp.symbols("t")

	ten_d=random.choice(["d","d_1","\\Delta"])	
	vecto_u="\\overrightarrow{{u}}"
	vecto_n="\\overrightarrow{{n}}"
	
	a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	if a==b: b=a+random.randint(1,5)
	x_0=random.randint(-10,10)
	y_0=random.randint(-10,10)
	if x_0==y_0: y_0=x_0+random.randint(1,3)
	if a==x_0 and b==y_0:
		x_0=a+random.randint(1,5)
		y_0=b+random.randint(1,5)
	t1=random.randint(1,3)
	t2=random.randint(-3,-1)
	t3=random.randint(4,6)
	t4=random.randint(-6,-4)
	
	
	#Tìm UCLN của véctơ pháp tuyến:
	
	ucln=gcd(abs(a),abs(b))
	a,b=int(a/ucln),int(b/ucln)
	b1=show_dau_value(-a)


	f=latex(b*(x-x_0)-a*(y-y_0))

	chon=random.choice(["thuộc", "không thuộc"])
	if chon=="thuộc":
		kq=random.choice([f"({x_0};{y_0})", f"({x_0+a*t1};{y_0+b*t1})", f"({x_0+a*t2};{y_0+b*t2})", f"({x_0+a*t3};{y_0+b*t3})"])
		kq2=f"({x_0};{y_0+1})"
		kq3=random.choice([f"({a};{b})", f"({-x_0+a*t3};{y_0-b*t3})"])
		kq4=random.choice([f"({x_0+a*t1};{x_0+b*t1})",f"({x_0+a*t2};{-y_0-b*t2})"])
	else:
		kq=random.choice([f"({a};{b})", f"({-x_0+a*t3};{y_0-b*t3})", f"({x_0+a*t2};{-y_0-b*t2})" ])
		kq2=random.choice([f"({x_0};{y_0})", f"({x_0+a*t1};{y_0+b*t1})"])
		kq3=random.choice([f"({x_0+a*t2};{y_0+b*t2})", f"({x_0+a*t3};{y_0+b*t3})"])
		kq4=f"({x_0+a*t4};{y_0+b*t4})"


	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho đường thẳng ${{{ten_d}}}$ có phương trình tổng quát là ${f}=0$."\
			 f" Điểm nào sau đây {chon} đường thẳng ${{{ten_d}}}$?"
	
    #Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   	

	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.    C. { list_PA[2]}.     D. { list_PA[3]}.\n"
	
	noi_dung_loigiai=f"Thay tọa độ các điểm từ các phương án vào phương trình tổng quát ta được điểm ${{{kq}}}$ {chon} ${{{ten_d}}}$."
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

#[D10_CX_B1_19]-M2. Cho PTTQ của 2 đường thẳng, xét vị trí tương đối.
def gghik_L10_CX_B1_19():   

	x=sp.symbols("x")
	y=sp.symbols("y")


	d1=["d","d_1","\\Delta_1"]
	d2=["d'","d_2","\\Delta_2"]
	i=random.randint(0,2)
	d1, d2 = d1[i], d2[i]
	chon=random.randint(1,4)
	#Tạo giả thiết trùng nhau
	if chon==1:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=t*a1
		b2= t*b1
		c2= t*c1

		kq=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		noi_dung_loigiai=f"Do $\\dfrac{{{a1}}}{{{a2}}}=\\dfrac{{{b1}}}{{{b2}}}=\\dfrac{{{c1}}}{{{c2}}}$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ trùng nhau.".replace("+-","-").replace("\\frac","\\dfrac")
	#Tạo giả thiết song song
	if chon==2:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=t*a1
		b2= t*b1
		c2= (t+random.randint(4,7))*c1

		kq=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		noi_dung_loigiai=f"Do $\\dfrac{{{a1}}}{{{a2}}}=\\dfrac{{{b1}}}{{{b2}}}\\ne \\dfrac{{{c1}}}{{{c2}}}$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ song song.".replace("+-","-").replace("\\frac","\\dfrac")

	#Tạo giả thiết cắt không vuông góc

	if chon==3:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=b1*t
		b2=a1*t
		c2= random.randint(-10,10)

		kq=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		noi_dung_loigiai=f"Do $\\dfrac{{{a1}}}{{{a2}}} \\ne \\dfrac{{{b1}}}{{{b2}}}$ và ${show_tich(a1,a2)}+{show_tich(b1,b2)} \\ne 0$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ cắt nhau và ${{{d1}}}$ không vuông góc với ${{{d2}}}$.".replace("+-","-").replace("\\frac","\\dfrac")

	if chon==4:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=-b1*t
		b2= a1*t
		c2= random.randint(-10,10)
		kq=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"

		noi_dung_loigiai=f"Do ${show_tich(a1,a2)}+{show_tich(b1,b2)} = 0$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ vuông góc nhau.".replace("+-","-").replace("\\frac","\\dfrac")

	f1=latex(a1*x+b1*y+c1)
	f2=latex(a2*x+b2*y+c2)
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai đường thẳng ${d1}:{f1}=0$ và ${d2}:{f2}=0$."\
			 f" Xét vị trí tương đối của ${{{d1}}}$ và ${{{d2}}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D10_CX_B1_20]-M1. Cho PTTQ của 2 đường thẳng, tính cosin của góc.
def gghik_L10_CX_B1_20():   

	x=sp.symbols("x")
	y=sp.symbols("y")


	d1=["d","d_1","\\Delta_1"]
	d2=["d'","d_2","\\Delta_2"]
	i=random.randint(0,2)
	d1, d2 = d1[i], d2[i]
	

	a1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
	b1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
	c1= random.randint(-10, 10)
	
	a2= random.choice([random.randint(-6, -1), random.randint(1, 7)])
	b2= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	c2= random.randint(-10, 10)

	t=abs(a1*a2+b1*b2)/(sqrt(a1**2+b1**2)*sqrt(a2**2+b2**2))
	t2=abs(a1+a2+b1+b2)/(sqrt(abs(a1)+abs(b1))*sqrt(abs(a2)+abs(b2)))
	t3=abs(a1+a2-b1-b2)/(sqrt(a1**2+b1**2)*sqrt(a2**2+b2**2))
	t4=abs(a1*b1+a2*b2)/(sqrt(a1**2+a2**2+b1**2+b2**2))

	pa_kotrung=my_module.khong_trung_so(t,t2,t3,t4)
	t2=pa_kotrung[1]
	t3=pa_kotrung[2]
	t4=pa_kotrung[3]

	kq=f"${{{latex(t)}}}$"
	kq2=f"${{{latex(t2)}}}$"
	kq3=f"${{{latex(t3)}}}$"
	kq4=f"${{{latex(t4)}}}$"
	noi_dung_loigiai=f"$ \\cos ({d1},{d2})=\\dfrac{{|{show_tich(a1,a2)}+{show_tich(b1,b2)}|}}{{\\sqrt{{{a1**2}+{b1**2}}}.\\sqrt{{{a2**2}+{b2**2}}}}}=$ {kq}.".replace("+-","-").replace("\\frac","\\dfrac")

	f1=latex(a1*x+b1*y+c1)
	f2=latex(a2*x+b2*y+c2)
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai đường thẳng ${d1}:{f1}=0$ và ${d2}:{f2}=0$."\
			 f" Tính cosin của góc tạo bởi ${{{d1}}}$ và ${{{d2}}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n".replace("\\frac","\\dfrac")
	
	
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

#[D10_CX_B1_21]-M1. Cho điểm và PTTQ của đường thẳng, tính khoảng cách.
def gghik_L10_CX_B1_21():   

	x=sp.symbols("x")
	y=sp.symbols("y")

	d=["d","d_1","\\Delta_1"]
	i=random.randint(0,2)
	d=d[i]
	diem=random.choice(["M","N","A","B","C","E","P"])
	chon=random.randint(1,2)
	if chon==1:
		a1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
		b1= random.choice([random.randint(-8, -1), random.randint(1, 8)])
	if chon==2:
		a1= random.choice([random.randint(-8, -1), random.randint(1, 8)])
		b1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
	c1=random.randint(-10, 10)
	
	x_0=random.randint(-10, 10)
	y_0=random.randint(-10, 10)	
	
	t=abs(a1*x_0+b1*y_0+c1)/sqrt(a1**2+b1**2)
	t2=abs(a1*x_0+b1*y_0+c1+random.randint(1,4))/sqrt(abs(a1)+abs(b1))
	t3=abs(a1+x_0+b1+y_0)/sqrt(a1**2+b1**2)
	t4=abs(x_0+y_0)/(a1**2+b1**2)


	kq=t
	kq2=t2
	kq3=t3
	kq4=t4

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	noi_dung_loigiai=f"$ d({diem},{d})=\\dfrac{{|{show_tich(a1,x_0)}+{show_tich(b1,y_0)}+{c1}|}} {{\\sqrt{{{a1**2}+{b1**2}}}}}={latex(kq)}$.".replace("+-","-").replace("\\frac","\\dfrac")\
	

	f=latex(a1*x+b1*y+c1)

	
    #Tạo các phương án
	pa_A= f"*${{ {latex(kq)}}}$"
	pa_B= f"${{ {latex(kq2)}}}$"
	pa_C= f"${{ {latex(kq3)}}}$"
	pa_D= f"${{ {latex(my_module.hien_phan_so(kq4))}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho điểm ${{{diem}({x_0};{y_0})}}$ và đường thẳng ${d}:{f}=0$."\
			 f" Tính khoảng cách từ điểm ${{{diem}({x_0};{y_0})}}$ đến đường thẳng ${{{d}}}$."
	debai= f"{noi_dung}\n"
	phuongan= my_module.frac_to_dfrac(f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n")
	
	
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

#[D10_CX_B1_22]-M2. Cho điểm và PTTS của đường thẳng, tính khoảng cách.
def gghik_L10_CX_B1_22():   

	x=sp.symbols("x")
	y=sp.symbols("y")

	d=["d","d_1","\\Delta_1"]
	i=random.randint(0,2)
	d=d[i]
	diem=random.choice(["M","N","A","B","C","E","P"])
	
	x_0=random.randint(-10, 10)
	y_0=random.randint(-10, 10)	

	a1= random.choice([random.randint(-7, -1), random.randint(1, 7)])
	b1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
	x_1=random.randint(-8, 8)
	y_1=random.randint(-8, 18)
	c1= -a1*x_1-b1*y_1

	f_ts=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_1,-b1)} \\\\ \
y = {show_ptts(y_1,a1)}\
\\end{{array}} \\right."	
	
	t=abs(a1*x_0+b1*y_0+c1)/sqrt(a1**2+b1**2)
	t2=abs(a1*x_0+b1*y_0+c1+random.randint(1,4))/sqrt(abs(a1)+abs(b1))
	t3=abs(a1+x_0+b1+y_0)/sqrt(a1**2+b1**2)
	t4=abs(x_0+y_0)/(a1**2+b1**2)

	kq=t
	kq2=t2
	kq3=t3
	kq4=t4

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	
    #Tạo các phương án
	pa_A= f"*$ {{{latex(kq)}}}$"
	pa_B= f"$ {{{latex(kq2)}}}$"
	pa_C= f"$ {{{latex(kq3)}}}$"
	pa_D= f"$ {{{latex(my_module.hien_phan_so(kq4))}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho điểm ${{{diem}({x_0};{y_0})}}$ và đường thẳng ${d}:{f_ts}$."\
			 f" Tính khoảng cách từ điểm ${{{diem}({x_0};{y_0})}}$ đến đường thẳng ${{{d}}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n".replace("\\frac","\\dfrac")

	noi_dung_loigiai=f"Đường thẳng ${{{d}}}$ qua điểm $({x_1};{y_1})$ có vectơ chỉ phương là $\\vec{{u}}=({-b1};{a1})$"\
	f"nên có véctơ pháp tuyến là $\\vec{{n}}=({a1};{b1})$.\n\n"\
	f"Phương trình tổng quát của ${{{d}}}$ là: ${a1}(x-{x_1})+{b1}(y-{y_1})=0 \\Leftrightarrow {latex(a1*x+b1*y-a1*x_1-b1*y_1)}=0$\n\n"\
	f"$d({diem},{d})=\\dfrac{{|{show_tich(a1,x_0)}+{show_tich(b1,y_0)}+{c1}|}} {{\\sqrt{{{a1**2}+{b1**2}}}}}={latex(kq)}$.".replace("+-","-").replace("--","+").replace("-+","-").replace("\\frac","\\dfrac")
	
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

#[D10_CX_B1_23]-M2. Cho PTTS của 2 đường thẳng, tính cosin của góc.
def gghik_L10_CX_B1_23(): 

	x=sp.symbols("x")
	y=sp.symbols("y")

	d1=["d","d_1","\\Delta_1"]
	d2=["d'","d_2","\\Delta_2"]
	i=random.randint(0,2)
	d1, d2 = d1[i], d2[i]	

	a1= random.randint(-6, 6)
	b1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
	c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	a2= random.choice([random.randint(-6, -1), random.randint(1, 7)])
	b2= random.randint(-6, 6)
	c2= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	t=abs(a1*a2+b1*b2)/(sqrt(a1**2+b1**2)*sqrt(a2**2+b2**2))
	t2=abs(a1+a2+b1+b2)/(sqrt(abs(a1)+abs(b1))*sqrt(abs(a2)+abs(b2)))
	t3=abs(a1+a2-b1-b2)/(sqrt(a1**2+b1**2)*sqrt(a2**2+b2**2))
	t4=abs(a1*b1+a2*b2)/(sqrt(a1**2+a2**2+b1**2+b2**2))

	pa_kotrung=my_module.khong_trung_so(t,t2,t3,t4)
	t2=pa_kotrung[1]
	t3=pa_kotrung[2]
	t4=pa_kotrung[3]

	kq=f"$ {latex(t)}$"
	kq2=f"$ {latex(t2)}$"
	kq3=f"$ {latex(t3)}$"
	kq4=f"$ {latex(t4)}$"
	
	x_1= random.randint(-10, 10)
	y_1= random.randint(-10, 10)

	f1=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_1,-b1)} \\\\ \
y = {show_ptts(y_1,a1)}\
\\end{{array}} \\right."

	x_2= random.randint(-10, 10)
	y_2= random.randint(-10, 10)

	f2=f"\\left\\{{ \\begin{{array}}{{l}}\
x = {show_ptts(x_2,b2)} \\\\ \
y = {show_ptts(y_2,-a2)}\
\\end{{array}} \\right."
	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai đường thẳng ${d1}:{f1}$ và ${d2}:{f2}$."\
			 f" Tính cosin của góc tạo bởi ${{{d1}}}$ và ${{{d2}}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n".replace("\\frac","\\dfrac")

	noi_dung_loigiai=f"Đường thẳng ${{{d1}}}$ có véctơ chỉ phương $\\overrightarrow{{u_1}}=({-b1};{a1})$ nên có véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({a1};{b1})$.\n\n"\
	f"Đường thẳng ${{{d2}}}$ có véctơ chỉ phương $\\overrightarrow{{u_1}}=({b2};{-a2})$ nên có véctơ pháp tuyến là $\\overrightarrow{{n_2}}=({a2};{b2})$.\n\n"\
	f"$\\cos ({d1},{d2})=\\dfrac{{|{show_tich(a1,a2)}+{show_tich(b1,b2)}|}}{{\\sqrt{{{a1**2}+{b1**2}}}.\\sqrt{{{a2**2}+{b2**2}}}}}=$ {kq}.".replace("+-","-").replace("\\frac","\\dfrac")
	
	
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

#[D10_CX_B1_24]-M2. Cho PTTS và PTTQ, tính cosin của góc.
def gghik_L10_CX_B1_24(): 

	x=sp.symbols("x")
	y=sp.symbols("y")

	d1=["d","d_1","\\Delta_1"]
	d2=["d'","d_2","\\Delta_2"]
	i=random.randint(0,2)
	d1, d2 = d1[i], d2[i]	

	a1= random.randint(-6, 6)
	b1= random.choice([random.randint(-5, -1), random.randint(1, 5)])
	c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	a2= random.choice([random.randint(-6, -1), random.randint(1, 7)])
	b2= random.randint(-6, 6)
	c2= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	t=abs(a1*a2+b1*b2)/(sqrt(a1**2+b1**2)*sqrt(a2**2+b2**2))
	t2=abs(a1+a2+b1+b2)/(sqrt(abs(a1)+abs(b1))*sqrt(abs(a2)+abs(b2)))
	t3=abs(a1+a2-b1-b2)/(sqrt(a1**2+b1**2)*sqrt(a2**2+b2**2))
	t4=abs(a1*b1+a2*b2)/(sqrt(a1**2+a2**2+b1**2+b2**2))

	pa_kotrung=my_module.khong_trung_so(t,t2,t3,t4)
	t2=pa_kotrung[1]
	t3=pa_kotrung[2]
	t4=pa_kotrung[3]

	kq=f"$ {latex(t)}$"
	kq2=f"$ {latex(t2)}$"
	kq3=f"$ {latex(t3)}$"
	kq4=f"$ {latex(t4)}$"

	f1=a1*x+b1*y+c1

	x_2= random.randint(-10, 10)
	y_2= random.randint(-10, 10)
	chon=random.randint(1,2)
	if chon==1:
		f2=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_2,b2)} \\\\ \
	y = {show_ptts(y_2,-a2)}\
	\\end{{array}} \\right."
	if chon==2:
		f2=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_2,-b2)} \\\\ \
	y = {show_ptts(y_2,a2)}\
	\\end{{array}} \\right."

	
    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai đường thẳng ${d1}:{latex(f1)}=0$ và ${d2}:{f2}$."\
			 f" Tính cosin của góc tạo bởi ${{{d1}}}$ và ${{{d2}}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n".replace("\\frac","\\dfrac")

	noi_dung_loigiai=f"Đường thẳng ${{{d1}}}$ có véctơ pháp tuyến là $\\overrightarrow{{n_1}}=({a1};{b1})$.\n\n"\
	f"Đường thẳng ${{{d2}}}$ có véctơ chỉ phương $\\overrightarrow{{u_1}}=({b2};{-a2})$ nên có véctơ pháp tuyến là $\\overrightarrow{{n_2}}=({a2};{b2})$.\n\n"\
	f"$\\cos ({d1},{d2})=\\dfrac{{|{show_tich(a1,a2)}+{show_tich(b1,b2)}|}}{{\\sqrt{{{a1**2}+{b1**2}}}.\\sqrt{{{a2**2}+{b2**2}}}}}=$ {kq}.".replace("+-","-").replace("\\frac","\\dfrac")
	
	
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

#[D10_CX_B1_25]-M2. Cho PTTS của 2 đường thẳng, xét vị trí tương đối.
def gghik_L10_CX_B1_25():   
	x=sp.symbols("x")
	y=sp.symbols("y")
	d1=["d","d_1","\\Delta_1"]
	d2=["d'","d_2","\\Delta_2"]
	i=random.randint(0,2)
	d1, d2 = d1[i], d2[i]
	chon=random.randint(1,4)
	chon=4
	#Tạo giả thiết trùng nhau
	if chon==1:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		
		x_1=random.randint(-8,8)
		y_1=random.randint(-8,8)
		f1=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_1,b1)} \\\\ \
	y = {show_ptts(y_1,-a1)}\
	\\end{{array}} \\right."
		c1= -a1*x_1-b1*y_1

		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=t*a1
		b2= t*b1

		x_2=x_1+b1*t
		y_2=y_1-a1*t
		f2=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_2,-b2)} \\\\ \
	y = {show_ptts(y_2,a2)}\
	\\end{{array}} \\right."
		c2= -a2*x_2-b2*y_2
		
		kq=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		noi_dung_loigiai=f"${{{d1}}}$ qua điểm $A({x_1};{y_1})$ và có véctơ chỉ phương là $\\overrightarrow{{u_1}}({b1};{-a1})$.\n\n"\
		f"Phương trình tổng quát của ${{{d1}}}$: ${a1}(x-{x_1})+{b1}(y-{y_1})=0\\Leftrightarrow {latex(a1*x+b1*y+c1)}=0$\n\n"\
		f"${{{d2}}}$ qua điểm $B({x_2};{y_2})$ và có véctơ chỉ phương là $\\overrightarrow{{u_2}}({-b2};{a2})$.\n\n"\
		f"Phương trình tổng quát của ${{{d2}}}$: ${a2}(x-{x_2})+{b2}(y-{y_2})=0\\Leftrightarrow {latex(a2*x+b2*y+c2)}=0$\n\n"\
		f"Do $\\dfrac{{{a1}}}{{{a2}}}=\\dfrac{{{b1}}}{{{b2}}}=\\dfrac{{{c1}}}{{{c2}}}$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ trùng nhau.".replace("+-","-").replace("--","+").replace("-+","-").replace("\\frac","\\dfrac")

	#Tạo giả thiết song song
	if chon==2:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])

		x_1=random.randint(-8,8)
		y_1=random.randint(-8,8)
		f1=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_1,b1)} \\\\ \
	y = {show_ptts(y_1,-a1)}\
	\\end{{array}} \\right."
		c1= -a1*x_1-b1*y_1

		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=t*a1
		b2= t*b1

		x_2=x_1+b1*t
		y_2=y_1+a1*t

		f2=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_2,-b2)} \\\\ \
	y = {show_ptts(y_2,a2)}\
	\\end{{array}} \\right."
		c2= -a2*x_2-b2*y_2
		

		kq=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		noi_dung_loigiai=f"${{{d1}}}$ qua điểm $A({x_1};{y_1})$ và có véctơ chỉ phương là $\\overrightarrow{{u_1}}({b1};{-a1})$.\n\n"\
		f"Phương trình tổng quát của ${{{d1}}}$: ${a1}(x-{x_1})+{b1}(y-{y_1})=0\\Leftrightarrow {latex(a1*x+b1*y+c1)}=0$\n\n"\
		f"${{{d2}}}$ qua điểm $B({x_2};{y_2})$ và có véctơ chỉ phương là $\\overrightarrow{{u_2}}({-b2};{a2})$.\n\n"\
		f"Phương trình tổng quát của ${{{d2}}}$: ${a2}(x-{x_2})+{b2}(y-{y_2})=0\\Leftrightarrow {latex(a2*x+b2*y+c2)}=0$\n\n"\
		f"Do $\\dfrac{{{a1}}}{{{a2}}}=\\dfrac{{{b1}}}{{{b2}}}\\ne \\dfrac{{{c1}}}{{{c2}}}$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ song song.".replace("+-","-").replace("--","+").replace("-+","-").replace("\\frac","\\dfrac")

	#Tạo giả thiết cắt không vuông góc

	if chon==3:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		x_1=random.randint(-8,8)
		y_1=random.randint(-8,8)
		f1=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_1,b1)} \\\\ \
	y = {show_ptts(y_1,-a1)}\
	\\end{{array}} \\right."
		c1= -a1*x_1-b1*y_1

		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=b1*t
		b2=a1*t

		x_2=random.randint(-6,6)
		y_2=random.randint(-6,6)

		f2=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_2,-b2)} \\\\ \
	y = {show_ptts(y_2,a2)}\
	\\end{{array}} \\right."
		c2= -a2*x_2-b2*y_2		

		kq=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		noi_dung_loigiai=f"${{{d1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}({b1};{-a1})$ nên có véctơ pháp tuyến là $\\overrightarrow{{n_1}}({a1};{b1})$.\n\n"\
		f"${{{d2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}({-b2};{a2})$ nên có véctơ pháp tuyến là $\\overrightarrow{{n_2}}({a2};{b2})$.\n\n"\
		f"Do $\\dfrac{{{a1}}}{{{a2}}} \\ne \\dfrac{{{b1}}}{{{b2}}}$ và ${show_tich(a1,a2)}+{show_tich(b1,b2)} \\ne 0$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ cắt nhau và ${{{d1}}}$ không vuông góc với ${{{d2}}}$.".replace("+-","-").replace("--","+").replace("-+","-").replace("\\frac","\\dfrac")

	if chon==4:
		a1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		c1= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		x_1=random.randint(-8,8)
		y_1=random.randint(-8,8)
		f1=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_1,b1)} \\\\ \
	y = {show_ptts(y_1,-a1)}\
	\\end{{array}} \\right."
		c1= -a1*x_1-b1*y_1

		t=random.choice([random.randint(-3, -1), random.randint(2, 4)])
		a2=-b1*t
		b2= a1*t

		x_2=random.randint(-6,6)
		y_2=random.randint(-6,6)

		f2=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_2,-b2)} \\\\ \
	y = {show_ptts(y_2,a2)}\
	\\end{{array}} \\right."
		c2= -a2*x_2-b2*y_2	

		
		kq=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và vuông góc"
		kq2=f"${{{d1}}}$ và ${{{d2}}}$ song song"
		kq3=f"${{{d1}}}$ và ${{{d2}}}$ trùng nhau"
		kq4=f"${{{d1}}}$ và ${{{d2}}}$ cắt nhau và không vuông góc"

		noi_dung_loigiai=f"${{{d1}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_1}}({b1};{-a1})$ nên có véctơ pháp tuyến là $\\overrightarrow{{n_1}}({a1};{b1})$.\n\n"\
		f"${{{d2}}}$ có véctơ chỉ phương là $\\overrightarrow{{u_2}}({-b2};{a2})$ nên có véctơ pháp tuyến là $\\overrightarrow{{n_2}}({a2};{b2})$.\n\n"\
		f"Do ${show_tich(a1,a2)}+{show_tich(b1,b2)} = 0$"\
		f" nên ${{{d1}}}$ và ${{{d2}}}$ vuông góc nhau.".replace("+-","-").replace("--","+").replace("-+","-").replace("\\frac","\\dfrac")


    #Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)

	noi_dung=f"Trong mặt phẳng tọa độ ${{Oxy}}$, cho hai đường thẳng ${d1}:{f1}$ và ${d2}:{f2}$."\
			 f" Xét vị trí tương đối của ${{{d1}}}$ và ${{{d2}}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D10_CX_B1_26]-TF-M2. Cho PTTQ của 1 đường thẳng, xét đúng-sai về VTCP,VTPT, điểm thuộc đường thẳng.   
def gghik_L10_CX_B1_26():
	x=sp.symbols("x")
	y=sp.symbols("y")
	d=["d","d_1","\\Delta","\\Delta_1"]
	i=random.randint(0,3)
	d = d[i]
	a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	x_0=random.randint(-8,8)
	y_0=random.randint(-8,8)
	f_ts=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,b)} \\\\ \
	y = {show_ptts(y_0,-a)}\
	\\end{{array}} \\right."

	f_tsfalse=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,a)} \\\\ \
	y = {show_ptts(y_0,b)}\
	\\end{{array}} \\right."

	c= -a*x_0-b*y_0

	f_tq=a*x+b*y+c
	noi_dung=f"Trong mặt phẳng ${{(Oxy)}}$, cho đường thẳng ${d}:{latex(a*x+b*y+c)}=0$. Xét tính đúng-sai của các khẳng định sau:"
	m,n=random.randint(2,15), random.randint(3,9)   
	if m==n: n=n+random.randint(1,5)
	kq1_T=f"*${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}({a};{b})$"
	kq1_F=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}({b};{-a})$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}({a};{b})$ là khẳng định đúng."
	if kq1==kq1_F:
		loigiai_1=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}({b};{-a})$ là khẳng định sai vì ${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}({a};{b})$."

	t=random.choice([random.randint(-2,-1),random.randint(1,2)])
	kq2_T=f"*${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*b};{-t*a})$"
	kq2_F=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*a};{t*b})$"
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*b};{-t*a})$ là khẳng định đúng vì ${{{d}}}$ có một véctơ chỉ phương là $({b};{-a})$."
	if kq2==kq2_F:
		loigiai_2=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*a};{t*b})$ là khẳng định sai vì ${{{d}}}$ có một véctơ chỉ phương là $({b};{-a})$."

	# kq3_T=f"*${{{d}}}$ có phương trình tham số là ${f_ts}$"
	# kq3_F=f"${{{d}}}$ có phương trình tham số là ${f_tsfalse}$"
	# kq3=random.choice([kq3_T, kq3_F])
	# loigiai_3=f"${{{d}}}$ có phương trình tham số là ${f_ts}$ là khẳng định đúng."\
	# f" Vì ${{{d}}}$ qua điểm $({x_0};{y_0})$ và nhận vectơ $\\vec{{n}}({a};{b})$ làm véctơ pháp tuyến thì nhận vectơ $\\vec{{u}}({b};{-a})$ làm véctơ chỉ phương."
	# if kq3==kq3_F:
	# 	loigiai_3=f"${{{d}}}$ có phương trình tham số là ${f_tsfalse}$ là khẳng định sai."\
	# 	f" Vì ${{{d}}}$ qua điểm $({x_0};{y_0})$ và nhận vectơ $\\vec{{n}}({a};{b})$ làm véctơ pháp tuyến thì nhận vectơ $\\vec{{u}}({b};{-a})$ làm véctơ chỉ phương."
	
	t=random.choice([random.randint(-2,-1),random.randint(1,2)])
	x_1,y_1=x_0+b*t, y_0-a*t
	t1=t+random.randint(1,3)
	x_2,y_2=x_0+b*t1, y_0+a*t1
	ten_diem=random.choice(["A","B","C","D"])	

	kq3_T=f"*Điểm ${ten_diem}({x_1};{y_1})$ thuộc đường thẳng ${{{d}}}$"
	kq3_F=f"Điểm ${ten_diem}({x_1};{y_1})$ không thuộc đường thẳng ${{{d}}}$"
	kq3=random.choice([kq3_T, kq3_F]) 
	loigiai_3=f"Điểm ${ten_diem}({x_1};{y_1})$ thuộc đường thẳng ${{{d}}}$ là khẳng định đúng vì tọa độ điểm ${{{ten_diem}}}$ thỏa mãn phương trình ${{{d}}}$." 
	if kq3==kq3_F:
		loigiai_3=f"Điểm ${ten_diem}({x_1};{y_1})$ không thuộc đường thẳng ${{{d}}}$ là khẳng định sai vì tọa độ điểm ${{{ten_diem}}}$ thỏa mãn phương trình ${{{d}}}$."
	
	
	ten_diem=random.choice(["M","N", "P", "Q"])
	kq4_T=f"*Điểm ${ten_diem}({x_2};{y_2})$ không thuộc đường thẳng ${{{d}}}$"
	kq4_F=f"Điểm ${ten_diem}({x_2};{y_2})$ thuộc đường thẳng ${{{d}}}$"
	kq4=random.choice([kq4_T, kq4_F]) 
	loigiai_4=f"Điểm ${ten_diem}({x_2};{y_2})$ không thuộc đường thẳng ${{{d}}}$ là khẳng định đúng vì tọa độ điểm ${{{ten_diem}}}$ không thỏa mãn phương trình ${{{d}}}$." 
	if kq4==kq4_F:
		loigiai_4=f"Điểm ${ten_diem}({x_2};{y_2})$ thuộc đường thẳng ${{{d}}}$ là khẳng định sai vì tọa độ điểm ${{{ten_diem}}}$ không thỏa mãn phương trình ${{{d}}}$."
	
	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_CX_B1_27]-TF-M2. Tạo câu đúng-sai: Cho PTTS của 1 đường thẳng, xét đúng-sai về VTCP,VTPT, điểm thuộc đường thẳng.   
def gghik_L10_CX_B1_27():
	x=sp.symbols("x")
	y=sp.symbols("y")
	d=["d","d_1","\\Delta","\\Delta_1"]
	i=random.randint(0,3)
	d = d[i]
	a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	x_0=random.randint(-8,8)
	y_0=random.randint(-8,8)
	f_ts=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,b)} \\\\ \
	y = {show_ptts(y_0,-a)}\
	\\end{{array}} \\right."

	f_tsfalse=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,a)} \\\\ \
	y = {show_ptts(y_0,b)}\
	\\end{{array}} \\right."

	c= -a*x_0-b*y_0
	f_tq=a*x+b*y+c

	noi_dung=f"Trong mặt phẳng ${{(Oxy)}}$, cho đường thẳng ${d}:{f_ts}$. Xét tính đúng-sai của các khẳng định sau:"
	m,n=random.randint(2,15), random.randint(3,9)   
	if m==n: n=n+random.randint(1,5)
	kq1_T=f"*${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({a};{b})$"
	kq1_F=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({b};{-a})$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({a};{b})$ là khẳng định đúng."\
	f"Vì ${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({b};{-a})$"
	if kq1==kq1_F:
		loigiai_1=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({b};{-a})$ là khẳng định sai vì $\\vec{{u}}=({b};{-a})$ là tọa độ véctơ chỉ phương của ${{{d}}}$."

	t=random.choice([random.randint(-3,-1),random.randint(1,3)])
	kq2_T=f"*${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*b};{-t*a})$"
	kq2_F=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*a};{t*b})$"
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*b};{-t*a})$ là khẳng định đúng vì ${{{d}}}$ có một véctơ chỉ phương là $({b};{-a})$."
	if kq2==kq2_F:
		loigiai_2=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*a};{t*b})$ là khẳng định sai vì ${{{d}}}$ có một véctơ chỉ phương là $({b};{-a})$."

	# kq3_T=f"*${{{d}}}$ có phương trình tham số là ${f_ts}$"
	# kq3_F=f"${{{d}}}$ có phương trình tham số là ${f_tsfalse}$"
	# kq3=random.choice([kq3_T, kq3_F])
	# loigiai_3=f"${{{d}}}$ có phương trình tham số là ${f_ts}$ là khẳng định đúng."\
	# f" Vì ${{{d}}}$ qua điểm $({x_0};{y_0})$ và nhận vectơ $\\vec{{n}}({a};{b})$ làm véctơ pháp tuyến thì nhận vectơ $\\vec{{u}}({b};{-a})$ làm véctơ chỉ phương."
	# if kq3==kq3_F:
	# 	loigiai_3=f"${{{d}}}$ có phương trình tham số là ${f_tsfalse}$ là khẳng định sai."\
	# 	f" Vì ${{{d}}}$ qua điểm $({x_0};{y_0})$ và nhận vectơ $\\vec{{n}}({a};{b})$ làm véctơ pháp tuyến thì nhận vectơ $\\vec{{u}}({b};{-a})$ làm véctơ chỉ phương."
	
	t=random.choice([random.randint(-3,-1),random.randint(1,3)])
	x_1,y_1=x_0+b*t, y_0-a*t
	x_2,y_2=x_0+a*t, y_0+b*t
	ten_diem=random.choice(["A","B","C","D"])	

	kq3_T=f"*Điểm ${ten_diem}({x_1};{y_1})$ thuộc đường thẳng ${{{d}}}$"
	kq3_F=f"Điểm ${ten_diem}({x_1};{y_1})$ không thuộc đường thẳng ${{{d}}}$"
	kq3=random.choice([kq3_T, kq3_F]) 
	loigiai_3=f"Điểm ${ten_diem}({x_1};{y_1})$ thuộc đường thẳng ${{{d}}}$ là khẳng định đúng vì có $t={t}$ vào phương trình thì $x={x_1},y={y_1}$." 
	if kq3==kq3_F:
		loigiai_3=f"Điểm ${ten_diem}({x_1};{y_1})$ không thuộc đường thẳng ${{{d}}}$ là khẳng định sai vì có $t={t}$ vào phương trình thì $x={x_1},y={y_1}$."


	ten_diem=random.choice(["M","N", "P", "Q"])
	kq4_T=f"*Điểm ${ten_diem}({x_2};{y_2})$ không thuộc đường thẳng ${{{d}}}$"
	kq4_F=f"Điểm ${ten_diem}({x_2};{y_2})$ thuộc đường thẳng ${{{d}}}$"
	kq4=random.choice([kq4_T, kq4_F]) 
	loigiai_4=f"Điểm ${ten_diem}({x_2};{y_2})$ không thuộc đường thẳng ${{{d}}}$ là khẳng định đúng vì không tồn tại ${{t}}$ thỏa mãn $x={x_1},y={y_1}$." 
	if kq4==kq4_F:
		loigiai_4=f"Điểm ${ten_diem}({x_2};{y_2})$ thuộc đường thẳng ${{{d}}}$ là khẳng định sai vì không tồn tại ${{t}}$ thỏa mãn $x={x_1},y={y_1}$."
	
	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_CX_B1_28]-TF-M2. Tạo câu đúng-sai: Cho PTTS của 1 đường thẳng, xét đúng-sai về VTCP, VTPT, PTTS, PTTQ.   
def gghik_L10_CX_B1_28():
	x=sp.symbols("x")
	y=sp.symbols("y")
	d=["d","d_1","\\Delta","\\Delta_1"]
	i=random.randint(0,3)
	d = d[i]
	a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	x_0=random.randint(-8,8)
	y_0=random.randint(-8,8)
	f_ts=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,b)} \\\\ \
	y = {show_ptts(y_0,-a)}\
	\\end{{array}} \\right."

	noi_dung=f"Trong mặt phẳng ${{(Oxy)}}$, cho đường thẳng ${d}:{f_ts}$. Xét tính đúng-sai của các khẳng định sau:"

	m,n=random.randint(2,15), random.randint(3,9)   
	if m==n: n=n+random.randint(1,5)
	kq1_T=f"*${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({a};{b})$"
	kq1_F=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({b};{-a})$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({a};{b})$ là khẳng định đúng."\
	f"Vì ${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({b};{-a})$"
	if kq1==kq1_F:
		loigiai_1=f"${{{d}}}$ có một véctơ pháp tuyến là $\\vec{{n}}=({b};{-a})$ là khẳng định sai vì $\\vec{{u}}=({b};{-a})$ là tọa độ véctơ chỉ phương của ${{{d}}}$."

	t=random.choice([random.randint(-3,-1),random.randint(1,3)])
	kq2_T=f"*${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*b};{-t*a})$"
	kq2_F=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*a};{t*b})$"
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*b};{-t*a})$ là khẳng định đúng vì ${{{d}}}$ có một véctơ chỉ phương là $({b};{-a})$."
	if kq2==kq2_F:
		loigiai_2=f"${{{d}}}$ có một véctơ chỉ phương là $\\vec{{u}}=({t*a};{t*b})$ là khẳng định sai vì ${{{d}}}$ có một véctơ chỉ phương là $({b};{-a})$."

	t=random.choice([random.randint(-3,-1),random.randint(2,5)])
	f_ts_1=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,b*t)} \\\\ \
	y = {show_ptts(y_0,-a*t)}\
	\\end{{array}} \\right."

	f_ts_false=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,a)} \\\\ \
	y = {show_ptts(y_0,b)}\
	\\end{{array}} \\right."

	kq3_T=f"*${{{d}}}$ có phương trình tham số là ${f_ts_1}$"
	kq3_F=f"${{{d}}}$ có phương trình tham số là ${f_ts_false}$"
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"${{{d}}}$ có phương trình tham số là ${f_ts_1}$ là khẳng định đúng.\n\n"\
	f" Vì ${{{d}}}$ qua điểm $({x_0};{y_0})$ và nhận vectơ $\\vec{{u}}=({b};{-a})$ làm véctơ chỉ phương thì cũng nhận vectơ $\\overrightarrow{{u_1}}=({b*t};{-a*t})$ làm véctơ chỉ phương."
	if kq3==kq3_F:
		loigiai_3=f"${{{d}}}$ có phương trình tham số là ${f_ts_false}$ là khẳng định sai.\n\n"\
		f" Vì ${{{d}}}$ nhận vectơ $\\vec{{u}}=({b};{-a})$ làm véctơ chỉ phương thì vectơ $\\overrightarrow{{u_1}}=({a};{b})$ không là một véctơ chỉ phương của ${{{d}}}$."
	
	c= -a*x_0-b*y_0
	f_tq=a*x+b*y+c
	f_tq_false=b*x-a*y+c

	kq4_T=f"*Phương trình tổng quát của đường thẳng ${{{d}}}$ là ${latex(f_tq)}=0$"
	kq4_F=f"Phương trình tổng quát của đường thẳng ${{{d}}}$ là ${latex(f_tq_false)}=0$"
	kq4=random.choice([kq4_T, kq4_F]) 
	loigiai_4=f"${{{d}}}$ qua điểm $({x_0};{y_0})$ nhận $\\vec{{u}}=({b};{-a})$ làm véctơ chỉ phương nên có véctơ pháp tuyến là $\\vec{{n}}=({a};{b})$.\n\n"\
	f"Phương trình tổng quát của ${{{d}}}:{a}(x-{x_0})+{b}(y-{y_0})=0 \\Leftrightarrow {latex(a*x+b*y+c)}=0$.".replace("-+","-").replace("--","+").replace("+-","-")  
	if kq4==kq4_F:
		loigiai_4=f"Phương trình tổng quát của đường thẳng ${{{d}}}$ là ${latex(f_tq_false)}=0$ là khẳng định sai.\n\n"\
		f"Vì ${{{d}}}$ nhận vectơ $\\vec{{u}}=({b};{-a})$ làm véctơ chỉ phương thì vectơ $\\overrightarrow{{u}}=({b};{-a})$ không là một véctơ pháp tuyến của ${{{d}}}$."
	
	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_CX_B1_29]-TF-M2. Tạo câu đúng-sai: Cho PTTQ của 1 đường thẳng, xét đúng-sai về vị trí tương đối.   
def gghik_L10_CX_B1_29():
	x=sp.symbols("x")
	y=sp.symbols("y")
	d=["d","\\Delta"]	
	i=random.randint(0,1)
	d = d[i]
	a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	c= random.randint(-10, 10)	
	f=a*x+b*y+c	
	noi_dung=f"Trong mặt phẳng ${{(Oxy)}}$, cho đường thẳng ${d}:{latex(f)}=0$. Xét tính đúng-sai của các khẳng định sau:"
	
	d1=["d_1","\\Delta_1"]
	d1 = d1[i]
	t=random.randint(1,100)
	f1=a*x+b*y+c+t
	kq1_T=f"*Đường thẳng ${{{d}}}$ song song với đường thẳng ${d1}: {latex(f1)}=0$"
	kq1_F=f"Đường thẳng ${{{d}}}$ không song song với đường thẳng ${d1}: {latex(f1)}=0$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"${{{d}}}$ song song với đường thẳng ${d1}: {latex(f1)}=0$ là khẳng định đúng.\n\n"\
	f" Vì $\\dfrac{{{a}}}{{{a}}}=\\dfrac{{{b}}}{{{b}}} \\ne \\dfrac{{{c}}}{{{c+t}}}$."
	if kq1==kq1_F:
		loigiai_1=f"${{{d}}}$ không song song với đường thẳng ${d1}: {latex(f1)}=0$ là khẳng định sai.\n\n"\
		f" Vì $\\dfrac{{{a}}}{{{a}}}=\\dfrac{{{b}}}{{{b}}} \\ne \\dfrac{{{c}}}{{{c+t}}}$ nên ${{{d}}}$ song song với ${{{d1}}}$."

	d2=["d_2","\\Delta_2"]
	d2 = d2[i]
	t=random.randint(1,100)
	if a**2==b**2: b=a+1
	f2=b*x+a*y+t
	kq2_T=f"*Đường thẳng ${{{d}}}$ cắt đường thẳng ${d2}: {latex(f2)}=0$"
	kq2_F=f"Đường thẳng ${{{d}}}$ và đường thẳng ${d2}: {latex(f2)}=0$ không cắt nhau"
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"${{{d}}}$ cắt đường thẳng ${d2}: {latex(f2)}=0$ là khẳng định đúng vì $\\dfrac{{{a}}}{{{b}}} \\ne \\dfrac{{{b}}}{{{a}}}$."
	if kq2==kq2_F:
		loigiai_2=f"${{{d}}}$ và đường thẳng ${d2}: {latex(f2)}=0$ không cắt nhau là khẳng định sai.\n\n"\
		f"Vì $\\dfrac{{{a}}}{{{b}}} \\ne \\dfrac{{{b}}}{{{a}}}$ nên ${{{d}}}$ và ${{{d2}}}$ cắt nhau."

	d3=["d_3","\\Delta_3"]
	d3 = d3[i]
	t=random.randint(1,100)	
	f3=b*x-a*y+t

	kq3_T=f"*Đường thẳng ${{{d}}}$ và đường thẳng ${d3}: {latex(f3)}=0$ vuông góc nhau"
	kq3_F=f"Đường thẳng ${{{d}}}$ và đường thẳng ${d3}: {latex(f3)}=0$ không vuông góc nhau"
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Đường thẳng ${{{d}}}$ và đường thẳng ${d3}: {latex(f3)}=0$ vuông góc nhau là khẳng định đúng "\
	f" vì ${show_tich(a,b)}+{show_tich(b,-a)}=0$."
	if kq3==kq3_F:
		loigiai_3=f"Đường thẳng ${{{d}}}$ và đường thẳng ${d3}: {latex(f3)}=0$ không vuông góc nhau là khẳng định sai.\n\n"\
		f"Vì ${show_tich(a,b)}+{show_tich(b,-a)}=0$ nên ${d}\\bot {d3}$."

	d4=["d_4","\\Delta_4"]
	d4 = d4[i]
	t=random.choice([random.randint(-5,-1), random.randint(1,5)])
	f4=a*t*x + b*t*y + c*t

	kq4_T=f"*Đường thẳng ${{{d}}}$ và đường thẳng ${d4}: {latex(f4)}=0$ trùng nhau"
	kq4_F=f"Đường thẳng ${{{d}}}$ và đường thẳng ${d4}: {latex(f4)}=0$ không trùng nhau"
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Đường thẳng ${{{d}}}$ và đường thẳng ${d4}: {latex(f4)}=0$ trùng nhau là khẳng định đúng.\n\n"\
	f"Vì $\\dfrac{{{a}}}{{{a*t}}}=\\dfrac{{{b}}}{{{b*t}}}=\\dfrac{{{c}}}{{{c*t}}}$."
	if kq4==kq4_F:
		loigiai_4=f"Đường thẳng ${{{d}}}$ và đường thẳng ${d4}: {latex(f4)}=0$ không trùng nhau là khẳng định sai.\n\n"\
	f"Vì $\\dfrac{{{a}}}{{{a*t}}}=\\dfrac{{{b}}}{{{b*t}}}=\\dfrac{{{c}}}{{{c*t}}}$ nên ${{{d}}} \\equiv {{{d4}}}$."

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]
	random.shuffle(list_PA)
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_CX_B1_30]-TF-M2. Tạo câu đúng-sai: Cho 1 điểm và PTTQ của 1 đường thẳng, xét đúng-sai về vị trí tương đối, khoảng cách.   
def gghik_L10_CX_B1_30():
	x=sp.symbols("x")
	y=sp.symbols("y")
	d=["d","\\Delta"]	
	i=random.randint(0,1)
	d = d[i]

	a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	
	x_0, y_0 =random.randint(-8,8), random.randint(-8,8)
	f_ts=f"\\left\\{{ \\begin{{array}}{{l}}\
	x = {show_ptts(x_0,b)} \\\\ \
	y = {show_ptts(y_0,-a)}\
	\\end{{array}} \\right."
	c=-a*x_0-b*y_0
	f=a*x+b*y+c
	ten_diem=random.choice(["A","B","C","M","N","P"])
	x_A, y_A=random.randint(-10,10), random.randint(-10,10)

	noi_dung=f"Trong mặt phẳng ${{(Oxy)}}$, cho điểm ${ten_diem}({x_A};{y_A})$ và đường thẳng ${d}:{latex(f)}=0$. Xét tính đúng-sai của các khẳng định sau:"

	kc_A_d=abs(a*x_A+b*y_A+c)/sqrt(a**2+b**2)
	kc_A_d_false=abs(a*x_A+b*y_A+c)/sqrt(abs(a)+abs(b))
	kq1_T=f"*Khoảng cách từ điểm ${ten_diem}({x_A};{y_A})$ đến đường thẳng ${{{d}}}$ bằng ${latex(kc_A_d)}$".replace("\\frac","\\dfrac")
	kq1_F=f"Khoảng cách từ điểm ${ten_diem}({x_A};{y_A})$ đến đường thẳng ${{{d}}}$ bằng ${latex(kc_A_d_false)}$".replace("\\frac","\\dfrac")
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Khoảng cách từ điểm ${ten_diem}({x_A};{y_A})$ đến đường thẳng ${{{d}}}$ bằng ${latex(kc_A_d)}$ là khẳng định đúng.\n\n"\
	f" Vì $d({ten_diem},{d})=\\dfrac{{|{show_tich(a,x_A)} + {show_tich(b,y_A)} + {c}|}} {{ \\sqrt{{ {a**2}+{b**2} }} }}={latex(kc_A_d)}$."
	if kq1==kq1_F:
		loigiai_1=f"Khoảng cách từ điểm ${ten_diem}({x_A};{y_A})$ đến đường thẳng ${{{d}}}$ bằng ${latex(kc_A_d_false)}$ là khẳng định sai.\n\n"\
		f" $d({ten_diem},{d})=\\dfrac{{|{show_tich(a,x_A)} + {show_tich(b,y_A)} + {c}|}} {{ \\sqrt{{ {a**2}+{b**2} }} }}={latex(kc_A_d)}$."
	loigiai_1=thay_dau_congtru(loigiai_1).replace("\\frac","\\dfrac")

	kc_O_d=abs(c)/sqrt(a**2+b**2)
	kc_O_d_false=abs(c)/sqrt(abs(a)+abs(b))

	kq2_T=f"*Khoảng cách từ gốc tọa độ ${{O}}$ đến đường thẳng ${{{d}}}$ bằng ${latex(kc_O_d)}$".replace("\\frac","\\dfrac")
	kq2_F=f"Khoảng cách từ gốc tọa độ ${{O}}$  đến đường thẳng ${{{d}}}$ bằng ${latex(kc_O_d_false)}$".replace("\\frac","\\dfrac")
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khoảng cách từ gốc tọa độ ${{O}}$  đến đường thẳng ${{{d}}}$ bằng ${latex(kc_O_d)}$ là khẳng định đúng.\n\n"\
	f"Vì $d(O,{d})=\\dfrac{{|{c}|}} {{ \\sqrt{{ {a**2}+{b**2} }} }}={latex(kc_O_d)}$."
	if kq2==kq2_F:
		loigiai_2=f" Khoảng cách từ gốc tọa độ ${{O}}$  đến đường thẳng ${{{d}}}$ bằng ${latex(kc_O_d_false)}$ là khẳng định sai.\n\n"\
		f"Vì $d(O,{d})=\\dfrac{{|{c}|}} {{ \\sqrt{{ {a**2}+{b**2} }} }}={latex(kc_O_d)}$."
	loigiai_2=thay_dau_congtru(loigiai_2).replace("\\frac","\\dfrac")

	OA=sqrt(x_A**2+y_A**2)
	OA_false=sqrt(abs(x_A)+abs(y_A))
	if OA_false==OA: OA_false=abs(x_A)+abs(y_A)

	kq3_T=f"*Khoảng cách từ gốc tọa độ ${{O}}$ đến điểm ${{{ten_diem}}}$ bằng ${latex(OA)}$"
	kq3_F=f"Khoảng cách từ gốc tọa độ ${{O}}$ đến điểm ${{{ten_diem}}}$ bằng ${latex(OA_false)}$"
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Khoảng cách từ gốc tọa độ ${{O}}$ đến điểm ${{{ten_diem}}}$ bằng ${latex(OA)}$ là khẳng định đúng.\n\n"\
	f"Vì $OA=\\sqrt{{({x_A})^2 +({y_A})^2 }}={latex(OA)}$."
	if kq3==kq3_F:
		loigiai_3=f"Khoảng cách từ gốc tọa độ ${{O}}$ đến điểm ${{{ten_diem}}}$ bằng ${latex(OA_false)}$ là khẳng định sai.\n\n"\
		f"Vì $OA=\\sqrt{{({x_A})^2 +({y_A})^2 }}={latex(OA)}$."
	loigiai_3=thay_dau_congtru(loigiai_3).replace("\\frac","\\dfrac")

	# Giải hệ phương trình
	x, y = symbols('x y')
	
	eq1 = Eq(a*x + b*y, -c)
	eq2 = Eq(b*x - a*y, b*x_A+a*y_A)

	# Giải hệ phương trình
	solution = linsolve((eq1, eq2), x, y)

	# Biểu diễn nghiệm dưới dạng LaTeX
	latex_solution = latex(solution)

	kq4_T=f"*Hình chiếu vuông góc của điểm ${{{ten_diem}}}$ trên đường thẳng ${{{d}}}$ là điểm $H{latex_solution}$".replace("\\left\\{\\left(", "\\left(").replace("\\right)\\right\\}", "\\right)").replace(",", ";")
	kq4_F=f"Hình chiếu vuông góc của điểm ${{{ten_diem}}}$ trên đường thẳng ${{{d}}}$ là điểm $H{random.choice([f'(0;{y_A})',f'({x_A};0)'])}$".replace("\\left\\{\\left(", "\\left(").replace("\\right)\\right\\}", "\\right)").replace(",", ";")
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"Hình chiếu vuông góc của điểm ${{{ten_diem}}}$ trên đường thẳng ${{{d}}}$ là điểm $H{latex_solution}$ là khẳng định đúng.\n\n"\
	f"Đường thẳng ${ten_diem}H$ qua ${ten_diem}({x_A};{y_A})$ và vuông góc với đường thẳng ${{{d}}}$ có phương trình:\n\n"\
	f"${b}(x-{x_A})+{-a}(y-{y_A})=0 \\Leftrightarrow {latex(b*(x-x_A)-a*(y-y_A))}=0$.\n\n"\
	f"Tọa độ điểm ${{H}}$ là nghiệm của hệ phương trình:\n\n "\
	f"$\\left\\{{ \\begin{{array}}{{l}}\n\
{a}x + {b}y = {-c}\\\\ \n\
{b}x + {-a}y = {b*x_A-a*y_A} \n\
\\end{{array}} \\right. \\Rightarrow (x;y)={latex_solution}$."
	if kq4==kq4_F:
		loigiai_4=f"Hình chiếu vuông góc của điểm ${{{ten_diem}}}$ trên đường thẳng ${{{d}}}$ là điểm $H{random.choice([f'(0;{y_A})',f'({x_A};0)'])}$ là khẳng định sai.\n\n"\
	f"Đường thẳng ${ten_diem}H$ qua ${ten_diem}({x_A};{y_A})$ và vuông góc với đường thẳng ${{{d}}}$ có phương trình:\n\n"\
	f"${b}(x-{x_A})+{-a}(y-{y_A})=0 \\Leftrightarrow {latex(b*(x-x_A)-a*(y-y_A))}=0$.\n\n"\
	f"Tọa độ điểm ${{H}}$ là nghiệm của hệ phương trình:\n\n "\
	f"$\\left\\{{ \\begin{{array}}{{l}}\n\
{a}x + {b}y = {-c}\\\\ \n\
{b}x + {-a}y = {b*x_A-a*y_A} \n\
\\end{{array}} \\right. \\Rightarrow (x;y)={latex_solution}$."
	loigiai_4=thay_dau_congtru(loigiai_4).replace("\\left\\{\\left(", "\\left(").replace("\\right)\\right\\}", "\\right)").replace(",", ";")

	#Trộn các phương án
	list_PA =[kq1, kq2, kq3, kq4]	
	random.shuffle(list_PA)	
	list_TF=my_module.tra_ve_TF(list_PA)
	dap_an=f"{list_TF[0]}{list_TF[1]}{list_TF[2]}{list_TF[3]}".replace("đúng","Đ").replace("sai","S")

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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_CX_B1_31]. Tìm A thuộc đường thẳng d cách B một khoảng cho trước.
def gghik_L10_CX_B1_31():
	x,y=sp.symbols("x y")
	a= random.choice([random.randint(-6, -1), random.randint(1, 6)])
	b= random.choice([random.randint(-6, -1), random.randint(1, 6)])
	x_0=random.choice([random.randint(-7, -1), random.randint(1, 7)])
	y_0=a*x_0+b

	x_1= random.choice([random.randint(-6, -1), random.randint(1, 6)])
	y_1= random.choice([random.randint(-6, -1), random.randint(1, 6)])
	if x_1==x_0: x_1=x_1+random.randint(1,3)

	r=sqrt((x_0-x_1)**2+(y_0-y_1)**2)

	m= random.choice([random.randint(-10, -1), random.randint(1, 10)])
	n= random.choice([random.randint(-10, -1), random.randint(1, 10)])

	eq = Eq((x_1-x)**2+(y_1-a*x-b)**2,r**2)
	tap_nghiem=solve(eq,x)
	if len(tap_nghiem)==1:
		x_0=tap_nghiem[0]
		nghiem=f"x={phan_so(x_0)}"
	else:
		x_0=min(tap_nghiem[0],tap_nghiem[1])
		nghiem=f"x={phan_so(tap_nghiem[0])},x={phan_so(tap_nghiem[1])}"
	
	kq= m*x_0+n*y_0
	kq2=m*x_0-n*y_0
	kq3=kq+random.randint(1,5)
	kq4=kq2-random.randint(1,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]


	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)  
	dap_an=my_module.tra_ve_dap_an(list_PA)
	diem_A=random.choice(["A","M","C"])
	diem_B=random.choice(["B","N","Q","D"])
	

	noi_dung=thay_dau_congtru(f"Trong các điểm thuộc đường thẳng $d:{latex(a*x-y+b)}=0$ cho khoảng cách từ điểm đó đến điểm ${{{diem_B}}}$ bằng ${latex(r)}$ với ${diem_B}({x_1};{y_1})$,"\
	f" gọi ${diem_A}(a;b)$ là điểm có hoành độ nhỏ nhất. Tính $P={m}a+{n}b$.")
	noi_dung_loigiai=thay_dau_congtru(f"${latex(a*x-y+b)}=0\\Leftrightarrow y={latex(a*x+b)}$. Gọi ${diem_A}(x;{latex(a*x+b)})\\in d$.\n\n"\
	f" Khi đó: ${diem_A}{diem_B}={latex(sqrt((x_1-x)**2+(y_1-a*x-b)**2))}={latex(r)}$"\
	f"$\\Leftrightarrow {latex((x_1-x)**2+(y_1-a*x-b)**2)}={r**2}$\n\n"\
	f"$\\Rightarrow {nghiem}$. Do ${{{diem_A}}}$ có hoành độ nhỏ nhất nên $x={phan_so(x_0)} \\Rightarrow A({phan_so(x_0)};{phan_so(a*x_0+b)})$.\n\n"\
	f"Do đó: $P={m}a+{n}b={kq}$.")

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

#Bài 3 - Phương trình đường tròn

#[D10_CX_B3_01]. Viết phương trình đường tròn có tâm và bán kính
def gghik_L10_CX_B3_01():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    lits_r=[sqrt(i) for i in range(1,101)]
    r=random.choice(lits_r)
    a,b = [random.randint(-10,10) for i in range(2)]
    if a==b==0:
        a=random.randint(1,5)        

    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, phương trình đường tròn ${{(C)}}$ có tâm ${{I({a};{b})}}$"\
                f" và bán kính ${{R}}={latex(r)}$ là"

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}={latex(r**2)}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}={latex(r**2)}"
    kq3=f"{latex((x+a)**2)}+{latex((y+b)**2)}={latex(r)}"
    kq4=f"{latex((x-a)**2)}+{latex((y-b)**2)}={latex(4*r**2)}"

    noi_dung_loigiai=f"Đường tròn ${{(S)}}$ có phương trình là: ${kq}$."    

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.\n    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

      
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

#[D10_CX_B3_02]-M1. Đọc tọa độ tâm từ phương trình đường tròn thu gọn
def gghik_L10_CX_B3_02():
	#Tạo bậc ngẫu nhiên
	x,y=sp.symbols("x y")
	lits_r=[sqrt(i) for i in range(1,101)]
	r=random.choice(lits_r)
	chon=random.randint(1,3)
	
	if chon==1:
		a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])	        

		noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{latex((x-a)**2)}+{latex((y-b)**2)}={latex(r**2)}$."\
		            f" Tọa độ tâm ${{I}}$ của đường tròn ${{(C)}}$ là"
		kq= f"{{I({a};{b})}}"
		kq2=f"{{I({-a};{-b})}}"
		kq3=random.choice([f"{{I({a};{-b})}}", f"{{I({b};{a})}}", f"{{I({-b};{-a})}}"])
		kq4=random.choice([f"{{I({-a};{b})}}"])

	if chon==2:
		a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b= 0       
		noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{latex((x-a)**2)}+{latex((y-b)**2)}={latex(r**2)}$."\
		            f" Tọa độ tâm ${{I}}$ của đường tròn ${{(C)}}$ là"
		kq= f"{{I({a};0)}}"
		kq2=f"{{I({-a};0)}}"
		kq3=random.choice([f"{{I(0;{a})}}"])
		kq4=random.choice([f"{{I(0;{-a})}}"])

	if chon==3:
		a= 0
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])	           

		noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{latex((x-a)**2)}+{latex((y-b)**2)}={latex(r**2)}$."\
		            f" Tọa độ tâm ${{I}}$ của đường tròn ${{(C)}}$ là"
		kq= f"{{I(0;{b})}}"
		kq2=f"{{I(0;{-b})}}"
		kq3=random.choice([f"{{I({b};0)}}"])
		kq4=random.choice([f"{{I({-b};0)}}"])

	noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tọa độ tâm là: ${kq}$."    

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B3_03]-M1. Đọc bán kính từ phương trình đường tròn thu gọn
def gghik_L10_CX_B3_03():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    lits_r=[i for i in range(1,50)]
    r=random.choice(lits_r)
    a,b,c = [random.randint(-10,10) for i in range(3)]
    if a==b==c==0:
        b=random.randint(1,5)
        c=random.randint(-10,-1) 

    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{latex((x-a)**2)}+{latex((y-b)**2)}={latex(r**2)}$."\
                f" Bán kính của đường tròn ${{(C)}}$ là"

    kq=r
    kq2=r**2
    kq3=sqrt(r)
    kq4=2*r

    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]

    kq= f"{{R={latex(kq)}}}"
    kq2=f"{{R={latex(kq2)}}}"
    kq3=f"{{R={latex(kq3)}}}"
    kq4=f"{{R={latex(kq4)}}}"

    noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tọa độ bán kính là: $R=\\sqrt{{{latex(r**2)}}}={latex(r)}$."    

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D10_CX_B3_04]-M1. Đọc tọa độ tâm từ phương trình đường tròn khai triển
def gghik_L10_CX_B3_04():
    
	x,y,z=sp.symbols("x y z")
	lits_r=[sqrt(i) for i in range(1,101)]
	r=random.choice(lits_r)
   
	chon=random.randint(1,3)
	
	if chon==1:
		a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])	        

		noi_dung= thay_dau_congtru(f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:x^2+y^2+{latex(-2*a*x)}+{latex(-2*b*y)}+{latex(a**2+b**2-r**2)}=0$."\
		            f" Tọa độ tâm ${{I}}$ của đường tròn ${{(C)}}$ là")
		kq= f"{{I({a};{b})}}"
		kq2=f"{{I({-a};{-b})}}"
		kq3=random.choice([f"{{I({a};{-b})}}", f"{{I({b};{a})}}", f"{{I({-b};{-a})}}"])
		kq4=random.choice([f"{{I({-a};{b})}}"])

	if chon==2:
		a= random.choice([random.randint(-10, -1), random.randint(1, 10)])
		b= 0       
		noi_dung= thay_dau_congtru(f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:x^2+y^2+{latex(-2*a*x)}+{latex(a**2+b**2-r**2)}=0$."\
		            f" Tọa độ tâm ${{I}}$ của đường tròn ${{(C)}}$ là")
		kq= f"{{I({a};0)}}"
		kq2=f"{{I({-a};0)}}"
		kq3=random.choice([f"{{I(0;{a})}}"])
		kq4=random.choice([f"{{I(0;{-a})}}"])

	if chon==3:
		a= 0
		b= random.choice([random.randint(-10, -1), random.randint(1, 10)])	           

		noi_dung= thay_dau_congtru(f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:x^2+y^2+{latex(-2*b*y)}+{latex(a**2+b**2-r**2)}=0$."\
		            f" Tọa độ tâm ${{I}}$ của đường tròn ${{(C)}}$ là")
		kq= f"{{I(0;{b})}}"
		kq2=f"{{I(0;{-b})}}"
		kq3=random.choice([f"{{I({b};0)}}"])
		kq4=random.choice([f"{{I({-b};0)}}"])

	noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tọa độ tâm là: ${kq}$."    

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B3_05]-M2. Đọc bán kính từ phương trình đường tròn khai triển
def gghik_L10_CX_B3_05():
    
    x,y,z=sp.symbols("x y z")
    a,b = [random.choice([random.randint(-10, -1), random.randint(1, 10)]) for i in range(2)]  
    
    d=a**2 +b**2 -random.randint(1,30)
    dau_a, dau_b, dau_d = tao_dau(-a),tao_dau(-b), tao_dau(d)
    if a!=0:
        hs_ax=latex(-2*a*x)
    else:
        hs_ax=""

    if b!=0:
        hs_by=latex(-2*b*y)
    else:
        hs_by=""    

    if d!=0:
        hs_d=d
    else:
        hs_d=""
    ptmc=f"x^2+y^2{dau_a}{hs_ax} {dau_b}{hs_by} {dau_d}{d} =0"

    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{ptmc}$."\
                f" Bán kính của đường tròn ${{(C)}}$ là"
    kq=sqrt(a**2 +b**2 -d)
    kq2=sqrt(a**2 +b**2 )
    kq3=sqrt(abs(a) +abs(b) + abs(d))
    kq4=a**2 +b**2 -d
    pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
    kq2=pa_kotrung[1]
    kq3=pa_kotrung[2]
    kq4=pa_kotrung[3]


    noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có bán kính là:"\
        f" $R=\\sqrt{{{tao_ngoac(a)}^2 + {tao_ngoac(b)}^2 -{tao_ngoac(d)}}}={latex(sqrt(a**2 +b**2 -d))}$."    

    #Tạo các phương án
    pa_A= f"*$R={latex(kq)}$"
    pa_B= f"$R={latex(kq2)}$"
    pa_C= f"$R={latex(kq3)}$"
    pa_D= f"$R={latex(kq4)}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
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

#[D10_CX_B3_06]-M2. Viết phương trình đường tròn có tâm và đường kính
def gghik_L10_CX_B3_06():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    lits_r=[i for i in range(1,101)]
    r=random.choice(lits_r)
    a,b = [random.choice([random.randint(-10, -1), random.randint(1, 10)]) for i in range(2)]        

    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, đường tròn ${{(C)}}$ tâm ${{I({a};{b})}}$"\
                f" và đường kính bằng ${{{latex(2*r)}}}$ có phương trình là"

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}={latex(r**2)}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}={latex(r**2)}"
    kq3=f"{latex((x+a)**2)}+{latex((y+b)**2)}={latex(r)}"
    kq4=f"{latex((x-a)**2)}+{latex((y-b)**2)}={latex(4*r**2)}"

    noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tâm ${{I({a};{b})}}$ và bán kính $R=\\dfrac{{{latex(2*r)}}}{{2}}={latex(r)}$.\n\n"\
                f"Phương trình đường tròn: ${kq}$."

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

      
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

#[D10_CX_B3_07]-M3. Viết phương trình đường tròn có đường kính AB
def gghik_L10_CX_B3_07():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    diem_A=["A","M","P","C"]
    diem_B=["B","N","Q","D"]
    i=random.randint(0,3)
    diem_A,diem_B =diem_A[i], diem_B[i]

    a1,a2= [random.randint(-10,10) for i in range(2)]
    if a1==a2==0:
        a1=random.choice([random.randint(-10, -1), random.randint(1, 10)])         
    
    a,b = [random.randint(-10,10) for i in range(2)]
    if a==b==0:
        b=random.choice([random.randint(-10, -1), random.randint(1, 10)])
    if a==a1: a=a+1  
       
    b1, b2= 2*a-a1, 2*b-a2
   
    r=sqrt((a1-b1)**2+(a2-b2)**2)/2

    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, viết phương trình đường tròn ${{(C)}}$ có đường kính ${{{diem_A}{diem_B}}}$"\
                f" với ${diem_A}({a1};{a2}),{diem_B}({b1};{b2})$."

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}={latex(r**2)}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}={latex(r**2)}"
    kq3=f"{latex((x+a)**2)}+{latex((y+b)**2)}={latex(r)}"
    kq4=f"{latex((x-a)**2)}+{latex((y-b)**2)}={latex(4*r**2)}"

    noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tâm ${{I({a};{b})}}$ là trung điểm của đoạn thẳng ${{{diem_A}{diem_B}}}$. \n\n"\
    f"${{{diem_A}{diem_B}}}=\\sqrt{{\\left({show_hieu(b1,a1)}\\right)^2 + \\left({show_hieu(b2,a2)}\\right)^2 }}= {latex(sqrt((a1-b1)**2+(a2-b2)**2))}$.\n\n"\
    f" ${{(C)}}$ có bán kính $R=\\dfrac{{{diem_A}{diem_B}}}{{2}}={latex(r)}$.\n\n"\
    f"Phương trình đường tròn: ${kq}$."

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

      
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

#[D10_CX_B3_08]-M3. Viết phương trình đường tròn đi qua 3 điểm
def gghik_L10_CX_B3_08():
    #Tạo bậc ngẫu nhiên
    x,y,z,a,b=sp.symbols("x y z a b")
    diem_A=["A","M","D","B", "C"]
    diem_B=["B","N","E","C", "D"]
    diem_C=["C","P","F","D", "E"]
    i=random.randint(0,4)
    diem_A,diem_B,diem_C =diem_A[i], diem_B[i], diem_C[i]

    x=sp.symbols("x")
    y=sp.symbols("y")
    
    #Tạo tọa độ tâm và bán kính  đường tròn tùy ý
    x_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    y_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
    r=random.randint(1,10)

    #Tìm các điểm có tọa độ nguyên và thuộc đường tròn và lưu vào list điểm
    list_diem=[]
    for x_0 in range(-20,20):
        for y_0 in range(-20,20):
            if (x_0-x_I)**2+(y_0-y_I)**2==r**2:
                list_diem.append([x_0, y_0])

    #Lấy 3 cặp tọa độ đầu tiên đã lưu trong list lưu vào bien diem_A,diem_B,diem_C
    diem_A, diem_B, diem_C = list_diem[0],list_diem[1], list_diem[2]
    x_A, y_A = diem_A[0], diem_A[1]
    x_B, y_B = diem_B[0], diem_B[1]
    x_C, y_C = diem_C[0], diem_C[1]


    print(f"$({latex((x-x_I)**2)}+({latex((y-y_I)**2)})={r**2}$")
    

    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}$ đi qua ba điểm $A({x_A};{y_A}), B({x_B};{y_B})$ và $C({x_C};{y_C})$. Phương trình đường tròn ${{(C)}}$ là"

    kq= f"{latex((x-x_I)**2)}+{latex((y-y_I)**2)}={r**2}"
    kq2=f"{latex((x+x_I)**2)}+{latex((y+y_I)**2)}={r}"
    kq3=f" {latex((x+x_I)**2)}+{latex((y+y_I)**2)}={latex(my_module.hien_phan_so(r/2))}"
    kq4=f"{latex((x-x_I)**2)}+{latex((y-y_I)**2)}={4*r**2}"

    noi_dung_loigiai=my_module.thay_dau_congtru(f"Giả sử phương trình đường tròn ${{(C)}}$ có dạng: $x^2+y^2+ax+by+c=0$. \n\n"\
        f"Đường tròn đi qua ba điểm $A({x_A};{y_A}), B({x_B};{y_B}), C({x_C};{y_C})$ nên ta có:\n\n"\
        f"$\\left\\{{ \\begin{{array}}{{l}}\
{x_A**2}+{y_A**2}+a.{tao_ngoac(x_A)}+b.{tao_ngoac(y_A)}+c=0\\\\ \
{x_B**2}+{y_B**2}+a.{tao_ngoac(x_B)}+b.{tao_ngoac(y_B)}+c=0\\\\ \
{x_C**2}+{y_C**2}+a.{tao_ngoac(x_C)}+b.{tao_ngoac(y_C)}+c=0\
\\end{{array}} \\right.$\n"\
f"$\\Leftrightarrow\\left\\{{ \\begin{{array}}{{l}}\
{latex(x_A*a)}+{latex(y_A*b)}+c={-x_A**2-y_A**2}\\\\ \
{latex(x_B*a)}+{latex(y_B*b)}+c={-x_B**2-y_B**2}\\\\ \
{latex(x_C*a)}+{latex(y_C*b)}+c={-x_C**2-y_C**2}\
\\end{{array}} \\right.$\n\n"\
f"Giải hệ ta được: $a={-2*x_I}, b={-2*y_I},c={x_I**2+y_I**2-r**2}$.\n\n"\
f"Đường tròn có tâm $I({x_I};{y_I})$ và bán kính $R=\\sqrt{{{tao_ngoac(x_I)}^2+{tao_ngoac(y_I)}^2-{x_I**2+y_I**2-r**2}}}={r}$.\n\n"\
f"Phương trình đường tròn là: ${kq}$.")


    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

      
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


#[D10_CX_B3_09]-M2. Viết tiếp tuyến của đường tròn tại điểm (x_0;y_0)
def gghik_L10_CX_B3_09():
    #Tạo bậc ngẫu nhiên
    #Tạo bậc ngẫu nhiên
	x,y,z,a,b=sp.symbols("x y z a b")
	i=random.randint(0,4)
	
	x=sp.symbols("x")
	y=sp.symbols("y")

	chon=random.randint(1,2)
	
	if chon==1:
		x_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		y_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		r=random.randint(2,10)

		#Tìm các điểm có tọa độ nguyên và thuộc đường tròn và lưu vào list điểm
		list_diem=[]
		for x_0 in range(-20,20):
			for y_0 in range(-20,20):
				if (x_0-x_I)**2+(y_0-y_I)**2==r**2:
					list_diem.append([x_0, y_0])

		#Lấy 3 cặp tọa độ đầu tiên đã lưu trong list lưu vào bien diem_A,diem_B,diem_C
		diem_A, diem_B, diem_C = list_diem[0],list_diem[1], list_diem[2]
		x_A, y_A = diem_A[0], diem_A[1]
		x_B, y_B = diem_B[0], diem_B[1]
		x_C, y_C = diem_C[0], diem_C[1]

	if chon==2:
	#Tạo tọa độ tâm và bán kính đường tròn tùy ý
		x_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		y_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		#r=random.randint(2,10)

		#Tìm các điểm có tọa độ nguyên và thuộc đường tròn và lưu vào list điểm
		list_diem=[]
		for r in range (1,10):
			for x_0 in range(-20,20):
				for y_0 in range(-20,20):
					if (x_0-x_I)**2+(y_0-y_I)**2==r**2:
						if x_0!= x_I and y_0!=y_I:
							list_diem.append([x_0, y_0,r])
							r_final=r

		#Lấy 3 cặp tọa độ đầu tiên đã lưu trong list lưu vào bien diem_A,diem_B,diem_C
		diem_A, diem_B, diem_C = list_diem[0],list_diem[1], list_diem[2]
		x_A, y_A = diem_A[0], diem_A[1]
		x_B, y_B = diem_B[0], diem_B[1]
		x_C, y_C = diem_C[0], diem_C[1]
		r=r_final

	ten_diem=random.choice(["A", "B", "D","E", "M", "N"])
	a, b=x_A, y_A
	ucln=math.gcd(x_I-a,y_I-b)
	a1,b1=int((x_I-a)/ucln), int((y_I-b)/ucln)
	   
	noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, đường tròn ${{(C)}}:{latex((x-x_I)**2)}+{latex((y-y_I)**2)}={r**2}$. "\
	            f"Phương trình tiếp tuyến của đường tròn ${{(C)}}$ tại điểm ${ten_diem}({a};{b})$ là"

	kq= f"{latex(expand(a1*(x-a)+b1*(y-b)))}=0"
	kq2=f"{latex(expand(a1*x+b1*y-a1*a-b1*b+random.randint(1,10)))}=0"
	kq3=f"{latex(expand(b1*(x-a)-a1*(y-b)))}=0"
	kq4=f"{latex(expand(b1*x-a1*y-b1*a+a1*b-random.randint(1,10)))}=0"

	noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tâm ${{I({x_I};{y_I})}}$ và bán kính $R={latex(r)}$.\n\n"\
	f"Tiếp tuyến tại điểm ${ten_diem}({a};{b})$ nhận vectơ $\\overrightarrow{{{ten_diem}I}}=({x_I-a};{y_I-b})$ làm một véctơ pháp tuyến.\n\n"\
	f"Phương trình tiếp tuyến là: ${x_I-a}({latex(x-a)})+{y_I-b}({latex(y-b)})=0\\Leftrightarrow {latex(expand(a1*(x-a)+b1*(y-b)))}=0$.".replace("+-","-")

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t\t     D. { list_PA[3]}.\n"

	  
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

#[D10_CX_B3_10]-M2. Viết tiếp tuyến của đường tròn song song với đường thẳng
def gghik_L10_CX_B3_10():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    diem_A=random.choice(["A","B","M","N","P"])
    x_I,y_I = [random.randint(-8,8) for i in range(2)]
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    a,b = [random.choice([random.randint(-5, -1), random.randint(1, 5)]) for i in range(2)]
    ucln=math.gcd(a,b)
    a, b = int(a/ucln), int(b/ucln)

    r=random.randint(1,10)
    c=-a*x_I-b*y_I +random.randint(1,5)
    c1=r*sqrt(a**2+b**2)-a*x_I-b*y_I
    c2=-r*sqrt(a**2+b**2)-a*x_I-b*y_I  
       
    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{latex((x-x_I)**2)}+{latex((y-y_I)**2)}={r**2}$.\n\n"\
                f"Phương trình tiếp tuyến của đường tròn ${{(C)}}$ song song với đường thẳng $d:{latex(a*x+b*y+c)}=0$ là"

    kq= f"${latex(a*x+b*y+c1)}=0$ hoặc ${latex(a*x+b*y+c2)}=0$"
    kq2=f"${latex(b*x-a*y+c1)}=0$ hoặc ${latex(b*x-a*y+c2)}=0$"
    kq3=f"${latex(b*x-a*y+c)}=0$ hoặc ${latex(b*x-a*y-c)}=0$"
    kq4=f"${latex(a*x+b*y+c1+random.randint(1,4))}=0$ hoặc ${latex(a*x+b*y+c2+random.randint(1,4))}=0$"

    noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tâm ${{I({x_I};{y_I})}}$ và bán kính $R={latex(r)}$.\n\n"\
    f"Đường thẳng $\\Delta$ song song với $d:{latex(a*x+b*y+c)}=0$ nên có phương trình dạng ${latex(a*x+b*y)}+c=0$.\n\n"\
    f"$\\Delta$ tiếp xúc với ${{(C)}} \\Leftrightarrow d(I,\\Delta)=R "\
    f"\\Leftrightarrow \\dfrac{{|{show_tich(a,x_I)} + {show_tich(b,y_I)} +c|}} {{{latex(sqrt(a**2+b**2))}}}={r}$\n\n"\
    f"$\\Leftrightarrow |c+{latex(a*x_I+b*y_I)}|={latex(r*sqrt(a**2+b**2))} \\Leftrightarrow c={latex(c1)}, c={latex(c2)}$.\n\n"\
    f"Phương trình các đường tiếp tuyến là: {kq}.".replace("+-","-")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n    D. { list_PA[3]}.\n"

      
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

#[D10_CX_B3_11]-M3. Viết tiếp tuyến của đường tròn vuông góc với đường thẳng
def gghik_L10_CX_B3_11():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    diem_A=random.choice(["A","B","M","N","P"])
    x_I,y_I = [random.randint(-8,8) for i in range(2)]
    a = random.choice([random.randint(-10, -1), random.randint(1, 10)])

    a,b = [random.choice([random.randint(-5, -1), random.randint(1, 5)]) for i in range(2)]
    ucln=math.gcd(a,b)
    a, b = int(a/ucln), int(b/ucln)

    r=random.randint(1,10)
    c=-a*x_I-b*y_I +random.randint(1,5)
    c1=r*sqrt(a**2+b**2)-a*x_I-b*y_I
    c2=-r*sqrt(a**2+b**2)-a*x_I-b*y_I
    m=random.randint(1,10)
       
    noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{latex((x-x_I)**2)}+{latex((y-y_I)**2)}={r**2}$.\n\n"\
                f"Phương trình tiếp tuyến của đường tròn ${{(C)}}$ vuông góc với đường thẳng $d:{latex(b*x-a*y+m)}=0$ là"

    kq= f"${latex(a*x+b*y+c1)}=0$ hoặc ${latex(a*x+b*y+c2)}=0$"
    kq2=f"${latex(b*x-a*y+c1)}=0$ hoặc ${latex(b*x-a*y+c2)}=0$"
    kq3=f"${latex(b*x-a*y+c)}=0$ hoặc ${latex(b*x-a*y-c)}=0$"
    kq4=f"${latex(a*x+b*y+c1+random.randint(1,4))}=0$ hoặc ${latex(a*x+b*y+c2+random.randint(1,4))}=0$"

    noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có tâm ${{I({x_I};{y_I})}}$ và bán kính $R={latex(r)}$.\n\n"\
    f"Đường thẳng $\\Delta$ vuông góc với $d:{latex(b*x-a*y+m)}=0$ nên có phương trình dạng ${latex(a*x+b*y)}+c=0$.\n\n"\
    f"$\\Delta$ tiếp xúc với ${{(C)}} \\Leftrightarrow d(I,\\Delta)=R "\
    f"\\Leftrightarrow \\dfrac{{|{show_tich(a,x_I)} + {show_tich(b,y_I)} +c|}} {{{latex(sqrt(a**2+b**2))}}}={r}$\n\n"\
    f"$\\Leftrightarrow |c+{latex(a*x_I+b*y_I)}|={latex(r*sqrt(a**2+b**2))} \\Leftrightarrow c={latex(c1)}, c={latex(c2)}$.\n\n"\
    f"Phương trình các đường tiếp tuyến là: {kq}.".replace("+-","-")

    #Tạo các phương án
    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.\n   B. { list_PA[1]}.\n    C. { list_PA[2]}.\n    D. { list_PA[3]}.\n"

      
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

#[D10_CX_B3_12]-TF-M2. Cho phương trình đường tròn dạng thu gọn. Tạo câu hỏi đúng-sai   
def gghik_L10_CX_B3_12():
	#Tạo bậc ngẫu nhiên
	x,y,z,a,b=sp.symbols("x y z a b")
	i=random.randint(0,4)
	
	x=sp.symbols("x")
	y=sp.symbols("y")

	chon=random.randint(1,2)
	
	if chon==1:
		x_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		y_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		r=random.randint(2,10)

		#Tìm các điểm có tọa độ nguyên và thuộc đường tròn và lưu vào list điểm
		list_diem=[]
		for x_0 in range(-20,20):
			for y_0 in range(-20,20):
				if (x_0-x_I)**2+(y_0-y_I)**2==r**2:
					list_diem.append([x_0, y_0])

		#Lấy 3 cặp tọa độ đầu tiên đã lưu trong list lưu vào bien diem_A,diem_B,diem_C
		diem_A, diem_B, diem_C = list_diem[0],list_diem[1], list_diem[2]
		x_A, y_A = diem_A[0], diem_A[1]
		x_B, y_B = diem_B[0], diem_B[1]
		x_C, y_C = diem_C[0], diem_C[1]

	if chon==2:
	#Tạo tọa độ tâm và bán kính đường tròn tùy ý
		x_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		y_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		#r=random.randint(2,10)

		#Tìm các điểm có tọa độ nguyên và thuộc đường tròn và lưu vào list điểm
		list_diem=[]
		for r in range (1,10):
			for x_0 in range(-20,20):
				for y_0 in range(-20,20):
					if (x_0-x_I)**2+(y_0-y_I)**2==r**2:
						if x_0!= x_I and y_0!=y_I:
							list_diem.append([x_0, y_0,r])
							r_final=r

		#Lấy 3 cặp tọa độ đầu tiên đã lưu trong list lưu vào bien diem_A,diem_B,diem_C
		diem_A, diem_B, diem_C = list_diem[0],list_diem[1], list_diem[2]
		x_A, y_A = diem_A[0], diem_A[1]
		x_B, y_B = diem_B[0], diem_B[1]
		x_C, y_C = diem_C[0], diem_C[1]
		r=r_final


	noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{latex((x-x_I)**2)}+{latex((y-y_I)**2)}={r**2}$."\
	f" Xét tính đúng sai của các khẳng định sau"

	kq1_T=f"*Đường tròn ${{(C)}}$ có tâm $I({x_I};{y_I})$"
	kq1_F=f"Đường tròn ${{(C)}}$ có tâm $I({-x_I};{-y_I})$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Đường tròn có tâm $I({x_I};{y_I})$ là khẳng định đúng."
	if kq1==kq1_F:
		loigiai_1=f"{kq1_F} là khẳng định sai vì đường tròn có tâm $I({x_I};{y_I})$."

	kq2_T=f"*Đường tròn ${{(C)}}$ có bán kính $R={r}$."
	kq2_F=f"Đường tròn ${{(C)}}$ có bán kính $R={latex(sqrt(r))}$ "
	kq2=random.choice([kq2_T, kq2_F])	
	loigiai_2=f"Đường tròn ${{(C)}}$ có bán kính $R={r}$ là khẳng định đúng."
	if kq2==kq2_F:
		loigiai_2=f"{kq2_F} là khẳng định sai vì $R=\\sqrt{{{r**2}}}={r}$."

	ten_diem=random.choice(["A","B","M","N"])

	kq3_T=f"*Đường tròn ${{(C)}}$ đi qua điểm ${ten_diem}({x_C};{y_C})$"
	kq3_F=f"Đường tròn ${{(C)}}$ không đi qua điểm ${ten_diem}({x_C};{y_C})$"
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Đường tròn ${{(C)}}$ đi qua điểm ${ten_diem}({x_A};{y_A})$ là khẳng định đúng"\
	f" vì tọa độ điểm ${{{ten_diem}}}$ thỏa mãn phương trình đường tròn ${{(C)}}$."
	if kq3==kq3_F:
		loigiai_3=f"{kq3_F} là khẳng định sai vì tọa độ điểm ${{{ten_diem}}}$ thỏa mãn phương trình đường tròn ${{(C)}}$."

	ucln=math.gcd(x_I-x_B,y_I-y_B)
	a1,b1=int((x_I-x_B)/ucln), int((y_I-y_B)/ucln)
	ten_diem=random.choice(["E","G","H","P"])

	kq4_T=f"*Tiếp tuyến của đường tròn ${{(C)}}$ tại điểm ${ten_diem}({x_B};{y_B})$ có phương trình là "\
	f"${latex(a1*(x-x_B)+b1*(y-y_B))}=0$"

	kq4_F=f"Tiếp tuyến của đường tròn ${{(C)}}$ tại điểm ${ten_diem}({x_B};{y_B})$ có phương trình là "\
	f"${latex(b1*(x-x_B)-a1*(y-y_B))}=0$"
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"{kq4_T[1:]} là khẳng định đúng.\n\n"\
	f"Đường tròn ${{(C)}}$ có tâm ${{I({x_I};{y_I})}}$.\n\n"\
	f"Tiếp tuyến tại điểm ${ten_diem}({x_B};{y_B})$ nhận vectơ $\\overrightarrow{{{ten_diem}I}}=({x_I-x_B};{y_I-y_B})$ làm một véctơ pháp tuyến.\n\n"\
	f"Phương trình tiếp tuyến là: ${x_I-x_B}({latex(x-x_B)})+{y_I-y_B}({latex(y-y_B)})=0\\Leftrightarrow {latex(expand(a1*(x-x_B)+b1*(y-y_B)))}=0$.".replace("+-","-")
	if kq4==kq4_F:
		loigiai_4=f"{kq4_F} là khẳng định sai.\n\n"\
		f"Đường tròn ${{(C)}}$ có tâm ${{I({x_I};{y_I})}}$.\n\n"\
	f"Tiếp tuyến tại điểm ${ten_diem}({x_B};{y_B})$ nhận vectơ $\\overrightarrow{{{ten_diem}I}}=({x_I-x_B};{y_I-y_B})$ làm một véctơ pháp tuyến.\n\n"\
	f"Phương trình tiếp tuyến là: ${x_I-x_B}({latex(x-x_B)})+{y_I-y_B}({latex(y-y_B)})=0\\Leftrightarrow {latex(expand(a1*(x-x_B)+b1*(y-y_B)))}=0$.".replace("+-","-")


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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_CX_B3_13]-TF-M2. Cho phương trình đường tròn dạng thu gọn. Tạo câu hỏi đúng-sai   
def gghik_L10_CX_B3_13():
	#Tạo bậc ngẫu nhiên
	x,y,z,a,b=sp.symbols("x y z a b")
	diem_A=["A","M","D","B", "C"]
	diem_B=["B","N","E","C", "D"]
	diem_C=["C","P","F","D", "E"]
	i=random.randint(0,4)
	diem_A,diem_B,diem_C =diem_A[i], diem_B[i], diem_C[i]

	x=sp.symbols("x")
	y=sp.symbols("y")

	chon=random.randint(1,2)
	
	if chon==1:
		x_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		y_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		r=random.randint(2,10)

		#Tìm các điểm có tọa độ nguyên và thuộc đường tròn và lưu vào list điểm
		list_diem=[]
		for x_0 in range(-20,20):
			for y_0 in range(-20,20):
				if (x_0-x_I)**2+(y_0-y_I)**2==r**2:
					list_diem.append([x_0, y_0])

		#Lấy 3 cặp tọa độ đầu tiên đã lưu trong list lưu vào bien diem_A,diem_B,diem_C
		diem_A, diem_B, diem_C = list_diem[0],list_diem[1], list_diem[2]
		x_A, y_A = diem_A[0], diem_A[1]
		x_B, y_B = diem_B[0], diem_B[1]
		x_C, y_C = diem_C[0], diem_C[1]

	if chon==2:
	#Tạo tọa độ tâm và bán kính  đường tròn tùy ý
		x_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		y_I = random.choice([random.randint(-10, -1), random.randint(1, 10)])
		#r=random.randint(2,10)

		#Tìm các điểm có tọa độ nguyên và thuộc đường tròn và lưu vào list điểm
		list_diem=[]
		for r in range (1,10):
			for x_0 in range(-20,20):
				for y_0 in range(-20,20):
					if (x_0-x_I)**2+(y_0-y_I)**2==r**2:
						if x_0!= x_I and y_0!=y_I:
							list_diem.append([x_0, y_0,r])
							r_final=r

		#Lấy 3 cặp tọa độ đầu tiên đã lưu trong list lưu vào bien diem_A,diem_B,diem_C
		diem_A, diem_B, diem_C = list_diem[0],list_diem[1], list_diem[2]
		x_A, y_A = diem_A[0], diem_A[1]
		x_B, y_B = diem_B[0], diem_B[1]
		x_C, y_C = diem_C[0], diem_C[1]
		r=r_final


	d=x_I**2+y_I**2-r**2
	dau_a, dau_b, dau_d = tao_dau(-x_I),tao_dau(-y_I), tao_dau(d)
	if x_I!=0:
	    hs_ax=latex(-2*x_I*x)
	else:
	    hs_ax=""

	if y_I!=0:
	    hs_by=latex(-2*y_I*y)
	else:
	    hs_by=""    

	if d!=0:
		hs_d=d
	else:
		hs_d=""

	ptdt=f"x^2+y^2{dau_a}{hs_ax} {dau_b}{hs_by} {dau_d}{d} =0"

	noi_dung= f"Trong mặt phẳng với hệ tọa độ $(Oxy)$, cho đường tròn ${{(C)}}:{ptdt}$."\
	f" Xét tính đúng sai của các khẳng định sau"

	kq1_T=f"*Đường tròn ${{(C)}}$ có tâm $I({x_I};{y_I})$"
	kq1_F=f"Đường tròn ${{(C)}}$ có tâm $I({-x_I};{-y_I})$"
	kq1=random.choice([kq1_T, kq1_F])
	loigiai_1=f"Đường tròn có tâm $I({x_I};{y_I})$ là khẳng định đúng."
	if kq1==kq1_F:
		loigiai_1=f"{kq1_F} là khẳng định sai vì đường tròn có tâm $I({x_I};{y_I})$."

	kq2_T=f"*Đường tròn ${{(C)}}$ có bán kính $R={r}$"
	kq2_F=f"Đường tròn ${{(C)}}$ có bán kính $R={latex(sqrt(r))}$ "
	kq2=random.choice([kq2_T, kq2_F])	
	loigiai_2=f"Đường tròn ${{(C)}}$ có bán kính $R={r}$ là khẳng định đúng vì $R=\\sqrt{{{tao_ngoac(x_I)}^2 + {tao_ngoac(y_I)}^2 -{tao_ngoac(d)}}}={r}$."
	if kq2==kq2_F:
		loigiai_2=f"{kq2_F} là khẳng định sai vì $R=\\sqrt{{{tao_ngoac(x_I)}^2 + {tao_ngoac(y_I)}^2 -{tao_ngoac(d)}}}={r}$."

	ten_diem=random.choice(["A","B","M","N"])

	kq3_T=f"*Đường tròn ${{(C)}}$ đi qua điểm ${ten_diem}({x_C};{y_C})$"
	kq3_F=f"Đường tròn ${{(C)}}$ không đi qua điểm ${ten_diem}({x_C};{y_C})$"
	kq3=random.choice([kq3_T, kq3_F])
	loigiai_3=f"Đường tròn ${{(C)}}$ đi qua điểm ${ten_diem}({x_A};{y_A})$ là khẳng định đúng"\
	f" vì tọa độ điểm ${{{ten_diem}}}$ thỏa mãn phương trình đường tròn ${{(C)}}$."
	if kq3==kq3_F:
		loigiai_3=f"{kq3_F} là khẳng định sai vì tọa độ điểm ${{{ten_diem}}}$ thỏa mãn phương trình đường tròn ${{(C)}}$."

	ucln=math.gcd(x_I-x_B,y_I-y_B)
	a1,b1=int((x_I-x_B)/ucln), int((y_I-y_B)/ucln)
	ten_diem=random.choice(["E","G","H","P"])

	kq4_T=f"*Tiếp tuyến của đường tròn ${{(C)}}$ tại điểm ${ten_diem}({x_B};{y_B})$ có phương trình là "\
	f"${latex(a1*(x-x_B)+b1*(y-y_B))}=0$"

	kq4_F=f"Tiếp tuyến của đường tròn ${{(C)}}$ tại điểm ${ten_diem}({x_B};{y_B})$ có phương trình là "\
	f"${latex(b1*(x-x_B)-a1*(y-y_B))}=0$"
	kq4=random.choice([kq4_T, kq4_F])
	loigiai_4=f"{kq4_T[1:]} là khẳng định đúng.\n\n"\
	f"Đường tròn ${{(C)}}$ có tâm ${{I({x_I};{y_I})}}$.\n\n"\
	f"Tiếp tuyến tại điểm ${ten_diem}({x_B};{y_B})$ nhận vectơ $\\overrightarrow{{{ten_diem}I}}=({x_I-x_B};{y_I-y_B})$ làm một véctơ pháp tuyến.\n\n"\
	f"Phương trình tiếp tuyến là: ${x_I-x_B}({latex(x-x_B)})+{y_I-y_B}({latex(y-y_B)})=0\\Leftrightarrow {latex(expand(a1*(x-x_B)+b1*(y-y_B)))}=0$.".replace("+-","-")
	if kq4==kq4_F:
		loigiai_4=f"{kq4_F} là khẳng định sai.\n\n"\
		f"Đường tròn ${{(C)}}$ có tâm ${{I({x_I};{y_I})}}$.\n\n"\
	f"Tiếp tuyến tại điểm ${ten_diem}({x_B};{y_B})$ nhận vectơ $\\overrightarrow{{{ten_diem}I}}=({x_I-x_B};{y_I-y_B})$ làm một véctơ pháp tuyến.\n\n"\
	f"Phương trình tiếp tuyến là: ${x_I-x_B}({latex(x-x_B)})+{y_I-y_B}({latex(y-y_B)})=0\\Leftrightarrow {latex(expand(a1*(x-x_B)+b1*(y-y_B)))}=0$.".replace("+-","-")


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

	return debai,debai_latex,loigiai_word,dap_an

#[D10_CX_B3_14]. Viết phương trình đường tròn có tâm và đi qua điểm
def gghik_L10_CX_B3_14():
    #Tạo bậc ngẫu nhiên
    x,y,z=sp.symbols("x y z")
    a,b = [random.randint(-10,10) for i in range(2)]
    x_0,y_0=[random.randint(-10,10) for i in range(2)]
    if x_0 ==a and y_0==b:
    	x_0=x_0+random.randint(1,3)
    ten_tam=random.choice(["A","B","I","H"])
    ten_diem=random.choice(["M","N","E","F","D","K"])
    r=sqrt((a-x_0)**2+(b-y_0)**2)
          

    noi_dung= f"Trong mặt phẳng ${{Oxy}}$, phương trình đường tròn ${{(C)}}$ có tâm ${{{ten_tam}({a};{b})}}$"\
                f" và đi qua điểm ${ten_diem}({x_0};{y_0})$ là"

    kq= f"{latex((x-a)**2)}+{latex((y-b)**2)}={r**2}"
    kq2=f"{latex((x+a)**2)}+{latex((y+b)**2)}={r**2}"
    kq3=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={r**2}"
    kq4=f"{latex((x+x_0)**2)}+{latex((y+y_0)**2)}={r**2}"

    noi_dung_loigiai=f"Đường tròn ${{(C)}}$ có bán kính là ${{{ten_tam}{ten_diem}}}=\\sqrt{{({show_hieu(x_0,a)})^2+({show_hieu(y_0,b)})^2}}={latex(r)}$.\n\n"\
    f"Đường tròn ${{(C)}}$ có phương trình là: ${kq}$.".replace("(0)","0")

    #Tạo các phương án
    pa_A= f"*${kq}$"
    pa_B= f"${kq2}$"
    pa_C= f"${kq3}$"
    pa_D= f"${kq4}$"

    #Trộn các phương án
    list_PA =[pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)    
    dap_an=my_module.tra_ve_dap_an(list_PA)

    debai= f"{noi_dung}\n"
        #f"{file_name}\n"
    phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.\n    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

      
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

#[D10_CX_B3_15]. Viết phương trình đường tròn có tâm và đi qua điểm
def gghik_L10_CX_B3_15():
    #Tạo bậc ngẫu nhiên
	x,y,z=sp.symbols("x y z")   
	x_0,y_0=[random.randint(-10,10) for i in range(2)]
	ten_tam=random.choice(["A","B","I","H","E","M","N"])
	a = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	b = random.choice([random.randint(-5, -1), random.randint(1, 5)])
	c=random.randint(-7,7)
	r=abs(a*x_0+b*y_0+c)/sqrt(a**2+b**2)
          

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho đường thẳng $\\Delta: {latex(a*x+b*y+c)}=0$ và điểm ${{{ten_tam}({x_0};{y_0})}}$."\
	            f" Đường tròn ${{(C)}}$ có tâm ${{{ten_tam}}}$ và tiếp xúc với đường thẳng $\\Delta$ có phương trình là"

	kq= f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={latex(r**2)}"
	kq2=f"{latex((x+x_0)**2)}+{latex((y+y_0)**2)}={latex(r**2)}"
	kq3=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={latex(r)}"
	kq4=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={(a*x_0+b*y_0+c)**2}"

	noi_dung_loigiai=thay_dau_congtru(f"Đường tròn ${{(C)}}$ có bán kính là:"\
	f" $R=d({ten_tam},\\Delta)=\\dfrac{{|{show_tich(a,x_0)}+{show_tich(b,y_0)}+{c}|}}{{ \\sqrt{{{a**2}+{b**2}}} }}={latex(r)}$.\n\n"\
	f"Đường tròn ${{(C)}}$ có phương trình là: ${kq}$.".replace("(0)","0"))

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.\n    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

	  
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

#[D10_CX_B3_16]. Viết phương trình đường tròn có tâm và tiếp xúc với trục tọa độ
def gghik_L10_CX_B3_16():
    #Tạo bậc ngẫu nhiên
	x,y,z=sp.symbols("x y z")   
	x_0 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	y_0 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if x_0==y_0 or x_0==-y_0:
		x_0=x_0+random.randint(1,4)

	ten_tam=random.choice(["A","B","I","H","E","M","N"])
	truc=random.choice(["Ox", "Oy"])    
	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, đường tròn ${{(C)}}$ có tâm ${{{ten_tam}({x_0};{y_0})}}$ và tiếp xúc với trục ${{{truc}}}$ có phương trình là"

	if truc=="Ox":
		kq= f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={y_0**2}"
		kq2=f"{latex((x+x_0)**2)}+{latex((y+y_0)**2)}={y_0**2}"
		kq3=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={abs(x_0)}"
		kq4=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={x_0**2}"

		noi_dung_loigiai=thay_dau_congtru(f"Đường tròn ${{(C)}}$ có bán kính là $R={abs(y_0)}$.\n\n"\
		f"Đường tròn ${{(C)}}$ có phương trình là: ${kq}$.".replace("(0)","0"))

	if truc=="Oy":
		kq= f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={x_0**2}"
		kq2=f"{latex((x+x_0)**2)}+{latex((y+y_0)**2)}={x_0**2}"
		kq3=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={abs(y_0)}"
		kq4=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={y_0**2}"

		noi_dung_loigiai=thay_dau_congtru(f"Đường tròn ${{(C)}}$ có bán kính là $R={abs(x_0)}$.\n\n"\
		f"Đường tròn ${{(C)}}$ có phương trình là: ${kq}$.".replace("(0)","0"))

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.\n    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

	  
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

#[D10_CX_B3_17]. Xét vị trí tương đối giữa điểm và đường tròn có phương trình thu gọn
def gghik_L10_CX_B3_17():
    #Tạo bậc ngẫu nhiên
	x,y,z=sp.symbols("x y z")   
	x_0 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	y_0 = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	if x_0==y_0 or x_0==-y_0:
		x_0=x_0+random.randint(1,4)

	a = random.choice([random.randint(-10, -1), random.randint(1, 10)])
	b = random.choice([random.randint(-10, -1), random.randint(1, 10)])

	if a==x_0 and b==y_0:
		a=a+random.randint(1,4)
		b=b-random.randint(1,4)

	ten_diem=random.choice(["A","B","H","E","M","N","P"])
	vitri=random.randint(1,3)
	
	if vitri==1:
		IM=sqrt((a-x_0)**2+(b-y_0)**2)
		R=sqrt((a-x_0)**2+(b-y_0)**2+random.randint(2,15))
		duong_tron=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={R**2}"

		noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho đường tròn ${{(C)}}:{duong_tron}$ và điểm ${ten_diem}({a};{b})$.\n\n"\
	f"Tìm khẳng định đúng trong các khẳng định sau"

		
		kq= f"Điểm ${{{ten_diem}}}$ nằm trong đường tròn ${{(C)}}$"
		kq2=f"Điểm ${{{ten_diem}}}$ nằm ngoài đường tròn ${{(C)}}$"
		kq3=f"Điểm ${{{ten_diem}}}$ nằm trên đường tròn ${{(C)}}$"
		kq4=f"Điểm ${{{ten_diem}}}$ là tâm của đường tròn ${{(C)}}$"

		noi_dung_loigiai=thay_dau_congtru(f"Đường tròn ${{(C)}}$ có tâm $I({x_0};{y_0})$ và bán kính là $R={latex(R)}$.\n\n"\
		f"$\\overrightarrow{{IM}}=({a-x_0};{b-y_0}) \\Rightarrow IM={latex(IM)}<{latex(R)}$.\n\n"\
		f"Vậy điểm ${{{ten_diem}}}$ nằm trong đường tròn ${{(C)}}$.")

	if vitri==2:
		IM=sqrt((a-x_0)**2+(b-y_0)**2)
		R=sqrt(abs((a-x_0)**2+(b-y_0)**2-random.randint(2,10)))
		duong_tron=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={R**2}"

		noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho đường tròn ${{(C)}}:{duong_tron}$ và điểm ${ten_diem}({a};{b})$.\n\n"\
	f"Tìm khẳng định đúng trong các khẳng định sau"

		
		kq= f"Điểm ${{{ten_diem}}}$ nằm ngoài đường tròn ${{(C)}}$"
		kq2=f"Điểm ${{{ten_diem}}}$ nằm trong đường tròn ${{(C)}}$"
		kq3=f"Điểm ${{{ten_diem}}}$ nằm trên đường tròn ${{(C)}}$"
		kq4=f"Điểm ${{{ten_diem}}}$ là tâm của đường tròn ${{(C)}}$"

		noi_dung_loigiai=thay_dau_congtru(f"Đường tròn ${{(C)}}$ có tâm $I({x_0};{y_0})$ và bán kính là $R={latex(R)}$.\n\n"\
		f"$\\overrightarrow{{IM}}=({a-x_0};{b-y_0}) \\Rightarrow IM={latex(IM)}>{latex(R)}$.\n\n"\
		f"Vậy điểm ${{{ten_diem}}}$ nằm ngoài đường tròn ${{(C)}}$.")

	
	if vitri==3:
		IM=sqrt((a-x_0)**2+(b-y_0)**2)
		R=IM
		duong_tron=f"{latex((x-x_0)**2)}+{latex((y-y_0)**2)}={R**2}"

		noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho đường tròn ${{(C)}}:{duong_tron}$ và điểm ${ten_diem}({a};{b})$.\n\n"\
	f"Tìm khẳng định đúng trong các khẳng định sau"

		
		kq= f"Điểm ${{{ten_diem}}}$ nằm ngoài đường tròn ${{(C)}}$"
		kq2=f"Điểm ${{{ten_diem}}}$ nằm trong đường tròn ${{(C)}}$"
		kq3=f"Điểm ${{{ten_diem}}}$ nằm trên đường tròn ${{(C)}}$"
		kq4=f"Điểm ${{{ten_diem}}}$ là tâm của đường tròn ${{(C)}}$"

		noi_dung_loigiai=thay_dau_congtru(f"Đường tròn ${{(C)}}$ có tâm $I({x_0};{y_0})$ và bán kính là $R={latex(R)}$.\n\n"\
		f"$\\overrightarrow{{IM}}=({a-x_0};{b-y_0}) \\Rightarrow IM={latex(IM)}=R$.\n\n"\
		f"Vậy điểm ${{{ten_diem}}}$ nằm trên đường tròn ${{(C)}}$.")

	

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.   B. { list_PA[1]}.\n    C. { list_PA[2]}.     D. { list_PA[3]}.\n"

	  
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
#BÀI 2-ELIP

#[D10_CX_B4_01]-M2. Cho phương trình Elip. Đọc trục lớn.
def gghik_L10_CX_B4_01():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=b+random.randint(1,5)
	e=x**2/a**2+y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip $ {{(E)}}:{latex(x**2/a**2)}+\\dfrac{{y^2}}{{{b**2}}}=1$. Độ dài trục lớn bằng"                

	kq=2*a
	kq2=2*b
	kq3=a**2
	kq4=b**2
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $a^2={a**2} \\Rightarrow a={a}$. Độ dài trục lớn bằng $2a={{{2*a}}}$."

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_02]-M2. Cho phương trình Elip. Đọc trục nhỏ.
def gghik_L10_CX_B4_02():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=b+random.randint(1,5)
	e=x**2/a**2+y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip $ {{(E)}}:{latex(x**2/a**2)}+\\dfrac{{y^2}}{{{b**2}}}=1$. Độ dài trục nhỏ bằng"                

	kq=2*b
	kq2=2*a
	kq3=a**2
	kq4=b**2
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $b^2={b**2} \\Rightarrow b={b}$. Độ dài trục nhỏ bằng $2b={{{2*b}}}$."

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_03]-M2. Cho phương trình Elip. Đọc tiêu cự.
def gghik_L10_CX_B4_03():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=b+random.randint(1,5)
	c=sqrt(a**2-b**2)
	e=x**2/a**2+y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip $ {{(E)}}:{latex(x**2/a**2)}+\\dfrac{{y^2}}{{{b**2}}}=1$. Độ dài tiêu cự bằng"                

	kq=2*c
	kq2=2*sqrt(a)
	kq3=2*b
	kq4=2*a
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $c^2=a^2-b^2={a**2}-{b**2}={a**2-b**2} \\Rightarrow c={latex(c)}$. Độ dài tiêu cự bằng $2c={{{latex(2*c)}}}$."

	#Tạo các phương án
	pa_A= f"*${{{latex(kq)}}}$"
	pa_B= f"${{{latex(kq2)}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_04]-M2. Cho phương trình Elip. Đọc tiêu điểm.
def gghik_L10_CX_B4_04():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=b+random.randint(1,5)
	c=sqrt(a**2-b**2)
	e=x**2/a**2+y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip $ {{(E)}}:{latex(x**2/a**2)}+\\dfrac{{y^2}}{{{b**2}}}=1$. Tọa độ tiêu điểm là"                
	
	kq=f"$F_1({latex(-c)};0)$ và $F_2({latex(c)};0)$"
	kq2=f"$F_1({-a};0)$ và $F_2({a};0)$"
	kq3=f"$F_1(0;{-b})$ và $F_2(0;{b})$"
	kq4=f"$F_1({latex(-2*c)};0)$ và $F_2({latex(2*c)};0)$"

	noi_dung_loigiai=f"Ta có: $c^2=a^2-b^2={a**2}-{b**2}={a**2-b**2} \\Rightarrow c={latex(c)}$. Tọa độ tiêu điểm là {kq}."

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"

	  
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

#[D10_CX_B4_05]-M2. Cho phương trình Elip. Đọc tọa độ đỉnh
def gghik_L10_CX_B4_05():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=b+random.randint(1,5)
	c=sqrt(a**2-b**2)
	e=x**2/a**2+y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip $ {{(E)}}:{latex(x**2/a**2)}+\\dfrac{{y^2}}{{{b**2}}}=1$."\
	f" Điểm nào sau đây là một đỉnh của elip đã cho?"                
	A=["A","B","C","D"]
	B=["B","C","D","A"]
	C=["C","D","A","B"]
	D=["D","A","B","C"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	kq=random.choice([f"{A}({a};0)",f"{A}({-a};0)",f"{A}(0;{b})", f"{A}(0;{-b})"])
	kq2=random.choice([f"{B}(0;{a})",f"{B}(0;{-a})"])
	kq3=random.choice([f"{C}({b};0)",f"{B}({-b};0)"])
	kq4=random.choice([f"{D}({latex(c)};0)",f"{D}({latex(-c)};0)"])

	noi_dung_loigiai=f"Ta có: $a^2={a**2} \\Rightarrow a={a},b^2={b**2} \\Rightarrow b={b}$.\n\n"\
	f"Do đó tọa độ các đỉnh là $A_1({-a};0),A_2({a};0), B_1(0;{-b}), B_2(0;{b})$.\n\n"\
	f"Vậy phương án đúng là ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_06]-M2. Cho trục lớn, trục nhỏ. Viết phương trình Elip.
def gghik_L10_CX_B4_06():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=b+random.randint(1,5) 

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip có độ dài trục lớn bằng ${{{2*a}}}$, độ dài trục nhỏ bằng ${{{2*b}}}$."\
	f" Phương trình của elip đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{a**2+random.randint(1,10)}}} + \\dfrac{{y^2}}{{{a**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{(2*a)**2}}} + \\dfrac{{y^2}}{{{(2*b)**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*b)**2}}} + \\dfrac{{y^2}}{{{(2*a)**2}}}=1"

	noi_dung_loigiai=f"Ta có: $2a={2*a}\\Rightarrow a={a} \\Rightarrow a^2={a**2}$, $2b={2*b}\\Rightarrow b={b} \\Rightarrow b^2={b**2}$.\n\n"\
	f"Phương trình của elip đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_07]-M2. Cho trục lớn, tiêu cự. Viết phương trình Elip.
def gghik_L10_CX_B4_07():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=b+random.randint(1,5)
	c=sqrt(a**2-b**2)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip có độ dài trục lớn bằng ${{{2*a}}}$, tiêu cự bằng ${{{latex(2*c)}}}$."\
	f" Phương trình của elip đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{c**2+random.randint(1,10)}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*a)**2}}} + \\dfrac{{y^2}}{{{(2*c)**2}}}=1"

	noi_dung_loigiai=f"Ta có: $2a={2*a}\\Rightarrow a={a} \\Rightarrow a^2={a**2}$, $2c={latex(2*c)}\\Rightarrow c={latex(c)} \\Rightarrow c^2={c**2}$.\n\n"\
	f"$b^2=a^2-c^2={a**2}-{latex(c**2)}={b**2}$.\n\n"\
	f"Phương trình của elip đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_08]-M2. Cho trục nhỏ, tiêu cự. Viết phương trình Elip.
def gghik_L10_CX_B4_08():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=b+random.randint(1,5)
	c=sqrt(a**2-b**2)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip có độ dài trục nhỏ bằng ${{{2*b}}}$, tiêu cự bằng ${{{latex(2*c)}}}$."\
	f" Phương trình của elip đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{c**2+random.randint(1,10)}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*a)**2}}} + \\dfrac{{y^2}}{{{(2*c)**2}}}=1"

	noi_dung_loigiai=f"Ta có: $2b={2*b}\\Rightarrow b={b} \\Rightarrow b^2={b**2}$, $2c={latex(2*c)}\\Rightarrow c={latex(c)} \\Rightarrow c^2={c**2}$.\n\n"\
	f"$a^2=b^2+c^2={b**2}+{latex(c**2)}={a**2}$.\n\n"\
	f"Phương trình của elip đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_09]-M2. Cho đỉnh thuộc trục 2 trục. Viết phương trình Elip.
def gghik_L10_CX_B4_09():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=b+random.randint(1,5)
	diem_A=random.choice(["A","E","C", "G"])
	diem_B=random.choice(["B","D","M", "N"])

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip nhận các điểm ${diem_A}({a};0)$ và ${diem_B}(0;{b})$ làm đỉnh."\
	f" Phương trình của elip đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{a**2+random.randint(1,10)}}} + \\dfrac{{y^2}}{{{a**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{(2*a)**2}}} + \\dfrac{{y^2}}{{{(2*b)**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{b**2+random.randint(1,5)}}} + \\dfrac{{y^2}}{{{b**2}}}=1"

	noi_dung_loigiai=f"Phương trình elip có dạng: $ \\dfrac{{x^2}}{{a^2}} + \\dfrac{{y^2}}{{b^2}}=1$.\n\n"\
	f"Ta có: ${diem_A}({a};0) \\Rightarrow a={a}$, ${diem_B}(0;{b})\\Rightarrow b={b}$.\n\n"\
	f"Phương trình của elip đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_10]-M2. Cho đỉnh thuộc trục lớn, tiêu điểm. Viết phương trình Elip.
def gghik_L10_CX_B4_10():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=b+random.randint(1,5)
	c=sqrt(a**2-b**2)
	ten_dinh=random.choice(["A","E","C", "G"])
	ten_tieudiem=random.choice(["B","D","M", "N"])
	dinh=random.choice([f"({-a};0)", f"({a};0)"])
	tieudiem=random.choice([f"({latex(-c)};0)", f"({latex(c)};0)"])


	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip nhận điểm ${ten_dinh}{dinh}$ làm một đỉnh, nhận điểm ${ten_tieudiem}{tieudiem}$ làm tiêu điểm."\
	f" Phương trình của elip đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{c**2+random.randint(1,10)}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*a)**2}}} + \\dfrac{{y^2}}{{{(2*c)**2}}}=1"

	noi_dung_loigiai=f"Phương trình elip có dạng: $ \\dfrac{{x^2}}{{a^2}} + \\dfrac{{y^2}}{{b^2}}=1$.\n\n"\
	f"Elip nhận điểm ${ten_dinh}{dinh}$ làm một đỉnh nên $a={a} \\Rightarrow a^2={a**2}$.\n\n"\
	f"Elip nhận điểm ${ten_tieudiem}{tieudiem}$ làm tiêu điểm nên $c={latex(c)} \\Rightarrow c^2={c**2}$.\n\n"\
	f"$b^2=a^2-c^2={a**2}-{c**2}={b**2}$.\n\n"\
	f"Phương trình của elip đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_11]-M2. Cho đỉnh thuộc trục nhỏ, tiêu điểm. Viết phương trình Elip.
def gghik_L10_CX_B4_11():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=b+random.randint(1,5)
	c=sqrt(a**2-b**2)
	ten_dinh=random.choice(["A","E","C", "G"])
	ten_tieudiem=random.choice(["B","D","M", "N"])
	dinh=random.choice([f"(0;{-b})", f"(0;{b})"])
	tieudiem=random.choice([f"({latex(-c)};0)", f"({latex(c)};0)"])


	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho elip nhận điểm ${ten_dinh}{dinh}$ làm một đỉnh, nhận điểm ${ten_tieudiem}{tieudiem}$ làm tiêu điểm."\
	f" Phương trình của elip đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{c**2+random.randint(1,10)}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{c**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*a)**2}}} + \\dfrac{{y^2}}{{{(2*c)**2}}}=1"

	noi_dung_loigiai=f"Phương trình elip có dạng: $ \\dfrac{{x^2}}{{a^2}} + \\dfrac{{y^2}}{{b^2}}=1$.\n\n"\
	f"Elip nhận điểm ${ten_dinh}{dinh}$ làm một đỉnh nên $b={b} \\Rightarrow b^2={b**2}$.\n\n"\
	f"Elip nhận điểm ${ten_tieudiem}{tieudiem}$ làm tiêu điểm nên $c={latex(c)} \\Rightarrow c^2={c**2}$.\n\n"\
	f"$a^2=b^2+c^2={b**2}+{c**2}={a**2}$.\n\n"\
	f"Phương trình của elip đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#HYPEBOL
#[D10_CX_B4_11]-M2. Cho phương trình Hypebol. Đọc trục thực.
def gghik_L10_CX_B4_11():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=random.randint(1,20)
	if a==b: a=a+random.randint(1,3)
	h=x**2/a**2-y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol $ {{(H)}}:\\dfrac{{x^2}}{{{a**2}}}-\\dfrac{{y^2}}{{{b**2}}}=1$. Độ dài trục thực bằng"                

	kq=2*a
	kq2=2*b
	kq3=a**2
	kq4=b**2
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $a^2={a**2} \\Rightarrow a={a}$. Độ dài trục thực bằng $2a={{{2*a}}}$."

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_12]-M2. Cho phương trình Hypebol. Đọc trục ảo.
def gghik_L10_CX_B4_12():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=random.randint(1,20)
	if a==b: a=a+random.randint(1,3)
	e=x**2/a**2-y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol ${{(H)}}:\\dfrac{{x^2}}{{{a**2}}}-\\dfrac{{y^2}}{{{b**2}}}=1$. Độ dài trục ảo bằng"                

	kq=2*b
	kq2=2*a
	kq3=a**2
	kq4=b**2
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $b^2={b**2} \\Rightarrow b={b}$. Độ dài trục ảo bằng $2b={{{2*b}}}$."

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_13]-M2. Cho phương trình Hypebol. Đọc tiêu cự.
def gghik_L10_CX_B4_13():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=random.randint(1,20)
	if a==b: a=a+random.randint(1,3)
	c=sqrt(a**2+b**2)
	e=x**2/a**2-y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol ${{(H)}}:\\dfrac{{x^2}}{{{a**2}}}-\\dfrac{{y^2}}{{{b**2}}}=1$. Độ dài tiêu cự bằng"                

	kq=2*c
	kq2=2*sqrt(a)
	kq3=2*b
	kq4=2*a
	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $c^2=a^2+b^2={a**2}+{b**2}={a**2+b**2} \\Rightarrow c={latex(c)}$. Độ dài tiêu cự bằng $2c={{{latex(2*c)}}}$."

	#Tạo các phương án
	pa_A= f"*${{{latex(kq)}}}$"
	pa_B= f"${{{latex(kq2)}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_14]-M2. Cho phương trình Hypebol. Đọc tiêu điểm.
def gghik_L10_CX_B4_14():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=random.randint(1,20)
	if a==b: a=a+random.randint(1,3)
	c=sqrt(a**2+b**2)
	e=x**2/a**2-y**2/b**2    

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol ${{(H)}}:\\dfrac{{x^2}}{{{a**2}}}-\\dfrac{{y^2}}{{{b**2}}}=1$. Tọa độ tiêu điểm là"                
	
	kq=f"$F_1({latex(-c)};0)$ và $F_2({latex(c)};0)$"
	kq2=f"$F_1({-a};0)$ và $F_2({a};0)$"
	kq3=f"$F_1(0;{-b})$ và $F_2(0;{b})$"
	kq4=f"$F_1({latex(-2*c)};0)$ và $F_2({latex(2*c)};0)$"

	noi_dung_loigiai=f"Ta có: $c^2=a^2+b^2={a**2}+{b**2}={a**2+b**2} \\Rightarrow c={latex(c)}$. Tọa độ tiêu điểm là {kq}."

	#Tạo các phương án
	pa_A= f"*{kq}"
	pa_B= f"{kq2}"
	pa_C= f"{kq3}"
	pa_D= f"{kq4}"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\n    C. { list_PA[2]}.\t    D. { list_PA[3]}.\n"

	  
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

#[D10_CX_B4_15]-M2. Cho phương trình Hypebol. Đọc tọa độ đỉnh
def gghik_L10_CX_B4_15():
	x,y=sp.symbols("x y")
	b=random.randint(1,20)
	a=random.randint(1,20)
	if a==b: a=a+random.randint(1,3)
	c=sqrt(a**2+b**2)
	e=x**2/a**2-y**2/b**2

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol  ${{(H)}}:\\dfrac{{x^2}}{{{a**2}}}-\\dfrac{{y^2}}{{{b**2}}}=1$."\
	f" Điểm nào sau đây là một đỉnh của hypebol đã cho?"                
	A=["A","B","C","D"]
	B=["B","C","D","A"]
	C=["C","D","A","B"]
	D=["D","A","B","C"]
	i=random.randint(0,3)
	A, B, C, D = A[i], B[i], C[i], D[i]
	kq=random.choice([f"{A}({a};0)",f"{A}({-a};0)"])
	kq2=random.choice([f"{B}(0;{a})",f"{B}(0;{-a})"])
	kq3=random.choice([f"{C}({b};0)",f"{B}({-b};0)"])
	kq4=random.choice([f"{D}(0;{b})",f"{D}(0;{-b})"])

	noi_dung_loigiai=f"Ta có: $a^2={a**2} \\Rightarrow a={a},b^2={b**2} \\Rightarrow b={b}$.\n\n"\
	f"Do đó tọa độ các đỉnh là $A_1({-a};0),A_2({a};0)$.\n\n"\
	f"Vậy phương án đúng là ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_16]-M2. Cho trục thực, trục ảo. Viết phương trình Hypebol.
def gghik_L10_CX_B4_16():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=random.randint(1,10)
	if a==b: b=b+random.randint(1,4)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol có độ dài trục thực bằng ${{{2*a}}}$, độ dài trục ảo bằng ${{{2*b}}}$."\
	f" Phương trình của hypebol đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} - \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{a**2}}} + \\dfrac{{y^2}}{{{b**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{(2*a)**2}}} -\\dfrac{{y^2}}{{{(2*b)**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*b)**2}}} +\\dfrac{{y^2}}{{{(2*a)**2}}}=1"

	noi_dung_loigiai=f"Ta có: $2a={2*a}\\Rightarrow a={a} \\Rightarrow a^2={a**2}$, $2b={2*b}\\Rightarrow b={b} \\Rightarrow b^2={b**2}$.\n\n"\
	f"Phương trình của hypebol đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_17]-M2. Cho trục thực, tiêu cự. Viết phương trình Hypebol.
def gghik_L10_CX_B4_17():
	x,y=sp.symbols("x y")
	b=random.randint(1,15)
	a=random.randint(1,15)
	if a==b: a=a+random.randint(1,4)
	c=sqrt(a**2+b**2)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol có độ dài trục thực bằng ${{{2*a}}}$, tiêu cự bằng ${{{latex(2*c)}}}$."\
	f" Phương trình của hypebol đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} - \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{c**2+random.randint(1,10)}}} - \\dfrac{{y^2}}{{{c**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{a**2}}} - \\dfrac{{y^2}}{{{c**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*a)**2}}} - \\dfrac{{y^2}}{{{(2*c)**2}}}=1"

	noi_dung_loigiai=f"Ta có: $2a={2*a}\\Rightarrow a={a} \\Rightarrow a^2={a**2}$, $2c={latex(2*c)}\\Rightarrow c={latex(c)} \\Rightarrow c^2={c**2}$.\n\n"\
	f"$b^2=c^2-a^2={c**2}-{latex(a**2)}={b**2}$.\n\n"\
	f"Phương trình của hypebol đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_18]-M2. Cho trục ảo, tiêu cự. Viết phương trình Hypebol.
def gghik_L10_CX_B4_18():
	x,y=sp.symbols("x y")
	b=random.randint(1,10)
	a=random.randint(1,15)
	if a==b: b=b+random.randint(1,5)
	c=sqrt(a**2+b**2)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol có độ dài trục ảo bằng ${{{2*b}}}$, tiêu cự bằng ${{{latex(2*c)}}}$."\
	f" Phương trình của hypebol đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} - \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{c**2+random.randint(1,10)}}} - \\dfrac{{y^2}}{{{c**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{a**2}}} - \\dfrac{{y^2}}{{{c**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*a)**2}}} - \\dfrac{{y^2}}{{{(2*c)**2}}}=1"

	noi_dung_loigiai=f"Ta có: $2b={2*b}\\Rightarrow b={b} \\Rightarrow b^2={b**2}$, $2c={latex(2*c)}\\Rightarrow c={latex(c)} \\Rightarrow c^2={c**2}$.\n\n"\
	f"$a^2=c^2-b^2={latex(c**2)}-{b**2}={a**2}$.\n\n"\
	f"Phương trình của hypebol đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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


#[D10_CX_B4_19]-M2. Cho đỉnh thuộc trục thực, tiêu điểm. Viết phương trình Hypebol.
def gghik_L10_CX_B4_19():
	x,y=sp.symbols("x y")
	b=random.randint(1,10)
	a=random.randint(1,15)
	if a==b: b=b+random.randint(1,5)
	c=sqrt(a**2+b**2)
	ten_dinh=random.choice(["A","E","C", "G"])
	ten_tieudiem=random.choice(["B","D","M", "N"])
	dinh=random.choice([f"({-a};0)", f"({a};0)"])
	tieudiem=random.choice([f"({latex(-c)};0)", f"({latex(c)};0)"])


	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho hypebol nhận điểm ${ten_dinh}{dinh}$ làm một đỉnh, nhận điểm ${ten_tieudiem}{tieudiem}$ làm tiêu điểm."\
	f" Phương trình của hypebol đã cho là"                
	
	kq=f" \\dfrac{{x^2}}{{{a**2}}} - \\dfrac{{y^2}}{{{b**2}}}=1"
	kq2=f" \\dfrac{{x^2}}{{{c**2+random.randint(1,10)}}} - \\dfrac{{y^2}}{{{c**2}}}=1"
	kq3=f" \\dfrac{{x^2}}{{{a**2}}} - \\dfrac{{y^2}}{{{c**2}}}=1"
	kq4=f" \\dfrac{{x^2}}{{{(2*a)**2}}} - \\dfrac{{y^2}}{{{(2*c)**2}}}=1"

	noi_dung_loigiai=f"Phương trình hypebol có dạng: $ \\dfrac{{x^2}}{{a^2}} + \\dfrac{{y^2}}{{b^2}}=1$.\n\n"\
	f"Hypebol nhận điểm ${ten_dinh}{dinh}$ làm một đỉnh nên $a={a} \\Rightarrow a^2={a**2}$.\n\n"\
	f"Hypebol nhận điểm ${ten_tieudiem}{tieudiem}$ làm tiêu điểm nên $c={latex(c)} \\Rightarrow c^2={c**2}$.\n\n"\
	f"$b^2=c^2-a^2={c**2}-{a**2}={b**2}$.\n\n"\
	f"Phương trình của hypebol đã cho là: ${kq}$."

	#Tạo các phương án
	pa_A= f"*${kq}$"
	pa_B= f"${kq2}$"
	pa_C= f"${kq3}$"
	pa_D= f"${kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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


#[D10_CX_B4_20]-M1. Cho parabol. Tìm tham số tiêu.
def gghik_L10_CX_B4_20():
	x,y=sp.symbols("x y")
	p=random.randint(1,20)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, cho parabol $(P):y^2={2*p}x$."\
	f" Tham số tiêu của parabol đã cho là"              
	
	kq=p
	kq2=2*p
	kq3=p**2
	kq4=p+random.randint(1,5)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $p=\\dfrac{{{2*p}}}{{2}}={p}$. "\
	f"Parabol có tham số tiêu là $p={kq}$."
	

	#Tạo các phương án
	pa_A= f"*$p={kq}$"
	pa_B= f"$p={kq2}$"
	pa_C= f"$p={kq3}$"
	pa_D= f"$p={kq4}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_21]-M1. Cho parabol. Tìm đường chuẩn.
def gghik_L10_CX_B4_21():
	x,y=sp.symbols("x y")
	p=random.randint(1,20)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, đường chuẩn của parabol $(P):y^2={2*p}x$ có phương trình là"        
	
	kq=-p/2
	kq2=p/2
	kq3=p
	kq4=-p

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $p=\\dfrac{{{2*p}}}{{2}}={p}$. "\
	f"Parabol có đường chuẩn là đường thẳng $x={phan_so(kq)}$."	

	#Tạo các phương án
	pa_A= f"*$x={phan_so(kq)}$"
	pa_B= f"$x={phan_so(kq2)}$"
	pa_C= f"$x={phan_so(kq3)}$"
	pa_D= f"$x={phan_so(kq4)}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)    
	dap_an=my_module.tra_ve_dap_an(list_PA)

	debai= f"{noi_dung}\n"
	    #f"{file_name}\n"
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

#[D10_CX_B4_22]-M1. Cho parabol. Tìm tiêu điểm.
def gghik_L10_CX_B4_22():
	x,y=sp.symbols("x y")
	p=random.randint(1,20)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, tiêu điểm của parabol $(P):y^2={2*p}x$ là"        
	
	kq=p/2
	kq2=-p/2
	kq3=p
	kq4=-p

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=f"Ta có: $p=\\dfrac{{{2*p}}}{{2}}={p}$. "\
	f"Parabol có tiêu điểm là $F\\left({phan_so(kq)};0\\right)$."

	#Tạo các phương án
	pa_A= f"*$F\\left({phan_so(kq)};0\\right)$"
	pa_B= random.choice([f"$F\\left({phan_so(kq2)};0\\right)$", f"$F\\left(0; {phan_so(kq)}\\right)$"])
	pa_C= f"$F\\left({phan_so(kq3)};0\\right)$"
	pa_D= f"$F\\left({phan_so(kq4)};0\\right)$"

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

#[D10_CX_B4_23]-M1. Viết phương trình parabol có tham số tiêu.
def gghik_L10_CX_B4_23():
	x,y=sp.symbols("x y")
	p=random.randint(1,20)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, parabol ${{(P)}}$ có tham số tiêu $p={{{p}}}$ có phương trình chính tắc là"        
	
	kq=2*p
	kq2=p
	kq3=-p
	kq4=p*2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=thay_conic(f"Parabol có phương trình chính tắc là $y^2={kq}x$.")

	#Tạo các phương án
	pa_A= thay_conic(f"*$y^2={kq}x$")
	pa_B= thay_conic(f"$y^2={kq2}x$")
	pa_C= thay_conic(f"$y^2={kq3}x$")
	pa_D= thay_conic(f"$y^2={kq4}x$")

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

#[D10_CX_B4_24]-M1. Viết phương trình parabol có tiêu điểm.
def gghik_L10_CX_B4_24():
	x,y=sp.symbols("x y")
	p=random.randint(1,20)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, parabol ${{(P)}}$ có tiêu điểm $F\\left({phan_so(p/2)};0\\right)$ có phương trình chính tắc là"        
	
	kq=2*p
	kq2=p
	kq3=-p
	kq4=p*2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=thay_conic(f"Parabol có tham số tiêu $p=2.{phan_so(p/2)}={p}$ nên có phương trình chính tắc là $y^2={kq}x$.")

	#Tạo các phương án
	pa_A= thay_conic(f"*$y^2={kq}x$")
	pa_B= thay_conic(f"$y^2={kq2}x$")
	pa_C= thay_conic(f"$y^2={kq3}x$")
	pa_D= thay_conic(f"$y^2={kq4}x$")

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


#[D10_CX_B4_25]-M2. Viết phương trình parabol có đường chuẩn.
def gghik_L10_CX_B4_25():
	x,y=sp.symbols("x y")
	p=random.randint(1,20)

	noi_dung= f"Trong mặt phẳng ${{Oxy}}$, parabol ${{(P)}}$ có đường chuẩn $x+{phan_so(p/2)}=0$ có phương trình chính tắc là"        
	
	kq=2*p
	kq2=p
	kq3=-p
	kq4=p*2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	noi_dung_loigiai=thay_conic(f"Parabol có tham số tiêu $p=2.{phan_so(p/2)}={p}$ nên có phương trình chính tắc là $y^2={kq}x$.")

	#Tạo các phương án
	pa_A= thay_conic(f"*$y^2={kq}x$")
	pa_B= thay_conic(f"$y^2={kq2}x$")
	pa_C= thay_conic(f"$y^2={kq3}x$")
	pa_D= thay_conic(f"$y^2={kq4}x$")

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