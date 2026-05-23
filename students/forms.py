from django import forms

from .models import Students


class StudentCreation(forms.ModelForm):

    class Meta:

        model = Students

        fields = [
            'name',
            'picture',
            'dob',
            'father_name',
            'contact',
            'class_roll',
            'village',
            'p_o',
            'p_s',
            'dist',
            'state',
            'pin',
        ]

        widgets = {

            'dob': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'name': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'father_name': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'contact': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'class_roll': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'village': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'p_o': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'p_s': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'dist': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'state': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),

            'pin': forms.TextInput(
                attrs={
                    'class': 'border p-2 rounded w-full'
                }
            ),
            
            'picture': forms.ClearableFileInput(
                attrs={
                    'class': 'border p-2 rounded w-full bg-white'
                }
            ),
        }