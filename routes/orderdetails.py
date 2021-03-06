from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.saleDetailCreateForm import SaleCreateform
from utils.db import db
from models.order import Order
from models.orderdetail import Sale

orderDetails = Blueprint("orderDetails", __name__, url_prefix="/orderDetails")


@orderDetails.route("/<int:id_order>")
@login_required
def home(id_order):
    details = Sale.query.filter_by(orderId = id_order)
    return render_template("orders/ordersDetails.html", user=current_user, orders=details)


@orderDetails.route("/<int:orderId>")
@login_required
def homeByOrderId(orderId):
    currentOrder = Order.query.filter_by(id=orderId).first()
    orderDetailList = Sale.query.filter_by(orderId=orderId).all()
    return render_template("orderDetails/home.html", order=currentOrder, user=current_user, items=orderDetailList)


@orderDetails.route("/create/<int:orderId>", methods=["GET", "POST"])
@login_required
def create(orderId):
    form = SaleCreateform()
    if form.validate_on_submit():
        currentSale = Sale.query.filter_by(id=orderId).first()

        quantity = form.quantity.data
        description = form.description.data
        unitCost = form.unitCost.data
        totalCost = quantity * unitCost
        currentOrder.totalsale += totalCost

        newOrderDetail = OrderDetail(orderId, quantity, description, unitCost, totalCost)
        db.session.add(newOrderDetail)
        db.session.add(currentOrder)
        db.session.commit()
        return redirect(url_for("orderDetails.home", id_order=orderId))
    return render_template("orderDetails/create.html", form=form, orderId=orderId)


@orderDetails.route("/create/<int:orderId>", methods=["GET", "POST"])
@login_required
def createByOrderId(orderId):
    form = OrderDetailCreateForm(orderId=orderId)
    if form.validate_on_submit():
        currentOrder = Order.query.filter_by(id=orderId).first()
        quantity = form.quantity.data
        description = form.description.data
        unitCost = form.unitCost.data
        totalCost = quantity * unitCost
        currentOrder.totalSale += totalCost

        newOrderDetail = OrderDetail(orderId, quantity, description, unitCost, totalCost)
        db.session.add(newOrderDetail)
        db.session.add(currentOrder)
        db.session.commit()
        return redirect(url_for("orderDetails.home", id_order=orderId))
    return render_template("orderDetails/create.html", form=form, user=current_user, orderId=orderId)
