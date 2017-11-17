#!/usr/bin/env python
import csv
import functools
import xmlrpclib
HOST = 'atanipuebla.ddns.me'
#HOST = '172.17.0.2'
PORT = 8069
DB = 'Atani_dev2'
USER = 'gbarrientos@soluciones4g.com'
PASS = 'Happy2016*'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
#*****************************************************************************************
#*****************************************************************************************

reader = csv.reader(open('marcas.csv', 'rb'))

#actualizar campos de contactos comparando por nombre
for row in reader:
    #nome=row[1]
    nombre = call('product.template', 'search', [('name', '=', row[1])])
    marc = call('x.model.marcas', 'search', [('x_name', '=', row[5])])
    #print marc
    if len(nombre)>0 :
        #print row[5]
        partner_id = call('product.template', 'write', [nombre[0]], {'x_marcaProducto': marc[0]})
        print partner_id
 
"""
ids = call('product.template', 'search_read', [('id','=','2996')],['x_marcaProducto'])
#print "\n partner ids %s" % ids
for x in ids:
    print x
"""