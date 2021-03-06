import maya.cmds as cmds

import os
from functools import partial

import fileManager as fm
import Utilities.projectGlobals as pg

widgets = {}

def set_project_UI(*args):
	if cmds.window("setProjectWin", exists=True):
		cmds.deleteUI("setProjectWin")

	widgets["win"] = cmds.window("setProjectWin", t="Set Project", w=200, h=100)
	widgets["mainCLO"] = cmds.columnLayout(w=300, h=200)
	cmds.text("Click the project you'll be working in", al="left")
	cmds.separator(h=10)
# procedularize this to pull from project globals, projectGlobals.projects dictionary	
	widgets["frog"] = cmds.button(l="OutOfBoxExperience Project", w=300, h=40, bgc=(.5, .5, .5), c=partial(set_project_env_variables, "OutOfBoxExperience"))
	widgets["fit"] = cmds.button(l="FitAndSetup Project", w=300, h=40, bgc=(.3, .3, .3), c=partial(set_project_env_variables, "FitAndSetup"))

	cmds.window(widgets["win"], e=True, w=5, h=5, rtf=True)
	cmds.showWindow(widgets["win"])


def set_project_env_variables(proj = None, *args):
	"""
	sets two environment variables: MAYA_CURRENT_PROJECT and MAYA_PROJ_PATH, which we'll use in doing some pipeline stuff
	ARGS:
		proj (string) - the shortcut for the project we're using. Currently only "frog" and "fit", which stand for OutOfBoxExperience and FitAndSetup

	"""
	if not proj:
		return()

	currProj = None
	projPath = None

	if proj in pg.projects.keys():
		currProj = proj
		projPath = pg.projects[proj]

	os.environ["MAYA_CURRENT_PROJECT"] = currProj
	os.environ["MAYA_PROJECT_PATH"] = projPath

	print "{0} is now the current project (MAYA_CURRENT_PROJECT env var)\n{1} is now the current project path (MAYA_PROJECT_PATH env var)".format(currProj, projPath)

	if cmds.window("setProjectWin", exists=True):
		cmds.deleteUI(widgets["win"])

	fm.fileManager()


def setProject(*args):
	set_project_UI()


