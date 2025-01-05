from django.db import models
from .validators import validate_image_format, validate_image_size

class ImageUpload(models.Model):
    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_format, validate_image_size]
    )
    sign = models.ImageField(
        upload_to='signs/',
        validators=[validate_image_format, validate_image_size]
    )
    thumb = models.ImageField(
        upload_to='thumbnails/',
        validators=[validate_image_format, validate_image_size]
    )

    def __str__(self):
        return f"Images {self.id}"
