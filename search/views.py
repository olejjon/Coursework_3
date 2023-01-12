from flask import render_template, Blueprint, request
from Class.PostDAO import Post

# Добавим настройку папки с шаблонами
search_blueprint = Blueprint('search_blueprint', __name__)

path_posts = "./data/posts.json"
post = Post(path_posts)


@search_blueprint.route("/")
def search_posts():
    text_search = request.args['s']
    list_posts = post.search_for_posts(text_search)
    return render_template("search.html", list_posts=list_posts, len_posts=len(list_posts))