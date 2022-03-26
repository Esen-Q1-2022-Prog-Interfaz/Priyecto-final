from utils.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.String(50), nullable=False)
    provider = db.Column(db.String(50), nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    tax = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=True)
    totalsale=db.Column(db.Integer, nullable=False)

    def _init_(self, buyer, provider, discount, tax, totalsale=0, date=None) -> None:
        self.comprador = buyer
        self.vendedor = provider
        self.descuento = discount
        self.impuesto = tax
        self.date = date
        self.totalsale=  totalsale

    def _repr_(self) -> str:
        return f"Order({self.id}, {self.buyer}, '{self.provider}', '{self.discount}', '{self.tax}', '{self.totalsale}', '{self.date}')"