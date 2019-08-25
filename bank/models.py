from django.db import models

# Create your models here.

class Bank(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	id = models.BigIntegerField(primary_key=True)

	class Meta:
		verbose_name = 'Bank'
		verbose_name_plural = 'Banks'

	def __str__(self):
		return self.name


class Branch(models.Model):
	ifsc_code = models.CharField(max_length=15, null=True, blank=True)
	bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="bank_branches")
	branch = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	district = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=25, null=True, blank=True)

	class Meta:
		verbose_name = "Bank Branch"
		verbose_name_plural = "Bank Branches"

	def __str__(self):
		return self.branch + '->' + self.ifsc_code