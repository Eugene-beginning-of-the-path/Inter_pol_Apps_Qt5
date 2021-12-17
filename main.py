#pip freeze > requirements.txt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtWidgets
from datetime import datetime
import pymysql
import Authorization
import CompletedTable
import CrimeTable
import InfoAboutMenu
import Interpol
import MafiaTable
import Menu
import User
import MySQL_config

authorization_time = ''
counter_rows_crimeTable = 8
counter_rows_mafiaTable = 10
counter_rows_completedTable = 2


class AuthorizationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.this_window = Authorization.Ui_MainWindow()
        self.this_window.setupUi(self)
        self.this_window.login_Button.clicked.connect(self.actionLoginButton) #Сначала пытался вызвать функцию, а надо передать ее
                                                                              #в переменную параметра

    def actionLoginButton(self):
        global authorization_time
        authorization_time = str(current_datatime.hour) + ':' + str(current_datatime.minute) + ':' + str(
            current_datatime.second)
        if(self.this_window.user.toPlainText() != "Clint" and self.this_window.password.toPlainText() != "Guard1"):
            menu_2.show()
            menu_2.setDataInLabels()
            self.close()
        else:
            self.this_window.user.setPlainText("Data entered incorrectly")
            self.this_window.password.setPlainText("Access is blocked")

class MenuWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.this_window = Menu.Ui_Dialog()
        self.this_window.setupUi(self)
        self.this_window.InterpolButton.clicked.connect(self.actionInterpolButton)
        self.this_window.UserButton.clicked.connect(self.actionUserButton)
        self.this_window.aboutWin_Button.clicked.connect(self.actionAboutWinButton)
        self.this_window.CrimeTable_Button.clicked.connect(self.ationCrimeTableButton)
        self.this_window.MafiaTable_Button.clicked.connect(self.ationMafiaTableButton)
        self.this_window.CompletedTable_Button.clicked.connect(self.ationCompletedTableButton)
        self.this_window.exit_Button.clicked.connect(self.ationExitButton)
        self.this_window.refresh_Button.clicked.connect(self.actionRefreshButton)

    def ationExitButton(self):
        self.close()

    def actionAboutWinButton(self):
        infoaboutmenu_5.show()

    def ationCompletedTableButton(self):
        self.close()
        completedtable_8.show()

    def ationCrimeTableButton(self):
        self.close()
        crimetable_6.show()

    def ationMafiaTableButton(self):
        self.close()
        mafiatable_7.show()

    def actionInterpolButton(self):
        interpol_3.show()

    def actionUserButton(self):
        user_4.show()

    def actionRefreshButton(self):
        self.this_window.counter_crime.setText(str(counter_rows_crimeTable))
        self.this_window.counter_mafia.setText(str(counter_rows_mafiaTable))
        self.this_window.counter_completed.setText(str(counter_rows_completedTable))

    def setDataInLabels(self):
        self.this_window.label_9.setText(authorization_time) #authorization_time - уже конвертировано в str
        self.this_window.counter_crime.setText(str(counter_rows_crimeTable)) #QLabel может в себе содержать только строки
        self.this_window.counter_mafia.setText(str(counter_rows_mafiaTable))
        self.this_window.counter_completed.setText(str(counter_rows_completedTable))

class InterpolWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.this_window = Interpol.Ui_Dialog()
        self.this_window.setupUi(self)
        self.this_window.exit_Button.clicked.connect(self.actionExitButton)

    def actionExitButton(self):
        self.close()

class UserWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.this_window = User.Ui_Dialog()
        self.this_window.setupUi(self)
        self.this_window.exit_Button.clicked.connect(self.actionExitButton)

    def actionExitButton(self):
        self.close()

class InfoAboutMenuWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.this_window = InfoAboutMenu.Ui_Dialog()
        self.this_window.setupUi(self)
        self.this_window.exit_Button.clicked.connect(self.actionExitButton)

    def actionExitButton(self):
        self.close()

class CrimeTableWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.this_window = CrimeTable.Ui_Dialog()
        self.this_window.setupUi(self)
        self.connect_MySQL()
        self.this_window.exit_Button.clicked.connect(self.actionExitButton)
        self.this_window.deleteInfo_Button.clicked.connect(self.actionDeleteInfoButton)
        self.this_window.refreshInfo_Button.clicked.connect(self.actionRefreshButton)
        self.this_window.addInfo_Button.clicked.connect(self.actionAddInfoButton)
        self.this_window.deleteInfo_Button_2.clicked.connect(self.actionMoveToCompletedButton)

        self.this_window.name_sortButton.clicked.connect(self.actionname_sortButton_DESC)
        self.this_window.NickName_sortButton.clicked.connect(self.actionNickname_sortButton_DESC)
        self.this_window.surname_sortButton.clicked.connect(self.actionSurname_sortButton_DESC)
        self.this_window.height_sortButton.clicked.connect(self.actionHeight_sortButton_DESC)
        self.this_window.eyecolor_sortButton.clicked.connect(self.actionEyeColor_sortButton_DESC)
        self.this_window.specialSigns_sortButton.clicked.connect(self.actionSpecialSigns_sortButton_DESC)
        self.this_window.Citizenship_sortButton.clicked.connect(self.actionCitizenship_sortButton_DESC)
        self.this_window.placeOfBirth_sortButton.clicked.connect(self.actionPlaceOfBirth_sortButton_DESC)
        self.this_window.languages_sortButton.clicked.connect(self.actionLanguages_sortButton_DESC)
        self.this_window.lastCase_sortButton.clicked.connect(self.actionLastCase_sortButton_DESC)
        # self.this_window.lastCase_sortButton.mouseDoubleClickEvent(self, self.actionLastCase_sortButton_ASC)
        self.this_window.crimincalActivity_sortButton.clicked.connect(self.actionCriminalActivity_sortButton_DESC)
        self.this_window.birth_sortButton.clicked.connect(self.actionBirth_sortButton_DESC)

    #Метод для подключения DataBase
    def connect_MySQL(self):
        self.connect = pymysql.connect(host = MySQL_config.local_host,
                                       port= MySQL_config.local_port,
                                       user= MySQL_config.local_user,
                                       passwd= MySQL_config.local_passwd,
                                       db= MySQL_config.database)

        self.cursor = self.connect.cursor()
        query = "SELECT * FROM `crimetable`"
        self.this_window.tableWidget.setRowCount(counter_rows_crimeTable)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    #Метод для сокращения кода
    def forQuery(self, rows):
        index = 0
        for row in rows:
            self.this_window.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.this_window.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.this_window.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.this_window.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.this_window.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.this_window.tableWidget.setItem(index, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.this_window.tableWidget.setItem(index, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.this_window.tableWidget.setItem(index, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.this_window.tableWidget.setItem(index, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.this_window.tableWidget.setItem(index, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.this_window.tableWidget.setItem(index, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.this_window.tableWidget.setItem(index, 11, QtWidgets.QTableWidgetItem(row[11]))
            self.this_window.tableWidget.setItem(index, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.this_window.tableWidget.setItem(index, 13, QtWidgets.QTableWidgetItem(row[13]))
            index += 1

    ############ DESC (по убыванию) ############
    def actionname_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY name DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionNickname_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY nickname DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionSurname_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY surname DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionHeight_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY height DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionEyeColor_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY eye_color DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionSpecialSigns_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY special_signs DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionCitizenship_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY citizenship DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionPlaceOfBirth_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY place_of_birth DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionLanguages_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY languages DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionLastCase_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY last_case DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionCriminalActivity_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY criminal_activity DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionBirth_sortButton_DESC(self):
        query = "SELECT * FROM crimetable ORDER BY birth DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    ############ Action Button ############
    def actionAddInfoButton(self):
        name = self.this_window.Name_Label.toPlainText()
        nickname = self.this_window.NickName_Label.toPlainText()
        surname = self.this_window.Sername_Label.toPlainText()
        height = self.this_window.Height_Label.toPlainText()
        hairColor = self.this_window.HairColor_Label.toPlainText()
        eyeColor = self.this_window.EyeColor_Label.toPlainText()
        specialSigns = self.this_window.SpecialSigns_Label.toPlainText()
        citizenship = self.this_window.Citizenship_Label.toPlainText()
        placeOfBirth = self.this_window.PlaceOfBirth_Label.toPlainText()
        languages = self.this_window.Languages_Label.toPlainText()
        criminalActivity = self.this_window.CriminalActivity_Label.toPlainText()
        lastCase = self.this_window.LastCase_Label.toPlainText()
        birth = self.this_window.Birth_Label.toPlainText()
        alive = "Жив"

        query = "INSERT INTO  crimetable\
                (name, surname, nickname, height, hair_color, \
                eye_color, special_signs, citizenship, place_of_birth,  \
                languages, criminal_activity, last_case, birth, Status) \
                VALUES \
                (  \
                  '{name}', '{surname}', '{nickname}', '{height}', '{hairColor}', '{eyeColor}', '{specialSigns}', \
                  '{citizenship}', '{placeOfBirth}',\
                  '{languages}', '{criminalActivity}', '{lastCase}', '{birth}', '{alive}' \
                )".format(name=name, surname=surname, nickname=nickname, height=height, hairColor=hairColor, eyeColor=eyeColor,
                          specialSigns=specialSigns, citizenship=citizenship, placeOfBirth=placeOfBirth,
                          languages=languages, criminalActivity=criminalActivity, lastCase=lastCase, birth=birth,
                          alive=alive)

        #query = "INSERT INTO  crimetable (name) VALUES ( (?) )"

        self.cursor.execute(query)
        self.connect.commit() #сохраним изменения на сервере

        global counter_rows_crimeTable
        counter_rows_crimeTable += 1

    def actionRefreshButton(self):
        self.cursor = self.connect.cursor()
        query = "SELECT * FROM `crimetable`"
        self.this_window.tableWidget.setRowCount(counter_rows_crimeTable)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionDeleteInfoButton(self):
        currentRow = self.this_window.tableWidget.currentRow()
        self.this_window.tableWidget.removeRow(currentRow)

        query = "DELETE FROM crimetable WHERE `id` = {};".format(currentRow + 1) #AND 'Status'='Мертв'

        self.cursor.execute(query)

        self.connect.commit()

        global counter_rows_crimeTable
        counter_rows_crimeTable -= 1
        #   ALTER TABLE crimetable DROP COLUMN id; ALTER TABLE completedtable DROP COLUMN id; ALTER TABLE mafiatable DROP COLUMN id;

        #   ALTER TABLE completedtable ADD id INT AUTO_INCREMENT PRIMARY KEY; ALTER TABLE crimetable ADD id INT AUTO_INCREMENT PRIMARY KEY; ALTER TABLE mafiatable ADD id INT AUTO_INCREMENT PRIMARY KEY;

    def actionMoveToCompletedButton(self):
        currentRow = self.this_window.tableWidget.currentRow()
        self.this_window.tableWidget.removeRow(currentRow)
        query = "insert into completedtable select * from crimetable where id = {};".format(currentRow + 1)
        self.cursor.execute(query)
        #self.connect.commit()
        query = "DELETE FROM `crimetable` WHERE `crimetable`.`id` = {};".format(currentRow + 1)
        self.cursor.execute(query)
        self.connect.commit()

        global counter_rows_crimeTable, counter_rows_completedTable
        counter_rows_crimeTable -= 1
        counter_rows_completedTable += 1


    def actionExitButton(self):
        self.close()
        menu_2.show()

class MafiaTableWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.this_window = MafiaTable.Ui_Dialog()
        self.this_window.setupUi(self)
        self.connect_MySQL()
        self.this_window.exit_Button.clicked.connect(self.actionExitButton)
        self.this_window.deleteInfo_Button.clicked.connect(self.actionDeleteInfoButton)
        self.this_window.refreshInfo_Button.clicked.connect(self.actionRefreshButton)
        self.this_window.addInfo_Button.clicked.connect(self.actionAddInfoButton)

        self.this_window.name_sortButton.clicked.connect(self.actionname_sortButton_DESC)
        self.this_window.NickName_sortButton.clicked.connect(self.actionNickname_sortButton_DESC)
        self.this_window.surname_sortButton.clicked.connect(self.actionSurname_sortButton_DESC)
        self.this_window.height_sortButton.clicked.connect(self.actionHeight_sortButton_DESC)
        self.this_window.eyecolor_sortButton.clicked.connect(self.actionEyeColor_sortButton_DESC)
        self.this_window.specialSigns_sortButton.clicked.connect(self.actionSpecialSigns_sortButton_DESC)
        self.this_window.Citizenship_sortButton.clicked.connect(self.actionCitizenship_sortButton_DESC)
        self.this_window.placeOfBirth_sortButton.clicked.connect(self.actionPlaceOfBirth_sortButton_DESC)
        self.this_window.languages_sortButton.clicked.connect(self.actionLanguages_sortButton_DESC)
        self.this_window.lastCase_sortButton.clicked.connect(self.actionLastCase_sortButton_DESC)
        # self.this_window.lastCase_sortButton.mouseDoubleClickEvent(self, self.actionLastCase_sortButton_ASC)
        self.this_window.crimincalActivity_sortButton.clicked.connect(self.actionCriminalActivity_sortButton_DESC)
        self.this_window.birth_sortButton.clicked.connect(self.actionBirth_sortButton_DESC)
        self.this_window.deleteInfo_Button_2.clicked.connect(self.actionMoveToCompletedButton)

        # Метод для подключения DataBase

    def connect_MySQL(self):
        self.connect = pymysql.connect(host=MySQL_config.local_host,
                                       port=MySQL_config.local_port,
                                       user=MySQL_config.local_user,
                                       passwd=MySQL_config.local_passwd,
                                       db=MySQL_config.database)

        self.cursor = self.connect.cursor()
        query = "SELECT * FROM `mafiatable`"
        self.this_window.tableWidget.setRowCount(counter_rows_mafiaTable)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    # Метод для сокращения кода
    def forQuery(self, rows):
        index = 0
        for row in rows:
            self.this_window.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.this_window.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.this_window.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.this_window.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.this_window.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.this_window.tableWidget.setItem(index, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.this_window.tableWidget.setItem(index, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.this_window.tableWidget.setItem(index, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.this_window.tableWidget.setItem(index, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.this_window.tableWidget.setItem(index, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.this_window.tableWidget.setItem(index, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.this_window.tableWidget.setItem(index, 11, QtWidgets.QTableWidgetItem(row[11]))
            self.this_window.tableWidget.setItem(index, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.this_window.tableWidget.setItem(index, 13, QtWidgets.QTableWidgetItem(row[13]))
            index += 1

        ############ DESC (по убыванию) ############

    def actionname_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY name DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionNickname_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY nickname DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionSurname_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY surname DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionHeight_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY height DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionEyeColor_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY eye_color DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionSpecialSigns_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY special_signs DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionCitizenship_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY citizenship DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionPlaceOfBirth_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY place_of_birth DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionLanguages_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY languages DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionLastCase_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY last_case DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionCriminalActivity_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY criminal_activity DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionBirth_sortButton_DESC(self):
        query = "SELECT * FROM mafiatable ORDER BY birth DESC"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    ############ Action Button ############

    def actionAddInfoButton(self):
        name = self.this_window.Name_Label.toPlainText()
        nickname = self.this_window.NickName_Label.toPlainText()
        surname = self.this_window.Sername_Label.toPlainText()
        height = self.this_window.Height_Label.toPlainText()
        hairColor = self.this_window.HairColor_Label.toPlainText()
        eyeColor = self.this_window.EyeColor_Label.toPlainText()
        specialSigns = self.this_window.SpecialSigns_Label.toPlainText()
        citizenship = self.this_window.Citizenship_Label.toPlainText()
        placeOfBirth = self.this_window.PlaceOfBirth_Label.toPlainText()
        languages = self.this_window.Languages_Label.toPlainText()
        criminalActivity = self.this_window.CriminalActivity_Label.toPlainText()
        lastCase = self.this_window.LastCase_Label.toPlainText()
        birth = self.this_window.Birth_Label.toPlainText()
        alive = "Жив"

        query = "INSERT INTO  mafiatable\
                        (name, surname, nickname, height, hair_color, \
                        eye_color, special_signs, citizenship, place_of_birth,  \
                        languages, criminal_activity, last_case, birth, Status) \
                        VALUES \
                        (  \
                          '{name}', '{surname}', '{nickname}', '{height}', '{hairColor}', '{eyeColor}', '{specialSigns}', \
                          '{citizenship}', '{placeOfBirth}',\
                          '{languages}', '{criminalActivity}', '{lastCase}', '{birth}', '{alive}' \
                        )".format(name=name, surname=surname, nickname=nickname, height=height, hairColor=hairColor,
                                  eyeColor=eyeColor,
                                  specialSigns=specialSigns, citizenship=citizenship, placeOfBirth=placeOfBirth,
                                  languages=languages, criminalActivity=criminalActivity, lastCase=lastCase,
                                  birth=birth,
                                  alive=alive)

        self.cursor.execute(query)
        self.connect.commit()  # сохраним изменения на сервере

        global counter_rows_mafiaTable
        counter_rows_mafiaTable += 1

    def actionRefreshButton(self):
        self.cursor = self.connect.cursor()
        query = "SELECT * FROM `mafiatable`"
        self.this_window.tableWidget.setRowCount(counter_rows_mafiaTable)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionDeleteInfoButton(self):
        currentRow = self.this_window.tableWidget.currentRow()
        self.this_window.tableWidget.removeRow(currentRow)
        query = "DELETE FROM `mafiatable` WHERE `mafiatable`.`id` = {};".format(currentRow + 1)
        self.cursor.execute(query)
        self.connect.commit()

        global counter_rows_mafiaTable
        counter_rows_mafiaTable -= 1
        #   ALTER TABLE crimetable DROP COLUMN id; ALTER TABLE completedtable DROP COLUMN id; ALTER TABLE mafiatable DROP COLUMN id;

        #   ALTER TABLE completedtable ADD id INT AUTO_INCREMENT PRIMARY KEY; ALTER TABLE crimetable ADD id INT AUTO_INCREMENT PRIMARY KEY; ALTER TABLE mafiatable ADD id INT AUTO_INCREMENT PRIMARY KEY;

    def actionMoveToCompletedButton(self):
        currentRow = self.this_window.tableWidget.currentRow()
        self.this_window.tableWidget.removeRow(currentRow)
        query = "insert into completedtable select * from mafiatable where id = {};".format(currentRow + 1)
        self.cursor.execute(query)
        self.connect.commit()
        query = "DELETE FROM `mafiatable` WHERE `mafiatable`.`id` = {};".format(currentRow + 1)
        self.cursor.execute(query)
        self.connect.commit()

        global counter_rows_mafiaTable, counter_rows_completedTable
        counter_rows_mafiaTable -= 1
        counter_rows_completedTable += 1

    def actionExitButton(self):
        self.close()
        menu_2.show()

class CompletedTableWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.this_window = CompletedTable.Ui_Dialog()
        self.this_window.setupUi(self)
        self.connect_MySQL()
        self.this_window.exit_Button.clicked.connect(self.actionExitButton)
        self.this_window.deleteInfo_Button_2.clicked.connect(self.actionDeleteInfoButton)
        self.this_window.refreshInfo_Button.clicked.connect(self.actionRefreshButton)

        # Метод для подключения DataBase
    def connect_MySQL(self):
        self.connect = pymysql.connect(host=MySQL_config.local_host,
                                       port=MySQL_config.local_port,
                                       user=MySQL_config.local_user,
                                       passwd=MySQL_config.local_passwd,
                                       db=MySQL_config.database)

        self.cursor = self.connect.cursor()
        query = "SELECT * FROM `completedtable`"
        self.this_window.tableWidget.setRowCount(10) #counter_rows_completedTable
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

        # Метод для сокращения кода

    def forQuery(self, rows):
        index = 0
        for row in rows:
            self.this_window.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.this_window.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.this_window.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.this_window.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.this_window.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.this_window.tableWidget.setItem(index, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.this_window.tableWidget.setItem(index, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.this_window.tableWidget.setItem(index, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.this_window.tableWidget.setItem(index, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.this_window.tableWidget.setItem(index, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.this_window.tableWidget.setItem(index, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.this_window.tableWidget.setItem(index, 11, QtWidgets.QTableWidgetItem(row[11]))
            self.this_window.tableWidget.setItem(index, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.this_window.tableWidget.setItem(index, 13, QtWidgets.QTableWidgetItem(row[13]))
            index += 1

        ############ Action Button ############

    def actionRefreshButton(self):
        self.cursor = self.connect.cursor()
        query = "SELECT * FROM `completedtable`"
        self.this_window.tableWidget.setRowCount(10) #counter_rows_completedTable
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.forQuery(rows)

    def actionExitButton(self):
        self.close()
        menu_2.show()

    def actionDeleteInfoButton(self):
        currentRow = self.this_window.tableWidget.currentRow()
        self.this_window.tableWidget.removeRow(currentRow)
        query = "DELETE FROM completedtable WHERE `id` = {};".format(currentRow + 1)
        self.cursor.execute(query)
        self.connect.commit()

        global counter_rows_completedTable
        counter_rows_completedTable -= 1
        #   ALTER TABLE crimetable DROP COLUMN id; ALTER TABLE completedtable DROP COLUMN id; ALTER TABLE mafiatable DROP COLUMN id;

        #   ALTER TABLE completedtable ADD id INT AUTO_INCREMENT PRIMARY KEY; ALTER TABLE crimetable ADD id INT AUTO_INCREMENT PRIMARY KEY; ALTER TABLE mafiatable ADD id INT AUTO_INCREMENT PRIMARY KEY;


if __name__ == '__main__':
    app = QApplication(sys.argv)

    current_datatime = datetime.now()

    authorization_1 = AuthorizationWindow()
    menu_2 = MenuWindow()
    interpol_3 = InterpolWindow()
    user_4 = UserWindow()
    infoaboutmenu_5 = InfoAboutMenuWindow()
    crimetable_6 = CrimeTableWindow()
    mafiatable_7 = MafiaTableWindow()
    completedtable_8 = CompletedTableWindow()

    authorization_1.show()


    sys.exit(app.exec_())



