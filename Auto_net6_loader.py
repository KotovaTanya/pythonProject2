import random
import time
from datetime import datetime
import ThreadPoolExecutorPlus
from selenium import webdriver
from selenium.webdriver.common.by import By

def auth():
    # Открытие браузера
    browser = webdriver.Chrome()
    start_datatime = datetime.now().time()
    print("Начало теста в " + str(start_datatime))
    browser.get("http://10.11.3.145:7981/Login/Login")
    time.sleep(2)
    browser.implicitly_wait(2)
    login = browser.find_element(By.NAME, "login")
    password = browser.find_element(By.NAME, "pwd")
    # Ввод логина и пароля
    login.send_keys("regionAdmin")
    time.sleep(3)
    password.send_keys("123456")
    time.sleep(3)
    browser.implicitly_wait(2)
    browser.find_element(By.CLASS_NAME, "pull-right").click()
    browser.implicitly_wait(3)

    # Смена области видимости
    browser.find_element(By.ID, "scopeLink").click()
    browser.implicitly_wait(4)
    time.sleep(2)
    region = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    browser.implicitly_wait(4)
    time.sleep(2)
    region.click()

    # Выбор муниципалитета
    browser.implicitly_wait(2)
    time.sleep(3)
    municipallity = browser.find_element(By.ID, "s2id_autogen1")
    browser.implicitly_wait(2)
    time.sleep(3)
    municipallity.click()

    # Список муниципалитетов для ввода
    municipality_list = ["Фрунзенский район", "Приморский район", "Московский район", "Красносельский район",
                         "Центральный район", "Пушкинский район"]

    time.sleep(3)
    browser.implicitly_wait(2)
    municipallity_l = browser.find_element(By.CSS_SELECTOR, ".select2-focused")

    time.sleep(3)

    # Рандомный выбор муниципалитета из списка
    i = random.randint(0, len(municipality_list) - 1)
    choice_municipallity_random = municipality_list[i]
    municipallity_l.send_keys(choice_municipallity_random + "\n")
    print(str(datetime.now().time()) + " Муниципалитет выбран")
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(3)
    browser.implicitly_wait(4)
    browser.find_element(By.CSS_SELECTOR, ".btn:nth-child(3) > .head-menu-a").click()
    browser.implicitly_wait(3)
    time.sleep(3)
    # Клик на меню Реестры
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, "#sidebar_ul > .ng-scope:nth-child(13) > a").click()
    time.sleep(3)

    # Выбор заявлений
    if choice_municipallity_random == "Фрунзенский район":
        # Заявление принято к рассмотрению, без льгот
        inquiry_numbers_list = ["2207255563459", "2207258797889", "2207256587080", "2207251621315", "2207258604005",
                                "2207258433047"]
        inquiry_numbers = ["40296/ЗЗ/2207255563459", "40296/ЗЗ/2207258797889", "40296/ЗЗ/2207256587080",
                           "40296/ЗЗ/2207251621315", "40296/ЗЗ/2207258604005", "40296/ЗЗ/2207258433047"]
    elif choice_municipallity_random == "Приморский район":
        # Заявление принято к рассмотрению, без льгот
        inquiry_numbers_list = ["19082556248", "190825355459", "190825346460", "190825340607", "190825328355",
                                "190825317697"]
        inquiry_numbers = ["40294/ЗЗ/19082556248", "40294/ЗЗ/190825355459", "40294/ЗЗ/190825346460",
                           "40294/ЗЗ/190825340607", "40294/ЗЗ/190825328355", "40294/ЗЗ/190825317697"]
    elif choice_municipallity_random == "Московский район":
        # Заявление принято к рассмотрению, без льгот
        inquiry_numbers_list = ["2010223507", "2204211784584", "2207197542723", "2207165499716", "2207180394475",
                                "2207185604405"]
        inquiry_numbers = ["40279/ЗЗ/2010223507", "40284/ЗЗ/2204211784584", "40284/ЗЗ/2207197542723",
                           "40284/ЗЗ/2207165499716", "40284/ЗЗ/2207180394475", "40284/ЗЗ/2207185604405"]
    elif choice_municipallity_random == "Красносельский район":
        # Заявление принято к рассмотрению, без льгот
        inquiry_numbers_list = ["2004241669", "2108177988", "2204077110480", "2204274553272", "2111286076322",
                                "2012163020"]
        inquiry_numbers = ["40296/ЗЗ/2004241669", "40296/ЗЗ/2108177988", "40279/ЗЗ/2204077110480",
                           "40279/ЗЗ/2204274553272", "40279/ЗЗ/2111286076322", "40265/ЗЗ/2012163020"]
    elif choice_municipallity_random == "Центральный район":
        inquiry_numbers_list = ["2207209403851", "2207204880466", "2207206883968", "2207203464450", "2207205509979",
                                "2207218523705"]
        inquiry_numbers = ["40298/ЗЗ/2207209403851", "40298/ЗЗ/2207204880466", "40298/ЗЗ/2207206883968",
                           "40298/ЗЗ/2207203464450", "40298/ЗЗ/2207205509979", "40298/ЗЗ/2207218523705"]
    elif choice_municipallity_random == "Пушкинский район":
        inquiry_numbers_list = ["2106154151", "2109154707", "2208162380609", "2111090594047", "2109103889",
                                "2109084436"]
        inquiry_numbers = ["40294/ЗЗ/2106154151", "40294/ЗЗ/2109154707", "40000/ЗЗ/2208162380609",
                           "40294/ЗЗ/2111090594047", "40294/ЗЗ/2109103889", "40294/ЗЗ/2109084436"]
    else:
        print("Выбран неверный муниципалитет")
