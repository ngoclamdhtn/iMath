import math
import sympy as sp
import numpy as np
from sympy import *
import random
from fractions import Fraction
import my_module
from collections import Counter
def round_half_up(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5 * (1 if n > 0 else -1)) / multiplier

def find_mode(my_list):
    # Đếm số lần xuất hiện của các phần tử trong danh sách
    count = Counter(my_list)
    
    # Tìm số lần xuất hiện cao nhất
    max_count = max(count.values())
    
    # Lọc các phần tử có số lần xuất hiện bằng max_count
    most_frequent = [key for key, value in count.items() if value == max_count]
    
    return most_frequent

def group_by_frequency(lst):
    # Đếm số lần xuất hiện của mỗi phần tử
    frequency_count = Counter(lst)
    
    # Tạo một dictionary với key là số lần xuất hiện và value là danh sách các phần tử có số lần xuất hiện đó
    grouped = {}
    for value, count in frequency_count.items():
        grouped.setdefault(count, []).append(value)

    return grouped

def find_mode_2(lst):
    # Lấy danh sách các giá trị được nhóm theo số lần xuất hiện
    grouped = group_by_frequency(lst)
    
    # Tìm số lần xuất hiện lớn nhất
    max_frequency = max(grouped.keys())
    
    # Lấy danh sách các giá trị có số lần xuất hiện lớn nhất
    return max_frequency, grouped[max_frequency]

def phan_so(t):
    m=latex(Rational(t).limit_denominator(100000000000))
    return m

def calculate_mode(data):
    unique_values, counts = np.unique(data, return_counts=True)
    max_count_index = np.argmax(counts)
    mode_value = unique_values[max_count_index]
    mode_count = counts[max_count_index]
    return mode_value, mode_count

#Chương 6 - Bài 1: Số gần đúng và sai số
#[D10_C6_B1_01]-M2. Viết số quy tròn của số nguyên có độ chính xác cho trước.
def tktk_L10_C6_B1_01():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	a = random.randint(1100, 1000000)	

	# Tạo số nguyên nhỏ hơn a
	len_a=int(len(str(a)))
	b=10**(random.randint(2,len_a-2))
	t_d=random.randint(1,4)
	d=t_d*b
	len_d=int(len(str(d)))
	decimal_position = -len_d

	kq=round(a, decimal_position)
	kq2=round(a, decimal_position+1)
	kq3=round(a, decimal_position-1)
	kq4=a
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

	noi_dung_1=f"Cho số gần đúng $a={a}$ với độ chính xác $d={d}$. Hãy viết số quy tròn của số $a$."
	noi_dung_2=f"Hãy viết số quy tròn của số gần đúng $a={a}\\pm {d}$."
	noi_dung=random.choice([noi_dung_1,noi_dung_2])

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

#Quy tròn số thập phân với sai số
#[D10_C6_B1_02]-M2. Viết số quy tròn của số thập phân có độ chính xác cho trước.
def tktk_L10_C6_B1_02():
	chon=random.randint(1,2)
	
	if chon==1:
		b = random.randint(10120, 998877)
		a=b/10000
		st_a=f"{round(a,5):.4f}".replace(".",",")


		d=random.randint(1,6)/100
		st_d=f"{round(d,2):.2f}".replace(".",",")

		kq=f"{round(a, 1):.1f}".replace(".",",")
		kq2=f"{round(a, 2):.2f}".replace(".",",")
		kq3=f"{round(a, 3):.3f}".replace(".",",")
		kq4=f"{round(a+random.choice([0.4,0.5,0.2]), 1):.1f}".replace(".",",")
	
	if chon==2:
		b = random.randint(101205, 998877)
		chon=random.randint(1,2)
		if chon==1:
			a=b/100000
			st_a=f"{round(a,5):.5f}".replace(".",",")
		
		if chon==2:
			a=b/10000
			st_a=f"{round(a,4):.4f}".replace(".",",")	
		

		d=random.randint(1,6)/1000
		st_d=f"{round(d,3):.3f}".replace(".",",")

		kq=f"{round(a, 2):.2f}".replace(".",",")
		kq2=f"{round(a, 4):.4f}".replace(".",",")
		kq3=f"{round(a, 3):.3f}".replace(".",",")
		kq4=f"{round(a+random.choice([0.4,0.5,0.2]), 2):.2f}".replace(".",",")
	
	ten=random.choice(["a","b","c","m","e" ])
	noi_dung_1=f"Cho số gần đúng ${ten}={st_a}$ với độ chính xác $d={st_d}$. Hãy viết số quy tròn của số $a$."
	noi_dung_2=f"Hãy viết số quy tròn của số gần đúng ${ten}={st_a}\\pm {st_d}$."
	noi_dung=random.choice([noi_dung_1,noi_dung_2])

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)

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



#[D10_C6_B1_03]-SA-M2. Viết số quy tròn của số nguyên có độ chính xác cho trước.
def tktk_L10_C6_B1_03():
	chon=random.randint(1,2)
	if chon==1:
		a=random.randint(1000,8000)
		chon=random.randint(1,2)
		if chon==1:
			d=random.randint(1,9)
			dap_an=round(a,-1)
		if chon==2:
			d=random.randint(10,50)
			dap_an=round(a,-2)	
		if chon==3:
			d=random.randint(100,200)
			dap_an=round(a,-3)	
	if chon==2:
		a=random.randint(100,800)
		chon=random.randint(1,2)
		if chon==1:
			d=random.randint(1,9)
			dap_an=round(a,-1)
		if chon==2:
			d=random.randint(10,50)
			dap_an=round(a,-2)	

	ten=random.choice(["a","b","c","m","e" ])
	noi_dung_1=f"Cho số gần đúng ${{{a}}}$ với độ chính xác $d={{{d}}}$. Hãy viết số quy tròn của số $a$."
	noi_dung_2=f"Hãy viết số quy tròn của số gần đúng ${ten}={a}\\pm {d}$."
	noi_dung=random.choice([noi_dung_1,noi_dung_2])

	noi_dung_loigiai=(
	f"Số quy tròn của ${ten}={a}\\pm {d}$ là ${{{dap_an}}}$."
	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C6_B1_04]-SA-M2. Viết số quy tròn của số thập phân có độ chính xác cho trước.
def tktk_L10_C6_B1_04():	

	chon=random.randint(1,2)

	if chon==1:
		a=random.randint(1000,8000)/1000
		st_a=f"{round_half_up(a,3):.3f}".replace(".",",")
		

		d=random.randint(3,9)/100
		d=f"{round_half_up(d,2):.2f}".replace(".",",")

		dap_an=f"{round_half_up(a,1):.1f}".replace(".",",")	
	
	if chon==2:
		a=random.randint(10000,80000)/100
		st_a=f"{round_half_up(a,2):.2f}".replace(".",",")

		d=random.randint(3,9)/10
		d=f"{round_half_up(d,1):.1f}".replace(".",",")

		dap_an=f"{round_half_up(a,0):.0f}".replace(".",",")

	
	ten=random.choice(["a","b","c","m","e" ])
	noi_dung_1=f"Cho số gần đúng ${{{st_a}}}$ với độ chính xác $d={{{d}}}$. Hãy viết số quy tròn của số $a$."
	noi_dung_2=f"Hãy viết số quy tròn của số gần đúng ${ten}={st_a}\\pm {d}$."
	noi_dung=random.choice([noi_dung_1,noi_dung_2])

	noi_dung_loigiai=(
	f"Số quy tròn của ${ten}={st_a}\\pm {d}$ là ${{{dap_an}}}$."
	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#Chương 6 - Bài 3: Các số đặc trưng đo xu thế trung tâm của mẫu số liệu
#[D10_C6_B3_01]. Cho dãy số liệu. Tính số trung bình.
def tktk_L10_C6_B3_01():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]
	
	kq = np.mean(sample_data) # Tính giá trị trung bình
	kq2= np.var(sample_data) # Tính phương sai
	kq3= np.median(sample_data) # Tính trung vị
	# Tính tứ phân vị
	quantiles = np.percentile(sample_data, [25, 50, 75])
	kq4= quantiles[0]

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	kq=list_PA[0]
	kq2=list_PA[1]
	kq3=list_PA[2]
	kq4=list_PA[3]

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
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tính số trung bình của mẫu số liệu đã cho."

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

#[D10_C6_B3_02]. Cho dãy số liệu. Tính số trung vị.
def tktk_L10_C6_B3_02():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]
	
	kq =np.median(sample_data)  # Tính trung vị 
	kq2= np.var(sample_data) # Tính phương sai
	kq3=np.mean(sample_data)  # Tính giá trị trung bình
	# Tính tứ phân vị
	quantiles = np.percentile(sample_data, [25, 50, 75])
	kq4= quantiles[0]
	#kq4=np.median(sample_data)+random.randint(1,3)

	#list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	# kq=list_PA[0]
	# kq2=list_PA[1]
	# kq3=list_PA[2]
	# kq4=list_PA[3]

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{phan_so(kq)}}}$"
	pa_B= f"${{{phan_so(kq2)}}}$"
	pa_C= f"${{{phan_so(kq3)}}}$"
	pa_D= f"${{{phan_so(kq4)}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tìm trung vị của mẫu số liệu đã cho."

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



#[D10_C6_B3_03]. Cho dãy số liệu. Tính mốt.
def tktk_L10_C6_B3_03():
	t=random.randint(8,14)
	mau_solieu=[random.randint(7,30) for i in range(t)]	
	max_freq, result = find_mode_2(mau_solieu)

	list_not_most=[x for x in mau_solieu if x not in result]	
	while  len(list_not_most)<4:
		t=random.randint(8,14)
		mau_solieu=[random.randint(7,30) for i in range(t)]	
		max_freq, result = find_mode_2(mau_solieu)

		list_not_most=[x for x in mau_solieu if x not in result]	
		
	kq =result[0]
	kq2,kq3,kq4=list_not_most[0:3]

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{int(kq2)}}}$"
	pa_C= f"${{{int(kq3)}}}$"
	pa_D= f"${{{int(kq4)}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Giá trị nào sau đây là một mốt của mẫu số liệu đã cho.".replace("[","").replace("]","")
	
	noi_dung_loigiai=f"Mốt của mẫu số liệu đã cho là: ${{{result}}}$ với tần số xuất hiện là {max_freq}.".replace("[","").replace("]","")
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

