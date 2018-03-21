from django.db import models

class Alternant(models.Model):

    NATIONALITE = (
        (1,"Française"),
        (2,"Union Européenne"),
        (3,"Etranger hors Union Européenne"),
    )

    REGIMESOCIAL = (
        (1,"MSA"),
        (2,"URSSAF"),
    )

    SITUATIONAVANTCONTRAT = (
        (1,"Scolaire (hors DIMA)"),
        (2,"Dispositif d’initiation aux métiers en alternance (DIMA) ou autre classe préparatoire à l’apprentissage (CLIPA, CPA...)"),
        (3,"Etudiant"),
        (4,"Contrat d’apprentissage"),
        (5,"Contrat de professionnalisation"),
        (6,"Contrat aidé"),
        (7,"Stagiaire de la formation professionnelle"),
        (8,"Salarié"),
        (9,"Personne à la recherche d’un emploi (inscrite ou non au Pôle Emploi)"),
        (10,"Inactif"),
    )

    DIPLOME = (
        (10,"Doctorat"),
        (11,"Master professionnel/DESS/diplôme grande école"),
        (12,"Master recherche/DEA"),
        (19,"Autre diplôme ou titre de niveau bac+5 ou plus"),
        (21,"Master professionnel (M1+M2 ou seul M2)"),
        (22,"Master général (M1+M2 ou seul M2)"),
        (23,"Licence professionnelle"),
        (24,"Licence générale"),
        (29,"Autre diplôme ou titre de niveau bac +3 ou 4"),
        (31,"Brevet de Technicien Supérieur"),
        (32,"Diplôme Universitaire de technologie"),
        (39,"Autre diplôme ou titre de niveau bac+2"),
        (41,"Baccalauréat professionnel"),
        (42,"Baccalauréat général"),
        (43,"Baccalauréat technologique"),
        (49,"Autre diplôme ou titre de niveau bac"),
        (51,"CAP"),
        (52,"BEP"),
        (53,"Mention complémentaire"),
        (59,"Autre diplôme ou titre de niveau CAP/BEP"),
        (60,"Aucun diplôme ni titre professionnel"),
    )

    DERNIEREANNEESUIVIE = (
        (1,"l’apprenti a suivi la dernière année du cycle de formation et a obtenu le diplôme ou titre"),
        (11,"l’apprenti a suivi la 1ère année du cycle et l’a validée (examens réussis mais année non diplômante)"),
        (12,"l’apprenti a suivi la 1ère année du cycle mais ne l’a pas validée (échec aux examens, interruption ou abandon de formation)"),
        (21,"l’apprenti a suivi la 2è année du cycle et l’a validée (examens réussis mais année non diplômante)"),
        (22,"l’apprenti a suivi la 2è année du cycle mais ne l’a pas validée (échec aux examens, interruption ou abandon de formation)"),
        (31,"l’apprenti a suivi la 3è année du cycle et l’a validée (examens réussis mais année non diplômante, cycle adapté)"),
        (32,"l’apprenti a suivi la 3è année du cycle mais ne l’a pas validée (échec aux examens, interruption ou abandon de formation)"),
        (40,"l’apprenti a achevé le 1er cycle de l’enseignement secondaire (collège)"),
        (41,"l’apprenti a interrompu ses études en classe de 3è"),
        (42,"l’apprenti a interrompu ses études en classe de 4è"),
    )

    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=70)
    prenom=models.CharField(max_length=35)
    sexe=models.CharField(max_length=1)
    datenaissance=models.DateField()
    numerodepartementnaissance=models.CharField(max_length=3)
    codeINSEEcommuneNaissance=models.CharField(max_length=5)
    adresse1=models.CharField(max_length=100)
    adresse2=models.CharField(max_length=100)
    codepostal=models.CharField(max_length=5)
    ville=models.CharField(max_length=60)
    telephone=models.CharField(max_length=15)
    handicape=models.BooleanField(default=False)
    courriel=models.CharField(max_length=40)
    nationalite=models.PositiveSmallIntegerField(choices=NATIONALITE)
    regimesocial=models.PositiveSmallIntegerField(choices=REGIMESOCIAL)
    situationavantcontrat=models.PositiveSmallIntegerField(choices=SITUATIONAVANTCONTRAT)
    dernierdiplomeprepare=models.PositiveSmallIntegerField(choices=DIPLOME)
    derniereanneesuivie=models.PositiveSmallIntegerField(choices=DERNIEREANNEESUIVIE)
    intituledernierdiplomeprepare=models.CharField(max_length=100)
    diplomelepluseleve=models.PositiveSmallIntegerField(choices=DIPLOME)
    nomrepresentant=models.CharField(max_length=70)
    prenomrepresentant=models.CharField(max_length=35)
    adresse1representant=models.CharField(max_length=100)
    adresse2representant=models.CharField(max_length=100)
    codepostalrepresentant=models.CharField(max_length=5)
    villerepresentant=models.CharField(max_length=60)

    def __str__(self):
        return self.nom + " " + self.prenom

