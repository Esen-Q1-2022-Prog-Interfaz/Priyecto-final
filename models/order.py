from utils.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.String(50), nullable=False)
    provider = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    tax = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=True)
    totalsale=db.Column(db.Integer, nullable=False)

    def __init__(self, buyer, provider, discount, tax, description, totalsale=0, date=None) -> None:
        self.buyer = buyer
        self.provider= provider
        self.discount = discount
        self.tax = tax
        self.description = description
        self.date = date
        self.totalsale=  totalsale

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.buyer}, '{self.provider}', '{self.discount}', '{self.tax}', '{self.description}','{self.totalsale}', '{self.date}')"