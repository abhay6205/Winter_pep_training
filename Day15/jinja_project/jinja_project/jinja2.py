from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    # Add any custom filters, tests, or globals here if needed
    return env