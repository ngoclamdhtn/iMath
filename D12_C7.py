import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module

######### BÀI 1: MẶT NÓN ######### 
#[D12_C7_B1_01]. Cho hình nón có bán kính r và đường sinh l. Tính S_xq. 
def zz8zz_L12_C7_B1_01():
	r = random.randint(2,10)
	l = r + random.randint(3,7)
	kq= r*l
	kq2 = 2*r*l
	kq3 = r*l+r**2
	kq4 = r**2*l

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{latex(kq)}}}\\pi$"
	pa_B= f"${{{latex(kq2)}}}\\pi$"
	pa_C= f"${{{latex(kq3)}}}\\pi$"
	pa_D= f"${{{latex(kq4)}}}\\pi$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	
	noi_dung = f"Cho hình nón có bán kính đáy bằng ${{{r}}}$ và độ dài đường sinh bằng ${{{l}}}$. Tính diện tích xung quanh của hình nón đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
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


#[D12_C7_B1_02]. Cho hình nón có bán kính r và chiều cao h. Tính V. 
def zz8zz_L12_C7_B1_02():
	r = random.randint(2,4)
	h = r + random.randint(4,6)
	kq= 1/3*r**2*h
	kq2 = r**2*h
	kq3 = r**2
	kq4 = r**2+h

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{latex(my_module.hien_phan_so(kq))}}}\\pi$"
	pa_B= f"${{{latex(kq2)}}}\\pi$"
	pa_C= f"${{{latex(kq3)}}}\\pi$"
	pa_D= f"${{{latex(kq4)}}}\\pi$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình nón có bán kính đáy bằng ${{{r}}}$ và chiều cao bằng ${{{h}}}$. Tính thể tích của khối nón đã cho.\n"
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D12_C7_B1_03]. Cho hình nón có chu vi đáy và đường sinh. Tính chiều cao h. 
def zz8zz_L12_C7_B1_03():
	r = random.randint(2,6)
	l = r + random.randint(2,8)
	h= sqrt(l**2 - r**2)
	chu_vi = 2*pi*r
	kq= latex(h)
	kq2 = latex(sqrt(l**2 + r**2))
	kq3 = latex(sqrt(r))
	kq4 = latex(sqrt(l + r))
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f" Cho hình nón có chu vi đáy bằng ${latex(chu_vi)}$ và độ dài đường sinh bằng ${{{l}}}$. Tính chiều cao của hình nón đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D12_C7_B1_04]. Cho hình nón có diện tích đáy và đường sinh. Tính chiều cao h. 
def zz8zz_L12_C7_B1_04():
	r = random.randint(2,8)
	l = r + random.randint(2,8)
	h= sqrt(l**2 - r**2)
	dien_tich = pi*(r**2)
	kq= latex(h)
	kq2 = latex(sqrt(l**2 + r**2))
	kq3 = latex(sqrt(r))
	kq4 = latex(sqrt(l + r))
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình nón có diện tích đáy bằng ${latex(dien_tich)}$ và độ dài đường sinh bằng ${{{l}}}$. Tính chiều cao của hình nón đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

######### BÀI 2: MẶT TRỤ ######### 
#[D12_C7_B2_01]. Cho hình trụ có bán kính r và đường sinh l. Tính S_xq. 
def zz8zz_L12_C7_B2_01():
	r = random.randint(2,10)
	l = r + random.randint(3,7)
	kq= 2*r*l
	kq2 = r*l
	kq3 = r*l+2*r**2
	kq4 = r*l+r**2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{kq}\\pi}}$"
	pa_B= f"${{{kq2}\\pi}}$"
	pa_C= f"${{{kq3}\\pi}}$"
	pa_D= f"${{{kq4}\\pi}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung= f"Cho hình trụ có bán kính đáy bằng ${{{r}}}$ và độ dài đường sinh bằng ${{{l}}}$. Tính diện tích xung quanh của hình trụ đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D12_C7_B2_02]. Cho hình trụ có bán kính r và đường sinh l. Tính V. 
