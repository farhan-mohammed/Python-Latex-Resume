from .General import existsNonEmpty, existsNonEmptyArr


class ExtraCurriculars:
    def __init__(self, data):
        self.title = None
        self.team = None
        self.tools = None
        self.points = []

        if existsNonEmpty(data, "title"):
            self.title = data["title"]
        if existsNonEmpty(data, "team"):
            self.team = data["team"]
        if existsNonEmpty(data, "tools"):
            self.tools = data["tools"]
        if existsNonEmptyArr(data, "points"):
            for point in data["points"]:
                self.addPoints(point)

    def addPoints(self, point: str):
        if point == "":
            return
        self.points.append(point)

    def toLatex(self):
        output = (
            r"\resumeProjectHeading{\textbf{"
            + self.title
            + r"} $|$ \emph{"
            + self.team
            + " "
            + "duration!"
            + r"}}{\small{"
            + self.tools
            + r"}}\resumeItemListStart"
        )
        for point in self.points:
            output += r"\resumeItem{" + point + "}"
        output += r"\resumeItemListEnd"

        return output


class ExtraCurricularsContainer:
    def __init__(self, data):
        self.order = data.get("order", -1)
        self.entries = []
        for entry in data.get("entries", []):
            self.entries.append(ExtraCurriculars(entry))

    def toLatex(self):
        if len(self.entries) == 0:
            return ""

        output = r"\section{Extracurriculars}\resumeSubHeadingListStart"
        for entry in self.entries:
            output += entry.toLatex()
        output += r"\resumeSubHeadingListEnd"
        return output
