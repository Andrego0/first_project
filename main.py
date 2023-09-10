class Title:
    def __init__(self, title_text, x, y):
        self.title = title_text
        self.x = x
        self.y = y
        self.appear = True
    def print_info(self):
        print("Кнопка", self.title)
        print("Розташування: (", self.x, self.y, ")")
        print("Видимість:", self.appear)

    def hide(self):
        self.appear = False
        print("Напис приховано")


t1 = Title("Hello", 200, 250)
t1.print_info()
t1.hide()     