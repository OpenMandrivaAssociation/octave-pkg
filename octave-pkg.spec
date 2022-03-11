%define octpkg pkg

# there are not official releases yet.
%global commit	de58aaf2181bdd0ad214b39ee5b7de528268b6dc

Summary:	The GNU Octave package management tool
Name:		octave-%{octpkg}
Version:	1.0.0
Release:	1
Url:		https://github.com/gnu-octave/%{octpkg}
Source0:	%{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
BuildArch:	noarch
BuildRequires:	octave-devel >= 4.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Since Octave is Free Software users are encouraged to share their programs with
others. To aid this sharing Octave supports the installation of extra packages.
At the time of writing a collection of packages can be found online at

  *  the 'Octave Packages' page https://gnu-octave.github.io/packages/
  *  the 'Octave Forge' project https://octave.sourceforge.io

Since the Internetis an ever-changing place this may not be true at the time of
reading. Therefore it is recommended to see the Octave website https://octave.org
for an updated reference.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{commit}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
# NOTE: check fails because actually pkg can't be uninstalled without admin privileges
#octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

