from flask import Blueprint, redirect, render_template
from Class.BookmarksDAO import Bookmarks

# Добавим настройку папки с шаблонами
bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__)
path_bookmarks = "./data/bookmarks.json"
path_posts = "./data/posts.json"
bookmarks = Bookmarks(path_bookmarks, path_posts)


@bookmarks_blueprint.route("/")
def bookmarks_all():
    list_posts = bookmarks.get_bookmarks()
    return render_template("bookmarks.html", list_posts=list_posts)


@bookmarks_blueprint.post("/add/<int:post_id>")
def bookmarks_add(post_id):
    bookmarks.add_bookmarks(post_id)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/remove/<int:post_id>")
def bookmarks_remove(post_id):
    bookmarks.remove_bookmarks(post_id)
    return redirect("/", code=302)
