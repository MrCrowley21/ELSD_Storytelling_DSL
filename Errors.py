# define the basic error class that contains its name and details about the error
class Error(Exception):
    def __init__(self, error_name, line, details):
        self.error_name = error_name
        self.line = line
        self.details = details


# defines syntax errors
class MySyntaxError(Error):
    def __init__(self, line, details):
        super().__init__(f'Syntax Error', line, details)

    # defines output format
    def __str__(self):
        return f'Syntax error. Line {self.line}: {self.details}'


# defines illegal instances appearance
class IllegalNameError(Error):
    def __init__(self, line, details):
        super().__init__(f'Illegal Name Error', line, details)

    # defines output format
    def __str__(self):
        return f'IllegalNameError. Line {self.line}: Illegal name "{self.details}" found'


# defines variable multiple initialization error
class InitiationError(Error):
    def __init__(self, line, details):
        super().__init__(f'Initiation Error', line, details)

    # defines output format
    def __str__(self):
        return f'InitiationError. Line {self.line}: "{self.details}" is already defined'


# defines illegal instances appearance
class ReferencesError(Error):
    def __init__(self, line):
        self.line = line

    # defines output format
    def __str__(self):
        return f'ReferenceError. Line {self.line}: "Not a valid path described'


# defines illegal name of identifiers
class IdentifierError(Error):
    def __init__(self, line, details):
        super().__init__('Illegal Name Error', line, details)

    # defines output format
    def __str__(self):
        return f'IdentifierError. Line {self.line}: Expected identifier name. Found: "{self.details}"'


# defines wrong type of token
class MyTypeError(Error):
    def __init__(self, line, expected_type, real_type):
        self.line = line
        self.expected_type = expected_type
        self.real_type = real_type

    # defines output format
    def __str__(self):
        return f'TypeError. Line {self.line}: Expected token of type {self.expected_type}. Found: {self.real_type}'


# defines wrong converting type
class ConvertingError(Error):
    def __init__(self, line, value, type):
        self.line = line
        self.value = value
        self.type = type

    # defines output format
    def __str__(self):
        return f'ConvertingError. Line {self.line}: Error converting {self.value} to {self.type}'
