from django import template
from re import compile, findall
from string import capwords
register = template.Library()

@register.filter(name="get_attr")
def get_attr(value, arg):
    result = getattr(value, str(arg))
    if callable(result):
        temp = []
        for item in result.all():
            temp.append(item.name)
        if len(temp) > 1:
            result = ', '.join(temp)
        elif len(temp) == 1:
            result = temp[0]
        else:
            result = ''
    return result



@register.filter(name="titlize")
def titlize(value):
    first_cap = compile('(.)([A-Z][a-z]+)')
    all_caps = compile('([a-z0-9])([A-Z])')
    temp = first_cap.sub(r'\1 \2', value)
    value = all_caps.sub(r'\1 \2', temp)
    pattern = compile("[\W_\d]+")
    value = pattern.sub(' ', value)
    return capwords(value)

@register.filter(name="elem")
def elem(value, arg):
    return value[arg]

@register.filter(name="getrel")
def getrel(val, arg):
    def get_repr(value):
        if callable(value):
            return '%s' % value()
        return value

    def get_field(instance, field):
        field_path = field.split('.')
        attr = instance
        for elem in field_path:
            try:
                attr = getattr(attr, elem)
            except AttributeError:
                return None
        return attr

    return get_repr(get_field(val, arg))
