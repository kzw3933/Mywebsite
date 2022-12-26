from django.urls import register_converter

class TwointConvert:
    regex = r'\d\d'

    def to_python(self, value):
        return int(value)*2

    def to_url(self, value):
        return value

register_converter(TwointConvert, 'twoint')