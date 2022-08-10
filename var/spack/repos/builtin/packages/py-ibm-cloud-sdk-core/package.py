# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIbmCloudSdkCore(PythonPackage):
    """This project contains core functionality required by
    Python code generated by the IBM Cloud OpenAPI SDK
    Generator (openapi-sdkgen)."""

    homepage = "https://github.com/IBM/python-sdk-core"
    pypi = "ibm-cloud-sdk-core/ibm-cloud-sdk-core-3.9.0.tar.gz"

    version("3.10.0", sha256="ab9520be99066ec41a24e31ac653c28953adc8fc349f0fa53a598e1802a79cd6")
    version("3.9.0", sha256="51403f33003254d83d5028d8cebd7617f5cca82af85b6e9c4ad553eccd079dbf")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-requests@2.20:2", type=("build", "run"))
    depends_on("py-python-dateutil@2.5.3:2", type=("build", "run"))
    depends_on("py-pyjwt@2.0.1:2", type=("build", "run"))
