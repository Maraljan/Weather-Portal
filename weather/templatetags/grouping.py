from django import template

register = template.Library()


@register.filter(name='grouping_by_n')
def group_by_n(list_: list, n: int) -> list[list]:
    result = []
    temporary_list = []
    for j in list_:
        temporary_list.append(j)
        if len(temporary_list) == n:
            result.append(temporary_list)
            temporary_list = []
    if temporary_list:
        result.append(temporary_list)
    return result
