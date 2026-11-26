"""Loopback-only HTTP workspace. Maintainer: João Victor da Silva (JustJao1)."""
import argparse,base64,csv,datetime as dt,io,json,mimetypes,os,re,threading,time,urllib.parse,urllib.request
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from engine import *
ROOT=Path(__file__).resolve().parent

class Workspace:
    def __init__(self,path,port):self.store=Store(path);self.store.seed();self.port=port;self.stop=threading.Event();self.monitor_lock=threading.Lock();self.flow_lock=threading.Lock()
    def state(self,p):
        kinds=["documents"]
        data={k:self.store.list(p,k) for k in kinds};
        data['ai_available']=False
        return data
    def action(self,p,a,d):
        s=self.store;d=obj(d)
        if p=='doc':
            if a=='import':
                name=text(d.get('name'),220);raw=base64.b64decode(d.get('data',''),validate=True);return s.put(p,'documents',{'title':name,'pages':parse_document(name,raw),'format':Path(name).suffix[1:].upper(),'sample':False})
            if a=='delete':s.remove(p,'documents',d['id']);return {'ok':True}
            if a=='search':return search_docs(s.list(p,'documents'),text(d.get('query'),1000))
            if a=='facts':return facts(s.get(p,'documents',d['id']))
            if a=='compare':
                x=s.get(p,'documents',d['a']);y=s.get(p,'documents',d['b']);need(x['id']!=y['id'],'Selecione documentos distintos.');left={f['value'] for f in facts(x)};right={f['value'] for f in facts(y)};return {'common':sorted(left&right),'removed':sorted(left-right),'added':sorted(right-left),'diff':'\n'.join(unified_diff('\n'.join(p['text'] for p in x['pages']).splitlines(),'\n'.join(p['text'] for p in y['pages']).splitlines(),fromfile=x['title'],tofile=y['title']))[:100000]}
        raise ValueError('Operação desconhecida.')
