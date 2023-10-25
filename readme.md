# Pythonified LaTeX Resume

```py
python3 main.py

```

1. Edit your resume points and sections in `/myresumecontent/`
1. Use `python3 main.py` to render the resume to `/out/resume.pdf`
1. When `main.py` is executed it uses the content from `/myresumecontent/`, saves the data to `/build/data.json` and then tells `/buildresume/main.py` to render the pdf.
