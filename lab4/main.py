from PyQt5 import QtWidgets, QtGui
import os
from itertools import cycle

class DatasetApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.tiger_cycle = None
        self.leopard_cycle = None
        self.current_instance_path = None
        self.tiger_paths = []
        self.leopard_paths = []

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.image_label = QtWidgets.QLabel(self)
        layout.addWidget(self.image_label)

        next_tiger_button = QtWidgets.QPushButton('Следующий тигр', self)
        next_tiger_button.clicked.connect(self.show_next_instance_tiger)
        layout.addWidget(next_tiger_button)

        next_leopard_button = QtWidgets.QPushButton('Следующий леопард', self)
        next_leopard_button.clicked.connect(self.show_next_instance_leopard)
        layout.addWidget(next_leopard_button)

        select_folder_button = QtWidgets.QPushButton('Выбрать папку с датасетом', self)
        select_folder_button.clicked.connect(self.select_dataset_folder)
        layout.addWidget(select_folder_button)

        create_annotation_button = QtWidgets.QPushButton('Создать файл аннотации', self)
        create_annotation_button.clicked.connect(self.create_annotation_file)
        layout.addWidget(create_annotation_button)

        self.setLayout(layout)

    def select_dataset_folder(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку с датасетом')
        if folderpath:
            tiger_path = os.path.join(folderpath, 'tiger')
            leopard_path = os.path.join(folderpath, 'leopard')

            self.tiger_paths = [os.path.join(tiger_path, file) for file in os.listdir(tiger_path)]
            self.leopard_paths = [os.path.join(leopard_path, file) for file in os.listdir(leopard_path)]

            self.tiger_cycle = cycle(self.tiger_paths)
            self.leopard_cycle = cycle(self.leopard_paths)

            self.show_next_instance_tiger()

    def show_next_instance_tiger(self):
        instance_path = next(self.tiger_cycle)
        self.current_instance_path = instance_path

        pixmap = QtGui.QPixmap(self.current_instance_path)
        self.image_label.setPixmap(pixmap.scaledToWidth(400))

    def show_next_instance_leopard(self):
        instance_path = next(self.leopard_cycle)
        self.current_instance_path = instance_path

        pixmap = QtGui.QPixmap(self.current_instance_path)
        self.image_label.setPixmap(pixmap.scaledToWidth(400))

    def create_annotation_file(self):
        all_paths = self.tiger_paths + self.leopard_paths
        if all_paths:
            destination_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self, 'Выберите файл для сохранения аннотации', filter='Text files (*.txt)')

            if destination_path:
                with open(destination_path, 'w') as annotation_file:
                    annotation_file.write('\n'.join(all_paths))

                QtWidgets.QMessageBox.information(self, 'Аннотация создана', 'Файл аннотации успешно создан.')
        else:
            QtWidgets.QMessageBox.warning(self, 'Пустой датасет', 'Датасет пуст. Выберите папку с изображениями.')

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = DatasetApp()
    window.show()
    app.exec_()
