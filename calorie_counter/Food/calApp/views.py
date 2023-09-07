from django.shortcuts import render
import requests
import json
# Create your views here.

API_KEY='uxjjqLh379Zwkw7Qs1+Dxw==73C3nUvmjIMIR3NK'
def home(request):
   
    if request.method=='POST':
        food=request.POST['food']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request=requests.get(api_url + food, headers={'X-Api-Key': 'uxjjqLh379Zwkw7Qs1+Dxw==73C3nUvmjIMIR3NK'})
        try:
            api=json.loads(api_request.content)
            print(api_request.content)
            
        except Exception as e:
            api='there was an error'
            print(e)
       
        return render(request,'home.html',{'api':api})
            
    else:
         return render(request,'home.html',{'query':'enter a valid query'})
         
         
  
        
        
   