# Общий список для запросов  ('40296/ЗЗ/2207255563459', '40296/ЗЗ/2207258797889', '40296/ЗЗ/2207256587080','40296/ЗЗ/2207251621315','40296/ЗЗ/2207258604005','40296/ЗЗ/2207258433047','40294/ЗЗ/19082556248','40294/ЗЗ/190825355459','40294/ЗЗ/190825346460','40294/ЗЗ/190825340607','40294/ЗЗ/190825328355','40294/ЗЗ/190825317697','40279/ЗЗ/2010223507','40284/ЗЗ/2204211784584','40284/ЗЗ/2207197542723','40284/ЗЗ/2207165499716','40284/ЗЗ/2207180394475','40284/ЗЗ/2207185604405','40296/ЗЗ/2004241669','40296/ЗЗ/2108177988','40279/ЗЗ/2204077110480','40279/ЗЗ/2204274553272','40279/ЗЗ/2111286076322','40265/ЗЗ/2012163020','40298/ЗЗ/2207209403851','40298/ЗЗ/2207204880466','40298/ЗЗ/2207206883968','40298/ЗЗ/2207203464450', '40298/ЗЗ/2207205509979', '40298/ЗЗ/2207218523705', '40294/ЗЗ/2106154151', '40294/ЗЗ/2109154707', '40000/ЗЗ/2208162380609', '40294/ЗЗ/2111090594047', '40294/ЗЗ/2109103889', '40294/ЗЗ/2109084436')
    # Клик на раздел Заявления
    browser.find_element(By.CSS_SELECTOR, ".ng-scope > ul > .ng-scope:nth-child(8) .ng-scope").click()
    time.sleep(3)
    browser.implicitly_wait(4)
    browser.find_element(By.LINK_TEXT, "Дошкольники").click()
    time.sleep(4)
    browser.implicitly_wait(4)
    browser.find_element(By.CLASS_NAME, "select2-container.form-control.ng-valid.ng-valid-required.ng-dirty").click()
    time.sleep(4)
    browser.implicitly_wait(4)
    browser.find_element(By.CLASS_NAME, "select2-focused").send_keys("Номер" + "\n")
    time.sleep(3)

    # Запоминаем индекс, выбранный для списка
    inquiry_index = random.randint(0, len(inquiry_numbers_list) - 1)
    print(inquiry_index)
    inquiry_number_filter = inquiry_numbers_list[inquiry_index]
    inquiry_number = inquiry_numbers[inquiry_index]
    print(str(datetime.now().time()) + " Муниципалитет:" + choice_municipallity_random + "\n" + "Номер заявления " + inquiry_number + "\n")
    time.sleep(3)
    browser.find_element(By.CLASS_NAME, "form-control:nth-child(5)").send_keys(inquiry_number_filter)
    time.sleep(3)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(5)
    try:
        browser.find_element(By.CLASS_NAME, "btn-primary").click()
        browser.implicitly_wait(20)
        a = browser.find_element(By.LINK_TEXT, inquiry_number)
        a.click()
        print(str(datetime.now().time()) + " Открыта карточка заявления " + inquiry_number)
        open_inquiry_data = input("Введите данные после открытия карточки заявления")
        time.sleep(10)
    except:
        print("Не загрузился список заявлений. Попытка номер 2")
        browser.implicitly_wait(30)
        try:
            browser.find_element(By.CLASS_NAME, "btn-primary").click()
            browser.implicitly_wait(30)
            browser.find_element(By.LINK_TEXT, inquiry_number).click()
            print("Открыта карточка заявления " + inquiry_number)
            open_inquiry_data = input("Введите данные после открытия карточки заявления")
            time.sleep(10)
        except:
            print("Не загрузился список заявлений. Попытка номер 3")
            try:
                browser.implicitly_wait(30)
                browser.find_element(By.LINK_TEXT, inquiry_number).click()
                print("Открыта карточка заявления " + inquiry_number)
                open_inquiry_data = input("Введите данные после открытия карточки заявления")
                time.sleep(10)
            except:
                print("Не загрузился список заявлений")
    time.sleep(2)

    # Редактирование льготы
    browser.implicitly_wait(10)
    browser.find_element(By.CLASS_NAME, "btn-group:nth-child(1)>.dropdown-toggle").click()
    time.sleep(3)
    browser.implicitly_wait(15)
    browser.find_element(By.LINK_TEXT, "Заявление").click()
    print(str(datetime.now().time()) + " Открыто редактирование заявления " + inquiry_number)
    time.sleep(4)


    # Редактирование льготы  - добавить льготу
    browser.implicitly_wait(4)
    browser.find_element(By.ID, 'privilege').click()
    print(str(datetime.now().time()) + " Открыто редактирование льготы " + inquiry_number)
    time.sleep(4)
    browser.find_element(By.CLASS_NAME, "pull-right").click()
    time.sleep(2)
    browser.implicitly_wait(15)
    browser.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(4) .col-md-12>div").click()
    print(str(datetime.now().time()) + " Добавлена льгота для заявления " + inquiry_number)
    time.sleep(4)
    browser.implicitly_wait(4)
    browser.find_element(By.CSS_SELECTOR, ".form-horizontal:nth-child(6) .btn-primary").click()
    time.sleep(5)
    try:
        browser.find_element(By.LINK_TEXT, "Просмотр").click()
        browser.implicitly_wait(1)
        print("Возврат к карточке заявления")
    except:
        print("Не возвращена карточка заявления")
    time.sleep(2)

    # Удаление льготы
    time.sleep(5)
    browser.implicitly_wait(15)
    browser.find_element(By.CLASS_NAME, "btn-group:nth-child(1)>.dropdown-toggle").click()
    time.sleep(3)
    browser.implicitly_wait(1)
    browser.find_element(By.LINK_TEXT, "Заявление").click()
    print(str(datetime.now().time()) + " Открыто редактирование заявления " + inquiry_number)
    time.sleep(4)
    browser.implicitly_wait(40)
    browser.find_element(By.CSS_SELECTOR, ".icon-trash").click()
    time.sleep(5)
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, ".modal-footer>.btn-primary").click()
    print(str(datetime.now().time()) + " Удалена льгота у заявления " + inquiry_number)
    time.sleep(5)
    try:
        browser.implicitly_wait(15)
        browser.find_element(By.LINK_TEXT, "Просмотр").click()
        print(str(datetime.now().time()) + " Возврат к карточке заявления")
        edit_privilige_data = input("Введите данные после редактирования льготы")
        time.sleep(10)
    except:
        print("Не возвращена карточка заявления")
        try:
            browser.implicitly_wait(15)
            browser.find_element(By.LINK_TEXT, "Просмотр").click()
            print("Возврат к карточке заявления")
            edit_privilige_data = input("Введите данные после редактирования льготы")
            time.sleep(10)
        except:
            print("Не возвращена карточка заявления")
    time.sleep(3)

    # Редактирование заявителя
    browser.implicitly_wait(15)
    browser.find_element(By.CLASS_NAME, "btn-group:nth-child(1)>.dropdown-toggle").click()
    time.sleep(3)
    browser.implicitly_wait(10)
    browser.find_element(By.LINK_TEXT, "Заявитель").click()
    print(str(datetime.now().time()) + " Открыто редактирование заявителя " + inquiry_number)
    time.sleep(3)
    browser.implicitly_wait(3)
    # Редактирование email
    mail_applicant = browser.find_element (By.ID, "applicantInfoContactInfoEmail")
    time.sleep(1)
    mail_applicant.clear()
    time.sleep(3)
    mail_applicant.send_keys("mail@mail.ru")
    time.sleep(3)
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, ".controls:nth-child(1) label").click()
    time.sleep(3)
    browser.implicitly_wait(3)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary.ng-binding").click()
    time.sleep(3)
    browser.implicitly_wait(3)
    print(str(datetime.now().time()) + " Параметры заявителя в заявлении " + inquiry_number + " изменены:" + "\n" + "Email: mail@mail.ru" + "\n" + "Чекбокс - Адрес ребенка и заявителя совпадают:Да")

    try:
        time.sleep(3)
        browser.implicitly_wait(15)
        browser.find_element(By.LINK_TEXT, "Просмотр").click()
        browser.implicitly_wait(1)
        print(str(datetime.now().time()) + " Возврат к карточке заявления")
    except:
        print("Не возвращена карточка заявления")
    time.sleep(2)

    # Возврат к редактированию заявителя
    time.sleep(5)
    browser.implicitly_wait(15)
    browser.find_element(By.CLASS_NAME, "btn-group:nth-child(1)>.dropdown-toggle").click()
    time.sleep(5)
    browser.implicitly_wait(15)
    browser.find_element(By.LINK_TEXT, "Заявитель").click()
    print(str(datetime.now().time()) + " Открыто редактирование заявителя " + inquiry_number)
    time.sleep(3)
    browser.implicitly_wait(3)

    # Редактирование заявителя - возврат email
    mail_applicant = browser.find_element (By.ID, "applicantInfoContactInfoEmail")
    mail_applicant.clear()
    time.sleep(2)
    mail_applicant.send_keys("123mail@mail.ru")
    time.sleep(3)
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, ".controls:nth-child(1) label").click()
    time.sleep(3)
    browser.implicitly_wait(3)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary.ng-binding").click()
    time.sleep(3)
    browser.implicitly_wait(3)
    print(str(datetime.now().time()) + " Параметры заявителя в заявлении " + inquiry_number + " изменены:" + "\n" + "Email: 123mail@mail.ru" + "\n" + "Чекбокс - Адрес ребенка и заявителя совпадают:Нет")
    try:
        time.sleep(3)
        browser.implicitly_wait(15)
        browser.find_element(By.LINK_TEXT, "Просмотр").click()
        print("Возврат к карточке заявления")
        edit_applicant_data = input("Введите данные после редактирования заявителя")
        time.sleep(10)
    except:
        print("Не возвращена карточка заявления")
    time.sleep(2)

    # Редактирование желаемых параметров (ЖДЗ)
    time.sleep(4)
    browser.implicitly_wait(60)
    browser.find_element(By.CLASS_NAME, "btn-group:nth-child(1)>.dropdown-toggle").click()
    time.sleep(1)
    browser.implicitly_wait(20)
    browser.find_element(By.LINK_TEXT, "Желаемые параметры").click()
    print(str(datetime.now().time()) + " Открыто редактирование желаемых параметров " + inquiry_number + "\n")
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "span:nth-child(1)>.btn").click()
    time.sleep(2)
    change_wish_date = "30.09.2025"
    browser.find_element(By.ID, "wishParamsWithSpecsWishDate").send_keys(change_wish_date + "\n")
    time.sleep(2)
    browser.implicitly_wait(60)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    print(str(datetime.now().time()) + " ЖДЗ заявление " + inquiry_number + " изменено на " + change_wish_date + "\n")
    time.sleep(10)
    browser.implicitly_wait(60)
    browser.find_element(By.ID, "WishStayMode").click()
    time.sleep(4)
    browser.implicitly_wait(60)
    browser.find_element(By.CSS_SELECTOR, "#WishStayMode:nth-child(1)>option:nth-child(2)").click()
    print(str(datetime.now().time()) + " Режим пребывания изменен на Круглосуточного пребывания" + "\n")
    time.sleep(5)

    # Редактирование предпочитанмых
    time.sleep(5)
    browser.implicitly_wait(20)
    browser.find_element(By.CSS_SELECTOR, "[ng-click='addWishInstitution()']").click()
    time.sleep(4)
    time.sleep(4)
    browser.find_element(By.CLASS_NAME, "select2-choice").click()
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR,".select2-drop.select2-with-searchbox.select2-drop-active .select2-input").send_keys("1" + "\n")
    time.sleep(4)
    new_wish_org = browser.find_element(By.CSS_SELECTOR,".select2-container.ng-valid.ng-valid-required.ng-dirty >.select2-choice").text
    print(str(datetime.now().time()) + " Добавлена предпочитаемая организация " + new_wish_org + "\n")
    time.sleep(3)
    browser.implicitly_wait(20)
    browser.find_element(By.CSS_SELECTOR, "[ng-click='Editing.WishDistributionParams.Wish.Commit()']").click()
    time.sleep(6)
    browser.implicitly_wait(20)
    browser.find_element(By.CSS_SELECTOR,".widget-content.ng-valid-validator.ng-dirty.ng-valid.ng-valid-required > .form-horizontal > .form-actions > .btn.btn-primary.ng-binding").click()
    print(str(datetime.now().time()) + " Сохранена новая предпочитаемая организация " + new_wish_org + "\n")

    # Вывод всех предпочитаемых
    time.sleep(7)
    browser.implicitly_wait(20)
    list_wish_organization = browser.find_elements(By.CSS_SELECTOR,
                                                   "[loader='wishInstitutions'] span[class='ng-scope']")
    len_list_wish_organization = len(list_wish_organization)
    for i in list_wish_organization:
        a = i.text
        print("Предпочитаемые: " + a)
    time.sleep(2)
    try:
        time.sleep(2)
        browser.implicitly_wait(15)
        browser.find_element(By.LINK_TEXT, "Просмотр").click()
        print(str(datetime.now().time()) + " Возврат к карточке заявления" + "\n")
    except:
        print("Не возвращена карточка заявления")
    time.sleep(2)

    # Вернуть параметры обратно
    browser.implicitly_wait(60)
    browser.find_element(By.CLASS_NAME, "btn-group:nth-child(1)>.dropdown-toggle").click()
    time.sleep(1)
    browser.implicitly_wait(20)
    browser.find_element(By.LINK_TEXT, "Желаемые параметры").click()
    print(str(datetime.now().time()) + " Открыто редактирование желаемых параметров " + inquiry_number + "\n")
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "span:nth-child(1)>.btn").click()
    time.sleep(3)
    change_wish_date = "01.11.2022"
    browser.find_element(By.ID, "wishParamsWithSpecsWishDate").send_keys(change_wish_date + "\n")
    time.sleep(3)
    browser.implicitly_wait(60)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    print(str(datetime.now().time()) + " ЖДЗ заявление " + inquiry_number + "изменено на " + change_wish_date)
    time.sleep(10)
    browser.implicitly_wait(60)
    browser.find_element(By.ID, "WishStayMode").click()
    time.sleep(4)
    browser.implicitly_wait(60)
    browser.find_element(By.CSS_SELECTOR, "#WishStayMode:nth-child(1)>option:nth-child(1)").click()
    print(str(datetime.now().time()) + " Режим пребывания изменен на Полный день" + "\n")

    # Удаление новой предпочитаемой
    time.sleep(7)
    browser.implicitly_wait(15)
    browser.find_element(By.CSS_SELECTOR,
                         f".ng-scope:nth-child({len_list_wish_organization})>.btn-group >.btn:nth-child(3)").click()
    time.sleep(7)
    browser.implicitly_wait(15)
    browser.find_element(By.CSS_SELECTOR, "[aria-hidden='false'] .modal-footer>.btn-primary").click()
    time.sleep(6)
    browser.implicitly_wait(20)
    browser.find_element(By.CSS_SELECTOR,
                         ".widget-content.ng-valid-validator.ng-dirty.ng-valid.ng-valid-required > .form-horizontal > .form-actions > .btn.btn-primary.ng-binding").click()
    print(str(datetime.now().time()) + " Удалена новая предпочитаемая организация " + new_wish_org + "\n")
    try:
        time.sleep(3)
        browser.implicitly_wait(1)
        browser.find_element(By.LINK_TEXT, "Просмотр").click()
        print(str(datetime.now().time()) + " Возврат к карточке заявления")
        edit_wish_param_data = input("Введите данные после редактирования предпочитаемых" + "\n")
        time.sleep(10)
    except:
        print("Не возвращена карточка заявления")
    time.sleep(2)
    try:
        time.sleep(4)
        browser.implicitly_wait(30)
        name_status = "Заявление рассмотрено"
        browser.find_element(By.XPATH, "//div[2]/div[2]/div/div/select").click()
        print(str(datetime.now().time()) + " Автотест нашел статус " + name_status)
        time.sleep(4)
        browser.implicitly_wait(5)
        browser.find_element(By.LINK_TEXT, "Выполнить").click()
        time.sleep(4)
        browser.implicitly_wait(15)
        browser.find_element(By.CSS_SELECTOR, "[name = 'comment']").send_keys("Проверка перехода статуса автотестом")
        time.sleep(4)
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, "//*[text()='Подтвердить']").click()
        time.sleep(4)
        print(str(datetime.now().time()) + " Заявление  " + inquiry_number + "перешло в статус " + name_status)
        # После Заявление рассмотрено - переходим в Отмену по запросу заявителя
        time.sleep(10)
        browser.implicitly_wait(20)
        browser.find_element(By.XPATH, "//div[2]/div[2]/div/div/select").click()
        time.sleep(4)
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, "[ng-model='group.selectedCommand'] option:nth-child(2)").click()
        time.sleep(4)
        browser.implicitly_wait(5)
        browser.find_element(By.LINK_TEXT, "Выполнить").click()
        time.sleep(4)
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, "//*[text()='Подтвердить']").click()
        print(
            str(datetime.now().time()) + " Заявление  " + inquiry_number + "перешло в статус Отмену по запросу заявителя")
        time.sleep(10)
        browser.implicitly_wait(5)
        browser.find_element(By.LINK_TEXT, "Выполнить").click()
        time.sleep(3)
        print(str(datetime.now().time()) + " Заявление вернулось в статус Заявление принято к рассмотрению")
    except:
        print("Автотест не нашел статус " + name_status)

    print("Автотест прошел успешно " + inquiry_number)
    browser.close()
    end_data = input('Введите конечное значение')
    end_datatime = datetime.now().time()
    print("Окончание теста в  " + str(end_datatime) + "\n")
    print("До открытия заявления: " + "\n" + "Начальное: " + start_data + "\n" + "Конечное: " + open_inquiry_data)
    print("Редактирование льготы: " + "\n" + "Начальное: " + open_inquiry_data + "\n" + "Конечное: " + edit_privilige_data)
    print("Редактирование заявителя:" + "\n" + "Начальное: " + edit_privilige_data + "\n" + "Конечное: " + edit_applicant_data)
    print("Редактирование желаемых параметров" + "\n" + "Начальное: " + edit_applicant_data + "\n" + "Конечное: " + edit_wish_param_data)
    print("Переходы по статусам" + "\n" + "Начальное: " + edit_wish_param_data + "\n" + "Конечное: " + end_data)


start_data = input("Введите начальные измерения " + "\n")
executors_list = []
with ThreadPoolExecutorPlus.ThreadPoolExecutor(max_workers=5) as executor:
    executors_list.append(executor.submit(auth))
    time.sleep(4)
    executors_list.append(executor.submit(auth))
    time.sleep(4)
    executors_list.append(executor.submit(auth))
    time.sleep(4)
    executors_list.append(executor.submit(auth))
    time.sleep(4)
    executors_list.append(executor.submit(auth))