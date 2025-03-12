class CustomException(Exception):
    pass

def throw_custom_exception():
    raise CustomException("Custom exception message")

try:
    throw_custom_exception()
except CustomException as e:
    print(e)