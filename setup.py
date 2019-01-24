from setuptools import setup, find_packages

setup(name='postfinance',
      version='0.1',
      python_requires='>=3.6',
      description='PostFinance PSP library',
      url='http://github.com/niespodd/postfinance',
      author='Dariusz Niespodziany',
      author_email='d.niespodziany@gmail.com',
      license='MIT',
      tests_require=["pytest", "pytest-cov", "pytest-pep8", "pytest-mock", "mock"],
      setup_requires=["pytest-runner"],
      packages=find_packages(),
      zip_safe=False)
