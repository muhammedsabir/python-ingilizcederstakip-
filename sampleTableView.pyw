from PyQt4 import QtCore, QtGui, QtSql
  
import connection
  
  
def initializeModel(model):
    model.setTable('ogrenci')
  
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.select()
  
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
  
  
def createView(title, model):
    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view
  
  
if __name__ == '__main__':
  
    import sys
  
    app = QtGui.QApplication(sys.argv)
    if not connection.createConnection():
        sys.exit(1)
  
    model = QtSql.QSqlTableModel()
  
    initializeModel(model)
  
    view1 = createView("Table Model (View 1)", model)
    view2 = createView("Table Model (View 2)", model)
  
    view1.show()
    view2.move(view1.x() + view1.width() + 20, view1.y())
    view2.show()
  
    sys.exit(app.exec_())
