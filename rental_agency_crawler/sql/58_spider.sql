/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50712
 Source Host           : localhost
 Source Database       : crawler1

 Target Server Type    : MySQL
 Target Server Version : 50712
 File Encoding         : utf-8

 Date: 07/06/2016 17:10:50 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `58_spider`
-- ----------------------------
DROP TABLE IF EXISTS `58_spider`;
CREATE TABLE `58_spider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mobile` varchar(20) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `area` varchar(20) DEFAULT NULL,
  `service_area` varchar(50) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile_unique` (`mobile`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=5023 DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;
