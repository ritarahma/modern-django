
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView):
	"""behaviour untuk rest api """
	queryset = Bucketlist.objects.all()
	serializer_class = BucketlistSerializer

	def perform_create(self, serializers):
		"""save  data"""
		serializers.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""buat get, put, delete"""
	queryset = Bucketlist.objects.all()
	serializer_class = BucketlistSerializer
		