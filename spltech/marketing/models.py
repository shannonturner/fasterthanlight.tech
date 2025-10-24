from django.db import models

class Submission(models.Model):

    """ One submission to /services#contact
    """

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    services = models.ManyToManyField('Service')
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"Submission by {self.name} at {self.organization} on {self.created_at}"

class Service(models.Model):

    """ One service offered at /services#contact
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
