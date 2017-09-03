# -*- coding: utf-8 -*-

import json
from . import admin
from flask import request
from flask import redirect
from flask import url_for
from core.models import Book
from sqlalchemy import or_
from flask import render_template
from flask_login import login_required
from core.views.common import render_json


@admin.route('/books', methods=['GET'])
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
    return render_template('admin/book.html', books=books, count=len(books))


@admin.route('/book/add', methods=['GET', 'POST'])
@login_required
def book_add():
    if request.method == 'POST':
        book_info = {
            'name': request.form['name'],
            'author': request.form['author'],
            'publish': request.form['publish'],
            'price': request.form['price'],
            'isbn': request.form['isbn']
        }

        Book.create(**book_info)
        return render_json(0, {'href': '/admin/books', 'delaySuccess': True})
    return render_template('admin/book_add.html')


@admin.route('/book/edit', methods=['GET', 'POST'])
@login_required
def book_edit():
    book_id = request.args.get('id')
    book = Book.get_by_id(book_id)
    if request.method == 'POST':
        book_info = {
            'name': request.form['name'],
            'author': request.form['author'],
            'publish': request.form['publish'],
            'price': request.form['price'],
            'isbn': request.form['isbn']
        }

        book.update(**book_info)
        return render_json(0, {'href': '/admin/books', 'delaySuccess': True})
    return render_template('admin/book_edit.html', book=book)


@admin.route('/book/delete', methods=['GET', 'POST'])
@login_required
def video_detail():
    book_id = request.args.get('id')
    book = Book.get_by_id(book_id)
    book.update(active=False)
    return redirect(url_for('admin.books_list'))
