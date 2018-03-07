from setuptools import setup


setup(name='ActiveCampaign',
    version='0.1',
    description='ActiveCampaign',
    packages=['activecampaign'],
    install_requires=[
        'pytest',
        'requests',
        'simplejson'
    ],
    keywords='activeCampaign',
    zip_safe=False,
    license='GPL',
)