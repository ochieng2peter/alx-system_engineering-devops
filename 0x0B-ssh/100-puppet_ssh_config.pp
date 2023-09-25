# Client configuration file (w/ Puppet)

file { '/home/stephen/.ssh/config':
  ensure  => file,
  owner   => 'stephen',
  group   => 'stephen',
  mode    => '0600',
  content => template('~/.ssh/school/ssh_config.erb'),
}
