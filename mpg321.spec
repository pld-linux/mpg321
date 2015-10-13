Summary:	A Free command-line MP3 player based on smpeg
Summary(pl.UTF-8):	Odtwarzacz MP3 bazujący na smpeg wywoływany z linii poleceń
Name:		mpg321
Version:	0.3.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/mpg321/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d3c343d2183e239e4df56a4aae2466a6
Patch0:		%{name}-tags.patch
Patch1:		%{name}-format.patch
URL:		http://sourceforge.net/projects/mpg321/
BuildRequires:	alsa-lib-devel
BuildRequires:	libao-devel
BuildRequires:	libid3tag-devel >= 0.14.1
BuildRequires:	libmad-devel > 0.14
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpg321 is a clone of the popular mpg123 command-line MP3 player. It
should function as a drop-in replacement for mpg123 in many simple
cases. However, it is currently very simple, and many of the
command-line options of mpg123 are no-ops. Don't expect this program
to work for everything! In particular, it will probably work with
front-ends (tested with gqmpeg) and as a MP3-to-WAV decoder. On
lower-end systems it will probably not be as efficient as mpg123,
however.

%description -l pl.UTF-8
mpg321 to klon popularnego odtwarzacza MP3 mpg123. mpg321 powinien być
doskonałym zamiennikiem dla mpg123 w wielu prostych przypadkach.
Jednak na razie jest bardzo prosty, i wiele opcji z linii poleceń
mpg123 jest ignorowane. Nie należy oczekiwać, że ten program będzie
będzie działać w każdej sytuacji! W szczególności, prawdopodobnie
będzie działać z frontendami (testowane z programem gqmpeg) oraz jako
dekoder MP3 do WAV. Na bardzo słabych systemach prawdopodobnie nie
będzie tak wydajny jak mpg123.

%package mpg123
Summary:	Package to use mpg321 as mpg123 replacement
Summary(pl.UTF-8):	Pakiet pozwalający używać mpg321 jako zamiennika mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	mpg123
Obsoletes:	mpg123

%description mpg123
Package to use mpg321 as mpg123 replacement.

%description mpg123 -l pl.UTF-8
Pakiet pozwalający używać mpg321 jako zamiennika mpg123.

%prep
%setup -q -n %{name}-%{version}-orig
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so mpg321.1' > $RPM_BUILD_ROOT%{_mandir}/man1/mpg123.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS README README.remote THANKS TODO
%attr(755,root,root) %{_bindir}/mpg321
%{_mandir}/man1/mpg321.1*

%files mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpg123
%{_mandir}/man1/mpg123.1*
