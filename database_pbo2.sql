-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 02 Jun 2021 pada 16.15
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
-- Database: `database_pbo2`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_akun`
--

CREATE TABLE `data_akun` (
  `username` varchar(7) NOT NULL,
  `password` varchar(7) NOT NULL,
  `nama` varchar(12) NOT NULL,
  `role` int(1) NOT NULL,
  `tanggal_pembuatan` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_akun`
--

INSERT INTO `data_akun` (`username`, `password`, `nama`, `role`, `tanggal_pembuatan`) VALUES
('bagus', 'bagus12', 'bagusnk', 1, '2021-06-02'),
('dinda', 'dinda12', 'adinda', 3, '2021-06-02'),
('shyfa', 'shyfa12', 'shyfanaya', 2, '2021-06-02');

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_barang`
--

CREATE TABLE `data_barang` (
  `kode_barang` varchar(3) NOT NULL,
  `nama_barang` varchar(15) NOT NULL,
  `stok` int(3) NOT NULL,
  `harga_jual` int(7) NOT NULL,
  `harga_beli` int(7) NOT NULL,
  `tanggal_pembayaran` date NOT NULL,
  `tanggal_kadaluarsa` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_detail_pesanan`
--

CREATE TABLE `data_detail_pesanan` (
  `kode_pesanan` int(3) NOT NULL,
  `username` varchar(7) NOT NULL,
  `tanggal` date NOT NULL,
  `pembayaran` int(8) NOT NULL,
  `kembalian` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_pesanan`
--

CREATE TABLE `data_pesanan` (
  `kode_pesanan` int(3) NOT NULL,
  `kode_barang` varchar(3) NOT NULL,
  `quantity` int(3) NOT NULL,
  `sub_total` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `data_akun`
--
ALTER TABLE `data_akun`
  ADD PRIMARY KEY (`username`);

--
-- Indeks untuk tabel `data_barang`
--
ALTER TABLE `data_barang`
  ADD PRIMARY KEY (`kode_barang`);

--
-- Indeks untuk tabel `data_detail_pesanan`
--
ALTER TABLE `data_detail_pesanan`
  ADD KEY `username` (`username`),
  ADD KEY `kode_pesanan` (`kode_pesanan`);

--
-- Indeks untuk tabel `data_pesanan`
--
ALTER TABLE `data_pesanan`
  ADD PRIMARY KEY (`kode_pesanan`),
  ADD KEY `kode_barang` (`kode_barang`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `data_pesanan`
--
ALTER TABLE `data_pesanan`
  MODIFY `kode_pesanan` int(3) NOT NULL AUTO_INCREMENT;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `data_detail_pesanan`
--
ALTER TABLE `data_detail_pesanan`
  ADD CONSTRAINT `data_detail_pesanan_ibfk_2` FOREIGN KEY (`username`) REFERENCES `data_akun` (`username`),
  ADD CONSTRAINT `data_detail_pesanan_ibfk_3` FOREIGN KEY (`kode_pesanan`) REFERENCES `data_pesanan` (`kode_pesanan`);

--
-- Ketidakleluasaan untuk tabel `data_pesanan`
--
ALTER TABLE `data_pesanan`
  ADD CONSTRAINT `kode_barang` FOREIGN KEY (`kode_barang`) REFERENCES `data_barang` (`kode_barang`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
