import os
import csv
from lib.models.site import Site

def get_all_sites() -> set():
	result = set()
	script_dir = os.path.dirname(__file__)
	#Fake database access
	with open(script_dir + '//site.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			data_site = Site(row['site_id'],row['name']);
			data_site.image_path = row['image_path'];
			result.add(data_site);
		return result;