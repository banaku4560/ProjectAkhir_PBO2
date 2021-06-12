-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Jun 2021 pada 11.44
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projekkasir`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_barang`
--

CREATE TABLE `data_barang` (
  `kode_barang` varchar(5) NOT NULL,
  `nama_barang` varchar(50) NOT NULL,
  `stok` int(4) NOT NULL,
  `harga_jual` int(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_barang`
--

INSERT INTO `data_barang` (`kode_barang`, `nama_barang`, `stok`, `harga_jual`) VALUES
('AQ01', 'Aqua botol', 15, 6000),
('MI01', 'Indomie Goreng', 2500, 100),
('MS02', 'Mie Sedap Goreng', 10, 2500),
('SB01', 'Susu Beruang', 9500, 100);

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_kasir`
--

CREATE TABLE `data_kasir` (
  `id_kasir` int(3) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `nama_kasir` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_kasir`
--

INSERT INTO `data_kasir` (`id_kasir`, `username`, `password`, `nama_kasir`) VALUES
(1, 'adiind_', 'Adinda123', 'Adinda'),
(2, 'shyfaau_', 'shyfa124', 'Shyfaa');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `data_barang`
--
ALTER TABLE `data_barang`
  ADD PRIMARY KEY (`kode_barang`);

--
-- Indeks untuk tabel `data_kasir`
--
ALTER TABLE `data_kasir`
  ADD PRIMARY KEY (`id_kasir`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `data_kasir`
--
ALTER TABLE `data_kasir`
  MODIFY `id_kasir` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
