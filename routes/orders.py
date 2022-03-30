from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderCreateForm import OrderCreateForm
from utils.db import db
from models.order import Order
from datetime import date, datetime

orders = Blueprint("orders", __name__, url_prefix="/orders")


@orders.route("/")
@login_required
def home():
    orderList = Order.query.all()
    return render_template("orders/home.html", orders=orderList, user=current_user)


@orders.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderCreateForm()
    if form.validate_on_submit():
        buyer = form.buyer.data
        provider = form.provider.data
        description = form.description.data
        discount = form.discount.data
        tax = form.tax.data
        newOrder = Order(buyer, provider, discount, tax, description, totalsale=0, date=datetime.today())
        db.session.add(newOrder)
        db.session.commit()
        return redirect(url_for("orders.home"))
    return render_template("orders/create.html", form=form)


# http://127.0.0.1:5000/orders/finalize/1
@orders.route("/finalize/<int:id>")
@login_required
def finalize(id):
    currentOrder = Order.query.get(id)
    currentDate = date.today().isoformat()
    currentOrder.date = currentDate
    # db.session.add si ocupas un objeto completamente nuevo hace un insert
    # db.session.add si ocupas un objeto modificado hace un update
    db.session.add(currentOrder)
    db.session.commit()
    return redirect(url_for("orders.home"))
