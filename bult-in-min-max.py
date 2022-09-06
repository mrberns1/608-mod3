def maximum (value1, value2, value3):
    """Return the maximum of three values"""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

def min(value1, value2, value3):
    """Return the minimum of three values"""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value

print(maximum (12, 27, 36))


print(maximum(12.3, 45.6, 9.7))


print(maximum('yellow', 'red', 'orange'))


print(min(16, 89, 23))

print(min('dotson', 'poodle', 'sheperd'))

#missybernskoetter

