from django.shortcuts import render
from django.views import View
from .models import Books
from django.contrib.auth.models import User


def home(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'defaults/home.htm', context)

class BooksList(View):
    template_name = 'books/books_list.html'

    def get(self, request):
        books = Books.objects.all()
        return render(request, self.template_name, {'books': books})

class BookDetail(View):
    template_name = 'books/books_inner.html'

    def get(self, request, book_id):
        try:
            book = Books.objects.get(id=book_id)
        except Books.DoesNotExist:
            book = None
        return render(request, self.template_name, {'book': book})

class Library(View):
    template_name = 'books/library.htm'

    def get(self, request):
        books = Books.objects.all()
        return render(request, self.template_name, {'books': books})
    
class UserListView(View):
    template_name = 'Members/member.htm'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})
    



    
class Contacts(View):
    template_name = 'Contacts/contact.htm'

    def get(self, request):
        return render(request, self.template_name)
    
        