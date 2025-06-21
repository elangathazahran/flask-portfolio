from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional


class PortfolioForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    category = SelectField(
        "Category",
        choices=[
            ("web", "Web Development"),
            ("freelance", "Freelance"),
            ("certifications", "Certification"),
        ],
        validators=[DataRequired()],
    )
    description = TextAreaField("Description", validators=[Optional()])
    image = FileField("Image", validators=[Optional()])
    live_link = StringField("Live Link", validators=[Optional()])
    github_link = StringField("GitHub Link", validators=[Optional()])
    submit = SubmitField("Create")
