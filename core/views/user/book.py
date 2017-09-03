# -*- coding: utf-8 -*-

from . import client
from flask import request
from core.models import Book
from flask import render_template
from flask_login import login_required
from flask_login import current_user
from flask import redirect, url_for
from sqlalchemy import or_


@client.route('/books', methods=['GET'])
@login_required
def books_list():
    keyword = request.args.get('keyword', '')
    book_query = Book.query
    if keyword:
        keyword = "%%%s%%" % keyword
        book_query = book_query.filter(or_(
            Book.name.like(keyword),
            Book.author.like(keyword),
            Book.publish.like(keyword),
            Book.isbn.like(keyword)
        ))
    books = book_query.filter_by(active=True).all()
    return render_template('user/book.html', books=books, count=len(books))


@client.route('/book/mine', methods=['GET'])
@login_required
def my_books_list():
    keyword = request.args.get('keyword', '')
    book_query = Book.query
    if keyword:
        keyword = "%%%s%%" % keyword
        book_query = book_query.filter(or_(
            Book.name.like(keyword),
            Book.author.like(keyword),
            Book.publish.like(keyword),
            Book.isbn.like(keyword)
        ))
    books = book_query.filter_by(active=True, borrowed_by=current_user.user.name).all()
    return render_template('user/book_order.html', books=books, count=len(books))


@client.route('/book/order', methods=['GET'])
@login_required
def book_order():
    book_id = request.args.get('id')
    book = Book.get_by_id(book_id)
    info = {
        'borrowed_by': current_user.user.name,
        'borrowed_phone': current_user.user.phone
    }

    book.update(**info)
    return redirect(url_for('client.my_books_list'))


@client.route('/book/return', methods=['GET'])
@login_required
def book_return():
    book_id = request.args.get('id')
    book = Book.get_by_id(book_id)
    info = {
        'borrowed_by': None,
        'borrowed_phone': None
    }

    book.update(**info)
    return redirect(url_for('client.my_books_list'))