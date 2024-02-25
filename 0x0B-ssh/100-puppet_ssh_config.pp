# connect to server using the connection string

# create a file in the server
exec { 'ssh_school':
  command  => 'ssh-keygen -b 4096 -f /home/ubuntu/.ssh/school',
  path     => '/usr/bin:bin',
  provider => 'shell',
  returns  => [0, 1],
}

exec { 'ssh':
  command  => 'ssh -i /home/ubuntu/.ssh/school ubuntu@54.144.139.47 -o PasswordAuthentication=no',
  path     => '/usr/bin:bin',
  provider => 'shell',
  returns  => [0, 1],
}
