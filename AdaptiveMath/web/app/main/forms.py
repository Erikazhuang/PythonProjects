from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField,HiddenField,FileField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app.models import User, Record

class AdminForm(FlaskForm):
    tableList = ['Question','Skill','Category']
    targettable = SelectField('Select target database table',choices=tableList)
    file = FileField('Select file to upload')
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0,max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username,*args,**kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        self.original_username = original_username

    
    def validate_username(self, username):
        if username.data!=self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('User already exists, please use a different username.')



class SingleQuestionForm(FlaskForm):
    qid = HiddenField('qid')
    question = StringField('question', validators=[DataRequired()])
    answer = TextAreaField('answer', validators=[Length(min=1,max=140)])
    response = StringField('response', validators=[DataRequired()])
    submit = SubmitField('Submit')