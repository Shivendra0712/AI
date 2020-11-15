import mod1 as m

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
a=list(map(int,input().split()))
st=m.state(a)

f=m.Front()
f.addF(st)
ar=[];c=0
dic={}
while(len(m.Front.fr)>0):
    curr=m.Front.fr[0]
    print(curr.a,c)
    f.remF()
    if curr.a==list(range(9)):  #goal Test
        print(path(dic,curr))
        print('Solution Found after expanding ',len(ar),' nodes')
        break
    ar.append(curr);c+=1
    curr.crU()   #creating checking and adding UpperNode
    dic[curr.U]=curr
    curr.crD()   #same as above..
    dic[curr.D]=curr
    curr.crL()
    dic[curr.L]=curr
    curr.crR()
    dic[curr.R]=curr
    
    
