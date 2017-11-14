from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired

class CadastrarProcessoForm(Form):
    processo_descricao = TextAreaField('Descrição')
    processo_tipo =  StringField('Tipo', validators=[DataRequired('Tipo do Processo é obrigatória')])
    