"""
   metotlar            kullanımı
assertEqual(a, b)	    a == b
assertNotEqual(a, b)	a != b
assertTrue(x)	        x == True
assertFalse(x)	        x == False
assertIn(item, list)	item in list
assertNotIn(item, list)	item not in list
"""

class AnonymousSurvey():
    """Anonim anket için gerekli sınıf"""
    def __init__(self,question):
        """Anket için soruyu kaydet ve yanıtları hazırla"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Anket sorusunu göster"""
        print(self.question)
    
    def store_response(self,new_response):
        """Ankete verilen yanıtları sakla"""
        self.responses.append(new_response)
    
    def show_results(self):
        """Anket sonuçlarını göster"""
        print("Anket sonuçları:")
        for response in self.responses:
            print(f"- {response}")