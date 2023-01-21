from setuptools import setup

package_name = 'mouse_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='grzechu',
    maintainer_email='grzechu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'mouse_subscriber = mouse_pubsub.mouse_subscriber:main',
        	'move_publisher = mouse_pubsub.move_publisher:main',
        	'display = mouse_pubsub.display:main',
        ],
    },
)
