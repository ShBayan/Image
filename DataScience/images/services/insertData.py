from images.services.downloadService import DownloadImage
from images.models.serializers import ImageSerializer


class InsertData:

    def insert_data(self,data):

        count=0
        for item in data['imagesInfo']:
            serializer = ImageSerializer(data={'imageName':item['fileName'],'imageURL':item['url'],'vendorName':data['vendor'],'collectionName':item['collection'],'designName':item['design'],'SKU':item['sku']})
            if serializer.is_valid():
                serializer.save()
                count+=1

        images_info=data['imagesInfo']
        num=len(images_info)
        vendor=data['vendor']
        download_instance = DownloadImage()
        if num>=1:
            for i in range(0,num,10):
                chunked_list = images_info[i:i + 10]
                download_instance.get_info(chunked_list,vendor)


