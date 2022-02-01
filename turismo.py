import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "da588100-74a2-11ec-b559-81cf22e009279a5ab59c-4e94-4938-9556-5dee0c8e707c"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()




def answer_question():
    question = input("> ")
    answer = classify(question)
    
    answerclass = answer["class_name"]
    confidence = answer["confidence"]

    if confidence < 75:
        print("No entiendo la pregunta. Pregúntame otra cosa!")
    if answerclass == "Ciudad":
        print ("quiero visitar roma")
    elif answerclass == "Gastronomia":
        print ("Muy bien. Aqui tienes planes de gastromia")
    elif answerclass == "Arte":
        print ("Muy bien. Aqui tienes planes de arte y cultura")
    elif answerclass == "Otros":
        print ("Muy bien. Aqui tienes planes que se salen de lo comun")
    elif answerclass == "si":
        print("Cual será tu próximo destino?")
    elif answerclass == "no":
        print("Vale, pues que tengas un buen día.")

  


print ("¿Que te gustaria hacer mientras estas en la ciudad?")  

while True:
    answer_question()


