import wx
from wx.core import Event
import noname
import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="projekkasir")
cursor=conn.cursor()

class TampilanAwal(noname.pageUtamaBanget):
    def __init__(self, parent):
        noname.pageUtamaBanget.__init__(self,parent)
        self.pageLogin = Login(parent=self)
        self.pageRegister = Register(parent=self)

    def startLoginOnButtonClick(self,event):
        self.pageLogin.Show()

    def startRegistrasiOnButtonClick(self,event):
        self.pageRegister.Show()

class Register(noname.pageRegistrasi):
    def __init__(self, parent):
        noname.pageRegistrasi.__init__(self,parent)
        self.pageUtama = Utama(parent=self)

    def btnRegisterOnButtonClick(self,event):
        reg_nama = str(self.regNama.GetValue())
        reg_username = str(self.regUsername.GetValue())
        reg_pass = str(self.regPassword.GetValue())

        query = "insert into data_kasir values('','{}','{}','{}')".format(reg_nama,reg_username,reg_pass)
        cursor.execute(query)
        conn.commit()

        wx.MessageBox('Registrasi Berhasil!','Information',wx.OK | wx.ICON_INFORMATION )

        a=TampilanAwal(None)
        a.Show()
        self.Hide()

class Login(noname.pageLogin):
    def __init__(self,parent):
        noname.pageLogin.__init__(self,parent)
        self.pageUtama = Utama(parent = self)
        # self.pageLoginSalah = LoginSalah(parent=self)

    def btnLoginOnButtonClick(self,event):
        a = str(self.inputUsername.GetValue())
        b = str(self.inputPassword.GetValue())

        query = "select id_kasir from data_kasir where username='{}' and password='{}'".format(a,b)
        cursor.execute(query)
        id=cursor.fetchall()
        try:
            self.pageUtama.Show()
            return id[0][0]
        except:
            # self.pageLoginSalah.Show()
            self.pageUtama.Hide()
            wx.MessageBox('Data yang anda masukkan salah!\nSilahkan login kembali','Information',wx.OK | wx.ICON_INFORMATION )

        a=Login(None)
        a.Show()
        self.Hide()
        

class Utama(noname.pageUtama):
    def __init__(self,parent):
        noname.pageUtama.__init__(self,parent)
        self.p2 = Kasir(self)
        self.p3 = LihatData(self)
        self.p4 = TambahData(self)
        self.p5 = EditData(self)
        
    def show_kasir(self):
        self.p2.Show()
        self.p3.Hide()
        self.p4.Hide()
        self.p5.Hide()

    def show_data(self):
        self.p2.Hide()
        self.p3.Show()
        self.p4.Hide()
        self.p5.Hide()

    def show_tambah(self):
        self.p2.Hide()
        self.p3.Hide()
        self.p4.Show()
        self.p5.Hide()

    def show_edit(self):
        self.p2.Hide()
        self.p3.Hide()
        self.p4.Hide()
        self.p5.Show()

    def startKasirOnButtonClick(self, event):
        self.show_kasir()

    def startLihatBarangOnButtonClick(self, event):
        self.show_data()

    def startTambahDataOnButtonClick(self, event):
        self.show_tambah()

    def startEditBarangOnButtonClick(self, event):
        self.show_edit()


class Kasir(noname.pageKasir):
    def __init__(self,parent):
        noname.pageKasir.__init__(self,parent.panelUtama)
        self.parent = parent

    def inputKodeBarangOnText( self, event ):
        h = str(self.inputKodeBarang.GetValue())

        query="select nama_barang from data_barang where kode_barang='{}'".format(h)
        cursor.execute(query)
        data=cursor.fetchall()
        self.teksNamaBarang.SetLabelText(data[0][0])

    def inputJmlBarangOnText( self, event ):
        i = str(self.inputKodeBarang.GetValue())
        j = int(self.inputJmlBarang.GetValue())

        query="select harga_jual from data_barang where kode_barang='{}'".format(i)
        cursor.execute(query)
        harga=cursor.fetchall()

        total = j * harga[0][0]
        self.teksTotal.SetLabelText(str(total))

    def btnHitungOnButtonClick( self, event ):
        k = str(self.inputKodeBarang.GetValue())
        l = int(self.inputJmlBarang.GetValue())
        m = int(self.inputBayar.GetValue())

        query="select harga_jual from data_barang where kode_barang='{}'".format(k)
        cursor.execute(query)
        harga=cursor.fetchall()

        total = l * harga[0][0]

        susuk = m - total

        self.teksKembalian.SetLabelText(str(susuk))


class LihatData(noname.pageDataBarang):
    def __init__(self,parent):
        noname.pageDataBarang.__init__(self,parent.panelUtama)
        self.parent = parent

        query = 'SELECT kode_barang, nama_barang, stok, harga_jual FROM data_barang'
        cursor.execute(query)
        tabel = cursor.fetchall()

        for b in range(4):
            a = 0
            for row in tabel:
                self.tabelBarang.SetCellValue(a, b, str(row[b]))
                a = a + 1

class TambahData(noname.pageTambahBarang):
    def __init__(self,parent):
        noname.pageTambahBarang.__init__(self,parent.panelUtama)
        self.parent = parent
        # self.pageBerhasilTambah = BerhasilTambah(parent =self)

    def dialogTambahBrgOnSaveButtonClick( self, event ):
        c = str(self.tambahKodeBrg.GetValue())
        d = str(self.tambahNamaBrg.GetValue())
        e = int(self.tambahStok.GetValue())
        f = int(self.tambahHargaJual.GetValue()) 
        
        query="Insert into data_barang values('{}','{}',{},{})".format(c,d,e,f)
        cursor.execute(query)
        conn.commit()

        # self.pageBerhasilTambah.Show()
        wx.MessageBox('Data berhasil ditambahkan!','Information',wx.OK | wx.ICON_INFORMATION )

    def dialogTambahBrgOnCancelButtonClick( self, event ):
        self.parent.show_data()

class EditData(noname.pageEditBarang):
    def __init__(self,parent):
        noname.pageEditBarang.__init__(self,parent.panelUtama)
        self.parent = parent
        # self.pageBerhasilUbah = BerhasilUbah(parent=self)

    def cekKodeOnText(self, event):
        n = str(self.cekKode.GetValue())
        query="select nama_barang from data_barang where kode_barang='{}'".format(n)
        cursor.execute(query)
        data1=cursor.fetchall()
        self.teksCekBarang.SetLabelText(data1[0][0])

    def dialogEditOnSaveButtonClick(self, event):
        o = str(self.editNama.GetValue())
        p = int(self.editStok.GetValue())
        q = int(self.editHarga.GetValue())
        r = str(self.cekKode.GetValue())

        query="update data_barang set nama_barang='{}', stok={}, harga_jual={} where kode_barang='{}'".format(o,p,q,r)
        cursor.execute(query)
        conn.commit()

        # self.pageBerhasilUbah.Show()
        wx.MessageBox('Data berhasil diubah!','Information',wx.OK | wx.ICON_INFORMATION )

    

app = wx.App()
frame = TampilanAwal(parent=None)
frame.Show()
app.MainLoop()