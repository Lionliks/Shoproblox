IMT_DICT = {lambda x: x <= 16: "Выраженный дефицит массы тела",
            lambda x: 16 < x < 18.5: "Недостаточная (дефицит) масса тела", lambda x: 18.5 <= x <= 25: "Норма",
            lambda x: 25 < x <= 30: "Избыточная масса тела (предожирение)",
            lambda x: 30 < x <= 35: "Ожирение 1 степени", lambda x: 35 < x <= 40: "Ожирение 2 степени",
            lambda x: 40 < x: "Ожирение 3 степени"}
GENDER_DICT = {"male": "Мужской", "female": "Женский"}
LEVEL_OF_ACTIVITIES_LIST = [{"title": "Минимальный", "ratio": 1.2}, {"title": "Низкий", "ratio": 1.375},
                            {"title": "Средний", "ratio": 1.55}, {"title": "Высокий", "ratio": 1.725},
                            {"title": "Очень высокий", "ratio": 1.9}]
FOOD_GROUP_DICT = {"breakfast": "завтрак", "lunch": "обед", "dinner": "ужин", "snack": "перекус"}

TXT_START = "id; chat_id; name; username; height; weight; age; born_date; gender; level_of_activities; end_message; register_datetime; register_date; last_message"
JSON_KEYS = ["id", "chat_id", "name", "username", "height", "weight", "age", "born_date", "gender",
             "level_of_activities", "end_message", "register_datetime", "register_date", "last_message"]


class Categories1:
    width = 2
    height = 3


class Categories2:
    width = 2
    height = 3


class Products:
    width = 2
    height = 4


class AnswerProductsSearch:
    width = 2
    height = 4


class RecipesCategories1:
    width = 2
    height = 3


class Recipes:
    width = 2
    height = 4


class AnswerRecipesSearch:
    width = 2
    height = 4


class Favourties:
    width = 2
    height = 4


class LastMailings:
    width = 2
    height = 4


class BlockUsers:
    width = 2
    height = 4
