import math
import sympy as sp
import numpy as np
from sympy import *
import random
from fractions import Fraction
import my_module
from collections import Counter
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