from setuptools import find_packages, setup

package_name = 'drone'

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
    maintainer='alexander',
    maintainer_email='agrawal.alexander@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_drone = drone.arm_drone:main',
            'drone_pose = drone.drone_pose:main',
            'set_throttle_test = drone.set_throttle_test:main',
            'set_alt_test = drone.set_alt_test:main',
            'fake_gps = drone.fake_gps:main',
        ],
    },
)
