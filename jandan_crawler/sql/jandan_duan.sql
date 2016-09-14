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

 Date: 09/14/2016 23:07:57 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `jandan_duan`
-- ----------------------------
DROP TABLE IF EXISTS `jandan_duan`;
CREATE TABLE `jandan_duan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `duan` varchar(400) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_duan` (`duan`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=37262 DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;
