# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:57:06 2024

@author: Ethan Hu
"""


import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
#path = 'SV.JPEG'
#path = 'IMG_0303.CR2'
path = 'Oct13D1.JPEG'
#plt.close('all')
plt.figure()
import PIL.Image as image
im =image.open(path)
drop=np.array(im) #Converts data into array
plt.imshow(drop)

apointx = [1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1698, 1699, 1699, 1699, 1699, 1699, 1699, 1699, 1699, 1699, 1699, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1700, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1701, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1702, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1703, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1704, 1705, 1705, 1705, 1705, 1705, 1705, 1705, 1705, 1705, 1705, 1705, 1705, 1705, 1706, 1706, 1706, 1706, 1706, 1706, 1706, 1706, 1706, 1706, 1706, 1706, 1706, 1707, 1707, 1707, 1707, 1707, 1707, 1707, 1707, 1707, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1708, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1709, 1710, 1710, 1710, 1710, 1710, 1710, 1710, 1710, 1710, 1710, 1710, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1711, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1713, 1713, 1713, 1713, 1713, 1713, 1713, 1713, 1713, 1713, 1713, 1713, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1714, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1715, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1716, 1717, 1717, 1717, 1717, 1717, 1717, 1717, 1717, 1717, 1717, 1717, 1717, 1717, 1718, 1718, 1718, 1718, 1718, 1718, 1718, 1718, 1718, 1718, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1719, 1720, 1720, 1720, 1720, 1720, 1720, 1720, 1720, 1720, 1720, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1721, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1722, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1723, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1724, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1725, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1726, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1727, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1728, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1729, 1730, 1730, 1730, 1730, 1730, 1730, 1730, 1730, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1731, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1732, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1733, 1734, 1734, 1734, 1734, 1734, 1734, 1734, 1734, 1734, 1734, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1735, 1736, 1736, 1736, 1736, 1736, 1736, 1736, 1736, 1736, 1736, 1736, 1736, 1736, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1737, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1738, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1739, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1740, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1741, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1742, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1743, 1744, 1744, 1744, 1744, 1744, 1744, 1744, 1744, 1744, 1744, 1744, 1745, 1745, 1745, 1745, 1745, 1745, 1745, 1745, 1745, 1745, 1745, 1745, 1745, 1746, 1746, 1746, 1746, 1746, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1747, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1748, 1749, 1749, 1749, 1749, 1749, 1749, 1749, 1749, 1749, 1749, 1749, 1750, 1750, 1750, 1750, 1750, 1750, 1750, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1751, 1752, 1752, 1752, 1752, 1752, 1752, 1752, 1752, 1752, 1752, 1752, 1752, 1752, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1753, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1754, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1755, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1756, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1757, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1758, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1759, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1760, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1761, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1762, 1763, 1763, 1763, 1763, 1763, 1763, 1763, 1763, 1763, 1763, 1763, 1763, 1764, 1764, 1764, 1764, 1764, 1764, 1764, 1764, 1764, 1764, 1764, 1764, 1764, 1765, 1765, 1765, 1765, 1765, 1765, 1765, 1765, 1765, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1766, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1767, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1769, 1770, 1770, 1770, 1770, 1770, 1770, 1770, 1770, 1770, 1770, 1770, 1770, 1770, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1771, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1772, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1773, 1774, 1774, 1774, 1774, 1774, 1774, 1774, 1774, 1774, 1774, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1775, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1776, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1777, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1778, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1779, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1780, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1781, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1782, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1783, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1784, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1785, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1786, 1787, 1787, 1787, 1787, 1787, 1787, 1787, 1787, 1787, 1788, 1788, 1788, 1788, 1788, 1788, 1788, 1788, 1788, 1789, 1789, 1789, 1789, 1789, 1789, 1789, 1789, 1790, 1790, 1790, 1790, 1790, 1791, 1791, 1791, 1791, 1791, 1791, 1792, 1792, 1792, 1792, 1793, 1793, 1793, 1794, 1794, 1794, 1794, 1794, 1794, 1795, 1795, 1795, 1795, 1795, 1796, 1797, 1797, 1797, 1797, 1797, 1797, 1798, 1798, 1798, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1799, 1800, 1800, 1800, 1800, 1800, 1800, 1801, 1801, 1801, 1801, 1801, 1802, 1802, 1802, 1802, 1802, 1802, 1802, 1802, 1802, 1803, 1803, 1803, 1803, 1803, 1803, 1803, 1803, 1803, 1803, 1804, 1804, 1804, 1804, 1804, 1804, 1804, 1805, 1805, 1805, 1805, 1805, 1805, 1805, 1805, 1806, 1806, 1806, 1806, 1807, 1807, 1807, 1807, 1807, 1807, 1807, 1807, 1807, 1807, 1809, 1809, 1809, 1810, 1810, 1810, 1810, 1810, 1811, 1811, 1811, 1812, 1812, 1812, 1812, 1813, 1813, 1814, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1815, 1816, 1816, 1816, 1816, 1816, 1816, 1817, 1817, 1817, 1817, 1817, 1817, 1818, 1818, 1818, 1818, 1819, 1819, 1819, 1819, 1819, 1819, 1819, 1819, 1819, 1819, 1820, 1820, 1820, 1820, 1820, 1820, 1821, 1821, 1821, 1821, 1821, 1821, 1821, 1821, 1821, 1821, 1822, 1822, 1822, 1822, 1822, 1822, 1822, 1823, 1823, 1823, 1823, 1824, 1824, 1824, 1824, 1824, 1825, 1825, 1825, 1825, 1825, 1825, 1825, 1826, 1826, 1828, 1828, 1828, 1828, 1829, 1829, 1830, 1830, 1830, 1830, 1830, 1830, 1830, 1830, 1830, 1831, 1831, 1831, 1831, 1831, 1831, 1831, 1831, 1831, 1831, 1831, 1831, 1832, 1832, 1833, 1833, 1833, 1833, 1834, 1834, 1834, 1834, 1834, 1834, 1835, 1835, 1835, 1835, 1835, 1835, 1836, 1836, 1836, 1836, 1836, 1836, 1836, 1836, 1836, 1837, 1837, 1837, 1837, 1837, 1837, 1837, 1838, 1838, 1838, 1838, 1838, 1838, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1839, 1840, 1840, 1840, 1840, 1840, 1840, 1840, 1840, 1840, 1840, 1840, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1841, 1842, 1842, 1842, 1842, 1842, 1843, 1843, 1843, 1843, 1843, 1843, 1843, 1843, 1843, 1843, 1844, 1844, 1844, 1844, 1844, 1844, 1844, 1844, 1844, 1844, 1844, 1845, 1845, 1845, 1845, 1845, 1845, 1845, 1845, 1845, 1845, 1845, 1846, 1846, 1846, 1846, 1846, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1847, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1848, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1849, 1850, 1850, 1850, 1850, 1850, 1850, 1850, 1850, 1850, 1851, 1851, 1851, 1851, 1851, 1851, 1851, 1851, 1852, 1852, 1852, 1852, 1852, 1852, 1853, 1853, 1853, 1853, 1853, 1853, 1853, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1854, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1855, 1856, 1856, 1856, 1856, 1856, 1856, 1857, 1857, 1857, 1857, 1857, 1857, 1857, 1857, 1858, 1858, 1858, 1858, 1858, 1858, 1858, 1858, 1859, 1859, 1859, 1859, 1859, 1859, 1859, 1859, 1859, 1859, 1859, 1860, 1860, 1860, 1860, 1860, 1860, 1860, 1860, 1860, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1861, 1862, 1862, 1862, 1862, 1862, 1862, 1862, 1862, 1862, 1862, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1863, 1864, 1864, 1864, 1864, 1865, 1865, 1865, 1865, 1866, 1866, 1866, 1866, 1866, 1867, 1867, 1867, 1867, 1868, 1868, 1868, 1868, 1868, 1868, 1869, 1869, 1869, 1869, 1869, 1869, 1869, 1870, 1870, 1870, 1870, 1870, 1870, 1870, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1871, 1872, 1872, 1872, 1873, 1873, 1873, 1873, 1873, 1873, 1873, 1873, 1874, 1874, 1874, 1874, 1874, 1875, 1875, 1876, 1876, 1876, 1876, 1877, 1877, 1877, 1877, 1877, 1878, 1878, 1879, 1879, 1879, 1879, 1879, 1879, 1879, 1879, 1879, 1879, 1879, 1879, 1879, 1880, 1880, 1880, 1880, 1880, 1880, 1881, 1881, 1881, 1881, 1881, 1881, 1881, 1881, 1881, 1881, 1882, 1882, 1882, 1883, 1883, 1883, 1883, 1883, 1884, 1884, 1884, 1884, 1884, 1884, 1885, 1885, 1885, 1885, 1885, 1885, 1885, 1885, 1885, 1885, 1886, 1886, 1886, 1886, 1886, 1886, 1886, 1886, 1886, 1886, 1886, 1886, 1887, 1887, 1887, 1887, 1887, 1887, 1887, 1888, 1888, 1888, 1889, 1889, 1889, 1889, 1889, 1889, 1889, 1890, 1890, 1890, 1890, 1890, 1890, 1890, 1890, 1890, 1890, 1891, 1891, 1891, 1891, 1891, 1891, 1891, 1891, 1891, 1891, 1891, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1892, 1893, 1893, 1893, 1893, 1893, 1893, 1893, 1893, 1893, 1893, 1894, 1894, 1894, 1894, 1894, 1894, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1895, 1896, 1896, 1896, 1896, 1896, 1896, 1896, 1896, 1896, 1896, 1897, 1897, 1897, 1897, 1897, 1897, 1897, 1897, 1897, 1897, 1898, 1898, 1898, 1898, 1898, 1898, 1898, 1899, 1899, 1899, 1899, 1899, 1899, 1899, 1899, 1899, 1899, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1900, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1901, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1902, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1903, 1904, 1904, 1904, 1904, 1904, 1904, 1904, 1904, 1904, 1904, 1904, 1904, 1905, 1905, 1905, 1905, 1905, 1905, 1905, 1905, 1905, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1906, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1907, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1908, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1909, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1910, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1911, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912, 1912]
apointy = [1101, 1110, 1111, 1112, 1113, 1120, 1121, 1122, 1123, 1125, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1112, 1113, 1119, 1126, 1127, 1129, 1130, 1131, 1135, 1138, 1101, 1111, 1119, 1131, 1134, 1135, 1138, 1140, 1097, 1100, 1101, 1102, 1104, 1110, 1111, 1112, 1113, 1117, 1118, 1119, 1120, 1124, 1125, 1126, 1130, 1131, 1141, 1101, 1104, 1110, 1111, 1112, 1113, 1117, 1118, 1120, 1121, 1124, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1137, 1101, 1106, 1107, 1108, 1109, 1110, 1111, 1116, 1117, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1128, 1129, 1133, 1135, 1136, 1137, 1138, 1140, 1141, 1142, 1104, 1111, 1120, 1123, 1124, 1127, 1129, 1130, 1131, 1133, 1134, 1136, 1137, 1138, 1144, 1104, 1113, 1122, 1123, 1124, 1126, 1127, 1129, 1130, 1133, 1135, 1141, 1143, 1118, 1120, 1121, 1122, 1123, 1128, 1129, 1130, 1131, 1142, 1143, 1145, 1146, 1120, 1121, 1122, 1123, 1128, 1129, 1130, 1131, 1143, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1136, 1137, 1142, 1144, 1145, 1147, 1151, 1118, 1119, 1122, 1123, 1124, 1125, 1126, 1127, 1132, 1133, 1136, 1137, 1141, 1148, 1119, 1123, 1124, 1125, 1126, 1127, 1132, 1133, 1143, 1144, 1147, 1112, 1115, 1117, 1118, 1119, 1121, 1127, 1128, 1133, 1134, 1135, 1136, 1137, 1138, 1140, 1143, 1144, 1145, 1146, 1151, 1154, 1155, 1123, 1127, 1131, 1132, 1140, 1141, 1142, 1150, 1151, 1153, 1154, 1155, 1121, 1122, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1140, 1141, 1143, 1116, 1118, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1145, 1147, 1156, 1157, 1158, 1159, 1122, 1123, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1144, 1145, 1146, 1147, 1150, 1151, 1157, 1121, 1122, 1123, 1125, 1129, 1130, 1133, 1134, 1135, 1136, 1144, 1145, 1150, 1151, 1155, 1122, 1125, 1126, 1134, 1135, 1136, 1137, 1138, 1139, 1145, 1146, 1147, 1148, 1122, 1125, 1131, 1132, 1135, 1136, 1144, 1145, 1146, 1147, 1124, 1125, 1140, 1141, 1142, 1145, 1146, 1149, 1150, 1152, 1156, 1157, 1160, 1161, 1162, 1123, 1124, 1127, 1136, 1137, 1142, 1143, 1147, 1157, 1166, 1125, 1136, 1137, 1138, 1143, 1145, 1146, 1147, 1148, 1149, 1152, 1162, 1163, 1164, 1126, 1127, 1138, 1141, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1155, 1156, 1157, 1165, 1166, 1167, 1127, 1128, 1136, 1144, 1145, 1146, 1147, 1154, 1155, 1161, 1162, 1163, 1164, 1165, 1128, 1129, 1130, 1131, 1132, 1133, 1141, 1142, 1143, 1144, 1145, 1146, 1154, 1155, 1157, 1158, 1159, 1163, 1167, 1168, 1170, 1171, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1150, 1151, 1152, 1153, 1154, 1162, 1167, 1168, 1169, 1172, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1142, 1143, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1160, 1161, 1162, 1163, 1164, 1166, 1140, 1141, 1142, 1143, 1148, 1149, 1150, 1151, 1153, 1154, 1155, 1156, 1160, 1163, 1164, 1165, 1166, 1167, 1169, 1170, 1137, 1138, 1140, 1141, 1145, 1146, 1148, 1151, 1152, 1153, 1154, 1155, 1168, 1169, 1170, 1173, 1174, 1175, 1135, 1136, 1137, 1138, 1140, 1141, 1143, 1145, 1146, 1153, 1154, 1156, 1158, 1159, 1160, 1161, 1162, 1165, 1174, 1175, 1176, 1151, 1152, 1161, 1174, 1175, 1176, 1177, 1178, 1137, 1138, 1140, 1142, 1145, 1146, 1150, 1151, 1158, 1159, 1165, 1176, 1178, 1179, 1137, 1138, 1143, 1144, 1145, 1146, 1151, 1152, 1160, 1164, 1165, 1166, 1174, 1180, 1139, 1140, 1143, 1144, 1147, 1148, 1150, 1152, 1153, 1155, 1156, 1157, 1160, 1161, 1164, 1165, 1166, 1171, 1172, 1140, 1143, 1147, 1148, 1153, 1165, 1166, 1170, 1171, 1182, 1142, 1144, 1147, 1148, 1150, 1153, 1155, 1156, 1158, 1159, 1160, 1161, 1165, 1166, 1167, 1170, 1171, 1172, 1180, 1181, 1182, 1142, 1154, 1160, 1161, 1162, 1165, 1166, 1168, 1180, 1181, 1182, 1183, 1184, 1143, 1146, 1147, 1148, 1149, 1150, 1151, 1154, 1155, 1159, 1172, 1173, 1180, 1181, 1182, 1183, 1144, 1145, 1146, 1147, 1148, 1149, 1160, 1166, 1167, 1168, 1172, 1173, 1174, 1184, 1185, 1186, 1145, 1146, 1147, 1148, 1149, 1150, 1160, 1164, 1165, 1166, 1171, 1174, 1175, 1176, 1183, 1148, 1158, 1159, 1168, 1169, 1171, 1172, 1174, 1175, 1176, 1177, 1178, 1185, 1186, 1187, 1159, 1162, 1163, 1169, 1170, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1150, 1151, 1161, 1162, 1163, 1164, 1170, 1171, 1172, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1187, 1188, 1149, 1150, 1151, 1152, 1154, 1155, 1156, 1158, 1159, 1160, 1161, 1164, 1165, 1167, 1173, 1174, 1175, 1176, 1182, 1183, 1186, 1187, 1188, 1189, 1190, 1154, 1157, 1158, 1162, 1163, 1167, 1171, 1172, 1173, 1176, 1191, 1153, 1154, 1155, 1157, 1158, 1162, 1163, 1167, 1171, 1172, 1176, 1190, 1191, 1152, 1155, 1175, 1184, 1185, 1156, 1159, 1160, 1162, 1163, 1165, 1166, 1168, 1169, 1175, 1176, 1181, 1183, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1184, 1185, 1186, 1187, 1190, 1191, 1154, 1155, 1161, 1162, 1166, 1167, 1168, 1176, 1185, 1186, 1192, 1155, 1160, 1165, 1167, 1174, 1176, 1189, 1156, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1176, 1178, 1179, 1184, 1188, 1189, 1190, 1191, 1192, 1194, 1196, 1197, 1163, 1164, 1165, 1166, 1168, 1170, 1171, 1188, 1189, 1190, 1191, 1192, 1193, 1162, 1163, 1164, 1165, 1166, 1169, 1170, 1171, 1175, 1187, 1188, 1189, 1190, 1191, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1159, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1184, 1188, 1189, 1190, 1192, 1193, 1194, 1159, 1160, 1162, 1163, 1164, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1176, 1177, 1178, 1179, 1184, 1195, 1196, 1197, 1198, 1199, 1160, 1161, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1195, 1196, 1197, 1198, 1161, 1162, 1163, 1164, 1169, 1170, 1171, 1172, 1173, 1176, 1177, 1184, 1185, 1186, 1187, 1188, 1192, 1193, 1194, 1162, 1163, 1164, 1166, 1167, 1169, 1170, 1171, 1172, 1176, 1178, 1185, 1186, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1164, 1165, 1167, 1168, 1171, 1172, 1173, 1174, 1175, 1176, 1178, 1179, 1182, 1183, 1184, 1187, 1188, 1190, 1191, 1195, 1196, 1197, 1199, 1203, 1163, 1164, 1165, 1168, 1169, 1170, 1175, 1183, 1184, 1185, 1189, 1192, 1196, 1197, 1198, 1199, 1200, 1164, 1165, 1166, 1167, 1176, 1177, 1178, 1179, 1184, 1195, 1196, 1197, 1198, 1199, 1201, 1202, 1203, 1165, 1166, 1167, 1168, 1169, 1170, 1173, 1176, 1177, 1178, 1179, 1180, 1188, 1189, 1192, 1199, 1200, 1202, 1203, 1205, 1168, 1169, 1174, 1175, 1176, 1177, 1179, 1198, 1199, 1202, 1204, 1205, 1166, 1171, 1173, 1174, 1175, 1183, 1192, 1193, 1194, 1195, 1198, 1199, 1206, 1173, 1174, 1175, 1176, 1192, 1193, 1204, 1205, 1206, 1168, 1169, 1170, 1173, 1174, 1175, 1176, 1180, 1181, 1182, 1183, 1185, 1186, 1187, 1198, 1199, 1200, 1203, 1204, 1205, 1206, 1207, 1168, 1169, 1170, 1171, 1172, 1174, 1176, 1177, 1178, 1179, 1182, 1183, 1184, 1186, 1190, 1191, 1192, 1193, 1196, 1197, 1198, 1199, 1201, 1202, 1204, 1205, 1206, 1207, 1170, 1171, 1172, 1177, 1178, 1179, 1180, 1183, 1192, 1199, 1200, 1202, 1203, 1206, 1207, 1208, 1169, 1170, 1171, 1172, 1173, 1177, 1178, 1179, 1180, 1181, 1182, 1198, 1199, 1200, 1202, 1203, 1204, 1206, 1207, 1209, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1200, 1201, 1202, 1203, 1204, 1210, 1174, 1175, 1176, 1177, 1178, 1183, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1200, 1203, 1206, 1207, 1208, 1174, 1175, 1176, 1177, 1178, 1184, 1185, 1186, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1174, 1175, 1176, 1177, 1179, 1181, 1182, 1185, 1189, 1190, 1191, 1193, 1194, 1195, 1196, 1200, 1205, 1206, 1207, 1209, 1210, 1211, 1176, 1180, 1181, 1182, 1183, 1184, 1202, 1203, 1210, 1211, 1173, 1174, 1175, 1176, 1178, 1179, 1181, 1182, 1183, 1185, 1186, 1195, 1200, 1202, 1203, 1207, 1208, 1209, 1210, 1212, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1182, 1183, 1188, 1193, 1194, 1201, 1202, 1203, 1204, 1205, 1206, 1208, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1193, 1194, 1198, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1174, 1176, 1177, 1178, 1179, 1180, 1184, 1185, 1196, 1197, 1198, 1200, 1207, 1175, 1178, 1179, 1180, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1194, 1197, 1200, 1201, 1202, 1203, 1204, 1205, 1212, 1213, 1175, 1179, 1180, 1181, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1177, 1179, 1180, 1181, 1182, 1183, 1189, 1190, 1191, 1197, 1198, 1199, 1205, 1206, 1207, 1208, 1209, 1215, 1180, 1181, 1182, 1183, 1186, 1187, 1188, 1191, 1193, 1194, 1196, 1197, 1198, 1199, 1201, 1202, 1208, 1214, 1215, 1178, 1180, 1181, 1182, 1184, 1185, 1186, 1189, 1190, 1192, 1201, 1202, 1203, 1204, 1205, 1208, 1210, 1211, 1212, 1214, 1215, 1216, 1181, 1182, 1183, 1187, 1188, 1189, 1190, 1192, 1193, 1194, 1195, 1198, 1199, 1200, 1180, 1181, 1182, 1183, 1184, 1185, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1201, 1202, 1208, 1216, 1178, 1181, 1182, 1183, 1184, 1185, 1190, 1191, 1195, 1196, 1197, 1198, 1199, 1200, 1208, 1209, 1210, 1216, 1217, 1178, 1184, 1185, 1187, 1188, 1189, 1190, 1196, 1199, 1185, 1187, 1188, 1189, 1190, 1191, 1208, 1216, 1217, 1181, 1182, 1197, 1198, 1200, 1208, 1217, 1218, 1182, 1189, 1193, 1194, 1201, 1192, 1210, 1212, 1214, 1215, 1218, 1202, 1203, 1216, 1217, 1181, 1194, 1216, 1206, 1207, 1208, 1209, 1218, 1219, 1206, 1207, 1208, 1214, 1219, 1214, 1192, 1205, 1206, 1207, 1208, 1209, 1206, 1207, 1208, 1182, 1183, 1184, 1187, 1194, 1195, 1198, 1200, 1201, 1207, 1208, 1209, 1210, 1211, 1212, 1215, 1216, 1217, 1192, 1196, 1205, 1208, 1213, 1216, 1192, 1210, 1213, 1214, 1216, 1202, 1208, 1209, 1210, 1212, 1213, 1214, 1215, 1216, 1195, 1196, 1201, 1202, 1203, 1205, 1206, 1208, 1209, 1215, 1206, 1207, 1210, 1211, 1213, 1214, 1220, 1183, 1184, 1200, 1207, 1208, 1209, 1213, 1214, 1202, 1207, 1208, 1209, 1187, 1188, 1189, 1198, 1199, 1200, 1201, 1207, 1208, 1213, 1196, 1207, 1215, 1194, 1195, 1219, 1220, 1221, 1213, 1214, 1215, 1184, 1213, 1214, 1215, 1219, 1220, 1221, 1184, 1185, 1191, 1192, 1193, 1200, 1208, 1209, 1210, 1211, 1212, 1213, 1219, 1221, 1184, 1187, 1188, 1200, 1210, 1211, 1184, 1186, 1187, 1188, 1205, 1211, 1186, 1187, 1191, 1192, 1185, 1186, 1189, 1190, 1191, 1192, 1202, 1203, 1204, 1209, 1188, 1189, 1200, 1209, 1210, 1213, 1188, 1189, 1199, 1203, 1204, 1205, 1209, 1210, 1213, 1214, 1187, 1202, 1203, 1204, 1205, 1206, 1207, 1184, 1193, 1194, 1210, 1184, 1185, 1187, 1188, 1189, 1184, 1185, 1186, 1189, 1190, 1205, 1206, 1186, 1205, 1187, 1193, 1194, 1202, 1183, 1205, 1183, 1184, 1188, 1190, 1191, 1192, 1197, 1198, 1206, 1192, 1193, 1194, 1197, 1198, 1205, 1206, 1208, 1210, 1212, 1213, 1218, 1201, 1212, 1211, 1212, 1215, 1218, 1208, 1209, 1211, 1212, 1216, 1217, 1207, 1212, 1213, 1214, 1215, 1216, 1192, 1193, 1210, 1211, 1212, 1213, 1214, 1215, 1217, 1192, 1193, 1194, 1210, 1211, 1212, 1214, 1192, 1193, 1195, 1213, 1214, 1215, 1181, 1182, 1187, 1188, 1191, 1192, 1194, 1197, 1200, 1201, 1202, 1203, 1206, 1207, 1215, 1216, 1180, 1181, 1184, 1187, 1188, 1189, 1208, 1209, 1210, 1211, 1215, 1180, 1181, 1183, 1184, 1187, 1188, 1189, 1190, 1208, 1209, 1210, 1211, 1212, 1214, 1215, 1186, 1187, 1188, 1190, 1215, 1183, 1184, 1185, 1192, 1193, 1194, 1200, 1206, 1208, 1209, 1183, 1184, 1192, 1193, 1194, 1195, 1205, 1206, 1209, 1210, 1211, 1181, 1185, 1190, 1191, 1192, 1193, 1194, 1195, 1204, 1205, 1212, 1181, 1191, 1192, 1193, 1194, 1179, 1181, 1182, 1185, 1186, 1187, 1193, 1194, 1196, 1197, 1200, 1202, 1203, 1204, 1205, 1206, 1207, 1211, 1212, 1180, 1181, 1182, 1183, 1185, 1188, 1189, 1190, 1192, 1193, 1194, 1195, 1197, 1198, 1200, 1201, 1202, 1203, 1204, 1205, 1208, 1209, 1210, 1211, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1188, 1189, 1190, 1192, 1193, 1194, 1195, 1198, 1200, 1201, 1203, 1204, 1205, 1209, 1210, 1211, 1179, 1180, 1181, 1189, 1190, 1192, 1193, 1194, 1195, 1176, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1197, 1200, 1201, 1204, 1205, 1206, 1178, 1182, 1187, 1188, 1195, 1200, 1209, 1176, 1177, 1178, 1179, 1182, 1183, 1187, 1188, 1189, 1199, 1202, 1203, 1204, 1208, 1209, 1175, 1184, 1185, 1186, 1187, 1191, 1192, 1196, 1199, 1200, 1201, 1206, 1207, 1208, 1187, 1188, 1192, 1200, 1201, 1202, 1180, 1183, 1184, 1187, 1188, 1189, 1200, 1201, 1179, 1181, 1182, 1183, 1192, 1200, 1201, 1207, 1180, 1181, 1182, 1183, 1188, 1191, 1192, 1199, 1200, 1201, 1205, 1174, 1176, 1182, 1183, 1184, 1188, 1189, 1192, 1205, 1171, 1173, 1174, 1175, 1176, 1177, 1181, 1182, 1183, 1184, 1185, 1189, 1190, 1199, 1200, 1174, 1175, 1183, 1184, 1192, 1194, 1199, 1200, 1203, 1204, 1170, 1175, 1180, 1183, 1184, 1185, 1188, 1189, 1190, 1191, 1193, 1194, 1196, 1197, 1198, 1202, 1203, 1176, 1179, 1180, 1181, 1176, 1179, 1180, 1194, 1176, 1177, 1178, 1184, 1200, 1176, 1177, 1178, 1179, 1171, 1172, 1176, 1179, 1180, 1181, 1166, 1170, 1171, 1172, 1173, 1176, 1199, 1170, 1171, 1172, 1173, 1179, 1180, 1181, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1174, 1175, 1176, 1177, 1179, 1180, 1181, 1182, 1184, 1187, 1188, 1196, 1197, 1198, 1169, 1184, 1185, 1167, 1173, 1174, 1179, 1180, 1184, 1185, 1189, 1172, 1173, 1180, 1183, 1184, 1183, 1185, 1182, 1183, 1186, 1191, 1173, 1174, 1178, 1180, 1183, 1173, 1191, 1159, 1160, 1163, 1169, 1170, 1172, 1173, 1175, 1176, 1177, 1181, 1182, 1190, 1165, 1176, 1177, 1178, 1179, 1180, 1161, 1162, 1164, 1165, 1169, 1172, 1177, 1178, 1179, 1189, 1157, 1162, 1188, 1168, 1179, 1180, 1182, 1183, 1166, 1174, 1179, 1181, 1182, 1183, 1154, 1157, 1158, 1159, 1164, 1165, 1169, 1170, 1173, 1174, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1165, 1170, 1173, 1174, 1175, 1160, 1165, 1166, 1167, 1168, 1182, 1183, 1176, 1177, 1178, 1152, 1156, 1157, 1158, 1166, 1176, 1177, 1152, 1157, 1167, 1170, 1171, 1172, 1173, 1174, 1175, 1179, 1161, 1165, 1166, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1163, 1164, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1156, 1161, 1162, 1163, 1164, 1165, 1169, 1170, 1176, 1177, 1160, 1161, 1162, 1163, 1164, 1170, 1147, 1148, 1149, 1150, 1151, 1152, 1155, 1156, 1157, 1158, 1159, 1164, 1169, 1170, 1145, 1146, 1156, 1164, 1165, 1166, 1167, 1168, 1170, 1171, 1146, 1155, 1163, 1164, 1165, 1166, 1167, 1168, 1170, 1171, 1145, 1154, 1162, 1163, 1164, 1165, 1166, 1157, 1158, 1159, 1161, 1162, 1163, 1164, 1168, 1170, 1171, 1139, 1142, 1144, 1153, 1154, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1169, 1138, 1146, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1165, 1166, 1168, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1159, 1160, 1161, 1162, 1165, 1136, 1138, 1139, 1143, 1146, 1147, 1148, 1149, 1151, 1152, 1155, 1156, 1158, 1159, 1165, 1166, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1159, 1165, 1134, 1135, 1136, 1137, 1143, 1144, 1148, 1159, 1162, 1133, 1134, 1135, 1139, 1140, 1141, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1160, 1162, 1131, 1132, 1133, 1138, 1139, 1140, 1144, 1145, 1146, 1147, 1148, 1149, 1152, 1153, 1157, 1158, 1159, 1161, 1130, 1131, 1138, 1139, 1140, 1141, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1129, 1130, 1131, 1134, 1135, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1145, 1146, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1147, 1148, 1152, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1143, 1144, 1145, 1146, 1147, 1148]
XY = list(zip(apointx, apointy))
endpoints = [1698.5197802964217, 1913.4034087606117]

XY = [point for point in XY if point[1] > 1120]
res = list(zip(*XY))
apointx = list(res[0])
apointy = list(res[1])

plt.plot(apointx,apointy,'ro')
def func(x, a, b, c, d):
    return a/c*np.sqrt(c**2-((x-b))**2)+d

poptf, pcovf = op.curve_fit(func, apointx, apointy, p0 = (70,1800,120,1120), sigma = None, absolute_sigma = False, method ='lm', nan_policy = 'omit')
pxf = np.arange(min(endpoints), max(endpoints),3)
error = np.sqrt(np.diag(pcovf))
a,b,c,d = poptf
pyf = func(pxf, a,b,c,d)
plt.plot(pxf,pyf,'b-')
plt.text(b,func(min(endpoints),a,b,c,d), '$\\frac{x-%s}{%s}^2+\\frac{y-%s}{%s}^2=1$'%(str(b),str(c),str(d),str(a)),fontsize=8)