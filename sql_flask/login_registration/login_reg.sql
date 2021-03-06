-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema login_reg
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema login_reg
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `login_reg` DEFAULT CHARACTER SET utf8 ;
USE `login_reg` ;

-- -----------------------------------------------------
-- Table `login_reg`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first` VARCHAR(255) NOT NULL,
  `last` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


