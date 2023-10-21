from .General import Link, existsNonEmpty, existsNonEmptyArr


class Projects:
    def __init__(self, data):
        self.title = data.get("title", None)
        self.tools = data.get("tools", None)
        self.links = []
        self.points = []

        for link in data.get("directs", []):
            self.addLink(Link(link["link"], link.get("name", "")))
        for point in data.get("points"):
            self.addPoint(point)

    def addPoint(self, point: str):
        if point == "":
            return
        self.points.append(point)

    def addLink(self, link: Link):
        self.links.append(link)

    def toLatex(self):
        output = ""
        output += (
            r"\resumeProjectHeading{\textbf{"
            + self.title
            + r"} $|$ \emph{"
            + self.tools
            + "}}"
            + "{"
            + " $|$ ".join(
                [
                    r"\href{" + link.name + r"}{\small \underline{" + link.name + r"}}"
                    for link in self.links
                ]
            )
            + r"}\vspace{-3pt}"
        )
        if len(self.points):
            output += r"\resumeItemListStart"
            for p in self.points:
                output += r"\resumeItem{" + p + "}"
            output += r"\resumeItemListEnd"
        return output


class ProjectsContainer:
    def __init__(self, data):
        self.projects = []
        self.order = data.get("order", -1)
        for prj in data.get("entries", []):
            self.projects.append(Projects(prj))

    def toLatex(self):
        if len(self.projects) == 0:
            return ""
        output = r"\section{Projects}\resumeSubHeadingListStart"
        for prj in self.projects:
            output += prj.toLatex()
        output += r"\resumeSubHeadingListEnd"
        return output
