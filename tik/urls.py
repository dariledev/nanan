from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_us, name='login'),
    path('upload/', views.upload, name='upload'),
    path('homme/', views.homme, name='homme'),
    path('femme/', views.femme, name='femme'),
    path('logout/', views.logout_user, name='logout'),
    path('edit/<int:my_id>/', views.editform, name='update'),
    #path('download/', views.some_view, name='download_file'),
     path('demandeur/', views.demander, name='demandeur'),
     path('staf/', views.staf, name='staf'),
     path('donnees/', views.donne, name='donnee'),
     path('download/', views.download),
     path('detail/<int:id>/', views.detail, name='show'),
     path('modifier/<int:id>/', views.updatedemande, name='udm'),
     path('post_comment/<int:id>/', views.detail_post, name='post'),



     #path('rap/', views.rap, name='rap'),










]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)