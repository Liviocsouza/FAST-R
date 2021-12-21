from typing import Sized
import PySimpleGUI as sg
import os
import subprocess
import sys
from tkinter import filedialog
import glob
import re
from flask import Flask, request

def getProjectName(projectPath):
    return os.path.basename(os.path.normpath(projectPath))

def getTestFilesFromProject(projectPath):
    # https://junit.org/junit5/docs/current/user-guide/#running-tests-build-maven-filter-test-class-names
    arr = glob.glob(f'{projectPath}/**/Test*.java', recursive=True)
    arr.extend(glob.glob(f'{projectPath}/**/*Test.java', recursive=True))
    arr.extend(glob.glob(f'{projectPath}/**/*Tests.java', recursive=True))
    arr.extend(glob.glob(f'{projectPath}/**/*TestCase.java', recursive=True))
    return arr

def codeFormat(code):

    return re.compile(r"\s+").sub(" ", code).strip()

def defineAppendWrite(fileName):

    if os.path.exists(fileName):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    return append_write

def openAndWriteInFile(fileName, append_write, code):
    f = open(fileName, append_write)
    f.write(code)
    f.close()

def parameterizer(projectPath, entity):
    projectName = getProjectName(projectPath)
    try:
        os.makedirs("input/{}_v1".format(projectName))
    except OSError as exc:  # Python ≥ 2.5
        pass
    fileName = "input/{}_v1/{}-{}.txt".format(projectName,projectName, entity)
    indexTestFilesPaths = "{}/{}-indexTestFilesPaths.txt".format(projectPath, projectName)
    arr = getTestFilesFromProject(projectPath+'/**/src/test/java')

    for fileTest in arr:

        f = open(fileTest, "r")

        code = codeFormat(f.read()) + '\n'

        append_write = defineAppendWrite(fileName)
        openAndWriteInFile(fileName, append_write, code)

        append_write = defineAppendWrite(indexTestFilesPaths)
        testFile = os.path.relpath(fileTest, projectPath) + '\n'
        openAndWriteInFile(indexTestFilesPaths, append_write, testFile)
        f.close()



           
            
app = Flask("Youtube")

@app.route("/", methods=["GET"])
def olamundo():
    return {"ola":"mundo"}

@app.route("/executaFastR", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()
    cenario= body['cenario']
    cobertura= body['cobertura']
    projeto= body['projeto']

    executarCmd = f'py D:/back-end/FAST-R/py/{cenario} {cobertura} {projeto}'
    print(executarCmd)
            # os.system('py experimentBudget.py function flex v3 10')
            # subprocess.run(['py experimentBudget.py function flex v3 10'], stderr=sys.stderr, stdout=sys.stdout)
    process = subprocess.Popen(executarCmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output
    # print(output)



app.run()

