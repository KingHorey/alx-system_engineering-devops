# connect to server using the connection string

exec { 'ssh':
  command  => 'ssh -i /home/ubuntu/.ssh/school ubuntu@54.144.139.47 -o PasswordAuthentication=no',
  path     => [ '/usr/bin', '/usr/sbin', '/bin' ],
  provider => 'shell',
}
