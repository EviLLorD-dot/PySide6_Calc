# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_w_calc(object):
    def setupUi(self, w_calc):
        if not w_calc.objectName():
            w_calc.setObjectName(u"w_calc")
        w_calc.setWindowModality(Qt.NonModal)
        w_calc.resize(300, 400)
        w_calc.setMinimumSize(QSize(300, 400))
        w_calc.setMaximumSize(QSize(300, 400))
        self.l_display = QLabel(w_calc)
        self.l_display.setObjectName(u"l_display")
        self.l_display.setGeometry(QRect(26, 12, 251, 41))
        font = QFont()
        font.setPointSize(16)
        self.l_display.setFont(font)
        self.l_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.widget = QWidget(w_calc)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 261, 326))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_squar = QPushButton(self.widget)
        self.btn_squar.setObjectName(u"btn_squar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_squar.sizePolicy().hasHeightForWidth())
        self.btn_squar.setSizePolicy(sizePolicy)
        self.btn_squar.setMinimumSize(QSize(60, 60))
        self.btn_squar.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setPointSize(36)
        self.btn_squar.setFont(font1)
        icon = QIcon()
        icon.addFile(u"icons/icons8-square-number-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_squar.setIcon(icon)
        self.btn_squar.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_squar, 0, 0, 1, 1)

        self.btn_sqrt = QPushButton(self.widget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        sizePolicy.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy)
        self.btn_sqrt.setMinimumSize(QSize(60, 60))
        self.btn_sqrt.setMaximumSize(QSize(60, 60))
        self.btn_sqrt.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-square-root-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sqrt.setIcon(icon1)
        self.btn_sqrt.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_sqrt, 0, 1, 1, 1)

        self.btn_rmlst = QPushButton(self.widget)
        self.btn_rmlst.setObjectName(u"btn_rmlst")
        sizePolicy.setHeightForWidth(self.btn_rmlst.sizePolicy().hasHeightForWidth())
        self.btn_rmlst.setSizePolicy(sizePolicy)
        self.btn_rmlst.setMinimumSize(QSize(60, 60))
        self.btn_rmlst.setMaximumSize(QSize(60, 60))
        self.btn_rmlst.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"icons/icons8-clear-symbol-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rmlst.setIcon(icon2)
        self.btn_rmlst.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_rmlst, 0, 2, 1, 1)

        self.btn_clear = QPushButton(self.widget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QSize(60, 60))
        self.btn_clear.setMaximumSize(QSize(60, 60))
        self.btn_clear.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icons/icons8-broom-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon3)
        self.btn_clear.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_clear, 0, 3, 1, 1)

        self.btn_7 = QPushButton(self.widget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QSize(60, 60))
        self.btn_7.setMaximumSize(QSize(60, 60))
        self.btn_7.setFont(font1)

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(self.widget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QSize(60, 60))
        self.btn_8.setMaximumSize(QSize(60, 60))
        self.btn_8.setFont(font1)

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.widget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QSize(60, 60))
        self.btn_9.setMaximumSize(QSize(60, 60))
        self.btn_9.setFont(font1)

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_mul = QPushButton(self.widget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        self.btn_mul.setMinimumSize(QSize(60, 60))
        self.btn_mul.setMaximumSize(QSize(60, 60))
        self.btn_mul.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"icons/icons8-multiply-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mul.setIcon(icon4)
        self.btn_mul.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_4 = QPushButton(self.widget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QSize(60, 60))
        self.btn_4.setMaximumSize(QSize(60, 60))
        self.btn_4.setFont(font1)

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.widget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QSize(60, 60))
        self.btn_5.setMaximumSize(QSize(60, 60))
        self.btn_5.setFont(font1)

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.widget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QSize(60, 60))
        self.btn_6.setMaximumSize(QSize(60, 60))
        self.btn_6.setFont(font1)

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_div = QPushButton(self.widget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setMinimumSize(QSize(60, 60))
        self.btn_div.setMaximumSize(QSize(60, 60))
        self.btn_div.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u"icons/icons8-divide-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_div.setIcon(icon5)
        self.btn_div.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_div, 2, 3, 1, 1)

        self.btn_1 = QPushButton(self.widget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QSize(60, 60))
        self.btn_1.setMaximumSize(QSize(60, 60))
        self.btn_1.setFont(font1)

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(self.widget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QSize(60, 60))
        self.btn_2.setMaximumSize(QSize(60, 60))
        self.btn_2.setFont(font1)

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(self.widget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMaximumSize(QSize(60, 60))
        self.btn_3.setFont(font1)

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_sub = QPushButton(self.widget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        self.btn_sub.setMinimumSize(QSize(60, 60))
        self.btn_sub.setMaximumSize(QSize(60, 60))
        self.btn_sub.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"icons/icons8-subtract-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sub.setIcon(icon6)
        self.btn_sub.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_sub, 3, 3, 1, 1)

        self.btn_dot = QPushButton(self.widget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setMinimumSize(QSize(60, 60))
        self.btn_dot.setMaximumSize(QSize(60, 60))
        self.btn_dot.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u"icons/icons8-new-moon-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dot.setIcon(icon7)

        self.gridLayout.addWidget(self.btn_dot, 4, 0, 1, 1)

        self.btn_0 = QPushButton(self.widget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setMinimumSize(QSize(60, 60))
        self.btn_0.setMaximumSize(QSize(60, 60))
        self.btn_0.setFont(font1)

        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_equ = QPushButton(self.widget)
        self.btn_equ.setObjectName(u"btn_equ")
        sizePolicy.setHeightForWidth(self.btn_equ.sizePolicy().hasHeightForWidth())
        self.btn_equ.setSizePolicy(sizePolicy)
        self.btn_equ.setMinimumSize(QSize(60, 60))
        self.btn_equ.setMaximumSize(QSize(60, 60))
        self.btn_equ.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u"icons/icons8-equal-sign-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_equ.setIcon(icon8)
        self.btn_equ.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_equ, 4, 2, 1, 1)

        self.btn_add = QPushButton(self.widget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QSize(60, 60))
        self.btn_add.setMaximumSize(QSize(60, 60))
        self.btn_add.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u"icons/icons8-plus-math-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon9)
        self.btn_add.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btn_add, 4, 3, 1, 1)


        self.retranslateUi(w_calc)

        QMetaObject.connectSlotsByName(w_calc)
    # setupUi

    def retranslateUi(self, w_calc):
        w_calc.setWindowTitle(QCoreApplication.translate("w_calc", u"Calculator", None))
        self.l_display.setText(QCoreApplication.translate("w_calc", u"0", None))
        self.btn_squar.setText("")
        self.btn_sqrt.setText("")
        self.btn_rmlst.setText("")
        self.btn_clear.setText("")
        self.btn_7.setText(QCoreApplication.translate("w_calc", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("w_calc", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("w_calc", u"9", None))
        self.btn_mul.setText("")
        self.btn_4.setText(QCoreApplication.translate("w_calc", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("w_calc", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("w_calc", u"6", None))
        self.btn_div.setText("")
        self.btn_1.setText(QCoreApplication.translate("w_calc", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("w_calc", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("w_calc", u"3", None))
        self.btn_sub.setText("")
        self.btn_dot.setText("")
        self.btn_0.setText(QCoreApplication.translate("w_calc", u"0", None))
        self.btn_equ.setText("")
        self.btn_add.setText("")
    # retranslateUi

