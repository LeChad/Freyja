from django.db import models
from django.contrib.auth.models import User
from main.validator import validate_image
from os import remove
from os.path import splitext
import uuid

class Photographs(models.Model):
    class Meta:
        verbose_name = "Photographs"
        verbose_name_plural = "Photographs"


    photograph_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photograph = models.ImageField(
        upload_to="photographs",
        validators=[validate_image],
        default='avatar.jpg'
    )

    title = models.CharField(max_length=100, blank=False, null=False, default="Untitled")
    description = models.CharField(max_length=500, null=True)
    uploaded_by = models.ForeignKey(User, null=True, editable=False, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now=True, editable=False)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        print(f"Photograph file path {self.photograph.path}")
        file_name, file_extension = splitext(self.photograph.file.name)
        self.photograph.name = f"{self.photograph_id}{file_extension}"
        super(Photographs, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        remove(self.photograph.path)
        super(Photographs, self).delete(*args, **kwargs)
