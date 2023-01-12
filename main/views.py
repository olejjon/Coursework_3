from flask import Blueprint, render_template
from Class.PostDAO import Post
from Class.BookmarksDAO import Bookmarks

main_blueprint = Blueprint('main_blueprint', __name__)

path_posts = "./data/posts.json"
path_bookmarks = "./data/bookmarks.json"

post = Post(path_posts)
bookmarks = Bookmarks(path_bookmarks, path_posts)


@main_blueprint.route("/")
def page_index():
    posts = post.get_posts_all()
    list_bookmarks = bookmarks.get_bookmarks()
    return render_template("index.html", posts=posts, len_bookmarks=len(list_bookmarks))