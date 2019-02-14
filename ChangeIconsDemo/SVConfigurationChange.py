# coding: utf-8
import os,sys,shutil,optparse

# 生产环境appicon路径
proPath = os.path.abspath("./Appicon/production/Appicon.appiconset")
# 开发环境appicon路径
devPath = os.path.abspath("./Appicon/dev/Appicon.appiconset")
# 项目中appicon路径
dPath = os.path.abspath("./Assets.xcassets/Appicon.appiconset")

# 需要修改的文件
configPath = os.path.abspath("AppDelegate.swift")
# 开发环境此行类容
devConfigLine = "config.dev\n"
# 生产环境此行类容
proConfigLine = "config.pro\n"


class SVChangeLinesModel(object):
	"""
	need to change file with lines
	lines  0：oldStr -> 1：newStr
	 """
	def __init__(self, file,lines):
		super(SVChangeLinesModel, self).__init__()
		self.file = file
		self.lines = lines

class SVHandleChangeLines(object):
	"""docstring for SVHandleChangeLines"""
	def __init__(self):
		super(SVHandleChangeLines, self).__init__()

		
	def handingModels(self,models):
		for model in models:
			file = model.file
			filePath = os.path.dirname(file)
			fileName = os.path.basename(file)
			r_file = filePath + '/r_' + fileName
			if os.path.isfile(file):
				with open(file,mode = 'r',encoding = 'utf-8') as fr,open(r_file,mode = 'w',encoding = 'utf-8') as fw:
					for line in fr:
						for item in model.lines:
							fw.write(line.replace(item[0],item[1]))
					os.remove(file)
					os.rename(r_file,file)


class SVChangeIcons():
    def __init(self):
        super(SVChangeIcons,self).__init__()

    def changeIcons(self,cPath,dPath):
    	if os.path.isdir(cPath):
    		if os.path.isdir(dPath):
    			shutil.rmtree(dPath)
    		shutil.copytree(cPath,dPath)


def configAction(oldLine,newLine):
    m = SVChangeLinesModel(configPath,[[oldLine,newLine]])
    arr = [m]
    h = SVHandleChangeLines()
    h.handingModels(arr)

def iconAction(path):
 	icon = SVChangeIcons()
 	icon.changeIcons(path,dPath)


def toDev():
	configAction(proConfigLine,devConfigLine)
	iconAction(devPath)

def toProduction():
	configAction(devConfigLine,proConfigLine)
	iconAction(proPath)

def SVConfigIconsAction():
	p = optparse.OptionParser()
	p.add_option('--configuration','-c',default='Dev')
	opthions,arguments = p.parse_args()
	if opthions.configuration == 'Production':
		toProduction()
	else:
		toDev()

if __name__ == '__main__':
	SVConfigIconsAction()




