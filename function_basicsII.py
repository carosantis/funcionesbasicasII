
def hoy (num, b):
    print (num,b)
    lalista.append (b)
    for b in num:
        b=b-1
        print (b)
        lalista.append(b)
        if b==0:
            break
    return num

lalista=[]
a=hoy(lalista,10)
print(a)

def imprimir_devolver (a,b):
    print(a)
    return b
a=imprimir_devolver(1,2)
print(a)

def maslongitud ():
    x=(len(listita))+(listita[1])
    return x
listita=[1,2,3,4,5]
a=maslongitud()
print(a)

def mayorS (lista):
    if len(lista)>1:
        listaM=[]
        for x in lista:
            if x> lista[1]:
                listaM.append(x)
        print(len(listaM))
        return listaM
    else:
        return False

a= mayorS ([5,2,3,2,1,4])
b = mayorS ([9])
print(a)
print(b)

def estalong(a,b):
    lista= []
    lista.append(b)
    return a*lista

print(estalong(4,7))
print(estalong(6,2))