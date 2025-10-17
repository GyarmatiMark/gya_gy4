from setuptools import setup  # FONTOS: ez kellett, hogy ne dobjon NameError-t

package_name = 'position_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=False,
    maintainer='Te Neved',
    maintainer_email='email@example.com',
    description='Position publisher/subscriber example',
    license='Apache License 2.0',
    # tests_require eltávolítva, mert Python 3.10+ setuptools warningot dobott
    entry_points={
        'console_scripts': [
            'position_publisher = position_pkg.position_publisher:main',
            'position_subscriber = position_pkg.position_subscriber:main',
        ],
    },
)
