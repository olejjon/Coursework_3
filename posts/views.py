from flask import render_template, Blueprint, jsonify
from Class.PostDAO import Post
from Class.CommentsDAO import Comments

# Добавим настройку папки с шаблонами
posts_blueprint = Blueprint('posts_blueprint', __name__)

path_posts = "./data/posts.json"
path_comment = "./data/comments.json"
path_bookmarks = "./data/bookmarks.json"

post = Post(path_posts)
comments = Comments(path_comment)


@posts_blueprint.route("/<int:postid>")
def profile(postid):
    list_comments = comments.get_comments_by_post_id(postid)
    post_by_pk = post.get_post_by_pk(postid)
    list_hashtags = post.search_hashtag(post_by_pk)
    return render_template("post.html", comments=list_comments, post=post_by_pk, len_comment=len(list_comments), pk=postid,
                           list_hashtags=list_hashtags)