import math
import sympy as sp
from sympy import *
import random
from fractions import Fraction
import my_module
def xu_li_dau_cham(a):
	str_a=str(a)
	str_a=str_a.replace(".",",")
	return str_a
def thay_the_tap_hop(st):
	kq=st.replace("'","").replace("{","\\{").replace("[","\\{").replace("]","\\}")
	return kq
#Tính số chỉnh hợp chập k của n
def chinh_hop(k,n):
	t=factorial(n) / factorial(n - k)
	return t
################ Bài 1: BIẾN CỐ GIAO VÀ QUY TẮC NHÂN ########################
#[D11_C9_B1_01]-M2. Cho một hộp chứa n quả cầu. Tìm biến cố giao vừa là số chẵn (lẻ), vừa chia hết cho k.
def zz8zz_L11_C9_B1_01():   
    #Tạo bậc ngẫu nhiên
	n =random.randint(15,40)
	k=random.choice([3,4,5,6,7])
	chan_le=random.choice(["chẵn", "lẻ"])
	#if k in [2,4,6]: chan_le="chẵn"
	t=0
	list_kq=[]
	if chan_le=="chẵn":
		for i in range(1,n+1):    	
			if i%k==0 and i%2==0:
				t=t+1
				list_kq.append(i)
	else:
		for i in range(1,n+1):
			if i%k==0 and i%2!=0:
				t=t+1
				list_kq.append(i)
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")

    
	kq=f"{t}"
	kq2=f"{t+1}"
	kq3=f"{t+random.randint(2,4)}"
	kq4=f"{t+random.randint(5,7)}"

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một hộp chứa {n} quả cầu cùng kích thước được đánh số từ 1 đến {n}. Chọn ngẫu nhiên 1 quả cầu từ hộp." \
	f" Gọi ${{A}}$ là biến cố “Số ghi trên quả cầu được chọn là một số {chan_le}”, $B$ là biến cố “ Số ghi trên quả cầu được chọn là số chia hết cho {k}”."\
	f" Xác định số phần tử của biến cố ${{AB}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"${{AB}}$ là biến cố số ghi trên quả cầu được chọn vừa là một số {chan_le} vừa là số chia hết cho {k}.\n"\
					f"${{AB}}=\\{{{list_kq}\\}}$.\n Vậy số phần tử của biến cố ${{AB}}$ là ${{{kq}}}$."    
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B1_02]-M2. Cho một hộp chứa n tấm thẻ. Tìm biến cố giao: thẻ vừa thuộc phạm vi [a;b], vừa chia hết cho k.
def zz8zz_L11_C9_B1_02():   
    #Tạo bậc ngẫu nhiên
	n =random.randint(15,40)
	k=random.choice([3,4,5,6])	
	a=random.randint(1,6)
	b=n-random.randint(1,4)

	t=0
	list_kq=[]
	for i in range(a,b+1):    	
		if i%k==0:
			t=t+1
			list_kq.append(i)

	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	
    
	kq=f"{t}"
	kq2=f"{t+1}"
	kq3=f"{t+random.randint(2,4)}"
	kq4=f"{t+random.randint(5,7)}"

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Một hộp chứa {n} quả cầu cùng kích thước được đánh số từ 1 đến {n}. Chọn ngẫu nhiên 1 quả cầu từ hộp." \
	f" Gọi ${{A}}$ là biến cố “Số ghi trên quả cầu được chọn là một số thuộc đoạn ${{[{a};{b}]}}$”, $B$ là biến cố “ Số ghi trên quả cầu được chọn là số chia hết cho {k}”."\
	f" Xác định số phần tử của biến cố ${{AB}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"${{AB}}$ là biến cố số ghi trên quả cầu được chọn vừa là một số thuộc đoạn ${{[{a};{b}]}}$, vừa là số chia hết cho {k}.\n"\
					f"${{AB}}=\\{{{list_kq}\\}}$.\n Vậy số phần tử của biến cố ${{AB}}$ là ${{{kq}}}$."    
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B1_03]-M2. Cho một hộp chứa n quả cầu. Tìm biến cố giao vừa chia hết cho m, vừa chia hết cho k.
def zz8zz_L11_C9_B1_03():   
    #Tạo bậc ngẫu nhiên
	n =random.randint(25,50)
	m=random.choice([2,4,6])
	k=random.choice([3,5,7])

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,n+1):    	
		if i%m==0 and i%k==0:
			t=t+1
			list_kq.append(i)
		if i%m==0:
			t_m=t_m+1
		if i%k==0:
			t_k=t_k+1
	if t_m<t_k:
		t_kq2=t_k-t_m
	else:
		t_kq2=t_m-t_k

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	
    
	kq=t
	kq2=t_kq2
	kq3=t_m
	kq4=t_k

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

	noi_dung=f"Một hộp chứa {n} quả cầu cùng kích thước được đánh số từ 1 đến {n}. Chọn ngẫu nhiên 1 quả cầu từ hộp." \
	f" Gọi ${{A}}$ là biến cố “Số ghi trên quả cầu được chọn là số chia hết cho {m}”, $B$ là biến cố “ Số ghi trên quả cầu được chọn là số chia hết cho {k}”."\
	f" Xác định số phần tử của biến cố ${{AB}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"${{AB}}$ là biến cố số ghi trên quả cầu được chọn vừa là một số chia hết cho {m}, vừa là số chia hết cho {k}.\n"\
					f"${{AB}}=\\{{{list_kq}\\}}$.\n Vậy số phần tử của biến cố ${{AB}}$ là ${{{kq}}}$."    
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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


