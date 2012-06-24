Summary:	A Free command-line mp3 player based on smpeg
Summary(pl):	Odtwarzacz mp3 bazuj�cy na smpeg wywo�ywany z linii polece�.
Name:		mpg321
Version:	0.0.2
Release:	1
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
Copyright:	GPL
Source0:	http://gemini.woot.net/~hosehead/packages/%{name}_%{version}.tar.gz
Patch0:		mpg321-configure.patch
BuildRequires:	libao-devel
BuildRequires:	smpeg-devel
BuildRequires:	SDL-devel >= 1.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpg321 is a clone of the popular mpg123 command-line mp3 player. It should
function as a drop-in replacement for mpg123 in many simple cases. However,
it is currently very simple, and many of the command-line options of
mpg123 are no-ops. Don't expect this program to work for everything!
In particular, it will probably work with front-ends (tested with gqmpeg)
and as a mp3-to-wav decoder. On lower-end systems it will probably not be
as efficient as mpg123, however.                                                                                                           
%description -l pl
mpg321 to klon popularnego odtwarzacza mp3 mpg123. mpg321 powinien by�
doskona�ym zamiennikiem dla mpg123 w wielu prostych przypadkach.

%prep
%setup -q
%patch -p1

%build
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS CREDITS README PROBLEMS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
