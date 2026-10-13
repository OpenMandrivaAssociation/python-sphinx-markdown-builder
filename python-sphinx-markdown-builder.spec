Name:		python-sphinx-markdown-builder
Version:	0.6.11
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-markdown-builder/sphinx_markdown_builder-%{version}.tar.gz
Summary:	A Sphinx extension to add markdown generation support
URL:		https://pypi.org/project/sphinx-markdown-builder/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
A Sphinx extension to add markdown generation support.

%files
%{py_sitedir}/sphinx_markdown_builder
%{py_sitedir}/sphinx_markdown_builder-*.*-info
