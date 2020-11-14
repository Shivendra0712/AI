import random as rnd
board=[[0]*4 for i in range(4)]
pl=True
def boardshow():
    for i in board:
        print(i)
    print()

def play():
    a=input(); option=['L','R','U','D','l','r','u','d']
    if option.index(a)%4==0:
        left()
    elif option.index(a)%4==1:
        right()
    elif option.index(a)%4==2:
        up()
    elif option.index(a)%4==3:
        down()


def prod(B):
    s=0
    for i in B:
        p=1
        for j in i:
            if j!=0:
                p*=j
        s+=p
    return s

def heuClose(B):
    Hr=0
    for i in range(4):
        R=[j for j in range(4) if B[i][j]!=0]
        for j in range(len(R)-1):
            if B[i][R[j]]==B[i][R[j+1]]:
                j+=1
                Hr+=2*B[i][R[j]]
    Hc=0
    for j in range(4):
        C=[i for i in range(4) if B[i][j]!=0]
        for i in range(len(C)-1):
            if B[C[i]][j]==B[C[i+1]][j]:
                i+=1
                Hc+=2*B[C[i]][j]
    return Hc+Hr

def sumBoard(B):
    s=0
    for i in B:
        for j in i:
            s+=j**2
    return s



def randomfill():
    playable=False
    global pl
    for i in board:
        for j in i:
            if j==0:
                playable=True
                break
        
    if not playable:
        print("The Game's Over")
        pl=False
        return
    
    t=rnd.randint(2,4)
    while(t==3):
        t=rnd.randint(2,4)
    i=rnd.randrange(4);j=rnd.randrange(4)
    while board[i][j]!=0:
        i=rnd.randrange(4);j=rnd.randrange(4)
    board[i][j]=t
    
    boardshow()
    
    playGreedy()

def playGreedy():
    global board
    L=[list(i) for i in board]
    left(L)
    R=[list(i) for i in board]
    right(R)
    U=[list(i) for i in board]
    up(U)
    D=[list(i) for i in board]
    down(D)
    Ar=[L,R,U,D];w1=1;w2=1;w3=0
    m=0
    for i in Ar:
        v=w1*heuClose(i)+w2*sumBoard(i)+w3*prod(i)
        if m<v:
            board=i;m=v
    step=['left','right','up','down']
    print(step[Ar.index(board)],m)



                
def left(B=board):
    #print('left')
    for i in range(4):
        In=[j for j in range(4) if B[i][j]!=0]
        for k in range(len(In)-1):
            if B[i][In[k]]==B[i][In[k+1]]:
                B[i][In[k]]=2*B[i][In[k]]
                B[i][In[k+1]]=0
        
        

    for i in range(4):
        j=1
        while j<4:
            while B[i][j-1]==0 and B[i][j]!=0:
                B[i][j-1]=B[i][j]
                B[i][j]=0
                if j>=2:
                    j-=1
            j+=1
    #boardshow()
def right(B=board):
    #print('right')
    for i in range(4):
        In=[j for j in range(4) if B[i][j]!=0]
        for k in range(len(In)-1,0,-1):
            if B[i][In[k]]==B[i][In[k-1]]:
                B[i][In[k]]=B[i][In[k]]*2
                B[i][In[k-1]]=0

    for i in range(4):
        j=2
        while j>-1:
            while B[i][j+1]==0 and B[i][j]!=0:
                B[i][j+1]=B[i][j]
                B[i][j]=0
                if j<2:
                    j+=1
            j-=1
def up(B=board):
    #print('up')
    for j in range(4):
        In=[i for i in range(4) if B[i][j]!=0]
        for k in range(len(In)-1):
            if B[In[k]][j]==B[In[k+1]][j]:
                B[In[k]][j]=B[In[k]][j]*2
                B[In[k+1]][j]=0
    for j in range(4):
        i=1
        while i<4:
            while B[i-1][j]==0 and B[i][j]!=0:
                B[i-1][j]=B[i][j]
                B[i][j]=0
                if i>=2:
                      i-=1
            i+=1
def down(B=board):
    #print('down')
    for j in range(4):
        In=[i for i in range(4) if B[i][j]!=0]
        for k in range(len(In)-1,0,-1):
            if B[In[k]][j]==B[In[k-1]][j]:
                B[In[k]][j]=B[In[k]][j]*2
                B[In[k-1]][j]=0
    for j in range(4):
        i=2
        while i>-1:
            while B[i+1][j]==0 and B[i][j]!=0:
                B[i+1][j]=B[i][j]
                B[i][j]=0
                if i<2:
                    i+=1
            i-=1

for i in range(500):  #here we take the max expanding depth of 500
    print('trial',i+1)
    if not pl:
        break
    randomfill()
