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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/paranoid
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/support
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/paranoid/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{gem_dir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{gem_dir}/gems/%{rbname}-%{version}/LICENSE
%doc %{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

