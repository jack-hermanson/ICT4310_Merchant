from dataclasses import asdict
from json import JSONDecodeError
from uuid import uuid4

from flask import Blueprint, render_template, redirect, url_for, flash, jsonify

from application.constants import merchant_data
from application.modules.main.forms import CheckoutForm
from application.processor.ProcessorRequest import ProcessorRequest, RequestMerchantData, RequestCard
from application.processor.request_authorization import request_authorization

main = Blueprint("main", __name__, url_prefix="")


@main.route("/make-payment", methods=["GET", "POST"])
def make_payment():
    form = CheckoutForm()
    if form.validate_on_submit():
        try:
            processor_request = ProcessorRequest(
                id=f"auth_{uuid4().__str__()}",
                amount=int(form.amount.data * 100),
                merchant_data=merchant_data,
                currency="usd",
                card=RequestCard(
                    id=form.card_number.data,
                    card_code=form.card_code.data,
                    exp_year=form.exp_year.data,
                    exp_month=form.exp_month.data,
                    name="ICT4310 Instructor",
                    currency="usd",
                ),
            )
            authorization = request_authorization(processor_request)
            return render_template("main/payment-confirmation.html", authorization=authorization)
        except Exception as e:
            flash(f"We couldn't process your request. {e.__str__()}.", category="danger")

    return render_template("main/make-payment.html", form=form)


@main.route("/")
def home():
    return redirect(url_for("main.make_payment"), 301)
