import unittest

from Edad import Edad

class EdadTest(unittest.TestCase):

    def setUp(self):
	self.ed = Edad()

    def test_edad_0_no_existes(self):
	result = self.ed.edad(0)
	self.assertEquals('No existes',result)
	
    def test_edad_13_eres_nino(self):
	result = self.ed.edad(13)
	self.assertEquals('Eres nino',result)

    def test_edad_18_eres_adolescente(self):
	result = self.ed.edad(18)
	self.assertEquals('Eres adolescente',result)

    def test_edad_65_eres_adulto(self):
	result = self.ed.edad(65)
	self.assertEquals('Eres adulto',result)

    def test_edad_120_eres_adulto_mayor(self):
	result = self.ed.edad(120)
	self.assertEquals('Eres adulto mayor',result)

    def test_edad_121_eres_adulto_mayor(self):
	result = self.ed.edad(121)
	self.assertEquals('Eres Mumma-Ra',result)

    def tearDown(self):
	pass

if __name__ == '__main__':
    unittest.main()


