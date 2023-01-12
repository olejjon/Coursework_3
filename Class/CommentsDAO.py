import json


class Comments:

    def __init__(self, path_file):
        self.path_file = path_file

    def __repr__(self):
        return f"Путь {self.path_file}"

    def get_comments(self):
        """Получает все комменты по постам"""
        with open(self.path_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id):
        """Получает комменты по посту"""
        data = self.get_comments()
        list_comments = []
        try:
            for comment in data:
                if comment["post_id"] == post_id:
                    list_comments.append(comment)

            return list_comments
        except ValueError:
            return "Список комментариев пустой"