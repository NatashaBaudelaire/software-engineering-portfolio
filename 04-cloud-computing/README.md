# Cloud Computing Infrastructure

This directory contains cloud computing exercises focused on infrastructure setup, server configuration, and network analysis. These exercises were completed as part of my learning journey in cloud computing and network services.

## Directory Structure

### 📁 apache-setup-testing-cloud-shell
Apache web server setup and testing in cloud environments.

**Content:**
- Apache web server installation and configuration
- Cloud shell environment setup
- Web server testing and validation
- Security configuration basics
- Performance monitoring

### 📁 ftp-server-practice
File Transfer Protocol (FTP) server implementation and management.

**Content:**
- FTP server installation and configuration
- User management and authentication
- File transfer operations
- Security and access control
- Connection troubleshooting

### 📁 http-traffic-capture-analysis
HTTP traffic monitoring, capture, and analysis.

**Content:**
- Network traffic capture tools (tcpdump, Wireshark)
- HTTP protocol analysis
- Request/response inspection
- Performance analysis
- Security monitoring

## Learning Objectives

These exercises cover fundamental cloud computing concepts:

- **Cloud Services**: Understanding cloud platform services
- **Web Server Administration**: Apache configuration and management
- **Network Protocols**: HTTP, FTP, and other network protocols
- **Traffic Analysis**: Network monitoring and debugging
- **Security Basics**: Server security and access control
- **Cloud Shell Usage**: Command-line cloud environment management
- **Performance Monitoring**: Server performance tracking

## Prerequisites

- Cloud platform account (Google Cloud, AWS, Azure, etc.)
- Basic understanding of Linux commands
- Network fundamentals knowledge
- SSH access to cloud instances

## How to Use

### Apache Setup in Cloud Shell

```bash
# Connect to your cloud shell or cloud instance
ssh user@cloud-instance

# Update package manager
sudo apt update

# Install Apache
sudo apt install apache2

# Start Apache service
sudo systemctl start apache2
sudo systemctl enable apache2

# Check status
sudo systemctl status apache2

# Test the web server
curl http://localhost
# or access via public IP in browser
```

### FTP Server Setup

```bash
# Install FTP server (vsftpd example)
sudo apt install vsftpd

# Configure the server
sudo nano /etc/vsftpd.conf

# Start the service
sudo systemctl start vsftpd
sudo systemctl enable vsftpd

# Test FTP connection
ftp localhost
```

### HTTP Traffic Capture

```bash
# Install tcpdump
sudo apt install tcpdump

# Capture HTTP traffic
sudo tcpdump -i eth0 -A 'tcp port 80'

# Or use Wireshark for GUI analysis
sudo apt install wireshark
sudo wireshark
```

## Cloud Platforms

These exercises can be performed on various cloud platforms:

- **Google Cloud Platform**: Cloud Shell, Compute Engine
- **AWS**: EC2 instances, CloudShell
- **Azure**: Azure Cloud Shell, Virtual Machines
- **DigitalOcean**: Droplets
- **Linode**: Virtual machines

## Security Considerations

- Always use SSH key-based authentication
- Configure firewalls appropriately
- Keep software updated
- Use strong passwords or SSH keys
- Disable unused services
- Monitor access logs

## Common Issues

### Connection Problems
- Check firewall rules and security groups
- Verify SSH key configuration
- Ensure services are running
- Check network connectivity

### Service Failures
- Review service logs: `sudo journalctl -u service_name`
- Check configuration files for syntax errors
- Verify port availability
- Review system resources

### Permission Issues
- Use sudo for administrative commands
- Check file and directory permissions
- Verify user group memberships

## Best Practices

- Always backup configurations before making changes
- Use version control for configuration files
- Document setup procedures
- Implement monitoring and logging
- Follow security best practices
- Test in non-production environments first

## Next Steps

After completing these exercises, consider:
- Learning containerization (Docker, Kubernetes)
- Exploring Infrastructure as Code (Terraform, CloudFormation)
- Studying CI/CD pipelines
- Learning about serverless architectures
- Understanding microservices deployment
- Exploring cloud security in depth

## Resources

- [Apache Documentation](https://httpd.apache.org/docs/)
- [vsftpd Documentation](https://security.appspot.com/vsftpd.html)
- [Wireshark Documentation](https://wiki.wireshark.org/)
- [Cloud Platform Documentation](https://cloud.google.com/docs)
