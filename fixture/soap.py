from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def convert_projects(self, projects):
        def convert(project):
            return Project(name=project.name, description=project.description, id=str(project.id))
        return list(map(convert, projects))

    def get_project_list(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            return self.convert_projects(client.service.mc_projects_get_user_accessible(username, password))
        except WebFault:
            return None