#[D11_C9_B1_04]-M2. Gieo 2 con xúc xắc. Tìm biến cố giao: k < i + j và i+j <m.
def zz8zz_L11_C9_B1_04():   
    #Tạo bậc ngẫu nhiên
	
	k=random.randint(6,8)
	m=random.randint(9,11)

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):	 
			if k<i+j<m:
				t=t+1
				list_kq.append(f"({i};{j})")
			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")
	
    
	kq=t
	kq2=t_kq2
	kq3=abs(t-2)
	kq4=t+3

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

	noi_dung=f"Gieo đồng thời một con xúc xắc cân đối và đồng chất hai lần." \
	f" Gọi ${{A}}$ là biến cố “Tổng số chấm của hai lần gieo lớn hơn {k}”, $B$ là biến cố “Tổng số chấm của hai lần gieo nhỏ hơn {m}”."\
	f" Xác định số phần tử của biến cố ${{AB}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"${{AB}}$ là biến cố tổng số chấm của hai lần gieo lớn hơn {k} và nhỏ hơn {m}.\n"\
					f"${{AB}}=\\{{{list_kq}\\}}$. \n Vậy số phần tử của biến cố ${{AB}}$ là ${{{kq}}}$."    
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B1_05]-M2. Gieo 2 con xúc xắc. Tìm biến cố giao: mặt k chấm xuất hiện và tổng số chấm =,>,< m.
def zz8zz_L11_C9_B1_05():   
    #Tạo bậc ngẫu nhiên
	
	k=random.randint(3,6)
	m=random.randint(7,10)
	chon=random.choice(["bằng", "nhỏ hơn", "lớn hơn"])

	t,t_m,t_k=0,0,0
	list_kq=[]


	for i in range(1,7):
		for j in range(1,7):
			if chon=="bằng":	 
				if (i==k or j==k) and i+j==m:
					t=t+1
					list_kq.append(f"({i};{j})")
			elif chon=="nhỏ hơn":
				if (i==k or j==k) and i+j<m:
					t=t+1
					list_kq.append(f"({i};{j})")
			else:
				if (i==k or j==k) and i+j>m:
					t=t+1
					list_kq.append(f"({i};{j})")
			if i==k or j==k:
				t_k=t_k+1
			if i+j==m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")
	
    
	kq=t
	kq2=t_kq2
	kq3=abs(t-2)
	kq4=t+3

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

	noi_dung=f"Gieo một con xúc xắc cân đối và đồng chất hai lần." \
	f" Gọi ${{A}}$ là biến cố “Có ít nhất một lần gieo xuất hiện mặt {k} chấm”, $B$ là biến cố “Tổng số chấm của hai lần gieo {chon} {m}”."\
	f" Xác định số phần tử của biến cố ${{AB}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"${{AB}}$ là biến cố có ít nhất một lần gieo xuất hiện mặt {k} và tổng số chấm của hai lần gieo {chon} {m}.\n"\
					f"${{AB}}=\\{{{list_kq}\\}}$. \n Vậy số phần tử của biến cố ${{AB}}$ là ${{{kq}}}$."    
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B1_06]-M2. Gieo 2 con xúc xắc. Tìm biến cố giao: i + j = k và i.j <(>) m.
def zz8zz_L11_C9_B1_06():      
	
	k=random.randint(6,8)
	m=random.randint(8,11)
	chon=random.choice(["nhỏ hơn", "lớn hơn"])

	t,t_m,t_k=0,0,0
	list_kq=[]

	for i in range(1,7):
		for j in range(1,7):
			if chon=="nhỏ hơn":	 
				if i+j==k and i*j<m:
					t=t+1
					list_kq.append(f"({i};{j})")
			else:
				if i+j==k and i*j>m:
					t=t+1
					list_kq.append(f"({i};{j})")

			if i+j>k:
				t_k=t_k+1
			if i+j<m:
				t_m=t_m+1
	t_kq2=abs(t_k-t_m)

	
	list_kq=str(list_kq)
	list_kq=list_kq.replace("[","")
	list_kq=list_kq.replace("]","")
	list_kq=list_kq.replace("'","")	
    
	kq=t
	kq2=t_kq2
	kq3=t_k
	kq4=t_m

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

	noi_dung=f"Gieo một con xúc xắc cân đối và đồng chất hai lần." \
	f" Gọi ${{A}}$ là biến cố “Tổng số chấm của hai lần gieo bằng {k}”, $B$ là biến cố “Tích số chấm của hai lần gieo {chon} {m}”."\
	f" Xác định số phần tử của biến cố ${{AB}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"${{AB}}$ là biến cố tổng số chấm của hai lần gieo bằng {k} và tích số chấm của hai lần gieo {chon} {m}.\n"\
					f"${{AB}}=\\{{{list_kq}\\}}$. \n Vậy số phần tử của biến cố ${{AB}}$ là ${{{kq}}}$."    
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#9.1.2 Quy tắc nhân xác suất

#[D11_C9_B1_07]-M1. Cho xác suất của 2 biến cố độc lập. Tìm xác suất của biến cố giao
def zz8zz_L11_C9_B1_07():      
	
	a=random.randint(1,95)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)

	kq=round(p_a*p_b,3)
	kq2=round((1-p_a)*p_b,3)
	kq3=round((1-p_b)*p_a,3)
	kq4=round((1-p_a)*(1-p_b),3)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Cho ${{A}}$ và ${{B}}$ là hai biến cố độc lập." \
	f" Biết $P(A)={p_a_text}$ và $P(B)={p_b_text}$."\
	f" Tính xác suất của biến cố ${{AB}}$ (kết quả làm tròn đến hàng phần nghìn)."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"$P{{AB}}=P(A).P(B)={p_a_text}.{p_b_text}={kq}$ .\n"				
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B1_08]-M2. Cho xác suất của 2 biến cố độc lập. Tìm xác suất của biến cố giao chứa biến cố đối
def zz8zz_L11_C9_B1_08():      
	
	a=random.randint(1,95)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_ngang=xu_li_dau_cham(p_a_ngang)
	p_b_ngang=xu_li_dau_cham(p_b_ngang)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)
	chon=random.choice(["\\overline{{A}}B", "A\\overline{{B}}", "\\overline{{A}}\\,\\overline{{B}}"])
	if chon=="\\overline{{A}}B":
		kq=round((1-p_a)*p_b,2)
		kq2=round(p_a*p_b,2)
		kq3=round((1-p_b)*p_a,2)
		kq4=round((1-p_a)*(1-p_b),2)
		noi_dung_loigiai=f"$P\\left(\\overline{{A}}B\\right)=P(\\overline{{A}}).P(B)=(1-{p_a_text}).{p_b_text}={p_a_ngang}.{p_b_text}={kq}$ .\n"

	elif chon=="A\\overline{{B}}":
		kq=round((1-p_b)*p_a,2)
		kq2=round(p_a*p_b,2)
		kq3=round((1-p_a)*p_b,2)
		kq4=round((1-p_a)*(1-p_b),2)
		noi_dung_loigiai=f"$P\\left(A\\overline{{B}}\\right)=P(A).P(\\overline{{B}})={p_a_text}.(1-{p_b_text})={p_a_text}.{p_b_ngang}={kq}$ .\n"
	else:
		kq=round((1-p_a)*(1-p_b),2)
		kq2=round(p_a*p_b,2)
		kq3=round((1-p_a)*p_b,2)
		kq4=round((1-p_b)*p_a,2)
		noi_dung_loigiai=f"$P\\left(\\overline{{A}}\\,\\overline{{B}}\\right)=P(\\overline{{A}}).P(\\overline{{B}})=(1-{p_a_text}).(1-{p_b_text})={p_a_ngang}.{p_b_ngang}={kq}$ .\n"

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Cho ${{A}}$ và ${{B}}$ là hai biến cố độc lập." \
	f" Biết $P(A)={p_a_text}$ và $P(B)={p_b_text}$."\
	f" Tính xác suất của biến cố $P\\left({chon}\\right)$ (kết quả làm tròn đến hàng phần trăm)."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
					
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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


