from flask import render_template, Blueprint
from Class.PostDAO import Post

# Добавим настройку папки с шаблонами
users_blueprint = Blueprint('users_blueprint', __name__)

path_posts = "./data/posts.json"
post = Post(path_posts)


@users_blueprint.route("/<username>")
def search_username(username):
    list_username = post.get_posts_by_user(username)
    return render_template("user-feed.html", list_username=list_username, username=username)

