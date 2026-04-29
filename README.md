##MITRE Persistance

This module demonstrates how Windows services can be abused as a persistence mechanism.

### Focus Areas
- Service creation behavior
- Event log artifacts (Event ID 7045)
- Detection opportunities for defenders

### Defensive Notes
- Monitor new service installations
- Alert on services executing from user-writable directories
- Validate service binary signatures