#[D11_C9_B1_09]-M2. Hộp chứa các viên bi có 2 màu. Phát biểu biến cố giao.
def zz8zz_L11_C9_B1_09():   
    #Tạo bậc ngẫu nhiên
	m =random.randint(8,20)
	so_lan =random.randint(5,9)
	j=random.randint(1,so_lan-1)
	k=random.randint(1,so_lan)
	if j==k: j=j+1
	if j>k:
		t=j
		j=k
		k=t

	mau=random.choice(["màu đỏ", "màu đen", "màu xanh dương", "màu hồng", "màu vàng", "màu trắng", "màu tím", "màu nâu"])

	noi_dung=f'Một hộp chứa {m} viên bi có màu sắc khác nhau. Lấy ngẫu nhiên một viên bi, quan sát màu sắc rồi trả lại vào hộp. ' \
	f'Tiếp tục lấy lần 2 rồi trả lại, cứ tiếp tục như thế đến {so_lan} lần. Gọi ${{A_i}}$ là biến cố "Lần thứ ${{i}}$ lấy được viên bi {mau}". '\
	f'Mệnh đề nào dưới đây mô tả biến cố $A_{j} \\cap A_{k}$?\n\n'
    
	kq=f"Cả hai lần lấy thứ ${{{j}}}$ và thứ ${{{k}}}$ đều lấy được bi {mau}"
	kq2=f"Cả hai lần lấy thứ ${{{j}}}$ và thứ ${{{k}}}$ đều không lấy được bi {mau}"
	kq3=f"Ít nhất một trong các lần lấy thứ ${{{j}}}$ và thứ ${{{k}}}$ đều lấy được bi {mau}"
	kq4=f"Lần rút đầu tiên lấy được bi {mau} là lần lấy thứ {int((j+k)/2)}"

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
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Biến cố $A_{j} \\cap A_{k}$ là {kq}."
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B1_10]-M2. Cho xác suất bị bệnh của 2 bệnh nhân. Tìm xác suất cả hai không bị bệnh.
def zz8zz_L11_C9_B1_10():      
	
	a=random.randint(1,95)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_ngang=xu_li_dau_cham(p_a_ngang)
	p_b_ngang=xu_li_dau_cham(p_b_ngang)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)

	noi_dung=f"Hai bệnh nhân ${{X}}$ và ${{Y}}$ bị nhiễm một loại vi rút." \
	f" Biết rằng xác suất bị biến chứng nặng của bệnh nhân ${{X}}$ là ${{{p_a_text}}}$ và của bệnh nhân ${{Y}}$ là ${{{p_b_text}}}$."\
	f' Khả năng bị biến chứng nặng của hai bệnh nhân là độc lập. Tính xác suất của biến cố "Cả hai bệnh nhân đều không bị biến chứng nặng" (kết quả làm tròn đến hàng phần trăm).'

	kq=round((1-p_a)*(1-p_b),2)
	kq2=round(p_a*p_b,2)
	kq3=round((1-p_a)*p_b,2)
	kq4=round((1-p_b)*p_a,2)
	xacsuat=f"{kq:.2f}"
	noi_dung_loigiai=f'Gọi ${{A}}$ là biến cố "Bệnh nhân ${{X}}$ bị biến chứng nặng". Ta có: $P(A)={p_a_text}$ và $P\\left(\\overline{{A}}\\right)={p_a_ngang}$.\n\n'\
	f'Gọi ${{B}}$ là biến cố "Bệnh nhân ${{Y}}$ bị biến chứng nặng". Ta có: $P(B)={p_b_text}$ và $P\\left(\\overline{{B}}\\right)={p_b_ngang}$.\n\n'\
	f"Do $\\overline{{A}}$ và $\\overline{{B}}$ là độc lập nên xác suất để cả hai bệnh nhân đều không bị biến chứng nặng là:\n\n"\
	f"$P\\left(\\overline{{A}}\\,\\overline{{B}}\\right)=P(\\overline{{A}}).P(\\overline{{B}})={p_a_ngang}.{p_b_ngang}={xu_li_dau_cham(xacsuat)}$ .\n"

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq:.2f}"
	kq2=f"{kq2:.2f}"
	kq3=f"{kq3:.2f}"
	kq4=f"{kq4:.2f}"

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C9_B1_11]-M2. Cho xác suất bị bệnh của 2 bệnh nhân. Tìm xác suất chỉ một trong hai không bị biến chứng nặng.
def zz8zz_L11_C9_B1_11():      
	
	a=random.randint(1,95)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_ngang=xu_li_dau_cham(p_a_ngang)
	p_b_ngang=xu_li_dau_cham(p_b_ngang)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)

	noi_dung=f"Hai bệnh nhân ${{X}}$ và ${{Y}}$ bị nhiễm một loại vi rút." \
	f" Biết rằng xác suất bị biến chứng nặng của bệnh nhân ${{X}}$ là ${{{p_a_text}}}$ và của bệnh nhân ${{Y}}$ là ${{{p_b_text}}}$."\
	f' Khả năng bị biến chứng nặng của hai bệnh nhân là độc lập. Tính xác suất của biến cố "Chỉ một trong hai bệnh nhân không bị biến chứng nặng" (kết quả làm tròn đến hàng phần trăm).'
	
	
	kq=round((1-p_a)*p_b+(1-p_b)*p_a,2)
	kq2=round(p_a*p_b,2)
	kq3=round((1-p_a)*p_b,2)
	kq4=round((1-p_b)*p_a,2)
	xacsuat=f"{kq:.2f}"
	noi_dung_loigiai=f'Gọi ${{A}}$ là biến cố "Bệnh nhân ${{X}}$ bị biến chứng nặng". Ta có: $P(A)={p_a_text}$ và $P\\left(\\overline{{A}}\\right)={p_a_ngang}$.\n\n'\
	f'Gọi ${{B}}$ là biến cố "Bệnh nhân ${{Y}}$ bị biến chứng nặng". Ta có: $P(B)={p_b_text}$ và $P\\left(\\overline{{B}}\\right)={p_b_ngang}$.\n\n'\
	f"Do $\\overline{{A}}$ và $\\overline{{B}}$ là độc lập nên xác suất để chỉ một trong hai bệnh nhân không bị biến chứng nặng là:\n\n"\
	f"$P\\left(\\overline{{A}}B \\cup A\\overline{{B}} \\right)=P(\\overline{{A}}).P(B)+P(A).P(\\overline{{B}})=$\n${p_a_ngang}.{p_b_text}+{p_a_text}.{p_b_ngang}={xu_li_dau_cham(xacsuat)}$.\n"

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq:.2f}"
	kq2=f"{kq2:.2f}"
	kq3=f"{kq3:.2f}"
	kq4=f"{kq4:.2f}"

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C9_B1_12]-M2. Cho xác suất bắn trúng bia của 1 xạ thủ. Tính xác suất cả hai không bắn trúng.
def zz8zz_L11_C9_B1_12():      
	
	a=random.randint(1,95)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_ngang=xu_li_dau_cham(p_a_ngang)
	p_b_ngang=xu_li_dau_cham(p_b_ngang)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)

	noi_dung=f"Một xạ thủ bắn lần lượt 2 viên đạn vào một bia." \
	f" Xác suất trúng đích của viên thứ nhất là ${{{p_a_text}}}$ và của viên thứ hai là ${{{p_b_text}}}$."\
	f' Biết rằng kết quả của các lần bắn là độc lập với nhau. Tính xác suất của biến cố "Cả hai lần bắn đều không trúng đích" (kết quả làm tròn đến hàng phần trăm).'

	kq=round((1-p_a)*(1-p_b),2)
	kq2=round(p_a*p_b,2)
	kq3=round((1-p_a)*p_b,2)
	kq4=round((1-p_b)*p_a,2)
	xacsuat=f"{kq:.2f}"
	noi_dung_loigiai=f'Gọi ${{A}}$ là biến cố viên thứ nhất bắn trúng. Ta có: $P(A)={p_a_text}$ và $P\\left(\\overline{{A}}\\right)={p_a_ngang}$.\n\n'\
	f'Gọi ${{B}}$ là biến cố viên thứ hai bắn trúng. Ta có: $P(B)={p_b_text}$ và $P\\left(\\overline{{B}}\\right)={p_b_ngang}$.\n\n'\
	f"Do $\\overline{{A}}$ và $\\overline{{B}}$ là độc lập nên xác suất để cả hai lần bắn đều không trúng đích là:\n\n"\
	f"$P\\left(\\overline{{A}}\\,\\overline{{B}}\\right)=P(\\overline{{A}}).P(\\overline{{B}})={p_a_ngang}.{p_b_ngang}={xu_li_dau_cham(xacsuat)}$ .\n"

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq:.2f}"
	kq2=f"{kq2:.2f}"
	kq3=f"{kq3:.2f}"
	kq4=f"{kq4:.2f}"

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an


