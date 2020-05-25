import re

"""
Regular Expressions Shorthand Character Sets

\\d    Digit [0-9]
\\D    Non-digit [^0-9]
\\w    Alphanumeric character [a-zA-Z0-9_]
\\W    Non-alphanumeric character [^a-zA-Z0-9_]
\\s    Whitespace character [\t\n\r]
\\S    Non-whitespace [^\\s]


Dot(.)           . is used to get one word before dot(.) except \n with all after it
Question(?)      ? is used to represent (Optional) zero or one repeated character(s) before it
Plus(+)          + is used to represent more like that preceding it
Asterisk(*)      * is used to get zero or one repetition character(s)
Pipe(|)          | is used to represent connectivity with other character(s)

()               Parentheses() means gets the value from the parentheses
[]               Square Brackets[] means only one digit inside it like [0-9] or [a-z]



You just need to write type single slash like \t just wrote \\ to indicate single slash


"""


def get_phone_numbers(string):
    regex = re.compile(r'(\d\d\d\d\d\d\d\d\d\d)')    # Number
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def get_phone_numbers_with_optional(string):
    regex = re.compile(r'(\+\d+)?(\d\d\d\d\d\d\d\d\d\d)')    # Optional is mentioned as (something)?
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def get_phone_numbers_with_country_code(string):
    regex = re.compile(r'(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)')         # Grouping
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def get_emails(string):
    regex = re.compile(r'\D\w+@\w+.\w+')      # Email
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def get_emails_with_multiple_dots(string):
    regex = re.compile(r'\D\w+@\w.\w+.\w+.\w+')  # Email with multiple dots like helloworld@gmail.ac.in
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def get_correct_emails(string):
    regex = re.compile(r'(\D\w+@\w+)(.com|.in|.co.uk|.us|.ac.in|.co.in)')  # Only specified using | (No spaces)
    match = regex.findall(string)

    get = []

    if match:
        for matched in match:
            get.append(matched[0]+matched[1])
        return get

    else:
        return None


def get_multiple_repeated_word(string):
    regex = re.compile(r'(ha)*')  # asterisk(*) is used to get a word like hahahaha......
    match = regex.search(string)

    if match:
        return match.group()
    else:
        return None


def starting_with(string):
    regex = re.compile(r'^Good')   # caret(^) symbol is used to identify something starting with that like
    match = regex.search(string)   # Good Morning  (We can use anything like \d, \w, \D etc instead Good)

    if match:
        return match.group()
    else:
        return None


def ending_with(string):
    regex = re.compile(r'You$')   # dollar($) symbol is used to identify something ending with that like
    match = regex.search(string)  # ....Thank You  (We can use anything like \d, \w, \D etc instead You)

    if match:
        return match.group()
    else:
        return None


def n_words_with(string):
    regex = re.compile(r'\w+.man')         # like Iron man, Superman, Batman etc it shows total word
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def word_with(string):
    regex = re.compile(r'.man')   # dot(.) is used to get one word before dot(.) with all after it =>
    # We can use (\w+.man)                ex: .at (mat, hat etc)    we can use just dot(.) in gmail.com by \. to get
    match = regex.findall(string)      # => like Ironman, Superman, Batman etc

    if match:                          # This takes all characters like $, #, % etc except \n
        return match
    else:
        return None


def total_string(string):
    regex = re.compile(r'.*')     # dot(.) means one word before it and asterisk(*) means repeated
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def all_letters(string):
    regex = re.compile(r' *.')    # dot(.) means one word before it and asterisk(*) means any char repeated
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def string_with_symbols(string):
    regex = re.compile(r'<\w+>')    # ex: <something> then something with <> returned, we can use {}, () etc
    match = regex.findall(string)

    if match:
        return match
    else:
        return None


def get_all_tags(string):
    regex = re.compile(r'<\w+')
    match = regex.findall(string)

    if match:
        for index, tag in enumerate(match):
            tag = str(tag).replace('<', '')
            print(index, tag)
    else:
        return None


data = get_correct_emails("helloworld@gmail.com")
print(data)
