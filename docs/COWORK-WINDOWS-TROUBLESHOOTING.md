# Claude Cowork on Windows — Troubleshooting Guide

> **Last updated:** 2026-02-16
> **Applies to:** Claude Cowork (Research Preview) on Windows 10/11

---

## What is Cowork?

Claude Cowork is Anthropic's desktop AI agent that runs inside the Claude Desktop app. Unlike Claude Code (CLI-based, developer-focused), Cowork connects directly to your local file system and executes multi-step tasks — document creation, file organization, research, spreadsheets — without needing a terminal or GitHub.

Cowork launched on **macOS** in January 2026 and became available on **Windows** on February 10, 2026.

---

## Requirements

| Requirement | Details |
|---|---|
| **OS** | Windows 10 or 11 (x64 only — ARM64 is **not** supported) |
| **Claude Desktop** | Latest version from [claude.com/download](https://claude.com/download) |
| **Subscription** | Pro, Max, Team, or Enterprise plan required |
| **Virtualization** | WSL2 + Virtual Machine Platform must be enabled |
| **Internet** | Active connection required throughout the session |

---

## Common Issues and Fixes

### 1. "Cannot connect to Claude API from workspace"

This is the most widespread Windows issue (see [GitHub #24918](https://github.com/anthropics/claude-code/issues/24918)). Cowork's workspace VM starts but can't reach the API.

**Step-by-step fix:**

1. **Change your DNS to a public provider**
   - Open **Settings → Network & Internet → Wi-Fi** (or Ethernet) **→ Hardware properties → DNS server assignment → Edit**
   - Set:
     - Preferred DNS: `1.1.1.1`
     - Alternate DNS: `8.8.8.8`
   - Or via PowerShell (run as Admin):
     ```powershell
     Set-DnsClientServerAddress -InterfaceAlias "Wi-Fi" -ServerAddresses ("1.1.1.1","8.8.8.8")
     ```
   - Restart Claude Desktop after changing DNS.

2. **Ensure WSL2 is installed and up to date**
   ```powershell
   wsl --install
   wsl --update
   ```
   Reboot after installation.

3. **Enable required Windows features**
   ```powershell
   # Run as Administrator
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   ```
   Reboot after enabling.

4. **Full restart** (not just sleep/wake — do a complete shutdown and power-on)

5. **Check firewall rules**
   - Open **Windows Defender Firewall → Allow an app through firewall**
   - Ensure **Claude** is allowed on both **Private** and **Public** networks
   - If using third-party antivirus (e.g., AhnLab, Kaspersky, Norton), temporarily disable it to test

6. **Reset network stack** (if above steps don't work)
   ```powershell
   # Run as Administrator
   netsh winsock reset
   netsh int ip reset
   ipconfig /flushdns
   ```
   Reboot after running.

---

### 2. "VM service not running"

The virtualization backend that Cowork depends on isn't active.

**Fix:**

1. Verify virtualization is enabled in BIOS/UEFI:
   - Open **Task Manager → Performance → CPU** — look for "Virtualization: Enabled"
   - If disabled, reboot into BIOS and enable **Intel VT-x** or **AMD-V**

2. Ensure Hyper-V or Virtual Machine Platform is running:
   ```powershell
   # Check status
   Get-Service vmcompute | Select-Object Status, Name

   # Start if stopped
   Start-Service vmcompute
   ```

3. On **Windows 11 Home** (no full Hyper-V):
   - You rely on **Virtual Machine Platform** + **Windows Hypervisor Platform**
   - Enable both in **Settings → Apps → Optional Features → More Windows Features**
   - Cowork *should* work on Home edition via WSL2, but it's less stable than Pro/Enterprise

---

### 3. File access restricted to personal folder

Cowork on Windows currently limits file access to your user profile directory (`C:\Users\<YourName>\`).

**Workarounds:**

- Move or symlink project files into your user folder:
  ```powershell
  # Create a symlink from your dev folder into your profile
  New-Item -ItemType SymbolicLink -Path "$HOME\dev-projects" -Target "C:\git"
  ```
- When starting a Cowork session, explicitly grant access to the folder you need via the folder picker in the Cowork UI

---

### 4. Cowork tab not appearing in Claude Desktop

- Ensure you have the **latest version** of Claude Desktop — Cowork on Windows shipped Feb 10, 2026
- Go to [claude.com/download](https://claude.com/download) and reinstall if needed
- Verify your subscription is active (Pro/Max/Team/Enterprise required)

---

### 5. Workspace starts but hangs or times out

- **Proxy/VPN interference:** Disable any VPN or proxy and retry
- **Antivirus sandboxing:** Some antivirus products sandbox new executables — add Claude Desktop to your exclusion list
- **Low resources:** Cowork's VM needs memory. Close unnecessary apps and ensure you have at least 4GB RAM available

---

## Windows 11 Home vs. Pro

| Feature | Home | Pro |
|---|---|---|
| Virtual Machine Platform | Yes | Yes |
| Windows Hypervisor Platform | Yes | Yes |
| Full Hyper-V | **No** | Yes |
| WSL2 | Yes | Yes |
| Cowork support | Partial (more issues reported) | Full |

If you're on **Windows 11 Home** and hitting persistent issues, the root cause is likely the missing full Hyper-V stack. Upgrading to Pro ($99 from Microsoft) resolves most VM-related problems.

---

## Quick Diagnostic Checklist

Run through this list before filing a bug:

- [ ] Claude Desktop is the latest version
- [ ] Paid subscription is active (Pro/Max/Team/Enterprise)
- [ ] Windows is x64 (not ARM64)
- [ ] WSL2 is installed (`wsl --status` shows version 2)
- [ ] Virtual Machine Platform is enabled
- [ ] DNS is set to public resolver (1.1.1.1 / 8.8.8.8)
- [ ] Claude is allowed through Windows Firewall (Private + Public)
- [ ] VPN/proxy is disabled
- [ ] Third-party antivirus is paused or has Claude excluded
- [ ] Full system restart was performed (not sleep/wake)
- [ ] Task Manager shows "Virtualization: Enabled" under CPU

---

## Still Not Working?

1. **Collect logs:**
   - Claude Desktop logs: `%APPDATA%\Claude\logs\`
   - WSL logs: `wsl --status` and `wsl -l -v`

2. **File a bug:**
   - [github.com/anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues)
   - Include: Windows version, edition (Home/Pro), CPU arch, error message, and logs

3. **Related GitHub issues:**
   - [#24918](https://github.com/anthropics/claude-code/issues/24918) — Cannot connect to API (main tracking issue)
   - [#24945](https://github.com/anthropics/claude-code/issues/24945) — VM boots but API unreachable
   - [#24962](https://github.com/anthropics/claude-code/issues/24962) — DNS config / missing NAT
   - [#25024](https://github.com/anthropics/claude-code/issues/25024) — CSP blocks API domain

---

## Alternative: Use Claude Code CLI Instead

If Cowork remains unreliable on your Windows setup, Claude Code (the CLI) is a stable alternative that doesn't require VM infrastructure:

```powershell
# Install via npm
npm install -g @anthropic-ai/claude-code

# Or use directly in VS Code terminal
claude
```

Claude Code uses your terminal directly — no VM, no Hyper-V, no WSL2 dependency for the tool itself. See [docs/SETUP-AND-INSTALLATION.md](./SETUP-AND-INSTALLATION.md) for the full setup guide.

---

## Sources

- [Getting started with Cowork — Claude Help Center](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)
- [Cowork Windows bug report — GitHub #24918](https://github.com/anthropics/claude-code/issues/24918)
- [Anthropic's Claude Cowork lands on Windows — VentureBeat](https://venturebeat.com/technology/anthropics-claude-cowork-finally-lands-on-windows-and-it-wants-to-automate)
- [Claude Cowork Tutorial — DataCamp](https://www.datacamp.com/tutorial/claude-cowork-tutorial)
