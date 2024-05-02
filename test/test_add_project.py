from model.project import Project


def test_add_project(app):
    project = Project(name="Test9", description="Test9")
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
