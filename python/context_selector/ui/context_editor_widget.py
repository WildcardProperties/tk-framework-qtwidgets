# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'context_editor_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from tank.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from ..qtwidgets import GlobalSearchWidget

from  . import resources_rc

class Ui_ContextWidget(object):
    def setupUi(self, ContextWidget):
        if not ContextWidget.objectName():
            ContextWidget.setObjectName(u"ContextWidget")
        ContextWidget.resize(285, 89)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ContextWidget.sizePolicy().hasHeightForWidth())
        ContextWidget.setSizePolicy(sizePolicy)
        ContextWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(ContextWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(ContextWidget)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label)

        self.edit_widget = QWidget(ContextWidget)
        self.edit_widget.setObjectName(u"edit_widget")
        self.verticalLayout = QVBoxLayout(self.edit_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.task_label = QLabel(self.edit_widget)
        self.task_label.setObjectName(u"task_label")
        self.task_label.setMinimumSize(QSize(0, 0))
        self.task_label.setMaximumSize(QSize(16777215, 32))
        self.task_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.task_label.setOpenExternalLinks(True)
        self.task_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.task_label, 0, 0, 1, 1)

        self.task_widgets_layout = QHBoxLayout()
        self.task_widgets_layout.setSpacing(4)
        self.task_widgets_layout.setObjectName(u"task_widgets_layout")
        self.task_widgets_layout.setContentsMargins(-1, -1, -1, 1)
        self.task_display = QLabel(self.edit_widget)
        self.task_display.setObjectName(u"task_display")
        self.task_display.setMinimumSize(QSize(0, 0))
        self.task_display.setMaximumSize(QSize(16777215, 32))
        self.task_display.setMargin(4)
        self.task_display.setOpenExternalLinks(True)
        self.task_display.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.task_widgets_layout.addWidget(self.task_display)

        self.task_search_layout = QHBoxLayout()
        self.task_search_layout.setSpacing(0)
        self.task_search_layout.setObjectName(u"task_search_layout")
        self.task_search = GlobalSearchWidget(self.edit_widget)
        self.task_search.setObjectName(u"task_search")
        self.task_search.setMinimumSize(QSize(0, 32))
        self.task_search.setMaximumSize(QSize(16777215, 32))

        self.task_search_layout.addWidget(self.task_search)

        self.task_menu_btn = QToolButton(self.edit_widget)
        self.task_menu_btn.setObjectName(u"task_menu_btn")
        self.task_menu_btn.setMinimumSize(QSize(32, 32))
        self.task_menu_btn.setMaximumSize(QSize(32, 32))
        self.task_menu_btn.setFocusPolicy(Qt.NoFocus)
        self.task_menu_btn.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/tk_framework_qtwidgets.context_selector/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_menu_btn.setIcon(icon)
        self.task_menu_btn.setIconSize(QSize(32, 32))
        self.task_menu_btn.setCheckable(False)
        self.task_menu_btn.setPopupMode(QToolButton.InstantPopup)

        self.task_search_layout.addWidget(self.task_menu_btn)

        self.task_search_layout.setStretch(0, 100)
        self.task_search_layout.setStretch(1, 1)

        self.task_widgets_layout.addLayout(self.task_search_layout)

        self.task_search_btn = QToolButton(self.edit_widget)
        self.task_search_btn.setObjectName(u"task_search_btn")
        self.task_search_btn.setMinimumSize(QSize(32, 32))
        self.task_search_btn.setMaximumSize(QSize(32, 32))
        self.task_search_btn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/tk_framework_qtwidgets.context_selector/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task_search_btn.setIcon(icon1)
        self.task_search_btn.setIconSize(QSize(32, 32))
        self.task_search_btn.setCheckable(True)

        self.task_widgets_layout.addWidget(self.task_search_btn)

        self.task_widgets_layout.setStretch(0, 1)
        self.task_widgets_layout.setStretch(1, 100)
        self.task_widgets_layout.setStretch(2, 1)

        self.gridLayout.addLayout(self.task_widgets_layout, 0, 1, 1, 1)

        self.status_label = QtGui.QLabel(self.edit_widget)
        self.status_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.status_label.setOpenExternalLinks(True)
        #self.status_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.status_label.setObjectName("status_label")
        self.gridLayout.addWidget(self.status_label, 1, 0, 1, 1)
        self.status_widgets_layout = QtGui.QHBoxLayout()
        self.status_widgets_layout.setSpacing(4)
        #self.status_widgets_layout.setContentsMargins(-1, 1, -1, -1)
        self.status_widgets_layout.setContentsMargins(-1, 1, -1, 8)
        self.status_widgets_layout.setObjectName("status_widgets_layout")
        self.status_display = QtGui.QComboBox(self.edit_widget)
        self.status_display.setToolTip('Display or change current task status.')
        self.status_display.setMinimumSize(QtCore.QSize(0, 0))
        self.status_display.setMaximumSize(QtCore.QSize(16777215, 32))
        self.status_display.setObjectName("status_display")
        self.status_widgets_layout.addWidget(self.status_display)

        self.status_widgets_layout.setStretch(0, 1)
        self.status_widgets_layout.setStretch(1, 100)
        self.status_widgets_layout.setStretch(2, 1)
        self.gridLayout.addLayout(self.status_widgets_layout, 1, 1, 1, 1)

        self.link_label = QtGui.QLabel(self.edit_widget)
        self.link_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.link_label, 2, 0, 1, 1)

        self.link_widgets_layout = QHBoxLayout()
        self.link_widgets_layout.setSpacing(4)
        self.link_widgets_layout.setObjectName(u"link_widgets_layout")
        self.link_widgets_layout.setContentsMargins(-1, 1, -1, -1)
        self.link_display = QLabel(self.edit_widget)
        self.link_display.setObjectName(u"link_display")
        self.link_display.setMinimumSize(QSize(0, 0))
        self.link_display.setMaximumSize(QSize(16777215, 32))
        self.link_display.setMargin(4)
        self.link_display.setOpenExternalLinks(True)
        self.link_display.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.link_widgets_layout.addWidget(self.link_display)

        self.link_search = GlobalSearchWidget(self.edit_widget)
        self.link_search.setObjectName(u"link_search")
        self.link_search.setMinimumSize(QSize(0, 32))
        self.link_search.setMaximumSize(QSize(16777215, 32))

        self.link_widgets_layout.addWidget(self.link_search)

        self.link_search_btn = QToolButton(self.edit_widget)
        self.link_search_btn.setObjectName(u"link_search_btn")
        self.link_search_btn.setMinimumSize(QSize(32, 32))
        self.link_search_btn.setMaximumSize(QSize(32, 32))
        self.link_search_btn.setFocusPolicy(Qt.NoFocus)
        self.link_search_btn.setIcon(icon1)
        self.link_search_btn.setIconSize(QSize(32, 32))
        self.link_search_btn.setCheckable(True)

        self.link_widgets_layout.addWidget(self.link_search_btn)

        self.link_widgets_layout.setStretch(0, 1)
        self.link_widgets_layout.setStretch(1, 100)
        self.link_widgets_layout.setStretch(2, 1)
        self.gridLayout.addLayout(self.link_widgets_layout, 2, 1, 1, 1)

        self.publish_name_label = QtGui.QLabel(self.edit_widget)
        self.publish_name_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.publish_name_label.setOpenExternalLinks(True)
        self.publish_name_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.publish_name_label.setObjectName("publish_name_label")
        self.gridLayout.addWidget(self.publish_name_label, 3, 0, 1, 1)
        self.publish_name_widgets_layout = QtGui.QHBoxLayout()
        self.publish_name_widgets_layout.setSpacing(4)
        # self.publish_name_widgets_layout.setContentsMargins(-1, 1, -1, -1)
        self.publish_name_widgets_layout.setContentsMargins(-1, 1, -1, 8)
        self.publish_name_widgets_layout.setObjectName("publish_name_widgets_layout")
        self.publish_name_display = QLineEdit(self.edit_widget)
        self.publish_name_display.setCursorPosition(0)
        self.publish_name_display.setToolTip('Display potential publish version name.')
        self.publish_name_display.setPlaceholderText('Potential publish version name')
        # self.publish_name_display.setMinimumSize(QtCore.QSize(0, 0))
        # self.publish_name_display.setMaximumSize(QtCore.QSize(16777215, 32))
        self.publish_name_display.setObjectName("publish_name_display")
        self.publish_name_display.setEnabled(False)
        self.publish_name_widgets_layout.addWidget(self.publish_name_display)

        self.publish_name_label.hide()
        self.publish_name_display.hide()

        self.publish_name_widgets_layout.setStretch(0, 1)
        self.publish_name_widgets_layout.setStretch(1, 100)
        self.publish_name_widgets_layout.setStretch(2, 1)
        self.gridLayout.addLayout(self.publish_name_widgets_layout, 3, 1, 1, 1)

        self.publish_token_label = QtGui.QLabel(self.edit_widget)
        self.publish_token_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.publish_token_label.setOpenExternalLinks(True)
        self.publish_token_label.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.publish_token_label.setObjectName("publish_token_label")
        self.gridLayout.addWidget(self.publish_token_label, 4, 0, 1, 1)
        self.publish_token_widgets_layout = QtGui.QHBoxLayout()
        self.publish_token_widgets_layout.setSpacing(4)
        # self.publish_token_widgets_layout.setContentsMargins(-1, 1, -1, -1)
        self.publish_token_widgets_layout.setContentsMargins(-1, 1, -1, 8)
        self.publish_token_widgets_layout.setObjectName("publish_token_widgets_layout")
        self.publish_token_display = QLineEdit(self.edit_widget)
        self.publish_token_display.setCursorPosition(0)
        self.publish_token_display.setToolTip('Type version token then press enter')
        self.publish_token_display.setPlaceholderText('Type version token then press enter')
        # self.publish_token_display.setMinimumSize(QtCore.QSize(0, 0))
        # self.publish_token_display.setMaximumSize(QtCore.QSize(16777215, 32))
        self.publish_token_display.setObjectName("publish_token_display")
        self.publish_token_display.setEnabled(True)
        self.publish_token_widgets_layout.addWidget(self.publish_token_display)

        self.publish_token_label.hide()
        self.publish_token_display.hide()

        self.publish_token_widgets_layout.setStretch(0, 1)
        self.publish_token_widgets_layout.setStretch(1, 100)
        self.publish_token_widgets_layout.setStretch(2, 1)
        self.gridLayout.addLayout(self.publish_token_widgets_layout, 4, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 100)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout_2.addWidget(self.edit_widget)

        self.retranslateUi(ContextWidget)

        QMetaObject.connectSlotsByName(ContextWidget)
    # setupUi

    def retranslateUi(self, ContextWidget):
        ContextWidget.setWindowTitle(QtGui.QApplication.translate("ContextWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ContextWidget", "Task and Entity Link to apply to the selected item:", None, QtGui.QApplication.UnicodeUTF8))
        self.task_label.setText(QtGui.QApplication.translate("ContextWidget", "Task: ", None, QtGui.QApplication.UnicodeUTF8))
        self.task_display.setText(QtGui.QApplication.translate("ContextWidget", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.task_search_btn.setToolTip(QtGui.QApplication.translate("ContextWidget", "<html><head/><body><p>Toggle this button to allow searching for a Task to associate with the selected item.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.task_search_btn.setText(QtGui.QApplication.translate("ContextWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.status_label.setText(QtGui.QApplication.translate("ContextWidget", "Task status: ", None, QtGui.QApplication.UnicodeUTF8))
        #self.status_display.setText(QtGui.QApplication.translate("ContextWidget", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_label.setText(QtGui.QApplication.translate("ContextWidget", "Link: ", None, QtGui.QApplication.UnicodeUTF8))
        self.link_display.setText(QtGui.QApplication.translate("ContextWidget", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_search_btn.setToolTip(QtGui.QApplication.translate("ContextWidget", "<html><head/><body><p>Toggle this button to allow searching for an entity to link to the selected item.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.link_search_btn.setText(QtGui.QApplication.translate("ContextWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_name_label.setText(QtGui.QApplication.translate("ContextWidget", "Version name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_token_label.setText(QtGui.QApplication.translate("ContextWidget", "Version token: ", None, QtGui.QApplication.UnicodeUTF8))

from ..qtwidgets import GlobalSearchWidget
from . import resources_rc
