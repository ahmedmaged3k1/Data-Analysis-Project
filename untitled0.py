import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import pandas as pd
import pandas as pf
import matplotlib.pyplot as plt

file = pd.read_csv ('dataset.csv')
file2= pf.read_csv('BMI.csv')



#Measures of Height Column
def measures_H(self):
    mean1= file['Height'].mean()
    max1= file['Height'].max()
    median1 = file['Height'].median()
    min1= file['Height'].min()
    std1 = file['Height'].std()
    mode1 = file['Height'].mode()[0]
    range1 = max1 - min1
    print("\033[4mCentral Tendency of Height\033[0m")  #Escape Character
    print('Mean of Height is = ' ,"{:.2f}".format(mean1))
    print('Maximum of Height is = ' ,"{:.2f}".format(max1))
    print('Minimum of Height is = ' ,"{:.2f}".format(min1))
    print('Range of Height is = ' ,"{:.2f}".format(range1))
    print('Median of Height  is = ' ,"{:.2f}".format(median1))
    print('Standard Deviation of Height  is = ' ,"{:.2f}".format(std1))
    print('Mode of Height is = ',"{:.2f}".format(mode1))
   
#Measures of Weight Column
def measures_W():    
    mean2= file['Weight'].mean()
    max2= file['Weight'].max()
    min2 =file['Weight'].min()
    median2 = file['Weight'].median()
    std2 = file['Weight'].std()
    mode2=file['Weight'].mode()[1]
    range2= max2 - min2
    print("\033[4mCentral Tendency of Weight\033[0m")
    print('Mean of Weight is = ' ,"{:.2f}".format(mean2))
    print('Mode of Height is = ',"{:.2f}".format(mode2))
    print('Maximum of Weight is = ' ,"{:.2f}".format(max2))
    print('Minimum of Weight is = ' ,"{:.2f}".format(min2))
    print('Range of Weight is = ' ,"{:.2f}".format(range2))
    print('Median of Weight is = ' ,"{:.2f}".format(median2))
    print('Standard Deviation of Weight is = ' ,"{:.2f}".format(std2))
    
    
#Correlation
def correlation():
    s1 = pd.Series(file['Weight'])
    s2 = pd.Series(file['Height'])
    corr = s1.corr(s2)
    print("\033[4mCorrelation between Height and Weight is equal to\033[0m" ,"{:.5f}".format(corr))
   
#PLOTS
def histH():
    file.hist(column='Height',bins = 23)
    plt.title(" Height Histogram")
    plt.ylabel("Frequency")
    plt.xlabel("Height/cm")
    plt.ylim(0, 35)
    plt.xlim(140,200)
    plt.show()
    

def histW():
    file.hist(column="Weight",bins = 23)
    plt.title(" Weight Histogram")
    plt.ylabel("Frequency")
    plt.xlabel("Weight/KG")
    plt.ylim(0, 35)
    plt.xlim(50,160)
    plt.show()

def pie():
    lab = ['Obesity','Extreme Obesity','Weak','Normal','Overweight','Extremely weak']
    sizes = [130,198,22,69,68,13]
    plt.pie(sizes,labels=lab)
    plt.title("Pie Chart of BMI")
    plt.show()
    
def box():
    file.boxplot(column=['Height','Weight'])
    plt.show()

def scatter():
    file.plot(x="Height",y="Weight",kind= "scatter")
    plt.xlim(135,200)
    plt.ylim(45, 165)
    plt.show()
    
    

     

        

class firstW(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super(firstW,self).__init__(parent)
        #Window properties
        self.setWindowTitle("Statistical Analysis Project")
        self.resize(700, 400)
        self.setStyleSheet("background-image : url(portrait.jpg);background-repeat: no-repeat;")
    
        
       
        
        #Box plot button
        box_plot=QtWidgets.QPushButton(self)
        box_plot.setText("Box Plot")
        box_plot.clicked.connect(box)
        box_plot.setGeometry(375, 20, 300, 40)
        box_plot.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        
        #Scatter plot button
        scatter_plot=QtWidgets.QPushButton(self)
        scatter_plot.setText("Scatter Plot")
        scatter_plot.clicked.connect(scatter)
        scatter_plot.setGeometry(375, 63, 300, 40)
        scatter_plot.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        #Measures of Height button
        measure_H_button=QtWidgets.QPushButton(self)
        measure_H_button.setText("Show Measures of Height")
        measure_H_button.clicked.connect(measures_H)
        measure_H_button.setGeometry(375, 105, 300, 40)
        measure_H_button.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        

   
        #Measures of Weight button
        measure_W_button=QtWidgets.QPushButton(self)
        measure_W_button.setText("Show Measures of Weight")
        measure_W_button.clicked.connect(measures_W)
        measure_W_button.setGeometry(375, 147, 300, 40)
        measure_W_button.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        #Correlation button
        corr=QtWidgets.QPushButton(self)
        corr.setText("Correlation value")
        corr.clicked.connect(correlation)
        corr.setGeometry(375, 190, 300, 40)
        corr.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        
        #Historam_Height button
        hist_H=QtWidgets.QPushButton(self)
        hist_H.setText("Histogram of Height")
        hist_H.clicked.connect(histH)
        hist_H.setGeometry(375, 233, 300, 40)
        hist_H.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        #Histogram_Weight button
        hist_W=QtWidgets.QPushButton(self)
        hist_W.setText("Histogram of Weight")
        hist_W.clicked.connect(histW)
        hist_W.setGeometry(375, 277, 300, 40)
        hist_W.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        pie_button=QtWidgets.QPushButton(self)
        pie_button.setText("Pie Chart")
        pie_button.clicked.connect(pie)
        pie_button.setGeometry(375, 320, 300, 40)
        pie_button.setStyleSheet("color: white;background: red;font-size:12pt;font-weight: bold")
        
        
        
#class otherwindow(QMainWindow):
      
   


        
if __name__ == "__main__":
    # create pyqt5 app
    app = QApplication(sys.argv)
    # create the instance of our Window
    main= firstW()
    main.show()
    #start the app
    sys.exit(app.exec_())
    
