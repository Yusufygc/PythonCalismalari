import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """AnonymousSurvey sınıfının testi"""
    def setUp(self):
        """Tüm test metodları için bir anket ve bir dizi yanıt oluşturur"""
        question = "En sevdiğiniz programlama dili nedir?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Python','C#','Java']

    def test_store_single_response(self):
        """Bir yanıtın doğru şekilde saklanıp saklanmadığını test eder"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
   
    def test_store_three_responses(self):
       # Üç yanıtın doğru şekilde saklanıp saklanmadığını test eder
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
    
if __name__ == '__main__':
    unittest.main()