%include	/usr/lib/rpm/macros.perl
Summary:	qmail message queue tool
Summary(pl.UTF-8):	Narzędzie do obsługi kolejki poczty qmaila
Name:		qmhandle
Version:	1.2.0
Release:	5.1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/qmhandle/%{name}-%{version}.tar.gz
# Source0-md5:	0d2b5f1756d7641a8a8054e29e1b9747
Patch0:		%{name}-no-diagnostics.patch
Patch1:		%{name}-alarm.patch
URL:		http://qmhandle.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	daemontools
Requires:	qmail >= 1.03-58.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qmHandle is a tool which can be used to manage the qmail message
queue. It's written in Perl (so fully customizable) and much more
powerful than qmail-qread and qmail-qstat. Key features are colored
output and the ability to view and delete messages in the queue.

With this program you can:
 - Read the qmail queue, like you do with the qmail-qread program.
   However, the output of this program is improved over qmail-qread, with
   the output of the message subjects and color capabilities.
 - Print queue statistics, like qmail-qstat, with color capabilities.
 - View a message in the queue.
 - Remove one or more messages from the queue.
 - Force qmail to send queued messages immediately.

%description -l pl.UTF-8
qmHandle jest narzędziem służącym do zarządzania kolejką poczty
qmaila. Został napisany w Perlu (więc jest całkowicie konfigurowalny)
i jest znacznie potężniejszy niż qmail-qread czy qmail-qstat. Kluczowe
cechy to kolorowe wyjście oraz możliwość przeglądania i kasowania
wiadomości w kolejce.

Program ten umożliwia:
 - Odczyt kolejki qmaila, podobnie jak za pomocą programu qmail-qread.
   Jednakże program ten ma nowocześniejsze wyjście niż qmail-qread:
   kolorowe i zawierające tematy listów.
 - Drukowanie statystyk kolejki, podobnie jak w qmail-qstat, ale w
   kolorach.
 - Obejrzenie wiadomości w kolejce.
 - Usunięcie jednej lub więcej wiadomości z kolejki.
 - Wymuszenie na qmailu natychmiastowego wysłania wiadomości z kolejki.

%prep
%setup -q -c
%patch0 -p0
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install qmHandle $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%attr(755,root,root) %{_sbindir}/*
