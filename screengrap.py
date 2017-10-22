#encoding:utf-8
import time
import locale
import os
import imagesqrc
from PIL import ImageGrab
from PySide import QtCore
from PySide import QtGui

class ScreenGrab(QtGui.QWidget):
	def __init__(self):
		super(ScreenGrab,self).__init__()
		self.base_dir=''
		self.setUI()
		
	def setUI(self):
		self.setGeometry(250,250,300,300)
		self.setWindowTitle(u'苏大附一院临检中心')
		self.setFixedSize(self.width(),self.height()); 
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/snake.ico"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(icon)
		
		self.tuopan=QtGui.QSystemTrayIcon(self)
		self.tuopan.setIcon(icon)
		self.tuopan.show()
		self.tuopan_menu()
		self.tuopan.activated.connect(self.tuopanEvent)
		
		self.dir_path=QtGui.QLineEdit(self.tr("D:\original_catalog"))
		open_button=QtGui.QPushButton(u"打开")
		open_button.clicked.connect(self.dirDialog)
		submit_button=QtGui.QPushButton(u"截图")
		submit_button.clicked.connect(self.grab)
		h_layout=QtGui.QHBoxLayout()
		h_layout.addWidget(self.dir_path)
		h_layout.addWidget(open_button)
		v_layout=QtGui.QVBoxLayout()
		v_layout.addLayout(h_layout)
		v_layout.addWidget(submit_button)
		
		self.setLayout(v_layout)
	def tuopan_menu(self):
		self.restoreAction = QtGui.QAction(u"还原", self,triggered=self.showNormal)
		self.quitAction = QtGui.QAction(u"退出", self,triggered=QtGui.qApp.quit)
		self.trayIconMenu = QtGui.QMenu(self)
		self.trayIconMenu.addAction(self.restoreAction)
		self.trayIconMenu.addSeparator()
		self.trayIconMenu.addAction(self.quitAction)
		self.tuopan.setContextMenu(self.trayIconMenu)
	
	def tuopanEvent(self,type):
		if type==QtGui.QSystemTrayIcon.DoubleClick:
			self.showNormal()
		else:
			pass
		
	def closeEvent(self,event):
		if self.tuopan.isVisible():
			self.hide()
			event.ignore()
	def dirDialog(self):
		dir_path=QtGui.QFileDialog.getExistingDirectory(self,"choose directory","C:\Users\Administrator\Desktop")
		self.base_dir=dir_path
		self.dir_path.setText(self.base_dir)
		#print self.base_dir
		
	def grab(self):
		if not self.base_dir:
			if not os.path.exists(r'd:\original_catalog'):
				os.makedirs(r'd:\original_catalog')
			else:
				self.base_dir=r'd:\original_catalog'
		TimeName=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
		im=ImageGrab.grab()
		if not im.save(os.path.join(self.base_dir,TimeName)+'.jpg',"jpeg"):
			QtGui.QMessageBox.information(self,u"截屏工具",u"截屏成功!!")
		
		
		
		
if __name__=='__main__':
	import sys
	app=QtGui.QApplication(sys.argv)
	mycode = locale.getpreferredencoding()  
	code = QtCore.QTextCodec.codecForName(mycode)  
	QtCore.QTextCodec.setCodecForLocale(code)  
	QtCore.QTextCodec.setCodecForTr(code)  
	QtCore.QTextCodec.setCodecForCStrings(code)
	main=ScreenGrab()
	main.show()
	sys.exit(app.exec_())
		