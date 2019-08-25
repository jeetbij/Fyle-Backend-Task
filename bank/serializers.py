from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Branch, Bank

class BankSerializer(ModelSerializer):

	class Meta:
		model = Bank
		fields = '__all__'


class BranchSerializer(ModelSerializer):

	bank = serializers.SerializerMethodField()

	def get_bank(self, obj):
		return BankSerializer(obj.bank).data

	class Meta:
		model = Branch
		fields = '__all__'