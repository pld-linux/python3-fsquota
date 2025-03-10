%define		module	FsQuota
Summary:	Interface to file system quotas on UNIX platforms
Name:		python3-fsquota
Version:	0.1.0
Release:	5
License:	GPL v2
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	d741877a2247dd85e6f2daa29dedc111
URL:		https://github.com/tomzox/Python-Quota
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The quota module allows accessing file system quotas on UNIX
platforms. This works both for locally mounted file systems and
network file systems (via RPC, i.e. Remote Procedure Call) for all the
operating systems listed below. The interface is designed to be
independent of UNIX flavours as well as file system types.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* CHANGES README.md
%attr(755,root,root) %{py3_sitedir}/%{module}*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
