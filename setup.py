#!/usr/bin/env python3

from setuptools import setup

package_name = 'ds4drv'

setup(name=package_name,
      version="0.5.1",
      description="A Sony DualShock 4 userspace driver for Linux",
      url="https://github.com/chrippa/ds4drv",
      author="Christopher Rosell",
      author_email="chrippa@tanuki.se",
      license="MIT",
      entry_points={
        "console_scripts": ["ds4drv=ds4drv.__main__:main"]
      },
      data_files=[
          ('share/ament_index/resource_index/packages',
              ['resource/' + package_name]),
          ('share/' + package_name, ['package.xml']),
      ],
      packages=["ds4drv",
                "ds4drv.actions",
                "ds4drv.backends",
                "ds4drv.packages"],
      install_requires=["evdev>=0.3.0", "pyudev>=0.16"],
      maintainer='Daniel Hackbarth',
      maintainer_email='da_ha@mailbox.org',
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Games/Entertainment"
      ]
)

