from images.controller.saveImageController import SaveImageController
from images.controller.bulkImageController import BulkImageController
from images.controller.getColorController import ColorController
from images.controller.rotateController import RotateController
from images.controller.blobController import BlobController
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from django import forms
# Create your views here.


class BlobImage:

    def blob_image(self,request):
            image=BlobController().blob_controller(request)
            return HttpResponse(image,content_type="image/jpeg")


class SaveImage:

    @csrf_exempt
    def save_image(self,request):
            SaveImageController().save_image_controller(request)
            return HttpResponse(request)


class SaveBulkImage:

    @csrf_exempt
    def send_bulkImages(self,request):
        BulkImageController().bulk_image_controller(request)
        return HttpResponse(request)


class RotateImage:

    @csrf_exempt
    def rotate_image(self,request):
        rotated_image=RotateController().rotate_controller(request)
        return HttpResponse(rotated_image, content_type="image/jpeg")

class GetColorImages:

    @csrf_exempt
    def get_color_of_images(self,request):
        ColorController().color_controller(request)
        return HttpResponse(request)
