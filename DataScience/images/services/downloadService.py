from images.services.saveImagesInfoService import SaveImagesInfo
from images.services.logService import LogService
from images.models.models import ImagesInfo
import datetime
import eventlet
import requests


class DownloadImage:
    def get_info(self,data,vendor):

        image_list=data
        vendor=vendor
        images_info=[]
        api = 'bulkImage'
        save_instance=SaveImagesInfo()
        pool = eventlet.GreenPool()

        for url,filename,sku,collection,design,body in pool.imap(DownloadImage().fetch, image_list):
            image_details={'fileName':filename,'sku':sku,'collection':collection,'design':design,'vendor':vendor,'body':body}
            images_info.append(image_details)
            print ('****** got body from url *****')

        for sku in pool.imap(save_instance.save_images_info,images_info):
            print('****** save image is done *******',sku)


        del image_list


    def fetch(self,image_info):

        try:
            url=image_info['url']
            filename=image_info['fileName']
            sku=image_info['sku']
            collection=image_info['collection']
            design=image_info['design']
            print("opening", url,'*******',filename)
            open_time=datetime.datetime.now().time()
            print('********* time of opening URL *********',open_time)
            url_type=requests.get(url,timeout=180)
            print(' url is ',url_type)
            header =url_type.headers['Content-Type']
            print('*********** header is ************',header)
            api = 'bulkImage'

            if header:
                if header=='image/jpeg' or header=='application/binary' or header=='application/octet-stream':
                    body = url_type.content
                    return url, filename, sku, collection, design, body


        except Exception as e:
            print('******** error in download image ********', str(e))
            sku = image_info['sku']
            filename = image_info['fileName']
            blob_instance = ImagesInfo.objects.get(SKU=sku, imageName=filename)
            blob_instance.errorType = 'Wrong URL'
            blob_instance.save()








