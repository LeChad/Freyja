from django.core.exceptions import ValidationError
def validate_image(image):
    file_size_limit = 10 * 1024 * 1024 ## 10mb limit
    if image.file.size > file_size_limit:
        raise ValidationError(f"Maximum photograph size limit is 10mb")