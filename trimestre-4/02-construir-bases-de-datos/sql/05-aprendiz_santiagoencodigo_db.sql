-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 09-03-2026 a las 13:45:57
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `aprendiz_santiagoencodigo_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aprendiz`
--

CREATE TABLE `aprendiz` (
  `ID_APRENDIZ` int(11) NOT NULL,
  `APR_NOMBRE` varchar(100) NOT NULL,
  `APR_APELLIDO` varchar(100) NOT NULL,
  `APR_CORREO` varchar(120) NOT NULL,
  `APR_UBICACION` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `aprendiz`
--

INSERT INTO `aprendiz` (`ID_APRENDIZ`, `APR_NOMBRE`, `APR_APELLIDO`, `APR_CORREO`, `APR_UBICACION`) VALUES
(1, 'Juan', 'Pérez', 'juan.perez@example.com', 'Ciudad A'),
(2, 'María', 'Gómez', 'maria.gomez@example.com', 'Ciudad B'),
(3, 'Pedro', 'López', 'pedro.lopez@example.com', 'Ciudad C'),
(4, 'Laura', 'Torres', 'laura.torres@example.com', 'Ciudad A'),
(5, 'Carlos', 'Rodríguez', 'carlos.rodriguez@example.com', 'Ciudad B');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `posiciones`
--

CREATE TABLE `posiciones` (
  `id` int(11) NOT NULL,
  `grupo` char(10) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `jugados` int(11) NOT NULL,
  `ganados` int(11) NOT NULL,
  `empatados` int(11) NOT NULL,
  `perdidos` int(11) NOT NULL,
  `puntos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_contacto_aprendiz`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_contacto_aprendiz` (
`APR_NOMBRE` varchar(100)
,`APR_CORREO` varchar(120)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_contacto_aprendiz`
--
DROP TABLE IF EXISTS `vista_contacto_aprendiz`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_contacto_aprendiz`  AS SELECT `aprendiz`.`APR_NOMBRE` AS `APR_NOMBRE`, `aprendiz`.`APR_CORREO` AS `APR_CORREO` FROM `aprendiz` ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `aprendiz`
--
ALTER TABLE `aprendiz`
  ADD PRIMARY KEY (`ID_APRENDIZ`);

--
-- Indices de la tabla `posiciones`
--
ALTER TABLE `posiciones`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pais` (`pais`),
  ADD KEY `grupo` (`grupo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `posiciones`
--
ALTER TABLE `posiciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
