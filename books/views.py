from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from datetime import datetime

from books.models import Book


def home_page(request):
    return redirect('books')


def books_view_pub_date(request, date, books):
    page_links = {}
    pub_date = datetime.strptime(date, '%Y-%m-%d').date()
    pub_dates = books.values_list('pub_date').distinct().order_by('pub_date')
    pub_dates = [elem[0] for elem in pub_dates]
    if pub_date in pub_dates:
        index = pub_dates.index(pub_date)
        if index - 1 >= 0:
            page_links['previos'] = str(pub_dates[index - 1])
        if index + 1 < len(pub_dates):
            page_links['next'] = str(pub_dates[index + 1])
    books = books.filter(pub_date=date)
    page_num = request.GET.get('page')
    element_per_page = 9
    paginator = Paginator(books, element_per_page)
    page = paginator.get_page(page_num)
    context = {
        'books': page.object_list,
        'page': page,
        'page_links': page_links
    }
    return context


def books_view_all(request, date=None):
    books = Book.objects.all()
    template = 'books/books_list.html'
    if date:
       context = books_view_pub_date(request, date, books)
    else:
        context = {'books': books}
    return render(request, template, context)