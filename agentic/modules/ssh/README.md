# SSH Module

Execute commands and transfer files on remote servers via SSH/SFTP.

## Setup

### Environment Variables

Add to your `.env` file:

```bash
# SSH authentication (at least one required)
SSH_KEY_PATH=/path/to/your/private/key    # Path to SSH private key
SSH_PASSWORD=your_password                 # Or use password auth
```

### Install Dependencies

```bash
pip install paramiko python-dotenv
```

## Usage

Target format: `user@host` or `user@host:port` (default port: 22)

### Execute Commands

```bash
./run modules/ssh/tool/ssh_client.py exec root@192.168.1.50 "ls -la"
./run modules/ssh/tool/ssh_client.py exec admin@server:2222 "df -h"
```

### Upload Files

```bash
./run modules/ssh/tool/ssh_client.py upload root@server local.txt /remote/path/file.txt
./run modules/ssh/tool/ssh_client.py upload root@server ./folder/ /remote/folder/
```

### Download Files

```bash
./run modules/ssh/tool/ssh_client.py download root@server /var/log/syslog ./logs/syslog
./run modules/ssh/tool/ssh_client.py download root@server /etc/nginx/ ./nginx-backup/
```

## Authentication Priority

1. SSH key (if `SSH_KEY_PATH` is set and file exists)
2. Password (if `SSH_PASSWORD` is set)

## Limitations

- Single connection per command (no persistent sessions)
- Does not support jump hosts / bastion servers
- Does not support SSH agent forwarding

## Troubleshooting

**Connection refused**: Check that SSH is running on the target and port is correct.

**Authentication failed**: Verify your key path or password is correct. For key auth, ensure the public key is in the target's `~/.ssh/authorized_keys`.

**Permission denied**: Check file permissions on the remote server.
