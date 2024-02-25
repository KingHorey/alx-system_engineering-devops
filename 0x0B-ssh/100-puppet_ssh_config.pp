# connect to server using the connection string
exec {'ssh_config':
  command => 'echo "	IdentityFile ~/.ssh/school\n	PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0, 1],
}
