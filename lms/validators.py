from rest_framework.serializers import ValidationError

allowed_sites = ['youtube.com',]

def validate_allowed_sites(value):
    if not value.lower() in allowed_sites:
        raise ValidationError("Разрешено переходить только на youtube.com!")
