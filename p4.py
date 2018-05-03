def añadir(object, collection= []):
    if collection is None:
        collection = []
    collection.append(object)
    f = open('nombres.txt', 'a')
    f.write(name+ '\n')
    f.close()
    return collection

listanombres = ['Guillermo', 'Charlotte']
name = input('Dime tu nombre: ').replace(',', ' ').replace('?', ' ').replace('¿', ' ').replace('.', ' ')
usuario = name.split()
comun = set (usuario) & set(listanombres)
if len(comun) == 0:
    añadir (name, listanombres)
    comun = set (usuario) & set(listanombres)
    for x in comun:
        print ('No me suena tu nombre, %s.' % x)
elif len(comun) == 1:        
    for x in comun:
        print ('Hola, %s. ¿Qué tal?' % x)
for x in comun:
    print('Vamos a jugar a un juego, %s.' % x)
