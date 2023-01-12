import json
import re


class Post:

    def __init__(self, path_file):
        self.path_file = path_file

    def __repr__(self):
        return f"Путь {self.path_file}"

    def get_posts_all(self):
        """Получает список всех постов"""
        with open(self.path_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_by_user(self, user_name):
        """Получает пост по имени юзера"""
        data = self.get_posts_all()
        list_posts = []
        try:
            for post in data:
                if user_name.lower() in post["poster_name"].lower():
                    list_posts.append(post)
            return list_posts

        except ValueError:
            return "Список постов пустой"

    def search_for_posts(self, query, list_posts=[], new_list=[]):
        """Ищет посты по словам"""
        data = self.get_posts_all()
        for post in data:
            if query.lower() in post['content'].lower():
                list_posts.append(post)

        if len(list_posts) > 10:
            for i in range(0, 9):
                new_list.append(list_posts[i])
            return new_list
        else:
            return list_posts

    def get_post_by_pk(self, pk):
        """Получает пост по номеру pk"""
        data = self.get_posts_all()
        for post in data:
            if post['pk'] == pk:
                return post

    def search_hashtag(self, post):
        """Получает список всех хештегов без знака"""
        list_hashtags = []
        if post['content'].find("#") > 0:
            hashtags = re.findall(r'(#\w+)', post['content'])
            for hashtag in hashtags:
                list_hashtags.append(hashtag.replace("#", ""))
        return list_hashtags

    def search_hashtag_posts(self, tag):
        """Получает список всех хештегов без знака"""
        data = self.get_posts_all()
        list_posts = []
        for post in data:
            if "#" + tag in post["content"]:
                list_posts.append(post)
        return list_posts
