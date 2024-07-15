from django.urls import path
from .views import (create_research,create_thesis,graphics_design_submission,programming_project_submission,video_editing_submission,transcription,business_plan,assignment)
from django.conf import settings
from django.conf.urls.static import static


app_name = 'order'

urlpatterns = [
    path('order/',create_research,name='order' ),
    path('thesis/',create_thesis,name='thesis' ),
    path('graphdesign/',graphics_design_submission,name='graphics-design' ),
    path('programming/',programming_project_submission,name='program-project' ),
    path('video/',video_editing_submission,name='video-project' ),
    path('transcription/',transcription,name='transcription' ),
    path('assignment/',transcription,name='assignment' ),
    path('business/',transcription,name='business-plan' ),


    # path('order_tabel/',order_tabel,name='order_tabel' ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)