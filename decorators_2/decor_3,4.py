class Div:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, func):
        def wrap(*args, **kwargs):
            new_str = ''
            new_str += f"<div class=*{self.arg}*>\n"
            result = func(*args, **kwargs)
            new_str += result
            new_str += "</div>\n"
            return new_str

        return wrap


def body(func):
    def wrap(*args, **kwargs):
        new_str = ''
        new_str += "<body>\n"
        result = func(*args, **kwargs)
        new_str += result
        new_str += "</body>\n"
        return new_str

    return wrap


class Head:
    def __init__(self, str_to_insert):
        self.str_to_insert = str_to_insert

    def __call__(self, func):
        def wrap(*args, **kwargs):
            new_str = ''
            new_str += f'<head>\n' + f'<title>{self.str_to_insert}</title>\n' + f'</head>\n'
            result = func(*args, **kwargs)
            new_str += result
            return new_str

        return wrap


def html_decor(func):
    def wrap(*args, **kwargs):
        new_str = ''
        new_str += '<html>\n'
        result = func(*args, *kwargs)
        new_str += result
        new_str += '</html>\n'
        return new_str

    return wrap


@html_decor
@Head('Users')
@body
@Div('users_block')
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>\n"
    template = "<p> {} </p>\n"
    new_str = ''
    new_str += template_head
    for i in names_list:
        new_str += template.format(i)
    return new_str


names = ['Misha', 'Olya', 'Vitaliy', 'Vita']

print(get_names_page(names))
