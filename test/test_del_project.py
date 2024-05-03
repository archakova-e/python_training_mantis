from model.project import Project
import random


def test_del_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    if len(old_projects) == 0:
        app.project.create(Project(name="Test1", description="Test1"))
        old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    old_projects.remove(project)
    app.project.del_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
