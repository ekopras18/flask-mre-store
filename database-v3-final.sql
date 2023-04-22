-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 09, 2019 at 09:05 AM
-- Server version: 5.7.17-log
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database_skripsi_master`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_address`
--

CREATE TABLE `admin_address` (
  `id_aa` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phonenumber` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `twitter` varchar(100) NOT NULL,
  `facebook` varchar(100) NOT NULL,
  `instagram` varchar(100) NOT NULL,
  `weixin` varchar(100) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `motive` text NOT NULL,
  `picture` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin_address`
--

INSERT INTO `admin_address` (`id_aa`, `name`, `address`, `phonenumber`, `email`, `twitter`, `facebook`, `instagram`, `weixin`, `title`, `content`, `motive`, `picture`) VALUES
(1, 'Mre 商店, Inc', '中国广西南宁市大学东路188号', '15678903347', 'admin@mrestore.com', 'https://twitter.com/eko_prasetio8', 'https://facebook.com/ekopras', 'https://instagram.com/ekopras18', 'https://qq.weixin.com/ekopras18', 'Title disini', 'asdsadasdas ue, ridiculus nascetur odio ridiculus? Hac ac, adipiscing ut dapibus. Adipiscing cras in? Magna nisi augue odio! Pellentesque magnis? Lacus integer magnis\r\n              purus sed mus lorem aliquam lectus, placerat pellentesque quis, nunc urna turpis lorem. Etiam velit, augue sed magnis placerat! In cras, dignissim lorem, porttitor in velit in, nisi vut a cursus cum, odio sagittis nisi turpis? Mus penatibus\r\n              non, pulvinar porttitor arcu hac ut', 'asdasdadasd rient velit non tincidunt sit sagittis pulvinar phasellus rhoncus hac! Sit porta. Tristique, hac. Porttitor\r\n              adipiscing ac. Ac tincidunt a porttitor natoque auctor ultricies! Proin nunc scelerisque? Habitass', 'project2.png');

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(100) NOT NULL,
  `body` text NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`id`, `title`, `author`, `body`, `create_date`) VALUES
