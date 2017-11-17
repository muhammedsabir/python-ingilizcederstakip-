BEGIN TRANSACTION;
CREATE TABLE ogrenci                 
                    ( 'id' integer primary key AUTOINCREMENT,
                    'adsoyad' varchar(40) DEFAULT NULL,       
                    'adres' varchar(250) DEFAULT NULL,        
                    'telefon' varchar(12) DEFAULT NULL,       
                    'meslek' varchar(25) DEFAULT NULL,      
                    'ucret' varchar(10) DEFAULT NULL,       
                    'email' varchar(40) DEFAULT NULL,       
                    'kayit_tarihi' date DEFAULT NULL,       
                    'bitis_tarihi' date DEFAULT NULL,       
                    'ders_gunleri' varchar(25) DEFAULT NULL,
                    'aylik_takip' date DEFAULT NULL,        
                    'kac_saat' varchar(2) DEFAULT NULL,     
                    'baslangic_saat' varchar(12) DEFAULT NULL,
                    'bitis_saat' varchar(12) DEFAULT NULL,    
                    'aktif' varchar(12) DEFAULT NULL );
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (8,'fgfd','dfgfdg','dfgfd','dfgfdg','dfgfg','dfgfg','01.01.2017','01.01.2017','2,3,5,','17.04.2017','2','08:00:00','08:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (9,'dfsdfds','dfdsfdfdsf','sdfdf','sdfdf','sdfdsf','sdfdsf','01.01.2017','01.01.2018','2,5,','17.04.2017','2','08:00:00','22:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (10,'sdfsdfsdg','fgfgdf','fdgfdg','dfgdfg','dfgfdg','dfgdfgdfg','01.01.2017','01.01.2017','2,5,','17.04.2017','2','08:00:00','08:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (11,'fdgfdg','dfgfdgfd','dfgfdg','dfgfdg','fdgdfg','dfgfdg','01.01.2017','01.01.2017','2,5,','17.04.2017','2','08:00:00','08:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (17,'muhammed sabır','haznedar','5054238124','yazılım','500','denem@deneme.com','01.01.2017','01.01.2017','2,5,','2017-04-23','2','20:00:00','22:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (18,'musa tos','bakırköy','5054584585','','750','','20.04.2017','20.04.2018','1,2,4,5,','2017-04-22','4','10:00:00','12:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (28,'peyami','','','','850','','01.01.2017','01.01.2017','1,4,','2017-04-27','3','20:00:00','22:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (32,'teyo','','','','','','01.01.2017','01.01.2017','3,6,','2017-04-27','2','20:00:00','22:00:00','1');
INSERT INTO `ogrenci` (id,adsoyad,adres,telefon,meslek,ucret,email,kayit_tarihi,bitis_tarihi,ders_gunleri,aylik_takip,kac_saat,baslangic_saat,bitis_saat,aktif) VALUES (33,'zeynep','','','','','','01.01.2017','01.01.2017','3,6,','2017-04-27','2','18:00:00','20:00:00','1');
COMMIT;