#[D10_C6_B3_04]. Cho dãy số liệu. Tính tứ phân vị thứ nhất
def tktk_L10_C6_B3_04():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]
	
	kq =my_module.tu_phan_vi(sample_data)[0]  #Tính tứ phân vị thứ nhất
	kq2=my_module.tu_phan_vi(sample_data)[1]  # Tính trung vị
	kq3=np.mean(sample_data)  # Tính giá trị trung bình
	kq4=my_module.tu_phan_vi(sample_data)[2]   #Tính tứ phân vị thứ hai 

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	kq=list_PA[0]
	kq2=list_PA[1]
	kq3=list_PA[2]
	kq4=list_PA[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tính tứ phân vị thứ nhất $Q_1$ của mẫu số liệu đã cho."

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


#[D10_C6_B3_05]. Cho dãy số liệu. Tính tứ phân vị thứ hai
def tktk_L10_C6_B3_05():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]

	
	kq =my_module.tu_phan_vi(sample_data)[1] #Tính tứ phân vị thứ hai
	kq2= my_module.tu_phan_vi(sample_data)[0]  #Tính tứ phân vị thứ nhất
	kq3=np.mean(sample_data)  # Tính giá trị trung bình
	kq4= my_module.tu_phan_vi(sample_data)[2]  #Tính tứ phân vị thứ ba

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	kq=list_PA[0]
	kq2=list_PA[1]
	kq3=list_PA[2]
	kq4=list_PA[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tính tứ phân vị thứ hai $Q_2$ của mẫu số liệu đã cho."
	
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

#[D10_C6_B3_06]. Cho dãy số liệu. Tính tứ phân vị thứ ba
def tktk_L10_C6_B3_06():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]
	
	kq =my_module.tu_phan_vi(sample_data)[2] #Tính tứ phân vị thứ ba
	kq2= my_module.tu_phan_vi(sample_data)[0]  # Tính tứ phân vị thứ hai
	kq3=np.mean(sample_data)  # Tính giá trị trung bình
	kq4= my_module.tu_phan_vi(sample_data)[1]# Tính trung vị

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	kq=list_PA[0]
	kq2=list_PA[1]
	kq3=list_PA[2]
	kq4=list_PA[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"
	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tính tứ phân vị thứ ba $Q_3$ của mẫu số liệu đã cho."

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

#[D10_C6_B3_07]-TF-M2. Cho dãy số liệu. Xét Đ-S: số trung bình, trung vị, mốt, khoảng tứ phân vị
def tktk_L10_C6_B3_07():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	data=sample_data.tolist()	

	max_freq, list_mode = find_mode_2(data)
	list_not_mode=[x for x in data if x not in list_mode]

	

	mau_solieu=str(sample_data)	
	mau_solieu=mau_solieu.split()	
	mau_solieu="; ".join(mau_solieu)

	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]		

	noi_dung = f"Cho mẫu số liệu ${{{mau_solieu}}}$. Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười):"		
	debai_word= f"{noi_dung}\n"
	
	st=""
	for x in data:
		st+=f"{x}+"
	st=st[:-1]
	so_trungbinh=f"{round(np.mean(sample_data),1):.1f}".replace(".",",")
	so_trungbinh_false=f"{round(np.mean(sample_data)+random.choice([0.2, 0.4,0.5, random.randint(1,2)]),1):.1f}".replace(".",",")
	kq1_T=f"* Số trung bình của mẫu số liệu là ${{{so_trungbinh}}}$"
	kq1_F=f"Số trung bình của mẫu số liệu là ${{{so_trungbinh_false}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"$\\overline{{x}}=\\dfrac{{{st}}}{{{so_luong}}}={so_trungbinh}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	trung_vi_round= f"{round(my_module.tu_phan_vi(sample_data)[1],1):.1f}".replace(".",",")
	trung_vi_false= f"{round(my_module.tu_phan_vi(sample_data)[1]+random.choice([0.2, 0.4,0.5, random.randint(1,2)]),1):.1f}".replace(".",",")
	
	
	data.sort()
	st_data_sort=", ".join(map(str, data))

	kq2_T=f"* Số trung vị của mẫu số liệu là ${{{trung_vi_round}}}$"
	kq2_F=f"Số trung vị của mẫu số liệu là ${{{trung_vi_false}}}$"
	kq2=random.choice([kq2_T, kq2_F])
	n=len(data)
	if n%2!=0: # n lẻ
		trung_vi=data[n//2]
		HDG=(f"Sắp xếp dãy số liệu ta được: ${{{st_data_sort}}}$.\n\n"
			f"Số phần tử là $n={n}$ (lẻ) nên trung vị là số chính giữa: ${{{trung_vi}}}$.")
	else:
		trung_vi=(data[n//2-1]+data[n//2])/2
		HDG=(f"Sắp xếp dãy số liệu ta được: ${{{st_data_sort}}}$.\n\n"
			f"Số phần tử là $n={n}$ (chẵn) nên trung vị là : $\\dfrac{{{data[n//2-1]} +{data[n//2]} }}{{2}}={phan_so(trung_vi)}={trung_vi_round}$.")	
		
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"



	kq3_T=f"* Mốt của mẫu số liệu là ${{{list_mode}}}$".replace("[","").replace("]","")
	kq3_F=f"Mốt của mẫu số liệu là ${{{list_not_mode[0]}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f" Các mốt của mẫu số liệu là: {list_mode}.\n"
		)
	HDG=HDG.replace("[","").replace("]","")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	Q1 = my_module.tu_phan_vi(sample_data)[0]
	Q1_round=f"{round(Q1,1):.1f}".replace(".",",")

	Q3 = my_module.tu_phan_vi(sample_data)[2]
	Q3_round=f"{round(Q3,1):.1f}".replace(".",",")

	Delta_Q_round=f"{round(Q3-Q1,1):.1f}".replace(".",",")
	Delta_Q_round_false=f"{round(Q3-Q1+random.choice([random.randint(1,20)/10]),1):.1f}".replace(".",",")

	kq4_T=f"* Khoảng tứ phân vị của mẫu số liệu là {Delta_Q_round}"
	kq4_F=f"Khoảng tứ phân vị của mẫu số liệu là {Delta_Q_round_false}" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"Tứ phân vị thứ nhất là $Q_1={Q1_round}$.\n\n"
		f"Tứ phân vị thứ ba là $Q_3={Q3_round}$.\n\n"
		f"Khoảng tứ phân vị của mẫu số liệu là: $\\Delta_Q={Q3_round}-{Q1_round}={Delta_Q_round}$.")
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

#[D10_C6_B3_08]-SA-M2. Cho dãy số liệu. Tính khoảng tứ phân vị.
def tktk_L10_C6_B3_08():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	data=sample_data.tolist()

	mau_solieu=str(sample_data)	
	mau_solieu=mau_solieu.split()	
	mau_solieu="; ".join(mau_solieu)

	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]

	Q1 = my_module.tu_phan_vi(sample_data)[0]
	Q1_round=f"{round(Q1,1):.1f}".replace(".",",")

	Q3 = my_module.tu_phan_vi(sample_data)[2]
	Q3_round=f"{round(Q3,1):.1f}".replace(".",",")

	Delta_Q_round=f"{round(Q3-Q1,1):.1f}".replace(".",",")

	data=sample_data.tolist()
	data.sort()
	st_data_sort=", ".join(map(str, data))

	noi_dung = f"Cho mẫu số liệu ${{{mau_solieu}}}$. Tính khoảng tứ phân vị của mẫu số liệu (các kết quả làm tròn đến hàng phần mười):"	
	dap_an=Delta_Q_round

	noi_dung_loigiai=(
		f"Sắp xếp dãy số liệu ta được: ${{{st_data_sort}}}$.\n\n"
	f"Tứ phân vị thứ nhất là $Q_1={Q1_round}$.\n\n"
		f"Tứ phân vị thứ ba là $Q_3={Q3_round}$.\n\n"
		f"Khoảng tứ phân vị của mẫu số liệu là: $\\Delta_Q={Q3_round}-{Q1_round}={Delta_Q_round}$."	
	)	
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C6_B3_09]-TF-M2. Cho dãy số liệu. Xét Đ-S: trung vị, Q1-Q3, khoảng tứ phân vị, giá trị ngoại lệ
def tktk_L10_C6_B3_09():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(2,7)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b	

	mau_solieu=str(sample_data)	
	mau_solieu=mau_solieu.split()	
	mau_solieu="; ".join(mau_solieu)

	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]		

	noi_dung = f"Cho mẫu số liệu ${{{mau_solieu}}}$ . Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười):"		

	trung_vi_round= f"{round(my_module.tu_phan_vi(sample_data)[1],1):.1f}".replace(".",",")
	trung_vi_false= f"{round(my_module.tu_phan_vi(sample_data)[1]+random.choice([0.2, 0.4,0.5, random.randint(1,2)]),1):.1f}".replace(".",",")
	
	data=sample_data.tolist()
	data.sort()
	st_data_sort=", ".join(map(str, data))

	kq1_T=f"* Số trung vị của mẫu số liệu là ${{{trung_vi_round}}}$"
	kq1_F=f"Số trung vị của mẫu số liệu là ${{{trung_vi_false}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	n=len(data)
	if n%2!=0: # n lẻ
		trung_vi=data[n//2]
		HDG=(f"Sắp xếp dãy số liệu ta được: ${{{st_data_sort}}}$.\n\n"
			f"Số phần tử là $n={n}$ (lẻ) nên trung vị là số chính giữa: ${{{trung_vi}}}$.")
	else:
		trung_vi=(data[n//2-1]+data[n//2])/2
		HDG=(f"Sắp xếp dãy số liệu ta được: ${{{st_data_sort}}}$.\n\n"
			f"Số phần tử là $n={n}$ (chẵn) nên trung vị là : $\\dfrac{{{data[n//2-1]} +{data[n//2]} }}{{2}}={phan_so(trung_vi)}={trung_vi_round}$.")	
		
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	Q1 = my_module.tu_phan_vi(sample_data)[0]
	Q1_round=f"{round(Q1,1):.1f}".replace(".",",")
	Q1_round_false=f"{round(Q1+random.choice([random.randint(1,20)/10]),1):.1f}".replace(".",",")

	Q3 = my_module.tu_phan_vi(sample_data)[2]
	Q3_round=f"{round(Q3,1):.1f}".replace(".",",")
	Q3_round_false=f"{round(Q3+random.choice([random.randint(1,20)/10]),1):.1f}".replace(".",",")

	Delta_Q_round=f"{round(Q3-Q1,1):.1f}".replace(".",",")
	Delta_Q_round_false=f"{round(Q3-Q1+random.choice([random.randint(1,20)/10]),1):.1f}".replace(".",",")

	chon=random.randint(1,2)
	if chon==1:
		kq2_T=f"* Tứ phân vị thứ nhất là {Q1_round}"
		kq2_F=f"Tứ phân vị thứ nhất là {Q1_round_false}" 
		
		HDG=(f"Tứ phân vị thứ nhất là $Q_1={Q1_round}$.\n\n")
	
	if chon==2:
		kq2_T=f"* Tứ phân vị thứ ba là {Q3_round}"
		kq2_F=f"Tứ phân vị thứ ba là {Q3_round_false}" 
		
		HDG=(f"Tứ phân vị thứ ba là $Q_3={Q3_round}$.\n\n")
	
	kq2=random.choice([kq2_T, kq2_F])
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	kq3_T=f"* Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q={Delta_Q_round}$" 
	kq3_F=f"Khoảng tứ phân vị của mẫu số liệu là $\\Delta_Q={Delta_Q_round_false}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"Tứ phân vị thứ nhất là $Q_1={Q1_round}$.\n\n"
			f"Tứ phân vị thứ ba là $Q_3={Q3_round}$.\n\n"
			f"Khoảng tứ phân vị của mẫu số liệu là: $\\Delta_Q={Q3_round}-{Q1_round}={Delta_Q_round}$.")
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	Delta_Q=Q3-Q1	
	x_1,x_3=Q1-1.5*Delta_Q, Q3+1.5*Delta_Q
	x_1_round=f"{round(x_1,1):.1f}".replace(".",",")
	x_3_round=f"{round(x_3,1):.1f}".replace(".",",")

	chon=random.randint(1,2)

	if chon==1:
		#Tạo giá trị ngoại lệ
		x_0=random.choice([
		x_1-random.choice([random.randint(2,15)/10]),
		x_3+random.choice([random.randint(2,15)/10])])

		x_0=f"{round(x_0,1):.1f}".replace(".",",")

		kq4_T=f"* ${{{x_0}}}$ là giá trị ngoại lệ của mẫu số liệu"
		kq4_F=f"${{{x_0}}}$ không phải là giá trị ngoại lệ của mẫu số liệu" 
		
		HDG=(f"Ta có: $Q_1-1,5\\Delta_Q={x_1_round}$, $Q_3+1,5\\Delta_Q={x_3_round}$.\n\n"
			f"Vì ${{{x_0}}}$ không thuộc đoạn $[{x_1_round};{x_3_round}]$ nên ${{{x_0}}}$ là giá trị ngoại lệ.")
	
	if chon==2:
		#Tạo giá trị không ngoại lệ
		x_0=random.choice([
		x_1+random.choice([random.randint(2,15)/10]),
		x_3-random.choice([random.randint(2,15)/10])])
		
		x_0=f"{round(x_0,1):.1f}".replace(".",",")

		kq4_T=f"* ${{{x_0}}}$ không phải là giá trị ngoại lệ của mẫu số liệu"
		kq4_F=f"${{{x_0}}}$ là giá trị ngoại lệ của mẫu số liệu" 
		
		HDG=(f"Ta có: $Q_1-1,5\\Delta_Q={x_1_round}$, $Q_3+1,5\\Delta_Q={x_3_round}$.\n\n"
			f"Vì ${{{x_0}}}$ thuộc đoạn $[{x_1_round};{x_3_round}]$ nên ${{{x_0}}}$ không phải là giá trị ngoại lệ.")	

	
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




#[D10_C6_B3_10]-M2. CHo biểu đồ cột thống kế số từ mới học mỗi ngày. Tính TBC
def tktk_L10_C6_B3_10():
    A=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường","Khôi", "Giang", "Lam", "Hà", "Thái"])
    n=random.randint(5,8)
    b = random.randint(2*n-7, 2*n)
    c = random.randint(2*n-7, 2*n)
    d = random.randint(3, 2*n)

    # Tính số còn lại e sao cho tổng đúng 100
    a = random.randint(2*n-5, 2*n)
    e = random.randint(6, 2*n)
    
    a1,b1,c1,d1,e1= sorted(random.sample(range(5, 21), 5))
    so=random.choice([c1,d1,e1])
    code_hinh = fr"""
    \begin{{tikzpicture}}[y=0.3cm,x=0.8cm]
        %\draw[color=gray!50,line width=1.5pt]  (-1,-2.4)--(14.6,-2.4)--(14.6,6.5)--(-1,6.5)--cycle ;
        \foreach \i  in {{2,4,...,{2*n}}} 
        {{
            \draw (0,\i) node[left]{{$\i$}};
            \draw (-0.1,\i)--(0.1,\i) ;
            \draw[gray!40] (0.5,\i)--(11.5,\i);
        }}
        
        \foreach \x/\y/\z in {{2/{a1}/{a},4/{b1}/{b},6/{c1}/{c},8/{d1}/{d},10/{e1}/{e}}} 
        {{
            \draw ({{\x}},0) node[below]{{$\y$}};
            \draw ({{\x}},{{\z}}) node[above]{{$\z$}};
        }}
        \draw [->] (0,0)--(11.5,0) node[below right]{{Số từ mới}};
        \draw [->] (0,0)--(0,{2*n+1}) node[above]{{\text{{Số ngày}}}};
        \draw [pattern=north east lines]  (1.6,0)--(1.6,{a})--(2.4,{a})--(2.4,0)--cycle   
        (3.6,0)--(3.6,{b})--(4.4,{b})--(4.4,0)--cycle  
        (5.6,0)--(5.6,{c})--(6.4,{c})--(6.4,0)--cycle   
         (7.6,0)--(7.6,{d})--(8.4,{d})--(8.4,0)--cycle   
         (9.6,0)--(9.6,{e})--(10.4,{e})--(10.4,0)--cycle   ;
        %[pattern=north east lines]
    \end{{tikzpicture}}

    """
    ts=[a,b,c,d,e]
    gt=[a1,b1,c1,d1,e1]
    i=random.randint(0,4)
    gt=gt[i]
    ts=ts[i]
    kc= (a*a1+b*b1+c*c1+d*d1+e*e1)/(a+b+c+d+e)
    tbc="{:.1f}".format(kc).replace(".", ",")
    noi_dung =(f"Vào đợt nghỉ hè vừa rồi, mỗi ngày bạn {A} đều học thêm một số từ vựng tiếng Anh mới. Số lượng từ vựng mới bạn {A} học mỗi ngày được biểu diễn ở biểu đồ cột như hình dưới.\n\n"
        f"Tính trung bình cộng lượng từ mới học mỗi ngày.")

    noi_dung_loigiai=(f"TBC là $\\overline{{x}}= \\dfrac{{{a} . {a1}+{b}.{b1}+{c}.{c1}+{d}.{d1}+{e}.{e1}}}{{{a}+{b}+{c}+{d}+{e}}} \\approx {tbc}$")

    kq=f"${{{tbc}}}$ "
    dss=[f"${{{"{:.1f}".format(kc+0.4).replace(".", ",")}}}$  ",
    f"${{{"{:.1f}".format(kc+1).replace(".", ",")}}}$   ",
    f" ${{{"{:.1f}".format(kc-1).replace(".", ",")}}}$ "  ,    
    f" ${{{"{:.1f}".format(kc+0.5).replace(".", ",")}}}$  "  ]
    kq2,kq3,kq4=random.sample(dss,3)    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    list_PA = [pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an = my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)



    debai=(f"{noi_dung}\n"
        f"{file_name}\n")

    phuongan = f"A. {list_PA[0]}\t   B. {list_PA[1]}\t    C. {list_PA[2]}\t   D. {list_PA[3]}\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề LaTeX
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
        
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an










#[D10_C6_B3_11]-M2. CHo bảng thống kế số anh chị em ruột. Tìm TBC
def tktk_L10_C6_B3_11():
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])

    n0=random.randint(1,5)
    n1=random.randint(15,25)
    n2=random.randint(1,5)
    n3=random.randint(1,3)
    n4=random.randint(1,2)

    ts=[n0,n1,n2,n3,n4]
    gt=[0,1,2,3,4]
    i=random.randint(0,4)
    gt=gt[i]
    ts=ts[i]
    kc= (n0*0+n1*1+n2*2+n3*3+n4*4)/(n0+n1+n2+n3+n4)
    tbc="{:.1f}".format(kc).replace(".", ",")
    code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}}
        \\hline
                 Số anh chị em ruột & $0$ & 1& $2$ & $3$ & $4$   \\\\
        \\hline
       Số học sinh & ${n0}$ & $ {n1}$ & ${n2}$ & ${n3}$ & ${n4}$  \\\\
        \\hline
    \\end{{tabular}}
    """
    noi_dung=f" Bạn {A} được cô giáo giao nhiệm vụ thống kê số anh chị em ruột của các bạn trong lớp. Kết quả thu được được bạn {A} thống kê bằng bảng dưới đây. Tìm trung bình cộng số lượng anh chị em ruột của mỗi bạn. "

    noi_dung_loigiai=(f"TBC $\\overline{{x}}= \\dfrac{{{n0}. 0+ {n1}. 1+{n2}. 2+{n3}. 3+{n4}. 4  }}{{{n0}+ {n1}+{n2}+{n3}+{n4}}} \\approx {tbc}$.")

    kq=f"${{{tbc}}}$ "
    dss=[f"${{{"{:.1f}".format(kc+0.4).replace(".", ",")}}}$  ",
    f"${{{"{:.1f}".format(kc+1).replace(".", ",")}}}$   ",
    f" ${{{"{:.1f}".format(kc-1).replace(".", ",")}}}$ "  ,    
    f" ${{{"{:.1f}".format(kc+0.5).replace(".", ",")}}}$  "  ]
    kq2,kq3,kq4=random.sample(dss,3)    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    list_PA = [pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an = my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai=(f"{noi_dung}\n"
        f"{file_name}\n")

    phuongan = f"A. {list_PA[0]}\t   B. {list_PA[1]}\t    C. {list_PA[2]}\t   D. {list_PA[3]}\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề LaTeX
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
        
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an





#[D10_C6_B3_12]-M2. CHo bảng thống kế điểm. Tìm TBC
def tktk_L10_C6_B3_12():
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    X=random.choice(["Toán", "Ngoại ngữ", "Văn", "Lý", "Sử", "Địa", "Hoá", "Sinh"])
    y=random.randint(9,12)

    n0=random.randint(1,5)
    n1=random.randint(5,25)
    n2=random.randint(30,100)
    n3=random.randint(100,150)
    n4=random.randint(50,100)
    n6=random.randint(1,5)
    n5=random.randint(1,10)


    ts=n0+n1+n2+n3+n4+n5+n6
    kc= (n0*4+n1*5+n2*6+n3*7+n4*8 +n5*9+n6*10)/(n0+n1+n2+n3+n4+n5+n6)
    tbc="{:.1f}".format(kc).replace(".", ",")
    code_hinh = f"""    
    \\setlength{{\\tabcolsep}}{{12pt}} 
    \\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}}
        \\hline
                 Điểm số & $4$ & 5& $6$ & $7$ & $8$  & $9$ & $10$ \\\\
        \\hline
       Số học sinh & ${n0}$ & $ {n1}$ & ${n2}$ & ${n3}$ & ${n4}$ & ${n5}$ & ${n6}$ \\\\
        \\hline
    \\end{{tabular}}
    """
    noi_dung=f"Nhà trường thống kê điểm thi môn {X} của tất cả học sinh khối ${{{y}}}$ trong kì thi khảo sát chất lượng. Kết quả thống kê bằng bảng dưới đây. Tính điểm trung bình cộng? "

    noi_dung_loigiai=(f"Có $N={n0}+{n1}+{n2}+{n3}+{n4}+{n5}+{n6}={{{ts}}}$ học sinh khối ${{{y}}}$ .\n\n"
    	f"TBC $\\overline{{x}}= \\dfrac{{{n0}.4+{n1}.5+{n2}.6+{n3}.7+{n4}.8+{n5}.9+{n6}.10 }}{{ N}} \\approx {tbc}$")

    kq=f"${{{tbc}}}$ "
    dss=[f"${{{"{:.1f}".format(kc+0.4).replace(".", ",")}}}$  ",
    f"${{{"{:.1f}".format(kc+1).replace(".", ",")}}}$   ",
    f" ${{{"{:.1f}".format(kc-1).replace(".", ",")}}}$ "  ,    
    f" ${{{"{:.1f}".format(kc+0.5).replace(".", ",")}}}$  "  ]
    kq2,kq3,kq4=random.sample(dss,3)    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    list_PA = [pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an = my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai=(f"{noi_dung}\n"
        f"{file_name}\n")

    phuongan = f"A. {list_PA[0]}\t   B. {list_PA[1]}\t    C. {list_PA[2]}\t   D. {list_PA[3]}\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề LaTeX
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
        
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C6_B3_13]-SA-M2. Tính số trung bình của dãy số liệu 7-10 giá trị) theo chủ đề
def tktk_L10_C6_B3_13():

	x = sp.symbols("x")  # giữ cấu trúc, không dùng trong bài này

	ten = random.choice(["Lam", "Minh", "Hùng", "An", "Vinh", "Phương", "Chi"])

	# --- Sinh dữ liệu theo chủ đề ---
	chude = random.choice(["giáo dục", "khoa học", "y tế", "vận tải", "công nghệ", "sinh học"])

	# Mỗi chủ đề chọn bối cảnh, đơn vị, cách sinh số liệu
	if chude == "giáo dục":
		bocanh = "điểm kiểm tra (thang 10) của một nhóm học sinh"
		donvi = "điểm"
		n = random.randint(7, 10)
		data = [random.randint(5, 10) for _ in range(n)]
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng trong thí nghiệm (ms) đo qua các lần thử"
		donvi = "ms"
		n = random.randint(7, 10)
		data = [random.randint(180, 320) for _ in range(n)]
	elif chude == "y tế":
		bocanh = "nhịp tim lúc nghỉ (bpm) của các bệnh nhân trong một ca đo"
		donvi = "bpm"
		n = random.randint(7, 10)
		data = [random.randint(55, 95) for _ in range(n)]
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển (phút) của một tuyến xe qua các ngày"
		donvi = "phút"
		n = random.randint(7, 10)
		data = [random.randint(25, 70) for _ in range(n)]
	elif chude == "công nghệ":
		bocanh = "tốc độ tải xuống (Mbps) đo tại cùng một điểm theo các thời điểm"
		donvi = "Mbps"
		n = random.randint(7, 10)
		data = [random.randint(20, 120) for _ in range(n)]
	else:  # "sinh học"
		bocanh = "chiều cao cây non (cm) trong một thí nghiệm nuôi trồng"
		donvi = "cm"
		n = random.randint(7, 10)
		data = [random.randint(12, 45) for _ in range(n)]

	# (Tuỳ chọn) đảm bảo dữ liệu không quá "đều"
	random.shuffle(data)

	# --- Tính trung bình ---
	tong = sum(data)
	mean = tong / len(data)

	# Đáp án: làm tròn 2 chữ số thập phân (nếu là số nguyên thì vẫn hiển thị dạng số)
	dap_an = round_half_up(mean, 1)

	# Chuỗi dữ liệu hiển thị
	s_data = ", ".join([str(v) for v in data])
	s_mean = f"{round_half_up(float(dap_an), 1):.1f}".rstrip("0").rstrip(".").replace(".", ",")

	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau:"
		f" ${{{s_data}}} $.\n\n"
		f"Hãy tính số trung bình của dãy số liệu trên (kết quả làm tròn đến hàng phần mười)."
	)

	noi_dung_loigiai = (
		f"Dãy số liệu có $n={len(data)}$ giá trị.\n\n"
		f"Tổng các giá trị là:\n\n"
		f"$S={'+'.join([str(v) for v in data])}={tong}$.\n\n"
		f"Số trung bình của dãy là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{S}}{{n}}=\\dfrac{{{tong}}}{{{len(data)}}}={s_mean}$ ({donvi})."
	)
	if mean>100:
		# Đáp án: làm tròn 2 chữ số thập phân (nếu là số nguyên thì vẫn hiển thị dạng số)
		dap_an = mean

		# Chuỗi dữ liệu hiển thị
		s_data = ", ".join([str(v) for v in data])
		s_mean = f"{round_half_up(float(dap_an), 0):.0f}".replace(".", ",")

		noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau:"
		f" ${s_data}$.\n\n"
		f"Hãy tính số trung bình của dãy số liệu trên (kết quả làm tròn đến hàng đơn vị).")

		noi_dung_loigiai = (
		f"Dãy số liệu có $n={len(data)}$ giá trị.\n\n"
		f"Tổng các giá trị là:\n\n"
		f"$S={'+'.join([str(v) for v in data])}={tong}$.\n\n"
		f"Số trung bình của dãy là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{S}}{{n}}=\\dfrac{{{tong}}}{{{len(data)}}}={s_mean}$ ({donvi}).")

	dap_an=f"{dap_an}".replace(".",",")

	debai_word = f"{noi_dung}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_14]-SA-M2. Tính tứ phân vị Q1 của dãy số liệu (7-10 giá trị) theo chủ đề
def tktk_L10_C6_B3_14():
	import random
	import sympy as sp

	x = sp.symbols("x")  # giữ cấu trúc, không dùng trực tiếp

	ten = random.choice(["Lam", "Minh", "Hùng", "An", "Vinh"])

	# --- Chọn chủ đề và sinh dữ liệu ---
	chude = random.choice(["giáo dục", "khoa học", "y tế", "vận tải", "công nghệ", "sinh học"])

	if chude == "giáo dục":
		bocanh = "điểm kiểm tra của một nhóm học sinh"
		donvi = "điểm"
		data = [random.randint(4, 10) for _ in range(random.randint(7, 10))]
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng (ms) trong một thí nghiệm"
		donvi = "ms"
		data = [random.randint(180, 320) for _ in range(random.randint(7, 10))]
	elif chude == "y tế":
		bocanh = "nồng độ đường huyết (mg/dL) của bệnh nhân"
		donvi = "mg/dL"
		data = [random.randint(70, 160) for _ in range(random.randint(7, 10))]
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển (phút) của một tuyến xe"
		donvi = "phút"
		data = [random.randint(25, 90) for _ in range(random.randint(7, 10))]
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu (Mbps) tại một điểm đo"
		donvi = "Mbps"
		data = [random.randint(20, 150) for _ in range(random.randint(7, 10))]
	else:  # sinh học
		bocanh = "chiều cao cây non (cm) trong thí nghiệm sinh học"
		donvi = "cm"
		data = [random.randint(10, 50) for _ in range(random.randint(7, 10))]

	# --- Sắp xếp số liệu ---
	data_sorted = sorted(data)
	n = len(data_sorted)

	# --- Tính Q1 theo chương trình THPT ---
	# Q1 là trung vị của nửa dưới (không tính trung vị chung nếu n lẻ)
	if n % 2 == 0:
		lower_half = data_sorted[:n // 2]
	else:
		lower_half = data_sorted[:n // 2]

	m = len(lower_half)
	if m % 2 == 0:
		Q1 = (lower_half[m//2 - 1] + lower_half[m//2]) / 2
	else:
		Q1 = lower_half[m//2]

	dap_an = float(Q1)

	# --- Chuỗi hiển thị ---
	s_data = ", ".join(str(v) for v in data)
	s_data_sorted = ", ".join(str(v) for v in data_sorted)
	

	if dap_an.is_integer():
		s_Q1 = int(dap_an)
		noi_dung = (
			f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau: "
			f"${{{s_data}}}$.\n\n"
			f"Hãy xác định tứ phân vị thứ nhất $Q_1$ của dãy số liệu trên (đơn vị: {donvi})."
		)

		noi_dung_loigiai = (
			f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
			f"${{{s_data_sorted}}}$.\n\n"
			f"Dãy có $n={n}$ giá trị.\n\n"
			f"Nửa dưới của dãy là: "
			f"${{{', '.join(str(v) for v in lower_half)}}}$.\n\n"
			f"Tứ phân vị thứ nhất $Q_1$ là trung vị của nửa dưới này, do đó:\n\n"
			f"$Q_1={s_Q1}$ ({donvi})."
		)
		dap_an=int(dap_an)
	else:
		if Q1<99:
			s_Q1 = f"{round_half_up(float(dap_an),1):.1f}".rstrip("0").rstrip(".").replace(".", ",")
			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau: "
				f"${{{s_data}}}$.\n\n"
				f"Hãy xác định tứ phân vị thứ nhất $Q_1$ của dãy số liệu trên (kết quả làm tròn đến hàng phần mười)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị.\n\n"
				f"Nửa dưới của dãy là: "
				f"${{{', '.join(str(v) for v in lower_half)}}}$.\n\n"
				f"Tứ phân vị thứ nhất $Q_1$ là trung vị của nửa dưới này, do đó:\n\n"
				f"$Q_1={s_Q1}$ ({donvi})."
			)
			dap_an=f"{round_half_up(dap_an,1):.1f}".replace(".",",")
		else:
			s_Q1 = f"{round_half_up(float(dap_an),0):.0f}".rstrip("0").rstrip(".").replace(".", ",")
			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau: "
				f"${{{s_data}}}$.\n\n"
				f"Hãy xác định tứ phân vị thứ nhất $Q_1$ của dãy số liệu trên (kết quả làm tròn đến hàng đơn vị)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị.\n\n"
				f"Nửa dưới của dãy là: "
				f"${{{', '.join(str(v) for v in lower_half)}}}$.\n\n"
				f"Tứ phân vị thứ nhất $Q_1$ là trung vị của nửa dưới này, do đó:\n\n"
				f"$Q_1={s_Q1}$ ({donvi})."
			)
			dap_an=f"{round_half_up(dap_an,0):.0f}".replace(".",",")



	

	debai_word = f"{noi_dung}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_15]-SA-M2. Tính tứ phân vị Q3 của dãy số liệu theo chủ đề
def tktk_L10_C6_B3_15():
	import random
	import sympy as sp

	x = sp.symbols("x")  # giữ cấu trúc, không dùng trực tiếp

	ten = random.choice(["Lam", "Minh", "Hùng", "An", "Vinh"])

	# --- Chọn chủ đề và sinh dữ liệu ---
	chude = random.choice(["giáo dục", "khoa học", "y tế", "vận tải", "công nghệ", "sinh học", "xây dựng", "nông nghiệp"])

	if chude == "giáo dục":
		bocanh = "điểm kiểm tra (thang 10) của một nhóm học sinh"
		donvi = "điểm"
		data = [random.randint(4, 10) for _ in range(random.randint(7, 10))]
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng (ms) trong một thí nghiệm"
		donvi = "ms"
		data = [random.randint(180, 320) for _ in range(random.randint(7, 10))]
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu (mmHg) của bệnh nhân"
		donvi = "mmHg"
		data = [random.randint(95, 170) for _ in range(random.randint(7, 10))]
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển (phút) của một tuyến xe"
		donvi = "phút"
		data = [random.randint(25, 100) for _ in range(random.randint(7, 10))]
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu (Mbps) tại một điểm đo"
		donvi = "Mbps"
		data = [random.randint(20, 180) for _ in range(random.randint(7, 10))]
	elif chude == "sinh học":
		bocanh = "chiều cao cây non (cm) trong thí nghiệm sinh học"
		donvi = "cm"
		data = [random.randint(10, 55) for _ in range(random.randint(7, 10))]
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông (MPa)"
		donvi = "MPa"
		data = [random.randint(18, 45) for _ in range(random.randint(7, 10))]
	else:  # nông nghiệp
		bocanh = "năng suất lúa (tạ/ha) đo trên các thửa ruộng"
		donvi = "tạ/ha"
		data = [random.randint(35, 80) for _ in range(random.randint(7, 10))]

	# --- Sắp xếp số liệu ---
	data_sorted = sorted(data)
	n = len(data_sorted)

	# --- Tính Q3 theo chương trình THPT ---
	# Q3 là trung vị của nửa trên (không tính trung vị chung nếu n lẻ)
	if n % 2 == 0:
		upper_half = data_sorted[n // 2:]
	else:
		upper_half = data_sorted[n // 2 + 1:]

	m = len(upper_half)
	if m % 2 == 0:
		Q3 = (upper_half[m//2 - 1] + upper_half[m//2]) / 2
	else:
		Q3 = upper_half[m//2]

	dap_an = float(Q3)

	# --- Chuỗi hiển thị ---
	s_data = ", ".join(str(v) for v in data)
	s_data_sorted = ", ".join(str(v) for v in data_sorted)
	s_upper = ", ".join(str(v) for v in upper_half)
	

	if dap_an.is_integer():
		dap_an=int(dap_an)
		noi_dung = (
			f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau:\n\n"
			f"${{{s_data}}}$.\n\n"
			f"Hãy xác định tứ phân vị thứ ba $Q_3$ của dãy số liệu trên."
		)

		noi_dung_loigiai = (
			f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
			f"${{{s_data_sorted}}}$.\n\n"
			f"Dãy có $n={n}$ giá trị.\n\n"
			f"Nửa trên của dãy là:"
			f"${{{s_upper}}}$.\n\n"
			f"Tứ phân vị thứ ba $Q_3$ là trung vị của nửa trên này, do đó:\n\n"
			f"$Q_3={dap_an}$ ({donvi})."
		)
	else:
		if Q3<100:
			dap_an=f"{round_half_up(Q3,1):.1f}".replace(".0","").replace(".",",")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau:\n\n"
				f"${{{s_data}}}$.\n\n"
				f"Hãy xác định tứ phân vị thứ ba $Q_3$ của dãy số liệu trên (kết quả làm tròn đến hàng phần mười)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị.\n\n"
				f"Nửa trên của dãy là:"
				f"${{{s_upper}}}$.\n\n"
				f"Tứ phân vị thứ ba $Q_3$ là trung vị của nửa trên này, do đó:\n\n"
				f"$Q_3={dap_an}$ ({donvi})."
			)
		else:
			dap_an=f"{round_half_up(Q3,0):.0f}".replace(".0","").replace(".",",")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau:\n\n"
				f"${{{s_data}}}$.\n\n"
				f"Hãy xác định tứ phân vị thứ ba $Q_3$ của dãy số liệu trên (kết quả làm tròn đến hàng đơn vị)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị.\n\n"
				f"Nửa trên của dãy là: "
				f"${{{s_upper}}}$.\n\n"
				f"Tứ phân vị thứ ba $Q_3$ là trung vị của nửa trên này, do đó:\n\n"
				f"$Q_3={dap_an}$ ({donvi})."
			)

	debai_word = f"{noi_dung}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_16]-SA-M2. Tính trung vị của dãy số liệu theo chủ đề
def tktk_L10_C6_B3_16():
	import random
	import sympy as sp

	x = sp.symbols("x")  # giữ cấu trúc, không dùng trực tiếp

	ten = random.choice(["Lam", "Minh", "Hùng", "An", "Vinh"])

	# --- Chọn chủ đề và sinh dữ liệu ---
	chude = random.choice(["giáo dục", "khoa học", "y tế", "vận tải", "công nghệ", "sinh học", "xây dựng", "nông nghiệp"])

	if chude == "giáo dục":
		bocanh = "điểm kiểm tra (thang 10) của một nhóm học sinh"
		donvi = "điểm"
		data = [random.randint(4, 10) for _ in range(random.randint(7, 10))]
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng (ms) trong một thí nghiệm"
		donvi = "ms"
		data = [random.randint(180, 320) for _ in range(random.randint(7, 10))]
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu (mmHg) của bệnh nhân"
		donvi = "mmHg"
		data = [random.randint(95, 170) for _ in range(random.randint(7, 10))]
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển (phút) của một tuyến xe"
		donvi = "phút"
		data = [random.randint(25, 100) for _ in range(random.randint(7, 10))]
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu (Mbps) tại một điểm đo"
		donvi = "Mbps"
		data = [random.randint(20, 180) for _ in range(random.randint(7, 10))]
	elif chude == "sinh học":
		bocanh = "chiều cao cây non (cm) trong thí nghiệm sinh học"
		donvi = "cm"
		data = [random.randint(10, 55) for _ in range(random.randint(7, 10))]
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông (MPa)"
		donvi = "MPa"
		data = [random.randint(18, 45) for _ in range(random.randint(7, 10))]
	else:  # nông nghiệp
		bocanh = "năng suất lúa (tạ/ha) đo trên các thửa ruộng"
		donvi = "tạ/ha"
		data = [random.randint(35, 80) for _ in range(random.randint(7, 10))]

	# --- Sắp xếp số liệu ---
	data_sorted = sorted(data)
	n = len(data_sorted)

	# --- Tính trung vị ---
	if n % 2 == 1:
		median = data_sorted[n // 2]
	else:
		median = (data_sorted[n//2 - 1] + data_sorted[n//2]) / 2

	dap_an = median

	# --- Chuỗi hiển thị ---
	s_data = ", ".join(str(v) for v in data)
	s_data_sorted = ", ".join(str(v) for v in data_sorted)

	# --- Chuẩn hiển thị đáp án (≤ 4 kí tự) ---
	if float(dap_an).is_integer():
		dap_an = int(dap_an)

		noi_dung = (
			f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau: "
			f"${{{s_data}}}$.\n\n"
			f"Hãy xác định trung vị của dãy số liệu trên."
		)

		noi_dung_loigiai = (
			f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
			f"${{{s_data_sorted}}}$.\n\n"
			f"Dãy có $n={n}$ giá trị nên trung vị là giá trị đứng giữa dãy:\n\n"
			f"$Me={dap_an}$ ({donvi})."
		)
	else:
		if median < 99:
			dap_an = f"{round_half_up(median,1):.1f}".replace(".",",")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau: "
				f"${{{s_data}}}$.\n\n"
				f"Hãy xác định trung vị của dãy số liệu trên (kết quả làm tròn đến hàng phần mười)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ (chẵn) nên trung vị là trung bình cộng của hai giá trị đứng giữa:\n\n"
				f"$Me={dap_an}$ ({donvi})."
			)
		else:
			dap_an = f"{round_half_up(median,0):.0f}".replace(".0","")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} (đơn vị: {donvi}) như sau: "
				f"${{{s_data}}}$.\n\n"
				f"Hãy xác định trung vị của dãy số liệu trên (kết quả làm tròn đến hàng đơn vị)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu theo thứ tự không giảm:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ (chẵn) nên trung vị là trung bình cộng của hai giá trị đứng giữa:\n\n"
				f"$Me={dap_an}$ ({donvi})."
			)

	debai_word = f"{noi_dung}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_17]-SA-M2. Tính số trung bình của bảng số liệu theo chủ đề
def tktk_L10_C6_B3_17():
	ten = random.choice([
		"Lam", "Minh", "Hùng", "An", "Vinh",
		"Tuấn", "Nam", "Hải", "Quân", "Phúc"
	])

	# --- Chủ đề ---
	chude = random.choice([
		"giáo dục", "khoa học", "y tế", "vận tải",
		"công nghệ", "sinh học", "xây dựng", "nông nghiệp"
	])

	# --- Số cột ---
	m = random.randint(6, 8)

	# --- Sinh giá trị & tần số (đã fix cận randint) ---
	def gen_vals_freqs(val_min, val_max, step_choices, freq_min=2, freq_max=15):
		nonlocal m

		min_step = min(step_choices)
		hi = val_max - (m - 1) * min_step

		# Nếu hi <= val_min -> không đủ rộng, giảm m cho phù hợp để không lỗi randint
		if hi <= val_min:
			m = max(2, (val_max - val_min) // min_step + 1)
			hi = val_max - (m - 1) * min_step

		# Đảm bảo cận phải > cận trái
		hi = max(hi, val_min + 1)

		start = random.randint(val_min, hi)

		vals = [start]
		for _ in range(m - 1):
			vals.append(vals[-1] + random.choice(step_choices))

		freqs = [random.randint(freq_min, freq_max) for _ in range(m)]
		return vals, freqs

	# --- Bối cảnh theo chủ đề + tham số sinh ---
	if chude == "giáo dục":
		bocanh = "điểm kiểm tra của một nhóm học sinh"
		donvi = "điểm"
		vals, freqs = gen_vals_freqs(4, 10, [1], freq_min=2, freq_max=12)
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng trong thí nghiệm"
		donvi = "ms"
		vals, freqs = gen_vals_freqs(180, 320, [5, 10, 15], freq_min=2, freq_max=10)
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu của bệnh nhân"
		donvi = "mmHg"
		vals, freqs = gen_vals_freqs(95, 170, [5, 10], freq_min=2, freq_max=10)
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển của một tuyến xe"
		donvi = "phút"
		vals, freqs = gen_vals_freqs(25, 100, [3, 5], freq_min=2, freq_max=12)
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu"
		donvi = "Mbps"
		vals, freqs = gen_vals_freqs(20, 180, [5, 10], freq_min=2, freq_max=10)
	elif chude == "sinh học":
		bocanh = "chiều cao cây non trong thí nghiệm"
		donvi = "cm"
		vals, freqs = gen_vals_freqs(10, 55, [2, 3, 4], freq_min=2, freq_max=12)
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông"
		donvi = "MPa"
		vals, freqs = gen_vals_freqs(18, 45, [2, 3], freq_min=2, freq_max=10)
	else:
		bocanh = "năng suất lúa trên các thửa ruộng"
		donvi = "tạ/ha"
		vals, freqs = gen_vals_freqs(35, 80, [2, 3, 5], freq_min=2, freq_max=12)

	# --- Tính số trung bình (bảng tần số) ---
	N = sum(freqs)
	S = sum(v * n_i for v, n_i in zip(vals, freqs))
	mean = S / N

	# --- Chuẩn hiển thị đáp án (≤ 4 ký tự) ---
	if float(mean).is_integer():
		dap_an = int(mean)
		s_mean = str(dap_an)
		ghi_chu_lam_tron = ""
	else:
		if mean < 99:
			dap_an = f"{round_half_up(mean, 1):.1f}".replace(".", ",")
			s_mean = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng phần mười)"
		else:
			dap_an = f"{round_half_up(mean, 0):.0f}".replace(".0", "").replace(".", ",")
			s_mean = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng đơn vị)"

	# --- Tạo bảng LaTeX ---
	col_spec = "|c|" + "c|" * m
	row_vals = " & ".join(f"${v}$" for v in vals)
	row_freqs = " & ".join(f"${n_i}$" for n_i in freqs)

	if chude == "giáo dục":
	    ten_dong = "Điểm số"
	elif chude == "khoa học":
	    ten_dong = "Thời gian"
	elif chude == "y tế":
	    ten_dong = "Huyết áp"
	elif chude == "vận tải":
	    ten_dong = "Thời gian"
	elif chude == "công nghệ":
	    ten_dong = "Tốc độ"
	elif chude == "sinh học":
	    ten_dong = "Chiều cao"
	elif chude == "xây dựng":
	    ten_dong = "Cường độ"
	else:  # nông nghiệp
	    ten_dong = "Năng suất"

	code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{{col_spec}}}
        \\hline
        {ten_dong} & {row_vals} \\\\
        \\hline
        Số lượng & {row_freqs} \\\\
        \\hline
    \\end{{tabular}}
    """

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)

	# --- Nội dung ---
	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu"
		f" về {bocanh} (đơn vị: {donvi}) như sau:\n{file_name}\n"
		f"Hãy tính số trung bình của bảng số liệu trên{ghi_chu_lam_tron}."
	)

	noi_dung_loigiai = (
		f"Gọi các giá trị là $x_i$ và tần số tương ứng là $n_i$.\n\n"
		f"Tổng tần số: $N=\\sum n_i={N}$.\n\n"
		f"Tổng có trọng số: $\\sum x_in_i={S}$.\n\n"
		f"Số trung bình của bảng là:\n\n"
		f"$\\overline{{x}}=\\dfrac{{\\sum x_in_i}}{{\\sum n_i}}=\\dfrac{{{S}}}{{{N}}}={s_mean}$ ({donvi})."
	)

	# ===== GIỮ ĐÚNG CẤU TRÚC ĐOẠN CUỐI (theo yêu cầu) =====
	debai_word = f"{noi_dung}\n" 

	loigiai_word = ( 
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu"
		f" về {bocanh} (đơn vị: {donvi}) như sau:\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
		f"Hãy tính số trung bình của bảng số liệu trên{ghi_chu_lam_tron}.")

	latex_tuluan = (f"\\begin{{ex}}\n {noi_dung}\n"		
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_18]-SA-M2. Tính tứ phân vị Q1 của bảng số liệu theo chủ đề
def tktk_L10_C6_B3_18():

	ten = random.choice([
		"Lam", "Minh", "Hùng", "An", "Vinh",
		"Tuấn", "Nam", "Hải", "Quân", "Phúc"
	])

	# --- Chủ đề ---
	chude = random.choice([
		"giáo dục", "khoa học", "y tế", "vận tải",
		"công nghệ", "sinh học", "xây dựng", "nông nghiệp"
	])

	# --- Số cột ---
	m = random.randint(5, 7)

	# --- Sinh giá trị & tần số (fix lỗi cận randint) ---
	def gen_vals_freqs(val_min, val_max, step_choices, freq_min=2, freq_max=15):
		nonlocal m

		min_step = min(step_choices)
		hi = val_max - (m - 1) * min_step

		# Không đủ rộng -> giảm m để không lỗi randint
		if hi <= val_min:
			m = max(2, (val_max - val_min) // min_step + 1)
			hi = val_max - (m - 1) * min_step

		# Đảm bảo cận phải > cận trái
		hi = max(hi, val_min + 1)

		start = random.randint(val_min, hi)

		vals = [start]
		for _ in range(m - 1):
			vals.append(vals[-1] + random.choice(step_choices))

		freqs = [random.randint(freq_min, freq_max) for _ in range(m)]
		return vals, freqs

	# --- Bối cảnh theo chủ đề + tham số sinh ---
	if chude == "giáo dục":
		bocanh = "điểm kiểm tra của một nhóm học sinh"
		donvi = "điểm"
		ten_dong = "Điểm số"
		vals, freqs = gen_vals_freqs(4, 10, [1], freq_min=2, freq_max=12)
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng trong thí nghiệm"
		donvi = "ms"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(180, 320, [5, 10, 15], freq_min=2, freq_max=10)
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu của bệnh nhân"
		donvi = "mmHg"
		ten_dong = "Huyết áp"
		vals, freqs = gen_vals_freqs(95, 170, [5, 10], freq_min=2, freq_max=10)
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển của một tuyến xe"
		donvi = "phút"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(25, 100, [3, 5], freq_min=2, freq_max=12)
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu"
		donvi = "Mbps"
		ten_dong = "Tốc độ"
		vals, freqs = gen_vals_freqs(20, 180, [5, 10], freq_min=2, freq_max=10)
	elif chude == "sinh học":
		bocanh = "chiều cao cây non trong thí nghiệm"
		donvi = "cm"
		ten_dong = "Chiều cao"
		vals, freqs = gen_vals_freqs(10, 55, [2, 3, 4], freq_min=2, freq_max=12)
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông"
		donvi = "MPa"
		ten_dong = "Cường độ"
		vals, freqs = gen_vals_freqs(18, 45, [2, 3], freq_min=2, freq_max=10)
	else:
		bocanh = "năng suất lúa trên các thửa ruộng"
		donvi = "tạ/ha"
		ten_dong = "Năng suất"
		vals, freqs = gen_vals_freqs(35, 80, [2, 3, 5], freq_min=2, freq_max=12)

	# --- Tính Q1 cho bảng tần số theo CT THPT ---
	# Tổng tần số
	N = sum(freqs)

	# Vị trí của Q1: ceil(N/4)
	pos = int(sp.ceiling(N / 4))

	# Tìm Q1 là giá trị nhỏ nhất sao cho tần số tích lũy >= pos
	cum = 0
	Q1 = None
	for v, n_i in zip(vals, freqs):
		cum += n_i
		if cum >= pos:
			Q1 = float(v)
			break

	# Nếu vì lý do nào đó chưa gán (rất hiếm), lấy giá trị cuối
	if Q1 is None:
		Q1 = float(vals[-1])

	dap_an = Q1

	# --- Chuẩn hiển thị đáp án (≤ 4 ký tự) ---
	if float(dap_an).is_integer():
		dap_an = int(dap_an)
		s_Q1 = str(dap_an)
		ghi_chu_lam_tron = ""
	else:
		if dap_an < 99:
			dap_an = f"{round_half_up(dap_an, 1):.1f}".replace(".", ",")
			s_Q1 = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng phần mười)"
		else:
			dap_an = f"{round_half_up(dap_an, 0):.0f}".replace(".0","").replace(".",",")
			s_Q1 = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng đơn vị)"

	# --- Tạo bảng LaTeX (nhãn dòng 1 theo đối tượng nghiên cứu, KHÔNG dùng 'Giá trị') ---
	col_spec = "|c|" + "c|" * m
	row_vals = " & ".join(f"${v}$" for v in vals)
	row_freqs = " & ".join(f"${n_i}$" for n_i in freqs)

	code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{{col_spec}}}
        \\hline
        {ten_dong} & {row_vals} \\\\
        \\hline
        Tần số & {row_freqs} \\\\
        \\hline
    \\end{{tabular}}
    """

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	
	# --- Nội dung ---
	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu"
		f" về {bocanh} (đơn vị:{donvi}) như sau \n{file_name}\n"
		f"Hãy tính tứ phân vị thứ nhất $Q_1$ của bảng số liệu trên{ghi_chu_lam_tron}."
	)

	noi_dung_loigiai = (
		f"Tổng tần số là $N={N}$.\n\n"
		f"Vị trí của $Q_1$ là $\\left\\lceil\\dfrac{{N}}{{4}}\\right\\rceil=\\left\\lceil\\dfrac{{{N}}}{{4}}\\right\\rceil={pos}$.\n\n"
		f"Lập tần số tích lũy và tìm giá trị nhỏ nhất sao cho tần số tích lũy $\\ge {pos}$.\n\n"
		f"Suy ra $Q_1={s_Q1}$ ({donvi})."
	)

	# ===== GIỮ ĐÚNG CẤU TRÚC ĐOẠN CUỐI (theo yêu cầu) =====
	debai_word = f"{noi_dung}\n" 

	loigiai_word = ( 
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu"
		f" về {bocanh} (đơn vị: {donvi}) như sau:\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
		f"Hãy tính tứ phân vị $Q_1$ của bảng số liệu trên{ghi_chu_lam_tron}.")

	latex_tuluan = (f"\\begin{{ex}}\n {noi_dung}\n"
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_19]-SA-M2. Tính tứ phân vị Q3 của bảng số liệu theo chủ đề
def tktk_L10_C6_B3_19():

	ten = random.choice([
		"Lam", "Minh", "Hùng", "An", "Vinh",
		"Tuấn", "Nam", "Hải", "Quân", "Phúc"
	])

	# --- Chủ đề ---
	chude = random.choice([
		"giáo dục", "khoa học", "y tế", "vận tải",
		"công nghệ", "sinh học", "xây dựng", "nông nghiệp"
	])

	# --- Số cột ---
	m = random.randint(5, 7)

	# --- Sinh giá trị & tần số (fix lỗi cận randint) ---
	def gen_vals_freqs(val_min, val_max, step_choices, freq_min=2, freq_max=15):
		nonlocal m

		min_step = min(step_choices)
		hi = val_max - (m - 1) * min_step

		# Không đủ rộng -> giảm m để không lỗi randint
		if hi <= val_min:
			m = max(2, (val_max - val_min) // min_step + 1)
			hi = val_max - (m - 1) * min_step

		# Đảm bảo cận phải > cận trái
		hi = max(hi, val_min + 1)

		start = random.randint(val_min, hi)

		vals = [start]
		for _ in range(m - 1):
			vals.append(vals[-1] + random.choice(step_choices))

		freqs = [random.randint(freq_min, freq_max) for _ in range(m)]
		return vals, freqs

	# --- Bối cảnh theo chủ đề + tham số sinh + tên dòng 1 (KHÔNG dùng 'Giá trị') ---
	if chude == "giáo dục":
		bocanh = "điểm kiểm tra của một nhóm học sinh"
		donvi = "điểm"
		ten_dong = "Điểm số"
		vals, freqs = gen_vals_freqs(4, 10, [1], freq_min=2, freq_max=12)
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng trong thí nghiệm"
		donvi = "ms"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(180, 320, [5, 10, 15], freq_min=2, freq_max=10)
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu của bệnh nhân"
		donvi = "mmHg"
		ten_dong = "Huyết áp"
		vals, freqs = gen_vals_freqs(95, 170, [5, 10], freq_min=2, freq_max=10)
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển của một tuyến xe"
		donvi = "phút"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(25, 100, [3, 5], freq_min=2, freq_max=12)
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu"
		donvi = "Mbps"
		ten_dong = "Tốc độ"
		vals, freqs = gen_vals_freqs(20, 180, [5, 10], freq_min=2, freq_max=10)
	elif chude == "sinh học":
		bocanh = "chiều cao cây non trong thí nghiệm"
		donvi = "cm"
		ten_dong = "Chiều cao"
		vals, freqs = gen_vals_freqs(10, 55, [2, 3, 4], freq_min=2, freq_max=12)
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông"
		donvi = "MPa"
		ten_dong = "Cường độ"
		vals, freqs = gen_vals_freqs(18, 45, [2, 3], freq_min=2, freq_max=10)
	else:
		bocanh = "năng suất lúa trên các thửa ruộng"
		donvi = "tạ/ha"
		ten_dong = "Năng suất"
		vals, freqs = gen_vals_freqs(35, 80, [2, 3, 5], freq_min=2, freq_max=12)

	# --- Tính Q3 cho bảng tần số theo CT THPT ---
	N = sum(freqs)

	# Vị trí của Q3: ceil(3N/4)
	pos = int(sp.ceiling(3 * N / 4))

	# Tìm Q3 là giá trị nhỏ nhất sao cho tần số tích lũy >= pos
	cum = 0
	Q3 = None
	for v, n_i in zip(vals, freqs):
		cum += n_i
		if cum >= pos:
			Q3 = float(v)
			break

	if Q3 is None:
		Q3 = float(vals[-1])

	dap_an = Q3

	# --- Chuẩn hiển thị đáp án (≤ 4 ký tự) ---
	if float(dap_an).is_integer():
		dap_an = int(dap_an)
		s_Q3 = str(dap_an)
		ghi_chu_lam_tron = ""
	else:
		if dap_an < 99:
			dap_an = f"{round_half_up(dap_an, 1):.1f}".replace(".", ",")
			s_Q3 = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng phần mười)"
		else:
			dap_an = f"{round_half_up(dap_an, 0):.0f}".replace(".0","").replace(".",",")
			s_Q3 = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng đơn vị)"

	# --- Tạo bảng LaTeX ---
	col_spec = "|c|" + "c|" * m
	row_vals = " & ".join(f"${v}$" for v in vals)
	row_freqs = " & ".join(f"${n_i}$" for n_i in freqs)

	code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{|c|{'c|'*m}}}
        \\hline
        {ten_dong} & {row_vals} \\\\
        \\hline
        Tần số & {row_freqs} \\\\
        \\hline
    \\end{{tabular}}
    """

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)


	# --- Nội dung (có đơn vị trong đề) ---
	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu "
		f"về {bocanh} (đơn vị: {donvi}) như sau.\n{file_name}\n"
		f"Hãy tính tứ phân vị thứ ba $Q_3$ của bảng số liệu trên{ghi_chu_lam_tron}."
	)

	noi_dung_loigiai = (
		f"Tổng tần số là $N={N}$.\n\n"
		f"Vị trí của $Q_3$ là $\\left\\lceil\\dfrac{{3N}}{{4}}\\right\\rceil"
		f"=\\left\\lceil\\dfrac{{3\\cdot {N}}}{{4}}\\right\\rceil={pos}$.\n\n"
		f"Lập tần số tích lũy và tìm giá trị nhỏ nhất sao cho tần số tích lũy $\\ge {pos}$.\n\n"
		f"Suy ra $Q_3={s_Q3}$ ({donvi})."
	)

	# ===== GIỮ ĐÚNG CẤU TRÚC ĐOẠN CUỐI (theo yêu cầu) =====
	debai_word = f"{noi_dung}\n{file_name}\n" 

	loigiai_word = ( 
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu"
		f" về {bocanh} (đơn vị: {donvi}) như sau:\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
		f"Hãy tính tứ phân vị $Q_1$ của bảng số liệu trên{ghi_chu_lam_tron}.")

	latex_tuluan = (f"\\begin{{ex}}\n {noi_dung}\n"
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_20]-SA-M2. Tính trung vị của bảng số liệu theo chủ đề (2 dòng: giá trị - tần số, 6-8 cột)
def tktk_L10_C6_B3_20():
	import random
	import sympy as sp

	x = sp.symbols("x")  # giữ cấu trúc

	ten = random.choice([
		"Lam", "Minh", "Hùng", "An", "Vinh",
		"Tuấn", "Nam", "Hải", "Quân", "Phúc"
	])

	# --- Chủ đề ---
	chude = random.choice([
		"giáo dục", "khoa học", "y tế", "vận tải",
		"công nghệ", "sinh học", "xây dựng", "nông nghiệp"
	])

	# --- Số cột ---
	m = random.randint(5, 7)

	# --- Sinh giá trị & tần số (fix lỗi cận randint) ---
	def gen_vals_freqs(val_min, val_max, step_choices, freq_min=2, freq_max=15):
		nonlocal m

		min_step = min(step_choices)
		hi = val_max - (m - 1) * min_step

		# Không đủ rộng -> giảm m để không lỗi randint
		if hi <= val_min:
			m = max(2, (val_max - val_min) // min_step + 1)
			hi = val_max - (m - 1) * min_step

		# Đảm bảo cận phải > cận trái
		hi = max(hi, val_min + 1)

		start = random.randint(val_min, hi)

		vals = [start]
		for _ in range(m - 1):
			vals.append(vals[-1] + random.choice(step_choices))

		freqs = [random.randint(freq_min, freq_max) for _ in range(m)]
		return vals, freqs

	# --- Bối cảnh theo chủ đề + tham số sinh + tên dòng 1 (KHÔNG dùng 'Giá trị') ---
	if chude == "giáo dục":
		bocanh = "điểm kiểm tra của một nhóm học sinh"
		donvi = "điểm"
		ten_dong = "Điểm số"
		vals, freqs = gen_vals_freqs(4, 10, [1], freq_min=2, freq_max=12)
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng trong thí nghiệm"
		donvi = "ms"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(180, 320, [5, 10, 15], freq_min=2, freq_max=10)
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu của bệnh nhân"
		donvi = "mmHg"
		ten_dong = "Huyết áp"
		vals, freqs = gen_vals_freqs(95, 170, [5, 10], freq_min=2, freq_max=10)
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển của một tuyến xe"
		donvi = "phút"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(25, 100, [3, 5], freq_min=2, freq_max=12)
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu"
		donvi = "Mbps"
		ten_dong = "Tốc độ"
		vals, freqs = gen_vals_freqs(20, 180, [5, 10], freq_min=2, freq_max=10)
	elif chude == "sinh học":
		bocanh = "chiều cao cây non trong thí nghiệm"
		donvi = "cm"
		ten_dong = "Chiều cao"
		vals, freqs = gen_vals_freqs(10, 55, [2, 3, 4], freq_min=2, freq_max=12)
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông"
		donvi = "MPa"
		ten_dong = "Cường độ"
		vals, freqs = gen_vals_freqs(18, 45, [2, 3], freq_min=2, freq_max=10)
	else:
		bocanh = "năng suất lúa trên các thửa ruộng"
		donvi = "tạ/ha"
		ten_dong = "Năng suất"
		vals, freqs = gen_vals_freqs(35, 80, [2, 3, 5], freq_min=2, freq_max=12)

	# --- Trung vị của bảng tần số theo CT THPT ---
	N = sum(freqs)

	# Nếu N lẻ: vị trí (N+1)/2
	# Nếu N chẵn: trung vị là trung bình của hai vị trí N/2 và N/2+1
	pos1 = (N + 1) / 2
	pos2 = pos1
	if N % 2 == 0:
		pos1 = N / 2
		pos2 = N / 2 + 1

	def value_at_position(pos):
		# pos là số nguyên (vị trí trong dãy đã khai triển)
		cum = 0
		for v, n_i in zip(vals, freqs):
			cum += n_i
			if cum >= pos:
				return float(v)
		return float(vals[-1])

	if N % 2 == 1:
		Me = value_at_position(int(pos1))
	else:
		v1 = value_at_position(int(pos1))
		v2 = value_at_position(int(pos2))
		Me = (v1 + v2) / 2

	dap_an = Me

	# --- Chuẩn hiển thị đáp án (≤ 4 ký tự, theo chuẩn bạn đã chốt) ---
	if float(dap_an).is_integer():
		dap_an = int(dap_an)
		s_Me = str(dap_an)
		ghi_chu_lam_tron = ""
	else:
		if dap_an < 99:
			dap_an = f"{round_half_up(dap_an, 1):.1f}".replace(".", ",")
			s_Me = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng phần mười)"
		else:
			dap_an = f"{round_half_up(dap_an, 0):.0f}".replace(".0","").replace(".",",")
			s_Me = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng đơn vị)"

	# --- Tạo bảng LaTeX ---
	col_spec = "|c|" + "c|" * m
	row_vals = " & ".join(f"${v}$" for v in vals)
	row_freqs = " & ".join(f"${n_i}$" for n_i in freqs)

	code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{{col_spec}}}
        \\hline
        {ten_dong} & {row_vals} \\\\
        \\hline
        Tần số & {row_freqs} \\\\
        \\hline
    \\end{{tabular}}
    """

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)
	#file_name=""

	# --- Nội dung (có đơn vị trong đề) ---
	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu "
		f"về {bocanh} (đơn vị: {donvi}) như sau.\n{file_name}\n"
		f"Hãy tính trung vị của bảng số liệu trên{ghi_chu_lam_tron}."
	)

	noi_dung_loigiai = (
		f"Tổng tần số là $N={N}$.\n\n"
		f"Nếu $N$ lẻ thì trung vị là giá trị ở vị trí $\\dfrac{{N+1}}{{2}}$; "
		f"nếu $N$ chẵn thì trung vị là trung bình cộng của hai giá trị ở vị trí "
		f"$\\dfrac{{N}}{{2}}$ và $\\dfrac{{N}}{{2}}+1$.\n\n"
		f"Với $N={N}$, suy ra trung vị $Me={s_Me}$ ({donvi})."
	)

	# ===== GIỮ ĐÚNG CẤU TRÚC ĐOẠN CUỐI (theo yêu cầu + latex_tuluan chuẩn mới) =====
	debai_word = f"{noi_dung}\n{file_name}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu"
		f" về {bocanh} (đơn vị: {donvi}) như sau:\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
		f"Hãy tính trung vị của bảng số liệu trên{ghi_chu_lam_tron}.")

	latex_tuluan = (f"\\begin{{ex}}\n {noi_dung}\n"
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B3_21]-SA-M2. Tính khoảng tứ phân vị của bảng số liệu theo chủ đề
def tktk_L10_C6_B3_21():

	ten = random.choice([
		"Lam", "Minh", "Hùng", "An", "Vinh",
		"Tuấn", "Nam", "Hải", "Quân", "Phúc"
	])

	# --- Chủ đề ---
	chude = random.choice([
		"giáo dục", "khoa học", "y tế", "vận tải",
		"công nghệ", "sinh học", "xây dựng", "nông nghiệp"
	])

	# --- Số cột ---
	m = random.randint(5, 7)

	# --- Sinh giá trị & tần số (fix lỗi cận randint) ---
	def gen_vals_freqs(val_min, val_max, step_choices, freq_min=2, freq_max=15):
		nonlocal m

		min_step = min(step_choices)
		hi = val_max - (m - 1) * min_step

		# Không đủ rộng -> giảm m để không lỗi randint
		if hi <= val_min:
			m = max(2, (val_max - val_min) // min_step + 1)
			hi = val_max - (m - 1) * min_step

		# Đảm bảo cận phải > cận trái
		hi = max(hi, val_min + 1)

		start = random.randint(val_min, hi)

		vals = [start]
		for _ in range(m - 1):
			vals.append(vals[-1] + random.choice(step_choices))

		freqs = [random.randint(freq_min, freq_max) for _ in range(m)]
		return vals, freqs

	# --- Bối cảnh theo chủ đề + tham số sinh + tên dòng 1 (KHÔNG dùng 'Giá trị') ---
	if chude == "giáo dục":
		bocanh = "điểm kiểm tra của một nhóm học sinh"
		donvi = "điểm"
		ten_dong = "Điểm số"
		vals, freqs = gen_vals_freqs(4, 10, [1], freq_min=2, freq_max=12)
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng trong thí nghiệm"
		donvi = "ms"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(180, 320, [5, 10, 15], freq_min=2, freq_max=10)
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu của bệnh nhân"
		donvi = "mmHg"
		ten_dong = "Huyết áp"
		vals, freqs = gen_vals_freqs(95, 170, [5, 10], freq_min=2, freq_max=10)
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển của một tuyến xe"
		donvi = "phút"
		ten_dong = "Thời gian"
		vals, freqs = gen_vals_freqs(25, 100, [3, 5], freq_min=2, freq_max=12)
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu"
		donvi = "Mbps"
		ten_dong = "Tốc độ"
		vals, freqs = gen_vals_freqs(20, 180, [5, 10], freq_min=2, freq_max=10)
	elif chude == "sinh học":
		bocanh = "chiều cao cây non trong thí nghiệm"
		donvi = "cm"
		ten_dong = "Chiều cao"
		vals, freqs = gen_vals_freqs(10, 55, [2, 3, 4], freq_min=2, freq_max=12)
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông"
		donvi = "MPa"
		ten_dong = "Cường độ"
		vals, freqs = gen_vals_freqs(18, 45, [2, 3], freq_min=2, freq_max=10)
	else:
		bocanh = "năng suất lúa trên các thửa ruộng"
		donvi = "tạ/ha"
		ten_dong = "Năng suất"
		vals, freqs = gen_vals_freqs(35, 80, [2, 3, 5], freq_min=2, freq_max=12)

	# --- Tính Q1, Q3 cho bảng tần số theo CT THPT (vị trí ceil) ---
	N = sum(freqs)

	pos_Q1 = int(sp.ceiling(N / 4))
	pos_Q3 = int(sp.ceiling(3 * N / 4))

	def value_at_or_after(pos):
		cum = 0
		for v, n_i in zip(vals, freqs):
			cum += n_i
			if cum >= pos:
				return float(v)
		return float(vals[-1])

	Q1 = value_at_or_after(pos_Q1)
	Q3 = value_at_or_after(pos_Q3)

	IQR = Q3 - Q1
	dap_an = IQR

	# --- Chuẩn hiển thị đáp án (≤ 4 ký tự, theo chuẩn bạn đã chốt) ---
	if float(dap_an).is_integer():
		dap_an = int(dap_an)
		s_iqr = str(dap_an)
		ghi_chu_lam_tron = ""
	else:
		if dap_an < 99:
			dap_an = f"{round_half_up(dap_an, 1):.1f}".replace(".", ",")
			s_iqr = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng phần mười)"
		else:
			dap_an = f"{round_half_up(dap_an, 0):.0f}".replace(".0","").replace(".",",")
			s_iqr = dap_an
			ghi_chu_lam_tron = " (kết quả làm tròn đến hàng đơn vị)"

	# --- Tạo bảng LaTeX ---
	col_spec = "|c|" + "c|" * m
	row_vals = " & ".join(f"${v}$" for v in vals)
	row_freqs = " & ".join(f"${n_i}$" for n_i in freqs)

	code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{{col_spec}}}
        \\hline
        {ten_dong} & {row_vals} \\\\
        \\hline
        Tần số & {row_freqs} \\\\
        \\hline
    \\end{{tabular}}
    """

	code = my_module.moi_truong_anh_latex(code_hinh)
	file_name = my_module.pdftoimage_timename(code)


	# --- Nội dung (có đơn vị trong đề) ---
	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu "
		f"về {bocanh} (đơn vị: {donvi}) như sau:\n{file_name}\n"
		f"Hãy tính khoảng tứ phân vị của bảng số liệu trên{ghi_chu_lam_tron}."
	)

	noi_dung_loigiai = (
		f"Tổng tần số là $N={N}$.\n\n"
		f"Vị trí của $Q_1$ là $\\left\\lceil\\dfrac{{N}}{{4}}\\right\\rceil"
		f"=\\left\\lceil\\dfrac{{{N}}}{{4}}\\right\\rceil={pos_Q1}$.\n\n"
		f"Vị trí của $Q_3$ là $\\left\\lceil\\dfrac{{3N}}{{4}}\\right\\rceil"
		f"=\\left\\lceil\\dfrac{{3\\cdot {N}}}{{4}}\\right\\rceil={pos_Q3}$.\n\n"
		f"Dựa vào tần số tích lũy suy ra $Q_1={Q1}$ và $Q_3={Q3}$.\n\n"
		f"Vậy $\\Delta_Q=Q_3-Q_1={Q3}-{Q1}={s_iqr}$ ({donvi})."
	)

	# ===== GIỮ ĐÚNG CẤU TRÚC ĐOẠN CUỐI (theo yêu cầu + latex_tuluan chuẩn mới) =====
	debai_word = f"{noi_dung}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	noi_dung = (
		f"Trong lĩnh vực {chude}, bạn {ten} thu thập được bảng số liệu"
		f" về {bocanh} (đơn vị: {donvi}) như sau:\n"
		f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"
		f"Hãy tính khoảng tứ phân vị của bảng số liệu trên{ghi_chu_lam_tron}.")

	latex_tuluan = (f"\\begin{{ex}}\n {noi_dung}\n"
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"
		f"\\end{{ex}}\n")

	return debai_word, loigiai_word, latex_tuluan, dap_an
