class Entreprise(models.Model):

    TYPEEMPLOYEUR = (
        (11,"Entreprise inscrite au répertoire des métiers ou au registre des entreprises pour l’Alsace-Moselle"),
        (12,"Entreprise inscrite uniquement au registre du commerce et des sociétés"),
        (13,"Entreprises dont les salariés relèvent de la mutualité sociale agricole"),
        (14,"Profession libérale"),
        (15,"Association"),
        (16,"Autre employeur privé"),
        (21,"Service de l’Etat (administrations centrales et leurs services déconcentrés de la fonction publique d’Etat)"),
        (22,"Commune"),
        (23,"Département"),
        (24,"Région"),
        (25,"Etablissement public hospitalier"),
        (26,"Etablissement public local d’enseignement"),
        (27,"Etablissement public administratif de l’Etat"),
        (28,"Etablissement public administratif local (y compris établissement public de coopération intercommunale EPCI)"),
        (29,"Autre employeur public"),
    )

    EMPLOYEURSPECIFIQUE = (
        (1,"Entreprise de travail temporaire"),
        (2,"Groupement d’employeurs"),
        (3,"Employeur saisonnier"),
        (4,"Apprentissage familial : l’employeur est un ascendant de l’apprenti"),
        (0,"Aucun de ces cas"),
    )

    id=models.AutoField(primary_key=True)
    raisonsociale = models.CharField(max_length=70)
    numeroSIRET = models.CharField(max_length=14)
    adresse1=models.CharField(max_length=100)
    adresse2=models.CharField(max_length=100)
    codepostal=models.CharField(max_length=5)
    ville=models.CharField(max_length=70)
    typeemployeur=models.PositiveSmallIntegerField(choices=TYPEEMPLOYEUR)
    employeurspecifique=models.PositiveSmallIntegerField(choices=EMPLOYEURSPECIFIQUE)
    codeAPE=models.CharField(max_length=5)
    effectifentreprise=models.PositiveSmallIntegerField()
    telephone=models.CharField(max_length=15)
    telecopie=models.CharField(max_length=15)
    courriel=models.CharField(max_length=40)
    codeconventioncollective=models.CharField(max_length=4)
    libelleconventioncollective=models.CharField(max_length=200)
    adhesionregimeassurancechomage=models.BooleanField(default=False)

    def __str__(self):
        return self.raisonsociale

class Personnel(models.Model):
    id=models.AutoField(primary_key=True)
    entreprise=models.ForeignKey(Entreprise,on_delete=models.CASCADE)
    role=models.CharField(max_length=25)
    civilite=models.CharField(max_length=12)
    nom=models.CharField(max_length=70)
    prenom=models.CharField(max_length=35)
    datenaissance=models.DateField()

    def __str__(self):
        return self.nom + " " + self.prenom

class CFA(models.Model):
    numeroUAI=models.CharField(max_length=8,primary_key=True)
    nom = models.CharField(max_length=70)
    adresse1=models.CharField(max_length=100)
    adresse2=models.CharField(max_length=100)
    codepostal=models.CharField(max_length=5)
    ville=models.CharField(max_length=60)

    def __str__(self):
        return self.nom

class Formation(models.Model):

    DIPLOME = (
        (10,"Doctorat"),
        (11,"Master professionnel/DESS/diplôme grande école"),
        (12,"Master recherche/DEA"),
        (19,"Autre diplôme ou titre de niveau bac+5 ou plus"),
        (21,"Master professionnel (M1+M2 ou seul M2)"),
        (22,"Master général (M1+M2 ou seul M2)"),
        (23,"Licence professionnelle"),
        (24,"Licence générale"),
        (29,"Autre diplôme ou titre de niveau bac +3 ou 4"),
        (31,"Brevet de Technicien Supérieur"),
        (32,"Diplôme Universitaire de technologie"),
        (39,"Autre diplôme ou titre de niveau bac+2"),
        (41,"Baccalauréat professionnel"),
        (42,"Baccalauréat général"),
        (43,"Baccalauréat technologique"),
        (49,"Autre diplôme ou titre de niveau bac"),
        (51,"CAP"),
        (52,"BEP"),
        (53,"Mention complémentaire"),
        (59,"Autre diplôme ou titre de niveau CAP/BEP"),
        (60,"Aucun diplôme ni titre professionnel"),
    )

    numeroUAI=models.CharField(max_length=8,primary_key=True)
    cfa=models.ForeignKey(CFA,on_delete=models.CASCADE)
    diplome=models.PositiveSmallIntegerField(choices=DIPLOME)
    intitule=models.CharField(max_length=100)
    codediplome=models.CharField(max_length=8)
    an1du=models.DateTimeField()
    an1au=models.DateTimeField()
    heuresan1=models.PositiveSmallIntegerField()
    an2du=models.DateTimeField()
    an2au=models.DateTimeField()
    heuresan2=models.PositiveSmallIntegerField()
    an3du=models.DateTimeField()
    an3au=models.DateTimeField()
    heuresan3=models.PositiveSmallIntegerField()
    niveau=models.PositiveSmallIntegerField()
    duree=models.PositiveSmallIntegerField()
    inpectionpedagogiquecompetente=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.intitule