#[D11_C9_B1_13]-M2. Cho xác suất bắn trúng bia của 1 xạ thủ. Tính xác suất chỉ một lần bắn trúng.
def zz8zz_L11_C9_B1_13():      
	
	a=random.randint(1,96)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_ngang=xu_li_dau_cham(p_a_ngang)
	p_b_ngang=xu_li_dau_cham(p_b_ngang)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)

	noi_dung=f"Một xạ thủ bắn lần lượt 2 viên đạn vào một bia." \
	f" Xác suất trúng đích của viên thứ nhất là ${{{p_a_text}}}$ và của viên thứ hai là ${{{p_b_text}}}$."\
	f' Biết rằng kết quả của các lần bắn là độc lập với nhau. Tính xác suất của biến cố "chỉ một lần bắn trúng đích" (kết quả làm tròn đến hàng phần trăm).'
	
	
	kq=round((1-p_a)*p_b+(1-p_b)*p_a,2)
	kq2=round(p_a*p_b,2)
	kq3=round((1-p_a)*p_b,2)
	kq4=round((1-p_b)*p_a,2)
	xacsuat=f"{kq:.2f}"
	noi_dung_loigiai=f'Gọi ${{A}}$ là biến cố viên thứ nhất bắn trúng. Ta có: $P(A)={p_a_text}$ và $P\\left(\\overline{{A}}\\right)={p_a_ngang}$.\n\n'\
	f'Gọi ${{B}}$ là biến cố viên thứ hai bắn trúng. Ta có: $P(B)={p_b_text}$ và $P\\left(\\overline{{B}}\\right)={p_b_ngang}$.\n\n'\
	f"Do $\\overline{{A}}$ và $\\overline{{B}}$ là độc lập nên xác suất để chỉ một lần bắn trúng đích là:\n\n"\
	f"$P\\left(\\overline{{A}}B \\cup A\\overline{{B}} \\right)=P(\\overline{{A}}).P(B)+P(A).P(\\overline{{B}})$\n$={p_a_ngang}.{p_b_text}+{p_a_text}.{p_b_ngang}={xu_li_dau_cham(xacsuat)}$.\n"

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq:.2f}"
	kq2=f"{kq2:.2f}"
	kq3=f"{kq3:.2f}"
	kq4=f"{kq4:.2f}"

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C9_B1_14]-M2. Cho xác suất bắn trúng bia của 1 xạ thủ. Tính xác suất cả hai lần đều trúng.
def zz8zz_L11_C9_B1_14():      
	
	a=random.randint(1,95)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_ngang=xu_li_dau_cham(p_a_ngang)
	p_b_ngang=xu_li_dau_cham(p_b_ngang)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)

	noi_dung=f"Một xạ thủ bắn lần lượt 2 viên đạn vào một bia." \
	f" Xác suất trúng đích của viên thứ nhất là ${{{p_a_text}}}$ và của viên thứ hai là ${{{p_b_text}}}$."\
	f' Biết rằng kết quả của các lần bắn là độc lập với nhau. Tính xác suất của biến cố "Cả hai lần bắn đều trúng đích" (kết quả làm tròn đến hàng phần trăm).'

	kq=round(p_a*p_b,2)
	kq2=round((1-p_a)*(1-p_b),2)
	kq3=round((1-p_a)*p_b,2)
	kq4=round((1-p_b)*p_a,2)
	xacsuat=f"{kq:.2f}"
	noi_dung_loigiai=f'Gọi ${{A}}$ là biến cố viên thứ nhất bắn trúng. Ta có: $P(A)={p_a_text}$.\n\n'\
	f'Gọi ${{B}}$ là biến cố viên thứ hai bắn trúng. Ta có: $P(B)={p_b_text}$.\n\n'\
	f"Do ${{A}}$ và ${{B}}$ là độc lập nên xác suất để cả hai lần bắn đều trúng đích là:\n\n"\
	f"$P(AB)=P(A).P(B)={p_a_text}.{p_b_text}={xu_li_dau_cham(xacsuat)}$ .\n"

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq:.2f}"
	kq2=f"{kq2:.2f}"
	kq3=f"{kq3:.2f}"
	kq4=f"{kq4:.2f}"

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an

