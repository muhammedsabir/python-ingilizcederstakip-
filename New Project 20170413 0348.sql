-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.27


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema follow
--

CREATE DATABASE IF NOT EXISTS follow;
USE follow;

--
-- Definition of table `ogrenci`
--

DROP TABLE IF EXISTS `ogrenci`;
CREATE TABLE `ogrenci` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `adsoyad` varchar(40) DEFAULT NULL,
  `adres` varchar(250) DEFAULT NULL,
  `telefon` varchar(12) DEFAULT NULL,
  `meslek` varchar(25) DEFAULT NULL,
  `ucret` varchar(10) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `kayit_tarihi` date DEFAULT NULL,
  `bitis_tarihi` date DEFAULT NULL,
  `ders_gunleri` varchar(25) DEFAULT NULL,
  `aylik_takip` date DEFAULT NULL,
  `kac_saat` varchar(2) DEFAULT NULL,
  `baslangic_saat` time DEFAULT NULL,
  `bitis_saat` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


