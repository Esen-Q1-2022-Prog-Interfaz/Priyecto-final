from utils.db import db


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    client = db.Column(db.String(50), nullable=False)
    unitcostsale = db.Column(db.Integer, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    totalSale = db.Column(db.Integer, nullable=False)

    def __init__(self, description, client, unitcostsale, Quantity, totalCost=0) -> None:
        self.description = description
        self.client = client
        self.unitcostsale = unitcostsale
        self.Quantity = Quantity
        self.totalCost = totalCost

    def __repr__(self) -> str:
        return f"Order({self.description}, {self.client}, '{self.unitcostsale}', '{self.Quantity}', '{self.totalCost}')"
