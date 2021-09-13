from django import forms
from .models import Passsql

# form dari bootstrap
class CreateBatchForm(forms.Form):
 
    action   = forms.ChoiceField(
        widget= forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
        ),
        choices= [
                            ('Get Data Toko','Get Data Toko'),
                            ('Update/Insert/Delete/Create','Update/Insert/Delete/Create'),
                        ]    
                        )   
    CHOICES_CAB = (('g117', 'G117'),('g113', 'G113'),)
    cabang = forms.ChoiceField(label = 'Cabang',choices=CHOICES_CAB,
                widget= forms.Select(
                    attrs={
                        'class':'form-control'
                    }
                )                   
            )
    
    # passtoko = forms.ModelMultipleChoiceField(queryset=Passsql.objects.all(),
    #         widget= forms.Select(
    #                 attrs={
    #                     'class':'form-select'
    #                 }
    #             )    
    #         )
    
    passtoko = forms.ModelChoiceField(queryset=Passsql.objects.all(),to_field_name='password',
                                   widget=forms.Select(attrs={'class':'form-control'}))
    
    kdtk = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'class':'form-control',
                'readonly':'True'
            }
            ),
    )
                         
    
    nama_file           = forms.CharField(
        widget= forms.TextInput(
        attrs={
              'class':'form-control',
              'placeholder':'Nama File',
          }  
        ),
    )
    
    query          = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control'
            }
        ),
        )
    