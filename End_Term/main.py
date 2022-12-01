import numpy as np 
from sympy import *
#------------ A = Q * S ------------

#-----------size for matrix--------------
matrix_size = int(input("What is the size of matrix?"))

#----------fill our matrix randomly------------
matrix_A = np.random.randint(0,4 , size = (matrix_size,matrix_size))
print(matrix_A, " This is matrix A","\n")

#----------take transpose of our matrix---------
#matrix_A_transpose = matrix_A.transpose()
list_A_transpose=[] 
matrix_str1=[] 
for i in range(0,matrix_size): 
    for j in range(0,matrix_size): 
        matrix_str1.append(matrix_A[j][i]) 
    list_A_transpose.append(matrix_str1) 
    matrix_str1=[] 
matrix_A_transpose = np.matrix(list_A_transpose)
print(matrix_A_transpose," This is transpoed matrix ","\n")

#---------- A(transpose) * A -----------------
matrix_AtA1 =np.matrix(np.matmul(matrix_A_transpose , matrix_A))
print(matrix_AtA1," This is our A transpose * A matrix in R field ","\n")

#----------Take by Z5-------------
str_AtA = []
list_AtA = []
for i in range(0,matrix_size):
    for j in range(0,matrix_size):
        str_AtA.append(matrix_AtA1.item(i,j) % 5 )
    list_AtA.append(str_AtA)
    str_AtA=[]
matrix_AtA = np.matrix(list_AtA)
print(matrix_AtA," This is A transpose A in Z5 field ","\n")

#---------- Eigenvalue matrix ---------------
x = var("x")
matrix_str2 = []
list_eigenvalue =[]
for i in range(0,matrix_size):
    for j in range(0,matrix_size):
        if i==j :
            matrix_str2.append(x)
        else:
            matrix_str2.append(0)
    list_eigenvalue.append(matrix_str2)
    matrix_str2=[]
matrix_eigenvalue = np.matrix(list_eigenvalue)
print(matrix_eigenvalue," This is our diagonal eigenvalue matrix ","\n")  

#------------Add lambdas to AtA matrix------------
matrix_AtA_lambda = np.matrix(matrix_AtA - matrix_eigenvalue)
print(matrix_AtA_lambda," This is matrix for definding polinomials ","\n")

#------------find determinante----------------
sum = 0 
for i in range(0,matrix_size):
    for j in range(0,matrix_size):
        if matrix_size == 2:
            sum = matrix_AtA_lambda.item(0,0) * matrix_AtA_lambda.item(1,1) - matrix_AtA_lambda.item(0,1) * matrix_AtA_lambda.item(1,0)
        elif matrix_size == 3 :
            sum = matrix_AtA_lambda.item(0,0)* (matrix_AtA_lambda.item(1,1) * matrix_AtA_lambda.item(2,2) - matrix_AtA_lambda.item(1,2) * matrix_AtA_lambda.item(2,1)) - matrix_AtA_lambda.item(0,1) * (matrix_AtA_lambda.item(1,0) * matrix_AtA_lambda.item(2,2) - matrix_AtA_lambda.item(2,0) * matrix_AtA_lambda.item(1,2)) + matrix_AtA_lambda.item(0,2) * (matrix_AtA_lambda.item(1,0)*matrix_AtA_lambda.item(2,1)-matrix_AtA_lambda.item(2,0)*matrix_AtA_lambda.item(1,1))
print(sum," = 0 ","This is our equation","\n")
'''
#--------------find roots--------------
for x in sum :
    x = -100 
    while x<= 100 :
        if sum == 0 :
            print("x=",x)
        x+=0.5
'''

#------------eigenvalues--------------
eigen_list1 = np.linalg.eigvals(matrix_AtA)
print(eigen_list1,"They are our eigenvalues","\n")

eigen_list = []
for x in eigen_list1:
    eigenvalue = (round(x) * 36 ) % 5 
    eigen_list.append(eigenvalue)
print(eigen_list," They are our eigenvalues in Z5", "\n")
#------ diagonal matrix ------------
diagonal_list = []
diagonal_str = []
for x in eigen_list:
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            if i==j:
                diagonal_str.append(x)
            else:
                diagonal_str.append(0)
        diagonal_list.append(diagonal_str)
        diagonal_str = []
    matrix_diagonal = np.matrix(diagonal_list)
print(matrix_diagonal,"This is diagonal matrix with known eigenvalues","\n")

#-----------Deviding matrix into 3-----------
deviding_list = matrix_diagonal.reshape(-1)
print(deviding_list)

matrices_3x3 = deviding_list.reshape(3)
'''
#----------Matrix For System --------------
matrix_for_system = np.matrix(matrix_AtA - matrix_diagonal)
print(matrix_for_system,"This is the difference matrix fo system","\n")

#---------Solving this system -----------------
if matrix_size == 3:
    a = var("a")
    b = var("b")
    c = var("c")
    matrix_2_0 = np.matrix([[a],
                        [b],
                        [c]])
elif matrix_size ==2:
    a = var("a")
    b = var("b")
    matrix_2_0 = np.matrix([[a],
                             [b]])    
print(matrix_2_0)

zero_array = ([0,0,0])
sol = np.linalg.solve(matrix_for_system,zero_array)
print(sol)
#matrix_inverse_A = np.linalg.inv(matrix_A)
#print(matrix_inverse_A)      
'''