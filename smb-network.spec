Summary:	Browse your SMB shares using a web browser
Summary(pl):	Przegl±daj zasoby dostêpne poprzez SMB za pomoc± przegl±darki
Name:		smb-network
Version:	1.15
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.dragonsdawn.net/~gordon/smb-network/%{name}-%{version}.tar.gz
URL:		http://www.dragonsdawn.net/~gordon/smb-network/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	webserver
BuildArch:	noarch

%description
This CGI will allow you to browse your SMB network using a web
browser. It it ideal for accessing your shares when you are at a
remote location, and can be used over SSL.

%description -l pl
Ten skrypt CGI umo¿liwia przegl±danie sieci SMB ("Otoczenie sieciowe",
lub "Moje miejsca sieciow") za pomoc± przegl±darki WWW. ¦wietnie siê
nadaje do uzyskania dostêpu do zasobów bêd±c poza sieci± lokaln±, a w
po³±czeniu z SSL gwarantuje bezpieczeñstwo transmisji.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/services/httpd/{cgi-bin,html}

install smb-network.cgi $RPM_BUILD_ROOT/home/services/httpd/cgi-bin
cp -a smbicons $RPM_BUILD_ROOT/home/services/httpd/html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/home/services/httpd/cgi-bin/smb-network.cgi
/home/services/httpd/html/smbicons
