from rest_framework.serializers import ValidationError

allowed_site = 'youtube.com'

def validate_allowed_sites(value):
    if not allowed_site in value.lower():
        raise ValidationError("Разрешено переходить только на youtube.com!")
