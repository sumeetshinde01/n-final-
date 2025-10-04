import re
from flask import flash

def is_valid_email(email):
    """Simple email validator using regex."""
    regex = r'^[^@]+@[^@]+\.[^@]+$'
    return re.match(regex, email) is not None

def flash_errors(form):
    """Flash all errors for a given WTForm."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')

def to_title_case(s):
    """Convert string to title case."""
    return s.title()

def truncate_text(s, length=100):
    """Truncate text if longer than length."""
    return s if len(s) <= length else s[:length] + "..."

# Add more helpers as needed!
