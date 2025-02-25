from flask import Blueprint, render_template, redirect, url_for, request

from application.modules.main.forms import CheckoutForm

main = Blueprint("main", __name__, url_prefix="")


@main.route("/make-payment", methods=["GET", "POST"])
def make_payment():
    form = CheckoutForm()
    if form.validate_on_submit():
        return "valid!"
    elif request.method == "GET":
        pass
    return render_template("main/make-payment.html", form=form)


@main.route("/")
def home():
    return redirect(url_for("main.make_payment"), 301)
