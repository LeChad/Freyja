from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default='avatar.jpg',
        upload_to='profile_pictures'
    )
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # resize images
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Create a thumbnail
            print(f"PICTURE PATH: {self.profile_picture.path}")
            img.save(self.profile_picture.path) # overwrite larger image
