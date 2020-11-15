class state():
    
    def __init__(ob,a=[]):
        ob.a=a
        ob.U=None;ob.D=None;ob.L=None;ob.R=None

    def crU(ob):
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
            tsT.addF(n)

    def crD(ob):
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
            tsT.addF(n)

    def crL(ob):
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
            tsT.addF(n)

    def crR(ob):
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
            tsT.addF(n)
        
            

    
    
class trav():
    tr=[]
    def __init__(ob):
        pass
    
    def ispresent(ob,a):
        return a in trav.tr
    
    def add(ob,a):
        if not ob.ispresent(a):
            trav.tr.append(a)
            return(True)
        return(False)

class Front():
    fr=[]
    def __init__(ob):
        pass
    
    def addF(ob,n):
        Front.fr.append(n)
        
    def remF(ob):
        a=Front.fr
        T=a[::-1]
        x=T.pop()
        Front.fr=T[::-1]
        
