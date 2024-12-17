from django import template
from django.forms.boundfield import BoundField

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to a form field
    Usage: {{ form.field|add_class:"my-class" }}
    """
    if isinstance(value, BoundField):
        existing_classes = value.field.widget.attrs.get('class', '')
        new_classes = f"{existing_classes} {arg}".strip()
        value.field.widget.attrs['class'] = new_classes
    return value
