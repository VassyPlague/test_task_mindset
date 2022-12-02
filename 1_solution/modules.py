rus_chars_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def return_upper(doc):
    ret_str = ''

    for i in doc:
        if i == i.upper() and i in rus_chars_upper:
            ret_str += i
        if i == ' ':
            ret_str += i
    return ret_str

def cleaner(doc):
    cleaned = ''
    for i in doc:
        if i in rus_chars_upper:
            cleaned += i
        else:
            cleaned += ' '
    return cleaned

def split_all_names(doc):
    returned = []
    for i in doc.split():
        if len(i) > 4:
            returned.append(i)
    return returned[0:3]

def return_all_names(doc):
    cleaned = cleaner(doc)
    upper = return_upper(cleaned)
    names = split_all_names (upper)
    return " ".join(names)

