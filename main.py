import wx
import noname
import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="projek_kasir")
cursor=conn.cursor()

class Mulai(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        self.pageBeranda = Beranda(parent=self)

    def btnStartOnButtonClick(self, event):
        self.pageBeranda.Show()

class Beranda(noname.pageBeranda):
    def __init__(self, parent):
        noname.pageBeranda.__init__(self,parent)
        self.pageKasir = Kasir(parent=self)
        self.pageBarang = DataBarang(parent=self)

    def startKasirOnButtonClick( self, event ):
        self.pageKasir.Show()

    def startDataOnButtonClick( self, event ):
        self.pageBarang.Show()

class Kasir(noname.pageKasir):
    def __init__(self, parent):
        noname.pageKasir.__init__(self,parent)

    def cekKodeBarang1OnText( self, event ):
        e = str(self.cekKodeBarang1.GetValue())

        query="Select nama_barang from kasir where kode_barang='{}'".format(e)
        cursor.execute(query)
        self.data = cursor.fetchall()

        self.namaBarang.SetLabelText(self.data[0][0])
        

    def addCartOnButtonClick( self, event ):
        e = str(self.cekKodeBarang1.GetValue())
        f = int(self.jumlahBarang.GetValue())
        order = []

        query="select harga_barang from kasir where kode_barang='{}'".format(e)
        cursor.execute(query)
        self.data1=cursor.fetchall()
        # query="Select nama_barang from kasir where kode_barang='{}'".format(e)
        # cursor.execute(query)
        # self.data = cursor.fetchall()
        
        order.append(self.data1[0][0])
        print(order)
        # e = str(self.cekKodeBarang1.GetValue())
        # f = int(self.jumlahBarang.GetValue())
        # query="Select harga_barang from kasir where kode_barang='{}'".format(e)
        # cursor.execute(query)
        # data1 = cursor.fetchall()






class DataBarang(noname.pageBarang):
    def __init__(self, parent):
        noname.pageBarang.__init__(self,parent)
        self.pageTambahBarang=TambahBarang(parent=self)

    def startTambahBrgOnButtonClick( self, event ):
        self.pageTambahBarang.Show()

class TambahBarang(noname.pageTambahBarang):
    def __init__(self, parent):
        noname.pageTambahBarang.__init__(self, parent)

    def dialogBox1OnSaveButtonClick( self, event ):
        a = str(self.inputKodeBrg.GetValue())
        b = str(self.inputNamaBrg.GetValue())
        c = int(self.inputHargaBrg.GetValue())
        d = int(self.inputJmlBrg.GetValue())  
        
        query="Insert into kasir values('','{}','{}',{},{})".format(a,b,c,d)
        cursor.execute(query)
        conn.commit()


    # def 

app = wx.App()
frame = Mulai(None)
frame.Show()
app.MainLoop()
