from .education import education, order as order_edu
from .experience import experience, order as order_exp
from .extracurriculars import extracurriculars, order as order_extra
from .resumeprofile import profile as resumeprofile
from .projects import projects, order as order_prj
from .tools import tools, order as order_to
import os
import json


def run():
    output = {}
    # Profile
    output["profile"] = resumeprofile
    # Education
    output["education"] = education
    output["education"]["order"] = order_edu
    # Extracurriculars
    output["extracurriculars"] = {}
    output["extracurriculars"]["entries"] = extracurriculars
    output["extracurriculars"]["order"] = order_exp
    # projects
    output["projects"] = {}
    output["projects"]["entries"] = projects
    output["projects"]["order"] = order_prj
    # experience
    output["experience"] = {}
    output["experience"]["entries"] = experience
    output["experience"]["order"] = order_exp
    # tools
    output["tools"] = {}
    output["tools"]["entries"] = tools
    output["tools"]["order"] = order_to

    parent_directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir)
    )
    build_directory = os.path.join(parent_directory, "build")
    json_file_path = os.path.join(build_directory, "data.json")

    # Save the JSON data to the specified file
    with open(json_file_path, "w") as json_file:
        json.dump(output, json_file)

    print(f"JSON data saved to: {json_file_path}")
