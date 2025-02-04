from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Review

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        Book.objects.create(title=title, author=author, description=description, added_by=request.user)
        return redirect('book_list')
    return render(request, 'add_book.html')

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.added_by == request.user:
        book.delete()
    return redirect('book_list')

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        review_text = request.POST['review_text']
        Review.objects.create(book=book, user=request.user, review_text=review_text)
    return redirect('book_list')
