import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setuptools.setup(
  name = 'PriceIndices',
  packages = ['PriceIndices'],
  version = '0.1',
  license='MIT',
  description = 'This package can be useful to get historical price data of cryptocurrencies from CoinMarketCap, and calculate & plot different indicators.',
  author = 'Dayal Chand Aichara',
  author_email = 'dc.aichara@gmail.com',
  url = 'https://github.com/dc-aichara/Price-Indices',
  download_url = 'https://github.com/dc-aichara/PriceIndices/archive/0.1.tar.gz',
  keywords = ['Volatility', 'blockchain', 'cryptocurrency', 'Price', 'trading'],
  install_requires=['requests', 'bs4', 'pandas', 'numpy', 'matplotlib'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ],
  long_description=long_description,
  long_description_content_type='text/markdown'
)
