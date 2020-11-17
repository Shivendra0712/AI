"""
Applications of N-Queens
These are given below:
1. VLSI Testing.
2. Traffic control.
3. Deadlock Prevention.
4. Image Processing.
5. Motion Estimation.
6. Register Allocation. 

"""


def leftDiag(B,a,b):
    inval=False
    for i in range(1,n):
        if a+i in range(n) and b+i in range(n):
            if B[a+i][b+i]==1:
                inval=True
                break
        elif a-i in range(n) and b-i in range(n):
            if B[a-i][b-i]==1:
                inval=True
                break
        else:
            break
    return not inval
def rightDiag(B,a,b):
    inval=False
    for i in range(1,n):
        if a+i in range(n) and b-i in range(n):
            if B[a+i][b-i]==1:
                inval=True
                break
        elif a-i in range(n) and b+i in range(n):
            if B[a-i][b+i]==1:
                inval=True
                break
        else:
            break
    return not inval
    

def check(b):
    B=list(b);inval=False
    for i in range(n):
        for j in range(n):
            if B[i][j]==1:
                
                if not leftDiag(B,i,j) or not rightDiag(B,i,j):
                    
                    inval=True
                    break
                
        if inval:
            break
    if not inval:
        show(B)
    
def show(B):
    for i in B:
        print(i)
    print()
    
    
def boards(l):
    if l==n:
        check(board)
        return
    for i in range(n):
        if board[i]==[0]*n :
            if not leftDiag(board,i,l) or not rightDiag(board,i,l):
                continue
            board[i][l]=1
            boards(l+1)
            board[i][l]=0
n=int(input('Enter board size n-'))
board=[[0]*n for i in range(n)]
print('Valid Boards:')
boards(0)


            
        
        
    


