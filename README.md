# Library-management
Application developed using OOP principles:

-class Persoane inherited by the classes Membru and Bibliotecar  

-Members (Membru) can borrow (imprumuta) or return (returneaza) books

-Librarians (Bibliotecar) can search (cautacartea) for a book and check if they are available or not

-class Carte inherited by class CarteFizica. A book has a name, an author, a location in the library, a publishing house and a status

-class Notificare - 2 methods. The method trimite_notif is used to connect to a locally configured SMTP server on the personal machine

-A notification is sent if a book is not returned on time. A message will appear in the terminal
