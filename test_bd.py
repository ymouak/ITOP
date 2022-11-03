# coding: utf-8
import sys  
import MySQLdb 
import logging
logging.basicConfig(filename='login.log', encoding='utf-8', level=logging.INFO)
 
try:  
   conn = MySQLdb.connect ( user = "root", passwd = "AwbAwb+1988" ,  db = "test1")
   print ("Connexion etablie")
   cursor = conn.cursor () 
   cursor.execute ("DROP TABLE IF EXISTS Element") 
   cursor.execute ("""CREATE TABLE Element ( 
         numero    INT(4), 
         nom       CHAR(40), 
         colonne   INT(4), 
         ligne     INT(4) 
   )""") 
   cursor.execute ("""INSERT INTO Element (numero, nom, colonne,  
ligne) VALUES 
         (1, 'Hydrogène',1, 1), 
         (2, 'Hélium', 18, 1), 
         (3, 'Lithium', 1, 2), 
         (4, 'Bérylium', 2, 2), 
         (5, 'Bore', 13, 2), 
         (10, 'Néon', 18, 2) 
   """) 

   print("Nombre de colonnes insérées: %d" % cursor.rowcount)
   logging.info("Nombre de colonnes insérées: %d" % cursor.rowcount)  
   cursor.close () 
   conn.commit ()
   cursor = conn.cursor () 
   cursor.execute ("SELECT nom, colonne FROM Element") 
   while (1): 
          row = cursor.fetchone () 
          if row == None: 
                 break 
          print("%s, %s" % (row[0], row[1])) 
   print("Nombre de lignes renvoyées: %d" % cursor.rowcount) 
   cursor.close () 
except MySQLdb.Error, e: 
   print("Erreur %d: %s" % (e.args[0], e.args[1])) 
   sys.exit (1)
