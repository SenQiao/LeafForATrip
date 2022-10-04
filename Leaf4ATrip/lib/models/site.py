from .name import Name
from .attraction import Attraction
from .peakrating import PeakRating
import csv

class Site(Name):
	#list of attractions
	attractions = set();
	peak_rating = PeakRating(None, None);
	image_path = '';
	def get_image_path(self) -> str:
		return self.image_path;