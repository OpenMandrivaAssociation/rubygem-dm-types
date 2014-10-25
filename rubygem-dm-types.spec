%define rbname dm-types

Summary:	DataMapper plugin providing extra data types
Name:		rubygem-%{rbname}
Version:	1.2.2
Release:	1
License:	GPLv2+ or Ruby
Group:		Development/Ruby
Url:		http://github.com/datamapper/%{rbname}
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
DataMapper plugin providing extra data types.

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/paranoid
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/paranoid/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

