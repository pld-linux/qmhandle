Summary:	Qmail message queue tool
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
qmHandle is a tool which can be used to manage the qmail message queue. It's
written in Perl (so fully customizable) and much more powerful than qmail-qread
and qmail-qstat. Key features are colored output and the ability to view and
delete messages in the queue.

With this program you can:
 * Read the qmail queue, like you do with the qmail-qread program. However,
   the output of this program is improved over qmail-qread, with the output
   of the message subjects and color capabilities.
 * Print queue statistics, like qmail-qstat, with color capabilities
 * View a message in the queue.
 * Remove one or more messages from the queue.
 * Force qmail to send queued messages immediately.

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
