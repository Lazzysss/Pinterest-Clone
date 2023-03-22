from django.contrib import admin
from app.views import home
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, {'pagename': ''}, name='home'),
    path('register/', views.sign_up, name='sign up'),
    path('login/', views.sign_in, name='sign in'),
    path('logout/', views.sign_out, name='sign out'),
    path('register/success/', views.success_class, name='success_class'),
    path('register/logout/', views.success_out, name='success_out'),
    path('MyProfile/', views.MyProfile, name='MyProfile'),
    path('MyPosts/', views.MyPosts, name='MyPosts'),
    path('MyProfile/change_password/', views.change_password, name='change_password'),
    path('create/', views.create, name='create'),
    path('detaile/<int:pk>/', views.detaile, name='detail'),
    path('change_password/success/', views.success_password, name='success_password'),
    path("search/", views.search, name="search_results"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)