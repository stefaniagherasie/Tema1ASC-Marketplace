Tema 1 ASC - Marketplace
Gherasie Stefania-Elena, grupa 333CB

ORGANIZARE

Tema contine fisierele product.py, consumer.py, producer.py si marketplace.py, unde se
afla implementarea Marketplace-ului cu două tipuri de produse (ceai și cafea) ce vor fi
comercializate de către producători si achizitionate de consumatori.

Consideri ca tema este utila?
	Tema a fost utila deoarece am reusit sa implementez un Multiple Producer Multiple 
	Consumer mai interesant si complex
Consideri implementarea naivă, eficientă, se putea mai bine?
	Imlementarea nu este foarte eficienta, dar nici naiva. Puteam sa implementez mai 
	eficient gasirea produselor la adaugarea lor in cos.


IMPLEMENTARE

Am implementat tot enuntul temei. In producer.py producatorul va produce intr-o bucla
infinita lista de produse de care dispune. Pentru fiecare element din lista, se obtine
produsul, cantitatea si timpul de asteptare. Se publica cantitatea de produse, tinand 
cont ca producatorul sa nu depaseasca limita de produse pe care pe poate avea in 
marketplace. Se da sleep dupa publicarea fiecarui produs pentru a simula timpul de 
asteptare pentru a face produsul.

Consumatorul prelucreaza lista cu comenzi, verifica de ce tip este fiecare comanda(add 
sau remove), obtine produsul si cantitatea. Se adauga pe rand fiecare produs in codul
de cumparaturi, iar in cazul in care produsul nu a fost inca publicat de producatori, 
se reincearca la un interval de timp. Daca se doreste stergerea unui produs din cos, 
cererea e trimisa la marketplace si produsul e scos din cos si adaugat inapoi pe piata
pentru a fi disponibil altor consumatori. La final se executa comanda si se afiseaza
lista cu produse in formatul de output dorit.

In Marketplace se retin in "prod_count" si "carts_count" cati producatori si cosuri sunt.
Prin register_producer() si new_cart() se aloca un index producatorului/cosului. Aceste
sectiuni sunt protejate de un Lock pentru a evita probleme de concurenta. Dictionarul
"products" retine produsele realizare de fiecare producator(cheia este id-ul producato-
rului, iar valoarea este lista de produse). In "carts" se retine in mod similar continutul 
cosurilor de cumparaturi (avand insa ca valoare o lista de tupluri de forma 
(produs, producator)). In "add_to_cart" se adauga produsul in cos si se sterge din lista 
producatorului, iar daca produsul nu exista inca in marketplace se returneaza False sa
semnaleze consumatorului sa incerce mai tarziu. In "remove_from_cart" se sterge produsul
din cos si acesta devine disponibil din nou pe piata. In "place_order" se obtine lista
de produse din cos.

BIBLIOGRAFIE

https://ocw.cs.pub.ro/courses/asc/laboratoare/02
https://ocw.cs.pub.ro/courses/asc/laboratoare/03

Git: https://github.com/stefaniagherasie/Tema1ASC-Marketplace.git
