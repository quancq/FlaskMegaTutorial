from app import app
from flask import render_template


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