def zz8zz_L12_C7_B2_02():
	r = random.randint(2,10)
	l = r + random.randint(3,7)
	kq= r**2*l
	kq2 =1/3*r**2*l
	kq3 = r*l
	kq4 = 2*r*l+2*r**2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{latex(kq)}\\pi}}$"
	pa_B= f"${{{latex(my_module.hien_phan_so(kq2))}\\pi}}$"
	pa_C= f"${{{latex(kq3)}\\pi}}$"
	pa_D= f"${{{latex(kq4)}\\pi}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho khối trụ có bán kính đáy bằng ${{{r}}}$ và độ dài đường sinh bằng ${{{l}}}$. Tính thể tích của khối trụ đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D12_C7_B2_03]. Cho hình trụ có thiết diện qua trục là hình vuông. Tính S_tp. 
def zz8zz_L12_C7_B2_03():
	r = random.randint(2,10)
	l = 2*r 
	choice = random.choice(["chu vi","diện tích"])
	if choice == "chu vi":
		input_choice = latex(4*l)
	else:
		input_choice = latex(l**2)
	kq= 2*r*l + 2*r**2
	kq2 = r**2*l
	kq3 = 2*r*l + r**2
	kq4 = r*l+2*r**2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	pa_A= f"*${{{kq}\\pi}}$"
	pa_B= f"${{{kq2}\\pi}}$"
	pa_C= f"${{{kq3}\\pi}}$"
	pa_D= f"${{{kq4}\\pi}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình trụ có thiết diện qua trục là hình vuông với {choice} bằng ${{{input_choice}}}$. Tính diện tích toàn phần của hình trụ đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D12_C7_B2_04]. Cho hình trụ có thiết diện qua trục là hình chữ nhật. Tính S_tp. 
def zz8zz_L12_C7_B2_04():
	r = random.randint(2,6)
	l = r + random.randint(2,6) 
	choice = random.choice(["chu vi","diện tích"])	
	if choice == "chu vi":
		input_choice = latex(2*(l+2*r))
	else:
		input_choice = latex(l*(2*r))

	choice_r_l=random.choice(["r","l"])
	if choice_r_l == "r":
		name_choice_r_l = "bán kính"
		input_choice_r_l = {r}
	else:
		name_choice_r_l = "đường sinh"
		input_choice_r_l = {l}

	kq= latex(2*pi*r*l + 2*pi*r**2)
	kq2 = latex(pi*r**2*l)
	kq3 = latex(2*pi*r*l + pi*r**2)
	kq4 = latex(pi*r*l+2*pi*r**2)
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho hình trụ có thiết diện qua trục là hình chữ nhật với {choice} bằng ${{{input_choice}}}$ và độ dài {name_choice_r_l} bằng ${{{input_choice_r_l}}}$. Tính diện tích toàn phần của hình trụ đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#######################################################

######### BÀI 3: MẶT CẦU ######### 
#[D12_C7_B3_01]. Cho mặt cầu có bán kính r. Tính S_mc. 
def zz8zz_L12_C7_B3_01():
	r = random.randint(2,13)
	kq= latex(4*pi*r**2)
	kq2 = latex(pi*r**2)
	kq3 = latex(my_module.hien_phan_so(4/3*r**3))
	kq4 = latex(2*pi*r)
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}\\pi}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mặt cầu có bán kính bằng ${{{r}}}$. Tính diện tích mặt cầu đã cho.\n"
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#[D12_C7_B3_02]. Cho mặt cầu có thể tích. Tính bán kính R. 
def zz8zz_L12_C7_B3_02():
	r = random.randint(3,13)
	v =latex(my_module.hien_phan_so(4/3*r**3))
	kq= r
	kq2 = 2*r
	kq3 = latex(sqrt(r))
	kq4 = r**2

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{kq}a}}$"
	pa_B= f"${{{kq2}a}}$"
	pa_C= f"${{{kq3}a}}$"
	pa_D= f"${{{kq4}a}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mặt cầu có thể tích bằng ${v}\\pi a^3$. Tính bán kính mặt cầu đã cho."
	noi_dung_loigiai=f""
	debai= f"{noi_dung}\n"
	
	dap_an=my_module.tra_ve_dap_an(list_PA)
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t    C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	
	
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

#print(D12_C7_B2_02())