import os
import csv
from lib.models.attraction import Attraction

#SELECT a.name FROM attraction a, siteattraction sa WHERE sa.site_id = site_id_parameter and a.id = sa.attraction_id;
def get_site_attractions(site_id: int) -> set():
	result = set();
	script_dir = os.path.dirname(__file__)
	#Fake database access
	with open(script_dir + '//siteattraction.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row['site_id'] == str(site_id):
				result.add(get_attraction(row['attraction_id']));
		return result;

#SELECT * FROM attraction WHERE attraction_id = attraction_id_parameter
def get_attraction(attraction_id: int) -> Attraction:
	script_dir = os.path.dirname(__file__)
	#Fake database access
	with open(script_dir + '//attraction.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row['attraction_id'] == attraction_id:
				return Attraction(row['attraction_id'], row['name']);

#SELECT * FROM attraction
def get_all_attractions() -> set():
	result = set();
	script_dir = os.path.dirname(__file__)
	#Fake database access
	with open(script_dir + '//attraction.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			result.add(Attraction(row['attraction_id'],row['name']));
		return result;