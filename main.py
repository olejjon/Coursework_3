import logging

from flask import Flask, send_from_directory, jsonify

from Class.BookmarksDAO import Bookmarks
from Class.CommentsDAO import Comments
from Class.PostDAO import Post
from bookmarks.views import bookmarks_blueprint
from main.views import main_blueprint
from posts.views import posts_blueprint
from search.views import search_blueprint
from tag.views import tag_blueprint
from users.views import users_blueprint

new_logger = logging.getLogger()

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("api.log")

formatter_one = logging.Formatter("%(asctime)s  [ %(levelname)s] %(message)s")
console_handler.setFormatter(formatter_one)

new_logger.addHandler(console_handler)
new_logger.addHandler(file_handler)

main = Flask(__name__)
main.config['JSON_AS_ASCII'] = False

path_posts = "../data/posts.json"
path_comment = "./data/comments.json"
path_bookmarks = "./data/bookmarks.json"

post = Post(path_posts)
comments = Comments(path_comment)
bookmarks = Bookmarks(path_bookmarks, path_posts)

# Регистрируем блюпринт c указанием префикса
main.register_blueprint(main_blueprint)
# main.register_blueprint(api_blueprint, url_prefix='/api')
main.register_blueprint(bookmarks_blueprint, url_prefix='/bookmarks')
main.register_blueprint(posts_blueprint, url_prefix='/posts')
main.register_blueprint(users_blueprint, url_prefix='/users')
main.register_blueprint(search_blueprint, url_prefix='/search')
main.register_blueprint(tag_blueprint, url_prefix='/tag')


# засунул в blueprint, но тест API хз как делать, у блюпринта нет метода config
@main.route("/api/posts")
def api_posts():
    posts = post.get_posts_all()
    return jsonify(posts)


@main.route("/api/posts/<int:post_id>")
def api_post(post_id):
    list_post = post.get_post_by_pk(post_id)
    return jsonify(list_post)


@main.route("/static/img/<path:path>")
def static_dir(path):
    return send_from_directory("image", path)


@main.errorhandler(404)
def page_not_found(e):
    return "<h1>Такой страницы не существует</h1>", 404


@main.errorhandler(500)
def server_error(e):
    return "<h1>Ошибка, возникла на стороне сервера</h1>", 500


if __name__ == "__main__":
    main.run()
