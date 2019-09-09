-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Route88_Inventory
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Route88_Inventory
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Route88_Inventory` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema Route88_EmployeeInfo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Route88_EmployeeInfo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Route88_EmployeeInfo` ;
USE `Route88_Inventory` ;

-- -----------------------------------------------------
-- Table `Route88_Inventory`.`Item_MenuList`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_Inventory`.`Item_MenuList` (
  `MenuCode` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Cost` FLOAT NOT NULL,
  `IncludeInMenu` TINYINT NOT NULL,
  `CreationTime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `LastUpdate` TIMESTAMP NULL,
  PRIMARY KEY (`Cost`, `Name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route88_Inventory`.`Inventory_ItemList`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_Inventory`.`Inventory_ItemList` (
  `ItemCode` INT NOT NULL,
  `ItemName` VARCHAR(45) NOT NULL,
  `ItemType` VARCHAR(45) NOT NULL,
  `Cost` FLOAT NOT NULL,
  `ExpiryDate` DATE NOT NULL,
  `AvailableStock` INT NOT NULL,
  `CreationTime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `LastUpdate` TIMESTAMP NULL,
  `Menu_Customer_Cost` FLOAT NOT NULL,
  `Menu_Customer_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ItemCode`),
  INDEX `fk_InventoryList_Menu_Customer1_idx` (`Menu_Customer_Cost` ASC, `Menu_Customer_Name` ASC),
  CONSTRAINT `fk_InventoryList_Menu_Customer1`
    FOREIGN KEY (`Menu_Customer_Cost` , `Menu_Customer_Name`)
    REFERENCES `Route88_Inventory`.`Item_MenuList` (`Cost` , `Name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route88_Inventory`.`Supplier_ReferenceList`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_Inventory`.`Supplier_ReferenceList` (
  `SupplierCode` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `LastDeliveryDate` DATE NOT NULL,
  `NextDeliveryDate` DATE NOT NULL,
  `CreationTime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `LastUpdate` TIMESTAMP NULL,
  PRIMARY KEY (`SupplierCode`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route88_Inventory`.`Supplier_TransactionList`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_Inventory`.`Supplier_TransactionList` (
  `ItemCode` INT NOT NULL,
  `OrderCode` INT NOT NULL,
  `SupplierCode` INT NOT NULL,
  `OrderDate` DATE NOT NULL,
  `QuantityReceived` INT NOT NULL,
  `CreationTime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  `LastUpdate` TIMESTAMP NULL,
  PRIMARY KEY (`OrderCode`),
  INDEX `FK_OL_ItemCode_idx` (`ItemCode` ASC),
  INDEX `FK_OL_SupplierCode_idx` (`SupplierCode` ASC),
  CONSTRAINT `FK_OL_ItemCode`
    FOREIGN KEY (`ItemCode`)
    REFERENCES `Route88_Inventory`.`Inventory_ItemList` (`ItemCode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_OL_SupplierCode`
    FOREIGN KEY (`SupplierCode`)
    REFERENCES `Route88_Inventory`.`Supplier_ReferenceList` (`SupplierCode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route88_Inventory`.`Item_TransactionList`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_Inventory`.`Item_TransactionList` (
  `TransactionCode` INT NOT NULL,
  `MenuCode` INT NOT NULL,
  `Cost` FLOAT NOT NULL,
  `CreationTime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`TransactionCode`),
  INDEX `FK_TL_Cost_idx` (`Cost` ASC),
  CONSTRAINT `FK_TL_Cost`
    FOREIGN KEY (`Cost`)
    REFERENCES `Route88_Inventory`.`Item_MenuList` (`Cost`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route88_Inventory`.`Receipts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_Inventory`.`Receipts` (
  `TransactionCode` INT NOT NULL,
  `TotalCost` FLOAT NOT NULL,
  `VatableCost` FLOAT NOT NULL,
  `VatExempt` FLOAT NOT NULL,
  `ZeroRated` FLOAT NOT NULL,
  `NetVat` FLOAT NOT NULL,
  `VatRate` FLOAT NOT NULL,
  `CreationTime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  INDEX `FK_TL_TransactionCode_idx` (`TransactionCode` ASC),
  CONSTRAINT `FK_TT_TransactionCode`
    FOREIGN KEY (`TransactionCode`)
    REFERENCES `Route88_Inventory`.`Item_TransactionList` (`TransactionCode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `Route88_EmployeeInfo` ;

-- -----------------------------------------------------
-- Table `Route88_EmployeeInfo`.`JobPosition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_EmployeeInfo`.`JobPosition` (
  `PositionCode` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PositionCode`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Route88_EmployeeInfo`.`Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Route88_EmployeeInfo`.`Employees` (
  `EmployeeCode` INT NOT NULL,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `PositionCode` INT NOT NULL,
  `DOB` DATE NOT NULL,
  `Address` VARCHAR(300) NOT NULL,
  `SSS` INT(10) NOT NULL,
  `TIN` INT(12) NOT NULL,
  `PhilHealth` INT(12) NOT NULL,
  `CreationTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  `LastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`EmployeeCode`),
  INDEX `FK_EL_PositionCode_idx` (`PositionCode` ASC),
  CONSTRAINT `FK_EL_PositionCode`
    FOREIGN KEY (`PositionCode`)
    REFERENCES `Route88_EmployeeInfo`.`JobPosition` (`PositionCode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE USER 'temp_firstTime' IDENTIFIED BY 'dbms_UserActivation';

GRANT SELECT ON TABLE `Route88_Inventory`.* TO 'temp_firstTime';
GRANT SELECT ON TABLE `Route88_EmployeeInfo`.* TO 'temp_firstTime';
GRANT SELECT, INSERT, TRIGGER ON TABLE `Route88_Inventory`.* TO 'temp_firstTime';
GRANT SELECT, INSERT, TRIGGER ON TABLE `Route88_EmployeeInfo`.* TO 'temp_firstTime';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
