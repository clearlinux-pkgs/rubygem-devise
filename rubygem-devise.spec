#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-devise
Version  : 3.5.6
Release  : 8
URL      : https://rubygems.org/downloads/devise-3.5.6.gem
Source0  : https://rubygems.org/downloads/devise-3.5.6.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-responders
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-warden

%description
===============================================================================
Some setup you must do manually if you haven't yet:

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n devise-3.5.6
gem spec %{SOURCE0} -l --ruby > rubygem-devise.gemspec

%build
gem build rubygem-devise.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
devise-3.5.6.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/devise-3.5.6.gem
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/CODE_OF_CONDUCT.md
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/Gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/README.md
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/controllers/devise/confirmations_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/controllers/devise/omniauth_callbacks_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/controllers/devise/passwords_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/controllers/devise/registrations_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/controllers/devise/sessions_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/controllers/devise/unlocks_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/controllers/devise_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/helpers/devise_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/mailers/devise/mailer.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/confirmations/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/mailer/confirmation_instructions.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/mailer/password_change.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/mailer/reset_password_instructions.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/mailer/unlock_instructions.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/passwords/edit.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/passwords/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/registrations/edit.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/registrations/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/sessions/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/shared/_links.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/app/views/devise/unlocks/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/config/locales/en.yml
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/devise.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/devise.png
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-3.2-stable
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-3.2-stable.lock
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-4.0-stable
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-4.0-stable.lock
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-4.1-stable
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-4.1-stable.lock
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-4.2-stable
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/gemfiles/Gemfile.rails-4.2-stable.lock
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/controllers/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/controllers/rememberable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/controllers/scoped_views.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/controllers/sign_in_out.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/controllers/store_location.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/controllers/url_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/delegator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/encryptor.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/failure_app.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/activatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/csrf_cleaner.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/forgetable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/lockable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/rememberable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/timeoutable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/hooks/trackable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/mailers/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/mapping.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/authenticatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/confirmable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/database_authenticatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/lockable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/omniauthable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/recoverable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/registerable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/rememberable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/timeoutable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/trackable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/models/validatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/modules.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/omniauth.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/omniauth/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/omniauth/url_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/orm/active_record.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/orm/mongoid.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/parameter_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/parameter_sanitizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/rails/routes.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/rails/warden_compat.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/strategies/authenticatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/strategies/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/strategies/database_authenticatable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/strategies/rememberable.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/test_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/time_inflector.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/token_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/devise/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/active_record/devise_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/active_record/templates/migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/active_record/templates/migration_existing.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/devise/controllers_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/devise/devise_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/devise/install_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/devise/orm_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/devise/views_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/mongoid/devise_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/README
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/controllers/README
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/controllers/confirmations_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/controllers/omniauth_callbacks_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/controllers/passwords_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/controllers/registrations_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/controllers/sessions_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/controllers/unlocks_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/devise.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/markerb/confirmation_instructions.markerb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/markerb/password_change.markerb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/markerb/reset_password_instructions.markerb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/markerb/unlock_instructions.markerb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/simple_form_for/confirmations/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/simple_form_for/passwords/edit.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/simple_form_for/passwords/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/simple_form_for/registrations/edit.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/simple_form_for/registrations/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/simple_form_for/sessions/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/lib/generators/templates/simple_form_for/unlocks/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/script/cached-bundle
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/script/s3-put
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/custom_registrations_controller_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/custom_strategy_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/helper_methods_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/helpers_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/inherited_controller_i18n_messages_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/internal_helpers_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/load_hooks_controller_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/passwords_controller_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/sessions_controller_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/controllers/url_helpers_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/delegator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/devise_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/failure_app_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/generators/active_record_generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/generators/controllers_generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/generators/devise_generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/generators/install_generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/generators/mongoid_generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/generators/views_generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/helpers/devise_helper_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/authenticatable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/confirmable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/database_authenticatable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/http_authenticatable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/lockable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/omniauthable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/recoverable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/registerable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/rememberable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/timeoutable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/integration/trackable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/mailers/confirmation_instructions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/mailers/reset_password_instructions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/mailers/unlock_instructions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/mapping_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/authenticatable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/confirmable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/database_authenticatable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/lockable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/omniauthable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/recoverable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/registerable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/rememberable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/serializable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/timeoutable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/trackable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models/validatable_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/models_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/omniauth/config_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/omniauth/url_helpers_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/orm/active_record.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/orm/mongoid.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/parameter_sanitizer_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/active_record/admin.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/active_record/shim.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/active_record/user.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/active_record/user_on_engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/active_record/user_on_main_app.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/active_record/user_without_email.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/admins/sessions_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/admins_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/application_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/application_with_fake_engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/custom/registrations_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/home_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/publisher/registrations_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/publisher/sessions_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/users/omniauth_callbacks_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/controllers/users_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/helpers/application_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mailers/users/from_proc_mailer.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mailers/users/mailer.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mailers/users/reply_to_mailer.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mongoid/admin.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mongoid/shim.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mongoid/user.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mongoid/user_on_engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mongoid/user_on_main_app.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/mongoid/user_without_email.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/admins/index.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/admins/sessions/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/home/admin_dashboard.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/home/index.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/home/join.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/home/private.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/home/user_dashboard.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/layouts/application.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/users/edit_form.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/users/index.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/users/mailer/confirmation_instructions.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/app/views/users/sessions/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/bin/bundle
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/bin/rails
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/bin/rake
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config.ru
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/boot.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/database.yml
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/environment.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/environments/development.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/environments/production.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/environments/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/initializers/backtrace_silencers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/initializers/devise.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/initializers/inflections.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/initializers/secret_token.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/initializers/session_store.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/config/routes.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/db/migrate/20100401102949_create_tables.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/db/schema.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/lib/shared_admin.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/lib/shared_user.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/lib/shared_user_without_email.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/lib/shared_user_without_omniauth.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/public/404.html
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/public/422.html
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/public/500.html
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_app/public/favicon.ico
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/rails_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/routes_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/support/action_controller/record_identifier.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/support/assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/support/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/support/integration.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/support/locale/en.yml
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/support/mongoid.yml
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/support/webrat/integrations/rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/test_helpers_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/devise-3.5.6/test/test_models.rb
/usr/lib64/ruby/gems/2.3.0/specifications/devise-3.5.6.gemspec