(18, 'Starter template', 'admin', '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Be sure to have your pages set up with the latest design and development standards. That means using an HTML5 doctype and including a viewport meta tag for proper responsive behaviors. Put it all together and your pages should look like this:</p><p>&nbsp;</p><p>&lt;!doctype html&gt; &lt;html lang=&quot;en&quot;&gt; &lt;head&gt; &lt;!-- Required meta tags --&gt; &lt;meta charset=&quot;utf-8&quot;&gt; &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1, shrink-to-fit=no&quot;&gt; &lt;!-- Bootstrap CSS --&gt; &lt;link rel=&quot;stylesheet&quot; href=&quot;https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css&quot; integrity=&quot;sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS&quot; crossorigin=&quot;anonymous&quot;&gt; &lt;title&gt;Hello, world!&lt;/title&gt; &lt;/head&gt; &lt;body&gt; &lt;h1&gt;Hello, world!&lt;/h1&gt; &lt;!-- Optional JavaScript --&gt; &lt;!-- jQuery first, then Popper.js, then Bootstrap JS --&gt; &lt;script src=&quot;https://code.jquery.com/jquery-3.3.1.slim.min.js&quot; integrity=&quot;sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo&quot; crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt; &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js&quot; integrity=&quot;sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut&quot; crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt; &lt;script src=&quot;https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js&quot; integrity=&quot;sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k&quot; crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt; &lt;/body&gt; &lt;/html&gt;</p>', '2019-01-10 10:34:06'),
(19, 'Review Iphone X - Indonesia', 'admin', '<p>testes tes</p>', '2019-01-11 14:07:54'),
(20, 'What Makes Us Tick!', 'admin', '<p>&nbsp;</p><p>Elit pellentesque dolor facilisis aenean eu</p>', '2019-01-11 14:08:21'),
(21, 'zzz', 'admin', '<p>sdsdsds</p>', '2019-01-11 18:43:39'),
(22, 'asasasasa', 'admin', '<p>aaaaaa</p>', '2019-01-11 18:44:04'),
(23, 'Your Article!', 'admin', '<p>zxZXYour Article!Your Article!Your Article!Your Article!Your Article!Your Article!Your Article!Your Article!Your Article!Your Article!</p>', '2019-01-11 18:49:30'),
(24, 'Update ios 11.4.1', 'admin', '<p>sadasdasdasdasd</p>', '2019-01-13 05:01:10'),
(25, 'Flask URL Converters', 'admin', '<p>Eko Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p><p>Welcome to part 28 of our Flask web development tutorial series. In this tutorial, we&#39;re going to be discussing custom&nbsp;<a target=\"blank\" href=\"https://exploreflask.com/views.html#url-converters\"><strong>converters</strong></a>. The idea of these custom converters is to allow us to create very dynamic URLs, where part of the URL is actually treated as a variable.</p><p>An example of where this may prove useful might be where you have something with pagination, or maybe a user account page. Another example would be with PythonProgramming.net&#39;s development version content management system, where we have lots of pages that are almost identical, where the only main difference in the function itself is the URL and the template that is rendered, along with some minor variable changes along the way. Let&#39;s start with a simple example of a converter:</p>', '2019-01-16 14:35:39'),
(26, '我的新闻', 'admin', '<p>就是德国；科技时代不时地是的就是德国；科技时代不时地是的就是德国；科技时代不时地是的就是德国；科技时代不时地是的就是德国；科技时代不时地是的就是德国；科技时代不时地是的</p>', '2019-02-09 05:24:38'),
(27, 'Samsung Galaxy S10+ ', 'admin', '<p>Punch out a hole in the display, add an extra camera on the back, do the mandatory yearly updates to the internals and you&#39;d end up with a Samsung Galaxy S10+ - that is, if you started out with an S9+ if it wasn&#39;t obvious. Only that would be oversimplifying it, and we&#39;d rather explore the nuances. Let&#39;s go ahead and get started on our journey to find out how big of an upgrade the tenth edition of Samsung&#39;s Galaxy S is.</p><p>Now, just because we opened so bluntly, doesn&#39;t mean all of that isn&#39;t true - there is, indeed, a hole in the display, but it&#39;s one gorgeous AMOLED panel that covers almost the entirety of the phone, plus the hole is not simply a hole but an all-new 4K-capable dual pixel selfie cam.</p><p>Also true, there&#39;s a third camera on the back of the S10+ and S10, the missing ultra wide angle piece of the S9+&#39;s camera puzzle, completing what is in our minds the smartphone camera trifecta. At least for now?</p><p><a href=\"https://cdn.gsmarena.com/imgroot/reviews/19/samsung-galaxy-s10-plus/lifestyle/-728w2/gsmarena_025.jpg\" onclick=\"window.open(this.href, \'ViewImage\', \'resizable=no,status=no,location=no,toolbar=no,menubar=no,fullscreen=no,scrollbars=no,dependent=no\'); return false;\">View Image</a></p><p>&nbsp;</p>', '2019-03-04 11:09:28');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id_cart` int(11) NOT NULL,
  `id_phone` int(11) NOT NULL,
  `id_users` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`id_cart`, `id_phone`, `id_users`, `date`) VALUES
(1, 27, 3, '2019-03-08 11:18:53'),
(5, 1, 11, '2019-03-08 14:09:00'),
(6, 1, 11, '2019-03-08 14:09:06'),
(7, 1, 2, '2019-03-08 14:12:05');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id_orders` int(11) NOT NULL,
  `id_users` int(11) NOT NULL,
  `id_phone` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `price` int(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `orders_receipt`
--

CREATE TABLE `orders_receipt` (
  `id_receipt` int(11) NOT NULL,
  `id_orders` int(11) NOT NULL,
  `id_users` int(11) NOT NULL,
  `id_phone` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `price` int(50) NOT NULL,
  `status` varchar(25) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders_receipt`
--

INSERT INTO `orders_receipt` (`id_receipt`, `id_orders`, `id_users`, `id_phone`, `username`, `phone`, `price`, `status`, `date`) VALUES
(18, 7, 6, 20, 'eko prasetio', 'Iphone Xs Max', 11000, 'confirm', '2019-03-05 17:26:52'),
(19, 10, 6, 25, 'eko prasetio', 'Iphone 7 Plus', 5898, 'confirm', '2019-03-05 17:26:52'),
(21, 8, 2, 19, 'ekopras', 'Xiaomi mi8', 4800, 'confirm', '2019-03-07 15:06:28'),
(22, 9, 8, 21, 'xxxxxx', 'Iphone Xs', 9800, 'confirm', '2019-03-08 11:44:40'),
(23, 12, 6, 12, 'eko prasetio', 'Samsung Galaxy S8', 5678, 'confirm', '2019-03-07 15:25:37'),
(24, 11, 3, 22, 'safi', 'Iphone XR', 5005, 'confirm', '2019-03-08 11:08:55'),
(25, 14, 2, 27, 'ekopras', 'Samsung Galaxy S10 5G', 10889, 'confirm', '2019-03-07 16:45:32'),
(26, 15, 2, 27, 'ekopras', 'Samsung Galaxy S10 5G', 10889, 'confirm', '2019-03-07 16:45:32'),
(27, 16, 2, 12, 'ekopras', 'Samsung Galaxy S8', 5678, 'confirm', '2019-03-07 16:45:32'),
(28, 17, 2, 21, 'ekopras', 'Iphone Xs', 9800, 'confirm', '2019-03-07 16:45:32'),
(29, 18, 2, 20, 'ekopras', 'Iphone Xs Max', 11000, 'confirm', '2019-03-07 16:45:32'),
(30, 9, 8, 21, 'xxxxxx', 'Iphone Xs', 9800, 'confirm', '2019-03-08 11:44:40'),
(31, 22, 8, 27, 'xxxxxx', 'Samsung Galaxy S10 5G', 10889, 'confirm', '2019-03-08 11:44:40'),
(33, 23, 8, 26, 'xxxxxx', 'Iphone 7', 4788, 'confirm', '2019-03-08 12:05:48'),
(34, 24, 8, 18, 'xxxxxx', 'Sony Experia XZ3', 7900, 'confirm', '2019-03-08 12:05:48');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id_pay` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `methods` varchar(10) NOT NULL,
  `id_users` int(11) NOT NULL,
  `id_phone` int(11) NOT NULL,
  `total` int(50) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id_pay`, `username`, `methods`, `id_users`, `id_phone`, `total`, `date`) VALUES
(1, 'eko prasetio', 'Alipay', 6, 12, 5678, '2019-03-07 16:03:12'),
(2, 'ekopras', 'Alipay', 2, 23, 5880, '2019-03-07 16:03:17'),
(3, 'ekopras', 'Alipay', 2, 27, 10889, '2019-03-07 16:00:35'),
(4, 'ekopras', 'Alipay', 2, 27, 26367, '2019-03-07 16:01:52'),
(5, 'ekopras', 'Weixin', 2, 20, 21889, '2019-03-07 16:25:01'),
(6, 'safi', 'Weixin', 3, 27, 10889, '2019-03-07 16:54:47'),
(7, 'xxxxxx', 'Alipay', 8, 27, 10889, '2019-03-08 11:22:14'),
(8, 'xxxxxx', 'Weixin', 8, 26, 4788, '2019-03-08 11:46:17'),
(9, 'xxxxxx', 'Weixin', 8, 18, 7900, '2019-03-08 12:01:43');

-- --------------------------------------------------------

--
-- Table structure for table `product_phone`
--

CREATE TABLE `product_phone` (
  `id_phone` int(20) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `available` int(5) NOT NULL,
  `price` int(50) NOT NULL,
  `description` text NOT NULL,
  `picture` text CHARACTER SET latin1 NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_phone`
--

INSERT INTO `product_phone` (`id_phone`, `brand`, `phone`, `available`, `price`, `description`, `picture`, `time`) VALUES
(1, 'Appel', 'Iphone X', 9, 8888, 'the best product the best productthe best productthe best productthe best productthe best productthe best productthe best product', 'apple-iphone-x.jpg', '2019-02-09 15:10:39'),
(12, 'Samsung', 'Samsung Galaxy S8', 4, 5678, 'image/product', 'samsung-galaxy-s8.jpg', '2019-02-09 15:45:04'),
(18, 'Sony', 'Sony Experia XZ3', 4, 7900, 'qedasdasd', 'sony-xperia-xz3-.jpg', '2019-02-12 10:20:23'),
(19, 'Xiaomi', 'Xiaomi mi8', 4, 4800, 'Xiaomi bagus loh', 'xiaomi-mi8.jpg', '2019-02-17 14:25:11'),
(20, 'Appel', 'Iphone Xs Max', 6, 11000, 'hgd,hcgchgc', 'apple-iphone-xs-max.jpg', '2019-02-17 14:35:10'),
(21, 'Appel', 'Iphone Xs', 9, 9800, 'hgcgcjhcgh', 'apple-iphone-xs.jpg', '2019-02-17 15:06:02'),
(22, 'Appel', 'Iphone XR', 9, 5005, 'jfkhvhgvjhg', 'apple-iphone-xr.jpg', '2019-02-17 15:07:30'),
(23, 'Appel', 'Iphone 8 Plus', 4, 5880, 'Iphone 8 Plus cakep', 'apple-iphone-8-plus.jpg', '2019-02-18 15:32:09'),
(24, 'Appel', 'Iphone 8', 3, 4788, 'khgckhgcygkcvgh', 'apple-iphone-8.jpg', '2019-02-18 15:37:10'),
(25, 'Appel', 'Iphone 7 Plus', 6, 5898, 'ckhggckgh hkghg', 'apple-iphone-7-plus.jpg', '2019-02-18 15:41:58'),
(26, 'Appel', 'Iphone 7', 7, 4788, 'kjbkkbjkj', 'apple-iphone-7.jpg', '2019-02-18 15:43:47'),
(27, 'Samsung', 'Samsung Galaxy S10 5G', 5, 10889, 'Samsung galaxy S10 5g', 'samsung-galaxy-s10-5g.jpg', '2019-03-05 10:02:49');

-- --------------------------------------------------------

--
-- Table structure for table `product_phone_level`
--

CREATE TABLE `product_phone_level` (
  `id_level` int(10) NOT NULL,
  `id_phone` int(11) NOT NULL,
  `colors` varchar(50) NOT NULL,
  `camera` int(11) NOT NULL,
  `internal` varchar(50) NOT NULL,
  `network` varchar(50) NOT NULL,
  `battery` int(20) NOT NULL,
  `announced` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `dimensions` varchar(50) NOT NULL,
  `weight` varchar(10) NOT NULL,
  `size` varchar(10) NOT NULL,
  `resolution` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_phone_level`
--

INSERT INTO `product_phone_level` (`id_level`, `id_phone`, `colors`, `camera`, `internal`, `network`, `battery`, `announced`, `status`, `dimensions`, `weight`, `size`, `resolution`) VALUES
(1, 1, 'Black,Silver', 12, '256-3', '5G/4G LTE', 2716, '2017-10-24', 'Discontinued', '143.9 x 70.9 x 4.4', '174', '5.8', '1125 x 2436'),
(12, 12, 'Black', 12, '256-3', '5G/4G LTE', 3500, '2018-11-07', 'Discontinued', '143.9 x 70.9 x 4.4', '123', '6', '1125 x 2436'),
(18, 18, 'Black', 12, '64-6', '5G/4G LTE', 3500, '2019-02-12', 'Available', '143.9 x 70.9 x 4.4', '123', '5.8', '1125 x 2436'),
(19, 19, 'Blue,Black', 13, '64-6', '5G/4G LTE', 3500, '2019-02-17', 'Available', '143.9 x 70.9 x 4.4', '137', '5.8', '1125 x 2436'),
(20, 20, 'Black,Silver,white', 12, '256-4', '5G/4G LTE', 3500, '2018-12-05', 'Available', '143.9 x 70.9 x 4.4', '149', '6', '1125 x 2436'),
(21, 21, 'Black', 12, '256-3', '5G/4G LTE', 3500, '2019-02-17', 'Available', '143.9 x 70.9 x 4.4', '123', '5.8', '1125 x 2436'),
(22, 22, 'Black', 12, '256-3', '5G/4G LTE', 2716, '2018-10-19', 'Available', '143.9 x 70.9 x 4.4', '132', '5.8', '1125 x 2436'),
(23, 23, 'Black,Silver,white', 12, '64/256-3', '5G/4G LTE', 2691, '2018-06-07', 'Discontinued', '158.4 x 78.1 x 7.5', '202', '5.5', '1080 x 1920'),
(24, 24, 'Black,Silver', 12, '64-3', '5G/4G LTE', 1821, '2018-02-08', 'Discontinued', '138.4 x 67.3 x 7.3', '148', '4.7', '750x1334'),
(25, 25, 'Black', 12, '32/128/256-3', '5G/4G LTE', 2900, '2017-06-01', 'Discontinued', '158.2 x 77.9 x 7.3', '188', '5.5', '1080 x 1920'),
(26, 26, 'Black', 12, '32/128-3', '5G/4G LTE', 3567, '2017-06-10', 'Discontinued', '138.4 x 67.3 x 7.3', '177', '4.7', '750x1334'),
(27, 27, 'blue,black', 16, '256-8', '5G/4G', 4500, '2019-02-18', 'Available', '162.6 x 77.1 x 7.9', '198', '6.7', '1440x3040');

-- --------------------------------------------------------

--
-- Table structure for table `product_phone_view`
--

CREATE TABLE `product_phone_view` (
  `id` int(20) NOT NULL,
  `user_id` int(20) NOT NULL,
  `product_id_phone` int(20) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_phone_view`
--

INSERT INTO `product_phone_view` (`id`, `user_id`, `product_id_phone`, `date`) VALUES
(1, 1, 20, '2019-02-17 14:35:25'),
(2, 1, 18, '2019-02-17 14:35:39'),
(3, 1, 12, '2019-02-17 14:35:54'),
(4, 1, 21, '2019-02-17 15:07:44'),
(5, 1, 22, '2019-02-17 15:08:44'),
(6, 1, 1, '2019-02-17 15:33:14'),
(7, 2, 22, '2019-02-17 15:36:57'),
(8, 2, 19, '2019-02-17 15:37:05'),
(9, 2, 18, '2019-02-17 15:43:26'),
(10, 2, 1, '2019-02-18 07:13:01'),
(11, 2, 20, '2019-02-18 07:13:07'),
(12, 2, 21, '2019-02-18 07:13:37'),
(13, 2, 12, '2019-02-18 09:57:47'),
(14, 1, 23, '2019-02-18 15:32:23'),
(15, 1, 24, '2019-02-18 15:37:18'),
(16, 3, 24, '2019-02-20 17:14:26'),
(17, 2, 26, '2019-02-23 11:33:24'),
(18, 2, 25, '2019-02-24 07:47:52'),
(19, 8, 19, '2019-03-01 08:41:44'),
(20, 2, 24, '2019-03-03 10:58:46'),
(21, 6, 26, '2019-03-03 10:59:20'),
(22, 6, 24, '2019-03-03 10:59:35'),
(23, 6, 1, '2019-03-03 11:00:05'),
(24, 6, 25, '2019-03-03 11:05:00'),
(25, 6, 23, '2019-03-03 15:00:21'),
(26, 1, 25, '2019-03-04 14:39:53'),
(27, 1, 26, '2019-03-04 14:42:07'),
(28, 1, 19, '2019-03-04 17:09:05'),
(29, 1, 27, '2019-03-05 10:05:27'),
(30, 2, 27, '2019-03-05 10:58:50'),
(31, 8, 24, '2019-03-08 11:21:07');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(5) NOT NULL,
  `type` tinyint(1) NOT NULL,
  `username` varchar(50) NOT NULL,
  `consignee` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phonenumber` varchar(20) NOT NULL,
  `provinces` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `region` varchar(200) NOT NULL,
  `street` varchar(200) NOT NULL,
  `d_address` varchar(225) NOT NULL,
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `type`, `username`, `consignee`, `email`, `password`, `phonenumber`, `provinces`, `city`, `region`, `street`, `d_address`, `register_date`) VALUES
(1, 1, 'admin', '', 'ekoxit1@gmail.com', '$5$rounds=535000$HOADhdvEhU/nXZA3$X.Ul1oYCQyWFJHB3xP7jl9bhc9bLujTMrtCZhvjgNuB', '15678903347', '', '', '', '', '', '2019-03-06 17:53:44'),
(2, 0, 'ekopras', 'Eko Prasetio', 'ekopras@gmail.com', '$5$rounds=535000$Oq32cHuewkIGxgGg$GNrJz66q85hOWO/gRfAed0Do8VU.WQJBei4d4745Yw/', '15678903347', '广西', '南宁市', '西乡塘区', '西乡塘街道', '西乡塘区 西乡塘街道 广西民族大学4坡13栋', '2019-03-04 16:41:51'),
(3, 0, 'safi', 'Safi', 'safi@gmail.com', '$5$rounds=535000$NU1QoaSFCOw.JGMR$3mxwEn0/3yjCtHj5XsLPYyEb15QN9aQGLS1us29Che9', '1243638849', 'Gahag', 'Hshss', 'Gagsh', 'Hshs', 'Gshshd', '2019-03-05 13:11:01'),
(5, 0, 'mrekopras', '', 'mre_pras@programmer.net', '$5$rounds=535000$cgRpdWKsKG3550WU$sshQfvCm3ew8ldppBOV3LXQsY0hK0DwxxIrjNyxthH.', '', '', '', '', '', '', '2019-01-31 09:33:05'),
(6, 0, 'eko prasetio', 'Eko Pras', 'test@gmail.com', '$5$rounds=535000$t2PFdQexCjeuoNRB$DFV4Gqoo49aR9MiuJtt/yrdGTg1.oULCC96BI3EjOv8', '12344566778', '广西', '桂林', '唐山区', '唐山小区', '广西师范大学7坡12栋', '2019-02-25 16:26:49'),
(8, 0, 'xxxxxx', 'xxxxxx', 'xxx@xxx.xxx', '$5$rounds=535000$T95QDkOVDAKSpGhM$9lhHnOdCbVUg0DHny.znTlX/F74VMXxhuvSGRx3fsWD', '087647444444', '广西', '南宁市', '西乡塘区', '西乡塘街道', '32432423423442343242', '2019-02-28 09:59:04'),
(11, 1, 'mrestore', '', 'admin@mrestore.com', '$5$rounds=535000$LPspiqI10fiPGuZ7$sFTazeng5cyZl3JgbkHXXdMpcjXOFcTHFYff5Lqq2j0', '15678903347', '', '', '', '', '', '2019-03-07 04:53:13');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_address`
--
ALTER TABLE `admin_address`
  ADD PRIMARY KEY (`id_aa`);

--
-- Indexes for table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id_cart`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id_orders`);

--
-- Indexes for table `orders_receipt`
--
ALTER TABLE `orders_receipt`
  ADD PRIMARY KEY (`id_receipt`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id_pay`);

--
-- Indexes for table `product_phone`
--
ALTER TABLE `product_phone`
  ADD PRIMARY KEY (`id_phone`);

--
-- Indexes for table `product_phone_level`
--
ALTER TABLE `product_phone_level`
  ADD PRIMARY KEY (`id_level`),
  ADD UNIQUE KEY `id_phone` (`id_phone`);

--
-- Indexes for table `product_phone_view`
--
ALTER TABLE `product_phone_view`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_address`
--
ALTER TABLE `admin_address`
  MODIFY `id_aa` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id_cart` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id_orders` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `orders_receipt`
--
ALTER TABLE `orders_receipt`
  MODIFY `id_receipt` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id_pay` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `product_phone`
--
ALTER TABLE `product_phone`
  MODIFY `id_phone` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `product_phone_view`
--
ALTER TABLE `product_phone_view`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `product_phone_level`
--
ALTER TABLE `product_phone_level`
  ADD CONSTRAINT `product_phone_level_ibfk_1` FOREIGN KEY (`id_phone`) REFERENCES `product_phone` (`id_phone`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
