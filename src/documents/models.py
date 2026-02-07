from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL #-> auth.user

class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, delete all documents related to that user
    title = models.CharField(max_length=255, default="Title")
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now_add=False,auto_now=False, blank=True, null=True) # when the document is active, this field will be updated with the current time
    created_at = models.DateTimeField(auto_now_add=True) #db auto update this field when it's created
    updared_at = models.DateTimeField(auto_now=True) # db auto update this field when it's updated
    
    def __str__(self):
        return f"<Document: {self.title}>"
    
    def save(self, *args, **kwargs):
        if self.active and self.active_at is not None:
            self.active_at = timezone.now()
        else:
            self.active_at = None
        super().save(*args, **kwargs)