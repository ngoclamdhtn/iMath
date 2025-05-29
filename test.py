import D10_C1,D10_C2, D10_C3, D10_C4, D10_C5, D10_C6, D10_C7,D10_C8,D10_C9,D10_C10, D11_C1, D11_C2, D11_C3, D11_C4, D11_C5, D11_C6,D11_C7, D11_C8,D11_C9, D12_C1,D12_C2, D12_C4,D12_C5,D12_C6, D12_C7
import D12_C3
import my_module
import math
import random
import sympy as sp
from sympy import *
from fractions import Fraction
from docx import Document

import pyperclip

#Test trắc nghiệm
# test, test_latex="",""
# for i in range(1):
# 	debai_word,debai_latex,loigiai_word,phuongan,latex_tuluan,loigiai_traloingan,dap_an=D12_C4.ckz_L12C4_B5_34()
# 	test=test + f"{debai_word}\n{phuongan}\n{loigiai_word}\n"
# 	test_latex=test_latex + f"{debai_latex}\n"
# 	#print(test)
# 	print(test_latex)
# 	pyperclip.copy(test_latex)



# #Test đúng sai
test, test_latex="",""
for i in range(1):
	debai,debai_latex,loigiai_word,dap_an =D12_C6.newy25_L12_C6_B2_38()
	#print(debai)
	#print(loigiai_word)
	test=test + f"{debai}\n{loigiai_word}\n"
	test_latex=test_latex + f"{debai_latex}\n"
	print(test_latex)
pyperclip.copy(test_latex)

#Test tự luận
# test, test_latex="",""
# for i in range(1):
# 	debai_word,loigiai_word,latex_tuluan,dap_an = D11_C2.mn8mn_L11_C2_B3_01()
# 	#print(debai)\\log {d}
# 	#print(loigiai_word)
# 	test=test + f"{debai_word}\n{loigiai_word}\n"
# 	test_latex=test_latex + f"{latex_tuluan}\n"
# 	print(test_latex)
# pyperclip.copy(test_latex)









