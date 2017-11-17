import os
import datetime
import sqlite3
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from course import Ui_MainWindow
from ListView import Ui_Form

class Course(QMainWindow):

    def createTable():
          baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
          isretci = baglanti.cursor()
          isretci.execute(
              '''CREATE TABLE ogrenci
                    ( 'id' integer primary key AUTOINCREMENT,
                    'adsoyad' varchar(40) DEFAULT NULL,
                    'adres' varchar(250) DEFAULT NULL,
                    'telefon' varchar(12) DEFAULT NULL,
                    'meslek' varchar(25) DEFAULT NULL,
                    'ucret' varchar(10) DEFAULT NULL,
                    'email' varchar(40) DEFAULT NULL,
                    'kayit_tarihi' date DEFAULT NULL,
                    'bitis_tarihi' date DEFAULT NULL,
                    'ders_gunleri' varchar(25) DEFAULT NULL,
                    'aylik_takip' date DEFAULT NULL,
                    'kac_saat' varchar(2) DEFAULT NULL,
                    'baslangic_saat' varchar(12) DEFAULT NULL,
                    'bitis_saat' varchar(12) DEFAULT NULL,
                    'aktif' varchar(12) DEFAULT NULL )  ''')
          baglanti.commit()
          baglanti.close()



    def __init__(self, ebeveyn=None):
        QWidget.__init__(self, ebeveyn)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.pushKaydet,SIGNAL("clicked()"), self.kaydet)
        self.connect(self.ui.pushButton,SIGNAL("clicked()"),self.ara)
        self.ui.pushButton_2.setEnabled(False)
        self.connect(self.ui.pushButton_2,SIGNAL("clicked()"),self.guncelle)
        self.errorMessageDialog = QErrorMessage(self)
        self.connect(self.ui.pushButton_3,SIGNAL("clicked()"),self.listele)
        #self.connect(self.ui.actionYedek_Al,SIGNAL("clicked()"),self.yedekAl)
        #self.saveAsMenu.aboutToShow.connect(self.aboutToShowSaveAsMenu)


    def yedekAl(self):
        print("yedekAl")
        #dosya = open("/dosyayı/oluşturmak/istediğimiz/dizin/dosya_adı", "w")
        global completed
        completed = 0
        #goster = GostergeYukle()
        #self.ui.goster.show()
        self.progress = QProgressBar()
        self.progress.show()
        try:
            f = open('c:/Course/yedek.txt', 'w')
            baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
            isretci = baglanti.cursor()
            print("yedekAl step2")
            db =isretci.execute("select id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif from ogrenci")
            #print(db.fetchall())
            data = db.fetchall()
            #if len(data)>0:
            print("yedekAl step3")
            for i in data:
                if completed < 100:
                   completed += 1
                   self.progress.setValue(completed)
                print(i)
                global ogrenciId
                ogrenciId = i[0]
                insertScript = "insert into ogrenci (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) values ("
                parametre = insertScript+str(ogrenciId),i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14]
                f.write(str(parametre))
                f.write("\n")
            if completed < 100:
                while completed < 100:
                    completed +=1
                    self.progress.setValue(completed)

        except IOError:
            print("yedek al da bir hata oluştu!")
        finally:
            f.close()

    def yaziciyaGonder(self):
        print("yaziciyaGonder")
        print(self.ui.adsoyad.text())
        print(self.ui.timeBaslangic.text())
        print(self.ui.timeBitis.text())
        self.logo = None
        pdffile = 'test.pdf'
        self.histogram = None
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.Letter)
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdffile)
        document = QTextDocument()
        days = ""
        if self.ui.checkBox.isChecked():
                    days = "Pazartesi"
        if self.ui.checkBox_2.isChecked():
                    days += " Salı"
        if self.ui.checkBox_3.isChecked():
                    days += " Çarşamba"
        if self.ui.checkBox_4.isChecked():
                    days += " Perşembe"
        if self.ui.checkBox_5.isChecked():
                    days += " Cuma"
        if self.ui.checkBox_6.isChecked():
                    days += " Cumartesi"
        if self.ui.checkBox_7.isChecked():
                    days += " Pazar"
        html = ""
        html += ('<head><title>Report</title><style></style></head>'
                 '<body><table width="100%"><tr>'
                    '<td></td>'
                    '<td><h1>Excelent English Course</h1></td>'
                 '<td></td>'
                 '<td></td>'
                    '<tr><td>Ad Soyad</td><td>Kayıt Tarihi</td><td>Başlangıç Tarihi</td><td>Ücret</td><td>Ders Günleri</td><td>Eğitim Saati</td><td>Başlangıç Saati</td><td>Bitiş Saati</td></tr>'
                 '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td></tr>'
                 '</table>'

                 '</body>').format(self.ui.adsoyad.text(), self.ui.kayitTarihi.text(),"",self.ui.ucret.text(),str(days),self.ui.kacsaat.text(),self.ui.timeBaslangic.text(),self.ui.timeBitis.text())
        document.setHtml(html)

        printer = QPrinter()
        printer.setResolution(96)
        printer.setPageSize(QPrinter.Letter)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("test.pdf")
        printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
        document.setPageSize(QSizeF(printer.pageRect().size()))
        print(document.pageSize(), printer.resolution(), printer.pageRect())
        document.print_(printer)
        #document = self.ui.adsoyad.text()
        #printer = QPrinter()

        #dlg = QPrintDialog(printer, self)
        #if dlg.exec_() != QDialog.Accepted:
        #    return
        #document.print_(printer)
    def mailGonder(self):
        print("mailGonder")
        global mail_gonder
        try:
            f = open('c:/Course/ayarlar.txt', 'r')
            f.seek(24)
            print (f.read())
            mail_gonder = f.read()
            Message(self,'''Mail gönderme modülü aktif değil!..''')
        except IOError:
            print("ayarlar.txt okurken bir hata oluştu!")
        finally:
            f.close()
    def kullanimBilgisi(self):
        print("kullanimBilgisi")
    def veritabaniSifirla(self):
        print("veritabaniSifirla")
        baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
        isretci = baglanti.cursor()
        isretci.execute('''DELETE FROM ogrenci''')
        baglanti.commit()
        baglanti.close()


    def listele(self):
        print("listele")
        w = PrettyWidget()
        self.ui.w.show()
        #self.ui = uic.loadUi('ListView.ui',self)
        #self.ListView = QMainWindow()
        #self.ui.ListView = ListView()
        #self.setupUi(self.ListView)
        #self.ui.ListView.show()

    def ara(self):
        print("ara")
        self.ui.pushButton_2.setEnabled(True)
        baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
        isretci = baglanti.cursor()
        if self.ui.telefon.text() == '':
            db =isretci.execute("select id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif from ogrenci where adsoyad = (?) ",[(self.ui.adsoyad.text())])
        elif self.ui.adsoyad.text() == '':
            db =isretci.execute("select id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif from ogrenci where telefon = (?) ",[(self.ui.telefon.text())])
        ekraniTemizle(self)
        #print(db.fetchall())
        data = db.fetchall()
        if len(data)>0:
         for i in data:
            print(i)
            global ogrenciId
            ogrenciId = i[0]
            self.ui.adsoyad.setText(i[1])
            self.ui.adres.setText(i[2])
            self.ui.telefon.setText(i[3])
            self.ui.ucret.setText(i[5])
            meslek = str(i[4])
            if meslek is None:
               self.ui.meslek.setText("")
            self.ui.meslek.setText(meslek)
            self.ui.email.setText(i[6])
            days = i[9].split(",")
            for dy in days:
                print(dy)
                if dy == "1":
                    self.ui.checkBox.setChecked(True)
                if dy == "2":
                    self.ui.checkBox_2.setChecked(True)
                if dy == "3":
                    self.ui.checkBox_3.setChecked(True)
                if dy == "4":
                    self.ui.checkBox_4.setChecked(True)
                if dy == "5":
                    self.ui.checkBox_5.setChecked(True)
                if dy == "6":
                    self.ui.checkBox_6.setChecked(True)
                if dy == "7":
                    self.ui.checkBox_7.setChecked(True)
            listDay = convertDate(i[7])
            self.ui.kayitTarihi.setDate(QDate(int(listDay[2]),int(listDay[1]),int(listDay[0])))
            listDay = convertDate(i[8])
            self.ui.bitisTarihi.setDate(QDate(int(listDay[2]),int(listDay[1]),int(listDay[0])))
            if i[14] == "1":
                self.ui.radioAktif.setChecked(True)
            else:
                self.ui.radioAktif.setChecked(False)
            self.ui.kacsaat.setValue(int(i[11]))

            listTime = convertTime(i[12])
            self.ui.timeBaslangic.setTime(QTime(int(listTime[0]),int(listTime[1]) , int(listTime[2])))
            listTime = convertTime(i[13])
            self.ui.timeBitis.setTime(QTime(int(listTime[0]),int(listTime[1]) , int(listTime[2])))
        else:
             print("kayıt bulunamadı...")
             ekraniTemizle(self)
             errorMessage(self)
             self.ui.pushButton_2.setEnabled(False)
        baglanti.commit()
        baglanti.close()

    global db_sifirla
    db_sifirla = "1"
    try:
            f = open('c:/Course/ayarlar.txt', 'r')
            f.seek(13)
            print (f.read())
            db_sifirla = f.read()
    except IOError:
            print("ayarlar.txt okurken bir hata oluştu!")
    finally:
            f.close()
    if db_sifirla == "1":
        print("db_sıfırla")
        #createTable()
    else:
        print("db_sifirla = 0")



    def kaydet(self):
        print("kaydet")
        days = []
        global gun,timeBaslangic,timeBitis
        gun = ""
        print (self.ui.adsoyad.text())
        print (self.ui.adres.toPlainText())
        print (self.ui.telefon.text())
        print (self.ui.meslek.text())
        print (self.ui.ucret.text())
        print (self.ui.kayitTarihi.text())
        print (self.ui.email.text())
        print (self.ui.aylikDersTakibi.selectedDate())
        print(datetime.date.today())
        print (self.ui.kacsaat.text())
        print (self.ui.timeBaslangic.text())
        print (self.ui.timeBitis.text())
        if self.ui.checkBox.isChecked():
                    days.append("1")
        if self.ui.checkBox_2.isChecked():
                    days.append("2")
        if self.ui.checkBox_3.isChecked():
                    days.append("3")
        if self.ui.checkBox_4.isChecked():
                    days.append("4")
        if self.ui.checkBox_5.isChecked():
                    days.append("5")
        if self.ui.checkBox_6.isChecked():
                    days.append("6")
        if self.ui.checkBox_7.isChecked():
                    days.append("7")
        if self.ui.radioAktif.isChecked():
                    aktif = "1"
        else:
            aktif = "0"
        for day in days:
          #print (day)
          gun += day
          gun += ","
          print(gun)
        timeBaslangic = self.ui.timeBaslangic.text()
        timeBitis     = self.ui.timeBitis.text()
