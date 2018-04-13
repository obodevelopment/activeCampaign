from setuptools import setup, find_packages

setup(name='activecampaign',
    version='1.0',
    description='ActiveCampaign API Library',
    packages=find_packages(exclude=['test_activecampaign']),
    install_requires=[
        'pytest',
        'requests',
        'simplejson'
    ],
    keywords='activecampaign',
    zip_safe=False,
    license='GPL',
)
