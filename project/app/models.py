from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage,VideoMediaCloudinaryStorage,MediaCloudinaryStorage

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    document = models.FileField(upload_to='file/' ,storage=RawMediaCloudinaryStorage)
    image=models.ImageField(upload_to='image/', storage=MediaCloudinaryStorage)
    vedioo=models.FileField(upload_to='video/',null=True, blank=True, storage=VideoMediaCloudinaryStorage)
    passw= models.CharField(max_length=50)
    c_passw =models.CharField(max_length=50)
    