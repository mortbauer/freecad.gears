from setuptools import setup
from pygears import __version__

setup(name='freecad_gears',
      version=str(__version__),
      packages=['freecad_gears','pygears'],
      maintainer="looooo",
      maintainer_email="sppedflyer@gmail.com",
      url="https://github.com/looooo/FCGear",
      description="gears for FreeCAD",
      install_requires=['numpy'],
	  include_package_data=True
)
