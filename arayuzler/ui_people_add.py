# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'people_add.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PeopleAdd(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 380)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(340, 10, 67, 17))
        self.label_4.setObjectName("label_4")
        self.lbResim = QtWidgets.QLabel(Form)
        self.lbResim.setGeometry(QtCore.QRect(310, 30, 161, 191))
        self.lbResim.setText("")
        self.lbResim.setPixmap(QtGui.QPixmap("../../../Masaüstü/nobody.png"))
        self.lbResim.setScaledContents(True)
        self.lbResim.setObjectName("lbResim")
        self.btnDegistir = QtWidgets.QPushButton(Form)
        self.btnDegistir.setGeometry(QtCore.QRect(308, 230, 161, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnDegistir.setFont(font)
        self.btnDegistir.setObjectName("btnDegistir")
        self.btnCek = QtWidgets.QPushButton(Form)
        self.btnCek.setGeometry(QtCore.QRect(310, 260, 161, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCek.setFont(font)
        self.btnCek.setObjectName("btnCek")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 101, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 10, 161, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbOkulNo = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lbOkulNo.setObjectName("lbOkulNo")
        self.verticalLayout_2.addWidget(self.lbOkulNo)
        self.lbAdSoyad = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lbAdSoyad.setObjectName("lbAdSoyad")
        self.verticalLayout_2.addWidget(self.lbAdSoyad)
        self.lbSinif = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lbSinif.setObjectName("lbSinif")
        self.verticalLayout_2.addWidget(self.lbSinif)
        self.btnKaydet = QtWidgets.QPushButton(Form)
        self.btnKaydet.setGeometry(QtCore.QRect(20, 170, 271, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnKaydet.setFont(font)
        self.btnKaydet.setObjectName("btnKaydet")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kişi Ekle"))
        self.label_4.setText(_translate("Form", "Resim:"))
        self.btnDegistir.setText(_translate("Form", "Kamerayı Başlat"))
        self.btnCek.setText(_translate("Form", "Çek"))
        self.label_2.setText(_translate("Form", "Okul No:"))
        self.label.setText(_translate("Form", "Ad Soyad:"))
        self.label_3.setText(_translate("Form", "Sınıf:"))
        self.btnKaydet.setText(_translate("Form", "Kaydet"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_PeopleAdd()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())