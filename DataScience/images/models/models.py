from django.db import models

class ImagesInfo(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    imageName=models.CharField(max_length=500,blank=True,default='')
    imageURL=models.CharField(max_length=2000,blank=True,default='')
    SKU=models.CharField(max_length=2000,blank=True,default='')
    vendorName=models.CharField(max_length=200,blank=True,default='')
    collectionName=models.CharField(max_length=500,blank=True,default='')
    designName=models.CharField(max_length=500,blank=True,default='')
    isDone=models.BooleanField(default=False)
    errorType=models.CharField(max_length=2000,blank=True,default='')

class Meta:
    ordering=('created',)