#BÀI 4
#[D10_C6_B4_01]. Cho dãy số liệu. Tính độ lệch chuẩn
def tktk_L10_C6_B4_01():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]

	
	kq =np.std(sample_data)  # Tính độ lệch chuẩn
	kq2= np.var(sample_data) # Tính phương sai
	kq3=np.mean(sample_data)  # Tính giá trị trung bình
	kq4= np.median(sample_data) # Tính trung vị

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	kq=list_PA[0]
	kq2=list_PA[1]
	kq3=list_PA[2]
	kq4=list_PA[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tính độ lệch chuẩn của mẫu số liệu đã cho."
	
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

#[D10_C6_B4_02]. Cho dãy số liệu. Tính phương sai
def tktk_L10_C6_B4_02():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]

	
	kq =np.var(sample_data)  #Tính phương sai 
	kq2= np.std(sample_data)  # Tính độ lệch chuẩn
	kq3=np.mean(sample_data)  # Tính giá trị trung bình
	kq4= np.median(sample_data) # Tính trung vị

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	kq=list_PA[0]
	kq2=list_PA[1]
	kq3=list_PA[2]
	kq4=list_PA[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tính phương sai của mẫu số liệu đã cho."
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




#[D10_C6_B4_03]-M2. Cho dãy số liệu. Tính khoảng biến thiên
def tktk_L10_C6_B4_03():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]

	data=sample_data.tolist()
	data.sort()
	st_data_sort=", ".join(map(str, data))

	min_data, max_data=min(data),max(data)
	
	kq =max_data-min_data  #Tính phương sai 
	kq2= np.var(sample_data)   # Tính độ lệch chuẩn
	kq3=np.mean(sample_data)  # Tính giá trị trung bình
	kq4= np.median(sample_data) # Tính trung vị

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	list_PA=my_module.tra_ve_so_nguyen([kq,kq2,kq3,kq4])
	kq=list_PA[0]
	kq2=list_PA[1]
	kq3=list_PA[2]
	kq4=list_PA[3]

	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D=f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tìm khoảng biến thiên của mẫu số liệu đã cho."
	noi_dung_loigiai=f"Khoảng biến thiên của mẫu số liệu: $R={max_data}-{min_data}={max_data-min_data}$."
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

















