class Div:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, func):
        def wrap(*args, **kwargs):
            print(f"<div class=*{self.arg}*>")
            result = func(*args, **kwargs)
            print("</div>")
            return result

        return wrap


def body(func):
    def wrap(*args, **kwargs):
        print("<body>")
        result = func(*args, **kwargs)
        print("</body>")
        return result

    return wrap


class Head:
    def __init__(self, str_to_insert):
        self.str_to_insert = str_to_insert

    def __call__(self, func):
        def wrap(*args, **kwargs):
            print(f'<head>\n'
                  f'<title>{self.str_to_insert}</title>\n'
                  f'</head>')
            result = func(*args, **kwargs)
            return result

        return wrap


def html_decor(func):
    def wrap(*args, **kwargs):
        print('<html>')
        result = func(*args, *kwargs)
        print('</html>')
        return result

    return wrap


@html_decor
@Head('Users')
@body
@Div('users_block')
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>"
    template = "<p> {} </p>"
    print(template_head)
    for i in names_list:
        print(template.format(i))


names = ['Misha', 'Olya', 'Vitaliy', 'Vita']

get_names_page(names)
