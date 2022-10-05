# Leaf For A Trip :maple_leaf:

**Goal of the Application**
- Pick out the best trail to see autumn leaves

**Design Process**
<br />
The Idea was to start with a basic MVC model. I first designed the data model and the classes, then design the APIs needed, and then finally design with my wife the UI. Most of the time was allocated with planning and testing. The plan was to have maybe 15% of the time as coding.

**What will I need?**

1. Storage Model (How do I store the data)
	- Data Relationship
		- Site
		- ~~Weather~~
		- Attraction
		- Peak
		- SiteAttraction
		- SitePeak
	- CSV files for simple storage (maybe sqlite later)
	- Images

2. API Controller (How do I communicate with the data)
	- Get Methods
	- *Create Methods*
	- *Update Methods*
	- *Delete Methods*

3. UI View (How do I interact with the data)
	- Pyqt5
	- Display site images
	- On hover display attraction and peak for each site
	- ~~Interactive Map~~

**Basics Left to Add**

1. Code Refactoring 
	- Generalize csv reader
	- Style Attractions
2. New Functionality
	- Add Create/Update/SoftDelete (Attractions, Site)
	- Image Uploader

**Fun Things to Add**

1. Python image to peak percentage Converter
2. Map location
3. Search bar