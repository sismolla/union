from django.db import models

class Contact_us_page(models.Model):
    name = models.CharField(null=False,max_length=50)
    email = models.EmailField(null=False, blank=False)
    Subject = models.TextField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    # date = models.DateTimeField(auto_created=True, blank=False)
    
    def __str__(self):
        return self.name
    