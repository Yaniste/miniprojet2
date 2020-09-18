def somme(n : int) -> int:
    """ fonction qui retourne la somme des termes 
    Pré : n est un entier
    Post : somme est un entier"""
    assert type(n)==int, "l'argument doit être un entier"
    assert n>0, "n doit être supérieur à 0"
    somme=0
    for i in range(n+1):
        somme+=i
    return somme

print(somme(2))

def fact(n:int)->int:
    assert type(n)==int, "l'argument doit être un entier"
    assert n>=0, "n doit être supérieur ou égal à 0"
    if n==0:
        return 1
    if n>0:
        return n*fact(n-1)
    
print(fact(8))

def factit(n:int)->int:
    assert type(n)==int, "l'argument doit être un entier"
    assert n>=0, "n doit être supérieur ou égal à 0"
    s=1
    for i in range(1, n+1):
        s=s*i
    return s

print(factit(0))

def boucle(i:int, k:int)->int:
    assert type(i)==int, "l'argument doit être un entier"
    assert type(k)==int, "l'argument doit être un entier"
    assert i>=0, "i doit être supérieur ou égal à 0"
    if i==k:
        print(i)
    else:
        print(i, end=" ")
        boucle(i+1,k)
    
boucle(0,3)

def algo(x:int, y:int)->int:
    if x <= 0:
        return 0
    elif x % 2 == 0:
        return algo(x//2, y+y)
    else:
        return algo(x//2, y+y) + y
    
print(algo(105,253))

def lapin(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return lapin(n-1)+lapin(n-2)
    
print(lapin(7))

def fibo(n):
    f0=0
    f1=1
    result=0
    for i in range(2,n+1):
        result=f0+f1
        f0=f1
        f1=result
    return result

print(fibo(7))