from django.db import models

# Create your models here.
# Creo modelo familiares con los campos de 
# id = identificador 
# nombre = apellido y nombre del familiar
# fechaNacimiento
class Familiar(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()

    def __str__(self):
        return "Id :"+str(self.id) + "\n Nombre :"+ str(self.nombre) + " Fecha Nacimiento :" + str(self.fechaNacimiento)   