#[D11_C9_B1_15]-M2. Cho xác suất bị bệnh của 2 bệnh nhân. Tìm xác suất cả hai bị biến chứng.
def zz8zz_L11_C9_B1_15():      
	
	a=random.randint(1,95)
	b=random.randint(1,95)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if round(p_a,2)==round(p_b,2):
		p_a=p_a +0.05
	p_a=round(p_a,2)
	p_b=round(p_b,2)
	p_a_ngang=round(1-p_a,2)
	p_b_ngang=round(1-p_b,2)

	p_a_ngang=xu_li_dau_cham(p_a_ngang)
	p_b_ngang=xu_li_dau_cham(p_b_ngang)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)

	noi_dung=f"Hai bệnh nhân ${{X}}$ và ${{Y}}$ bị nhiễm một loại vi rút." \
	f" Biết rằng xác suất bị biến chứng nặng của bệnh nhân ${{X}}$ là ${{{p_a_text}}}$ và của bệnh nhân ${{Y}}$ là ${{{p_b_text}}}$."\
	f' Khả năng bị biến chứng nặng của hai bệnh nhân là độc lập. Tính xác suất của biến cố "Cả hai bệnh nhân đều bị biến chứng nặng" (kết quả làm tròn đến hàng phần trăm).'

	kq=round(p_a*p_b,2)
	kq2=round((1-p_a)*(1-p_b),2)
	kq3=round((1-p_a)*p_b,2)
	kq4=round((1-p_b)*p_a,2)
	xacsuat=f"{kq:.2f}"
	noi_dung_loigiai=f'Gọi ${{A}}$ là biến cố "Bệnh nhân ${{X}}$ bị biến chứng nặng". Ta có: $P(A)={p_a_text}$.\n\n'\
	f'Gọi ${{B}}$ là biến cố "Bệnh nhân ${{Y}}$ bị biến chứng nặng". Ta có: $P(B)={p_b_text}$.\n\n'\
	f"Do ${{A}}$ và ${{B}}$ là độc lập nên xác suất để cả hai bệnh nhân đều bị biến chứng nặng là:\n\n"\
	f"$P(AB)=P(A).P(B)={p_a_text}.{p_b_text}={xu_li_dau_cham(xacsuat)}$ .\n"

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=f"{kq:.2f}"
	kq2=f"{kq2:.2f}"
	kq3=f"{kq3:.2f}"
	kq4=f"{kq4:.2f}"

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

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

	debai_latex= f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\choice\n"\
	    f"{{ {list_PA[0]} }}\n   {{ {list_PA[1]} }}\n     {{ { list_PA[2]} }}\n    {{ { list_PA[3]} }}\n"\
	    f"\\loigiai{{ \n\n {noi_dung_loigiai} \n }}"\
	    f"\\end{{ex}}\n"

	latex_tuluan=f"\\begin{{ex}}\n {noi_dung}\n \n"\
	    f"\\loigiai{{ \n\n  {noi_dung_loigiai} \n\n }}"\
	    f"\\end{{ex}}\n"

	return debai,debai_latex,loigiai_word,phuongan,latex_tuluan, loigiai_traloingan,dap_an



