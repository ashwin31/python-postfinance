from setuptools import setup, find_packages

setup(name='postfinance',
      version='0.1',
      python_requires='>=3.6',
      description='PostFinance PSP library',
      url='http://github.com/niespodd/postfinance',
      author='Dariusz Niespodziany',
      author_email='d.niespodziany@gmail.com',
      license='MIT',
      classifiers=[
            "Intended Audience :: Financial and Insurance Industry",
            "License :: OSI Approved :: MIT License",
            "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      install_requires=[
            "iso4217"
      ],
      tests_require=[
            "coveralls",
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "mock"
      ],
      setup_requires=["pytest-runner"],
      packages=find_packages(),
      zip_safe=False)
