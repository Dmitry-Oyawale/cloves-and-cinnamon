from app import db
from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app.main.models import Viewer, Author, Post
from app.main.forms import *
from flask_login import current_user, login_required
from sqlalchemy import text

from app.main import main_blueprint as main
from datetime import datetime
from app.auth.role_required import role_required

@main.route('/', methods=['GET'])
@main.route('/index', methods=['GET'])
def index():
    #courses = db.session.scalars(sqla.select(Course))
    posts = db.session.scalars(sqla.select(Post))
    return render_template('base.html', title="Course List", posts = posts)

@main.route('/author/<author_id>/post', methods=['GET', 'POST'])
@login_required
@role_required("author")
def create_post(author_id):
    author = db.session.get(Author, author_id)
    if author is None:
        flash('Author not found.', 'error')
        return redirect(url_for('main.index'))

    if str(current_user.id) != str(author_id) or current_user.role != 'author':
        flash('You are not authorized to create posts for this author.', 'error')
        return redirect(url_for('main.index'))

    cform = CreatePost()

    if cform.validate_on_submit():
        new_post = Post(
            name=cform.name.data,
            description=cform.description.data,
            date=datetime.strptime(str(cform.date.data), '%Y-%m-%d').date(),
            author_id=author.id
        )

        new_post.tags = cform.tags.data

        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.index'))

    else:
        for fieldName, errorMessages in cform.errors.items():
            for err in errorMessages:
                print(err)

    return render_template('create_post.html', title='Create Post', form=cform, user=author)