-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: mysql
-- ------------------------------------------------------
-- Server version	8.0.28
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `help_keyword`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `help_keyword` (
  `help_keyword_id` int unsigned NOT NULL,
  `name` char(64) NOT NULL,
  PRIMARY KEY (`help_keyword_id`),
  UNIQUE KEY `name` (`name`)
) /*!50100 TABLESPACE `mysql` */ ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 STATS_PERSISTENT=0 ROW_FORMAT=DYNAMIC COMMENT='help keywords';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `help_keyword`
--
-- WHERE:  1 limit 100

INSERT INTO `help_keyword` VALUES (108,'%');
INSERT INTO `help_keyword` VALUES (264,'&');
INSERT INTO `help_keyword` VALUES (422,'(JSON');
INSERT INTO `help_keyword` VALUES (86,'*');
INSERT INTO `help_keyword` VALUES (84,'+');
INSERT INTO `help_keyword` VALUES (85,'-');
INSERT INTO `help_keyword` VALUES (423,'->');
INSERT INTO `help_keyword` VALUES (425,'->>');
INSERT INTO `help_keyword` VALUES (87,'/');
INSERT INTO `help_keyword` VALUES (75,':=');
INSERT INTO `help_keyword` VALUES (59,'<');
INSERT INTO `help_keyword` VALUES (266,'<<');
INSERT INTO `help_keyword` VALUES (58,'<=');
INSERT INTO `help_keyword` VALUES (56,'<=>');
INSERT INTO `help_keyword` VALUES (57,'<>');
INSERT INTO `help_keyword` VALUES (55,'=');
INSERT INTO `help_keyword` VALUES (61,'>');
INSERT INTO `help_keyword` VALUES (60,'>=');
INSERT INTO `help_keyword` VALUES (267,'>>');
INSERT INTO `help_keyword` VALUES (90,'ABS');
INSERT INTO `help_keyword` VALUES (879,'ACCOUNT');
INSERT INTO `help_keyword` VALUES (91,'ACOS');
INSERT INTO `help_keyword` VALUES (659,'ACTION');
INSERT INTO `help_keyword` VALUES (49,'ADD');
INSERT INTO `help_keyword` VALUES (120,'ADDDATE');
INSERT INTO `help_keyword` VALUES (121,'ADDTIME');
INSERT INTO `help_keyword` VALUES (913,'ADMIN');
INSERT INTO `help_keyword` VALUES (270,'AES_DECRYPT');
INSERT INTO `help_keyword` VALUES (271,'AES_ENCRYPT');
INSERT INTO `help_keyword` VALUES (581,'AFTER');
INSERT INTO `help_keyword` VALUES (247,'AGAINST');
INSERT INTO `help_keyword` VALUES (934,'AGGREGATE');
INSERT INTO `help_keyword` VALUES (582,'ALGORITHM');
INSERT INTO `help_keyword` VALUES (721,'ALL');
INSERT INTO `help_keyword` VALUES (50,'ALTER');
INSERT INTO `help_keyword` VALUES (583,'ANALYZE');
INSERT INTO `help_keyword` VALUES (62,'AND');
INSERT INTO `help_keyword` VALUES (526,'ANY_VALUE');
INSERT INTO `help_keyword` VALUES (660,'ARCHIVE');
INSERT INTO `help_keyword` VALUES (254,'ARRAY');
INSERT INTO `help_keyword` VALUES (722,'AS');
INSERT INTO `help_keyword` VALUES (464,'ASC');
INSERT INTO `help_keyword` VALUES (185,'ASCII');
INSERT INTO `help_keyword` VALUES (92,'ASIN');
INSERT INTO `help_keyword` VALUES (774,'ASSIGN_GTIDS_TO_ANONYMOUS_TRANSACTIONS');
INSERT INTO `help_keyword` VALUES (6,'ASYMMETRIC_DECRYPT');
INSERT INTO `help_keyword` VALUES (7,'ASYMMETRIC_DERIVE');
INSERT INTO `help_keyword` VALUES (8,'ASYMMETRIC_ENCRYPT');
INSERT INTO `help_keyword` VALUES (9,'ASYMMETRIC_SIGN');
INSERT INTO `help_keyword` VALUES (10,'ASYMMETRIC_VERIFY');
INSERT INTO `help_keyword` VALUES (643,'AT');
INSERT INTO `help_keyword` VALUES (93,'ATAN');
INSERT INTO `help_keyword` VALUES (94,'ATAN2');
INSERT INTO `help_keyword` VALUES (880,'ATTRIBUTE');
INSERT INTO `help_keyword` VALUES (911,'AUTHENTICATION');
INSERT INTO `help_keyword` VALUES (743,'AUTOCOMMIT');
INSERT INTO `help_keyword` VALUES (584,'AUTOEXTEND_SIZE');
INSERT INTO `help_keyword` VALUES (585,'AUTO_INCREMENT');
INSERT INTO `help_keyword` VALUES (458,'AVG');
INSERT INTO `help_keyword` VALUES (586,'AVG_ROW_LENGTH');
INSERT INTO `help_keyword` VALUES (755,'BACKUP');
INSERT INTO `help_keyword` VALUES (769,'BEFORE');
INSERT INTO `help_keyword` VALUES (744,'BEGIN');
INSERT INTO `help_keyword` VALUES (288,'BENCHMARK');
INSERT INTO `help_keyword` VALUES (63,'BETWEEN');
INSERT INTO `help_keyword` VALUES (186,'BIN');
INSERT INTO `help_keyword` VALUES (253,'BINARY');
INSERT INTO `help_keyword` VALUES (563,'BINLOG');
INSERT INTO `help_keyword` VALUES (527,'BIN_TO_UUID');
INSERT INTO `help_keyword` VALUES (460,'BIT_AND');
INSERT INTO `help_keyword` VALUES (269,'BIT_COUNT');
INSERT INTO `help_keyword` VALUES (187,'BIT_LENGTH');
INSERT INTO `help_keyword` VALUES (461,'BIT_OR');
INSERT INTO `help_keyword` VALUES (462,'BIT_XOR');
INSERT INTO `help_keyword` VALUES (17,'BOOL');
INSERT INTO `help_keyword` VALUES (18,'BOOLEAN');
INSERT INTO `help_keyword` VALUES (230,'BOTH');
INSERT INTO `help_keyword` VALUES (647,'BTREE');
INSERT INTO `help_keyword` VALUES (465,'BY');
INSERT INTO `help_keyword` VALUES (42,'BYTE');
INSERT INTO `help_keyword` VALUES (969,'CACHE');
INSERT INTO `help_keyword` VALUES (689,'CALL');
INSERT INTO `help_keyword` VALUES (497,'CAN_ACCESS_COLUMN');
INSERT INTO `help_keyword` VALUES (498,'CAN_ACCESS_DATABASE');
INSERT INTO `help_keyword` VALUES (499,'CAN_ACCESS_TABLE');
INSERT INTO `help_keyword` VALUES (500,'CAN_ACCESS_USER');
INSERT INTO `help_keyword` VALUES (501,'CAN_ACCESS_VIEW');
INSERT INTO `help_keyword` VALUES (661,'CASCADE');
INSERT INTO `help_keyword` VALUES (76,'CASE');
INSERT INTO `help_keyword` VALUES (255,'CAST');
INSERT INTO `help_keyword` VALUES (860,'CATALOG_NAME');
INSERT INTO `help_keyword` VALUES (95,'CEIL');
INSERT INTO `help_keyword` VALUES (96,'CEILING');
INSERT INTO `help_keyword` VALUES (745,'CHAIN');
INSERT INTO `help_keyword` VALUES (881,'CHALLENGE_RESPONSE');
INSERT INTO `help_keyword` VALUES (587,'CHANGE');
INSERT INTO `help_keyword` VALUES (564,'CHANNEL');
INSERT INTO `help_keyword` VALUES (43,'CHAR');
INSERT INTO `help_keyword` VALUES (39,'CHARACTER');
INSERT INTO `help_keyword` VALUES (189,'CHARACTER_LENGTH');
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-27 22:59:17
