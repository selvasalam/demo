from django.urls import path
from .import views
app_name='movieapp'
urlpatterns = [
    #path('',views.index,name='index'),
    path('',views.Movielistview.as_view(),name="index"),
   #path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('Moviedetail/<int:pk>',views.Moviedetailview.as_view(),name="moviedetail"),
    #path('add/',views.add_movie,name='add_movie'),
    path('Moviecreate',views.Movieaddview.as_view(),name="moviecreate"),
    #path('update/<int:id>/',views.update,name='update'),
    path('Movieupdate/<int:pk>',views.Movieupdateview.as_view(),name="movieupdate"),
    path('Moviedelete/<int:pk>', views.Moviedeleteview.as_view(), name="moviedelete"),

    # path('delete/<int:id>/', views.delete, name='delete'),

]
