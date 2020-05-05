from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class SomeForm(forms.Form)
	foo = forms.CharField(widget=SummernoteWidget())