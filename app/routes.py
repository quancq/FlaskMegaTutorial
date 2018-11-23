from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "QuanCQ"}

    posts = [
        ("DungBV", "Mai hop nhom nhe cac thanh nien"),
        ("LongLV", "OK, gio lam btl đã")
    ]

    posts = [
        {
            "author": {"username": post[0]},
            "body": post[1]
        }
        for post in posts
    ]

    return render_template("index.html", title="HelloWorld App", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me = {}".format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))

    return render_template("login.html", title="Sign In", form=form)
