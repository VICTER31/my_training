calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    strinfo = []
    strinfo.append(len(string))
    strinfo.append((string).upper())
    strinfo.append((string).lower())
    strinfo = tuple(strinfo)
    count_calls()
    return strinfo

def is_contains(string, list_to_search):
    contains = False
    for i in list_to_search:
        if string.lower() == i.lower():
            contains = True
    count_calls()
    return contains

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)