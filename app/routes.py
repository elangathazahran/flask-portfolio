from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Portfolio
from app.forms import PortfolioForm
import os

main = Blueprint("main", __name__)


@main.route("/")
def home():
    portfolios = Portfolio.query.all()
    return render_template("index.html", portfolios=portfolios)


@main.route("/admin/create", methods=["GET", "POST"])
def create():
    form = PortfolioForm()
    if form.validate_on_submit():
        image_file = form.image.data

        filename = ""
        if image_file:
            filename = image_file.filename
            image_path = os.path.join("app", "static", "images", filename)
            image_file.save(image_path)

        new_item = Portfolio(
            title=form.title.data,
            category=form.category.data,
            description=form.description.data,
            image=filename,
            live_link=form.live_link.data,
            github_link=form.github_link.data,
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("main.home"))

    return render_template("create.html", form=form)


@main.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    item = Portfolio.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("main.home"))
