# install flask from pip

package { 'flask':
  provider => 'pip3',
  ensure => '2.1.0'
}
