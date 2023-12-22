about = {"Имя": "Данила", "Возраст": "16", "Город": "Москва"}
hobby = {"*Баскетбол*": "Я несколько лет занимался баскетболом, сейчас играю как любитель.", "*Компьютерные игры*": "Люблю играть в компьютерные игры разных жанров, в основном в многопользовательские выживания, песочницы и шутеры", "*Программирование на Python*": "Программирую несколько лет, планирую дальше развиваться в этом направлении.", "*Музыка*": "Люблю петь, играю на гитаре и пианино."}

def about_me(about1):
    about_in_text = ""
    for i in about1:
        about_in_text += i
        about_in_text += ": "
        about_in_text += about1[i]
        about_in_text += "\n"
    return about_in_text

def my_hobby(hobby1):
    hobby_in_text = ""
    for i in hobby1:
        hobby_in_text += i
        hobby_in_text += "\n"
        hobby_in_text += hobby1[i]
        hobby_in_text += "\n"
    return hobby_in_text

def show_about():
    return about_me(about)

def show_hobby():
    return my_hobby(hobby)