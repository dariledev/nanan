from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_homme = models.BooleanField('Is_homme', default=False)
    is_femme = models.BooleanField('Is_femme', default=False)








class Postes(models.Model):
    autheur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    date_joind = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()



    def __str__(self):
        return self.titre

class Comment(models.Model):
  post = models.ForeignKey(Postes, on_delete = models.CASCADE, related_name ='comments')
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  content = models.TextField()
  def __str__(self):
    return self.post.titre
class Demandeur(models.Model):
    nom_tribunal = models.CharField(max_length=60)
    numero_dossier = models.CharField(max_length=20)
    date_jugement = models.DateField(auto_now=True)


    nom_president = models.CharField(max_length=60)
    nom_demandeure = models.CharField(max_length=60)
    nom_avocat1 = models.CharField(max_length=60)
    nom = models.CharField(max_length=60)
    local1 = models.CharField(max_length=60)
    nom_demande = models.CharField(max_length=60)
    nom_avocat2 = models.CharField(max_length=60)
    local2 = models.CharField(max_length=60)
    nom_notaire = models.CharField(max_length=60)
    date_invitation = models.DateTimeField(auto_now=True)
    num_inivation = models.CharField(max_length=60)
    vehicul_type = models.CharField(max_length=60)
    matricule = models.CharField(max_length=60)
    date_accident = models.DateTimeField(auto_now=True)
    lieu_accident = models.CharField(max_length=80)
    nom_proces = models.CharField(max_length=60)
    date_pv =models.DateTimeField(auto_now_add=True)
    source_pv = models.CharField(max_length=60)
    description_acc = models.TextField()
    num_ordonance = models.CharField(max_length=60)
    date_ordonance = models.DateField(auto_now_add=True)
    type_vehicule = models.CharField(max_length=60)
    date_expertise = models.DateField(auto_now=True)
    dmg_materiel = models.CharField(max_length=100)
    numero_dossier = models.CharField(max_length=60)
    nom_avocat1 = models.CharField(max_length=60)
    nom_avocat2 = models.CharField(max_length=60)
    date_pledorie = models.DateField(auto_now_add=True)
    nom_avocat = models.CharField(max_length=60)
    nom_avocatdeux = models.CharField(max_length=60)
    adminupload = models.FileField(upload_to='media')

    cout_expertise = models.CharField(max_length=60)
    honaire_avocat_demande = models.CharField(max_length=60)
    cout_invitation = models.CharField(max_length=60)
    avocat_honoraire_ordonnance_demandes = models.CharField(max_length=60)
    avocat_honoraire_ordonnance_juge = models.CharField(max_length=60)
    cout_information_expertise = models.CharField(max_length=60)
    Demande_contradictoire = models.CharField(max_length=60)

    période_assurance = models.CharField(max_length=60)



    def __str__(self):
        return self.nom