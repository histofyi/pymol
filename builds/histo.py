from typing import Dict, List, Union
from pymol import cmd

import requests
import webbrowser


class Histo():
  def __init__(self):
    self.say_hello()
    self.data = {}


  def say_hello(self):
    print('Hello! I\'m histo. To perform any action type histo.do_something()')
    print('For help, type histo.help()')


  def help(self):
    print(help)
  

  def get_molecule_id(self, pdb_code:str, assembly_id:int=None, domain:str='abd') -> str:
    return f"{pdb_code}_{assembly_id}_{domain}"
    
    
  def get_structure_url(self, moleucle_id:str, format:str='cif') -> str:
    return f"https://coordinates.histo.fyi/structures/downloads/class_i/without_solvent/{moleucle_id}.{format}"
   
   
  def fetch_structure(self, pdb_code:str, assembly_id:int=1, domain:str='abd'):
    molecule_id = self.get_molecule_id(pdb_code, assembly_id=assembly_id, domain=domain)
    structure_url = self.get_structure_url(molecule_id)
    cmd.load(structure_url)
    

  def fetch_info(self, pdb_code:str) -> Dict:
    if pdb_code not in self.data:  
      info_api_url = f"https://api.histo.fyi/v1/structures/{pdb_code}"
      r = requests.get(info_api_url)
      if r.status_code == 200:
        info = r.json()['structure']
      else:
        info = None
    else:
      info = self.data[pdb_code]
    return info


  def load(self, pdb_code, assembly_id=None, domain='abd'):
    if ',' in pdb_code:
      pdb_codes = pdb_code.split(',')
    else:
      pdb_codes = [pdb_code]
    if not assembly_id:
      assembly_id = 1
    for pdb_code in pdb_codes:
      self.fetch_structure(pdb_code, assembly_id=assembly_id, domain=domain)
      print (f"Loaded {pdb_code} assembly {assembly_id}")
      if pdb_code not in self.data:
        self.data[pdb_code] = self.fetch_info(pdb_code)
  


  def info(self, pdb_code:str):
    info = self.fetch_info(pdb_code)
    print (info)
    print ('Å')
    pass
      

  def structure_page(self, pdb_code:str):
    webbrowser.open(f"https://histo.fyi/structures/view/{pdb_code}")


  def publication(self, pdb_code:str):
    info = self.fetch_info(pdb_code)
    publication = info['publication']
    print (publication['bibjson'])
    if 'url' in publication['bibjson']:
      webbrowser.open(publication['bibjson']['url'])
    pass


  def alpha_chain_info(self, pdb_code:str):
    pass


  def peptide_info(self, pdb_code:str):
    pass


  def beta_chain_info(self, pdb_code:str):
    pass

  
  def tcr_info(self, pdb_code:str):
    pass


  def similar(self, pdb_code:str):
    pass


  def reload(self):
    print (cmd.get_names('objects', 0, selection='(all)'))



  def reset_view(self):
    cmd.reset()

histo = Histo()

help = """
histo meets pymol

This is where the help file will go
"""