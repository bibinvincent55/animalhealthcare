-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2021 at 10:15 AM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `animalhealth`
--

-- --------------------------------------------------------

--
-- Table structure for table `animalbreed`
--

CREATE TABLE IF NOT EXISTS `animalbreed` (
  `anname` varchar(20) NOT NULL,
  `breed` varchar(30) NOT NULL,
  `foodsp` varchar(100) NOT NULL,
  `annature` varchar(100) NOT NULL,
  `anhusbandary` varchar(100) NOT NULL,
  PRIMARY KEY (`anname`,`breed`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `animalbreed`
--

INSERT INTO `animalbreed` (`anname`, `breed`, `foodsp`, `annature`, `anhusbandary`) VALUES
('aass', 'aaaa', 'ccccc', 'vvvvv', 'nnnnnn'),
('Agel Fish', 'African', 'Any food', 'Energetic', 'Fresh water and calm atmosphere'),
('Germen Sheperd', 'aaaa', 'hhhh', 'jjjjj', 'kkkkk'),
('Germen Sheperd', 'bbbbb', 'mmmmmm', 'iiii', 'eeeeeeeeeeee'),
('Ordinary', 'aaa1', 'gggghhh', 'jjjj', 'jj kkkk'),
('Ordinary', 'aaa2', 'gggg', 'hhhhh', 'jjjjj'),
('Vechoor Cow', 'HHigh', 'daily 3 times food', 'slow ', 'Bath daily altleast one time'),
('Vechoor Cow', 'Low', 'hhhhhh', 'jjjjjjjj', 'lllllll');

-- --------------------------------------------------------

--
-- Table structure for table `animaltype`
--

CREATE TABLE IF NOT EXISTS `animaltype` (
  `anname` varchar(30) NOT NULL,
  `Antype` varchar(15) NOT NULL,
  `Production` varchar(20) NOT NULL,
  `specification` varchar(100) NOT NULL,
  PRIMARY KEY (`anname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `animaltype`
--

INSERT INTO `animaltype` (`anname`, `Antype`, `Production`, `specification`) VALUES
('Agel Fish', 'Fish', 'Pet', 'Colourful '),
('Block Hen', 'Hen', 'Egg', 'Rich '),
('Bufellow', 'Cattle', 'Milk', 'healthy milk'),
('Germen Sheperd', 'Dog', 'Pet', 'good dog'),
('Ordinary', 'Dog', 'Pet', 'gg hh jjj '),
('Small Cow', 'Cattle', 'Milk', 'Profitable'),
('Vechoor Cow', 'Cattle', 'Milk', 'looks so small');

-- --------------------------------------------------------

--
-- Table structure for table `applyvaccine`
--

CREATE TABLE IF NOT EXISTS `applyvaccine` (
  `applyno` int(11) NOT NULL,
  `ownerid` varchar(15) NOT NULL,
  `anno` int(11) NOT NULL,
  `vacname` varchar(30) NOT NULL,
  `applydate` date NOT NULL,
  `staffid` varchar(15) NOT NULL,
  PRIMARY KEY (`applyno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `applyvaccine`
--

INSERT INTO `applyvaccine` (`applyno`, `ownerid`, `anno`, `vacname`, `applydate`, `staffid`) VALUES
(1, 'O1001', 1, 'aaa', '2021-04-10', 's1000'),
(2, 'O1001', 1, 'aaa', '2021-04-10', 's1000'),
(3, 'O1001', 1, 'aaa', '2021-04-10', 's1000'),
(4, 'O1005', 1, 'aassdd', '2021-04-10', 's1005'),
(5, 'O1006', 1, 'Covaccin', '2021-04-10', 's1006'),
(6, 'O1006', 1, 'Covaccin', '2021-04-10', 's1006');

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE IF NOT EXISTS `hospital` (
  `hospid` varchar(15) NOT NULL,
  `location` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `district` varchar(20) NOT NULL,
  `hosptype` varchar(15) NOT NULL,
  PRIMARY KEY (`hospid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`hospid`, `location`, `place`, `pin`, `phone`, `district`, `hosptype`) VALUES
('H101', 'Adoor', 'Adoor', '691523', '9944332211', 'Pathanamthitta', 'District Hospit'),
('H102', 'Adoor', 'Adoor', '691523', '9944332211', 'Pathanamthitta', 'District Hospit'),
('H103', 'Adoor', 'Adoor', '691523', '9944332211', 'Pathanamthitta', 'District Hospit'),
('H104', 'Near KSRTC', 'Kollam', '689765', '9765432312', 'Kollam', 'District Hospit'),
('H105', 'Kottayam', 'Kottayam', '687766', '6633445566', 'Kottayam', 'District Hospit'),
('H106', 'Kumbazha', 'Pathanamthitta', '685644', '9922334455', 'Pathanamthitta', 'Clinik'),
('H107', 'Manakkala', 'Adoor', '691524', '8899776655', 'Pathanamthitta', 'Clinik'),
('H108', 'Poothankara', 'Elamannoor', '691524', '5566554433', 'Pathanamthitta', 'District Hospit'),
('H109', 'ITI Jn', 'Chengannur', '689123', '9944667788', 'Alapuzha', 'Clinik');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `userid` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`userid`, `password`) VALUES
('admin', 'abc');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE IF NOT EXISTS `medicine` (
  `medid` varchar(15) NOT NULL,
  `medname` varchar(20) NOT NULL,
  `medtype` varchar(15) NOT NULL,
  `content` varchar(100) NOT NULL,
  `medcategory` varchar(20) NOT NULL,
  `medunit` varchar(15) NOT NULL,
  `company` varchar(20) NOT NULL,
  PRIMARY KEY (`medid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`medid`, `medname`, `medtype`, `content`, `medcategory`, `medunit`, `company`) VALUES
('M1001', 'MMmm', 'Tab', 'ss dd ff', 'Birds', 'Mg', 'AAAA'),
('M1002', 'ssssss', 'Tonic', 'hh  jjj kk  h', 'Birds', 'Mg', 'AAAA'),
('M1003', 'Dolo 500', 'Tab', 'Paracetamol', 'Animals', 'Mg', 'xxxxx'),
('M1004', 'Paracetamol', 'Tab', 'gg hh jj', 'All', 'Mg', 'hhhhhh'),
('M1005', 'Vicorel', 'Tab', 'hh jj kk', 'All', 'Mg', 'yyyyy');

-- --------------------------------------------------------

--
-- Table structure for table `owner`
--

CREATE TABLE IF NOT EXISTS `owner` (
  `ownerid` varchar(15) NOT NULL,
  `ownername` varchar(20) NOT NULL,
  `hname` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `district` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `regdate` date NOT NULL,
  `adhar` varchar(20) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  PRIMARY KEY (`ownerid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `owner`
--

INSERT INTO `owner` (`ownerid`, `ownername`, `hname`, `place`, `pin`, `phone`, `gender`, `hospid`, `district`, `email`, `password`, `regdate`, `adhar`, `staffid`) VALUES
('O1001', 'Kumar', 'KK House', 'PTA', '685233', '9933221122', 'M', 'H101', 'Thiruvananthapuram', 'ttt@gmail.com', 'bbb', '2021-04-10', '1_kJuTJD3.txt', 's1001'),
('O1002', 'Arun', 'AR H0use', 'Adoor', '665566', '7744554433', 'M', 'H101', 'Thiruvananthapuram', 'ggg@gmail.com', 'O1002', '2021-04-11', 'a11.png', 's1000'),
('O1003', 'Ram', 'RR House', 'Adoor', '691523', '8877887766', 'M', 'H101', 'Pathanamthitta', 'ram@gmail.com', 'O1003', '2021-04-11', 'a11_73HfQDO.png', 's1000'),
('O1004', 'Kumar', 'KK House', 'Kumbazha', '683455', '8866554433', 'M', 'H101', 'Pathanamthitta', 'kumar@gmail.com', 'O1004', '2021-04-10', 'a11_0LqKuNx.png', 's1000'),
('O1005', 'Hari Kumar', 'HH House', 'Adoor', '691523', '9966775544', 'M', 'H108', 'Pathanamthitta', 'fff@gmail.com', 'O1005', '2021-04-10', 'a11_1c1NpEI.png', 's1005'),
('O1006', 'Arjun', 'AR House', 'Adoor', '691523', '5566778899', 'M', 'H109', 'Pathanamthitta', 'arjun@gmail.com', 'O1006', '2021-04-10', 'a1.txt', 's1006');

-- --------------------------------------------------------

--
-- Table structure for table `owneranimal`
--

CREATE TABLE IF NOT EXISTS `owneranimal` (
  `ownerid` varchar(15) NOT NULL,
  `anno` int(3) NOT NULL,
  `anname` varchar(20) NOT NULL,
  `breed` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  `ageunit` varchar(10) NOT NULL,
  `origin` varchar(15) NOT NULL,
  `regdate` date NOT NULL,
  `approval` varchar(1) DEFAULT NULL,
  `details` varchar(30) DEFAULT NULL,
  `staffid` varchar(15) DEFAULT NULL,
  `appdate` date DEFAULT NULL,
  `certificate` varchar(20) DEFAULT NULL,
  `exist` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `owneranimal`
--

INSERT INTO `owneranimal` (`ownerid`, `anno`, `anname`, `breed`, `age`, `ageunit`, `origin`, `regdate`, `approval`, `details`, `staffid`, `appdate`, `certificate`, `exist`) VALUES
('O1001', 1, 'Germen Sheperd', 'aaaa', 2, 'Days', 'Purchase', '2021-04-10', '', '', '', '0000-00-00', '1.txt', 'Y'),
('O1001', 2, 'Germen Sheperd', 'bbbbb', 3, 'Month', 'Purchase', '2021-04-10', 'Y', 'jjjj', 's1001', '2021-04-10', '1.txt', 'Y'),
('o1001', 3, 'aass', 'aaaa', 2, 'Days', 'Purchase', '2021-04-11', 'Y', 'ok good', 's1000', '2021-04-10', 'a11.png', 'Y'),
('o1001', 4, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 5, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 6, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 7, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 8, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 9, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 10, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 11, 'aass', 'aaaa', 0, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 12, 'aass', 'aaaa', 3, 'Days', 'Production', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 13, 'aass', 'aaaa', 2, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 14, 'aass', 'aaaa', 3, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1001', 15, 'aass', 'aaaa', 4, 'Days', 'Purchase', '2021-04-10', NULL, NULL, NULL, NULL, NULL, NULL),
('o1005', 1, 'Ordinary', 'aaa1', 2, 'Month', 'Purchase', '2021-04-10', 'Y', 'good', 's1005', '2021-04-10', 'a1.txt', 'Y'),
('o1006', 1, 'Vechoor Cow', 'Low', 3, 'Month', 'Purchase', '2021-04-10', 'Y', 'good', 's1006', '2021-04-10', 'a11_fzFxSSy.png', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `ownerrequest`
--

CREATE TABLE IF NOT EXISTS `ownerrequest` (
  `reqno` int(11) NOT NULL,
  `request` varchar(100) NOT NULL,
  `reqdate` date NOT NULL,
  `ownerid` varchar(15) NOT NULL,
  PRIMARY KEY (`reqno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ownerrequest`
--

INSERT INTO `ownerrequest` (`reqno`, `request`, `reqdate`, `ownerid`) VALUES
(1, 'hello', '2021-04-10', 'O1001'),
(2, 'hello.....', '2021-04-10', 'O1001'),
(3, 'hello.....jjjj', '2021-04-10', 'O1001'),
(4, 'jkjkjkjkjk', '2021-04-10', 'O1001'),
(5, 'take care', '2021-04-10', 'o1001'),
(6, 'ggg hh  jj j', '2021-04-10', 'o1005'),
(7, 'dddd', '2021-04-10', 'o1005'),
(8, 'cmncmxncxmncxm', '2021-04-10', 'o1006');

-- --------------------------------------------------------

--
-- Table structure for table `response`
--

CREATE TABLE IF NOT EXISTS `response` (
  `reqno` int(11) NOT NULL,
  `response` varchar(100) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `respdate` date NOT NULL,
  PRIMARY KEY (`reqno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `response`
--

INSERT INTO `response` (`reqno`, `response`, `staffid`, `respdate`) VALUES
(1, 'ddd', 's1000', '2021-04-10'),
(2, 'dddffff', 's1000', '2021-04-10'),
(3, 'hhhhh', 's1000', '2021-04-10'),
(6, 'k kjkj  l k lklkk', 's1005', '2021-04-10'),
(8, 'njjj kk  kkk k', 's1006', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE IF NOT EXISTS `session` (
  `userid` varchar(15) NOT NULL,
  `hospid` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`userid`, `hospid`) VALUES
('s1006', 'H109');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE IF NOT EXISTS `staff` (
  `staffid` varchar(15) NOT NULL,
  `name` varchar(20) NOT NULL,
  `hname` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `ph` varchar(13) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `email` varchar(20) NOT NULL,
  `qlfn` varchar(20) NOT NULL,
  `designation` varchar(15) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`staffid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staffid`, `name`, `hname`, `place`, `pin`, `ph`, `gender`, `email`, `qlfn`, `designation`, `password`) VALUES
('s1000', 'Anu', 'AA House', 'Adoor', '691523', '9988776655', 'F', 'aa@kk.ll', 'SSLC', 'Doctor', 's1000'),
('S1001', 'Ram', 'RR House', 'Adoor', '691523', '9911223344', 'F', 'rr@gmail.com', 'SSLC', 'Doctor', 'bbb'),
('S1002', 'Varghese', 'XX House', 'Adoor', '691523', '9876564532', 'M', 'vv@gmail.com', 'SSLC', 'Doctor', 'S1002'),
('S1003', 'dffff', 'hhhhh', 'jj', '666778', '5588663322', 'F', 'ggg@gg.kk', 'SSLC', 'Doctor', 'S1003'),
('S1004', 'Hari lal', 'HH House', 'Adoor', '691523', '7865434323', 'M', 'hari@gmail.com', 'MBBS', 'Doctor', 'S1004'),
('S1005', 'Akash', 'AK House', 'Poothankkara', '685544', '7788776655', 'M', 'abc@jj.ll', 'MBBS', 'Doctor', 'S1005'),
('S1006', 'Ben', 'ABC House', 'Chengannur', '687755', '8844554433', 'M', 'ben@gmail.com', 'Degree', 'Office Staff', 'S1006');

-- --------------------------------------------------------

--
-- Table structure for table `staffwork`
--

CREATE TABLE IF NOT EXISTS `staffwork` (
  `staffid` varchar(15) NOT NULL,
  `eno` int(3) NOT NULL,
  `hospid` varchar(15) NOT NULL,
  `regdate` date NOT NULL,
  PRIMARY KEY (`staffid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staffwork`
--

INSERT INTO `staffwork` (`staffid`, `eno`, `hospid`, `regdate`) VALUES
('s1000', 1, 'H101', '2021-04-10'),
('S1001', 1, 'H101', '2021-04-10'),
('S1002', 1, 'H104', '2021-04-10'),
('S1003', 1, 'H101', '2021-04-10'),
('S1004', 1, 'H101', '2021-04-10'),
('S1005', 1, 'H108', '2021-04-10'),
('S1006', 1, 'H109', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `treatment`
--

CREATE TABLE IF NOT EXISTS `treatment` (
  `Tno` int(11) NOT NULL,
  `ownerid` varchar(15) NOT NULL,
  `Anno` int(11) NOT NULL,
  `Problem` varchar(100) NOT NULL,
  `pdate` date NOT NULL,
  `phfname` varchar(20) NOT NULL,
  `pfname` varchar(20) DEFAULT NULL,
  `instruction` varchar(100) DEFAULT NULL,
  `staffid` varchar(15) DEFAULT NULL,
  `Tdate` date DEFAULT NULL,
  PRIMARY KEY (`Tno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `treatment`
--

INSERT INTO `treatment` (`Tno`, `ownerid`, `Anno`, `Problem`, `pdate`, `phfname`, `pfname`, `instruction`, `staffid`, `Tdate`) VALUES
(1, 'O1001', 1, 'ewewe', '2021-04-10', '1.txt', '1_229sQsX.txt', 'ddd', 's1000', '2021-04-10'),
(2, 'O1001', 2, 'ddddd', '2021-04-10', '2.txt', '1_3tFtgL4.txt', 'jjjj', 's1000', '2021-04-10'),
(3, 'O1001', 2, 'lll', '2021-04-10', '2_HnhZOlG.txt', '1_ZnmMnhz.txt', 'ooo', 's1000', '2021-04-10'),
(4, 'O1001', 1, 'vvvvv', '2021-04-10', '1_OM10kko.txt', 'a11.png', 'take care\r\nNo bath', 's1000', '2021-04-10'),
(5, 'o1005', 1, 'Not taking food', '2021-04-10', 'a11.png', 'a11_9tT4FO3.png', 'ui buiu bobiobi', 's1005', '2021-04-10'),
(6, 'o1005', 1, 'dddd', '2021-04-10', 'a11_R5jEfWF.png', NULL, NULL, NULL, NULL),
(7, 'o1006', 1, 'Having no food\r\nlooks very bad', '2021-04-10', 'a11_ddcJ2a8.png', 'a1.txt', 'cvcvccv', 's1006', '2021-04-10');

-- --------------------------------------------------------

--
-- Table structure for table `vaccine`
--

CREATE TABLE IF NOT EXISTS `vaccine` (
  `vacname` varchar(30) NOT NULL,
  `details` varchar(100) NOT NULL,
  PRIMARY KEY (`vacname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vaccine`
--

INSERT INTO `vaccine` (`vacname`, `details`) VALUES
('aaa', 'bbbbb'),
('aassdd', 'hhh jj kkk '),
('bbbb', 'bbbbbgfggfgg'),
('Covaccin', 'prevent covid');

-- --------------------------------------------------------

--
-- Table structure for table `vaccinebreed`
--

CREATE TABLE IF NOT EXISTS `vaccinebreed` (
  `vacname` varchar(30) NOT NULL,
  `anname` varchar(30) NOT NULL,
  `age` int(2) NOT NULL,
  `ageunit` varchar(20) NOT NULL,
  `ndos` int(2) NOT NULL,
  `vqty` int(2) NOT NULL,
  `details` varchar(50) NOT NULL,
  PRIMARY KEY (`vacname`,`anname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vaccinebreed`
--

INSERT INTO `vaccinebreed` (`vacname`, `anname`, `age`, `ageunit`, `ndos`, `vqty`, `details`) VALUES
('aaa', 'Block Hen', 2, 'Days', 2, 1, 'nnj kkk'),
('aaa', 'Germen Sheperd', 1, 'Month', 3, 2, 'dd ff gg hh'),
('aaa', 'Small Cow', 3, 'Month', 2, 2, 'dd ff gg '),
('aassdd', 'Ordinary', 3, 'Month', 3, 10, 'ggg hh hhh'),
('Covaccin', 'Vechoor Cow', 2, 'Month', 2, 10, 'gg hh jj');

-- --------------------------------------------------------

--
-- Table structure for table `visit`
--

CREATE TABLE IF NOT EXISTS `visit` (
  `vno` int(11) NOT NULL,
  `ownerid` varchar(15) NOT NULL,
  `vstatus` varchar(20) NOT NULL,
  `staffid` varchar(15) NOT NULL,
  `vdetails` varchar(100) NOT NULL,
  `vdate` date NOT NULL,
  PRIMARY KEY (`vno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `visit`
--

INSERT INTO `visit` (`vno`, `ownerid`, `vstatus`, `staffid`, `vdetails`, `vdate`) VALUES
(1, 'O1001', 'On Request', 's1000', 'dddd', '2021-04-10'),
(2, 'O1001', 'On Request', 's1000', 'dddd', '2021-04-10'),
(3, 'O1001', 'On Request', 's1000', 'xxx', '2021-04-10'),
(4, 'O1001', 'On Request', 's1000', 'dddd', '2021-04-10'),
(5, 'O1001', 'Regular Visit', 's1000', 'mm jj uu', '2021-04-10'),
(6, 'O1005', 'Regular Visit', 's1005', 'g huu u', '2021-04-10'),
(7, 'O1006', 'Regular Visit', 's1006', 'hh jjjjj kk k k', '2021-04-10');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
