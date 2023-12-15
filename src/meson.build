sources = files(
        'crypt-util.c'
)
headers = files(
        'crypt-util.h'
)

ifaces = [
  ['accounts-generated', 'org.freedesktop.', 'Accounts'],
  ['accounts-user-generated', act_namespace + '.', 'User'],
]

foreach iface: ifaces
  gdbus_sources = gnome.gdbus_codegen(
    iface[0],
    join_paths(data_dir, iface[1] + iface[2] + '.xml'),
    interface_prefix: iface[1],
    namespace: 'Accounts',
    extra_args: ['--glib-min-required', '2.64'],
  )
  sources += gdbus_sources
  headers += gdbus_sources[1]
endforeach

deps = [
  gio_dep,
  gio_unix_dep,
  crypt_dep,
]

cflags = [
  '-DLOCALSTATEDIR="@0@"'.format(act_localstatedir),
  '-DDATADIR="@0@"'.format(act_datadir),
  '-DSYSCONFDIR="@0@"'.format(act_sysconfdir),
  '-DICONDIR="@0@"'.format(join_paths(act_localstatedir, 'lib', 'AccountsService', 'icons')),
  '-DUSERDIR="@0@"'.format(join_paths(act_localstatedir, 'lib', 'AccountsService', 'users')),
]

libaccounts_shared = static_library(
  'accounts-shared',
  sources: sources,
  include_directories: top_inc,
  dependencies: deps,
  c_args: cflags,
)

libaccounts_shared_dep = declare_dependency(
  sources: headers,
  include_directories: include_directories('.'),
  dependencies: gio_dep,
  link_with: libaccounts_shared,
)

sources = files(
  'daemon.c',
  'extensions.c',
  'main.c',
  'user.c',
  'user-classify.c',
  'util.c',
  'wtmp-helper.c',
)

deps = [
  gio_unix_dep,
  glib_dep,
  libaccounts_shared_dep,
  polkit_gobject_dep,
  json_dep,
]

daemon = executable(
  'accounts-daemon',
  sources,
  include_directories: top_inc,
  dependencies: deps,
  c_args: cflags,
  install: true,
  install_dir: act_libexecdir,
)

subdir('libaccountsservice')
