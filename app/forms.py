from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired

class CityForm(FlaskForm):
    city_name = TextField('city_name', validators = [DataRequired()])

    def validate_city(self,code_from_api):
        if code_from_api == '404':
            self.city_name.errors.append('Город не найден ;(')
            return 0
        return 1
