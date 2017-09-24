import os
import json
import ycm_core

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

compilation_database_folder = os.path.join(BASE_DIR, 'build')

if os.path.exists(compilation_database_folder):
    database = ycm_core.CompilationDatabase(compilation_database_folder)
else:
    database = None

FLAGS = {}

def parseFlagsFile(fn):
    with open(fn, "rt") as fs:
        ff = json.load(fs)
        for f in ff["files"]:
            FLAGS[f] = ff["flags"].split()


def collectFlags():
    for r, d, fs in os.walk(compilation_database_folder):
        for f in fs:
            _, e = os.path.splitext(f)
            if e != ".flags":
                continue
            parseFlagsFile(os.path.join(r, f))

collectFlags()


def ciFromDatabase(filename):
    return database.GetCompilationInfoForFile(filename)


def tryFindCi(filename):
    return FLAGS[filename]


def getCompilationInfoForFile(filename):
    ci = ciFromDatabase(filename)

    if ci and ci.compiler_flags_:
        return ci.compiler_flags_

    return tryFindCi(filename)


def makePathAbsolute(flags, wd):
    if not wd:
        return list(flags)

    newFlags = []

    makeNextAbs = False

    pathFlags = ['-isystem', '-I', '-iquote', '--sysroot=']

    for flag in flags:
        nf = flag

        if makeNextAbs:
            makeNextAbs = False

            if not flag.startswith('/'):
                nf = os.path.join(wd, flag)

        for pf in pathFlags:
            if flag == pf:
                makeNextAbs = True
                break

            if flag.startswith(pf):
                path = flag[len(pf):]
                nf = pf + os.path.join(wd, path)
                break
        if nf:
            newFlags.append(nf)

    return newFlags


def FlagsForFile(filename, **kwargs):
    if not database:
        ci = tryFindCi(filename)
    else:
        ci = getCompilationInfoForFile(filename)

    return { 'flags': makePathAbsolute(ci, compilation_database_folder) }

