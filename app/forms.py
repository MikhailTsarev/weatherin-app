from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired, Length

class CityForm(FlaskForm):
    city_name = TextField('Введи название города', validators = [DataRequired(),Length(min=1, max=140)])
    submit = SubmitField('Узнать погоду')

    def validate_city(self,code_from_api):
        if code_from_api == '404':
            self.city_name.errors.append('Город не найден ;(')
            return 0
        return 1
