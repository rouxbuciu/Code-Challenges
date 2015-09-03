# ==============================
#           CLASSES
# ==============================


class Client(object):

    def __init__(self, first_name, last_name, kind, email, phone, street,
                 city, country, zip_code, survey, projects=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.kind = kind
        self.email = email
        self.phone = phone
        self.survey = survey
        self.projects = projects
        self.street = street
        self.city = city
        self.country = country
        self.zip_code = zip_code


class Project(object):

    def __init__(self, name, date, sessions=[]):
        self.name = name
        self.date = date
        self.sessions = sessions


class Sessions(object):

    def __init__(self, date, service, length, cost):
        self.date = date
        self.service = service
        self.cost = cost
        self.length = length



class Invoice(object):
    pass


class Quote(object):
    pass
