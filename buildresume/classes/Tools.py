from .General import existsNonEmpty


class Tools:
    def __init__(self, data):
        self.name = data.get("topic", "Tools")
        self.tools = data.get("tools", None)


class ToolContainer:
    def __init__(self, data):
        self.tools = []
        self.order = data.get("order", -1)
        for tool in data.get("entries", []):
            self.tools.append(Tools(tool))

    def toLatex(self):
        if len(self.tools) == 0:
            return ""
        output = r"\section{Technical Skills} \begin{itemize}[leftmargin=0.15in, label={}] \small{ \item{"
        for tool in self.tools:
            output += r"\textbf{" + tool.name + "}{: " + tool.tools + r"} \\ "
        output += r"}} \end{itemize}"
        return output
