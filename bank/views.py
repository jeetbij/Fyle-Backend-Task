from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Branch
from .serializers import BranchSerializer
# Create your views here.


class GetBankView(APIView):

	def get(self, request, format=None):

		data = request.GET.copy()

		limit = int(data.get('limit', 25))
		offset = int(data.get('offset', 0))

		if 'ifsc' in data:
			ifsc_code = data.get('ifsc', '')
			bank_branch = Branch.objects.filter(ifsc=ifsc_code)[offset:offset+limit]
			serialized_data = BranchSerializer(bank_branch, many=True).data

			return Response({
				"status": status.HTTP_200_OK,
				"data": serialized_data
				})

		elif 'bank_name' in data and 'city' in data:
			bank_name = data.get('bank_name', '')
			city = data.get('city', '')
			branches = Branch.objects.filter(bank__name=bank_name, city=city)[offset:offset+limit]
			serialized_data = BranchSerializer(branches, many=True).data

			return Response({
				"status": status.HTTP_200_OK,
				"data": serialized_data
				})
		return Response({
			"status": status.HTTP_204_NO_CONTENT,
			"data": "No data found."
			})