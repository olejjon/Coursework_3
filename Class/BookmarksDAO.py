import json


class Bookmarks:

    def __init__(self, path_file, path_file_posts):
        self.path_file = path_file
        self.path_file_posts = path_file_posts

    def __repr__(self):
        return f"Путь {self.path_file}"

    def get_bookmarks(self):
        """Получает все закладки"""
        with open(self.path_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def add_bookmarks(self, post_pk):
        """Добавляет пост в закладки"""
        data_bookmarks = json.load(open(self.path_file, "r", encoding="utf-8"))
        with open(self.path_file_posts, "r", encoding="utf-8") as file:
            data_posts = json.load(file)
        for post in data_posts:
            if post["pk"] == post_pk:
                data_bookmarks.append(post)
        with open(self.path_file, "w", encoding="utf-8") as file:
            json.dump(data_bookmarks, file, indent=2, ensure_ascii=False)

    def remove_bookmarks(self, post_pk):
        """Удаляет пост из закладок"""
        data = json.load(open(self.path_file))
        for post in data:
            if post["pk"] == post_pk:
                data.remove(post)
        with open(self.path_file, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)