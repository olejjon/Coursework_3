import pytest
#from api.views import api_blueprint
from main import main
from Class.PostDAO import Post
from Class.CommentsDAO import Comments
from Class.BookmarksDAO import Bookmarks


main.config['JSON_AS_ASCII'] = True

path_posts = "../data/posts.json"
path_comment = "../data/comments.json"
path_bookmarks = "../data/bookmarks.json"

post = Post(path_posts)
comments = Comments(path_comment)
bookmarks = Bookmarks(path_bookmarks, path_posts)

keys_should_be = {'content',
 'likes_count',
 'pic',
 'pk',
 'poster_avatar',
 'poster_name',
 'views_count'}


@pytest.mark.parametrize("test_input, expected", [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
def test_comment_id(test_input, expected):
    assert comments.get_comments_by_post_id(test_input)[0]["post_id"] == expected


def test_search_hashtag():
    data = post.get_posts_all()
    assert post.search_hashtag(data[4])[0] == "кот", "Такого хештега нет"
    assert post.search_hashtag(data[4])[1] == "котики", "Такого хештега нет"
    assert post.search_hashtag(data[4])[2] == "инста", "Такого хештега нет"


#В курсе не было написно про тестирование блюпринтов. В интернете не успел "нарыть" инфы
def test_api_posts():
    #response = api_blueprint.test_client().get('/api/posts')
    response = main.test_client().get('/api/posts')
    assert set(response.json[0].keys()) == keys_should_be, "неверный список ключей"
    assert type(response.json) is list


#В курсе не было написно про тестирование блюпринтов. В интернете не успел "нарыть" инфы
def test_api_post():
    post_id = 1
    #response = api_blueprint.test_client().get(f'/api/posts/{post_id}')
    response = main.test_client().get(f'/api/posts/{post_id}')
    assert set(response.json.keys()) == keys_should_be, "неверный список ключей"
    assert type(response.json) is dict
