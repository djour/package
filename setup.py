# -*- coding: UTF-8 -*-
#
from setuptools import setup, find_packages
setup(
    name = "demo",
    version = "0.3",
    packages = find_packages('src'),  # 包含所有src中的包
    package_dir = {'':'src'},   # 告诉distutils包都在src下
    # include_package_data = True, # 包含所有包内文件

    # 包含一部分文件，排除一部分文件
    include_package_data = True,    

    # 排除所有 README.txt
    exclude_package_data = { '': ['README.txt'] },

    package_data = {
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt'],
        # 包含demo包data文件夹中的 *.dat文件
        'demo': ['data/*.dat'],
    },

    # 自动生成脚本
	entry_points = {
        'console_scripts': [
            'foo = demo:test',
            'bar = demo:test',
        ],
        'gui_scripts': [
            'baz = demo:test',
        ],

        # other arguments here...
        'setuptools.installation': [
            'eggsecutable = demo:test',
        ],

        'blogtool.parsers': '.rst = some_module:SomeClass',
        'blogtool.parsers': ['.rst = some_module:a_func'],
    },

    extras_require = dict(reST = "Docutils>=0.3.5"),


)

