def generate_class_not_found_exception():
    try:
        from non_existent_module import NonExistentClass
    except ImportError:
        print("Import error handled")

generate_class_not_found_exception()

