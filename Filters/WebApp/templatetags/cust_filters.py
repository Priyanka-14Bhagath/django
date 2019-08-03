from django import template
register = template.Library()


# def truncate3(value):
#     #custom Filter
#     result = value[0:3]
#     return result

# register.filter('Hello',truncate3)
def truncaten(value, n):
    #custom Filter
    result = value[0:n]
    return result


register.filter('t_n',truncaten)



