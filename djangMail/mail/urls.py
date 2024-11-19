from django.urls import path

from.views import index, send_mail, mail_end

app_name = 'mail'

urlpatterns = [
    path('index/', index, name='index'),
    path('new/', send_mail, name='new'),
    path('end/', mail_end, name='end'),
]