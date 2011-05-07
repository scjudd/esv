from django import template

def esv_popout(value):
  "Replaces a given passage with javascript lookup code"
  return "<a href=\"#\" onclick=\"esv_popout(%s);\">%s</a>" % (value, value)
esv_popout.is_safe = True

register = template.Library()
register.filter('esv_popout', esv_popout)
