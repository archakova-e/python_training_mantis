from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath("//select[@name='" + field_name + "']/option[@value='" + text + "']").click()

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.select_field_value("status", project.status)
        self.select_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.open_project_page()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            projects_list = wd.find_elements_by_css_selector(".width100 tr[class*='row']:not([class='row-category'])")
            for item in projects_list:
                properties = item.find_elements_by_css_selector("td")
                name = properties[0].find_element_by_css_selector("a").text
                status = properties[1].text
                view_state = properties[3].text
                description = properties[4].text
                href = properties[0].find_element_by_css_selector("a").get_attribute("href")
                index = href.find('=') + 1
                id = href[index:]
                self.project_cache.append(Project(name=name, status=status, view_state=view_state,
                                                  description=description, id=id))
        return list(self.project_cache)

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[@href="manage_proj_edit_page.php?project_id=%s"]' % id).click()

    def del_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath('//input[@value="Delete Project"]').click()
        wd.find_element_by_xpath('//input[@value="Delete Project"]').click()
        self.project_cache = None
