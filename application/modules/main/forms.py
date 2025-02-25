from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import StringField, SubmitField


class CheckoutForm(FlaskForm):
    card_number = StringField(
        "Credit Card Number",
        validators=[
            DataRequired(),
            Length(min=16, max=16, message="Card number must be between 16 digits"),
            Regexp(r"^\d+$", message="Card number must contain only digits"),
        ],
    )
    submit = SubmitField("Submit")

    @staticmethod
    def validate_card_number(_, field):
        # Remove hyphens before validation
        field.data = field.data.replace("-", "")
