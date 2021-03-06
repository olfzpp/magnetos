# -*- coding: utf-8 -*-
# Created by restran on 2017/7/27
from __future__ import unicode_literals
import sys
import os
from setuptools import setup, find_packages

from magnetos import __version__

kwargs = {
    'packages': find_packages(),
    # 还需要创建一个 MANIFEST.in 的文件，然后将这些数据也放在那里
    'package_data': {
        'magnetos.fuzzing': [
            'data/what_format.dic'
        ],
    }
}

install_requires = [
    'requests',
    'future',
    'validators',
    'mountains',
]

if sys.version_info < (3, 0):
    install_requires.append('futures')

kwargs['install_requires'] = install_requires


if os.path.exists('README.rst'):
    readme_file = 'README.rst'
else:
    readme_file = 'README.md'
# writes converted file
with open(readme_file, 'r') as f:
    long_description = f.read()

setup(
    name='magnetos',  # 文件名
    version=__version__,  # 版本(每次更新上传 pypi 需要修改)
    description="Some hacker scripts.",
    long_description=long_description,  # 放README.md文件，方便在 pypi 页展示
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],  # Get strings from http://pypi.python.org/pypi?:action=list_classifiers
    keywords='python utils',  # 关键字
    author='restran',  # 用户名
    author_email='grestran@gmail.com',  # 邮箱
    url='https://github.com/restran/mountains',  # github上的地址
    license='MIT',  # 遵循的协议
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'what_format = magnetos.fuzzing.what_format:main',
            'what_code_scheme = magnetos.fuzzing.what_code_scheme:main',
            'what_encode = magnetos.fuzzing.what_encode:main',
            'what_steg = magnetos.fuzzing.what_steg:main',
            'file_hash = magnetos.utils.file_hash:main',
            'file_strings = magnetos.utils.file_strings:main',
            'find_ctf_flag = magnetos.utils.find_ctf_flag:main',
            'reverse_proxy = magnetos.proxy.reverse_proxy:main',
            'steg_hide_break = magnetos.cracker.steg_hide_break:main',
        ],
    },
    **kwargs
)