#[D10_C6_B4_04]-TF-M2. Cho dãy số liệu. Xét Đ-S: khoảng biến thiên, độ lệch chuẩn, phương sai, khoảng tứ phân vị
def tktk_L10_C6_B4_04():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	

	mau_solieu=str(sample_data)	
	mau_solieu=mau_solieu.split()	
	mau_solieu="; ".join(mau_solieu)

	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]		

	noi_dung = f"Cho mẫu số liệu ${{{mau_solieu}}}$ . Xét tính đúng-sai của các khẳng định sau (các kết quả làm tròn đến hàng phần mười):"		
	debai_word= f"{noi_dung}\n"

	data=sample_data.tolist()	
	st=""
	for x in data:
		st+=f"{x}+"
	st=st[:-1]
	so_trungbinh=f"{round(np.mean(sample_data),1):.1f}".replace(".",",")
	so_trungbinh_false=f"{round(np.mean(sample_data)+random.choice([0.2, 0.4,0.5, random.randint(1,2)]),1):.1f}".replace(".",",")
	kq1_T=f"* Số trung bình của mẫu số liệu là ${{{so_trungbinh}}}$"
	kq1_F=f"Số trung bình của mẫu số liệu là ${{{so_trungbinh_false}}}$"
	kq1=random.choice([kq1_T, kq1_F])
	HDG=f"Số trung bình là:\n\n $\\overline{{x}}=\\dfrac{{{st}}}{{{so_luong}}}={so_trungbinh}$."
	loigiai_1=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq1==kq1_F:
		loigiai_1=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	trung_vi_round= f"{round(my_module.tu_phan_vi(sample_data)[1],1):.1f}".replace(".",",")
	trung_vi_false= f"{round(my_module.tu_phan_vi(sample_data)[1]+random.choice([0.2, 0.4,0.5, random.randint(1,2)]),1):.1f}".replace(".",",")
	
	
	data.sort()
	st_data_sort=", ".join(map(str, data))

	min_data, max_data=min(data),max(data)
	
	bienthien =max_data-min_data
	bienthien_false =max_data-min_data +random.randint(1,4)

	kq2_T=f"* Khoảng biến thiên của mẫu số liệu là ${{{bienthien}}}$"
	kq2_F=f" Khoảng biến thiên của mẫu số liệu là ${{{bienthien_false}}}$"
	kq2=random.choice([kq2_T, kq2_F])

	HDG=(f"Sắp xếp dãy số liệu ta được: ${{{st_data_sort}}}$.\n\n"
		f"Khoảng biến thiên của mẫu số liệu: $R={max_data}-{min_data}={max_data-min_data}$.")
		
	loigiai_2=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq2==kq2_F:
		loigiai_2=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	ds_mode=find_mode(data)
	st_st_mode=", ".join(map(str, ds_mode))

	mode = random.choice(ds_mode)	
	mode_false=random.choice([x for x in data if x not in ds_mode ])
	count = data.count(mode)

	phuong_sai=f"{round(np.var(sample_data),1):.1f}".replace(".",",")
	phuong_sai_false=f"{round(np.var(sample_data)+random.choice([0.2, 0.4,0.5, random.randint(1,2)]),1):.1f}".replace(".",",")
	
	st=""
	for x in data:
		st+=f"{x}^2+"
	st=st[:-1]

	kq3_T=f"* Phương sai của mẫu số liệu là ${{{phuong_sai}}}$" 
	kq3_F=f"Phương sai của mẫu số liệu là ${{{phuong_sai_false}}}$"
	kq3=random.choice([kq3_T, kq3_F])
	HDG=(f"Số trung bình là:\n\n $\\overline{{x}}={so_trungbinh}$.\n\n"
		f"Phương sai của mẫu số liệu là:\n\n $S^2={phan_so(1/len(data))}({st})-{so_trungbinh}^2={phuong_sai}$.\n\n"
		)
	loigiai_3=f"Khẳng định đã cho là khẳng định đúng.\n\n {HDG}"
	if kq3==kq3_F:
		loigiai_3=f"Khẳng định đã cho là khẳng định sai.\n\n {HDG}"

	do_lech_chuan=f"{round(np.std(sample_data),1):.1f}".replace(".",",")
	do_lech_chuan_false=f"{round(np.std(sample_data)+random.choice([0.2, 0.4,0.5, random.randint(1,2)]),1):.1f}".replace(".",",")
	kq4_T=f"* Độ lệch chuẩn của mẫu số liệu là {do_lech_chuan}"
	kq4_F=f"Độ lệch chuẩn của mẫu số liệu là {do_lech_chuan_false}" 
	kq4=random.choice([kq4_T, kq4_F])
	HDG=(f"Số trung bình là: $\\overline{{x}}={so_trungbinh}$.\n\n"
		f"Phương sai của mẫu số liệu là:\n\n $S^2={phuong_sai}$.\n\n"
		f"Độ lệch chuẩn của mẫu số liệu là:\n\n $S=\\sqrt{{{phuong_sai}}}={do_lech_chuan}$.\n\n")
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


