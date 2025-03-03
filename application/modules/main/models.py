# Author: Jack Hermanson
from application import db


class Purchase(db.Model):
    # Primary key
    purchase_id = db.Column(db.Integer, primary_key=True)

    # Amount in cents
    amount = db.Column(db.Integer, nullable=False)

    # Set by merchant before it is sent to processor.
    authorization_id = db.Column(db.String(50), nullable=False)

    # Received by merchant in processor response
    approval_code = db.Column(db.String(50), nullable=False)
