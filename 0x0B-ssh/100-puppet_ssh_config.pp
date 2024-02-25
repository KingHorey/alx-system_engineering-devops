# connect to server using the connection string

exec { 'ssh':
  command => 'ssh -i ~/.ssh/school ubuntu@54.144.139.47 PasswordAuthentication=no',
  path    => [ '/usr/bin', '/usr/sbin', '/bin' ],
}
