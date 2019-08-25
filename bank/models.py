from django.db import models

# Create your models here.

class Bank(models.Model):
	name = models.CharField(max_length=49, null=True, blank=True)
	id = models.BigIntegerField(primary_key=True)

	class Meta:
		db_table = 'banks'
		verbose_name = 'Bank'
		verbose_name_plural = 'Banks'

	def __str__(self):
		return self.name


class Branch(models.Model):
	ifsc = models.CharField(max_length=11, primary_key=True)
	bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="bank_branches")
	branch = models.CharField(max_length=74, null=True, blank=True)
	address = models.CharField(max_length=195, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	district = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=26, null=True, blank=True)

	class Meta:
		db_table = 'branches'
		verbose_name = "Bank Branch"
		verbose_name_plural = "Bank Branches"

	def __str__(self):
		return self.branch + '->' + self.ifsc