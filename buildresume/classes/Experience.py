from .General import Duration, existsNonEmpty, existsNonEmptyArr


class Experience:
    def __init__(self, data):
        self.company = data.get("company", None)
        self.title = data.get("title", None)
        self.team = data.get("team", None)
        self.duration = None
        self.location = data.get("location", None)
        self.points = []

        # TODO: add checks here
        if existsNonEmpty(data, "start") and existsNonEmpty(data, "end"):
            self.duration = Duration(data["start"], data["end"])

        for point in data.get("points", []):
            if point == "":
                continue
            self.points.append(point)

    def toLatex(self):
        combinedTitle = self.title
        if self.team:
            combinedTitle += "- " + self.team
        output = (
            r"\resumeSubheading{"
            + combinedTitle
            + "}{"
            + " -- ".join(self.duration.toString())
            + "}{"
            + self.company
            + "}{"
            + self.location
            + "}"
        )
        output += r"\resumeItemListStart"
        for point in self.points:
            output += r"\resumeItem{" + point + "}"

        output += r"\resumeItemListEnd"
        return output


class ExperienceContainer:
    def __init__(self, data):
        self.order = data.get("order", -1)
        self.experiences = []
        for entry in data.get("entries", []):
            self.experiences.append(Experience(entry))

    def toLatex(self):
        if len(self.experiences) == 0:
            return ""
        output = r"\section{Experience}\resumeSubHeadingListStart"
        for exp in self.experiences:
            output += exp.toLatex()
        output += r"\resumeSubHeadingListEnd"
        return output
