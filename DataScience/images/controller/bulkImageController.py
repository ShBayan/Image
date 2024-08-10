from images.services.insertData import InsertData
from rest_framework.parsers import JSONParser


class BulkImageController:
    def bulk_image_controller(self,request):
        if request.method=='POST':
            data = JSONParser().parse(request)
            data_instance = InsertData()
            data_instance.insert_data(data)

