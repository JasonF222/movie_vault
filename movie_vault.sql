-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema movie_vault
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `movie_vault` ;

-- -----------------------------------------------------
-- Schema movie_vault
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `movie_vault` DEFAULT CHARACTER SET utf8 ;
USE `movie_vault` ;

-- -----------------------------------------------------
-- Table `movie_vault`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_vault`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `pw_hash` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `movie_vault`.`queues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_vault`.`queues` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `movie_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `title` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_queues_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_queues_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `movie_vault`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `movie_vault`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `movie_vault`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `movie_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `title` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorites_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_favorites_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `movie_vault`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
