from rest_framework.serializers import ValidationError


allowed_site = "youtube.com"

def validate_allowed_sites(value):
    if not allowed_site in value:
        raise ValidationError("Запрещенная ссылка!")
