#前言

实际需求中，测试需要区分测试包和正式包，最直观的就是看你安装的ipa的显示的icon，解决的方案可能是创建多个target设置不同的AppIcon，或者是根据debug或者release设置不同的iconAppIcon但是对于这种解决方案，个人觉得还是有点不方便，于是想让一键替换这种方式。或许大佬有优秀的解决方案，请多指教。
#需求
1.更改配置
2.切换不同环境的icon
#实现效果
![更改配置](https://upload-images.jianshu.io/upload_images/2608128-fcdce34f38e4687b.gif?imageMogr2/auto-orient/strip)
![替换icon](https://upload-images.jianshu.io/upload_images/2608128-4e947c745ad83487.gif?imageMogr2/auto-orient/strip)
#思路
-**替换配置文件内容**
```
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
```
-**替换AppIcon**
```
class SVChangeIcons():
    def __init(self):
        super(SVChangeIcons,self).__init__()

"""cPath: 需要的Appicon  dPath:被替换的Appicon"""
    def changeIcons(self,cPath,dPath):
    	if os.path.isdir(cPath) and os.path.isdir(dPath):
        	shutil.rmtree(dPath)
        	shutil.copytree(cPath,dPath)
```
-**通过调用脚本来实现一键替换配置文件和Appicons**
利用Aggregate实现脚本，就能实现效果图所示 一键切换Appicon
![Aggregate](https://upload-images.jianshu.io/upload_images/2608128-3a3fb00560383fe1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#结语
到此整个流程思路就结束了
 py脚本及demo在github地址
可以直接拿来用，只需根据你的需求来修改几个内容，目前只支持修改单个配置文件 当然也可以更改多个配置 需要自己改造
```
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
```




