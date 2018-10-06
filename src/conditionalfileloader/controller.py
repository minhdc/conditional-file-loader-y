#
# This class for control ConsoleBotClient. 
# It takes input from user console. 
# And then return the answer#


from programy.clients.events.console.client import ConsoleBotClient

class Controller(object):
    def __init__(self, a, b):
        self._a = a 
        self._b = b
    def sum(self):
        return self._a + self._b 

class GetEntities(object):
    def __init__(self):
        pass 
    
    def get(self, question):
        return "" 



def sanitize(question, intend, entities):
    return question 

if __name__ == '__main__':
    bot_client = ConsoleBotClient()   #initiate program-y
    
    client_context = bot_client.create_client_context(bot_client._configuration.client_configuration.default_userid)
    
    #get_intend = GetIntend()          #get_intend object from anh Hoang 
    
    get_entities = GetEntities()      #get_entities object from AKI 
    
    while True:
        question = input()           #question is taken from user 
        #intend = get_intend.get(question)
        #entites = get_entities.get(question)
        #question = sanitize(question, intend, entites)
        if (question == "Bye"):
            break 
        response = bot_client.process_question(client_context, question)
        print(response)
    