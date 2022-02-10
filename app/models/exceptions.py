class InvalidPhone(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = 400
        self.message = {'error': 'phone must follow this format: (xx)xxxxx-xxxx'}


class InvalidValue(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = 400
        self.message = {"error": "All values must be string type"}

class NothingHere(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = 200
        self.message = []
