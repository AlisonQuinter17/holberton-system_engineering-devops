# Execute a command
exec { 'killmenow':
  command => 'pkill',
  path    => '/usr/bin'
}