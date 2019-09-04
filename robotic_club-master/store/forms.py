from django import forms
from store.models import Item_discription,Cart


class ItemForm(forms.ModelForm):
	class Meta():
	
		model = Item_discription
		fields = ('text','amount','photo1','photo2','product_name')



class CartForm(forms.ModelForm):
	class Meta():
	
		model = Cart
		fields = ('amount',)