Summary:	A Free command-line mp3 player based on smpeg
Summary(pl):	Odtwarzacz mp3 bazuj±cy na smpeg wywo³ywany z linii poleceñ
Name:		mpg321
Version:	0.2.10
Release:	4
Group:		Applications/Sound
License:	GPL
Source0:	http://dl.sourceforge.net/mpg321/%{name}-%{version}.tar.gz
# Source0-md5: bb403b35c2d25655d55f0f616b8f47bb
Patch0:		%{name}-tags.patch
URL:		http://sourceforge.net/projects/mpg321/
BuildRequires:	libao-devel
BuildRequires:	libmad-devel > 0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mpg321 is a clone of the popular mpg123 command-line mp3 player. It
should function as a drop-in replacement for mpg123 in many simple
cases. However, it is currently very simple, and many of the
command-line options of mpg123 are no-ops. Don't expect this program
to work for everything! In particular, it will probably work with
front-ends (tested with gqmpeg) and as a mp3-to-wav decoder. On
lower-end systems it will probably not be as efficient as mpg123,
however.

%description -l pl
mpg321 to klon popularnego odtwarzacza mp3 mpg123. mpg321 powinien byæ
doskona³ym zamiennikiem dla mpg123 w wielu prostych przypadkach.
Jednak na razie jest bardzo prosty, i wiele opcji z linii poleceñ
mpg123 jest ignorowane. Nie nale¿y oczekiwaæ, ¿e ten program bêdzie
bêdzie dzia³aæ w ka¿dej sytuacji! W szczególno¶ci, prawdopodobnie
bêdzie dzia³aæ z frontendami (testowane z programem gqmpeg) oraz jako
dekoder mp3 do wav. Na bardzo s³abych systemach prawdopodobnie nie
bêdzie tak wydajny jak mpg123.

%package mpg123
Summary:	Package to use mpg321 as mpg123 replacement
Summary(pl):	Pakiet pozwalaj±cy u¿ywaæ mpg321 jako zamiennika mpg123
Group:		Applications/Sound
Requires:	%{name} = %{version}
Provides:	mpg123
Obsoletes:	mpg123

%description mpg123
Package to use mpg321 as mpg123 replacement.

%description mpg123 -l pl
Pakiet pozwalaj±cy u¿ywaæ mpg321 jako zamiennika mpg123.

%prep
%setup -q
%patch -p1

%build
%configure

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
%doc AUTHORS README README.remote THANKS NEWS TODO BUGS debian/changelog
%attr(755,root,root) %{_bindir}/mpg321
%{_mandir}/man*/mpg321.1*

%files mpg123
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpg123
%{_mandir}/man*/mpg123.1*
