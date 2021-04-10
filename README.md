# Tema1ASC-Marketplace
[Tema1 -Arhitectura Sistemelor de Calcul] Implementarea unui Marketplace pe baza problemei Multi Producer Multi Consumer.

Enunt: https://ocw.cs.pub.ro/courses/asc/teme/tema1 <br>
Schelet: https://bitbucket.org/ASC-admin/asc.git

#### ORGANIZARE

Tema contine fisierele consumer.py, producer.py si marketplace.py (In folderul 1-marketplace/tema). <br>
Aici se afla implementarea Marketplace-ului cu două tipuri de produse (ceai și cafea) ce vor fi
comercializate de către producători si achizitionate de consumatori. Acesta va fi intermediarul dintre producători și consumatori, prin el realizându-se achiziția de produse: producătorul (producer) va produce o anumită cantitate de produse de un anumit tip, cumpărătorul (consumer) va cumpăra o anumită cantitate de produse. De asemenea, Marketplace-ul va pune la dispoziția fiecărui cumpărător câte un coș de produse (cart) (acesta va fi folosit pentru rezervarea produselor care se doresc a fi cumpărate).
	
» Informatii despre testare se gasesc [aici](https://github.com/stefaniagherasie/Tema1ASC-Marketplace/tree/master/1-marketplace). <br>
» Informații despre conținutul fișierelor de intrare/ ieșire se regăsesc [aici](https://bitbucket.org/ASC-admin/asc/src/master/assignments/1-marketplace/skel/test-gen/README_TESTS.md).
<br>


#### IMPLEMENTARE

- Producatorul va produce intr-o bucla
infinita lista de produse de care dispune. Pentru fiecare element din lista, se obtine
produsul, cantitatea si timpul de asteptare. Se publica cantitatea de produse, tinand 
cont ca producatorul sa nu depaseasca limita de produse pe care pe poate avea in 
marketplace. Se da sleep dupa publicarea fiecarui produs pentru a simula timpul de 
asteptare pentru a face produsul.

- Consumatorul prelucreaza lista cu comenzi, verifica de ce tip este fiecare comanda(add 
sau remove), obtine produsul si cantitatea. Se adauga pe rand fiecare produs in codul
de cumparaturi, iar in cazul in care produsul nu a fost inca publicat de producatori, 
se reincearca la un interval de timp. Daca se doreste stergerea unui produs din cos, 
cererea e trimisa la marketplace si produsul e scos din cos si adaugat inapoi pe piata
pentru a fi disponibil altor consumatori. La final se executa comanda si se afiseaza
lista cu produse in formatul de output dorit.

- In Marketplace se retin in "prod_count" si "carts_count" cati producatori si cosuri sunt. Dictionarul
"products" retine produsele realizare de fiecare producator(cheia este id-ul producato-
rului, iar valoarea este lista de produse). In "carts" se retine in mod similar continutul 
cosurilor de cumparaturi (avand insa ca valoare o lista de tupluri de forma 
(produs, producator)).
	- Prin register_producer() si new_cart() se aloca un index producatorului/cosului. Aceste
sectiuni sunt protejate de un Lock pentru a evita probleme de concurenta.  
	- In "add_to_cart" se adauga produsul in cos si se sterge din lista 
producatorului, iar daca produsul nu exista inca in marketplace se returneaza False sa
semnaleze consumatorului sa incerce mai tarziu. 
	- In "remove_from_cart" se sterge produsul
din cos si acesta devine disponibil din nou pe piata. 
	- In "place_order" se obtine lista
de produse din cos.

#### Bibliografie

https://ocw.cs.pub.ro/courses/asc/laboratoare/02 <br>
https://ocw.cs.pub.ro/courses/asc/laboratoare/03


