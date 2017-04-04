from django.shortcuts import render, redirect
from .models import Book, Author, Review
from ..login_registration.models import User

# Create your views here.

def start(request):
    context={
        'reviews': reversed(Review.objects.all().order_by('-id')[:3]),
        'books': Book.objects.all(),
    }
    return render(request, 'book_review/start.html', context)

def add(request):
    context={
        'authors': Author.objects.all(),
    }
    return render(request, 'book_review/add.html', context)

def add_book(request):
    if request.method == 'POST':
        if request.POST['add']=='review':
            #Author
            print request.POST.keys()
            if 'author' in request.POST and request.POST['author']:
                author = request.POST['author']
                author = Author.objects.get(name=author)
            elif request.POST['new_author']:
                author = Author.objects.create(name=request.POST['new_author'])
            new_book = Book.objects.create(title=request.POST['book_title'], author=author)
            #Rating & Review
            user = User.objects.get(id=request.session['user_id'])
            review = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user=user, book=new_book)
            return redirect('book_review:review_book', book_id=new_book.id)

def review_book(request, book_id):
    context={
        'book': Book.objects.get(id=book_id),
        'reviews': Review.objects.filter(book=Book.objects.get(id=book_id))
    }
    return render(request, 'book_review/book.html', context)

def submit_review(request, book_id):
    if request.method=='POST':
        user=User.objects.get(id=request.session['user_id'])
        book=Book.objects.get(id=book_id)
        new = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user=user, book=book)
        return redirect('book_review:review_book', book_id=book_id)

def user(request, user_id):
    context={
        'user': User.objects.get(id=user_id),
        'reviews': Review.objects.filter(user=User.objects.get(id=user_id)),
        'count': Review.objects.filter(user=User.objects.get(id=user_id)).count(),
    }
    return render(request, 'book_review/user.html', context)
