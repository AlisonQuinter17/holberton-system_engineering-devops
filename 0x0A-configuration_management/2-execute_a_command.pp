# Execute a command
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}