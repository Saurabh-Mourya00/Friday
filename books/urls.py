from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name='home'),
    path('books/', BooksList.as_view(), name='books_list'),
    path('books/<int:book_id>/', BookDetail.as_view(), name='book_detail'),
    path('library/', Library.as_view(), name='library'),
    path('member/', UserListView.as_view(), name='member'),
    path('member/', UserListView.as_view(), name='member'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    
    



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)