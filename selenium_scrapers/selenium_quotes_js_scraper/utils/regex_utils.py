import re


class RegexUtils:

    @staticmethod
    def getting_valid_options(option):
        expression = '[-]+'
        option_text = option.text.strip()
        if re.match(expression, option_text):
            return False
        return True
