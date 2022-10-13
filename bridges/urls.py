from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.board_list),
    path('add/', views.board_write),
    # path('detail/<int:pk>', views.board_detail),
    # path('map/<str:latitude>/<str:longitude>', views.board_map),
]
