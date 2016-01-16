#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Term
%define		pnam	ShellUI
%include	/usr/lib/rpm/macros.perl
Summary:	Term::ShellUI - A fully-featured shell-like command line environment
Name:		perl-Term-ShellUI
Version:	0.92
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7a76e73f193ff3a01bdf683bcbb677e
URL:		http://search.cpan.org/dist/Term-ShellUI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::ShellUI uses the history and autocompletion features of
Term::ReadLine to present a sophisticated command-line interface to
the user. It tries to make every feature that one would expect to see
in a fully interactive shell trivial to implement. You simply declare
your command set and let ShellUI take care of the heavy lifting.

This module was previously called Term::GDBUI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Term/*.pm
%dir %{perl_vendorlib}/Text/Shellwords
%{perl_vendorlib}/Text/Shellwords/Cursor.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
