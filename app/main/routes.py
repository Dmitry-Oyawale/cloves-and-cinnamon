from app import db
from flask import render_template, flash, redirect, url_for, request, jsonify
import sqlalchemy as sqla

from app.main.models import Viewer, Author, Post, Comment, PostLike
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
def read_more(post_id):
    post=Post.query.get_or_404(post_id)
    form = CommentForm()
    return render_template('post.html', post=post, form=form)

@main.route('/author/<author_id>/view', methods=['GET'])
def view_about(author_id):
    author = db.session.get(Author, author_id)
    return render_template('about.html', author=author)

@main.route('/author/<post_id>/settings', methods=['GET', 'POST'])
@login_required
@role_required("author")
def edit_post(post_id):
    form = EditPost()
    post=Post.query.get_or_404(post_id)
    if form.validate_on_submit():
        post.name = form.name.data
        post.description = form.description.data
        post.date = form.date.data
        post.tags = form.tags.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.read_more', post_id=post.id))
    elif request.method == 'GET':
        form.name.data = post.name
        form.description.data = post.description
        form.date.data = post.date
        form.tags.data = post.tags
    return render_template('edit_post.html', title='Edit Post', form=form, post=post)

@main.route('/author/<post_id>/deletion', methods=['GET', 'POST'])
@login_required
@role_required("author")
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if current_user.role != 'author' or post.author_id != current_user.id:
        flash('You are not authorized to delete this position.', 'error')
        return redirect(url_for('main.index'))
    
    Comment.query.filter_by(post_id=post.id).delete()
    
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/post/<post_id>/like', methods=['POST'])
@login_required
def toggle_post_like(post_id):
    post = Post.query.get_or_404(post_id)

    like = PostLike.query.filter_by(
        viewer_id=current_user.id,
        post_id=post_id
    ).first()

    if like:
        db.session.delete(like)  
    else:
        db.session.add(PostLike(viewer_id=current_user.id, post_id=post_id)) 

    db.session.commit()
    return redirect(url_for('main.read_more', post_id=post_id))

@main.route('/author/about/edit', methods=['GET', 'POST'])
@login_required
@role_required("author")
def edit_about():
    form = EditAbout()
    if form.validate_on_submit():

        if form.email.data != current_user.email:
            existing_author = Author.query.filter(
                Author.email == form.email.data,
                Author.id != current_user.id
            ).first()

            existing_viewer = Viewer.query.filter_by(email=form.email.data).first()

            if existing_viewer or existing_author:
                form.email.errors.append("This email is already in use. Please choose another one.")
                return render_template(
                    'edit_about.html',
                    title='Edit About',
                    form=form
                )

        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about = form.about.data
        current_user.set_password(form.password.data)

        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.view_about', author_id=current_user.id))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about.data = current_user.about

    return render_template('edit_about.html', title='Edit About',
                           form=form)

@main.route('/post/<post_id>/comments', methods=['POST'])
@login_required
def leave_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(post_id=post.id, statement=form.statement.data)

        if current_user.role == 'viewer':
            comment.viewer_id = current_user.id
        else:  
            comment.author_id = current_user.id

        db.session.add(comment)
        db.session.commit()
        flash("Comment submitted, waiting for approval!")

    return redirect(url_for('main.read_more', post_id=post.id))

@main.route('/author/tags/settings', methods=['GET', 'POST'])
@login_required
@role_required("author")
def edit_tags():
    form = AddTagForm(prefix='tag')
    dform = DeleteTagForm(prefix='tag_delete')

    if dform.submit.data and dform.validate_on_submit(): 
        try:
            for tag in dform.tags.data:
                db.session.delete(tag)

            db.session.commit()
            flash('Tags deleted!', 'success')
            return redirect(url_for('main.edit_tags'))
        except sqla.exc.IntegrityError:
            db.session.rollback()
            flash('Cannot delete this item due to dependencies!', 'error')
            return redirect(url_for('main.edit_tags'))
    else:
        for fieldName, errorMessages in dform.errors.items():
            for err in errorMessages:
                print(err)

    if form.submit.data and form.validate_on_submit():
        if form.name.data:
            name = form.name.data.strip()

            existing_topic = db.session.scalars(
                sqla.select(Tag).where(Tag.name == name)
            ).first()

            if existing_topic:
                flash(f'Tag "{name}" already exists.', 'error')
                return redirect(url_for('main.edit_tags'))
            
            new_tag = Tag(
                name = tag.name.data
            )

            db.session.add(new_tag)
            db.session.commit()
            flash('Tag added!', 'success')
            return redirect(url_for('main.edit_tags'))
        else:
            flash('Please complete the form', 'error')
            return redirect(url_for('main.edit_tags'))
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)

    return render_template('edit_tags.html', title='Edit tags', form=form, dform=dform)