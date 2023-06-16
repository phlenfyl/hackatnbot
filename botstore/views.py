from django.http import JsonResponse
import requests

from django.shortcuts import render
from dataclasses import dataclass

from . models import *

# Create your views here.


@dataclass
class O:
    his = ChatHistory.objects.all()

def home(request):
    

    return render(request, 'home.html')

def chatresponseAPI(request):
    if request.method == 'POST':
        # Retrieve user input from the request
        user_input = request.POST.get('message')

        # Send user input to the Rasa chatbot for processing
        rasa_api_url = 'http://localhost:5005/webhooks/rest/webhook'  # Adjust the URL based on your Rasa deployment
        rasa_payload = {'sender': 'user', 'message': user_input}
        rasa_response = requests.post(rasa_api_url, json=rasa_payload).json()

        if rasa_response:
            # Extract the chatbot's response from the Rasa response
            chatbot_response = rasa_response[0]['text']
            save = O.his.create(user = request.user, user_input= user_input, bot_response = chatbot_response)
            return JsonResponse({'response': chatbot_response, 'save':save})
        
        save = O.his.create(user = request.user, user_input= user_input, bot_response = chatbot_response)

    return JsonResponse({'error': 'Invalid request method.', 'save':save})




# # Django View (views.py)

# from django.http import JsonResponse
# from rasa.core.agent import Agent

# # Load the Rasa model
# rasa_model_path = "/path/to/your/rasa/model"
# rasa_agent = Agent.load(rasa_model_path)

# def chatbot_api(request):
#     if request.method == 'POST':
#         # Retrieve user input from the request
#         user_input = request.POST.get('message')

#         # Process user input with the Rasa agent
#         response = rasa_agent.handle_text(user_input)

#         # Extract the chatbot's response from the Rasa response
#         chatbot_response = response[0]['text']

#         # Return the chatbot response as a JSON response
#         return JsonResponse({'response': chatbot_response})

#     return JsonResponse({'error': 'Invalid request method.'})



