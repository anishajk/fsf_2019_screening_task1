
from django.contrib import admin
from django.urls import include,path
from .views import home

from accounts.views import login_view, register_view, logout_view

app_name='dj'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pro/', include('pro.urls')),
    path('', login_view),
    path('accounts/login/', login_view, name='signin'),
    path('accounts/register/', register_view, name='signup'),
    path('accounts/logout/', logout_view, name='logout')

]
