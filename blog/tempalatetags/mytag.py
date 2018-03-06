from django import Template

register = template.library()


@register.simple_tag
def url_replace(request, field, value):
    """GETパラメーターを一部を置き換える。"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urllencode()