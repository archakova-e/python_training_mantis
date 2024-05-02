from model.project import Project
import random


def test_del_project(app):
    old_projects = app.project.get_project_list()
    if len(old_projects) == 0:
        app.project.create(Project(name="Test1", description="Test1"))
        old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    old_projects.remove(project)
    app.project.del_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
