from django.db import models

# Create your models here.
class Occupation(models.Model):
	name 				= models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
		
	
	
class Member(models.Model):
	name 				= models.CharField(max_length=200)
	#icon
	#banner
	bio_html 			= models.CharField(max_length=200)
	beatport_name 		= models.CharField(max_length=200)
	soundcloud_name 	= models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
	
class MemberOccupation(models.Model):
	member 				= models.ForeignKey(Member)
	occupation 			= models.ForeignKey(Occupation)
	def __unicode__(self):
		return ', '.join([
			self.member.__unicode__(),
			self.occupation.__unicode__(),
		])
				  
	