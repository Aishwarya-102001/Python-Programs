favorite_languages={
    'jen':    ['python','ruby'],
    'sarah':  ['C','python'],
    'edward': ['C++','C'],
    'john':   ['java','C++'],
    'jenny':  ['ruby','C']
}    #nesting lists inside a dictionary

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"{language.title()}")

#**************Nesting a dictionary in a dictionary is possible but makes the code complicated**********#