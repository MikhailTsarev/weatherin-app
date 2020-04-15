from flask_wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import Required

class CityForm(Form):
    city_name = TextField('city_name', validators = [Required()])
    country_choice = SelectField('country_choice', choices = [])

    def validate_city(self,code):
        if code == '404':
            self.city_name.errors.append('Город не найден ;(')
            return 1
        return 0
