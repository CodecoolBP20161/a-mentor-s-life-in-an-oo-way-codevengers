from person import Person


class Candidate(Person):
    def __init__(self, application_code, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application_code = application_code
        self.accepted = False
