from django.db import models


class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    displayName = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phoneNumber = models.BigIntegerField()
    photoURL = models.FileField(upload_to="", null=False, blank=True)

    def __str__(self):
        return f"{self.displayName} - (id= {self.id}) "
