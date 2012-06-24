Summary:	A Free command-line mp3 player based on smpeg
Summary(pl):	Odtwarzacz mp3 bazuj�cy na smpeg wywo�ywany z linii polece�
Name:		mpg321
Version:	0.2.10
Release:	2
Group:		Applications/Sound
License:	GPL
Source0:	http://prdownloads.sourceforge.net/mpg321/%{name}-%{version}.tar.gz
Patch0:		%{name}-tags.patch
URL:		http://sourceforge.net/projects/%{name}/
BuildRequires:	libao-devel
BuildRequires:	mad-devel
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
mpg321 to klon popularnego odtwarzacza mp3 mpg123. mpg321 powinien by�
doskona�ym zamiennikiem dla mpg123 w wielu prostych przypadkach.
Jednak na razie jest abrdzo prosty, i wiele opcji z linii polece�
mpg123 jest ignorowana. Nie nale�y oczekiwa�, �e ten program b�dzie
b�dzie dzia�a� w ka�dej sytuacji! W szczeg�lno�ci, prawdopodobnie
b�dzie dzia�a� z frontendami (testowane z programem gqmpeg) oraz jako
dekoder mp3 do wav. Na bardzo s�abych systemach prawdopodobnie nie
b�dzie tak wydajny jak mpg123.

%prep
%setup -q
%patch -p1

%build
%configure \
	--disable-mpg123-symlink

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv debian/changelog ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README README.remote THANKS NEWS TODO ChangeLog BUGS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
