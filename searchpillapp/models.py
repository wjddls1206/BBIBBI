from django.db import models

# Create your models here.
class Product(models.Model):
    imgfile = models.ImageField(null=True, upload_to="", blank=True)  # 이미지 컬럼 추가