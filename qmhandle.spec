Summary:	qmail message queue tool
Summary(pl)	Narzêdzie do obs³ugi kolejki poczty qmaila
Name:		qmhandle
Version:	1.2.0
Release:	2
Epoch:		0
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-daemontools.patch
# Source0-md5:	0d2b5f1756d7641a8a8054e29e1b9747
URL:		http://qmhandle.sf.net/
Requires:	qmail
Requires:	daemontools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qmHandle is a tool which can be used to manage the qmail message
queue. It's written in Perl (so fully customizable) and much more
powerful than qmail-qread and qmail-qstat. Key features are colored
output and the ability to view and delete messages in the queue.

With this program you can:
 * Read the qmail queue, like you do with the qmail-qread program.
   However, the output of this program is improved over qmail-qread,
   with the output of the message subjects and color capabilities.
 * Print queue statistics, like qmail-qstat, with color capabilities.
 * View a message in the queue.
 * Remove one or more messages from the queue.
 * Force qmail to send queued messages immediately.

%description -l pl
qmHandle jest narzêdziem s³u¿±cym do zarz±dzania kolejk± poczty
qmaila. Zosta³ napisany w Perlu (wiêc jest ca³kowicie konfigurowalny)
i jest znacznie potê¿niejszy ni¿ qmail-qread czy qmail-qstat. Kluczowe
cechy to kolorowe wyj¶cie oraz mo¿liwo¶æ przegl±dania i kasowania
wiadomo¶ci w kolejce.

Program ten umo¿liwia:
 * Odczyt kolejki qmaila, podobnie jak za pomoc± programu qmail-qread.
   Jednak¿e program ten ma nowocze¶niejsze wyj¶cie ni¿ qmail-qread:
   kolorowe i zawieraj±ce tematy listów.
 * Drukowanie statystyk kolejki, podobnie jak w qmail-qstat, ale w
   kolorach.
 * Obejrzenie wiadomo¶ci w kolejce.
 * Usuniêcie jednej lub wiêcej wiadomo¶ci z kolejki.
 * Wymuszenie na qmailu natychmiastowego wys³ania wiadomo¶ci z
   kolejki.

%prep
%setup -q -c
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install qmHandle $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY
%attr(755,root,root) %{_bindir}/*
