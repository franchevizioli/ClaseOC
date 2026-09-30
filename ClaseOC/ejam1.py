notas=[8,9,1,1,2,3,6,6,7,8,10]
ap=[]
deap=[]
for nota in notas:
    if nota>=6:
        ap.append(nota)
    else:
        deap.append(nota)
print(ap)
print(deap)
