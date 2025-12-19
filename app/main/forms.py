from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField, DateField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Email
from wtforms import TextAreaField
from wtforms.validators import Length

from app import db
import sqlalchemy as sqla
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.widgets import ListWidget, CheckboxInput
from app.main.models import Tag


class CreatePost(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    description = StringField('Text', validators=[DataRequired()])
    date = DateField('Publication Date', validators=[DataRequired()], render_kw={"class": "datepicker-input"})
    tags = QuerySelectMultipleField('Tags',
                                      query_factory=lambda: db.session.scalars(sqla.select(Tag).order_by(Tag.name)),
                                      get_label=lambda theTopic: theTopic.name,
                                      widget=ListWidget(prefix_label=False),
                                      option_widget=CheckboxInput())

    submit = SubmitField('Create Post')

class EditPost(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    description = StringField('Text', validators=[DataRequired()])
    date = DateField('Publication Date', validators=[DataRequired()], render_kw={"class": "datepicker-input"})
    tags = QuerySelectMultipleField('Tags',
                                      query_factory=lambda: db.session.scalars(sqla.select(Tag).order_by(Tag.name)),
                                      get_label=lambda theTopic: theTopic.name,
                                      widget=ListWidget(prefix_label=False),
                                      option_widget=CheckboxInput())

    submit = SubmitField('Save Changes')

class EditAbout(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    about = StringField('Text', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

class CommentForm(FlaskForm):
    statement = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Add Comment')

class AddTagForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add tag')

class DeleteTagForm(FlaskForm):
    tags = QuerySelectMultipleField('Tags',
                                      query_factory=lambda: db.session.scalars(sqla.select(Tag).order_by(Tag.name)),
                                      get_label=lambda theTopic: theTopic.name,
                                      widget=ListWidget(prefix_label=False),
                                      option_widget=CheckboxInput())
    submit = SubmitField('Delete tag')

