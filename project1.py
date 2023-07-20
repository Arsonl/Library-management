import smtplib
from datetime import datetime , timedelta

class Persoane:
    def __int__(self,nume,prenume,varsta):
        self.nume=nume
        self.prenume=prenume
        self.varsta=varsta


class Membru(Persoane):
    def __init__(self,nume,prenume,varsta,idmembru,nr_carti):
        super().__init__ ()
        self.idmembru=idmembru
        self.nr_carti=nr_carti


    def imprumuta(self,carte_fizica):
        self.nr_carti.append(carte_fizica)
        carte_fizica.data_retur +=timedelta(weeks=4)


    def returneaza(self,carte_fizica):
        self.nr_carti.remove(carte_fizica)
        carte_fizica.data_retur = datetime.now()


class Bibliotecar(Persoane):
    def __init__(self,nume,prenume,varsta,data_angajare):
        super().__init__()
        self.data_angajare=data_angajare

    def cautacartea(self,carte_fizica):
        if carte_fizica.status == "neimprumutata":
            print("Cartea " +  carte_fizica.titlu + " scrisa de " + carte_fizica.autor + " este disponibila")
            return True
        else:
            print("Cartea " + carte_fizica.titlu + " scrisa de " + carte_fizica.autor + " este indisponibila")
            return False

class Carte:
    def __init__(self,titlu,autor):
        self.titlu=titlu
        self.autor=autor

class CarteFizica(Carte):
    def __init__(self,titlu,autor,locatie,status,editura):
        super().__init__(titlu,autor)
        self.locatie=locatie
        self.status=status
        self.editura=editura
        self.data_retur=datetime.now()


class Notificare:
    def __init__(self,adresa_from,adresa_to,subiect,text_email):
        self.adresa_from=adresa_from
        self.adresa_to=adresa_to
        self.subiect=subiect
        self.text_email=text_email

    def trimite_notif(self):
       import smtplib

       mesaj = """ Subiect: %s
           Mesaj: %s
       """ % (self.subiect, self.text_email)

       server=smtplib.SMTP('localhost',5555)


       server.sendmail(self.adresa_from,self.adresa_to,mesaj)

       server.quit()


if __name__ == '__main__':
    carte_fizica = CarteFizica("Baltagul ", "Mihail Sadoveanu ", "Raft 5", "neimprumutata", "Litera")

    membru = Membru("Mosteanu", "Radu", "23", "100", [])

    bibliotecar= Bibliotecar("Ionescu", "Ion", "35", datetime(2020,10,25))

    if bibliotecar.cautacartea(carte_fizica):
        membru.imprumuta(carte_fizica)

        if carte_fizica.data_retur > datetime.now() - timedelta(weeks=5):

            notificare = Notificare("radu.mosteanu@gmail.com", "radu.mosteanu@gmail.com", "ALERTA ",
                                    "RETURNEAZA CARTEA " + carte_fizica.titlu + "DE " + carte_fizica.autor )

            notificare.trimite_notif()


