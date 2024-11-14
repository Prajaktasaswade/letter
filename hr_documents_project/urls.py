from django.contrib import admin  # Ensure this is imported
from django.urls import path, include  # Ensure 'include' is imported
from letters import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.index_page, name='index_page'),  # Your home page URL
    path('letters/', include('letters.urls')),  # Include URLs from the 'letters' app
    path('index-letter/', views.index_letter_view, name='index_letter'),
   
]
