from .General import Link, existsNonEmpty, existsNonEmptyObj


class Profile:
    def __init__(self, data: str):
        self.name = data.get("name", "John Doe")
        self.email = data.get("email", None)
        self.phone = data.get("phone", None)

        self.linkedin = None
        self.github = None
        self.url = None

        if existsNonEmpty(data, "linkedin") and existsNonEmptyObj(data, "linkedin"):
            linkData = data["linkedin"]
            self.linkedin = Link(linkData["link"], linkData.get("name", ""))
        if existsNonEmpty(data, "github") and existsNonEmptyObj(data, "github"):
            githubData = data["github"]
            self.github = Link(githubData["link"], githubData.get("name", ""))
        if existsNonEmpty(data, "url") and existsNonEmptyObj(data, "url"):
            linkData = data["url"]
            self.github = Link(linkData["link"], linkData.get("name", ""))

    def toLatex(self):
        out = r"\begin{center} \textbf{\Huge \scshape " + self.name + "}"
        contacts = []
        if self.phone:
            contacts.append(r"\small " + self.phone)
        if self.email:
            contacts.append(
                r"\href{mailto:" + self.email + r"}{\uline{" + self.email + r"}}"
            )
        if self.linkedin:
            contacts.append(
                r"\href{"
                + self.linkedin.link
                + r"}{\uline{"
                + self.linkedin.name
                + r"}}"
            )
        if self.github:
            contacts.append(
                r"\href{" + self.github.link + r"}{\uline{" + self.github.name + r"}}"
            )
        if len(contacts):
            out += r"\\ \vspace{5pt} " + " $|$ ".join(contacts) + r"\end{center}"
        return out