#BÀI 2- BIẾN CỐ HỢP - QUY TẮC CỘNG XÁC SUẤT
#[D11_C9_B2_01]-M2. Hộp chứa các viên bi có 2 màu. Phát biểu biến cố hợp.
def zz8zz_L11_C9_B2_01():   
    #Tạo bậc ngẫu nhiên
	n1 =random.randint(8,20)
	n2 =random.randint(8,20)

	mau1=random.choice(["màu đỏ", "màu đen", "màu xanh dương", "màu hồng"])
	mau2=random.choice(["màu vàng", "màu trắng", "màu tím", "màu nâu"])

	noi_dung=f"Một hộp chứa {n1} viên bi {mau1} và {n2} viên bi {mau2}. Lấy ngẫu nhiên hai viên bi. Xét các biến cố:\n\n" \
	f"${{P}}$ : Hai viên bi lấy được có {mau1}.\n\n"\
	f"${{Q}}$ : Hai viên bi lấy được có {mau2}.\n\n"\
	f"Khi đó biến cố hợp của hai biến cố ${{P}}$ và ${{Q}}$ là:"

    
	kq=f"Hai viên bi lấy ra có cùng màu"
	kq2=f"Hai viên bi lấy ra có màu khác nhau"
	kq3=f"Hai viên bi lấy ra chỉ có màu {mau1}"
	kq4=f"Hai viên bi lấy ra chỉ có màu {mau2}"

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
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Biến cố hợp của hai biến cố ${{P}}$ và ${{Q}}$  là ${{P}}$  hoặc ${{P}}$ xảy ra.\n\n"\
					f"Do đó $P \\cup Q$ là biến cố hai viên bi lấy ra có cùng màu."    
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B2_02]-M2. Hộp chứa các viên bi, lấy ra rồi trả lại. Phát biểu biến cố hợp.
def zz8zz_L11_C9_B2_02():   
    #Tạo bậc ngẫu nhiên
	m =random.randint(8,20)
	so_lan =random.randint(5,9)
	j=random.randint(1,so_lan-1)
	k=random.randint(1,so_lan)
	if j==k: j=j+1
	if j>k:
		t=j
		j=k
		k=t

	mau=random.choice(["màu đỏ", "màu đen", "màu xanh dương", "màu hồng", "màu vàng", "màu trắng", "màu tím", "màu nâu"])

	noi_dung=f'Một hộp chứa {m} viên bi có màu sắc khác nhau. Lấy ngẫu nhiên một viên bi, quan sát màu sắc rồi trả lại vào hộp. ' \
	f'Tiếp tục lấy lần 2 rồi trả lại, cứ tiếp tục như thế đến {so_lan} lần. Gọi ${{A_i}}$ là biến cố "Lần thứ ${{i}}$ lấy được viên bi {mau}". '\
	f'Mệnh đề nào dưới đây mô tả biến cố $A_{j} \\cap A_{k}$?\n\n'
    
	kq=f"Cả hai lần lấy thứ ${{{j}}}$ và thứ ${{{k}}}$ đều lấy được bi {mau}"
	kq2=f"Cả hai lần lấy thứ ${{{j}}}$ và thứ ${{{k}}}$ đều không lấy được bi {mau}"
	kq3=f"Ít nhất một trong các lần lấy thứ ${{{j}}}$ và thứ ${{{k}}}$ đều lấy được bi {mau}"
	kq4=f"Lần rút đầu tiên lấy được bi {mau} là lần lấy thứ {int((j+k)/2)}"

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
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"


	noi_dung_loigiai=f"Biến cố $A_{j} \\cap A_{k}$ là {kq}."
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B2_03]-M2. Gieo một con xúc xắc và 1 đồng xu.Tìm số phần tử của biến cố hợp.
def zz8zz_L11_C9_B2_03():   
	chon=random.randint(1,8)	
	if chon==1:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt sấp và xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in [2,4,6]:
			set_A.add(f"S{i}")
				
		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	if chon==2:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt sấp và xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in [1,3,5]:
			set_A.add(f"S{i}")

		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")
	if chon==3:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in [1,3,5]:
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")
	if chon==4:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in [2,4,6]:
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")
	
	if chon==5:
		k=random.randint(1,5)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số lớn hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(k+1,7):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,4,6]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")
	if chon==6:
		k=random.randint(1,5)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số lớn hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(k+1,7):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [1,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")
	if chon==7:
		k=random.randint(2,6)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số nhỏ hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(1,k):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [1,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")
	if chon==8:
		k=random.randint(2,6)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số nhỏ hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Số phần tử của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(1,k):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,4,6]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	set_kq= set_A | set_B
	list_set_A=list(set_A)
	list_set_B=list(set_B)
	list_set_kq=list(set_kq)
	list_set_A.sort()
	list_set_B.sort()
	list_set_kq.sort()

	kq=len(set_kq)
	kq2=kq+random.randint(1,4)
	kq3=kq+random.randint(5,8)
	kq4=abs(kq-random.randint(2,5))

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]    


	#Tạo các phương án
	pa_A= f"*${{{my_module.hien_phan_so(kq)}}}$"
	pa_B= f"${{{my_module.hien_phan_so(kq2)}}}$"
	pa_C= f"${{{my_module.hien_phan_so(kq3)}}}$"
	pa_D= f"${{{my_module.hien_phan_so(kq4)}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"

	noi_dung_loigiai=f"Biến cố ${{A}}$ có các phần tử là ${thay_the_tap_hop(str(list_set_A))}$.\n\n"\
	f"Biến cố ${{B}}$ có các phần tử là ${thay_the_tap_hop(str(list_set_B))}$.\n\n"\
	f"Biến cố $A\\cup B={thay_the_tap_hop(str(list_set_kq))}$. Số phần tử của $A\\cup B$ là ${kq}$."
	
	
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#9.1.4 Xác suất biến cố hợp
#[D11_C9_B2_04]-M1. Cho A, B xung khắc và P(A), P(B). Tính P(AUB).
def zz8zz_L11_C9_B2_04():      
	
	a=random.randint(1,45)
	b=random.randint(1,65)
	p_a=float(f"0.{a}")
	p_b=float(f"0.{b}")
	if p_a==p_b:
		p_a=p_a + 0.05
	if p_a+p_b>1:
		p_b=round(1-p_a-random.choice([0.01,0.05,0.04,0.03,0.02]),2)

	p_a_text=xu_li_dau_cham(p_a)
	p_b_text=xu_li_dau_cham(p_b)	

	kq=round(p_a+p_b,2)
	kq2=round(p_a*p_b,2)
	kq3=round((1-p_b)*p_a,2)
	kq4=round((1-p_a)*(1-p_b),2)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]

	kq=xu_li_dau_cham(kq)
	kq2=xu_li_dau_cham(kq2)
	kq3=xu_li_dau_cham(kq3)
	kq4=xu_li_dau_cham(kq4)

	#Tạo các phương án
	pa_A= f"*${{{kq}}}$"
	pa_B= f"${{{kq2}}}$"
	pa_C= f"${{{kq3}}}$"
	pa_D= f"${{{kq4}}}$"

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	noi_dung=f"Cho ${{A}}$ và ${{B}}$ là hai biến cố xung khắc." \
	f" Biết $P(A)={p_a_text}$ và $P(B)={p_b_text}$."\
	f" Tính xác suất của biến cố ${{A \\cup B}}$."
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"



	noi_dung_loigiai=f"$P(A \\cup B)=P(A)+P(B)={p_a_text}+{p_b_text}={kq}$ .\n"				
	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B2_05]-M2. Gieo một con xúc xắc và 1 đồng xu. Tính xác suất của biến cố hợp.
def zz8zz_L11_C9_B2_05():   
	chon=random.randint(1,8)
	
	if chon==1:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt sấp và xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in [2,4,6]:
			set_A.add(f"S{i}")
				
		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")


	if chon==2:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt sấp và xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in [1,3,5]:
			set_A.add(f"S{i}")

		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	if chon==3:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in [1,3,5]:
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	if chon==4:
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số nguyên tố".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in [2,4,6]:
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")


	if chon==5:
		k=random.randint(1,5)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số lớn hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(k+1,7):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,4,6]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	if chon==6:
		k=random.randint(1,5)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số lớn hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(k+1,7):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [1,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	if chon==7:
		k=random.randint(2,6)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số nhỏ hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số lẻ".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(1,k):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [1,3,5]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	if chon==8:
		k=random.randint(2,6)
		noi_dung=f'Gieo đồng thời một đồng xu và một con xúc xắc.\n\n' \
		f'Gọi ${{A}}$ là biến cố: "Đồng xu xuất hiện mặt ngửa và xúc xắc xuất hiện mặt chứa số nhỏ hơn {k}".\n\n'\
		f'Gọi ${{B}}$ là biến cố: "Xúc xắc xuất hiện mặt chứa số chẵn".\n\n'\
		f'Tính xác suất của biến cố $A \\cup B$.'
		set_A=set()
		for i in range(1,k):
			set_A.add(f"N{i}")

		set_B=set()
		for i in [2,4,6]:
			set_B.add(f"S{i}")
			set_B.add(f"N{i}")

	set_kq= set_A | set_B
	list_set_A=list(set_A)
	list_set_B=list(set_B)
	list_set_kq=list(set_kq)
	list_set_A.sort()
	list_set_B.sort()
	list_set_kq.sort()

	kq=len(set_kq)/12
	kq3=(len(set_A)+len(set_B))/12
	kq2=(kq+random.randint(1,3))/12
	
	kq4=abs(kq-random.randint(2,5))/12

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
    

	#Tạo các phương án
	pa_A= my_module.frac_to_dfrac(f"*${{{latex(my_module.hien_phan_so(kq))}}}$")
	pa_B= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq2))}}}$")
	pa_C= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq3))}}}$")
	pa_D= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq4))}}}$")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	phuongan=my_module.frac_to_dfrac(phuongan)

	noi_dung_loigiai=f"Số phần tử của không gian mẫu là: $n(\\Omega)=2.6=12$.\n\n"\
	f"Biến cố ${{A}}$ có các phần tử là ${thay_the_tap_hop(str(list_set_A))}$.\n\n"\
	f"Biến cố ${{B}}$ có các phần tử là ${thay_the_tap_hop(str(list_set_B))}$.\n\n"\
	f"Biến cố $A\\cup B={thay_the_tap_hop(str(list_set_kq))}$. Số phần tử của $A\\cup B$ là $n(A\\cup B)={len(set_kq)}$.\n\n"\
	f"Xác suất của biến cố $A\\cup B$: $P=\\dfrac{{{len(set_kq)}}}{{12}}={latex(my_module.hien_phan_so(kq))}$.\n\n"
	noi_dung_loigiai=my_module.frac_to_dfrac(noi_dung_loigiai)


	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B2_06]-M2. Cho 2 nhóm đồ vật. Tính xác suất để số vật được chọn thuộc cùng 1 nhóm.
