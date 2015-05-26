from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    notes = models.TextField(default="")

    @property
    def name_abbrev(self):
        name = str(self)
        return name[:25] + "..." if len(name) > 28 else name

    @property
    def notes_abbrev(self):
        if self.notes:
            return self.notes[:30] + "..." if len(self.notes) > 33 else self.notes
        else:
            return "..."

    def __str__(self):
        return " ".join([self.first_name, self.last_name])
