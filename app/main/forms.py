#from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class AddpitchieieForm(FlaskForm):
    title = StringField("pitchie Title", validators = [Required()])
    pitchie = TextAreaField("Go", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("pick-up", "pick-up"),("boring","boring"),("funny","funny"),("promotion","promotion"),("product","product"),("cheesy","cheesy"),("random","random")],validators = [Required()]
    )
    submit = SubmitField("Add pitchie")

class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Add")

class EditBio(FlaskForm):
    bio = StringField("Bio")
    submit = SubmitField("Update")
