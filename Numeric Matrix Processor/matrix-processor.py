# ------------------------------------
#
#  Author : Ankit Dhiman
#  Date   : 3 / 07 / 2020
#  matrix-processor.py
#
#  compute different matrx operations on matrices
#
# ------------------------------------#




def choices():
    print("\n1. Add matrices ")
    print("2. Multiply matrix by a constant ")
    print("3. Multiply matrices") 
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse Matrix")
    print("0. Exit")
    

    choice = int(input("Your choice: " ))

    if(choice == 1):
        MatrixAddition()
    elif(choice == 2):
        ConstantMultiplication()
    elif(choice == 3):
        MatrixMultiplication()
    elif(choice == 4):
        print("1. Main diagonal ")
        print("2. Side diagonal ")
        print("3. Vertical line") 
        print("4. Horizontal line")
        
        k = int(input("Your choice: "))
        if(k == 1):
            MainDiagonal()
        elif(k==2):
            SideDiagonal()
        elif(k==3):
            VerticalLine()
        elif(k==4):
            HorizontalLine()  
        else:
            print("Invalid input ! ")
            exit()          
            
    elif(choice ==5):
        Determinant()
    
    elif(choice == 6):
        InverseMatrix()
        
    elif(choice == 0):
        exit()
    
    else:
        print("Invalid input ! ")
        exit()

#---------------------------------------------------------------------------


def PromptMatSize():
    print("Enter matrix size:    ")
    
#--------------------------------------------------------------------------- 
        
    
def PrintMatrix(c):
    print("\nThe result is:")
    for i in c:
        print(" ".join(map(str,i)))
        
    choices()    

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
    
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    elif len(m) == 1:
        return m[0][0] 
            
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def Determinant():
    m = []
    d = 0
    PromptMatSize()
    m1,n1 =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        m.append([float(j) for j in input().split()])
    
    print("The result is: \n",getMatrixDeternminant(m))

                    
 
 
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def MatrixAddition():
    a = []
    b = []
    c = []
    PromptMatSize()
    m1,n1 =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        a.append([float(j) for j in input().split()])
    
    m2,n2 =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m2):
        b.append([float(j) for j in input().split()])

    c = [[a[i][j] + b[i][j]  for j in range(len(a[i]))] for i in range(len(a))]
    
    PrintMatrix(c)                       


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def ConstantMultiplication():
    a = []
    c = []
    PromptMatSize()
    m1,n1 =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        a.append([float(j) for j in input().split()])
    k = int(input())

    c = [[ k*a[i][j]  for j in range(len(a[i]))] for i in range(len(a))]
    
    PrintMatrix(c)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


def MainDiagonal():
    
    a = []
    c = []
    PromptMatSize()
    m1,n1 =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        a.append([float(j) for j in input().split()])
       
    c = [[ a[j][i]  for j in range(len(a))] for i in range(len(a[i]))]
    PrintMatrix(c)




def SideDiagonal():
    a = []
    c = []
    PromptMatSize()
    m1,n =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        a.append([float(j) for j in input().split()])
    
    c = [[ a[(n - 1) - j][(n - 1) - i]  for j in range(len(a[i]))] for i in range(len(a))]
    
    PrintMatrix(c)
 

def VerticalLine():
    a = []
    c = []
    PromptMatSize()
    m1,n =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        a.append([float(j) for j in input().split()])
    
    c = [[ a[i][(n-1) - j]  for j in range(len(a[i]))] for i in range(len(a))]
    
    PrintMatrix(c)


def HorizontalLine():
    a = []
    c = []
    PromptMatSize()
    m1,n =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        a.append([float(j) for j in input().split()])
    
    c = [[ a[(n - 1) - i][ j]  for j in range(len(a[i]))] for i in range(len(a))]
    PrintMatrix(c)
    
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

                        
def MatrixMultiplication():
    a = []
    b = []
    c = []
    PromptMatSize()

    m1,n1 =map(int, input().split())
    print("Enter matrix: ")
    for i in range(0,m1):
        a.append([float(j) for j in input().split()])
    print("Enter matrix: ")
    m2,n2 =map(int, input().split())
    
    for i in range(0,m2):
        b.append([float(j) for j in input().split()])    
    
    c = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*b)] for X_row in a]

    
    PrintMatrix(c)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------



      
def InverseMatrix():
    m = []
    adj = []
    inv = []
    cf = []
    PromptMatSize()
    m1,n1 =map(int, input().split())

    print("Enter matrix: ")
    for i in range(0,m1):
        m.append([float(j) for j in input().split()])
     
    det = getMatrixDeternminant(m) 
    if det == 0 :
        print("This matrix doesn't have an inverse.")
        choices()
    else:
        
        cf = [[ pow(-1 ,(i + j)) * getMatrixDeternminant(getMatrixMinor(m,i,j)) for j in range(len(m[i])) ] for i in range(len(m)) ]
        adj = [[ cf[j][i]  for j in range(len(cf))] for i in range(len(cf[i]))]
        inv = [[ round(adj[i][j]/det , 3) for j in range(len(adj[i])) ] for i in range(len(adj)) ]
        
        PrintMatrix(inv)
        
        
        
        


    
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

#print(" \n\t \tMatrix Processor ")

if __name__ == '__main__':
    choices()


    
    




          
          
