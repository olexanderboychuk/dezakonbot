class Zakon:
    pass


class RegisteredZakon(Zakon):

    def __init__(self, zakon_id, zakon_date, zakon_name, zakon_authors):
        self.id = zakon_id
        self.date = zakon_date
        self.name = zakon_name
        self.authors = zakon_authors

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "name": self.name,
            "authors": self.authors
        }

class AcceptedZakon(Zakon):
    def __init__(self, zakon_id, zakon_date, zakon_name, number_act, date_act):
        self.id = zakon_id
        self.date = zakon_date
        self.name = zakon_name
        self.number_act = number_act
        self.date_act = date_act

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "name": self.name,
            "number_act": self.number_act,
            "date_act": self.date_act
        }