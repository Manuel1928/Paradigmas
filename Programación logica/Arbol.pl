hombre(francisco).
hombre(adan).
hombre(david).
hombre(manuel).
hombre(osvaldo).
hombre(jesus).
hombre(lorenzo).

mujer(felicitas).
mujer(felix).
mujer(rosario).
mujer(mariana).
mujer(ines).
mujer(reyna).

progenitor(francisco,adan).
progenitor(rosario,adan).

progenitor(francisco,david).
progenitor(rosario,david).

progenitor(francisco,manuel).
progenitor(rosario,manuel).

progenitor(lorenzo,reyna).
progenitor(ines,reyna).
progenitor(lorenzo,osvaldo).
progenitor(ines,osvaldo).
progenitor(ines,rosario).
progenitor(lorenzo,rosario).
progenitor(lorenzo,felix).
progenitor(ines,felix).
progenitor(ines,mariana).
progenitor(lorenzo,mariana).

conyuge(francisco,rosario).
conyuge(felicitas,lorenzo).
conyuge(ines,jesus).

abuelo(X,Y):-progenitor(M,Y),progenitor(X,M),hombre(X).
abuela(X,Y):-progenitor(M,Y),progenitor(X,M),mujer(X).

hermano(X,Y):-progenitor(M,Y),progenitor(M,X),hombre(X).
hermana(X,Y):-progenitor(M,Y),progenitor(M,X),mujer(X).

tio(X,Y):-progenitor(M,Y),hermano(M,X).
tia(X,Y):-progenitor(M,Y),hermana(M,X).





