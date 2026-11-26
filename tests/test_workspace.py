import unittest
from api.workspace import process

class WorkspaceTest(unittest.TestCase):
    def setUp(self):self.snapshot=None
    def request(self,action,data=None):
        r=process({'project':'doc','action':action,'data':data or {},'snapshot':self.snapshot})
        self.snapshot=r['snapshot']
        return r['result']
    def test_primary_flow(self):
        state=self.request('state')
        self.assertGreaterEqual(len(state['documents']),2)
        hits=self.request('search',{'query':'aluguel'})
        self.assertTrue(any('aluguel' in h['excerpt'].lower() for h in hits))
        self.assertTrue(self.request('facts',{'id':state['documents'][0]['id']}))
    def test_reject_other_project(self):
        with self.assertRaises(ValueError):
            process({'project':'affiliate','action':'state','data':{}})
