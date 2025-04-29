import pytest
import allure
from pages.main_page import MainPage

def test_all_faq_questions(driver):
    page = MainPage(driver)
    page.open()
    page.accept_cookies()

    questions = page.driver.find_elements(*MainPage.QUESTION_LIST)
    question_count = len(questions)

    for index in range(question_count):
        with allure.step(f"Проверка вопроса №{index + 1}"):
            page.click_question_by_index(index)
            answer_text = page.get_answer_text_by_index(index)
            allure.attach(answer_text, name=f"Ответ на вопрос №{index + 1}", attachment_type=allure.attachment_type.TEXT)
            assert answer_text.strip() != "", f"Ответ на вопрос {index + 1} пустой"
