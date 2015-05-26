from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    notes = models.TextField(default="")
    protected = models.BooleanField(default=0)

    @property
    def name_abbrev(self):
        name = str(self)
        return name[:25] + "..." if len(name) > 28 else name

    def __str__(self):
        return " ".join([self.first_name, self.last_name])
