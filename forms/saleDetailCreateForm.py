from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length


class SaleCreateform(FlaskForm):
    
    description = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=50),
        ],
        render_kw={"placeholder": "description..."},
    )

    client = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=50),
        ],
        render_kw={"placeholder": "client..."},
    )

    quantity = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "quantity..."},
    )
    
    unitcostsale = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "unit cost sale..."},
    )
    submit = SubmitField("create")
