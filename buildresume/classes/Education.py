from datetime import datetime
from .General import existsNonEmpty, Duration


class Education:
    def __init__(self, data):
        self.degree = data.get("degree", None)
        self.date = None
        self.school = data.get("school", None)
        self.gpa = data.get("gpa", None)
        self.order = data.get("order", -1)

        if existsNonEmpty(data, "date"):
            self.date = datetime(data["date"][0], data["date"][1], 1)

    def toLatex(self):
        output = (
            r"\section{Education}\resumeSubHeadingListStart\resumeSubheading{"
            + self.degree
            + r"}{"
            + Duration.dateToString(self.date)
            + r"}{"
            + self.school
            + "}"
            + ("{GPA: " + self.gpa + "}" if self.gpa else "{}")
            + r"\resumeSubHeadingListEnd"
        )
        return output
