
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from myapi.views import ListView, DetailView, CreateView , UpdateView , DeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('api_list/', ListView.as_view(), name='apl-list'),
    path('api_details/<int:classroom_id>/', DetailView.as_view(), name='api-details'),
    path('api_create/', CreateView.as_view(), name='apl-create'),
    path('api_update/<int:classroom_id>/', UpdateView.as_view(), name='api-update'),
    path('api_delete/<int:classroom_id>/', DeleteView.as_view(), name='api-delete'),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
