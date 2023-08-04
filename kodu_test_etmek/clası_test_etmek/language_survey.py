from survey import AnonymousSurvey
"""Bir soru tanımla ve anket yap"""

question = "En sevdiğiniz programlama dili nedir?"

my_survey = AnonymousSurvey(question)
""" soruyu göster ve yanıtları sakla"""

my_survey.show_question()

print("Çıkmak için 'q' tuşuna basın")

while True:
    response = input("Dil: ")
    if response == 'q':
        break
    my_survey.store_response(response)

"""Anket sonuçlarını göster"""

print("\nAnkete katılan herkes için teşekkürler!")
my_survey.show_results()