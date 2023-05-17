import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import seaborn as sns

class UserInterfaceWindow(QWidget):

    def __init__(self, parent=None):

        super(UserInterfaceWindow, self).__init__(parent)


        self.setObjectName("mainWindow")
        self.resize(827, 669)

        self.figure_displayer_label = QLabel(self)
        self.figure_displayer_label.setGeometry(180, 230, 141, 31)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.figure_displayer_label.setFont(font)
        #self.file_selector_label.setObjectName("file_selector_label")

        self.values_input_lineEdit = QLineEdit(self)
        self.values_input_lineEdit.setGeometry(360, 290, 181, 22)
        #self.values_input_lineEdit.setObjectName("values_input_lineEdit")

        # to block user from entering values first
        # blocks input values option intially so user selects the file first
        self.values_input_lineEdit.setEnabled(False)

        self.figure_displayer_button = QPushButton(self)
        self.figure_displayer_button.setGeometry(362, 230, 181, 28)
        #self.file_selector_button.setObjectName("file_selector_button")

        self.submit_button = QPushButton(self)
        self.submit_button.setGeometry(350, 520, 93, 28)
        #self.submit_button.setObjectName("submit_button")

        self.value_label = QLabel(self)
        self.value_label.setGeometry(180, 280, 151, 41)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.value_label.setFont(font)
        #self.value_label.setObjectName("value_label")

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(140, 60, 571, 101)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setTextFormat(Qt.AutoText)
        #self.label_3.setObjectName("label_3")

        self.Note_header_label = QLabel(self)
        self.Note_header_label.setGeometry(180, 360, 71, 16)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Note_header_label.setFont(font)
        #self.Note_header_label.setObjectName("Note_header_label")

        self.fileshower_label = QLabel(self)
        self.fileshower_label.setGeometry(180, 390, 501, 21)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fileshower_label.setFont(font)
        #self.valid_value_selector_label.setObjectName("valid_value_selector_label")

        self.hit_submit_to_get_figure_label = QLabel(self)
        self.hit_submit_to_get_figure_label.setGeometry(180, 420, 491, 21)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.hit_submit_to_get_figure_label.setFont(font)
        #self.give_space_note_label.setObjectName("give_space_note_label")

        self.enter_file_correct_numofheadings_label = QLabel(self)
        self.enter_file_correct_numofheadings_label.setGeometry(180, 450, 491, 21)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.enter_file_correct_numofheadings_label.setFont(font)
        # self.give_space_note_label.setObjectName("give_space_note_label")

        self.enter_file_correct_headingnames_label = QLabel(self)
        self.enter_file_correct_headingnames_label.setGeometry(180, 480, 600, 21)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.enter_file_correct_headingnames_label.setFont(font)
        # self.give_space_note_label.setObjectName("give_space_note_label")

        self.file_name = QLineEdit(self)
        self.file_name.setGeometry(360, 180, 181, 28)
        #self.file_name.setObjectName("file_name_space")

        self.file_asker_label = QLabel(self)
        self.file_asker_label.setGeometry(180, 180, 151, 16)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.file_asker_label.setFont(font)
        #self.label.setObjectName("label")

        UserInterfaceWindow.setWindowTitle(self, "Time Series Analyzer Application")

        self.figure_displayer_label.setText("Show figure: ")

        self.values_input_lineEdit.setPlaceholderText("Example: 4")

        self.figure_displayer_button.setText("Show Figure")

        self.submit_button.setText("Submit")

        self.value_label.setText("Enter value:")

        self.label_3.setText("Time Series Analyzer Application")

        self.Note_header_label.setText("Note:")

        self.fileshower_label.setText("* After entering filename please click 'Show Figure' button to get figure.")

        self.hit_submit_to_get_figure_label.setText("* After entering a value click 'Submit' to get estimated value.")

        self.enter_file_correct_numofheadings_label.setText("* Enter file with 2 columns only. ")

        self.enter_file_correct_headingnames_label.setText("* First column name should be 'Xdata', Second column name should be 'Ydata'. ")

        self.file_name.setPlaceholderText("Ex: data.csv")

        self.file_asker_label.setText("Enter filename:")

        self.figure_displayer_button.clicked.connect(self.file_selection)
        self.submit_button.clicked.connect(self.submit_button_handler)
        #self.user_details_button.clicked.connect(self.user_details_window_function)

    def submit_button_handler(self):

        value = self.values_input_lineEdit.text()

        if len(value) == 0:
            QMessageBox.warning(self, "Empty value indicator", "No value is enetered. Please enter some value.")
            print("No value is entered. Please enter some value.")

        else:
            #print(self.Pandas_for_file.corr())

            #print(self.Pandas_for_file.describe())

            x = 'Xdata'
            y = 'Ydata'

            y = self.Pandas_for_file[y].values.reshape(-1, 1)
            X = self.Pandas_for_file[x].values.reshape(-1, 1)

            #print(self.Pandas_for_file['Xdata'].values)  # [2.5 5.1 3.2 8.5 3.5 1.5 9.2 ... ]
            #print(self.Pandas_for_file['Xdata'].values.shape)

            #print(X.shape)  # (25, 1)
            print(X)

            #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            SEED = 42

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=SEED)

            print("This is X train: ")
            print(X_train)
            print("This is y train: ")
            print(y_train)

            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            print(regressor.intercept_)
            print(regressor.coef_)

            '''
            def calc(slope, intercept, hours):
                return slope * hours + intercept

            score = calc(regressor.coef_, regressor.intercept_, 4.5)
            print(score)
            '''

            final_val=float(value)
            score = regressor.predict([[final_val]])
            print("Estimate value is: ")
            print(score)

            y_pred = regressor.predict(X_test)
            df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
            print(df_preds)

            plt.plot(X_test,y_pred)
            plt.title("Graph after Linear Regression")
            plt.show()

            QMessageBox.information(self, "Job status", "Estimated value is %.2f" % score)

            fig, ax = plt.subplots()
            sns.heatmap(self.Pandas_for_file.corr(method='pearson'), annot=True, fmt='.4f',cmap=plt.get_cmap('coolwarm'), cbar=False, ax=ax)
            ax.set_yticklabels(ax.get_yticklabels(), rotation="horizontal")
            plt.savefig('result.png', bbox_inches='tight', pad_inches=0.0)
            #print("Matrix profile analyzer completed. Figures saved.")



    def file_selection(self):
        name = self.file_name.text()
        self.Pandas_for_file = pd.read_csv(name)

        print(self.Pandas_for_file)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(x=self.Pandas_for_file['Xdata'], y=self.Pandas_for_file['Ydata'])
        plt.title("Graph before Linear Regression")
        plt.xlabel("X Data")
        plt.ylabel("Y Data")
        plt.show()
        self.values_input_lineEdit.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    mainWindow = UserInterfaceWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()