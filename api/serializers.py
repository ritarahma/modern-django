from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
	"""mapping model kedalam JSON format"""

	class Meta:
		"""mapping field serializer kedalam field model"""
		model = Bucketlist
		fields = ('id','name','date_created','date_modified')
		read_only_fields = ('date_created','date_modified')
		