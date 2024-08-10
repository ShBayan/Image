from rest_framework import serializers

from images.models.models import ImagesInfo

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=ImagesInfo
        fields=('id','imageName','imageURL','SKU','vendorName','collectionName','designName','isDone','errorType')

    def create(self,validated_data):
        return ImagesInfo.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.imageName=validated_data.get('imageName',instance.imageName)
        instance.imageURL=validated_data.get('imageURL',instance.imageURL)
        instance.SKU=validated_data.get('SKU',instance.SKU)
        instance.vendorName=validated_data.get('vendorName',instance.vendorName)
        instance.collectionName=validated_data.get('collectionName',instance.collectionName)
        instance.designName=validated_data.get('designName',instance.designName)
        instance.isDone=validated_data.get('isDone',instance.isDone)
        instance.errorType=validated_data.get('errorType',instance.errorType)
        instance.save()
        return instance