#datetime.date.today()


        kontrol_et(self,gun,timeBaslangic,timeBitis)
        if sameDay == False:
            print( aktif )
            date = self.ui.aylikDersTakibi.selectedDate()
            baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
            isretci = baglanti.cursor()
            isretci.execute('''INSERT INTO ogrenci(adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif)
                              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                            (self.ui.adsoyad.text(),
                            self.ui.adres.toPlainText(),
                            self.ui.telefon.text(),
                            self.ui.meslek.text(),
                            self.ui.ucret.text(),
                            self.ui.email.text(),
                            self.ui.kayitTarihi.text(),
                            self.ui.bitisTarihi.text(),
                            gun,
                            str(date.toPyDate()),
                            self.ui.kacsaat.text(),
                            self.ui.timeBaslangic.text(),
                            self.ui.timeBitis.text(),
                            aktif))

            baglanti.commit()
            baglanti.close()
            self.ui.adres.setText("")
            self.ui.telefon.setText("")
            self.ui.meslek.setText("")
            self.ui.ucret.setText("")
            self.ui.adsoyad.setText("")
            self.ui.email.setText("")




    def guncelle(self):
        print("guncelle")
        print(ogrenciId)
        days = []
        gun = ""
        date = self.ui.aylikDersTakibi.selectedDate()
        if self.ui.checkBox.isChecked():
                    days.append("1")
        if self.ui.checkBox_2.isChecked():
                    days.append("2")
        if self.ui.checkBox_3.isChecked():
                    days.append("3")
        if self.ui.checkBox_4.isChecked():
                    days.append("4")
        if self.ui.checkBox_5.isChecked():
                    days.append("5")
        if self.ui.checkBox_6.isChecked():
                    days.append("6")
        if self.ui.checkBox_7.isChecked():
                    days.append("7")
        if self.ui.radioAktif.isChecked():
                    aktif = "1"
        else:
            aktif = "0"
        for day in days:
          #print (day)
          gun += day
          gun += ","
        baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
        isretci = baglanti.cursor()
        isretci.execute('''UPDATE ogrenci set adsoyad=?,adres=?,telefon=?,meslek=?,ucret=?,email=?,kayit_tarihi=?,bitis_tarihi=?,
                                              ders_gunleri=?,aylik_takip=?,kac_saat=?,baslangic_saat=?,bitis_saat=?,aktif=?
                         WHERE id = ?''',(self.ui.adsoyad.text(),
                                self.ui.adres.toPlainText(),
                                self.ui.telefon.text(),
                                self.ui.meslek.text(),
                                self.ui.ucret.text(),
                                self.ui.email.text(),
                                self.ui.kayitTarihi.text(),
                                self.ui.bitisTarihi.text(),
                                gun,
                                str(date.toPyDate()),
                                self.ui.kacsaat.text(),
                                self.ui.timeBaslangic.text(),
                                self.ui.timeBitis.text(),
                                aktif,
                                int(ogrenciId)))

        #isretci.execute(sql)
        baglanti.commit()
        baglanti.close()


def kontrol_et(self,day,timeBaslangic,timeBitis):
        print("kontrol et")
        print(day)
        print(timeBaslangic)
        print(timeBitis)
        global sameDay
        sameDay = False
        baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
        isretci = baglanti.cursor()
        db =isretci.execute("""select * from ogrenci where baslangic_saat = (?)  and bitis_saat = (?) and ders_gunleri = (?) and aktif = 1 """,(self.ui.timeBaslangic.text(),self.ui.timeBitis.text(),day))
        pday = day.split(",")
        print("pday")
        print(pday)
        data = db.fetchall()
        if len(data)>0:
         for i in data:
            print(i)
            global ogrenciId
            ogrenciId = i[0]
            adsoyad = i[1]
            telefon = i[3]
            checkDay = ""
            days = i[9].split(",")
            for dy in days:

                for d in pday:
                    if d != '' or dy != '' :
                        if  d == dy:
                            print(dy)
                            print(d)
                            print(sameDay)
                            sameDay = True
                            print(sameDay)



        else:
             print("kayıt kontrol bulunamadı...")


        if sameDay == True:
           a = QMessageBox()
           a.setWindowTitle("Mesaj Ekranı")
           a.setText("seçilen saatler arası kayıt mevcut öğrenci :"+ adsoyad  +" Bilgileri kontrol ediniz!")
           a.setIcon(a.Warning)
           a.exec_()
           self.ui.pushButton_2.setEnabled(False)
        baglanti.commit()
        baglanti.close()



def convertDate(day):
    days = day.split(".")
    print(days[0])
    print(days[1])
    print(days[2])
    newDay  = days[2]
    newDay += "."
    newDay += days[1]
    newDay += "."
    newDay += days[0]
    print(newDay)
    return days

def convertTime(times):
    times = times.split(":")
    return times


def ekraniTemizle(self):
    self.ui.adres.setText("")
    self.ui.telefon.setText("")
    self.ui.meslek.setText("")
    self.ui.ucret.setText("")
    self.ui.adsoyad.setText("")
    self.ui.email.setText("")
    self.ui.adres.setText("")
    self.ui.checkBox.setChecked(False)
    self.ui.checkBox_2.setChecked(False)
    self.ui.checkBox_3.setChecked(False)
    self.ui.checkBox_4.setChecked(False)
    self.ui.checkBox_5.setChecked(False)
    self.ui.checkBox_6.setChecked(False)
    self.ui.checkBox_7.setChecked(False)

def errorMessage(self):
    a = QMessageBox()
    a.setWindowTitle("Mesaj Ekranı")
    a.setText("Aradığınız kayıt bulunamadı Bilgileri kontrol ediniz!")
    a.setIcon(a.Warning)
    a.exec_()
        #self.errorMessageDialog.showMessage("Kayıt Bulunamadı...")
        #self.errorLabel.setText("If the box is unchecked, the message won't "
        #        "appear again.")

def Message(self,parameter):
    a = QMessageBox()
    a.setWindowTitle("Mesaj Ekranı")
    a.setText(parameter)
    a.setIcon(a.Warning)
    a.exec_()

class GostergeYukle(QWidget):
    def __init__(self):
        super(GostergeYukle,self).__init__()
        self.initUI()

    def initUI(self):
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 20, 20)
        self.progress.setValue(completed)
        self.show()

class PrettyWidget(QWidget):
    global table
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(250, 200, 1024, 640)
        self.setWindowTitle('Customer List View')

        #Grid Layout
        grid = QGridLayout()
        #grid.setGeometry(QRect(10, 10, 1024, 20))
        self.setLayout(grid)

        #Data
        dataHeaders = ['Id','Ad Soyad','Telefon','Meslek','Ücret','E-mail','Kayıt Tarihi','Bitiş Tarihi','Ders Günler','Kaç Saat','Başlangıç Saati','Bitiş Saati','Aktif']

        #Create Empty 5x5 Table

        self.table = QTableWidget(self)
        #table.setRowCount(5)
        self.table.setColumnCount(13)
        self.table.setAutoFillBackground(True)

        #Enter data onto Table
        horHeaders = []
        for n in dataHeaders:
            horHeaders.append(n)
        #    for m, item in enumerate(data[key]):
        #    newitem = QTableWidgetItem("denee")
        #    table.setItem(newitem)



        baglanti = sqlite3.connect('C:/Course/ogrenciler.db')
        isretci = baglanti.cursor()
        db =isretci.execute("select id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif from ogrenci")
        #print(db.fetchall())
        data = db.fetchall()
        row  = 0
        if len(data)>0:
         for i in data:
            print(i)
            self.table.insertRow(row)

            global ogrenciId
            ogrenciId = i[0]
            item1 = QTableWidgetItem(str(ogrenciId))
            #if row % 2 == 0:
                #item1.setBackground(QColor(125,125,125))
            self.table.setItem(row,0,item1)
            adSoyad = i[1]
            self.table.setItem(row,1,QTableWidgetItem(adSoyad))
            telefon = str(i[3])
            self.table.setItem(row,2,QTableWidgetItem(telefon))
            meslek = i[5]
            self.table.setItem(row,4,QTableWidgetItem(meslek))
            ucret = i[6]
            self.table.setItem(row,5,QTableWidgetItem(ucret))
            email = i[7]
            self.table.setItem(row,6,QTableWidgetItem(email))
            kayit_tarihi = i[8]
            self.table.setItem(row,7,QTableWidgetItem(kayit_tarihi))
            bitis_tarihi = i[9]
            self.table.setItem(row,8,QTableWidgetItem(bitis_tarihi))
            days = i[9].split(",")
            global dersGunleri
            dersGunleri =""
            for dy in days:
                print(dy)
                if dy == "1":
                    dersGunleri += "Pazartesi"
                if dy == "2":
                    dersGunleri += ",Salı"
                if dy == "3":
                    dersGunleri += ",Çarşamba"
                if dy == "4":
                    dersGunleri += ",Perşembe"
                if dy == "5":
                    dersGunleri += ",Cuma"
                if dy == "6":
                    dersGunleri += ",Cumartesi"
                if dy == "7":
                    dersGunleri += ",Pazar"
            self.table.setItem(row,8,QTableWidgetItem(dersGunleri))
            #listDay = str(i[10])
            #table.setItem(row,10,QTableWidgetItem(listDay))
            #self.ui.kayitTarihi.setDate(QDate(int(listDay[2]),int(listDay[1]),int(listDay[0])))
            #listDays = str(i[8])
            #table.setItem(row,11,QTableWidgetItem(listDays))
            #self.ui.bitisTarihi.setDate(QDate(int(listDay[2]),int(listDay[1]),int(listDay[0])))
            kacsaat = i[11]
            self.table.setItem(row,9,QTableWidgetItem(kacsaat))
            listTime = str(i[12])
            self.table.setItem(row,10,QTableWidgetItem(listTime))
            #self.ui.timeBaslangic.setTime(QTime(int(listTime[0]),int(listTime[1]) , int(listTime[2])))
            listTime = str(i[13])
            self.table.setItem(row,11,QTableWidgetItem(listTime))
            #self.ui.timeBitis.setTime(QTime(int(listTime[0]),int(listTime[1]) , int(listTime[2])))
            if i[13] == "1":
                #self.ui.radioAktif.setChecked(True)
                self.table.setItem(row,12,QTableWidgetItem(str("Aktif")))
            else:
                #self.ui.radioAktif.setChecked(False)
                self.table.setItem(row,12,QTableWidgetItem(str("Pasif")))
            row = row + 1
        else:
             print("kayıt bulunamadı...")

        baglanti.commit()
        baglanti.close()

        #Add Header
        self.table.setHorizontalHeaderLabels(horHeaders)

        #Adjust size of Table
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()


        #Add Table to Grid

        self.menuBar = QMenuBar(self)
        self.menuBar.setGeometry(QRect(0, 0, 1024, 19))
        self.fileMenu = QMenu("&Menü", self)
        self.printAction = self.fileMenu.addAction("Yazdır")
        self.menuBar.addMenu(self.fileMenu)
        self.printAction.triggered.connect(self.tableWrite)

        grid.addWidget(self.table, 0,0)
        print(self.table.rowCount())
        self.show()
    def tableWrite(self):
        print("tableWrite")
        document = QTextDocument()
        row = 0
        allRows = self.table.rowCount()
        dataList = []
        print(allRows)
        html = ""
        html += "<head><title>All Customer List</title><style></style></head>"\
                +"<body><table width="+'100%'+"><tr>"\
                +"<td></td>"\
                +"<td><h1>Excelent English Course</h1></td>"\
                +"<td></td>"\
                +"<td></td>"\
                +"<tr><td>Ad Soyad</td><td>Kayıt Tarihi</td><td>Başlangıç Tarihi</td><td>Ücret</td><td>Ders Günleri</td><td>Eğitim Saati</td><td>Başlangıç Saati</td><td>Bitiş Saati</td></tr>"



        while row < allRows:		
            html += "<tr><td>" + self.table.item(row, 0).text() + "</td>"
            html += "<td>" + self.table.item(row, 1).text() + "</td>"
            html += "<td>" + self.table.item(row, 2).text() + "</td>"
            #html += "<td>" + self.table.item(row, 3) + "</td>"
            html += "<td>" + self.table.item(row, 4).text() + "</td>"
            html += "<td>" + self.table.item(row, 5).text() + "</td>"
            html += "<td>" + self.table.item(row, 6).text() + "</td>"
            html += "<td>" + self.table.item(row, 7).text() + "</td>"
            html += "<td>" + self.table.item(row, 8).text() + "</td>"
            html += "<td>" + self.table.item(row, 9).text() + "</td>"
            html += "<td>" + self.table.item(row, 10).text() + "</td>"
            html += "<td>" + self.table.item(row, 11).text() + "</td>"
            html += "<td>" + self.table.item(row, 12).text() + "</td>"
            #html += "<td>" + self.table.item(row, 13) + "</td>
            html +="</tr>"
            row += 1


        html += "</table>' '</body>"
        print(html)
        document.setHtml(html)
        printer = QPrinter()
        printer.setResolution(96)
        printer.setPageSize(QPrinter.Letter)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("AllListCustomer.pdf")
        printer.setPageMargins(12, 16, 12, 20, QPrinter.Millimeter)
        document.setPageSize(QSizeF(printer.pageRect().size()))
        print(document.pageSize(), printer.resolution(), printer.pageRect())
        document.print_(printer)


uyg = QApplication([])
pencere = Course()
pencere.show()
uyg.exec_()
