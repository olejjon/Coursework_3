from Class.PostDAO import Post

import pytest


@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = Post("../data/posts.json")
    return candidates_dao_instance


keys_should_be = {'content',
 'likes_count',
 'pic',
 'pk',
 'poster_avatar',
 'poster_name',
 'views_count'}


class TestPostDAO:

    def test_get_all(self, candidates_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = candidates_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_pk(self, candidates_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного """
        posts = candidates_dao.get_post_by_pk(1)
        assert posts["pk"] == 1, "возвращается неправильный пост"
        assert set(posts.keys()) == keys_should_be, "неверный список ключей"