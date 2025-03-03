from datetime import datetime

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Regexp, NumberRange
from wtforms import StringField, SubmitField, IntegerField, DecimalField


class CheckoutForm(FlaskForm):
    card_number = StringField(
        "Credit Card Number",
        validators=[
            DataRequired(),
            Length(min=19, max=19, message="Card number must be exactly 19 characters (including hyphens)"),
            Regexp(r"^\d{4}-\d{4}-\d{4}-\d{4}$", message="Card number must be formatted as XXXX-XXXX-XXXX-XXXX"),
        ],
        render_kw={"oninput": "formatCardNumber(this)", "autofocus": True},
        description="16-digit number; we don't take American Express because their numbers are weird",
    )
    card_code = StringField(
        "Card Code",
        validators=[
            DataRequired(),
            Length(min=3, max=3, message="Card code is 3 characters"),
            Regexp("^\d{3}$", message="Card code is a 3-digit number"),
        ],
        description="",
    )
    exp_month = IntegerField(
        "Exp Month",
        validators=[DataRequired(), NumberRange(min=1, max=12, message="Exp month must be between 1 and 12")],
    )
    exp_year = IntegerField(
        "Exp Year",
        validators=[
            DataRequired(),
            NumberRange(min=datetime.today().year, message="Exp year must be between current year"),
        ],
    )
    name = StringField("Name", validators=[DataRequired(), Length(max=25)])
    amount = DecimalField(
        "Amount",
        validators=[DataRequired(), NumberRange(min=0, message="Amount must be positive")],
        render_kw={"step": "0.01"},
    )

    submit = SubmitField("Submit")
