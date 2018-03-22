from django.db import models

class PhotoManager(models.Manager):
	def create_photo(self, url):
		photo = self.create(url=url)
		photo = self.create(bird = False)
		photo = self.create(score = 0)
		return photo
	
	def update_bird(status):
		self.bird = status
	
	def update_score(change):
		self.score = self.score + change
		
	def get_url(self):
		return self.url
		
	def is_bird(self):
		return self.bird
	
	def current_score(self):
		return self.score
		
class Photo(models.Model):
	url = models.URLField(default = '')
	bird = models.BooleanField(default = False)
	score = models.IntegerField(default = 0)
	
 	objects = PhotoManager()
	

	


