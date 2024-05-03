from model.project import Project


def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    project = Project(name="Test022", description="Test")
    old_projects = app.soap.get_project_list(username, password)
    app.project.create_project(project)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
