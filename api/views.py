from flask import Blueprint, jsonify
from Class.PostDAO import Post

# Добавим настройку папки с шаблонами
api_blueprint = Blueprint('api_blueprint', __name__)

path_posts = "./data/posts.json"

post = Post(path_posts)


@api_blueprint.route("/posts")
def api_posts():
    posts = post.get_posts_all()
    return jsonify(posts)


@api_blueprint.route("/posts/<int:post_id>")
def api_post(post_id):
    list_post = post.get_post_by_pk(post_id)
    return jsonify(list_post)
