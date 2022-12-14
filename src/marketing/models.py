from django.db import models



class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return "{} - {}".format(
                self.id,
                self.email
                )
