class state():
    
    def __init__(ob,a=[]):
        ob.a=a
        ob.U=None;ob.D=None;ob.L=None;ob.R=None

    def crU(ob,X):
        n=state()
        ar=[i for i in ob.a]
        if ar.index(0) in range(3):
            return
        x=ar.index(0)
        ar[x],ar[x-3]=ar[x-3],ar[x]
        n.a=ar
        Tst=trav();tsT=Front()
        if Tst.add(n.a):
            ob.U=n
            tsT.addF(n,X)

    def crD(ob,X):
        n=state()
        ar=[i for i in ob.a]
        if ar.index(0) in range(6,9):
            return
        x=ar.index(0)
        ar[x],ar[x+3]=ar[x+3],ar[x]
        n.a=ar
        Tst=trav();tsT=Front()
        if Tst.add(n.a):
            ob.D=n
            tsT.addF(n,X)

    def crL(ob,X):
        n=state()
        ar=[i for i in ob.a]
        if ar.index(0)%3==0:
            return
        x=ar.index(0)
        ar[x],ar[x-1]=ar[x-1],ar[x]
        n.a=ar
        Tst=trav();tsT=Front()
        if Tst.add(n.a):
            ob.L=n
            tsT.addF(n,X)

    def crR(ob,X):
        n=state()
        ar=[i for i in ob.a]
        if (ar.index(0)+1) %3==0:
            return
        x=ar.index(0)
        ar[x],ar[x+1]=ar[x+1],ar[x]
        n.a=ar
        Tst=trav();tsT=Front()
        if Tst.add(n.a):
            ob.R=n
            tsT.addF(n,X)
        
            

    
    
class trav():
    tr=set()
    def __init__(ob):
        pass
    
    def ispresent(ob,a):
        return tuple(a) in trav.tr
    
    def add(ob,a):
        if not ob.ispresent(tuple(a)):
            trav.tr.add(tuple(a))
            return(True)
        return(False)

class Front():
    fr=[]
    def __init__(ob):
        pass

    def heu(ob,a):
        h=0
        l=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        for i,I in enumerate(a):
            
            if I==0:
                continue
            x=i%3;y=i//3
            Y,X=l[I]
            h+=abs(X-x)+abs(Y-y)
        return h
            
    
    def addF(ob,n,X=0):
        t=tuple([n,X+ob.heu(n.a)])
        Front.fr.append(t); i=len(Front.fr)-2
        while Front.fr[i][1]>t[1]:
            Front.fr[i+1]=Front.fr[i];i-=1
            if i<0:
                break
        Front.fr[i+1]=t
        
    def remF(ob):
        a=Front.fr
        T=a[::-1]
        x=T.pop()
        Front.fr=T[::-1]
        
