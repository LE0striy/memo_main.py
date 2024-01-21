from PyQt5.QtCore import Qt, QCoreApplication 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QMessageBox,QRadioButton,QComboBox 
from random import randint 
app=QApplication([]) 
# Зберігання посилання на вікно "Транспорт" 
transport_win = None 
show_avto = None 
#створення дод вікон 
def show_paris(): 
    victory_win=QMessageBox() 
    victory_win.setText('Австрія') 
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;") 
    victory_win.setWindowTitle('Країна') 
    victory_win.exec_() 
def show_london(): 
    victory_win=QMessageBox() 
    victory_win.setText('Польща - Тут була прийнята перша Європейська Конституція') 
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;") 
    victory_win.setWindowTitle('Країна') 
    victory_win.exec_() 
def show_german(): 
    victory_win=QMessageBox() 
    victory_win.setText('Угорщина') 
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;") 
    victory_win.setWindowTitle('Країна') 
    victory_win.exec_() 
def show_itali(): 
    victory_win=QMessageBox() 
    victory_win.setText('Молдова') 
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;") 
    victory_win.setWindowTitle('Країна') 
    victory_win.exec_() 
def show_amer(): 
    victory_win=QMessageBox() 
    victory_win.setText('Північна Корея') 
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;") 
    victory_win.setWindowTitle('Країна') 
    victory_win.exec_() 
def show_litak(): 
    victory_win=QMessageBox() 
    victory_win.setText('Вірно ти виграв!') 
    victory_win.setWindowTitle('Час та кошти') 
    victory_win.exec_() 
def show_korabel(): 
    victory_win=QMessageBox() 
    victory_win.setText('Ні 2015 ти мав вибрати!') 
    victory_win.setWindowTitle('Час та кошти') 
    victory_win.exec_() 
def show_poizd(): 
    victory_win=QMessageBox() 
    victory_win.setText('Ні 2015 ти мав вибрати!') 
    victory_win.setWindowTitle('Час та кошти') 
    victory_win.exec_() 
def show_car(): 
    victory_win=QMessageBox() 
    victory_win.setText('Ні 2015 ти мав вибрати!') 
    victory_win.setWindowTitle('Час та кошти') 
    victory_win.exec_() 
def show_info(message): 
    info_win = QMessageBox() 
    info_win.setText(message) 
    info_win.setStyleSheet("font-size: 16px; font-weight: bold;") 
    info_win.setWindowTitle('Інформація') 
    info_win.exec_() 
#Створення другого вікна (2 вікно)    
def show_transport_window(): 
    global transport_win 
    transport_win = QWidget() 
    transport_win.setWindowTitle('Транспорт') 
    transport_win.resize(530, 530) 
    transport_win.setStyleSheet("background-color: red; font-size: 16px; font-weight: bold;") 
 
    question = QLabel('Виберіть транспортні засоби на яких ви будете подорожувати:') 
    #Додати машини 
    combo_transport1 = QComboBox() 
    combo_transport1.addItem('Nissan') 
    combo_transport1.addItem('Jaguar') 
    combo_transport1.addItem('Volvo') 
    combo_transport1.addItem('Ferrari') 
    combo_transport1.addItem('Porsche') 
    # Додати літаки 
     
    combo_transport2 = QComboBox() 
    combo_transport2.addItem('Мрія') 
    combo_transport2.addItem('Boeing 737') 
    combo_transport2.addItem('Dassault Falcon 2000') 
    combo_transport2.addItem('McDonnell Douglas DC-9') 
    combo_transport2.addItem('Lockheed Martin X-59 QueSST') 
    # Додати поїзда 
     
    combo_transport3 = QComboBox() 
    combo_transport3.addItem('Швидкісний купе ') 
    combo_transport3.addItem('Швидкісний плацкарт') 
    combo_transport3.addItem('Звичайний купе') 
    combo_transport3.addItem('Звичайний плацкарт') 
    # Додати кораблі 
     
    combo_transport4 = QComboBox() 
    combo_transport4.addItem('Club Med 2') 
    combo_transport4.addItem('Wind Surf') 
    combo_transport4.addItem('S/Y A') 
    combo_transport4.addItem('Royal Clipper') 
    # Додайте інші можливості вибору, які потрібні 
     
    btn_choose_items = QPushButton('Вибрати транспорт') 
    btn_styles = "font-size: 16px; font-weight: bold;" 
    question.setStyleSheet(btn_styles)