#[D10_C6_B4_05]-M2. Cho dãy số liệu. Tính phương sai
def tktk_L10_C6_B4_05():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]
	
	kq =np.var(sample_data)  #Tính phương sai 

	noi_dung = (
	f"Cho mẫu số liệu: ${{{mau_solieu}}}$. Tính phương sai của mẫu số liệu (kết quả làm tròn đến hàng phần mười)."
	)
	dap_an=f"{round(kq,1):.1f}".replace(".",",")

	data=sample_data.tolist()	
	st=""
	for x in data:
		st+=f"{x}+"
	st=st[:-1]
	so_trungbinh=f"{round(np.mean(sample_data),1):.1f}".replace(".",",")

	noi_dung_loigiai=(
	f"Số trung bình là:\n\n $\\overline{{x}}=\\dfrac{{{st}}}{{{so_luong}}}={so_trungbinh}$.\n\n"
	)

	st=""
	for x in data:
		st+=f"{x}^2+"
	st=st[:-1]

	noi_dung_loigiai+=(
		f"Phương sai của mẫu số liệu là:\n\n $S^2={phan_so(1/len(data))}({st})-{so_trungbinh}^2={dap_an}$.\n\n")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an

#[D10_C6_B4_06]-M2. Cho dãy số liệu. Tính độ lệch chuẩn
def tktk_L10_C6_B4_06():
	# Tạo một mẫu số liệu ngẫu nhiên gồm 100 số nguyên dương
	np.random.seed(42)  # Để có thể tái tạo kết quả
	a= random.randint(1,20)
	b=a+random.randint(5,30)

	so_luong=random.randint(7,13)

	sample_data = np.random.randint(a, b, so_luong)  # Tạo ngẫu nhiên số từ a đến b
	mau_solieu=str(sample_data)
	mau_solieu=mau_solieu.split()
	mau_solieu="; ".join(mau_solieu)
	mau_solieu=mau_solieu.replace("[","")
	mau_solieu=mau_solieu.replace("]","")
	#Xử lí dấu ' thừa
	if mau_solieu[0]==";":
		mau_solieu=mau_solieu[1:]
	
	phuong_sai =np.var(sample_data)  #Tính phương sai
	phuong_sai=f"{round(phuong_sai,1):.1f}".replace(".",",")

	do_lech_chuan =np.std(sample_data)
	do_lech_chuan=f"{round(do_lech_chuan,1):.1f}".replace(".",",")
	dap_an=do_lech_chuan
	

	noi_dung = (
	f"Cho mẫu số liệu: ${{{mau_solieu}}}$. Tính độ lệch chuẩn của mẫu số liệu (kết quả làm tròn đến hàng phần mười)."
	)

	data=sample_data.tolist()	
	st=""
	for x in data:
		st+=f"{x}+"
	st=st[:-1]
	so_trungbinh=f"{round(np.mean(sample_data),1):.1f}".replace(".",",")

	noi_dung_loigiai=(
	f"Số trung bình là:\n\n $\\overline{{x}}=\\dfrac{{{st}}}{{{so_luong}}}={so_trungbinh}$.\n\n"
	)

	st=""
	for x in data:
		st+=f"{x}^2+"
	st=st[:-1]

	noi_dung_loigiai+=(
		f"Phương sai của mẫu số liệu là:\n\n $S^2={phan_so(1/len(data))}({st})-{so_trungbinh}^2={phuong_sai}$.\n\n"
		f"Độ lệch chuẩn của mẫu số liệu là:\n\n $S=\\sqrt{{{phuong_sai}}}={do_lech_chuan}$.\n\n")
		
	debai_word= f"{noi_dung}\n"

	loigiai_word=(f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n")


	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n"\
	f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
	f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
	f"\\end{{ex}}\n"
	return debai_word,loigiai_word,latex_tuluan,dap_an





#[D10_C6_B4_07]-M2. CHo biểu đồ cột thống kế số từ mới học mỗi ngày. Tính phương sai
def tktk_L10_C6_B4_07():
    A=random.choice(["Hoà", "Minh", "Hiếu", "Hùng", "Hoàng", "Hưng", "Công", "Thành", "Long", "Tân", "Trường","Khôi", "Giang", "Lam", "Hà", "Thái"])
    n=random.randint(5,8)
    b = random.randint(2*n-7, 2*n)
    c = random.randint(2*n-7, 2*n)
    d = random.randint(3, 2*n)

    # Tính số còn lại e sao cho tổng đúng 100
    a = random.randint(2*n-5, 2*n)
    e = random.randint(6, 2*n)
    
    a1,b1,c1,d1,e1= sorted(random.sample(range(5, 21), 5))
    so=random.choice([c1,d1,e1])
    code_hinh = fr"""
    \begin{{tikzpicture}}[y=0.3cm,x=0.8cm]
        %\draw[color=gray!50,line width=1.5pt]  (-1,-2.4)--(14.6,-2.4)--(14.6,6.5)--(-1,6.5)--cycle ;
        \foreach \i  in {{2,4,...,{2*n}}} 
        {{
            \draw (0,\i) node[left]{{$\i$}};
            \draw (-0.1,\i)--(0.1,\i) ;
            \draw[gray!40] (0.5,\i)--(11.5,\i);
        }}
        
        \foreach \x/\y/\z in {{2/{a1}/{a},4/{b1}/{b},6/{c1}/{c},8/{d1}/{d},10/{e1}/{e}}} 
        {{
            \draw ({{\x}},0) node[below]{{$\y$}};
            \draw ({{\x}},{{\z}}) node[above]{{$\z$}};
        }}
        \draw [->] (0,0)--(11.5,0) node[below right]{{Số từ mới}};
        \draw [->] (0,0)--(0,{2*n+1}) node[above]{{\text{{Số ngày}}}};
        \draw [pattern=north east lines]  (1.6,0)--(1.6,{a})--(2.4,{a})--(2.4,0)--cycle   
        (3.6,0)--(3.6,{b})--(4.4,{b})--(4.4,0)--cycle  
        (5.6,0)--(5.6,{c})--(6.4,{c})--(6.4,0)--cycle   
         (7.6,0)--(7.6,{d})--(8.4,{d})--(8.4,0)--cycle   
         (9.6,0)--(9.6,{e})--(10.4,{e})--(10.4,0)--cycle   ;
        %[pattern=north east lines]
    \end{{tikzpicture}}

    """
    ts=[a,b,c,d,e]
    gt=[a1,b1,c1,d1,e1]
    i=random.randint(0,4)
    gt=gt[i]
    ts=ts[i]
    tb= (a*a1+b*b1+c*c1+d*d1+e*e1)/(a+b+c+d+e)
    tbc="{:.1f}".format(tb).replace(".", ",")
    kc=(a*(a1-tb)**2+b*(b1-tb)**2+c*(c1-tb)**2+d*(d1-tb)**2+e*(e1-tb)**2)/(a+b+c+d+e)
    ps="{:.1f}".format(kc).replace(".", ",")

    noi_dung =(f"Vào đợt nghỉ hè vừa rồi, mỗi ngày bạn {A} đều học thêm một số từ vựng tiếng Anh mới. Số lượng từ vựng mới bạn {A} học mỗi ngày được biểu diễn ở biểu đồ cột như hình dưới.\n\n"
        f"Tính phương sai.")

    noi_dung_loigiai=(f"TBC là $\\overline{{x}}= \\dfrac{{{a} . {a1}+{b}.{b1}+{c}.{c1}+{d}.{d1}+{e}.{e1}}}{{{a}+{b}+{c}+{d}+{e}}} \\approx {tbc}$\n\n"
    	f" Phương sai $s^{{2}}= \\dfrac{{{a} . ({a1}-{tbc})^{{2}}+{b}.({b1}-{tbc})^{{2}}+{c}.({c1}-{tbc})^{{2}}+{d}.({d1}-{tbc})^{{2}}+{e}.({e1}-{tbc})^{{2}}}}{{{a}+{b}+{c}+{d}+{e}}} \\approx {ps}$ ")

    kq=f"${{{ps}}}$ "
    dss=[f"${{{"{:.1f}".format(kc+0.4).replace(".", ",")}}}$  ",
    f"${{{"{:.1f}".format(kc+1).replace(".", ",")}}}$   ",
    f" ${{{"{:.1f}".format(kc-1).replace(".", ",")}}}$ "  ,    
    f" ${{{"{:.1f}".format(kc+0.5).replace(".", ",")}}}$  "  ]
    kq2,kq3,kq4=random.sample(dss,3)    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    list_PA = [pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an = my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)



    debai=(f"{noi_dung}\n"
        f"{file_name}\n")

    phuongan = f"A. {list_PA[0]}\t   B. {list_PA[1]}\t    C. {list_PA[2]}\t   D. {list_PA[3]}\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề LaTeX
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
        
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an










#[D10_C6_B4_08]-M2. CHo bảng thống kế số anh chị em ruột. Tìm phương sai
def tktk_L10_C6_B4_08():
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])

    n0=random.randint(1,5)
    n1=random.randint(15,25)
    n2=random.randint(1,5)
    n3=random.randint(1,3)
    n4=random.randint(1,2)

    ts=[n0,n1,n2,n3,n4]
    gt=[0,1,2,3,4]
    i=random.randint(0,4)
    gt=gt[i]
    ts=ts[i]
    tb= (n0*0+n1*1+n2*2+n3*3+n4*4)/(n0+n1+n2+n3+n4)
    tbc="{:.1f}".format(tb).replace(".", ",")

    kc=(n0*(0-tb)**2+n1*(1-tb)**2+n2*(2-tb)**2+n3*(3-tb)**2+n4*(4-tb)**2)/(n0+n1+n2+n3+n4)
    ps="{:.1f}".format(kc).replace(".", ",")

    code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}}
        \\hline
                 Số anh chị em ruột & $0$ & 1& $2$ & $3$ & $4$   \\\\
        \\hline
       Số học sinh & ${n0}$ & $ {n1}$ & ${n2}$ & ${n3}$ & ${n4}$  \\\\
        \\hline
    \\end{{tabular}}
    """
    noi_dung=f" Bạn {A} được cô giáo giao nhiệm vụ thống kê số anh chị em ruột của các bạn trong lớp. Kết quả thu được được bạn {A} thống kê bằng bảng dưới đây. Tìm phương sai. "

    noi_dung_loigiai=(f"TBC $\\overline{{x}}= \\dfrac{{{n0}. 0+ {n1}. 1+{n2}. 2+{n3}. 3+{n4}. 4  }}{{{n0}+ {n1}+{n2}+{n3}+{n4}}} \\approx {tbc}$.\n\n"
    
    	f" Phương sai $s^{{2}}= \\dfrac{{{n0} . (0-{tbc})^{{2}}+{n1}.(1-{tbc})^{{2}}+{n2}.(2-{tbc})^{{2}}+{n3}.(3-{tbc})^{{2}}+{n4}.(4-{tbc})^{{2}}}}{{{n0}+ {n1}+{n2}+{n3}+{n4}}} \\approx {ps}$ ")

    kq=f"${{{ps}}}$ "
    dss=[f"${{{"{:.1f}".format(kc+0.4).replace(".", ",")}}}$  ",
    f"${{{"{:.1f}".format(kc+1).replace(".", ",")}}}$   ",
    f" ${{{"{:.1f}".format(kc-0.4).replace(".", ",")}}}$ "  ,    
    f" ${{{"{:.1f}".format(kc+0.5).replace(".", ",")}}}$  "  ]
    kq2,kq3,kq4=random.sample(dss,3)    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    list_PA = [pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an = my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai=(f"{noi_dung}\n"
        f"{file_name}\n")

    phuongan = f"A. {list_PA[0]}\t   B. {list_PA[1]}\t    C. {list_PA[2]}\t   D. {list_PA[3]}\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề LaTeX
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
        
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an










#[D10_C6_B4_09]-M2. CHo bảng thống kế điểm. Tìm phương sai
def tktk_L10_C6_B4_09():
    A=random.choice(["Hoa", "Mai", "Hiền", "Huệ", "Hà", "Hương", "Cúc", "Thu", "Xuân", "Lan", "Trúc"])
    X=random.choice(["Toán", "Ngoại ngữ", "Văn", "Lý", "Sử", "Địa", "Hoá", "Sinh"])
    y=random.randint(9,12)

    n0=random.randint(1,5)
    n1=random.randint(5,25)
    n2=random.randint(30,100)
    n3=random.randint(100,150)
    n4=random.randint(50,100)
    n6=random.randint(1,5)
    n5=random.randint(1,10)


    ts=n0+n1+n2+n3+n4+n5+n6
    tb= (n0*4+n1*5+n2*6+n3*7+n4*8 +n5*9+n6*10)/(n0+n1+n2+n3+n4+n5+n6)
    tbc="{:.1f}".format(tb).replace(".", ",")

    kc=(n0*(4-tb)**2+n1*(5-tb)**2+n2*(6-tb)**2+n3*(7-tb)**2+n4*(8-tb)**2 +n5*(9-tb)**2+n6*(10-tb)**2 )/(n0+n1+n2+n3+n4)
    ps="{:.1f}".format(kc).replace(".", ",")




    code_hinh = f"""
    \\centering
    \\setlength{{\\tabcolsep}}{{12pt}} % Tăng khoảng cách giữa các cột
    \\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}}
        \\hline
                 Điểm số & $4$ & 5& $6$ & $7$ & $8$  & $9$ & $10$ \\\\
        \\hline
       Số học sinh & ${n0}$ & $ {n1}$ & ${n2}$ & ${n3}$ & ${n4}$ & ${n5}$ & ${n6}$ \\\\
        \\hline
    \\end{{tabular}}
    """
    noi_dung=f"Nhà trường thống kê điểm thi môn {X} của tất cả học sinh khối ${{{y}}}$ trong kì thi khảo sát chất lượng. Kết quả thống kê bằng bảng dưới đây. Tính phương sai? "

    noi_dung_loigiai=(f"Có $N={n0}+{n1}+{n2}+{n3}+{n4}+{n5}+{n6}={{{ts}}}$ học sinh khối ${{{y}}}$ .\n\n"
    	f"TBC $\\overline{{x}}= \\dfrac{{{n0}.4+{n1}.5+{n2}.6+{n3}.7+{n4}.8+{n5}.9+{n6}.10 }}{{ N}} \\approx {tbc}$ \n\n"

    	f" Phương sai \n\n $s^{{2}}= \\dfrac{{{n0} . (4-{tbc})^{{2}}+{n1}.(5-{tbc})^{{2}}+{n2}.(6-{tbc})^{{2}}+{n3}.(7-{tbc})^{{2}}+{n4}.(8-{tbc})^{{2}}+{n5}.(9-{tbc})^{{2}}+{n6}.(10-{tbc})^{{2}}}}{{{n0}+ {n1}+{n2}+{n3}+{n4}+{n5}+{n6}}} \\approx {ps}$ ")

    kq=f"${{{ps}}}$ "
    dss=[f"${{{"{:.1f}".format(kc+0.4).replace(".", ",")}}}$  ",
    f"${{{"{:.1f}".format(kc+1).replace(".", ",")}}}$   ",
    f" ${{{"{:.1f}".format(kc-0.4).replace(".", ",")}}}$ "  ,    
    f" ${{{"{:.1f}".format(kc+0.5).replace(".", ",")}}}$  "  ]
    kq2,kq3,kq4=random.sample(dss,3)    

    pa_A= f"*{kq}"
    pa_B= f"{kq2}"
    pa_C= f"{kq3}"
    pa_D= f"{kq4}"

    list_PA = [pa_A, pa_B, pa_C, pa_D]
    random.shuffle(list_PA)
    dap_an = my_module.tra_ve_dap_an(list_PA)

    code = my_module.moi_truong_anh_latex(code_hinh)
    file_name=my_module.pdftoimage_timename(code)

    debai=(f"{noi_dung}\n"
        f"{file_name}\n")

    phuongan = f"A. {list_PA[0]}\t   B. {list_PA[1]}\t    C. {list_PA[2]}\t   D. {list_PA[3]}\n"
    
    loigiai_word = f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
    loigiai_traloingan = f"Lời giải:\n {noi_dung_loigiai} \n"

    # Tạo đề LaTeX
    for i in range(4):
        list_PA[i] = list_PA[i].replace("*", "\\True ")

    debai_latex= f"\\begin{{ex}}\n {noi_dung}\n"\
    f"\\begin{{center}}\n{code_hinh}\n\\end{{center}}\n"\
        f"\\choice\n"\
        f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"

    latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\\ \n"\
        f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
        f"\\end{{ex}}\n"
        
    return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D10_C6_B4_10]-SA-M2. Tính phương sai của dãy số liệu theo chủ đề
def tktk_L10_C6_B4_10():
	import random
	import sympy as sp

	x = sp.symbols("x")  # giữ cấu trúc, không dùng trực tiếp

	ten = random.choice(["Lam", "Minh", "Hùng", "An", "Vinh"])

	# --- Chọn chủ đề và sinh dữ liệu ---
	chude = random.choice(["giáo dục", "khoa học", "y tế", "vận tải", "công nghệ", "sinh học", "xây dựng", "nông nghiệp"])

	if chude == "giáo dục":
		bocanh = "điểm kiểm tra (thang 10) của một nhóm học sinh"
		donvi = "điểm"
		data = [random.randint(4, 10) for _ in range(random.randint(7, 10))]
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng (ms) trong một thí nghiệm"
		donvi = "ms"
		data = [random.randint(180, 320) for _ in range(random.randint(7, 10))]
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu (mmHg) của bệnh nhân"
		donvi = "mmHg"
		data = [random.randint(95, 170) for _ in range(random.randint(7, 10))]
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển (phút) của một tuyến xe"
		donvi = "phút"
		data = [random.randint(25, 100) for _ in range(random.randint(7, 10))]
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu (Mbps) tại một điểm đo"
		donvi = "Mbps"
		data = [random.randint(20, 180) for _ in range(random.randint(7, 10))]
	elif chude == "sinh học":
		bocanh = "chiều cao cây non (cm) trong thí nghiệm sinh học"
		donvi = "cm"
		data = [random.randint(10, 55) for _ in range(random.randint(7, 10))]
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông (MPa)"
		donvi = "MPa"
		data = [random.randint(18, 45) for _ in range(random.randint(7, 10))]
	else:  # nông nghiệp
		bocanh = "năng suất lúa (tạ/ha) đo trên các thửa ruộng"
		donvi = "tạ/ha"
		data = [random.randint(35, 80) for _ in range(random.randint(7, 10))]

	# --- Sắp xếp số liệu ---
	data_sorted = sorted(data)
	n = len(data_sorted)

	# --- Tính trung bình ---
	mean = sum(data_sorted) / n

	# --- Tính phương sai (theo CT THPT): S^2 = (1/n) * Σ(xi - x̄)^2 ---
	var = sum((xi - mean)**2 for xi in data_sorted) / n
	dap_an = var

	# --- Chuỗi hiển thị ---
	s_data = ", ".join(str(v) for v in data)
	s_data_sorted = ", ".join(str(v) for v in data_sorted)
	s_mean = round_half_up(mean, 2)

	# --- Chuẩn hiển thị đáp án (≤ 4 kí tự, theo code đã ghi nhớ) ---
	if float(dap_an).is_integer():
		dap_an = int(dap_an)

		noi_dung = (
			f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau: "
			f"${{{s_data}}}$.\n\n"
			f"Hãy tính phương sai của dãy số liệu trên."
		)

		noi_dung_loigiai = (
			f"Sắp xếp dãy số liệu:\n\n"
			f"${{{s_data_sorted}}}$.\n\n"
			f"Dãy có $n={n}$ giá trị, số trung bình là $\\overline{{x}}={s_mean}$.\n\n"
			f"Phương sai là:\n\n"
			f"$S^2=\\dfrac{{1}}{{{n}}}\\sum (x_i-\\overline{{x}})^2={dap_an}$."
		)
	else:
		if var < 99:
			dap_an = f"{round_half_up(var,1):.1f}".replace(".",",")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau: "
				f"${{{s_data}}}$.\n\n"
				f"Hãy tính phương sai của dãy số liệu trên (kết quả làm tròn đến hàng phần mười)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị, số trung bình là $\\overline{{x}}={s_mean}$.\n\n"
				f"Phương sai là:\n\n"
				f"$S^2=\\dfrac{{1}}{{{n}}}\\sum (x_i-\\overline{{x}})^2={dap_an}$."
			)
		else:
			dap_an = f"{round_half_up(var,0):.0f}".replace(".0","")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau: "
				f"${{{s_data}}}$.\n\n"
				f"Hãy tính phương sai của dãy số liệu trên (kết quả làm tròn đến hàng đơn vị)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị, số trung bình là $\\overline{{x}}={s_mean}$.\n\n"
				f"Phương sai là:\n\n"
				f"$S^2=\\dfrac{{1}}{{{n}}}\\sum (x_i-\\overline{{x}})^2={dap_an}$."
			)

	debai_word = f"{noi_dung}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	return debai_word, loigiai_word, latex_tuluan, dap_an

#[D10_C6_B4_11]-SA-M2. Tính độ lệch chuẩn của dãy số liệu theo chủ đề
def tktk_L10_C6_B4_11():

	x = sp.symbols("x")  # giữ cấu trúc, không dùng trực tiếp

	ten = random.choice([
		"Lam", "Minh", "Hùng", "An", "Vinh",
		"Tuấn", "Nam", "Hải", "Quân", "Phúc"
	])

	# --- Chọn chủ đề và sinh dữ liệu ---
	chude = random.choice(["giáo dục", "khoa học", "y tế", "vận tải", "công nghệ", "sinh học", "xây dựng", "nông nghiệp"])

	if chude == "giáo dục":
		bocanh = "điểm kiểm tra (thang 10) của một nhóm học sinh"
		donvi = "điểm"
		data = [random.randint(4, 10) for _ in range(random.randint(7, 10))]
	elif chude == "khoa học":
		bocanh = "thời gian phản ứng (ms) trong một thí nghiệm"
		donvi = "ms"
		data = [random.randint(180, 320) for _ in range(random.randint(7, 10))]
	elif chude == "y tế":
		bocanh = "huyết áp tâm thu (mmHg) của bệnh nhân"
		donvi = "mmHg"
		data = [random.randint(95, 170) for _ in range(random.randint(7, 10))]
	elif chude == "vận tải":
		bocanh = "thời gian di chuyển (phút) của một tuyến xe"
		donvi = "phút"
		data = [random.randint(25, 100) for _ in range(random.randint(7, 10))]
	elif chude == "công nghệ":
		bocanh = "tốc độ tải dữ liệu (Mbps) tại một điểm đo"
		donvi = "Mbps"
		data = [random.randint(20, 180) for _ in range(random.randint(7, 10))]
	elif chude == "sinh học":
		bocanh = "chiều cao cây non (cm) trong thí nghiệm sinh học"
		donvi = "cm"
		data = [random.randint(10, 55) for _ in range(random.randint(7, 10))]
	elif chude == "xây dựng":
		bocanh = "cường độ chịu nén của mẫu bê tông (MPa)"
		donvi = "MPa"
		data = [random.randint(18, 45) for _ in range(random.randint(7, 10))]
	else:  # nông nghiệp
		bocanh = "năng suất lúa (tạ/ha) đo trên các thửa ruộng"
		donvi = "tạ/ha"
		data = [random.randint(35, 80) for _ in range(random.randint(7, 10))]

	# --- Sắp xếp số liệu ---
	data_sorted = sorted(data)
	n = len(data_sorted)

	# --- Tính trung bình ---
	mean = sum(data_sorted) / n

	# --- Tính phương sai (theo CT THPT): S^2 = (1/n) * Σ(xi - x̄)^2 ---
	var = sum((xi - mean)**2 for xi in data_sorted) / n

	# --- Độ lệch chuẩn ---
	std = float(sp.sqrt(var))
	dap_an = std

	# --- Chuỗi hiển thị ---
	s_data = ", ".join(str(v) for v in data)
	s_data_sorted = ", ".join(str(v) for v in data_sorted)

	# --- Chuẩn hiển thị đáp án (≤ 4 kí tự, theo code đã ghi nhớ) ---
	# Nếu là số nguyên
	if float(dap_an).is_integer():
		dap_an = int(round(dap_an))

		noi_dung = (
			f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau: "
			f"${{{s_data}}}$.\n\n"
			f"Hãy tính độ lệch chuẩn của dãy số liệu trên."
		)

		noi_dung_loigiai = (
			f"Sắp xếp dãy số liệu:\n\n"
			f"${{{s_data_sorted}}}$.\n\n"
			f"Dãy có $n={n}$ giá trị.\n\n"
			f"Gọi $\\overline{{x}}$ là số trung bình, phương sai là $S^2=\\dfrac{{1}}{{n}}\\sum (x_i-\\overline{{x}})^2$.\n\n"
			f"Độ lệch chuẩn là $S=\\sqrt{{S^2}}={dap_an}$."
		)
	else:
		if std < 99:
			dap_an = f"{round_half_up(std,1):.1f}".replace(".",",")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau: "
				f"${{{s_data}}}$.\n\n"
				f"Hãy tính độ lệch chuẩn của dãy số liệu trên (kết quả làm tròn đến hàng phần mười)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị.\n\n"
				f"Tính phương sai: $S^2=\\dfrac{{1}}{{n}}\\sum (x_i-\\overline{{x}})^2$. "
				f"Suy ra độ lệch chuẩn: $S=\\sqrt{{S^2}}={dap_an}$."
			)
		else:
			dap_an = f"{round_half_up(std,0):.0f}".replace(".0","").replace(".",",")

			noi_dung = (
				f"Trong lĩnh vực {chude}, bạn {ten} thu thập được dãy số liệu về {bocanh} như sau:\n\n"
				f"${{{s_data}}}$.\n\n"
				f"Hãy tính độ lệch chuẩn của dãy số liệu trên (kết quả làm tròn đến hàng đơn vị)."
			)

			noi_dung_loigiai = (
				f"Sắp xếp dãy số liệu:\n\n"
				f"${{{s_data_sorted}}}$.\n\n"
				f"Dãy có $n={n}$ giá trị.\n\n"
				f"Tính phương sai: $S^2=\\dfrac{{1}}{{n}}\\sum (x_i-\\overline{{x}})^2$.\n\n"
				f"Suy ra độ lệch chuẩn: $S=\\sqrt{{S^2}}={dap_an}$."
			)

	debai_word = f"{noi_dung}\n"

	loigiai_word = (
		f"Lời giải:\n {noi_dung_loigiai} \n"
		f"Đáp án: {dap_an}\n"
	)

	latex_tuluan = f"\\begin{{ex}}\n {noi_dung}\n"\
		f"\n\n\\shortans[4]{{{dap_an}}}\n\n"\
		f"\\loigiai{{ \n {noi_dung_loigiai} \n }}"\
		f"\\end{{ex}}\n"

	return debai_word, loigiai_word, latex_tuluan, dap_an

