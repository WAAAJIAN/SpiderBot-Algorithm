from setuptools import find_packages, setup

package_name = 'gwen'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='spider',
    maintainer_email='wsjasonteh2003@gmail.com',
    description='ROS2 package for our DIY Gwen Spider Hexapod Robot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'stand = gwen.movements.stand : main',
		'maestro = gwen.movements.maestro :main',
		'sit = gwen.movements.sit :main',
		'clockwise = gwen.movements.clockwiseturn :main',
		'anticlockwise = gwen.movements.anticlockwiseturn :main',
		'testing_rotate = gwen.movements.testing_rotate :main'
        ],
    },
)
