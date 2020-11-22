# Web Infrastructure Design

## Simple web stack
A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack, so design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start having a user wanting to access your website.

### Contains:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

<img src="https://github.com/AlisonQuinter17/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/markdown_multimedia/simple_web_desing.gif" class="responsive"/>

## Distributed web infrastructure 
Desing three server web infrastructure that hosts the website www.foobar.com.

### Contains:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

<img src="https://github.com/AlisonQuinter17/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/markdown_multimedia/distributed.gif" class="responsive"/>
