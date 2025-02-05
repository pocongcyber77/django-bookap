from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Review

def book_list(request):
    if request.user.is_authenticated:
        books = Book.objects.all()  # Show all books for authenticated users
    else:
        books = Book.objects.all()  # Show all books for unauthenticated users

    return render(request, "library_app/book_list.html", {"books": books})

@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description', '')

        if title and author:
            Book.objects.create(title=title, author=author, description=description, added_by=request.user)
            return redirect('book_list')  

    return render(request, "library_app/add_book.html")

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Ensure only the user who added the book can delete it
    if book.added_by == request.user:
        book.delete()

    return redirect('book_list')






def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('/')  # Redirect to login page after logout

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        review_text = request.POST.get('review_text', '')

        if review_text:
            Review.objects.create(book=book, user=request.user, review_text=review_text)

    return redirect('book_list')

