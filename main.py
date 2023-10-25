"""
Three Parts:
1. Generate content into a json file
2. Have json file ready to be ingested
3. Generate LaTeX

"""
import shutil
import os
import myresumecontent.main as GenerateJSON
import buildresume.main as BuildObject
import subprocess

build_directory = "./build"
out_directory = "./out"


def build_pdf(info):
    source_file = "./latex-template/JakesResume.tex"
    destination_file = "./build/JakeResume.tex"

    try:
        shutil.copy(source_file, destination_file)
        with open(destination_file, "r") as file:
            content = file.read()
        content = content.replace("%%%% INSERT HERE %%%%", info)
        with open(destination_file, "w") as file:
            file.write(content)
        os.chdir("./build")
        try:
            # Run pdflatex with output redirected to a log file
            with open("./pdflatex.log", "w") as log:
                subprocess.check_call(
                    ["pdflatex", "./JakeResume.tex"],
                    stdout=log,
                    stderr=subprocess.STDOUT,
                )
        except subprocess.CalledProcessError as e:
            print(f"Error running pdflatex: {e}")
        shutil.copyfile("./JakeResume.pdf", "../out/resume.pdf")
        os.chdir("..")

        shutil.rmtree(build_directory)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    if not os.path.exists(out_directory):
        os.makedirs(out_directory)
    if not os.path.exists(build_directory):
        os.makedirs(build_directory)
    GenerateJSON.run()
    build_pdf(BuildObject.run())


main()
