import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """AnonymousSurvey sınıfının testi"""
    def test_store_single_response(self):
        """Bir yanıtın doğru şekilde saklanıp saklanmadığını test eder"""
        question = "En sevdiğiniz programlama dili nedir?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Python')
        self.assertIn('Python',my_survey.responses)
   
    def test_store_three_responses(self):
       # Üç yanıtın doğru şekilde saklanıp saklanmadığını test eder
        question = "En sevdiğiniz programlama dili nedir?"
        my_survey = AnonymousSurvey(question)
        responses = ['Python','C#','Java']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
    
if __name__ == '__main__':
    unittest.main()