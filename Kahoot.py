import piot


def generar_nombre():
    first = random.choice(name)
    last = random.choice(surname)
    while first==last:
        first = random.choice(name)
        last = random.choice(surname)
    nombre = first+' '+last
    return nombre


if __name__ == "__main__":
    import sys, random
    name =  ('Petroleo', 'Hitler', 'Tommy', 'Dolores', 'Belen', 'Corona','Justiciero', 'Martillo', 'Delirio', 'El negro', 'El chino', 'Pornhub', 'Willy', 'Cigarro', 'María',
    'Vladimir', 'Bostezo', 'Parapléjico','Sara', 'Tyler', 'El Cid', 'Santiago', 'El otaku','El Gitano', 'Fibonazi')

    surname = ('Polla', 'Desgracias', 'Zipote', 'Delano', 'Negro', 'Virus', 'Okupa', 'Pañales', 'Rascaespaldas', 'Neumático', 'Empalme', 'Elnaci', 'Elpollas', 'Vergalarga',
    'Otako', 'Aceitoso', 'Mantequilla', 'Ascensores', 'Rex', 'Porritos', 'DuchasPocas', 'Petroleo', 'Toysarus', 'Machete', 'Porrinhio', 'Cerdo', 'Anal', 'Ceniceros'
    'Sinfuturos', 'RoncaMucho', 'Metralletas', 'Malamadre', 'Borrachín', 'Elswat', 'Espadachín', 'Rojeras', 'DePodemos', 'Abascal', 'Rosita', 'Lachupa')

    nombre = generar_nombre()

    anterior = open(r'nombre.txt','r+')
    for línea in anterior:
        if línea == nombre:
            generar_nombre
    print(nombre)
    anterior.write(nombre+'\n')
