Summary:	Simple tic-tac-toe game
Summary(pl.UTF-8):	Prosta gra w kółko i krzyżyk
Name:		naughts_and_crosses
Version:	0.83
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.jamyskis.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	6a49a4c569dd44ec4e43e44ab0b21fd2
Patch0:		%{name}-useless_files.patch
URL:		http://www.jamyskis.net/naughts.php
BuildRequires:	allegro-devel >= 4.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple tic-tac-toe game.

%description -l pl.UTF-8
Prosta gra w kółko i krzyżyk.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,ChangeLog,NEWS,README,TODO}
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
