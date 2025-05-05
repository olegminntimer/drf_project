from rest_framework.serializers import ValidationError

allowed_site = "youtube.com"


def validate_allowed_sites(value):
    if allowed_site not in value.lower():
        raise ValidationError("Разрешено переходить только на youtube.com!")
