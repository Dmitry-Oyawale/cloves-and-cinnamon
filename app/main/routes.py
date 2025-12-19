from app import db
from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app.main.models import Viewer, Author, Post, Comment
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

@main.route('/post/<post_id>/view', methods=['GET'])
@login_required
def view_post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@main.route('/author/<post_id>/settings', methods=['GET', 'POST'])
@login_required
@role_required("author")
def edit_position(post_id):
    form = EditPost()
    post=Post.query.get_or_404(post_id)
    if form.validate_on_submit():
        post.name = form.name.data
        post.description = form.description.data
        post.date = form.date.data
        post.tags = form.tags.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.view_post', post_id=post.id))
    elif request.method == 'GET':
        form.name.data = post.name
        form.description.data = post.description
        form.date.data = post.date
        form.tags.data = post.tags
    return render_template('edit_post.html', title='Edit Post', form=form, post=post)

@main.route('/author/<post_id>/deletion', methods=['GET', 'POST'])
@login_required
@role_required("author")
def delete_position(post_id):
    post = Post.query.get_or_404(post_id)
    
    if current_user.role != 'author' or post.author_id != current_user.id:
        flash('You are not authorized to delete this position.', 'error')
        return redirect(url_for('main.index'))
    
    Comment.query.filter_by(post_id=post.id).delete()
    
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/post/<post_id>/like', methods=['GET', 'POST'])
@login_required
def like_post(post_id):
    post=Post.query.get_or_404(post_id)
    post.likes = post.likes + 1

