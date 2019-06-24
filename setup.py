import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setuptools.setup(
  name = 'PriceIndices',
  packages = ['PriceIndices'],
  version = '0.3',
  license='MIT',
  description = 'This package can be useful to get historical price data of cryptocurrencies from CoinMarketCap, and calculate & plot different indicators.',
  author = 'Dayal Chand Aichara',
  author_email = 'dc.aichara@gmail.com',
  url = 'https://github.com/dc-aichara/Price-Indices',
  download_url = 'https://github.com/dc-aichara/PriceIndices/archive/v-0.3.tar.gz',
  keywords = ['Volatility', 'blockchain', 'cryptocurrency', 'Price', 'trading', 'CoinMarketCap'],
  install_requires=['requests', 'pandas', 'numpy', 'matplotlib'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ],
  long_description=long_description,
  long_description_content_type='text/markdown'
)
