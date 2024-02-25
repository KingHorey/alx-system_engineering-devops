# connect to server using the connection string
exec {'ssh_config':
  command => 'echo -e "\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no" >> /ect/ssh/ssh_config',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0, 1],
}
