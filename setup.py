from setuptools import setup

package_name = 'rqt_topic'

setup(
    name=package_name,
    version='1.1.0',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource',
            ['resource/TopicWidget.ui']),
        ('share/' + package_name + '/resource/icons/rqt_icons/actions/22',
            ['resource/icons/rqt_icons/actions/22/zoom-in.png',
             'resource/icons/rqt_icons/actions/22/zoom-out.png']),
        ('share/' + package_name + '/resource/icons/rqt_icons',
            ['resource/icons/rqt_icons/index.theme']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dorian Scholz',
    maintainer='Dirk Thomas, Dorian Scholz',
    maintainer_email='dthomas@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'rqt_topic provides a GUI plugin for displaying debug information about ROS ' +
        'topics including publishers, subscribers, publishing rate, and ROS Messages.'
    ),
    license='BSD',
    entry_points={
        'console_scripts': [
            'rqt_topic = ' + package_name + '.main:main',
        ],
    },
)
