#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Jasmine
Version  : 2.1.2.0
Release  : 10
URL      : https://pypi.python.org/packages/source/X/XStatic-Jasmine/XStatic-Jasmine-2.1.2.0.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Jasmine/XStatic-Jasmine-2.1.2.0.tar.gz
Summary  : Jasmine 2.1.2 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Jasmine-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Jasmine
--------------
Jasmine JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Jasmine package.
Group: Default

%description python
python components for the XStatic-Jasmine package.


%prep
%setup -q -n XStatic-Jasmine-2.1.2.0

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
