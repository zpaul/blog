from flask_wtf import FlaskForm
from wtforms import StringField, TextField,TextAreaField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    """Form validator for comment."""

    #Set some field(InputBox) for enter the data.
    #param validators: setup lists of validators

    name = StringField(
        'Name',
        validators=[DataRequired(),Length(min=3, max=255)]
    )
    text = TextAreaField(u'Comment',validators=[DataRequired()])