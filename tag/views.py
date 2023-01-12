from flask import render_template, Blueprint
from Class.PostDAO import Post

# Добавим настройку папки с шаблонами
tag_blueprint = Blueprint('tag_blueprint', __name__)

path_posts = "./data/posts.json"

post = Post(path_posts)


@tag_blueprint.route("/<tag>")
def tag(tag):
    list_posts = post.search_hashtag_posts(tag)
    return render_template("tag.html", list_posts=list_posts, tag=tag)
