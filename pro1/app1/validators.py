from django.core.exceptions import ValidationError

def validate_image_format(image):
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
    file_extension = image.name.split('.')[-1].lower()
    if file_extension not in valid_extensions:
        raise ValidationError("Unsupported file format. Please upload JPG, JPEG, PNG, or GIF files.")

def validate_image_size(image):
    max_size_in_kb = 100  # Maximum allowed size in KB
    max_size_in_bytes = max_size_in_kb * 1024  # Convert KB to Bytes
    if image.size > max_size_in_bytes:
        raise ValidationError(f"File size exceeds {max_size_in_kb}KB.")
