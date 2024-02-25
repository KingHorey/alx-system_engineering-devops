# connect to server using the connection string
exec {'ssh_connect':
  command => '/usr/bin/ssh ubuntu@54.236.44.249 -o IdentityFile=/home/ubuntu/.ssh/school PasswordAuthentication=no',
  path    => ['/usr/bin', '/usr/sbin'],
  returns => [0, 1],
}