class Contrat(models.Model):

    MODECONTRACTUEL = (
        (1,"à durée limitée"),
        (2,"dans le cade d'un CDI"),
        (3,"entreprise de travail temporaire"),
        (4,"activités saisonnières à deux employeurs"),
    )

    TYPECONTRATAVENANT = (
        (11,"Premier contrat d’apprentissage de l’apprenti"),
        (21,"Renouvellement de contrat chez le même employeur"),
        (22,"Contrat avec un apprenti qui a terminé son précédent contrat auprès d’un autre employeur"),
        (23,"Contrat avec un apprenti dont le précédent contrat auprès d’un autre employeur a été rompu"),
        (31,"Modification de la situation juridique de l’employeur"),
        (32,"Changement d’employeur dans le cadre d’un contrat saisonnier"),
        (33,"Prolongation du contrat suite à un échec à l’examen de l’apprenti"),
        (34,"Prolongation du contrat suite à la reconnaissance de l’apprenti comme travailleur handicapé"),
        (35,"Modification du diplôme préparé par l’apprenti"),
        (36,"Autres changements : changement de maître d’apprentissage, de durée de travail hebdomadaire, etc ..."),
    )

    TYPEDEROGATION = (
        (11,"Age de l’apprenti inférieur à 16 ans"),
        (12,"Age supérieur à 25 ans : cas spécifiques prévus dans le code du travail"),
        (21,"Réduction de la durée du contrat ou de la période d’apprentissage"),
        (22,"Allongement  de la durée du contrat ou de la période d’apprentissage"),
        (31,"Début de l’apprentissage hors période légale (plus de 3 mois avant ou après la date de début du cycle de formation)"),
        (40,"Troisième contrat pour une formation de même niveau"),
        (50,"Cumul de dérogations"),
        (60,"Autre dérogation"),
    )

    id=models.AutoField(primary_key=True)
    modecontractuel=models.PositiveSmallIntegerField(choices=MODECONTRACTUEL)
    alternant=models.ForeignKey(Alternant, on_delete=models.CASCADE)
    entreprise=models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    formation=models.ForeignKey(Formation, on_delete=models.CASCADE)
    mission=models.TextField()
    typecontratavenant=models.PositiveSmallIntegerField(choices=TYPECONTRATAVENANT)
    dateinscription=models.DateField()
    typederogation=models.PositiveSmallIntegerField(choices=TYPEDEROGATION)
    numerocontratanterieur=models.CharField(max_length=20)
    dateembauche=models.DateField()
    dateexecution=models.DateField()
    dateeffetavenant=models.DateField()
    datefincontrat=models.DateField()
    dureehebdomadairetravail=models.DurationField()
    risquesparticuliers=models.BooleanField(default=False)
    an1per1du=models.DateTimeField()
    an1per1au=models.DateTimeField()
    an1per1taux=models.FloatField()
    an1per1base=models.CharField(max_length=4)
    an1per2du=models.DateTimeField()
    an1per2au=models.DateTimeField()
    an1per2taux=models.FloatField()
    an1per2base=models.CharField(max_length=4)
    an2per1du=models.DateTimeField()
    an2per1au=models.DateTimeField()
    an2per1taux=models.FloatField()
    an2per1base=models.CharField(max_length=4)
    an2per2du=models.DateTimeField()
    an2per2au=models.DateTimeField()
    an2per2taux=models.FloatField()
    an2per2base=models.CharField(max_length=4)
    an3per1du=models.DateTimeField()
    an3per1au=models.DateTimeField()
    an3per1taux=models.FloatField()
    an3per1base=models.CharField(max_length=4)
    an3per2du=models.DateTimeField()
    an3per2au=models.DateTimeField()
    an3per2taux=models.FloatField()
    an3per2base=models.CharField(max_length=4)
    an4per1du=models.DateTimeField()
    an4per1au=models.DateTimeField()
    an4per1taux=models.FloatField()
    an4per1base=models.CharField(max_length=4)
    an4per2du=models.DateTimeField()
    an4per2au=models.DateTimeField()
    an4per2taux=models.FloatField()
    an4per2base=models.CharField(max_length=4)
    salairebrutmensuel=models.FloatField()
    caisseretraitecomplementaire=models.CharField(max_length=35)
    nourriture=models.FloatField()
    logement=models.FloatField()
    primepanier=models.FloatField()
    faita=models.CharField(max_length=60)
    faitle=models.DateField()
    attestationpieces=models.BooleanField(default=False)
    attestationmaitreapprentissage=models.BooleanField(default=False)

    def __str__(self):
        return self.id
