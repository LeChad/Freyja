from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default="Photography Enthusiast")

    profile_picture = models.ImageField(
        default='avatar.jpg',  # default avatar
        upload_to='profile_pictures'  # dir to store the image
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.profile_picture.path)


