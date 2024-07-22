import requests
# parameters define what type of questions will be asked as well as the amount of questions
parameters = {
    "amount" : 10,
    "type" : "boolean"
}
# parameter's necessary to specific the amount of questions and the type 
response = requests.get("https://opentdb.com/api.php", params=parameters)

response.raise_for_status

api_data = response.json()

# saves the data into a library which can read the data properly in the quiz_brain
question_data = api_data["results"]


