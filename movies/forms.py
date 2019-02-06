from django import forms
import requests

class SearchForm(forms.Form):
    search_string = forms.CharField(max_length=100)

    def search(self):
        result = {}
        search_string = self.cleaned_data['search_string']
        endpoint = 'http://www.omdbapi.com/?apikey=a6793cf9&t={movie}'
        url = endpoint.format(movie=search_string)
        response = requests.get(url)
        if response.status_code == 200: #success
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404: #Not found
                result['message'] = 'No entry found for "%s"' % search_string
            else:
                result['message'] = 'Database is not available currently'
        return result