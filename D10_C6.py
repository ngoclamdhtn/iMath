import math
import sympy as sp
import numpy as np
from sympy import *
import random
from fractions import Fraction
import my_module

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

def calculate_mode(data):
    unique_values, counts = np.unique(data, return_counts=True)
    max_count_index = np.argmax(counts)
    mode_value = unique_values[max_count_index]
    mode_count = counts[max_count_index]
    return mode_value, mode_count

#[D10_C6_B3_03]. Cho dãy số liệu. Tính mốt.
def tktk_L10_C6_B3_03():
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

	mode = calculate_mode(sample_data)[0]
	
	kq =mode #Tính phương sai 
	kq2= calculate_mode(sample_data)[1]  # Tính độ lệch chuẩn
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
	noi_dung = f"Cho mẫu số liệu như sau: {mau_solieu}. Tìm mốt mẫu số liệu đã cho."

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




