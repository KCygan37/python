# lista = [[7,5,11],[8,12,6],[1,2,3]]


# def znajd_max(lista):
#     m = lista[0][0]
#     for i in range(len(lista)):
#         for j in range(len(lista[i])):
#             if m < lista[i][j]:
#                 m = lista[i][j]
#     return m

# print(znajd_max(lista))


# lista = [1,2,3,4,5,6,7,8,9,10]

# for i in range(len(lista)):
#     dod = int(input('Podaj liczbę'))
#     lista[i] = [lista[i],dod]
# print(lista)



# lista = [[7,5,11],[8,12,6],[1,2,3]]

# def oblicz_sume(lista):
#     m = 0
#     for i in range(len(lista)):
#         for j in range(len(lista[i])):
#             m += lista[i][j]
#     return m

# print(oblicz_sume(lista))



# dziennik = {
#     'matma':[2,3,4],
#     'polski':[1,5,3]
# }

# oceny = dziennik['matma']
# srednia_matma = sum(oceny) / len(oceny)

# oceny = dziennik['polski']
# srednia_polski = sum(oceny) / len(oceny)

# srednia_sem = (srednia_polski+srednia_matma)/2
# print(f'Średnia z matmy to: {srednia_matma}, Średnia z polskiego to: {srednia_polski}, Średnia semestralana to: {srednia_sem}')



import random

##WAŻNE
# n = int(input('Podaj n: '))
# m = int(input('Podaj m: '))

# lista = []
# for i in range(n):
#     lista.append([])
#     for j in range(m):
#         lista[i].append(random.randint(0,100))

# print(lista)


# lista = []
# for i in range(100):
#     lista.append(random.randint(0,10))
# slownik = {}
# for i in range(11):
#     suma = 0
#     for a in lista:
#         if i == a:
#             suma += 1
#     slownik[i] = suma
# print(slownik)


# lista = []
# for i in range(1000):
#     lista.append(random.randint(0,1000))
# slownik = {}
# juz_bylo = []
# for b in lista:
#     if b in juz_bylo:
#         continue
#     suma = 0
#     for a in lista:
#         if b == a:
#             suma += 1
#     slownik[b] = suma
#     juz_bylo.append(b)
# print(slownik)


# #1 1 2 2 3 4 4 4 4 5

# lista = []
# for i in range(1000):
#     lista.append(random.randint(0,1000))
#     lista.sort()
# slownik = {}
# courrent = -1
# suma = 0
# for b in lista:
#     if b == courrent:
#         suma+=1
#     else:
#         if courrent != -1:
#             slownik[courrent] = suma
#         courrent = b
#         suma = 1

# print(slownik)



# slownik = {}

# for i in range(0,10):
#     slownik[i] = i*i
# print(slownik)



# slownik = {'polska':'warszawa', 'niemcy':'berlin'}

# kraj = input('Podaj kraj: ')
# print(f'Stoilicą {kraj} to {slownik[kraj]}')



# lista = [1,2,3,4,5,6,7,8,9,0]

# print(f'Maksymalna wartośc to: {max(lista)}, minimalna to: {min(lista)}, śerdnai wartość to: {sum(lista)/len(lista)}')



# for i in range(0,7):
#     print(f'| {i} | {random.random()} |')



#to samow tym ze słókami - 16
# slownik = {'masło':5, 'szynka':2,}

# while True:
#     prod = input('podaj prdukt: ')
#     if prod == 'x':
#         break
#     cena = int(input('podaj cene w zł: '))
#     slownik[prod] = cena
# suma = 0
# for i in slownik:
#     suma+= slownik[i]
# print(suma)



# #ZRÓB TRUDNIEJSZA!!
# slownik = {1:'I', 5:"V", 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

# liczba = int(input('Podaj liczbę: '))
# print(f'Liczba to: {liczba}, liczba w zapisie rzymskim to: {slownik[liczba]}')



# l = [1,2,1,3,3,4]
# print(list(set(l)))


# set1={1,2,3}
# set2={4,5,6}
# set3=set1.union(set2)
# print(set3)


# l1=[1,2,3]
# l2=[4,5,6]
# set1=set(l1)
# set2=set(l2)
# set3=set1.union(set2)
# print(list(set3))

# l1=[1,2,3]
# l2=[4,5,6]
# l1.append(l2)
# print(l1)

# l1=[1,2,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)

