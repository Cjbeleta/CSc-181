from flask_wtf import Form
from wtforms import StringField, validators

class studentForm(Form):
    idnumber = StringField('ID Number', [validators.Length(min=9, max=9)])
    first = StringField('First Name')
    middle = StringField('Middle Name')
    last = StringField('Last Name')
    sex = StringField('Sex')
    course = StringField('Course')