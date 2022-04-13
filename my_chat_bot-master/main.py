import re
import random

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'Hi', 'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Que guto saber eso en que podemos ayudarte', ['muy bien','bien','excelente'], single_response=True)
        response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        response('Frenos, Puestes, Coronas, Extracciones, Carillas, Protesis, Empastes, Blanqueamiento', ['que hay', 'procedimientos', 'tratamientos','servicios'], single_response=True)
        response('$3.900.00', ['precio de los frenos','frenos'], single_response=True)
        response('$800.000', ['precio de los implantes','implantes'], single_response=True)
        response('$350.000', ['precio de la corona','coronas'], single_response=True)
        response('$440.000', ['precio de la extraccion','extracciones'], single_response=True)
        response('$1.600.000', ['precio de la carilla','carillas'], single_response=True)
        response('$300.000', ['precio de la protesis','protesis'], single_response=True)
        response('$100.000', ['precio del empaste','empaste'], single_response=True)
        response('$500.000', ['precio de la cirugia de encias','cirugia de encias'], single_response=True)
        response('$30.000', ['precio de los selladores','selladores'], single_response=True)
        response('$500.000', ['precio del blanquiamiento','blanquiamiento'], single_response=True)
        response('3135403397', ['telefono','contacto'], single_response=True)



        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))