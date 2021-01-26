from tir import Webapp
import unittest

class GTPA418(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "31/08/2020", "T1", "M SP 04")
		inst.oHelper.Program('GTPA418')
	
	def GTPA418_CT001(self):
		self.oHelper.SetButton("Outras Ações","BASECOMCTR 1")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Processar Comissão")
		self.oHelper.SetButton("OK")              
		self.oHelper.SetValue('Data emissão NFs de ?', '01/01/2020')         
		self.oHelper.SetValue('Data emissão NFs até ?', '31/12/2020')        
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações","BASECOMCTR 2")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Processar Comissão")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('Vendedor de ?', '')                 
		self.oHelper.SetValue('Vendedor ate ?', 'ZZZZZZ')                
		self.oHelper.SetValue('Data emissão NFs de ?', '01/01/2020')         
		self.oHelper.SetValue('Data emissão NFs até ?', '31/12/2020')        
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações","BASECOMCTR 3")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Processar Comissão")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('Agência de ?', '')                 
		self.oHelper.SetValue('Agência até ?', 'ZZZZZZ') 
		self.oHelper.SetValue('Vendedor de ?', '')                 
		self.oHelper.SetValue('Vendedor até ?', 'ZZZZZZ')                
		self.oHelper.SetValue('Data de ?', '01/01/2020')         
		self.oHelper.SetValue('Data até ?', '31/12/2020')        
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações","BASECOMCTR 1")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Processar Comissão")
		self.oHelper.SetButton("OK")              
		self.oHelper.SetValue('Data emissão NFs de ?', '01/01/2020')         
		self.oHelper.SetValue('Data emissão NFs até ?', '31/12/2020')        
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações", "Exportação Folha Pgto")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('Cod.Comissão de ?', '')
		self.oHelper.SetValue('Cod.Comissão até ?', 'ZZZZZZ')
		self.oHelper.SetValue('Vendedor de ?', '')
		self.oHelper.SetValue('Vendedor até ?', 'ZZZZZZ')
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações", "Est. Exp. Folha")
		self.oHelper.SetValue('Cod.Comissão de ?', '')
		self.oHelper.SetValue('Cod.Comissão até ?', 'ZZZZZZ')
		self.oHelper.SetValue('Vendedor de ?', '')
		self.oHelper.SetValue('Vendedor até ?', 'ZZZZZZ')
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()