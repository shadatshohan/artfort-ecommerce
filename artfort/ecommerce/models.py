from django.db import models


class Tags(models.Model):
	tag=models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return self.tag
# Create your models here.
class Product(models.Model):
	product_id=models.AutoField
	product_name=models.CharField(max_length=50,default="")
	product_desc=models.CharField(max_length=200,default="")
	pub_date=models.DateField()
	category=models.CharField(max_length=50)
	sub_category=models.CharField(max_length=50)
	price=models.IntegerField(default=0)
	image=models.ImageField(upload_to='shop/images',default="")
	tag=models.ManyToManyField(Tags,blank=True,null=True)

	def __str__(self):
		return self.product_name