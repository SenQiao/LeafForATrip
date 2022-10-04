import sys
from lib.models.site import Site
from lib.controllers.sitecontroller import get_all_sites
from lib.controllers.peakratingcontroller import get_site_peak_rating
from lib.controllers.attractioncontroller import get_site_attractions
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Leaf For a Trip';
		self.left = 100;
		self.top = 100;
		self.width = 1000;
		self.height = 1000;
		self.margin= 100;
		self.initUI();
    
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setStyleSheet("""
			MainWindow {
				background-color: #73264d;
			}

			QWidget #hiddenImages{
				background-image: url("image/background.jpeg")
			}

			QWidget #topImage{
				background-image: url("image/background2.jpeg");
				padding: 200px;
			}

			QWidget #title{
				color: white;
				font-size: 20px;
				font-weight: bold;
			}
			""");

		# Create top image widget
		self.create_image(0, 0, 'image/nc.png', 1000, 200, True, None);
		self.create_title(300,210);

		#Get All Sites
		sites = get_all_sites();
		for site in sites:
			site.peak_rating = get_site_peak_rating(site.id);
			site.attractions = get_site_attractions(site.id);

		width = 100;
		height = 250;
		for site in sites:
			if width > 700:
				width = 100;
				height += 250;
			self.create_image(width, height, site.get_image_path(), 200, 200, False, site);
			width+=300;

		self.show();

	def eventFilter(self, object, event):
		if event.type() == QEvent.Enter:
			object.setText(object.sitename +'\n'+
				"Attractions: " + object.attractions+'\n'+
				"Leaf Color Rating: " + object.peak_rating)
			return True
		elif event.type() == QEvent.Leave:
			pixmap = QPixmap(object.image_path);
			object.setPixmap(pixmap);
		return False

	def create_title(self, right: int, top: int):
		label = QLabel(self);
		label.move(right,top);
		label.setText("Hover over and discover your NC Autumn World!");
		label.setObjectName("title");
		label.show();

	def create_image(self, right: int, top: int, path: str, width: int, height: int, hasbackground_color: bool, site: Site):
		label = QLabel(self);
		pixmap = QPixmap(path);
		label.setPixmap(pixmap);
		label.image_path = path;
		if site != None:
			label.sitename = site.get_text();
			label.attractions = ', '.join([a.get_text() for a in site.attractions]);
			label.peak_rating = site.peak_rating.get_text();
		label.move(right,top);
		label.setMaximumWidth(width);
		label.setMaximumHeight(height);
		if hasbackground_color:
			label.setObjectName("topImage");
		else:
			label.setObjectName("hiddenImages");
			label.installEventFilter(self);
		label.show();

if __name__ == '__main__':
	app = QApplication(sys.argv);
	ex = MainWindow();
	sys.exit(app.exec_());