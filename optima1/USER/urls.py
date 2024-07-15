from django.urls import path
from .views import (Sign_up,home,
                    Sign_in,portfolio_detail,
                    research_details,
                    res_help_details,
                    web_details,
                    video_details,
                    thesis_details,
                    transcription_details,
                    wr_ed_details,
                    business_details,
                    graphics_details,
                    programming_details,
                    assignment_details,
                    contact_us)

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'user'

urlpatterns = [
    path('login/',Sign_in,name='login' ),
    path('signup/', Sign_up, name='signup'),
    path('dashboard/', home, name='home_page'),
    path('portfolio_detail/', portfolio_detail, name='portfolio-details'),

    path('web_details/', web_details, name='web-details'),
    path('res_details/', research_details, name='research-details'),
    path('rh_details/', res_help_details, name='res_help-details'),
    path('video_details/', video_details, name='video-details'),
    path('the_details/', thesis_details, name='thesis-details'),
    path('tran_details/', transcription_details, name='transcription-details'),
    path('ass_details/', assignment_details, name='assignment-details'),
    path('graph_details/', graphics_details, name='graphics-details'),
    path('wd_details/', wr_ed_details, name='wr-ed-details'),
    path('bus_details/', business_details, name='business-details'),
    path('pro_details/', programming_details, name='programming-details'),


    # path('contactus/', contact_us, name='contactus'),
    path('logout/',LogoutView.as_view(),name='logout'),

    
    path('password-reset/', PasswordResetView.as_view(template_name='user/password_reset.html',email_template_name='user/password_reset_email.html',success_url = reverse_lazy('user:password_reset_done')),name='password-reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm1/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm1.html',success_url = reverse_lazy('user:password_reset_complete')),name='password_reset_confirm'),
    path('password-reset-complete1/done',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete1.html'),name='password_reset_complete'),
    

]