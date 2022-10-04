import os
import csv
from lib.models.peakrating import PeakRating

def get_site_peak_rating(site_id: int) -> PeakRating:
	script_dir = os.path.dirname(__file__)
	#Fake database access
	with open(script_dir + '//sitepeakrating.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row['site_id'] == str(site_id):
				return get_peak_rating(row['peak_rating_id']);
		return PeakRating(None,None);

def get_peak_rating(peak_rating_id: int) -> PeakRating:
	script_dir = os.path.dirname(__file__)
	#Fake database access
	with open(script_dir + '//peakrating.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			if row['peak_rating_id'] == peak_rating_id:
				return PeakRating(row['peak_rating_id'], row['name']);