def zz8zz_L11_C9_B2_06():   
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]

	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	cung_nhom=["cùng giới tính", "cùng màu", "cùng thể loại truyện", "cùng thể loại tranh", "cùng thể loại sách"]

	i=random.randint(0,len(vat_1)-1)
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	cung_nhom = cung_nhom[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	so_vat_1=random.randint(6,15)
	so_vat_2=random.randint(6,15)
	if so_vat_1==so_vat_2: so_vat_1=so_vat_1+random.randint(1,5)
	k=random.randint(3,min(so_vat_1,so_vat_2))
	n=so_vat_1 + so_vat_2

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} từ {address}."\
	f' Tính xác suất của biến cố "Cả ${{{k}}}$ {ten_chung} được chọn đều {cung_nhom}".'

	kq=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/binomial(n,k)
	kq2=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/chinh_hop(k,n)
	kq3=binomial(so_vat_1,k)/binomial(n,k)
	kq4=binomial(so_vat_2,k)/binomial(n,k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	  

	#Tạo các phương án
	pa_A= my_module.frac_to_dfrac(f"*${{{latex(my_module.hien_phan_so(kq))}}}$")
	pa_B= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq2))}}}$")
	pa_C= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq3))}}}$")
	pa_D= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq4))}}}$")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	phuongan=my_module.frac_to_dfrac(phuongan)

	noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} là: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_1} là: $C^{{{k}}}_{{{so_vat_1}}}={binomial(so_vat_1,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_2} là: $C^{{{k}}}_{{{so_vat_2}}}={binomial(so_vat_2,k)}$.\n\n"\
	f"Xác suất cần tính là: $P=\\dfrac{{{binomial(so_vat_1,k)}+{binomial(so_vat_2,k)}}} {{{binomial(n,k)}}}={latex(my_module.hien_phan_so(kq))}$."\


	noi_dung_loigiai=my_module.frac_to_dfrac(noi_dung_loigiai)


	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B2_07]-M2. Cho 2 nhóm sách tham khảo. Tính xác suất để số vật được chọn thuộc cùng 1 loại.
def zz8zz_L11_C9_B2_07():   
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]

	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	cung_nhom=["cùng giới tính", "cùng màu", "cùng thể loại truyện", "cùng thể loại tranh", "cùng thể loại sách"]

	i=0
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	cung_nhom = cung_nhom[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	
	so_vat_1=random.randint(6,15)
	so_vat_2=random.randint(6,15)
	if so_vat_1==so_vat_2: so_vat_1=so_vat_1+random.randint(1,5)
	k=random.randint(3,min(so_vat_1,so_vat_2))
	n=so_vat_1 + so_vat_2

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} từ {address}."\
	f' Tính xác suất của biến cố "Cả ${{{k}}}$ {ten_chung} được chọn đều {cung_nhom}".'

	kq=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/binomial(n,k)
	kq2=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/chinh_hop(k,n)
	kq3=binomial(so_vat_1,k)/binomial(n,k)
	kq4=binomial(so_vat_2,k)/binomial(n,k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	  

	#Tạo các phương án
	pa_A= my_module.frac_to_dfrac(f"*${{{latex(my_module.hien_phan_so(kq))}}}$")
	pa_B= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq2))}}}$")
	pa_C= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq3))}}}$")
	pa_D= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq4))}}}$")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	phuongan=my_module.frac_to_dfrac(phuongan)

	noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} là: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_1} là: $C^{{{k}}}_{{{so_vat_1}}}={binomial(so_vat_1,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_2} là: $C^{{{k}}}_{{{so_vat_2}}}={binomial(so_vat_2,k)}$.\n\n"\
	f"Xác suất cần tính là: $P=\\dfrac{{{binomial(so_vat_1,k)}+{binomial(so_vat_2,k)}}} {{{binomial(n,k)}}}={latex(my_module.hien_phan_so(kq))}$."\


	noi_dung_loigiai=my_module.frac_to_dfrac(noi_dung_loigiai)


	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B2_08]-M2. Cho các viên bi. Tính xác suất để các bi được chọn cùng màu.
