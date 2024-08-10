from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from images import views

urlpatterns=[url(r'^api/v1/blobImage/$', views.BlobImage().blob_image),
             url(r'^api/v1/saveImage/$',views.SaveImage().save_image),
             url(r'^api/v1/rotateImage/$',views.RotateImage().rotate_image),
             url(r'^api/v1/bulkImageImport/$',views.SaveBulkImage().send_bulkImages),
             url(r'^api/v1/getImageColor/$',views.GetColorImages().get_color_of_images)]
             # url(r'^home/$',views.home, name="home")]

urlpatterns = format_suffix_patterns(urlpatterns)

