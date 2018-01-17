# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
class ModelTestCase(TestCase):
	def setUp(self):
		self.bucketlist_name = "nei belajar DRF"
		self.bucketlist = Bucketlist(name=self.bucketlist_name)

	def test_model_bisa_ngisi(self):
		old_count = Bucketlist.objects.count()
		self.bucketlist.save()
		new_count = Bucketlist.objects.count()
		self.assertNotEqual(old_count,new_count)

class ViewTestCase(TestCase):
	"""test untuk api view"""

	def setUp(self):
		"""setting test client dan variable test lainnya"""
		self.client = APIClient()
		self.bucketlist_data = {'name':'Go to Ibiza'}
		self.response = self.client.post(
			reverse('create'),
			self.bucketlist_data,
			format='json')

	def test_api_bisa_ngisi(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_bisa_get(self):
		bucketlist = Bucketlist.objects.get()
		response = self.client.get(
			reverse('details',
			kwargs={'pk':bucketlist.id}), format="json")

		self.assertEqual(response.status_code, status.HTTP_201_OK)
		self.assertContains(response, bucketlist)

	def test_api_bisa_update(self):
		change_bucketlist = {'name':'yang baru'}
		res = self.client.put(
			reverse('details', kwargs={'pk': bucketlist.id}),
			change_bucketlist, format='json'
		)
		self.assertEqual(res.status_code, status.HTTP_201_OK)

	def test_api_bisa_delete(self):
		bucketlist = Bucketlist.objects.get()
		response = self.client.delete(
			reverse('details', kwargs={'pk':bucketlist.id}),
			format='json',
			follow = True)