import os
import json
from .classes.Profile import Profile
from .classes.Education import Education
from .classes.Tools import ToolContainer as Tools
from .classes.Experience import ExperienceContainer as Experience
from .classes.Extracurriculars import ExtraCurricularsContainer as ExtraCurriculars
from .classes.Projects import ProjectsContainer as Projects

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
data_file_path = os.path.join(parent_directory, "build", "data.json")


def run():
    data = {}
    if not os.path.exists(data_file_path):
        raise FileNotFoundError("The 'data.json' file does not exist.")
    with open(data_file_path, "r") as json_file:
        data = json.load(json_file)
        education = Education(data["education"])
        tools = Tools(data["tools"])
        profile = Profile(data["profile"])
        extracurriculars = ExtraCurriculars(data["extracurriculars"])
        projects = Projects(data["projects"])
        experience = Experience(data["experience"])
        allData = [education, tools, experience, projects, extracurriculars]
        return profile.toLatex() + "".join(
            [x.toLatex() for x in sorted(allData, key=lambda x: x.order)]
        )
