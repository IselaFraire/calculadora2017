import unittest

from cadena import Cadena

class TestCadena(unittest.TestCase):

    def setUp(self):
	self.cad = Cadena()

    def test_que2_lindo1_dia1_hace1_hoy1(self):
	result = self.cad.cadena("que lindo dia que hace hoy")
	self.assertEquals({'que':2,'lindo':1,'dia':1,'hace':1,'hoy':1},result)	


    def test_que2_bonito1_es1_lo1(self):
	result = self.cad.cadena("que bonito es lo bonito")
	self.assertEquals({'que':1,'bonito':2,'es':1,'lo':1},result)	

    def test_El1_negro2_es1_muy1(self):
	result = self.cad.cadena("El negro es muy negro")
	self.assertEquals({'El':1,'negro':2,'es':1,'muy':1},result)	


    def tearDown(self):
	pass

if __name__ == '__main__':
    unittest.main()
