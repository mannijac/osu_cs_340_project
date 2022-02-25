-- MySQL dump 10.16  Distrib 10.1.37-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: cartridgecollector
-- ------------------------------------------------------
-- Server version 10.1.37-MariaDB
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
--
-- Table structure for table users'
--
DROP TABLE IF EXISTS users;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE users (
  user_id int NOT NULL UNIQUE AUTO_INCREMENT,
  email varchar(30) UNIQUE NOT NULL,
  screen_name varchar(30) NOT NULL,
  country varchar,
  PRIMARY KEY (user_id)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table users'
--
LOCK TABLES users WRITE;
/*!40000 ALTER TABLE users DISABLE KEYS */;
/*!40000 ALTER TABLE users ENABLE KEYS */;
UNLOCK TABLES;
--
-- Table structure for table games
--
DROP TABLE IF EXISTS games;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE games (
  game_id int NOT NULL UNIQUE AUTO_INCREMENT,
  title varchar(30) NOT NULL,
  platform varchar(30) NOT NULL,
  genre varchar, 
  developer varchar,
  publisher varchar(30) NOT NULL,
  release_date date NOT NULL,
  PRIMARY KEY (game_id),
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table games
--
LOCK TABLES games WRITE;
/*!40000 ALTER TABLE games DISABLE KEYS */;
/*!40000 ALTER TABLE games ENABLE KEYS */;
UNLOCK TABLES;
--
-- Table structure for table wishes
--
DROP TABLE IF EXISTS wishes;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE wishes (
  user_id int NOT NULL,
  game_id int NOT NULL,
  PRIMARY KEY (wishes_fk),
  CONSTRAINT wishes_fk FOREIGN KEY (user_id) REFERENCES users
(user_id) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table wishes
--
LOCK TABLES wishes WRITE;
/*!40000 ALTER TABLE wishes DISABLE KEYS */;
/*!40000 ALTER TABLE wishes ENABLE KEYS */;
UNLOCK TABLES;
--
-- Table structure for table ratings
--
DROP TABLE IF EXISTS ratings;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE ratings (
  user_id int NOT NULL,
  game_id int NOT NULL,
  rating_value int NOT NULL, 
  rating_comment VARCHAR,
  PRIMARY KEY (ratings_fk),
  CONSTRAINT ratings_fk FOREIGN KEY (user_id) REFERENCES users
(user_id) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table ratings
--
LOCK TABLES ratings WRITE;
/*!40000 ALTER TABLE ratings DISABLE KEYS */;
/*!40000 ALTER TABLE ratings ENABLE KEYS */;
UNLOCK TABLES;
--
-- Table structure for table collections
--
DROP TABLE IF EXISTS collections;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE collections (
  user_id int NOT NULL,
  game_id int NOT NULL,
  CONSTRAINT collections_fk FOREIGN KEY (user_id) REFERENCES users
(user_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT collections_fk FOREIGN KEY (game_id) REFERENCES games
(game_id) ON DELETE SET NULL ON UPDATE CASCADE
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Dumping data for table collections
--
LOCK TABLES collections WRITE;
/*!40000 ALTER TABLE collections DISABLE KEYS */;
/*!40000 ALTER TABLE collections ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
