# -*- coding: utf-8 -*-
"""
Created on Tue Jun 07 11:30:58 2016

@author: lenovo
"""

#Filename:NameLetterPrint


#--------------------------*--------------------------------------------------------
A=['    #       ','   # #      ','  #####     ',' #     #    ','#       #   ']
B=['# # # #     ','#       #   ','# # # #     ','#       #   ','# # # #     ']
C=['  # # # #   ','#           ','#           ','#           ','  # # # #   ']
D=['# ## #      ','#      #    ','#       #   ','#      #    ','# ## #      ']
E=['# # # # #   ','#           ','# # # # #   ','#           ','# # # # #   ']
F=['# # # # #   ','#           ','# # # #     ','#           ','#           ']
G=['   # # ##   ',' #          ','#     # #   ',' #      #   ','  # # # #   ']
H=['#       #   ','#       #   ','# # # # #   ','#       #   ','#       #   ']
I=['  # # #     ','    #       ','    #       ','    #       ','  # # #     ']
J=['     ####   ','        #   ','        #   ','   #    #   ','     # #    ']
K=[' #      #   ',' #    #     ',' #  #       ',' #    #     ',' #      #   ']
L=['#           ','#           ','#           ','#       #   ','# # # # #   ']
M=['#       #   ','# #   # #   ','#  # #  #   ','#   #   #   ','#       #   ']
N=['#       #   ','# #     #   ','#   #   #   ','#     # #   ','#       #   ']
O=['   # #      ',' #     #    ',' #     #    ',' #     #    ','   # #      ']
P=['# # # #     ','#      #    ','# # # #     ','#           ','#           ']
Q=['   # #      ',' #     #    ',' #     #    ','   # #      ','     # #    ']
R=['# # # #     ','#      #    ','# # # #     ','#   #       ','#      #    ']
S=['  # # #     ',' #          ','  # # #     ','       #    ','  # # #     ']
T=['# # # # #   ','    #       ','    #       ','    #       ','    #       ']
U=['#       #   ','#       #   ','#       #   ',' #     #    ','  # # #     ']
V=['#       #   ',' #     #    ','  #   #     ','   # #      ','    #       ']
W=['#       #   ','#   #   #   ','#  # #  #   ','# #   # #   ','#       #   ']
X=['#       #   ','  #   #     ','    #       ','  #   #     ','#       #   ']
Y=['#       #   ','  #   #     ','    #       ','    #       ','    #       ']
Z=['# # # # #   ','      #     ','    #       ','  #         ','# # # # #   ']
#--------------------------*----------------------------------------------

let_dict={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R,'S':S,'T':T,'U':U,'V':V,'W':W,'X':X,'Y':Y,'Z':Z}

#------------------------------------------------------------------------------------------------------------

name=raw_input('Please input your name: ')
NAME=name.upper()   #to convert word to uppercase

#--------------------------------------------------------------------------
let_list=['']*5
for k in range(5):
    for i in range(len(NAME)):
        if NAME[i]==' ':
            let_list[k]=let_list[k]+'        '
        else:
            let_list[k]=let_list[k]+let_dict[NAME[i]][k]
#--------------------------------------------------------------------------

for i in range(5):
    print let_list[i]  #output the printed character
        
        
        
        
        
        
