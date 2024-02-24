# kill a resource

exec {'killmenow':
  command => 'pkill -9 killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/bin',
  provider => 'shell',
  returns => [0, 1],
}
