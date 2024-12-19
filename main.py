from PyQt5 import QtWidgets
from add import Ui_MainWindow as AddSupplierWindow
from additem import Ui_MainWindow as AddItemWindow

class AddSupplierApp(QtWidgets.QMainWindow, AddSupplierWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_supplier)

    def add_supplier(self):
        supplier_name = self.plainTextEdit.toPlainText()
        supplier_address = self.plainTextEdit_2.toPlainText()
        supplier_id = self.plainTextEdit_3.toPlainText()

        # Example action: Print to console (replace with DB insert or file write)
        print(f"Supplier Added: Name={supplier_name}, Address={supplier_address}, ID={supplier_id}")
        QtWidgets.QMessageBox.information(self, "Success", "Supplier added successfully!")


class AddItemApp(QtWidgets.QMainWindow, AddItemWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_new_supplier)
        self.pushButton_2.clicked.connect(self.add_item)
        self.pushButton_3.clicked.connect(self.done)

    def add_new_supplier(self):
        self.supplier_window = AddSupplierApp()
        self.supplier_window.show()

    def add_item(self):
        item_number = self.plainTextEdit_2.toPlainText()
        price = self.plainTextEdit_4.toPlainText()
        quantity = self.plainTextEdit_5.toPlainText()
        unit = self.plainTextEdit_6.toPlainText()

        # Example action: Print to console (replace with DB insert or file write)
        print(f"Item Added: Number={item_number}, Price={price}, Quantity={quantity}, Unit={unit}")
        QtWidgets.QMessageBox.information(self, "Success", "Item added successfully!")

    def done(self):
        QtWidgets.QMessageBox.information(self, "Done", "All actions completed.")
        self.close()


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = AddItemApp()
        self.main_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