def zz8zz_L11_C9_B2_08():   
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]

	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	cung_nhom=["cùng giới tính", "cùng màu", "cùng thể loại truyện", "cùng thể loại tranh", "cùng thể loại sách"]

	i=1
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	cung_nhom = cung_nhom[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	
	so_vat_1=random.randint(6,15)
	so_vat_2=random.randint(6,15)
	if so_vat_1==so_vat_2: so_vat_1=so_vat_1+random.randint(1,5)

	k=random.randint(3,min(so_vat_1,so_vat_2))
	n=so_vat_1 + so_vat_2

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} từ {address}."\
	f' Tính xác suất của biến cố "Cả ${{{k}}}$ {ten_chung} được chọn đều {cung_nhom}".'

	kq=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/binomial(n,k)
	kq2=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/chinh_hop(k,n)
	kq3=binomial(so_vat_1,k)/binomial(n,k)
	kq4=binomial(so_vat_2,k)/binomial(n,k)
	

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	  

	#Tạo các phương án
	pa_A= my_module.frac_to_dfrac(f"*${{{latex(my_module.hien_phan_so(kq))}}}$")
	pa_B= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq2))}}}$")
	pa_C= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq3))}}}$")
	pa_D= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq4))}}}$")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	phuongan=my_module.frac_to_dfrac(phuongan)

	noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} là: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_1} là: $C^{{{k}}}_{{{so_vat_1}}}={binomial(so_vat_1,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_2} là: $C^{{{k}}}_{{{so_vat_2}}}={binomial(so_vat_2,k)}$.\n\n"\
	f"Xác suất cần tính là: $P=\\dfrac{{{binomial(so_vat_1,k)}+{binomial(so_vat_2,k)}}} {{{binomial(n,k)}}}={latex(my_module.hien_phan_so(kq))}$."\


	noi_dung_loigiai=my_module.frac_to_dfrac(noi_dung_loigiai)


	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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

#[D11_C9_B2_09]-M2. Cho các cuốn truyện. Tính xác suất để các cuốn được chọn cùng thể loại.
def zz8zz_L11_C9_B2_09():   
	do_vat_1=["cuốn sách tham khảo môn Toán 10", "cuốn sách tham khảo môn Văn 10", "cuốn sách tham khảo môn Tiếng Anh 10", "cuốn sách tham khảo môn Vật Lí 10", "cuốn sách tham khảo môn Hóa Học 10", "cuốn sách tham khảo môn Sinh Học 10"]
	do_vat_2=["cuốn truyện cổ tích", "cuốn truyện tuyển thuyết", "cuốn truyện khoa học viễn tưởng", "cuốn truyện trinh thám", "cuốn truyện ngắn"]
	do_vat_3=["bức tranh lụa", "bức tranh gỗ","bức tranh sơn dầu", "bức tranh sơn mài", "bức tranh Đông Hồ"]
	do_vat_4=["viên bi màu xanh", "viên bi màu đen","viên bi màu trắng", "viên bi màu đỏ", "viên bi màu vàng"]
	random.shuffle(do_vat_1)
	sach_1, sach_2=do_vat_1[0], do_vat_1[1]

	random.shuffle(do_vat_2)
	truyen_1, truyen_2=do_vat_2[0], do_vat_2[1]

	random.shuffle(do_vat_3)
	buctranh_1, buctranh_2=do_vat_3[0], do_vat_3[1]

	random.shuffle(do_vat_4)
	vienbi_1, vienbi_2=do_vat_4[0], do_vat_4[1]

	vat_1=["học sinh nam", f"{vienbi_1}", f"{truyen_1}", f"{buctranh_1}", f"{sach_1}"]
	vat_2=["học sinh nữ", f"{vienbi_2}", f"{truyen_2}", f"{buctranh_2}", f"{sach_2}"]
	address=["lớp học", "hộp", "thư viện", "tiệm tranh", "nhà sách"]
	ten_chung=["học sinh", "viên bi", "cuốn truyện", "bức tranh", "cuốn sách"]
	in_where=["của lớp","trong hộp", "để đọc","để mua", "để mua"]
	cung_nhom=["cùng giới tính", "cùng màu", "cùng thể loại truyện", "cùng thể loại tranh", "cùng thể loại sách"]

	i=2
	vat_1, vat_2, address,in_where, ten_chung =vat_1[i], vat_2[i], address[i], in_where[i], ten_chung[i]
	cung_nhom = cung_nhom[i]
	st_khac=""
	if i != 0:
		st_khac=f", các {ten_chung} là khác nhau"

	so_vat_1=random.randint(6,15)
	so_vat_2=random.randint(6,15)
	if so_vat_1==so_vat_2: so_vat_1=so_vat_1+random.randint(1,5)
	k=random.randint(3,min(so_vat_1,so_vat_2))
	n=so_vat_1 + so_vat_2

	noi_dung=f"Một {address} có ${{{so_vat_1}}}$ {vat_1} và ${{{so_vat_2}}}$ {vat_2}{st_khac}. Chọn ngẫu nhiên ${{{k}}}$ {ten_chung} từ {address}."\
	f' Tính xác suất của biến cố "Cả ${{{k}}}$ {ten_chung} được chọn đều {cung_nhom}".'

	kq=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/binomial(n,k)
	kq2=(binomial(so_vat_1,k)+binomial(so_vat_2,k))/chinh_hop(k,n)
	kq3=binomial(so_vat_1,k)/binomial(n,k)
	kq4=binomial(so_vat_2,k)/binomial(n,k)

	pa_kotrung=my_module.khong_trung_so(kq,kq2,kq3,kq4)
	kq2=pa_kotrung[1]
	kq3=pa_kotrung[2]
	kq4=pa_kotrung[3]
	  

	#Tạo các phương án
	pa_A= my_module.frac_to_dfrac(f"*${{{latex(my_module.hien_phan_so(kq))}}}$")
	pa_B= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq2))}}}$")
	pa_C= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq3))}}}$")
	pa_D= my_module.frac_to_dfrac(f"${{{latex(my_module.hien_phan_so(kq4))}}}$")

	#Trộn các phương án
	list_PA =[pa_A, pa_B, pa_C, pa_D]
	random.shuffle(list_PA)
	dap_an=my_module.tra_ve_dap_an(list_PA)   

	
	debai= f"{noi_dung}\n"
	phuongan= f"A. { list_PA[0]}.\t   B. { list_PA[1]}.\t     C. { list_PA[2]}.\t     D. { list_PA[3]}.\n"
	phuongan=my_module.frac_to_dfrac(phuongan)

	noi_dung_loigiai=f"Số cách chọn ${{{k}}}$ {ten_chung} là: $C^{{{k}}}_{{{n}}}={binomial(n,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_1} là: $C^{{{k}}}_{{{so_vat_1}}}={binomial(so_vat_1,k)}$.\n\n"\
	f"Số cách chọn ${{{k}}}$ {ten_chung} từ {vat_2} là: $C^{{{k}}}_{{{so_vat_2}}}={binomial(so_vat_2,k)}$.\n\n"\
	f"Xác suất cần tính là: $P=\\dfrac{{{binomial(so_vat_1,k)}+{binomial(so_vat_2,k)}}} {{{binomial(n,k)}}}={latex(my_module.hien_phan_so(kq))}$."\


	noi_dung_loigiai=my_module.frac_to_dfrac(noi_dung_loigiai)


	loigiai_word=f"Lời giải:\n Chọn {dap_an} \n {noi_dung_loigiai} \n"
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