Summary:	Browse your SMB shares using a web browser
Summary(pl):	Przegl±danie zasobów dostêpnych poprzez SMB za pomoc± przegl±darki
Name:		smb-network
Version:	1.21
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.dragonsdawn.net/~gordon/smb-network/%{name}-%{version}.tar.gz
# Source0-md5:	7697178abc365eff40d3cd201f778b1e
URL:		http://www.dragonsdawn.net/~gordon/smb-network/
Requires:	webserver
BuildArch:	noarch
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		htmldir		/home/services/httpd/html
%define		cgidir		/home/services/httpd/cgi-bin

%description
This CGI will allow you to browse your SMB network using a web
browser. It it ideal for accessing your shares when you are at a
remote location, and can be used over SSL.

%description -l pl
Ten skrypt CGI umo¿liwia przegl±danie sieci SMB ("Otoczenie sieciowe",
lub "Moje miejsca sieciowe") za pomoc± przegl±darki WWW. ¦wietnie siê
nadaje do uzyskania dostêpu do zasobów bêd±c poza sieci± lokaln±, a w
po³±czeniu z SSL gwarantuje bezpieczeñstwo transmisji.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{htmldir},%{cgidir}}

install smb-network.cgi $RPM_BUILD_ROOT%{cgidir}
cp -a smbicons $RPM_BUILD_ROOT%{htmldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{cgidir}/smb-network.cgi
%{htmldir}/smbicons
