import mod3 as m

def path(d,g):
    try:
        val=d[g]
    except:
        return ''
    
    s=''
    if val.U==g:
        s='UP'
    elif val.D==g:
        s='DOWN'
    elif val.L==g:
        s='LEFT'
    else :
        s='RIGHT'
    return(path(d,val)+'->'+s)
sol=''
def calc(a):
    global sol
    a=[int(x) for x in a]
    st=m.state(a)

    f=m.Front()
    f.addF(st)
    
    dic={};dic2={m.Front.fr[0][0]:0}
    while(len(m.Front.fr)>0):
        curr=m.Front.fr[0][0]
        h=m.Front.fr[0][1]
        print(curr.a,c,'Heuristic=',h,'path cost=',dic2[curr])
        f.remF()
        if curr.a==list(range(9)):  #goal Test
            sol=path(dic,curr)
            break
        
    
        curr.crU(dic2[curr]+1)   #creating checking and adding UpperNode
        dic[curr.U]=curr; dic2[curr.U]=dic2[curr]+1
        curr.crD(dic2[curr]+1)   #same as above..
        dic[curr.D]=curr; dic2[curr.D]=dic2[curr]+1
        curr.crL(dic2[curr]+1)
        dic[curr.L]=curr; dic2[curr.L]=dic2[curr]+1
        curr.crR(dic2[curr]+1)
        dic[curr.R]=curr; dic2[curr.R]=dic2[curr]+1
    
    
