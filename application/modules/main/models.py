from application import db


class Purchase(db.Model):
    purchase_id = db.Column(db.Integer, primary_key=True)

    # Amount in cents
    amount = db.Column(db.Integer, nullable=False)
