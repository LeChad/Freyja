from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from main.validator import validate_image
from PIL import Image
from shutil import copy
from os import remove
from os.path import splitext, join
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = models.ImageField(
        default='avatar.jpg',
        upload_to='profile_pictures',
        validators=[validate_image]
    )
    bio = models.CharField(max_length=1500)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # resize images
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Create a thumbnail
            img.save(self.profile_picture.path) # overwrite larger image

        file_name, file_extension = splitext(self.profile_picture.file.name)
        print(f"PICTURE NAME: {self.profile_picture.name}")


        if self.profile_picture.name == "avatar.jpg":
            default_avatar_path = join(settings.MEDIA_ROOT, "avatar.jpg")
            new_avatar_path = join(settings.MEDIA_ROOT, "profile_pictures", f"{self.profile_picture_id}.jpg")
            copy(default_avatar_path, new_avatar_path)
        else:
            self.profile_picture.name = f"{self.profile_picture_id}{file_extension}"

        super(Profile, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        remove(self.profile_picture.path)
        super(Profile, self).delete(*args, **kwargs)
