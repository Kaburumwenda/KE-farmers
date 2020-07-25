from django import forms
from .models import MultivendorProduct


class MultivendorProductForm(forms.ModelForm):

	class Meta:
		model = MultivendorProduct
		fields = ['firstname','lastname','phone','email',
		           'address','businessname','title','price',
		           'discount','amount','condition','description']
		labels = {
		 'firstname':'First Name (jina la kwanza)',
		 'lastname':'Last Name (jina la familia)',
		 'phone':'phone (Nambari ya simu)',
		 'email':'Email (Barua pepe)',
		  'businessname':'Business Name (Jina la Biashara kama unalo)',
		  'address':'Address (Anwani)',
		  'title':'Product title (Kichwa cha bidhaa)',
		  'price':'Price (Bei)',
		  'discount':'Discount (punguzo)',
		  'amount':'Amount (kiasi unacho)',
		  'description':'Description (maelezo zaidi)',
		  'condition':'Condition (Hali ya bidhaa)',


		}

	def __init__(self, *args, **kwargs):
		super(MultivendorProductForm,self).__init__(*args, **kwargs)
		self.fields['phone'].required = True
		self.fields['businessname'].required = False
		self.fields['email'].required = False
		self.fields['discount'].required = False
		self.fields['condition'].empty_label = 'Select (Changua)'
