import unittest

from fecha import Fecha

class FechaTest(unittest.TestCase):

    def setUp(self):
        self.fech = Fecha()

    def test_fecha_15_11_2017_quince_nov_dos_mil_diescisiete(self):
        result = self.fech.fecha("15/11/2017")
        self.assertEquals('Quince de Noviembre del dos mil diecisiete',result)

    def test_fecha_10_02_2015_diez_feb_dos_mil_quince(self):
        result = self.fech.fecha("10/02/2015")
        self.assertEquals('Diez de Febrero del dos mil quince',result)

    def test_fecha_27_05_2012_veintisiete_may_dos_mil_doce(self):
        result = self.fech.fecha("27/05/2012")
        self.assertEquals('Veintisiete de Mayo del dos mil doce',result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()



